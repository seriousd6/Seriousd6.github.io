"""
MKT 2 Corinthians chapters 10–12 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-2corinthians-10-12.py

Translation decisions:
- G4561 σάρξ (flesh): "flesh" in L always; 10:2-3 rendered "world/human" in M/T (peristatic,
    ethical sense — Paul is not talking about carnality but merely-human resources); 11:18 "worldly"
    in M/T; 12:7 "flesh" retained across all tiers — the thorn is σκόλοψ τῇ σαρκί, a physical
    or experiential affliction; the idiom is best left literal even in T
- G4151 πνεῦμα (Spirit/spirit): 11:4 "Spirit" (capitalized) — the Holy Spirit received at
    conversion, contrasted with a counterfeit; 12:18 "Spirit" (capitalized) — the Holy Spirit
    guiding both Paul and Titus in the same course; lowercase in no occurrence here
- G1343 δικαιοσύνη (righteousness): 11:15 "righteousness" (L/M); "righteousness" (T) — Satan's
    ministers disguise themselves as ministers of righteousness; the irony is theological: they
    claim the very quality that is God's gift
- G3056 λόγος (word/speech): 10:10 "speech" (L/M/T) — Paul's detractors mock his rhetorical
    ability; 11:6 "speech" (L), "speaking ability" (M/T) — rude in speech but not in knowledge
- G2962 κύριος (Lord): "Lord" all tiers — no deviation
- G1577 ἐκκλησία (church): "churches" all tiers — used generically for the network of
    congregations; no single-assembly context that would demand "assembly"
- G4102 πίστις (faith): does not appear prominently in chs 10-12
- G26 ἀγάπη / G25 ἀγαπάω: 11:11 uses verb ἀγαπάω "I love you" — rendered "love" all tiers;
    12:15 same — willed, self-giving love not mere affection
- The "super-apostles" (ὑπερλίαν ἀπόστολοι, 11:5, 12:11): "super-apostles" in L/M (quotation
    marks convey Paul's irony); "great apostles" in T — the irony is surfaced by narrative framing
- 11:2 "betrothed" / "espoused" (G718 ἁρμόζω): "betrothed" (L/M); "promised as a bride" (T)
    — the marriage contract metaphor draws on OT covenant imagery (Hos 2; Ezek 16)
- 12:2 "third heaven" / "paradise" (v4): retained in all tiers — Paul deliberately avoids
    cosmological specificity; T notes the identity of the man as Paul himself (implied by v7
    self-identification), so "I was caught up" in T is interpretive but defensible
- 12:7 "thorn in the flesh" — σκόλοψ (stake/splinter/thorn): "thorn" all tiers; the identity
    of the affliction is deliberately kept open; T does not speculate
- 11:24 "forty stripes minus one" — the Jewish synagogue punishment of 39 lashes (Deut 25:3);
    "thirty-nine lashes" in T for immediacy
- 11:25 "in the deep" (G1037 βυθός) — open sea / depth; "adrift at sea" in T
- 10:17 quotes Jer 9:24 LXX — maintained as Scripture quotation in all tiers
- Aspect: 10:4-5 present participles (ongoing spiritual warfare action) — continuous sense in M/T;
    12:8 aorist παρεκάλεσα (single act of pleading, repeated three times) — "three times I begged"
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

CORINTHIANS2 = {
  "10": {
    "1": {
      "L": "Now I myself Paul beseech you by the meekness and gentleness of Christ — I who in face am lowly among you, but being absent am bold toward you —",
      "M": "By the meekness and gentleness of Christ, I appeal to you—I, Paul, who am 'timid' when face to face with you, but 'bold' toward you when away!",
      "T": "It is I, Paul, who appeal to you personally, in the meekness and gentleness of Christ—I who, they say, am timid in person but bold when writing from a distance."
    },
    "2": {
      "L": "I beg of you that when I am present I may not need to be bold with the confidence with which I reckon to be bold against some who reckon of us as walking according to the flesh.",
      "M": "I beg you that when I come I may not have to be as bold as I expect to be toward some people who think that we live by the standards of this world.",
      "T": "Please don't make me be harsh when I arrive—for I can indeed be bold against those who think that we live and operate by merely human means."
    },
    "3": {
      "L": "For though we walk in the flesh, we do not war according to the flesh.",
      "M": "For though we live in the world, we do not wage war as the world does.",
      "T": "We are human beings, yes, but the battle we fight is not a human battle."
    },
    "4": {
      "L": "For the weapons of our warfare are not of the flesh, but mighty to God for the pulling down of strongholds —",
      "M": "The weapons we fight with are not the weapons of the world. On the contrary, they have divine power to demolish strongholds.",
      "T": "We use God's mighty weapons, not worldly ones, for knocking down the strongholds of human reasoning."
    },
    "5": {
      "L": "casting down reasonings and every high thing that exalts itself against the knowledge of God, and bringing every thought captive to the obedience of Christ —",
      "M": "We demolish arguments and every pretension that sets itself up against the knowledge of God, and we take captive every thought to make it obedient to Christ.",
      "T": "We demolish every proud obstacle that keeps people from knowing God, and we capture every rebellious thought and make it submit to Christ."
    },
    "6": {
      "L": "and being ready to punish every disobedience, when your obedience is fulfilled.",
      "M": "And we will be ready to punish every act of disobedience, once your obedience is complete.",
      "T": "Once you are fully obedient, we will deal firmly with anyone among you who remains in rebellion."
    },
    "7": {
      "L": "Do you look at things according to outward appearance? If anyone is persuaded in himself that he is of Christ, let him reckon this again in himself, that as he is of Christ, so also are we.",
      "M": "You are judging by appearances. If anyone is confident that they belong to Christ, they should consider again that we belong to Christ just as much as they do.",
      "T": "You are looking only at what is right in front of you. If anyone is sure they belong to Christ, let them think carefully: so do we."
    },
    "8": {
      "L": "For even if I should boast somewhat more of our authority, which the Lord gave us for building you up and not for tearing you down, I will not be ashamed —",
      "M": "So even if I boast somewhat freely about the authority the Lord gave us for building you up rather than pulling you down, I will not be ashamed of it.",
      "T": "Even if I boast a little too freely about the authority the Lord gave us for building you up rather than tearing you down, I will not be put to shame by that boast."
    },
    "9": {
      "L": "so that I may not seem as if I am terrifying you through my letters.",
      "M": "I do not want to seem to be trying to frighten you with my letters.",
      "T": "I don't want it to look as though I'm trying to intimidate you with my letters."
    },
    "10": {
      "L": "For his letters, they say, are weighty and strong, but his bodily presence is weak and his speech contemptible.",
      "M": "For some say, 'His letters are weighty and forceful, but in person he is unimpressive and his speaking amounts to nothing.'",
      "T": "His critics say that his letters are stern and powerful, but when he shows up in person he is a disappointment, and his preaching is not worth listening to."
    },
    "11": {
      "L": "Let such a one reckon this, that what we are in word by letters when absent, such also we are in deed when present.",
      "M": "Such people should realize that what we are in our letters when we are absent, we will be in our actions when we are present.",
      "T": "Such people should understand that what we say in our letters from a distance, we will back up with action when we arrive."
    },
    "12": {
      "L": "For we dare not class or compare ourselves with some of those who commend themselves. But when they measure themselves by themselves and compare themselves with themselves, they have no understanding.",
      "M": "We do not dare to classify or compare ourselves with some who commend themselves. When they measure themselves by themselves and compare themselves with themselves, they are not wise.",
      "T": "We would never dare to compare ourselves to those who commend themselves so freely. When they measure their success by their own standards and compare themselves to each other—that is sheer foolishness."
    },
    "13": {
      "L": "But we will not boast beyond our measure, but according to the measure of the rule which God apportioned to us as a measure, to reach even to you.",
      "M": "We, however, will not boast beyond proper limits, but will confine our boasting to the sphere of service God himself has assigned to us—a sphere that also includes you.",
      "T": "We will not boast beyond the boundaries God has set for us. We will only boast about the area of work he has assigned to us, an area that reaches all the way to you."
    },
    "14": {
      "L": "For we do not stretch beyond our measure, as though we did not reach to you; for we came even to you in the gospel of Christ.",
      "M": "We are not going too far in our boasting, as would be the case if we had not come to you, for we did get as far as you with the gospel of Christ.",
      "T": "We are not overstepping our boundaries. We were the first to bring the gospel of Christ all the way to you, so you are well within our assigned territory."
    },
    "15": {
      "L": "Not boasting beyond our measure in other men's labors, but having hope that as your faith grows our sphere among you will be greatly enlarged,",
      "M": "Neither do we go beyond our limits by boasting of work done by others. Our hope is that, as your faith continues to grow, our sphere of activity among you will greatly expand,",
      "T": "We don't take credit for the work others have done. Instead, as your faith matures, we hope that the scope of our mission will grow greatly among you."
    },
    "16": {
      "L": "so as to preach the gospel in the regions beyond you, without boasting in another man's line of things already made ready.",
      "M": "so that we can preach the gospel in the regions beyond you. For we do not want to boast about work already done in someone else's territory.",
      "T": "This will allow us to carry the gospel even farther, into lands beyond you. We want to preach where no one else has laid a foundation—not to boast about what someone else has already accomplished."
    },
    "17": {
      "L": "But he that glorieth, let him glory in the Lord.",
      "M": "But, 'Let the one who boasts boast in the Lord.'",
      "T": "As the Scripture says, 'If you want to boast, boast only about the Lord.'"
    },
    "18": {
      "L": "For not he that commendeth himself is approved, but he whom the Lord commendeth.",
      "M": "For it is not the one who commends himself who is approved, but the one whom the Lord commends.",
      "T": "The only approval that matters is the Lord's commendation—not self-congratulation."
    }
  },
  "11": {
    "1": {
      "L": "Would that you would bear with me in a little foolishness — indeed, do bear with me!",
      "M": "I hope you will put up with me in a little foolishness. Yes, please put up with me!",
      "T": "I hope you'll be patient with me as I say some foolish things. Bear with me, please!"
    },
    "2": {
      "L": "For I am jealous for you with a godly jealousy; for I betrothed you to one husband, to present you as a pure virgin to Christ.",
      "M": "I am jealous for you with a godly jealousy. I promised you to one husband, to present you as a pure virgin to him.",
      "T": "For I am jealous for you with the jealousy of God himself. I promised you as a pure bride to one husband—Christ."
    },
    "3": {
      "L": "But I fear lest somehow as the serpent deceived Eve in his craftiness, your minds might be corrupted from the simplicity and purity that is in Christ.",
      "M": "But I am afraid that just as Eve was deceived by the serpent's cunning, your minds may somehow be led astray from your sincere and pure devotion to Christ.",
      "T": "But I am afraid that your minds may be corrupted and led away from your wholehearted devotion to Christ—just as Eve was deceived by the serpent's cunning lies."
    },
    "4": {
      "L": "For if the one coming preaches another Jesus whom we did not preach, or you receive a different spirit which you did not receive, or a different gospel which you did not accept, you put up with it well enough.",
      "M": "For if someone comes to you and preaches a Jesus other than the Jesus we preached, or if you receive a different spirit from the Spirit you received, or a different gospel from the one you accepted, you put up with it easily enough.",
      "T": "You seem quite willing to put up with someone who comes and tells you about a different Jesus—not the one we preached—or about a different Spirit than the one you received, or a different kind of gospel."
    },
    "5": {
      "L": "For I reckon that in nothing I was behind the very chiefest apostles.",
      "M": "I do not think I am in the least inferior to those 'super-apostles.'",
      "T": "But I don't think I am inferior in any way to these great apostles who claim such authority."
    },
    "6": {
      "L": "But though I am rude in speech, yet not in knowledge; but in all things I have been made manifest among all men to you.",
      "M": "I may indeed be untrained as a speaker, but I do have knowledge. We have made this perfectly clear to you in every way.",
      "T": "I may not be a polished speaker, but I know what I am talking about—and you know it. We have made that clear to you in every possible way."
    },
    "7": {
      "L": "Or did I commit a sin in humbling myself that you might be exalted, because I preached the gospel of God to you freely?",
      "M": "Was it a sin for me to lower myself in order to elevate you by preaching the gospel of God to you free of charge?",
      "T": "Was it wrong of me to humble myself so that you could be lifted up? I preached God's Good News to you without charging you anything."
    },
    "8": {
      "L": "I robbed other churches, taking wages of them, to minister to you.",
      "M": "I robbed other churches by receiving support from them so as to serve you.",
      "T": "I was supported by other churches, essentially taking their resources in order to serve you."
    },
    "9": {
      "L": "And when I was present with you and was in need, I was not a burden to anyone; for the brothers who came from Macedonia supplied my need. And in everything I kept myself from being burdensome to you, and so will I keep myself.",
      "M": "And when I was with you and needed something, I was not a burden to anyone, for the brothers who came from Macedonia supplied what I needed. I have kept myself from being a burden to you in any way, and will continue to do so.",
      "T": "When I was with you and ran short of money, I never asked you for anything. The believers from Macedonia brought me all I needed. I have never been a financial burden to you, and I never will be."
    },
    "10": {
      "L": "As the truth of Christ is in me, this boasting of mine shall not be stopped in the regions of Achaia.",
      "M": "As surely as the truth of Christ is in me, nobody in the regions of Achaia will stop this boasting of mine.",
      "T": "I am absolutely committed, by the truth of Christ within me, that no one in all of Greece will take away this boast of mine."
    },
    "11": {
      "L": "Wherefore? Because I love you not? God knoweth.",
      "M": "Why? Because I do not love you? God knows I do!",
      "T": "Why? Because I don't love you? God knows I do!"
    },
    "12": {
      "L": "But what I do I will also continue to do, in order to cut off opportunity from those who desire an opportunity to be found as we are in what they boast.",
      "M": "And I will keep on doing what I am doing in order to cut the ground from under those who want an opportunity to be considered equal with us in the things they boast about.",
      "T": "I will keep on doing this so as to undermine those who are looking for an opportunity to claim that their work is on the same level as ours."
    },
    "13": {
      "L": "For such are false apostles, deceitful workers, transforming themselves into apostles of Christ.",
      "M": "For such people are false apostles, deceitful workers, masquerading as apostles of Christ.",
      "T": "These people are false apostles. They are deceitful workers who disguise themselves as apostles of Christ."
    },
    "14": {
      "L": "And no marvel; for Satan himself transforms himself into an angel of light.",
      "M": "And no wonder, for Satan himself masquerades as an angel of light.",
      "T": "This should not surprise us. Even Satan disguises himself as an angel of light."
    },
    "15": {
      "L": "It is no great thing therefore if his ministers also transform themselves as ministers of righteousness, whose end shall be according to their works.",
      "M": "It is not surprising, then, if his servants also masquerade as servants of righteousness. Their end will be what their actions deserve.",
      "T": "So it is no wonder his servants also disguise themselves as servants of righteousness. In the end they will receive the punishment their wicked deeds deserve."
    },
    "16": {
      "L": "I say again, let no one think me a fool; but if otherwise, receive me even as a fool, that I also may boast a little.",
      "M": "I repeat: Let no one take me for a fool. But if you do, then receive me just as you would a fool, so that I may do a little boasting.",
      "T": "I say again—please don't think of me as a fool. But even if you do, hear me out so that I too may do a little boasting."
    },
    "17": {
      "L": "What I speak, I speak not after the Lord, but as in foolishness, in this confidence of boasting.",
      "M": "In this self-confident boasting I am not talking as the Lord would, but as a fool.",
      "T": "I am not speaking as the Lord would in this matter—I am talking like a fool in my boastful confidence."
    },
    "18": {
      "L": "Seeing that many glory after the flesh, I will glory also.",
      "M": "Since many are boasting in the way the world does, I too will boast.",
      "T": "Since many others are boasting about their worldly credentials, I will too."
    },
    "19": {
      "L": "For you gladly bear with fools, seeing ye yourselves are wise.",
      "M": "You gladly put up with fools since you are so wise!",
      "T": "After all, you think you are so wise—yet you gladly put up with fools!"
    },
    "20": {
      "L": "For you bear it if a man bring you into bondage, if a man devour you, if a man take you, if a man exalt himself, if a man smite you on the face.",
      "M": "In fact, you even put up with anyone who enslaves you or exploits you or takes advantage of you or puts on airs or slaps you in the face.",
      "T": "You put up with it when someone controls you, devours your resources, takes advantage of you, acts arrogantly toward you, or even slaps you in the face."
    },
    "21": {
      "L": "I speak by way of reproach, as though we had been weak. But in whatever any man is bold — I speak in foolishness — I am bold also.",
      "M": "To my shame I admit that we were too weak for that! Whatever anyone else dares to boast about—I am speaking as a fool—I also dare to boast about.",
      "T": "I'm ashamed to say that we were too 'weak' to treat you that way! But whatever those others dare to claim—I'm speaking like a fool now—I dare to claim it too."
    },
    "22": {
      "L": "Are they Hebrews? So am I. Are they Israelites? So am I. Are they the seed of Abraham? So am I.",
      "M": "Are they Hebrews? So am I. Are they Israelites? So am I. Are they Abraham's descendants? So am I.",
      "T": "Are they Hebrews? So am I. Are they Israelites? So am I. Are they descendants of Abraham? So am I."
    },
    "23": {
      "L": "Are they servants of Christ? — I speak as one beside himself — I more so; in labors more abundantly, in stripes above measure, in prisons more frequently, in deaths often.",
      "M": "Are they servants of Christ? (I am out of my mind to talk like this.) I am more. I have worked much harder, been in prison more frequently, been flogged more severely, and been exposed to death again and again.",
      "T": "Are they servants of Christ? I know I sound like a madman, but I have served him far more! I have worked harder, been put in prison more often, been whipped times without number, and faced death again and again."
    },
    "24": {
      "L": "Five times I received of the Jews forty stripes save one.",
      "M": "Five times I received from the Jews the forty lashes minus one.",
      "T": "Five different times the Jewish leaders gave me thirty-nine lashes."
    },
    "25": {
      "L": "Thrice was I beaten with rods, once was I stoned, thrice I suffered shipwreck, a night and a day I have been in the deep.",
      "M": "Three times I was beaten with rods, once I was pelted with stones, three times I was shipwrecked, I spent a night and a day in the open sea,",
      "T": "Three times I was beaten with rods. Once I was stoned. Three times I was shipwrecked. Once I spent a whole night and a day adrift at sea."
    },
    "26": {
      "L": "in journeyings often; in perils of rivers, in perils of robbers, in perils from my own countrymen, in perils from the Gentiles, in perils in the city, in perils in the wilderness, in perils in the sea, in perils among false brothers;",
      "M": "I have been constantly on the move. I have been in danger from rivers, in danger from bandits, in danger from my fellow Jews, in danger from Gentiles; in danger in the city, in danger in the country, in danger at sea; and in danger from false believers.",
      "T": "I have traveled many weary miles and faced danger from rivers, from robbers, from my own people the Jews, and from Gentiles. I have faced danger in the cities, in the deserts, and on the seas—and from men who claim to be believers but are not."
    },
    "27": {
      "L": "in toil and hardship, in many a sleepless night, in hunger and thirst, often without food, in cold and nakedness.",
      "M": "I have labored and toiled and have often gone without sleep; I have known hunger and thirst and have often gone without food; I have been cold and naked.",
      "T": "I have worked hard and long, enduring many sleepless nights. I have been hungry and thirsty and have often gone without food. I have shivered in the cold without enough clothing to keep me warm."
    },
    "28": {
      "L": "Beside those things that are without, there is that which presseth upon me daily, the care of all the churches.",
      "M": "Besides everything else, I face daily the pressure of my concern for all the churches.",
      "T": "Then, on top of everything else, the daily burden of my deep concern for all the churches weighs on me constantly."
    },
    "29": {
      "L": "Who is weak, and I am not weak? Who is made to stumble, and I burn not?",
      "M": "Who is weak, and I do not feel weak? Who is led into sin, and I do not inwardly burn?",
      "T": "Who is weak without my feeling that weakness? Who is led into sin, and I do not burn with grief and anger?"
    },
    "30": {
      "L": "If I must needs glory, I will glory of the things that concern my weakness.",
      "M": "If I must boast, I will boast of the things that show my weakness.",
      "T": "If I must boast, I would rather boast about the things that show how weak I am."
    },
    "31": {
      "L": "The God and Father of the Lord Jesus, who is blessed for evermore, knoweth that I lie not.",
      "M": "The God and Father of the Lord Jesus, who is to be praised forever, knows that I am not lying.",
      "T": "God, the Father of our Lord Jesus, who is worthy of eternal praise, knows that I am not lying."
    },
    "32": {
      "L": "In Damascus the governor under Aretas the king was guarding the city of the Damascenes in order to seize me,",
      "M": "In Damascus the governor under King Aretas had the city of the Damascenes guarded in order to arrest me.",
      "T": "When I was in Damascus, the governor under King Aretas had the city surrounded and wanted to capture me."
    },
    "33": {
      "L": "and through a window in the wall I was let down in a basket and escaped his hands.",
      "M": "But I was lowered in a basket from a window in the wall and slipped through his hands.",
      "T": "But I was let down in a basket through an opening in the city wall, and that is how I escaped from him."
    }
  },
  "12": {
    "1": {
      "L": "It is necessary to boast; it is not profitable, but I will come to visions and revelations of the Lord.",
      "M": "I must go on boasting. Although there is nothing to be gained, I will go on to visions and revelations from the Lord.",
      "T": "This boasting is necessary even though it accomplishes nothing. So let me tell you about the visions and revelations I received from the Lord."
    },
    "2": {
      "L": "I know a man in Christ, fourteen years ago — whether in the body, I know not; or whether out of the body, I know not; God knoweth — such a one was caught up even to the third heaven.",
      "M": "I know a man in Christ who fourteen years ago was caught up to the third heaven. Whether it was in the body or out of the body I do not know—God knows.",
      "T": "I was caught up to the third heaven fourteen years ago. Whether I was in my body or out of my body, I don't know—only God knows."
    },
    "3": {
      "L": "And I know such a man — whether in the body, or apart from the body, I know not; God knoweth —",
      "M": "And I know that this man—whether in the body or apart from the body I do not know, but God knows—",
      "T": "And I know that this man—whether in his body or away from his body, I cannot tell, but God knows—"
    },
    "4": {
      "L": "was caught up into paradise and heard unspeakable words, which it is not lawful for a man to utter.",
      "M": "was caught up to paradise and heard inexpressible things, things that no one is permitted to tell.",
      "T": "was caught up into paradise and heard things so astounding they cannot be expressed in words—things no human being is allowed to repeat."
    },
    "5": {
      "L": "On behalf of such a one I will glory; but on mine own behalf I will not glory, save in my weaknesses.",
      "M": "I will boast about a man like that, but I will not boast about myself, except about my weaknesses.",
      "T": "That experience is worth boasting about. But I am not going to boast about myself—only about my weaknesses."
    },
    "6": {
      "L": "For if I should desire to glory, I shall not be a fool; for I shall speak the truth: but I forbear, lest any man should account of me above that which he seeth me to be, or heareth from me.",
      "M": "Even if I should choose to boast, I would not be a fool, because I would be speaking the truth. But I refrain, so no one will think more of me than is warranted by what I do or say,",
      "T": "If I wanted to boast I would be no fool in doing so, because I would be telling the truth. But I won't do it, because I don't want anyone to think more highly of me than what they can see in my life and work."
    },
    "7": {
      "L": "And by reason of the exceeding greatness of the revelations — wherefore, that I should not be exalted overmuch, there was given to me a thorn in the flesh, a messenger of Satan to buffet me, that I should not be exalted overmuch.",
      "M": "or because of these surpassingly great revelations. Therefore, in order to keep me from becoming conceited, I was given a thorn in my flesh, a messenger of Satan, to torment me.",
      "T": "Even though I received such wonderful revelations from God, so I wouldn't become proud of them, I was given a thorn in my flesh—a messenger from Satan—to torment me and keep me from becoming proud."
    },
    "8": {
      "L": "Concerning this thing I besought the Lord thrice, that it might depart from me.",
      "M": "Three times I pleaded with the Lord to take it away from me.",
      "T": "Three times I begged the Lord to take it away from me."
    },
    "9": {
      "L": "And he hath said unto me, My grace is sufficient for thee: for my power is made perfect in weakness. Most gladly therefore will I rather glory in my weaknesses, that the power of Christ may rest upon me.",
      "M": "But he said to me, 'My grace is sufficient for you, for my power is made perfect in weakness.' Therefore I will boast all the more gladly about my weaknesses, so that Christ's power may rest on me.",
      "T": "Each time he said, 'My grace is all you need. My power works best in weakness.' So now I am glad to boast about my weaknesses, so that the power of Christ can work through me."
    },
    "10": {
      "L": "Wherefore I take pleasure in weaknesses, in insults, in necessities, in persecutions, in distresses, for Christ's sake: for when I am weak, then am I strong.",
      "M": "That is why, for Christ's sake, I delight in weaknesses, in insults, in hardships, in persecutions, in difficulties. For when I am weak, then I am strong.",
      "T": "That is why I take pleasure in my weaknesses, and in the insults, hardships, persecutions, and troubles that I suffer for Christ. For when I am weak, then I am strong."
    },
    "11": {
      "L": "I am become a fool in glorying; ye compelled me: for I ought to have been commended of you: for in nothing was I behind the very chiefest apostles, though I be nothing.",
      "M": "I have made a fool of myself, but you drove me to it. I ought to have been commended by you, for I am not in the least inferior to the 'super-apostles,' even though I am nothing.",
      "T": "You have made me act like a fool—boasting like this. You ought to be writing commendations for me, for I am not at all inferior to these great apostles, even though I am nothing at all."
    },
    "12": {
      "L": "Truly the signs of an apostle were wrought among you in all patience, by signs and wonders and mighty works.",
      "M": "I persevered in demonstrating among you the marks of a true apostle, including signs, wonders and miracles.",
      "T": "When I was with you, I certainly gave you proof that I am a true apostle. For I patiently performed many signs, wonders, and miracles among you."
    },
    "13": {
      "L": "For what is there wherein ye were made inferior to the rest of the churches, except it be that I myself was not a burden to you? Forgive me this wrong.",
      "M": "How were you inferior to the other churches, except that I was never a burden to you? Forgive me this wrong!",
      "T": "The only thing I failed to do, which I do for the other churches, was to let you support me financially. Please forgive me for this terrible wrong!"
    },
    "14": {
      "L": "Behold, this is the third time I am ready to come to you; and I will not be a burden to you: for I seek not yours, but you: for the children ought not to lay up for the parents, but the parents for the children.",
      "M": "Now I am ready to visit you for the third time, and I will not be a burden to you, because what I want is not your possessions but you. After all, children should not have to save up for their parents, but parents for their children.",
      "T": "Now I am coming to you for the third time, and I will not be a burden to you. I don't want what you have—I want you. Anyway, children shouldn't have to provide for their parents. Rather, parents provide for their children."
    },
    "15": {
      "L": "And I will most gladly spend and be spent for your souls. If I love you more abundantly, am I loved the less?",
      "M": "So I will very gladly spend for you everything I have and expend myself as well. If I love you more, will you love me less?",
      "T": "I will gladly spend everything I have, and I will even wear myself out, for the sake of your souls. If I love you more, does that mean you will love me less?"
    },
    "16": {
      "L": "But be it so, I did not myself burden you; but, being crafty, I caught you with guile.",
      "M": "Be that as it may, I have not been a burden to you. Yet, crafty fellow that I am, I caught you by trickery!",
      "T": "Some admit I was not a burden to you—but others still think I was sneaky and that I took advantage of you by trickery."
    },
    "17": {
      "L": "Did I take advantage of you by any of them whom I have sent unto you?",
      "M": "Did I exploit you through any of the men I sent to you?",
      "T": "But tell me—did any of the men I sent to you take advantage of you?"
    },
    "18": {
      "L": "I desired Titus to go, and I sent the brother with him. Did Titus take advantage of you? Did we not walk in the same spirit? Did we not walk in the same steps?",
      "M": "I urged Titus to go to you and I sent our brother with him. Titus did not exploit you, did he? Did we not walk in the same footsteps by the same Spirit?",
      "T": "When I urged Titus to visit you and sent our brother along with him, did Titus take advantage of you? No! And didn't we both walk in the same Spirit and follow the same course?"
    },
    "19": {
      "L": "Ye think all this time that we are excusing ourselves unto you. In the sight of God speak we in Christ; and all things, beloved, are for your edifying.",
      "M": "Have you been thinking all along that we have been defending ourselves to you? We have been speaking in the sight of God as those in Christ; and everything we do, dear friends, is for your strengthening.",
      "T": "Perhaps you think we have been defending ourselves to you all this time. Not so! We speak in Christ's presence, before God himself—and everything we do, dear friends, is for your spiritual growth."
    },
    "20": {
      "L": "For I fear, lest by any means, when I come, I should find you not such as I would, and should myself be found of you such as ye would not; lest by any means there should be strife, jealousy, wraths, factions, slanders, whisperings, swellings, tumults:",
      "M": "For I am afraid that when I come I may not find you as I want you to be, and you may not find me as you want me to be. I fear that there may be discord, jealousy, fits of rage, selfish ambition, slander, gossip, arrogance and disorder.",
      "T": "I am afraid that when I come I won't like what I find, and you won't like how I respond. I am afraid I will find quarreling, jealousy, outbursts of anger, selfishness, slander, gossip, arrogance, and disorderly conduct."
    },
    "21": {
      "L": "lest again when I come my God should humble me before you, and I should mourn for many of them that have sinned heretofore, and have not repented of the uncleanness and fornication and lasciviousness which they practised.",
      "M": "I am afraid that when I come again my God will humble me before you, and I will be grieved over many who have sinned earlier and have not repented of the impurity, sexual sin and debauchery in which they have indulged.",
      "T": "Yes, I am afraid that when I come again, God will humble me before you. And I will grieve over many of you who sinned before and still have not repented of your impurity, your sexual immorality, and your eagerness for lustful pleasure."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '2corinthians')
        merge_tier(existing, CORINTHIANS2, tier_key)
        save(tier_dir, '2corinthians', existing)
    print('2 Corinthians 10–12 written.')

if __name__ == '__main__':
    main()
