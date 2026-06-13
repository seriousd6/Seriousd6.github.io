"""
BP Article Synthesis — s3: Shaveh, Valley of → Shiphtan
Covers Easton entries: Shaveh, Valley of through Shiphtan (75 entries)

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

Script: scripts/bp-s3.py
Run: python3 scripts/bp-s3.py
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
    "shaveh-valley-of": {
        "id": "shaveh-valley-of",
        "term": "Shaveh, Valley of",
        "category": "places",
        "intro": "<p>The Valley of Shaveh, meaning <em>valley of the plain</em>, is the ancient name for the King's Dale — the broad valley near Jerusalem where Absalom later erected his memorial pillar (2 Samuel 18:18). It is mentioned in Genesis 14:17 as the place where the king of Sodom came out to meet Abraham after his victorious return from the rescue of Lot and the defeat of the four kings under Chedorlaomer. It was also the site of Abraham's meeting with Melchizedek, king of Salem and priest of God Most High.</p><p>The identification of the King's Dale with the Kidron Valley or the valley south of Jerusalem near En-rogel has been proposed by various scholars, though certainty is difficult. Its importance in Genesis 14 lies not in its geography but in the dramatic encounter it frames: Abraham's refusal of the king of Sodom's offer of spoils and his receipt of bread, wine, and blessing from Melchizedek — a meeting that the New Testament epistle to the Hebrews interprets as a type of Christ's eternal priesthood.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "shaveh-valley-of"},
        "key_refs": ["Genesis 14:17", "Genesis 14:18", "2 Samuel 18:18"]
    },
    "shaveh-kiriathaim": {
        "id": "shaveh-kiriathaim",
        "term": "Shaveh-Kiriathaim",
        "category": "places",
        "intro": "<p>Shaveh-Kiriathaim (meaning: <em>plain of Kiriathaim</em>) was a location in Transjordan, east of the Dead Sea in the territory of Moab, where the Emim — the ancient giant inhabitants of the region — were defeated by Chedorlaomer and the coalition of four eastern kings in the military campaign described in Genesis 14:5. This expedition preceded the more famous battle of the kings of the plain, and the defeat of the Emim at Shaveh-Kiriathaim represents one step in a broad campaign that swept down the eastern side of the Jordan valley.</p><p>The site takes its name from the nearby city of Kiriathaim, a double city whose name means <em>the two cities</em> or <em>the two meeting places</em>. Kiriathaim later became a Reubenite settlement (Numbers 32:37; Joshua 13:19) and is mentioned by the prophets Jeremiah (48:1, 23) and Ezekiel (25:9) in oracles of judgment against Moab. The plain or valley beside it served as the battlefield for this early confrontation between the eastern kings and the pre-Israelite peoples of Canaan.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "shaveh-kiriathaim", "smith": "shaveh-kiriathaim", "isbe": "shaveh-kiriathaim"},
        "key_refs": ["Genesis 14:5"]
    },
    "shavsha": {
        "id": "shavsha",
        "term": "Shavsha",
        "category": "concepts",
        "intro": "<p>Shavsha was David's royal secretary, an administrative officer responsible for maintaining official correspondence and records in the Davidic court. He appears under several variant names in the parallel lists of David's officers: Seraiah in 2 Samuel 8:17, Shisha in 1 Kings 4:3, Sheva in 2 Samuel 20:25, and Shavsha in 1 Chronicles 18:16. The variation in the name across these lists reflects scribal variation in the transmission of an originally foreign name, possibly Egyptian in origin.</p><p>The office of royal secretary or scribe was one of the highest administrative posts in ancient Near Eastern kingdoms, responsible for correspondence with foreign powers, recording royal decrees, and managing the administrative records of the realm. Shavsha's sons Elihoreph and Ahiah continued in the same office under Solomon (1 Kings 4:3), indicating that the secretarial position became hereditary in this family during the early monarchy. His prominence in the lists of royal officials reflects the growing complexity of the Davidic administration.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "shavsha", "smith": "shavsha", "isbe": "shavsha"},
        "key_refs": ["2 Samuel 8:17", "1 Kings 4:3", "1 Chronicles 18:16"]
    },
    "shealtiel": {
        "id": "shealtiel",
        "term": "Shealtiel",
        "category": "people",
        "intro": "<p>Shealtiel (meaning: <em>asked of God</em> or <em>I have asked God</em>) was the son of King Jeconiah (Jehoiachin) of Judah, born during the Babylonian exile, and the father of Zerubbabel, the governor who led the first return of Jewish exiles to Jerusalem and superintended the rebuilding of the temple (Ezra 3:2, 8; Nehemiah 12:1; Haggai 1:1, 12). Shealtiel thus stands in the line of the royal Davidic dynasty bridging the exile and the restoration.</p><p>A textual complexity arises in comparing 1 Chronicles 3:17–19 with Ezra 3:2, since Chronicles appears to list Pedaiah rather than Shealtiel as Zerubbabel's father. Various explanations have been proposed, including levirate marriage by which Zerubbabel was legally Shealtiel's son though biologically Pedaiah's. Whatever the exact family relationship, Shealtiel is the name consistently used in the prophets Haggai and Zechariah when addressing Zerubbabel, and both Matthew 1:12 and Luke 3:27 include Shealtiel in their genealogies of Jesus Christ.</p>",
        "hitchcock_meaning": "asked or lent of God",
        "source_ids": {"easton": "shealtiel", "smith": "shealtiel", "isbe": "shealtiel"},
        "key_refs": ["Ezra 3:2", "Haggai 1:1", "Matthew 1:12", "Luke 3:27"]
    },
    "shear-jashub": {
        "id": "shear-jashub",
        "term": "Shear-Jashub",
        "category": "people",
        "intro": "<p>Shear-jashub (meaning: <em>a remnant shall return</em> or <em>a remnant shall repent</em>) was the son of the prophet Isaiah, who bore this name as a living prophetic sign. Isaiah was commanded by God to take his son with him when he went to meet King Ahaz at the conduit of the upper pool during the Syro-Ephraimite crisis (Isaiah 7:3), a period when Syria and Israel had besieged Jerusalem to force Judah into their anti-Assyrian alliance.</p><p>The child's name embodied a double-edged prophetic message: a warning that a remnant only — not all — would survive the coming judgment, and a promise that at least a remnant would return and be saved. This tension between judgment and hope runs throughout Isaiah's theology of the remnant. The concept is developed extensively in Isaiah 10:20–22 and becomes a key theme linking the prophetic ministry of Isaiah to Paul's exposition of election and salvation in Romans 9:27, where the prophet's words are cited to explain God's dealings with Israel.</p>",
        "hitchcock_meaning": "the remnant shall return",
        "source_ids": {"easton": "shear-jashub", "isbe": "shear-jashub"},
        "key_refs": ["Isaiah 7:3", "Isaiah 10:21", "Romans 9:27"]
    },
    "shearing-house": {
        "id": "shearing-house",
        "term": "Shearing-house",
        "category": "concepts",
        "intro": "<p>The shearing-house (Hebrew <em>beth eked ha-ro'im</em>, literally <em>house of binding of the shepherds</em>) is a location mentioned in 2 Kings 10:12–14 in connection with one of the most violent episodes of Jehu's revolution against the house of Ahab. Traveling toward Samaria after slaying King Joram of Israel and King Ahaziah of Judah, Jehu encountered forty-two kinsmen of Ahaziah at a place called the shearing-house. When they identified themselves as relatives of the royal family going down to salute the sons of Ahab and the queen mother Jezebel, Jehu had them all seized and killed at the pit of the shearing-house.</p><p>The location likely designates a rendezvous point used by shepherds or a station where sheep were sheared and bound — a common feature of pastoral infrastructure in ancient Canaan. The Revised Version margin renders it simply <em>Beth-eked of the shepherds</em>, treating it as a place name. This slaughter completed the purge of Ahaziah's family alongside the broader destruction of the Ahab dynasty, fulfilling Elijah's prophecy (1 Kings 21:21).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "shearing-house", "isbe": "shearing-house"},
        "key_refs": ["2 Kings 10:12", "2 Kings 10:14"]
    },
    "sheba": {
        "id": "sheba",
        "term": "Sheba",
        "category": "people",
        "intro": "<p>Sheba is the name of several individuals and a region in Scripture. Among persons, the most prominent is Sheba the son of Bichri, a Benjamite who led a rebellion against David immediately after the suppression of Absalom's revolt (2 Samuel 20:1–22). Crying <em>We have no part in David</em>, he drew the northern tribes away from the king, but was pursued to Abel Beth-maacah, where he was beheaded by the city's inhabitants to prevent its siege.</p><p>Several other men named Sheba appear in the genealogies: a son of Raamah and grandson of Cush (Genesis 10:7), a son of Joktan descended from Shem (Genesis 10:28), and a son of Jokshan and grandson of Abraham by Keturah (Genesis 25:3). The kingdom and people of Sheba — a prosperous trading nation in southwestern Arabia (modern Yemen) — are most memorably represented by the Queen of Sheba, who came to Jerusalem to test Solomon's wisdom with hard questions (1 Kings 10:1–13; Matthew 12:42). This kingdom was famous for its gold, frankincense, myrrh, and spices.</p>",
        "hitchcock_meaning": "captivity, conversion, old man",
        "source_ids": {"easton": "sheba", "smith": "sheba"},
        "key_refs": ["2 Samuel 20:1", "1 Kings 10:1", "Genesis 10:7", "Matthew 12:42"]
    },
    "shebaniah": {
        "id": "shebaniah",
        "term": "Shebaniah",
        "category": "people",
        "intro": "<p>Shebaniah (meaning: <em>whom Jehovah hides</em> or <em>whom Jehovah has caused to grow up</em>) is the name of several individuals in the post-exilic period. One Shebaniah was a priest appointed by David to blow a trumpet before the ark of the Lord when it was brought to Jerusalem (1 Chronicles 15:24). Several others appear in the Nehemiah narrative: a Levite who led the congregation in the great prayer of confession on the twenty-fourth day of the seventh month (Nehemiah 9:4–5), a priest who sealed the covenant renewal (Nehemiah 10:4), and two Levites also among the signatories of the covenant (Nehemiah 10:10, 12).</p><p>The frequency of the name in the restoration community reflects the Levitical and priestly families' strong presence in the return from Babylon and their central role in the religious renewal under Ezra and Nehemiah. The various Shebaniahss demonstrate how the same priestly and Levitical names recurred across generations within these families.</p>",
        "hitchcock_meaning": "God is my strength",
        "source_ids": {"easton": "shebaniah", "smith": "shebaniah", "isbe": "shebaniah"},
        "key_refs": ["1 Chronicles 15:24", "Nehemiah 9:4", "Nehemiah 10:4"]
    },
    "shebarim": {
        "id": "shebarim",
        "term": "Shebarim",
        "category": "places",
        "intro": "<p>Shebarim (meaning: <em>breaks</em> or <em>ruins</em>) was a place near the city of Ai where the men of Ai pursued and routed the Israelite force that had been sent in the first ill-fated attempt to take the city (Joshua 7:5). Israel's initial attack on Ai with a small force of two or three thousand men failed disastrously because of the hidden sin of Achan, who had taken forbidden spoil from Jericho. The Israelites fled before the men of Ai and were struck down <em>before the gate even unto Shebarim</em>.</p><p>The location of Shebarim is uncertain. The Revised Version margin renders it as <em>the quarries</em>, suggesting a rocky broken terrain rather than a proper place name. The defeat at Ai caused great discouragement in Israel and led to Joshua's prayer of distress before the ark, followed by God's revelation of Achan's sin, his judgment, and the subsequent successful campaign against Ai using the divinely directed ambush strategy of Joshua 8.</p>",
        "hitchcock_meaning": "hopes, expectations",
        "source_ids": {"easton": "shebarim", "smith": "shebarim", "isbe": "shebarim"},
        "key_refs": ["Joshua 7:5"]
    },
    "shebna": {
        "id": "shebna",
        "term": "Shebna",
        "category": "people",
        "intro": "<p>Shebna (meaning: <em>tender youth</em> or possibly of foreign origin) was a high royal official during the reign of King Hezekiah of Judah, initially holding the position of steward or treasurer <em>over the house</em> — the highest domestic office of the royal court (Isaiah 22:15). The prophet Isaiah pronounced a severe oracle against him for his pride, specifically for hewing himself a grand tomb in the rock as though he were a great man, and predicted that he would be hurled violently away and die in a foreign land (Isaiah 22:16–19).</p><p>Shebna subsequently appears at a lower rank — as secretary rather than steward — when Hezekiah sends him with Eliakim and Joah to negotiate with the Assyrian Rabshakeh during the siege of Jerusalem (2 Kings 18:18, 26, 37; Isaiah 36:3, 11, 22), suggesting that Isaiah's rebuke resulted in his demotion. The position of <em>steward over the house</em> that Isaiah says will be given to Eliakim was fulfilled (Isaiah 22:20–24), making Shebna's trajectory a vivid illustration of pride brought low and faithful service exalted.</p>",
        "hitchcock_meaning": "who rests himself",
        "source_ids": {"easton": "shebna", "smith": "shebna", "isbe": "shebna"},
        "key_refs": ["Isaiah 22:15", "Isaiah 22:19", "2 Kings 18:18", "Isaiah 36:3"]
    },
    "shebuel": {
        "id": "shebuel",
        "term": "Shebuel",
        "category": "people",
        "intro": "<p>Shebuel (meaning: <em>captive of God</em> or <em>God is my captivity</em>) is the name of two individuals in the Davidic era. The first was a descendant of Gershom the son of Moses, who held the position of chief officer over the treasuries of the house of God in David's administrative organization (1 Chronicles 23:16; 26:24). His appointment to this position reflects David's comprehensive reorganization of the Levitical roles in preparation for Solomon's temple.</p><p>The second Shebuel was a son of Heman the musician, one of fourteen sons appointed by David to prophesy with musical instruments — harps, psalteries, and cymbals — in the house of the Lord (1 Chronicles 25:4–5). Shebuel and his brothers served in the twenty-fourth division of the temple musicians, a system organized by lot to ensure regular rotation through the liturgical calendar (1 Chronicles 25:20). Both figures represent the careful organization of Levitical service that David established as his lasting contribution to Israel's worship.</p>",
        "hitchcock_meaning": "captivity of God",
        "source_ids": {"easton": "shebuel", "isbe": "shebuel"},
        "key_refs": ["1 Chronicles 23:16", "1 Chronicles 26:24", "1 Chronicles 25:4"]
    },
    "shecaniah": {
        "id": "shecaniah",
        "term": "Shecaniah",
        "category": "people",
        "intro": "<p>Shecaniah (meaning: <em>one intimate with Jehovah</em> or <em>Jehovah is my neighbor</em>) is the name of several individuals in the post-exilic period. A priest of the tenth division of priests organized by David is named Shecaniah in 1 Chronicles 24:11. Another prominent in 2 Chronicles 31:15 distributed the freewill offerings among the priests during Hezekiah's reform. A descendant of Zerubbabel appears in the Davidic genealogy of 1 Chronicles 3:21–22.</p><p>The most historically significant Shecaniah was the son of Jehiel of the sons of Elam, who made the remarkable proposal to Ezra that the community confess and address the crisis of foreign marriages (Ezra 10:2–4). Though he himself may not have been among the offenders, Shecaniah urged Ezra to act decisively, pledging community support for covenant renewal. Another Shecaniah, the father of Shemaiah who repaired a section of Jerusalem's wall (Nehemiah 3:29), and one who returned from Babylon with Ezra (Ezra 8:3, 5) also bear the name.</p>",
        "hitchcock_meaning": "dwelling of the Lord",
        "source_ids": {"easton": "shecaniah"},
        "key_refs": ["Ezra 10:2", "1 Chronicles 24:11", "Nehemiah 3:29"]
    },
    "shechem": {
        "id": "shechem",
        "term": "Shechem",
        "category": "places",
        "intro": "<p>Shechem (meaning: <em>shoulder</em> or <em>ridge</em>) was one of the most important cities of ancient Canaan, situated in the mountain pass between Mount Gerizim and Mount Ebal in the central highlands of what became the territory of Ephraim. It served as the first recorded stopping place of Abraham in Canaan (Genesis 12:6), the site of Jacob's purchase of land and his daughter Dinah's violation by the prince Shechem son of Hamor (Genesis 33–34), and the place where Joseph was sent to find his brothers before his sale into Egypt.</p><p>Shechem's theological and political significance continued throughout Israel's history. Joshua assembled all Israel at Shechem for the great covenant renewal ceremony following the conquest (Joshua 24), and it became a Levitical city of refuge (Joshua 20:7; 21:21). After Solomon's death, Rehoboam's refusal at Shechem to lighten the people's burden triggered the division of the kingdom (1 Kings 12:1–16). Jeroboam made it his first capital. In the New Testament, Jesus's conversation with the Samaritan woman at Jacob's well took place near Sychar, close to the ancient site of Shechem (John 4:5).</p>",
        "hitchcock_meaning": "part, portion",
        "source_ids": {"easton": "shechem", "smith": "shechem", "isbe": "shechem"},
        "key_refs": ["Genesis 12:6", "Joshua 24:1", "1 Kings 12:1", "John 4:5"]
    },
    "shechinah": {
        "id": "shechinah",
        "term": "Shechinah",
        "category": "concepts",
        "intro": "<p>Shechinah (from the Chaldee/Aramaic <em>shekhan</em>, meaning <em>resting-place</em> or <em>dwelling</em>) is a post-biblical Jewish term for the visible manifestation of God's glorious presence among his people. The word itself does not appear in Scripture but was coined by Jewish rabbis to describe the theophanic phenomena recorded throughout the Old Testament: the pillar of cloud and fire that guided Israel in the wilderness, the cloud that filled the tabernacle so that Moses could not enter (Exodus 40:34–35), and the glory that filled Solomon's temple at its dedication (1 Kings 8:10–11; 2 Chronicles 7:1–3).</p><p>The Shechinah is also identified with the cloud of glory (<em>kavod</em>) that appeared between the cherubim over the ark of the covenant, the bright light of the divine presence that the prophet Ezekiel saw departing the temple before Jerusalem's destruction (Ezekiel 10–11). In the New Testament, John 1:14 — <em>the Word became flesh and dwelt</em> (<em>eskēnōsen</em>, tabernacled) <em>among us, and we beheld his glory</em> — is widely understood as a deliberate allusion to the Shechinah, presenting the Incarnation as the ultimate and permanent dwelling of God among his people.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "shechinah", "smith": "shechinah"},
        "key_refs": ["Exodus 40:34", "1 Kings 8:10", "Ezekiel 10:18", "John 1:14"]
    },
    "sheep": {
        "id": "sheep",
        "term": "Sheep",
        "category": "concepts",
        "intro": "<p>Sheep were among the most important domestic animals of the ancient biblical world, central to the pastoral economy of the patriarchs and throughout Israelite life. They provided wool for clothing, milk for food, and were the principal animals of the sacrificial system. Several breeds are attested in ancient Palestine, including the broad-tailed sheep (<em>Ovis laticaudata</em>) whose fat tail was specified in the peace offerings (Leviticus 3:9). The wealth of patriarchs like Abraham, Isaac, Jacob, and Job was measured partly in their flocks.</p><p>In Scripture the sheep carries profound theological symbolism. Israel is repeatedly described as God's flock (Psalm 23; Psalm 100:3; Isaiah 40:11; Ezekiel 34), and the faithless leaders of Israel are condemned as negligent or predatory shepherds (Ezekiel 34:2–10; Jeremiah 23:1–4). Jesus applied this imagery most fully in declaring himself the Good Shepherd who lays down his life for the sheep (John 10:11–18), fulfilling Ezekiel's promise that God himself would shepherd his scattered flock. The image of straying sheep (Isaiah 53:6; Luke 15:4–7) and of sheep before the shearers (Isaiah 53:7) runs through the Passion narratives.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sheep", "smith": "sheep", "isbe": "sheep"},
        "key_refs": ["Psalms 23:1", "John 10:11", "Isaiah 53:6", "Ezekiel 34:2"]
    },
    "sheep-fold": {
        "id": "sheep-fold",
        "term": "Sheep-fold",
        "category": "concepts",
        "intro": "<p>A sheep-fold was a strong fenced enclosure, typically built of stone walls with thorn bushes laid along the top, designed to protect flocks from predators and thieves during the night. In the ancient Near East, several shepherds might share a single communal fold, each bringing their flocks in at nightfall and removing them by name in the morning with the porter's assistance. The fold had a single gate through which the shepherd entered legitimately.</p><p>Jesus uses the imagery of the sheepfold extensively in John 10:1–16, drawing a sharp contrast between the true shepherd, who enters by the door and calls his own sheep by name, and the thief, who climbs in by another way to steal and destroy. The sheep know the shepherd's voice and follow him, a metaphor for the relationship between Christ and his disciples. The image also appears in the Old Testament: David was called from following the sheep-folds to shepherd Israel (Psalm 78:70–71; 2 Samuel 7:8), and the wilderness encampments of the Transjordanian tribes included sheepfolds as permanent features of their pastoral settlements (Numbers 32:24).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sheep-fold"},
        "key_refs": ["John 10:1", "John 10:16", "Psalms 78:70", "Numbers 32:24"]
    },
    "sheep-gate": {
        "id": "sheep-gate",
        "term": "Sheep Gate",
        "category": "places",
        "intro": "<p>The Sheep Gate was one of the gates of Jerusalem rebuilt under Nehemiah's direction following the return from Babylon. It is mentioned first in the list of gate restorations (Nehemiah 3:1), rebuilt by Eliashib the high priest and his fellow priests, and stands as the starting and ending point of Nehemiah's circuit of the wall (Nehemiah 12:39). The gate was dedicated first and was the only one whose builders are said to have consecrated it, reflecting its priestly associations.</p><p>The Sheep Gate's location on the northern side of the temple mount area made it the natural entry point for sheep brought into the city for sacrifice. In the New Testament, John 5:2 places a pool called Bethesda (<em>in Hebrew</em>) near the Sheep Gate, surrounded by five porches — the site where Jesus healed a man who had been ill for thirty-eight years. Archaeological investigations in the nineteenth and twentieth centuries identified a large double pool complex north of the temple mount as the probable location of this pool.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sheep-gate", "isbe": "sheep-gate"},
        "key_refs": ["Nehemiah 3:1", "Nehemiah 12:39", "John 5:2"]
    },
    "sheep-market": {
        "id": "sheep-market",
        "term": "Sheep Market",
        "category": "places",
        "intro": "<p>The sheep market appears in John 5:2 in the phrase <em>there is at Jerusalem by the sheep market a pool, which is called in the Hebrew tongue Bethesda</em>. Both the Revised Version text and the Authorized Version margin render the underlying Greek as <em>sheep gate</em> rather than sheep market, since the Greek <em>probatikē</em> (feminine adjective, <em>of sheep</em>) more naturally modifies the implied noun <em>gate</em> than market, following the reference to the Sheep Gate in Nehemiah 3:1.</p><p>Whether the designation refers to a gate or a market, the location is the same: the area near the north side of the temple mount where sheep destined for sacrifice were assembled, inspected, and sold. Pools in this area were used for washing animals prior to sacrifice. The pool of Bethesda, with its five colonnaded porches, was associated with healing, and it was there that Jesus encountered the man who had waited thirty-eight years for someone to lower him into the water at its periodic stirring — whom Jesus healed by his word alone.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sheep-market", "isbe": "sheep-market"},
        "key_refs": ["John 5:2", "John 5:5", "John 5:8"]
    },
    "shekel": {
        "id": "shekel",
        "term": "Shekel",
        "category": "concepts",
        "intro": "<p>The shekel (Hebrew <em>sheqel</em>, from <em>shaqal</em>, to weigh) was the standard unit of both weight and currency in ancient Israel, preceding the introduction of coined money. Silver and gold were weighed out in transactions rather than counted as coins, and the shekel provided the normative weight standard. The sanctuary shekel — twenty gerahs — was the sacred standard (Exodus 30:13; Numbers 3:47), slightly heavier than the common shekel to prevent shortchanging in sacred dues.</p><p>The shekel appears throughout the biblical narratives as the standard medium of significant transactions: Abraham weighed four hundred shekels of silver to Ephron for the cave of Machpelah (Genesis 23:15–16); Joseph was sold for twenty pieces of silver (Genesis 37:28); the temple tax was a half-shekel (Exodus 30:13); and Goliath's armor weighed five thousand shekels of bronze (1 Samuel 17:5). After the exile, the Jews began minting their own silver shekels during the Maccabean period. The New Testament drachma and stater (Matthew 17:27) served as rough equivalents for the shekel in the Greek monetary system.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "shekel", "smith": "shekel", "isbe": "shekel"},
        "key_refs": ["Exodus 30:13", "Genesis 23:16", "Numbers 3:47", "Ezekiel 45:12"]
    },
    "shelah": {
        "id": "shelah",
        "term": "Shelah",
        "category": "people",
        "intro": "<p>Shelah (meaning: <em>petition</em> or <em>sprout</em>) is the name of several individuals in the Old Testament. The most prominent is Shelah, the third son of Judah by the Canaanite daughter of Shua (Genesis 38:2, 5). He was withheld from marriage to Tamar after the deaths of his brothers Er and Onan, which led Tamar to take matters into her own hands by disguising herself as a cult prostitute to conceive sons from Judah himself. Shelah became the ancestor of the Shelanite clan within Judah (Numbers 26:20; 1 Chronicles 4:21).</p><p>A second Shelah was a son of Arphaxad, grandson of Shem, and an ancestor of Abraham in the genealogy of Genesis 11:13–15 (called Salah). He is included in Luke's genealogy of Jesus (Luke 3:35). A third Shelah was the pool and aqueduct of Siloah (Shiloah), which fed water from the Gihon spring into the lower city of Jerusalem — a distinct usage of the same root meaning a sending forth of water, referenced in Nehemiah 3:15 and Isaiah 8:6.</p>",
        "hitchcock_meaning": "peace, abundance",
        "source_ids": {"easton": "shelah", "smith": "shelah", "isbe": "shelah"},
        "key_refs": ["Genesis 38:5", "Genesis 38:14", "Numbers 26:20", "Luke 3:35"]
    },
    "shelemiah": {
        "id": "shelemiah",
        "term": "Shelemiah",
        "category": "people",
        "intro": "<p>Shelemiah (meaning: <em>whom Jehovah repays</em> or <em>Jehovah is recompense</em>) is the name of numerous individuals in the Old Testament, clustered especially in the prophetic and restoration periods. Among the most significant are: a man whose son Hananiah repaired part of Jerusalem's wall under Nehemiah (Nehemiah 3:30); the father of Jehucal, one of the officials sent by King Zedekiah to the prophet Jeremiah (Jeremiah 37:3); and the father of Irijah, the officer who arrested Jeremiah as he tried to leave Jerusalem (Jeremiah 37:13).</p><p>Others include: one of the officials who had Baruch's scroll read in the temple chamber (Jeremiah 36:14); a son of Cushi whose son Nethaniah read Jeremiah's scroll before the princes (Jeremiah 36:14); an official who threw Jeremiah into the cistern on the charge of demoralizing the people (Jeremiah 38:1); and several who had married foreign wives and agreed to put them away (Ezra 10:39, 41). The name's frequency in the prophetic era may reflect the pious hope for divine restoration that accompanied the Babylonian crisis.</p>",
        "hitchcock_meaning": "God is my recompense",
        "source_ids": {"easton": "shelemiah", "smith": "shelemiah", "isbe": "shelemiah"},
        "key_refs": ["Jeremiah 37:3", "Jeremiah 38:1", "Nehemiah 3:30"]
    },
    "shem": {
        "id": "shem",
        "term": "Shem",
        "category": "people",
        "intro": "<p>Shem (meaning: <em>name</em> or <em>renown</em>) was the firstborn son of Noah and one of the three patriarchal figures from whom all post-flood humanity descends (Genesis 5:32; 6:10). He entered the ark with his parents and brothers and emerged with them after the flood. When his father Noah lay drunk and uncovered in his tent, Shem and Japheth covered him with a garment without looking at him, an act of filial respect for which Noah prophesied blessing upon both (Genesis 9:23–26).</p><p>Shem received the specific blessing: <em>Blessed be the Lord, the God of Shem</em> (Genesis 9:26), marking his line as the custodian of the covenant relationship with God. Through Shem descended the Semitic peoples — including Elam, Asshur, Arphaxad, Lud, and Aram — and ultimately Abraham, Isaac, Jacob, and the line of David and Jesus (Genesis 11:10–26; Luke 3:36). The name <em>Semite</em>, used for the linguistic and ethnic family to which Hebrew belongs, derives from his name. Shem lived to the extraordinary age of 600 years, long enough to have been contemporary with Abraham.</p>",
        "hitchcock_meaning": "name, renown",
        "source_ids": {"easton": "shem", "smith": "shem", "isbe": "shem"},
        "key_refs": ["Genesis 5:32", "Genesis 9:23", "Genesis 11:10", "Luke 3:36"]
    },
    "shema": {
        "id": "shema",
        "term": "Shema",
        "category": "people",
        "intro": "<p>Shema (meaning: <em>rumour</em> or <em>hearing</em>) is the name of several minor figures in the Old Testament. One Shema was a Reubenite, a descendant of Joel, listed in the genealogy of that tribe in 1 Chronicles 5:8. A second was a Benjamite, the son of Elpaal, who with his brother Beriah drove away the inhabitants of Gath (1 Chronicles 8:13). A third Shema stood at Ezra's right hand on the wooden platform during the public reading of the law to the restored community (Nehemiah 8:4). A town in the Negeb of Judah (Joshua 15:26) also bears this name.</p><p>It should be noted that <em>Shema</em> as a personal name is entirely distinct from the <em>Shema</em> (Hebrew: <em>hear</em>) of Deuteronomy 6:4 — <em>Hear, O Israel: The Lord our God, the Lord is one</em> — which is the foundational confession of Jewish faith and liturgy. The personal name shares the same Hebrew root but carries no inherent connection to that central creed.</p>",
        "hitchcock_meaning": "hearing, obeying",
        "source_ids": {"easton": "shema", "smith": "shema"},
        "key_refs": ["1 Chronicles 5:8", "1 Chronicles 8:13", "Nehemiah 8:4"]
    },
    "shemaah": {
        "id": "shemaah",
        "term": "Shemaah",
        "category": "concepts",
        "intro": "<p>Shemaah (meaning: <em>rumour</em> or <em>fame</em>) was a Benjamite from Gibeah whose two sons, Ahiezer and Joash, were among the ambidextrous warriors — able to sling stones and shoot arrows with either hand — who came to David at Ziklag before his accession to the throne (1 Chronicles 12:3). These Benjamites had detached themselves from Saul's service to join David, despite being from Saul's own tribe.</p><p>Their father Shemaah is mentioned only in this genealogical notice; no individual acts are attributed to him beyond being the father of these two warriors. The Ziklag contingent (1 Chronicles 12:1–7) represents the growing movement of supporters who recognized David's divine calling even before Saul's death, and the Benjamite presence among them was particularly significant given the political loyalty that tribe generally owed to its kinsman Saul.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "shemaah", "smith": "shemaah", "isbe": "shemaah"},
        "key_refs": ["1 Chronicles 12:3"]
    },
    "shemaiah": {
        "id": "shemaiah",
        "term": "Shemaiah",
        "category": "people",
        "intro": "<p>Shemaiah (meaning: <em>whom Jehovah heard</em>) is one of the most common names in the Old Testament, borne by numerous individuals across several centuries. The most historically significant was the prophet Shemaiah who spoke in the reign of Rehoboam, forbidding the king to make war against the northern tribes after the division of the kingdom: <em>Ye shall not go up, nor fight against your brethren</em> (1 Kings 12:22–24). The same prophet later explained the Shishak invasion of Judah as divine judgment, yet recorded the people's repentance and Rehoboam's partial deliverance (2 Chronicles 12:5–8).</p><p>Other notable Shemaiahss include: the false prophet who opposed Jeremiah's counsel during the exile in Babylon (Jeremiah 29:24–32); a Levite involved in bringing the ark to Jerusalem in David's time (1 Chronicles 15:8, 11); a scribe who recorded the priestly divisions under David (1 Chronicles 24:6); several who participated in the wall rebuilding under Nehemiah (Nehemiah 3:29; 12:34–42); and men who had married foreign wives (Ezra 10:21, 31). The name's extraordinary frequency reflects its pious expression of answered prayer.</p>",
        "hitchcock_meaning": "that hears or obeys the Lord",
        "source_ids": {"easton": "shemaiah", "smith": "shemaiah", "isbe": "shemaiah"},
        "key_refs": ["1 Kings 12:22", "2 Chronicles 12:5", "Jeremiah 29:24", "Nehemiah 3:29"]
    },
    "shemariah": {
        "id": "shemariah",
        "term": "Shemariah",
        "category": "people",
        "intro": "<p>Shemariah (meaning: <em>whom Jehovah guards</em> or <em>Jehovah has kept</em>) is the name of three individuals in the Old Testament. The first was a Benjamite warrior of the ambidextrous soldiers who crossed to David at Ziklag before his accession, one of Jeroham's sons from Gedor (1 Chronicles 12:5). The second and third were among those Israelites who had married foreign wives and agreed to put them away in response to Ezra's reform of the covenant community (Ezra 10:32, 41).</p><p>Beyond these notices, no individual narratives about any of the three Shemariahss are recorded. The first represents the category of warriors who chose David's cause over Saul's before the monarchy was settled, while the latter two represent the community members who responded to Ezra's challenge to covenant faithfulness. The name expresses confidence in divine protection and was apparently in common use in the early monarchy and restoration periods.</p>",
        "hitchcock_meaning": "God is my guard",
        "source_ids": {"easton": "shemariah", "smith": "shemariah", "isbe": "shemariah"},
        "key_refs": ["1 Chronicles 12:5", "Ezra 10:32"]
    },
    "shemeber": {
        "id": "shemeber",
        "term": "Shemeber",
        "category": "people",
        "intro": "<p>Shemeber (meaning: <em>soaring on high</em> or <em>lofty flight</em>) was the king of Zeboiim, one of the five cities of the plain of the Jordan valley (the Pentapolis), who joined the coalition against Chedorlaomer in the rebellion of Genesis 14:2. After twelve years of subjection to Chedorlaomer king of Elam and his allied kings from the east, the five kings — including Shemeber of Zeboiim — rose in revolt in the thirteenth year and engaged the eastern coalition in the valley of Siddim.</p><p>The battle went badly for the five kings of the plain: they were defeated, and the city of Sodom was plundered along with its inhabitants, including Lot. This defeat prompted Abraham's military rescue of Lot with his trained household servants, which in turn led to the famous meeting with Melchizedek at the valley of Shaveh. Shemeber and his fellow kings represent the pre-destruction political structure of the region that was obliterated in the divine judgment of Sodom and Gomorrah (Genesis 19).</p>",
        "hitchcock_meaning": "illustrious name, lofty flight",
        "source_ids": {"easton": "shemeber", "smith": "shemeber", "isbe": "shemeber"},
        "key_refs": ["Genesis 14:2"]
    },
    "sheminith": {
        "id": "sheminith",
        "term": "Sheminith",
        "category": "concepts",
        "intro": "<p>Sheminith (Hebrew: <em>eighth</em>) is a musical term appearing in the headings of Psalms 6 and 12 and in 1 Chronicles 15:21, where certain Levitical musicians were appointed to play on harps <em>on the sheminith</em>. The term most likely refers to the octave — the eighth note of a musical scale — and indicates either a specific pitch register or a type of instrument tuned to the lower octave.</p><p>Ancient understanding of the sheminith placed it in contrast to the <em>alamoth</em> (possibly the soprano register, associated with young women's voices) mentioned in the same Chronicler's passage (1 Chronicles 15:20). If this interpretation is correct, the sheminith designated the bass or tenor register, and the instruments playing on it would have produced the deeper harmonies of the Levitical ensemble. The presence of technical musical vocabulary in the Psalm headings reflects the sophisticated liturgical music culture of the Jerusalem temple, though the precise meaning of these terms was lost relatively early in the tradition.</p>",
        "hitchcock_meaning": "eighth, by octaves",
        "source_ids": {"easton": "sheminith", "smith": "sheminith", "isbe": "sheminith"},
        "key_refs": ["Psalms 6:1", "Psalms 12:1", "1 Chronicles 15:21"]
    },
    "shemiramoth": {
        "id": "shemiramoth",
        "term": "Shemiramoth",
        "category": "people",
        "intro": "<p>Shemiramoth (meaning: <em>most high name</em> or <em>height of the heavens</em>) is the name of two Levites in the period of David. The first was a Levite of the second rank appointed to play on psalteries (harps of lower pitch) when the ark was brought from the house of Obed-edom to Jerusalem (1 Chronicles 15:18, 20). He continued in Levitical service before the ark in Jerusalem after its installation (1 Chronicles 16:5).</p><p>The second Shemiramoth was one of the Levites sent by King Jehoshaphat throughout the cities of Judah in the third year of his reign as part of a teaching mission — bringing the Book of the Law to instruct the people alongside the priests and other Levites (2 Chronicles 17:8). This itinerant teaching initiative represented Jehoshaphat's effort to ground his kingdom's reform in the knowledge of God's law among the common people. Both Shemiramoths represent the Levitical class's dual function in Israel: musical worship in the sanctuary and teaching of the Torah in the community.</p>",
        "hitchcock_meaning": "name of the heavens",
        "source_ids": {"easton": "shemiramoth", "isbe": "shemiramoth"},
        "key_refs": ["1 Chronicles 15:18", "1 Chronicles 16:5", "2 Chronicles 17:8"]
    },
    "shemuel": {
        "id": "shemuel",
        "term": "Shemuel",
        "category": "people",
        "intro": "<p>Shemuel (meaning: <em>heard of God</em> or <em>name of God</em>) is a Hebrew form of the name Samuel, borne by three distinct individuals in the Old Testament. The first was the son of Ammihud and the representative of the tribe of Simeon appointed to assist in the division of the land of Canaan among the tribes (Numbers 34:20). The second was the son of Tola and a chief of the tribe of Issachar, listed in the genealogy of 1 Chronicles 7:2.</p><p>The third Shemuel was a grandson of Samuel the prophet through his son Joel, listed in 1 Chronicles 6:33 as an ancestor of Heman the musician who served before the tabernacle in David's time. This genealogical connection links the great prophet Samuel to the Levitical musical tradition of the Davidic era. The name's meaning — affirming that God has heard — reflects the circumstances of the birth of Samuel the prophet, whose mother Hannah cried out to God in her barrenness and whose son's name memorialized the divine answer to her prayer.</p>",
        "hitchcock_meaning": "heard or asked of God",
        "source_ids": {"easton": "shemuel", "smith": "shemuel", "isbe": "shemuel"},
        "key_refs": ["Numbers 34:20", "1 Chronicles 7:2", "1 Chronicles 6:33"]
    },
    "shen": {
        "id": "shen",
        "term": "Shen",
        "category": "places",
        "intro": "<p>Shen (meaning: <em>a tooth</em> or <em>tooth-like crag</em>) was the name given to a rock or crag that served as one of the boundary markers defining the location where Samuel set up the Ebenezer stone after Israel's decisive victory over the Philistines (1 Samuel 7:12). The stone was placed <em>between Mizpeh and Shen</em>, memorializing God's help: <em>Hitherto hath the Lord helped us</em>.</p><p>The tooth-shaped rock from which Shen takes its name was likely a prominent limestone outcrop in the hill country of Benjamin, a natural landmark recognizable to people of the region. It is mentioned only in this one verse and cannot be located with certainty today. The victory at Mizpeh that the Ebenezer stone commemorated represented a major turning point: the Philistines who had taken the ark of the covenant were repelled, and Israel recovered the cities they had lost. The stone of help marked the boundary between the preceding era of defeat and a new beginning under Samuel's leadership.</p>",
        "hitchcock_meaning": "tooth, ivory, changed",
        "source_ids": {"easton": "shen", "smith": "shen", "isbe": "shen"},
        "key_refs": ["1 Samuel 7:12"]
    },
    "shenir": {
        "id": "shenir",
        "term": "Shenir",
        "category": "places",
        "intro": "<p>Shenir (also written <em>Senir</em>) was the Amorite name for Mount Hermon, the great snow-capped peak at the northern boundary of the promised land. Deuteronomy 3:9 clarifies the multiple names for the same summit: <em>which Hermon the Sidonians call Sirion; and the Amorites call it Shenir.</em> The mountain thus had at least three distinct names used by different peoples of the region: Hermon (used by Israel and generally), Sirion (Sidonian/Phoenician), and Shenir (Amorite).</p><p>Shenir appears in Song of Solomon 4:8 in a poetic invitation: <em>Come with me from Lebanon, my spouse, with me from Lebanon: look from the top of Amana, from the top of Shenir and Hermon.</em> Here the two names appear together, perhaps distinguishing a southern peak from the main summit. Ezekiel 27:5 records that the fir trees of Shenir were used for planking in the ships of Tyre, indicating the mountain's extensive cedar and fir forests that supplied timber for Phoenician maritime construction.</p>",
        "hitchcock_meaning": "announcement of the lamp of sleep",
        "source_ids": {"easton": "shenir", "smith": "shenir", "isbe": "shenir"},
        "key_refs": ["Deuteronomy 3:9", "Song of Solomon 4:8", "Ezekiel 27:5"]
    },
    "sheol": {
        "id": "sheol",
        "term": "Sheol",
        "category": "concepts",
        "intro": "<p>Sheol (Hebrew, often rendered <em>the grave</em>, <em>hell</em>, or <em>the pit</em> in older translations, and transliterated as <em>Sheol</em> in modern versions) designates in the Old Testament the realm of the dead — the place to which all the deceased descend, righteous and wicked alike. It is portrayed as a shadowy underworld beneath the earth (Numbers 16:30–33; Deuteronomy 32:22; Job 26:6), a land of silence and darkness (Psalm 115:17; Job 10:21–22) from which return was impossible.</p><p>The Hebrew concept of Sheol does not clearly distinguish between the fates of the righteous and wicked, though some texts hint at degrees of existence within it (Isaiah 14:9–11; Ezekiel 32:17–32). It corresponds to the Greek <em>Hades</em> used in the Septuagint. The New Testament develops a sharper distinction, with Hades reserved for the wicked (Luke 16:23; Revelation 20:13–14) while the righteous dead dwell with Christ in paradise. The resurrection of Christ is described as his not being abandoned to Hades (Acts 2:27, quoting Psalm 16:10), marking the beginning of death's defeat.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sheol", "isbe": "sheol"},
        "key_refs": ["Numbers 16:33", "Psalms 16:10", "Acts 2:27", "Revelation 20:14"]
    },
    "shepham": {
        "id": "shepham",
        "term": "Shepham",
        "category": "places",
        "intro": "<p>Shepham (meaning: <em>a treeless place</em> or <em>bare</em>) was a location on the northeastern boundary of the promised land as defined by God through Moses in Numbers 34:10–11. The boundary line was to run from Hazar-enan to Shepham, then descend from Shepham to Riblah on the east side of Ain. This northeastern border description places Shepham somewhere in the region between the headwaters of the Jordan and the Syrian highlands north of Dan.</p><p>The precise identification of Shepham is uncertain. It appears only in this boundary text and in no narrative context. The fact that the boundary text of Numbers 34 describes an idealized or aspirational northern extent of the land — one never fully realized in Israel's actual settlement — means that Shepham's location matters primarily for understanding the scope of the divine promise rather than Israel's historical territory. The northeastern boundary of the promised land in this passage extends significantly further north than Israel ever consistently controlled.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "shepham", "smith": "shepham", "isbe": "shepham"},
        "key_refs": ["Numbers 34:10", "Numbers 34:11"]
    },
    "shephatiah": {
        "id": "shephatiah",
        "term": "Shephatiah",
        "category": "people",
        "intro": "<p>Shephatiah (meaning: <em>judged of the Lord</em> or <em>Jehovah is judge</em>) is the name of several individuals across several centuries of Israelite history. The most prominent was the fifth son of David, born to Abital in Hebron during the early years of his reign (2 Samuel 3:4; 1 Chronicles 3:3). He does not play a major role in the subsequent Davidic narratives, though his inclusion in the royal family list is significant.</p><p>Other notable bearers of the name include: a Benjamite warrior who joined David at Ziklag (1 Chronicles 12:5); a Simeonite officer under David (1 Chronicles 27:16); a son of King Jehoshaphat who was killed when his brother Jehoram seized power (2 Chronicles 21:2, 4); an ancestor of returnees from Babylon (Ezra 2:4; Nehemiah 7:9); and crucially, a prince in Jerusalem during Jeremiah's ministry who was among those who had the prophet thrown into a muddy cistern for his message that resistance to Babylon was futile (Jeremiah 38:1–6). This last Shephatiah represents the hostile establishment that sought to silence the prophet.</p>",
        "hitchcock_meaning": "God is judge",
        "source_ids": {"easton": "shephatiah", "smith": "shephatiah", "isbe": "shephatiah"},
        "key_refs": ["2 Samuel 3:4", "Jeremiah 38:1", "Ezra 2:4", "2 Chronicles 21:2"]
    },
    "shepherd": {
        "id": "shepherd",
        "term": "Shepherd",
        "category": "concepts",
        "intro": "<p>The shepherd was a central figure in the pastoral economy of the ancient Near East, responsible for guiding flocks to pasture and water, protecting them from predators and thieves, tending the injured and sick, and keeping account of every animal. The patriarchs Abraham, Isaac, and Jacob were all shepherds; Moses tended his father-in-law's flocks at Midian when God appeared to him in the burning bush; and David was called from following the sheep to shepherd God's people Israel (Psalm 78:70–72).</p><p>The shepherd metaphor pervades biblical theology as the primary image for divine and human leadership. God is Israel's shepherd (Psalm 23; Isaiah 40:11), the leaders of Israel are shepherds whose failure brings prophetic condemnation (Ezekiel 34; Jeremiah 23:1–4; Zechariah 11), and God promises to shepherd his flock directly through the Davidic Messiah (Ezekiel 34:23–24). Jesus claimed this role explicitly: <em>I am the good shepherd: the good shepherd giveth his life for the sheep</em> (John 10:11). The birth announcement of the Messiah was made first to shepherds keeping watch over their flocks by night (Luke 2:8–20), and the risen Christ commissioned Peter with the pastoral charge to <em>feed my sheep</em> (John 21:16–17).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "shepherd", "smith": "shepherd", "isbe": "shepherd"},
        "key_refs": ["John 10:11", "Psalms 23:1", "Ezekiel 34:23", "Isaiah 40:11"]
    },
    "sherebiah": {
        "id": "sherebiah",
        "term": "Sherebiah",
        "category": "people",
        "intro": "<p>Sherebiah (meaning: <em>flame of the Lord</em> or <em>Jehovah has brought the heat</em>) was a leading Levite of the post-exilic community, prominent in the records of Ezra and Nehemiah. Ezra sought capable Levites for the return journey to Jerusalem and specifically asked for Sherebiah from the community at Casiphia; he is described as <em>a chief man, and of the sons of Mahli, the son of Levi</em> — making him a man of Levitical standing whose recruitment required special effort (Ezra 8:17–18).</p><p>Sherebiah's subsequent service was extensive: he was among the Levites entrusted with the silver, gold, and temple vessels for the journey (Ezra 8:24); he assisted in explaining the law during Ezra's great public reading (Nehemiah 8:7); he led praise and confession in the great assembly of Nehemiah 9 (Nehemiah 9:4–5); and he sealed the covenant renewal document (Nehemiah 10:12). He is also listed among the leading Levites who came up with Zerubbabel (Nehemiah 12:8). Sherebiah stands as one of the most prominent Levitical figures of the entire restoration period.</p>",
        "hitchcock_meaning": "heat of the Lord",
        "source_ids": {"easton": "sherebiah", "smith": "sherebiah", "isbe": "sherebiah"},
        "key_refs": ["Ezra 8:18", "Nehemiah 8:7", "Nehemiah 9:4", "Nehemiah 10:12"]
    },
    "sheresh": {
        "id": "sheresh",
        "term": "Sheresh",
        "category": "concepts",
        "intro": "<p>Sheresh (meaning: <em>root</em>) was a son of Machir and grandson of Manasseh, mentioned in the genealogical record of 1 Chronicles 7:16. His mother was Maachah, the wife of Machir, and his brothers included Peresh. The genealogical information is concise and sparse: only the name, parentage, and a bare reference to his son Ulam and nephew Rakem are supplied in 1 Chronicles 7:16–17.</p><p>No narrative events or individual achievements are recorded for Sheresh beyond this genealogical listing. He represents one of many individuals preserved in the Chronicler's tribal genealogies who are otherwise unknown in the biblical narrative. His inclusion in the Manassite genealogy reflects the Chronicler's comprehensive effort to document the family structures of all twelve tribes, particularly the half-tribe of Manasseh whose complex clan divisions across both sides of the Jordan required careful record-keeping.</p>",
        "hitchcock_meaning": "root, navel",
        "source_ids": {"easton": "sheresh", "smith": "sheresh", "isbe": "sheresh"},
        "key_refs": ["1 Chronicles 7:16"]
    },
    "sherezer": {
        "id": "sherezer",
        "term": "Sherezer",
        "category": "concepts",
        "intro": "<p>Sherezer was one of two men sent by the men of Bethel to the house of God to inquire of the priests and prophets whether the fasts observed in the fifth and seventh months should continue to be kept during the second year of Darius (Zechariah 7:2). The delegation, coming from the community that had returned to the land, raised a question about the relevance of the mourning fasts commemorating the destruction of the temple and Jerusalem, now that the rebuilding was underway.</p><p>The Lord's response through Zechariah (chapters 7–8) reoriented the question away from ritual observance toward the ethical demands of justice, mercy, and compassion that the fasts were meant to cultivate. The name Sherezer is of Assyrian or Babylonian origin, reflecting the cultural milieu of the returnees who had grown up in the exile. No further information about Sherezer is given beyond this single narrative mention.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sherezer", "smith": "sherezer", "isbe": "sherezer"},
        "key_refs": ["Zechariah 7:2"]
    },
    "sheriffs": {
        "id": "sheriffs",
        "term": "Sheriffs",
        "category": "concepts",
        "intro": "<p>Sheriffs appear once in the Authorized Version, in Daniel 3:2–3, in the list of Babylonian officials summoned by Nebuchadnezzar to the dedication of his golden image on the plain of Dura. The Aramaic word translated <em>sheriff</em> (<em>tiphtaye</em>) designates a class of legal or judicial officers, possibly district administrators responsible for law enforcement in the provinces of the Babylonian empire.</p><p>The list in Daniel 3 names seven or eight categories of Babylonian officials — satraps, governors, deputies, sheriffs, treasurers, counselors, judges, and rulers — representing the entire administrative hierarchy of the empire. Their summoning to bow before the image, and the death penalty decreed for those who refused, formed the backdrop for the testing of Shadrach, Meshach, and Abednego, who refused to bow and were cast into the fiery furnace. The precision of the title list reflects the authentic flavor of Babylonian court practice that characterizes the Aramaic sections of Daniel.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sheriffs"},
        "key_refs": ["Daniel 3:2", "Daniel 3:3"]
    },
    "sheshach": {
        "id": "sheshach",
        "term": "Sheshach",
        "category": "places",
        "intro": "<p>Sheshach is a name appearing twice in Jeremiah (25:26; 51:41) that is widely understood as a coded designation for Babylon, employing the <em>atbash</em> cipher — a simple substitution code in which the letters of the Hebrew alphabet are reversed (aleph = taw, beth = shin, etc.), so that the letters of Babel (Babylon) become the letters of Sheshach. The Revised Version and most modern translations note this equation explicitly.</p><p>In Jeremiah 25:26, after listing the nations that will drink the cup of God's wrath, the prophecy culminates: <em>and the king of Sheshach shall drink after them</em> — placing Babylon last and greatest among those destined for judgment. In Jeremiah 51:41, the fall of Babylon is lamented with the same term: <em>How is Sheshach taken! and how is the praise of the whole earth surprised!</em> The use of the cipher may have served as a measure of protection for the prophet or scribe, or it may be a literary device emphasizing the totality of Babylon's fall — even its name will be obscured and overcome.</p>",
        "hitchcock_meaning": "bag of flax",
        "source_ids": {"easton": "sheshach", "smith": "sheshach", "isbe": "sheshach"},
        "key_refs": ["Jeremiah 25:26", "Jeremiah 51:41"]
    },
    "sheshai": {
        "id": "sheshai",
        "term": "Sheshai",
        "category": "people",
        "intro": "<p>Sheshai (meaning: <em>whitish</em> or <em>six</em>) was one of the three sons of Anak — the gigantic pre-Israelite inhabitants of the hill country of Canaan — encountered by the Israelite spies at Hebron during the wilderness reconnaissance (Numbers 13:22). The three sons of Anak named are Sheshai, Ahiman, and Talmai, and their stature contributed to the fearful report of the ten faithless spies, who said Israel was like grasshoppers compared to these men (Numbers 13:33).</p><p>Sheshai and his brothers were eventually expelled from Hebron by Caleb, who at eighty-five years old claimed the hill country as his inheritance and drove out the three Anakites (Joshua 15:14; Judges 1:10). Their defeat at Caleb's hand vindicates Joshua's minority report from forty-five years earlier that the land could be taken with God's help, and it demonstrates that the very enemies whose size had caused ten spies to despair were entirely within the capability of a man walking in faith.</p>",
        "hitchcock_meaning": "six, mercy, linen",
        "source_ids": {"easton": "sheshai", "smith": "sheshai", "isbe": "sheshai"},
        "key_refs": ["Numbers 13:22", "Joshua 15:14", "Judges 1:10"]
    },
    "sheshbazzar": {
        "id": "sheshbazzar",
        "term": "Sheshbazzar",
        "category": "people",
        "intro": "<p>Sheshbazzar (meaning possibly: <em>O sun-god, defend the lord</em> or <em>fire-worshipper</em>) was the prince of Judah to whom Cyrus king of Persia entrusted the gold and silver vessels of the Jerusalem temple when he issued his famous decree permitting the Jews to return and rebuild (Ezra 1:8–11). Cyrus appointed Sheshbazzar as governor and charged him with bringing these five thousand four hundred articles — taken by Nebuchadnezzar — back to Jerusalem.</p><p>Sheshbazzar is also said to have laid the foundations of the temple (Ezra 5:14–16). Many scholars identify him with Zerubbabel, since both are called governor and both are credited with beginning the temple foundation, while others distinguish them as separate individuals — possibly uncle and nephew in the Davidic line. If Sheshbazzar is the same as Shenazzar listed in 1 Chronicles 3:18 as a son of Jehoiachin, he was Zerubbabel's uncle. His role as the initial leader of the restoration connects him to the fulfillment of Jeremiah's prophecy of return after seventy years of exile.</p>",
        "hitchcock_meaning": "joy in tribulation",
        "source_ids": {"easton": "sheshbazzar", "smith": "sheshbazzar", "isbe": "sheshbazzar"},
        "key_refs": ["Ezra 1:8", "Ezra 1:11", "Ezra 5:14", "Ezra 5:16"]
    },
    "sheth": {
        "id": "sheth",
        "term": "Sheth",
        "category": "concepts",
        "intro": "<p>Sheth appears in two distinct biblical contexts. In Numbers 24:17, Balaam's fourth oracle contains the enigmatic poetic line: <em>and shall smite the corners of Moab, and destroy all the children of Sheth.</em> The Revised Version renders <em>children of Sheth</em> as <em>sons of tumult</em> (from the Hebrew <em>sheth</em>, tumult or pride), treating it as a poetic synonym for the warlike nations rather than a proper name. Some interpreters, however, have proposed that <em>Sheth</em> refers to a specific tribe or to Seth the son of Adam, making all humanity the object of the prophecy.</p><p>The second occurrence is in 1 Chronicles 1:1, where Sheth appears in the genealogy from Adam to Abraham, equivalent to Seth the son of Adam (from the Hebrew <em>Shet</em>). This reflects the use of variant spellings in the biblical text for the same figure. The Balaam oracle in Numbers 24 is typically understood as a messianic prophecy pointing to a future king from Israel who will achieve universal dominion — applied in Jewish and Christian tradition to the Davidic Messiah.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "sheth", "smith": "sheth", "isbe": "sheth"},
        "key_refs": ["Numbers 24:17", "1 Chronicles 1:1"]
    },
    "shethar": {
        "id": "shethar",
        "term": "Shethar",
        "category": "people",
        "intro": "<p>Shethar (meaning: <em>a star</em> or possibly of Persian origin meaning <em>commander</em>) was one of the seven princes of Persia and Media who had special access to the king's presence and sat first in the kingdom under Ahasuerus (Xerxes), as listed in Esther 1:14. These seven counselors formed the inner circle of the Persian royal court and were consulted when Queen Vashti refused the king's command to appear before his banquet guests.</p><p>It was these princes who advised the king that Vashti's refusal, if unpunished, would set a dangerous precedent for wives throughout the empire to despise their husbands. Their counsel led to Vashti's removal and ultimately to the beauty contest that brought Esther into the palace. Shethar and his colleagues represent the Persian administrative aristocracy whose power and influence were considerable — the same class of advisors from whom Haman later emerged as the king's chief minister. The names of the seven princes are Persian in character, consistent with the historical setting of the book.</p>",
        "hitchcock_meaning": "star, spy",
        "source_ids": {"easton": "shethar", "smith": "shethar", "isbe": "shethar"},
        "key_refs": ["Esther 1:14"]
    },
    "shethar-boznai": {
        "id": "shethar-boznai",
        "term": "Shethar-boznai",
        "category": "people",
        "intro": "<p>Shethar-boznai (meaning: <em>star of splendour</em> or possibly <em>he who investigates their wickedness</em>) was a Persian official, an associate of Tatnai the governor of the province Beyond the River, who jointly challenged the Jews' right to rebuild the temple in Jerusalem following the return from Babylon (Ezra 5:3, 6). They wrote a letter to King Darius questioning whether the king had authorized the building project and asking for an investigation of the decree of Cyrus.</p><p>The response of Darius confirmed Cyrus's original decree, not only permitting the work but commanding that the costs be paid from the royal treasury and that the needs of the Jewish community for sacrificial animals and provisions be supplied by the governors of the province (Ezra 6:6–12). Darius's decree also imposed severe penalties on anyone who interfered with the work. Shethar-boznai and Tatnai, faced with this royal directive, complied fully and assisted rather than hindered the rebuilding (Ezra 6:13). His name is Persian, consistent with the administrative setting of Ezra 5–6.</p>",
        "hitchcock_meaning": "star of splendor",
        "source_ids": {"easton": "shethar-boznai"},
        "key_refs": ["Ezra 5:3", "Ezra 5:6", "Ezra 6:6", "Ezra 6:13"]
    },
    "sheva": {
        "id": "sheva",
        "term": "Sheva",
        "category": "people",
        "intro": "<p>Sheva is the name of two individuals in Scripture. The first was a son of Caleb (the son of Hezron, not the spy) by his concubine Maachah, and the father of Machbenah and Gibea (1 Chronicles 2:49). This Sheva belongs to the Calebite branch of Judah and appears in the genealogy tracing the clans that settled the region around Hebron and Ziph.</p><p>The second and more prominent Sheva was David's royal secretary, the chief administrative scribe responsible for the king's official correspondence. He appears in 2 Samuel 20:25 under this name, but the same officer is called Seraiah in 2 Samuel 8:17, Shisha in 1 Kings 4:3, and Shavsha in 1 Chronicles 18:16. The variation in spelling across the different biblical lists reflects scribal variation in transliterating an originally foreign name — possibly Egyptian — into Hebrew. His sons Elihoreph and Ahiah continued as royal secretaries under Solomon, making the position hereditary in his family.</p>",
        "hitchcock_meaning": "vanity, elevation, fame",
        "source_ids": {"easton": "sheva", "smith": "sheva", "isbe": "sheva"},
        "key_refs": ["2 Samuel 20:25", "1 Chronicles 2:49"]
    },
    "shewbread": {
        "id": "shewbread",
        "term": "Shewbread",
        "category": "concepts",
        "intro": "<p>The shewbread (Hebrew <em>lechem ha-panim</em>, <em>bread of the face</em> or <em>bread of the presence</em>) consisted of twelve loaves of unleavened bread arranged in two rows of six on the golden table in the holy place of the tabernacle and temple (Exodus 25:30; Leviticus 24:5–9). The twelve loaves represented the twelve tribes of Israel continually presented before the face of God. They were made of fine flour, renewed each Sabbath by the priests, and the removed loaves were eaten exclusively by the priests in the holy place.</p><p>The shewbread symbolized Israel's perpetual covenant relationship with God — continually before his presence, renewed weekly, and shared in sacred meal with the priestly mediators. The most famous narrative incident involving the shewbread is David's taking of the consecrated loaves from the priest Ahimelech at Nob to feed his starving men (1 Samuel 21:1–6), which Jesus cited in his dispute with the Pharisees about Sabbath regulations, arguing that human need can take precedence over cultic restriction (Matthew 12:3–4; Mark 2:25–26; Luke 6:3–4).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "shewbread", "smith": "shewbread"},
        "key_refs": ["Exodus 25:30", "Leviticus 24:5", "1 Samuel 21:1", "Matthew 12:3"]
    },
    "shibboleth": {
        "id": "shibboleth",
        "term": "Shibboleth",
        "category": "concepts",
        "intro": "<p>Shibboleth (Hebrew, meaning either <em>an ear of corn</em> or <em>a flowing stream</em>) became history's most famous linguistic test when the Gileadites used it to identify Ephraimite fugitives at the fords of the Jordan after defeating them in battle (Judges 12:1–6). The Ephraimites, whose dialect lacked the initial <em>sh</em> sound, pronounced the word as <em>Sibboleth</em> — and this phonological difference cost those who mispronounced it their lives. Forty-two thousand Ephraimites are said to have been killed in this manner.</p><p>The episode in Judges 12 arose from Ephraimite jealousy over being excluded from Jephthah's Ammonite campaign, paralleling an earlier complaint about Gideon (Judges 8:1). The word <em>shibboleth</em> has entered English and many other languages as a common noun denoting any password, test, or distinguishing practice that identifies membership in a group — a linguistic or cultural marker used to distinguish insiders from outsiders. Its entry into general usage reflects the enduring power of this biblical story as a parable of how dialect and custom reveal origins.</p>",
        "hitchcock_meaning": "ear of corn, stream, flood",
        "source_ids": {"easton": "shibboleth", "smith": "shibboleth", "isbe": "shibboleth"},
        "key_refs": ["Judges 12:5", "Judges 12:6"]
    },
    "shibmah": {
        "id": "shibmah",
        "term": "Shibmah",
        "category": "places",
        "intro": "<p>Shibmah (also spelled Sibmah and Shebam; meaning: <em>fragrance</em> or <em>coolness</em>) was a town in the territory of Reuben east of the Jordan River, captured from the Amorites and assigned to the tribe of Reuben (Numbers 32:38; Joshua 13:19). The city is mentioned alongside Heshbon, Elealeh, and other Transjordanian cities as part of the Reubenite settlement. It appears in the boundary and possession lists of Reuben and was apparently noted for its vineyards.</p><p>Shibmah became a subject of prophetic lament in the oracles against Moab in Isaiah 16:8–9 and Jeremiah 48:32, where the prophet mourns the destruction of its famous vines — vines whose branches had extended to Jazer and reached even to the sea, and whose vintage cries had ceased. The luxuriance of Shibmah's vineyards makes it a symbol of Moabite prosperity brought to desolation under divine judgment. The prophetic weeping over Shibmah mirrors the weeping over Jazer, capturing the total devastation of the Moabite agricultural heartland.</p>",
        "hitchcock_meaning": "captivity, conversion",
        "source_ids": {"easton": "shibmah", "smith": "shibmah", "isbe": "shibmah"},
        "key_refs": ["Numbers 32:38", "Isaiah 16:8", "Jeremiah 48:32"]
    },
    "shield": {
        "id": "shield",
        "term": "Shield",
        "category": "concepts",
        "intro": "<p>Shields were a fundamental element of ancient Israelite and Near Eastern warfare, coming in several sizes and materials. The large body-shield (<em>tsinnah</em>) was typically made of wood covered with leather, large enough to protect most of the body, and was carried by a separate shield-bearer in front of a warrior (1 Samuel 17:7, 41). The smaller round shield or buckler (<em>magen</em>) was carried by the soldier himself, used for parrying blows in close combat. Solomon made two hundred large shields and three hundred smaller shields of beaten gold for decorative display in the House of the Forest of Lebanon (1 Kings 10:16–17).</p><p>The shield's spiritual significance in Scripture is extensive. God is repeatedly called the shield of his people (Genesis 15:1; Psalm 18:2; Psalm 115:9–11), a metaphor expressing divine protection against enemies. Ephesians 6:16 describes faith as a shield — specifically the large body-shield (<em>thureos</em>) — with which believers can quench all the fiery darts of the evil one, applying the military image to the spiritual warfare of the Christian life. The shields hung on the walls of Tyre (Ezekiel 27:10–11) and the shields captured from enemies became trophies of victory throughout the biblical narrative.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "shield", "smith": "shield", "isbe": "shield"},
        "key_refs": ["1 Samuel 17:7", "Psalms 18:2", "Ephesians 6:16", "Genesis 15:1"]
    },
    "shiggaion": {
        "id": "shiggaion",
        "term": "Shiggaion",
        "category": "concepts",
        "intro": "<p>Shiggaion (from the Hebrew root <em>shagah</em>, meaning <em>to reel about</em> or <em>to err</em>) is a musical term appearing in the heading of Psalm 7 (<em>Shiggaion of David</em>) and in Habakkuk 3:1, where the prophet's prayer-psalm is described as set to <em>Shigionoth</em> (the plural form). The precise musical significance of the term is uncertain, having been lost in the transmission of ancient musical tradition.</p><p>Proposed interpretations include: a dithyrambic or free-flowing musical style characterized by irregular rhythm or passionate movement (resembling the Greek dithyramb); a type of song of lamentation; or a composition of irregular, wandering meter suited to the agitated emotional content of the Psalm. The Septuagint renders it with a word suggesting a psalm sung with understanding. The emotional intensity of Psalm 7 — a cry for deliverance from enemies — and of Habakkuk 3 — a vision of God's terrifying march in judgment — would fit a musical form suited to passionate, spontaneous expression rather than regular strophic structure.</p>",
        "hitchcock_meaning": "a song of trouble or comfort",
        "source_ids": {"easton": "shiggaion", "smith": "shiggaion", "isbe": "shiggaion"},
        "key_refs": ["Psalms 7:1", "Habakkuk 3:1"]
    },
    "shihon": {
        "id": "shihon",
        "term": "Shihon",
        "category": "places",
        "intro": "<p>Shihon (meaning: <em>overturning</em> or <em>ruin</em>) was a town in the tribal territory of Issachar, listed among the cities assigned to that tribe in the boundary and settlement list of Joshua 19:19. It appears in a cluster of Issacharite towns in the eastern Jezreel valley and lower Galilee region, though its precise location is not established with certainty.</p><p>Shihon is mentioned only in this single settlement list and plays no role in any narrative events in the Old Testament. Like many of the minor settlement names in the Joshua boundary lists, it preserves the memory of populated sites in the Iron Age Israelite landscape that were part of the tribal administrative geography even though no significant events were associated with them. The region of Issachar was one of the fertile tribal territories in the northern kingdom, dominated by the agricultural plains of the Jezreel valley and the approaches to Galilee.</p>",
        "hitchcock_meaning": "their turning away, destruction",
        "source_ids": {"easton": "shihon", "smith": "shihon", "isbe": "shihon"},
        "key_refs": ["Joshua 19:19"]
    },
    "shihor": {
        "id": "shihor",
        "term": "Shihor",
        "category": "places",
        "intro": "<p>Shihor (meaning: <em>dark</em> or <em>turbid</em>, referring to the dark waters of the Nile) designates the southwestern boundary of the land of Canaan as given to Israel. In 1 Chronicles 13:5, David assembles all Israel <em>from Shihor of Egypt even unto the entering of Hamath</em> — from the southernmost to the northernmost extent of the promised land. Joshua 13:3 similarly mentions Shihor as lying <em>before Egypt</em>, east of the Nile Delta.</p><p>Most scholars identify Shihor with the Wadi el-Arish (the Brook of Egypt), the natural boundary between Canaan and Egypt in the northern Sinai, though some identify it with the easternmost branch of the Nile Delta (the Pelusiac branch). Isaiah 23:3 refers to the Shihor as a source of grain harvested and transported on the Nile to the trading markets of Tyre, which would suggest the Egyptian Nile itself. The two uses may reflect different periods of usage or different geographical references within the general Egypt-Canaan border region.</p>",
        "hitchcock_meaning": "black, trouble",
        "source_ids": {"easton": "shihor", "isbe": "shihor"},
        "key_refs": ["1 Chronicles 13:5", "Joshua 13:3", "Isaiah 23:3"]
    },
    "shihor-libnath": {
        "id": "shihor-libnath",
        "term": "Shihor-Libnath",
        "category": "places",
        "intro": "<p>Shihor-Libnath (meaning: <em>black-white</em>, or possibly <em>dark stream of Libnath</em>) was a stream or wadi forming part of the southern boundary of the tribal territory of Asher, mentioned in Joshua 19:26. The name may combine <em>Shihor</em> (dark/black, as used of the Nile's dark waters) with <em>Libnath</em> (white), suggesting a river with contrasting characteristics — perhaps one with dark banks and white limestone bed, or joining two streams of different character.</p><p>The identification of Shihor-Libnath is uncertain. Various proposals have connected it with the Nahr ez-Zerqa (the Crocodile River, ancient Nahal Tanninim) on the Sharon plain, or with another watercourse in the Carmel region south of Asher's territory. The boundary context in Joshua 19:24–31 places the stream among the landmarks defining Asher's southern edge, in the vicinity of the Carmel range. Beyond this boundary reference, Shihor-Libnath appears nowhere else in Scripture.</p>",
        "hitchcock_meaning": "black and white",
        "source_ids": {"easton": "shihor-libnath", "isbe": "shihor-libnath"},
        "key_refs": ["Joshua 19:26"]
    },
    "shilhim": {
        "id": "shilhim",
        "term": "Shilhim",
        "category": "places",
        "intro": "<p>Shilhim (meaning: <em>aqueducts</em> or <em>armed men</em>) was a town in the Negev district of the tribal territory of Judah, listed in the settlement list of Joshua 15:32 alongside Ain, Rimmon, and other towns of the southernmost portion of Judah. The same town appears to be called Sharuhen in Joshua 19:6 and Shaaraim in 1 Chronicles 4:31 in parallel lists of Simeonite cities, suggesting either textual variation or a double name.</p><p>Shilhim is mentioned only in these settlement lists and plays no role in any subsequent biblical narrative. Its location in the Negev, the semi-arid region south of Beersheba, places it on the frontier of Judahite settlement, in an area where water management — possibly reflected in the name <em>aqueducts</em> — would have been crucial for habitation. The overlap between Judahite and Simeonite town lists in this region reflects the gradual absorption of the tribe of Simeon into Judah during the later monarchy period.</p>",
        "hitchcock_meaning": "armed men, transports",
        "source_ids": {"easton": "shilhim", "smith": "shilhim", "isbe": "shilhim"},
        "key_refs": ["Joshua 15:32"]
    },
    "shiloah-the-waters-of": {
        "id": "shiloah-the-waters-of",
        "term": "Shiloah, The Waters of",
        "category": "places",
        "intro": "<p>The waters of Shiloah (also spelled Siloah, Siloam) were the gentle, reliable waters flowing from the Gihon spring through Hezekiah's tunnel into the Pool of Siloam in the lower city of Jerusalem. The name Shiloah derives from the Hebrew root <em>shaloach</em>, meaning <em>sent</em> or <em>sending forth</em>, describing the conducted flow of the water through the tunnel. Nehemiah 3:15 references the Pool of Siloah near the king's garden and the stairs of the city of David.</p><p>Isaiah 8:6–7 employs the waters of Shiloah in a famous oracle: because Judah <em>refuseth the waters of Shiloah that go softly</em> and instead fears Rezin and the son of Remaliah, God will bring upon them the powerful flood of the Assyrian army. The gentle, quiet waters of Shiloah become a metaphor for trusting in God's quiet provision and the Davidic covenant, in contrast to the turbulent flood of human military power. In the New Testament, the Pool of Siloam is the site where Jesus sent the man born blind to wash after applying clay to his eyes (John 9:7).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "shiloah-the-waters-of", "smith": "shiloah-the-waters-of"},
        "key_refs": ["Isaiah 8:6", "Nehemiah 3:15", "John 9:7"]
    },
    "shiloh": {
        "id": "shiloh",
        "term": "Shiloh",
        "category": "concepts",
        "intro": "<p>Shiloh carries two distinct meanings in Scripture. As a city, Shiloh was the central Israelite sanctuary town in the hill country of Ephraim where the tabernacle was set up after the conquest and remained for approximately three centuries (Joshua 18:1). It was the annual site of religious assemblies, the location where Hannah prayed and received the promise of Samuel, and the priestly center of Israel under Eli and his sons — until the Philistines captured the ark and apparently destroyed the site (1 Samuel 4; Jeremiah 7:12–14; Psalm 78:60).</p><p>As a title or name, Shiloh appears in Jacob's dying blessing of Judah: <em>The sceptre shall not depart from Judah, nor a lawgiver from between his feet, until Shiloh come; and unto him shall the gathering of the people be</em> (Genesis 49:10). This <em>Shiloh</em> has been widely interpreted in Jewish and Christian tradition as a messianic title meaning <em>the one to whom it belongs</em> (cf. Ezekiel 21:27) or <em>the peaceful one</em> — a prophecy that the royal authority of Judah culminates in a coming king to whom the nations will be gathered. The New Testament sees this fulfilled in Jesus Christ of the tribe of Judah.</p>",
        "hitchcock_meaning": "peace, abundance",
        "source_ids": {"easton": "shiloh", "smith": "shiloh"},
        "key_refs": ["Genesis 49:10", "Joshua 18:1", "1 Samuel 1:3", "Jeremiah 7:12"]
    },
    "shilonite": {
        "id": "shilonite",
        "term": "Shilonite",
        "category": "concepts",
        "intro": "<p>Shilonite is a gentillic designation meaning <em>inhabitant of Shiloh</em>, used in the Old Testament to identify individuals connected with the town of Shiloh in Ephraim. The designation is applied most prominently to Ahijah the prophet, who is consistently identified as <em>Ahijah the Shilonite</em> (1 Kings 11:29; 12:15; 14:2; 15:29; 2 Chronicles 9:29). Ahijah was the prophet who tore his garment into twelve pieces and gave ten to Jeroboam, symbolizing the division of Solomon's kingdom, and who later pronounced doom on Jeroboam's house.</p><p>The term also appears in Nehemiah 11:5 identifying a Judahite settler in Jerusalem named Maaseiah as a Shilonite, and in 1 Chronicles 9:5 in the parallel list. The priestly and prophetic associations of Shiloh — as the location of the tabernacle and the center of Eli's priestly family — gave the designation <em>Shilonite</em> a specific religious weight. Ahijah's connection to the prophetic guild centered at Shiloh links him to the tradition that preceded the monarchy and that continued to speak God's word as an independent voice to the kings.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "shilonite", "isbe": "shilonite"},
        "key_refs": ["1 Kings 11:29", "1 Kings 12:15", "2 Chronicles 9:29"]
    },
    "shimea": {
        "id": "shimea",
        "term": "Shimea",
        "category": "concepts",
        "intro": "<p>Shimea (meaning: <em>the hearing of prayer</em> or <em>fame</em>) is the name of four distinct individuals in the Old Testament, the most prominent being the third son of David by Bathsheba (called also Shammua), listed in 1 Chronicles 3:5 and 14:4. Another Shimea was a son of David's brother Jesse (1 Chronicles 2:13), making him David's nephew — this figure appears in 2 Samuel 21:21 as the father of Jonathan who slew the Philistine giant of Gath with six fingers on each hand and six toes on each foot.</p><p>A third Shimea was a son of Michael in the Levitical genealogy of Gershom (1 Chronicles 6:39), and a fourth was an ancestor of Asaph the musician through Berechiah (1 Chronicles 6:39). The multiplicity of individuals named Shimea across different families and centuries reflects the name's popularity in ancient Israel. The absence of Hitchcock data for this entry reflects the variant spellings under which these figures appear in different manuscript traditions.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "shimea", "smith": "shimea", "isbe": "shimea"},
        "key_refs": ["1 Chronicles 3:5", "2 Samuel 21:21", "1 Chronicles 6:39"]
    },
    "shimeah": {
        "id": "shimeah",
        "term": "Shimeah",
        "category": "people",
        "intro": "<p>Shimeah (meaning: <em>fame</em> or <em>rumour</em>) was a brother of King David, the son of Jesse, also called Shammah (1 Samuel 16:9; 17:13) and Shimma (1 Chronicles 2:13). He appears most dramatically as the father of Jonadab, described as a <em>very subtle</em> (crafty) man who devised the ruse by which Amnon could get Tamar alone — which led to Tamar's rape (2 Samuel 13:3–5). Jonadab later revealed to David that Absalom had killed only Amnon and not all the king's sons (2 Samuel 13:32).</p><p>The same man may be referred to in 2 Samuel 21:21 as the father of Jonathan, who killed the Philistine giant of Gath — though the name there is Shimei or Shimeah in variant textual traditions. As a brother of David, Shimeah belongs to the generation of Jesse's sons who were evaluated by Samuel when God directed him to anoint a king from Jesse's household (1 Samuel 16). He is one of the brothers who went to fight with Saul's army at the time of Goliath's challenge.</p>",
        "hitchcock_meaning": "that is heard",
        "source_ids": {"easton": "shimeah", "smith": "shimeah", "isbe": "shimeah"},
        "key_refs": ["2 Samuel 13:3", "1 Chronicles 2:13", "2 Samuel 21:21"]
    },
    "shimei": {
        "id": "shimei",
        "term": "Shimei",
        "category": "people",
        "intro": "<p>Shimei (meaning: <em>famous</em> or <em>renowned</em>) is one of the most frequently occurring names in the Old Testament, borne by more than a dozen individuals. The most notable is Shimei the son of Gera, a Benjamite of the house of Saul who cursed David with bitter words and threw stones at the king as he fled Jerusalem during Absalom's revolt, calling him a <em>bloody man</em> (2 Samuel 16:5–13). David restrained his men from killing Shimei and received the cursing with notable humility as potentially God's will.</p><p>When David returned victorious, Shimei rushed to meet him, confessed his sin, and begged forgiveness. David swore not to put him to death (2 Samuel 19:16–23), but on his deathbed instructed Solomon to deal wisely with Shimei, not holding him guiltless (1 Kings 2:8–9). Solomon required Shimei to remain in Jerusalem under house arrest; when he violated the restriction to pursue runaway servants to Gath, Solomon had him executed (1 Kings 2:36–46). Other Shimeis include a son of Gershon (Numbers 3:18), a relative of Saul who was loyal to David (1 Chronicles 8:21), and an officer over David's vineyards (1 Chronicles 27:27).</p>",
        "hitchcock_meaning": "that hears or obeys",
        "source_ids": {"easton": "shimei", "smith": "shimei", "isbe": "shimei"},
        "key_refs": ["2 Samuel 16:5", "2 Samuel 19:18", "1 Kings 2:8", "1 Kings 2:44"]
    },
    "shimeon": {
        "id": "shimeon",
        "term": "Shimeon",
        "category": "people",
        "intro": "<p>Shimeon (meaning: <em>hearkening</em> or <em>hearing</em>) was an Israelite of the family of Harim who had taken a foreign wife and was listed among those who agreed to put her away in response to Ezra's covenant reform (Ezra 10:31). He is mentioned in the single verse of Ezra 10:31 among a group of laymen who similarly responded to Ezra's call for covenant faithfulness.</p><p>Beyond this single appearance, nothing further is known about Shimeon. He represents one of the many ordinary members of the post-exilic community whose personal response to the crisis of intermarriage and covenant compromise is preserved in the list of Ezra 10. The name Shimeon is a variant of Simeon, the tribal ancestor of Israel, and its use in this context reflects the continuity of traditional Hebrew names in the restored community that had returned from Babylon.</p>",
        "hitchcock_meaning": "that hears and obeys",
        "source_ids": {"easton": "shimeon", "smith": "shimeon", "isbe": "shimeon"},
        "key_refs": ["Ezra 10:31"]
    },
    "shimhi": {
        "id": "shimhi",
        "term": "Shimhi",
        "category": "concepts",
        "intro": "<p>Shimhi (meaning: <em>famous</em> or <em>my fame</em>) was a Benjamite listed in the genealogical record of 1 Chronicles 8:21 as one of the sons of Shimei (a different person from the Shimei of David's time). The text places him in the Benjamite clan structure recorded in 1 Chronicles 8, which traces the descendants of Benjamin through multiple generations and branches, with particular attention to the Saulide families and the residents of Jerusalem and Aijalon.</p><p>No narrative events are associated with Shimhi beyond his genealogical listing. He represents one of the many named individuals in the Chronicler's extensive tribal genealogies whose names are preserved as records of family lineage without accompanying biographical detail. The genealogies of Benjamin in 1 Chronicles 7–8 are among the most complex in the book, reflecting the historical and administrative importance of Benjamin's territory between Judah and Ephraim.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "shimhi", "smith": "shimhi", "isbe": "shimhi"},
        "key_refs": ["1 Chronicles 8:21"]
    },
    "shimrath": {
        "id": "shimrath",
        "term": "Shimrath",
        "category": "people",
        "intro": "<p>Shimrath (meaning: <em>guardian</em> or <em>watchman</em>) was a Benjamite, one of the sons of Shimhi listed in the genealogy of Benjamin in 1 Chronicles 8:21. He appears alongside his brothers in a brief genealogical notice that records the Benjamite family structure during the period covered by the Chronicler's account. Beyond his inclusion in this tribal record, no events or achievements are attributed to Shimrath in Scripture.</p><p>The name Shimrath, meaning watchman or guard, was a common type in Hebrew naming conventions, expressing either an actual function or a hoped-for quality. His placement in the Benjamite genealogy of 1 Chronicles 8 locates him among the clans that inhabited the territory of Benjamin, the small but strategically vital tribe whose land lay between Jerusalem and the northern tribes. The Chronicler's detailed attention to Benjamite genealogy reflects Benjamin's importance as the tribe that produced Israel's first king, Saul.</p>",
        "hitchcock_meaning": "guarding, observing",
        "source_ids": {"easton": "shimrath", "smith": "shimrath"},
        "key_refs": ["1 Chronicles 8:21"]
    },
    "shimri": {
        "id": "shimri",
        "term": "Shimri",
        "category": "people",
        "intro": "<p>Shimri (meaning: <em>watchman</em>) is the name of three individuals in the Old Testament. The first was a Simeonite, the son of Shemaiah and ancestor of Ziza, listed in the genealogy of Simeon in 1 Chronicles 4:37. The second was the father of Jediael, one of David's mighty men at Ziklag, described as one of the thirty warriors (1 Chronicles 11:45). The third Shimri was a Levite, the son of Hosah of the Merarite family, who was appointed as a gatekeeper of the ark of the covenant, with his father's house assigned to the south gate (1 Chronicles 26:10).</p><p>A fourth Shimri appears in 2 Chronicles 29:13 as a Levite who participated in the cleansing of the temple under Hezekiah's reform, consecrating himself and purifying the house of the Lord from the defilements accumulated under Ahaz. The name's meaning — watchman or guardian — appears in several different family and tribal contexts across the monarchic and Davidic periods.</p>",
        "hitchcock_meaning": "guarding, observing",
        "source_ids": {"easton": "shimri", "smith": "shimri", "isbe": "shimri"},
        "key_refs": ["1 Chronicles 4:37", "1 Chronicles 11:45", "2 Chronicles 29:13"]
    },
    "shimrom": {
        "id": "shimrom",
        "term": "Shimrom",
        "category": "concepts",
        "intro": "<p>Shimrom (also written Shimron) was the fourth son of Issachar, listed in the census of Jacob's family who came into Egypt (Genesis 46:13; 1 Chronicles 7:1). He became the ancestor of the Shimronite clan within Issachar (Numbers 26:24). Beyond his listing in these genealogical registers, no individual narrative is attached to Shimrom himself.</p><p>The name Shimrom is distinguished from the city of Shimron (a Canaanite royal city whose king was defeated by Joshua) only by the spelling convention, and the two should not be confused. As an ancestor of one of Issachar's four major clan divisions, Shimrom's significance lies entirely in his role as a genealogical progenitor. The tribe of Issachar occupied the fertile Jezreel valley and was known for its agricultural wealth and for the wisdom of its leaders in understanding the times (1 Chronicles 12:32).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "shimrom", "smith": "shimrom"},
        "key_refs": ["Genesis 46:13", "1 Chronicles 7:1", "Numbers 26:24"]
    },
    "shimron": {
        "id": "shimron",
        "term": "Shimron",
        "category": "places",
        "intro": "<p>Shimron (meaning: <em>watch-post</em> or <em>watch-height</em>) was an ancient Canaanite royal city whose king joined the northern coalition under Jabin king of Hazor against Joshua and the Israelites. The coalition was defeated at the waters of Merom (Joshua 11:1–9), and the king of Shimron is listed among the thirty-one kings whom Joshua defeated (Joshua 12:20). The city was subsequently assigned to the tribe of Zebulun (Joshua 19:15).</p><p>Shimron's location is generally identified with Tell Shimron or Khirbet Sammuniyeh in the western Jezreel valley, near the foot of the Carmel range, a strategically positioned site overlooking important routes through the valley. The city's role in the northern coalition against Joshua reflects the organized political structure of Canaanite city-states during the Late Bronze Age. After the conquest, Shimron became part of Zebulun's territorial inheritance in the western approaches to the Jezreel valley.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "shimron", "smith": "shimron"},
        "key_refs": ["Joshua 11:1", "Joshua 12:20", "Joshua 19:15"]
    },
    "shimron-meron": {
        "id": "shimron-meron",
        "term": "Shimron-meron",
        "category": "places",
        "intro": "<p>Shimron-meron is listed in Joshua 12:20 among the thirty-one Canaanite kings defeated by Joshua in the conquest of the land. It is widely regarded as either a variant name or an expanded form of Shimron (also in the list), possibly designating the same city with its associated territory. The suffix <em>-meron</em> may identify the city's ruling king by his eponym, distinguish a distinct urban entity from the simpler Shimron, or reflect a different name tradition for the same site.</p><p>Some scholars suggest that Shimron-meron designates a city of the Madon region (since <em>meron</em> may connect to Madon in Joshua 11:1) as distinct from the Zebulunite Shimron. The identification remains uncertain. In any case, its appearance in the defeat list of Joshua 12 places it among the conquered Canaanite city-states of northern Canaan, all of which submitted to Israel's military campaign during the conquest period. Beyond this single reference, the name does not appear elsewhere in the biblical record.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "shimron-meron", "isbe": "shimron-meron"},
        "key_refs": ["Joshua 12:20"]
    },
    "shimshai": {
        "id": "shimshai",
        "term": "Shimshai",
        "category": "people",
        "intro": "<p>Shimshai (meaning: <em>the shining one</em> or <em>sunny</em>) was the secretary or scribe of Rehum the chancellor, a Persian administrative official in Samaria who opposed the rebuilding of Jerusalem's walls in the early restoration period. Shimshai and Rehum wrote an accusatory letter to King Artaxerxes against the Jews, claiming that the rebuilding of Jerusalem's walls would lead to the refusal of taxes and tribute and ultimately to rebellion against the Persian empire (Ezra 4:8–9).</p><p>Their letter succeeded in halting the work: Artaxerxes ordered the construction to cease until further notice (Ezra 4:17–22), and Rehum and Shimshai went to Jerusalem with armed men and compelled the Jews to stop by force (Ezra 4:23). This interruption is part of the broader opposition to the restoration recorded in Ezra 4. The building project was eventually resumed under Darius after the prophets Haggai and Zechariah stirred the community to recommit to completing the temple. Shimshai's name is of Persian or Babylonian origin, reflecting the administrative culture of the Samaritan province.</p>",
        "hitchcock_meaning": "my joy",
        "source_ids": {"easton": "shimshai", "isbe": "shimshai"},
        "key_refs": ["Ezra 4:8", "Ezra 4:9", "Ezra 4:23"]
    },
    "shinab": {
        "id": "shinab",
        "term": "Shinab",
        "category": "people",
        "intro": "<p>Shinab (meaning: <em>cooling</em> or <em>father's tooth</em>) was the king of Admah, one of the five cities of the plain of the Dead Sea region, who joined the coalition that rebelled against Chedorlaomer and the four eastern kings in the battle of the vale of Siddim described in Genesis 14:2. After twelve years of vassalage to Chedorlaomer, the kings of Sodom, Gomorrah, Admah, Zeboiim, and Bela (Zoar) revolted in the thirteenth year, precipitating the military campaign that led to their defeat and the capture of Lot.</p><p>Shinab and his allies were routed at the vale of Siddim, with many of their forces falling into the bitumen pits that characterized the area. The Admah he ruled is known from the prophetic literature as one of the cities destroyed alongside Sodom and Gomorrah (Deuteronomy 29:23; Hosea 11:8), and the divine mercy that spared Israel from such a fate is evoked in Hosea's tender portrayal of God's reluctance to destroy Ephraim as he destroyed Admah. Shinab himself does not reappear in the biblical narrative after Genesis 14.</p>",
        "hitchcock_meaning": "father of change, tooth of the father",
        "source_ids": {"easton": "shinab", "smith": "shinab", "isbe": "shinab"},
        "key_refs": ["Genesis 14:2", "Hosea 11:8", "Deuteronomy 29:23"]
    },
    "shinar-the-land-of": {
        "id": "shinar-the-land-of",
        "term": "Shinar, The Land of",
        "category": "places",
        "intro": "<p>The land of Shinar designates ancient Babylonia — the broad alluvial plain of Mesopotamia watered by the Tigris and Euphrates rivers in what is now southern Iraq. It appears in the Septuagint as <em>Senaar</em> and is identified in Assyrian inscriptions with the region of <em>Shumeru</em> (Sumer), the homeland of one of the world's earliest civilizations. Shinar is first mentioned in Genesis 10:10 as the location of Nimrod's kingdom, encompassing Babel, Erech, Accad, and Calneh.</p><p>The tower of Babel was built in the land of Shinar (Genesis 11:2), making it the site of humanity's archetypal act of collective pride and the subsequent dispersion of languages and peoples. Later, Amraphel king of Shinar was one of the four eastern kings who defeated the cities of the plain in the time of Abraham (Genesis 14:1). Daniel and his companions were brought to Shinar — Babylon — in exile (Daniel 1:2). In Zechariah's apocalyptic vision, the woman in the ephah is transported to the land of Shinar, where a house is built for her (Zechariah 5:11), using the ancient name to evoke wickedness enthroned in its primordial seat.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "shinar-the-land-of"},
        "key_refs": ["Genesis 11:2", "Genesis 14:1", "Daniel 1:2", "Zechariah 5:11"]
    },
    "shiphmite": {
        "id": "shiphmite",
        "term": "Shiphmite",
        "category": "concepts",
        "intro": "<p>Shiphmite is a gentillic designation appearing once in 1 Chronicles 27:27, identifying Zabdi as the officer in charge of David's vineyards — <em>over the vineyards was Shimei the Ramathite: over the increase of the vineyards for the wine cellars was Zabdi the Shiphmite.</em> The designation indicates Zabdi's origin or family connection to a place or clan called Shiphmi, though the location of this place is not identified in Scripture.</p><p>Some have proposed that Shiphmite derives from Shepham, a place on the northeastern border of Canaan mentioned in Numbers 34:10–11, suggesting Zabdi may have originated from a family associated with that region. Others connect it to a place called Siphmoth in 1 Samuel 30:28, where David sent gifts after his victory over the Amalekites. In any case, Zabdi's role as manager of David's wine cellars places him among the specialized agricultural administrators of David's royal household, whose careful management of the king's estates was essential to supplying the court.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "shiphmite", "isbe": "shiphmite"},
        "key_refs": ["1 Chronicles 27:27"]
    },
    "shiphrah": {
        "id": "shiphrah",
        "term": "Shiphrah",
        "category": "people",
        "intro": "<p>Shiphrah (meaning: <em>beauty</em> or <em>brightness</em>) was one of the two Hebrew midwives — alongside Puah — commanded by Pharaoh to kill all Hebrew male infants at birth by throwing them into the Nile (Exodus 1:15–21). Instead of obeying, the midwives feared God and allowed the boys to live, telling Pharaoh that the Hebrew women were vigorous and gave birth before the midwives could arrive. This act of civil disobedience on behalf of the vulnerable is celebrated as one of Scripture's earliest examples of human beings choosing the fear of God over obedience to tyrannical human authority.</p><p>As a result of their courage and faithfulness, God blessed both midwives: <em>because the midwives feared God, he made them houses</em> — meaning he established their families and gave them descendants. Shiphrah and Puah are the first named heroes of the exodus story, their courage preceding and making possible the survival of Moses himself. Their names appear in Egyptian documents of the period, lending historical plausibility to the account's setting. The narrative establishes a theme of providential preservation that runs through the entire exodus narrative.</p>",
        "hitchcock_meaning": "that does good, that is beautiful",
        "source_ids": {"easton": "shiphrah", "smith": "shiphrah", "isbe": "shiphrah"},
        "key_refs": ["Exodus 1:15", "Exodus 1:17", "Exodus 1:20", "Exodus 1:21"]
    },
    "shiphtan": {
        "id": "shiphtan",
        "term": "Shiphtan",
        "category": "concepts",
        "intro": "<p>Shiphtan (meaning: <em>judicial</em> or <em>judge-like</em>) was an Ephraimite, the father of Kemuel who was appointed as the representative of the tribe of Ephraim to assist Moses and Eleazar in the division of the promised land among the tribes (Numbers 34:24). Like many of the tribal leaders listed in Numbers 34, Shiphtan himself held no listed office; he is known entirely through his son Kemuel's appointment to the land-division commission.</p><p>Kemuel's role as Ephraim's commissioner in the land allotment reflects the significant status of Ephraim among the tribes — as the leading tribe of the house of Joseph, Ephraim received a generous territorial inheritance in the central highlands. Shiphtan's name, suggesting judicial authority, was perhaps fitting for a man whose son was appointed to an adjudicative role in determining tribal boundaries. Beyond this single genealogical reference, Shiphtan does not appear elsewhere in Scripture.</p>",
        "hitchcock_meaning": "their judgment",
        "source_ids": {"easton": "shiphtan", "smith": "shiphtan", "isbe": "shiphtan"},
        "key_refs": ["Numbers 34:24"]
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
    print(f'BP {__doc__.split(chr(10))[1].strip()}: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
