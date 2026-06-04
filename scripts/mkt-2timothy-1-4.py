"""
MKT 2 Timothy chapters 1–4 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-2timothy-1-4.py

Translation decisions:
- G4151 (πνεῦμα): "Spirit" (capitalised, divine gift) in 1:7 and 1:14; "spirit" (lower case, human faculty) in 4:22 — context determines each; consistent with Titus/2 Thess conventions.
- G26 (ἀγάπη): "love" in all tiers — covenantal, self-giving love; distinguished from φιλία where relevant.
- G4102 (πίστις): "faith" / "the faith" — context determines whether personal trust or body of doctrine; documented per verse.
- G3056 (λόγος): "word" / "the word" — the proclaimed message, not the Johannine Logos here; 2:15 uses "the word of truth."
- G166 (αἰώνιος): "eternal" throughout — quality of age-to-come life; noted in 2:10 context.
- G1343 (δικαιοσύνη): "righteousness" — both moral character and right standing; context distinguishes; 4:8 "crown of righteousness" = eschatological reward.
- H3068 / κύριος (G2962): "Lord" throughout for κύριος applied to Jesus; standard convention matching Titus/phase2 scripts.
- G4991 (σωτηρία): "salvation" — holistic deliverance, not merely forensic.
- G2315 (θεόπνευστος): "God-breathed" in L; "breathed out by God" in M; "the very breath of God" in T — this hapax legomenon is crucial in 3:16 and must not be flattened to "inspired."
- Aspect: perfect tenses rendered with past-act / present-result sense (e.g. 4:7 "I have fought ... I have finished ... I have kept").
- OT echo: 2:19 "the Lord knows those who are his" echoes Num 16:5 (Korah rebellion); noted in T tier.
- Textual note: 4:22 subscription ("written from Rome ... when Paul was brought before Nero") is a later scribal addition present in some MSS; included as v.22 following KJV interlinear but marked interpretively in T.
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

TWOTIMOTHY = {
  "1": {
    "1": {
      "L": "Paul, an apostle of Christ Jesus by the will of God, according to the promise of life that is in Christ Jesus,",
      "M": "Paul, an apostle of Christ Jesus by the will of God, in keeping with the promise of life that is in Christ Jesus,",
      "T": "I, Paul, am an apostle of Christ Jesus—appointed by God's own will—sent to proclaim the life that is found in Christ Jesus."
    },
    "2": {
      "L": "to Timothy, my beloved child: Grace, mercy, and peace from God the Father and Christ Jesus our Lord.",
      "M": "To Timothy, my dear son: Grace, mercy and peace from God the Father and Christ Jesus our Lord.",
      "T": "To Timothy, my dear son in the faith: May God the Father and Christ Jesus our Lord give you grace, mercy, and peace."
    },
    "3": {
      "L": "I give thanks to God, whom I serve with a clear conscience as my forefathers did, as I constantly remember you in my prayers night and day,",
      "M": "I thank God, whom I serve with a clear conscience as my ancestors did, when I constantly remember you in my prayers night and day.",
      "T": "I thank God—the same God my ancestors served, whom I serve with a clean conscience—every time I remember you in my prayers, which is constantly, night and day."
    },
    "4": {
      "L": "longing to see you, remembering your tears, that I may be filled with joy,",
      "M": "Recalling your tears, I long to see you, so that I may be filled with joy.",
      "T": "I remember your tears, and I long to see you so I can be filled with joy."
    },
    "5": {
      "L": "calling to mind the sincere faith in you, which dwelt first in your grandmother Lois and your mother Eunice, and I am persuaded dwells in you also.",
      "M": "I am reminded of your sincere faith, which first lived in your grandmother Lois and in your mother Eunice, and I am persuaded now lives in you also.",
      "T": "I keep thinking about your genuine, unfeigned faith—faith that first took root in your grandmother Lois and your mother Eunice, and I am fully confident it now lives in you as well."
    },
    "6": {
      "L": "For this reason I remind you to fan into flame the gift of God, which is in you through the laying on of my hands.",
      "M": "For this reason I remind you to fan into flame the gift of God, which is in you through the laying on of my hands.",
      "T": "This is why I urge you: stir up into full flame the gift that God placed in you when I laid my hands on you."
    },
    "7": {
      "L": "For God has not given us a spirit of fear, but of power and of love and of a sound mind.",
      "M": "For the Spirit God gave us does not make us timid, but gives us power, love and self-discipline.",
      "T": "God did not give us a Spirit that makes us shrink back in fear. He gave us a Spirit of power, love, and self-control."
    },
    "8": {
      "L": "Therefore do not be ashamed of the testimony of our Lord, nor of me his prisoner, but share in suffering for the gospel according to the power of God,",
      "M": "So do not be ashamed of the testimony about our Lord or of me his prisoner. Rather, join with me in suffering for the gospel, by the power of God.",
      "T": "So do not be ashamed to bear witness to our Lord, or to stand beside me his prisoner. Join me instead in suffering for the gospel—and do it in the power God provides."
    },
    "9": {
      "L": "who saved us and called us with a holy calling, not according to our works but according to his own purpose and grace, which was given to us in Christ Jesus before eternal ages,",
      "M": "He has saved us and called us to a holy life—not because of anything we have done but because of his own purpose and grace. This grace was given us in Christ Jesus before the beginning of time,",
      "T": "This is the God who saved us and called us to a holy life—not because of our deeds, but because of his own purpose and grace. This grace was given to us in Christ Jesus before the world began,"
    },
    "10": {
      "L": "but has now been manifested through the appearing of our Savior Christ Jesus, who abolished death and brought life and immortality to light through the gospel,",
      "M": "but it has now been revealed through the appearing of our Savior, Christ Jesus, who has destroyed death and has brought life and immortality to light through the gospel.",
      "T": "and it has now burst into the open through the appearing of our Savior Christ Jesus. He has broken the power of death and flooded everything with the light of life and immortality through the gospel."
    },
    "11": {
      "L": "for which I was appointed a herald and an apostle and a teacher.",
      "M": "And of this gospel I was appointed a herald and an apostle and a teacher.",
      "T": "I was appointed to this gospel as its herald, apostle, and teacher."
    },
    "12": {
      "L": "For this reason I also suffer these things, but I am not ashamed; for I know whom I have believed, and I am persuaded that he is able to guard what has been entrusted to me until that day.",
      "M": "That is why I am suffering as I am. Yet this is no cause for shame, because I know whom I have believed, and am convinced that he is able to guard what I have entrusted to him until that day.",
      "T": "This is why I am suffering as I do—yet I am not ashamed. I know exactly whom I have trusted, and I am absolutely convinced that he is able to guard everything I have placed in his care until the last day."
    },
    "13": {
      "L": "Hold to the pattern of sound words that you heard from me, in the faith and love that are in Christ Jesus.",
      "M": "What you heard from me, keep as the pattern of sound teaching, with faith and love in Christ Jesus.",
      "T": "Hold firmly to the pattern of sound teaching you received from me—hold it in the faith and love that are yours in Christ Jesus."
    },
    "14": {
      "L": "Guard the good deposit that was entrusted to you by the Holy Spirit who dwells in us.",
      "M": "Guard the good deposit that was entrusted to you—guard it with the help of the Holy Spirit who lives in us.",
      "T": "Guard the precious deposit entrusted to you. You can do it—the Holy Spirit who dwells in us will help you."
    },
    "15": {
      "L": "You know this, that all who are in Asia have turned away from me, among whom are Phygelus and Hermogenes.",
      "M": "You know that everyone in the province of Asia has deserted me, including Phygelus and Hermogenes.",
      "T": "You know that everyone in the province of Asia has turned their back on me—Phygelus and Hermogenes among them."
    },
    "16": {
      "L": "May the Lord grant mercy to the household of Onesiphorus, for he often refreshed me and was not ashamed of my chain,",
      "M": "May the Lord show mercy to the household of Onesiphorus, because he often refreshed me and was not ashamed of my chains.",
      "T": "May the Lord show mercy to the family of Onesiphorus. He repeatedly lifted my spirits and was never embarrassed by my chains."
    },
    "17": {
      "L": "but when he was in Rome, he sought me out very diligently and found me.",
      "M": "On the contrary, when he was in Rome, he searched hard for me until he found me.",
      "T": "On the contrary, when he came to Rome, he searched for me persistently until he tracked me down."
    },
    "18": {
      "L": "May the Lord grant to him to find mercy from the Lord on that day! And how well you know all the ways he served at Ephesus.",
      "M": "May the Lord grant that he will find mercy from the Lord on that day! You know very well in how many ways he helped me in Ephesus.",
      "T": "May the Lord grant that he will find mercy from the Lord on that final day. And you know better than anyone how much he served me in Ephesus."
    }
  },
  "2": {
    "1": {
      "L": "You therefore, my son, be strengthened in the grace that is in Christ Jesus.",
      "M": "You then, my son, be strong in the grace that is in Christ Jesus.",
      "T": "So then, my son, draw your strength from the grace that is yours in Christ Jesus."
    },
    "2": {
      "L": "And what you have heard from me in the presence of many witnesses, commit to faithful men who will be able to teach others also.",
      "M": "And the things you have heard me say in the presence of many witnesses entrust to reliable people who will also be qualified to teach others.",
      "T": "What you heard from me in front of many witnesses—pass that on to trustworthy people who will, in turn, be able to teach others."
    },
    "3": {
      "L": "Suffer hardship with me as a good soldier of Christ Jesus.",
      "M": "Join with me in suffering, like a good soldier of Christ Jesus.",
      "T": "Take your share of suffering alongside me, as a good soldier of Christ Jesus."
    },
    "4": {
      "L": "No soldier on service entangles himself in the affairs of this life, so that he may please the one who enlisted him.",
      "M": "No one serving as a soldier gets entangled in civilian affairs, but rather tries to please his commanding officer.",
      "T": "A soldier on active duty doesn't get tangled up in the business of ordinary life—his whole aim is to please the officer who enlisted him."
    },
    "5": {
      "L": "Also, if anyone competes as an athlete, he does not win the prize unless he competes according to the rules.",
      "M": "Similarly, anyone who competes as an athlete does not receive the victor's crown except by competing according to the rules.",
      "T": "And an athlete doesn't receive the winner's wreath unless he competes by the rules."
    },
    "6": {
      "L": "The hard-working farmer must be the first to receive his share of the crops.",
      "M": "The hardworking farmer should be the first to receive a share of the crops.",
      "T": "The farmer who does the hard work deserves to be the first to eat from his harvest."
    },
    "7": {
      "L": "Consider what I say, for the Lord will give you understanding in all things.",
      "M": "Reflect on what I am saying, for the Lord will give you insight into all this.",
      "T": "Think carefully about what I'm telling you. The Lord will help you see what it means."
    },
    "8": {
      "L": "Remember Jesus Christ, raised from the dead, descended from David, according to my gospel,",
      "M": "Remember Jesus Christ, raised from the dead, descended from David. This is my gospel,",
      "T": "Keep this at the center of everything: Jesus Christ—raised from the dead, a descendant of David. This is the gospel I proclaim,"
    },
    "9": {
      "L": "for which I suffer hardship as a criminal, even to the point of chains; but the word of God is not chained.",
      "M": "for which I am suffering even to the point of being chained like a criminal. But God's word is not chained.",
      "T": "for which I suffer like a criminal—yes, even in chains. But God's word cannot be chained."
    },
    "10": {
      "L": "Therefore I endure all things for the sake of the elect, that they also may obtain the salvation that is in Christ Jesus with eternal glory.",
      "M": "Therefore I endure everything for the sake of the elect, that they too may obtain the salvation that is in Christ Jesus, with eternal glory.",
      "T": "So I endure everything for the sake of those God has chosen—so they too can obtain the salvation that is in Christ Jesus, with all its eternal glory."
    },
    "11": {
      "L": "The saying is faithful: for if we died with him, we will also live with him;",
      "M": "Here is a trustworthy saying: If we died with him, we will also live with him;",
      "T": "This is a trustworthy saying: If we have died with him, we will also live with him."
    },
    "12": {
      "L": "if we endure, we will also reign with him; if we deny him, he also will deny us;",
      "M": "if we endure, we will also reign with him. If we disown him, he will also disown us;",
      "T": "If we endure, we will reign with him. If we disown him, he will disown us."
    },
    "13": {
      "L": "if we are faithless, he remains faithful; for he cannot deny himself.",
      "M": "if we are faithless, he remains faithful, for he cannot disown himself.",
      "T": "Even when we fail him, he remains faithful—he cannot contradict his own nature."
    },
    "14": {
      "L": "Remind them of these things, solemnly charging them before the Lord not to dispute about words, which is useful for nothing, but to the ruin of those who hear.",
      "M": "Keep reminding God's people of these things. Warn them before God against quarreling about words; it is of no value, and only ruins those who listen.",
      "T": "Keep putting these truths before people. Charge them solemnly before God to stop quarreling over words—it serves no purpose and only tears apart those who listen."
    },
    "15": {
      "L": "Be diligent to present yourself approved to God, a worker who has no need to be ashamed, rightly dividing the word of truth.",
      "M": "Do your best to present yourself to God as one approved, a worker who does not need to be ashamed and who correctly handles the word of truth.",
      "T": "Work hard so you can stand before God without shame—a workman who correctly cuts the word of truth straight."
    },
    "16": {
      "L": "But avoid profane and empty chatter, for they will go further into ungodliness,",
      "M": "Avoid godless chatter, because those who indulge in it will become more and more ungodly.",
      "T": "Steer clear of godless, empty talk. Those who indulge in it only sink deeper and deeper into ungodliness."
    },
    "17": {
      "L": "and their word will spread like gangrene. Among them are Hymenaeus and Philetus,",
      "M": "Their teaching will spread like gangrene. Among them are Hymenaeus and Philetus,",
      "T": "Their words spread like gangrene. Hymenaeus and Philetus are examples of this—"
    },
    "18": {
      "L": "who have gone astray from the truth, saying that the resurrection has already occurred, and they are upsetting the faith of some.",
      "M": "who have departed from the truth. They say that the resurrection has already taken place, and they destroy the faith of some.",
      "T": "they have swerved away from the truth by claiming the resurrection has already happened, and they are capsizing the faith of some people."
    },
    "19": {
      "L": "Nevertheless, the firm foundation of God stands, having this seal: 'The Lord knows those who are his,' and, 'Let everyone who names the name of the Lord depart from iniquity.'",
      "M": "Nevertheless, God's solid foundation stands firm, sealed with this inscription: 'The Lord knows those who are his,' and, 'Everyone who confesses the name of the Lord must turn away from wickedness.'",
      "T": "Yet God's solid foundation cannot be shaken. It bears this double seal: 'The Lord knows those who belong to him'—an echo of Korah's rebellion, when God vindicated his own—and: 'Everyone who claims the Lord's name must turn away from evil.'"
    },
    "20": {
      "L": "Now in a great house there are not only vessels of gold and silver, but also of wood and clay, some to honor and some to dishonor.",
      "M": "In a large house there are articles not only of gold and silver, but also of wood and clay; some are for special purposes and some for ordinary use.",
      "T": "In a large household you don't find only gold and silver bowls—there are also wooden and clay ones. Some are set apart for honorable use; others are used for everyday, disposable tasks."
    },
    "21": {
      "L": "Therefore, if anyone cleanses himself from these things, he will be a vessel for honor, sanctified, useful to the master, prepared for every good work.",
      "M": "Those who cleanse themselves from the latter will be instruments for special purposes, made holy, useful to the Master and prepared to do any good work.",
      "T": "If you purge yourself of the dishonorable things, you become a vessel set apart for honorable use—made holy, useful to the Master, ready for any good work."
    },
    "22": {
      "L": "Flee youthful lusts, but pursue righteousness, faith, love, and peace with those who call on the Lord out of a pure heart.",
      "M": "Flee the evil desires of youth and pursue righteousness, faith, love and peace, along with those who call on the Lord out of a pure heart.",
      "T": "Run from youthful passions. Instead, pursue righteousness, faith, love, and peace—alongside everyone who calls on the Lord with a sincere heart."
    },
    "23": {
      "L": "But refuse foolish and ignorant disputes, knowing that they give birth to quarrels.",
      "M": "Don't have anything to do with foolish and stupid arguments, because you know they produce quarrels.",
      "T": "Have nothing to do with foolish, uninformed arguments—you already know they only breed fights."
    },
    "24": {
      "L": "The Lord's servant must not be quarrelsome, but be gentle to all, able to teach, patient when wronged,",
      "M": "And the Lord's servant must not be quarrelsome but must be kind to everyone, able to teach, not resentful.",
      "T": "The Lord's servant must not be a fighter. He must be gentle with everyone, skilled at teaching, able to bear wrongs without bitterness."
    },
    "25": {
      "L": "in meekness correcting those who oppose, if perhaps God may grant them repentance leading to the knowledge of the truth,",
      "M": "Opponents must be gently instructed, in the hope that God will grant them repentance leading them to a knowledge of the truth,",
      "T": "He must gently instruct those who push back—because God may grant them the repentance they need to come to the knowledge of the truth."
    },
    "26": {
      "L": "and they may come to their senses and escape the snare of the devil, having been captured by him to do his will.",
      "M": "and that they will come to their senses and escape from the trap of the devil, who has taken them captive to do his will.",
      "T": "Then they can sober up and escape the devil's trap—they have been captured by him to serve his purposes, but God can free them."
    }
  },
  "3": {
    "1": {
      "L": "But know this: in the last days difficult times will come.",
      "M": "But mark this: There will be terrible times in the last days.",
      "T": "Understand this clearly: in the last days perilous times will arrive."
    },
    "2": {
      "L": "For people will be lovers of self, lovers of money, boastful, proud, blasphemers, disobedient to parents, ungrateful, unholy,",
      "M": "People will be lovers of themselves, lovers of money, boastful, proud, abusive, disobedient to their parents, ungrateful, unholy,",
      "T": "People will be utterly self-obsessed and money-hungry—boastful, arrogant, abusive, disobedient to parents, ungrateful, and godless."
    },
    "3": {
      "L": "unloving, irreconcilable, slanderers, without self-control, brutal, despisers of good,",
      "M": "without love, unforgiving, slanderous, without self-control, brutal, not lovers of the good,",
      "T": "They will be loveless, unforgiving, slanderous, without self-control, savage, and hostile to everything good."
    },
    "4": {
      "L": "traitors, reckless, conceited, lovers of pleasure rather than lovers of God,",
      "M": "treacherous, rash, conceited, lovers of pleasure rather than lovers of God—",
      "T": "They will be treacherous, reckless, puffed up—devoted to pleasure rather than to God."
    },
    "5": {
      "L": "holding a form of godliness but having denied its power. Turn away from these people.",
      "M": "having a form of godliness but denying its power. Have nothing to do with such people.",
      "T": "They will keep up the outward appearance of religion while emptying it of all its power. Stay away from people like this."
    },
    "6": {
      "L": "For among them are those who creep into households and captivate weak women who are burdened with sins, led by various impulses,",
      "M": "They are the kind who worm their way into homes and gain control over gullible women, who are loaded down with sins and are swayed by all kinds of evil desires,",
      "T": "These are the ones who slither into households and gain power over vulnerable women—women weighed down by guilt and tossed about by one craving after another."
    },
    "7": {
      "L": "always learning and never able to come to the knowledge of the truth.",
      "M": "always learning but never able to come to a knowledge of the truth.",
      "T": "They are perpetually taking in information yet never arriving at the truth."
    },
    "8": {
      "L": "Just as Jannes and Jambres opposed Moses, so these men also oppose the truth, men corrupted in mind and disqualified concerning the faith.",
      "M": "Just as Jannes and Jambres opposed Moses, so also these teachers oppose the truth. They are men of depraved minds, who, as far as the faith is concerned, are rejected.",
      "T": "Just as Jannes and Jambres stood against Moses, these men stand against the truth. Their minds are rotten and when it comes to the faith, they have failed the test."
    },
    "9": {
      "L": "But they will not make further progress, for their folly will be plain to all, as it was also with those two.",
      "M": "But they will not get very far because, as in the case of those men, their folly will be clear to everyone.",
      "T": "But they won't get far. Their stupidity will become obvious to everyone—just as it was with Jannes and Jambres."
    },
    "10": {
      "L": "But you have followed my teaching, conduct, purpose, faith, patience, love, endurance,",
      "M": "You, however, know all about my teaching, my way of life, my purpose, faith, patience, love, endurance,",
      "T": "But you have followed closely my teaching, my way of life, my purpose, my faith, my patience, my love, my endurance—"
    },
    "11": {
      "L": "persecutions, and sufferings—such as happened to me at Antioch, at Iconium, at Lystra; what persecutions I endured, and out of them all the Lord rescued me.",
      "M": "persecutions, sufferings—what kinds of things happened to me in Antioch, Iconium and Lystra, the persecutions I endured. Yet the Lord rescued me from all of them.",
      "T": "the persecutions and sufferings that came on me in Antioch, in Iconium, in Lystra. You know the kinds of things I endured—and out of all of them the Lord rescued me."
    },
    "12": {
      "L": "And indeed, all who desire to live godly in Christ Jesus will be persecuted.",
      "M": "In fact, everyone who wants to live a godly life in Christ Jesus will be persecuted,",
      "T": "And make no mistake: everyone who intends to live a godly life in Christ Jesus will face persecution."
    },
    "13": {
      "L": "But evil men and impostors will proceed from bad to worse, deceiving and being deceived.",
      "M": "while evildoers and impostors will go from bad to worse, deceiving and being deceived.",
      "T": "Meanwhile evil people and frauds will go from bad to worse—they deceive others and are themselves deceived."
    },
    "14": {
      "L": "But as for you, continue in what you have learned and have become convinced of, knowing from whom you have learned it,",
      "M": "But as for you, continue in what you have learned and have become convinced about, because you know those from whom you learned it,",
      "T": "But you—stand firm in what you have learned and become fully convinced of, knowing the people you learned it from."
    },
    "15": {
      "L": "and that from a child you have known the sacred scriptures, which are able to make you wise unto salvation through faith which is in Christ Jesus.",
      "M": "and how from infancy you have known the Holy Scriptures, which are able to make you wise for salvation through faith in Christ Jesus.",
      "T": "From childhood you have known the holy Scriptures, and they have the power to make you wise for salvation—through faith in Christ Jesus."
    },
    "16": {
      "L": "All scripture is God-breathed and profitable for teaching, for reproof, for correction, for instruction in righteousness,",
      "M": "All Scripture is breathed out by God and is profitable for teaching, rebuking, correcting and training in righteousness,",
      "T": "Every Scripture text carries the very breath of God—which makes it useful for teaching the truth, exposing error, correcting faults, and training people in the way of righteousness."
    },
    "17": {
      "L": "that the man of God may be complete, thoroughly equipped for every good work.",
      "M": "so that the servant of God may be thoroughly equipped for every good work.",
      "T": "This is how the person who belongs to God becomes complete—fully outfitted for every good work there is."
    }
  },
  "4": {
    "1": {
      "L": "I charge you before God and Christ Jesus, who is going to judge the living and the dead, and by his appearing and his kingdom:",
      "M": "In the presence of God and of Christ Jesus, who will judge the living and the dead, and in view of his appearing and his kingdom, I give you this charge:",
      "T": "I charge you solemnly—before God and before Christ Jesus, who will one day judge the living and the dead, and in light of his appearing and his kingdom:"
    },
    "2": {
      "L": "preach the word; be ready in season and out of season; reprove, rebuke, and exhort with all patience and teaching.",
      "M": "Preach the word; be prepared in season and out of season; correct, rebuke and encourage—with great patience and careful instruction.",
      "T": "Preach the word. Be ready to do it whether the moment seems right or not. Correct, rebuke, and encourage—always with deep patience and careful teaching."
    },
    "3": {
      "L": "For the time will come when they will not endure sound teaching, but having itching ears they will heap up for themselves teachers according to their own desires,",
      "M": "For the time will come when people will not put up with sound doctrine. Instead, to suit their own desires, they will gather around them a great number of teachers to say what their itching ears want to hear.",
      "T": "The day is coming when people will refuse to put up with sound teaching. Instead, driven by their own cravings, they will surround themselves with teachers who scratch the itch they want scratched."
    },
    "4": {
      "L": "and they will turn their ears away from the truth and will turn aside to myths.",
      "M": "They will turn their ears away from the truth and turn aside to myths.",
      "T": "They will stop listening to the truth and wander off after myths."
    },
    "5": {
      "L": "But as for you, be sober in all things, suffer hardship, do the work of an evangelist, fulfill your ministry.",
      "M": "But you, keep your head in all situations, endure hardship, do the work of an evangelist, discharge all the duties of your ministry.",
      "T": "But you—stay clear-headed in everything. Bear hardship. Do the work of an evangelist. Carry out your ministry to the full."
    },
    "6": {
      "L": "For I am already being poured out as a drink offering, and the time of my departure has come.",
      "M": "For I am already being poured out like a drink offering, and the time for my departure is near.",
      "T": "For I am already being poured out like a sacrificial drink offering, and the hour of my departure has arrived."
    },
    "7": {
      "L": "I have fought the good fight, I have finished the race, I have kept the faith.",
      "M": "I have fought the good fight, I have finished the race, I have kept the faith.",
      "T": "I have fought the good fight to its end. I have run the full course. I have kept the faith."
    },
    "8": {
      "L": "Henceforth there is laid up for me the crown of righteousness, which the Lord, the righteous Judge, will award to me on that day, and not only to me but also to all who have loved his appearing.",
      "M": "Now there is in store for me the crown of righteousness, which the Lord, the righteous Judge, will award to me on that day—and not only to me, but also to all who have longed for his appearing.",
      "T": "From now on the crown of righteousness waits for me. The Lord, who judges rightly, will place it on my head on that final day—and not only on mine, but on the head of everyone who has been longing for his return."
    },
    "9": {
      "L": "Do your best to come to me quickly,",
      "M": "Do your best to come to me quickly,",
      "T": "Make every effort to come to me soon."
    },
    "10": {
      "L": "for Demas, having loved this present world, has deserted me and has gone to Thessalonica; Crescens to Galatia, Titus to Dalmatia.",
      "M": "for Demas, because he loved this world, has deserted me and has gone to Thessalonica. Crescens has gone to Galatia, and Titus to Dalmatia.",
      "T": "Demas has abandoned me—he fell in love with this present age—and gone to Thessalonica. Crescens has gone to Galatia, Titus to Dalmatia."
    },
    "11": {
      "L": "Only Luke is with me. Take Mark and bring him with you, for he is useful to me for service.",
      "M": "Only Luke is with me. Get Mark and bring him with you, because he is helpful to me in my ministry.",
      "T": "Only Luke is still with me. Pick up Mark on your way—he is genuinely useful to me in the work."
    },
    "12": {
      "L": "But Tychicus I have sent to Ephesus.",
      "M": "I sent Tychicus to Ephesus.",
      "T": "I have sent Tychicus to Ephesus."
    },
    "13": {
      "L": "When you come, bring the cloak that I left with Carpus at Troas, and the books, and especially the parchments.",
      "M": "When you come, bring the cloak that I left with Carpus at Troas, and my scrolls, especially the parchments.",
      "T": "When you come, bring the cloak I left at Troas with Carpus, and bring my scrolls—especially the parchments."
    },
    "14": {
      "L": "Alexander the coppersmith did me great harm; the Lord will repay him according to his works.",
      "M": "Alexander the metalworker did me a great deal of harm. The Lord will repay him for what he has done.",
      "T": "Alexander the metalworker caused me enormous trouble. The Lord will pay him back for what he did."
    },
    "15": {
      "L": "You also be on guard against him, for he greatly opposed our words.",
      "M": "You too should be on your guard against him, because he strongly opposed our message.",
      "T": "You should watch out for him too—he put up fierce resistance to our message."
    },
    "16": {
      "L": "At my first defense no one stood with me, but all forsook me. May it not be held against them.",
      "M": "At my first defense, no one came to my support, but everyone deserted me. May it not be held against them.",
      "T": "When I appeared for my first hearing, no one stood with me—everyone deserted me. May it not be counted against them."
    },
    "17": {
      "L": "But the Lord stood with me and strengthened me, so that through me the proclamation might be fully made and all the Gentiles might hear it; and I was delivered from the mouth of the lion.",
      "M": "But the Lord stood at my side and gave me strength, so that through me the message might be fully proclaimed and all the Gentiles might hear it. And I was delivered from the lion's mouth.",
      "T": "But the Lord himself stood by my side and poured strength into me—so that through me the proclamation would be completed and every nation would hear it. And I was rescued from the lion's jaws."
    },
    "18": {
      "L": "The Lord will deliver me from every evil work and will save me into his heavenly kingdom; to whom be glory for ever and ever. Amen.",
      "M": "The Lord will rescue me from every evil attack and will bring me safely to his heavenly kingdom. To him be glory for ever and ever. Amen.",
      "T": "The Lord will rescue me from every evil assault and bring me safely home to his heavenly kingdom. To him be glory for ever and ever. Amen."
    },
    "19": {
      "L": "Greet Prisca and Aquila and the household of Onesiphorus.",
      "M": "Greet Priscilla and Aquila and the household of Onesiphorus.",
      "T": "Give my greetings to Priscilla and Aquila, and to the family of Onesiphorus."
    },
    "20": {
      "L": "Erastus remained at Corinth, but Trophimus I left sick at Miletus.",
      "M": "Erastus stayed in Corinth, and I left Trophimus sick in Miletus.",
      "T": "Erastus stayed behind in Corinth. I had to leave Trophimus sick in Miletus."
    },
    "21": {
      "L": "Do your best to come before winter. Eubulus greets you, and Pudens, and Linus, and Claudia, and all the brothers.",
      "M": "Do your best to get here before winter. Eubulus greets you, and so do Pudens, Linus, Claudia and all the brothers and sisters.",
      "T": "Try hard to get here before winter. Eubulus sends greetings, as do Pudens, Linus, Claudia, and all the brothers and sisters here."
    },
    "22": {
      "L": "The Lord be with your spirit. Grace be with you.",
      "M": "The Lord be with your spirit. Grace be with you all.",
      "T": "May the Lord be with your spirit. Grace be with you all."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '2timothy')
        merge_tier(existing, TWOTIMOTHY, tier_key)
        save(tier_dir, '2timothy', existing)
    print('2 Timothy 1–4 written.')

if __name__ == '__main__':
    main()
