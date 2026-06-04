"""
MKT 1 Chronicles chapter 29 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-1chronicles-29-29.py

Content:
- Ch 29: David's final address and personal gift (vv. 1–5); leaders' freewill offerings (vv. 6–9);
  David's great prayer of praise (vv. 10–19); congregational worship and Solomon's anointing (vv. 20–22);
  Solomon's accession and David's death (vv. 23–30)

Translation decisions:
- H3068 (יהוה): "LORD" in L/M; "the LORD" in T. Consistent with all prior 1 Chronicles scripts.
- H430 (אֱלֹהִים): "God" throughout all tiers.
- H1002 (בִּירָה, birah): "palace" — the Chronicler uses this citadel/fortress term specifically for the
  temple complex, distinct from בַּיִת (bayit, "house"). Retained throughout to honour its architectural
  register.
- H5068/H5071 (נָדַב/נְדָבָה, nadab/nedavah): "willingly" / "freewill" in L/M; T surfaces the theological
  weight — this is the spirit of voluntary devotion that the entire chapter celebrates. L/M: "offered
  willingly"; T: "gave freely" or "willing devotion."
- H1420 (גְּדֻלָּה, gedullah): "greatness" — L/M/T.
- H1369 (גְּבוּרָה, gevurah): "power" — L/M/T (consistent with prior scripts using "might/power").
- H8597 (תִּפְאֶרֶת, tifaret): "glory" — L/M/T.
- H5331 (נֵצַח, netsach): "victory" in the doxology (v. 11) — L/M/T.
- H1935 (הוֹד, hod): "majesty" — L/M/T.
- H4467 (מַמְלָכָה, mamlakah): "kingdom" — L/M/T.
- H3678 (כִּסֵּא, kisse') + v. 23 "throne of the LORD" (כִּסֵּא יהוה): Rendered literally. The Chronicler's
  distinctive language — not David's throne or Solomon's throne, but God's throne — signals that the
  king is God's regent. T notes this explicitly at v. 23.
- H2617 (חֶסֶד): does not appear in ch. 29; no override needed.
- H1616/H8453 (גֵּר/תּוֹשָׁב, ger/toshav): "strangers / sojourners" in L/M; T preserves the covenantal
  weight of these terms — Israel is always resident-alien before God, never proprietary owner of life
  or wealth.
- H3336 (יֵצֶר, yetser): "the thoughts" / "intention" of the heart (v. 18). The yetser is the deep
  inclination or orientation of the inner person; same root used in Gen 6:5 for the evil inclination.
  Here it is the whole-hearted devotion of the people. L: "imagination of the thoughts"; M: "disposition";
  T: "the deep intent."
- H4723 (מִקְוֶה, miqveh): "abiding" / "permanence" (v. 15) — "there is none abiding"; T: "no
  permanence, no tenure."
- H150 (אֲדַרְכּוֹן, adarkon) at v. 7: a daric, Persian gold coin. The Chronicler uses contemporary
  currency; L/M note this as "drams/gold coins"; T acknowledges the term.
- Aspect: David's speech uses qatals for completed acts of preparation and imperfects with waw-
  consecutive for narrative. David's prayer moves between completed past gifts (qatal) and imperative
  petitions. Maintained in all tiers.
- OT intertextuality:
  - v. 11 doxology: echoed in the Lord's Prayer (Matt 6:13, "yours is the kingdom and the power and
    the glory"). T notes this at v. 11.
  - v. 15 "our days are as a shadow": Ps 102:11; Ps 144:4; Job 8:9. A pervasive OT theme of human
    transience before the eternal God.
  - v. 18 "God of Abraham, Isaac, and Israel": the covenant-oath formula grounding the prayer in the
    foundational patriarchal covenant.
  - v. 23 "throne of the LORD": anticipates the Davidic-messianic throne theology of Psalm 2, 110,
    and the NT's identification of Jesus as the Davidic heir.
  - v. 28 "full of days, riches, and honor": the covenantal blessing of a completed life (cf. Gen 25:8,
    Abraham "full of years"; Job 42:17).
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

CHRONICLES1 = {
  "29": {
    "1": {
      "L": "Furthermore David the king said to all the congregation: 'Solomon my son, whom alone God has chosen, is young and tender, and the work is great; for the palace is not for man but for the LORD God.'",
      "M": "King David addressed the whole assembly: 'My son Solomon, the one whom God alone has chosen, is young and inexperienced. The task ahead is immense, because this palace is not for human beings — it is for the LORD God.'",
      "T": "David addressed the full assembly of Israel with the weight of his final years behind him. 'Solomon my son — chosen by God himself, and by no one else — is young and still untested, and the work before him is immense. This is not an ordinary building project. This is a house for the LORD God. Nothing about it should be approached as ordinary, and Solomon cannot carry it alone.'"
    },
    "2": {
      "L": "Now I have prepared with all my might for the house of my God: gold for things of gold, silver for things of silver, bronze for things of bronze, iron for things of iron, and wood for things of wood; onyx stones and stones to be set, glistering stones and stones of divers colours, and all manner of precious stones, and marble stones in abundance.",
      "M": "With all my strength I have prepared for the house of my God: gold for gold work, silver for silver work, bronze for bronze work, iron for iron work, and wood for woodwork — onyx stones and setting stones, sparkling and colored stones, all kinds of precious stones, and marble in great quantity.",
      "T": "I have poured everything I have into preparing for the house of my God — every strength, every resource, every ounce of energy these aging hands could give. Gold matched to gold work, silver to silver, bronze to bronze, iron to iron, wood to wood. And stones: onyx and stones for setting, glittering mosaic-tiles and jewels of many colors, every variety of precious stone, marble in abundance. Nothing was held back because nothing less than everything belonged to this work."
    },
    "3": {
      "L": "Moreover, because I have set my affection on the house of my God, I have given of my own personal goods to the house of my God, over and above all that I have prepared for the holy house: gold and silver.",
      "M": "Furthermore, because of my devotion to the house of my God, I give from my own personal treasury — over and above everything else I have already prepared for the holy house — gold and silver.",
      "T": "Beyond all the public preparations — beyond every royal stockpile and national resource — I am giving from my own private holdings, the treasure that belongs to me personally, because my heart is set on the house of my God. The official preparations seemed inadequate. So I am adding what is mine alone."
    },
    "4": {
      "L": "Three thousand talents of gold, of the gold of Ophir, and seven thousand talents of refined silver, to overlay the walls of the houses;",
      "M": "Three thousand talents of Ophir gold and seven thousand talents of refined silver, enough to overlay the walls of the sanctuary buildings —",
      "T": "Three thousand talents of Ophir gold — the finest gold the ancient world produced, renowned for its purity — and seven thousand talents of silver refined until no impurity remained, enough to plate the walls of the entire sanctuary complex from floor to ceiling. These are not symbolic gestures; they are staggering quantities drawn from David's own treasury."
    },
    "5": {
      "L": "the gold for things of gold and the silver for things of silver and for all manner of work to be made by the hands of artificers. And who then is willing to consecrate his service this day to the LORD?",
      "M": "gold for all gold work and silver for all silver work, for every kind of crafted item by skilled artisans. Now — who is willing to consecrate himself in service to the LORD today?",
      "T": "Gold for gold-work, silver for silver-work, raw material for every artisan's craft. But then David paused and asked the real question — not the financial one but the personal one: 'Who is willing to give himself? Not just his wealth, but his whole devoted service, consecrated to the LORD today?' The giving of treasure matters only when the heart behind it is given first."
    },
    "6": {
      "L": "Then the chief men and the princes and the captains of thousands and of hundreds, with the rulers of the king's work, offered willingly.",
      "M": "Then the family leaders, the princes, the commanders of thousands and hundreds, and the officers of the king's work all gave willingly.",
      "T": "The response was immediate and total. The chiefs, the princes, the military commanders of thousands and hundreds, the royal officials — every rank of Israel's leadership gave freely and without compulsion, swept into the current of David's own willingness. No one had to be persuaded twice."
    },
    "7": {
      "L": "And they gave for the service of the house of God five thousand talents of gold and ten thousand drams, and of silver ten thousand talents, and of brass eighteen thousand talents, and of iron a hundred thousand talents.",
      "M": "For the service of the house of God they contributed: five thousand talents and ten thousand gold coins of gold, ten thousand talents of silver, eighteen thousand talents of bronze, and a hundred thousand talents of iron.",
      "T": "The totals poured in: five thousand talents of gold plus ten thousand darics — the Persian coin already circulating as currency, marking the Chronicler's own era — ten thousand talents of silver, eighteen thousand of bronze, a hundred thousand of iron. An entire temple's worth of materials assembled in a single day's voluntary giving by Israel's leadership, returned to God from wealth God had given them in the first place."
    },
    "8": {
      "L": "And those who had precious stones gave them to the treasure of the house of the LORD, by the hand of Jehiel the Gershonite.",
      "M": "Those who possessed precious stones gave them to the treasury of the house of the LORD, entrusted to Jehiel the Gershonite.",
      "T": "Whoever held precious stones added them to the LORD's treasury, placing them in the care of Jehiel the Gershonite, the appointed keeper of the sacred storehouse. The entire nation was emptying its finest possessions into the service of God's house. Not one category of wealth was withheld."
    },
    "9": {
      "L": "Then the people rejoiced, for that they offered willingly, because with perfect heart they offered willingly to the LORD; and David the king also rejoiced with great joy.",
      "M": "The people rejoiced because their leaders had given so willingly and wholeheartedly to the LORD. And King David was filled with great joy.",
      "T": "The people caught fire. They rejoiced with great gladness because their leaders had given with whole, undivided hearts — freely, without pressure, without calculation. The willingness was the thing. It was not reluctant duty scaled to obligation; it was love overflowing into open hands. David himself wept and rejoiced. The scene was a foretaste of what the temple would one day be: a people wholly given, offering their best because their hearts belonged to the LORD."
    },
    "10": {
      "L": "Wherefore David blessed the LORD before all the congregation; and David said, 'Blessed are you, LORD, God of Israel our father, from everlasting to everlasting.'",
      "M": "David blessed the LORD in the sight of the whole assembly. He said, 'Blessed are you, LORD, God of our father Israel, from everlasting to everlasting.'",
      "T": "David stood before all Israel and blessed the LORD. What followed is one of the great prayers of the Hebrew Bible — a meditation on sovereignty, transience, and grace that has shaped Jewish and Christian worship ever since:\n\n'Blessed are you, LORD, God of Israel our father — from before the ages to beyond the ages. You are the eternity within which our brief lives are held, and we worship you from within our small portion of it.'"
    },
    "11": {
      "L": "Yours, O LORD, is the greatness and the power and the glory and the victory and the majesty, for all that is in the heaven and in the earth is yours. Yours, O LORD, is the kingdom, and you are exalted as head above all.",
      "M": "'Yours, LORD, is the greatness and the power and the glory and the victory and the majesty — everything in heaven and earth belongs to you. Yours, LORD, is the kingdom; you are exalted as head over all.'",
      "T": "'Yours, LORD, is the greatness — greater than any claim we could make in your honor. Yours is the power — stronger than any force we could assemble. Yours is the glory — our gold and silver only faintly reflects what you already possess. Yours is the victory — every battle Israel has ever won, you won through us. Yours is the majesty — no crown in the ancient world sits higher than yours. Everything in heaven and earth belongs to you. The kingdom is yours; the throne belongs to you; you reign as head above all that exists.' This prayer would echo in the mouths of Jesus' disciples: 'Yours is the kingdom and the power and the glory, forever' (Matt 6:13)."
    },
    "12": {
      "L": "Both riches and honor come from you, and you rule over all. In your hand is power and might, and in your hand it is to make great and to give strength to all.",
      "M": "'Riches and honor come from you alone, and you rule over all. Strength and might are in your hand, and it is yours to make great and to give strength to all.'",
      "T": "'Even what we brought today — the gold, the silver, the bronze, the precious stones — it all came from your hand in the first place. Riches belong to you; honor is yours to give and to withhold. You are the ruler of everything. Every strength is a gift from you, every greatness is your doing, every increase in power is what you have poured out. We are conduits, not sources.'"
    },
    "13": {
      "L": "Now therefore, our God, we thank you and praise your glorious name.",
      "M": "'Now therefore, our God, we give you thanks and praise your glorious name.'",
      "T": "'So what can we do but give thanks? We have nothing to offer that was not first yours to give. We stand before you with empty hands and full hearts, and we praise the glory of your name — a name that stands above every name that has ever received tribute from the nations of the earth.'"
    },
    "14": {
      "L": "But who am I, and what is my people, that we should be able to offer so willingly after this sort? For all things come of you, and of your own have we given you.",
      "M": "'But who am I, and who are my people, that we should be able to give so willingly? Everything comes from you, and we have given you only what came from your own hand.'",
      "T": "'But who am I — truly, who am I? And what is this people? We have no strength, no wealth, no capacity to give except what you have first given us. This entire day's offering — every talent of gold and silver, every precious stone, every pledge of willing service — came to us from you. We are returning it to the one to whom it already belongs. We cannot be generous with what was never ours.'"
    },
    "15": {
      "L": "For we are strangers before you and sojourners, as were all our fathers. Our days on the earth are as a shadow, and there is none abiding.",
      "M": "'For we are strangers and sojourners before you, as all our ancestors were. Our days on earth pass like a shadow, and there is no permanence.'",
      "T": "'We are, before you, exactly what our fathers were: strangers passing through, resident aliens on the earth who have no permanent title to anything. Our days are a shadow — cast briefly when the light stands at one angle, then gone when it shifts. No generation abides here. None of us holds tenure. We are all moving through the same landscape toward the same destination, bringing nothing into the world and taking nothing out. The wealth we gathered and gave today was borrowed from your hand; we only ever held it in trust.'"
    },
    "16": {
      "L": "O LORD our God, all this store that we have prepared to build you a house for your holy name comes from your hand, and is all your own.",
      "M": "'O LORD our God, all this abundance we have gathered to build a house for your holy name — it all came from your hand. It is entirely yours.'",
      "T": "'LORD our God — this entire mountain of resources: the gold, the silver, the bronze, the iron, the timber, the stone, all of it prepared for the house of your holy name — every last piece came from your hand to ours and back to yours again. We are intermediaries in a transaction that begins and ends with you. The house will bear your name because the materials were always yours and the name is yours alone.'"
    },
    "17": {
      "L": "I know also, my God, that you test the heart and have pleasure in uprightness. As for me, in the uprightness of my heart I have willingly offered all these things; and now I have seen with joy your people, who are present here, offering willingly to you.",
      "M": "'I also know, my God, that you examine the heart and delight in integrity. With an honest heart I have freely offered all these things. And now I have watched with joy as your people present here have given to you so willingly.'",
      "T": "'And I know something else, my God: you are not impressed by the totals. You test the heart. What you look for is not the size of the gift but the quality of the soul behind it. You delight in uprightness — in hearts that give without calculation, without display, without the hidden wish to be seen. That is what I have tried to do today: give from honest love, not from the desire for honor. And I have watched your people do the same. They gave willingly — not from pressure, not from fear, but from hearts that are genuinely and freely yours. That is the thing that fills me with joy today more than all the gold and silver combined.'"
    },
    "18": {
      "L": "O LORD, God of Abraham, Isaac, and Israel, our fathers, keep this for ever in the imagination of the thoughts of the heart of your people, and prepare their heart unto you;",
      "M": "'LORD, God of Abraham, Isaac, and Israel, our fathers — keep this disposition forever in the hearts and minds of your people, and turn their hearts toward you.'",
      "T": "'LORD, God of Abraham, of Isaac, of Israel — the God who has kept covenant through every generation of our fathers: do not let what I have seen today be a single unrepeated moment. Guard the deep intent of their hearts. The willingness the people have shown today — this whole-hearted giving, this open-handed devotion — keep it alive in them. Cultivate it. Let it be the settled orientation of their hearts toward you, not just today but forever. And beyond that: turn their hearts to you. Willingness in giving is the beginning; union with you is the end for which you made them.'"
    },
    "19": {
      "L": "And give unto Solomon my son a perfect heart, to keep your commandments, your testimonies, and your statutes, and to do all these things, and to build the palace, for which I have made provision.",
      "M": "'Give my son Solomon an undivided heart to keep your commandments, your decrees, and your statutes — to carry out everything needed and to build the palace for which I have made all these preparations.'",
      "T": "'And my son Solomon — give him a heart that is wholly, undividedly yours. Not a heart split between God and ambition, between worship and self-interest, between the commandments and convenience. A heart that keeps your commandments, that lives by your testimonies, that honors your statutes — not out of fear or routine but from the same depth of devotion I have tried to offer today. And give him the wisdom and will to build the house for which I have prepared everything. The materials are ready. The workers are ready. Let the king who builds it have a heart that makes the building mean what it is supposed to mean.'"
    },
    "20": {
      "L": "And David said to all the congregation, 'Now bless the LORD your God.' And all the congregation blessed the LORD, the God of their fathers, and bowed down their heads and worshipped the LORD and the king.",
      "M": "David told the whole assembly, 'Now bless the LORD your God.' The entire assembly blessed the LORD, the God of their ancestors, and bowed their heads, prostrating themselves before the LORD and before the king.",
      "T": "David turned from prayer to proclamation: 'Now — bless the LORD your God.' And all Israel did exactly that. Every head bowed. Every person prostrated themselves before the LORD, the God of their fathers. They had heard David's prayer; they had watched their leaders give beyond what anyone expected; and now they worshiped together — all at once, faces to the ground before the LORD and his anointed king. The prayer was not a private matter; it ended in a congregation on its knees."
    },
    "21": {
      "L": "And they sacrificed sacrifices to the LORD and offered burnt offerings to the LORD on the morrow after that day, even a thousand bullocks, a thousand rams, and a thousand lambs, with their drink offerings, and sacrifices in abundance for all Israel.",
      "M": "The next day they made offerings to the LORD: a thousand bulls, a thousand rams, and a thousand lambs as burnt offerings, along with their drink offerings, and abundant sacrifices for all Israel.",
      "T": "The next day, the celebration continued in worship. A thousand bulls, a thousand rams, a thousand lambs — all as burnt offerings ascending to the LORD — plus drink offerings poured out beside every sacrifice, and peace offerings in abundance for all Israel. The entire nation ate and drank before the LORD in the gladness of covenant feast. What had begun in David's prayer of praise ended in a great meal before the LORD's presence. The whole sequence — gift, prayer, worship, feast — was Israel at its best."
    },
    "22": {
      "L": "And they did eat and drink before the LORD on that day with great gladness. And they made Solomon the son of David king the second time, and anointed him to the LORD to be the chief governor, and Zadok to be priest.",
      "M": "They ate and drank before the LORD that day with great joy. Then they made David's son Solomon king a second time, anointing him before the LORD as ruler, and Zadok as priest.",
      "T": "The feast was before the LORD — not a private royal banquet but a covenant meal in God's presence, overflowing with gladness. And in the midst of the celebration, Solomon was formally anointed king for the second time. The first public declaration had come when David was still active (1 Chr 23:1); this second anointing was the solemn, ceremonial confirmation before all Israel's assembled leadership at the end of the greatest day of voluntary worship the nation had known. Alongside Solomon, Zadok was anointed as high priest — the man who would serve through the entire Solomonic era. Two anointings: king and priest together. The succession was sealed before God and all Israel."
    },
    "23": {
      "L": "Then Solomon sat on the throne of the LORD as king in place of David his father, and prospered; and all Israel obeyed him.",
      "M": "Solomon sat on the LORD's throne as king in place of his father David. He prospered, and all Israel obeyed him.",
      "T": "Solomon ascended — not to David's throne but to the throne of the LORD. The Chronicler's language is deliberate and precise: this is God's throne, held by God's king, administered on God's behalf. The king of Israel is not a sovereign in his own right but the LORD's regent, holding the kingdom in trust. Solomon prospered. And all Israel obeyed — not the grudging submission of a subdued people but the willing allegiance of a nation that had just worshiped together and understood what God's anointed meant for them."
    },
    "24": {
      "L": "And all the princes and the mighty men, and all the sons also of King David, submitted themselves to Solomon the king.",
      "M": "All the princes, all the warriors, and all of King David's other sons submitted themselves to King Solomon.",
      "T": "Even the potential rivals submitted: the princes, the military elite, and all of David's other sons — any of whom might have pressed a claim to the throne — placed themselves under Solomon's authority without resistance. The transition had been declared from heaven (17:12), prepared by earth across this entire chapter, and sealed by the submission of every possible competitor. There would be no Adonijah-style rival claim in the Chronicler's account. The kingdom was whole, and it was the LORD's doing."
    },
    "25": {
      "L": "And the LORD magnified Solomon exceedingly in the sight of all Israel, and bestowed upon him such royal majesty as had not been on any king before him in Israel.",
      "M": "The LORD gave Solomon extraordinary greatness in the sight of all Israel, bestowing on him a royal majesty beyond anything any previous king of Israel had possessed.",
      "T": "This was the LORD's doing, not Israel's politics: Solomon was exalted with a royal splendor that made even David's glory seem like its precursor. No king before him in Israel had sat on a throne so elevated, so confirmed, so publicly celebrated in a single assembled act of worship and national acclamation. God had promised it through David in chapter 17 ('I will establish his kingdom forever'); here that promise stood visible before all eyes. The exaltation came from God; Solomon's task was to bear it faithfully."
    },
    "26": {
      "L": "Thus David the son of Jesse reigned over all Israel.",
      "M": "Thus David son of Jesse reigned over all Israel.",
      "T": "So ends the reign of David son of Jesse. He had come from the sheepfolds of Bethlehem, been anointed by Samuel when his own father did not think to include him in the lineup, survived Saul's jealousy across a decade as an outlaw, united the tribes of Israel, brought the ark of the covenant to Jerusalem in a procession of great joy, received the eternal covenant from the LORD's own word through Nathan, subdued every surrounding nation, and prepared the temple of God down to its last beam and stone. He reigned over all Israel."
    },
    "27": {
      "L": "And the time that he reigned over Israel was forty years: seven years he reigned in Hebron and thirty-three years he reigned in Jerusalem.",
      "M": "He reigned over Israel for forty years: seven in Hebron and thirty-three in Jerusalem.",
      "T": "Forty years of kingship: seven in Hebron, where Judah crowned him first while the north still answered to Saul's house; and thirty-three in Jerusalem, the city David had taken from the Jebusites and made the capital of united Israel, the city where the ark of the LORD now rested and where the throne of the LORD would permanently stand."
    },
    "28": {
      "L": "Then he died in a good old age, full of days, riches, and honor; and Solomon his son reigned in his place.",
      "M": "He died at a ripe old age, full of years, wealth, and honor. His son Solomon succeeded him as king.",
      "T": "He died well. 'Full of days' — the covenant blessing of a long life completed under God's hand (cf. Gen 25:8, Abraham 'full of years'; Job 42:17). 'Full of riches' — the wealth that had poured through his hands into God's treasury rather than into his own monuments. 'Full of honor' — the glory that comes from being faithful to an extraordinary calling across a long and eventful life. The man who began behind his father's flock ended having given his people a kingdom, a covenant, and a temple half-built. Solomon his son sat in his place."
    },
    "29": {
      "L": "Now the acts of David the king, first and last, behold, they are written in the book of Samuel the seer, and in the book of Nathan the prophet, and in the book of Gad the seer.",
      "M": "The acts of King David, from first to last, are recorded in the records of Samuel the seer, in the records of Nathan the prophet, and in the records of Gad the seer.",
      "T": "The Chronicler cites his sources: three prophetic archives that documented David's entire reign. Samuel — who anointed David when he was still a boy and lived to see him established in Hebron. Nathan — who delivered the Davidic covenant and who later confronted David with the word that interrupted his worst moment (2 Sam 12). Gad — the seer who had been with David since the outlaw years in the wilderness (1 Sam 22:5) and who delivered God's word during the plague of chapter 21. Every era of David's life had its prophet; every act was witnessed by a man who understood that what he was recording was not merely the political history of a Near Eastern monarchy but the outworking of God's covenant with his people."
    },
    "30": {
      "L": "With all his reign and his might, and the times that went over him and over Israel and over all the kingdoms of the countries.",
      "M": "This encompassed everything about his reign and his power, and the events that came upon him and upon Israel and upon all the surrounding kingdoms.",
      "T": "The full record encompassed it all: his reign, his power, and every event that swept over him and over Israel — the times of exile and return, the seasons of war and peace, the kingdoms of every land whose histories intersected with his. David had not lived in isolation; his story was woven into the story of the ancient Near East. Every nation that came under his hand, every alliance and confrontation, every moment when the covenant promise pressed against the pressures of surrounding empires — all of it witnessed, all of it written, all of it carrying the pattern of a God who was working through a shepherd-king to establish his kingdom on the earth."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '1chronicles')
        merge_tier(existing, CHRONICLES1, tier_key)
        save(tier_dir, '1chronicles', existing)
    print('1 Chronicles 29 written.')

if __name__ == '__main__':
    main()
