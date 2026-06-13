#!/usr/bin/env python3
"""BP R1: Raamah → Resurrection of Christ (75 Easton entries)"""
import json, os

OUT_DIR = 'data/biblepedia/articles'
os.makedirs(OUT_DIR, exist_ok=True)

def load_article(slug):
    fp = os.path.join(OUT_DIR, f'{slug}.json')
    if os.path.exists(fp):
        with open(fp) as f:
            return json.load(f)
    return None

def save_article(slug, data):
    fp = os.path.join(OUT_DIR, f'{slug}.json')
    with open(fp, 'w') as f:
        json.dump(data, f, indent=2)

def merge_article(slug, data):
    if load_article(slug) is not None:
        return False
    save_article(slug, data)
    return True

ARTICLES = {
    "raamah": {
        "id": "raamah",
        "term": "Raamah",
        "category": "people",
        "intro": "<p>Raamah was a son of Cush (grandson of Ham) listed in the Table of Nations (Genesis 10:7; 1 Chronicles 1:9), whose descendants settled in the Arabian peninsula. He was the father of Sheba and Dedan, two peoples who figure prominently in Old Testament trade narratives. Ezekiel 27:22 names <em>the merchants of Sheba and Raamah</em> among those who traded with Tyre in spices, precious stones, and gold. The territory of Raamah is generally associated with ancient south Arabia, in the region of modern Yemen, where both Sabaean and Dedanite tribes are historically attested.</p>",
        "sections": [],
        "hitchcock_meaning": "greatness; thunder; some sort of evil",
        "source_ids": {"easton": "raamah"},
        "key_refs": ["Genesis 10:7", "Ezekiel 27:22"]
    },
    "raamiah": {
        "id": "raamiah",
        "term": "Raamiah",
        "category": "people",
        "intro": "<p>Raamiah (meaning <em>thunder from the LORD</em>) was one of the leaders who returned to Judah from the Babylonian exile with Zerubbabel (Nehemiah 7:7). He appears in the parallel list in Ezra 2:2 under the name Reelaiah — a variant spelling common in the transmission of post-exilic names. Raamiah was presumably a leader of one of the returning family groups, though nothing further is recorded about him. His name is one of the relatively rare theophoric names incorporating the root <em>ra'am</em> (thunder) rather than the more common <em>el</em> or <em>yah</em> elements.</p>",
        "sections": [],
        "hitchcock_meaning": "thunder, or evil, from the Lord",
        "source_ids": {"easton": "raamiah"},
        "key_refs": ["Nehemiah 7:7", "Ezra 2:2"]
    },
    "raamses": {
        "id": "raamses",
        "term": "Raamses",
        "category": "places",
        "intro": "<p>Raamses (also spelled Rameses or Ramses) was one of the two store-cities built by the enslaved Israelites for Pharaoh in Egypt (Exodus 1:11), along with Pithom. The city's name preserves that of the great pharaoh Rameses II (c. 1279–1213 BC), who built extensively in the eastern Nile Delta. It is generally identified with the site of ancient Pi-Ramesses, near modern Qantir, which Egyptian archaeology has confirmed as a major royal and administrative center of the Ramesside period. The construction of Raamses is the setting for the intensified oppression of Israel just before Moses's birth, establishing the backdrop for the Exodus narrative.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "raamses", "smith": "raamses"},
        "key_refs": ["Exodus 1:11", "Exodus 12:37"]
    },
    "rabbah": {
        "id": "rabbah",
        "term": "Rabbah",
        "category": "places",
        "intro": "<p>Rabbah (meaning <em>great</em> or <em>populous</em>) was the capital city of the Ammonites, located in the Transjordan highlands approximately 25 miles east of the Jordan River at the site of modern Amman, Jordan. In the Old Testament it is called Rabbah of the Ammonites or Rabbath-ammon (Deuteronomy 3:11; 2 Samuel 12:27). The iron bedstead of the giant Og king of Bashan was displayed there (Deuteronomy 3:11). The city withstood David's siege under Joab while David remained in Jerusalem — a context immortalized by the Bathsheba incident and Uriah's death — before Joab summoned David to lead the final assault (2 Samuel 12:26–29).</p><p>The prophets later directed oracles against Rabbah: Jeremiah 49:2–3, Ezekiel 21:20; 25:5, and Amos 1:14 all announce judgment on Ammon's proud capital. In the Hellenistic period the city was renamed Philadelphia by Ptolemy II Philadelphus and later became part of the Decapolis.</p>",
        "sections": [],
        "hitchcock_meaning": "great; powerful; contentious",
        "source_ids": {"easton": "rabbah", "smith": "rabbah"},
        "key_refs": ["Deuteronomy 3:11", "2 Samuel 12:27", "Jeremiah 49:2"]
    },
    "rabbi": {
        "id": "rabbi",
        "term": "Rabbi",
        "category": "concepts",
        "intro": "<p>Rabbi (from Hebrew <em>rav</em>, great, with first-person suffix: <em>my great one</em> or <em>my master</em>) was an honorific title of address for a teacher of the Jewish law. In the first century it was not yet a formal ordination title (that usage developed after 70 AD) but a respectful form of address for a recognized religious authority. Jesus was addressed as <em>Rabbi</em> repeatedly by his disciples, the crowds, and even by Nicodemus (John 3:2), indicating that he was recognized as a teacher of comparable standing to the Pharisaic sages.</p><p>Jesus himself, however, warned his disciples against seeking the title: <em>But you are not to be called Rabbi, for you have one teacher... and the greatest among you shall be your servant</em> (Matthew 23:8–11). John 1:38 translates <em>Rabbi</em> as <em>Teacher</em> for his Greek audience. <em>Rabboni</em> (my great master) was a more emphatic form used by Mary Magdalene at the resurrection (John 20:16) and by the blind Bartimaeus (Mark 10:51).</p>",
        "sections": [],
        "hitchcock_meaning": "Rabboni, my master",
        "source_ids": {"easton": "rabbi", "isbe": "rabbi"},
        "key_refs": ["Matthew 23:7", "Matthew 23:8", "John 1:38", "John 3:2"]
    },
    "rabboni": {
        "id": "rabboni",
        "term": "Rabboni",
        "category": "concepts",
        "intro": "<p>Rabboni (an intensified form of Rabbi, meaning <em>my great master</em> or <em>my lord</em>) is used twice in the New Testament. The blind beggar Bartimaeus addressed Jesus as <em>Rabboni</em> when calling for healing (Mark 10:51), and Mary Magdalene used the same term when she recognized the risen Jesus at the tomb (John 20:16) — a moment of profound recognition that the Gospel of John preserves in Aramaic alongside the Greek. The intensified form conveys greater personal reverence and intimacy than the simple <em>Rabbi.</em> John translates it as <em>Teacher</em> for his Greek readers.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "rabboni"},
        "key_refs": ["Mark 10:51", "John 20:16"]
    },
    "rabmag": {
        "id": "rabmag",
        "term": "Rabmag",
        "category": "people",
        "intro": "<p>Rabmag was a title, not a personal name, borne by Nergal-sharezer, one of the Babylonian princes who sat at the gate after the fall of Jerusalem in 586 BC (Jeremiah 39:3, 13). The title's meaning is debated: it may derive from the Akkadian <em>rab mugi</em> or a similar official title denoting a high military or court rank. Nergal-sharezer the Rabmag later became king of Babylon (Neriglissar, 560–556 BC), having killed Evil-merodach. He and the other officials were commanded to treat the prophet Jeremiah kindly and to take care of him after the city's fall.</p>",
        "sections": [],
        "hitchcock_meaning": "who overthrows or destroys a multitude",
        "source_ids": {"easton": "rabmag"},
        "key_refs": ["Jeremiah 39:3", "Jeremiah 39:13"]
    },
    "rabsaris": {
        "id": "rabsaris",
        "term": "Rabsaris",
        "category": "people",
        "intro": "<p>Rabsaris was a Babylonian official title (Akkadian <em>rab sha reshi</em>, <em>chief of the head officials</em> or possibly <em>chief eunuch</em>) borne by officials in both the Assyrian and Babylonian courts. The title appears in three biblical contexts: an Assyrian officer sent by Sennacherib along with Tartan and Rabshakeh to demand Jerusalem's surrender from Hezekiah (2 Kings 18:17); a Babylonian prince who sat at the gate of Jerusalem after Nebuchadnezzar's conquest (Jeremiah 39:3); and the court official Ashpenaz, <em>chief of his eunuchs</em> (the same Hebrew term), who oversaw Daniel and his companions in Babylon (Daniel 1:3).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "rabsaris"},
        "key_refs": ["2 Kings 18:17", "Jeremiah 39:3", "Daniel 1:3"]
    },
    "rabshakeh": {
        "id": "rabshakeh",
        "term": "Rabshakeh",
        "category": "people",
        "intro": "<p>Rabshakeh was the title — not a personal name — of the chief spokesman of the Assyrian king Sennacherib, sent with two other officials to demand Jerusalem's surrender from Hezekiah around 701 BC (2 Kings 18:17–37; Isaiah 36). The title likely means <em>chief cupbearer</em> or a senior court official. The Rabshakeh's speech before the walls of Jerusalem is one of the most dramatic episodes in the historical books: delivered in Hebrew so the people on the walls could understand, it combined psychological intimidation, theological argument (claiming the LORD himself had sent Assyria against Judah), and propaganda about Assyrian invincibility.</p><p>Hezekiah's officials pleaded with him to speak in Aramaic to avoid demoralizing the people, but he refused. Isaiah 37 records Hezekiah's prayer and Isaiah's oracle of reassurance — that Sennacherib would hear a rumor and return to his own land and fall by the sword — a prophecy fulfilled when the Assyrian army was struck by the LORD and Sennacherib was later killed by his sons.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "rabshakeh", "smith": "rabshakeh"},
        "key_refs": ["2 Kings 18:17", "2 Kings 18:27", "Isaiah 36:4", "Isaiah 37:33"]
    },
    "raca": {
        "id": "raca",
        "term": "Raca",
        "category": "concepts",
        "intro": "<p>Raca (Aramaic <em>reqa</em>, meaning <em>empty one</em>, <em>worthless</em>, or <em>good-for-nothing</em>) was an Aramaic term of contempt and abuse appearing in the Sermon on the Mount. Jesus cited it as an example of the kind of contemptuous anger that violates the spirit of the commandment against murder: <em>whoever says to his brother, Raca, shall be liable to the council</em> (Matthew 5:22). The term conveys dismissal of another person's worth and intelligence — treating someone as a mental and moral nonentity. By connecting verbal contempt with the prohibition against murder, Jesus internalized and deepened the law's reach to include the attitudes of the heart.</p>",
        "sections": [],
        "hitchcock_meaning": "worthless; good-for-nothing",
        "source_ids": {"easton": "raca", "isbe": "raca"},
        "key_refs": ["Matthew 5:22"]
    },
    "rachab": {
        "id": "rachab",
        "term": "Rachab",
        "category": "people",
        "intro": "<p>Rachab is the Greek New Testament form of the Hebrew name Rahab, used in Matthew 1:5 in the genealogy of Jesus: <em>Salmon begot Boaz by Rachab.</em> This identifies the Rahab of the genealogy with the Rahab of Joshua 2 — the Canaanite woman of Jericho who sheltered the Israelite spies and was saved when Jericho fell. Her inclusion in Matthew's genealogy is theologically significant: she is one of four women (with Tamar, Ruth, and Bathsheba) mentioned in Jesus's lineage, all associated with irregularity or Gentile origin, anticipating the gospel's reach to all nations. Hebrews 11:31 and James 2:25 also commend Rahab's faith.</p>",
        "sections": [],
        "hitchcock_meaning": "same as Rahab",
        "source_ids": {"easton": "rachab"},
        "key_refs": ["Matthew 1:5", "Hebrews 11:31", "James 2:25"]
    },
    "rachal": {
        "id": "rachal",
        "term": "Rachal",
        "category": "places",
        "intro": "<p>Rachal (meaning <em>to whisper</em> or <em>an embalmer</em>) was one of the towns to which David sent portions of the Amalekite spoil after his raid on Ziklag (1 Samuel 30:29). It was among the cities of Judah to which David distributed gifts as part of his ongoing cultivation of supporters in the region before he became king. The exact location is unknown; it appears only in this list. Some manuscripts read <em>Carmel</em> instead of <em>Rachal</em>, suggesting possible textual uncertainty.</p>",
        "sections": [],
        "hitchcock_meaning": "to whisper; an embalmer",
        "source_ids": {"easton": "rachal"},
        "key_refs": ["1 Samuel 30:29"]
    },
    "rachel": {
        "id": "rachel",
        "term": "Rachel",
        "category": "people",
        "intro": "<p>Rachel (meaning <em>ewe</em> or <em>lamb</em>) was the younger daughter of Laban, Jacob's maternal uncle, the beloved wife of the patriarch Jacob, and the mother of Joseph and Benjamin. Jacob fell in love with her at the well in Paddan-aram and agreed to serve Laban seven years for her hand — years that seemed to him only a few days because of his love (Genesis 29:20). Laban's substitution of the older Leah on the wedding night required Jacob to work another seven years for Rachel. The rivalry between the two sisters, and Rachel's barrenness contrasted with Leah's fruitfulness, is one of the sustained narrative tensions of Genesis 29–30.</p><p>Rachel died in childbirth near Bethlehem giving birth to Benjamin, whom she named Ben-oni (son of my sorrow); Jacob renamed him Benjamin (son of my right hand). She was buried on the road to Bethlehem (Genesis 35:19), and her tomb became a landmark. Jeremiah 31:15 — <em>Rachel weeping for her children, refusing to be comforted because they are no more</em> — is quoted in Matthew 2:18 as a prophecy of the massacre of the innocents at Herod's command.</p>",
        "sections": [],
        "hitchcock_meaning": "sheep",
        "source_ids": {"easton": "rachel", "smith": "rachel", "isbe": "rachel"},
        "key_refs": ["Genesis 29:20", "Genesis 35:19", "Jeremiah 31:15", "Matthew 2:18"]
    },
    "raguel": {
        "id": "raguel",
        "term": "Raguel",
        "category": "people",
        "intro": "<p>Raguel (meaning <em>shepherd of God</em> or <em>friend of God</em>) is used in Numbers 10:29 as an alternative name for Reuel, the father-in-law of Moses. The same individual is elsewhere called Jethro (Exodus 3:1; 18:1–2), Reuel (Exodus 2:18), and Hobab (Judges 4:11; Numbers 10:29). The variation in names reflects either multiple designations for the same person in different source traditions, or the distinction between Reuel as the father and Hobab as the son who served as guide for Israel in the wilderness. The name Raguel is the Greek form used in the Septuagint and appears also in the book of Tobit.</p>",
        "sections": [],
        "hitchcock_meaning": "shepherd, or friend of God",
        "source_ids": {"easton": "raguel"},
        "key_refs": ["Numbers 10:29", "Exodus 2:18"]
    },
    "rahab": {
        "id": "rahab",
        "term": "Rahab",
        "category": "people",
        "intro": "<p>Rahab was a Canaanite woman — described in Joshua 2 as a prostitute — who lived in Jericho and sheltered the two Israelite spies sent by Joshua before the conquest. Having heard of the LORD's mighty acts for Israel at the Red Sea and in the Transjordan, she declared her faith: <em>the LORD your God, he is God in the heavens above and on the earth beneath</em> (Joshua 2:11). She protected the spies and negotiated a covenant of protection for herself and her household, marked by a scarlet cord tied in her window. When Jericho fell, Rahab and her family were spared (Joshua 6:25).</p><p>The New Testament holds Rahab as a model of faith and works: Hebrews 11:31 includes her in the roll of faith heroes — <em>by faith Rahab the prostitute did not perish with those who were disobedient</em> — and James 2:25 cites her as proof that faith without works is dead. Matthew 1:5 places her in the messianic genealogy as the mother of Boaz. The scarlet cord she hung in her window has been interpreted in Christian tradition as a type of the blood of Christ.</p>",
        "sections": [],
        "hitchcock_meaning": "proud; quarrelsome (applied to Egypt)",
        "source_ids": {"easton": "rahab", "smith": "rahab", "isbe": "rahab"},
        "key_refs": ["Joshua 2:11", "Joshua 6:25", "Hebrews 11:31", "James 2:25"]
    },
    "raham": {
        "id": "raham",
        "term": "Raham",
        "category": "people",
        "intro": "<p>Raham (meaning <em>compassion</em> or <em>a friend</em>) was a son of Shema and a descendant of Caleb in the genealogy of the tribe of Judah (1 Chronicles 2:44). He is listed as the father of Jorkeam, a Judahite clan or settlement. Beyond this single genealogical notice nothing is known of him. The name <em>raham</em> is related to the Hebrew root for <em>womb</em> and <em>compassion</em> (<em>rachamim</em>), which in its plural form is one of the Bible's richest words for divine mercy.</p>",
        "sections": [],
        "hitchcock_meaning": "compassion; a friend",
        "source_ids": {"easton": "raham"},
        "key_refs": ["1 Chronicles 2:44"]
    },
    "rain": {
        "id": "rain",
        "term": "Rain",
        "category": "concepts",
        "intro": "<p>In the climate of ancient Palestine, rain was the defining factor of agricultural prosperity and survival. The land received nearly all its rainfall between October and April, with the critical <em>early rain</em> (<em>yoreh</em> or <em>moreh</em>) falling in autumn to soften the earth for plowing and seeding, and the <em>latter rain</em> (<em>malqosh</em>) falling in March–April to swell the grain before harvest. Summer was virtually rainless. The promise of rain in its season was thus a fundamental covenant blessing (Deuteronomy 11:14; Leviticus 26:4), while drought was a covenant curse (Deuteronomy 28:22–24).</p><p>Rain functioned as a powerful theological symbol throughout the Bible. Elijah's three-and-a-half years of drought and its dramatic end (1 Kings 17–18) demonstrated the LORD's sovereignty over Baal, the supposed rain-deity of Canaan. Hosea 6:3 compares the LORD's coming to <em>the latter rain that waters the earth.</em> James 5:7 uses the farmer waiting for the early and late rains as a metaphor for patient waiting for Christ's return. Jesus noted that God <em>sends rain on the just and the unjust alike</em> (Matthew 5:45) — rain as common grace.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "rain", "smith": "rain", "isbe": "rain"},
        "key_refs": ["Deuteronomy 11:14", "1 Kings 18:41", "James 5:7", "Matthew 5:45"]
    },
    "rainbow": {
        "id": "rainbow",
        "term": "Rainbow",
        "category": "concepts",
        "intro": "<p>The rainbow (<em>qeshet</em> in Hebrew, the same word as <em>bow</em> for a weapon) was designated by God as the sign of his covenant with Noah and all living creatures after the Flood — a pledge that the waters would never again destroy all flesh (Genesis 9:12–17). The bow's appearance in the clouds was to serve as a visual reminder both for humanity and, as the text frames it, for God himself: <em>when I see the bow in the cloud, I will remember my covenant.</em> The image of a warrior hanging up his weapon in the sky has been read as a symbol of divine restraint — the bow of judgment laid aside.</p><p>The rainbow appears in prophetic and apocalyptic literature as a symbol of divine glory: Ezekiel 1:28 describes the brightness surrounding the divine throne as <em>the appearance of the rainbow in the clouds on a rainy day.</em> Revelation 4:3 depicts a rainbow (<em>iris</em>) around the throne in heaven, and the mighty angel of Revelation 10:1 has a rainbow over his head — images that identify the figure with the creator God of the covenant.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "rainbow", "isbe": "rainbow"},
        "key_refs": ["Genesis 9:13", "Genesis 9:16", "Ezekiel 1:28", "Revelation 4:3"]
    },
    "raisins": {
        "id": "raisins",
        "term": "Raisins",
        "category": "concepts",
        "intro": "<p>Raisins (<em>tsimmuqim</em> in Hebrew, dried grapes pressed into cakes) were a common preserved food of ancient Israel, used as provisions for travel and military campaigns and as gifts. David received a gift of raisins among other provisions when fleeing from Absalom (2 Samuel 16:1–2), and the people of Israel who came to make him king at Hebron brought raisin cakes along with other foods (1 Chronicles 12:40). The context of 2 Samuel 6:19 (David distributing raisin cakes to the entire assembly) and Song of Solomon 2:5 (<em>sustain me with raisin cakes</em>) suggests they were considered strengthening and festive. Hosea 3:1 mentions raisin cakes in a cultic context associated with Canaanite worship.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "raisins"},
        "key_refs": ["2 Samuel 6:19", "1 Chronicles 12:40", "Song of Solomon 2:5"]
    },
    "rakkath": {
        "id": "rakkath",
        "term": "Rakkath",
        "category": "places",
        "intro": "<p>Rakkath (meaning <em>empty</em> or <em>shore of the sea</em>) was a fortified city in the territory of Naphtali listed in Joshua 19:35. It was located on the western shore of the Sea of Galilee. Many scholars identify it with or near the site of Tiberias, built by Herod Antipas around 20 AD, or with the nearby hot springs of Hammath. The Talmud identifies Rakkath with Tiberias. The city appears only in this single tribal allotment list.</p>",
        "sections": [],
        "hitchcock_meaning": "empty; temple of the head",
        "source_ids": {"easton": "rakkath"},
        "key_refs": ["Joshua 19:35"]
    },
    "rakkon": {
        "id": "rakkon",
        "term": "Rakkon",
        "category": "places",
        "intro": "<p>Rakkon (meaning <em>vain</em> or <em>mountain of enjoyment</em>) was a town in the territory of Dan listed in Joshua 19:46, located near the Mediterranean coast and the border with Joppa. The site is generally identified with Tell er-Reqeit on the coast north of Jaffa. Like several other Danite cities on the coastal plain, Rakkon may have been difficult for the tribe to control against Philistine and other pressure — a factor that eventually contributed to Dan's migration to the far north (Judges 18).</p>",
        "sections": [],
        "hitchcock_meaning": "vain; void; mountain of enjoyment",
        "source_ids": {"easton": "rakkon"},
        "key_refs": ["Joshua 19:46"]
    },
    "ram": {
        "id": "ram",
        "term": "Ram",
        "category": "people",
        "intro": "<p>Ram (meaning <em>elevated</em> or <em>sublime</em>) was the name of several individuals in the Old Testament. The most significant was Ram son of Hezron, in the line of Judah through Perez, who appears in the genealogy linking Judah to David (Ruth 4:19; 1 Chronicles 2:9–10) and in Matthew's and Luke's genealogies of Jesus (Matthew 1:3–4; Luke 3:33). He was the grandfather of Nahshon, the prince of the tribe of Judah in the wilderness (Numbers 1:7; 7:12). A second Ram was the firstborn of Jerahmeel (1 Chronicles 2:25), and a third was a kinsman of Elihu who rebuked Job (Job 32:2).</p>",
        "sections": [],
        "hitchcock_meaning": "elevated; sublime",
        "source_ids": {"easton": "ram"},
        "key_refs": ["Ruth 4:19", "1 Chronicles 2:9", "Matthew 1:3"]
    },
    "rama": {
        "id": "rama",
        "term": "Rama",
        "category": "places",
        "intro": "<p>Rama (the Greek and Hebrew form of Ramah, meaning <em>height</em>) is used in Matthew 2:18 in the quotation from Jeremiah 31:15: <em>A voice was heard in Rama, lamentation and bitter weeping — Rachel weeping for her children.</em> Matthew applies this text to the massacre of the infants in Bethlehem by Herod. Ramah was a town in Benjamin, approximately five miles north of Jerusalem, near the border with Ephraim, where the road north passed through the hill country. It became associated with Rachel's lament because tradition held that her tomb was nearby, and because the Benjaminite exiles were assembled there before deportation to Babylon (Jeremiah 40:1) — a historical fulfillment of Jeremiah's weeping Rachel image that Matthew then extends forward to Herod's slaughter.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "rama", "smith": "rama"},
        "key_refs": ["Matthew 2:18", "Jeremiah 31:15", "Jeremiah 40:1"]
    },
    "ramath-of-the-south": {
        "id": "ramath-of-the-south",
        "term": "Ramath of the south",
        "category": "places",
        "intro": "<p>Ramath of the South (Hebrew <em>Ramath-negeb</em>, meaning <em>height of the south</em>) was a city in the southern Negev territory of Judah, listed in Joshua 19:8 as the southernmost city of the tribe of Simeon. It is also called Baalath-beer in the same verse. The town was located in the arid zone south of Beersheba, on the edge of the Negev desert. David sent spoil from his raid on the Amalekites to the elders of this city, among others, as gifts (1 Samuel 30:27), where it is called Ramoth of the south.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ramath-of-the-south"},
        "key_refs": ["Joshua 19:8", "1 Samuel 30:27"]
    },
    "ramath-lehi": {
        "id": "ramath-lehi",
        "term": "Ramath-lehi",
        "category": "places",
        "intro": "<p>Ramath-lehi (meaning <em>height of the jawbone</em> or <em>casting away of the jawbone</em>) was the place in Judah where Samson killed a thousand Philistines with the jawbone of a donkey (Judges 15:17). After the feat, Samson named the place Ramath-lehi to memorialize it. He was then desperately thirsty and cried to God, who opened a spring from the jawbone's hollow — a spring called En-hakkore (fountain of him who called), which remained <em>in Lehi to this day</em> according to the narrator (Judges 15:18–19). The exact location is unknown.</p>",
        "sections": [],
        "hitchcock_meaning": "elevation of the jaw-bone",
        "source_ids": {"easton": "ramath-lehi"},
        "key_refs": ["Judges 15:17", "Judges 15:19"]
    },
    "ramath-mizpeh": {
        "id": "ramath-mizpeh",
        "term": "Ramath-mizpeh",
        "category": "places",
        "intro": "<p>Ramath-mizpeh (meaning <em>height of the watchtower</em>) was a city marking the northern border of the tribe of Gad in Transjordan (Joshua 13:26). It is usually identified with Ramoth-gilead or with a site near Mizpeh of Gilead (Judges 11:29). The place was in the highland of Gilead east of the Jordan, in territory that was perpetually contested between Israel, Aram-Damascus, and Ammon. Its designation as both a <em>height</em> and a <em>watchtower</em> reflects the strategic importance of elevated positions in the Transjordanian hill country.</p>",
        "sections": [],
        "hitchcock_meaning": "elevation of the watch-tower",
        "source_ids": {"easton": "ramath-mizpeh"},
        "key_refs": ["Joshua 13:26"]
    },
    "ramathaim-zophim": {
        "id": "ramathaim-zophim",
        "term": "Ramathaim-zophim",
        "category": "places",
        "intro": "<p>Ramathaim-zophim (meaning <em>the two watch-towers of the Zuphites</em>) was the hometown of Elkanah and his wife Hannah, the parents of Samuel (1 Samuel 1:1). The city is identified with the Ramah of Samuel — the place where Samuel was born, grew up, judged Israel, lived, built an altar, and was buried (1 Samuel 7:17; 8:4; 25:1). The <em>Zophim</em> component connects the location to the Ephraimite family of Zuph, Elkanah's ancestor. The site has been identified with Beit Rima, Rentis, and other locations in the Ephraimite highlands, though no consensus has been reached.</p>",
        "sections": [],
        "hitchcock_meaning": "the two watch-towers",
        "source_ids": {"easton": "ramathaim-zophim"},
        "key_refs": ["1 Samuel 1:1", "1 Samuel 7:17"]
    },
    "ramathite": {
        "id": "ramathite",
        "term": "Ramathite",
        "category": "people",
        "intro": "<p>Ramathite is a gentillic adjective designating a person from Ramah. It appears in 1 Chronicles 27:27, where Shimei the Ramathite is listed as the official in charge of David's vineyards. The designation distinguishes him from other officials in David's administrative lists. Ramah was the name of several towns in ancient Israel; the Ramah from which this official came was likely the Benjamin or Ephraim town, though the specific identification is uncertain.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ramathite"},
        "key_refs": ["1 Chronicles 27:27"]
    },
    "rameses": {
        "id": "rameses",
        "term": "Rameses",
        "category": "places",
        "intro": "<p>Rameses (also Raamses or Ramses) appears in the Old Testament both as the store-city built by Israelite slaves (Exodus 1:11) and as the district from which Israel departed at the Exodus (Genesis 47:11; Exodus 12:37; Numbers 33:3). The name derives from the Egyptian royal name Ramesses (<em>Ra has fashioned him</em>), most famously borne by Ramesses II (c. 1279–1213 BC), who built the eastern Delta capital Pi-Ramesses near modern Qantir. Israel's departure <em>from Rameses to Succoth</em> on the night of the Passover is the first stage of the Exodus route. Genesis 47:11 calls the district where Jacob's family settled <em>the land of Rameses</em>, suggesting the Goshen region in the eastern Nile Delta.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "rameses"},
        "key_refs": ["Exodus 1:11", "Exodus 12:37", "Genesis 47:11"]
    },
    "ramoth": {
        "id": "ramoth",
        "term": "Ramoth",
        "category": "places",
        "intro": "<p>Ramoth (meaning <em>eminences</em> or <em>high places</em>) was the name of several towns in Israel. The most significant was Ramoth in Gilead (Ramoth-gilead), treated separately. A second Ramoth was a Levitical city in the tribe of Issachar (1 Chronicles 6:73), also called Jarmuth in Joshua 21:29 and Remeth in Joshua 19:21. A third Ramoth in the south appears in 1 Samuel 30:27 (Ramoth of the south / Ramath of the Negeb). The recurrence of the name throughout the tribal territories reflects its basic meaning: any elevated, prominent location could be designated a <em>ramoth.</em></p>",
        "sections": [],
        "hitchcock_meaning": "eminences; high places",
        "source_ids": {"easton": "ramoth"},
        "key_refs": ["1 Chronicles 6:73", "1 Samuel 30:27"]
    },
    "ramoth-gilead": {
        "id": "ramoth-gilead",
        "term": "Ramoth-gilead",
        "category": "places",
        "intro": "<p>Ramoth-gilead (meaning <em>heights of Gilead</em>) was one of the most strategically important cities in the Transjordan, serving as a Levitical city of refuge (Deuteronomy 4:43; Joshua 20:8; 21:38) and later as a frontier fortress contested between Israel and Aram-Damascus for most of the ninth century BC. It was the focal point of the battle in which Ahab of Israel was killed: against the advice of the prophet Micaiah, Ahab and Jehoshaphat of Judah fought against Aram to recover Ramoth-gilead; Ahab was killed by a random arrow (1 Kings 22:29–38).</p><p>The city remained a military flashpoint: Jehoram son of Ahab was wounded fighting for Ramoth-gilead (2 Kings 8:28–29), and it was at Ramoth-gilead that the prophet Elisha sent a young prophet to anoint Jehu son of Nimshi as king over Israel — the act that triggered Jehu's revolution and the end of the Omride dynasty (2 Kings 9:1–14). The site is generally identified with Tell Ramith in northern Jordan.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ramoth-gilead", "smith": "ramoth-gilead"},
        "key_refs": ["Deuteronomy 4:43", "1 Kings 22:3", "2 Kings 9:1"]
    },
    "ranges": {
        "id": "ranges",
        "term": "Ranges",
        "category": "concepts",
        "intro": "<p>Ranges in the KJV refers to cooking ranges — portable furnaces or hearth structures used in ancient Israelite households for preparing food. The Hebrew word <em>kirayim</em> (dual form, <em>two hearths</em>) appears in Leviticus 11:35 in the context of uncleanness: an earthenware oven or cooking range (ranges for pots) that became unclean through contact with a dead animal's carcass was to be broken and discarded, as earthenware could not be purified. The dual form likely reflects a double-hearth cooking arrangement. The term appears also in 2 Kings 11:8 and 2 Chronicles 23:14 with a different meaning: the <em>ranges</em> there refer to military ranks or formations.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ranges"},
        "key_refs": ["Leviticus 11:35", "2 Kings 11:8"]
    },
    "ransom": {
        "id": "ransom",
        "term": "Ransom",
        "category": "concepts",
        "intro": "<p>Ransom in the biblical sense is the price paid to secure the release of a captive, slave, condemned person, or dedicated animal. The Hebrew <em>kopher</em> (covering, ransom) and <em>padah</em> (to redeem) both appear in Old Testament legal and theological contexts. A ransom price was paid to release the firstborn from the obligation of consecration to God (Numbers 3:46–51), to substitute for a life forfeit under the law (Exodus 21:30), and to purchase the freedom of a slave (Leviticus 19:20).</p><p>The New Testament applies the concept directly to Christ's atoning work: Jesus declared that the Son of Man came <em>to give his life a ransom (<em>lytron</em>) for many</em> (Matthew 20:28; Mark 10:45). Paul uses the related term <em>antilytron</em> — a substitutionary ransom — in 1 Timothy 2:6. The concept implies a price paid, a captive released, and a substitute who takes the captive's place. Peter explains that redemption was not with silver or gold but with the precious blood of Christ (1 Peter 1:18–19).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ransom", "isbe": "ransom"},
        "key_refs": ["Matthew 20:28", "1 Timothy 2:6", "1 Peter 1:18", "Exodus 21:30"]
    },
    "rapha": {
        "id": "rapha",
        "term": "Rapha",
        "category": "people",
        "intro": "<p>Rapha (possibly meaning <em>tall</em>, related to Rephaim; or <em>lax</em>) was the name of two individuals in the Old Testament. The first was the fifth son of Benjamin (1 Chronicles 8:2), appearing in the later genealogical lists though not in Genesis 46:21's original list of Benjamin's sons — possibly reflecting a later descendant elevated to clan status. The second was a Benjaminite ancestor of the family of Saul: Rapha son of Binea and father of Eleasah (1 Chronicles 8:37; 9:43). The Rephaim or giants associated with the Philistines (2 Samuel 21:15–22) are called sons of <em>harapha</em> in some translations, suggesting a connection to this name.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "rapha"},
        "key_refs": ["1 Chronicles 8:2", "1 Chronicles 8:37"]
    },
    "raphu": {
        "id": "raphu",
        "term": "Raphu",
        "category": "people",
        "intro": "<p>Raphu (meaning <em>healed</em> or <em>feared</em>) was a Benjaminite, the father of Palti son of Raphu, who was chosen as the representative of the tribe of Benjamin among the twelve spies sent by Moses to explore Canaan (Numbers 13:9). Palti (not to be confused with Paltiel the husband of Michal) is the only context in which Raphu is mentioned. He is otherwise unknown.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "raphu"},
        "key_refs": ["Numbers 13:9"]
    },
    "raven": {
        "id": "raven",
        "term": "Raven",
        "category": "concepts",
        "intro": "<p>The raven (<em>oreb</em> in Hebrew, <em>korax</em> in Greek) was among the unclean birds forbidden as food (Leviticus 11:15; Deuteronomy 14:14) but is honored in several remarkable biblical episodes. Noah first sent out a raven after the Flood; unlike the dove, it went to and fro, finding no rest, until the waters dried up (Genesis 8:7). God supernaturally provided for Elijah at the brook Cherith by commanding ravens to bring him bread and meat morning and evening (1 Kings 17:4–6). Jesus cited God's care for ravens — who neither sow nor reap nor have storehouses yet are fed by God — as evidence that the heavenly Father cares far more for his people (Luke 12:24).</p><p>Ravens are black birds of the crow family known for intelligence and adaptability. The raven's dark color is celebrated in the Song of Solomon 5:11: the beloved's hair is described as <em>black as a raven.</em></p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "raven", "isbe": "raven"},
        "key_refs": ["Genesis 8:7", "1 Kings 17:4", "Luke 12:24"]
    },
    "razor": {
        "id": "razor",
        "term": "Razor",
        "category": "concepts",
        "intro": "<p>The razor (<em>ta'ar</em> in Hebrew) was a sharp blade used for shaving the head and beard in the ancient Near East. Its most theologically significant use in the Old Testament is in connection with the Nazirite vow: one of the three defining restrictions of a Nazirite was that <em>no razor shall touch his head</em> for the duration of the vow (Numbers 6:5). Samson's Nazirite consecration from birth meant his hair was never to be cut; Delilah's betrayal of this secret to the Philistines, resulting in a razor being applied to his head while he slept, caused the loss of his strength (Judges 16:17–19). Isaiah 7:20 uses the image of a hired razor as a metaphor for Assyrian conquest: God will use the king of Assyria to shave Israel bare — a symbol of humiliation and devastation.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "razor"},
        "key_refs": ["Numbers 6:5", "Judges 16:17", "Isaiah 7:20"]
    },
    "reba": {
        "id": "reba",
        "term": "Reba",
        "category": "people",
        "intro": "<p>Reba (meaning <em>the fourth</em> or <em>a square</em>) was one of five Midianite kings slain by Israel in the punitive campaign commanded after the Baal-peor apostasy (Numbers 31:8; Joshua 13:21). He and his four royal colleagues — Evi, Rekem, Zur, and Hur — were <em>princes of Midian</em> who were vassal rulers under Sihon king of the Amorites. Balaam son of Beor was also killed in the same campaign (Numbers 31:8). The five kings represented the leadership of the Midianite confederacy that had seduced Israel into idolatry at Peor, making them targets of the divinely commanded military response.</p>",
        "sections": [],
        "hitchcock_meaning": "the fourth; a square; that lies or stoops down",
        "source_ids": {"easton": "reba"},
        "key_refs": ["Numbers 31:8", "Joshua 13:21"]
    },
    "rebekah": {
        "id": "rebekah",
        "term": "Rebekah",
        "category": "people",
        "intro": "<p>Rebekah (meaning <em>captivating</em> or <em>a quarrel appeased</em>) was the daughter of Bethuel, the grandniece of Abraham, and the wife of Isaac. She was chosen as Isaac's bride when Abraham's servant prayed at a well in Paddan-aram and she appeared, offering to draw water for him and all his camels — an act of extraordinary generosity that the servant took as the divine sign he had requested (Genesis 24). She agreed to leave her family immediately and travel to Canaan to marry the man she had never met (Genesis 24:58).</p><p>Rebekah was barren for twenty years until Isaac's prayer moved God to open her womb. She carried twins who struggled within her; God's oracle declared that the elder would serve the younger. When the time came, she orchestrated Jacob's deception of the blind Isaac to secure the patriarchal blessing for Jacob rather than Esau (Genesis 27) — an act of cunning that achieved the divine purpose but set off decades of family conflict and Jacob's exile. She was buried in the cave of Machpelah (Genesis 49:31). Paul cites her as evidence of God's elective purpose operating before the children were born (Romans 9:10–13).</p>",
        "sections": [],
        "hitchcock_meaning": "fat; fattened; a quarrel appeased",
        "source_ids": {"easton": "rebekah", "smith": "rebekah", "isbe": "rebekah"},
        "key_refs": ["Genesis 24:58", "Genesis 25:23", "Genesis 27:6", "Romans 9:10"]
    },
    "rechab": {
        "id": "rechab",
        "term": "Rechab",
        "category": "people",
        "intro": "<p>Rechab was the name of several biblical figures. The most theologically significant was Rechab son of Rimmon the Beerothite, who, with his brother Baanah, murdered Ish-bosheth son of Saul in his bed hoping to gain David's favor; David instead condemned them to death for killing an innocent man (2 Samuel 4:2–12). A different and more honored Rechab was the ancestor of the Rechabites — a clan of strict traditionalists who maintained the nomadic lifestyle and abstinence from wine in honor of their ancestor Jonadab son of Rechab, who had assisted Jehu in his purge of the Omrides (2 Kings 10:15–23). Jeremiah honored the Rechabites as a model of covenantal faithfulness (Jeremiah 35).</p>",
        "sections": [],
        "hitchcock_meaning": "square; chariot with team of four horses",
        "source_ids": {"easton": "rechab", "smith": "rechab"},
        "key_refs": ["2 Samuel 4:2", "2 Kings 10:15", "Jeremiah 35:6"]
    },
    "rechabites": {
        "id": "rechabites",
        "term": "Rechabites",
        "category": "people",
        "intro": "<p>The Rechabites were a clan within Israel who maintained an ascetic, nomadic way of life in strict obedience to the commands of their ancestor Jonadab (Jehonadab) son of Rechab. Jonadab had commanded his descendants to drink no wine, build no houses, sow no seed, and plant no vineyards — to live always in tents as sojourners in the land (Jeremiah 35:6–7). Jonadab was the same man who accompanied Jehu in his violent purge of Baal worship from Israel (2 Kings 10:15–23), and the Rechabites' lifestyle reflected a conservative, Kenite-related tradition of pre-agricultural religious simplicity.</p><p>Jeremiah's encounter with the Rechabites (Jeremiah 35) is one of the most striking symbolic acts in the prophetic literature: God commanded Jeremiah to offer them wine; they refused. God then used their obedience to Jonadab's human command as a rebuke to Judah's disobedience to the divine command — and rewarded the Rechabites with the promise that they would never lack a man to stand before the LORD.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "rechabites", "isbe": "rechabites"},
        "key_refs": ["Jeremiah 35:6", "Jeremiah 35:19", "2 Kings 10:15"]
    },
    "reconcilation": {
        "id": "reconcilation",
        "term": "Reconciliation",
        "category": "concepts",
        "intro": "<p>Reconciliation — the restoration of a broken relationship — is one of the New Testament's primary metaphors for the effect of Christ's atoning work. The Greek <em>katallage</em> (reconciliation, exchange) and its verb <em>katallasso</em> describe the restoration of peaceful relationship between estranged parties. The metaphor assumes that sin has created a state of enmity between humanity and God; Christ's death addresses this enmity, making possible a restored relationship. Paul develops the theology in Romans 5:10–11 (<em>we were reconciled to God through the death of his Son</em>) and 2 Corinthians 5:18–21, where God through Christ <em>reconciled us to himself</em> and gave the church the <em>ministry of reconciliation.</em></p><p>Paul's formulation in Colossians 1:21–22 describes the change from hostile alienation to holy standing before God <em>through his body of flesh by his death.</em> The reconciliation is God-initiated, Christ-accomplished, and results not in God changing his character but in the removal of the sin-barrier that prevented restored fellowship. Hebrews uses the related term <em>atonement</em> in the context of the Day of Atonement typology.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "reconcilation", "isbe": "reconcilation"},
        "key_refs": ["Romans 5:10", "2 Corinthians 5:18", "Colossians 1:21"]
    },
    "recorder": {
        "id": "recorder",
        "term": "Recorder",
        "category": "concepts",
        "intro": "<p>The recorder (<em>mazkir</em> in Hebrew, from <em>zakar</em>, to remember or make mention) was a high official in the royal courts of both David and Solomon, listed alongside the priest and the secretary as one of the principal officers of state (2 Samuel 8:16; 20:24; 1 Kings 4:3). The office appears in the courts of Hezekiah (2 Kings 18:18, 37; Isaiah 36:3, 22) and Josiah (2 Chronicles 34:8). The recorder likely served as a herald or spokesman — one who kept and announced the official records and communications of the court, perhaps functioning as both court historian and royal announcer. The Assyrian parallel (<em>rab shakeh</em>, chief announcer) illuminates the office's public-communication dimension.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "recorder", "isbe": "recorder"},
        "key_refs": ["2 Samuel 8:16", "1 Kings 4:3", "2 Kings 18:18"]
    },
    "red-sea": {
        "id": "red-sea",
        "term": "Red Sea",
        "category": "places",
        "intro": "<p>The Red Sea (Hebrew <em>Yam Suph</em>, literally <em>Sea of Reeds</em> or <em>Reed Sea</em>) was the body of water through which God miraculously delivered Israel from Pharaoh's army during the Exodus. The term <em>Yam Suph</em> applies in various Old Testament contexts both to the Gulf of Suez arm of the Red Sea and to the Gulf of Aqabah. The exact site of the Exodus crossing has been debated for centuries: proposed locations include the northern Gulf of Suez, the Bitter Lakes, Lake Timsah, and the papyrus marshes of the eastern Nile Delta. Exodus 14–15 describes the miraculous crossing and Moses's song of triumph celebrating God's defeat of the Egyptians.</p><p>The Red Sea crossing became the defining paradigm of divine deliverance in Israelite theology — the act to which prophets, psalmists, and apostolic writers return repeatedly as the supreme demonstration of God's power and faithfulness. Hebrews 11:29 counts crossing the Red Sea by faith among the acts of the wilderness generation. The Song of Moses at the sea (Exodus 15) is echoed in the Song of the Lamb in Revelation 15:3.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "red-sea", "smith": "red-sea", "isbe": "red-sea"},
        "key_refs": ["Exodus 14:22", "Exodus 15:4", "Hebrews 11:29", "Revelation 15:3"]
    },
    "red-sea-passage-of": {
        "id": "red-sea-passage-of",
        "term": "Red Sea, Passage of",
        "category": "events",
        "intro": "<p>The passage through the Red Sea (Reed Sea) was the pivotal event of the Exodus in which God opened a way through the waters for Israel to cross on dry ground and then caused the waters to return upon Pharaoh's pursuing army, drowning the Egyptian forces (Exodus 14). Moses stretched out his hand over the sea; the LORD drove the sea back with a strong east wind all night, and Israel passed through on dry ground with walls of water on their right and left. When Pharaoh's chariots followed, the LORD looked down from the pillar of fire and threw the Egyptian army into confusion; Moses stretched out his hand and the waters returned.</p><p>The event generated two of the oldest and most celebrated poems in the Old Testament: the Song of Moses (Exodus 15:1–18) and Miriam's brief antiphonal chorus (Exodus 15:20–21). Psalm 77:16–20, Psalm 78:13, and Isaiah 51:10 commemorate it as defining evidence of divine power. Paul in 1 Corinthians 10:1–4 interprets the passage as a baptism <em>into Moses</em>, a typological anticipation of Christian baptism.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "red-sea-passage-of"},
        "key_refs": ["Exodus 14:22", "Exodus 15:1", "1 Corinthians 10:1", "Psalms 77:16"]
    },
    "redeemer": {
        "id": "redeemer",
        "term": "Redeemer",
        "category": "concepts",
        "intro": "<p>Redeemer (<em>go'el</em> in Hebrew) was a legal term for the nearest male kinsman who had both the right and the obligation to act on behalf of a family member in need: to purchase back land that had been sold under economic distress, to marry a kinsman's widow to continue his name (levirate duty), and to avenge a murdered relative (blood avenger). The institution of the kinsman-redeemer is fully illustrated in the book of Ruth, where Boaz fulfills the role for Naomi and Ruth by marrying Ruth and redeeming Elimelech's land. The concept required the redeemer to be a blood relative with the means and will to act.</p><p>The Old Testament applies the title to God himself as Israel's supreme Redeemer: Isaiah uses <em>go'el</em> of the LORD more than twenty times, especially in the passages of consolation (Isaiah 41:14; 43:14; 44:6, 24; 48:17; 49:7, 26; 54:5, 8; 60:16). Job's great confession — <em>I know that my Redeemer lives</em> (Job 19:25) — anticipates a personal divine advocate who will vindicate him. The New Testament applies the full weight of this imagery to Christ, whose incarnation as a human being qualified him as the kinsman who could redeem humanity from bondage.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "redeemer", "isbe": "redeemer"},
        "key_refs": ["Job 19:25", "Isaiah 44:6", "Ruth 4:1", "Galatians 4:5"]
    },
    "redemption": {
        "id": "redemption",
        "term": "Redemption",
        "category": "concepts",
        "intro": "<p>Redemption in biblical theology refers to the act of buying back someone from bondage or releasing them from an obligation by payment of a price. The Hebrew roots <em>padah</em> (to ransom, buy out of obligation) and <em>ga'al</em> (to act as kinsman-redeemer) both underlie the English word, alongside the Greek <em>agorazo</em> (to buy in the marketplace) and <em>lytroo</em> (to release on payment of ransom). The Exodus from Egypt was the paradigmatic act of divine redemption in the Old Testament: God <em>redeemed</em> Israel from the house of slavery (Deuteronomy 7:8; 13:5).</p><p>The New Testament presents Christ's death as the ultimate redemptive act: <em>you were bought with a price</em> (1 Corinthians 6:20); <em>redemption that is in Christ Jesus</em> (Romans 3:24); <em>he gave himself as a ransom for all</em> (1 Timothy 2:6). Ephesians 1:7 identifies redemption with forgiveness of trespasses through Christ's blood. The full scope of redemption includes liberation from sin's penalty, power, and presence — extending to the redemption of the body at the resurrection (Romans 8:23) and the renewal of creation (Colossians 1:20).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "redemption", "isbe": "redemption"},
        "key_refs": ["Romans 3:24", "Ephesians 1:7", "1 Peter 1:18", "Deuteronomy 7:8"]
    },
    "reed": {
        "id": "reed",
        "term": "Reed",
        "category": "concepts",
        "intro": "<p>Reeds (<em>agmon</em>, <em>qaneh</em>, <em>suph</em> in Hebrew) were tall grasses growing in the marshy margins of rivers, lakes, and coastal areas throughout the ancient Near East, especially in Egypt along the Nile. The <em>qaneh</em> (calamus reed) was used as a measuring rod — a standard unit of length equal to six cubits (Ezekiel 40:3, 5; 41:8; Revelation 11:1; 21:15–16). Moses's basket was made of reeds or papyrus (Exodus 2:3). Reeds were also used to make writing tools, flutes, and roof thatch.</p><p>The symbolic uses of the reed in prophecy are significant. Isaiah 36:6 and 2 Kings 18:21 warn that trusting Egypt is like leaning on a <em>bruised reed</em> — it will pierce the hand. Matthew 12:20, quoting Isaiah 42:3, uses the same image of God's Servant: <em>a bruised reed he will not break</em> — a symbol of the gentle care of Christ for the weak and damaged. Reeds were also instruments of mockery at the crucifixion: Jesus was given a reed scepter in his hand by the soldiers who mocked him as king, and a vinegar-soaked sponge was offered to him on a reed (Matthew 27:29, 48).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "reed", "isbe": "reed"},
        "key_refs": ["Isaiah 42:3", "Matthew 12:20", "Ezekiel 40:3", "Matthew 27:48"]
    },
    "refiner": {
        "id": "refiner",
        "term": "Refiner",
        "category": "concepts",
        "intro": "<p>The refiner was a craftsman who purified metals — primarily silver and gold — by melting ore in a crucible and skimming off the dross (impurities) until only pure metal remained. The process required sustained, controlled heat and the skill to know when purification was complete. The refiner's work became one of the most powerful metaphors in biblical prophecy for God's disciplinary action on his people. Malachi 3:2–3 asks: <em>who can endure the day of his coming?... for he is like a refiner's fire</em>; he will sit as a refiner of silver, purifying the sons of Levi until they present offerings in righteousness.</p><p>Isaiah 48:10 applies the same image to Israel's exile: <em>I have refined you, but not as silver; I have tried you in the furnace of affliction.</em> Jeremiah 6:29–30 uses the image of a failed refining process as a metaphor for Israel's incorrigibility. Proverbs 17:3 draws the parallel: <em>the crucible is for silver, and the furnace is for gold, and the LORD tests hearts.</em> The metaphor conveys both the painful character of divine discipline and its purposeful, restorative goal.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "refiner", "isbe": "refiner"},
        "key_refs": ["Malachi 3:2", "Isaiah 48:10", "Proverbs 17:3", "Jeremiah 6:29"]
    },
    "refuge-cities-of": {
        "id": "refuge-cities-of",
        "term": "Refuge, Cities of",
        "category": "concepts",
        "intro": "<p>The cities of refuge were six specially designated Levitical cities — three on each side of the Jordan — to which a person who had accidentally killed another could flee and receive protection from the blood avenger until a fair trial could be conducted (Numbers 35:9–34; Deuteronomy 19:1–13; Joshua 20). The three cities west of the Jordan were Kedesh in Naphtali, Shechem in Ephraim, and Kirjath-arba (Hebron) in Judah; the three east of the Jordan were Bezer in Reuben, Ramoth in Gilead, and Golan in Bashan. The roads to them were to be kept in good repair.</p><p>The institution distinguished between murder (premeditated killing, which received no asylum) and manslaughter (unintentional killing, which did). The accidental killer must remain in the city until the death of the high priest, after which he could return safely to his home. The New Testament, particularly in Hebrews 6:18, alludes to the cities of refuge as a type of the hope in Christ: believers who have fled for refuge to the hope set before them find an anchor for the soul, established by God's oath.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "refuge-cities-of", "isbe": "refuge-cities-of"},
        "key_refs": ["Numbers 35:11", "Joshua 20:1", "Hebrews 6:18"]
    },
    "regem-melech": {
        "id": "regem-melech",
        "term": "Regem-melech",
        "category": "people",
        "intro": "<p>Regem-melech (meaning <em>friend of the king</em> or <em>stone of the king</em>) was one of two men sent by the people of Bethel to Jerusalem to inquire of the priests and prophets whether the fasts observed during the exile should continue now that the temple was being rebuilt (Zechariah 7:2). The mission prompted Zechariah's response about the purpose of true fasting and true justice. Regem-melech appears only in this passage and nothing further is known of him.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "regem-melech"},
        "key_refs": ["Zechariah 7:2"]
    },
    "regeneration": {
        "id": "regeneration",
        "term": "Regeneration",
        "category": "concepts",
        "intro": "<p>Regeneration (Greek <em>palingenesia</em>, <em>new birth</em>; also described as being <em>born again</em> or <em>born of the Spirit</em>) is the theological term for the divine act by which God imparts new spiritual life to a person, transforming them from spiritual death to spiritual life. The concept is developed most fully in John 3:1–8, where Jesus tells Nicodemus: <em>unless one is born of water and the Spirit, he cannot enter the kingdom of God.</em> This new birth is not of human will but of God (John 1:13), accomplished by the Holy Spirit working through the word of God (1 Peter 1:23; James 1:18).</p><p>Titus 3:5 uses <em>palingenesia</em> directly: God saved us <em>through the washing of regeneration and renewing of the Holy Spirit.</em> The term also appears in Matthew 19:28 for the cosmic renewal at the consummation. The regenerate person is described as a <em>new creation</em> (2 Corinthians 5:17), passing from death to life (1 John 3:14) — a change as total as being born a second time. Reformed theology has typically held that regeneration logically precedes and produces saving faith; Arminian theology typically views faith as a condition that precedes regeneration.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "regeneration", "isbe": "regeneration"},
        "key_refs": ["John 3:3", "Titus 3:5", "1 Peter 1:23", "2 Corinthians 5:17"]
    },
    "rehabiah": {
        "id": "rehabiah",
        "term": "Rehabiah",
        "category": "people",
        "intro": "<p>Rehabiah (meaning <em>breadth</em> or <em>extent of the LORD</em>) was a Levite, the only son of Eliezer son of Moses, and ancestor of a large Levitical family. The text notes that Eliezer had no other sons, yet Rehabiah's descendants were very numerous (1 Chronicles 23:17; 26:25). His descendants served as temple officials: the eldest of Rehabiah's line, Isshiah, was an officer over the treasuries of the dedicated things in David's administrative organization (1 Chronicles 26:25). The note about their great number despite a single-son lineage emphasizes divine blessing on Moses's line.</p>",
        "sections": [],
        "hitchcock_meaning": "breadth, or extent, of the Lord",
        "source_ids": {"easton": "rehabiah"},
        "key_refs": ["1 Chronicles 23:17", "1 Chronicles 26:25"]
    },
    "rehob": {
        "id": "rehob",
        "term": "Rehob",
        "category": "places",
        "intro": "<p>Rehob (meaning <em>breadth</em> or <em>open space</em>) was the name of two towns and two individuals in the Old Testament. The most important town was Rehob in Asher (Joshua 19:28, 30), which was among the cities the tribe of Asher failed to drive the Canaanites from (Judges 1:31). A second Rehob was in the far north of Canaan — the scouts sent by Moses entered Canaan as far as Rehob near the entrance to Hamath (Numbers 13:21). As a personal name, Rehob was the father of Hadadezer, the Aramean king of Zobah whom David defeated (2 Samuel 8:3, 12), and a Levite who sealed Nehemiah's covenant (Nehemiah 10:11).</p>",
        "sections": [],
        "hitchcock_meaning": "breadth; space; extent",
        "source_ids": {"easton": "rehob"},
        "key_refs": ["Numbers 13:21", "Joshua 19:28", "Judges 1:31"]
    },
    "rehoboam": {
        "id": "rehoboam",
        "term": "Rehoboam",
        "category": "people",
        "intro": "<p>Rehoboam was the son of Solomon by the Ammonite princess Naamah and the last king of the united monarchy, whose foolish response to the people's petition for relief precipitated the division of the kingdom in approximately 930 BC. When the northern tribes assembled at Shechem and asked Rehoboam to lighten the heavy tax burden of Solomon's reign, Rehoboam rejected the counsel of the experienced elders who advised conciliation and instead followed the young men who advised severity: <em>My father chastised you with whips, but I will chastise you with scorpions</em> (1 Kings 12:14). The northern tribes immediately seceded under Jeroboam, leaving Rehoboam with only Judah and Benjamin.</p><p>Rehoboam reigned seventeen years in Jerusalem (1 Kings 14:21) but presided over a marked religious deterioration — Judah built high places, sacred pillars, and Asherah poles on every hill. In the fifth year of his reign, Shishak king of Egypt invaded and plundered both Jerusalem and the temple, carrying away the gold shields of Solomon which Rehoboam replaced with bronze shields (1 Kings 14:25–28). His reign is treated as a cautionary example of pride, folly, and the cost of ignoring wise counsel.</p>",
        "sections": [],
        "hitchcock_meaning": "who sets the people at liberty",
        "source_ids": {"easton": "rehoboam", "smith": "rehoboam", "isbe": "rehoboam"},
        "key_refs": ["1 Kings 12:14", "1 Kings 12:16", "1 Kings 14:25"]
    },
    "rehoboth": {
        "id": "rehoboth",
        "term": "Rehoboth",
        "category": "places",
        "intro": "<p>Rehoboth (meaning <em>spaces</em> or <em>wide places</em>) was the name of a well and a city. The well was dug by Isaac in the valley of Gerar after two earlier wells had been disputed by the herdsmen of Gerar; when this third well was dug without dispute, Isaac named it Rehoboth, saying <em>Now the LORD has made room for us</em> (Genesis 26:22). The name marked a moment of divine provision and the beginning of peaceable settlement.</p><p>Rehoboth-by-the-river (Genesis 36:37; 1 Chronicles 1:48) was the hometown of Saul (Shaul) king of Edom, one of the pre-Israelite Edomite kings. Genesis 10:11 mentions a Rehoboth-Ir as a city near Nineveh, built by Nimrod or Asshur. The recurrence of the name reflects its topographic meaning — broad, spacious places suitable for settlement.</p>",
        "sections": [],
        "hitchcock_meaning": "spaces; places",
        "source_ids": {"easton": "rehoboth", "smith": "rehoboth"},
        "key_refs": ["Genesis 26:22", "Genesis 36:37"]
    },
    "rehum": {
        "id": "rehum",
        "term": "Rehum",
        "category": "people",
        "intro": "<p>Rehum (meaning <em>merciful</em> or <em>compassionate</em>) was a common name in the post-exilic period, borne by several figures. The most prominent was Rehum the commanding officer who, with Shimshai the scribe, wrote to Artaxerxes king of Persia to oppose the rebuilding of Jerusalem, claiming the city was historically rebellious and would refuse to pay tribute (Ezra 4:8–24). The letter was successful in temporarily halting the work. Other bearers of the name include a leader who returned from exile with Zerubbabel (Ezra 2:2 — called Nehum in Nehemiah 7:7), a Levite who helped repair the wall under Nehemiah (Nehemiah 3:17), and one who sealed the covenant (Nehemiah 10:25).</p>",
        "sections": [],
        "hitchcock_meaning": "merciful; compassionate",
        "source_ids": {"easton": "rehum"},
        "key_refs": ["Ezra 4:8", "Nehemiah 3:17"]
    },
    "rei": {
        "id": "rei",
        "term": "Rei",
        "category": "people",
        "intro": "<p>Rei (meaning <em>my shepherd</em> or <em>my friend</em>) was one of David's loyal supporters who did not side with Adonijah when Adonijah attempted to seize the throne before David's death (1 Kings 1:8). He is listed alongside Benaiah, the mighty men, Zadok, and Nathan as those who supported the succession of Solomon. Nothing further is recorded about him; his exact role or status at the court is not defined. The brief mention preserves his name in the narrative of David's final political crisis.</p>",
        "sections": [],
        "hitchcock_meaning": "my shepherd; my companion; my friend",
        "source_ids": {"easton": "rei"},
        "key_refs": ["1 Kings 1:8"]
    },
    "reins": {
        "id": "reins",
        "term": "Reins",
        "category": "concepts",
        "intro": "<p>Reins (from the Latin <em>renes</em>, kidneys) is an archaic English term used in the KJV to translate the Hebrew <em>kelayot</em> (kidneys) when referring to the seat of the deepest emotions, thoughts, and moral sensibility. In ancient Israelite physiological psychology the kidneys (reins) were understood to be the location of the deepest self — equivalent to what we might call conscience or the innermost being. Psalm 7:9 speaks of God as the one who <em>tests the hearts and minds (reins)</em>; Psalm 16:7 describes the reins instructing the psalmist in the night; Psalm 26:2 invites God to examine his heart and reins; Revelation 2:23 uses the same imagery when the risen Christ declares he is the one who <em>searches minds (kidneys) and hearts.</em> Modern translations typically render <em>kelayot</em> as <em>mind</em> or <em>inner parts.</em></p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "reins"},
        "key_refs": ["Psalms 7:9", "Psalms 16:7", "Revelation 2:23"]
    },
    "rekem": {
        "id": "rekem",
        "term": "Rekem",
        "category": "people",
        "intro": "<p>Rekem (meaning <em>vain pictures</em> or <em>embroidered</em>) was the name of two individuals and possibly a place in the Old Testament. The most prominent was Rekem, one of the five Midianite kings slain by Israel in the punitive campaign following the Baal-peor apostasy (Numbers 31:8; Joshua 13:21). A second Rekem was a Calebite, the son of Hebron in the genealogy of Judah (1 Chronicles 2:43–44). Some scholars associate the personal name with the Nabataean city of Petra, known to later sources as Rekem, though this connection is uncertain.</p>",
        "sections": [],
        "hitchcock_meaning": "vain pictures; divers picture",
        "source_ids": {"easton": "rekem"},
        "key_refs": ["Numbers 31:8", "1 Chronicles 2:43"]
    },
    "remaliah": {
        "id": "remaliah",
        "term": "Remaliah",
        "category": "people",
        "intro": "<p>Remaliah (meaning <em>the exaltation of the LORD</em>) was the father of Pekah, who murdered Pekahiah king of Israel and seized the throne, reigning approximately 740–732 BC (2 Kings 15:25–31). Isaiah refers to Pekah contemptuously as <em>the son of Remaliah</em> rather than by his royal name — a dismissive periphrasis reflecting Isaiah's low regard for Pekah's legitimacy and character (Isaiah 7:1, 4–5, 9; 8:6). The combined threat of Pekah and Rezin of Damascus against Jerusalem provided the occasion for Isaiah's great Immanuel prophecy (Isaiah 7:14).</p>",
        "sections": [],
        "hitchcock_meaning": "the exaltation of the Lord",
        "source_ids": {"easton": "remaliah"},
        "key_refs": ["2 Kings 15:25", "Isaiah 7:1", "Isaiah 7:9"]
    },
    "remeth": {
        "id": "remeth",
        "term": "Remeth",
        "category": "places",
        "intro": "<p>Remeth (meaning <em>height</em>) was a town in the territory of Issachar listed in Joshua 19:21. It is generally identified with Ramoth in Issachar (1 Chronicles 6:73) and with Jarmuth in the parallel list of Joshua 21:29. The same site appears under three names due to variant spellings and source traditions. It was a Levitical city allocated to the Gershonite families in the tribal allotment of Issachar. The site is tentatively identified with Kokab el-Hawa in the lower Jezreel valley.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "remeth"},
        "key_refs": ["Joshua 19:21", "1 Chronicles 6:73"]
    },
    "remmon-methoar": {
        "id": "remmon-methoar",
        "term": "Remmon-methoar",
        "category": "places",
        "intro": "<p>Remmon-methoar (meaning <em>Rimmon which is marked out</em> or <em>Rimmon to Neah</em>) appears in Joshua 19:13 as a place on the northern border of Zebulun. The phrase is likely a compound boundary description — the border reached toward Rimmon and went on to Neah — rather than a single place name. Rimmon (the Pomegranate) was a town north of Nazareth, possibly modern Rummana. The border description of Zebulun in Joshua 19:10–16 is notoriously difficult to trace precisely.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "remmon-methoar"},
        "key_refs": ["Joshua 19:13"]
    },
    "remphan": {
        "id": "remphan",
        "term": "Remphan",
        "category": "concepts",
        "intro": "<p>Remphan (also spelled Rephan or Rompha) is the name of a star-deity mentioned in Stephen's speech in Acts 7:43, quoting from the Septuagint version of Amos 5:26: <em>You took up the tent of Moloch and the star of your god Rephan, the images that you made to worship.</em> The Hebrew of Amos 5:26 reads <em>Kiyyun</em> (or Chiun), generally identified with the Akkadian Kayyamanu, a name for the planet Saturn worshipped in Mesopotamia. The Septuagint translators apparently substituted a related astral deity name known in their Egyptian context. Stephen uses the verse to indict Israel's persistent idolatry in the wilderness — worshipping astral deities alongside the LORD.</p>",
        "sections": [],
        "hitchcock_meaning": "prepared; arrayed",
        "source_ids": {"easton": "remphan", "isbe": "remphan"},
        "key_refs": ["Acts 7:43", "Amos 5:26"]
    },
    "rent": {
        "id": "rent",
        "term": "Rent",
        "category": "concepts",
        "intro": "<p>Rending or tearing garments (<em>qara</em> in Hebrew) was the most common and dramatic gesture of mourning, grief, and horror in ancient Israel. When Jacob heard of Joseph's apparent death, he <em>tore his garments and put sackcloth on his loins and mourned</em> (Genesis 37:34). Job tore his robe after receiving the news of his children's deaths (Job 1:20). The high priest tore his clothes when Jesus claimed to be the Son of God (Matthew 26:65), and Paul and Barnabas tore their clothes when the Lycaonians tried to sacrifice to them (Acts 14:14).</p><p>Rending garments was both a personal expression of grief and a prescribed ritual gesture. The Mosaic law restricted the high priest from tearing his vestments in mourning (Leviticus 10:6; 21:10) to preserve the integrity of the sacred office. The tearing of the temple veil from top to bottom at Jesus's death (Matthew 27:51) carries symbolic resonance with the garment-rending gesture — representing the radical opening of divine access accomplished by Christ's death.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "rent"},
        "key_refs": ["Genesis 37:34", "Job 1:20", "Matthew 26:65", "Matthew 27:51"]
    },
    "repentance": {
        "id": "repentance",
        "term": "Repentance",
        "category": "concepts",
        "intro": "<p>Repentance in biblical theology denotes a genuine change of mind, heart, and direction — a turning from sin toward God. The primary Hebrew root <em>shub</em> means to turn or return; it is the language of prophetic call: <em>Return to me and I will return to you</em> (Malachi 3:7). The Greek <em>metanoia</em> (from <em>meta</em> + <em>nous</em>, a change of mind) carries the sense of a fundamental reorientation of the whole person. Both John the Baptist and Jesus began their public ministries with the identical summons: <em>Repent, for the kingdom of heaven is at hand</em> (Matthew 3:2; 4:17).</p><p>Biblical repentance is not merely emotional sorrow (though grief over sin may accompany it) — Paul distinguishes between <em>godly grief</em> that produces repentance and mere worldly grief (2 Corinthians 7:10). Repentance involves acknowledgment of specific sin, turning from it, and turning toward God with changed behavior (Acts 26:20). Peter's Pentecost sermon demands repentance as the prerequisite for receiving forgiveness and the Holy Spirit (Acts 2:38). God himself does not change his nature but the Old Testament speaks of divine relenting (<em>nacham</em>) when human behavior changes (Jonah 3:10).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "repentance", "isbe": "repentance"},
        "key_refs": ["Matthew 4:17", "Acts 2:38", "2 Corinthians 7:10", "Acts 26:20"]
    },
    "rephael": {
        "id": "rephael",
        "term": "Rephael",
        "category": "people",
        "intro": "<p>Rephael (meaning <em>the healing of God</em> or <em>God has healed</em>) was the first son of Obed-edom, listed among the gatekeepers of the temple in David's administrative organization (1 Chronicles 26:7). He was described as a <em>capable man</em> (<em>ben chayil</em>), the same phrase used of Boaz and other men of valor. The Obed-edom family produced a notable number of gatekeepers and temple servants, perhaps because of their association with the ark of the covenant that had rested in Obed-edom's house. Rephael appears only in this genealogical-administrative context.</p>",
        "sections": [],
        "hitchcock_meaning": "the physic or medicine of God",
        "source_ids": {"easton": "rephael"},
        "key_refs": ["1 Chronicles 26:7"]
    },
    "rephaim": {
        "id": "rephaim",
        "term": "Rephaim",
        "category": "people",
        "intro": "<p>The Rephaim (singular Rapha; meaning uncertain — possibly <em>shades</em>, <em>the dead</em>, or <em>the giant ones</em>) were an ancient race of people of extraordinary physical stature who inhabited Canaan and Transjordan before and during Israel's conquest of the land. They are associated with several specific groups: the Emim in Moab, the Zamzummim in Ammon (Deuteronomy 2:10–11, 20–21), and the Anakim in the hill country. Og king of Bashan was described as the last survivor of the Rephaim (Deuteronomy 3:11), and the Valley of Rephaim near Jerusalem was apparently named after them (Joshua 15:8).</p><p>Several giant warriors encountered by David's men are described as descendants of <em>harapha</em> (the giant), including Ishbi-benob, Saph, the unnamed brother of Goliath, and Lahmi (2 Samuel 21:15–22; 1 Chronicles 20:4–8). In the poetic literature, <em>rephaim</em> also functions as a word for the shades of the dead in Sheol (Job 26:5; Psalm 88:10; Proverbs 2:18; Isaiah 14:9; 26:14, 19) — an overlap of meaning that has generated considerable discussion.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "rephaim", "smith": "rephaim", "isbe": "rephaim"},
        "key_refs": ["Genesis 14:5", "Deuteronomy 3:11", "2 Samuel 21:16"]
    },
    "rephaim-valley-of": {
        "id": "rephaim-valley-of",
        "term": "Rephaim, Valley of",
        "category": "places",
        "intro": "<p>The Valley of Rephaim (also called the Plain of Rephaim) was a broad, fertile valley southwest of Jerusalem, lying between Jerusalem and Bethlehem. It appears in the tribal boundary descriptions of both Judah (Joshua 15:8) and Benjamin (Joshua 18:16) and was evidently a prominent geographic feature of the region. The Philistines twice deployed forces in the Valley of Rephaim to attack David after he became king at Hebron, and David twice defeated them — the second time with the notable strategic device of circling and attacking from the rear at God's direction (2 Samuel 5:17–25; 1 Chronicles 14:8–17). Isaiah 17:5 invokes the valley's grain harvest as a simile for judgment.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "rephaim-valley-of"},
        "key_refs": ["Joshua 15:8", "2 Samuel 5:18", "2 Samuel 5:22", "Isaiah 17:5"]
    },
    "rephidim": {
        "id": "rephidim",
        "term": "Rephidim",
        "category": "places",
        "intro": "<p>Rephidim (meaning <em>resting places</em> or <em>supports</em>) was an Israelite campsite in the Sinai wilderness, the scene of two decisive events: the miraculous provision of water from the rock, and the battle against Amalek. At Rephidim Israel found no water and quarreled bitterly with Moses; God commanded Moses to strike the rock at Horeb, and water gushed out — the event named Massah and Meribah (Exodus 17:1–7). Immediately afterward, the Amalekites attacked and Joshua led the Israelite army in battle while Moses held up his hands on the hilltop, supported by Aaron and Hur; when his arms were raised, Israel prevailed (Exodus 17:8–16).</p><p>The location of Rephidim is debated: most traditional identifications place it in the Sinai peninsula in the vicinity of Jebel Musa. The altar Moses built there, called <em>The LORD is My Banner</em> (Yahweh-Nissi), established the theological connection between God's presence and military victory.</p>",
        "sections": [],
        "hitchcock_meaning": "beds; places of rest",
        "source_ids": {"easton": "rephidim", "smith": "rephidim"},
        "key_refs": ["Exodus 17:1", "Exodus 17:8", "Exodus 17:15"]
    },
    "reprobate": {
        "id": "reprobate",
        "term": "Reprobate",
        "category": "concepts",
        "intro": "<p>Reprobate (from Latin <em>reprobatus</em>, rejected after testing) translates the Hebrew <em>ma'as</em> (rejected) and Greek <em>adokimos</em> (failing the test, disqualified) in the KJV. Jeremiah 6:30 uses the image of a failed refining process: <em>refuse silver they are called, for the LORD has rejected them.</em> In the New Testament, <em>adokimos</em> describes a mind that God gives over to its own perversity (Romans 1:28 — <em>God gave them up to a reprobate mind</em>), land that has been cleared and bears only thorns (Hebrews 6:8), and Paul's own fear of being disqualified after preaching to others (1 Corinthians 9:27). 2 Timothy 3:8 describes those who oppose the truth as reprobate (disqualified) concerning the faith.</p><p>In Reformed theology, reprobation is the doctrinal counterpart to election — God's sovereign decision to pass over certain individuals and allow them to face the consequences of their sin. The term in the KJV, however, more often refers to practical failure of moral and spiritual testing than to eternal decretal reprobation.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "reprobate", "isbe": "reprobate"},
        "key_refs": ["Romans 1:28", "Jeremiah 6:30", "1 Corinthians 9:27"]
    },
    "rereward": {
        "id": "rereward",
        "term": "Rereward",
        "category": "concepts",
        "intro": "<p>Rereward (an archaic form of <em>rearguard</em>) is used in the KJV for the rear or covering force of a marching army or procession. In Numbers 10:25, the tribe of Dan served as the rereward for the entire camp of Israel in the wilderness march — the last tribal contingent, gathering and protecting the stragglers. Isaiah 52:12 and 58:8 use the image theologically: God promises his people that in the new Exodus from Babylon they will not leave in haste as they did from Egypt, for <em>the God of Israel will be your rereward</em> — protecting the rear of the procession. The image conveys complete divine protection from before and behind simultaneously.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "rereward"},
        "key_refs": ["Numbers 10:25", "Isaiah 52:12", "Isaiah 58:8"]
    },
    "resen": {
        "id": "resen",
        "term": "Resen",
        "category": "places",
        "intro": "<p>Resen (meaning <em>a bridle</em> or <em>bit</em>) was one of the cities of the ancient Assyrian empire described in Genesis 10:11–12 as built by Nimrod (or by Asshur) between Nineveh and Calah — <em>that is the great city.</em> The phrase <em>the great city</em> may refer to Resen itself, to the entire complex of cities, or to Nineveh or Calah. The location of Resen has not been positively identified; it may correspond to one of the sites on the Tigris between the ruins of Nineveh (modern Mosul) and Calah (modern Nimrud).</p>",
        "sections": [],
        "hitchcock_meaning": "a bridle or bit",
        "source_ids": {"easton": "resen"},
        "key_refs": ["Genesis 10:12"]
    },
    "rest": {
        "id": "rest",
        "term": "Rest",
        "category": "concepts",
        "intro": "<p>Rest in biblical theology encompasses both physical cessation from labor and the deep theological concept of God's sabbath rest and the eschatological rest promised to his people. The divine rest on the seventh day of creation (Genesis 2:2–3) established the pattern for the sabbath commandment (Exodus 20:11) and for Israel's land-sabbath every seventh year. The promised rest for Israel was the land of Canaan — a place of settled security in God's presence after the wilderness wandering (Deuteronomy 12:9–10; Joshua 21:44).</p><p>The letter to the Hebrews develops the theology of rest most fully (chapters 3–4). Drawing on Psalm 95:11 (<em>They shall not enter my rest</em>), the writer argues that the wilderness generation failed to enter the rest through unbelief; that Joshua's entry into Canaan was not the final rest (for David still spoke of it as future in Psalm 95); and that therefore a <em>sabbath rest</em> (<em>sabbatismos</em>) remains for the people of God — entered now by faith and consummated in the age to come (Hebrews 4:1–11). Jesus's invitation — <em>Come to me... and I will give you rest</em> (Matthew 11:28–29) — identifies himself as the rest of God.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "rest", "isbe": "rest"},
        "key_refs": ["Matthew 11:28", "Hebrews 4:1", "Hebrews 4:9", "Psalms 95:11"]
    },
    "resurrection-of-christ": {
        "id": "resurrection-of-christ",
        "term": "Resurrection of Christ",
        "category": "events",
        "intro": "<p>The resurrection of Christ is the foundational event of Christian faith — the bodily rising of Jesus of Nazareth from death to eternal life on the third day after his crucifixion. All four Gospels narrate the discovery of the empty tomb on the first day of the week by women followers of Jesus (Matthew 28; Mark 16; Luke 24; John 20), followed by appearances of the risen Jesus to Mary Magdalene, the disciples, Thomas, the Emmaus travelers, and others. Paul provides the earliest written account, recording a series of post-resurrection appearances including to Peter, the twelve, five hundred people at once, James, and finally Paul himself (1 Corinthians 15:3–8).</p><p>Paul argues in 1 Corinthians 15:12–19 that the resurrection is not peripheral but constitutive of the gospel: <em>if Christ has not been raised, your faith is futile and you are still in your sins.</em> The resurrection vindicated Jesus's claims, fulfilled the Scriptures (citing Psalm 16:10 in Acts 2:27–31), inaugurated the new creation, and guaranteed the future resurrection of all who belong to Christ. Jesus's resurrection body was physical yet glorified — recognizable yet able to appear and disappear. The empty tomb and the post-resurrection appearances together formed the basis of apostolic proclamation from Pentecost onward.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "resurrection-of-christ", "isbe": "resurrection-of-christ"},
        "key_refs": ["1 Corinthians 15:4", "1 Corinthians 15:14", "Acts 2:24", "Matthew 28:6"]
    },
}


def main():
    written = 0
    skipped = 0
    for slug, data in ARTICLES.items():
        if merge_article(slug, data):
            written += 1
        else:
            skipped += 1
    print(f'BP R1: Raamah → Resurrection of Christ: wrote {written}, skipped {skipped} existing.')

if __name__ == '__main__':
    main()
