"""
MKT 1 Corinthians chapters 10–12 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-1corinthians-10-12.py

Translation decisions:
- G4151 πνεῦμα: "Spirit" (L/M/T) — capitalized throughout chs 10–12; divine referent is unambiguous
- G5486 χάρισμα: "gift" (L/M); "gift of grace" (T first occurrence in ch 12) — emphasizes charis root
- G4152 πνευματικός: "spiritual" (L/M); varies in T (e.g. "Spirit-given" for gifts, "things of the Spirit")
- G1577 ἐκκλησία: "assembly" (L); "church" (M/T) — Pauline ekklesia carries civic-assembly resonance
- G2962 κύριος: "Lord" (L/M/T) throughout
- G4983 σῶμα: "body" (L/M/T) — both eucharistic and ecclesiological senses; context distinguishes
- G2842 κοινωνία (10:16): "participation" (L); "communion" (M); "sharing in" (T) — avoids collapsing the
  word into a ritual label; the point is organic participation, not just ceremony
- G1849 ἐξουσία (11:10): rendered "authority" (L); "symbol of authority" (M); "her own authority" (T) —
  the phrase ἐξουσίαν ἔχειν ἐπὶ τῆς κεφαλῆς means the woman herself "has authority over her head";
  T surfaces this reading rather than flattening it to mere submission
- G2776 κεφαλή (11:3): "head" (L/M/T) — metaphorical; T note on relational ordering, not ontological
  subordination (the Father–Christ axis proves this: Christ is not ontologically inferior to the Father)
- G4160 ποιεῖτε (11:24,25): "do" (L); "do this" (M/T) — present imperative, ongoing practice
- G1242 διαθήκη (11:25): "covenant" (L/M/T) — not "testament"; the Sinai echo is intentional
- G26 ἀγάπη: does not appear in chs 10–12; reserved for ch 13 (next unit)
- G166 αἰώνιος: does not appear in chs 10–12
- G4102 πίστις (12:9): "faith" (L/M); "Spirit-given trust" (T) — contextually a charismatic endowment,
  distinct from saving faith, though the boundary is permeable
- 10:4 "Rock was Christ" — typological identification maintained in all three tiers; no softening
- 10:9 textual note: some MSS read "Lord" rather than "Christ"; following NA28/SBLGNT which have Χριστόν
- 11:2 "traditions" / παραδόσεις — "traditions" (L/M); "the teaching I passed on" (T) — avoids
  ecclesiastical loading of "tradition" in T
- 11:10 "because of the angels" — retained literally in L/M; T offers "in the presence of the watching
  angels" — the most common interpretation is angelic witness to proper worship order
- 11:29 "discerning the body" — "body" left unglossed in L/M; T adds "the Lord's body" to clarify the
  eucharistic sense that the Greek context requires
- 12:2 "led astray to mute idols" — L preserves the passive/inarticulate quality; T: "swept along toward
  speechless idols" — the contrast with Spirit-speech (v3) is deliberate
- 12:13 "made to drink of one Spirit" — aorist passive; T renders as completed initiatory act
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

CORINTHIANS = {
  "10": {
    "1": {
      "L": "For I do not want you to be ignorant, brothers, that our fathers were all under the cloud and all passed through the sea,",
      "M": "I do not want you to be unaware, brothers, that our ancestors were all under the cloud and all passed through the sea,",
      "T": "Brothers, I want you to take this to heart: our ancestors all marched under the cloud and all walked through the sea,"
    },
    "2": {
      "L": "and all were baptized into Moses in the cloud and in the sea,",
      "M": "and all were baptized into Moses in the cloud and in the sea,",
      "T": "and in the cloud and in the sea they were all, in effect, baptized into Moses—united to him as their deliverer."
    },
    "3": {
      "L": "and all ate the same spiritual food,",
      "M": "and all ate the same spiritual food,",
      "T": "They all ate the same Spirit-given food"
    },
    "4": {
      "L": "and all drank the same spiritual drink. For they drank from the spiritual Rock that followed them, and the Rock was Christ.",
      "M": "and all drank the same spiritual drink. For they drank from the spiritual Rock that accompanied them, and that Rock was Christ.",
      "T": "and drank the same Spirit-given drink—for they were drinking from a spiritual Rock that traveled with them, and that Rock was Christ himself."
    },
    "5": {
      "L": "But with most of them God was not pleased, for they were struck down in the wilderness.",
      "M": "Nevertheless, God was not pleased with most of them, and they were laid low in the wilderness.",
      "T": "Yet God was not pleased with most of them—their bodies were strewn across the wilderness."
    },
    "6": {
      "L": "Now these things happened as examples for us, so that we should not desire evil things as they also desired.",
      "M": "Now these things happened as examples for us, so that we would not crave evil things as they did.",
      "T": "These events stand as warnings for us, so we won't fall into the same craving for evil that destroyed them."
    },
    "7": {
      "L": "And do not become idolaters as some of them were; as it is written, 'The people sat down to eat and drink and rose up to play.'",
      "M": "Do not be idolaters, as some of them were. As it is written: 'The people sat down to eat and drink and rose up to play.'",
      "T": "Don't become idolaters as some of them did. The scripture says: 'The people sat down to eat and drink, then got up to revel.'"
    },
    "8": {
      "L": "Neither let us commit sexual immorality, as some of them committed sexual immorality, and fell in a single day twenty-three thousand.",
      "M": "We must not commit sexual immorality, as some of them did—and in a single day twenty-three thousand of them fell dead.",
      "T": "Don't commit sexual immorality the way some of them did—twenty-three thousand died in a single day."
    },
    "9": {
      "L": "Neither let us put Christ to the test, as some of them tested him and were destroyed by serpents.",
      "M": "We must not put Christ to the test, as some of them did and were destroyed by snakes.",
      "T": "Don't put Christ to the test as some of them did—and were killed by serpents."
    },
    "10": {
      "L": "And do not grumble, as some of them grumbled, and were destroyed by the Destroyer.",
      "M": "And do not grumble, as some of them did—and were destroyed by the destroying angel.",
      "T": "Don't grumble, as some of them grumbled—they were cut down by the destroying angel."
    },
    "11": {
      "L": "Now these things happened to them as examples, and were written for our instruction, upon whom the ends of the ages have come.",
      "M": "These things happened to them as examples and were written down for our instruction—we who live at the culmination of the ages.",
      "T": "All of this befell them as a warning, and it was recorded for our sake—we who stand at the very end of the age."
    },
    "12": {
      "L": "Therefore let the one who thinks he stands take heed lest he fall.",
      "M": "So if you think you are standing firm, be careful that you do not fall.",
      "T": "So if you think you're standing secure, watch out—the fall can come quickly."
    },
    "13": {
      "L": "No temptation has overtaken you except what is common to humanity. But God is faithful, who will not allow you to be tempted beyond what you are able, but with the temptation will also make the way of escape, that you may be able to endure it.",
      "M": "No temptation has seized you except what is common to all people. God is faithful; he will not let you be tempted beyond what you can bear. But when you are tempted, he will also provide a way out so that you can endure it.",
      "T": "Every temptation you face is the ordinary kind that all human beings face. God is faithful—he will not allow you to be tested beyond your strength, and when the test comes, he will open a way through so that you can hold on."
    },
    "14": {
      "L": "Therefore, my beloved ones, flee from idolatry.",
      "M": "Therefore, my dear friends, flee from idolatry.",
      "T": "This is why, dear friends, you must run from idol worship."
    },
    "15": {
      "L": "I speak as to sensible people; judge what I say for yourselves.",
      "M": "I speak to you as to wise people; judge for yourselves what I say.",
      "T": "I'm addressing you as thinking people—weigh what I say."
    },
    "16": {
      "L": "The cup of blessing which we bless, is it not the participation in the blood of Christ? The bread which we break, is it not the participation in the body of Christ?",
      "M": "Is not the cup of thanksgiving for which we give thanks a communion in the blood of Christ? And is not the bread that we break a communion in the body of Christ?",
      "T": "When we take the cup of blessing and give thanks over it, are we not sharing in the blood of Christ? When we break the bread, are we not sharing in the body of Christ?"
    },
    "17": {
      "L": "Because there is one bread, we who are many are one body; for we all partake of the one bread.",
      "M": "Because there is one loaf, we who are many are one body, for we all share in that one loaf.",
      "T": "There is one loaf, and because we all share it, we who are many form one body."
    },
    "18": {
      "L": "Consider Israel according to the flesh: are not those who eat the sacrifices participants in the altar?",
      "M": "Consider the people of Israel: do not those who eat the sacrifices share in the altar?",
      "T": "Think about Israel as they offered sacrifices—those who ate from the offering became participants at the altar itself."
    },
    "19": {
      "L": "What therefore am I saying? That what is sacrificed to an idol is anything? Or that an idol is anything?",
      "M": "What am I saying then? That food sacrificed to an idol is anything real? Or that an idol is anything real?",
      "T": "What am I getting at? That meat offered to an idol has any real significance? Or that an idol itself amounts to anything?"
    },
    "20": {
      "L": "No, but that what they sacrifice, they sacrifice to demons and not to God. And I do not want you to become participants with demons.",
      "M": "No, but I am saying that what pagans sacrifice they offer to demons, not to God, and I do not want you to be participants with demons.",
      "T": "No—what I mean is this: the sacrifices that pagans make are offered to demons, not to God. And I refuse to see you become partners with demons."
    },
    "21": {
      "L": "You cannot drink the cup of the Lord and the cup of demons. You cannot partake of the table of the Lord and the table of demons.",
      "M": "You cannot drink the cup of the Lord and the cup of demons too; you cannot partake of the Lord's table and the table of demons.",
      "T": "You cannot drink from the Lord's cup and from the cup of demons at the same time. You cannot sit at the Lord's table and at the table of demons."
    },
    "22": {
      "L": "Or are we provoking the Lord to jealousy? Are we stronger than he?",
      "M": "Are we trying to arouse the Lord's jealousy? Are we stronger than he is?",
      "T": "Are we really trying to make the Lord jealous? Do we imagine we're stronger than he is?"
    },
    "23": {
      "L": "'All things are permitted,' but not all things are profitable. 'All things are permitted,' but not all things build up.",
      "M": "'Everything is permissible'—but not everything is beneficial. 'Everything is permissible'—but not everything builds others up.",
      "T": "'Everything is allowed'—but not everything is good. 'Everything is allowed'—but not everything strengthens others."
    },
    "24": {
      "L": "Let no one seek his own good, but the good of the other.",
      "M": "No one should seek his own good, but the good of others.",
      "T": "Stop pursuing your own advantage—pursue the advantage of the person next to you."
    },
    "25": {
      "L": "Whatever is sold in the meat market, eat without raising any question on account of conscience,",
      "M": "Eat whatever is sold in the meat market without raising questions of conscience,",
      "T": "Buy and eat whatever is in the market without making it a matter of conscience—"
    },
    "26": {
      "L": "for 'the earth is the Lord's and everything in it.'",
      "M": "for 'the earth is the Lord's, and everything in it.'",
      "T": "since 'the earth belongs to the Lord, and everything it contains.'"
    },
    "27": {
      "L": "If one of the unbelievers invites you and you wish to go, eat whatever is set before you without raising any question on account of conscience.",
      "M": "If an unbeliever invites you to a meal and you want to go, eat whatever is put in front of you without raising questions of conscience.",
      "T": "If a pagan invites you to dinner and you choose to accept, eat whatever they serve without making an issue of conscience."
    },
    "28": {
      "L": "But if anyone says to you, 'This was offered in sacrifice,' do not eat it, for the sake of the one who told you and for the sake of conscience—",
      "M": "But if someone says to you, 'This has been offered in sacrifice,' then do not eat it, both for the sake of the one who told you and for the sake of conscience.",
      "T": "But if someone tells you, 'This meat was offered to an idol,' don't eat it—both to protect the conscience of the person who said it and to honor what conscience requires."
    },
    "29": {
      "L": "conscience, I say, not your own, but the other's. For why is my freedom judged by another's conscience?",
      "M": "I mean the other person's conscience, not yours. For why should my freedom be judged by someone else's conscience?",
      "T": "I mean his conscience, not yours. But you might ask: why should my freedom be limited by another person's scruples?"
    },
    "30": {
      "L": "If I partake with thankfulness, why am I spoken against over that for which I give thanks?",
      "M": "If I take part in the meal with thankfulness, why am I condemned for something I eat with gratitude?",
      "T": "If I eat with genuine thanksgiving, why should I be condemned for food I received with gratitude?"
    },
    "31": {
      "L": "So whether you eat or drink, or whatever you do, do all to the glory of God.",
      "M": "So whether you eat or drink or whatever you do, do it all for the glory of God.",
      "T": "The answer is this: whether you're eating, drinking, or doing anything else—make it all about the glory of God."
    },
    "32": {
      "L": "Give no offense to Jews or to Greeks or to the assembly of God,",
      "M": "Do not cause anyone to stumble, whether Jews, Greeks or the church of God—",
      "T": "Don't become a stumbling block to anyone—not to Jewish people, not to Gentiles, not to the church of God."
    },
    "33": {
      "L": "just as I also please everyone in all things, not seeking my own advantage, but the advantage of the many, in order that they may be saved.",
      "M": "even as I try to please everyone in every way. For I am not seeking my own good but the good of many, so that they may be saved.",
      "T": "Take my lead: I try to accommodate everyone in every situation—not for my own benefit, but for the benefit of as many people as possible, so that they might be saved."
    }
  },
  "11": {
    "1": {
      "L": "Be imitators of me, as I also am of Christ.",
      "M": "Follow my example, as I follow the example of Christ.",
      "T": "Imitate me—the way I imitate Christ."
    },
    "2": {
      "L": "Now I commend you because you remember me in all things and hold fast to the traditions just as I delivered them to you.",
      "M": "I commend you because you remember me in everything and hold to the traditions just as I passed them on to you.",
      "T": "I'm glad to commend you for remembering me in all this and for holding to the teaching I passed on to you."
    },
    "3": {
      "L": "But I want you to know that the head of every man is Christ, and the head of a woman is the man, and the head of Christ is God.",
      "M": "But I want you to realize that the head of every man is Christ, the head of the woman is the man, and the head of Christ is God.",
      "T": "Here is something I want you to understand: the relational head of every man is Christ, the relational head of a wife is her husband, and the relational head of Christ is God—a pattern of ordered love from the Trinity downward."
    },
    "4": {
      "L": "Every man praying or prophesying with something on his head dishonors his head.",
      "M": "Every man who prays or prophesies with his head covered dishonors his head.",
      "T": "Any man who prays or prophesies with his head covered shames his head—Christ."
    },
    "5": {
      "L": "But every woman praying or prophesying with her head uncovered dishonors her head, for it is one and the same as if she were shaved.",
      "M": "But every woman who prays or prophesies with her head uncovered dishonors her head—it is just as though her head were shaved.",
      "T": "But any woman who prays or prophesies with her head uncovered shames her head—her husband. It's equivalent to having her head shaved."
    },
    "6": {
      "L": "For if a woman does not cover herself, let her also be shorn. But if it is shameful for a woman to be shorn or shaved, let her cover herself.",
      "M": "For if a woman does not cover her head, she might as well have her hair cut off; but if it is a disgrace for a woman to have her hair cut off or her head shaved, then she should cover her head.",
      "T": "If a woman won't cover her head, she may as well cut her hair off—but since cropping or shaving a woman's hair is disgraceful, she should keep her head covered."
    },
    "7": {
      "L": "For a man indeed ought not to cover his head, being the image and glory of God; but the woman is the glory of the man.",
      "M": "A man ought not to cover his head, since he is the image and glory of God; but woman is the glory of man.",
      "T": "A man should not cover his head, because he is the image and reflected glory of God; but woman is the reflected glory of man."
    },
    "8": {
      "L": "For man is not from woman, but woman from man.",
      "M": "For man did not come from woman, but woman from man;",
      "T": "Man did not originate from woman, but woman from man—"
    },
    "9": {
      "L": "For man was not created for the sake of the woman, but woman for the sake of the man.",
      "M": "and man was not created for the sake of woman, but woman for the sake of man.",
      "T": "and man was not made for woman's sake, but woman for the sake of man."
    },
    "10": {
      "L": "For this reason the woman ought to have authority on her head, on account of the angels.",
      "M": "For this reason, and because of the angels, the woman ought to have a sign of authority on her head.",
      "T": "For this reason—and because of the watching angels—a woman should have authority over her own head."
    },
    "11": {
      "L": "Nevertheless, in the Lord, woman is not without man, nor man without woman.",
      "M": "Nevertheless, in the Lord woman is not independent of man, nor is man independent of woman.",
      "T": "But in the Lord, woman and man are not independent of each other—"
    },
    "12": {
      "L": "For just as the woman is from the man, so also the man is through the woman; and all things are from God.",
      "M": "For as woman came from man, so also man is born of woman. And all things come from God.",
      "T": "for as woman came from man, so now every man enters the world through woman—and all of it comes from God."
    },
    "13": {
      "L": "Judge among yourselves: is it proper for a woman to pray to God with her head uncovered?",
      "M": "Judge for yourselves: is it proper for a woman to pray to God with her head uncovered?",
      "T": "Use your own judgment: is it right for a woman to pray to God with her head uncovered?"
    },
    "14": {
      "L": "Does not nature itself teach you that if a man has long hair it is a dishonor to him?",
      "M": "Does not the very nature of things teach you that if a man has long hair, it is a disgrace to him,",
      "T": "Doesn't the natural order itself instruct you? Long hair on a man is a mark of dishonor—"
    },
    "15": {
      "L": "But if a woman has long hair it is a glory to her? For her hair is given to her as a covering.",
      "M": "but that if a woman has long hair, it is her glory? For long hair is given to her as a covering.",
      "T": "but for a woman, her long hair is her glory. Her hair has been given to her as a natural covering."
    },
    "16": {
      "L": "But if anyone is inclined to be contentious, we have no such practice, nor do the assemblies of God.",
      "M": "If anyone wants to be contentious about this, we have no other practice—nor do the churches of God.",
      "T": "If anyone wants to argue the point—we have no other custom, and neither do the churches of God."
    },
    "17": {
      "L": "But in giving this instruction, I do not commend you, because you come together not for the better but for the worse.",
      "M": "In the following instructions, however, I must say that your meetings do more harm than good.",
      "T": "But what I'm about to address next I cannot commend: your gatherings are doing you more harm than good."
    },
    "18": {
      "L": "For first, when you come together in assembly, I hear that divisions exist among you, and in part I believe it.",
      "M": "First of all, I hear that when you come together as a church there are divisions among you, and to some extent I believe it.",
      "T": "To begin with, I'm told that when you assemble as a congregation there are factions forming—and I'm inclined to believe it."
    },
    "19": {
      "L": "For it is necessary for there to be factions among you, so that those who are approved may be made evident among you.",
      "M": "No doubt there have to be differences among you to show which of you have God's approval.",
      "T": "Such divisions may be inevitable—they expose who among you is genuinely tested and approved."
    },
    "20": {
      "L": "Therefore when you come together in the same place, it is not to eat the Lord's Supper;",
      "M": "So when you come together, it is not the Lord's Supper you are eating,",
      "T": "When you gather like this, it simply isn't the Lord's Supper that you're eating—"
    },
    "21": {
      "L": "for each one takes his own supper first in the eating, and one is hungry while another is drunk.",
      "M": "for as you eat, each of you goes ahead without waiting for anybody else. One remains hungry, another gets drunk.",
      "T": "because each of you rushes ahead with your own meal, and one person goes hungry while another has too much to drink."
    },
    "22": {
      "L": "For do you not have houses to eat and drink in? Or do you despise the assembly of God and humiliate those who have nothing? What shall I say to you? Shall I commend you? In this I do not commend you.",
      "M": "Don't you have homes to eat and drink in? Or do you despise the church of God by humiliating those who have nothing? What do you want me to say to you? Shall I praise you? Certainly not!",
      "T": "Don't you have homes to eat and drink in? Or is your aim to shame the church of God and humiliate the poor among you? What can I say? Should I praise you? Not for this."
    },
    "23": {
      "L": "For I received from the Lord what I also delivered to you: that the Lord Jesus, on the night he was betrayed, took bread,",
      "M": "For I received from the Lord what I also passed on to you: The Lord Jesus, on the night he was betrayed, took bread,",
      "T": "What I'm about to say I received directly from the Lord, and I passed it on to you: On the night he was handed over, the Lord Jesus took bread,"
    },
    "24": {
      "L": "and when he had given thanks he broke it and said, 'This is my body which is for you; do this in remembrance of me.'",
      "M": "and when he had given thanks, he broke it and said, 'This is my body, which is for you; do this in remembrance of me.'",
      "T": "and after giving thanks he broke it and said, 'This is my body, given for you. Keep doing this to remember me.'"
    },
    "25": {
      "L": "In the same way also the cup, after supper, saying, 'This cup is the new covenant in my blood; do this, as often as you drink it, in remembrance of me.'",
      "M": "In the same way, after supper he took the cup, saying, 'This cup is the new covenant in my blood; do this, whenever you drink it, in remembrance of me.'",
      "T": "He did the same with the cup after the meal: 'This cup is the new covenant, sealed in my blood. Every time you drink it, do it to remember me.'"
    },
    "26": {
      "L": "For as often as you eat this bread and drink the cup, you proclaim the death of the Lord until he comes.",
      "M": "For whenever you eat this bread and drink this cup, you proclaim the Lord's death until he comes.",
      "T": "Every time you eat this bread and drink this cup, you are announcing the Lord's death—and you will keep doing so until he returns."
    },
    "27": {
      "L": "So then whoever eats the bread or drinks the cup of the Lord in an unworthy manner will be guilty concerning the body and blood of the Lord.",
      "M": "So then, whoever eats the bread or drinks the cup of the Lord in an unworthy manner will be guilty of sinning against the body and blood of the Lord.",
      "T": "This means that anyone who eats the bread or drinks the cup carelessly is answerable for the body and blood of the Lord himself."
    },
    "28": {
      "L": "But let a person examine himself, and thus eat of the bread and drink of the cup.",
      "M": "Everyone ought to examine themselves before they eat the bread and drink from the cup.",
      "T": "Let everyone examine themselves before they eat and drink—then eat."
    },
    "29": {
      "L": "For the one who eats and drinks without discerning the body eats and drinks judgment upon himself.",
      "M": "For those who eat and drink without discerning the body of the Lord eat and drink judgment on themselves.",
      "T": "Eating and drinking without recognizing the Lord's body means eating and drinking a verdict against yourself."
    },
    "30": {
      "L": "For this reason many among you are weak and sick, and a number sleep.",
      "M": "That is why many among you are weak and sick, and a number of you have fallen asleep in death.",
      "T": "This is why many of you are weak and ill, and some have died."
    },
    "31": {
      "L": "But if we were judging ourselves rightly, we would not be judged.",
      "M": "But if we were more discerning with regard to ourselves, we would not come under such judgment.",
      "T": "If we honestly judged ourselves, we would not face this kind of judgment from God."
    },
    "32": {
      "L": "But being judged by the Lord, we are disciplined so that we may not be condemned with the world.",
      "M": "Nevertheless, when we are judged in this way by the Lord, we are being disciplined so that we will not be finally condemned with the world.",
      "T": "When the Lord brings this discipline on us, it is to keep us from being swept up in the world's final condemnation."
    },
    "33": {
      "L": "So then, my brothers, when you come together to eat, wait for one another.",
      "M": "So then, my brothers and sisters, when you gather to eat, you should all wait for each other.",
      "T": "So then, brothers and sisters, when you come together to share the meal, wait for one another."
    },
    "34": {
      "L": "If anyone is hungry, let him eat at home, so that you may not come together for judgment. And the remaining matters I will set in order when I come.",
      "M": "Anyone who is hungry should eat something at home, so that when you meet together it may not result in judgment. And when I come I will give further directions.",
      "T": "If you're hungry before you arrive, eat at home—so that your gatherings don't bring judgment down on you. The remaining questions I'll deal with in person when I come."
    }
  },
  "12": {
    "1": {
      "L": "Now concerning spiritual things, brothers, I do not want you to be ignorant.",
      "M": "Now about the gifts of the Spirit, brothers and sisters, I do not want you to be uninformed.",
      "T": "I don't want you in the dark about Spirit-given gifts, brothers and sisters."
    },
    "2": {
      "L": "You know that when you were Gentiles you were being led astray to mute idols, however you were led.",
      "M": "You know that when you were pagans, somehow or other you were influenced and led astray to mute idols.",
      "T": "You know what you were before: pagans, swept along—however you were led—toward speechless idols."
    },
    "3": {
      "L": "Therefore I make known to you that no one speaking by the Spirit of God says, 'Jesus is accursed,' and no one is able to say, 'Jesus is Lord,' except by the Holy Spirit.",
      "M": "Therefore I want you to know that no one who is speaking by the Spirit of God says, 'Jesus be cursed,' and no one can say, 'Jesus is Lord,' except by the Holy Spirit.",
      "T": "So here is how you discern: no one speaking by God's Spirit calls Jesus accursed—and no one can confess 'Jesus is Lord' except by the Holy Spirit."
    },
    "4": {
      "L": "Now there are diversities of gifts, but the same Spirit;",
      "M": "There are different kinds of gifts, but the same Spirit distributes them.",
      "T": "The gifts are varied, but they all come from the same Spirit."
    },
    "5": {
      "L": "and there are diversities of ministries, but the same Lord;",
      "M": "There are different kinds of service, but the same Lord.",
      "T": "The forms of service are varied, but it is the same Lord they serve."
    },
    "6": {
      "L": "and there are diversities of workings, but the same God who works all things in all.",
      "M": "There are different kinds of working, but in all of them and in everyone it is the same God at work.",
      "T": "The activities are varied, but the same God is at work in all of them through everyone."
    },
    "7": {
      "L": "But to each one is given the manifestation of the Spirit for the common benefit.",
      "M": "Now to each one the manifestation of the Spirit is given for the common good.",
      "T": "Each person is given a visible expression of the Spirit's presence—and it is for the benefit of everyone."
    },
    "8": {
      "L": "For to one is given through the Spirit a word of wisdom, and to another a word of knowledge according to the same Spirit,",
      "M": "To one there is given through the Spirit a message of wisdom, to another a message of knowledge by means of the same Spirit,",
      "T": "Through the Spirit, one person receives a word of wisdom; another, through the same Spirit, a word of knowledge."
    },
    "9": {
      "L": "to another faith by the same Spirit, and to another gifts of healing by the one Spirit,",
      "M": "to another faith by the same Spirit, to another gifts of healing by that one Spirit,",
      "T": "Another receives Spirit-given trust; another, gifts of healing—all from the same one Spirit."
    },
    "10": {
      "L": "and to another workings of miracles, and to another prophecy, and to another discerning of spirits, and to another different kinds of tongues, and to another the interpretation of tongues.",
      "M": "to another miraculous powers, to another prophecy, to another distinguishing between spirits, to another speaking in different kinds of tongues, and to still another the interpretation of tongues.",
      "T": "Another receives the power to work miracles; another, prophecy; another, the ability to discern spirits; another, various kinds of tongues; and another, the interpretation of those tongues."
    },
    "11": {
      "L": "But all these things are worked by the one and the same Spirit, distributing to each one separately just as he wills.",
      "M": "All these are the work of one and the same Spirit, and he distributes them to each one, just as he determines.",
      "T": "All of these are the work of one and the same Spirit, who gives to each person exactly what he chooses."
    },
    "12": {
      "L": "For just as the body is one and has many members, and all the members of the body, being many, are one body, so also is Christ.",
      "M": "Just as a body, though one, has many parts, but all its many parts form one body, so it is with Christ.",
      "T": "Think of the human body: one body, many parts—yet all those many parts together form one body. That is exactly how it is with Christ."
    },
    "13": {
      "L": "For by one Spirit we were all baptized into one body—whether Jews or Greeks, whether slaves or free—and we were all made to drink of one Spirit.",
      "M": "For we were all baptized by one Spirit so as to form one body—whether Jews or Gentiles, slave or free—and we were all given the one Spirit to drink.",
      "T": "In one Spirit we were all baptized into one body—Jewish or Greek, slave or free—and we were all immersed in the one Spirit, the same Spirit given to each of us."
    },
    "14": {
      "L": "For the body is not one member but many.",
      "M": "Even so the body is not made up of one part but of many.",
      "T": "A body is not a single part—it's made of many."
    },
    "15": {
      "L": "If the foot should say, 'Because I am not a hand, I do not belong to the body,' it is not for this reason any less a part of the body.",
      "M": "Now if the foot should say, 'Because I am not a hand, I do not belong to the body,' it would not for that reason stop being part of the body.",
      "T": "Suppose the foot were to say, 'Since I'm not a hand, I don't belong to the body'—that declaration wouldn't make it any less part of the body."
    },
    "16": {
      "L": "And if the ear should say, 'Because I am not an eye, I do not belong to the body,' it is not for this reason any less a part of the body.",
      "M": "And if the ear should say, 'Because I am not an eye, I do not belong to the body,' it would not for that reason stop being part of the body.",
      "T": "Or if the ear were to say, 'Since I'm not an eye, I don't belong to the body'—that declaration wouldn't make it any less a part of the body."
    },
    "17": {
      "L": "If the whole body were an eye, where would the hearing be? If the whole were hearing, where would the smelling be?",
      "M": "If the whole body were an eye, where would the sense of hearing be? If the whole body were an ear, where would the sense of smell be?",
      "T": "If the whole body were only an eye, how would you hear? If it were only an ear, how would you smell anything?"
    },
    "18": {
      "L": "But now God has placed the members, each one of them, in the body, just as he willed.",
      "M": "But in fact God has placed the parts in the body, every one of them, just as he wanted them to be.",
      "T": "As it is, God has arranged each and every part of the body exactly as he saw fit."
    },
    "19": {
      "L": "And if they were all one member, where would the body be?",
      "M": "If they were all one part, where would the body be?",
      "T": "If everything were just one part, there would be no body at all."
    },
    "20": {
      "L": "But now there are many members, but one body.",
      "M": "As it is, there are many parts, but one body.",
      "T": "But there are many parts—and they together make one body."
    },
    "21": {
      "L": "And the eye cannot say to the hand, 'I have no need of you,' or the head to the feet, 'I have no need of you.'",
      "M": "The eye cannot say to the hand, 'I don't need you!' And the head cannot say to the feet, 'I don't need you!'",
      "T": "The eye can't tell the hand, 'I don't need you.' And the head can't say to the feet, 'I don't need you.'"
    },
    "22": {
      "L": "On the contrary, the members of the body which seem to be weaker are much more necessary,",
      "M": "On the contrary, those parts of the body that seem to be weaker are indispensable,",
      "T": "In fact, the parts that seem weakest are often the most essential—"
    },
    "23": {
      "L": "and those members of the body which we consider to be less honorable, on these we bestow more abundant honor, and our unpresentable members have more abundant propriety,",
      "M": "and the parts that we think are less honorable we treat with special honor. And the parts that are unpresentable are treated with special modesty,",
      "T": "and we give extra care and honor to the parts we think look less distinguished, while our private parts are covered with the greatest propriety—"
    },
    "24": {
      "L": "but our presentable members have no need of it. But God has composed the body, having given more abundant honor to the member that lacks,",
      "M": "while our presentable parts need no special treatment. But God has put the body together, giving greater honor to the parts that lacked it,",
      "T": "things our more presentable parts don't require. God himself has arranged the body this way, giving extra honor to whatever seemed to lack it—"
    },
    "25": {
      "L": "so that there may be no division in the body, but that the members may have equal concern for one another.",
      "M": "so that there should be no division in the body, but that its parts should have equal concern for each other.",
      "T": "so that there would be no split in the body, and every part would genuinely care for every other part."
    },
    "26": {
      "L": "And whether one member suffers, all the members suffer with it; or one member is honored, all the members rejoice with it.",
      "M": "If one part suffers, every part suffers with it; if one part is honored, every part rejoices with it.",
      "T": "When one part of the body suffers, all the other parts suffer alongside it. When one part is honored, all the others share in the joy."
    },
    "27": {
      "L": "Now you are the body of Christ, and members in particular.",
      "M": "Now you are the body of Christ, and each one of you is a part of it.",
      "T": "You are the body of Christ—and each of you is a distinct, irreplaceable part of it."
    },
    "28": {
      "L": "And God has set in the assembly first apostles, second prophets, third teachers, then miracles, then gifts of healing, helps, governments, diversities of tongues.",
      "M": "And God has placed in the church first of all apostles, second prophets, third teachers, then miracles, then gifts of healing, of helping, of guidance, and of different kinds of tongues.",
      "T": "And God himself has appointed roles within the church: first apostles, second prophets, third teachers—then those who work miracles, those who have gifts of healing, those who help others, those who lead, those who speak in various kinds of tongues."
    },
    "29": {
      "L": "Are all apostles? Are all prophets? Are all teachers? Are all workers of miracles?",
      "M": "Are all apostles? Are all prophets? Are all teachers? Do all work miracles?",
      "T": "Is everyone an apostle? Is everyone a prophet? Is everyone a teacher? Does everyone work miracles?"
    },
    "30": {
      "L": "Do all have gifts of healing? Do all speak with tongues? Do all interpret?",
      "M": "Do all have gifts of healing? Do all speak in tongues? Do all interpret?",
      "T": "Does everyone have gifts of healing? Does everyone speak in tongues? Does everyone interpret?"
    },
    "31": {
      "L": "But earnestly desire the greater gifts. And yet I will show you a still more excellent way.",
      "M": "Now eagerly desire the greater gifts. And yet I will show you the most excellent way.",
      "T": "Pursue the greater gifts with eagerness—but I am going to show you a way that surpasses them all."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '1corinthians')
        merge_tier(existing, CORINTHIANS, tier_key)
        save(tier_dir, '1corinthians', existing)
    print('1 Corinthians 10–12 written.')

if __name__ == '__main__':
    main()
