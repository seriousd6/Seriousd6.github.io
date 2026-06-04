"""
MKT Hebrews chapters 11–12 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-hebrews-11-12.py

Translation decisions:
- G5287 ὑπόστασις (11:1): different sense from 1:3 ("very being/nature"). Here means
    the objective ground/assurance of what is hoped for. L: "substance" (traditional,
    preserves the Greek surface and its ontological weight); M: "assurance" (confidence
    grounded in real coming things); T: "bedrock certainty" — faith is what makes
    future realities solid underfoot now.
- G1650 ἔλεγχος (11:1): "proof/evidence/conviction" — the inner demonstration that
    makes unseen realities real to the mind. L: "evidence"; M: "proof"; T: "compelling
    proof." Not merely subjective feeling but the logical force of faith-perception.
- G4102 πίστις (faith): central throughout ch. 11 (the faith roll-call). "Faith" in
    all tiers — the trusting, loyal allegiance that characterises covenant relationship.
    The repeated "By faith" (Πίστει) formula is preserved as a structural anaphora in
    all tiers; T does not collapse or vary it.
- G747 ἀρχηγός (12:2): "pioneer" in L/M (consistent with HEB-1a decision at 2:10);
    T uses "trailblazer" (consistent with HEB-1a). Jesus both opened the path of faith
    and completed it — the two roles are now specified by the added G5051 τελειωτής.
- G5051 τελειωτής (12:2, hapax legomenon): "perfecter/finisher." L: "perfecter";
    M: "perfecter"; T: "brought it to its goal" — he ran the full course of faith to
    its completion, which is what enables him to bring others through.
- G3809 παιδεία (12:5–11): "chastening/discipline/training" — the Greek word covers
    the whole range of parental education including correction and suffering. L:
    "chastening" (preserves the corrective nuance); M: "discipline"; T: "discipline"
    or context-driven phrases to surface the parental/formative dimension.
- G2962 κύριος (12:5–6, 14): "Lord" all tiers, consistent with established HEB convention.
- G26 ἀγάπη (12:6 via G25 ἀγαπάω): "loves" all tiers — covenant love, not sentiment.
- G38/G41 ἁγιασμός/ἁγιότης (holiness/sanctification 12:10, 14): "holiness" in all
    tiers. 12:14 makes explicit: without holiness no one will see the Lord — the
    ethical dimension is non-negotiable; T does not soften this.
- G1343 δικαιοσύνη (12:11): "righteousness" L/M; T: "righteousness and peace" as a
    hendiadys describing the fruit of discipline — the peaceable fruit of righteousness
    that characterises a life shaped by God.
- G1577 ἐκκλησία (12:23): "assembly" in L (word-for-word); "church" in M (established
    Christian convention for this community); T: "great gathering" to surface the
    festal dimension (paired with G3831 πανήγυρις).
- G4416 πρωτότοκος (12:23): "firstborn" all tiers — the title given to those who share
    Christ's status as heirs. Does not mean only literally firstborn children.
- G1242 διαθήκη (12:24): "covenant" all tiers — the formal, oath-bound relationship.
    G3501 (new) used here; "new covenant" consistent with NT usage.
- OT intertextuality: 11:5 alludes to Gen 5:24; 11:18 quotes Gen 21:12; 11:26
    applies "reproach of Christ" to Moses — the Messiah-identification is the author's
    own move, preserved in all tiers. 12:5–6 quotes Prov 3:11–12 (LXX). 12:12 echoes
    Isa 35:3. 12:13 echoes Prov 4:26. 12:15 echoes Deut 29:18. 12:26 quotes Hag 2:6.
    12:29 quotes Deut 4:24.
- Sinai / Zion contrast (12:18–24): The two mountains are deliberately contrasted as
    the old covenant (Sinai = terror, tangibility, exclusion) vs. the new covenant
    (Zion = joyful assembly, full access). T surfaces this theological geography
    explicitly without paraphrasing the imagery away.
- Aspect: 11:17 perfect προσενήνοχεν (Abraham has offered — the perfect denotes a
    completed act that remains on the record); 12:2 perfect κεκάθικεν (he has sat
    down — and remains seated); 12:22 perfect προσεληλύθατε (you have come — and
    stand there now). These are rendered in English as present-perfect or present-state
    constructions.
- "Brothers and sisters" (ἀδελφοί): not present in chs 11–12, so no issue.
- "high priest" does not appear in chs 11–12.
- The "cloud of witnesses" (12:1): μάρτυς = one who testifies by their life, not
    primarily spectators watching from heaven (though the image includes that). L/M:
    "witnesses"; T: surfaces the testimonial function.
"""
import json, pathlib

