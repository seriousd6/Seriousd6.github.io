import json, os, pathlib

OUT_DIR = 'data/biblepedia/articles'
os.makedirs(OUT_DIR, exist_ok=True)

def load_article(slug):
    p = pathlib.Path(OUT_DIR) / f'{slug}.json'
    return json.loads(p.read_text()) if p.exists() else None

def save_article(slug, data):
    p = pathlib.Path(OUT_DIR) / f'{slug}.json'
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False))

def merge_article(slug, data):
    if load_article(slug) is not None: return False
    save_article(slug, data); return True

ARTICLES = {
"taanach": {
  "term": "Taanach",
  "category": "places",
  "intro": "<p>Taanach was an ancient Canaanite royal city in the southwestern plain of Jezreel (Esdraelon), approximately 5 miles southeast of Megiddo. Its king was defeated by Joshua in the conquest (Josh. 12:21). Although assigned to Manasseh, the Canaanites were not immediately expelled (Judg. 1:27). The city is celebrated in Deborah's victory hymn: \"the kings of Canaan fought in Taanach by the waters of Megiddo\" (Judg. 5:19). Solomon placed Taanach in the fifth administrative district governed by Baana (1 Kgs. 4:12). Archaeological excavations at Tel Ta'annek have confirmed a major Bronze and Iron Age city here, yielding the famous \"cult stand\" and extensive cuneiform tablets.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "taanach", "smith": "taanach", "isbe": "taanach"},
  "key_refs": ["Joshua 12:21", "Judges 5:19", "1 Kings 4:12"]
},
"taanath-shiloh": {
  "term": "Taanath-shiloh",
  "category": "places",
  "intro": "<p>Taanath-shiloh (meaning \"approach to Shiloh\") was a town marking the eastern boundary of the territory of Ephraim (Josh. 16:6), mentioned only in the tribal boundary survey. The name suggests a location on the road approaching the sanctuary city of Shiloh. It has been tentatively identified with Khirbet Ta'na, approximately 10 miles southeast of Shechem, though the identification is uncertain. The site appears only in this single geographical reference and plays no further narrative role.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "taanath-shiloh"},
  "key_refs": ["Joshua 16:6"]
},
"tabbaoth": {
  "term": "Tabbaoth",
  "category": "people",
  "intro": "<p>Tabbaoth was the ancestor of a family of Nethinim (temple servants) who returned from Babylonian exile with Zerubbabel (Ezra 2:43; Neh. 7:46). The Nethinim were non-Israelite servants assigned to assist the Levites in the temple. Tabbaoth's descendants are listed among the first wave of returnees, suggesting a family with established temple service. The name means \"rings\" or \"signet rings.\"</p>",
  "hitchcock_meaning": "good; goodness of the Lord",
  "source_ids": {"easton": "tabbaoth"},
  "key_refs": ["Ezra 2:43", "Nehemiah 7:46"]
},
"tabbath": {
  "term": "Tabbath",
  "category": "places",
  "intro": "<p>Tabbath was a location in the Jordan valley on the route of the fleeing Midianite army after Gideon's surprise night attack (Judg. 7:22). The Midianites fled from Beth-shittah toward Zererath, \"as far as the border of Abel-meholah, by Tabbath.\" Its exact location is uncertain, though Abel-meholah (Elijah's hometown) was in the Jordan valley south of Beth-shan, placing Tabbath in the same general vicinity. The site appears only in this battle account.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "tabbath"},
  "key_refs": ["Judges 7:22"]
},
"tabeal": {
  "term": "Tabeal",
  "category": "people",
  "intro": "<p>Tabeal was the father of an unnamed man whom Rezin king of Syria and Pekah king of Israel planned to install as a puppet king of Judah in place of Ahaz, during the Syro-Ephraimite crisis of c. 735 B.C. (Isa. 7:6). Isaiah's prophecy to Ahaz countered this scheme with the assurance \"it shall not stand, and it shall not come to pass\" (Isa. 7:7), in the same oracle that gave the sign of Immanuel (Isa. 7:14). The Aramaic name Tabeal (\"God is good\") suggests a Syrian or pro-Syrian figure intended to be more pliable to Damascene interests than the Davidic Ahaz.</p>",
  "hitchcock_meaning": "good God",
  "source_ids": {"easton": "tabeal"},
  "key_refs": ["Isaiah 7:6"]
},
"tabeel": {
  "term": "Tabeel",
  "category": "people",
  "intro": "<p>Tabeel was a Persian official in Samaria who co-signed a letter to King Artaxerxes I opposing the Jewish rebuilding of Jerusalem (Ezra 4:7). The letter, written in Aramaic, accused the returned exiles of sedition and warned that a rebuilt Jerusalem would not pay taxes or toll. Artaxerxes ordered the work halted (Ezra 4:21–23). This Tabeel is distinct from Tabeal (Isa. 7:6). The name is Persian-era Aramaic, meaning \"God is good.\"</p>",
  "hitchcock_meaning": "good God",
  "source_ids": {"easton": "tabeel"},
  "key_refs": ["Ezra 4:7"]
},
"taberah": {
  "term": "Taberah",
  "category": "places",
  "intro": "<p>Taberah (meaning \"burning\") was a place in the wilderness where the LORD's fire broke out against the Israelites when they complained (Num. 11:1–3). The fire burned on the outskirts of the camp; Moses prayed and the fire was quenched, but the place was named Taberah to commemorate the judgment. Moses later recalled it as one of Israel's repeated provocations of God in the wilderness (Deut. 9:22). The episode underscores the deadly seriousness of grumbling against the divine provision.</p>",
  "hitchcock_meaning": "burning",
  "source_ids": {"easton": "taberah"},
  "key_refs": ["Numbers 11:1", "Numbers 11:3", "Deuteronomy 9:22"]
},
"tabering": {
  "term": "Tabering",
  "category": "concepts",
  "intro": "<p>\"Tabering\" is an archaic English term (from Middle English <em>tabour</em>, a small drum) meaning to beat repeatedly as on a drum. It appears once in the KJV: the maidens of Nineveh are pictured as \"tabering upon their breasts\" (Nah. 2:7) in lamentation as the city falls — a gesture of beating the breast in grief, described through the metaphor of drumming. The term reflects the widespread ancient practice of striking the chest as an expression of mourning, also seen in the NT (Luke 18:13; 23:48).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "tabering"},
  "key_refs": ["Nahum 2:7"]
},
"tabernacle": {
  "term": "Tabernacle",
  "category": "concepts",
  "intro": "<p>The Tabernacle (Hebrew <em>mishkan</em>, \"dwelling\"; <em>ohel mo'ed</em>, \"tent of meeting\") was the portable sanctuary God commanded Moses to construct as his dwelling place among Israel in the wilderness (Ex. 25–31; 35–40). Built from acacia wood, gold, silver, bronze, and fine linen with blue, purple, and scarlet yarns, it comprised an outer court (containing the bronze altar of burnt offering and the bronze laver), the Holy Place (containing the seven-branched menorah, the table of showbread, and the altar of incense), and the Holy of Holies (containing the ark of the covenant beneath the mercy seat and the two golden cherubim). The divine glory filled it upon completion (Ex. 40:34–38). The tabernacle traveled with Israel throughout the wilderness, set up at each campsite with the tribe of Levi encamped around it. It was eventually superseded by Solomon's Temple. The New Testament interprets the tabernacle typologically: the Word \"tabernacled\" among us (John 1:14), Christ's body is the true tabernacle (Heb. 9:11), and the entire system prefigures his high-priestly ministry (Heb. 8–10).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "tabernacle", "smith": "tabernacle", "isbe": "tabernacle"},
  "key_refs": ["Exodus 25:8", "Exodus 40:34", "Hebrews 9:11", "John 1:14"]
},
"tabernacles-feast-of": {
  "term": "Tabernacles, Feast of",
  "category": "events",
  "intro": "<p>The Feast of Tabernacles (Hebrew <em>Sukkot</em>, \"Booths\"; also called Feast of Ingathering) was one of the three great pilgrimage festivals of Israel (Ex. 23:16; Lev. 23:33–43; Deut. 16:13–15). Held on the 15th–22nd of Tishri (September–October), it followed the autumn harvest and commemorated Israel's forty years of wilderness dwelling. Worshippers lived in leafy booths (<em>sukkot</em>) for seven days as a reminder of the tents of the Exodus, and a solemn assembly on the eighth day closed the celebration. It was the most joyous of Israel's festivals and accompanied by an extensive schedule of sacrifices (Num. 29:12–38). Jesus attended the feast in Jerusalem (John 7:2–10) and on the last great day proclaimed himself the source of living water (John 7:37–39), alluding to the water-pouring ceremony performed each morning of the feast. Zechariah 14:16–19 envisions all nations keeping this feast in the eschatological age.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "tabernacles-feast-of", "smith": "tabernacles-feast-of", "isbe": "tabernacles-feast-of"},
  "key_refs": ["Leviticus 23:34", "Deuteronomy 16:13", "John 7:37", "Zechariah 14:16"]
},
"tabitha": {
  "term": "Tabitha",
  "category": "people",
  "intro": "<p>Tabitha (Aramaic, equivalent to Greek <em>Dorcas</em>, both meaning \"gazelle\") was a Christian disciple at Joppa renowned for her good works and charity — especially making garments for the widows of the congregation (Acts 9:36). When she died, the disciples sent for Peter, who came to Joppa, cleared the room of mourners, knelt in prayer, and commanded: \"Tabitha, arise.\" She opened her eyes and sat up, and Peter presented her alive (Acts 9:40–41). This miracle — the first apostolic resurrection in the NT narrative — became known throughout Joppa and led many to believe in the Lord (Acts 9:42). Tabitha's combination of faith and practical service to the poor makes her a model of Christian discipleship.</p>",
  "hitchcock_meaning": "clear-sighted; a roe-deer",
  "source_ids": {"easton": "tabitha", "smith": "tabitha"},
  "key_refs": ["Acts 9:36", "Acts 9:40", "Acts 9:42"]
},
"tables": {
  "term": "Tables",
  "category": "concepts",
  "intro": "<p>\"Tables\" in Scripture most commonly refers to the stone tablets of the law given to Moses on Sinai (Ex. 31:18; 34:1–4; Deut. 10:1–5), also called the \"tables of testimony.\" These two tablets, inscribed by the finger of God, were the physical documentation of the covenant between God and Israel and were kept in the ark of the covenant. The phrase \"tables of the heart\" appears in Proverbs (3:3; 7:3) and Jeremiah (17:1) — hearts as the surface on which instruction or sin is written. Paul contrasts Moses' stone tables with the \"fleshy tables of the heart\" written by the Spirit of the living God (2 Cor. 3:3). The \"tables of the moneychangers\" in the temple court were overturned by Jesus at his cleansing of the temple (Matt. 21:12; John 2:15).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "tables", "isbe": "tables"},
  "key_refs": ["Exodus 31:18", "Deuteronomy 10:2", "2 Corinthians 3:3", "Matthew 21:12"]
},
"tablet": {
  "term": "Tablet",
  "category": "concepts",
  "intro": "<p>In biblical usage, a tablet is a flat writing surface — of stone, clay, or wax-covered wood — used for inscribing laws, records, or prophetic messages. Isaiah is commanded to write a prophecy on a large tablet as a public witness (Isa. 30:8), and Habakkuk is told to write his vision plainly on tablets \"so that a runner may read it\" (Hab. 2:2). In the NT, Zechariah writes \"His name is John\" on a writing tablet (<em>pinakidion</em>, a small wax-coated board) when unable to speak, resolving the dispute over his son's name (Luke 1:63). The Hebrew word <em>luch</em> (tablet) is also used for the stone tablets of the law (Ex. 34:1) and the cedar planks of temple paneling (1 Kgs. 7:36).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "tablet", "isbe": "tablet"},
  "key_refs": ["Isaiah 30:8", "Habakkuk 2:2", "Luke 1:63"]
},
"tabor": {
  "term": "Tabor",
  "category": "places",
  "intro": "<p>Mount Tabor is an isolated, dome-shaped mountain rising approximately 1,843 feet above the surrounding plain of Jezreel in lower Galilee. It served as the mustering point for Barak's forces at Deborah's direction before the defeat of Sisera (Judg. 4:6, 12–14). The psalmist joins \"Tabor and Hermon\" as rejoicing in God's name (Ps. 89:12), and Jeremiah employs it as a metaphor for the certainty of coming judgment: \"Surely as Tabor is among the mountains... so shall he come\" (Jer. 46:18). The border of Zebulun reached Tabor (Josh. 19:22), and a Levitical city Chisloth-tabor was nearby (1 Chr. 6:77). Christian tradition from at least the 4th century has identified Tabor as the site of the Transfiguration, though the Synoptic Gospels specify only \"a high mountain\" (Matt. 17:1; Mark 9:2).</p>",
  "hitchcock_meaning": "choice; purity; bruising",
  "source_ids": {"easton": "tabor", "smith": "tabor", "isbe": "tabor"},
  "key_refs": ["Judges 4:6", "Psalms 89:12", "Jeremiah 46:18"]
},
"tabret": {
  "term": "Tabret",
  "category": "concepts",
  "intro": "<p>A tabret (Hebrew <em>toph</em>) was a small, hand-held frame drum or tambourine — a percussion instrument used in joyful celebration, worship, dance, and procession. Miriam led the women of Israel with tabrets and dancing after the crossing of the Red Sea (Ex. 15:20). Jephthah's daughter came out with tabrets to greet her returning father (Judg. 11:34). The instrument is prescribed for praise of the LORD (Ps. 81:2; 150:4) and appears in descriptions of festive processions (1 Sam. 18:6; 2 Sam. 6:5). Isaiah 5:12 lists the tabret among the instruments at the feasts of the wicked, and 14:11 uses it as a symbol of earthly pomp destined for Sheol.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "tabret", "isbe": "tabret"},
  "key_refs": ["Exodus 15:20", "Judges 11:34", "Psalms 150:4"]
},
"tabrimon": {
  "term": "Tabrimon",
  "category": "people",
  "intro": "<p>Tabrimon (meaning \"Rimmon is good\") was a Syrian king of Damascus, son of Hezion and father of Ben-hadad I (1 Kgs. 15:18). He is mentioned only in the genealogy of the Syrian royal house, in the context of King Asa of Judah sending a gift of silver and gold to Ben-hadad I, citing the league between their fathers — including Tabrimon — to persuade Ben-hadad to break his alliance with Baasha of Israel. The name incorporates the Aramaean storm deity Rimmon (Hadad), attesting to the religious culture of the Damascene kingdom.</p>",
  "hitchcock_meaning": "Remmon is good",
  "source_ids": {"easton": "tabrimon"},
  "key_refs": ["1 Kings 15:18"]
},
"taches": {
  "term": "Taches",
  "category": "concepts",
  "intro": "<p>Taches (from Old French <em>tache</em>, \"clasp\" or \"fastener\") were the gold and bronze clasps used to join the curtain panels of the tabernacle into a unified structure (Ex. 26:6, 11, 33; 36:13, 18). Fifty gold taches fastened together the two sets of fine linen inner curtains of the tabernacle; fifty bronze taches joined the two sets of goat-hair curtains constituting the outer tent covering. The architectural distinction — gold for the inner sanctuary curtains, bronze for the outer — reflects the graduated holiness of the tabernacle's zones, with the inner curtains nearest the Holy of Holies made from the most precious materials.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "taches"},
  "key_refs": ["Exodus 26:6", "Exodus 26:11"]
},
"tachmonite": {
  "term": "Tachmonite",
  "category": "people",
  "intro": "<p>The Tachmonite (or Tahchemonite) is the designation of Adino the Eznite, listed as \"the chief of the captains\" among David's thirty mighty men, credited with slaying eight hundred men at one time (2 Sam. 23:8). The parallel text in 1 Chronicles 11:11 names him Jashobeam the Hachmonite (Hachmoni). The divergence between the texts reflects textual corruption in one or both accounts; the heroic feat of individual combat against hundreds connects both descriptions. \"Tachmonite\" likely refers to a clan or place of origin.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "tachmonite"},
  "key_refs": ["2 Samuel 23:8", "1 Chronicles 11:11"]
},
"tackling": {
  "term": "Tackling",
  "category": "concepts",
  "intro": "<p>\"Tackling\" in Scripture denotes the ropes, rigging, and shipboard equipment. Isaiah employs the image of a storm-battered vessel whose tackling is loose as a metaphor for the helplessness of the nations before God: \"Thy tacklings are loosed; they could not well strengthen their mast, they could not spread the sail\" (Isa. 33:23 KJV). The contrast is with Zion, which shall be a place of \"quiet resting,\" whose stakes will never be removed. In Acts 27:19, the sailors on the storm-tossed ship carrying Paul cast the tackling overboard to lighten the vessel during the shipwreck voyage to Malta.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "tackling"},
  "key_refs": ["Isaiah 33:23", "Acts 27:19"]
},
"tadmor": {
  "term": "Tadmor",
  "category": "places",
  "intro": "<p>Tadmor (later known in Greek as Palmyra, \"city of palms\") was a strategic oasis city in the Syrian desert, approximately 150 miles northeast of Damascus. Solomon built Tadmor as a store-city and military outpost on the trade routes between the Mediterranean coast and Mesopotamia (1 Kgs. 9:18; 2 Chr. 8:4). The site's identification with Palmyra is well established archaeologically. Palmyra grew to great commercial and political prominence in the Roman period, controlling caravan trade across the Syrian desert, before being destroyed by the emperor Aurelian in A.D. 273. Today the ruins of Palmyra (a UNESCO World Heritage site) remain one of the most spectacular ancient sites in the Middle East.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "tadmor", "smith": "tadmor"},
  "key_refs": ["1 Kings 9:18", "2 Chronicles 8:4"]
},
"tahapanes": {
  "term": "Tahapanes",
  "category": "places",
  "intro": "<p>Tahapanes (also Tahpanhes; identified with ancient Daphne) was a fortified Egyptian border city in the eastern Nile Delta. After the fall of Jerusalem in 586 B.C., Jewish refugees fled to Egypt against Jeremiah's warnings, taking Jeremiah with them to Tahpanhes (Jer. 43:7–8). Jeremiah performed a symbolic act there, burying large stones at the entrance of Pharaoh's palace and prophesying that Nebuchadnezzar would erect his throne upon them in judgment on Egypt (Jer. 43:9–13). The city had already appeared in Jeremiah (2:16) as \"Noph and Tahapanes\" among Egypt's cities that would bring judgment on Israel's foolish reliance on Egypt.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "tahapanes", "smith": "tahapanes"},
  "key_refs": ["Jeremiah 2:16", "Jeremiah 43:7", "Jeremiah 43:9"]
},
"tahpenes": {
  "term": "Tahpenes",
  "category": "people",
  "intro": "<p>Tahpenes was an Egyptian queen, wife of an unnamed Pharaoh, who played a role in sheltering Israelite fugitives (1 Kgs. 11:19–20). When Hadad the Edomite prince fled to Egypt after David's general Joab killed the Edomite males, Pharaoh received him favorably and gave him the sister of Queen Tahpenes in marriage. Tahpenes weaned the resulting son, Genubath, in Pharaoh's household alongside the royal children. This alliance provided Solomon with a persistent adversary: Hadad returned to Edom and became a thorn in Solomon's side (1 Kgs. 11:14–22).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "tahpenes"},
  "key_refs": ["1 Kings 11:19", "1 Kings 11:20"]
},
"tahtim-hodshi": {
  "term": "Tahtim-hodshi",
  "category": "places",
  "intro": "<p>Tahtim-hodshi was a region visited by Joab's census team during David's ill-fated numbering of the people (2 Sam. 24:6). The census party traveled from Gilead through this region as part of their northern circuit before coming to Dan and Sidon. The Hebrew text here is uncertain — some manuscripts and versions read \"to the land of the Hittites, toward Kadesh\" — and the location has not been identified. The passage is part of the narrative that culminates in the plague sent as divine punishment for David's pride in numbering Israel.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "tahtim-hodshi"},
  "key_refs": ["2 Samuel 24:6"]
},
"tale": {
  "term": "Tale",
  "category": "concepts",
  "intro": "<p>\"Tale\" in biblical English most commonly carries the archaic sense of a count or tally (from Old English <em>talu</em>, \"reckoning\"), rather than a narrative. In the KJV, the Egyptian taskmasters require the Israelites to deliver the same \"tale of bricks\" (i.e., the same number or quota) without being provided straw (Ex. 5:8, 18). Psalm 90:9 speaks of spending years as \"a tale that is told\" — life passing swiftly as a spoken word. The related sense of \"talebearing\" (spreading gossip or slander) is condemned in the law (Lev. 19:16) and in Proverbs (11:13; 18:8; 20:19; 26:20–22).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "tale"},
  "key_refs": ["Exodus 5:8", "Psalms 90:9", "Leviticus 19:16"]
},
"talent": {
  "term": "Talent",
  "category": "concepts",
  "intro": "<p>A talent (Hebrew <em>kikkar</em>; Greek <em>talanton</em>) was the largest standard unit of weight and monetary value in the biblical world, equivalent to approximately 3,000 shekels (roughly 75 lbs or 34 kg). A talent of gold or silver represented an enormous sum — effectively a lifetime's wages for a laborer. David set aside 3,000 talents of gold and 7,000 talents of refined silver for the temple (1 Chr. 29:4). In Jesus' Parable of the Talents (Matt. 25:14–30), three servants receive 5, 2, and 1 talent respectively and are held accountable for how they employ them — a parable of faithful stewardship of what God entrusts. The Parable of the Unforgiving Servant features a debt of 10,000 talents (Matt. 18:24), a deliberately impossible sum representing humanity's unpayable moral debt to God.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "talent", "isbe": "talent"},
  "key_refs": ["1 Chronicles 29:4", "Matthew 25:15", "Matthew 18:24"]
},
"talitha-cumi": {
  "term": "Talitha Cumi",
  "category": "concepts",
  "intro": "<p>Talitha cumi (Aramaic טַלִּיתָא קוּמִי, \"little girl, arise\") are the words Jesus spoke when he raised the twelve-year-old daughter of Jairus from the dead (Mark 5:41). Mark preserves the Aramaic original alongside his Greek translation — \"Damsel, I say unto thee, arise\" — giving the reader direct access to Jesus' actual words. The diminutive <em>talitha</em> (\"little girl\" or \"little lamb\") expresses the tenderness of the moment. Immediately she rose and walked, causing astonishment among the witnesses (Mark 5:42–43). Jesus ordered that she be given food and that the miracle not be publicized. The preservation of these Aramaic words alongside \"Ephphatha\" (Mark 7:34) and \"Eloi, Eloi, lama sabachthani\" (Mark 15:34) reflects Mark's eyewitness detail.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "talitha-cumi"},
  "key_refs": ["Mark 5:41", "Mark 5:42"]
},
"talmai": {
  "term": "Talmai",
  "category": "people",
  "intro": "<p>Talmai was the name of two biblical figures. (1) Talmai was a son of Anak, one of the giant-clans (Anakim) inhabiting Hebron at the time of the spies' report (Num. 13:22). Caleb subsequently drove him out when he took possession of Hebron in fulfillment of Moses' promise (Josh. 15:14; Judg. 1:10). (2) Talmai king of Geshur (an Aramaic state east of the Jordan) was the father of Maacah, one of David's wives, who became the mother of Absalom (2 Sam. 3:3; 1 Chr. 3:2). After Absalom murdered his half-brother Amnon, he fled to his maternal grandfather Talmai in Geshur and remained three years before Joab arranged his recall to Jerusalem (2 Sam. 13:37–39).</p>",
  "hitchcock_meaning": "my furrows; that suspends the waters",
  "source_ids": {"easton": "talmai", "smith": "talmai"},
  "key_refs": ["Numbers 13:22", "Joshua 15:14", "2 Samuel 3:3", "2 Samuel 13:37"]
},
"talmon": {
  "term": "Talmon",
  "category": "people",
  "intro": "<p>Talmon was the head of a family of Levitical gatekeepers whose descendants returned from Babylonian exile (Ezra 2:42; Neh. 7:45) and served at the temple gates in Nehemiah's Jerusalem (Neh. 11:19; 12:25). The family of Talmon and Akkub are consistently mentioned together in the post-exilic records, suggesting they served in the same gatekeeper division. Gatekeepers held an honorable position in the temple hierarchy, controlling access to the sacred precincts and keeping watch at the four compass points of the sanctuary.</p>",
  "hitchcock_meaning": "injury; violent oppression",
  "source_ids": {"easton": "talmon"},
  "key_refs": ["Ezra 2:42", "Nehemiah 11:19", "Nehemiah 12:25"]
},
"tamar": {
  "term": "Tamar",
  "category": "people",
  "intro": "<p>Tamar was the name of several significant women in the OT. (1) Tamar the Canaanite was the daughter-in-law of Judah, whose husband Er died and then Onan. Denied her right to levirate marriage with Shelah, she disguised herself as a prostitute, conceived twins by Judah himself, and so secured her place in the covenant line (Gen. 38). From this union came Perez and Zerah; Perez is in the Messianic genealogy (Ruth 4:18–22; Matt. 1:3). (2) Tamar daughter of David and Maacah was violated by her half-brother Amnon, triggering Absalom's murder of Amnon and a cycle of royal family destruction (2 Sam. 13). David's failure to punish Amnon was a turning point in the disintegration of his household. (3) Absalom later named his own daughter Tamar — \"a woman of beautiful appearance\" (2 Sam. 14:27). The name also designates boundary locations in Ezekiel's restored land (Ezek. 47:19).</p>",
  "hitchcock_meaning": "palm tree; palm tree of bitterness or oppression",
  "source_ids": {"easton": "tamar", "smith": "tamar", "isbe": "tamar"},
  "key_refs": ["Genesis 38:6", "Matthew 1:3", "2 Samuel 13:1", "2 Samuel 14:27"]
},
"tamarisk": {
  "term": "Tamarisk",
  "category": "concepts",
  "intro": "<p>The tamarisk (Hebrew <em>eshel</em>) was a shrub or small tree of the genus Tamarix — feathery-branched, salt-tolerant, and adapted to the arid conditions of the Negev and Sinai. It provided the shade of a sacred grove. Abraham planted a tamarisk at Beersheba and called there on the name of the LORD El Olam (Gen. 21:33), marking the site as a place of covenant worship. Saul held court \"under the tamarisk tree on the hill at Gibeah\" (1 Sam. 22:6), a detail that evokes both the dignity and the rootlessness of his kingship. His bones and those of his sons, retrieved from Beth-shan, were buried \"under the tamarisk tree at Jabesh\" (1 Sam. 31:13). The KJV translates <em>eshel</em> variously as \"grove\" and \"tree.\"</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "tamarisk", "smith": "tamarisk"},
  "key_refs": ["Genesis 21:33", "1 Samuel 22:6", "1 Samuel 31:13"]
},
"tammuz": {
  "term": "Tammuz",
  "category": "concepts",
  "intro": "<p>Tammuz was a Sumerian and Babylonian deity of vegetation and the grain harvest, the divine shepherd and consort of Inanna/Ishtar, whose annual death and descent to the underworld explained the withering of crops in summer. Mourning rites for Tammuz — women weeping at his death — were performed annually. In Ezekiel's throne-vision of the abominations in the Jerusalem temple, he saw \"women weeping for Tammuz\" at the north gate of the inner court (Ezek. 8:14) — a pagan ritual that had infiltrated the worship of the LORD. This is the only direct biblical mention of the deity. The fourth month of the Hebrew calendar (approximately June–July) bears the name Tammuz, adopted from Babylonia during the exile and retained in the Jewish calendar to the present.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "tammuz", "isbe": "tammuz"},
  "key_refs": ["Ezekiel 8:14"]
},
"tanhumeth": {
  "term": "Tanhumeth",
  "category": "people",
  "intro": "<p>Tanhumeth the Netophathite was the father of Seraiah, one of the Judean military captains who came to Gedaliah at Mizpah after the Babylonian destruction of Jerusalem (2 Kgs. 25:23; Jer. 40:8). These captains pledged their allegiance to Gedaliah as the Babylonian-appointed governor and were told to settle throughout the land and serve the king of Babylon. The name Netophathite indicates origin from Netophah, a village near Bethlehem. Tanhumeth himself plays no narrative role; he is known only as the father of Seraiah.</p>",
  "hitchcock_meaning": "consolation; repentance",
  "source_ids": {"easton": "tanhumeth"},
  "key_refs": ["2 Kings 25:23", "Jeremiah 40:8"]
},
"tanis": {
  "term": "Tanis",
  "category": "places",
  "intro": "<p>Tanis (Egyptian <em>Djanet</em>; Hebrew <em>Zoan</em>) was a major Egyptian city in the northeastern Nile Delta, capital of Egypt during the 21st and 22nd Dynasties (c. 1070–716 B.C.). In Scripture it appears as Zoan, the site of Moses' miraculous signs: \"He wrought his signs in Egypt and his wonders in the field of Zoan\" (Ps. 78:12, 43). Isaiah includes \"the princes of Zoan\" among the foolish counselors whose wisdom has failed Pharaoh (Isa. 19:11, 13; 30:4). Numbers 13:22 notes that Zoan/Tanis was built seven years after Hebron, placing it among the oldest inhabited cities. The modern site of San el-Hagar in the Egyptian Delta preserves the ruins of ancient Tanis.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "tanis", "smith": "tanis"},
  "key_refs": ["Psalms 78:12", "Isaiah 19:11", "Numbers 13:22"]
},
"tappuah": {
  "term": "Tappuah",
  "category": "places",
  "intro": "<p>Tappuah (meaning \"apple\" or \"height\") was a Canaanite royal city whose king Joshua defeated (Josh. 12:17). It appears in the tribal boundary descriptions as a town of the Ephraim-Manasseh border region (Josh. 16:8; 17:7–8): the land of Tappuah belonged to Manasseh, but the city itself fell within Ephraim's portion. A separate Tappuah is listed among the cities of the Judean Shephelah (Josh. 15:34). The place name also appears in 2 Kings 15:16, where Menahem's brutal campaign targeted \"Tiphsah\" — some manuscripts read Tappuah. The Beth-tappuah of Joshua 15:53 is yet another associated place in Judah.</p>",
  "hitchcock_meaning": "apple; swelling",
  "source_ids": {"easton": "tappuah", "smith": "tappuah"},
  "key_refs": ["Joshua 12:17", "Joshua 16:8", "Joshua 17:8"]
},
"tarah": {
  "term": "Tarah",
  "category": "places",
  "intro": "<p>Tarah (also Terah) was an Israelite wilderness campsite listed in the Exodus itinerary of Numbers 33:27–28, between Tahath and Mithcah. It should not be confused with Terah the patriarch, father of Abraham. The site has not been identified; most of the encampments in this section of Numbers 33 remain unlocated. It represents one of the many stages in the forty-year journey through the Sinai wilderness and appears only in this travel record.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "tarah"},
  "key_refs": ["Numbers 33:27"]
},
"tares": {
  "term": "Tares",
  "category": "concepts",
  "intro": "<p>Tares (Greek <em>zizania</em>) are weeds identified by most scholars as darnel (<em>Lolium temulentum</em>), a ryegrass that in its early stages is virtually indistinguishable from wheat. In Jesus' Parable of the Tares (Matt. 13:24–30, 36–43), an enemy sows tares among a man's wheat while he sleeps. The householder refuses to pull the tares before harvest lest the wheat be uprooted with them; at harvest the reapers will separate them — burning the tares and storing the wheat. Jesus interprets the parable himself: the field is the world, the wheat the sons of the kingdom, the tares the sons of the evil one, the harvest the end of the age, and the reapers the angels (Matt. 13:36–43). The parable addresses the mystery of evil coexisting with the righteous during the present age of the kingdom.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "tares", "isbe": "tares"},
  "key_refs": ["Matthew 13:25", "Matthew 13:38", "Matthew 13:40"]
},
"target": {
  "term": "Target",
  "category": "concepts",
  "intro": "<p>\"Target\" in the KJV translates the Hebrew <em>kidon</em> (a javelin or spear) in 1 Samuel 17:6, describing the weapon Goliath carried between his shoulders — \"he had a target of brass between his shoulders\" (KJV) — rather than a circular aiming mark. Modern translations render this as \"javelin\" or \"spear.\" The Hebrew <em>tzinnah</em>, sometimes translated \"target\" in older versions (e.g., Job 16:12), refers to the large body-shield rather than a target for archery. In Lamentations 3:12 the prophet feels as if God has set him as a mark or target for his arrows, expressing profound suffering under divine judgment.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "target"},
  "key_refs": ["1 Samuel 17:6", "Lamentations 3:12"]
},
"tarshish": {
  "term": "Tarshish",
  "category": "places",
  "intro": "<p>Tarshish was a distant maritime trading destination famous for its wealth, reachable only by the largest ocean-going vessels (\"ships of Tarshish\"). Most scholars identify it with Tartessus in southwestern Spain, though Sardinia and other western Mediterranean sites have been proposed. Solomon and Hiram of Tyre sent a joint fleet to Tarshish every three years, returning with gold, silver, ivory, apes, and peacocks (1 Kgs. 10:22; 2 Chr. 9:21). Jonah booked passage to Tarshish — the most distant western port — in his flight from God's commission (Jon. 1:3). Isaiah's oracle against Tyre laments the destruction of the \"ships of Tarshish\" (Isa. 23:1, 14) and his eschatological vision includes Tarshish among nations that will declare God's glory and bring the dispersed of Israel home (Isa. 66:19).</p>",
  "hitchcock_meaning": "examination of the marble",
  "source_ids": {"easton": "tarshish", "smith": "tarshish", "isbe": "tarshish"},
  "key_refs": ["1 Kings 10:22", "Jonah 1:3", "Isaiah 23:1", "Isaiah 66:19"]
},
"tarsus": {
  "term": "Tarsus",
  "category": "places",
  "intro": "<p>Tarsus was the capital city of the Roman province of Cilicia in southern Asia Minor (modern south-central Turkey), situated on the Cydnus River about 10 miles from the Mediterranean. It was a prosperous commercial city with a distinguished university tradition, renowned for its Stoic philosophers, and a free city under Roman rule. Paul the apostle was born in Tarsus (Acts 9:11; 21:39; 22:3) and later described it as \"no mean city\" — a city of no small distinction. Paul spent time in Tarsus between his conversion and his call to Antioch (Acts 9:30; 11:25–26). The city's Hellenistic and Roman cultural environment contributed substantially to Paul's bilingual, bicultural background as a diaspora Jew equally at home in Greek and Hebrew worlds.</p>",
  "hitchcock_meaning": "winged; feathered",
  "source_ids": {"easton": "tarsus", "smith": "tarsus", "isbe": "tarsus"},
  "key_refs": ["Acts 9:11", "Acts 21:39", "Acts 22:3"]
},
"tartak": {
  "term": "Tartak",
  "category": "concepts",
  "intro": "<p>Tartak was a deity worshipped by the Avvites, one of the foreign peoples the Assyrians settled in Samaria after deporting the northern Israelites (2 Kgs. 17:31). The Avvites made idols of Nibhaz and Tartak, worshipping them alongside the gods they had brought from their homeland. Nothing further is known of Tartak from biblical or extra-biblical sources; the name and origin remain obscure, though the pairing with Nibhaz suggests a Mesopotamian or Syrian provenance. The syncretistic religion of the Samaritans that resulted — mixing Yahweh worship with paganism — was condemned by the biblical writers (2 Kgs. 17:33).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "tartak"},
  "key_refs": ["2 Kings 17:31"]
},
"tartan": {
  "term": "Tartan",
  "category": "people",
  "intro": "<p>Tartan was the title (not a personal name) of the commander-in-chief of the Assyrian army, second only to the king in the military hierarchy. The Assyrian word <em>turtanu</em> is confirmed in cuneiform records. Two biblical accounts mention a Tartan: (1) The Tartan of Sargon II came against the Philistine city of Ashdod c. 711 B.C. (Isa. 20:1), the occasion for Isaiah's three-year symbolic act of going naked and barefoot as a sign of coming Assyrian captivity for Egypt and Cush. (2) Sennacherib sent his Tartan along with the Rabshakeh and Rabsaris with a large army to demand Jerusalem's surrender from Hezekiah (2 Kgs. 18:17).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "tartan", "isbe": "tartan"},
  "key_refs": ["Isaiah 20:1", "2 Kings 18:17"]
},
"tatnai": {
  "term": "Tatnai",
  "category": "people",
  "intro": "<p>Tatnai (or Tattenai) was the Persian governor of the satrapy \"Beyond the River\" (Trans-Euphrates) during the early reign of Darius I Hystaspes. When he inspected the Jewish rebuilding of the Jerusalem temple, he wrote to Darius asking whether the project had royal authorization (Ezra 5:3–6). Darius searched the royal archives, found Cyrus's original decree authorizing the rebuilding (Ezra 6:3–5), and ordered Tatnai not only to stop hindering the work but to supply building materials and animals for sacrifice from the royal revenues (Ezra 6:7–12). Tatnai complied (Ezra 6:13). A cuneiform text from 502 B.C. mentions a governor named Tattannu in this region, providing extra-biblical corroboration of the name.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "tatnai", "isbe": "tatnai"},
  "key_refs": ["Ezra 5:3", "Ezra 6:6", "Ezra 6:13"]
},
"taverns-the-three": {
  "term": "Taverns, The Three",
  "category": "places",
  "intro": "<p>The Three Taverns (Latin <em>Tres Tabernae</em>, \"three shops\") was a station on the Via Appia (Appian Way) approximately 33 miles south of Rome, near modern Cisterna di Latina. It was a well-known road stop mentioned by Cicero in his letters. When Paul was being transported as a prisoner from Puteoli to Rome, a delegation of Roman Christians traveled out to meet him — some as far as the Forum of Appius (43 miles from Rome), others at the Three Taverns (Acts 28:15). The sight of these brothers caused Paul to give thanks to God and take courage for the ordeal ahead. The Three Taverns thus marks the point at which Paul, the prisoner, first received Christian fellowship on Roman soil.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "taverns-the-three"},
  "key_refs": ["Acts 28:15"]
},
"taxes": {
  "term": "Taxes",
  "category": "concepts",
  "intro": "<p>Taxation in Israel took the form of tithes and sanctuary dues under the theocracy, supplemented by civil levies under the monarchy. The annual half-shekel temple tax was levied for the maintenance of the sanctuary (Ex. 30:11–16; Matt. 17:24–27). Solomon imposed forced labor and district taxation (1 Kgs. 4:7; 12:4), burdens that led to the northern revolt after his death. Roman taxation — including the poll tax (tributum capitis) and customs duties — was the context for the Pharisees' question to Jesus: \"Is it lawful to give tribute to Caesar, or not?\" Jesus' reply — \"Render to Caesar what is Caesar's, and to God what is God's\" (Matt. 22:17–21) — established the principle of dual obligation to civil and divine authority. Paul commands that taxes be paid as a duty owed to governing authorities who are God's servants (Rom. 13:6–7).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "taxes", "isbe": "taxes"},
  "key_refs": ["Matthew 22:17", "Matthew 22:21", "Romans 13:6"]
},
"taxing": {
  "term": "Taxing",
  "category": "concepts",
  "intro": "<p>\"Taxing\" in the KJV (Luke 2:1–2; Acts 5:37) translates the Greek <em>apographe</em>, a census-enrollment for purposes of taxation. Augustus's decree of a worldwide enrollment (Luke 2:1) places the birth of Jesus in the context of Roman imperial administration — providing the occasion for Mary and Joseph's journey from Nazareth to Bethlehem, fulfilling Micah's prophecy (Mic. 5:2). The enrollment is associated with Quirinius as governor of Syria (Luke 2:2), which has generated significant historical debate about the chronology of Roman census-taking in Judea. The taxing of Acts 5:37 refers to the census of 6 A.D. (confirmed in Josephus) that provoked Judas of Galilee's revolt and the founding of the Zealot movement.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "taxing", "isbe": "taxing"},
  "key_refs": ["Luke 2:1", "Luke 2:2", "Acts 5:37"]
},
"tebeth": {
  "term": "Tebeth",
  "category": "concepts",
  "intro": "<p>Tebeth (Hebrew <em>Tevet</em>) was the tenth month of the Hebrew religious calendar (December–January), corresponding roughly to the Babylonian month <em>Tebetu</em>. It is mentioned by name once in Scripture in connection with Esther: \"So Esther was taken unto king Ahasuerus into his house royal in the tenth month, which is the month Tebeth\" (Esth. 2:16). The tenth of Tebeth was also the date on which the Babylonian siege of Jerusalem began (2 Kgs. 25:1; Jer. 39:1; Ezek. 24:1), and it is still observed as a fast day in Judaism. The modern Jewish calendar retains Tevet as its tenth month.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "tebeth"},
  "key_refs": ["Esther 2:16", "2 Kings 25:1", "Ezekiel 24:1"]
},
"teil-tree": {
  "term": "Teil Tree",
  "category": "concepts",
  "intro": "<p>The teil tree (KJV) translates the Hebrew <em>elah</em>, the terebinth (<em>Pistacia palaestina</em> or <em>Pistacia atlantica</em>), a large, long-lived deciduous tree of the Palestinian landscape. Isaiah uses it in his famous stump metaphor: \"But yet in it shall be a tenth, and it shall return, and shall be eaten: as a teil tree, and as an oak, whose substance is in them, when they cast their leaves: so the holy seed shall be the substance thereof\" (Isa. 6:13 KJV) — the surviving stump retaining life and regenerative capacity. The terebinth was a landmark tree for the patriarchs (Gen. 35:4; Judg. 6:11) and is the same tree under which Absalom's hair was caught (2 Sam. 18:9). Modern translations render <em>elah</em> as \"terebinth\" throughout.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "teil-tree"},
  "key_refs": ["Isaiah 6:13", "Judges 6:11", "2 Samuel 18:9"]
},
"tekel": {
  "term": "Tekel",
  "category": "concepts",
  "intro": "<p>Tekel (Aramaic תְּקֵל) is the second word of the mysterious inscription \"MENE, MENE, TEKEL, UPHARSIN\" written by a disembodied hand on the palace wall during Belshazzar's feast (Dan. 5:25). Daniel interpreted it as the Aramaic passive participle <em>teqal</em>, \"weighed\": \"You have been weighed in the balances and found wanting\" (Dan. 5:27). The imagery draws on the ancient Near Eastern concept of divine judgment as the weighing of a person's deeds — found also in Egyptian mortuary texts (the weighing of the heart against Ma'at's feather) and in other Mesopotamian traditions. The verdict pronounced Belshazzar's life and reign deficient in the scales of divine justice. He was killed that same night (Dan. 5:30).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "tekel", "isbe": "tekel"},
  "key_refs": ["Daniel 5:25", "Daniel 5:27"]
},
"tekoa-tekoah": {
  "term": "Tekoa, Tekoah",
  "category": "places",
  "intro": "<p>Tekoa (also Tekoah) was a town in the hill country of Judah approximately 6 miles south of Bethlehem and 12 miles south of Jerusalem, overlooking the Judean wilderness toward the Dead Sea. The prophet Amos was a herdsman and dresser of sycamore figs from Tekoa (Amos 1:1), making it the hometown of one of the earliest writing prophets. Joab engaged a \"wise woman\" from Tekoa to bring a parable to King David to prepare the way for Absalom's return (2 Sam. 14:2). Rehoboam fortified Tekoa as a defensive position (2 Chr. 11:6). Jeremiah commanded the blowing of the trumpet at Tekoa as a warning signal of northern invasion (Jer. 6:1). The men of Tekoa helped repair Jerusalem's wall under Nehemiah (Neh. 3:5, 27).</p>",
  "hitchcock_meaning": "trumpet; that is confirmed",
  "source_ids": {"easton": "tekoa-tekoah", "smith": "tekoa", "isbe": "tekoa"},
  "key_refs": ["Amos 1:1", "2 Samuel 14:2", "Jeremiah 6:1"]
},
"tel-abib": {
  "term": "Tel-abib",
  "category": "places",
  "intro": "<p>Tel-abib (Hebrew for \"mound of the flood\" or \"mound of grain\"; cf. Akkadian <em>til abubi</em>, \"mound of the deluge\") was a settlement of Jewish exiles beside the Chebar canal in Babylonia. Ezekiel went there after his inaugural vision of the divine chariot to minister to the captive community: \"Then I came to them of the captivity at Tel-abib, that dwelt by the river of Chebar, and I sat where they sat, and remained there astonished among them seven days\" (Ezek. 3:15). The place name was revived in 1909 when the first modern Hebrew city was established near Jaffa and named Tel Aviv (\"Hill of Spring\"), drawing on Ezekiel's text.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "tel-abib"},
  "key_refs": ["Ezekiel 3:15"]
},
"tel-haresha": {
  "term": "Tel-haresha",
  "category": "places",
  "intro": "<p>Tel-haresha (meaning \"mound of the craftsman\" or \"hill of the artificer\") was one of several Babylonian settlements from which Jewish exiles attempted to return to Judah but could not prove their Israelite ancestry (Ezra 2:59; Neh. 7:61). These returnees from Tel-haresha, Tel-melah, and Cherub sought to establish their identity in the restored community but lacked genealogical documentation — a significant concern in the post-exilic community where lineage determined priestly service and land inheritance. Their inclusion despite uncertainty reflects the breadth of Zerubbabel's restoration gathering.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "tel-haresha"},
  "key_refs": ["Ezra 2:59", "Nehemiah 7:61"]
},
"tel-melah": {
  "term": "Tel-melah",
  "category": "places",
  "intro": "<p>Tel-melah (meaning \"mound of salt\" or \"salt hill\") was a Babylonian settlement from which Jewish exiles returned to Judah who could not verify their Israelite lineage (Ezra 2:59; Neh. 7:61). It is listed alongside Tel-haresha and Cherub. The \"salt mound\" designation may indicate a location near the salt flats or saline marshlands of Babylonia. Like the other unverifiable returnees, these families were permitted to join the restoration community despite their uncertain pedigree, pending priestly inquiry through the Urim and Thummim (Ezra 2:63).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "tel-melah"},
  "key_refs": ["Ezra 2:59", "Nehemiah 7:61"]
},
"telaim": {
  "term": "Telaim",
  "category": "places",
  "intro": "<p>Telaim was the site where Saul mustered his army for the campaign against the Amalekites at Samuel's command (1 Sam. 15:4), assembling 200,000 footmen from Israel and 10,000 men of Judah. The battle that followed resulted in the capture of Agag and the partial sparing of the best livestock — Saul's disobedience that led Samuel to pronounce his rejection as king (1 Sam. 15:10–23). Telaim is commonly identified with Telem, a city in the southern hill country of Judah (Josh. 15:24), though the identification is not certain.</p>",
  "hitchcock_meaning": "lambs; their shadows",
  "source_ids": {"easton": "telaim"},
  "key_refs": ["1 Samuel 15:4"]
},
"telassar": {
  "term": "Telassar",
  "category": "places",
  "intro": "<p>Telassar was a territory inhabited by \"the children of Eden\" (2 Kgs. 19:12; Isa. 37:12), cited by Sennacherib's emissary Rabshakeh as an example of regions whose gods could not deliver them from Assyrian conquest: \"Where is the king of Hamath, and the king of Arpad, and the king of the city of Sepharvaim, of Hena, and Ivah?\" The \"children of Eden\" in Telassar are likely identified with the Aramaic state Bit-Adini on the middle Euphrates, known from Assyrian texts as a kingdom subdued by Shalmaneser III. The reference underscores the Assyrian claim that no god had successfully protected its territory — a claim rebutted by the deliverance of Jerusalem (2 Kgs. 19:35).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "telassar"},
  "key_refs": ["2 Kings 19:12", "Isaiah 37:12"]
},
"telem": {
  "term": "Telem",
  "category": "places",
  "intro": "<p>Telem was (1) a city in the extreme south of Judah, in the Negev region, listed among the cities of the tribe of Judah (Josh. 15:24); and (2) a Levitical gatekeeper in the post-exilic community who was among those who had taken foreign wives and were required to send them away at Ezra's insistence (Ezra 10:24). The city Telem may be the same as Telaim, where Saul mustered his forces against the Amalekites (1 Sam. 15:4).</p>",
  "hitchcock_meaning": "their shadow; their dew",
  "source_ids": {"easton": "telem"},
  "key_refs": ["Joshua 15:24", "Ezra 10:24"]
},
"tema": {
  "term": "Tema",
  "category": "places",
  "intro": "<p>Tema was a son of Ishmael (Gen. 25:15; 1 Chr. 1:30) and the North Arabian oasis settlement that bore his name — modern Tayma in northwestern Saudi Arabia. The Tema oasis sat astride the major incense and spice trade routes between southern Arabia and the Fertile Crescent. Job alludes to the caravans of Tema looking for water in the scorching desert (Job 6:19). Isaiah's oracle concerning Arabia (Isa. 21:13–14) calls on the inhabitants of Tema to bring water to the thirsty refugee. Cuneiform texts confirm that the Babylonian king Nabonidus resided at Tema for approximately ten years (c. 553–543 B.C.), during which Belshazzar governed Babylon — the setting of Daniel 5.</p>",
  "hitchcock_meaning": "admiration; perfection; consummation",
  "source_ids": {"easton": "tema", "smith": "tema"},
  "key_refs": ["Genesis 25:15", "Job 6:19", "Isaiah 21:14"]
},
"teman": {
  "term": "Teman",
  "category": "places",
  "intro": "<p>Teman (meaning \"south\" or \"right hand\") was a district and clan of Edom, descended from Teman the grandson of Esau (Gen. 36:11, 15; 1 Chr. 1:36). It gave its name to the southern region of Edom and became used synonymously with Edom itself in prophetic literature. Teman was proverbially famous for its wisdom (Jer. 49:7; Bar. 3:22–23). Prophetic judgment fell specifically on Teman: Amos (1:12) pronounces fire on it, Obadiah (9) declares its warriors dismayed, Jeremiah (49:20) announces its destruction, and Habakkuk (3:3) recalls God coming \"from Teman\" in the theophanic march of judgment. Job's friend Eliphaz is identified as \"the Temanite\" (Job 2:11), associated with this region's wisdom tradition.</p>",
  "hitchcock_meaning": "on the right hand; the south",
  "source_ids": {"easton": "teman", "smith": "teman", "isbe": "teman"},
  "key_refs": ["Genesis 36:11", "Jeremiah 49:7", "Obadiah 9", "Habakkuk 3:3"]
},
"temanite": {
  "term": "Temanite",
  "category": "people",
  "intro": "<p>A Temanite was an inhabitant of Teman, the southern district of Edom noted for its wisdom tradition. The term is most significant as the designation of Eliphaz the Temanite, the first and most prominent of Job's three comforters (Job 2:11; 4:1; 15:1; 22:1; 42:7, 9). Eliphaz appeals to personal vision (Job 4:12–21), the observation of natural order, and the principle of retributive justice to argue that Job must have sinned. God ultimately rebukes him along with Bildad and Zophar for not speaking \"what is right\" about God (Job 42:7–8) and requires the three to offer burnt offerings and have Job intercede for them. Several early Edomite kings are identified as Temanites (Gen. 36:34), confirming Teman as a place of political significance.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "temanite"},
  "key_refs": ["Job 2:11", "Job 4:1", "Job 42:7"]
},
"temeni": {
  "term": "Temeni",
  "category": "people",
  "intro": "<p>Temeni was a son of Ashhur, the posthumous son of Hezron who founded Tekoa, listed in the genealogy of the tribe of Judah (1 Chr. 4:6). He is one of the children born to Ashhur's wife Naarah. Beyond his place in the genealogical record, Temeni plays no narrative role in Scripture. The name may mean \"southerner\" or relate to Teman (south).</p>",
  "hitchcock_meaning": "south wind; on the right hand",
  "source_ids": {"easton": "temeni"},
  "key_refs": ["1 Chronicles 4:6"]
},
"temple": {
  "term": "Temple",
  "category": "concepts",
  "intro": "<p>The Temple (Hebrew <em>hekal</em>, \"great house\"; <em>bayit</em>, \"house\") was the permanent sanctuary in Jerusalem that replaced the tabernacle as the dwelling of God's presence among Israel. Three temples stood on Mount Moriah: Solomon's (completed c. 959 B.C., destroyed 586 B.C.), the Second Temple of Zerubbabel (completed 516 B.C., expanded under Herod and destroyed A.D. 70), and the eschatological temple of Ezekiel's vision (Ezek. 40–48). The temple was the center of Israel's sacrificial worship, annual pilgrimage feasts, and priestly service — the architectural expression of the covenant relationship between God and his people. The New Testament interprets the temple typologically in multiple registers: Jesus is the true temple (John 2:19–21; Rev. 21:22), believers collectively are God's temple indwelt by the Spirit (1 Cor. 3:16; 2 Cor. 6:16; Eph. 2:21), and the heavenly sanctuary is the archetype of which the earthly was a copy (Heb. 8:2; 9:11).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "temple", "smith": "temple", "isbe": "temple"},
  "key_refs": ["1 Kings 6:1", "John 2:19", "1 Corinthians 3:16", "Hebrews 9:11"]
},
"temple-herods": {
  "term": "Temple, Herod's",
  "category": "concepts",
  "intro": "<p>Herod the Great's temple was a massive renovation and expansion of Zerubbabel's Second Temple, begun in 20/19 B.C. and still under construction in Jesus' day (John 2:20: \"forty-six years has this temple been under construction\"). Herod doubled the size of the Temple Mount by constructing enormous retaining walls and vaulted substructures — the Western Wall (\"Wailing Wall\") survives today. On this platform stood the gleaming white marble and gold-clad sanctuary, the Court of the Gentiles, the Court of Women, the Court of Israel, and the inner sanctuary. Jesus taught throughout this complex (John 7–8; Matt. 21), performed his cleansing of the outer court (John 2:14–16; Matt. 21:12–13), and predicted its total destruction: \"There will not be left here one stone upon another that will not be thrown down\" (Matt. 24:2). Roman armies under Titus fulfilled this prophecy in A.D. 70.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "temple-herods", "smith": "temple", "isbe": "temple-herod"},
  "key_refs": ["John 2:16", "John 2:20", "Matthew 24:2", "Luke 21:6"]
},
"temple-solomons": {
  "term": "Temple, Solomon's",
  "category": "concepts",
  "intro": "<p>Solomon's Temple (<em>Bet Yahweh</em>, \"House of the LORD\") was built on Mount Moriah in Jerusalem and completed c. 959 B.C. (1 Kgs. 6:38; 2 Chr. 3–5). The interior measured 60 × 20 × 30 cubits, comprising the vestibule (<em>ulam</em>), the Holy Place (<em>hekal</em>), and the Holy of Holies (<em>debir</em>) — the same three-part structure as the tabernacle but on a larger scale. Cedar panels lined the interior, the walls and floors were overlaid with gold, and massive carved cherubim flanked the ark in the inner sanctuary. The furnishings included the Molten Sea, ten bronze lavers, ten golden lampstands, and the altar of incense. At its dedication, the divine glory so filled the temple that the priests could not stand to minister (1 Kgs. 8:10–11). Nebuchadnezzar plundered its treasuries and burned the temple in 586 B.C. (2 Kgs. 25:8–17).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "temple-solomons", "smith": "temple", "isbe": "temple-solomon"},
  "key_refs": ["1 Kings 6:1", "1 Kings 8:10", "2 Chronicles 3:1", "2 Kings 25:9"]
},
"temple-the-second": {
  "term": "Temple, the Second",
  "category": "concepts",
  "intro": "<p>The Second Temple was built by the Jewish exiles who returned from Babylon under Zerubbabel the governor and Jeshua the high priest, completed in 516 B.C. — seventy years after the first temple's destruction (Ezra 6:15). Cyrus of Persia had decreed its reconstruction (Ezra 1:1–4; 6:3–5), and foundation-laying began in 536 B.C. but was halted by Samaritan opposition (Ezra 4) until the prophets Haggai and Zechariah renewed the community's resolve in 520 B.C. (Hag. 1:1; Zech. 1:1). Haggai encouraged the returned community by promising that the latter glory of this house would surpass the former (Hag. 2:9). The Second Temple stood nearly 500 years before Herod the Great began its wholesale renovation in 20/19 B.C.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "temple-the-second", "isbe": "temple-second"},
  "key_refs": ["Ezra 6:15", "Haggai 2:9", "Zechariah 4:9"]
},
"temptation": {
  "term": "Temptation",
  "category": "concepts",
  "intro": "<p>Temptation (Hebrew <em>nisah</em>, \"to test\"; Greek <em>peirasmos</em>, \"trial, temptation\") in Scripture encompasses both divine testing — designed to prove and develop faith — and satanic or fleshly enticement toward sin. God tested Abraham by commanding the sacrifice of Isaac (Gen. 22:1), a trial that demonstrated faith rather than induced sin. Israel was tested in the wilderness (Deut. 8:2–3). Satan tempted Jesus in the wilderness with three specific enticements after forty days of fasting (Matt. 4:1–11; Luke 4:1–13), each countered by Jesus with Deuteronomy. Jesus taught his disciples to pray for deliverance from temptation (Matt. 6:13; Luke 11:4). James draws the crucial distinction: God does not tempt anyone to sin; each person is tempted by his own desire (Jas. 1:13–14). God promises that believers will not be tempted beyond their ability and will always be provided a way of escape (1 Cor. 10:13); and Christ, having been tempted in all respects as we are yet without sin, is able to sympathize and help (Heb. 4:15).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "temptation", "smith": "temptation", "isbe": "temptation"},
  "key_refs": ["Matthew 4:1", "James 1:13", "1 Corinthians 10:13", "Hebrews 4:15"]
},
"tent": {
  "term": "Tent",
  "category": "concepts",
  "intro": "<p>The tent (<em>ohel</em>) was the primary dwelling of nomadic and semi-nomadic peoples in the biblical world and the paradigm for the divine dwelling in Israel. The patriarchs — Abraham, Isaac, and Jacob — lived in tents (Gen. 12:8; 13:3; 18:1–2), moving them as they followed God's direction. The Israelites dwelt in tents throughout the forty wilderness years, with the tabernacle (<em>ohel mo'ed</em>, \"tent of meeting\") at the center of the camp. \"Tent\" becomes a rich theological metaphor: to \"pitch one's tent\" is to settle (Gen. 26:25), to \"spread one's tent\" over another is to protect (Rev. 7:15). Paul describes the mortal body as an earthly tent that will be dissolved and replaced by \"a building from God, a house not made with hands, eternal in the heavens\" (2 Cor. 5:1). John 1:14 — the Word \"tabernacled\" (<em>eskenosen</em>) among us — echoes the tent of meeting as the paradigm of divine presence.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "tent", "isbe": "tent"},
  "key_refs": ["Genesis 18:1", "Exodus 33:7", "2 Corinthians 5:1", "John 1:14"]
},
"tenth-deal": {
  "term": "Tenth Deal",
  "category": "concepts",
  "intro": "<p>A tenth deal (Hebrew <em>issaron</em>, \"a tenth part\") was one-tenth of an ephah — the standard flour measure for many Mosaic offerings. It appears repeatedly in the sacrificial regulations (Ex. 29:40; Lev. 14:10; Num. 28–29) prescribing specific quantities of grain for daily burnt offerings, the Sabbath, new moon, and festival sacrifices. A tenth deal approximated 2.2 liters (roughly half a gallon), a modest but symbolically precise quantity. The specificity of these measurements in the Mosaic law reflects the ordered, proportional character of Israel's worship and its concern for proper calibration of offerings to the LORD.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "tenth-deal"},
  "key_refs": ["Exodus 29:40", "Leviticus 14:10", "Numbers 28:5"]
},
"terah": {
  "term": "Terah",
  "category": "people",
  "intro": "<p>Terah was the father of Abraham (Abram), Nahor, and Haran, and the grandfather of Lot, living in Ur of the Chaldeans (Gen. 11:24–32). He initiated the journey toward Canaan, departing Ur with Abram, Lot, and Sarai, but the family settled at Harran rather than continuing to Canaan. Terah died at Harran at the age of 205. Joshua 24:2 explicitly states that Terah \"served other gods\" in Mesopotamia, underscoring God's sovereign grace in calling Abraham out of an idolatrous family background. In Luke's genealogy, Jesus' lineage is traced through Terah back to Adam (Luke 3:34), placing the Messianic line within this family history of divine rescue from paganism.</p>",
  "hitchcock_meaning": "wild goat; small stone; delay",
  "source_ids": {"easton": "terah", "smith": "terah"},
  "key_refs": ["Genesis 11:26", "Genesis 11:31", "Joshua 24:2", "Luke 3:34"]
},
"teraphim": {
  "term": "Teraphim",
  "category": "concepts",
  "intro": "<p>Teraphim (Hebrew <em>teraphim</em>) were household figurines or idols used for divination and as protective clan deities in the ancient Near East. They appear throughout the OT in varied contexts: Rachel stole her father Laban's teraphim (Gen. 31:19, 34–35), suggesting they had both religious and legal significance (perhaps as tokens of inheritance rights); Micah the Ephraimite kept teraphim in a private shrine (Judg. 17:5; 18:14–20); Michal placed a teraph in David's bed to simulate his form and delay his pursuers (1 Sam. 19:13–16); and Hosea's prophecy anticipates a day when Israel will live \"without ephod, and without teraphim\" (Hos. 3:4). Josiah's reform eliminated teraphim from Judah (2 Kgs. 23:24). Their size varied: small enough to conceal in a camel's saddle (Gen. 31:34) but also human-sized (1 Sam. 19:13–16). Zechariah 10:2 condemns them as speaking falsehood, associating them with divination.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "teraphim", "smith": "teraphim", "isbe": "teraphim"},
  "key_refs": ["Genesis 31:19", "Judges 17:5", "1 Samuel 19:13", "Hosea 3:4"]
},
"terebinth": {
  "term": "Terebinth",
  "category": "concepts",
  "intro": "<p>The terebinth (<em>Pistacia atlantica</em> or <em>Pistacia palaestina</em>; Hebrew <em>elah</em>) is a large, long-lived deciduous tree native to the Mediterranean and Near East, capable of growing to considerable size and living for centuries. Several landmark events in Scripture occur at or near terebinth trees: Jacob buried foreign gods and earrings under the terebinth at Shechem (Gen. 35:4); the angel of the LORD appeared to Gideon under a terebinth at Ophrah (Judg. 6:11); Absalom's hair caught in a terebinth as he fled on his mule, and he was killed there (2 Sam. 18:9–10). Isaiah uses the stump of a felled terebinth (KJV: \"teil tree\") as a symbol for the holy seed that survives judgment (Isa. 6:13). The terebinth was often a landmark and a place of assembly or worship.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "terebinth", "smith": "terebinth", "isbe": "terebinth"},
  "key_refs": ["Genesis 35:4", "Judges 6:11", "2 Samuel 18:9", "Isaiah 6:13"]
},
"teresh": {
  "term": "Teresh",
  "category": "people",
  "intro": "<p>Teresh was one of two royal eunuchs (chamberlains, or \"keepers of the threshold\") who conspired to assassinate the Persian king Ahasuerus (Xerxes I), the other being Bigthan (Esth. 2:21–23; 6:2). Mordecai uncovered the plot and informed Queen Esther, who told the king in Mordecai's name. After investigation, both Teresh and Bigthan were hanged. The record of Mordecai's service was written in the royal chronicles. When Ahasuerus could not sleep and had the chronicles read to him, he heard of Mordecai's loyalty (Esth. 6:1–2), leading directly to Mordecai's public honor and the reversal of Haman's genocidal plot — a providential chain of events hinging on this foiled conspiracy.</p>",
  "hitchcock_meaning": "strict; severe",
  "source_ids": {"easton": "teresh"},
  "key_refs": ["Esther 2:21", "Esther 6:2"]
},
"tertius": {
  "term": "Tertius",
  "category": "people",
  "intro": "<p>Tertius was the trained secretary (amanuensis) who physically wrote the letter to the Romans as Paul dictated it. He inserts his own personal greeting into the letter: \"I Tertius, who wrote this letter, greet you in the Lord\" (Rom. 16:22). The use of a professional scribe for important correspondence was standard practice in the ancient Mediterranean world; Paul also employed secretaries for other letters (1 Cor. 16:21; Gal. 6:11; Col. 4:18; 2 Thess. 3:17; Philem. 19). Tertius is the only amanuensis who identifies himself by name within a Pauline letter, suggesting he was personally known to the Roman congregation, which may indicate he was from Rome or had connections there.</p>",
  "hitchcock_meaning": "third",
  "source_ids": {"easton": "tertius"},
  "key_refs": ["Romans 16:22"]
},
"tertullus": {
  "term": "Tertullus",
  "category": "people",
  "intro": "<p>Tertullus was the professional orator (<em>rhetor</em>) hired by the Jewish high priest Ananias and elders to prosecute Paul before the Roman governor Felix at Caesarea (Acts 24:1–8). His speech follows the conventions of Roman forensic oratory: an elaborate flattery of Felix in the opening (<em>captatio benevolentiae</em>), followed by three accusations — Paul was a public pest, a ringleader of the Nazarene sect, and a defiler of the temple. Paul refuted each charge systematically before Felix (Acts 24:10–21), noting that Tertullus' accusers could not produce witnesses for their claims. The episode illustrates the formal legal procedures of the Roman provincial court and the way early Christian leaders engaged official Roman institutions.</p>",
  "hitchcock_meaning": "a liar; third",
  "source_ids": {"easton": "tertullus", "smith": "tertullus"},
  "key_refs": ["Acts 24:1", "Acts 24:2", "Acts 24:8"]
},
"testament": {
  "term": "Testament",
  "category": "concepts",
  "intro": "<p>\"Testament\" (Greek <em>diatheke</em>; Latin <em>testamentum</em>) translates the Hebrew <em>berith</em> (\"covenant\") in the Septuagint and most NT occurrences. In Greek, <em>diatheke</em> carries the primary meaning of a \"will\" or \"last testament\" — a legally binding disposition of an estate, taking effect at the death of the testator. The author of Hebrews exploits this double meaning: Christ mediates a new covenant (<em>diatheke</em>), and \"where a testament is, there must also of necessity be the death of the testator. For a testament is in force after men are dead, since it has no force at all while the testator lives\" (Heb. 9:16–17 NKJV) — explaining the necessity of Christ's death for the new covenant's ratification. The terms \"Old Testament\" and \"New Testament\" as designations for the two canonical collections derive from Jeremiah's prophecy of a new covenant (Jer. 31:31–34), cited extensively in Hebrews 8–10.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "testament", "isbe": "testament"},
  "key_refs": ["Hebrews 9:15", "Hebrews 9:16", "Jeremiah 31:31"]
},
"testimony": {
  "term": "Testimony",
  "category": "concepts",
  "intro": "<p>Testimony (Hebrew <em>edah</em>, <em>eduth</em>; Greek <em>martyria</em>) in Scripture denotes the divine law as a witness to God's will, as well as human witness to God's acts. The stone tablets of the Decalogue are called \"the testimony\" (Ex. 25:16, 21) because they testify to the terms of the covenant, and the ark is \"the ark of the testimony\" (Ex. 25:22) and the tabernacle \"the tabernacle of testimony\" (Ex. 38:21; Acts 7:44). The psalmist celebrates the testimony of the LORD as \"sure, making wise the simple\" (Ps. 19:7). In the NT, testimony refers to the apostolic proclamation based on eyewitness experience of Jesus' life, death, and resurrection (Luke 24:48; Acts 1:8; 1 John 1:1–3), and the faithful confession of Christ even unto death — the original sense underlying the later term \"martyr\" (Rev. 1:9; 12:11; 20:4).</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "testimony", "isbe": "testimony"},
  "key_refs": ["Exodus 25:16", "Psalms 19:7", "Acts 1:8", "Revelation 12:11"]
},
"testimony-tabernacle-of": {
  "term": "Testimony, Tabernacle of the",
  "category": "concepts",
  "intro": "<p>The Tabernacle of Testimony (Hebrew <em>mishkan ha'eduth</em>; also Tent of Witness or Tabernacle of Witness) was a designation for the wilderness sanctuary understood specifically as the house of the covenant \"testimony\" — the stone tablets of the law deposited in the ark of the testimony within the Holy of Holies (Ex. 38:21; Num. 1:50–53; 9:15; 17:7–8; 18:2). The name emphasizes that the tabernacle was not merely a place of worship but the earthly dwelling built around God's covenant documentation. Stephen uses this designation in his speech before the Sanhedrin: \"Our fathers had the tabernacle of witness in the wilderness\" (Acts 7:44), anchoring the continuity of God's presence with his people from Moses to Solomon. Revelation 15:5 speaks of \"the temple of the tabernacle of the testimony in heaven\" opening for the bowl judgments — the heavenly archetype of the earthly tent.</p>",
  "hitchcock_meaning": None,
  "source_ids": {"easton": "testimony-tabernacle-of", "isbe": "testimony"},
  "key_refs": ["Exodus 38:21", "Numbers 1:50", "Acts 7:44", "Revelation 15:5"]
},
}

wrote = skipped = 0
for slug, data in ARTICLES.items():
    article = {
        "id": slug,
        "term": data["term"],
        "category": data["category"],
        "intro": data["intro"],
        "hitchcock_meaning": data.get("hitchcock_meaning"),
        "source_ids": data.get("source_ids", {}),
        "key_refs": data.get("key_refs", []),
        "sections": []
    }
    if merge_article(slug, article):
        wrote += 1
    else:
        skipped += 1

print(f"BP t1: Taanach -> Testimony, Tabernacle of: wrote {wrote}, skipped {skipped} existing.")
