#!/usr/bin/env python3
import json, os

OUT_DIR = '../data/biblepedia/articles'
os.makedirs(OUT_DIR, exist_ok=True)

def merge_article(slug, data):
    path = os.path.join(OUT_DIR, f'{slug}.json')
    if os.path.exists(path):
        return False
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
    return True

ARTICLES = {
"scripture": {
  "id": "scripture",
  "term": "Scripture",
  "category": "concepts",
  "intro": "<p>Scripture, as the term is used invariably in the New Testament, denotes the definite collection of sacred books regarded as given by inspiration of God — what Christians call the Old Testament. The Greek word <em>graphe</em> (writing) carries the force of authority: Paul tells Timothy that \"all Scripture is God-breathed and profitable for doctrine\" (2 Tim. 3:16), and Jesus himself appeals repeatedly to \"the Scriptures\" as the decisive word of God. The NT also begins to apply the term to its own emerging writings, as Peter places Paul's letters alongside \"the other Scriptures\" (2 Pet. 3:16).</p><p>The phrase \"the Scripture cannot be broken\" (John 10:35) reflects the high view of inspiration held in the apostolic church. The New Testament draws a sharp line between Scripture — the fixed, authoritative text — and oral tradition or human interpretation. The canon of Hebrew writings recognized as Scripture in the first century formed the basis for the Old Testament received by the Christian church.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["2 Timothy 3:15", "2 Timothy 3:16", "John 20:9", "Galatians 3:22", "2 Peter 1:20"]
},
"scythian": {
  "id": "scythian",
  "term": "Scythian",
  "category": "people",
  "intro": "<p>The Scythians were a vast confederation of pastoral nomadic tribes who inhabited the steppes north of the Black Sea and the Caspian, ranging far to the east across central Asia. In the Table of Nations they are associated with descendants of Japheth. Greek and Roman writers describe them as formidable warriors; their sudden raids into the Fertile Crescent were a source of dread in the ancient Near East, and the prophet Jeremiah may allude to Scythian incursions in his visions of a foe from the north.</p><p>In the New Testament, \"Scythian\" is used by Paul as shorthand for the most barbarous of peoples: in Christ \"there is neither Greek nor Jew… barbarian, Scythian, slave nor free\" (Col. 3:11). This inclusion of the Scythian — the archetype of the uncivilized outsider — underscores the universal reach of the gospel across every cultural boundary.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Genesis 9:27", "Colossians 3:11"]
},
"sea-of-glass": {
  "id": "sea-of-glass",
  "term": "Sea of glass",
  "category": "concepts",
  "intro": "<p>The sea of glass is a figurative expression appearing twice in the Book of Revelation. In Revelation 4:6 it is described as \"like crystal\" before the throne of God, and in Revelation 15:2 as \"mingled with fire,\" on which the victorious stand holding harps. Interpreters understand it variously as a symbol of the vast, untroubled wisdom of God, of the purity and transcendence of the divine presence, or — by analogy with the molten sea of the temple — of the means of cleansing before worship.</p><p>The image draws on the ancient Near Eastern association of the cosmic sea with primordial chaos, which in the heavenly vision is rendered calm, transparent, and fiery rather than threatening. The redeemed standing upon it signals final victory over the forces that once seemed overwhelming from below.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Revelation 4:6", "Revelation 15:2", "Psalms 36:6", "Romans 11:33"]
},
"sea-of-jazer": {
  "id": "sea-of-jazer",
  "term": "Sea of Jazer",
  "category": "places",
  "intro": "<p>The sea of Jazer is mentioned in Jeremiah's lamentation over Moab (Jer. 48:32) as the body of water associated with the Ammonite city of Jazer, east of the Jordan. It is not a major sea but rather the lake or series of ponds formed in the high valley where Jazer stood, whose ruins are identified with the site called Sar in the Transjordan highlands. Jazer itself was a significant Ammonite city and later an Israelite possession, and its vineyards and fields were celebrated for their productivity.</p><p>The prophet's weeping \"with the weeping of Jazer\" over Moab uses this body of water as a poetic image of abundance now turned to desolation — the waters that once nourished productive land becoming a symbol of grief and ruin.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Jeremiah 48:32"]
},
"sea-the": {
  "id": "sea-the",
  "term": "Sea, The",
  "category": "concepts",
  "intro": "<p>The Hebrew word <em>yam</em>, translated \"sea\" throughout the Old Testament, carries several distinct meanings in Scripture. It signifies (1) the ocean as the great gathering of waters at creation (Gen. 1:10); (2) large rivers such as the Nile (Isa. 19:5) and the Euphrates (Isa. 21:1; Jer. 51:36); (3) the Red Sea, the site of Israel's deliverance from Egypt; (4) the Mediterranean (\"the great sea\" or \"the hinder sea\"); and (5) the Dead Sea (\"the salt sea\" or \"the eastern sea\").</p><p>In biblical symbolism the sea often represents chaos, danger, or the unknown realm beyond human control — a force that only God commands (Ps. 65:7; 89:9). The prophetic and apocalyptic literature transforms this image: Isaiah promises that the sea will be dried up at the final redemption, and Revelation declares that in the new creation \"there was no more sea\" (Rev. 21:1), signifying the end of all that opposes God.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Genesis 1:10", "Isaiah 19:5", "Exodus 14:16", "Revelation 21:1"]
},
"sea-the-molten": {
  "id": "sea-the-molten",
  "term": "Sea, The molten",
  "category": "concepts",
  "intro": "<p>The molten sea was the great bronze laver constructed by Solomon for the Jerusalem temple, described in 1 Kings 7:23–26 and 2 Chronicles 4:2–5. It stood in the south-eastern corner of the inner court, measuring ten cubits in diameter and five in height, and rested upon twelve bronze oxen arranged in groups of three facing the four points of the compass. It held approximately two thousand baths of water and served for the ritual washing of the priests.</p><p>The twelve oxen supporting the laver likely symbolized the twelve tribes of Israel bearing the means of purification. The Chronicler notes that its metal came from the spoils David had taken from Hadarezer (1 Chr. 18:8). King Ahaz later removed the bronze oxen and placed the sea on a stone pavement (2 Kings 16:17), and it was broken up and carried to Babylon at the fall of Jerusalem.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["1 Kings 7:23", "2 Chronicles 4:2", "1 Chronicles 18:8", "2 Kings 16:17"]
},
"seah": {
  "id": "seah",
  "term": "Seah",
  "category": "concepts",
  "intro": "<p>The seah was a Hebrew unit of measurement used for both area and capacity. As a land measure it denoted a space of approximately 50 cubits by 50 cubits — the area a seah of grain could sow. As a capacity measure a seah equaled roughly one peck (just over two gallons), being one-third of an ephah. The term appears in narrative and legal texts when grain, flour, or other dry goods are measured out.</p><p>The seah is notable in the Elisha narrative where the prophet promises a seah of fine flour for a shekel in a time of severe famine (2 Kings 7:1, 16, 18), a pledge met the following day when the Aramean siege of Samaria was mysteriously broken. The measure thus becomes a unit of miraculous provision in the biblical account.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["2 Kings 7:1", "2 Kings 7:16"]
},
"seal": {
  "id": "seal",
  "term": "Seal",
  "category": "concepts",
  "intro": "<p>A seal in the biblical world was commonly a signet ring or cylinder carved with a personal device that, when pressed into clay or wax, authenticated the owner's authority on letters, documents, and jars. The patriarchal narratives, royal correspondence, and legal texts all attest its use: Judah carried a seal as a personal pledge (Gen. 38:18), Jezebel sealed royal letters with Ahab's ring (1 Kings 21:8), and Nehemiah and the leading families sealed the covenant renewal (Neh. 9:38).</p><p>In biblical theology the seal carries rich symbolic weight. God's covenant promises are described as sealed and certain (Deut. 32:34); in the New Testament the Holy Spirit given to believers is called the seal of their redemption and the guarantee of the inheritance (Eph. 1:13–14). The sealed scroll of Revelation whose seven seals Christ alone is worthy to open (Rev. 5–8) represents the culmination of history under divine authority.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Genesis 38:18", "1 Kings 21:8", "Nehemiah 9:38", "Ephesians 1:13"]
},
"seasons": {
  "id": "seasons",
  "term": "Seasons",
  "category": "concepts",
  "intro": "<p>The agricultural seasons of the biblical world shaped both the economy and the liturgical calendar of ancient Israel. The year divided broadly into two seasons — the wet (winter) season and the dry (summer) season — with sowing and harvest punctuating the cycle (Gen. 8:22). Spring brought the barley harvest (Passover season), followed by wheat harvest at Pentecost; the dry summer ripened grapes, figs, and olives; autumn plowing and the early rains began the new agricultural year.</p><p>Israel's three great pilgrimage feasts were tied directly to this agrarian rhythm: Passover and Unleavened Bread at barley harvest, Weeks (Pentecost) at wheat harvest, and Tabernacles at the fruit harvest and autumn thanksgiving. The regular return of the seasons was itself a sign of God's faithfulness and covenant steadfastness, reaffirmed after the flood (Gen. 8:22).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Genesis 8:22"]
},
"seba": {
  "id": "seba",
  "term": "Seba",
  "category": "places",
  "intro": "<p>Seba appears in the Table of Nations as one of the sons of Cush (Gen. 10:7), and also as a country and nation mentioned alongside Egypt and Ethiopia in the prophetic literature, placing it in north-eastern Africa. Isaiah records God's declaration that Egypt, Ethiopia, and Seba would be given as a ransom for Israel (Isa. 43:3; 45:14), indicating that Seba was a substantial African power whose resources were considerable.</p><p>The Psalmist's vision of universal tribute to the messianic king includes the kings of Sheba and Seba bringing gifts (Ps. 72:10), linking Seba to the wider theme of the nations acknowledging Israel's God. Ancient sources variously identify Seba with the region of Meroe in upper Nubia, south of Egypt along the Nile.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Genesis 10:7", "Isaiah 43:3", "Isaiah 45:14", "Psalms 72:10"]
},
"sebat": {
  "id": "sebat",
  "term": "Sebat",
  "category": "concepts",
  "intro": "<p>Sebat (also spelled Shebat) is the eleventh month of the Hebrew sacred calendar and the fifth of the civil year, running approximately from the new moon of February to that of March. The Assyrian cognate <em>sabatu</em> carries the sense of \"storm,\" reflecting the weather that characterized this winter month in the ancient Near East. Sebat is mentioned by name in the prophetic vision of Zechariah dated to the twenty-fourth day of Sebat (Zech. 1:7), which was the second year of Darius I (520–519 B.C.).</p><p>In the modern Jewish calendar it is spelled Shevat and is associated with Tu BiShvat, a traditional festival marking the new year for trees. The month falls during the latter rains in the land of Israel.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Zechariah 1:7"]
},
"secacah": {
  "id": "secacah",
  "term": "Secacah",
  "category": "places",
  "intro": "<p>Secacah (meaning: <em>enclosure</em>) was one of six cities listed in the wilderness district of Judah (Josh. 15:61), notable for its \"great cistern.\" The city lay in the arid region east of Bethany toward the Dead Sea, and its large water-storage system was essential for settlement in that desert landscape. Secacah has been tentatively identified with the ruin Sikkeh in the Judean wilderness, though the identification is not certain.</p><p>The wilderness cities of Judah listed in Joshua 15 represent early Israelite settlements in a challenging environment. Secacah's cistern system reflects the ingenuity required to sustain habitation in an area receiving minimal rainfall, a feature that made it distinctive enough for mention in the tribal allotment records.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Joshua 15:61"]
},
"sechu": {
  "id": "sechu",
  "term": "Sechu",
  "category": "places",
  "intro": "<p>Sechu (meaning: <em>a hill</em> or <em>watch-tower</em>) was a place between Gibeah and Ramah in the territory of Benjamin, known for its \"great well\" (1 Sam. 19:22). It marks the stopping point of those searching for David and Samuel: when men came to Sechu and asked where Samuel and David were, they were directed to Naioth in Ramah. The site has been tentatively identified with modern Suweikeh, south of Beeroth.</p><p>Sechu's mention in the narrative of Saul's pursuit of David places it within the Benjaminite highlands north of Jerusalem, in an area where the prophet Samuel maintained prophetic communities. The presence of a prominent well at Sechu suggests it was a recognized landmark and gathering place in the region.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["1 Samuel 19:22"]
},
"sect": {
  "id": "sect",
  "term": "Sect",
  "category": "concepts",
  "intro": "<p>The Greek word <em>hairesis</em> (from which English derives \"heresy\") originally meant simply \"a choice\" or \"chosen manner of life,\" and in the New Testament it first denotes a religious party or school: the sect of the Sadducees (Acts 5:17), the sect of the Pharisees (Acts 15:5), and Christianity itself, which opponents called \"the sect of the Nazarenes\" (Acts 24:5). Paul, defending himself before Felix, refuses to concede that his faith is a mere sect, insisting it is the fulfillment of all that the law and prophets promised (Acts 24:14).</p><p>Over time <em>hairesis</em> acquired its pejorative sense of a divisive party that departs from recognized truth. Paul lists it among the works of the flesh (Gal. 5:20), and Peter warns against teachers who will introduce \"destructive heresies\" (2 Pet. 2:1). The shift reflects the growing awareness in the apostolic church that not all who claimed Christian identity held the faith delivered to the saints.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Acts 24:14", "Acts 5:17", "Galatians 5:20", "2 Peter 2:1"]
},
"secundus": {
  "id": "secundus",
  "term": "Secundus",
  "category": "people",
  "intro": "<p>Secundus (meaning: <em>second</em> in Latin) was a Christian from Thessalonica who accompanied Paul on his journey through Macedonia and Asia at the conclusion of the third missionary journey (Acts 20:4). He is named alongside Aristarchus, also a Thessalonian, among the group of delegates from the various Gentile churches who accompanied Paul, likely carrying the collection for the saints in Jerusalem.</p><p>Beyond his mention in Acts 20:4, nothing further is known of Secundus. His Latin name suggests he may have been a freedman or of Roman background, though Thessalonica's cosmopolitan character made Latin names common regardless of origin.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Acts 20:4"]
},
"seer": {
  "id": "seer",
  "term": "Seer",
  "category": "concepts",
  "intro": "<p>The title <em>seer</em> (Hebrew: <em>ro'eh</em> or <em>hozeh</em>) was an early designation for the prophet in Israel, emphasizing the visionary dimension of the prophetic gift. The antiquity of the title is confirmed by the parenthetical note in 1 Samuel 9:9: \"He that is now called a Prophet was beforetime called a Seer.\" Samuel himself is described as a seer, and kings employed court seers alongside other prophets: Gad served David as \"the king's seer\" (2 Sam. 24:11), and Heman was the king's seer in matters of music (1 Chr. 25:5).</p><p>The two Hebrew words used for seer overlap in meaning but may reflect different modes of revelation — <em>ro'eh</em> emphasizing visual perception and <em>hozeh</em> emphasizing the receiving of visions. Both gave way to the more common later term <em>nabi</em> (prophet), though all three appear in the Hebrew canon and are treated as functionally equivalent in describing those who received and communicated the divine word.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["1 Samuel 9:9", "2 Samuel 24:11", "1 Chronicles 9:22", "1 Chronicles 25:5"]
},
"seethe": {
  "id": "seethe",
  "term": "Seethe",
  "category": "concepts",
  "intro": "<p>The verb <em>seethe</em> in the Authorized Version means simply \"to boil,\" translating Hebrew <em>bashal</em>. The instruction in Exodus 16:23 — \"bake that which ye will bake today, and seethe that ye will seethe\" — refers to the preparation of manna on the day before the Sabbath. The same verb underlies the repeated prohibition \"thou shalt not seethe a kid in its mother's milk\" (Ex. 23:19; 34:26; Deut. 14:21), which became the basis for later Jewish laws governing the separation of meat and dairy.</p><p>The term also appears in the preparation of the Passover lamb and in ritual instructions for the Levitical offerings, reflecting the practical significance of boiling as a method of cooking in ancient Israelite household and cultic life.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Exodus 16:23", "Exodus 23:19"]
},
"seething-pot": {
  "id": "seething-pot",
  "term": "Seething pot",
  "category": "concepts",
  "intro": "<p>The seething pot (a vessel for boiling provisions) appears in two significant biblical passages. In Job 41:20 the boiling breath of Leviathan is compared to a seething pot or cauldron, using the image of furious, irresistible heat as a metaphor for the monster's power. More theologically significant is Jeremiah 1:13, where the prophet's second vision is \"a seething pot; and the face thereof is toward the north\" — the boiling contents about to spill southward symbolize the Babylonian invasion that God is bringing upon Judah.</p><p>Cooking vessels of this kind were common household items in the ancient Near East, typically clay or bronze cauldrons suspended over fire. Their use in prophetic vision transforms a mundane domestic object into an emblem of divine judgment, a pattern also found in Ezekiel's allegory of the cooking pot (Ezek. 24:3–14).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Jeremiah 1:13", "Job 41:20", "Ezekiel 24:3"]
},
"segub": {
  "id": "segub",
  "term": "Segub",
  "category": "people",
  "intro": "<p>Segub (meaning: <em>elevated</em> or <em>exalted</em>) is the name of two distinct persons in the Old Testament. (1) The youngest son of Hiel the Bethelite, who lost his life when Hiel rebuilt Jericho in the days of Ahab — fulfilling the curse Joshua had pronounced that the builder would lay its foundation at the cost of his firstborn and set up its gates at the cost of his youngest (1 Kings 16:34; cf. Josh. 6:26). (2) A descendant of Judah through Hezron and a daughter of Machir the Manassite, who fathered Jair and held twenty-three cities in Gilead (1 Chr. 2:21–22).</p><p>The first Segub's death is a sobering illustration of the long reach of a prophetic word, fulfilled centuries after Joshua's curse was first uttered.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["1 Kings 16:34", "Joshua 6:26", "1 Chronicles 2:21"]
},
"seir": {
  "id": "seir",
  "term": "Seir",
  "category": "places",
  "intro": "<p>Seir (meaning: <em>rough</em> or <em>hairy</em>) designates both a Horite chieftain and the mountainous region that bears his name. As a geographical term it refers to the rugged highland stretching along the eastern side of the Arabah from the Dead Sea south toward the Gulf of Aqaba, the territory that became the ancestral homeland of Edom (Gen. 36:8–9). Before Esau's descendants settled there the land was inhabited by the Horites (\"cave dwellers\"), whose eponymous ancestor Seir is listed among the \"dukes\" of the land (Gen. 36:20–30).</p><p>The mountains of Seir appear repeatedly in Israel's wilderness journeys, prophetic oracles against Edom, and eschatological visions. Balaam's oracle envisions Israel's dominion over Seir (Num. 24:18), and the later prophets — Ezekiel and Obadiah most pointedly — pronounce judgment on Seir/Edom for violence against their brother Jacob. Mount Seir also figures in early hymnic poetry as a scene of the divine march in battle (Deut. 33:2; Judg. 5:4).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Genesis 36:20", "Genesis 14:6", "Deuteronomy 33:2", "Ezekiel 35:2"]
},
"seirath": {
  "id": "seirath",
  "term": "Seirath",
  "category": "places",
  "intro": "<p>Seirath (meaning: <em>woody district</em> or <em>shaggy</em>) was a location in the hill country bordering Benjamin and Ephraim to which Ehud fled after assassinating the Moabite king Eglon at Jericho (Judg. 3:26–27). From Seirath he blew a trumpet in the hill country of Ephraim, rallied Israel, and led the pursuit that secured the fords of the Jordan, cutting off the Moabite army and achieving a great deliverance for Israel.</p><p>The forested, rugged character suggested by the name would have provided Ehud effective cover during his flight. Though the precise location of Seirath is not identified with certainty, the narrative places it north of Jericho in the highland country west of the Jordan, where the terrain transitions from the Jordan Valley to the Ephraimite plateau.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Judges 3:26", "Judges 3:27"]
},
"sela": {
  "id": "sela",
  "term": "Sela",
  "category": "places",
  "intro": "<p>Sela (meaning: <em>the rock</em>) was the ancient capital of Edom, situated in the great valley extending from the Dead Sea to the Red Sea, near Mount Hor and the desert of Zin. The name simply describes the setting: a high, sheer rock plateau forming a natural fortress. Amaziah king of Judah captured it, renamed it Joktheel (\"subdued by God\"), and cast ten thousand Edomite prisoners from its cliffs (2 Kings 14:7).</p><p>Sela is almost certainly identified with the site later known as Petra, the spectacular rose-red city carved into sandstone cliffs by the Nabataeans. The prophets invoke Sela's rocky heights as both a symbol of Edom's pride and false security (Isa. 16:1; Obad. 1:3–4) and as a destination for the fugitives of Moab who might find shelter there (Isa. 16:1). Its natural impregnability made it the ideal image of a stronghold, whether of refuge or of proud self-reliance.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["2 Kings 14:7", "Isaiah 16:1", "Obadiah 1:3"]
},
"sela-hammahlekoth": {
  "id": "sela-hammahlekoth",
  "term": "Sela-hammahlekoth",
  "category": "places",
  "intro": "<p>Sela-hammahlekoth (meaning: <em>cliff of divisions</em> or <em>rock of separations</em>) was the name given to the great gorge that separated David from Saul during one of their most dramatic encounters in the wilderness south-east of Hebron. The name appears in 1 Samuel 23:28, explaining why Saul had to break off his pursuit of David: news of a Philistine raid compelled the king to turn away, and the two parties separated on opposite sides of the ravine.</p><p>The gorge is identified with the Wady Malaky, the deep, precipitous valley between the rocky heights of Hachilah and the wilderness of Maon. The name commemorates the providential deliverance of David, as the very landscape became the instrument of his rescue from Saul's hand.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["1 Samuel 23:28"]
},
"selah": {
  "id": "selah",
  "term": "Selah",
  "category": "concepts",
  "intro": "<p>Selah is a Hebrew term of uncertain meaning that appears approximately seventy-four times in the Book of Psalms and three times in the prayer of Habakkuk (Hab. 3:9, 13). It occurs at the end of strophes and at key turning points in poetic composition, suggesting it served some liturgical or musical function. Major interpretations include: a pause for reflection or silent prayer; an instruction to lift the voice or instruments; a musical interlude; or a direction to the congregation to prostrate itself in worship.</p><p>Though its precise meaning remains debated, Selah consistently appears at moments of theological weight — following declarations of God's power, statements of distress, or affirmations of trust. Its consistent presence at structurally significant points in the Psalter has led many scholars to conclude it was a performance notation ensuring that the content just sung was allowed to resonate before the next section began.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Habakkuk 3:9", "Habakkuk 3:13", "Psalms 46:3", "Psalms 47:4"]
},
"seleucia": {
  "id": "seleucia",
  "term": "Seleucia",
  "category": "places",
  "intro": "<p>Seleucia was the sea-port of Syrian Antioch, situated near the mouth of the Orontes River on the northeastern Mediterranean coast. It was founded by Seleucus I Nicator, ruler of the Seleucid kingdom after Alexander the Great's death, who named it after himself. The city served as the harbor through which Antioch — the third largest city of the Roman Empire and the mother church of Gentile Christianity — communicated with the wider world.</p><p>Paul and Barnabas sailed from Seleucia on the first missionary journey, beginning the sustained expansion of the gospel into Asia Minor and beyond (Acts 13:4). The return voyage of the first journey also concluded at Seleucia (Acts 14:26). Its strategic position made it the natural gateway for the missionary enterprise launched from Antioch.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Acts 13:4"]
},
"semei": {
  "id": "semei",
  "term": "Semei",
  "category": "people",
  "intro": "<p>Semei is a name appearing in the Lukan genealogy of Jesus Christ (Luke 3:26), listed in the long genealogical chain running from Jesus back through Joseph's line to Adam. The name is a Greek form of the Hebrew Shimei. Beyond its occurrence in this genealogy, no further details are given in Luke or in parallel texts.</p><p>Like many names in Luke's genealogy between Zerubbabel and Joseph, Semei is otherwise unknown in canonical Scripture. The genealogy's purpose is theological — tracing the full human lineage of the Son of God — rather than providing biographical data on every ancestor named.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Luke 3:26"]
},
"senaah": {
  "id": "senaah",
  "term": "Senaah",
  "category": "places",
  "intro": "<p>Senaah (meaning: <em>thorny</em>) was a settlement whose inhabitants returned from the Babylonian exile with Zerubbabel following Cyrus's decree. The list in Ezra 2:35 records 3,630 returning descendants of Senaah, and Nehemiah 7:38 gives a figure of 3,930 — one of the largest single contingents among the returnees. This suggests Senaah was a significant town, likely in the territory of Benjamin north of Jerusalem.</p><p>The sons of Senaah also contributed to rebuilding the Fish Gate of Jerusalem's walls under Nehemiah (Neh. 3:3), demonstrating the community's active participation in the restoration. The large number of returning exiles associated with this town indicates it had been a substantial center before the Babylonian deportation.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Ezra 2:35", "Nehemiah 7:38", "Nehemiah 3:3"]
},
"senate": {
  "id": "senate",
  "term": "Senate",
  "category": "concepts",
  "intro": "<p>The term \"senate\" in the New Testament (Acts 5:21) refers to the <em>gerousia</em> — the council of elders — which formed a component part of the Jewish Sanhedrin. When the high priest convened the full council to examine the apostles, the text distinguishes between \"the council\" (Sanhedrin) and \"all the senate of the children of Israel,\" suggesting either an expanded gathering or the formal designation of the elder body within the larger ruling institution.</p><p>The Jewish <em>gerousia</em> had deep roots in the Mosaic period, when Moses appointed seventy elders to assist in governing Israel (Num. 11:16–17). By the Second Temple period the eldership had become institutionalized within the Sanhedrin, which combined priestly, scribal, and lay-elder representation. The term's use in Acts reflects the formal dignity of the institution that was now confronting the early church.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Acts 5:21", "Numbers 11:16"]
},
"seneh": {
  "id": "seneh",
  "term": "Seneh",
  "category": "places",
  "intro": "<p>Seneh (meaning: <em>the acacia</em> or <em>rock-thorn</em>) was the name of the southern cliff in the Wady es-Suweinit, a narrow valley running south of Michmash. Jonathan and his armor-bearer climbed Seneh's rocky face in the bold assault that triggered the rout of the Philistine garrison at Michmash (1 Sam. 14:4–5, 13). The northern cliff facing it was called Bozez.</p><p>The two named cliffs flanking this ravine formed a natural pass of great military significance, as control of Michmash controlled movement between the northern and central highlands. Jonathan's daring climb — a sheer ascent on all fours — and the subsequent Philistine panic is one of the most vivid episodes of personal heroism in the books of Samuel.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["1 Samuel 14:4", "1 Samuel 14:13"]
},
"senir": {
  "id": "senir",
  "term": "Senir",
  "category": "places",
  "intro": "<p>Senir (also spelled Shenir) was the Amorite name for Mount Hermon (Deut. 3:9), the highest peak in the Anti-Lebanon range at the northern boundary of Canaan. The Sidonians called the same mountain Sirion. Some scholars interpret Senir as denoting only a part of the Hermon massif rather than the entire mountain, though the biblical evidence is not conclusive. The summit supplied timber for Phoenician shipbuilding: Ezekiel's lament over Tyre mentions planks of Senir firs used in the construction of Tyrian ships (Ezek. 27:5).</p><p>Hermon/Senir marked the northernmost extent of the territory Israel conquered east of the Jordan under Moses, and its snow-capped heights are celebrated in poetic texts (Ps. 89:12; Song 4:8). The mountain's prominence made it a natural boundary marker and a symbol of majestic natural grandeur.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Deuteronomy 3:9", "Ezekiel 27:5", "Psalms 89:12"]
},
"sennacherib": {
  "id": "sennacherib",
  "term": "Sennacherib",
  "category": "people",
  "intro": "<p>Sennacherib (meaning: <em>Sin the god sends many brothers</em>) was king of Assyria from approximately 705 to 681 B.C., succeeding his father Sargon II. He is best known in biblical history for his invasion of Judah in the fourteenth year of King Hezekiah (2 Kings 18:13; Isa. 36–37), during which he besieged and captured forty-six fortified cities and shut Hezekiah up \"like a bird in a cage\" in Jerusalem. His own annals on the Taylor Prism confirm this campaign in detail, making it one of the best-attested events linking Assyrian records to biblical narrative.</p><p>The siege of Jerusalem was not completed: the angel of the LORD struck the Assyrian camp overnight, killing 185,000 soldiers, and Sennacherib withdrew to Nineveh (2 Kings 19:35–36). He was later murdered by two of his own sons, Adrammelech and Sharezer, who then fled to Ararat, and his son Esarhaddon succeeded him (2 Kings 19:37). Sennacherib's arrogant blasphemy against God and his humiliation became a paradigm of divine sovereignty over imperial power.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["2 Kings 18:13", "2 Kings 19:35", "Isaiah 37:36", "2 Chronicles 32:1"]
},
"seorim": {
  "id": "seorim",
  "term": "Seorim",
  "category": "people",
  "intro": "<p>Seorim (meaning: <em>barley</em>) was the head of the fourth of the twenty-four priestly divisions organized by David for rotating temple service (1 Chr. 24:8). Under the system David established with Zadok and Ahimelech, the priestly families were assigned by lot to specific weeks of the year for service at the sanctuary — an arrangement continued and formalized by Solomon for the Jerusalem temple and maintained throughout the monarchy and beyond.</p><p>Seorim himself is otherwise unknown beyond this single reference. His course of service would have rotated to temple duty for one week in every twenty-four, a system that made the large priestly population manageable while ensuring continuous worship.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["1 Chronicles 24:8"]
},
"sephar": {
  "id": "sephar",
  "term": "Sephar",
  "category": "places",
  "intro": "<p>Sephar (meaning: <em>numbering</em> or <em>census</em>) is mentioned in the Table of Nations as the eastern boundary of the territory of the sons of Joktan, descendants of Shem (Gen. 10:30): their dwelling extended \"from Mesha, as thou goest unto Sephar, a mount of the east.\" Some scholars identify it with the ancient Himyaritic capital Zaphar on the Indian Ocean coast between the Persian Gulf and the Red Sea, in what is today Yemen.</p><p>If the identification with Zaphar is correct, Sephar marks the southeastern extent of early Semitic settlement in the Arabian Peninsula. Its remote location in the narrative of the Table of Nations makes it one of the most distant boundary markers in the genealogical-geographical description of the post-flood world.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Genesis 10:30"]
},
"sepharad": {
  "id": "sepharad",
  "term": "Sepharad",
  "category": "places",
  "intro": "<p>Sepharad is a place name that appears once in the Old Testament, in Obadiah 1:20, where the prophet declares that the exiles of Jerusalem in Sepharad will possess the cities of the Negev. The identification of Sepharad is uncertain; proposed locations include Sardis in Asia Minor (supported by a trilingual inscription at Sardis containing a form of the name), a region in Media, Sparta, or a location in Asia Minor. No consensus has been reached among scholars.</p><p>The name became enormously significant in Jewish tradition: medieval Jews identified Sepharad with Spain, and \"Sephardim\" (Spanish Jews) took their name from this identification, in contrast to \"Ashkenazim\" (Jews of the German-speaking lands). The Sephardic diaspora from Spain following the 1492 expulsion carried this identification across the Mediterranean world.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Obadiah 1:20"]
},
"sepharvaim": {
  "id": "sepharvaim",
  "term": "Sepharvaim",
  "category": "places",
  "intro": "<p>Sepharvaim was a city taken by the Assyrian empire and whose people were subsequently settled in the cities of Samaria to replace the deported Israelites (2 Kings 17:24). The Assyrian king Sennacherib later boasted that the gods of Sepharvaim had not saved it from Assyrian power (2 Kings 18:34; 19:13). The name is understood as a dual form meaning \"the two Sipparas\" — referring to the two cities of Sippar (Sippar-Yahrurum and Sippar-Amnanum) on the Euphrates north of Babylon, an important cult center of the sun-god Shamash.</p><p>The settlers from Sepharvaim brought their own gods with them to Samaria, worshipping Adrammelech and Anammelech with child sacrifice (2 Kings 17:31), contributing to the religious syncretism that characterized the population of Samaria after the fall of the Northern Kingdom.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["2 Kings 17:24", "2 Kings 18:34", "2 Kings 19:13"]
},
"septuagint": {
  "id": "septuagint",
  "term": "Septuagint",
  "category": "concepts",
  "intro": "<p>The Septuagint (abbreviated LXX, from the Latin <em>septuaginta</em>, \"seventy\") is the Greek translation of the Hebrew Old Testament, made for the Greek-speaking Jewish diaspora beginning in Alexandria in the third century B.C. According to the ancient Letter of Aristeas, seventy-two Jewish scholars completed the Pentateuch for Ptolemy II Philadelphus — hence the name. The remaining books were translated over the following two centuries, with varying quality and translation philosophy across different sections.</p><p>The Septuagint was the Bible of the early church. The New Testament authors quote the Old Testament predominantly from the LXX rather than the Hebrew, making it the primary scriptural text for the earliest Christian communities. It differs from the Masoretic (Hebrew) text at numerous points — in word order, in added or omitted material, and occasionally in theological nuance — and these variants are significant for textual criticism and the history of the biblical canon.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Luke 4:18", "Isaiah 61:1", "Acts 2:17", "Joel 2:28"]
},
"sepulchre": {
  "id": "sepulchre",
  "term": "Sepulchre",
  "category": "concepts",
  "intro": "<p>Sepulchre in biblical usage refers to the tombs and burial chambers used throughout Palestine. Abraham's purchase of the cave of Machpelah from Ephron the Hittite as a family burial place is the first extended treatment of the subject in Scripture (Gen. 23), establishing the pattern of family tomb ownership as a matter of legal title and deep cultural significance. The patriarchs — Abraham, Isaac, Jacob, Sarah, Rebekah, and Leah — were all buried there. Joseph's bones, carried through the wilderness, were finally interred in a field at Shechem (Josh. 24:32).</p><p>Tombs in biblical Palestine were typically natural or cut caves, sealed with a stone. Wealthy individuals commissioned elaborate rock-cut tombs, and royal tombs in Jerusalem were a distinct category. The most theologically significant sepulchre in Christian tradition is the tomb of Jesus, in or near which the resurrection occurred (John 20:1–18), and whose location has been venerated since at least the fourth century.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Genesis 23:20", "Joshua 24:32", "John 20:1", "Matthew 27:60"]
},
"serah": {
  "id": "serah",
  "term": "Serah",
  "category": "people",
  "intro": "<p>Serah (meaning: <em>abundance</em> or <em>princess</em>) was the daughter of Asher and granddaughter of Jacob, one of the few women named in the lists of those who went down to Egypt with Jacob (Gen. 46:17). She is listed again in the Mosaic census as a daughter of Asher (Num. 26:46, where the alternate spelling \"Sarah\" appears in some texts). Her inclusion in both the entry list and the wilderness census suggests she held a notable place in tribal memory.</p><p>A later tradition preserved in rabbinic literature celebrated Serah bat Asher as extraordinarily long-lived, attributing to her special knowledge of Israel's history and even a role in confirming Moses as the true redeemer. While these traditions go beyond the biblical text, they reflect the reverence in which this otherwise briefly-mentioned woman was held in Jewish memory.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Genesis 46:17", "Numbers 26:46"]
},
"seraiah": {
  "id": "seraiah",
  "term": "Seraiah",
  "category": "people",
  "intro": "<p>Seraiah (meaning: <em>soldier of Jehovah</em> or <em>Yahweh is prince</em>) is the name of several men in the Old Testament, reflecting the name's popularity in Israel and Judah. The most historically prominent is the chief priest Seraiah whom Nebuchadnezzar executed at Riblah after the fall of Jerusalem (2 Kings 25:18–21; Jer. 52:24–27) — the ancestor of Ezra (Ezra 7:1). Another Seraiah was David's royal secretary or scribe (2 Sam. 8:17, where the name appears as Shavsha or Sheva in parallel texts). A Seraiah son of Neriah was the quartermaster who accompanied Zedekiah to Babylon and was given Jeremiah's oracle of Babylon's fall to read and then sink in the Euphrates (Jer. 51:59–64).</p><p>The frequency of the name means several lesser-known individuals also bear it in the books of Chronicles, Nehemiah, and Jeremiah, each playing distinct roles in the administrative and priestly life of Judah.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["2 Kings 25:18", "Ezra 7:1", "Jeremiah 51:59", "2 Samuel 8:17"]
},
"seraphim": {
  "id": "seraphim",
  "term": "Seraphim",
  "category": "concepts",
  "intro": "<p>The seraphim are the celestial beings described in Isaiah's vision of the divine throne-room (Isa. 6:2–7). The name comes from the Hebrew root <em>saraph</em> (to burn), suggesting fiery ones — a reference perhaps to their burning radiance or their consuming love for God. They are portrayed as standing above the Lord, each with six wings: two covering their face in reverence, two covering their feet in humility, and two used for flight. They cry to one another \"Holy, holy, holy is the LORD of hosts; the whole earth is full of his glory.\"</p><p>One seraph takes a live coal from the altar and touches it to Isaiah's lips, declaring his iniquity taken away and his sin purged — the preparatory act for the prophetic commission that follows. The seraphim appear nowhere else in the Hebrew Bible under this name, though their function as worshipping attendants of the divine throne overlaps with that of the cherubim and the living creatures of Ezekiel and Revelation.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Isaiah 6:2", "Isaiah 6:3", "Isaiah 6:6", "Isaiah 6:7"]
},
"sered": {
  "id": "sered",
  "term": "Sered",
  "category": "people",
  "intro": "<p>Sered (meaning: <em>fear</em>) was the firstborn son of Zebulun and grandson of Jacob and Leah (Gen. 46:14). He was among the seventy souls of Jacob's house who went down into Egypt. His descendants formed the clan of the Sardites in the tribe of Zebulun (Num. 26:26), one of the family groups counted in the second Mosaic census in the wilderness of Moab.</p><p>Beyond these two genealogical references, Sered is not mentioned in the narrative of the Old Testament. As the head of a Zebulunite clan he represents one of the tribal sub-units through whom the tribe maintained its identity and land inheritance in the subsequent allotment.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Genesis 46:14", "Numbers 26:26"]
},
"sergeants": {
  "id": "sergeants",
  "term": "Sergeants",
  "category": "concepts",
  "intro": "<p>\"Sergeants\" in Acts 16:35 and 38 (Authorized Version) renders the Greek <em>rhabdouchoi</em> — literally \"rod-bearers\" — and is better translated \"lictors\" in the Revised Version. Lictors were the official attendants of Roman magistrates, carrying the <em>fasces</em> (bundle of rods, sometimes with an axe) as symbols of the magistrate's authority to punish and execute. In Roman colonies like Philippi, the magistrates (called <em>strategi</em> or praetors) were attended by two lictors each.</p><p>These are the officers who delivered Paul and Silas to the jailer and who returned the next morning to release them. When Paul revealed his Roman citizenship, the magistrates feared because they had ordered the public beating of Roman citizens without trial — an illegal act — and came in person to escort Paul and Silas out of prison (Acts 16:35–39).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Acts 16:35", "Acts 16:38"]
},
"sergius-paulus": {
  "id": "sergius-paulus",
  "term": "Sergius Paulus",
  "category": "people",
  "intro": "<p>Sergius Paulus was the Roman proconsul of Cyprus during Paul and Barnabas's first missionary journey, described in Acts 13:6–12 as \"a prudent man\" (or \"man of understanding\"). He summoned Paul and Barnabas to hear the word of God, but his access was blocked by the Jewish sorcerer Bar-Jesus (Elymas), who sought to turn the proconsul away from the faith. Paul, filled with the Holy Spirit, pronounced a curse of temporary blindness on Elymas, and when the proconsul witnessed the judgment fall, \"he believed, being astonished at the doctrine of the Lord.\"</p><p>Sergius Paulus is one of the most prominent Roman officials recorded as converting to Christianity in the New Testament era. An inscription discovered at Paphos mentioning a Sergius Paulus has been cited as possible corroborating evidence for his historicity, though the identification is debated. His conversion at the very outset of the first missionary journey signals the gospel's penetration into the highest levels of Roman provincial administration.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Acts 13:6", "Acts 13:12"]
},
"sermon-on-the-mount": {
  "id": "sermon-on-the-mount",
  "term": "Sermon on the mount",
  "category": "events",
  "intro": "<p>The Sermon on the Mount is the name given to Jesus's extended discourse preserved in Matthew 5–7, delivered on a mountain (or elevated plain, per Luke 6:17) in the vicinity of the Sea of Galilee following a night of prayer and the formal calling of the Twelve. It opens with the Beatitudes — eight declarations of blessing addressing the poor in spirit, the mournful, the meek, the hungry for righteousness, the merciful, the pure in heart, the peacemakers, and the persecuted — and proceeds through the greater righteousness Jesus demands in contrast to Pharisaic interpretation, instruction on prayer (including the Lord's Prayer), warnings against false religion, and a closing call to build on the rock of obedience to his words.</p><p>The Sermon on the Mount functions in Matthew as the inaugural manifesto of the kingdom of God, paralleling the giving of the Law at Sinai but surpassing it in authority: \"You have heard it said… but I say to you.\" It has shaped Christian ethics, catechesis, and social thought more profoundly than any other single teaching passage in the Gospels.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Matthew 5:1", "Luke 6:17", "Matthew 7:28", "Matthew 5:3"]
},
"serpent": {
  "id": "serpent",
  "term": "Serpent",
  "category": "concepts",
  "intro": "<p>The serpent appears at pivotal moments throughout Scripture, from the Garden of Eden to the Apocalypse. In Genesis 3 the serpent is the instrument of the temptation that brought sin into human experience, and the divine curse upon it (Gen. 3:14–15) introduces the proto-evangelium — the promise of enmity between the serpent's seed and the woman's seed, and of the ultimate crushing of the serpent. More than forty species of snake inhabited the ancient Near East, and the poisonous character of many species made the serpent a potent symbol of danger and death in biblical poetry and prophecy.</p><p>The bronze serpent Moses lifted up in the wilderness (Num. 21:8–9) became a type of the crucifixion in Jesus's own interpretation (John 3:14–15). The New Testament identifies the ancient serpent of Eden with Satan and the devil (Rev. 12:9; 20:2), tying together the narrative arc from fall to final judgment. Paul, writing on spiritual gifts, includes the handling of serpents in the list of signs accompanying believers in some early traditions (Mark 16:18).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Genesis 3:14", "Numbers 21:8", "John 3:14", "Revelation 12:9"]
},
"serpent-fiery": {
  "id": "serpent-fiery",
  "term": "Serpent, Fiery",
  "category": "concepts",
  "intro": "<p>The fiery serpents sent among Israel in the wilderness (Num. 21:6) were likely the <em>naja haje</em> (Egyptian cobra) or a similarly swift and deadly species whose bite produced an intense burning sensation — hence the term <em>seraphim</em> (fiery ones), the same Hebrew root as the heavenly beings of Isaiah 6. God sent them as judgment for Israel's repeated complaint against Moses and against God during the journey from Ezion-gaber. Many Israelites died from their bites.</p><p>At Moses's intercession God commanded him to make a bronze serpent and set it on a pole, so that any bitten person who looked at it would live (Num. 21:8–9). Jesus cites this episode as a direct type of his own crucifixion: \"As Moses lifted up the serpent in the wilderness, even so must the Son of Man be lifted up, that whoever believes in him should not perish\" (John 3:14–15). The bronze serpent was later destroyed by Hezekiah when it became an object of idolatrous veneration (2 Kings 18:4).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Numbers 21:6", "Numbers 21:8", "John 3:14", "2 Kings 18:4"]
},
"serug": {
  "id": "serug",
  "term": "Serug",
  "category": "people",
  "intro": "<p>Serug (meaning: <em>branch</em> or <em>shoot</em>) was the son of Reu and great-great-grandfather of Abraham in the Shemite genealogy of Genesis 11:20–23. He is called Saruch in the Greek Septuagint and in Luke's genealogy of Jesus (Luke 3:35). Serug lived 230 years, fathering Nahor at age thirty and living another two centuries afterward, according to the Masoretic chronology.</p><p>Serug stands in the post-flood genealogy of Shem at the transitional generation when, according to the later tradition preserved in Jubilees and other sources, idolatry began to spread among the descendants of Noah. Though the biblical text says nothing of this, the long-lived ancestors of the Abrahamic line represent the narrowing genealogical path through which the covenant promises would pass.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Genesis 11:20", "Luke 3:35"]
},
"servitor": {
  "id": "servitor",
  "term": "Servitor",
  "category": "concepts",
  "intro": "<p>The word \"servitor\" appears only once in the Authorized Version, in 2 Kings 4:43, where Elisha's servant questions how forty loaves could be distributed to a hundred men. The Revised Version renders the Hebrew as \"servant,\" and the same word elsewhere appears as \"minister\" (Ex. 24:13; 33:11). The term describes a personal attendant or assistant to a man of God, functioning as aide and household manager.</p><p>In the Elisha narratives the servitor — likely Gehazi, identified as Elisha's principal assistant — acts as intermediary between the prophet and those who came to him. The episode in 2 Kings 4:43–44 becomes a foreshadowing of the feeding miracles recorded in the Gospels, as Elisha's faith overrode the servant's practical objection and the bread fed all with food to spare.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["2 Kings 4:43", "Exodus 24:13"]
},
"seth": {
  "id": "seth",
  "term": "Seth",
  "category": "people",
  "intro": "<p>Seth (meaning: <em>appointed</em> or <em>a substitute</em>) was the third son of Adam and Eve, born after the murder of Abel by Cain (Gen. 4:25; 5:3). Eve named him Seth because, she said, \"God has appointed me another seed instead of Abel, whom Cain killed.\" Seth thus represents the divinely provided continuation of the line through which the promised seed (Gen. 3:15) would eventually come — a line marked by the beginnings of formal worship (\"then men began to call upon the name of the LORD,\" Gen. 4:26), in contrast to the line of Cain.</p><p>The Sethite genealogy in Genesis 5 traces the line from Adam through Seth to Noah, spanning ten generations with remarkable longevity. Seth fathered Enosh at age 105 and lived a total of 912 years. In Luke's genealogy of Jesus, Seth appears directly after Adam (Luke 3:38), marking the line through which the Son of God entered human history.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Genesis 4:25", "Genesis 5:3", "Genesis 4:26", "Luke 3:38"]
},
"sethur": {
  "id": "sethur",
  "term": "Sethur",
  "category": "people",
  "intro": "<p>Sethur (meaning: <em>hidden</em> or <em>concealed</em>) was the representative of the tribe of Asher among the twelve men Moses sent to spy out the land of Canaan (Num. 13:13). His father was Michael. Sethur is one of the ten spies who returned with a discouraging report about the strength of the Canaanite inhabitants, contributing to Israel's forty-year delay in entering the promised land — though the text does not name individually those who brought the evil report versus the faithful two, Caleb and Joshua.</p><p>Beyond his appearance in the spy narrative, Sethur is not mentioned elsewhere in Scripture. His name and tribal assignment reflect the formal representation of all twelve tribes in this pivotal reconnaissance mission.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Numbers 13:13"]
},
"seven": {
  "id": "seven",
  "term": "Seven",
  "category": "concepts",
  "intro": "<p>The number seven holds a uniquely prominent place in biblical numerology, grounded in the seven days of the creation week. God rested on the seventh day and sanctified it (Gen. 2:2–3), establishing the pattern of the Sabbath that structured Israel's calendar at every level: the seventh-day Sabbath, the seventh-year sabbatical release, and the seven-times-seven Jubilee. The number pervades ritual law: seven days of priestly consecration, seven-day feasts, seven-day periods of purification, and the seven-branched menorah in the tabernacle.</p><p>Seven appears throughout Scripture as the number of completeness and perfection. The Psalms speak of praising God seven times a day (Ps. 119:164); the perfectly refined word of God is silver purified seven times (Ps. 12:6). In the New Testament the Book of Revelation structures its visions around sevens: seven churches, seven seals, seven trumpets, seven bowls — signaling the completeness of God's purposes in history and judgment.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Genesis 2:2", "Leviticus 25:4", "Psalms 12:6", "Revelation 1:4"]
},
"seventy-weeks": {
  "id": "seventy-weeks",
  "term": "Seventy weeks",
  "category": "concepts",
  "intro": "<p>The seventy weeks (or seventy \"sevens\") is a prophetic period revealed to Daniel in answer to his prayer for Jerusalem (Dan. 9:24–27). The angel Gabriel announces that seventy weeks are determined upon Daniel's people and holy city \"to finish the transgression, to make an end of sins, to make reconciliation for iniquity, to bring in everlasting righteousness, to seal up the vision and prophecy, and to anoint the most Holy.\" The period is further subdivided into seven weeks, sixty-two weeks, and a final week, with a gap implied between the sixty-ninth and seventieth weeks in many interpretations.</p><p>Most interpreters read the \"weeks\" as weeks of years (each week = seven years), giving a total span of 490 years. The majority Christian tradition identifies the fulfillment in the ministry, death, and resurrection of Christ, who brings to an end the old covenant sacrificial system. Dispensationalist interpretation places the final week in a future eschatological period. The passage is one of the most discussed prophetic texts in the entire Old Testament.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Daniel 9:24", "Daniel 9:25", "Daniel 9:26", "Daniel 9:27"]
},
"shaalabbin": {
  "id": "shaalabbin",
  "term": "Shaalabbin",
  "category": "places",
  "intro": "<p>Shaalabbin (also Shaalbim, meaning: <em>place of foxes</em>) was a town in the allotment of the tribe of Dan (Josh. 19:42). The Amorites proved difficult to dislodge from the area and continued to dwell in Shaalabbin, though the Ephraimites eventually placed them under forced labor (Judg. 1:35). By the time of Solomon's administration it was one of the towns from which the king drew provisions (1 Kings 4:9), indicating it had been incorporated into the settled administration of the united kingdom.</p><p>The site is tentatively identified with the modern village of Selbit in the Aijalon Valley, west of Jerusalem. The Aijalon Valley, through which the town was located, was the site of Joshua's miraculous battle when the sun stood still (Josh. 10:12).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Joshua 19:42", "Judges 1:35", "1 Kings 4:9"]
},
"shaaraim": {
  "id": "shaaraim",
  "term": "Shaaraim",
  "category": "places",
  "intro": "<p>Shaaraim (meaning: <em>two gates</em>) appears as the name of two distinct places in the Old Testament. (1) A city in the Shephelah lowlands of Judah (Josh. 15:36), on or near the road running northwest from the Valley of Elah toward the coastal plain. After David's defeat of Goliath the Philistines were pursued \"to the gates of Ekron\" and their slain lay along \"the road to Shaaraim\" (1 Sam. 17:52). It is probably to be identified with Tell Zakariya or Kefr Zakariya in the Valley of Elah. (2) A town in the territory of Simeon (1 Chr. 4:31), also called Sharuhen or Shilhim.</p><p>The strategic position of Shaaraim (1) on the edge of the Shephelah, between the Philistine plain and the Judean highlands, made it a significant site in the ongoing territorial contest between Israel and Philistia.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["1 Samuel 17:52", "Joshua 15:36"]
},
"shaashgaz": {
  "id": "shaashgaz",
  "term": "Shaashgaz",
  "category": "people",
  "intro": "<p>Shaashgaz (meaning: <em>servant of the beautiful</em> or possibly a Persian name) was the chamberlain (chief eunuch) in charge of the second house of the harem of the Persian king Ahasuerus (Esther 2:14). After a young woman's initial night with the king she was transferred to the custody of Shaashgaz, who managed the concubines' quarters, distinct from the house of Hegai who supervised the virgins in preparation for their audience with the king.</p><p>Shaashgaz appears only in this single verse. His role in the Esther narrative illustrates the elaborate administrative structure of the Persian royal household, where different officials oversaw the various divisions of the harem. The account of Esther's rise from the house of Hegai to queen provides the backdrop against which Shaashgaz's role is incidentally described.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Esther 2:14"]
},
"shabbethai": {
  "id": "shabbethai",
  "term": "Shabbethai",
  "category": "people",
  "intro": "<p>Shabbethai (meaning: <em>sabbath-born</em>) was a Levite active in the post-exilic community of Jerusalem who is mentioned three times in Ezra and Nehemiah. He was among those who assisted Ezra in the investigation and resolution of the crisis of mixed marriages among the returned exiles (Ezra 10:15), participated in the public reading and explanation of the law at the Water Gate alongside Ezra (Neh. 8:7), and was among the Levitical leaders who had oversight of the external affairs of the house of God in Nehemiah's reorganized community (Neh. 11:16).</p><p>Shabbethai's consistent involvement in key moments of community reform — the marriage crisis, the law reading, and the post-wall-building reorganization — marks him as a significant Levitical figure in the restoration period, even though no further biographical details are given.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Ezra 10:15", "Nehemiah 8:7", "Nehemiah 11:16"]
},
"shaddai": {
  "id": "shaddai",
  "term": "Shaddai",
  "category": "concepts",
  "intro": "<p>Shaddai (or <em>El Shaddai</em>) is one of the primary divine names in the Hebrew Bible, traditionally translated \"the Almighty.\" The name appears forty-eight times in the Old Testament, thirty-one of which are in Job alone, making it the characteristic name for God in that book's theological reflection on suffering and sovereignty. God reveals himself to the patriarchs by this name: \"I am God Almighty [El Shaddai]; walk before me and be blameless\" (Gen. 17:1; cf. Ex. 6:3).</p><p>The etymology of Shaddai is disputed: proposed derivations connect it to a word for mountain (suggesting \"God of the mountains,\" a deity of power and might), or to a root meaning \"sufficient\" (God who is all-sufficient), or to an Akkadian cognate. Whatever the precise etymology, the name consistently emphasizes God's overwhelming power and his sovereign ability to bless and curse. It is used in the Balaam oracles (Num. 24:4, 16) and in Ruth's lament (Ruth 1:20–21), where Naomi says \"the Almighty has dealt very bitterly with me.\"</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Genesis 17:1", "Exodus 6:3", "Job 5:17", "Ruth 1:20"]
},
"shadow": {
  "id": "shadow",
  "term": "Shadow",
  "category": "concepts",
  "intro": "<p>Shadow as a theological concept in the New Testament describes the typical or anticipatory relationship of the Mosaic law and its institutions to the realities fulfilled in Christ. Paul writes in Colossians 2:17 that the Jewish festivals, new moons, and sabbaths are \"a shadow of things to come, but the body [substance] is of Christ.\" The Letter to the Hebrews develops this most fully: the Levitical priesthood and sacrificial system are \"a shadow of the heavenly things\" (Heb. 8:5) and \"a shadow of good things to come\" rather than the very form of those realities (Heb. 10:1).</p><p>This typological framework — shadow versus substance, copy versus original — is foundational to the New Testament's interpretation of the Old Testament. The shadow is not false or worthless; it is a real projection of the coming reality cast backward in time. But the shadow passes when the substance arrives: the death of Christ renders the entire shadow-system of temple, priesthood, and sacrifice obsolete and fulfilled.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Colossians 2:17", "Hebrews 8:5", "Hebrews 10:1"]
},
"shadrach": {
  "id": "shadrach",
  "term": "Shadrach",
  "category": "people",
  "intro": "<p>Shadrach was the Babylonian name given to Hananiah, one of the four young men of Judah brought to Nebuchadnezzar's court and trained for royal service (Dan. 1:6–7). His Hebrew name means \"Yahweh is gracious\"; Shadrach is understood as meaning \"Aku's command\" or may be a deliberate Babylonian substitution. He and his companions Meshach and Abednego refused to worship the golden image Nebuchadnezzar erected on the plain of Dura, declaring that their God was able to deliver them — but even if he did not, they would not serve the king's gods (Dan. 3:17–18).</p><p>Thrown into a furnace heated seven times hotter than normal, they were seen walking unbound in the flames accompanied by a fourth figure \"like a son of the gods.\" They emerged unharmed, without even the smell of smoke on their garments. Their deliverance prompted Nebuchadnezzar to issue a decree protecting the God of Shadrach, Meshach, and Abednego throughout the empire, and the three were promoted to higher offices.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Daniel 1:6", "Daniel 3:17", "Daniel 3:25", "Daniel 3:30"]
},
"shalem": {
  "id": "shalem",
  "term": "Shalem",
  "category": "places",
  "intro": "<p>Shalem (meaning: <em>perfect</em> or <em>complete</em>) is identified in Genesis 33:18 as the place where Jacob, returning from Paddan-aram, arrived \"safely\" (or \"to Shalem, a city of Shechem\"). The text is ambiguous as to whether Shalem is a proper place name or the Hebrew adverb meaning \"safely.\" Many translations render it as an adverb, reading that Jacob came safely to the city of Shechem. If a place name, it may designate a village near Shechem, tentatively identified with a site about two miles east of Jacob's well near modern Nablus.</p><p>Regardless of the textual question, Genesis 33:18–20 describes Jacob's purchase of land at Shechem and his erection of an altar there called El-Elohe-Israel, marking his return to Canaan as a theologically significant act of worship and territorial settlement.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Genesis 33:18", "Genesis 33:20"]
},
"shalim-land-of": {
  "id": "shalim-land-of",
  "term": "Shalim, Land of",
  "category": "places",
  "intro": "<p>The land of Shalim (meaning: <em>land of foxes</em>) is mentioned in 1 Samuel 9:4 as one of the districts through which Saul and his servant passed in their fruitless search for his father's lost donkeys, before finally seeking the seer Samuel. Its location is uncertain but appears to lie in the general vicinity of Benjamin's northern border, perhaps near the district of Shaalabbin in Dan (Josh. 19:42).</p><p>The journey through Shalim and adjacent territories before reaching the territory of Zuph — where Samuel lived — sets the geographical stage for Saul's providential encounter with the prophet who would anoint him Israel's first king. The ordinary errand of recovering lost animals becomes the occasion for a divinely orchestrated meeting.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["1 Samuel 9:4"]
},
"shalisha-land-of": {
  "id": "shalisha-land-of",
  "term": "Shalisha, Land of",
  "category": "places",
  "intro": "<p>The land of Shalisha is mentioned alongside the land of Shalim in 1 Samuel 9:4 as part of the territory through which Saul searched for his father's lost donkeys before encountering Samuel. It is probably to be identified with the district of Baal-shalisha (2 Kings 4:42), lying approximately twelve miles north of Lydda in the western slopes of the Ephraimite highlands — a fertile area from which a man brought Elisha twenty loaves of barley bread.</p><p>Like the land of Shalim, Shalisha serves primarily as a geographical marker in the narrative of Saul's journey, establishing that he had traveled widely through Benjamin and adjacent districts before the providential turn of events that brought him to the prophet.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["1 Samuel 9:4", "2 Kings 4:42"]
},
"shallecheth-the-gate-of": {
  "id": "shallecheth-the-gate-of",
  "term": "Shallecheth, The gate of",
  "category": "places",
  "intro": "<p>The gate of Shallecheth (meaning: <em>the gate of casting out</em>, sometimes interpreted as the refuse or rubbish gate) was one of the gates of the Jerusalem temple complex mentioned in 1 Chronicles 26:16. It was located \"by the causeway of the going up\" — the ascending roadway from the Tyropoeon Valley on the western side of the temple mount — and was assigned to the gatekeeping family of Shuppim and Hosah, with Obed-edom's sons serving the storehouse nearby.</p><p>The name may indicate it was the gate through which refuse, ash from the altar, and spent materials were removed from the sacred precincts. Its precise location within the complex of temple gates is uncertain, as the topography of the temple mount is known only partially from textual and archaeological evidence.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["1 Chronicles 26:16"]
},
"shallum": {
  "id": "shallum",
  "term": "Shallum",
  "category": "people",
  "intro": "<p>Shallum (meaning: <em>retribution</em> or <em>the recompensed one</em>) is the name of several persons in the Old Testament. The most historically significant was Shallum son of Jabesh, who assassinated King Zechariah of Israel in public view (fulfilling Jehu's dynasty's termination after four generations), reigned only one month, and was then killed by Menahem son of Gadi (2 Kings 15:10–15). A second prominent Shallum was the husband of Huldah the prophetess, keeper of the royal wardrobe, through whose wife King Josiah received the word of God regarding the newly discovered book of the law (2 Kings 22:14).</p><p>Other bearers of the name include a son of King Josiah (the same as Jehoahaz, 1 Chr. 3:15; Jer. 22:11), a son of Sismai in the genealogy of Judah (1 Chr. 2:40–41), a Levite gatekeeper who was ancestor of Ezra (Ezra 7:2), and several others in Chronicles, Ezra, and Nehemiah.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["2 Kings 15:10", "2 Kings 22:14", "Jeremiah 22:11"]
},
"shalman": {
  "id": "shalman",
  "term": "Shalman",
  "category": "people",
  "intro": "<p>Shalman is named in Hosea 10:14 in the warning \"as Shalman spoiled Beth-arbel in the day of battle,\" cited as a precedent for the destruction about to fall on Israel. The identity of Shalman is debated: most scholars identify him with Shalmaneser IV (or II in some reckonings), the Assyrian king who warred against Israel and to whom Hoshea paid tribute (2 Kings 17:3; 18:9), though Shalmaneser V is another candidate. Some have suggested a Moabite or other regional king named Shalmanu.</p><p>The incident at Beth-arbel is not recorded elsewhere in the Old Testament, making Hosea's allusion difficult to place with precision. Beth-arbel is generally identified with modern Irbid in northern Jordan, and its violent fall apparently served as a notorious example of Assyrian brutality well known to Hosea's audience.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Hosea 10:14", "2 Kings 17:3", "2 Kings 18:9"]
},
"shamgar": {
  "id": "shamgar",
  "term": "Shamgar",
  "category": "people",
  "intro": "<p>Shamgar son of Anath was one of the judges of Israel who delivered the nation from Philistine oppression in the period between Joshua and the monarchy. With only two verses devoted to him (Judg. 3:31; 5:6), he remains one of the most briefly described judges, yet his feat is remarkable: he struck down six hundred Philistines with an ox goad — a long iron-tipped agricultural implement — in a single engagement. The Philistines had been raiding the Israelite highlands from the coastal plain, and Shamgar's resistance broke their grip long enough to provide a period of rest.</p><p>The song of Deborah mentions \"the days of Shamgar son of Anath\" as a time of lawlessness on the highways (Judg. 5:6), suggesting his judge-ship preceded Deborah's and was a period of acute insecurity before her deliverance. His non-Israelite name (Anath was a Canaanite goddess) may indicate he was of mixed or Canaanite background who nevertheless acted as Israel's deliverer.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Judges 3:31", "Judges 5:6"]
},
"shamir": {
  "id": "shamir",
  "term": "Shamir",
  "category": "places",
  "intro": "<p>Shamir (meaning: <em>a sharp thorn</em>) is the name of a place and a person in the Old Testament. (1) As a town it appears in two distinct locations: in the hill country of Judah (Josh. 15:48), tentatively identified with Somerah about 2½ miles northwest of Debir; and as the residence and burial place of the judge Tola son of Puah in the hill country of Ephraim (Judg. 10:1–2). (2) As a personal name, Shamir was a son of Michah in the Levitical genealogy of 1 Chronicles 24:24.</p><p>The two places named Shamir are geographically separate, one in the southern highlands of Judah and one in the central highlands of Ephraim, reflecting how common place names were recycled across different tribal territories in ancient Canaan.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Joshua 15:48", "Judges 10:1", "1 Chronicles 24:24"]
},
"shammah": {
  "id": "shammah",
  "term": "Shammah",
  "category": "people",
  "intro": "<p>Shammah is the name of several men in the Old Testament. (1) A grandson of Esau and an Edomite chieftain (Gen. 36:13, 17). (2) The third son of Jesse and older brother of David (1 Sam. 16:9), also called Shimeah (2 Sam. 13:3) and Shimma (1 Chr. 2:13) — he was among the sons passed over by Samuel before the anointing of David. (3) One of David's three chief mighty men, Shammah son of Agee the Hararite, celebrated for his heroic defense of a plot of lentils against the Philistines when other Israelites fled — \"the LORD wrought a great victory\" through him (2 Sam. 23:11–12).</p><p>The Davidic mighty man Shammah represents the celebrated warrior tradition around David's court, whose individual acts of valor are memorialized in 2 Samuel 23.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["1 Samuel 16:9", "2 Samuel 23:11", "Genesis 36:13"]
},
"shammua": {
  "id": "shammua",
  "term": "Shammua",
  "category": "people",
  "intro": "<p>Shammua (meaning: <em>heard</em> or <em>renowned</em>) is the name of several persons in the Old Testament. (1) The spy sent from the tribe of Reuben — son of Zaccur — one of the twelve who scouted the land of Canaan (Num. 13:4). (2) One of David's sons born in Jerusalem — listed as Shammua (2 Sam. 5:14; 1 Chr. 14:4) or Shimea (1 Chr. 3:5) — the son of Bathsheba. (3) A Levite who assisted Nehemiah in organizing the dedication of the Jerusalem wall (Neh. 12:18). (4) A Levite in Nehemiah's community (Neh. 11:17, possibly called Shemaiah elsewhere).</p><p>The frequency of the name reflects its common roots in the concept of God having heard a prayer, a theme prominent in birth narratives throughout the Old Testament.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Numbers 13:4", "2 Samuel 5:14", "Nehemiah 12:18"]
},
"shaphan": {
  "id": "shaphan",
  "term": "Shaphan",
  "category": "people",
  "intro": "<p>Shaphan son of Azaliah was the royal scribe (secretary of state) under King Josiah of Judah, playing a pivotal role in the religious reformation of 621 B.C. When the high priest Hilkiah discovered the Book of the Law in the temple during renovation work, he gave it to Shaphan, who read it and brought it to the king (2 Kings 22:3–10). Shaphan's reading aloud of the law before Josiah precipitated the king's great grief and the subsequent consultation of the prophetess Huldah, setting in motion Josiah's sweeping reforms.</p><p>Shaphan's family became an important dynasty of reform-minded officials: his son Ahikam protected Jeremiah from execution (Jer. 26:24), his grandson Gedaliah became governor of Judah after the Babylonian conquest (Jer. 40:5), and another son Elasah carried Jeremiah's letter to the exiles in Babylon (Jer. 29:3). The family thus represents the faithful remnant of Judah's administration across the last generation of the monarchy and into the exile.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["2 Kings 22:3", "2 Kings 22:8", "Jeremiah 26:24"]
},
"shaphat": {
  "id": "shaphat",
  "term": "Shaphat",
  "category": "people",
  "intro": "<p>Shaphat (meaning: <em>judge</em>) is the name of several men in the Old Testament. (1) The son of Hori and representative of the tribe of Simeon among the twelve spies sent to scout Canaan (Num. 13:5). (2) The father of Elisha the prophet (1 Kings 19:16, 19; 2 Kings 3:11; 6:31), an Abelmehelah farmer from across the Jordan; Elisha was plowing with twelve yoke of oxen when Elijah cast his mantle upon him. (3) One of David's chief herdsmen who had charge of the cattle in the valleys (1 Chr. 27:29). (4) A descendant of David through Shecaniah (1 Chr. 3:22). (5) A Gadite chief who settled in Bashan (1 Chr. 5:12).</p><p>The most theologically significant Shaphat is the father of Elisha, a man of sufficient wealth to own twelve yoke of oxen — evidence that the prophetic ministry could arise from agricultural prosperity as well as poverty.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Numbers 13:5", "1 Kings 19:16", "1 Chronicles 27:29"]
},
"shapher": {
  "id": "shapher",
  "term": "Shapher",
  "category": "places",
  "intro": "<p>Shapher (or Shepher, meaning: <em>brightness</em> or <em>beauty</em>) was one of the encampment sites of Israel during the wilderness wandering, mentioned in Numbers 33:23–24 between Kehelathah and Haradah. It is described as a mountain (\"mount Shapher\"), suggesting a prominent highland location on the route between Sinai and the plains of Moab. The exact identification of mount Shapher is uncertain, as many of the wilderness stations remain unlocated with confidence.</p><p>The itinerary of Numbers 33 provides the most complete list of Israel's wilderness stopping points, though the precise geography of most stations between Sinai and Kadesh-barnea cannot be determined from available evidence. Shapher appears in the middle section of this journey, in the general Sinai/Negev region.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Numbers 33:23", "Numbers 33:24"]
},
"sharaim": {
  "id": "sharaim",
  "term": "Sharaim",
  "category": "places",
  "intro": "<p>Sharaim is an alternate form of Shaaraim (meaning: <em>two gates</em>), appearing in Joshua 15:36 as one of the towns in the lowland district of Judah. The same town appears as Shaaraim in 1 Samuel 17:52 in the account of the Israelite pursuit of the Philistines after Goliath's defeat: the slain Philistines lay \"in the way to Shaaraim.\" Some scholars treat Sharaim and Shaaraim as the same site; Easton suggests an identification with Tell Zakariya and Kefr Zakariya in the Valley of Elah, approximately 3½ miles northwest of Socoh.</p><p>The valley of Elah, where David's encounter with Goliath took place, was the strategic corridor between the Philistine coastal plain and the Judean highlands, and Sharaim/Shaaraim lay along the road connecting these zones.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Joshua 15:36", "1 Samuel 17:52"]
},
"sharezer": {
  "id": "sharezer",
  "term": "Sharezer",
  "category": "people",
  "intro": "<p>Sharezer was a son of the Assyrian king Sennacherib who, together with his brother Adrammelech, murdered their father as he was worshipping in the temple of Nisroch his god (2 Kings 19:37; Isa. 37:38). After the assassination the two brothers fled to the land of Ararat (Urartu), and Sennacherib was succeeded by his son Esarhaddon. The Babylonian chronicle confirms that Sennacherib was killed by his own sons in 681 B.C., corroborating the biblical account, though it names only one son as the slayer.</p><p>The name Sharezer is an Assyrian compound, meaning approximately \"protect the king\" (a prayer to a deity). The parricide of Sennacherib, following so closely on his catastrophic loss of 185,000 troops before Jerusalem, was read by the biblical writers as divine retribution against the king who had blasphemed the God of Israel.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["2 Kings 19:37", "Isaiah 37:38"]
},
"sharon-saron": {
  "id": "sharon-saron",
  "term": "Sharon, Saron",
  "category": "places",
  "intro": "<p>Sharon (Greek: Saron) is the broad coastal plain extending along the Mediterranean from the Yarkon River north of Joppa to Mount Carmel, approximately thirty miles long and eight to fifteen miles wide. Celebrated in antiquity for its fertility and beauty, it was famous for its wildflowers — especially the rose of Sharon (Song 2:1) — and for its rich pastureland (1 Chr. 27:29). Isaiah repeatedly invokes Sharon as an emblem of abundant natural beauty, promising that in the age of restoration \"the glory of Lebanon shall be given unto it, the excellency of Carmel and Sharon\" (Isa. 35:2).</p><p>In the New Testament, Saron (Acts 9:35) is the plain from Lydda to Joppa, through which the news of Peter's healing of Aeneas spread, bringing many to faith in Christ. In prophecy Sharon is a symbol of God's transformative blessing: \"Sharon shall be a fold of flocks\" (Isa. 65:10), and the Messiah himself is called \"the rose of Sharon\" in the devotional tradition, drawing on the plain's association with natural glory.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["1 Chronicles 27:29", "Isaiah 35:2", "Song of Solomon 2:1", "Acts 9:35"]
},
}

def main():
    written = skipped = 0
    for slug, data in ARTICLES.items():
        if merge_article(slug, data):
            written += 1
        else:
            skipped += 1
    print(f"BP s2: Scripture → Sharon, Saron: wrote {written}, skipped {skipped} existing.")

main()
