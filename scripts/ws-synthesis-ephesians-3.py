"""
Wide Source Synthesis — Ephesians chapter 3
bookId: ephesians
Run: python3 scripts/ws-synthesis-ephesians-3.py

Sources used: calvin, ellicott, clarke, wesley, barnes, rwp
Note: mhcc not found for Ephesians; jfb ch3 entries are misaligned (Romans content), skipped.
Chapter range: 3  (21 verses)

Key synthesis decisions:
- v5: mixed — Calvin/Ellicott/Barnes treat the mystery as essentially hidden in prior ages;
  Clarke argues the Gentile calling was partially known but the specific form (apart from Mosaic law)
  was not. Wesley distinguishes New Testament prophets as the newly appointed recipients.
- v10: mixed — Calvin argues these are good angels who learn through redemptive history;
  Clarke is uncertain whether principalities/powers means good or evil heavenly beings.
- v15: mixed — Barnes, Locke, Calvin take "of whom" as referring to Christ; Bloomfield, Chandler,
  Erasmus, Clarke refer it to the Father. Ellicott's etymology (patria from pater) yields "fatherhood."
- v18: mixed — four dimensions (breadth/length/depth/height) referred by early fathers to the cross,
  by Calvin to Christ's love from every angle, by Wesley to dimensions of love, by Barnes to the
  scope of universal salvation.
- v19: mixed — Wesley reads the self-correction as conceding full knowledge is impossible; Calvin and
  Ellicott read the paradox as intentional and irreducible.
- Ellicott v2 and v3 are chapter-level structural overviews, not verse-specific — skipped for those verses.
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

EPHESIANS = {
    "3": {
        "1": {
            "synthesis": "<p>Paul opens Ephesians 3 by naming himself "the prisoner of Christ Jesus on behalf of you Gentiles" — a phrase that reframes Roman captivity as apostolic credential rather than disgrace. Calvin notes that Paul's adversaries had used the imprisonment as evidence against his authority, so Paul inverts the argument: his chains are not the mark of a criminal but the seal of an ambassador for the Gentile mission. The very fact of imprisonment becomes evidence that something cosmically significant was happening through Paul's calling.</p><p>Robertson's Word Pictures observes that the phrase "for this cause" (τούτου χάριν) refers back to the preceding argument about God's elective grace, and that Paul may have intended to begin his prayer here but was diverted by the enormity of his own words into the extended parenthesis of vv. 2–13. Wesley captures the pastoral force succinctly: Paul is a prisoner "for your advantage, and for asserting your right to these blessings." The chains, far from undermining the Gentile churches, are the mark of their champion.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>Paul's imprisonment, which ought to have been held as a confirmation of his apostleship, was undoubtedly presented by his adversaries in an opposite light. He therefore points out to the Ephesians that his chains served to prove and to declare his calling; and that the only reason why he had been imprisoned was, that he had preached the gospel to the Gentiles. His unshaken firmness was no small additional proof that he had discharged his office in a proper manner.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>For this cause — That ye may be so "built together," I am a prisoner for you Gentiles — For your advantage, and for asserting your right to these blessings. This it was which so enraged the Jews against him.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>It is possible that Paul started to make the prayer that comes in verses 14–21 when he repeats τούτου χάριν. If so, he is diverted by his own words "the prisoner of Christ Jesus in behalf of you Gentiles" to set forth in a rich paragraph (1–13) God's use of him for the Gentiles.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "2": {
            "synthesis": "<p>Verse 2 introduces the term "stewardship of God's grace" (οικονομίαν) — a commission to manage and distribute what God has entrusted, not merely a personal privilege. Clarke argues that the Greek particle είγε means "since indeed" here rather than a genuine conditional, because Paul takes it as established fact that his readers know his commission. Wesley reduces the stewardship to its essential shape: "a commission to dispense the gracious gospel to you Gentiles in particular."</p><p>Barnes explains the grammar carefully: the particle is "spoken of what is taken for granted," equivalent to Doddridge's rendering "Since I well know you have heard." Calvin adds that Paul had not previously addressed these matters at Ephesus because no controversy over the Gentile calling had yet arisen there; he is not raising a new issue but confirming what was already known. Robertson notes that the aorist construction and the intensive particle γε together point to a confident appeal to known fact — Paul received a specific, stewardship-shaped calling directly from God.</p>",
            "voices": [
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>The compound particle είγε, which is commonly translated <em>if indeed</em>, in several places means <em>since indeed, seeing that</em>, and should be translated so in this verse. Seeing ye have heard of the dispensation of God, which is given me to you-ward: this they had amply learned from the apostle during his stay at Ephesus, for he had not shunned to declare unto them the whole counsel of God.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>The dispensation of the grace of God given me in your behalf — That is, the commission to dispense the gracious gospel; to you Gentiles in particular. This they had heard from his own mouth.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>The particle here is not designed to express a doubt whether they had heard of it or not, for he takes it for granted that they had. Doddridge renders it, "Since I well know you have heard." He had informed them of his being called to be the minister to the Gentiles, and they had had full opportunity to know it.</p>"
                },
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>There is reason to believe that, while Paul was at Ephesus, he had said nothing on these subjects, no necessity for doing so having arisen; for no controversy had taken place among them about the calling of the Gentiles. He did not, of his own accord, raise unnecessary disputes. It was only when opponents compelled him to speak that he explained his views.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "3": {
            "synthesis": "<p>Paul grounds his knowledge of the mystery not in human reasoning or received tradition but in direct divine revelation. Clarke highlights an important textual variant: the best manuscripts read "was made known" (passive) rather than "he made known" (active), which reinforces that Paul did not discover this himself but received it as disclosed to him from outside. Barnes connects this revelation to Paul's Damascus Road calling (Acts 9:15) and to Galatians 1:12, where Paul uses the same formal claim for the origin of his gospel.</p><p>Calvin emphasizes that calling the Gentile inclusion a "mystery" was a deliberate rhetorical move: it preempts the objection of novelty by locating the hiddenness in divine design. Wesley keeps it spare: this is the mystery of "salvation by Christ alone, and that both to Jews and Gentiles." Robertson notes the formal parallel with Galatians 1:12 — κατα ἀποκάλυψιν is Paul's consistent formula for marking the direct, unmediated source of his commission.</p>",
            "voices": [
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>Instead of εγνωρισε, <em>he made known</em>, εγνωρισθη, <em>was made known</em>, is the reading of the best manuscripts. The apostle wishes the Ephesians to understand that it was not an opinion of his own, or a doctrine which he was taught by others, but one that was immediately revealed to him by God himself.</p>"
                },
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He calls the Gentile inclusion a <em>mystery</em> because it was necessary that it should remain hidden until it was revealed by Christ's coming. By this name he endeavors to remove the prejudice which the general displeasure at the event was fitted to excite. His own personal interest in the matter was a proof that it was divine.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>He refers to the revelation which was made to him when he was called to the apostolic office, that the gospel was to be preached to the Gentiles, and that he was converted for the special purpose of carrying it to them. The hitherto concealed truth that the gospel was to be preached to the Gentiles is what he calls the mystery.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>The mystery — Of salvation by Christ alone, and that both to Jews and Gentiles. As I wrote before — Namely, Eph 1:9, 10; the very words of which passage he here repeats.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "4": {
            "synthesis": "<p>Reading this very letter, Paul claims, can produce genuine understanding of his insight into the mystery of Christ. Clarke glosses the phrase simply: when you refer back to what was written, you may see what God has given Paul to know. Barnes explains: "By the bare reading of which you may understand the view which I entertain of the plan of salvation." The "mystery of Christ" is not anything obscure about Christ's person; it is, Barnes clarifies, the plan of salvation that specifically includes the Gentiles, previously concealed and now disclosed.</p><p>Robertson captures the pedagogical point sharply: "Every sermon reveals the preacher's grasp of 'the mystery of Christ.' If he has no insight into Christ, he has no call to preach." Calvin works through the Greek syntax with characteristic care, exploring whether the participle ἀναγινώσκοντες is connected with the preposition or the verb, but the substantive point is clear to all: the letter is itself the vehicle of disclosure.</p>",
            "voices": [
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>Whereby, when ye read — When ye refer back to them. Ye may understand my knowledge — Ye may see what God has given me to know concerning what has been hitherto a mystery — the calling of the Gentiles, and the breaking down the middle wall between them and the Jews, so as to make both one spiritual body, and on the same conditions.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>By the bare reading of which you may understand the view which I entertain of the plan of salvation. The "mystery of Christ" does not refer to anything mysterious in the person of Christ; it means the hitherto concealed truth that the gospel was to be preached to the Gentiles and made fully known among all nations.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>This Epistle will be read in public. My understanding in the mystery of Christ — my comprehension (σύνεσιν). Every sermon reveals the preacher's grasp of "the mystery of Christ." If he has no insight into Christ, he has no call to preach.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "5": {
            "synthesis": "<p>All voices agree that the mystery of Gentile inclusion was not revealed in earlier ages with the clarity now manifest in apostolic proclamation, but they nuance this differently. Calvin explains that calling it "mystery" implied purposeful hiddenness: it had to remain concealed until Christ's coming inaugurated the right moment for disclosure. Ellicott notes that "sons of men" is predominantly an Old Testament expression and does not restrict the earlier audience to Israelites or to prophets alone.</p><p>Clarke offers the most careful historical argument: the Gentile calling was indeed foreshadowed in the prophets, but the specific form of it — salvation on equal footing with Jews, and apart from the Mosaic law — was not made known in that earlier era. Wesley distinguishes New Testament prophets as the newly appointed recipients of the fully disclosed mystery, implying that even Ezekiel, though called "son of man," did not receive this clarity. Barnes stresses that the word "prophets" here refers to inspired teachers in the Christian church, and their inspiration proves the divine origin of the disclosure.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He had simply called it a <em>mystery</em>, but now calls it the <em>mystery of Christ</em> because it was necessary that it should remain hidden until it was revealed by his coming. We must first explain the word, and then inquire why it is said to have remained unknown in all ages. The appellation was given because the proper time for publishing this decree belongs to the kingdom of Christ.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>That the calling of the Gentiles was made known by the prophets is exceedingly clear; but it certainly was not made known in that clear and precise manner in which it was now revealed. Nor was it made known unto them at all that the Gentiles should find salvation without coming under the yoke of the Mosaic law, and that the Jews themselves should be freed from that yoke.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>Which in other — In former, ages was not so clearly or fully made known to the sons of men — To any man, no, not to Ezekiel, so often styled "son of man;" nor to any of the ancient prophets. Those here spoken of are New Testament prophets.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>The word "prophets" here refers to those who exercised the office of prophet or inspired teacher in the Christian church. This proves that those who exercised the office of prophet in the Christian church were inspired. They were persons endowed in this manner for the purpose of imparting to the newly-formed churches the doctrines of the Christian system.</p>"
                }
            ],
            "consensus": "mixed",
            "key_tension": "Clarke argues that earlier prophets knew the Gentile calling partially, while Calvin, Ellicott, and Wesley hold that the full form of the mystery — Gentile salvation apart from the Mosaic law and on equal terms with Jews — was essentially withheld until the apostolic age."
        },
        "6": {
            "synthesis": "<p>The content of the mystery is now named in three interlocking dimensions: the Gentiles are fellow-heirs, fellow-members of the body, and fellow-partakers of the promise in Christ Jesus through the gospel. All voices agree on the substance, though they weight the terms differently. Ellicott sees these as progressive steps in the order of salvation: first acceptance to heirship, then incorporation into the body, then participation in the promise. Wesley compresses each to a terse gloss: "Of God," "under Christ the head," and "the communion of the Holy Ghost."</p><p>Robertson notes that Paul uses three unusual Greek compounds with the prefix συνν- ("together with"): συγκληρονόμα, σύσσωμα, and συμμέτοχα — the second of these ("fellow-members of the body") appears for the first time in Paul's Greek. Clarke connects the fellow-heir language to Paul's extended argument in Romans that Abraham's promise extends to the Gentiles, while Barnes confirms that "fellow-heirs" means entitled to the same privileges as the ancient people of God.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>These three words evidently describe progressive steps in the work of salvation. First comes the acceptance by God to a share in the inheritance as "heirs of God, and joint-heirs with Christ" (Romans 8:17); next, incorporation into one body under one Head; and lastly, the participation in the one great promise of the covenant, the gift of the Holy Spirit.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>That the Gentiles are joint-heirs — Of God. And of the same body — Under Christ the head. And joint-partakers of his promise — The communion of the Holy Ghost.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>Paul is fond of compounds with συν and here uses three of them. <em>Fellow-heirs</em> (συγκληρονόμα) is a late and rare word. <em>Fellow-members of the body</em> (σύσσωμα) is first found here and only here save in later ecclesiastical writers. The Gentiles are here on equal footing with the Jews in all spiritual matters.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "7": {
            "synthesis": "<p>Paul now applies the general statement about Gentile inclusion to himself specifically: he was made a "minister" (διάκονος) of this gospel by grace alone. Clarke presses the literal force of the word: not a grand title but a servant, one who acts under direction; the apostleship is a servanthood, not a lordship. The gift came with a corresponding energy to carry it out, and Ellicott notes that the "effectual working of his power" is not the means but the measure of the gift — the working is itself the grace.</p><p>Calvin guards against any claim that Paul deserved this commission: it was grace, not excellence, and the comparison of persons is entirely out of place. Barnes emphasizes the same point from the other side: there was nothing in Paul's native inclination toward the gospel; the origin was entirely outside himself. Wesley notes the double direction of the power: it was at work both in Paul and through him, the enabling and the effect indistinguishable from each other.</p>",
            "voices": [
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>Whereof I was made a minister — Διάκονος — a deacon, a servant acting under and by the direction of the great Master, Jesus Christ; from whom, by an especial call and revelation, I received the apostolic gifts and office, and by the energy of his power this Gospel which I preached was made effectual to the salvation of vast multitudes of Jews and Gentiles.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The words "given by" should be rendered "given according to." The working of God's power is described, not as the means, but as the measure of the gift of his grace. What is a "gift" in its source is "effectual working" in its actual nature.</p>"
                },
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>To avoid claiming for himself more than is proper, he affirms that it is grace, and that this gift was an exhibition of divine grace. As if he had said, "Inquire not what I have deserved; for in the free exercise of kindness, the Lord made me an apostle of the Gentiles, not for any excellence of mine, but because it pleased him."</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>According to the gift of the grace of God — That is, the apostleship which he hath graciously given me, and which he hath qualified me for. By the effectual working of his power — In me and by me.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "8": {
            "synthesis": "<p>"Less than the least of all saints" is Paul's grammatically compressed paradox — a comparative (ελαχιστότερος) built upon a superlative. Barnes notes that this word does not occur elsewhere in the New Testament: "a word is therefore coined to convey an idea more emphatically." Ellicott situates the expression within a cluster of Pauline self-depreciations (1 Cor. 15:9–10; 2 Cor. 11:30; 1 Tim. 1:15) and observes that in each case the sense of unworthiness is provoked by contemplating God's specific grace to him.</p><p>Calvin notes that the self-abasement simultaneously deflects a personal objection ("Why should God have chosen this man above all others?") while making the grace of God more conspicuous by contrast. Clarke stresses that the purpose of the self-deprecation is to keep the readers' eyes on Christ: "the excellency of the power is of God, and not of man." Wesley captures the paradox elegantly: "Here are the noblest strains of eloquence to paint the exceeding low opinion the apostle had of himself, and the fulness of unfathomable blessings which are treasured up in Christ."</p>",
            "voices": [
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>This is one of the class of expressions peculiar to Paul. The ordinary terms of language do not express the idea which he wishes to convey, and a word is therefore coined to convey an idea more emphatically. The word here used — ελαχιστότερος — does not occur elsewhere in the New Testament. It is a comparative made from the superlative.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>In each case his deep sense of unworthiness is brought out by the thought of God's especial grace and favour to him. The more richly he is endowed, the more deeply does he feel that he deserved nothing — that all is pure grace.</p>"
                },
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He labors to exhibit himself in as humiliating a light as possible, in order that the grace of God may be the more highly exalted. "Who is this man that God should have raised him above all his brethren?" All such comparisons of persons are put to silence by his voluntary abasement.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>Unto me, who am less than the least of all saints, is this grace given — Here are the noblest strains of eloquence to paint the exceeding low opinion the apostle had of himself, and the fulness of unfathomable blessings which are treasured up in Christ.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "9": {
            "synthesis": "<p>The apostle's commission is to "enlighten all" (φωτίσαι πάντας) — to turn the light on, as Robertson puts it, using the image of illumination rather than mere information. Calvin notes the implied metaphor: in this apostleship the grace of God shines with the brightness of noon-day, overcoming all prejudice of novelty. Ellicott observes that while Christ alone is the Light of the world, the apostle as servant reflects and distributes that light, serving as its earthly channel.</p><p>The "fellowship of the mystery" (or "stewardship," as several manuscripts read) points to the communal nature of what was formerly hidden: the mystery is not disclosed to one person but opened for all humanity to share. Clarke notes the force of φωτίσαι — not merely to inform but to flood with light, making visible what was dark. Wesley glosses it as revealing "those mysterious blessings whereof all believers jointly partake." Barnes prefers the textual variant οἰκονομία (stewardship), which several major manuscripts support over κοινωνία (fellowship).</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>The publication of the gospel is called a <em>mystery</em> because it is the will of God that his purpose, which had formerly been hidden, shall now be shared by men. There is an appropriate metaphor in the words φωτίσαι πάντας, conveying the thought that in his apostleship the grace of God shines with the brightness of noon-day.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>And to illuminate all — to give information both to Jews and Gentiles; to afford them a sufficiency of light, so that they might be able distinctly to discern the great objects exhibited in this Gospel. The word κοινωνία, which we properly translate <em>fellowship</em>, here intimates the association of Jews and Gentiles in one Church or body.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>To make see (φωτίσαι) — first aorist active infinitive of φωτίζω, a late verb, to turn the light on. With the eyes of the heart enlightened (Eph 1:18) one can then turn the light for others to see.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "10": {
            "synthesis": "<p>The eternal purpose behind the Gentile mission extends upward into the heavenly realm: through the church, the "manifold wisdom of God" (πολυποίκιλος σοφία) is to be disclosed to "principalities and powers in heavenly places." All voices agree on the remarkable claim that heavenly beings learn from the church, but they differ on who these beings are.</p><p>Calvin argues carefully that these must be good angels: even they, who behold God's brightness, learn progressively through the unfolding of redemptive history. He cites 1 Peter 1:12 (angels desiring to look into these things) as confirmation that such progressive learning is consistent with angelic perfection. Ellicott concurs, noting the same text and 1 Corinthians 4:9. Clarke is more cautious: some take these powers as evil angels (citing Eph. 6:12), but he inclines toward good angels who observe the economy of the gospel as curious, holy spectators. Wesley distills the entire verse to a single memorable image: the church is "the theatre of the divine wisdom." Barnes elaborates the cosmic scope: the universe was made partly so that the redeemed community could display what no other creature can show. Robertson notes that πολυποίκιλος ("much-variegated, with many colours") occurs only here in the New Testament.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>There can be no doubt that the angels, by the preaching of the gospel and the calling of the Gentiles, receive fresh information. Nay, the redemption of mankind is a kind of new world, which God has produced, and which fills the angels with astonishment. Every day they make progress in the knowledge of this wisdom, and yet it is always new and always wonderful to them.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>St. Paul passes on to consider the manifestation of God in Christ as brought home not only to the race of man but to the angels — who are described (1 Peter 1:12) as "desiring to look into" the consummation of the gospel mystery. In the same sense the apostles, in their ministration of the gospel, are said to be a spectacle to angels and to men (1 Corinthians 4:9).</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>It was not enough to evince God's wisdom by the formation of the sun, the stars, the earth, the seas, the mountains, the floods. It was not enough to show it by the creation of intelligent beings. One grand purpose in the creation of the universe was that the wisdom of God might be clearly shown by the church.</p>"
                }
            ],
            "consensus": "mixed",
            "key_tension": "Calvin and Ellicott identify the "principalities and powers" as good angels who learn progressively through redemptive history; Clarke notes that the same phrase in 6:12 refers to hostile powers, leaving open whether the beings here are holy or otherwise."
        },
        "11": {
            "synthesis": "<p>The eternal purpose grounds the entire chapter's argument: the Gentile mission is not an improvisation but the fulfillment of a design formed before the ages, executed in Christ Jesus. Calvin notes that Paul has now reinforced this point three times in the chapter — a pastoral strategy against the objection that God's purpose has changed. The decree is eternal and unchangeable; its execution is "in Christ Jesus," because in him it was made. Ellicott explains that "purpose of the ages" means a design conceived before all history, not merely a very ancient plan.</p><p>Clarke introduces a nuanced reading of the Greek αἰώνων: he takes it to refer to the complete scope of the Jewish and gospel dispensations, the full round of God's ordered periods, rather than simply "eternity" in an abstract sense. Barnes defends the plain meaning against interpreters who tried to soften it into a mere "arrangement of the ages": the text speaks of sovereign divine purpose. Robertson adds with characteristic brevity: "God's purpose runs on through the ages."</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>How carefully does he guard against the objection that the purpose of God has been changed! A third time he repeats that the decree was eternal and unchangeable, but must be carried into effect by Christ, because in him it was made. The proper time for publishing this decree belongs to the kingdom of Christ.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The eternal purpose — properly, <em>the purpose of the ages</em>: a design conceived before the ages of his dispensation, and fulfilled through them. Hence the rendering of our version is substantially correct. What was "purposed" before time is now being "worked out" through Christ Jesus.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>The object of those interpretations which render this "the arrangement of the ages" seems to be to avoid the doctrine that God had a purpose or plan in the salvation of men; but the text plainly speaks of a sovereign purpose of God, purposed in Christ Jesus our Lord.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>According to the purpose of the ages (κατὰ πρόθεσιν τῶν αἰώνων). God's purpose runs on through the ages. "Through the ages one eternal purpose runs."</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "12": {
            "synthesis": "<p>The practical fruit of the eternal purpose is direct, confident access to God. The verse returns to the theme of 2:18 but here emphasizes two terms: "boldness" (παρρησία) and "confidence" (πεποίθησις) — together painting a picture of a believer who approaches God not with cringing uncertainty but with the open speech of a trusted child. Wesley's image is memorable: access like a petitioner "introduced to the royal presence by some distinguished favourite," with "unrestrained liberty of speech, such as children use in addressing an indulgent father."</p><p>Calvin grounds the boldness in the work of reconciliation: "the honor of reconciling the Father to the whole world must be given to Christ." Clarke notes the exclusivity implied by the syntax: "it is only in his name we can pray to God, and it is only by him that we can come to God." Ellicott sees in this verse Paul's habitual movement from cosmic sweep (vv. 10–11) back to the personal and practical. All voices agree: through Christ, and only through Christ, the boldness of prayer is warranted.</p>",
            "voices": [
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>By whom we have free access — Such as those petitioners have, who are introduced to the royal presence by some distinguished favourite. And boldness — Unrestrained liberty of speech, such as children use in addressing an indulgent father, when, without fear of offending, they disclose all their wants, and make known all their requests.</p>"
                },
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>The honor of reconciling the Father to the whole world must be given to Christ. From the effects of this grace its excellence is demonstrated; for the access which is possessed by Gentiles in common with Jews admits them into the presence of God. Most important and valuable instruction is here conveyed, that the only door by which we enter into the presence of God is Christ.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>The word παρρησίαν means, properly, boldness of speaking. Here it seems to mean "freedom of utterance"; and the idea is that we may come to God now in prayer with confidence through the Lord Jesus. See Hebrews 4:16.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "13": {
            "synthesis": "<p>The parenthesis of verse 13 turns Paul's sufferings into a source of encouragement for the Ephesians rather than a scandal. Calvin's comment is memorable: "O heroic breast, which drew from a prison, and from death itself, comfort to those who were not in danger!" The verb ἐκκακεῖν (to faint, or to play the coward) is noted by Robertson as meaning literally "to give in to evil" — a strong word for the temptation to abandon faithfulness under pressure of someone else's suffering.</p><p>Ellicott describes the verse as parenthetical, inserted as a warning against discouragement: Paul's chains are not a sign that the mission has failed but that it is advancing at the cost of the missionary. Clarke situates it in the pastoral context of early Christian persecution: believers who were not yet deeply rooted could be easily shaken by the sight of their apostle in captivity. Barnes confirms: Paul recognizes the natural tendency to be distressed, and addresses it by reframing his tribulations as their glory. Wesley's note is the most compressed: "The not fainting is your glory."</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>O heroic breast, which drew from a prison, and from death itself, comfort to those who were not in danger! He says that he endured tribulations for the Ephesians, because they tended to promote the edification of all the godly. How powerful and godlike is this magnanimity, which enables a man in his own prison to tranquilize others!</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The verse is parenthetical — a reflection suggested by the greatness of the trust and the littleness of the minister, inserted as a warning to the Ephesians not to be disheartened at the present tribulation of his imprisonment, as if it were a failure of his mission.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>The infinitive ἐνκακεῖν is a late and rare word and means to behave badly in, to give in to evil (ἐν, κακός). Paul urges all his apostolic authority to keep the readers from giving in to evil because of his tribulations for them.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>The not fainting is your glory.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "14": {
            "synthesis": "<p>The sentence Paul began in verse 1 — interrupted by the great parenthesis on the mystery — is here resumed and completed in the act of prayer. Calvin draws the pastoral lesson: if Paul, with all his apostolic authority, still prays for those he has taught, how much more must pastors pray for their people, since "nothing will be gained by their industry and toil" without divine blessing. Robertson confirms that kneeling was one of two common postures in New Testament prayer (the other being standing), citing Luke 22:41, Acts 7:60, Acts 20:36.</p><p>Barnes links the resumption to verse 1, seeing this as completing the interrupted thought. Ellicott raises a textual question: the words "of our Lord Jesus Christ" following "the Father" appear to be absent from several ancient manuscripts, and if so, Paul is praying to the Father understood in the universal sense he will develop in verse 15. Clarke observes that kneeling marked genuine humility and contrasts it with casual or presumptuous approaches to God. The great prayer of vv. 14–19, all voices agree, is among the richest intercessory passages in the New Testament.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>His prayers for them are mentioned, not only to testify his regard for them, but likewise to excite them to pray in the same manner. Let pastors learn from Paul's example, not only to admonish and exhort their people, but to entreat the Lord to bless their labors, that they may not be unfruitful. Nothing will be gained by their industry and toil without the Lord's blessing.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The words "of our Lord Jesus Christ" appear, by both external and internal evidence, to be an interpolation — probably from a gloss indicating that the universal fatherhood here spoken of is derived from the fatherly relation to him in whom "all things are gathered up."</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>He now prays whether he had at first intended to do so at 3:1 or not. This was a common attitude in prayer (Lu 22:41; Ac 7:60; 20:36; 21:5), though standing is also frequent (Mr 11:25; Lu 18:11, 13).</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>Some suppose that this is a resumption of what he had commenced saying in Ephesians 3:1, but which had been interrupted by a long parenthesis. "Wherefore, that the great work may be carried on and that the purposes of these my sufferings may be answered in your benefit and glory, I bow my knees to God, and pray to him."</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "15": {
            "synthesis": "<p>"Of whom the whole family in heaven and earth is named" introduces a wordplay between πατήρ (Father) and πατριά (family/descent-group). Ellicott presses the etymology toward a grand sense: every "fatherhood" in the universe derives its name and reality from the Fatherhood of God — all lower fatherhood is a shadow and derivative. Clarke reads the family as undivided: angels in heaven, saints departed, and believers on earth form one household under one Father, not three separate families. Wesley agrees: "the whole family of angels in heaven, saints in paradise, and believers on earth."</p><p>Barnes and Robertson note a genuine exegetical division over the antecedent of "of whom": does the family take its name from the Father, or from Christ? Barnes cites Calvin, Locke, and Doddridge for the Christ-referent; Bloomfield, Chandler, Erasmus, and Clarke for the Father. Robertson opts for the Father — every family in heaven and earth derives its familial identity from God the Father of all — and this reading fits the trinitarian structure of the prayer, which began with the Father as its explicit address.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The original word (<em>patria</em>) here rendered "family" is literally derived from the word "father" (<em>pater</em>). It has been proposed to render it <em>fatherhood</em>, and translate: from whom all fatherhood whatever derives its name — all lower fatherhood being, in fact, a shadow and derivative from the Fatherhood of God.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>Believers in the Lord Jesus Christ on earth, the spirits of just men made perfect in a separate state, and all the holy angels in heaven, make but one family, of which God is the Father and Head. St. Paul does not say, <em>of whom the families</em>, as if each order formed a distinct household; but he says <em>family</em>, because they are all one, and of one.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>Commentators have been divided in opinion about whether "of whom" refers to the Father or to the Lord Jesus. Bloomfield, Chandler, Erasmus, and some others refer it to the Father. Locke, Doddridge, Calvin, and some others refer it to the Lord Jesus. This is the more natural interpretation — all God's children bear the same name, derived from the Redeemer.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>Of whom — the Father. The whole family of angels in heaven, saints in paradise, and believers on earth is named — being the "children of God," a more honourable title than "children of Abraham," and depending on him as the Father of the family.</p>"
                }
            ],
            "consensus": "mixed",
            "key_tension": "Whether "of whom the whole family is named" refers to the Father (Clarke, Wesley, Robertson) or to Christ (Calvin, Locke, Doddridge, Barnes), and whether πατριά should be rendered "family" or "fatherhood.""
        },
        "16": {
            "synthesis": "<p>The first petition of the great prayer is for inner strengthening by the Spirit: that believers should be "strengthened with might in the inner man." Calvin notes that even those who have genuine faith still need deeper rooting; the highest perfection in this life is an earnest desire to make further progress, and such progress is entirely the work of the Holy Spirit. Ellicott traces the trinitarian movement of the prayer: the Father is the source, the Spirit is the giver of life to the soul, and (in v17) Christ is the one who dwells in the heart through faith.</p><p>The measure of the gift is "the riches of his glory" — not human deserving but divine abundance. Clarke calls the whole prayer "one of the most grand and sublime in the whole oracles of God," finding every word laden with significance. Barnes glosses "riches of glory" as inexhaustible stores of grace: "Out of those stores of rich grace which can never be exhausted." Robertson notes that the prayer's five petitions (two infinitives after ἵνα δῷ, two after ἵνα ἐξισχύσητε, and a final ἵνα πληρωθήτε) are architecturally layered.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>Paul wishes that the Ephesians should be strengthened, and yet he had already bestowed on their piety no mean commendation. But believers have never advanced so far as not to need further growth. The highest perfection of the godly in this life is an earnest desire to make progress. This he tells us is the work of the Spirit, so that it does not proceed from man's own ability.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>From the Father, as the source of all life and being, St. Paul passes on to the Spirit as the giver of life to men. His prayer here, as in Ephesians 1:17, is for the gift of the Spirit, but under a different aspect. There the prayer is for illumination; here for strength to grasp the mystery, to be rooted in love, and be filled up to the fulness of God.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>According to the riches of his glory — according to the glorious abundance of his mercy. The word <em>riches</em>, so often used by Paul, denotes abundance; and the idea here is that his grace was inexhaustible and ample for all their wants. Out of those stores of rich grace which can never be exhausted.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>This prayer of the apostle is one of the most grand and sublime in the whole oracles of God. The riches of the grace of the Gospel, and the extent to which the soul of man may be saved here below, are most emphatically pointed out here. Every word seems to have come immediately from heaven; labouring to convey ideas of infinite importance to mankind.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "17": {
            "synthesis": "<p>The second petition of the prayer is that Christ may "dwell" (κατοικεῖν — to be permanently at home, not a transient guest) in the believers' hearts through faith. Calvin insists on the inseparability of Spirit and Christ: one cannot obtain Christ without the Spirit, and one cannot receive the Spirit without Christ. Ellicott agrees and draws on John 14:16–20 to show that the office of the Spirit is to implant and work out in believers the likeness of Christ — what looks like two petitions in vv. 16–17 is actually one gift under two descriptions.</p><p>Clarke develops the temple metaphor, noting that as Solomon prayed at the dedication of the Jerusalem temple that God would fill it with his presence (2 Chr. 6), Paul prays that the living God would fill the Ephesian community. Barnes distinguishes the botanical from the architectural image in the phrase that follows — "rooted" pictures a tree's deep roots, while "grounded" (τεθεμελιωμένοι) pictures the laid foundation of a building. Wesley keeps it spare: dwelling means "constantly and sensibly abide."</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He explains what is meant by "the strength of the inner man." It is a mistake to imagine that the Spirit can be obtained without obtaining Christ; and it is equally foolish and absurd to dream that we can receive Christ without the Spirit. We are partakers of the Holy Spirit in proportion to the intercourse which we maintain with Christ.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The indwelling of Christ (as the construction of the original plainly shows) is not a consequence of the gift of the Spirit; it is identical with it, for the office of the Holy Spirit is to implant and work out in us the likeness of Christ. So in John 14:16–20, in immediate connection with the promise of the Paraclete, our Lord says, "I will come to you."</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>Κατοικέω is an old verb to make one's home, to be at home. Christ is asked to make his home in our hearts. This is the ideal, but a deal of fixing would have to be done in our hearts to make them a fit dwelling for Christ.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>That ye being <em>rooted</em> — firmly established, as a tree whose roots strike deep and extend afar. The meaning is that his love should be as firm in our hearts as a tree in the soil whose roots strike deep. And <em>grounded</em> (τεθεμελιωμένοι) — as firmly laid as the foundation of a building.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "18": {
            "synthesis": "<p>The third petition is that believers, together with all the saints, may have full strength to seize the dimensions of the love of Christ. Clarke presses the Greek verbs: ἐξισχύσητε means to be thoroughly able (a compound of intensity upon strength), while καταλαβέσθαι means to fully catch or seize — not passive reception but active, straining apprehension. Robertson confirms both: the first is found only here in the New Testament, the second means to lay hold of effectively.</p><p>The four spatial dimensions — breadth, length, depth, height — have generated much interpretation. The early fathers referred them to the cross, as Ellicott notes approvingly. Calvin argues they simply present the love of Christ from every angle, so that in whatever direction one looks, the love is found to be limitless. Wesley maps each dimension onto an aspect of that love: breadth embraces all mankind, length spans eternity, depth is beyond creature-fathoming, height is beyond all enemy reach. Barnes reads the breadth and length as describing the universal scope of redemption, including Gentile and Jew alike. The diversity of these readings itself illustrates the inexhaustibility of the love they attempt to describe.</p>",
            "voices": [
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>The first word, ἐξισχύσητε, from ἐξ, intensive, and ἰσχύω, to be strong, signifies that they might be <em>thoroughly able</em>, by having been strengthened with might by God's power. The second word, καταλαβέσθαι, from κατα, intensive, and λαμβάνω, to take, catch, or seize, may be translated <em>that ye may fully catch or apprehend</em>.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>St. Paul has of set purpose omitted all definition, leaving the phrase incomplete in absolute generality. The early fathers delighted to refer it to the cross, and to trace in the four dimensions of the cross a symbol of this fourfold extension of the love of God in Christ.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>That being rooted and grounded — that is, deeply fixed and firmly established, in love, ye may comprehend — so far as a human mind is capable — what is the breadth of the love of Christ, embracing all mankind; and length, from everlasting to everlasting; and depth, not to be fathomed by any creature; and height, not to be reached by any enemy.</p>"
                },
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>By those dimensions Paul means nothing else than the love of Christ, of which he speaks afterwards. The meaning is that he who knows it fully and perfectly is in every respect a wise man. As if he had said, "In whatever direction men may look, they will find nothing in the doctrine of salvation that does not bear some relation to this subject."</p>"
                }
            ],
            "consensus": "mixed",
            "key_tension": "The four dimensions (breadth, length, depth, height) are referred by the early fathers to the cross, by Calvin to the love of Christ viewed from every angle, by Wesley to distinct attributes of that love, and by Barnes to the universal scope of redemption — the text deliberately withholds specification."
        },
        "19": {
            "synthesis": "<p>The fourth petition presents an intentional paradox: to know the love of Christ which surpasses knowledge. All voices recognize the paradox but interpret it differently. Wesley reads the sentence as a self-correction: "the apostle corrects himself, and immediately observes, it cannot be fully known. This only we know, that the love of Christ surpasses all knowledge." Ellicott resists resolving the paradox by distinguishing head-knowledge from faith-knowledge, arguing that no such opposition is indicated in the text — the paradox is real and is meant to stand.</p><p>Calvin argues that the four dimensions of verse 18 are simply the same love described here — to comprehend it from every angle is to discover it infinite: "the love of Christ contains within itself the whole of wisdom." Barnes fixes the object concretely: this is not a generic love but "the immensity of redeeming love" shown in dying for a lost world. The ultimate purpose is filling: "that ye may be filled with all the fulness of God" — a phrase so vast that Robertson confesses he "hesitates to comment on this sublime prayer."</p>",
            "voices": [
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>And to know — But the apostle corrects himself, and immediately observes, it cannot be fully known. This only we know, that the love of Christ surpasses all knowledge. That ye may be filled — which is the sum of all — with all the fulness of God — with all his light, love, wisdom, holiness, power, and glory. A perfection far beyond a bare freedom from sin.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The intentional paradox of this expression is weakened if we suppose that there is opposition in kind between the knowledge referred to in the two clauses, as if "to know" meant to know by faith while the "knowledge" which the love of Christ "passes" is mere human head-knowledge. Of such opposition there is no trace in the original. The paradox is real and intentional.</p>"
                },
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>By those dimensions Paul means nothing else than the love of Christ, of which he now speaks openly. The love of Christ contains within itself the whole of wisdom. He who knows it fully and perfectly is in every respect a wise man; for in it all the treasures of wisdom and knowledge are laid up.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>The love of Christ towards us; the immensity of redeeming love. It is not merely the love which he showed for the Gentiles in calling them into his kingdom; it is the love which is shown for the lost world in giving himself to die. To feel this; to have a lively sense of it — is the highest attainment of the Christian life.</p>"
                }
            ],
            "consensus": "mixed",
            "key_tension": "Wesley reads the prayer as a self-correcting concession that full knowledge of Christ's love is impossible; Calvin and Ellicott read the paradox as intentional and irreducible, not a rhetorical mistake but the point itself."
        },
        "20": {
            "synthesis": "<p>The doxology opens with a crescendo of adverbs: God is able to do "exceeding abundantly above all" (ὑπερεκπερισσοῦ) — a double compound that Robertson calls "late and rare," as Paul piles word upon word to strain ordinary language toward the infinite. Wesley traces a "most beautiful gradation": God gives exceeding abundant blessings; we may ask for more; he can do more than we ask; and more than we can even think. The measure is not the scope of human petition but the power already at work within believers — the same Spirit-strengthening prayed for in verse 16.</p><p>Calvin draws out the pastoral function: the doxology is designed to prevent the reader from viewing the prayer's requests as impossible or the praying as presumptuous. Clarke stresses the omnipotence: God is able to do ὕπερ ἐκ περισσοῦ, "superabundantly above the greatest abundance." Barnes notes that such doxological outbursts are characteristic of Paul (Romans 9:5; 11:36; Galatians 1:5), arising when his mind is so full of the subject that words pour out in praise rather than argument.</p>",
            "voices": [
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>This doxology is admirably adapted to strengthen our faith, that we may not stagger at the great things the apostle has been praying for, as if they were too much for God to give, or for us to expect from him. When he has given us exceeding, yea, abundant blessings, still we may ask for more. He is able to do it. Yea, and above all we ask — above all we can think.</p>"
                },
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He now breaks out into thanksgiving, which serves the additional purpose of exhorting the Ephesians to maintain good hope through grace and to endeavor constantly to obtain more and more adequate conceptions of the value of the grace of God. The doxology is designed to prevent the reader from viewing the prayer's requests as impossible or the praying as presumptuous.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>Paul is fully aware of the greatness of the blessings asked for, but the Doxology ascribes to God the power to do them for us. Ὁπερεκπερισσοῦ — a late and rare double compound (ὕπερ, ἐκ, περισσοῦ). It suits well Paul's effort to pile Pelion on Ossa.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>It is not uncommon for Paul to utter an ascription of praise in the midst of an argument. Here his mind is full of the subject; and in view of the fact that God communicates to his people such blessings, that they may become filled with all his fullness, he desires that praise should be given to him.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "21": {
            "synthesis": "<p>The doxology concludes with glory ascribed to God "in the church and in Christ Jesus throughout all generations, to the age of the ages." Ellicott draws out the profound unity implied by the parallelism: what is "in the church" is "in Christ Jesus," because the church's visible unity represents and depends upon its invisible unity with God in him. Clarke envisions the assembled people of God across all time and place: "in all the assemblies of the people of God, wherever these glad tidings are preached."</p><p>Barnes identifies the church as both the instrument and the sphere of God's glory: it is through the church that the manifold wisdom of God is displayed to heavenly principalities (v. 10), and through the church that his praise is eternally celebrated. The amplified formula "throughout all generations, world without end" (εἰς πάσας τὰς γενεὰς τοῦ αἰῶνος τῶν αἰώνων) signals, as Barnes notes, that Paul's heart is overflowing and ordinary language cannot contain the scope of the eternity he envisions. Robertson adds simply: the church as the body of Christ, and Christ as the Head of the glorious church.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>In the parallelism of these clauses is implied the great idea of the Epistle — the unity of the Church in Christ. Hence all that is "in the Church" is "in Christ Jesus." The visible unity of the Church represents, as it depends on, the invisible unity with God in him. The doxology rises to "all the generations of the age of the ages" — each successive generation worshipping within the one eternal age.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>Be unceasing praises ascribed in all the assemblies of the people of God, wherever these glad tidings are preached, and wherever this glorious doctrine shall be credited. By Christ Jesus — through whom, and for whom, all these miracles of mercy and power are wrought. Through all succeeding generations — while the race of human beings continues to exist on the face of the earth.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>The church was to be the instrument by which the glory of God would be shown; and it was by the church that his praise would be celebrated. There is a richness and amplification of language here which shows that his heart was full of the subject, and that it was difficult to find words to express his conceptions. It means, in the strongest sense, <em>for ever</em>.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>In the church (ἐν τῇ ἐκκλησίᾳ) — the general church, the body of Christ. And in Christ Jesus (καὶ ἐν Χριστῷ Ἰησοῦ) — the Head of the glorious church.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        }
    }
}

def main():
    existing = load_synthesis('ephesians')
    merge_synthesis(existing, EPHESIANS)
    save_synthesis('ephesians', existing)
    print('Ephesians 3 synthesis complete.')

if __name__ == '__main__':
    main()
