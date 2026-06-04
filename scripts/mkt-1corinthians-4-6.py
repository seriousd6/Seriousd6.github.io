"""
MKT 1 Corinthians chapters 4–6 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-1corinthians-4-6.py

Translation decisions:
- G2962 (κύριος): "Lord" across all tiers — consistent with all Pauline scripts.
- G4151 (πνεῦμα): "Spirit" (capitalized) when clearly the divine Holy Spirit (5:4 assembly power; 6:11, 6:19);
  lowercase "spirit" for the human spirit (5:5 "that his spirit may be saved"; 4:21 spirit of gentleness;
  6:17 "one spirit with him" — the union-with-Christ sense is debated but lowercase fits the grammar).
- G4561 (σάρξ): "flesh" in L always. In 5:5 "destruction of the flesh" = the sinful bodily sphere;
  rendered "flesh" (L), "sinful nature" (M), and "this mortal life" (T) to surface the eschatological
  dimension. In 6:16 "one flesh" kept across all tiers (OT quotation from Gen 2:24).
- G4202 (πορνεία) / G4203 (πορνεύω): "fornication" in L (word-for-word); "sexual immorality" in M/T —
  the Greek term covers all illicit sexual acts; "sexual immorality" is most accurate in modern English.
- G3120 (μαλακοί) / G733 (ἀρσενοκοῖται) at 6:9: Two distinct Greek terms. μαλακοί = "the soft ones",
  the passive partner in same-sex acts. ἀρσενοκοῖται = Paul's compound from Lev 18:22/20:13 LXX,
  the active partner. L renders word-for-word; M/T name each role clearly. Both terms apply to the act,
  not merely orientation. Documented deviation from the glossary draft which lists only generic renderings.
- G3466 (μυστήριον): "mysteries" throughout — the sacred trusts of God, not esoteric secrets per se;
  T surfaces the stewardship-of-revelation sense.
- G5547 (Χριστός): "Christ" in L/M; "Christ" in T (not "Messiah" — Corinthian context is primarily
  Greek, not Jewish-messianic; "Christ" functions as a proper name here as in all Pauline corpus).
- G1577 (ἐκκλησία): "church" in all tiers — consistent with Romans, Galatians, Philippians scripts.
- G1343 (δικαιοσύνη) implied at 6:11 (δεδικαίωσθε): "justified" (L/M); "declared righteous" (T)
  to preserve the forensic sense.
- 4:6 "not to go beyond what is written": the phrase τὸ μὴ ὑπὲρ ἃ γέγραπται is obscure — probably a
  Corinthian slogan or a compressed reference to OT scripture. All tiers reflect the plain sense.
- 6:12 "All things are lawful for me": a Corinthian slogan Paul quotes twice before refuting;
  shown in quotation marks in M/T to signal the citation.
- 6:13 "Food is meant for the stomach": likewise a Corinthian slogan; shown in quotation marks in M/T.
- 6:20 follows the critical text (NA28); the phrase "and in your spirit, which are God's" is omitted
  as it lacks support in earliest manuscripts.
- Aspect: 6:11 three aorist passives (washed, sanctified, justified) = three completed acts at conversion;
  rendered as simple past across all tiers to honour the aorist punctiliar force.
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

CORINTHIANS_1 = {
  "4": {
    "1": {
      "L": "So let a man reckon us as servants of Christ and stewards of the mysteries of God.",
      "M": "So then, people should regard us as servants of Christ and as stewards entrusted with the mysteries of God.",
      "T": "Think of us this way: we are servants of Christ, and we have been entrusted with the sacred things of God."
    },
    "2": {
      "L": "Moreover, it is required among stewards that one be found faithful.",
      "M": "Now it is required that those who have been given a trust must prove faithful.",
      "T": "The one requirement for a steward is this: he must be found trustworthy."
    },
    "3": {
      "L": "But to me it is a very small thing to be examined by you, or by any human court; in fact, I do not even examine myself.",
      "M": "I care very little if I am judged by you or by any human court; indeed, I do not even judge myself.",
      "T": "Frankly, it matters very little to me whether you or any human tribunal passes judgment on me. I don't even pass judgment on myself."
    },
    "4": {
      "L": "For I am aware of nothing against myself; yet I am not by this acquitted; but the one judging me is the Lord.",
      "M": "My conscience is clear, but that does not make me innocent. It is the Lord who judges me.",
      "T": "My conscience is clear—but that doesn't settle the matter. The Lord is the one who evaluates me, and his judgment is the only one that counts."
    },
    "5": {
      "L": "Therefore judge nothing before the time, until the Lord comes, who will bring to light the things hidden in the darkness and reveal the counsels of hearts; and then each will receive his praise from God.",
      "M": "Therefore judge nothing before the appointed time; wait until the Lord comes. He will bring to light what is hidden in darkness and will expose the motives of the heart. At that time each person will receive their praise from God.",
      "T": "So stop judging before the right time comes. Wait for the Lord to appear. He will drag into the light what is now hidden in the dark, and he will lay bare every hidden motive of every heart. Then—and only then—will God give each person the recognition they truly deserve."
    },
    "6": {
      "L": "Now these things, brothers, I have applied figuratively to myself and Apollos for your sake, that in us you may learn not to go beyond what is written, so that no one of you will be puffed up in favor of one against the other.",
      "M": "Now, brothers and sisters, I have applied these things to myself and Apollos for your benefit, so that you may learn from us the meaning of 'Do not go beyond what is written.' Then you will not be puffed up in being a follower of one of us over against the other.",
      "T": "Brothers and sisters, I have used Apollos and myself as illustrations for your sake. Through us I want you to learn what 'Do not go beyond what is written' means—so that none of you will take sides, boasting about one leader over another."
    },
    "7": {
      "L": "For who makes you to differ? And what do you have that you did not receive? But if you did receive it, why do you boast as though you did not receive it?",
      "M": "For who makes you different from anyone else? What do you have that you did not receive? And if you did receive it, why do you boast as though you did not?",
      "T": "Who gave you any special standing above anyone else? Everything you have was given to you as a gift. If that is true, why are you boasting as though you earned it yourself?"
    },
    "8": {
      "L": "Already you are filled; already you have become rich; you have begun to reign without us—and would that you did reign, so that we also might reign with you!",
      "M": "Already you have all you want! Already you have become rich! You have begun to reign—and that without us! How I wish that you really had begun to reign so that we also might reign with you!",
      "T": "You think you have it all already! You think you are already rich! You act as though the kingdom has arrived and you are already reigning—without us! I wish you really were reigning, so we could reign alongside you!"
    },
    "9": {
      "L": "For I think that God has displayed us apostles last of all, as men sentenced to death; because we have become a spectacle to the world—both to angels and to men.",
      "M": "For it seems to me that God has put us apostles on display at the end of the procession, like those condemned to die in the arena. We have been made a spectacle to the whole universe, to angels as well as to human beings.",
      "T": "I sometimes think God has placed us apostles at the very end of the line—like prisoners of war paraded before the crowd just before they are executed. We have become a public spectacle before the entire universe: angels and humans alike are watching."
    },
    "10": {
      "L": "We are fools for Christ's sake, but you are wise in Christ; we are weak, but you are strong; you are honored, but we are dishonored.",
      "M": "We are fools for Christ, but you are so wise in Christ! We are weak, but you are strong! You are honored, we are dishonored!",
      "T": "We are fools for the sake of Christ—but you are so wise in Christ! We are weak—but you are strong! You are held in honor—but we are looked down on!"
    },
    "11": {
      "L": "To this present hour we both hunger and thirst, and we are poorly clothed and beaten and homeless.",
      "M": "To this very hour we go hungry and thirsty, we are in rags, we are brutally treated, we are homeless.",
      "T": "Right up to this very hour we are hungry and thirsty. We wear rags. We are beaten. We have no place to call home."
    },
    "12": {
      "L": "and we labor, working with our own hands; when reviled, we bless; when persecuted, we endure;",
      "M": "We work hard with our own hands. When we are cursed, we bless; when we are persecuted, we endure it;",
      "T": "We work hard with our own hands. When people curse us, we bless them. When they hunt us down, we keep going."
    },
    "13": {
      "L": "when slandered, we respond gently; we have become as the scum of the world—the off-scouring of all things—until now.",
      "M": "when we are slandered, we answer kindly. We have become the scum of the earth, the garbage of the world—right up to this moment.",
      "T": "When people slander us, we speak kindly in return. We have become the world's filth—the dregs scraped off the bottom—and we are still treated that way."
    },
    "14": {
      "L": "I do not write these things to shame you, but to admonish you as my beloved children.",
      "M": "I am not writing this to shame you, but to warn you as my dear children.",
      "T": "I'm not writing all this to make you feel ashamed. I'm writing it because I love you, as a father urges his own children."
    },
    "15": {
      "L": "For though you have ten thousand guardians in Christ, you do not have many fathers; for in Christ Jesus I became your father through the gospel.",
      "M": "Even if you had ten thousand guardians in Christ, you do not have many fathers, for in Christ Jesus I became your father through the gospel.",
      "T": "You might have ten thousand instructors in Christ, but you don't have many fathers. I am your father—I brought you to life in Christ Jesus through the gospel."
    },
    "16": {
      "L": "I exhort you, therefore, be imitators of me.",
      "M": "Therefore I urge you to imitate me.",
      "T": "So I urge you: follow my example."
    },
    "17": {
      "L": "For this reason I have sent to you Timothy, who is my beloved and faithful child in the Lord, and he will remind you of my ways which are in Christ Jesus, as I teach everywhere in every church.",
      "M": "For this reason I have sent to you Timothy, my son whom I love, who is faithful in the Lord. He will remind you of my way of life in Christ Jesus, which agrees with what I teach everywhere in every church.",
      "T": "That is why I am sending Timothy to you. He is my beloved and trustworthy son in the Lord. He will remind you how I conduct myself in Christ Jesus—which is exactly what I teach in all the churches everywhere."
    },
    "18": {
      "L": "Now some have become arrogant, as though I were not coming to you.",
      "M": "Some of you have become arrogant, as if I were not coming to you.",
      "T": "Some of you have grown arrogant, thinking I would never actually come to deal with it."
    },
    "19": {
      "L": "But I will come to you soon, if the Lord wills, and I will know not the speech of those who are arrogant, but their power.",
      "M": "But I will come to you very soon, if the Lord is willing, and then I will find out not only how these arrogant people are talking, but what power they have.",
      "T": "I will come to you soon—if the Lord allows. Then I will see for myself: not what these proud people are saying, but whether there is any real power behind it."
    },
    "20": {
      "L": "For the kingdom of God does not consist in speech but in power.",
      "M": "For the kingdom of God is not a matter of talk but of power.",
      "T": "God's kingdom is not about impressive words—it is about real power."
    },
    "21": {
      "L": "What do you wish? Shall I come to you with a rod, or with love and a spirit of gentleness?",
      "M": "What do you prefer? Shall I come to you with a rod of discipline, or shall I come in love and with a gentle spirit?",
      "T": "What will it be? Do you want me to come with a stick in hand, or do you want me to come to you in love and with a gentle spirit? The choice is yours."
    }
  },
  "5": {
    "1": {
      "L": "It is actually reported that there is fornication among you—and fornication of a kind not found even among the Gentiles—that a man has his father's wife.",
      "M": "It is actually reported that there is sexual immorality among you, and of a kind that even pagans do not tolerate: a man is living with his father's wife.",
      "T": "The word is out that there is sexual immorality in your community—of a kind that shocks even the pagan world. A man is actually living with his stepmother."
    },
    "2": {
      "L": "And you are arrogant! Ought you not rather to have mourned? Let the one who has done this be removed from among you.",
      "M": "And you are proud! Shouldn't you rather have gone into mourning and have put out of your fellowship the man who has been doing this?",
      "T": "And you are proud of yourselves! You should be in mourning instead—and you should remove from your fellowship the man who did this."
    },
    "3": {
      "L": "For I, though absent in body but present in spirit, have already judged the one who has done this, as though I were present.",
      "M": "For my part, even though I am not physically present, I am with you in spirit. As one who is present with you in this way, I have already passed judgment on the one who has been doing this.",
      "T": "Even though I am not there with you in body, I am there in spirit—and I have already rendered my verdict on this man, as if I were standing there in person."
    },
    "4": {
      "L": "in the name of our Lord Jesus, when you are assembled, and my spirit is with you, with the power of our Lord Jesus—",
      "M": "So when you are assembled in the name of our Lord Jesus and I am with you in spirit, and the power of our Lord Jesus is present,",
      "T": "When you gather in the name of our Lord Jesus, and my spirit is there with you, and the power of our Lord Jesus is at work—"
    },
    "5": {
      "L": "to deliver such a one to Satan for the destruction of the flesh, so that his spirit may be saved in the day of the Lord Jesus.",
      "M": "hand this man over to Satan for the destruction of the sinful nature, so that his spirit may be saved on the day of the Lord Jesus.",
      "T": "hand this man over to Satan. The aim is the destruction of his sinful flesh, so that on the day of the Lord Jesus his spirit will be saved."
    },
    "6": {
      "L": "Your boasting is not good. Do you not know that a little leaven leavens the whole lump?",
      "M": "Your boasting is not good. Don't you know that a little yeast works through the whole batch of dough?",
      "T": "There is nothing good about your boasting here. Don't you know that a small amount of yeast spreads through the whole batch of dough?"
    },
    "7": {
      "L": "Cleanse out the old leaven so that you may be a new lump, just as you are in fact unleavened. For Christ our Passover has been sacrificed.",
      "M": "Get rid of the old yeast, so that you may be a new unleavened batch—as you really are. For Christ, our Passover lamb, has been sacrificed.",
      "T": "Clear out the old yeast, so you can be the fresh, unleavened community you truly are. Christ, our Passover lamb, has already been slaughtered."
    },
    "8": {
      "L": "Therefore let us celebrate the feast, not with old leaven, nor with the leaven of malice and wickedness, but with the unleavened bread of sincerity and truth.",
      "M": "Therefore let us keep the Festival, not with the old bread leavened with malice and wickedness, but with the unleavened bread of sincerity and truth.",
      "T": "So let us celebrate the festival—but not with the old yeast of malice and evil. Let us celebrate with the unleavened bread of sincerity and truth."
    },
    "9": {
      "L": "I wrote to you in my letter not to associate with fornicators—",
      "M": "I wrote to you in my letter not to associate with sexually immoral people—",
      "T": "In an earlier letter I told you not to associate with sexually immoral people—"
    },
    "10": {
      "L": "not at all meaning the fornicators of this world, or the covetous and swindlers, or idolaters, since then you would have to go out of the world.",
      "M": "not at all meaning the people of this world who are immoral, or the greedy and swindlers, or idolaters. In that case you would have to leave this world.",
      "T": "I did not mean the immoral people of the wider world, or greedy people, or swindlers, or idol worshipers—because then you would have to leave the world altogether."
    },
    "11": {
      "L": "But now I am writing to you not to associate with anyone who bears the name of brother if he is a fornicator or covetous or an idolater or a reviler or a drunkard or a swindler—not even to eat with such a one.",
      "M": "But now I am writing to you that you must not associate with anyone who claims to be a brother or sister but is sexually immoral or greedy, an idolater or slanderer, a drunkard or swindler. Do not even eat with such people.",
      "T": "What I mean is this: do not associate with anyone who claims to be a fellow believer but is sexually immoral, greedy, an idol worshiper, an abusive talker, a drunk, or a swindler. Don't even sit down to eat with such a person."
    },
    "12": {
      "L": "For what have I to do with judging those outside? Is it not those inside whom you judge?",
      "M": "What business is it of mine to judge those outside the church? Are you not to judge those inside?",
      "T": "It is not my business to judge those outside your community. You are responsible for judging those inside it."
    },
    "13": {
      "L": "But God judges those outside. Remove the wicked person from among you.",
      "M": "God will judge those outside. 'Expel the wicked person from among you.'",
      "T": "God will deal with outsiders. Your task is clear: remove the wicked person from your midst."
    }
  },
  "6": {
    "1": {
      "L": "Does any one of you, having a matter against another, dare to go to law before the unrighteous and not before the saints?",
      "M": "If any of you has a dispute with another, do you dare to take it before the ungodly for judgment instead of before the Lord's people?",
      "T": "When one of you has a complaint against another believer, do you actually dare to bring it before a pagan court rather than before God's people?"
    },
    "2": {
      "L": "Or do you not know that the saints will judge the world? And if the world is judged by you, are you not worthy to judge the smallest matters?",
      "M": "Or do you not know that the Lord's people will judge the world? And if you are to judge the world, are you not competent to judge trivial cases?",
      "T": "Don't you know that God's people will one day judge the world? If the world comes under your judgment, surely you are capable of settling minor disputes among yourselves."
    },
    "3": {
      "L": "Do you not know that we will judge angels? How much more, then, matters pertaining to this life!",
      "M": "Do you not know that we will judge angels? How much more the things of this life!",
      "T": "Don't you know that we will one day judge angels? If that is true, how much more can we handle ordinary everyday disputes!"
    },
    "4": {
      "L": "So if you have judgments concerning things of this life, do you appoint as judges those who have no standing in the church?",
      "M": "Therefore, if you have disputes about such matters, do you ask for a ruling from those whose way of life is scorned in the church?",
      "T": "So when you have disputes about this-world matters, why are you placing them before judges who carry no weight in the church?"
    },
    "5": {
      "L": "I say this to your shame. Is it so that there is not among you one wise man who will be able to decide between his brothers?",
      "M": "I say this to shame you. Is it possible that there is nobody among you wise enough to judge a dispute between believers?",
      "T": "I say this to shame you. Can it really be true that there is not a single person among you wise enough to settle a dispute between fellow believers?"
    },
    "6": {
      "L": "but brother goes to law against brother, and that before unbelievers?",
      "M": "Instead, one brother takes another to court—and this in front of unbelievers!",
      "T": "Instead, believers are dragging other believers into court before people who don't even believe in God."
    },
    "7": {
      "L": "To have lawsuits at all with one another is already a defeat for you. Why not rather suffer wrong? Why not rather be defrauded?",
      "M": "The very fact that you have lawsuits among you means you have been completely defeated already. Why not rather be wronged? Why not rather be cheated?",
      "T": "The fact that you have lawsuits against one another at all is already your defeat. Why not accept the injustice? Why not let yourselves be cheated?"
    },
    "8": {
      "L": "But you yourselves wrong and defraud—and this even your brothers.",
      "M": "Instead, you yourselves cheat and do wrong, and you do this to your brothers and sisters.",
      "T": "But instead you are the ones doing wrong and cheating—and doing it to your own brothers and sisters."
    },
    "9": {
      "L": "Or do you not know that the unrighteous will not inherit the kingdom of God? Do not be deceived: neither the fornicators, nor idolaters, nor adulterers, nor the passive in same-sex acts, nor males who bed males,",
      "M": "Or do you not know that the unrighteous will not inherit the kingdom of God? Do not be deceived: neither the sexually immoral, nor idolaters, nor adulterers, nor those who take the passive role in same-sex acts, nor those who take the active role,",
      "T": "Don't you know that the unrighteous will have no share in God's kingdom? Don't be deceived about this: the sexually immoral, idol worshipers, adulterers, and those who engage in same-sex intercourse—whether as the passive or the active partner—"
    },
    "10": {
      "L": "nor thieves, nor the covetous, nor drunkards, nor revilers, nor swindlers will inherit the kingdom of God.",
      "M": "nor thieves, nor the greedy, nor drunkards, nor slanderers, nor swindlers will inherit the kingdom of God.",
      "T": "nor thieves, the greedy, drunkards, abusive people, or swindlers—none of them will inherit God's kingdom."
    },
    "11": {
      "L": "And such were some of you. But you were washed, you were sanctified, you were justified in the name of the Lord Jesus Christ and by the Spirit of our God.",
      "M": "And that is what some of you were. But you were washed, you were sanctified, you were justified in the name of the Lord Jesus Christ and by the Spirit of our God.",
      "T": "And some of you were exactly like that. But you were washed clean. You were set apart as holy. You were declared righteous—all in the name of the Lord Jesus Christ and by the Spirit of our God."
    },
    "12": {
      "L": "'All things are lawful for me,' but not all things are beneficial. 'All things are lawful for me,' but I will not be dominated by anything.",
      "M": "'I have the right to do anything,' you say—but not everything is beneficial. 'I have the right to do anything'—but I will not be mastered by anything.",
      "T": "You say, 'I am free to do anything.' Yes—but not everything is good for you. You say, 'I am free to do anything.' Yes—but I refuse to let anything become my master."
    },
    "13": {
      "L": "'Food is for the stomach and the stomach for food'—but God will destroy both. The body is not for fornication but for the Lord, and the Lord for the body.",
      "M": "'Food for the stomach and the stomach for food'—but God will bring them both to an end. The body is not meant for sexual immorality but for the Lord, and the Lord for the body.",
      "T": "You say, 'Food is made for the stomach and the stomach for food.' Perhaps—but God will one day bring both to nothing. What matters is this: your body was not made for sexual immorality. It was made for the Lord, and the Lord cares deeply about your body."
    },
    "14": {
      "L": "And God both raised the Lord and will raise us up by his power.",
      "M": "By his power God raised the Lord from the dead, and he will raise us also.",
      "T": "God raised the Lord from the dead—and he will raise us too by that same power."
    },
    "15": {
      "L": "Do you not know that your bodies are members of Christ? Shall I then take the members of Christ and make them members of a prostitute? Never!",
      "M": "Do you not know that your bodies are members of Christ himself? Shall I then take the members of Christ and unite them with a prostitute? Never!",
      "T": "Don't you know that your bodies are actually parts of Christ himself? Should I then take what belongs to Christ and join it to a prostitute? God forbid!"
    },
    "16": {
      "L": "Or do you not know that he who is joined to a prostitute is one body with her? For, as it is written, 'The two will become one flesh.'",
      "M": "Do you not know that he who unites himself with a prostitute is one with her in body? For it is said, 'The two will become one flesh.'",
      "T": "Don't you know that when a man joins himself to a prostitute he becomes physically one with her? Scripture says, 'The two shall become one flesh.'"
    },
    "17": {
      "L": "But he who is joined to the Lord is one spirit with him.",
      "M": "But whoever is united with the Lord is one with him in spirit.",
      "T": "But the one who is joined to the Lord becomes one spirit with him."
    },
    "18": {
      "L": "Flee fornication. Every sin that a man commits is outside the body, but the one who fornicates sins against his own body.",
      "M": "Flee from sexual immorality. All other sins a person commits are outside the body, but whoever sins sexually, sins against their own body.",
      "T": "Run from sexual immorality. Every other sin a person commits is external to the body—but sexual immorality is a sin against your own body."
    },
    "19": {
      "L": "Or do you not know that your body is a temple of the Holy Spirit within you, whom you have from God, and you are not your own?",
      "M": "Do you not know that your bodies are temples of the Holy Spirit, who is in you, whom you have received from God? You are not your own;",
      "T": "Don't you know that your body is a temple where the Holy Spirit lives—the Spirit you received from God? You do not belong to yourself."
    },
    "20": {
      "L": "for you were bought with a price. Therefore glorify God in your body.",
      "M": "you were bought at a price. Therefore honor God with your bodies.",
      "T": "You were purchased at a price. So use your body to bring glory to God."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '1corinthians')
        merge_tier(existing, CORINTHIANS_1, tier_key)
        save(tier_dir, '1corinthians', existing)
    print('1 Corinthians 4–6 written.')

if __name__ == '__main__':
    main()
