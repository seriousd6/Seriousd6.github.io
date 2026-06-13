"""
BP Article Synthesis — gap-nt-context: NT epistles, persons, practices, and intertestamental
Covers 61 gap articles with priority score 10 from Smith and Nave sources
Topics: NT epistles, NT-era persons and places, NT practices, intertestamental, general concepts

Sources consulted:
  - data/smith/index.json (Smith briefs)
  - data/topical/nave.json (Nave verse lists)
  - data/biblepedia/gaps.json (gap metadata)

Category logic applied:
  - people:   Named individuals in the NT narrative
  - places:   Cities, regions, pools, fields
  - concepts: Epistles, practices, doctrines, themes, virtues, vices
  - events:   Feasts, specific historical occasions

Script: scripts/bp-gap-nt-context.py
Run: python3 scripts/bp-gap-nt-context.py
"""

import json, os

OUT_DIR = 'data/biblepedia/articles'
os.makedirs(OUT_DIR, exist_ok=True)


def load_article(slug):
    path = os.path.join(OUT_DIR, slug + '.json')
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    return None


def save_article(slug, data):
    path = os.path.join(OUT_DIR, slug + '.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)


def merge_article(slug, data):
    # Never overwrite an existing synthesis — idempotent safety
    if load_article(slug) is not None:
        return False
    save_article(slug, data)
    return True


ARTICLES = {
    # ── NT Epistles ─────────────────────────────────────────────────────────
    "ephesians-the-epistle-to-the": {
        "id": "ephesians-the-epistle-to-the",
        "term": "Ephesians, The Epistle to the",
        "category": "concepts",
        "intro": "<p>The Epistle to the Ephesians is one of Paul's \"Prison Epistles,\" written during his first Roman captivity (Acts 28:16) around AD 60–62. Unlike his more polemical letters, Ephesians is elevated and doxological in tone — a sustained meditation on the cosmic purposes of God centered on the church of Jesus Christ. The first three chapters expound the blessings God has bestowed \"in Christ\" (election, redemption, the mystery of Jew and Gentile united in one body) and culminate in a great doxological prayer (Eph. 3:14–21). The final three chapters draw out the ethical and ecclesiological implications: the unity of the body (Eph. 4:1–16), the renewal of individual conduct (Eph. 4:17–5:21), the ordering of households (Eph. 5:22–6:9), and the famous call to put on the whole armor of God (Eph. 6:10–20). The letter's universalist scope and lack of specific local references have led some scholars to propose it was a circular letter sent to multiple churches in the Lycus valley, with Ephesus as one recipient.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "ephesians-the-epistle-to-the"},
        "key_refs": ["Ephesians 1:3", "Ephesians 2:8", "Ephesians 4:4", "Ephesians 6:11"]
    },
    "galatians-the-epistle-to-the": {
        "id": "galatians-the-epistle-to-the",
        "term": "Galatians, The Epistle to the",
        "category": "concepts",
        "intro": "<p>The Epistle to the Galatians is Paul's most polemical letter, written to counter the Judaizing teachers who were insisting that Gentile believers must be circumcised and observe the Mosaic law to be fully saved. Paul composed the letter shortly after his journey through Galatia and Phrygia (Acts 18:23), most likely from Antioch or Corinth in the early 50s AD. The argument unfolds in three movements: a biographical defense of his apostolic authority and gospel (Gal. 1–2), a theological demonstration that justification is by faith alone and not by works of the law (Gal. 3–4), and an ethical appeal to walk by the Spirit rather than by the flesh (Gal. 5–6). The declaration of Galatians 2:16 — that a person is justified by faith in Christ and not by works of the law — became the Reformation's foundational text. The letter also contains the celebrated list of the fruit of the Spirit (Gal. 5:22–23) and the summary of Christian ethics in bearing one another's burdens (Gal. 6:2). Martin Luther called Galatians \"my epistle\" and wrote an influential commentary on it.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "galatians-the-epistle-to-the"},
        "key_refs": ["Galatians 2:16", "Galatians 3:28", "Galatians 5:22", "Galatians 6:2"]
    },
    "james-the-general-epistle-of": {
        "id": "james-the-general-epistle-of",
        "term": "James, The General Epistle of",
        "category": "concepts",
        "intro": "<p>The Epistle of James is a general letter addressed to \"the twelve tribes scattered abroad\" (Jas. 1:1), written most probably by James the brother of the Lord and leader of the Jerusalem church, likely before AD 50 — making it one of the earliest New Testament writings. The letter is intensely practical, drawing heavily on the wisdom tradition of the Old Testament and the teaching of Jesus. James addresses the testing of faith (Jas. 1:2–18), the call to be doers of the word and not hearers only (Jas. 1:22–27), warnings against partiality toward the rich (Jas. 2:1–13), the relationship between faith and works (Jas. 2:14–26), the dangers of the tongue (Jas. 3), conflicts arising from worldly desires (Jas. 4), warnings to the wealthy oppressors (Jas. 5:1–6), and instructions on prayer and confession (Jas. 5:13–20). The famous passage on faith and works (Jas. 2:17–26) has been read alongside Paul's letters as complementary: James attacks presumptuous faith without deeds, while Paul attacks self-justifying deeds without faith.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "james-the-general-epistle-of"},
        "key_refs": ["James 1:2", "James 1:22", "James 2:17", "James 5:16"]
    },
    "john-the-first-epistle-general-of": {
        "id": "john-the-first-epistle-general-of",
        "term": "John, The First Epistle General of",
        "category": "concepts",
        "intro": "<p>The First Epistle of John was written by the apostle John, most likely from Ephesus in the final decades of the first century. It is not a letter in the formal sense — it has no salutation or closing — but a theological treatise addressed to churches facing a proto-Gnostic secession. The secessionists denied that Jesus had come in the flesh (1 John 4:2) and claimed a superior spiritual knowledge that freed them from ethical obligation. John counters on both fronts: God is light and there is no darkness in him (1 John 1:5), requiring that those who know him keep his commandments and love their brothers. The letter offers three recurring \"tests\" of genuine faith: right doctrine (confessing Jesus as Christ come in the flesh), right conduct (obeying his commandments), and right love (loving one another). The thundering declaration of 1 John 4:8 — \"God is love\" — is one of the most cited theological statements in the New Testament. The letter also contains the foundational assurance that the blood of Jesus cleanses from all sin (1 John 1:7) and that believers may know they possess eternal life (1 John 5:13).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "john-the-first-epistle-general-of"},
        "key_refs": ["1 John 1:7", "1 John 4:2", "1 John 4:8", "1 John 5:13"]
    },
    "john-the-second-and-third-epistles-of": {
        "id": "john-the-second-and-third-epistles-of",
        "term": "John, The Second and Third Epistles of",
        "category": "concepts",
        "intro": "<p>The Second and Third Epistles of John are the shortest books in the New Testament, each occupying a single papyrus sheet. Both are written by \"the Elder\" (Greek <em>ho presbyteros</em>), widely identified with the apostle John. Second John is addressed to \"the elect lady and her children,\" most likely a metaphor for a local church and its members. Its central concern is the same as First John: false teachers who deny that Jesus Christ has come in the flesh must not be received into one's home or given a greeting that could be construed as endorsing their teaching (2 John 7–10). Third John is addressed to Gaius, a church member commended for his hospitality to traveling missionaries. The letter rebukes Diotrephes, who refuses to receive the Elder's authority and expels those who show hospitality to the brethren, and commends Demetrius. Together these brief letters illuminate the dynamics of authority, hospitality, and doctrinal discipline in early second-generation Christianity.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "john-the-second-and-third-epistles-of"},
        "key_refs": ["2 John 7", "2 John 10", "3 John 4", "3 John 9"]
    },
    "philemon-the-epistle-of-paul-to": {
        "id": "philemon-the-epistle-of-paul-to",
        "term": "Philemon, The Epistle of Paul to",
        "category": "concepts",
        "intro": "<p>The Epistle to Philemon is Paul's shortest letter and the most personal — a private appeal written from Rome during his first captivity (AD 60–62) to Philemon, a Christian slave-owner in Colossae. Onesimus, Philemon's runaway slave, had encountered Paul in prison and been converted to faith in Christ. Paul is sending Onesimus back and interceding that Philemon receive him \"no longer as a slave, but better than a slave, as a dear brother\" (Philem. 16). Paul's approach is deliberately indirect: he appeals rather than commands, even offering to repay any debt Onesimus owes (Philem. 18–19), while tactfully reminding Philemon that he owes Paul his very soul. The letter has been central to discussions of Paul and slavery: while Paul does not demand emancipation, his framing of the Christian fellowship as one that transcends the slave-owner relationship implied a profound social challenge. The letter's preservation in the canon suggests Philemon did release Onesimus, and early tradition identifies this Onesimus with the bishop of Ephesus of that name mentioned by Ignatius.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "philemon-the-epistle-of-paul-to"},
        "key_refs": ["Philemon 10", "Philemon 16", "Philemon 18", "Philemon 21"]
    },
    "philippians-epistle-to-the": {
        "id": "philippians-epistle-to-the",
        "term": "Philippians, Epistle to the",
        "category": "concepts",
        "intro": "<p>The Epistle to the Philippians was written by Paul from Rome during his first captivity (AD 62–63) to the church at Philippi — the first church he planted in Europe (Acts 16:12–40). The relationship between Paul and the Philippians was uniquely warm; they alone among his churches sent him financial support on multiple occasions (Phil. 4:15–16), and the letter carries a tone of joy and mutual affection throughout. The letter's doctrinal center is the famous Christ-hymn of Philippians 2:5–11, which traces the trajectory of Christ from equality with God through self-emptying incarnation and obedient death on the cross, to exaltation and universal lordship — offered as the model for Christian humility. Paul also warns against Judaizing teachers (Phil. 3:2), shares his own autobiographical renunciation of confidence in the flesh in favor of \"the surpassing worth of knowing Christ Jesus my Lord\" (Phil. 3:8), and commends contentment learned in all circumstances (Phil. 4:11–13). The exhortation to \"rejoice in the Lord always\" (Phil. 4:4) is one of the NT's most celebrated imperatives.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "philippians-epistle-to-the"},
        "key_refs": ["Philippians 2:5", "Philippians 3:8", "Philippians 4:4", "Philippians 4:13"]
    },
    "revelation-of-st.-john": {
        "id": "revelation-of-st.-john",
        "term": "Revelation of St. John",
        "category": "concepts",
        "intro": "<p>The Book of Revelation (Greek <em>Apokalypsis Ioannou</em>) is the final and most visionary book of the New Testament, addressed by a prophet named John to seven churches in the Roman province of Asia during a period of imperial persecution, most likely under Domitian (c. AD 95). The book opens with letters to the seven churches (Rev. 1–3), then unfolds in a series of visions of the heavenly throne room, the seven seals, trumpets, and bowls of judgment, the beast and false prophet, the millennium, and the new heaven and new earth. The central theological assertion is that Jesus Christ — the \"Lamb who was slain\" — holds ultimate sovereignty over all history and will consummate God's purposes in the defeat of evil, the vindication of his suffering saints, and the renewal of creation (Rev. 21–22). Revelation draws heavily on the symbolic language and imagery of the OT prophets, particularly Daniel, Ezekiel, Isaiah, and Zechariah. Interpretive approaches range from preterist (visions fulfilled in the first century) to historicist, idealist, and futurist readings. Its closing promise — \"I am coming soon\" (Rev. 22:20) — has nourished Christian hope across the centuries.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "revelation"},
        "key_refs": ["Revelation 1:1", "Revelation 5:12", "Revelation 19:6", "Revelation 22:20"]
    },
    "thessalonians-first-epistle-to-the": {
        "id": "thessalonians-first-epistle-to-the",
        "term": "Thessalonians, First Epistle to the",
        "category": "concepts",
        "intro": "<p>First Thessalonians is one of Paul's earliest letters, written from Corinth around AD 50–51, just months after he had planted the church at Thessalonica and been driven out by a Jewish mob (Acts 17:1–10). The letter is notable for its warmth — Paul's relationship with the Thessalonians was deeply affectionate — and for its sustained focus on eschatology. Concern about believers who had died before the Lord's return prompted Paul's most detailed description of the resurrection and the parousia: the dead in Christ will rise first, then those alive will be caught up together with them in the clouds to meet the Lord (1 Thess. 4:13–18). Paul stresses that the \"day of the Lord\" will come as a thief in the night for those unprepared (1 Thess. 5:1–11), while urging watchfulness and sobriety. The closing verses contain some of the NT's most compact ethical summaries: \"Rejoice always, pray without ceasing, give thanks in all circumstances\" (1 Thess. 5:16–18), and the call not to quench the Spirit or despise prophecy (1 Thess. 5:19–20).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "thessalonians-first-epistle-to-the"},
        "key_refs": ["1 Thessalonians 4:13", "1 Thessalonians 4:16", "1 Thessalonians 5:2", "1 Thessalonians 5:16"]
    },
    "luke-gospel-of": {
        "id": "luke-gospel-of",
        "term": "Luke, Gospel of",
        "category": "concepts",
        "intro": "<p>The Gospel of Luke is the third of the canonical Gospels, attributed by the unanimous testimony of the early church to Luke — Paul's \"beloved physician\" (Col. 4:14) and traveling companion. Luke addresses his work to Theophilus (Luke 1:3), claiming to have investigated sources carefully to produce an orderly account. Together with Acts, Luke constitutes a two-volume work covering the ministry of Jesus and the expansion of the early church. Luke's Gospel is characterized by its special emphases: the ministry of the Holy Spirit, prayer, the inclusion of women and the marginalized, and the universal scope of salvation. Only Luke records the parables of the Good Samaritan (Luke 10:25–37) and the Prodigal Son (Luke 15:11–32), as well as the infancy narratives featuring Mary's Magnificat (Luke 1:46–55) and Zechariah's Benedictus (Luke 1:68–79). Luke gives special attention to the journey to Jerusalem (Luke 9:51–19:27) and preserves unique resurrection appearances, ending with the Ascension (Luke 24:50–53) that opens Acts.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "luke-gospel-of"},
        "key_refs": ["Luke 1:3", "Luke 4:18", "Luke 10:25", "Luke 15:11"]
    },
    "colossians-the-epistle-to-the": {
        "id": "colossians-the-epistle-to-the",
        "term": "Colossians, The Epistle to the",
        "category": "concepts",
        "intro": "<p>The Epistle to the Colossians was written by Paul during his first Roman captivity (AD 62) to a church he had not personally founded — it was planted by Epaphras, one of his co-workers (Col. 1:7). The occasion was a doctrinal error infiltrating the church, commonly called the \"Colossian heresy,\" which involved angel worship, observance of Jewish ceremonial regulations, and possibly ascetic and mystical practices (Col. 2:16–23). Paul counters by presenting the absolute supremacy and sufficiency of Christ: the great Christ-hymn of Colossians 1:15–20 declares that Christ is the image of the invisible God, the firstborn of all creation, in whom all things were created, and through whom all things are reconciled. Against any philosophy that diminishes Christ, Paul insists that \"in him the whole fullness of deity dwells bodily\" (Col. 2:9). The ethical section (Col. 3–4) draws out the implications: the believer has died and been raised with Christ, and this new identity reshapes all human relationships including household and social duties. Colossians is closely related to Ephesians in both language and theology.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "colossians-the-epistle-to-the"},
        "key_refs": ["Colossians 1:15", "Colossians 2:9", "Colossians 3:1", "Colossians 3:12"]
    },
    "laodiceans": {
        "id": "laodiceans",
        "term": "Laodiceans",
        "category": "concepts",
        "intro": "<p>The Laodiceans were the inhabitants and Christian congregation of Laodicea, a prosperous city of the Lycus valley in the Roman province of Asia. The church at Laodicea receives the most severe of the seven letters in Revelation 3:14–22, addressed by the risen Christ as \"the Amen, the faithful and true witness, the beginning of God's creation.\" The letter rebukes the Laodicean church for being \"lukewarm\" — neither cold nor hot — and threatens to spit them out of his mouth. The self-assessment of the church reflected its city's wealth: \"I am rich and have prospered and need nothing.\" Christ's response is to commend \"gold refined by fire\" (true riches), \"white garments\" (righteousness), and \"eye salve\" (spiritual sight), contrasting with Laodicea's fame for banking, clothing manufacture, and its school of ophthalmology. The closing verse contains the celebrated image of Christ standing at the door and knocking (Rev. 3:20). Colossians 4:16 mentions a letter Paul sent to Laodicea; this lost letter was sought by early scribes and circulated in a spurious Latin version in the Western church.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "laodiceans"},
        "key_refs": ["Colossians 4:16", "Revelation 3:14", "Revelation 3:16", "Revelation 3:20"]
    },
    # ── NT-era Persons ───────────────────────────────────────────────────────
    "james-the-less": {
        "id": "james-the-less",
        "term": "James the Less",
        "category": "people",
        "intro": "<p>James the Less (meaning the younger or smaller in stature, to distinguish him from James the son of Zebedee) was one of the twelve apostles, identified as the son of Alphaeus, also called the son of Clopas (Matt. 10:3; Mark 15:40). The epithet \"the Less\" appears in Mark 15:40 at the crucifixion, where his mother Mary is distinguished from other women at the cross. He is widely identified with James the Lord's brother (Gal. 1:19), who became the leader of the Jerusalem church, wrote the Epistle of James, and presided at the Jerusalem Council (Acts 15:13). If the identification is correct, the phrase \"brother of the Lord\" may mean a half-brother (son of Joseph) or a close cousin, depending on one's interpretation. He was martyred around AD 62, reportedly thrown from the temple pinnacle and then clubbed to death — an event recorded by Josephus (Antiquities 20.9.1) and by Eusebius. His faithful leadership of the Jerusalem church through decades of tension between Jewish Christianity and the growing Gentile mission made him a pivotal figure in the apostolic era.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "james-the-less"},
        "key_refs": ["Matthew 10:3", "Mark 15:40", "Acts 15:13", "Galatians 1:19"]
    },
    "junias": {
        "id": "junias",
        "term": "Junias",
        "category": "people",
        "intro": "<p>Junias (or Junia, the feminine form preferred by modern translators) is a figure greeted by Paul in Romans 16:7 as one who is \"outstanding among the apostles\" and who was \"in Christ before\" Paul. The Greek text reads <em>Iounian</em>, which could be either the accusative of the feminine name Junia or the masculine Junias. The overwhelming consensus of ancient commentators through John Chrysostom read the name as feminine — Junia — and understood the greeting as a notable honor. Modern scholarly debate has largely returned to this reading, interpreting Paul's commendation as identifying Junia as a female apostle in the broader sense of \"messenger\" or \"commissioned missionary.\" She and Andronicus, likely her husband, had shared Paul's imprisonment and belonged to the earliest stratum of Jewish Christianity in Rome. The passage is significant in discussions of women's roles in the earliest church and the range of meanings attached to the term \"apostle\" in NT usage.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "junias"},
        "key_refs": ["Romans 16:7"]
    },
    "barsabbas": {
        "id": "barsabbas",
        "term": "Barsabbas",
        "category": "people",
        "intro": "<p>Barsabbas (Aramaic \"son of the Sabbath\" or \"son of Saba\") is the surname shared by two men in the New Testament. The more prominent is Joseph Barsabbas, also called Justus, who was proposed alongside Matthias to fill the place vacated by Judas Iscariot among the twelve (Acts 1:23). He had been a follower of Jesus from the baptism of John through the ascension, meeting the qualifications set by Peter. The lot fell to Matthias, and Barsabbas disappears from the narrative. A second man named Judas Barsabbas appears in Acts 15:22, where he is selected along with Silas as a leading man among the Jerusalem brothers to carry the decree of the Jerusalem Council to the Gentile churches in Antioch, Syria, and Cilicia. He is described as a prophet (Acts 15:32) who exhorted and strengthened the believers. Both Barsabbas figures illustrate the network of trusted witnesses and emissaries active in the early apostolic community.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "barsabbas"},
        "key_refs": ["Acts 1:23", "Acts 15:22", "Acts 15:32"]
    },
    "candace-or-candace": {
        "id": "candace-or-candace",
        "term": "Candace",
        "category": "people",
        "intro": "<p>Candace (Greek <em>Kandake</em>, meaning \"prince of servants\" or possibly a dynastic title) was the title — not a personal name — given to the queens of Meroe (Upper Nubia/Ethiopia), much as \"Pharaoh\" was the title of the Egyptian rulers. The Candace appears in Acts 8:27 when Philip the Evangelist encounters an Ethiopian court official, the \"treasurer\" (eunuch) of the Candace of Ethiopia, returning from Jerusalem in his chariot while reading the book of Isaiah. Philip explains the passage of Isaiah 53:7–8 to him, and the official believes and is baptized at a pool of water by the roadside. This narrative is significant as one of the earliest conversions of a person of African descent and represents the gospel's geographical and ethnic expansion toward the ends of the earth, fulfilling Acts 1:8. The title Candace is attested in classical writers including Strabo and Pliny, confirming it as a recognized dynastic title of Nubian queens during the Hellenistic and Roman periods.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "candace-or-candace"},
        "key_refs": ["Acts 8:27", "Acts 8:35", "Acts 8:38"]
    },
    "bernice-or-berenice": {
        "id": "bernice-or-berenice",
        "term": "Bernice",
        "category": "people",
        "intro": "<p>Bernice (Greek, \"bringing victory\") was the eldest daughter of Herod Agrippa I (Acts 12:1) and sister of Drusilla and Herod Agrippa II. She appears in Acts 25–26 alongside her brother Agrippa II as a member of the royal court that heard Paul's defense before Festus at Caesarea. After the death of her first husband, her uncle Herod of Chalcis, she returned to live with her brother Agrippa II in circumstances that gave rise to scandalous rumors of an incestuous relationship. She later became the mistress of the Roman Emperor Vespasian and then of his son Titus, who reportedly intended to marry her but sent her away due to Roman public opposition. Her role in Acts 25–26 is that of an observer and evaluator at Paul's hearing; after his defense Agrippa II tells Festus that Paul \"could have been set free\" had he not appealed to Caesar. Bernice represents the complex world of Herodian client royalty navigating between Roman power and Jewish identity.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "bernice-or-berenice"},
        "key_refs": ["Acts 25:13", "Acts 25:23", "Acts 26:30"]
    },
    "caiaphas-or-caiaphas": {
        "id": "caiaphas-or-caiaphas",
        "term": "Caiaphas",
        "category": "people",
        "intro": "<p>Caiaphas (Hebrew meaning uncertain; perhaps \"depression\" or a family name), in full Joseph Caiaphas, served as High Priest of the Jews under the Roman prefects Valerius Gratus and Pontius Pilate, from approximately AD 18 to 36. He was the son-in-law of Annas, the former High Priest who retained great influence, and both are named in Luke 3:2 as the high-priestly authorities at the time of John the Baptist's ministry. Caiaphas presided over the Sanhedrin trial of Jesus and was the instigator of the plot to arrest and execute him (John 11:49–53; Matt. 26:3–5, 57). John records his unwitting prophecy that \"it is better for you that one man should die for the people\" (John 11:50). He also interrogated Peter and John before the Sanhedrin following the healing at the temple gate (Acts 4:6). His tenure as High Priest was unusually long for the period, suggesting skilled political management of his role within the Roman administrative framework. Archaeological confirmation of his family came with the 1990 discovery of an ossuary inscribed with the name \"Joseph son of Caiaphas\" in Jerusalem.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "caiaphas-or-caiaphas"},
        "key_refs": ["Matthew 26:57", "John 11:49", "John 18:13", "Acts 4:6"]
    },
    "genealogy-of-jesus-christ": {
        "id": "genealogy-of-jesus-christ",
        "term": "Genealogy of Jesus Christ",
        "category": "concepts",
        "intro": "<p>The New Testament preserves two genealogies of Jesus: Matthew 1:1–17 and Luke 3:23–38. Matthew opens his Gospel with a descending genealogy from Abraham through David and the royal line of Judah to Joseph, the legal father of Jesus, structured in three sets of fourteen generations as a mnemonic device highlighting the Davidic messianic credentials of Christ. Luke's genealogy ascends from Joseph back through David, Abraham, and ultimately to Adam and God, emphasizing the universality of Christ's significance for all humanity. The two genealogies diverge between David and Joseph, and various solutions have been proposed — the most common being that Matthew traces Joseph's legal lineage while Luke traces Mary's biological ancestry, or that one represents a levirate marriage succession. Both evangelists affirm that Jesus was born of a virgin and that Joseph was his legal but not biological father (Matt. 1:16; Luke 3:23), situating his lineage within the covenant promises made to Abraham and David while maintaining the uniqueness of his birth.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "genealogy-of-jesus-christ"},
        "key_refs": ["Matthew 1:1", "Matthew 1:16", "Luke 3:23", "Luke 3:38"]
    },
    "brethren-of-jesus": {
        "id": "brethren-of-jesus",
        "term": "Brethren of Jesus",
        "category": "concepts",
        "intro": "<p>The \"brethren of Jesus\" refers to a group of men named James, Joseph, Simon, and Judas (Matt. 13:55; Mark 6:3) who are associated with Jesus's family throughout the Gospels and Acts. Three principal interpretations have been proposed: (1) the Helvidian view, held by most Protestants, that these were the natural children of Joseph and Mary born after Jesus; (2) the Epiphanian view, that they were children of Joseph by a prior marriage and thus stepbrothers of Jesus; and (3) the Hieronymian view, most common in Roman Catholicism, that \"brethren\" (Greek <em>adelphoi</em>) here means cousins. The Gospels record that during Jesus's ministry his brothers did not believe in him (John 7:5), but after the resurrection James became the leader of the Jerusalem church and a witness to the risen Christ (1 Cor. 15:7; Gal. 1:19). James wrote the Epistle of James and presided at the Jerusalem Council (Acts 15); Jude likely wrote the Epistle of Jude. Paul refers to meeting \"James the Lord's brother\" on his first visit to Jerusalem (Gal. 1:19), confirming the historical significance of this group in earliest Christianity.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "brethren-of-jesus"},
        "key_refs": ["Matthew 13:55", "John 7:5", "Acts 1:14", "Galatians 1:19"]
    },
    "magi": {
        "id": "magi",
        "term": "Magi",
        "category": "people",
        "intro": "<p>The Magi (Greek <em>magoi</em>; rendered \"wise men\" in the KJV) were learned men from the East who came to Jerusalem following a star to seek the newborn \"king of the Jews\" and worship him (Matt. 2:1–12). Matthew's account does not specify their number or their names — the tradition of three Magi, and the names Caspar, Melchior, and Balthasar, are later developments of Christian tradition. In the OT the Hebrew term from which <em>magi</em> derives appears primarily in Daniel, where the Babylonian magicians are distinguished from Daniel's God-given wisdom (Dan. 1:20; 2:2–13). By the first century, the term was associated with Persian Zoroastrian priests who studied astronomy and astrology. Their arrival in Jerusalem confirms Herod's murderous intent and leads to the slaughter of the innocents, which Matthew reads as fulfilling Jeremiah 31:15. The gifts of gold, frankincense, and myrrh have been interpreted symbolically as signifying kingship, divinity, and mortality (burial ointment). Their worship of the infant Christ and return \"by another route\" to avoid Herod has made the Magi a symbol of Gentile recognition of Israel's Messiah.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "magi"},
        "key_refs": ["Matthew 2:1", "Matthew 2:11", "Matthew 2:12"]
    },
    # ── NT Places ────────────────────────────────────────────────────────────
    "caesarea-philippi": {
        "id": "caesarea-philippi",
        "term": "Caesarea Philippi",
        "category": "places",
        "intro": "<p>Caesarea Philippi was a city at the foot of Mount Hermon, near the principal source of the Jordan River, in the northernmost region of Palestine. Originally called Paneas (after the Greek god Pan, whose grotto and spring were there), it was rebuilt and renamed by the tetrarch Philip — son of Herod the Great — in honor of the Emperor Augustus and himself, to distinguish it from Caesarea on the Mediterranean coast. It appears in the New Testament only in connection with Peter's confession: Jesus led his disciples to \"the region of Caesarea Philippi\" and there asked who people said he was, eliciting Peter's declaration, \"You are the Christ, the Son of the living God\" (Matt. 16:13–16; Mark 8:27–29). The remote location, far from Galilee and Jewish religious centers, may have provided a deliberate setting for this pivotal moment. The city later passed to Agrippa II, who renamed it Neronias in honor of Nero, but the name Paneas has survived as modern Banias.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "caesarea-philippi"},
        "key_refs": ["Matthew 16:13", "Matthew 16:16", "Mark 8:27"]
    },
    "cenchrea-or-cenchrea": {
        "id": "cenchrea-or-cenchrea",
        "term": "Cenchrea",
        "category": "places",
        "intro": "<p>Cenchrea (sometimes spelled Cenchreae; Greek, \"millet\") was the eastern harbor of Corinth, situated on the Saronic Gulf approximately seven miles from the city. It served as the port through which trade flowed between Corinth and the eastern Mediterranean — a significant emporium for the ancient world. Two biblical references place it in the life of Paul: Acts 18:18 records that Paul, near the end of his second missionary journey, had his head shaved at Cenchrea before sailing to Ephesus, apparently fulfilling a Nazirite vow (Num. 6). Romans 16:1–2 introduces Phoebe as \"a deacon of the church at Cenchrea\" — one of the clearest NT references to a woman holding a recognized church office — whom Paul commends to the Roman church as a patron and helper. The existence of a congregation at Cenchrea, distinct from the church in Corinth proper, reflects the rapid spread of Christianity through commercial harbor towns in the first century.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "cenchrea-or-cenchrea"},
        "key_refs": ["Acts 18:18", "Romans 16:1"]
    },
    "potters-field-the": {
        "id": "potters-field-the",
        "term": "Potter's Field, The",
        "category": "places",
        "intro": "<p>The Potter's Field was a piece of ground purchased according to Matthew 27:7 by the chief priests with the thirty pieces of silver returned by Judas Iscariot after his betrayal of Jesus. Because the money was considered \"blood money,\" the priests could not put it into the temple treasury (Matt. 27:6), so they bought the field as a burial place for foreigners — hence it was also called \"the Field of Blood\" or <em>Aceldama</em> (Acts 1:19; Aramaic for \"field of blood\"). Matthew interprets the purchase as fulfilling Jeremiah's prophecy (Matt. 27:9–10, citing Zechariah 11:12–13 under the name Jeremiah). The two accounts differ in detail: in Matthew the priests buy the field after Judas's death; in Acts 1:18–19, Peter's speech implies that Judas himself bought the field with his blood money and died there. The field was traditionally located on the south side of the Hinnom Valley where it meets the Kidron, south of Jerusalem. A monastery stood on the traditional site from at least the Byzantine period.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "potters-field-the"},
        "key_refs": ["Matthew 27:7", "Matthew 27:9", "Acts 1:18", "Acts 1:19"]
    },
    "siloam": {
        "id": "siloam",
        "term": "Siloam",
        "category": "places",
        "intro": "<p>Siloam (Hebrew <em>Shiloach</em>, \"sent\"; Greek <em>Siloam</em>) was a pool on the south-eastern edge of ancient Jerusalem, fed by the waters of the Gihon spring channeled through Hezekiah's tunnel — an engineering work constructed in the late eighth century BC (2 Kings 20:20; 2 Chr. 32:30). Isaiah 8:6 refers to \"the waters of Shiloach that go softly,\" contrasting the gentle waters of God's provision with the overwhelming Assyrian flood. The pool is most prominently featured in John 9:1–11, where Jesus heals a man born blind by making clay with saliva, spreading it on his eyes, and instructing him to wash in the Pool of Siloam. The man obeys, washes, and comes back seeing — provoking an extended confrontation with the Pharisees who question the healing's validity on the sabbath. The pool is also mentioned in Luke 13:4, where Jesus references the tower of Siloam whose collapse killed eighteen people. Archaeological excavations in 2004 uncovered what is believed to be the Second Temple-period pool on the slope of the City of David.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "siloam"},
        "key_refs": ["Isaiah 8:6", "John 9:7", "John 9:11", "Luke 13:4"]
    },
    "cappadocia-cappadocians": {
        "id": "cappadocia-cappadocians",
        "term": "Cappadocia",
        "category": "places",
        "intro": "<p>Cappadocia was a large, high plateau region in the interior of Asia Minor (modern central Turkey), bounded by the Taurus Mountains to the south, Pontus to the north, and Armenia to the east. It became a Roman province in AD 17 under Tiberius. In the New Testament, Cappadocians are listed among the diaspora Jews present in Jerusalem on the Day of Pentecost (Acts 2:9), hearing the apostles' proclamation in their own language. First Peter addresses its epistle to \"the strangers dispersed\" through Pontus, Galatia, Cappadocia, Asia, and Bithynia (1 Pet. 1:1), indicating an early Christian community there. Cappadocia later became one of the most theologically significant regions in early Christianity: the Cappadocian Fathers — Basil of Caesarea, Gregory of Nazianzus, and Gregory of Nyssa — in the fourth century developed the classical Trinitarian theology that was enshrined at the Councils of Nicaea and Constantinople.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "cappadocia-cappadocians"},
        "key_refs": ["Acts 2:9", "1 Peter 1:1"]
    },
    "kenite-the": {
        "id": "kenite-the",
        "term": "Kenite, The",
        "category": "concepts",
        "intro": "<p>The Kenites (Hebrew <em>Qeni</em>, possibly related to <em>qayin</em>, \"smith\" or \"spear\") were a nomadic tribal group associated with the region of Midian and the Sinai peninsula in the Old Testament. Jethro, Moses's father-in-law, was a Midianite priest (Exod. 18:1) who is also called a Kenite (Judg. 1:16), and through him Moses received counsel on judicial administration during the wilderness period. The Kenites apparently traveled with Israel from the wilderness and settled in the Negev (Judg. 1:16). In the time of Deborah and Barak, Heber the Kenite had separated from the main Kenite community and his wife Jael killed Sisera, the Canaanite commander, in her tent (Judg. 4:11–22) — an act celebrated in the Song of Deborah (Judg. 5:24–27). Balaam's oracle in Numbers 24:21–22 names the Kenites and prophesies their eventual destruction by Assyria. Some scholars have proposed that early Israelite religion was influenced by Kenite Yahwism, a hypothesis that remains debated.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "kenite-the"},
        "key_refs": ["Judges 1:16", "Judges 4:11", "Judges 4:17", "Numbers 24:21"]
    },
    # ── NT Practices and Concepts ────────────────────────────────────────────
    "baptism": {
        "id": "baptism",
        "term": "Baptism",
        "category": "concepts",
        "intro": "<p>Baptism (Greek <em>baptisma</em>, from <em>baptizein</em>, \"to dip\" or \"immerse\") is the initiatory rite of the Christian church, commanded by Christ in the Great Commission (Matt. 28:19) and practiced from the Day of Pentecost onward (Acts 2:38, 41). In its NT form it involves application of water in the name of the Father, Son, and Holy Spirit. The rite's background lies in Jewish purification washings and particularly in John the Baptist's baptism of repentance (Matt. 3:6; Luke 3:3), which Jesus himself received at the Jordan River, where the Spirit descended on him and the Father's voice affirmed him (Matt. 3:13–17). Paul's theology of baptism in Romans 6:3–4 connects it with union with Christ in his death, burial, and resurrection — a dying to sin and rising to new life. Colossians 2:12 speaks of being \"buried with him in baptism and raised with him through faith.\" The NT connects baptism with faith, repentance, forgiveness, the gift of the Spirit, and incorporation into the body of Christ (Acts 2:38; 1 Cor. 12:13; Gal. 3:27). The mode (immersion, pouring, sprinkling), subjects (believers only or including infants), and precise theological significance have been matters of ongoing debate across Christian traditions.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "baptism"},
        "key_refs": ["Matthew 28:19", "Acts 2:38", "Romans 6:3", "Colossians 2:12"]
    },
    "lords-day-the": {
        "id": "lords-day-the",
        "term": "Lord's Day, The",
        "category": "concepts",
        "intro": "<p>The Lord's Day (<em>kyriake hemera</em>) appears in Revelation 1:10 as the day on which John received his vision on Patmos — the only NT occurrence of the phrase. From the second century onward, Christian writers (Ignatius, the Didache, Justin Martyr) consistently identify the Lord's Day as Sunday, the first day of the week, the day of Christ's resurrection. The NT evidence for the early church's Sunday practice includes Acts 20:7, where believers at Troas gathered on \"the first day of the week to break bread,\" and 1 Corinthians 16:2, where Paul instructs the Corinthians to set aside a collection \"on the first day of every week.\" The shift from the Jewish Sabbath (seventh day) to Sunday as the primary day of Christian assembly reflects the resurrection as the defining event of the new creation. The theological relationship between the OT Sabbath command and the Christian Lord's Day has been interpreted variously: some see a direct continuity (the Sabbath principle transferred to Sunday), others see discontinuity (the Sabbath command fulfilled in Christ), and others see both rest in Christ and gathered worship on Sunday as interrelated expressions of the same reality.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "lords-day-the"},
        "key_refs": ["Revelation 1:10", "Acts 20:7", "1 Corinthians 16:2"]
    },
    "love-feasts": {
        "id": "love-feasts",
        "term": "Love Feasts",
        "category": "concepts",
        "intro": "<p>Love feasts (Greek <em>agapai</em>) were communal meals held by the early Christian community, apparently distinct from or closely associated with the Lord's Supper. The term appears in the NT in Jude 12, where false teachers are condemned for being \"hidden reefs\" at the agape feasts, and in 2 Peter 2:13 (in some manuscripts). From early Christian sources — Ignatius, Tertullian, and the Didache — it is clear that these communal meals served to feed the poor, demonstrate brotherhood across social divisions, and accompany the celebration of the Eucharist. Paul's rebuke in 1 Corinthians 11:17–34 likely addresses abuses at a combined love feast and Lord's Supper gathering: the wealthy ate their own food and became drunk while the poor went hungry, destroying the communal testimony of the meal. The agape meal subsequently became separated from the eucharistic rite as the church grew and liturgical practice became more formalized. Love feasts represent an important strand of early Christian social practice that expressed the leveling of class distinctions in the body of Christ.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "love-feasts"},
        "key_refs": ["Jude 12", "1 Corinthians 11:20", "1 Corinthians 11:22"]
    },
    "laying-on-of-hands": {
        "id": "laying-on-of-hands",
        "term": "Laying on of Hands",
        "category": "concepts",
        "intro": "<p>The laying on of hands is a symbolic ritual act in both Testaments in which a person places their hands on another to convey blessing, appointment, healing, or the communication of the Spirit. In the OT, the practice accompanied the ordination of the Levites (Num. 8:10), the installation of Joshua as Moses's successor (Num. 27:18–23; Deut. 34:9), and the offering of sacrifices (Lev. 1:4). In the NT, Jesus laid hands on children to bless them (Matt. 19:13–15), on the sick to heal them (Mark 6:5; Luke 4:40), and on blind Bartimaeus (Mark 10:52 implied). The apostles and early church used the laying on of hands in connection with the reception of the Holy Spirit (Acts 8:17–19; 19:6), healing (Acts 9:17; 28:8), and commissioning for ministry (Acts 6:6; 13:3). Paul instructs Timothy in the laying on of hands for ordination to church office (1 Tim. 4:14; 5:22; 2 Tim. 1:6) and lists it as one of the foundational Christian teachings (Heb. 6:2). The practice continues in Christian ordination and anointing for healing in most church traditions.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "laying-on-of-hands"},
        "key_refs": ["Numbers 27:18", "Acts 8:17", "Acts 13:3", "1 Timothy 4:14"]
    },
    "miracles": {
        "id": "miracles",
        "term": "Miracles",
        "category": "concepts",
        "intro": "<p>A miracle in Scripture denotes an extraordinary act of power by which God intervenes directly and visibly in the natural order to accomplish his purposes — an act that transcends ordinary natural causation and serves as a sign of his presence and authority. The OT uses several terms: <em>ot</em> (sign), <em>mofet</em> (wonder), <em>niflaot</em> (marvels). The NT uses <em>semeion</em> (sign), <em>teras</em> (wonder), and <em>dynamis</em> (power). The great clusters of miracles occur at decisive moments of redemptive history: the Exodus plagues and wilderness journey (Exod. 7–17), Elijah and Elisha's ministries (1 Kings 17–2 Kings 6), and supremely the ministry of Jesus and the apostolic age. Jesus's miracles — healing disease, exorcising demons, raising the dead, calming storms, multiplying loaves — are integral to his identity as the Christ and serve as signs that the kingdom of God has arrived (Matt. 12:28; Luke 11:20). John calls them \"signs\" revealing Christ's glory (John 2:11; 20:30–31). Paul's letters testify to miracles in the apostolic churches (1 Cor. 12:10; Gal. 3:5), while Hebrews 2:3–4 grounds their significance as God's testimony to the message of salvation.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "miracles"},
        "key_refs": ["Matthew 12:28", "John 2:11", "John 20:30", "Hebrews 2:4"]
    },
    "beelzebul": {
        "id": "beelzebul",
        "term": "Beelzebul",
        "category": "concepts",
        "intro": "<p>Beelzebul (Greek <em>Beelzeboul</em>; KJV \"Beelzebub\") is a title for a demonic being identified in the New Testament as the ruler of demons and equated with Satan. The name derives from a Canaanite deity — probably Baal-zebul (\"prince Baal\" or \"lord of the exalted abode\"), related to but distinct from the mocking form Baal-zebub (\"lord of flies\") in 2 Kings 1:2–3. In the NT, the Pharisees accuse Jesus of casting out demons by the power of Beelzebul, the prince of demons (Matt. 12:24; Mark 3:22; Luke 11:15). Jesus refutes this by arguing that a kingdom divided against itself cannot stand, and that his exorcisms instead signal the arrival of the kingdom of God (Matt. 12:25–28). He also predicts that if they called the master of the house Beelzebul, they will call his disciples the same (Matt. 10:25). The identification of Beelzebul with Satan as the supernatural ruler of the opposing spiritual realm reflects the NT's consistent picture of Christ's ministry as a conquest of the demonic order.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "beelzebul"},
        "key_refs": ["Matthew 12:24", "Matthew 12:28", "Mark 3:22", "Luke 11:18"]
    },
    "magic-magicians": {
        "id": "magic-magicians",
        "term": "Magic, Magicians",
        "category": "concepts",
        "intro": "<p>Magic and magicians in Scripture denote the practice of attempting to manipulate supernatural forces through incantations, divination, or secret arts, as distinct from reliance on the revealed God of Israel. Egyptian magicians confronted Moses and Aaron during the plagues (Exod. 7:11–12, 22; 8:7, 18–19), initially replicating miracles but ultimately acknowledging their limits before \"the finger of God.\" The Mosaic law strictly prohibited all forms of divination, sorcery, and consultation of spirits (Lev. 19:26, 31; Deut. 18:9–14), and Saul's visit to the witch of Endor illustrates the prohibition's violation (1 Sam. 28). In the New Testament, Simon Magus in Samaria had practiced magic and amazed the people until Philip's preaching led to his conversion — though his subsequent offer to purchase the power of the Spirit exposed a fundamental misunderstanding of grace (Acts 8:9–24). At Ephesus, converts publicly burned their books of magic arts worth fifty thousand pieces of silver (Acts 19:19). The magicians (<em>magoi</em>) of Daniel's court and the magi of Matthew 2 carry different connotations from the forbidden occult practices, operating in the wider ancient world of learned astrology and natural philosophy.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "magic-magicians"},
        "key_refs": ["Deuteronomy 18:10", "Acts 8:9", "Acts 19:19", "Revelation 21:8"]
    },
    "roman-empire": {
        "id": "roman-empire",
        "term": "Roman Empire",
        "category": "places",
        "intro": "<p>The Roman Empire was the dominant political power of the Mediterranean world during the entire New Testament period, providing both the governing framework and the physical infrastructure (the <em>Pax Romana</em> and the road network) within which Christianity spread. The first biblical mention of Rome appears in 1 Maccabees 1:10 (c. 161 BC). Rome absorbed Judea through Pompey's conquest of Jerusalem in 63 BC, after which a succession of client kings (the Herods) and Roman prefects and procurators governed the province. The NT is set entirely within the empire: Jesus was born during Caesar Augustus's census (Luke 2:1), was tried before the Roman prefect Pontius Pilate (John 18:28–38), and was crucified by Roman soldiers. Paul's Roman citizenship (Acts 22:28) gave him legal protections he used repeatedly, and his appeal to Caesar (Acts 25:11) brought him to Rome where he wrote several epistles. Paul's letter to the Romans addresses the church in the empire's capital, and Revelation's symbolic references to \"Babylon\" and the beast are widely understood as coded critiques of Roman imperial power and its demands for emperor worship.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "roman-empire"},
        "key_refs": ["Luke 2:1", "John 18:31", "Acts 25:11", "Romans 13:1"]
    },
    # ── Intertestamental ──────────────────────────────────────────────────────
    "jesus-the-son-of-sirach": {
        "id": "jesus-the-son-of-sirach",
        "term": "Jesus the Son of Sirach",
        "category": "people",
        "intro": "<p>Jesus (Joshua) the son of Sirach was a Jewish scribe and wisdom teacher in Jerusalem who composed the book known as Ecclesiasticus (or the Wisdom of Ben Sira) around 180 BC, during the period between the Testaments. He belongs to the tradition of Israelite wisdom literature, but unlike Proverbs and Job, Ben Sira identifies wisdom explicitly with the Torah of Moses (Sir. 24:23), producing a synthesis of Hellenistic-era wisdom and Jewish covenantal piety. His grandson translated the work from Hebrew into Greek in Egypt around 132 BC, as explained in the book's prologue. The book addresses practical ethics, the fear of God, the praise of famous biblical men (Sir. 44–50), and liturgical hymns. Though not in the Jewish or Protestant canon, Ecclesiasticus is included in the deuterocanonical books of the Catholic and Eastern Orthodox traditions and was widely quoted by early church fathers. Portions of the original Hebrew text were recovered among the Cairo Geniza manuscripts in the late nineteenth century and in the Masada scrolls in the 1960s.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "jesus-the-son-of-sirach"},
        "key_refs": ["Sirach 1:1", "Sirach 24:23", "Sirach 44:1"]
    },
    "judith-the-book-of": {
        "id": "judith-the-book-of",
        "term": "Judith, The Book of",
        "category": "concepts",
        "intro": "<p>The Book of Judith is a deuterocanonical text included in the Catholic and Eastern Orthodox Old Testament but not in the Hebrew Bible or Protestant canon. It tells the story of Judith, a beautiful and devout Jewish widow from the fictional city of Bethulia, who saved her people from the Assyrian general Holofernes during a siege. Presenting herself as a defector, she gained access to Holofernes's tent, intoxicated him with wine at a banquet, and beheaded him with his own sword, causing the Assyrian army to flee in panic. The book is widely recognized as a work of historical fiction or didactic novella rather than straightforward history: it contains numerous anachronisms (confusing Nebuchadnezzar as an Assyrian king ruling from Nineveh; Bethulia is unidentifiable; the timeline conflicts with established history). Scholars date its composition to the Maccabean period (second century BC) as an encouragement to faithful resistance under foreign oppression. The figure of Judith as a model of piety, courage, and national deliverance became influential in later Jewish and Christian art and literature.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "judith-the-book-of"},
        "key_refs": ["Judith 8:1", "Judith 13:8"]
    },
    "purim": {
        "id": "purim",
        "term": "Purim",
        "category": "events",
        "intro": "<p>Purim (Hebrew, \"lots,\" from Akkadian <em>puru</em>, a lot or die) is the annual Jewish festival instituted to commemorate the deliverance of the Jewish people in Persia from the massacre plotted by Haman the Agagite, as narrated in the Book of Esther. Haman cast lots (<em>purim</em>) to determine the most auspicious day on which to destroy the Jews (Esth. 3:7), but the Jewish queen Esther and her cousin Mordecai reversed his decree through Esther's courageous appeal to King Ahasuerus (Xerxes). Purim is observed on the 14th and 15th of Adar (February–March) with the public reading of the entire Book of Esther, feasting, gifts of food to neighbors, charity to the poor, and noisemaking whenever Haman's name is read. Esther 9:20–32 records the institution of the festival and the obligation to celebrate it yearly. Purim is the only Jewish holiday not rooted in the Mosaic law and is not mentioned in the New Testament, though Josephus describes it (Antiquities 11.6.13). It represents the ongoing commemoration of providence preserving the Jewish people in exile.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"smith": "purim"},
        "key_refs": ["Esther 3:7", "Esther 9:26", "Esther 9:28"]
    },
    # ── General Concepts ─────────────────────────────────────────────────────
    "parables": {
        "id": "parables",
        "term": "Parables",
        "category": "concepts",
        "intro": "<p>A parable (Hebrew <em>mashal</em>; Greek <em>parabole</em>, \"comparison\" or \"illustration\") is a short narrative or comparison drawn from everyday life used to illuminate a spiritual or moral truth. The device appears throughout the OT — Jotham's fable of the trees (Judg. 9:7–15), Nathan's story of the ewe lamb (2 Sam. 12:1–6), and Isaiah's song of the vineyard (Isa. 5:1–7) — but it reaches its fullest expression in the teaching of Jesus, who is said to have spoken almost exclusively in parables when addressing the crowds (Matt. 13:34). The Synoptic Gospels preserve about thirty distinct parables of Jesus covering the kingdom of God (the Sower, the Mustard Seed, the Hidden Treasure), judgment (the Ten Virgins, the Sheep and Goats), mercy (the Good Samaritan, the Prodigal Son), prayer (the Importunate Widow), and stewardship (the Talents). When asked why he taught in parables, Jesus quoted Isaiah 6:9–10 — parables both reveal to those given understanding and conceal from those who harden their hearts (Matt. 13:11–17). Each parable typically makes one central point, though allegorical readings have enriched the tradition throughout church history.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "parables"},
        "key_refs": ["Matthew 13:3", "Matthew 13:34", "Luke 8:10", "Luke 15:11"]
    },
    "false-teachers": {
        "id": "false-teachers",
        "term": "False Teachers",
        "category": "concepts",
        "intro": "<p>False teachers are a persistent concern throughout both Testaments, representing those who claim to speak for God but lead God's people astray through distorted doctrine, moral license, or self-serving motives. The OT prophets repeatedly confronted false prophets who spoke peace when God had not spoken peace, predicted events that did not happen, and gave comfort to covenant-breakers (Jer. 23:16–22; Ezek. 13; Deut. 18:20–22). Jesus warned of false prophets in sheep's clothing who are known by their fruits (Matt. 7:15–20) and predicted the rise of false Christs in the last days (Matt. 24:11). The NT epistles give sustained attention to false teachers infiltrating the churches: Paul warns of those who preach \"another gospel\" (Gal. 1:8–9) and predicts that in later times some will depart from the faith following deceiving spirits (1 Tim. 4:1). Second Peter 2 and Jude both address teachers who deny the Master, indulge in licentiousness, and exploit their congregations for financial gain. First John 4:1–3 provides a doctrinal test — confession that Jesus Christ has come in the flesh. The recurring biblical response to false teaching is not tolerance but clear doctrinal definition, church discipline, and the refusal of fellowship with those who corrupt the gospel.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "false-teachers"},
        "key_refs": ["Matthew 7:15", "Galatians 1:8", "2 Peter 2:1", "1 John 4:1"]
    },
    "care": {
        "id": "care",
        "term": "Care",
        "category": "concepts",
        "intro": "<p>Care in Scripture encompasses both the anxious worry that Christ commands his disciples to renounce and the genuine pastoral and personal concern that characterizes love. Jesus's Sermon on the Mount addresses excessive anxiety about food, drink, and clothing with the assurance that the heavenly Father knows his children's needs and that seeking first the kingdom of God is the antidote to worldly anxiety (Matt. 6:25–34). The same teaching is echoed in 1 Peter 5:7: \"Cast all your anxiety on him because he cares for you.\" Paul's profound peace transcends understanding — \"not being anxious about anything\" through prayer and thanksgiving (Phil. 4:6–7). At the same time, Scripture commends genuine care for others as integral to love: Paul speaks of the \"care of all the churches\" weighing daily upon him (2 Cor. 11:28), and the NT repeatedly uses the language of mutual care within the body of Christ (1 Cor. 12:25). The parable of Martha and Mary distinguishes between anxious distraction and the one thing needful — sitting at the Lord's feet (Luke 10:41–42). Care rightly ordered is directed first to God's kingdom and then expressed outward in love for neighbor.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "care"},
        "key_refs": ["Matthew 6:25", "Philippians 4:6", "1 Peter 5:7", "Luke 10:41"]
    },
    "charitableness": {
        "id": "charitableness",
        "term": "Charitableness",
        "category": "concepts",
        "intro": "<p>Charitableness in the biblical sense denotes a generous and benevolent disposition toward others, particularly in judgment and in material giving — a virtue closely related to love (<em>agape</em>) in the New Testament. The OT wisdom literature praises the one who gives to the poor (Prov. 19:17; 22:9), and the Mosaic law made structural provision for the poor through gleaning rights and sabbatical release. Jesus elevated charitable giving above legal obligation: alms given in secret before the Father, not publicly for honor (Matt. 6:2–4), and generosity toward the poor, the stranger, and the enemy as expressions of kingdom citizenship (Matt. 5:42–48). Paul's great poem on love in 1 Corinthians 13 grounds all charitable giving in love — without love, giving away all one's possessions profits nothing (1 Cor. 13:3). The NT also commends charitable judgment: covering a neighbor's fault (Prov. 10:12; 1 Pet. 4:8), thinking the best of others (1 Cor. 13:7), and bearing one another's burdens (Gal. 6:2). Charitableness is thus both an outward disposition of generosity and an inward disposition of goodwill.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "charitableness"},
        "key_refs": ["Matthew 6:3", "1 Corinthians 13:3", "Galatians 6:2", "1 Peter 4:8"]
    },
    "chastity": {
        "id": "chastity",
        "term": "Chastity",
        "category": "concepts",
        "intro": "<p>Chastity in Scripture denotes sexual purity — the faithful ordering of the body and sexual life according to God's design: celibacy outside marriage and faithful monogamy within it. The foundation is laid in the seventh commandment (Exod. 20:14) and the Mosaic laws governing sexual conduct. Proverbs 2:10–19 warns the young man against the adulterous woman with an extended poem on the devastation of sexual immorality. Job models chastity by making a covenant with his eyes not to look at a woman lustfully (Job 31:1). The New Testament grounds sexual ethics in theology: the body is a temple of the Holy Spirit and is for the Lord (1 Cor. 6:13–20), and sexual immorality is therefore not merely a social transgression but a sin against one's own body and against God who indwells it. Paul's repeated catalogues of vices include sexual immorality (<em>porneia</em>) and adultery alongside idolatry and greed (1 Cor. 6:9–10; Gal. 5:19). The call to \"flee sexual immorality\" (1 Cor. 6:18) and the instruction that \"the body is not meant for sexual immorality\" express the positive vision of chastity as freedom for devoted service to God and neighbor.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "chastity"},
        "key_refs": ["Exodus 20:14", "Job 31:1", "1 Corinthians 6:18", "1 Thessalonians 4:3"]
    },
    "loyalty": {
        "id": "loyalty",
        "term": "Loyalty",
        "category": "concepts",
        "intro": "<p>Loyalty in Scripture is expressed through the Hebrew concept of <em>hesed</em> — steadfast love, faithfulness, and covenant commitment — and encompasses both God's unwavering loyalty to his covenant people and the human response of faithful devotion. God's loyalty to his own promises is the theological bedrock of the OT: \"Know therefore that the LORD your God is God, the faithful God who keeps covenant and steadfast love with those who love him\" (Deut. 7:9). Ruth's loyalty to Naomi — \"where you go, I will go\" (Ruth 1:16–17) — has become a defining image of human covenant faithfulness. The NT develops loyalty under the concept of faithfulness (<em>pistis</em>) as both saving trust in God and relational fidelity to other believers. Citizens are called to loyalty to governing authorities (Rom. 13:1; Ezra 6:10), servants to their masters (Tit. 2:9), and all believers to their Lord. The ultimate call on loyalty is absolute — \"No servant can serve two masters\" (Luke 16:13), demanding undivided devotion to God above all competing allegiances.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "loyalty"},
        "key_refs": ["Ruth 1:16", "Deuteronomy 7:9", "Romans 13:1", "Luke 16:13"]
    },
    "lukewarmness": {
        "id": "lukewarmness",
        "term": "Lukewarmness",
        "category": "concepts",
        "intro": "<p>Lukewarmness in Scripture describes a state of spiritual halfheartedness — neither fully committed to God nor fully opposed to him, producing a complacent mediocrity that is more dangerous than outright unbelief because it mimics true faith without the substance. The most vivid NT expression is Christ's rebuke of the Laodicean church in Revelation 3:15–16: \"I know your works: you are neither cold nor hot. Would that you were either cold or hot! So, because you are lukewarm, and neither hot nor cold, I will spit you out of my mouth.\" The OT prophets gave analogous warnings: Hosea 6:4 compared Israel's love to morning mist that quickly evaporates, and Ezekiel 16:30 diagnosed the same inconstancy. Jesus warned that those who are \"almost persuaded\" fall short, and James indicts the double-minded man as unstable in all his ways (Jas. 1:6–8). The antidote prescribed in Revelation 3:18–19 is repentance — buying true gold from Christ, accepting his discipline, and opening the door to him in renewed communion. Lukewarmness is presented throughout Scripture as the spiritual condition most resistant to self-diagnosis.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "lukewarmness"},
        "key_refs": ["Revelation 3:15", "Revelation 3:16", "Hosea 6:4", "James 1:8"]
    },
    "remorse": {
        "id": "remorse",
        "term": "Remorse",
        "category": "concepts",
        "intro": "<p>Remorse in Scripture denotes the painful awareness of one's guilt and the distress that follows recognized sin — distinguished from true repentance by whether it leads to turning toward God or spiraling into despair. The Psalms of David — especially Psalm 31, 38, and 51 — express profound remorse over sin: \"my bones wasted away through my groaning all day long\" (Ps. 32:3), \"I am burdened and utterly bowed down\" (Ps. 38:6). This anguish over sin is presented as the proper ground of repentance and the approach to God's mercy. In the New Testament, Paul distinguishes between \"godly grief\" that produces repentance leading to salvation and \"worldly grief\" that produces death (2 Cor. 7:10). Judas Iscariot illustrates worldly grief — he felt remorse, returned the silver, and declared Jesus's innocence, but went and hanged himself (Matt. 27:3–5) rather than seeking forgiveness. Peter's weeping after his denial (Luke 22:62) stands as the contrasting example: remorse that became the doorway to restoration (John 21:15–17). Genuine remorse is thus not to be suppressed but to be redirected toward the mercy of God.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "remorse"},
        "key_refs": ["Psalms 51:1", "2 Corinthians 7:10", "Matthew 27:3", "Luke 22:62"]
    },
    "responsibility": {
        "id": "responsibility",
        "term": "Responsibility",
        "category": "concepts",
        "intro": "<p>Responsibility in Scripture is grounded in the accountability of moral agents before God — the conviction that persons are answerable for their actions because they possess rational will and live under divine law. The early chapters of Genesis establish the pattern: when Adam and Eve sin, God questions them and they shift blame (Gen. 3:12–13), but God holds each accountable in the judgments that follow. The OT wisdom tradition repeatedly affirms individual responsibility: \"The soul who sins shall die\" (Ezek. 18:4) counters the fatalistic proverb about sour grapes (Ezek. 18:2), insisting each generation is accountable for its own deeds. The NT deepens this by presenting all humanity as accountable before God (Rom. 3:19; 14:12), while simultaneously teaching that greater knowledge brings greater responsibility: \"Everyone to whom much was given, of him much will be required\" (Luke 12:48). Stewardship parables (Matt. 25:14–30) develop the theme of accountability for entrusted gifts. The ultimate horizon of responsibility is the last judgment, where each person will give account for every careless word (Matt. 12:36) and every deed, whether good or evil (2 Cor. 5:10; Rev. 20:12).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "responsibility"},
        "key_refs": ["Ezekiel 18:4", "Luke 12:48", "Romans 14:12", "2 Corinthians 5:10"]
    },
    "revenge": {
        "id": "revenge",
        "term": "Revenge",
        "category": "concepts",
        "intro": "<p>Revenge — the act of retaliating against a wrongdoer for personal injury or satisfaction — is consistently condemned in Scripture as an overstepping of human authority into a domain reserved for God. The foundational prohibition is Leviticus 19:18: \"You shall not take vengeance or bear a grudge against the sons of your own people, but you shall love your neighbor as yourself.\" Proverbs 24:29 warns against repaying evil for evil, and Proverbs 20:22 counsels waiting on God's vindication rather than taking matters into one's own hands. Paul applies this principle comprehensively in Romans 12:17–21: \"Repay no one evil for evil,\" and \"Vengeance is mine, I will repay, says the Lord\" (citing Deut. 32:35). Instead, believers are commanded to feed an enemy who is hungry and give drink to one who is thirsty. Jesus extends the prohibition to the inner life — the heart disposition of wishing evil on those who wrong us (Matt. 5:38–44) — and commands loving enemies and praying for persecutors. The restraint of revenge is grounded theologically in the conviction that God is a righteous judge whose vindication of the wronged is certain (Rev. 6:9–11).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "revenge"},
        "key_refs": ["Leviticus 19:18", "Romans 12:19", "Matthew 5:39", "Proverbs 24:29"]
    },
    "revivals": {
        "id": "revivals",
        "term": "Revivals",
        "category": "concepts",
        "intro": "<p>Revivals in biblical usage describe those seasons of spiritual renewal and corporate return to God in which previously cold or faithless communities are restored to active devotion, repentance, and covenant obedience. The OT records several such renewals: Hezekiah's reform (2 Kings 18:1–8), Josiah's covenant renewal upon the discovery of the Book of the Law (2 Kings 22–23), Ezra's reform of the returned exiles (Ezra 9–10; Neh. 8–9), and the preaching of Jonah at Nineveh (Jonah 3). The prophets looked forward to a great eschatological outpouring: Joel 2:28–32 predicted the pouring out of God's Spirit on all flesh, a prophecy cited by Peter at Pentecost (Acts 2:16–21). The Day of Pentecost itself, with three thousand converted in a single day (Acts 2:41), stands as the paradigmatic NT revival. Habakkuk 3:2 captures the posture of the revived heart: \"LORD, I have heard your speech, and I was afraid. O LORD, revive your work in the midst of the years.\" Scripture consistently depicts revival as a sovereign work of the Spirit (Isa. 32:15; Ezek. 37:1–14) that produces visible fruits of repentance, restored worship, social justice, and missionary expansion.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "revivals"},
        "key_refs": ["Habakkuk 3:2", "Joel 2:28", "Acts 2:41", "Isaiah 32:15"]
    },
    "selfishness": {
        "id": "selfishness",
        "term": "Selfishness",
        "category": "concepts",
        "intro": "<p>Selfishness — placing one's own interests, comfort, and advancement above the well-being of others — is treated throughout Scripture as a fundamental expression of fallen human nature and a denial of the love commanded by God. Cain's refusal of responsibility for his brother (Gen. 4:9) and the self-serving choices that recur through Israel's history reflect the pattern of radical self-concern that Scripture diagnoses as the root of much sin. Proverbs indicts the one who withholds grain in time of famine (Prov. 11:26) and the man who takes all the gleaning for himself. The NT makes self-denial explicit as a mark of discipleship: Jesus commands taking up the cross and losing one's life as the path to finding it (Matt. 16:24–25). Paul grounds unselfishness in the Christ-hymn of Philippians 2:3–5: \"Do nothing from selfish ambition or conceit, but in humility count others more significant than yourselves. Let each of you look not only to his own interests, but also to the interests of others. Have this mind among yourselves, which is yours in Christ Jesus.\" The selflessness of Christ in emptying himself is the theological basis and model for the Christian's renunciation of self-seeking.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "selfishness"},
        "key_refs": ["Genesis 4:9", "Matthew 16:24", "Philippians 2:3", "Romans 15:1"]
    },
    "self-delusion": {
        "id": "self-delusion",
        "term": "Self-Delusion",
        "category": "concepts",
        "intro": "<p>Self-delusion — the false assessment of one's own spiritual state, merit, or wisdom — is treated throughout Scripture as a particular danger because it is immune to easy correction. The rich fool of Luke 12:16–21 congratulates himself on his abundance while his soul stands under judgment. The Pharisee of Luke 18:11–12 thanks God for his superiority to others. The church at Laodicea says \"I am rich, I have prospered, and I need nothing,\" unaware that it is \"wretched, pitiable, poor, blind, and naked\" (Rev. 3:17). Proverbs repeatedly warns against the self-reliant: \"There is a way that seems right to a man, but its end is the way of death\" (Prov. 14:12; 16:25). The prophets pronounced judgment on those who said \"peace, peace\" when there was no peace (Jer. 6:14; 8:11) — a collective form of self-delusion. James 1:22–26 identifies the danger of hearing the word without doing it as a form of self-deception, like a man who looks in a mirror and immediately forgets what he looks like. The antidote throughout Scripture is honest self-examination before God, prayer for revealed self-knowledge (Ps. 139:23–24), and submission to correction from the Word and godly counsel.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "self-delusion"},
        "key_refs": ["Proverbs 14:12", "Luke 12:19", "Revelation 3:17", "James 1:22"]
    },
    "walking": {
        "id": "walking",
        "term": "Walking",
        "category": "concepts",
        "intro": "<p>Walking is used throughout Scripture as a primary metaphor for the moral and spiritual life — the steady, daily progress of one's conduct along a path determined by one's commitments and character. The Psalter opens with the image of the blessed person who does not \"walk in the counsel of the wicked\" (Ps. 1:1). Deuteronomy repeatedly uses \"walking in God's ways\" as the comprehensive summary of covenant obedience (Deut. 5:33; 8:6; 10:12; 28:9). The prophet Micah's summary of the moral demand — \"to do justice, and to love kindness, and to walk humbly with your God\" (Mic. 6:8) — is among the OT's most celebrated ethical summaries. In the New Testament, Paul employs the Hebrew idiom extensively: believers are to \"walk by the Spirit\" (Gal. 5:16, 25), \"walk in love\" (Eph. 5:2), \"walk in the light\" (1 John 1:7), and \"walk in a manner worthy of the Lord\" (Col. 1:10). Enoch and Noah are described as those who \"walked with God\" (Gen. 5:22, 24; 6:9), setting the paradigmatic image of a life oriented entirely toward God. The metaphor captures the persistent, forward-moving, habitual quality of sanctified life.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "walking"},
        "key_refs": ["Psalms 1:1", "Micah 6:8", "Galatians 5:16", "Colossians 1:10"]
    },
    "trouble": {
        "id": "trouble",
        "term": "Trouble",
        "category": "concepts",
        "intro": "<p>Trouble in Scripture encompasses the full range of human distress — affliction, hardship, anxiety, bereavement, persecution, and suffering — and is treated as an inevitable dimension of life in a fallen world that God's people navigate by faith and prayer. Jesus directly addresses worry and anxiety in the Sermon on the Mount (Matt. 6:25–34), commanding his disciples not to be anxious about life's necessities, since the heavenly Father knows their needs. His final discourse includes the assurance \"In the world you will have tribulation. But take heart; I have overcome the world\" (John 16:33). Psalm 46 offers the classic OT reassurance: \"God is our refuge and strength, a very present help in trouble\" (Ps. 46:1). Paul teaches that afflictions produce endurance, character, and hope (Rom. 5:3–4) and describes his own sufferings as preparation for eternal glory (2 Cor. 4:17). The NT consistently reframes trouble not as evidence of divine abandonment but as a crucible for sanctification, a sharing in Christ's sufferings (Phil. 3:10; 1 Pet. 4:13), and an occasion for God's comfort to flow through his people to others (2 Cor. 1:3–5).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "trouble"},
        "key_refs": ["Psalms 46:1", "John 16:33", "Romans 5:3", "2 Corinthians 4:17"]
    },
    "procrastination": {
        "id": "procrastination",
        "term": "Procrastination",
        "category": "concepts",
        "intro": "<p>Procrastination — the delay of what ought to be done immediately — is treated in Scripture as a particular danger in spiritual matters, since it assumes a future that God has not promised and may harden the heart against the urgency of repentance and decision. Proverbs 27:1 warns against boasting of tomorrow, \"for you do not know what a day may bring.\" Exodus 22:29 forbids delay in offering the firstfruits, establishing the pattern that God's claims are not to be deferred. Ezekiel 11:2–3 condemned those who said \"the time is not near\" — a false sense of spiritual leisure in the face of judgment. In the NT, the urgency of response to the kingdom's arrival is a dominant theme: \"Now is the acceptable time; behold, now is the day of salvation\" (2 Cor. 6:2). The parable of the rich young ruler illustrates procrastination's cost — he went away sorrowful rather than deciding immediately (Matt. 19:22). Felix the governor, moved by Paul's preaching, deferred: \"When I find it convenient, I will call for you\" (Acts 24:25). James 4:13–14 punctures the illusion of time by asking \"What is your life? For you are a mist that appears for a little time and then vanishes.\"</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "procrastination"},
        "key_refs": ["Proverbs 27:1", "2 Corinthians 6:2", "Acts 24:25", "James 4:14"]
    },
    "knowledge": {
        "id": "knowledge",
        "term": "Knowledge",
        "category": "concepts",
        "intro": "<p>Knowledge in Scripture encompasses both intellectual understanding of God's revelation and the intimate experiential knowing that characterizes a covenantal relationship with God. The Hebrew <em>yada</em> carries both cognitive and relational dimensions — Adam \"knew\" his wife (Gen. 4:1) and Israel was called to \"know\" the LORD (Hos. 6:6). The tree of the knowledge of good and evil (Gen. 2:9, 17) represents the forbidden appropriation of moral autonomy, the desire to determine good and evil independently of God. Proverbs places the fear of the LORD as the beginning of knowledge (Prov. 1:7) and wisdom, establishing that true knowledge is not merely factual but covenantally ordered. In the NT, Paul warns against the puffed-up \"knowledge\" that destroys weaker believers (1 Cor. 8:1–3) while praising the knowledge of God that surpasses all understanding and unites believers to Christ. John's Gospel uses <em>ginoskein</em> (to know) for the mutual indwelling of the Father, Son, and believer (John 10:14–15; 17:3). Paul's great prayer is that believers \"may know him\" (Phil. 3:10), treating this as the supreme goal of the Christian life. False knowledge — Gnosticism — is opposed in 1 Timothy 6:20 and 1 John 4.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "knowledge"},
        "key_refs": ["Proverbs 1:7", "Hosea 6:6", "1 Corinthians 8:1", "Philippians 3:10"]
    },
    "lending": {
        "id": "lending",
        "term": "Lending",
        "category": "concepts",
        "intro": "<p>Lending in Scripture is regulated by law and shaped by the principle that the needy neighbor has a claim on the generosity of the more prosperous. Mosaic law prohibited charging interest to a fellow Israelite in need (Exod. 22:25–27; Lev. 25:35–37; Deut. 23:19–20), while interest could be charged to foreigners. Deuteronomy 15:1–11 required debts to fellow Israelites to be released every seventh year and condemned the hard heart that refused to lend as the release year approached. The Psalter commends the righteous man who \"lends generously\" and is gracious (Ps. 112:5). Jesus radicalized lending by demanding generosity without expectation of return: \"Lend, expecting nothing in return, and your reward will be great, and you will be sons of the Most High\" (Luke 6:35). The parable of the unforgiving servant (Matt. 18:23–35) frames forgiveness of debt as the model for interpersonal forgiveness. Paul's instruction that believers \"owe no one anything, except to love each other\" (Rom. 13:8) creates a spiritual reframing of debt in which love is the perpetual obligation that cannot be discharged.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "lending"},
        "key_refs": ["Exodus 22:25", "Deuteronomy 15:7", "Psalms 112:5", "Luke 6:35"]
    },
    "leaven-yeast": {
        "id": "leaven-yeast",
        "term": "Leaven (Yeast)",
        "category": "concepts",
        "intro": "<p>Leaven (Hebrew <em>chametz</em>; Greek <em>zyme</em>; yeast) is a fermenting agent that permeates and transforms the whole lump of dough and carries dual symbolic weight in Scripture — sometimes representing the hidden, permeating power of the kingdom of God and sometimes representing the corrupting influence of sin and false teaching. Its most foundational use is the unleavened bread of Passover (Exod. 12:15–20; 13:7), where the urgent departure from Egypt left no time for bread to rise; henceforth unleavened bread (<em>matzah</em>) marked the Feast of Unleavened Bread as a commemoration of the Exodus and a ritual removal of the old leaven. Paul applies this symbolism to the Christian community: \"Cleanse out the old leaven that you may be a new lump\" (1 Cor. 5:7–8), calling for the removal of moral corruption from the congregation. Leaven also represents false teaching: Jesus warns against \"the leaven of the Pharisees and Sadducees\" (Matt. 16:6–12) and Paul warns that \"a little leaven leavens the whole lump\" (Gal. 5:9). Yet in Matthew 13:33 Jesus uses the same leaven as an image of the kingdom of God growing imperceptibly but pervasively through the world — showing that context determines whether the metaphor is positive or negative.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "leaven-yeast"},
        "key_refs": ["Exodus 12:15", "Matthew 13:33", "Matthew 16:6", "1 Corinthians 5:7"]
    },
    "lot-the": {
        "id": "lot-the",
        "term": "Lot, The",
        "category": "concepts",
        "intro": "<p>The lot (Hebrew <em>goral</em>; Greek <em>kleros</em>) was an instrument of decision-making in the ancient world in which small stones, sticks, or marked tokens were cast to determine an outcome — comparable to dice — but in Israel its use was governed by the theological conviction that the LORD determines its result: \"The lot is cast into the lap, but its every decision is from the LORD\" (Prov. 16:33). The OT employs lots extensively for distributing the promised land among the tribes (Josh. 14–21), for identifying Achan's sin (Josh. 7:14–18), for selecting Saul as king (1 Sam. 10:20–21), and for distributing priestly and Levitical duties (1 Chr. 24–26; Neh. 10:34). Jonah's lot identified him as the source of the storm (Jon. 1:7). In the NT, Roman soldiers cast lots for Jesus's garments (Matt. 27:35; fulfilling Ps. 22:18), and the apostles cast lots to select Matthias as the twelfth apostle (Acts 1:26) — the last recorded biblical use of the lot. After Pentecost and the gift of the Spirit, the lot disappears from NT practice, suggesting that direct spiritual discernment superseded it as a method of divine guidance in the church.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "lot-the"},
        "key_refs": ["Proverbs 16:33", "Joshua 14:2", "Matthew 27:35", "Acts 1:26"]
    },
    "boasting": {
        "id": "boasting",
        "term": "Boasting",
        "category": "concepts",
        "intro": "<p>Boasting in Scripture is treated with sharp ambivalence: boasting in oneself, one's accomplishments, or one's wisdom is consistently condemned as pride and self-deception, while boasting in the LORD is commended as the proper response to his grace and power. Proverbs 25:14 compares the man who boasts of gifts he does not give to clouds and wind without rain, and Proverbs 27:1 warns against boasting of tomorrow. Isaiah 10:15 mocks the Assyrian's self-glorying: \"Shall the axe boast over him who hews with it?\" Jeremiah 9:23–24 provides the locus classicus: \"Let not the wise man boast in his wisdom, let not the mighty man boast in his might, let not the rich man boast in his riches, but let him who boasts boast in this, that he understands and knows me.\" Paul quotes this passage in 1 Corinthians 1:31 and 2 Corinthians 10:17 to ground his own rhetorical strategy: he boasts only of weaknesses through which the power of Christ is made perfect (2 Cor. 11:30; 12:9), and he counts all his personal credentials \"loss\" compared to knowing Christ (Phil. 3:7–8). The cross eliminates all grounds for human boasting: \"Let the one who boasts, boast in the Lord\" (1 Cor. 1:31).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "boasting"},
        "key_refs": ["Jeremiah 9:23", "1 Corinthians 1:31", "2 Corinthians 12:9", "Galatians 6:14"]
    },
    "bereavement": {
        "id": "bereavement",
        "term": "Bereavement",
        "category": "concepts",
        "intro": "<p>Bereavement — the grief attending the death of a loved one — is taken with full seriousness in Scripture as a genuine human experience that God neither condemns nor minimizes. The OT presents weeping and mourning as natural and appropriate responses to death: Abraham mourned and wept for Sarah (Gen. 23:2), Jacob tore his garments at the supposed death of Joseph (Gen. 37:34), and the death of Moses was mourned by Israel for thirty days (Deut. 34:8). The prophet Hosea uses maternal bereavement as an image of devastating loss (Hos. 9:12). At the death of Lazarus, Jesus wept (John 11:35) — the shortest verse in the Bible and a profound affirmation of the legitimacy of grief. The theological framework Scripture provides for bereavement is not the denial of grief but its transformation by resurrection hope: Paul instructs the Thessalonians not to grieve \"as others do who have no hope\" (1 Thess. 4:13) — not forbidding grief but distinguishing grief transformed by the resurrection from hopeless grief. The beatitude \"Blessed are those who mourn, for they shall be comforted\" (Matt. 5:4) places even bereavement within the horizon of divine consolation.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "bereavement"},
        "key_refs": ["Genesis 23:2", "John 11:35", "1 Thessalonians 4:13", "Matthew 5:4"]
    },
    "chastisement": {
        "id": "chastisement",
        "term": "Chastisement",
        "category": "concepts",
        "intro": "<p>Chastisement (Hebrew <em>musar</em>; Greek <em>paideia</em>, \"discipline\" or \"training\") in Scripture refers to God's corrective action toward his people — the suffering, hardship, or rebuke by which the Lord trains those he loves in righteousness and holy character. The foundational statement is Proverbs 3:11–12 (quoted in Hebrews 12:5–6): \"My son, do not despise the LORD's discipline or be weary of his reproof, for the LORD reproves him whom he loves, as a father the son in whom he delights.\" This parent-child analogy runs through the biblical teaching on chastisement: God's corrective dealings with Israel in the wilderness were explicitly educational (Deut. 8:5; 11:2), shaping a people in humility, dependence, and covenant obedience. The Psalms of affliction (Ps. 119:67, 71) confess that suffering proved beneficial: \"Before I was afflicted I went astray, but now I keep your word.\" Hebrews 12:7–11 provides the NT's fullest treatment, arguing that the experience of hardship as God's discipline produces \"the peaceful fruit of righteousness\" in those who are trained by it. The promise of chastisement is paradoxically a mark of sonship: God disciplines every son he receives (Heb. 12:6; Rev. 3:19).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"nave": "chastisement"},
        "key_refs": ["Proverbs 3:11", "Deuteronomy 8:5", "Hebrews 12:6", "Psalms 119:71"]
    },
}


def main():
    written = skipped = 0
    for slug, data in ARTICLES.items():
        if merge_article(slug, data):
            written += 1
        else:
            skipped += 1
    print(f'BP gap-nt-context: NT epistles, persons, practices, and intertestamental: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
