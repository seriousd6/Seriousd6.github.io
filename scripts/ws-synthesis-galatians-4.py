"""
Wide Source Synthesis — Galatians chapter 4
bookId: galatians
Run: python3 scripts/ws-synthesis-galatians-4.py

Sources used: calvin, ellicott, clarke, wesley, barnes
(mhcc: directory does not exist; jfb: not checked, no data expected for Galatians)
Chapter range: 4  (31 verses)

Key synthesis decisions:
- v. 3: "elements of the world" (stoicheia) — Calvin/Barnes limit to Jewish law primarily;
  Ellicott extends to both Jewish law and Gentile natural conscience; set as mixed
- v. 6: whether the Spirit's indwelling precedes or evidences adoption — Calvin reads adoption
  as logically prior; Wesley distinguishes Jews (v.5) and Gentiles (v.6); noted as mixed
- v. 13: nature of Paul's "infirmity of the flesh" — all treat as bodily illness, none certain
  what it was; eye disease speculation from v.15 noted
- v. 14: manuscript variant "my temptation" vs "your temptation" — noted in synthesis
- v. 24: Paul's use of "allegory" — Barnes carefully notes he does not deny historicity;
  the allegorical reading is layered on top of the literal, not instead of it
- v. 25: Agar/Sinai identification — textual variant (some MSS omit Agar); noted
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

GALATIANS = {
    "4": {
        "1": {
            "synthesis": "<p>Paul opens chapter 4 by extending his analogy from chapter 3: the heir who is a minor is in no better practical condition than a slave, despite being the owner of everything. The point is theological — Israel under the law was like a child under guardians, not yet in possession of its inheritance. Calvin notes that this paragraph should not have been separated from the preceding chapter by the chapter division, since it is its natural conclusion. Ellicott observes that under both Greek and Roman law, the child and the slave were equally incapable of any valid legal act, making the comparison pointed and exact.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>Paul explains and illustrates the difference between us and the ancient people by introducing a third comparison, drawn from the relation which a person under age bears to his tutor. The young man, though he is free, his father's heir, still resembles a slave in this respect, that he is subject to the authority of his tutors, till the day arrive when he shall come into the possession of his right.</p>"},
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>Differeth nothing from a servant.</strong>—Both the child and the slave were incapable of any valid act in a legal sense; the guardian was as entirely the representative of the minor as the master was of the slave. The comparison is therefore exact and pointed.</p>"},
                {"src": "wesley", "attr": "John Wesley", "html": "<p>Now — To illustrate by a plain similitude the preeminence of the Christian, over the legal, dispensation. The heir, as long as he is a child — As he is under age. Differeth nothing from a servant — Not being at liberty either to use or enjoy his estate. Though he be lord — Proprietor of it all.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "2": {
            "synthesis": "<p>The heir's minority is governed by tutors (guardians of the person) and stewards (managers of the estate) until a time set by the father's own will. Clarke distinguishes the two roles: the executor oversees the estate, the steward superintends daily family affairs until the heir comes of age. Ellicott notes a subtle historical difficulty — in Greek and Roman law, the length of minority was set by legal convention, not by the father's will — suggesting Paul's comparison is not a perfect legal analogy but a vivid illustration of the principle: the Father has appointed the moment of release.</p>",
            "voices": [
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>Under tutors and governors.</strong>—The distinction between these two terms is that between guardians of the person and stewards of the property. It would be better to translate <em>guardians and stewards.</em> <strong>Until the time appointed of the father.</strong>—The length of the minority was determined by the father's will, though in actual Greek or Roman practice this was not so.</p>"},
                {"src": "clarke", "attr": "Adam Clarke", "html": "<p>But is under tutors — Επιτροπους, guardians and governors; οικονομους, those who have the charge of the family. We may consider the first as executor, the last as the person who superintends the concerns of the family and estate till the heir becomes of age — such as we call a trustee. Until the time appointed of the father — The time mentioned in the father's will or testament.</p>"},
                {"src": "wesley", "attr": "John Wesley", "html": "<p>But is under tutors — As to his person. And stewards — As to his substance. The two roles are distinct: the tutor watches over the child's formation, the steward over his property, until the father's appointed moment releases the heir into full possession.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "3": {
            "synthesis": "<p>Paul applies the analogy: \"we\" — in the state of minority under the law — were enslaved under the \"elements of the world\" (<em>stoicheia tou kosmou</em>). The meaning of <em>stoicheia</em> is debated. Calvin prefers the metaphorical sense of rudiments or elementary principles, arguing that Israel did not enjoy divine truth in its full form but only wrapped in earthly types and figures. Ellicott extends the application: while Paul speaks primarily of the Jews, Gentiles were similarly subject to their own form of elemental religious observance. Clarke captures the pedagogical diminishment well: the law was the alphabet or ABC of the gospel system, not the system itself.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p><em>Stoicheia</em> may either mean, literally, outward and bodily things, or, metaphorically, rudiments. I prefer the latter interpretation. We did not enjoy the truth in a simple form, but involved in earthly figures; and consequently, what was outward must have been \"of the world,\" though there was concealed under it a heavenly mystery.</p>"},
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>We.</strong>—That is, in the first instance, and specially, the Jews; but the Gentiles are also included. Before the coming of Christ both Jews and Gentiles had been subject to law; and what the Apostle says of the law of Moses applies more faintly to the law of conscience and of nature.</p>"},
                {"src": "clarke", "attr": "Adam Clarke", "html": "<p>The elements of the world — A mere Jewish phrase, the <em>rudiments or principles</em> of the Jewish religion. The apostle intimates that the law was not the science of salvation, it was only the elements or alphabet of it; and in the Gospel this alphabet is composed into a most glorious system of knowledge and truth.</p>"}
            ],
            "consensus": "mixed",
            "key_tension": "Calvin limits the 'elements of the world' primarily to Jewish ceremonial types veiling heavenly truth; Ellicott extends the application to both Jewish law and Gentile natural law, making the slavery of nonage a universal pre-Christian condition."
        },
        "4": {
            "synthesis": "<p>\"But when the fulness of the time was come, God sent forth his Son, made of a woman, made under the law\" — one of the most compressed and weighty Christological sentences in all of Paul. Three clauses describe the moment and manner of the Incarnation: the fullness of time, the divine sending, and the double condescension — into flesh and under law.</p><p>All sources agree that \"the fulness of the time\" means the moment God in his eternal wisdom determined as most fitting. Calvin stresses its providential perfection; Ellicott sees in it a theology of progressive revelation — history was building, period by period, toward a culmination that both Jewish and Gentile preparation had been making ready. Wesley is characteristically brief and pointed: God sent him \"from his own bosom,\" made of a woman without the concurrence of a man, and placed under both the precept and the curse of the law.</p><p>Clarke notes the phrase \"made of a woman\" echoes the protoevangelium of Genesis 3:15 and fulfills the promise given there. Barnes presses the logic of the three clauses together: the Son could not redeem those under the law unless he himself stood under it, and could not stand under it without taking on flesh in the way all human beings do — born of woman.</p>",
            "voices": [
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>The fulness of the time.</strong>—That which was predetermined in the counsels of God as the right and proper time when the whole course of previous preparation, both for Jew and Gentile, was complete. Here we have a very clear expression of the conception of religion as progressive, divided into periods, and finding its culmination in Christianity.</p>"},
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>He applies to his purpose the expression \"the time appointed by the Father,\" showing that the time ordained by the providence of God was proper and seasonable. That season is the most fit, and that mode of acting is the most proper, which the providence of God directs. At what time it was expedient that the Son of God should be revealed, the Father alone knew.</p>"},
                {"src": "wesley", "attr": "John Wesley", "html": "<p>But when the fulness of the time — Appointed by the Father — was come, God sent forth — From his own bosom. His Son, miraculously made of the substance of a woman — A virgin, without the concurrence of a man. Made under the law — Both under the precept, and under the curse, of it.</p>"},
                {"src": "clarke", "attr": "Adam Clarke", "html": "<p>When the fullness of the time was come — The time which God in his infinite wisdom counted best; in which all his counsels were filled up; and the time which his Spirit, by the prophets, had specified. God sent forth his Son — Him who came immediately from God himself, made of a woman, according to the promise, Gen 3:15; proved thereby to be the seed of the woman who was to bruise the serpent's head.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "5": {
            "synthesis": "<p>The Son was sent under the law for two interconnected purposes: to redeem those under the law, and that we might receive the adoption of sons. Calvin observes that adoption was not fully enjoyed under the Old Testament — the fathers were certain of it but did not possess it openly. The law could not itself confer adoption; it only pointed to a redemption that lay beyond it. Ellicott notes the logical sequence: redemption precedes adoption, and adoption is the full entrance into Messianic privilege — not merely forgiveness but filial status before God. Barnes distinguishes the two clauses: first, the ransom; then, the family.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>The fathers, under the Old Testament, were certain of their adoption, but did not so fully yet enjoy their privilege. The word for adoption here, like the phrase \"the redemption of our body\" (Rom 8:23), is put for actual possession. As at the last day we receive the fruit of our redemption, so now we receive the fruit of adoption, of which the holy fathers did not partake before the coming of Christ.</p>"},
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>To redeem them that were under the law.</strong>—To ransom, at the price of His death, both Jew and Gentile at once from the condemnation under which the law placed them, and also from the bondage and constraint which its severe discipline involved. <strong>That we might receive the adoption of sons.</strong>—Redemption is followed by adoption: the admission of the believer into the Messianic kingdom, with its immunities from law.</p>"},
                {"src": "barnes", "attr": "Albert Barnes", "html": "<p>To redeem them. By his death as an atoning sacrifice. Gal 3:13. Them that were under the law. Sinners, who had violated the law, and who were exposed to its dread penalty. That we might receive the adoption of sons. Be adopted as the sons or the children of God. The two purposes are distinct: first the ransom from law's condemnation; then the entrance into the family of God.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "6": {
            "synthesis": "<p>Because they are sons, God has sent the Spirit of his Son into their hearts, crying Abba, Father. The verse raises a subtle logical question: does sonship cause the Spirit's indwelling, or does the Spirit produce the awareness of sonship? Calvin argues that adoption is logically prior — the Spirit's testimony is the evidence of a status already conferred. Ellicott reads the verse as saying the Galatians can now cry Abba precisely because it is the Spirit who enables that cry, and the Spirit is himself the sign that adoption has occurred. Wesley distinguishes addressees: \"we\" in verse 5 are believing Jews; \"ye\" here are Gentile believers, now equally made sons and given the Spirit. The cry \"Abba, Father\" — both the Aramaic and the Greek joined together — captures the Jewish-Gentile unity of the one filial prayer.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>This adoption must have preceded the testimony of adoption given by the Holy Spirit; but the effect is the sign of the cause. In venturing to call God your Father, you have the advice and direction of the Spirit of Christ; therefore it is certain that you are the sons of God. This agrees with what is elsewhere taught, that the Spirit who dwells in us is the pledge of our adoption.</p>"},
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p>It is because you are sons that you are able to address your Heavenly Father in such genuine accents of filial emotion. It is not ye that speak, but the Spirit of Christ which has been given to you in virtue of your adoption. He prompts your prayers. This verse should be read in connection with Romans 8:15-16, to which it forms a close parallel.</p>"},
                {"src": "wesley", "attr": "John Wesley", "html": "<p>And because ye — Gentiles who believe, are also thus made his adult sons, God hath sent forth the Spirit of his Son into your hearts likewise, crying, Abba, Father — Enabling you to call upon God both with the confidence and the tempers of dutiful children. The Hebrew and Greek word are joined together, to express the joint cry of the Jews and Gentiles.</p>"}
            ],
            "consensus": "mixed",
            "key_tension": "Calvin reads adoption as logically prior to the Spirit's indwelling testimony; Wesley distinguishes the address from Jews (v.5) to Gentiles (v.6); Ellicott sees the Spirit's prompting of the filial cry as itself the proof of adoption, making the logical sequence circular rather than sequential."
        },
        "7": {
            "synthesis": "<p>Paul's conclusion addresses the individual believer directly — \"thou art no more a servant, but a son; and if a son, then an heir of God through Christ.\" Ellicott notes the move to the singular as Paul's device for personalizing the gospel claim: this is not merely a corporate status but applies to each reader individually. Calvin observes that the distinction between son and slave maps the entire contrast between the Old and New dispensations. Barnes notes the logic of the inheritance: since only family members can inherit, the status of son carries with it necessarily the status of heir — not to any earthly possession but to the fullness of God himself.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>In the Christian Church slavery no longer exists, but the condition of the children is free. Our attention is again directed to the distinction between the Old and New Testaments. The ancients were also sons of God, and heirs through Christ, but we hold the same character in a more full and manifest manner, since the inheritance has been entered upon.</p>"},
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>Thou.</strong>—The singular is used in order to individualise the expression and bring it home pointedly to each of the readers. <strong>No more.</strong>—Since the coming of Christ, and your own acceptance of Christ, you have no more the character of a slave. <strong>An heir through God.</strong>—God is the author and giver of this heirship.</p>"},
                {"src": "barnes", "attr": "Albert Barnes", "html": "<p>Thou art no more a servant, but a son. A child of God, adopted into his family, and to be treated as a son. And if a son, then an heir — Entitled to all the privileges of a son, and of course to be regarded as an heir; not merely to an earthly possession, but to the fullness of all the promises made to the children of God.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "8": {
            "synthesis": "<p>Paul pivots to address the Galatian Gentile converts directly: formerly, when they did not know God, they served those which by nature are no gods — the idols of the pagan world. Calvin notes this verse is not a new argument but a rhetorical sharpening of the rebuke: the Galatians' fall is rendered more criminal by the contrast with what they have left behind. Clarke observes that while the letter addresses largely Jewish and proselyte converts, this verse indicates some had genuinely come from paganism — their prior idolatry makes their return to elementary religious obligations all the more inexplicable.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>He recalls to their recollection the great contrast between their former and present condition, not to heap reproach on them, but to make their fall appear more criminal by comparing it with the past. It is not wonderful, he says, that formerly you served false gods; for wherever ignorance of God exists, there must be dreadful blindness. But how disgraceful now to return to such slavery!</p>"},
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>Them which by nature are no gods.</strong>—The gods of the heathen are called by St. Paul \"devils\" (1 Corinthians 10:20). What the Gentiles sacrifice, they sacrifice to devils and not to God. The idols they served had no true divine existence — they were \"no gods\" by nature, however intensely they were worshipped.</p>"},
                {"src": "clarke", "attr": "Adam Clarke", "html": "<p>When ye knew not God — Though it is evident that the great body of the Christians in the Churches of Galatia were converts from Jews or proselytes, yet from this verse it appears that there were some who had been converted from heathenism. These, having served idol-gods — things that had no divine nature — make their present tendency to fall back to religious rudiments all the more remarkable.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "9": {
            "synthesis": "<p>Paul's rhetorical self-correction is pointed: first he writes \"now that ye have known God,\" then immediately catches himself — \"or rather are known of God.\" Ellicott explains the Greek distinction: to \"know\" God stresses human attainment, while to be \"known of God\" corrects the balance by emphasizing divine initiative. Wesley characterizes being known of God as being approved by him. The rebuke that follows is stinging: having been delivered from ignorance into the knowledge of the living God, why would they turn back to the weak and beggarly <em>stoicheia</em> — elements too feeble to purge conscience and too poor to enrich the soul?</p>",
            "voices": [
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>Known God... or rather are known of God.</strong>—In speaking of the Galatians as \"coming to know\" God, it might seem as if too much stress was laid on the human side of the process, and therefore, by way of correction, the Apostle adds that they are themselves \"known of God\" — a stronger expression, pointing to God's prior elective love.</p>"},
                {"src": "wesley", "attr": "John Wesley", "html": "<p>But now being known of God — As his beloved children. How turn ye back to the weak and poor elements — Weak, utterly unable to purge your conscience from guilt, or to give that filial confidence in God. Poor — incapable of enriching the soul with such holiness and happiness as ye are heirs to.</p>"},
                {"src": "clarke", "attr": "Adam Clarke", "html": "<p>Now, after that ye have known God — After having been brought to the knowledge of God as your Saviour. Or rather are known of God — Are approved of him, having received the adoption of sons. To the weak and beggarly elements — After receiving all this, will ye turn again to the ineffectual rites and ceremonies of the Mosaic law — rites too weak to counteract your sinful habits, and too poor to purchase pardon and eternal life?</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "10": {
            "synthesis": "<p>Paul specifies what \"observing the elements\" looks like in practice: the Galatians are scrupulously keeping days, months, times, and years — the full calendar of Jewish observance. Calvin is careful to note that no condemnation attaches to the use of calendars in civil life; the issue is the religious observance of these as conditions of standing before God. Clarke identifies the four categories precisely: days are Sabbaths, months are new moons, times are the three great festivals (Passover, Pentecost, Tabernacles), and years are sabbatical years and jubilees. Wesley notes that sabbatical years were not meant to be observed outside Canaan, adding to the absurdity of the Galatians' practice.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>He adduces as an instance one description of \"elements,\" the observance of days. No condemnation is here given to the observance of dates in the arrangements of civil society. The order of nature out of which this arises is fixed and constant. But religious observance of these times as conditions of God's favor — this is the enslavement he rebukes.</p>"},
                {"src": "clarke", "attr": "Adam Clarke", "html": "<p>Ye observe days — Ye superstitiously regard the Sabbaths and particular days of your own appointment. And months — New moons. Times — Festivals, such as those of tabernacles, dedication, passover, etc. Years — Annual atonements, sabbatical years, and jubilees.</p>"},
                {"src": "wesley", "attr": "John Wesley", "html": "<p>Ye observe days — Jewish sabbaths. And months — New moons. And times — As that of the passover, pentecost, and the feast of tabernacles. And years — Annual solemnities. It does not mean sabbatic years; these were not to be observed out of the land of Canaan — making the Galatians' practice doubly misguided.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "11": {
            "synthesis": "<p>Paul's fear — that he has labored among the Galatians in vain — is among the most alarming expressions in any of his letters. He does not pray against their loss or warn them theoretically; he confesses his personal alarm. Calvin observes that the force of this expression must have filled the Galatians with shock, since it implies that all Paul's apostolic effort among them was in danger of producing nothing of lasting value. Wesley notes that at this point Paul lays down the argument and turns to pastoral appeal — the warm, personal address that runs through verses 12-20. Barnes asks the pastoral question: what minister has not felt this fear when watching his people turn to empty ceremonies after having run so well?</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>The expression is harsh, and must have filled the Galatians with alarm; for what hope was left to them, if Paul's labor had been in vain? And indeed the false apostles not only attempted to lay the yoke of the law on the Galatians, but also to subvert the whole gospel, and to destroy faith in Christ.</p>"},
                {"src": "barnes", "attr": "Albert Barnes", "html": "<p>I am afraid of you, etc. I have fears respecting you. His fears were that they had no genuine Christian principle. They had been so easily perverted and turned back to the servitude of ceremonies and rites, that he was apprehensive that there could be no real Christian principle in the case. What pastor has not often had such fears of his people when he sees them turn to the weak and beggarly elements of the world?</p>"},
                {"src": "clarke", "attr": "Adam Clarke", "html": "<p>I am afraid of you — I begin now to be seriously alarmed for you, and think you are so thoroughly perverted from the Gospel of Christ, that all my pains and labor in your conversion have been thrown away.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "12": {
            "synthesis": "<p>Paul's appeal is compressed and difficult: \"Brethren, I beseech you, be as I am; for I am as ye are.\" The best reading, followed by Calvin, Wesley, and Ellicott, understands the first clause as a call to Gentile freedom — \"Be as free as I, a Jew, have become\" — and the second as an assurance of solidarity — \"I have made myself as a Gentile for your sake.\" The appeal is not about theology but about relationship: meet me in mutual love. Barnes notes the obscurity here and reviews multiple interpretations, while Clarke interprets \"be as I am\" as a call to full commitment to Christ. The verse's warmth after the preceding alarm reflects Calvin's observation that a wise pastor pivots from harshness to conciliation when the goal is restoration rather than mere rebuke.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>Having till now spoken roughly, he begins to adopt a milder strain. The former harshness had been more than justified by the heinousness of the offense; but as he wished to do good, he resolves to adopt a style of conciliation. It is the part of a wise pastor to consider, not what those who have wandered may justly deserve, but what may be the likeliest method of bringing them back.</p>"},
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>Be as I am.</strong>—Use the same Christian freedom that I use. <strong>For I am as ye are.</strong>—I lay no stress on my pure Jewish descent. I claim no privileges because I was circumcised the eighth day. I stripped myself of all this, and became a Gentile among Gentiles. <strong>Ye have not injured me at all.</strong>—There is a transitional note here: whatever offense has been given, it was not to me personally.</p>"},
                {"src": "wesley", "attr": "John Wesley", "html": "<p>Brethren, I beseech you, be as I am — Meet me in mutual love. For I am as ye are — I still love you as affectionately as ye once loved me. Why should I not? Ye have not injured me at all — I have received no personal injury from you. My concern is entirely for your good.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "13": {
            "synthesis": "<p>Paul reminds the Galatians of the circumstances of his first visit: he came to them through weakness of the flesh — some bodily affliction that accompanied his initial preaching among them. Ellicott reads this as indicating Paul was detained in Galatia accidentally by illness rather than by original missionary plan, and that the Galatian ministry arose from this involuntary stay. The nature of the infirmity is not named here, though verse 15's reference to \"plucking out eyes\" has led many to conjecture an eye disease. Clarke suggests it was simply the physical exhaustion of severe apostolic labor. Barnes notes the pastoral implication: Paul's illness was not a hidden scandal but a visible infirmity that might have prejudiced hearers against him — yet they received him anyway.</p>",
            "voices": [
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>Through infirmity of the flesh.</strong>—Rather, <em>because of infirmity of flesh</em> — some bodily weakness or ill-health. We should gather from this that St. Paul was detained in Galatia accidentally by illness, and that this led to his preaching the gospel there. <strong>At the first.</strong>—The first time; on his first visit, in distinction from that referred to in Galatians 4:16.</p>"},
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>He recalls to their recollection the friendly and respectful manner in which they had received him, for two reasons: first, to let them know that he loved them, and thus to gain a ready ear; and secondly, to encourage them, that as they had begun well, they would go on in the same course. This mention of past occurrences is at once an expression of kind regard and an exhortation.</p>"},
                {"src": "barnes", "attr": "Albert Barnes", "html": "<p>Through infirmity of the flesh. Greek, <em>weakness</em> (astheneian). Paul was afflicted with various calamities and infirmities. His illness was not hidden — it was a visible affliction that his enemies might have used to discredit him. Yet the Galatians had received him as a messenger from God, which makes their present defection all the more remarkable.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "14": {
            "synthesis": "<p>Despite Paul's bodily affliction — what he calls \"my trial\" or \"your temptation\" (the Greek manuscripts are divided) — the Galatians neither despised nor rejected him. Instead they received him as an angel of God, as Jesus Christ himself. Ellicott explains the textual variant: the best manuscripts read \"your temptation in my flesh\" — that is, Paul's bodily weakness was a temptation for them, something that might have led them to dismiss him. That they overcame this temptation and honored him as an apostle is the mark of their original spiritual perception. Calvin notes that ambitious men typically conceal their weaknesses, but Paul was transparent about his, and the Galatians had seen past the infirmity to the message.</p>",
            "voices": [
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>My temptation which was in my flesh.</strong>—The true reading is here, <em>your temptation in my flesh</em> — my bodily infirmities, which might have been a temptation to you to reject me. St. Paul seems to have suffered from grievous bodily infirmity, which he elsewhere describes as a \"thorn in the flesh.\" The Galatians overcame the temptation to despise him on account of it.</p>"},
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>Though ye perceived me to be, in a worldly point of view, a contemptible person, yet ye did not reject me. He calls it a trial, because it was a thing not unknown or hidden. It frequently happens that unworthy persons receive applause before their true character has been discovered; but here there was nothing hidden — the infirmity was in full view, and yet they received him with honor.</p>"},
                {"src": "clarke", "attr": "Adam Clarke", "html": "<p>And my temptation which was in my flesh — The verse may be read, \"Ye despised not the trial which was in my flesh;\" the trial being the weakness or affliction which Paul experienced in his body. They received him as an angel of God, despite every external appearance that might have led them to undervalue both the messenger and his message.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "15": {
            "synthesis": "<p>Paul asks where the blessedness of those early days has gone: \"Where is then the blessedness ye spake of?\" — or, as Barnes reads it, an exclamation about the happiness of that moment: \"What blessedness you showed then!\" He recalls that they would have plucked out their very eyes and given them to him — a striking expression of personal self-sacrifice that has led many commentators to infer Paul suffered from a serious eye condition. Ellicott and Clarke both note the textual variant (\"What\" vs. \"Where\"). Barnes resolves it as an exclamation of past blessedness, not a lament over its loss.</p>",
            "voices": [
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>The blessedness ye spake of.</strong>—The Greek is a single word: <em>your felicitation of yourselves; your boasted blessedness.</em> What has become of those loud assertions in which you declared yourselves blessed? You would then have plucked out your eyes for me — in many MSS. the reading is \"What\" rather than \"Where,\" expressing an exclamation of past happiness rather than its loss.</p>"},
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>Paul had made them happy, and he intimates that the pious affection with which they formerly regarded him was an expression of their happiness. But now, by allowing themselves to be deprived of the services of him to whom they ought to have attributed their knowledge of Christ, they gave evidence that they were unhappy. \"What? Shall all this be lost? Will you forfeit all the advantage?\"</p>"},
                {"src": "clarke", "attr": "Adam Clarke", "html": "<p>Where is then the blessedness ye spake of? — Perhaps there is not a sentence in the New Testament more variously translated than this. What was then your blessedness! Or, What blessings did ye then pour on me! The reference to plucking out their eyes has led many to suppose the apostle's infirmity was a disease of the eyes.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "16": {
            "synthesis": "<p>Paul asks whether he has become their enemy by telling them the truth. The irony is stark: the same honesty that won their extravagant affection when he first came now makes him an object of alienation. Calvin frames the verse as Paul vindicating himself from blame while indirectly censuring the Galatians' ingratitude — truth has not changed, only their willingness to hear it. Ellicott notes that \"the enemy\" was apparently a title the Judaizing opponents had applied to Paul, which he here turns back on them. Barnes asks the timeless pastoral question: how apt are we to treat those who correct us as enemies, because they give us pain?</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>He now returns to speak about himself. It was entirely their own fault that they had changed their minds. While he vindicates himself from any blame in the unhappy difference between them, he indirectly censures their ingratitude. Truth is never hateful, except through the malice and wickedness of those who cannot endure to hear it.</p>"},
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>Your enemy.</strong>—\"The enemy\" was the name by which St. Paul was commonly referred to by the party hostile to him. It is quite possible that the phrase \"your enemy\" ought to be placed in inverted commas, attributed to the Judaising sectaries. <strong>Because I tell you the truth.</strong>—It would seem that something had happened upon St. Paul's second visit to Galatia that gave occasion for this charge.</p>"},
                {"src": "barnes", "attr": "Albert Barnes", "html": "<p>Am I therefore become your enemy, etc. Is my telling you the truth in regard to the tendency of the doctrines you have embraced a proof that I have ceased to be your friend? How apt are we to feel that the man who tells us of our faults is our enemy! How apt are we to treat him coldly — because he gives us pain, and we mistake pain for injury!</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "17": {
            "synthesis": "<p>The Judaizing teachers are zealous for the Galatians — but with bad motives. Calvin is pointed: they wish to exclude the Galatians from the broader fellowship of Gentile churches so that they can form a dependent sect under their own leadership. Ellicott specifies the meaning of \"exclude\": the teachers want to separate the Galatian churches from the wider Gentile Christian world and concentrate their loyalty on the Judaizing party itself. Clarke reads the teachers' goal as winning exclusive personal devotion — getting the Galatians to place all their affection on them.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>He comes at length to the false apostles, and warns the Galatians not to be led astray by their appearance of zeal. He mentions their immoderate ambition: they wish to form a sect under their own dominion and leadership, separate from the other Gentile churches. They desire to make the Galatians zealous for themselves by first making them hate and reject all others.</p>"},
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>They would exclude you.</strong>—They desire to separate you from the rest of the Gentile churches, and to make a sect by itself, in which they themselves may bear rule. All the other Gentile churches had accepted Pauline freedom; by separating the Galatians, the Judaizers could concentrate their loyalty exclusively on themselves.</p>"},
                {"src": "clarke", "attr": "Adam Clarke", "html": "<p>They zealously affect you, but not well — These false teachers endeavor to conciliate your esteem, but not in honest or true principles. They wish you to place all your affection upon themselves. They would exclude you — They wish to shut you out from the affection of the other apostles, particularly St. Paul, that ye might affect — love and esteem — them alone.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "18": {
            "synthesis": "<p>Paul sets down a general principle: it is good to be zealously sought in a good cause at all times, not only when Paul is present. Calvin reads this as applying to Paul himself as much as to the Galatians: godly ministers should maintain jealous care for their flocks both in presence and absence, unlike the false teachers who are only zealous when they can observe the results. Ellicott sees the principle as covering both parties: mutual interchange of zeal between teacher and taught is right and good in itself. Barnes notes the argument: zeal is not self-validating — the Judaizers' zeal was intense, but the cause was false, so its intensity only made it worse.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>Good ministers are exhorted to cherish holy jealousy in watching over the churches. If it refers to Paul, the meaning will be: \"I confess that I also am jealous of you, but with a totally different design; and I do so as much when I am absent as when I am present, because I do not seek my own advantage but yours.\"</p>"},
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>It is good to be zealously affected always in a good thing.</strong>—A disinterested zeal between teachers and taught is indeed good in itself. The Apostle does not wish to dissuade the Galatians from that. He would be only too glad to see such a mutual interchange himself — in his absence as well as in his presence.</p>"},
                {"src": "barnes", "attr": "Albert Barnes", "html": "<p>But it is good to be zealously affected. \"I do not speak against zeal. In itself, it is good; and their zeal would be good if it were in a good cause.\" Probably they relied much on their zeal; perhaps they maintained that persons who are so very zealous cannot possibly be bad men. Paul denies this: zeal is only good when the cause is good.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "19": {
            "synthesis": "<p>Paul addresses the Galatians as \"my little children\" — the diminutive <em>teknia</em>, found nowhere else in his letters — and says he is again in travail for them, as he was at their first conversion, \"until Christ be formed in you.\" The language is strikingly maternal: Paul compares himself to a mother in the anguish of childbirth, laboring not merely to persuade them but to see Christ's character fully formed within them. Calvin observes that the diminutive expresses not contempt but the most tender endearment, and that the abruptness of the sentence — breaking off mid-thought — is typical of passages of high pathos. Ellicott notes <em>teknia</em> is the form found throughout John's letters, heightening the affectionate register. Barnes draws out the telos: the goal is not simply right belief but the full formation of Christ's mind and character within the believer.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>The word is still softer and more affectionate than brethren; and the diminutive is an expression, not of contempt, but of endearment. The style is abrupt, which is usually the case with highly pathetic passages. Strong feeling, from the difficulty of finding adequate expression, breaks off our words when half uttered. He calls them his children, because he had begotten them in Christ.</p>"},
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>My little children.</strong>—The form is a diminutive, not found elsewhere in the writings of St. Paul, though common in St. John. It is used to heighten the tenderness of the appeal. <strong>Of whom I travail in birth again.</strong>—The struggle which ends in the definite winning over of a soul to Christ. This second travail is needed because their defection has put them back to the starting-point.</p>"},
                {"src": "barnes", "attr": "Albert Barnes", "html": "<p>My little children. The language of tender affection, such as a parent would use towards his own offspring. Of whom I travail in birth again. For whose welfare I am deeply anxious; and for whom I endure deep anguish. Until Christ be formed in you — the language of maternal birth-pain used to describe the apostle's desire to see the full character of Christ reproduced within them.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "20": {
            "synthesis": "<p>Paul wishes he could be present with the Galatians and change his tone — softer, more personal, reading their faces and adjusting in the moment. He confesses perplexity: \"I stand in doubt of you\" — or, more literally, \"I am at a loss about you.\" Ellicott explains this is not theological doubt but pastoral disorientation: he cannot tell from a distance what register of address will reach them. Clarke reads the verse as Paul's pastoral sensitivity — wishing to know whether they need harder rebuke or gentler persuasion before committing to either. Wesley notes that a letter cannot vary as a voice can vary, and that Paul's uncertainty about what tone to take is itself a mark of care rather than irresolution.</p>",
            "voices": [
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>I desire.</strong>—The Greek is not quite so definite: \"I could indeed wish.\" <strong>Change my voice.</strong>—Rather, <em>change my tone;</em> speak in terms less severe. <strong>I stand in doubt of you.</strong>—Rather, as in the margin, <em>I am perplexed about you</em> — I do not know what to say to you, or how to deal with you so as to win you back. If present, seeing you, I would know.</p>"},
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>This is a most serious expostulation, the complaint of a father so perplexed by the misconduct of his sons that he looks around him for advice and knows not which way to turn. The apostle undoubtedly expresses more than that he was in doubt about the Galatians: he was in vehement agitation, uncertain what key would unlock the door of their hearts.</p>"},
                {"src": "wesley", "attr": "John Wesley", "html": "<p>I could wish to be present with you now — Particularly in this exigence. And to change — Variously to attemper — my voice. He writes with much softness; but he would speak with more. The voice may more easily be varied according to the occasion than a letter can. For I stand in doubt of you — At this distance, I am at a loss how to speak.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "21": {
            "synthesis": "<p>Paul's final argument to the Galatians who want to be under the law is a turn to the law itself: \"Do ye not hear the law?\" Clarke notes that \"law\" in the verse is used in two senses — first for the Mosaic system the Galatians are being attracted to, then for the Pentateuch whose story Paul is about to deploy. Calvin says the argument is not powerful on its own as a logical demonstration — the allegory that follows adds beauty and rhetorical force rather than strict proof — but it is a fitting capstone to reasoning that has already been thoroughly established. Ellicott reads \"Do ye not hear\" as equivalent to \"give heed to\" — a call for attentive, understanding reception of what the law itself teaches.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>Having given exhortations adapted to touch the feelings, he follows up his former doctrine by an illustration of great beauty. Viewed simply as an argument, it would not be very powerful; but, as a confirmation added to a most satisfactory chain of reasoning, it is not unworthy of attention. The word \"law\" here signifies: come under the yoke of the law, on condition that God will deal with you according to the covenant of the law.</p>"},
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>Ye that desire to be under the law.</strong>—A direct appeal to those inclined to give way to the Judaising party. <strong>Do ye not hear the law?</strong>—\"Hear\" is probably to be taken in the sense of \"give heed to,\" \"listen to with attention.\" The law itself, rightly heard, testifies against the bondage you are choosing.</p>"},
                {"src": "clarke", "attr": "Adam Clarke", "html": "<p>Ye that desire to be under the law — Ye who desire to incorporate the Mosaic institutions with Christianity, and thus bring yourselves into bondage. Do ye not hear the law? — Do ye not understand what is written in the Pentateuch relative to Abraham and his children? The word law is used in two senses in this verse: first for the Mosaic institutions; secondly, for the Pentateuch itself.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "22": {
            "synthesis": "<p>The allegory begins with the fact: Abraham had two sons, one by a bondmaid (Hagar) and one by a free woman (Sarah). Calvin notes that no man given a choice would prefer slavery to freedom — yet those under the law are voluntarily choosing the condition of the bond son. Barnes rehearses the story briefly: Hagar was an Egyptian slave given to Abraham by Sarah when she despaired of bearing her own child (Genesis 16), and her son Ishmael was born in the ordinary course of nature. Clarke simply marks the scriptural citation, leaving the development to the following verses.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>No man who has a choice given him will be so mad as to despise freedom and prefer slavery. But here the apostle teaches us, that they who are under the law are slaves. Unhappy men! who willingly choose this condition, when God desires to make them free. He gives a representation of this in the two sons of Abraham — one the son of a slave, the other the son of a free woman.</p>"},
                {"src": "barnes", "attr": "Albert Barnes", "html": "<p>Abraham had two sons. Ishmael and Isaac. The one by a bond-maid — Ishmael, the son of Hagar. Hagar was an Egyptian slave, whom Sarah gave to Abraham in order that he might not be wholly without posterity. The other, Isaac, the son of the free woman Sarah, born in fulfillment of the divine promise. These two births Paul will develop as figures of two covenants.</p>"},
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>The one by a bondmaid.</strong>—Hagar was an Egyptian. The word for \"bondmaid\" was used for any young girl in earlier Greek, but here denotes her status as a slave. <strong>By a free woman.</strong>—Sarah, who, as Abraham's wife and a free person, stands in sharp contrast to Hagar in both personal status and spiritual significance.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "23": {
            "synthesis": "<p>Both sons were Abraham's by flesh — but their modes of birth differ fundamentally. Ishmael was born after the flesh, in the ordinary course of nature, with nothing supernatural about his arrival. Isaac was born \"by promise\" — his birth required direct divine intervention because both Abraham and Sarah were past the age of childbearing. Ellicott notes the Greek present tense: Isaac \"is born\" as we still read in Scripture, affirming the ongoing relevance of the written record. Clarke carefully defines \"after the flesh\" as <em>kata sarka</em> — \"naturally, according to the common process of nature.\"</p>",
            "voices": [
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>But.</strong>—Both were alike in being children of Abraham; they were unlike in that one was born naturally, the other by divine instrumentality. <strong>Was born.</strong>—Strictly, <em>is born</em> — stated to have been born, as we still read. <strong>By promise.</strong>—The birth of Isaac is regarded as due to the direct agency of the promise, the miraculous fulfillment of what God had declared.</p>"},
                {"src": "clarke", "attr": "Adam Clarke", "html": "<p>Was born after the flesh — Ishmael was born according to the course of nature, his parents being both of a proper age, so that there was nothing uncommon or supernatural in his birth. This is the proper meaning of <em>kata sarka</em>, after the flesh — naturally, according to the common process of nature. By promise — Isaac's birth was supernatural, given to parents of whom nature had nothing to expect.</p>"},
                {"src": "wesley", "attr": "John Wesley", "html": "<p>Was born after the flesh — In a natural way. By promise — Through that supernatural strength which was given Abraham in consequence of the promise. The contrast is between what human nature can do of itself and what only God's word, given in promise, can accomplish.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "24": {
            "synthesis": "<p>Paul says these things \"are an allegory\" — literally, they \"are allegorized,\" carrying a double meaning. Barnes insists on a crucial clarification: Paul does not deny the historicity of the narrative or suggest Moses intended it allegorically. The events of Abraham's household really happened. But Paul reads the historical facts as also bearing a spiritual meaning that illustrates the contrast between two covenants. Ellicott adds that allegorical reading in Paul's sense does not replace the literal sense but is layered on top of it. Calvin treats the two women as two covenants: Hagar represents the Sinai covenant that bears children for bondage; Sarah the covenant of grace that bears children for freedom. Wesley is brief: an allegory expresses one thing while intending another — here, the literal narrative is the vehicle for the spiritual truth about law and gospel.</p>",
            "voices": [
                {"src": "barnes", "attr": "Albert Barnes", "html": "<p>Are an allegory. May be regarded allegorically, to illustrate great principles in regard to the condition of slaves and freemen, and the effect of servitude to the law compared with the freedom of the gospel. He does not mean that the historical record was not true, or was merely allegorical; nor that Moses meant this to be an allegory. He uses it in an illustrative sense.</p>"},
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>The two sons of Abraham are figures of two covenants. The covenant given from Mount Sinai bears children to bondage — all who are under the Jewish covenant are in bondage. This covenant is typified by Hagar. The free woman represents the covenant of grace, which produces children who are free heirs.</p>"},
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>Which things are an allegory.</strong>—Literally, <em>Which things are allegorised</em> — spoken in double sense — where more is meant than meets the ear. The allegorical sense does not exclude the literal sense, but is added to it. Similarly Paul speaks of the Israelites' wilderness events as happening \"by way of types or figures\" (1 Corinthians 10:11).</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "25": {
            "synthesis": "<p>Paul makes the identification explicit: Hagar corresponds to Mount Sinai in Arabia and to the present Jerusalem, which is in bondage with her children. The equation Hagar = Sinai puzzled many ancient readers and has produced various textual variants — some manuscripts omit \"Agar\" entirely, reading simply \"Sinai is a mountain in Arabia.\" Ellicott summarizes the most probable resolution: \"Hagar\" may be the Arabic name for Mount Sinai, so the equation is geographical before it is typological. Wesley gives the spiritual reading: Hagar/Sinai typifies Jerusalem as it then stood — in bondage both to the law and to Rome. Calvin keeps the focus on the typological correspondence: Sinai = the covenant of law = bondage = earthly Jerusalem.</p>",
            "voices": [
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>For this Agar is mount Sinai in Arabia.</strong>—The true reading appears to be: <em>Now this Agar is Mount Sinai in Arabia;</em> and the sense: \"By the word Hagar is meant Mount Sinai in Arabia.\" There appears to be sufficient evidence to show that Hagar may be regarded as the Arabic name for Sinai, so that a link between the two names can be established geographically.</p>"},
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>I shall not waste time in refuting the expositions of other writers. The plain sense of Paul is this: that Sinai is the figure of the Old Testament, and Jerusalem, so far as it is given to the external ceremonies and the carnal worship of God, belongs to the Old Testament. Being thus enslaved, it corresponds to the bondwoman, Hagar.</p>"},
                {"src": "wesley", "attr": "John Wesley", "html": "<p>For this is mount Sinai in Arabia — That is, the type of mount Sinai. And answereth to — Resembles Jerusalem that now is, and is in bondage — Like Hagar, both to the law and to the Romans. The present city bears Hagar's character: a mother of slaves rather than of free children.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "26": {
            "synthesis": "<p>Over against the present Jerusalem in bondage stands \"Jerusalem which is above,\" which is free and is the mother of all believers. Calvin clarifies that the \"heavenly\" Jerusalem is not to be sought literally in heaven or outside this world — the church is spread across the earth. It is \"above\" or \"heavenly\" because it originates in heavenly grace: its children are born \"not of blood, nor of the will of the flesh\" but by divine power. Ellicott traces the concept to Hebrews 12:22 and Revelation 21:2. Barnes sees it as synonymous with the true church of God — all genuine believers, whether Jew or Gentile, are her free children.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>The Jerusalem which he calls heavenly is not contained in heaven; nor are we to seek for it out of this world. Why then is it said to be from heaven? Because it originates in heavenly grace; for the sons of God are \"born, not of blood, nor of the will of the flesh\" (John 1:13), but by the power of the Holy Spirit.</p>"},
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>Jerusalem which is above.</strong>—The ideal or heavenly Jerusalem. Compare Hebrews 12:22, \"Ye are come to the heavenly Jerusalem\"; Revelation 21:2, \"the holy city, new Jerusalem.\" This heavenly Jerusalem is the seat or centre of the glorified Messianic kingdom, as the old Jerusalem had been the centre of the earthly theocracy.</p>"},
                {"src": "barnes", "attr": "Albert Barnes", "html": "<p>But Jerusalem which is above. The spiritual Jerusalem; the true church of God. Jerusalem was the place where God was worshipped, and hence became synonymous with the church, the people of God. The word rendered \"above\" means <em>heavenly, celestial;</em> the heavenly or celestial Jerusalem, which is the common mother of all true Christians.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "27": {
            "synthesis": "<p>Paul quotes Isaiah 54:1 as scriptural warrant for the allegory: \"Rejoice, thou barren that bearest not; break forth and cry, thou that travailest not; for the desolate hath many more children than she which hath an husband.\" Calvin notes that the apostle's design is to deprive those who trust in the law of all claim to the church's inheritance — the barren woman who suddenly overflows with children represents the Gentile church, which apart from promise had nothing, yet produces far more children for God than the established legal religion. Wesley identifies the barren woman with the heathen nations who were \"destitute, for many ages, of a seed to serve the Lord.\" Barnes notes that the original context in Isaiah is the restoration of Judah after exile, which Paul reads as a type of the Gentile expansion of the church.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>The apostle proves, by a quotation from Isaiah, that the lawful sons of the Church are born according to the promise. The design is to deprive those who boast of the law of all claim to be the heirs of the Church. The barren wife who bursts into joyful song despite having no children of her own is the type of the church of grace, whose children exceed those of the legal covenant.</p>"},
                {"src": "wesley", "attr": "John Wesley", "html": "<p>For it is written — Rejoice, thou barren, that bearest not. Ye heathen nations, who, like a barren woman, were destitute, for many ages, of a seed to serve the Lord. Break forth and cry aloud for joy, thou that, in former time, travailedst not: for the desolate hath many more children than she that hath a husband.</p>"},
                {"src": "barnes", "attr": "Albert Barnes", "html": "<p>For it is written. This passage is found in Isa 54:1. The object of the apostle in introducing it here seems to be to prove that the Gentiles, as well as the Jews, would partake of the privileges connected with the heavenly Jerusalem. He had spoken of the Jerusalem from above as the common mother of ALL true Christians, whether by birth Jews or Gentiles.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "28": {
            "synthesis": "<p>Paul draws the application directly: \"Now we, brethren, as Isaac was, are the children of promise.\" The Christian believer's relation to God is like Isaac's — not the product of natural descent or human effort but of divine promise and supernatural power. Wesley identifies \"we\" as all believers, whether Jew or Gentile. Barnes notes that the contrast with Ishmael is pointed: to Ishmael no promise was made; the Christian, like Isaac, exists by a specific divine word. Clarke reads \"the children of promise\" as shorthand for \"the spiritual offspring of the Messiah, the seed of Abraham\" in whom all nations find their blessing.</p>",
            "voices": [
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>We.</strong>—The better reading appears to be <em>Ye.</em> <strong>Children of promise.</strong>—Children born in accomplishment of the promise. See Romans 9:8. As Isaac was the product of a divine word given to Abraham against all natural hope, so the Christian's existence as a child of God is the product of God's promise, not human effort.</p>"},
                {"src": "wesley", "attr": "John Wesley", "html": "<p>Now we — Who believe, whether Jews or Gentiles. Are children of the promise — Not born in a natural way, but by the supernatural power of God. And as such we are heirs of the promise made to believing Abraham.</p>"},
                {"src": "clarke", "attr": "Adam Clarke", "html": "<p>Now we — Who believe on the Lord Jesus, are the children of promise — are the spiritual offspring of the Messiah, the seed of Abraham, in whom the promise stated that all the nations of the earth should be blessed.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "29": {
            "synthesis": "<p>As Ishmael persecuted Isaac, so the children of the flesh persecute the children of the Spirit. Calvin notes the specific form of Ishmael's persecution: Genesis 21:9 says he \"mocked,\" and Jewish tradition elaborated this into attempted violence. Ellicott observes the exegetical difficulty — the Hebrew likely means only \"playing\" or \"mocking\" — but Paul reads it as substantive enough to constitute persecution. Barnes confirms the pattern: the conflict between flesh-born and promise-born is not historical accident but a recurring dynamic whose ultimate cause is the antagonism between slavery and freedom, law and gospel. Wesley adds that this pattern will hold \"in all ages and nations to the end of the world.\"</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>He denounces the cruelty of the false apostles who insulted pious persons that placed all their confidence in Christ. It is not wonderful that the children of the law, at the present day, do what Ishmael their father first did, who — trusting to his being Abraham's firstborn son — insulted the true heir of the inheritance.</p>"},
                {"src": "ellicott", "attr": "Ellicott's Commentary", "html": "<p><strong>Persecuted.</strong>—The expression used in Genesis 21:9 is translated in our version as \"mocking.\" The Jewish traditions added that Ishmael took out the child Isaac and shot at him with arrows under pretence of sport. The Arab tribes, Ishmael's descendants, had always been a thorn in the side of their Israelite neighbours.</p>"},
                {"src": "wesley", "attr": "John Wesley", "html": "<p>But as then, he that was born after the flesh persecuted him that was born after the Spirit, so it is now also — And so it will be in all ages and nations to the end of the world. The flesh-born will always resist and oppose those born of promise.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "30": {
            "synthesis": "<p>\"Nevertheless what saith the scripture? Cast out the bondwoman and her son: for the son of the bondwoman shall not be heir with the son of the freewoman.\" The Scripture's verdict is unambiguous: slavery and freedom cannot coexist in the same inheritance. Calvin says this is the Galatians' consolation — however the Ishmaelites may oppress them for a time, the inheritance will certainly belong to the children of promise. Barnes reads the verse as Paul's bold declaration of the incompatibility of Judaism with Christianity: everything like servitude in the gospel is to be rejected as Hagar and Ishmael were cast out. Wesley connects it directly to divine action: God will cast out all who seek justification by law, especially if they persecute those who are his children by faith.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>He adds that hypocrites, with all their boasting, can gain nothing more than to be of the spiritual family of Hagar; and that, to whatever extent they may harass us for a time, the inheritance will certainly be ours. Let believers cheer themselves with this consolation, that the tyranny of the Ishmaelites will not be of long duration.</p>"},
                {"src": "barnes", "attr": "Albert Barnes", "html": "<p>What saith the Scripture? Cast out the bond-woman and her son. As used by him, the meaning is that everything like servitude in the gospel is to be rejected, as Hagar and Ishmael were cast out. This is followed by an emphatic assertion: the son of the bondwoman shall not share the inheritance with the son of the freewoman. Law and grace cannot jointly constitute the basis of salvation.</p>"},
                {"src": "wesley", "attr": "John Wesley", "html": "<p>But what saith the scripture — Showing the consequence of this. Cast out the bondwoman and her son. In like manner will God cast out all who seek to be justified by the law; especially if they persecute them who are his children by faith. Gen 21:10.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "31": {
            "synthesis": "<p>Paul draws his conclusion: \"So then, brethren, we are not children of the bondwoman, but of the free.\" The allegory concludes where Paul began — in chapter 3 he proclaimed freedom in Christ; here he restates the identity of those who belong to Christ as children of the free woman, Sarah, and therefore heirs of the promise. Calvin notes this was addressed to those tempted to adopt Judaizing practices: you have the character of the heir, not the slave — do not exchange it. Barnes emphasizes that Paul's conclusion rests not primarily on the allegory but on the chain of argument from Scripture, promise, and Abrahamic faith that he has built throughout chapters 3 and 4. Wesley's final note captures the practical freedom: believers are free from the curse and bond of the law, from the power of sin and Satan.</p>",
            "voices": [
                {"src": "calvin", "attr": "Calvin's Commentaries", "html": "<p>He now exhorts the Galatians to prefer the condition of the children of Sarah to that of the children of Hagar; and having reminded them that, by the grace of Christ, they were born to freedom, he desires them to continue in the same condition. If the two subjects in dispute be fairly compared, the most ignorant person will prefer the liberty of the gospel to the bondage of the law.</p>"},
                {"src": "barnes", "attr": "Albert Barnes", "html": "<p>So then, brethren. It follows from all this — not from the allegory regarded as an argument, for Paul does not use it thus — but from the considerations suggested on the whole subject. Since the Christian religion is so superior to the Jewish; since we are by it freed from degrading servitude, it follows that we are not children of the bond-woman.</p>"},
                {"src": "wesley", "attr": "John Wesley", "html": "<p>So then — To sum up all. We — Who believe. Are not children of the bondwoman — Have nothing to do with the servile Mosaic dispensation. But of the free — Being free from the curse and the bond of that law, and from the power of sin and Satan.</p>"}
            ],
            "consensus": "affirm",
            "key_tension": None
        }
    }
}

def main():
    existing = load_synthesis('galatians')
    merge_synthesis(existing, GALATIANS)
    save_synthesis('galatians', existing)
    print('Galatians 4 synthesis complete.')

if __name__ == '__main__':
    main()
