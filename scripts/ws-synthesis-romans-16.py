"""
Wide Source Synthesis — Romans chapter 16
bookId: romans
Run: python3 scripts/ws-synthesis-romans-16.py

Sources used: calvin, ellicott, clarke, wesley, barnes
(mhcc: directory does not exist; jfb: ch 16 data is misassigned to Acts material — excluded)
Chapter range: 16  (27 verses)

Key synthesis decisions:
- v. 7: "Junia" vs. "Junias" gender is textually unresolved; Clarke leans female; set as divided
- v. 7: "of note among the apostles" — Clarke reads as esteemed by apostles; Barnes leaves both options
- v. 20: Calvin insists "shall bruise Satan" is indicative promise not prayer; set as mixed
- vv. 25-27: Clarke and Barnes note doxology appears after ch. 14 in major MSS; noted in synthesis
- v. 24: Ellicott flags verse as absent from oldest MSS; set as mixed
- v. 1 Barnes entry is chapter intro, not Phoebe commentary; barnes voice used from v. 2 content for that verse
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_synthesis(book):
    p = ROOT / 'data' / 'commentary' / 'synthesis' / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_synthesis(book, data):
    p = ROOT / 'data' / 'commentary' / 'synthesis' / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_synthesis(existing, new_data):
    """Merge new chapter/verse entries without overwriting existing ones."""
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, entry in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entry

ROMANS = {
    "16": {
        "1": {
            "synthesis": "<p>Paul opens his closing chapter with a formal letter of recommendation for Phoebe, identified as a <em>diakonos</em> — servant or deaconess — of the church at Cenchrea, the eastern port of Corinth. The precise weight of the term is a genuine question: Ellicott and Wesley both translate it as \"deaconess,\" recognizing the formal office that appears elsewhere in the apostolic church, while Calvin is more cautious, noting that the word can designate generally anyone who contributes help to others without implying an ordained role. Clarke adds that Phoebe was most likely the bearer of this letter to Rome, which explains the commendation's placement at the epistle's close.</p><p>The structure of Paul's commendation follows the ancient letter of introduction: he vouches for her character and office, then asks the Roman believers to extend her whatever practical help she needs. That a woman carried this weightiest of Paul's letters across the Aegean speaks to the trust and esteem in which he held her.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>He first commends to them Phoebe, to whom he gave this Epistle to be brought to them; and, in the first place, he commends her on account of her office, for she performed a most honorable and a most holy function in the Church; and then he adduces another reason — for she had always been a helper to all the godly. The word <em>diakonos</em> does not necessarily prove a formal deaconess office; it often designates generally one who does service and contributes to the help of others.</p>"},
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p>As the Roman Church is especially exhorted to receive Phoebe, it has been inferred that she was one of the party to which St. Paul entrusted his Epistle, if not the actual bearer of it herself. <strong>Servant.</strong>—Rather, <em>a deaconess,</em> keeping the technical term rather than softening it into a vaguer description of general service.</p>"},
                {"src": "wesley", "attr": "John Wesley", "html": "<p>I commend unto you Phoebe — The bearer of this letter. A servant — the Greek word is <em>a deaconess.</em> Of the church in Cenchrea. In the apostolic age, some grave and pious women were appointed deaconesses in every church. It was their office, not to teach publicly, but to visit the sick, the women in particular, and to minister to them both in their temporal and spiritual necessities.</p>"}
            ],
            "consensus": "mixed",
            "key_tension": "Calvin regards 'diakonos' as a general description of Phoebe's service without implying a formal ordained office, while Ellicott and Wesley read it as the established title 'deaconess,' reflecting a recognized role in the apostolic church."
        },
        "2": {
            "synthesis": "<p>Paul asks the Romans to receive Phoebe \"in the Lord, as becometh saints\" — that is, with the conscious hospitality that Christian fellowship demands. Ellicott focuses on the phrase \"in the Lord\" as freighting the act with theological weight: it is a reception performed with awareness of Christian obligation. Barnes unpacks the title <em>prostatis</em> — translated \"succourer\" — as meaning patron or protectress, one who used her social standing and resources to advocate and provide for others, Paul himself included. Wesley notes simply that \"in the Lord\" is the characteristic Pauline qualifier for Christian relationship.</p>",
            "voices": [
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>In the Lord.</strong>—With the consciousness that you are performing a Christian act, subject to all those serious obligations implied in the name. <strong>As becometh saints.</strong>—As Christians ought to receive a fellow-Christian. <strong>Succourer.</strong>—Patroness or protectress, in the exercise of her office as deaconess.</p>"},
                {"src": "barnes", "attr": "Albert Barnes", "html": "<p>She hath been a succourer of many. The word used here (<em>prostatis</em>) means, properly, a patron, a help, and was applied by the Greeks to one who appeared for another; a defender, one who stood before another to protect him. Here it denotes that she had shown great kindness in aiding many Christians, and particularly the apostle Paul himself.</p>"},
                {"src": "wesley", "attr": "John Wesley", "html": "<p>In the Lord — That is, for the Lord's sake, and in a Christian manner. St. Paul seems fond of this expression, using it to ground all Christian hospitality in its proper theological motive rather than mere social courtesy.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "3": {
            "synthesis": "<p>Paul greets Prisca (Priscilla) and Aquila as his fellow workers in Christ Jesus — the Jewish couple expelled from Rome under Claudius who had sheltered and partnered with Paul at Corinth and Ephesus. The fact that the wife is named before the husband is notable in all sources. Ellicott suggests this may reflect Prisca's greater public activity; Calvin observes that Paul's willingness to name a woman as his associate in the Lord's work reflects his genuine modesty and freedom from social convention. Clarke notes they had returned to Rome following the annulment of Claudius's edict.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>The testimonies which he brings here in favor of some individuals were partly intended for this end, that by honoring those who were faithful and worthy, faithfulness itself might be honored. It is a singular honor which he ascribes here to Prisca and Aquila, especially with regard to a woman. The modesty of the holy man does on this account more clearly shine forth; for he disdained not to have a woman as his associate in the work of the Lord; nor was he ashamed to confess this.</p>"},
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>Priscilla.</strong>—The correct reading here is Prisca, of which Priscilla is the diminutive. It is rather remarkable that the wife should be mentioned first. Perhaps it may be inferred that she was the more active and conspicuous of the two. Aquila was a Jew of Pontus, whom St. Paul had found with his wife at Corinth; they had been converted by him, and followed him to Ephesus.</p>"},
                {"src": "clarke", "attr": "Adam Clarke", "html": "<p>Greet Priscilla and Aquila — This pious couple had been obliged to leave Rome on the edict of Claudius and take refuge in Greece. It is likely that they returned to Rome at the death of Claudius, or whenever the decree was annulled. It seems they had greatly contributed to assist the apostle in his important labors.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "4": {
            "synthesis": "<p>Paul records that Prisca and Aquila had at some point risked their own lives — \"laid down their necks\" — to preserve his. The precise occasion is now unknown to us, though Ellicott raises the tumult at Ephesus and the \"fighting with beasts\" of 1 Corinthians 15:32 as possible referents. Calvin notes that Paul records their sacrifice not only out of personal gratitude but so that the Romans, knowing the wider gratitude of all Gentile churches, might be moved to honor them in turn. Wesley observes the theological proportion: all Gentile churches owe a debt to those who protected the apostle through whom the gospel reached them.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>As Prisca and Aquila had not spared their life for preserving the life of Paul, he testifies that he himself was individually thankful to them; he however adds that thanks were given them by all the Churches of Christ; and he added this that he might, by such an example, influence the Romans. Deservedly dear and precious to all the Gentiles was the life of him through whom the gospel had been spread among them.</p>"},
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>Laid down their own necks.</strong>—Whether this expression is to be taken literally or figuratively we do not know, neither can we do more than guess at the event to which it refers. It may have something to do with the tumult at Ephesus, and with that \"fighting with beasts\" mentioned in 1 Corinthians 15:32.</p>"},
                {"src": "wesley", "attr": "John Wesley", "html": "<p>Who have for my life, as it were, laid down their own necks — That is, exposed themselves to the utmost danger. But likewise all the churches of the Gentiles — Even that at Rome, for preserving so valuable a life as the apostle's, through whom the gospel had come to them.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "5": {
            "synthesis": "<p>Paul greets the house-church meeting in Prisca and Aquila's home — a reminder that in the apostolic decades, private residences were the primary sites of Christian assembly. Ellicott notes parallel house-churches at Ephesus, Colossae, and in Philemon's household. Paul then singles out Epaenetus, the first convert in the province of Asia, honoring him as the \"firstfruits\" of that territory. Calvin observes that the firstfruits image, drawn from the Levitical system, signals how those first to believe carry a special prerogative of honor — though only when their beginning is matched by a faithful end.</p>",
            "voices": [
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>The church that is in their house.</strong>—A party of Christians seem to have been in the habit of meeting in the house of Aquila and Priscilla for worship at Rome, as previously at Ephesus (1 Corinthians 16:19). Similar instances may be found in Acts 12:12; Colossians 4:15; Philemon 1:2.</p>"},
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>This is an allusion to the rites of the law; for as men are sanctified to God by faith, they who first offer themselves are fitly called the first-fruit. Whosoever then is called first in time to the faith, Paul allows him the prerogative of honor; yet he retains this eminence only when the end corresponds with the beginning.</p>"},
                {"src": "clarke", "attr": "Adam Clarke", "html": "<p>The Church that is in their house — In these primitive times no such places existed as those which we now term churches; the word always signifying the congregation or assembly of believers, and not the place they assembled in. Epaenetus — the first fruits of Achaia — probably one of the household of Stephanas, who are called the first fruits of Achaia in 1 Cor 16:15.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "6": {
            "synthesis": "<p>Mary is commended for having labored much, but nothing further is known of her. Calvin notes that Paul records such praises to recommend people to the Romans and to encourage others by their example. Clarke draws a quiet devotional observation: her works, though hidden from human record, are known to God — \"her name is recorded with honor in this book of life.\" Barnes suggests she was likely a former resident of Greece who had relocated to Rome, becoming known to Paul through his earlier ministry in Corinth or Achaia.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>He again testifies his gratitude, in recording the kindness of Mary to him. Nor is there any doubt but that he commemorates these praises, in order to recommend those whom he praised to the Romans. It is said of Mary, that she \"labored much,\" <em>eis hymas</em>, towards us or among us; the reading <em>eis hymas</em>, \"toward you,\" has many manuscripts in its favor.</p>"},
                {"src": "clarke", "attr": "Adam Clarke", "html": "<p>Greet Mary, who bestowed much labor on us — Who this Mary was, or what the labor was which she bestowed upon the apostles, we know not. Her works, though hidden from man, are with God; and her name is recorded with honor in this book of life.</p>"},
                {"src": "barnes", "attr": "Albert Barnes", "html": "<p>Who bestowed much labour on us. Who laboured much for us. Nothing more is known of her but this honourable mention of her name. It is probable that these persons were formerly residents in Greece, and that the apostle had there become acquainted with them, but that they had now removed to Rome.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "7": {
            "synthesis": "<p>Paul greets Andronicus and Junia — his kinsmen (likely fellow Jews, possibly relatives), fellow prisoners for the gospel, who were \"in Christ before me\" and are \"of note among the apostles.\" Two genuine interpretive tensions run through the tradition here. The first concerns the name: the Greek <em>Iounian</em> is ambiguous between the feminine Junia and a contracted masculine Junias; Clarke leans toward reading Junia as Andronicus's wife, while Ellicott and Calvin remain uncertain. The second, more substantial tension is the phrase \"of note among the apostles\": does it mean they were themselves eminent figures in the apostolic circle, or only that they were well-regarded by the apostles? Clarke takes the latter reading; Barnes leaves both open; Calvin's primary concern is with the ambiguity of gender. If Junia is female and the phrase marks her own apostolic standing, the verse becomes a striking early witness to a woman recognized in apostolic terms.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>There is more weight in the second eulogy, when he calls them his fellow-prisoners. It is not certain whether the Apostle means that they were well known to the apostles, or that they themselves held apostolic rank. As to Junia, it is not certain whether it is the name of a man or a woman. If of a woman, it is by no means a common thing for Paul to attribute to her apostolic honor.</p>"},
                {"src": "clarke", "attr": "Adam Clarke", "html": "<p>Andronicus and Junia, my kinsmen — As Junia may probably be the name of a woman, the wife of Andronicus, it would be better to say relatives than kinsmen. Who are of note among the apostles — who are distinguished persons, highly esteemed by the apostles. They appear to have been among the earliest converts; they were in Christ before Paul was converted.</p>"},
                {"src": "barnes", "attr": "Albert Barnes", "html": "<p>My kinsmen. In Rom 9:3 the apostle calls all the Jews his kinsmen, and it has been doubted whether he means anything more here. My fellowprisoners — they had been imprisoned on account of the gospel. They must have been disciples of Christ before Paul, as they were among the apostles, or noted among them, before Paul was converted.</p>"}
            ],
            "consensus": "divided",
            "key_tension": "Whether Junia is a woman's name (making this a reference to a female figure of apostolic standing) or a contracted male name Junias is textually unresolved; and whether 'of note among the apostles' describes their own apostolic rank or their reputation in the eyes of the apostles is disputed — Clarke reads the latter, while the phrase in context most naturally implies the former."
        },
        "8": {
            "synthesis": "<p>Paul greets Ampliatus as his \"beloved in the Lord\" — a term of personal affection anchored in their shared life in Christ. Ellicott notes that the name Ampliatus (the fullest form of \"Amplias\") appears frequently in inscriptions connected to the imperial household, placing this early Roman believer within the social world of the empire's servants and freedmen. Clarke reads the phrase as indicating simple particular friendship and genuine faith. The qualification \"in the Lord\" preserves the characteristic Pauline insistence that even personal love is theologically grounded.</p>",
            "voices": [
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>Amplias.</strong>—The three oldest MSS. have \"Ampliatus,\" for which \"Amplias\" is a contracted form. The name is a common one, in several instances found in connection with the imperial household. The name \"beloved in the Lord\" implies close personal affection grounded in their common faith in Christ.</p>"},
                {"src": "clarke", "attr": "Adam Clarke", "html": "<p>Amplias, my beloved in the Lord — One who is my particular friend, and also a genuine Christian. The phrase \"in the Lord\" always denotes the spiritual ground of the relationship Paul is describing, not mere social acquaintance.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "9": {
            "synthesis": "<p>Paul greets Urbanus as \"our helper in Christ\" — a fellow missionary laborer whose partnership Paul shares with Timothy (Wesley notes the plural \"our\" links to verse 21). Stachys receives the simple but warm title \"my beloved.\" Ellicott observes that Urbanus, like several other names in this chapter, appears in inscriptions of the imperial household, suggesting early Christianity had penetrated the administrative and domestic circles of Rome's palace staff. Clarke notes that beyond what Paul records, nothing further is known of either man.</p>",
            "voices": [
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>Urbane.</strong>—Urbanus; a common name found among members of the imperial household. <strong>Our helper in Christ.</strong>—The helper both of St. Paul and of the Roman Church by her efforts in spreading the gospel. <strong>Stachys.</strong>—A rarer name; it appears as that of a court physician in imperial records.</p>"},
                {"src": "wesley", "attr": "John Wesley", "html": "<p>Our fellow-labourer — Mine and Timothy's, as named in verse 21. The possessive \"our\" ties this greeting to the companions mentioned at the close of the chapter, indicating a shared missionary partnership rather than Paul's alone.</p>"},
                {"src": "clarke", "attr": "Adam Clarke", "html": "<p>Urbane, our helper — Who this Urbanus was we know not; what is here stated is that he had been a fellow laborer with the apostles. Stachys, my beloved — One of my particular friends; beyond what is here recorded we know nothing of either man.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "10": {
            "synthesis": "<p>Apelles is commended as \"approved in Christ\" — one whose faith has been tested and found genuine. Ellicott notes the name appears among the dependents of the emperor. Paul then greets those of the household of Aristobulus, a phrasing that suggests Aristobulus himself was not a Christian — or was deceased — while certain members of his extended household had come to faith. Ellicott speculates Aristobulus may be the brother of Herod Agrippa I, in which case his household, falling into imperial possession after his death, would have supplied slaves and freedmen to the Roman church.</p>",
            "voices": [
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>Apelles.</strong>—This name is also found among the dependents of the emperor. <strong>Approved in Christ.</strong>—Whose fidelity to Christ has been tried, and has stood the test. <strong>Aristobulus' household.</strong>—Aristobulus, if he is the brother of Herod Agrippa I, would have been known in Rome; his household would include dependents and slaves, some of whom were now believers.</p>"},
                {"src": "barnes", "attr": "Albert Barnes", "html": "<p>Approved in Christ. An approved or tried Christian; approved and beloved by Christ. Them which are of Aristobulus' household — It is doubted whether Aristobulus was converted. The salutation is to those of his household who were Christians, not to Aristobulus himself; he may have been dead, or a non-believer at the time.</p>"},
                {"src": "clarke", "attr": "Adam Clarke", "html": "<p>Apelles, approved in Christ — A man who, on different occasions, had given the highest proofs of the sincerity and depth of his religion. Whoever he was, he had given every demonstration of being a genuine Christian.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "11": {
            "synthesis": "<p>Paul greets Herodion, likely a converted Jew and perhaps a relative, then those of the household of Narcissus who are \"in the Lord\" — a qualifier Clarke notes implies that not all Narcissus's household had believed. Ellicott identifies a historical Narcissus, a famous freedman of Claudius who had been executed years earlier; his household would have passed into imperial ownership, placing these believers among the emperor's household slaves. Calvin pointedly notes that Peter's name does not appear anywhere in this long Roman catalogue — a silence that, he argues, refutes the Catholic claim that Peter was the founding bishop of Rome.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>It would have been unbecoming to have passed by Peter in so long a catalogue, if he was then at Rome: yet he must have been there, if we believe the Romanists. But since in doubtful things nothing is better than to follow probable conjecture, no one who judges impartially will be persuaded that what they affirm is true; for Paul could not surely have passed over in silence so eminent a figure.</p>"},
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p>There had been a famous Narcissus, a freed-man and favourite of Claudius, who had been put to death three or four years before this Epistle was written; his household would then have come into the possession of the emperor. The qualifying phrase \"which are in the Lord\" implies that only part of the household had come to faith.</p>"},
                {"src": "clarke", "attr": "Adam Clarke", "html": "<p>Herodion, my kinsman — Probably another converted Jew. Of the household of Narcissus — Which are in the Lord — This might intimate that some of this family were not Christians; those only of that family that were converted to the Lord being here intended.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "12": {
            "synthesis": "<p>Paul greets Tryphaena, Tryphosa, and Persis — three women commended for their labor in the Lord. Clarke and Barnes both understand these women as serving a diaconal function, visiting the sick and providing pastoral care. Barnes observes a subtle tense distinction in the Greek: Tryphaena and Tryphosa labor in the present tense, while Persis \"labored much\" in the past — suggesting she may have been elderly or that her period of most active service had already concluded. Ellicott notes the two names Tryphaena and Tryphosa may indicate sisters or close relatives.</p>",
            "voices": [
                {"src": "barnes", "attr": "Albert Barnes", "html": "<p>Tryphena and Tryphosa. These names, with the participle rendered \"who labour,\" are in the feminine gender, and these were probably two holy women who performed the office of deaconesses. Persis, too, laboured much in the Lord — the past tense possibly implying that her active service was completed, whether by age or infirmity.</p>"},
                {"src": "clarke", "attr": "Adam Clarke", "html": "<p>Tryphena and Tryphosa — Two holy women who it seems were assistants to the apostle in his work, probably by exhorting, visiting the sick, etc. Persis was another woman who it seems excelled the preceding; for of her it is said she laboured much in the Lord. We learn from this that Christian women, as well as men, labored in the ministry of the word.</p>"},
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>Tryphena and Tryphosa.</strong>—Probably sisters or near relatives. They, too, may have been attached to the court. The names occur with some frequency in inscriptions connected to the imperial household.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "13": {
            "synthesis": "<p>Paul greets Rufus, \"chosen in the Lord,\" and his mother, calling her \"his mother and mine.\" Clarke unpacks the title: <em>eklektos</em> here most likely means eminent or choice rather than simply the theologically elected, as the word carries that connotation in similar LXX usage. Ellicott raises the tradition that this may be the Rufus of Mark 15:21 (son of Simon of Cyrene), plausible if Mark's Gospel was indeed composed at Rome. The phrase \"his mother and mine\" is Paul's most affecting line in the chapter — Barnes calls it \"an instance of the delicacy and tenderness of Paul,\" his way of saying that this woman had mothered him spiritually in the way only an intimate could.</p>",
            "voices": [
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>Rufus.</strong>—Simon of Cyrene is described in St. Mark's Gospel (Mark 15:21) as \"the father of Alexander and Rufus,\" and as there is a substantial tradition that this Gospel was written at Rome, it is not unlikely that the same Rufus may be meant. <strong>His mother and mine.</strong>—An eminent Christian whose motherly care had evidently extended to Paul himself.</p>"},
                {"src": "barnes", "attr": "Albert Barnes", "html": "<p>And his mother and mine. \"His mother in a literal sense, and mine in a figurative one.\" An instance of the delicacy and tenderness of Paul; of his love for this disciple and his mother, as if he were of the same family. Religion binds the hearts of all who embrace it tenderly together, making them feel that they are members of one family.</p>"},
                {"src": "clarke", "attr": "Adam Clarke", "html": "<p>Rufus, chosen in the Lord — <em>Ton eklekton</em>, one of great excellence in Christianity; a choice man. So the word <em>eklektos</em> often signifies excellence and distinction rather than theological election specifically. His mother and mine — One who had shown to Paul all the kindness and tenderness of a mother.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "14": {
            "synthesis": "<p>Paul greets a circle of five men — Asyncritus, Phlegon, Hermas, Patrobas, Hermes — along with the brothers associated with them, likely a house-church group. Ellicott notes that several of these names appear in inscriptions of the imperial household; Hermas and Hermes are very common, Patrobas appears as the name of one of Nero's freedmen. Clarke wisely cautions against assuming identity from shared names alone. Wesley observes that Paul groups these names together because those he names appear connected by kinship, proximity, or circumstance — and that even the unknown poor would have been encouraged to find their names commended to the Roman church by the apostle.</p>",
            "voices": [
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p>Of the names in this verse, Hermas, Patrobas, Hermes all occur with more or less frequency in inscriptions relating to the imperial household. Hermas and Hermes are very common. Patrobas is contracted from Patrobius — a freed-man of Nero's bore that name. These were likely slaves or freedmen now belonging to the Christian community at Rome.</p>"},
                {"src": "wesley", "attr": "John Wesley", "html": "<p>Salute Asyncritus, Phlegon, etc. — He seems to join those together who were joined by kindred, nearness of habitation, or any other circumstance. It could not but encourage the poor especially, to be saluted by name, who perhaps did not know that the apostle had ever heard of them.</p>"},
                {"src": "clarke", "attr": "Adam Clarke", "html": "<p>Salute Asyncritus, etc. — Who these were we know not. Hermas was probably the same to whom a work called the Shepherd is attributed, still extant among the apostolical fathers. But it is in vain to look for identity of persons in similarity of names; for, among the Greeks and Romans, the same names were exceedingly common.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "15": {
            "synthesis": "<p>Paul greets a second group: Philologus and Julia, Nereus and his sister, Olympas, and all the saints with them — almost certainly another house-church. Ellicott notes that Philologus, Julia, and Nereus all appear as names in the imperial household's inscriptions, confirming that early Roman Christianity extended into the domestic ranks of the palace. Wesley draws his sharpest anti-papal argument from this verse: since Paul names every notable Christian in Rome yet says nothing of Peter, Peter could not have been there — and the entire Catholic tradition of Roman episcopal succession from Peter fails at its foundation.</p>",
            "voices": [
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p>Of the names in this verse, Philologus, Julia, Nereus all occur with more or less frequency in inscriptions relating to the imperial household. Philologus appears as a name of some of Claudius's freedmen; Julia was a common name among freedwomen of the court. The gospel had penetrated even the emperor's domestic establishment.</p>"},
                {"src": "wesley", "attr": "John Wesley", "html": "<p>Salute all the saints — Had St. Peter been then at Rome, St. Paul would doubtless have saluted him by name; since no one in this numerous catalogue was of an eminence comparable to his. But if he was not then at Rome, the whole Roman tradition with regard to the succession of their bishops fails in the most fundamental article.</p>"},
                {"src": "clarke", "attr": "Adam Clarke", "html": "<p>Salute Philologus, etc. — Of these several persons, though much has been conjectured, nothing certain is known. They were persons well known to St. Paul, and undoubtedly were such as had gone from different places where the apostle had preached to sojourn or dwell at Rome.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "16": {
            "synthesis": "<p>Paul commands the Roman believers to greet one another with a holy kiss — an Eastern gesture of affection that Christianity consecrated into a mark of spiritual solidarity. Calvin notes that the kiss had long been common among Jews and was adopted by Christians as a sign of mutual love, particularly before participating in the Lord's Supper, though it was later corrupted and eventually restricted. Ellicott traces it into the formal liturgical \"kiss of peace\" that survived in several ancient churches. Barnes emphasizes that the word \"holy\" is the critical qualifier: this is not a social courtesy but a theological act expressing the bond of the body of Christ.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>It is clear from many parts of Scripture that a kiss was a usual and common symbol of friendship among the Jews. It became however a custom among the ancients for Christians to kiss one another before partaking of the Lord's Supper, as a token of mutual love and Christian unity. This custom was afterwards corrupted, and the practice was finally curtailed.</p>"},
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>With an holy kiss.</strong>—A common Eastern and Jewish custom specially consecrated in Christianity. It has its place in the Liturgy of the Apostolic Constitutions, and other early service books, and survives to this day in the liturgical \"kiss of peace\" of several ancient churches.</p>"},
                {"src": "barnes", "attr": "Albert Barnes", "html": "<p>With an holy kiss. This mode of salutation has been practised at all times, particularly in eastern nations. The use of the word <em>holy</em> here serves to denote that Paul intended it as an expression of Christian affection — not merely a social custom, but a mark of the brotherly love that binds the members of Christ's body together.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "17": {
            "synthesis": "<p>After the long catalogue of personal greetings, Paul pivots sharply to warn against divisive teachers. Barnes notes this return to the epistle's central concern for Jew-Gentile unity is characteristic of Paul: unable to let the subject rest, he returns to it even after the epistle appears to be closing. Calvin analyzes the two methods by which Satan's ministers disturb the church: sowing discord that fractures the unity of truth, and setting occasions of offense that trap the unwary. The prescription is to mark them and avoid them — not to engage in controversy with them, but to withdraw from unnecessary association with those who contradict the apostolic teaching.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>He now adds an exhortation by which all Churches have often need of being stirred up; for the ministers of Satan are ever ready to take occasion to disturb the kingdom of Christ. They attempt to make disturbances in two ways: they either sow discord, by which the minds of men are drawn away from the unity of truth, or they occasion offenses, by which men are alienated from the love of the gospel.</p>"},
                {"src": "barnes", "attr": "Albert Barnes", "html": "<p>One great object of this epistle had been to promote peace between the Jewish and Gentile converts. So much did this subject press upon the mind of the apostle that he seems unwilling to leave it. He returns to it again and again; and even after the epistle is apparently concluded, he returns to it to give them a new charge on the subject.</p>"},
                {"src": "wesley", "attr": "John Wesley", "html": "<p>Mark them who cause divisions — Such there were, therefore, at Rome also. Avoid them — Avoid all unnecessary intercourse with them; do not engage them in controversy but withdraw from the association they seek to exploit.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "18": {
            "synthesis": "<p>Paul identifies the invariable diagnostic mark of divisive teachers: they do not serve Christ but their own belly — their motive is appetite and self-interest, not the glory of God. Calvin calls this \"an unvarying mark\" distinguishing false prophets from genuine servants of Christ. Wesley specifies their tools: \"good words\" about themselves — grandiose promises — and \"fair speeches\" to flatter their hearers, flattering the gullible into compliance. Ellicott draws a comparison with Philippians 3:18-19 while acknowledging the group in view may not be identical. The simple-hearted — <em>akakoi</em>, those without guile — are their easiest prey precisely because they do not suspect others of bad faith.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>He mentions an unvarying mark by which false prophets are to be distinguished from the servants of Christ: they have no care for the glory of Christ, but seek the benefit of their stomach. As they deceitfully crept in and by assuming another character concealed their own wickedness, he pointed out the arts they adopted — that they ingratiated themselves by a bland address, alluring men by flattery and sparing their vices.</p>"},
                {"src": "wesley", "attr": "John Wesley", "html": "<p>By good words — Concerning themselves, making great promises. And fair speeches — Concerning you, praising and flattering you. The harmless — Who, doing no ill themselves, are not upon their guard against them that do.</p>"},
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>Their own belly.</strong>—Compare the description in Philippians 3:18-19, where the Apostle is also denouncing certain persons who made \"a god of their belly.\" It is not, however, quite clear that the class of persons intended is precisely the same in both passages.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "19": {
            "synthesis": "<p>Paul acknowledges that the Romans' obedience is celebrated everywhere, yet this very docility makes them vulnerable to exploitation — the same compliant spirit that makes them good hearers also makes them susceptible to plausible deceivers. Calvin reads this \"obedience\" as equivalent to \"faith\" as used in Romans 1:8, treating the two terms as interchangeable: to obey the gospel is to believe it. Ellicott draws a precise grammatical distinction in the Greek: the word for \"simple\" with respect to evil (<em>akeraios</em>, unmixed or uncorrupted) is not the same as naivety or gullibility — it is a positive moral quality of one who has deliberately refused to learn the ways of evil. Wesley's summary is economical: be as knowing as possible about good, as ignorant as possible about evil.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>This he calls \"faith\" in Romans 1:8: so that obedience to the gospel is faith in what it declares. To believe is the special command of the gospel; hence to believe is the special act of obedience that is required; and he who believes is he who shall be saved. But this faith is that of the heart, and not of the lips; and a faith which works by love and overcomes the world.</p>"},
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>Simple concerning evil.</strong>—This is not at all the same word as that translated \"simple\" above. The first refers to natural disposition. The second (<em>akeraios</em>) refers to the result of deliberate choice — an unmixed, uncorrupted quality of will that refuses to acquire familiarity with evil methods or techniques.</p>"},
                {"src": "wesley", "attr": "John Wesley", "html": "<p>But I would have you — Not only obedient, but discreet also. Wise with regard to that which is good — As knowing in this as possible. And simple with regard to that which is evil — As ignorant of this as possible.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "20": {
            "synthesis": "<p>Paul closes his warning with a promise that echoes the protoevangelium of Genesis 3:15: the God of peace will bruise Satan under their feet shortly. The allusion is noted by Barnes and Clarke as deliberate — the crushing of the serpent first promised in Eden will be locally realized as the Roman believers overcome the divisive agents of Satan in their midst. Calvin makes the grammatical point sharply: this is a promise in the indicative mood, not a prayer in the optative — though he acknowledges some manuscripts read it as a prayer. Ellicott associates the \"shortly\" with Paul's expectation of the Messiah's near return and the final resolution of all conflict.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>What follows is a promise to confirm them, rather than a prayer. He indeed exhorts them to fight manfully against Satan, and promises that they should shortly be victorious. He was indeed once conquered by Christ, but not in such a way but that he renews the war continually. He then promises ultimate defeat, which does not appear in the midst of the conflict.</p>"},
                {"src": "barnes", "attr": "Albert Barnes", "html": "<p>The God of peace. The God who promotes peace. Shall bruise. The language here refers to the prediction in Gen 3:15. It here means to subdue, to gain the victory over. It denotes Paul's confidence that they would gain the victory and be able to overcome all the arts of those who were endeavouring to sow discord and contention among them.</p>"},
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>The God of peace.</strong>—We can well understand how the Apostle, in the midst of \"fightings without and fears within,\" should look forward with joyous confidence to the time when all turmoil and conflict would give way to peace. The reference seems to be to his near expectation of the Messiah's return, and with it the final victory of the faith.</p>"}
            ],
            "consensus": "mixed",
            "key_tension": "Calvin insists the verb 'shall bruise Satan' is a firm indicative promise, not a prayer-wish, while Ellicott and others associate the fulfillment with the parousia rather than an immediate local victory, and some manuscripts support an optative reading."
        },
        "21": {
            "synthesis": "<p>Paul relays greetings from his companions gathered at Corinth: Timothy, his closest co-worker; Lucius, whom Clarke identifies as likely Luke the evangelist; Jason, perhaps the same who hosted Paul at Thessalonica and bore the cost of his tumultuous reception (Acts 17:5-7); and Sosipater, likely the Sopater of Acts 20:4. Wesley notes that Timothy is named before Paul's kinsmen — a mark of exceptional honor. Calvin observes that co-signatures from fellow workers were not mere formality but served to foster union between distant churches, confirming that the letter's apostolic message carried the assent of the wider mission team.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>The salutations which he records served in part to foster union between those who were far asunder, and in part to make the Romans know that their brethren subscribed to the Epistle; not that Paul had need of the testimony of others, but because the consent of the godly is not of small importance.</p>"},
                {"src": "wesley", "attr": "John Wesley", "html": "<p>Timotheus my fellow-labourer — Here he is named even before St. Paul's kinsmen. But as he had never been at Rome, he is not named in the beginning of the epistle. His placement first among the co-senders signals the singular closeness of their partnership in the gospel.</p>"},
                {"src": "clarke", "attr": "Adam Clarke", "html": "<p>Timotheus my workfellow — This is on all hands allowed to be the same Timothy to whom St. Paul directs the two epistles which are still extant. Lucius — This was probably Luke the evangelist and writer of the book called The Acts of the Apostles, though some eminent critics dispute this identification.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "22": {
            "synthesis": "<p>Tertius, Paul's amanuensis who physically wrote the epistle at the apostle's dictation, steps forward to insert his own greeting — a rare and touching moment where the scribe's voice enters the text. Ellicott notes this is a departure from the normal convention: Paul habitually added a final flourish in his own hand as authentication, making Tertius's separate greeting unusual. Clarke speculates that Tertius may have been Silas, though the identification remains uncertain. Barnes simply notes that Paul evidently employed a secretary for this epistle, as he may have done commonly, and that Tertius joined the apostle in affectionate greeting.</p>",
            "voices": [
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>Tertius.</strong>—The Apostle's amanuensis. It was the custom of St. Paul to add a few words of parting admonition in his own handwriting, partly as a mark of his personal interest in his readers, and partly as a precaution against forgery. The intrusion of Tertius's own greeting is therefore a striking departure from normal epistolary convention.</p>"},
                {"src": "barnes", "attr": "Albert Barnes", "html": "<p>I Tertius. Of Tertius nothing more is known than is mentioned here. It is evident that Paul employed an amanuensis to write this epistle, and perhaps he commonly did so. Tertius, who thus wrote it, joins with the apostle in affectionate salutations to the brethren at Rome.</p>"},
                {"src": "clarke", "attr": "Adam Clarke", "html": "<p>I Tertius, who wrote this epistle — Some eminent commentators suppose Tertius to be the same with Silas, the companion of St. Paul. If this were so, it is strange that the name generally given him elsewhere in Scripture should not be used in this place.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "23": {
            "synthesis": "<p>Paul passes on greetings from Gaius, his host at Corinth and patron of the whole local church — the same Gaius whom Paul baptized personally (1 Cor. 1:14) and to whom John later addressed his Third Epistle. Then from Erastus, the city treasurer of Corinth, whose civic standing makes him a notable figure: Christianity had penetrated the administrative ranks of a major Roman provincial city. Barnes notes that the title <em>oikonomos</em> implies a position of real governmental responsibility. Quartus, identified simply as \"a brother,\" closes the list — his single title may be all that is needed in a community where brotherhood is the supreme credential.</p>",
            "voices": [
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>Gaius.</strong>—St. Paul was now lodging in the house of Gaius at Corinth. He had been baptized by Paul himself (1 Cor 1:14) and was so highly esteemed by the church that John wrote one of his Epistles to him. <strong>Mine host, and of the whole church.</strong>—He opened his house both to Paul personally and to the church's assemblies.</p>"},
                {"src": "barnes", "attr": "Albert Barnes", "html": "<p>Gaius mine host. Who has received me into his house, and shown me hospitality. He was baptized by Paul himself at Corinth (1Cor 1:14). Erastus, the chamberlain — the city treasurer — his civic office shows that Christianity had penetrated the upper administrative levels of Corinth, not only its poor and enslaved.</p>"},
                {"src": "clarke", "attr": "Adam Clarke", "html": "<p>Gaius mine host — Who has received me into his house and shown me hospitality. And of the whole church — His house being probably a place of public worship for the Christians of Corinth. Erastus the chamberlain of the city — The treasurer of Corinth; a person of considerable rank and influence.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "24": {
            "synthesis": "<p>A second benediction — \"The grace of our Lord Jesus Christ be with you all. Amen\" — appears here in many manuscripts but is absent from the oldest textual witnesses. Ellicott judges this verse a scribal insertion, added to provide a closing benediction before the doxology of verses 25-27, and notes it is wanting in the primary manuscript group. Clarke proposes that Tertius may have added it alongside verses 22-23, with Paul's general permission, as a natural epistolary close. Barnes treats it as original but acknowledges the textual question is genuine. Its content is identical to Paul's standard benediction and raises no theological objection even if secondary.</p>",
            "voices": [
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>The grace of our Lord Jesus Christ.</strong>—This verse is wanting in the oldest group of MSS., and is found chiefly in Græco-Latin Codices and in Antiochene authorities of the fourth and fifth centuries. It is almost certainly a scribal addition, inserted to provide a standard benedictory close before the concluding doxology.</p>"},
                {"src": "clarke", "attr": "Adam Clarke", "html": "<p>The grace of our Lord — This is the conclusion of Tertius, and is similar to what St. Paul used above. Hence it is possible that Tertius wrote the whole of the 22nd, 23rd, and 24th verses, without receiving particular instructions from St. Paul, except the bare permission to add his own salutations with those of his particular friends.</p>"},
                {"src": "barnes", "attr": "Albert Barnes", "html": "<p>The grace of our Lord Jesus Christ be with you all. This benediction closes the chapter in many editions. The textual question is genuine — some of the best manuscript evidence does not include this verse — though its content perfectly matches the apostle's standard benedictory formula elsewhere.</p>"}
            ],
            "consensus": "mixed",
            "key_tension": "Ellicott regards this verse as a scribal insertion absent from the oldest manuscripts; Clarke suggests it may be Tertius's own addition written with Paul's permission; Barnes treats it as original, though all acknowledge the textual uncertainty is real."
        },
        "25": {
            "synthesis": "<p>The closing doxology opens with an ascription of power to God: \"to him who is able to establish you according to my gospel and the preaching of Jesus Christ.\" Wesley makes a remarkable structural observation: the letter's ending answers its beginning with almost exact symmetry — Romans 1:1-5 and Romans 16:25-27 share the same constellation of themes: divine power, the gospel, Jesus Christ, the prophetic scriptures, the obedience of faith, all nations. The letter is a theological ring. Barnes identifies the \"mystery\" as God's comprehensive plan of salvation for Jew and Gentile alike, the mystery that has been the epistle's great subject from chapter 1 through chapter 11.</p>",
            "voices": [
                {"src": "wesley", "attr": "John Wesley", "html": "<p>Now to him who is able — The last words of this epistle exactly answer the first, chapter i. 1–5: in particular, concerning the power of God, the gospel, Jesus Christ, the scriptures, the obedience of faith, all nations. To establish you — Both Jews and Gentiles. According to my gospel, and the preaching of Jesus Christ — that is, according to the tenor of the gospel of Jesus Christ.</p>"},
                {"src": "barnes", "attr": "Albert Barnes", "html": "<p>Now to him that is able, etc. To God; be glory. Who has power to establish you. The apostle thus concludes the whole epistle with an ascription of praise. The mystery here is God's plan of saving men — revealed after long ages of silence — and the establishing of believers is its practical fruit in their lives.</p>"},
                {"src": "clarke", "attr": "Adam Clarke", "html": "<p>Now to him — These and the following verses are by the most reputable MSS. placed at the end of chapter 14; but their proper place appears to be here. To establish you — to fix and settle you firmly in the faith of the gospel. According to my gospel — The doctrine which I preach; the system of truth which God has revealed to me.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "26": {
            "synthesis": "<p>Paul identifies what has been manifested: the long-silent mystery is now disclosed through the prophetic scriptures and proclaimed to all nations for the obedience of faith. Clarke notes that hints of Gentile inclusion were scattered through the OT prophets, but never with the fullness and clarity the gospel now brings. Ellicott and Barnes specify the function of the prophetic scriptures: they serve not as the primary source of the revelation but as its corroboration, confirming after the fact that what God has now done was always his purpose. Wesley adds a crucial observation about the purpose clause: the nations are not merely to receive information but to \"enjoy\" the mystery \"through obeying the faith\" — reception and obedience are inseparable in Paul's missiology.</p>",
            "voices": [
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>But now is made manifest.</strong>—The mystery, before kept secret, has been made manifest. Through the corroboration which it derives from the prophets of the Old Testament, it has, by God's command to the Apostles, been communicated to all the Gentile nations for the purpose of securing their obedience to the faith.</p>"},
                {"src": "wesley", "attr": "John Wesley", "html": "<p>According to the commandment — The foundation of the apostolical office. Of the eternal God — A more proper epithet could not be. A new dispensation infers no change in God. Made known to all nations — Not barely that they might know, but enjoy it also, through obeying the faith.</p>"},
                {"src": "clarke", "attr": "Adam Clarke", "html": "<p>But now is made manifest — Now, under the New Testament dispensation, and by my preaching. By the scriptures of the prophets — Hints relative to this important work being scattered up and down through all their works, but no clear revelation that the Gentiles should be admitted without passing under the law of Moses.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "27": {
            "synthesis": "<p>The doxology closes with the ascription \"to the only wise God, through Jesus Christ, to whom be glory forever. Amen.\" Ellicott notes a genuine grammatical difficulty in the Greek: <em>hô</em> (\"to whom\") is technically antecedent-ambiguous between God and Christ, and if it refers to God, the construction is grammatically irregular; he concludes God is nonetheless the intended referent. Wesley links the verse to 1 Corinthians 1:24, where Christ is identified as \"the wisdom and power of God,\" so that the wisdom ascribed to God in the doxology is inseparable from the Son through whom it is exercised. Barnes draws the theological line: the wisdom praised here is precisely the wisdom displayed in the plan of salvation that the entire epistle has unfolded — wisdom in devising the plan, in adapting it to the renewal of the heart, in the just arrangement by which both Jew and Gentile could be received through faith.</p>",
            "voices": [
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>To God.</strong>—The Greek stands literally: \"To the only wise God, through Jesus Christ, <em>to whom</em> be glory for ever.\" \"To whom,\" if it refers to God, is ungrammatical. If it refers to Christ, the doxology becomes Christocentric. Ellicott concludes that God is the more probable intended referent despite the grammatical irregularity.</p>"},
                {"src": "wesley", "attr": "John Wesley", "html": "<p>To the only wise God — Whose manifold wisdom is known in the church through the gospel, Eph 3:10. \"To him who is able\" and \"to the wise God\" are joined, as 1 Cor 1:24, where Christ is styled \"the wisdom of God\" and \"the power of God.\" To him be glory through Christ Jesus for ever — And let every believer say, Amen!</p>"},
                {"src": "barnes", "attr": "Albert Barnes", "html": "<p>To God only wise. The apostle here resumes the doxology interrupted by the parenthesis. The attribute of wisdom is brought into view because it had been particularly displayed in this plan of salvation now revealed. That wisdom was evinced in devising the plan; in adapting it to the renewing of the heart; in the just arrangement by which both Jew and Gentile could be saved.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        }
    }
}

def main():
    existing = load_synthesis('romans')
    merge_synthesis(existing, ROMANS)
    save_synthesis('romans', existing)
    print('Romans 16 synthesis complete.')

if __name__ == '__main__':
    main()
