"""
Wide Source Synthesis — Romans chapter 14
bookId: romans
Run: python3 scripts/ws-synthesis-romans-14.py

Sources used: calvin, ellicott, clarke, wesley, barnes
Note: mhcc not available for Romans; jfb data for Romans 14 is corrupted (contains Acts content), so jfb excluded.
Chapter range: 14  (23 verses)

Key synthesis decisions:
- calvin missing v13, v16, v21; ellicott missing v8, v12; clarke missing v8, v11; wesley missing vv4, 8, 9, 12, 20.
  Remaining sources provide adequate coverage for all verses.
- v14: consensus "affirm" — all voices agree that nothing is inherently unclean AND that personal
  conviction of uncleanness creates real moral obligation; the emphasis between objective freedom
  and subjective conscience is held together by every commentator, not divided between them.
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
    "14": {
        "1": {
            "synthesis": "<p>Paul opens Romans 14 by addressing the single most destabilizing conflict in the Roman church: whether Gentile believers, free from the Mosaic food laws, should insist on their liberty while Jewish converts retained inherited scruples about clean and unclean meats. The command is clear — 'receive' the weak one, a warm word of active welcome rather than grudging toleration. Ellicott illumines 'weak in the faith' as describing a believer whose mind lacks the integrating power of Christ as sole master-motive; when faith is not yet strong enough to govern conscience by a single great allegiance, petty details fill the space. Calvin stresses that the strong bear the obligation of accommodation, since it is precisely their progress in understanding that creates the asymmetry. Wesley captures the pastoral posture compactly: receive the weak 'with all love and courtesy into Christian fellowship.' The critical restraint Paul adds — 'not to doubtful disputations' — forbids the stronger believer from using the welcome as an occasion to debate and convert the weaker to his own position.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>They who have made the most progress in Christian doctrine should accommodate themselves to the more ignorant, and employ their own strength to sustain their weakness; for among the people of God there are some weaker than others, and who, except they are treated with great tenderness and kindness, will be discouraged, and become at length alienated from religion.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p><strong>Weak in the faith</strong> — there may be a sincere desire to lead a religious life, and yet the mind is taken up with petty details, each of which is painfully judged by itself, and not by reference to a central principle. The opposite of this is to be 'weak in the faith.'</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>Him that is weak — Through needless scruples. Receive — With all love and courtesy into Christian fellowship. But not to doubtful disputations — About questionable points.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>The converts to Christianity were from both Jews and Gentiles. There were many Jews in Rome; and it is probable that no small part of the church was composed of them. The New Testament everywhere shows that they were disposed to bind the Gentile converts to their own customs, and to insist on the observance of the peculiar laws of Moses.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "2": {
            "synthesis": "<p>Paul illustrates the division between strong and weak by the most tangible marker: what each eats. The 'strong' believer — typically the Gentile convert — is confident that the Mosaic distinctions between clean and unclean meats have no binding claim on the Christian, and so eats freely. The 'weak' believer — typically a Jewish convert — has not yet shed the ingrained reverence for the dietary laws, and so retreats to herbs alone to avoid any taint of forbidden meat. Clarke helpfully notes that Jewish converts living in a Gentile city could not always verify whether meat had been properly slaughtered, and so abstained altogether as the safer conscience. Calvin underscores that Paul's phrasing is descriptive, not prescriptive: he is not commanding the more restricted diet but simply noting the fact of the division. Ellicott focuses on the psychological root: the strong person's 'confidence' is faith large enough to prevent the conscience from becoming uneasy over such distinctions — the difference is not merely custom but the reach of faith into daily life.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>Both sentences are declarative, announcing a fact respecting two parties: the one believed he might eat all things — the other, who is weak, abstains from things forbidden by the law, and chooses to eat herbs rather than be defiled by contact with what the law prohibits.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p><strong>Believeth that he may</strong> — rather, <em>hath confidence to eat all things.</em> His faith is strong enough to prevent his conscience from becoming uneasy.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>Another, who is weak, eateth herbs — Certain Jews, lately converted to the Christian faith, and having as yet little knowledge of its doctrines, believe the Mosaic law relative to clean and unclean meats to be still in force; and therefore, when they are in a Gentile country, for fear of being defiled, avoid flesh entirely, and live on vegetables.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>The apostle admits that the Jewish convert was weak — not fully informed of the liberty which the gospel gives; while the strong, whether Gentile or enlightened Jewish convert, was not restrained by any scruples about the lawfulness of certain meats.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "3": {
            "synthesis": "<p>Paul addresses the characteristic failure of each party with surgical economy. The strong — who eat freely — are prone to despise the scrupulous as petty, superstitious, or spiritually immature; Calvin observes that this contempt comes naturally to those who regard such scruples as beneath notice. The weak — who abstain — are prone to judge and condemn the free-eaters as irreligious or careless about holiness; Ellicott notes drily that 'human nature alters very little' in these matters. The silencing argument is the same for both: 'God hath received him.' This is not an appeal to the man's own virtue but to the divine verdict already rendered. Ellicott points out that 'received' (προσελάβετο) means admitted him into God's church at his conversion; the act of divine welcome has already settled a question that neither party is competent to reopen. Wesley draws the application sharp: that welcome places the received person among God's children, and neither contempt nor condemnation from a human judge is appropriate toward a member of the divine household.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He wisely and suitably meets the faults of both parties. They who were strong had this fault — that they despised those as superstitious who were scrupulous about insignificant things; these, on the other hand, were hardly able to refrain from rash judgments, so as not to condemn what they did not follow.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The strong <em>despise</em> the weak; the weak <em>judge</em> the strong. In the one case there is contempt for what is thought to be narrowness and pedantry. In the other case censorious judgments are passed on what is regarded as levity and irreligion. Human nature alters very little. <strong>God hath received him</strong> — admitted him into His Church when he was baptised.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>Both being sincere and upright, and acting in the fear of God, are received as heirs of eternal life, without any difference on account of these religious scruples or prejudices.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>Despise him that eateth not — As over-scrupulous or superstitious. Judge him that eateth — As profane, or taking undue liberties. For God hath received him — Into the number of his children, notwithstanding this.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "4": {
            "synthesis": "<p>The rebuke in verse 4 extends the servant-master image to its full weight. In the Greek and Roman world, a master's servant was not subject to the discipline of a neighbor's household — interfering with another man's servants was both a social breach and a legal overreach. Calvin applies this precisely: to judge God's servant by your own convictions about meats is exactly this kind of presumption, treating your preferences as law for someone else's household. The question 'who art thou?' is not rhetorical softening but a genuine challenge to assumed standing. Ellicott notes it is directed especially at the weak believer who, carrying over the Jewish tradition of religious authority, assumed a mandate to pronounce on others. The verse does not leave the condemned servant's fate in uncertainty: 'he shall be holden up.' Clarke stresses that God's ability to make even the scrupulous believer stand is the real point — sincere uprightness before God secures the verdict, regardless of what either party thinks about the other's practice.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>As you would act presumptuously among men were you to bring another man's servant under your own rules, and try all his acts by the rule of your own will; so you assume too much, if you condemn anything in God's servant, because it does not please you; for it belongs not to you to prescribe to him what to do and what not to do.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p><strong>Who art thou?</strong> — This is addressed to the weak. The Apostle indignantly challenges his right to judge. That right belongs to another tribunal, before which the conduct of the stronger Christian will not be condemned but approved and upheld. <strong>Holden up</strong> — Made to stand — by God himself.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>Who has ever given thee the right to condemn the servant of another man? To his own master he standeth or falleth. He is sincere and upright, and God, who is able to make him stand, will uphold him; and so teach him that he shall not essentially err.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>The doctrine of this epistle is uniformly that the Jew had no such privilege, but that in regard to salvation he was on the same level with the Gentile. This is a principle of common sense and common propriety: no man has the right to sit in judgment on another man's servant in the matters that belong to his master's household.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "5": {
            "synthesis": "<p>From food, Paul moves to days: the same structure of Jewish scruple and Gentile freedom repeats itself in the observance of festivals. Calvin observes that the converted Jew, raised from infancy with a reverence for Passover, Pentecost, Sabbath, and the rest, could not simply set aside those observances once converted to Christ; the associations were too deep and the law's authority too long established. The Gentile convert, with no such formation, observed no such days and saw no reason to begin. Paul's resolution is not to adjudicate which practice is correct but to locate the authority where it belongs: in each believer's own conscience. The phrase 'fully persuaded in his own mind' (πληροφορείσθω ἐν τῷ ἰδίῳ νοΐ) is the hinge. Wesley makes the application direct: a person should be fully persuaded that a thing is lawful before doing it. Ellicott notes from Galatians and Colossians that day-observance has no absolute apostolic sanction but may have genuine religious expediency — which is a sufficient basis for those who practice it in good conscience.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>The Jews, who had been brought up from their childhood in the doctrine of the law, would not lay aside that reverence for days which they had entertained from the beginning, and to which they had been accustomed. The Gentile convert, with no such formation, observed no such days and saw no reason to begin.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>For the observance of days and seasons, compare Galatians 4:10; Colossians 2:16. From these passages, taken together, it is clear that the observance of special days has no absolute sanction, but is purely a question of religious expediency. That, however, is sufficient ground on which to rest it.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>The converted Jew still thought these festivals of moral obligation; the Gentile Christian not having been bred up in this way had no such prejudices. As those who were the instruments of bringing him to the knowledge of God gave him no such instructions, he did not think himself obliged to observe them.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>One day above another — As new moons, and other Jewish festivals. Let every man be fully persuaded — That a thing is lawful, before he does it.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "6": {
            "synthesis": "<p>The logic of verse 6 is unexpected and generous: Paul pronounces both the day-keeper and the day-ignorer, both the meat-eater and the herb-only abstainer, acceptable to the Lord — provided both act from genuine conscience toward God and seal the act with thanksgiving. Clarke calls this 'a beautiful apology for mistaken sincerity,' recognizing that Paul does not endorse the theological position of the day-keeping Jew but does honor the intention behind it. Calvin draws the same distinction carefully: the notion that the Mosaic observances remain binding is, in his view, a superstition; but the sincere intention to honor God by observing them can be received by God. The act of giving thanks is the mark of sincerity on both sides. Wesley notes that both the observer and non-observer of days act 'out of a principle of conscience toward God' — the motive, not the menu or the calendar, is what the Lord sees. Ellicott adds that saying grace at meals consecrates the meal to God, making even the act of eating meat a religious act offered in worship.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>It is necessary to distinguish between the notion which any one may have entertained as to the observance of days, and the observance itself to which he felt himself bound. The notion was indeed superstitious, but the sincere intention to honor God by observing them can be received; for Paul commends only the upright intention, and not the error.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p><strong>For he giveth God thanks</strong> — By the saying of grace at meat, the meal, whatever it may be, is consecrated to God, and he who partakes of it shows that he does so in no irreverent spirit.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>A beautiful apology for mistaken sincerity and injudicious reformation. Do not condemn the man for what is indifferent in itself: if he keep these festivals, his purpose is to honor God by the religious observance of them. On the other hand, he who cannot observe them in honor of God does not observe them at all.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>Regardeth it to the Lord — That is, out of a principle of conscience toward God. To the Lord he doth not regard it — He also acts from a principle of conscience. He that eateth not — Flesh. Giveth God thanks — For his herbs.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "7": {
            "synthesis": "<p>Verse 7 draws back from the debate about food and days to articulate the controlling principle behind both. No Christian lives to himself or dies to himself — the language of total belonging to another. Clarke notes that Greek usage applied 'living to oneself' specifically to acting on one's own judgment, following one's own preferences as law; Paul's categorical denial of this for the Christian means that every act, however mundane, is referred to a higher will. Calvin presses the argument from whole to part: if the whole of life belongs to God's glory, then it follows that each particular choice — what to eat, which day to observe — is also governed by his claim. This has immediate relevance for the strong believer who wants to assert liberty: the freedom he claims is not self-ownership but stewardship. Wesley is crisp: the Christian is 'not at his own disposal; doeth not his own will.' Barnes notes that no Christian lives to gratify his own inclinations or appetites, making it the very principle distinguishing Christian life from merely natural life.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He confirms the former verse by an argument derived from the whole to a part — that it is no matter of wonder that particular acts of our life should be referred to the Lord's will, since life itself ought to be wholly spent to his glory; for then only is the life of a Christian rightly formed, when it has for its object the will of God.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>The Greek writers use the phrase <em>ἑαυτῳ ζῃν</em> to signify acting according to one's own judgment, following one's own opinion. Christians must act in all things according to the mind and will of God, and not follow their own wills. God is our master; we must live to him, as we live under his notice and by his bounty.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>None of us — Christians, in the things we do. Liveth to himself — Is at his own disposal; doeth his own will.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>No Christian lives to gratify his own inclinations or appetites. He makes it his great aim to do the will of God; to subordinate all his desires to his law and gospel; and though one should eat flesh and another abstain, both may be doing the will of God in their respective choices.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "8": {
            "synthesis": "<p>Verse 8 unpacks the claim of verse 7 into its full scope. Whether the Christian lives or dies, he belongs to the Lord — not merely in moments of religious exercise but in the totality of existence. Calvin explains 'living to the Lord' as conforming to Christ's will and designing all things to his glory, not simply performing outward acts of devotion. The verb 'live' here describes the quality and orientation of life, not merely its continuation. Barnes notes that this is the distinguishing mark of the Christian among all people: other men live to gratify themselves, to pursue their own projects and pleasures; the Christian has a different center, doing those things 'which the Lord requires.' The declaration 'we are the Lord's' lands with finality — it is not a conditional membership but a statement of ownership established by Christ's own act, as verse 9 will clarify. For the debate about meats and days, the implication is plain: neither the eating nor the abstaining is the point in itself; the question is whether the act is offered to the Lord.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>This does not mean only that we perform outward acts of devotion, but that we conform to his will and pleasure, and design all things to his glory. Nor are we only to live to the Lord, but also to die; that is, our death as well as our life is to be referred to his will — he has full authority over our life and our death.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>Other men live to gratify themselves; the Christian to do those things which the Lord requires. By the Lord the apostle evidently intends the Lord Jesus, and the truth taught here is that it is the leading and grand purpose of the Christian to do honour to the Saviour — this constitutes his peculiar character.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "9": {
            "synthesis": "<p>The 'for' of verse 9 grounds the total claim of verses 7–8 in a historical event with a stated purpose. Christ died and rose 'to this end' — not incidentally, not merely as an act of love, but with sovereign intent — that he might be Lord of both dead and living. Calvin stresses the purchase: through death and resurrection, Christ acquired authority over us that death itself cannot dissolve; he who lived and died for us has received our whole existence as his peculiar property. Clarke extends the scope: Christ's dominion extends not only over the living but over separate spirits in the intermediate state — all throughout eternity belong to his authority. Barnes notes that Paul does not present this as the only design of Christ's death, but as a main purpose distinctly in view, confirming what precedes: the reason we live and die to the Lord (v. 8) is that the Lord purchased us by doing so himself. Ellicott identifies a textual note: the best manuscripts substitute 'and lived' for the longer 'and rose, and revived,' making resurrection the single enthroning act.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>In order to prove that we ought to live and to die to the Lord, he shows how rightly Christ claims this power over us, since he has obtained it by so great a price; for by undergoing death for our salvation, he has acquired authority over us which cannot be destroyed by death, and by rising again, he has received our whole life as his peculiar property.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>It was through the resurrection that Christ was finally enthroned at His Father's right hand, and that universal dominion was given to Him. The best MSS. substitute simply 'and lived' for the received 'and rose, and revived.'</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>Christ's power extends equally over both worlds: separate, as well as embodied spirits, are under his authority; and he it is who is to raise even the dead to life: and thus all throughout eternity shall live under his dominion.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>The apostle does not say that this was the <em>only</em> design of his death, but that it was a main purpose, or an object which he had distinctly in view — confirming what he had said that in all circumstances we are the Lord's.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "10": {
            "synthesis": "<p>With the universal lordship of Christ established, Paul draws the judicial conclusion: no Christian has standing to judge another, because only Christ is Lord and Judge of all. Calvin identifies this as the specific power in view — not mere moral guidance but the divine authority to pronounce on a person's standing before God, authority received by Christ from the Father and not delegated to any believer. To exercise that authority is to usurp what belongs to Christ alone. Wesley notes that Paul here turns specifically to address the stronger believer ('why dost thou set at nought thy brother?') after addressing the weak in earlier verses, so both parties receive the rebuke. Barnes frames the argument in equity: if all must stand before the same tribunal on the same footing, what grounds remain for one believer to sit in judgment over another? Ellicott flags an important textual variant — the best manuscripts read 'judgment seat of God' rather than 'of Christ,' uniting the divine persons in the single judgment Paul is invoking. The word 'brother' is itself the rebuke: this is someone God has already received.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He concludes that it is an unreasonable boldness in any one to assume the power to judge his brother, since by taking such a liberty he robs Christ the Lord of the power which he alone has received from the Father. By the term <em>brother</em> he checks this lust for judging; for the Lord has established among us the right of fraternal relationship.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p><strong>Judgment seat of Christ</strong> — The true reading is <em>of God.</em></p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>The superstitious are prone to judge, and those who are not superstitious are prone to despise. Both must appear before God's bar: the Christian Jew must answer for his judging; the Christian Gentile for his contempt. It is God's bar, not ours.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>Or why dost thou despise thy brother — Hitherto the apostle has addressed the weak brother: now he speaks to the stronger.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>Since we are all subjects and servants alike, and must all stand at the same tribunal, what right have we to sit in judgment on others? God has recognised the weak brother as his friend, and he should be regarded by thee as a brother in the same family.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "11": {
            "synthesis": "<p>Paul supports the coming universal judgment with Isaiah 45:23, a text in which Jehovah swears by his own life that every knee will bow and every tongue confess. Barnes draws the significant implication: since in Isaiah the speaker is unambiguously Jehovah (the divine name is used repeatedly and exclusively), Paul's application of the text to Christ's judgment seat in verse 10 constitutes a strong incidental proof of Christ's divinity — one Paul does not argue for but simply presupposes in the quotation. Calvin reads the purpose of the citation differently from mere proof: Paul quotes Isaiah not primarily to establish that a judgment exists (Christians already knew this) but to induce the humility appropriate to those who must stand there. 'Every knee shall bow' levels all distinctions; the scrupulous Jewish convert and the free Gentile believer will both bow in the same posture before the same Lord. Wesley notes that the oath 'As I live' is proper to God alone — no creature possesses 'life infinite and independent' — and that the full scope of the confession awaits its accomplishment at the final judgment.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He seems to have quoted this testimony of the Prophet not so much to prove what he had said of the judgment-seat of Christ, which was not doubted among Christians, as to show that judgment ought to be looked for by all with the greatest humility and lowliness of mind; for all flesh must be humbled while expecting that judgment.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>As I live — An oath proper to him, because he only possesseth life infinite and independent. It is Christ who is here termed both Lord and God; as it is he to whom we live, and to whom we die. Every tongue shall confess to God — Shall own him as their rightful Lord; which shall then only be accomplished in its full extent.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>In Isaiah there can be no doubt that it refers to Jehovah. The speaker expressly calls himself Jehovah, the name appropriate to God alone. In the place before us, the words are applied by Paul expressly to Christ — a strong incidental proof that the apostle regarded the Lord Jesus as Divine.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "12": {
            "synthesis": "<p>The judicial argument of verses 10–11 reaches its practical conclusion: since every one of us must give account of himself to God, no one has the leisure to prosecute a judgment against a neighbor. Calvin notes the elegant verbal pivot Paul has performed: he has forbidden 'judging' in the sense of condemning others (v. 10), and now reminds us that we must ourselves be judged — the same verb, two opposite uses, both landing on the same person. The irony is that those most eager to sit in judgment of their brethren are also those who must give the full account. Clarke applies the conclusion with a practical urgency: let each person take heed to be prepared 'to give up his accounts with joy' — not merely resigned to judgment but glad to face it. Barnes extends the principle beyond the immediate context: while the debate is about the Jewish-Gentile tension over meats and days, the truth that every word, work, and purpose will be exposed and weighed at God's unerring tribunal is universal and reaches every believer in every era.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>From the various significations of the word <em>to judge</em>, he has aptly drawn two different meanings: in the first place he forbids us to judge, that is, to condemn; in the second place he bids us to judge, that is, to exercise judgment so as not to give offense. It is not lawful for us to usurp the office of judging, who must ourselves submit to be judged.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>Every one of us shall give account of himself — We shall not, at the bar of God, be obliged to account for the conduct of each other — each shall give account of himself: and let him take heed that he be prepared to give up his accounts with joy.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>In the fearful arraignment of that day, every work and purpose shall be brought forth, and tried by the unerring standard of justice. This is a truth revealed elsewhere, that all men shall give account of their conduct to God — it is here applied to settle the quarrel between believers over meats and days.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "13": {
            "synthesis": "<p>Paul pivots the very word 'judge' that has characterized the weak believer's failure into a positive command: stop judging one another, and instead exercise judgment about how to avoid becoming an obstacle in a brother's path. Ellicott notes that this turning of the word forms the connecting link between the two halves of the chapter; the faculty for judgment, redirected from condemning others to examining one's own conduct, becomes a virtue rather than a sin. Barnes observes that Paul is meeting the judgmental temperament on its own ground: those who cannot resist pronouncing opinions should at least direct their judgment toward something useful — determining how not to cause harm. Wesley is precise about the two categories of harm: the 'stumblingblock' causes the weak brother to imitate you against his conscience; the 'scandal' (σκάνδαλον) causes him to resent and reject you, losing both peace and love. Clarke anchors the motive: rites and ceremonies are not the center of the Gospel; anything that causes a brother to abandon the Gospel is a catastrophic harm, regardless of the liberty that occasioned it.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p><strong>Judge this rather</strong> — The word 'judge' forms the connecting-link between what follows and what has gone before. If any judgment is to be formed at all, let it be rather as a principle to guide our own action, and not in the shape of a criticism upon others. This principle should be not to put temptation in the way of weaker brethren.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>Let us abandon such rash conduct; it is dangerous, it is uncharitable: judgment belongs to the Lord. Let both the converted Jew and Gentile consider that they should labor to promote each other's spiritual interests, and not be a means of causing them to abandon the Gospel, on which, and not on questions of rites and ceremonies, their salvation depends.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>But judge this rather — Concerning ourselves. Not to lay a stumblingblock — By moving him to do as thou doest, though against his conscience. Or a scandal — Moving him to hate or judge thee.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>Some men have an irresistible propensity to sit in judgment, to pronounce opinions. Let them make good use of that talent by exercising it on their own conduct — judging not to injure the cause of Christ.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "14": {
            "synthesis": "<p>Verse 14 is the epistemological turning point of the chapter. Paul declares his personal persuasion — formed 'by the Lord Jesus,' whether through Christ's own teaching or through special revelation as Wesley suggests — that no food is intrinsically unclean. This is a direct endorsement of the Gentile position and an implicit ruling against the continuing force of the Mosaic dietary code for Christians. Clarke underscores that Paul speaks with apostolic authority: 'I have the inspiration and authority of Jesus Christ to say so.' Yet the verse immediately qualifies what this liberty means in practice: the subjective conviction of a person who regards something as unclean creates real uncleanness for him. To eat against conscience is not freedom but violation. Barnes observes that Paul has formerly carried the very same scruples the weak brother now carries, and his own transformation of view makes him simultaneously confident in the truth and gentle toward those still in transition. Both the objective declaration and the subjective qualification are held together by every commentator — the freedom is real, but so is the binding force of conscience.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He declares that no meat is impure to a right and pure conscience, and that there is no hindrance to a pure use of meats, except ignorance and infirmity; for when any imagines an impurity in them, he is not at liberty to use them without sin against his own conscience.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The Apostle clearly identifies himself with the less scrupulous party. For one of his intense penetration and grasp on the realities of things, any other position was impossible. But while these essential features in the Apostle's character find the noblest expression, we cannot but note his attitude of gentle forbearance towards those whose faith is less deep and less robust than his own.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>After reasoning so long without attempting to give any opinion, he now expresses himself fully, and tells them that nothing is unclean of itself, and that he has the inspiration and authority of Jesus Christ to say so. And yet, after delivering this important sentiment, he proceeds to show how the use of this liberty may be sinful.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>I am assured by the Lord Jesus — Perhaps by a particular revelation. That there is nothing — Neither flesh nor herbs. Unclean of itself — Unlawful under the gospel.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "15": {
            "synthesis": "<p>Paul now appeals to the two most powerful forces in Christian ethics: love and the cross. If a brother is grieved by your eating — not merely inconvenienced but wounded in conscience, stumbled in his walk — you are violating the law of love regardless of your theoretical freedom. Calvin presses this as a matter of proportion: the trivial pleasure of insisting on your liberty against a brother's grief is an act of selfishness disproportionate to any benefit. But the second argument is sharper still: 'destroy not him for whom Christ died.' Wesley draws the logical consequence with economy: 'he for whom Christ died may be destroyed' — the weak believer is not a permanent fixture of weakness but a soul whose ruin is a real possibility. To value the liberty to eat more than the preservation of a soul Christ purchased at the cost of his life is, in Calvin's words, 'basely given up to our own lusts.' Clarke raises the stakes: this is not a dispute about cuisine but about whether a person will remain in the faith. Barnes notes that the power of Paul's appeal lies precisely in the asymmetry: Christ gave everything for this person; you are asked only to give up a meal.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>When the weak conscience is wounded, the price of Christ's blood is wasted; for the most abject brother has been redeemed by the blood of Christ: it is then a heinous crime to destroy him by gratifying the stomach; and we must be basely given up to our own lusts, if we prefer our appetite to the salvation of a brother.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>Destroy not him with thy meat — Do not cause him to apostatize. Do not value thy meat more than Christ valued his life. He for whom Christ died may be utterly lost through thy persistence in asserting a liberty which costs him his soul.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>If thy brother is grieved — That is, wounded, led into sin. Destroy not him for whom Christ died — So we see, he for whom Christ died may be destroyed. With thy meat — Do not value thy meat more than Christ valued his life.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>The pain of the weak brother would be real, though the opinion from which it sprang was erroneous. The power of Paul's appeal lies in the asymmetry: Christ gave his life for this person; you are asked only to abstain from a particular food. The question of proportion answers itself.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "16": {
            "synthesis": "<p>The warning of verse 16 widens the horizon from damage done to a weak brother to damage done to the Gospel's reputation before the wider world. Ellicott notes that 'your good' (τὸ ἀγαθὸν ὑμῶν) refers to the blessing of Christian liberty — the freedom from the Mosaic law that is genuinely a gift and a privilege. But that gift, exercised in ways that wound, offend, and provoke quarrels, generates 'evil speaking' (βλασφημεῖσθω) — not merely criticism of you personally but blasphemy against the faith you embody. Barnes makes explicit what the Greek implies: the misuse of liberty gives outsiders occasion to speak evil of Christianity as a religion of license and disregard for holiness. Clarke adds a wise practical note: many acts that are lawful in themselves become destructive when performed at the wrong time or in the wrong spirit; prudence about when and how to exercise good things is itself part of the Christian calling. Wesley's summary is terse: 'Let not your good and lawful liberty be evil spoken of by being offensive to others.'</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p><strong>Your good</strong> — That blessing of Christian liberty which you enjoy. This is not to be used so as to give rise to reproaches and recriminations which will make a bad impression on the outside world.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>Do not make such a use of your Christian liberty as to subject the Gospel itself to reproach. There are many who have such an unhappy method of doing their good acts as to do little good by them, and a great deal of evil. It requires much prudence to find out the proper time of performing even a good action.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>Let not then your good and lawful liberty be evil spoken of — By being offensive to others.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>The word rendered 'evil spoken of' is <em>blasphemed</em>. Do not so use your Christian liberty as to give occasion for railing, so as to produce contention and strife, and thus to give rise to evil reports among the wicked about the tendency of the Christian religion.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "17": {
            "synthesis": "<p>Verse 17 offers the theological grounding of all the practical counsel: the kingdom of God is not constituted by food or drink. Paul's triad of kingdom-essentials is deliberately counter to the Jewish categories — not meats and feast-days but righteousness, peace, and joy in the Holy Ghost. Wesley gives each term its weight: righteousness is 'the image of God stamped on the heart, the love of God and man'; peace is the peace passing understanding that rules in the soul through God's mercy; joy is the Spirit's own inward gladness, not dependent on external circumstances. Ellicott reads 'righteousness' as the moral condition of the believer himself and 'peace' as his concord with fellow Christians — relational and ethical rather than forensic. Calvin draws the practical implication directly: since the kingdom is not constituted by these things, the strong believer loses nothing essential by abstaining from the exercise of his liberty for love's sake. Barnes states the positive complement: the Christian church is to be distinguished by these inward realities, not by the food regulations that distinguished the Jewish community.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He teaches us that we can without loss abstain from the use of our liberty, because the kingdom of God does not consist in such things. If for love's sake it be lawful to abstain from meat, while God's honour is uninjured and Christ's kingdom suffers no harm, then those who for meat's sake disturb the church are not to be endured.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>By 'righteousness and peace' is not here meant imputed righteousness or justification, but rather the moral condition of righteousness in the Christian himself, and concord with his fellow-men. These are crowned in the confirmed Christian by that feeling of subdued and chastened exultation which is wrought by the constant influence of the Holy Spirit.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>The kingdom of God is that holy religion which God has sent from heaven. It is not meat and drink — it consists not in these outward and indifferent things. But righteousness — pardon of sin and holiness of heart and life; and peace — in the soul from a sense of God's mercy; and joy in the Holy Ghost.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>For the kingdom of God — that is, true religion, does not consist in external observances. But in righteousness — The image of God stamped on the heart; the love of God and man, accompanied with the peace that passeth all understanding, and joy in the Holy Ghost.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "18": {
            "synthesis": "<p>Verse 18 completes the trinitarian cluster of verse 17 by naming its two-directional fruit. The one who serves Christ in righteousness, peace, and joy is acceptable to God — the divine verdict — and approved of men — the human recognition. Calvin draws the argument from effect: it is impossible that a life governed by such qualities should not commend the faith to observers; the kingdom of God 'fully prevails and flourishes' in such a person. Ellicott explains 'approved of men' carefully: Paul does not promise that the wicked world will love such a person, but that the life will be recognizable as right, even to those who oppose it. Barnes makes the same distinction: not affection from outsiders but acknowledgment of the consistency and integrity of the life. Wesley confines 'men' to 'wise and good men' — those with the discernment to recognize genuine righteousness. Clarke adds that even when religion is persecuted, the righteousness it produces eventually commands recognition, since a holy life is a standing argument that cannot finally be dismissed.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>An argument drawn from the effect: it is impossible but that when any one is acceptable to God and approved by men, the kingdom of God fully prevails and flourishes in him. Wherever there is righteousness and peace and spiritual joy, there the kingdom of God is complete in all its parts.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p><strong>Approved of men</strong> — So that he will not be 'evil spoken of,' as the uncompromising legalist or anti-legalist is apt to be. Paul does not promise the love of the wicked world, but recognition of rightness even by those who oppose.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>The man who has righteousness, peace, and joy in the Holy Ghost has not only the form of godliness but the power; and therefore the whole frame of his mind, as well as his acts, must be acceptable to God. Although religion may be persecuted, its righteousness will eventually command respect.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>In these — Righteousness, peace, and joy. Men — Wise and good men.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "19": {
            "synthesis": "<p>Paul's imperative turns constructive: follow the things that make for peace, and pursue those things by which one may edify another. Calvin identifies the logical force of the 'therefore': all the negative counsel — stop despising, stop judging, stop eating so as to offend — has been in service of these positive goods, concord and mutual upbuilding. Barnes presents verse 19 as the conclusion of the whole chapter's argument, the destination toward which the reasoning has been moving: if Christians aim at the great objects of the faith, they will live in peace; if they focus on their divergent practices in minor things, they will never stop quarreling. Wesley's observation deserves attention: 'Practical divinity tends equally to peace and to edification. Controversial divinity less directly tends to edification' — a judgment shaped by Wesley's own experience of the divisive power of theological dispute as distinct from the unifying power of applied Christian living. Ellicott notes that 'edify' (οἰκοδομή) means the 'upbuilding' of Christian character through mutual intercourse — a richer image than the now-flattened English word conveys.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He recalls us, as much as possible, from a mere regard to meats to consider those greater things which ought to have the first place in all our actions. In order to promote concord and edification, all the duties of love ought to be exercised.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p><strong>Edify</strong> — The word has unfortunately lost its freshness of meaning, but we have no other single equivalent for it in English. It is the 'upbuilding,' or mutual help and assistance in the spiritual life which Christians receive from their intercourse with each other.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>Peace and edification are closely joined. Practical divinity tends equally to peace and to edification. Controversial divinity less directly tends to edification, although sometimes, as they of old, we cannot build without it.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>This verse may be regarded as the conclusion to which the argument had conducted him. If men aim at the great objects proposed by the Christian religion, they will live in peace. If they seek to promote their private views, in smaller matters, they will produce strifes and contentions.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "20": {
            "synthesis": "<p>The building image from verse 19 (edify) generates its contrasting image in verse 20: destroying God's work — pulling down what grace has been constructing in a soul — for the sake of insisting on the right to eat freely. Ellicott presses the etymology: 'destroy' here (καταλύω) is the exact opposite of 'edify,' meaning to dismantle and unbuild the structure; 'the work of God' is the spiritual formation grace has been raising in the weak believer's life. Paul then allows the abstract principle: all things are indeed pure — reaffirming verse 14 — but the general truth does not override the particular act. Calvin explains the qualification precisely: the purity of meat is unchanged, but when a man eats in a way that violates love — causing grief, causing offense, pulling down a brother — the act of eating becomes evil regardless of the food's inherent status. Barnes presses the contrast between the worth of the prize and the price of the claim: to risk the ruin of a soul in order to vindicate your right to eat a particular food is a profoundly disproportionate exchange.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>By saying that all things are pure, he makes a general declaration; and by adding that it is evil for man to eat with offense, he makes an exception — as though he had said: 'Meat is indeed good, but to give offense is bad.' He then pollutes the use of pure meat who by it violates love.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p><strong>Destroy not</strong> — A different word from that employed in Romans 14:15. It is the correlative and opposite of 'edify,' and means to 'unbuild' or 'pull down.' <strong>The work of God</strong> — The fabric which the grace of God has begun — the gradual formation of a truly Christian character in the soul of the weak believer.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>For meat destroy not the work of God — Do not hinder the progress of the Gospel either in your own souls or in those of others, by contending about lawful or unlawful meats. All things indeed are pure — Nothing that is proper for aliment is unlawful to be eaten.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>By obstinate, pertinacious attachment to your opinions about the distinctions of meats and drinks, do not pursue such a course as to lead a brother into sin and ruin his soul. The opposite of the building metaphor — pulling down what God is building — applied to the tender work of grace in a fragile conscience.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "21": {
            "synthesis": "<p>Verse 21 restates the principle of verses 13–20 in its most compressed and positive form. It is good — a moral assessment, not merely advice — to abstain from whatever will make a brother stumble, be offended, or grow weak. Wesley draws out three distinct harms with precision: stumbling means the weak brother imitates you against his conscience, violating his own integrity; offense means he loses the peace of his walk; weakness means the loss of that joy in the Lord that had been his strength. Clarke extends the reach of the self-denying principle: the same spirit that forbids damaging your brother through food should, at the limit, extend to giving your life for him — the principle has no comfortable floor. Barnes notes that the mention of wine alongside flesh suggests the principle extends beyond merely Mosaic food laws; Nazirite customs and associations with pagan libations made wine a separate area of conscience for some believers. Ellicott recognizes that these sentences — direct, clear, incisive — are characteristic of Paul when he addresses concrete moral urgency rather than abstract theological argument.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>These direct, clear, incisive sentences are as characteristic of the style of the Apostle (when he is dealing with moral questions of present urgency, and not with the abstract problems of theology) as the generous impulse which prompts them is of his heart.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>The spirit and self-denying principles of the Gospel teach us that we should not only avoid every thing in eating or drinking which may be an occasion of offense or apostasy to our brethren, but even lay down our lives for them should it be necessary. The principle has no comfortable floor.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>Thy brother stumbleth — By imitating thee against his conscience, contrary to righteousness. Or is offended — At what thou doest to the loss of his peace. Or made weak — Hesitating between imitation and abhorrence, to the loss of that joy in the Lord which was his strength.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>The mention of wine alongside flesh suggests this principle extends beyond Mosaic food laws; wine was used in libations in heathen worship, and perhaps some early converts regarded it as unlawful. The mention broadens the principle to any practice that proves an occasion of stumbling.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "22": {
            "synthesis": "<p>Paul addresses the strong believer's impulse to demonstrate his freedom publicly: you have the right conviction about food and days — keep it between yourself and God. Calvin articulates why: the value of the strong man's freedom is real, but it consists in 'peace of conscience before God'; it does not require public vindication. Displaying your liberty before a weak brother in a way that presses him toward conduct his conscience cannot yet bear is not freedom but imposition. Barnes clarifies that 'faith' here has the specific sense of the conviction that all meats are permissible — not the saving faith that justifies, but the settled persuasion on a disputed practical question. Ellicott notes a textual shift that makes the verse even crisper: 'The faith you have, have it to yourself before God' — your liberty is between you and the Lord, not a public cause to be won. The beatitude that closes the verse is telling: 'happy is he who does not condemn himself in the thing he allows.' Wesley applies it two ways: happy the man who uses innocent things without self-condemnation, and happy also the man who has a conscience free from disabling doubt in the first place.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>Liberty really understood, as it is that of faith, has properly a regard to God; so that he who is endued with a conviction of this kind ought to be satisfied with peace of conscience before God; nor is it needful for him to show before men that he possesses it.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Reserve the exhibition of your liberty to the privacy of your own direct communion with God, and do not display it ostentatiously in public where it may do harm. It is a happy thing to have no self-condemnatory scruples of conscience, but it is fatal to have scruples and to disregard them.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>The term <em>faith</em> seems to signify in this place a full persuasion in a man's mind that he is right, that what he does is lawful, and has the approbation of God and his conscience. Have it to thyself; keep it to thyself, and do not offend others by it.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>Hast thou faith — That all things are pure? Have it to thyself before God — In circumstances like these, keep it to thyself, and do not offend others by it. Happy is he that condemneth not himself — By an improper use of even innocent things!</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "23": {
            "synthesis": "<p>Verse 23 closes the chapter with one of Paul's most far-reaching moral axioms: whatever is not of faith is sin. The argument moves from the particular to the universal. The particular: he who doubts about eating, and eats anyway against his hesitation, is condemned — not because the food is wrong, but because he has acted against the testimony of his own conscience. Calvin identifies the Greek word (ὁ διακρινόμενος) as describing a mind vacillating between two judgments, unable to settle to a clear persuasion; such a divided mind, proceeding against itself, cannot please God regardless of what the act is. The universal principle is equally momentous: 'whatsoever is not of faith is sin.' Clarke explains 'faith' as a full persuasion that a thing is lawful — a moral certainty before God, not a theological proposition. Without that persuasion, any act, however innocent in itself, becomes sinful for the person who performs it without it. Ellicott draws the philosophical sharpness: the only faculty that can override the voice of conscience is a faith robust enough to silence the doubt; where faith is insufficient and conscience is clear about one direction, choosing the other direction is wrong regardless of what theology says about the thing's inherent permissibility. Barnes clarifies that 'damned' (κατακέκριται) means morally condemned, not necessarily condemned to eternal punishment.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>As then the main thing in a good work is the persuasion of a mind conscious of being right before God — as it were a calm assurance — nothing is more opposed to the acceptance of our works than vacillation. <em>He who discerns</em> describes a mind that undergoes alternate changes and is held suspended by uncertainty.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The one thing which justifies a man in neglecting such punctilious distinctions is a faith so strong that it can afford to make light of them. Where faith is not strong enough, and where the conscience deliberately approves one course but the other is chosen, this alone stamps the act as wrong.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>He that feeds on meats prohibited by the Mosaic law, with the persuasion in his mind that he may be wrong in so doing, is condemned by his conscience. For whatsoever is not of faith is sin — Whatever a man does without a full persuasion of its lawfulness is sin to him.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>Because it is not of faith — He does not believe it lawful; and in all these cases, whatsoever is not of faith is sin — Whatever a man does without a full persuasion of its lawfulness, it is sin to him.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>We apply 'damned' almost exclusively to future punishment, but here it means properly <em>to condemn</em>; the person is condemned by his own conscience for doing what he has reason to think God has forbidden — a present moral verdict, not necessarily a final one.</p>"
                }
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
    print('Romans 14 synthesis complete.')

if __name__ == '__main__':
    main()
