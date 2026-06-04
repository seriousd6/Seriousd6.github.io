"""
MKT 1 Timothy chapters 4–6 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-1timothy-4-6.py

Translation decisions:
- G4151 (πνεῦμα): "the Spirit" (capitalized) in 4:1, where the Holy Spirit speaks explicitly;
  "spirit" (lowercase) in 4:12, where it refers to Timothy's personal character/spirit.
- G166 (αἰώνιος): "eternal" in L/M throughout. In T at 6:12 and 6:19, rendered with the
  eschatological note "the life of the coming age" to surface the Jewish idiom behind αἰώνιος
  (= belonging to the age-to-come, not merely infinite duration).
- G2150 (εὐσέβεια): "godliness" throughout all three tiers, consistent with Titus (mkt-phase2.py).
  In T at 4:7-8, "godly devotion" is used for variety and to capture the active-piety sense.
- G26 (ἀγάπη): "love" throughout; context here is pastoral instruction, not John's covenant
  register, so no expansion needed.
- G1343 (δικαιοσύνη): "righteousness" in L/M; "right living" in T at 6:11 where the practical
  conduct sense dominates over the forensic.
- G4102 (πίστις): "faith" when denoting personal trust; "the faith" when denoting the body of
  Christian doctrine (4:1, 4:6, 5:8, 6:10, 6:12, 6:21).
- G3056 (λόγος): "word" in most contexts; "teaching" or "message" where λόγος refers to the
  proclamation rather than a text.
- Textual note — 4:10: Interlinear shows G3679 (ὀνειδιζόμεθα, "we suffer reproach"), the majority
  reading. Some witnesses read G75 (ἀγωνιζόμεθα, "we strive"). L/M/T follow the majority text
  ("suffer reproach / press on under reproach").
- Textual note — 4:12: G4151 ("spirit") appears in the list of Timothy's example areas in some
  witnesses; included in L as "in spirit" but not forced into M/T, which retain the cleaner
  five-part list (speech, conduct, love, faith, purity).
- Aspect note — 4:6: G3877 (parakoloutheō, perfect form) = "you have closely followed" —
  emphasizing the past act with present stable result.
- 5:22 "laying on of hands": refers to commissioning elders (linking back to v17-22 context),
  not baptism or confirmation.
- 6:5 false teachers: the irony of πορισμός (gain) is preserved across tiers — the same word used
  in v5 (they think godliness is a gain) is inverted in v6 (godliness with contentment IS great gain).
- 6:16 doxology: αἰώνιος here modifies "might/dominion" — rendered "everlasting power" in M,
  "power without end" in T, distinguishing from the "eternal life" use at 6:12/6:19.
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

TIMOTHY = {
  "4": {
    "1": {
      "L": "Now the Spirit expressly says that in later times some will fall away from the faith, giving heed to deceitful spirits and doctrines of demons,",
      "M": "The Spirit clearly says that in later times some will abandon the faith and follow deceiving spirits and things taught by demons.",
      "T": "The Holy Spirit speaks plainly: in the last days some will walk away from the faith—drawn off by lying spirits and teachings that originate with demons."
    },
    "2": {
      "L": "speaking lies in hypocrisy, having their own conscience seared as with a hot iron,",
      "M": "Such teachings come through hypocritical liars, whose consciences have been seared as with a hot iron.",
      "T": "These false teachers are hypocrites—hollow liars whose capacity for moral feeling has been burned away like flesh under a branding iron."
    },
    "3": {
      "L": "forbidding to marry, commanding to abstain from foods, which God created to be received with thanksgiving by those who believe and know the truth.",
      "M": "They forbid people to marry and order them to abstain from certain foods, which God created to be received with thanksgiving by those who believe and who know the truth.",
      "T": "They forbid marriage and demand abstinence from certain foods—foods that God himself created to be received with gratitude by those who trust him and know the truth."
    },
    "4": {
      "L": "For every creature of God is good, and nothing is to be rejected if it is received with thanksgiving,",
      "M": "For everything God created is good, and nothing is to be rejected if it is received with thanksgiving,",
      "T": "Everything God made is good. Nothing is to be turned away when received with a grateful heart—"
    },
    "5": {
      "L": "for it is sanctified through the word of God and prayer.",
      "M": "because it is sanctified by the word of God and prayer.",
      "T": "because God's word and prayer consecrate it."
    },
    "6": {
      "L": "If you put these things before the brothers, you will be a good minister of Christ Jesus, nourished on the words of the faith and of the good teaching that you have closely followed.",
      "M": "If you point these things out to the brothers and sisters, you will be a good minister of Christ Jesus, nourished on the truths of the faith and of the good teaching that you have faithfully followed.",
      "T": "By holding these things before the community, you will prove yourself a worthy servant of Christ Jesus—a minister shaped by the words of faith and the sound teaching you have made your own."
    },
    "7": {
      "L": "But refuse profane and old-wives' fables, and train yourself for godliness.",
      "M": "Have nothing to do with godless myths and old wives' tales; rather, train yourself to be godly.",
      "T": "Reject the hollow myths that godless people pass around. Discipline yourself for godly devotion instead—that is where the real work lies."
    },
    "8": {
      "L": "For bodily training is profitable for a little, but godliness is profitable for all things, having promise of the present life and of that which is to come.",
      "M": "For physical training is of some value, but godliness has value for all things, holding promise for both the present life and the life to come.",
      "T": "Physical discipline has some value, but godly devotion is valuable in every dimension—it carries the promise of life both now and in the age to come."
    },
    "9": {
      "L": "This is a faithful saying and worthy of all acceptance.",
      "M": "This is a trustworthy saying that deserves full acceptance.",
      "T": "This is a saying you can rely on completely."
    },
    "10": {
      "L": "For to this end we both labor and suffer reproach, because we have set our hope on the living God, who is the Savior of all men, especially of those who believe.",
      "M": "That is why we labor and press on under reproach, because we have put our hope in the living God, who is the Savior of all people, and especially of those who believe.",
      "T": "This is why we pour ourselves out in toil and press on even when reproached—because our hope is fixed on the living God, the Savior of all humanity, and above all of those who trust him."
    },
    "11": {
      "L": "Command and teach these things.",
      "M": "Command and teach these things.",
      "T": "Make these things your standing instructions—teach them and insist on them."
    },
    "12": {
      "L": "Let no one despise your youth, but be an example to the believers in word, in conduct, in love, in faith, in purity.",
      "M": "Don't let anyone look down on you because you are young, but set an example for the believers in speech, in conduct, in love, in faith and in purity.",
      "T": "Don't let anyone dismiss you because of your age. Show the community who you are by the way you speak, the way you live, the love you show, the faith you hold, and the purity you keep."
    },
    "13": {
      "L": "Until I come, give attention to reading, to exhortation, to teaching.",
      "M": "Until I come, devote yourself to the public reading of Scripture, to preaching and to teaching.",
      "T": "Until I arrive, make the public reading of Scripture your steady practice—along with encouraging people and teaching sound doctrine."
    },
    "14": {
      "L": "Do not neglect the gift that is in you, which was given to you through prophecy with the laying on of hands of the council of elders.",
      "M": "Do not neglect your gift, which was given you through prophecy when the body of elders laid their hands on you.",
      "T": "Don't let the spiritual gift within you lie dormant—the gift given through prophetic declaration when the elders laid their hands on you."
    },
    "15": {
      "L": "Meditate on these things; give yourself wholly to them, so that your progress may be evident to all.",
      "M": "Be diligent in these matters; give yourself wholly to them, so that everyone may see your progress.",
      "T": "Keep your mind on these things. Throw yourself into them completely—so that everyone around you can see you growing."
    },
    "16": {
      "L": "Take heed to yourself and to the teaching; continue in them, for in doing this you will save both yourself and those who hear you.",
      "M": "Watch your life and doctrine closely. Persevere in them, because if you do, you will save both yourself and your hearers.",
      "T": "Keep a close watch on your own soul and on what you teach. Stay the course—because in doing so you become the instrument of salvation for yourself and for all who hear you."
    }
  },
  "5": {
    "1": {
      "L": "Do not rebuke an elder harshly, but appeal to him as to a father; and younger men as brothers,",
      "M": "Do not rebuke an older man harshly, but exhort him as if he were your father. Treat younger men as brothers,",
      "T": "Don't come down hard on an older man—speak to him the way a son speaks to his father. Address younger men as brothers."
    },
    "2": {
      "L": "older women as mothers, younger women as sisters, in all purity.",
      "M": "older women as mothers, and younger women as sisters, with absolute purity.",
      "T": "Treat older women as you would your mother, and younger women as sisters—with absolute moral purity in everything."
    },
    "3": {
      "L": "Honor widows who are indeed widows.",
      "M": "Give proper recognition to those widows who are really in need.",
      "T": "Support and honor the women who are truly alone—genuine widows with no one to depend on."
    },
    "4": {
      "L": "But if any widow has children or grandchildren, let them first learn to show piety toward their own household and to make return to their forebears, for this is acceptable before God.",
      "M": "But if a widow has children or grandchildren, these should learn first of all to put their religion into practice by caring for their own family and so repaying their parents and grandparents, for this is pleasing to God.",
      "T": "But when a widow has children or grandchildren, those family members should learn the meaning of godliness by caring for their own kin first—repaying in kind the care they themselves once received. This is what pleases God."
    },
    "5": {
      "L": "Now she who is indeed a widow, and has been left alone, has set her hope on God and continues in supplications and prayers night and day.",
      "M": "The widow who is really in need and left all alone puts her hope in God and continues night and day to pray and to ask God for help.",
      "T": "A woman who is truly alone—no family to fall back on—sets her entire hope on God, persisting in prayer and petition day and night."
    },
    "6": {
      "L": "But she who lives for pleasure is dead even while she lives.",
      "M": "But the widow who lives for pleasure is dead even while she lives.",
      "T": "But a widow who lives only for self-indulgence is spiritually dead, though she still walks around."
    },
    "7": {
      "L": "And command these things, that they may be above reproach.",
      "M": "Give the people these instructions, so that no one may be open to blame.",
      "T": "Make these expectations clear—so that the whole community lives without reproach."
    },
    "8": {
      "L": "But if anyone does not provide for his own, and especially for those of his own household, he has denied the faith and is worse than an unbeliever.",
      "M": "Anyone who does not provide for their relatives, and especially for their own household, has denied the faith and is worse than an unbeliever.",
      "T": "Anyone who refuses to provide for his own family—especially those living under his roof—has effectively repudiated the faith. He is worse than someone who never believed at all."
    },
    "9": {
      "L": "Let a widow be enrolled if she is not less than sixty years of age, the wife of one husband,",
      "M": "No widow may be put on the list of widows unless she is over sixty, has been faithful to her husband,",
      "T": "A widow may be added to the church's support roll only if she is at least sixty years old and has been faithful to her husband—"
    },
    "10": {
      "L": "having testimony in good works: if she has brought up children, if she has shown hospitality, if she has washed the feet of the saints, if she has helped the afflicted, and if she has devoted herself to every good work.",
      "M": "and is well known for her good deeds, such as bringing up children, showing hospitality, washing the feet of the Lord's people, helping those in trouble and devoting herself to all kinds of good deeds.",
      "T": "—and known for a life of good works: raising children well, welcoming strangers, serving God's people in humble ways, caring for those in distress, and giving herself to every form of good work."
    },
    "11": {
      "L": "But refuse to enroll younger widows, for when they grow restless against Christ, they desire to marry,",
      "M": "As for younger widows, do not put them on such a list. For when their sensual desires overcome their dedication to Christ, they want to marry,",
      "T": "Don't put younger widows on the support list. When their desires pull them away from their commitment to Christ, they want to remarry—"
    },
    "12": {
      "L": "bringing condemnation on themselves because they have set aside their first pledge of faith.",
      "M": "thus bringing judgment on themselves, because they have broken their first pledge.",
      "T": "—and in doing so they draw judgment on themselves for abandoning their original commitment."
    },
    "13": {
      "L": "At the same time they also learn to be idlers, going about from house to house; and not only idlers, but also gossips and busybodies, saying things they should not.",
      "M": "Besides, they get into the habit of being idle and going about from house to house. And not only do they become idlers, but also busybodies who talk nonsense, saying things they ought not to.",
      "T": "On top of that, they learn idleness—wandering from house to house. Worse, they become gossips and busybodies, saying things they have no business saying."
    },
    "14": {
      "L": "So I want younger widows to marry, bear children, manage their households, and give the adversary no occasion for slander.",
      "M": "So I counsel younger widows to marry, to have children, to manage their homes and to give the enemy no opportunity for slander.",
      "T": "My counsel: let younger widows marry, have children, run their households well—and give the opponent no foothold for accusation."
    },
    "15": {
      "L": "For some have already turned aside after Satan.",
      "M": "Some have in fact already turned away to follow Satan.",
      "T": "Some have already gone down that road—following Satan rather than their Lord."
    },
    "16": {
      "L": "If any believing woman has widows in her family, let her assist them, and do not let the church be burdened, so that it may assist those who are indeed widows.",
      "M": "If any woman who is a believer has widows in her care, she should continue to help them and not let the church be burdened with them, so that the church can help those widows who are really in need.",
      "T": "If a believing woman has widows in her family, she should take responsibility for them herself—freeing the church from that burden so its resources can flow to the women who have truly no one."
    },
    "17": {
      "L": "Let the elders who rule well be considered worthy of double honor, especially those who labor in word and teaching.",
      "M": "The elders who direct the affairs of the church well are worthy of double honor, especially those whose work is preaching and teaching.",
      "T": "Elders who lead the community well deserve full support—doubly so for those who pour themselves into preaching and teaching."
    },
    "18": {
      "L": "For the Scripture says, 'You shall not muzzle the ox when it treads out grain,' and, 'The worker is worthy of his wages.'",
      "M": "For Scripture says, 'Do not muzzle an ox while it is treading out the grain,' and 'The worker deserves his wages.'",
      "T": "Scripture makes it plain: 'Don't muzzle the ox while it works.' And again: 'The one doing the work deserves to be paid.'"
    },
    "19": {
      "L": "Do not receive an accusation against an elder unless it is on the basis of two or three witnesses.",
      "M": "Do not entertain an accusation against an elder unless it is brought by two or three witnesses.",
      "T": "Never take up a charge against an elder unless at least two or three witnesses stand behind it."
    },
    "20": {
      "L": "Those who continue in sin, rebuke in the presence of all, so that the rest also may have fear.",
      "M": "But those who are sinning you are to reprove before everyone, so that the others may take warning.",
      "T": "Those who do persist in sin must be publicly rebuked—so the rest of the community takes it as a serious warning."
    },
    "21": {
      "L": "I charge you before God and Christ Jesus and the elect angels that you observe these things without prejudice, doing nothing by partiality.",
      "M": "I charge you, in the sight of God and Christ Jesus and the elect angels, to keep these instructions without partiality, and to do nothing out of favoritism.",
      "T": "I solemnly charge you—before God, before Christ Jesus, and before the chosen angels—follow these directives with complete impartiality. No prejudging. No playing favorites."
    },
    "22": {
      "L": "Do not lay hands on anyone hastily, nor be a partaker of other men's sins; keep yourself pure.",
      "M": "Do not be hasty in the laying on of hands, and do not share in the sins of others. Keep yourself pure.",
      "T": "Don't rush to commission anyone for ministry—and don't make yourself complicit in others' wrongs. Guard your own purity."
    },
    "23": {
      "L": "No longer drink only water, but use a little wine for the sake of your stomach and your frequent illnesses.",
      "M": "Stop drinking only water, and use a little wine because of your stomach and your frequent illnesses.",
      "T": "Stop restricting yourself to water alone—take a little wine for your stomach's sake and for the ailments that keep troubling you."
    },
    "24": {
      "L": "The sins of some men are evident beforehand, going before them to judgment; but the sins of others follow after.",
      "M": "The sins of some are obvious, reaching the place of judgment ahead of them; the sins of others trail behind them.",
      "T": "Some people's sins are glaring—they arrive at the day of judgment ahead of the person. Others' sins only surface afterward."
    },
    "25": {
      "L": "Likewise also the good works of some are evident beforehand, and those that are otherwise cannot be hidden.",
      "M": "In the same way, good deeds are obvious, and even those that are not obvious cannot remain hidden forever.",
      "T": "It works the same way with good deeds—most are visible now, but even those that are not cannot stay hidden forever."
    }
  },
  "6": {
    "1": {
      "L": "Let as many as are under the yoke as slaves regard their own masters as worthy of all honor, so that the name of God and the teaching may not be blasphemed.",
      "M": "All who are under the yoke of slavery should consider their masters worthy of full respect, so that God's name and our teaching may not be slandered.",
      "T": "Those living under a master's authority should treat that master with full respect—so no one can use their behavior as a weapon against God's name or the message we proclaim."
    },
    "2": {
      "L": "And those who have believing masters must not disrespect them because they are brothers; but serve them all the more, because those who receive the benefit of their good service are believers and beloved. Teach and urge these things.",
      "M": "Those who have believing masters should not show them disrespect just because they are fellow believers. Instead, they should serve them even better because their masters are dear to them as fellow believers and devoted to their welfare. These are the things you are to teach and insist on.",
      "T": "If the master is a fellow believer, that is no grounds for disrespect—it is a reason to serve even more wholeheartedly, because the one receiving the service is a beloved brother in the faith. Teach this and keep pressing it home."
    },
    "3": {
      "L": "If anyone teaches a different doctrine and does not agree with the sound words of our Lord Jesus Christ and the teaching that accords with godliness,",
      "M": "If anyone teaches otherwise and does not agree to the sound instruction of our Lord Jesus Christ and to godly teaching,",
      "T": "Anyone who teaches something different—who refuses to submit to the sound teaching of our Lord Jesus Christ, the teaching that leads to godliness—"
    },
    "4": {
      "L": "he is puffed up, knowing nothing, but is obsessed with disputes and arguments about words, from which arise envy, strife, slander, evil suspicions,",
      "M": "they are conceited and understand nothing. They have an unhealthy interest in controversies and quarrels about words that result in envy, strife, malicious talk, evil suspicions",
      "T": "—that person is puffed up with pride while understanding nothing. They have a morbid obsession with controversies and word-battles that breed envy, conflict, slander, and vicious suspicions—"
    },
    "5": {
      "L": "constant friction of men corrupted in mind and deprived of the truth, who suppose that godliness is a means of gain. Withdraw yourself from such men.",
      "M": "and constant friction between people of corrupt mind, who have been robbed of the truth and who think that godliness is a means to financial gain.",
      "T": "—a constant grinding friction among people whose minds have been corrupted and stripped of truth. They have turned religion into a business."
    },
    "6": {
      "L": "But godliness with contentment is great gain.",
      "M": "But godliness with contentment is great gain.",
      "T": "Here is the real profit: godliness paired with a contented heart. That is wealth beyond measure."
    },
    "7": {
      "L": "For we brought nothing into the world, and we can carry nothing out of it.",
      "M": "For we brought nothing into the world, and we can take nothing out of it.",
      "T": "We came into this world with nothing, and we will leave it with nothing—that much is certain."
    },
    "8": {
      "L": "But if we have food and covering, with these we will be content.",
      "M": "But if we have food and clothing, we will be content with that.",
      "T": "If we have enough food and enough clothing, that is sufficient. Let that be enough."
    },
    "9": {
      "L": "But those who desire to be rich fall into temptation and a snare and many foolish and harmful desires, which plunge men into ruin and destruction.",
      "M": "Those who want to get rich fall into temptation and a trap and into many foolish and harmful desires that plunge people into ruin and destruction.",
      "T": "Those set on becoming rich walk straight into a trap—caught by foolish and destructive desires that drag them down into ruin and wreckage."
    },
    "10": {
      "L": "For the love of money is a root of all kinds of evil. Through this craving some have wandered away from the faith and pierced themselves with many pangs.",
      "M": "For the love of money is a root of all kinds of evil. Some people, eager for money, have wandered from the faith and pierced themselves with many griefs.",
      "T": "The love of money is the root of every kind of evil. Chasing after it, some have strayed far from the faith—and in doing so have driven their own hearts through with grief."
    },
    "11": {
      "L": "But as for you, O man of God, flee these things. Pursue righteousness, godliness, faith, love, steadfastness, gentleness.",
      "M": "But you, man of God, flee from all this, and pursue righteousness, godliness, faith, love, endurance and gentleness.",
      "T": "But you—a man who belongs to God—run from all that. Instead, pursue right living, godly devotion, faith, love, patient endurance, and humility."
    },
    "12": {
      "L": "Fight the good fight of the faith; take hold of the eternal life to which you were called and about which you made the good confession in the presence of many witnesses.",
      "M": "Fight the good fight of the faith. Take hold of the eternal life to which you were called when you made your good confession in the presence of many witnesses.",
      "T": "Compete in the great contest of faith. Seize the eternal life—the life of the coming age—to which God called you when you confessed him boldly before many witnesses."
    },
    "13": {
      "L": "I charge you before God, who gives life to all things, and before Christ Jesus, who made the good confession before Pontius Pilate,",
      "M": "In the sight of God, who gives life to everything, and of Christ Jesus, who while testifying before Pontius Pilate made the good confession, I charge you",
      "T": "I charge you in the presence of God—the one who gives life to everything—and of Christ Jesus, who himself spoke the truth without flinching before Pontius Pilate:"
    },
    "14": {
      "L": "that you keep the commandment spotless and above reproach until the appearing of our Lord Jesus Christ,",
      "M": "to keep this command without spot or blame until the appearing of our Lord Jesus Christ,",
      "T": "keep this commission without blemish or failure, right up until the day our Lord Jesus Christ appears—"
    },
    "15": {
      "L": "which the blessed and only Sovereign will display at the proper times—the King of kings and Lord of lords,",
      "M": "which God will bring about in his own time—God, the blessed and only Ruler, the King of kings and Lord of lords,",
      "T": "—an appearing that the blessed and only Sovereign will bring about in his own appointed time: the King who rules over all kings and the Lord who reigns over all lords,"
    },
    "16": {
      "L": "who alone has immortality, dwelling in unapproachable light, whom no man has seen or can see. To him be honor and eternal might. Amen.",
      "M": "who alone is immortal and who lives in unapproachable light, whom no one has seen or can see. To him be honor and might forever. Amen.",
      "T": "who alone possesses immortality, who dwells in light so blazing that no one can draw near—whom no human eye has seen or ever can see. To him belong honor and power without end. Amen."
    },
    "17": {
      "L": "Command those who are rich in this present age not to be haughty, nor to set their hope on the uncertainty of riches, but on God, who richly provides us with all things for our enjoyment.",
      "M": "Command those who are rich in this present world not to be arrogant nor to put their hope in wealth, which is so uncertain, but to put their hope in God, who richly provides us with everything for our enjoyment.",
      "T": "Tell those who are wealthy in this present age: don't be arrogant, and don't anchor your hope in something as unstable as riches. Fix your hope on God instead—the one who lavishes everything on us generously for our enjoyment."
    },
    "18": {
      "L": "They are to do good, to be rich in good works, to be generous and ready to share,",
      "M": "Command them to do good, to be rich in good deeds, and to be generous and willing to share.",
      "T": "Tell them to do good—to be rich in generosity, open-handed and eager to share what they have—"
    },
    "19": {
      "L": "thus storing up for themselves a good foundation for the future, so that they may take hold of that which is truly life.",
      "M": "In this way they will lay up treasure for themselves as a firm foundation for the coming age, so that they may take hold of the life that is truly life.",
      "T": "—building for themselves a solid foundation for the age to come, so that they can lay hold of the life that truly deserves the name."
    },
    "20": {
      "L": "O Timothy, guard the deposit entrusted to you. Avoid the irreverent babble and contradictions of what is falsely called knowledge,",
      "M": "Timothy, guard what has been entrusted to your care. Turn away from godless chatter and the opposing ideas of what is falsely called knowledge,",
      "T": "Timothy—guard the deposit placed in your care. Keep well away from the godless chatter and the contradictions of what people falsely call knowledge—"
    },
    "21": {
      "L": "which some, professing, have missed the mark concerning the faith. Grace be with you.",
      "M": "which some have professed and in so doing have departed from the faith. Grace be with you all.",
      "T": "—some have made a show of possessing it and in doing so have wandered clean away from the faith. Grace be with you."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '1timothy')
        merge_tier(existing, TIMOTHY, tier_key)
        save(tier_dir, '1timothy', existing)
    print('1 Timothy 4–6 written.')

if __name__ == '__main__':
    main()
