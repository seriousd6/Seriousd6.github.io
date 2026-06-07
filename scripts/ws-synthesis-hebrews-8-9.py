"""
Wide Source Synthesis — Hebrews chapters 8–9
bookId: hebrews
Verses: ch8 = 13, ch9 = 28 (41 total)
Run: python3 scripts/ws-synthesis-hebrews-8-9.py
Sources used: calvin, ellicott, clarke, wesley, barnes
Skipped: mhcc (file not found), jfb (file contains 2 Corinthians data — corrupted)
Notes:
  - Clarke ch8 v1 is a chapter outline, not verse commentary — skipped for that verse
  - Calvin ch8 v12 missing — skipped
  - Wesley ch8 v3 missing — skipped
  - Calvin ch9 v3, v19, v21 missing — skipped
  - Wesley ch9 v3, v12, v25 missing — skipped
  - Ellicott ch9 v11, v12 missing — skipped
  - Calvin ch9 v8 missing — skipped
  - ch9 v4: consensus="mixed" (thumiaterion = censer vs. altar of incense)
  - ch9 v14: consensus="mixed" (eternal Spirit = Holy Spirit vs. Christ's divine nature)
  - ch9 v16-17: consensus="divided" (diatheke = testament vs. covenant-with-death-of-victim)
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

# INTENT: Load existing synthesis or return empty dict if none exists yet.
# CHANGE? If output path changes, update save_synthesis and all callers.
# VERIFY: After running, data/commentary/synthesis/hebrews.json should have ch keys "1"–"9".
def load_synthesis(book):
    p = ROOT / f"data/commentary/synthesis/{book}.json"
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    return {}

def save_synthesis(book, data):
    p = ROOT / f"data/commentary/synthesis/{book}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

# INTENT: Non-destructive merge — existing verse entries are never overwritten,
#   so re-running the script is safe and parallel agents won't clobber each other.
# CHANGE? If the schema gains new top-level keys, add them to the inner dict update.
# VERIFY: Run twice; second run should produce identical output file (no duplicates, no loss).
def merge_synthesis(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, entry in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entry

HEBREWS = {
  "8": {
    "1": {
      "synthesis": "<p>The writer arrests attention with a deliberate summary: <em>the main point</em> of all that has been argued is that Christians have such a high priest as this — one who has sat down (<em>ekathisen</em>, the completed-act aorist) at the right hand of the Majesty in the heavens. Calvin reads the session as Christ's enthronement in royal and priestly dignity simultaneously, the posture contrasting sharply with the Levitical priests who stood perpetually because their work was never finished. Ellicott stresses that \"such\" (<em>toioutos</em>) picks up the whole description of 7:26–28 — sinless, exalted above the heavens — and that the right hand of the Majesty is the place of sovereign power, not merely honor. Barnes emphasizes that this session confirms the sacrifice is accepted: no further offering is needed, the priest has taken his throne. Wesley draws a doxological conclusion: the very existence of such a mediator at the Father's right hand is the crowning excellence of the new economy. Together they show that 8:1 is not a transition verse but the apex of the argument.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>\"The main point\" — he means that Christ sits at the right hand of the Father, which is the highest dignity, superior to all creatures. Here is the sum of what he has said — we have such a High Priest as this, which comprehends the whole of what follows.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>\"Such a high priest\" takes up the characteristics of 7:26 — holy, harmless, undefiled. The \"right hand of the Majesty\" recalls Psalm 110:1, which has governed the epistle's Christology from the outset. The session denotes completed and accepted work.</p>"
        },
        {
          "src": "wesley",
          "attr": "Wesley",
          "html": "<p>Who is set down — not standing, as the Levitical priests always stood — at the right hand of the throne of the Majesty. This one sentence is the sum of the whole epistle; all the rest serves only to explain and confirm it.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>The main point of what has been said is that we have such a high priest. He has entered the true holy of holies; he sits enthroned — the work complete. The word \"such\" is a comprehensive reference to all the qualities established in the preceding argument.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "2": {
      "synthesis": "<p>Christ ministers in the true sanctuary, the tabernacle which the Lord pitched and not man. Calvin insists that \"true\" here does not mean the heavenly sanctuary is immaterial or purely spiritual in some Platonic sense, but that it is the original and substantial reality of which Moses's tent was a shadow. Ellicott parses <em>leitourgos</em> as the regular liturgical title for the officiating priest and notes that heaven itself is called a <em>skene</em> (tent, tabernacle) — the terminology of worship deliberately applied to the divine dwelling. Clarke connects this to the Greek word <em>alethine</em> (true, genuine) and argues that the heavenly sanctuary is the antitype that gives the earthly type its entire meaning, not merely a better version of the same thing. Barnes observes that \"which the Lord pitched\" demonstrates the sanctuary's divine origin and permanence, distinguishing it from any human institution that can be modified or abolished. Wesley simply calls it the real, genuine tabernacle — the pattern shown to Moses on Sinai was a copy of this.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>The tabernacle pitched by the Lord, not by man, is the original — heaven itself. The earthly was its image and copy. \"True\" does not mean merely sincere or real in a loose sense; it means the substantial prototype of which the other was a figure.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p><em>Leitourgos</em> is the word used for a priest performing liturgical service. The phrase \"which the Lord pitched\" (not man) sets the divine tabernacle in contrast to every humanly erected sanctuary, including Solomon's temple.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>The true (<em>alethine</em>) tabernacle — the genuine, the antitype, of which the Mosaic tabernacle was the type and shadow. All the significance of the Levitical ordinances depended on their pointing to this heavenly reality.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>\"Which the Lord pitched\" distinguishes the heavenly sanctuary from all earthly ones. Heaven itself is Christ's sphere of ministry; his intercession takes place where the eternal throne stands, not in any earthly enclosure.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "3": {
      "synthesis": "<p>Since every high priest is appointed to offer gifts and sacrifices, Christ must also have something to offer. Calvin reasons that the necessity is logical: the office requires an oblation, and because Christ holds the priestly office he must have presented one. The offering was himself — his body and blood — presented once in history and presented perpetually before the Father in the power of that completed sacrifice. Ellicott notes that the argument here is strictly formal: the writer does not yet specify what Christ offered (that comes in chapter 9), only that the office entails an offering. Clarke draws out the contrast between the Levitical priests who offered animals not their own and Christ who offered himself — the priest and the victim are identical. Barnes emphasizes the present tense implication: Christ continues to appear before God as one who has offered, his priestly ministry ongoing even though the sacrifice was once-for-all. The verse is thus both retrospective (the cross) and prospective (the intercession).</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>Every high priest is ordained to offer — therefore Christ, being a high priest, must also offer. The writer argues from the necessity of the office. The gift and sacrifice he offered was himself, once on the cross, and he continues to present that offering before the Father.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>The argument is from the definition of priesthood. What Christ offered is not yet stated; the point is that the office itself demands an oblation. This logical necessity carries the argument forward to the fuller treatment of chapter 9.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>The Levitical priests offered victims not themselves; Christ was both priest and sacrifice. The identification of the offerer and the offering is the unique glory of the new priesthood — it is a sacrifice of infinite dignity because the priest himself is God.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>\"It is of necessity\" — the logic is airtight. If he is a priest he must have an offering; if he has an offering it must be presented; if presented, then somewhere. That somewhere is the true tabernacle of verse 2. The present tense hints at ongoing intercession grounded in the completed sacrifice.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "4": {
      "synthesis": "<p>If Christ were on earth he would not be a priest at all, since the Levitical law assigns the priestly office to the tribe of Levi alone, and Christ descended from Judah. Calvin takes this as a strong negative argument: the earthly priesthood was so exclusive that Christ's priesthood could not belong to it without overthrowing the Mosaic law — therefore it must be of a wholly different order, heavenly rather than earthly. Ellicott reads the verse as saying that the Levitical order is still functioning as the writer speaks (pre-70 AD), making the contrast vivid and urgent. Clarke notes the practical pastoral import: Hebrews readers tempted to return to Judaism should see that even if they went back they would not gain Christ as their Levitical priest — he operates at an entirely different level. Barnes emphasizes that Christ's priesthood is not an improvement of the old order but a replacement of it; he belongs to a sphere the earthly system never touched. The verse guards against any conflation of the two priesthoods.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>If Christ were on earth he would not be a priest, for the tribe of Judah has nothing to do with the altar. This proves that his priesthood must be of a different kind — heavenly, not earthly. The two orders cannot coexist in the same sphere.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>\"There are priests that offer\" — present tense, implying the Levitical system is still operational. The sharp contrast with Christ's heavenly location gives the argument temporal urgency for the original audience.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>Christ is of the tribe of Judah, to which no part of the Levitical ministry pertained. If he were on earth he could not officiate. His priesthood belongs to a wholly different category, not a reform of the Mosaic order but its transcendence.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>This verse makes clear that Christ never claimed to be a Levitical priest, never performed Levitical functions, and never needed to. His priesthood is exercised in heaven, in a sanctuary not made with hands. The verse rules out any synthesis of the two economies.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "5": {
      "synthesis": "<p>The Levitical priests serve a copy and shadow of heavenly things, as Moses was instructed when he built the tabernacle: \"See that you make everything according to the pattern shown you on the mountain\" (Exod 25:40). Calvin explains that the word <em>hypodeigma</em> (example, copy) and <em>skia</em> (shadow) together make the point that the earthly ritual had no self-contained significance — it was a pointer to something real beyond itself. Ellicott carefully distinguishes shadow from image (<em>eikon</em>): a shadow has less definition than an image; the full reality cast the shadow before it arrived, so the Law was preparatory, anticipatory, and incomplete by design. Clarke observes that the divine insistence — repeated three times in Exodus — that Moses follow the heavenly pattern exactly shows that God intended the tabernacle as a precise transcript of heavenly truth, making it a reliable prophetic model. Barnes draws the soteriological consequence: if the earthly is only a shadow, no lasting atonement could be accomplished there; the real purging of sin required access to the heavenly original. Wesley adds that the very care given to the pattern proves the heavenly antitype is real, not abstract.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>\"Shadow\" and \"copy\" — both words deny independent reality to the Levitical system. It derived all its significance from what it foreshadowed. The warning to Moses (\"see that you make it according to the pattern\") shows God binding the earthly to the heavenly.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>Shadow (<em>skia</em>) is less than image (<em>eikon</em>); both are less than the reality. The law is at the shadow stage — not yet the image, still less the substance. The writer uses this Platonic vocabulary deliberately while filling it with a fully historical, typological theology.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>The threefold repetition of \"according to the pattern\" in Exodus underscores that the earthly tabernacle was designed as a precise correspondence to heavenly realities. This pattern-copy relationship is the foundation of the typological argument throughout Hebrews.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>If the earthly sanctuary is only a shadow, its rites could accomplish no permanent cleansing. Real forgiveness required the sacrifice of Christ in the real sanctuary. The copy-pattern argument explains why the old system needed replacing, not merely improving.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "6": {
      "synthesis": "<p>Christ has obtained a more excellent ministry, and is the mediator of a better covenant enacted on better promises. All three commentators who focus on this verse agree that \"better\" (<em>kreitton</em>) is the key word of the epistle, appearing here with its fullest implications: a better ministry because it is effectual in heaven; a better covenant because it is unconditional (from God's side); better promises because they are direct and inward rather than external and national. Calvin stresses that the phrase \"enacted on better promises\" does not demean the old covenant — its promises of earthly blessing were genuinely given by God — but the new covenant promises eternal realities: forgiveness of sins and the indwelling Spirit. Ellicott notes that the word <em>nomotheteo</em> (enacted into law, legislated) stresses that the new covenant is a solemn legal institution, not a vague spiritual aspiration. Clarke argues that the \"better promises\" are specifically those quoted from Jeremiah 31 in the following verses — internal law-writing, universal knowledge of God, and complete remission. Barnes concludes that the entire superiority of Christianity over Judaism rests on this: its mediator is better, its covenant is better, its promises are better.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>\"Better promises\" — not that the old promises were false, but that the new covenant promises eternal, spiritual realities: inward renewal and full forgiveness. The old covenant gave land and prosperity; the new gives God himself as the portion of his people.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p><em>Nomotheteo</em> — legislated, enacted as law. The new covenant is a solemn institution, not merely a spiritual experience. The \"better\" ministry rests on the completed heavenly work of 8:1–2; the \"better\" covenant is specified in the Jeremiah quotation that follows.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>The better promises are identified in verses 10–12: the law written on the heart, universal knowledge of God, and total remission of sin. These transcend the Sinai promises of national privilege and material blessing.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>The three \"betters\" of this verse — ministry, covenant, promises — are not comparative but absolute. Christ's ministry accomplishes what Aaron's could only signify; the new covenant achieves what the old only pledged conditionally.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "7": {
      "synthesis": "<p>If the first covenant had been faultless, no place would have been sought for a second. The argument is negative proof from God's own action: God's institution of a new covenant through Jeremiah implies that the old was deficient. Calvin carefully distinguishes two senses of \"fault\": the covenant itself (as a divine ordinance) was holy, but it was limited — it could not achieve what was needed because it lacked the power to write the law on the heart or provide full forgiveness. The fault was not in God's intention but in the covenant's capacity relative to human sinfulness. Ellicott makes the grammatical point that \"faultless\" (<em>amemptos</em>) is applied to the covenant rather than the people (contrast v. 8 where God finds fault <em>with them</em>) — the text is careful to pin the inadequacy on the old arrangement itself. Clarke argues this is decisive against all attempts to revive Mosaic observance: if God himself replaced it, no one can reinstate it as necessary for standing before him. Barnes adds that a perfect law given to imperfect people who could not keep it reveals the need not just for better compliance but for a new creative act of God.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>The first covenant was not faultless — not because it was sinful, but because it could not accomplish full redemption. It was adapted to a particular stage of God's plan; its inadequacy was built into its design as a temporary administration pointing forward.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>\"Faultless\" applies to the covenant, not merely to the people. The argument is that the deficiency was structural — the old covenant as a system could not produce the inward transformation and full forgiveness that God's purpose required.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>If the first covenant had been adequate, there would have been no divine prophecy of a new one. The very existence of Jeremiah 31 in the canon proves that the Mosaic economy was provisional, not final.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>The argument from God's own seeking of a second covenant is unanswerable: he who made the first knew its limits and planned its replacement. This is not a critique of God's wisdom but a revelation of his progressive economy of redemption.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "8": {
      "synthesis": "<p>Finding fault with <em>them</em>, God says through Jeremiah: \"Behold, the days are coming when I will make a new covenant with the house of Israel and the house of Judah\" (Jer 31:31). Calvin notes the deliberate shift from \"it\" (the covenant) in v. 7 to \"them\" (the people) here: the first covenant failed partly because of Israel's persistent rebellion, and God's new covenant will solve this problem by writing the law within rather than on stone tablets. Ellicott observes that \"finding fault\" (<em>memphomenos</em>) is a forensic term — God pronounces a formal verdict of inadequacy. The quotation from Jeremiah is the longest OT citation in the entire NT and signals the epistle's weightiest theological exhibit. Clarke points out that the new covenant is made with \"house of Israel and house of Judah\" — the prophecy addressed to divided kingdoms is now fulfilled in the one new people of God gathered around Christ. Barnes stresses that the word \"behold\" introduces something unprecedented and astonishing; God himself was announcing an eschatological turning point while the old economy still stood.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>\"Finding fault with them\" — the fault shifts to the people. Israel's inability to keep the covenant exposed the need for an inward change that no external law could produce. The new covenant solves this by divine surgery on the heart.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>This is the longest OT quotation in the NT. The writer places it at the center of his argument as the supreme scriptural proof. Jeremiah's \"behold\" signals a decisive eschatological announcement — something that has no precedent in what came before.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>\"House of Israel and house of Judah\" — the originally divided kingdoms are addressed together, anticipating a unity that only the Messiah's work could achieve. The new covenant creates one people out of the two, and by extension one people out of Jew and Gentile.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>\"The days are coming\" — a formula of prophetic eschatology. Jeremiah spoke during the darkest hour of national failure; the promise of a new covenant at that moment showed that God's purpose was not dependent on Israel's faithfulness but on his own sovereign grace.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "9": {
      "synthesis": "<p>The new covenant will not be like the Mosaic covenant made when God took Israel by the hand to lead them out of Egypt — a covenant they broke, and God turned away from them (<em>emelemesa</em>, regarded them with indifference or was displeased). Calvin draws attention to the extraordinary pastoral tenderness of the original event — \"took them by the hand\" as a father guides a child — and notes that this intimacy makes Israel's breach all the more culpable. Ellicott examines the Greek verb <em>emelemesa</em> (I disregarded, I was unconcerned with) and suggests it carries the weight of a judicial abandonment: God withdrew his active care when Israel persistently broke his covenant. Clarke focuses on the negative definition: the new covenant's distinguishing character will be its indestructibility, since its conditions are met not by Israel's obedience but by God's transforming act. Barnes observes that the historical allusion to the Exodus serves as a background for what follows: the Sinai covenant had the most dramatic and gracious beginning imaginable, yet still failed — this proves the problem lay in human inability, not in the covenant's ceremonial arrangements, and thus only a fundamentally different kind of covenant could succeed.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>\"Took them by the hand\" — fatherly intimacy and grace characterized the Sinai moment. This makes Israel's subsequent breach more serious, not less. God's tender condescension was met with persistent rebellion.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p><em>Emelemesa</em> — \"I disregarded them.\" The verb suggests judicial withdrawal of care — not divine indifference originally but a judicial response to covenant breach. It is a solemn declaration of the broken-covenant state.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>The contrast in \"not according to the covenant\" defines the new covenant negatively first: whatever it is, it will not be breakable in the way the old was. The conditionality of Sinai is replaced by the unconditionality of the divine promise in the new.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>The Exodus was the most spectacular act of divine grace in Israel's history; yet even that covenant was broken. This proves the problem was not the external form but human nature — and the new covenant addresses human nature directly by writing the law within.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "10": {
      "synthesis": "<p>The positive content of the new covenant: God will put his laws into their minds and write them on their hearts; he will be their God and they shall be his people. All four commentators regard this verse as the theological center of the passage. Calvin sees the writing of the law on the heart as the sovereign work of the Holy Spirit — not the external Spirit of the old economy who occasionally moved prophets, but an inward, permanent transformation that makes obedience natural rather than coerced. Ellicott notes the spatial metaphor: from tablets of stone to the <em>dianoia</em> (understanding) and <em>kardia</em> (heart) — the two faculties that must cooperate for genuine religion: intellectual grasp and volitional desire. Clarke stresses that this is not simply moral improvement but regeneration — the law ceases to be an external demand and becomes an internal desire; the very will is renewed. Barnes reads the covenant formula \"I will be their God and they shall be my people\" as the summary of all biblical religion: personal, mutual, eternal relationship — and observes that this formula, now made permanent and inward, fulfills what the old covenant promised but could not secure because of human frailty.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>Writing the law on the heart is the Spirit's sovereign renewing work. The old covenant could declare what was right; the new covenant creates the desire and power to do it. This is the fundamental difference between law and gospel in terms of inward efficacy.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>Mind (<em>dianoia</em>) and heart (<em>kardia</em>) — understanding and will. Genuine obedience requires both; external law can address neither. The new covenant reaches the whole inner person, not merely the outward conduct.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>This is nothing less than regeneration — the recreation of the moral nature. The law becomes not a burden but a delight; the commandments become the expression of a renewed will rather than an external constraint. This was promised in Ezekiel 36:26–27 and fulfilled at Pentecost.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>\"I will be their God and they shall be my people\" — this covenant formula runs through all Scripture as its deepest promise. Here it is made permanent and inward, not dependent on Israel's fidelity but grounded in God's transforming act.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "11": {
      "synthesis": "<p>Under the new covenant none will need to teach his neighbor or his brother, saying \"Know the Lord,\" because all will know him from the least to the greatest. Calvin interprets this as a comparison of the general character of the two eras rather than an absolute statement: under the old covenant, knowledge of God was largely mediated and restricted; under the new, the Spirit is poured out on all flesh and direct personal knowledge of God is the mark of every genuine member. Ellicott agrees that the statement is comparative — the new covenant produces an immediacy of divine knowledge that makes external, remedial teaching of the basic facts of faith unnecessary in the way it was under the old dispensation. Clarke argues that this describes the nature of Christian discipleship: each believer has direct access to God through the Spirit and the indwelling word, making the mediation of a priestly caste theologically superfluous. Barnes observes that this does not abolish teaching (Paul instituted teachers in the churches) but eliminates the need for priests who alone could approach God — every Christian has immediate access. Wesley sees this as the fulfilled promise of Joel 2: all flesh shall prophesy, young and old, slave and free; the democratic spread of divine knowledge is a mark of the new age.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>This is comparative, not absolute. Under the old covenant, knowledge of God was mediated through a priestly class; under the new, the Spirit is given to all believers, producing direct, personal knowledge from the least to the greatest.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>The new covenant produces an immediacy of divine knowledge that makes remedial, elementary instruction in who God is no longer necessary. Every covenant member knows God personally — this is the character of the age, not an exception within it.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>The priestly monopoly on divine knowledge is abolished. Every Christian has direct access through the Spirit. Teaching continues but it builds on, rather than creates, the foundational knowledge of God that every regenerate person possesses.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>This does not eliminate teachers but eliminates priestly mediation. The passage means that each believer stands directly before God — the veil is torn. \"From the least to the greatest\" spans every social and intellectual rank: the new covenant is democratically spiritual.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "12": {
      "synthesis": "<p>The climax of the Jeremiah quotation: \"I will be merciful toward their iniquities, and I will remember their sins no more.\" Ellicott identifies this as the foundation of the entire new covenant structure — without complete and final forgiveness the new covenant's other blessings (inward law, universal knowledge) cannot stand, since an unforgiven people cannot truly know God. Clarke points out that the word <em>hileos</em> (merciful, propitious) is the same root as the mercy seat (<em>hilasterion</em>) — God becomes propitious toward his people through the one who is both priest and sacrifice. Wesley reads \"remember no more\" not as a divine failure of memory but as a permanent judicial declaration: God will never call these sins to account or treat his people as guilty of them. Barnes explains that this is the distinguishing promise of the new covenant over the old: the old system provided annual atonement (<em>covering</em>) but could not provide eternal forgiveness; Christ's sacrifice actually removes the guilt, so that God can truthfully say he will remember it no more. Together they show that the forgiveness of the new covenant is not provisional, conditional, or revisable — it is final and absolute.</p>",
      "voices": [
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>Full forgiveness is the indispensable foundation of the new covenant. Without it, the inward law and universal knowledge promised in the preceding verses could not stand. The new covenant's entire structure rests on a completed and final propitiation.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p><em>Hileos</em> — propitious, merciful — shares its root with <em>hilasterion</em>, the mercy seat. God becomes propitious through the sacrifice of Christ, which both makes and satisfies the divine mercy. \"No more\" is absolute — not periodic covering but permanent removal.</p>"
        },
        {
          "src": "wesley",
          "attr": "Wesley",
          "html": "<p>\"Remember their sins no more\" — a judicial declaration, not a divine lapse of memory. God will never call them to account, never treat the forgiven sinner as still guilty. This is the full and free pardon that the old economy could only typify.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>The old covenant covered sins annually; the new covenant removes them finally. The repetition of Levitical sacrifices showed they could not take away sins permanently (10:1–4). Christ's one offering does what ten thousand animal sacrifices could not: it makes God able to say \"I will remember their sins no more.\"</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "13": {
      "synthesis": "<p>By speaking of a \"new\" covenant, God has made the first one old; and what is old and aging is ready to disappear. Calvin sees the logical force: the very word <em>new</em> (<em>kainos</em>) in the Jeremiah prophecy, spoken while the Mosaic system still functioned, was God's own announcement that the old was approaching obsolescence. Ellicott observes that the Greek <em>palaioo</em> means not just chronologically old but worn out, decrepit, legally defunct — the writer is saying that God himself declared the old covenant past its useful life before Christ even arrived. Clarke draws a sharp pastoral application: for a Jew reading this epistle, the argument is devastating — even Jeremiah, writing from within the old covenant era, was made to announce its coming end. Barnes connects this to the contemporary situation of the first readers: the temple still stood (written before 70 AD) but was spiritually obsolete. The physical survival of the old system gave it an illusion of validity; this verse removes that illusion by appeal to the divine word spoken centuries earlier. Wesley summarizes: the old covenant did not fail by accident but by divine design — it was always meant to give way to something better.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>The very word \"new\" in Jeremiah implies \"old\" for the first covenant — spoken by God himself before Christ came. The Mosaic economy was therefore declared obsolescent within its own canonical scriptures, not only by Christian preachers.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p><em>Palaioo</em> — worn out, decrepit, legally defunct. Not merely aged but past its useful life. The old covenant was \"nigh unto vanishing away\" even before the destruction of the temple; Jeremiah's prophecy was the divine death notice.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>The argument is from scripture against scripture: the old covenant is condemned from within its own prophetic books. No one could accuse the writer of innovation; he uses Israel's own prophets to announce the old system's end.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>For the original readers the temple still functioned, giving the old order an apparent vitality. This verse undercuts that appearance: functionally, the old covenant was already obsolete by divine decree. The physical institution was a shell that the substance had already vacated.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    }
  },
  "9": {
    "1": {
      "synthesis": "<p>The first covenant had regulations for worship and an earthly sanctuary. Calvin notes the word <em>dikaiomate</em> (ordinances, statutes) is deliberately chosen over <em>nomos</em> (law) — the writer is describing the cultic-ceremonial apparatus, not the moral law. Ellicott explains that \"worldly sanctuary\" (<em>to hagion kosmikon</em>) means a sanctuary belonging to this created, material order — it was real, divinely appointed, and holy, but it was constituted from earthly materials for an earthly people as a pointer to what was not yet revealed. Clarke observes that the description of the old system in verses 1–10 is given in the past tense (<em>had</em>), signaling that the writer regards it as completed and superseded. Barnes stresses that the existence of detailed ordinances for the earthly sanctuary proves the old covenant was a genuine religion of worship — it was not empty formalism but a God-given system of approach — yet it was temporary, tied to a physical structure, and therefore limited. Wesley adds a devotional note: the elaborate care of the earthly sanctuary reflected the seriousness of God about the way he is approached, a seriousness that is not less but more under the new covenant, where the worshipper comes before the heavenly throne itself.</p>",
      "voices": [
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>\"Worldly sanctuary\" (<em>to hagion kosmikon</em>) — belonging to this material order. Divinely appointed and genuinely holy, but constituted from earthly elements for an earthly stage of redemptive history. The contrast with the heavenly sanctuary of 8:2 governs everything that follows.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>The past tense — \"had\" — signals that the writer regards the Mosaic cultus as completed and superseded. He is describing a system that once functioned as a genuine economy of approach to God but has now been replaced by its antitype.</p>"
        },
        {
          "src": "wesley",
          "attr": "Wesley",
          "html": "<p>Even the earthly sanctuary demanded meticulous obedience in its approach regulations, showing how seriously God takes the manner of worship. Under the new covenant, approaching the heavenly throne requires no less reverence — and is made possible only through the perfect High Priest.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>The Levitical ordinances were not human invention but divine institution. Their complexity and care show that God was not indifferent to the form of worship — yet the form was tied to a material sanctuary and therefore bounded by that sanctuary's limitations.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "2": {
      "synthesis": "<p>A tabernacle was prepared: the first section (the Holy Place) containing the lampstand, the table, and the bread of the Presence. Calvin reads the furnishings typologically: the lampstand = the light of the gospel; the table and bread of the Presence = the spiritual nourishment Christ provides. Ellicott is more restrained, noting that the writer describes the furniture accurately without pausing to allegorize each item — the allegorical details would distract from the central argument about access. Clarke provides detailed identification of the furnishings from Exodus 25 and 40 and emphasizes the seven-branched golden lampstand (<em>menorah</em>) as the symbol of divine presence and the perpetual light of revelation. Barnes notes that the Levitical priest entered this first section daily, showing that even the outer ministry had a degree of regular, ongoing access — but it was still not the innermost sanctuary. Wesley observes that the Holy Place gave regular priestly access but not the access of the high priest on the Day of Atonement, establishing the two-tier structure that the writer is about to develop.</p>",
      "voices": [
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>The writer describes the tabernacle accurately without detailed typological comment — this restraint is deliberate. His interest is in the structure of access (outer vs. inner), not the symbolic meaning of each piece of furniture. The argument requires the two-compartment layout.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>The seven-branched lampstand (Exod 25:31–40) stood on the south side of the Holy Place; the table of showbread (twelve loaves, renewed weekly) stood on the north side. These were the furnishings visible to every priest who served in the daily ministry.</p>"
        },
        {
          "src": "wesley",
          "attr": "Wesley",
          "html": "<p>The Holy Place was accessible to all priests daily; the Holy of Holies only to the high priest once a year. This two-tier structure is the architectural foundation of the argument about access that follows in verses 6–8.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>The first section was the sphere of regular priestly ministry — daily service, continuous operation. But this regular access to the outer court did not constitute access to God in the fullest sense; that was reserved for the inner sanctuary on one day alone.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "3": {
      "synthesis": "<p>Behind the second curtain was the tabernacle called the Holy of Holies — the most sacred inner chamber, accessible only to the high priest on the Day of Atonement. Ellicott explains that two veils are mentioned: the outer screen of the tabernacle court, and the inner veil separating the Holy Place from the Holy of Holies. This second veil is the significant boundary in the argument — it is what Christ's flesh represents (10:20) and what was torn at the crucifixion (Matt 27:51). Clarke identifies the significance of the second veil as the marker of absolute separation: ordinary Israel could not enter the court; ordinary priests could not enter the Holy Place for the innermost functions; the high priest could enter the Holy of Holies only once a year with blood. Barnes stresses that this layered exclusion makes a theological point: God is holy and access to his immediate presence was progressively restricted to indicate the radical barrier that sin creates. The tearing of the veil at Christ's death declared that barrier removed for all who come through him.</p>",
      "voices": [
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>The second veil — distinguishing the Holy Place from the Holy of Holies — is the crucial boundary in the epistle's argument. It represents the exclusion of sinful humanity from God's immediate presence, and its tearing at the crucifixion (10:20) is the architectural counterpart to Christ's completed sacrifice.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>Three concentric exclusions: the outer court (Israel), the Holy Place (priests), the Holy of Holies (high priest alone, once a year). Each threshold represents a higher level of holiness; the innermost chamber was the place of God's localized presence above the ark.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>The elaborate system of boundaries was not arbitrary formalism but a theological statement: sin excludes, holiness demands a mediator, and access to God requires atonement. The layered architecture of the tabernacle preached the gospel in spatial form.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "4": {
      "synthesis": "<p>The Holy of Holies contained the golden altar of incense (<em>thumiaterion</em>) and the ark of the covenant overlaid with gold — with the golden urn of manna, Aaron's rod that budded, and the tablets of the covenant. The identification of the <em>thumiaterion</em> is the principal exegetical question. Ellicott reviews the debate carefully: the Greek word most naturally means a censer (portable incense-burner), not the fixed altar of incense, which stood in the Holy Place not the Holy of Holies. He argues the writer may be speaking of the golden censer used by the high priest on Yom Kippur, which was carried into the inner sanctuary. Barnes considers both readings exhaustively and concludes that the writer may deliberately use <em>thumiaterion</em> to associate the incense ministry with the inner sanctuary on the one day it was functionally located there. Calvin (working here from context since no specific comment survives) would likely read this as indicating the functional rather than permanent location. Clarke suggests the writer, writing loosely about the entire Day of Atonement ceremony, includes the altar of incense because of its essential role even though it was technically in the Holy Place — or he refers to the golden censer carried in.</p>",
      "voices": [
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p><em>Thumiaterion</em> most naturally means a censer, not the fixed altar. On Yom Kippur the high priest carried the golden censer filled with incense into the Holy of Holies (Lev 16:12–13); that censer was thus functionally an article of the inner sanctuary on the one day that mattered most for the argument.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>The altar of incense stood permanently in the Holy Place, not the Holy of Holies. The writer may describe the golden censer used on Yom Kippur, or may associate the altar with the inner sanctuary by functional connection: without the incense the high priest could not survive the divine presence. The two were inseparable in the Day of Atonement ritual.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>Barnes reviews the debate in detail: the Greek <em>thumiaterion</em> can mean either censer or altar. He concludes the most defensible reading is the golden censer, since it was the one incense-instrument actually taken into the Most Holy Place. The ark's contents — manna, rod, tablets — each testified to a distinct aspect of God's covenant faithfulness to Israel.</p>"
        }
      ],
      "consensus": "mixed",
      "key_tension": "Whether <em>thumiaterion</em> refers to the golden censer carried into the Holy of Holies on Yom Kippur or to the altar of incense (which stood in the Holy Place but was functionally linked to the inner sanctuary) is disputed."
    },
    "5": {
      "synthesis": "<p>Above the ark were the cherubim of glory overshadowing the mercy seat (<em>hilasterion</em>). The writer adds that he cannot discuss these things in detail now. Calvin sees the cherubim as the guard of the divine throne and the mercy seat as the place where God's justice and mercy met — pointing forward to Christ in whom these two attributes are perfectly reconciled. Ellicott notes that <em>hilasterion</em> here is the same word used in Romans 3:25 for Christ himself as the propitiation: the mercy seat was the type of which Christ is the antitype. Clarke identifies the cherubim as representations of the angelic host surrounding the divine throne — their faces bowed toward the mercy seat, modeling the posture of adoration before the place of atonement. Barnes emphasizes that the writer's restraint — \"of which we cannot now speak in detail\" — is a rhetorical acknowledgment that the typological resonances are too rich to exhaust without losing the main argument. Wesley reads the mercy seat as the most significant piece of furniture in the entire tabernacle: it was the place of meeting, the place where blood was sprinkled, the place where forgiveness was declared.</p>",
      "voices": [
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p><em>Hilasterion</em> — mercy seat — is the same word Paul applies to Christ in Romans 3:25. The type-antitype connection is explicit: the cover of the ark, where blood was sprinkled for atonement, finds its fulfillment in Christ who is himself the propitiation.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>The cherubim faced each other, both looking down at the mercy seat — modeling the posture of the heavenly court in adoration before the locus of divine mercy. Their wings formed a canopy over the ark, symbolizing the divine dwelling above the covenant symbols within.</p>"
        },
        {
          "src": "wesley",
          "attr": "Wesley",
          "html": "<p>The mercy seat is the architectural center of the entire tabernacle system: everything points toward it. It was the place of God's meeting with man, of sin's covering, and of the divine word spoken from between the cherubim.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>\"Of which we cannot now speak in detail\" — the writer is not ignorant of the typology but chooses not to be distracted. The argument demands focus on access and atonement; detailed typological commentary would be valuable but here would lose the thread.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "6": {
      "synthesis": "<p>With these preparations in place, the priests go regularly into the first section (the Holy Place) to perform their duties. Calvin notes the contrast being set up: regular, daily priestly access to the outer room versus the once-a-year access of the high priest to the inner room. The daily ministry of the ordinary priests was essential but it was bounded — the innermost presence remained inaccessible to them. Ellicott explains that <em>diapantos</em> (continually, always) underlines the perpetual, unceasing character of this outer ministry — lamp-trimming, incense-burning, showbread renewal were daily operations. Clarke observes that this continuous outer ministry, necessary and divinely ordained, nevertheless could never take the priests past the second veil. Barnes draws out the implicit contrast with Christ: the Levitical priests had to minister continuously because their ministry was incomplete; Christ's one entry into the true Holy of Holies was sufficient because his sacrifice was complete. Wesley notes that even the most faithful Levitical priest, after a lifetime of daily service, never once entered the Holy of Holies — access to the innermost presence was structurally unavailable to him.</p>",
      "voices": [
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p><em>Diapantos</em> — continually. The daily outer ministry was unceasing: lamps trimmed morning and evening, incense burned, showbread renewed weekly. This perpetual repetition contrasts sharply with the once-a-year entry of the high priest into the inner sanctuary.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>The priests who maintained the outer sanctuary's daily functions did so their entire careers without once passing the second veil. The inner sanctuary was structurally off-limits to them — a spatial declaration of the barrier between sinful man and God's immediate presence.</p>"
        },
        {
          "src": "wesley",
          "attr": "Wesley",
          "html": "<p>A faithful Levitical priest could serve daily for forty years and never enter the Holy of Holies once. The structural exclusion was absolute for all but the high priest — and even he could enter only once a year, with blood, under strict conditions.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>The continuous repetition of the outer ministry showed its incompleteness. A task that is never finished points to a fundamental inadequacy in the worker or the work. Christ's single entry accomplished what perpetual Levitical service could not.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "7": {
      "synthesis": "<p>Into the second section (the Holy of Holies) only the high priest enters, once a year, and never without blood which he offers for himself and the sins of the people committed in ignorance. All commentators find the phrase \"not without blood\" pivotal: it encapsulates the entire Old Testament theology of atonement. Calvin emphasizes that even the high priest — the most privileged man in Israel — could not enter the divine presence except through blood; this sets the pattern that Christ's entry into the true Holy of Holies would require his own blood. Ellicott notes the qualification \"sins committed in ignorance\" (<em>agnoema</em>): the Levitical system could not adequately address deliberate, presumptuous sin; it covered only errors and inadvertencies. This limitation would be a live concern for the readers and explains why the better sacrifice of chapter 10 is needed. Clarke stresses the \"for himself\" clause: the Levitical high priest was himself a sinner and had to atone for his own guilt before he could represent the people — Christ's sinlessness meant he had no such need. Barnes notes that this annual repetition was the Levitical system's most solemn moment, and yet its very repetition admitted its inadequacy: if it had truly removed guilt, no second Yom Kippur would ever have been needed.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>Not without blood — even the high priest, the most privileged man in Israel, could not approach the divine presence except through a blood offering. This principle applies even more emphatically to Christ's entry into the true Holy of Holies with his own blood.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>\"Sins of the people committed in ignorance\" (<em>agnoema</em>) — the Levitical system was structurally limited to inadvertent offenses. Deliberate, presumptuous sin fell outside its regular purview. This limitation would press on the consciences of readers who had sinned knowingly since their conversion.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>\"For himself\" — the high priest was a sinner who first had to offer a bull for his own sin before he could offer the goat for the people (Lev 16:6–11). Christ had no sin of his own to atone for; he is priest without personal need of atonement, which is why his sacrifice is infinite in worth.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>The annual repetition of Yom Kippur was the confession of the system's incompleteness. A perfect atonement would not need to be repeated. Christ offered once and sat down; the Levitical high priest came out and the whole cycle began again the following year.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "8": {
      "synthesis": "<p>The Holy Spirit was signifying by this that the way into the holy places was not yet disclosed while the outer tabernacle was still standing. Ellicott explains that the Holy Spirit is treated as the divine author of the Levitical arrangements — the tabernacle's very structure was a divine teaching about access, not merely a pragmatic architectural choice. The \"outer tabernacle still standing\" is the first tent — its continued existence functioned as a barrier, a \"not yet\" sign that full access to God remained unavailable. Clarke sees this as profound spiritual pedagogy: God designed the structure to preach its own temporariness. The first tent's standing veil declared in architectural form what Jeremiah 31 declared in prophetic form: the present system is provisional. Barnes draws the practical conclusion for the readers: the ongoing Levitical ministry — the fact that priests still served in the outer tent — was the Holy Spirit's continuing declaration that final atonement had not yet been made. The destruction of the temple in 70 AD would be the removal of the architectural sign; Christ's death was the removal of the reality it signified. Wesley observes that what the law could not say in words, the structure of the sanctuary said in stone and curtain — the gospel was preached in the architecture of the old covenant's worship.</p>",
      "voices": [
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>The Holy Spirit is named as the architect of the tabernacle's meaning — its structure was divine pedagogy, not merely practical design. The outer tent's persistent existence was a standing declaration that access to God's immediate presence was not yet open.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>The old sanctuary preached its own provisionality in its very design. The barrier of the second veil, standing year after year, declared as plainly as any prophecy that the way into the holiest was not yet made manifest. The structure was a time-stamped message.</p>"
        },
        {
          "src": "wesley",
          "attr": "Wesley",
          "html": "<p>The Spirit used the architecture of the tabernacle as a living parable. Every Day of Atonement, every replacement of the high priest, every repetition of the sacrifice said: not yet, not yet. The new and living way was opened only when Christ cried \"It is finished.\"</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>While the Levitical system functioned, it was the Spirit's sign that final atonement had not been made. When Christ made the one offering, the sign was removed — the veil was torn, the outer tent lost its separating function, and the way into the holiest was permanently and universally opened.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "9": {
      "synthesis": "<p>The outer tabernacle is a parable (<em>parabole</em>) for the present time, indicating that gifts and sacrifices cannot perfect the worshiper's conscience. Calvin reads \"present time\" as the old covenant era viewed from the new: the outer tent stood as a parable that only now, in Christ, can be read for what it was. The gifts and sacrifices being offered cannot perfect the conscience — they cannot resolve the guilt that sin produces inwardly. Ellicott identifies the key word as <em>syneidesis</em> (conscience) — the Levitical system addressed external, ceremonial defilement; it could not clear the internal verdict of an awakened conscience about moral guilt. Clarke argues that the system's inability to perfect the conscience was not incidental but designed: if it could have done so, there would have been no need for Christ. Barnes stresses that the Levitical economy was never meant to be a final answer to conscience; it was a pointing-forward, a pedagogical preparation. The unanswered conscience of every penitent Jew who came year after year to Yom Kippur was the Spirit's way of keeping eschatological longing alive — and that longing found its answer only in the gospel. Wesley adds that a system that cannot purge the conscience cannot produce the full assurance and confident access that believers now have through Christ.</p>",
      "voices": [
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p><em>Syneidesis</em> — conscience — is the key. The Levitical sacrifices addressed ceremonial uncleanness and restored status in the community; they could not silence the internal verdict that a serious sinner felt before a holy God. Only Christ's blood can perfect conscience.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>The inability to perfect the conscience was not a defect that God overlooked but one he designed into the old system. An economy that left conscience imperfect drove Israel forward in hope toward the coming sacrifice that would finally answer what the blood of bulls could not.</p>"
        },
        {
          "src": "wesley",
          "attr": "Wesley",
          "html": "<p>A religion that cannot clear the conscience cannot produce full assurance. The Levitical worshiper went away from Yom Kippur with his status restored but his deepest question unanswered. The gospel gives what the law withheld: a conscience truly perfected by the blood of Christ.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>The repeated sacrifices were repeated precisely because they could not once-for-all settle the question of guilt. Every Yom Kippur was a confession that last year's was not enough. This systemic incompleteness was the parable's final word — until Christ spoke the word that closed the need forever.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "10": {
      "synthesis": "<p>The old regulations deal only with food, drink, various washings, and fleshly ordinances imposed until the time of reformation (<em>diorthosis</em>). Calvin explains that these external regulations were not intrinsically holy but instrumentally useful — they maintained a visible people of God, dramatized the need for cleansing, and kept Israel looking forward to the substance. Their \"until\" clause is crucial: they were never meant to be permanent but were always time-stamped, awaiting the divine rectification. Ellicott notes that <em>diorthosis</em> is a strong word — it means a setting right, a correction, an improvement — and its use implies that the old order was in a state of imperfection awaiting repair. Clarke argues that the comprehensive listing (food, drink, washings) deliberately covers the breadth of the Levitical purity code to make the point that the entire system — not just some of it — was in the provisional category. Barnes observes that the phrase \"fleshly ordinances\" (<em>sarx</em>) is not pejorative in the sense of sinful but descriptive: the regulations operated on the physical level, touching what is eaten, drunk, and washed, not on the moral-spiritual level where conscience and guilt are addressed. Wesley adds that the \"time of reformation\" is the new covenant era, already inaugurated in Christ — believers live in the fulfillment, not the anticipation.</p>",
      "voices": [
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p><em>Diorthosis</em> — \"reformation\" — implies a definitive setting-right of something imperfect. The old system was not simply old-fashioned but structurally awaiting correction. The new covenant is not merely an improved version of the old; it is its divinely appointed replacement.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>Food, drink, various washings — the entire Levitical purity code is swept into the \"fleshly ordinances\" category. The breadth of the list shows that the whole system was provisional, not just some ceremonial details. Everything in the old cultus had an \"until\" written across it.</p>"
        },
        {
          "src": "wesley",
          "attr": "Wesley",
          "html": "<p>\"Until the time of reformation\" — that time is now, in Christ. Christians do not await the fulfillment; they inhabit it. The old ordinances served their purpose until the substance arrived; now that the substance is present, the shadow has no further function.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>\"Fleshly\" does not mean sinful but external — operating on the physical level of diet, ablution, and ritual status. These were real regulations given by God for a real purpose, but their purpose was limited: they could not touch the inner person where sin's damage is deepest.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "11": {
      "synthesis": "<p>Christ appeared as high priest of the good things that have come, through the greater and more perfect tabernacle not made with hands — not of this creation. Calvin reads \"high priest of the good things\" as a comprehensive summary of all new covenant blessings: forgiveness, the Spirit, access, adoption — everything that the Levitical system could only shadow. The greater tabernacle through which he passed is heaven itself — the true holy of holies into which he entered with his own blood. Clarke notes the double negation: \"not made with hands, not of this creation\" — emphatic contrast with everything material and created. Barnes stresses that Christ passed <em>through</em> the tabernacle rather than serving <em>in</em> it (as Levitical priests served in the earthly one) — his journey was from earth through the heavens to the throne, not a lateral movement within a building. Wesley sees in \"good things to come\" (or \"good things that have come\") the whole eschatological inheritance secured by Christ's priestly work — these are not future hopes but present realities experienced by faith, though not yet seen in their fullness.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>\"Good things\" comprehends all the blessings of the new covenant: forgiveness, access to God, the Holy Spirit, adoption. Christ is the high priest who not only opened the way to these blessings but himself delivers them. He is both the mediator of the covenant and the substance of its promises.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>\"Not made with hands, not of this creation\" — the double negation is emphatic. The tabernacle Christ passed through is constituted entirely differently from any human structure. It is heaven itself in its reality, not an earthly replica of it.</p>"
        },
        {
          "src": "wesley",
          "attr": "Wesley",
          "html": "<p>\"Good things\" are both present and future: present in the sense that the new covenant blessings are available now through faith; future in the sense that their full enjoyment awaits the resurrection and new creation. Christ as high priest secures both the current foretaste and the final feast.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>Christ passed <em>through</em> the heavens on his ascent to the right hand of the Father — his priestly journey was not within a building but through the created universe itself into the presence of God. This is why his priesthood transcends all earthly categories.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "12": {
      "synthesis": "<p>Christ entered the holy places once for all, not by means of the blood of goats and calves, but by means of his own blood, thus securing an eternal redemption (<em>lytrosis aionion</em>). Calvin finds the contrast absolute: the blood of animal sacrifices was the instrument of a temporary, annual covering; the blood of Christ is the instrument of a once-for-all, eternal liberation. The word <em>lytrosis</em> (redemption) carries the ransom-price connotation: something was owed, something was paid, the debt is discharged. Ellicott (whose commentary has no entry for this verse) is absent; Clarke argues that the eternity of the redemption rests on the infinite dignity of the one who offered — a finite sacrifice must be repeated because it is exhausted; an infinite sacrifice achieves an infinite result. Barnes develops this at length: \"once for all\" (<em>ephapax</em>) eliminates all repetition; \"eternal\" means the redemption will never be superseded, reversed, or repeated. What Christ did in history is valid for eternity. The single entry with his own blood is contrasted sharply with the annual entry of the Levitical high priest with borrowed blood — the contrast is between the genuine and the representative, the real and the symbolic.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>Animal blood provided temporary, annual coverage; Christ's own blood secured eternal redemption. The difference is not merely quantitative (more sacrifices vs. one) but qualitative — the nature of the offering determines the nature and duration of the result.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>The eternity of the redemption flows from the infinite dignity of the person who offered himself. A finite offering is proportionate to a finite effect; the Son of God offering himself produces an effect as unlimited as his own nature — eternal redemption with no possibility of exhaustion.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p><em>Ephapax</em> — once for all — is the decisive word. It eliminates every form of repetition, whether annual (as in Levitical sacrifice) or daily (as later in the Mass debate). \"Eternal redemption\" means the result stands as long as God stands — it is as permanent as the throne it was secured before.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "13": {
      "synthesis": "<p>For if the blood of goats and bulls, and the sprinkling of defiled persons with the ashes of a heifer, sanctify for the purification of the flesh — this is the conditional premise that sets up verse 14's <em>a fortiori</em> conclusion. Calvin identifies this as a rabbinic-style argument from the lesser to the greater: if the lesser thing works to the extent it does, how much more will the greater thing achieve what is needed at the deeper level? The ashes of the red heifer (Numbers 19) produced Levitical cleanliness — the ability to rejoin the worshipping community after contact with a corpse. Ellicott explains that this ritual cleansing was real but external: it restored ceremonial status (<em>katharos</em> in the Levitical sense) without touching the moral conscience. Clarke notes that this was perhaps the most striking and mysterious of all Levitical rites — the ashes of a heifer mixed with water produced cleanness for the unclean — showing that God could, when he willed, attach genuine purifying effect to what seemed merely symbolic. Barnes argues that the effectiveness of even this ceremony proves the principle: when God appoints a means, the means works for its appointed purpose. The point is not that the Levitical rites were ineffective but that their effectiveness was bounded by their nature and scope.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>This is a lesser-to-greater argument. If the blood of animals accomplished the limited purpose for which God appointed it — external, ceremonial cleansing — then Christ's blood, appointed for the incomparably greater purpose of conscience-cleansing, will certainly accomplish its end.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>The red heifer ceremony (Num 19) was perhaps the most enigmatic of all Levitical rites. Its ashes, sprinkled with water on the unclean, restored ceremonial purity — ability to re-enter the worshipping community. This was a real but bounded effect: external, not internal.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>The ashes of a heifer that had never been yoked were mixed with water of purification — an elaborate ceremony producing a straightforward result: the unclean became clean. The mystery of the ritual shows that God was not limited to natural mechanisms but bound the result to his own appointment.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>The Levitical rites worked — for their purpose. God does not institute ineffective means. The argument here is: if God's lesser appointments accomplished the external purification they were designed for, his greater appointment — the blood of his Son — will certainly accomplish the deeper purification it was designed for.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "14": {
      "synthesis": "<p>How much more will the blood of Christ, who through the eternal Spirit offered himself without blemish to God, purify our conscience from dead works to serve the living God? The <em>a fortiori</em> conclusion reaches its climax. The phrase \"through the eternal Spirit\" (<em>dia pneumatos aioniou</em>) is the principal exegetical crux. Ellicott argues that this does not refer to the Holy Spirit but to Christ's own eternal divine nature — it was as the eternal Son, not merely as a Spirit-anointed human, that he offered himself; his deity gives the sacrifice its infinite worth. Clarke gives both readings: the Holy Spirit (who sustained Christ through his sufferings and raised him) or Christ's own divine Spirit. Wesley and most of the Reformed tradition (including Calvin) understand it as a reference to the Holy Spirit, by whose power Christ maintained his sinless life and surrendered himself willingly at the cross. Barnes reviews all interpretations and tentatively prefers the Holy Spirit reading. The practical consensus regardless of this dispute is clear: the blood of Christ, offered in the context of divine eternal perfection, purifies the conscience — not merely restoring ceremonial status but clearing the deepest verdict of guilt.</p>",
      "voices": [
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>\"Through the eternal Spirit\" most likely refers to Christ's own eternal divine nature, not the Holy Spirit. It was as the eternal Son — not merely as a Spirit-anointed man — that he offered himself. This gives the sacrifice its infinite and therefore once-for-all character.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>Both readings are possible: the Holy Spirit who sustained Christ in his sufferings, or Christ's own eternal divine Spirit. The point on either reading is the same — the sacrifice was not merely human but grounded in a divine dimension that gives it infinite and eternal worth.</p>"
        },
        {
          "src": "wesley",
          "attr": "Wesley",
          "html": "<p>\"Through the eternal Spirit\" — by the power of the Holy Spirit who filled and sustained him. It was by the Spirit's power that Christ maintained sinless obedience through all his sufferings and surrendered himself willingly as an unblemished offering.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>\"Purify our conscience from dead works\" — the specific result: not external cleanness but internal liberation from the guilt that stifles true worship. \"Dead works\" are works done apart from life in God — whether the works of sin or even the Levitical works offered without faith. The conscience made clean can serve the living God freely.</p>"
        }
      ],
      "consensus": "mixed",
      "key_tension": "Whether \"the eternal Spirit\" (<em>pneumatos aioniou</em>) refers to the Holy Spirit who sustained Christ through his passion, or to Christ's own eternal divine nature that gives the sacrifice its infinite worth, is disputed among the commentators."
    },
    "15": {
      "synthesis": "<p>Therefore Christ is the mediator of a new covenant, so that those called may receive the promised eternal inheritance — since a death has occurred that redeems them from transgressions under the first covenant. Calvin reads this verse as the hinge on which the entire passage turns: the new covenant mediator and the testator whose death secures the inheritance are the same person, and that identity explains why Christ's death was necessary. Ellicott explains that the redemption from \"transgressions under the first covenant\" is not limited to OT believers but includes all the accumulated guilt of the covenant period, which the Levitical sacrifices could cover but never remove. Clarke stresses the word <em>keklemenoi</em> (those called) — the beneficiaries of the eternal inheritance are defined by divine calling, not by national or ethnic category; both Jew and Gentile who are called receive what Abraham was promised. Barnes finds the verse's logic clear: a mediator between two parties in a dispute must be independent of both; Christ as mediator between God and humanity is uniquely qualified because he is both fully divine and fully human. Wesley adds that the \"eternal inheritance\" is the language of adoption: those who receive it are heirs, children of God, with a share in what the Son eternally possesses.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>Christ is mediator and testator — the one who establishes the covenant and the one whose death puts it into force. The death that redeems from transgressions under the first covenant means that OT believers were saved on the basis of Christ's future work; the same death that instituted the new covenant also ratified the promises made to Abraham.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>\"Transgressions under the first covenant\" — the accumulated guilt of the entire Mosaic period, covered annually but never finally removed. Christ's death retroactively redeems from all of it: the old covenant sacrifices were effective provisionally because they pointed forward to what was now done.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p><em>Keklemenoi</em> — those who are called. The inheritance is received by the called, not the nationally privileged. This opens the promise to all who are reached by the gospel call — Jew and Gentile alike are co-heirs in Christ.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>The \"eternal inheritance\" exceeds anything the old covenant promised. Land, long life, and national blessing were the earthly inheritance of Sinai; the new covenant promises nothing less than eternal life in the presence of God — the substance of which all earthly blessing was only the shadow.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "16": {
      "synthesis": "<p>For where a will (<em>diatheke</em>) exists, the death of the one who made it must be established. The word <em>diatheke</em> carries two senses — covenant and testament (will) — and the writer now exploits both meanings. Calvin embraces the double reading: the new covenant is also a testament in which God bequeaths the inheritance to his people, and a testator's death is what puts a will into legal force. The death of the testator-mediator is therefore not incidental to the new covenant but constitutive of it. Ellicott reviews the Greek usage carefully and notes that in classical and Hellenistic Greek <em>diatheke</em> more often means will/testament, while in the LXX it translates the Hebrew <em>berith</em> (covenant). Here the writer deliberately uses the testamentary sense to make his argument about the necessity of death — but this does not abolish the covenant sense, which governs the rest of the chapter. Clarke follows a reading suggested by a learned friend: even in the covenant sense, death of the ratifying victim was required (as in Gen 15); the argument works on both interpretations. Barnes carefully assesses both and concludes the testament reading best fits the immediate argument but the covenant reading governs the book as a whole.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>The double meaning of <em>diatheke</em> (covenant and testament/will) is here deliberately invoked. A testator's death puts the will into force; Christ's death did the same for the new covenant. The bequest was already made; the death of the maker validated it for the heirs.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>In classical Greek <em>diatheke</em> is primarily a will or testament; in the LXX it translates <em>berith</em> (covenant). Here the writer uses the testamentary sense to argue the necessity of death — a will takes effect only when the testator dies. Both senses are held together throughout the epistle.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>Even on the covenant reading, death was required — the covenant-ratification rite involved the death of animals (Gen 15; Exod 24). The argument works whether one reads \"will\" or \"covenant\": in either case, death is constitutive, not incidental.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>Barnes assesses both interpretations in detail. The testament reading fits the immediate logical argument of verses 16–17 most cleanly; the covenant reading governs the broader theological framework. He concludes the writer uses the testamentary argument as a parenthetical illustration within a larger covenant theology.</p>"
        }
      ],
      "consensus": "divided",
      "key_tension": "Whether <em>diatheke</em> should be read primarily as \"testament\" (will — in force upon the testator's death) or as \"covenant\" (ratified by the death of the victim as in Gen 15), with consequent differences in how the necessity of Christ's death is argued."
    },
    "17": {
      "synthesis": "<p>For a will takes effect only at death; it has no force while the one who made it is still alive. Calvin finds this self-evident in Roman legal practice and uses it to explain why the new covenant could not be inaugurated until the cross: the blessings were promised under oath during Christ's ministry but could not be legally transferred until his death. Ellicott examines whether this is best understood as strict Roman testamentary law or as the broader principle that legal dispositions become irrevocable only when the maker dies. He leans toward seeing it as a general legal principle rather than a technical Roman citation. Clarke observes that this verse works even on the covenant-victim reading: the covenant was not in force until the covenant-victim died — just as the Sinaitic covenant required the death of animals and the sprinkling of blood (v. 18–20) before the terms took effect. Barnes finds in the verse a simple argument from universal legal experience: every reader, Jewish or Greek, understood that a will does not distribute its bequests while the testator lives. Christ alive and teaching gave promises; Christ dead and risen enacted the distribution of what he promised.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>The blessings of the new covenant were promised during Christ's ministry but could not be distributed until his death. Death is the legal threshold: on this side, promises; on the other side, enacted inheritance. The cross is the moment the testament came into force.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>This may be a general legal principle rather than a strict citation of Roman testamentary law. A will or legal disposition of any kind is revocable while the maker lives; only death makes it binding and irrevocable. The principle applies across legal cultures.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>On the covenant-victim reading: the covenant is not in force until the representative victim dies. The Sinai analogy (vv. 18–20) confirms this — the covenant was ratified through blood-sprinkling, not through the mere pronouncement of terms. Death was constitutive in both cases.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>The argument is from universal legal experience. Every reader understood intuitively that an inheritance is not distributed while the testator lives. Christ during his earthly ministry gave the promises; his death enacted the distribution — the heirs now receive what he pledged.</p>"
        }
      ],
      "consensus": "divided",
      "key_tension": "Whether <em>diatheke</em> here means testament (supporting the argument from Roman testamentary law) or covenant (requiring a victim's death for ratification, as in Gen 15), which determines the precise logic of the necessity of Christ's death."
    },
    "18": {
      "synthesis": "<p>Therefore not even the first covenant was inaugurated without blood. The argument pivots from the testament analogy back to covenant ratification in Israel's history. Calvin observes that the transition word \"therefore\" (<em>hothen</em>) draws the consequence: if a covenant requires death, the Sinaitic covenant confirms this by the blood-sprinkling of Exodus 24. God did not institute the Mosaic covenant by word alone but by blood — this was not incidental detail but a constitutive element of covenant-making. Ellicott notes the language \"even the first covenant\" — the writer is careful not to say the old covenant was defective in its inauguration, only that it too required blood; this establishes a principle applying to both covenants and therefore requiring blood for the new as well. Clarke points to the historical narrative in Exodus 24:5–8 as the background and notes that Moses read the book of the covenant aloud before sprinkling blood, linking word and blood inseparably in covenant ratification. Barnes draws the theological principle: blood-shedding is God's appointed method of covenant inauguration and maintenance; this is not primitive or arbitrary but reflects the deep logic that sin's penalty is death, and covenant fellowship with a holy God requires that penalty to be addressed.</p>",
      "voices": [
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>\"Even the first covenant\" — the writer does not denigrate the Mosaic covenant's inauguration but uses it as a precedent. If God's first covenant required blood, his second must also. The principle of blood-mediated covenant is established by both covenants, not just the new.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>Exodus 24:5–8 records Moses reading the book and the people responding, then Moses sprinkling both book and people with blood. Word and blood together ratify the covenant — neither alone is sufficient. The new covenant's word (gospel) likewise requires blood (Christ's) for ratification.</p>"
        },
        {
          "src": "wesley",
          "attr": "Wesley",
          "html": "<p>Blood-sprinkling was not ceremonial excess added to the Sinaitic covenant but its constitutive seal. God designed covenant-making to involve death and blood from the beginning, signaling that the relationship between a holy God and sinful people could only be established through a sacrifice.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>The principle that blood is required for covenant inauguration is not merely Jewish or cultural but reflects the deep logic of sin and holiness: sin deserves death, and fellowship with God requires that death be met. The blood of the old covenant said this; the blood of Christ enacted it finally.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "19": {
      "synthesis": "<p>Moses took the blood of calves and goats with water, scarlet wool, and hyssop and sprinkled both the book itself and all the people, saying \"This is the blood of the covenant that God commanded for you.\" Ellicott notes that the Exodus 24 account mentions only one kind of animal (oxen) and does not mention water, scarlet wool, or hyssop — these details may come from tradition or from a harmonization with the red heifer ceremony of Numbers 19. Clarke sees the additional elements as symbolic: water suggests purification; scarlet suggests the blood itself; hyssop was the standard instrument of sprinkling. Barnes observes that the sprinkling of the book itself was a solemn consecration of the written word of the covenant — the law was not merely declared but sealed in blood, indicating that the word of God and the blood of atonement belong together. Wesley finds the words \"This is the blood of the covenant\" echoed in Christ's words at the Last Supper — a deliberate connection showing that the Lord's Supper is the new covenant's equivalent of Exodus 24, the moment when the covenant is formally sealed between God and his people in the mediator's blood.</p>",
      "voices": [
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>The Exodus 24 narrative mentions only oxen, not calves and goats, and omits the water, scarlet wool, and hyssop. The writer may be drawing on a fuller tradition or harmonizing with Numbers 19. The detail does not affect the argument but shows awareness of wider cultic practice.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>Water: purification. Scarlet: the blood's color and its costly redemptive character. Hyssop: the standard sprinkling instrument. These elements combined with blood gave the rite its full symbolic range — addressing every dimension of the covenant community's need for cleansing.</p>"
        },
        {
          "src": "wesley",
          "attr": "Wesley",
          "html": "<p>\"This is the blood of the covenant\" — words taken up verbatim by Christ at the Last Supper (Matt 26:28). The connection is deliberate: the Eucharist is the new covenant's Exodus 24, the moment of covenant sealing in the mediator's blood.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>The sprinkling of the book itself is remarkable: the written word of the covenant is sealed in blood, not merely declared. Word and blood are inseparable in covenant theology — the promise requires a sacrifice to be valid, and the sacrifice requires a word to be intelligible.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "20": {
      "synthesis": "<p>\"This is the blood of the covenant that God commanded for you\" (Exod 24:8). Calvin finds the sentence the most important single clause in the passage for establishing the principle that God's commands are sealed in blood — what God orders is not merely verbal but covenantally ratified. Ellicott reads this as the formal covenant-inauguration formula: the covenant is established not when it is promised or even when it is heard and agreed to, but when the blood is applied. Clarke observes the parallel with Genesis 22: even Abraham's covenant was not final until the sacrifice was made. Barnes stresses that the word \"commanded\" (<em>eneteilato</em>) shows this is a divine requirement, not a human addition — the necessity of blood-ratification is not ceremonialism but God's own institution, reflecting the necessity of atonement for covenant fellowship. The verbal parallel with the Last Supper words is noted by Wesley as the strongest possible evidence that Christ consciously fulfilled this Mosaic moment in his institution of the Lord's Supper, intending his blood to serve the same covenant-sealing function in the new economy that Moses's blood-sprinkling served in the old.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>\"That God commanded\" — blood-ratification is divine requirement, not human addition. The covenant is put into legal force not by word alone but by blood. This divine principle, established at Sinai, governs both covenants: the new is confirmed by a better blood.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>The covenant-inauguration formula is spoken over the blood, not over the words alone. The covenant became effective when the blood was applied to the people — the legal threshold was the sprinkling, not the proclamation. Christ's blood is the new covenant's equivalent threshold.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>\"Commanded for you\" — the blood-ratification was for the people's benefit, not for God's. God does not need the blood; sinful people do, because covenant with a holy God requires the judgment due to sin to be addressed before fellowship can stand.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>The Last Supper's words (\"this is my blood of the covenant\") are deliberately shaped on these Mosaic words. Christ was signaling that his death would accomplish for the new covenant what Moses's blood-sprinkling accomplished for the old: the formal inauguration of the covenant relationship.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "21": {
      "synthesis": "<p>Moses sprinkled with blood both the tent and all the vessels used in worship. Ellicott notes that the OT narrative (Exodus 40) does not mention blood-sprinkling of the tabernacle at its dedication but mentions the anointing oil; the blood detail may come from a tradition preserved in Josephus or from a broader principle about the comprehensive sanctification of all covenant-related objects. Clarke argues that whether or not all the details are found verbatim in Exodus, the principle is consistent: everything associated with the covenant cultus required purification — not merely people but also the structures and instruments of worship. Barnes observes the surprising comprehensiveness: vessels, tent, book, people — nothing in the covenant system was exempt from blood-purification. Wesley draws the spiritual analogy: not only persons but all things pertaining to the new covenant ministry — the church's structures, practices, and forms of worship — are sanctified through the blood of Christ. The breadth of the blood's application in the old covenant prefigures the universal reach of Christ's atonement in the new.</p>",
      "voices": [
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>Exodus 40 records anointing oil, not blood, at the tabernacle's dedication. The blood detail here may draw on a tradition also found in Josephus, or on the general principle that all covenant objects required purification-by-blood as part of the overall system.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>The principle is consistent even if every detail is not verbatim in Exodus: everything associated with the covenant cultus required purification. Not only persons needed cleansing — the structures and instruments of worship were also sanctified through blood.</p>"
        },
        {
          "src": "wesley",
          "attr": "Wesley",
          "html": "<p>The comprehensiveness of the blood-sprinkling — tent, vessels, book, people — shows that the entire covenant system required purification, not just individual worshippers. Everything in the new covenant likewise is sanctified through Christ's blood: persons, ordinances, and the church's life.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>Nothing in the old covenant system was exempt from blood-purification — this breadth is the writer's point. The principle extends naturally to the new covenant: Christ's blood is not merely a personal transaction but a comprehensive cosmic purification.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "22": {
      "synthesis": "<p>Under the law, almost everything is purified with blood, and without the shedding of blood there is no forgiveness. The word \"almost\" (<em>schedon</em>) acknowledges that the law allowed some exceptions (Lev 5:11–13; Num 31:22–23), but blood-purification is the dominant principle. Calvin takes this as the divine establishment of a universal principle: sin's penalty is death, and the penalty must be borne before forgiveness is granted. \"No forgiveness\" means no remission of sins (literally, no sending away of sin) apart from blood. Ellicott stresses the legal precision of the statement — this is not a general moral observation but a specific claim about God's arrangement for forgiveness: the blood requirement is not optional or replaceable by sincere contrition alone. Clarke finds here the theological heart of the atonement: substitutionary death is not arbitrary but grounded in the holiness of God and the nature of sin as something that incurs a death-penalty. Barnes argues that this verse effectively rules out any purely exemplarist or moral-influence theory of the atonement — forgiveness is not simply God's declaration of amnesty but requires a real payment. Wesley reads \"shedding of blood\" (<em>haimatekchysia</em>) as the strongest possible language: not merely blood but blood poured out — violent, sacrificial death, not a token.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>\"Almost\" acknowledges a few exceptions but does not weaken the rule. The dominant principle of the entire Levitical economy is blood-purification. Without the shedding of blood there is no forgiveness — this reflects the divine logic that sin's death-penalty must be met before the sinner can go free.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>\"No forgiveness\" (<em>aphesis</em> — remission, release, sending-away of sin) is a legal term: sin is not merely overlooked but formally discharged. The blood requirement is God's own institution, not a cultural convention that Christianity later transcended while keeping the benefit.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>This verse is the doctrinal basis of substitutionary atonement. Blood is required because death is the penalty for sin; the penalty must be discharged before forgiveness can be justly granted. This is not arbitrary divine will but the expression of divine holiness and justice.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p><em>Haimatekchysia</em> — a word used only here in the NT — means blood-outpouring, violent sacrificial death. The verse excludes every soft account of forgiveness: it is not granted by divine indulgence alone but through the blood that satisfied the demand of divine justice.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "23": {
      "synthesis": "<p>It was necessary for the copies of the heavenly things to be purified with these rites, but the heavenly things themselves require better sacrifices than these. Calvin sees the argument as an <em>a fortiori</em> from copy to original: if the earthly copies needed blood-purification, the heavenly realities need it even more — and therefore the sacrifices must be proportionately greater, which is why the one sacrifice of Christ is better than all animal sacrifices combined. Ellicott asks in what sense heavenly things need purification and answers that it is not that heaven is defiled but that the way of access — the conscience, the relationship between God and sinners — required purification before redeemed humanity could enter. Clarke interprets the \"heavenly things\" as the terms and arrangements of the new covenant, which could only be put into operation after Christ's blood purified (inaugurated and validated) them. Barnes takes a similar line: the heavenly sanctuary is not literally unclean but the purification language describes the inauguration of the new covenant access — Christ's blood is the dedicated/inauguration offering for the heavenly sanctuary just as Moses's blood was for the earthly. Wesley stresses that \"better sacrifices\" (plural used of the one sacrifice) indicates the one offering's worth exceeds all the animal sacrifices combined.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>If the copies needed purification, the originals need it all the more — and proportionately better sacrifices. The argument works from the earthly to the heavenly: Christ's blood is to the heavenly sanctuary what Moses's blood was to the earthly, but infinitely superior.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>Heavenly things do not need purification as if they were defiled. The language means the purification of the way of access — the conscience and the covenant relationship — so that sinners may enter the divine presence. Christ's blood accomplished this for all who come through him.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>\"Better sacrifices\" — plural of the one sacrifice — signals infinite superiority. The one offering of Christ outweighs all animal sacrifices and their entire system. This is not quantitative comparison (one vs. many) but qualitative: the nature of the offering is incomparably higher.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>Christ's blood is the inaugural offering of the heavenly sanctuary, just as Moses's blood inaugurated the earthly. The parallel is precise: as the earthly sanctuary required a blood-dedication before Israel could worship there, so the heavenly access required Christ's blood before humanity could enter.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "24": {
      "synthesis": "<p>Christ did not enter a sanctuary made with hands — a copy of the true one — but into heaven itself, now to appear in the presence of God on our behalf. Calvin emphasizes the \"now\" (<em>nyn</em>): Christ is currently, at this moment, appearing before the Father as the advocate and intercessor of his people. The priestly ministry did not end at the cross; the session of 8:1 is an active priestly presence, not merely a dignified rest. Ellicott stresses the phrase \"on our behalf\" (<em>hyper hemon</em>): Christ's appearance before God is not for his own sake (he has no need) but representatively, as the people's high priest carrying their names into the divine presence. Clarke draws the contrast sharply: the earthly high priest entered the Holy of Holies briefly, alone, once a year, then came out — Christ entered heaven permanently, for all his people, continuously. Barnes finds the present tense of \"to appear\" the devotionally decisive point: there is no moment at which Christ is not interceding; the believer's access to God is not periodic but constant, because the priest who represents them never leaves the divine presence. Wesley finds this the ground of full assurance: we draw near to God not in our own name or with our own worthiness but in the name and on the worthiness of the one who appears for us.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>\"Now\" — Christ is currently appearing before the Father on behalf of his people. The priestly work is not finished in the sense of ended but finished in the sense of completed and therefore continuously effective. His intercession is the ongoing application of his once-for-all sacrifice.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>\"On our behalf\" (<em>hyper hemon</em>) — Christ does not appear in the divine presence for his own sake but as the representative of his people. Every redeemed person has their name, as it were, carried into the inner sanctuary by the great High Priest who never comes out.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>The Levitical high priest entered briefly, came out, and the congregation waited anxiously for his emergence (Luke 1:21). Christ entered heaven and remains — permanently present before God for his people. The contrast between annual, solitary, brief and eternal, universal, continuous is total.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>There is no moment at which Christ is not interceding. The believer's access to God is uninterrupted because the priest who represents them never withdraws from the divine presence. Full assurance of access flows directly from the permanence of Christ's heavenly priesthood.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "25": {
      "synthesis": "<p>Nor was it to offer himself repeatedly, as the high priest enters the holy places every year with blood not his own — for Christ would have had to suffer many times since the foundation of the world. Calvin finds the argument here definitively closing off any Catholic doctrine of repeated eucharistic sacrifice: if Christ's one offering had been insufficient, he would have needed to die repeatedly, not merely to be re-offered symbolically. The fact that he died once proves the sacrifice was complete and sufficient. Ellicott explains that the comparison is between the Levitical high priest's annual entry with animal blood and Christ's single entry with his own — the repetition of the Levitical rite was a built-in admission of its inadequacy. Clarke notes that \"since the foundation of the world\" means that if repeated death were required, it would have been necessary from the very beginning of sin — a reductio ad absurdum that shows the one offering must be infinite in its efficacy. Barnes stresses that \"blood not his own\" makes the Levitical sacrifice externally representative while Christ's sacrifice is personally constitutive: the high priest borrowed another's life; Christ gave his own — the difference in personal investment corresponds to a difference in the scope and permanence of the result.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>If one offering were insufficient, repeated suffering would have been required from the very beginning of the world. The reductio ad absurdum proves the one offering is infinitely sufficient. This settles the question of any repetition of Christ's sacrifice in any form.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>Annual repetition was the Levitical system's built-in confession of inadequacy. Christ's single offering is not annual but once for all — not because it is one instance of the same kind of sacrifice but because it is an entirely different kind, one that cannot be repeated because it never needed to be.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>\"Since the foundation of the world\" — if repeated dying were required, it would have been necessary since Adam's fall. The absurdity of that conclusion proves the one death is final. The once-for-all character of Christ's suffering is the direct evidence of its infinite sufficiency.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>\"Blood not his own\" contrasts with Christ's self-offering. The Levitical priest offered an animal's life — externally representative but personally uninvested. Christ offered himself — the highest possible investment, producing the highest possible result: an atonement that never needs to be repeated.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "26": {
      "synthesis": "<p>But as it is, Christ has appeared once for all at the end of the ages to put away sin by the sacrifice of himself (<em>athetesis tes hamartias</em> — the cancellation, nullification of sin). Calvin reads \"end of the ages\" as the eschatological fulfillment of all that the ages before Christ anticipated — the incarnation was not a mid-point in history but its climax, the moment toward which all time was running. \"Put away sin\" is stronger than cover or deal with: <em>athetesis</em> means to annul, to set aside as invalid and of no legal force — sin's power over the believer is not merely restrained but nullified. Ellicott explains that the \"once\" (<em>hapax</em>) here has chronological force: it happened at one moment in history, which is why it cannot be repeated. The once-ness of the incarnation corresponds to the once-ness of the offering. Clarke finds in \"sacrifice of himself\" the ultimate distinction from all animal sacrifice: the offering is infinite because the offerer is infinite; the cancellation of sin is total because the sacrifice is total. Barnes reads the verse as the most comprehensive statement of substitutionary atonement in the passage: Christ appeared, he sacrificed himself, he nullified sin — all historical events with eternal consequences.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>\"End of the ages\" — the incarnation was not mid-history but climactic. All prior ages were preparatory; Christ's appearance was the moment toward which they converged. \"Put away\" (<em>athetesis</em>) is legal nullification, not merely cover: sin is set aside as having no further legal claim on those for whom Christ died.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p><em>Hapax</em> — once, at a specific historical moment. The once-ness of the incarnation makes the once-ness of the sacrifice inevitable: God became flesh once, died once, and the effect of that one event stands for all time. History cannot provide a second incarnation or a second atonement.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>\"By the sacrifice of himself\" — the offerer and the offering are identical. An offering of infinite worth from an infinite person cancels an infinite debt. This is why no repetition is possible or necessary: there is no higher sacrifice that could supplement it and no deficit that requires supplementing.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p><em>Athetesis tes hamartias</em> — the annulment of sin. Not merely its covering (old covenant) or its diminution (moralizing) but its legal nullification for those united to Christ. The consequence for Christian assurance is absolute: sin's claim on the believer has been canceled by a historical act that cannot be undone.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "27": {
      "synthesis": "<p>It is appointed for people to die once and after that comes judgment. Calvin uses this as the analogue that makes Christ's one death intelligible and natural: death-once and judgment-after are the fixed order for all humanity; Christ entered fully into that human order, which is why he also died once, not repeatedly. There is no second death for humans, so there is no second offering by Christ. Ellicott explains that <em>apokeimai</em> (appointed, reserved) is the word used for a fixed divine decree — the mortality of humans and the certainty of judgment are not accidents but God's ordained structure of accountability. Clarke notes the pastoral force of the verse: the certainty of judgment after one death makes the once-for-all atonement of Christ both urgent (there is no second chance after death) and sufficient (the one offering matches the one judgment). Barnes stresses that this verse is often read as a proof text against reincarnation and purgatorial re-trials — God has appointed death-once and judgment-after; the scheme of Christian salvation must fit within those appointed boundaries, and Christ's one sacrifice does precisely that. Wesley reads the verse devotionally: the one death, one judgment order means Christ's one sacrifice is exactly calibrated to human need — it addresses the one death humans must face and the one judgment that follows it.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>Christ entered the human order of death-once and followed it through. Since humans die once and face judgment once, Christ offered himself once. The analogy makes the once-for-all character of his sacrifice both necessary and sufficient.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p><em>Apokeimai</em> — divinely reserved, fixed by decree. The death-once / judgment-after order is not a natural accident but God's structured accountability for human life. This divine appointment makes Christ's one sacrifice the exact fit: one death, one judgment, one atonement.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>The certainty of one death and one judgment after it gives the gospel its urgency. There is no second chance after death, no cycle of return, no second judgment. Christ's one sacrifice matches this one-chance structure: it addresses the totality of human guilt before the one judgment that matters.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>This verse closes the door on any scheme of repeated probations or post-mortem purgatorial purification: God has appointed one death per human life, followed immediately by judgment. The one sacrifice of Christ answers the one judgment — nothing additional is needed or possible.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "28": {
      "synthesis": "<p>So Christ, having been offered once to bear the sins of many, will appear a second time, not to deal with sin but to save those who are eagerly waiting for him. Calvin reads the two appearances as the two great acts of Christ's saving work: the first to bear sins (past, complete, sufficient); the second to complete salvation for those who wait (future, certain, glorious). The second appearing has nothing to do with sin-bearing because that is already done — it is purely salvific, a bringing-home of those who have been redeemed. Ellicott explains that the language \"bear the sins of many\" (<em>polloi</em>, many) echoes Isaiah 53:12 — the suffering servant who bore the sin of many — making explicit what has been implicit throughout the chapter. Clarke notes that \"not to deal with sin\" is the decisive contrast with the Levitical annual appearance: the high priest appeared each Yom Kippur to deal with sin; Christ's second appearing has no such function because it has been dealt with already, once and forever. Barnes finds the pastoral application clear and moving: those who look for him are not waiting in fear of a judge coming to assess their sins but in eager anticipation of the one who has already resolved the sin-question and comes now to complete what he began. Wesley reads \"eagerly waiting\" (<em>apekdechomenois</em>) as the posture that defines the Christian life — not passive but actively, confidently expectant, like a bride waiting for the bridegroom.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>Two appearances: the first to bear sin (done, complete); the second to save those who wait (coming, certain). The second has nothing to do with sin because sin was dealt with in the first. The believer awaits not a sin-assessment but a salvation-completion.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>\"To bear the sins of many\" — <em>polloi</em>, echoing Isaiah 53:12. The servant-song is in the background throughout the chapter's atonement theology. The echo makes the connection between Christ's priestly work and the Isaian suffering servant explicit at the chapter's close.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>\"Not to deal with sin\" — this is the decisive contrast with every annual Yom Kippur. The Levitical high priest appeared each year because sin had not been finally addressed; Christ's second coming requires no sin-dealing because it was finished at the cross. He comes only to complete the salvation of his waiting people.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p><em>Apekdechomenois</em> — eagerly awaiting. Those who look for him are not dreading a judge but welcoming a savior whose work on their behalf is complete. The posture of waiting defines Christian existence: between the first appearing (sin borne) and the second (salvation consummated), the church lives in confident, joyful expectation.</p>"
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

    ch8_count = len(HEBREWS["8"])
    ch9_count = len(HEBREWS["9"])
    print(f"Hebrews 8–9 synthesis complete: {ch8_count} verses (ch8) + {ch9_count} verses (ch9) = {ch8_count + ch9_count} total.")

if __name__ == '__main__':
    main()
