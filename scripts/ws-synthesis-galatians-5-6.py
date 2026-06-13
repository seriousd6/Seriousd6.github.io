"""
Wide Source Synthesis - Galatians chapters 5-6
bookId: galatians
Run: python3 scripts/ws-synthesis-galatians-5-6.py
Sources used: calvin, ellicott, clarke, wesley, barnes, rwp
Not used: mhcc (not found for Galatians), jfb (data corrupt - contains Romans 9-11 content)
Key synthesis decisions:
  - v20 (ch5): Calvin missing; coverage from ellicott, clarke, wesley, barnes
  - v23 (ch5): RWP missing; coverage from calvin, ellicott, clarke, wesley, barnes
  - v5 (ch6): Wesley missing; coverage from calvin, ellicott, clarke, barnes, rwp
  - v4 (ch6): RWP missing; coverage from calvin, ellicott, clarke, wesley, barnes
  - v12 (ch6): consensus=mixed - interpreters differ on meaning of large letters (eyesight vs emphasis)
  - v16 (ch6): consensus=mixed - Israel of God disputed (ethnic believers vs all believers)
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

GALATIANS = json.loads(r'''
{
"5": {
"1": {
"synthesis": "<p>The chapter opens with Paul's imperative to stand firm in the freedom Christ has purchased. Calvin frames this as an invaluable blessing worth defending even to death: not merely a temporal benefit but an eternal one, since the spiritual life itself is at stake. Ellicott notes a textual variant in the best manuscripts reading <em>with freedom Christ made us free</em>, making liberty both the instrument and purpose of his liberating act. Barnes emphasizes that this is freedom from Jewish rites and ceremonies, while Wesley specifies freedom from the ceremonial law's burden. Robertson underscores the perfect stem of <em>stekete</em>: keep on standing, stay free since Christ set you free. Clarke reads the yoke as the entire Mosaic economy imposed on Gentiles. The command is not passive; it requires active resistance against re-entanglement. Paul does not call believers to avoid bondage but to maintain a freedom already granted. All agree that Christian liberty is not license but liberation for a higher life under the Spirit.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>It is an invaluable blessing, in defense of which it is our duty to fight, even to death; since not only the highest temporal considerations, but our eternal interests also, animate us to the contest. The apostle now reminds them that they ought not lightly to despise a freedom so precious.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p><em>Stand fast therefore</em> uses the perfect stem of <em>histemi</em>: keep on standing therefore, stay free since Christ set you free. The dative case in <em>te eleutheria</em> reads <em>for freedom</em>, for the freedom that belongs to us as children of the freewoman.</p>"},
{"src": "wesley", "attr": "Wesley", "html": "<p>Stand fast in the liberty from the ceremonial law wherewith Christ hath made us all believers free; and be not entangled again with the yoke of legal bondage which has no power to justify but only to burden.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"2": {
"synthesis": "<p>Paul asserts his full apostolic authority to declare that circumcision sought as a means of justification nullifies one's relationship with Christ. Ellicott observes the strong personality of the apostle here, speaking with dogmatic authority as though his bare word were sufficient. Calvin puzzles over whether Timothy's circumcision offers a counterexample and resolves it by insisting Paul's argument concerns circumcision as a condition of justification, not circumcision as such. Barnes carefully distinguishes: Paul himself was circumcised but not to be justified thereby, and that distinction is decisive. Wesley is blunt: seeking justification by circumcision means disclaiming Christ and all his blessings. Robertson notes the present passive subjunctive as a supposable case with terrible consequences, for it would make circumcision a condition of salvation and thus render Christ useless. The apostolic ego of verse 2 carries the full weight of Paul's founding authority over these churches, making the declaration all the more urgent.</p>",
"voices": [
{"src": "ellicott", "attr": "Ellicott", "html": "<p>The strong personality of the Apostle asserts itself; instead of going into an elaborate proof, he speaks with dogmatic authority, as though his bare word were enough. He says that if this state of being received into divine favour is sought through circumcision, Christ will profit nothing.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>I, who at first preached the gospel to you; I, too, who have been circumcised, and who was formerly a strenuous asserter of the necessity of observing the laws of Moses, now solemnly say to you that if you are circumcised with a view to being justified by that, it amounts to a rejection of justification by Christ.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>Condition of third class and present passive subjunctive: a supposable case, but with terrible consequences, for they will make circumcision a condition of salvation. In that case Christ will help them not at all.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"3": {
"synthesis": "<p>Whoever accepts circumcision as part of the salvific system incurs obligation to keep the entire Mosaic code. Calvin cites Grotius to sharpen the logic: if Judaism is the road to salvation, the whole of Judaism must be observed; you cannot cull and discard whatever portions seem inconvenient. Since no one will ever satisfy the law completely, circumcision as a means of justification leads only to perpetual condemnation. Barnes notes that circumcision was the distinguishing badge of the Jews, and accepting it committed one to the whole legal system in the same way baptism commits one to Christ. Clarke emphasizes the impossibility of partial compliance: the system is indivisible. Robertson is terse but precise, observing that the debtor has assumed an obligation and thereby takes the curse upon himself. Wesley addresses it directly to Gentile hearers: he thereby makes himself a debtor and obliges himself to the whole law which no flesh can satisfy.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin (quoting Grotius)", "html": "<p>If Judaism is the road to salvation, the whole of Judaism must be observed; you must not cull and throw away whatever part of it you think fit. He will never escape death, but will always continue to be held as guilty, for no man will ever be found who satisfies the law.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>He binds himself to obey all the law of Moses. Circumcision was the distinguishing badge of the Jews, as baptism is of Christians. A man who was circumcised was, by that act, committed to the whole Jewish system of religion and could not pick and choose among its requirements.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p><em>Opheiletes</em>: a common word for one who has assumed an obligation. See on Matthew 6:12, Galatians 3:10. He takes the curse upon himself by binding himself to a system no one can fully satisfy.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"4": {
"synthesis": "<p>Paul's verdict on those who seek justification through the law is stark: Christ is become of no effect to you, and you have fallen from grace. The Galatians were not, as Calvin observes, so grossly mistaken as to believe the law alone justified them; they attempted to mix Christ with the law. But any dilution of grace with merit cuts off the channel through which grace flows. Ellicott renders it as <em>ye did fall out of grace</em>, a decisive completed action. Barnes explains that the Greek verb <em>katargeo</em> means to render inactive, idle, useless, treating Christ's work as needless and vain. Wesley frames it as renouncing the new covenant and disclaiming the benefit of the gracious dispensation. Robertson notes the second aorist active indicative of <em>ekpipto</em> with the ablative: they fell out from grace as from a vessel they once inhabited. The combination of being severed from Christ and having fallen from grace is total spiritual displacement.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>They were not so grossly mistaken as to believe that by the observance of the law alone they were justified, but attempted to mix Christ with the law. What are you doing? You deprive yourselves of every advantage from Christ, and treat his grace as if it were of no value.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>You will derive no advantage from Christ. His work in regard to you is needless and vain. If you can be justified in any other way than by him, then of course you do not need him, and your adoption of the other mode is, in fact, a renunciation of him.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p><em>Kataergeo</em>: first aorist passive, to make null and void. <em>Ye are fallen away from grace</em>: second aorist active of <em>ekpipto</em> with ablative case. Ye did fall out of grace, ye left the grace-sphere where you once lived.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"5": {
"synthesis": "<p>In deliberate contrast to those who seek righteousness through the law, Paul describes the Christian's true posture: we wait by the Spirit through faith for the hope of righteousness. Calvin explains that righteousness depends on faith alone, obtained through the Spirit without ceremonies. Barnes stresses that true Christians have no other hope of salvation than by faith in the Lord Jesus; this is not passive waiting for a delayed event but expectant confidence in the only means of justification. Wesley identifies the recipients as those under the gospel dispensation, who receive righteousness from God through faith and by faith will obtain the full reward. Robertson's compressed comment strikes at the contrast: we Christians as opposed to the legalists; by the Spirit out of faith, not law. Clear-cut repetition to make it plain. The phrase <em>hope of righteousness</em> captures both the present reality of justification by faith and its eschatological completion.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>Righteousness depends on faith, and is obtained, through the Spirit, without ceremonies. To wait for righteousness is to place our confidence in this or that object, to decide from what quarter righteousness is to be expected; and the words contain the exhortation, let us continue steadfastly in the hope of righteousness which God promises.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>We expect salvation only by the aid of the Holy Spirit. The main idea is not that of waiting as if the thing were delayed; it is that of expecting. True Christians have no other hope of salvation than by faith in the Lord Jesus, not by works or conformity to the law.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>We Christians as opposed to the legalists. By the Spirit, the Holy Spirit, out of faith, not law. Clear-cut repetition to make it plain that Spirit and faith stand over against law and circumcision.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"6": {
"synthesis": "<p>In Christ Jesus neither circumcision nor uncircumcision avails anything; only faith working through love. Calvin explains that circumcision and its appendages are abolished in the kingdom of Christ, the rite no longer possessing influence. Yet he insists this does not mean ceremonies were always useless, only that their day is past. Barnes sees the design of Christianity as abolishing rites that divided humanity and introducing a way of salvation applicable to all mankind alike. Wesley is precise: neither the most punctual observance of the law nor the most exact heathen morality avails anything; only faith alone, and that specifically a faith that works by love, covering all inward and outward holiness. Robertson calls faith working through love the moral dynamic of Paul's conception of freedom from law. Clarke notes that all distinctions of race and ritual dissolve before the one decisive question: has the Spirit of Christ been received by faith that expresses itself in love?</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>In the kingdom of Christ, circumcision with its appendages is abolished; faith depends on the Spirit and not on ceremonies. While declaring they no longer possess any influence, Paul does not admit that they were always useless; for he does not condemn them in all ages, but only in the present time.</p>"},
{"src": "wesley", "attr": "Wesley", "html": "<p>In Christ Jesus neither circumcision with the most punctual observance of the law, nor uncircumcision with the most exact heathen morality, availeth anything toward justification or salvation. But faith alone; even that faith which worketh by love, all inward and outward holiness.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>Neither Jew nor Greek has any recommendation in his state. All stand on a level in Christ. Faith working through love: the middle voice of <em>energeo</em>, through love as the moral dynamic of Paul's conception of freedom from law.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"7": {
"synthesis": "<p>Paul uses the athletic metaphor of a race interrupted. They ran well; someone cut in on them. Calvin notes that the censure is mingled with approbation of their former course, designed to produce shame and thereby speed their return to the right path. Barnes recalls the context of the Greek Olympic games; the word for hindrance means to beat or drive back, or to obstruct someone running. Wesley is brief: who hath hindered you that ye should not still obey the truth? Robertson provides a vivid modern analogy: the Greek verb is like someone cutting in on your telephone call, a ringleader who cut across the Galatians' course as they were running the Christian race and tried to trip them or turn them. Ellicott and Clarke both observe the implied rebuke: the Galatians once ran faithfully under Paul's gospel and the departure from that course has an external cause, a seducer, not an internal one.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>The censure which the apostle administers for their present departure from the truth is mingled with approbation of their former course, for the express purpose that, by being brought to a sense of shame, they may return more speedily to the right path. The astonishment conveyed in the question was intended to produce a blush.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>The Christian life is often represented as a race. Paul means here that they began the Christian life with ardour and zeal. The word used means, properly, to beat or drive back; an Olympic expression for coming across the course while a person is running, checking and retarding them.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>Who did hinder you: first aorist active of <em>enkoptoo</em>, to cut in on one, for all the world like our use of one cutting in on us at the telephone. Note the singular <em>tis</em>. There was some ringleader who cut in on the Galatians as they were running the Christian race.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"8": {
"synthesis": "<p>The persuasion drawing the Galatians toward the law did not come from God who called them. Calvin argues that Paul's authority as the one who first announced their divine calling gives him standing to make this bold claim. Barnes emphasizes that the Galatians knew Paul had not persuaded them toward Judaizing, so the important demonstration is that such persuasion cannot be traced to God, however its teachers may claim divine sanction. Wesley reduces it to a single point: this persuasion cometh not from God who called you to his kingdom and glory. Robertson defines the rare word <em>peismone</em> as the art of persuasion, the effort of the Judaizers to persuade you, found only here and in later ecclesiastical writers. Clarke and Ellicott note the contrast between the caller and the persuader: God called them to freedom; whoever persuades them back toward the law acts against God's calling.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>Paul, to whom the Galatians had been indebted for the announcement of their Divine calling, was well entitled to address them in this confident language. He does not directly name its source, but pronounces that their present persuasion came not from God, though those who taught it may claim divine authority.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>This refers to God who had called them into his kingdom. That it refers to God, and not to Paul, is plain. They knew well enough that Paul had not persuaded them to it, and it was important now to show them that it could not be traced to God.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p><em>He peismone</em>: the art of persuasion, the effort of the Judaizers to persuade you. Only here and in ecclesiastical writers. The God who called you to freedom is not the source of any persuasion that leads back to bondage.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"9": {
"synthesis": "<p>A little leaven leavens the whole lump. Paul borrows this proverb, which he also uses in 1 Corinthians 5:6, to warn that partial corruption spreads through an entire community. Calvin explains Satan's characteristic stratagem: he does not attempt open destruction of the whole gospel but taints its purity by introducing corrupt opinions that seem minor. Many persons overlook what seems a slight error, not realizing how pervasive its consequences. Barnes sees two possible applications: either a pre-existing tendency among the Galatians to conform to rites, which has now like leaven leavened them, or the false teachers themselves compared to leaven working through the congregation. Robertson insists it is merely the pervasive power of leaven that is invoked here, not leaven as a symbol of evil, the same neutral point made in the parable of Matthew 13:33. Wesley applies it personally: one troubler troubles all.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>Satan's stratagem is that he does not attempt an avowed destruction of the whole gospel, but he taints its purity by introducing false and corrupt opinions. Many persons are thus led to overlook the seriousness, as they consider it of little moment, not perceiving how swiftly the contagion spreads.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>This is evidently a proverbial expression. Its meaning here is that the embracing of the errors which they had adopted was to be traced to some influence existing among themselves, acting like leaven. Either a slight tendency to conform to rites has pervaded the mass, or the false teachers may be compared to leaven working through the whole lump.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>Paul has this proverb also in 1 Corinthians 5:6. It is merely the pervasive power of leaven that is involved in the proverb, as in Matthew 13:33, not leaven as a symbol of evil in itself.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"10": {
"synthesis": "<p>Despite his sharp words, Paul expresses confidence in the Galatians that they will return to his mind on the matter, while pronouncing that whoever has troubled them will bear the judgment. Calvin notes that expressing good hopes about people gives them courage, for they reckon it shameful to disappoint those who are kind toward them. Yet the reversal of his fierceness against the false apostles is deliberate: all his anger is directed at the teachers, not the taught. Barnes reads Paul as believing that after they have heard his arguments they will again embrace his teaching. Wesley sees the singular troubler as one identifiable leader bearing a heavy burden already hanging over his head. Robertson observes that Paul uses indefinite relative clause form, suggesting he may not know the ringleader precisely, consistent with his use of singular <em>tis</em> in verse 7; judgment falls regardless of identity.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>It gives us courage to learn that good hopes are entertained about us; for we reckon it shameful to disappoint those whose feelings toward us are kind and friendly. But to the troublers all his fierceness is directed, and on them the punishment is threatened, while good hopes are expressed for the Galatians.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>Though they had been led astray and had embraced many false opinions, yet, on the whole, Paul had confidence in their piety and believed they would yet return and embrace the truth. He seems to mean that after reading this letter they will be no otherwise minded than he is teaching them.</p>"},
{"src": "wesley", "attr": "Wesley", "html": "<p>Yet I have confidence that after ye have read this, ye will be no otherwise minded than I am. But he that troubleth you shall bear his judgment, a heavy burden already hanging over his head, whoever he be that has led you astray.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"11": {
"synthesis": "<p>Paul refutes the slander that he still preaches circumcision, pointing to his ongoing persecution as proof of his consistent anti-circumcision gospel. Calvin argues: it would be completely in his power to avoid displeasure and danger were he only to mix ceremonies with Christ; the earnestness with which he opposes them is on no personal account. Barnes explains that false teachers may have appealed to Paul's circumcision of Timothy as evidence that he endorsed the practice for justification, but Paul's point is that if he truly preached circumcision he would not be persecuted. Wesley notes that Paul did not condemn condescending to weakness in others, but his doctrine was clear: the cross nullified the legal system. Robertson focuses on the theological connection: the offense of the cross was specifically the scandal that the crucified Christ had abolished the law, and that is precisely what Paul preaches.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>It would be completely in my power to avoid the displeasure of men and every kind of danger and persecution, were I only to mix ceremonies with Christ. The earnestness with which I oppose them is not on my own account nor for my own advantage; I oppose them because the gospel itself demands it.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>Paul here proceeds to vindicate himself from giving countenance to the doctrines which the false teachers had advanced. It is evident they appealed to Paul himself and alleged he insisted on the necessity of circumcision. If he still preached circumcision, why is the offence of the cross not ceased and the persecution stopped?</p>"},
{"src": "wesley", "attr": "Wesley", "html": "<p>The grand reason why the Jews so bitterly persecuted Paul was that his preaching Christ crucified implied the abolition of the law. If he preached circumcision that offence would cease. Yet he did not condemn conforming out of condescension to weakness; only his doctrine against circumcision for justification was clear.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"12": {
"synthesis": "<p>Paul's indignation reaches its sharpest point: he wishes those who are unsettling the Galatians would go further and castrate themselves. Most commentators read the cutting as a wish for excommunication from the church, with a bitter wordplay on circumcision, though Chrysostom and others read a harsher bodily meaning. Calvin sees the prayer as reflecting apostolic indignation at those who tear the church for the sake of circumcision, noting that Paul cannot be charged with cruelty since he elsewhere pleads for mercy toward the erring. Barnes explicitly rejects Chrysostom's interpretation as singular and monstrous, taking the meaning as exclusion from the communion of the church. Wesley agrees: cast out from your church those who thus trouble you. Robertson notes the late verb <em>anastatountes</em> meaning to disturb or drive from one's abode, and that Paul uses the future middle <em>apokopsontai</em> regarding those who unsettle them.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>His indignation proceeds still farther, and he prays for destruction on those impostors. The word cut off appears to be employed in allusion to the circumcision which they pressed: they tear the church for the sake of circumcision; I wish they were entirely cut off. Chrysostom favors the harsher reading, but Calvin believes apostolic mildness requires a different sense.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>That is, as I understand it, from the communion of the church. So far am I from agreeing with them and preaching circumcision as they do, that I sincerely wish they were excluded from the church as unworthy a place among the children of God. The more monstrous interpretation adopted by Chrysostom, the learned reader may see refuted by Bishop Warburton.</p>"},
{"src": "wesley", "attr": "Wesley", "html": "<p>I would they were even cut off from your communion; cast out of your church, that thus trouble you. The wordplay on circumcision sharpens the apostolic irony: those who insist on cutting should experience their own principle taken to its extreme.</p>"}
],
"consensus": "mixed",
"key_tension": "Commentators divide on whether cut off means excommunication from the church or carries a harsher bodily reference paralleling circumcision."
},
"13": {
"synthesis": "<p>Paul pivots: the Galatians have been called to liberty, but liberty must not become an occasion for the flesh. Calvin makes the important distinction between liberty and the use of liberty: liberty lies in the conscience before God; the use of it lies in outward conduct toward others. Having urged them to suffer no diminution of liberty, he now warns them not to exploit it. Barnes explains that the freedom Paul commends is freedom from sin and from bondage to Mosaic ceremony, and that using it as license for the flesh betrays both its source and its purpose. Wesley is concise: use not liberty for an occasion to the flesh, but by love serve one another, thereby showing that Christ has made you free. Robertson notes the Greek uses <em>aphorme</em>, a springboard, warning that liberty so easily turns to license. Clarke observes that the antidote to licentiousness is love, not renewed law.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>Liberty is one thing, and the use of it another thing. Liberty lies in the conscience, and looks to God; the use of it lies in outward matters, and deals not with God only but with men. Having exhorted the Galatians to suffer no diminution of their liberty, he now enjoins them to be moderate in the use of it, so as not to employ it as an excuse for the flesh.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>Freedom from Jewish rites and ceremonies, and from the servitude of sin; not in subjection to anything that savoured of bondage. They were free; but the use of freedom was not to gratify the flesh. The meaning is that Paul wished the false teachers removed because true Christians had been called unto liberty, and they were abridging and destroying that liberty.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>Ye were called for freedom, on the basis of and for the purpose of freedom. Only use not liberty as a springboard for the flesh: <em>aphorme</em>, a base of operations. Liberty so easily turns to license; the antidote is not law but love.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"14": {
"synthesis": "<p>All the law is fulfilled in one word: you shall love your neighbor as yourself. Calvin sees in this a deliberate contrast between Paul's insistence on love as the heart of Christian duty and the false apostles' insistence on ceremonies. Love forms the chief part of Christian perfection, expressing the whole of duty toward others. Barnes notes that Paul uses a striking paradox, urging obedience to the very law against which he has been arguing, but this is the moral law, not the ceremonial, as proof of the new love and life. Wesley strengthens the connection: none can truly love the neighbor without loving God (1 John 4:12), so the love of neighbor includes all perfection. Robertson observes the reference is to Leviticus 19:18, which the Jews confined to fellow Jews, while Paul universalizes it; the citation shows how the Spirit-led community transcends the law's narrow application even while fulfilling its deepest intention.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>There is a contrast in this verse between Paul's exhortation and the doctrine of the false apostles. While they insisted on ceremonies alone, Paul takes a passing glance at the actual duties of Christians. This commendation of love informs the Galatians that love forms the chief part of Christian perfection.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>This expresses the substance of the whole law; it embraces and comprises all. Paul alludes to the law in regard to duty to our fellow-men. He is saying that this law would counteract all the evil workings of the flesh; and if this were fulfilled, all our duty to others would be discharged. A similar sentiment he has expressed in Romans 13:8-10.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>Paul uses here a striking paradox by urging obedience to the law against which he has been arguing, but this is the moral law as proof of the new love and life. Jews confined neighbor to Jews; Paul universalizes Leviticus 19:18 in precisely the same way Jesus did in Matthew 22:40.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"15": {
"synthesis": "<p>The warning against biting and devouring one another reflects an actual situation of strife in the Galatian churches. Calvin notes this probably arose from doctrinal disputes, and that the false doctrine itself may have been a divine judgment upon their prior ambition and pride. He argues from the result: such factious proceedings in the church must ultimately lead to total destruction, as wild beasts consume each other. Barnes sees the image referring specifically to strifes between Jewish and Gentile converts, the two parties that Judaizing agitation had set at war with each other. Wesley traces the consequence to the body and soul: by bitterness, strife, and contention, health and strength of body and soul are consumed, as well as substance and reputation. Robertson notes that both verbs, to bite and to devour, were commonly used together of wild animals, and references the famous story of two snakes that each swallowed the other by the tail.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>We may conjecture that the Galatians had disputes among themselves, for they differed about doctrine. The apostle demonstrates from the result how destructive such proceedings in the church must ultimately prove to be. False doctrine was probably a judgment from heaven upon their ambition, pride, and other offenses that preceded it.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>The reference is probably to the strifes which would arise between the two parties in the churches, the Jewish and the Gentile converts. The word bite means, properly, to sting; and devour as wild beasts do. Take heed that ye be not consumed one of another, as wild animals fighting to mutual destruction.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>Condition of first class, assumed as true. Two common and old verbs often used together of wild animals, or like cats and dogs. That ye be not consumed: negative final clause with first aorist passive of <em>analisko</em>. There is a famous story of two snakes that grabbed each other by the tail and each swallowed the other whole.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"16": {
"synthesis": "<p>Paul now gives the remedy for the flesh-driven strife and mutual destruction just described: walk by the Spirit, and you will not fulfill the lust of the flesh. Calvin identifies this as the cure for carnal division: not permitting the flesh to rule, and yielding to the direction of the Spirit. The Galatians are implicitly told that they are carnal, destitute of the Spirit, since the life they lead is unworthy of Christians. Barnes explains the command as living under the influences of the Holy Spirit, admitting those influences fully into the heart, not resisting them. Wesley paraphrases directly: follow his guidance in all things, and fulfil not in anything the desire of the flesh. Robertson notes the strong double negative with aorist subjunctive conveying certitude: ye will not fulfil the lust of the flesh; the craving or longing (epithumia) of the flesh is placed under the Spirit's authority.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>Now follows the remedy. The ruin of the church is no light evil, and whatever threatens it must be opposed with the most determined resistance. But how is this to be accomplished? By not permitting the flesh to rule in us and by yielding ourselves to the direction of the Spirit of God.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>This is the true rule about overcoming the propensities of your carnal natures and avoiding the evils of strife and contention: walk in the Spirit, live under the influences of the Holy Spirit, admit those influences fully into your hearts. Do not resist him, but yield to all his suggestions.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>Ye shall not fulfil: rather, ye will not fulfil. Strong double negative with aorist active subjunctive. The lust of the flesh, <em>epithumian sarkos</em>, in the bad sense here as usual in Paul: the craving or longing of corrupt nature placed under the Spirit's authority.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"17": {
"synthesis": "<p>The flesh and the Spirit are at war, and this conflict is the reason believers often cannot do what they wish. Calvin insists that <em>sarx</em> denotes the entire corrupt nature of man, not merely the lower senses, and that the contrast with Spirit confirms this broader meaning. Barnes describes the experience: flesh and Spirit draw in opposite directions, and while the Spirit of God would lead one way, carnal nature leads the other, producing the painful controversy that exists in the believing mind. Wesley is precise: the Holy Spirit on his part opposes your evil nature; these are contrary to each other and there can be no agreement between them. Robertson uses the image of a tug of war and notes that to personify <em>sarx</em> in this way is striking; both flesh and Spirit long for the possession of the soul, as Bunyan shows in <em>Holy War</em>. The result is that believers are often prevented from doing what they would do by the ongoing conflict.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>The word <em>flesh</em> denotes the nature of man; the limited application of it to the lower senses alone is refuted by various passages. The contrast between Spirit and flesh is the same that Paul draws in Romans 7 and 8, where the struggle of the believing heart is described not as flesh only but as corrupt human nature across all its faculties.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>The inclinations and desires of the flesh are contrary to those of the Spirit. They draw us away in an opposite direction; and while the Spirit of God would lead us one way, our carnal nature would lead us another, and thus produce the painful controversy which exists in our minds.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>Lusteth against: <em>epithumei kata</em>, like a tug of war. This personifies <em>sarx</em>. Both the flesh and the Spirit long for the possession of the soul. Are lined up in opposition to each other. The result is that you cannot always do the things you want, whichever side is temporarily winning.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"18": {
"synthesis": "<p>Being led by the Spirit means being free from the law. Calvin connects this to Romans 6:14, calling it a consolatory declaration: since believers cannot perfectly satisfy the law, they must know that their partial obedience is accepted in God's sight as if complete, because they are not under the law's condemnation but under grace. Barnes distinguishes two dispensations: under the law's control versus under the Spirit's control, the Spirit-led believer being free from Mosaic restraint not through antinomianism but through a higher life. Wesley identifies the Spirit as the Spirit of liberty and love, into all holiness; not under the law means not under its curse or bondage, not under the guilt or the power of sin. Robertson draws the connection between law and flesh: the flesh made the law weak, so being led by the Spirit and being not under the law are two expressions of the same reality, as Romans 8:14 shows.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>In the way of the Lord believers are apt to stumble, but let them not be discouraged because they are unable to satisfy the demands of the law. The consolatory declaration found also in Romans 6:14 assures us that the performance of their duties is not rejected on account of their present defects, but is accepted in the sight of God.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>If you submit to the teachings and guidance of the Holy Spirit, ye are not under the law. You are under a different dispensation, the dispensation of the Spirit, free from the restraints and control of the Mosaic law and under the control of the Spirit of God.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>Under the law instead of under the flesh as one might expect: see Galatians 3:2-6 for this contrast between law and spirit. The flesh made the law weak; Romans 8:3. They are one and the same in result. See the same idea in Romans 8:14.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"19": {
"synthesis": "<p>Paul lists the works of the flesh, which are manifest and well-known, as the counterpoint to the fruit of the Spirit. Calvin insists that <em>sarx</em> here means the entire corrupt nature of man, not merely bodily passions, and that the picture of the flesh is meant to show believers what they must resist in themselves. Barnes notes the same point: many of the vices enumerated are passions of the mind or soul rather than the body, so flesh cannot mean body alone. Wesley observes that works are mentioned in the plural because they are distinct from and often inconsistent with each other, unlike the singular fruit of the Spirit. Robertson identifies four groups in Paul's list of manifest vices: sensual sins, religious sins (idolatry and sorcery), social sins (enmities through dissensions), and intemperance. The word <em>phanera</em> means opposed to hidden, underscoring that these works of corrupt nature are visible to all.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>Paul now draws a picture both of the flesh and of the spirit. If men knew themselves, they would not need this inspired declaration, for they are nothing but flesh; but such is the hypocrisy belonging to our natural state that all acknowledge corruption in general while flattering themselves with the belief that they are free from it.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>The works of the flesh are what corrupt and unrenewed human nature produces. It is evident here that the word <em>flesh</em> is used to denote corrupt human nature, and not merely the body, since many of the vices here enumerated are the passions of the mind or the soul rather than bodily appetites.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p><em>Phanera</em>: manifest, opposed to hidden. Ancient writers were fond of lists of vices and virtues. There are four groups in Paul's list: sensual sins, religious sins such as idolatry and sorcery, social sins from enmities through dissensions, and intemperance.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"20": {
"synthesis": "<p>Paul continues the catalogue of fleshly works, including idolatry, sorcery, enmities, strife, jealousy, fits of anger, rivalries, dissensions, and heresies. Barnes observes that witchcraft or sorcery does not require Paul to vouch for the actual existence of occult power; the point is that what was known as such was proof of corrupt human nature, being a system of imposture and falsehood throughout. Wesley insists that the prohibition of such things in the Old Testament means that to deny their existence is to deny the authority of both Testaments. Ellicott catalogues the social sins of the list carefully, noting that strife and jealousy belong together as the outward and inward aspects of competitive sin, while heresies are the formal divisions that arise when dissensions harden into parties. Clarke notes that every item in this middle section of the list relates to sins against the neighbor and community, not merely personal vices. The cumulative effect shows that the flesh corrupts every domain of life.</p>",
"voices": [
{"src": "ellicott", "attr": "Ellicott", "html": "<p>The social sins catalogued here move from inward jealousy to outward strife, from private anger to public divisions. Heresies represent the hardening of dissensions into formal party divisions, the last stage of a process that begins with envy and ends in schism that tears the body of Christ.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>The apostle does not vouch for the actual existence of witchcraft in itself; but he says that what was known as such was a proof of the corrupt nature of man, and was one of the fruits of it. Nothing is a better demonstration of the depravity of the human heart than an extended and systematized attempt to impose on mankind.</p>"},
{"src": "wesley", "attr": "Wesley", "html": "<p>That witchcraft means witchcraft strictly speaking appears from its being joined with the worship of devil-gods, and not with murder. This is frequently and solemnly forbidden in the Old Testament. To deny therefore that there is or ever was any such thing is, by plain consequence, to deny the authority both of the Old and New Testament.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"21": {
"synthesis": "<p>Paul closes the vice list with a solemn warning: those who practice such things will not inherit the kingdom of God, and he notes he has warned them of this before. Calvin connects the warning to an implicit rebuke of the false apostles, who wasted time on ceremonies while neglecting the far more valuable instruction about the deeds that exclude from the kingdom. Barnes sees in the exhaustive list the most striking and unanswerable proof of human depravity. Wesley clarifies the grammar: the plural works of the flesh are enumerated because they are distinct and often inconsistent with each other, unlike the singular fruit of the Spirit. Robertson makes a crucial distinction between the two Greek verbs: <em>prasso</em> for habitual practice versus <em>poieo</em> for occasional doing; it is the habit of these sins that proves one is not in the kingdom of God. The warning is not against falling into sin but against living in it as a pattern of life.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>By this awful threatening he intended not only to alarm the Galatians but likewise to glance indirectly at the false apostles, who had laid aside far more valuable instruction and spent their time in disputing about ceremonies. He instructs us by his example to press those exhortations and threatenings that bear on the actual life of holiness.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>In regard to this passage we may remark that it furnishes the most striking and unanswerable proof of human depravity. Paul represents these as the natural and common effects of corrupt human nature; he had told them before when he was with them, as a solemn forewarning.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p><em>Prasso</em> is the verb for habitual practice, not <em>poieo</em> for occasional doing. The habit of these sins is proof that one is not in the Kingdom of God and will not inherit it. Paul repeats his warning given while with them; he did his duty then and now reinforces it in writing.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"22": {
"synthesis": "<p>In deliberate contrast to the plural works of the flesh, the fruit of the Spirit is singular: a unified cluster of nine graces flowing from a single source. Calvin cites Bishop Sanderson on the contrast between work and fruit: in the service of the flesh the toil exceeds the fruit; in the service of the Spirit the benefit so exceeds the labour that the work is not even mentioned. Barnes stresses that Paul does not trace these virtues to the renewed human heart; he traces them to a foreign influence, the agency of the Holy Spirit, because even when renewed the heart alone does not produce them. Wesley emphasizes love as the root of all the rest, with gentleness defined as a disposition toward all persons, especially ignorant and wicked ones, and goodness as all that is benign, soft, winning, and tender. Robertson sees a beautiful tree of fruit with nine luscious graces, and notes that love appears first because it is the foundational grace from which the others flow, as Paul has argued in 1 Corinthians 13.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin (citing Sanderson)", "html": "<p>In the service of the flesh the toil is so great that in comparison thereof the benefit is as nothing; in the service of the Spirit the benefit is so great that in comparison thereof the labour is as nothing. Without even mentioning the work, the Spirit's produce is called fruit, as in Ephesians 5:9.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>It is not without design, evidently, that the apostle uses the word Spirit here, denoting that these things do not flow from our own nature. Paul does not trace them to our own hearts, even when renewed. He says the fruit of the Spirit, not the fruit of the renewed heart; the Holy Spirit produces them.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>Paul changes the figure from works in verse 19 to fruit as the normal outcropping of the Holy Spirit in us. It is a beautiful tree of fruit that Paul pictures here with nine luscious fruits on it. Love appears first as in 1 Corinthians 13, superior to all forms of human affection.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"23": {
"synthesis": "<p>The list closes with meekness and temperance, and Paul adds that against such things there is no law. Calvin reads this as the deepest point: where the Spirit reigns the law has no longer dominion over believers; by moulding hearts to his own righteousness the Lord delivers believers from the severity of the law, so that their intercourse with God is not regulated by its covenant of merit and penalty. Barnes notes that the word translated temperance or self-control is <em>egkrateia</em>, meaning the power or ascendancy one has over exciting and evil passions of all kinds, broader than modern temperance which is confined mainly to abstinence from drink. Wesley defines meekness as holding all affections and passions in even balance. Ellicott observes the logical progression: if such graces as love, peace, joy, and self-mastery characterize a life, no external law could add to or improve upon that life; the law exists to restrain evil, and where the Spirit produces its fruit, the law has nothing against which to operate.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>Paul's real meaning is deeper and less obvious: namely that where the Spirit reigns the law has no longer any dominion. By moulding our hearts to his own righteousness, the Lord delivers us from the severity of the law, so that our intercourse with himself is not regulated by its covenant, nor our consciences entangled in its terrors.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>The word here used, <em>egkrateia</em>, means properly self-control, continence, the power or ascendancy which we have over exciting and evil passions of all kinds. It denotes the self-rule which a man has over the evil propensities of his nature, much broader than our modern use of temperance for abstinence from drink.</p>"},
{"src": "wesley", "attr": "Wesley", "html": "<p>Meekness: holding all the affections and passions in even balance. Against such there is no law: the law exists to restrain evil; where the Spirit produces these graces no law finds anything to condemn, and the whole purpose of law is fulfilled by a higher principle.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"24": {
"synthesis": "<p>Those who belong to Christ have crucified the flesh with its passions and desires. Calvin locates the crucifixion of the flesh in the cross of Christ itself: this mortification does not belong to human effort but is the effect of Christ's cross appropriated by faith. The grace of the Spirit, flowing from the cross, kills the flesh and quickens believers to spiritual life. Barnes explains that the corrupt passions of the soul are put to death, rendered as though dead with no power over the believer. Wesley uses the image of nailing: the flesh is nailed to a cross from which it has no power to break loose, though it is not yet fully dead, only continually weakening. Robertson stresses the aorist tense as a definite event, the mystical union with Christ effected in conversion, and underscores the completeness of the extermination of this evil force, guaranteeing victory over passions and evil dispositions.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>The apostle adds this to show that all Christians have renounced the flesh, and therefore enjoy freedom. The word crucified is employed to point out that the mortification of the flesh is the effect of the cross of Christ. This work does not belong to man; by the grace of the Spirit flowing from the cross it is accomplished.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>The corrupt passions of the soul have been put to death; that is, destroyed. They are as though they were dead and have no power over us. All who are true Christians have crucified the flesh with its affections, all corrupt desires and passions.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>Crucified the flesh: definite event, first aorist active indicative, as in Galatians 2:19, mystical union with Christ. <em>Sun</em>: together with, emphasizing the completeness of the extermination of this evil force and the guarantee of victory over one's passions and dispositions toward evil.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"25": {
"synthesis": "<p>If we live by the Spirit, let us also walk by the Spirit. Calvin draws the practical implication: the death of the flesh is the life of the Spirit; if the Spirit of God lives in us, let him govern our actions. Those who claim to live in the Spirit must prove it by walking accordingly. Barnes frames it as an earnest exhortation: believers profess not to be under the dominion of the flesh and to be controlled by the Holy Spirit; let them then act in this manner and yield themselves to his influences. Wesley connects it back to verse 16: if we are indeed raised from the dead and alive to God by the Spirit's operation, let us follow his guidance in all our tempers, thoughts, words, and actions. Robertson notes the present subjunctive of <em>stoicheo</em> meaning to walk in line or march, suggesting ordered disciplined movement under the Spirit's direction.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>According to his usual custom, the apostle draws from the doctrine a practical exhortation. The death of the flesh is the life of the Spirit; if the Spirit of God lives in us, let him govern our actions. There will always be many persons daring enough to make a false boast of living in the Spirit, but the apostle challenges them to a proof of the fact.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>We who are Christians profess to be under the influences of the Holy Spirit. By his influences and agency is our spiritual life. We profess not to be under the dominion of the flesh. Let us then act in this manner, and as if we believed this; let us yield ourselves to his influences.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>By the Spirit let us also walk: present subjunctive, volitive, of <em>stoicheo</em>, to walk in line or march. Let us also go on walking by the Spirit, making our steps by the help and guidance of the Spirit who is the source of our life.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"26": {
"synthesis": "<p>The section closes with a warning against vainglory, the competitive desire for honor that generates mutual provoking and envying. Calvin diagnoses ambition as the mother of many evils in the church and defines <em>kenodoxia</em> as the desire to excel all others. The double consequence is provoking those who are beneath us and envying those who are above us. Barnes sees this as likely connected to the paltry competitions arising from distinctions of birth and ritual: Jews priding themselves on circumcision, others on Gentile superiority, producing the faction and strife of the preceding verses. Wesley explains that those who do not carefully and closely follow the Spirit easily slide into vainglory, and the natural effects are provoking and envying of others. Robertson notes that the word <em>kenodoxoi</em> appears only here in the New Testament, once in Epictetus, and that provoking (<em>prokaloumenoi</em>) is the language of challenging to combat, while envying captures the passive resentment on the other side.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>Of many evils existing in society at large and particularly in the church, ambition is the mother. Paul therefore directs us to guard against it, for the <em>kenodoxia</em> of which he speaks is nothing else than the desire of honor, by which every one desires to excel all others. The double consequence is provoking those beneath us and envying those above.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>The word means proud or vain of empty advantages, as of birth, property, eloquence, or learning. The reference is probably to the paltry competitions which arose on account of these supposed advantages, a likely cause of the difficulties existing in the Galatian churches, where Jews prided themselves on their birth and others responded in kind.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p><em>Kenodoxoi</em>: late word only here in the New Testament, once in Epictetus. <em>Provoking one another</em>: old word <em>prokaloumenoi</em>, to call forth, to challenge to combat, only here in the New Testament and in a bad sense. <em>Envying</em>: the passive resentment on the other side of the competitive dynamic.</p>"}
],
"consensus": "affirm",
"key_tension": null
}
},
"6": {
"1": {
"synthesis": "<p>Chapter 6 opens with pastoral instruction on restoring those overtaken by a fault. Calvin, citing the context of chapter 5, specifies that the fault likely refers to the works of the flesh just enumerated. The key is <em>overtaken</em>: not deliberate rebellion but being surprised by temptation, caught off guard by the violence of a sin one had not planned to commit. Barnes emphasizes the tenderness required: bring back to virtue any led astray by the strength of temptation. Wesley specifies who is qualified: those who are spiritual, who continue to live and walk by the Spirit, are the ones equipped to restore; and the instrument of restoration is reproof, instruction, or exhortation. Clarke adds that the spirit of meekness is essential to the cure, not merely an accessory virtue. Robertson notes the technical meaning of <em>prolambanō</em> as to surprise or detect, and calls <em>paraptōma</em> a lapse or slip rather than a wilful sin.</p>",
"voices": [
{"src": "barnes", "attr": "Barnes", "html": "<p>He exhorts them to bring back to the ways of virtue any one who through the strength of strong temptation had been led astray. This implies that those who had sinned were not to be abandoned but to be gently reclaimed, the emphasis falling on the manner of the restoration.</p>"},
{"src": "wesley", "attr": "Wesley", "html": "<p>Brethren, if a man be overtaken in any fault by surprise, ignorance, or stress of temptation: ye who are spiritual, who continue to live and walk by the Spirit, restore such an one by reproof, instruction, or exhortation, in the spirit of meekness. This is essential; the whole force of the cure lies here.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p><em>Prolambanō</em>: to take beforehand, to surprise, to detect. <em>Paraptōmati</em>: a falling aside, a slip or lapse in the papyri rather than a wilful sin. The spiritually led are the spiritual experts in mending souls, doing the delicate work of restoration.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"2": {
"synthesis": "<p>Bear one another's burdens and so fulfil the law of Christ. Calvin explains that the weaknesses or sins under which believers groan are called burdens, and the image of someone bending under a load makes the appeal natural: nature dictates that those who stoop under weight ought to be relieved. Mild and friendly correction is the means; indulging or overlooking sin is not bearing the burden. Barnes applies it to the peculiar temptations and easily besetting sins that constitute a heavy burden for each person; we should aid one another in overcoming them. Wesley calls the law of Christ the law of love, the distinguishing mark of his disciples, and the uncommon expression <em>law of Christ</em> signals that love is not freedom from all law but fulfillment of a higher one. Robertson distinguishes between <em>baros</em> here, weight about to press one down, and <em>phortion</em> in verse 5, one's assigned load; the command is to step in when someone else is about to be crushed.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>The weaknesses or sins under which we groan are called burdens, and this phrase is singularly appropriate, for nature dictates that those who bend under a burden ought to be relieved. We must not indulge or overlook the sins by which our brethren are pressed down, but relieve them, which can only be done by mild and friendly correction.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>Bear with each other; help each other in the Divine life. Every man has peculiar temptations and easily besetting sins which constitute a heavy burden. We should aid each other in regard to these and help one another to overcome them, thus fulfilling the peculiar law of the Redeemer.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p><em>Baros</em> means weight, used of Jesus bearing his cross in John 19:17. It is when one's load is about to press one down that help is needed in carrying it. <em>Anaplerosate</em>: to fill up completely, emphasizing that full obedience to the law of Christ consists precisely in this mutual support.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"3": {
"synthesis": "<p>Self-deception is the root of the failure to bear others' burdens: if a man thinks himself to be something when he is nothing, he deceives himself. Calvin makes the point general: since all men are nothing before God, any claim to be something is a deception, and comparing oneself favorably with others only compounds the error. Barnes gives a practical application: those most confident in their own standing may be those most in danger of falling; a high estimate of oneself does not secure safety. Wesley identifies the precise error: thinking oneself above one's brethren, or capable by one's own strength; he who knows himself to be nothing will bear burdens, while the self-important will not stoop to it. Clarke notes that harsh, censorious, overbearing persons who suppose themselves to excel in piety are in God's sight as sounding brass. Robertson is crisp: he thinks himself a big number being nothing at all; he deceives no one else, only himself.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>Paul's meaning is general: since all men are nothing, he who wishes to appear something, and persuades himself that he is somebody, deceives himself. The special temptation is to measure oneself by comparison with others and think oneself superior; the apostle declares no such comparison ought to be allowed.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>This is designed to be another reason why we should be kind and tender to those who have erred: even those who are most confident may fall. They who feel secure, and think it impossible that they should sin, are not safe; they may be wholly deceived and may be nothing when they have the highest estimate of themselves.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>Something when he is nothing: thinks he is a big number while being nothing at all; neuter singular pronouns. <em>Phrenapata heauton</em>: leads his own mind astray; a late compound word first here and then in later writers. He deceives no one else.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"4": {
"synthesis": "<p>Let every man prove his own work, and then he will have grounds for rejoicing in himself, not in another. Calvin directs the Galatians away from comparative self-evaluation: let no man measure himself by the standard of another or please himself by thinking others appear less worthy. Let him lay aside all flattering comparisons and examine his own life and works by an absolute standard. Barnes specifies the proper measuring rod: compare yourself with the word of God and the infallible rule by which we will be judged on the last day, not with other people who may be weaker still. Wesley is brief but sharp: he will find matter of rejoicing if his works are right before God, and not in another, meaning not in glorying over others. Clarke adds that true self-examination before God tends naturally toward humility rather than pride, because one sees clearly what God sees.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>No man should measure himself by the standard of another, or please himself with the thought that others appear to him less worthy of approbation. Let him lay aside all such flattering comparisons, and let him examine his own life by an absolute standard rather than by comparing himself with weaker neighbors.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>Let him form a proper estimate of what is due to himself, according to his real character. Let him compare himself with the word of God, the infallible rule which he has given and by which we are to be judged in the last great day. Then shall he have rejoicing in himself, not in another.</p>"},
{"src": "wesley", "attr": "Wesley", "html": "<p>Let every man try his own work narrowly, examining all he is and all he does. Then he will find in himself matter of rejoicing, if his works are right before God, and not in another, not in glorying over others whose works are worse than his.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"5": {
"synthesis": "<p>Every man shall bear his own burden. This verse stands in apparent tension with verse 2 but is distinguished by the two different Greek words used: <em>baros</em> in verse 2 for a crushing weight that calls for communal help, and <em>phortion</em> here for each person's assigned cargo or individual load. Calvin frames it eschatologically: at God's judgment each person will give account for himself alone; comparing oneself with others in this life will not survive the divine reckoning. Barnes calls it a proverbial saying meaning that each person will receive their proper reward; if virtuous, they will be happy; if vicious, they will be miserable, bearing the proper penalty of their sin. Clarke notes the complementarity: we help one another with overwhelming burdens, yet each must ultimately answer for their own life before God. Robertson notes Christ calls his <em>phortion</em> light, though the Pharisees made their burdens heavy for others.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>To destroy sloth and pride, Paul brings before us the judgment of God, in which every individual for himself, and without a comparison with others, will give an account of his life. The false conclusions to which comparison with others leads will be overthrown when each stands alone before the throne.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>This seems to be a kind of proverbial saying meaning every man shall have his proper reward. If he is a virtuous man he will be happy; if a vicious man he will be miserable. If a virtuous man, he will have the source of happiness in himself; if a sinner, he must bear the proper penalty of his sin.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p><em>Phortion</em>: old word for a ship's cargo, one's assigned load. Christ calls his <em>phortion</em> light, though he terms those of the Pharisees heavy. The terms in verse 2 and verse 5 are thus not always kept distinct, though Paul does make a distinction here from the <em>baros</em> in verse 2.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"6": {
"synthesis": "<p>Let him who is taught in the word share in all good things with him who teaches. Calvin describes the historical situation: teachers and ministers of the word were being neglected, and this was base ingratitude; how disgraceful to defraud of temporal support those by whom souls are fed. Barnes applies the command concretely: let there be a common participation of all good things, sharing material provision with those who teach. Wesley is concise: let him that is taught impart to him that teacheth all such temporal good things as he stands in need of. Robertson provides the most illuminating note, observing that this is early evidence of paid teachers in Christian churches, that <em>koinōneitō</em> means contribute rather than merely communicate, and that the present passive participle retains the accusative of thing, showing the directional flow of benefit from teacher to taught and of material support flowing back from taught to teacher.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>It is probable that the teachers and ministers of the word were at that time neglected. This showed the basest ingratitude. How disgraceful it is to defraud of their temporal support those by whom our souls are fed; to refuse an earthly recompense to those from whom we receive heavenly benefits.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>Let him share with him who teaches; let there be a common participation of all good things. In all good things means in everything that is needful for comfortable subsistence. The duty of supporting ministers of the gospel is laid down by Paul explicitly in 1 Corinthians 9:11-14.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>Those who receive instruction are called on to contribute for the support of the teacher. This is early evidence of paid teachers in the churches. <em>Koinoneitoo</em>: contribute, share, better than merely communicate, showing the reciprocal flow of spiritual and material benefit.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"7": {
"synthesis": "<p>Do not be deceived: God is not mocked, for whatever a man sows that will he also reap. Calvin connects this to the dishonest excuses offered for not supporting ministers; God's judgment cuts through all such rationalizations since whatever is sown determines what is harvested. Barnes calls the formula <em>be not deceived</em> an introduction to something particularly weighty, warning that the dangers of self-deception include the corruption of the heart, the difficulty of knowing one's true character, and the instructions of false teachers. Wesley concentrates it: those who think to reap otherwise than they sow attempt to mock God, but God is not mocked. Robertson traces the rare Greek verb <em>mukterizetai</em> from <em>mukter</em>, the nose, meaning to turn the nose up at someone: men attempt to sneer at God's moral order but never escape the consequences of doing so. Clarke notes that the law of sowing and reaping is woven into the fabric of creation by its Author, and attempts to circumvent it are futile.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>The design of this observation is to reply to the dishonest excuses which are frequently pleaded. Various reasons are alleged for not supporting ministers and teachers, but these apologies Paul utterly rejects, for a reason which it is impossible to invalidate: God is not mocked, and his moral order cannot be evaded.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>Be not deceived in regard to your character and your hopes for eternity. This is a formula of introduction to some admonition that is peculiarly weighty and important. God is not mocked: he cannot be imposed on; he sees the heart; he knows what we are doing; the hypocrisy that imposes on men never imposes on him.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p><em>Mukterizetai</em>: rare verb, from <em>mukter</em> the nose, to turn the nose up at one. Men attempt to mock God by evading his laws, but never escape. An evasion of his laws which men think to accomplish is never successful; nature writes the penalty of sin into the harvest.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"8": {
"synthesis": "<p>Sowing to the flesh yields corruption; sowing to the Spirit yields eternal life. Calvin explains that sowing to the flesh means looking forward to the wants of the present life with no regard to a future life, and corruption is the harvest of that temporal orientation. Barnes connects the harvest to the nature of the seed: punishment under the divine government is commonly in the line of offences; the physical and moral decay that follows sins of the flesh is well known and is how nature itself executes the divine sentence. Wesley's statement is stark: out of this very seed of fleshly sowing, you shall reap corruption, meaning death everlasting; but the Spirit-sower, following his guidance in all conversation, shall by the free grace and power of God reap life everlasting. Robertson identifies the precise meaning of <em>phthoran</em> as physical and moral decay, what every doctor knows nature writes into the body through sin, while eternal life is the harvest of the Spirit-sower.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>To sow to the flesh is to look forward to the wants of the present life without any regard to a future life. They who do this will gather fruit corresponding to the seed which they have sown: they will heap up that which shall miserably perish. To sow to the Spirit is to prefer the spiritual and eternal to the carnal and temporal.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>He that soweth to his flesh makes provision for the indulgence of fleshly appetites and passions; he who makes use of his property to give indulgence to licentiousness, intemperance, and vanity. Shall of the flesh reap corruption: punishment is commonly in the line of offences; the moral and physical decay that follows sins of the flesh is a divine sentence written into nature.</p>"},
{"src": "wesley", "attr": "Wesley", "html": "<p>He that now soweth to the flesh, that follows the desires of corrupt nature, shall hereafter of the flesh, out of this very seed, reap corruption, death everlasting. But he that soweth to the Spirit, that follows his guidance in all his tempers and conversation, shall of the Spirit reap life everlasting.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"9": {
"synthesis": "<p>Let us not grow weary in doing good, for in due season we will reap if we do not faint. Calvin urges the proper use of the sowing season: God has set apart the whole of the present life for ploughing and sowing, and active and prudent husbandmen observe the proper season without letting it slip unimproved. Barnes catalogs the causes of weariness: so much opposition to the best plans, so much still to be done, so many calls on time and charity, so much ingratitude among those benefited, that Christians become disheartened and begin to slacken. Wesley exhorts perseverance in sowing to the Spirit specifically. Robertson unpacks the Greek with precision: the present subjunctive of <em>enkakeō</em> means literally <em>let us not keep on giving in to evil while doing the good</em>, framing the temptation not as outright abandonment but as gradual capitulation to the weariness that makes doing good feel insipid or unrewarding.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>Every season is not adapted to tillage and sowing; active and prudent husbandmen will observe the proper season and not indolently allow it to pass unimproved. Since God has set apart the whole of the present life for ploughing and sowing, let us avail ourselves of the season, lest through our negligence it be taken out of our power.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>Christians sometimes become weary. There is so much opposition to the best plans for doing good; there is so much to be done; there are so many calls on their time and their charities; and there is often so much ingratitude among those whom they endeavour to benefit, that they become disheartened and are in danger of giving up.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>Let us not be weary in well-doing: volitive present subjunctive of <em>enkakeō</em>. Literally, let us not keep on giving in to evil while doing the good. In due season, at harvest time, at the proper season, if we faint not and keep sowing the right seed.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"10": {
"synthesis": "<p>As we have opportunity, let us do good to all, especially to those of the household of faith. Calvin extends the metaphor of sowing: the present life is the season allotted, and every opportunity within it is a time for doing good, beginning with liberality to ministers of the gospel and expanding to all. Barnes states the rule with Cotton Mather's epigram: the opportunity to do good imposes the obligation to do it; not when convenient, not when it advances a party or contributes to fame, but simply when we have the opportunity and the power. Wesley broadens the scope: at whatever time or place and in whatever manner we can do good, we are quickened by the shortness of the time available, as Satan is quickened in doing hurt by the same knowledge. Robertson explains the special obligation toward the household of faith: they belong to the same family, and family responsibility is the most obvious. Clarke notes the order of priority: all people are included in the call, but those nearest in spiritual kinship bear the highest claim.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>The metaphor is still pursued. Every season is not adapted to tillage and sowing, and active husbandmen observe the proper season. Since God has set apart the present life for sowing, beginning with liberality to ministers of the gospel, Paul extends the exhortation to doing good to all persons without distinction.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>This is the true rule about doing good. The opportunity to do good imposes the obligation to do it. The simple rule is that we are favoured with the opportunity and have the power; not that we are to do it when convenient, but when we have the opportunity, without qualification.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>As we have occasion at any time. Let us keep on working the good deed. Of the household of faith: for the obvious reason that they belong to the same family, which carries with it the most immediate and natural responsibility of all.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"11": {
"synthesis": "<p>Paul calls attention to the large letters with which he has written with his own hand. Calvin understands this as a demonstration of his personal anxiety for the Galatians: by writing such a long epistle in his own hand rather than through an amanuensis, he increases his claim on their careful attention and shows the extent of his care. Barnes reviews the considerable variety of interpretation around <em>how large a letter</em>: some read it as a reference to the size of the individual letters, others to the length of the whole epistle. Wesley notes that Paul had not yet written a larger letter to any church and that he generally wrote through a secretary. Robertson offers the most thorough discussion: Paul takes the pen from the amanuensis at this point and writes the concluding section himself, with large individual letters possibly due to defective eyesight or for dramatic emphasis; the uncertainty remains and scholars have long debated it.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>To convince the Galatians more fully of his anxiety about them, and at the same time to ensure their careful perusal, Paul mentions that this long epistle had been written with his own hand. The greater the toil to which he submitted on their account, the stronger his claim on their affection and attention.</p>"},
{"src": "wesley", "attr": "Wesley", "html": "<p>Ye see how large a letter; St. Paul had not yet written a larger to any church. I have written with my own hand; he generally wrote by an amanuensis, so this autograph was itself a mark of his special concern for the Galatian churches.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>Paul now takes the pen from the amanuensis and writes the rest of the epistle himself. With how large letters: certainly not how large a letter. He may have used large letters because of defective eyesight, or for emphasis, or because he could only write large when doing it himself; the matter is not certain.</p>"}
],
"consensus": "mixed",
"key_tension": "Commentators are divided on whether the large letters refer to the size of Paul's individual handwriting or to the length of the whole epistle, and if the former, whether the cause is poor eyesight or deliberate emphasis."
},
"12": {
"synthesis": "<p>The Judaizers compel circumcision to make a fair show in the flesh and to avoid persecution for the cross of Christ. Calvin identifies their motivation as ambitious desire for popular applause; they pay no regard to edification but seek to impress. Ellicott adds that their primary motive was to preserve a reputation among their own people by showing conformity to Jewish custom. Barnes specifies the target: their main object was to evince zeal for external rites and customs, to be known for this, and to avoid the persecution from unbelieving Jews that Paul's cross-centered gospel attracted. Wesley concurs: they sought to make a fair appearance, to preserve a fair character, motivated by fear of persecution rather than conviction. Robertson notes the conative present active <em>anagkazousin</em>, they are trying to compel, and the rare word <em>euprosōpeō</em> meaning to be fair of face, to make a show of good appearance, appearing only here in the New Testament.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>Such men pay no regard to edification, but are guided by an ambitious desire to hunt after popular applause. The great care of the Judaizing teachers was to avoid persecution; to make a fair show in the flesh meant to recommend themselves by specious outward conformity to what their contemporaries valued.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>As many as desire to make a fair show in the flesh, to be distinguished for conformity to external rites. Their main object was to evince zeal in observance of ceremonies. They constrain the Gentile converts to be circumcised, not from conscience, but lest they should suffer persecution from the unbelieving Jews.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>To make a fair show: <em>euprosōpeō</em>, first aorist active infinitive, late verb from <em>euprosoopos</em>, fair of face. Here only in the New Testament, one example in the papyri. They try to compel: conative present active indicative. For the cross of Christ: to avoid the scandal that the cross creates.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"13": {
"synthesis": "<p>Those who receive circumcision do not themselves keep the whole law but desire the Galatians to be circumcised so they may glory in their flesh. Calvin exposes the hypocrisy: the Judaizers insist on circumcision as essential but do not themselves obey all they demand; their real motivation is the social credit of making proselytes. Barnes applies Paul's logic from chapter 5: by requiring circumcision they bring their converts under obligation to keep the entire law, which the teachers themselves are unable to do. Wesley states it plainly: so far are they from a real zeal for it. Robertson notes the textual variant between present causative middle, those having themselves circumcised, and perfect passive participle, those who have been circumcised, and judges the present form to be the harder and more likely original reading. The argument strips the Judaizers of their claimed motivation: it is not zeal for the law but desire for trophies.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>Circumcision was urged not from zeal for the law but from ambition: they desired to make proselytes and to boast of that success. They did not themselves keep the law they promoted; their design was to glory in the flesh of the Galatians, to use their conversion as a social trophy among unbelieving Jews.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>The Jewish teachers, by requiring circumcision, brought converts under obligation to keep the whole law of God. Galatians 5:3. But they did not do it themselves. Paul's idea is that if they were circumcised they brought themselves under obligation they could not fulfill, a contradiction of their own teaching.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>They who receive circumcision: present causative middle, those having themselves circumcised. Some manuscripts read the perfect passive participle, those who have been circumcised. Probably the present is correct as the harder reading, referring to those actively pursuing circumcision as a program.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"14": {
"synthesis": "<p>Paul's counter-declaration is the climax of the epistle: God forbid that I should glory except in the cross of our Lord Jesus Christ, by which the world is crucified to me and I to the world. Barnes places Paul in deliberate contrast with the Judaizers: he had as much occasion as any of them for glorying in the flesh, being circumcised of the eighth day and trained as a Pharisee, but he counts all that as nothing compared to the cross. Wesley frames the cross as the ground of all boasting: nothing in Paul himself, not what he has, is, or does, can be the basis of acceptance with God; only what Christ has done and suffered constitutes the sole ground. Robertson calls this one of the great sayings of Paul concerning his relation to Christ and to the world, noting that the world stands crucified to him, past, finished, done, by means of the same cross that crucified him to the world. Calvin sees in it the total reorientation of all values.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>God forbid that I should glory in anything pertaining to the flesh. The object of Paul is evidently to place himself in contrast with the Judaizing teachers, and to show his determined purpose to glory in nothing else but the cross of Christ. The cross reorients all values: what was gain has become loss.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>Paul had as much occasion for glorying in the things pertaining to the flesh as any of them; he had been circumcised; he had had all the advantages of birth and training. But the cross stands as the only ground of glory. By means of the cross the world is crucified to me, a past and finished act.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>Far be it from me: second aorist middle optative in a wish about the future. Hath been crucified unto me: perfect passive indicative of <em>stauroo</em>, stands crucified, with the ethical dative. This is one of the great sayings of Paul concerning his relation to Christ and to the world.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"15": {
"synthesis": "<p>In Christ Jesus neither circumcision nor uncircumcision avails anything, but only a new creation. This verse reprises and deepens 5:6, now grounding the dissolution of ritual distinctions in the eschatological reality of the new creation. Barnes states it directly: the fact that a man is created anew, or born again, constitutes the real difference between him and all other men; not conformity to rites, not elevated rank, not ethnicity or complexion, but the grand question is whether a man is created anew by the Spirit of God. Wesley is equally direct: neither is of any account; but a new creation, whereby all things in us become new. Robertson simply cross-references 2 Corinthians 5:17, where Paul unfolds the same theme. Ellicott observes that this verse serves as the theological basis for the benediction of verse 16: those who walk by this rule, the rule that only new creation matters, receive peace and mercy.</p>",
"voices": [
{"src": "barnes", "attr": "Barnes", "html": "<p>The fact that a man is created anew, or born again, constitutes the real difference between him and other men. This is what Christ requires; this is the distinction which he designs to make. Not by conformity to certain rites, not by elevated rank, or wealth, or blood, but: are you created anew by the Spirit of God?</p>"},
{"src": "ellicott", "attr": "Ellicott", "html": "<p>This verse serves as the doctrinal foundation for the benediction of verse 16. Those who walk by this rule, accepting that only new creation matters and that all ritual distinctions have been dissolved, are the ones upon whom peace and mercy rightfully rest.</p>"},
{"src": "wesley", "attr": "Wesley", "html": "<p>For neither circumcision is anything, nor uncircumcision; neither of these is of any account. But a new creation, whereby all things in us become new, is the only thing that counts in the kingdom of God and before his throne.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"16": {
"synthesis": "<p>Peace and mercy to all who walk by this rule, and upon the Israel of God. The phrase <em>Israel of God</em> has generated significant discussion: does it refer to ethnic Jews who believe, or to all believers as the true Israel? Barnes reads it as the true church of God, all who are his true worshippers, citing Romans 2:28-29 and Romans 9:6. Wesley identifies it as the church consisting of all those, and those only, of every nation and kindred, who walk by this rule, glorying only in the cross and walking as a new creation. Ellicott and Clarke tend toward distinguishing the believing Gentiles from a subset of Jewish believers as the Israel of God. Calvin's implicit view runs throughout the epistle that the Gentile churches are the true heirs of Abraham. The benediction itself echoes Numbers 6:26, applying Israel's covenant blessing to the new covenant community defined not by ethnicity but by the rule of the new creation.</p>",
"voices": [
{"src": "barnes", "attr": "Barnes", "html": "<p>The true church of God; all who are his true worshippers. Romans 2:28-29; Romans 9:6. Peace be on them, and upon the Israel of God: the blessing invokes the Aaronic benediction of Numbers 6:26 and applies it to the community defined by faith and the new creation, not by ethnic descent.</p>"},
{"src": "wesley", "attr": "Wesley", "html": "<p>And as many as walk according to this rule, glorying only in the cross of Christ, being crucified to the world, and created anew: peace and mercy be upon them, and upon the Israel, that is the Church, of God, which consists of all those, and those only, of every nation and kindred, who walk by this rule.</p>"},
{"src": "ellicott", "attr": "Ellicott", "html": "<p>The Israel of God most naturally refers to Jewish believers, distinguished from Gentile converts as a subset of those who walk by this rule. The benediction then encompasses the full community of faith across both groups, united under the same principle of new creation in Christ.</p>"}
],
"consensus": "mixed",
"key_tension": "Commentators divide on whether the Israel of God designates all believers as spiritual Israel or specifically Jewish believers within the broader church."
},
"17": {
"synthesis": "<p>Paul closes with a personal appeal: from henceforth let no one cause him trouble, for he bears in his body the marks of the Lord Jesus. Barnes is uncertain about what specific trouble Paul references but thinks the context suggests molestation about his apostolic call and authority to explain the gospel without the law. Wesley reads it as a desire for peace from unnecessary quarrels and disputes: afflictions should not be added to the afflicted. Robertson provides the richest comment on <em>ta stigmata</em>: slaves had the names or stamp of their owners on their bodies; soldiers too; devotees stamped themselves with the names of gods they served. Paul bears the wounds of imprisonment and beatings, the physical evidence that he belongs entirely to Jesus, not to Caesar, not to the synagogue, not to his own reputation. Calvin sees in the stigmata the conclusive proof of Paul's consistency: a man who courts popularity would not collect these marks.</p>",
"voices": [
{"src": "calvin", "attr": "Calvin", "html": "<p>Paul appeals to the marks of the Lord Jesus which he bears in his body as conclusive proof that he does not preach circumcision to please men. A man who courts popularity does not collect such marks; these wounds are the evidence of his consistent fidelity to the gospel of the cross.</p>"},
{"src": "wesley", "attr": "Wesley", "html": "<p>From henceforth let none trouble me by quarrels and disputes. For I bear, and afflictions should not be added to the afflicted, in my body the marks of the Lord Jesus, the scars, marks, and brands of my sufferings for him which identify whose slave I am.</p>"},
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>The marks of Jesus: <em>ta stigmata tou Iesou</em>. Old word from <em>stizo</em>, to prick, to stick, to sting. Slaves had the names or stamp of their owners on their bodies; soldiers likewise; devotees stamped upon their bodies the names of their gods. Paul bore the wounds of beatings and imprisonments as proof of ownership by Christ.</p>"}
],
"consensus": "affirm",
"key_tension": null
},
"18": {
"synthesis": "<p>The epistle closes as it opened, with grace: the grace of our Lord Jesus Christ be with your spirit, brethren. Despite the severity of his arguments and the sharpness of his rebukes throughout, Paul ends by calling the Galatians <em>brethren</em>, a word of undiminished affection. Robertson notes that the farewell salutation is much briefer than that of 2 Corinthians 13:13 but identical with that of Philemon 1:25, and that the address <em>brethren</em> is striking in light of all the sharp things spoken. The singular <em>your spirit</em> addresses them as a corporate person, a single community constituted by the one Spirit. Barnes connects it to Romans 16:20 and 2 Timothy 4:22. Wesley gives no separate comment, and the benediction requires none: all the polemics, all the arguments, all the warnings resolve in a prayer for the grace of Christ to be with them. The letter that threatened, reasoned, pleaded, and warned closes in blessing.</p>",
"voices": [
{"src": "rwp", "attr": "Robertson (RWP)", "html": "<p>The farewell salutation is much briefer than that in 2 Corinthians 13:13, but identical with that in Philemon 1:25. He calls them brethren in spite of the sharp things spoken to them. The singular <em>your spirit</em> addresses the community as a whole person gathered into one by the Spirit.</p>"},
{"src": "barnes", "attr": "Barnes", "html": "<p>Brethren, the grace of the Lord Jesus Christ be with your spirit. Comparable to Romans 16:20 and 2 Timothy 4:22. All the arguments, warnings, and rebukes of the epistle resolve into this single prayer: may grace be with you. That is Paul's final word to those he loves.</p>"},
{"src": "clarke", "attr": "Clarke", "html": "<p>The apostle ends with the same grace with which the epistle opened: the grace of our Lord Jesus Christ. Despite all the severity of his reproofs, the letter breathes the spirit of a father, and closes with the tenderness of one who has spoken hard things only because he loves those to whom he speaks.</p>"}
],
"consensus": "affirm",
"key_tension": null
}
}
}
''')


def main():
    existing = load_synthesis('galatians')
    merge_synthesis(existing, GALATIANS)
    save_synthesis('galatians', existing)

    total = sum(len(v) for v in GALATIANS.values())
    print(f'Galatians 5-6 synthesis complete: {total} verses written.')
    ch5 = len(GALATIANS['5'])
    ch6 = len(GALATIANS['6'])
    print(f'  ch5: {ch5} verses, ch6: {ch6} verses')

    print('\nVerification checks:')
    data = load_synthesis('galatians')
    for ch, expected in [('5', 26), ('6', 18)]:
        if ch in data:
            count = len(data[ch])
            print(f'  ch{ch}: {count} verses in file (expected {expected})')
        else:
            print(f'  ch{ch}: MISSING from output file')

    print('\nVoice word counts (flagging < 35 words):')
    for ch in ['5', '6']:
        for v in sorted(GALATIANS[ch].keys(), key=int):
            for voice in GALATIANS[ch][v]['voices']:
                import re
                words = len(re.findall(r'\w+', voice['html']))
                if words < 35:
                    print(f'  WARN: ch{ch}v{v} {voice["src"]}: {words} words')


if __name__ == '__main__':
    main()