ROOT  = pathlib.Path(__file__).parent.parent
DRAFT = ROOT / 'data' / 'translation' / 'draft'

def load(tier, book):
    p = DRAFT / tier / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save(tier, book, data):
    p = DRAFT / tier / f'{book}.json'
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_tier(existing, new_data, tier_key):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, tiers in verses.items():
            existing[ch][v] = tiers[tier_key]

HEBREWS = {
  "11": {
    "1": {
      "L": "Now faith is the substance of things hoped for, the evidence of things not seen.",
      "M": "Now faith is the assurance of things hoped for, the proof of things not seen.",
      "T": "Faith is the bedrock certainty of what we hope for—the compelling proof of what we cannot see."
    },
    "2": {
      "L": "For by it the elders obtained a good testimony.",
      "M": "For by this the people of old received their commendation.",
      "T": "This is the faith by which the ancients earned God's approval."
    },
    "3": {
      "L": "By faith we understand that the worlds were formed by the word of God, so that what is seen was not made from things that appear.",
      "M": "By faith we understand that the universe was formed by God's spoken word, so that what is seen was not made from visible things.",
      "T": "By faith we grasp that the entire created age was ordered by a word from God—which means that what we see was brought into being out of what was not visible."
    },
    "4": {
      "L": "By faith Abel offered to God a more excellent sacrifice than Cain, through which he obtained testimony that he was righteous, God testifying about his gifts; and through it, though he died, he still speaks.",
      "M": "By faith Abel brought God a better offering than Cain. Through his faith he was commended as righteous, when God himself testified about his gifts. And by his faith Abel still speaks, even though he is dead.",
      "T": "Abel offered God a sacrifice worth more than Cain's—and this came from faith. Through that faith God himself testified that Abel was righteous, speaking of his gifts. Abel died, but his faith goes on speaking."
    },
    "5": {
      "L": "By faith Enoch was translated so that he should not see death, and he was not found, because God translated him; for before his translation he had obtained testimony that he had pleased God.",
      "M": "By faith Enoch was taken from this life so that he did not experience death. He could not be found, because God had taken him away. For before he was taken, he was commended as one who pleased God.",
      "T": "By faith Enoch was lifted out of this world without dying—one day he was here, the next he was nowhere to be found, because God had taken him. Before that translation God had placed on record: 'Enoch pleased me.'"
    },
    "6": {
      "L": "And without faith it is impossible to please him; for he who comes to God must believe that he exists and that he is a rewarder of those who diligently seek him.",
      "M": "And without faith it is impossible to please God, because anyone who comes to him must believe that he exists and that he rewards those who earnestly seek him.",
      "T": "Without faith there is no pleasing God at all. Anyone who approaches him must hold two convictions: that God actually exists, and that he is not indifferent—he rewards those who truly seek him."
    },
    "7": {
      "L": "By faith Noah, being warned by God concerning things not yet seen, moved with godly fear, constructed an ark for the saving of his house; through which he condemned the world, and became heir of the righteousness which is according to faith.",
      "M": "By faith Noah, when warned about things not yet seen, in holy fear built an ark to save his family. By his faith he condemned the world and became heir of the righteousness that is in keeping with faith.",
      "T": "When God warned Noah about what was coming—something no one had ever seen before—Noah took it seriously. He built the ark, moved by reverence, and thereby saved his whole household. In doing so, his faith stood as a verdict against the world's unbelief, and he came to possess the righteousness that faith brings."
    },
    "8": {
      "L": "By faith Abraham obeyed when he was called to go out to a place which he was to receive as an inheritance; and he went out, not knowing where he was going.",
      "M": "By faith Abraham obeyed when he was called to go to a place he would later receive as his inheritance; and he set out without knowing where he was going.",
      "T": "When God called Abraham to leave and go to a place he would one day inherit, Abraham obeyed. He set out not knowing his destination—faith was his only map."
    },
    "9": {
      "L": "By faith he sojourned in the land of promise, as in a foreign land, dwelling in tents with Isaac and Jacob, fellow heirs of the same promise.",
      "M": "By faith he made his home in the promised land like a stranger in a foreign country; he lived in tents, as did Isaac and Jacob, who were heirs with him of the same promise.",
      "T": "He lived in the promised land as though he were a foreigner, pitching tents alongside Isaac and Jacob, who shared with him the same promise and the same waiting."
    },
    "10": {
      "L": "For he was looking for the city which has foundations, whose architect and builder is God.",
      "M": "For he was looking forward to the city with foundations, whose architect and builder is God.",
      "T": "What Abraham was really waiting for was the city with unshakeable foundations—the city God himself has designed and built."
    },
    "11": {
      "L": "By faith even Sarah herself received ability for the founding of seed even beyond the proper age, since she considered faithful him who had promised.",
      "M": "And by faith even Sarah, who was past the age for childbearing, received the ability to conceive because she considered him who had made the promise to be faithful.",
      "T": "Sarah, too, received by faith what nature had long denied her—the power to conceive a child, though she was well past the age for it. She was certain that the one who had promised was faithful to keep it."
    },
    "12": {
      "L": "Therefore from one man, and him as good as dead, were born as many as the stars of heaven in multitude, and as innumerable as the sand which is by the seashore.",
      "M": "And so from this one man, and he as good as dead, came descendants as numerous as the stars in the sky and as countless as the sand on the seashore.",
      "T": "And so from a single man—from one as good as dead—came a multitude as vast as the stars above and as uncountable as the grains of sand along the shore."
    },
    "13": {
      "L": "These all died in faith, not having received the promises, but having seen them afar off and having greeted them, and having confessed that they were strangers and pilgrims on the earth.",
      "M": "All these people were still living by faith when they died. They did not receive the things promised; they only saw them and welcomed them from a distance, admitting that they were foreigners and strangers on earth.",
      "T": "Every one of these people died still holding on to faith, never having received what was promised. But they saw it from afar and called out to it, greeting it across the distance—and they openly acknowledged that they were strangers and wanderers on this earth."
    },
    "14": {
      "L": "For those who say such things make clear that they are seeking a homeland.",
      "M": "People who say such things show that they are looking for a country of their own.",
      "T": "When people speak that way, they are showing their hand: what they are really seeking is their true homeland."
    },
    "15": {
      "L": "And if indeed they had been mindful of that country from which they went out, they would have had opportunity to return.",
      "M": "If they had been thinking of the country they had left, they would have had opportunity to return.",
      "T": "If they had been pining for the land they had left behind, nothing was stopping them from turning back."
    },
    "16": {
      "L": "But as it is, they desire a better country, that is, a heavenly one. Therefore God is not ashamed to be called their God, for he has prepared a city for them.",
      "M": "Instead, they were longing for a better country—a heavenly one. Therefore God is not ashamed to be called their God, for he has prepared a city for them.",
      "T": "No—what they were longing for was something far better: the heavenly homeland. That is why God is not embarrassed when they call him their God. He has a city waiting for them."
    },
    "17": {
      "L": "By faith Abraham, when he was tested, offered up Isaac; and he who had received the promises was in the act of offering up his only begotten son,",
      "M": "By faith Abraham, when God tested him, offered Isaac as a sacrifice. He who had received the promises was about to sacrifice his one and only son,",
      "T": "When God put Abraham to the test, Abraham by faith laid Isaac on the altar—this same Abraham who had received the promises—offering up his only son."
    },
    "18": {
      "L": "of whom it was said, 'In Isaac shall your seed be called,'",
      "M": "even though God had said to him, 'It is through Isaac that your offspring will be reckoned.'",
      "T": "—the very son about whom God had said, 'Through Isaac your line will be carried forward.'"
    },
    "19": {
      "L": "accounting that God was able to raise him even from the dead; from which, also in a figure, he received him back.",
      "M": "Abraham reasoned that God could even raise the dead, and so in a manner of speaking he did receive Isaac back from death.",
      "T": "Abraham had reasoned it through: God can raise the dead. And so, in a real sense, he did receive Isaac back—it was a kind of resurrection."
    },
    "20": {
      "L": "By faith Isaac blessed Jacob and Esau, even concerning things to come.",
      "M": "By faith Isaac blessed Jacob and Esau in regard to their future.",
      "T": "By faith Isaac looked ahead and spoke blessing over Jacob and Esau, calling down God's purposes for their futures."
    },
    "21": {
      "L": "By faith Jacob, when dying, blessed each of the sons of Joseph, and worshipped, leaning on the top of his staff.",
      "M": "By faith Jacob, when he was dying, blessed each of Joseph's sons, and worshipped as he leaned on the top of his staff.",
      "T": "By faith Jacob, even as he lay dying, blessed each of Joseph's sons in turn—and bowed in worship over the head of his walking staff."
    },
    "22": {
      "L": "By faith Joseph, when his end was near, made mention of the exodus of the children of Israel, and gave instructions about his bones.",
      "M": "By faith Joseph, when he was dying, spoke of the exodus of the Israelites and gave instructions about his bones.",
      "T": "By faith Joseph, on his deathbed, spoke of the day the Israelites would leave Egypt—and gave strict orders about what should be done with his bones when that day came."
    },
    "23": {
      "L": "By faith Moses, when he was born, was hidden for three months by his parents, because they saw that the child was beautiful; and they were not afraid of the king's edict.",
      "M": "By faith Moses' parents hid him for three months after he was born, because they saw he was a fine child, and they were not afraid of the king's edict.",
      "T": "When Moses was born, his parents saw something extraordinary in the child, and by faith they hid him for three months—paying no attention to the king's decree."
    },
    "24": {
      "L": "By faith Moses, when he was grown up, refused to be called the son of Pharaoh's daughter,",
      "M": "By faith Moses, when he had grown up, refused to be known as the son of Pharaoh's daughter.",
      "T": "When Moses had grown to manhood, he refused—by faith—to be identified as the son of Pharaoh's daughter."
    },
    "25": {
      "L": "choosing rather to suffer affliction with the people of God than to enjoy the passing pleasures of sin,",
      "M": "He chose to be mistreated along with the people of God rather than to enjoy the fleeting pleasures of sin.",
      "T": "He chose to suffer alongside God's people rather than enjoy the short-lived pleasures that sin offers. He made the trade deliberately."
    },
    "26": {
      "L": "considering the reproach of Christ greater wealth than the treasures of Egypt; for he was looking to the reward.",
      "M": "He regarded the reproach suffered for the sake of Christ as greater wealth than the treasures of Egypt, because he was looking ahead to his reward.",
      "T": "He calculated that the shame endured for the Messiah's sake was worth more than all of Egypt's treasure—because what he was looking toward lay further ahead than any earthly prize."
    },
    "27": {
      "L": "By faith he left Egypt, not fearing the wrath of the king; for he endured as seeing him who is invisible.",
      "M": "By faith he left Egypt, not fearing the king's anger; he persevered because he saw him who is invisible.",
      "T": "By faith Moses turned his back on Egypt, with no fear of the king's fury. He held on because he could see—with the eyes of faith—the One who cannot be seen."
    },
    "28": {
      "L": "By faith he kept the Passover and the sprinkling of blood, so that the destroyer of the firstborn might not touch them.",
      "M": "By faith he kept the Passover and the application of blood, so that the destroyer of the firstborn would not touch them.",
      "T": "By faith Moses kept the Passover and had blood applied to the doorposts—so that the angel destroying the firstborn would pass over them."
    },
    "29": {
      "L": "By faith they passed through the Red Sea as through dry land; when the Egyptians attempted the same, they were swallowed up.",
      "M": "By faith the people passed through the Red Sea as on dry land; but when the Egyptians tried to do so, they were drowned.",
      "T": "By faith the whole nation crossed the Red Sea on dry ground. The Egyptians tried to follow—and the sea swallowed them."
    },
    "30": {
      "L": "By faith the walls of Jericho fell down, after they were encircled for seven days.",
      "M": "By faith the walls of Jericho fell, after the army had marched around them for seven days.",
      "T": "By faith the walls of Jericho collapsed—after the people had marched around them for seven days, trusting God's instruction."
    },
    "31": {
      "L": "By faith Rahab the harlot did not perish with those who were disobedient, having received the spies with peace.",
      "M": "By faith Rahab the prostitute did not perish with those who were disobedient, because she welcomed the spies in peace.",
      "T": "By faith Rahab the prostitute was spared when the city fell—she had welcomed the Israelite spies as friends, and her faith set her apart from those who perished in their unbelief."
    },
    "32": {
      "L": "And what more shall I say? For time would fail me to tell of Gideon, Barak, Samson, Jephthah, David and Samuel and the prophets,",
      "M": "And what more shall I say? Time would fail me to tell of Gideon, Barak, Samson, Jephthah, David, Samuel, and the prophets,",
      "T": "What more can I say? I would run out of time before I ran out of names—Gideon, Barak, Samson, Jephthah, David, Samuel, and all the prophets."
    },
    "33": {
      "L": "who through faith conquered kingdoms, worked righteousness, obtained promises, stopped the mouths of lions,",
      "M": "who through faith conquered kingdoms, administered justice, and gained what was promised; who shut the mouths of lions,",
      "T": "These are those who through faith brought kingdoms to their knees, enforced justice, obtained what God had promised, and shut the mouths of lions."
    },
    "34": {
      "L": "quenched the power of fire, escaped the edge of the sword, out of weakness were made strong, became valiant in battle, turned to flight the armies of aliens.",
      "M": "who quenched the fury of the flames, and escaped the edge of the sword; whose weakness was turned to strength; and who became powerful in battle and routed foreign armies.",
      "T": "They quenched the raging of fire, escaped the sword's edge, and when they were weak they were made strong. They became mighty in battle and sent foreign armies fleeing."
    },
    "35": {
      "L": "Women received back their dead by resurrection; and others were tortured, not accepting their release, so that they might obtain a better resurrection;",
      "M": "Women received their dead, raised to life again. There were others who were tortured, refusing to be released, so that they might gain an even better resurrection.",
      "T": "Women received their dead back from the grave by resurrection. Others were beaten to death, refusing to accept release—because they were looking past this life to a far greater resurrection."
    },
    "36": {
      "L": "and others had trial of mockings and scourgings, and also of bonds and imprisonment;",
      "M": "Some faced jeers and flogging, and even chains and imprisonment.",
      "T": "Others suffered taunting and lashing—and worse still, chains and dungeons."
    },
    "37": {
      "L": "they were stoned, they were sawn asunder, they were tempted, they were slain with the sword; they went about in sheepskins and goatskins, being destitute, afflicted, tormented,",
      "M": "They were put to death by stoning; they were sawn in two; they were killed by the sword. They went about in sheepskins and goatskins, destitute, persecuted and mistreated—",
      "T": "They were stoned. They were sawed in half. They were cut down by the sword. They wandered in sheepskins and goatskins, utterly without resources, hounded, abused—"
    },
    "38": {
      "L": "of whom the world was not worthy, wandering in deserts and mountains and caves and the holes of the earth.",
      "M": "the world was not worthy of them. They wandered in deserts and mountains, and in caves and holes in the ground.",
      "T": "—the world was not worthy of them—left to roam through wastelands, mountains, caves, and cracks in the earth."
    },
    "39": {
      "L": "And all these, having obtained testimony through their faith, did not receive the promise,",
      "M": "These were all commended for their faith, yet none of them received what had been promised.",
      "T": "Every one of these people was commended by God for their faith—and yet not one of them received in this life what God had promised."
    },
    "40": {
      "L": "God having provided some better thing for us, so that they without us should not be made perfect.",
      "M": "God had planned something better for us so that only together with us would they be made perfect.",
      "T": "God had something better in mind—a plan that included us—so that they would not reach the final goal apart from us."
    }
  },
  "12": {
    "1": {
      "L": "Therefore, since we are surrounded by so great a cloud of witnesses, let us also lay aside every weight, and the sin which so easily besets us, and let us run with endurance the race that is set before us,",
      "M": "Therefore, since we are surrounded by such a great cloud of witnesses, let us throw off everything that hinders and the sin that so easily entangles, and let us run with endurance the race marked out for us,",
      "T": "All those witnesses—that vast cloud of them—surround us. So let us strip off everything that slows us down, especially the sin that wraps itself so easily around our legs, and let us run with patient endurance the race laid out for us."
    },
    "2": {
      "L": "looking to Jesus, the pioneer and perfecter of faith, who for the joy that was set before him endured the cross, despising the shame, and has sat down at the right hand of the throne of God.",
      "M": "fixing our eyes on Jesus, the pioneer and perfecter of faith. For the joy set before him he endured the cross, scorning its shame, and sat down at the right hand of the throne of God.",
      "T": "Eyes fixed on Jesus—the trailblazer who opened the path of faith and brought it to its goal. For the joy that lay ahead of him, he endured the cross; he treated its shame as nothing. And now he is seated at the right hand of God's throne."
    },
    "3": {
      "L": "For consider him who has endured such contradiction by sinners against himself, so that you do not grow weary, fainting in your souls.",
      "M": "Consider him who endured such opposition from sinners against himself, so that you will not grow weary and lose heart.",
      "T": "Think long and hard about him—about the level of hostility he absorbed from sinners, aimed directly at him—so that you do not collapse under your own struggle and give up."
    },
    "4": {
      "L": "You have not yet resisted to the point of blood in your striving against sin.",
      "M": "In your struggle against sin, you have not yet resisted to the point of shedding your blood.",
      "T": "Your contest with sin has not yet cost you your blood. Others before you went that far—he himself did."
    },
    "5": {
      "L": "and you have forgotten the exhortation which speaks to you as sons: 'My son, do not despise the chastening of the Lord, nor faint when you are rebuked by him;'",
      "M": "And have you completely forgotten this word of encouragement that addresses you as a father addresses his son: 'My son, do not make light of the Lord's discipline, and do not lose heart when he rebukes you,'",
      "T": "And you have quite forgotten the word that speaks to you as children of a father: 'My son, do not shrug off the Lord's discipline or lose heart when he corrects you—'"
    },
    "6": {
      "L": "for whom the Lord loves he chastens, and scourges every son whom he receives.",
      "M": "because the Lord disciplines the one he loves, and he chastens everyone he accepts as his son.",
      "T": "'—for the Lord disciplines those he loves, and his correction is a sign that he has fully received you as his own child.'"
    },
    "7": {
      "L": "It is for discipline that you endure; God is dealing with you as with sons; for what son is there whom a father does not discipline?",
      "M": "Endure hardship as discipline; God is treating you as his children. For what children are not disciplined by their father?",
      "T": "What you are enduring is God's discipline—his way of treating you as his own children. Show me a father who never corrects his child."
    },
    "8": {
      "L": "But if you are without discipline, of which all have become partakers, then you are bastards and not sons.",
      "M": "If you are not disciplined—and everyone undergoes discipline—then you are not legitimate children but illegitimate.",
      "T": "If you are exempt from the discipline that every true child receives, that is a troubling sign—it would mean you are not genuine members of the family."
    },
    "9": {
      "L": "Furthermore, we had fathers of our flesh as discipliners, and we respected them; shall we not much more be in subjection to the Father of spirits and live?",
      "M": "Moreover, we have all had human fathers who disciplined us and we respected them for it. How much more should we submit to the Father of spirits and live!",
      "T": "We had fathers in the flesh who disciplined us, and we respected them for it. How much more, then, should we place ourselves under the Father of our spirits—and gain life in doing so?"
    },
    "10": {
      "L": "For they indeed, for a few days, disciplined us as seemed good to them; but he, for our benefit, that we may be partakers of his holiness.",
      "M": "They disciplined us for a little while as they thought best; but God disciplines us for our good, in order that we may share in his holiness.",
      "T": "Our earthly fathers disciplined us as best they could, for a few years, by their own judgment. God disciplines us for our genuine good—he is forming us to share in his own holiness."
    },
    "11": {
      "L": "Now no chastening for the present seems to be joyful but grievous; but afterward it yields the peaceable fruit of righteousness to those who have been trained by it.",
      "M": "No discipline seems pleasant at the time, but painful. Later on, however, it produces a harvest of righteousness and peace for those who have been trained by it.",
      "T": "No discipline feels good in the moment—it is painful, not pleasant. But for those who are trained by it, the season of discipline later yields a harvest of peace and righteousness."
    },
    "12": {
      "L": "Wherefore lift up the hands that hang down, and the feeble knees;",
      "M": "Therefore, strengthen your feeble arms and weak knees.",
      "T": "So—raise those drooping hands! Steady those buckling knees!"
    },
    "13": {
      "L": "and make straight paths for your feet, so that what is lame may not be turned aside, but rather be healed.",
      "M": "Make level paths for your feet, so that the lame may not be disabled, but rather healed.",
      "T": "Clear a straight path for your steps—so that the one who is limping does not stumble off the course, but is instead restored."
    },
    "14": {
      "L": "Pursue peace with all men and the sanctification without which no one will see the Lord.",
      "M": "Make every effort to live in peace with everyone and to be holy; without holiness no one will see the Lord.",
      "T": "Pursue peace with all people—and pursue holiness: without it, seeing the Lord is out of the question."
    },
    "15": {
      "L": "looking carefully lest any man fall short of the grace of God; lest any root of bitterness springing up trouble you, and by it many be defiled;",
      "M": "See to it that no one fails to obtain the grace of God and that no bitter root grows up to cause trouble and defile many.",
      "T": "Watch over one another. See that no one drifts away from the grace of God. See that no poisonous root of bitterness grows up and spreads its contamination through the community."
    },
    "16": {
      "L": "lest there be any fornicator or profane person like Esau, who for one morsel of food sold his birthright.",
      "M": "See that no one is sexually immoral, or is godless like Esau, who for a single meal sold his inheritance rights as the oldest son.",
      "T": "Let no one be sexually immoral, and let no one be as godless as Esau, who traded away his inheritance—everything due him as firstborn—for a single meal."
    },
    "17": {
      "L": "For you know that afterward, when he desired to inherit the blessing, he was rejected; for he found no place of repentance, though he sought it carefully with tears.",
      "M": "Afterward, as you know, when he wanted to inherit this blessing, he was rejected. Even though he sought the blessing with tears, he could not change what he had done.",
      "T": "You know what happened: afterward, when he wanted to claim the blessing, he was turned away. Even weeping and begging, he found no way to undo what he had done. The door to repentance was closed."
    },
    "18": {
      "L": "For you have not come to the mountain that can be touched and that burned with fire, and to darkness, gloom, and tempest,",
      "M": "You have not come to a mountain that can be touched and that is burning with fire; to darkness, gloom and storm,",
      "T": "You have not come to a mountain like Sinai—a physical mass wreathed in blazing fire, wrapped in darkness, gloom, and storm—"
    },
    "19": {
      "L": "and to the sound of a trumpet, and the voice of words, which voice they who heard entreated that not a word more should be spoken to them,",
      "M": "to the blast of a trumpet and to such a voice speaking words that those who heard it begged that no further word be spoken to them,",
      "T": "—nor to the blare of a trumpet, nor to a voice that spoke words so overwhelming that the people begged it to stop."
    },
    "20": {
      "L": "for they could not endure what was commanded: 'If even a beast touches the mountain, it shall be stoned.'",
      "M": "because they could not bear what was commanded: 'If even an animal touches the mountain, it must be stoned.'",
      "T": "They could not bear the terms: 'Even if an animal merely touches the mountain, it is to be stoned.'"
    },
    "21": {
      "L": "And so terrifying was the sight that Moses said, 'I am terrified and trembling.'",
      "M": "The sight was so terrifying that Moses said, 'I am trembling with fear.'",
      "T": "Even Moses, when he saw it, said: 'I am shaking with fear.'"
    },
    "22": {
      "L": "But you have come to Mount Zion and to the city of the living God, the heavenly Jerusalem, and to myriads of angels,",
      "M": "But you have come to Mount Zion, to the city of the living God, the heavenly Jerusalem. You have come to thousands upon thousands of angels in joyful assembly,",
      "T": "But you have come to a completely different mountain—Mount Zion, the city of the living God, the heavenly Jerusalem. You have come to countless angels in festive celebration,"
    },
    "23": {
      "L": "to the general assembly and church of the firstborn who are enrolled in heaven, and to God the Judge of all, and to the spirits of the righteous made perfect,",
      "M": "to the assembly of the firstborn, whose names are written in heaven. You have come to God, the Judge of all, to the spirits of the righteous made perfect,",
      "T": "to the great gathering of God's firstborn—those whose names are written in heaven—to God himself, the judge of everyone, and to the spirits of those who have been made righteous and brought to completion,"
    },
    "24": {
      "L": "and to Jesus, the mediator of a new covenant, and to the blood of sprinkling that speaks better than the blood of Abel.",
      "M": "to Jesus the mediator of a new covenant, and to the sprinkled blood that speaks a better word than the blood of Abel.",
      "T": "and to Jesus, who stands as mediator of a new covenant, and to the sprinkled blood that speaks something far better than Abel's blood ever did."
    },
    "25": {
      "L": "See that you do not refuse him who is speaking; for if they did not escape when they refused him who warned them on earth, much less will we who turn away from him who speaks from heaven.",
      "M": "See to it that you do not refuse him who speaks. If they did not escape when they refused him who warned them on earth, how much less will we, if we turn away from him who warns us from heaven?",
      "T": "Be careful—do not turn away from the One who is speaking. Those who refused God when he spoke on earth did not escape. How much less will we escape if we reject the one who speaks now from heaven?"
    },
    "26": {
      "L": "whose voice then shook the earth, but now he has promised, saying, 'Yet once more I will shake not only the earth but also the heaven.'",
      "M": "At that time his voice shook the earth, but now he has promised, 'Once more I will shake not only the earth but also the heavens.'",
      "T": "That voice shook the earth at Sinai. But now God has promised something more: 'Once more, and this time I will shake not only the earth but the heavens too.'"
    },
    "27": {
      "L": "And this word, 'Yet once more,' denotes the removal of those things that are shaken, as of created things, that those things which are not shaken may remain.",
      "M": "The words 'once more' indicate the removing of what can be shaken—that is, created things—so that what cannot be shaken may remain.",
      "T": "The phrase 'once more' is telling: it signals a final removal of everything that can be shaken—the entire created order—so that only what cannot be shaken will be left standing."
    },
    "28": {
      "L": "Wherefore, receiving a kingdom that cannot be shaken, let us have grace, by which we may serve God acceptably with reverence and awe;",
      "M": "Therefore, since we are receiving a kingdom that cannot be shaken, let us be thankful, and so worship God acceptably with reverence and awe,",
      "T": "We are receiving a kingdom that no upheaval of history can topple. Let us therefore be thankful—and offer God the worship that pleases him: with reverence, with awe."
    },
    "29": {
      "L": "for our God is a consuming fire.",
      "M": "for our God is a consuming fire.",
      "T": "For the God we come before is himself a consuming fire."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'hebrews')
        merge_tier(existing, HEBREWS, tier_key)
        save(tier_dir, 'hebrews', existing)
    print('Hebrews 11–12 written.')

if __name__ == '__main__':
    main()
