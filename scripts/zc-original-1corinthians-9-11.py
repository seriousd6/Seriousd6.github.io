"""
mkt-original layer — 1 Corinthians chapters 9–11
Output: data/commentary/mkt-original/1corinthians.json
Run: python3 scripts/zc-original-1corinthians-9-11.py
"""
import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_comm(source, book):
    p = ROOT / 'data' / 'commentary' / source / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_comm(source, book, data):
    p = ROOT / 'data' / 'commentary' / source / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_comm(existing, new_data):
    # INTENT: Merge new verse entries without overwriting already-present keys — safe to re-run.
    # CHANGE? If commentary JSON structure changes from {ch:{v:html}}, update this traversal.
    # VERIFY: Re-running the script should produce identical output.
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

NEW = {
  "9": {
    "1": "Paul opens with four rapid rhetorical questions — am I not free? am I not an apostle? have I not seen Jesus our Lord? are you not my work in the Lord? — each expects a yes. The Greek eleutheros (free) and apostolos are his twin credentials: freedom from human authority and commission from Christ himself.",
    "2": "Even if others deny his apostleship, the Corinthians cannot — they are the seal (sphragis) of his apostolate in the Lord, a term from official documents that validated legal claims.",
    "3": "This is Paul's defense (apologia, the legal term for a formal reply to accusers) to those who examine (anakrinousi) him — judicial language signaling that a formal charge against his apostleship is in view.",
    "4": "Do we not have the right (exousia) to eat and drink? — exousia recurs seven times in this chapter; Paul's argument is precisely about legitimate authority and the choice to waive it.",
    "5": "Do we not have the right to take along a believing wife (adelphen gynaika, literally a sister-woman, i.e. a Christian wife)? — Paul mentions Cephas (Peter) and the brothers of the Lord as examples who exercised this right, grounding his argument in recognized apostolic practice.",
    "6": "Or is it only Barnabas and I who have no right to refrain from working for a living? — Paul and Barnabas are unique in funding their own ministry; the rhetorical force is that their self-support is the anomaly, not the norm.",
    "7": "Three analogies from common life: a soldier who serves at his own expense, a farmer who plants but never eats the fruit, a shepherd who keeps a flock but gets no milk — each is absurd, making the case that workers deserve their wages.",
    "8": "Paul is not relying on human reasoning alone — he asks whether the Law itself does not say the same thing, raising the argument to the level of scripture.",
    "9": "The Mosaic text cited: do not muzzle an ox while it treads out the grain (Deut 25:4) — Paul asks pointedly whether God's concern is really for oxen, signaling that the text carries a deeper human application.",
    "10": "Paul asserts the text was written for our sake — the plowman plows in hope, the thresher threshes in hope of sharing the crop. The agricultural imagery transfers directly to apostolic labor and its rightful reward.",
    "11": "If we sowed spiritual things among you, is it too much if we reap material things from you? — the rhetorical question makes the exchange look obviously proportionate: spiritual seed deserves material harvest.",
    "12": "Others share this right over you — other teachers at Corinth apparently did receive support. Paul and his companions did not exercise this right, but endure all things rather than put any obstacle in the way of the gospel. The word enkopē (obstacle) is a military term for cutting a road to impede an army.",
    "13": "Those who work in the temple share in what is offered; those who serve at the altar share in the altar's portions — the Jerusalem priestly system supports the analogy: those who minister in holy things receive their sustenance from holy things.",
    "14": "The Lord commanded that those who proclaim the gospel should get their living from the gospel — a reference to Jesus's instruction to his disciples (Matt 10:10; Luke 10:7: the laborer is worthy of his wages).",
    "15": "Paul has not used any of these rights and is not writing to claim them now — his boast (kauchema) would be emptied if he did. For him to preach free of charge is the essence of his particular calling.",
    "16": "Preaching the gospel carries no grounds for boasting — anankē (necessity, compulsion) is laid upon him; woe to him if he does not preach. The word anankē was used of divine compulsion, fate, and moral obligation — Paul places his commission in this category of inescapable necessity.",
    "17": "If Paul preaches willingly he has a reward (misthos); if unwillingly he is still entrusted with a stewardship (oikonomia) — the oikonomos (steward) manages the master's household goods, not his own; Paul's calling is a trust, not a choice.",
    "18": "His wage is precisely this: to offer the gospel free of charge, not making full use of his right in the gospel — the paradox is complete. His pay is the act of working for free.",
    "19": "Free from all (eleutheros ek pantōn), Paul made himself a slave to all so that he might win the more — the same root word (eleutheros/slave) that opened chapter 9 now drives the conclusion: freedom is exercised through voluntary servitude.",
    "20": "To Jews he became as a Jew — not abandoning his own Jewishness (he was already Jewish), but entering the Jewish cultural world fully in order to win those under the Law.",
    "21": "To those outside the Law (Gentiles) he became as one outside the Law — though he is not outside God's law but within Christ's law (ennomos Christou); the Greek carefully distinguishes being outside Torah from being lawless before God.",
    "22": "To the weak he became weak — the language of weakness (astheneia) anticipates the strong/weak discussion of chapter 8-10 about idol food; Paul became whatever his hearers needed so that by all means he might save some.",
    "23": "He does everything for the sake of the gospel so that he might share in its blessings — he is not merely an instrument of the gospel but a fellow-partaker (synkoinonos) in its benefits.",
    "24": "Do you not know that those who run in a stadium all run but only one receives the prize? — the Greek games (pan-Hellenic athletics) were familiar to Corinthians; Paul shifts to athletic metaphor to press the urgency of self-discipline.",
    "25": "Everyone who competes (agōnizomenos, from the agōn, the contest) exercises self-control (enkrateuetai) in all things — the agōn word-group carries connotations of life-and-death struggle; enkrateia (self-control) was a key Greek virtue. The athlete does it for a perishable crown (the pine or laurel wreath); Paul runs for an imperishable one.",
    "26": "Paul does not run aimlessly or box like one beating the air — his ministry is purposeful and aimed; the contrast implies that the Corinthians who think freedom means indulgence are shadow-boxing.",
    "27": "Paul disciplines his body (hypōpiazō, literally strike under the eye, beat black and blue) and keeps it under control (doulagōgeō, enslave it) lest after preaching to others he himself should be disqualified (adokimos) — the word adokimos (failing the test) is the opposite of dokimos (approved); even an apostle can fail the test of endurance.",
  },
  "10": {
    "1": "Paul calls the Corinthians brothers — a term of solidarity — and says he does not want them to be ignorant about their fathers, all of whom were under the cloud and passed through the sea. The Exodus generation is Israel's founding narrative, and Paul is about to treat it as a warning for the church.",
    "2": "All were baptized into Moses in the cloud and in the sea — a striking use of the baptism language the Corinthians knew; the cloud and sea become the waters of their initiation into the Mosaic covenant, as water baptism initiates into Christ.",
    "3": "All ate the same spiritual food (broma pneumatikon) — the manna of the wilderness, reread as pneumatic, Spirit-bearing food that prefigured the Eucharist.",
    "4": "All drank the same spiritual drink — the water from the rock, which Paul identifies as Christ who accompanied them. The rock that followed was a midrashic tradition; Paul reads it as a christological presence throughout the wilderness journey.",
    "5": "Yet with most of them God was not pleased — the Greek uses the word katestrofēsan (they were scattered, overthrown): the same generation that received spiritual gifts perished in the wilderness. Blessing does not guarantee ultimate approval.",
    "6": "These events became examples (typoi) for us — typos (pattern, type, mold) is the key hermeneutical word; the wilderness events are not mere history but a divinely designed pattern warning against desire for evil things.",
    "7": "Do not be idolaters as some of them were — citing Exodus 32:6 (the golden calf episode: the people sat down to eat and drink and rose up to play). The link to idol-feast meat in Corinth is direct: eating at idol temples is the church's golden calf moment.",
    "8": "Do not engage in sexual immorality as some of them did and twenty-three thousand fell in a single day — the reference is to Numbers 25:9 (which says twenty-four thousand; Paul may cite a variant tradition or count differently). Sexual immorality and idolatry were inseparably linked at Corinthian temple festivals.",
    "9": "Do not put Christ to the test as some of them did and were destroyed by serpents — the serpent episode of Numbers 21:5-6; Paul reads it as testing Christ, affirming Christ's presence in the wilderness (v.4) and applying the warning to the Corinthians' behavior.",
    "10": "Do not grumble as some of them grumbled and were destroyed by the destroyer — the murmuring narratives of Numbers 11:1 and 14:2; the destroyer (olothreutēs) likely refers to the destroying angel. Grumbling against God's appointed leaders is spiritually lethal.",
    "11": "These things happened to them as a type (typikōs) and were written for our instruction, upon whom the ends of the ages have come — the church stands at the convergence of the ages; the OT was written with the church in view, serving as Scripture's eschatological function.",
    "12": "Therefore let anyone who thinks he stands take heed lest he fall — the Corinthians who pride themselves on their gnōsis (knowledge) and freedom are precisely those at greatest risk; spiritual self-confidence is the precondition of the fall.",
    "13": "No temptation has seized you except what is common to humanity — Paul offers assurance: the Corinthians are not facing superhuman trial. And God is faithful (pistos ho theos) — the same faithfulness that sustained Israel through the wilderness will not allow testing beyond endurance, but will also provide the way of escape (ekbasis).",
    "14": "Therefore, flee from idolatry (eidōlolatria) — the imperative is strong: pheugete, run away. Not negotiate, not discern case by case, but flee. This is the summary response to the whole argument from Israel's wilderness failures.",
    "15": "Paul addresses them as sensible (phronimoi) people and invites them to judge what he says — the irony is sharp given their self-flattery about wisdom; now he asks them to exercise real judgment about the Supper.",
    "16": "The cup of blessing (potērion tēs eulogias) which we bless — the technical language of the Passover fourth cup (the cup of blessing), now used for the Lord's Supper cup. Communion/fellowship (koinōnia) in the blood of Christ — koinōnia means participation, sharing, solidarity. The cup creates real fellowship with Christ.",
    "17": "Because there is one bread, we who are many are one body, since we all partake of the one bread — the Eucharist does not merely symbolize unity; sharing the one loaf constitutes the one body. The logic is participatory.",
    "18": "Consider Israel according to the flesh — those who eat the sacrifices are partners (koinōnoi) with the altar; participation in the temple cult creates real solidarity with what is being worshiped.",
    "19": "What then am I saying — that an idol is something? or that food sacrificed to idols is something? — Paul is not reversing his position from chapter 8 that idols are nothing; he is shifting the question from ontology to participation.",
    "20": "What pagans sacrifice they offer to demons, not to God — citing Deuteronomy 32:17 (LXX). The idol is nothing, but behind the idol-cult stands demonic reality; participation in idol feasts creates solidarity with those demonic powers.",
    "21": "You cannot drink the cup of the Lord and the cup of demons — the two tables are mutually exclusive; koinōnia with Christ and koinōnia with demons are incompatible loyalties. To sit at both is to provoke the Lord.",
    "22": "Are we provoking the Lord to jealousy (parazēloumen)? — citing Deuteronomy 32:21 from the Song of Moses; the jealousy of God is the response to Israel's idolatry. Are we stronger than he? — the rhetorical question presupposes the answer no.",
    "23": "All things are permissible — Paul quotes the Corinthian slogan again (as in 6:12), but not all things are beneficial (sympherei) or build up (oikodomei). The criterion shifts from personal rights to communal edification.",
    "24": "Let no one seek his own good but the good of his neighbor — the ethical principle that governs all the preceding discussion about idol food; the question is never only about what I am permitted but what serves the other.",
    "25": "Eat whatever is sold in the meat market without raising questions of conscience — practical guidance for the agora; meat of unknown cultic origin does not require investigation. The earth is the Lord's and everything in it (Psalm 24:1).",
    "26": "Psalm 24:1 citation: the earth is the Lord's and the fullness thereof — all creation belongs to God; food purchased in the market is God's provision regardless of its prior use.",
    "27": "If an unbeliever invites you to dinner and you wish to go, eat whatever is set before you without asking questions of conscience — the same freedom applies at private dinners; don't interrogate the host about the food's provenance.",
    "28": "But if someone says this was offered in sacrifice (hierothyton is the pagan term; Paul used eidōlothyton, idol-meat, in chapter 8, using the insider critical term), do not eat it for the sake of the one who informed you and for the sake of conscience.",
    "29": "Paul means not your own conscience but the other's — the conscience at stake is not the knowledgeable believer's but the weaker person's or the unbeliever who raised the issue. Why should my freedom be judged by another's conscience?",
    "30": "If I partake with thankfulness, why am I slandered over that for which I give thanks? — another rhetorical question: if Paul eats with gratitude, the food is sanctified by prayer; but the point is that neighbor-conscience overrides personal thanksgiving-freedom in borderline cases.",
    "31": "So whether you eat or drink or whatever you do, do all to the glory of God — the summary principle; every act is subsumed under the telos of divine glory.",
    "32": "Give no offense to Jews or to Greeks or to the church of God — three communities whose stumbling must be avoided; the church is distinguished from both ethnic groups as a third category.",
    "33": "Paul himself tries to please all people in all things, not seeking his own advantage but that of the many, so that they may be saved — the apostle's own practice of self-limitation is the model that summarizes chapters 8-10 as a whole.",
  },
  "11": {
    "1": "Be imitators of me as I am of Christ — the imitation chain: Corinthians imitate Paul who imitates Christ. This closing verse of chapter 10 (some manuscripts begin chapter 11 here) anchors the entire self-limitation argument in the pattern of Christ's own self-giving.",
    "2": "Paul praises them for remembering him in everything and holding to the traditions (paradoseis) as he delivered them — paradosis is the technical term for the handing-on of authoritative teaching; the same word used in 11:23 for the Supper institution.",
    "3": "The head (kephalē) of every man is Christ, the head of a woman is man, and the head of Christ is God — a relational hierarchy of headship. The meaning of kephalē (source? authority?) is debated; in context it frames the discussion of honorable and dishonorable head-covering practice.",
    "4": "Every man who prays or prophesies with his head covered dishonors his head — in Roman honor culture, men of social standing wore the toga capite velato (head veiled) at religious ceremonies; Paul appears to be countering a practice that confused Roman civic-religious customs with Christian worship.",
    "5": "Every woman who prays or prophesies with her head uncovered dishonors her head — women pray and prophesy publicly in the assembly; that is assumed, not questioned. The issue is the head-covering that signals sexual honor in the Mediterranean world.",
    "6": "If a woman does not cover her head let her also cut off her hair — a reductio ad absurdum; a woman with a shaved head in the ancient Mediterranean signaled shame or mourning; since that is unthinkable, so is going uncovered.",
    "7": "A man should not cover his head since he is the image and glory of God; but woman is the glory of man — Genesis 1:26-27 is the ground; both image God (Paul does not deny this of women), but the glory-relation Paul describes maps the creation order onto the covering practice.",
    "8": "Man was not made from woman but woman from man — the creation sequence of Genesis 2 is invoked; woman was taken from man's side (ek tou andros), establishing a derivative relation.",
    "9": "Man was not created for woman but woman for man — the purpose stated in Genesis 2:18-20: it is not good for man to be alone, so a helper was made for him. Paul reads this as indicating the directional orientation of the original creation.",
    "10": "A woman ought to have authority (exousia) on her head because of the angels — the exousia is on the woman herself, not over her; most scholars read this as her authority to pray and prophesy, signaled by the covering. The angel reference may allude to Genesis 6 traditions or angelic observers of worship.",
    "11": "Nevertheless, in the Lord woman is not independent of man nor man of woman — Paul immediately qualifies the asymmetry with mutuality: in the Lord (en kyriō), the relational hierarchy does not mean subordination of worth.",
    "12": "For as woman came from man, so man is now born through woman, and all things are from God — the interdependence is complete; creation began with woman from man, but every subsequent human comes through woman, and both originate from God.",
    "13": "Judge for yourselves — is it proper for a woman to pray to God with her head uncovered? — Paul appeals to the Corinthians' own judgment, a rhetorical move that assumes they will agree with him when they think it through.",
    "14": "Does not nature itself teach you that if a man wears long hair it is a disgrace to him — Paul appeals to physis (nature) meaning conventional expectation; the culturally natural signal of male dignity in the Greek world involved shorter hair.",
    "15": "But if a woman wears long hair it is her glory (doxa), because her hair was given to her as a covering (peribolaiou) — the long hair itself functions as a natural head-covering, suggesting that the artificial covering mirrors what nature already provides.",
    "16": "If anyone is inclined to be contentious about this, we have no such practice, nor do the churches of God — Paul closes not with a theological argument but an appeal to universal church practice; the Corinthians are out of step with every other assembly.",
    "17": "Paul issues a sharper rebuke: in giving these instructions he does not praise them, for they come together not for the better but for the worse — the word is kreisson/hēsson (better/worse); the assembly is actively harmful, not merely neutral.",
    "18": "He hears there are divisions (schismata) among them when they meet — the schismata of 1:10-12 (party factions) have now infected the eucharistic assembly itself, the one place that should most express unity.",
    "19": "There must also be factions (haireseis) among you so that those who are genuine (dokimoi) may be recognized among you — a grim concession: divisions reveal who truly belongs. The word hairesis (faction, later heresy) will carry heavy freight in church history.",
    "20": "When you come together it is not the Lord's Supper that you eat (kyriakon deipnon) — the word kyriakon (belonging to the Lord) is used only here and in Revelation 1:10 (the Lord's Day) in the NT; a technical early designation for the community meal.",
    "21": "Each one goes ahead with his own meal — they are not sharing but eating their own provisions; the wealthy eat and drink well while the poor go hungry. The economic inequality of Corinthian society has invaded the sacred meal.",
    "22": "Do you not have houses to eat and drink in? Or do you despise the church of God and humiliate those who have nothing? — the question is devastating: if you want to eat your own food, do it at home; the assembly is not a private dinner party.",
    "23": "Paul received from the Lord what he also delivered to you — the language of tradition: paralambanō (receive) and paradidōmi (deliver/hand on) are the technical rabbinic terms for transmitting authoritative teaching. Paul received this from the Lord, not from a human chain.",
    "25": "The new covenant in my blood — hē kainē diathēkē en tō emō haimati; kainē diathēkē echoes Jeremiah 31:31-34, the new covenant. The Lord's Supper is the enacted ratification of the covenant Jeremiah announced.",
    "26": "For as often as you eat this bread and drink the cup, you proclaim the Lord's death until he comes — katangellete (proclaim); the Supper is itself a proclamation, an acted-out word. Until he comes (achri hou elthē) gives the practice an eschatological horizon: the meal announces a present absence and a coming presence.",
    "27": "Whoever eats the bread or drinks the cup of the Lord in an unworthy manner (anaxiōs) will be guilty (enochos) of the body and blood of the Lord — anaxiōs is an adverb of manner, not a statement of personal worthiness; the unworthiness refers to the manner of eating (the divisions and humiliations of vv.18-22).",
    "28": "Let a person examine himself (dokimazō) and so eat of the bread and drink of the cup — the self-examination (dokimazō, to test for authenticity, the same root as dokimos in v.19) is not about personal sinfulness in general but about discerning the body properly.",
    "29": "Anyone who eats and drinks without discerning the body (mē diakrinōn to sōma) eats and drinks judgment (krima) on himself — the body to be discerned is probably the community as body of Christ (the social reading) as much as the eucharistic elements; failure to see the poor as members of Christ's body is the precise sin Paul has been addressing.",
    "30": "That is why many among you are weak and ill and a number have died (koimōntai, fallen asleep) — Paul sees the physical ailments in the Corinthian community as divine discipline connected to the eucharistic abuse. He is not explaining all illness but a specific pattern of judgment.",
    "31": "But if we judged ourselves truly (diekrinomen), we would not be judged — the verb diakrinō (discern, judge) links back to v.29; proper self-examination anticipates and forestalls divine judgment.",
    "32": "When we are judged by the Lord we are being disciplined (paideuometha) so that we may not be condemned along with the world — the illness and death Paul mentioned are corrective discipline (paideia), not final condemnation; God chastens believers rather than condemning them.",
    "33": "So then, brothers, when you come together to eat, wait for one another (ekdechesthe) — the practical resolution: the failure was not waiting for the poor who arrived later; communal waiting repairs the rupture.",
    "34": "If anyone is hungry let him eat at home so that when you come together it will not be for judgment — the solution is simple: eat your private meals privately; the assembly is for the shared sacred meal, not private consumption. The rest Paul will arrange when he comes.",
  }
}

if __name__ == '__main__':
    existing = load_comm('mkt-original', '1corinthians')
    merge_comm(existing, NEW)
    save_comm('mkt-original', '1corinthians', existing)
    for ch in ['9', '10', '11']:
        print(f'  ch {ch}: {len(existing.get(ch, {}))} verses')
