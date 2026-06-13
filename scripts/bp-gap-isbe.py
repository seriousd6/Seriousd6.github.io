"""
BP Article Synthesis — gap-isbe-theology: Canon → Heavens
Covers Phase 2 gap articles: ISBE scholarly theology, Christology, textual studies (65 entries)

Sources consulted:
  - data/biblepedia/gaps.json (gap analysis)
  - ISBE index entries and scholarly articles

Script: scripts/bp-gap-isbe.py
Run: python3 scripts/bp-gap-isbe.py
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
        json.dump(data, f, ensure_ascii=False, indent=2)


def merge_article(slug, data):
    if load_article(slug) is not None:
        return False
    save_article(slug, data)
    return True


ARTICLES = {
    "canon-of-the-new-testament": {
        "id": "canon-of-the-new-testament",
        "term": "Canon of the New Testament",
        "category": "concepts",
        "intro": "<p>The canon of the New Testament is the authoritative collection of 27 books recognized by the church as divinely inspired Scripture. The word <em>canon</em> (Greek <em>kanon</em>, \"rule\" or \"measuring rod\") denotes the standard by which books were judged. The process of canonization was not a single council decision but a gradual, organic recognition over the first four centuries. Paul's letters were circulating and being collected within decades of his death (cf. 2 Pet. 3:16, which already groups them with \"other Scriptures\"). The major criteria applied by the early church were apostolicity (authorship by an apostle or apostolic associate), catholicity (acceptance by the church broadly), orthodoxy (conformity with the rule of faith), and liturgical use. Disputed books — Hebrews, James, 2 Peter, 2–3 John, Jude, Revelation — achieved full recognition by different regions at different times. Eusebius (<em>Ecclesiastical History</em>, c. 325) distinguished between the <em>homologoumena</em> (universally accepted), <em>antilegomena</em> (disputed), and rejected writings. The Festal Letter of Athanasius (367) is the first surviving document listing exactly the 27 books of the present NT canon. The councils of Hippo (393) and Carthage (397) ratified this list for the Western church.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "canon-of-the-new-testament"},
        "key_refs": ["2 Peter 3:16", "2 Timothy 3:16", "Luke 1:1", "Revelation 22:18"]
    },
    "canon-of-the-old-testament": {
        "id": "canon-of-the-old-testament",
        "term": "Canon of the Old Testament",
        "category": "concepts",
        "intro": "<p>The canon of the Old Testament is the collection of Hebrew Scriptures recognized as divinely authoritative, whose contents have been debated between Jewish, Protestant, Roman Catholic, and Eastern Orthodox traditions. The Hebrew Bible contains 39 books (counted in the Protestant OT), traditionally divided into Torah (Law), Nevi'im (Prophets), and Ketuvim (Writings) — together the Tanakh. The Council of Jamnia (c. 90 A.D.) is sometimes cited as fixing the Jewish canon, though the evidence suggests broader earlier consensus on most books. The Septuagint (LXX), the Greek translation used widely in the first century, included additional books not in the Hebrew canon — 1–2 Maccabees, Tobit, Judith, Wisdom of Solomon, Sirach, Baruch, and additions to Daniel and Esther. These are accepted as deuterocanonical by Roman Catholic and Eastern Orthodox churches and as apocryphal (useful but non-canonical) by Protestants. Jesus and the apostles cite what appear to be the 39 books of the Hebrew canon; no NT book explicitly cites the deuterocanonical books as Scripture, though allusions occur. Jerome's Prologus Galeatus (c. 390) clearly distinguished the Hebrew canon from the additional Greek books.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "canon-of-the-old-testament"},
        "key_refs": ["Luke 24:44", "2 Timothy 3:16", "Matthew 5:17", "Romans 3:2"]
    },
    "manuscripts-of-the-new-testament": {
        "id": "manuscripts-of-the-new-testament",
        "term": "Manuscripts of the New Testament",
        "category": "concepts",
        "intro": "<p>The New Testament is preserved in a remarkable wealth of manuscript evidence — over 5,800 Greek manuscripts, ranging from tiny papyrus fragments to complete parchment codices, plus over 10,000 Latin manuscripts and 9,300 manuscripts in other ancient versions. This textual tradition far surpasses any other ancient document in both quantity and proximity to the original compositions. Manuscripts are categorized by material (papyrus, vellum/parchment, paper), by script (uncial/majuscule, minuscule, lectionary), and by age. The earliest substantial fragments include P52 (Rylands Papyrus, John 18:31–33, c. 125 A.D.) and P66 (Bodmer II, Gospel of John, c. 200 A.D.). The great fourth-century codices — Codex Sinaiticus (ℵ) and Codex Vaticanus (B) — preserve complete or nearly complete NTs. Textual critics organize manuscripts into text-types: Alexandrian, Western, and Byzantine (or Majority Text). The discipline of textual criticism seeks to reconstruct the most original text by evaluating variants; modern critical editions (Nestle-Aland, UBS Greek NT) reflect the consensus of this scholarship. No major Christian doctrine hangs on any disputed textual variant.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "manuscripts-of-the-new-testament"},
        "key_refs": ["John 5:39", "2 Timothy 3:16", "Luke 1:1", "2 Peter 1:21"]
    },
    "manuscripts-of-the-old-testament": {
        "id": "manuscripts-of-the-old-testament",
        "term": "Manuscripts of the Old Testament",
        "category": "concepts",
        "intro": "<p>The text of the Old Testament is preserved primarily through Hebrew manuscripts of the Masoretic tradition, supplemented by the Greek Septuagint, the Samaritan Pentateuch, the Targums (Aramaic paraphrases), the Syriac Peshitta, and Latin Vulgate. The Masoretic Text (MT), standardized by Jewish scribal scholars (Masoretes) between the 6th and 10th centuries A.D., represents the authoritative Hebrew text; the oldest complete MT manuscript is the Leningrad Codex (1008–1009 A.D.). The discovery of the Dead Sea Scrolls (1947–1956) at Qumran dramatically pushed the textual evidence back a thousand years: the Great Isaiah Scroll (1QIsa<sup>a</sup>, c. 125 B.C.) is nearly complete and shows remarkable stability in the textual tradition while also revealing some variants. The Septuagint (LXX), translated in stages from the 3rd to 1st centuries B.C., reflects a Hebrew text sometimes differing from the MT and proves invaluable for textual criticism. The Samaritan Pentateuch preserves an independent textual tradition for the Torah. OT textual criticism applies the same principles as NT — weighing internal and external evidence — to reconstruct the most original reading.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "manuscripts-of-the-old-testament"},
        "key_refs": ["Isaiah 40:8", "Psalm 119:89", "Matthew 5:18", "Romans 3:2"]
    },
    "hermeneutics": {
        "id": "hermeneutics",
        "term": "Hermeneutics",
        "category": "concepts",
        "intro": "<p>Hermeneutics (from Greek <em>hermeneuo</em>, to interpret, related to Hermes as messenger of the gods) is the science and art of biblical interpretation — the principles and methods by which Scripture is understood and applied. The discipline encompasses both general hermeneutics (principles applicable to all literature) and special hermeneutics (principles specific to Scripture as divine revelation). Classical hermeneutics established the grammatical-historical method: understanding the biblical text in light of its original language, grammar, literary genre, and historical setting — what the text meant to its first readers. This method, developed by Reformation exegetes and refined in subsequent Protestant scholarship, holds that the text has a single determinate meaning intended by the human author under divine inspiration, though it may have multiple applications. Key hermeneutical principles include: context (immediate, book-wide, and canonical), grammar (syntax and word meaning in the original languages), genre (narrative, poetry, prophecy, epistle, apocalyptic), analogy of faith (interpreting obscure passages by clearer ones), and progressive revelation. Modern hermeneutics has expanded to address pre-understanding, cultural distance, reader response, and the role of tradition, while evangelical scholarship maintains the priority of authorial intent rooted in divine inspiration (2 Pet. 1:20–21).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "hermeneutics"},
        "key_refs": ["2 Timothy 2:15", "Nehemiah 8:8", "2 Peter 1:20", "Luke 24:27"]
    },
    "deutero-canonical-books": {
        "id": "deutero-canonical-books",
        "term": "Deuterocanonical Books",
        "category": "concepts",
        "intro": "<p>The deuterocanonical books (from Greek <em>deuteros</em>, second + <em>kanon</em>, rule) are the books accepted as canonical by the Roman Catholic and Eastern Orthodox churches but not by Protestants or in the Hebrew Bible. The Roman Catholic Church uses the term to distinguish them from the protocanonical books (universally accepted), while Protestant traditions call the same writings the Apocrypha (Greek, \"hidden things\"). The books include: Tobit, Judith, 1–2 Maccabees, Wisdom of Solomon, Sirach (Ecclesiasticus), Baruch, and additions to Daniel (Susanna, Bel and the Dragon, the Prayer of Azariah) and Esther. They were written primarily in the intertestamental period (c. 300 B.C. – 100 A.D.) and were included in the Septuagint. Jerome, while translating the Vulgate, placed them in the Bible but noted their secondary status. Luther removed them from the OT canon but included them as an appendix. The Council of Trent (1546) formally declared them canonical for Roman Catholics. Protestant scholarship values them as historical and religious literature illuminating Second Temple Judaism, but does not grant them scriptural authority alongside the canonical OT.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "deutero-canonical-books"},
        "key_refs": ["Luke 24:44", "Romans 3:2", "2 Timothy 3:16"]
    },
    "acts-apocryphal": {
        "id": "acts-apocryphal",
        "term": "Acts, Apocryphal",
        "category": "concepts",
        "intro": "<p>The apocryphal Acts are a collection of early Christian writings that imitate the canonical Acts of the Apostles, narrating the missionary travels and martyrdoms of individual apostles with legendary and often theologically heterodox content. The major texts include the Acts of Peter, Acts of Paul (with the <em>Acta Pauli et Theclae</em>), Acts of John, Acts of Andrew, and Acts of Thomas — composed primarily in the 2nd and 3rd centuries A.D. They circulated widely in both orthodox and Gnostic Christian communities and enjoyed great popularity, particularly for their dramatic miracle stories and martyrdom accounts. Their theology often reflects docetic, encratite (extreme asceticism), or Gnostic tendencies: the Acts of Thomas, for instance, presents a strongly ascetic theology with Syriac Gnostic influences. They were never accepted into the canonical NT; Eusebius placed them among \"rejected\" writings. Modern scholarship values them as evidence of popular Christian piety, women's leadership in early Christianity, the spread of Gnosticism, and the development of apostolic legends. They should not be confused with the canonical Acts of the Apostles, which has strong historical grounding in its eyewitness sources.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "acts-apocryphal"},
        "key_refs": ["Acts 1:1", "2 Peter 1:16", "Galatians 1:8"]
    },
    "apocryphal-gospels": {
        "id": "apocryphal-gospels",
        "term": "Apocryphal Gospels",
        "category": "concepts",
        "intro": "<p>The apocryphal gospels are a diverse body of early Christian writings that claim to record the life, teachings, or secret revelations of Jesus, distinct from the four canonical Gospels. They range widely in genre, date, and theological orientation. The Gnostic gospels — including the Gospel of Thomas (a sayings collection), the Gospel of Philip, the Gospel of Truth, and the Gospel of Judas — were discovered at Nag Hammadi (1945) and reflect 2nd–4th century Gnostic Christianity, presenting secret knowledge (<em>gnosis</em>) as the path to salvation rather than historical redemption. The infancy gospels (Protevangelium of James, Infancy Gospel of Thomas) filled in details about Mary and Jesus's childhood absent from the canonical accounts. The Gospel of Peter and Gospel of the Hebrews were known to and cited (cautiously) by early fathers. None were accepted into the canonical NT; most were composed too late and too far from apostolic circles to carry historical authority. The Muratorian Canon (c. 170 A.D.) explicitly rejects several. Modern scholarship uses them to trace the diversity of early Christianity, but their historical value for reconstructing the life of Jesus is minimal compared to the four canonical Gospels.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "apocryphal-gospels"},
        "key_refs": ["Luke 1:1", "John 20:30", "1 Corinthians 15:3", "Galatians 1:8"]
    },
    "apocryphal-epistles": {
        "id": "apocryphal-epistles",
        "term": "Apocryphal Epistles",
        "category": "concepts",
        "intro": "<p>The apocryphal epistles are writings in letter form falsely attributed to apostles or other NT figures, circulating in early Christianity outside the canonical NT. They include: the Epistle to the Laodiceans (a short, unremarkable Latin letter falsely attributed to Paul, long suspected as a forgery), the Correspondence of Paul and Seneca (14 letters, a 4th-century Latin fabrication), the Third Epistle to the Corinthians (preserved within the Acts of Paul), the Epistle of the Apostles (<em>Epistula Apostolorum</em>, an early 2nd-century anti-Gnostic work in the form of a letter from the apostles), and various Gnostic epistles. Colossians 4:16 mentions a letter to Laodicea from Paul, which has fueled speculation about the apocryphal Laodiceans, but Jerome and most ancient critics dismissed it as inauthentic. The apocryphal epistles were produced to fill in gaps in the apostolic record, support particular doctrinal positions, or satisfy curiosity about figures mentioned in the NT. None achieved canonical status; their lack of apostolic authorship and their often doctrinal peculiarities ruled them out.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "apocryphal-epistles"},
        "key_refs": ["Colossians 4:16", "2 Thessalonians 2:2", "Galatians 1:8", "2 Peter 3:16"]
    },
    "apocryphal-acts": {
        "id": "apocryphal-acts",
        "term": "Apocryphal Acts",
        "category": "concepts",
        "intro": "<p>The apocryphal acts are a cluster of early Christian narratives — Acts of Peter, Acts of Paul, Acts of John, Acts of Andrew, and Acts of Thomas being the most significant — that extend the apostolic story beyond the canonical Acts of the Apostles with legendary missionary adventures, miracles, and martyrdom accounts. Composed primarily in the 2nd and 3rd centuries, they served as popular devotional literature in Christian communities. Photius, the 9th-century patriarch, noted that Leucius Charinus was associated with collecting some of them, though modern scholarship regards this as legend. Their theological tendencies are often heterodox: the Acts of Thomas is strongly encratite (prohibiting marriage even within Christianity); the Acts of John presents a docetic Christ who leaves no footprint and appears in varying forms. Despite their theological problems, they preserve valuable traditions about early Christian practice, veneration of apostles, women's roles, and popular religion. The church never accepted them as Scripture; Eusebius categorized the best-known as <em>notha</em> (spurious). They are distinguished from the pseudepigrapha primarily by genre — narrative travelogue rather than epistle or apocalypse.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "apocryphal-acts"},
        "key_refs": ["Acts 1:8", "2 Peter 1:16", "1 Corinthians 15:15"]
    },
    "christology": {
        "id": "christology",
        "term": "Christology",
        "category": "concepts",
        "intro": "<p>Christology is the branch of Christian theology concerned with the person of Jesus Christ — who he is in his divine and human natures, their relationship, and how this bears on his salvific work. The NT presents a high Christology from its earliest layers: Paul's letters (written before the Gospels) identify Jesus with divine titles (<em>Kyrios</em>, Lord; <em>Theos</em>, God), apply OT divine texts to him (Phil. 2:10–11; Rom. 10:13), and present him as the agent of creation and the one through whom God acts cosmically (1 Cor. 8:6; Col. 1:15–17). John's Prologue identifies him as the eternal Logos who was God and became flesh (John 1:1–14). The councils of the 4th–5th centuries hammered out the church's formal Christological definition in response to heresies. Arianism (Jesus is a created being, not fully divine) was condemned at Nicaea (325), which affirmed the Son is <em>homoousios</em> (same substance) with the Father. Apollinarianism (Jesus had a divine mind replacing the human) was condemned at Constantinople (381). Nestorianism (two persons in Christ) and Eutychianism (two natures merged into one) were condemned at Chalcedon (451), which defined Christ as one person in two natures, fully divine and fully human, without confusion, change, division, or separation — the formula that has defined orthodox Christology ever since.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "christology"},
        "key_refs": ["John 1:1", "Philippians 2:6", "Colossians 1:15", "Hebrews 1:3", "John 8:58"]
    },
    "eschatology": {
        "id": "eschatology",
        "term": "Eschatology",
        "category": "concepts",
        "intro": "<p>Eschatology (from Greek <em>eschaton</em>, last + <em>logos</em>, word) is the branch of theology concerned with the last things — death, resurrection, judgment, and the final state of persons and the universe. Biblical eschatology encompasses both individual eschatology (what happens to each person at death and at the last day) and cosmic eschatology (the consummation of history and creation). The OT develops eschatological hope progressively: from the Day of the LORD as divine judgment and restoration (Amos 5:18–20; Isa. 2:12–22; Joel 2:28–32) to explicit resurrection hope (Dan. 12:2; Isa. 26:19) to the vision of a new heavens and new earth (Isa. 65:17–25). NT eschatology is shaped by the decisive event of Christ's resurrection as the \"firstfruits\" (1 Cor. 15:20) and the gift of the Spirit as the \"deposit\" of the coming inheritance (Eph. 1:14). The NT presents an eschatology of inauguration: the kingdom of God has already arrived in Christ's ministry (Luke 11:20) but awaits its full revelation at his return (Rev. 22:20). Major disputed topics include the millennium (Rev. 20:1–6), the timing of the rapture, the relationship of Israel and the church in prophecy, and the nature of hell and eternal punishment.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "eschatology"},
        "key_refs": ["Daniel 12:2", "1 Corinthians 15:20", "Revelation 20:11", "1 Thessalonians 4:16", "Revelation 21:1"]
    },
    "eschatology-of-the-new-testament": {
        "id": "eschatology-of-the-new-testament",
        "term": "Eschatology of the New Testament",
        "category": "concepts",
        "intro": "<p>NT eschatology is shaped by the conviction that the end-time events have already begun in the death and resurrection of Jesus Christ — a schema sometimes called \"inaugurated eschatology\" or the \"already/not yet\" tension. Jesus announces that the kingdom of God has arrived (Mark 1:15; Luke 11:20), performs exorcisms as signs of Satan's defeat (Matt. 12:29), and declares that eternal life is already possessed by those who believe in him (John 5:24; 3:36). Yet the full consummation remains future: Christ will return visibly and gloriously (Matt. 24:30; Acts 1:11), the dead will be raised (1 Cor. 15:52; John 5:28–29), and the final judgment will occur (Matt. 25:31–46; Rev. 20:11–15). Paul's eschatology in 1 Thessalonians 4:13–18 and 1 Corinthians 15 addresses questions about those who die before Christ's return, presenting resurrection as bodily transformation from perishable to imperishable. The Book of Revelation, employing apocalyptic imagery, depicts the tribulation, the binding and loosing of Satan, the millennium, and the new Jerusalem as the consummation of God's plan. The precise sequence of these events is debated among premillennial, postmillennial, and amillennial interpreters.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "eschatology-of-the-new-testament"},
        "key_refs": ["Mark 1:15", "1 Corinthians 15:52", "1 Thessalonians 4:16", "Revelation 20:4", "Matthew 25:31"]
    },
    "eschatology-of-the-old-testament": {
        "id": "eschatology-of-the-old-testament",
        "term": "Eschatology of the Old Testament",
        "category": "concepts",
        "intro": "<p>OT eschatology develops across the canon from theocratic covenant expectations toward an increasingly cosmic vision of divine judgment, renewal, and restoration. Early eschatological motifs include the Day of the LORD — initially assumed by Israel to be a day of vindication for them but reinterpreted by Amos as a day of darkness and judgment for all who do evil, including Israel (Amos 5:18–20). The prophets project a future in which God will judge the nations (Isa. 24–27; Ezek. 38–39; Zeph. 3:8–9), restore a remnant of Israel (Isa. 10:20–22; Jer. 31:7), and establish a Davidic king (Isa. 9:1–7; 11:1–9; Jer. 23:5–6; Mic. 5:2) over an age of peace. Isaiah envisions the nations streaming to Zion (Isa. 2:2–4) and a new creation (Isa. 65:17–25; 66:22). Daniel contributes the clearest OT statements of individual resurrection (Dan. 12:2–3) and the Son of Man coming with clouds to receive universal dominion (Dan. 7:13–14). The 70 Weeks prophecy (Dan. 9:24–27) frames the redemptive timeline. Scholars debate whether OT prophecies regarding Israel's restoration are to be understood as literally national or as typologically fulfilled in Christ and the church.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "eschatology-of-the-old-testament"},
        "key_refs": ["Amos 5:18", "Daniel 12:2", "Isaiah 65:17", "Jeremiah 31:31", "Daniel 7:13"]
    },
    "election": {
        "id": "election",
        "term": "Election",
        "category": "concepts",
        "intro": "<p>Election is the divine act of choosing certain persons or a people for salvation and service, grounded entirely in God's sovereign will and mercy rather than foreseen human merit. In the OT, election is primarily corporate: God chose Israel from among the nations not because of her size or righteousness but solely because of his love and covenant faithfulness to the patriarchs (Deut. 7:6–8; 9:4–6). Within Israel, election narrowed to a remnant: those who actually believed (Isa. 10:22; Rom. 9:27) — anticipating NT individual election. Paul's extended treatment in Romans 9–11 defends divine election as consistent with justice: God's sovereign choice does not rest on human willing or running but on God who shows mercy (Rom. 9:16). Election is \"in Christ\" (Eph. 1:4–5) — the elect are chosen in the Beloved before the foundation of the world. Calvinism and Arminianism represent the major theological positions: Reformed theology holds to unconditional individual election to salvation; Arminian theology holds to corporate or conditional election based on foreknown faith. Both agree that election results in assurance for believers (Rom. 8:29–30; 2 Pet. 1:10) and issues in calling, justification, and glorification.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "election"},
        "key_refs": ["Deuteronomy 7:6", "Romans 9:16", "Ephesians 1:4", "Romans 8:29", "2 Peter 1:10"]
    },
    "perseverance": {
        "id": "perseverance",
        "term": "Perseverance",
        "category": "concepts",
        "intro": "<p>The perseverance of the saints is the doctrine that those whom God has genuinely regenerated will persevere in faith and holiness to the end and will ultimately be saved — not because of their own unaided strength but because God faithfully preserves them by his Spirit. It is one of the five points of Calvinism (the \"P\" of TULIP) and is closely connected to the doctrines of election and effectual calling. The biblical basis rests on divine preservation texts: \"My sheep hear my voice... and I give them eternal life, and they will never perish, and no one will snatch them out of my hand\" (John 10:27–28); \"He who began a good work in you will bring it to completion at the day of Jesus Christ\" (Phil. 1:6); \"I am sure that neither death nor life... will be able to separate us from the love of God\" (Rom. 8:38–39). Perseverance does not mean that true believers never sin, experience doubt, or temporarily wander, but that they will ultimately return and not finally apostatize. Arminian theology holds instead to conditional security — believers can forfeit salvation by apostasy. The warning passages in Hebrews (6:4–6; 10:26–31) are interpreted differently by the two traditions: either as warnings to those who were never truly regenerated, or as genuine warnings to true believers who can fall away.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "perseverance"},
        "key_refs": ["John 10:28", "Philippians 1:6", "Romans 8:38", "Hebrews 6:4", "1 Peter 1:5"]
    },
    "new-covenant": {
        "id": "new-covenant",
        "term": "New Covenant",
        "category": "concepts",
        "intro": "<p>The new covenant is the eschatological covenant God promised through Jeremiah to supersede the Mosaic covenant, characterized by the law written on the heart, universal knowledge of God, and complete forgiveness of sin (Jer. 31:31–34). Ezekiel develops related promises: a new heart, a new spirit, and God's own Spirit enabling obedience (Ezek. 36:25–27). Jesus inaugurates the new covenant at the Last Supper: \"This cup that is poured out for you is the new covenant in my blood\" (Luke 22:20; 1 Cor. 11:25), fulfilling these prophetic promises through his death. The writer of Hebrews provides the most extensive NT exposition, citing Jeremiah 31 in full (Heb. 8:8–12) and arguing that Christ is the mediator of a better covenant enacted on better promises (Heb. 8:6), whose blood establishes it definitively (Heb. 9:15; 12:24). The new covenant brings: the Spirit's indwelling (Rom. 8:9; 1 Cor. 3:16), adoption as children of God (Gal. 4:4–7), complete forgiveness of sins (Col. 2:13–14), and direct access to God (Eph. 2:18; Heb. 10:19–22). Covenant theology and dispensationalism debate how completely the new covenant supersedes the old and its relationship to the church and national Israel.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "new-covenant"},
        "key_refs": ["Jeremiah 31:31", "Luke 22:20", "Hebrews 8:6", "Ezekiel 36:26", "2 Corinthians 3:6"]
    },
    "covenant-in-the-new-testament": {
        "id": "covenant-in-the-new-testament",
        "term": "Covenant, In the New Testament",
        "category": "concepts",
        "intro": "<p>The NT's use of the covenant concept (<em>diatheke</em>) integrates the OT covenantal framework with the decisive fulfillment achieved in Jesus Christ. The Greek <em>diatheke</em> can mean either covenant (agreement) or testament (will), and Hebrews exploits the ambiguity: Christ's death activates the \"testament\" as a will takes effect at death (Heb. 9:15–17), while simultaneously establishing the new covenant. Paul's contrast of the covenants in Galatians 3–4 and 2 Corinthians 3 presents the Mosaic covenant as a temporary custodian arrangement (the \"old covenant\" of Sinai) that served until Christ came to fulfill the Abrahamic promise. The Spirit's ministry under the new covenant surpasses the written code of Sinai: \"The letter kills, but the Spirit gives life\" (2 Cor. 3:6). Jesus's invocation of \"the blood of the covenant\" at the Last Supper (Matt. 26:28; cf. Ex. 24:8; Zech. 9:11) identifies his death as the covenant-ratifying sacrifice. The NT presents all previous covenants — Noahic, Abrahamic, Mosaic, Davidic — as converging toward and fulfilled in the new covenant in Christ, which is the ultimate realization of God's covenant promise: \"I will be your God and you will be my people\" (Heb. 8:10; cf. Lev. 26:12; Jer. 31:33; Rev. 21:3).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "covenant-in-the-new-testament"},
        "key_refs": ["Matthew 26:28", "Hebrews 9:15", "2 Corinthians 3:6", "Galatians 3:17", "Hebrews 8:10"]
    },
    "covenant-in-the-old-testament": {
        "id": "covenant-in-the-old-testament",
        "term": "Covenant, In the Old Testament",
        "category": "concepts",
        "intro": "<p>Covenant (<em>berit</em>) is the organizing theological concept of the OT, structuring the relationship between God and his people through formal agreements that define obligations, promises, and the nature of the relationship. The major OT covenants form a redemptive-historical sequence. The Noahic covenant (Gen. 9:1–17) is universal, unconditional, and confirmed by the rainbow — God's commitment to preserve creation. The Abrahamic covenant (Gen. 12:1–3; 15; 17) promises land, seed, and blessing to Abraham and his descendants and through them to all nations, sealed with circumcision. The Mosaic/Sinaitic covenant (Ex. 19–24; Deut.) is the national covenant with Israel, resembling ancient suzerainty treaties in structure, with its stipulations (law), sanctions (blessings and curses), and ratification in blood (Ex. 24:8). The Davidic covenant (2 Sam. 7:8–16; Ps. 89; 132) promises an eternal dynasty through David's line, fulfilled in the Messiah. Ancient Near Eastern parallels illuminate the formal structure of these covenants, but Scripture's covenants are distinctive in their moral character and their grounding in the character of the covenant-making God (<em>El-Shaddai</em>, <em>YHWH</em>) who is faithful to his own word.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "covenant-in-the-old-testament"},
        "key_refs": ["Genesis 15:18", "Exodus 24:8", "2 Samuel 7:12", "Deuteronomy 7:9", "Psalm 89:3"]
    },
    "holy-spirit": {
        "id": "holy-spirit",
        "term": "Holy Spirit",
        "category": "concepts",
        "intro": "<p>The Holy Spirit is the third person of the Trinity — fully divine, co-equal and co-eternal with the Father and the Son — who is the personal agent of God's presence and power in creation, revelation, redemption, and the Christian life. The OT depicts the Spirit of God (<em>Ruah Elohim</em>) as the agent of creation (Gen. 1:2), empowering judges and kings (Judg. 3:10; 1 Sam. 16:13), inspiring prophets (Isa. 61:1; Ezek. 2:2), and promised in eschatological abundance on all flesh (Joel 2:28–29). Jesus is conceived by the Spirit (Luke 1:35), anointed by the Spirit at baptism (Matt. 3:16), driven by the Spirit into the wilderness (Mark 1:12), and ministers in the Spirit's power (Luke 4:18). He promises the Spirit as <em>Parakletos</em> (Helper/Advocate, John 14:16–17, 26; 15:26; 16:7–15) who will dwell in believers, teach them all truth, and convict the world of sin. At Pentecost (Acts 2) the Spirit is poured out on the early church with visible signs, empowering witness (Acts 1:8). Paul's letters ground the Spirit's role in union with Christ: the Spirit indwells believers (Rom. 8:9–11), produces the fruit of the Spirit (Gal. 5:22–23), distributes gifts for building the body (1 Cor. 12), intercedes in prayer (Rom. 8:26–27), and seals the believer until final redemption (Eph. 1:13–14; 4:30).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "holy-spirit"},
        "key_refs": ["John 14:16", "Acts 2:4", "Romans 8:9", "Galatians 5:22", "Ephesians 1:13"]
    },
    "baptism-of-the-holy-spirit": {
        "id": "baptism-of-the-holy-spirit",
        "term": "Baptism of the Holy Spirit",
        "category": "concepts",
        "intro": "<p>\"Baptism of/in/with the Holy Spirit\" refers to the experience of being immersed in or overwhelmed by the Holy Spirit, a phrase used in all four Gospels and Acts to describe what John the Baptist contrasts with his own water baptism: \"He will baptize you with the Holy Spirit and fire\" (Matt. 3:11; Mark 1:8; Luke 3:16; John 1:33). Jesus promises the Spirit's coming baptism to the disciples before Pentecost (Acts 1:5), which is fulfilled in Acts 2. Paul uses the concept in 1 Corinthians 12:13: \"For in one Spirit we were all baptized into one body,\" applying it universally to all believers at conversion. Significant theological debate exists about the timing and repeatability of Spirit baptism. Classical Pentecostalism (from 1906 Azusa Street revival onward) teaches that Spirit baptism is a second, post-conversion experience subsequent to and distinct from conversion, evidenced initially by speaking in tongues (Acts 2:4; 10:44–46; 19:6). Cessationist and Reformed theology identifies Spirit baptism with regeneration and conversion, making it a once-for-all event for all believers at the moment of faith. Charismatic Christianity occupies a middle position. The exegesis of Acts (which records multiple Spirit-outpourings) and 1 Corinthians 12:13 are central to the debate.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "baptism-of-the-holy-spirit"},
        "key_refs": ["Matthew 3:11", "Acts 1:5", "Acts 2:4", "1 Corinthians 12:13", "Ephesians 4:5"]
    },
    "baptismal-regeneration": {
        "id": "baptismal-regeneration",
        "term": "Baptismal Regeneration",
        "category": "concepts",
        "intro": "<p>Baptismal regeneration is the theological position that water baptism is the ordinary means through which the new birth (regeneration) is effected, making baptism instrumentally necessary for salvation rather than merely a sign and seal of grace already received. This view is held in varying forms by Roman Catholic, Eastern Orthodox, Lutheran (ex opere operato sacramental), and some Anglican traditions. The primary NT texts cited in support are John 3:5 (\"born of water and the Spirit\"), Acts 2:38 (\"be baptized... for the forgiveness of your sins, and you will receive the gift of the Holy Spirit\"), Titus 3:5 (\"washing of regeneration\"), and 1 Peter 3:21 (\"baptism now saves you\"). Reformed and evangelical Protestant theology strongly contests this interpretation: John 3:5 refers to Spirit-birth, not water baptism; Acts 2:38's preposition <em>eis</em> may indicate direction (\"because of\") rather than purpose; 1 Peter 3:21 explicitly qualifies \"not the removal of dirt from the body but an appeal to God for a good conscience.\" Protestant theology affirms baptism as the ordained sign of the covenant and of regeneration, but distinguishes the sign from the thing signified — regeneration being the Spirit's work through the Word received by faith (Rom. 10:17; Eph. 2:8–9; 1 Pet. 1:23).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "baptismal-regeneration"},
        "key_refs": ["John 3:5", "Acts 2:38", "Titus 3:5", "1 Peter 3:21", "Ephesians 2:8"]
    },
    "lords-supper;-eucharist": {
        "id": "lords-supper;-eucharist",
        "term": "Lord's Supper; Eucharist",
        "category": "concepts",
        "intro": "<p>The Lord's Supper (also called the Eucharist, Holy Communion, or the Breaking of Bread) is one of the two sacraments universally recognized in Christian tradition, instituted by Jesus at the Last Supper on the night of his betrayal (Matt. 26:26–29; Mark 14:22–25; Luke 22:14–20; 1 Cor. 11:23–26). The term <em>eucharist</em> derives from Greek <em>eucharistia</em> (thanksgiving), reflecting Jesus's act of giving thanks over the bread and cup. The four major theological traditions interpret Christ's presence in the supper differently. Roman Catholicism teaches <em>transubstantiation</em>: the bread and wine become the actual body and blood of Christ (the substance changes while the accidents remain), re-presenting Christ's sacrifice at each mass. Lutheranism holds <em>consubstantiation</em> or \"sacramental union\": Christ's body and blood are truly present \"in, with, and under\" the bread and wine, without transubstantiation. The Reformed tradition (Calvinist) holds that Christ is spiritually and truly present to the faith of the receiver but not locally in the elements; the supper is a means of grace by which Christ truly feeds the soul. Memorialism (Zwingli, most Baptist traditions) holds the supper is a memorial of Christ's death without his physical presence in the elements. Paul's treatment in 1 Corinthians 10:16–17 and 11:23–32 establishes its covenantal and communal dimensions.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "lords-supper;-eucharist"},
        "key_refs": ["Matthew 26:26", "1 Corinthians 11:23", "Luke 22:20", "1 Corinthians 10:16", "John 6:53"]
    },
    "eucharist": {
        "id": "eucharist",
        "term": "Eucharist",
        "category": "concepts",
        "intro": "<p>The Eucharist (from Greek <em>eucharistia</em>, thanksgiving) is the Christian sacramental meal of bread and wine commemorating Christ's body and blood given in his atoning death, instituted at the Last Supper and celebrated by Christians from the apostolic era onward. The term appears in early Christian literature: the <em>Didache</em> (c. 100 A.D.) uses it for the Lord's Supper, and Ignatius of Antioch (c. 107 A.D.) employs it to describe the church's central gathering. The Eucharist's institution is narrated in the Synoptics and 1 Corinthians 11:23–26, where Paul records the tradition he received: \"This is my body... This cup is the new covenant in my blood.\" The eschatological dimension is explicit: \"You proclaim the Lord's death until he comes\" (1 Cor. 11:26), making each celebration both a memorial of the past redemption and a foretaste of the messianic banquet (Matt. 26:29; Rev. 19:9). The Eucharist functions as: proclamation of the gospel (1 Cor. 11:26), participation in Christ's body and blood (1 Cor. 10:16), expression of the church's unity as one body (1 Cor. 10:17), and the covenant renewal meal of the new covenant (Luke 22:20; 1 Cor. 11:25). Different traditions (Catholic, Lutheran, Reformed, memorialist) understand Christ's mode of presence in the elements differently, making this one of Christian theology's most disputed doctrinal points.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "eucharist"},
        "key_refs": ["1 Corinthians 11:23", "Matthew 26:26", "Luke 22:19", "1 Corinthians 10:16", "Revelation 19:9"]
    },
    "kingdom-of-god-of-heaven-the": {
        "id": "kingdom-of-god-of-heaven-the",
        "term": "Kingdom of God (of Heaven), The",
        "category": "concepts",
        "intro": "<p>The Kingdom of God (Greek <em>basileia tou theou</em>; Matthew's equivalent, <em>basileia ton ouranon</em>, Kingdom of Heaven) is the central theme of Jesus's preaching — the sovereign reign of God that has arrived in Jesus's own person and ministry and will be consummated at his return. The phrase denotes not primarily a territory but a dynamic reality: God's kingly rule being exercised and acknowledged. The OT anticipates it: God is king over Israel and all nations (Ps. 47; 93; 96–99); the prophets envision a future in which his reign will be universally recognized (Isa. 2:2–4; Zech. 14:9). Jesus announces its arrival: \"The kingdom of God has come upon you\" (Matt. 12:28; Luke 11:20), confirmed by his exorcisms, healings, and table fellowship with sinners. His parables describe its surprising character: it grows invisibly from small beginnings (mustard seed, leaven), contains both righteous and wicked until harvest, and is of surpassing worth (treasure, pearl). The kingdom is already present in the Spirit's power (1 Cor. 4:20; Rom. 14:17) but not yet fully revealed — believers await its consummation at Christ's return (Matt. 25:34; Rev. 11:15; 1 Cor. 15:24–28). The millennium (Rev. 20:1–6) is the major point of dispute in mapping the kingdom's consummation.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "kingdom-of-god-of-heaven-the"},
        "key_refs": ["Matthew 12:28", "Mark 1:15", "Luke 11:20", "1 Corinthians 15:24", "Revelation 11:15"]
    },
    "hellenism;-hellenist": {
        "id": "hellenism;-hellenist",
        "term": "Hellenism; Hellenist",
        "category": "concepts",
        "intro": "<p>Hellenism refers to the spread of Greek language, culture, and thought throughout the ancient Near East and Mediterranean world following the conquests of Alexander the Great (336–323 B.C.). The term <em>Hellenist</em> in Acts 6:1 and 9:29 designates Greek-speaking Jews, as distinct from Hebrew-speaking (<em>Hebraios</em>) Jews. Alexander's campaigns and the subsequent Diadochi kingdoms — particularly the Ptolemies in Egypt and the Seleucids in Syria — imposed Greek as the <em>lingua franca</em> of commerce, diplomacy, and culture. For Judaism, Hellenism created a profound cultural challenge: the Maccabean crisis (167–164 B.C.) arose directly from Seleucid attempts to Hellenize Judea, provoking armed Jewish resistance. The resulting intertestamental literature (1–2 Maccabees, Jubilees, 1 Enoch) reflects both resistance to and accommodation of Hellenistic influence. For NT Christianity, Hellenism's legacy was decisive: the Septuagint (Greek OT translation) became the Bible of the early church; Greek served as the universal language of NT composition; and Hellenistic philosophical concepts (Logos, <em>pneuma</em>, <em>psyche</em>) provided vocabulary and conceptual frameworks that NT authors filled with new theological content. The relationship between Hellenism and early Christianity remains a major topic in NT scholarship.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "hellenism;-hellenist"},
        "key_refs": ["Acts 6:1", "John 12:20", "Acts 9:29", "Galatians 3:28", "Colossians 3:11"]
    },
    "gnosticism": {
        "id": "gnosticism",
        "term": "Gnosticism",
        "category": "concepts",
        "intro": "<p>Gnosticism (from Greek <em>gnosis</em>, knowledge) designates a diverse cluster of religious movements in the 1st–4th centuries A.D. that taught salvation through secret, esoteric knowledge of divine mysteries, typically accompanied by a dualistic cosmology in which the material world is evil (created by a lesser or malevolent demiurge), the true God is utterly transcendent, and salvation consists in the spirit's liberation from material entrapment and return to the divine Pleroma (fullness). Gnostic systems produced elaborate mythologies featuring divine emanations (aeons), a Sophia figure whose fall generates the material world, and a revealer figure (often Jesus reinterpreted docetically — appearing to be human but not truly incarnate) who delivers the saving <em>gnosis</em>. The Nag Hammadi library (discovered 1945 in Egypt) greatly expanded scholarly knowledge of Gnostic texts: the Gospel of Thomas, Gospel of Philip, Gospel of Truth, and Apocryphon of John are among the most significant. Whether a fully developed Gnosticism pre-dated Christianity and influenced the NT (a thesis associated with Bultmann and the Religionsgeschichtliche Schule) or whether Gnosticism developed as a Christian heresy from the 2nd century onward (the traditional view) remains debated. The NT warns against proto-Gnostic tendencies (Col. 2:8, 18; 1 John 4:2; 1 Tim. 6:20).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "gnosticism"},
        "key_refs": ["1 John 4:2", "Colossians 2:8", "1 Timothy 6:20", "John 1:14", "2 John 7"]
    },
    "kenosis": {
        "id": "kenosis",
        "term": "Kenosis",
        "category": "concepts",
        "intro": "<p>Kenosis (from Greek <em>kenoo</em>, to empty) is the theological concept derived from Philippians 2:7, where Paul describes Christ as having \"emptied himself\" (<em>heauton ekenosen</em>) in taking the form of a servant and being born in human likeness. The kenosis doctrine addresses how the eternal Son of God could genuinely become human — and specifically, how divine omniscience, omnipotence, and omnipresence relate to the limitations Jesus experienced in his earthly life (Matt. 24:36; Luke 2:52; John 11:34). Classic orthodox Christology (Chalcedon, 451) affirms the two natures without confusion or change: the divine nature is not diminished by the incarnation. The Kenotic theology that emerged in 19th-century German Lutheranism (Thomasius, Gess, Ebrard) and British theology (Forsyth, Gore) proposed that the Son literally divested himself of certain divine attributes (omniscience, omnipotence) at the incarnation, genuinely limiting himself to human knowledge and power. Critics argued this compromised divine immutability and the Son's full deity. The mainstream evangelical position holds that Philippians 2:7 describes not the abandonment of divine attributes but the addition of human nature and the veiling of divine glory, the voluntary choice not to exercise certain divine prerogatives, as Christ took the role of servant rather than sovereign.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "kenosis"},
        "key_refs": ["Philippians 2:7", "John 1:14", "Hebrews 2:17", "Luke 2:52", "Matthew 24:36"]
    },
    "virgin-birth": {
        "id": "virgin-birth",
        "term": "Virgin Birth",
        "category": "concepts",
        "intro": "<p>The virgin birth (more precisely the virginal conception) is the doctrine that Jesus Christ was conceived in the womb of the Virgin Mary by the power of the Holy Spirit without a human father, making him truly the Son of God incarnate. The birth narratives of Matthew and Luke both affirm it explicitly: Matthew identifies it as fulfillment of Isaiah 7:14 (\"Behold, the virgin shall conceive and bear a son\"; LXX <em>parthenos</em>), and Luke records the angel Gabriel's announcement that the Spirit would come upon Mary (Luke 1:31–35). The apologetic significance is theological, not merely biological: the virgin birth is the mode of the incarnation, ensuring both Jesus's genuine humanity (born of woman) and his divine sonship (conceived by the Spirit). It guards against Adoptionism (Jesus became divine at baptism) by establishing that he is the Son of God from conception. Critics challenged the historicity of the virgin birth on grounds of alleged pagan parallels (divine hero births) and the silence of other NT texts (Paul, John, Mark). Defenders note that the pagan parallels (Zeus fathering children sexually) are entirely unlike the virginal conception in Luke 1; that Paul's \"born of woman\" (Gal. 4:4) assumes normal birth language without contradicting it; and that the two independent witness sources (Matthew and Luke) satisfy the requirement for substantiation.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "virgin-birth"},
        "key_refs": ["Isaiah 7:14", "Matthew 1:23", "Luke 1:35", "Galatians 4:4", "John 1:14"]
    },
    "parousia": {
        "id": "parousia",
        "term": "Parousia",
        "category": "concepts",
        "intro": "<p>Parousia (Greek <em>parousia</em>, presence, arrival, or coming) is the NT's primary technical term for the second coming of Christ — his visible, personal, glorious return at the end of the age. In secular Greek, <em>parousia</em> described an official visit of a dignitary or king, complete with ceremonial greeting. The NT applies it to Christ's awaited return: Matthew 24:3, 27, 37, 39; 1 Thessalonians 2:19; 3:13; 4:15; 5:23; 2 Thessalonians 2:1, 8–9; James 5:7–8; 2 Peter 1:16; 3:4, 12; 1 John 2:28. The Thessalonian letters give the most sustained eschatological teaching around the parousia: the Lord will descend with a shout, trumpet call, and archangel's voice; the dead in Christ will rise first; then the living believers will be caught up (<em>harpageso</em>, \"raptured\") to meet the Lord in the air (1 Thess. 4:16–17). Paul's second Thessalonian letter corrects misunderstanding: the Day of the Lord has not yet come and awaits the apostasy and the revelation of the man of lawlessness (2 Thess. 2:1–12). The timing of the parousia relative to the tribulation and millennium (pre-, mid-, or post-tribulation; premillennial, amillennial, or postmillennial) is the major division in Protestant eschatology.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "parousia"},
        "key_refs": ["Matthew 24:27", "1 Thessalonians 4:16", "2 Thessalonians 2:8", "James 5:7", "1 John 2:28"]
    },
    "second-coming": {
        "id": "second-coming",
        "term": "Second Coming",
        "category": "concepts",
        "intro": "<p>The second coming of Christ (Greek <em>parousia</em>, <em>epiphaneia</em>, <em>apokalupsis</em>) is the foundational Christian hope for the visible, personal, and glorious return of Jesus Christ at the end of the age to judge the living and the dead, resurrect the dead, and establish his eternal kingdom. It is attested across all strata of the NT: Jesus's own teaching (Matt. 24–25; Mark 13; Luke 21), apostolic preaching (Acts 1:11; 3:20–21; 17:31), Paul's letters (1 Thess. 4:13–18; 2 Thess. 1:7–10; 1 Cor. 15:51–54; Tit. 2:13), the General Epistles (Jas. 5:7–8; 2 Pet. 3:10–13; 1 John 2:28), and Revelation (1:7; 19:11–16; 22:12, 20). The two angels at the ascension promised that \"this same Jesus... will come back in the same way you have seen him go into heaven\" (Acts 1:11). The manner of his return will be visible and universal (\"every eye will see him,\" Rev. 1:7), glorious (Matt. 24:30; 2 Thess. 1:7), sudden as lightning (Matt. 24:27), and unexpected as a thief (Matt. 24:43–44; 1 Thess. 5:2). Its purposes include the resurrection of the dead (John 5:28–29; Rev. 20:4–5), the final judgment (Matt. 25:31–46; Rev. 20:11–15), the renewal of creation (Rom. 8:21; Rev. 21:1–5), and the gathering of the elect (Matt. 24:31; 1 Thess. 4:17).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "second-coming"},
        "key_refs": ["Acts 1:11", "Matthew 24:30", "1 Thessalonians 4:16", "Revelation 1:7", "Titus 2:13"]
    },
    "millennium-postmillennial-view": {
        "id": "millennium-postmillennial-view",
        "term": "Millennium, Postmillennial View",
        "category": "concepts",
        "intro": "<p>Postmillennialism is the eschatological view that Christ will return <em>after</em> (Greek <em>post</em>) the millennium — a long period of spiritual prosperity and gospel triumph during which the church's preaching will progressively Christianize the world and usher in a golden age of righteousness, before Christ's return at the end. The \"millennium\" of Revelation 20:1–6 is interpreted spiritually: the binding of Satan refers to Christ's victory at the cross restricting his ability to deceive nations (John 12:31; Col. 2:15), and the thousand years are symbolic of a prolonged period of gospel advance rather than a literal thousand-year earthly reign. Postmillennialism was the dominant eschatology of Puritan and Reformed theology in the 17th–19th centuries, providing the theological fuel for missionary movements and social reform. Key texts cited include the Great Commission (Matt. 28:18–20), the Davidic psalms of Christ's universal reign (Pss. 2; 72; 110), Paul's vision of the fullness of the Gentiles and \"all Israel\" being saved (Rom. 11:25–26), and the growth parables of the kingdom (Matt. 13:31–33). Postmillennialism declined after World War I but has been revived by Christian Reconstructionism (Rushdoony, Bahnsen) and progressive covenantal theology.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "millennium-postmillennial-view"},
        "key_refs": ["Revelation 20:1", "Matthew 28:19", "Psalm 72:8", "Romans 11:25", "Isaiah 2:2"]
    },
    "millennium-premillennial-view": {
        "id": "millennium-premillennial-view",
        "term": "Millennium, Premillennial View",
        "category": "concepts",
        "intro": "<p>Premillennialism is the eschatological view that Christ will return <em>before</em> (Latin <em>pre</em>) the millennium — a literal thousand-year reign of Christ on earth (Rev. 20:1–6) following his return and the first resurrection. Premillennialism is the oldest organized Christian eschatological scheme, attested in Justin Martyr, Irenaeus, Tertullian, and other early fathers, though later replaced by amillennialism in Augustinian theology. The millennium of Revelation 20 is interpreted literally: Satan is physically bound for a thousand years, the martyrs and saints reign with Christ on earth, and at the end Satan is loosed, the final rebellion crushed, and the great white throne judgment occurs. Premillennialism divides into historic premillennialism (the church passes through the tribulation before Christ's return) and dispensational premillennialism (the church is raptured before the tribulation, God deals separately with Israel during a seven-year tribulation period, and Christ then returns to reign from Jerusalem). Dispensational premillennialism, developed by J.N. Darby (1800–1882) and popularized by the Scofield Reference Bible, became the dominant eschatological scheme in American evangelical and fundamentalist Christianity in the 20th century. Key texts include Daniel 9:24–27; Matthew 24; Revelation 4–22; and the OT promises of national Israel's restoration.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "millennium-premillennial-view"},
        "key_refs": ["Revelation 20:4", "Daniel 7:27", "Zechariah 14:9", "Matthew 24:29", "1 Thessalonians 4:16"]
    },
    "new-heavens": {
        "id": "new-heavens",
        "term": "New Heavens",
        "category": "concepts",
        "intro": "<p>\"New heavens and a new earth\" is the biblical designation for the renewed cosmos that will replace the present creation at the consummation of God's redemptive plan. The promise originates in Isaiah (Isa. 65:17–25; 66:22), where God declares he will create new heavens and a new earth in which the former things — including weeping, death, and premature death — will not be remembered or come to mind, and in which his redeemed people will enjoy shalom, productive labor, and his immediate presence. Peter describes the eschatological transition: the present heavens and earth will be dissolved and purified by fire, and God's people await \"new heavens and a new earth in which righteousness dwells\" (2 Pet. 3:10–13). Revelation's climactic vision centers on this renewal: \"Then I saw a new heaven and a new earth, for the first heaven and the first earth had passed away\" (Rev. 21:1), followed by the descent of the New Jerusalem and the declaration that God will dwell with his people and wipe away every tear (Rev. 21:2–5). Whether the new creation is a total replacement (ex nihilo) or a radical renewal and transformation of the present creation is debated; the Greek word <em>kainos</em> (new in quality) and the analogy of bodily resurrection favor transformation. The new heavens and earth are the eternal home of the redeemed.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "new-heavens"},
        "key_refs": ["Isaiah 65:17", "2 Peter 3:13", "Revelation 21:1", "Isaiah 66:22", "Romans 8:21"]
    },
    "lake-of-fire": {
        "id": "lake-of-fire",
        "term": "Lake of Fire",
        "category": "concepts",
        "intro": "<p>The lake of fire is the Revelation's designation for the place of final, eternal punishment for the devil, his angels, the beast and false prophet, and all whose names are not found written in the book of life (Rev. 19:20; 20:10, 14–15; 21:8). John identifies it explicitly with \"the second death\" (Rev. 20:14; 21:8): the first death is physical; the second death is the eternal separation from God that follows the final judgment. The sequence in Revelation is: the beast and false prophet are thrown into the lake of fire at Christ's return (Rev. 19:20); after the millennium, Satan joins them there (Rev. 20:10); then death and Hades themselves are cast into it (Rev. 20:14); finally, all whose names are not in the book of life (Rev. 20:15). The torment is described as eternal — the same word (<em>eis tous aionas ton aionon</em>, forever and ever) used of God's reign (Rev. 11:15) and the Lamb's glory (Rev. 1:18; 5:13). Jesus elsewhere describes hell as \"eternal fire prepared for the devil and his angels\" (Matt. 25:41) and as <em>Gehenna</em> — the Valley of Hinnom, Jerusalem's burning refuse pit — where the fire is unquenched and the worm does not die (Mark 9:43–48; Isa. 66:24). Annihilationism (final extinction rather than eternal conscious suffering) and conditionalism challenge the traditional view of eternal conscious torment.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "lake-of-fire"},
        "key_refs": ["Revelation 20:14", "Revelation 21:8", "Matthew 25:41", "Mark 9:44", "Revelation 19:20"]
    },
    "resurrection-of-jesus-christ-the": {
        "id": "resurrection-of-jesus-christ-the",
        "term": "Resurrection of Jesus Christ, The",
        "category": "events",
        "intro": "<p>The resurrection of Jesus Christ — his bodily rising from the dead on the third day after his crucifixion — is the central, constitutive event of the Christian faith. Paul states the stakes plainly: \"If Christ has not been raised, your faith is futile and you are still in your sins\" (1 Cor. 15:17). All four Gospels narrate the empty tomb and resurrection appearances; 1 Corinthians 15:3–8 preserves an early creedal tradition (likely dating within 3–5 years of the crucifixion) listing Christ's appearances to Peter, the Twelve, over five hundred brethren at once, James, all the apostles, and finally Paul. The resurrection was bodily: the tomb was empty (all four Gospels), the risen Christ invited Thomas to touch his wounds (John 20:27), he ate fish with the disciples (Luke 24:42–43), and he was physically recognizable as Jesus, not a phantom. Yet his resurrection body was also transformed: he entered locked rooms (John 20:19, 26), was not always immediately recognized (Luke 24:16), and finally ascended into heaven (Acts 1:9). The resurrection is the Father's vindicating declaration that Christ's atoning death was accepted (Rom. 4:25), the basis for the believer's justification (Rom. 4:25), the guarantee of the believer's future resurrection (1 Cor. 15:20–23), and the ground for Christ's cosmic lordship (Rom. 1:4; Phil. 2:9–11).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "resurrection-of-jesus-christ-the"},
        "key_refs": ["1 Corinthians 15:4", "Matthew 28:6", "Romans 4:25", "John 20:27", "Acts 1:3"]
    },
    "day-of-atonement": {
        "id": "day-of-atonement",
        "term": "Day of Atonement",
        "category": "events",
        "intro": "<p>The Day of Atonement (Hebrew <em>Yom Kippur</em>, \"day of coverings\") was the most solemn day of the Israelite religious calendar, observed annually on the tenth day of the seventh month (Tishri), as prescribed in Leviticus 16. On this day alone the High Priest entered the Most Holy Place (the inner sanctum of the tabernacle/temple) to make atonement for himself, his household, and the entire congregation of Israel. The ritual involved two goats: one was sacrificed as a sin offering and its blood sprinkled on the mercy seat (atonement cover) to cleanse the sanctuary from Israel's impurities; the other — the scapegoat (<em>Azazel</em>) — had the high priest confess all Israel's sins over it and was then driven into the wilderness, bearing those sins away (Lev. 16:20–22). The high priest entered with incense whose smoke shielded him from the divine glory (Lev. 16:12–13). The NT presents Christ's death as the ultimate fulfillment of Yom Kippur: the Epistle to the Hebrews expounds this at length, showing Jesus as the eternal High Priest who entered the true sanctuary in heaven with his own blood, achieving not annual but once-for-all atonement (Heb. 9:7–14, 24–28). The mercy seat (Greek <em>hilasterion</em>, Rom. 3:25) is the very word used for Christ as the propitiatory sacrifice. Modern Judaism still observes Yom Kippur as its holiest day, with prayer and fasting replacing the temple sacrifice.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "day-of-atonement"},
        "key_refs": ["Leviticus 16:2", "Leviticus 16:21", "Hebrews 9:12", "Romans 3:25", "Hebrews 10:1"]
    },
    "omnipotence": {
        "id": "omnipotence",
        "term": "Omnipotence",
        "category": "concepts",
        "intro": "<p>Omnipotence (Latin <em>omni</em>, all + <em>potens</em>, powerful) is the divine attribute of unlimited power — God's ability to do all things that are consistent with his nature and will. It is a corollary of his aseity (self-existence) and sovereignty. Scripture affirms it in multiple forms: the divine name <em>El-Shaddai</em> (God Almighty) introduces God to Abraham in connection with covenant promises that seem humanly impossible (Gen. 17:1); the angelic announcement to Mary cites it: \"Nothing will be impossible with God\" (Luke 1:37; cf. Gen. 18:14: \"Is anything too hard for the LORD?\"); God's foundational declaration to Job from the whirlwind invokes his creative power as the basis for questioning Job's presumption (Job 38–41). The theological tradition, following Anselm and Aquinas, defines omnipotence as God's power to do all things that are <em>logically possible</em> — not self-contradictory acts (God cannot make a square circle, cannot lie or deny himself, Tit. 1:2; 2 Tim. 2:13; Heb. 6:18; Num. 23:19). These limitations are not weaknesses but expressions of God's perfect moral nature. Omnipotence grounds confidence in prayer (Matt. 19:26; Eph. 3:20), the execution of judgment (Rev. 19:6), and the certainty of redemptive promises (Rom. 4:21; 2 Tim. 1:12).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "omnipotence"},
        "key_refs": ["Genesis 17:1", "Luke 1:37", "Job 42:2", "Matthew 19:26", "Revelation 19:6"]
    },
    "omnipresence": {
        "id": "omnipresence",
        "term": "Omnipresence",
        "category": "concepts",
        "intro": "<p>Omnipresence is the divine attribute of being fully present everywhere simultaneously — not spread thinly across space but wholly present at every point of creation. It is closely related to divine immensity (God is not contained by any space) and to his Spirit, through which God is present in all creation (Ps. 139:7–10). Psalm 139 is the biblical locus classicus: \"Where shall I go from your Spirit? Or where shall I flee from your presence? If I ascend to heaven, you are there! If I make my bed in Sheol, you are there!\" Solomon acknowledges it at the temple dedication: \"Will God indeed dwell on the earth? Behold, heaven and the highest heaven cannot contain you; how much less this house that I have built!\" (1 Kgs. 8:27). Jeremiah 23:23–24 specifically invokes omnipresence against those who think their hidden sins are unseen: \"Am I a God at hand, declares the LORD, and not a God far away? Can a man hide himself in secret places so that I cannot see him?\" Omnipresence is not to be confused with pantheism (the identification of God with the universe): God is present in his creation but distinct from it as its sovereign Creator. The theological significance is practical: no prayer goes unheard (1 Kgs. 8:27–30), no sin is hidden (Heb. 4:13), and no believer is ever truly alone (Matt. 28:20; Heb. 13:5).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "omnipresence"},
        "key_refs": ["Psalm 139:7", "1 Kings 8:27", "Jeremiah 23:23", "Hebrews 4:13", "Matthew 28:20"]
    },
    "omniscience": {
        "id": "omniscience",
        "term": "Omniscience",
        "category": "concepts",
        "intro": "<p>Omniscience is the divine attribute of complete, perfect, and exhaustive knowledge — God's awareness of all things actual and possible, past, present, and future, including all human thoughts, motivations, and deeds. Scripture repeatedly affirms it: \"His understanding is unsearchable\" (Isa. 40:28); \"God is greater than our heart, and he knows everything\" (1 John 3:20); \"No creature is hidden from his sight, but all are naked and exposed to the eyes of him to whom we must give account\" (Heb. 4:13). The Psalms celebrate it in personal terms: God knows the thoughts of humans (Ps. 94:11; 139:1–4) and numbers the very hairs of the head (Matt. 10:30). Divine foreknowledge — God's knowledge of future events, including free human choices — has generated significant theological debate. Calvinism holds that God knows the future because he sovereignly determines it (compatibilist foreknowledge). Arminianism holds that God foreknows genuinely free human choices without determining them. Open theism (a minority position) argues that future free choices are genuinely unknowable even to God, limiting divine omniscience to what is knowable. Open theism has been widely criticized as incompatible with biblical prophecy (detailed predictions of specific freely-chosen acts, Isa. 44:28; Jer. 1:5; John 13:18–19) and with classical theism's account of divine perfection.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "omniscience"},
        "key_refs": ["Psalm 139:1", "1 John 3:20", "Hebrews 4:13", "Isaiah 40:28", "Romans 11:33"]
    },
    "foreknow;-foreknowledge": {
        "id": "foreknow;-foreknowledge",
        "term": "Foreknow; Foreknowledge",
        "category": "concepts",
        "intro": "<p>Divine foreknowledge (Greek <em>prognosis</em>, <em>proginosko</em>) refers to God's knowledge of persons or events before they occur, a concept with both simple epistemic content (God knows what will happen) and in biblical usage often a deeper relational sense of prior covenantal intimacy. The Septuagint and NT use of <em>yada</em>/ginosko suggests that \"knowing\" can mean intimate, relational acknowledgment, not merely informational awareness (cf. Gen. 18:19; Jer. 1:5; Amos 3:2; Matt. 7:23). In Romans 8:29, \"those whom he foreknew he also predestined to be conformed to the image of his Son\" — where Calvinist interpreters read foreknowledge as the relational forelove that grounds predestination, and Arminian interpreters read it as God's advance knowledge of who would believe. First Peter 1:2 addresses Christians as chosen \"according to the foreknowledge of God the Father.\" Acts 2:23 attributes Jesus's crucifixion to God's \"definite plan and foreknowledge,\" demonstrating that foreknowledge does not eliminate human agency (the Jews acted wickedly). Peter also describes Christ as \"foreknown before the foundation of the world\" (1 Pet. 1:20), making the eternal purpose behind the incarnation the ground of the believer's faith. The relationship between divine foreknowledge and human freedom is among Christian theology's most discussed problems.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "foreknow;-foreknowledge"},
        "key_refs": ["Romans 8:29", "1 Peter 1:2", "Acts 2:23", "Romans 11:2", "1 Peter 1:20"]
    },
    "redeemer;-redemption": {
        "id": "redeemer;-redemption",
        "term": "Redeemer; Redemption",
        "category": "concepts",
        "intro": "<p>Redemption (Hebrew <em>ga'al</em>, <em>padah</em>; Greek <em>lutroo</em>, <em>agorazo</em>, <em>exagorazo</em>) is the deliverance of persons from bondage, guilt, or death through the payment of a price — a concept rooted in Israel's Exodus and elaborated as the theological heart of the NT's account of salvation. The <em>goel</em> (kinsman-redeemer) of OT law was the near relative who had the right and obligation to redeem a family member sold into slavery, to redeem forfeited property, or to avenge innocent blood (Lev. 25:25, 47–49; Num. 35:19). God exercises this role for Israel nationally — \"I will redeem you with an outstretched arm\" (Ex. 6:6) — and is celebrated as Israel's ultimate Redeemer in Isaiah (Isa. 41:14; 43:1; 44:6; 47:4; 48:17). Job's confidence in his living Redeemer (Job 19:25) anticipates the NT application. In the NT, Christ's redemption is comprehensive: he redeems from the curse of the law by becoming a curse (Gal. 3:13), from slavery to sin (John 8:36; Rom. 6:18), from death (Heb. 2:14–15), and unto God as his own purchased people (1 Pet. 1:18–19; Rev. 5:9). The price is his own blood (Acts 20:28; 1 Cor. 6:20; Eph. 1:7), not silver or gold (1 Pet. 1:18). Redemption is both accomplished (Col. 1:14) and awaited — the final redemption of the body at resurrection (Rom. 8:23; Eph. 4:30).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "redeemer;-redemption"},
        "key_refs": ["Leviticus 25:25", "Isaiah 41:14", "Galatians 3:13", "1 Peter 1:18", "Revelation 5:9"]
    },
    "biblical-theology": {
        "id": "biblical-theology",
        "term": "Biblical Theology",
        "category": "concepts",
        "intro": "<p>Biblical theology is the discipline that traces the progressive revelation of God's redemptive purposes across the canon of Scripture, attending to the historical development and unfolding of theological themes within their own historical and literary contexts. It is distinguished from systematic theology (which organizes biblical teaching topically and systematically across all of Scripture simultaneously) and from historical theology (which traces the church's doctrinal development). Biblical theology as a distinct academic discipline was pioneered in J.P. Gabler's inaugural lecture at Altdorf (1787), which distinguished \"biblical theology\" (descriptive, historically conditioned) from \"dogmatic theology\" (normative, philosophical). Within evangelical scholarship, biblical theology pursues the unified redemptive-historical story of Scripture: creation, fall, promise (to Abraham), the Mosaic covenant, the Davidic kingdom, the exile, the prophetic hope, and the fulfillment in Christ's first and second comings, with the church as the eschatological community between the ages. Key figures include Geerhardus Vos (<em>Biblical Theology</em>, 1948), who established the discipline's theological rigor in Reformed circles; D.A. Carson and Frank Thielman in NT biblical theology; and W. Dyrness and Bruce Waltke in OT biblical theology. Biblical theology illuminates how earlier texts are taken up, deepened, and transformed in later texts (typology, promise-fulfillment, intertextuality).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "biblical-theology"},
        "key_refs": ["Luke 24:27", "Romans 1:2", "Hebrews 1:1", "2 Timothy 3:16", "Galatians 4:4"]
    },
    "absolution": {
        "id": "absolution",
        "term": "Absolution",
        "category": "concepts",
        "intro": "<p>Absolution (Latin <em>absolutio</em>, a releasing) is the pronouncement of forgiveness of sins — either by God directly (as in Scripture's declarations of forgiveness) or, in Roman Catholic, Lutheran, and some Anglican traditions, by a priest or minister as an authorized agent of divine forgiveness. The theological question is whether the minister declares God's forgiveness (declaratory absolution) or instrumentally conveys it (judicial or sacramental absolution). The NT grounds for absolution include John 20:23: \"If you forgive the sins of any, they are forgiven them; if you withhold forgiveness from any, it is withheld\" — the key text cited for priestly absolution. Protestant exegesis reads this as the church's authority to declare the gospel's terms of forgiveness and to apply them in church discipline, not a sacerdotal power to pronounce individual forgiveness ex opere operato. Roman Catholic practice requires confession to a priest, contrition, and the performance of a penance as the form of the sacrament of Reconciliation (Penance), after which the priest pronounces absolution with the formula \"I absolve you.\" Lutheran practice retains private confession and absolution as a means of grace. Reformed and Baptist traditions emphasize direct access to God through Christ as the one mediator (1 Tim. 2:5; Heb. 4:16) and the priesthood of all believers (1 Pet. 2:9).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "absolution"},
        "key_refs": ["John 20:23", "Matthew 16:19", "1 Timothy 2:5", "Hebrews 4:16", "1 John 1:9"]
    },
    "abstinence": {
        "id": "abstinence",
        "term": "Abstinence",
        "category": "concepts",
        "intro": "<p>Abstinence in Scripture refers to the voluntary refusal of food, drink, or other pleasures for spiritual, ceremonial, or ethical reasons. The OT prescribed fasting on the Day of Atonement (Lev. 16:29–31) and regulated abstinence from certain foods through the dietary laws. Nazirites abstained from wine and all grape products for the duration of their vow (Num. 6:2–4). The prophetic tradition sometimes involved abstinence as mourning and intercession: Daniel ate no delicacies for three weeks (Dan. 10:3). The NT treats abstinence with notable nuance. It affirms physical self-control (<em>enkrateia</em>, Gal. 5:23; 1 Cor. 9:25–27) and the legitimacy of fasting as a private spiritual discipline (Matt. 6:16–18: \"when you fast,\" not \"if you fast\"). But it strongly resists abstinence as a salvific requirement: Paul warns against those who \"forbid marriage and require abstinence from foods that God created to be received with thanksgiving\" (1 Tim. 4:3). Romans 14–15 and 1 Corinthians 8–10 address the problem of foods offered to idols, counseling the strong to abstain voluntarily out of love for the weak, though the food is not intrinsically defiling (Rom. 14:14; Mark 7:19). The NT principle is that all things are lawful for the believer (1 Cor. 10:23) but not all things are beneficial — abstinence is a matter of love and wisdom, not law.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "abstinence"},
        "key_refs": ["1 Timothy 4:3", "Romans 14:3", "1 Corinthians 9:25", "Galatians 5:23", "Matthew 6:17"]
    },
    "abyss": {
        "id": "abyss",
        "term": "Abyss",
        "category": "concepts",
        "intro": "<p>The Abyss (Greek <em>abyssos</em>, \"bottomless\" or \"unfathomable depth\") designates in the NT and Jewish apocalyptic literature the place of imprisonment for demons and fallen angels — the netherworld as a prison of spiritual forces opposed to God. In the LXX, <em>abyssos</em> translates the Hebrew <em>tehom</em> (the deep, the primordial waters of creation, Gen. 1:2), and in some passages refers to the depths of the sea (Ps. 107:26; Jon. 2:3). In the NT, the abyss takes on a more specifically eschatological character. The demons who possessed the Gerasene/Gadarene man pleaded with Jesus \"not to command them to depart into the abyss\" (Luke 8:31), indicating it as a place of restrained judgment. In Revelation, the abyss is a sealed prison from which the demonic army of the fifth trumpet emerges under Abaddon/Apollyon (Rev. 9:1–11); it is the domain from which the beast ascends (Rev. 11:7; 17:8); and it is the place into which Satan is cast and sealed for the millennium before his final release (Rev. 20:1–3). Paul uses the term in Romans 10:7 (quoting Deut. 30:13) for the depths of the sea or the realm of the dead. The abyss is thus a liminal concept — the boundary between the created order and the realm of imprisoned spiritual powers awaiting final judgment.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "abyss"},
        "key_refs": ["Revelation 9:1", "Revelation 20:1", "Luke 8:31", "Romans 10:7", "Revelation 11:7"]
    },
    "accountability": {
        "id": "accountability",
        "term": "Accountability",
        "category": "concepts",
        "intro": "<p>Accountability in biblical ethics and theology refers to the obligation of moral agents to give account of their actions, beliefs, and stewardship to God as the ultimate Judge. Scripture consistently presents every human being as accountable to God: \"Each of us will give an account of himself to God\" (Rom. 14:12); \"We must all appear before the judgment seat of Christ, so that each one may receive what is due for what he has done in the body, whether good or evil\" (2 Cor. 5:10). Human accountability is grounded in the creation of humanity in the image of God (Gen. 1:26–27), the moral law written on the conscience (Rom. 2:14–16), and the universal witness of creation to God's power and character (Rom. 1:19–20). Both Jew and Gentile are accountable: the Gentile by natural law and conscience; the Jew by explicit covenant revelation (Rom. 2:12–13; 3:19). Ecclesiastes grounds universal accountability in the final judgment: \"God will bring every deed into judgment, with every secret thing, whether good or evil\" (Eccl. 12:14). In the NT, accountability encompasses secret thoughts and intentions (1 Cor. 4:5; Heb. 4:12–13; Matt. 12:36–37), stewardship of gifts, abilities, and resources (Matt. 25:14–30; Luke 12:48), and specifically the accountability of teachers who will be judged more strictly (Jas. 3:1).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "accountability"},
        "key_refs": ["Romans 14:12", "2 Corinthians 5:10", "Hebrews 4:13", "Ecclesiastes 12:14", "Matthew 12:36"]
    },
    "accursed": {
        "id": "accursed",
        "term": "Accursed",
        "category": "concepts",
        "intro": "<p>\"Accursed\" (Hebrew <em>herem</em>, devoted to destruction; Greek <em>anathema</em>, set apart for divine judgment) designates persons or things placed under divine curse and devoted to destruction. In OT holy war, items and peoples were declared <em>herem</em> — totally devoted to destruction as belonging wholly to God, with no portion to be kept for human use (Josh. 6:17–19; 7:1, 11–13). Achan's sin of secretly keeping <em>herem</em> items brought judgment on all Israel (Josh. 7:1–26). The LXX translates <em>herem</em> with <em>anathema</em>, which carries the related meaning of something devoted to God — either in the positive sense of a votive offering (Luke 21:5) or the negative sense of devoted to destruction and divine curse. Paul uses <em>anathema</em> with full force: he pronounces anathema on any who preach a different gospel — even an angel or Paul himself (Gal. 1:8–9). In 1 Corinthians 12:3, no one speaking by the Spirit says \"Jesus is accursed (<em>anathema</em>)\"; the opposite confession — \"Jesus is Lord\" — is the mark of the Spirit. The most startling usage is Paul's conditional self-imprecation in Romans 9:3: he could wish himself accursed (<em>anathema</em>) from Christ for the sake of his kinsmen — a hyperbolic expression of intercession, not a doctrinal claim about forfeiting salvation.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "accursed"},
        "key_refs": ["Joshua 6:17", "Galatians 1:8", "Romans 9:3", "1 Corinthians 12:3", "Deuteronomy 7:26"]
    },
    "adam-in-the-new-testament": {
        "id": "adam-in-the-new-testament",
        "term": "Adam In the New Testament",
        "category": "people",
        "intro": "<p>In the NT, Adam is treated as a historical individual whose transgression introduced sin and death into the human race — the first Adam whose role as representative head is answered and reversed by Christ, the last Adam. Paul's two extended treatments are the theological center: Romans 5:12–21 and 1 Corinthians 15:21–22, 45–49. In Romans 5, Paul traces the universal reign of sin and death to \"one man\" (Adam) in whom all sinned — the basis of the doctrine of original sin and original guilt, contested since Augustine and Pelagius. The structure is typological: Adam as <em>typos</em> (Rom. 5:14) prefigures Christ, but the contrast is asymmetrical — grace superabounds over the trespass. In 1 Corinthians 15, Paul works out the contrast between the first Adam (the living soul, Gen. 2:7) and the last Adam (the life-giving Spirit): physical resurrection follows the pattern set by Christ, as physical death followed the pattern set by Adam. Jesus's genealogy in Luke 3:38 traces his human lineage to \"Adam, the son of God.\" Jude 14 quotes 1 Enoch attributing a prophecy to Enoch, seventh from Adam. The NT's historical treatment of Adam has been a flashpoint in debates over the relationship between evolutionary science and theology.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "adam-in-the-new-testament"},
        "key_refs": ["Romans 5:12", "1 Corinthians 15:22", "1 Corinthians 15:45", "Luke 3:38", "Romans 5:14"]
    },
    "adam-in-the-old-testament": {
        "id": "adam-in-the-old-testament",
        "term": "Adam In the Old Testament",
        "category": "people",
        "intro": "<p>Adam (Hebrew <em>adam</em>, humanity, or man; connected with <em>adamah</em>, ground) is presented in Genesis as the first human being, formed from the ground by divine action, receiving the breath of life, placed in the garden of Eden, and given the commission to work and keep it and to exercise dominion over the creation (Gen. 1:26–28; 2:7, 15). His name is both individual and generic: as <em>ha-adam</em> (the man, the human), he represents humanity collectively; as the recipient of Eve from his own rib (Gen. 2:21–23), he establishes the pattern of marriage. The garden narrative culminates in the transgression: Adam and Eve ate the forbidden fruit at the serpent's instigation (Gen. 3:1–7), God pronounced curses on serpent, woman, and man, and expelled them from Eden with toil, pain, and mortality as the consequences. In the OT outside Genesis, Adam is rarely mentioned explicitly (Deut. 32:8 LXX; Job 31:33; Hos. 6:7; Eccl. 7:29), but the Adamic framework — humanity's dignity, responsibility, and fallenness — permeates the whole. The genealogies of Genesis 5 and Chronicles 1 trace the line from Adam to later patriarchs and ultimately to Israel. Whether the Genesis narrative is intended as literal historical reportage or as theological narrative employing ancient Near Eastern literary conventions is actively debated in contemporary scholarship.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "adam-in-the-old-testament"},
        "key_refs": ["Genesis 1:26", "Genesis 2:7", "Genesis 3:6", "Genesis 3:19", "Genesis 5:1"]
    },
    "angel-of-god": {
        "id": "angel-of-god",
        "term": "Angel of God",
        "category": "concepts",
        "intro": "<p>\"The angel of God\" (Hebrew <em>mal'ak ha-elohim</em>) is a designation used interchangeably in some OT texts with \"the angel of the LORD\" (<em>mal'ak YHWH</em>) for a divine messenger who speaks with the authority of God, appears as God, and sometimes is identified with God himself. In Hagar's narrative, \"the angel of the LORD\" speaks to her in the wilderness (Gen. 16:7–13) and is identified as God: \"She called the name of the LORD who spoke to her, 'You are a God of seeing'\" (Gen. 16:13). Jacob wrestles with a mysterious being at the Jabbok (Gen. 32:24–30) who is later described as an angel by Hosea (Hos. 12:4) while Jacob declares he \"saw God face to face.\" At the burning bush, the angel of the LORD appears (Ex. 3:2) but then God himself speaks (Ex. 3:4ff). This oscillation between angel and God has led theologians — particularly from Origen and Justin Martyr onward — to identify the angel of the LORD as a pre-incarnate appearance of the Son of God (a Christophany). This interpretation is not universally accepted: some scholars understand the angel as a representative bearing the divine name by delegation (Ex. 23:20–21), not as a distinct divine person. The NT nowhere explicitly identifies the angel of the LORD as the pre-incarnate Christ, though the category of divine representation is consistent with the Logos Christology of John 1.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "angel-of-god"},
        "key_refs": ["Genesis 16:7", "Genesis 32:28", "Exodus 3:2", "Judges 13:22", "Exodus 23:20"]
    },
    "angel-of-yahweh": {
        "id": "angel-of-yahweh",
        "term": "Angel of Yahweh",
        "category": "concepts",
        "intro": "<p>The Angel of Yahweh (Hebrew <em>mal'ak YHWH</em>, \"messenger of the LORD\") is a theologically significant figure in the OT whose appearances are characterized by the same identity oscillation as the Angel of God: the angel speaks with divine authority, is worshipped as God, and is identified with God, yet is also distinguished from him as a sent messenger. Key appearances: at the burning bush (Ex. 3:2–6), where the angel is and then becomes God speaking; to Gideon (Judg. 6:11–24), who says \"I have seen the angel of the LORD face to face\" in fear of death; to Manoah (Judg. 13:3–22), whose name is \"wonderful\" (cf. Isa. 9:6) and who ascends in the flame; and to Elijah (1 Kgs. 19:5–7). In Zechariah's visions, the angel of the LORD intercedes for Jerusalem (Zech. 1:12), and in Zechariah 3 stands beside Joshua the high priest while contending with Satan. This figure is distinct from ordinary angels in three respects: he bears and speaks the divine name (Ex. 23:20–21), receives worship without correcting the worshipper, and is identified with God in the text. The majority of church fathers interpreted this as a pre-incarnate manifestation of the second person of the Trinity; a minority reading understands him as God's fully authorized representative who speaks in God's name without being a distinct divine person.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "angel-of-yahweh"},
        "key_refs": ["Exodus 3:2", "Judges 6:22", "Judges 13:18", "Zechariah 1:12", "Malachi 3:1"]
    },
    "advent": {
        "id": "advent",
        "term": "Advent",
        "category": "concepts",
        "intro": "<p>Advent (Latin <em>adventus</em>, arrival or coming) designates in Christian theology the two comings of Christ: his first advent in the incarnation (the historical event of his birth, life, death, and resurrection) and his second advent at the end of the age (his visible, glorious return in judgment and salvation). As a liturgical season, Advent is the four-week period of preparation preceding Christmas in the Western church, observed since at least the 4th–5th centuries, combining penitential reflection on human need with joyful anticipation of Christ's coming. The dual focus of Advent — on the first coming already accomplished and the second coming yet awaited — is theologically rich: Christians live between the advents, in the \"already/not yet\" tension of the kingdom. The OT prophets spoke of the coming of the LORD in both immediate-historical and eschatological senses (Isa. 9:6; 40:3; Mal. 3:1), with NT retrospection seeing the first advent as fulfillment and the second as the remaining goal. The Advent season's scriptural themes include John the Baptist's preparation ministry (Matt. 3:1–3; Isa. 40:3), Mary's Magnificat (Luke 1:46–55), the messianic promises (Isa. 7:14; 9:1–7; 11:1–9), and eschatological readiness (Matt. 24:42–44; Rom. 13:11–14). The theological center of Advent is Christ himself — Emmanuel, God with us — who came, who comes in Word and Spirit, and who will come again.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "advent"},
        "key_refs": ["Isaiah 9:6", "Matthew 3:1", "Galatians 4:4", "Hebrews 9:28", "Revelation 22:20"]
    },
    "anthropomorphism": {
        "id": "anthropomorphism",
        "term": "Anthropomorphism",
        "category": "concepts",
        "intro": "<p>Anthropomorphism (from Greek <em>anthropos</em>, human + <em>morphe</em>, form) in biblical studies refers to the use of human bodily features, emotions, or actions to describe God — language that gives God human form and characteristics to communicate divine truth in terms accessible to human understanding. Scripture is replete with such language: God has hands (Ex. 7:5), an arm (Isa. 51:5), eyes (2 Chr. 16:9), ears (Ps. 116:2), a face (Num. 6:25–26), and nostrils (Ex. 15:8). He speaks, hears, sees, walks, rests, laughs, and grieves. In Genesis 3:8, God walks in the garden in the cool of the day. Moses speaks with God \"face to face, as a man speaks to his friend\" (Ex. 33:11), though the same chapter qualifies this by insisting no one can see God's full face and live (Ex. 33:20). Theologians have treated anthropomorphism variously: Maimonides and much of medieval Jewish and Christian philosophy interpreted such language as purely metaphorical, to be allegorized away; Reformation and orthodox Protestant theology maintained that anthropomorphisms are accommodations by which the infinite God condescends to communicate with finite humans (Calvin's <em>accommodatio</em>), while insisting on God's spiritual, non-physical nature (John 4:24); recent evangelical scholarship (Frame, Feinberg) debates whether \"literal\" application of some personal-attribute language to God is more appropriate than always reading it metaphorically.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "anthropomorphism"},
        "key_refs": ["Exodus 33:11", "Isaiah 51:5", "Exodus 15:8", "Genesis 3:8", "Numbers 6:25"]
    },
    "apostasy;-apostate": {
        "id": "apostasy;-apostate",
        "term": "Apostasy; Apostate",
        "category": "concepts",
        "intro": "<p>Apostasy (Greek <em>apostasia</em>, a standing away from; <em>apostates</em>, one who forsakes) is the formal abandonment or renunciation of the Christian faith — or, in the OT, of covenant loyalty to God. OT apostasy includes Israel's recurring defection to Baal worship (1 Kgs. 11:4–9; 2 Kgs. 17:7–18) and the individual's turning from God to idolatry, condemned by prophets and punished under the covenant curses (Deut. 13:1–5; 17:2–7). In the NT, <em>apostasia</em> appears twice: Acts 21:21 (accusation that Paul teaches apostasy from Moses) and 2 Thessalonians 2:3, where Paul predicts a great apostasy preceding the Day of the Lord. The warning passages in Hebrews are the most contested: Hebrews 6:4–8 warns that those who have tasted the heavenly gift and shared in the Holy Spirit and then fall away make it impossible to renew them to repentance. Whether this describes genuinely regenerate persons who finally apostatize (Arminian reading) or those who had real but non-saving exposure to Christian community and truth (Reformed reading) is one of NT theology's most discussed exegetical questions. 1 John 2:19 states: \"They went out from us, but they were not of us; for if they had been of us, they would have continued with us.\" Paul warns Timothy that some will depart from the faith in the last days (1 Tim. 4:1; 2 Tim. 3:1–5; 4:3–4).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "apostasy;-apostate"},
        "key_refs": ["2 Thessalonians 2:3", "Hebrews 6:4", "1 John 2:19", "1 Timothy 4:1", "Hebrews 3:12"]
    },
    "apostolic-age": {
        "id": "apostolic-age",
        "term": "Apostolic Age",
        "category": "concepts",
        "intro": "<p>The apostolic age designates the period of the church's history from Pentecost (c. 30 A.D.) to the death of the last apostle (traditionally John, c. 100 A.D.) — the foundational era when the church was governed by eyewitnesses of the resurrection and when the NT was composed. The apostles (Greek <em>apostoloi</em>, sent ones) held a unique, non-repeatable authority as those commissioned directly by the risen Christ (Acts 1:21–22; 1 Cor. 9:1; 15:7–8; Gal. 1:1), who received authoritative revelation and whose teaching formed the doctrinal standard for the church (Eph. 2:20; Acts 2:42). The apostolic age is marked by rapid geographical expansion (Acts 1:8; Rom. 15:19–20), internal doctrinal controversy resolved by apostolic council (Acts 15), external persecution, and the emergence of the canon through apostolic authorization. The concept of the apostolic age is theologically significant for ecclesiology and canon: cessationists and Protestants generally hold that the apostolic office (with its foundational, revelatory function) ended with the first generation, the canon being closed; charismatics and Pentecostals hold that the spiritual gifts of the apostolic age continue; Roman Catholicism holds that apostolic authority continues through episcopal succession. The Apostolic Fathers (Clement, Ignatius, Polycarp, Didache) are the primary literary bridge between the NT and the 2nd century.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "apostolic-age"},
        "key_refs": ["Acts 1:8", "Ephesians 2:20", "Acts 2:42", "1 Corinthians 9:1", "Galatians 1:1"]
    },
    "athanasian;-creed": {
        "id": "athanasian;-creed",
        "term": "Athanasian Creed",
        "category": "concepts",
        "intro": "<p>The Athanasian Creed (Latin <em>Quicumque vult</em>, \"Whoever wishes to be saved\") is one of the three ecumenical creeds of Western Christianity, alongside the Apostles' and Nicene Creeds, providing the most detailed and precise statement of Trinitarian and Christological doctrine. Despite its name, it was not written by Athanasius of Alexandria (c. 296–373) — that attribution is medieval — but is now dated to the late 5th or early 6th century, probably of Gallic or North African origin. The creed comprises two parts: a Trinitarian section (affirming that the three persons are co-equal, co-eternal, and uncreated yet constitute one God) and a Christological section (affirming that Christ is one person in two complete natures — fully God and fully man). Its distinctive feature is the use of damnatory clauses: \"Whoever wishes to be saved must, above all, hold the catholic faith... which faith unless each one preserves whole and undefiled, he will without doubt perish eternally.\" These anathemas have made the creed controversial for ecumenical dialogue. It is accepted by Roman Catholic, Lutheran, and Anglican traditions and was historically used in their liturgies; it has less liturgical use in Reformed churches but is affirmed in confessional documents.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "athanasian;-creed"},
        "key_refs": ["Matthew 28:19", "John 1:1", "John 1:14", "Philippians 2:6", "1 John 5:7"]
    },
    "authority-in-religion": {
        "id": "authority-in-religion",
        "term": "Authority in Religion",
        "category": "concepts",
        "intro": "<p>Authority in religion addresses the question of what ultimate norm governs Christian belief and practice — what or who has the right to determine what Christians must believe and how they must live. The major positions correspond to the great divisions of Christendom. Roman Catholicism holds to a dual-source authority: Scripture and Sacred Tradition as interpreted by the Magisterium (the teaching authority of the church, centered in the papacy, with infallibility defined by Vatican I, 1870, and Vatican II, 1962–65). Eastern Orthodoxy grounds authority in Scripture, tradition, and the consensus of the seven ecumenical councils, without a single papal head. Protestantism's Reformation principle is <em>sola scriptura</em> (Scripture alone as the supreme norm of faith and practice), though tradition (creeds, confessions, church councils) serves as a subordinate authority. Scripture's own claim to authority is grounded in divine inspiration: \"All Scripture is God-breathed\" (2 Tim. 3:16–17; cf. 2 Pet. 1:20–21). Jesus consistently appealed to Scripture as final authority (Matt. 5:17–18; John 10:35: \"Scripture cannot be broken\"). The challenge of <em>sola scriptura</em> is the interpretive question — who interprets Scripture? — which Protestant ecclesiology addresses through the hermeneutical community of the church under the Spirit's guidance, creeds, and confessions as secondary authorities.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "authority-in-religion"},
        "key_refs": ["2 Timothy 3:16", "John 10:35", "Matthew 5:17", "2 Peter 1:20", "Isaiah 8:20"]
    },
    "between-the-testaments": {
        "id": "between-the-testaments",
        "term": "Between the Testaments",
        "category": "concepts",
        "intro": "<p>\"Between the Testaments\" (also called the intertestamental period or Second Temple period) designates the roughly 400 years separating the close of the OT canon (c. 400 B.C., the time of Malachi) from the ministry of John the Baptist and Jesus (c. 27–30 A.D.) — a period of theological development and political upheaval that is essential background for understanding the NT. The period is subdivided by major political transitions: Persian rule (to 333 B.C.), Greek/Hellenistic rule under Alexander and the Diadochi (333–168 B.C.), the Maccabean revolt and Hasmonean kingdom (168–63 B.C.), and Roman rule from Pompey's conquest (63 B.C.) onward. The religious literature of the period (Apocrypha, Pseudepigrapha, Dead Sea Scrolls, Philo, Josephus) reveals a Judaism diversified into Pharisees, Sadducees, Essenes, Zealots, and other groups, each with distinctive theological emphases. Key theological developments include: a heightened angelology and demonology; apocalyptic thought and eschatological expectation; messianic hopes; the synagogue as the center of Jewish life; the Oral Torah's development; and heightened expectation for divine intervention. The NT's frequent references to Jewish interpretive traditions, sectarian debates, and eschatological language are comprehensible only against this intertestamental background.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "between-the-testaments"},
        "key_refs": ["Malachi 4:5", "Matthew 3:1", "Galatians 4:4", "Luke 2:25", "Mark 1:15"]
    },
    "baptism-infant": {
        "id": "baptism-infant",
        "term": "Baptism, Infant",
        "category": "concepts",
        "intro": "<p>Infant baptism (paedobaptism, from Greek <em>pais</em>, child) is the practice of baptizing the infants of Christian parents, widely practiced in Roman Catholic, Eastern Orthodox, Lutheran, Reformed, and Anglican traditions. Its theological defense rests on the covenant theology of the OT: as circumcision was the covenant sign for infant males in Abraham's household (Gen. 17:9–14), so baptism is the corresponding covenant sign in the new covenant, applied to the children of believers as members of the covenant community (Col. 2:11–12). The Great Commission's \"baptizing them\" (Matt. 28:19) includes, on this view, household members; household baptisms in Acts (Cornelius, Acts 10:48; Lydia, Acts 16:15; the Philippian jailer, Acts 16:33; Crispus, Acts 18:8; Stephanas, 1 Cor. 1:16) likely included infants. Jesus's blessing of children and declaration that \"of such is the kingdom of heaven\" (Matt. 19:13–15; Mark 10:14) is cited as affirming their covenant standing. The opposing credobaptist (Baptist, Anabaptist) position holds that baptism must follow a conscious, personal profession of faith, that infant baptism has no explicit NT warrant, and that the new covenant community is composed only of the regenerate. The debate turns on the relationship between the covenants, the nature of the church, and the meaning of baptism as sign and seal.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "baptism-infant"},
        "key_refs": ["Genesis 17:12", "Colossians 2:11", "Matthew 19:14", "Acts 16:33", "Matthew 28:19"]
    },
    "barnabas-epistle-of": {
        "id": "barnabas-epistle-of",
        "term": "Barnabas, Epistle of",
        "category": "concepts",
        "intro": "<p>The Epistle of Barnabas is an early Christian writing preserved in Codex Sinaiticus (4th century) and various other manuscripts, dating most likely to the period between 70 and 135 A.D. Despite its traditional attribution to Barnabas (Paul's companion, Acts 4:36; 9:27; 13–14), ancient and modern scholarship generally rejects this ascription — the letter is anonymous and its author's identity is unknown. It was highly regarded in some early Christian circles: Clement of Alexandria and Origen cite it with respect, though Eusebius classified it among the <em>antilegomena</em> (disputed books) and never considered it canonical. The letter is primarily an allegory-intensive typological exposition of the OT, arguing that the Jewish interpretation of Scripture has been superseded by the Christian reading, which sees Christ as the true fulfillment of the law and the covenant. Its treatment of the OT dietary laws (Barnabas 10) is radically allegorical: the prohibition on eating unclean animals is interpreted as a prohibition against associating with wicked people, not a food law. The letter also contains an early version of the Two Ways (ethical instruction) material also found in the Didache. It is valuable as a witness to early Christian biblical interpretation, anti-Judaism in 2nd-century Christianity, and the diversity of early theological expression.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "barnabas-epistle-of"},
        "key_refs": ["Acts 4:36", "Hebrews 1:1", "2 Peter 1:20", "Galatians 4:24"]
    },
    "benediction": {
        "id": "benediction",
        "term": "Benediction",
        "category": "concepts",
        "intro": "<p>A benediction (Latin <em>benedictio</em>, speaking well; Greek <em>eulogia</em>) is a formal blessing pronounced over persons, typically at the conclusion of a worship service or in a significant relational or covenantal context. The paradigmatic OT benediction is the Aaronic blessing given by God to Moses as the form of priestly blessing over Israel: \"The LORD bless you and keep you; the LORD make his face shine on you and be gracious to you; the LORD turn his face toward you and give you peace\" (Num. 6:24–26). God's own name is thereby placed upon the people (Num. 6:27). Patriarchal blessings carry covenantal weight: Isaac's blessing of Jacob (Gen. 27) and Jacob's blessings of his sons (Gen. 49) are prophetic-covenantal acts with enduring significance. The Psalms of Ascent (Pss. 120–134) contain benedictions associated with pilgrimage and temple worship. In the NT, benedictions appear at the conclusions of letters as theologically rich summaries: the grace benediction (\"The grace of the Lord Jesus Christ be with you,\" 1 Cor. 16:23; Rev. 22:21), the Trinitarian benediction (2 Cor. 13:14: \"The grace of the Lord Jesus Christ and the love of God and the fellowship of the Holy Spirit be with you all\"), and the peace benedictions characteristic of Paul's letters. Jesus blesses his disciples at the ascension (Luke 24:50–51). The benediction in Christian worship is not a wish but a declaration of divine favor, commissioned and authorized by God.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "benediction"},
        "key_refs": ["Numbers 6:24", "2 Corinthians 13:14", "Luke 24:50", "Genesis 49:28", "Revelation 22:21"]
    },
    "holy-ghost-spirit-sin-against-the": {
        "id": "holy-ghost-spirit-sin-against-the",
        "term": "Holy Ghost (Spirit), Sin Against The",
        "category": "concepts",
        "intro": "<p>The sin against the Holy Spirit — the so-called \"unforgivable sin\" or \"blasphemy against the Holy Spirit\" — is identified by Jesus as the one sin for which there is no forgiveness either in this age or the age to come (Matt. 12:31–32; Mark 3:28–29; Luke 12:10). The immediate context is the Pharisees' accusation that Jesus casts out demons by Beelzebul (Matt. 12:24; Mark 3:22), attributing the Holy Spirit's work in Christ to Satan. Jesus identifies this as blasphemy against the Holy Spirit — a deliberate, knowing rejection of and opposition to the Spirit's clear testimony to Christ, hardening the heart beyond recovery. Interpreters have debated the precise nature and boundaries of this sin. The patristic and Reformation majority held it to be not a single act but a settled state: the deliberate, persistent, and final rejection of the Spirit's convicting work and testimony to Christ. Augustine located it in final impenitence. Hebrews 6:4–6 and 10:26–29 describe similar states. The pastoral application is significant: those who fear they have committed the unforgivable sin demonstrate by their very fear and desire for forgiveness that they have not — for the sin involves a settled rejection of God's mercy, not anxiety about having offended him. The sin is irremediable not because God's mercy is limited but because the sinner has cut himself off from the very Spirit through whom forgiveness comes.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "holy-ghost-spirit-sin-against-the"},
        "key_refs": ["Matthew 12:31", "Mark 3:29", "Luke 12:10", "Hebrews 6:4", "Hebrews 10:26"]
    },
    "revelation-of-john": {
        "id": "revelation-of-john",
        "term": "Revelation of John",
        "category": "concepts",
        "intro": "<p>The Book of Revelation (Greek <em>Apokalupsis Ioannou</em>) is the NT's one work of sustained apocalyptic literature, addressed to seven churches of Asia Minor and presenting visions of cosmic conflict, divine judgment, and the ultimate triumph of God and the Lamb. Its author identifies himself as John (Rev. 1:1, 4, 9; 22:8), traditionally identified as the Apostle John, though some scholars prefer a different John (\"John the Elder\"). The date is debated: the evidence of Domitian's persecution suggests 81–96 A.D. (early date: 64–68 A.D., Nero's reign). The book's genre is complex — it is simultaneously an apocalypse (revelatory heavenly visions), a prophecy (\"words of this prophecy,\" Rev. 1:3; 22:7), and a circular letter to specific congregations. Its theological center is the throne-room vision of God and the Lamb (Rev. 4–5), which grounds the confidence that God's purposes will prevail despite earthly persecution. The four major interpretive approaches are: preterist (the visions describe first-century events), historicist (the visions trace the church's history from the 1st century to Christ's return), futurist (the visions primarily describe future end-time events), and idealist (the visions are timeless symbols of the cosmic struggle between good and evil). The book's central message is stated at its end: \"He who testifies to these things says, 'Surely I am coming soon.' Amen. Come, Lord Jesus!\" (Rev. 22:20).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "revelation-of-john"},
        "key_refs": ["Revelation 1:1", "Revelation 1:3", "Revelation 4:1", "Revelation 19:6", "Revelation 22:20"]
    },
    "heavens": {
        "id": "heavens",
        "term": "Heavens",
        "category": "concepts",
        "intro": "<p>\"The heavens\" (Hebrew <em>shamayim</em>; Greek <em>ouranos</em>) in Scripture encompasses the visible sky and beyond it the dwelling place of God — a term that bridges physical cosmology and theological reality. The OT uses <em>shamayim</em> in multiple senses: the atmospheric heavens (where clouds and rain are, Gen. 1:8; Deut. 11:11), the stellar heavens (where sun, moon, and stars are set, Gen. 1:14–17; Ps. 8:3), and the dwelling place of God, who \"looks down from heaven\" (Ps. 14:2; 33:13; 102:19). Paul's reference to \"the third heaven\" (2 Cor. 12:2) reflects a common Jewish cosmological scheme of multiple heavens, ascending to God's immediate presence. Jewish and rabbinic tradition variously posited three or seven heavens. Ephesians locates the believer's position and Christ's exaltation \"in the heavenly places\" (<em>en tois epouraniois</em>, Eph. 1:3, 20; 2:6; 3:10; 6:12), a realm of spiritual reality both present and transcendent. The OT affirmation that \"the heavens are the LORD's heavens, but the earth he has given to the children of man\" (Ps. 115:16) distinguishes divine from human realms while maintaining that God is the creator of both. The \"new heavens and new earth\" of Isaiah 65:17 and Revelation 21:1 indicate that even the present heavens are subject to eschatological renewal and replacement.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"isbe": "heavens"},
        "key_refs": ["Genesis 1:8", "Psalm 8:3", "2 Corinthians 12:2", "Ephesians 1:3", "Revelation 21:1"]
    },
}


def main():
    written = 0
    skipped = 0
    first_term = list(ARTICLES.values())[0]['term']
    last_term = list(ARTICLES.values())[-1]['term']
    for slug, data in ARTICLES.items():
        if merge_article(slug, data):
            written += 1
        else:
            skipped += 1
    print(f'BP gap-isbe-theology: {first_term} -> {last_term}: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
