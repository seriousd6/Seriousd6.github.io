"""
Wide Source Synthesis — Hebrews chapter 10
bookId: hebrews
Run: python3 scripts/ws-synthesis-hebrews-10.py

Sources used: calvin, ellicott, clarke, wesley, barnes
(mhcc not available for Hebrews; jfb ch 10 data is mislabeled 2 Corinthians content — not used)

Chapter range: 10 (39 verses)

Key synthesis decisions:
- vv.26-31: All sources read the "willful sin" passage as apostasy from Christ, not ordinary sin;
  the question of whether true believers can so fall divides Calvin and Wesley — noted at v.38.
- v.5 "A body hast thou prepared for me": LXX differs from MT ("ears you have dug"); all sources
  note and accept the LXX reading; consensus = affirm.
- Calvin's entry at key 15 is section-level, covering the argument of vv.15-18; used selectively.
- Ellicott has no key 20; v.20 synthesis draws on Calvin, Clarke, Wesley, Barnes.
- Wesley's key 16 is only a cross-reference ("Jer 31:33, &c") — too brief to use as a voice.
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

HEBREWS = {
    "10": {
        "1": {
            "synthesis": "<p>Hebrews 10 opens by establishing the epistle's sharpest architectural contrast: the law occupies the position of a shadow (<em>skia</em>), while the gospel possesses the image (<em>eikon</em>) — the solid, faithful representation of heavenly realities. Calvin draws the analogy from pictorial art: a shadow is cast by the real thing but does not contain its substance, while an image reproduces its subject. The distinction is more precise than we might expect, and Ellicott notes that the antithesis surprises — we might have anticipated \"shadow vs. reality\" — but the writer deliberately chooses \"image\" to mark the gospel as a true and faithful copy of what is eternal. Wesley states the point plainly: the Mosaic dispensation is \"a bare, unsubstantial shadow of good things to come,\" not the solid form of those blessings. The immediate proof of the law's shadowy character is its repetitiveness. Barnes observes that the annual repetition of the same sacrifices is itself the decisive evidence of their incapacity: what truly cleanses does not require repetition. No accumulation of shadows produces a solid object. Clarke marks this verse as the thesis of the chapter's opening argument (vv.1-4): the legal sacrifices were insufficient precisely because they were repeated, and their repetition was inescapable because they were only ever shadows of the one perfect offering to come.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He has borrowed this similitude from the pictorial art; for a shadow here is in a different sense from what it has in Colossians 2:17, where the ancient rites are called shadows because they did not possess the real substance of what they represented. Here shadow is contrasted with image — a rough outline contrasted with a finished picture.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>\"A Shadow of good things to come\" — these words have already come before us. \"Not the very image\" — the antithesis is hardly what we should have expected. The idea of repetition has been very strikingly brought out: the same sacrifices, offered year by year continually, can never make the comers thereunto perfect.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>The law, the Mosaic dispensation, being a bare, unsubstantial shadow of good things to come — of the gospel blessings — and not the substantial, solid image of them, can never with the same kind of sacrifices, though continually repeated, make the comers thereunto perfect.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>The very fact that the sacrifices were repeated showed that there was some deficiency in them as to the matter of cleansing the soul from sin. If they had answered all the purpose of a sacrifice for sin, they would have been offered but once, and the whole Jewish system would have ceased.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "2": {
            "synthesis": "<p>The argument moves swiftly from assertion to proof. If the Levitical sacrifices had genuinely accomplished their purpose — if those who offered them had been truly and permanently cleansed — the sacrifices would have stopped. Their very continuation is a self-indictment. Ellicott sharpens the translation: \"otherwise\" rather than \"for then,\" capturing the logical force of the argument. The repetition was not incidental but symptomatic: it testified that the worshippers remained conscious of sin year after year. Wesley presses the point into the inner life: those who had been \"once perfectly purged\" would have been \"no longer conscious either of the guilt or power of their sins.\" Barnes draws out the structural logic — the annual renewal itself declared that the sacrifices had not in prior years achieved their end. Clarke adds that the divine design was that Israel would understand this: the Levitical system was not meant to be mistaken for a full atonement. Its perpetual renewal was a divinely intended signal that the ultimate sacrifice was still to come.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Better, <em>otherwise.</em> The very repetition of the annual ceremonial was a testimony to its imperfection. \"Once purged\" — because the worshippers, having been once cleansed, would have had no longer any consciousness of sins. The worshippers' continuing consciousness of guilt proved the sacrifice's inadequacy.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>They who had been once perfectly purged would have been no longer conscious either of the guilt or power of their sins.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>Had they made an effectual reconciliation for the sins of the world, and contained in their once offering a plenitude of permanent merit, they would have ceased to be offered — at least in reference to those whose sins had been once atoned for. God intended that they should understand the matter so.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>The very fact that they were repeated showed that there was some deficiency in them as to the matter of cleansing the soul from sin. The annual renewal declared that the same deficiency remained as before; the prior year's sacrifice had accomplished nothing final.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "3": {
            "synthesis": "<p>In place of permanent cleansing, the annual sacrifices produced something quite different: a yearly remembrance of sins. Far from wiping the slate clean, the Day of Atonement was formally constituted as a public acknowledgment that the slate remained written upon. Ellicott supplies the specific liturgical detail — in each of the three great prayers of the high priest on that day, he made explicit confession: \"I have sinned, I and my house.\" The ceremony did not pretend to accomplish what it could not; it was designed as a reminder, not a resolution. Calvin distinguishes this from the daily remembrance that the gospel rightly requires: Christian memory of sin serves gratitude and humility, but the Levitical remembrance served to mark out guilt awaiting removal. Wesley underlines the structural implication: the annual acknowledgment was \"a clear proof that the guilt thereof is not perfectly purged away.\" Barnes notes that the very repetition of the confession — once a year, every year — was built into the design of the system as testimony to its own provisional character.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>Though the Gospel is a message of reconciliation with God, yet it is necessary that we should daily remember our sins; but what the Apostle means is, that sins were brought to remembrance in those sacrifices that guilt might be marked out and awaiting removal — not that guilt was removed by the sacrifice then offered.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Better, <em>a remembrance of sins is made year by year.</em> In each of the three prayers of the high priest — for himself and his house, for the priesthood, for the people — he made special acknowledgment of sin: \"I have sinned, I and my house.\" The ceremony was constituted as yearly confession, not yearly absolution.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>There is a public commemoration of the sins both of the last and of all the preceding years; a clear proof that the guilt thereof is not perfectly purged away.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>The reference is to the sacrifices made on the great day of atonement. As often as a sacrifice was offered, it was an acknowledgment of guilt on the part of those who offered it. The annual recurrence of the acknowledgment showed that the prior year's sacrifice had accomplished nothing final.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "4": {
            "synthesis": "<p>The writer now states as a simple axiom what the whole preceding argument has been approaching: it is impossible that the blood of bulls and of goats should take away sins. The impossibility is metaphysical, not merely practical — it is not that animal blood is quantitatively insufficient but that it belongs to an entirely different order of being from the moral guilt it would have to address. Calvin had urged this in the previous chapter and restates it here: the blood of beasts cannot cleanse souls from sin; the Jews had in the sacrifices only a symbol and pledge of the real cleansing, looking forward to another. Ellicott notes that no inconsistency belonged to the ceremonial despite its inability — the offering was necessary, it answered its purpose as a type, but it could not remove the thing it pointed toward. Wesley is characteristically blunt: the blood of goats cannot take away sin, \"either the guilt or the power of them.\" Clarke adds that common sense, rightly operating, would have taught this — and God intended Israel to understand it so, that the system not be mistaken for the thing itself. Barnes presses the theological point: Paul means the blood of animals cannot effect moral pardon, a function belonging to an entirely different category.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He confirms the former sentiment with the same reason he had adduced before, that the blood of beasts could not cleanse souls from sin. The Jews, indeed, had in this a symbol and a pledge of the real cleansing; but it was with reference to another — the sacrifice that was still to come.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>No inconsistency really belonged to these sacrifices and this ceremonial, though so often repeated; for it was impossible that any such sacrifice should really remove sin. The offering was necessary, and it answered its purpose as a type and pledge; but it could not remove the guilt it symbolically addressed.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>It is impossible the blood of goats should take away sins — either the guilt or the power of them.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>Paul here means to say that the blood of animals cannot effect the moral purpose of pardon. It is not that the sacrifice was inadequate in quantity, but that it belongs to an entirely different order from the moral guilt it would have to address. Remission requires a sacrifice of a different kind.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "5": {
            "synthesis": "<p>Having established what animal sacrifice cannot accomplish, the writer turns to what the Messiah's advent does accomplish, and the evidence is drawn from Psalm 40. The words of the psalmist — \"Sacrifice and offering thou wouldest not, but a body hast thou prepared for me\" — are presented as Christ's own speech upon entering the world. Calvin identifies \"coming into the world\" as the manifestation of Christ in the flesh: his incarnation is the moment these words become fully his. The citation follows the LXX rather than the Hebrew (MT: \"ears you have dug\" or \"opened\"), and Ellicott notes that the LXX reads \"a body hast thou prepared for me\" — a translation the writer accepts as capturing the deeper intention. Clarke underscores the dramatic scene: the eternal Son, when about to take on human nature, says to the Father, \"Sacrifice and offering thou wouldest not\" — marking that the entire Levitical system was never God's final intent. Wesley observes that the sacrifice is offered not merely for Israel but for the whole world: the writer says Christ came \"into the world,\" not \"into the tabernacle,\" because all humanity is interested in his sacrifice. Barnes applies this directly: Paul treats the psalm as Messianic, spoken by Christ as the one who comes to substitute the offering of himself for the offerings the law prescribed.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>This entering into the world was the manifestation of Christ in the flesh; for when he put on man's nature that he might be a Redeemer to the world and appeared to men, he is said to have then come into the world. The words are his own, declaring that no sacrifice except himself could accomplish what the Father required.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Christ, in the prophetic word of Scripture, speaks these words. The LXX renders the Hebrew \"ears thou hast dug\" as \"a body hast thou prepared for me\" — a translation the writer accepts as reaching the deeper meaning: God prepared the incarnate body as the instrument of the one perfect sacrifice.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>When the Messiah was about to be incarnated, he said to God the Father: Sacrifice and offering thou wouldest not — it was never thy will and design that the sacrifices under thy own law should be considered as making atonement for sin; they were only types and shadows of the one great sacrifice.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>It is said, into the world, not into the tabernacle, because all the world is interested in his sacrifice. A body hast thou prepared for me — that I may offer up myself as the one true offering that fulfills all the types of the law.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "6": {
            "synthesis": "<p>The second line of the Psalm 40 citation reinforces what the first announced: God had no pleasure in burnt offerings and sin offerings. Ellicott identifies the \"whole burnt offering\" (<em>holokautoma</em>) as a distinct category — the symbol of complete consecration, offered entirely to God — and observes that this is one of only two places in Hebrews where it is mentioned, underlining the comprehensiveness of the rejection. No class of Levitical sacrifice is exempted: neither the burnt offerings symbolizing dedication, nor the sin offerings addressing guilt, satisfied the divine intention. Clarke presses the theological implication: God could never be pleased with victims under the law as true atonements; they could not satisfy divine justice, nor make the law honorable. Barnes notes that the citation follows the LXX rather than the Hebrew literally, but the sense is retained: God had not \"required\" them in the sense of appointing them as ultimate means of atonement. Their rejection is not a surprise revelation but the open secret embedded in the design of the system from the beginning.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>\"Whole burnt offerings\" — these, the symbol of complete consecration, are mentioned in Hebrews only in this verse and verse 8. \"Thou hast had no pleasure\" — no class of Levitical sacrifice is exempted from this verdict: neither those symbolizing dedication nor those addressing guilt.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>Thou couldst never be pleased with the victims under the law; thou couldst never consider them as atonements for sin; as they could never satisfy thy justice, nor make thy law honorable. Their inadequacy was not incidental but constitutional — built into what they were.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>This is not quoted literally from the Psalm, but the sense is retained. The reading there is, \"burnt-offering and sin-offering hast thou not required.\" God had not appointed them as the ultimate means of atonement — their provisional character was built into their institution from the beginning.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "7": {
            "synthesis": "<p>The Messiah's response to God's dissatisfaction with the Levitical offerings is a declaration of willingness: \"Lo, I come\" — not merely a future arrival but a present one. Ellicott argues for translating \"I am come\" as a present-tense announcement of arrival, not a prediction: the speaker is already present as the one who fulfills what the book prescribes. The phrase \"in the volume of the book it is written of me\" connects the Messiah's mission to the whole sweep of Scripture, and Calvin notes the literary detail: the Hebrew word (<em>megillath sepher</em>) refers to a scroll rolled into a cylinder — books in antiquity were scrolls, and the whole scroll of Scripture testifies to Christ's coming obedience. Clarke expands the philological point: both the Pentateuch in the synagogue and the ancient literary convention of scrolls explain the expression. Barnes identifies this as Paul's explicit application of the psalm to Christ, treating the words as Christ's own at his incarnation — the coming one declares his mission not merely to arrive but to do the Father's will in place of the offerings that could not accomplish it. Wesley's gloss is pointed: \"In this very psalm it is written of me. Accordingly I come to do thy will — by the sacrifice of myself.\"</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>\"Volume\" is properly the meaning of the Hebrew word (<em>megillath</em>); for we know that books were formerly rolled up in the form of a cylinder. There is also nothing unreasonable in understanding it as meaning the Law, which prescribes the rule of a holy life — but the whole of Scripture testifies to Christ's coming.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Rather, <em>Lo, I am come</em> — I am here. The speaker announces his arrival, not merely a future coming. The writer follows the version that renders the mission as an accomplished declaration: I am present, and in the roll of the Book it is written of me what I come to do.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p><em>Bimgillath sepher</em>, \"in the roll of the book\" — anciently, books were written on skins and rolled up. Among the Romans these were called <em>volumina</em>, from <em>volvo</em>, I roll. The Pentateuch in the Jewish synagogue is called <em>sepher</em> and is read in this rolled form to the present day.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>In the volume of the book — in this very psalm it is written of me. Accordingly I come to do thy will — by the sacrifice of myself.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "8": {
            "synthesis": "<p>The writer now unpacks the logic of the psalm citation in two moves, treating first the \"above\" clause and then the conclusion. Here the emphasis falls on what Christ's voice first said: the rejection of the entire catalogue of Levitical offerings. Ellicott clarifies the translation: \"saying at the outset\" — establishing that the rejection of sacrifices is the premise from which the conclusion follows, not an incidental element. The best manuscripts have the plural in the list: sacrifices and offerings and whole burnt offerings and sacrifices for sin. No category is spared the verdict. Wesley notes that when the Psalmist pronounced these words, he spoke in Christ's name — the prophetic Scripture already anticipated the moment of the incarnation. Barnes observes that \"above\" in the writer's phrase refers to the earlier part of the quotation: having first established that no offering man could make would avail, the speaker then announces the alternative. The structure of the psalm is thus made to carry the structure of the argument: the rejection precedes and grounds the substitution.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Better, <em>saying at the outset:</em> the rejection of sacrifices is the established premise. The best MSS. have the plural: \"Sacrifices and offerings and whole burnt offerings and sacrifices for sin\" — every class of Levitical offering falls under the same verdict of divine rejection.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>\"Above when he said, Sacrifice thou hast not chosen\" — that is, when the Psalmist pronounced those words in Christ's name. The prophetic Scripture rehearsed the rejection before announcing the arrival of the one who fulfills what sacrifice could not.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>The word \"above\" refers here to the former part of the quotation — having in the former part said that God did not require sacrifices, in the latter part the Messiah says he came to do the will of God in the place of them. The structure of the psalm carries the structure of the argument.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "9": {
            "synthesis": "<p>The second move in the exegesis: \"then said he, Lo, I come to do thy will.\" Having rejected the first (the Levitical order), he establishes the second (the doing of God's will through the offering of himself). Calvin identifies this as the heart of the theological argument: the full and perfect righteousness under Christ's kingdom stands in no need of the law's sacrifices, for when they are removed, the will of God is set up in their place. The \"first\" and \"second\" here refer not to covenants but to the two halves of the psalm quotation — the rejected offering-system and the accepted obedience — yet they correspond precisely to the covenantal contrast the epistle has been developing. Ellicott observes that the substitution is complete: Christ \"hath taken away\" the first in order to establish the second. Clarke reads the verse as the hinge: the offerings, sacrifices, burnt-offerings, and sin-offerings prescribed by the law are removed; the offering of the body of Jesus once for all is what the will of God now establishes. Wesley condenses the movement: \"in that very instant he subjoined, Lo, I come\" — the rejection and the fulfillment arrive simultaneously. Barnes keeps focus on the finality: Christ shows the prior system to be superseded by coming himself as the appointed alternative.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>See now why and for what purpose this passage was quoted — that we may know that the full and perfect righteousness under the kingdom of Christ stands in no need of the sacrifices of the Law; for when they are removed, the will of God is set up as the foundation of righteousness in their place.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Rather, <em>then hath he said, Lo, I am come to do Thy will. He taketh away the first, that he may establish the second.</em> The substitution is complete and deliberate: the Levitical order is removed in order that the obedience of the incarnate Son may be permanently established in its place.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>He taketh away the first — the offerings, sacrifices, burnt-offerings, and sin-offerings prescribed by the law. That he may establish the second — the offering of the body of Jesus once for all. What the law could never accomplish, the will of God accomplishes through the Son's obedient self-offering.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>In that very instant he subjoined: Lo, I come to do Thy will — to offer a more acceptable sacrifice; and by this very act he taketh away the legal, that he may establish the evangelical, dispensation.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "10": {
            "synthesis": "<p>The consequence of Christ's obedient substitution is sanctification: \"by the which will we are sanctified through the offering of the body of Jesus Christ once for all.\" Ellicott presses the tense: not \"we are being sanctified\" but \"we have been sanctified\" (<em>hēgiasmenoi esmen</em>), placing the act in the past and grounding it in the once-for-all character of the offering. Barnes identifies this verse as the key to the writer's entire argument: sanctification flows not from repeated ritual acts but from the will of God enacted in Christ's obedient self-offering at Calvary. Calvin notes a subtle dimension: David in the psalm professes, not merely in his own person but in Christ's, that God is honored not by the works of the law but by willing and ready obedience. The Levitical system offered external rites; Christ offered his will — and the offering of his body was the perfect expression of that interior obedience. Clarke highlights the practical conclusion: in closing with God's declared will and believing in Christ, the believer finds redemption in his blood and sanctification of heart and life. Wesley is economical: \"By which will — of God, done and suffered by Christ — we are sanctified. Cleansed from guilt, and consecrated to God.\"</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Better, <em>In which will we have been sanctified.</em> The offering was Christ's perfect obedience — \"obedience as far as death, even the death of the cross.\" The past tense grounds sanctification in the completed act of the one offering, not in ongoing ritual repetition.</p>"
                },
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>David professed, not so much in his own person as in that of Christ, that God is honored, not by the external works of the law, but by willing and ready obedience. The offering of the body was the outward expression of an inward obedience — and it is this completed obedience that sanctifies.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>By which will — of God, done and suffered by Christ. We are sanctified — cleansed from guilt, and consecrated to God.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>The apostle immediately specifies what he means, and furnishes the key to his whole argument, when he says that it was through the offering of the body of Jesus Christ once for all. Sanctification flows from this completed act — not from repeated ritual observance.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "11": {
            "synthesis": "<p>The contrast that the chapter has been building now receives its sharpest statement. Every Levitical priest stood — the posture of a servant actively at work — offering daily the same sacrifices that never take away sin. Calvin identifies this as the chapter's conclusion: the practice of daily sacrificing is inconsistent with and wholly foreign to the priesthood of Christ, and hence after his coming the Levitical priests whose settled practice was to sacrifice had nothing left to do. Ellicott reads the verse as a transition, the word \"once for all\" opening naturally to the theme of Christ's completed session. Clarke draws the contrast between priesthood offices: the Jewish priest stands like a servant in continual ministry, repeating what cannot accomplish its end; Christ offered himself once and then sat down. Barnes adds the historical precision: it was not literally every priest every day (they served in courses), but the daily sacrifice was performed within the system, and every priest was part of a system that repeated because it could not complete. Wesley's gloss captures the posture: the standing priest is a servant, never finishing; the seated Christ is a son who has finished his work.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>Here is the conclusion of the whole argument — that the practice of daily sacrificing is inconsistent with and wholly foreign to the priesthood of Christ; and that hence after his coming the Levitical priests whose custom and settled practice was daily to sacrifice had nothing left to do.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>This last was a verse of transition. Naturally following from and completing the previous argument, it leads in the words \"once for all\" to a new thought — preparing the way for the contrast between the standing Levitical priest and the seated Son.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>The office of the Jewish priest is here compared with the office of our High Priest. The Jewish priest stands daily at the altar, like a servant ministering, repeating the same sacrifices; our High Priest offered himself once and by that one offering has done what the other could never accomplish.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>Every priest standeth — as a servant in a humble posture, ministering continually, offering the same sacrifices again and again. The standing posture itself signifies unfinished work; the labor goes on because it cannot complete.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "12": {
            "synthesis": "<p>Against the standing servant-priests who never finish stands this one — \"but he\" (<em>houtos de</em>) — who offered a single sacrifice for sins and then sat down. The session at the Father's right hand is itself the proclamation that the work is done. Ellicott traces the verse as a combination of earlier statements (Hebrews 7:27, 9:26, 8:1) with one addition: the word \"forever\" (<em>eis to dienekes</em>), which appears three other times in the epistle and carries here the full weight of finality. Barnes notes that \"this man\" is not literally in the Greek — the writer says \"but this one\" (<em>houtos de</em>), referring to him as a priest, deliberately leaving open his status as one greater than human. Clarke returns to the servant-king contrast: the Jewish priest stood like a servant actively engaged; Christ sat down as a son in the dignity and honor of completed victory. Wesley compresses the point: \"the virtue of whose one sacrifice remains forever. Sat down — as a son, in majesty and honour.\" The seated posture is not inactivity but the posture of accomplished sovereignty.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>In the main this verse is a combination of Hebrews 7:27 and 9:26 and 8:1. One addition is made, in the words \"for ever\" — these words occur in three other places in Hebrews, and carry here the full weight of finality: one sacrifice, permanently effective, completed forever.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>The office of the Jewish priest is compared here with that of Christ. The Jewish priest stands daily at the altar like a servant; our High Priest offered himself once and sat down — as a son, in the dignity and honour of completed and permanent victory over sin.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>But he — the virtue of whose one sacrifice remains for ever. Sat down — as a son, in majesty and honour. The session is not inactivity but the posture of one whose work stands complete and unassailable.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>\"But this man\" — the word \"man\" is not in the original. The Greek is literally \"but this\" — referring to this priest, without specifying rank or nature, as one greater than human comparison can capture. The contrast with the standing, repeating priests is absolute: one offering, one sitting down, one completion.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "13": {
            "synthesis": "<p>Having sat down, Christ now waits — but the waiting is not passive. Psalm 110:1 lies behind this verse as it has behind the epistle's central argument: \"Sit thou at my right hand, until I make thine enemies thy footstool.\" Ellicott observes that Christ does not continue to offer sacrifice or minister; he waits for the promised subjection of his foes. This forward orientation toward the consummation is not incidental: it appears also at Hebrews 9:28, where the writer has directed thought to the coming of Christ for salvation. Clarke draws out the political dimension: the enemies include all who oppose Christ's high priesthood and sacrificial offering; they will be defeated and made to acknowledge his supremacy as universal and eternal King. Barnes anchors the verse in Psalm 110, where God promises the Davidic king that enemies will be subdued; the writer applies this to Christ's present session and future triumph. Wesley identifies the waiting one as the coming judge who will reward every man according to his works — the session of rest and the expectation of vindication are held together.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>He does not minister and offer His sacrifice again, but waits for the promised subjection of His foes. Once before in this context our thought has been directed to the future consummation (Hebrews 9:28); here again the session of completion leads directly to expectation of final victory.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>Till his enemies be made his footstool — till all that oppose his high priesthood and sacrificial offering shall be defeated, routed, and confounded; and acknowledge, in their punishment, the supremacy of his power as universal and eternal King and Judge.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>There is an allusion here to Psalm 110:1: \"The Lord said unto my Lord, Sit thou at my right hand, until I make thine enemies thy footstool.\" He waits there until this shall be accomplished — the complete subjection of all opposition to his reign and priesthood.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "14": {
            "synthesis": "<p>The argument reaches a summit: \"by one offering he hath perfected forever them that are sanctified.\" Every key element in the epistle's argument is compressed here. One offering — not many. Perfected — the very goal the Levitical system could never reach. Forever (<em>eis to dienekes</em>) — not provisionally or annually, but permanently. Those being sanctified — the ongoing application to believers of what is eternally accomplished. Ellicott notes that \"perfection\" was the specific term the writer used in chapter 7 to show that perfection did not come through the Levitical priesthood or the law; now it is stated that it has come through this one offering. Clarke highlights the equivalence the writer has established: <em>teleioo</em> (to make perfect) is functionally equivalent to <em>aphesis</em> (remission of sins) — to be perfected is to receive full pardon and consecration together. Wesley states the practical upshot: Christ \"hath done all that was needful in order to their full reconciliation with God.\" Barnes observes the structural contrast: the Jewish priest offered often and still did not avail to put away sin; the Saviour made one sacrifice, and it was sufficient for the sins of the world.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>No repetition of His offering is needed, for by one offering He hath brought all unto \"perfection\" — and that \"for ever.\" In Hebrews 7:11 we read that perfection did not come through the Levitical priesthood or the law; now perfection is declared as achieved through this one offering.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>For by one offering — his death upon the cross. He hath perfected for ever — <em>teleioo</em> here is functionally equivalent to <em>aphesis</em>, remission of sins: he has procured remission of sins and holiness together, in one completed act of everlasting efficacy.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>He hath perfected them for ever — that is, has done all that was needful in order to their full reconciliation with God. The completion is permanent and total; nothing remains to be added to what this one offering has accomplished.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>By one offering — by offering himself once on the cross. The Jewish priest offered his sacrifices often, and still they did not avail to put away sin; the Saviour made one sacrifice, and it was sufficient for the sins of the world. He hath laid the foundation of eternal perfection for all who are sanctified.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "15": {
            "synthesis": "<p>The argument from Jeremiah that was introduced in chapter 8 is now recalled to provide the capstone of the doctrinal section. The Holy Spirit is identified as the speaker of Scripture — not the human prophet Jeremiah, but the divine author whose word endures. Calvin's note here is precise: the Spirit's testimony is not adduced a second time to reestablish the point but to prove its permanence — the new covenant, once ratified, removes the need for the entire sacrificial apparatus the writer has just dismissed. Ellicott explains the syntax: \"the Holy Ghost also beareth witness unto us\" introduces what follows, and \"after He hath said before\" refers back to what was already quoted in chapter 8. The double citation is not mere repetition but a demonstration that the prophecy is now fulfilled — what Jeremiah foretold has come to pass in Christ. Wesley sees this verse as winding up the entire argument concerning Christ's priesthood and sacrifice: the new covenant is now completely ratified, and the Jeremiah quotation seals the conclusion. Clarke adds the pneumatological point: that Jeremiah spoke at all confirms he spoke by the inspiration of the Spirit of God.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>\"Now testifieth to us does also the Holy Spirit\" — this testimony from Jeremiah is not adduced a second time to reestablish what was said, but to prove that the covenant is permanent. The Spirit's witness confirms that sins once forgiven under this covenant are forgiven forever.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>\"And the Holy Ghost also beareth witness unto us\" — the Holy Ghost speaking in Scripture, as in Hebrews 3:7 and 9:8. \"After He hath said\" refers back to the quotation in chapter 8. The double citation is not repetition but confirmation: prophecy fulfilled is testimony that the new covenant stands.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>The Holy Ghost is a witness to us — the words are quoted from Jeremiah 31:33-34, and here we are assured that Jeremiah spoke by the inspiration of the Spirit of God. The Spirit who inspired the prophecy is the same Spirit who now confirms its fulfillment in Christ.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>In this and the three following verses, the apostle winds up his argument concerning the excellency and perfection of the priesthood and sacrifice of Christ. The new covenant is now completely ratified, and the prophecy from Jeremiah seals what the sacrifice accomplished.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "16": {
            "synthesis": "<p>The first clause of the Jeremiah quotation as it appears here focuses on the interiority of the new covenant: \"I will put my laws into their hearts, and in their minds will I write them.\" Ellicott notes the slight variation from the version given in chapter 8: the first part of the original quotation is omitted, and the order in this version places \"heart\" before \"mind,\" emphasizing that the law under the new covenant is not external statute but internal disposition. The contrast with Sinai is implicit: the old covenant wrote on stone; the new covenant writes on the human heart. Barnes draws out the practical difference: the law given externally at Sinai could command but not enable; the law written on the heart is accompanied by the power that fulfills it. This is the positive side of the new covenant — not merely that sins are forgiven (v.17) but that the believer is constituted as one whose deepest orientation is toward God's will. The entire preceding argument about Christ's once-for-all sacrifice finds here its goal: not just the removal of guilt but the renovation of the inner person.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The first part of the quotation from Jeremiah is omitted here; the order in this version places \"heart\" before \"mind\" — putting my laws upon their heart, upon their mind also will I write them. The interiority of the new covenant is the point: not external statute but inward disposition.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>The covenant written on the heart — this is the positive side of the new covenant's promise. The law given externally at Sinai could command but not enable; the law written on the heart is accompanied by the power that fulfills it. Forgiveness and inner renovation belong together as the new covenant's twin gifts.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "17": {
            "synthesis": "<p>The second clause of the Jeremiah citation is the hinge on which the entire doctrinal argument turns: \"Their sins and their iniquities will I remember no more.\" Ellicott notes a textual difficulty — the Authorized Version's rendering leaves the sense imperfect across vv.15-17, but the true reading flows continuously from v.15's introduction of the Holy Spirit's witness through to this conclusion. Barnes identifies this as the decisive logical step: God's promise to remember sins no more means the complete and permanent removal of guilt. This is not the suppression of divine memory but the legal reality of full pardon — God as judge will not bring these sins forward again. The implication the writer will draw in the next verse is immediate: where God has promised to remember sins no more, there is no function remaining for a sin-offering. The entire Levitical apparatus for the removal of guilt is made redundant by this single divine declaration. The promise does not merely reduce the frequency of condemnation; it eliminates the category of condemnation altogether for those under the new covenant.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Every reader must feel that as these verses stand in the Authorised version the sense is imperfect. The true text flows from the Spirit's witness in verse 15 through to this conclusion: \"Their sins and their iniquities will I remember no more\" — the final and decisive word of the new covenant promise.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>God's promise to remember sins no more means the complete and permanent removal of guilt. This is not the suppression of memory but the legal reality of full pardon — God as judge will not bring these sins forward again at any future reckoning. The promise eliminates condemnation for those in the new covenant.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "18": {
            "synthesis": "<p>The doctrinal argument reaches its triumphant close: \"Now where remission of these is, there is no more offering for sin.\" Ellicott supplies the better translation: \"But where remission of these is, there is no longer offering for sin.\" The logic is airtight. If sins are fully forgiven — if God has promised to remember them no more — then there remains no function for any sacrifice to discharge. The entire system of atonement offerings is not merely superseded but rendered logically impossible: you cannot offer an atonement for something that has already been permanently and finally remitted. Calvin had made this point throughout the argument; Ellicott notes that here the argument reaches its formal conclusion. Clarke states it clearly: in any case where sin is once pardoned, there is no further need of a sin-offering, and every believer in Christ has sin blotted out and therefore needs no other offering. Barnes uses the economic analogy: if a debt is fully paid, there is no need to pay it again; to offer another sacrifice would imply that the first had failed. The single sufficient sacrifice has rendered the entire sacrificial apparatus permanently obsolete.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Better, <em>But where remission of these is, there is no longer offering for sin.</em> Here the argument reaches its triumphant close. Full forgiveness logically eliminates any function for further sacrifice — you cannot offer an atonement for what has been permanently and finally remitted.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>Now where remission of these is — in any case where sin is once pardoned, there is no farther need of a sin-offering; but every believer on Christ has his sin blotted out, and therefore needs no other offering for that sin. The forgiveness is final and complete.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>If those sins are wholly blotted out, there is no more need of sacrifice to atone for them, any more than there is need to pay a debt that has already been paid in full. To offer another sacrifice would imply that the first had failed — which the entire argument has shown to be impossible.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "19": {
            "synthesis": "<p>The epistle pivots here from doctrine to application, and the transition is marked by the word \"therefore\" — everything that follows flows from what has just been established. The first conclusion the writer draws is that believers now have \"boldness\" (<em>parresia</em>) to enter the holiest place by the blood of Jesus. Calvin summarizes the sum of the preceding doctrine: all the faithful have free access to God through Christ, by the sacrifice he has offered and by his intercession. Ellicott notes that <em>parresia</em> carries the sense of frank, confident openness — not the cringing approach of the unclean to the sacred but the free and direct access of those whose entry is purchased and permanent. Barnes observes that the hortatory section will continue to the end of the epistle, and this verse launches it by recalling the chief comparison of the argument: what the Jewish high priest alone could approach once a year, every believer may now approach always. Clarke notes the completion of the doctrinal section and the shift to exhortation grounded in the superiority of Christ's priesthood. Wesley sees this as a brief recapitulation: having liberty to enter the holy of holies, believers are summoned to exercise that liberty.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He states the conclusion or sum of his previous doctrine — that all the faithful now have free access to God through Christ, by the sacrifice he has offered and by his intercession. This is the foundation from which the exhortation of the chapter's second half proceeds.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The exhortation here begins very similar to that of Hebrews 4:14-16; its greater fullness is in accordance with the development of the thought. The word \"boldness\" — <em>parresia</em> — carries the sense of frank, confident openness: not the cringing of the unclean but the free access of those whose entry is purchased and permanent.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>The apostle, having now finished the doctrinal part of his epistle, and fully shown the superiority of Christ to all men and angels, and the superiority of his priesthood to that of Aaron, now proceeds to exhortation — beginning with this: believers have boldness to enter the most holy place by the blood of Jesus.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>The apostle enters on the hortatory part of his epistle. What the Jewish high priest alone could approach once a year — and that only with blood — every believer may now approach always. The blood of Jesus is the permanent and sufficient ground of that access.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "20": {
            "synthesis": "<p>The access described in v.19 proceeds by \"a new and living way\" (<em>hodon prosphaton kai zosan</em>) — Christ himself is the path into the divine presence. Both adjectives are significant. Calvin presses the image: the divinity, though hidden in the flesh of Christ, leads us even into heaven; no one can find God except through the man Christ as door and guide. The veil concealed the inner sanctuary but admitted entry into it, and so Christ's flesh — in concealing divinity — simultaneously becomes the means by which humanity enters the presence of God. Clarke emphasizes the novelty: no human being had ever before entered heaven in human nature; Jesus was the first, and his resurrection and ascension opened the way for all who are his. Barnes identifies the Greek word for \"new\" (<em>prosphatos</em>) as rare — occurring only here in the NT and carrying the sense of freshly killed or recently opened — capturing the very freshness of the access purchased by Christ's death. Wesley develops the paradox of the veil: as the rending of the temple veil made the holy of holies visible and accessible, so the wounding of Christ's body opened the way into the divine presence. The way is \"living\" because Christ who is the way is himself alive, and therefore the access is permanent.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>As the veil covered the recesses of the sanctuary and yet afforded entrance there, so the divinity, though hid in the flesh of Christ, leads us even into heaven; nor can any one find God except he to whom the man Christ becomes the door and the guide into the holy presence.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>By a new and living way — it is a new way; no human being had ever before entered into the heaven of heavens in human nature; Jesus was the first, and thus his resurrection and ascension to glory has opened the way to heaven for all mankind.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>By a living way — the way of faith, whereby we live indeed. As by rending the veil in the temple, the holy of holies became visible and accessible; so by wounding the body of Christ, the way to heaven was opened to all who believe.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>The Greek word rendered \"new\" — <em>prosphatos</em> — occurs only here in the New Testament and carries the sense of freshly opened, recently prepared. The way is \"living\" because Christ who is the way is alive, and therefore the access he provides is permanent and unceasing.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "21": {
            "synthesis": "<p>The third element grounding the exhortations is a great High Priest over the house of God. Calvin draws attention to the corollary: whatever has been said throughout the epistle about the abrogation of the ancient priesthood must be borne in mind here, for Christ could not be a priest without the former priests being divested of their office — the two cannot coexist. Ellicott notes that the Greek here properly signifies a \"great priest\" rather than \"high priest,\" one of the technical designations used both in Hebrew and in the LXX, and finds it interesting that this designation was not introduced earlier in the exhortation. Clarke identifies the \"house of God\" as the Christian Church — all true believers in Christ — and observes that over this congregation Christ is the High Priest who offers his own blood on their behalf and intercedes at the Father's right hand. Barnes reinforces the parallel with the prior demonstration: that there is a great high priest over the spiritual house of God had been shown at length in the preceding chapters, and it now becomes the second ground of the triple exhortation. The three grounds are complete: blood of Jesus, the new and living way, and the great High Priest.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>Whatever he has previously said of the abrogation of the ancient priesthood, it behaves us now to bear in mind, for Christ could not be a priest without having the former priests divested of their office. He then intimates that there is now a supreme and only priest in the kingdom of Christ.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>The Greek words properly signify a <em>great priest</em> — one of the names by which the high priest is frequently designated in both the Hebrew and the LXX. Its appearance here completes the triple foundation for the appeals to follow: boldness of access, the living way, and the great High Priest.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>The house or family of God is the Christian Church, or all true believers in the Lord Jesus. Over this Church, house, or family, Christ is the High Priest — in their behalf he offers his own blood, and their persons and services are accepted through him.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "22": {
            "synthesis": "<p>The first of the three great exhortations: \"let us draw near\" — the central act of worship now enabled by everything that has been established. Four qualifications accompany the exhortation, arranged in pairs. The heart must be true and must hold faith in full assurance; the conscience must be sprinkled clean and the body washed with pure water. Calvin emphasizes the correspondence: as the Levitical system required external washings, so the gospel requires a deep interior reality. Ellicott identifies \"true\" (<em>alethine</em>) as the same word used in chapters 8 and 9 for the \"real\" sanctuary — a sincere, real heart as opposed to a counterfeit or divided one. Clarke reads the verse in sacrificial language: \"let us draw near\" is the language of coming to the altar. Wesley lists the four conditions plainly and draws a pointed contrast: \"our bodies washed with pure water — all our conversation spotless and holy, which is far more acceptable to God than all the legal sprinklings and washings.\" Barnes observes that sincerity of heart was always required under every religious dispensation; what is new here is the full assurance that Christ's completed sacrifice makes available as the confident ground of approach.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>As he shows that in Christ and his sacrifice there is nothing but what is spiritual or heavenly, so he would have what we bring on our part correspond. The Jews cleansed themselves by various washings to prepare for the service of God; now a true heart and a sprinkled conscience are what the gospel requires.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>\"True\" — the word used in Hebrews 8:2 and 9:24 for what is <em>real</em>, as opposed to shadowy or symbolic. A sincere and genuine heart, as opposed to a counterfeit or divided one. \"Full assurance of faith\" — the confident ground of approach that Christ's completed sacrifice makes available.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>Let us draw near to God. With a true heart — in godly sincerity. Having our hearts sprinkled from an evil conscience — so as to condemn us no longer. And our bodies washed with pure water — all our conversation spotless and holy, far more acceptable to God than all the legal sprinklings and washings.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>A sincere heart was required under the ancient dispensation; it is always demanded when men draw near to God. What is new here is the \"full assurance of faith\" — the confident ground of approach made available by Christ's completed sacrifice, which removes the barrier that once made certainty of acceptance impossible.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "23": {
            "synthesis": "<p>The second exhortation: \"let us hold fast the profession of our hope without wavering.\" Calvin notes that the writer says \"hope\" here rather than \"faith\" deliberately: hope is born of faith and sustained by it, and it is hope — the forward-looking grip on what is not yet possessed — that requires particular steadiness under pressure. He also requires \"confession\" (<em>homologia</em>), for true faith does not remain interior; it shows itself before others. Ellicott traces the characteristic vocabulary: \"hold fast\" and \"profession/confession\" both appear in earlier exhortation passages (3:6, 3:14, 4:14), and their return here shows the writer consolidating and intensifying his appeal. Clarke gives the etymology: <em>homologia</em>, from <em>homou</em> (together) and <em>logos</em> (word), implies the common acknowledgment that united all Christians — particularly their shared confession of Jesus as Lord and Messiah. Barnes notes that securing this was one of the epistle's leading designs: those addressed were suffering persecution, and there was real danger of falling away from public confession under pressure. The ground of not wavering is stated: \"for he is faithful that promised\" — the stability of hope rests not on the quality of the believer's grip but on the reliability of the promiser.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>As he exhorts here to persevere, he mentions hope rather than faith; for as hope is born of faith, so it is fed and sustained by it to the last. He requires also confession, for it is not true faith except it shows itself before men, particularly under the pressure of persecution.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>\"Hold fast\" and \"confession\" are both characteristic words of earlier exhortations in this letter. \"Of our hope\" — hope as the forward-looking expression of faith, which requires steadiness under the pressure of not yet possessing what is believed. The faithful promiser is the ground of not wavering.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p><em>Homologia</em> — from <em>homou</em>, together, and <em>logos</em>, a word — implies that general consent that was among Christians on all the important articles of their faith and practice; particularly their acknowledgment that Jesus is the Christ, the Messiah, the universal Saviour.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>It is evident that those to whom the epistle was written were suffering persecution, and that there was great danger of their apostatizing. The foundation of holding fast is given: \"for he is faithful that promised.\" Stability of hope rests not on the quality of the believer's grip but on the reliability of God's word.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "24": {
            "synthesis": "<p>The third exhortation turns outward from the individual to the community: \"let us consider one another to provoke unto love and to good works.\" Calvin observes that the writer addresses the Jews especially here, noting their historical tendency toward national exclusivism; the gospel reverses this toward mutual care and encouragement. Ellicott reads a careful sociological observation: the word \"consider\" carries the sense of steady, attentive regard — the writer may have known that among his addressees \"provocations\" existed that did not tend toward brotherly love, and he is redirecting the capacity for provocation toward its constructive use. Clarke gives the Greek: <em>katanooomen</em> — let us diligently and attentively consider each other's trials, difficulties, and weaknesses; feel for each other. The provocation to love and good works is not the passive assumption that these will naturally occur but an active stirring-up. Barnes emphasizes the mutuality: they were not to be selfish or confine attention to their own spiritual state; the welfare of others is to be actively regarded and promoted. The exhortation assumes that the Christian life is inherently communal — no one perseveres in isolation.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>I doubt not but that he addresses the Jews especially in this exhortation. It is well-known how great was the arrogance of that nation; being the posterity of Abraham, they boasted that they alone had been chosen. The gospel reverses this inward-looking tendency toward mutual care and provocation to love.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Gradually the writer passes from that which belongs to the individual to the mutual duties of members of a community. Possibly he knew that amongst those whom he addresses there had existed \"provocations\" that did not tend towards brotherly love — and he is redirecting that capacity toward its constructive use.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p><em>Katanooomen</em> — let us diligently and attentively consider each other's trials, difficulties, and weaknesses; feel for each other, and excite each other to an increase of love to God and man; and, as the proof of this, abound in good works toward all.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>Let us so regard the welfare of others as to endeavour to excite them to persevere in the Christian life. They were not to be selfish; they were not to confine attention to their own spiritual state. Much might be done in securing perseverance and fidelity by mutual, kind exhortation.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "25": {
            "synthesis": "<p>The communal exhortation takes a concrete and urgent form: do not forsake the assembling of yourselves together, as the manner of some already is. Ellicott identifies what was happening: some members of the community had persuaded themselves that the relationship of Judaism to Christianity allowed them to step back from the distinctively Christian assembly, as though external ordinances were beneath those who had received the Spirit. Calvin finds in the Greek word (<em>episynagoge</em>) the image of the new community gathering within and beyond the old: the wall of partition having been broken down by Christ, the assembly includes all. Clarke notes the word appears only once more in the NT (2 Thess. 2:1), and whether it refers to public or private worship, the force is the same: deliberate withdrawal from Christian fellowship is treated as a step toward apostasy. Wesley identifies two reasons some were withdrawing: fear of persecution or the vain imagination of being above external ordinances. The urgency increases as the Day approaches — and the exhortation to assemble is simultaneously an exhortation to mutual encouragement as the pressure intensifies.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>The composition of the Greek word ought to be noticed; for <em>epi</em> signifies an addition; then <em>episynagoge</em>, assembling together, means a congregation increased by additions. The wall of partition having been put down by Christ, the assembling now includes both Jew and Gentile together.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Some members of this community had persuaded themselves that the relation of Judaism to Christianity allowed them to step back from the Christian assembly, as though external ordinances were beneath those who had received the Spirit. The writer names this \"the manner of some\" and opposes it directly.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p><em>Episynagoge</em> is used only once more in the NT (2 Thess. 2:1). Whether it means public or private worship, the force is the same: deliberate withdrawal from Christian fellowship is treated as a step toward the apostasy warned against in the verses that follow.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>Not forsaking the assembling ourselves — in public or private worship. As the manner of some is — either through fear of persecution, or from a vain imagination that they were above external ordinances. But exhorting one another — and so much the more, as ye see the day approaching.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "26": {
            "synthesis": "<p>The warning passage that opens here (vv.26-31) is among the most severe in the NT, and all commentators agree on its subject: not ordinary repeated sin but deliberate apostasy — the willful, final, public renunciation of Christ and his gospel. Calvin is unequivocal: severe vengeance awaits those who fall away from the grace of Christ, being now given up to inevitable destruction. Ellicott specifies that the state described is even more clearly than in 6:4-6 one of willful and continued apostasy — the word \"willfully\" (<em>hekousios</em>) is decisive. Clarke reads the verse historically: to renounce the profession of the Gospel and its Author deliberately, for fear of persecution or from any other motive, after having been convinced that Jesus is the Messiah — this is what is described. Wesley's reading is characteristically precise: \"wilfully — by total apostasy from God, termed 'drawing back' in verse 38.\" The consequence is stark: there remains no more sacrifice for sins. Having rejected the one sacrifice that avails, the apostate stands without any means of atonement. This verse addresses those who abandon Christ as the foundation of their relation to God, not Christians who stumble in ordinary failing.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He shows how severe a vengeance of God awaits all those who fall away from the grace of Christ; for being without that one true salvation, they are now given up to inevitable destruction. The sin described is not ordinary failure but the deliberate and final rejection of the only sacrifice that avails.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Even more clearly than in Hebrews 6:4-6 the state described is one of wilful and continued apostasy. The word \"wilfully\" (<em>hekousios</em>) is decisive: this is not stumbling or repeated failure but the deliberate, knowing renunciation of Christ after receiving the knowledge of the truth.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>If we deliberately, for fear of persecution or from any other motive, renounce the profession of the Gospel and the Author of that Gospel, after having received the knowledge of the truth so as to be convinced that Jesus is the Messiah — there remaineth no more sacrifice for sins.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>When we — any of us Christians — sin wilfully — by total apostasy from God, termed \"drawing back\" in verse 38 — after having received the experimental knowledge of the gospel truth, there remaineth no more sacrifice for sins. None but that which we obstinately reject.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "27": {
            "synthesis": "<p>For the apostate who has abandoned the one sacrifice, what remains is not nothing but something far worse: \"a certain fearful looking for of judgment, and fiery indignation which shall devour the adversaries.\" Ellicott's translation sharpens the image: \"a fearful awaiting of judgment, and a jealousy of fire\" — the fire that will consume God's adversaries. Calvin presses into the psychological dimension: the torment is not only future judgment but the present torment of an evil conscience in those who know they have tasted grace and lost it forever through their own fault. That present anguish is itself a foretaste of the judgment awaited. Barnes notes that \"certain\" in the Authorized Version does not mean fixed or inevitable in the sense of logical necessity; rather, the Greek has the sense of a fearful <em>tis</em> expectation — an indefinite but overwhelming dread. Clarke drives the theological point: God will pardon no one without a sacrifice for sin, and from this it follows that when no sacrifice remains, no pardon remains. Wesley supplies the context: God's judgment reaches even to his own who rebel against him.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He means the torment of an evil conscience which the ungodly feel, who not only have no grace but who also know that having tasted grace they have lost it forever through their own fault; such are not merely pricked and bitten but tormented as a present anticipation of the judgment to come.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Better, <em>a fearful awaiting of judgment, and a jealousy of fire that shall devour the adversaries.</em> For Christ's waiting servants the thought of \"judgment\" is lost in that of \"salvation\"; to these sinners nothing remains but the devouring fire that consumes those who stand against God.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>From this it is evident that God will pardon no man without a sacrifice for sin; for otherwise it would not follow from there remaining to apostates no more sacrifice that they must expect only fearful judgment. No sacrifice, no pardon; no pardon, only judgment awaited.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>The word \"certain\" does not mean fixed or inevitable in the sense our translation implies. The Greek carries the sense of a fearful, overwhelming dread — an indefinite but crushing expectation of judgment that hangs over those who have knowingly abandoned the only means of reconciliation.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "28": {
            "synthesis": "<p>The argument from lesser to greater begins here. Under Moses' law, the one who despised it — who presumptuously transgressed its terms — died without mercy on the testimony of two or three witnesses. No appeal for clemency was permitted; the structure of the law made the penalty automatic and public. Calvin identifies the logic as <em>a fortiori</em>: if it was a capital offense to violate the law of Moses, how much heavier punishment does the rejection of the gospel deserve? Ellicott identifies the specific legal reference: Deuteronomy 17:2-7, where the penalty for idolatry is death by stoning at the mouth of two or three witnesses. The one who \"hath set at nought\" the law — a stronger word than merely breaking it, implying contemptuous rejection — receives the same contemptuous treatment in kind from the law. Clarke adds Numbers 15:30 to the background: presumptuous sinning was categorically excluded from the normal provision for atonement even under the old covenant. Barnes specifies that the apostle has in view particularly those offences punishable with death — not ordinary breaches but the categorical rejection of the covenant itself. Wesley echoes: capital cases, presumptuously transgressed, died without delay or mitigation.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>This is an argument from the less to the greater; for if it was a capital offense to violate the law of Moses, how much heavier punishment does the rejection of the gospel deserve, a sin which involves so many and so heinous impieties! The lesser penalty anchors the scale for what the greater demands.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Rather, <em>a man that hath set at nought a law of Moses dieth without pity before two or three witnesses.</em> The reference is to Deuteronomy 17:2-7. \"Set at nought\" is stronger than breaking a law — it implies contemptuous rejection of the covenant structure itself.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>He that rejected it, threw it aside, and denied its Divine authority by presumptuous sinning, died without mercy — without any extenuation or mitigation of punishment (Numbers 15:30). Presumptuous sinning was categorically excluded from normal atonement even within the old covenant.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>It does not mean that in all cases the offender against Moses' law died without mercy, but only where offences were punishable with death — and probably the apostle had particularly in view the case of idolatry, which is the closest analogue to apostasy from the gospel.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "29": {
            "synthesis": "<p>If death without mercy was the penalty for despising Moses, of how much severer punishment shall he be thought worthy who has committed three acts of apostasy against the very Son of God? Ellicott identifies three distinct acts named in this verse: trampling the Son of God underfoot, treating the blood of the covenant as a common or unholy thing, and outraging the Spirit of grace. Each is a deliberate reversal of what was received in faith. Calvin presses the eschatological weight: apostates from Moses suffered death of the body; apostates from the gospel deserve not merely temporal punishment but eternal perdition — the punishment is proportioned to the dignity of the one rejected. Clarke unpacks \"trodden underfoot the Son of God\" as the utmost contempt and blasphemy. Counting the blood of the covenant \"an unholy thing\" (<em>koinon</em> — common, profane) is the deliberate devaluation of what was designated as the most sacred in existence. Wesley identifies the verse's scope: \"it does not appear that this passage refers to any other sin\" than total apostasy. Barnes notes that if one who abandoned Moses was deserving of death without mercy, one who abandons Christ deserves commensurately greater judgment — and God will treat such a person accordingly.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>There is this likeness between apostates under the Law and under the Gospel, that both perish without mercy; but the kind differs: the Apostle denounces on the despisers of Christ not only the death of the body but eternal perdition — the punishment proportioned to the infinite dignity of the one they have rejected.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>In the act of apostasy the sinner trampled under foot the Son of God, treated with contempt Him to whom belongs all majesty; counted the blood of the covenant — the most sacred thing in existence — as common and profane; and insulted the Spirit of grace who had drawn him to Christ.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>Such offenses under Moses were trifling in comparison, and in justice the punishment should be proportioned to the offense. Trodden under foot the Son of God — treated him with the utmost contempt and blasphemy. The blood of the covenant counted as a common, profane thing.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>He who renounces Christianity ought to be regarded as deserving a much severer punishment than the man who apostatized from the Jewish religion, and if he ought to be so regarded he will be — for God will treat people according to what they deserve. Greater privilege brings greater accountability.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "30": {
            "synthesis": "<p>Two quotations from Deuteronomy 32 are brought forward to ground the warning in divine self-declaration: \"Vengeance is mine; I will repay,\" and \"The Lord will judge his people.\" Calvin notes that both passages in their original context promise that God would take vengeance for wrongs done to his people by their enemies — yet the writer applies them with full propriety to the vengeance God exacts from apostates within the people, because apostates have become the enemies of God from within. Ellicott observes that the first quotation (Deut. 32:35) departs from both the Hebrew and the LXX in its phrasing while completely preserving the sense, and that the application here is to those who stand against God precisely by abandoning his covenant. Clarke confirms: the saying originally addressed idolatrous Gentiles who were enemies of God's people, and is here applied to apostates who stand in the same adversarial relation. Barnes points back to Romans 12:19, where the same verse is quoted to discourage private revenge — here it is quoted to confirm that God's own judgment is certain and sovereign. Wesley distills the weight of the second quotation: God judges his people far more rigorously than he judges pagans if they rebel against him.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>Both passages are taken from Deuteronomy 32:35-36. As Moses there promises that God would take vengeance for the wrongs done to his people, the writer applies them to the vengeance God exacts from apostates — their rebellion is the greater because it is from within the covenant itself.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>This quotation from Deuteronomy 32:35 completely preserves the sense of the original while departing from its form. The application here is to those who stand against God by abandoning his new covenant — making themselves adversaries from within the very community of grace.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>Vengeance belongeth unto me — this is the saying of God in Deuteronomy 32:35, in reference to idolatrous Gentiles who were enemies of his people; and it is here with propriety applied to apostates who, being enemies to God's ordinances, stand in the same adversarial relation.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>The Lord will judge his people — yea, far more rigorously than the heathens, if they rebel against him. Those who have received the greatest light and the greatest privilege bear the greatest accountability when they turn against what they received.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "31": {
            "synthesis": "<p>The warning section closes with one of the most solemn sentences in the NT: \"It is a fearful thing to fall into the hands of the living God.\" The very phrase \"the living God\" carries weight throughout Hebrews (3:12, 9:14) and in the broader biblical tradition: the one who lives forever can punish forever, and his hands are not metaphorical but the hands of infinite power and absolute justice. Ellicott draws the connection with Deuteronomy 32:39 — \"I kill and I make alive\" — and with David's choice in 2 Samuel 24 between human and divine judgment; Barnes develops this allusion in detail: David asked to fall into the hands of the Lord rather than the hands of men because God's mercies are great. Yet here the phrase is turned to its other edge: for the apostate who has exhausted the mercy available and rejected its sole source, to fall into those same hands is a fearful and not a welcome prospect. Clarke presses the eternal dimension: he who lives forever can punish forever; the \"living God\" is precisely the one who cannot be outworn by time. Wesley is direct: to fall into the hands of God's avenging justice. The severity of the warning is the measure of the grace that makes such falling unnecessary.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>\"A Living God\" — as in Hebrews 3:12 and 9:14 the exact meaning is \"a Living God.\" There can be little doubt that Deuteronomy 32:39 lies behind the phrase. The one who lives forever possesses both the power and the duration to execute judgment that outlasts all human time.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>To fall into the hands of God is to fall under his displeasure; and he who lives for ever can punish for ever. How dreadful to have the displeasure of an eternal, almighty Being turned against you — one whose justice is as inexhaustible as his life!</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>To fall into the hands — of his avenging justice. The very phrase that elsewhere offers comfort — falling into God's hands rather than human hands — here carries its other edge: for those who have rejected the mercy offered, the same hands become the instrument of inevitable judgment.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>There may be an allusion to David's request to \"fall into the hands of the Lord, and not into the hands of men\" (2 Sam. 24). David said this because God's mercies are great; but for the apostate who has rejected those mercies, to fall into the same hands is the most fearful prospect imaginable.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "32": {
            "synthesis": "<p>From warning the writer pivots to encouragement, and as in chapter 6 the encouragement takes the form of a grateful appeal to what these believers have already endured and demonstrated. \"Call to remembrance the former days\" — the early season of their Christian life, after they were enlightened, when they endured a great contest of sufferings. Calvin identifies the rhetorical purpose: it is shameful to begin well and faint in the middle of the course, and still more disgraceful to abandon it altogether after having run much of it; the memory of earlier faithfulness is meant to shame any thought of retreat now. Ellicott notes the structural parallel with chapter 6: from warning the writer turns to encouragement, and here, as there, he thankfully recalls the earlier proofs his readers gave of genuine faith under fire. Clarke provides historical context: the first believers in Judea were greatly persecuted from the earliest days — Stephen's martyrdom, the persecution after his death, subsequent waves of suffering — and the readers had endured a great fight of sufferings in that earlier season. Barnes notes that they were currently again under severe trial, and the memory of the former victory is the ground for confidence that they can endure again.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>In order to stimulate them and rouse their alacrity to go forward, he reminds them of the evidences of piety which they had previously manifested; for it is a shameful thing to begin well and to faint in the middle of our course, and still more disgraceful to abandon it altogether after having run much of it.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>In the last six verses the writer has enforced his exhortation by an appeal to the danger of falling away; from warning he now turns to encouragement, as in Hebrews 6, and here, as there, he thankfully recalls the earlier proofs his readers gave of genuine faith under suffering.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>It appears from this that the first believers in Judea were greatly persecuted; our Lord's crucifixion, Stephen's martyrdom, the persecution that arose after his death — the readers had endured a great fight of sufferings in those early days, and the memory of it is ground for renewed confidence.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>Enlightened — with the knowledge of God and of his truth. After they had been illuminated and drawn into the Christian community, they endured a great contest of sufferings — and endured it well. The writer recalls this to shame any thought of retreat now that the contest is renewed.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "33": {
            "synthesis": "<p>The suffering took two forms, and both are mentioned. The first was direct and public: being made a theatrical spectacle (<em>theatrizomenoi</em>), exposed to reproaches and afflictions before a watching crowd. Ellicott notes the theatrical metaphor — the Greek word literally invokes the theatre, the place of public spectacle; here it is probably figurative, as in 1 Corinthians 4:9. The second form was indirect but equally demanding: becoming companions (<em>koinonoi</em>) — sharers — with those who were so treated. Both modes of suffering required the same interior resource. Clarke supplies the detail: the word <em>theatrizomenoi</em> means to be exhibited as wild beasts and other shows at the theatres, and parallels 1 Corinthians 4:9. The companions were those who, though not personally under public attack, chose to stand with the persecuted and share their disgrace rather than step away to safety. Barnes identifies the same two categories: visible persecution through public reproach, and solidarity with the persecuted by accompanying and supporting them at personal cost. Both required that the believers subordinate their reputation and safety to their allegiance to Christ and to one another.</p>",
            "voices": [
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>\"Whilst ye were made a gazingstock\" — literally, being exposed in the theatre. Here also it is probable that the word has only a figurative sense, as in 1 Corinthians 4:9. The theatrical image captures the public and deliberate nature of the humiliation, performed before a hostile audience.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p><em>Theatrizomenoi</em> — ye were exhibited as wild beasts and other shows at the theatres. See the note on 1 Corinthians 4:9, where all this is illustrated. Companions of them that were so used — those who stood alongside the persecuted, sharing their disgrace at personal cost.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>The affliction consisted partly in being made a public spectacle — held up to public view and scorn — and partly in accompanying and supporting those who suffered directly, becoming partners in their reproach rather than stepping away to security. Both demanded loyalty to Christ over reputation.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "34": {
            "synthesis": "<p>The solidarity the readers showed in their earlier sufferings is now specified in two concrete acts: compassion for those in bonds, and joyful acceptance of the spoiling of their own goods. Ellicott draws attention to a significant textual variant: the true reading of the first clause is not \"ye had compassion of me in my bonds\" but \"ye had sympathy with them that were in bonds\" — a change that removes a specific reference to the writer's own imprisonment and makes the statement a general testimony to their solidarity with all who suffered. Ellicott notes this change is important in connection with questions of authorship. Calvin highlights the greater sign: taking joyfully the spoiling of goods. To be stripped of possessions without bitterness, with positive joy, is not natural endurance but supernatural grace — rooted in the certainty that the believers possessed in themselves a heavenly substance that no confiscation could touch. Clarke takes the personal reading as a reference to Paul's long imprisonment in Caesarea or Rome, which the Jerusalem believers supported through their sympathy and practical help. Barnes focuses on the inner disposition: they took the spoliation joyfully, knowing that they had an enduring possession in heaven — and it is exactly this disposition that the writer now summons them to maintain.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>To take joyfully the spoliation of goods is not the result of natural endurance but of supernatural grace — rooted in the certainty that the believers possessed in themselves a heavenly substance that no confiscation could reach. This joy is the sign that their hope was genuinely anchored beyond what could be taken.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Rather, according to the true reading, <em>for ye had sympathy with them that were in bonds</em> — not \"with me.\" The change of reading is very important in connection with questions of authorship. The statement becomes a general testimony to their solidarity with all who suffered for Christ.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>Ye sympathized with the prisoners — probably referring to Paul's long imprisonment in Caesarea or Rome — and ye received joyfully the loss of your own goods, knowing that you had in heaven a better and an enduring substance than all that could be stripped away.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>For ye sympathized with all your suffering brethren; and received joyfully the loss of your own goods — because you knew that the possession awaiting you in heaven was better and more enduring than all that men could confiscate from you on earth.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "35": {
            "synthesis": "<p>\"Cast not away therefore your confidence (<em>parresia</em>), which hath great recompence of reward.\" The word <em>parresia</em> has appeared already in this chapter (v.19) and earlier in the epistle (3:6, 4:16) — it is the bold, frank, open access and confidence that belongs to those in Christ. Ellicott draws the direct contrast: to \"cast away\" this boldness is the opposite of \"holding fast the boldness of the hope\" called for in 3:6; the one belongs to faithful endurance, the other to apostasy. Calvin makes the connection explicit: confidence is itself the foundation of a godly and holy life — not merely a desirable attitude but the structural basis on which perseverance rests. To lose it is to lose the thing that makes continued faithfulness possible. Clarke gives the phrase its richest translation: the <em>parresia</em> they must not cast away is their \"liberty of access to God; your title and right to approach his throne; your birthright as his sons and daughters.\" Wesley states the practical reality simply: faith and hope are the confidence in question, and no one can take them away except the believers themselves. Barnes adds the motivational element: the recompense is great — the suffering endured for Christ does not go unrecorded, and the reward proportioned to it awaits.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He shows what especially makes us strong to persevere — the retaining of confidence; for when that is lost, we lose the recompense set before us. It hence appears that confidence is the foundation of a godly and holy life; to lose it is to lose the structural basis on which all perseverance rests.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>\"Cast not away therefore your boldness, seeing it hath a great recompence.\" To \"cast away boldness\" is the opposite of \"holding fast the boldness of the hope\" in Hebrews 3:6; the one belongs to the endurance of the faithful, the other to the retreat that the whole chapter has been warning against.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p><em>Ten parresian hymon</em> — your liberty of access to God; your title and right to approach his throne; your birthright as his sons and daughters; and the clear evidence you have of his favour. Cast not this away — it is far too valuable to surrender for any earthly consideration.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>Cast not away your confident hope in God. The recompense is great — the suffering endured for Christ does not go unrecorded or unrewarded. The motivation to hold on is not merely perseverance for its own sake but the certainty of a proportioned and enduring reward.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "36": {
            "synthesis": "<p>Patience (<em>hypomone</em>) — the endurance that actively bears what cannot be changed — is declared necessary, and the reason is given: after doing the will of God, to receive the promise. The sequence is deliberate: first the doing of the will, then the receiving of the promise, and in between the patience that bridges them. Calvin notes that Satan has innumerable arts by which he harasses those who seek to persevere, and hence extraordinary patience is needed — not a passive waiting but an active resistance to a thousand different pressures to give up before the finish. Ellicott connects this verse directly with the general exhortation in chapter 6 (vv.9-20), where a similar combination of doing and waiting appears. Clarke draws the practical distinction: God furnishes the grace of patience as a principle; the believer must exercise it. The grace is given; the work of deploying it belongs to the human will and effort in cooperation with God. Barnes gives the experiential grounding: patience is needed because of the natural disposition to murmur; because human nature sinks under prolonged suffering; and because trials are often extended far longer than expected. The promise is certain — but the path to receiving it runs through the discipline of patient continuance in the will of God.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He says that patience is necessary, not only because we have to endure to the end, but as Satan has innumerable arts by which he harasses us; and hence except we possess extraordinary patience, we shall a thousand times be broken down before we come to the goal.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>\"Patience\" — brave, patient endurance. The general strain of the exhortation in Hebrews 6:9-20 closely resembles these verses. The sequence is deliberate: doing the will of God, then patience, then receiving the promise. The middle term — endurance — is what bridges the doing and the receiving.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>Having so great a fight of sufferings to pass through. God furnishes the grace; you must exercise it. The grace or principle of patience comes from God; the use and exercise of that grace belong to the believer — cooperation of divine provision and human effort.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>We have need of patience because there is in us so much disposition to murmur and repine; because our nature is liable to sink under sufferings; and because our trials are often protracted far beyond what we anticipated. The promise is certain; the path to it runs through patient continuance in the will of God.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "37": {
            "synthesis": "<p>\"For yet a little while, and he that shall come will come, and will not tarry.\" The citation blends Isaiah 26:20 with Habakkuk 2:3-4, and the combined effect is to shorten the horizon dramatically. What seems like an indefinite future is declared to be \"a very little while\" — <em>mikron hoson hoson</em>, an intensive reduplication that Ellicott notes is unusual and emphatic. Calvin observes that hope of a speedy end avails greatly to sustain minds that are beginning to faint; the knowledge that the waiting is bounded, not open-ended, is itself a support. Clarke applies the coming of Christ in the immediate horizon to the judgment upon Jerusalem — the overflowing scourge determined because the measure of rebellion is full — while also holding open the final eschatological horizon. Barnes suggests the allusion may be to John 16:16 or to Habakkuk directly; he understands the coming in terms appropriate to Habakkuk's context — the vindication of the faithful amid national catastrophe. Wesley simply identifies the coming one as \"he that cometh — to reward every man according to his works.\" In every reading the point is the same: the delay is bounded, the coming is certain, and the brevity of the interval is itself a call to steadiness.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>That it may not be grievous to us to endure, he reminds us that the time will not be long. There is nothing that avails more to sustain our minds, should they at any time become faint, than the hope of a speedy and near termination. The bounded interval is itself a support to endurance.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>Rather, <em>a very little while.</em> The expression is remarkable and unusual; <em>mikron hoson hoson</em> is intensive reduplication. \"Ye have need of endurance\" — for the end is not yet; but \"a very little while,\" far shorter than it feels, and the Coming One will not delay.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>For yet a very little time — in a very short space of time the Messiah will come and execute judgment upon the rebellious country. This is determined because they have filled up the measure of their iniquities. The coming in view is the vindication of the faithful by divine judgment on their persecutors.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>There seems to be an allusion here either to John 16:16 or more probably to Habakkuk 2:3: \"For the vision is yet for an appointed time, but at the end it shall speak, and not lie.\" In either case, the interval is declared to be brief and the arrival certain.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        },
        "38": {
            "synthesis": "<p>The Habakkuk quotation continues: \"Now the just shall live by faith: but if any man draw back, my soul shall have no pleasure in him.\" Two things are asserted in sequence: the life of the righteous person is sustained by faith; and if he draws back, God disowns him. The first clause is one of the great Pauline texts (quoted also in Romans 1:17 and Galatians 3:11), but the second clause here creates a genuine tension among the commentators. Ellicott argues for reading \"my righteous one shall live by faith\" with the possessive — God's own righteous one — which makes the disowning of the one who draws back all the more stark. Calvin reads the verse through the lens of perseverance: faith is what sustains the contests, and hence drawing back (<em>hypostole</em>) is the failure of faith, not merely a moral lapse. Barnes understands the verse in Habakkuk's context: the righteous person survives judgment by holding to God in faith, while the one who draws back is destroyed by the very judgment they sought to escape. Wesley shows his Arminian conviction explicitly: \"the just — the justified person. Shall live in God's favour, a spiritual and holy life. By faith — as long as he retains that gift of God. But if he draw back — if he make shipwreck of his faith — My soul hath no pleasure in him — That is, I abhor him; I cast him off.\" For Wesley, a genuinely justified person who abandons faith is genuinely cast off; Calvin would say that true perseverance is itself the mark of genuine election, and the one who draws back thereby shows the faith was not genuine.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>He means that patience is born of faith; and this is true, for we shall never be able to carry on our contests unless we are sustained by faith — even as John truly declares that our victory over the world is by faith. Drawing back is therefore the failure of the very thing that makes endurance possible.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>It is probable that the word \"my\" should be added: <em>But my righteous one shall live by faith.</em> The possessive makes the disowning of the one who draws back all the more stark — God explicitly claims the righteous person as his own, and explicitly disowns the one who shrinks back.</p>"
                },
                {
                    "src": "wesley",
                    "attr": "John Wesley's Notes",
                    "html": "<p>Now the just — the justified person. Shall live in God's favour, a spiritual and holy life. By faith — as long as he retains that gift of God. But if he draw back — if he make shipwreck of his faith — My soul hath no pleasure in him; that is, I abhor him; I cast him off.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>In accordance with the sense in which it was used by Habakkuk, the meaning is that the righteous person will be preserved through times of judgment and catastrophe by faith — by maintaining hold on God — while the one who shrinks back from that trust is destroyed by the very judgment they sought to escape.</p>"
                }
            ],
            "consensus": "divided",
            "key_tension": "Calvin treats drawing back as evidence that the faith in question was never genuine — a truly elect believer cannot finally apostatize; Wesley treats it as the genuine and total fall of a genuinely justified person who has made shipwreck of real faith, resulting in God's actual abandonment of him."
        },
        "39": {
            "synthesis": "<p>The chapter closes not on the warning but on the confession — and the writer includes himself in it. \"But we are not of them who draw back unto perdition; but of them that believe to the saving of the soul.\" Calvin observes that the writer uses the Habakkuk quotation wisely: having warned against the possibility of drawing back, he now expresses full confidence that those he addresses belong to the other company — the company of faith. The warning was not an accusation but a fence; the confession here is both pastoral encouragement and theological location. Ellicott notes the literal rendering: \"But we are not of drawing back unto perdition, but of faith unto the gaining of the soul\" — the last phrase is nearly identical with Luke 17:33 and points toward the paradox that the one who seeks to save his life loses it, while the one who gives it for Christ gains it. Clarke gives the verse its sharpest edge in translation: \"we are not the cowards, but the courageous\" — arguing that the Greek form of the antithesis requires this rendering, and that what is contrasted is not only theological status but moral disposition under pressure. Barnes closes with pastoral confidence: the case of willful apostasy he has been describing was a supposable case, not one he believed would apply to his readers. They are, in his settled conviction, of the company of those who believe — to the full and final preservation of the soul.</p>",
            "voices": [
                {
                    "src": "calvin",
                    "attr": "Calvin's Commentaries",
                    "html": "<p>The Apostle made a free use of the Greek version most suitable to the doctrine he was discussing; and he now wisely applies it. He had before warned them lest by forsaking the Church they should alienate themselves from the faith — and now he expresses confidence that they belong to the company of faith, not of retreat.</p>"
                },
                {
                    "src": "ellicott",
                    "attr": "Ellicott's Commentary",
                    "html": "<p>\"But we are not of drawing back unto perdition, but of faith unto the gaining of the soul.\" The last words are nearly identical with those of Luke 17:33, though deeper in meaning: the soul that is gained is the self found precisely in the act of surrendering all for Christ.</p>"
                },
                {
                    "src": "clarke",
                    "attr": "Adam Clarke's Commentary",
                    "html": "<p>\"We are not the cowards, but the courageous.\" I have no doubt of this being the meaning of the apostle, and the form of speech requires such a translation. What is contrasted here is not merely theological category but moral disposition — the brave versus the fearful — under the pressure of persecution.</p>"
                },
                {
                    "src": "barnes",
                    "attr": "Barnes' Notes",
                    "html": "<p>In this the apostle expresses the fullest conviction that none of those to whom he wrote would apostatize. The case which he had been describing was only a supposable case, not one which he believed would occur. They are, he is confident, of the company that believes — to the full and final preservation of the soul.</p>"
                }
            ],
            "consensus": "affirm",
            "key_tension": None
        }
    }
}

def main():
    existing = load_synthesis('hebrews')
    merge_synthesis(existing, HEBREWS)
    save_synthesis('hebrews', existing)
    print('Hebrews 10 synthesis complete.')

if __name__ == '__main__':
    main()
