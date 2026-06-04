"""
MKT Hebrews chapters 4–6 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-hebrews-4-6.py

Translation decisions:
- G2663 κατάπαυσις (rest): "rest" in all tiers throughout chs 4–6. The Septuagint term
    deliberately echoes Gen 2:2 and Ps 95:11. "Rest" is retained even in T because the
    theological layering (creation rest → Canaan rest → eschatological rest) is exactly
    what the author intends; paraphrasing would collapse the typology.
- G4520 σαββατισμός (4:9 only — hapax): "sabbath rest" in L; "sabbath-rest" in M/T.
    The author coins this word to distinguish the eschatological rest from κατάπαυσις.
    In T: "God's sabbath rest" to surface the divine origin explicitly.
- G3056 λόγος (4:12): "word" in all tiers. This is the Hebrew dabar sense — God's
    spoken/written word as active agent — not the Greek philosophical Logos. No deviation.
- G166 αἰώνιος (5:9 "eternal salvation"; 6:2 "eternal judgment"): "eternal" in L/M.
    In T at 5:9: "salvation that belongs to the age to come" to surface the eschatological
    quality (life of the coming age, not merely unending duration). At 6:2: "eternal
    judgment" retained in T — the final judgment's permanence is the point.
- G4151 πνεῦμα (6:4): "Holy Spirit" (capitalized) in all tiers. Context is unambiguous:
    the community gift given at conversion (μετόχους πνεύματος ἁγίου).
- G4102 πίστις (6:1, 12): "faith" in all tiers — the trusting, loyal allegiance that
    characterises covenant relationship. At 6:1, "faith toward God" (not "faith in God")
    to preserve the directional πρὸς τὸν θεόν idiom. At 6:12, paired with patience.
- G26 ἀγάπη / G25 ἀγαπάω (6:10): "love" in all tiers — the willed, covenant-keeping
    love that showed itself in service, not mere sentiment.
- G1343 δικαιοσύνη (5:13 "word of righteousness"): "righteousness" in L/M; "righteous
    instruction" in T — the phrase refers to mature doctrinal content about God's
    righteous character and how his people are to live.
- G3954 παρρησία (4:16): "boldly" (L), "confidence" (M), "boldly, with full access" (T).
    The term denotes the citizen's right of free speech before authority — in T this
    access-language is surfaced to match the temple/throne-room imagery.
- Melchizedek (5:6, 10; 6:20): Transliterated as "Melchizedek" (not Melchisedec) in all
    tiers — matching the established spelling in HEB-1a for consistency across chapters.
- 5:5–6 quotations: Ps 2:7 and Ps 110:4 quoted verbatim. Both are rendered as Scripture
    quotations using em-dash framing in M/T.
- 6:4–6 apostasy warning: Rendered straight in all tiers. "Impossible" (ἀδύνατον) is not
    softened to "very difficult." In T, the framing makes explicit that these are people
    who participated in every covenant blessing, so the gravity is maximised, not reduced.
- 6:13–14 oath to Abraham quotes Gen 22:17 LXX. The Hebrew infinitive absolute ("blessing
    I will bless, multiplying I will multiply") is preserved in L as emphatic repetition;
    M uses "surely" to convey the force; T uses "absolutely" for contemporary register.
- Aspect: 4:3 present εἰσερχόμεθα ("we are entering" — ongoing, continuous) preserved
    in L/M; 5:7–9 aorists describing Christ's completed earthly acts (offered prayers,
    was heard, learned obedience, was made perfect) — each rendered as a completed act
    in M/T; 6:6 aorists for the falling-away — a completed break.
- "high priest" lowercase throughout — a functional title, not a personal name.
- OT intertextuality: Ch 4 draws on Ps 95 and Gen 2:2; ch 5 on Ps 2:7 and Ps 110:4;
    ch 6 on Gen 22:17. These are quoted or explicitly referenced, so no hidden echoes
    need special surfacing beyond the text itself.
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
  "4": {
    "1": {
      "L": "Let us therefore fear, lest any one of you should seem to fall short of the promise being left of entering into his rest.",
      "M": "Let us therefore be on guard, lest any of you should seem to have fallen short of the promise of entering his rest.",
      "T": "We need to take this seriously: God's promise of entering his rest still stands open, and we dare not let any of us fall short of it."
    },
    "2": {
      "L": "For the good news was preached also to us, just as to them; but the word of hearing did not profit those ones, not having been mixed with faith in those who heard.",
      "M": "For we have had the good news proclaimed to us just as they did; but the message they heard was of no value to them, because it was not combined with faith in those who heard it.",
      "T": "We have heard the same gospel they heard in the wilderness. But for them the message did no good, because when they heard it they did not unite it with faith."
    },
    "3": {
      "L": "For we who have believed are entering the rest, just as he has said: 'As I swore in my wrath, they shall not enter into my rest' — though the works were finished from the foundation of the world.",
      "M": "Now we who have believed are entering that rest, just as God has said: 'As I swore in my anger: they shall never enter my rest.' Yet his rest had been established since the creation of the world.",
      "T": "We who believe are entering the rest. God himself declared: 'I swore in my anger — they will never enter my rest.' Yet that rest existed from the very founding of the world; only their unbelief shut them out."
    },
    "4": {
      "L": "For somewhere he has spoken of the seventh day in this way: 'And God rested on the seventh day from all his works.'",
      "M": "Somewhere in Scripture God spoke about the seventh day in these words: 'And God rested on the seventh day from all his works.'",
      "T": "We know this because Scripture records God speaking about the seventh day: 'On the seventh day God rested from all that he had made.'"
    },
    "5": {
      "L": "And in this place again: 'They shall not enter into my rest.'",
      "M": "And again in this passage: 'They shall never enter my rest.'",
      "T": "And yet the same Scripture returns with its warning: 'They shall not enter my rest.'"
    },
    "6": {
      "L": "Since therefore it remains for some to enter it, and those who formerly received the good news failed to enter in because of disobedience,",
      "M": "Therefore it still remains for some to enter that rest, and since those who formerly had the good news proclaimed to them did not enter because of disobedience,",
      "T": "The door to that rest, then, is still open — someone must yet enter it. Those who first heard the good news were barred by their own disobedience;"
    },
    "7": {
      "L": "he again defines a certain day — 'Today' — saying through David after so long a time, just as it has been said before: 'Today, if you hear his voice, do not harden your hearts.'",
      "M": "God again set a certain day — calling it 'Today' — saying through David much later: 'Today, if you hear his voice, do not harden your hearts.'",
      "T": "so God designated another day, which he called 'Today.' Long after Joshua's generation, he spoke again through David: 'Today, if you hear his voice, do not harden your heart.'"
    },
    "8": {
      "L": "For if Joshua had given them rest, he would not have spoken afterward of another day.",
      "M": "For if Joshua had given them rest, God would not have spoken later about another day.",
      "T": "If Joshua's conquest had truly given the people God's rest, there would have been no need for God to speak of yet another 'today' centuries later."
    },
    "9": {
      "L": "Therefore a sabbath rest remains for the people of God.",
      "M": "There remains, then, a sabbath-rest for the people of God.",
      "T": "The conclusion stands: God's sabbath rest is still waiting for his people."
    },
    "10": {
      "L": "For he who has entered into his rest has also himself rested from his works, just as God rested from his own.",
      "M": "For anyone who enters God's rest also rests from their own work, just as God rested from his.",
      "T": "Whoever enters that rest leaves their own striving behind, just as God rested from the work of creation on the seventh day."
    },
    "11": {
      "L": "Let us therefore give diligence to enter into that rest, lest anyone fall by the same example of disobedience.",
      "M": "Let us make every effort to enter that rest, so that no one will fall by following the same pattern of disobedience.",
      "T": "So let us press hard to enter that rest — determined that none of us will fall away through the same unbelief that destroyed them."
    },
    "12": {
      "L": "For the word of God is living and active, and sharper than any two-edged sword, and piercing even to the dividing of soul and spirit, of both joints and marrow, and a discerner of the thoughts and intentions of the heart.",
      "M": "For the word of God is alive and active. Sharper than any double-edged sword, it penetrates even to dividing soul and spirit, joints and marrow; it judges the thoughts and intentions of the heart.",
      "T": "God's word is a living thing, and it acts. Keener than any two-edged blade, it drives in between soul and spirit, between joint and bone marrow, and lays bare the secret purposes hidden in the heart."
    },
    "13": {
      "L": "And there is no creature invisible before him, but all things are naked and laid bare to the eyes of him with whom we have to do.",
      "M": "Nothing in all creation is hidden from God's sight. Everything is uncovered and laid bare before the eyes of him to whom we must give account.",
      "T": "Nothing in all creation can hide from God. Every creature stands stripped and exposed before the eyes of the one to whom we must ultimately answer."
    },
    "14": {
      "L": "Having therefore a great high priest who has passed through the heavens, Jesus the Son of God, let us hold fast our confession.",
      "M": "Therefore, since we have a great high priest who has passed through the heavens, Jesus the Son of God, let us hold firmly to the faith we profess.",
      "T": "We have a great high priest who has gone ahead of us through the heavens themselves into the very presence of God — Jesus, the Son of God. Let us grip tightly the faith we declare."
    },
    "15": {
      "L": "For we have not a high priest unable to sympathize with our weaknesses, but one who was in all respects tempted as we are, yet apart from sin.",
      "M": "For we do not have a high priest who is unable to empathize with our weaknesses, but we have one who has been tempted in every way, just as we are — yet he did not sin.",
      "T": "Our high priest is not someone who cannot feel for our struggles. He was tested in every way that we are — he knows the full weight of human weakness from the inside — yet he never sinned."
    },
    "16": {
      "L": "Let us therefore draw near with boldness to the throne of grace, that we may receive mercy and may find grace for help in time of need.",
      "M": "Let us then approach God's throne of grace with confidence, so that we may receive mercy and find grace to help us in our time of need.",
      "T": "So let us come boldly to the throne of grace — not cringing but with full access — and there receive mercy and the grace we need, exactly when we need it most."
    }
  },
  "5": {
    "1": {
      "L": "For every high priest taken from among men is appointed on behalf of men in the things pertaining to God, that he may offer both gifts and sacrifices for sins.",
      "M": "Every high priest is selected from among the people and appointed to represent them in matters relating to God, to offer gifts and sacrifices for sins.",
      "T": "Every high priest is taken from ordinary human beings and set apart to stand before God on their behalf — to offer gifts and sacrifices that deal with sin."
    },
    "2": {
      "L": "Who can deal gently with those who are ignorant and going astray, since he himself also is surrounded with weakness.",
      "M": "He is able to deal gently with those who are ignorant and going astray, since he himself is subject to weakness.",
      "T": "Because he shares the same human frailty, he can treat with gentleness those who have wandered or stumbled through ignorance."
    },
    "3": {
      "L": "And because of this he is obligated to offer sacrifices for sins, as for the people, so also for himself.",
      "M": "This is why he has to offer sacrifices for his own sins as well as for the sins of the people.",
      "T": "That same weakness means he must bring sin offerings for himself as well as for the people."
    },
    "4": {
      "L": "And no one takes the honor to himself, but only when called by God, just as Aaron was.",
      "M": "And no one takes this honor on himself, but he receives it when called by God, just as Aaron was.",
      "T": "No one promotes himself to the high priesthood. The honor belongs only to those God himself calls — as he called Aaron."
    },
    "5": {
      "L": "So also Christ did not glorify himself to be made a high priest, but it was he who said to him: 'My Son you are; today I have begotten you.'",
      "M": "In the same way, Christ did not take on himself the glory of becoming a high priest. But God said to him: 'You are my Son; today I have become your Father.'",
      "T": "Christ, too, did not appoint himself as high priest. God gave him that honor — the same God who said to him: 'You are my Son; this day I have declared you to be mine.'"
    },
    "6": {
      "L": "As also in another place he says: 'You are a priest forever after the order of Melchizedek.'",
      "M": "And he says in another place: 'You are a priest forever, in the order of Melchizedek.'",
      "T": "And in another psalm God declares to him: 'You are a priest forever — not in Aaron's line, but in the ancient order of Melchizedek.'"
    },
    "7": {
      "L": "Who in the days of his flesh, having offered up both prayers and supplications with strong crying and tears to him that was able to save him from death, and having been heard for his godly fear,",
      "M": "During the days of Jesus' life on earth, he offered up prayers and petitions with loud cries and tears to the one who could save him from death, and he was heard because of his reverent submission.",
      "T": "In the days when he walked among us in human flesh, Jesus prayed with loud weeping and tears to his Father, who had the power to rescue him from death. The Father heard him — not by sparing him suffering, but in response to his holy and obedient trust."
    },
    "8": {
      "L": "though being a Son, he learned obedience from the things which he suffered.",
      "M": "Though he was the Son, he learned obedience from what he suffered.",
      "T": "He was the Son — and yet he learned what obedience truly costs through the hard school of suffering."
    },
    "9": {
      "L": "and having been made perfect, he became to all those who obey him the cause of eternal salvation,",
      "M": "and once made perfect, he became the source of eternal salvation for all who obey him,",
      "T": "Brought through suffering to the fullness of his calling, he became the sole source of the salvation that belongs to the age to come — for all who submit to him."
    },
    "10": {
      "L": "having been designated by God a high priest after the order of Melchizedek.",
      "M": "and was designated by God to be high priest in the order of Melchizedek.",
      "T": "God himself gave him the title: High Priest in the order of Melchizedek."
    },
    "11": {
      "L": "Concerning whom we have much to say and hard to interpret, since you have become dull of hearing.",
      "M": "We have much to say about this, but it is hard to explain because you are slow to learn.",
      "T": "There is much more we could say on this, but it is not easy to put into words — not because the subject is too deep, but because you have stopped really listening."
    },
    "12": {
      "L": "For when by this time you ought to be teachers, you have need again of someone to teach you the first principles of the oracles of God; and you have come to need milk, and not solid food.",
      "M": "In fact, though by this time you ought to be teachers, you need someone to teach you the elementary truths of God's word all over again. You need milk, not solid food!",
      "T": "By now you should be teaching others. Instead, you need someone to go back to the beginning and re-explain the basic ABCs of God's word. You still need milk — you are not ready for solid food."
    },
    "13": {
      "L": "For everyone who partakes only of milk is without experience of the word of righteousness; for he is a babe.",
      "M": "Anyone who lives on milk is still an infant, unskilled in the teaching about righteousness.",
      "T": "Milk is for infants who have no real experience of what it means to live by God's righteous instruction."
    },
    "14": {
      "L": "But solid food is for the mature, for those who by reason of use have their senses exercised to discern good and evil.",
      "M": "But solid food is for the mature, who by constant use have trained themselves to distinguish good from evil.",
      "T": "Solid food belongs to those who have grown up — people who, through long practice, have sharpened their moral perception to tell right from wrong."
    }
  },
  "6": {
    "1": {
      "L": "Therefore leaving the word of the beginning of Christ, let us press on to maturity, not laying again a foundation of repentance from dead works, and of faith toward God,",
      "M": "Therefore let us leave the elementary teaching about Christ and press forward to maturity, not laying again the foundation of repentance from acts that lead to death, and of faith toward God,",
      "T": "We must leave the elementary ABCs of Christ behind us and press on to full maturity. We cannot keep re-laying the same foundation: turning from dead religious works, trusting in God,"
    },
    "2": {
      "L": "of teaching of washings, and of laying on of hands, and of resurrection of the dead, and of eternal judgment.",
      "M": "the teaching about baptisms, the laying on of hands, the resurrection of the dead, and eternal judgment.",
      "T": "the meaning of baptisms and the laying on of hands, the resurrection of the dead, and the judgment that will last forever."
    },
    "3": {
      "L": "And this will we do, if God permit.",
      "M": "And God permitting, we will do so.",
      "T": "We intend to move forward — with God's help."
    },
    "4": {
      "L": "For it is impossible for those who were once enlightened, and have tasted of the heavenly gift, and were made partakers of the Holy Spirit,",
      "M": "It is impossible for those who have once been enlightened, who have tasted the heavenly gift, who have shared in the Holy Spirit,",
      "T": "Consider those who have received the light, who have tasted the goodness of God's heavenly gift, who have shared in the Holy Spirit,"
    },
    "5": {
      "L": "and have tasted the good word of God and the powers of the age to come,",
      "M": "who have tasted the goodness of the word of God and the powers of the coming age,",
      "T": "who have tasted how good God's word is and experienced the powers that belong to the age to come —"
    },
    "6": {
      "L": "and then have fallen away, it is impossible to renew them again to repentance, seeing they crucify to themselves the Son of God afresh and put him to an open shame.",
      "M": "and who have then fallen away — it is impossible to bring them back to repentance. By falling away they are crucifying the Son of God all over again and subjecting him to public disgrace.",
      "T": "if such people then fall away, it is impossible to bring them back to repentance. In their falling they are crucifying the Son of God for themselves all over again, holding him up to open contempt."
    },
    "7": {
      "L": "For the land that drinks the rain that comes often upon it, and brings forth herbs useful for those for whom it is also tilled, receives blessing from God.",
      "M": "Land that drinks in the rain often falling on it and produces a crop useful to those for whom it is farmed receives the blessing of God.",
      "T": "Think of farmland that soaks up the rain and yields good crops for those who work it — that land receives God's blessing."
    },
    "8": {
      "L": "But if it bears thorns and thistles, it is rejected and nigh unto cursing, whose end is to be burned.",
      "M": "But land that produces thorns and thistles is worthless and in danger of being cursed. In the end it will be burned.",
      "T": "But land that yields only thorns and weeds is rejected, standing on the edge of a curse — its fate is the torch."
    },
    "9": {
      "L": "But, beloved, we are persuaded of better things concerning you, and things that accompany salvation, though we thus speak.",
      "M": "Even though we speak like this, dear friends, we are convinced of better things in your case — things that have to do with salvation.",
      "T": "But dear friends — though we issue these warnings, we are confident that you are on the better path, the one that leads to salvation."
    },
    "10": {
      "L": "For God is not unrighteous to forget your work and the love which you showed toward his name, in that you ministered to the saints, and still do minister.",
      "M": "God is not unjust; he will not forget your work and the love you have shown him as you have helped his people and continue to help them.",
      "T": "God is not the kind to forget. He sees every act of service, every expression of love you have shown in his name by caring for his people — and you have kept at it."
    },
    "11": {
      "L": "And we desire that each one of you may show the same diligence to the fullness of hope even to the end,",
      "M": "We want each of you to show this same diligence to the very end, in order to make your hope sure,",
      "T": "Our deepest desire is that every one of you will keep this same diligent effort all the way to the finish, holding your hope rock-solid,"
    },
    "12": {
      "L": "that you be not sluggish, but imitators of those who through faith and patience inherit the promises.",
      "M": "so that you will not be lazy, but will imitate those who through faith and patience inherit what has been promised.",
      "T": "so that you do not grow sluggish, but follow the example of those who held on through faith and patient endurance until they received what God had promised."
    },
    "13": {
      "L": "For when God made promise to Abraham, since he could swear by none greater, he swore by himself,",
      "M": "When God made his promise to Abraham, since there was no one greater for him to swear by, he swore by himself,",
      "T": "When God made his promise to Abraham, there was no higher authority he could appeal to for confirmation, so he swore by his own name,"
    },
    "14": {
      "L": "saying: 'Surely blessing I will bless you, and multiplying I will multiply you.'",
      "M": "saying: 'I will surely bless you and give you many descendants.'",
      "T": "declaring: 'I will absolutely bless you — and I will multiply your descendants beyond all counting.'"
    },
    "15": {
      "L": "And thus, having patiently endured, he obtained the promise.",
      "M": "And so after waiting patiently, Abraham received what was promised.",
      "T": "Abraham held on, and in the end he received exactly what God had promised."
    },
    "16": {
      "L": "For men swear by the greater, and in every dispute of theirs the oath is final for confirmation.",
      "M": "People swear by someone greater than themselves, and the oath confirms what is said and puts an end to all argument.",
      "T": "Human beings always swear by something higher than themselves, and an oath settles every dispute — it is the final word that ends all argument."
    },
    "17": {
      "L": "Wherein God, being minded to show more abundantly to the heirs of the promise the unchangeableness of his counsel, interposed with an oath,",
      "M": "Because God wanted to make the unchanging nature of his purpose very clear to the heirs of what was promised, he confirmed it with an oath,",
      "T": "Because God wanted to make absolutely certain that those who were to inherit the promise would know beyond all doubt that his purpose could never change, he backed his word with an oath."
    },
    "18": {
      "L": "that by two unchangeable things, in which it is impossible for God to lie, we may have strong consolation, who have fled for refuge to lay hold of the hope set before us.",
      "M": "God did this so that, by two unchangeable things in which it is impossible for God to lie, we who have fled to take hold of the hope set before us may be greatly encouraged.",
      "T": "There are two things that cannot change: God's promise and God's oath. Since it is impossible for God to lie, we who have run to him for refuge can seize the hope set before us with both hands — it will not give way."
    },
    "19": {
      "L": "which hope we have as an anchor of the soul, both sure and steadfast, and which enters into that within the veil,",
      "M": "We have this hope as an anchor for the soul, firm and secure. It enters the inner sanctuary behind the curtain,",
      "T": "This hope is the anchor of our souls — firm, unbreakable. It reaches into the very presence of God, past the curtain that once divided the holiness of God from human approach,"
    },
    "20": {
      "L": "where as a forerunner Jesus entered for us, having become a high priest forever after the order of Melchizedek.",
      "M": "where our forerunner, Jesus, has entered on our behalf. He has become a high priest forever, in the order of Melchizedek.",
      "T": "where Jesus, our forerunner, has already gone in for us — appointed forever as high priest in the order of Melchizedek."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'hebrews')
        merge_tier(existing, HEBREWS, tier_key)
        save(tier_dir, 'hebrews', existing)
    print('Hebrews 4–6 written.')

if __name__ == '__main__':
    main()
