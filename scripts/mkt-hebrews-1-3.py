"""
MKT Hebrews chapters 1–3 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-hebrews-1-3.py

Translation decisions:
- G2316 θεός: 1:8 quotes Ps 45:6 addressing the Son directly as "O God" — retained in all three
    tiers; this is the strongest divine-name attribution to the Son in the Epistle and must not be
    softened; L/M/T all preserve "O God" as direct address
- G5207 υἱός (Son): "Son" capitalized throughout all tiers when referring to Christ; 3:6 "as a Son"
    kept lowercase-article to match the Greek anarthrous comparative
- G4151 πνεῦμα: 2:4 "the Holy Spirit" (capitalized, divine person); 1:7 "winds" (M/T) following
    the OT Ps 104 meaning of the LXX quote — angels are elemental, transitory; L keeps "spirits"
    to match the Greek surface; no occurrence of a contested spirit/Spirit ambiguity in chs 1–3
    beyond these two cases
- G3056 λόγος does not appear prominently; G4487 ῥῆμα at 1:3 "the word of his power" is the
    spoken, active utterance that sustains creation — rendered "word" across tiers; T adds "mighty
    word" to surface the power nuance
- G5481 χαρακτήρ (1:3): technical term for a die-stamped exact impression; L "express image";
    M "exact representation"; T "precise imprint" — the Son does not merely resemble the Father but
    bears his exact likeness as a wax seal bears the precise form of the signet ring
- G5287 ὑπόστασις (1:3): here means "essential nature/being" (not yet the Nicene technical sense
    of "person"); L "person" (traditional); M "nature"; T "very being"
- G541 ἀπαύγασμα (1:3): "outshining/radiance" — whether active (radiating) or passive (reflecting)
    is debated; "radiance" used in L/M; T "outshining" to keep the active sense
- G2433 ἱλάσκομαι (2:17): the verb means to propitiate/expiate; L "make propitiation"; M "make
    atonement"; T "make the atoning sacrifice" — the context is priestly service (high priest), so
    sacrificial language is appropriate; avoid mere "reconcile" which loses the cultic frame
- G747 ἀρχηγός (2:10): "one who goes ahead and opens the way" — leader, pioneer, author, founder;
    L "pioneer"; M "pioneer"; T "trailblazer" — the word emphasizes Christ as the first to traverse
    the path of suffering-to-glory that the "many sons" will follow
- G1343 δικαιοσύνη: 1:8-9 in OT quotation (Ps 45:7) — "righteousness" all tiers; the scepter
    and the virtue are both rendered "righteousness" for clarity and to preserve the parallelism
- G2962 κύριος: 1:10 is an OT quotation (Ps 102:25) where κύριε addresses YHWH; the Hebrews
    author applies it to the Son — "Lord" all tiers; the theological move is the author's own
- G652 ἀπόστολος (3:1): Jesus is called "the Apostle" only here in the NT; capitalized in L/M/T
    to mark its titular force; the term frames Jesus as the definitive divine Envoy (sent one)
- G749 ἀρχιερεύς (high priest): 2:17, 3:1 — "high priest" all tiers; Hebrews introduces this
    central theme; T does not paraphrase to "great priest" etc.
- G3671 ὁμολογία (3:1): "confession/profession" — what the community confesses about Jesus;
    L "confession"; M "confession"; T "confession we share" to surface the communal dimension
- G2663 κατάπαυσις (3:11, 18-19): "rest" — the eschatological Sabbath-rest that the wilderness
    generation forfeited; "rest" all tiers; the OT quotation (Ps 95) is preserved verbatim
- Ps 95:7-11 (3:7-11): quoted at length from the LXX; the repeated "today" is emphatic; the
    T tier surfaces the urgency without paraphrasing the divine speech itself
- Aspect: 1:3 perfect participle ποιησάμενος (having made purification) = completed, decisive act
    before the session; rendered as pluperfect sequence in English; 2:14 aorist κεκοινώνηκεν
    (shared) = completed entry into human solidarity; 3:14 perfect γεγόναμεν (we have become) =
    past act with present standing — "we have come to share" and "we remain" distinguished
- "Brethren" (G80 ἀδελφοί): L keeps "brethren" (traditional); M/T use "brothers and sisters"
    to reflect the inclusive Gk. plural that addressed mixed congregations
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
  "1": {
    "1": {
      "L": "In many portions and in many ways God spoke long ago to the fathers by the prophets,",
      "M": "Long ago, at many times and in many ways, God spoke to our fathers through the prophets,",
      "T": "In ages past, through the prophets and in many installments and many modes, God spoke to our ancestors."
    },
    "2": {
      "L": "in these last days he has spoken to us by a Son, whom he appointed heir of all things, through whom also he made the ages.",
      "M": "but in these last days he has spoken to us by his Son, whom he appointed heir of all things, through whom also he made the universe.",
      "T": "But in these final days he has spoken to us through a Son—the one he appointed heir of all things, and through whom he created the very ages themselves."
    },
    "3": {
      "L": "who, being the radiance of his glory and the express image of his person, upholding all things by the word of his power, having made purification for sins, sat down at the right hand of Majesty on high,",
      "M": "He is the radiance of God's glory and the exact representation of his nature, upholding all things by the word of his power. After he had made purification for sins, he sat down at the right hand of the Majesty on high,",
      "T": "This Son is the outshining of God's glory and the precise imprint of his very being. He sustains all creation by his mighty word. Having himself accomplished the purification of sins, he took his seat at the right hand of the Majesty in the heavens—"
    },
    "4": {
      "L": "having become so much better than the angels as he has inherited a name more excellent than they.",
      "M": "having become as much superior to the angels as the name he has inherited is more excellent than theirs.",
      "T": "—having become as far above the angels as the name he has inherited surpasses theirs."
    },
    "5": {
      "L": "For to which of the angels did he ever say, 'Thou art my Son, today I have begotten thee'? Or again, 'I will be to him a Father, and he shall be to me a Son'?",
      "M": "For to which of the angels did God ever say, 'You are my Son; today I have begotten you'? Or again, 'I will be his Father, and he will be my Son'?",
      "T": "After all, to which angel did God ever say, 'You are my Son—today I have brought you forth as my own'? Or again, 'I will be his Father and he will be my Son'?"
    },
    "6": {
      "L": "And again, when he brings the firstborn into the inhabited world, he says, 'Let all God's angels worship him.'",
      "M": "And again, when he brings the firstborn into the world, he says, 'Let all God's angels worship him.'",
      "T": "And when God brings the Firstborn into the world, he commands: 'Let all the angels of God worship him.'"
    },
    "7": {
      "L": "And of the angels he says, 'Who makes his angels spirits and his ministers a flame of fire.'",
      "M": "Regarding the angels he says, 'He makes his angels winds and his ministers a flame of fire.'",
      "T": "Of the angels he says, 'He turns his angels into winds and his servants into flames of fire.'"
    },
    "8": {
      "L": "But of the Son he says, 'Thy throne, O God, is forever and ever, and the scepter of righteousness is the scepter of thy kingdom.'",
      "M": "But about the Son he says: 'Your throne, O God, is forever and ever, and the scepter of righteousness is the scepter of your kingdom.'",
      "T": "But to the Son he says: 'Your throne, O God, endures forever and ever—the royal scepter of your kingdom is a scepter of righteousness.'"
    },
    "9": {
      "L": "Thou hast loved righteousness and hated iniquity; therefore God, thy God, hath anointed thee with the oil of gladness above thy fellows.",
      "M": "You have loved righteousness and hated wickedness; therefore God, your God, has anointed you with the oil of gladness beyond your companions.",
      "T": "You loved what was right and hated lawlessness—so your God has anointed you with gladness beyond all who share your rank."
    },
    "10": {
      "L": "And, 'Thou, Lord, didst lay the foundations of the earth in the beginning, and the heavens are the works of thy hands.'",
      "M": "He also says: 'In the beginning, Lord, you laid the foundations of the earth, and the heavens are the work of your hands.'",
      "T": "And again: 'You, Lord, founded the earth at the beginning; the heavens are the work of your hands.'"
    },
    "11": {
      "L": "They will perish, but thou remainest; and they all will become old like a garment,",
      "M": "They will perish, but you remain; they will all wear out like a garment.",
      "T": "They will decay and vanish, but you remain. They will grow threadbare as a cloak—"
    },
    "12": {
      "L": "and like a mantle thou wilt roll them up, and like a garment they shall be changed; but thou art the same, and thy years shall not fail.",
      "M": "You will roll them up like a robe; like a garment they will be changed. But you are the same, and your years will never end.",
      "T": "—and like a worn-out robe you will fold them away; they are replaced like old clothes. But you are always the same, and your years will never run out."
    },
    "13": {
      "L": "But to which of the angels has he ever said, 'Sit at my right hand until I make thy enemies a footstool for thy feet'?",
      "M": "To which of the angels has God ever said, 'Sit at my right hand until I make your enemies a footstool for your feet'?",
      "T": "Has God ever told any angel, 'Take your seat at my right hand while I make your enemies your footstool'? Never."
    },
    "14": {
      "L": "Are they not all ministering spirits sent out for service on behalf of those who are to inherit salvation?",
      "M": "Are not all angels ministering spirits sent to serve those who will inherit salvation?",
      "T": "What are all these angels? They are servants—spiritual beings dispatched to minister to those who are destined to receive salvation."
    }
  },
  "2": {
    "1": {
      "L": "Therefore we must give more earnest heed to the things we have heard, lest we drift away.",
      "M": "We must therefore pay the closest attention to what we have heard, so that we do not drift away.",
      "T": "This is why we must hold fast with all our might to what we have heard, so that it does not slip through our fingers."
    },
    "2": {
      "L": "For if the word spoken through angels proved reliable, and every transgression and disobedience received a just recompense,",
      "M": "For if the message declared through angels was reliable, and every transgression and act of disobedience received a just penalty,",
      "T": "The law delivered through angels stood firm: every violation and act of defiance earned the punishment it deserved."
    },
    "3": {
      "L": "how shall we escape if we neglect so great a salvation? It was first declared by the Lord, and it was attested to us by those who heard.",
      "M": "how shall we escape if we neglect such a great salvation? This salvation was first announced by the Lord, then confirmed to us by those who heard him.",
      "T": "So how will we escape if we ignore a salvation as vast as this one? It was first spoken by the Lord himself, then confirmed to us by eyewitnesses."
    },
    "4": {
      "L": "God also bearing witness with them by signs and wonders and various miracles and by gifts of the Holy Spirit distributed according to his own will.",
      "M": "while God confirmed their message with signs, wonders, various miracles, and gifts of the Holy Spirit distributed according to his will.",
      "T": "God himself confirmed this message with signs and wonders and all kinds of miracles, and by distributing the gifts of the Holy Spirit as he chose."
    },
    "5": {
      "L": "For he did not subject to angels the world to come, of which we speak.",
      "M": "God did not subject the coming world—the world we are speaking about—to angels.",
      "T": "After all, the coming age—the one we are talking about—was not placed under the control of angels."
    },
    "6": {
      "L": "But someone has testified somewhere, saying, 'What is man that thou art mindful of him, or the son of man that thou visitest him?'",
      "M": "But there is a place where someone has testified: 'What is man that you are mindful of him, or the son of man that you care for him?'",
      "T": "But someone has written this testimony, and it is worth heeding: 'What is a human being, that you keep him in mind? What is a son of man, that you attend to him?'"
    },
    "7": {
      "L": "Thou madest him a little lower than the angels; thou crownedst him with glory and honor, and didst set him over the works of thy hands.",
      "M": "You made him a little lower than the angels; you crowned him with glory and honor and set him over the works of your hands.",
      "T": "You made him for a time lower than the angels, then crowned him with glory and honor and placed him in charge of all your handiwork."
    },
    "8": {
      "L": "putting all things in subjection under his feet.' For in subjecting all things to him, he left nothing unsubjected to him. But now we do not yet see all things subjected to him.",
      "M": "'You have put everything under his feet.' In putting everything under him, God left nothing that is not subject to him. Yet at present we do not see everything subject to him.",
      "T": "—'you placed everything in subjection under his feet.' When God says 'everything,' that means nothing is excluded. Yet we do not see everything subjected to him at the present time."
    },
    "9": {
      "L": "But we see Jesus, who was made a little lower than the angels, now crowned with glory and honor because of the suffering of death, so that by the grace of God he might taste death for everyone.",
      "M": "But we do see Jesus—who was made a little lower than the angels—now crowned with glory and honor because he suffered death, so that by God's grace he might taste death for everyone.",
      "T": "What we do see is Jesus—made lower than the angels for a brief time, and now crowned with glory and honor precisely because he suffered death. By God's grace he tasted death on behalf of everyone."
    },
    "10": {
      "L": "For it was fitting for him, for whom are all things and through whom are all things, in bringing many sons to glory, to make the pioneer of their salvation perfect through sufferings.",
      "M": "It was fitting that God, for whom and through whom all things exist, should make the pioneer of their salvation perfect through suffering, in bringing many sons and daughters to glory.",
      "T": "It was entirely fitting that God—the one for whose sake and through whose power all things exist—should bring many children to glory by making the trailblazer of their salvation complete through suffering."
    },
    "11": {
      "L": "For both he who sanctifies and those who are sanctified are all from one; for which reason he is not ashamed to call them brethren,",
      "M": "Both the one who sanctifies and those who are sanctified have the same Father. That is why Jesus is not ashamed to call them brothers and sisters,",
      "T": "The one who makes people holy and the people he makes holy share the same origin—which is why he is not ashamed to call them his brothers and sisters."
    },
    "12": {
      "L": "saying, 'I will declare thy name to my brethren; in the midst of the congregation I will sing praise to thee.'",
      "M": "He says: 'I will proclaim your name to my brothers and sisters; in the midst of the assembly I will sing your praise.'",
      "T": "He says: 'I will make your name known to my brothers and sisters; I will sing your praise in the midst of the gathered community.'"
    },
    "13": {
      "L": "And again, 'I will put my trust in him.' And again, 'Behold, I and the children God has given me.'",
      "M": "He also says, 'I will trust in him.' And again, 'Here am I and the children God has given me.'",
      "T": "'My confidence is in him.' And again: 'Here I stand, with the children God has entrusted to me.'"
    },
    "14": {
      "L": "Since therefore the children share in flesh and blood, he himself likewise partook of the same, so that through death he might destroy him who had the power of death, that is, the devil,",
      "M": "Since the children share in flesh and blood, he himself likewise took part in these, so that through death he might destroy the one who holds the power of death—that is, the devil—",
      "T": "Since the children are made of flesh and blood, he too shared the same humanity—so that by dying he might break the power of the one who wields death, that is, the devil,"
    },
    "15": {
      "L": "and might deliver all those who through fear of death were subject to lifelong slavery.",
      "M": "and free all those who all their lives had been held in slavery by their fear of death.",
      "T": "and set free all who had lived their entire lives as slaves to the dread of dying."
    },
    "16": {
      "L": "For surely he does not take hold of angels, but he takes hold of the seed of Abraham.",
      "M": "For surely it is not angels he helps, but Abraham's descendants.",
      "T": "He did not come to aid angels—he came to take hold of the seed of Abraham."
    },
    "17": {
      "L": "Therefore he was obliged to be made like his brethren in all things, so that he might become a merciful and faithful high priest in things pertaining to God, to make propitiation for the sins of the people.",
      "M": "For this reason he had to be made like his brothers and sisters in every way, in order that he might become a merciful and faithful high priest before God, and make atonement for the sins of the people.",
      "T": "This is why he had to become fully human in every respect—so that he could serve as a compassionate and trustworthy high priest before God and make the atoning sacrifice that covers his people's sins."
    },
    "18": {
      "L": "For because he himself suffered when tempted, he is able to help those who are being tempted.",
      "M": "Because he himself suffered when he was tempted, he is able to help those who are being tempted.",
      "T": "He suffered through temptation himself, and that is exactly why he can come to the aid of those who face it now."
    }
  },
  "3": {
    "1": {
      "L": "Wherefore, holy brethren, partakers of a heavenly calling, consider the Apostle and High Priest of our confession, Jesus,",
      "M": "Therefore, holy brothers and sisters who share in the heavenly calling, consider carefully Jesus, the Apostle and High Priest of our confession.",
      "T": "So then, brothers and sisters set apart for God, partners in a calling that reaches into heaven—fix your eyes on Jesus, the one we confess as our Apostle and High Priest."
    },
    "2": {
      "L": "who was faithful to him who appointed him, as Moses also was faithful in all his house.",
      "M": "He was faithful to the one who appointed him, just as Moses was faithful in all God's house.",
      "T": "He was faithful to the one who commissioned him—just as Moses was faithful in all of God's household."
    },
    "3": {
      "L": "For this man has been counted worthy of more glory than Moses, inasmuch as the builder of a house has more honor than the house.",
      "M": "But Jesus has been found worthy of greater honor than Moses—just as the builder of a house deserves more honor than the house itself.",
      "T": "Jesus, however, deserves far more glory than Moses—in the way a builder is more honored than the building he constructs."
    },
    "4": {
      "L": "For every house is built by someone, but God is the builder of all things.",
      "M": "Every house is built by someone, but God is the builder of everything.",
      "T": "Every house is built by someone—and the builder of all things is God."
    },
    "5": {
      "L": "And Moses was faithful in all his house as a servant, for a testimony of those things which were to be spoken afterward.",
      "M": "Moses was faithful as a servant in all God's house, giving testimony to what would be said in the future.",
      "T": "Moses served faithfully throughout God's entire household—as an attendant, bearing witness to what was yet to be announced."
    },
    "6": {
      "L": "but Christ was faithful over his own house as a son, whose house we are, if we hold fast the confidence and the rejoicing of hope firm unto the end.",
      "M": "But Christ is faithful as the Son over God's house. And we are his house, if we hold firmly to our confidence and the hope in which we glory.",
      "T": "Christ, however, serves not as an attendant but as a Son over God's own house. And we are that house—provided we hold firmly to the confident hope we began with."
    },
    "7": {
      "L": "Wherefore as the Holy Spirit says, 'Today if ye will hear his voice,",
      "M": "So, as the Holy Spirit says: 'Today, if you hear his voice,",
      "T": "So, as the Holy Spirit says—and this word is for today: 'If you hear his voice,"
    },
    "8": {
      "L": "do not harden your hearts, as in the provocation, in the day of the temptation in the wilderness,",
      "M": "do not harden your hearts as you did in the rebellion, on the day of testing in the wilderness,",
      "T": "do not harden your hearts as your ancestors did in the rebellion, on that day of testing in the wilderness."
    },
    "9": {
      "L": "where your fathers tried and tested me and saw my works for forty years.",
      "M": "where your ancestors tested and tried me, though they saw my works for forty years.",
      "T": "That is where your ancestors tested and provoked me, even though they had watched what I did for forty years."
    },
    "10": {
      "L": "Therefore I was grieved with that generation and said, 'They always err in their heart, and they have not known my ways.'",
      "M": "That is why I was angry with that generation; I said, 'Their hearts are always going astray, and they have not known my ways.'",
      "T": "And so I grew angry with that generation: 'Their hearts are forever wandering off course; they have never come to know my ways.'"
    },
    "11": {
      "L": "As I swore in my wrath, 'They shall not enter into my rest.'",
      "M": "So I swore in my anger, 'They shall never enter my rest.'",
      "T": "So I swore in my anger: 'They will never enter into my rest.'"
    },
    "12": {
      "L": "Take heed, brethren, lest there be in any of you an evil heart of unbelief, in departing from the living God.",
      "M": "See to it, brothers and sisters, that none of you has a sinful, unbelieving heart that turns away from the living God.",
      "T": "Watch yourselves, brothers and sisters: let none of you harbor a faithless, hardened heart that turns away from the living God."
    },
    "13": {
      "L": "But exhort one another daily, while it is called 'Today,' lest any of you be hardened through the deceitfulness of sin.",
      "M": "But encourage one another daily, as long as it is called 'Today,' so that none of you may be hardened by sin's deceitfulness.",
      "T": "Instead, keep encouraging one another every single day—as long as today is still today—so that sin's deceptions don't slowly callous your heart."
    },
    "14": {
      "L": "For we have become partakers of Christ, if we hold firm the beginning of our confidence steadfast unto the end,",
      "M": "We have come to share in Christ, if indeed we hold our original conviction firmly to the very end.",
      "T": "We have become partners with Christ—but only if we hold firmly to what we were confident in at the start, all the way to the finish."
    },
    "15": {
      "L": "while it is said, 'Today if ye will hear his voice, do not harden your hearts as in the provocation.'",
      "M": "As it has just been said: 'Today, if you hear his voice, do not harden your hearts as you did in the rebellion.'",
      "T": "The word stands: 'Today, if you hear his voice, do not harden your hearts as in that old rebellion.'"
    },
    "16": {
      "L": "For who, having heard, did provoke? Was it not all who came out of Egypt by Moses?",
      "M": "Who were they who heard and rebelled? Were they not all those Moses led out of Egypt?",
      "T": "Who were the ones who heard and still rebelled? All who followed Moses out of Egypt—every last one of them."
    },
    "17": {
      "L": "And with whom was he grieved forty years? Was it not with those who had sinned, whose carcases fell in the wilderness?",
      "M": "And with whom was God angry for forty years? Was it not with those who sinned, whose bodies perished in the wilderness?",
      "T": "And who was it that provoked his anger for forty years? Those who had sinned—whose bodies were left scattered in the wilderness."
    },
    "18": {
      "L": "And to whom did he swear that they would not enter his rest, but to those who were disobedient?",
      "M": "And to whom did God swear that they would never enter his rest if not to those who disobeyed?",
      "T": "And to whom did he swear that they would never enter his rest? To those who refused to obey."
    },
    "19": {
      "L": "So we see that they could not enter in because of unbelief.",
      "M": "So we see that they were unable to enter because of their unbelief.",
      "T": "The conclusion is plain: they could not enter because they would not believe."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'hebrews')
        merge_tier(existing, HEBREWS, tier_key)
        save(tier_dir, 'hebrews', existing)
    print('Hebrews 1–3 written.')

if __name__ == '__main__':
    main()
