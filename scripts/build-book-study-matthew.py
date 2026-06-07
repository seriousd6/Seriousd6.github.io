"""
Book Study Data — Matthew
book_id: matthew
lang: greek

Run: python3 scripts/build-book-study-matthew.py

Notes:
- Key vocabulary selected from Matthew author group peaks in author-freq-greek.json
- ἐκκλησία included despite not peaking in Matthew author group because Matthew is the
  only gospel to record Jesus using the word (16:18; 18:17) — theologically non-negotiable
- τότε included as Matthew's single most statistically distinctive narrative word (~90x)
- πληρόω included for the formula-quotation structure that defines Matthew's hermeneutic
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
    "bookId": "matthew",

    "key_vocabulary": [
        {
            "code": "G932",
            "lemma": "βασιλεία",
            "translit": "basileía",
            "gloss": "kingdom",
            "significance": (
                "Matthew uses 'kingdom of heaven' (βασιλεία τῶν οὐρανῶν) 32 times — a "
                "distinctively Jewish circumlocution for 'kingdom of God' that respects the "
                "Jewish reverence for the divine name. This is not a different concept from "
                "Mark and Luke's 'kingdom of God' but a culturally targeted expression for "
                "Matthew's Jewish-Christian audience. The kingdom is simultaneously present "
                "(4:17 — 'has drawn near') and future (6:10 — 'your kingdom come'), ethical "
                "(5:20 — requires surpassing righteousness) and gift (5:3 — 'theirs is the "
                "kingdom of heaven'). Matthew's parables of the kingdom (ch. 13) explore this "
                "paradox more systematically than any other gospel."
            )
        },
        {
            "code": "G5207",
            "lemma": "υἱός",
            "translit": "huiós",
            "gloss": "son",
            "significance": (
                "Matthew opens with the double title 'Son of David, Son of Abraham' (1:1) and "
                "ends with Jesus commissioning in the name of 'the Father and of the Son' "
                "(28:19). The word accumulates Christological freight through the genealogy "
                "(legal Davidic lineage), the baptism (divine voice: 'This is my beloved Son'), "
                "the temptation (Satan's challenge 'if you are the Son of God'), and Peter's "
                "confession (16:16). By the end, 'Son' in Matthew carries the full weight of "
                "divine identity — Immanuel, God-with-us — not merely messianic office."
            )
        },
        {
            "code": "G4137",
            "lemma": "πληρόω",
            "translit": "plēróō",
            "gloss": "accomplish",
            "significance": (
                "Matthew's fulfillment formula ('this happened to fulfill what was spoken by "
                "the prophet...') appears ten times — more than any other NT book. But πληρόω "
                "means more than mechanical prediction-matching: it denotes bringing something "
                "to its intended completeness, filling up what was partial or provisional. The "
                "same verb appears at 5:17 — Jesus came not to abolish the Law and Prophets but "
                "to 'fulfill' them. Matthew's hermeneutic is not proof-texting but an argument "
                "that the OT's entire trajectory — its promises, patterns, and people — reaches "
                "its destined end in Jesus."
            )
        },
        {
            "code": "G3101",
            "lemma": "μαθητής",
            "translit": "mathētḗs",
            "gloss": "disciple",
            "significance": (
                "The word means 'learner' — one who follows a teacher in a sustained pedagogical "
                "relationship. Matthew uses it 73 times (more than any other gospel), and the "
                "Great Commission climaxes with the verb form: 'disciple all nations' "
                "(μαθητεύσατε, 28:19). In Matthew, discipleship is not merely following Jesus "
                "geographically but entering a school of thought and practice, learning to "
                "'observe all that I have commanded you.' The five discourses are Jesus' "
                "curriculum; Matthew's church is the community of ongoing learners."
            )
        },
        {
            "code": "G5119",
            "lemma": "τότε",
            "translit": "tóte",
            "gloss": "that time",
            "significance": (
                "Matthew uses τότε ('then / at that time') approximately 90 times — compared to "
                "6 in Mark and 15 in Luke. In Greek, τότε marks temporal and causal sequence "
                "more precisely than the simple connective καί ('and'). Matthew's high frequency "
                "creates a sense of destined progression: event leads to event, and prophecy to "
                "fulfillment. When Matthew writes τότε ἐπληρώθη ('then was fulfilled'), the "
                "particle bears narratological weight — this is the moment toward which the "
                "story was always moving."
            )
        },
        {
            "code": "G3772",
            "lemma": "οὐρανός",
            "translit": "ouranós",
            "gloss": "heaven",
            "significance": (
                "Matthew's preferred phrase 'kingdom of heaven' uses the plural οὐρανοί "
                "(heavens), following Jewish idiom that spoke of the upper realms in the plural. "
                "The word appears across different registers: the physical sky (birds of the air, "
                "6:26), the dwelling of the Father ('our Father in heaven,' 6:9), and the seat "
                "of Jesus' cosmic authority (28:18 — 'all authority in heaven and on earth'). "
                "The range from created sky to divine throne makes 'heaven' in Matthew not a "
                "place souls go but the realm of God's sovereign rule that has invaded earth in "
                "the person of Jesus."
            )
        },
        {
            "code": "G1343",
            "lemma": "δικαιοσύνη",
            "translit": "dikaiosýnē",
            "gloss": "righteousness",
            "significance": (
                "Matthew uses this word 7 times — compared to zero in Mark and once in Luke — "
                "making it a distinctively Matthean theological category. In the Sermon on the "
                "Mount it appears in key statements: disciples are to hunger and thirst for "
                "righteousness (5:6), their righteousness must exceed the Pharisees' (5:20), "
                "and they are to seek God's kingdom and righteousness first (6:33). The word "
                "carries a Hebrew semantic range inherited from צְדָקָה: it encompasses both "
                "moral uprightness and the covenant faithfulness God shows his people — a "
                "double meaning that English 'righteousness' often flattens into a purely "
                "ethical category."
            )
        },
        {
            "code": "G4396",
            "lemma": "προφήτης",
            "translit": "prophḗtēs",
            "gloss": "prophet",
            "significance": (
                "The prophet appears as both the source of Matthew's fulfillment quotations and "
                "a category Jesus redefines. Jesus identifies John the Baptist as the Elijah-"
                "prophet (17:12-13), calls himself a prophet rejected in his hometown (13:57), "
                "and warns extensively against false prophets (7:15; 24:11, 24). The double "
                "edge is distinctive to Matthew: the genuine prophetic tradition of Israel finds "
                "its culmination and end in Jesus, while false prophecy — even miraculous-"
                "seeming — is one of the gravest dangers the community faces. Matthew 7:22-23 "
                "('did we not prophesy in your name?') is the sobering counterpart to the "
                "fulfillment formula."
            )
        },
        {
            "code": "G1577",
            "lemma": "ἐκκλησία",
            "translit": "ekklēsía",
            "gloss": "assembly",
            "significance": (
                "Matthew is the only gospel that records Jesus using this word — twice: at 16:18 "
                "('I will build my church') and 18:17 (community discipline). The term means "
                "'called-out assembly' and carries Jewish overtones of the qahal (the gathered "
                "covenant community) alongside Greco-Roman civic meaning (a public deliberative "
                "body). Jesus' use anticipates the post-resurrection community that will execute "
                "the Great Commission. Matthew's ecclesiology — the church as a disciplined, "
                "forgiving, authoritative community carrying Jesus' teaching into all nations — "
                "is embedded in Jesus' own speech, not a Pauline addition."
            )
        },
        {
            "code": "G5330",
            "lemma": "Φαρισαῖος",
            "translit": "Pharisaîos",
            "gloss": "Pharisee",
            "significance": (
                "The Pharisees appear approximately 29 times in Matthew and are the book's "
                "primary antagonist group. Matthew's portrait escalates systematically: early "
                "suspicion (9:34), Sabbath controversy (12:2), murder plot (12:14), testing "
                "(16:1), and culminating in the seven woes of ch. 23 — the most extended "
                "denunciation in any gospel. The woes are not merely polemical; they function "
                "as a mirror for the community: the failures of external religion (performing "
                "to be seen, 23:5) are precisely the temptations Matthew's disciples face. "
                "The Pharisees illustrate what discipleship is not."
            )
        },
        {
            "code": "G4334",
            "lemma": "προσέρχομαι",
            "translit": "prosérchomai",
            "gloss": "come thereunto",
            "significance": (
                "Matthew uses this compound verb (literally, 'to come toward') approximately "
                "52 times to structure approach to Jesus — by disciples, crowds, Pharisees, "
                "petitioners, the tempter, and angels. The word implies deliberate, respectful "
                "movement toward a person of authority, often in the posture of petition or "
                "homage. Matthew's characteristic scene — someone προσέρχεται to Jesus, a "
                "question or request follows, Jesus teaches or acts — is his narrative grammar "
                "for Jesus as the one toward whom all movement is oriented. Noticing who "
                "approaches and why reveals Matthew's social and theological map."
            )
        },
        {
            "code": "G3551",
            "lemma": "νόμος",
            "translit": "nómos",
            "gloss": "law",
            "significance": (
                "The Torah stands as the unavoidable question behind Matthew's entire narrative. "
                "Jesus' programmatic claim at 5:17-18 — that he came to 'fulfill' the Law and "
                "that not one iota will pass until all is accomplished — sets the agenda for the "
                "Sermon on the Mount's antitheses. Matthew 22:37-40 identifies love of God and "
                "neighbor as the two commands on which 'the whole Law and the Prophets hang.' "
                "This is neither abolition nor simple continuity: Matthew's Jesus is the "
                "authoritative interpreter who brings the Torah to its inner intention, the "
                "only lawgiver whose understanding of the law is definitive."
            )
        },
        {
            "code": "G5547",
            "lemma": "Χριστός",
            "translit": "Christós",
            "gloss": "Christ",
            "significance": (
                "Matthew opens with 'Jesus Christ' (1:1) — a title, not a name — establishing "
                "immediately that this figure is the anointed one of Jewish expectation. The "
                "title carries the full weight of Davidic messiahship: king, deliverer, temple-"
                "builder. Peter's confession at 16:16 ('You are the Christ, the Son of the "
                "living God') is the book's theological pivot, after which Jesus begins "
                "redefining messiahship through suffering and resurrection. Matthew's passion "
                "narrative is his argument that the cross does not falsify the messianic claim "
                "but reveals its true meaning."
            )
        },
        {
            "code": "G1342",
            "lemma": "δίκαιος",
            "translit": "díkaios",
            "gloss": "righteous",
            "significance": (
                "Matthew applies this adjective to a surprising range of figures: Joseph is "
                "'righteous' (1:19) because he responds to Mary's situation with compassion "
                "rather than legal severity; the righteous will shine in the kingdom (13:43); "
                "the blood of 'righteous Abel' to 'righteous Zechariah' cries out (23:35); "
                "those who fed the hungry are called 'righteous' at the judgment (25:37). In "
                "Matthew, righteousness is not merely a forensic verdict but the character of "
                "those who do the Father's will — it describes a way of life, not just a "
                "legal standing, and is accessible to anyone who acts with justice and mercy."
            )
        },
        {
            "code": "G1453",
            "lemma": "ἐγείρω",
            "translit": "egeírō",
            "gloss": "awake",
            "significance": (
                "Matthew uses this verb in both healing and resurrection contexts — Jesus "
                "raises Jairus's daughter (9:25), restores the paralytic with 'arise' (9:6), "
                "and is himself announced as raised (ἠγέρθη, 28:6-7). The passive voice of "
                "the resurrection announcements is theologically deliberate: Jesus was raised "
                "by God, not by his own power — the same divine act that healed and restored "
                "in the miracles now vindicates the Son definitively. Matthew's use of the "
                "same verb across both domains suggests the healings are advance signs of the "
                "eschatological resurrection, not isolated wonders."
            )
        },
    ],

    "language_notes": (
        "<p>Matthew's most architecturally significant linguistic feature is the formula "
        "quotation. Ten times the narrative pauses for the phrase <em>τοῦτο δὲ ὅλον γέγονεν "
        "ἵνα πληρωθῇ τὸ ῥηθὲν ὑπὸ τοῦ προφήτου</em> — 'all this happened that what was "
        "spoken through the prophet might be fulfilled.' The verb <em>γέγονεν</em> is a "
        "perfect tense, marking the event as accomplished with present consequence; "
        "<em>ἵνα πληρωθῇ</em> uses a subjunctive of purpose, signaling design rather than "
        "accident. This is not proof-texting but a sophisticated hermeneutic embedded in "
        "Greek grammar: Matthew reads the OT as a story whose intended ending has arrived "
        "in the person of Jesus.</p>"
        "<p>The particle <strong>τότε</strong> ('then') is Matthew's single most statistically "
        "distinctive narrative word, appearing approximately 90 times compared to 6 in Mark "
        "and 15 in Luke. In Greek prose, <em>τότε</em> marks temporal sequence with a "
        "stronger sense of causal or narrative consequence than the simple connective "
        "<em>καί</em> ('and'). Matthew's high frequency of <em>τότε</em> creates a sense of "
        "inevitable progression — event leads to event, opposition to judgment, prophecy to "
        "fulfillment. When Matthew writes <em>τότε ἐπληρώθη</em> ('then was fulfilled'), the "
        "particle bears narratological weight: this is the destined moment.</p>"
        "<p>The five discourses each end with a formulaic closure: <em>καὶ ἐγένετο ὅτε "
        "ἐτέλεσεν ὁ Ἰησοῦς</em> — 'and when Jesus had finished these words' (7:28; 11:1; "
        "13:53; 19:1; 26:1). The verb <em>τελέω</em> (to complete, to bring to an end) is "
        "the same root as <em>τετέλεσται</em> in John 19:30 ('it is finished'). Matthew's "
        "closure formula is a structural signal that each discourse is a completed literary "
        "unit — not a miscellany of sayings — with its own internal coherence and intended "
        "audience. The student should read each discourse as a whole before mining it for "
        "individual verses.</p>"
        "<p>The antitheses of the Sermon on the Mount are a grammatical argument for "
        "Jesus' authority. <em>Ἠκούσατε ὅτι ἐρρέθη</em> — 'you have heard that it was "
        "said' — uses the passive <em>ἐρρέθη</em>, a divine passive implying God as speaker. "
        "Jesus then counters with <em>ἐγὼ δὲ λέγω ὑμῖν</em> — 'but I say to you' — an "
        "emphatic first-person present active. This is not the grammar of a prophet citing "
        "God's words but of a lawgiver speaking in his own right. The grammatical shift from "
        "passive report to first-person declaration is Matthew's most concentrated statement "
        "of Christology: Jesus does not cite precedent — he is the authority from whom "
        "precedent flows.</p>"
    ),

    "reception": (
        "<p><strong>Patristic:</strong> Matthew was the most quoted gospel in the early "
        "church — cited by Ignatius of Antioch (c. AD 110), Justin Martyr, Irenaeus, and "
        "Tertullian far more frequently than Mark or Luke. Its comprehensive teaching "
        "discourses made it the church's catechetical gospel. The <em>Didache</em> "
        "(late 1st–early 2nd c.) reflects Matthew's version of the Lord's Prayer (6:9-13) "
        "and the Great Commission, indicating Matthew's early liturgical primacy. Origen "
        "wrote one of the earliest sustained gospel commentaries on Matthew, and Chrysostom's "
        "90 homilies on Matthew shaped Eastern preaching for centuries.</p>"
        "<p><strong>Medieval:</strong> Medieval exegesis read Matthew through the fourfold "
        "sense — the genealogy was extensively allegorized, the Sermon on the Mount became "
        "the primary basis for monastic ethics, and the parables of the kingdom were read "
        "anagogically as pictures of heaven. Thomas Aquinas drew on Matthew's law-fulfillment "
        "framework in the <em>Summa Theologiae</em> to articulate the relationship between "
        "Old Law and New Law, arguing that the Sermon on the Mount perfects rather than "
        "abolishes the Mosaic commandments.</p>"
        "<p><strong>Reformation:</strong> Luther read the Sermon on the Mount as the "
        "impossible righteousness that drives one to Christ for grace — not a moral program "
        "for self-improvement. Calvin's <em>Harmony of the Gospels</em> interweaved Matthew, "
        "Mark, and Luke, treating Matthew's fulfillment quotations as the key to reading the "
        "OT as Christian Scripture. Matthew 16:18 became a Reformation flashpoint: Luther "
        "accepted Peter as the rock of the church's foundation; Calvin argued the 'rock' was "
        "Peter's confession of faith, not Peter's person — a distinction with obvious "
        "implications for ecclesial authority.</p>"
        "<p><strong>Modern debates:</strong> Twentieth-century scholarship was dominated by "
        "redaction criticism — identifying what Matthew changed from Mark and what those "
        "changes reveal about his community. W.D. Davies and Dale Allison's three-volume ICC "
        "commentary (1988–1997) remains the standard critical reference. Two debates define "
        "current scholarship: first, whether Matthew represents a Jewish-Christian community "
        "in painful tension with emerging rabbinic Judaism after AD 70, or a community that "
        "has already separated; second, whether Matthew 23's extended denunciation of the "
        "Pharisees reflects an in-group dispute (intra-Jewish polemic) or out-group rhetoric, "
        "with significant implications for Jewish-Christian dialogue.</p>"
    ),

    "reading_guide": (
        "<p>The single most important thing to grasp before reading Matthew is the "
        "<strong>five-discourse structure</strong>. The book is not a continuous biography "
        "but five blocks of teaching — Sermon on the Mount (chs. 5–7), Mission Discourse "
        "(ch. 10), Parables of the Kingdom (ch. 13), Community Discourse (ch. 18), and "
        "Eschatological Discourse (chs. 24–25) — each with a distinct audience and purpose, "
        "embedded in a narrative frame. Each discourse ends with a formulaic closure. Reading "
        "each discourse as a literary unit before extracting individual verses prevents the "
        "common mistake of applying a verse to a context it was never meant to address.</p>"
        "<p>Watch for Matthew's fulfillment formula quotations. Each time the narrative pauses "
        "for 'this happened that it might be fulfilled...', follow the OT reference to its "
        "source and read it in context. The fulfillment is almost never a simple one-to-one "
        "prediction: Matthew reads Israel's history as recapitulated and transcended in Jesus. "
        "The richest study practice is to ask what the OT passage meant originally, then what "
        "Matthew sees as fulfilled — the gap between the two is where Matthew's hermeneutic "
        "is most visible.</p>"
        "<p>A common misreading of the Sermon on the Mount is to treat it as a higher law "
        "replacing the Mosaic — a perfectionist ethics no one can keep, intended to drive us "
        "to despair. Matthew 5:17 rules this out: Jesus came to fulfill, not abolish. The "
        "Sermon is his authoritative exposition of what Torah always intended when read from "
        "within. A second common misreading: assuming Matthew 16:18 settles the question of "
        "Petrine primacy. The verse is genuinely disputed; read it alongside ch. 18, where "
        "the 'keys of binding and loosing' are extended to the whole community (18:18), to "
        "see that Matthew's ecclesiology distributes authority more broadly than a single "
        "verse suggests. If entering non-sequentially, start with chs. 5–7 for kingdom ethics "
        "or ch. 13 for Jesus' most sustained teaching on what the kingdom actually is.</p>"
    ),
}

# ── main ─────────────────────────────────────────────────────────────────────

def main():
    existing = load_book_study('matthew')
    merged   = merge_book_study(existing, BOOK_STUDY)
    save_book_study('matthew', merged)

main()
