"""
MKT 1 Timothy chapters 1–3 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-1timothy-1-3.py

Translation decisions:
- G2962 (κύριος): "Lord" across all tiers — consistent with all Pauline scripts.
- G5547 (Χριστός): "Christ" as a proper name throughout — consistent with Pauline pattern.
- G4102 (πίστις): "faith" throughout; no "faithfulness of Christ" construct in these chapters.
  At 1:2 "genuine child in the faith" — the phrase modifies relationship, not a genitive-of-origin.
- G26 (ἀγάπη) at 1:5, 1:14, 2:15: "love" — willed, covenantal, self-giving; distinct from φιλία.
- G166 (αἰώνιος) at 1:16: "eternal" life — consistent with all Pauline scripts; the eschatological
  quality of age-to-come life is surfaced in T without abandoning "eternal" in L/M.
- G4151 (πνεῦμα) at 3:16: "Spirit" (capitalized) — the Holy Spirit's vindication/justification of
  Christ; all prior Pauline scripts capitalize when the referent is clearly divine.
- G4561 (σάρξ) at 3:16: "flesh" — straightforward bodily incarnation; no fallen-nature sense here.
  L/M keep "flesh." T expands to "mortal flesh" to surface the incarnation's weight.
- G831 (αὐθεντέω) at 2:12: hapax legomenon (appears only here in the NT). Options include
  "usurp authority" (KJV), "assume authority" (NIV), "exercise authority" (ESV/NASB), or "domineer."
  Rendered "exercise authority" in L/M — the least loaded of the accurate options. In T the directive
  is framed as Paul's instruction for this congregation's specific situation, which is the most
  defensible reading given the hapax status and the congregational context of ch. 2 as a whole.
- G3466 (μυστήριον) at 3:9, 3:16: "mystery" in all tiers — the apocalyptic sense (a secret of God
  now disclosed, not a riddle to be solved). T at 3:16 expands on the revealed-mystery register.
- G1228 (διάβολος): context-dependent. At 3:6, 3:7 = "the devil" (Satan, the adversary).
  At 3:11 = "slanderers" (same Greek word applied to humans who make false accusations; the KJV
  "false accusers" and NIV "malicious talkers" both render this correctly). The double meaning is
  noted but not collapsed: different English words are used in each context.
- G1985 (ἐπίσκοπος): "overseer" throughout — avoids the ecclesiastical/episcopal freight of "bishop"
  and stays closer to the Greek's functional meaning of one who watches over a community.
- G1249 (διάκονος): "deacons" — the role is well-established enough to keep the transliterated term.
- G1984 (ἐπισκοπή) at 3:1: "the office of overseer" (L/M) / "the role of overseer" (T).
- G3547 (νομοδιδάσκαλος) at 1:7: "teachers of the law" — the compound Greek term rendered literally.
- 1:15 "faithful saying" formula (G4103 λόγος): this is the first of five πιστὸς ὁ λόγος formulas
  in the Pastoral Epistles. Rendered "trustworthy saying" in L/M; T brings out the formula's
  liturgical weight ("this is worth trusting completely").
- 2:15 "saved through childbearing" (σωθήσεται διὰ τῆς τεκνογονίας): one of the NT's most debated
  verses. L preserves the literal Greek. M gives the most natural English reading. T acknowledges
  that Paul is speaking of women's sphere of faithful living (including but not limited to
  childbearing) rather than making childbearing a mechanism of justification; the conditional
  "if they continue..." clarifies this. Neither an exemption gloss nor a radical reinterpretation.
- 3:16 six-line confessional hymn (ἐφανερώθη ἐν σαρκί...): probably pre-Pauline. L follows the
  compressed participle structure. M adds natural subjects. T renders each line as a stanza,
  surfacing the cosmic scope of the incarnation-exaltation pattern.
- Aspect notes: 1:12 aorist ἡγήσατο = completed act of judgment ("he judged me faithful");
  1:14 aorist ὑπερεπλεόνασεν = "overflowed" (point action, lavish abundance);
  3:16 aorist passives throughout = completed eschatological acts (manifested, vindicated, etc.).
- No יהוה (H3068) in this book — all of 1 Timothy is Greek. "Lord" renders G2962 exclusively.
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

TIMOTHY_1 = {
  "1": {
    "1": {
      "L": "Paul, an apostle of Christ Jesus by commandment of God our Savior and of Christ Jesus our hope,",
      "M": "Paul, an apostle of Christ Jesus by the command of God our Savior and of Christ Jesus our hope,",
      "T": "I, Paul, am an apostle of Christ Jesus—appointed by the command of God our Savior and by Christ Jesus himself, who is our hope."
    },
    "2": {
      "L": "to Timothy, my true child in the faith: Grace, mercy, and peace from God the Father and Christ Jesus our Lord.",
      "M": "To Timothy, my true son in the faith: Grace, mercy and peace from God the Father and Christ Jesus our Lord.",
      "T": "To Timothy—my genuine son in the faith. May you receive grace, mercy, and peace from God the Father and Christ Jesus our Lord."
    },
    "3": {
      "L": "As I urged you when going into Macedonia: remain at Ephesus so that you might charge certain ones not to teach differently,",
      "M": "As I urged you when I went to Macedonia, stay on at Ephesus so that you may command certain people not to teach false doctrines",
      "T": "When I left for Macedonia I urged you to stay in Ephesus—and that instruction still stands. Your task is to command certain people to stop teaching their own version of the faith."
    },
    "4": {
      "L": "nor to give heed to fables and endless genealogies, which cause speculation rather than godly stewardship in faith.",
      "M": "and not to devote themselves to myths and endless genealogies. Such things promote controversial speculations rather than advancing God's work—which is by faith.",
      "T": "Tell them to stop fixating on myths and endless genealogies. These things breed endless speculation rather than building up God's people in the faith."
    },
    "5": {
      "L": "Now the end of the commandment is love out of a pure heart and a good conscience and sincere faith,",
      "M": "The goal of this instruction is love, which comes from a pure heart and a good conscience and a sincere faith.",
      "T": "The whole point of this charge is love—the kind that flows from a clean heart, a clear conscience, and a genuine faith."
    },
    "6": {
      "L": "from which some, having swerved, have turned aside to vain jangling,",
      "M": "Some have departed from these and turned to meaningless talk.",
      "T": "Some people have missed all of this—veering off into pointless argument."
    },
    "7": {
      "L": "desiring to be teachers of the law, not understanding either what they say or the things about which they confidently assert.",
      "M": "They want to be teachers of the law, but they do not know what they are talking about or what they so confidently affirm.",
      "T": "They want to be respected teachers of the Law, yet they have no real grasp of what they say or what they claim to teach with such confidence."
    },
    "8": {
      "L": "But we know that the law is good, if one uses it lawfully,",
      "M": "We know that the law is good if one uses it properly.",
      "T": "The Law itself is good—that is not the issue. The question is whether it is being used rightly."
    },
    "9": {
      "L": "knowing this, that the law is not laid down for a righteous man but for the lawless and disobedient, for the ungodly and sinners, for the unholy and profane, for murderers of fathers and murderers of mothers, for manslayers,",
      "M": "We also know that the law is made not for the righteous but for lawbreakers and rebels, the ungodly and sinful, the unholy and irreligious, for those who kill their fathers or mothers, for murderers,",
      "T": "We know the Law was not designed for the righteous person but for those who defy it: the lawless and rebellious, the godless and sinful, the unholy and irreverent, those who murder their parents, those who kill—"
    },
    "10": {
      "L": "for the sexually immoral, for men who lie with men, for enslavers, for liars, for perjurers, and for whatever else is contrary to sound doctrine,",
      "M": "for the sexually immoral, for those who practice homosexuality, for slave traders, for liars and perjurers—and for whatever else is contrary to the sound doctrine",
      "T": "—the sexually immoral, those who engage in same-sex acts, slave traders, liars, those who swear falsely, and anyone else whose conduct is out of step with healthy teaching."
    },
    "11": {
      "L": "in accordance with the gospel of the glory of the blessed God with which I was entrusted.",
      "M": "that conforms to the gospel concerning the glory of the blessed God, which he entrusted to me.",
      "T": "This is the standard set by the gospel of the glory of the blessed God—the gospel that was entrusted specifically to me."
    },
    "12": {
      "L": "I thank Christ Jesus our Lord, who has given me strength, because he deemed me faithful, appointing me to his service,",
      "M": "I thank Christ Jesus our Lord, who has given me strength, that he considered me trustworthy, appointing me to his service.",
      "T": "I am deeply grateful to Christ Jesus our Lord, who strengthened me and counted me as faithful—placing me in his service."
    },
    "13": {
      "L": "who was formerly a blasphemer, a persecutor, and insolent—but I received mercy because I did it in ignorance in unbelief.",
      "M": "Even though I was once a blasphemer and a persecutor and a violent man, I was shown mercy because I acted in ignorance and unbelief.",
      "T": "I had been a blasphemer, a persecutor, a violent man. But God showed me mercy because I acted out of ignorance—I did not yet believe."
    },
    "14": {
      "L": "And the grace of our Lord was exceedingly abundant with the faith and love that are in Christ Jesus.",
      "M": "The grace of our Lord was poured out on me abundantly, along with the faith and love that are in Christ Jesus.",
      "T": "And the grace of our Lord flooded into me—bringing with it the faith and love that are found in Christ Jesus."
    },
    "15": {
      "L": "This is a faithful saying and worthy of all acceptance: that Christ Jesus came into the world to save sinners, of whom I am chief.",
      "M": "Here is a trustworthy saying that deserves full acceptance: Christ Jesus came into the world to save sinners—of whom I am the worst.",
      "T": "This is a saying you can trust completely: Christ Jesus came into the world to save sinners—and I am the worst of them."
    },
    "16": {
      "L": "But for this reason I obtained mercy: that in me first Jesus Christ might display all his patience, as a pattern for those about to believe in him for eternal life.",
      "M": "But for that very reason I was shown mercy so that in me, the worst of sinners, Christ Jesus might display his immense patience as an example for those who would believe in him and receive eternal life.",
      "T": "The very reason I received mercy was so that in me—the foremost sinner—Jesus Christ could put his inexhaustible patience on full display, as a prototype of grace for all who would ever believe and receive the life of the age to come."
    },
    "17": {
      "L": "Now to the King of the ages, immortal, invisible, the only God, be honor and glory forever and ever. Amen.",
      "M": "Now to the King eternal, immortal, invisible, the only God, be honor and glory for ever and ever. Amen.",
      "T": "All honor and glory to the eternal King—the one who never dies, whom no eye can see, the only God. Forever and ever. Amen."
    },
    "18": {
      "L": "This charge I commit to you, Timothy my son, in accordance with the prophecies previously made about you, that by them you may wage the good warfare,",
      "M": "Timothy, my son, I am giving you this command in keeping with the prophecies once made about you, so that by recalling them you may fight the battle well,",
      "T": "Timothy, my son, I am entrusting this command to you. It aligns with the prophetic words once spoken over you—hold on to them, and let them fuel your fight in this great campaign."
    },
    "19": {
      "L": "holding faith and a good conscience, which some having thrust away have made shipwreck of the faith.",
      "M": "holding on to faith and a good conscience, which some have rejected and so have suffered shipwreck with regard to the faith.",
      "T": "Keep a firm grip on faith and a clean conscience. Some have thrown both overboard—and their faith has capsized."
    },
    "20": {
      "L": "among whom are Hymenaeus and Alexander, whom I delivered over to Satan that they may be taught not to blaspheme.",
      "M": "Among them are Hymenaeus and Alexander, whom I have handed over to Satan to be taught not to blaspheme.",
      "T": "Hymenaeus and Alexander are among them. I have handed them over to Satan—so they can learn, at real cost, not to blaspheme."
    }
  },
  "2": {
    "1": {
      "L": "I urge, then, first of all, that petitions, prayers, intercessions, and giving of thanks be made for all men,",
      "M": "I urge, then, first of all, that petitions, prayers, intercession and thanksgiving be made for all people—",
      "T": "The first and most important thing: pray for everyone. Bring your requests, your prayers, your intercession, and your gratitude to God—for all people."
    },
    "2": {
      "L": "for kings and all who are in authority, that we may lead a tranquil and quiet life in all godliness and dignity.",
      "M": "for kings and all those in authority, that we may live peaceful and quiet lives in all godliness and holiness.",
      "T": "Pray for kings and for everyone who holds authority—so that we can live in peace and quiet, conducting ourselves with godliness and dignity."
    },
    "3": {
      "L": "This is good and acceptable before God our Savior,",
      "M": "This is good, and pleases God our Savior,",
      "T": "God our Savior is pleased by this kind of prayer. It is simply the right thing to do."
    },
    "4": {
      "L": "who wills all men to be saved and to come to the knowledge of the truth.",
      "M": "who wants all people to be saved and to come to a knowledge of the truth.",
      "T": "He wants every person to be saved and to come to know the truth clearly."
    },
    "5": {
      "L": "For there is one God, and one mediator between God and men, the man Christ Jesus,",
      "M": "For there is one God and one mediator between God and mankind, the man Christ Jesus,",
      "T": "There is one God. And there is one go-between connecting that God to humanity—the man Christ Jesus."
    },
    "6": {
      "L": "who gave himself as a ransom for all, the testimony given at the proper time.",
      "M": "who gave himself as a ransom for all people. This has now been witnessed to at the proper time.",
      "T": "He gave himself as the ransom-price for every person—a truth publicly disclosed at exactly the right moment in history."
    },
    "7": {
      "L": "for which I was appointed a preacher and an apostle—I speak the truth, I am not lying—a teacher of the Gentiles in faith and truth.",
      "M": "And for this purpose I was appointed a herald and an apostle—I am telling the truth, I am not lying—and a true and faithful teacher of the Gentiles.",
      "T": "To deliver this message I was personally appointed as a herald and an apostle—I am speaking plainly and without exaggeration—a teacher of the Gentiles, working within the bounds of faith and truth."
    },
    "8": {
      "L": "I desire therefore that the men pray in every place, lifting up holy hands without anger and disputing.",
      "M": "Therefore I want the men everywhere to pray, lifting up holy hands without anger or disputing.",
      "T": "So I want men everywhere to pray—raising hands that are clean, free from anger and the quarreling that poisons prayer."
    },
    "9": {
      "L": "In the same way, women are to adorn themselves with proper clothing, with modesty and sobriety, not with braided hair or gold or pearls or expensive clothes,",
      "M": "I also want the women to dress modestly, with decency and propriety, adorning themselves not with elaborate hairstyles or gold or pearls or expensive clothes,",
      "T": "Similarly, women should dress in a way that is becoming—with modesty and good judgment, not making a display of elaborate hairstyles, jewelry, or expensive clothing."
    },
    "10": {
      "L": "but with what is fitting for women who profess godliness—through good works.",
      "M": "but with good deeds, appropriate for women who profess to worship God.",
      "T": "Instead, the fitting adornment for women who claim to follow God is a life full of good works."
    },
    "11": {
      "L": "Let a woman learn in silence with all submission.",
      "M": "A woman should learn in quietness and full submission.",
      "T": "Let a woman learn—and let her learning take place in a spirit of quiet receptiveness and genuine deference."
    },
    "12": {
      "L": "But I do not permit a woman to teach or to exercise authority over a man; she is to be in silence.",
      "M": "I do not permit a woman to teach or to assume authority over a man; she must be quiet.",
      "T": "In this congregation's current situation, I am not permitting a woman to teach or to direct the men; let her hold a posture of quiet reception."
    },
    "13": {
      "L": "For Adam was formed first, then Eve.",
      "M": "For Adam was formed first, then Eve.",
      "T": "The order of creation underlies this: Adam was formed first, then Eve."
    },
    "14": {
      "L": "And Adam was not deceived, but the woman was deceived and fell into transgression.",
      "M": "And Adam was not the one deceived; it was the woman who was deceived and became a sinner.",
      "T": "It was not Adam who was taken in by the serpent's deception—it was the woman who was deceived and stepped into disobedience."
    },
    "15": {
      "L": "But she will be saved through bearing children, if they continue in faith and love and holiness with self-control.",
      "M": "But women will be saved through childbearing—if they continue in faith, love and holiness with propriety.",
      "T": "Yet women are not without hope within these constraints—salvation comes through ordinary faithful living, including the bearing and raising of children, as they continue in faith, love, and holiness with thoughtful self-control."
    }
  },
  "3": {
    "1": {
      "L": "This is a faithful saying: if any man aspires to the office of overseer, he desires a good work.",
      "M": "Here is a trustworthy saying: whoever aspires to be an overseer desires a noble task.",
      "T": "This is worth taking seriously: anyone who sets their heart on being an overseer is reaching for something genuinely good."
    },
    "2": {
      "L": "The overseer therefore must be above reproach, the husband of one wife, sober, self-controlled, respectable, hospitable, able to teach;",
      "M": "Now the overseer is to be above reproach, faithful to his wife, temperate, self-controlled, respectable, hospitable, able to teach;",
      "T": "An overseer must be above reproach—faithful to his spouse, clear-headed, disciplined, dignified, hospitable, and able to teach."
    },
    "3": {
      "L": "not given to wine, not violent but gentle, not quarrelsome, not a lover of money;",
      "M": "not given to drunkenness, not violent but gentle, not quarrelsome, not a lover of money.",
      "T": "He must not be a heavy drinker, must not be quick with his fists but rather gentle, free from contentiousness, and not driven by greed."
    },
    "4": {
      "L": "one who rules his own household well, having his children in subjection with all dignity,",
      "M": "He must manage his own family well and see that his children obey him, and he must do so in a manner worthy of full respect.",
      "T": "He must lead his own home with genuine authority—his children respectful and under his guidance, the whole household marked by dignity."
    },
    "5": {
      "L": "for if a man does not know how to manage his own household, how will he care for the church of God?",
      "M": "If anyone does not know how to manage his own family, how can he take care of God's church?",
      "T": "The logic is straightforward: if a man cannot govern his own household well, how will he ever shepherd the church of God?"
    },
    "6": {
      "L": "not a novice, lest being puffed up with pride he fall into the judgment of the devil.",
      "M": "He must not be a recent convert, or he may become conceited and fall under the same judgment as the devil.",
      "T": "He must not be a new believer—such responsibility can inflate a young man's pride, and pride leads right into the same trap the devil walked into."
    },
    "7": {
      "L": "Moreover he must have a good report from those outside, lest he fall into disgrace and the snare of the devil.",
      "M": "He must also have a good reputation with outsiders, so that he will not fall into disgrace and into the devil's trap.",
      "T": "He also needs a good reputation among people outside the church—otherwise he becomes vulnerable to public disgrace and the devil's traps."
    },
    "8": {
      "L": "Deacons likewise must be dignified, not double-tongued, not addicted to much wine, not greedy for dishonest gain;",
      "M": "In the same way, deacons are to be worthy of respect, sincere, not indulging in much wine, and not pursuing dishonest gain.",
      "T": "Deacons must be people of genuine dignity—honest in speech, not heavy drinkers, not in it for the money."
    },
    "9": {
      "L": "holding the mystery of the faith in a pure conscience.",
      "M": "They must keep hold of the deep truths of the faith with a clear conscience.",
      "T": "They must hold the mystery of the faith—God's revealed plan now disclosed in Christ—with a conscience that has nothing to hide."
    },
    "10": {
      "L": "And these also must be tested first; then let them serve as deacons if they are found blameless.",
      "M": "They must first be tested; and then if there is nothing against them, let them serve as deacons.",
      "T": "Before anyone takes on this role, test them first. Let them serve as deacons only when they have proven themselves beyond reproach."
    },
    "11": {
      "L": "Women likewise must be dignified, not slanderers, sober-minded, faithful in all things.",
      "M": "In the same way, the women are to be worthy of respect, not malicious talkers but temperate and trustworthy in everything.",
      "T": "The women serving alongside them—whether wives or deaconesses—must be equally dignified: no malicious gossip, clear-headed, and completely trustworthy in all things."
    },
    "12": {
      "L": "Deacons are to be the husband of one wife, managing their children and their own households well.",
      "M": "A deacon must be faithful to his wife and must manage his children and his household well.",
      "T": "Each deacon must be faithful to his spouse and keep his household and children in good order."
    },
    "13": {
      "L": "For those who serve well as deacons gain for themselves a good standing and great boldness in faith in Christ Jesus.",
      "M": "Those who have served well gain an excellent standing and great assurance in their faith in Christ Jesus.",
      "T": "Faithful deacons earn something of real value: a solid reputation and the freedom that comes from deep, confident faith in Christ Jesus."
    },
    "14": {
      "L": "These things I write to you, hoping to come to you shortly;",
      "M": "Although I hope to come to you soon, I am writing you these instructions",
      "T": "I am writing all this to you hoping to come in person before long—"
    },
    "15": {
      "L": "but if I delay, that you may know how one must conduct himself in the household of God, which is the church of the living God, the pillar and foundation of the truth.",
      "M": "so that, if I am delayed, you will know how people ought to conduct themselves in God's household, which is the church of the living God, the pillar and foundation of the truth.",
      "T": "—but if I am delayed, you will have this in writing. You need to know how to conduct yourself in the household of God—the church of the living God, which holds up the truth like a pillar and holds it firm like a foundation."
    },
    "16": {
      "L": "And confessedly great is the mystery of godliness: He who was manifested in the flesh, vindicated in the Spirit, seen by angels, proclaimed among the nations, believed on in the world, taken up in glory.",
      "M": "Beyond all question, the mystery from which true godliness springs is great: He appeared in the flesh, was vindicated by the Spirit, was seen by angels, was preached among the nations, was believed on in the world, was taken up in glory.",
      "T": "By universal agreement among us, the mystery at the heart of all godly living is astonishing:\nThe eternal one appeared in mortal flesh.\nThe Spirit declared him righteous.\nAngels witnessed him.\nHe was announced to all the nations.\nThe world came to believe in him.\nHe was received back into glory."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '1timothy')
        merge_tier(existing, TIMOTHY_1, tier_key)
        save(tier_dir, '1timothy', existing)
    print('1 Timothy 1–3 written.')

if __name__ == '__main__':
    main()
