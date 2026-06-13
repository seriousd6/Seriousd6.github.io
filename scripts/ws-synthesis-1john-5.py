"""
Wide Source Synthesis — 1 John chapter 5
bookId: 1john
Run: python3 scripts/ws-synthesis-1john-5.py

Sources used: calvin, ellicott (section, vv. 13-21), clarke, wesley, barnes
(mhcc not available; jfb data for this book appears to be Philippians — omitted)
Chapter range: 5 (21 verses)

Key synthesis decisions:
- v7 (Comma Johanneum): Calvin inclines toward retention; Clarke and Barnes reject it as
  interpolation absent from all pre-16th-century Greek MSS; Wesley defends it via Bengel
  and patristic citations — consensus: divided
- v16 (sin unto death): Calvin = final apostasy; Wesley = total apostasy from godliness;
  Clarke surveys multiple Jewish/early-church readings; Barnes reserves judgment — consensus: mixed
- v18 ('sinneth not'): Barnes and Calvin read as permanent security; Wesley reads as
  conditional on continuing faith — consensus: mixed
- v20 ('This is the true God'): Barnes identifies the referent as Jesus Christ; Clarke
  reads it as revealing the Trinity through Christ's coming — consensus: divided
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

ONEJOHN = {
    "5": {
        "1": {
            "synthesis": "<p>The chapter opens with a logical bridge from the love-commands of chapter 4: belief and brotherly love are not two separate duties but two aspects of a single regenerate life. Calvin stresses that since God regenerates us by faith, He must be loved as Father, and that love necessarily embraces all His children — <em>faith cannot be separated from love</em>. The argument is structural: if one is born of God, one loves the Father; and love for the Father extends by natural kinship to all the Father's other children. Clarke and Barnes read the verse similarly, noting that to believe Jesus is the Christ is to receive all the Messianic promises, and that belief generates a filial love toward God that extends to His family. Wesley characteristically frames it in terms of natural affection: those born of God have <em>a natural affection to all his brethren</em>, the way any child loves siblings who share the same parent. The verse thus grounds brotherly love not in sentiment or moral obligation but in the shared reality of divine birth — which means that testing one's love for fellow Christians becomes a test of whether one's faith is genuine at all.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He confirms by another reason that faith and brotherly love are united; for since God regenerates us by faith, he must necessarily be loved by us as a Father; and this love embraces all his children. Then faith cannot be separated from love. The first truth is, that all born of God believe that Jesus is the Christ; where Christ alone is set forth as the object of faith, as in him it finds righteousness, life, and every blessing that can be desired.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>The scope and sum of this whole paragraph appears from the conclusion of it: 'These things have I written to you who believe, that ye may know that ye who believe have eternal life.' So faith is the first and last point with St. John also. Every one who loveth God that begat, loveth him also that is begotten of him — hath a natural affection to all his brethren.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>This is repeating the same truth in another form. If we love him who has begotten us, we shall also love his children, or our Christian brethren. In other places the apostle says that we may know that we love God if we love those who bear his image. He here offers another confirmation: we may have undoubted evidence that we love God, and from that, infer that we have true love to his children.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "2": {
            "synthesis": "<p>Verse 2 inverts the logic of verse 1. Where verse 1 said that loving God means loving His children, verse 2 says that we can confirm our love for God's children by first establishing that we love God and keep His commandments. Calvin notes that this reversal serves a necessary theological purpose: men may love one another for private advantage or carnal friendship, but Christian love requires God to hold the primacy. If love to God is genuine, love to the brethren follows necessarily; if love to the brethren is claimed without love to God, it is suspect. Clarke puts it plainly: our love of God's followers is a proof that we love God, and keeping the commandments is the evidence that the love is genuine rather than sentimental. Barnes observes that John deliberately builds a mutual-confirmation structure — each test reinforces the other, so that neither love of God nor love of the brethren stands alone as self-certifying. The verse guards against both a cold orthodoxy (honoring God while caring nothing for His people) and a sentimental humanitarianism (loving people without honoring God).</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He briefly shows in these words what true love is, even that which is towards God. He now teaches us that men are rightly and duly loved when God holds the primacy. It often happens that we love men apart from God, as unholy and carnal friendships regard only private advantages or some other vanishing objects. His purpose is to show that mutual love ought to be cultivated in such a way that God may be honored.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>By this we know that we love the children of God — our love of God's followers is a proof that we love God. Our love to God is the cause why we love his children, and our keeping the commandments of God is the proof that we love him.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>John says that there is another way of determining what we are. We may have undoubted evidence that we love God, and from that, as the basis of an argument, we may infer that we have true love to his children. Of the fact that we may have evidence that we love God, apart from that which we derive from our love to the brethren, there can be no doubt.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "3": {
            "synthesis": "<p>John now addresses the obvious objection: if keeping God's commandments is the test of genuine love, are they not an insupportable burden? The verse answers directly — God's commandments are not grievous. Calvin handles this with pastoral nuance: he acknowledges that the law is spiritually impossible apart from regeneration (Paul in Romans 7 makes this plain), yet the Spirit creates within the born-again believer a love that transforms the character of the demand from foreign constraint into native desire. Clarke captures this in a proverb that has become memorable: <em>Love feels no loads</em>. The burden that might crush the unwilling servant becomes natural to the willing child. Barnes distinguishes carefully between those who are and are not disposed to obey: complaints that God's laws are unreasonable come exclusively from those who have no intention of keeping them; those who sincerely endeavor to obey do not find them oppressive. Wesley is the most compact: God's commandments are not grievous <em>to any that are born of God</em> — the qualifier does all the work. The verse does not deny that obedience is difficult in practice but claims that regeneration transforms the orientation of the heart toward those commands.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>John, in order to rouse our efforts, says that God's commandments are not grievous. As the denial of self is a prelude to keeping the law — and since the law is spiritual, as Paul teaches in Romans 7 — John must mean that although the law is onerous to those under it as a yoke, to those renewed by the Spirit and walking in love it is otherwise. The Spirit creates a delight in the law that makes its demands feel native rather than foreign.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>His commandments are not grievous — are not burdensome; for no man is burdened with the duties which his own love imposes. The old proverb explains the meaning of the apostle's words: <em>Love feels no loads</em>. Love to God brings strength from God; through his love and his strength, all his commandments are not only easy and light, but pleasant and delightful.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>The meaning is that his laws are not unreasonable; the duties which he requires are not beyond our ability; his government is not oppressive. It is easy to obey God when the heart is right; and those who endeavour in sincerity to keep his commandments do not complain that they are hard. All complaints of this kind come from those who are not disposed to keep his commandments.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "4": {
            "synthesis": "<p>The connective <em>for</em> explains why obedience is not burdensome: all who are born of God overcome the world. The regenerate life is not a life of grinding resistance but of genuine victory. Calvin attends to the Greek grammar — the neuter <em>pan to gegennēmenon</em> ('whatever is born of God') encompasses all classes of believers: male and female, Jew and Gentile, old and young — an all-inclusive category. Wesley reads 'whatsoever' as implying the most unlimited universality and identifies faith as the grand means of overcoming, since 'all things are possible to him that believeth.' Barnes frames the conflict concretely: the world in its maxims, customs, and social pressures does not rule the believer; he is a freeman from that system. Clarke offers the most distinctive reading, suggesting that 'the world' may refer specifically to the Jewish establishment that denied the Messiah, and that the verse may address Gentile converts' capacity to refute that unbelief on its own terms. All voices agree that the victory is real and present, not merely eschatological, and that its mechanism is faith rather than moral effort or natural temperament.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He also sets forth the way of overcoming. The words literally are, 'For every thing begotten by God overcomes the world.' The neuter gender is used for the masculine — 'every thing' for 'every one' — in order to comprehend all sorts of persons, males and females, young and old, Jews and Gentiles, bond or free. He then makes the victory over the world depend on faith.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>For whatsoever — this expression implies the most unlimited universality — is born of God overcometh the world: conquers whatever it can lay in the way, either to allure or fright the children of God from keeping his commandments. And this is the victory — the grand means of overcoming — even our faith, seeing all things are possible to him that believeth.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>The world, in its maxims and precepts and customs, does not rule him, but he is a freeman. The idea is that there is a conflict between religion and the world, and that in the heart of every true Christian, religion secures the victory. In John 16:33 the Saviour says, 'Be of good cheer; I have overcome the world,' laying the foundation for a victory by his people over all vice, error, and sin.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "5": {
            "synthesis": "<p>Verse 5 answers the implicit question of verse 4 with a challenge: <em>who</em> overcomes the world? John's answer is exclusive — only the one who believes that Jesus is the Son of God. Calvin frames this christologically: the believer overcomes 'because we derive strength from Christ,' as Paul says in Philippians 4:13. One who is 'diffident as to himself' and recumbs on Christ's power alone is the one who can conquer Satan, the world, and his own flesh — and no one else. Clarke reads the verse against the backdrop of Jewish unbelief, arguing that only the one who believes in Christ's divine Sonship can claim the Messianic promises and thereby refute the claim that the old order is still sufficient. Barnes makes the point experientially: a person may overcome one worldly passion by sheer willpower, or abandon one vice, or leave corrupt company, but 'unless he has faith in the Son of God, the spirit of the world will reign supreme in his soul in some form.' Wesley is the most pointed: 'Who is superior to all worldly care, desire, fear? Every believer, and none else.' All voices agree that world-overcoming faith is specific — it is faith in the Sonship of Jesus, not generic religious sincerity.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>This is a reason for the previous sentence: we conquer by faith, because we derive strength from Christ; as Paul also says, 'I can do all things through him that strengtheneth me.' He only can conquer Satan and the world who, diffident as to himself, recumbs on Christ's power alone. For 'faith' here means a real apprehension of Christ, or an effectual laying hold on him, by which we apply his power to ourselves.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>All else are worldly and governed by worldly aims and principles. It is true that a man may gain a victory over one worldly passion, or abandon the gay circle, or break away from habits of profaneness; but still, unless he has faith in the Son of God, the spirit of the world will reign supreme in his soul in some form. The appeal which John so confidently made in his time may be as confidently made now.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>Who is he that overcometh the world — that is superior to all worldly care, desire, fear? Every believer, and none else.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "6": {
            "synthesis": "<p>Having established that faith in Christ's Sonship overcomes the world, John now presents the grounds of that faith — the evidence that this Jesus is indeed the Son of God. He identifies two historical realities: the water and the blood. Calvin connects these to the Old Testament ceremonial system: water represented purification before God, enabling approach; blood effected expiation and pledged full reconciliation. Jesus fulfills both in their substance, not their shadow. Wesley takes the water as referring specifically to Jesus' baptism at the Jordan, where the Spirit descended and the Father spoke, and the blood as referring to the cross — noting that 'when all was finished, blood and water came out of his side.' Clarke similarly identifies the water with the baptism, when divine attestation was given publicly, and the blood with the sacrificial death that fulfilled prophetic expectation. Barnes emphasizes the role of the Spirit as the third element: all three witnesses together form a single, convergent testimony. The phrase 'not by water only' guards against any reading that spiritualizes the ministry while minimizing the cross.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He alludes by the words to the ancient rites of the law. The comparison is intended not only that we may know that the Law of Moses was abolished by the coming of Christ, but that we may seek in him the fulfillment of those things which the ceremonies formerly typified. By water was all filth washed away, so that men might come before God pure and clean; and by blood was expiation made, and a pledge given of full reconciliation with God.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>Jesus is he of whom it was promised that he should come. Who came — not by the water only, wherein he was baptized, but by the water and the blood — which he shed when he had finished the work his Father had given him to do. He not only undertook at his baptism 'to fulfil all righteousness,' but on the cross accomplished what he had undertaken; in token whereof, when all was finished, blood and water came out of his side.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>Jesus was attested to be the Son of God and promised Messiah by water — his baptism, when the Spirit of God came down from heaven upon him, and the voice from heaven said, 'This is my beloved Son, in whom I am well pleased.' Jesus Christ came also by blood — he shed his blood for the sins of the world. Here the apostle says that the Spirit witnesses this; he came not by water only, but by blood also, without which the world could not be saved.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "7": {
            "synthesis": "<p>No verse in 1 John — perhaps in all the NT epistles — has generated more sustained controversy than verse 7. The text as printed in the Received Text reads: 'For there are three that bear record in heaven: the Father, the Word, and the Holy Ghost: and these three are one.' This clause, known as the Comma Johanneum, divides the tradition sharply on textual grounds.</p><p>Calvin acknowledges the dispute, noting that 'even the Greek copies do not agree,' but concludes that 'since the passage flows better when this clause is added, and as I see that it is found in the best and most approved copies, I am inclined to receive it' — while admitting this judgment rests on printed copies rather than Greek manuscripts. Wesley mounts a vigorous patristic defense, citing Bengel, Tertullian, and Cyprian, and argues that the verse is 'the sun' of the epistle without which verses 6, 8, and 9 are disconnected.</p><p>Clarke is categorical in the other direction: the verse is 'wanting in every MS. of this epistle written before the invention of printing' except one, absent from all ancient versions, and 'most probably spurious.' Barnes reaches the same conclusion at length. The weight of all subsequent textual scholarship has sided with Clarke and Barnes — the Comma Johanneum is absent from the critical Greek text — though the Trinitarian unity it expresses is affirmed across the NT by less contested passages.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>As even the Greek copies do not agree, I dare not assert any thing on the subject. Since, however, the passage flows better when this clause is added, and as I see that it is found in the best and most approved copies, I am inclined to receive it as the true reading. He probably refers to printed copies in his day, and not to Greek MSS.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>What Bengel has advanced, both concerning the transposition of these two verses and the authority of the controverted verse, will abundantly satisfy any impartial person. For there are three that testify — literally, <em>testifying</em>, or bearing witness. The participle is put for the noun 'witnesses,' to intimate that the act of testifying and the effect of it are continually present.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>It is likely this verse is not genuine. It is wanting in every MS. of this epistle written before the invention of printing, one excepted — the Codex Montfortii, in Trinity College, Dublin. The others which omit this verse amount to one hundred and twelve. It is wanting in both the Syriac, all the Arabic, Ethiopic, Coptic, Sahidic, Armenian, Slavonian versions — in a word, in all the ancient versions but the Vulgate.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>There is no passage of the New Testament which has given rise to so much discussion in regard to its genuineness as this. The supposed importance of the verse in its bearing on the doctrine of the Trinity has contributed to this. On the one hand, the clear testimony which it seems to bear to the doctrine of the Trinity has made that portion of the Christian church which holds the doctrine reluctant to abandon it.</p>"
                }
            ],
            "consensus": "divided",
            "key_tension": "Calvin and Wesley argue the verse's internal coherence and patristic citations support its retention; Clarke and Barnes hold that its absence from all Greek manuscripts before the sixteenth century requires its rejection as an interpolation."
        },
        "8": {
            "synthesis": "<p>Verse 8 completes the thought of verse 6 — or, in the critical text, provides the full sentence of which verse 7 is a spurious interpolation. The three earthly witnesses are the Spirit, the water, and the blood, 'and these three agree in one.' Calvin argues that the Spirit holds the primary place among these three, for without the Spirit the water and blood would 'flow without any benefit' — it is the Spirit who seals on our hearts the testimony of the other two, and by his power makes the fruit of Christ's death come to us. Clarke follows Wesley's schema: the Spirit witnesses through the word confirmed by miracles; the water witnesses through baptism, which typifies purification and consecration to Christ; the blood witnesses through the Lord's Supper and its application to the believer's conscience. Barnes explains the Spirit's testimony as including the inner experience of grace, the transformation produced by believing, and the miraculous attestations of the apostolic era — all of these confirming that Jesus is who He claimed to be. All voices affirm that these three witnesses converge on a single point — the divine Sonship of Jesus — and that their concurrence constitutes legally sufficient testimony by the standards of any court.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He applies what had been said of water and blood to its own purpose. He adds a third witness, the Holy Spirit, who yet holds the first place; for without him the water and blood would have flowed without any benefit. It is he who seals on our hearts the testimony of the water and the blood; it is he who by his power makes the fruit of Christ's death to come to us; yea, he makes the blood shed for our redemption to penetrate into our hearts.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>The Spirit — in the word confirmed by miracles; the water — in baptism, wherein we are dedicated to the Son, typifying his spotless purity and the inward purifying of our nature; and the blood — represented in the Lord's Supper, and applied to the consciences of believers. And all these harmoniously agree in the same testimony, that Jesus Christ is the Divine, the complete, the only Saviour of the world.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>The testimony of the Holy Ghost to the fact that Jesus is the Son of God is contained in the evidence which the Spirit gave at his baptism, in the miraculous gifts bestowed upon the apostles, in the conversion of sinners, and in the peace and joy which are imparted to those who believe in him — all concurring in the one declaration that Jesus is the Son of God.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "9": {
            "synthesis": "<p>Verse 9 draws a lesser-to-greater argument: if human testimony commands our assent — as it must in courts, commerce, and daily life — then divine testimony commands it far more. Calvin states the logic sharply: 'if in worldly affairs we stand to the words of men, who may lie and deceive, how unreasonable it is that God should have less credit given to him, when sitting as it were on his own throne.' Clarke formulates the asymmetry with elegant brevity: God 'can neither be deceived nor deceive, but man may deceive and be deceived.' Barnes observes that the practice of crediting human testimony is so universal and unavoidable that we could not function for a single day without it — we act on it constantly, unreflectively, from the moment we wake. Against this backdrop, refusing to credit God's testimony about His Son is not a neutral intellectual posture but a special irrationality and culpability. Wesley reduces the argument to its essential form: God's testimony 'is greater — of higher authority, and much more worthy to be received.' All voices agree on the a fortiori structure and its corollary: rejecting the divine testimony about Christ is not merely unbelief but an active insult to God's truthfulness.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He proves, reasoning from the less to the greater, how ungrateful men are when they reject Christ. If in worldly affairs we stand to the words of men, who may lie and deceive, how unreasonable it is that God should have less credit given to him, when sitting as it were on his own throne, where he is the supreme judge. Then our own corruption alone prevents us from receiving Christ.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>If we receive the witness of men — which all are obliged to do, and which is deemed a sufficient testimony to truth in numberless cases — the witness of God is greater. He can neither be deceived nor deceive, but man may deceive and be deceived.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>We are constantly acting on the belief that what others say is true. We could not get along a single day if we did not act on this belief; nor are we accustomed to call it in question, unless we have reason to suspect that it is false. The mind is so made that it must credit the testimony borne by others; and if this should cease even for a single day, the affairs of the world would come to a pause.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>If we receive the testimony of men — as we do continually, and must do in a thousand instances — the testimony of God is greater: of higher authority, and much more worthy to be received; namely, this very testimony which God the Father, together with the Word and the Spirit, hath testified of the Son, as the Saviour of the world.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "10": {
            "synthesis": "<p>Verse 10 moves from the objective ground of testimony to its subjective reception, and then to the gravity of its rejection. The believer who credits God's testimony about His Son has that testimony confirmed inwardly — 'hath the witness in himself.' Calvin carefully guards this inner witness from being misunderstood as a private, free-floating revelation independent of the external evidence. Rather, it is the Spirit who 'imprints on our hearts' the testimony of the water and the blood — the inner confirmation is the fruit and seal of the objective testimony. Barnes similarly: the inner witness is 'the fruit of all the evidence, external and internal, on the heart, producing this result' — peace, transformed desires, answers to prayer — amounting to 'the deepest conviction of the truth that Jesus is the Son of God.' Clarke expresses this warmly: 'to know, to feel his sin forgiven, to have the testimony of this in the heart from the Holy Spirit himself, is the privilege of every true believer.' Wesley is sharpest on the reverse: the unbeliever 'hath made him a liar,' which is not a mild intellectual error but a practical accusation against the truthfulness of God. The believer's inner witness and the unbeliever's culpability are two sides of one coin.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>The Apostle, after having reminded us that God deserves to be believed much more than men, now adds that we can have no faith in God except by believing in Christ, because God sets him alone before us. He does not say that God speaks outwardly, but that every one of the godly feels within that God is the author of his faith. It hence appears how different from faith is a fading opinion dependent on something else.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>He that believeth on the Son of God — this is God's witness to a truth, the most important and interesting to mankind. God has witnessed that whosoever believeth on his Son shall be saved and have everlasting life, and shall have the witness of it in himself — the Spirit bearing witness with his spirit that he is a child of God. To know, to feel his sin forgiven, to have the testimony from the Holy Spirit himself, is the privilege of every true believer.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>He that believeth on the Son of God hath the testimony — the clear evidence of this — in himself. He that believeth not God, in this, hath made him a liar; because he supposes that to be false which God has expressly testified.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "11": {
            "synthesis": "<p>Verse 11 states the content of God's testimony plainly: God has given us eternal life, and this life is in His Son. Calvin notes that the formulation is deliberately inviting — not merely a command to obey but a gift 'so sweet and so lovely' that prompt faith should be the natural response, and ingratitude for such an offer is 'intolerable.' He also draws out what 'in his Son' means: life is not merely mediated through Christ as a channel but located in him as its source and seat. Clarke grounds the verse soteriologically: the life is 'a right to endless glory, and a meetness for it,' and it comes only through Christ — 'no other scheme of salvation can be effectual; God has provided none other.' Wesley traces the Trinitarian movement of the verse: eternal life is 'purchased by, and treasured up in, his Son, who has all the springs and the fulness of it in himself, to communicate to his body, the church, first in grace and then in glory.' Barnes notes John's deliberate allusion to the Gospel of John (John 1:4; 14:6) and underscores the totality of the claim: Christ is not one path among several but the exclusive location of life.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>Having now set forth the benefit, he invites us to believe. Since he freely offers life to us, our ingratitude will be intolerable unless with prompt faith we receive a doctrine so sweet and so lovely. The words of the Apostle are intended to show that we ought not only reverently to obey the gospel, lest we affront God; but that we ought to love it, because it brings to us eternal life. We hence learn what is especially to be sought in the gospel — the free gift of salvation.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>This is the record — the great truth to which the Spirit, the water, and the blood bear testimony. God hath given us eternal life — a right to endless glory, and a meetness for it. And this life is in his Son; it comes by and through him; he is its author and its purchaser. No other scheme of salvation can be effectual; God has provided none other, and in such a case a man's invention must be vain.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>This is the sum of that testimony: that God hath given us a title to, and the real beginning of, eternal life; and that this is purchased by, and treasured up in, his Son, who has all the springs and the fulness of it in himself, to communicate to his body, the church, first in grace and then in glory.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "12": {
            "synthesis": "<p>Verse 12 states the binary corollary of verse 11: to have the Son is to have life; to lack the Son is to lack life. The stark simplicity is deliberate. Calvin confronts the obvious objection — great men throughout history who never knew Christ apparently lived virtuous and admirable lives. He answers that whatever appears eminent in fallen human goodness is not genuine life in the biblical sense; the appearance of virtue apart from Christ is not the reality of life. Barnes traces the verse's logic back to Jesus' own words in John 5:24 and John 17:3, so that John is affirming a principle Christ Himself laid down. Clarke is arrestingly direct, almost aphoristic: 'An indwelling Christ and Glory; no indwelling Christ, No glory. God's record must stand.' Wesley makes a careful pastoral distinction: in the positive clause John says simply 'the Son,' because believers know him intimately; in the negative clause he adds 'the Son of God,' so that unbelievers may fully understand the weight of what they are forfeiting. All voices agree that the verse is not triumphalist exclusion but the straightforward consequence of the logic in verse 11 — if life is located in Christ, then there is no life apart from Him.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>We are greatly mistaken if we think that whatever is eminent in our nature is genuine life. We know what it is to have Christ, for he is possessed by faith. He then shows that all who are separated from the body of Christ are without life.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>He that hath the Son hath life — as the eternal life is given in the Son of God, it follows that it cannot be enjoyed without him. No man can have it without having Christ. It is in vain to expect eternal glory if we have not Christ in our heart. The indwelling Christ gives both a title to it and a meetness for it. This is God's record. An indwelling Christ and Glory; no indwelling Christ, No glory. God's record must stand.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>He that hath the Son — living and reigning in him by faith — hath this life. He that hath not the Son of God hath not this life — hath no part or lot therein. In the former clause, the apostle says simply, the Son, because believers know him; in the latter, the Son of God, that unbelievers may know how great a blessing they fall short of.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "13": {
            "synthesis": "<p>Here John pauses to state the purpose of the whole epistle: that those who believe may know they have eternal life. Calvin reads 'know' as a call to ongoing confirmation and deepening assurance — the epistle is not evangelistic but confirmatory in aim: 'as there ought to be a daily progress in faith, so he says that he wrote to those who had already believed, so that they might believe more firmly and with greater certainty.' Clarke describes the kind of knowing John intends — not 'a blind reliance for, but an actual enjoyment of, salvation; Christ living, working, and reigning in the heart.' Wesley notices a significant tense shift: in the introduction (1:4) John said 'I write'; now he says 'I have written,' marking the closure of the letter's argument and the sufficiency of what has been set forth. Barnes adds that John writes also 'that ye may continue to believe' — implying that assurance is not a static possession but the fruit of continuing engagement with the testimony John has presented. Ellicott identifies this verse as a fresh statement of purpose equivalent to the opening of the epistle, placing what follows (vv. 14-21) as practical application of the assurance established here.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>As there ought to be a daily progress in faith, so he says that he wrote to those who had already believed, so that they might believe more firmly and with greater certainty, and thus enjoy a fuller confidence as to eternal life. The use of doctrine is not only to initiate the ignorant in the knowledge of Christ, but also to confirm those more and more who have been already taught.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>That ye may know that ye have eternal life — I write to show your privileges, to lead you into this holy of holies, to show what believing on the Son of God is, by the glorious effects it produces: it is not a blind reliance for, but an actual enjoyment of, salvation; Christ living, working, and reigning in the heart.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>These things have I written — in the introduction, 1 John 1:4, he said, I write; now, in the close, I have written. That ye may know — with a fuller and stronger assurance — that ye have eternal life.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>On vv. 13-21: Fresh Statement of the Purpose of Writing, equivalent to that at the beginning of the Epistle. What can be done for those who do not come up to the standard assumed throughout the Epistle. Some practical points recapitulated: God's sons do not sin; personal assurance that we are God's sons; personal assurance that Christ is come, of the gift of the spiritual sense, and of abiding in the God of Truth through His Son.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "14": {
            "synthesis": "<p>From assurance of eternal life, John moves to one of its chief fruits: confidence in prayer. Calvin identifies this access to God as among the most precious gifts of faith — 'were we driven away from an access to God, nothing could make us more miserable; but, provided this asylum be opened to us, we should be happy even in extreme evils.' The qualifier 'according to his will' is crucial: Clarke specifies that God's will means what He has revealed and promised in Scripture — prayer is not blank-check petition but faith-informed request aligned with His declared purposes. Barnes draws attention to the Greek word for 'confidence' (παρρησία), which implies the liberty to speak freely and openly before one's sovereign — an access previously impossible apart from Christ. Wesley is economical but complete: believers 'have this farther confidence in him, that he heareth — that is, favourably regards, whatever prayer we offer in faith, according to his revealed will.' All voices agree that this confidence in prayer is itself a mark of genuine faith and a fruit of the eternal life established in vv. 11-13.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He commends the faith he mentioned by its fruit: the godly dare confidently to call on God. Were we driven away from an access to God, nothing could make us more miserable; but, provided this asylum be opened to us, we should be happy even in extreme evils; nay, this one thing renders our troubles blessed, because we surely know that God will be our deliverer. Let us bear in mind that calling on God is the chief trial of our faith.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>This is the confidence — παρρησία, the liberty of access and speech — that if we ask any thing according to his will, that is, which he has promised in his word. His word is a revelation of his will in the things which concern the salvation of man. All that God has promised we are justified in expecting; and what he has promised, and we expect, we should pray for.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>The confidence referred to here is that which relates to the answer to prayer. The sense is that one of the effects of believing on the Lord Jesus is that we have the assurance that our prayers will be answered. The word 'confidence' (παρρησία) implies the liberty to speak freely before one's sovereign — an access previously impossible, now opened through Christ.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "15": {
            "synthesis": "<p>Verse 15 draws the logical consequence of verse 14: if God hears prayer (which verse 14 affirmed), then the believer can be assured of already having the petitions asked. Calvin addresses the apparent paradox — are the petitions obtained before the event? He answers that the godly 'pray or ask for nothing from God but what they obtain,' because they pray only for what aligns with God's commanded purposes, not for indiscriminate desires or private wishes. Clarke emphasizes immediacy: 'God gives it to him who prays, when it is needful. We are not to ask today for mercy that we now need, and not receive it till tomorrow.' Barnes adds a pastoral qualification: the specific thing asked may not always be granted (as in Luke 22:42 or 2 Corinthians 12:8-9), but 'the prayer will not be disregarded, and the thing which is most for our good will be bestowed.' The faith that 'anticipates the blessings,' as Wesley says, is not presumption but the natural posture of a child who trusts a faithful Father. All voices agree that the assurance is real and not merely rhetorical, grounded in God's faithfulness to His stated purposes.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>When he says that all the petitions of the faithful are heard, he speaks of right and humble petitions, such as are consistent with the rule of obedience. For the faithful do not give loose reins to their desires, nor indulge in anything that may please them, but always regard in their prayers what God commands. This is an application of the general doctrine to the special and private benefit of every one, lest the faithful should doubt that God is propitious to the prayers of each individual.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>And if we know that he hear us — seeing we are satisfied that he hears the prayer of faith requesting the things which himself has promised — we know, consequently, that we have the petitions that we desired of him; for he cannot deny himself. We are not to ask today for mercy that we now need, and not receive it till tomorrow. God gives it to him who prays when it is needful.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>We have — faith anticipates the blessings — the petitions which we asked of him, even before the event. And when the event comes, we know it comes in answer to our prayer.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "16": {
            "synthesis": "<p>Verse 16 applies the prayer-confidence of vv. 14-15 to a specific and difficult case: intercession for a brother who sins. John distinguishes between a sin 'not unto death,' for which prayer is appropriate and effective, and a 'sin unto death,' for which he does not command prayer. The distinction has generated substantial interpretive dispute. Calvin identifies 'sin unto death' as final apostasy from God's grace — a complete falling away in which 'all sense of religion' is lost and the person has 'surrendered himself wholly to the devil and the flesh.' Wesley takes a similar line: the sin unto death is 'total apostasy from both the power and form of godliness,' and the point is not that prayer is forbidden but that John makes no obligation to pray for such a person. Clarke surveys three distinct early traditions: the Jewish legal distinction between capital and lesser offenses; the early church's practice of distinguishing public excommunicable sins from private, pardonable ones; and the identification with final impenitence or unbelief. Barnes notes 'great diversity of opinion' and declines to pronounce firmly, suggesting the most probable reading is willful, persistent rejection of Christ leading to irrecoverable ruin. The shared conviction across all voices is that there is a category of sin so grave that it places a person beyond ordinary intercession.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>The Apostle extends the benefits of faith so that our prayers may avail for our brethren. He would also have us regard the falls of the brethren as stimulants to prayer. He shows that sin unto death belongs to those who have wholly fallen away from the grace of God — those who have lost all sense of religion and surrendered themselves wholly to the devil and the flesh. For those who sin not unto death, God keeps them even in their falls, so that they do not perish.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>If any one see his brother sin a sin which is not unto death — that is, any sin but total apostasy from both the power and form of godliness — let him ask, and God will give him life for that sinner. There is a sin unto death: I do not say that he shall pray for that. A sin unto death may likewise mean one which God has determined to punish with death.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>This is an extremely difficult passage. What is the sin not unto death, for which we should ask? And what is the sin unto death, for which we should not pray? Three chief opinions are noted: the Jewish legal distinction between capital sins and lesser transgressions; the early church distinction between public excommunicable sins and private pardonable ones; and the identification of the sin unto death with unbelief or final impenitence.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>There has been great diversity of opinion in regard to the meaning of this passage, and the views of expositors of the New Testament are by no means settled as to its true sense. It does not comport with my design to examine the opinions which have been held in detail. The most probable reading is final, willful, persistent rejection of Christ leading to irrecoverable ruin.</p>"
                }
            ],
            "consensus": "mixed",
            "key_tension": "Calvin and Wesley identify the sin unto death as final apostasy from God's grace; Clarke finds multiple early traditions each with merit; Barnes reserves judgment, noting that expositors have never reached consensus on the verse's specific referent."
        },
        "17": {
            "synthesis": "<p>Verse 17 serves as a pastoral guardrail around the frightening verse 16: although there exists a sin unto death, not all sin is of that character. The verse guards against two opposite errors: complacency (pretending that sin is inconsequential) and despair (imagining that any fall places one beyond hope of forgiveness). Calvin considers two readings — 'though all unrighteousness is sin, yet every sin is not unto death,' or 'since sin is every unrighteousness, it follows that not every sin is unto death' — and notes that the practical result is the same either way. Clarke is characteristically terse: 'every act contrary to justice is sin — is a transgression of the law which condemns all injustice.' Barnes uses the verse to frame a proportionate response: readers should feel deep awareness that there is an unforgivable sin, while also feeling free to intercede generously for those who fall into ordinary transgressions. Wesley reduces it to a memorable maxim: 'All deviation from perfect holiness is sin; but all sin is not unpardonable.' All voices affirm the same balanced message and agree the verse's function is precisely this dual guardrail.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>This passage may be explained variously. If you take it adversatively: 'Though all unrighteousness is sin, yet every sin is not unto death.' Equally suitable is another meaning: 'As sin is every unrighteousness, hence it follows that every sin is not unto death.' As the result is nearly the same, I leave it to the judgment of readers to determine which of the two is the more appropriate.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>All deviation from perfect holiness is sin; but all sin is not unpardonable.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>This seems to be thrown in to guard what he had just said. He says also that there are many other forms and degrees of sin — sin for which prayer may be made. Everything which does not conform to the holy law of God is to be regarded as sin; but we are not to suppose that all sin of that kind is of such a character that it cannot possibly be forgiven. There are many who commit sin for whom we may hope for recovery, and for them it is proper to pray.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "18": {
            "synthesis": "<p>Verse 18 opens the epistle's closing triad of 'we know' statements. The first: whoever is born of God does not sin — and the one born of God keeps himself, so that the evil one does not touch him. Calvin connects this backward to verses 16-17: we need never treat a true Christian as one who has committed the unpardonable sin, because the person born of God 'keeps himself' and does not suffer himself to be so led away as to lose all sense of religion. Barnes draws the same connection and makes it the basis for perseverance: a genuine Christian cannot commit the unpardonable sin, which for him constitutes evidence of the saints' final security. Clarke locates the protection in active relationship with God — 'keeping himself in the love of God' (as Jude 21 commands), in prayer and faith, so that Christ's indwelling leaves the devil nothing of his own nature to work on. Wesley offers a carefully conditional reading: 'so long as that loving faith abides in him, he neither speaks nor does anything which God hath forbidden' — subtly allowing that the protection is relational rather than automatic, contingent on the exercise of ongoing faith.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He says that those who do not wholly fall away from the grace of God keep themselves — that is, keep themselves in the fear of God — and do not suffer themselves to be so led away as to lose all sense of religion, and to surrender themselves wholly to the devil and the flesh. For when he says they are not 'touched unto death,' reference is made to a deadly wound; for the children of God do not remain untouched by the devil's darts, but they are not slain by them.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>Whosoever is born of God sinneth not — this is spoken of adult Christians; they are cleansed from all unrighteousness. Keepeth himself — that is, in the love of God, by building up himself on his most holy faith and praying in the Holy Ghost; and that wicked one toucheth him not — finds nothing of his own nature in him on which he can work, Christ dwelling in his heart by faith.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>He that is born of God — that sees and loves God — sinneth not: so long as that loving faith abides in him, he neither speaks nor does anything which God hath forbidden. He keepeth himself — watching unto prayer. And, while he does this, the wicked one toucheth him not — so as to hurt him.</p>"
                }
            ],
            "consensus": "mixed",
            "key_tension": "Barnes and Calvin read 'sinneth not' as a mark of the believer's permanent security and evidence of final perseverance; Wesley reads it as conditional on the ongoing exercise of loving faith, allowing for the theoretical loss of this protection."
        },
        "19": {
            "synthesis": "<p>The second 'we know': believers are of God; the whole world lies in the evil one. Calvin reads this as a pastoral application — he takes what has been declared about God's children in general and brings it directly to the readers, urging them 'to prove by our separation from the world, and by the sanctity of our life, that we have not been in vain called God's children.' The contrast between 'we are of God' and 'the whole world lieth in the wicked one' is stark. Clarke's reading of the Greek εν τω πονηρω (which the KJV renders 'wickedness' but which most interpreters take as masculine — 'the wicked one') is vivid: the world is 'embraced in the arms of the devil, where it lies fast asleep and carnally secure, deriving its heat and power from its infernal fosterer.' Wesley quotes his own note at length: 'In this short expression the horrible state of the world is painted in the most lively colours.' Barnes settles the grammatical question toward the masculine, linking the world's condition to the same 'evil one' from whom Christ keeps believers in verse 18 — so that the two realities (protection of the born-of-God, bondage of the world) are set in deliberate contrast.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He deduces an exhortation from his previous doctrine; for what he had declared in common as to the children of God, he now applies to those he was writing to, to stimulate them to beware of sin and to encourage them to repel the onsets of Satan. Let readers observe that it is only true faith that applies to us the grace of God; for the Apostle acknowledges none as faithful but those who have the dignity of being God's children.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>We know that we are of God — have the fullest proof of the truth of Christianity and of our own reconciliation to God. The whole world lieth in the wicked one — εν τω πονηρω κειται — lieth in the wicked one, embraced in the arms of the devil, where it lies fast asleep and carnally secure, deriving its heat and power from its infernal fosterer. What a truly awful state!</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>We know that we are children of God — by the witness and the fruit of his Spirit. But the whole world — all who have not his Spirit — lieth in the wicked one, void of life, void of sense. In this short expression the horrible state of the world is painted in the most lively colours; a comment on which we have in the actions, conversations, contracts, quarrels, and friendships of worldly men.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "20": {
            "synthesis": "<p>The third 'we know' brings the epistle to its theological summit: the Son of God has come and has given believers a spiritual understanding — a capacity to know the true God — and the believers are in Christ, 'the true God and eternal life.' Calvin presents Christ as the source of 'a sure knowledge of the true God' uniquely: without Christ, knowledge of God remains uncertain and unstable, but through Him believers know God with a certainty that can sustain them in every contest against darkness. Clarke reads the final clause broadly, seeing the verse as revealing the eternal Trinity through the Son's incarnation — Father, Word, and Holy Spirit together disclosed in the event of Christ's coming. Barnes argues that 'This is the true God and eternal life' refers specifically and directly to Jesus Christ, making verse 20 one of the strongest explicit Christological identifications in the New Testament — a deliberate affirmation that the Son who has come is Himself the very God whom the epistle has been describing.</p><p>The interpretive question of the antecedent of 'this' (Greek οὗτος) — whether it points back to Jesus Christ or to 'him that is true' (the Father) — is one of the most consequential in the verse. Barnes represents the majority of later commentators in reading it as an identification of Christ with God; Clarke stands with those who read it as Trinitarian rather than narrowly Christological.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>The Apostle now reminds them where this knowledge is especially to be found. He says that God has been so made known to us that now there is no reason for doubting. The Apostle does not without reason dwell on this point; for except our faith is really founded on God, we shall never stand firm in the contest. He shows that we have obtained through Christ a sure knowledge of the true God, so that we may not fluctuate in uncertainty.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>The Son of God is come into the flesh, and hath given us an understanding — a more eminent degree of light than we ever enjoyed before — that we may know him who is true, even the True God, and get eternal life from him through his Son. And it is through this revelation of Jesus that we know the ever blessed and glorious Trinity; and the Trinity, Father, Word, and Holy Ghost, in the eternal, undivided unity of the ineffable Godhead.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>We know this by the evidence that John had referred to in this epistle. And hath given us an understanding — not a new faculty of mind, but such instruction that we do understand the great truths referred to. All the correct knowledge which we have of God is to be traced directly or indirectly to the great Prophet whom God has sent into the world. 'This is the true God and eternal life' most naturally refers to Jesus Christ, making this one of the strongest explicit identifications of Christ with God in the NT.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>We know that the Son of God is come into the world. And he hath given us a spiritual understanding, that we may know him, the true one. And we are in the true one, even in Jesus Christ, the eternal Son of God. This Jesus is the only living and true God, together with the Father and the Spirit, and the original fountain of eternal life. So the beginning and the end of the epistle agree.</p>"
                }
            ],
            "consensus": "divided",
            "key_tension": "Barnes reads 'This is the true God' as identifying Jesus Christ directly with the divine name, one of the strongest explicit Christological affirmations in the NT; Clarke reads it as revealing the Trinity as a whole through Christ's coming, with the antecedent being 'him that is true' (the Father)."
        },
        "21": {
            "synthesis": "<p>The final verse is the epistle's closing command: 'Little children, keep yourselves from idols.' After the exalted Christology of verse 20 — in which the Son of God is declared the source of true understanding and eternal life — the closing word descends to the most concrete and practical plane. Calvin links the warning directly to the 'vivifying light of the Gospel': wherever the true knowledge of God shines, every form of idolatrous attachment becomes visible and must be resisted. He extends the warning characteristically toward the Reformation concern about religious imagery: 'who does not see that images are a great help to superstition?' Clarke reads the command on two levels: literal (against pagan idol-feasts, a genuine danger for Gentile converts in the Roman world) and spiritual — 'no idols in your houses, none in your churches, none in your hearts.' Barnes agrees on the double reference: immediate protection from temple meals with idol devotees, and the broader principle that nothing should 'estrange their hearts from' the true God. Wesley offers the deepest and most interior reading: an idol is anything 'loving, desiring, fearing more than God.' The abrupt closing is not a non sequitur but the epistle's logical conclusion — true knowledge of God, properly received, makes idolatry in every form unthinkable.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>Though this be a separate sentence, it is an appendix to the preceding doctrine. The vivifying light of the Gospel ought to scatter and dissipate all mists from the minds of the godly. The Apostle not only condemns idolatry, but commands us to beware of all images and idols; by which he intimates that the worship of God cannot continue uncorrupted and pure whenever men begin to be in love with idols or images. So innate in us is superstition that the least occasion will infect us with its contagion.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>Little children — τεκνια, beloved children — he concludes with the same affectionate feeling with which he commenced. Keep yourselves from idols — avoid the idolatry of the heathens; not only have no false gods, but have the true God. Have no idols in your houses, none in your churches, none in your hearts. Have no object of idolatrous worship by attending to which your minds may be divided and prevented from worshipping the infinite Spirit in spirit and in truth.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes on the NT",
                    "html": "<p>His great object had been to lead them to the knowledge and love of God, and all his counsels would be practically followed if, amidst the temptations of idolatry and the allurements of sin, nothing were allowed to estrange their hearts from him. Keep yourselves from idols — from worshipping them; from all that would imply communion with them or their devotees.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>Keep yourselves from idols — from all worship of false gods, from all worship of images or of any creature, and from every inward idol; from loving, desiring, fearing anything more than God. Seek all help and defence from evil, all happiness in the true God alone.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        }
    }
}

def main():
    existing = load_synthesis('1john')
    merge_synthesis(existing, ONEJOHN)
    save_synthesis('1john', existing)
    print('1 John 5 synthesis complete.')

if __name__ == '__main__':
    main()
