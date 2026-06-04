"""
MKT 2 Chronicles chapters 1–6 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-2chronicles-1-6.py

Content:
- Ch 1: Solomon at Gibeon — wisdom granted; wealth and horses
- Ch 2: Temple preparations — correspondence with Huram of Tyre; the Name theology
- Ch 3: Building the Temple — Moriah identified; dimensions, cherubim, pillars
- Ch 4: Temple furnishings — bronze altar, molten sea, lavers, lampstands, tables
- Ch 5: Ark brought into the completed Temple — cloud and glory fill the house
- Ch 6: Solomon's dedicatory prayer — Davidic covenant rehearsed; seven intercessions

Translation decisions:
- H3068 (יהוה): "LORD" in L/M; "the LORD" in T. Consistent with all prior OT scripts.
- H430 (אֱלֹהִים): "God" throughout all tiers.
- H2617 (חֶסֶד): "steadfast love" in L/M; "covenant loyalty" in T (1:8, 6:14, 6:42).
  No English word covers chesed's range of covenant obligation + active kindness.
- H8034 (שֵׁם, "name"): "name" in all tiers. The Name theology is central: Solomon builds
  "a house for the name of the LORD" (2:1, 2:4, 6:5-10) — not to contain God but to make
  the divine name present. T surfaces this distinction.
- H3519 (כָּבוֹד, "glory"): "glory" in L/M; T notes the weight and overwhelming presence
  of the divine כָּבוֹד filling the Temple (5:14).
- H7931 (שָׁכַן, "dwell/tabernacle"): "dwell" in L/M; T notes the irony that Solomon asks
  in 6:18 whether God can "dwell with man on earth" — the very verb of the Tabernacle.
- H6205 (עֲרָפֶל, "thick darkness") at 6:1: "thick darkness" in L/M; T notes this is the
  same term for the cloud at Sinai — divine presence is both revealed and concealed.
- H4725 (מָקוֹם, "place") in ch 6: "this place" / "place" — the Deuteronomic appointed
  place formula. T surfaces the theological weight of "the place where you set your name."
- H8064 (שָׁמַיִם, "heavens"): "heaven/heavens" in all tiers. "Your dwelling place in heaven"
  (6:21, 27, 30, 33, 35, 39) is the structural answer to 6:18's rhetorical question.
- H1285 (בְּרִית): "covenant" throughout.
- H4150 (מוֹעֵד): "tent of meeting" — the wilderness sanctuary at Gibeon (ch 1, 5).
- H2022 מוֹרִיָּה (Moriah) at 3:1: "Mount Moriah" — Chronicles uniquely identifies the
  Temple mount with the site of the Aqedah (Gen 22:2); this theological move is noted in T.
- H1116 (בָּמָה, "high place") at 1:3-13: "high place" in L/M; T notes that Gibeon was
  the legitimate sanctuary before the Temple — not a pagan site in this context.
- H5178 (נְחֹשֶׁת): "bronze" throughout (not "brass" as in KJV).
- Aspect: Chronicles uses waw-consecutive imperfects for the narrative of chs 1-5, shifting
  to direct speech in ch 6. The dedicatory prayer uses mixed aspects: qatal (completed facts),
  imperfect jussive (petitions), and infinitives construct (purpose clauses). Rendered
  accordingly: narrative past, petition present, and purpose "so that/in order that."
- OT intertextuality:
  - 1:3-6: Gibeon was the site of the tabernacle; 1 Chr 16:39-40 explains how the
    Mosaic tent of meeting ended up there separate from the ark.
  - 3:1: Mount Moriah = Gen 22:2 (the Aqedah) — the Temple occupies the most
    theologically loaded piece of real estate in the narrative. T notes explicitly.
  - 5:13-14: The cloud filling the temple echoes Exod 40:34-35 (tabernacle) and 1 Kgs 8:10-11.
    The Shekinah's arrival is the theological vindication of the entire building project.
  - 6:16: "walk before me as David your father walked" — the Davidic standard becomes the
    covenant condition; Solomon's wisdom now measured against his father's heart.
  - 6:41-42: Solomon quotes Ps 132:8-10 — one of the psalms of ascents associated with
    the ark's procession. The prayer closes with Scripture. T notes this.
  - 6:14: "there is no God like you" — echoes Moses' song (Deut 4:39) and the Shema context.
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

CHRONICLES2 = {
  "1": {
    "1": {
      "L": "And Solomon the son of David was strengthened in his kingdom, and the LORD his God was with him and magnified him exceedingly.",
      "M": "Solomon son of David established himself firmly in his kingdom, and the LORD his God was with him and made him exceedingly great.",
      "T": "Solomon son of David took firm hold of his kingdom, and the LORD his God was with him — making him greater and greater. The Chronicler's opening line does double work: it signals divine blessing and sets the theological standard for everything that follows. A king who holds his throne because God is with him holds it on entirely different terms than a king who takes it by force."
    },
    "2": {
      "L": "Then Solomon spoke to all Israel, to the commanders of thousands and of hundreds, and to the judges, and to every prince in all Israel, the heads of the fathers' houses.",
      "M": "Solomon addressed all Israel — the commanders of thousands and hundreds, the judges, and every leader throughout Israel, the heads of the ancestral families.",
      "T": "Solomon's first act was to summon all Israel — military commanders, civil judges, every tribal leader and head of a family. It was a royal assembly of the whole nation. Nothing that follows is done in private; the worship at Gibeon and everything leading to the Temple is a corporate, public act of the people."
    },
    "3": {
      "L": "And Solomon and all the assembly with him went to the high place that was at Gibeon, for there was the tent of meeting of God, which Moses the servant of the LORD had made in the wilderness.",
      "M": "Solomon and the whole assembly went to the high place at Gibeon, for the tent of meeting of God was there — the one that Moses the servant of the LORD had made in the wilderness.",
      "T": "The entire assembly made the pilgrimage to Gibeon — the high place that housed the ancient tent of meeting, the very tabernacle Moses had built in the wilderness. This was not a pagan shrine but the legitimate sanctuary, the oldest dwelling-place of the divine name on Israelite soil. The ark was in Jerusalem (v. 4), but the tent and its bronze altar remained at Gibeon."
    },
    "4": {
      "L": "But the ark of God David had brought up from Kiriath-jearim to the place that David had prepared for it, for he had pitched a tent for it in Jerusalem.",
      "M": "The ark of God, however, David had brought up from Kiriath-jearim to the place David had prepared for it, pitching a tent for it in Jerusalem.",
      "T": "The ark was not at Gibeon — David had already brought it to Jerusalem and pitched a special tent for it there (1 Chr 15–16). So Israel's sacred center was divided: the tent of meeting with the bronze altar at Gibeon, and the ark in Jerusalem. Building the Temple would at last unite them. The Chronicler carefully explains this geography so the reader understands why the assembly went south to Gibeon rather than to the ark."
    },
    "5": {
      "L": "Moreover the bronze altar that Bezalel the son of Uri, the son of Hur, had made was there before the tabernacle of the LORD, and Solomon and the assembly sought it.",
      "M": "The bronze altar that Bezalel son of Uri, son of Hur, had made stood before the tabernacle of the LORD, and Solomon and the assembly went there to seek God.",
      "T": "The bronze altar at Gibeon was the one Bezalel had hammered out in the wilderness — crafted by the Spirit-filled craftsman of Exodus (Exod 31:2-5). To approach this altar was to approach the oldest authorized worship-place in Israel's memory. Solomon was not improvising; he was seeking God at the right place, through the right channel."
    },
    "6": {
      "L": "And Solomon went up there to the bronze altar before the LORD that was at the tent of meeting, and offered a thousand burnt offerings on it.",
      "M": "Solomon went up to the bronze altar before the LORD at the tent of meeting and offered a thousand burnt offerings on it.",
      "T": "A thousand burnt offerings — the entire animal given to God, nothing held back for the worshiper. Solomon's first act as king was not a military campaign or a diplomatic treaty but lavish, extravagant sacrifice. The number signals total consecration: this king begins his reign by burning everything before the LORD."
    },
    "7": {
      "L": "In that night God appeared to Solomon and said to him, 'Ask what I shall give you.'",
      "M": "That night God appeared to Solomon and said, 'Ask what you want me to give you.'",
      "T": "God came to Solomon that very night — the night of the thousand offerings — with a blank-check invitation: ask for anything. The sequence matters: the sacrifice came first, the vision second. Solomon did not calculate his offering to manipulate a divine response; the LORD answered the worshiper with an unimaginable gift."
    },
    "8": {
      "L": "And Solomon said to God, 'You have shown great steadfast love to David my father, and have made me king in his place.'",
      "M": "Solomon replied to God, 'You have shown great steadfast love to my father David and have made me king in his place.'",
      "T": "Solomon's first words are not a request but a confession of grace — he begins by naming what God has already done. The great chesed shown to David, the covenant loyalty that stood behind every promise God made to his father — that same faithfulness has now placed Solomon on the throne. He comes to God as a recipient of prior grace, not as a petitioner making his opening bid."
    },
    "9": {
      "L": "Now O LORD God, let your word to David my father be established, for you have made me king over a people as numerous as the dust of the earth.",
      "M": "Now, LORD my God, let your promise to my father David be confirmed, for you have made me king over a people as numerous as the dust of the earth.",
      "T": "Solomon's petition is not primarily for himself but for God's faithfulness to his father. 'Let your word to David stand firm' — the whole weight of the Davidic covenant is what Solomon brings forward. Then the second clause strikes with awe: this people over whom I reign is as vast as the dust of the earth. The imagery echoes Abraham's covenant (Gen 13:16). Solomon is standing at the convergence of every promise God ever made."
    },
    "10": {
      "L": "Give me now wisdom and knowledge so that I may go out and come in before this people, for who can govern this your great people?",
      "M": "Give me wisdom and knowledge so that I may lead this people, for who can govern this great people of yours?",
      "T": "The request is disarmingly simple: wisdom and knowledge to lead. Solomon does not ask how to rule but whether he can. 'Who can govern this great people of yours?' is a question that implies its own answer — no one, apart from God's equipping. The humility of the request is the theological point: the king who knows he cannot govern is the king fit to govern."
    },
    "11": {
      "L": "And God said to Solomon, 'Because this was in your heart, and you have not asked for riches, wealth, or honor, or the life of those who hate you, nor have you asked for many days, but have asked for wisdom and knowledge for yourself in order to govern my people over whom I have made you king—'",
      "M": "God said to Solomon, 'Because this was in your heart — you did not ask for wealth, riches, or honor, or the death of your enemies, or even long life — but you asked for wisdom and knowledge so you could govern my people over whom I have made you king —'",
      "T": "God's response begins not with the grant but with an observation about Solomon's heart. The list of things not asked is revealing: wealth, honor, enemy's death, long life — every temptation of kingship, everything a young ruler might covet. Solomon bypassed them all. And God, who knows the heart, declares what was actually there: not greed, not ambition, but the single desire to govern well. This is what pleases God — the heart aligned with the task."
    },
    "12": {
      "L": "'wisdom and knowledge are granted to you. I will also give you riches, wealth, and honor, such as no king who was before you had, nor shall any after you have.'",
      "M": "'wisdom and knowledge are granted to you. I will also give you riches, wealth, and honor such as no king before you had, and none after you will have.'",
      "T": "'Wisdom and knowledge — granted.' The thing asked for is given without condition or delay. But then God does the unexpected: everything Solomon did not ask for, God adds. Riches, wealth, honor beyond any king before or after. The one who sought what mattered most received everything else as surplus. Jesus would later name this same principle (Matt 6:33): seek the kingdom first, and all these things will be added to you."
    },
    "13": {
      "L": "So Solomon came from the high place that was at Gibeon, from before the tent of meeting, to Jerusalem. And he reigned over Israel.",
      "M": "So Solomon returned from the high place at Gibeon — from before the tent of meeting — to Jerusalem, and he reigned over Israel.",
      "T": "Solomon returns from Gibeon to Jerusalem — from the old sanctuary to the city where the ark was, where the Temple would be built. The journey is geographical and theological. He has been commissioned, equipped, and enlarged by God. Now he reigns. The Chronicler says it simply: he reigned over Israel. Everything else in 2 Chronicles unfolds from that deceptively plain sentence."
    },
    "14": {
      "L": "And Solomon gathered chariots and horsemen. He had fourteen hundred chariots and twelve thousand horsemen, and he stationed them in the chariot cities and with the king at Jerusalem.",
      "M": "Solomon built up a force of chariots and cavalry — fourteen hundred chariots and twelve thousand horsemen, stationed in the chariot cities and with the king in Jerusalem.",
      "T": "The wealth pours in immediately — fourteen hundred chariots, twelve thousand horsemen. The Chronicler records this as fulfillment of God's promise ('riches and honor,' v. 12), though the reader with Deuteronomy in view will hear a faint warning: Moses had forbidden the king from 'multiplying horses' (Deut 17:16). Solomon stands at the edge of faithfulness. The Chronicler reports the fact; the tension is real."
    },
    "15": {
      "L": "And the king made silver and gold as plentiful in Jerusalem as stones, and cedars he made as plentiful as the sycamores of the foothills.",
      "M": "The king made silver and gold as common in Jerusalem as stones, and cedar as plentiful as the sycamore trees of the western foothills.",
      "T": "Silver as common as stones on the road. Cedar — precious imported timber — as ubiquitous as the native sycamore-figs of the lowlands. The exaggeration is rhetorical and intentional: Israel under Solomon lived in a golden age of abundance that later generations would look back on as the standard of prosperity never again matched. The Chronicler invites a moment of wonder before the complications of the reign begin."
    },
    "16": {
      "L": "And the horses which Solomon had were brought out of Egypt and from Kue; the king's traders would acquire them from Kue at a price.",
      "M": "Solomon's horses were imported from Egypt and Kue; the royal traders obtained them from Kue at an established price.",
      "T": "The trade routes are named: Egypt and Kue (Cilicia in southern Turkey). The king's merchants worked the international markets. Horses from Egypt — the same land Israel fled in the Exodus, the country Moses warned Israel never to return to for more horses (Deut 17:16). The Chronicler does not editorialize here; he simply records. But the reader knows."
    },
    "17": {
      "L": "They imported from Egypt a chariot for six hundred shekels of silver, and a horse for a hundred and fifty; and so, through them, they were exported to all the kings of the Hittites and the kings of Aram.",
      "M": "A chariot from Egypt cost six hundred shekels of silver, and a horse a hundred and fifty. Through Solomon's traders, these were also exported to all the kings of the Hittites and the kings of Aram.",
      "T": "Solomon's court ran an international arms-and-horses trading operation. Six hundred shekels per chariot; a hundred and fifty per horse. The prices are preserved with the precision of a merchant's ledger. Israel under Solomon was not merely wealthy but economically central — the middleman between Egypt and the kingdoms of the north. The empire God promised Abraham had become a commercial empire. Whether this is glory or warning, the text holds both possibilities open."
    }
  },
  "2": {
    "1": {
      "L": "Now Solomon purposed to build a house for the name of the LORD, and a house for his kingdom.",
      "M": "Solomon decided to build a house for the name of the LORD and a palace for his own royal use.",
      "T": "Two buildings, one decision. The Temple comes first — 'a house for the name of the LORD' — but Solomon's own palace is part of the same determination. The Name theology is already present in this first sentence: Solomon is not building a house for God to live in (6:18 will address that question directly) but a house where the divine name dwells, the focal point of Israel's worship and prayer."
    },
    "2": {
      "L": "Solomon counted seventy thousand men to bear burdens and eighty thousand to quarry in the hill country, and three thousand six hundred to oversee them.",
      "M": "Solomon conscripted seventy thousand burden-bearers, eighty thousand stone-cutters in the hill country, and thirty-six hundred foremen to supervise them.",
      "T": "The scale is staggering: one hundred fifty thousand workers, plus thousands of foremen. Building the Temple was not a craft project but a national industrial undertaking. Every Israelite would have known someone who labored on the Temple; the building wove itself into the social fabric of a generation."
    },
    "3": {
      "L": "And Solomon sent word to Huram the king of Tyre: 'As you dealt with David my father and sent him cedar timber to build himself a house to dwell in, so deal with me.'",
      "M": "Solomon sent this message to Huram king of Tyre: 'Deal with me as you dealt with my father David, when you sent him cedar to build himself a house to live in.'",
      "T": "Solomon opens the diplomatic correspondence by invoking his father. Huram and David had a working relationship — trade, materials, goodwill. Solomon's first move is to claim that legacy: deal with me as you dealt with him. The appeal to his father's covenant relationship is both politically savvy and personally honest. He is David's son, and that lineage is his calling card."
    },
    "4": {
      "L": "'Behold, I am about to build a house for the name of the LORD my God, to dedicate it to him for the burning of sweet incense before him, for the regular arrangement of the showbread, and for burnt offerings morning and evening, on Sabbaths and new moons and appointed feasts of the LORD our God, as ordained forever for Israel.'",
      "M": "'I am going to build a house for the name of the LORD my God and consecrate it to him for burning fragrant incense, for the regular display of the bread of the Presence, for burnt offerings morning and evening, and for offerings on Sabbaths, new moons, and the appointed feasts of the LORD our God — this is Israel's obligation forever.'",
      "T": "Solomon explains himself to Huram not as a king soliciting a business partner but as a servant of God fulfilling an obligation. The Temple is 'for the name of the LORD my God' — but then Solomon immediately fills that abstract phrase with concrete liturgical content: incense, showbread, morning and evening offerings, Sabbath and feast worship. The Name dwells in a place of ordered, daily, uninterrupted worship. This is what Solomon is building: a permanent house of prayer for all of Israel's generations."
    },
    "5": {
      "L": "'The house that I am building will be great, for our God is greater than all gods.'",
      "M": "'The house I am building will be great, for our God is greater than all gods.'",
      "T": "A single sentence carrying enormous weight. The Temple's greatness is not architectural ambition but theological declaration: our God exceeds all others. Solomon is not in competition with the temples of Tyre or Egypt or Babylon; he is making a statement about the category difference between the LORD and every other divine claimant. The Temple's scale is a sermon in stone."
    },
    "6": {
      "L": "'But who is able to build him a house, since heaven, even highest heaven, cannot contain him? And who am I to build him a house, except as a place to make offerings before him?'",
      "M": "'But who is really able to build him a house? The highest heavens cannot contain him! So who am I to build him a house — only as a place where offerings can be made before him?'",
      "T": "Having declared God's greatness, Solomon immediately undercuts any pretension that the Temple could house or contain that greatness. The highest heavens — the plural of majesty, the uttermost reaches of the cosmos — cannot contain God. A building made of cedar and stone certainly cannot. So what is the Temple? A place to make offerings before him. Not a cage for God but an altar for humans, a designated meeting point where the infinite makes himself accessible to the finite. This is Solomon's theology of the Temple, stated before the first stone is laid."
    },
    "7": {
      "L": "'Now send me a skilled man to work in gold, silver, bronze, iron, in purple, crimson, and blue, and who knows how to engrave, to be with the skilled craftsmen who are with me in Judah and Jerusalem, whom David my father provided.'",
      "M": "'Now send me a craftsman skilled in working with gold, silver, bronze, and iron, as well as in purple, crimson, and blue fabrics, and in engraving — to work with the craftsmen I have in Judah and Jerusalem whom my father David assembled.'",
      "T": "The theological groundwork laid, Solomon turns practical. He needs a master craftsman — someone with the breadth of Bezalel, the Exodus artisan. Gold, silver, bronze, iron, textiles, engraving — the same skill set used in building the tabernacle. Solomon has craftsmen of his own, inherited from David, but he needs the best Phoenician expertise to work alongside them. The Temple will be an international collaboration."
    },
    "8": {
      "L": "'Send me also cedar, cypress, and algum timber from Lebanon, for I know that your servants know how to cut timber in Lebanon. And my servants will work alongside your servants,'",
      "M": "'Also send me cedar, cypress, and algum timber from Lebanon — I know your servants are expert at cutting Lebanese timber — and my servants will work with yours'",
      "T": "Lebanon's forests were the premier timber source of the ancient Near East, and Phoenician woodcutters their acknowledged masters. Solomon is not just placing an order; he is inviting a joint venture. His workers alongside Huram's workers in the mountain forests. The Temple will be built by many hands from many places — a foretaste of the prayer in chapter 6 for foreigners who come to pray there."
    },
    "9": {
      "L": "'to prepare timber for me in abundance, for the house that I am to build will be great and wonderful.'",
      "M": "'to prepare timber for me in great quantity, for the house I am going to build must be magnificent and wonderful.'",
      "T": "Great and wonderful — the Hebrew pair suggests both scale (rav, great in quantity) and astonishment (pala', wonderful, the same root as the word for miracles). Solomon is aiming for a building that will make people stop and stare, a house whose beauty points beyond itself to the beauty of the One whose name dwells there."
    },
    "10": {
      "L": "'I will give your servants, the woodcutters who cut timber, twenty thousand cors of crushed wheat, twenty thousand cors of barley, twenty thousand baths of wine, and twenty thousand baths of olive oil.'",
      "M": "'For your servants, the workers who fell the timber, I will provide: twenty thousand cors of ground wheat, twenty thousand cors of barley, twenty thousand baths of wine, and twenty thousand baths of olive oil.'",
      "T": "The payment is specified in agricultural produce — the currency of the ancient Near East. Twenty thousand cors is roughly 110,000 bushels of wheat; the same of barley; twenty thousand baths of wine and oil. These are staggering quantities for a building project. Solomon is not bartering; he is signaling that Israel's agricultural abundance — the blessing of the land — will fund the house of the Name. The land's fertility flows toward the Temple."
    },
    "11": {
      "L": "Then Huram the king of Tyre answered in writing and sent it to Solomon: 'Because the LORD loves his people, he has made you king over them.'",
      "M": "Huram king of Tyre replied in a letter to Solomon: 'Because the LORD loves his people, he has made you their king.'",
      "T": "Huram's opening sentence is a confession of faith — remarkable on the lips of a Phoenician king. Whether he means it theologically or diplomatically, the Chronicler reports it without irony: 'Because the LORD loves his people, he made you king.' The pagan ally recognizes what Solomon himself declared at Gibeon — this throne was given, not taken. Even the nations can perceive the love of the LORD at work in Israel."
    },
    "12": {
      "L": "Huram also said, 'Blessed be the LORD, the God of Israel, who made heaven and earth, who has given King David a wise son, endued with discretion and understanding, who will build a house for the LORD and a royal house for himself.'",
      "M": "Huram continued: 'Praised be the LORD, the God of Israel, maker of heaven and earth, who has given King David a wise son with discernment and understanding, to build a house for the LORD and a palace for his own rule.'",
      "T": "Huram blesses the LORD as 'maker of heaven and earth' — the widest possible designation of divine sovereignty, the LORD who exceeds every territorial or national deity. The praise is remarkable: a Phoenician king blessing the God of Israel by his covenant name and his cosmic title. Then Huram names what David's son is: wise, discerning, understanding — the very qualities Solomon asked for (v. 10). The answer to Solomon's prayer is already visible in the character Huram perceives."
    },
    "13": {
      "L": "'Now I have sent a skilled man, endued with understanding, Huram-abi,'",
      "M": "'I am sending you a skilled craftsman of great ability: Huram-abi.'",
      "T": "Huram delivers what Solomon asked for: a master craftsman, Huram-abi ('Huram my father' — a title of respect, not necessarily biological). The name echoes the tradition of Bezalel; the skills listed in the next verse mirror the skills of the tabernacle craftsmen. The Chronicler is drawing an invisible line: as God equipped Bezalel to build the wilderness sanctuary, he is now equipping Huram-abi to help build the permanent one."
    },
    "14": {
      "L": "'the son of a woman of the daughters of Dan, and his father was a man of Tyre. He is trained to work in gold, silver, bronze, iron, stone, and wood, and in purple, blue, fine linen, and crimson, and in engraving any kind of engraving, and in executing any design that may be assigned to him with your craftsmen and with the craftsmen of my lord David your father.'",
      "M": "'His mother was from Dan and his father from Tyre. He is expert in working gold, silver, bronze, iron, stone, and wood, and in purple, blue, fine linen, and crimson fabrics, and skilled in all kinds of engraving and carrying out any design he is given. He will work with your craftsmen and those of my lord, your father David.'",
      "T": "The skill list covers every material and medium used in the Temple: metals, stone, wood, textiles, engraving. Huram-abi is, effectively, the new Bezalel. His parentage — a woman of Dan (matching the 1 Kings 7:14 tradition of Naphtali in some tension; the Chronicler harmonizes or preserves a different tradition), a Tyrian father — makes him a hybrid craftsman at the junction of Israelite and Phoenician culture. The Temple is built at the meeting-point of traditions, just as the prayer of chapter 6 anticipates foreigners coming to pray there."
    },
    "15": {
      "L": "'And now let my lord send to his servants the wheat, the barley, the olive oil, and the wine of which my lord has spoken.'",
      "M": "'Now let my lord send to his servants the wheat, barley, olive oil, and wine that my lord promised.'",
      "T": "Huram's reply is practical and businesslike. The theology has been exchanged; now the transaction. Send the provisions as promised. The Temple will be built on kept agreements, on workers fed and paid. The sacred and the mundane are not opposed; the LORD's house is built by human hands working under human arrangements."
    },
    "16": {
      "L": "'We will cut wood from Lebanon, as much as you need. We will bring it to you in rafts by sea to Joppa, and you shall carry it up to Jerusalem.'",
      "M": "'We will cut as much timber from Lebanon as you need and float it to you in rafts by sea to Joppa. You can then transport it up to Jerusalem.'",
      "T": "Cedar from the mountains of Lebanon, floated in rafts down to Joppa on the Mediterranean coast, then hauled up the long climb to Jerusalem. The logistics alone tell the story of dedication: every massive beam in the Temple traveled a hundred miles by sea and mountain road before it was set in place. The house of the Name was not built cheaply or easily."
    },
    "17": {
      "L": "Then Solomon counted all the resident aliens who were in the land of Israel, after the census that David his father had taken, and there were found a hundred and fifty-three thousand six hundred.",
      "M": "Solomon took a census of all the resident aliens in the land of Israel — following the count his father David had made — and found a hundred and fifty-three thousand six hundred.",
      "T": "The resident aliens — the gerim, foreigners living under Israelite jurisdiction — are counted separately from the Israelite workforce. There were 153,600 of them. The Chronicler notes this carefully: the Temple is built in part by non-Israelite hands. The house that will later pray for foreigners (6:32-33) is built by foreigners. There is a quiet irony in that fact that the Chronicler does not underline but does not obscure."
    },
    "18": {
      "L": "He assigned seventy thousand of them as burden-bearers and eighty thousand as stonecutters in the hill country, and three thousand six hundred as overseers to make the people work.",
      "M": "He assigned seventy thousand as laborers, eighty thousand as quarrymen in the hills, and thirty-six hundred as foremen keeping the workers on task.",
      "T": "The allocation of the alien workforce: seventy thousand haulers, eighty thousand quarriers, thirty-six hundred supervisors. The Temple foundation stones were cut and carried by people who had no tribal share in Israel, no covenant ancestry in Abraham. Yet the work they did would make possible the house from which Solomon would ask God to hear even the foreigners who came to pray (6:33). The building itself enacts the prayer it would one day shelter."
    }
  },
  "3": {
    "1": {
      "L": "Then Solomon began to build the house of the LORD in Jerusalem on Mount Moriah, where the LORD had appeared to David his father, at the place that David had prepared on the threshing floor of Ornan the Jebusite.",
      "M": "Solomon began building the house of the LORD in Jerusalem on Mount Moriah, where the LORD had appeared to his father David, at the site David had designated — the threshing floor of Ornan the Jebusite.",
      "T": "The site is named with deliberate precision: Mount Moriah. The Chronicler alone among the biblical writers makes this identification explicit (2 Chr 3:1). Moriah is the mountain where Abraham bound Isaac and was stopped by God's angel — the place where God provided a substitute and swore his covenant oath (Gen 22:2, 14). The Temple is built on the very ground where the covenant of life-from-death was established. It is also Ornan's threshing floor, where David saw the angel of destruction and the plague halted — the site of another near-death spared by divine mercy. Every stone of the Temple sits on layers of covenant history."
    },
    "2": {
      "L": "He began to build in the second month of the fourth year of his reign.",
      "M": "He began construction in the second month of the fourth year of his reign.",
      "T": "The Chronicler dates the construction to Solomon's fourth year. The parallel in 1 Kings 6:1 counts 480 years from the Exodus — placing the Temple at the center of Israel's entire redemptive history, the culmination toward which the Exodus itself was heading. The Chronicler omits that calculation but adds the Moriah identification instead. Together the two accounts say the same thing from different angles: this building stands at the intersection of all of God's purposes."
    },
    "3": {
      "L": "These are the foundations that Solomon laid for building the house of God. The length was sixty cubits, by the old standard, and the width twenty cubits.",
      "M": "This is how Solomon laid the foundations for the house of God: the length, measured by the old standard, was sixty cubits, and the width twenty cubits.",
      "T": "Sixty cubits long, twenty wide — the same proportions as the tabernacle nave, scaled up. The 'old standard' cubit was about 20.5 inches. The building is approximately 90 by 30 feet in the nave alone. Every dimension echoes the tabernacle's ratios; the Temple is the wilderness sanctuary made permanent, stone where there was linen, cedar where there was acacia."
    },
    "4": {
      "L": "The vestibule in front of the nave of the house was twenty cubits long, equal to the width of the house, and its height was a hundred and twenty cubits. He overlaid it on the inside with pure gold.",
      "M": "The vestibule in front of the main hall was twenty cubits wide — matching the width of the house — and a hundred and twenty cubits high. He overlaid the inside with pure gold.",
      "T": "A hundred and twenty cubits — roughly 180 feet high. This is either a monumental tower or a textual variant (1 Kgs 6:3 gives 10 cubits); the Chronicler's number may reflect a specific architectural feature not preserved in the parallel account. Whatever the precise height, the vestibule was overlaid with pure gold — the first thing the worshiper passed through was already sheathed in the glory-metal."
    },
    "5": {
      "L": "The main hall he lined with cypress wood and covered it with fine gold, and made palm trees and chains on it.",
      "M": "The main hall he paneled with cypress wood, then covered with fine gold, carving palm trees and chains into it.",
      "T": "Cypress panels overlaid with gold, carved with palms and interlaced chains. Palm trees (temarim) were ancient symbols of life, abundance, and the sacred tree. The chains or festoons linked the carved trees in a pattern of organic abundance. The interior of the Temple was a garden in gold — Eden imagery planted in the sanctuary."
    },
    "6": {
      "L": "He adorned the house with precious stones. The gold was gold of Parvaim.",
      "M": "He decorated the house with precious stones. The gold used was gold of Parvaim.",
      "T": "Parvaim — an unidentified but evidently prestigious gold source, perhaps in Arabia. Precious stones set throughout. The Temple was encrusted with the wealth of the ancient world: gold, stone, timber. Not because God needs jewels but because humans use beauty as the closest earthly language for the holy. The art of the Temple was theology expressed in material."
    },
    "7": {
      "L": "He lined the house, its beams, thresholds, walls, and doors with gold, and he engraved cherubim on the walls.",
      "M": "He overlaid the beams, thresholds, walls, and doors of the house with gold and carved cherubim on the walls.",
      "T": "Every surface — beams, thresholds, walls, doors — gold. Cherubim carved on the walls. The worshiper entering the Temple stepped into a golden garden guarded by angelic figures, the same cherubim who once barred the way back to Eden. Here they are not guardians of exclusion but features of the sanctuary, indicating that this space stands at the boundary between the human and the divine."
    },
    "8": {
      "L": "And he made the Most Holy Place. Its length, corresponding to the width of the house, was twenty cubits, and its width was twenty cubits. He overlaid it with six hundred talents of fine gold.",
      "M": "He built the Most Holy Place, twenty cubits in length and twenty cubits in width — a perfect cube. He overlaid it with six hundred talents of fine gold.",
      "T": "Twenty by twenty — a perfect square, or rather (with the same height) a perfect cube. The Most Holy Place is the only perfect cube in the Temple, just as the New Jerusalem in Revelation 21:16 is a perfect cube. The geometry of perfection: equal in all dimensions, no side greater than another, no axis privileged. Into this cube went six hundred talents of gold — roughly 22 tons. The Most Holy Place was not merely gilded; it was encased in gold."
    },
    "9": {
      "L": "The weight of the nails was fifty shekels of gold. And he overlaid the upper chambers with gold.",
      "M": "The gold nails weighed fifty shekels. He also overlaid the upper chambers with gold.",
      "T": "Even the construction hardware — the nails — were gold. Fifty shekels per nail: these were not functional fasteners but theological statements. In a building where wood met stone met gold met carved angel, even the joining elements participated in the beauty. The upper chambers above the main nave were equally overlaid. There was no corner of the Temple that did not shine."
    },
    "10": {
      "L": "In the Most Holy Place he made two cherubim of carved wood and overlaid them with gold.",
      "M": "In the Most Holy Place he carved two cherubim and overlaid them with gold.",
      "T": "Two carved cherubim in the innermost room, gleaming gold in the lamplight, their wings spread to cover the ark. The cherubim of the tabernacle had been hammered out of the single gold sheet of the mercy seat (Exod 25:18-20). These Temple cherubim are larger — fifteen feet tall — wood overlaid with gold, presiding over the ark with spread wings. They are not idols but attendants, the honor guard of the divine presence."
    },
    "11": {
      "L": "The wings of the cherubim together were twenty cubits in length: the wing of the one, five cubits, reached to the wall of the house, and its other wing, five cubits, reached to the wing of the other cherub;",
      "M": "The combined wingspan of the cherubim was twenty cubits: each wing of the first cherub was five cubits, one touching the wall and the other reaching the second cherub's wing;",
      "T": "A twenty-cubit wingspan combined — roughly thirty feet. Each cherub reached from wall to center, their wingtips meeting over the ark below. The proportions are deliberate: the same twenty cubits as the width of the Most Holy Place, so that the cherubim's outstretched wings exactly filled the room from wall to wall. They covered everything."
    },
    "12": {
      "L": "and the wing of the other cherub, five cubits, reached to the wall of the house, and its other wing, five cubits, reached to the wing of the first cherub.",
      "M": "and each wing of the second cherub was likewise five cubits, one touching the wall and the other meeting the first cherub's wing.",
      "T": "The second cherub mirrors the first: five cubits to the wall, five to the center. Together their wings formed a canopy twenty cubits wide, sheltering the ark beneath in its completeness. Every point of the Most Holy Place was overshadowed. This is the image of protection and presence: to stand under the wings of the cherubim was to stand at the center of divine care."
    },
    "13": {
      "L": "These cherubim spread their wings twenty cubits. They stood on their feet, facing inward.",
      "M": "The wingspan of these cherubim spanned twenty cubits. They stood upright, facing the main hall.",
      "T": "They stood — not crouching, not prostrate, but standing upright on their feet, faces turned toward the nave, toward the worshipers who would enter the outer hall. The cherubim faced the people, not the wall. As if to say: the guardians of the holy place are not indifferent to those who approach. They stand watch, facing outward, ready to meet those who come."
    },
    "14": {
      "L": "And he made the veil of blue, purple, and crimson, and fine linen, and worked cherubim into it.",
      "M": "He made the curtain of blue, purple, and crimson yarn and fine linen, with cherubim woven into it.",
      "T": "The great curtain — the parochet, the veil — hung between the main hall and the Most Holy Place, blue and purple and crimson and fine linen, cherubim woven throughout. It was the threshold between the accessible and the unapproachable, between the priests' daily world and the ark's eternal one. The Gospels will record that this curtain tore from top to bottom when Jesus died — the ripping open of the boundary between God and man. Solomon wove it; God tore it."
    },
    "15": {
      "L": "In front of the house he made two pillars, thirty-five cubits high, and the capital on the top of each was five cubits.",
      "M": "In front of the temple he erected two pillars, each thirty-five cubits high, topped with a capital five cubits tall.",
      "T": "Two pillars at the entrance to the Temple — free-standing, not load-bearing. They were architectural theology: everything about the Temple entrance announced something before you went inside. Thirty-five cubits high (about 52 feet), plus a five-cubit capital — towering markers that said: you are entering a different kind of space."
    },
    "16": {
      "L": "He made chains like a necklace and put them on the tops of the pillars, and he made a hundred pomegranates and put them on the chains.",
      "M": "He made chain-work like necklaces and set them on top of the pillars, with a hundred pomegranates hanging on the chains.",
      "T": "Chains like necklaces, a hundred pomegranates hanging from each. The pomegranate was a symbol of abundance, fertility, and the blessing of the land — its many seeds a visual sermon on fruitfulness. Hung at the entrance to the Temple, they announced: this is the place where God's blessing overflows, where the abundance of Eden is remembered and anticipated."
    },
    "17": {
      "L": "He set up the pillars in front of the temple, one on the south and one on the north; the one on the south he called Jachin, and the one on the north he called Boaz.",
      "M": "He erected the pillars in front of the temple — the southern one he named Jachin and the northern one Boaz.",
      "T": "Jachin and Boaz — two names, two declarations. Jachin (יָכִין): 'He establishes.' Boaz (בֹּעַז): 'In him is strength.' Every Israelite who entered the Temple passed between pillars that proclaimed: God establishes; in God is strength. The names were a creed spoken in stone, a confession of the LORD's sovereignty stated at the threshold of his house. You could not enter without reading the sermon."
    }
  },
  "4": {
    "1": {
      "L": "He made an altar of bronze, twenty cubits long, twenty cubits wide, and ten cubits high.",
      "M": "He made a bronze altar, twenty cubits long, twenty cubits wide, and ten cubits high.",
      "T": "The bronze altar — massive, thirty feet square and fifteen feet high. This is the place of sacrifice, the altar that stood in the open court where every burnt offering and peace offering would be consumed. Its size was proportional to its function: an altar to serve the whole nation, receiving the sacrifices of a people whose God was greater than all gods."
    },
    "2": {
      "L": "Then he made the sea of cast metal. It was round, ten cubits from brim to brim, and five cubits high, and a line of thirty cubits measured its circumference.",
      "M": "He also made the molten sea — circular, ten cubits across and five cubits deep, with a circumference of thirty cubits.",
      "T": "The great bronze sea — a circular basin of cast metal, fifteen feet across, seven and a half feet deep. A line of thirty cubits around its rim. It held three thousand baths of water (about 17,500 gallons) and was used for the priests' ritual washing. Its name, 'the sea' (yam), invokes the vast waters of creation; here in the Temple court they are tamed, set in a vessel, made to serve the purposes of worship."
    },
    "3": {
      "L": "Under it was the likeness of oxen encircling it, ten to a cubit all around. The oxen were in two rows, cast with it when it was cast.",
      "M": "Around the outside were figures of oxen encircling it, ten per cubit, all the way around. The oxen were cast in two rows as part of the same casting.",
      "T": "Ten oxen per cubit around the circumference — hundreds of cast oxen running in two rings around the base. Oxen were symbols of strength, labor, and agricultural blessing. Here they support the great waters, as if the strength of the created order bears up the ritual purity of the priesthood. The sea rests on what the earth produces; the worship of God is grounded in the created world."
    },
    "4": {
      "L": "It stood on twelve oxen, three facing north, three facing west, three facing south, and three facing east. The sea was set above them, and all their rear parts were turned inward.",
      "M": "It rested on twelve oxen — three facing north, three facing west, three facing south, and three facing east — with the sea on top and all their hindquarters facing inward.",
      "T": "Twelve oxen bearing the sea — three to each compass point, covering every direction of the world. The Temple's ritual sea was supported by a symbol of the whole creation, facing outward to every nation and every place. Just as the prayer of chapter 6 will petition God to hear from 'heaven your dwelling place' when people in every situation call out, so the great sea rests on creation itself, oriented to the whole earth."
    },
    "5": {
      "L": "Its thickness was a handbreadth. Its rim was made like the rim of a cup, like a lily blossom. It held three thousand baths.",
      "M": "Its walls were a handbreadth thick, and its rim was shaped like the rim of a cup, like a lily flower in bloom. It held three thousand baths.",
      "T": "A lily-rimmed bowl — functional and beautiful, utilitarian and artistic. The craftsman who could have left the rim plain chose instead to shape it like a flower opening. This is the aesthetics of temple worship: even the functional vessels proclaim the beauty of God. Three thousand baths of water — roughly 17,500 gallons — held in a vessel that looked like a lily. Holiness and beauty were never in tension here."
    },
    "6": {
      "L": "He also made ten basins in which to wash, and set five on the south side and five on the north side. In these they rinsed off what was used for the burnt offering, but the sea was for the priests to wash in.",
      "M": "He made ten basins for washing, placing five on the south side and five on the north. In these they washed the parts used in the burnt offerings. The great sea was for the priests to wash themselves.",
      "T": "Ten smaller lavers for the sacrificial work; the great sea for the priests themselves. The distinction matters: the lavers served the offerings, the sea served the offerers. The whole system of ritual washing encoded a theology of purity — what is brought before God must be clean, and the ones who bring it must also be clean. The architecture enacted the requirement before a word of instruction was spoken."
    },
    "7": {
      "L": "And he made ten golden lampstands as prescribed, and set them in the temple, five on the south side and five on the north side.",
      "M": "He made ten gold lampstands according to the prescribed pattern and placed them in the temple — five on the south side, five on the north.",
      "T": "Ten lampstands of gold — not the single seven-branched menorah of the tabernacle but ten, five per side, filling the nave with light. The interior of the Temple, entered through gold-covered doors, enclosed by gold-covered walls, would have blazed with reflected lamplight. To enter the Temple was to step into radiance. The light was not natural; it was the light of consecrated worship."
    },
    "8": {
      "L": "He made ten tables and placed them in the temple, five on the south side and five on the north side. And he made a hundred basins of gold.",
      "M": "He made ten tables and set them in the temple, five on the south side and five on the north. He also made a hundred gold bowls.",
      "T": "Ten tables for the bread of the Presence — fivefold the tabernacle's single table. A hundred gold bowls. The multiplication of every element from the tabernacle pattern signals expansion: what Israel had in the wilderness is now multiplied for a settled nation. The tabernacle was sufficient for a nomadic people; the Temple serves a kingdom. The abundance of the furnishings is the abundance of God's provision for his people's worship."
    },
    "9": {
      "L": "And he made the court of the priests and the great court, and doors for the great court, and he overlaid their doors with bronze.",
      "M": "He built the court of the priests and the large outer court, with bronze-covered doors on the outer court.",
      "T": "Two courts: the priests' court, closer to the Temple, where the sacrifices were performed; and the great outer court where the people gathered. Two concentric spaces of graduated holiness. The doors between them — bronze, not gold — marked the transition from public assembly to priestly service. The architecture mapped the theology: there are zones of approach, and each zone has its own requirements."
    },
    "10": {
      "L": "And he set the sea at the right side of the house, toward the southeast.",
      "M": "He positioned the great sea on the south side of the house, at the southeast corner.",
      "T": "The sea at the southeast, the right side as one faces east. Orientation mattered in the Temple — worshipers faced west, toward the Most Holy Place; east was the direction of the sunrise and of the morning offering. The great sea, the ritual washing place, stood at the corner between the morning and the south, between beginning and warmth. Even the placement of furnishings was spatial theology."
    },
    "11": {
      "L": "Huram made the pots, the shovels, and the basins. So Huram finished doing the work that he did for King Solomon for the house of God:",
      "M": "Huram made the pots, shovels, and basins. So Huram completed all the work he undertook for King Solomon on the house of God:",
      "T": "Huram-abi, the master craftsman sent by Tyre, finishes his commission. Pots, shovels, basins — the working hardware of the altar, unglamorous but essential. The list that follows (vv. 12-18) is the accounting of his completed work. The Chronicler records it with care: every piece made, every craftsman's contribution preserved. The Temple was built by named people, not anonymous forces."
    },
    "12": {
      "L": "the two pillars, the bowls, and the two capitals on top of the pillars; and the two networks to cover the two bowls of the capitals that were on top of the pillars;",
      "M": "the two pillars, the bowl-shaped capitals on top of them, and the two networks of chains that covered the bowls of the capitals;",
      "T": "The inventory of Huram's work begins with the defining features of the Temple entrance — the two great pillars and their elaborate capitals. Every element is documented as completed. The Chronicler's inventory is an act of honor: this is what was made, by whom, for what purpose. Nothing is forgotten."
    },
    "13": {
      "L": "and the four hundred pomegranates for the two networks, two rows of pomegranates for each network, to cover the two bowls of the capitals that were on top of the pillars.",
      "M": "and four hundred pomegranates for the two networks — two rows per network — covering the bowl-shaped capitals on top of the pillars.",
      "T": "Four hundred pomegranates — two hundred per pillar. At the threshold of the Temple, abundant fruitfulness in bronze hung in rows, the symbol of the land's plenty flanking the entrance to the house of the LORD. Every worshiper entered through a harvest."
    },
    "14": {
      "L": "He also made the stands, and the basins on the stands,",
      "M": "He made the movable stands and the basins mounted on them,",
      "T": "The ten wheeled stands that Huram made (elaborated in 1 Kgs 7:27-37) were practical and decorative: movable bases for the lavers, themselves objects of craft — bronze frames with panels carved with lions, oxen, and cherubim. Functionality and artistry were not separable in Temple design."
    },
    "15": {
      "L": "one sea, and the twelve oxen under it.",
      "M": "one great sea with the twelve oxen beneath it.",
      "T": "The sea and its twelve oxen — listed together as a single, inseparable unit. The sea does not stand alone; it stands on the strength of the twelve. The liturgical vessel and its cosmological support belong together. Worship does not float free of the created order; it stands on it."
    },
    "16": {
      "L": "The pots, the shovels, the forks, and all their equipment — all these items for the house of the LORD that Huram-abi made for King Solomon were of burnished bronze.",
      "M": "The pots, shovels, meat forks, and all related equipment that Huram-abi made for King Solomon for the LORD's house were of polished bronze.",
      "T": "Burnished bronze — hammered and polished until it shone. Even the pots and meat-forks, the most utilitarian tools of the sacrifice, were made with care. In the Temple, nothing was careless. The craftsman's attention to the unglamorous implements was an act of worship: the LORD is honored not only in the gold of the Most Holy Place but in the gleam of every cooking fork in the outer court."
    },
    "17": {
      "L": "In the plain of the Jordan the king cast them, in the clay ground between Succoth and Zeredah.",
      "M": "The king had them cast in the clay ground of the Jordan plain, between Succoth and Zeredah.",
      "T": "The casting work happened in the Jordan Valley — where the clay soil was ideal for making molds. Between Succoth and Zeredah: the same territory where Jacob had camped and built booths (Gen 33:17), now a foundry for the Temple's bronze. The Jordan Valley, the land of Jacob's journey and of Israel's crossing into Canaan, now served as the metalworks for the eternal house."
    },
    "18": {
      "L": "Solomon made all these things in great quantity, so that the weight of the bronze was not determined.",
      "M": "Solomon made all these vessels in such quantity that the total weight of the bronze was never calculated.",
      "T": "Beyond counting. The weight of the bronze used for the Temple was so immense it was never measured. This is abundance as theological statement: the God who fills the highest heavens has a house furnished with uncountable bronze. The contrast between the unmeasurable weight of the bronze and the unmeasurable expanse of the heavens (6:18) is part of the Chronicler's own irony — the greatest earthly abundance cannot begin to contain the God it is meant to honor."
    },
    "19": {
      "L": "So Solomon made all the vessels that were in the house of God: the golden altar, the tables for the bread of the Presence,",
      "M": "Solomon also made all the furnishings for the house of God: the golden altar, the tables for the bread of the Presence,",
      "T": "From the outer-court bronze to the inner-sanctuary gold. The golden altar of incense and the tables for the showbread — these are the furnishings of daily priestly ministry, the constant offering of bread and incense that marked every morning and evening of Israel's worship."
    },
    "20": {
      "L": "the lampstands and their lamps of pure gold to burn before the inner sanctuary as prescribed,",
      "M": "the lampstands of pure gold with their lamps to burn before the inner sanctuary, as the specifications required,",
      "T": "Pure gold lampstands, burning day and night before the veil. The light that filled the nave of the Temple was the unending light of worship — never allowed to go out. A fire that was never quenched mirrored the unending nature of the worship it illuminated."
    },
    "21": {
      "L": "the flower work, the lamps, and the tongs, of gold — and that of perfect gold —",
      "M": "the floral decorations, lamps, and tongs of purest gold,",
      "T": "Flower-shaped ornaments on the lampstands, tongs to tend the wicks — even the maintenance tools were gold, and not just gold but 'perfect gold,' the most refined. The Chronicler adds this qualification with emphasis: when it comes to what stands nearest to the Most Holy Place, the standard is perfection. Proximity to the holy demands the best."
    },
    "22": {
      "L": "the snuffers, the basins, the dishes, and the fire pans of pure gold; and the sockets of the temple — the inner doors for the Most Holy Place and the doors of the main hall — of gold.",
      "M": "the wick trimmers, sprinkling bowls, ladles, and fire pans of pure gold; and the door sockets of the temple — the doors to the Most Holy Place and the doors of the main hall — all gold.",
      "T": "The full inventory closes: snuffers, basins, ladles, fire pans — everything needed for the lamp and altar ministry — all of pure gold. And the doors themselves: the doors to the Most Holy Place and the doors of the main hall, mounted on golden sockets. Gold from threshold to innermost room, from hinges to altars. The Temple was a unified vision of worship, every element speaking the same language of consecrated beauty."
    }
  },
  "5": {
    "1": {
      "L": "Thus all the work that Solomon did for the house of the LORD was finished. And Solomon brought in the things that David his father had dedicated — the silver, the gold, and all the vessels — and stored them in the treasuries of the house of God.",
      "M": "All the work Solomon did on the house of the LORD was completed. He then brought in what his father David had dedicated — the silver, gold, and all the vessels — and stored them in the treasuries of the house of God.",
      "T": "Finished. The word carries the finality of a great completion: all that Solomon did — years of labor by hundreds of thousands of workers — was finished. And now the last act before the dedication: David's dedicated treasures, accumulated over a lifetime of preparation, are brought in and stored in the temple treasury. Father and son together, across the boundary of death, fill the house. What David gathered, Solomon houses. The generations are united in the completed Temple."
    },
    "2": {
      "L": "Then Solomon assembled the elders of Israel and all the heads of the tribes, the leaders of the ancestral houses of the people of Israel, in Jerusalem, to bring up the ark of the covenant of the LORD out of the city of David, which is Zion.",
      "M": "Solomon then summoned to Jerusalem all the elders of Israel and all the tribal heads — the leaders of the Israelite ancestral families — to bring the ark of the LORD's covenant up from the city of David, that is, from Zion.",
      "T": "The ark had waited in Zion since David brought it up from Kiriath-jearim (1 Chr 15). Now it was the Temple's turn. Solomon calls the full leadership of Israel — elders, tribal heads, family leaders — to make the final procession. The ark's journey from Zion to the Temple was the culminating act of the entire Davidic-Solomonic project, and it required all Israel to witness it."
    },
    "3": {
      "L": "And all the men of Israel assembled before the king at the feast that is in the seventh month.",
      "M": "All the Israelite men assembled before the king at the feast in the seventh month.",
      "T": "The seventh month — Tishri, the month of the Feast of Booths (Sukkot), the great harvest celebration and the feast commemorating Israel's wilderness journey. The timing was intentional: the ark's entrance into the Temple happened at the festival that recalled the wilderness, when God's presence had traveled with Israel in the tabernacle. As the tabernacle was Israel's companion in the wilderness, the Temple would be God's dwelling place in the land."
    },
    "4": {
      "L": "And all the elders of Israel came, and the Levites took up the ark.",
      "M": "When all the elders of Israel had arrived, the Levites took up the ark.",
      "T": "The Levites carried the ark — as the law required (Num 4:15; 1 Chr 15:2). David had learned this the hard way when Uzzah died touching the ark (1 Chr 13). Now the ark is carried correctly, by the right people, at the right time. The distinction matters: not every reverent intention counts as right approach to the holy. Form and theology go together."
    },
    "5": {
      "L": "And they brought up the ark, and the tent of meeting, and all the holy vessels that were in the tent; the Levitical priests brought them up.",
      "M": "They brought up the ark and the tent of meeting along with all the sacred furnishings inside the tent. The Levitical priests carried them.",
      "T": "The ark and the tent of meeting — together. The two sacred centers of Israel's worship, separated since before David (the tent at Gibeon, the ark in Zion), were finally reunited in the Temple. The entire wilderness inheritance — ark, tent, sacred vessels — was carried in procession to its permanent home. The wandering was over. The tabernacle age was ending; the Temple age was beginning."
    },
    "6": {
      "L": "And King Solomon and all the congregation of Israel who had assembled before him were before the ark, sacrificing sheep and oxen that could not be counted or numbered because of their abundance.",
      "M": "King Solomon and the whole congregation of Israel assembled before the ark were sacrificing sheep and cattle so numerous they could not be counted or tallied.",
      "T": "Uncountable sacrifices — sheep and cattle pouring in from every direction, the smoke rising, the priests overwhelmed with the sheer volume of offering. Abundance beyond accounting. The nation met God with everything it had. Nothing was held back. This was Israel at its best: lavish, joyful, corporate worship at the threshold of a new age."
    },
    "7": {
      "L": "So the priests brought the ark of the covenant of the LORD to its place, in the inner sanctuary of the house, in the Most Holy Place, underneath the wings of the cherubim.",
      "M": "The priests brought the ark of the LORD's covenant to its designated place — the inner sanctuary of the house, the Most Holy Place — and set it beneath the wings of the cherubim.",
      "T": "To its place — the Hebrew implies a destined, appointed location. This is where the ark had been going since Mount Sinai: through the wilderness, through Shiloh, through the capture and return, through David's tent in Zion — always toward this moment, this room, this position beneath the outspread wings of the golden cherubim. The ark had found its home."
    },
    "8": {
      "L": "The cherubim spread out their wings over the place of the ark, so that the cherubim covered the ark and its poles from above.",
      "M": "The cherubim spread their wings over the ark's resting place, sheltering the ark and its carrying poles from above.",
      "T": "Wings spread over the ark — the posture of protection and presence. In Exodus 25, the cherubim on the mercy seat bent toward each other, face to face above the cover. Here in the Temple the cherubim are larger, standing, wings extended over the entire space. The small cherubim of the wilderness mercy seat are surrounded and covered by the great Temple cherubim. The presence has grown. The dwelling has expanded."
    },
    "9": {
      "L": "And the poles were so long that the ends of the poles were seen from the holy place before the inner sanctuary, but they could not be seen from outside. And they are there to this day.",
      "M": "The poles were long enough that their ends could be seen from the holy place just outside the inner sanctuary, though not from further out. They remain there to this day.",
      "T": "The poles of the ark extended out through the doorway of the Most Holy Place into the holy place — just barely visible to the priests ministering at the lampstands and incense altar. Not visible to the people, not hidden in the dark — perceptible only to those who stood nearest. The ark announced its presence to the priests through the slight protrusion of its carrying poles: a reminder that the dwelling was not static, not merely architectural. The ark had been carried; it could be carried again. The poles stayed in place as testimony to that history."
    },
    "10": {
      "L": "There was nothing in the ark except the two tablets that Moses put there at Horeb, where the LORD made a covenant with the people of Israel when they came out of Egypt.",
      "M": "Nothing was in the ark except the two stone tablets Moses had placed there at Horeb, where the LORD made a covenant with Israel when they came out of Egypt.",
      "T": "Nothing but the tablets — the two tablets of the covenant law, placed there by Moses at Sinai. The golden jar of manna and Aaron's rod (Heb 9:4) are noted elsewhere; the Chronicler focuses on the tablets alone. The ark that rests at the center of the Temple contains the covenant that defines Israel's relationship with God. The Temple was not built around a relic or an image but around the written terms of the covenant. The house of worship stands on the word."
    },
    "11": {
      "L": "And when the priests came out of the Holy Place — for all the priests who were present had consecrated themselves without regard to their divisions,",
      "M": "When the priests came out of the Holy Place — all the priests present had consecrated themselves regardless of their assigned divisions —",
      "T": "The priests came out of the Holy Place — and the Chronicler notes a procedural detail: all the priests had consecrated themselves, without the usual rotation of their divisions. On this day, the divisions were set aside. Every priest was holy, every priest was ready, every priest was present. The ordinary rules of rotation gave way to the extraordinary unity of the dedication. One holy people, all together, at the threshold of a new era."
    },
    "12": {
      "L": "and all the Levitical singers — Asaph, Heman, and Jeduthun — and their sons and kinsmen, clothed in fine linen, with cymbals, harps, and lyres, stood east of the altar, and with them a hundred and twenty priests sounding trumpets —",
      "M": "and all the Levitical musicians — Asaph, Heman, and Jeduthun, with their sons and relatives, dressed in fine linen — took their places east of the altar with cymbals, harps, and lyres, accompanied by a hundred and twenty trumpet-playing priests —",
      "T": "Asaph, Heman, Jeduthun — the three great guilds of Levitical music that David had established (1 Chr 6; 25). Sons and kinsmen stretching back through generations of training. Dressed in white linen — the color of holiness, the priests' vestment, now worn by the musicians too. A hundred and twenty priests with trumpets. The scale of the music was proportional to the scale of the moment: not a chamber choir but a national orchestra and choir at full strength."
    },
    "13": {
      "L": "it was the duty of the trumpeters and singers to make themselves heard as one voice, in praise and thanksgiving to the LORD. And when the song was raised with trumpets and cymbals and instruments, in praise to the LORD, 'For he is good, for his steadfast love endures forever,' the house — the house of the LORD — was filled with a cloud,",
      "M": "when the trumpeters and singers joined together as one voice to praise and give thanks to the LORD, and the sound arose — trumpets, cymbals, and instruments — in praise to the LORD: 'For he is good; his steadfast love endures forever,' then the house of the LORD was filled with a cloud,",
      "T": "One voice — not in unison by instruction but in the unity of a single act of praise. The song they sang was the simplest and most ancient refrain of Israel's worship: 'He is good; his steadfast love endures forever.' The same words sung at every sacrifice, at every dedication, on every feast day — the irreducible heart of Israel's praise. And at that moment, when the music and the words and the hundreds of voices became one, the cloud came. The Shekinah, the visible divine glory, filled the house. God had been waiting for this song."
    },
    "14": {
      "L": "so that the priests could not stand to minister because of the cloud, for the glory of the LORD filled the house of God.",
      "M": "The priests could not stand to carry out their duties because the cloud had filled the house, for the glory of the LORD filled the house of God.",
      "T": "They could not stand. When the glory of the LORD filled the Temple, the priests who had just carried the ark, who had just led the sacrifices, who had just played and sung — they fell. Not from failure or judgment but from the overwhelming weight of the divine presence. This is the moment the entire project had been building toward since 1 Chronicles 22 when David first said 'the house must be magnificently great.' The answer came not in architecture but in glory: the LORD took up residence in his house. The building was full."
    }
  },
  "6": {
    "1": {
      "L": "Then Solomon said, 'The LORD has said that he would dwell in thick darkness.'",
      "M": "Then Solomon declared: 'The LORD has said he would dwell in thick darkness.'",
      "T": "Solomon speaks into the cloud-filled silence. His first words after the glory descended are not triumph but theology: the LORD dwells in thick darkness. The Hebrew word is araphel — the same dense darkness that accompanied God at Sinai, the cloud that both revealed and concealed (Exod 20:21; Deut 4:11). God is present in the cloud that blinds the priests. His coming is not luminous clarity but overwhelming obscurity. The Temple has been filled not with light but with darkness that contains the Light."
    },
    "2": {
      "L": "'But I have built for you a house of habitation, an elevated place for you to dwell in forever.'",
      "M": "'But I have built you an exalted house — a place for you to dwell in forever.'",
      "T": "Solomon's response to the divine mystery: I have built you a place to dwell. The word for 'dwell' (shakan) is the root of Shekinah — the divine dwelling-presence. The same word used for the tabernacle (mishkan, the dwelling). Solomon has built a permanent form of the tent, an eternal mishkan. 'Forever' — this is the covenant permanence of the Davidic promise. The Temple is meant to endure as long as the dynasty, as long as the covenant."
    },
    "3": {
      "L": "Then the king turned around and blessed all the assembly of Israel, while all the assembly of Israel stood.",
      "M": "The king then turned and blessed the whole assembly of Israel while they all stood.",
      "T": "Solomon turns from the cloud-filled Temple — from addressing God — and faces the people. He blesses them. The king stands between the divine and the human, the link between the glory that filled the house and the people who have gathered to witness it. His blessing is the bridge. This is the priestly dimension of kingship: not merely to rule but to mediate the blessing of God to the people."
    },
    "4": {
      "L": "And he said, 'Blessed be the LORD, the God of Israel, who with his hands has fulfilled what he promised with his mouth to my father David, saying,'",
      "M": "He said: 'Blessed be the LORD, the God of Israel, who has fulfilled with his hands what he promised with his mouth to my father David, saying:'",
      "T": "Promise and fulfillment — this is the structure of the whole speech. God said something to David; God has now done it with his hands. The word-deed unity of God is Solomon's first and foundational theological declaration. The God who speaks is the God who acts, and the gap between the two is not indeterminate but certain. David heard the promise; Solomon stands in its fulfillment."
    },
    "5": {
      "L": "'Since the day I brought my people out of the land of Egypt, I chose no city from any of the tribes of Israel in which to build a house so that my name might be there, and I chose no man as prince over my people Israel;'",
      "M": "'From the day I brought my people out of Egypt, I chose no city from any tribe of Israel to build a house there for my name, nor did I choose anyone to be prince over my people Israel;'",
      "T": "God speaks through Solomon's prayer: from the Exodus to this day, no city and no king were chosen until now. The entire history of Israel — the judges, the failed kings, the wandering — is reframed as an extended period of unchosen-ness. Jerusalem was not inevitable; David was not the default. The election of city and dynasty was a singular, deliberate, grace-filled act. This is the covenant God chose, in the fullness of his own freedom."
    },
    "6": {
      "L": "'but I have chosen Jerusalem for my name to be there, and I have chosen David to be over my people Israel.'",
      "M": "'but I chose Jerusalem for my name to dwell there, and I chose David to lead my people Israel.'",
      "T": "The two elections side by side: Jerusalem and David. City and king chosen together, inseparable. 'For my name to be there' — the divine name as the form of God's presence, the way the infinite makes itself available to the finite. Not 'for me to live in' but 'for my name to dwell.' The Name is both more and less than God himself: more, because the Name carries all that God is; less, because God himself cannot be contained."
    },
    "7": {
      "L": "'Now it was in the heart of David my father to build a house for the name of the LORD, the God of Israel.'",
      "M": "'It was in the heart of my father David to build a house for the name of the LORD, the God of Israel.'",
      "T": "David's desire — the movement of his heart toward God's house — is honored here even though David was denied permission to build. God sees the intention, not only the deed. 'It was in his heart' is the honorific that God gives to David's thwarted ambition. The desire to build the Temple was itself pleasing to God, even though the building was assigned to another. Intent and action are not the same thing, but God counts both."
    },
    "8": {
      "L": "'But the LORD said to my father David, \"Because it was in your heart to build a house for my name, you did well in having this in your heart.\"'",
      "M": "'But the LORD said to my father David, \"You did well to have it in your heart to build a house for my name.\"'",
      "T": "God affirms the desire before he redirects it: 'You did well.' Not 'but unfortunately' or 'however' — first the affirmation, then the redirection. This is God's characteristic generosity: he honors what is right in a person before he explains what is not for them. David's heart was right; only the assignment was different."
    },
    "9": {
      "L": "'Nevertheless, it is not you who shall build the house, but your son who shall be born of you shall build the house for my name.'",
      "M": "'Nevertheless, you are not the one to build the house. Your son, born from you, is the one who will build it for my name.'",
      "T": "Your son — the pronoun falls with precision. Not you, but your son. The Temple belongs to the next generation, the generation of peace. David was a man of war (1 Chr 22:8); his son would be a man of rest, and God's house is a house of rest. The reallocation from father to son was not a demotion but a differentiation — each generation has its own assignment, and David's assignment (preparing, gathering, planning) was as essential as Solomon's (building)."
    },
    "10": {
      "L": "'The LORD has fulfilled his word that he spoke, for I have risen in the place of David my father and sit on the throne of Israel, as the LORD promised, and have built the house for the name of the LORD, the God of Israel.'",
      "M": "'The LORD has kept the promise he made, for I have succeeded my father David and sit on the throne of Israel, just as the LORD promised, and have built the house for the name of the LORD, the God of Israel.'",
      "T": "Solomon declares the fulfillment in his own person: I have risen, I sit, I have built. Three completed acts, three verbs of accomplishment. The LORD's word has not returned empty (Isa 55:11). What God said to David, God has done through Solomon. The chain of promise-fulfillment that began with Abraham, continued through Moses and David, has reached another link. The Temple stands as evidence that God keeps his word."
    },
    "11": {
      "L": "'And there I have set the ark, in which is the covenant of the LORD that he made with the people of Israel.'",
      "M": "'There I have placed the ark containing the covenant the LORD made with Israel.'",
      "T": "The Temple's identity is grounded in the ark, and the ark's identity is grounded in the covenant. The building is not sacred because of its materials or its beauty but because it houses the covenant — the formal, oath-bound agreement between the LORD and Israel. The covenant gives the Temple its meaning; the Temple gives the covenant its location. Neither is complete without the other."
    },
    "12": {
      "L": "Then Solomon stood before the altar of the LORD in the presence of all the assembly of Israel and spread out his hands.",
      "M": "Solomon stood before the altar of the LORD in front of the whole assembly of Israel and stretched out his hands.",
      "T": "The great prayer begins with a posture: Solomon standing before the altar, arms spread wide, palms upward toward heaven. This was the standard posture of ancient prayer — not kneeling (that comes in v. 13) but standing with hands extended, the body opened toward God. All Israel watching. The king's prayer is a public act, witnessed by the nation; what he asks for belongs to everyone."
    },
    "13": {
      "L": "Solomon had made a bronze platform five cubits long, five cubits wide, and three cubits high, and had set it in the middle of the court. He stood on it, and then he knelt on his knees before all the assembly of Israel and spread out his hands toward heaven.",
      "M": "Solomon had made a bronze platform, five cubits long, five cubits wide, and three cubits high, which he placed in the middle of the outer court. He stood on it, then knelt before the whole assembly and stretched his hands toward heaven.",
      "T": "A bronze platform, three cubits high, at the center of the great court — so all Israel could see the king. Solomon stood on it, elevated before his people, then knelt. The king's knees touched the bronze. He who sat on the throne of Israel prostrated himself before the greater throne. Every Israelite who watched the king kneel learned something about the structure of power in the kingdom: the king is a servant, the LORD is the King. Solomon's knees were his greatest sermon."
    },
    "14": {
      "L": "and said: 'O LORD, God of Israel, there is no God like you, in heaven or on earth, keeping covenant and showing steadfast love to your servants who walk before you with all their heart.'",
      "M": "He prayed: 'LORD, God of Israel, there is no God like you in all heaven or earth — you who keep your covenant and show steadfast love to those who serve you wholeheartedly.'",
      "T": "The prayer opens with incomparability: there is no God like you. Not a comparative judgment among equals — there are no equals. The heavens and the earth together contain no rival. Then the content of God's uniqueness: he keeps covenant and shows chesed to those who walk before him. God's incomparability is not power or size but faithfulness. No other god keeps his promises. No other god maintains covenant loyalty across generations, across failures, across the whole arc of a people's history. This is the LORD."
    },
    "15": {
      "L": "'You have kept with your servant David my father what you promised him; what you spoke with your mouth you have fulfilled with your hand, as on this day.'",
      "M": "'You have kept your promise to your servant, my father David. You said it with your mouth, and this day you have fulfilled it with your hand.'",
      "T": "Mouth and hand — the two organs of promise and fulfillment. God spoke and God acted, and they are the same. 'As on this day' — this day is the evidence. Solomon stands in the fulfillment of a promise made to his father, in a Temple built on covenant ground, with an ark carrying covenant law, and he says: today proves that God keeps his word. The dedication of the Temple is an epistemological event: here is evidence that God is faithful."
    },
    "16": {
      "L": "'Now therefore, O LORD, God of Israel, keep for your servant David my father what you have promised him, saying, \"You shall not lack a man to sit before me on the throne of Israel, if only your sons take heed to their way, to walk in my law as you have walked before me.\"'",
      "M": "'Now, LORD, God of Israel, keep the promise you made to your servant, my father David: \"You will always have a descendant on the throne of Israel if your sons are careful to obey my law, just as you have obeyed me.\"'",
      "T": "The promise is quoted — but so is its condition. 'If only your sons take heed.' The Davidic covenant in Chronicles is not unconditional; obedience is the path of its continuation. This is the honest prayer of a king who knows what is at stake: the dynasty's future depends on the dynasty's faithfulness. Solomon prays not for the promise to be unconditional but for the grace to meet its condition. He has heard the word 'if' and he does not flinch from it."
    },
    "17": {
      "L": "'Now therefore, O LORD, God of Israel, let your word that you spoke to your servant David be confirmed.'",
      "M": "'And now, LORD, God of Israel, let the promise you made to your servant David stand firm.'",
      "T": "A short verse that carries the weight of the whole prayer: let your word be confirmed. Solomon does not ask for new things; he asks that the old word hold. The covenant God made to David — let it stand. The promises God spoke at Gibeon, at Sinai, to Abraham — let them be fulfilled. The prayer is fundamentally a prayer for God to be himself, to do what he said he would do."
    },
    "18": {
      "L": "'But will God indeed dwell with man on the earth? Behold, heaven, even the highest heaven, cannot contain you, how much less this house that I have built!'",
      "M": "'But will God truly dwell with human beings on the earth? Even the highest heavens cannot contain you — how much less this house I have built!'",
      "T": "The central theological question of the entire Temple project: can God dwell with humans? Solomon asks it not as doubt but as wonder — the wonder that he does, given that he cannot be contained. Heaven and the highest heaven are too small. The cosmos is too narrow. And yet — the cloud has just filled this house. God who cannot be contained has chosen to be present. The Temple is not a contradiction of God's transcendence but a miracle of his condescension. He who fills the universe stoops to fill a room."
    },
    "19": {
      "L": "'Yet have regard for the prayer of your servant and his plea, O LORD my God, listening to the cry and the prayer that your servant prays before you,'",
      "M": "'Yet give attention to your servant's prayer and his plea for mercy, LORD my God. Hear the cry and the prayer your servant offers before you.'",
      "T": "From the cosmic to the personal: Solomon the king, before the whole nation, calls himself 'your servant' — twice in one verse. The one who built a house for God approaches God as a servant, not as an equal. The cry and the prayer — two words for petition, the spontaneous cry of need and the structured prayer of address. Both are welcomed. God attends to both."
    },
    "20": {
      "L": "'That your eyes may be open day and night toward this house, toward the place where you have promised to set your name, that you may listen to the prayer that your servant prays toward this place.'",
      "M": "'May your eyes remain open toward this house day and night — toward the place where you promised to put your name — so that you will hear the prayer your servant offers toward this place.'",
      "T": "Eyes open day and night toward this place. Solomon asks for God's continual, attentive, wakeful regard — directed not toward Solomon himself but toward the place. The Name-theology does its work here: because God's name has been placed in the Temple, prayers directed toward the Temple reach God. It is not the building that hears but God, who has attached his name to the building as the address by which he can be found."
    },
    "21": {
      "L": "'And listen to the pleas of your servant and of your people Israel, when they pray toward this place. And from your dwelling place in heaven, hear and forgive.'",
      "M": "'Hear the pleas of your servant and your people Israel when they pray toward this place. From your heavenly dwelling place, hear and forgive.'",
      "T": "The prayer's structure is established: prayers are directed toward the Temple on earth; God hears from his dwelling place in heaven. The Temple is not God's residence but his address. Heaven is where he lives; the Temple is where he can be reached. This distinction — heard on earth, answered from heaven — runs through every intercession that follows (vv. 22-39). Solomon understands the Temple's purpose with precision: a focus for prayer, not a cage for God."
    },
    "22": {
      "L": "'If a man sins against his neighbor and is made to take an oath and comes and swears his oath before your altar in this house,'",
      "M": "'When someone sins against a neighbor and is required to take an oath, and comes and swears before your altar in this house,'",
      "T": "The first of seven intercession scenarios. A dispute between neighbors, an oath sworn at the altar. The Temple was not only for feast-day worship but for the daily business of justice — a place where oaths carried the weight of God's name, where disputes between individuals could be settled under divine witness. The house of prayer was also a hall of justice."
    },
    "23": {
      "L": "'then hear from heaven and act and judge your servants, repaying the guilty by bringing his conduct on his own head, and vindicating the righteous by rewarding him according to his righteousness.'",
      "M": "'then hear from heaven and act — judge your servants by condemning the guilty and bringing what they did on their own head, and by vindicating the innocent according to their innocence.'",
      "T": "God is the judge who sees what the human court cannot: the heart. He brings the guilty man's conduct back on his own head — not arbitrary punishment but perfect accountability. And he vindicates the righteous — gives back to the innocent man the standing that was taken from him. This is divine justice: not just punishment of the wicked but restoration of the wronged. Solomon asks God to be what no human court can fully be."
    },
    "24": {
      "L": "'If your people Israel are defeated before the enemy because they have sinned against you, and they turn again and acknowledge your name and pray and plead before you in this house,'",
      "M": "'When your people Israel are defeated by an enemy because they sinned against you, and they turn back and acknowledge your name, praying and pleading before you in this house,'",
      "T": "The second scenario: military defeat. Not 'if' in the abstract — the Chronicler's audience knew this had happened, would happen again. Defeat was not the end of the story; it was the occasion for return. The three verbs of restoration are paired: turn and acknowledge. The turning is bodily — they come back to the Temple. The acknowledgment is theological — they confess the name. Both together constitute genuine repentance."
    },
    "25": {
      "L": "'then hear from heaven and forgive the sin of your people Israel and bring them back to the land that you gave to them and to their fathers.'",
      "M": "'then hear from heaven, forgive the sin of your people Israel, and bring them back to the land you gave them and their ancestors.'",
      "T": "The petition for defeated Israel: forgive and restore. Forgiveness is not the final gift — restoration to the land is. The sin that caused the defeat is removed; the people are brought home. This is the full arc of covenant restoration: the broken relationship is healed, and the covenant blessings — land, presence, security — are returned. Solomon is praying for something that will not happen in his lifetime; he is praying for every generation of Israel that will come after him."
    },
    "26": {
      "L": "'When heaven is shut up and there is no rain because they have sinned against you, and they pray toward this place and acknowledge your name and turn from their sin, when you afflict them,'",
      "M": "'When heaven is shut and there is no rain because they sinned against you, and they pray toward this place, acknowledge your name, and turn from their sin when you afflict them,'",
      "T": "Third scenario: drought. In an agricultural society, drought was divine judgment made visible in the landscape. No rain meant no harvest meant death. When the sky was closed, Solomon prays, let the Temple remain open — a channel that drought cannot shut. The closed heavens and the open house of prayer are the two poles of the scenario: drought closes the sky; repentance at the Temple reopens it."
    },
    "27": {
      "L": "'then hear in heaven and forgive the sin of your servants, your people Israel, when you teach them the good way in which they should walk, and send rain on your land that you have given to your people as an inheritance.'",
      "M": "'then hear in heaven, forgive the sin of your servants your people Israel, teach them the right way to walk, and send rain on your land that you gave your people as an inheritance.'",
      "T": "Hear, forgive, teach, send rain. Four gifts in response to repentance. God's forgiveness comes with instruction — 'teach them the good way in which they should walk.' The drought was not arbitrary; it was an occasion for learning. When the rain comes back, it comes back to people who have been taught. The blessing returns to those who know how to receive and hold it."
    },
    "28": {
      "L": "'If there is famine in the land, if there is pestilence, blight, mildew, locust, or caterpillar; if their enemies besiege them in the land at their gates; whatever plague or disease there is;'",
      "M": "'If there is famine in the land, or plague, or blight or mildew, locusts or grasshoppers; if enemies besiege them in their own towns; whatever disaster or disease there is —'",
      "T": "The fourth scenario expands into a list: famine, plague, crop disease, infestation, siege. Solomon is cataloging the complete range of ancient calamity — every threat to life that Israel might face. By listing them all, the prayer ensures that no suffering falls outside the Temple's reach. Whatever the disaster, this prayer covers it. No one who suffers need think their affliction too ordinary or too strange for God's attention."
    },
    "29": {
      "L": "'whatever prayer or plea is made by any man or by all your people Israel, each knowing his own affliction and pain, spreading out his hands toward this house —'",
      "M": "'whatever prayer or plea any person makes — each knowing their own pain and grief — when they spread their hands toward this house —'",
      "T": "Each person knowing his own affliction. Not generic suffering but the specific, personal knowledge of one's own wound — the grief that belongs to a single person who carries it alone. Solomon's prayer sees the individual inside the catastrophe. The hand spread toward the Temple is not just Israel's hand but this person's hand, this pain, this need. God is asked to see what no one else can fully see: the inner knowledge of one's own hurt."
    },
    "30": {
      "L": "'then hear from heaven, your dwelling place, and forgive and render to each according to all his ways, for you, you alone, know the hearts of the children of man,'",
      "M": "'then hear from heaven, your dwelling place, forgive, and deal with everyone according to what they do — for you alone know the human heart —'",
      "T": "You alone know the human heart. This is the foundation of Solomon's entire prayer system: God can hear and judge rightly because he sees what no human tribunal can reach — the interior of the person. Every scenario in this prayer depends on this: God distinguishes between genuine repentance and performance, between the truly wronged and the merely plausible claimant, between the sincere prayer and the manipulative one. Only God knows the hearts. Only God can answer these prayers with justice."
    },
    "31": {
      "L": "'that they may fear you and walk in your ways all the days that they live in the land that you gave to our fathers.'",
      "M": "'so that they may respect you and walk in your ways throughout their lives in the land you gave our ancestors.'",
      "T": "The purpose behind every answer to prayer: not merely that Israel will be safe or fed or victorious, but that they will fear the LORD and walk in his ways. Every act of divine hearing serves this end. The rain, the forgiveness, the defeat of enemies — all of it aimed at producing a people who walk with God through all the days of their lives in the land of the covenant. God's gifts serve God's purpose: a holy people in a holy land."
    },
    "32": {
      "L": "'Likewise, when a foreigner, who is not of your people Israel, comes from a far country for the sake of your great name and your mighty hand and your outstretched arm, when he comes and prays toward this house,'",
      "M": "'And also for the foreigner who is not part of your people Israel — when they come from a distant land because of your great name and your mighty outstretched arm — when they come and pray toward this house,'",
      "T": "The fifth scenario breaks the expected pattern: the foreigner. Not an Israelite in distress but a person from far away, drawn by the fame of the LORD's name — the great name, the mighty arm, the outstretched power. This person comes to pray at the Temple without covenant claim or tribal membership. Solomon asks God to hear him too. The Temple of the God who is incomparable to all gods (v. 14) is open to those who have heard of his incomparability from wherever they stand."
    },
    "33": {
      "L": "'hear from heaven, your dwelling place, and do according to all that the foreigner calls to you for, in order that all the peoples of the earth may know your name and fear you, as do your people Israel, and that they may know that this house I have built is called by your name.'",
      "M": "'hear from heaven your dwelling place and grant all that the foreigner asks — so that all peoples of the earth may know your name and fear you, as your own people Israel do, and may know that this house I built bears your name.'",
      "T": "The reason God should hear the foreigner: all the peoples of the earth. Solomon's horizon is universal. The Temple was not built for Israel alone but as a witness-point to every nation. When God answers the foreign worshiper's prayer, the world learns that the LORD is real, that his name has power, that this house stands under his authority. The Temple's walls are narrowly Israelite; its reach is meant to be the whole earth. Isaiah would later call it 'a house of prayer for all peoples' (Isa 56:7). Solomon prays that vision before Isaiah speaks it."
    },
    "34": {
      "L": "'If your people go out to battle against their enemies, by whatever way you send them, and they pray to you toward this city that you have chosen and the house that I have built for your name,'",
      "M": "'When your people go to war against their enemies — wherever you send them — and they pray to you toward this city you have chosen and this house built for your name,'",
      "T": "Sixth scenario: war. The direction of prayer is toward the city and the house — the earthly address of the divine name. Even in foreign lands, at the edge of battle, Israel could orient its prayer toward Jerusalem. The Temple was not only for worshipers who stood inside it but for every Israelite, anywhere, who needed to pray. The house of the Name was a directional anchor for the entire diaspora of hope."
    },
    "35": {
      "L": "'then hear from heaven their prayer and their plea, and maintain their cause.'",
      "M": "'then hear from heaven their prayer and plea, and uphold their cause.'",
      "T": "Maintain their cause — advocate for them, take their side in the cosmic court. God is asked to be not merely the hearer but the advocate: to hear the prayer and then act as the champion of those who prayed it. This is covenant solidarity: Israel's cause becomes God's cause, because Israel is God's people."
    },
    "36": {
      "L": "'If they sin against you — for there is no one who does not sin — and you are angry with them and deliver them to an enemy, so that they are carried away captive to a land far or near,'",
      "M": "'When they sin against you — for there is no one who never sins — and you are angry with them and hand them over to an enemy who takes them captive to a distant or nearby land,'",
      "T": "The seventh and final scenario is also the deepest: exile. Not just military defeat but removal from the land — captivity in a foreign country, far or near. Solomon frames this with a parenthetical that carries its own weight: 'for there is no one who does not sin.' This is not pessimism but realism. The covenant includes the anticipation of failure. God's provision for sin is not surprise that sin happens but a structured path back. The Temple exists precisely because humans fail and need a way home."
    },
    "37": {
      "L": "'yet if they turn their heart in the land to which they have been carried captive, and repent and plead with you in the land of their captors, saying, \"We have sinned and done wrong and acted wickedly\",'",
      "M": "'and if in the land of their captors they have a change of heart and repent, pleading with you: \"We have sinned; we have done wrong and acted wickedly\" —'",
      "T": "Three words for failure: sinned, done wrong, acted wickedly. The prayer of exile names the sin in full — no euphemism, no minimizing. This is the pattern of genuine repentance: name it clearly, claim it honestly, own the full weight of it. The exiles in a foreign land with no Temple in sight, no altar, no priest — they pray with nothing but these words and the memory of Solomon's prayer, and God is asked to hear them."
    },
    "38": {
      "L": "'if they repent with all their heart and with all their soul in the land of their captivity to which they were carried captive, and pray toward their land, which you gave to their fathers, and the city that you have chosen, and the house that I have built for your name,'",
      "M": "'if they repent with all their heart and soul in the land of their captivity, and pray toward their own land that you gave their ancestors, this city you chose, and this house I built for your name —'",
      "T": "Heart and soul — the whole embodied self, from center to edge. The exile's prayer is directed toward the land, the city, the house. Three nested circles of orientation: the land of the covenant, the city of David, the house of the Name. From wherever the exile stands, the prayer is aimed at Jerusalem — not because Jerusalem contains God but because God has put his name there and made it the address of covenant relationship."
    },
    "39": {
      "L": "'then hear from heaven your dwelling place their prayer and their pleas, and maintain their cause and forgive your people who have sinned against you.'",
      "M": "'then hear from your heavenly dwelling place their prayer and their pleas, uphold their cause, and forgive your people who sinned against you.'",
      "T": "The final petition for the exiles: hear, uphold, forgive. Not restore to the land — that will come; this prayer rests in the act of forgiveness itself. God hearing from heaven the prayer aimed toward Jerusalem from wherever in the world an exile stands. This is the prayer that sustained Israel in Babylon, in Persia, in Rome, in every diaspora. Solomon prayed it before any exile happened. The prayer was ready before the need arrived."
    },
    "40": {
      "L": "'Now, O my God, let your eyes be open and your ears attentive to the prayer of this place.'",
      "M": "'Now, my God, may your eyes be open and your ears attentive to the prayers offered at this place.'",
      "T": "The prayer turns intimate: 'my God' — not 'God of Israel' or 'LORD God' but 'my God.' Solomon has prayed for every scenario of national and personal need; now he speaks person to person. The request is simple: look at this place, listen to these prayers. Open eyes and attentive ears — the posture of a parent listening to a child. Solomon asks for nothing more than God's full attention. That, it turns out, is everything."
    },
    "41": {
      "L": "'And now arise, O LORD God, and go to your resting place, you and the ark of your might. Let your priests, O LORD God, be clothed with salvation, and let your saints rejoice in your goodness.'",
      "M": "'Now arise, LORD God, and come to your resting place — you and the ark of your power. May your priests, LORD God, be clothed with salvation, and may your faithful people rejoice in your goodness.'",
      "T": "The closing words are a quotation: Psalm 132:8-10, the psalm of the ark's procession. Solomon closes his great dedicatory prayer by singing Scripture. 'Arise, O LORD, and go to your resting place' — the same words that summoned the ark on its journey to the Temple. Now Solomon uses them as the doxological close: the prayer ends where the ark's procession ended, in the rest of God's chosen dwelling place. Priests clothed with salvation; the faithful rejoicing in goodness. This is the vision of what the Temple should produce: saved priests and joyful worshipers. Not an institution but a people transformed by God's presence."
    },
    "42": {
      "L": "'O LORD God, do not turn away the face of your anointed one. Remember your steadfast love for David your servant.'",
      "M": "'LORD God, do not reject your anointed one. Remember your steadfast love for your servant David.'",
      "T": "The prayer ends with David's name. 'Do not reject your anointed one' — the anointed is both Solomon in the present and every Davidic king to come, stretching forward in covenant hope. The final appeal is not to Solomon's merit but to David's covenant, and beyond it to the chesed — the covenant loyalty — that has been the subject of this whole prayer. God's steadfast love for David is the final ground on which the king stands. Not his own building, not his own wisdom, not his own prayer — but the lovingkindness that God swore to a shepherd from Bethlehem."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '2chronicles')
        merge_tier(existing, CHRONICLES2, tier_key)
        save(tier_dir, '2chronicles', existing)
    print('2 Chronicles 1–6 written.')

if __name__ == '__main__':
    main()
