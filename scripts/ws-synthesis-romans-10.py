"""
Wide Source Synthesis — Romans chapter 10
bookId: romans
Run: python3 scripts/ws-synthesis-romans-10.py

Sources used: calvin, ellicott, clarke, wesley, barnes, rwp
  (mhcc not found for Romans; jfb file contains Acts content — both omitted)
Chapter range: 10  (21 verses)

Key synthesis decisions:
- v4 "Christ is the end of the law": τέλος means both termination and goal/fulfillment. Ellicott/RWP
  lean toward termination; Wesley = "scope and aim" (goal); Calvin = "complement/completion";
  Clarke = "where the law ends, Christ begins." All agree Christ completes AND supersedes the law.
  Consensus: mixed (on which dimension of τέλος is primary).
- vv. 6-8 Deuteronomy 30 application: all commentators acknowledge Paul is using Moses' words in a
  typological/analogical way. Consensus: affirm (all agree on the gospel meaning drawn from the text).
- v9 confession/belief formula: full consensus across all sources. Consensus: affirm.
- v17 "faith comes by hearing": full consensus. Consensus: affirm.
- Missing keys: calvin v7,v13; ellicott v8,v10,v14; clarke v7; wesley v7,v14 — use
  closest section entry for synthesis.
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

TELOS_TENSION = (
    "Ellicott and RWP read τέλος primarily as termination — Christ ended the law as a system of "
    "salvation; Wesley reads it primarily as goal or aim — the law was designed to drive men to "
    "Christ; Calvin, Clarke, and Barnes read it as both fulfillment and supersession, refusing to "
    "reduce it to one dimension."
)

ROMANS = {
    "10": {
        "1": {
            "synthesis": "<p>Paul reopens the chapter with pastoral warmth: his heart's desire (εὐδοκία) and his prayer before God is for Israel's salvation. The transition from chapter 9's predestination argument is deliberate — Calvin notes that Paul's prayer for Israel would be absurd if they were absolutely reprobated, and Wesley makes the same point directly: \"He would not have prayed for this, had they been absolutely reprobated.\" The prayer serves double duty: it signals genuine love for the people he is about to further indict, and it guards against any impression that the election argument of ch. 9 has made Paul indifferent to evangelism and prayer. RWP observes the unusual Greek word εὐδοκία (goodwill, pleasure, desire) — normally used of God's will, here applied to Paul's own intense longing. Barnes notes that Paul's qualification \"brethren\" opens the verse with the language of kinship and shared faith, softening the severity of what follows. Ellicott reads the verse as Paul's way of showing that even his most rigorous theological arguments were not conducted in a spirit of triumph over unbelieving Israel.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>Paul was careful to soften whatever sharpness there may have been in his manner of explaining the rejection of the Jews. He testifies his goodwill toward them and proves it by the effect: their salvation was an object of concern to him before the Lord. Note: he would not have prayed for this, had they been absolutely reprobated.</p>"},
                {"src": "rwp", "attr": "Robertson's Word Pictures", "html": "<p>Desire (<em>εὐδοκία</em>). No papyri examples of this word with the sense of \"desire\" unless this is one — it normally means will, pleasure, satisfaction (Matt 11:26; 2 Thess 1:11). Prayer for their salvation — Paul would not have uttered this prayer if he had concluded all Israel to be finally reprobated.</p>"},
                {"src": "barnes", "attr": "Barnes' Notes", "html": "<p>\"Brethren\" — an expression of tenderness and affection, denoting his deep interest in their welfare. It opens the chapter in a spirit of kinship rather than controversy. The prayer for Israel's salvation is Paul's credential — the man who prays this for those who persecute him cannot be accused of indifference to them.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "2": {
            "synthesis": "<p>The diagnosis: Israel has a zeal for God, but not according to knowledge (ἐπίγνωσιν — accurate, full knowledge). Ellicott supplies Josephus's testimony to make the charge vivid and historically grounded: \"The Jew knew the Law better than his own name... the sacred rules were punctually observed... the great feasts were frequented by countless thousands.\" The zeal was real; the knowledge was deficient. Calvin sees this distinction as establishing the basis for compassion rather than condemnation: Israel had fallen through ignorance, not malice or deliberate rejection. Wesley captures the irony in a single compressed sentence: \"They had zeal without knowledge; we [Gentiles] have knowledge without zeal.\" RWP adds the structural point from the Greek: the genitive in \"zeal of God\" (ζῆλον θεοῦ) is objective — a zeal directed at God, passionate for God — but pursued without the accurate knowledge of what God actually requires. Barnes affirms that the ignorance was voluntary and therefore criminal: Paul himself had had such zeal before Damascus (cf. Acts 26:6; Philippians 3:5).</p>",
            "voices": [
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p>\"A zeal for God, but not according to knowledge.\" Josephus: \"The Jew knew the Law better than his own name... The sacred rules were punctually observed.\" The zeal was not hypocritical — it was genuine and intense. But it was directed by a misconception of what God actually required for righteousness.</p>"},
                {"src": "wesley", "attr": "John Wesley's Notes", "html": "<p>They had zeal without knowledge; we have knowledge without zeal. The Jew's problem was direction, not intensity — they pursued God with real energy along a road that did not lead to him. The contrasting defect of Gentiles is equally searching: right understanding without earnestness to act on it.</p>"},
                {"src": "barnes", "attr": "Barnes' Notes", "html": "<p>The ignorance of the Jews was voluntary and therefore criminal. An attentive study of their own Scriptures would have led them to the true knowledge of God's plan. Paul himself had such zeal (Acts 26:6; Php 3:5) before his conversion — and knew from the inside how sincere and how misdirected it was.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "3": {
            "synthesis": "<p>The ignorance is specified: being ignorant of the righteousness of God (the way God justifies sinners), and seeking to establish their own righteousness, they have not submitted to God's righteousness. The three movements — ignorance, self-assertion, non-submission — form a coherent spiritual anatomy of works-righteousness. Calvin sees the fundamental contrast: God's righteousness and human righteousness are not merely different but \"wholly contrary\" and mutually excluding. RWP is direct: \"They did not understand the God-kind of righteousness by faith (1:17). They misconceived it (2:4). They did not subject themselves (οὐχ ὑπετάγησαν)\" — the aorist passive of ὑποτάσσω, to be placed in rank under. Clarke's practical summary: they were ignorant of God's method of saving sinners (the only efficient method), and went about to establish their own. Barnes adds the theological weight: God's righteousness is offered as a gift; their own righteousness is demanded as wages — the categories are not merely different but incompatible.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>Notice the contrast between the righteousness of God and that of men. They are opposed to one another as things wholly contrary, and cannot be joined together. Whoever has even a small taste of heavenly wisdom will acknowledge that God's righteousness and human righteousness are mutually exclusive — the one making the other impossible.</p>"},
                {"src": "rwp", "attr": "Robertson's Word Pictures", "html": "<p>Being ignorant (<em>ἀγνοοῦντες</em>). A blunt thing to say, but true (as Paul has shown in 2:1–3:20). They did not understand the God-kind of righteousness by faith (1:17). They misconceived it (2:4). They did not subject themselves (<em>οὐχ ὑπετάγησαν</em>) — second aorist passive of <em>ὑποτάσσω</em>, to submit to rank under another's authority.</p>"},
                {"src": "barnes", "attr": "Barnes' Notes", "html": "<p>God's righteousness is offered as a gift through faith; their own righteousness is demanded as wages earned by works. The categories are not merely different but incompatible. To seek one is to reject the other — for the moment a person insists on earning righteousness, they have declined to receive it as the gift of grace.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "4": {
            "synthesis": "<p>\"For Christ is the end of the law for righteousness to everyone who believes.\" The word τέλος (end) is rich with ambiguity, and the commentators divide somewhat on which dimension is primary. Ellicott leans toward termination: \"Christ is that which brings the functions of the Law to an end by superseding it.\" Wesley reads it as aim or goal: \"the scope and aim of it... it is the very design of the law to bring men to believe in Christ.\" RWP attempts to hold both: \"Christ put a stop to the law as a means of salvation... Christ is the goal or aim of the law... Christ is the fulfilment of the law... Paul's main idea is that Christ ended the law as a method of salvation.\" Clarke combines both: \"Where the law ends, Christ begins. The law ends with representative sacrifices; Christ begins with the real offering.\" Barnes similarly: the word \"end\" means the design, aim, and purpose — the law was designed to lead to Christ, and Christ achieves for faith what the law could only describe. The phrase \"for righteousness\" (εἰς δικαιοσύνην) clarifies the scope: τέλος in the domain of justification specifically, not in every dimension of the law's use.</p>",
            "voices": [
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p>\"End\" — in the proper sense of termination or conclusion. Christ is that which brings the functions of the Law to an end by superseding it. Bengel: \"The Law pursues a man until he takes refuge in Christ; then it says, Thou hast found thine asylum; I shall trouble thee no more, now thou art wise; now thou art safe.\"</p>"},
                {"src": "wesley", "attr": "John Wesley's Notes", "html": "<p>Christ is the end of the law — the scope and aim of it. It is the very design of the law to bring men to believe in Christ for justification and salvation. He alone gives that pardon and life which the law shows the want of but cannot give.</p>"},
                {"src": "rwp", "attr": "Robertson's Word Pictures", "html": "<p>The end of the law (<em>τέλος νόμου</em>). Christ put a stop to the law as a means of salvation (6:14; 9:31); Christ is the goal or aim of the law (Gal 3:24); Christ is the fulfilment of the law (Matt 5:17; 13:10; 1 Tim 1:5). Paul's main idea here is that Christ ended the law as a method of salvation for all who believe.</p>"}
            ],
            "consensus": "mixed",
            "key_tension": TELOS_TENSION
        },
        "5": {
            "synthesis": "<p>Moses describes the righteousness of the law: \"The man who does these things shall live by them\" (Leviticus 18:5). Paul cites Moses himself as witness to the demands of works-righteousness, in order to show how impossible and demanding it is. Calvin notes that Paul refers to Moses rather than the prophets so that Jews could not claim the prophets had softened or modified the law's requirements — the law itself, in its original Mosaic form, makes the demand absolute. Ellicott specifies: the law required actual literal fulfillment; its essence consisted in works, not disposition or intention alone. Wesley presses the condition: \"the man who doeth these things\" means perfect obedience in every point — and anyone who has ever transgressed in any one point has forfeited any claim to life under this system. Barnes draws the application directly: since no one has kept the law perfectly, no one can obtain righteousness on these terms. The citation of Leviticus 18:5 is not an attack on the law but a statement of its actual demand — which, once stated clearly, drives the reader toward the alternative described in vv. 6-8.</p>",
            "voices": [
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p>For Moses describeth — the Law required an actual literal fulfillment. Its essence consisted in works. \"The man which doeth these things shall live\" — not the man who attempts them, or who is disposed toward them, but the man who actually does them, thoroughly and completely.</p>"},
                {"src": "wesley", "attr": "John Wesley's Notes", "html": "<p>The man who doeth these things shall live by them — that is, he that perfectly keeps all these precepts in every point, he alone may claim life and salvation by them. But this way of justification is impossible to any who have ever transgressed any one law in any point.</p>"},
                {"src": "barnes", "attr": "Barnes' Notes", "html": "<p>Since no one has kept the law perfectly, no one can obtain righteousness on these terms. The citation of Leviticus 18:5 is not an attack on the law but a statement of its actual demand — which, stated clearly, reveals its impossibility as a path to justification and drives the reader toward the righteousness of faith.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "6": {
            "synthesis": "<p>\"But the righteousness that comes from faith says thus: 'Do not say in your heart, Who will ascend into heaven?'\" Paul personifies righteousness-by-faith and has it speak in adapted words from Deuteronomy 30:11-14. This is one of Paul's most creative uses of Scripture. RWP acknowledges it openly: \"A free reproduction from Deut 30:11-14... He does not quote Moses as saying this or meaning this. He seizes upon the words for his inspired conviction and experiences of the gospel.\" Calvin notes Paul is not claiming Moses meant what he himself draws from the text — the words are \"turned to a different meaning,\" but legitimately so, because the principle Moses stated about the nearness and accessibility of the Torah applies even more fully to the gospel. Ellicott provides the Deuteronomy context: the original referred to the law itself, which did not require heroic quests to retrieve from heaven. Paul takes the accessibility principle and applies it to the gospel: Christ's incarnation and resurrection mean there is no need to fetch him from heaven or the depths — he is already present in the word proclaimed.</p>",
            "voices": [
                {"src": "rwp", "attr": "Robertson's Word Pictures", "html": "<p>A free reproduction from Deut 30:11-14. Paul personifies \"the from faith righteousness\" (<em>ἡ ἐκ πίστεως δικαιοσύνη</em>). He does not quote Moses as saying this or meaning this. He seizes upon the words for his inspired conviction and experience of the gospel — using them as a vessel for the new wine of the gospel's accessibility.</p>"},
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>Righteousness is personified here, as law and sin had been before. The words of Deuteronomy are turned to a different meaning — Paul does not claim Moses intended the gospel. Rather, the accessibility principle Moses stated about the law (near, not requiring heroic quests) applies even more fully to the gospel.</p>"},
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p>In opposition to the righteousness of works — so laborious and impracticable — the Apostle adduces another quotation to show that the righteousness of faith is much easier and simpler. The original referred to that very law; Paul applies the nearness and accessibility principle to the gospel of Christ.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "7": {
            "synthesis": "<p>\"Or, 'Who will descend into the abyss?' (that is, to bring Christ up from the dead).\" The second forbidden question is paired with the first: no need to ascend to heaven to bring Christ down (implying the incarnation has already occurred), and no need to descend to the abyss to bring Christ up from the dead (implying the resurrection has already occurred). Ellicott notes that \"abyss\" (ἄβυσσον) in the LXX represents the deep, the chaotic waters, and here stands for the realm of the dead — parallel to Sheol in Hebrew thought. RWP observes that Paul has changed the Deuteronomy text's \"sea\" to \"abyss,\" adapting the geography for the resurrection application. Barnes explains the logic: the righteousness of faith asks no impossible questions, demands no heroic journeys — the incarnation and resurrection are accomplished facts; the only thing required is to receive what has already been done. Wesley grounds it pastorally: the gospel's demands are not vertical (ascend or descend) but horizontal — \"the word is near you\" (v. 8), requiring only belief and confession.</p>",
            "voices": [
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p>\"Abyss\" (<em>ἄβυσσον</em>) — in the LXX, the deep, the chaotic waters; here, the realm of the dead, the counterpart to heaven. Paul has adapted the Deuteronomy \"sea\" to \"abyss\" to fit the resurrection application. Neither heaven nor the place of the dead needs to be invaded — both journeys have been completed in Christ.</p>"},
                {"src": "rwp", "attr": "Robertson's Word Pictures", "html": "<p>Paul has changed the Deuteronomy text's \"sea\" (<em>θάλασσαν</em>) to \"abyss\" (<em>ἄβυσσον</em>), adapting the geography for the resurrection application. The descent to the abyss = to bring Christ up from the dead. The meaning: since the resurrection has already happened, asking who will perform it is asking an impossible and unnecessary question.</p>"},
                {"src": "barnes", "attr": "Barnes' Notes", "html": "<p>The righteousness of faith asks no impossible questions and demands no heroic journeys. The incarnation and resurrection are accomplished facts. The only thing required of the believer is to receive what has already been done — to believe, to confess, to call on his name. The difficulty is not vertical but internal.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "8": {
            "synthesis": "<p>\"But what does it say? 'The word is near you, in your mouth and in your heart' — that is, the word of faith that we proclaim.\" Paul applies Deuteronomy 30:14 to the gospel itself: the word of faith is near, accessible, not remote. Wesley identifies the double nearness: \"in thy mouth\" = easy to confess; \"in thy heart\" = easy to believe. Calvin notes that Paul shifts from negative (do not say Who will ascend/descend) to positive: here is what the righteousness of faith affirmatively declares. RWP explains the identification: \"the word of faith\" (τὸ ῥῆμα τῆς πίστεως) is the gospel message concerning faith — objective genitive — the message about faith, the content of which is Christ's completed work. Barnes stresses the contrast with the law: the law placed righteousness at a great distance (requiring perfect performance of difficult demands); the gospel places righteousness near (requiring only reception of what God has already done). Clarke adds the homiletical warmth: the way of salvation is now both plain and easy — the law is magnified and honored by Christ's death, and the doctrine of faith in his death and resurrection is fully proclaimed.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>For the purpose of removing the impediments of faith, Paul has hitherto spoken negatively. Now he adopts an affirmative mode of speaking: the word of faith is near. \"Since the Lord sets his word before our face, no doubt he calls upon us to confess it with our mouth, and to embrace it with our heart\" — accessibility and response belong together.</p>"},
                {"src": "rwp", "attr": "Robertson's Word Pictures", "html": "<p>\"The word of faith\" (<em>τὸ ῥῆμα τῆς πίστεως</em>) — the gospel message concerning faith (objective genitive). Only here. In contrast to the law. The living voice brings home to every one the faith-kind of righteousness. Paul seizes upon the words of Deut 30:14 and applies them to the gospel's nearness and accessibility.</p>"},
                {"src": "barnes", "attr": "Barnes' Notes", "html": "<p>The contrast with the law is sharp: the law placed righteousness at a great distance — requiring performance of difficult demands beyond human reach. The gospel places righteousness near — requiring only reception of what God has already done in Christ. What is near us may be easily obtained; what is far requires difficult journeys.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "9": {
            "synthesis": "<p>\"Because if you confess with your mouth that Jesus is Lord and believe in your heart that God raised him from the dead, you will be saved.\" This verse and the next are the most compact statement of saving faith in Paul's letters. Ellicott calls the confession formula here \"the earliest formal confession of faith\" in the NT epistles. RWP notes it contains two elements presented in reverse order from v. 10 — here confession precedes belief for rhetorical reasons (the mouth/heart sequence of the Deuteronomy quotation), but v. 10 will give the logical order. Calvin observes that \"confess with the mouth\" is not a bare verbal act — it includes all that outward profession entails, including willingness to confess even under persecution. Wesley is acute about the persecuted context: \"even in time of persecution, when such a confession may send thee to the lions.\" Clarke is practical: acknowledge Jesus Christ as the only Savior, believe in your heart that he has been raised for your justification, depend solely on him — and you shall be saved. Barnes specifies the content: the resurrection is the foundation, because without it the death of Christ would not be identified as redemptive.</p>",
            "voices": [
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p>Interesting as containing the earliest formal confession of faith in the Pauline letters. There is no opposition between the outward confession and the inward act of faith — one is regarded as the necessary consequence and expression of the other. The confession is faith's voice; faith is the confession's root.</p>"},
                {"src": "wesley", "attr": "John Wesley's Notes", "html": "<p>If thou confess with thy mouth — even in time of persecution, when such a confession may send thee to the lions. The condition is not casual or private acknowledgment, but public, costly, risk-bearing confession of Jesus as Lord in any and every circumstance.</p>"},
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>\"Confess with the mouth\" is not a bare verbal act — it includes all that outward profession entails. The mouth and heart together make up the full act of faith: inward trust receiving the righteousness, outward profession declaring it. Neither alone is the complete response the gospel requires.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "10": {
            "synthesis": "<p>\"For with the heart one believes and is justified, and with the mouth one confesses and is saved.\" V. 10 restores the logical order that v. 9 reversed: first the heart (faith → justification), then the mouth (confession → final salvation). RWP explains the Greek: both verbs are impersonal passives — \"it is believed,\" \"it is confessed\" — emphasizing the ongoing, general, repeatable character of the process rather than a once-for-all transaction. Calvin distinguishes the two phrases: heart-believing is the inward appropriation of righteousness; mouth-confession is the outward evidence and completion. Wesley draws the comprehensive scope: \"Confession here implies the whole of outward, as believing does the root of all inward, religion.\" Barnes adds the qualification: \"with the heart\" means not with the understanding merely, but with such a faith as shall be sincere and shall influence the whole life — no genuine faith can remain purely notional and internal. Clarke ties it together: sincerity is the condition — the heart must be duly affected with a sense of guilt and the sufficiency of Christ's sacrifice.</p>",
            "voices": [
                {"src": "rwp", "attr": "Robertson's Word Pictures", "html": "<p>Man believeth (<em>πιστεύεται</em>). Impersonal construction — \"it is believed.\" The order is here reversed from verse 9, giving the true logical order: faith first, then confession. Confession is made (<em>ὁμολογεῖται</em>). Impersonal again — \"it is confessed.\" Both heart and mouth are in the instrumental case.</p>"},
                {"src": "wesley", "attr": "John Wesley's Notes", "html": "<p>\"Confession here implies the whole of outward, as believing does the root of all inward, religion.\" The two halves are comprehensive: inward religion (root, heart, justification) and outward religion (fruit, mouth, final salvation) together constitute the complete life of faith.</p>"},
                {"src": "barnes", "attr": "Barnes' Notes", "html": "<p>\"With the heart\" — not with the understanding merely, but with such a faith as shall be sincere and shall influence the whole life. There can be no genuine faith that remains purely notional and internal. Faith that justifies is faith that transforms — and the transformation is what the confession of the mouth manifests.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "11": {
            "synthesis": "<p>\"For the Scripture says, 'Everyone who believes in him will not be put to shame.'\" Paul quotes Isaiah 28:16 again (already cited in 9:33) to anchor the faith-righteousness argument in Scripture. The universal πᾶς (everyone) is the grammatical key: no distinction of person, nation, or background qualifies or limits the promise. Calvin notes that Paul is establishing the universality of the promise before stating it explicitly in v. 12 — the Scripture itself provides the universal form before Paul draws the universal conclusion. RWP highlights the same point: \"the same Lord over all.\" Barnes explains the negative form of the promise — \"not be put to shame\" rather than \"will be glorified\" — as Hebraistic: it is a strong negative expressing a strong positive. To not be put to shame before God is to be fully accepted, vindicated, welcomed. Clarke draws the practical application: all are equally welcome to this salvation. Wesley sees in the πᾶς the implicit answer to every objection of Jewish exclusivism: if Scripture itself says \"everyone,\" no further restriction can be imposed.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>Since faith alone is required — wherever it is found, there the goodness of God manifests itself unto salvation. The universality (\"everyone\") is Paul's scriptural warrant for what he is about to say explicitly: there is no difference between Jew and Greek, because the promise is addressed to all without distinction.</p>"},
                {"src": "barnes", "attr": "Barnes' Notes", "html": "<p>\"Shall not be put to shame\" — a Hebraism expressing a strong positive: to not be put to shame before God is to be fully accepted, vindicated, welcomed. The universal \"everyone\" (<em>πᾶς</em>) in the quotation from Isaiah itself removes any ethnic or legal restriction the reader might try to impose.</p>"},
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p>Christ is the Lord alike of Jew and of Gentile (cf. Eph 4:5). The quotation from Isaiah affirms that the promise attaches to faith, not to ethnicity. The same Lord over all is rich toward all — his resources of grace are not exhausted by any one people's share of them.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "12": {
            "synthesis": "<p>\"For there is no distinction between Jew and Greek; for the same Lord is Lord of all, abounding in riches for all who call on him.\" The universal promise of v. 11 is now explicitly stated as a universal principle. RWP: \"Lord of all (Κύριος πάντων) — see Gal 3:28. Rich (πλουτῶν) — present active participle; his riches are inexhaustible and continuously dispensed.\" Calvin explains the theological grounding of the universality: since the Creator of all is the God of all, he will show himself kind to all without the distinctions of nation. Ellicott: \"Christ is the Lord alike of Jew and of Gentile\" — the same Lord over all is rich, so his blessings are never exhausted and he is never constrained to hold his hand. Clarke is crisp: all are equally welcome to this salvation; one simple way of being saved is proposed to all — faith in the Lord Jesus Christ. Wesley adds the pastoral implication: the Lord's riches are such that the blessing of one does not diminish the share of another — his abundance is not a fixed pie but a perpetually replenished supply.</p>",
            "voices": [
                {"src": "rwp", "attr": "Robertson's Word Pictures", "html": "<p>Lord of all (<em>Κύριος πάντων</em>). See Gal 3:28. Rich (<em>πλουτῶν</em>) — present active participle of <em>πλουτέω</em>. See Eph 3:8, \"the unsearchable riches of Christ.\" His riches are not a fixed fund exhausted by use — they are continuously dispensed toward all who call on him.</p>"},
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>Since he who is the Creator and Maker of the whole world is the God of all men, he will show himself kind to all without the distinctions of nation. The universality of God's lordship is the foundation of the universality of his grace: if he is Lord of all, then his riches are available to all on the same terms.</p>"},
                {"src": "clarke", "attr": "Adam Clarke's Commentary", "html": "<p>All are equally welcome to this salvation. Here the Jew has no exclusive privilege; and from this the Greek is not rejected. One simple way of being saved is proposed to all: faith in the Lord Jesus Christ — because he is the same Lord who has made all and governs all, and is rich in mercy to all.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "13": {
            "synthesis": "<p>\"For everyone who calls on the name of the Lord will be saved\" (Joel 2:32). The climactic OT quotation draws the whole argument together: universal accessibility, through the single act of calling (ἐπικαλέσηται), to the Lord whose riches are inexhaustible. RWP notes that Paul quotes Joel 3:5 (Joel 2:32 LXX), and that this same text was used by Peter at Pentecost (Acts 2:21) — confirming it was a well-established messianic proof text in the early church. Clarke identifies what calling on the name entails: invoking the Lord Jesus Christ as the Savior of sinners; expecting him to save. Barnes notes the universality: \"whosoever shall call\" — as universal as the Gentile mission. Ellicott traces the original application in Joel — \"Jehovah\" is now applied to the Messiah/Lord Jesus, reading the OT text Christologically, which Paul treats as natural and unforced. Wesley draws the missionary implication: since \"whosoever calls\" is saved, and since they cannot call without hearing (v. 14), the obligation to send preachers follows immediately from this promise.</p>",
            "voices": [
                {"src": "rwp", "attr": "Robertson's Word Pictures", "html": "<p>Paul quotes Joel 3:5 (= 2:32 LXX). This same text was used by Peter at Pentecost (Acts 2:21) — confirming it was a well-established messianic proof text. \"Call\" (<em>ἐπικαλέσηται</em>) — deliberative subjunctive as in the chain of questions in vv. 14-15. \"Lord\" here is Jesus, as in Acts 2:36.</p>"},
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p>\"Upon the name of the Lord\" — originally meaning \"of Jehovah,\" but with especial reference to the Messianic Advent. Paul here applies it to our Lord Jesus. The Christological application of the Joel text is not forced but natural — if Jesus is Lord of all (v. 12), then calling on him is calling on the name of Jehovah.</p>"},
                {"src": "barnes", "attr": "Barnes' Notes", "html": "<p>\"Whosoever shall call\" — as universal as the Gentile mission. To call on the name of the Lord is the same as calling on the Lord himself — the name stands for the person. The promise is that no one who so calls will be disappointed; salvation is the answer to every genuine call made on the Lord's name.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "14": {
            "synthesis": "<p>The chain of questions now unfolds with logical beauty: how shall they call on one in whom they have not believed? How shall they believe in one they have not heard? How shall they hear without someone preaching? The three questions trace backward from calling to believing to hearing to preaching, establishing the necessity of the entire evangelistic enterprise. RWP notes that each question picks up the preceding verb: \"call\" → \"believe\" → \"hear\" → \"preach\" — a logical chain in which each link is necessary. Calvin reads the chain as proving that the ministry of the gospel is divinely ordered: it is not an accident that the gospel spreads through preaching; it is the mechanism God designed. Clarke's exposition is characteristically thorough: there can be no salvation without calling; no calling without faith; no faith without hearing; no hearing without preaching; no preaching without a sender. Barnes notes the implicit answer to the Jew who says Gentiles are outside the covenant: if calling on the Lord saves all who call, and if calling requires faith which requires hearing which requires preaching, then the obligation to preach to Gentiles follows from the promise of salvation itself.</p>",
            "voices": [
                {"src": "rwp", "attr": "Robertson's Word Pictures", "html": "<p>How then shall they call? (<em>πῶς οὖν ἐπικαλέσωνται</em>?) Deliberative subjunctive of <em>ἐπικαλέομαι</em> (see vv. 12-13). Each time Paul picks up the preceding verb as the condition — call / believe / hear / preach. A chain of four links, each requiring the prior.</p>"},
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>The ministry of the gospel is not accidental — it is the mechanism God designed for spreading faith. This is the gradation Paul lays down: to show that wherever faith is, God has already given evidence of his grace; that by pouring his blessing on the ministration of the gospel he illumines the minds of men by faith and leads them to call on his name.</p>"},
                {"src": "barnes", "attr": "Barnes' Notes", "html": "<p>Paul adverts to an objection: his doctrine requires faith in Christ for salvation, and faith requires hearing, and hearing requires preaching. The objection was that the Gentiles had not heard and could not believe. Paul's answer (vv. 14-21) is that they have heard — and even if they had not, the obligation to preach to them follows directly from the universal promise of v. 13.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "15": {
            "synthesis": "<p>\"And how are they to preach unless they are sent? As it is written, 'How beautiful are the feet of those who preach the good news!'\" The chain's final link is the divine sending (ἀποσταλῶσιν — the passive implies God as sender). The Isaiah 52:7 quotation pictures the messenger's feet as beautiful because of the message they carry — the tidings of peace, good news, salvation. Calvin reads the sending as proof that God's hand is behind every gospel proclamation: the preacher raises up in his special providence, and that nation to whom the gospel is proclaimed is being visited by God. RWP notes that Paul assumes the missionaries (ἀπόστολοι) have been sent as implied by v. 14. Ellicott specifies that Paul omits some of Isaiah's words and quotes loosely from the LXX, keeping the essence: the beauty of the messenger's arrival is the beauty of the message. Barnes makes the pastoral point: the beauty is in the effect — it is the tidings of good news, the offer of peace with God, that makes even the messenger's dusty feet beautiful. Clarke supplies the exegetical note that feet in Scripture sometimes signify the person's principles and manner of life — \"feet\" = the whole course of the preacher's coming and going for the gospel.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>Paul intimates that it is a proof and pledge of divine love when any nation is favored with the preaching of the gospel. No one is a preacher of it but he whom God has raised up in his special providence — hence there is no doubt that God visits that nation to whom the gospel is proclaimed.</p>"},
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p>A quotation from Isaiah 52:7, more like the Hebrew than the LXX. The beautiful consequences of this preaching were already intimated by the prophet. Paul assumes that the missionaries have been sent — as implied by the logical chain of verse 14. The beauty of the feet is the beauty of the mission they carry out.</p>"},
                {"src": "barnes", "attr": "Barnes' Notes", "html": "<p>The beauty is in the effect — it is the tidings of good news, the offer of peace with God, that makes even the messenger's dusty and travel-worn feet beautiful. No other errand makes feet so beautiful: the physician who brings healing, the soldier who brings victory, the preacher who brings peace with God — the last surpasses all.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "16": {
            "synthesis": "<p>\"But they have not all obeyed the gospel. For Isaiah says, 'Lord, who has believed what he heard from us?'\" The chain of proclamation is complete — and yet many did not obey. Paul anticipates the objection: if sending produces hearing and hearing produces faith, why didn't Israel believe when they heard? He answers with Isaiah 53:1, where the prophet himself laments the unbelief of those who heard his preaching. RWP notes the verb ὑπήκουσαν (obeyed) — they heard but did not heed; some disbelieved then as they do now (3:3). Calvin reads the Isaiah quotation as Paul's way of preventing any argument that the word fails of its purpose when not believed — the very Scripture predicted this outcome. Ellicott sees two threads in Paul's mind simultaneously: (1) the necessity of preaching for faith; (2) the fact that preaching has not resulted in universal faith. The two are held together without canceling each other. Barnes suggests the verse anticipates the chain's incompleteness: hearing is necessary but not sufficient for faith — the same word that saves believers condemns those who hear and disobey.</p>",
            "voices": [
                {"src": "rwp", "attr": "Robertson's Word Pictures", "html": "<p>They did not all hearken (<em>οὐ πάντες ὑπήκουσαν</em>). They heard, but did not heed. Some disbelieve now (3:3) as they did then. He quotes Isa 53:1 to show how Isaiah felt about the same experience — the prophet knew firsthand what it was to preach to unhearing ears.</p>"},
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>Paul introduces this sentence to prevent any argument that the word fails of its purpose when not believed. The quotation from Isaiah shows that this non-reception was foreseen and foretold by the Scripture itself — preaching without universal reception is not a failure of the gospel but a pattern predicted in Israel's own prophets.</p>"},
                {"src": "barnes", "attr": "Barnes' Notes", "html": "<p>Hearing is necessary but not sufficient for faith. The same word that saves those who believe condemns those who hear and disobey. Isaiah's lament — \"Lord, who has believed our report?\" — shows that even the greatest prophet faced the experience of unbelief in his hearers; Paul faces the same with Israel under the gospel.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "17": {
            "synthesis": "<p>\"So faith comes from hearing, and hearing through the word of Christ.\" This is Paul's summary conclusion from the entire chain: hearing (ἀκοή) of the proclaimed word is the God-ordained means by which faith is produced. Ellicott: \"Inference from the prophecy just quoted. Before men can believe, there must be something for them to believe. That something is the word of God, which we preach and they hear.\" RWP identifies the genitive: \"by the word about Christ\" (objective genitive) — the content proclaimed is Christ. Calvin describes the verse as the practical conclusion of the evangelistic chain: God has poured his blessing on the ministration of the gospel to illuminate the minds of men by faith. Clarke states it simply and memorably: \"Preaching, God sends; if heard attentively, faith will be produced; and if they believe the report, the arm of the Lord will be revealed in their salvation.\" Barnes and Wesley both affirm that preaching is the ordinary means of salvation — not the only possible means, but God's designed instrument for bringing people to faith. Wesley adds: \"faith, indeed, ordinarily cometh by hearing; even by hearing the word of God.\"</p>",
            "voices": [
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p>Inference from the prophecy just quoted. Before men can believe, there must be something for them to believe. That something is the word of God, which we preach and they hear. Faith is not self-generated — it has an object, and the object must be announced before it can be embraced.</p>"},
                {"src": "clarke", "attr": "Adam Clarke's Commentary", "html": "<p>Preaching the Gospel is the ordinary means of salvation; faith in Christ is the result of hearing the word, the doctrine of God preached. Preaching, God sends; if heard attentively, faith will be produced; and if they believe the report, the arm of the Lord will be revealed in their salvation.</p>"},
                {"src": "rwp", "attr": "Robertson's Word Pictures", "html": "<p>By the word of Christ (<em>διὰ ῥήματος Χριστοῦ</em>). \"By the word about Christ\" — objective genitive. The content of the proclaimed message is Christ himself — his person, death, and resurrection. It is hearing this word that the Spirit uses to produce faith.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "18": {
            "synthesis": "<p>\"But I ask, have they not heard? Indeed they have, for 'Their voice has gone out to all the earth, and their words to the ends of the world.'\" Paul now closes the potential escape route of ignorance: Israel cannot claim they never heard, because the gospel has been widely proclaimed. He quotes Psalm 19:4, which speaks of the universal witness of creation, applying it to the universal reach of the gospel proclamation. RWP notes the triple affirmative particle μενοῦνγε (\"yes, verily\" or \"nay rather\") — the strongest possible affirmation. Calvin explains the typological move: the psalm declares that God had from the beginning made himself known to the Gentiles, if only through creation; how much more has the fuller light of the gospel now reached them? Ellicott: \"Did they (the Jews) not hear? Yes, for the gospel was preached to them, as indeed to all mankind.\" Clarke makes the application specific: the means of salvation have been placed within the reach of every Jew in Palestine and within reach of those sojourning in Gentile countries where Paul preached. Barnes: Paul's answer does not deny the principle that hearing precedes faith — it affirms that the hearing has in fact occurred.</p>",
            "voices": [
                {"src": "rwp", "attr": "Robertson's Word Pictures", "html": "<p>Yea, verily (<em>μενοῦνγε</em>). Triple particle (<em>μέν, οὖν, γε</em>) as in 9:20 — the strongest possible affirmative. So many nations have already heard the preachers of the gospel that Paul can say of them as David said of the lights of heaven in Ps 19:4. The voice has gone out; the hearing has happened.</p>"},
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>Since the minds of men are imbued by preaching with the knowledge of God, the question is whether that truth has been proclaimed to the Gentiles. Paul's answer: God had from the beginning made himself known to them through creation (Psalm 19); how much more has the fuller light of the gospel now reached them? Non-hearing is not the excuse.</p>"},
                {"src": "barnes", "attr": "Barnes' Notes", "html": "<p>Paul's answer does not deny that hearing precedes faith — it affirms that the hearing has in fact occurred. The gospel has been preached widely enough that Israel cannot claim ignorance as an excuse. The Psalm 19 quotation captures the universality of the reach: their voice has gone into all the earth.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "19": {
            "synthesis": "<p>\"But I ask, did Israel not know? First Moses says, 'I will make you jealous of those who are not a nation; with a foolish nation I will make you angry.'\" Paul now presses further: Israel not only heard, they knew from their own Scripture that the Gentiles would be preferred. Moses in Deuteronomy 32:21 (the Song of Moses) predicted that God would provoke Israel to jealousy by those who are \"not a people\" — the very reversal of election that chapters 9-11 describe. Ellicott: \"Did Israel know that the preaching of the gospel would be thus universal? Yes, certainly, for Moses had warned them of this.\" Calvin reads the argument as the final removal of all Jewish objections: even their most revered lawgiver foresaw and announced the Gentile calling and the Jewish provocation. Wesley explains the logic of the reversal: as Israel had worshipped \"no-gods\" (idols), so God would show favor to a \"no-nation\" — the poetic justice of the divine response. RWP supplies the Greek irony: the Jews had worshipped \"no-gods\" (εἰδώλοις = idols), and now God shows favors to a \"no-nation\" (ἐπ' οὐκ ἔθνει).</p>",
            "voices": [
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p>Did Israel know that the preaching of the gospel would be thus universal, passing from them to the Gentiles? Yes — Moses had warned them of this. The prophecy of Deuteronomy 32:21 was part of Israel's own national song, sung at Moses' command — so Israel's ignorance is inexcusable.</p>"},
                {"src": "rwp", "attr": "Robertson's Word Pictures", "html": "<p>With that which is no nation (<em>ἐπ' οὐκ ἔθνει</em>). The Jews had worshipped \"no-gods\" (idols) and now God shows favour to a \"no-nation\" — the poetic justice of the divine mirror. LXX quotation Deut 32:21. See 1 Cor 10:22 for <em>παραζηλώσω</em> (I will provoke you to jealousy).</p>"},
                {"src": "wesley", "attr": "John Wesley's Notes", "html": "<p>As they had followed gods that were not gods, God accepted in their stead a nation that was not a nation — a nation that was not in their account: the Gentiles, whom they despised. The very structure of Moses' song predicts the reversal: Israel's unfaithfulness → God's turning to the nations → Israel's jealousy → Israel's restoration.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "20": {
            "synthesis": "<p>\"Then Isaiah is very bold and says, 'I have been found by those who did not seek me; I have shown myself to those who did not ask for me.'\" (Isaiah 65:1) If Moses spoke this prediction obliquely, Isaiah states it openly (ἀποτολμᾷ — dares, ventures boldly). Calvin notes that Paul uses this verse to justify his own boldness in asserting the Gentile calling against Jewish prejudice. RWP: \"Isaiah 'breaks out boldly' (Gifford). Paul cites Isa 65:1 in support of his own courage against the prejudice of the Jews.\" Ellicott specifies the original application: in Isaiah, the verse referred to apostate Israel; Paul here applies it to the Gentiles. Barnes explains the argument: the Gentiles had not been seeking God in any systematic way, yet God was found by them — the initiative is entirely divine. The contrast with Israel is stark and implicit: Israel sought God earnestly (9:31) through the law and missed him; the Gentiles were not seeking and were found. Clarke notes that Isaiah was bold to say this because the declaration exposed him to danger among a crooked and dangerous people — the boldness was costly.</p>",
            "voices": [
                {"src": "rwp", "attr": "Robertson's Word Pictures", "html": "<p>Is very bold (<em>ἀποτολμᾷ</em>). Present active indicative of <em>ἀποτολμάω</em>, old word — to assume boldness away from fear (<em>ἀπό</em>). Isaiah \"breaks out boldly\" (Gifford). Paul cites Isa 65:1 in support of his own courage against the prejudice of the Jews about the Gentile calling.</p>"},
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p>\"I was found\" — the original of the quotation referred to apostate Israel; Paul here applies it to the Gentiles. Those who had ceased to belong to the chosen people and those who had never belonged to it were in the same position — equally finding God only by his sovereign initiative, not their seeking.</p>"},
                {"src": "barnes", "attr": "Barnes' Notes", "html": "<p>The Gentiles had not been seeking God in any systematic way, yet God was found by them — the initiative is entirely divine. The contrast with Israel is implicit and devastating: Israel sought God earnestly through the law and missed him; the Gentiles were not seeking and were found. The difference lies in the method of approach, not the intensity of the search.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "21": {
            "synthesis": "<p>\"But of Israel he says, 'All day long I have held out my hands to a disobedient and contrary people.'\" (Isaiah 65:2) The chapter closes with God's word characterizing Israel's response to his persistent overtures. \"All day long\" (ὅλην τὴν ἡμέραν) speaks of continuous, uninterrupted divine patience and persistence. Calvin reads this as the reason God passed over to the Gentiles: his favor had become a mockery to the Jews. RWP provides the dramatic image: \"spread out\" (ἐξεπέτασα — first aorist of ἐκπεταννύμι, to stretch out) — \"a bold metaphor, only here in the NT.\" Barnes: the outstretched hands is the biblical gesture of invitation and pleading — God has not withdrawn or withheld; he has actively, persistently, lovingly extended himself to Israel, and been refused. Wesley closes it in a single sharp contrast: the Gentiles believed with their hearts and made confession with their mouths (v. 10); Israel is \"just opposite — an unbelieving and gainsaying people.\" Ellicott adds the note that the Isaiah passage that follows this verse (65:3 onward) is even darker — Paul stops before the full judgment, leaving the door open for the \"all Israel shall be saved\" of ch. 11.</p>",
            "voices": [
                {"src": "rwp", "attr": "Robertson's Word Pictures", "html": "<p>Did I spread out (<em>ἐξεπέτασα</em>). First aorist active of <em>ἐκπεταννύμι</em>, old verb — to stretch out, a bold metaphor, only here in the NT. All the day long (<em>ὅλην τὴν ἡμέραν</em>) — accusative of extent of time. The stretched-out hands is the biblical gesture of persistent, pleading invitation — the rejection is of a God who kept reaching out.</p>"},
                {"src": "barnes", "attr": "Barnes' Notes", "html": "<p>The outstretched hands is the biblical gesture of invitation and pleading. God has not withdrawn or withheld; he has actively, persistently, lovingly extended himself to Israel and been refused. The disobedience and gainsaying are Israel's — the hands stretched out all day long are God's. The fault lies entirely on one side.</p>"},
                {"src": "wesley", "attr": "John Wesley's Notes", "html": "<p>An unbelieving and gainsaying people — just opposite to those who believed with their hearts and made confession with their mouths (v. 10). The chapter ends with the same contrast it began with: Israel's zeal without knowledge, now specified as active disobedience against the persistently extended grace of God.</p>"}
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
    print('Romans 10 synthesis complete.')

if __name__ == '__main__':
    main()
