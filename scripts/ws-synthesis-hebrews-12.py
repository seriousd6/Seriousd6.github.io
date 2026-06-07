"""
Wide Source Synthesis — Hebrews chapter 12
bookId: hebrews
Verses: ch12 = 29
Run: python3 scripts/ws-synthesis-hebrews-12.py
Sources used: calvin, ellicott, clarke, wesley, barnes
Skipped: mhcc (file not found), jfb (file contains Galatians/2 Corinthians data — corrupted)
Notes:
  - calvin missing: v8, v20, v21, v28
  - ellicott missing: v18
  - clarke missing: v19, v20, v21
  - wesley missing: v4
  - ch12 v17: consensus="mixed" — metanoia referent debated (Isaac's change of mind vs. Esau's own repentance)
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

# INTENT: Load existing synthesis or return empty dict if none exists yet.
# CHANGE? If output path changes, update save_synthesis and all callers.
# VERIFY: After running, data/commentary/synthesis/hebrews.json should have ch key "12".
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
  "12": {
    "1": {
      "synthesis": "<p>Hebrews 12 opens as the grand conclusion to the faith-gallery of chapter 11: therefore — since we are surrounded by so great a cloud of witnesses — let us lay aside every weight and the sin that so easily entangles, and run with endurance the race set before us. Calvin identifies the cloud as the great multitude of saints whose lives press in upon us as testimonies to the power of faith — they witnessed that faith is real and worthwhile. Ellicott is precise: <em>martus</em> means witness, not spectator; these saints testified by their lives, not necessarily by watching ours. Clarke reads \"looking off\" (<em>aphorontes</em>) as an athletic image — the runner keeps his eye fixed on the finish line, turning away from distractions. Wesley reads the cloud as tending upward with holy swiftness, and the \"weight\" as anything that damps the vigor of the soul — not necessarily sinful but burdensome. Barnes stresses that the besetting sin is whatever has most power over a particular person — not the same sin for every reader, but the sin of their individual temperament or history that must be actively put aside. The verse unites past (ch11) with present: the testimony of the ancients becomes fuel for contemporary perseverance.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>The cloud of witnesses is the great multitude of saints who testify that faith is real and worthy of every sacrifice. Their testimony presses in on us as we run: they have proved by their lives that the race is worth finishing.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p><em>Martus</em> means witness, not spectator. The saints of chapter 11 bear witness to the power of faith — they do not necessarily watch us. But their testimony surrounds us as a cloud, dense and enveloping, making evasion of their example impossible.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>\"Looking off\" (<em>aphorontes</em>) — looking away from the world and all secular concerns toward Jesus and the heavenly prize. The Greek evokes the athlete who fixes his eyes on the goal, turning aside from every distraction that would slow his pace.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>The sin which \"easily besets\" is whatever has most power over each individual — the sin of their particular constitution, education, or temperament. Every runner must identify and put aside their own weight; the exhortation is personal, not generic.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "2": {
      "synthesis": "<p>The supreme example toward whom the runner's eyes are fixed is Jesus, the author and perfecter of faith (<em>archegos kai teleiotes</em>). Calvin insists the Greek is unambiguous: Christ freely chose the cross, though it was open to him to live a life free from trouble and full of earthly blessing. His voluntary acceptance of suffering is what makes him a model, not merely a symbol. Ellicott explains that <em>archegos</em> here does not mean pioneer in the sense that Jesus himself needed to run the race of faith (he was not in the same epistemic condition as believers) but that he brought faith to its complete expression as author and finisher of its story. Clarke reads the phrase with the athletic allusion intact: those who ran kept their eyes fixed on the mark — Jesus is the mark. Wesley likens the looking to Israel looking at the brazen serpent, the wounded gazing at the image of their wound as the instrument of their healing. Barnes emphasizes that Christ endured the cross for the joy set before him — the salvation of his people — which was greater than the shame; this utilitarian of love is offered to readers who face their own lesser sufferings and must weigh present pain against future glory.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>It was free to Christ to exempt himself from all trouble and lead a life of ease and blessing; he nonetheless underwent a death bitter and ignominious. The voluntary character of his self-offering is what makes him the author and completer of faith for all who follow him.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>\"Author and Perfecter\" (<em>archegos kai teleiotes</em>) — the runner looks away from all other objects and fixes his gaze on one. Jesus brought faith to its fullest and final expression: he is not merely the first to believe but the one in whom faith reached its complete form.</p>"
        },
        {
          "src": "wesley",
          "attr": "Wesley",
          "html": "<p>As the wounded Israelites looked to the brazen serpent, so we look to Jesus. Our Lord was prefigured by that lifting up; our guilt by the stings; our faith by their looking upward. He is the author who begins our faith and the finisher who carries it to completion.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>For the joy set before him — the redemption of his people — Christ endured the cross and despised the shame. The calculus of cross and joy is offered to readers facing their own trials: present suffering weighed against future glory is the logic of all Christian endurance.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "3": {
      "synthesis": "<p>Consider him who endured such hostility from sinners against himself, so that you may not grow weary or fainthearted. Calvin reads the exhortation as pastoral medicine for the discouraged: the contemplation of Christ's endurance counteracts the spiritual despondency that persecution produces. Ellicott notes the word <em>analogizomai</em> (consider, reckon up, calculate) — the readers are asked to think carefully, not just to remember; the meditation on Christ's experience should produce a reasoned re-assessment of their own. Clarke observes that the hostility Christ endured was not only physical but the contradiction of sinners — the social and intellectual opposition of those who rejected his claims — making it relevant to readers who were experiencing precisely this kind of rejection. Wesley stresses the internal consequence of failing to look to Christ: the soul grows weary and then fainthearted — exhaustion leading to despair. Barnes argues that the appropriate response to great suffering is not less reflection but more: the more attentively we consider what Christ endured, the more our own troubles shrink to their proper proportion.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>The contemplation of Christ's endurance is the medicine for spiritual discouragement. When we are tempted to grow weary, we must consider how much more he endured — and he endured it not for himself but for us. This consideration restores proportion to our suffering.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p><em>Analogizomai</em> — reckon up, calculate carefully. Not a passing glance but a deliberate meditation. The readers are asked to weigh Christ's experience against their own and reach a reasoned conclusion about the scale and meaning of what they face.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>\"Contradiction of sinners\" — not only physical violence but the social and intellectual hostility of those who opposed his claims. This makes the example directly relevant: the readers were experiencing rejection, not (yet) martyrdom. Christ was there before them.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>The more attentively we reflect on what Christ endured, the more our own troubles are reduced to their proper scale. Spiritual weariness comes from looking at our suffering in isolation; looking at Christ's suffering in comparison is the cure for fainthearted despair.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "4": {
      "synthesis": "<p>You have not yet resisted to the point of shedding your blood in your struggle against sin. Calvin reads this as a reminder that the ultimate sacrifice — martyrdom — had not yet been demanded of these readers, and that since the contest is against sin, there is a spiritual dimension even to physical suffering. Ellicott notes a shift in metaphor from the footrace (v1) to the combat of the pugilists, citing a parallel transition in 1 Corinthians 9:26 — in both cases Paul and this writer move from the race to the wrestling match. Clarke emphasizes the contrast with those in chapter 11 who did resist unto blood: the readers' suffering, real as it is, had not reached the level of martyrdom that others bore — and if they could not persevere at this level of trial, how would they face the worst? Barnes reads the verse as both a word of comfort (the worst had not come) and of challenge (therefore there is no excuse for surrender before the worst arrives).</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>The contest is against sin — and since sin always dwells in us, suffering serves to subdue and put it to flight. The readers had not yet been called to the ultimate sacrifice; this reminder should both encourage and challenge them to persevere in what they could still bear.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>The image shifts from the footrace to the boxing match — the same transition found in 1 Corinthians 9:26. In verse 1 sin was the weight to be laid aside; here it is the antagonist to be subdued. The contest is personal and intensely demanding, but blood has not yet been required.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>Many in chapter 11 resisted unto death, sealing their testimony with their blood. These readers had suffered persecution but not martyrdom. The contrast strengthens the exhortation: if the greatest sacrifice had not been required, there was every reason to hold on through the lesser trials.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>The verse offers both comfort and challenge: comfort that the worst had not come; challenge that surrender before the worst arrives is entirely without excuse. Those who cannot endure lesser trials are ill-prepared for greater ones — and greater ones may yet come.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "5": {
      "synthesis": "<p>And have you forgotten the exhortation that addresses you as sons? — \"My son, do not regard lightly the discipline of the Lord, nor be weary when reproved by him\" (Prov 3:11). Calvin reads the verse as a question, heightening its rhetorical force: \"Have you forgotten?\" implies they should not have. He identifies two opposite errors addressed by the Proverbs text: despising the Lord's correction (treating it as insignificant) and fainting under it (being crushed by it). Ellicott notes that the original addresses are in Proverbs and they coexist with a divine guarantee not found there: God speaks to these sufferers \"as sons\" — their suffering is not penal but paternal. Clarke draws attention to the distinction: Proverbs may appear to be a father's wisdom to a human son, but the writer shows it is properly God speaking to any person in affliction. Wesley identifies the two dangers precisely: despise = slight the chastening, make little of it, not impute it to God; faint = be crushed by it, unable to see its purpose or bear its weight. Barnes emphasizes that the divine word addresses them in the second person — God speaks to each reader individually and personally through this text.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>Two errors are identified in the Proverbs quotation: despising God's correction (treating it as nothing) and fainting under it (being overwhelmed). Both miss the true meaning of affliction. The question form — \"have you forgotten?\" — implies the readers should have known better.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>God addresses his suffering people \"as sons\" — this single phrase transforms the interpretation of every trial. What seemed like persecution or abandonment is reread as the language of a father speaking to his child. The suffering is not penal but paternal.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>The Proverbs text appears to be a father's advice to a human son; the writer shows it is God himself speaking to any person in affliction or persecution. The divine authorship of the word gives the correction its comfort: it comes from one who loves and who acts in love.</p>"
        },
        {
          "src": "wesley",
          "attr": "Wesley",
          "html": "<p>Do not despise — do not slight it, make little of it, or impute it to chance. Do not faint — do not be crushed by it or lose sight of its purpose. Two equal and opposite failures: the first is irreverence, the second is despair. The faithful middle is patient, expectant endurance.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "6": {
      "synthesis": "<p>For the Lord disciplines the one he loves and chastises every son he receives (Prov 3:12). Calvin acknowledges the apparent paradox: God visits elect and reprobate alike with affliction; his scourges manifest his wrath as often as his love in the broad witness of Scripture. Yet when the godly are directly addressed, the effect that chastisement produces in them is alone in view — and that effect is always love. Ellicott notes that the Hebrew text of Proverbs and the LXX differ slightly here; the writer follows the LXX, and for the purpose of the argument the difference is not material: both versions teach that love is expressed through discipline. Clarke emphasizes the practical logic: God's chastening of us is proof that we are his children, not proof of his abandonment; the man God ignores is the man God has given up, not the man God is training. Wesley finds the whole passage springs from love: \"for\" — all the chastening springs from this root; therefore neither despise it (it is an act of love) nor faint under it (love has a good purpose). Barnes observes that it is a universal rule in the divine economy that God sends trials on those he truly loves — not because they deserve them, but because they need them for their formation.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>The rule seems paradoxical — God afflicts elect and reprobate alike. But the difference is in the effect: in the godly, chastisement yields love and growth; in the reprobate, hardening and judgment. When the godly are addressed, only the former effect is in view.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>The LXX and Hebrew differ slightly in Proverbs 3:12; the writer follows the LXX. On either reading the teaching is clear: the father who loves his son disciplines him, and discipline therefore becomes the evidence of love rather than its absence.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>The man God chastens is the man God has not given up. Divine discipline is proof of belonging, not proof of rejection. It is precisely because God loves and owns his children that he refuses to leave their character undeveloped and their sins unaddressed.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>A universal rule in the divine economy: God sends trials on those he truly loves, not to inflict pain for its own sake, but because love that does not discipline is not the love of a father but the indulgence of one who does not care about the outcome.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "7": {
      "synthesis": "<p>Endure for the sake of discipline; God is treating you as sons. For what son is there whom his father does not discipline? Calvin reads this as a direct pastoral application: the readers' suffering is not evidence that God has abandoned them but evidence that he is treating them as sons in the household, not strangers outside it. Ellicott notes the word <em>hypomeno</em> (endure, remain under) is chosen deliberately over mere passivity — active, purposeful endurance rather than helpless suffering. Clarke stresses the universal dimension: what son is there whom the father does not discipline? The experience of trial is not exceptional but normal for every genuine member of God's family. Barnes develops the father-son analogy: even the best earthly fathers exercise discipline as a necessary expression of genuine care; this makes the argument from paternal love immediately accessible to every reader's experience. Wesley adds a note of aspiration: endurance in trial is not merely an obligation but an opportunity to demonstrate the reality of the relationship — the enduring son shows himself genuinely to be a son.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>\"God deals with you as sons\" — this sentence transforms the interpretation of suffering entirely. The trial is not abandonment but adoption in practice; not punishment as an enemy but training as a father. The son endures what the stranger is never asked to bear.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p><em>Hypomeno</em> — remain under, actively endure — rather than passive submission. The readers are to bear their trials with purposeful perseverance, conscious of the paternal relationship in which they stand and the good purposes behind the divine discipline.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>\"What son is there whom his father does not discipline?\" — the universality of the statement is important: no son is exempt. The experience of chastening is not exceptional or unusual for God's children; it is the normal pattern of a genuine father-son relationship.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>Every reader knew from experience that good earthly fathers discipline their children. The argument from analogy is immediate: if human fathers do this because they love, how much more certainly does the heavenly Father discipline those he has adopted as his own?</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "8": {
      "synthesis": "<p>If you are left without discipline, which all sons share, then you are illegitimate children and not sons. Ellicott explains that the logic is contrapositive: the universal experience of discipline among sons means its absence proves the opposite relationship. Clarke unpacks the cultural backdrop: illegitimate children were typically neglected in their formation — the father felt little obligation to invest in the training of a child he did not fully own. Wesley is brief but pointed: all sons share discipline, more or less; the one who shares none reveals he has no father who owns him. Barnes develops the pastoral implication: this verse should reframe every Christian's experience of suffering — the very fact that God has sent this trial is the evidence that the sufferer is genuinely his child. The argument is designed to convert the apparent disaster of affliction into a proof of sonship, so that what seemed to argue against belonging to God actually argues for it.</p>",
      "voices": [
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>The logic is contrapositive: all sons share discipline; therefore, the one who shares none is not a son. The absence of any trial or correction in a person's life is not evidence of divine favor but evidence of divine indifference — the most sobering condition of all.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>\"Then are ye bastards\" — the cultural fact is that illegitimate children were neglected in their formation; the father of spurious issue felt little obligation toward them. True sons receive discipline precisely because the father owns them and cares about their character.</p>"
        },
        {
          "src": "wesley",
          "attr": "Wesley",
          "html": "<p>Of which all sons are partakers — more or less. The one who never receives any chastening reveals by that absence that he has no father who owns him. The experience of divine discipline is the evidence of divine ownership, not its contradiction.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>This verse reframes affliction: the very suffering that seems to argue against God's favor is the proof of it. God has sent this trial; therefore the sufferer is his. The most unwanted experience of the Christian becomes, on this logic, the most reliable evidence of belonging.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "9": {
      "synthesis": "<p>Besides this, we have had earthly fathers who disciplined us and we respected them. Shall we not much more submit to the Father of spirits and live? Calvin argues that if we showed deference to earthly fathers when they corrected us — even when their corrections were imperfect and sometimes harsh — how much more reverence should we show to the heavenly Father whose discipline is never mistaken? Ellicott distinguishes \"Father of spirits\" from earthly fathers: the earthly father is \"father of flesh\" — the relationship is biological and temporary; God is the Father of our spirits — the relationship is constitutive and eternal. Clarke applies the <em>a fortiori</em>: the respect paid to earthly fathers, who are fallible men with limited wisdom and partial love, argues for greater submission to God, who is perfect in wisdom and infinite in love. Barnes stresses the word \"live\" at the end of the verse: submission to the Father of spirits is not merely a matter of obedience but of life — those who resist God's discipline turn away from the source of their spiritual vitality.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>If we respected earthly fathers who disciplined us — even imperfectly, with limited wisdom and sometimes excessive severity — how much more should we submit to the heavenly Father whose discipline is never mistaken, never excessive, always purposeful and loving?</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>\"Father of spirits\" — contrasted with \"fathers of our flesh.\" The earthly relationship is biological and temporary; the divine relationship is spiritual and constitutive. God is the Father of the inner person — the relationship goes deeper than birth and lasts beyond death.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>The <em>a fortiori</em> is powerful: we submitted to earthly fathers who were fallible, partial, and sometimes mistaken. God is perfectly wise, perfectly loving, and never wrong. If lesser authority earned our submission, how much more does the greatest authority deserve it?</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>\"And live\" — the addition is weighty. Submission to the Father of spirits is not merely a duty but a life-giving act. Those who resist God's discipline cut themselves off from the one who is the source and sustainer of spiritual vitality; to submit to him is to live.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "10": {
      "synthesis": "<p>Earthly fathers disciplined us for a short time as it seemed best to them, but he disciplines us for our good, so that we may share his holiness. All commentators find the contrast here decisive. Calvin notes the two dimensions of difference: temporal (a few days vs. a lifetime) and purposive (their best judgment vs. God's infallible wisdom aimed at our sharing his holiness). The goal — sharing in God's holiness (<em>tes hagiotetos autou</em>) — is the highest purpose conceivable for any human life, and it is named here as the explicit aim of divine chastening. Ellicott explains that earthly fathers discipline as seemed best to them — often erring in both directions, too lenient or too harsh — while God disciplines precisely for our profit. Clarke stresses that the phrase \"that we may share his holiness\" means not merely moral improvement but genuine participation in the divine nature (2 Pet 1:4): the end of discipline is not behavior management but transformation of character into the divine likeness. Barnes reads the verse as explaining the whole economy of suffering in the Christian life: no divine discipline is arbitrary or random; every affliction has the one purpose of making its recipient more holy, more like God.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>Two differences: duration (a few days vs. a lifetime) and purpose (their fallible judgment vs. God's infallible aim). The divine aim is that we may share his holiness — the highest imaginable end, which gives every affliction its ultimate justification.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>Earthly fathers discipline \"as seemed best to them\" — their estimate may be wrong in either direction. God disciplines for our profit — his estimate is always correct. The contrast is not merely quantitative (more vs. less discipline) but qualitative (fallible vs. infallible love).</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>\"That we may share his holiness\" — not merely moral improvement but participation in the divine nature. The end of divine discipline is not better behavior but genuine transformation: the disciplined soul becomes, through suffering, more truly like its Creator and Father.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>No divine affliction is arbitrary. Every trial has one purpose: to make the sufferer more holy. This transforms the entire landscape of Christian suffering — not a series of random misfortunes but a divinely orchestrated curriculum with holiness as its only goal.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "11": {
      "synthesis": "<p>For the moment all discipline seems painful rather than pleasant, but later it yields the peaceful fruit of righteousness to those who have been trained by it. Calvin warns against judging chastisements by present feelings: we are like children who dread the rod because they cannot yet judge how useful it is; aright estimation of discipline requires looking beyond the moment to the fruit it produces. Ellicott reads the verse as the epistle's general assessment of all chastening, human or divine — the parenthetical \"All chastening\" makes the statement applicable beyond the religious sphere; it resonates with universal human experience of any rigorous training. Clarke identifies the fruit — \"peaceable fruit of righteousness\" — as both holiness and happiness: the disciplined soul becomes both more holy (righteous) and more tranquil (peaceable). Wesley notes the conditional dimension: the fruit is given to \"those who have been exercised by it\" — those who receive the discipline as from God and improve it according to his will, not those who merely endure it or resist it. Barnes observes that the fruit is specifically \"peaceful,\" because discipline that produces righteousness removes the inner agitation of unresolved sin and the outer agitation of unsanctified passion.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>We must not judge chastisements by present feelings. Children dread the rod because their age prevents them from seeing its purpose. The right assessment of divine discipline requires looking beyond the moment of pain to the fruit it produces in the trained life.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>\"All chastening\" — the universality covers both human and divine discipline. The statement resonates with the common experience of any rigorous training: no athletic, intellectual, or moral discipline is pleasant in the moment, yet each yields its distinctive fruit afterward.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>\"Peaceable fruit of righteousness\" — the double quality of the fruit: holiness (righteousness) and tranquility (peace). The disciplined soul becomes more like God and more at rest within itself. These two are inseparable: the holier the life, the deeper the peace.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>The fruit is specifically \"peaceful\" because righteousness removes the inner restlessness of unresolved sin. The fruit is for those who have been \"exercised\" by the discipline — those who actively receive and respond to it rather than merely enduring or resisting it.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "12": {
      "synthesis": "<p>Therefore lift your drooping hands and strengthen your weak knees. The verse is drawn from Isaiah 35:3 — a prophetic call to courage addressed to those in the wilderness of exile. Calvin reads the application as clear: the previous teaching about the purposes of discipline should produce a rallying of courage, not continued dejection. If God is using our suffering for our good, there is no reason to let our hands hang down and our knees buckle. Ellicott notes the pastoral directness of the imperative: the readers are to act, not merely to think correctly. The arms that hang and the knees that tremble are images of exhaustion and near-collapse; they are to be deliberately strengthened by an act of will informed by the theology of the preceding verses. Clarke observes that the Isaiah context is significant: the prophet called for courage in the wilderness because deliverance was coming; the writer applies the same call to Christians because the unshakeable kingdom of vv28-29 is coming. Barnes reads this as the hinge of the chapter — the transition from doctrinal foundation (vv5-11) to practical application (vv12-17): the hands and knees must actually be strengthened, not merely taught about.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>The theology of divine discipline, properly understood, should produce a rallying of courage. If God is using our suffering for our good, there is no basis for continued despondency. The drooping hands and weak knees are healed not by the removal of suffering but by understanding its purpose.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>The imperative is direct and active: strengthen, lift up. The readers are not merely to understand the doctrine of chastening but to act on it. Arms hanging and knees trembling signal near-collapse; they are to be deliberately steadied by the will informed by truth.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>Isaiah 35:3 addressed exiles who needed courage because deliverance was coming. The application to Christians is exact: they are to strengthen their grip on the race because the unshakeable kingdom is coming — the wilderness is real but temporary; the city is real and permanent.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>This verse is the transition from doctrine to duty. The theology of chastening in vv5-11 must produce the strengthened hands and knees of v12; doctrine that does not eventuate in renewed vigor has not been received properly. The hands must actually be lifted, not merely explained.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "13": {
      "synthesis": "<p>Make straight paths for your feet so that what is lame may not be put out of joint but rather be healed. The verse echoes Proverbs 4:26 and continues the athletic imagery. Calvin reads the instruction as directed not only toward the runner but toward the community: the strong are to make smooth paths so that the weaker members — the lame — are not caused to stumble further and lose their footing entirely. Ellicott interprets the verse as an exhortation to right living: the crooked paths of compromise and sin make worse the spiritual lameness that already afflicts many; straight living heals rather than aggravates the condition. Clarke sees this as a pastoral community ethic: individual believers have responsibility for one another's progress — the strong must not take routes (theological, moral, or social) that the weak cannot follow. Barnes applies it to the community in trial: it is possible for the stronger to put extra burdens on the weaker by the way they navigate persecution, and the instruction is to choose the straight, clear path that enables the weakest member to make it through. Wesley reads the lame member as anyone in spiritual or physical weakness — the exhortation is to consider them and to avoid anything that would cause them to stumble rather than be healed.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>The strong are to make smooth paths so that the weaker members of the community are not caused to stumble or put further out of joint. The exhortation is not merely personal but communal: how we run affects how others can run, particularly those who are already struggling.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>Straight paths are paths of upright living. Crooked paths — compromises, deceptions, moral shortcuts — make worse the spiritual lameness that already afflicts the weakest. The instruction is to choose the clear, straight route that heals rather than aggravates.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>Every believer has responsibility for others' progress. The path the stronger takes is also the path the weaker must follow; if the stronger takes a route the weak cannot navigate, he has put a stumbling block rather than a smooth road before a limping traveler.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>In times of persecution especially, the way the stronger members navigate the trial can either enable or cripple the weaker. The instruction is to choose the clear path — straightforward, honest, uncompromising — that the weakest member can also follow without being put further out of joint.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "14": {
      "synthesis": "<p>Strive for peace with everyone, and for the holiness without which no one will see the Lord. The verse contains two imperatives that the commentators unanimously regard as inseparable in the Christian life. Calvin reads the double call as targeting two common human failures: the natural tendency to seek one's own interest over others' (requiring peace to be actively pursued) and the tendency to rest in external religious status without inward transformation (requiring active pursuit of holiness). Ellicott identifies an allusion to Psalm 34:14 (also cited in 1 Peter 3:11) and emphasizes that \"peace with all men\" cannot be limited to fellow Christians; the exhortation is universal in its scope. Clarke gives the Greek the strong athletic force: <em>eirenen diokete</em> — pursue peace as hunters pursue game, through all winding circumstances. Barnes reads the second clause — \"without which no one will see the Lord\" — as the most absolute statement in the chapter: there are no exceptions and no substitutes for holiness; it is the non-negotiable condition of the beatific vision. Wesley sees this verse as foundational for his entire theology of sanctification: the not-following-after holiness is the direct route to every sin; holiness is not optional but essential to the entire Christian life.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>Two natural failures are targeted: the selfishness that makes peace hard to pursue, and the complacency that mistakes external religion for the holiness of the heart. Both must be actively pursued — peace with all and holiness of life — and neither is optional for those who would see God.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>The allusion to Psalm 34:14 makes \"follow peace\" a scriptural imperative with deep roots. \"With all men\" is universal — not limited to the community of faith. The connection of peace and holiness is deliberate: a contentious life and a holy life are incompatible.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p><em>Eirenen diokete</em> — pursue peace as hunters pursue game, through every winding circumstance and in every direction. The word implies that peace will not come naturally; it must be actively, persistently sought at personal cost.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>\"Without which no one will see the Lord\" — absolute and without exception. There is no substitute for holiness, no alternative route to the beatific vision. This is the most uncompromising statement of the chapter: every reader must pursue holiness or they will not see God.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "15": {
      "synthesis": "<p>See to it that no one fails to obtain the grace of God; that no root of bitterness springs up and causes trouble and by it many become defiled. The verse introduces communal vigilance as a counterpart to individual pursuit: Christians must watch over one another. Calvin reads the phrase \"failing of the grace of God\" as falling short of, or turning back from, the grace already received — apostasy is the concern, and the community is to prevent it. Ellicott notes that <em>episkopountes</em> (looking diligently over) is the word from which \"bishop\" derives — the whole community is here given a quasi-episcopal oversight responsibility toward its own members. Clarke identifies the root of bitterness from Deuteronomy 29:18, where it describes idolatrous Israelites who turn away from God and corrupt others: a single apostate or bitter soul can defile many around them. Wesley specifies the fruits of a root of bitterness: envy, anger, and suspicion spring from it; they destroy the sweet peace of the community. Barnes emphasizes the social dynamic: spiritual failure is rarely isolated; the one who falls typically takes others with them. This makes communal vigilance not merely an act of love for the individual but self-defense for the community.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>\"Failing of the grace of God\" — turning back from, or falling short of, the grace already received. The community is to watch over its own members and not allow any to slip into apostasy unchecked. No Christian's spiritual welfare is solely their own concern.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p><em>Episkopountes</em> — the word behind \"bishop\" — the whole community exercises oversight toward its members. The defection of one brings loss to the whole body; communal vigilance is therefore not optional charity but a structural necessity of the corporate Christian life.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>The root of bitterness from Deuteronomy 29:18 described an idolater whose example corrupted the congregation. A single bitter soul — one who has turned from God or harbors deep resentment — can defile many around them before the infection is recognized or addressed.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>Spiritual failure is rarely isolated. The one who falls from grace does not fall alone; they draw others along by the force of example, influence, and the contagion of disillusionment. Communal vigilance is both love for the individual and self-protection for the community.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "16": {
      "synthesis": "<p>See that no one is sexually immoral or unholy like Esau, who sold his birthright for a single meal. Calvin reads \"profane\" (<em>bebelos</em>) as the key word here: Esau's sin was not primarily sexual but an utter indifference to sacred things — he treated his birthright, the emblem of his covenant standing and participation in the promise, as less valuable than a bowl of stew. Ellicott notes that Esau is called <em>bebelos</em> (profane, worldly, godless) — the opposite of <em>hagios</em> (holy) — and argues the primary charge is irreverence toward the sacred, not immorality; the fornicator is mentioned as a companion to the profane person, not as the same person. Clarke observes that the birthright contained the promises to Abraham — the right to the covenant, to the priestly function of the firstborn, and ultimately to the line through which the Messiah would come. To sell this for a single meal is the definitive act of a man who has no regard for eternal things. Barnes reads the warning as directed at the specific temptation of the readers: to apostatize from the new covenant promises for the sake of present relief from persecution is precisely Esau's act — trading an eternal birthright for temporal ease.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>\"Profane\" (<em>bebelos</em>) is the key word: Esau treated the sacred as worthless. His sin was not mere impulsiveness but a settled contempt for covenant realities — he regarded the birthright, which contained the promise of the Messiah, as worth less than one meal.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p><em>Bebelos</em> — profane, worldly, secular — the precise opposite of holy. Esau's defining characteristic was irreverence toward sacred things: the birthright, the covenant promise, the priestly prerogative of the firstborn. All were surrendered without hesitation for immediate appetite.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>The birthright carried the Abrahamic promises: covenant standing, priestly function of the firstborn, and the messianic lineage. To exchange all this for a single meal is not merely impulsive but reveals a soul so captive to the present that eternity has no weight in its calculations.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>The pastoral application to the readers is direct: apostatizing from the new covenant promises to escape present persecution is Esau's act exactly — trading an eternal inheritance for temporal relief. The birthright of the new covenant is worth infinitely more than anything earthly relief can offer.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "17": {
      "synthesis": "<p>For you know that afterward, when he desired to inherit the blessing, he was rejected, for he found no chance to repent, though he sought it with tears. The verse raises a significant interpretive question about the referent of \"repentance\" (<em>metanoia</em>). Calvin reads it as Esau seeking to move his father Isaac to change his mind — not that God refused Esau genuine penitence, but that the moment of the blessing, once given, could not be recalled; Isaac could not repent of what he had pronounced. Ellicott examines the grammar carefully and agrees: <em>metanoia</em> here refers to Isaac's change of mind, not Esau's repentance from sin. Clarke states this explicitly: Esau found no place of repentance in his father — the word belongs to Isaac. Wesley reads Esau as seeking to change his father's purpose, standing as one of the hearers, unable to undo what the divine economy had sealed. Barnes reviews the difficulty at length: the text could mean either (a) Esau found no repentance in himself from his profane act, or (b) he found no metanoia in Isaac, no reversal of the blessing. Barnes leans toward the latter reading while acknowledging the former is grammatically possible. The pastoral point is clear on either reading: the point of no return is real; the moment of decision, once irrevocably past, cannot be revisited by tears alone.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>Esau sought to move Isaac to change his mind about the blessing — not that God refused genuine repentance from sin, but that the spoken blessing could not be recalled. The word metanoia refers to Isaac's change of mind; what was divinely sealed through the father's word could not be undone by tears.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>The grammar supports the reading that <em>metanoia</em> refers to Isaac's change of purpose, not Esau's repentance from sin. Esau wept bitterly — Genesis 27:38 — but his tears could not move Isaac to reverse what had been divinely confirmed. The moment of the blessing was irrevocably past.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>\"He found no place of repentance\" — no place of change of mind in his father Isaac. The metanoia belongs to Isaac: Esau could find no way to bring his father to reverse the blessing. The tears were real but the decision was final — sealed by a word that had already taken effect.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>The text can mean either that Esau found no genuine repentance in himself, or that he found no change of mind in Isaac. Barnes prefers the latter: the blessing was given and could not be recalled; Esau's tears were for the lost blessing, not for the profanity that lost it. The warning stands: some moments of decision, once past, cannot be revisited.</p>"
        }
      ],
      "consensus": "mixed",
      "key_tension": "Whether <em>metanoia</em> refers to Esau's own repentance from sin (which he could not find in himself) or to Isaac's change of mind (which Esau could not move) is disputed; most commentators favor the latter reading but acknowledge the difficulty."
    },
    "18": {
      "synthesis": "<p>For you have not come to what may be touched, a blazing fire and darkness and gloom and a tempest. With this verse the chapter's great antithetical climax begins: two mountains, two covenants, two kinds of presence. Calvin explains that the writer contrasts the Gospel not with the Law abstractly but with the terrifying manner of its promulgation at Sinai — the sensory overwhelming of Israel on the day of the lawgiving. Clarke notes that the opening phrase — \"not to a mountain that may be touched\" — is sometimes mistranslated; the point is not that Sinai was literally touchable (it explicitly was not, Exod 19:12) but that it was a physical, palpable, material mountain belonging to this created order. Wesley makes the contrast sharp: what the readers have come to is not constituted from any earthly, material element; the new covenant's holy place is not a mountain that can be seen or a fire that can be felt. Barnes stresses that the list of physical phenomena — blazing fire, darkness, gloom, tempest — is drawn from Exodus 19 and Deuteronomy 4-5, and that each item was designed to produce one effect: overwhelming fear before the holy God.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>The contrast is not between the Law and the Gospel in the abstract but between the terrifying promulgation of the Law at Sinai and the joyful character of the Gospel's approach. God at Sinai manifested himself as a strict judge; God in the Gospel manifests himself as a merciful Father.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>\"A mountain that might be touched\" — a palpable, material mountain belonging to the created order. Sinai was a physical location with physical phenomena: blazing fire, deep darkness, tempest. Everything about the Sinai theophany operated on the earthly, sensory level — and produced overwhelming terror.</p>"
        },
        {
          "src": "wesley",
          "attr": "Wesley",
          "html": "<p>Ye are not come to the mountain that could be touched — that was of an earthly, material nature. This is the contrast with what follows: the mountain Christians have come to is constituted entirely otherwise, not from any element of this created order, not producing terror but drawing near in grace.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>The list — blazing fire, darkness, gloom, tempest — is drawn from Exodus 19 and Deuteronomy 4-5. Each element amplified the others to produce a single overwhelming effect: the dread of a holy God before whom no approach was possible except by his own strict terms.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "19": {
      "synthesis": "<p>And the sound of a trumpet and a voice whose words made the hearers beg that no further messages be spoken to them. Calvin explains that the second element of the Sinai terror was the divine voice itself — so overwhelming that Israel begged Moses to be the intermediary, saying they would die if God spoke to them directly (Exod 20:19). Ellicott identifies the OT references precisely: the trumpet from Exodus 19:19, the voice of words from Deuteronomy 4:12. The people did not ask to escape terror in general but specifically to stop hearing the direct divine voice. Wesley identifies the trumpet as formed by angelic ministry, preparatory to the divine words (the Ten Commandments) spoken with a loud voice (Deut 5:22). Barnes makes the pastoral application vivid: the speaker was invisible, the voice addressed hundreds of thousands in a thunderstorm, and the content was the holy Law of God — the cumulative effect was the primal human awareness of standing before an omnipotent and holy Judge who spoke and expected a response.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>The terror of the divine voice drove Israel to beg for a mediator: \"Let Moses speak to us, lest we die.\" The people were not asking for less revelation but for a human intermediary — they could not survive direct encounter with the holy God speaking from the fire and cloud.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>The trumpet from Exodus 19:19; the voice of words from Deuteronomy 4:12. The people entreated that no more words be spoken — not because they objected to the content but because the manner was beyond endurance. Even the medium of the voice was too holy to survive without protection.</p>"
        },
        {
          "src": "wesley",
          "attr": "Wesley",
          "html": "<p>The trumpet was formed, without doubt, by angelic ministry — preparatory to the divine words, the Ten Commandments, which were uttered with a loud voice (Deuteronomy 5:22). The sequence is deliberate: trumpet, then voice; angelic preparation, then divine proclamation.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>An invisible speaker addressed hundreds of thousands gathered before a mountain in a thunderstorm. The words were the holy Law; the effect was absolute terror before the holy Judge. Israel's request to stop hearing God directly was not cowardice but the accurate human response to an encounter with the living God.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "20": {
      "synthesis": "<p>For they could not endure the order that was given: If even a beast touches the mountain, it shall be stoned. The prohibition against even animals touching Sinai (Exod 19:12-13) expressed the absolute holiness-barrier between God and the created order. Ellicott notes that the following phrase — \"or thrust through with a dart\" — is absent from the best manuscripts and appears to have been added from Exodus 19:13; he excludes it from the text. Wesley explains the terror: it was not that the command itself was unreasonable but that the terror seized the hearers when they heard it proclaimed — if even an animal could not approach accidentally, how could sinful human beings approach at all? Barnes draws the pastoral point: the prohibition of animals touching the mountain was a vivid, physical declaration of the absolute exclusion of all that is unclean from God's holy presence; the fence around Sinai was a spatial gospel, teaching the doctrine of divine holiness in stone and distance before it was articulated in words.</p>",
      "voices": [
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>\"Or thrust through with a dart\" is absent from the best manuscripts and was likely added from Exodus 19:13. The core prohibition — no beast may touch the mountain or it shall be stoned — is sufficient to make the point: absolute exclusion of all that is unclean from the holy presence.</p>"
        },
        {
          "src": "wesley",
          "attr": "Wesley",
          "html": "<p>The terror was not that the command was harsh but that it revealed the absolute barrier between the holy God and all that lives. If an animal could not approach accidentally without judgment, how could sinful human beings approach intentionally? The fence around Sinai declared the holiness-barrier in physical form.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>The prohibition of animals touching the mountain was a spatial declaration of the doctrine of divine holiness. The fence was not arbitrary but expressive: the space between God's holy mountain and the camp of Israel measured the distance between God's holiness and human sinfulness — a distance that no animal or human could cross without death.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "21": {
      "synthesis": "<p>Indeed, so terrifying was the sight that Moses said, \"I tremble with fear.\" This detail is not found verbatim in the Exodus narrative of the lawgiving; in Deuteronomy 9:19 Moses expresses similar fear, though in a different context (the golden calf incident). Ellicott examines the discrepancy carefully: the Deuteronomy text applies to a later event, but the writer may have a fuller tradition or applies Moses's recorded fear to the original Sinai theophany. Barnes devotes considerable space to the difficulty and concludes the writer may be drawing on a reliable tradition, or using Deuteronomy 9:19 as evidence that Moses did experience overwhelming fear in God's presence — whenever and wherever it was expressed. Wesley observes that Moses was admitted to the closest human intercourse with God — God spoke to him as a friend — yet when the Ten Commandments were pronounced, he stood among the hearers as one of them, not as a privileged intimate. Even the most spiritually advanced human being was undone by the direct, unmediated holiness of God. The point of the whole Sinai section (vv18-21) is now complete: the whole scene was designed to produce one thing — the recognition that sinful humanity cannot approach a holy God on its own terms.</p>",
      "voices": [
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>Deuteronomy 9:19 records Moses's fear in the context of the golden calf, not the original lawgiving. The writer may draw on a fuller tradition, or the recorded fear of Moses in God's presence is taken as evidence of what he experienced at Sinai. The fact of Moses's fear, whenever expressed, is what matters for the argument.</p>"
        },
        {
          "src": "wesley",
          "attr": "Wesley",
          "html": "<p>God spoke to Moses face to face as a man speaks with his friend — the most intimate human-divine relationship in the old economy. Yet when the Ten Words were pronounced, Moses stood among the hearers, as one of the people, not in his privileged role. Even Moses was undone at Sinai.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>The detail about Moses's fear may come from a reliable tradition not preserved in Exodus, or may apply Deuteronomy 9:19 to the lawgiving context. Either way the point is clear: if Moses — the friend of God, the mediator of the covenant — trembled, what could any ordinary Israelite, or any unmediated sinner, have survived in that presence?</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "22": {
      "synthesis": "<p>But you have come to Mount Zion and to the city of the living God, the heavenly Jerusalem, and to innumerable angels in festal gathering. The contrast with vv18-21 is complete and deliberate. Calvin explains that the writer alludes to OT prophecies (Isa 2:1-4 and others) in which God promised that the gospel would go forth from Zion: the contrast with Sinai is not merely spatial (one mountain vs. another) but eschatological (the terror of the law vs. the joy of the gospel). Ellicott notes the careful language: \"you have come\" — the perfect tense, indicating a completed arrival; Christians are not approaching Zion but already there in Christ. Clarke develops the city metaphor: the church is called the city of the living God, the heavenly Jerusalem — not because it is ethereal but because its constitution, its citizenship, and its head are from above. Barnes identifies the \"innumerable angels in festal gathering\" as the first of seven constituent elements of the heavenly assembly that Christians approach (vv22-24) — the angelic host assembled not in terror (as at Sinai) but in <em>paneguris</em>, the joyful festival gathering. Wesley draws the pneumatological dimension: believers are already in communion with the church triumphant, though this is more visible to heavenly than earthly eyes.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>The contrast with Sinai is eschatological: the terror of the law's promulgation versus the joy of the gospel's invitation. God at Sinai ascended his tribunal; God at Zion opens his arms. The prophecies of Isaiah and others promised that the gospel would go from Zion — and now it has.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>\"You have come\" — perfect tense, a completed arrival. Christians are not approaching Zion; they are already there in Christ. The heavenly Jerusalem is not a future destination alone but a present reality entered by faith, though its full enjoyment waits for the resurrection.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>The church is the city of the living God, the heavenly Jerusalem — not because it is immaterial but because its citizenship, its constitution, and its king are from above. The living God, not a dead idol, dwells in this city; its life is divine and therefore indestructible.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>The first of seven elements of the heavenly assembly: innumerable angels in <em>paneguris</em> — festal gathering. At Sinai the angels were agents of terrifying law (Gal 3:19; Acts 7:53); at Zion they are assembled in festivity. The same beings appear in entirely different postures in the two dispensations.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "23": {
      "synthesis": "<p>And to the assembly of the firstborn who are enrolled in heaven, and to God the Judge of all, and to the spirits of the righteous made perfect. Calvin identifies the \"firstborn\" as the patriarchs and distinguished saints of the ancient church — not all God's children indiscriminately, but those of preeminent honor — enrolled in heaven as citizens of the heavenly city. Ellicott notes that believers approach not only the saints but God himself in his judicial capacity — \"Judge of all\" might seem terrifying, but in this context it is a comfort: the one who judges all will judge in favor of those who come through Christ. Clarke develops the corporate dimension: the assembly (Greek <em>ekklesia</em>) of the firstborn is the whole body of true believers, both on earth and in paradise — the church universal across time and space gathered before God. Barnes draws attention to \"spirits of the righteous made perfect\": these are OT believers who died in faith, imperfectly satisfied during their earthly lives because Christ had not yet come, but now fully perfected by his completed work. Wesley finds in \"the firstborn enrolled in heaven\" the echo of Moses's enrollment of the Israelite firstborn: these first-born of the new Israel are registered as citizens of heaven, not merely visitors.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>The firstborn enrolled in heaven are the patriarchs and eminent saints of the old economy — called firstborn not because all God's children are not his but as a title of honor for those preeminent in faith. Their enrollment in heaven makes them citizens of the city Christians now approach.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>\"God the Judge of all\" — in this context a comfort, not a terror. The Judge is the one whom Christians approach through Christ; his verdict, already declared in the gospel, is in their favor. They draw near not to a Judge who may condemn but to one who has acquitted them in the Son.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>The general assembly (<em>ekklesia</em>) of the firstborn — the universal church across all times and places, on earth and in paradise. The word <em>paneguris</em> (festal gathering) of verse 22 and <em>ekklesia</em> here together present the heavenly community as both celebratory and constituted.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>\"Spirits of the righteous made perfect\" — OT believers who died in faith, imperfectly satisfied because Christ had not yet come, but now fully perfected by his completed sacrifice. What the old covenant promised, Christ's death delivered retroactively for all who believed the promise.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "24": {
      "synthesis": "<p>And to Jesus, the mediator of a new covenant, and to the sprinkled blood that speaks a better word than the blood of Abel. Calvin identifies this as the climax of the whole catalogue: it is through Jesus and only through Jesus that Christians have access to everything named in vv22-23. He notes the blood of sprinkling speaks better than Abel's because Abel's blood cried for vengeance from the ground while Christ's blood speaks of propitiation — it cries not for justice against the murderer but for mercy for the sinner. Ellicott observes a subtle shift in the Greek word for \"new\" here: elsewhere in the epistle the word is <em>kainos</em> (new in kind), but here <em>neos</em> (new in time) — the covenant is recent, freshly inaugurated by Christ's death. Clarke develops the Abel contrast: Abel's murder was the first cry of martyred blood in human history; Christ's blood is the last and definitive answer to the entire sequence of blood-cries that began there. Barnes reads the verse devotionally: Christians come to the mediator who is present, the blood that avails, the covenant that is active — all things secured and currently effective, not merely remembered or anticipated. Wesley finds the blood of sprinkling to be the foundation of Christ's entire mediatorial office.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>Abel's blood cried for vengeance; Christ's blood speaks of propitiation. The difference is absolute: the one demanded justice against the murderer; the other pleads mercy for the sinner. Christ's blood is the better word precisely because it answers the cry of the law with the voice of grace.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p><em>Neos</em> here (new in time), unlike <em>kainos</em> (new in kind) elsewhere in the epistle — the covenant is freshly inaugurated. The blood of sprinkling recalls the Day of Atonement and Exodus 24: Christ's blood does for the new covenant what Moses's blood did for the old, but infinitely more.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>Abel's murder was the first blood-cry in human history. Christ's blood is the answer to the entire subsequent sequence: every martyred blood-cry from Abel to the last martyr finds its final answer in the blood of sprinkling that speaks propitiation rather than vengeance.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>Christians come to a mediator who is present, blood that currently avails, and a covenant that is actively in force. The language is not memorial but immediate: these realities are not past events to be remembered but present powers to be relied upon moment by moment.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "25": {
      "synthesis": "<p>See that you do not refuse him who is speaking. For if they did not escape when they refused him who warned them on earth, much less will we escape if we reject him who warns from heaven. Calvin identifies this as the epistle's most solemn warning: the whole Sinai-to-Zion comparison has been made to establish this single conclusion. If refusing the earthly warning brought judgment, refusing the heavenly warning brings incomparably greater judgment. Ellicott uses the same verb (<em>paraiteomai</em>) that appeared in 12:19, where Israel entreated that God not speak further — the readers are warned not to repeat Israel's fatal error of declining to hear. Clarke identifies \"him that spake on earth\" as Moses — whose words, transgressed, brought death in the wilderness — and \"him that speaks from heaven\" as Christ, whose gospel, refused, brings a proportionally greater reckoning. Barnes underscores the gravity of the comparison: Israel under the law had the most solemn external warning in history and still disobeyed; if external terror was insufficient to hold them, only greater grace and greater warning together can hold the readers. Wesley reads this as the chapter's practical climax: the voice that will shake heaven and earth already speaks in the gospel; to refuse it now is to refuse the final word.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>The whole Sinai-to-Zion comparison was built to establish this warning: if the earthly refusal brought judgment, the heavenly refusal brings incomparably greater judgment. The gospel's greater grace entails greater responsibility and greater peril for those who turn away.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p><em>Paraiteomai</em> — the same word used in 12:19 where Israel entreated that God stop speaking. The readers are warned not to repeat that fatal act of refusal. To turn away from the gospel voice is to repeat Israel's Sinai error, but with higher stakes and no further revelation beyond it.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>\"Him that spake on earth\" = Moses; \"him that speaketh from heaven\" = Christ. Every transgression of Moses's word brought condemnation (2:2); to transgress the word of the Son of God, who came from heaven and now speaks from heaven, can only bring a proportionally greater reckoning.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>Israel at Sinai had the most solemn external warning possible — fire, earthquake, divine voice — and still disobeyed. External terror proved insufficient. Only the internal grace of the gospel working through the Spirit can hold a person to God; to refuse it is to refuse the only thing that can save.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "26": {
      "synthesis": "<p>At that time his voice shook the earth, but now he has promised, \"Yet once more I will shake not only the earth but also the heavens\" (Haggai 2:6). Calvin reads the two shakings as contrasts of scale: Sinai's earthquake was local and earthly; the promised eschatological shaking will be cosmic. The quotation from Haggai 2:6 is a prophecy of the Messianic age, and the writer applies it to the eschatological consummation still ahead. Ellicott notes that the writer uses the Haggai prophecy to describe the decisive upheaval associated with the first coming of Christ (the revolution it produced) but also the final shaking at his second coming — the text carries both a historical and an eschatological referent. Clarke focuses on the contrast: the shaking at Sinai was the shaking of one mountain; the promised shaking is of heaven and earth together — the entire created order will be convulsed at the final judgment. Barnes reads \"yet once more\" (<em>eti hapax</em>) as indicating the unique, unrepeatable character of the coming event: what is about to happen will be final and decisive, leaving nothing of the shakeable order standing.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>Sinai's shaking was local — one mountain, one moment in Israel's history. The promised shaking is cosmic — heaven and earth together. The scale of the contrast prepares the reader for what follows: if the local shaking produced such terror, how should the cosmic shaking be received?</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>The Haggai prophecy has both a historical referent (the upheaval produced by Christ's first coming) and an eschatological one (the final consummation). The writer uses it to point forward: God has promised a shaking that will make the Sinai earthquake look local and preparatory by comparison.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>At Sinai only a mountain shook; the promised shaking is of heaven and earth — the entire created order. This is the eschatological judgment that brings the present age to its end, removing everything that belongs to the temporary order so that what is eternal may stand alone.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>\"Yet once more\" — unique and unrepeatable. The coming event will be the final decisive act: the shakeable order will be removed entirely, leaving only what God has made unshakeable. This once-more-and-no-more character of the coming shaking makes the present invitation to receive the kingdom all the more urgent.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "27": {
      "synthesis": "<p>This phrase \"yet once more\" indicates the removal of things that are shaken — that is, things that have been made — in order that the things that cannot be shaken may remain. Calvin reads this as the key to the whole eschatology of the passage: the created order as it now stands is provisional, capable of being shaken, and destined to be removed. What is unshakeable — the kingdom of God, the church of the firstborn, the new creation — will alone survive the final convulsion. Ellicott notes the Greek distinction the writer draws between made things (subject to shaking and removal) and unshakeable things (which will remain): the former category includes not only physical structures but all earthly institutions and arrangements — the Jewish temple, the Roman empire, and everything else that belongs to the <em>kosmos</em> as it stands. Clarke stresses that the removal is purposive: it is to allow what cannot be shaken to be more clearly seen and more fully possessed. Barnes identifies the pastoral application: Christians possess the unshakeable kingdom now, by faith; the coming shaking will not destroy them but reveal them as possessors of what nothing can take away. Wesley finds here the ground of all Christian confidence: the kingdom they hold is immune to every force that can shake the world.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>\"Made things\" are capable of being shaken and will be removed. What is unshakeable — the kingdom of God, the new creation — will alone remain when the convulsion comes. The eschatology is clarifying: the temporary world will be shaken away so that the eternal reality is fully revealed.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>The distinction is between made things (temporal, provisional, subject to removal) and unshakeable things (eternal, divinely constituted, permanent). This includes not only physical structures but all earthly institutions — everything that belongs to the present age will be subjected to the final shaking.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>The removal is purposive — not destruction for its own sake but the clearing away of what is temporary so that what is eternal may stand without competition. The shaking reveals the kingdom; it does not threaten it. The citizen of the unshakeable kingdom has nothing to fear from the shakeable world's end.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>Christians possess the unshakeable kingdom already, by faith. The coming shaking will not destroy them but reveal them as the only possessors of what cannot be taken away. When everything else is removed, the kingdom will stand — and they will stand with it as its citizens.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "28": {
      "synthesis": "<p>Therefore let us be grateful for receiving a kingdom that cannot be shaken, and thus let us offer to God acceptable worship, with reverence and awe. Ellicott identifies this as the practical conclusion of the entire passage: the unshakeable kingdom has been received — <em>paralambano</em>, received as a gift handed down — and the appropriate response is worship conducted with reverence and godly fear. Clarke argues that the kingdom here is the Gospel dispensation, in which God reigns among his people through the Spirit — it cannot fail because it is the last and final economy, never to be replaced. Barnes emphasizes the word \"receiving\" (<em>paralambano</em>): the kingdom is not being built or earned but received — it is a gift that calls for gratitude, not an achievement that calls for pride. Wesley combines reverence with joy: receiving a kingdom that cannot be moved calls for grateful, reverent service — not the servile fear of a slave but the holy awe of a child conscious of his own unworthiness and of his Father's gracious majesty. The verse thus gathers the whole chapter's theology (suffering, discipline, eschatology, two mountains) into a single devotional imperative: worship God acceptably.</p>",
      "voices": [
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p><em>Paralambano</em> — received as a gift handed over. The kingdom is not earned by faithful endurance but received by grace; endurance is the appropriate response of those who have received, not the condition of receiving. The gift calls for gratitude expressed in acceptable worship.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>The kingdom of God — the Gospel dispensation, the reign of God in the hearts of believers through the Spirit — cannot fail because it is the final economy, never to be replaced or superseded. Sinai gave way to Zion; Zion gives way to nothing. This permanence grounds the gratitude.</p>"
        },
        {
          "src": "wesley",
          "attr": "Wesley",
          "html": "<p>With reverence — literally, with shame, arising from a deep consciousness of our own unworthiness. And with godly fear — a tender, jealous fear of offending, arising from a sense of the gracious majesty of God. These two together constitute the posture of acceptable Christian worship: grateful humility before a gracious king.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>\"Receiving\" — the kingdom is a gift, not an achievement. Gratitude is the only appropriate first response. From gratitude comes worship; from worship, reverence; from reverence, the godly fear that keeps the worshipper from turning away from the one who has given everything.</p>"
        }
      ],
      "consensus": "affirm",
      "key_tension": None
    },
    "29": {
      "synthesis": "<p>For our God is a consuming fire (Deut 4:24). Calvin observes that the chapter closes as it opened, with an appeal to both love and severity: God began by alluring with his grace and now concludes with the reminder of his severity, so that nothing is left undone to draw the readers to faithful perseverance. The fire that consumed the offerings at the altar, and the fire that would consume those who refused God's approach, are both aspects of the same divine holiness. Ellicott notes the Deuteronomy context: the words follow a solemn warning against idolatry, placing this verse in the same category as 10:27-28 and 10:30 — the consuming-fire warnings of the epistle. Clarke draws the direct line from Sinai to the Gospel: sin under the Gospel is as abominable in God's sight as it was under the Law; the fire of God's holiness does not diminish across the dispensations. Barnes reads the verse as the final word of the entire comparison: the joyful Mount Zion of vv22-24 and the consuming fire of v29 are both true of the same God simultaneously — to receive his grace with gratitude (v28) is to stand in the fire without being consumed; to refuse his grace is to stand in the same fire with nothing to protect from it. Wesley finds here the final answer to any who would use the grace of the gospel to lower their guard: our God is still a consuming fire, in the strictness of his justice and the purity of his holiness.</p>",
      "voices": [
        {
          "src": "calvin",
          "attr": "Calvin",
          "html": "<p>God closes by appealing to both love and severity, having begun with grace and now ending with the reminder of his consuming holiness. He omits nothing that might draw his people to perseverance: the allure of grace and the dread of the fire are both instruments of the divine love for our souls.</p>"
        },
        {
          "src": "ellicott",
          "attr": "Ellicott",
          "html": "<p>Deuteronomy 4:24 follows a warning against idolatry. The consuming fire passage belongs to the same family as 10:27-30 — the epistle's solemn warnings of judgment for those who persistently refuse the living God. The grace of the new covenant does not remove the holiness of its Giver.</p>"
        },
        {
          "src": "clarke",
          "attr": "Clarke",
          "html": "<p>Sin under the Gospel is as abominable to God as sin under the Law. The fire of his holiness is not moderated by the dispensation; only the protection available to the worshipper changes. Those in Christ stand in the fire covered; those outside Christ stand in it exposed.</p>"
        },
        {
          "src": "barnes",
          "attr": "Barnes",
          "html": "<p>The joyful Mount Zion and the consuming fire are both true of the same God. To receive his grace is to stand in the fire as the burning bush — touched by the flame but not destroyed. To refuse his grace is to stand in the same fire with nothing between the holiness of God and the sinfulness of man.</p>"
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
    count = len(HEBREWS["12"])
    print(f"Hebrews 12 synthesis complete: {count} verses.")

if __name__ == '__main__':
    main()
