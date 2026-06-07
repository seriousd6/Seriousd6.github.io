"""
Wide Source Synthesis — Romans chapter 8
bookId: romans
Run: python3 scripts/ws-synthesis-romans-8.py

Sources used: calvin, ellicott, clarke, wesley, barnes
Chapter range: 8  (39 verses)

Key synthesis decisions:
- v.4: "Righteousness of the law fulfilled in us" — Calvin reads this as justification/imputation
  (the law's claims met in Christ's sacrifice); Ellicott reads it as practical moral fulfillment
  now possible through the Spirit. consensus: divided
- v.20: Who is "the creature" and who subjected it? Barnes reads "the creature" as the renewed
  Christian; Calvin/Wesley read it as the created order subjected by God at the fall (Gen 3:17).
  consensus: divided on referent
- v.29: Foreknowledge and predestination — Calvin reads election as unconditional sovereign choice;
  Wesley reads "whom he foreknew" as those he foreknew would be conformable to the image of his Son,
  making foreknowledge conditional on foreseen response. consensus: divided
- v.28: Ellicott notes a textual variant (Vatican/Alexandrian MSS + Origen) inserting "God" as
  explicit subject rather than "all things" as subject. consensus: affirm on the comfort; mixed on text
- Ellicott missing keys: 14, 29, 31, 32, 33. Wesley missing keys: 11, 12, 25, 39.
- Clarke v.1 entry is a chapter outline; Barnes v.1 is a chapter intro — actual verse content
  taken from their commentary body rather than the outline headings.
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
    "8": {
        "1": {
            "synthesis": "<p><em>There is therefore now no condemnation for those who are in Christ Jesus.</em> This is one of the great declarative sentences of the New Testament, and Paul places it at the hinge of Romans after the agonized contest with the flesh in chapter seven. Calvin notes that though the godly are perpetually beset by sin, they are exempt from the power of death — the contest with indwelling sin does not negate the verdict of acquittal. Ellicott observes that the word <em>therefore</em> connects forward as well as back: the apostle had already touched the confines of this deliverance at the close of chapter seven, and now enters fully into it.</p><p>Wesley underlines the scope of the declaration: <em>no condemnation, either for things present or past.</em> The ground is union with Christ, not moral achievement — which is why the declaration can stand even while the struggle described in chapter seven continues. Barnes calls this chapter one of the most interesting and precious portions of Scripture, identifying its central concern as the power of the gospel to sustain believers through present suffering toward certain glory.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>After having described the contest which the godly have perpetually with their own flesh, he returns to the consolation which was very needful for them, and which he had before mentioned; and it was this — that though they were still beset by sin, they were yet exempt from the power of death, because the Spirit of God dwells in them, by whose power the lusts of the flesh are mortified.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The Apostle had already, at the end of the last chapter, touched the confines of that state of deliverance and of liberty which he is now going on to describe. The opening of this chapter is, therefore, connected in form with the close of the last. The intervention of Christ puts an entirely different face upon the situation.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>There is therefore now no condemnation — either for things present or past. Now he comes to deliverance and liberty. The apostle here resumes the thread of his discourse, which was interrupted at Romans 7:7.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>This chapter is a continuation of the subject discussed in the previous chapter, and is designed to show the power of the gospel in delivering from the dominion of sin, and in producing peace and salvation. Its main scope and design is apparent to all — that believers are justified, sanctified, and secure in the love of God.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "2": {
            "synthesis": "<p>The ground of the declaration in v.1 is explained: <em>the law of the Spirit of life in Christ Jesus has set you free from the law of sin and death.</em> Calvin notes that Paul uses the word <em>law</em> loosely for the Spirit himself, since the Spirit applies Christ's blood to cleanse and also exerts his power to sanctify — both dimensions together constitute liberation from the dominion sin previously exercised. Clarke sees the gospel itself described here: not merely a rule but a sovereign energy by which guilt is removed and the power of sin is broken.</p><p>Wesley offers the sharpest distinction: the law of the Spirit = the gospel; the law of sin and death = the Mosaic dispensation, which could diagnose sin but had no power to overcome it. Barnes sees a broader meaning — the Spirit exerts a controlling influence analogous to a law, and that influence breaks the rule which sin and death previously held.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>Using a language not strictly correct, by the law of the Spirit he designates the Spirit of God, who sprinkles our souls with the blood of Christ, not only to cleanse us from the stain of sin with respect to the guilt that is before God, but also to sanctify us thoroughly, so that we may serve God in holiness of life.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>A statement of the great antithesis, of which the rest of the section is a development, between the law of the Spirit of life and the law of sin and of death. <em>The law of the Spirit of life</em> — a phrase defining more fully the mode in which the union with Christ becomes operative in the believer.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>The gospel of the grace of Christ, which is not only a law or rule of life, but affords that sovereign energy by which guilt is removed from the conscience, the power of sin broken, and its polluting influence removed from the heart. The law was a spiritual bondage; the gospel is a spiritual liberty.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>The law of the Spirit — that is, the gospel. Hath freed me from the law of sin and death — that is, the Mosaic dispensation, which, binding us under sin and death, was in this respect a law of sin and death.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "3": {
            "synthesis": "<p>God accomplished what the law could not do precisely because the law was weakened by the flesh — it could diagnose sin and condemn it, but it could not expel it. God's remedy was to send his own Son in the <em>likeness of sinful flesh</em> and as a sin offering, thereby condemning sin in the flesh. Calvin sees this as the heart of free justification: the Son assumed our humanity, met the law's demands on our behalf, and by his sacrifice made the condemnation announced in v.3 the condemnation of sin, not of the sinner.</p><p>Ellicott highlights the precision of Paul's language: <em>in the likeness of sinful flesh</em> — the Son genuinely took a body of flesh (real humanity) but not sinful flesh itself. Wesley notes the logic of necessity: with our sinful flesh we were devoted to death, so God sent his own Son in the likeness of that flesh to bear the judgment we deserved. Clarke observes that the law could not pardon or sanctify by its own nature; God's sending of the Son fills precisely that gap.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>Now follows the polishing of his proof, that the Lord has by his gratuitous mercy justified us in Christ; the very thing which it was impossible for the law to do. That he treats here of free justification is clear from this — that he ascribes it to Christ alone, and that by abolishing sin; for sin being taken away, righteousness necessarily follows.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Precisely on that very point where the law of Moses showed its impotence — namely, in the attempt to get rid of sin, which it failed to do because of the counteracting influence of the flesh — precisely on this very point God interposed by sending His Son in a body of flesh similar to our own sinful flesh, and, by the sacrifice of that body, condemned and extirpated sin.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>For what the law of Moses could not do, in that it was weak through the flesh — incapable of conquering our evil nature. We with our sinful flesh were devoted to death. But God sending his own Son, in the likeness of sinful flesh — the very same flesh which in us is sinful — condemned sin in the flesh.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>The law of God, the moral law — it could not free from sin and condemnation. It was feeble and inefficacious, in consequence of the opposition and counteraction of the flesh. But God interposed by sending his Son, who accomplished what the law could not accomplish — taking away the power of sin by the sacrifice of himself.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "4": {
            "synthesis": "<p><em>That the righteousness of the law might be fulfilled in us, who walk not after the flesh but after the Spirit.</em> This verse produces the sharpest exegetical division in the chapter. Calvin insists that Paul is speaking of imputed righteousness — the law's demands are fully met in Christ's sacrifice and credited to believers; the phrase <em>fulfilled in us</em> refers to justification, not to our moral performance, since believers never in this life make such proficiency that their law-keeping is full or complete. To read this as our actual compliance with the law's moral demands is, for Calvin, a gloss wholly alien to Paul's meaning here.</p><p>Ellicott reads the verse quite differently: the consequence of God's condemnation of sin in the flesh is precisely that the moral requirements of the law can now be met by the Spirit-led believer. The removal of the flesh's counteracting influence makes actual obedience possible where it was impossible before. Both Calvin and Ellicott agree that the Spirit's presence is indicated by the phrase <em>who walk not after the flesh</em>; they differ on whether <em>righteousness fulfilled</em> is imputed or infused.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>They who understand that the renewed, by the Spirit of Christ, fulfil the law, introduce a gloss wholly alien to the meaning of Paul; for the faithful, while they sojourn in this world, never make such a proficiency, as that the justification of the law becomes in them full or complete. This righteousness is not in our works, but in the forgiveness of sins; and it is fulfilled in us when we are pardoned and freely justified.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The consequence of this was a great change. Hitherto the Law could not be kept because of the antagonistic influence of the flesh; henceforth it may be kept for the reason that this influence has ceased and that its place is taken by the influence of the Spirit. <em>The righteousness</em> — the just requirement or demand of the Law.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>That the righteousness of the law might be fulfilled in us — that the guilt might be pardoned through the merit of that sacrifice; and that we might be enabled, by the power of his own grace and Spirit, to walk in newness of life; loving God with all our heart, soul, mind, and strength, and our neighbour as ourselves.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>That we might be conformed to the law, or be obedient to its requirements, and no longer under the influence of the flesh and its corrupt desires. <em>Might be fulfilled</em> — that we might be obedient, or comply with its demands. <em>Who walk</em> — who live; who conduct themselves according to the guidance of the Spirit.</p>"
                }
            ],
            "consensus": "divided",
            "key_tension": "Calvin reads 'the righteousness of the law fulfilled in us' as justification by imputation — the law's claims are met in Christ and credited to the believer; Ellicott and Clarke read it as moral transformation through the Spirit making actual obedience to the law's requirements possible."
        },
        "5": {
            "synthesis": "<p>Paul explains the two orientations by their objects: those who live <em>according to the flesh</em> set their minds on the things of the flesh; those who live <em>according to the Spirit</em> set their minds on the things of the Spirit. Calvin notes that Paul introduces this contrast not only to confirm the preceding argument by what is opposite, but also to distinguish genuine believers from hypocrites who claim the Spirit while remaining carnally minded. Ellicott sharpens the anthropology: those who are <em>after</em> the flesh are not merely people who sometimes succumb to fleshly impulses, but people whose whole mental and moral orientation is set upon those impulses — the flesh has become their governing principle.</p><p>Wesley connects this directly to the life of affections: the carnally minded have their thoughts and affections fixed on things visible, temporal, and pleasurable; the spiritually minded on things spiritual and eternal. Barnes applies the distinction diagnostically: it reveals the fundamental condition of the soul, whether renewed or not.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He introduces this difference between the flesh and the Spirit, not only to confirm, by an argument derived from what is of an opposite character, what he has before mentioned — that the grace of Christ belongs to none but to those who, having been regenerated by the Spirit, strive after purity — but also that hypocrites might not vainly boast that they have faith, while they are entirely under the dominion of the flesh.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Those who not only walk — direct their conduct — according to the promptings of the flesh, but who are in themselves and in the whole bent of their dispositions the slaves of these promptings. <em>Do mind the things of the flesh</em> — their whole mental and moral activity is set upon those things which minister to the gratification of the senses.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>They that are after the flesh — who remain under the guidance of corrupt nature — mind the things of the flesh — have their thoughts and affections fixed on such things as gratify corrupt nature; namely, on things visible and temporal; on things of the earth, on pleasure, on praise, and on all the things in which the natural man places his happiness.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>They that are after the flesh — those who are under the influence of the corrupt and sinful desires of the flesh, those who are unrenewed — do mind the things of the flesh; they are supremely devoted to the gratification of their corrupt desires. But they that are after the Spirit — those who are renewed — mind the things of the Spirit.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "6": {
            "synthesis": "<p>The mind of the flesh is death; the mind of the Spirit is life and peace. Paul names the two outcomes with characteristic directness. Ellicott renders the verse more precisely: <em>For the mind of the flesh is death, but the mind of the Spirit is life and peace</em> — to think of nothing but the gratification of the senses is in itself a form of death, that dead condition of the soul which issues in eternal death. Calvin traces the meaning of the Greek word behind <em>carnally minded</em> to Moses's language about the imagination of the heart, encompassing all the faculties of the soul directed toward earth rather than heaven.</p><p>Wesley maps the terms diagnostically: to be carnally minded is <em>a sure mark</em> of spiritual death and the way to death everlasting; to be spiritually minded is a sure mark of spiritual life and the way to life everlasting. Clarke connects the two outcomes eschatologically: the carnally minded live in the state of condemnation and are liable to eternal death; the spiritually minded have the life and peace of God in the soul and are in full prospect of glory.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Translate: <em>For the mind of the flesh is death, but the mind of the Spirit is life and peace.</em> To think of nothing but the gratification of the senses, is in itself death — that dead condition of the soul which issues in eternal death; and, on the other hand, to have the thoughts and affections governed by the Spirit is life and peace.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>For to be carnally minded is death — to live under the influence of the carnal mind is to live in the state of condemnation, and consequently liable to death eternal: whereas, on the contrary, he who is spiritually minded has the life and peace of God in his soul, and is in full prospect of eternal glory.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>For to be carnally minded — that is, to mind the things of the flesh — is death: the sure mark of spiritual death, and the way to death everlasting. But to be spiritually minded — that is, to mind the things of the Spirit — is life: a sure mark of spiritual life, and the way to life everlasting. And peace — peace with God, peace with conscience, and peace with all things.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>For to be carnally minded — the minding of the flesh — leads to condemnation and death. The expression is one of great energy, and shows that it not only leads to death, but that it is itself a species of death — a deadness to all the pure and holy enjoyments for which man was made.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "7": {
            "synthesis": "<p>The reason the carnal mind leads to death is that it is <em>enmity against God</em>. Paul does not say it is merely unfriendly to God, or in tension with God — it is constitutive opposition, not subject to God's law and in fact incapable of subjection to it. Clarke identifies this as the necessary consequence of its nature: because it is a carnal mind, relishing earthly and sinful things and living in opposition to the holy law of God, it is therefore irreconcilable and implacable hatred toward God. This is not a secondary characteristic of the unconverted soul but its very essence.</p><p>Calvin follows the structural logic Paul establishes: beginning at vv.4-5 with two characters — those after the flesh and those after the Spirit — and now explaining the first more deeply: not merely mindful of fleshly things but actively hostile to God's authority. Barnes reads this as the explanation Paul owes the reader from v.6: the carnal mind is death <em>because</em> it implies enmity with God, and enmity with God is itself death.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He does not reverse the order here, as he sometimes does; he takes the first character — those after the flesh — because it is first as to us in order of time. And now he shows more fully what the carnal mind is — not merely negligent of God but actively opposed to his law, incapable of submission, and therefore incapable of pleasing him.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>Because the carnal mind is enmity against God — because it is a carnal mind, and relishes earthly and sinful things, and lives in opposition to the pure and holy law of God: therefore, it is enmity against God; it is irreconcilable and implacable hatred. It is not subject to the law of God, neither indeed can be — this incapability arises from its own nature.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>This is given as a reason for what is said in Romans 8:6. In that verse the apostle had affirmed that to be carnally minded was death, but he had not stated why. He now explains it by saying that it is enmity against God, and thus involves a sinner in conflict with him, and exposes him to all the consequences of his displeasure.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "8": {
            "synthesis": "<p>The conclusion follows: those who are in the flesh cannot please God. Calvin frames this as a positive inference from what has been said — those who give themselves up to be guided by the lusts of the flesh are all of them abominable before God, since the flesh as a governing principle is constitutively opposed to him. Clarke draws the connection explicitly: <em>because</em> this carnal mind is enmity against God, those under its power cannot perform a single act that can be called pleasing to God, because the rebellious principle underlying their acts poisons them at the root.</p><p>Ellicott adds a negative expectation: it cannot be expected that those absorbed in the things of sense should be able to please God. Barnes names the practical referent: those who are unrenewed sinners, following supremely the desires of the flesh and not led by the Spirit of God.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>The Apostle infers from what had been said, that those who give themselves up to be guided by the lusts of the flesh, are all of them abominable before God; for he has thus far confirmed this truth — that all the deeds which flow from the flesh are displeasing to him, and that thus all who have not put off the nature of the flesh are hateful to God.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>So then — because this carnal mind is enmity against God — they that are in the flesh, who are under the power of the workings of this carnal mind, cannot please God — because of the rebellious workings of the carnal principle; every act they perform, every prayer they offer, every service they attempt to render, is vitiated by this principle.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>So then. It follows; it leads to this conclusion. They that are in the flesh — they who are unrenewed sinners; who are following supremely the desires of the flesh — cannot please God. This is given as a clear and necessary consequence of what had been established, that the carnal mind is enmity against God.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "9": {
            "synthesis": "<p>Having described the carnal person, Paul turns to address his readers: <em>you, however, are not in the flesh but in the Spirit, if in fact the Spirit of God dwells in you.</em> Calvin reads this as a hypothetical application of a general truth — Paul directs his discourse to them specifically so they might gather from the previous description that they are of the number of those who are led by the Spirit. The address is both assurance and examination. Ellicott notes an important theological point: the Spirit of God and the Spirit of Christ are used as convertible terms in this verse — the Spirit of Christ is indeed the very presence of Christ himself in the believer.</p><p>Wesley draws the sharpest and most serious application: <em>if any man have not the Spirit of Christ, he is none of his</em> — a plain, express declaration that admits of no exception. No Spirit, no union with Christ; no union, no salvation. Barnes notes the positive force of the address: <em>you</em> Christians are characterized by the Spirit's presence, which is the opposite condition from what he has been describing.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He applies hypothetically a general truth to those to whom he was writing; not only that by directing his discourse to them particularly he might more powerfully affect them, but also that they might with certainty gather from the description already given, that they were of the number of those who are led by the Spirit of God.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Such is not your case — if at least the Spirit of God and of Christ dwells in you, as it should in every Christian. It is to be observed that the Spirit of God and the Spirit of Christ are used as convertible terms. The Spirit of Christ is indeed the presence of Christ Himself in the soul of the believer.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>In the Spirit — under his government. If any man have not the Spirit of Christ — dwelling and governing in him — he is none of his — he is not a member of Christ; not a Christian; not in a state of salvation. A plain, express declaration, which admits of no exception. He that hath ears to hear, let him hear.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>But ye — you who are Christians. Not in the flesh — not under the full influence of corrupt desires and passions. But in the Spirit — that is, you are spiritually minded; you are under the influence of the Holy Spirit; this is your general character, your governing principle.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "10": {
            "synthesis": "<p><em>But if Christ is in you, although the body is dead because of sin, the Spirit is life because of righteousness.</em> Calvin observes that Paul here moves from speaking of the Spirit to speaking of Christ, since by the Spirit Christ consecrates us as temples to himself and by the same Spirit dwells in us — the two are not separable. Ellicott clarifies the term <em>dead</em>: it refers to physical death, not spiritual death — the body is still under the sentence of physical mortality that sin brought, and that sentence remains. But the Spirit is <em>life</em> — not merely alive but the source of life.</p><p>Wesley traces the logic: where the Spirit of Christ is, there is Christ himself. The body is devoted to physical death because of past sin — this consequence remains. But the spirit of the believer is truly alive because righteousness has now been attained through Christ. Barnes reads this as the pivotal transformation: the same presence of Christ that leaves the body under mortality raises the inner person to genuine spiritual life.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>What he had before said of the Spirit he says now of Christ, in order that the mode of Christ's dwelling in us might be intimated; for as by the Spirit he consecrates us as temples to himself, so by the same he dwells in us. The body, he says, is dead on account of sin, while the spirit is life on account of righteousness — that is, the Spirit quickens and enlivens by the righteousness obtained for us.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The results of the presence of Christ in the soul. <em>The body is dead because of sin</em> — here the word is evidently used of physical death. The doom entailed by sin still, indeed, attaches to the body — but only to the body. The body, indeed, must die, but there the hold of sin upon the Christian ends.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>Now if Christ be in you — where the Spirit of Christ is, there is Christ. The body indeed is dead — devoted to death. Because of sin — heretofore committed. But the Spirit is life — already truly alive. Because of righteousness — now attained. The spirit of the true believer is life, already entered into life everlasting.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>And if Christ be in you — the close connection between him and Christians, and the fact that they are led by his spirit, gives occasion to the expression that Christ is in them. The body is dead because of sin — the body is mortal; it is subjected to death by sin. But the spirit is life because of righteousness — the soul is made alive by the righteousness of Christ.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "11": {
            "synthesis": "<p>The Spirit who raised Jesus from the dead will also give life to the mortal bodies of those in whom he dwells. Calvin reads this as an argument from efficient cause: since by the power of God's Spirit Christ was raised, and since that Spirit possesses eternal power, he will exert the same toward believers. The resurrection of Christ is not a completed event disconnected from the believer's future — it is the pattern and pledge of their own. Ellicott extends this further: the vitality that the Spirit gives extends beyond the grave, and will react even upon the material body that was given over to death.</p><p>Clarke grounds the comfort in the resurrection of Christ as demonstrative evidence: God raised Christ by his Spirit; the Spirit now dwelling in believers is that same Spirit with that same power; therefore their resurrection to eternal life is certain. Barnes focuses on the argument from power: he who had power to restore Christ to life has power to give life to those in whom that Spirit dwells.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>This is a confirmation of the last verse, derived from the efficient cause. Since by the power of God's Spirit Christ was raised, and since the Spirit possesses eternal power, he will also exert the same with regard to us. And he takes it as granted, that the Spirit which dwells in Christ dwells also in all his members.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>And this vitality extends beyond the grave. It will even react upon that material body which had just been spoken of as given over to death. Die it must; but the same Spirit to which the soul owes its life will also reinfuse life into the dead body, just as the body of Christ was raised by the same Spirit.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>He who here receives the grace and Spirit of Christ, and continues to live under its influence a life of obedience to the Divine will, shall have a resurrection to eternal life; and the resurrection of Christ is the evidence and pledge of the resurrection of all who are his members.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>He that raised up Christ from the dead — he that had power to restore him to life, has power to give life to you. He that did, in fact, restore him to life, will also restore you. The argument seems to be founded, first, on the power of God, and second, on his promise and purpose.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "12": {
            "synthesis": "<p>Paul draws the practical conclusion: <em>So then, brothers, we are debtors, not to the flesh, to live according to the flesh.</em> Calvin identifies this as the conclusion of the preceding argument — if we are to renounce the flesh, we ought not to consent to it; if the Spirit ought to reign in us, it is inconsistent not to attend to his bidding. The sentence is structurally incomplete (Paul omits the positive counterpart — the debt owed to the Spirit — because it follows naturally from what he has said), but its force is full. We owe the flesh nothing.</p><p>Clarke notes that Paul here addresses both Jews and Gentiles together, drawing the general conclusion from all his preceding arguments about holiness and its obligations. Barnes specifies the grounds of the debt: the Spirit dwells in us, his design is to purify us, we have been recovered from the death of sin to the life of religion — one who has received so much, and who has been so recovered, owes the flesh nothing in return.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>This is the conclusion of what has been previously said; for if we are to renounce the flesh, we ought not to consent to it; and if the Spirit ought to reign in us, it is inconsistent not to attend to his bidding. Paul's sentence is here defective, for he omits the other part of the contrast — he does not add to whom we are debtors — because this was sufficiently clear from the context.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p><em>We are debtors</em> — we are under an obligation. Observe that in the lively sequence of thought the second clause of the antithesis is suppressed: <em>We are under an obligation, not to the flesh</em> — but to the Spirit. The suppression adds to the rhetorical force.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>We are debtors — we owe it as a matter of solemn obligation. This obligation arises first, from the fact that the Spirit dwells in us; second, because the design of his indwelling is to purify us; third, because we are thus recovered from the death of sin to the life of religion. One who has received so much owes the flesh nothing.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "13": {
            "synthesis": "<p>The stakes are named plainly: <em>if you live according to the flesh, you will die; but if by the Spirit you put to death the deeds of the body, you will live.</em> Calvin adds a threat to strengthen what might otherwise remain a mild appeal — those who boast of justification by faith without the Spirit of Christ are self-deceived, since there is no confidence in God where there is no desire for holiness. The mortification of the body's deeds is not optional for believers but the very evidence of genuine Spirit possession. Ellicott renders the verse precisely: mortifying the deeds of the flesh <em>through the Spirit</em> means bringing them to a condition of deadness and atrophy.</p><p>Wesley notes the breadth of what must be mortified: not only evil actions but evil desires, evil tempers, and evil thoughts. Barnes underscores that mortification can only be accomplished through the Spirit's aid — this is not willpower but dependence. The result — life — is both spiritual life more abundant now and life everlasting hereafter.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He adds a threatening, in order more effectually to shake off their torpor; by which also they are fully confuted who boast of justification by faith without the Spirit of Christ, though they are more than sufficiently convicted by their own conscience; for there is no confidence in God, where there is no desire for holiness.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>If under the influence of the Spirit you reduce to a condition of deadness and atrophy all those practices to which the impulses of your material nature would prompt you — then you will live. The mortification is real, not merely formal; and it is accomplished only by the Spirit's power, not by unaided resolve.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>The deeds of the flesh — not only evil actions, but evil desires, tempers, thoughts. If ye mortify — kill, destroy these. Ye shall live — the life of faith more abundantly here, and hereafter the life of glory.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>Through the Spirit — by the aid of the Spirit; by cherishing and cultivating his influences. What is here required can be accomplished only by the aid of the Holy Ghost. Do mortify — put to death; subdue entirely; destroy the influence of the corrupt and carnal propensities. The result — life — is both present spiritual vitality and eternal life.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "14": {
            "synthesis": "<p><em>For all who are led by the Spirit of God are sons of God.</em> Calvin reads this as a confirmation of v.13: the sons of God are identified precisely by being ruled by his Spirit. This defeats the empty boasting of hypocrites who claim the title of God's children without the Spirit's governance. The privilege of sonship and the reality of Spirit-direction cannot be separated — the one is the evidence of the other. Clarke grounds this in the mediatorial work of Christ and the assistance of the Spirit: no man can find the way to heaven or walk in it when found without divine assistance.</p><p>Wesley marks this as the point at which Paul enters the great description of blessedness, comprising what he will call <em>glorified</em> in v.30 — though the description begins not with mere glory but with the mixed state of sonship in a suffering world. Barnes names the specific content of the new topic: the Spirit of adoption, in contrast to the spirit of bondage that characterized the old dispensation.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>This is a confirmation of what has immediately preceded; for he teaches us, that those only are deemed the sons of God who are ruled by his Spirit; for by this mark God acknowledges them as his own people. Thus the empty boasting of hypocrites is taken away, who without any reason assume the title of the children of God.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>No man who has not Divine assistance can either find the way to heaven, or walk in it when found. As Christ, by his sacrificial offering, has opened the kingdom of God to all believers, the Spirit leads those believers into all truth, and guides them through every difficulty and danger in the way to glory.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>For as many as are led by the Spirit of God — in all the ways of righteousness — they are the sons of God. Here St. Paul enters upon the description of those blessings which he comprises in the word <em>glorified</em> at Romans 8:30; though, indeed, he does not describe mere glory, but that which is still mingled with suffering.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>For as many as are led — as submit to his influence and control. The Spirit is represented as influencing, suggesting, and guiding; the believer as yielding to that influence and following that guidance. This introduces the new topic of sonship, adoption, and heirship — the full benefits of the gospel.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "15": {
            "synthesis": "<p>The Spirit given to believers is not the <em>spirit of bondage</em> — the slavish fear that characterized existence under the law — but the <em>Spirit of adoption</em>, by whom we cry <em>Abba! Father!</em> Calvin identifies two effects of this Spirit that together confirm certainty of salvation: first, he was not given to torment or harass, but to produce peace and quiet confidence; second, the very cry <em>Abba</em> is evidence that God has created a genuine filial relationship in the soul. Ellicott recovers the precise force of the Greek: <em>a spirit of bondage</em> means the dominant habit of mind found in a slave — perpetual fear, insecurity, no confident approach to the master.</p><p>Clarke gives the historical background: those under the law were in bondage to its rites and ceremonies, and since they fell short of the law's demands, their dominant experience was fear of condemnation. Wesley observes the double witness implied: the Spirit prompts the cry <em>Abba</em>, and we ourselves cry it — both dimensions of the relationship are present.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He now confirms the certainty of that confidence, in which he has already bidden the faithful to rest secure; for the Spirit has not been given for the purpose of harassing us with trembling or of tormenting us with anxiety; but, on the contrary, that quietness of conscience may succeed in us which the certainty of our adoption produces.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p><em>Spirit of bondage</em> — the Greek corresponds to what we should naturally understand as <em>such a spirit as would be found in slaves.</em> The word <em>spirit</em> here means the dominant habit or frame of mind. The spirit of a slave is perpetual fear — fear of the master, fear of punishment, no filial confidence.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>Ye have not received the spirit of bondage — all that were under the law were under bondage to its rites and ceremonies; and as, through the prevalence of corrupt nature which the law gave no assistance to remove, they were often transgressing and consequently living in fear of punishment, the spirit of bondage and fear was the general characteristic of that dispensation.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>The spirit of bondage — the spirit that binds you; or the spirit of a slave, that produces only fear. The slave is under constant fear and alarm. But the spirit of religion is that of freedom and of confidence; the spirit of children, and not of slaves. By which we cry <em>Abba, Father</em> — expressing the fullest confidence of children to a parent.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "16": {
            "synthesis": "<p><em>The Spirit himself bears witness with our spirit that we are children of God.</em> Calvin notes the force of the compound Greek verb: the Spirit does not merely speak alongside our spirit but gives his own testimony so that when he is our witness, our minds are firmly persuaded of what he testifies. This is a distinct witness, not reducible to our own self-assessment. Ellicott describes the structure of the concurrent testimony: the self-consciousness of the believer assures him of sonship through his sense of the relationship; the Spirit then adds a distinct and separate attestation from outside the self, corroborating what the believer already dimly feels.</p><p>Clarke insists on the identity of the Spirit who witnesses: it is none other than the Holy Ghost himself, not a disposition or frame of mind. Wesley names this the clear and constant testimony of assurance — a witness distinct from the testimony of a good conscience, a witness <em>with</em> our spirit rather than <em>of</em> our spirit, which is itself a great thing.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He does not simply say that God's Spirit is a witness to our spirit, but he adopts a compound verb, which might be rendered <em>co-witness</em>. Paul means that the Spirit of God gives us such a testimony, that when he is our witness, our minds are firmly persuaded that what he testifies is beyond all controversy.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>What is the nature of this concurrent testimony? It would seem to be something of this kind. The self-consciousness of the believer assures him of his sonship. The relation in which he feels that he stands to God he knows to be that of a son. But, besides this, there is a further attestation from without, from the Spirit of God himself, corroborating that inner consciousness.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>The Spirit itself beareth witness with our spirit — that same Spirit, the Spirit of adoption; which can be no other than the Holy Ghost himself, and certainly cannot mean any disposition or affection of mind which the adopted person may have, for that would be the testimony of our spirit to itself, not the testimony of God's Spirit with ours.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>The same Spirit beareth witness with our spirit — with the spirit of every true believer, by a testimony distinct from that of his own spirit, or the testimony of a good conscience. Happy they who enjoy this clear and constant witness of God's Spirit with their own, that they are children of God.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "17": {
            "synthesis": "<p>If we are children, then we are heirs — heirs of God and fellow heirs with Christ, provided we suffer with him in order that we may also be glorified with him. Calvin connects the logic: inheritance is appointed for children; God has adopted us as his children; he has therefore ordained an inheritance for us. He then adds the significant qualification: sharing the inheritance means first sharing the path — the cross precedes the crown, and participation in suffering is the appointed route to participation in glory. Ellicott notes that one characteristic of the son is heirship, and the Christian shares an inheritance of glory with Christ — but must not be surprised to find that sharing the glory first means sharing the sufferings.</p><p>Wesley identifies <em>if we suffer with him</em> as a new proposition referring to what follows — it is the hinge between the comfort of sonship and the comfort derived from the certain glory that outweighs present suffering. Barnes notes that an adopted son comes into the inheritance as fully as a natural son — this is Paul's basis for the confidence that follows.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>By an argument taken from what is annexed he proves that our salvation consists in having God as our Father. It is for children that inheritance is appointed: since God then has adopted us as his children, he has at the same time ordained an inheritance for us. He then intimates what kind of inheritance this is — that it is a participation in the same glory which Christ has obtained.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>One characteristic of the son is that he is his father's heir. So it is with the Christian. He, too, has an inheritance — an inheritance of glory which he will share with Christ. But he must not be surprised if, before sharing the glory, he also shares the sufferings. <em>Suffer with him</em> — all who are partakers of Christ must share his sufferings as well as his glory.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>Joint heirs — that we may know it is a great inheritance which God will give us; for he hath given a great one to his Son. If we suffer with him — willingly and cheerfully, for righteousness' sake. This is a new proposition, referring to what follows — the great argument that present suffering is swallowed up in coming glory.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>And if children, then heirs — he will treat us as sons. An heir is one who succeeds to an estate. The meaning here is, that if we sustain the relation of sons to God, we shall be admitted to share his favours. An adopted son comes into the inheritance as fully as a natural son — and this is Paul's basis for the confidence that follows.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "18": {
            "synthesis": "<p><em>I consider that the sufferings of this present time are not worth comparing with the glory that is to be revealed to us.</em> Calvin notes the precise force of the word <em>reckon</em> — this is Paul's considered judgment after weighing the two sides, not merely an emotional assertion. The argument is one of proportion: when the glory is the full enjoyment of God himself, present sufferings, however real and intense, occupy a negligible position in the calculus. Clarke notes that compared with eternity, even the severest earthly trials are as for a moment.</p><p>Wesley notes that Paul's reckoning here anticipates the logic of vv.19-30: when that glory is revealed in us, then the sons of God will be revealed also, and all of creation will be affected by that revelation. Barnes identifies this as a new division of the subject, showing the power of the gospel in sustaining souls through trials — not by minimizing the trials but by the incomparably greater weight of the glory awaiting.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>Paul refers to his reckoning — his considered weighing of the two sides. The argument is one of proportion: the glory that shall be revealed is so immense that the sufferings of the present life, set against it, weigh nothing. He had before declared that we must be conformed to Christ; he now consoles us by the consideration of the incomparable excellence of what we are moving toward.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>If the glory that is to be revealed be the enjoyment of God himself, then the sufferings of this life, which, when compared with eternity, are but as for a moment, are not worthy to be put in competition with this glory. What we endure in time is finite and limited; what we shall enjoy in eternity is infinite and everlasting.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>For I reckon — this verse gives the reason why he but now mentioned sufferings and glory. When that glory <em>shall be revealed in us</em>, then the sons of God will be revealed also — and the whole creation affected by that revelation.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>For I reckon — I think; I judge. This verse commences a new division of the subject, continued to Romans 8:25. Its design is to show the power of the gospel in sustaining the soul in trials — not by minimizing them but by the incomparably greater weight of the glory awaiting. The sufferings of this present time — the persecutions, pains, and calamities to which Christians were then subject.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "19": {
            "synthesis": "<p>Creation itself waits with eager longing for the revealing of the sons of God. Calvin reads the creation's expectation as a pointer to the patient hope to which he has been exhorting believers — even mute creatures embody, in their own way, a sense of the present disordered state and a forward-looking orientation. Ellicott draws out the striking Greek word for <em>earnest expectation</em> (ἀποκαραδοκία) — a single evocative word meaning a state of intense, almost physical forward-straining, head thrust forward, toward a coming event. Paul attributes to creation a kind of eager consciousness of what lies ahead.</p><p>Wesley identifies the scope of the word <em>creation</em>: all visible creatures, believers excepted (who are spoken of separately), each according to its capacity. These have all been sufferers through sin, and all therefore look for the deliverance that will come through the glory of God's children. Barnes notes that this intense vocabulary suggests not mere passive waiting but a vivid, active anticipation.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He teaches us that there is an example of the patience to which he had exhorted us even in mute creatures. For there is no element and no part of the world which, being touched, as it were, with a sense of its present misery, does not intensely hope for a resurrection. He says that the creatures wait for the manifestation of the sons of God.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p><em>Earnest expectation</em> — a single word in the Greek, and a very striking one. The word denotes a state of earnest desire to see any object when the head is thrust forward; an intense, almost physical forward-straining toward a coming event. The whole creation is looking earnestly and intently for the same manifestation of glory as ourselves.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>For the earnest expectation — the word denotes a lively hope of something drawing near, and a vehement longing after it. Of the creation — of all visible creatures, believers excepted, who are spoken of apart; each kind, according as it is capable. All these have been sufferers through sin; and to all these, redemption will in some way extend.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p><em>Earnest expectation</em> — it properly denotes a state of earnest desire to see any object when the head is thrust forward; an intense anxiety; an ardent wish. It is thus applied to express the intense desire of the renewed mind to be delivered from sin and to obtain the full adoption as sons of God.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "20": {
            "synthesis": "<p>Creation was subjected to futility — to vanity, frustration, decay — <em>not willingly, but because of him who subjected it, in hope.</em> This verse has generated significant discussion about both the identity of the <em>creature</em> and the <em>him who subjected it.</em> Calvin and Wesley identify the one who subjected creation as God, acting at the fall (Genesis 3:17-19): the creation did not choose its subjection to corruption but was subjected by divine sentence — yet with a hope embedded in that sentence. Barnes takes a different path, reading <em>the creature</em> as the renewed Christian mind, which has been subjected to a state of suffering and imperfection not by its own choice but by God's wise purpose, with hope of full deliverance.</p><p>Ellicott reads the subjection as referring to the present imperfect state of nature and explains the hope: if creation were already perfect and fulfilling its noblest purpose, there would be no cause for forward-looking hope. Its present frustration is itself the ground of anticipation.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He shows the object of expectation from what is of an opposite character: as creatures, being now subject to corruption, cannot be restored until the sons of God shall be wholly restored; hence they, longing for their renewal, look forward to the manifestation of the celestial kingdom. He shows also that they groan in this their present condition, and he tells us that creation was subjected to vanity not by its own will, but through the appointment of God.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The Apostle gives the reason for this earnest expectation in the present state of nature; pointing out what creation <em>is</em>. If creation were perfect, and were fulfilling the noblest possible purpose, there would be no cause for looking forward hopefully to the future. Its very subjection to futility is the condition that makes hope possible and necessary.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>The creation was made subject to vanity — abuse, misery, and corruption. By him who subjected it — namely, God, Genesis 3:17; 5:29. Adam only made it liable to the sentence which God pronounced; yet not without hope — for God, at the very time he subjected it, promised a better state.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>The renewed creature — the Christian mind — is given as a reason for its aspiring to the full privileges of adoption: the present state is not one of choice, or one which is preferred, but one to which it has been subjected for wise reasons by God, with the sure promise that full deliverance will come.</p>"
                }
            ],
            "consensus": "divided",
            "key_tension": "Calvin and Wesley read 'the creature' as the created order subjugated by God at the fall (Gen 3:17); Barnes reads 'the creature' as the renewed Christian mind subjected to present imperfection by God's wise purpose; Ellicott reads it as natural creation whose present futility implies hope."
        },
        "21": {
            "synthesis": "<p>The hope embedded in creation's subjection is now declared: <em>creation itself will be set free from its bondage to corruption and obtain the freedom of the glory of the children of God.</em> Calvin notes the Isaianic background (Isaiah 65:17; 2 Peter 3) and insists that the dreadful extent of the curse — that even mute creatures groan under it — ought to awaken us to the gravity of what we deserved by sin, and the greatness of the redemption that reverses it. Ellicott takes the Greek conjunction (<em>ὅτι</em>) as meaning <em>that</em> rather than <em>because</em>, connecting v.21 closely to v.20: creation was subjected in hope <em>that</em> it also shall be delivered.</p><p>Wesley makes the sharp logical point: destruction is not deliverance — therefore, whatever is destroyed or ceases to be is not delivered at all. Creation's liberation is not annihilation but transformation into the glorious liberty that characterizes the children of God. Clarke notes that <em>φθορά</em> (corruption) often denotes sinful corruption, and the liberation is from that polluting power.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He shows how the creation has in hope been made subject to vanity — inasmuch as it shall sometime be made free, as Isaiah testifies and Peter confirms more clearly. It is then indeed meet for us to consider what a dreadful curse we have deserved, since all created things in themselves innocent are compelled to bear part of its punishment.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p><em>Because</em> — perhaps rather <em>that</em>, to be joined to the end of the last verse: <em>in hope that creation also shall be delivered.</em> The reason for the hope which survives through the degradation of nature: what creation <em>is to be</em>. Delivered from the bondage of corruption — freed from the enslaving power of decay and death.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>This and the preceding verse should be thus connected: <em>in hope that the creature itself also shall be delivered.</em> The word <em>corruption</em> denotes very frequently sinful corruption — and the liberation promised is from that enslaving power, not from mere physical decay alone.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>The creation itself shall be delivered — destruction is not deliverance: therefore whatsoever is destroyed, or ceases to be, is not delivered at all. Creation's liberation is transformation, not annihilation. Into the glorious liberty — the excellent state of freedom that will characterize the children of God.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "22": {
            "synthesis": "<p>The evidence for creation's hope is its present groaning: <em>the whole creation has been groaning together in the pains of childbirth until now.</em> Calvin reads this as confirmation and transition: creation's groaning is the evidence of its present subjection to corruption and simultaneously the sign that it reaches toward something beyond its current state. Ellicott notes the power of the childbirth image: groaning in labor is not the groaning of mere suffering but of purposeful pain moving toward a birth — the travail is instrumental, not terminal.</p><p>Wesley notes the phrase <em>together</em> (<em>συνστενάζει</em>): every member of creation groans with joint groans, as it were with one voice. Clarke observes that the verse describes a universal phenomenon that extends through all of history to the present moment — <em>until now</em> means the groaning has been uninterrupted and continues. Barnes takes the verse as an illustration of v.20-21 — the groaning of creation as a whole makes vivid what the renewed creature experiences.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He repeats the same sentiment, that he might pass over to us; for as creatures are subject to corruption not through their natural desire but through the appointment of God, and then as they have a hope of being hereafter freed from corruption, it would be unreasonable for us to refuse to bear the cross, and much more so to become weary on account of long waiting.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p><em>Groaneth and travaileth</em> — in view of the physical evil and misery prevalent in the world, the Apostle attributes a human consciousness of pain to creation. It groans and travails together, every member of it in common with its kind. The idea of travailing, as in childbirth, gives the note of purposefulness — pain moving toward a birth, not mere suffering without issue.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>For the whole creation groaneth together — with joint groans, as it were with one voice. And travaileth — literally, is in the pains of childbirth, to be delivered of the burden of the curse. Until now — to this very hour; and so on till the time of deliverance.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>The whole creation — intended as an illustration of what had just been said: the groaning of creation as a whole makes vivid what the renewed creature experiences. This expression of universal travail is a figure of the most sublime and impressive character, implying that all nature sympathizes with the fallen condition of man and awaits the great deliverance.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "23": {
            "synthesis": "<p>The groaning is not confined to the rest of creation — believers themselves groan inwardly, even though they have received the firstfruits of the Spirit. The possession of the Spirit is the down payment of the inheritance, and it is precisely the firstfruits that make believers feel most keenly the incompleteness of their present state. Calvin notes that Paul's point is not merely to exalt the dignity of future blessedness by showing that even those most advanced in grace still long for something beyond — it is to teach patience under the weight of present imperfection. Ellicott identifies what believers await: the time when adoption as sons of God will be complete, and even the mortal body will be transfigured.</p><p>Wesley connects <em>adoption</em> to its Roman form: privately adopted persons were brought into the public forum and there publicly owned as sons — the present state is private adoption, the resurrection is the public declaration. Barnes explains the firstfruits image: the Spirit now is a portion of the inheritance, the same in kind as what will be fully possessed — and the possession of the portion creates intense longing for the whole.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>The Apostle proves, by the groaning of the saints, that it becomes us patiently to sustain our present miseries — not because a hope of better things ought to be only a common one with us and brutes, but because the Spirit of God, who sees far more clearly what is wanting, stimulates us also by his groaning to seek a blessed resurrection.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Nor is it only the rest of creation that groans. We Christians, too, though we possess the firstfruits of the Spirit, nevertheless inwardly groan, sighing for the time when our adoption as the sons of God will be complete, and even our mortal bodies will be transfigured. The firstfruits make us feel the incompleteness most keenly.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>And even we, who have the first-fruits of the Spirit — that is, the Spirit, who is the first-fruits of our inheritance. The adoption — persons who had been privately adopted among the Romans were often brought forth into the forum, and there publicly owned as sons by those who adopted them. The resurrection answers to this public adoption.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>Which have the first-fruits of the Spirit — the portion that was first collected and consecrated to God as a pledge of the full harvest to come. The Spirit given to believers is of the same nature as the full inheritance to be possessed hereafter — the earnest, the pledge, the down payment — and creates intense longing for what remains.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "24": {
            "synthesis": "<p><em>For in this hope we were saved.</em> Hope is not incidental to salvation but constitutive of it — we were not saved into full possession but into certain expectation. Calvin draws out the nature of hope: since hope extends to things not yet obtained and represents to our minds the form of things hidden and far remote, whatever is either present to our view or already grasped cannot be an object of hope. Barnes refines this: most commentators have read this as meaning we have arrived at a condition in which we hope for future glory — salvation is already ours but not yet in full possession; we have its firstfruits and its certainty, but not yet its consummation. Ellicott captures the essential logic: hope in the future is of the very essence of the Christian life, and it was by hope that the Christian at his conversion made his salvation present to his mind, though it was still in the future.</p><p>Clarke underscores the sustaining function of hope: it supports and comforts in the troubles and adversities of present life, giving real present benefit from what is as yet only promised.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>Paul strengthens his exhortation by another argument: since our salvation cannot be separated from some kind of death, and this he proves by the nature of hope. Since hope extends to things not yet obtained, and represents to our minds the form of things hidden and far remote, whatever is either present to our view or already grasped in the hand cannot be an object of hope.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Why do I say that we <em>wait for the adoption</em>? Because hope in the future is of the very essence of the Christian's life. It was by hope that he was saved. Hope, at the time when he first believed, made him realise his salvation, though it is still in the future. This is, indeed, implied in the very nature of hope itself.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>For we are saved by hope — we are supported and comforted in the expectation we have of receiving from the hand of our God all the good we need in the troubles and adversities of this life, and of having our bodies raised from corruption and death at the general resurrection. Hope that is seen is not hope — for if you already possess the thing, you do not hope for it.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>It cannot be said that hope is the instrument or condition of salvation. Most commentators have understood this as meaning that we have as yet attained salvation only in hope — that we have arrived at a condition in which we hope for future glory; and that we are sustained and comforted by that hope in our present trials.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "25": {
            "synthesis": "<p>The second half of the antithesis follows: if we hope for what we do not see, we wait for it with patience. Calvin reads this as an argument from what the antecedent implies — patience necessarily follows hope, since one must sustain and comfort oneself against the weight of present absence, or faint through despair. The connection between hope and patience is not psychological accident but logical necessity. Ellicott frames the positive: since we do not yet see the salvation we hope for, we rightly and contentedly endure the sufferings that lie on the road to it — the patience is not resignation but the rational response to the certainty of what lies ahead.</p><p>Barnes draws from universal experience: where there is a strong desire for an object and a corresponding expectation of obtaining it — which together constitute true hope — we can wait for it patiently. Where there is strong desire without expectation, the result is restlessness and anguish, not patience.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>This is an argument derived from what the antecedent implies: patience necessarily follows hope. For when it is grievous to be without the good you may desire, unless you sustain and comfort yourselves with patience, you must necessarily faint through despair. Hope then ever draws patience with it; for hope ever sustains us, when we might otherwise sink under the burden of adversity.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>If salvation were something that could be seen, something that could be grasped by sight, there would be no room for hope. As it is we do not see it; we do hope for it; and, therefore, we patiently endure the sufferings that lie upon the road to it. The patience is not resigned passivity but the rational posture of those who know what lies ahead.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>But if we hope for that we see not — if we have a well-grounded expectation of our resurrection and final glorification, knowing that such things are necessarily future, and must for a certain time be delayed; then do we patiently wait for them, continuing to endure the common ills of this life with a mind sustained by the certainty of the promise.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>Where there is a strong desire for an object, and a corresponding expectation of obtaining it — which constitutes true hope — then we can wait for it with patience. Where there is a strong desire without a corresponding expectation, the mind becomes restless, impatient, and anguished. The certainty of the hope produces the patience.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "26": {
            "synthesis": "<p>While hope sustains from the human side, the Spirit sustains from the divine side, helping our weakness — especially our weakness in prayer. Calvin notes that believers cannot complain of weakness as a disqualification, since the Spirit's aid is abundantly sufficient to overcome all difficulties. The weakness in view is specifically the weakness of not knowing how to pray as we ought — we do not know what to ask for or how. Ellicott captures the double source of encouragement Paul is presenting: on one hand the human certainty of salvation, and on the other the divine Spirit's intercession — one source human, one divine, together fully sufficient.</p><p>Wesley broadens the application: our understandings are weak in the things of God, our desires are weak, our prayers are weak — and at these very points the Spirit takes hold with us, as a stronger person helping to carry what is too heavy for us alone. Clarke insists on the identity of the Spirit here — it is the same Spirit mentioned throughout the chapter, not a disposition of mind.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>That the faithful may not make this objection — that they are so weak as not to be able to bear so many and so heavy burdens — he brings before them the aid of the Spirit, which is abundantly sufficient to overcome all difficulties. There is then no reason for any one to complain, that the burden of hope is too great for them to sustain.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p><em>Likewise</em> — while on the one hand the prospect of salvation sustains him, so on the other hand the Divine Spirit interposes to aid him. The one source of encouragement is human — his own consciousness of the certainty of salvation — the other is divine. Together they make the Christian's position fully sufficient against all that presses upon him.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>The same Spirit mentioned before as bearing witness with ours that we are the children of God; and consequently it is not a disposition or frame of mind, for the disposition of our mind surely cannot help the infirmities of our minds. The Spirit makes intercession <em>for</em> us and <em>with</em> us and <em>in</em> us.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>Likewise the Spirit — nay, not only the universe, not only the children of God, but the Spirit of God also himself, as it were, groaneth, while he helpeth our infirmities, or weaknesses. Our understandings are weak, particularly in the things of God; our desires are weak; our prayers are weak. We know not what to pray for as we ought.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "27": {
            "synthesis": "<p>God who searches the hearts knows what is the mind of the Spirit, because the Spirit intercedes for the saints according to God's will. Calvin identifies this as a remarkable ground for confidence in prayer: when we pray through the Spirit, our prayers are heard by God because he thoroughly knows the desires of his own Spirit even when we cannot articulate them. The inarticulate groanings the Spirit stirs in us are fully transparent to God, who reads them not as incoherent noise but as exact conformity to his will. Ellicott puts it precisely: God recognizes the voice of his own Spirit because the prayers the Spirit prompts are in strict accordance with the divine will.</p><p>Wesley notes the particular comfort this provides: God's searching of the heart reaches not just our explicit prayers but the unutterable movements the Spirit prompts below the level of articulation. Barnes emphasizes that God does not need full verbal articulation — he knows the desires the Spirit excites, and he does not need the deep groaning to be translated into words.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>This is a remarkable reason for strengthening our confidence: that we are heard by God when we pray through his Spirit, for he thoroughly knows our desires, even as the thoughts of his own Spirit. He regards not the exterior form of words, but looks at the desires of the heart — and those desires, stirred by the Spirit, are always fully known to him.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>God recognises the voice of His own Spirit, because the prayers that the Spirit prompts are in strict accordance with His will. <em>What is the mind of the Spirit</em> — what are the thoughts of the Spirit, and therefore what is the echo of those thoughts in the prayers that are offered to Him. The accord between what the Spirit prompts and what God wills is perfect.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>But he who searcheth the hearts — wherein the Spirit dwells and intercedes — knoweth, though man cannot utter it, what is the mind of the Spirit; for he maketh intercession for the saints according to God — according to his will, as is worthy of God, and acceptable to him.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>And he that searcheth the hearts — God. To search the heart is one of his attributes which cannot be communicated to a creature. Knoweth what is the mind of the Spirit — knows the desires which the Holy Spirit excites and produces in the heart. He does not need that those deep, inarticulate longings be translated into words.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "28": {
            "synthesis": "<p><em>And we know that for those who love God all things work together for good, for those who are called according to his purpose.</em> Calvin draws the conclusion from everything preceding: so far are the troubles of this life from hindering salvation that, on the contrary, they are helps to it. The consolation is not that bad things are secretly good but that all things — including genuine evils — are under God's sovereign direction toward the good of his people. Ellicott notes a significant textual variant in the best manuscripts (Vatican and Alexandrian, plus Origen), which insert <em>God</em> as the explicit subject: <em>God works all things together</em> with believers for good, rather than <em>all things work together.</em></p><p>Wesley anchors the comfort in the character of God: all things — ease or pain, poverty or riches, and the ten thousand changes of life — work strongly and sweetly for spiritual and eternal good, for those who love God and are called according to his purpose. Barnes identifies this as yet another source of consolation: all things are under the direction of an infinitely wise Being who has purposed their salvation.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He now draws this conclusion from what had been said — that so far are the troubles of this life from hindering our salvation, that, on the contrary, they are helps to it. Those who love God shall find all things to minister to their salvation: not because they deserve it, but because God, who calls them, will make even adversity serve them.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p><em>All things</em> — persecution and suffering included. <em>Work together</em> — contribute. There is a rather remarkable reading in the Vatican and Alexandrian MSS., and in Origen, inserting <em>God</em> as the subject of the verb, and making <em>all things</em> the object: <em>God works all things together with</em> those who love him for good.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>And we know — this in general; though we do not always know particularly what to pray for. That all things — ease or pain, poverty or riches, and the ten thousand changes of life — work together for good — strongly and sweetly, for spiritual and eternal good — to them that are called according to his purpose.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>This verse introduces another source of consolation and support, drawn from the fact that all things are under the direction of an infinitely wise Being who has purposed the salvation of the Christian, and who has so appointed all things that they shall contribute to it. This is a most comforting declaration — that nothing happens to the Christian by chance.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "29": {
            "synthesis": "<p><em>For those whom he foreknew he also predestined to be conformed to the image of his Son.</em> The word <em>foreknew</em> (<em>προέγνω</em>) has generated one of the great exegetical debates of the epistle. Calvin reads this as the beginning of the <em>order of election</em>: by the very order of God's sovereign choice, afflictions are the appointed path of conformity to Christ's image, and that conformity was purposed before creation. Election is unconditional — God's foreknowledge is his sovereign fore-appointment, not his foresight of human response.</p><p>Wesley offers a markedly different reading: those foreknown are those foreknown to be conformable to the image of the Son — this is the mark of those who are foreknown and will be glorified. On this reading, foreknowledge is conditional, based on foreseen faith and conformity. Barnes takes a measured exegetical position, noting that the Hebrew sense of <em>know</em> often includes election or setting apart, and that the apostle's argument is about the certainty of final salvation for those who are called, whatever the mechanism of foreknowledge.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He then shows, by the very order of election, that the afflictions of the faithful are nothing else than the manner by which they are conformed to the image of Christ. He is not speaking of foreknowledge as mere prescience but as God's sovereign purpose — from before creation, God determined that those he chose would be conformed to his Son, and this conformity is worked out through present suffering.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>For whom he did foreknow — in this and the following verse the apostle shows how our calling is an argument that all things work together to advance our eternal happiness, by showing the several steps which the wisdom and goodness of God have settled in order to complete our salvation: foreknowledge, predestination, calling, justification, glorification.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>Whom he foreknew, he also predestinated conformable to the image of his Son — here the apostle declares who those are whom he foreknew and predestinated to glory; namely, those who are conformable to the image of his Son. This is the mark of those who are foreknown and will be glorified.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>For whom he did foreknow — the word denotes, properly, to know beforehand; but it has the Hebrew sense of <em>to know</em> as implying selection and setting apart. The design of the passage is to show the certainty of the salvation of those who love God, from the purpose which he had formed from the beginning to save them.</p>"
                }
            ],
            "consensus": "divided",
            "key_tension": "Calvin reads 'whom he foreknew' as God's sovereign fore-appointment (unconditional election); Wesley reads it as foreknowledge of those who would be conformable to Christ's image (conditional on foreseen faith and response); Barnes takes a measured position on the Hebrew sense of 'know' as including election."
        },
        "30": {
            "synthesis": "<p>The golden chain of salvation: <em>those he predestined he also called; those he called he also justified; those he justified he also glorified.</em> Calvin identifies the graduated structure — predestination, calling, justification, glorification — as a chain in which each link is inseparable from the rest. The argument provides complete assurance: no one falls out between these steps, since the one who predestined is the same who calls, justifies, and glorifies. Ellicott engages the specific theological weight of <em>predestinate</em>: it is this term that most directly engages questions of free will, but foreknowledge does not interfere with free will since it is posterior in the order of causation, whatever it is in order of time.</p><p>Wesley notes the pastoral force of the past tense <em>glorified</em>: Paul uses the past tense for a future event because from God's perspective it is as certain as done. Those called and justified are as certainly glorified as if they were already there. Barnes focuses on the structural argument: predestination, properly understood, implies the certainty of the whole chain — none fall out between calling and glorification.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>That he might now by a clearer proof show how true it is that a conformity with the humiliating state of Christ is for our good, he adopts a graduating process, by which he teaches us, that a participation of the cross is so connected with our vocation, justification, and finally glorification, that these cannot be separated from one another.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p><em>Predestinate</em> — this is the term which seems most to interfere with human free-will. Foreknowledge does not interfere with free-will, because the foreknowledge, though prior in point of time, is posterior in the order of causation to the act of choice. The chain here is presented as unbreakable: the same God who predestinated also called, justified, and will glorify.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>Them he — in due time — called — by his gospel and his Spirit. And whom he called, when obedient to the heavenly calling, he also justified. And whom he justified, he in the end glorified. St. Paul does not affirm that all whom God called were justified, or all who were justified were glorified — but only that this is the method of God's proceeding with those who follow his call.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>In this verse, in order to show the true consolation to be derived from the fact of predestination, the apostle states the connexion between that predestination and certain salvation. The one implied the other. The chain is complete — predestination leads to calling, calling to justification, justification to glorification — and none who enter the chain fall out of it.</p>"
                }
            ],
            "consensus": "mixed",
            "key_tension": "Wesley reads the chain as describing God's method with those who respond to his call, leaving room for human response at each step; Calvin and Barnes read it as an unbreakable sequence guaranteeing final salvation for all who are predestined."
        },
        "31": {
            "synthesis": "<p><em>What then shall we say to these things? If God is for us, who can be against us?</em> With the doctrine of vv.29-30 established, Paul breaks into triumphant questions. Calvin notes that he has sufficiently proved his doctrine and now bursts into exclamation, teaching that with the paternal favor of God is connected the certain victory against all adversaries. The logic is simple and irresistible: the opposition of every creature is nothing against God's purpose and love. Clarke identifies the primary reference of <em>these things</em> as the doctrines of vv.28-30 particularly, but also the whole preceding argument from v.1 about life in the Spirit and the certainty of the inheritance.</p><p>Wesley identifies the rhetorical structure: four rhetorical periods follow, each beginning with a glorying in God's grace and then showing how no opposition can overcome it. Barnes draws out the practical force: if God — who is omnipotent, omniscient, and who has purposed our salvation — is for us, who can successfully stand against us? Not that none will try, but that none can prevail.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>The subject discussed having been sufficiently proved, he now breaks out into exclamations, by which he sets forth the magnanimity with which the faithful ought to be furnished when adversities urge them to despond. He teaches us in these words that with the paternal favor of God is connected the certain victory against all adversaries.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>What shall we then say to these things? — what conclusion should we draw from the above premises? From all that was laid down in the preceding chapters, but especially from Romans 8:28-30. What comfort may we derive from these doctrines? If God be for us — as he most assuredly is, by the mission of his Son and Spirit — who can be against us with any prospect of success?</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>What shall we say then to these things — related in the third, fifth, and eighth chapters? As if he had said: We cannot go, think, or wish anything farther. If God be for us — here follow four periods, one general and three particular. Each begins with glorying in the grace of God, which is followed by a question defying all opposition.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>What fairly follows from the facts stated? or what conclusion shall we draw in regard to the power of the Christian religion to support us in our trials? If God — if the omnipotent Ruler of the universe — be for us, who can be against us, with any hope of success? He who is on our side is greater than all that can oppose us.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "32": {
            "synthesis": "<p>The evidence that God is for us: <em>he who did not spare his own Son but gave him up for us all — how will he not also with him graciously give us all things?</em> Calvin identifies this as the price of our redemption brought forward to prove God's love — and the argument from the greater to the lesser is irrefutable. If God gave what cost him most (his own Son, not a servant, not a creature, but his own), he will certainly give what costs him less. Clarke makes the application vivid: can we doubt his protection who loved us so intensely as to deliver his own Son to death for us all?</p><p>Wesley names the content of <em>all things</em>: all things needful or profitable for our souls, from justification forward. Barnes draws out the Abrahamic allusion in <em>he spared not</em> — God who withheld not his own Son (as Abraham did not withhold Isaac, Genesis 22:16) has given the supreme pledge that nothing needed for salvation will be withheld.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>Paul brings forward the price of our redemption in order to prove that God favors us. Doubtless it is a remarkable and clear evidence of inappreciable love, that God, in order to redeem us, spared not even his own Son. From the greater he argues to the less — he who gave what cost most will certainly give what costs less.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>He that spared not his own Son — and can we, his sincere followers, doubt of the safety of our state, or the certainty of his protection? No: for if he loved us, Gentiles and Jews, so intensely as to deliver up to death his own Son for us all, can he withhold from us any minor blessing? Shall he, who gave the greater gift, refuse the lesser?</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>He that spared not his own Son — therefore he will freely give us all things. He delivered him up for us all — therefore, none can lay anything to our charge. <em>Freely</em> — for all that follows justification is a free gift also. <em>All things</em> — needful or profitable for our souls, from justification to final glorification.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>He that spared not his own Son — who did not retain, or keep from suffering and death. The expression <em>spared not</em> carries the allusion to Genesis 22:16, where God commended Abraham because he had not withheld his son. He who gave the supreme pledge will not withhold lesser gifts; he who delivered up his Son will also freely give all things needful for salvation.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "33": {
            "synthesis": "<p><em>Who shall bring any charge against God's elect? It is God who justifies.</em> The question is asked from the perspective of a law court: who shall formally accuse, and to what effect? Calvin identifies the first and chief consolation of the godly in adversities as the certainty of God's paternal kindness — and here its judicial ground is named: God has justified, and his verdict overrides every possible accusation. If the Judge has declared the defendant righteous, no subsequent accuser can overturn the verdict. Clarke lays out the questions in the form in which the best Greek texts present them, with God's acts — justifying, condemning? no, dying — given as the definitive answers that silence each charge.</p><p>Wesley identifies <em>God's elect</em> with the background in prophetic tradition — those whom God has chosen, long before the term was restricted to Israel. Barnes underlines that the office of final judgment belongs to Christ, and the apostle is about to show that Christ, far from condemning, is the one who died and rose and intercedes for them.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>The first and the chief consolation of the godly in adversities, is to be fully persuaded of the paternal kindness of God; for hence arises the certainty of their salvation, and that calm quietness of the soul through which it comes that adversities are sweetened. No accuser can prevail when the Judge himself has acquitted — and God who justifies has spoken the final word.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>This and the two following verses contain a string of questions, most appropriately introduced and powerfully urged, tending to show the safety of the state of those who have believed the Gospel. The divine answers to each challenge — God justifies; Christ died; Christ rose; Christ intercedes — leave no room for any accusation to stand.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>God's elect — the above-cited author observes, that long before the coming of Christ the heathen world had revolted and were reprobated, or rejected. But those who believe the gospel are chosen, styled <em>the children or sons of God</em>. Who shall lay any charge against them, when God himself justifies?</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>Who shall lay any thing to the charge? — this expression is taken from courts of law and means, who shall accuse, or condemn, or so charge with crime before the tribunal of God as to cause their condemnation? God's elect — his chosen people. <em>It is God that justifieth</em> — the very Being to whom the appeal must be made has already pronounced the verdict of acquittal.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "34": {
            "synthesis": "<p><em>Who is to condemn? Christ Jesus is the one who died — more than that, who was raised — who is at the right hand of God, who indeed is interceding for us.</em> Calvin notes the comprehensive argument: Christ suffered the punishment due to us, thereby declaring that he undertook our cause; he rose, proving his victory over death; he sits at the right hand, holding universal power; and he intercedes, applying that victory to us continually. No condemnation is possible because the one to whom judgment belongs is the very one who died for us and now advocates for us. Ellicott connects this verse closely to v.35: the questions in these two verses form a unified reply — Christ who died, rose, and intercedes is the one from whose love Paul then asks who can separate us.</p><p>Wesley urges faith to rest not only on Christ's death but to be exercised further on his resurrection, exaltation, and second coming — the full arc of his saving work.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>As no one by accusing can prevail when the judge absolves; so there remains no condemnation when satisfaction is given to the laws and the penalty is already paid. Now Christ is he who, having once for all suffered the punishment due to us, thereby declared that he undertook our cause; he rose to proclaim his victory; he sits at the right hand with universal power; and he continually intercedes.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The remainder of this verse is to be closely connected with the opening of the next. <em>He that died, rose, &amp;c., is Christ: who then shall separate us from His love?</em> The two questions — <em>Who is he that condemneth?</em> and <em>Who shall separate us?</em> — are really parts of the reply to the single challenge of v.33.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>Yea rather, that is risen — our faith should not stop at his death, but be exercised farther on his resurrection, kingdom, second coming. Who maketh intercession for us — presenting there his obedience, his sufferings, his prayers, and our prayers sanctified through him.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>Who is he that condemneth? — who shall pass sentence of condemnation, and consign to perdition? The office of passing sentence of condemnation on men shall pertain to Christ, the Judge of quick and dead, and the apostle proceeds to say that it was certain he would not condemn the elect — for he died for them, rose for them, and ever lives to intercede for them.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "35": {
            "synthesis": "<p><em>Who shall separate us from the love of Christ?</em> And the catalog follows: tribulation, distress, persecution, famine, nakedness, danger, sword. Calvin notes that these usual harassers of believers lead some to interpret adversity as a token of divine abandonment — Paul's whole argument is that the conviction of God's love enables the saint to stand firm against this misinterpretation. Clarke raises an important exegetical question: is this Christ's love toward us or our love toward Christ? He inclines toward the latter, reading the verse as about the persecutions that test and might break believers' attachment to Christ — to which the answer is that genuine love does not break under persecution. Ellicott reads it as Christ's love toward us, and Barnes agrees, noting that the love in view is the love which Christ has for his people — persecutions cannot cause Christ to cease loving his own.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>The conviction of safety is now more widely extended, even to lower things; for he who is persuaded of God's kindness towards him is able to stand firm in the heaviest afflictions. These usually harass men in no small degree, because they interpret them as tokens of God's wrath. Paul answers that none of these things can sever the bond of love between Christ and his people.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p><em>The love of Christ</em> — that is to say, the love which Christ has for us, not that which we have for Christ. Shall tribulation? — the Apostle is speaking from his own actual experience. The enumeration covers the whole range of external pressure that life can bring.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>Who shall separate us from the love of Christ? — the apostle is referring to the persecutions and tribulations to which genuine Christians were exposed through their attachment to Christ, and the gracious provision God had made to preserve them in all these trials. The challenge is whether any external force can break the bond of love between the believer and his Lord.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>Who shall separate us — finally or entirely separate us? From the love of Christ — the love which Christ has for us. The argument is, that he who has shown such love will not withdraw it; that he who loved us so as to die for us will not cease to love his people in the midst of their trials and persecutions.</p>"
                }
            ],
            "consensus": "mixed",
            "key_tension": "Ellicott and Barnes read 'the love of Christ' as Christ's love toward us (objective genitive); Clarke reads it as our love toward Christ (subjective genitive), understanding the verse as asking whether persecution can break our attachment to him."
        },
        "36": {
            "synthesis": "<p>Paul supports the list of trials with a quotation from Psalm 44:22: <em>For your sake we are being killed all the day long; we are regarded as sheep to be slaughtered.</em> Calvin notes the double weight this citation adds: first, that the dread of death is far from a reason for falling away, since it has been almost ever the lot of God's servants to have death before their eyes; second, that what Paul's readers experience is nothing new — the pattern of suffering for God's sake runs through all of Scripture. Ellicott adds historical context: Psalm 44 was written at some period of great national distress, likely not earlier than Josiah, and represents the sufferings of God's people at all times as typical of the Christian experience.</p><p>Wesley underlines the constancy implied in <em>all the day</em>: every day, continually — not occasional persecution but sustained pressure. Barnes notes that Paul quotes not as if this passage originally predicted Christian suffering, but as aptly descriptive of the same condition the psalmist knew.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>This testimony adds no small weight to the subject; for he intimates, that the dread of death is so far from being a reason to us for falling away, that it has been almost ever the lot of God's servants to have death as it were present before their eyes. The same lot has belonged to the servants of God through every age.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The quotation is taken from Psalm 44:22, which was apparently written at some period of great national distress. The sufferings of God's people at all times are typical — they exemplify the same condition. The Apostle uses the psalm not as a specific prophecy of Christian martyrdom, but as the perennial description of what it costs to belong to God in a hostile world.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>All the day — that is, every day, continually. We are accounted — by our enemies; by ourselves — as sheep for the slaughter. The quotation shows that the pattern of suffering for God's sake is not new — it has characterized his people in every age.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>This passage the apostle quotes not as having originally reference to Christians, but as aptly descriptive of their condition. The condition of saints in the time of the psalmist was similar to that of Christians in the time of Paul. The same language would exactly describe the condition of both — in both cases, death for God's sake was the daily reality.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "37": {
            "synthesis": "<p><em>No, in all these things we are more than conquerors through him who loved us.</em> Calvin traces the force of the Greek compound (<em>ὑπερνικῶμεν</em>): <em>we do more than overcome; we most fully overcome; we emerge victorious and remain victorious.</em> The adversities do not merely fail to defeat believers — they are themselves transformed into instruments of victory. Calvin emphasizes the means: not through our own strength or fortitude, but <em>through him who loved us</em> — the love of Christ is not only the motive but the power of the victory. Ellicott puts it sharply: so far from being vanquished, we are conquerors; when we are weak then are we strong.</p><p>Wesley names what the more-than-conquering means practically: the believer is not only no loser but an abundant gainer by all these trials — they serve spiritual ends that make the final result richer than if they had never come. Clarke connects this to Paul's citations from the same psalm (v.36): the same sufferers who are as sheep for the slaughter emerge as more than conquerors through Christ's love.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>We always struggle and emerge — we do more than overcome; we emerge and remain victors. I have retained the word Paul uses, <em>supervincimus</em>. We do not merely survive, we triumph; and not through our own fortitude, but through him who loved us — the source of victory is Christ's own love for us.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p><em>Nay</em> — yet, or but. So far from being vanquished, we are conquerors: when we are weak then are we strong. The adversities themselves are transformed into instruments of victory by the power of him who loved us.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>We more than conquer — we are not only no losers, but abundant gainers, by all these trials. This period seems to describe the full assurance of hope. The love of Christ — the love he has shown — is both the ground and the power of the victory.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>Nay, but notwithstanding our severe pressures and trials. In all these things — in the very midst of them; while we are enduring them, we are able to triumph. We are more than conquerors — we gain the victory. They have not power to subdue us; to alienate our affections from Christ; or to impair our confidence in God.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "38": {
            "synthesis": "<p>Paul expands the catalog of what cannot separate into a comprehensive sweep of all possible reality: death and life, angels and rulers, things present and things to come, powers, height and depth. Calvin notes that Paul is now carried into hyperbolic expressions precisely to confirm believers more fully — what seems capable of tearing us from God cannot in fact do so. The list ranges across every metaphysical category: temporal states (death, life), spiritual powers (angels, rulers), temporal positions (things present, things to come), spatial dimensions (height, depth). Ellicott reads the enumeration as poetic rather than strictly logical, intended to include every possible category of being, especially the unseen powers of evil against which Christian warfare was directed.</p><p>Wesley maps the structural logic: <em>neither death</em> can hurt us — for Christ is dead; <em>nor life</em> — for he is risen; <em>nor angels nor principalities nor powers</em> — for he is at the right hand of God; <em>nor things present nor things to come</em> — for he makes intercession. Barnes emphasizes the language of personal certainty: <em>I am persuaded</em> — not merely a tentative hope but an unwavering confidence bordering on certainty.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He is now carried away into hyperbolic expressions, that he might confirm us more fully. Whatever, he says, there is in life or in death which seems capable of tearing us away from God, shall effect nothing; nay, the very angels, were they to attempt it, would not prevail. So extensive is his assertion, that he includes all things within heaven and earth.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The enumeration that follows is intended to include — poetically rather than logically — every possible category of being, especially those unseen powers of evil against which the warfare of the Christian was more particularly directed. <em>Nor principalities</em> — the spiritual powers arrayed against believers, whatever their order or authority.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "Wesley's Notes",
                    "html": "<p>I am persuaded — this is inferred from the thirty-fourth verse in admirable order: <em>neither death</em> shall hurt us, for Christ is dead; <em>nor life</em>, for he is risen; <em>nor angels nor principalities nor powers, nor things present nor things to come</em>, for he is at the right hand of God; <em>nor height nor depth</em>, for he maketh intercession.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>For I am persuaded — I have a strong and unwavering confidence. The expression here implies unwavering certainty. Neither death — neither the fear of death, nor all the pains and tortures of the dying scene, even in the most painful trials of persecution; death in all its forms cannot separate from Christ's love.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "39": {
            "synthesis": "<p>The catalog closes: <em>nor height nor depth, nor anything else in all creation, will be able to separate us from the love of God in Christ Jesus our Lord.</em> Calvin notes the final grounding: the love spoken of is the love of God <em>in Christ Jesus</em> — Christ is the bond of this love, the beloved Son in whom the Father is well pleased, and through whom we are united to God. If we are united to God through him, we may be assured of the immutable and unfailing kindness of God toward us. Ellicott observes that Paul now substitutes the fuller phrase <em>love of God</em> for the shorter <em>love of Christ</em> used earlier, suggesting that the love of Christ and the love of God are ultimately one and the same reality. Clarke reads <em>nor any other creature</em> (or thing) as a final catch-all: every conceivable power or circumstance is included in the sweep of what cannot separate. The chapter closes where it opened — with an absolute declaration of security in Christ — but now the ground has been laid in full: no condemnation, life in the Spirit, the certainty of the inheritance, the Spirit's intercession, the golden chain of salvation, and the love of God that nothing can overcome.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>That is, of which Christ is the bond; for he is the beloved Son, in whom the Father is well pleased. If, then, we are through him united to God, we may be assured of the immutable and unfailing kindness of God towards us. He now speaks more distinctly than before, declaring that the love of God is in Christ Jesus our Lord — not apart from him, but only through the bond of union with him.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p><em>Nor height, nor depth</em> — no remoteness in space. <em>Any other creature</em> — any other created thing. <em>The love of God</em> — it is to be observed that for the shorter phrase, <em>the love of Christ</em>, the Apostle now substitutes the fuller but equivalent phrase, suggesting that the love of Christ and the love of God are ultimately one reality.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Clarke's Commentary",
                    "html": "<p>Nor height of honor, nor depth of ignominy, nor any other creature — nor any other thing whatever — shall be able to separate us, who love God, from the love of God, which he has vouchsafed to us in Christ Jesus. The sweep is total: every conceivable power, circumstance, or created thing is excluded from the power of separation.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>Nor height — I regard it here as synonymous with prosperity, honour, elevation in this life. <em>Any other creature</em> — anything else that God has made; anything in the universe. None of these things shall be able to separate us from the love of God in Christ Jesus our Lord — a triumphant conclusion to the most sustained argument in the epistle for the security and blessedness of those who are in Christ.</p>"
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
    print('Romans 8 synthesis complete.')

if __name__ == '__main__':
    main()
