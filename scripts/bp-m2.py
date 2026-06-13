"""
BP Article Synthesis — m2: Mareshah → Merchant
Covers Easton entries: Mareshah through Merchant (75 entries)

Sources consulted:
  - data/dictionary/index.json (Easton briefs)
  - data/dictionary/{slug}.json (Easton full HTML + refs, per entry)
  - data/smith/index.json (Smith briefs)
  - data/isbe/index.json (ISBE briefs)
  - data/hitchcock/index.json (name meanings)

Category logic applied:
  - people:   Hitchcock match + no major place signals in brief
  - places:   brief/title contains 'city', 'town', 'sea of', 'river', 'mount', 'valley', etc.
  - concepts: no Hitchcock match, no place signals
  - names:    Hitchcock-only (no Easton/Smith entry exists)
  - events:   title is clearly an event (battle, feast, exile, flood, etc.)

Script: scripts/bp-m2.py
Run: python3 scripts/bp-m2.py
"""

import json, os

OUT_DIR = 'data/biblepedia/articles'
os.makedirs(OUT_DIR, exist_ok=True)


def load_article(slug):
    path = os.path.join(OUT_DIR, slug + '.json')
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    return None


def save_article(slug, data):
    path = os.path.join(OUT_DIR, slug + '.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)


def merge_article(slug, data):
    # Never overwrite an existing synthesis — idempotent safety
    if load_article(slug) is not None:
        return False
    save_article(slug, data)
    return True


ARTICLES = {
    "mareshah": {
        "id": "mareshah",
        "term": "Mareshah",
        "category": "places",
        "intro": "<p>Mareshah (meaning <em>from the beginning</em> or <em>an inheritance</em>) was a city in the Shephelah lowlands of Judah, assigned to the tribe of Judah (Joshua 15:44) and later fortified by Rehoboam as one of his border strongholds (2 Chronicles 11:8). It is best known as the site of the battle in which King Asa of Judah defeated the vast Ethiopian army of Zerah in the valley of Zephathah, a signal victory attributed to Asa's prayer and trust in God (2 Chronicles 14:9–10).</p><p>Mareshah was also the ancestral home of the prophet Micah (Micah 1:15) and appears in Micah's lament as one of the cities that would fall to Assyrian invasion. Archaeological excavation has identified it with Tell Sandahannah near Beit Jibrin, where Hellenistic remains confirm significant occupation in the intertestamental period.</p>",
        "hitchcock_meaning": "from the beginning; an inheritance",
        "source_ids": {"easton": "mareshah", "smith": "mareshah"},
        "key_refs": ["Joshua 15:44", "2 Chronicles 14:9", "2 Chronicles 14:10"]
    },
    "mark": {
        "id": "mark",
        "term": "Mark",
        "category": "people",
        "intro": "<p>Mark (meaning <em>same as Marcus</em>, from Latin <em>Marcus</em>) was the author of the second Gospel and a companion of Paul, Barnabas, and Peter in early Christian mission. His full name was John Mark; John was his Hebrew name, Mark his Roman surname. He was the son of Mary of Jerusalem, in whose house the early church gathered (Acts 12:12), and the cousin of Barnabas (Colossians 4:10). He accompanied Paul and Barnabas on the first missionary journey but turned back at Perga in Pamphylia — a desertion Paul regarded seriously enough to refuse his company on the second journey (Acts 13:13; 15:38).</p><p>Reconciliation followed: Paul later commended Mark as useful for ministry (2 Timothy 4:11), and Peter claimed him as a spiritual son (1 Peter 5:13). Ancient tradition, traced to Papias of Hierapolis through Eusebius, identifies Mark's Gospel as the written record of Peter's preaching — an interpretation consistent with the Gospel's vivid, eyewitness texture and its emphasis on Jesus's actions over his discourses.</p>",
        "hitchcock_meaning": "same as Marcus",
        "source_ids": {"easton": "mark", "smith": "mark", "isbe": "mark"},
        "key_refs": ["Acts 12:12", "Acts 12:25", "Colossians 4:10", "Acts 13:13", "2 Timothy 4:11"]
    },
    "mark-gospel-according-to": {
        "id": "mark-gospel-according-to",
        "term": "Mark, Gospel according to",
        "category": "concepts",
        "intro": "<p>The Gospel according to Mark is the second book of the New Testament and, by most modern assessments, the earliest of the four Gospels, probably written in Rome in the late 50s or early 60s A.D. It is the shortest and most action-oriented Gospel, characterized by rapid narrative movement (the Greek word <em>euthys</em>, meaning <em>immediately</em>, appears some forty times), vivid eyewitness detail, and an emphasis on Jesus's deeds rather than his teaching. The Gospel opens with John the Baptist's ministry, moves directly to Jesus's baptism and temptation, and sustains an urgent pace through healing, exorcism, and controversy until the extended Passion narrative that occupies roughly a third of the book.</p><p>Ancient tradition from Papias (quoted by Eusebius) states that Mark recorded Peter's preaching accurately though not in strict chronological order, which accounts for both its immediacy and its selective coverage. The Gospel's ending at 16:8, with the women fleeing the empty tomb in fear, is textually supported as the original conclusion — the longer endings (16:9–20) are widely regarded as later additions. Mark's portrait of Jesus centers on his authority as the Son of God and suffering Son of Man.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mark-gospel-according-to", "smith": "mark-gospel-according-to", "isbe": "mark-gospel-according-to"},
        "key_refs": ["Mark 1:1", "Mark 1:14", "Mark 15:21"]
    },
    "market-place": {
        "id": "market-place",
        "term": "Market-place",
        "category": "concepts",
        "intro": "<p>The market-place (<em>agora</em> in Greek) was the central public square of ancient cities, serving as the hub of commerce, civic life, legal proceedings, and philosophical discussion. In the New Testament, the <em>agora</em> appears as a space where Jesus and the apostles encountered ordinary people: Jesus observed children calling to one another there (Matthew 11:16), and Paul engaged in daily dialogue with Athenians in the <em>agora</em> before his address on the Areopagus (Acts 17:17). It was also in the market-place of Philippi that Paul and Silas were seized, beaten, and imprisoned after casting out a demon from a slave girl (Acts 16:19).</p><p>Ezekiel uses the market-place metaphorically to describe Tyre's commercial empire and its exchange with surrounding nations (Ezekiel 27:13). In the social world of the Gospels, market-places were also sites where day laborers waited to be hired (Matthew 20:3) and where the sick were laid for Jesus to heal (Mark 6:56), marking them as ordinary spaces that became scenes of divine intervention.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "market-place"},
        "key_refs": ["Matthew 11:16", "Matthew 20:3", "Acts 16:19", "Acts 17:17"]
    },
    "maroth": {
        "id": "maroth",
        "term": "Maroth",
        "category": "places",
        "intro": "<p>Maroth (meaning <em>bitterness</em>) was a town in the Shephelah of Judah, mentioned only in Micah 1:12 in the prophet's lament over the Assyrian advance. Micah depicts its inhabitants as waiting anxiously for good news but receiving only disaster, with calamity descending from the LORD to the gate of Jerusalem. The name's meaning — bitterness — is woven into Micah's series of puns on Judean town names, in which each city's name resonates ironically with its coming fate.</p>",
        "hitchcock_meaning": "bitterness",
        "source_ids": {"easton": "maroth", "smith": "maroth"},
        "key_refs": ["Micah 1:12"]
    },
    "marriage": {
        "id": "marriage",
        "term": "Marriage",
        "category": "concepts",
        "intro": "<p>Marriage, as defined in Scripture, is the covenantal union of one man and one woman, instituted by God at creation when he brought Eve to Adam and Adam declared her \"bone of my bones and flesh of my flesh\" (Genesis 2:23). This narrative establishes marriage as the foundational human relationship: a man shall leave father and mother and cleave to his wife so that the two become one flesh (Genesis 2:24). Jesus appeals explicitly to this creation ordinance when rejecting divorce (Matthew 19:4–6), and Paul cites the same text to ground the sanctity of the body (1 Corinthians 6:16).</p><p>Marriage in Scripture functions both as a social institution and a theological symbol. The Old Testament prophets — especially Hosea, Jeremiah, and Ezekiel — depict Israel's covenant relationship with God as a marriage, Israel's idolatry as adultery, and the restoration of the relationship in marital terms. The New Testament carries this forward: Paul compares the husband-wife bond to Christ's love for the church (Ephesians 5:25–32), and Revelation concludes with the marriage supper of the Lamb (Revelation 19:7–9), presenting the eschatological union of Christ and his people as the fulfillment toward which earthly marriage points.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "marriage", "smith": "marriage", "isbe": "marriage"},
        "key_refs": ["Genesis 2:18", "Matthew 19:4", "Matthew 19:5", "1 Corinthians 6:16", "Genesis 4:19"]
    },
    "marriage-feasts": {
        "id": "marriage-feasts",
        "term": "Marriage-feasts",
        "category": "concepts",
        "intro": "<p>Marriage-feasts in the ancient Near East were extended celebrations lasting seven to fourteen days, marked by music, rejoicing, and elaborate hospitality. The failure to honor such celebrations was a serious social breach. In the New Testament, the wedding at Cana — where Jesus performed his first recorded miracle by turning water into wine (John 2:1–11) — occurred in this festive context. The supply and quality of wine reflected the host's honor, and its failure at Cana provided the occasion for Jesus's disclosure of his glory.</p><p>Jesus drew extensively on the imagery of marriage feasts in his parables. The parable of the wedding banquet (Matthew 22:1–14) and the parable of the ten virgins (Matthew 25:1–13) use the marriage feast as the primary image for the kingdom of God and the urgency of readiness for the king's arrival. This imagery converges in Revelation 19:7–9, where the ultimate marriage supper of the Lamb is announced as the eschatological celebration awaiting God's redeemed people.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "marriage-feasts", "smith": "marriage-feasts"},
        "key_refs": ["John 2:1", "Matthew 22:2", "Revelation 19:7"]
    },
    "mars-hill": {
        "id": "mars-hill",
        "term": "Mars Hill",
        "category": "places",
        "intro": "<p>Mars Hill (Greek <em>Areios Pagos</em>, the Hill of Ares, or Areopagus) was a rocky outcropping northwest of the Acropolis in Athens that served as the ancient seat of the Athenian high court. By Paul's day the court of the Areopagus also functioned as Athens's council for philosophical and religious oversight. When Paul preached in the Athenian agora and engaged Epicurean and Stoic philosophers, they brought him to the Areopagus to explain his teaching about Jesus and the resurrection (Acts 17:19–22).</p><p>Paul's address on Mars Hill — recorded in Acts 17:22–31 — is a masterwork of cross-cultural apologetics: he begins from a pagan altar inscription (\"To an Unknown God\"), reasons from creation and common human nature toward the God who commands repentance, and concludes with the resurrection of Jesus as the appointed judge of all humanity. The response was mixed: some mocked the resurrection, some deferred, and some believed — including Dionysius the Areopagite and a woman named Damaris (Acts 17:32–34).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mars-hill", "smith": "mars-hill", "isbe": "mars-hill"},
        "key_refs": ["Acts 17:22"]
    },
    "martha": {
        "id": "martha",
        "term": "Martha",
        "category": "people",
        "intro": "<p>Martha (meaning <em>who becomes bitter</em> or <em>a lady</em>) was the sister of Mary and Lazarus of Bethany, one of the families closest to Jesus during his ministry. She appears in two significant Gospel episodes. In Luke 10:38–42, Martha receives Jesus into her home and is \"cumbered about with much serving\" while her sister Mary sits at Jesus's feet; Jesus gently corrects her anxiety, affirming that Mary has chosen \"the good part.\" The contrast is not a rejection of service but a recognition of misplaced priorities.</p><p>Martha's second appearance at the resurrection of Lazarus (John 11) reveals a woman of substantial faith: she meets Jesus on the road with both grief and theological confidence, confessing \"I know that he shall rise again in the resurrection at the last day\" (John 11:24). Jesus's response — \"I am the resurrection and the life\" (John 11:25) — is elicited by Martha's dialogue and followed by her confession that he is \"the Christ, the Son of God, which should come into the world\" (John 11:27), one of the most complete Christological confessions in the Gospels.</p>",
        "hitchcock_meaning": "who becomes bitter; provoking",
        "source_ids": {"easton": "martha", "smith": "martha", "isbe": "martha"},
        "key_refs": ["Luke 10:38", "Luke 10:40", "Luke 10:41", "John 11:1", "John 11:25"]
    },
    "martyr": {
        "id": "martyr",
        "term": "Martyr",
        "category": "concepts",
        "intro": "<p>Martyr (Greek <em>martys</em>, meaning <em>witness</em>) underwent a significant semantic shift in the New Testament era. Originally denoting any witness to a fact or event, it came to refer specifically to those who bore witness to Jesus Christ by dying for their testimony. Stephen is the first Christian martyr, described in Acts 22:20 as Christ's witness (<em>martys</em>) at the time of his death. Antipas is similarly called \"my faithful martyr\" in Revelation 2:13, and Revelation 17:6 speaks of Babylon as drunk with the blood of the martyrs of Jesus.</p><p>The theological weight of martyrdom in early Christianity drew on Jesus's own death as the paradigmatic witness (Revelation 1:5 calls him \"the faithful witness\") and on his teaching that to lose one's life for his sake is to find it (Matthew 16:25). The martyrs occupy a place of honor in the eschatological vision of Revelation: their souls cry out under the altar (Revelation 6:9–11), and they reign with Christ in the first resurrection (Revelation 20:4).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "martyr", "isbe": "martyr"},
        "key_refs": ["Acts 22:20", "Revelation 2:13", "Revelation 17:6"]
    },
    "mary": {
        "id": "mary",
        "term": "Mary",
        "category": "people",
        "intro": "<p>Mary (Greek form of Hebrew <em>Miriam</em>, meaning <em>bitterness</em> or <em>myrrh of the sea</em>) is the most common woman's name in the New Testament, borne by at least six distinct women. The most significant is Mary of Nazareth, the mother of Jesus, a virgin betrothed to Joseph of the house of David (Luke 1:27). The angel Gabriel announced to her that she would conceive by the Holy Spirit and bear the Son of the Most High (Luke 1:31–35); her response — \"Behold the handmaid of the Lord; be it unto me according to thy word\" (Luke 1:38) — is the model of obedient faith. Her <em>Magnificat</em> (Luke 1:46–55) is among Scripture's most beautiful hymns of praise. She was present at the crucifixion (John 19:25–27) and in the upper room at Pentecost (Acts 1:14).</p><p>Other notable Marys include Mary Magdalene, from whom Jesus cast seven demons (Luke 8:2) and who was the first witness of the resurrection (John 20:11–18); Mary of Bethany, the sister of Martha and Lazarus, who anointed Jesus's feet (John 12:3); and Mary the mother of John Mark (Acts 12:12). The New Testament's concentrated presence of this name reflects the Greco-Roman Jewish world's veneration of Miriam as a significant ancestral figure.</p>",
        "hitchcock_meaning": "same as Miriam",
        "source_ids": {"easton": "mary", "smith": "mary", "isbe": "mary"},
        "key_refs": ["Matthew 2:11", "Luke 1:38", "Luke 1:46", "John 20:16", "Acts 1:14"]
    },
    "maschil": {
        "id": "maschil",
        "term": "Maschil",
        "category": "concepts",
        "intro": "<p>Maschil (Hebrew <em>maskil</em>, meaning <em>giving instruction</em> or <em>song of wisdom</em>) is a musical or literary term appearing in the superscriptions of thirteen psalms (Psalms 32, 42, 44, 45, 52–55, 74, 78, 88, 89, 142). Its precise meaning is debated: it may indicate a contemplative or didactic poem, a psalm intended to make its singers or hearers wise, or a particular musical performance style. The word derives from the verb <em>sakal</em>, meaning to act with prudence or insight.</p><p>The psalms bearing this title vary widely in content — they include laments (Psalm 88), historical retrospectives (Psalm 78), royal hymns (Psalm 45), and cries of desperation (Psalm 142) — suggesting that <em>maskil</em> may designate literary quality or reflective depth rather than a single genre or liturgical function. Paul's instruction to sing psalms and \"make melody in your heart\" (Ephesians 5:19; Colossians 3:16) reflects the broader tradition of thoughtful, wisdom-saturated song that the <em>maskil</em> psalms exemplify.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "maschil", "smith": "maschil"},
        "key_refs": ["Psalms 47:7", "Psalms 32:1", "Psalms 78:1"]
    },
    "mash": {
        "id": "mash",
        "term": "Mash",
        "category": "people",
        "intro": "<p>Mash (meaning <em>drawn out</em>) was one of the sons of Aram, the son of Shem, listed in the table of nations in Genesis 10:23. He is called Meshech in the parallel genealogy of 1 Chronicles 1:17, and scholars have associated him with peoples of the region between Mesopotamia and the Taurus Mountains, possibly the Mashu mountains known from Assyrian sources. As a figure in the table of nations, Mash represents one of the clans descended from Noah through the Semitic line, but no further narrative details are preserved in Scripture.</p>",
        "hitchcock_meaning": "same as Meshech",
        "source_ids": {"easton": "mash", "smith": "mash"},
        "key_refs": ["Genesis 10:23", "1 Chronicles 1:17"]
    },
    "mashal": {
        "id": "mashal",
        "term": "Mashal",
        "category": "places",
        "intro": "<p>Mashal (meaning <em>a parable</em> or <em>governing</em>) was a Levitical city in the territory of Asher, assigned to the Gershonite Levites (1 Chronicles 6:74). It is called Mishal in Joshua 21:30. The city illustrates the system by which Levitical towns were distributed throughout the tribal territories so that priestly ministry would be accessible across Israel, rather than concentrated in a single location.</p>",
        "hitchcock_meaning": "a parable; governing",
        "source_ids": {"easton": "mashal", "smith": "mashal"},
        "key_refs": ["1 Chronicles 6:74", "Joshua 21:30"]
    },
    "mason": {
        "id": "mason",
        "term": "Mason",
        "category": "concepts",
        "intro": "<p>Masons — skilled workers in stone — played a vital role in the major building projects of ancient Israel. When David established his court in Jerusalem, Hiram king of Tyre sent masons along with cedar to build David's palace (2 Samuel 5:11). Solomon's construction of the temple required massive quarrying and dressing of stone: the text notes that Hiram's builders and Solomon's builders \"hewed\" (prepared) the stones, working stone so precisely that \"neither hammer nor axe nor any tool of iron was heard in the house while it was in building\" (1 Kings 6:7). Stone was the primary building material for permanent structures, and skilled masons were prized craftsmen in royal employ.</p><p>The post-exilic restoration under Ezra also employed masons for the temple rebuilding (Ezra 3:7), and Nehemiah's reconstruction of Jerusalem's walls relied on organized teams of builders working under threat of attack. The New Testament uses the image of stone-building metaphorically: Jesus identifies himself as the cornerstone the builders rejected (Matthew 21:42), and Peter extends the image to believers as living stones being built into a spiritual house (1 Peter 2:5).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mason", "smith": "mason"},
        "key_refs": ["1 Kings 5:17", "1 Kings 5:18", "2 Samuel 5:11"]
    },
    "masrekah": {
        "id": "masrekah",
        "term": "Masrekah",
        "category": "places",
        "intro": "<p>Masrekah was a city in Edom, mentioned in the list of Edomite kings who ruled before any king reigned over Israel (Genesis 36:36; 1 Chronicles 1:47). It was the home of Samlah, one of the pre-Israelite kings of Edom. The name may be connected with the Hebrew word for a vine-garden or vine-dresser. Its precise location has not been firmly identified.</p>",
        "hitchcock_meaning": "whistling; hissing",
        "source_ids": {"easton": "masrekah", "smith": "masrekah"},
        "key_refs": ["Genesis 36:36", "1 Chronicles 1:47"]
    },
    "massa": {
        "id": "massa",
        "term": "Massa",
        "category": "people",
        "intro": "<p>Massa (meaning <em>a burden</em> or <em>prophecy</em>) was a son of Ishmael and grandson of Abraham (Genesis 25:14), listed among the twelve princes of the Ishmaelite tribes. The Massaites settled in Arabia, and some scholars have associated the term <em>massa</em> (which in Hebrew also means an oracle or prophetic utterance) with the word used in the superscriptions of Proverbs 30–31, where the \"words of Agur\" and the \"words of King Lemuel\" are each described as a <em>massa</em> — possibly indicating Massa as an Arabian kingdom that produced its own wisdom tradition.</p>",
        "hitchcock_meaning": "a burden; prophecy",
        "source_ids": {"easton": "massa", "smith": "massa"},
        "key_refs": ["Genesis 25:14"]
    },
    "massah": {
        "id": "massah",
        "term": "Massah",
        "category": "places",
        "intro": "<p>Massah (meaning <em>temptation</em> or <em>testing</em>) was the name given to Rephidim, where the Israelites quarreled with Moses over the lack of water and put the LORD to the test, demanding \"Is the LORD among us, or not?\" (Exodus 17:7). Moses struck the rock at Horeb and water came forth; the site was given the double name Massah and Meribah (meaning <em>contention</em>) to memorialize both Israel's testing of God and their contention with Moses.</p><p>Massah became a byword for faithless rebellion in later Scripture. Deuteronomy 6:16 warns Israel not to put the LORD to the test as at Massah, and Psalm 95:8–9 calls the wilderness generation to account: \"Harden not your heart, as in the provocation, as in the day of temptation in the wilderness, when your fathers tempted me, proved me, and saw my work.\" The New Testament applies this warning directly: Jesus quotes Deuteronomy 6:16 in refusing Satan's temptation at the pinnacle of the temple (Matthew 4:7), and Hebrews 3:8 applies Psalm 95 to warn the church against the same unbelief.</p>",
        "hitchcock_meaning": "temptation",
        "source_ids": {"easton": "massah", "smith": "massah"},
        "key_refs": ["Exodus 17:7", "Deuteronomy 6:16", "Psalms 95:8", "Hebrews 3:8"]
    },
    "mattan": {
        "id": "mattan",
        "term": "Mattan",
        "category": "people",
        "intro": "<p>Mattan (meaning <em>a gift</em>) is the name of two biblical figures. The first was the priest of Baal in Jerusalem who was slain before his altars when Jehoiada the priest led the coup that overthrew Athaliah and restored Joash to the throne of Judah (2 Kings 11:18). The second was one of the princes of Judah in the reign of Zedekiah who cast the prophet Jeremiah into a muddy cistern (Jeremiah 38:1–6). The name also appears in the ancestry of Joseph, the husband of Mary (Matthew 1:15).</p>",
        "hitchcock_meaning": "a gift",
        "source_ids": {"easton": "mattan", "smith": "mattan"},
        "key_refs": ["2 Kings 11:18", "Jeremiah 38:1", "Matthew 1:15"]
    },
    "mattanah": {
        "id": "mattanah",
        "term": "Mattanah",
        "category": "places",
        "intro": "<p>Mattanah was a station in Israel's wilderness journey, mentioned between Beer and Nahaliel in the itinerary of Numbers 21:18–19 as the Israelites moved through Moabite territory toward the plains of Moab. The name means <em>a gift</em> and may be connected with the well of Beer, where the people sang a song celebrating the gift of water (Numbers 21:17). Its precise location in the Moabite highlands has not been identified with certainty.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mattanah", "smith": "mattanah"},
        "key_refs": ["Numbers 21:18", "Numbers 21:19"]
    },
    "mattaniah": {
        "id": "mattaniah",
        "term": "Mattaniah",
        "category": "people",
        "intro": "<p>Mattaniah (meaning <em>gift of the LORD</em>) is a name borne by several biblical figures. The most historically significant was the original name of Zedekiah, the last king of Judah: Nebuchadnezzar changed his name from Mattaniah to Zedekiah when he installed him as a puppet king after the deportation of Jehoiachin (2 Kings 24:17). Another notable Mattaniah was a Levite musician in the temple, a son of Asaph appointed by David for worship ministry (1 Chronicles 25:4, 16; 2 Chronicles 29:13).</p>",
        "hitchcock_meaning": "gift, or hope, of the Lord",
        "source_ids": {"easton": "mattaniah", "smith": "mattaniah"},
        "key_refs": ["2 Kings 24:17", "1 Chronicles 25:4", "2 Chronicles 29:13"]
    },
    "mattathias": {
        "id": "mattathias",
        "term": "Mattathias",
        "category": "people",
        "intro": "<p>Mattathias (Greek form of Hebrew <em>Mattithiah</em>, meaning <em>the gift of the LORD</em>) is the name of two individuals in the ancestry of Jesus as recorded in Luke 3: one is listed as the son of Amos (Luke 3:25), and another as the son of Semei (Luke 3:26). Outside Scripture, Mattathias is most famous as the priest of Modin whose refusal to offer pagan sacrifice in 167 B.C. ignited the Maccabean revolt against Antiochus IV Epiphanes — an event in the intertestamental period that preserved Jewish worship and Temple observance.</p>",
        "hitchcock_meaning": "the gift of the Lord",
        "source_ids": {"easton": "mattathias", "smith": "mattathias"},
        "key_refs": ["Luke 3:25", "Luke 3:26"]
    },
    "matthan": {
        "id": "matthan",
        "term": "Matthan",
        "category": "people",
        "intro": "<p>Matthan (meaning <em>a gift</em>) was the grandfather of Joseph, the husband of Mary, according to the genealogy in Matthew 1:15. He was the son of Eleazar and the father of Jacob, who was the father of Joseph. Matthan thus appears in the royal Davidic line leading to Jesus's legal father. The name is a shortened form of Mattaniah.</p>",
        "hitchcock_meaning": "same as Mattan",
        "source_ids": {"easton": "matthan", "smith": "matthan"},
        "key_refs": ["Matthew 1:15"]
    },
    "matthat": {
        "id": "matthat",
        "term": "Matthat",
        "category": "people",
        "intro": "<p>Matthat (meaning <em>gift of God</em>, a form of Matthan) is the name of two ancestors of Jesus in the genealogy recorded in Luke 3. One Matthat was the son of Levi and father of Heli (Luke 3:24), and another was the son of Levi and father of Jorim further back in the line (Luke 3:29). Both appear in the Lukan genealogy tracing Jesus's descent through David and the patriarchs to Adam.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "matthat", "smith": "matthat"},
        "key_refs": ["Luke 3:24", "Luke 3:29"]
    },
    "matthew": {
        "id": "matthew",
        "term": "Matthew",
        "category": "people",
        "intro": "<p>Matthew (Hebrew <em>Mattityahu</em>, meaning <em>gift of the LORD</em>; also called Levi, son of Alphaeus) was a tax collector (<em>telones</em>) at Capernaum when Jesus called him with the simple command \"Follow me\" (Matthew 9:9; Mark 2:14). As a collector of Roman taxes from his own countrymen, Matthew occupied a position of social contempt among observant Jews — tax collectors were regarded as collaborators with Roman occupation and ceremonially unclean. His response to Jesus's call was immediate: he left his tax booth and, as Luke reports, gave a great feast in Jesus's honor, bringing together \"a great company of publicans and others\" (Luke 5:29).</p><p>Matthew was numbered among the Twelve Apostles (Matthew 10:3; Acts 1:13) and is credited by the church's earliest tradition with authoring the first Gospel. Papias (as preserved by Eusebius) states that Matthew compiled the oracles of the Lord in the Hebrew language, and while the relationship between this statement and the Greek Gospel of Matthew has long been debated, the Gospel that bears his name is marked by its Jewish-Christian perspective, its organized blocks of teaching (including the Sermon on the Mount), and its extensive use of Old Testament fulfillment quotations.</p>",
        "hitchcock_meaning": "given; a reward",
        "source_ids": {"easton": "matthew", "smith": "matthew", "isbe": "matthew"},
        "key_refs": ["Matthew 9:9", "Mark 2:14", "Luke 5:27", "Luke 5:29", "Acts 1:13"]
    },
    "matthew-gospel-according-to": {
        "id": "matthew-gospel-according-to",
        "term": "Matthew, Gospel according to",
        "category": "concepts",
        "intro": "<p>The Gospel according to Matthew is the first book of the New Testament and the most quoted Gospel in the early church. Written with a strongly Jewish-Christian perspective, it presents Jesus above all as the fulfillment of the Hebrew Scriptures, weaving more than sixty direct citations and allusions to the Old Testament through its narrative. Its five major teaching blocks — the Sermon on the Mount (chapters 5–7), the Missionary Discourse (10), the Parables of the Kingdom (13), the Community Discourse (18), and the Olivet Discourse (24–25) — are commonly thought to mirror the five books of Moses, presenting Jesus as the new and greater Moses delivering the new law from a mountain.</p><p>Matthew's Gospel opens with a genealogy connecting Jesus to Abraham and David, and closes with the Great Commission sending the disciples to make disciples of all nations — a movement from Jewish roots to universal scope. Its distinctive material includes the visit of the Magi, Joseph's dreams, the Sermon on the Mount, the parable of the talents, and the final judgment scene of Matthew 25:31–46. The Gospel was almost certainly the primary catechetical text of the early church, reflecting its formative role in Christian worship, teaching, and mission.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "matthew-gospel-according-to", "smith": "matthew-gospel-according-to", "isbe": "matthew-gospel-according-to"},
        "key_refs": ["Matthew 1:1", "Matthew 5:1", "Matthew 28:19"]
    },
    "matthias": {
        "id": "matthias",
        "term": "Matthias",
        "category": "people",
        "intro": "<p>Matthias (meaning <em>gift of God</em>, same root as Mattathias) was the apostle elected to replace Judas Iscariot following his betrayal and death. The account in Acts 1:15–26 describes the process: Peter, citing Psalms 69 and 109, proposed that the vacancy be filled by one who had accompanied the disciples throughout Jesus's ministry and who had witnessed the resurrection. Two men qualified — Joseph called Barsabas (Justus) and Matthias — and the apostles cast lots, with the lot falling to Matthias (Acts 1:23–26). This is the only biblical account of the use of the lot to determine divine choice within the apostolic community, and no further mention of Matthias appears in the New Testament after his election.</p>",
        "hitchcock_meaning": "same as Mattathias",
        "source_ids": {"easton": "matthias", "smith": "matthias"},
        "key_refs": ["Acts 1:23", "Acts 1:26"]
    },
    "mattithiah": {
        "id": "mattithiah",
        "term": "Mattithiah",
        "category": "people",
        "intro": "<p>Mattithiah (meaning <em>gift of the LORD</em>) was a Levite of the Kohathite clan, the firstborn son of Shallum, who had charge of the flat cakes offered to God in the tabernacle and temple (1 Chronicles 9:31). Another Mattithiah was a musician appointed by David for the service of song before the ark, playing a psaltery (1 Chronicles 25:3, 21). A Mattithiah is also mentioned among the Levites who assisted Ezra when he read the Law to the returned exiles (Nehemiah 8:4), and the name appears twice in the Lukan genealogy of Jesus (Luke 3:25–26).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mattithiah", "smith": "mattithiah"},
        "key_refs": ["1 Chronicles 25:3", "1 Chronicles 9:31", "Nehemiah 8:4"]
    },
    "mattock": {
        "id": "mattock",
        "term": "Mattock",
        "category": "concepts",
        "intro": "<p>A mattock was an agricultural digging tool similar to a hoe or pickaxe, used for breaking hard ground, cultivating vineyards, and clearing land. Isaiah 7:25 refers to hills that had been worked with mattocks being given over to briers and thorns following the Assyrian devastation of the land. The Philistines' monopoly on iron-working required Israelites to come to them to sharpen their mattocks along with other iron tools, giving them a military and agricultural advantage over Israel during Saul's reign (1 Samuel 13:20–21).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mattock", "smith": "mattock"},
        "key_refs": ["Isaiah 7:25", "1 Samuel 13:20"]
    },
    "maul": {
        "id": "maul",
        "term": "Maul",
        "category": "concepts",
        "intro": "<p>A maul (Hebrew <em>mepits</em>) was a heavy war club or hammer used as a weapon, comparable to a battleaxe. The word appears in Proverbs 25:18, where a man who gives false testimony against his neighbor is compared to \"a maul, and a sword, and a sharp arrow\" — instruments of violent destruction. The image conveys the devastating, blunt-force damage that slander and false witness inflict on human relationships and reputation, no less lethal than a physical weapon.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "maul", "smith": "maul"},
        "key_refs": ["Proverbs 25:18"]
    },
    "mazzaroth": {
        "id": "mazzaroth",
        "term": "Mazzaroth",
        "category": "concepts",
        "intro": "<p>Mazzaroth (Hebrew <em>mazzarot</em>) appears in God's challenge to Job: \"Canst thou bring forth Mazzaroth in his season?\" (Job 38:32). Most translations understand it as a reference to the twelve signs of the zodiac or the constellations of the night sky in their seasonal progression — related to the Babylonian <em>manzazu</em> or the Hebrew <em>mazzalot</em> (2 Kings 23:5), the term for the zodiacal signs condemned by Josiah's reform as objects of idolatrous veneration. God's use of Mazzaroth in his speech to Job is not an endorsement of astrology but a rhetorical demonstration of divine sovereignty over the heavens: only God controls the orderly procession of the stars in their seasons, a power infinitely beyond human comprehension.</p>",
        "hitchcock_meaning": "the twelve signs of the zodiac",
        "source_ids": {"easton": "mazzaroth", "smith": "mazzaroth"},
        "key_refs": ["Job 38:32", "2 Kings 23:5"]
    },
    "me-jarkon": {
        "id": "me-jarkon",
        "term": "Me-jarkon",
        "category": "places",
        "intro": "<p>Me-jarkon (meaning <em>the waters of Jarkon</em> or <em>yellowish water</em>) was a place on the border of Dan's territory in the coastal region near Joppa, mentioned in Joshua 19:46. It is identified with the Nahr el-Auja (the Yarkon River), which flows westward into the Mediterranean north of Joppa. The river formed a natural boundary feature and its waters gave the area its name. Dan's territory in this region was never fully settled, as the tribe was unable to dispossess the Amorites and eventually migrated north (Judges 1:34–35; 18).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "me-jarkon", "smith": "me-jarkon"},
        "key_refs": ["Joshua 19:46"]
    },
    "meadow": {
        "id": "meadow",
        "term": "Meadow",
        "category": "concepts",
        "intro": "<p>Meadow in the Old Testament translates two distinct Hebrew words. In Genesis 41:2, 18 the word <em>achu</em> — likely borrowed from Egyptian — refers to the reedy marshland of the Nile Delta where Pharaoh's cows grazed in his dream, indicating a lush, water-fed pasturage. In Judges 20:33 the \"meadow of Gibeah\" (Hebrew <em>maareh</em>) refers to a plain or open area used in the ambush of Gibeah by the Israelite tribes. The imagery of green meadows and lush pasture also functions symbolically in Scripture: Psalm 23's \"green pastures\" use related language to depict God's provision and rest for his people.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "meadow", "smith": "meadow"},
        "key_refs": ["Genesis 41:2", "Genesis 41:18", "Judges 20:33"]
    },
    "meah": {
        "id": "meah",
        "term": "Meah",
        "category": "places",
        "intro": "<p>Meah (meaning <em>a hundred</em> or <em>a hundred cubits</em>) was a tower in Jerusalem near the Sheep Gate, mentioned in Nehemiah's account of the city's wall construction (Nehemiah 3:1). It lay between the Sheep Gate and the Tower of Hananeel, along the northern section of the city wall. Its name — \"the hundred\" — may refer to its height of one hundred cubits or to the hundred steps by which it was ascended. The tower was rebuilt as part of Nehemiah's restoration of Jerusalem's defenses after the return from Babylonian exile.</p>",
        "hitchcock_meaning": "a hundred cubits",
        "source_ids": {"easton": "meah", "smith": "meah"},
        "key_refs": ["Nehemiah 3:1"]
    },
    "meals": {
        "id": "meals",
        "term": "Meals",
        "category": "concepts",
        "intro": "<p>Meals in the biblical world carried rich social and ceremonial significance beyond simple nourishment. Sharing a meal was an act of covenant fellowship: to eat with someone was to declare solidarity and peace, which is why the Pharisees objected to Jesus eating with tax collectors and sinners (Luke 5:30; Mark 2:16). Ancient Near Eastern meals typically consisted of two main times — a morning meal (relatively light) and an evening meal (the primary meal of the day). Guests reclined on couches in the Greco-Roman period, with the host occupying a place of honor and guests arranged by social rank — a seating protocol Jesus subverted in his teaching (Luke 14:7–11).</p><p>The most theologically significant biblical meal is the Passover, instituted at the Exodus and transformed by Jesus into the Lord's Supper at the Last Supper (1 Corinthians 11:23–26). Meals in Jesus's ministry consistently carry theological weight: the feeding of the five thousand (John 6), the feeding of the four thousand (Matthew 15), table fellowship with sinners, the post-resurrection meals with disciples (Luke 24:30–31; John 21:12–13) — all reflect the kingdom of God as a feast hosted by God for his people.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "meals", "smith": "meals"},
        "key_refs": ["Luke 7:36", "Luke 14:7", "1 Corinthians 11:23"]
    },
    "mearah": {
        "id": "mearah",
        "term": "Mearah",
        "category": "places",
        "intro": "<p>Mearah (meaning <em>a cave</em> or <em>making empty</em>) was a place near Sidon mentioned in Joshua 13:4 as part of the land that remained to be possessed after Joshua's initial campaigns. It appears in the list of territory belonging to the Sidonians that Israel had not yet taken at the time of Joshua's old age. The exact location is uncertain, though it may be identified with a region of caverns in the slopes of the Lebanon mountains near Sidon.</p>",
        "hitchcock_meaning": "den; cave; making empty",
        "source_ids": {"easton": "mearah", "smith": "mearah"},
        "key_refs": ["Joshua 13:4"]
    },
    "measure": {
        "id": "measure",
        "term": "Measure",
        "category": "concepts",
        "intro": "<p>Biblical systems of measurement encompassed both linear distances and dry and liquid volumes. Hebrew linear measures included the cubit (approximately 18 inches, from elbow to fingertip), the span (half a cubit), the handbreadth, and the finger. Volume measures included the homer (the largest dry measure, approximately 6–7 bushels), the ephah (one-tenth of a homer), the omer (one-tenth of an ephah), the cab, and the log. The prophets invoked standard measurements as symbols of divine judgment: Isaiah 5:14 depicts Sheol opening without measure, and Jeremiah 13:25 speaks of the measured portion God apportions as judgment. Honest weights and measures were a matter of covenant faithfulness, as false balances were an abomination to the LORD (Proverbs 11:1; Leviticus 19:35–36).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "measure", "smith": "measure"},
        "key_refs": ["Isaiah 5:14", "Leviticus 19:35", "Proverbs 11:1"]
    },
    "meat-offering": {
        "id": "meat-offering",
        "term": "Meat-offering",
        "category": "concepts",
        "intro": "<p>The meat-offering (Hebrew <em>minchah</em>, better translated <em>grain offering</em>) was one of the five major Levitical offerings prescribed in the Law. Despite its English name, it contained no meat; it consisted of fine flour, oil, frankincense, and salt, offered either raw, baked in an oven, cooked on a griddle, or fried. Leaven and honey were prohibited, while salt — the symbol of covenant — was required (Leviticus 2:11–13). A handful (<em>azkarah</em>, the memorial portion) was burned on the altar as a sweet savor to God; the remainder was eaten by Aaron and his sons as most holy food.</p><p>The grain offering typically accompanied burnt offerings and peace offerings, and its required quantities are specified for various festivals and daily temple worship in Numbers 28–29. The <em>minchah</em> was also the evening sacrifice that accompanied the daily burnt offering, giving rise to the \"hour of the evening oblation\" as a regular time of prayer (Ezra 9:5; Daniel 9:21). Malachi 1:11 prophesies that in every place pure offerings (<em>minchah</em>) will be offered to God's name among the nations — a text early Christians applied to the Eucharist.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "meat-offering", "smith": "meat-offering", "isbe": "meat-offering"},
        "key_refs": ["Leviticus 2:1", "Exodus 29:40", "Ezra 9:5", "Malachi 1:11"]
    },
    "mebunnai": {
        "id": "mebunnai",
        "term": "Mebunnai",
        "category": "people",
        "intro": "<p>Mebunnai (meaning <em>son</em>, <em>building</em>, or <em>understanding of the LORD</em>) was one of David's thirty mighty warriors, a Hushathite from the clan of Hushah in Judah (2 Samuel 23:27). He is called Sibbecai the Hushathite in the parallel list of 1 Chronicles 11:29 and in the accounts of the Philistine wars, where he slew Saph (or Sippai), a descendant of the giants (2 Samuel 21:18; 1 Chronicles 20:4). He also served as the military commander for the eighth monthly division of David's army (1 Chronicles 27:11).</p>",
        "hitchcock_meaning": "son; building; understanding",
        "source_ids": {"easton": "mebunnai", "smith": "mebunnai"},
        "key_refs": ["2 Samuel 23:27", "1 Chronicles 11:29"]
    },
    "medad": {
        "id": "medad",
        "term": "Medad",
        "category": "people",
        "intro": "<p>Medad (meaning <em>he that measures</em> or <em>water of love</em>) was one of the seventy elders appointed by Moses to share the burden of leadership over Israel in the wilderness (Numbers 11:16–17). Along with Eldad, Medad remained in the camp rather than going to the tabernacle, yet the Spirit rested on him and he prophesied among the people. When Joshua urged Moses to stop them, Moses replied: \"Enviest thou for my sake? would God that all the LORD's people were prophets, and that the LORD would put his spirit upon them!\" (Numbers 11:29) — a remarkable statement of prophetic hope fulfilled at Pentecost (Acts 2).</p>",
        "hitchcock_meaning": "he that measures; water of love",
        "source_ids": {"easton": "medad", "smith": "medad"},
        "key_refs": ["Numbers 11:26", "Numbers 11:29"]
    },
    "medan": {
        "id": "medan",
        "term": "Medan",
        "category": "people",
        "intro": "<p>Medan (meaning <em>judgment</em> or <em>process</em>) was the third son of Abraham by Keturah, the wife Abraham took after Sarah's death (Genesis 25:2). He is listed among the six sons who were sent away eastward with gifts, keeping them separate from Isaac as the heir of promise (Genesis 25:6). The Medanites are possibly connected with the Midianites and may have been an Arabian tribe; some ancient texts use Medan and Midian interchangeably, as in Genesis 37:28–36 where the brothers who sold Joseph are called both Midianites and Medanites.</p>",
        "hitchcock_meaning": "judgment; process",
        "source_ids": {"easton": "medan", "smith": "medan"},
        "key_refs": ["Genesis 25:2"]
    },
    "mede": {
        "id": "mede",
        "term": "Mede",
        "category": "people",
        "intro": "<p>The Medes were an ancient Indo-European people descended from Madai, son of Japheth (Genesis 10:2), who established the Median kingdom in the region southeast of the Caspian Sea, corresponding to northwestern Iran. They rose to prominence by helping destroy Nineveh in 612 B.C., ending the Assyrian Empire. Israelite exiles were settled among the cities of the Medes (2 Kings 17:6; 18:11), and Daniel served under \"Darius the Mede\" after Babylon fell. The Persians and Medes are consistently paired in the Book of Esther and Daniel as the dual ruling power of the Achaemenid Empire — the laws of the Medes and Persians being irrevocable (Daniel 6:8; Esther 1:19).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mede", "smith": "mede", "isbe": "mede"},
        "key_refs": ["Genesis 10:2", "2 Kings 17:6", "Daniel 11:1"]
    },
    "medeba": {
        "id": "medeba",
        "term": "Medeba",
        "category": "places",
        "intro": "<p>Medeba (meaning <em>waters of rest</em> or <em>waters springing up</em>) was a town on the high Moabite plateau east of the Jordan, originally Moabite, later conquered by Sihon the Amorite king (Numbers 21:30), and assigned by Moses to the tribe of Reuben (Joshua 13:16). It figures in accounts of Israelite warfare: the Ammonite army camped at Medeba when David's forces defeated them (1 Chronicles 19:7), and Isaiah's oracle against Moab (Isaiah 15) mentions its grief. The town later reverted to Moabite control and was celebrated in the Mesha Stele, where Mesha king of Moab boasts of taking it back from Israel.</p>",
        "hitchcock_meaning": "waters of grief; waters springing up",
        "source_ids": {"easton": "medeba", "smith": "medeba"},
        "key_refs": ["Numbers 21:30", "Joshua 13:16", "1 Chronicles 19:7"]
    },
    "media": {
        "id": "media",
        "term": "Media",
        "category": "places",
        "intro": "<p>Media was the ancient kingdom of the Medes, occupying the mountainous region southeast of the Caspian Sea and northwest of Persia — roughly corresponding to northwestern and western Iran. Descended from Madai the son of Japheth (Genesis 10:2), the Medes built an empire that reached its peak under Cyaxares, who allied with Babylon to destroy Nineveh in 612 B.C. Media later merged with Persia under Cyrus the Great, and the resulting Medo-Persian Empire is consistently called the empire of the Medes and Persians in Esther and Daniel.</p><p>Israelite and Judahite exiles were settled in the cities of the Medes following the Assyrian conquests (2 Kings 17:6; 18:11). Daniel's apocalyptic visions identify the Median kingdom as the second great world empire (Daniel 8:20), and the laws of the Medes and Persians — irrevocable by royal decree — appear prominently in the stories of Daniel and Esther (Daniel 6:8; Esther 1:19). Isaiah 13:17 and 21:2 call the Medes as God's instrument to overthrow Babylon.</p>",
        "hitchcock_meaning": "measure; habit; covering",
        "source_ids": {"easton": "media", "smith": "media", "isbe": "media"},
        "key_refs": ["Genesis 10:2", "2 Kings 17:6", "Esther 1:3", "Daniel 8:20"]
    },
    "mediator": {
        "id": "mediator",
        "term": "Mediator",
        "category": "concepts",
        "intro": "<p>A mediator (Greek <em>mesites</em>, from <em>mesos</em>, middle) is an intermediary who stands between two parties to effect reconciliation or agreement. The concept pervades both Testaments. Moses functioned as mediator of the Mosaic covenant, standing between God and Israel at Sinai (Deuteronomy 5:5; Galatians 3:19). Job longed for an umpire (daysman) who could stand between him and God (Job 9:33). The entire Levitical priesthood mediated atonement through sacrifice, maintaining the covenant relationship between a holy God and a sinful people.</p><p>The New Testament declares that Christ is the singular mediator of the new covenant: \"For there is one God, and one mediator between God and men, the man Christ Jesus; who gave himself a ransom for all\" (1 Timothy 2:5). Hebrews 8:6; 9:15; and 12:24 call Jesus the mediator of a better covenant established on better promises, ratified by his blood. His mediation is not merely procedural but substitutionary and atoning: he stands between God's righteous wrath and sinful humanity by bearing the judgment himself, and now intercedes for believers at God's right hand (Hebrews 7:25; Romans 8:34).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mediator", "smith": "mediator", "isbe": "mediator"},
        "key_refs": ["1 Timothy 2:5", "Hebrews 8:6", "Hebrews 9:15", "Hebrews 12:24"]
    },
    "meekness": {
        "id": "meekness",
        "term": "Meekness",
        "category": "concepts",
        "intro": "<p>Meekness (Hebrew <em>anawah</em>; Greek <em>prautes</em>) is the quality of gentle strength and humble submission — not weakness, but power held under control in deference to God and in consideration of others. Moses is described as \"very meek, above all the men which were upon the face of the earth\" (Numbers 12:3), and Jesus invites the weary: \"I am meek and lowly in heart\" (Matthew 11:29). The third Beatitude promises that \"the meek shall inherit the earth\" (Matthew 5:5), an echo of Psalm 37:11, where the anawim — the poor and lowly who trust God — are promised possession of the land.</p><p>Meekness appears in Paul's lists of virtues that characterize the renewed life in Christ: \"the fruit of the Spirit is love, joy, peace, longsuffering, gentleness, goodness, faith, meekness, temperance\" (Galatians 5:22–23). It governs the spirit in which believers bear one another's burdens (Galatians 6:1), receive the Word (James 1:21), and give an answer for their hope (1 Peter 3:15). Isaiah 66:2 identifies meekness as the disposition God esteems: \"to this man will I look, even to him that is poor and of a contrite spirit, and trembleth at my word.\"</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "meekness", "smith": "meekness", "isbe": "meekness"},
        "key_refs": ["Matthew 5:5", "Isaiah 66:2", "Colossians 3:12", "Galatians 5:23"]
    },
    "megiddo": {
        "id": "megiddo",
        "term": "Megiddo",
        "category": "places",
        "intro": "<p>Megiddo (meaning <em>place of crowns</em> or <em>place of troops</em>) was a strategically vital Canaanite city commanding the Jezreel Valley and the pass through the Carmel ridge that controlled the main coastal route between Egypt and Mesopotamia. Joshua defeated its Canaanite king but Manasseh failed to drive out its inhabitants (Joshua 12:21; Judges 1:27). Solomon later fortified it as one of his chariot cities (1 Kings 9:15), and it remained a major administrative center. The valley of Megiddo witnessed pivotal battles: Deborah and Barak defeated Sisera near its waters (Judges 4–5), and King Josiah was killed at Megiddo fighting Pharaoh Neco (2 Kings 23:29) — a death mourned as a national catastrophe (Zechariah 12:11).</p><p>Megiddo's military significance made it the archetypal battlefield. Revelation 16:16 employs the Hebrew form <em>Har-Magedon</em> (Armageddon — \"mountain of Megiddo\") for the gathering place of the kings of the earth for the final eschatological battle, connecting the site's long history of decisive conflict with the ultimate confrontation between God and the forces of evil at the end of the age.</p>",
        "hitchcock_meaning": "his precious fruit; declaring a message",
        "source_ids": {"easton": "megiddo", "smith": "megiddo", "isbe": "megiddo"},
        "key_refs": ["Joshua 12:21", "1 Kings 9:15", "2 Kings 23:29", "Revelation 16:16"]
    },
    "mehetabeel": {
        "id": "mehetabeel",
        "term": "Mehetabeel",
        "category": "people",
        "intro": "<p>Mehetabeel was the grandfather of Shemaiah, the false prophet hired by Sanballat and Tobiah to frighten Nehemiah into fleeing to the temple — a plot intended to discredit him before the people (Nehemiah 6:10–14). The name means <em>how good is God</em> or <em>benefited by God</em>. Mehetabeel himself plays no active role in the narrative; only his grandson's treachery is recorded.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mehetabeel", "smith": "mehetabeel"},
        "key_refs": ["Nehemiah 6:10"]
    },
    "mehetabel": {
        "id": "mehetabel",
        "term": "Mehetabel",
        "category": "people",
        "intro": "<p>Mehetabel (meaning <em>how good is God</em> or <em>favored of God</em>) was the wife of Hadar (or Hadad), one of the later kings of Edom, listed in Genesis 36:39 and 1 Chronicles 1:50. She was the daughter of Matred and granddaughter of Me-zahab. Mehetabel is one of the few women named in the Edomite king lists, which is itself unusual in ancient genealogies and may indicate her family's particular prominence.</p>",
        "hitchcock_meaning": "how good is God",
        "source_ids": {"easton": "mehetabel", "smith": "mehetabel"},
        "key_refs": ["Genesis 36:39"]
    },
    "mehujael": {
        "id": "mehujael",
        "term": "Mehujael",
        "category": "people",
        "intro": "<p>Mehujael (meaning <em>who proclaims God</em> or <em>smitten by God</em>) was a descendant of Cain, the son of Irad and father of Methusael, who was the father of Lamech (Genesis 4:18). He appears in the genealogy of Cain's line in Genesis 4, which traces the development of civilization through Cain's descendants including city-builders, cattle-rearers, musicians, and metalworkers. Mehujael's name ironically contains the element El (God), though the Cainite line stands in contrast to the Sethite line that called on the name of the LORD (Genesis 4:26).</p>",
        "hitchcock_meaning": "who proclaims God",
        "source_ids": {"easton": "mehujael", "smith": "mehujael"},
        "key_refs": ["Genesis 4:18"]
    },
    "mehuman": {
        "id": "mehuman",
        "term": "Mehuman",
        "category": "people",
        "intro": "<p>Mehuman (meaning <em>making an uproar</em>, <em>faithful</em>, or <em>a multitude</em>) was one of the seven eunuchs who served before Ahasuerus (Xerxes) of Persia. He was commanded to bring Queen Vashti before the king with her royal crown at the great banquet in Susa (Esther 1:10). Her refusal to appear led to the events that eventually brought Esther to the Persian court. Mehuman is named first among the seven chamberlains, suggesting he held the highest rank among them.</p>",
        "hitchcock_meaning": "making an uproar; a multitude",
        "source_ids": {"easton": "mehuman", "smith": "mehuman"},
        "key_refs": ["Esther 1:10"]
    },
    "mehunims": {
        "id": "mehunims",
        "term": "Mehunims",
        "category": "people",
        "intro": "<p>The Mehunims (also Mehunim or Meunim) were a people of Arabia whom Uzziah king of Judah subdued in his campaigns east of the Jordan (2 Chronicles 26:7). A contingent of them also appears in the census of returning exiles under Zerubbabel among the Nethinim — temple servants — (Ezra 2:50; Nehemiah 7:52), suggesting that some had been taken as captives and assigned to temple service. They may be related to the inhabitants of Maon in Edom, east of Petra.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "mehunims", "smith": "mehunims"},
        "key_refs": ["2 Chronicles 26:7", "Ezra 2:50"]
    },
    "mekonah": {
        "id": "mekonah",
        "term": "Mekonah",
        "category": "places",
        "intro": "<p>Mekonah (meaning <em>a base</em> or <em>foundation of a pillar</em>) was a town in the Negeb region of Judah, repopulated after the return from Babylonian exile, listed alongside Ziklag and other southern Judean towns in Nehemiah 11:28. Its precise location has not been identified with certainty. It appears only in this single post-exilic text, suggesting it was a minor settlement resettled as part of the restoration of Judah's southern frontier.</p>",
        "hitchcock_meaning": "a foot of a pillar; provision",
        "source_ids": {"easton": "mekonah", "smith": "mekonah"},
        "key_refs": ["Nehemiah 11:28"]
    },
    "melchi": {
        "id": "melchi",
        "term": "Melchi",
        "category": "people",
        "intro": "<p>Melchi (meaning <em>my king</em> or <em>my counsel</em>) is the name of two ancestors of Jesus in Luke's genealogy. One Melchi was the son of Janna and father of Levi, appearing in the list at Luke 3:24. Another Melchi was the son of Addi and father of Neri, appearing at Luke 3:28. Both occupy positions in the long Lukan lineage tracing Jesus's descent through David and the patriarchs to Adam and to God.</p>",
        "hitchcock_meaning": "my king; my counsel",
        "source_ids": {"easton": "melchi", "smith": "melchi"},
        "key_refs": ["Luke 3:24", "Luke 3:28"]
    },
    "melchizedek": {
        "id": "melchizedek",
        "term": "Melchizedek",
        "category": "people",
        "intro": "<p>Melchizedek (meaning <em>king of righteousness</em> or <em>king of justice</em>) was the king of Salem and priest of God Most High who met Abraham returning from the defeat of the four kings, brought out bread and wine, blessed Abraham, and received tithes from him (Genesis 14:18–20). His dual role as king and priest was unique in the ancient world; his city, Salem, is most commonly identified with Jerusalem. Nothing is recorded of his parentage, genealogy, birth, or death — a silence that the author of Hebrews treats as typologically significant.</p><p>Psalm 110:4 declares that the messianic king will be \"a priest for ever after the order of Melchizedek\" — a promise the Epistle to the Hebrews expounds at length (Hebrews 5–7). Hebrews argues that Melchizedek's lack of recorded genealogy and his reception of tithes from Abraham (in whose loins the Levitical priesthood was present) demonstrate that his priesthood is superior to the Levitical order. Jesus, as a descendant of Judah rather than Levi, fulfills this non-Levitical priestly order by oath rather than heredity, offering a permanent and perfect priesthood that supersedes the Mosaic system.</p>",
        "hitchcock_meaning": "king of justice",
        "source_ids": {"easton": "melchizedek", "smith": "melchizedek", "isbe": "melchizedek"},
        "key_refs": ["Genesis 14:18", "Psalms 110:4", "Hebrews 5:6", "Hebrews 7:1"]
    },
    "melea": {
        "id": "melea",
        "term": "Melea",
        "category": "people",
        "intro": "<p>Melea (meaning <em>supplying</em> or <em>supplied</em>) was an ancestor of Jesus in Luke's genealogy, the son of Menan (or Menna) and father of Eliakim, appearing in the descent traced through David (Luke 3:31). He is mentioned only in this genealogical list and no further details about him appear in Scripture.</p>",
        "hitchcock_meaning": "supplying; supplied",
        "source_ids": {"easton": "melea", "smith": "melea"},
        "key_refs": ["Luke 3:31"]
    },
    "melech": {
        "id": "melech",
        "term": "Melech",
        "category": "people",
        "intro": "<p>Melech (meaning <em>king</em> or <em>counselor</em>) was the second son of Micah, the son of Meribbaal (also known as Mephibosheth), the son of Jonathan the son of Saul, listed in the genealogy of Benjamin in 1 Chronicles 8:35 and 9:41. He is thus a great-grandson of Jonathan and belonged to the royal house of Saul that survived after Saul's death. No further details of Melech are recorded beyond this genealogical reference.</p>",
        "hitchcock_meaning": "king; counselor",
        "source_ids": {"easton": "melech", "smith": "melech"},
        "key_refs": ["1 Chronicles 8:35"]
    },
    "melita": {
        "id": "melita",
        "term": "Melita",
        "category": "places",
        "intro": "<p>Melita (meaning <em>affording honey</em>, corresponding to the modern island of Malta) was the island on which Paul was shipwrecked during his voyage to Rome as a prisoner (Acts 27:27–28:1). After fourteen days adrift in the Adriatic storm, the ship ran aground on Melita and was broken apart by the waves, though all 276 persons aboard survived — in fulfillment of the angel's promise to Paul (Acts 27:24). The inhabitants of Melita showed remarkable hospitality, lighting a fire for the cold and wet survivors.</p><p>During his three-month stay on the island, Paul shook off a viper that fastened on his hand without suffering harm (Acts 28:3–6) — an event the islanders first interpreted as divine punishment and then as marking him a god. He healed the father of the island's chief man, Publius, of fever and dysentery, and others on the island came and were healed (Acts 28:7–9). Melita thus became an unexpected scene of apostolic ministry before Paul sailed on to Rome.</p>",
        "hitchcock_meaning": "affording honey",
        "source_ids": {"easton": "melita", "smith": "melita", "isbe": "melita"},
        "key_refs": ["Acts 27:28", "Acts 28:1", "Acts 28:7", "Acts 28:13"]
    },
    "melons": {
        "id": "melons",
        "term": "Melons",
        "category": "concepts",
        "intro": "<p>Melons (Hebrew <em>abattichim</em>) appear in the Old Testament only in Numbers 11:5, where the Israelites in the wilderness recalled with longing the food of Egypt: \"We remember the fish, which we did eat in Egypt freely; the cucumbers, and the melons, and the leeks, and the onions, and the garlick.\" Egypt was and remains famous for its melons — both water-melons and musk-melons — grown abundantly in the Nile valley. The complaint reflects a deeper spiritual failure: the people preferred the remembered abundance of slavery to the covenant relationship and manna that God provided in the wilderness.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "melons", "smith": "melons"},
        "key_refs": ["Numbers 11:5"]
    },
    "melzar": {
        "id": "melzar",
        "term": "Melzar",
        "category": "people",
        "intro": "<p>Melzar (from Babylonian, possibly meaning <em>the steward</em> or <em>warden</em>) was the official appointed over Daniel and his three companions during their training in Nebuchadnezzar's court in Babylon (Daniel 1:11, 16). When Daniel requested to be excused from the king's food and wine, Melzar feared punishment if the Hebrew youths became less healthy than the other young men. Daniel proposed a ten-day trial of pulse and water; after ten days Daniel and his companions appeared healthier than all the rest, and Melzar thereafter allowed them to continue their diet of vegetables.</p>",
        "hitchcock_meaning": "circumcision of a narrow place",
        "source_ids": {"easton": "melzar", "smith": "melzar"},
        "key_refs": ["Daniel 1:11", "Daniel 1:16"]
    },
    "memphis": {
        "id": "memphis",
        "term": "Memphis",
        "category": "places",
        "intro": "<p>Memphis (Hebrew <em>Moph</em> or <em>Noph</em>; Egyptian <em>Men-nefer</em>, meaning <em>enduring beauty</em> or <em>haven of the good</em>) was one of the greatest cities of ancient Egypt, situated on the western bank of the Nile at the apex of the Delta, approximately twelve miles south of modern Cairo. It served as the capital of Egypt through much of the Old Kingdom period and remained a major religious and administrative center throughout its long history, home to the worship of Ptah and the famous Sphinx and pyramids of the Giza plateau nearby.</p><p>Memphis figures in several prophetic oracles of judgment against Egypt. Hosea 9:6 predicts that Egypt — including Memphis — will receive those who flee from Israel's coming judgment. Isaiah 19:13 lists the princes of Memphis among those who have deceived Egypt. Jeremiah repeatedly invokes Noph (Memphis) as a symbol of Egyptian power that will be judged (Jeremiah 2:16; 46:14, 19), and Ezekiel 30:13–16 announces divine judgment against Memphis's idols. The city's pagan strength makes it an apt symbol of the world's systems that oppose God's purposes.</p>",
        "hitchcock_meaning": "abode of the good",
        "source_ids": {"easton": "memphis", "smith": "memphis", "isbe": "memphis"},
        "key_refs": ["Hosea 9:6", "Isaiah 19:13", "Jeremiah 2:16", "Jeremiah 46:14"]
    },
    "memucan": {
        "id": "memucan",
        "term": "Memucan",
        "category": "people",
        "intro": "<p>Memucan (meaning <em>impoverished</em> or <em>to prepare; certain; true</em>) was one of the seven princes of Persia and Media who had access to King Ahasuerus and sat first in the kingdom (Esther 1:14). When Queen Vashti refused the king's summons, the king consulted his princes about what should be done according to law. Memucan answered on behalf of the council, recommending that Vashti be deposed — arguing that her refusal would encourage all women throughout the empire to despise their husbands — and that a royal decree be published commanding honor for husbands in every household (Esther 1:16–21). His counsel shaped the events that led to Esther's selection as queen.</p>",
        "hitchcock_meaning": "impoverished; to prepare; certain; true",
        "source_ids": {"easton": "memucan", "smith": "memucan"},
        "key_refs": ["Esther 1:14", "Esther 1:16", "Esther 1:21"]
    },
    "menahem": {
        "id": "menahem",
        "term": "Menahem",
        "category": "people",
        "intro": "<p>Menahem (meaning <em>comforter</em> or <em>who conducts them</em>) was king of Israel (c. 752–742 B.C.), son of Gadi, who seized the throne by assassinating King Shallum a month into his reign (2 Kings 15:14). His ten-year reign was marked by cruelty — he sacked Tiphsah and ripped open all the pregnant women of those who refused to open their gates — and by political capitulation to Assyria. When Pul (Tiglath-pileser III) invaded Israel, Menahem paid him a thousand talents of silver as tribute, extracted from Israel's wealthy men at fifty shekels each, securing Assyrian support for his throne (2 Kings 15:19–20).</p><p>Menahem is evaluated by the biblical historian as one who \"did that which was evil in the sight of the LORD\" and maintained the sin of Jeroboam throughout his reign. His tribute to Assyria marks an early stage of the Assyrian domination that would eventually destroy the northern kingdom. He was succeeded by his son Pekahiah.</p>",
        "hitchcock_meaning": "comforter; who conducts them",
        "source_ids": {"easton": "menahem", "smith": "menahem", "isbe": "menahem"},
        "key_refs": ["2 Kings 15:14", "2 Kings 15:19"]
    },
    "mene": {
        "id": "mene",
        "term": "Mene",
        "category": "concepts",
        "intro": "<p>Mene (Aramaic <em>mene</em>, meaning <em>numbered</em> or <em>who is counted</em>) is the first word of the mysterious inscription written by a supernatural hand on the wall of Belshazzar's palace in Babylon during his great feast (Daniel 5:25): <em>Mene, Mene, Tekel, Upharsin</em>. Daniel interpreted its meaning: Mene — God has numbered the days of Belshazzar's kingdom and finished it; Tekel — he has been weighed in the balances and found wanting; Peres (singular of Upharsin) — his kingdom is divided and given to the Medes and Persians. That very night Belshazzar was slain and the kingdom passed to Darius the Mede (Daniel 5:30–31).</p><p>The phrase \"the writing on the wall\" has entered Western idiom as a metaphor for unmistakable signs of coming judgment or doom. The episode illustrates the biblical theme that the sovereign God holds all human rulers accountable and sets their term of power according to his own purposes (Daniel 4:17; Romans 13:1).</p>",
        "hitchcock_meaning": "who reckons or is counted",
        "source_ids": {"easton": "mene", "smith": "mene"},
        "key_refs": ["Daniel 5:25", "Daniel 5:26"]
    },
    "meni": {
        "id": "meni",
        "term": "Meni",
        "category": "concepts",
        "intro": "<p>Meni (meaning <em>fate</em> or <em>fortune</em>) appears in Isaiah 65:11 as a pagan deity worshipped by apostate Israelites: \"But ye are they that forsake the LORD, that forget my holy mountain, that prepare a table for Gad, and that furnish the drink offering unto Meni.\" Meni — the deity of fate or fortune — was apparently worshipped alongside Gad (a deity of luck) in syncretistic ceremonies that God condemns as a fundamental betrayal of the covenant. The same passage goes on to announce divine judgment on those who abandoned the LORD for such fortune-cults.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "meni", "smith": "meni"},
        "key_refs": ["Isaiah 65:11"]
    },
    "meonenim": {
        "id": "meonenim",
        "term": "Meonenim",
        "category": "places",
        "intro": "<p>Meonenim (meaning <em>charmers</em> or <em>regarders of times</em>) is a place name appearing in Judges 9:37, where Zebul tells Abimelech that men are \"coming down from the middle of the land, and another company is coming along the way of the plain of Meonenim\" (the oak or terebinth of Meonenim). The name suggests the site was associated with those who practiced divination or read omens — charmers or astrologers. The Mosaic law strictly prohibited such practices (Deuteronomy 18:10–14), and the name of this landmark preserves a memory of a site connected with forbidden divination, near Shechem.</p>",
        "hitchcock_meaning": "charmers, regarders of times",
        "source_ids": {"easton": "meonenim", "smith": "meonenim"},
        "key_refs": ["Judges 9:37", "Deuteronomy 18:10"]
    },
    "mephaath": {
        "id": "mephaath",
        "term": "Mephaath",
        "category": "places",
        "intro": "<p>Mephaath (meaning <em>splendor</em> or <em>force of waters</em>) was a city east of the Jordan originally belonging to Reuben, assigned to the Merarite Levites (Joshua 21:37). It is listed among the cities of Reuben in Joshua 13:18 and is mentioned in Jeremiah's oracle against Moab (Jeremiah 48:21), by which time it had apparently come under Moabite control. The site is possibly identified with modern Nefa'a, south of Amman in Jordan.</p>",
        "hitchcock_meaning": "appearance, or force, of waters",
        "source_ids": {"easton": "mephaath", "smith": "mephaath"},
        "key_refs": ["Joshua 21:37", "Jeremiah 48:21"]
    },
    "mephibosheth": {
        "id": "mephibosheth",
        "term": "Mephibosheth",
        "category": "people",
        "intro": "<p>Mephibosheth (meaning <em>from my mouth proceeds reproach</em>, or a scribal alteration of the original Meribbaal, <em>contender with Baal</em>) was the son of Jonathan and grandson of King Saul. He became lame in both feet as a child of five when his nurse dropped him while fleeing the news of Saul and Jonathan's deaths at Jezreel (2 Samuel 4:4). David, honoring his covenant with Jonathan, sought out surviving members of Saul's house to show covenant kindness (<em>hesed</em>), and found Mephibosheth living in Lo-debar under the care of Machir son of Ammiel.</p><p>David restored to Mephibosheth all the lands of Saul his grandfather, seated him permanently at the royal table as one of the king's sons (2 Samuel 9), and gave him Ziba as a servant to work the land. The episode is a celebrated illustration of grace: the lame, forgotten son of the king's friend is raised from obscurity and given royal honor not for his own merit but solely because of his father. Mephibosheth's later conduct during Absalom's rebellion (2 Samuel 16:1–4; 19:24–30) is complicated by conflicting claims between him and his servant Ziba.</p>",
        "hitchcock_meaning": "out of my mouth proceeds reproach",
        "source_ids": {"easton": "mephibosheth", "smith": "mephibosheth", "isbe": "mephibosheth"},
        "key_refs": ["2 Samuel 4:4", "2 Samuel 9:7", "2 Samuel 16:1", "1 Chronicles 8:34"]
    },
    "merab": {
        "id": "merab",
        "term": "Merab",
        "category": "people",
        "intro": "<p>Merab (meaning <em>he that fights</em> or <em>increase</em>) was the eldest daughter of King Saul. Saul had promised her as wife to whoever killed Goliath (1 Samuel 17:25), and she was promised to David — but then given instead to Adriel the Meholathite (1 Samuel 14:49; 18:17–19). Her five sons by Adriel were later handed over by David to the Gibeonites for execution as partial restitution for Saul's massacre of that people (2 Samuel 21:8). Merab's story illustrates the turbulent dynamics of royal families and political marriages in the Saulide court.</p>",
        "hitchcock_meaning": "he that fights or disputes",
        "source_ids": {"easton": "merab", "smith": "merab"},
        "key_refs": ["1 Samuel 14:49", "2 Samuel 21:8"]
    },
    "meraiah": {
        "id": "meraiah",
        "term": "Meraiah",
        "category": "people",
        "intro": "<p>Meraiah (meaning <em>rebellion</em> or <em>stubbornness</em>) was a priest in Jerusalem in the days of Joiakim the high priest, representing the priestly family of Seraiah (Nehemiah 12:12). He appears in the list of priestly heads of families in the post-exilic community of the restoration period. No other details of his life or ministry are recorded in Scripture.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "meraiah", "smith": "meraiah"},
        "key_refs": ["Nehemiah 12:12"]
    },
    "meraioth": {
        "id": "meraioth",
        "term": "Meraioth",
        "category": "people",
        "intro": "<p>Meraioth (meaning <em>bitterness</em> or <em>rebellious</em>) is the name of several priests in the Old Testament. The most notable was a high-priestly ancestor: a descendant of Eleazar, son of Aaron, in the priestly line recorded in 1 Chronicles 6:6–7, 52. His name appears in the genealogy connecting Phinehas and Zadok. A second Meraioth was the head of a priestly family in the restoration period, mentioned in connection with the priesthood of Joiakim (Nehemiah 12:15). A third Meraioth is listed as an ancestor of Ezra the scribe (Ezra 7:3; 1 Chronicles 9:11; Nehemiah 11:11).</p>",
        "hitchcock_meaning": "bitterness; rebellious; changing",
        "source_ids": {"easton": "meraioth", "smith": "meraioth"},
        "key_refs": ["1 Chronicles 6:6", "1 Chronicles 6:52", "Nehemiah 12:15"]
    },
    "merari": {
        "id": "merari",
        "term": "Merari",
        "category": "people",
        "intro": "<p>Merari (meaning <em>bitter</em> or <em>to provoke</em>) was the third son of Levi, younger brother of Gershon and Kohath, and founder of the Merarite clan of Levites (Genesis 46:11; Exodus 6:16–19). In the organization of the wilderness tabernacle, the Merarites were responsible for carrying the structural elements of the tabernacle: the boards, bars, pillars, and sockets — the heavy framework that supported the tent structure. They were assigned forty-two cities at the settlement of Canaan, including Jokneam and Kartah in Zebulun, and were given four cities by Reuben and Gad.</p><p>The three great Levitical clans — Gershonites, Kohathites, and Merarites — together served the tabernacle and temple, the Merarites providing the structural backbone of the worship tent as the others carried the sacred furnishings and outer coverings. David reorganized the Levitical assignments for the temple, with Merarites serving as gatekeepers and as musicians appointed to lead praise (1 Chronicles 15:17; 23:21–23).</p>",
        "hitchcock_meaning": "bitter; to provoke",
        "source_ids": {"easton": "merari", "smith": "merari", "isbe": "merari"},
        "key_refs": ["Genesis 46:11", "Exodus 6:16", "Numbers 3:36"]
    },
    "merarites": {
        "id": "merarites",
        "term": "Merarites",
        "category": "people",
        "intro": "<p>The Merarites were the descendants of Merari, the third son of Levi, constituting one of the three main Levitical clans. In the wilderness tabernacle system, they numbered 6,200 males between thirty and fifty years old available for service (Numbers 4:44). Their specific charge was the transport and erection of the tabernacle's structural frame: the boards, bars, pillars, sockets, and cords that formed the physical skeleton of the tent of meeting (Numbers 3:36–37; 4:31–33). They were given four wagons and eight oxen to carry these heavy loads — twice the allotment of the Gershonites (Numbers 7:8).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "merarites", "smith": "merarites"},
        "key_refs": ["Numbers 3:36", "Numbers 4:44", "Numbers 7:8"]
    },
    "merathaim": {
        "id": "merathaim",
        "term": "Merathaim",
        "category": "places",
        "intro": "<p>Merathaim (meaning <em>double rebellion</em>) is a symbolic name applied to Babylon in Jeremiah's oracle against it (Jeremiah 50:21). The prophet calls on the armies of God to go up against \"the land of Merathaim\" and against the inhabitants of Pekod, to destroy and utterly devote them to judgment. The name may also play on the Babylonian region Marratu (the salt marshes of southern Mesopotamia near the Persian Gulf), transforming a geographical term into a theological indictment of Babylon's persistent defiance of God.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "merathaim", "smith": "merathaim"},
        "key_refs": ["Jeremiah 50:21"]
    },
    "merchant": {
        "id": "merchant",
        "term": "Merchant",
        "category": "concepts",
        "intro": "<p>Merchants and trade play a significant role throughout Scripture, reflecting the commercial world of the ancient Near East. The earliest biblical merchant appears in Genesis 37:25–28, where Ishmaelite traders carried Joseph down to Egypt, initiating the chain of events that positioned him as the instrument of God's providential preservation of Israel. Proverbs 31:14 praises the capable wife as one who \"is like the merchants' ships; she bringeth her food from afar.\" Solomon's reign was characterized by extensive international trade, including the famous Tarshish ships that brought gold, silver, ivory, apes, and peacocks from distant lands (1 Kings 10:22).</p><p>Ezekiel 27 contains a remarkable sustained lament over Tyre as the great merchant city of the ancient world, cataloguing its trade in metals, slaves, horses, wheat, wine, oil, and luxury goods from across the known world — and predicting its total destruction. In the New Testament, the parable of the pearl of great price likens the kingdom of heaven to a merchant seeking fine pearls who sells all he has to obtain one of surpassing value (Matthew 13:45–46). Revelation 18 echoes Ezekiel's Tyre lament in its elegy for fallen Babylon, mourning merchants who \"were the great men of the earth\" (Revelation 18:23).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "merchant", "smith": "merchant"},
        "key_refs": ["Genesis 37:25", "Matthew 13:45", "Revelation 18:23"]
    },
}


def main():
    written = skipped = 0
    for slug, data in ARTICLES.items():
        if merge_article(slug, data):
            written += 1
        else:
            skipped += 1
    print(f'BP m2: Mareshah → Merchant: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
