"""
MKT 1 Chronicles chapters 17–22 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-1chronicles-17-22.py

Content:
- Ch 17: The Davidic Covenant — Nathan's oracle and David's prayer of thanksgiving
- Ch 18: David's military victories — Philistines, Moab, Zobah, Syria, Edom
- Ch 19: The Ammonite and Syrian wars — Hanun's insult, two campaigns
- Ch 20: Capture of Rabbah; Philistine giants at Gezer and Gath
- Ch 21: David's census and its consequences — plague, the angel, Ornan's threshing floor
- Ch 22: David's temple preparations — materials stockpiled, Solomon charged

Translation decisions:
- H3068 (יהוה): "LORD" in L/M; "the LORD" in T. Consistent with all prior OT scripts.
- H430 (אֱלֹהִים): "God" throughout all tiers.
- H1004 (בַּיִת bayit, "house"): Rendered "house" throughout to preserve the critical wordplay
  in ch 17 — David's cedar palace / the temple David wants to build / the dynasty God promises
  to build for David instead. All three meanings converge on the same Hebrew word. T tier
  surfaces this triple meaning at 17:1 and 17:10.
- H5769 (עוֹלָם, "everlasting / forever"): "forever" in L/M/T. The Davidic covenant uses this
  term for dynastic permanence; rendering as "eternal" imports Greek timelessness; "forever"
  (the unending Davidic age) is accurate.
- H2617 (חֶסֶד): "steadfast love" in L/M; "covenant loyalty" in T (17:13, 19:2). No English
  word covers chesed's range of covenant obligation + active kindness; "covenant loyalty" in T
  surfaces the covenantal structure.
- H7854 (שָׂטָן at 21:1): "the adversary" in L; "Satan" in M/T. Significant: 2 Sam 24:1
  attributes the incitement to the LORD; 1 Chr 21:1 reattributes it to "an adversary." The
  Chronicler interprets, not contradicts — God permitted what the adversary instigated. T notes
  this theological move at 21:1.
- H4397 (מַלְאָךְ): "angel of the LORD" / "the angel" in all tiers (ch 21). The destroying angel
  who stands over Jerusalem with drawn sword gets full apocalyptic weight in T.
- H6635 (צָבָא) in "LORD of hosts": "hosts" in L/M/T — cosmic armies.
- H4496 (מְנוּחָה, "rest") / H7965 (שָׁלוֹם, "peace") at 22:9: Solomon as "man of rest" is
  deliberate — Shelomoh (שְׁלֹמֹה) derives from shalom. T surfaces this wordplay.
- H1818 (דָּם, "blood") at 22:8: David's disqualification is ritual unfitness, not moral
  condemnation. A warrior cannot build the peace-house. T frames this accordingly.
- H5071 (נְדָבָה, "freewill offering / willingness") at 22:14: T renders as "with willing
  devotion" to capture both voluntary giving and whole-hearted spirit.
- H5315 (נֶפֶשׁ, "soul") at 22:19: "heart and soul" — the embodied whole self, not a Greek
  immaterial soul. "Set your whole self to seek the LORD."
- Aspect: Ch 17 oracle uses prophetic perfects and imperfects for covenant promises — the
  LORD's declarations have the force of completed speech. Waw-consecutives carry the narrative
  of chs 18–20. Ch 21 alternates both. Genealogical chains in ch 22 use qatals.

OT intertextuality:
- 17:1–15 nearly verbatim with 2 Sam 7:1–16; T notes key Chronicler differences: no mention
  of Solomon's potential sin or conditional clause; the covenant appears more unconditional.
- 17:13: "I will be his father, he shall be my son" — Ps 2:7; quoted Heb 1:5 of Christ. T notes.
- 17:14: Chronicles reads "my kingdom" where 2 Sam 7:16 reads "your kingdom" — the kingdom
  belongs to God; David's line holds it in trust. T notes at v.14.
- 21:1: Cross-references Job 1–2, where the adversary likewise operates against God's servant.
- 21:15: The threshing floor of Ornan — identified with Moriah in 2 Chr 3:1, the site of
  Abraham's near-sacrifice (Gen 22). T notes at 21:15 and 21:18.
- 22:8–10: David's blood / Solomon's rest — structures chs 17–29; the promised rest of
  17:9 embodied in the very name of the temple-builder. T notes at 22:9.
- 22:13: "Be strong and courageous" — deliberate echo of Josh 1:6–9, David commissioning
  Solomon as Moses commissioned Joshua.
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
  "17": {
    "1": {
      "L": "Now it came to pass, as David dwelt in his house, that David said to Nathan the prophet, 'Behold, I dwell in a house of cedar, but the ark of the covenant of the LORD is under tent curtains.'",
      "M": "When David was settled in his palace, he said to the prophet Nathan, 'Here I am, living in a house of cedar, while the ark of the LORD's covenant is still sheltered under tent curtains.'",
      "T": "Once David was established in his cedar palace, he said to the prophet Nathan, 'Look — I live in a house of cedar, but the ark of the LORD's covenant is still under tent curtains.' The word 'house' opens the great conversation of this chapter: David's cedar house, the house he hopes to build for God, and the house — the dynasty — that God will build for David instead."
    },
    "2": {
      "L": "And Nathan said to David, 'Do all that is in your heart, for God is with you.'",
      "M": "Nathan replied to David, 'Go ahead with everything you have in mind, for God is with you.'",
      "T": "Nathan's first response was wholehearted agreement — do whatever is in your heart; God is with you. He was speaking from his own spirit before the LORD's word came to him that night, and the word that came would reverse everything Nathan had just said."
    },
    "3": {
      "L": "But it came to pass the same night that the word of God came to Nathan, saying:",
      "M": "But that same night the word of God came to Nathan, saying:",
      "T": "That very night — before Nathan could relay his encouragement — God interrupted with a different word. The prophet's opinion and God's decree were not the same."
    },
    "4": {
      "L": "'Go and tell David my servant, Thus says the LORD: You shall not build me a house to dwell in.'",
      "M": "'Go, tell my servant David: This is what the LORD says — You are not to build me a house to dwell in.'",
      "T": "'Go and tell my servant David: This is the word of the LORD — You will not be the one to build me a house to dwell in. Not you.'"
    },
    "5": {
      "L": "'For I have not dwelt in a house since the day I brought up Israel to this day, but I have gone from tent to tent and from one tabernacle to another.'",
      "M": "'I have never lived in a house from the day I brought Israel up from Egypt until now; I have always moved from tent to tent, from one dwelling to another.'",
      "T": "'From the day I brought Israel out of Egypt to this moment, I have never lived in a house — I have traveled with my people in tents and tabernacles. My presence was never meant to be fixed in cedar. A portable God moved with a traveling people.'"
    },
    "6": {
      "L": "'In all the places where I have walked with all Israel, did I speak a word to any of the judges of Israel whom I commanded to shepherd my people, saying, \"Why have you not built me a house of cedar?\"'",
      "M": "'In all my travels among all Israel, did I ever say a single word to any of the judges I appointed to shepherd my people — did I ever ask them why they had not built me a house of cedar?'",
      "T": "'Never once, in all my journeying among my people, did I demand a cedar house. The initiative here is entirely David's, and I am about to turn his impulse into something immeasurably greater than any building project he imagined.'"
    },
    "7": {
      "L": "'And now, thus you shall say to my servant David: Thus says the LORD of hosts — I took you from the pasture, from following the flock, to be ruler over my people Israel.'",
      "M": "'Now, say this to my servant David: This is what the LORD of hosts says — I took you from the pasture, from following the sheep, to be ruler over my people Israel.'",
      "T": "'So say this to my servant David: This is the word of the LORD of hosts — I lifted you from the sheepfold, from behind the flock, and set you as prince over my people Israel. Before you were a king you were a shepherd; that was entirely my doing, not yours.'"
    },
    "8": {
      "L": "'And I have been with you wherever you have gone, and I have cut off all your enemies from before you. And I will make for you a name, like the name of the greatest men who are on the earth.'",
      "M": "'I have been with you wherever you went, and I cut down all your enemies before you. I will make your name as great as the names of the most renowned people on earth.'",
      "T": "'I have been at every step of your journey, cutting down every enemy in your path. And I am about to make your name as great as the greatest names the world has ever known — not by your sword, but by my faithfulness to you.'"
    },
    "9": {
      "L": "'And I will appoint a place for my people Israel, and I will plant them, that they may dwell in their own place and be disturbed no more. And violent men shall waste them no more, as formerly.'",
      "M": "'I will establish a place for my people Israel and plant them firmly there, so they can live undisturbed in their own home. Wicked men will no longer waste them as they once did.'",
      "T": "'I will give my people Israel a permanent home — plant them deep so they live undisturbed, without the cycles of oppression that marked the era of the judges. The age of raiders and devastation is coming to an end.'"
    },
    "10": {
      "L": "'And since the time that I appointed judges over my people Israel, I will subdue all your enemies. Moreover, I declare to you that the LORD will build you a house.'",
      "M": "'From the time I appointed judges over my people Israel, I will put down all your enemies. And further, I am telling you that the LORD will build a house for you.'",
      "T": "'I am subduing your enemies completely — that age is finished. But hear the great reversal: you wanted to build me a house; instead, the LORD will build a house for you. Your dynasty is my gift to you, not your construction project for me.'"
    },
    "11": {
      "L": "'And it shall be, when your days are fulfilled to go to be with your fathers, that I will raise up your offspring after you, one from your own sons, and I will establish his kingdom.'",
      "M": "'When the time comes for you to join your ancestors, I will raise up one of your own sons after you, and I will establish his kingdom.'",
      "T": "'When your days are done and you lie with your fathers, I will raise up a son from your own body to succeed you, and I will make his kingdom firm. The covenant runs through your blood.'"
    },
    "12": {
      "L": "'He it is who shall build a house for me, and I will establish his throne forever.'",
      "M": "'He is the one who will build a house for me, and I will establish his throne forever.'",
      "T": "'He — not you — is the one who will build my house. And the throne I give him will stand forever. The house of cedar you wanted to build me will be built by your son; but the house I am building for you will outlast every cedar beam ever cut.'"
    },
    "13": {
      "L": "'I will be his father, and he shall be my son. And I will not take away my steadfast love from him, as I took it from him who was before you.'",
      "M": "'I will be his father, and he will be my son. I will not remove my steadfast love from him as I removed it from the one who came before you.'",
      "T": "'I will be his father; he will be my son — a royal sonship declared over the Davidic line, words that Psalm 2 will carry as God's decree and that the letter to the Hebrews (1:5) will see fulfilled in the Son of God himself. And unlike Saul, whose kingship I revoked, I will never withdraw my covenant loyalty from this son.'"
    },
    "14": {
      "L": "'But I will set him in my house and in my kingdom forever, and his throne shall be established forever.'",
      "M": "'I will establish him in my house and over my kingdom forever, and his throne will stand firm forever.'",
      "T": "'I will seat him in my house and my kingdom forever — note that Chronicles reads my kingdom, not David's (contrast 2 Sam 7:16, \"your kingdom\"). The throne belongs to God; the king holds it in trust as God's regent. This throne will stand forever.'"
    },
    "15": {
      "L": "According to all these words and according to all this vision, Nathan spoke to David.",
      "M": "In keeping with all these words and the full vision, Nathan delivered this message to David.",
      "T": "Nathan faithfully delivered every word of the vision — no softening, no abbreviation. What God said in the night, the prophet said in the morning, holding nothing back from the king."
    },
    "16": {
      "L": "Then King David went in and sat before the LORD and said, 'Who am I, O LORD God, and what is my house, that you have brought me to this point?'",
      "M": "King David went in and sat before the LORD and said, 'Who am I, LORD God, and what is my family, that you have brought me this far?'",
      "T": "David did not go out to celebrate or summon architects. He went in and sat before the LORD — the posture of a man undone by grace. 'Who am I? What is this household — a shepherd's family from Bethlehem — that you have brought me here?'"
    },
    "17": {
      "L": "'And this was a small thing in your sight, O God. You have spoken of your servant's house for a great while to come, and you have regarded me as a man of high degree, O LORD God.'",
      "M": "'But even this was a small thing in your sight, O God — and you have spoken of your servant's house reaching far into the future. You have regarded me as if I were of the highest rank, O LORD God.'",
      "T": "'And even all this — making a shepherd-boy king — you count as a small thing. You have spoken your servant's house forward into the far future, and you have looked on me as though I were a person of exalted standing. This is entirely beyond anything I could deserve.'"
    },
    "18": {
      "L": "'What more can David say to you for the honor you have shown your servant? For you know your servant.'",
      "M": "'What more can David say to you about the honor you have shown your servant? You know your servant.'",
      "T": "'I have no words. What does a man add to a conversation where God has already said everything? You know me — all my failures, all my smallness. That is precisely why what you have promised is so astonishing.'"
    },
    "19": {
      "L": "'O LORD, for your servant's sake and according to your own heart, you have done all this greatness in making known all these great things.'",
      "M": "'LORD, for your servant's sake and according to your own heart's purpose, you have done this great thing, revealing all these wonderful plans.'",
      "T": "'This came from your heart, not mine — your initiative, your purposes, your design for your world. You have made known what you are building through all of history, and it is greater than any house of cedar could ever be.'"
    },
    "20": {
      "L": "'O LORD, there is none like you, and there is no God besides you, according to all that we have heard with our own ears.'",
      "M": "'LORD, there is no one like you — there is no God but you — as everything we have heard with our own ears confirms.'",
      "T": "'There is simply no one like you, and no god to stand alongside you. This is what our entire history has been demonstrating: a God unlike any other, doing what no other power in the world can do.'"
    },
    "21": {
      "L": "'And who is like your people Israel, the one nation on earth whom God went to redeem for himself as a people, making for yourself a name by great and awesome deeds, by driving out nations before your people whom you redeemed from Egypt?'",
      "M": "'And who is like your people Israel — the one nation on earth that God set out to redeem as his own people? You made a name for yourself through great and awe-inspiring deeds, driving out nations before your people whom you redeemed from Egypt.'",
      "T": "'No nation in history has experienced what Israel has experienced: a God who launched his own rescue mission from Egypt, who displaced entire nations to plant his people in their place, making himself known through acts the world had never seen. Israel's peculiarity among the nations is entirely your doing, not ours.'"
    },
    "22": {
      "L": "'And you made your people Israel to be your people forever, and you, O LORD, became their God.'",
      "M": "'You established Israel as your own people forever, and you, LORD, became their God.'",
      "T": "'In that act of redemption you made the covenant permanent — Israel your people, you their God, forever. The exodus is not only past history; it is the foundation that holds every subsequent promise, including this Davidic covenant you have just made with me.'"
    },
    "23": {
      "L": "'And now, O LORD, let the word that you have spoken concerning your servant and concerning his house be established forever. Do as you have spoken.'",
      "M": "'And now, LORD, let the promise you have spoken about your servant and his house stand firm forever. Act as you have said.'",
      "T": "'Now, LORD — let it be. You have spoken; let your word stand. I am not asking you to change anything or do more than you have declared. I am asking you to be faithful to what you have already promised.'"
    },
    "24": {
      "L": "'And let it be established, and let your name be magnified forever, saying, \"The LORD of hosts, the God of Israel, is Israel's God.\" And let the house of your servant David be established before you.'",
      "M": "'May it stand firm, and may your name be made great forever, as people say: \"The LORD of hosts, the God of Israel, is Israel's God.\" And may the house of your servant David be established before you.'",
      "T": "'Let it be confirmed so that the whole world will say: The LORD of hosts, the God of Israel, truly is Israel's God. Let the establishment of David's house become a monument to your faithfulness, a name that outlasts the cedar of any building men have ever raised.'"
    },
    "25": {
      "L": "'For you, my God, have revealed to your servant that you will build him a house. Therefore your servant has found courage to pray before you.'",
      "M": "'For you, my God, have revealed to your servant that you will build him a house. That is why your servant has found the courage to pray before you.'",
      "T": "'You told me. That is the only reason I dare come before you with these words. You revealed the plan — I am only asking you to carry through what you yourself began. The boldness of this prayer rests entirely on your promise, not on anything in me.'"
    },
    "26": {
      "L": "'And now, O LORD, you are God, and you have promised this good thing to your servant.'",
      "M": "'Now, LORD, you are God, and you have made this good promise to your servant.'",
      "T": "'You are God — that settles everything. Your word is not speculation; it is what will be. And you have called this good — not merely useful or politically convenient, but genuinely good. That is enough.'"
    },
    "27": {
      "L": "'Now therefore, let it please you to bless the house of your servant, that it may continue before you forever. For you, O LORD, have blessed it, and it is blessed forever.'",
      "M": "'Now please be pleased to bless the house of your servant, that it may stand before you forever. For you, LORD, have blessed it, and it will be blessed forever.'",
      "T": "'Do what only you can do: bless it. Not for my sake, but because you are the one whose blessing makes things permanent. You have spoken blessing over this house — now let that blessing be the thing that holds it up forever. It rests on your word, not on our worthiness.'"
    }
  },
  "18": {
    "1": {
      "L": "Now after this, David struck down the Philistines and subdued them, and he took Gath and its towns from the hand of the Philistines.",
      "M": "After this, David defeated the Philistines and subdued them, capturing Gath and its surrounding towns from Philistine control.",
      "T": "With the covenant established, the narrative moves to its outworking: David's military victories confirm the LORD's promise to subdue all his enemies. Gath — the Philistine heartland where giants once terrorized Israel — falls to David's hand."
    },
    "2": {
      "L": "And he struck down Moab, and the Moabites became David's servants and brought tribute.",
      "M": "He also defeated Moab, and the Moabites became his subjects, bringing him tribute.",
      "T": "Moab too was subdued — the nation that had once sheltered David's parents during Saul's persecution (1 Sam 22:3–4) now paying tribute to their son. The ironies of David's story run in every direction."
    },
    "3": {
      "L": "And David struck Hadarezer king of Zobah — toward Hamath — as he went to establish his dominion at the river Euphrates.",
      "M": "David also defeated Hadadezer king of Zobah near Hamath when Hadadezer went to extend his control to the Euphrates River.",
      "T": "David's reach extended to the Euphrates — the northern boundary of the promised land (Gen 15:18). Hadadezer of Zobah, the most powerful Aramaean king of the era, could not withstand the LORD's anointed."
    },
    "4": {
      "L": "And David took from him a thousand chariots and seven thousand horsemen and twenty thousand foot soldiers, and David hamstrung all the chariot horses but retained a hundred chariots from them.",
      "M": "David captured a thousand of his chariots, seven thousand cavalry, and twenty thousand infantry. He hamstrung all but a hundred of the chariot horses, keeping those.",
      "T": "David destroyed the military hardware — hamstringing horses so they could not be used for further war, keeping only a token force. This follows the royal law of Deuteronomy 17:16 ('he must not acquire many horses for himself'). These victories were not becoming an arms race."
    },
    "5": {
      "L": "And when the Syrians of Damascus came to help Hadarezer king of Zobah, David struck down twenty-two thousand men of the Syrians.",
      "M": "When the Syrians from Damascus came to help Hadadezer king of Zobah, David struck down twenty-two thousand of them.",
      "T": "Damascus — the great Syrian capital — sent an army to rescue its Aramaean ally. David destroyed it. The breadth of these victories signals a momentary fulfillment of the Abrahamic land promise."
    },
    "6": {
      "L": "Then David put garrisons in Syria of Damascus, and the Syrians became David's servants and brought tribute. And the LORD preserved David wherever he went.",
      "M": "David stationed garrisons throughout Damascus in Syria, and the Syrians became his subjects, bringing tribute. The LORD gave David victory wherever he went.",
      "T": "Every conquest is bracketed by the same refrain: the LORD gave David victory wherever he went. These victories are not David's achievement but God's faithfulness to the covenant just declared in chapter 17."
    },
    "7": {
      "L": "And David took the shields of gold that were on the servants of Hadarezer and brought them to Jerusalem.",
      "M": "David took the gold shields carried by Hadadezer's officers and brought them to Jerusalem.",
      "T": "Gold shields from the Aramaean king's bodyguard — war trophies brought to Jerusalem, the city that would one day hold the temple. David's conquests are preparing a storehouse for Solomon's future worship."
    },
    "8": {
      "L": "And from Tibhath and from Chun, cities of Hadarezer, David brought very much bronze, with which Solomon made the bronze sea and the pillars and the vessels of bronze.",
      "M": "From Tibhath and Chun, cities of Hadadezer, David brought a great quantity of bronze — the bronze Solomon later used to make the bronze sea, the pillars, and the bronze temple vessels.",
      "T": "The Chronicler notes what 2 Samuel 8:8 does not: this captured Aramaean bronze became the raw material for Solomon's great bronze sea and temple pillars. What David won in battle, Solomon would consecrate in worship. Every military campaign points forward to the sanctuary."
    },
    "9": {
      "L": "Now when Tou king of Hamath heard that David had struck down the entire army of Hadarezer king of Zobah,",
      "M": "When Tou king of Hamath heard that David had defeated the entire army of Hadadezer king of Zobah,",
      "T": "News of the Zobah campaign reached Hamath — the northernmost limit of the promised territory (Num 34:8). King Tou had every reason to welcome Hadadezer's defeat; Hadadezer had long been Hamath's enemy."
    },
    "10": {
      "L": "he sent his son Hadoram to King David to greet him and to congratulate him, because he had fought against Hadarezer and struck him down — for Hadarezer had been at war with Tou — and he brought all manner of articles of gold, silver, and bronze.",
      "M": "he sent his son Hadoram to King David to greet him and congratulate him on his victory over Hadadezer, who had been Tou's enemy. Hadoram brought all kinds of gold, silver, and bronze articles.",
      "T": "Tou sent his son with congratulations and gifts — a diplomatic acknowledgment that David's power now extended to the northern boundary of the land of promise. Gold, silver, and bronze: the materials of the future temple were beginning to flow toward Jerusalem from the nations."
    },
    "11": {
      "L": "King David dedicated these also to the LORD, together with the silver and gold that he carried away from all the nations — from Edom, from Moab, from the Ammonites, from the Philistines, and from Amalek.",
      "M": "King David dedicated all of this to the LORD, along with the silver and gold he had taken from all the other nations — from Edom, Moab, the Ammonites, the Philistines, and Amalek.",
      "T": "Everything — the tribute and plunder from every conquered nation — David dedicated to the LORD. He did not enrich himself from these victories. He was a conduit, gathering what would one day fill the temple treasury. The warrior-king refused to treat God's gift as his own wealth."
    },
    "12": {
      "L": "Moreover, Abishai the son of Zeruiah struck down eighteen thousand Edomites in the Valley of Salt.",
      "M": "Abishai son of Zeruiah killed eighteen thousand Edomites in the Valley of Salt.",
      "T": "Abishai — one of the three greatest warriors, son of David's sister Zeruiah — inflicted a devastating defeat on Edom in the salt flats south of the Dead Sea. Edom had long been a hostile neighbor; now they were crushed."
    },
    "13": {
      "L": "And he put garrisons in Edom, and all the Edomites became David's servants. And the LORD preserved David wherever he went.",
      "M": "He stationed garrisons throughout Edom, and all the Edomites became David's subjects. The LORD gave David victory wherever he went.",
      "T": "The refrain returns: the LORD preserved David wherever he went. Edom — descendants of Esau, Israel's oldest rival — now serve Jacob's greatest king. The tables of Genesis are being turned."
    },
    "14": {
      "L": "So David reigned over all Israel, and he administered justice and righteousness to all his people.",
      "M": "David reigned over all Israel, and he administered justice and equity to all his people.",
      "T": "The summary of David's reign: justice and righteousness for all his people. The Hebrew mishpat u-tzedaqah — justice and right order — is the standard of the ideal Davidic king, what the prophets will later demand and what the Messianic king will finally embody perfectly."
    },
    "15": {
      "L": "And Joab son of Zeruiah was over the army, and Jehoshaphat son of Ahilud was the recorder.",
      "M": "Joab son of Zeruiah was in charge of the army; Jehoshaphat son of Ahilud was the royal herald.",
      "T": "The administrative structure of David's kingdom: Joab, his ruthless and indispensable general, commanded the army. Jehoshaphat was the court recorder — the keeper of official memory who would ensure that what God had done was not forgotten."
    },
    "16": {
      "L": "And Zadok son of Ahitub and Abimelech son of Abiathar were priests, and Shavsha was the scribe.",
      "M": "Zadok son of Ahitub and Abimelech son of Abiathar were priests, and Shavsha was the scribe.",
      "T": "Zadok — who would survive Adonijah's coup and outlast Abiathar to become Solomon's sole high priest — here shares priestly duties with Abimelech. The final consolidation of the Zadokite priesthood that would serve through the temple era lay ahead."
    },
    "17": {
      "L": "And Benaiah son of Jehoiada was over the Cherethites and the Pelethites, and the sons of David were the chief officials in the service of the king.",
      "M": "Benaiah son of Jehoiada commanded the Cherethites and Pelethites, and David's sons served as the king's chief officials.",
      "T": "Benaiah commanded the royal bodyguard — the Cherethites and Pelethites, likely Aegean mercenaries — who would prove decisive in the succession crisis at David's death. David's own sons held positions of honor at court; the seeds of future rivalry were already present in this list."
    }
  },
  "19": {
    "1": {
      "L": "Now after this, Nahash the king of the Ammonites died, and his son reigned in his place.",
      "M": "After this, Nahash the king of the Ammonites died, and his son became king in his place.",
      "T": "The narrative shifts: Nahash the Ammonite king — who had shown kindness to David during Saul's persecution — died. A new king meant a new diplomatic situation, and David moved immediately to maintain the relationship."
    },
    "2": {
      "L": "And David said, 'I will show steadfast love to Hanun the son of Nahash, for his father showed steadfast love to me.' So David sent messengers to comfort him concerning his father. And David's servants came to the land of the Ammonites to Hanun to comfort him.",
      "M": "David said, 'I will show kindness to Hanun son of Nahash, because his father was kind to me.' So David sent a delegation to console him over his father's death. When David's servants arrived in Ammon to comfort Hanun,",
      "T": "David extended the same covenant loyalty (chesed) that Nahash had shown him: his father had been a friend in dark days, and the son deserved the same courtesy. The gesture was genuine — the king sending comfort at a time of loss, honoring an old friendship across a border. What followed would shatter everything."
    },
    "3": {
      "L": "the princes of the Ammonites said to Hanun, 'Do you think David is honoring your father by sending comforters to you? Have not his servants come to you to search and to overthrow and to spy out the land?'",
      "M": "the Ammonite commanders said to Hanun, 'Do you really think David is honoring your father by sending men to console you? His servants have come to spy out and overthrow the land.'",
      "T": "The advisers planted suspicion where none existed: diplomacy was misread as espionage, kindness reinterpreted as threat. The honor-shame dynamics of the ancient Near East turned a gesture of covenant loyalty into a conspiracy in the minds of those who refused to believe in it."
    },
    "4": {
      "L": "So Hanun took David's servants and shaved them and cut off their garments in the middle, at their buttocks, and sent them away.",
      "M": "So Hanun seized David's men, shaved them, cut their garments off at the hips, and sent them away.",
      "T": "The humiliation was total and calculated: shaved beards — in ancient Near Eastern culture the mark of a man's dignity and honor — and robes cut to expose nakedness. This was a declaration of war communicated through deliberate public shaming. David's representatives had been treated as slaves and fools."
    },
    "5": {
      "L": "When David was told about the men, he sent to meet them, for the men were greatly ashamed. And the king said, 'Stay at Jericho until your beards have grown, and then return.'",
      "M": "When David heard what had happened to his men, he sent word to meet them, for they were deeply ashamed. The king said, 'Stay in Jericho until your beards have grown back, then come home.'",
      "T": "David's response was pastoral before it was martial: he intercepted his humiliated envoys before they had to walk through Jerusalem in shame, giving them the dignity of time at Jericho while their beards regrew. He had lived as an outcast long enough to understand what it meant to be stripped of dignity."
    },
    "6": {
      "L": "When the Ammonites saw that they had made themselves odious to David, Hanun and the Ammonites sent a thousand talents of silver to hire chariots and horsemen from Mesopotamia, from Aram-maacah, and from Zobah.",
      "M": "When the Ammonites realized they had become repugnant to David, they paid a thousand talents of silver to hire chariots and cavalry from Mesopotamia, Aram-maacah, and Zobah.",
      "T": "The insult had made war inevitable, and Ammon knew it. Unable to match David's forces alone, they assembled a coalition: Mesopotamian chariotry, Aramaean mercenaries from Maacah, and Zobah — the very kingdom David had crushed in the previous chapter. A thousand talents of silver to field an army against the LORD's anointed."
    },
    "7": {
      "L": "So they hired thirty-two thousand chariots and the king of Maacah with his army, who came and camped before Medeba. And the Ammonites gathered from their cities and came to battle.",
      "M": "They hired thirty-two thousand chariots along with the king of Maacah and his forces, who came and camped near Medeba. The Ammonites also mustered from their towns and came to fight.",
      "T": "An enormous chariot force — thirty-two thousand — assembled at Medeba on the Transjordanian plateau. It was the largest coalition arrayed against David in his entire career. The test of the Davidic covenant had arrived."
    },
    "8": {
      "L": "When David heard of it, he sent Joab and all the army of the mighty men.",
      "M": "When David heard this, he sent Joab out with the whole army and its warriors.",
      "T": "David did not underestimate the threat. He sent Joab — his best general — with Israel's entire elite force. The response was commensurate with the danger."
    },
    "9": {
      "L": "The Ammonites came out and drew up for battle at the entrance of the city, and the kings who had come were by themselves in the open country.",
      "M": "The Ammonites came out and formed their battle line at the entrance to the city, while the allied kings deployed in the open field.",
      "T": "A two-front problem: the Ammonites held their city gate — a natural defensive chokepoint; the allied Aramaean kings spread out in the open country, threatening Joab's flank and rear. He had to fight in two directions at once."
    },
    "10": {
      "L": "When Joab saw that the battle was set against him both in front and behind, he chose some of the best men of Israel and deployed them against the Syrians.",
      "M": "When Joab saw that he faced attack from both front and rear, he selected the best troops in Israel and deployed them against the Arameans.",
      "T": "Joab made the tactically correct decision: the greater threat was the professional Aramaean chariot force in the field, not the Ammonites behind their walls. He took the elite troops to meet the Aramaeans himself."
    },
    "11": {
      "L": "The rest of the people he put under the command of Abishai his brother, and they deployed against the Ammonites.",
      "M": "The rest of the troops he placed under his brother Abishai's command, facing the Ammonites.",
      "T": "Abishai commanded the holding force before the city gate — a capable commander assigned to contain the Ammonite threat while Joab crushed the more dangerous coalition in the field."
    },
    "12": {
      "L": "And he said, 'If the Syrians are too strong for me, then you shall help me; but if the Ammonites are too strong for you, then I will come and help you.'",
      "M": "'If the Arameans prove too strong for me,' he said, 'come and reinforce me; but if the Ammonites overpower you, I will come and help you.'",
      "T": "Joab's order was both tactical and covenantal: two brothers fighting in coordination, pledged to reinforce each other. Not isolated heroism, but mutual faithfulness to the mission — the pattern of Israel's covenant life applied to the battlefield."
    },
    "13": {
      "L": "'Be strong, and let us be courageous for our people and for the cities of our God, and let the LORD do what is good in his sight.'",
      "M": "'Be strong, and let us fight bravely for our people and the cities of our God. May the LORD do what is right in his eyes.'",
      "T": "'Be strong — and fight for what actually matters: our people and God's cities. But the outcome belongs to the LORD. We bring our courage; he decides the victory.' Joab's battlefield theology was precisely right: human effort and divine sovereignty together, neither one without the other."
    },
    "14": {
      "L": "So Joab and the people who were with him drew near before the Syrians for battle, and they fled before him.",
      "M": "So Joab and his troops advanced to engage the Arameans, and the Arameans fled before him.",
      "T": "The Aramaean coalition — mercenaries fighting for silver, not for their homes or their God — broke and ran when Joab's warriors came at them. Professional soldiers recalculate when the battle turns against them."
    },
    "15": {
      "L": "And when the Ammonites saw that the Syrians had fled, they also fled before Abishai his brother and entered the city. Then Joab came to Jerusalem.",
      "M": "When the Ammonites saw that the Arameans had fled, they too fled from Abishai and retreated behind the city walls. Then Joab returned to Jerusalem.",
      "T": "The Ammonites' nerve broke the moment their coalition collapsed. They retreated to safety behind their gates — alive, but defeated. Joab returned to Jerusalem; the first campaign was over, but the war was not."
    },
    "16": {
      "L": "But when the Syrians saw that they had been defeated before Israel, they sent messengers and brought out the Syrians who were beyond the Euphrates River, with Shophach the commander of the army of Hadarezer leading them.",
      "M": "When the Arameans realized they had been routed by Israel, they sent for reinforcements — the Arameans from beyond the Euphrates — led by Shophach, the commander of Hadadezer's army.",
      "T": "The defeat at Medeba did not end Aramaean ambitions. Hadadezer of Zobah raised a new and larger army from his eastern territories beyond the Euphrates — a far more determined effort to halt Israel's expanding power. Shophach, his army commander, led this second and greater force."
    },
    "17": {
      "L": "And when it was told to David, he gathered all Israel, crossed the Jordan, and came to them and drew up in battle array against them. And David deployed his forces against the Syrians, and they fought with him.",
      "M": "When David was informed, he mobilized all Israel, crossed the Jordan, and advanced to meet them. He arranged his forces against the Arameans and they fought.",
      "T": "This time David went personally — all Israel behind him, the covenant king leading from the front. The scale had escalated beyond what could be delegated to Joab. David crossed the Jordan to confront the challenge to his kingdom directly, taking the fight into Aramaean territory."
    },
    "18": {
      "L": "And the Syrians fled before Israel, and David killed seven thousand chariot fighters of the Syrians and forty thousand foot soldiers, and he put to death Shophach the commander of their army.",
      "M": "The Arameans fled before Israel. David killed seven thousand of their chariot fighters and forty thousand infantry, and Shophach the commander was struck down and died.",
      "T": "The second campaign ended in a far more decisive rout than the first: seven thousand chariot warriors and forty thousand foot soldiers killed, and Shophach their commander slain. The Aramaean power that had underpinned the entire coalition was broken at its head."
    },
    "19": {
      "L": "And when the servants of Hadarezer saw that they had been defeated before Israel, they made peace with David and became his servants. And the Syrians were not willing to help the Ammonites anymore.",
      "M": "When Hadadezer's subject kings saw that they had been routed by Israel, they made peace with David and submitted to him. After that the Arameans refused to come to the aid of the Ammonites.",
      "T": "The network of Aramaean client states that had sustained Zobah's power collapsed. State by state they came to terms with David. Ammon lost its entire coalition and stood alone — isolated, defeated, its hired armies dissolved. The campaign had remade the political map of the ancient Near East in a single season."
    }
  },
  "20": {
    "1": {
      "L": "In the spring of the year, the time when kings go out to battle, Joab led out the army and ravaged the country of the Ammonites and came and besieged Rabbah. But David remained at Jerusalem. And Joab struck Rabbah and overthrew it.",
      "M": "In the spring, at the time when kings went to war, Joab led the army out, devastated the Ammonite countryside, and came to besiege Rabbah. David remained in Jerusalem. Joab attacked Rabbah and left it in ruins.",
      "T": "The Chronicler's account of Rabbah's fall is compressed compared to 2 Samuel 11–12, omitting entirely the Bathsheba and Uriah episode. The Chronicler is not ignorant of these events — he is focusing his readers on the pattern of covenant faithfulness, not narrating David's failure. Joab does the hard work in the field; David remains in Jerusalem, and the text passes over in silence what happened there."
    },
    "2": {
      "L": "And David took the crown of their king from his head and found it weighed a talent of gold, with a precious stone in it. And it was placed on David's head. And he brought out the spoil of the city, a very great amount.",
      "M": "David removed the crown from the head of their king — it weighed a talent of gold and held a precious stone — and it was placed on David's head. He also carried off enormous plunder from the city.",
      "T": "A talent of gold for a crown — roughly thirty-four kilograms, a statement of extravagant royal wealth, set with a precious stone. This crown transferred from the Ammonite king's head to David's is a visible symbol of the Davidic covenant's fulfillment: the nations brought low, the LORD's anointed exalted."
    },
    "3": {
      "L": "And he brought out the people who were in it and set them to work with saws and with iron picks and with axes. Thus David did to all the cities of the Ammonites. Then David and all the people returned to Jerusalem.",
      "M": "He brought out the inhabitants of the city and put them to work with saws, iron picks, and axes. David treated all the Ammonite cities this way. Then he and all the people returned to Jerusalem.",
      "T": "The Ammonites were put to forced labor — a harsh but customary outcome of ancient Near Eastern conquest. The threat that had begun with Hanun's humiliation of David's envoys was now completely and permanently resolved. David and all Israel came home."
    },
    "4": {
      "L": "After this, war arose at Gezer with the Philistines, at which time Sibbecai the Hushathite struck down Sippai, who was one of the descendants of the giants, and they were subdued.",
      "M": "Some time later there was war with the Philistines at Gezer, in which Sibbecai the Hushathite killed Sippai, one of the descendants of the Rephaim; and the Philistines were subdued.",
      "T": "The Rephaim — the ancient giant warrior-clans of Canaan, who had once made Israel's spies feel like grasshoppers (Num 13:33) — make their last stand in these verses. Sibbecai the Hushathite, one of David's thirty mighty men, killed Sippai at Gezer. The age of the giants was ending."
    },
    "5": {
      "L": "And there was again war with the Philistines, and Elhanan the son of Jair struck down Lahmi the brother of Goliath the Gittite, whose spear shaft was like a weaver's beam.",
      "M": "There was another war with the Philistines, in which Elhanan son of Jair killed Lahmi the brother of Goliath the Gittite, whose spear was as thick as a weaver's beam.",
      "T": "Goliath's own brother Lahmi — carrying the same kind of enormous spear that had made Goliath's name synonymous with terror — was killed by Elhanan. David had killed the name; his men finished the family."
    },
    "6": {
      "L": "And again there was war at Gath, where there was a man of great stature who had six fingers on each hand and six toes on each foot, twenty-four in number. And he too was descended from the giants.",
      "M": "There was yet another battle at Gath, where there was a huge man with six fingers on each hand and six toes on each foot — twenty-four in all — who was also a descendant of the Rephaim.",
      "T": "At Gath — Goliath's own city — stood another giant, marked by his physical abnormality: six fingers, six toes. He was among the last of the Rephaim, the ancient warrior race that had made the conquest of Canaan seem impossible to an earlier generation."
    },
    "7": {
      "L": "When he taunted Israel, Jonathan the son of Shimea, David's brother, struck him down.",
      "M": "When he defied Israel, Jonathan son of Shimea, David's brother, struck him down.",
      "T": "He made the same mistake Goliath had made: he taunted Israel's army. David's nephew Jonathan — Shimea was David's brother — answered the taunt exactly as his uncle had, with lethal and swift courage."
    },
    "8": {
      "L": "These were descended from the giants in Gath, and they fell by the hand of David and by the hand of his servants.",
      "M": "These were the descendants of the Rephaim in Gath, and they fell at the hands of David and his warriors.",
      "T": "The last of the Canaanite giant-warriors are named here, and then they are gone from the biblical record. They fell to David's men — the covenant community overcoming every threat that had once filled their ancestors with terror. The land was being subdued, exactly as the covenant promised."
    }
  },
  "21": {
    "1": {
      "L": "And the adversary stood up against Israel and incited David to number Israel.",
      "M": "Satan stood up against Israel and incited David to take a census of Israel.",
      "T": "One of the most theologically striking verses in Chronicles: the parallel text in 2 Samuel 24:1 says 'the anger of the LORD was kindled against Israel, and he incited David against them.' The Chronicler assigns this instigation to the adversary — the שָׂטָן, literally 'the accuser' or 'the opponent.' As in Job 1–2, the adversary operates within the sphere of God's permission, not outside it. Both accounts are theologically truthful: God permitted what the adversary prompted, using the adversary's scheme as the occasion for necessary judgment on Israel."
    },
    "2": {
      "L": "So David said to Joab and to the commanders of the people, 'Go, number Israel from Beersheba to Dan, and bring me a report that I may know their number.'",
      "M": "David told Joab and the army commanders, 'Go and count Israel from Beersheba to Dan, and report back to me so I know how many there are.'",
      "T": "The command echoes the census language of Moses, but the motivation is entirely different: not God's covenant ordering of the people for service (as in Numbers 1–2), but David's desire to measure his own military resources. 'That I may know their number' — the question behind the question is whether he can rely on these numbers rather than on the LORD."
    },
    "3": {
      "L": "But Joab said, 'May the LORD add to his people a hundred times as many as they are! My lord the king, are they not all my lord's servants? Why then should my lord require this? Why should he bring guilt upon Israel?'",
      "M": "'May the LORD multiply his people a hundredfold!' Joab replied. 'My lord the king, are they not all your servants? Why should you require this? Why bring guilt on Israel?'",
      "T": "Even Joab — the unsentimental general who would later murder innocent men without hesitation — recognized something theologically wrong in this order. A census of Israel's fighting strength implied trust in human resources that displaced trust in God's provision. His protest was theologically perceptive: 'Why would you bring guilt on Israel?' He understood what David apparently did not yet see."
    },
    "4": {
      "L": "But the king's word prevailed against Joab. So Joab departed and went throughout all Israel and came back to Jerusalem.",
      "M": "But the king's command overrode Joab's objection. So Joab set out, went throughout all Israel, and returned to Jerusalem.",
      "T": "The king's authority prevailed over the general's better judgment. Joab went — and carried out an order he believed was wrong. The completed census now rests as David's responsibility: he overrode the warning and proceeded. The consequences would be his to bear."
    },
    "5": {
      "L": "And Joab gave the sum of the numbering of the people to David. All Israel was one million one hundred thousand men who drew the sword, and Judah was four hundred seventy thousand men who drew the sword.",
      "M": "Joab reported the total to David: all Israel had 1,100,000 men able to wield a sword, and Judah had 470,000.",
      "T": "The numbers were vast — more than a million and a half fighting men between Israel and Judah. The sharp irony was unavoidable: David had counted these men to measure his strength, and the numbers confirmed he commanded an enormous force. Yet this very counting, disconnected from the covenant framework of Numbers 1–2, was precisely the sin."
    },
    "6": {
      "L": "But he did not number Levi and Benjamin among them, for the king's command was abhorrent to Joab.",
      "M": "But Joab did not include Levi and Benjamin in the count, because the king's order was repugnant to him.",
      "T": "Joab's moral resistance showed itself in selective non-compliance: he excluded Levi — which held a status of sacred consecration before God — and Benjamin, perhaps from loyalty to the tribe most associated with the old Saulide order and its tensions. His conscience drew a line inside an order he could not fully refuse."
    },
    "7": {
      "L": "But God was displeased with this thing, and he struck Israel.",
      "M": "But God was displeased with this and struck Israel.",
      "T": "The brief, devastating sentence: God was displeased. The strike followed — not yet named, but coming. The census that measured Israel's strength would become the occasion for a reduction of that strength. Pride in numbers was answered with loss of numbers."
    },
    "8": {
      "L": "And David said to God, 'I have sinned greatly in that I have done this thing. But now, please take away the iniquity of your servant, for I have acted very foolishly.'",
      "M": "David said to God, 'I have sinned greatly by doing this. Now please take away your servant's guilt, for I have acted very foolishly.'",
      "T": "David's confession was swift and unqualified: 'I have sinned greatly.' He did not equivocate or explain his reasons. The man after God's own heart knew how to repent — openly, without qualification, appealing only to mercy. The word 'foolishly' (סָכַל sakal) means acting without wisdom, failing to fear what ought to be feared."
    },
    "9": {
      "L": "And the LORD spoke to Gad, David's seer, saying:",
      "M": "The LORD spoke to Gad, David's prophet, saying:",
      "T": "The LORD responded to David's confession through Gad — 'the seer,' the prophetic counselor who had been with David since his outlaw years (1 Sam 22:5). Judgment would come, but God chose to speak rather than simply strike."
    },
    "10": {
      "L": "'Go and say to David, \"Thus says the LORD: I offer you three things. Choose one of them, that I may do it to you.\"'",
      "M": "'Go and tell David: This is what the LORD says — I am giving you three options. Choose one and I will carry it out.'",
      "T": "'Tell David: choose.' God's judgment left room for David's agency — the king who had asserted his will in taking the census must now exercise his will in choosing the consequence. Three options, each terrible, each distinct in kind."
    },
    "11": {
      "L": "So Gad came to David and said to him, 'Thus says the LORD, \"Take your choice:\"'",
      "M": "Gad came to David and told him, 'This is what the LORD says — take your pick:'",
      "T": "The prophet stood before the king with three forms of judgment on his lips. The audience must have been unbearable — David waiting to hear what his sin had cost the people he loved."
    },
    "12": {
      "L": "'three years of famine, or three months of devastation before your foes while the sword of your enemies overtakes you, or three days of the sword of the LORD — pestilence in the land, and the angel of the LORD destroying throughout all the territory of Israel. Now consider what answer I shall return to him who sent me.'",
      "M": "'Three years of famine, or three months of being swept away before your enemies and their swords, or three days of the LORD's own sword — a plague across the land, with the angel of the LORD bringing destruction throughout Israel. Consider what answer I should take back to the one who sent me.'",
      "T": "'Three years of famine — slow death through empty harvests. Three months of enemy sword — rapid death at human hands. Three days of God's own plague — total death delivered by an angel, beyond any human power to resist or negotiate.' The three options diminish in duration but increase in divine directness. David understood what this meant: fall into human hands or fall into God's."
    },
    "13": {
      "L": "Then David said to Gad, 'I am in great distress. Let me fall into the hand of the LORD, for his mercy is very great, but do not let me fall into human hands.'",
      "M": "David answered Gad, 'I am in great distress. Let me fall into the LORD's hands, because his mercy is very great; but don't let me fall into human hands.'",
      "T": "David's answer was both profound and theologically sound: he would rather be at God's mercy than at human mercy, because God's mercy — even when it expressed itself through discipline — was greater than anything human enemies would offer. This is the logic of faith under judgment: God disciplines those he loves; enemies destroy. Fall toward the one who loves you, even when his hand is heavy."
    },
    "14": {
      "L": "So the LORD sent a pestilence on Israel, and seventy thousand men of Israel fell.",
      "M": "So the LORD sent a plague on Israel, and seventy thousand men died.",
      "T": "Seventy thousand men. The people David had been so eager to count were now dying because he had counted them. The covenant community that his census sought to measure as a military asset was diminished by a power no military asset could resist. The arithmetic of pride became the arithmetic of grief."
    },
    "15": {
      "L": "And God sent the angel to Jerusalem to destroy it, but as he was about to destroy it, the LORD saw, and he relented from the calamity, and said to the angel who was destroying, 'It is enough; now stay your hand.' And the angel of the LORD was standing by the threshing floor of Ornan the Jebusite.",
      "M": "God sent an angel to destroy Jerusalem, but as the angel was about to do so, the LORD looked and relented from the disaster. He said to the destroying angel, 'Enough! Hold your hand!' The angel of the LORD was standing at the threshing floor of Ornan the Jebusite.",
      "T": "The destroyer's march was stopped at the threshing floor of Ornan the Jebusite — the same elevated site associated with Mount Moriah, where Abraham had nearly offered Isaac, where God had provided and been seen (Gen 22:14). Here God's compassion arrested his own judgment: 'Enough' — the word that stopped the plague also designated the place where mercy met the people. The site of God's relenting would become the site of God's house."
    },
    "16": {
      "L": "And David lifted his eyes and saw the angel of the LORD standing between earth and heaven, with his drawn sword in his hand stretched out over Jerusalem. Then David and the elders, clothed in sackcloth, fell on their faces.",
      "M": "David looked up and saw the angel of the LORD standing between heaven and earth, with a drawn sword extended over Jerusalem. He and the elders, dressed in sackcloth, fell facedown.",
      "T": "The vision was apocalyptic: a figure suspended between heaven and earth, sword drawn and reaching toward the city. Jerusalem had been spared at the last moment, but the destroyer still stood visible to David and the elders prostrate in sackcloth. This was the face of the mercy they had received — an agent of wrath held back, not an indifference to their sin."
    },
    "17": {
      "L": "And David said to God, 'Was it not I who commanded the counting of the people? It is I who have sinned and done great evil. But these sheep — what have they done? O LORD my God, let your hand be against me and against my father's house, but do not let the plague be on your people.'",
      "M": "David said to God, 'Was it not I who ordered the census? I am the one who sinned and acted wickedly. These sheep — what have they done? O LORD my God, let your hand fall on me and my family, but keep this plague away from your people.'",
      "T": "'I counted them; I bear the guilt — not them.' This prayer is the exact mirror of the failure: the census had treated people as numbers to be measured; now David's prayer named them as God's sheep and himself as the one responsible for their suffering. He offered himself in their place. He could not atone for them, but the posture of substitute intercession anticipates the one who finally and fully could."
    },
    "18": {
      "L": "Now the angel of the LORD commanded Gad to say to David that David should go up and build an altar to the LORD on the threshing floor of Ornan the Jebusite.",
      "M": "The angel of the LORD instructed Gad to tell David to go up and build an altar to the LORD on the threshing floor of Ornan the Jebusite.",
      "T": "The command that arrested the judgment also established the worship site. The threshing floor where the angel stood with drawn sword would become the altar-place — and Solomon's temple would be built on this same spot (2 Chr 3:1). God's judgment and God's mercy occupy the same geography."
    },
    "19": {
      "L": "So David went up at the word of Gad, which he had spoken in the name of the LORD.",
      "M": "David went up in obedience to Gad's word, spoken in the LORD's name.",
      "T": "Immediate, uncalculated obedience: no negotiation about the site or the cost, no delay. David went because the LORD said go. The obedience that had been absent when the census was commanded was present here, at the place where it mattered most."
    },
    "20": {
      "L": "Now Ornan turned and saw the angel, and his four sons who were with him hid themselves. Now Ornan was threshing wheat.",
      "M": "Ornan turned and saw the angel; his four sons with him hid themselves. Ornan had been threshing wheat.",
      "T": "Ornan the Jebusite — a Canaanite who had remained in Jerusalem after David's conquest, working his farm on the city's elevated threshing floor — was at his labor when the vision struck. He saw the angel. His sons fled. He stood, or perhaps froze in the act of threshing, overwhelmed by what he saw."
    },
    "21": {
      "L": "As David came to Ornan, Ornan looked up and saw David, and he went out from the threshing floor and paid homage to David with his face to the ground.",
      "M": "When David approached, Ornan looked up, saw him, and came out from the threshing floor, bowing with his face to the ground before David.",
      "T": "The Jebusite farmer bowed before the Israelite king — a Canaanite showing honor to the man whose people had displaced his. In this encounter, the boundary between Israel and the nations was being transcended: Ornan's land would become the meeting point between heaven and earth."
    },
    "22": {
      "L": "And David said to Ornan, 'Give me the site of this threshing floor so that I may build on it an altar to the LORD — give it to me at the full price — so that the plague may be averted from the people.'",
      "M": "David said to Ornan, 'Sell me the site of this threshing floor so I can build an altar to the LORD here — at full price — so the plague on the people may stop.'",
      "T": "'At full price' — David insisted on paying. He refused to offer God something that cost him nothing, stating the principle explicitly in verse 24. The altar that would stop the plague, and the site that would one day be the temple, had to be purchased honestly, not claimed by royal power."
    },
    "23": {
      "L": "And Ornan said to David, 'Take it, and let my lord the king do what seems good to him. See, I give the oxen for burnt offerings and the threshing sledges for the wood and the wheat for the grain offering — I give it all.'",
      "M": "Ornan said to David, 'Take it! Let my lord the king do whatever pleases him. Here — I give the oxen for the burnt offerings, the threshing sledges for wood, and the wheat for the grain offering. I give it all freely.'",
      "T": "Ornan's generosity was overwhelming: oxen, sledges for fuel, wheat for grain offering — everything needed for the sacrifice already assembled and freely offered. He was handing the king a complete act of worship, ready to go. His willingness to give all to the king's sacred need was extraordinary for a Jebusite, a man outside the covenant who was standing in the presence of God's judgment."
    },
    "24": {
      "L": "But King David said to Ornan, 'No, but I will buy it for the full price. I will not take what is yours for the LORD, or offer burnt offerings that cost me nothing.'",
      "M": "But King David replied to Ornan, 'No — I insist on paying the full price. I will not take what is yours for the LORD, or offer sacrifices that have cost me nothing.'",
      "T": "'I will not offer to the LORD what costs me nothing.' One of the great principles of biblical worship: sacrifice that demands nothing of the worshiper is not sacrifice. David's insistence on full payment was his repentance made concrete and costly — the man who had used others to satisfy his own desires now refused to let the LORD's worship be cheapened by a free transaction."
    },
    "25": {
      "L": "So David paid Ornan six hundred shekels of gold by weight for the site.",
      "M": "David paid Ornan six hundred shekels of gold for the site.",
      "T": "Six hundred shekels of gold — roughly seventeen kilograms. David paid it without hesitation. The most significant plot of ground in Israel's history — a hilltop threshing floor on Mount Moriah — was purchased at full market value and would become the platform of the temple."
    },
    "26": {
      "L": "And David built there an altar to the LORD and offered burnt offerings and peace offerings and called on the LORD, and he answered him with fire from heaven upon the altar of burnt offering.",
      "M": "David built an altar to the LORD there and offered burnt offerings and fellowship offerings. He called on the LORD, and the LORD answered him with fire from heaven on the altar of burnt offering.",
      "T": "Fire from heaven — the divine signature of acceptance, given to Moses at the tabernacle dedication, to Solomon at the temple's inauguration (2 Chr 7:1), to Elijah at Carmel. God consumed the sacrifice. The plague-judgment that had taken seventy thousand lives was answered by altar-worship that God himself accepted with consuming fire. The account is closed."
    },
    "27": {
      "L": "And the LORD commanded the angel, and he put his sword back into its sheath.",
      "M": "The LORD ordered the angel to sheathe his sword, and he did so.",
      "T": "The sword went back into the sheath. The plague was finished. The altar had accomplished what the census could not: it positioned Israel in right relationship before the LORD. Worship — not numbers — was the true measure of the nation's security."
    },
    "28": {
      "L": "At that time, when David saw that the LORD had answered him at the threshing floor of Ornan the Jebusite, he sacrificed there.",
      "M": "At that time David sacrificed at the threshing floor of Ornan the Jebusite, because he saw that the LORD had answered him there.",
      "T": "The threshing floor became the worship site not by human decision but by divine response: God answered here, with fire. David recognized the theological significance of the place — where God speaks and acts, that ground becomes holy."
    },
    "29": {
      "L": "For the tabernacle of the LORD, which Moses had made in the wilderness, and the altar of burnt offering were at that time at the high place at Gibeon.",
      "M": "For the tabernacle of the LORD that Moses had built in the wilderness, and the altar of burnt offering, were at that time at the high place in Gibeon.",
      "T": "The Chronicler pauses to explain why David worshiped here rather than at the official tabernacle at Gibeon, seven miles north of Jerusalem. The prescribed and authorized worship site was there — this is important context for understanding the exception."
    },
    "30": {
      "L": "But David could not go before it to inquire of God, for he was afraid because of the sword of the angel of the LORD.",
      "M": "But David could not go there to seek God, because he was terrified by the sword of the angel of the LORD.",
      "T": "The angel still stood between David and Gibeon — the sword sheathed but the presence still overwhelming. This is the logic that made Ornan's threshing floor the site of both David's worship and ultimately Solomon's temple: divine necessity created by the crisis, not human preference or architectural calculation. Where God answers, God is worshiped."
    }
  },
  "22": {
    "1": {
      "L": "Then David said, 'This is the house of the LORD God, and this is the altar of burnt offering for Israel.'",
      "M": "Then David said, 'This is to be the house of the LORD God, and this is the altar of burnt offering for Israel.'",
      "T": "The founding proclamation: from this moment, Ornan's threshing floor — the place where God accepted fire and sheathed his sword — is designated as the temple's location. David does not choose the site; he recognizes and declares what God has already established by divine response."
    },
    "2": {
      "L": "David commanded to gather together the aliens who were in the land of Israel, and he set stonecutters to cut hewn stones to build the house of God.",
      "M": "David ordered the foreign residents in Israel to be assembled, and he assigned them as stonecutters to prepare dressed stone for the house of God.",
      "T": "The workforce for God's house included Gentiles resident in Israel — the gerim, the foreign sojourners living under Israel's protection. The temple that would one day draw all nations to Jerusalem (Isa 2:2–3) was being built in part by hands that represented those nations already dwelling among the covenant people."
    },
    "3": {
      "L": "David also provided great quantities of iron for nails for the doors of the gates and for the joinings, and bronze in abundance beyond weighing,",
      "M": "David provided a large quantity of iron for nails for the gates and joints, and bronze in such abundance it could not be weighed,",
      "T": "David's preparation was systematic and extravagant: iron for every fastening, bronze beyond measurement. He could not build the temple, but he could spend his warrior's gains equipping the one who would. Every war trophy from chapters 18–20 was finding its way to this moment."
    },
    "4": {
      "L": "and cedar logs beyond counting, for the Sidonians and the Tyrians brought great quantities of cedar to David.",
      "M": "and cedar logs in countless numbers, since the Sidonians and Tyrians brought large quantities of cedar to David.",
      "T": "Cedar from Lebanon — the Phoenician timber that signified royal prestige and divine dwelling throughout the ancient Near East — arrived in abundance from Sidon and Tyre. These would be the beams of the holy place. The nations' finest trees would roof the house of God."
    },
    "5": {
      "L": "David said, 'Solomon my son is young and inexperienced, and the house to be built for the LORD must be exceedingly magnificent, famous and glorious throughout all lands. I will therefore make preparation for it.' So David provided materials in great quantity before his death.",
      "M": "David said, 'My son Solomon is young and inexperienced, and the house to be built for the LORD must be grand and magnificent, renowned and glorious throughout every land. I will make thorough preparations for it.' So David made extensive preparations before his death.",
      "T": "David's reasoning was generous and humble: Solomon would build what David could not, but the young king would need help, and the task was beyond any generation's unaided strength. So the old king spent his final years preparing what the young king would need. The temple would bear Solomon's name; the materials would carry David's love."
    },
    "6": {
      "L": "Then he called for Solomon his son and charged him to build a house for the LORD, the God of Israel.",
      "M": "Then David summoned his son Solomon and charged him to build the house of the LORD, the God of Israel.",
      "T": "The formal charge: father to son, one generation handing the central task of the covenant to the next. What David could not do, he commissioned Solomon to do. The temple becomes the great inter-generational act of worship."
    },
    "7": {
      "L": "David said to Solomon, 'My son, I had in my heart to build a house to the name of the LORD my God.'",
      "M": "David said to Solomon, 'My son, it was my deepest desire to build a house for the name of the LORD my God.'",
      "T": "'It was in my heart' — David's longing was genuine, not dynastic calculation. The temple was not a monument to his power but a response to his love for the LORD who deserved a permanent dwelling. His disqualification did not erase the desire, only the privilege of fulfillment."
    },
    "8": {
      "L": "'But the word of the LORD came to me, saying, \"You have shed much blood and have waged great wars. You shall not build a house to my name, because you have shed much blood before me on the earth.\"'",
      "M": "'But the word of the LORD came to me: \"You have shed much blood and fought many wars. You are not to build a house for my name, because you have shed so much blood before me on the earth.\"'",
      "T": "'The word of the LORD came to me.' David received this as explanation, not as condemnation — the reason for his disqualification was not moral failure (the blood of lawful warfare is not sin) but ritual unfitness. A temple is a house of peace; a warrior king cannot build it. The same principle runs throughout Scripture: the work of winning peace and the work of embodying peace require different hands."
    },
    "9": {
      "L": "'Behold, a son will be born to you who will be a man of rest. I will give him rest from all his enemies on every side, for his name will be Solomon, and I will give peace and quiet to Israel in his days.'",
      "M": "'But a son will be born to you — a man of rest. I will give him rest from all his enemies on every side. His name will be Solomon, and I will grant Israel peace and quiet during his reign.'",
      "T": "'A son will be born to you — a man of rest.' The name Shelomoh (שְׁלֹמֹה) echoes shalom (שָׁלוֹם): Solomon is Peace. Where David's reign was the reign of war, Solomon's would be the reign of rest — the shalom promised in the Davidic covenant of chapter 17 (\"I will give rest from all your enemies\") embodied in the very name of the one who would build the temple. Peace is not merely the absence of war but the presence of God's ordering, and it is Solomon — the peace-man — who builds the peace-place."
    },
    "10": {
      "L": "'He shall build a house for my name. He shall be my son, and I will be his father, and I will establish his royal throne in Israel forever.'",
      "M": "'He will build a house for my name. He will be my son and I will be his father, and I will establish his royal throne in Israel forever.'",
      "T": "The Davidic covenant of chapter 17 is now personally transmitted from father to son: the divine-sonship declaration — 'he shall be my son, I will be his father' — is restated directly to Solomon. The throne that 17:14 said would stand forever is now explicitly named as Solomon's inheritance. The covenant runs through the succession."
    },
    "11": {
      "L": "'Now, my son, the LORD be with you, so that you may succeed in building the house of the LORD your God, as he has spoken concerning you.'",
      "M": "'Now, my son, may the LORD be with you, so that you succeed in building the house of the LORD your God, as he has promised about you.'",
      "T": "The father's farewell charge becomes a prayer: 'May the LORD be with you.' David could give Solomon materials, plans, and workers, but the one thing that made success certain was the LORD's presence. Everything else was preparation; the LORD's presence was the substance."
    },
    "12": {
      "L": "'Only may the LORD give you wisdom and understanding, that when he gives you charge over Israel you may keep the law of the LORD your God.'",
      "M": "'May the LORD give you wisdom and discernment when he puts you in charge of Israel, so that you keep the law of the LORD your God.'",
      "T": "Wisdom is not merely intelligence; it is the capacity to govern in alignment with God's revealed order. David prays that Solomon will have the kind of wisdom that keeps the law of Moses — the covenant framework within which both king and temple exist. A temple without a law-keeping king is an empty architectural statement."
    },
    "13": {
      "L": "'Then you will prosper if you are careful to observe the statutes and the rules that the LORD commanded Moses for Israel. Be strong and courageous. Do not be afraid; do not be dismayed.'",
      "M": "'You will succeed if you carefully follow the statutes and ordinances the LORD commanded Moses for Israel. Be strong and courageous — don't be afraid or discouraged.'",
      "T": "'Then you will prosper' — the conditionality of the Mosaic covenant runs alongside the unconditionality of the Davidic. God's covenant with David will stand forever; but Solomon's personal flourishing depends on his personal obedience. Both levels of covenant operate simultaneously. 'Be strong and courageous' deliberately echoes Joshua 1:6–9 — David is commissioning his son as Moses commissioned Joshua, calling the next generation to the same brave obedience as the generation of the conquest."
    },
    "14": {
      "L": "'With great pains I have provided for the house of the LORD one hundred thousand talents of gold and one million talents of silver, and bronze and iron beyond weighing, for there is so much of it. I have also provided timber and stone, and you may add to these.'",
      "M": "'In my distress I have prepared for the house of the LORD one hundred thousand talents of gold, a million talents of silver, and quantities of bronze and iron too great to be measured. I have also gathered timber and stone. You may add to all this.'",
      "T": "'In my affliction I have prepared' — the word for affliction (עֳנִי) signals personal cost and labor. These staggering quantities — 100,000 talents of gold alone is roughly 3,400 metric tons — are the language of royal idealization common in ancient Near Eastern inscriptions, expressing the concept of boundless total devotion rather than a precise audit figure. What is theologically true is that David gave without calculation, held nothing back, and left Solomon free to add whatever more the work required."
    },
    "15": {
      "L": "'You have an abundance of workmen: stonecutters, masons, carpenters, and all kinds of craftsmen for every kind of work'",
      "M": "'You have a large workforce: stonecutters, masons, carpenters, and every kind of skilled craftsman for any task'",
      "T": "'You have more than enough people.' The work of building God's house was a whole-community project — every craft represented in the workforce. No single master builder would raise the temple; it would take the accumulated skill of an entire people working together."
    },
    "16": {
      "L": "'in gold, silver, bronze, and iron without number. Arise and be doing! The LORD be with you.'",
      "M": "'in gold, silver, bronze, and iron beyond counting. Now arise and get to work! The LORD be with you.'",
      "T": "'Arise and work — the LORD be with you.' David's charge to Solomon ends with a battle-cry and a blessing in the same breath. Every material was ready; the only thing remaining was the doing. The ancient call to courageous action — qum wa'aseh — was the last word of the father to the son who would build what the father could only love and prepare for."
    },
    "17": {
      "L": "David also commanded all the leaders of Israel to help Solomon his son, saying,",
      "M": "David also directed all the leaders of Israel to support his son Solomon:",
      "T": "The charge was not to Solomon alone but to every leader in Israel: the temple was not Solomon's private project but the nation's defining act of covenant worship, requiring every leader's full commitment."
    },
    "18": {
      "L": "'Is not the LORD your God with you? Has he not given you rest on every side? For he has delivered the inhabitants of the land into my hand, and the land is subdued before the LORD and before his people.'",
      "M": "'Is not the LORD your God with you? Hasn't he given you rest on every side? He has handed the land's inhabitants over to me, and the land is subdued before the LORD and his people.'",
      "T": "'Is not the LORD with you?' — the question that answers itself. The rest that the Davidic covenant promised (17:9) had been given; the land was subdued. The conditions were already met. There was no longer any excuse not to build. David called the princes to recognize what God had already done, so that doing what remained would be unstoppable."
    },
    "19": {
      "L": "'Now set your heart and soul to seek the LORD your God. Arise and build the sanctuary of the LORD God, so that you may bring the ark of the covenant of the LORD and the holy vessels of God into the house that is to be built for the name of the LORD.'",
      "M": "'Now devote your whole heart and soul to seeking the LORD your God. Get up and build the sanctuary of the LORD God, so you can bring the ark of the LORD's covenant and the holy vessels of God into the house that will be built for the name of the LORD.'",
      "T": "'Set your whole self — heart and soul — to seek the LORD.' This is the all-of-you orientation that Chronicles consistently demands of kings and people alike. This is why the temple matters: not as an architectural achievement but as the place where the ark rests, where the holy vessels serve, where God's name dwells among his people. Build it so that the presence of God has a permanent home in the midst of the covenant community. The ark that David had brought to Jerusalem in a procession of great joy must finally rest in a house built for the name of the LORD."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '1chronicles')
        merge_tier(existing, CHRONICLES1, tier_key)
        save(tier_dir, '1chronicles', existing)
    print('1 Chronicles 17–22 written.')

if __name__ == '__main__':
    main()
