"""
MKT 1 Corinthians chapters 7–9 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-1corinthians-7-9.py

This is the first completed script for 1 Corinthians; it establishes the book's term conventions.
Chapters 1–6 are covered by mkt-1corinthians-1-3.py and mkt-1corinthians-4-6.py (in-progress).

Translation decisions:
- G1849 (ἐξουσία): "right/authority" (L: "authority", M/T: "right") — in ch. 8–9, Paul argues
  for his apostolic entitlement and then waives it; "right" carries the legal-entitlement sense
  better than "power" in these contexts.
- G4561 (σάρξ): context-determined — "flesh" in L throughout; M/T distinguish:
  7:28 "trouble in the flesh" = hardships/pressures of married life (not sinful nature);
  8:13 "flesh" = literal meat (σάρξ as physical substance);
  context never implies Pauline "sinful nature" in these three chapters.
- G4151 (πνεῦμα): 7:34 "holy in spirit and body" — lowercase "spirit" throughout these
  chapters; Paul refers to the human person's spiritual dimension, not the Holy Spirit directly.
- G26 (ἀγάπη): "love" in all three tiers (8:1); the covenantal, outward-oriented sense is
  rendered explicitly in T ("love that builds").
- G1658 (ἐλεύθερος): "free/freedom" throughout; 9:1 Paul's claim to personal freedom as an
  apostle; 9:19 the voluntary self-enslavement paradox preserved in all three tiers.
- G96 (ἀδόκιμος): 9:27 "disqualified" (L "castaway" retained as archaic; M/T "disqualified")
  — athletic metaphor, not eternal damnation; the word means "failing the test/unfit."
- G2745/G2744 (καύχημα/καυχάομαι): 9:15–16 "boasting/glory" — Paul's boast is the free
  offer of the gospel; rendered "boast" in L/M, "glory in" or "ground for boasting" in T.
- G5486 (χάρισμα): 7:7 "gift" — the charism of celibacy or marriage; context rules out
  charismatic-gifts sense here; rendered "gift" in all tiers.
- G2962 (κύριος): "Lord" throughout; Paul's "word from the Lord" (7:10, 7:12) distinguished
  from his own apostolic judgment; T makes this distinction explicit in the narrative.
- G7:1 quotation: "it is good for a man not to touch a woman" is almost certainly a Corinthian
  slogan Paul is quoting before qualifying it; T flags this rhetorical move.
- Aspect notes: Present imperatives in ch. 7 (μενέτω etc.) = ongoing command, "let him
  continue to remain"; aorist in 7:28 (ἔγημεν) = completed single act of marrying.
- OT echo: 9:9 quotes Deut 25:4 (muzzled ox); Paul's argument that Torah speaks typologically
  of Christian workers is an example of his midrashic method — noted in T.
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


CORINTHIANS1 = {
  "7": {
    "1": {
      "L": "Now concerning the things whereof you wrote to me: it is good for a man not to touch a woman.",
      "M": "Now about the matters you wrote about: it is good for a man not to have sexual relations with a woman.",
      "T": "On the questions you raised in your letter — yes, you quoted back to me the principle that it is good for a man to abstain from marriage. I want to address that carefully."
    },
    "2": {
      "L": "But because of fornications, let each man have his own wife, and each woman have her own husband.",
      "M": "But to avoid sexual immorality, let each man have his own wife and each woman her own husband.",
      "T": "But given the reality of sexual temptation in Corinth, the right path for most people is marriage: one man, one woman, each belonging fully to the other."
    },
    "3": {
      "L": "Let the husband render to the wife her due benevolence, and likewise also the wife to the husband.",
      "M": "Let the husband fulfill his conjugal duty to his wife, and likewise the wife to her husband.",
      "T": "A husband owes his wife the intimacy of marriage — it is a debt, not a favor. And a wife owes the same to her husband."
    },
    "4": {
      "L": "The wife does not have authority over her own body, but the husband; and likewise also the husband does not have authority over his own body, but the wife.",
      "M": "A wife's body does not belong to her alone but also to her husband; likewise, a husband's body does not belong to him alone but also to his wife.",
      "T": "In marriage the body becomes shared: neither spouse can treat their own body as private property to withhold at will. This cuts both ways — he has authority over her body, and she has authority over his."
    },
    "5": {
      "L": "Do not defraud one another, except by mutual consent for a time, that you may give yourselves to fasting and prayer; and come together again, lest Satan tempt you because of your lack of self-control.",
      "M": "Do not deprive each other except by mutual agreement for a limited time, so you can devote yourselves to prayer. Then come together again, or Satan may tempt you through your lack of self-control.",
      "T": "Do not withhold from each other — except by joint, time-limited decision for a season of focused prayer. Then reunite. Otherwise you hand Satan an opening through your own vulnerability."
    },
    "6": {
      "L": "But I say this as a concession, not as a commandment.",
      "M": "I say this as a concession, not as a command.",
      "T": "What I just said is pastoral accommodation to reality, not apostolic law. I am not commanding sexual abstinence in marriage; I am permitting temporary, mutual, purposeful restraint."
    },
    "7": {
      "L": "For I would that all men were even as I myself am. But each man has his own gift from God, one after this manner, and another after that.",
      "M": "I wish that all people were like me — but each has their own gift from God, one of one kind and another of another.",
      "T": "Personally I would prefer everyone to live as I do — but that wish collides with reality. God gives different gifts: what I have is one kind of grace-endowment; what a married person has is another. Neither is inferior."
    },
    "8": {
      "L": "But I say to the unmarried and to the widows: it is good for them if they remain even as I.",
      "M": "To the unmarried and to widows I say: it is good for them to remain as I am.",
      "T": "My word to the single and the widowed: staying as you are, as I am, is a genuine good — not a lesser path, not a consolation prize."
    },
    "9": {
      "L": "But if they do not contain themselves, let them marry; for it is better to marry than to burn.",
      "M": "But if they do not have self-control, let them marry, for it is better to marry than to burn with passion.",
      "T": "But if remaining single proves to be a smoldering struggle rather than a peaceful gift, marry. Marriage is not defeat; it is wisdom. Burning unmet desire is the real danger."
    },
    "10": {
      "L": "And to the married I give charge, not I but the Lord: that the wife should not depart from her husband.",
      "M": "To the married I give this instruction — not from me but from the Lord — the wife must not separate from her husband.",
      "T": "For those already married, I relay a direct word from the Lord himself, not my own apostolic judgment: a wife must not leave her husband."
    },
    "11": {
      "L": "But if indeed she does depart, let her remain unmarried or be reconciled to her husband; and a husband must not put away his wife.",
      "M": "But if she does separate, she must remain unmarried or be reconciled to her husband. And a husband must not divorce his wife.",
      "T": "If she does leave, her only options are to remain single or to return to him — that door stays open, always. And equally, a husband must not initiate divorce against his wife."
    },
    "12": {
      "L": "But to the rest say I, not the Lord: if any brother has a wife that is an unbeliever, and she consents to dwell with him, let him not put her away.",
      "M": "To the others I say — I, not the Lord — if a believer has an unbelieving wife who is willing to live with him, he should not divorce her.",
      "T": "On the following question, I give my own apostolic judgment — I have no direct word of Jesus to relay here. If a Christian man has an unbelieving wife who is content to stay in the marriage, he must not end it."
    },
    "13": {
      "L": "And the woman who has an unbelieving husband, and he consents to dwell with her, let her not put him away.",
      "M": "And if a woman has an unbelieving husband who is willing to live with her, she should not divorce him.",
      "T": "The same principle holds for a Christian woman with an unbelieving husband who is content to remain — let the marriage stand."
    },
    "14": {
      "L": "For the unbelieving husband is sanctified by the believing wife, and the unbelieving wife is sanctified by the believing husband; else were your children unclean, but now they are holy.",
      "M": "For the unbelieving husband is made holy through his believing wife, and the unbelieving wife is made holy through her believing husband; otherwise your children would be unclean, but as it is, they are holy.",
      "T": "Here is the reason: the believer draws the whole household into the sphere of God's covenant. The unbelieving spouse inhabits sacred space. Your children prove this — you already treat them as belonging to God, not as outsiders to his reach."
    },
    "15": {
      "L": "But if the unbelieving depart, let him depart. A brother or a sister is not under bondage in such cases; but God has called us to peace.",
      "M": "But if the unbelieving partner leaves, let them go. A brother or sister is not enslaved in such cases; God has called us to peace.",
      "T": "But if the unbeliever walks out, release them — you are not bound by a marriage the other party has already abandoned. God's calling for your life is peace, not perpetual servitude to a broken bond."
    },
    "16": {
      "L": "For how do you know, O wife, whether you shall save your husband? Or how do you know, O husband, whether you shall save your wife?",
      "M": "For how do you know, wife, whether you will save your husband? Or how do you know, husband, whether you will save your wife?",
      "T": "And in any case, the future belongs to God, not you: you cannot know whether staying will win your spouse to faith — that uncertainty is precisely why peace, not burden, is the right frame for this whole question."
    },
    "17": {
      "L": "But as God has distributed to each, as the Lord has called each, so let him walk. And so ordain I in all the churches.",
      "M": "Only, let each person live the life the Lord has assigned them, as God has called them. This is my rule in all the churches.",
      "T": "The governing principle, which I teach in every church I serve: live faithfully in the situation where God placed you when he called you. Your circumstances at conversion are your starting point, not your ceiling."
    },
    "18": {
      "L": "Was any man called being circumcised? Let him not become uncircumcised. Was any man called in uncircumcision? Let him not be circumcised.",
      "M": "Was anyone already circumcised when called? He should not try to remove the marks of circumcision. Was anyone uncircumcised when called? He should not seek circumcision.",
      "T": "Were you Jewish when God called you? Don't try to erase that heritage. Were you Gentile? Don't submit to circumcision as though it changes your standing. The real issues lie elsewhere."
    },
    "19": {
      "L": "Circumcision is nothing, and uncircumcision is nothing, but the keeping of the commandments of God.",
      "M": "Circumcision counts for nothing and uncircumcision counts for nothing; what matters is obeying God's commands.",
      "T": "In the new order, circumcision is a non-issue and its absence is equally a non-issue. What defines faithfulness now is keeping God's commandments — the moral substance of the law, fulfilled in Christ."
    },
    "20": {
      "L": "Let every man abide in the same calling wherein he was called.",
      "M": "Each person should remain in the situation they were in when God called them.",
      "T": "Stay where God found you. The place and condition of your conversion is the ground from which your whole life with God grows."
    },
    "21": {
      "L": "Were you called as a slave? Do not be concerned about it. But if you are able to become free, use the opportunity rather.",
      "M": "Were you a slave when called? Do not let it trouble you. But if you are able to gain your freedom, take the opportunity.",
      "T": "Were you a slave when God called you? Don't let that define your horizon — you serve Christ now, and that transforms everything. But if freedom becomes possible, take it without hesitation."
    },
    "22": {
      "L": "For he that was called in the Lord being a slave is the Lord's freedman; likewise he that was called being free is Christ's slave.",
      "M": "For the one who was a slave when called in the Lord is the Lord's freed person; similarly, the one who was free when called is Christ's slave.",
      "T": "Here is the great reversal: a slave who belongs to Christ is the Lord's own freed man — Christ has already liberated what no human owner can touch. And a free person who belongs to Christ is Christ's own servant — the most meaningful slavery imaginable."
    },
    "23": {
      "L": "You were bought with a price; be not the servants of men.",
      "M": "You were bought at a price; do not become slaves to people.",
      "T": "The purchase price of your freedom was Christ's own blood. Do not sell that freedom back to human masters — to human approval, to social pressure, to the opinion of those who would define your worth."
    },
    "24": {
      "L": "Brethren, let every man wherein he was called therein abide with God.",
      "M": "Brothers and sisters, each of you should remain before God in the situation you were in when called.",
      "T": "Brothers, the place where God found you is the place where you can walk with him — stay there, in his presence, and let that transform the circumstances from within."
    },
    "25": {
      "L": "Now concerning virgins: I have no commandment of the Lord, but I give my judgment as one who has obtained mercy from the Lord to be faithful.",
      "M": "Now about those who have never been married: I have no command from the Lord, but I give my judgment as one who, by the Lord's mercy, is trustworthy.",
      "T": "On the question of those who have never married — I have no direct word of Jesus to pass on here, only my own apostolic judgment. I offer it as someone who has received God's mercy and aims to be reliable."
    },
    "26": {
      "L": "I think therefore that this is good, by reason of the present distress, that it is good for a man to remain as he is.",
      "M": "In view of the present crisis, I think it is good for a person to remain as they are.",
      "T": "Given the pressure of this present moment in history — we live at the hinge of the ages — staying as you are is the strategically wise course."
    },
    "27": {
      "L": "Are you bound to a wife? Do not seek to be loosed. Are you free from a wife? Do not seek a wife.",
      "M": "Are you committed to a wife? Do not seek release. Are you free from such a commitment? Do not seek a wife.",
      "T": "If you are married, don't engineer an exit. If you are single, don't let finding a spouse become your consuming preoccupation."
    },
    "28": {
      "L": "But even if you do marry, you have not sinned; and if a virgin marries, she has not sinned. But such shall have tribulation in the flesh; and I would spare you.",
      "M": "But if you do marry, you have not sinned, and if a virgin marries, she has not sinned. Yet those who marry will face practical hardships, and I am trying to spare you from those.",
      "T": "Marriage is no sin — if you marry, you are not disobeying God; the same for a woman who chooses to marry. But I want to be honest with you: married life brings its own pressures and burdens. It is those pressures I am trying to spare you, not the marriage itself."
    },
    "29": {
      "L": "But this I say, brethren: the time is shortened; that henceforth even they that have wives should be as though they had none;",
      "M": "What I mean is this, brothers and sisters: the time is short. From now on, let those who have wives live as though they had none,",
      "T": "Here is the urgent point, brothers: the clock is running down — the age is reaching its end. So live with your eyes on eternity, not absorbed in your circumstances. Married people should not be consumed by marriage —"
    },
    "30": {
      "L": "and those that weep as though they wept not; and those that rejoice as though they rejoiced not; and those that buy as though they possessed not;",
      "M": "and those who mourn as though not mourning, and those who rejoice as though not rejoicing, and those who buy as though having nothing of their own,",
      "T": "grief should not be the last word on your life; joy should not be your ultimate foundation; possessions should sit loosely in your hands —"
    },
    "31": {
      "L": "and those that use this world as not abusing it; for the fashion of this world passes away.",
      "M": "and those who use the world as though not absorbed in it. For the present form of this world is passing away.",
      "T": "engage the world without being mastered by it. The whole present structure of things is dissolving; the age that replaces it is your real home."
    },
    "32": {
      "L": "But I would have you without anxiety. He that is unmarried cares for the things of the Lord, how he may please the Lord;",
      "M": "I want you to be free from anxiety. The unmarried man is concerned about the things of the Lord — how to please the Lord.",
      "T": "What I desire for you is an undivided heart. The single man can give his whole attention to God's affairs — his one governing question is how to live for the Lord."
    },
    "33": {
      "L": "but he that is married cares for the things of the world, how he may please his wife;",
      "M": "But the married man is concerned about worldly affairs — how to please his wife.",
      "T": "The married man's attention is necessarily split: he must think about his household, his finances, how to honor his wife —"
    },
    "34": {
      "L": "and he is divided. The unmarried woman and the virgin cares for the things of the Lord, that she may be holy both in body and in spirit; but she that is married cares for the things of the world, how she may please her husband.",
      "M": "and he is pulled in different directions. The unmarried woman or virgin is concerned about the Lord's things, so that she may be holy in body and spirit. But the married woman is concerned about worldly things — how to please her husband.",
      "T": "— and that divided loyalty is the simple nature of married life, not a fault but a fact. The unmarried woman has the freedom to offer her whole self — body and spirit — to God's purposes without competing claims. The married woman must weave her devotion through the fabric of a shared life."
    },
    "35": {
      "L": "And this I say for your own benefit; not that I may cast a snare upon you, but for that which is seemly, and that you may attend upon the Lord without distraction.",
      "M": "I say this for your own benefit, not to restrict you, but to promote what is fitting and to enable undivided devotion to the Lord.",
      "T": "I am not laying down a law or trying to trap you in guilt. My one aim is to point you toward what is truly noble: an undistracted, undivided attentiveness to the Lord."
    },
    "36": {
      "L": "But if any man think that he behaves uncomely toward his virgin, if she passes the flower of her age and it must be so, let him do what he will, he sins not; let them marry.",
      "M": "But if anyone thinks he is acting dishonorably toward the woman betrothed to him — if she is past her prime and he feels the obligation — let him do what he wishes; he does not sin; let them marry.",
      "T": "But if a man finds that his restraint is beginning to dishonor the woman he is pledged to — if time is passing and the tension is real and marriage is what must happen — let him act. That is not weakness; it is not sin; it is the right and honorable thing to do."
    },
    "37": {
      "L": "But he that stands stedfast in his heart, having no necessity, but having power over his own will, and has so decreed in his heart to keep his own virgin, does well.",
      "M": "But the man who stands firm in his commitment, who is under no compulsion, has his desire under control, and has resolved in his heart to keep the woman as his betrothed — he does well.",
      "T": "But if a man has made a settled, free decision — no external pressure, desire genuinely mastered, chosen from the heart — to maintain a celibate commitment with the woman he is pledged to, he does something genuinely good."
    },
    "38": {
      "L": "So then both he that gives her in marriage does well, and he that gives her not in marriage does better.",
      "M": "So the one who marries his betrothed does well, and the one who refrains from marrying does even better.",
      "T": "Marriage is good. Celibacy chosen freely, for the kingdom's sake, is better still. Both are genuine goods; neither is a mistake or a spiritual shortcut."
    },
    "39": {
      "L": "A wife is bound by law as long as her husband lives; but if her husband be dead, she is free to be married to whom she will; only in the Lord.",
      "M": "A wife is bound to her husband as long as he lives. If her husband dies, she is free to marry anyone she wishes — only in the Lord.",
      "T": "Marriage is a bond that holds for life — that is its very nature. Death releases the bond, and the widow is genuinely free to remarry — anyone she chooses. One qualification only: he must belong to the Lord."
    },
    "40": {
      "L": "But she is happier if she abide so, after my judgment; and I think also that I have the Spirit of God.",
      "M": "But in my judgment she will be happier if she remains as she is. And I think I also have the Spirit of God.",
      "T": "But from where I stand — and I believe I am reading this by the Spirit of God — a widow who stays single chooses the better joy. That is my considered, Spirit-guided judgment."
    }
  },
  "8": {
    "1": {
      "L": "Now as touching things offered unto idols, we know that we all have knowledge. Knowledge puffs up, but love edifies.",
      "M": "Now about food offered to idols: we know that we all possess knowledge. Knowledge puffs up, but love builds up.",
      "T": "On the matter of food sacrificed to idols — yes, we all have the relevant theological knowledge. But knowledge on its own inflates the knower; it is love that actually builds people up and strengthens the community."
    },
    "2": {
      "L": "And if any man thinks that he knows any thing, he knows nothing yet as he ought to know.",
      "M": "Anyone who thinks they know something does not yet know as they ought to know.",
      "T": "The very confidence of 'I have this figured out' is a warning sign — whoever is certain they have grasped something has not yet understood how little they actually know."
    },
    "3": {
      "L": "But if any man loves God, the same is known of him.",
      "M": "But if anyone loves God, this person is known by God.",
      "T": "What matters is not that you know but that you are known — and to love God and be loved by him is the only knowledge that ultimately secures you."
    },
    "4": {
      "L": "As concerning therefore the eating of those things that are offered in sacrifice unto idols, we know that an idol is nothing in the world, and that there is none other God but one.",
      "M": "About eating food offered to idols: we know that an idol has no real existence in the world, and that there is no God but one.",
      "T": "So when it comes to the practical question — can we eat what passed through a pagan temple? — the theology is correct: an idol is a fiction, a nothing dressed in stone and gold. There is only one God."
    },
    "5": {
      "L": "For though there be that are called gods, whether in heaven or in earth, (as there be gods many, and lords many,)",
      "M": "For even if there are so-called gods — whether in heaven or on earth — as indeed there are many so-called gods and many lords —",
      "T": "The world is thick with so-called gods and lords — the temples are real, the cult is real, the social pressure to participate is real —"
    },
    "6": {
      "L": "yet to us there is but one God, the Father, of whom are all things, and we in him; and one Lord Jesus Christ, by whom are all things, and we by him.",
      "M": "yet for us there is one God, the Father, from whom all things come and for whom we exist; and one Lord, Jesus Christ, through whom all things were made and through whom we exist.",
      "T": "— but we confess a different reality entirely. One God: the Father, source of everything that exists, the goal toward whom everything moves and into whom we are gathered. One Lord: Jesus the Messiah, through whom the whole creation came to be and through whom we ourselves have been remade. That is our creed, our identity, our world."
    },
    "7": {
      "L": "Howbeit there is not in every man that knowledge; for some with conscience of the idol eat it as a thing offered unto an idol unto this hour; and their conscience being weak is defiled.",
      "M": "But not everyone has this knowledge. Some people, through their long association with idols, still eat such food as something genuinely offered to an idol; and because their conscience is weak, it is defiled.",
      "T": "But this knowledge is not evenly distributed — and here is where everything changes. Some believers were deep in idol worship before they came to faith. When they eat food that passed through a pagan shrine, they cannot shake the feeling that they are participating in something spiritually real. Their conscience is still tender at that point, and eating violates something in them."
    },
    "8": {
      "L": "But meat commends us not to God; for neither if we eat are we the better, nor if we eat not are we the worse.",
      "M": "But food does not bring us closer to God: we are no better if we eat, and no worse if we do not eat.",
      "T": "Let's be clear about what is not at stake here: food has zero power to alter your standing before God. Eating or abstaining changes nothing in your relationship with him."
    },
    "9": {
      "L": "But take heed lest by any means this liberty of yours becomes a stumblingblock to them that are weak.",
      "M": "But be careful that this right of yours does not become a stumbling block to the weak.",
      "T": "The danger, though, is this: your theological freedom, exercised without thought for others, can become the very obstacle over which a fragile believer falls."
    },
    "10": {
      "L": "For if any man see you who have knowledge sitting at meat in the idol's temple, shall not the conscience of him who is weak be emboldened to eat those things which are offered to idols?",
      "M": "For if someone with a weak conscience sees you who have this knowledge eating in an idol's temple, won't they be encouraged to eat food offered to idols?",
      "T": "Picture it: you, the theologically confident one, reclining at a meal in an idol's precinct. A believer with a tender conscience sees you. Your example doesn't liberate them — it gives them permission to do something they still believe is wrong. You have weaponized your freedom against a weaker brother."
    },
    "11": {
      "L": "And through your knowledge shall the weak brother perish, for whom Christ died?",
      "M": "So this weak brother, for whom Christ died, is destroyed by your knowledge.",
      "T": "And so this person — the one whose faith is fragile, the one Jesus bled and died to save — is being destroyed by your sophisticated theology. Sit with that."
    },
    "12": {
      "L": "But when ye sin so against the brethren, and wound their weak conscience, ye sin against Christ.",
      "M": "When you sin against the brothers and sisters in this way, and wound their weak conscience, you are sinning against Christ.",
      "T": "When you wound a fellow believer's conscience this carelessly, you are not simply being thoughtless. You are sinning against Christ himself, who is present and at stake in every one of his people."
    },
    "13": {
      "L": "Wherefore, if meat cause my brother to stumble, I will eat no flesh while the world stands, lest I make my brother to offend.",
      "M": "Therefore, if what I eat causes my brother to stumble, I will never eat meat again, so as not to cause my brother to sin.",
      "T": "My conclusion is non-negotiable: if a simple meal has the power to trip up someone for whom Christ died, then I will give up meat entirely — permanently, for life — rather than use my freedom as a weapon against a vulnerable fellow believer."
    }
  },
  "9": {
    "1": {
      "L": "Am I not free? Am I not an apostle? Have I not seen Jesus Christ our Lord? Are not ye my work in the Lord?",
      "M": "Am I not free? Am I not an apostle? Have I not seen Jesus our Lord? Are you not my work in the Lord?",
      "T": "Four questions before I go further: Am I not a free man? Am I not a genuine apostle? Did I not see the risen Lord Jesus with my own eyes? And are you Corinthians not yourselves the living proof of my apostolic labor?"
    },
    "2": {
      "L": "If I am not an apostle unto others, yet doubtless I am to you; for the seal of my apostleship are ye in the Lord.",
      "M": "Even if I am not an apostle to others, I certainly am to you; for you are the seal of my apostleship in the Lord.",
      "T": "Others may dispute my apostleship — that argument belongs to them. But you, the Corinthian church, cannot dispute it: your own existence is the certificate stamped by God himself on my calling."
    },
    "3": {
      "L": "My answer to them that do examine me is this.",
      "M": "This is my defense to those who sit in judgment on me.",
      "T": "When critics put me on trial, this is what I put on the witness stand."
    },
    "4": {
      "L": "Have we not authority to eat and to drink?",
      "M": "Do we not have the right to eat and drink?",
      "T": "As an apostle, do I not have the basic right to be fed and sustained by the communities I serve?"
    },
    "5": {
      "L": "Have we not authority to lead about a wife who is a sister, as well as other apostles, and as the brothers of the Lord, and Cephas?",
      "M": "Do we not have the right to take along a believing wife, as do the other apostles and the Lord's brothers and Cephas?",
      "T": "Do I not have the right — as every other apostle does, as the Lord's own brothers do, as Peter does — to travel with a believing wife who shares in the work?"
    },
    "6": {
      "L": "Or have only Barnabas and I no authority to forbear working?",
      "M": "Or are only Barnabas and I obligated to work to support ourselves?",
      "T": "Are Barnabas and I alone in the apostolic circle expected to hold down secular employment to survive while we serve you?"
    },
    "7": {
      "L": "Who ever goes to war at his own charges? Who plants a vineyard and does not eat of its fruit? Or who feeds a flock and does not eat of the milk of the flock?",
      "M": "Who serves as a soldier at his own expense? Who plants a vineyard and does not eat of its fruit? Who tends a flock and does not share in the milk?",
      "T": "Three illustrations from ordinary working life: no soldier pays for his own gear and rations — the army feeds its soldiers. No vine-grower forfeits the harvest of what they planted. No shepherd is denied milk from the flock they tend. Work earns its keep. That is simply how things work."
    },
    "8": {
      "L": "Say I these things as a man? or says not the law the same also?",
      "M": "Do I say this only on human grounds? Does not the law say the same thing?",
      "T": "Am I reasoning from mere human common sense? The Torah itself says as much — this is not my invention."
    },
    "9": {
      "L": "For it is written in the law of Moses: Thou shalt not muzzle the ox that treads out the corn. Doth God take care for oxen?",
      "M": "For it is written in the law of Moses: 'Do not muzzle an ox while it is treading out grain.' Is God concerned about oxen?",
      "T": "Moses wrote: Do not muzzle the ox while it works the threshing floor. Do you think that regulation was God's primary concern — the welfare of livestock?"
    },
    "10": {
      "L": "Or does he say it altogether for our sakes? For our sakes, no doubt, this is written, that he that plows should plow in hope, and that he that threshes in hope should be partaker of his hope.",
      "M": "Is he not certainly speaking for our sake? Yes, this was written for our sake, because the one who plows should plow in hope, and the one who threshes should do so expecting a share in the harvest.",
      "T": "Of course not — this text was written for the sake of workers like us. The underlying principle is this: anyone who labors — the plowman breaking ground in autumn, the thresher processing grain in summer — works with the legitimate expectation of sharing in the results. The ox is an illustration; we are the application."
    },
    "11": {
      "L": "If we have sown unto you spiritual things, is it a great thing if we shall reap your carnal things?",
      "M": "If we have sown spiritual seed among you, is it too much to expect a material harvest from you?",
      "T": "We have invested something immeasurable in you — the gospel, the Spirit's presence, eternal life itself. Is it so great a burden to ask that you meet our physical needs in return?"
    },
    "12": {
      "L": "If others are partakers of this authority over you, are not we rather? Nevertheless we have not used this authority; but suffer all things, lest we should hinder the gospel of Christ.",
      "M": "If others have this right over you, should we not have it even more? Yet we have not used this right; instead we endure everything rather than place any obstacle in the way of the gospel of Christ.",
      "T": "Other workers in Corinth exercise this very right over you — and we have a stronger claim than any of them. Yet we have never claimed it. We absorb every hardship, bear every deprivation, rather than let any legitimate right of ours become an obstacle to the gospel's free advance."
    },
    "13": {
      "L": "Do you not know that they who minister about holy things eat of the things of the temple, and they who wait at the altar are partakers with the altar?",
      "M": "Don't you know that those who serve in the temple eat what is offered there, and those who minister at the altar share in what is sacrificed?",
      "T": "Consider how the temple system has always been structured: priests live from what is consecrated to the sanctuary; altar servants have an appointed share in the altar's portions. That provision is built into the very architecture of sacred service."
    },
    "14": {
      "L": "Even so has the Lord ordained that they which preach the gospel should live of the gospel.",
      "M": "In the same way, the Lord has ordained that those who preach the gospel should receive their living from the gospel.",
      "T": "And the Lord Jesus himself established this same principle for gospel heralds: those who announce the good news are to be materially sustained by those who receive it. It is his command, not my preference."
    },
    "15": {
      "L": "But I have used none of these things; neither have I written these things that it should be so done unto me; for it were better for me to die than that any man should make my glorying void.",
      "M": "But I have not used any of these rights. And I am not writing this to start claiming them now, because I would rather die than have anyone take away what I can boast about.",
      "T": "Yet I have used none of these rights — deliberately, consistently, from the beginning. And I am not writing this argument in order to start claiming them now. I would sooner die penniless than let anyone strip away the one thing I have to glory in before God: that I offered the gospel free of charge."
    },
    "16": {
      "L": "For though I preach the gospel, I have nothing to glory of; for necessity is laid upon me; yea, woe is unto me, if I preach not the gospel!",
      "M": "For when I preach the gospel, I have no grounds for boasting in that, since I am compelled to preach. Woe to me if I do not preach the gospel!",
      "T": "The preaching itself is not my boast — I had no choice in the matter. A compulsion from above was laid upon me. If I refuse to preach, I fall under divine judgment. There is no glory in doing what you cannot escape doing."
    },
    "17": {
      "L": "For if I do this thing willingly, I have a reward; but if against my will, a dispensation of the gospel is committed unto me.",
      "M": "If I do this willingly, I have a reward; but if unwillingly, I am simply entrusted with a commission.",
      "T": "If I preached purely by free personal choice, there would be wages due. But I preach under orders — and a steward who simply does what the master requires is fulfilling a duty, not earning a bonus."
    },
    "18": {
      "L": "What is my reward then? Verily that when I preach the gospel, I may make the gospel of Christ without charge, that I abuse not my power in the gospel.",
      "M": "What then is my reward? That in preaching the gospel I may offer it free of charge, and so not make full use of my rights in the gospel.",
      "T": "So what is my boast, my genuine wage? This: to preach the gospel without ever charging for it. That voluntary renunciation of rights — that free, deliberate gift — is the one thing I do out of pure choice, and therefore the one thing I can call my own glory."
    },
    "19": {
      "L": "For though I am free from all men, I have made myself servant unto all, that I might gain the more.",
      "M": "For though I am free from all people, I have made myself a slave to all, so that I might win as many as possible.",
      "T": "Here is the paradox I live inside: I am beholden to no one — free as a person can be — yet I have voluntarily enslaved myself to every person I encounter, because winning them for Christ matters more than preserving my freedom."
    },
    "20": {
      "L": "And unto the Jews I became as a Jew, that I might gain the Jews; to them that are under the law, as under the law, that I might gain them that are under the law;",
      "M": "To the Jews I became like a Jew, to win Jews. To those under the law I became like one under the law — though I myself am not under the law — to win those under the law.",
      "T": "Among Jews I live as a Jew — not as performance but as genuine solidarity with their world — in order to bring them to the Messiah. Among Torah-observant believers I live within the Torah framework — though I am no longer bound by it as a covenant requirement — to reach those who are."
    },
    "21": {
      "L": "To them that are without law, as without law, (being not without law to God, but under the law to Christ,) that I might gain them that are without law.",
      "M": "To those without the law I became like one without the law — though I am not free from God's law but under Christ's law — to win those outside the law.",
      "T": "Among Gentiles I adopt Gentile ways — their food, their customs, their social world — but let no one misread that as lawlessness toward God. I am under the law of the Messiah, which fulfills and transcends the Torah. This is service, not license."
    },
    "22": {
      "L": "To the weak became I as weak, that I might gain the weak: I am made all things to all men, that I might by all means save some.",
      "M": "To the weak I became weak, to win the weak. I have become all things to all people, so that by all means I might save some.",
      "T": "To those whose faith is fragile, I identify with their fragility rather than brandishing my theological freedom at them. I make myself adaptable to everyone I meet — not out of people-pleasing, but because every soul I can reach through Christ is worth the sacrifice of my personal preferences."
    },
    "23": {
      "L": "And this I do for the gospel's sake, that I might be partaker thereof with you.",
      "M": "I do all this for the sake of the gospel, so that I may share in its blessings.",
      "T": "Everything I do — the flexibility, the self-denial, the voluntary weakness — is for the gospel. I want to be a full participant in what it promises, not merely a delivery agent who hands good news to others and never enters it himself."
    },
    "24": {
      "L": "Know ye not that they which run in a race run all, but one receives the prize? So run, that ye may obtain.",
      "M": "Don't you know that in a race all the runners run, but only one receives the prize? Run in such a way as to win.",
      "T": "You know how a race works: every runner takes the field, but only one crosses the finish first and takes the wreath. Let that be the image for your whole life in Christ — run as though winning actually matters, because it does."
    },
    "25": {
      "L": "And every man that strives for the mastery is temperate in all things. Now they do it to obtain a corruptible crown; but we an incorruptible.",
      "M": "Everyone who competes exercises self-control in all things. They do it to receive a crown that will not last; but we do it for one that will last forever.",
      "T": "Every serious athlete disciplines every appetite — diet, sleep, training schedules — for the sake of a laurel wreath that wilts within the week. We are in training for something that will never decay, never fade, never be taken away."
    },
    "26": {
      "L": "I therefore so run, not as uncertainly; so fight I, not as one that beats the air;",
      "M": "Therefore I do not run aimlessly; I do not fight like someone boxing the air.",
      "T": "My life is not an aimless sprint — I know exactly where the finish line is. And I am not shadowboxing — I land actual blows on an actual opponent, my own flesh."
    },
    "27": {
      "L": "but I buffet my body and bring it into subjection, lest that by any means, after that I have preached to others, I myself should be castaway.",
      "M": "But I discipline my body hard and make it my slave, so that after I have preached to others, I myself will not be disqualified.",
      "T": "I batter my own body into submission — the appetites, the comforts, the instinct for self-preservation — because the race demands it. My greatest fear is not criticism from others. It is this: that I would spend my whole life calling others to the finish line and be disqualified from crossing it myself."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '1corinthians')
        merge_tier(existing, CORINTHIANS1, tier_key)
        save(tier_dir, '1corinthians', existing)
    print('1 Corinthians 7–9 written.')

if __name__ == '__main__':
    main()
