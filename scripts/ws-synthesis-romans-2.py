"""
Wide Source Synthesis — Romans chapter 2
bookId: romans
Run: python3 scripts/ws-synthesis-romans-2.py

Sources used: calvin, ellicott, clarke, wesley, barnes
Chapter range: 2  (29 verses)

Key synthesis decisions:
- v.6: "According to his works" in a justification epistle. Calvin reads this as Paul pointing
  to what genuine righteousness before God requires, stripping false confidence in empty works;
  Ellicott and Barnes take it as straightforwardly establishing the justice of impartial judgment.
  consensus: mixed
- vv.14-15: Whether Gentile law-keeping is actual or hypothetical. Calvin and Ellicott read it
  as describing a genuine moral phenomenon (natural conscience); Barnes treats it as a hypothetical
  illustrative case; Wesley grounds even natural law-keeping in prevenient grace.
  consensus: mixed
- mhcc file is absent for Romans; jfb ch.2 entries appear to be misaligned Acts content.
  Sources used throughout: calvin, ellicott, clarke, wesley, barnes.
- Ellicott missing keys 10, 26, 28, 29; Clarke missing 3, 22, 23; Wesley missing 3, 18, 22, 23.
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
    "2": {
        "1": {
            "synthesis": "<p>Paul opens chapter 2 by pivoting from the catalog of Gentile wickedness to confront the moral self-assessor — whether Jew or Gentile — who sits in judgment on others while practicing the same things. The word <em>therefore</em> links the sections: the very person who condemns the vices Paul has just described is inexcusable when he commits them himself. Ellicott notes that by judging another you deliver your own verdict, since you declare those acts criminal which you yourself commit. Calvin identifies the target as <em>saintlings</em> — outwardly respectable hypocrites who could not be included in the grosser vices of chapter one, yet whose self-complacency before God is equally groundless.</p><p>Wesley sharpens the application: knowledge without practice only increases guilt. The rhetorical shift to second person keeps the accusation from being deflected; no category of moral respectability exempts one from the judgment Paul announces here.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>This reproof is directed against hypocrites, who dazzle the eyes of men by displays of outward sanctity, and even think themselves to be accepted before God, as though they had given him full satisfaction. Hence Paul, after having stated the grosser vices, now attacks saintlings of this kind, who could not have been included in the first catalogue.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The description just given of the state of one section of the human race contains implicitly the condemnation of the other; for it is equally applicable to both. By the very act of sitting in judgment upon your fellow-man, you pass sentence upon yourself. You declare those acts to be criminal of which you are yourself guilty.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>Thou art inexcusable — seeing knowledge without practice only increases guilt. O man — having before spoken of the gentile in the third person, he addresses the Jew in the second person. But he calls him by a common appellation, as not acknowledging him to be a Jew. Whosoever thou art that judgest — for in that thou judgest the other, thou condemnest thyself; for thou doest the same things.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>The design of this and the following chapter is to show that the Jews were no less guilty than the Gentiles, and that they needed the benefit of the same salvation. This the apostle does by showing that they had greater light than the Gentiles, and yet that they did the same things. Still they were in the habit of accusing and condemning the Gentiles as wicked and abandoned.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "2": {
            "synthesis": "<p>Paul appeals to a principle his readers will recognize as settled: God's judgment falls <em>according to truth</em> — in strict accordance with reality, without the partiality or self-exception that human courts allow. Ellicott observes that Paul assumes this as a shared axiom, known to both Jew and Gentile, which makes it the more pointed against those who presumed that divine judgment applied to others alone. Calvin notes Paul's strategy: he summons the hypocrite to the tribunal of God, to whom even darkness is not hidden — no human jury's verdict of innocent can stand before that bar.</p><p>Wesley adds that this judgment is <em>according to truth</em> in that it reaches the heart as well as the life, not merely the outward conduct. Barnes emphasizes that the Jews knew this principle thoroughly from their own scriptures, and it was the acknowledged doctrine of the entire nation.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>The design of Paul is to shake off from hypocrites their self-complacencies, that they may not think that they can really gain any thing, though they be applauded by the world, and though they regard themselves guiltless; for a far different trial awaits them in heaven. He summons them to the tribunal of God, to whom darkness itself is not hid.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>St. Paul assumes that this will be acknowledged as a general principle by his readers, whether Jew or Gentile. There is still a strong under-current of allusion to the way in which the Jew was apt to fall back upon his privileges. The Jews, it seems, had an idea that the Gentiles only would be judged, while they would be able to claim admission into the Messianic kingdom as theirs by right of birth.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>For we know — without thy teaching — that the judgment of God is according to truth: is just, making no exception, and reaches the heart as well as the life.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>It is the common and admitted sentiment of mankind that God will punish such crimes. It is known and believed by men generally. It is implied in this declaration that this was known to the Jews; they knew it because it was everywhere taught in the Old Testament, and it was the acknowledged doctrine of the nation.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "3": {
            "synthesis": "<p>Paul presses the logical collapse of the self-exempting judge: if God judges according to truth those who do such things, and you do the same things, how can you think you will escape his judgment? The argument is direct — not a complex syllogism but an appeal to moral consistency. Ellicott underscores the emphatic thrust: <em>Are you</em> — because you are a Jew — <em>to be the only exception to this rule?</em> The force of the question is that such an exception would be self-evidently absurd.</p><p>Calvin notes the unusual rhetoric: Paul does not argue before men but appeals to the tribunal of conscience, treating the charge as proven because no one can honestly deny their own iniquity when they submit to God's scrutiny. Barnes frames it as an appeal to deep instinctive convictions of justice — if imperfect human judges condemn such things, a holy God most certainly will.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>Paul may seem to some to have acted unwisely for having passed so severe a censure when he had not yet proved the accusation. But the fact is otherwise; for he adduced not his accusation before men, but appealed to the judgment of conscience; and thus he deemed that proved which he had in view — that they could not deny their iniquity, if they examined themselves and submitted to the scrutiny of God's tribunal.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>That thou shalt escape — emphatic. <em>Are you</em> — because you are a Jew — <em>to be the only exception to this rule?</em></p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>This is an appeal to their common sense, to their deep and instinctive conviction of what was right. If they condemned those who practised these things; if, imperfect and obscure as their sense of justice was; if, unholy as they were, they yet condemned those guilty of these offences — would not a holy and just God be far more likely to pronounce judgment?</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "4": {
            "synthesis": "<p>The apostle anticipates a subtle temptation: that present prosperity and God's patience might be read as tokens of divine approval. Calvin identifies this as the hypocrite's characteristic error — being transported with prosperity as if earthly blessing proved God's favor. Clarke names three distinct gifts being abused: God's goodness (undeserved benefit), his forbearance (toleration of past sins), and his longsuffering (continued patience under repeated provocation). All three exist for one purpose — to lead to repentance — but the self-righteous inverts their meaning, reading them as indulgence rather than as gracious summons.</p><p>Wesley captures the escalation: the sinner moves from hoping to escape God's wrath to actively abusing God's love. Barnes is precise: the abuse lies not in explicit contempt but in the practical inference that God's continued blessing means he regards you as innocent and safe — a perversion the apostle now exposes.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>As hypocrites are commonly transported with prosperity, as though they had merited the Lord's kindness by their good deeds, and become thus more hardened in their contempt of God, the Apostle anticipates their arrogance, and proves by an argument taken from a reason of an opposite kind, that there is no ground for them to think that God, on account of their outward prosperity, is propitious to them.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>Or despisest thou the riches of his goodness — wilt thou render of none effect that marked benevolence of God towards thee which has given so many superior advantages, and that forbearance which has tolerated thy many miscarriages, and that long-suffering which, after repeated provocations, still continues to bear with thee? Not acknowledging that this goodness of God leadeth thee to repentance — was designed to accomplish this blessed end.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>Or despisest thou — dost thou go farther still, from hoping to escape his wrath, to the abuse of his love? The riches — the abundance — of his goodness, forbearance, and longsuffering — seeing thou both hast sinned, dost sin, and wilt sin. All these are afterwards comprised in the single word <em>goodness</em>. Leadeth thee — that is, is designed of God to lead or encourage thee to repentance.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>This word properly means to contemn or to treat with neglect. It does not mean here that they professedly treated God's goodness with contempt; but they perverted and abused it. They did not regard it as fitted to lead them to repentance; but they derived a practical impression that because God had not cut them off, he did not regard them as sinners, or that they were innocent and safe.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "5": {
            "synthesis": "<p>The hardened heart does not remain neutral — it actively accumulates divine wrath. Wesley's image is arresting: the one who thinks himself treasuring up all good things is in fact laying up wrath against the day of judgment, each unrepented sin adding to the store. Calvin sees impenitence as the inevitable consequence of hardening oneself against God's admonitions — a trajectory ending in open provocation of the Lord. Clarke connects the Greek term (<em>ametanoēton</em>) to the idea of a heart that has become incapable of repenting rather than merely unwilling — the hardness has become structural.</p><p>Ellicott captures the severity in the contrast between accumulation and discharge: guilt is laid up gradually, little by little, but the punishment will come in one overwhelming tide. Barnes grounds the diagnosis anthropologically: hardness is a state of mind where no motive makes any impression, where every appeal God sends simply bounces off an insensible surface.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>When we become hardened against the admonitions of the Lord, impenitence follows; and they who are not anxious about repentance openly provoke the Lord. It is an impenitable rather than an impenitent heart — that is, a heart incapable of repenting.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The one condition upon which the goodness of God will come into operation, you directly contravene. Instead of being penitent, you are impenitent, and therefore the load of wrath which you have been accumulating against yourself remains unremoved. It is only waiting for the day of judgment to discharge itself upon you. The guilt of man is accumulated little by little; the punishment will be discharged upon him all at once, in one overwhelming tide.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>Treasurest up wrath — although thou thinkest thou art treasuring up all good things. O what a treasure may a man lay up either way, in this short day of life! To thyself — not to him whom thou judgest. In the day of wrath, and revelation, and righteous judgment of God — just opposite to the goodness and forbearance and longsuffering of God.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>The word <em>hardness</em> is used to denote insensibility of mind. It properly means that which is insensible to the touch, or on which no impression is made by contact. Hence it is applied to the mind to denote a state where no motives make an impression; which is insensible to all the appeals made to it — a state of mind where the goodness and forbearance of God makes no impression.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "6": {
            "synthesis": "<p>The declaration that God <em>will render to each one according to his works</em> is one of the most carefully placed sentences in Romans, arriving before Paul establishes universal guilt. Ellicott states its doctrinal force plainly: the consistent teaching of Scripture is that works — the moral tenor of a person's life — will be the standard by which each is judged at the last day. He then acknowledges the apparent tension with justification by faith and invites the reader to hold both as consistent. Calvin reads the verse differently in emphasis: Paul is pointing to genuine righteousness of works as God actually defines it, stripping away every false confidence in religious performance or outward piety that substitutes hollow observance for actual obedience.</p><p>Barnes establishes the governing principle as pure justice: God as righteous judge renders to each as each deserves — a standard that levels Jew and Gentile before the same bar.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>As he had to do with blind saintlings, who thought that the wickedness of their hearts was well covered, provided it was spread over with some disguises of empty works, he pointed out the true character of the righteousness of works — even that which is of account before God — lest they should feel confident that it was enough to pacify him, if they brought words and trifles, or leaves only.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The Apostle here lays down with unmistakable definiteness and precision the doctrine that <em>works</em> — what a man has <em>done</em>, the moral tenor of his life — will be the standard by which he will be judged at the last day. There can be no question that this is the consistent doctrine of Scripture. How is this to be reconciled with the main theme of the Epistle, justification by faith?</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>Who will render — that is, who will make retribution as a righteous Judge; who will give to every man as he deserves. This is a general principle, and it is clear that in this respect God would deal with the Jew as he does with the Gentile. This general principle the apostle is establishing, that he may bring it to bear on the Jew, and to show that he cannot escape simply because he is a Jew.</p>"
                }
            ],
            "consensus": "mixed",
            "key_tension": "Ellicott and Barnes read this as straightforwardly establishing the justice of divine judgment by works; Calvin reads it as stripping false confidence by pointing to what genuine righteousness before God actually requires, as opposed to the hollow performances the self-righteous offer."
        },
        "7": {
            "synthesis": "<p>Those who receive eternal life are described in terms of their sustained orientation: patient continuance in well-doing, seeking glory, honor, and immortality. Calvin notes that perseverance requires not only sustained effort but patience against every obstacle Satan places in the way; and he stresses that what the faithful seek is God's favor, not any merit of their own — the seeking is the evidence, not the ground, of their standing. Ellicott reads the syntactical awkwardness as Paul's earnestness overriding his rhetoric: those who honestly seek this life shall find it, with the stress falling on <em>patient</em> as the defining quality of the seeking.</p><p>Barnes draws from the consistent witness of Scripture that none will be saved except those who persevere in holiness — the one who perseveres gives evidence of genuine piety; the one who does not has never truly begun. Wesley briefly and pointedly notes that pure love does not exclude faith, hope, and desire.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>Patience also is required in the saints, by which they may continue firm, though oppressed with various trials. For Satan suffers them not by a free course to come to the Lord; but he strives by numberless hinderances to impede them, and to turn them aside from the right way. And when he says that the faithful aspire after the divine glory by continuing in good works, he does not mean that they aspire after any thing else but the favor of God.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The stress is upon the words <em>by patient continuance in well doing</em>. From the point of view of rhetoric, no doubt exception might be taken to the tautology; but St. Paul was far too much in earnest to attend carefully to the laws of rhetoric, and it is just this spontaneity which is in great part the secret of his power. Those who honestly seek for this life shall find it.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>It means that they who so continue or persevere in good works as to evince that they are disposed to obey the law of God. It does not mean those who perform one single act, but those who so live as to show that this is their character — to obey God. It is the uniform doctrine of the Bible that none will be saved but those who persevere in a life of holiness.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "8": {
            "synthesis": "<p>Against those who persevere in good-doing, Paul sets the contentious — those who are factious and self-seeking in their relation to God, who disobey the truth and obey unrighteousness instead. Ellicott recovers the word from mistranslation: the underlying Greek denotes one acting in the spirit of a hireling, with factiousness and self-interest, not primarily a quarrelsome disposition toward other people but an orientation of rebellion toward God. Calvin notes the grammatical irregularity — the second half of the contrast is expressed differently from the first — but the theology is clear: these are the disobedient, and upon them fall wrath, fury, tribulation, and anguish.</p><p>Wesley draws a sharp connection to Psalm 78:49, the plagues of Egypt, and suggests that the Jews' greater privileges will place them in the foremost rank of those so punished. Barnes names the disposition plainly as rebellion: contending with the Almighty, resisting his claims, refusing submission.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p><em>That are contentious</em> — an error in the Authorised version through a wrong derivation of the word. Strictly, <em>to those who act in the spirit of a hireling</em>; hence, according to the secondary meaning of the word, <em>to those who act in a spirit of factiousness and self-seeking</em>. It is, in fact, a disposition toward God — rebellious, self-seeking, refusing his obligations.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>But to them that are contentious — like thee, O Jew, who thus fightest against God. The character of a false Jew is disobedience, stubbornness, impatience. Indignation and wrath, tribulation and anguish — alluding to Psalm 78:49, intimating that the Jews would in the day of vengeance be more severely punished than even the Egyptians were when God made their plagues so wonderful.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>This expression here evidently denotes a disposition towards God, and is of the same signification as <em>rebellious</em>, or as opposing God. They who contend with the Almighty; who resist his claims, who rebel against his laws, and refuse to submit to his requirements, however made known. One striking characteristic of the sinner is, that he contends with God.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "9": {
            "synthesis": "<p>Tribulation and anguish fall on every human being who does evil — <em>the Jew first and also the Greek</em>. Calvin notes that the Jew takes precedence precisely because they had, in preference to others, both the promises and the threatenings of the law — privilege intensifies accountability. Ellicott observes that the phrase <em>upon every soul of man</em> is more pointed than <em>upon every man</em>: the punishment will be felt in the soul, the seat of moral life, not merely in external circumstance.</p><p>Clarke underlines the proportionality: the Jew, possessing greater privileges and having abused greater mercies, stands first; the Gentile, having what God saw as sufficient for his state, faces punishment proportioned to his demerit. Wesley stresses that the Jew's having true religion and receiving Christ's mission first will place him in the foremost rank of those who obey not the truth.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He simply places the Jew in opposition to the Gentile. But the Jews take the precedence in this case, for they had, in preference to others, both the promises and the threatenings of the law; as though he had said, This is the universal rule of the divine judgment; it shall begin with the Jews, and it shall include the whole world.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p><em>Upon every soul of man</em> — the phrase is not quite the same as <em>upon every man</em>, but more special in character, indicating the part in which the punishment will be felt.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>Misery of all descriptions, without the possibility of escape, will this righteous Judge inflict upon every impenitent sinner. The Jew first, as possessing greater privileges, and having abused greater mercies; and also on the Gentile, who, though he had not the same advantages, had what God saw was sufficient for his state; and, having sinned against them, shall have punishment proportioned to his demerit.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>Of the Jew first — here we have the first express mention of the Jews in this chapter. And it is introduced with great propriety. Their having been trained up in the true religion, and having had Christ and his apostles first sent to them, will place them in the foremost rank of the criminals that obey not the truth.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "10": {
            "synthesis": "<p>The symmetry Paul constructs is deliberate: just as tribulation and anguish fall on the Jew first and also the Greek, so glory, honor, and peace flow to every doer of good — the Jew first and also the Greek. The same ordering applies to blessing as to judgment, establishing God's absolute impartiality in both directions. Wesley maps the terms carefully against their opposites: glory against wrath, honor against indignation, and peace — present and eternal — against tribulation and anguish. The parallelism is not merely rhetorical; it establishes that the very logic of divine judgment is symmetrical.</p><p>Clarke reads this as a statement of eternal blessedness available to every conscientious person, Jew or Gentile, who lives in obedience to the known will of God. The verse prepares for the great axial principle of v.11 — there is no partiality with God — by demonstrating it in both directions.</p>",
            "voices": [
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>While the finally impenitent Jew and Gentile shall experience the fullest effects of the righteous indignation of the supreme Judge, every man that worketh good — that lives in a conscientious obedience to the known will of God, whether he be Jew or Gentile — shall have glory, honor, and peace; that is, eternal blessedness.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>But glory — just opposite to <em>wrath</em>, from the divine approbation. Honour — opposite to <em>indignation</em>, by the divine appointment; and peace now and for ever, opposed to tribulation and anguish.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "11": {
            "synthesis": "<p><em>There is no partiality with God</em> is the axial principle of the chapter's argument. Calvin connects it to his broader movement: the same God who arraigned all mortals as guilty now brings the charge home equally to Jew and Gentile; the privilege of possessing the law is no defense. Ellicott reaches for the historical significance: the great result of the Christian revelation was to break down belief in race-religions — to demolish the middle wall of partition that separated the covenant people from the world.</p><p>The principle does not deny that God distributes advantages unequally. Wesley notes it is well consistent with his distributing advantages and opportunities according to his own good pleasure — but those advantages do not alter the standard of judgment. Barnes defines partiality precisely: favoring one party not because his cause is more just, but on account of wealth, rank, or personal relationship. God has no such bias, and the judgment falls accordingly.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He has hitherto generally arraigned all mortals as guilty; but now he begins to bring home his accusation to the Jews and to the Gentiles separately. At the same time he teaches us that it is no objection that there is a difference between them, but that they are both without any distinction exposed to eternal death. The Gentiles pretended ignorance as their defense; the Jews gloried in the honor of having the law.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Regard for the external circumstances of a man as opposed to his internal condition — here, especially, regard for the circumstances of birth and race. The great result of the Christian revelation was to break down the belief in <em>race-</em>religions — the <em>middle wall of partition</em>, as St. Paul calls it. The essential equality of Jew and Gentile before God is not affected by their difference of privilege.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>For there is no respect of persons with God — he will reward every one according to his works. But this is well consistent with his distributing advantages and opportunities of improvement, according to his own good pleasure.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>The word thus rendered means <em>partiality</em>, in pronouncing judgment, in favouring one party or individual more than another, not because his cause is more just, but on account of something personal — on account of his wealth, or rank, or office, or influence. It has special reference to a judge who pronounces judgment contrary to justice from corrupt motives. God has no such bias.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "12": {
            "synthesis": "<p>Paul now works out the logic of impartial judgment across the two human situations. Gentiles who sinned <em>without the law</em> — that is, without the written revelation given at Sinai — will perish without that law serving as their specific measure; Jews who sinned under the law will be judged by the law they possessed. Ellicott draws out the essential fairness: each is judged by the method proper to his case. Calvin is pointed: the Gentile's ignorance of a written law does not constitute a defense, since condemnation follows from the sin itself, not from the code against which it is measured.</p><p>Clarke specifies the dispensations at issue: the Gentile lived under the inferior dispensation of natural conscience; the Jew under positive divine revelation. The result is that neither can claim exemption on the grounds of their respective positions. Wesley observes that Paul speaks as of time past because all time will be past at the day of judgment.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>In the former part of this section he assails the Gentiles; though no Moses was given them to publish and to ratify a law from the Lord, he yet denies this omission to be a reason why they deserved not the just sentence of death for their sins; as though he had said — that the knowledge of a written law was not necessary for the just condemnation of a sinner.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Jew and Gentile alike will be judged, each by the method proper to his case; the Jew by the written Law against which he has sinned, the Gentile by the unwritten law of conscience against which he too has sinned. The Gentile, who, at the dictates of conscience, acts as if he were subject to law, shall have the full benefit that law can give him. His conscience is to him a law.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>They, the Gentiles, who shall be found to have transgressed against the mere light of nature shall not come under the same rule with those, the Jews, who have in addition enjoyed an extraordinary revelation; but they shall be dealt with according to the inferior dispensation under which they lived: while those, the Jews, who have sinned against the law — the positive Divine revelation — shall be judged by that law.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>For as many as have sinned — he speaks as of the time past, for all time will be past at the day of judgment. Without the law — without having any written law — shall also perish without the law — without regard had to any outward law; being condemned by the law written in their hearts. The word <em>also</em> shows the agreement of the manner of sinning with the manner of suffering.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "13": {
            "synthesis": "<p>A central axiom dropped into the argument: the hearers of the law are not righteous before God; the doers will be justified. Calvin reads this as anticipating the Jewish objection that possession and knowledge of the law sufficed; Paul declares the claim groundless — obedience, not possession, is what God requires, since only those who do what the law says will live by it. Ellicott notes that mere existence under the law does not exempt from judgment; the only exemption belongs to those who have actually kept it, which Paul is about to show no one has.</p><p>Wesley is insistent that there is no parenthesis beginning here, and that the principle extends to Gentiles as well as Jews. Barnes traces the same axiom through James 1:22 and Matthew 7:21 — those who hear but do not do merely deceive themselves; actual obedience is the only evidence of righteousness before God.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>This anticipates an objection which the Jews might have adduced. As they had heard that the law was the rule of righteousness, they gloried in the mere knowledge of it: to obviate this mistake, he declares that the hearing of the law or any knowledge of it is of no such consequence that any one should on that account lay claim to righteousness, but that works must be produced.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>They must not suppose that the mere fact of their being under the Law will exempt them from this judgment. The only exemption will be that which is given to those who have <em>kept</em> the Law, and not merely had the privilege of hearing it.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>For not the hearers of the law are, even now, just before God, but the doers of the law shall be justified — finally acquitted and rewarded: a most sure and important truth, which respects the Gentiles also, though principally the Jews. There is therefore no parenthesis here; for the sixteenth verse also depends on the fifteenth, not on the twelfth.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>The same sentiment is implied in James 1:22 and Matthew 7:21. The apostle here doubtless designed to meet an objection of the Jews; to wit, that they had the law, that they manifested great deference for it, that they heard it read with attention, and professed a willingness to yield themselves to it. To meet this, he states a very plain and obvious principle — that this was insufficient to justify them before God unless they rendered actual obedience.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "14": {
            "synthesis": "<p>The Gentile who <em>by nature</em> does the things the law requires becomes a law to himself — a pivotal claim about natural moral knowledge. Calvin argues that Paul's point is not that all Gentiles fulfill the law but that there is no nation so wholly lost that it does not keep within the limits of some laws; moral conscience is a universal human endowment, however corrupted. Ellicott reads <em>by nature</em> as meaning spontaneously, without the coercion of any external rule — the point is internal prompting rather than external compulsion.</p><p>Wesley makes a pointed qualification: even this natural law-keeping is <em>strictly speaking by preventing grace</em>, refusing to ground it in unassisted human capacity. Barnes treats the verse as a hypothetical case Paul introduces to show that the heathen have sufficient moral knowledge to be accountable — not as a factual description of Gentile achievement in obedience.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He indeed shows that ignorance is in vain pretended as an excuse by the Gentiles, since they prove by their own deeds that they have some rule of righteousness: for there is no nation so lost to every thing human, that it does not keep within the limits of some laws. Since then the Gentiles have the righteousness of the law, though unwritten, engraven on their minds, the plea of ignorance is taken from them.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p><em>By nature</em> — spontaneously; of their own motion; not acting under the coercion of any external rule, but simply by the promptings of their own conscience left to itself. The things of the law — in this one instance the article is used, meaning, however, not the Mosaic law specifically, but <em>what law in its idea implies and requires.</em></p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>For when the Gentiles — that is, any of them — do by nature — that is, without an outward rule; though this also, strictly speaking, is by preventing grace — the things contained in the law — the ten commandments being only the substance of the law of nature — these, not having the written law, are a law to themselves.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>This verse is not to be understood as affirming, as a historical fact, that the Gentiles do keep the law of God. The apostle does not expressly affirm that this was ever done; but he supposes the case, to show the true nature and value of the rites of the Jews, and to show that the heathen have sufficient knowledge of his will to take away every excuse for sin.</p>"
                }
            ],
            "consensus": "mixed",
            "key_tension": "Calvin and Ellicott read vv.14-15 as describing an actual moral phenomenon — the Gentile conscience showing genuine moral knowledge; Barnes treats the case as hypothetical and illustrative; Wesley grounds even natural law-keeping in prevenient grace rather than in unaided human nature."
        },
        "15": {
            "synthesis": "<p>Where the law is not written on tablets of stone, it is written on hearts — and the conscience provides its own two-sided testimony. Ellicott captures the structure: there is a double witness — actions speak externally and conscience speaks internally, the two together providing equivalent evidence to what the written Law provides for the Jew. Wesley reaches for courtroom imagery: conscience functions as plaintiff, defendant, and witness alternately, with thoughts on both sides of the moral ledger accusing or excusing in turn.</p><p>Clarke connects this to Paul's earlier point: as the obedient Gentile demonstrates that the great object of the law — to bring people from injustice, cruelty, and falsehood — is accomplished even without the written code, their conscience corroborates their conduct. Barnes stresses that the Gentile's standard, though different in form, will be the same in substance as the written Law on the day of judgment — the will of God is the same whether made known by reason or by revelation.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The work of the law — the practical effect or realisation of the law — written in their hearts as the original Law was written upon the tables of stone. Also bearing witness — there is a double witness; their actions speak for them externally, and conscience speaks for them internally. <em>Between themselves</em> — that is, within themselves — their thoughts alternately accusing and excusing.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>Which show the work of the law — in acting according to justice, mercy, temperance, and truth, they show that the great object of the law, which was to bring men from injustice, cruelty, intemperance, and falsity, is accomplished so far in them: their conscience also bearing witness — that faculty of the soul where that Divine light dwells and works — shows them that they are right.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>Who show — to themselves, to other men, and, in a sense, to God himself — the work of the law written on their hearts. Their conscience — there is none of all its faculties which the soul has less in its power than this — bearing witness, and their thoughts, the mean while, accusing or else excusing one another. Among themselves — alternately, like plaintiff and defendant.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>The work of the law — the design, purpose, or object which is contemplated by the revealed law; to make known to man his duty, and to enforce the obligation to perform it. The will of God, whether made known by reason or revelation, will be the same in substance. In other words, the standard of judgment for the Gentile, though different in form, coincides with the revealed will of God.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "16": {
            "synthesis": "<p>Paul closes the bracket opened at v.12: all of this will be disclosed fully on that day when God judges the secrets of men by Jesus Christ. Ellicott insists that this verse cannot refer to the daily process of conscience described in vv.14-15 but to the final judgment specifically — where the Son functions as Mediator of judgment as he is Mediator of salvation. The secrets that shape the real moral quality of actions will then be made manifest, not just the external acts.</p><p>Wesley underlines that everything will then be shown to be what it really is; and he adds that Paul's phrase <em>according to my gospel</em> means the gospel too carries the force of law. Clarke reads this as Paul's claim that his apostolic proclamation is itself the statement of the principle of impartial, circumstance-sensitive judgment. Barnes connects the verse back to v.12, treating vv.13-15 as parenthetical, with heathen and Jew arraigned at the same bar, each judged by their own standard.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>This verse takes up the main thread of the subject. It cannot refer to what immediately precedes, because there the Apostle is referring to the daily process that goes on whenever doubtful actions are submitted to the law of conscience; here he is speaking expressly of the final judgment held by God and not by man. As the Son of God is the Mediator of salvation, so also is He the Mediator of judgment.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>And all this shall be farther exemplified and proved in the day when God shall judge the secrets of men by Jesus Christ; which judgment shall be according to my Gospel — according to what I am now laying down before you, relative to the impartiality of God, and his righteous procedure in judging men not according to their opinions or prejudices, but according to the various advantages or disadvantages of their actual situation.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>In the day — that is, who show this in the day. Everything will then be shown to be what it really is. In that day will appear the law written in their hearts as it often does in the present life. On secret circumstances depends the real quality of actions, frequently unknown to the actors themselves. According to my gospel — hence it appears that the gospel also is a law.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "17": {
            "synthesis": "<p>Having established the general principles of impartial judgment, Paul turns with full directness to the Jew — but with rhetorical skill, he first concedes all their claimed privileges before turning those privileges into charges. The catalog is extensive: the name Jew, resting on the law, glorying in God, knowing the divine will, discerning what is excellent. Wesley structures the passage as two sets of five articles, the first about what the Jew boasts in himself, the second about what he claims with respect to others.</p><p>Ellicott notes a significant textual matter: the KJV <em>behold</em> should read <em>but if</em>, making this verse the beginning of a conditional whose answering clause falls at v.21. Clarke observes that Paul's entire purpose is to demonstrate that superior knowledge, privileges, and profession serve only to aggravate condemnation when matched against actual conduct — and Barnes notes the pastoral skill of granting all their claims before pressing the charges.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>The Jews take the precedence in this case, for they had, in preference to others, both the promises and the threatenings of the law. Now Paul concedes to them the knowledge of the divine will, and the approval of things useful; and this they had attained from the doctrine of the law. But there is a twofold approval — one of choice, when we embrace the good we approve; the other of judgment, by which indeed we distinguish good from evil, but by no means strive or desire to follow it.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>An interesting case of a corrupt reading which has found its way into the Authorised version. For <em>behold</em>, a decisive consensus of the best MSS. has <em>but if.</em> Adopting <em>but if</em>, the answering clause of the sentence is to be found in the question, <em>Teachest thou not thyself?</em> at Romans 2:21. Turning to the Jew, the Apostle breaks out into indignant and vehement apostrophe.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>The apostle now throws off the cover, and openly argues with him in the most plain and nervous manner; asserting that his superior knowledge, privileges, and profession, served only to aggravate his condemnation. And that, in fact, he who, under all his greater advantages, transgressed the law of God, stood condemned by the honest Gentile who, to the best of his knowledge, obeyed it.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>By the use of the word <em>behold</em> he calls their attention to it as to an important subject; and with great skill and address, he states their privileges, before he shows them how those privileges might enhance their condemnation. He admits all their claims to pre-eminence in privileges, and then with great faithfulness proceeds to show them how those privileges aggravated their guilt.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "18": {
            "synthesis": "<p>The Jew knows God's will from the law and can discern what is most excellent — two gifts of privilege that mark him off from the Gentile. Calvin identifies a crucial distinction between two levels of discernment: the approval of judgment, by which one distinguishes good from evil, and the approval of choice, by which one actually embraces and pursues the good. The Jew possesses the first abundantly through the law, but the apostle's charge will be that the second is missing in practice.</p><p>Ellicott draws out an ambiguity in the Greek verb rendered <em>approvest</em>: it can mean either to approve (embrace the good) or to discriminate (distinguish good from evil), and probably indicates here the intellectual capacity to make moral distinctions, formed by constant synagogue reading of the law. Clarke stresses the privilege: God's revelation makes the finest moral distinctions possible, showing not merely what is obligatory but what is most excellent in God's sight. Barnes notes this knowledge distinctly marked the Jews from all other nations.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He now concedes to them the knowledge of the divine will, and the approval of things useful; and this they had attained from the doctrine of the law. But there is a twofold approval — one of choice, when we embrace the good we approve; the other of judgment, by which indeed we distinguish good from evil, but by no means strive or desire to follow it. Thus the Jews were so learned in the law that they could pass judgment on the conduct of others, but were not careful to regulate their life according to that judgment.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p><em>His will</em> — literally, <em>the will</em> — the supreme will. <em>Approvest the things that are more excellent</em> — probably rightly given in the Authorised version, though the marginal rendering is also possible: <em>triest the things that differ</em>, that is, art able to discriminate between good and evil. <em>Being instructed</em> — with reference to the constant reading of the Law in the synagogue.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>Knowest his will — hast been favored with a revelation of his own will, immediately from himself. The things that are more excellent — that revelation which God has given of himself makes the nicest distinctions between right and wrong; between vice and virtue; showing how you should walk so as to please God, and, consequently, acquire the most excellent portion that human spirits can have on this side heaven.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>And knowest his will — the will or commands of God. This knowledge they obtained from the Scriptures; and of course in this they were distinguished from other nations. The word rendered <em>approvest</em> can mean either to approve or to distinguish. This is probably its meaning here, referring rather to the intellectual process of discerning good from evil, a process formed by the instruction of the law.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "19": {
            "synthesis": "<p>The Jew's self-confidence reaches its height: he is persuaded he can serve as moral guide to the blind, a light in darkness, a corrector of the foolish, a teacher of children. Calvin notes that this confidence was partly grounded in reality — the Jews did have more light than surrounding nations — but Paul grants it precisely in order to intensify the accusation when practice fails to match the claim. The concession is rhetorical and pointed.</p><p>Ellicott cross-references Matthew 15:14, where Jesus describes the Pharisees as blind leaders of the blind — the confident guide turns out to share the blindness he purports to cure. Clarke reads the verse as capturing Jewish self-understanding accurately: they believed the Gentiles were babes and fools by comparison, and that all nations must look to them for the only true knowledge. Barnes notes that Jewish confidence in their religion was not mere hypocrisy but genuine, full conviction — they were not speculative infidels.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>More is still granted to them; as though they had not only what was sufficient for themselves, but also that by which they could enrich others. He grants, indeed, that they had such abundance of learning, as that others might have been supplied. He grants all this in order to press the accusation the more sharply when he shows their conduct to be wholly inconsistent with it.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p><em>A guide of the blind</em> — comp. Matthew 15:14, <em>They be blind leaders of the blind. And if the blind lead the blind</em> — the confident guide turns out to share the very blindness he purports to cure.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>And art confident — in consequence of all these religious advantages, ye believe that ye are able to teach others, and to be guides and lights to the bewildered, darkened Gentiles, who may become proselytes to your religion. They believed the Gentiles to be in utter ignorance and moral darkness, from which they alone could deliver them.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>This expression denotes the full assurance of the Jew that he was superior in knowledge to all other people. It is a remarkable fact, that the Jews put the fullest confidence in their religion. Though proud, wicked, and hypocritical, yet they were not speculative infidels. It was one of their characteristics through all their history that they had the fullest assurance that God was the Author of their institutions.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "20": {
            "synthesis": "<p>The catalog of Jewish privilege climaxes with the claim to possess <em>the form of knowledge and truth</em> — the law as the complete embodiment of all that is genuinely worth knowing. Calvin reads <em>form</em> (μόρφωσις) not as empty form opposed to substance but as a sketch, a delineation, a summary — the Jews genuinely claimed to carry in their breasts all the secrets of the law. Ellicott agrees: the word implies substance, not mere appearance — <em>presentation</em> or <em>embodiment</em> of knowledge and truth.</p><p>Clarke notes that the Jews considered themselves the sole possessors of the only true knowledge, and that all nations were dependent on them for the system of eternal truth derived from the law. Barnes observes that Paul here is giving the Jews' own self-description, one that was not without foundation — their failure was not in claiming the privilege but in never matching the claim with life.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>It may be thus explained: because thou hast the form of knowledge, they professed to be the teachers of others, because they seemed to carry in their breasts all the secrets of the law. The word <em>form</em> is put for model, for pattern; the same word occurs in 2 Timothy 3:5 in <em>the form of godliness</em>. It is taken here in a good sense, as meaning a sketch, a delineation, an outline, a representation, or a summary.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p><em>The form of knowledge and of the truth</em> — as we might say, <em>the presentation of knowledge and of truth.</em> Here not form as opposed to substance, but as implying substance — <em>presentation</em>, or <em>embodiment</em> of knowledge and truth.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>An instructer of the foolish — ye believe the Gentiles to be babes and fools when compared with yourselves; that ye alone possess the only true knowledge; that ye are the only favourites of Heaven; and that all nations must look up to you as possessing the only form of knowledge — the grand scheme and draught of all true science, of every thing that is worthy to be learned: the system of eternal truth, derived from the law.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>The word <em>foolish</em> here signifies those who are void of understanding. The expression is figurative, and denotes those who were as ignorant as children — a term they were likely to apply to all the Gentiles. It is evident that the character here given by Paul to the Jews is one which they claimed for themselves, and which was not without foundation. Their failure was that the claim was never matched by life.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "21": {
            "synthesis": "<p>The rhetorical turn is sharp and devastating: you who teach others, do you teach yourself? The one who preaches against theft has convicted himself when he steals; the moral instructor becomes the moral defendant. Wesley compresses the principle into an epigram: <em>he does not teach himself who does not practise what he teaches.</em> Calvin notes that Paul reverses the usual order here — he addresses sins against neighbor (theft), self (adultery), and God (sacrilege) — the inverse of his treatment of Gentile sin in chapter one.</p><p>Ellicott notes that <em>therefore</em> at v.21 is resumptive, referring back to the conditional <em>but if</em> of v.17, the long parenthesis of vv.18-20 now complete and the conditional's consequence now being drawn. Barnes observes that the question form is chosen because it conveys truth with greater rhetorical force — the implied answer is inescapable and well established by the evidence Paul goes on to adduce.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>It is worthy of notice, that the Apostle, after the Hebrew manner, reverses the order as to the points he mentions; he, as it were, retrogrades, and begins to do so at Romans 2:21. He addresses sins against neighbour, then against self, then against God — the inverse of his treatment of Gentile sin in chapter one, where sins against God come first.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p><em>Therefore</em> — see above on Romans 2:17. The word is resumptive, or, as it is technically called, <em>epanaleptic</em> — taking up the thread of the conditional clause, <em>but if thou art called a Jew</em>, after the parenthetical description of Jewish privilege in vv.18-20, and now drawing the consequence.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>Thou dost not teach thyself — he does not teach himself who does not practise what he teaches. Dost thou steal, commit adultery, commit sacrilege — sin grievously against thy neighbour, thyself, God. St. Paul had shown the Gentiles first their sins against God, then against themselves, then against their neighbours. He now inverts the order: for sins against God are the most glaring in a heathen, but not in a Jew.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>He who is a teacher of others may be expected to be learned himself. They ought to be found to be possessed of superior knowledge; and by this question the apostle impliedly reproves them for their failure. The form of a question is chosen because it conveys the truth with greater force. He puts the question as if it were undeniable that they were grossly inconsistent in conduct.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "22": {
            "synthesis": "<p>The accusation escalates from theft to adultery and finally to sacrilege — and the last charge is the most pointed, because the Jew who abhorred idolatry as the characteristic Gentile degradation was apparently not above treating idol temples as legitimate plunder. Calvin traces this to a universal category: sacrilege is the profanation of the divine majesty, and whether one plunders a pagan temple or treats God's commands with contempt, the category is the same — a violation of what belongs to God.</p><p>Ellicott notes that the charge of robbing pagan temples was commonly brought against Jews in this period (compare Acts 19:37, where the Ephesus town clerk specifically acquits Paul's companions of this charge, implying the accusation was current and credible). Barnes documents that the Jewish Talmud itself accuses certain celebrated rabbis of adultery by name, and defines sacrilege more broadly as devoting to improper purposes what rightly belongs to God.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He fitly compares sacrilege to idolatry, as it is a thing of the same kind; for sacrilege is simply a profanation of the Divine Majesty, a sin not unknown to heathen poets. As the Gentiles ascribed the majesty of their gods to idols, they only thought it a sacrilege when any one plundered what was dedicated to their temples. But Paul here points to the general truth: whatever violates what belongs to God falls under the same category.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p><em>Commit sacrilege</em> — properly, <em>rob temples</em>, idol temples, with a pointed antithesis to that abhorrence of idols on which the Jew prided himself. They may have thought the idol temples fair plunder. At any rate, it is clear that this charge was commonly brought against them. Comp. Acts 19:37, where the town-clerk of Ephesus specially acquits Paul and his companions of robbing temples, implying the charge was current.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>There is no doubt that adultery was a crime very common among the Jews. The Jewish Talmud accuses some of the most celebrated of their rabbies, by name, of this vice. Sacrilege is the robbing of God; withholding from him what is his due, or devoting to other purposes what is owed to him. Thus understood, it stands as the culmination of the charge against those who boast in the law while breaking it.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "23": {
            "synthesis": "<p>The charge is crystallized: the Jew who boasts in the law dishonors God by breaking it. Calvin locates the particular weight of this accusation in the fact that the Jews avowed God as their lawgiver — their transgression was not merely a moral failure but a contradiction of their highest profession. Ellicott notes the structural choice: whether v.23 is read as a question or as a summary statement, its force is identical — boasting proclaimed conviction of the law's excellence, while breaking it denied that conviction in practice.</p><p>Barnes makes a penetrating observation about the epistemology of conduct: actions are the truest test of real opinions. Whatever a person's speculative theology may assert about God's law, his life delivers a verdict that carries more evidential weight than his words. A life of transgression does the law more dishonor than any boast does it honor, and the watching Gentile world draws its own conclusions accordingly.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>Though every transgressor dishonors God, yet he justly imputes in this respect a special fault to the Jews; for as they avowed God as their Lawgiver, and yet had no care to form their life according to his rule, they clearly proved that the majesty of their God was not so regarded by them, but that they easily despised him.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>This verse has been regarded, not as a question, but as a summary answer to the previous questions: <em>You, who make all this boast in the Law, by breaking the Law, dishonour God.</em> There is a certain force in this view. Boasting of the law proclaimed their conviction of its excellence and obligation; breaking it denied it in practice, and the denial carries more weight.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>To boast in the law implied their conviction of its excellence and obligation, as a man does not boast of that which he esteems to be of no value. By boasting of the law, they proclaimed their conviction that it was from God. By breaking it, they denied it. And as actions are a true test of men's real opinions, their breaking the law did it more dishonour than their boasting of it did it honour.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "24": {
            "synthesis": "<p>Paul cites Scripture to confirm what practice has demonstrated: <em>The name of God is blasphemed among the Gentiles because of you.</em> The source of the quotation is disputed — Calvin thinks Ezekiel 36:20 is more likely than Isaiah 52:5, since Ezekiel is full of reproofs directed at the people's own conduct; Ellicott finds it in the LXX of Isaiah 52:5 and notes that Paul takes the aptest words available without being careful about their original context. Both agree that the prophetic tradition grounds the charge.</p><p>Clarke supplies a remarkably apt rabbinic parallel from Debarim rabba, where a rabbi is condemned for preaching against usury while practicing it — the very pattern Paul is describing. Barnes presses the practical point: Jewish hypocrisy and crime led the pagan world to despise a religion observed to have no effect over its professors, and the reproach terminated ultimately on God himself.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>I think this quotation is taken from Ezekiel 36:20, rather than from Isaiah 52:5; for in Isaiah there are no reproofs given to the people, but that chapter in Ezekiel is full of reproofs. Some think that it is a proof from the less to the greater: since the Prophet upbraided the Jews of his time that on account of their captivity, the glory of God was ridiculed among the Gentiles, much more will this apply when the cause is the people's own moral failure.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>From the LXX version of Isaiah 52:5. The sense of the original is that the name of God is dishonoured by the enslavement and oppression of his people. The Apostle is not careful as to the particular context from which he draws. He knew that he was giving the substance of Scripture, and he takes the aptest words that occur to him at the moment.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>In Debarim rabba it is said: The rulers destroy the influence of their own words among the people; and this is done when a rabbin, sitting and teaching in the academy, says, Do not take usury, and himself takes it; do not commit rapine, and himself commits it. That the Jews were exceedingly lax in their morals is thus demonstrated from their own sources.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>That is, your conduct is such as to lead the heathen world to blaspheme and reproach both your religion and its Author. By your hypocrisy and crimes the pagan world is led to despise a religion which is observed to have no effect in purifying and restraining its professors; and of course the reproach will terminate on the Author of your religion — that is, the true God.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "25": {
            "synthesis": "<p>Circumcision, the covenant sign of belonging to Israel, is of genuine value — but only conditionally. Calvin argues that circumcision was always a spiritual symbol: it pointed to the inward cutting away of corruption, and when that spiritual reality was absent the sign had no effect and in fact became a liability. The distinction between sign and reality signed is what the entire argument hinges on. Wesley notes sharply that Paul does not say circumcision <em>justifies</em> — only that it <em>profits</em> — and that profit is thoroughly conditional.</p><p>Clarke introduces a striking rabbinic parallel that actually supports Paul's argument: even the rabbis themselves allowed that an apostate or ungodly Israelite must go to hell despite his circumcision. Barnes explains the covenantal background: circumcision was the rite by which membership in Abraham's commonwealth was recognized, a real advantage — but always an advantage conditional on the obedience it signified.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He dissipates by anticipation what the Jews might have objected in their defense: since circumcision was a symbol of the Lord's covenant, they seemed not to have gloried in vain; but as they neglected what the sign signified, and regarded only the outward form, he gives this answer — that they had no reason to lay claim to any thing on account of the bare sign. The true character of circumcision was a spiritual promise, which required faith for its reception.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>For circumcision verily profiteth — it is a blessing to belong to the Church of God and wear the sign of the covenant, provided the terms of the covenant are complied with. But if thou be a breaker of the law — if thou do not observe the conditions of the covenant, the outward sign is both without meaning and without effect. This was a maxim of the rabbins themselves; for they allowed that an apostate or ungodly Israelite must go to hell, notwithstanding his circumcision.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>Circumcision indeed profiteth — he does not say <em>justifies</em>. How far it profited is shown in the third and fourth chapters. Thy circumcision is become uncircumcision — is so already in effect. Thou wilt have no more benefit by it than if thou hadst never received it. The very same observation holds with regard to baptism.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>This was the peculiar rite by which the relation to the covenant of Abraham was recognised; or by which the right to all the privileges of a member of the Jewish commonwealth was acknowledged. The apostle was not disposed to deny that they possessed this advantage; but it was an advantage that was conditional on the obedience it signified, not a guarantee of exemption from judgment.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "26": {
            "synthesis": "<p>If circumcision without law-keeping becomes uncircumcision, the reverse also holds: the uncircumcised Gentile who keeps the law's requirements will have his uncircumcision counted as circumcision before God. Calvin frames this as a logical argument about subordination and ends: circumcision looks to the law, is subordinate to it, and must therefore be inferior to it in value; keeping the law exceeds the value of the sign instituted for its sake. The argument is from purpose — the sign exists for the thing signified, not the reverse.</p><p>Clarke reads this as establishing that obedience to the spirit and design of the law, even without the outward rite, has covenantal standing before God. Barnes notes that Paul does not expressly affirm that Gentiles actually achieve this level of obedience, but introduces the case to clarify the true nature and conditional character of Jewish rites — their value was always instrumental, never intrinsic.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>This is a very strong argument. Every thing is below its end and subordinate to it. Circumcision looks to the law, and must therefore be inferior to it: it is then a greater thing to keep the law than circumcision, which was for its sake instituted. It hence follows, that the uncircumcised, provided he keeps the law, far excels the Jew with his barren and unprofitable circumcision, if he be a transgressor of the law.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>Therefore if the uncircumcision keep the righteous requirements of the law — if the Gentile be found to act according to the spirit and design of the law, his acting thus uprightly, according to the light which God has afforded him, will be reckoned to him as if he were circumcised and walked agreeably to the law.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>If the uncircumcision — that is, a person uncircumcised — keep the law — walk agreeably to it — shall not his uncircumcision be counted for circumcision — in the sight of God?</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>The apostle does not expressly affirm that this was ever done; but he supposes the case, to show the true nature and value of the rites of the Jews. Shall not his uncircumcision — shall the fact that he is uncircumcised stand in the way of the acceptance of his services? The implied answer is: no, because the rite's value was always conditional and instrumental.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "27": {
            "synthesis": "<p>The Gentile who fulfills the law will condemn — put to shame by contrast — the Jew who, despite possessing the written law and the external rite of circumcision, transgresses. The logic is the same that Jesus employs in Matthew 12:41-42, where the Ninevites rise in judgment against the generation that rejected him. Ellicott directs the reader there explicitly: the idea is condemnation by contrast, the obedient Gentile standing as a living refutation of the Jew's claim that privilege guarantees standing.</p><p>Calvin specifies the charge precisely: the violation does not come from possessing the outward rite but from persisting in neglect of spiritual worship while maintaining the sign. Barnes resolves the difficult phrase <em>by the letter and circumcision</em>: the preposition marks the condition or circumstance — <em>with all the advantages of the written Law and of circumcision</em> — making the transgression the more inexcusable rather than constituting its cause.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He does not mean that they violated the law, because they had the literal circumcision; but because they continued, though they had the outward rite, to neglect the spiritual worship of God, even piety, justice, judgment, and truth, which are the chief matters of the law. The Gentile who fulfills the substance stands as a living refutation of the claim that the sign suffices.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p><em>Judge thee</em> — comp. Matthew 12:41-42, <em>The men of Nineveh shall rise in judgment with this generation, and shall condemn it.</em> The idea is that of <em>putting to shame by contrast</em>. <em>By the letter</em> — the preposition here marks the condition or circumstance under which the action is done, and might be paraphrased, <em>with all the advantages of the written Law and of circumcision.</em></p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>And shall not uncircumcision, which is by nature — the Gentile, who is by birth not obliged to be circumcised — if it fulfill the law — if such a person act according to the spirit and design of the law — judge, condemn thee, who, whilst thou dost enjoy the letter, the written law, and bearest in thy body the proof of circumcision, dost transgress that law?</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>Yea, the uncircumcision that is by nature — those who are, literally speaking, uncircumcised — fulfilling the law as to the substance of it, shall judge thee — shall condemn thee in that day. Who by the letter and circumcision — who, having the bare, literal, external circumcision — transgressest the law.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "28": {
            "synthesis": "<p>Paul now draws the implications explicitly: genuine Jewish identity is not a matter of descent, profession, or external sign. Calvin grounds this in the whole tenor of Scripture — the people are everywhere commanded to circumcise their hearts, and that inward circumcision is what God himself promises to perform. Wesley states the logic directly: one who is a Jew <em>in outward show only</em> is not a Jew in the most important sense — not one of God's beloved people, whatever his genealogy or ritual status.</p><p>Clarke traces the prophetic background: Jeremiah 4:4, Jeremiah 9:26, and Ezekiel 44:7-9 all define circumcision in its truest sense as a matter of the heart. Barnes frames the point covenantally: the separation of the Jewish people was intended from the beginning to produce a people holy in heart and in life, not merely a people marked externally — a design not generally understood in the time of the apostles, but abundantly declared in the Hebrew Scriptures.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>The meaning is, that a real Jew is not to be ascertained, either by natural descent, or by profession, or by an external symbol; that the circumcision which constitutes a Jew, does not consist in an outward sign only, but that both are inward. What he subjoins with regard to true circumcision, is taken from various passages of Scripture; for the people are everywhere commanded to circumcise their hearts, and it is what the Lord promises to do.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>For he is not a Jew — a genuine member of the Church of God — who has only an outward profession. Neither is that circumcision — circumcision is a rite which represents a spiritual thing, namely, the change and purification of the heart, as may be seen Jeremiah 4:4, Jeremiah 9:26, Ezekiel 44:7, 44:9.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>For he is not a Jew — in the most important sense, that is, one of God's beloved people — who is one in outward show only; neither is that the true, acceptable circumcision, which is apparent in the flesh.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>He who is merely descended from Abraham, and is circumcised, and externally conforms to the law only, does not possess the true character contemplated by the separation of the Jewish people. Their separation required much more. It contemplated a people holy in heart and in life. This cannot be denied, though it was not generally understood in the time of the apostles.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "29": {
            "synthesis": "<p>The chapter closes with one of Paul's most compressed theological statements: a Jew is one inwardly, and circumcision is a matter of the heart, by the Spirit, not by the letter. Calvin explains the grammar of the contrast: the <em>letter</em> is the outward rite without the inward reality; the <em>Spirit</em> is the spiritual design of the rite, which when God's voice penetrates the heart rather than merely sounding at the ears produces genuine transformation and a new identity before God.</p><p>Wesley connects the phrase directly to Deuteronomy 30:6, where God promises to circumcise the hearts of his people — the inward Jew is the one in whom that promise is fulfilled. Clarke insists the circumcision of the heart is <em>by the Spirit of God, who is the author of all spiritual affections and holy purposes.</em> The closing phrase — <em>whose praise is not from man but from God</em> — seals the point: the inward Jew seeks no human recognition for covenant standing, since God alone searches the heart and renders the true and final verdict.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He calls the outward rite without piety the <em>letter</em>, and the spiritual design of this rite the <em>spirit</em>; for the whole importance of signs and rites depends on what is designed. Where the voice of God sounds, all that he commands, except it be received in sincerity of heart, will remain in the letter — that is, in the dead writing; but when it penetrates into the heart, it becomes spirit, that is, it has life and vigor.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>But he is a Jew — a true member of the Church of God — who is one inwardly. And the acceptable circumcision is that of the heart, in the spirit — by the Spirit of God, who is the author of all spiritual affections and holy purposes. Or, every thing here is to be understood spiritually, and not literally; for without holiness none can please God, and without holiness none can see him.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>But he is a Jew — one of God's people — who is one inwardly, in the secret recesses of his soul. And the acceptable circumcision is that of the heart, in the spirit — referring to Deuteronomy 30:6, the putting away all inward impurity — and not in the letter. Whose praise is not from men, but from God — the only searcher of the heart.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>But he is a Jew — he comes up to the design of the Jewish institution; he manifests truly what it is to be a Jew — who is one inwardly, who has the true spirit and fulfills the design of their being separated as a peculiar people. This passage proves that the design of separating them was not merely to perform certain external rites, but to be a people holy in heart and in life.</p>"
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
    print('Romans 2 synthesis complete.')

if __name__ == '__main__':
    main()
