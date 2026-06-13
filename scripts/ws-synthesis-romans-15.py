"""
Wide Source Synthesis — Romans chapter 15
bookId: romans
Run: python3 scripts/ws-synthesis-romans-15.py

Sources used: calvin, ellicott, clarke, wesley, barnes, rwp
Not used: mhcc (not found for Romans), jfb (data error — contains Acts 15, not Romans 15)
Chapter range: 15  (33 verses)

Key synthesis decisions:
- v6: Calvin is absent; entry draws on ellicott, clarke, barnes, rwp
- v10: Calvin disputes the Dt 32:43 reading and prefers Ps 47:5; others follow LXX Dt 32:43
  → consensus "mixed", key_tension set
- v16: Rich priestly metaphor (λειτουργόν / ἱερουργοῦντα) — Calvin and Clarke embrace the
  sacrificial imagery to describe Paul's apostolic work; Barnes and RWP explicitly deny any
  sacerdotal implication → consensus "mixed", key_tension set
- v23: Calvin entry is absent; entry draws from ellicott, clarke, wesley, barnes, rwp
- v26: Calvin and Clarke absent; entry draws from ellicott, wesley, barnes, rwp
- v32-33: Calvin and Wesley absent; entries draw from ellicott, clarke, barnes, rwp
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

ROMANS = json.loads(r'''
{
    "15": {
        "1": {
            "synthesis": "<p>Paul opens chapter 15 by identifying himself with the strong—those whose mature faith is not troubled by the dietary scruples that divided the Roman congregation—and at once deflects the privilege of strength into obligation. Calvin observes that God bestows strength for this very purpose: to sustain the weak, not to enjoy one's own advantage. The strong are stewards, not proprietors, of their spiritual robustness. Ellicott notes the unbroken continuity with the close of chapter 14, insisting that the exhortation extends beyond meat and drink to every arena of community life. Barnes anchors the call in the apostle's counting himself among the strong, underscoring that exemption from scruples brings heightened responsibility rather than license. RWP distinguishes Paul's emphasis on moral strength from the merely powerful or socially mighty—it is moral and spiritual strength that creates moral and spiritual debt.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>God has destined those to whom he has granted superior knowledge to convey instruction to the ignorant; so to those whom he makes strong he commits the duty of supporting the weak by their strength. Thus ought all gifts to be so employed as to be profitable to brethren, and not to be kept shut up in oneself.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The opening verses of the chapter are intimately connected with the close of the last. Not only ought those who are strong in faith to be careful what they do in the matter of meat and drink, but in all things they should show sympathy and consideration for their weaker brethren.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>The apostle resumes the subject of the preceding chapter, and continues the exhortation to those who had been converted from paganism, and who were strong in the faith. He identifies himself with the strong, and exhorts them to bear with and support the weak.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>Paul identifies himself with this wing in the controversy. He means the morally strong, not the mighty. The weaknesses are the scruples of the not-strong. To bear, as in Gal 6:2, is common in the figurative sense of carrying another's burden as one's own.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": null
        },
        "2": {
            "synthesis": "<p>The positive corollary of verse 1: because the strong must not please themselves, each must actively seek what builds up the neighbor. Calvin stresses that the obligation to accommodate runs without exception whenever it can be done consistently with God's word and genuine edification—not every demand of a weak conscience, but every real spiritual good of the neighbor. Clarke adds the pastoral wisdom that those who have grown in faith should remember how much others bore with them before they reached their current understanding, a check against the self-congratulation that strength can breed. Barnes distinguishes neighbor-pleasing from flattery or indulgence: the goal is the neighbor's benefit, not their approval.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He teaches us that we are under obligations to others, and that it is our duty to please and to serve them; that there is no exception in which we ought not to accommodate ourselves to our brethren when we can do so, according to God's word, to their edification.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>Though we should not indulge men in mere whims and caprices, yet we should bear with their ignorance and their weakness, knowing that others had much to bear with from us before we came to our present advanced state of religious knowledge.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>Not to seek to secure for the neighbor indulgence in those things which would be injurious, but in all things which his welfare would be promoted. The word neighbour here has especial reference to the members of the church.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>For the good—not to please men just for popular favours, but for their benefit and spiritual growth.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": null
        },
        "3": {
            "synthesis": "<p>The supreme ground of the obligation in verse 2: Christ himself pleased not himself. Paul cites Psalm 69:9, one of the Messianic psalms of suffering, to show that the reproaches aimed at God fell upon Christ—he absorbed into himself the consequences of others' enmity against the Father. Barnes carefully corrects any misreading of this as coercion: Christ volunteered. His not-pleasing-himself was a free, deliberate choice of another's welfare over his own ease. RWP identifies this as the supreme example for Christians. Calvin presses the logic of discipleship: if the Lord himself took this posture, no servant can claim exemption from bearing the infirmities of others. Wesley simply notes Christ bore not only infirmities but reproaches—the cost ran higher than inconvenience.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>Since it is not right that a servant should refuse what his lord has himself undertaken, it would be very strange in us to wish an exemption from bearing the infirmities of others, to which Christ submitted himself. In him was really verified what the Prophet declares—the reproaches of those who reproached God fell upon him.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>This is not to be understood as if the Lord Jesus did not voluntarily and cheerfully engage in his great work. He was not compelled to come and suffer. The idea is that he did not consult his own ease, his own comfort, his own wishes, but regarded the welfare of others.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Paul quotes after the LXX version of Psalm 69:9, one of those Psalms of suffering which, like Isaiah 53, afford a type of the sufferings of the Messiah. The insults directed against God Himself fell upon His servants.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>The supreme example for Christians. Paul quotes Psalm 69:9 (a Messianic Psalm) and represents the Messiah as bearing the reproaches of others—the cost absorbed by Christ that his people might go free.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": null
        },
        "4": {
            "synthesis": "<p>The quotation from Psalm 69 prompts Paul to a broader principle: everything written in the Old Testament was written for our learning. Calvin frames this as a defense of the typological use of scripture: it is not arbitrary to apply the Psalmist's words to Christ, because the whole of scripture was designed for the instruction of every generation, not just the original audience. Barnes observes that this reads like a parenthesis—the thought seems to have seized Paul spontaneously from the particular case he had just cited. Ellicott illuminates the purpose clause: the patient endurance and consolation scripture supplies all converge on <em>hope</em>—specifically the Messianic hope of future glory. Wesley catches a useful inversion: it is the consolation of scripture that <em>produces</em> patience, not patience that produces consolation.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>God had not intended the scriptures merely for those generations in which they were first delivered, but for the instruction of all succeeding generations of mankind. There is nothing in scripture which is not useful for our instruction and the direction of our life.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The promises and consolations of Scripture support the Christian under his trials, and enable him to endure them not only patiently but cheerfully. The Messianic hope centres in the promises of Scripture; it is through these that hope is sustained.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>This is a general observation which struck the mind of the apostle from the particular case he had just specified. He turned aside from his direct argument to express this sentiment: all the Old Testament is admirably adapted to express Christian duties and doctrine.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>Aforetime—In the Old Testament. That we, through the consolation which God gives us by these, may have patience and a joyful hope. It is the consolation of the scriptures that produces patience.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": null
        },
        "5": {
            "synthesis": "<p>Having finished the exhortation, Paul turns to prayer—the natural completion of all Christian instruction, since what God commands he must also supply. Calvin notes the significance of this movement: the Lord does not proportion his precepts to our natural strength; he commands what requires grace, thereby driving us to prayer. Barnes dwells on the analogy between God's own patience with his children and the patience Christians owe each other: the title God of patience is itself an argument for mutual forbearance. Ellicott identifies a subtle theological link—singleness of purpose, the concentrated self-dedication that enables suffering to be borne, is the same disposition that produces unity among believers. RWP notes the optative form (the grant-wish) as a prayer—Paul prays for what he has commanded, turning command into petition.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>God alone is the author of patience and of consolation; for he conveys both to our hearts by his Spirit, yet he employs his word as the instrument. After having exhorted and admonished the Romans, he turns to pray for them—for he fully knows that all exhortations are of no avail unless God works in the heart.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>He who is wholly self-dedicated to Christ, and in the strength of that self-dedication is able to endure persecution with patience, will naturally be drawn into harmony with all other believers who share the same self-dedication. Singleness of purpose is thus the link between patience and unity.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>The God who is himself long-suffering, who bears patiently with the errors and faults of his children, and who can give patience—if God bears long and patiently with our infirmities, we ought to bear with each other. This example is a strong argument for mutual forbearance.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>The God of patience and comfort—genitive case of the two words in verse 4, describing God who uses the Scriptures to reveal himself. Grant you—second aorist active optative as a prayer-wish for the future: may he grant.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": null
        },
        "6": {
            "synthesis": "<p>The intended outcome of the prayer in verse 5: that Jews and Gentiles together—with one mind and one mouth—might glorify the Father of our Lord Jesus Christ. Clarke draws out the public-worship dimension that is often overlooked: divisions between Jewish and Gentile believers would disrupt the very act of corporate praise, so unity is not an abstract virtue but a practical prerequisite for common liturgical life. Ellicott observes that it is in the heart that the spirit of harmony arises, and with the mouth that it is expressed—the outward oneness of voice must flow from an inward oneness of aim. Barnes presses the point further: strife and contention make even physically assembled worship a divided service, unheard by God. RWP notes that homothumadon, with one accord, appears eleven times in Acts but only here in Paul—a word Paul reaches for at the peak of his appeal for unity.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>It is in the heart that the spirit of humanity arises, and with the mouth that it is expressed. The inward oneness of aim must precede the outward oneness of voice before both Jews and Gentiles can glorify God together.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>Jews and Gentiles—thinking the same things and bearing with each other—might with one mouth glorify God in their religious assemblies, without jarring or contentions. The apostle refers to religious acts in public worship, which might have been greatly interrupted by the dissensions between the converts.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>Divisions, strife, and contention in the church prevent union in worship. Though the body may be there and the church professedly engaged in public worship, it is a divided service; and the prayers of strife and contention are not heard.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>With one accord (homothumadon)—here alone in Paul, but eleven times in Acts. With one mouth—vivid outward expression of the unity of feeling. May glorify—present active subjunctive: that ye may keep on glorifying.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": null
        },
        "7": {
            "synthesis": "<p>Paul gathers the entire argument of chapters 14-15 into a single imperative: receive one another, exactly as Christ received you. Calvin stresses that Christ's receiving of both weak and strong has <em>bound</em> them together—to separate from those the Lord has joined is to separate from Christ himself. Ellicott notes this is the same verb (proslambano) as the opening of chapter 14, deliberately recalling the starting point of the discussion to signal its close. The ground now given is the comprehensiveness of Christ's love: he did not receive a subset but the whole. Clarke adds the depth of the imagery—Christ received them as partakers of inestimable blessings, condescending to be present among them. Barnes states the practical application plainly: acknowledge one another as Christians and treat one another as such, even when you differ on lesser matters.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>Christ, having received not one or two of us, but all together, has thus connected us, so that we ought to cherish one another if we would indeed continue in his bosom. Only thus shall we confirm our calling—if we separate not ourselves from those whom the Lord has bound together.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The word received is the same as that at the beginning of Romans 14, the subject of which chapter is still continued, and is now taken up for the last time. The duty of Christians to show cordiality to each other is now based upon the comprehensiveness of the love of Christ.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>Receive ye one another—have the most affectionate regard for each other, and acknowledge each other as the servants and children of God Almighty. As Christ has received us into communion with himself and made us partakers of such inestimable blessings, so should we, Jews and Gentiles, receive each other.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>In view of all the considerations tending to produce unity and love which have been presented, receive ye one another: acknowledge one another as Christians and treat one another as such, though you may differ in opinion about many smaller matters.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": null
        },
        "8": {
            "synthesis": "<p>To ground the mutual reception of verse 7, Paul specifies the dual scope of Christ's mission. Ellicott offers the clearest formulation: Christ came with a twofold purpose—to confirm God's faithfulness to Israel by fulfilling the covenant promises, and to extend God's mercy to the Gentiles who stood outside that covenant. Calvin adds that the order of priority (Jews first, then Gentiles) does not imply a permanent hierarchy; it was a matter of historical sequence in salvation's unfolding. Clarke explains why this matters for Gentile-to-Jewish charity: the Gentiles should bear with scrupulous Jewish believers precisely because they owe them so much—Christ himself came first as minister of the circumcision on their behalf. Barnes notes that rendering Christ as Messiah throughout would make the apostle's reasoning strike with more immediate force for a Jewish reader.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Christ came with a two-fold purpose: on the one hand, with a mission to the Jews to vindicate to them the truthfulness of God by confirming and fulfilling the covenant promises; and, on the other hand, to exhibit the mercy of God in rescuing the Gentiles from their state of condemnation.</p>"
                },
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>Christ has embraced us all, so that he leaves no difference between Jews and Gentiles, except that in the first place he was promised to the Jewish nation before he was revealed to the Gentiles. He had gathered them both from a miserable dispersion and brought them into the Father's kingdom, that they might be one flock.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>To show the Gentiles the propriety of bearing with the scrupulous Jews, Paul shows them here that they were under the greatest obligations to this people, to whom in the days of his flesh Jesus Christ confined his ministry, confirming the truth of God contained in the promises made to the patriarchs.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>The force of the apostle's reasoning would often be more striking if he retained the word Messiah rather than the mere surname Christ. It is the name of his office; and to a Jew the name Messiah would convey much more than a proper name.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": null
        },
        "9": {
            "synthesis": "<p>The second half of Christ's mission—Gentile inclusion—Paul immediately grounds in scripture. He cites Psalm 18:49, where David declares he will praise God among the Gentiles, and interprets it as a forward-looking promise now fulfilled in Christ. Ellicott articulates the theological distinction with precision: the Jews had a covenant to appeal to, and the attribute of God most clearly displayed to them was his <em>veracity</em>—faithfulness to his word. The Gentiles had no such covenant; their admission was an act of pure <em>mercy</em>. Calvin draws the same line: God's truth was at stake for the Jews; God's grace was on display for the Gentiles. Clarke notes the symmetry: Jews glorified God for his truth, Gentiles for his mercy—different grounds, same destination of praise. RWP identifies the future tense (I will sing) as reinforcing the prophetic forward projection.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The Jews had their covenant to appeal to, and the attribute of God most clearly brought home to them in Christianity was His veracity in fulfilling promises. The Gentiles had no such covenant, and their admission to the blessings of Christianity was an act of pure grace and mercy, which they could only thankfully recognise.</p>"
                },
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>Mercy was destined to come to the Gentiles through the covenant God made with Abraham and through Christ. The Jews were to glorify God for his truth; the Gentiles were to glorify him for his mercy—though both had been gathered from a miserable dispersion into one people.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>The Jews received the blessings of the Gospel by right of promise, which promise God had most punctually and circumstantially fulfilled. The Gentiles had received the same Gospel as an effect of God's mere mercy, having no right in consequence of any promise made with their ancestors.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>The benefits of the gospel were not to be confined to the Jews; and as God designed that those benefits should be extended to the Gentiles, so the Jewish converts ought to be willing to admit them and treat them as brethren.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": null
        },
        "10": {
            "synthesis": "<p>Paul adds a second Old Testament witness for the Gentiles' place in God's praise: the call in Deuteronomy 32:43 for the Gentiles to rejoice with Israel. The source text is briefly disputed among the commentators. Calvin objects to the standard attribution and prefers Psalm 47:5, arguing that Moses's song in Deuteronomy was aimed at terrifying Israel's adversaries rather than inviting them to common joy. Ellicott and Barnes follow the LXX reading of Deuteronomy 32:43 without dispute, and Barnes adds that the accumulation of quotations (vv. 9-12) is itself deliberate—Paul will not rest his case on a single passage but builds a chain of witnesses from Law, Psalms, and Prophets. The practical point, wherever the text is sourced, is clear to all: Gentile rejoicing alongside Israel is embedded in the Old Testament itself.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>This verse is commonly considered as if taken from the song of Moses, but with this I cannot agree; for Moses's design there was to terrify the adversaries of Israel by setting forth his greatness, rather than to invite them to a common joy. I think this is quoted from Psalm 47:5, where the Prophet connects the Gentiles with Israel in a common celebration.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>St. Paul here follows the LXX version of Deuteronomy 32:43, which varies somewhat from the original. The sense of the Hebrew is disputed, but the design of the quotation is the same as the others: to show that Gentile inclusion in God's praise belongs to the Old Testament itself.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>The design of the quotation from Deuteronomy 32:43 is to show that the Old Testament calls on the Gentiles to celebrate the praises of God—that they are to be introduced to the same privileges as his people. Paul accumulates quotations to prevent reliance on a single expression.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>Rejoice, ye Gentiles—first aorist passive imperative from euphraino. Paul quotes from Deuteronomy 32:43 in the LXX, calling the Gentile nations to join Israel's joy at God's mighty acts.</p>"
                }
            ],
            "consensus": "mixed",
            "key_tension": "Calvin disputes that this quotation comes from Deuteronomy 32:43, preferring Psalm 47:5 on the grounds that Moses was there terrifying Israel's enemies rather than inviting them; Ellicott and Barnes accept the LXX Deuteronomy reading without question."
        },
        "11": {
            "synthesis": "<p>The third quotation in Paul's catena comes from Psalm 117:1—the shortest psalm in the Psalter—which is also the most universal in its scope: a direct summons to <em>all</em> nations, without exception, to praise the Lord. Calvin notes that praise presupposes knowledge; the Gentiles cannot praise what they do not know, so the psalm itself implies they will be brought into the knowledge of God. Barnes points out that Paul accumulates these witnesses precisely so that his argument cannot be dismissed as resting on one ambiguous text: he ranges across Deuteronomy, the historical psalms, and now the Hallelujah psalms to demonstrate that Gentile inclusion is the common language of the entire Old Testament. Ellicott draws attention to the monotheistic force of the passage: a call addressed to all nations presupposes a God who is Lord of the whole earth.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>How can those who know not God's greatness praise him? The call to praise is itself a prophecy of the Gentiles' calling, and this appears still more evident from the reason added in the psalm: they are bidden to give thanks for God's truth and mercy—precisely the grounds Paul has been developing.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>An invitation addressed to the Gentile peoples without restriction, at a time when the monotheistic conception of God as Lord of the whole earth was thoroughly established. The psalm's universality is itself the point of its inclusion here.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>The object in this quotation is the same as before. The apostle accumulates quotations to show that it was the common language of the Old Testament that Gentiles would praise God—a call on all nations, which is the very point in his discussion.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>From Psalm 117:1 with slight variations from the LXX text—the most universally inclusive summons in the Psalter, addressed to all the Gentiles without restriction or mediation.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": null
        },
        "12": {
            "synthesis": "<p>The climactic quotation comes from Isaiah 11:10: the root of Jesse—the Messiah—shall rise to rule the Gentiles, and in him the Gentiles shall hope. Calvin calls this the most illustrious of them all. The prophet spoke it when things were almost past hope, comforting the faithful remnant with the promise of a shoot from what appeared to be the dying trunk of David's line. Calvin presses the Messianic identification: it is clear from the context in Isaiah that this shoot is the Redeemer of the world, and the added prophecy that he would be a sign to the Gentiles seals the argument. Ellicott notes that Paul adheres to the LXX, which diverges more widely from the Hebrew here; the word translated root is better understood as a root-shoot or sprout—the fresh growth that emerges when the original stock appears dead. Wesley adds that the Gentiles' hope in Christ contrasts sharply with their pre-Christian condition of being without hope (Eph 2:12).</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>This prophecy is the most illustrious of them all. The prophet comforted the small remnant of the faithful by declaring there would arise a shoot from the dry and dying trunk of David's family, and that a branch would restore to God's people their pristine glory. This shoot is Christ; he would be raised as a sign to the Gentiles, that they too would share in his kingdom.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>St. Paul adheres to the LXX, which diverges more widely from the Hebrew. The root of Jesse is better rendered the root-shoot of Jesse—the expected descendant of Jesse's line, bringing out its intimate connection with the parent stock while emphasising the fresh growth springing from what seemed dead.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>When a tree dies and falls, the root may retain life and send up a sprout of a similar kind. Though Jesse's line should fall like an aged tree, there should be a descendant who would rise and reign over the Gentiles, and in him they should hope.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>There shall be the root of Jesse—that kings and the Messiah should spring from his house was promised to Jesse before it was to David. In him shall the Gentiles hope—who before had been without hope (Eph 2:12).</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": null
        },
        "13": {
            "synthesis": "<p>The benediction that closes the Gentile-inclusion catena (vv. 9-12) is one of the richest in the New Testament. Paul prays for all joy and peace in believing, that the Roman Christians may abound in hope through the power of the Holy Spirit. Ellicott identifies the three-part cluster of hope, joy, and peace as the Christian's distinctive attitude toward the future: they are not independent virtues but a single complex radiating from certainty about the Messianic promises. Calvin observes that Paul prays for precisely what he has just commanded, reminding the reader that the Lord commands what requires grace—the prayer is the honest acknowledgment that no human effort will produce this unity and hope. Wesley offers a memorable note: the title God of hope was unknown in the pagan world; Rome had a goddess Hope, but her temple had twice been struck by lightning—a sharp contrast to the God who is himself the ground of hope. Barnes anchors the hope in the Holy Spirit's power alone: it is through his constant energizing that Christian hope is sustained.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Hope, joy, and peace form a triad which represents the attitude of the Christian in looking towards the future. Hope may be taken as including the other two, for it is upon the certainty of the Messianic promises that they all depend, just as it is through the constant energising power of the Holy Ghost that they are kept alive.</p>"
                },
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>Paul now concludes the passage with prayer, as before. From this it appears that the Lord does not measure his precepts according to our strength; he commands those things which require the aid of his grace, that he may stimulate us in our attention to prayer.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>The God of hope—a glorious title of God, but till now unknown to the heathens; for their goddess Hope, like their other idols, was nothing. Her temple at Rome was burned by lightning—built again not long after, and again burned to the ground.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>The God who inspires or produces the Christian hope—may he fill you with all joy and peace. That ye may abound in hope through the power of the Holy Spirit: it is by his power alone that the Christian has the hope of eternal life.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": null
        },
        "14": {
            "synthesis": "<p>From verse 14 Paul turns to the personal epilogue of the letter. He opens it with an expression of genuine confidence in the Roman congregation before he has ever visited them—he is persuaded they are full of goodness, filled with all knowledge, and able to admonish one another. RWP notes that the main argument of the epistle (chapters 1-8, then 9-15:13) is now complete; these personal matters begin the wind-down. Calvin interprets the expression as a preemptive pacification: the Roman believers might have felt reproved by so many urgent admonitions, and Paul forestalls that reaction by affirming their competence. Ellicott adds that the explanation is especially necessary because Paul had not founded this church and might appear to overstep by writing with such apostolic force to a congregation not his own. Clarke reads the verse as addressed particularly to the Gentile portion of the church, the group he specially serves as apostle.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>This was said to anticipate an objection, or it may be deemed a concession made to pacify the Romans, lest they thought themselves unjustly reproved by so many urgent admonitions. He makes an excuse for having ventured to assume the character of teacher and exhorter, saying that he acted not because he doubted their wisdom or kindness.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>From this point onwards the apostle gives a personal turn to his letter. The explanation might seem the more necessary as the church was not one of his own founding, and he might seem to be both going out of his way and exceeding his commission in writing to them with such earnestness.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>He had never seen them, but he had full confidence in them. This he had expressed more fully in the first chapter. He now shows them the deep interest he had in their welfare, though he had never seen them, in order to secure their obedience to his injunctions.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>Here begins the Epilogue, the personal matters of importance. The argument of the epistle has been completed both in the main line of chapters 1-8 and the further applications of 9:1-15:13. Full of goodness—a LXX and Pauline word, as in 2 Thessalonians 1:11 and Galatians 5:22.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": null
        },
        "15": {
            "synthesis": "<p>Paul's boldness in writing to Rome, he explains, comes not from presumption but from the grace of his apostolic calling. He has written more boldly in some measure—qualifying the claim carefully—as one putting them in remembrance rather than instructing them for the first time. Calvin draws a fine point: Paul humbles himself in the very act of asserting his authority. By reminding them rather than teaching them, he implies they already know the truth; but by pointing to the grace given to him as apostle to the Gentiles, he insists he was authorized to write. Ellicott reads the phrase in some part (apo merous) as qualifying both the extent and degree of his boldness—not everywhere in the letter, but in specific passages where he wrote with unusual directness. Clarke adds an interesting reading: the phrase may indicate he wrote particularly to one party among them—those who needed the reminder more than others.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>Paul humbles himself, that he might exalt the excellency of his office. By mentioning the favor of God by which he was elevated to the apostleship, he shows that his boldness did not arise from arrogance but from duty—he was constrained by his calling to write even to those able to teach themselves.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Holding this good opinion of you, I nevertheless presumed somewhat upon my position as Apostle of the Gentiles to write with an earnestness I should not otherwise have ventured to show. In some part qualifies the boldness both in extent and degree—referring to specific passages where he was most direct.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>I have made bold to write to you in some sort, perhaps to a party among you who stand more in need of such instructions than the others. I do this because of the office which I have received from God—to be the apostle of the Gentiles—which gave him full right to say, advise, or enjoin anything he judged to be necessary.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>I write—epistolary aorist. The more boldly—old comparative adverb from tolmeros, only here in the NT. In some measure (apo merous), perhaps referring to specific portions where Paul wrote with particular plainness.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": null
        },
        "16": {
            "synthesis": "<p>Paul elaborates on the apostolic grace of verse 15 with a sustained priestly metaphor: he is a minister (leitourgon) of Jesus Christ to the Gentiles, priestly-ministering (hierourgounta) the gospel of God, that the offering up of the Gentiles might be acceptable to God, sanctified by the Holy Spirit. Ellicott notes that leitourgon draws originally on the liturgical service of the Jerusalem Temple, though in Paul it designates the public sacred calling of the apostle. Calvin and Clarke both embrace the sacrificial picture fully: the converted Gentiles are the offering; the Holy Spirit is the consecrating element that makes them acceptable. However, Barnes and RWP resist drawing sacerdotal conclusions—Barnes insists leitourgon is here applied metaphorically to New Testament ministry without implying a priestly class; RWP similarly states that the purely metaphorical use does not show that Paul attached a sacerdotal character to the ministry.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>Paul makes himself a chief priest in the ministration of the gospel, to offer up as a sacrifice the people whom he gained for God. This is the priesthood of the Christian pastor—to sacrifice men, as it were, to God, by bringing them through the gospel into obedience to him.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Both words—minister and ministering—refer originally to the liturgical service of the Temple; the first to all functions of priests and Levites, the second to the specific function of the priests in the offering of sacrifice. Paul is a minister of Jesus Christ whose special priestly duty is to see that the Gentiles are presented as an acceptable offering.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>The word leitourgon is properly appropriated to those who minister in public offices, applied in the NT mainly to the Levitical priesthood who ministered at the altar. It is applied here to Paul as discharging substantially the same offices toward the church—but this does not imply a sacerdotal character to the Christian ministry.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>This word derives from the context the priestly associations which often attach to it in the LXX. But this purely metaphorical use does not show that Paul attached a sacerdotal character to the ministry. The word hierourgounta comes from hieron (temple) and ergon (work)—priestly work in a fully figurative sense.</p>"
                }
            ],
            "consensus": "mixed",
            "key_tension": "Calvin and Clarke embrace the priestly and sacrificial language of this verse as a rich description of apostolic work, with the Gentiles as the offering; Barnes and RWP explicitly resist sacerdotal inferences, insisting the language is purely metaphorical and carries no implication of a priestly class in the New Testament ministry."
        },
        "17": {
            "synthesis": "<p>Paul has grounds for boasting in Christ Jesus concerning the things pertaining to God. Calvin reads this as the apostle's transition from general commendation of his calling to specific testimony of its fruit: it is not enough to be appointed; one must also have acted agreeably to the appointment. The boasting is in Christ Jesus—entirely dependent on and circumscribed by what Christ has done through him. Barnes surveys the range of the word (praise, thanksgiving, joy, as well as boasting) and settles on rejoicing: Paul had great cause to rejoice that God had so highly honored him in appointing him apostle to the Gentiles. Ellicott identifies this verse as the title on which Paul rests his claim: a sacred office given by Christ, in a religious sphere relating to God—not merely his own devising or career ambition.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>After having in general commended his calling, he now adds testimonies by which he proved that he had not only taken upon him the apostolic office conferred by God's appointment but had eminently adorned it. For it is of little purpose to be appointed unless one acts agreeably to the calling and fulfills the office.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>This is really the title on which Paul rests his claim. He can boast of a specially sacred office and ministry, given to him by Christ and not merely of his own devising. The sphere of this office is a religious sphere—it relates to the things pertaining to God.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>I have cause of glorying; I have cause of rejoicing that God has made me a minister to the Gentiles and has given me such success among them. All my glorying is in and through Christ Jesus.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>I have whereof to glory through Jesus Christ—all my glorying is in and through him.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": null
        },
        "18": {
            "synthesis": "<p>Paul draws the boundary of his boast with care: he will not dare to speak of what Christ has not wrought through him. The restraint is as significant as the confidence. Ellicott puts it plainly: all successes in the mission field are ultimately due to Christ; for some he has used Paul, for others different instruments; Paul confines himself strictly to his own proper province. Barnes echoes this as the mark of honest apostolic integrity—he will not exaggerate or claim another's work. The two instruments Christ used through Paul are word and deed, which both Calvin and Clarke read as doctrine and miracle: the Gentiles were made obedient to doctrine because they witnessed the miracles that authenticated it. RWP adds the Greek precision: word and deed in the instrumental case, covering preaching and life.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>All successes in the mission field are due ultimately to Christ; for some he has made use of me, for others of other men. I will confine myself to those in which I have been myself directly concerned. I will not dare to speak of anything beyond what Christ has wrought through me.</p>"
                },
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>These words prove what his object was—even to render his ministry approved by the Romans, that his doctrine might not be without fruit. He proves by evidences that God by the presence of his power had given testimony to his preaching, and in a manner sealed his apostleship.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>By word and deed—these words may refer to the doctrines which he taught and to the miracles which he wrought among them. So they became obedient to the doctrines, on the evidence of the miracles with which they were accompanied.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>I should be afraid to speak if the thing were not as I have stated. I do not arrogate to myself what Christ has done by others. I do not exaggerate my own success or claim what others have accomplished.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": null
        },
        "19": {
            "synthesis": "<p>The evidence Paul adduces for Christ's work through him: signs, wonders, and the power of the Holy Spirit—and the staggering geographical scope, from Jerusalem as far round as Illyricum (modern-day Croatia and Albania), a sweep of over fifteen hundred miles. Calvin observes that the success exceeded all human expectation: who could have gathered so many churches for Christ without being aided by the power of God? RWP notes that all three terms—power, signs, wonders—appear together elsewhere only in Hebrews 2:4, 2 Corinthians 12:12, and 2 Thessalonians 2:9; Paul uses them here to describe the same divine attestation that accompanied the preaching. Barnes leaves open whether the power of the Spirit of God is connected specifically with the miracles or constitutes a distinct category (prophecy, tongues), while noting the likely reference to Acts 19:11-12. Clarke adds geographical detail on Illyricum and emphasizes that Paul had gone not by a straight path but by a circular route through all the intervening regions.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>The success which followed his preaching exceeded all the thoughts of men. Who could have gathered so many churches for Christ without being aided by the power of God? From Jerusalem I have propagated the gospel as far as Illyricum, not by hastening in a straight way, but by going all around and through the intervening countries.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Through the might of signs and wonders—through those extraordinary powers which found their expression in signs and wonders. The two words denote the same acts but connote different aspects: signs pointing to the deeper significance, wonders to the impression produced on those who witnessed them.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>Paul here refers to the miracles which he had himself wrought—God wrought special miracles by his hands (Acts 19:11-12). The power of the Holy Spirit may refer either to those miracles or to the gift of prophecy and speaking in tongues—perhaps to both.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>Note all three words—power, signs, wonders—as in Hebrews 2:4; 2 Corinthians 12:12; 2 Thessalonians 2:9. Paul uses repetition of power here with both the signs/wonders and the Holy Spirit. So that expresses the result: the gospel has been fully proclaimed.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": null
        },
        "20": {
            "synthesis": "<p>Paul names the governing ambition of his apostolic career: to preach the gospel where Christ has not yet been named, lest he build on another man's foundation. Calvin argues that this principle defines the essence of the apostolate itself—the apostle's work is to propagate the gospel where it had not been preached; others may edify what apostles have planted, but pioneer proclamation is the apostle's distinctive task. Ellicott calls it a point of honor: Paul set it before him not merely as a duty but as a matter of pride, in the best sense. Clarke notes the etymology of philotimeisthai—to be a friend of honor—and translates it as meaning Paul considered it his honor to preach the gospel where it was before unknown. Wesley adds the cautious observation that this principle did not prevent Paul entirely from building where others had worked, lest his enemies accuse him of being unable to start from the ground.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>The proper and peculiar distinction of the apostleship is to propagate the gospel where it had not been preached. This is what we ought carefully to notice, lest we make no distinction between apostles and pastors who are called to edify established churches.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The apostle set it before him as a point of honour, not merely to carry forward a work that others had begun, but to build up the whole edifice from the foundation himself—not where Christ was named, not in places where there were Christians already.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>I have considered it my honor to preach the Gospel where that Gospel was before unknown. This is the proper import of philotimeisthai—from philos, a friend, and time, honor. As I am not ashamed of the Gospel of Christ, so I esteem it an honor to proclaim it, and especially among the heathen.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>He generally declined places where another apostle had planted, though not altogether, having a holy ambition to make the first proclamation of the gospel where it was quite unheard of, in spite of all the difficulty and dangers that attended it.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": null
        },
        "21": {
            "synthesis": "<p>The pioneer principle of verse 20 finds its scriptural mandate in Isaiah 52:15—those who were not told of him shall see, and those who have not heard shall understand. Paul reads his own career as the fulfillment of this word. Clarke is careful to note that Paul is not claiming the Isaiah text as a direct prediction of his ministry; rather, he is consciously acting in the spirit of what Isaiah declared about the Messiah's worldwide reach. Calvin sees the apostolic logic more firmly: the prophecy mandated a ministry to those who had not heard, and Paul's calling was specifically to discharge that mandate. Ellicott notes that the original context in Isaiah refers to the glorified Servant whose triumph would silence even kings—here Paul applies it to the worldwide evangelization that flows from that glorification. Barnes underlines the honor involved: Paul regarded himself as a privileged instrument in carrying a great prophecy into effect.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He confirms by the testimony of Isaiah what he had said of his apostleship. In Isaiah 52:15, speaking of the kingdom of Messiah, the prophet predicts that the knowledge of Christ would be spread among the Gentiles—that his name would be declared to those by whom it had not been heard. It was meet that this should be done by the Apostles, to whom the command was specifically given.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>From the LXX of Isaiah 52:15. The original has reference to the servant of Jehovah, first suffering and then glorified, so that kings should be dumb with astonishment. Here it is applied to the evangelisation of distant heathen nations as the fruit of that glorification.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>These words, quoted from Isaiah 52:15, the apostle applies to his own conduct; not that the words themselves predicted what Paul had done, but that he endeavored to fulfill such a declaration by his manner of preaching the Gospel to the heathen.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>This is not literally quoted, but the sense is retained. The design of quoting it is to justify the principle on which the apostle acted. He regarded it as a high honour to be the instrument of carrying this prediction into effect.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": null
        },
        "22": {
            "synthesis": "<p>This same pioneering drive explains why Paul has so long been hindered from visiting Rome. He had been entirely occupied with the founding work in regions where Christ had not yet been named; he could not leave a half-completed mission to visit a church already well established. Calvin stresses that Paul is also preemptively clearing himself of any charge of neglect: he had not forgotten Rome, but his God-given course had kept him elsewhere. RWP notes the imperfect tense of was hindered indicates not a single obstacle but repeated interruptions over time. Ellicott and Barnes both agree on these many times as meaning not a number of distinct moments but a sustained pattern of prior demand. Clarke adds the straightforward reason: having found the Gospel already planted at Rome, he preferred to expend his energy where it had not been.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>What he had said of his apostleship he applies now for the purpose of excusing himself for not having come to them. In propagating the gospel from Judea as far as Illyricum, he performed, as it were, a course enjoined him by the Lord; which being accomplished, he purposed not to neglect them.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>And just because he was so anxious to preach the gospel in new regions, and to finish what he had begun there, he had been prevented from coming to Rome sooner. These many times—so often, on many occasions, not merely once or twice.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>He had been so entirely occupied in the leading purpose of his life that he had not been able to come to Rome. I had so frequent and urgent demands on my time elsewhere—I desired to come, but have been unable to leave the vast region where I might preach to those who had never heard the gospel.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>I was hindered—imperfect passive indicating repeated action: I kept being cut off. Paul's pioneering work had repeatedly intervened between his desire to visit Rome and its fulfillment.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": null
        },
        "23": {
            "synthesis": "<p>But now that founding work in the eastern Mediterranean is complete. Paul says he has no more place in these regions—by which he means not that all individuals have heard but that all major population centers have been reached; churches have been planted and left in the care of elders. Ellicott notes the remarkable frankness of this self-assessment: not many preachers would so readily declare their own region exhausted and move on. Clarke, writing from Corinth (where Paul composed this letter), notes that having no large city where Christianity has not yet been planted is the practical criterion. RWP flags the word klima (region, climate) as a rare word meaning originally a slope of the earth—a geographical term brought into use for mission territories. The longing he now feels for Rome is not a new desire but one that has waited long for expression.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The work had been finished, so far as the apostle was concerned, in Asia Minor, Macedonia, and Greece. The churches had been founded and fairly set going; and now he felt it his duty to go on to new fields. Place means room for new working; the whole ground had been already occupied.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>Having no large place or city where Christianity has not yet been planted in which I can introduce the Gospel. The apostle was then at Corinth; and having evangelized all those parts, he had no opportunity of breaking up any new ground.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>Having no longer place in these parts—where Christ has now been preached in every city. The founding work is done; the churches are established; the pioneer season is over in these regions.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>Surprising frankness that the average preacher would hardly use. Paul is now free to come to Rome because there is no demand for him where he is. The word klima (from klinō, to incline), slope then tract of land or region, appears only here in this discussion in the NT.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": null
        },
        "24": {
            "synthesis": "<p>Paul's ambition carries him to Spain—the western edge of the known world—and Rome lies conveniently on the way. The journey to Spain reflects the same governing logic as his eastern mission: take the gospel to the unevangelized frontier. Ellicott traces the tradition that Paul did eventually reach Spain, pointing to Clement of Rome (c. AD 95), who speaks of Paul visiting the extreme limit of the West—though certainty is impossible. Barnes presses a remarkable detail: even here Paul does not make Rome his primary destination but names it as a stopping point on the way to Spain, still driven by the pioneer instinct rather than the prestige of the capital. Wesley catches the beautiful modesty of somewhat satisfied with your company—implying that Christ alone can thoroughly satisfy the soul; Paul hopes only for a partial refreshment among them. Calvin focuses on Paul's apostolic purpose in the visit: not merely fellowship but making himself known in his official character.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>Paul refers to the reason why he had for a long time wished to come to them—even that he might see them, enjoy intercourse with them, and make himself known in his official character; for by the coming of apostles the gospel also came. In saying he would be set forward by them, he intimates how much he reckoned on their kindness.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>In his eagerness to seek out entirely new regions, desiring himself to gather in the fulness of the Gentiles so far as lay in his power, he had determined to push on even to Spain. A tradition dating back to Clement of Rome says he visited the extreme limit of the West—a phrase which seems hardly consistent with any place short of Spain.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>It is remarkable that even here the apostle does not say his principal object was to visit the church at Rome, much as he desired that, but only to take it in his way to Spain—still driven by his higher purpose to preach the gospel where Christ was not named, rather than by the prestige of the capital.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>If first I may be somewhat satisfied with your company—how remarkable is the modesty with which he speaks! They might rather desire to be satisfied with his. Somewhat satisfied—intimating the shortness of his stay; or, perhaps, that Christ alone can thoroughly satisfy the soul.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": null
        },
        "25": {
            "synthesis": "<p>Before the Spain journey, however, Paul has an urgent prior obligation: he is bound for Jerusalem to deliver the collection gathered in Macedonia and Achaia for the poor saints there. Ellicott notes this delivery stands as the close of his apostolic labors in the eastern provinces, the drawing of a curtain before a new act. Barnes points out the remarkable convergence of external evidence: the intended journey is mentioned in Acts 19:21, the actual arrival at Jerusalem for this purpose is recorded in Acts 24:17, and the details in the Corinthian correspondence (1 Cor 16; 2 Cor 8-9) provide the organizational history—all of which Paul's biographer Paley used as strong internal evidence for the epistle's genuineness. Clarke adds the missional significance Paul attaches to the collection (2 Cor 9:12-13): it was not merely material relief but a public sign of Gentile-Jewish solidarity in the church.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Before very long, I hope to pay you this visit, but for the present I am bound for Jerusalem, in the service of the Church, to convey the alms collected in Macedonia and Achaia for the poorer members of that community. This journey to Jerusalem seems to mark the close of his own apostolic labours in those parts.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>The object of his journey to Jerusalem was to carry a contribution made among the Gentile Christians of Macedonia and Achaia for the relief of the poor Jewish Christians at Jerusalem. His design in this affair is very evident from 2 Corinthians 9:12-13, where he shows it not only supplied the want of the saints but was also a sign of the unity of Jews and Gentiles.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>That Paul went to Jerusalem according to his purpose is recorded in Acts 24:17. The intended journey is also mentioned in Acts 19:21 and in 1 Corinthians 16 and 2 Corinthians 8-9. This convergence of evidence has been used by Paley as a strong argument for the genuineness of this epistle.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>But now—repeating the very words used in verse 23. I go—futuristic present. Ministering unto the saints—present active participle of purpose. This collection had been one of Paul's chief cares for over a year.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": null
        },
        "26": {
            "synthesis": "<p>The collection originated in the free and glad decision of the Macedonian and Achaian churches. Paul's word for their decision (eudokesan) indicates voluntary pleasure, not merely compliance—they wanted to do this. Ellicott notes that wealthier churches such as those of Macedonia and Greece would naturally be glad to send relief to the mother church at Jerusalem, which had suffered under both the famine of Claudius's reign and the economic vulnerabilities of a community from which members had sold property in the earliest days. Wesley adds an important corrective: the presence of the poor at Jerusalem does not mean the community of goods described in Acts had already ceased; it simply indicates that in this time of dearth some members were in want. RWP establishes the voluntary character of the gift by the verb form alone, then identifies koinonian as the word for this specific contribution—a fellowship-sharing of material goods.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Literally, for the poor among the saints—it cannot be inferred from this that the church at Jerusalem consisted entirely of poor. Still, wealthier churches such as those of Macedonia and Greece would naturally be glad to have the opportunity of sending relief to the mother church, from which they had received such spiritual benefit.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>The poor of the saints that are in Jerusalem—it can by no means be inferred from this that the community of goods among the Christians was then ceased. All that can be gathered is that in this time of extreme dearth some of the church in Jerusalem were in want, the rest being barely able to subsist themselves.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>They have done it cheerfully and voluntarily—their liberality and cheerfulness are commended by the apostle in 2 Corinthians 8:1-6, 9:2. Paul had been at much pains to obtain this collection, but still they did it freely.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>It hath been the good pleasure—first aorist active of eudokeo, showing that the contribution was voluntary. A certain contribution (koinonian tina)—put thus because it was unknown to the Romans. This sense of koinonia as contribution appears also in 2 Corinthians 8:4 and 9:13.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": null
        },
        "27": {
            "synthesis": "<p>The Gentile contribution to the Jerusalem saints is not merely charity but the discharge of a genuine debt. Paul argues from the greater to the lesser: if the Gentiles have shared in the Jews' spiritual things—the gospel itself, the promises, the scriptures—they are debtors to minister back in material things. Calvin finds the argument binding for Rome no less than for Corinth and Macedonia: the logic of spiritual benefit creates an obligation to material support wherever the dynamic holds. Wesley compresses the syllogism to its essentials: the Gentiles received spiritual things from the Jews through the preaching of the gospel; they owe carnal things in return. Clarke extends the principle to a standing pattern: spiritual labor always creates a debt that can be partially repaid in material support—an argument Paul deploys elsewhere for the support of the ministry (1 Cor 9:11). Barnes calls it a matter of debt, not mere generosity.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>Every one perceives that what is said here of obligation is said not so much for the sake of the Corinthians as for the Romans themselves; for the Corinthians and Macedonians were not more indebted to the Jews than the Romans. The argument is from the greater to the lesser: those who received spiritual things owe carnal things in return.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>It pleased the Macedonians and Achaians to make their contribution. And, indeed, they owed a debt to the church at Jerusalem which it was their duty, as well as they could, to discharge. The spiritual gift received creates a material obligation.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>It was through and by means of the Jews that the Gentiles were brought to the knowledge of God and the Gospel of Christ. These were the spiritual things which they had received; and the pecuniary contribution was the carnal things which the Gentiles were now returning.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>It becomes a matter of debt where the hearer of the gospel receives, in spiritual blessings, far more than he confers by supporting the ministry. Every man who contributes his due proportion to support the gospel is only paying a debt.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": null
        },
        "28": {
            "synthesis": "<p>Once he has sealed the fruit of the collection to the Jerusalem saints, Paul plans to come to Rome on his way to Spain. The verb sealed (sphragisamenos) draws the commentators' attention. Barnes defines it as securing the contribution—making it certain, authenticated, delivered without question; the word is used of sealing a contract or deed. Calvin notes an ancient custom of sealing deposits for safekeeping, and reads Paul's language as a claim to the same scrupulous integrity in handling funds not his own. RWP adds that Paul was keenly sensitive about this collection being delivered free from any suspicion (2 Cor 8:18-23) and chose this metaphor to convey his personal guarantee. Wesley offers the poignant theological note: Paul fully purposed to go to Spain, and yet he never went. There are holy purposes in the minds of good men that are overruled by the providence of God—precious in his sight, even when they never take effect.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>I disapprove not of what some think—that there is here an allusion to the practice among the ancients who closed what they intended to lay up in safety with their seals. Thus Paul commends his own faithfulness and integrity: he was an honest keeper of the money deposited in his hands, carrying it as if sealed.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>To seal an instrument of writing, a contract, or deed is to authenticate it, to make it sure. Paul was going himself to see that the collection was placed securely in their hands. This fruit—the result of the liberality of the Gentile churches, the fruit their benevolence had produced.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>When I have safely delivered to them, as under seal, this fruit of their brethren's love—I will go by you into Spain. Such was his design; but it does not appear that Paul went into Spain. There are often holy purposes in good men's minds that are overruled by the providence of God so as never to take effect—yet precious in his sight.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>Having sealed—first aorist middle participle, antecedent action: having sealed. Paul was keenly sensitive that this collection should be conveyed to Jerusalem free from all suspicion. He seems to regard this journey as the close of his apostolic labours in those parts, the dropping of the curtain before a new act.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": null
        },
        "29": {
            "synthesis": "<p>Paul has full confidence—he says I know—that when he comes to Rome he will come in the fullness of the blessing of Christ. RWP notes that Paul had already said in chapter 1:11-12 that he had a spiritual gift to impart to them, and that he did eventually bring it. Ellicott clarifies the phrase: the fullness of the blessing of Christ does not mean full knowledge of doctrine but the full, abundant measure of the spiritual blessings that Paul, as Christ's apostle, was commissioned to convey. Clarke notes a textual point on which Griesbach and the manuscripts agree: the words of the gospel should be omitted—the fullness of the blessing of Christ is actually a richer formulation than the fullness of the blessing of the gospel of Christ, as it points to Christ himself as the source and content of the blessing. Barnes turns this into a model for every minister: this overflowing confidence in the blessing they carry should characterize all gospel preaching.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>I shall come furnished with the fulness of the blessing of Christ. By this the apostle means the full or abundant measure of those spiritual blessings which he, as the Minister and Apostle of Christ, was commissioned to impart.</p>"
                },
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>These words may be explained in two ways: that he should find a plentiful fruit from the gospel at Rome; or that in order to render his coming more an object of desire, he says that he hopes it would make a great accession to the gospel—he calls this a full blessing, meaning great success.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>The words of the gospel are wanting in almost every manuscript of importance; Griesbach has left them out of the text. The fullness of the blessing of Christ is really more than the fullness of the blessing of the gospel of Christ—pointing beyond the message to its living Author.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>This is a Hebrew mode of expression meaning with a full or abundant blessing. This should be every minister's ever-burning desire in preaching—Paul went to Rome, and he brought to them this fullness.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": null
        },
        "30": {
            "synthesis": "<p>Paul closes the letter's personal section with a rare and earnest request for intercession. He appeals to the Romans by two mediating realities—our Lord Jesus Christ and the love of the Spirit—to strive together with him in prayers to God on his behalf. RWP identifies synagonisasthai as a hapax in the New Testament—a compound of the Greek athletic and military verb for agonizing contest, the same root as the agony of Gethsemane (Luke 22:44). Calvin notes the pastoral vulnerability this reveals: Paul foresaw the dangers awaiting him at Jerusalem from both unbelieving Jews and the testimony of the Spirit in Acts 20:23. Wesley makes the observation that Paul alone among the apostles is recorded asking for the prayers of the faithful on his own behalf—and does so discriminately, with different tones to different churches.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>It is well known how much ill-will prevailed against Paul in his own nation on account of false reports. He was forewarned by the Spirit that bonds and afflictions awaited him at Jerusalem. The more danger he perceived, the more he was moved; hence his solicitude in begging their prayers.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The love of the Spirit—the love inspired in them by the Spirit, flowing from the Spirit. Strive together with me—second my own earnest entreaties before God. The appeal is grounded on both Christological and pneumatological realities working together.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>By that love of God which the Holy Spirit sheds abroad in your hearts—strive together with me. He must pray himself who would have others strive together with him. Of all the apostles, St. Paul alone is recorded to desire the prayers of the faithful for himself.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>That ye strive together with me (synagonisasthai moi)—first aorist middle infinitive, only here in the NT. The simplex agonizomenos appears in Colossians 4:12 of the prayers of Epaphras. For Christ's agony in prayer, see Matthew 26:42; Luke 22:44.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": null
        },
        "31": {
            "synthesis": "<p>Paul specifies the two petitions he asks for: first, that he be delivered from the disobedient in Judea—the unbelieving Jews who regarded him as an apostate and a threat to the law; second, that his service (the Jerusalem collection) be acceptable to the saints—the Jewish Christians who might be persuaded by Judaizers to reject a gift from the man they considered compromised. Ellicott notes that this prayer was partially answered: Paul escaped with his life (Acts 23:27) but only to be delivered to the Romans—a mixed outcome. Calvin sees in this verse one of his finest portraits of Paul's character: wonderful meekness, in that he labored without ceasing for those of whose gratitude he had no certainty, because the obligation to do good does not depend on the recipient's welcome. Barnes presses the ecclesiological stakes: there was real peril of a schism in Christianity if the Jerusalem church rejected the Gentile offering.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>Slanderers had so prevailed that Paul even feared the present would hardly be acceptable. Hence appears his wonderful meekness: he ceased not to labor for those to whom he doubted whether he would be acceptable. We ought to imitate this, so that we may not cease to do good to those of whose gratitude we are by no means certain.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>This prayer of the apostle was partially granted. He escaped with his life from his unbelieving countrymen (Acts 23:27), but only to be delivered over to the Romans. He was naturally in fear of the party to which he had himself once belonged, who would regard him as one of the worst of apostates.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>His countrymen lay in wait for his life; they thought they would do God service by destroying him—not only as an apostate from the Jewish religion but as one labouring to subvert and entirely destroy it. That my service may be acceptable to the saints—that the Jewish and gentile believers may be knit together in tender love.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>There was peril of a schism in Christianity. The Judaizers would give him trouble. Paul foresaw trouble all the way to Jerusalem (Acts 20:23; 21:4, 13). His fears, as the result showed, were well founded.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": null
        },
        "32": {
            "synthesis": "<p>Paul's hope, should God grant the deliverance of verse 31, is to come to the Romans with joy and be refreshed together with them. The two halves of the verse reflect the two petitions of verse 31: if the mission to Jerusalem succeeds, he will arrive in Rome with the gladness of a completed task; if the saints there receive the gift, the journey can continue in the spirit of solidarity Paul has been building throughout the letter. Ellicott notes the unusual compound verb Paul uses for be refreshed—sunanapaüsomai, rare enough to appear in the LXX only at Isaiah 11:6 (the leopard shall lie down with the kid)—emphasizing rest taken together as mutual refreshment, not one-sided reception. Clarke reminds the reader that Paul's fears were well founded (Acts 21-24) and that the Spirit had forewarned him; yet he still desired that welcome. Barnes adds the note that Paul submitted even his most ardent desires to the will of God: if God permit.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The way in which he was received at Jerusalem would make a great difference to the feelings with which the apostle would arrive in Rome. The Greek word for be refreshed together is a rare compound also found in LXX Isaiah 11:6—mutual rest and refreshment taken together.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>That his apprehensions of ill usage were not groundless, and the danger to which his life was exposed was real, we have already seen in Acts 21-24; and that he had such intimations from the Holy Spirit appears from Acts 20:23 and 21:11. Should his journey be prosperous, he hoped to see them at Rome with great joy.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>That I may come unto you—that I may not be impeded by opposition in Judea. By the will of God—if God will, if God permit. After all his desires and all their prayers, it still depended on the will of God; and to that the apostle was desirous to submit.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>That I may come to you—this refers to the former part of the preceding verse, with joy to the latter. Sunanapaüsomai—first aorist middle subjunctive of the double compound: to rest together with, to refresh one's spirit with, only here in the NT.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": null
        },
        "33": {
            "synthesis": "<p>The chapter closes with a brief but theologically weighted benediction: The God of peace be with you all. Amen. The title God of peace is one Paul uses regularly at the close of major sections (1 Thess 5:23; 2 Thess 3:16; 2 Cor 13:11; Phil 4:9; Rom 16:20), but Clarke argues it has particular force here as the summary of the entire epistle. The letter has been, from beginning to end, a sustained argument for peace between Jewish and Gentile believers—in their theology (chs. 1-11) and in their community life (chs. 12-15). Ellicott resists the view that this benediction closes the letter; intercalated doxologies and blessings are frequent in Paul and do not signal conclusion. RWP notes that some scholars have used the Amen here to argue that chapter 16 is a separate letter to the Ephesians, but the manuscript evidence does not support this partition. Barnes calls this the close of the doctrinal and hortatory parts; the remainder belongs to the personal.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>It does not follow that the benediction was intended to close the epistle. Intercalated benedictions and doxologies are frequent in the writings of St. Paul—see Romans 9:5; 11:36; Galatians 6 end; Ephesians 3:20-21—and no inference about the letter's end can safely be drawn from this one.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>The whole object of the epistle is to establish peace between the believing Jews and Gentiles, to show them their mutual obligations and the infinite mercy of God to both. He now concludes with praying that the God of peace—he from whom it comes and by whom it is preserved—may be for ever with them.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>God, the author or promoter of peace and union. The apostle desires that the God who gives peace would impart to them union of sentiment and feeling, particularly between the Jewish and Gentile Christians—the great object for which he laboured throughout this epistle.</p>"
                },
                {
                    "src": "rwp",
                    "attr": "Robertson's Word Pictures",
                    "html": "<p>The God of peace—one of the characteristics of God that Paul often mentions in benedictions. Because of the Amen here some scholars would make this the close of the epistle and chapter 16 a separate epistle to the Ephesians. But the MSS are against it.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": null
        }
    }
}
''')

def main():
    existing = load_synthesis('romans')
    merge_synthesis(existing, ROMANS)
    save_synthesis('romans', existing)
    print('Romans 15 synthesis complete.')

if __name__ == '__main__':
    main()
