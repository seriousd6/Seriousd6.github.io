"""
MKT 2 Samuel chapters 7–12 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-2samuel-7-12.py

Translation decisions:
- H3068 (יהוה): "LORD" (small-caps convention) in L/M throughout; "the LORD" in T narrative.
  Same convention as mkt-2samuel-1-6.py. Maintained here for continuity.
- H430 (אֱלֹהִים): "God" in all tiers. In 10:12 Joab's battle speech "our God" = H430.
  In 7:23 "whom God went to redeem" = H430 as subject in relative clause — "God" in all tiers.
- H136 + H3069 (ʾădōnāy YHWH): In ch.7 David's prayer this pairing appears throughout.
  Traditional rendering: "Lord God" (Adonai + YHWH combined vocalization). L/M/T: "Lord God."
- H2617 (חֶסֶד): Major in 9:1, 9:3, 9:7, 10:2. Continuity with 2SA-1:
  L "kindness," M "steadfast loyalty," T "covenant loyalty."
  In 7:15 "my steadfast love shall not depart from him" — this is the חֶסֶד of the covenant;
  L "mercy/steadfast love," M "steadfast love," T "covenant faithfulness."
- H5769 (ʿôlām): "forever" appears seven times in ch.7 (vv.13,16,24,25,26,29×2).
  This word denotes enduring, lasting duration, often eschatological ("to the age").
  L: "forever," M: "forever," T: "forever" — the covenant promise of a permanent dynasty
  is rendered with this word throughout; do not weaken it.
- H1004 (bayit): "house" in all tiers throughout ch.7 to preserve the covenant wordplay.
  David wants to build God a house (temple); God will build David a house (dynasty).
  The Hebrew makes this pun explicit; English "house" sustains it. Do not substitute
  "temple" in v.5 or "dynasty" in v.11 — let the wordplay stand.
- H2233 (zeraʿ): "seed" (L), "offspring/descendant" (M), "offspring" (T). In 7:12
  this is the covenant seed who will build the temple = immediate reference is Solomon,
  but the oracle has eschatological depth. T notes the breadth.
- H5315 (נֶפֶשׁ): 11:11 "as your soul lives" — L "soul," M "life," T "life."
- H7307 (רוּחַ): Not prominent in chs 7–12.
- David's prayer (ch.7 vv.18–29): The most sustained prayer prose in Samuel. David uses
  "Lord God" (ʾădōnāy YHWH) throughout. T preserves the elevated, almost liturgical register.
  The phrase "Is this the law for man" (v.19, H8452) is obscure; the dominant reading is
  "this is instruction/charter for mankind" (the Davidic covenant as a model for humanity).
  T renders it: "and this is the charter for all humanity, Lord God."
- Davidic Covenant oracle (ch.7 vv.8–16): Read on three levels simultaneously:
  (1) immediate: God's past acts toward David; (2) Solomonic: his son will build the temple;
  (3) eschatological: the eternal dynasty pointing to the Messiah. T surfaces the breadth
  without collapsing the immediate historical sense. "I will be his father, he shall be my son"
  (v.14) is a royal adoption formula; T notes this also anticipates Ps 2:7 / NT application.
- H7726 (šāqaṭ, "rod") and H5061 (nega, "stripes") in 7:14: The discipline of a royal son.
  L preserves the physical corrective language; M/T note this is covenantal discipline, not
  abandonment (contrast v.15: the steadfast love will NOT depart as it did from Saul).
- Chapter 8 military list: administrative titles follow the pattern of 2SA-1 ch.8. Keep proper
  nouns untranslated (Cherethites, Pelethites). v.2 Moab execution is stark; translate accurately.
- Chapter 9 (Mephibosheth): "as one of the king's sons" (v.11) — honor-restoration theme.
  A man who expected death (v.8 "dead dog") is given the standing of a son. T makes this
  reversal explicit. Connection to ch.4:4 (the parenthesis there prepared for this moment).
- Chapter 10 (Ammon/Syria): The humiliation of the envoys (v.4 shaving half-beards, cutting
  garments to the buttocks) is a calculated act of national shame. In ANE honor culture, the
  beard was a mark of masculine dignity. T emphasizes the deliberate shame inflicted.
  Joab's speech (v.12) "Be strong, and let us fight courageously for our people and the cities
  of our God" — T preserves this as the most theologically grounded military speech in Samuel.
- Chapter 11 (David and Bathsheba): The moral horror of this passage demands clarity, not
  softening. Key irony: David stays in Jerusalem when kings should go to war (v.1); his
  inaction leads to the temptation. Uriah's speech (v.11) ironically condemns David's behavior
  without knowing it. T surfaces this irony explicitly.
- H5315 (nefesh) in 11:11: Uriah's oath "as your soul lives" — the Hebrew uses נֶפֶשׁ here
  in the oath formula. L "soul," M/T "life."
- Chapter 12 (Nathan): The parable is a legal trap. David pronounces his own sentence before
  Nathan identifies him. "You are the man" (v.7) is the rhetorical climax of the whole
  unit (chs 10–12). T tier emphasizes the structural irony.
  "The sword shall never depart from your house" (v.10) — this dynastic curse is fulfilled
  across the rest of 2 Samuel (Amnon, Absalom, Adonijah). T acknowledges the scope.
- H5006 (nāʾaṣ) in 12:14: "you have utterly scorned" or "given great occasion to the enemies
  of the LORD to blaspheme." The MT is difficult; L follows the MT literally, M uses the
  traditional reading "scorned the enemies of the LORD" (honorific omission reading),
  T: "by this deed you have given the LORD's enemies every reason to despise his name."
- Birth of Solomon (12:24–25): "The LORD loved him" and Jedidiah ("beloved of the LORD").
  T notes the theological reversal — from the death of the child born of adultery to the
  birth of the beloved child who will build the temple. Grace over judgment.
- 12:31 labor-forced population: "he put them to labor under saws and iron picks and axes
  and made them toil at the brick kilns." This is a controversial verse — some read it as
  execution by iron implements; others as corvée labor. The translation follows the dominant
  reading (labor), acknowledging the ambiguity in the L tier note.
- Aspect: waw-consecutive imperfects throughout = narrative past (simple past in English).
  Perfect verbs mark completed states. Nathan's oracle in ch.7 uses imperfect for future
  divine action (L preserves with "I will..."); the oracle is in the voice of the LORD
  speaking through Nathan.
- OT echoes: Ch.7 echoes Deut 17:14–20 (the king must not multiply wives/horses/gold —
  David already has wives, ch.3, and will multiply; Solomon will fulfill all three violations).
  7:23 echoes the Exodus redemption. Ch.9's חֶסֶד language echoes Saul's family/Jonathan's
  covenant with David (1 Sam 20). Ch.11's "when kings go out to battle" (v.1) inverts the
  expected royal behavior — David's absence is itself a moral failure.
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

SAMUEL = {
  "7": {
    "1": {
      "L": "Now it came to pass when the king sat in his house and the LORD had given him rest from all his enemies on every side,",
      "M": "After the king had settled in his palace and the LORD had given him rest from all his enemies on every side,",
      "T": "When David was settled in his palace and the LORD had given him rest from all his enemies on every side,"
    },
    "2": {
      "L": "that the king said to Nathan the prophet, 'See now, I dwell in a house of cedar, but the ark of God dwells within curtains.'",
      "M": "the king said to Nathan the prophet, 'Look, I am living in a cedar palace, but the ark of God is inside tent curtains.'",
      "T": "David said to Nathan the prophet: 'Here I am, living in a cedar palace—while the ark of God sits in a tent.'"
    },
    "3": {
      "L": "And Nathan said to the king, 'Go, do all that is in your heart, for the LORD is with you.'",
      "M": "Nathan said to the king, 'Go ahead and do all that is in your heart, for the LORD is with you.'",
      "T": "Nathan said: 'Do whatever is in your heart, for the LORD is with you.'"
    },
    "4": {
      "L": "But it came to pass that night that the word of the LORD came to Nathan, saying,",
      "M": "But that night the word of the LORD came to Nathan:",
      "T": "But that night the word of the LORD came to Nathan:"
    },
    "5": {
      "L": "'Go and tell my servant David, Thus says the LORD: Shall you build me a house to dwell in?'",
      "M": "'Go and say to my servant David, Thus says the LORD: Are you the one to build me a house to dwell in?'",
      "T": "'Go, tell my servant David: This is what the LORD says—Is it you who will build me a house to live in?'"
    },
    "6": {
      "L": "'I have not dwelt in a house since the day I brought up the children of Israel from Egypt, even to this day, but have walked in a tent and a tabernacle.'",
      "M": "'From the day I brought Israel up out of Egypt until today, I have not lived in a house but have moved about with a tent as my dwelling.'",
      "T": "'From the day I brought Israel out of Egypt until now, I have never lived in a house. I have moved about with a tent as my dwelling.'"
    },
    "7": {
      "L": "'In all the places where I have walked with all the children of Israel, did I speak a word to any of the tribes of Israel, whom I commanded to shepherd my people Israel, saying, Why have you not built me a house of cedar?'",
      "M": "'Everywhere I traveled with all the Israelites, did I ever say a word to any of the tribal leaders I commanded to shepherd my people Israel? Did I ever ask: Why have you not built me a cedar house?'",
      "T": "'In all the places I traveled with Israel, did I ever say a single word to any tribal leader I had appointed to shepherd my people? Did I ever ask: Why have you not built me a house of cedar?'"
    },
    "8": {
      "L": "'Now therefore thus shall you say to my servant David, Thus says the LORD of hosts: I took you from the pasture, from following the sheep, to be ruler over my people Israel.'",
      "M": "'Now then, say this to my servant David: This is what the LORD of hosts says: I took you from the pasture, from following the flock, to be ruler over my people Israel.'",
      "T": "'Now say this to my servant David: This is what the LORD of hosts says—I took you from the pasture, from behind the flock, and made you ruler over my people Israel.'"
    },
    "9": {
      "L": "'And I have been with you wherever you went, and I have cut off all your enemies from before you, and I have made you a great name, like the name of the great men who are on the earth.'",
      "M": "'I have been with you wherever you went, and I have cut off all your enemies before you. And I have made your name great, like the names of the greatest men on earth.'",
      "T": "'I was with you everywhere you went. I cut off all your enemies before you. And I gave you a name as great as the greatest names on earth.'"
    },
    "10": {
      "L": "'And I will appoint a place for my people Israel and will plant them, so that they may dwell in their own place and be troubled no more. And violent men shall not afflict them anymore, as at the first,'",
      "M": "'I will appoint a place for my people Israel and will plant them there, so they may live in their own land and be disturbed no more. Wicked people will not oppress them anymore as they did at first,'",
      "T": "'I will appoint a place for my people Israel and will plant them there to live undisturbed. Never again will the wicked oppress them as they have done before.'"
    },
    "11": {
      "L": "'from the time that I appointed judges over my people Israel. And I will give you rest from all your enemies. Moreover the LORD declares to you that the LORD will make you a house.'",
      "M": "'as they have done since the time I appointed judges over my people Israel. I will give you rest from all your enemies. Furthermore, the LORD declares to you that the LORD himself will build you a house.'",
      "T": "'—as they have done since the time I appointed judges over Israel. I will give you rest from all your enemies. And now the LORD declares this to you: the LORD himself will build you a house.'"
    },
    "12": {
      "L": "'When your days are fulfilled and you lie down with your fathers, I will raise up your seed after you, who shall come from your bowels, and I will establish his kingdom.'",
      "M": "'When your days are over and you rest with your ancestors, I will raise up your offspring to succeed you—one who will come from your own body—and I will establish his kingdom.'",
      "T": "'When your days are done and you lie down with your fathers, I will raise up your offspring after you—one born from your own body—and I will establish his kingdom.'"
    },
    "13": {
      "L": "'He shall build a house for my name, and I will establish the throne of his kingdom forever.'",
      "M": "'He is the one who will build a house for my name, and I will establish the throne of his kingdom forever.'",
      "T": "'He will build a house for my name, and I will establish his kingdom's throne forever.'"
    },
    "14": {
      "L": "'I will be his father, and he shall be my son. When he commits iniquity, I will discipline him with the rod of men, with the stripes of the sons of men.'",
      "M": "'I will be his father, and he will be my son. When he does wrong, I will discipline him with the rod that men use and with punishments that sons receive.'",
      "T": "'I will be his father, and he will be my son. When he goes wrong, I will correct him with the rod that fathers use on sons—but I will not abandon him.'"
    },
    "15": {
      "L": "'But my steadfast love shall not depart from him, as I took it from Saul, whom I put away before you.'",
      "M": "'My steadfast love will not be taken from him, as I took it from Saul, whom I removed before you.'",
      "T": "'My covenant faithfulness will not be withdrawn from him—as I withdrew it from Saul, whom I removed before you.'"
    },
    "16": {
      "L": "'And your house and your kingdom shall be made sure before me forever. Your throne shall be established forever.'",
      "M": "'Your house and your kingdom will endure before me forever, and your throne will be established forever.'",
      "T": "'Your house and your kingdom will stand before me forever. Your throne will be established forever.'"
    },
    "17": {
      "L": "In accordance with all these words and all this vision, so Nathan spoke to David.",
      "M": "Nathan spoke to David all these words and shared with him the whole of this vision.",
      "T": "Nathan told David every word of this, and recounted the whole vision."
    },
    "18": {
      "L": "Then King David went in and sat before the LORD and said, 'Who am I, O Lord God, and what is my house, that you have brought me thus far?'",
      "M": "Then King David went in and sat before the LORD and said, 'Who am I, Lord God, and what is my family, that you have brought me to this point?'",
      "T": "David went in and sat before the LORD and said: 'Who am I, Lord God? What is my family, that you have brought me this far?'"
    },
    "19": {
      "L": "'And yet this was a small thing in your eyes, O Lord God. You have spoken also of your servant's house for a great while to come, and this is instruction for mankind, O Lord God.'",
      "M": "'And yet this was too small a thing in your eyes, Lord God. You have also spoken of your servant's house for a long time to come. And this is the charter for humanity, Lord God.'",
      "T": "'And still this was a small thing in your eyes, Lord God—so you have spoken about your servant's house for ages to come. This is the charter you have set for all humanity, Lord God.'"
    },
    "20": {
      "L": "'And what more can David say to you? For you know your servant, O Lord God.'",
      "M": "'What more can David say to you? You know your servant, Lord God.'",
      "T": "'What more can David say to you? You know your servant, Lord God.'"
    },
    "21": {
      "L": "'For your servant's sake and according to your own heart, you have done all these great things, to make your servant know them.'",
      "M": "'For the sake of your servant and according to your own purpose, you have done all these great things and revealed them to your servant.'",
      "T": "'For your servant's sake, and out of your own heart's purpose, you have done all these great things and let your servant know them.'"
    },
    "22": {
      "L": "'Therefore you are great, O LORD God. For there is none like you, and there is no God besides you, according to all that we have heard with our ears.'",
      "M": "'Therefore you are great, LORD God. There is no one like you, and there is no God besides you, as all we have heard confirms.'",
      "T": "'Therefore you are great, LORD God. There is none like you—no God beside you—as everything we have ever heard with our ears declares.'"
    },
    "23": {
      "L": "'And who is like your people Israel, the one nation on earth whom God went to redeem to be his people, making himself a name, and doing for them great and awesome things by driving out nations and their gods before your people, whom you redeemed for yourself from Egypt?'",
      "M": "'And who is like your people Israel, the one nation on earth whom God went to redeem as his own people, making himself a name, doing great and awesome things by driving out nations and their gods before your people, whom you redeemed from Egypt?'",
      "T": "'And who is like your people Israel—the one nation on earth for whom God himself went out to redeem a people, making a name for himself, doing great and awesome things by driving out nations and their gods before the people he redeemed from Egypt?'"
    },
    "24": {
      "L": "'You have established for yourself your people Israel to be your people forever, and you, O LORD, have become their God.'",
      "M": "'You established Israel as your people forever, and you, LORD, have become their God.'",
      "T": "'You have established Israel as your own people forever. And you, LORD, have become their God.'"
    },
    "25": {
      "L": "'And now, O LORD God, confirm forever the word that you have spoken concerning your servant and concerning his house, and do as you have promised.'",
      "M": "'And now, LORD God, confirm forever the word you have spoken about your servant and his house. Do as you have promised.'",
      "T": "'And now, LORD God, let the word you have spoken about your servant and his house stand forever. Do as you have promised.'"
    },
    "26": {
      "L": "'And let your name be magnified forever, saying, The LORD of hosts is the God over Israel. And let the house of your servant David be established before you.'",
      "M": "'May your name be magnified forever, so that it is said, The LORD of hosts is God over Israel. And let the house of your servant David be established before you.'",
      "T": "'May your name be magnified forever, so that all will say: The LORD of hosts is the God of Israel. And let the house of your servant David stand firm before you.'"
    },
    "27": {
      "L": "'For you, O LORD of hosts, the God of Israel, have revealed to your servant, saying, I will build you a house. Therefore your servant has found courage to pray this prayer to you.'",
      "M": "'For you, LORD of hosts, God of Israel, have revealed this to your servant: I will build you a house. This is why your servant has found the courage to pray this prayer before you.'",
      "T": "'For it is you, LORD of hosts, God of Israel, who revealed it to your servant: I will build you a house. That is why your servant has found the heart to pray this prayer before you.'"
    },
    "28": {
      "L": "'And now, O Lord God, you are God, and your words are true, and you have promised this good thing to your servant.'",
      "M": "'Now, Lord God, you are God; your words are true, and you have made this good promise to your servant.'",
      "T": "'Now, Lord God, you are God. Your words are true. You have made this gracious promise to your servant.'"
    },
    "29": {
      "L": "'Now therefore let it please you to bless the house of your servant, that it may continue before you forever. For you, O Lord God, have spoken, and with your blessing shall the house of your servant be blessed forever.'",
      "M": "'Therefore be pleased to bless the house of your servant, so that it may stand before you forever. For you, Lord God, have spoken, and your blessing shall rest on the house of your servant forever.'",
      "T": "'Therefore may it please you to bless the house of your servant, that it may stand before you forever. For you, Lord God, have spoken—and by your blessing the house of your servant will be blessed forever.'"
    }
  },
  "8": {
    "1": {
      "L": "After this it came to pass that David struck the Philistines and subdued them, and David took Metheg-ammah from the hand of the Philistines.",
      "M": "After this, David struck the Philistines and subdued them, taking Metheg-ammah from the Philistines.",
      "T": "After this David struck the Philistines and subdued them, taking Metheg-ammah from their grip."
    },
    "2": {
      "L": "He also struck Moab and measured them with a line, making them lie down on the ground. Two lines he measured to put to death, and one full line to keep alive. And Moab became servants to David, bearing tribute.",
      "M": "He also struck down Moab and measured the captives with a line, making them lie on the ground. Two lengths he measured for death and one full length to keep alive. So Moab became subject to David, bringing tribute.",
      "T": "He struck down Moab and measured the prisoners with a cord, making them lie on the ground. Two-thirds he measured out for death; one-third he kept alive. Moab became David's subjects, bringing tribute."
    },
    "3": {
      "L": "David also struck Hadadezer the son of Rehob, king of Zobah, as he went to restore his power at the river Euphrates.",
      "M": "David also struck down Hadadezer son of Rehob, king of Zobah, as Hadadezer was on his way to reassert his control at the Euphrates.",
      "T": "David also struck down Hadadezer son of Rehob, king of Zobah, who was marching to restore his power at the Euphrates River."
    },
    "4": {
      "L": "David took from him a thousand and seven hundred horsemen and twenty thousand foot soldiers. David hamstrung all the chariot horses but kept enough for a hundred chariots.",
      "M": "David captured from him 1,700 horsemen and 20,000 foot soldiers. He hamstrung all the chariot horses except enough for a hundred chariots.",
      "T": "David captured 1,700 horsemen and 20,000 foot soldiers. He hamstrung the chariot horses, keeping only enough for a hundred chariots."
    },
    "5": {
      "L": "When the Syrians of Damascus came to help Hadadezer king of Zobah, David struck down twenty-two thousand men of the Syrians.",
      "M": "When the Syrians of Damascus came to help Hadadezer king of Zobah, David struck down twenty-two thousand of them.",
      "T": "When the Syrians of Damascus came to reinforce Hadadezer, David cut them down—twenty-two thousand men."
    },
    "6": {
      "L": "Then David put garrisons in Aram of Damascus, and the Syrians became servants to David, bearing tribute. And the LORD preserved David wherever he went.",
      "M": "David placed garrisons in the Aramean territory of Damascus, and the Syrians became subject to him, bringing tribute. The LORD preserved David wherever he went.",
      "T": "David garrisoned Aram of Damascus, and the Syrians became his subjects, paying tribute. The LORD gave David victory wherever he went."
    },
    "7": {
      "L": "David took the shields of gold that were carried by the servants of Hadadezer and brought them to Jerusalem.",
      "M": "David took the gold shields carried by Hadadezer's officers and brought them to Jerusalem.",
      "T": "David took the gold shields that Hadadezer's officers had carried and brought them to Jerusalem."
    },
    "8": {
      "L": "And from Betah and from Berothai, cities of Hadadezer, King David took a very great amount of bronze.",
      "M": "From Betah and Berothai, cities of Hadadezer, King David took a very large quantity of bronze.",
      "T": "From Betah and Berothai—cities of Hadadezer—David carried off a great quantity of bronze."
    },
    "9": {
      "L": "When Toi king of Hamath heard that David had struck down the whole army of Hadadezer,",
      "M": "When Toi king of Hamath heard that David had destroyed the whole army of Hadadezer,",
      "T": "Toi king of Hamath heard that David had shattered the entire army of Hadadezer."
    },
    "10": {
      "L": "Toi sent Joram his son to King David, to greet him and bless him, because he had fought against Hadadezer and struck him down—for Hadadezer had often been at war with Toi. And Joram brought with him articles of silver, of gold, and of bronze.",
      "M": "So Toi sent his son Joram to King David to greet him and congratulate him for defeating Hadadezer, since Hadadezer had often been at war with Toi. Joram brought articles of silver, gold, and bronze.",
      "T": "Toi sent his son Joram to King David to greet him and bless him for defeating Hadadezer—Toi and Hadadezer had long been at war. Joram brought silver, gold, and bronze as gifts."
    },
    "11": {
      "L": "These also King David dedicated to the LORD, together with the silver and gold that he dedicated from all the nations he had subdued:",
      "M": "King David dedicated these to the LORD along with all the silver and gold he had set apart from the nations he had conquered:",
      "T": "King David dedicated all of this to the LORD—the silver and gold from every nation he had subdued:"
    },
    "12": {
      "L": "from Edom, Moab, the children of Ammon, the Philistines, Amalek, and from the spoil of Hadadezer the son of Rehob, king of Zobah.",
      "M": "from Edom, Moab, Ammon, the Philistines, Amalek, and from the plunder taken from Hadadezer son of Rehob, king of Zobah.",
      "T": "from Edom and Moab, from Ammon and the Philistines and Amalek, and from the spoil of Hadadezer son of Rehob, king of Zobah."
    },
    "13": {
      "L": "And David made a name for himself when he returned from striking down eighteen thousand Syrians in the Valley of Salt.",
      "M": "David made a name for himself when he returned from killing eighteen thousand Edomites in the Valley of Salt.",
      "T": "David made a great name for himself when he returned from striking down eighteen thousand in the Valley of Salt."
    },
    "14": {
      "L": "He put garrisons in Edom; throughout all Edom he put garrisons, and all the Edomites became David's servants. And the LORD preserved David wherever he went.",
      "M": "He put garrisons throughout all Edom, and all the Edomites became David's subjects. The LORD preserved David wherever he went.",
      "T": "He placed garrisons throughout Edom, and all the Edomites became David's subjects. The LORD gave David victory wherever he went."
    },
    "15": {
      "L": "So David reigned over all Israel, and David administered justice and equity to all his people.",
      "M": "David reigned over all Israel, administering justice and equity to all his people.",
      "T": "David reigned over all Israel and executed justice and righteousness for all his people."
    },
    "16": {
      "L": "Joab the son of Zeruiah was over the army, and Jehoshaphat the son of Ahilud was the recorder.",
      "M": "Joab son of Zeruiah was over the army; Jehoshaphat son of Ahilud was the recorder.",
      "T": "Joab son of Zeruiah commanded the army. Jehoshaphat son of Ahilud was the recorder."
    },
    "17": {
      "L": "Zadok the son of Ahitub and Ahimelech the son of Abiathar were the priests, and Seraiah was the secretary.",
      "M": "Zadok son of Ahitub and Ahimelech son of Abiathar were the priests. Seraiah was the secretary.",
      "T": "Zadok son of Ahitub and Ahimelech son of Abiathar served as priests. Seraiah was the secretary."
    },
    "18": {
      "L": "And Benaiah the son of Jehoiada was over the Cherethites and the Pelethites, and David's sons were priests.",
      "M": "Benaiah son of Jehoiada was over the Cherethites and the Pelethites, and David's sons served as royal priests.",
      "T": "Benaiah son of Jehoiada was over the Cherethites and the Pelethites. David's sons were royal advisers."
    }
  },
  "9": {
    "1": {
      "L": "And David said, 'Is there anyone still left of the house of Saul to whom I may show kindness for Jonathan's sake?'",
      "M": "David asked, 'Is there anyone still left from the house of Saul to whom I can show steadfast loyalty for Jonathan's sake?'",
      "T": "David asked: 'Is there anyone still left from the house of Saul to whom I can show covenant loyalty for Jonathan's sake?'"
    },
    "2": {
      "L": "Now there was a servant of the house of Saul whose name was Ziba. And when they called him to David, the king said to him, 'Are you Ziba?' He said, 'I am your servant.'",
      "M": "There was a servant of Saul's household named Ziba. They summoned him to David, and the king asked, 'Are you Ziba?' He answered, 'Your servant is he.'",
      "T": "There was a man named Ziba who had been a servant of Saul's household. They brought him to David. 'Are you Ziba?' the king asked. 'I am your servant,' he said."
    },
    "3": {
      "L": "The king said, 'Is there not yet any of the house of Saul that I may show the kindness of God to him?' And Ziba said to the king, 'Jonathan still has a son who is lame in his feet.'",
      "M": "The king asked, 'Is there no one left of the house of Saul to whom I can show the loyal love of God?' Ziba answered, 'Jonathan still has a son who is lame in both feet.'",
      "T": "'Is there no one left from Saul's house,' the king asked, 'to whom I can show the covenant loyalty of God?' Ziba said: 'Jonathan has a son—he is lame in both feet.'"
    },
    "4": {
      "L": "The king said to him, 'Where is he?' And Ziba said to the king, 'Behold, he is in the house of Machir the son of Ammiel, at Lo-debar.'",
      "M": "The king asked, 'Where is he?' Ziba said, 'He is at the house of Machir son of Ammiel, in Lo-debar.'",
      "T": "'Where is he?' David asked. 'In Lo-debar,' said Ziba. 'At the house of Machir son of Ammiel.'"
    },
    "5": {
      "L": "Then King David sent and brought him from the house of Machir the son of Ammiel, from Lo-debar.",
      "M": "King David sent and had him brought from the house of Machir son of Ammiel in Lo-debar.",
      "T": "King David sent for him and had him brought from the house of Machir son of Ammiel in Lo-debar."
    },
    "6": {
      "L": "And Mephibosheth the son of Jonathan the son of Saul came to David and fell on his face and bowed down. And David said, 'Mephibosheth!' And he answered, 'Here is your servant.'",
      "M": "When Mephibosheth son of Jonathan son of Saul came to David, he threw himself on his face and bowed down. David said, 'Mephibosheth!' He answered, 'Here is your servant.'",
      "T": "Mephibosheth son of Jonathan son of Saul came to David and fell to the ground in homage. David said: 'Mephibosheth.' 'Your servant,' he answered."
    },
    "7": {
      "L": "And David said to him, 'Do not be afraid, for I will surely show you kindness for the sake of Jonathan your father. I will restore to you all the land of Saul your grandfather, and you shall eat at my table always.'",
      "M": "David said to him, 'Do not be afraid. I will certainly show you steadfast loyalty for the sake of your father Jonathan. I will restore all the land of your grandfather Saul to you, and you will eat at my table from now on.'",
      "T": "David said: 'Do not be afraid. I will show you covenant loyalty for your father Jonathan's sake. I will restore all the land of your grandfather Saul to you, and you will eat at my table—always.'"
    },
    "8": {
      "L": "And he bowed down and said, 'What is your servant, that you should look on a dead dog such as I am?'",
      "M": "Mephibosheth bowed down and said, 'What is your servant, that you should give attention to a dead dog like me?'",
      "T": "He bowed down and said: 'Who is your servant, that you should regard a dead dog like me?'"
    },
    "9": {
      "L": "Then the king called Ziba, Saul's servant, and said to him, 'I have given to your master's grandson everything that belonged to Saul and to all his house.'",
      "M": "The king summoned Ziba, Saul's servant, and said to him, 'I have given to your master's grandson everything that belonged to Saul and his family.'",
      "T": "The king summoned Ziba, Saul's servant, and said: 'Everything that belonged to Saul and all his house I have now given to your master's grandson.'"
    },
    "10": {
      "L": "'You shall work the land for him—you and your sons and your servants—and you shall bring in the produce, so that your master's grandson may have food to eat. But Mephibosheth your master's grandson shall eat bread always at my table.' Now Ziba had fifteen sons and twenty servants.",
      "M": "'You, your sons, and your servants are to farm the land for him and bring in the produce, so that your master's grandson may have food to live on. But Mephibosheth himself shall always eat at my table.' Now Ziba had fifteen sons and twenty servants.",
      "T": "'You and your sons and servants will farm the land for him and bring in the harvest—that is how Mephibosheth your master's grandson will be provided for. But Mephibosheth will eat at my table.' Ziba had fifteen sons and twenty servants."
    },
    "11": {
      "L": "Then Ziba said to the king, 'Your servant will do everything my lord the king commands.' So Mephibosheth ate at David's table, like one of the king's sons.",
      "M": "Ziba said to the king, 'Your servant will do everything my lord the king commands.' So Mephibosheth ate at David's table, like one of the king's sons.",
      "T": "Ziba said: 'Your servant will do whatever my lord the king commands.' So Mephibosheth ate at David's table—treated as one of the king's own sons."
    },
    "12": {
      "L": "And Mephibosheth had a young son whose name was Micha. And all who dwelt in Ziba's house became Mephibosheth's servants.",
      "M": "Mephibosheth had a young son named Micha. All who lived in Ziba's household became servants to Mephibosheth.",
      "T": "Mephibosheth had a young son named Micha. Everyone in Ziba's household became servants to Mephibosheth."
    },
    "13": {
      "L": "So Mephibosheth dwelt in Jerusalem, for he ate always at the king's table. And he was lame in both his feet.",
      "M": "Mephibosheth lived in Jerusalem, eating regularly at the king's table. He was lame in both feet.",
      "T": "Mephibosheth lived in Jerusalem. He ate at the king's table, always. He was lame in both feet."
    }
  },
  "10": {
    "1": {
      "L": "It came to pass after this that the king of the children of Ammon died, and his son Hanun reigned in his place.",
      "M": "Some time later the king of the Ammonites died, and his son Hanun succeeded him.",
      "T": "After this the king of Ammon died, and his son Hanun became king."
    },
    "2": {
      "L": "And David said, 'I will show steadfast loyalty to Hanun the son of Nahash, as his father showed loyalty to me.' So David sent by his servants to comfort him concerning his father. David's servants came into the land of the children of Ammon.",
      "M": "David said, 'I will show steadfast loyalty to Hanun son of Nahash, as his father showed loyalty to me.' David sent his servants to express condolences over his father. David's servants came to the land of the Ammonites.",
      "T": "David said: 'I will show covenant loyalty to Hanun son of Nahash, as his father showed it to me.' He sent his servants to Hanun to offer condolences over his father. David's men came to the land of Ammon."
    },
    "3": {
      "L": "But the princes of the children of Ammon said to Hanun their lord, 'Do you think that David is honoring your father in that he has sent comforters to you? Has not David sent his servants to search the city and to spy it out and to overthrow it?'",
      "M": "But the Ammonite commanders said to Hanun their lord, 'Do you really think David is honoring your father by sending these mourners? Has David not sent his servants to search the city, spy it out, and overthrow it?'",
      "T": "But the Ammonite commanders said to Hanun their lord: 'Do you think David sent these men to honor your father? Has he not sent them to survey the city—to spy it out and bring it down?'"
    },
    "4": {
      "L": "So Hanun seized David's servants and shaved off half of each man's beard and cut off their garments in the middle, at their buttocks, and sent them away.",
      "M": "So Hanun seized David's servants, shaved off half of each man's beard, cut their garments in half at the waist to expose their buttocks, and sent them away.",
      "T": "So Hanun seized David's servants and humiliated them: he shaved off half of each man's beard and cut their garments at the waist, leaving them exposed, and sent them away."
    },
    "5": {
      "L": "When David was told, he sent to meet them, for the men were greatly ashamed. The king said, 'Remain at Jericho until your beards have grown, and then return.'",
      "M": "When David was told, he sent men to meet them, for they were deeply shamed. The king said, 'Stay in Jericho until your beards have grown back, then return.'",
      "T": "David was told. He sent men to meet them on the road, because the men were deeply shamed. 'Stay at Jericho,' the king said, 'until your beards grow back. Then come home.'"
    },
    "6": {
      "L": "When the children of Ammon saw that they had made themselves odious to David, they sent and hired the Syrians of Beth-rehob and the Syrians of Zobah, twenty thousand foot soldiers, and the king of Maacah with a thousand men, and the men of Tob, twelve thousand men.",
      "M": "When the Ammonites realized they had become a stench to David, they hired the Syrians of Beth-rehob and the Syrians of Zobah—twenty thousand foot soldiers—along with the king of Maacah with a thousand men, and the men of Tob with twelve thousand men.",
      "T": "The Ammonites knew they had made themselves enemies of David, so they hired mercenaries: the Syrians of Beth-rehob and Zobah—twenty thousand foot soldiers—plus the king of Maacah with a thousand men, and the men of Tob with twelve thousand."
    },
    "7": {
      "L": "When David heard of it, he sent Joab with all the army of the mighty men.",
      "M": "On hearing this, David sent Joab and the entire army of fighting men.",
      "T": "When David heard, he sent Joab with the full army of fighting men."
    },
    "8": {
      "L": "The children of Ammon came out and drew up in battle formation at the entrance of the gate, while the Syrians of Zobah and Rehob and the men of Tob and Maacah were by themselves in the open field.",
      "M": "The Ammonites came out and formed battle lines at the entrance of the city gate, while the Syrians of Zobah and Rehob and the men of Tob and Maacah took up position separately in the open country.",
      "T": "The Ammonites came out and drew up at the city gate. The Syrians of Zobah, Rehob, Tob, and Maacah took position separately in the open field—a two-front threat."
    },
    "9": {
      "L": "When Joab saw that the battle was set against him both in front and behind, he chose some of the best soldiers of Israel and deployed them against the Syrians.",
      "M": "When Joab saw that the battle lines were set against him both in front and behind, he selected the best troops of Israel and positioned them against the Syrians.",
      "T": "Joab saw that the attack was coming from two directions—front and rear. He chose the best of Israel's soldiers and arrayed them against the Syrians."
    },
    "10": {
      "L": "The rest of the people he put under the command of Abishai his brother, and he deployed them against the children of Ammon.",
      "M": "The remaining troops he placed under the command of his brother Abishai, and they were deployed against the Ammonites.",
      "T": "The rest he put under his brother Abishai, who faced the Ammonites."
    },
    "11": {
      "L": "He said, 'If the Syrians are too strong for me, then you shall help me. But if the children of Ammon are too strong for you, then I will come and help you.'",
      "M": "He said, 'If the Syrians prove too strong for me, you must come and help me. If the Ammonites prove too strong for you, I will come and help you.'",
      "T": "'If the Syrians are too strong for me, come to my aid. If the Ammonites are too strong for you, I will come to yours.'"
    },
    "12": {
      "L": "'Be strong, and let us fight courageously for our people and for the cities of our God. And may the LORD do what seems good to him.'",
      "M": "'Be strong; let us fight bravely for our people and for the cities of our God. The LORD will do what is good in his sight.'",
      "T": "'Be strong. Fight for our people and for the cities of our God. The LORD will do what is right.'"
    },
    "13": {
      "L": "So Joab and the people who were with him drew near to battle against the Syrians, and they fled before him.",
      "M": "Joab and the men with him advanced to fight the Syrians, and the Syrians fled before him.",
      "T": "Joab advanced against the Syrians, and they fled."
    },
    "14": {
      "L": "When the children of Ammon saw that the Syrians had fled, they also fled before Abishai and entered the city. So Joab returned from fighting the children of Ammon and came to Jerusalem.",
      "M": "When the Ammonites saw that the Syrians had fled, they fled too—before Abishai—and retreated into the city. Then Joab turned back from the Ammonites and returned to Jerusalem.",
      "T": "When the Ammonites saw the Syrians had fled, they too fled before Abishai and retreated into the city. Joab returned to Jerusalem."
    },
    "15": {
      "L": "When the Syrians saw that they had been struck down before Israel, they gathered themselves together.",
      "M": "When the Syrians saw that they had been routed by Israel, they regrouped.",
      "T": "The Syrians saw they had been broken before Israel. They regrouped."
    },
    "16": {
      "L": "And Hadadezer sent and brought out the Syrians who were beyond the Euphrates River, and they came to Helam, with Shobach the commander of the army of Hadadezer going before them.",
      "M": "Hadadezer sent and brought out the Syrians from beyond the Euphrates, and they came to Helam, with Shobach, the commander of Hadadezer's army, leading them.",
      "T": "Hadadezer sent for the Syrians beyond the Euphrates. They came to Helam under Shobach, the commander of Hadadezer's army."
    },
    "17": {
      "L": "When David was told, he gathered all Israel, crossed the Jordan, and came to Helam. The Syrians set themselves in array against David and fought him.",
      "M": "When David was told, he mustered all Israel, crossed the Jordan, and arrived at Helam. The Syrians formed battle lines against David and attacked.",
      "T": "David was told. He gathered all Israel, crossed the Jordan, and came to Helam. The Syrians drew up against him and gave battle."
    },
    "18": {
      "L": "And the Syrians fled before Israel. David killed seven hundred chariot drivers of the Syrians and forty thousand horsemen, and he struck down Shobach the commander of their army, who died there.",
      "M": "The Syrians fled before Israel. David struck down seven hundred of their chariot crews and forty thousand horsemen, and he killed Shobach the commander of their army.",
      "T": "The Syrians fled before Israel. David killed seven hundred chariot drivers and forty thousand horsemen, and Shobach the army commander died there."
    },
    "19": {
      "L": "When all the kings who were servants of Hadadezer saw that they had been struck down before Israel, they made peace with Israel and became their servants. So the Syrians were afraid to help the children of Ammon anymore.",
      "M": "When all the kings who served under Hadadezer saw that they had been defeated by Israel, they made peace with Israel and submitted to them. After that, the Syrians were afraid to help the Ammonites any further.",
      "T": "All the vassal kings of Hadadezer, seeing they were beaten, made peace with Israel and submitted to them. After that, the Syrians were unwilling to help Ammon again."
    }
  },
  "11": {
    "1": {
      "L": "It came to pass, at the turn of the year, at the time when kings go out to battle, that David sent Joab and his servants with him, and all Israel, and they ravaged the children of Ammon and besieged Rabbah. But David remained at Jerusalem.",
      "M": "In the spring, when kings typically march out to war, David sent Joab with his officers and all Israel. They devastated the Ammonites and besieged Rabbah. But David himself stayed in Jerusalem.",
      "T": "In the spring, the season when kings go to war, David sent Joab and his officers and all Israel. They laid waste to Ammon and besieged Rabbah. But David stayed in Jerusalem."
    },
    "2": {
      "L": "It came to pass late one afternoon that David arose from his bed and walked about on the roof of the king's house. From the roof he saw a woman bathing, and the woman was very beautiful to look upon.",
      "M": "One evening David got up from his couch and was walking on the roof of the palace. From the roof he saw a woman bathing, and she was very beautiful.",
      "T": "Late one afternoon David rose from his couch and walked on the palace roof. From the roof he saw a woman bathing. She was very beautiful."
    },
    "3": {
      "L": "And David sent and inquired about the woman. And someone said, 'Is this not Bathsheba the daughter of Eliam, the wife of Uriah the Hittite?'",
      "M": "David sent someone to find out about her. He was told, 'She is Bathsheba daughter of Eliam, the wife of Uriah the Hittite.'",
      "T": "David sent to find out who she was. Someone said: 'Is that not Bathsheba, daughter of Eliam—the wife of Uriah the Hittite?'"
    },
    "4": {
      "L": "So David sent messengers and took her. And she came in to him, and he lay with her—she had just purified herself from her uncleanness—and she returned to her house.",
      "M": "David sent messengers to bring her. She came to him, and he lay with her. (She had just completed her ritual purification from her monthly uncleanness.) Then she returned home.",
      "T": "David sent messengers and took her. She came to him, and he lay with her. She had just completed her purification. Then she went back home."
    },
    "5": {
      "L": "And the woman conceived, and she sent and told David, 'I am with child.'",
      "M": "The woman became pregnant, and she sent word to David: 'I am pregnant.'",
      "T": "The woman conceived. She sent word to David: 'I am pregnant.'"
    },
    "6": {
      "L": "So David sent word to Joab, 'Send me Uriah the Hittite.' And Joab sent Uriah to David.",
      "M": "David sent word to Joab: 'Send me Uriah the Hittite.' So Joab sent Uriah to David.",
      "T": "David sent word to Joab: 'Send me Uriah the Hittite.' Joab sent him."
    },
    "7": {
      "L": "When Uriah came to him, David asked how Joab was doing and how the people were doing and how the war was going.",
      "M": "When Uriah arrived, David asked about Joab's welfare, about the troops, and about how the war was going.",
      "T": "When Uriah came, David asked after Joab, after the men, after the progress of the war."
    },
    "8": {
      "L": "Then David said to Uriah, 'Go down to your house and wash your feet.' Uriah departed from the king's house, and a gift from the king followed him.",
      "M": "David said to Uriah, 'Go home and rest.' Uriah left the palace, and the king sent a present after him.",
      "T": "David said: 'Go home. Rest.' Uriah left the palace, and a gift from the king went with him."
    },
    "9": {
      "L": "But Uriah slept at the door of the king's house with all the servants of his lord, and did not go down to his house.",
      "M": "But Uriah slept at the entrance of the palace with all the king's other servants. He did not go home.",
      "T": "But Uriah slept at the palace entrance with all the king's servants. He did not go home."
    },
    "10": {
      "L": "When they told David, 'Uriah has not gone down to his house,' David said to Uriah, 'Have you not come from a journey? Why then did you not go down to your house?'",
      "M": "When David was told that Uriah had not gone home, he asked Uriah, 'You have just come back from a long journey—why did you not go home?'",
      "T": "When David was told, he summoned Uriah. 'You just got back from a journey. Why didn't you go home?'"
    },
    "11": {
      "L": "Uriah said to David, 'The ark and Israel and Judah dwell in booths, and my lord Joab and the servants of my lord are camping in the open fields. Shall I then go to my house, to eat and drink and lie with my wife? As you live, and as your soul lives, I will not do this thing.'",
      "M": "Uriah said to David, 'The ark and Israel and Judah are staying in tents, and my lord Joab and your servants are camped in the open country. Should I then go home to eat and drink and sleep with my wife? As surely as you live and as your soul lives, I will not do such a thing.'",
      "T": "Uriah said: 'The ark of God is in a tent. Israel and Judah are in tents. Joab and all your servants are camped in the open field. And I am to go home and eat and drink and sleep with my wife? As you live—as your life itself is my witness—I will not do it.'"
    },
    "12": {
      "L": "Then David said to Uriah, 'Stay here today also, and tomorrow I will send you back.' So Uriah remained in Jerusalem that day and the next.",
      "M": "David said to Uriah, 'Stay here today as well, and tomorrow I will let you go.' So Uriah stayed in Jerusalem that day and the next.",
      "T": "'Stay today,' David said. 'I'll send you back tomorrow.' So Uriah stayed in Jerusalem that day and the next."
    },
    "13": {
      "L": "And David invited him, and he ate in his presence and drank, so that David made him drunk. And in the evening he went out to lie on his bed with the servants of his lord, but he did not go down to his house.",
      "M": "David invited him, and Uriah ate and drank with him, and David made him drunk. But in the evening Uriah went out to sleep on his bed among the king's servants. He still did not go home.",
      "T": "David invited him to dinner. Uriah ate and drank—David plied him with wine until he was drunk. That evening Uriah went out and lay down with the king's servants. He did not go home."
    },
    "14": {
      "L": "In the morning David wrote a letter to Joab and sent it by the hand of Uriah.",
      "M": "In the morning David wrote a letter to Joab and sent it with Uriah.",
      "T": "In the morning David wrote a letter to Joab and sent it by Uriah's own hand."
    },
    "15": {
      "L": "In the letter he wrote, 'Set Uriah in the forefront of the hardest fighting, and then draw back from him, that he may be struck down and die.'",
      "M": "In the letter he wrote: 'Put Uriah at the front where the fighting is fiercest, then pull back so that he is struck down and killed.'",
      "T": "The letter said: 'Place Uriah in the front line where the battle is hardest. Then pull back—so that he is cut down and dies.'"
    },
    "16": {
      "L": "And as Joab was besieging the city, he assigned Uriah to the place where he knew there were valiant warriors.",
      "M": "While Joab had the city under siege, he stationed Uriah at the point where he knew the strongest defenders were.",
      "T": "Joab, watching the city, knew where the toughest defenders were posted. He put Uriah there."
    },
    "17": {
      "L": "And the men of the city came out and fought with Joab, and some of the servants of David fell. Uriah the Hittite also died.",
      "M": "The men of the city sallied out and attacked Joab's forces. Some of David's servants fell, and Uriah the Hittite died too.",
      "T": "The city's defenders came out and attacked. Some of David's men fell. Uriah the Hittite also died."
    },
    "18": {
      "L": "Then Joab sent and told David all the news about the fighting.",
      "M": "Then Joab sent a report to David about the full course of the battle.",
      "T": "Joab sent David a full report on the fighting."
    },
    "19": {
      "L": "And he commanded the messenger, 'When you have finished telling all the news about the war to the king,",
      "M": "He instructed the messenger: 'After you have given the king the full account of the battle,",
      "T": "He instructed the messenger: 'When you have finished reporting the battle to the king,'"
    },
    "20": {
      "L": "'if the king's anger rises, and he says to you, Why did you go so near the city to fight? Did you not know that they would shoot from the wall?'",
      "M": "'if the king flares up in anger and says, Why did you go so close to the city? Did you not know they would shoot from the wall?'",
      "T": "'if the king grows angry and asks why you pressed so close to the wall—did you not know they would shoot from there?—'"
    },
    "21": {
      "L": "'Who struck down Abimelech the son of Jerubbesheth? Was it not a woman who cast an upper millstone on him from the wall, so that he died at Thebez? Why did you go so near the wall?—then you shall say, Your servant Uriah the Hittite is dead also.'",
      "M": "'—who struck down Abimelech son of Jerubbesheth? Was it not a woman who dropped an upper millstone on him from the wall at Thebez, so that he died there? Why did you go close to the wall?—then say: Your servant Uriah the Hittite is dead also.'",
      "T": "'—who killed Abimelech son of Jerubbesheth? A woman dropped a millstone on him from the wall at Thebez. That is how he died. Why did you go near the wall?—then say: Your servant Uriah the Hittite is dead.'"
    },
    "22": {
      "L": "So the messenger went and came and told David all that Joab had sent him to say.",
      "M": "The messenger went and came and told David everything Joab had sent him to report.",
      "T": "The messenger went and came and told David everything Joab had sent him to say."
    },
    "23": {
      "L": "The messenger said to David, 'The men gained an advantage over us and came out against us in the field, but we drove them back to the entrance of the gate.'",
      "M": "The messenger said to David, 'The enemy had the advantage and came out against us in the open, but we pushed them back to the city gate.'",
      "T": "The messenger said: 'The men came out strong against us into the field, but we drove them back to the city gate.'"
    },
    "24": {
      "L": "'And the archers shot at your servants from the wall. Some of the king's servants are dead, and your servant Uriah the Hittite is dead also.'",
      "M": "'The archers shot at your servants from the wall. Some of the king's men died, and your servant Uriah the Hittite is dead too.'",
      "T": "'The archers shot from the wall and some of your men died. Your servant Uriah the Hittite is also dead.'"
    },
    "25": {
      "L": "Then David said to the messenger, 'Thus shall you say to Joab, Do not let this matter trouble you, for the sword devours one as well as another. Strengthen your attack against the city and overthrow it. Encourage him.'",
      "M": "David said to the messenger, 'Tell Joab: Do not let this distress you—the sword is no respecter of persons. Press the attack against the city and take it. Encourage him.'",
      "T": "David told the messenger: 'Say this to Joab: Do not be troubled by this. The sword cuts down one man as well as another. Press the attack. Take the city. Tell him to be strong.'"
    },
    "26": {
      "L": "And when the wife of Uriah heard that Uriah her husband was dead, she mourned for her husband.",
      "M": "When Uriah's wife heard that her husband was dead, she mourned for him.",
      "T": "When Uriah's wife heard that her husband was dead, she mourned for him."
    },
    "27": {
      "L": "And when the mourning was over, David sent and brought her to his house, and she became his wife and bore him a son. But the thing that David had done was evil in the sight of the LORD.",
      "M": "When the mourning period was over, David sent for her and brought her to his palace. She became his wife and bore him a son. But the thing David had done was evil in the LORD's sight.",
      "T": "When the mourning was done, David sent for her. She came to his house. She became his wife and bore him a son. But what David had done was evil in the sight of the LORD."
    }
  },
  "12": {
    "1": {
      "L": "And the LORD sent Nathan to David. He came to him and said to him, 'There were two men in one city, one rich and one poor.'",
      "M": "The LORD sent Nathan to David. He came to him and said: 'There were two men in a certain city, one rich and one poor.'",
      "T": "The LORD sent Nathan to David. Nathan came and said: 'There were two men in a city—one rich, one poor.'"
    },
    "2": {
      "L": "'The rich man had very many flocks and herds.'",
      "M": "'The rich man had very many flocks and herds.'",
      "T": "'The rich man had enormous flocks and herds.'"
    },
    "3": {
      "L": "'But the poor man had nothing but one little ewe lamb which he had bought. He raised it and it grew up with him and with his children. It ate from his food and drank from his cup and lay in his arms, and it was like a daughter to him.'",
      "M": "'But the poor man had only one small ewe lamb that he had bought. He raised it, and it grew up alongside him and his children. It shared his food, drank from his cup, slept in his arms, and was like a daughter to him.'",
      "T": "'The poor man had nothing—one little ewe lamb he had bought. He raised it. It grew up with him and his children, ate from his plate, drank from his cup, slept in his arms. It was like a daughter to him.'"
    },
    "4": {
      "L": "'Now a traveler came to the rich man, and he was unwilling to take from his own flock or his own herd to prepare for the guest who had come to him. Instead he took the poor man's lamb and prepared it for the man who had come to him.'",
      "M": "'A traveler came to the rich man. The rich man would not slaughter one of his own sheep or cattle for the guest. Instead he took the poor man's lamb and served it to the visitor.'",
      "T": "'A traveler came to the rich man. The rich man would not take from his own flock. He took the poor man's lamb—and served it to his guest.'"
    },
    "5": {
      "L": "Then David's anger was greatly kindled against the man, and he said to Nathan, 'As the LORD lives, the man who has done this deserves to die!'",
      "M": "David burned with anger against the man and said to Nathan, 'As the LORD lives, the man who did this deserves to die!'",
      "T": "David's anger blazed. He said to Nathan: 'As the LORD lives, the man who did this deserves to die!'"
    },
    "6": {
      "L": "'He shall restore the lamb fourfold, because he did this thing and because he had no pity.'",
      "M": "'He must repay the lamb four times over, because he did this and had no pity.'",
      "T": "'He must pay back fourfold—because he had no pity.'"
    },
    "7": {
      "L": "Nathan said to David, 'You are the man! Thus says the LORD, the God of Israel: I anointed you king over Israel, and I delivered you from the hand of Saul.'",
      "M": "Nathan said to David, 'You are the man! This is what the LORD, the God of Israel, says: I anointed you king over Israel, and I rescued you from the hand of Saul.'",
      "T": "Nathan said: 'You are the man. This is what the LORD God of Israel says: I anointed you king over Israel. I rescued you from Saul's hand.'"
    },
    "8": {
      "L": "'And I gave you your master's house and your master's wives into your arms, and I gave you the house of Israel and of Judah. And if that were too little, I would have added to you as much more.'",
      "M": "'I gave you your master's house and put his wives into your care, and I gave you Israel and Judah. And if that had not been enough, I would have given you even more.'",
      "T": "'I gave you your master's house. I placed his wives in your care. I gave you Israel and Judah. If that had been too little, I would have given you still more.'"
    },
    "9": {
      "L": "'Why have you despised the word of the LORD, to do what is evil in his sight? You have struck down Uriah the Hittite with the sword and taken his wife to be your wife, and have killed him with the sword of the children of Ammon.'",
      "M": "'Why have you despised the word of the LORD by doing what is evil in his eyes? You struck down Uriah the Hittite with the sword, took his wife as your own, and killed him with the sword of the Ammonites.'",
      "T": "'Why have you despised the word of the LORD and done this evil? You killed Uriah the Hittite with the sword. You took his wife. You killed him with the sword of Ammon.'"
    },
    "10": {
      "L": "'Now therefore the sword shall never depart from your house, because you have despised me and have taken the wife of Uriah the Hittite to be your wife.'",
      "M": "'Therefore the sword will never depart from your house, because you despised me and took Uriah the Hittite's wife as your own.'",
      "T": "'Therefore the sword will never leave your house. Because you despised me and took the wife of Uriah the Hittite.'"
    },
    "11": {
      "L": "'Thus says the LORD: Behold, I will raise up evil against you from your own house. And I will take your wives before your eyes and give them to your neighbor, and he shall lie with your wives in the sight of this sun.'",
      "M": "'This is what the LORD says: I am about to raise up evil against you from within your own household. I will take your wives before your own eyes and hand them over to another, and he will lie with them in broad daylight.'",
      "T": "'This is what the LORD says: I will raise up disaster against you from within your own house. I will take your wives before your eyes and give them to another man, and he will lie with them in the open light of day.'"
    },
    "12": {
      "L": "'For you did this secretly, but I will do this thing before all Israel and before the sun.'",
      "M": "'You acted in secret, but I will do this before all Israel and in broad daylight.'",
      "T": "'You acted in secret. I will do this in front of all Israel, in the full light of the sun.'"
    },
    "13": {
      "L": "David said to Nathan, 'I have sinned against the LORD.' And Nathan said to David, 'The LORD also has put away your sin. You shall not die.'",
      "M": "David said to Nathan, 'I have sinned against the LORD.' Nathan answered, 'The LORD has also put away your sin. You will not die.'",
      "T": "David said to Nathan: 'I have sinned against the LORD.' Nathan said: 'The LORD has taken away your sin. You will not die.'"
    },
    "14": {
      "L": "'Nevertheless, because by this deed you have utterly scorned the LORD, the child who is born to you shall die.'",
      "M": "'But because by this deed you have given the LORD's enemies every reason to despise his name, the child who has been born to you will die.'",
      "T": "'Nevertheless, by this deed you have given the LORD's enemies reason to despise his name. The child who has been born to you will die.'"
    },
    "15": {
      "L": "Then Nathan departed to his house. And the LORD struck the child that Uriah's wife had borne to David, and it became sick.",
      "M": "After Nathan had gone home, the LORD struck the child that Uriah's wife had borne to David, and the child became ill.",
      "T": "Nathan went home. The LORD struck the child that Uriah's wife had borne to David, and the child fell sick."
    },
    "16": {
      "L": "David therefore sought God on behalf of the child. And David fasted and went in and lay all night on the ground.",
      "M": "David pleaded with God for the child. He fasted and went in and spent the night lying on the ground.",
      "T": "David pleaded with God for the child. He fasted. He went in and lay on the ground all night."
    },
    "17": {
      "L": "And the elders of his house arose and went to him to raise him up from the ground, but he would not, nor did he eat food with them.",
      "M": "The elders of his household stood over him to lift him from the ground, but he refused. He would not eat food with them.",
      "T": "The elders of his household stood over him and tried to lift him. He would not get up. He would not eat."
    },
    "18": {
      "L": "On the seventh day the child died. And the servants of David were afraid to tell him that the child was dead, for they said, 'Behold, while the child was still alive, we spoke to him and he did not listen to us. How then can we say to him the child is dead? He may do something terrible.'",
      "M": "On the seventh day the child died. David's servants were afraid to tell him, because they said: 'Even while the child was alive, we spoke to him and he would not listen. How can we tell him the child is dead? He might do something desperate.'",
      "T": "On the seventh day the child died. David's servants were afraid to tell him. They said: 'While the child was still alive, he wouldn't listen to us. How can we tell him the child is dead? He might do something terrible.'"
    },
    "19": {
      "L": "But when David saw that his servants were whispering together, David understood that the child was dead. And David said to his servants, 'Is the child dead?' They said, 'He is dead.'",
      "M": "But David noticed his servants whispering among themselves and understood that the child was dead. He asked his servants, 'Is the child dead?' 'Yes,' they said, 'he is dead.'",
      "T": "But David saw his servants whispering. He understood. 'Is the child dead?' he asked. 'He is dead,' they said."
    },
    "20": {
      "L": "Then David arose from the earth and washed and anointed himself and changed his clothes. And he went into the house of the LORD and worshiped. He then went to his own house, and when he requested, they set food before him and he ate.",
      "M": "David got up from the ground, washed, anointed himself, and changed his clothes. He went into the house of the LORD and worshiped. Then he returned to his palace and ate when food was set before him.",
      "T": "David rose from the ground. He washed, anointed himself, changed his clothes, and went into the house of the LORD and worshiped. Then he came home, asked for food, and ate."
    },
    "21": {
      "L": "Then his servants said to him, 'What is this thing that you have done? You fasted and wept for the child while it was alive, but when the child died, you arose and ate food.'",
      "M": "His servants asked him, 'What is this behavior? You fasted and wept while the child was alive, but now that he is dead you get up and eat?'",
      "T": "His servants said: 'We don't understand. While the child was alive, you fasted and wept. Now that he is dead, you rise and eat?'"
    },
    "22": {
      "L": "He said, 'While the child was still alive, I fasted and wept, for I said, Who knows whether the LORD will be gracious to me, so that the child may live?'",
      "M": "He answered, 'While the child was still alive, I fasted and wept. I thought: Who knows? Perhaps the LORD will be gracious to me and let the child live.'",
      "T": "He said: 'While the child was alive, I fasted and wept. I thought: Who knows? Perhaps the LORD will show me grace and the child will live.'"
    },
    "23": {
      "L": "'But now he is dead. Why should I fast? Can I bring him back again? I shall go to him, but he will not return to me.'",
      "M": "'But now he is dead. Why should I keep fasting? Can I bring him back? I can go to him, but he cannot come back to me.'",
      "T": "'But he is dead. Why should I fast? Can I bring him back? I will go to him one day. He will not come back to me.'"
    },
    "24": {
      "L": "Then David comforted his wife Bathsheba and went in to her and lay with her. And she bore a son, and he called his name Solomon. And the LORD loved him.",
      "M": "David comforted his wife Bathsheba. He went in to her and lay with her. She bore a son, and David named him Solomon. The LORD loved him.",
      "T": "David comforted Bathsheba his wife. He went in to her, and she bore a son. David named him Solomon. And the LORD loved him."
    },
    "25": {
      "L": "And the LORD sent word by the hand of Nathan the prophet, and he called his name Jedidiah, because of the LORD.",
      "M": "The LORD sent a message through the prophet Nathan, who called the child Jedidiah—Beloved of the LORD—because the LORD loved him.",
      "T": "Through the prophet Nathan the LORD sent word, and the child was also called Jedidiah—Beloved of the LORD—because the LORD loved him."
    },
    "26": {
      "L": "Now Joab fought against Rabbah of the children of Ammon and captured the royal city.",
      "M": "Meanwhile, Joab fought against Rabbah of the Ammonites and captured the royal citadel.",
      "T": "Meanwhile, Joab was fighting Rabbah of Ammon and had taken the royal quarter of the city."
    },
    "27": {
      "L": "And Joab sent messengers to David and said, 'I have fought against Rabbah; I have also taken the city of waters.'",
      "M": "Joab sent messengers to David with the report: 'I have fought against Rabbah and captured the water supply of the city.'",
      "T": "Joab sent word to David: 'I have been fighting Rabbah. I have taken the water district.'"
    },
    "28": {
      "L": "'Now therefore gather the rest of the people together and encamp against the city and take it, lest I take the city and it be called by my name.'",
      "M": "'Now muster the rest of the army, march against the city, and take it—before I capture it and it gets named after me.'",
      "T": "'Now gather the rest of the forces, come and take the city yourself—before I take it and it bears my name, not yours.'"
    },
    "29": {
      "L": "So David gathered all the people and went to Rabbah and fought against it and captured it.",
      "M": "So David gathered all the forces, marched to Rabbah, attacked, and captured it.",
      "T": "David mustered the army, marched to Rabbah, and took it."
    },
    "30": {
      "L": "And he took the crown of their king from his head. Its weight was a talent of gold, with precious stones, and it was placed on David's head. And he brought out the spoil of the city, a very great amount.",
      "M": "He took the crown from the head of the Ammonite king. It weighed a talent of gold and was set with precious stones. It was placed on David's head. He also brought out a great quantity of plunder from the city.",
      "T": "He took the crown from the head of the Ammonite king—a talent of gold set with precious stones—and it was placed on David's head. He brought out an enormous amount of plunder from the city."
    },
    "31": {
      "L": "And he brought out the people who were in it and set them to labor with saws and iron picks and iron axes and made them toil at the brick kilns. And thus he did to all the cities of the children of Ammon. Then David and all the people returned to Jerusalem.",
      "M": "He also brought out the people of the city and set them to work with saws, iron picks, and iron axes, and put them at the brick kilns. He did this to all the cities of the Ammonites. Then David and the whole army returned to Jerusalem.",
      "T": "He brought the people out and put them to work—under saws, iron picks, and axes, and at the brick kilns. He did this to all the cities of Ammon. Then David and all the army returned to Jerusalem."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '2samuel')
        merge_tier(existing, SAMUEL, tier_key)
        save(tier_dir, '2samuel', existing)
    print('2 Samuel 7–12 written.')

if __name__ == '__main__':
    main()
