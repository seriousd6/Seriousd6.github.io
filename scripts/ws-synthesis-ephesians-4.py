"""
Wide Source Synthesis - Ephesians chapter 4
bookId: ephesians
Run: python3 scripts/ws-synthesis-ephesians-4.py
Sources used: calvin, ellicott, clarke, wesley, barnes, rwp
Not used: mhcc (not found), jfb (data corrupt - contains Romans 13-14 content, not Ephesians 4)
Key synthesis decisions:
  - v8: consensus=mixed - Calvin notes Paul departed from Psalm 68:18 and defends it as
    typological; RWP calls it a Messianic Psalm Paul adapts; genuine interpretive tension
  - v9: consensus=mixed - lower parts of the earth = Incarnation (most) vs. Hades (some);
    Ellicott and RWP both allow either reading; Wesley favors womb/grave
  - v11: four groups or five offices? RWP argues pastors-teachers are one combined office;
    others treat them separately
  - v26: permissive imperative (RWP, Clarke, Barnes) vs. "if angry, do not sin" reading
  - Wesley missing: v2, v5, v15, v23, v27
  - RWP missing: v2
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
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, entry in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entry

EPHESIANS = json.loads(r'''
{
"4": {
"1": {
"synthesis": "<p>Ephesians 4 opens the practical section of the epistle with Paul's appeal from prison: walk worthy of the calling by which you were called. Calvin notes that the three remaining chapters consist entirely of practical exhortations, with mutual agreement as the first subject, framed by the government of the church which Christ established to maintain unity. Ellicott observes that walking worthy may express itself in any of the graces of regenerate humanity, but in this passage the especial point is that they were all called to be <em>one</em> in Christ. Barnes captures the pastoral weight: Paul is in chains, yet he draws authority from that very imprisonment as he begs the Ephesians to maintain the unity their calling demands. Wesley adds the pathos of the apostle's situation: imprisoned for their sake and for the sake of the gospel he had preached among them, his chains make his appeal a powerful motive to their obedience. Robertson notes the attraction of the relative to the genitive of antecedent <em>kleseos</em>, connecting calling and worthy conduct into a single thought.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>The three remaining chapters consist entirely of practical exhortations. Mutual agreement is the first subject, in the course of which a discussion is introduced respecting the government of the church, as having been framed by our Lord for the purpose of maintaining unity among Christians. His imprisonment is appealed to for confirmation of his authority.</p>"},
{"src": "ellicott", "attr": "Ellicott", "html": "<p>Being worthy of the Christian calling may obviously show itself in any of the graces of regenerate humanity, all being features of the image of Christ. But in this passage the especial point which has been dwelt upon in their calling is the fact that they were all called to be one in Christ, and the grace of unity is specially enforced.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>The apostle now begins the practical part of the epistle, enforcing various duties growing out of the argument he had maintained. Paul is in prison, yet he bears his chains as a motive to their obedience, reminding them that he is a prisoner of the Lord for their sake and for the gospel's sake.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"2": {
"synthesis": "<p>The virtues Paul names as the ground of worthy walking — lowliness, meekness, long-suffering, and forbearing one another in love — are the specific graces that produce and preserve unity. Calvin notes that humility is the first step toward unity, since it produces the meekness that enables bearing with brethren and prevents the perpetual fractures pride would otherwise cause. Barnes provides lexical depth, tracing <em>tapeinophrosune</em> to its occurrence in Acts 20:19 and Philippians 2:3, and noting that the word for forbearing, <em>anechomenoi</em>, denotes actively sustaining one another, not merely tolerating. Clarke is precise: meekness is the opposite of anger and irritability, while long-suffering (<em>makrothumia</em>) is long-mindedness, never permitting trial or provocation to exhaust patience. The addition of <em>in love</em> to <em>forbearing one another</em> singles out love as the animating spirit without which the other virtues become mere social conventions.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>Paul mentions humility first because he was about to enter on the subject of unity, to which humility is the first step. This again produces meekness, which disposes us to bear with our brethren, and thus to preserve that unity which would otherwise be broken a hundred times in a day.</p>"},
{"src": "clarke", "attr": "Clarke", "html": "<p>With all lowliness: <em>tapeinophrosune</em> signifies subjection or humility of mind. Meekness is the opposite to anger and irritability of disposition. Long-suffering: <em>makrothumia</em>, long-mindedness; never permitting a trial or provocation to get to the end of your patience. Forbearing one another: <em>anechomenoi alleloon</em>, sustaining one another, helping to support each other's burdens.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>With all lowliness: humility; compare Philippians 2:3, in lowliness of mind let each esteem other better than themselves. Long-suffering: patience in bearing with the faults and injuries of others, not easily provoked, enduring with calm fortitude the evils which flow from the ill-conduct of others.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"3": {
"synthesis": "<p>Having listed the virtues that prepare for unity, Paul calls believers to endeavor to keep the unity of the Spirit in the bond of peace. Calvin notes that with good reason does Paul recommend forbearance as tending to promote this unity; innumerable offenses arise daily, particularly given the extreme bitterness of man's natural temper. Barnes carefully distinguishes: the unity of the Spirit does not refer to the fact that there is one Holy Spirit, but to unity of affection, of confidence, of love — a united spirit in believers. Clarke observes that the church at Ephesus was composed partly of converted Jews and Gentiles, whose different backgrounds made frequent causes of altercation natural, the Jews potentially envious of Gentiles sharing their privileges without circumcision. Robertson traces the late and rare word <em>enoteta</em> (unity), appearing in Aristotle and Plutarch, noting that it appears in the New Testament only here and in verse 13, and that there is no peace without love as laid down in verse 2.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>With good reason does he recommend forbearance, as tending to promote the unity of the Spirit. Innumerable offenses arise daily which might produce quarrels, particularly when we consider the extreme bitterness of man's natural temper. This unity is produced in us by the Spirit of God alone.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>The unity of the Spirit refers not to the fact that there is one Holy Spirit, but to unity of affection, of confidence, of love among Christians. Such a unity would be produced only by the Holy Spirit; and, as there is but one Spirit, the unity which he produces will be one and the same.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>The unity: <em>ten enoteta</em>, late and rare word from <em>eis</em>, one, in Aristotle and Plutarch, only here and verse 13 in the New Testament. In the bond of peace: in Colossians 3:14 love is the bond, but there is no peace without love as verse 2 shows.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"4": {
"synthesis": "<p>The sevenfold unity — one body, one Spirit, one hope, one Lord, one faith, one baptism, one God and Father — grounds the ethical appeal in theological reality. Calvin observes that the repetition of <em>one</em> shows in how complete a manner Christians ought to be united; these words denote the whole person, since we ought to be one not merely in external conduct but in heart and soul. Barnes notes that as there is but one church, there ought to be unity, even though the church is presently divided into many denominations with different forms of worship. Wesley compresses it to essentials: one body is the universal church, one Spirit, one Lord, one God and Father — the ever-blessed Trinity, and one hope of heaven. Robertson identifies the one body as the mystical body of Christ (the spiritual church or kingdom), the one Spirit as the Holy Spirit (grammatical neuter but not to be referred to by <em>it</em> but by <em>he</em>), and the one hope as the same hope for both Jew and Greek as shown in chapter 2.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>He proceeds to show more fully in how complete a manner Christians ought to be united. The union ought to be such that we shall form one body. These words denote the whole man; we ought to be not merely one in outward conduct but one in heart and soul, with the entire person oriented to the same head.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>There is one body, one church: for so the word body means here, denoting the body of Christ. As there is really but one church on earth, there ought to be unity. The church is at present divided into many denominations, yet the appeal to oneness is founded in the one Spirit given to all members.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>One body: one mystical body of Christ, the spiritual church or kingdom. One Spirit: one Holy Spirit, grammatical neuter gender, not to be referred to by <em>it</em> but by <em>he</em>. In one hope: the same hope as a result of their calling, for both Jew and Greek as shown in chapter 2.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"5": {
"synthesis": "<p>One Lord, one faith, one baptism. Calvin explains that the frequent repetition of <em>one</em> points to the indivisibility of the Christian relationship to Christ: we cannot be his subjects unless we are of one mind, and the oneness of Lord, faith, and baptism all point to the same unity. Ellicott traces the logic: from the idea of the calling, Paul passes naturally to him who calls — the one Lord — and to the method of his calling, first by the one faith and then by the one baptism at which profession of that faith is made. Barnes stresses that the argument is that there ought to be unity among Christians because they have one Lord and Saviour; there are not different saviours adapted to different classes, not one for the Jew and another for the Greek, not one for the rich and one for the poor. Robertson notes the Greek distinction: <em>baptisma</em> is the result of baptizing while <em>baptismos</em> is the act, and there is only one act of baptism for all who confess Christ by means of this symbol.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>In the first Epistle to the Corinthians he employs the word to denote simply the government of God; here he gives this appellation strictly to Christ, to whose government we cannot be subject unless we are of one mind. The frequent repetition of one points to the indivisibility of the Christian relationship to Christ.</p>"},
{"src": "ellicott", "attr": "Ellicott", "html": "<p>From the idea of the calling the Apostle passes naturally to him who calls, the one Lord, and to the method of his calling to himself, first by the one faith, and then by the one baptism at which profession of that one faith is made. It is on the indwelling of Christ in each heart by faith that the spiritual unity of all Christians primarily depends.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>One Lord: this evidently refers to the Lord Jesus. The argument is that there ought to be unity among Christians because they have one Lord and Saviour. They have not different Saviours adapted to different classes; not one for the Jew and another for the Greek; not one for the rich and one for the poor.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"6": {
"synthesis": "<p>The sevenfold unity reaches its apex: one God and Father of all, who is over all, through all, and in all. Calvin identifies this as the main argument from which all the rest flow: we are united by faith, by baptism, or even by the government of Christ because God the Father, extending his gracious presence to each, employs these means for gathering us to himself. Ellicott notes that the universal Fatherhood cannot be limited, though the context shows the immediate reference is to those who are his children by adoption in Christ. Barnes applies the theological logic: were there many gods to be worshipped, there could be no hope of unity; men who worship many gods cannot be united since their affections are directed to different objects. Robertson traces the three prepositions — <em>epi</em>, <em>dia</em>, <em>en</em> — as Paul's endeavor to express the universal sweep and power of God in men's lives, over all, through all, and in all.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>This is the main argument, from which all the rest flow. How comes it that we are united by faith, by baptism, or even by the government of Christ, but because God the Father, extending to each of us his gracious presence, employs these means for gathering us to himself?</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>One God; therefore there should be unity. Were there many gods to be worshipped, there could be no more hope of unity than there is among the worshippers of Mammon and various other idols. Men who worship many gods cannot be united; their affections are directed to different objects and there is no harmony or sympathy between them.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>One God and Father of all: not a separate God for each nation or religion. See here the Trinity again. Who is over all, and through all, and in all: Paul endeavours to express the universal sweep and power of God in men's lives by three prepositions, <em>epi</em>, <em>dia</em>, <em>en</em>.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"7": {
"synthesis": "<p>Having established the unity that binds all believers, Paul turns to the diversity of gifts within that unity. Calvin explains the relational principle: no member of the body of Christ is endowed with such perfection as to be able, without the assistance of others, to supply his own necessities; a certain proportion is allotted to each, and only by communicating with each other do all enjoy what is sufficient. Barnes notes that the grace given here most probably means the gracious influences of the Holy Spirit, or his operations on the heart in connection with the specific gifts needed for one's calling. Ellicott observes that the phrase <em>the grace</em> with the article suggests the one grace of the Lord Jesus Christ given in the Divine purpose in the regeneration of the whole body, though received and made one's own separately in each soul and gradually in the course of life. Robertson notes that each gets the gift that Christ has to bestow for his special case, citing the comparable passages in 1 Corinthians 12 and Romans 12.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>No member of the body of Christ is endowed with such perfection as to be able, without the assistance of others, to supply his own necessities. A certain proportion is allotted to each; and it is only by communicating with each other that all enjoy what is sufficient for maintaining their respective places in the body.</p>"},
{"src": "ellicott", "attr": "Ellicott", "html": "<p>To every one of us the grace was given according to the measure of the gift of Christ. It was given in the Divine purpose in the regeneration of the whole body, although it has to be received and made our own separately in each soul and gradually in the course of life, in the measure Christ bestows for each special case.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>Every Christian has received the means of living as he ought and God has made ample provision for it in his gospel. The grace referred to here most probably means the gracious influences of the Holy Spirit, his operations on the heart in connection with the specific gifts needed for each person's calling in the body.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"8": {
"synthesis": "<p>Paul cites Psalm 68:18 to ground the giving of gifts in Christ's ascension, though his citation diverges significantly from both the Hebrew and the Septuagint. Calvin acknowledges directly that Paul has departed not a little from the true meaning of this quotation, defending this as a typological rather than logical use of Scripture: Paul does not reason as a logician about what necessarily follows, but applies the deeper spiritual truth that the same God who worked in the Exodus ascent now works in Christ's ascension, giving gifts to men rather than receiving them. Ellicott traces the psalm to a celebration of the ark's movement to Zion under David, and explains the striking change from <em>received</em> to <em>gave</em> as a free quotation making the point that those whom the victorious King leads captive become themselves gifts distributed to his people. Barnes notes that Paul adduces this psalm to prove that Christ obtained gifts for men at his ascension and now bestows them. Robertson calls it a Messianic Psalm of victory which Paul adapts and interprets for Christ's triumph over death.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>To serve the purpose of his argument, Paul has departed not a little from the true meaning of this quotation. He does not here reason as a logician about what necessarily follows; rather, he sees in the psalm's ascent a type of Christ's ascension and applies the deeper spiritual truth to the giving of gifts to men in the new covenant.</p>"},
{"src": "ellicott", "attr": "Ellicott", "html": "<p>The reference is to Psalm 68, a psalm celebrating some moving of the ark, traditionally connected with David's bringing up of the ark to Mount Zion. The change from <em>received</em> to <em>gave</em> shows it to be a free quotation; those whom the victorious King leads captive become themselves gifts distributed to his people.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>The quotation is from Psalm 68:18, a Messianic Psalm of victory which Paul adapts and interprets for Christ's triumph over death. He led captivity captive: cognate accusative of <em>aichmalosian</em>, late word, only here and Revelation 13:10 in the New Testament.</p>"}
],
"consensus": "mixed",
"key_tension": "Calvin acknowledges Paul departed from the text and defends it as typological application; most commentators accept this as legitimate apostolic use of a Messianic psalm, though the exact interpretive principle varies."
},
"9": {
"synthesis": "<p>The descent corresponding to the ascent is interpreted differently by the commentators. Calvin defends the inference as meaningful even if not strictly logical: Paul's purpose is to make the point that the same Christ who once descended is now the one who ascended and gives gifts. The question of what <em>lower parts of the earth</em> means divides interpreters: Wesley reads it as the womb (citing Psalm 139:15) or the grave (citing Psalm 63:9), referring to the Incarnation and death. Ellicott notes that the reasoning of the text would be satisfied by understanding <em>lower parts of the earth</em> as the regions of the earth, simply lower than heaven, referring to the Incarnation, while acknowledging the alternative reading of regions beneath the earth. Barnes, surveying options, concludes that the phrase most probably refers to the Incarnation — Christ coming down from heaven to earth. Robertson observes that if the <em>anabas</em> (ascension) implies a previous <em>katabas</em> (descent), the descent would be from heaven to earth via Incarnation, and <em>tes ges</em> would be the genitive of apposition.</p>",
"voices": [
{"src": "ellicott", "attr": "Ellicott", "html": "<p>The lower parts of the earth may mean either the regions of the earth as lower than heaven, or the regions beneath the earth. The reasoning of the text would be satisfied by the former: Paul is simply arguing that the use of the phrase ascended from earth to heaven implies a previous descent from heaven to earth, exactly as in John 3:13.</p>"},
{"src": "wesley", "attr": "Wesley", "html": "<p>Now this expression, he ascended, what is it but that he descended? That is, does it not imply that he descended first? Into the lower parts of the earth: so the womb is called in Psalm 139:15, the grave in Psalm 63:9. The descent refers to his Incarnation and humiliation unto death.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>If the <em>anabas</em> (ascended) is the Ascension of Christ, then the <em>katabas</em> (coming down) would be the Descent of the Incarnation to earth, and <em>tes ges</em> would be the genitive of apposition. What follows in verse 10 confirms this: he who descended is himself also the one who ascended.</p>"}
],
"consensus": "mixed",
"key_tension": "Commentators divide on whether the lower parts of the earth refers to the earth itself (Incarnation) or to the realm beneath the earth (Hades); the Incarnation reading is more common among these sources."
},
"10": {
"synthesis": "<p>The one who descended is the same who ascended far above all heavens, that he might fill all things. Calvin insists that when Christ is said to be in heaven, we must not view him as dwelling among the spheres; heaven denotes a place higher than all spheres, assigned to the Son of God after his resurrection. The purpose clause — that he might fill all things — is read by Ellicott as particularly referring to the gift of the fullness of his grace flowing from his glorified humanity to all his members, though the words are too wide for any limitation. Clarke states the contrast with maximum force: he who descended is the same who has ascended; he came to the lowest abasement (emptying himself, taking the form of a servant, humbling himself to death on the cross) and is now ascended far above all heavens with a name above every name. Wesley captures the Trinitarian movement: the one who thus amazingly humbled himself is the same who was so highly exalted, that he might fill the whole church with his Spirit, presence, and operations.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>When Christ is said to be in heaven, we must not view him as dwelling among the spheres and numbering the stars. Heaven denotes a place higher than all spheres, assigned to the Son of God after his resurrection. He fills all things means that his power and virtue are diffused through every part of the universe.</p>"},
{"src": "ellicott", "attr": "Ellicott", "html": "<p>That he might fill all things: compare the description in Ephesians 1:23 of the Lord as filling all in all. The reference is more particularly to the gift of the fullness of his grace flowing from his glorified humanity to all his members. But the words are too wide for any limitation; in heaven and earth his presence and sovereignty extends.</p>"},
{"src": "clarke", "attr": "Clarke", "html": "<p>He who descended so low is the same who has ascended so high. He came to the lowest abasement, emptied himself, took the form of a servant, humbled himself unto death even the death of the cross; now he is ascended far above all heavens, higher than all height, with a name above every name.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"11": {
"synthesis": "<p>From the ascended Christ flows the giving of specific ministers to the church: apostles, prophets, evangelists, pastors and teachers. Calvin reads the ministry offices as the means by which the diversity of gifts within the body produces unity, as various tones in music produce sweet melody. Ellicott notes the emphasis: <em>he</em> gave — he and he alone, as the ascended Head of humanity; those who are ministers of his gifts are themselves gifts from him to the church. Barnes notes that the list parallels 1 Corinthians 12:28 and provides for both the extraordinary officers (apostles, prophets, evangelists) and the ordinary officers (pastors and teachers). Wesley distinguishes: a prophet testifies of things to come, an evangelist of things past by preaching the gospel before or after the apostles; all these were extraordinary, while pastors and teachers are ordinary. Robertson identifies four groups in Greek (note <em>tous men, tous de</em> three times), arguing that <em>pastors and teachers</em> are one combined office in Paul's thinking.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>He returns to explain the distribution of gifts and illustrates at greater length what he had hinted: that out of this variety arises unity in the church, as the various tones in music produce sweet melody. The external ministry of the word is commended on account of its advantages; certain men appointed to that office are employed in preaching the gospel.</p>"},
{"src": "ellicott", "attr": "Ellicott", "html": "<p>He gave: in the original <em>he</em> is emphatic — he and he alone as the ascended Head of humanity. The word <em>gave</em> instead of the more obvious word <em>set</em> or <em>appointed</em> is suggested by verse 8. Those who are ministers of his gifts are themselves gifts from him to the church.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>There are four groups: <em>tous men, tous de</em> three times, as the direct object of <em>edoken</em>. The titles are in the predicate accusative. Paul uses <em>edoken</em> (gave) from the quotation in verse 8, repeating that Christ the giver is the source of all ministry in the church.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"12": {
"synthesis": "<p>The purpose of all these ministry offices is threefold: for the perfecting of the saints, for the work of ministry, and for the edifying of the body of Christ. Calvin observes that <em>katartismos</em> — the Greek word for perfecting — signifies literally the adjustment of things possessing symmetry and proportion, so that the word comes close in meaning to <em>full development</em>. The three purposes are not parallel but sequential: the perfecting of the saints enables the work of ministry, and the work of ministry produces the edification of the body. Ellicott notes the different prepositions used and judges the right sense to be that ministers are given for the comprehensive work of equipping saints, who then do ministry, building up the body. Barnes explains that <em>katartismon</em> properly refers to restoring anything to its place, then putting in order, making complete; Christ appointed various officers so that everything in the church might be well arranged. Wesley summarizes the three purposes clearly: perfecting saints in number and gifts, service in ministry, and building up the body in faith, love, and holiness.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>The Greek word <em>katartismos</em> signifies literally the adjustment of things possessing symmetry and proportion; just as in the human body the members are united in a proper and regular manner. So the word comes close in meaning to full development or perfect equipment of each member for their place in the body.</p>"},
{"src": "ellicott", "attr": "Ellicott", "html": "<p>The prepositions used differ significantly: <em>pros</em> for the perfecting of saints suggests contact with an aim, while <em>eis</em> in the latter clauses suggests movement into a goal. Chrysostom takes the three as parallel, but the better reading sees them as sequential: equipped saints do ministry, and ministry builds up the body.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>For the perfecting of the saints: <em>katartismon</em> properly refers to restoring anything to its place, putting in order, making complete. Here it means that these various officers were appointed so that everything in the church might be well arranged, or put into its proper place, and the church might be complete in all its parts.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"13": {
"synthesis": "<p>The goal of the ministry is maturity, unity, and full knowledge — and these are not temporary goals to be surpassed but permanent ones to be attained by the whole church together. Calvin reminds his readers that the necessity for ministry is not confined to a single day but continues to the end of life; the ministry is not like a school for children to be outgrown, but is perpetually needed as long as we are in this mortal life. Barnes states the telos: till we all arrive at a state of complete unity and entire perfection, holding the same truths and the same confidence in the Son of God. Wesley emphasizes the corporate dimension: <em>till we all</em> — every one of us — come to the unity of the faith and knowledge, to a state of spiritual manhood in understanding and strength, to the full stature of Christ. Robertson focuses on the verb <em>katantesomen</em>, to come down to the goal, used of arriving after a journey — the full-grown man of verse 13 is the same metaphor as verse 15.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>Paul had already said that by the ministry of men the church is regulated and governed. But his commendation of the ministry is now carried farther: the necessity for which he pleads is not confined to a single day but continues to the end. The use of the ministry is not temporal, like that of a school for children, but perpetual.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>Till we all come to complete unity and entire perfection. In the unity of the faith: till we all hold the same truths, and the same confidence in the Son of God. And of the knowledge of the Son of God: that they might attain the same practical acquaintance with the Son of God and thus come to the maturity of Christian piety.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>Till we all attain: temporal clause with purpose idea, first aorist subjunctive of <em>katantao</em>, to come down to the goal. <em>The whole</em> including every individual; hence the need of so many gifts. Unto the unity of the faith: oneness of trust in Christ which the Gnostics were disturbing.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"14": {
"synthesis": "<p>Mature faith means no longer being children, tossed about by every wind of doctrine and by the cunning craftiness of those who lie in wait to deceive. Calvin describes the intervening period between childhood and maturity in faith: those who are children have not yet advanced a step in the Lord, or still hesitate and have not determined what road to choose, moving sometimes one way and sometimes another. Ellicott clarifies that the word used for children here is almost always used in a bad sense — not the guilelessness or trustfulness of children, which Jesus commended, but the changeableness and credulity that make them easy victims of deceivers. Barnes notes that children have characteristics besides simplicity and docility — they are often changeable, credulous, and influenced by those who are crafty. Wesley highlights the image of dice-cogging: the Greek word for sleight, he notes, literally implies someone cogging the dice, loading them to produce a false result. Robertson observes that some Christians are quite content to remain babes in Christ and never cut their eye-teeth, becoming the victims of every charlatan who comes along.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>Having spoken of that perfect manhood toward which we are proceeding, he reminds us that during such progress we ought not to resemble children. Those are children who have not yet advanced a step in the way of the Lord, but who still hesitate, who have not yet determined what road they ought to choose, but move sometimes one way and sometimes another.</p>"},
{"src": "ellicott", "attr": "Ellicott", "html": "<p>The word used here is almost always applied in a bad sense, like our word childish, not to the guilelessness, trustfulness, or humility of children which our Lord emphatically blessed, but to the changeableness and credulity that make them easy victims of those who use cunning craftiness to deceive.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>That we may be no longer children: negative final clause with present subjunctive. Some Christians are quite content to remain babes in Christ and never cut their eye-teeth, the victims of every charlatan who comes along. Tossed to and fro: present passive participle of <em>kludonizomai</em>, to be agitated by the waves, only here in the New Testament.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"15": {
"synthesis": "<p>In contrast to children being tossed about, believers are to speak the truth in love and grow up in all things into Christ. Calvin, citing Ellicott's reading favorably, renders the Greek <em>aletheuontes</em> not merely as speaking truth but as embracing and adhering to it; and to render the Christian perfect, love must accompany this regard to truth, since truth without love becomes a weapon and love without truth becomes indulgence. Barnes identifies two key principles: the truth is to be spoken — the simple, unvarnished truth in opposition to all trick, art, cunning, and deception — and it is to be spoken in love, to avoid the spirit of controversy and the desire to overwhelm rather than benefit. Clarke is emphatic that scolding and abuse from the pulpit or press in matters of religion are truly monstrous; he who has the truth of God has no need of any means but truth itself to defend it. Robertson notes that if truth were always spoken only in love, the church would be far different.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>He enjoins us to embrace and adhere to the truth; and, to render the Christian perfect, he must add to this regard to truth, love, or universal affection and benevolence. It was a noble saying of Pythagoras agreeable to this sentiment of our apostle: these two things are most lovely, to speak truth and to repay benefits.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>Two things are to be noted. The truth is to be spoken, the simple, unvarnished truth, in opposition to all trick and cunning and fraud and deception. And it is to be spoken in love; not to overwhelm an opponent, not in the spirit of controversy, but from love to the souls of men and to him who is the truth.</p>"},
{"src": "clarke", "attr": "Clarke", "html": "<p>The truth recommended by the apostle is the whole system of Gospel doctrine, to be taught and preached. This truth, as it is the doctrine of God's eternal love to mankind, must be preached in love. Scolding and abuse from the pulpit or press in matters of religion are truly monstrous; he who has the truth of God has no need of any means to defend it but truth itself.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"16": {
"synthesis": "<p>From Christ the whole body, fitly joined together and compacted through every joint's supply, makes increase to the edifying of itself in love. Calvin identifies three key principles: first, all life and health diffused through the body flows from Christ as its source; second, each member makes its contribution to the whole body rather than only receiving; third, all increase tends to exalt Christ's glory. Barnes uses the body analogy to illuminate the passage: as the head in the human frame conveys vital influences to every part, so Christ is the source of life and energy and increase to the church. Ellicott provides technical precision: the word rendered <em>fitly joined together</em> is the same used in Ephesians 2:21 for a building — clamped or bonded together — here applied to the union of limbs as being jointed. Wesley captures the corporate beauty: every joint supplying, every member contributing in its measure, the whole fitly joined and compacted, making increase in love.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>All the life or health which is diffused through the body must flow to us from Christ. As the root conveys sap to the whole tree, so all the vigor we possess must flow from Christ. Each member makes its contribution to the whole, and all increase tends to exalt more highly the glory of Christ from whom all proceeds.</p>"},
{"src": "ellicott", "attr": "Ellicott", "html": "<p>The word rendered fitly joined together is the same used in Ephesians 2:21 with more technical accuracy, of a building clamped or bonded together. Here the two words are applied to the union of the limbs of the body as being jointed and brought into close contact, so that all life flows from the Head.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>From which: out of which as the source of energy and direction. Through every joint of the supply: through every joint that contributes to the supply. In due measure: the assumption that each part of the body works proportionately as it ought. In love: the sphere and atmosphere of the whole growth.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"17": {
"synthesis": "<p>With full apostolic solemnity Paul turns to the contrast between the Christian life and the life of the Gentile world. Calvin describes this as Paul explaining what fruits the doctrine of the gospel ought to yield, beginning with the exhortation to renounce the way of unbelievers and arguing from its inconsistency with their present views. Barnes notes that Paul bears witness in the name of the Lord Jesus, not as expressing his own private opinion but with full authority, reminding them of what they were before conversion and of the manner in which the surrounding heathen still lived. Wesley connects this verse back to verse 1: Paul returns to where he began, testifying in the Lord's name. Clarke enumerates the particulars of the Gentile condition Paul will describe: walking in vanity of mind, which is the root of all evil walking, the loss of the knowledge of the true God leading inevitably to practical darkness and corruption. Robertson notes the infinite present active of <em>peripatein</em> in indirect command, placing the prohibition under apostolic authority.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>He next inquires what fruits the doctrine of the gospel ought to yield in the lives of Christians, or begins to explain minutely the nature of that edification by which doctrine ought to be followed. He first exhorts them to renounce the way of unbelievers, arguing from its inconsistency with their present views and calling.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>I bear witness in the name of the Lord Jesus, or ministering by his authority. The object is to exhort them to walk worthy of their high calling and to adorn the doctrine of the Saviour. With this view, he reminds them of what they were before they were converted and of the manner in which the heathen around them lived.</p>"},
{"src": "wesley", "attr": "Wesley", "html": "<p>He returns thither where he began, Ephesians 4:1, and testifies in the Lord, in the name and by the authority of the Lord Jesus. In the vanity of their mind: having lost the knowledge of the true God, Romans 1:21. This is the root of all evil walking.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"18": {
"synthesis": "<p>The Gentiles are darkened in their understanding, alienated from the life of God through the ignorance in them, because of the hardness of their hearts. Calvin observes that the phrase <em>life of God</em> may mean either what is accounted life in God's sight or the life God bestows on the elect by the Spirit of regeneration; in both cases the meaning is the same: our ordinary life is nothing more than an empty image of life. Barnes gives the social observation: the understanding becomes darkened by indulgence in sin, a well-known fact seen as much in the present as in Paul's day; a man who yields habitually to any sin finds his moral perceptions becoming confused. Wesley states the sequence with precision: having their understanding darkened through ignorance, so that they are totally void of the light of God, being alienated from the divine and spiritual life through the hardness of heart that is both cause and effect of the alienation. Ellicott notes that Paul dwells with intense emphasis on the moral rather than the intellectual dimension of this darkness.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>Our ordinary life, as men, is nothing more than an empty image of life, not only because it quickly passes, but also because, while we live, our souls, not keeping close to God, are dead. The understanding becomes darkened through the ignoring of God, and from this darkened understanding flow all the moral corruptions Paul is about to describe.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>The understanding becomes darkened by indulgence in sin; a fact seen now as well as then. A man who yields habitually to any sin finds his moral perceptions becoming confused and ultimately destroyed. The darkness of the Gentiles was not merely intellectual but moral; it was the darkness of alienation from the life of God.</p>"},
{"src": "ellicott", "attr": "Ellicott", "html": "<p>The phrase the life of God is unique. It may be interpreted as the life given by God, the life eternal of John 17:3. St. Paul, passing lightly over the intellectual loss, dwells on the moral with intense and terrible emphasis: they have lost the capacity of moral pain, the natural and healthful consequence of sin against our true natures.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"19": {
"synthesis": "<p>Being past feeling, they gave themselves over to lasciviousness, to work all uncleanness with greediness. Calvin describes the worst of all evils: having destroyed the sensibilities of the heart and allayed the stings of remorse, they abandon themselves to all manner of iniquity, giving loose reins to self-indulgence. Ellicott observes that Paul dwells on the moral loss with intensity: the Greek <em>apelgekotes</em> means literally having lost the capacity for pain — the moral pain that is the natural and healthful consequence of sin. Clarke notes that the verb signifies, first, throwing off all sense of shame and being utterly devoid of pain for committing unrighteous acts; second, being desperate, without hope or desire of reformation; in a word, without remorse and utterly regardless of character or final blessedness. Barnes describes the total want of all emotion on moral subjects as an accurate description of the state of a hardened sinner: he often gives an intellectual assent to truth but without emotion of any kind, the heart insensible as the hard rock. Wesley adds that pain urges the sick to seek a remedy; where there is no pain, remedy is not sought.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>The account which had been given of natural depravity is followed by a description of the worst of all evils, brought upon men by their own sinful conduct. Having destroyed the sensibilities of the heart and allayed the stings of remorse, they abandon themselves to all manner of iniquity and give loose reins to self-indulgence.</p>"},
{"src": "ellicott", "attr": "Ellicott", "html": "<p>They have lost the capacity of pain, the moral pain which is the natural and healthful consequence of sin against our true natures. Consequently, losing in this their true humanity, they give themselves over to lasciviousness, to work all uncleanness with greediness, trading in all uncleanness as a business.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>Being past feeling: wholly hardened in sin, a total want of all emotion on moral subjects. An accurate description of the state of a sinner: he often gives an intellectual assent to the truth, but it is without emotion of any kind; the heart is insensible as the hard rock. They have given themselves over voluntarily.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"20": {
"synthesis": "<p>But you did not so learn Christ. Calvin draws the contrast sharply: the Gentiles walk in darkness and cannot distinguish right from wrong, but those on whom the truth of God shines ought to live differently. To <em>learn Christ</em> is a phrase used nowhere else in Paul, but Ellicott notes it is easily interpreted by the commoner phrase <em>to know Christ</em>, and that the emphasis on <em>the Christ</em> here distinguishes the Messiah from the merely human teacher, in opposition to what the heathen had learned from their philosophers. Barnes is precise: you have been taught a different thing by Christ; you have been taught that his religion requires you to abandon such a course of life. Wesley reduces it to a single sentence: ye have received the doctrines of Christianity and are taught differently; ye have received the Spirit of Christ and are therefore saved from such dispositions. Robertson notes the sharp contrast with pagan life using <em>outos</em> (so): ye did not so learn the Christ.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>He now draws a contrast of a Christian life, making it evident how utterly inconsistent it is with the character of a godly man to defile himself with the abominations of the Gentiles. Because the Gentiles walk in darkness they do not distinguish between right and wrong; but those on whom the truth of God shines ought to live in a different manner.</p>"},
{"src": "ellicott", "attr": "Ellicott", "html": "<p>To learn Christ is a phrase not used elsewhere; but easily interpreted by the commoner phrase to know Christ. The name the Christ is here used emphatically in distinction from the merely human teacher, in opposition to the heathen philosophical teachers from whom the pagan world had learned its way of life.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>You have been taught a different thing by Christ; you have been taught that his religion requires you to abandon such a course of life. The religion of Christ demands a total change from the manner of living which Paul has been describing in the preceding verses.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"21": {
"synthesis": "<p>The appeal turns to what they have heard and been taught, with the truth as it is in Jesus as the governing standard. Calvin notes the reproof implicit in this appeal: it corrects that superficial knowledge of the gospel by which many are elated while wholly unacquainted with newness of life, thinking themselves wise while having no actual transformation. Ellicott observes that the rhetorical <em>if so be that</em> is the same particle used in Ephesians 3:2 and Colossians 1:23, indicating no real doubt but strong affirmation: he has heard; he has been taught in him; he knows the truth that is in Jesus. Barnes notes the possible delicate doubt implied as to whether they had attentively listened to his instructions, though Doddridge renders it as <em>seeing ye have heard him</em>. Robertson points to the Gnostic context: Paul identifies the Christ of verse 20 with Jesus of this verse, flatly affirming that there is truth in Jesus in direct opposition to the Cerinthian distinction between the man Jesus and the aeon Christ.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>To excite their earnestness the more, he not only tells them that they had heard Christ, but employs a still stronger expression, as if to say that this doctrine had not been slightly pointed out but faithfully delivered and explained. This contains a reproof of that superficial knowledge of the gospel by which many are elated, wholly unacquainted with newness of life.</p>"},
{"src": "ellicott", "attr": "Ellicott", "html": "<p>If so be that indicates no real doubt but only that rhetorical doubt which is strong affirmation. Ye heard him and were taught in him: Paul begins with the first means of knowledge, the hearing his voice directly or through his ministers, and proceeds to describe the fuller immersion in Christ as the sphere and atmosphere of all teaching.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>If indeed: condition of first class with aorist indicatives, assumed to be true. Paul here identifies Christ of verse 20 and Jesus of this verse, flatly affirming that there is truth in Jesus in direct opposition to the Cerinthian Gnostics who distinguished between the man Jesus and the aeon Christ.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"22": {
"synthesis": "<p>The content of the truth as it is in Jesus is the putting off of the old man, which is corrupt according to the deceitful lusts. Calvin explains that Paul demands from the Christian man repentance, or a new life, which consists of self-denial and the regeneration of the Holy Spirit. The old man means the natural disposition of man, what we were by nature before being renewed by the Spirit. Ellicott clarifies that the old man is to be put off in relation to the corruption of the true humanity, not in relation to the true humanity itself, and that the phrase <em>which is being marred</em> is a present participle indicating ongoing corruption getting progressively worse. Barnes notes the striking feature: it is possible there had been teachers among them who had not enforced the duties of practical religion as they should have, which explains Paul's emphasis here. Wesley is succinct: the old man is the whole body of sin; all sinful desires are deceitful, promising the happiness they cannot give.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>He demands from a Christian man repentance, or a new life, which he makes to consist of self-denial and the regeneration of the Holy Spirit. The old man, as we have repeatedly stated in expounding Romans 6, means the natural disposition of man — what we were before being renewed by the Spirit of God.</p>"},
{"src": "ellicott", "attr": "Ellicott", "html": "<p>The old man is to be put off as far as concerns the corruption of the true humanity, not in relation to the true humanity itself. The phrase which is being marred shows an ongoing process of corruption: the old man is not merely old but is getting worse and worse, decaying more and more completely.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>That ye lay aside the old man, renounce it: the former mode of life described as the old man. Your whole former life was corrupt and abominable; you lived in the pursuit of pleasure and happiness, sought it in the gratification of the lusts of the flesh, and were entirely in the power of sin and the devil.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"23": {
"synthesis": "<p>Be renewed in the spirit of your mind. Calvin identifies the spirit of the mind as the mind itself considered in its highest part — not only the inferior appetites or desires manifestly sinful, but that part of the soul most noble and excellent, which must also be renewed. Barnes notes that the Greek word <em>ananeoo</em> means to make new or young again, and the renewal is in the spirit of the mind, pointing to the innermost faculty of the soul as the seat of transformation. Clarke states the comprehensive scope: not merely the general complexion of the mind but its very spirit, all its faculties and powers, must be thoroughly, completely, and universally renewed. Ellicott observes that <em>spirit</em> here is not the Holy Spirit but the human spirit, the mind or inner man considered in its true relation to God; and the process of being made young again contrasts with the decrepitude of the old man, which is growing more corrupt.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>I understand the spirit of the mind to mean not only the inferior appetites or desires which are manifestly sinful, but also that part of the soul most noble and excellent. And here again Paul brings forward that queen which philosophers are accustomed almost to worship, as if no fault attached to it, and subjects it too to renewal.</p>"},
{"src": "ellicott", "attr": "Ellicott", "html": "<p>The word translated renewed means properly to be made young again, and the process of recovery is described as the natural effect of putting off the decrepitude of the old man. The spirit of the mind is the spiritual nature of the inner man; the human spirit, the mind considered in its true relation to God.</p>"},
{"src": "clarke", "attr": "Clarke", "html": "<p>And be renewed in the spirit of your mind: the mind is to be renovated, and not only its general complexion but the very spirit of it, all its faculties and powers must be thoroughly, completely, and universally renewed. Not only the outward conduct but the inward principle from which all conduct flows must be transformed.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"24": {
"synthesis": "<p>And put on the new man, created according to God in true righteousness and holiness. Calvin states the essential point: the metaphor of putting on the new man indicates that this is an act received, not achieved; the new man is God's creation, not man's manufacture. Adam was at first created after the image of God, reflecting divine righteousness, but that image has been corrupted and can only be restored by grace in Christ. Ellicott extends the thought: to put on the new man is to put on the Lord Jesus Christ, as the beginning in Galatians 3:27, the continuation in Romans 13:14, and the completion in 1 John 3:2. Barnes explains the change so completely that there is no impropriety in speaking of the one who has experienced it as a new man with new feelings, principles, and desires. Wesley makes it simple: the new man is universal holiness, created after the very image of God. Robertson identifies <em>ton kainon anthropon</em> as the brand-new man and notes that <em>kata theon</em> — after the pattern God — is the goal: the new birth aimed at conformity to God, ultimately like God in the end.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>Adam was at first created after the image of God and reflected, as in a mirror, divine righteousness; but that image has been effaced and is now corrupted. What is here said about the new creation refers to the second creation effected by the grace of Christ: we must receive it, not manufacture it.</p>"},
{"src": "ellicott", "attr": "Ellicott", "html": "<p>To put on the new man is to put on the Lord Jesus Christ, by that divine process of which we have the beginning in Galatians 3:27, the continuation in Romans 13:14, and the completion in 1 John 3:2. In the new man is implied not merely youthfulness but the freshness of a higher nature.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>The new man refers to the renovated nature; called in other places the new creature or the new creation, 2 Corinthians 5:17. The change is so great that there is no impropriety in speaking of one who has experienced it as a new man. He has new feelings, principles, and desires. He has laid aside his old principles and practices and commenced a new life.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"25": {
"synthesis": "<p>From the principle of the new man, all practical exhortations flow like streams from a fountain. The first specific command is to put away lying and speak truth, each one with his neighbor. Calvin notes that from the righteousness of the new man all godly exhortations derive their root and rationale; without this principle, moral rules are of little value, since philosophy can describe virtues but only the new creation can produce them. Ellicott offers a specific reason for truth as the first command: truth is the first condition of mutual confidence, which is the basis of all unity; and since we are members of one another in the body of Christ, deception is self-wounding. Barnes reminds readers that lying was the universal vice of the heathen world: among ancient pagans it was almost universally practised, and the Christian converts had been long addicted to it. Wesley adds the theological grounding: since they are created anew, they are to walk accordingly; deceit is quite repugnant to the intimate union of membership in one another.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>From this head of doctrine, that is, from the righteousness of the new man, all godly exhortations flow like streams from a fountain. Philosophers take a different method, but in the doctrine of godliness there is no other way than this for regulating the life. He comes now to lay down particular exhortations.</p>"},
{"src": "ellicott", "attr": "Ellicott", "html": "<p>Truth is the first condition of mutual confidence which is the basis of all unity. Hence it is the first duty of that membership one of another which follows from our being one body in Christ. No doubt it is also the first duty to our own humanity and to the God who hateth a lie; but here the appeal is to the body and its unity.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>Lying is the universal vice of the heathen world. Among the ancient heathen, as among the moderns, it was almost universally practised. The Christian converts at Ephesus had been long addicted to it; hence the necessity of special caution on that head. The new man, created in true righteousness and holiness, cannot indulge in a vice so directly opposed to its nature.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"26": {
"synthesis": "<p>Be angry and sin not; let not the sun go down on your wrath. Calvin notes the quotation from Psalm 4:4 and the ambiguity of the Hebrew, which can mean either <em>tremble</em> or <em>be agitated by anger</em>. The key question is whether this is a command to be angry or a permission, and whether anger itself is sinful. Ellicott is clear: anger is not sin, since our Lord himself felt it at the hardness of men's hearts, and it performs a legitimate function as the resentment of righteous indignation. Barnes agrees that anger may exist without sin, but there is special danger in all cases where anger exists that it will be accompanied with sin. Robertson calls this a permissive imperative, not a command to be angry, with the prohibition against sinning as the real point; the settled mood of anger in <em>paroorgismo</em> is the danger. Wesley and Clarke both make the pastoral point: if you are angry at the person as well as the fault, you sin; reprove your brother and be reconciled immediately — lose not one day.</p>",
"voices": [
{"src": "ellicott", "attr": "Ellicott", "html": "<p>Anger itself is not sin, for our Lord himself felt it at the hardness of men's hearts, and it is again and again attributed to God himself in language of human accommodation. In the form of resentment, and above all of righteous indignation, it performs an important function in maintaining moral order.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>It is implied here that there may be anger without sin, and that there is special danger, in all cases where there is anger, that it will be accompanied with sin. Anger is a passion too common to require definition and too dangerous to be indulged without the most careful guard lest it proceed too far.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>Be ye angry and sin not: permissive imperative, not a command to be angry. Prohibition against sinning as the peril in anger. Quotation from Psalm 4:4. Let not the sun go down upon your wrath: danger in settled mood of anger. <em>Paroorgismos</em>, provocation, from <em>paroorgizo</em>, to exasperate to anger, occurs only in LXX and here in the New Testament.</p>"}
],
"consensus": "mixed",
"key_tension": "Commentators agree anger is not inherently sinful (citing Christ's anger), but divide on whether the imperative is a command (be rightly angry) or a permission with immediate restriction (if angry, do not sin)."
},
"27": {
"synthesis": "<p>Neither give place to the devil. Calvin has no doubt that Paul's intention is to guard believers against allowing Satan to take possession of their minds, since Scripture uniformly uses this word for the adversary. Barnes applies this specifically to the exhortation of the previous verse: do not yield to the suggestions and temptations of Satan, who would take every opportunity to persuade you to cherish unkind and angry feelings. The heart is deceitful, and seldom more so than when we suppose we are merely defending our rights; many feelings about claiming what is ours are actually produced by the temptations of the devil. Clarke allows an alternative reading: since the word <em>diabolos</em> is sometimes used for a calumniator or tale-bearer, the command may mean do not open your ear to the tale-bearer who whispers accusations and inflames anger. Ellicott notes that the name <em>devil</em> appears in Paul only in his later epistles, while the earlier ones use <em>Satan</em>. Robertson offers the practical rule: present active imperative in prohibition — either stop doing it or do not have the habit.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>I have no doubt Paul's intention was to guard us against allowing Satan to take possession of our minds and, by keeping in his hands this citadel, to do whatever he pleases. We feel every day how impossible, or at least how difficult, it is to be angry and not to sin; and the difficulty arises from this, that Satan holds his seat in our anger.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>This has respect probably to the exhortation in the former verse. Do not yield to the suggestions and temptations of Satan, who would take every opportunity to persuade you to cherish unkind and angry feelings. Many feelings, when we suppose we are merely defending our rights, are produced by the temptations of the devil.</p>"},
{"src": "clarke", "attr": "Clarke", "html": "<p>Your adversary will strive to influence your mind and irritate your spirit; watch and pray that he may not get any place in you or ascendancy over you. As <em>diabolos</em> is sometimes used to signify a calumniator or backbiter, it may here mean: do not open your ear to the tale-bearer who uses your anger for his own wicked purposes.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"28": {
"synthesis": "<p>Let him who stole steal no more; rather let him labor, working with his own hands what is good, so that he may have to give to him who has need. Calvin notes that the prohibition extends beyond the grosser thefts punished by human laws to the more concealed forms of depredation by which we seize what belongs to others; and not merely does Paul forbid unjust taking, he enjoins active assistance to brethren. Barnes explains the social context: theft was almost a universal vice among the heathen, and the Christian converts at Ephesus had been long addicted to it, making special caution necessary. Clarke notes that the apostle here teaches a doctrine different from rabbinic permissiveness toward stealing if a portion was given to the poor; under the Christian system nothing contrary to truth and righteousness could be tolerated. Wesley focuses on the positive command: let him labour so that idleness does not lead him to steal again, and let him earn in order to give, becoming a blessing rather than a burden to his neighbors. Robertson is crisp: clearly here, cease stealing, and even unemployment is no excuse for stealing.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>This includes not merely the grosser thefts punished by human laws but those of a more concealed nature. He does not simply forbid taking property in an unjust manner; he enjoins active assistance to brethren. Thou who formerly stole must now not only obtain thy subsistence honestly, but must thine own necessities being supplied, have enough to assist others.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>Theft was almost a universal vice among the heathen. The Christian converts at Ephesus had been long addicted to it; hence the necessity of special caution on that head. Christianity requires not only that we do not steal but that we engage in honest industry, and that we give to those who are in need from the fruits of our own labor.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>Steal no more: clearly here, cease stealing, present active imperative with <em>meketi</em>. The good thing as opposed to his stealing, with his hands that did the stealing. To share with one: present active infinitive of <em>metadidoomi</em>. Even unemployment is no excuse for stealing; labor so as to be able to give.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"29": {
"synthesis": "<p>Let no corrupt communication proceed from your mouth, but only what is good for building up, as befits the need, that it may give grace to those who hear. Calvin first forbids all language used for inflaming lust, then enjoins speech framed for edification. Barnes explains the word <em>sapros</em> — corrupt, rotten — as applied to putrid vegetables or animal substances, used metaphorically to denote depraved, evil, contaminating speech. Clarke provides extensive lexical support, noting that <em>logos sapros</em> means useless, putrid, unsavory, and obscene words, and that calumnious or reproachful speech of every kind falls under this prohibition. Wesley states the practical principle: only speech that is profitable to speaker and hearers, forwarding them in repentance, faith, or holiness, so that it becomes a means of conveying more grace into their hearts; hence all speech that is not profitable, not edifying, and not apt to minister grace to the hearers is corrupt as if stinking in God's nostrils. Robertson notes the contrast: <em>sapros</em> is rotten, putrid, like rotten fruit, here the opposite of <em>agathos</em>, good.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>He first forbids believers to use any language employed for the purpose of inflaming lust. Not satisfied with the removal of the vice, he enjoins them to frame their discourse for edification. The genitive may no doubt be variously translated, but the meaning is speech that is useful or profitable, that which may contribute to the good of our neighbors.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>The word rendered corrupt means bad, decayed, rotten; applied to putrid vegetables or animal substances; then used in a moral sense to denote that which is depraved, evil, contaminating. Of this character is all impure language; all profaneness; all obscenity; all language that tends to inflame passion or that corrupts the mind.</p>"},
{"src": "wesley", "attr": "Wesley", "html": "<p>But that which is good, profitable to the speaker and hearers, to the use of edifying, to forward them in repentance, faith, or holiness, that it may minister grace to the hearers, being a means of conveying more grace into their hearts. All speech that is not profitable, not edifying, not apt to minister grace, is corrupt as stinking in God's nostrils.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"30": {
"synthesis": "<p>And grieve not the Holy Spirit of God, by whom you were sealed for the day of redemption. This verse, as Ellicott and Calvin both note, refers to all the practical commands given above, since the four cardinal sins forbidden — falsehood, wrath-holding, theft, corrupt speech — are all regarded as grieving the Holy Spirit who indwells believers. Calvin draws the implication: as the Holy Spirit dwells in us, every part of soul and body ought to be devoted to him; and if we give ourselves up to anything impure, we drive him from making his abode with us. Ellicott observes that the expression <em>grieving the Holy Spirit</em> implies a personal relation to a Divine Person capable of grief, which is stronger than <em>quenching the Spirit</em> in 1 Thessalonians 5:19 or <em>resisting the Holy Ghost</em> in Acts 7:51. Barnes addresses this to Christians specifically, proving that it is possible for believers to grieve the Spirit; the word means to afflict with sorrow, to make sad or sorrowful. Robertson makes the tense precise: cease grieving, or do not have the habit of grieving; and adds the personal note, who of us has not sometimes grieved the Holy Spirit?</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>As the Holy Spirit dwells in us, to him every part of our soul and body ought to be devoted. But if we give ourselves up to anything that is impure, we may be said to drive him away from making his abode with us; and, to express this still more familiarly, human affections such as joy and grief are ascribed to the Holy Spirit.</p>"},
{"src": "ellicott", "attr": "Ellicott", "html": "<p>This verse refers to all the practical commands given above. In the expression grieve the Holy Spirit, even more than in the cognate expressions of quenching the Spirit or resisting the Holy Ghost, there is implied a personal relation to a Divine Person capable of being grieved by our transgressions as sins against his perfect holiness.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>Grieve not the Holy Spirit of God: cease grieving, or do not have the habit of grieving. Who of us has not sometimes grieved the Holy Spirit? In whom ye were sealed: not in which. The day when final redemption is realized is the day of redemption toward which the sealing points.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"31": {
"synthesis": "<p>Let all bitterness, wrath, anger, clamor, and evil speaking be put away from you, with all malice. Calvin distinguishes the terms with care: between <em>thumos</em> and <em>orge</em> there is little difference except that the former denotes the power and the latter the act of anger; clamor is the noisy disputes and reproaches that accompany it; and malice is the root behind all of them. Ellicott notes that bitterness or sharpness is an acerbity of temper that shows itself in words and in the general tone of behavior, the first symptom of the forbidden temper; it proceeds through wrath and anger to clamor and evil speaking, each stage intensifying the one before. Barnes insists that Christians are to be calm and serious; harsh contentions and strifes, hoarse brawls and tumults, are to be unknown among them. Wesley gives a vivid pastoral rebuke: <em>I am not angry, but it is my way to speak so</em> — well, then unlearn that way; it is the way to hell. Clarke observes the astonishment that any professing the Christian name should indulge bitterness of spirit, and identifies the censorious as the prime offenders.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>Between wrath and anger there is little difference except that the former denotes the power and the latter the act; but here the only difference is that wrath is a more sudden attack. He again condemns anger, but on this occasion views it in connection with those offenses by which it is usually accompanied: noisy disputes, reproaches, and the malice that is the root of all.</p>"},
{"src": "ellicott", "attr": "Ellicott", "html": "<p>The first symptom of the temper forbidden is bitterness or sharpness, an acerbity of temper that shows itself in the general tone of character and speech. It proceeds through wrath and anger to clamor, the loud, violent speaking of excited contention, and on to evil speaking and malice, each stage intensifying the one before.</p>"},
{"src": "wesley", "attr": "Wesley", "html": "<p>Let all bitterness, the height of settled anger, and wrath, lasting displeasure, and anger, the very first risings of disgust at those that injure you, and clamour, or bawling — I am not angry, says one, but it is my way to speak so: then unlearn that way, it is the way to hell — and evil speaking be put away with all malice.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"32": {
"synthesis": "<p>Be kind to one another, tenderhearted, forgiving one another as God in Christ forgave you. Calvin shows how kindness and tenderness complete the removal of bitterness: with kindness he contrasts gentleness of countenance, language, and manners; and as this virtue will never reign unless attended by sympathy, he recommends sympathy that not only shares in the distresses of brethren but is affected by everything that happens to them as if we were in their situation. Ellicott provides lexical precision: <em>kindness</em> is gentleness in bearing with wrong, while <em>tenderheartedness</em> is the more positive warmth of sympathy and love, both issuing in the free forgiveness of God in Christ as their model. Barnes finds in Christianity the true secret of politeness: not roughness, crabbedness, or sourness, but benevolence, the desire to make others happy. Wesley reduces the whole to its theological ground: as God, showing himself kind and tenderhearted in the highest degree, hath forgiven you. Robertson draws on Colossians 3:12 for the parallel: keep on becoming kind toward one another, present middle imperative conveying ongoing habitual practice.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>With bitterness he contrasts gentleness of countenance, language, and manners. As this virtue will never reign unless attended by sympathy, he recommends that we be tenderhearted: not only to sympathize with the distresses of brethren as if they were our own, but to cultivate that true humanity which is affected by everything that happens to them as if we were in their situation.</p>"},
{"src": "ellicott", "attr": "Ellicott", "html": "<p>Kindness is gentleness in bearing with wrong; tenderheartedness is the more positive warmth of sympathy and love. Both issue in free forgiveness, after the model of the universal and unfailing forgiveness of God in Christ to us — the only model we dare to follow, suggested by our Saviour himself in the Lord's Prayer.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>Christianity produces true courteousness or politeness. It does not make one rough, crabbed, or sour; nor does it dispose its followers to violate the proper rules of social intercourse. The secret of true politeness is benevolence, or a desire to make others happy; and a Christian should be the most polite of men.</p>"}
],
"consensus": "affirm",
"key_tension": null
}
}
}
''')


def main():
    existing = load_synthesis('ephesians')
    merge_synthesis(existing, EPHESIANS)
    save_synthesis('ephesians', existing)

    total = sum(len(v) for v in EPHESIANS.values())
    print(f'Ephesians 4 synthesis complete: {total} verses written.')

    print('\nVerification checks:')
    import json as _json
    data = _json.loads((ROOT / 'data' / 'commentary' / 'synthesis' / 'ephesians.json').read_text())
    il = _json.loads((ROOT / 'data' / 'interlinear' / 'ephesians.json').read_text())
    for ch, expected in [('4', 32)]:
        if ch in data:
            count = len(data[ch])
            il_count = len(il.get(ch, {}))
            print(f'  ch{ch}: {count} verses in synthesis, {il_count} in interlinear (expected {expected})')
        else:
            print(f'  ch{ch}: MISSING from output file')

    print('\nVoice word counts (flagging < 35 words):')
    import re
    for ch in ['4']:
        for v in sorted(EPHESIANS[ch].keys(), key=int):
            for voice in EPHESIANS[ch][v]['voices']:
                words = len(re.findall(r'\w+', voice['html']))
                if words < 35:
                    print(f'  WARN: ch{ch}v{v} {voice["src"]}: {words} words')
    print('Done.')


if __name__ == '__main__':
    main()
