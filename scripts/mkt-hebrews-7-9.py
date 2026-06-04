"""
MKT Hebrews chapters 7–9 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-hebrews-7-9.py

Translation decisions:
- G3198 (Μελχισεδέκ): "Melchizedek" (modern English form, not KJV "Melchisedec") throughout all tiers.
- G1242 (διαθήκη): context-split rendering — "covenant" in relational/promise contexts (7:22, 8:6-13,
  9:1, 9:4, 9:15, 9:18-20); "will" in 9:16-17 where the author explicitly activates the testament/testator
  sense (the Greek word carries both meanings and the argument in 9:15-17 deliberately pivots on this
  dual meaning). T tier in 9:15 introduces both senses with a bridge phrase.
- G5048 (τελειόω / perfect): "perfect" as both adjective and verb; "bring to perfection/completion" where
  the goal sense is strongest. Key to the letter's argument: the law "made nothing perfect" (7:19, 9:9);
  Christ's priestly work and the Son himself are "made perfect" or are "perfect" (7:26-28).
- G749 (ἀρχιερεύς): "high priest" throughout; no variation.
- G2409 (ἱερεύς): "priest" throughout.
- G2420 (ἱερωσύνη): "priesthood" throughout.
- G4151 (πνεῦμα): "Holy Spirit" in 9:8 (the Spirit signifies through the tabernacle structure);
  "eternal Spirit" in 9:14 (Christ offered himself through the eternal Spirit, not a human impulse).
  Both capitalised — clearly divine Spirit in both contexts. Consistent with 2 Timothy conventions.
- G166 (αἰώνιος): "eternal" throughout — quality of age-to-come life; consistent with prior NT scripts.
- G2435 (ἱλαστήριον): "mercy seat" in 9:5 — this is the Ark's cover (kapporet), not the "propitiation"
  sense of Romans 3:25. Context is tabernacle furniture description; "atonement cover" used in T tier
  to surface the function.
- G2962 (κύριος): "Lord" throughout — consistent with all prior NT scripts.
- G1343 (δικαιοσύνη): "righteousness" in 7:2 (Melchizedek's name-meaning "king of righteousness").
- G629 (ἀπολύτρωσις): "redemption" in 9:12, 9:15 — holistic liberation/ransom, not merely legal.
- G3316 (μεσίτης): "mediator" in 8:6, 9:15.
- G2537 (καινός): "new" throughout (new covenant) — not merely recent but qualitatively new order.
- Aspect notes: aorist verbs rendered as completed acts; perfect tenses as past-act with present-result
  (e.g. 7:26 "has been made higher"; 9:12 "having obtained"). Present tenses (7:25, 8:1) as ongoing.
- OT echoes: 7:17, 7:21 quote Psalm 110:4; 8:8-12 is extended quotation of Jeremiah 31:31-34;
  9:19-20 echo Exodus 24:6-8. All identified in T tier.
- Textual note: 9:4 — the placement of the golden incense altar "in" the Most Holy Place is debated
  (cf. 1 Kings 6:22; some understand "belonging to" rather than physically located in); translation
  follows the interlinear and traditional reading without comment in the verse itself.
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
  "7": {
    "1": {
      "L": "For this Melchizedek, king of Salem, priest of God the Most High, who met Abraham returning from the slaughter of the kings and blessed him,",
      "M": "This Melchizedek was king of Salem and priest of God Most High. He met Abraham returning from the defeat of the kings and blessed him,",
      "T": "Consider who Melchizedek was: king of Salem, priest of the Most High God. When Abraham was coming back from the battle where he defeated the coalition of kings, Melchizedek met him and blessed him."
    },
    "2": {
      "L": "to whom also Abraham apportioned a tenth part of all. He is first, being interpreted, King of Righteousness, and then also King of Salem, that is, King of Peace,",
      "M": "and Abraham gave him a tenth of everything. First, his name means 'king of righteousness'; then also 'king of Salem' means 'king of peace'.",
      "T": "Abraham gave him a tenth of all the spoils. His very name carries a message: 'Melchizedek' means 'king of righteousness,' and his city 'Salem' means 'peace.' His kingship thus encompasses both righteousness and peace."
    },
    "3": {
      "L": "without father, without mother, without genealogy, having neither beginning of days nor end of life, but made like the Son of God, he remains a priest in perpetuity.",
      "M": "He is without father or mother, without genealogy, without beginning of days or end of life, made to resemble the Son of God. He remains a priest forever.",
      "T": "He appears in the record without father, without mother, without any genealogy — no recorded birth, no recorded death. In this way he resembles the Son of God, and like the Son of God, he remains a priest forever."
    },
    "4": {
      "L": "Now consider how great this man was, to whom the patriarch Abraham gave a tenth of the spoils.",
      "M": "Just think how great he was: Even the patriarch Abraham gave him a tenth of the plunder!",
      "T": "Think carefully about the scale of Melchizedek's greatness. Abraham — the founding patriarch of the entire covenant people — gave him a tithe from the battlefield spoils."
    },
    "5": {
      "L": "And those of the sons of Levi who receive the priestly office have a commandment by the law to collect tithes from the people, that is, from their brothers, even though these come from the loins of Abraham.",
      "M": "Now the law requires the descendants of Levi who become priests to collect a tenth from the people—that is, from their fellow Israelites—even though they also are descended from Abraham.",
      "T": "Under the Mosaic law, the Levitical priests hold the standing command to collect tithes from their fellow Israelites — and this, even though those paying the tithe are also children of Abraham, just as the priests themselves are."
    },
    "6": {
      "L": "But this man, whose descent is not counted from them, has received tithes from Abraham and has blessed the one who had the promises.",
      "M": "This man, however, did not trace his descent from Levi, yet he collected a tenth from Abraham and blessed him who had the promises.",
      "T": "But Melchizedek is not from Levi's line at all — and yet he received a tithe from Abraham himself. What is more, he blessed the very man who held the divine promises."
    },
    "7": {
      "L": "But without any dispute, the lesser is blessed by the greater.",
      "M": "And without doubt the lesser is blessed by the greater.",
      "T": "No one can dispute this: the one who gives the blessing stands above the one who receives it."
    },
    "8": {
      "L": "Here mortal men receive tithes; there, however, one receives them of whom it is testified that he lives.",
      "M": "In the one case, the tenth is collected by people who die; but in the other case, by him who is testified to be living.",
      "T": "Under the Levitical system, the tithe goes to men who will die. But Melchizedek received his tithe from Abraham, and the record simply bears this witness: he lives."
    },
    "9": {
      "L": "And, so to speak, through Abraham even Levi, who receives tithes, has paid tithes,",
      "M": "One might even say that Levi, who collects the tenth, paid the tenth through Abraham,",
      "T": "We could even say, in a manner of speaking, that Levi himself — ancestor of all the tithe-collecting priests — paid tithes that day through Abraham."
    },
    "10": {
      "L": "for he was still in the loins of his father when Melchizedek met him.",
      "M": "because when Melchizedek met Abraham, Levi was still in the body of his ancestor.",
      "T": "After all, Levi had not yet been born — he was still, as it were, inside Abraham when Melchizedek met and blessed him. The entire priestly line was present in their forefather."
    },
    "11": {
      "L": "Now if perfection were through the Levitical priesthood—for under it the people received the law—what further need was there for another priest to arise after the order of Melchizedek, and not be called after the order of Aaron?",
      "M": "If perfection could have been attained through the Levitical priesthood—and indeed the law was given to the people on the basis of that priesthood—why was there still need for another priest to come, one in the order of Melchizedek, not in the order of Aaron?",
      "T": "The Levitical priesthood was the very foundation on which the law was administered. But if that system could have brought people to complete wholeness before God, why would scripture ever speak of a different kind of priest — one after the order of Melchizedek, not after the order of Aaron?"
    },
    "12": {
      "L": "For when the priesthood is changed, there is necessarily a change in the law as well.",
      "M": "For when the priesthood is changed, the law must be changed also.",
      "T": "The implication is sweeping: if the priesthood changes, the whole legal structure built upon it changes with it."
    },
    "13": {
      "L": "For the one of whom these things are spoken belongs to another tribe, from which no one has ministered at the altar.",
      "M": "He of whom these things are said belonged to a different tribe, and no one from that tribe has ever served at the altar.",
      "T": "The priest the scriptures are describing here came from an entirely different tribe — one that has never provided a single altar priest."
    },
    "14": {
      "L": "For it is evident that our Lord descended from Judah, and in regard to that tribe Moses said nothing about priests.",
      "M": "For it is clear that our Lord descended from Judah, and in regard to that tribe Moses said nothing about priests.",
      "T": "We know perfectly well that our Lord came from the tribe of Judah. Moses never said a word about Judah furnishing priests. The whole Levitical framework has therefore been left behind."
    },
    "15": {
      "L": "And this is yet more evident, since another priest arises in the likeness of Melchizedek,",
      "M": "And what we have said is even more clear if another priest like Melchizedek appears,",
      "T": "The point becomes even clearer when we see that the new priest who has arisen bears the pattern of Melchizedek."
    },
    "16": {
      "L": "who has become a priest, not according to a law of fleshly commandment, but according to the power of an indestructible life.",
      "M": "one who has become a priest not on the basis of a regulation about his ancestry but on the basis of the power of an indestructible life.",
      "T": "He did not become a priest by a legal rule about physical descent. He became a priest by the power of a life that cannot be destroyed."
    },
    "17": {
      "L": "For it is testified, 'You are a priest forever, after the order of Melchizedek.'",
      "M": "For it is declared: 'You are a priest forever, in the order of Melchizedek.'",
      "T": "The testimony is clear — Psalm 110:4 says it plainly: 'You are a priest forever, in the order of Melchizedek.'"
    },
    "18": {
      "L": "For there is indeed a setting aside of a former commandment because of its weakness and uselessness",
      "M": "The former regulation is set aside because it was weak and useless",
      "T": "The old commandment has been set aside — not from any outside pressure, but because of its inherent weakness and ineffectiveness."
    },
    "19": {
      "L": "(for the law made nothing perfect), but a better hope is introduced, through which we draw near to God.",
      "M": "(for the law made nothing perfect), and a better hope is introduced, by which we draw near to God.",
      "T": "The law could not bring anyone to wholeness before God. Instead, a better hope has been opened up — and through this hope we can actually draw near to God himself."
    },
    "20": {
      "L": "And to the degree it was not without an oath—for those who became priests did so without an oath,",
      "M": "And it was not without an oath. The others became priests without any oath,",
      "T": "Notice also that Jesus' priesthood was established with an oath. The Levitical priests received their office with no oath at all —"
    },
    "21": {
      "L": "but this one with an oath by the one who said to him, 'The Lord has sworn and will not change his mind, You are a priest forever,'",
      "M": "but he became a priest with an oath when God said to him: 'The Lord has sworn and will not change his mind: You are a priest forever.'",
      "T": "but Jesus was installed by God's own oath. God declared it and will never revoke it: 'The Lord has sworn and will not change his mind: you are a priest forever' (Ps 110:4). The oath makes all the difference."
    },
    "22": {
      "L": "by so much also Jesus has become the guarantor of a better covenant.",
      "M": "Because of this oath, Jesus has become the guarantor of a better covenant.",
      "T": "Because of that unbreakable divine oath, Jesus stands as the guarantee of a covenant that is genuinely better than the old."
    },
    "23": {
      "L": "And indeed those who became priests were many, because death prevented them from remaining in office;",
      "M": "Now there were many of those priests, since death prevented them from continuing in office;",
      "T": "Under the old system there had to be many priests in succession, because death kept cutting them off."
    },
    "24": {
      "L": "but he, because he remains forever, holds his priesthood permanently.",
      "M": "but because Jesus lives forever, he has a permanent priesthood.",
      "T": "But Jesus lives forever, so his priesthood is permanent — it will never pass to another."
    },
    "25": {
      "L": "Hence also he is able to save to the uttermost those who draw near to God through him, since he always lives to make intercession for them.",
      "M": "Therefore he is able to save completely those who come to God through him, because he always lives to intercede for them.",
      "T": "This means he is able to save — completely, permanently, without limit — everyone who comes to God through him. He is always alive to intercede for them. The case never closes."
    },
    "26": {
      "L": "For it was fitting for us to have such a high priest: holy, blameless, undefiled, separated from sinners, and made higher than the heavens.",
      "M": "Such a high priest truly meets our need — one who is holy, blameless, pure, set apart from sinners, exalted above the heavens.",
      "T": "This is exactly the kind of high priest we need: holy in character, blameless in conduct, unstained by sin, utterly set apart from sinners — and then lifted high above the heavens themselves."
    },
    "27": {
      "L": "He has no need to offer sacrifices daily as those high priests do, first for his own sins and then for those of the people; for this he did once for all when he offered up himself.",
      "M": "Unlike the other high priests, he does not need to offer sacrifices day after day, first for his own sins, and then for the sins of the people. He sacrificed for their sins once for all when he offered himself.",
      "T": "Unlike the Levitical high priests, he does not come back day after day with fresh offerings — first for his own failures, then for the people's. He did this once and settled it forever: he offered himself."
    },
    "28": {
      "L": "For the law appoints men as high priests who have weakness, but the word of the oath, which came after the law, appoints a Son, made perfect forever.",
      "M": "For the law appoints as high priests men in all their weakness; but the oath, which came after the law, appointed the Son, who has been made perfect forever.",
      "T": "The law installed men surrounded by weakness; but the divine oath — which came later and superseded the law — installed the Son: consecrated, perfected, and permanent."
    }
  },
  "8": {
    "1": {
      "L": "Now the chief point in what we are saying is this: we have such a high priest, who has taken his seat at the right hand of the throne of the Majesty in the heavens,",
      "M": "Now the main point of what we are saying is this: We do have such a high priest, who sat down at the right hand of the throne of the Majesty in heaven,",
      "T": "Here is the heart of everything we have been building toward: we have exactly this kind of high priest — and he has taken his seat at the right hand of the Majesty on high."
    },
    "2": {
      "L": "a minister of the sanctuary and of the true tent that the Lord pitched, not man.",
      "M": "and who serves in the sanctuary, the true tabernacle set up by the Lord, not by a mere human being.",
      "T": "He is the minister of the true sanctuary — the real tabernacle, the one the Lord himself erected, not any human craftsman."
    },
    "3": {
      "L": "For every high priest is appointed to offer gifts and sacrifices; therefore it is necessary for this one also to have something to offer.",
      "M": "Every high priest is appointed to offer both gifts and sacrifices, and so it was necessary for this one also to have something to offer.",
      "T": "Every high priest is appointed to bring offerings to God. That means our high priest also needed something to offer."
    },
    "4": {
      "L": "Now if he were on earth, he would not be a priest at all, since there are those who offer gifts according to the law.",
      "M": "If he were on earth, he would not be a priest, for there are already priests who offer the gifts prescribed by the law.",
      "T": "If Jesus were still operating in the earthly realm, he could not even serve as a priest — because the lawful priests are already at work down here."
    },
    "5": {
      "L": "They serve a copy and shadow of the heavenly things. For when Moses was about to erect the tent, he was warned by God, saying, 'See that you make everything according to the pattern shown to you on the mountain.'",
      "M": "They serve at a sanctuary that is a copy and shadow of what is in heaven. This is why Moses was warned when he was about to build the tabernacle: 'See to it that you make everything according to the pattern shown you on the mountain.'",
      "T": "Their sanctuary is only a copy and shadow of the heavenly original. Remember when Moses was about to build the tabernacle — God personally warned him: 'Make sure everything follows the pattern I showed you on the mountain' (Exod 25:40). Even that warning confirms the earthly sanctuary is secondary."
    },
    "6": {
      "L": "But now he has obtained a more excellent ministry, by as much as he is also the mediator of a better covenant, which has been enacted on better promises.",
      "M": "But in fact the ministry Jesus has received is as superior to theirs as the covenant of which he is mediator is superior to the old one, since the new covenant is established on better promises.",
      "T": "But Jesus' ministry surpasses theirs by as much as the new covenant surpasses the old — and it surpasses the old because it rests on better promises."
    },
    "7": {
      "L": "For if that first covenant had been faultless, no place would have been sought for a second.",
      "M": "For if there had been nothing wrong with that first covenant, no place would have been sought for another.",
      "T": "If the first covenant had truly met the need, there would have been no reason to search for a replacement."
    },
    "8": {
      "L": "For finding fault with them he says: 'Behold, the days are coming, declares the Lord, when I will complete a new covenant with the house of Israel and with the house of Judah,'",
      "M": "But God found fault with the people and said: 'The days are coming, declares the Lord, when I will make a new covenant with the people of Israel and with the people of Judah.'",
      "T": "But God himself found fault — not merely with the system in the abstract, but with the people under it — and declared through Jeremiah: 'The time is coming,' says the LORD, 'when I will make a new covenant with Israel and with Judah' (Jer 31:31)."
    },
    "9": {
      "L": "'not like the covenant that I made with their fathers on the day when I took them by the hand to lead them out of the land of Egypt. For they did not continue in my covenant, and I paid them no heed, declares the Lord.'",
      "M": "'It will not be like the covenant I made with their ancestors when I took them by the hand to lead them out of Egypt, because they did not remain faithful to my covenant, and I turned away from them, declares the Lord.'",
      "T": "'It will not be like the Sinai covenant I made with their ancestors when I led them out of Egypt. They broke that covenant, and so I withdrew from them,' says the LORD."
    },
    "10": {
      "L": "'For this is the covenant that I will make with the house of Israel after those days, declares the Lord: I will put my laws into their minds, and on their hearts I will write them, and I will be their God, and they shall be my people.'",
      "M": "'This is the covenant I will establish with the people of Israel after that time, declares the Lord. I will put my laws in their minds and write them on their hearts. I will be their God, and they will be my people.'",
      "T": "'Here is the covenant I will make with Israel when that time comes,' says the LORD: 'I will inscribe my laws in their minds and engrave them on their hearts. I will be their God, and they will be my people.'"
    },
    "11": {
      "L": "'And they shall not teach, each one his neighbor and each one his brother, saying, Know the Lord, for all shall know me, from the least to the greatest.'",
      "M": "'No longer will they teach their neighbor, or say to one another, Know the Lord, because they will all know me, from the least of them to the greatest.'",
      "T": "'Gone will be the days when one person has to instruct another to know the LORD. They will all know me directly — the newest believer as surely as the most seasoned elder.'"
    },
    "12": {
      "L": "'For I will be merciful toward their iniquities, and their sins I will remember no more.'",
      "M": "'For I will forgive their wickedness and will remember their sins no more.'",
      "T": "'I will be merciful to their failures and will never bring their sins to mind again.'"
    },
    "13": {
      "L": "In speaking of a new covenant, he has made the first obsolete. And what is becoming obsolete and growing old is ready to vanish away.",
      "M": "By calling this covenant 'new,' he has made the first one obsolete; and what is obsolete and aging will soon disappear.",
      "T": "The moment God called it 'new,' he declared the first covenant old. And anything grown old and obsolete is already close to disappearing entirely."
    }
  },
  "9": {
    "1": {
      "L": "Now the first covenant also had regulations for worship and an earthly sanctuary.",
      "M": "Now the first covenant had regulations for worship and also an earthly sanctuary.",
      "T": "The first covenant, for all its limitations, did have its own system of worship and its own earthly sacred space."
    },
    "2": {
      "L": "For a tent was prepared, the first section, in which were the lampstand and the table and the presentation bread; it is called the Holy Place.",
      "M": "A tabernacle was set up. In its first room were the lampstand and the table with its consecrated bread; this was called the Holy Place.",
      "T": "A great tent was constructed. In its outer room stood the lampstand, the table, and the sacred loaves of the Presence — this was called the Holy Place."
    },
    "3": {
      "L": "And behind the second curtain was a second tent called the Most Holy Place,",
      "M": "Behind the second curtain was a room called the Most Holy Place,",
      "T": "Beyond a second curtain lay the innermost room — the Most Holy Place."
    },
    "4": {
      "L": "having the golden altar of incense and the ark of the covenant overlaid on all sides with gold, in which were a golden urn holding the manna, and Aaron's staff that budded, and the tablets of the covenant.",
      "M": "This room had the golden altar of incense and the gold-covered ark of the covenant. Inside the ark were the golden jar of manna, Aaron's staff that had budded, and the stone tablets of the covenant.",
      "T": "In that innermost room stood the golden altar of incense and the ark of the covenant — overlaid all over with gold. Inside the ark were three things: the golden jar of manna, Aaron's rod that once bloomed to life, and the stone tablets on which the covenant had been inscribed."
    },
    "5": {
      "L": "Above it were the cherubim of glory overshadowing the mercy seat. Of these things we cannot now speak in detail.",
      "M": "Above the ark were the cherubim of the Glory, overshadowing the atonement cover. But we cannot discuss these things in detail now.",
      "T": "Crowning it all were the cherubim of God's glory, wings spread over the mercy seat — the atonement cover. This is not the moment to go into all the significance of each."
    },
    "6": {
      "L": "Now with these things thus prepared, the priests enter the first tent regularly, performing their priestly duties.",
      "M": "When everything had been arranged like this, the priests entered regularly into the outer room to carry on their ministry.",
      "T": "Once the tabernacle was fully set up and furnished, the priests went about their daily work in the outer room on a regular basis."
    },
    "7": {
      "L": "But into the second, only the high priest enters, and but once a year, and not without blood, which he offers for himself and for the unintentional sins of the people.",
      "M": "But only the high priest entered the inner room, and only once a year, and never without blood, which he offered for himself and for the sins the people had committed in ignorance.",
      "T": "The inner room was a different matter entirely. Only the high priest could enter, and only on one day in the entire year — the Day of Atonement — and never without blood to offer for his own failures and for the people's unintentional sins."
    },
    "8": {
      "L": "The Holy Spirit is indicating this: the way into the holy place has not yet been opened while the first tent is still standing.",
      "M": "The Holy Spirit was showing by this that the way into the Most Holy Place had not yet been disclosed as long as the first tabernacle was still functioning.",
      "T": "The Holy Spirit was saying something through this entire arrangement: as long as that outer tent remained standing, the way into God's very presence had not yet been thrown open."
    },
    "9": {
      "L": "(which is a parable for the present age), in accordance with which gifts and sacrifices are offered that cannot perfect the conscience of the worshiper.",
      "M": "This is an illustration for the present time, indicating that the gifts and sacrifices being offered were not able to clear the conscience of the worshiper.",
      "T": "That outer tent stands as a parable for our age — pointing to a deeper reality not yet reached. The offerings brought under that system could not do the fundamental work: they could not clear the worshiper's conscience before God."
    },
    "10": {
      "L": "but only deal with foods and drinks and various washings, fleshly regulations imposed until the time of reformation.",
      "M": "They are only a matter of food and drink and various ceremonial washings — external regulations applying until the time of the new order.",
      "T": "They were purely external regulations — food rules, drink rules, various ritual washings for the body. All of them were holding patterns, imposed until the time came for God to set everything right."
    },
    "11": {
      "L": "But when Christ appeared as a high priest of the good things that have come, through the greater and more perfect tent not made with hands, that is, not of this creation,",
      "M": "But when Christ came as high priest of the good things that are now already here, he went through the greater and more perfect tabernacle that is not made with human hands, that is to say, is not a part of this creation.",
      "T": "But when Christ arrived as high priest of the good things God has now brought about, he passed through a greater and more perfect tent — not constructed by human hands, not belonging to this created order at all."
    },
    "12": {
      "L": "he entered once for all into the holy place, not by means of the blood of goats and calves but by means of his own blood, thus securing an eternal redemption.",
      "M": "He did not enter by means of the blood of goats and calves; but he entered the Most Holy Place once for all by his own blood, thus obtaining eternal redemption.",
      "T": "He entered the holy place once for all — not carrying the blood of goats and calves as the high priest carried each year, but carrying his own blood. In doing so he secured a redemption that will never expire."
    },
    "13": {
      "L": "For if the blood of goats and bulls, and the sprinkling of defiled persons with the ashes of a heifer, sanctify for the purification of the flesh,",
      "M": "The blood of goats and bulls and the ashes of a heifer sprinkled on those who are ceremonially unclean sanctify them so that they are outwardly clean.",
      "T": "Consider the old system: the blood of bulls and goats, and the ashes of a slaughtered heifer sprinkled on the ritually unclean — these purified the body, making a person outwardly fit for worship."
    },
    "14": {
      "L": "how much more will the blood of Christ, who through the eternal Spirit offered himself without blemish to God, purify our conscience from dead works to serve the living God?",
      "M": "How much more, then, will the blood of Christ, who through the eternal Spirit offered himself unblemished to God, cleanse our consciences from acts that lead to death, so that we may serve the living God!",
      "T": "If those outward washings could cleanse the body, how much more can the blood of Christ? He offered himself without blemish to God through the eternal Spirit — and his blood purges the conscience itself, removing the deadening weight of fruitless works so that we can serve the living God in real freedom."
    },
    "15": {
      "L": "For this reason he is the mediator of a new covenant, so that those who are called may receive the promised eternal inheritance, since a death has occurred that redeems them from the transgressions committed under the first covenant.",
      "M": "For this reason Christ is the mediator of a new covenant, that those who are called may receive the promised eternal inheritance — now that he has died as a ransom to set them free from the sins committed under the first covenant.",
      "T": "This is why he is the mediator of a new covenant: so that all who are called may receive the eternal inheritance God has promised. His death accomplished this — it ransomed those trapped under the guilt of the first covenant, so they could go free."
    },
    "16": {
      "L": "For where a will is, there must of necessity be the death of the one who made it.",
      "M": "In the case of a will, it is necessary to establish the death of the one who made it,",
      "T": "Think about how a will works: a will only comes into effect after its maker has died."
    },
    "17": {
      "L": "for a will is in force only at death, since it is never in force while the one who made it is alive.",
      "M": "because a will is in force only when somebody has died; it never takes effect while the one who made it is living.",
      "T": "A will has no legal force while the testator still lives. Death is what activates it."
    },
    "18": {
      "L": "Therefore not even the first covenant was inaugurated without blood.",
      "M": "This is why even the first covenant was not put into effect without blood.",
      "T": "This is the pattern running through all of history: even the first covenant required death — blood — before it became operative."
    },
    "19": {
      "L": "For when every commandment of the law had been spoken by Moses to all the people, he took the blood of calves and goats, with water and scarlet wool and hyssop, and sprinkled both the book itself and all the people,",
      "M": "When Moses had proclaimed every commandment of the law to all the people, he took the blood of calves, together with water, scarlet wool and branches of hyssop, and sprinkled the scroll and all the people.",
      "T": "When Moses had finished reading every commandment of the law to the assembled people, he took blood — of calves and goats, mixed with water, applied with scarlet wool and hyssop branches — and sprinkled both the scroll and the entire congregation (Exod 24:6-8)."
    },
    "20": {
      "L": "saying, 'This is the blood of the covenant that God commanded for you.'",
      "M": "He said, 'This is the blood of the covenant, which God has commanded you to keep.'",
      "T": "'This is the blood of the covenant,' he announced — 'the covenant God has ordained for you.'"
    },
    "21": {
      "L": "And in the same way he sprinkled with the blood both the tent and all the vessels of the ministry.",
      "M": "In the same way, he sprinkled with the blood both the tabernacle and everything used in its ceremonies.",
      "T": "He did the same to the tabernacle itself and to every vessel used in worship — they too were sprinkled with blood."
    },
    "22": {
      "L": "And under the law almost everything is cleansed with blood, and without the shedding of blood there is no forgiveness.",
      "M": "In fact, the law requires that nearly everything be cleansed with blood, and without the shedding of blood there is no forgiveness.",
      "T": "The law makes this plain: almost everything requires blood for cleansing. And behind that requirement stands an absolute principle — without the shedding of blood, there is no forgiveness."
    },
    "23": {
      "L": "It was therefore necessary for the copies of the things in the heavens to be purified with these rites, but the heavenly things themselves with better sacrifices than these.",
      "M": "It was necessary, then, for the copies of the heavenly things to be purified with these sacrifices, but the heavenly things themselves with better sacrifices than these.",
      "T": "So the earthly copies of the heavenly sanctuary needed to be cleansed with animal blood. But the heavenly originals — the real sanctuary — required better sacrifices altogether."
    },
    "24": {
      "L": "For Christ has entered, not into holy places made with hands, copies of the true things, but into heaven itself, now to appear in the presence of God on our behalf.",
      "M": "For Christ did not enter a sanctuary made with human hands that was only a copy of the true one; he entered heaven itself, now to appear for us in God's presence.",
      "T": "Christ did not enter some human-made sanctuary that was merely a copy of the real. He entered heaven itself — and he stands there now, in God's own presence, as our representative."
    },
    "25": {
      "L": "nor was it to offer himself repeatedly, as the high priest enters the holy place every year with blood not his own,",
      "M": "Nor did he enter heaven to offer himself again and again, the way the high priest enters the Most Holy Place every year with blood that is not his own.",
      "T": "And he did not go there to keep offering himself over and over — the way the earthly high priest entered the sanctuary each year carrying someone else's blood."
    },
    "26": {
      "L": "for then he would have had to suffer repeatedly since the foundation of the world. But as it is, he has appeared once for all at the end of the ages to put away sin by the sacrifice of himself.",
      "M": "Otherwise Christ would have had to suffer many times since the creation of the world. But he has appeared once for all at the culmination of the ages to do away with sin by the sacrifice of himself.",
      "T": "If repetition were required, he would have had to die again and again from the very beginning of creation. Instead, he appeared once — at this great turning point in history — to abolish sin once for all by offering himself."
    },
    "27": {
      "L": "And just as it is appointed for men to die once, and after that comes judgment,",
      "M": "Just as people are destined to die once, and after that to face judgment,",
      "T": "Every human being faces one death, and after that one judgment — that is the appointed order for everyone."
    },
    "28": {
      "L": "so Christ, having been offered once to bear the sins of many, will appear a second time, not to deal with sin but to save those who are eagerly waiting for him.",
      "M": "so Christ was sacrificed once to take away the sins of many; and he will appear a second time, not to bear sin, but to bring salvation to those who are waiting for him.",
      "T": "Christ's story follows the same shape: he was offered once, bearing the sins of many in that single act. He will appear a second time — not to deal with sin again, for that is finished — but to bring full salvation to those who are watching for him."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'hebrews')
        merge_tier(existing, HEBREWS, tier_key)
        save(tier_dir, 'hebrews', existing)
    print('Hebrews 7–9 written.')

if __name__ == '__main__':
    main()
