"""
BP Article Synthesis — a2: Acts of the Apostles → Ahitub
Covers Easton entries: Acts of the Apostles through Ahitub (76 entries)

Sources consulted:
  - data/dictionary/index.json (Easton briefs)
  - data/dictionary/{slug}.json (Easton full HTML + refs, per entry)
  - data/smith/index.json (Smith briefs)
  - data/isbe/index.json (ISBE briefs)
  - data/hitchcock/index.json (name meanings)

Category logic applied:
  - people:   named biblical persons (Hitchcock match or clearly biographical)
  - places:   brief/title contains city, town, sea, river, mount, valley, etc.
  - concepts: biblical books, theological terms, objects, practices, exclamations
  - events:   battles, feasts, exiles (none in this range)

Script: scripts/bp-a2.py
Run: python3 scripts/bp-a2.py
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


# ── Article data ──────────────────────────────────────────────────────────────
ARTICLES = {
    "acts-of-the-apostles": {
        "id": "acts-of-the-apostles",
        "term": "Acts of the Apostles",
        "category": "concepts",
        "intro": "<p>Acts of the Apostles is the fifth and final historical book of the New Testament, forming a direct sequel to the Gospel of Luke. Written by Luke, the physician and companion of Paul, its narrative begins where the Gospel ends — with the risen Christ's final commission and ascension — and traces the expansion of the early church from Jerusalem through Judea and Samaria to Rome. The opening verse addresses the same Theophilus named in Luke's Gospel, establishing the two-volume unity of the Lukan corpus.</p><p>The book covers roughly three decades of apostolic history, from Pentecost (c. A.D. 30) to Paul's Roman imprisonment (c. A.D. 62). Its two dominant figures are Peter, who dominates the first half (chapters 1–12), and Paul, whose three missionary journeys and trials occupy the second (chapters 13–28). Acts is the primary historical source for the missionary expansion of first-century Christianity and documents the transition of the gospel from a Jewish movement in Jerusalem to a Gentile-inclusive faith reaching the heart of the Roman Empire.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "acts-of-the-apostles", "smith": "acts-of-the-apostles", "isbe": "acts-of-the-apostles"},
        "key_refs": ["Luke 1:1", "Acts 1:1", "Colossians 4:14", "2 Timothy 4:11"]
    },
    "adah": {
        "id": "adah",
        "term": "Adah",
        "category": "people",
        "intro": "<p>Adah (meaning <em>ornament</em> or <em>an assembly</em>) is the name of two women in the Old Testament. The first was one of Lamech's two wives in the antediluvian period, and the mother of Jabal, the ancestor of those who dwell in tents and raise livestock, and Jubal, the ancestor of those who play the harp and flute. She is among the earliest named women in Scripture, appearing in the brief but significant genealogy of Cain's line in Genesis 4.</p><p>The second Adah was a wife of Esau and the daughter of Elon the Hittite, also called Bashemath in some references. She is listed among Esau's Canaanite wives whose presence grieved his parents Isaac and Rebekah, and she bore Esau's son Eliphaz, who became the ancestor of the Edomite clans. Though both women share the same name and period of patriarchal history, they belong to distinct narrative contexts separated by several generations.</p>",
        "hitchcock_meaning": "an assembly",
        "source_ids": {"easton": "adah", "smith": "adah", "isbe": "adah"},
        "key_refs": ["Genesis 4:19", "Genesis 4:20", "Genesis 4:23", "Genesis 36:2", "Genesis 36:4"]
    },
    "adam": {
        "id": "adam",
        "term": "Adam",
        "category": "people",
        "intro": "<p>Adam (meaning <em>earthy</em> or <em>red</em>) is the generic Hebrew word for humanity as well as the personal name of the first man. Formed from the dust of the ground and animated by the breath of God, Adam was placed in the Garden of Eden to tend and keep it, and was given dominion over every living creature. The name's connection to the Hebrew <em>adamah</em> (red earth) reflects his origin from the clay of the ground. Adam was the husband of Eve, and together they became the progenitors of the human race.</p><p>The biblical narrative gives Adam a lifespan of 930 years and traces his descendants through Seth, whose line preserved the knowledge of God. The account of Adam's creation, temptation, and fall in Genesis 1–5 establishes the foundational categories of human dignity, marriage, sin, and mortality that run throughout Scripture. The apostle Paul draws directly on Adam's significance in his theology of sin and redemption, describing him as the first representative head of humanity through whom sin entered the world.</p>",
        "hitchcock_meaning": "earthy; red",
        "source_ids": {"easton": "adam", "smith": "adam"},
        "key_refs": ["Genesis 1:27", "Genesis 2:7", "Genesis 3:15", "Genesis 5:4"]
    },
    "adam-a-type": {
        "id": "adam-a-type",
        "term": "Adam, a type",
        "category": "concepts",
        "intro": "<p>The apostle Paul, in Romans 5:14, describes Adam as <em>the figure of him who was to come</em> — that is, a type or foreshadowing of Christ. This typological reading draws a deliberate parallel between the two representative heads of humanity: as Adam's one act of disobedience introduced sin and death into the human race, so Christ's one act of obedience brought justification and life. The comparison is contrastive as much as it is parallel — where Adam failed, Christ succeeds; where Adam's trespass multiplied condemnation, Christ's gift multiplied grace.</p><p>Paul develops this typology most fully in Romans 5:12–21 and again in 1 Corinthians 15:21–22 and 45–49, where he distinguishes the <em>first Adam</em>, a living soul made from earth, from the <em>last Adam</em>, a life-giving spirit from heaven. This framework became foundational for patristic and Reformed theological accounts of original sin, federal headship, and the nature of Christ's atoning work as the second Adam who recapitulates and redeems what the first Adam forfeited.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "adam-a-type"},
        "key_refs": ["Romans 5:14"]
    },
    "adam-the-city-of": {
        "id": "adam-the-city-of",
        "term": "Adam, the city of",
        "category": "places",
        "intro": "<p>Adam was a city situated on the east bank of the Jordan River beside Zarethan, mentioned in Joshua 3:16 in connection with the miraculous crossing of Israel into Canaan. When the priests bearing the ark of the covenant entered the Jordan, the waters flowing downstream were cut off and stood in a heap <em>a great way off, at the city Adam, that is beside Zaretan</em> — allowing the entire nation to cross on dry ground. The site was evidently a significant geographic landmark used to measure the extent of the dam of water that piled up upstream.</p><p>The city is also referenced in 1 Kings 4:12 in Solomon's administrative divisions. Its exact location is debated by scholars, but it is generally identified with Tell ed-Damiyeh at the confluence of the Jabbok and Jordan rivers, where the banks have historically been prone to collapse and temporary blockage — a natural formation that may illuminate the mechanism by which the divine act was accomplished.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "adam-the-city-of"},
        "key_refs": ["Joshua 3:16", "1 Kings 4:12"]
    },
    "adamah": {
        "id": "adamah",
        "term": "Adamah",
        "category": "places",
        "intro": "<p>Adamah (meaning <em>red earth</em>) was a fortified city allotted to the tribe of Naphtali in the distribution of Canaan under Joshua. It is listed among the fortified cities of Naphtali in Joshua 19:36 and is tentatively identified by some scholars with the modern site of Damieh on the west bank of the Jordan, though the identification remains uncertain. The city's name shares the same root as the Hebrew word for ground or soil, suggesting its character as an agricultural settlement in the fertile northern territory.</p><p>Beyond its inclusion in Naphtali's territorial list, Adamah receives no further narrative development in the biblical text. Its significance is primarily administrative, marking the northern allotment boundaries of the tribal inheritance granted to Naphtali during the period of the conquest under Joshua.</p>",
        "hitchcock_meaning": "red earth; of blood",
        "source_ids": {"easton": "adamah", "smith": "adamah", "isbe": "adamah"},
        "key_refs": ["Joshua 19:36"]
    },
    "adamant": {
        "id": "adamant",
        "term": "Adamant",
        "category": "concepts",
        "intro": "<p>Adamant renders the Hebrew <em>shamir</em>, the hardest known substance in the ancient world — most likely corundum, emery, or possibly diamond. The Greek word <em>adamas</em> from which the English term derives means unconquerable or indestructible. In the Old Testament, the adamant stone appears as a figure of unyielding hardness applied both to the human heart and to the prophetic calling. Ezekiel 3:9 records God telling the prophet that his forehead has been made harder than flint or adamant so that he would not shrink from declaring an unwelcome word to a rebellious house.</p><p>Zechariah 7:12 uses the same term for the stubborn heart of the people who refused to hear the law and the words of the former prophets — hearts made like an adamant stone in their resistance to God's word. Jeremiah 17:1 similarly uses a related term for the cutting point of iron and diamond used to engrave sin upon the tablets of the heart. Together these passages use the hardness of the adamant as a moral metaphor for obstinacy in the face of divine instruction.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "adamant", "smith": "adamant", "isbe": "adamant"},
        "key_refs": ["Ezekiel 3:9", "Zechariah 7:12", "Jeremiah 17:1"]
    },
    "adar": {
        "id": "adar",
        "term": "Adar",
        "category": "concepts",
        "intro": "<p>Adar is the twelfth month of the Jewish ecclesiastical calendar and the sixth month of the civil year, corresponding roughly to February–March in the Gregorian calendar. The name is of Babylonian origin, reflecting the influence of the exile on the Hebrew calendar's nomenclature. It is a month of 29 days, occasionally extended to a 30-day intercalary month (<em>Adar Sheni</em>, or Second Adar) in leap years of the Jewish lunar-solar calendar to keep the calendar aligned with the agricultural seasons.</p><p>Adar figures prominently in the book of Esther, where it is the month in which Haman cast the lot (<em>pur</em>) to determine the most auspicious date for the destruction of the Jews — and the month in which that plot was reversed by the courage of Esther and Mordecai. The fourteenth and fifteenth days of Adar became the occasion for the festival of Purim, commemorating the Jewish deliverance in Persia.</p>",
        "hitchcock_meaning": "high; eminent",
        "source_ids": {"easton": "adar", "smith": "adar"},
        "key_refs": ["Esther 3:7"]
    },
    "adbeel": {
        "id": "adbeel",
        "term": "Adbeel",
        "category": "people",
        "intro": "<p>Adbeel (meaning <em>vapor of God</em> or <em>cloud of God</em>) was the third of the twelve sons of Ishmael listed in Genesis 25:13 and 1 Chronicles 1:29. He was a grandson of Abraham through Hagar, and his name heads one of the twelve tribes descended from Ishmael that settled in the territory stretching from Havilah to Shur, east of Egypt. These Ishmaelite clans formed an important network of desert peoples in the region of northwestern Arabia and the Sinai peninsula.</p><p>Adbeel receives no individual narrative treatment in Scripture beyond his genealogical listing. His significance lies in the fulfillment of God's promise to Abraham concerning Ishmael — that he too would become the father of twelve princes and a great nation — mirroring in structure, though not in covenant standing, the twelve tribes descended from Isaac's son Jacob.</p>",
        "hitchcock_meaning": "vapor, or cloud of God",
        "source_ids": {"easton": "adbeel", "smith": "adbeel", "isbe": "adbeel"},
        "key_refs": ["Genesis 25:13", "1 Chronicles 1:29"]
    },
    "addar": {
        "id": "addar",
        "term": "Addar",
        "category": "people",
        "intro": "<p>Addar was a son of Bela, the firstborn son of Benjamin, and thus a grandson of the patriarch Benjamin. He is listed in 1 Chronicles 8:3 among the sons of Bela in the genealogy of the tribe of Benjamin. The name Addar, meaning <em>ample</em> or <em>splendid</em>, appears also in the compound form Ard in Genesis 46:21, where he is listed among the seventy souls who went down to Egypt with Jacob, though the relationship between these two forms is a matter of textual discussion among scholars.</p><p>Addar figures in no individual narrative in Scripture and is known only through the tribal genealogies. His listing in the Benjaminite lineage confirms the early establishment of the clan structure within that tribe during the period of the Egyptian sojourn.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "addar", "smith": "addar", "isbe": "addar"},
        "key_refs": ["1 Chronicles 8:3", "Genesis 46:21"]
    },
    "adder": {
        "id": "adder",
        "term": "Adder",
        "category": "concepts",
        "intro": "<p>Adder is the English translation of several distinct Hebrew words that denote venomous serpents in the Old Testament. The term <em>akshub</em>, rendered adder in Psalm 140:3 and cited by Paul in Romans 3:13, describes a coiling or lying-in-wait serpent. <em>Pethen</em> (Psalm 58:4; 91:13) refers to a serpent that was supposedly deaf to the charmer's call, used as a figure of those who stop their ears against God's word. <em>Tsiphoni</em> (Proverbs 23:32; Isaiah 11:8) describes the serpent whose bite comes with delayed, deadly effect — used as a warning against wine.</p><p>These varied terms reflect the biblical world's awareness of multiple species of dangerous snakes in the Levant and Arabian Peninsula. In prophetic and wisdom literature the adder functions as an image of treachery, lethal power, and the consequences of sin, while in eschatological passages such as Isaiah 11:8 the nursing child playing over the adder's hole pictures the restoration of creation's original harmony.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "adder", "smith": "adder", "isbe": "adder"},
        "key_refs": ["Psalms 140:3", "Romans 3:13", "Psalms 58:4", "Proverbs 23:32", "Isaiah 11:8"]
    },
    "addi": {
        "id": "addi",
        "term": "Addi",
        "category": "people",
        "intro": "<p>Addi (meaning <em>ornament</em> or <em>my witness</em>) appears in Luke's genealogy of Jesus Christ as the son of Cosam and the father of Melchi, placing him in the ancestral line between David and Joseph. He is listed in Luke 3:28 among the generations between Zerubbabel and Neri in the post-exilic portion of the genealogy. As with many figures in the genealogical lists of Luke 3, Addi is known only by name and lineage without further biographical information in the biblical text.</p><p>His inclusion in Luke's genealogy, which traces the descent of Jesus through Mary's line according to many interpreters, reflects Luke's concern to ground the messianic identity of Jesus in the full sweep of Israel's history from Adam forward. Addi occupies a place in the generation following the return from Babylonian exile.</p>",
        "hitchcock_meaning": "my witness; adorned; prey",
        "source_ids": {"easton": "addi", "smith": "addi", "isbe": "addi"},
        "key_refs": ["Luke 3:28"]
    },
    "addon": {
        "id": "addon",
        "term": "Addon",
        "category": "people",
        "intro": "<p>Addon (meaning <em>basis</em> or <em>foundation</em>) was one of the persons named in Nehemiah 7:61 (called Tel-harsha in Ezra 2:59) who returned to Jerusalem from Babylon after the exile but could not demonstrate their genealogical connection to Israel. These returnees came from Tel-melah, Tel-harsha, Cherub, Addon, and Immer, but were unable to prove whether their fathers' houses and descent were of Israel. The passage reflects the importance of genealogical documentation in post-exilic Judah for determining membership in the covenant community.</p><p>The inability to verify ancestry had practical consequences: priests in this group were excluded from serving at the altar until a high priest could consult the Urim and Thummim to determine their status. Addon represents the broader challenge of identity and continuity that faced the Jewish community returning from Babylonian captivity after several generations of displacement.</p>",
        "hitchcock_meaning": "basis; foundation; the Lord",
        "source_ids": {"easton": "addon", "smith": "addon", "isbe": "addon"},
        "key_refs": ["Nehemiah 7:61"]
    },
    "adiel": {
        "id": "adiel",
        "term": "Adiel",
        "category": "people",
        "intro": "<p>Adiel (meaning <em>ornament of God</em> or <em>the witness of the Lord</em>) is the name of three distinct men in the Old Testament. The first was the father of Azmaveth, who served as treasurer over King David's storehouses (1 Chronicles 27:25). The second was a leader of the tribe of Simeon during the reign of Hezekiah whose clan expanded their territory by dispossessing the Hamites and Meunim (1 Chronicles 4:36). The third was an ancestor of Maasiai, a priest who settled in Jerusalem after the return from exile (1 Chronicles 9:12).</p><p>The name Adiel occurs in three separate genealogical and administrative contexts spanning the monarchic and post-exilic periods of Israelite history. None of the three figures receives extended narrative treatment, and they are known only through their listing in the Chronicler's administrative and genealogical records.</p>",
        "hitchcock_meaning": "the witness of the Lord",
        "source_ids": {"easton": "adiel", "smith": "adiel", "isbe": "adiel"},
        "key_refs": ["1 Chronicles 27:25", "1 Chronicles 4:36", "1 Chronicles 9:12"]
    },
    "adin": {
        "id": "adin",
        "term": "Adin",
        "category": "people",
        "intro": "<p>Adin (meaning <em>adorned</em> or <em>voluptuous</em>) is the name of two men mentioned in the post-exilic records of Ezra and Nehemiah. The first is an ancestor of a family of 454 members who returned from Babylonian exile with Zerubbabel, and whose representative Ebed son of Jonathan later returned with a further group of 50 males under Ezra (Ezra 2:15; 8:6). The second Adin was one of the chiefs of the people who set their seal to the covenant of national renewal under Nehemiah (Nehemiah 10:16).</p><p>The name appears to denote a significant clan in post-exilic Judah, with members documented both in the initial return under Zerubbabel and in subsequent waves of immigration. Their participation in the covenant renewal ceremony under Nehemiah indicates their continued prominence in the reconstituted community of Jerusalem.</p>",
        "hitchcock_meaning": "adorned; voluptuous; dainty",
        "source_ids": {"easton": "adin", "smith": "adin", "isbe": "adin"},
        "key_refs": ["Ezra 8:6", "Nehemiah 10:16"]
    },
    "adina": {
        "id": "adina",
        "term": "Adina",
        "category": "people",
        "intro": "<p>Adina (meaning <em>slender</em> or <em>delicate</em>) was a son of Shiza the Reubenite and one of David's thirty heroes — the second tier of his elite military corps below the Three. He is listed in 1 Chronicles 11:42 as having thirty men under his command, suggesting he held a position of some leadership within David's standing army during the consolidation of the kingdom. His Reubenite tribal identity is specifically noted, reflecting the participation of the eastern tribes in David's military organization.</p><p>Beyond his listing in the roster of David's mighty men, Adina receives no individual narrative in Scripture. His inclusion among the heroes who formed the core of David's military strength places him in the early monarchic period, likely during the years when David was establishing his kingdom from Hebron and then Jerusalem.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "adina", "smith": "adina"},
        "key_refs": ["1 Chronicles 11:42"]
    },
    "adino": {
        "id": "adino",
        "term": "Adino",
        "category": "people",
        "intro": "<p>Adino the Eznite is named in 2 Samuel 23:8 as one of David's three chief mighty men, credited with slaying eight hundred men in a single engagement. The text as it stands in the Hebrew of Samuel is difficult, and many scholars believe the name and deed may have been displaced — the parallel passage in 1 Chronicles 11:11 names Jashobeam the Hachmonite as the man who lifted up his spear against three hundred men at one time, and the Septuagint and other ancient versions differ from the Masoretic text at this point.</p><p>Whether Adino the Eznite is an alternative name for Jashobeam or represents a textual difficulty in transmission, the passage belongs to the catalogue of heroic deeds performed by David's elite warriors. These accounts celebrate extraordinary individual valor and form part of the larger narrative of David's military prowess and the loyalty of those who served him.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "adino", "isbe": "adino"},
        "key_refs": ["2 Samuel 23:8"]
    },
    "adjuration": {
        "id": "adjuration",
        "term": "Adjuration",
        "category": "concepts",
        "intro": "<p>An adjuration is a solemn appeal in which one person imposes on another the obligation of performing some act or stating the truth under the sanction of an oath or curse. In biblical usage, adjurations call on the authority of God or of a sworn covenant to bind the one addressed. Saul's rash adjuration forbidding his troops to eat food during battle (1 Samuel 14:24) resulted in a violation by his own son Jonathan, who had not heard the command. Joshua's adjuration at Jericho (Joshua 6:26) cursed anyone who would rebuild the city's walls, a curse later fulfilled in 1 Kings 16:34.</p><p>In the New Testament, the high priest's adjuration of Jesus — <em>I adjure thee by the living God that thou tell us whether thou be the Christ</em> (Matthew 26:63) — represents the formal use of the oath formula in a judicial context. At Ephesus, certain itinerant Jewish exorcists attempted an adjuration invoking Jesus's name without personal faith in him, with disastrous results (Acts 19:13). The practice appears across both testaments as a recognized legal and religious mechanism for demanding truthful testimony or binding compliance.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "adjuration", "isbe": "adjuration"},
        "key_refs": ["1 Samuel 14:24", "Joshua 6:26", "Matthew 26:63", "Acts 19:13"]
    },
    "admah": {
        "id": "admah",
        "term": "Admah",
        "category": "places",
        "intro": "<p>Admah (meaning <em>earthy</em> or <em>red</em>) was one of five cities of the vale of Siddim, grouped with Sodom, Gomorrah, Zeboiim, and Bela (Zoar) in the Jordan plain near the southern end of the Dead Sea. Listed among the cities in the original table of nations (Genesis 10:19), Admah was among the four cities defeated by the alliance of Chedorlaomer and three other kings in the battle described in Genesis 14, and subsequently destroyed by divine judgment alongside Sodom and Gomorrah for the wickedness of their inhabitants.</p><p>The destruction of Admah became a fixed reference point in the prophetic literature as a symbol of total divine judgment. Deuteronomy 29:23 names Admah and Zeboiim alongside Sodom and Gomorrah in describing the desolation the land would suffer if Israel broke the covenant. Hosea 11:8 records a divine lament — <em>How shall I make thee as Admah? How shall I set thee as Zeboiim?</em> — expressing God's hesitation to bring upon the northern kingdom the total destruction that fell on those ancient cities, revealing both the severity of the warning and the depth of divine compassion.</p>",
        "hitchcock_meaning": "earthy; red; bloody",
        "source_ids": {"easton": "admah", "smith": "admah", "isbe": "admah"},
        "key_refs": ["Genesis 10:19", "Deuteronomy 29:23"]
    },
    "adnah": {
        "id": "adnah",
        "term": "Adnah",
        "category": "people",
        "intro": "<p>Adnah (meaning <em>delight</em> or <em>eternal rest</em>) is the name of two men in the Old Testament. The first was a chief of the tribe of Manasseh who deserted Saul's army and joined David at Ziklag before the battle of Jezreel; he was among the commanders from Manasseh who switched their allegiance to the future king (1 Chronicles 12:20). The second Adnah was a military commander under King Jehoshaphat of Judah, placed over 300,000 men of war — the largest of the three divisions of Jehoshaphat's standing army described in 2 Chronicles 17:14.</p><p>Both men appear exclusively in the Chronicler's accounts of the Davidic and Judahite monarchies. The second Adnah's command over the largest division of Jehoshaphat's reorganized military reflects the significant expansion of Judah's defensive capacity during Jehoshaphat's reign, a period of relative peace and religious reform in the southern kingdom.</p>",
        "hitchcock_meaning": "eternal rest",
        "source_ids": {"easton": "adnah", "smith": "adnah", "isbe": "adnah"},
        "key_refs": ["1 Chronicles 12:20", "2 Chronicles 17:14"]
    },
    "adoni-zedec": {
        "id": "adoni-zedec",
        "term": "Adoni-zedec",
        "category": "people",
        "intro": "<p>Adoni-zedec (meaning <em>lord of justice</em> or <em>lord of righteousness</em>) was the Amorite king of Jerusalem at the time of Joshua's conquest of Canaan. When the news of Israel's treaty with Gibeon reached him, he formed a coalition of five Amorite kings — drawing in the rulers of Hebron, Jarmuth, Lachish, and Eglon — to punish Gibeon for its defection and to check Israel's advance. This coalition attacked Gibeon, prompting Joshua to mount a rapid night march from Gilgal in fulfillment of his alliance obligations.</p><p>The resulting battle at Gibeon was one of the most dramatic engagements of the conquest: Joshua's forces routed the coalition, and the pursuit was prolonged by a hailstorm that killed more of the enemy than the sword, and by the miraculous extension of daylight described in Joshua 10:12–14. Adoni-zedec and the four allied kings fled and hid in a cave at Makkedah, where they were captured, executed, and hung on trees until evening in accordance with the law of Deuteronomy 21:23. His defeat opened central and southern Canaan to Israelite control.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "adoni-zedec"},
        "key_refs": ["Joshua 10:1", "Joshua 10:3"]
    },
    "adonibezek": {
        "id": "adonibezek",
        "term": "Adonibezek",
        "category": "people",
        "intro": "<p>Adonibezek (meaning <em>lord of Bezek</em>) was a Canaanite king who ruled the city of Bezek and had subdued seventy petty kings, cutting off their thumbs and great toes and compelling them to gather scraps under his table. Following the death of Joshua, the tribes of Judah and Simeon attacked Bezek, defeated Adonibezek, and inflicted upon him the same mutilation he had practiced against his own captives. Adonibezek himself acknowledged the justice of this retribution: <em>Threescore and ten kings, having their thumbs and their great toes cut off, gathered their meat under my table: as I have done, so God hath requited me</em> (Judges 1:7).</p><p>He was brought to Jerusalem, where he died. The account is notable for its theological interpretation of the lex talionis — the principle that punishment corresponds to the crime — voiced by the defeated king himself. Adonibezek's confession stands as one of the rare instances in the conquest narrative where an enemy explicitly acknowledges the moral justice of Israel's God.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "adonibezek", "smith": "adonibezek", "isbe": "adonibezek"},
        "key_refs": ["Judges 1:4", "Judges 1:7"]
    },
    "adonijah": {
        "id": "adonijah",
        "term": "Adonijah",
        "category": "people",
        "intro": "<p>Adonijah (meaning <em>my Lord is Jehovah</em>) was the fourth son of David, born of Haggith at Hebron, and the heir apparent following the deaths of Amnon, Chileab, and Absalom. As David lay aged and weak, Adonijah — described as very handsome and never checked by his father — assembled a following of Joab and Abiathar the priest and proclaimed himself king at En-rogel without David's knowledge. The countermove by Bathsheba, the prophet Nathan, and the priest Zadok brought the matter to David, who immediately authorized the anointing of Solomon at Gihon.</p><p>When news of Solomon's accession reached the feast at En-rogel, Adonijah's coalition dissolved. He sought sanctuary at the altar, and Solomon initially spared his life on condition of good behavior. Adonijah's subsequent request — made through Bathsheba — for Abishag the Shunammite as wife was interpreted by Solomon as a renewed claim to the throne, and Solomon had him executed. The account is paradigmatic of the dangers of unchecked ambition and the dynamics of succession in the Davidic court.</p>",
        "hitchcock_meaning": "the Lord is my master",
        "source_ids": {"easton": "adonijah", "smith": "adonijah", "isbe": "adonijah"},
        "key_refs": ["2 Samuel 3:4", "1 Kings 1:5", "1 Kings 2:13"]
    },
    "adonikam": {
        "id": "adonikam",
        "term": "Adonikam",
        "category": "people",
        "intro": "<p>Adonikam (meaning <em>the Lord is raised</em> or <em>my Lord has arisen</em>) was the ancestor of a large family who returned from Babylonian exile. Ezra 2:13 lists 666 descendants of Adonikam among those who came back with Zerubbabel in the first return (c. 538 B.C.), making his clan one of the more numerous lay families in the initial restoration. A further group of three sons — Eliphelet, Jeiel, and Shemaiah — with 60 male members returned in Ezra's later expedition (Ezra 8:13).</p><p>Adonikam's name itself may reflect a pious sentiment about the Lord's exaltation, and his family's prominence in both waves of return suggests a well-established clan that maintained its identity and cohesion across the decades of Babylonian captivity. His descendants are also listed among those who sealed the covenant under Nehemiah.</p>",
        "hitchcock_meaning": "the Lord is raised",
        "source_ids": {"easton": "adonikam", "isbe": "adonikam"},
        "key_refs": ["Ezra 2:13"]
    },
    "adoniram": {
        "id": "adoniram",
        "term": "Adoniram",
        "category": "people",
        "intro": "<p>Adoniram (meaning <em>my Lord is most high</em>) was the son of Abda and the official placed over the forced labor (the tribute of conscripted workers) under both David and Solomon. He administered the levy of 30,000 Israelites whom Solomon sent in monthly rotations to Lebanon to cut timber for Hiram of Tyre, as well as the vast labor force employed in the temple and palace construction projects. His name appears also as Adoram and Hadoram in variant passages.</p><p>Adoniram's career ended in violence when Rehoboam sent him to the northern tribes after the division of the kingdom — precisely the man associated with the burden of forced labor — an extraordinarily ill-judged choice. The northern tribes stoned him to death, and Rehoboam fled to Jerusalem in his chariot. Adoniram's murder thus marks the point of no return in the political rupture between north and south, and the narrative underscores the fatal miscalculation of Rehoboam's advisors in how they managed the transition of power.</p>",
        "hitchcock_meaning": "my Lord is most high; Lord of height and grandeur",
        "source_ids": {"easton": "adoniram", "smith": "adoniram", "isbe": "adoniram"},
        "key_refs": ["1 Kings 12:18", "1 Kings 4:6", "1 Kings 5:14"]
    },
    "adoption": {
        "id": "adoption",
        "term": "Adoption",
        "category": "concepts",
        "intro": "<p>Adoption in its biblical sense is the act by which one outside a family is given the name, place, and privileges of a son within that family. The Old Testament records historical instances of adoption — Pharaoh's daughter taking Moses as her son (Exodus 2:10) and Mordecai raising his cousin Esther (Esther 2:7) — but the term's theological significance is developed most fully in the New Testament. Israel as a nation is described as God's adopted son (Exodus 4:22; Hosea 11:1), and Paul lists adoption among the distinctive privileges given to Israel (Romans 9:4).</p><p>The specifically Pauline theology of adoption (Greek <em>huiothesia</em>) describes the standing of believers in Christ. Galatians 4:5 declares that Christ came to redeem those under the law so that believers might receive the adoption of sons, and Romans 8:15 contrasts the spirit of adoption by which believers cry <em>Abba, Father</em> with a spirit of slavery and fear. The full realization of adoption — the redemption of the body — remains a future hope (Romans 8:23). John's Gospel expresses the same reality through the language of becoming children of God by new birth rather than the legal metaphor of adoption.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "adoption", "smith": "adoption", "isbe": "adoption"},
        "key_refs": ["Exodus 2:10", "Romans 9:4", "Galatians 4:5", "Romans 8:15"]
    },
    "adoram": {
        "id": "adoram",
        "term": "Adoram",
        "category": "people",
        "intro": "<p>Adoram is an alternate form of the name Adoniram, referring to the same official who administered forced labor under David and Solomon. The form Adoram appears in 2 Samuel 20:24, where he is listed as being <em>over the levy</em> in David's administrative roster, and in 1 Kings 12:18, where Rehoboam sends him to the northern tribes following the division of the kingdom. The northern Israelites stone him to death in response to Rehoboam's attempt to enforce continued labor obligations — the act that precipitates Rehoboam's flight to Jerusalem.</p><p>The name also appears as Hadoram in 2 Chronicles 10:18. The variations in spelling across the parallel accounts reflect common scribal transmission patterns in the Hebrew text. For the fuller account of this figure's career, see the entry for Adoniram.</p>",
        "hitchcock_meaning": "their beauty; their power",
        "source_ids": {"easton": "adoram", "smith": "adoram", "isbe": "adoram"},
        "key_refs": ["2 Samuel 20:24", "1 Kings 12:18"]
    },
    "adore": {
        "id": "adore",
        "term": "Adore",
        "category": "concepts",
        "intro": "<p>Adoration in Scripture denotes the act of worship and the expression of reverence toward God through prostration, gesture, and address. The forms of adoration in the ancient world included falling upon the face (Genesis 17:3), kneeling (Psalms 95:6), and the kissing of the hand extended toward the object of veneration — a practice the Job passage (31:27) condemns when directed toward celestial bodies. In the worship of Israel, adoration was directed exclusively toward God, and the prohibition of bowing before idols forms a central element of the Decalogue.</p><p>The removal of sandals as an act of reverence before sacred ground — commanded to Moses at the burning bush (Exodus 3:5) and to Joshua before the commander of the Lord's army (Joshua 5:15) — reflects the posture of adoration before divine presence. Isaiah 44:15–17 satirizes the adoration of idols fashioned from wood, contrasting the absurdity of worshipping one's own handicraft with the worship due to the living God. The New Testament's worship language draws on the same range of posture and address, converging on the person of Christ as the object of adoration.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "adore"},
        "key_refs": ["Genesis 17:3", "Psalms 95:6", "Exodus 3:5", "Isaiah 44:15"]
    },
    "adrammelech": {
        "id": "adrammelech",
        "term": "Adrammelech",
        "category": "people",
        "intro": "<p>Adrammelech (meaning <em>the glory or grandeur of the king</em>) refers to two distinct entities in the Old Testament. The first is an idol worshipped by the Sepharvites, a people whom the Assyrians settled in Samaria after the deportation of the northern kingdom. Their cult included the abhorrent practice of burning children in the fire as offerings to Adrammelech and Anammelech (2 Kings 17:31), deities identified with solar or astral worship and possibly associated with the Babylonian Anu or Adad.</p><p>The second Adrammelech was a son of the Assyrian king Sennacherib. Following the miraculous destruction of his army before Jerusalem and Sennacherib's return to Nineveh, Adrammelech and his brother Sharezer assassinated their father in the temple of Nisroch and fled to the land of Ararat. This fulfillment of Isaiah's prophecy against Sennacherib (Isaiah 37:7, 38) is confirmed in part by Babylonian and Assyrian annals, which record a succession crisis following Sennacherib's death in 681 B.C.</p>",
        "hitchcock_meaning": "the cloak, glory, grandeur or power of the king",
        "source_ids": {"easton": "adrammelech", "smith": "adrammelech"},
        "key_refs": ["2 Kings 17:31", "2 Kings 19:37", "Isaiah 37:38"]
    },
    "adramyttium": {
        "id": "adramyttium",
        "term": "Adramyttium",
        "category": "places",
        "intro": "<p>Adramyttium was a seaport city on the coast of Mysia in the Roman province of Asia, situated on a gulf of the Aegean Sea opposite the island of Lesbos. In Paul's day it was a commercially active port with a harbor that gave its name to the surrounding gulf. The city appears in the New Testament at a crucial moment in Paul's journey to Rome: the centurion Julius placed Paul and other prisoners aboard a ship of Adramyttium that was about to sail for the ports of Asia, intending to find a connection to Rome from the Aegean coast (Acts 27:2).</p><p>This Adramyttian vessel carried Paul as far as Myra in Lycia, where he transferred to an Alexandrian ship bound for Italy. The Adramyttium passage is one of the precise navigational details that give the sea-voyage account of Acts 27–28 its character as a firsthand travel narrative, consistent with Luke's presence as a companion on the voyage.</p>",
        "hitchcock_meaning": "the court of death",
        "source_ids": {"easton": "adramyttium", "smith": "adramyttium", "isbe": "adramyttium"},
        "key_refs": ["Acts 27:2"]
    },
    "adria": {
        "id": "adria",
        "term": "Adria",
        "category": "places",
        "intro": "<p>Adria, as used in Acts 27:27, refers not merely to the modern Adriatic Sea between Italy and the Balkan peninsula, but to a broader body of water that in Greco-Roman geographical usage encompassed much of the central and eastern Mediterranean — including the sea south of Italy and west of Greece. The Revised Version renders it <em>the sea of Adria</em>. In the first century, sailors and geographers applied the term loosely to the open sea between Sicily, Crete, and Greece.</p><p>During the storm described in Acts 27, Paul's ship was driven for fourteen nights across the sea of Adria before the sailors took soundings and recognized they were approaching land — subsequently identified as Malta. The broader ancient usage of the term explains how a vessel blown westward from the region of Crete could be described as drifting in Adria while eventually striking the shores of Malta.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "adria", "smith": "adria", "isbe": "adria"},
        "key_refs": ["Acts 27:27"]
    },
    "adriel": {
        "id": "adriel",
        "term": "Adriel",
        "category": "people",
        "intro": "<p>Adriel (meaning <em>flock of God</em>) was the son of Barzillai the Meholathite. Saul gave his elder daughter Merab to Adriel in marriage, though she had earlier been promised to David (1 Samuel 18:19). Merab bore Adriel five sons, who figure in a later and morally difficult episode: during a famine in David's reign, the Gibeonites demanded seven of Saul's male descendants as restitution for Saul's breach of the ancient treaty with their people (2 Samuel 21:1–9). David handed over two sons of Rizpah by Saul and five sons of Merab by Adriel, who were executed at Gibeon at the beginning of the barley harvest.</p><p>The narrative of Rizpah's vigil over the bodies (2 Samuel 21:10–14) is one of the most poignant in the books of Samuel. Adriel himself receives no further mention; he is known only as the husband of Merab and the father of the five sons given to the Gibeonites in the expiation of Saul's bloodguilt.</p>",
        "hitchcock_meaning": "the flock of God",
        "source_ids": {"easton": "adriel", "smith": "adriel", "isbe": "adriel"},
        "key_refs": ["1 Samuel 18:19", "2 Samuel 21:8"]
    },
    "adullam": {
        "id": "adullam",
        "term": "Adullam",
        "category": "places",
        "intro": "<p>Adullam was an ancient Canaanite royal city in the Shephelah — the foothills region between the coastal plain and the Judean highlands — assigned to the tribe of Judah after the conquest (Joshua 12:15; 15:35). It was fortified by Rehoboam as part of his southwestern defensive network (2 Chronicles 11:7) and reoccupied after the exile (Nehemiah 11:30; Micah 1:15). The site is identified with Tell esh-Sheikh Madhkur in the Wadi es-Sur valley.</p><p>Adullam's most famous association is with David's early fugitive years. After his flight from Saul, David took refuge in the cave of Adullam, where he was joined by his brothers, his father's household, and a growing band of about four hundred men who were in distress, in debt, or discontented (1 Samuel 22:1–2). The cave became the base of operations for David's guerrilla period and is recalled in the superscription of several psalms. The <em>mighty men</em> who formed the core of David's later royal army were largely drawn from those who first gathered with him at Adullam.</p>",
        "hitchcock_meaning": "their testimony; their prey; their ornament",
        "source_ids": {"easton": "adullam", "smith": "adullam", "isbe": "adullam"},
        "key_refs": ["Joshua 12:15", "1 Samuel 22:1", "1 Samuel 22:2", "Micah 1:15"]
    },
    "adullamite": {
        "id": "adullamite",
        "term": "Adullamite",
        "category": "people",
        "intro": "<p>Adullamite designates an inhabitant of the city of Adullam in the Shephelah of Judah. The term appears three times in Genesis 38, each time referring to Hirah, a Canaanite man of Adullam who was a friend of Judah during the period before the family's descent into Egypt. Through this friendship, Judah came into contact with Shua the Canaanite, whose daughter he married, and it was through Hirah that Judah sent the payment of a young goat to the woman he had mistaken for a prostitute — who proved to be his daughter-in-law Tamar.</p><p>Hirah the Adullamite plays a supporting but narratively significant role in the episode of Judah and Tamar in Genesis 38, which interrupts the Joseph narrative and explores the matrilineal continuity of the Judahite line. The term itself is purely a gentile designation indicating membership in the community of Adullam.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "adullamite", "isbe": "adullamite"},
        "key_refs": ["Genesis 38:1", "Genesis 38:12", "Genesis 38:20"]
    },
    "adultery": {
        "id": "adultery",
        "term": "Adultery",
        "category": "concepts",
        "intro": "<p>Adultery in biblical law denotes sexual intercourse between a married woman and any man other than her husband, or between a married man and another man's wife. The seventh commandment (<em>Thou shalt not commit adultery</em>, Exodus 20:14) placed the prohibition at the center of the Decalogue, and Mosaic law prescribed death for both parties when the act was proven before witnesses (Leviticus 20:10; Deuteronomy 22:22). The procedural test for a wife suspected of adultery — the ordeal of bitter water described in Numbers 5:11–31 — is unique in the Pentateuch and reflects the gravity with which the offense was treated as a violation of covenant loyalty within marriage.</p><p>The prophets, especially Jeremiah, Ezekiel, and Hosea, extend the concept to describe Israel's spiritual unfaithfulness to God as adultery against the covenant. In the New Testament, Jesus sharpens the definition inward — the one who looks at a woman with lustful intent has already committed adultery in his heart (Matthew 5:28). The episode of the woman caught in adultery (John 8:1–11) demonstrates both the legal severity of the charge and the mercy and moral seriousness with which Jesus responded to it.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "adultery", "smith": "adultery", "isbe": "adultery"},
        "key_refs": ["Numbers 5:11", "John 8:1", "Jeremiah 3:6", "Matthew 5:28"]
    },
    "adummim": {
        "id": "adummim",
        "term": "Adummim",
        "category": "places",
        "intro": "<p>Adummim (meaning <em>the red ones</em> or <em>bloody things</em>) was a pass or ascent on the road between Jericho and Jerusalem, mentioned in Joshua 15:7 and 18:17 as a boundary marker between the tribal territories of Judah and Benjamin. The name likely refers to the reddish limestone of the area or, according to some ancient authorities, to bloodshed that occurred there. The road through this pass was notoriously dangerous in antiquity, a steep and winding descent through the Judean wilderness favored by bandits.</p><p>The pass is traditionally identified with the modern Tal'at ed-Damm, approximately halfway between Jerusalem and Jericho at an elevation change of over 3,000 feet. Its character as a perilous wilderness road makes it the almost certain setting of Jesus's parable of the Good Samaritan, in which a man traveling from Jerusalem down to Jericho fell among thieves (Luke 10:30) — a scenario entirely credible to any first-century audience familiar with the road through Adummim.</p>",
        "hitchcock_meaning": "earthy; red; bloody things",
        "source_ids": {"easton": "adummim", "smith": "adummim", "isbe": "adummim"},
        "key_refs": ["Joshua 15:7", "Joshua 18:17", "Luke 10:30"]
    },
    "adversary": {
        "id": "adversary",
        "term": "Adversary",
        "category": "concepts",
        "intro": "<p>Adversary renders the Hebrew <em>satan</em> and the Greek <em>antidikos</em>, both meaning an opponent or one who stands against. In its most general Old Testament usage, the term refers to human enemies or opposing forces — political rivals who arose against Solomon (1 Kings 11:14, 23, 25) or legal opponents in a lawsuit (Matthew 5:25; Luke 13:17). The word carries no supernatural connotation in these contexts.</p><p>The term's theological weight derives from its application to the supernatural opponent of both God and humanity. In Job 1–2, Zechariah 3:1–2, and 1 Chronicles 21:1, the adversary appears as a distinct spiritual being who accuses, tests, and opposes. The New Testament identifies this figure with the devil and describes the believer's posture toward him: <em>your adversary the devil, as a roaring lion, walketh about, seeking whom he may devour</em> (1 Peter 5:8). The resistance to the adversary is to be accomplished through faith, sobriety, and submission to God rather than through direct spiritual confrontation conducted in one's own strength.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "adversary", "isbe": "adversary"},
        "key_refs": ["1 Kings 5:4", "1 Kings 11:14", "Matthew 5:25", "1 Peter 5:8"]
    },
    "advocate": {
        "id": "advocate",
        "term": "Advocate",
        "category": "concepts",
        "intro": "<p>Advocate renders the Greek <em>parakletos</em> — literally <em>one called alongside</em> — a term used in John's writings for both the Holy Spirit and Jesus Christ. In John 14:16, Jesus promises to ask the Father to send <em>another Paraclete</em> (implying that Jesus himself is the first), who will be with the disciples forever as the Spirit of truth. The Spirit as Advocate comes to teach, remind, convict, and guide into all truth (John 14:26; 15:26; 16:7–15). The word encompassed in Greek usage the roles of counselor, intercessor, helper, and legal advocate.</p><p>In 1 John 2:1, the term is applied directly to the risen Christ: <em>if anyone sins, we have an advocate with the Father, Jesus Christ the righteous</em>. Here the forensic dimension is primary — Christ as the one who pleads the cause of sinners before the Father on the basis of his atoning sacrifice. The theological distinction between the Spirit's ongoing ministry of advocacy within the believer and Christ's heavenly intercession before the Father frames the New Testament's account of the triune God's work on behalf of those who believe.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "advocate", "smith": "advocate", "isbe": "advocate"},
        "key_refs": ["John 14:16", "John 15:26", "1 John 2:1"]
    },
    "aenon": {
        "id": "aenon",
        "term": "AEnon",
        "category": "places",
        "intro": "<p>AEnon (meaning <em>springs</em> or <em>fountains</em>) was a place near Salim where John the Baptist conducted his later baptismal ministry before his imprisonment (John 3:23). The text notes explicitly that John baptized there <em>because there was much water</em> — a detail indicating the site had sufficient water for the practice of immersive or extensive baptism. The location is distinct from the sites associated with John's earlier ministry near the Jordan River.</p><p>The identification of AEnon is debated. The most favored site among scholars is in the upper Jordan Valley near Scythopolis (Beth-shean), where a cluster of springs and a village named Salim are attested. The passage in John 3 is important for Johannine chronology, placing Jesus's Judean ministry alongside John's final ministry and providing the context for John's famous declaration that he must decrease while Jesus must increase.</p>",
        "hitchcock_meaning": "a cloud; fountain; his eye",
        "source_ids": {"easton": "aenon", "smith": "aenon", "isbe": "aenon"},
        "key_refs": ["John 3:23"]
    },
    "affection": {
        "id": "affection",
        "term": "Affection",
        "category": "concepts",
        "intro": "<p>Affection in Scripture denotes the range of human emotions and inclinations, evaluated morally according to their object and orientation. Paul's reference to <em>vile affections</em> in Romans 1:26 — affections that are degrading or against nature — appears in his diagnosis of the consequences of suppressing the knowledge of God: disordered desire follows upon disordered worship. Colossians 3:5 lists <em>inordinate affection</em> among the works of the earthly nature that are to be mortified, while the same letter instructs believers to set their affections on things above rather than on things on the earth (Colossians 3:2).</p><p>Ezekiel 33:32 uses the related idea when describing the people's treatment of the prophet's words as a pleasant song — they are moved emotionally but not morally. Together these passages reflect the biblical view that affection is not inherently problematic but becomes disordered when directed toward wrong objects or when it substitutes emotional response for moral obedience. Rightly ordered affection — love of God, love of neighbor, love of what is good — is itself a mark of genuine spiritual transformation.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "affection"},
        "key_refs": ["Romans 1:26", "Colossians 3:5", "Colossians 3:2"]
    },
    "affinity": {
        "id": "affinity",
        "term": "Affinity",
        "category": "concepts",
        "intro": "<p>Affinity in the biblical context refers to relationship created through marriage or political alliance rather than blood. The term is used in 2 Chronicles 18:1 to describe the marriage alliance between Jehoshaphat of Judah and the house of Ahab of Israel — Jehoshaphat made affinity with Ahab by the marriage of his son Jehoram to Athaliah, Ahab's daughter. Similarly, Solomon's affinity with Pharaoh through marriage (1 Kings 3:1) is noted as part of his foreign policy, though subsequently criticized in the account of his foreign wives who led him into idolatry.</p><p>The Mosaic law regulated affinity through an extensive list of prohibited degrees of relationship (Leviticus 18:6–18), specifying the classes of relatives by marriage with whom sexual relations were forbidden. These regulations shaped the boundaries of permitted marriage within Israelite society and were treated in Second Temple Judaism and later halakhic tradition as binding definitions of incest even beyond the letter of the text.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "affinity", "smith": "affinity", "isbe": "affinity"},
        "key_refs": ["2 Chronicles 18:1", "1 Kings 3:1", "Leviticus 18:6"]
    },
    "afflictions": {
        "id": "afflictions",
        "term": "Afflictions",
        "category": "concepts",
        "intro": "<p>Afflictions in Scripture are presented as a universal feature of human existence common to all (Job 5:7; 14:1) that are neither accidental nor purposeless within the providential ordering of God. The Psalms acknowledge affliction as the normal backdrop of the righteous person's life — <em>many are the afflictions of the righteous</em> (Psalm 34:19) — while affirming divine deliverance from them all. The book of Job explores most deeply the problem of affliction befalling the blameless, resisting easy theodicy while ultimately grounding trust in the sovereignty and character of God.</p><p>The New Testament develops a theology of affliction as productive suffering. James 1:2–4 frames trials as the means of testing faith and producing endurance, while Paul in 2 Corinthians 1 and Romans 5 describes affliction as the context in which experience of divine comfort deepens and character is formed. The christological grounding is explicit: believers participate in the sufferings of Christ (Philippians 3:10; Colossians 1:24), and present afflictions are relativized against the weight of glory they are producing (2 Corinthians 4:17). Comfort received in affliction becomes the resource for comforting others in theirs.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "afflictions"},
        "key_refs": ["Job 5:7", "Psalms 34:19", "James 1:2", "2 Corinthians 4:17"]
    },
    "agabus": {
        "id": "agabus",
        "term": "Agabus",
        "category": "people",
        "intro": "<p>Agabus was a prophet of the early church, probably one of the wider circle of disciples associated with the Jerusalem community, though Easton suggests he may have been among the seventy sent out by Jesus. He is mentioned twice in Acts. At Antioch, during the early ministry of Barnabas and Saul, Agabus came down from Jerusalem and predicted by the Spirit that a great famine would come over all the world, which the narrator notes was fulfilled in the days of Claudius Caesar (Acts 11:27–28). This prophecy prompted the Antiochene church to send relief to the brethren in Judea — an early instance of Gentile churches supporting the Jerusalem community.</p><p>Agabus appears again in Acts 21:10–11 at Caesarea, where he took Paul's belt, bound his own hands and feet with it, and declared prophetically that the Jews of Jerusalem would bind the man who owned the belt and deliver him to the Gentiles. The symbolic-enacted form of the prophecy reflects the tradition of the Hebrew prophets, and though Paul did not alter his course in response to the warning, the prediction was substantively fulfilled in his arrest and Roman imprisonment.</p>",
        "hitchcock_meaning": "a locust; the father's joy or sorrow",
        "source_ids": {"easton": "agabus", "smith": "agabus", "isbe": "agabus"},
        "key_refs": ["Acts 11:27", "Acts 11:28", "Acts 21:10"]
    },
    "agag": {
        "id": "agag",
        "term": "Agag",
        "category": "people",
        "intro": "<p>Agag (meaning <em>flame</em> or <em>high</em>) was the hereditary title of the kings of Amalek, functioning as a dynastic name in the way that <em>Pharaoh</em> served for Egypt. Balaam's oracle in Numbers 24:7 uses the name prospectively — <em>his king shall be higher than Agag, and his kingdom shall be exalted</em> — as a measure of the greatness Israel would achieve. The Agag most prominent in Scripture is the king of the Amalekites whom Saul defeated but failed to execute following the battle described in 1 Samuel 15.</p><p>Saul's sparing of Agag in direct violation of the divine command to utterly destroy the Amalekites became the occasion for Samuel's confrontation with Saul and the announcement of his rejection as king. The prophet Samuel executed Agag at Gilgal with the declaration: <em>As thy sword hath made women childless, so shall thy mother be childless among women</em> (1 Samuel 15:33). Agag's execution and Saul's disobedience form one of the pivotal moments in the transition of the kingship from Saul to David.</p>",
        "hitchcock_meaning": "roof; upper floor",
        "source_ids": {"easton": "agag", "smith": "agag", "isbe": "agag"},
        "key_refs": ["Numbers 24:7", "1 Samuel 15:8", "1 Samuel 15:33"]
    },
    "agagite": {
        "id": "agagite",
        "term": "Agagite",
        "category": "people",
        "intro": "<p>Agagite is a designation applied to Haman and his father Hammedatha in the book of Esther (3:1, 10; 8:3, 5; 9:24). The term most naturally connects Haman to the Amalekite royal line of Agag, making him a descendant of Israel's ancient enemies. If this identification is correct, the conflict between Haman and Mordecai — a descendant of Kish of the tribe of Benjamin, the same tribal background as King Saul — would represent the continuation of the ancient enmity between Israel and Amalek, now playing out in the Persian court centuries after the time of Samuel and Saul.</p><p>Some scholars prefer to understand Agagite as a geographic or clan term rather than a genealogical connection to the Amalekite king Agag, but the canonical reading within the book of Esther clearly intends a narrative resonance with the earlier failure of Saul to destroy Agag — a failure now met by Mordecai's refusal to bow, and by the eventual destruction of Haman and his sons.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "agagite", "smith": "agagite", "isbe": "agagite"},
        "key_refs": ["Esther 3:1", "Esther 3:10", "Esther 8:3"]
    },
    "agate": {
        "id": "agate",
        "term": "Agate",
        "category": "concepts",
        "intro": "<p>Agate renders the Hebrew <em>shebo</em> in most English translations, identifying it as one of the twelve precious stones set in the breastplate of the high priest (Exodus 28:19; 39:12), where it occupied the third stone of the third row. The precise identification of the Hebrew gemstone terms is uncertain, as ancient and modern lapidary nomenclature differs considerably, and some scholars suggest the underlying stone may have been a different variety entirely. Agate in modern usage refers to a banded, translucent chalcedony occurring in a variety of colors.</p><p>The stone also appears in eschatological contexts. Isaiah 54:12 lists agate (or carbuncle, depending on the translation) among the precious stones with which the walls of the renewed Jerusalem would be built — a passage the New Testament's vision of the heavenly Jerusalem in Revelation 21 develops and transforms. Ezekiel 27:16 mentions agate among the merchandise that Syria traded with Tyre, indicating its commercial value in the ancient Near Eastern economy.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "agate", "smith": "agate", "isbe": "agate"},
        "key_refs": ["Exodus 28:19", "Isaiah 54:12", "Ezekiel 27:16"]
    },
    "age": {
        "id": "age",
        "term": "Age",
        "category": "concepts",
        "intro": "<p>Age in Scripture carries several distinct meanings. In its most straightforward sense it denotes the duration of a person's life: Jacob describes his 130 years as few and evil compared to the lifespans of his fathers (Genesis 47:9, 28), and John 9:21 uses the cognate phrase to note that the healed blind man was of age and could speak for himself. In wisdom literature, old age is treated as a mark of honor — <em>the glory of young men is their strength; and the beauty of old men is the gray head</em> (Proverbs 20:29) — and the instruction to rise before the elderly is embedded in the Holiness Code (Leviticus 19:32).</p><p>The term also carries a cosmological dimension. Paul refers to <em>the mystery hidden from ages and from generations</em> (Colossians 1:26) and to <em>the ages to come</em> in which God will display the exceeding riches of his grace (Ephesians 2:7). The Greek <em>aion</em> (age, world, or eon) underlies these passages, reflecting the apocalyptic framework in which present and future ages are distinguished and the full disclosure of God's purposes awaits the consummation.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "age", "isbe": "age"},
        "key_refs": ["Genesis 47:28", "Ephesians 2:7", "Colossians 1:26"]
    },
    "agee": {
        "id": "agee",
        "term": "Agee",
        "category": "people",
        "intro": "<p>Agee (meaning <em>a valley</em> or <em>deepness</em>) was the father of Shammah the Hararite, one of David's three chief mighty men. Shammah is celebrated in 2 Samuel 23:11–12 for his single-handed defense of a field of lentils against a Philistine raiding party after the men of Israel fled — an act of individual valor that the text attributes explicitly to the Lord's deliverance. Agee himself is named only in connection with his son, functioning in the genealogical formula that identifies warriors by patronymic.</p><p>The father's name Agee appears once in Scripture, in 2 Samuel 23:11, as part of the roster of David's mighty men. Nothing further is recorded about Agee beyond his role as Shammah's father. His Hararite designation indicates an origin in the hill country, possibly the region of the southern highlands of Judah.</p>",
        "hitchcock_meaning": "a valley; deepness",
        "source_ids": {"easton": "agee", "isbe": "agee"},
        "key_refs": ["2 Samuel 23:11"]
    },
    "agony": {
        "id": "agony",
        "term": "Agony",
        "category": "concepts",
        "intro": "<p>Agony renders the Greek <em>agonia</em>, derived from <em>agon</em> — the arena of athletic contest — denoting the intense straining effort of a competitor in a race or wrestling match. In biblical usage the term encompasses both physical anguish and the severe mental and spiritual distress of extreme suffering. Luke 22:44 uses <em>agonia</em> to describe Jesus's prayer in Gethsemane, where his anguish was so acute that his sweat became like drops of blood falling to the ground — one of the most physiologically arresting details in the passion narrative.</p><p>Paul employs the athletic sense of the word group in his accounts of his own ministry — <em>striving according to his working, which worketh in me mightily</em> (Colossians 1:29) — and in his exhortation to athletic discipline in 1 Corinthians 9:25. The word thus bridges two distinct registers in the New Testament: the unparalleled suffering of Christ in Gethsemane, and the strenuous but purposeful effort of Christian ministry and discipleship modeled on the athlete who competes for an incorruptible crown.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "agony", "isbe": "agony"},
        "key_refs": ["Luke 22:44", "1 Corinthians 9:25", "Colossians 1:29"]
    },
    "agriculture": {
        "id": "agriculture",
        "term": "Agriculture",
        "category": "concepts",
        "intro": "<p>Agriculture was the foundational occupation of Israel and is woven throughout the biblical narrative from creation to the prophets. The cultivation of the ground is presented as humanity's original vocation — Adam was placed in the garden to tend and keep it (Genesis 2:15), and after the fall the same ground became the medium of toilsome labor in conditions of curse and futility (Genesis 3:17–19). Cain, the farmer, and Abel, the shepherd, represent the two primary forms of subsistence in early biblical society. The promise of rain <em>for the first and latter rain</em> and the orderly sequence of harvest seasons (Deuteronomy 11:14; Jeremiah 5:24) are presented as covenant blessings contingent on Israel's faithfulness.</p><p>Israelite agriculture was adapted to the Mediterranean climate of Canaan, with its dry summers and winter rains. The main crops were grain (wheat and barley), grapes, and olives — the combination that defines the promised land's abundance. The agricultural calendar structured Israel's religious year: the festivals of Unleavened Bread, Weeks (Pentecost), and Tabernacles were harvest celebrations at their core. Sabbatical and Jubilee legislation regulated the land's use and provided periodic rest and redistribution.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "agriculture", "smith": "agriculture", "isbe": "agriculture"},
        "key_refs": ["Genesis 2:15", "Genesis 4:2", "Deuteronomy 11:14", "Jeremiah 5:24"]
    },
    "agrippa-i": {
        "id": "agrippa-i",
        "term": "Agrippa I",
        "category": "people",
        "intro": "<p>Agrippa I (also known as Herod Agrippa I) was the grandson of Herod the Great, the son of Aristobulus and Bernice, and the last ruler to govern a territory comparable in extent to that of his grandfather. Raised in Rome and educated alongside members of the imperial family, he cultivated friendships with Caligula and Claudius that proved politically decisive. Through a series of grants he eventually accumulated rule over virtually all of Palestine, the first such unified governance since Herod the Great.</p><p>In Acts 12, Agrippa is the king who executed James the brother of John and imprisoned Peter, seeking popular favor with the Jerusalem Jewish leadership. His sudden death — <em>smitten of an angel</em> and eaten by worms because he accepted divine honors at Caesarea (Acts 12:20–23) — is confirmed in a parallel account by Josephus, who records his death at the games in Caesarea in A.D. 44. The juxtaposition of Peter's miraculous escape and Agrippa's death frames the passage as a demonstration of divine judgment on the persecutor and divine protection of the persecuted church.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "agrippa-i"},
        "key_refs": ["Acts 12:1", "Acts 12:20", "Acts 12:23"]
    },
    "agrippa-ii": {
        "id": "agrippa-ii",
        "term": "Agrippa II",
        "category": "people",
        "intro": "<p>Agrippa II (Marcus Julius Agrippa, also known as Herod Agrippa II) was the son of Agrippa I and was born in Rome in A.D. 27. He was the brother of Bernice and Drusilla — the latter having married the procurator Felix. Emperor Claudius did not give him his father's full kingdom on account of his youth, but he was given rule over territories in Syria and eventually the tetrarchy formerly held by Philip and Lysanias. The Romans also gave him authority over the temple treasury and the appointment of the high priests.</p><p>Agrippa II is best known in the New Testament for his hearing of Paul's case at Caesarea (Acts 25:13–26:32), where Paul delivered one of his most developed defenses of his faith and mission. Paul's appeal — <em>King Agrippa, believest thou the prophets?</em> — elicited Agrippa's famous ambiguous reply. Agrippa's judgment, shared with Festus, was that Paul had done nothing deserving death or imprisonment and might have been freed had he not appealed to Caesar. Agrippa sided with Rome during the Jewish revolt of A.D. 66–70.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "agrippa-ii"},
        "key_refs": ["Acts 25:13", "Acts 26:2", "Acts 26:28"]
    },
    "ague": {
        "id": "ague",
        "term": "Ague",
        "category": "concepts",
        "intro": "<p>Ague is the traditional English rendering of the Hebrew <em>qaddachat</em> in Leviticus 26:16 and Deuteronomy 28:22, denoting a burning fever, likely including the intermittent fevers characteristic of malaria. The Revised Version translates the term simply as <em>fever</em>. In context, ague appears among the catalog of covenant curses that would afflict Israel for disobedience — <em>I will even appoint over you terror, consumption, and the burning ague, that shall consume the eyes</em> (Leviticus 26:16).</p><p>The identification with malaria is suggested by the prevalence of the disease in the Jordan Valley and coastal lowlands of Canaan, where standing water created ideal breeding conditions. The term belongs to a broader biblical vocabulary of illness and disease that functions within the covenant framework: disease is listed both as curse for disobedience and as something from which God promises healing upon repentance and return. The New Testament references to fevers in the healing accounts of Jesus (Matthew 8:14–15; John 4:52; Acts 28:8) reflect the same physical reality in a different theological register.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ague", "isbe": "ague"},
        "key_refs": ["Leviticus 26:16", "Deuteronomy 28:22"]
    },
    "agur": {
        "id": "agur",
        "term": "Agur",
        "category": "people",
        "intro": "<p>Agur son of Jakeh is identified as the author of the collection of sayings in Proverbs 30. He is described as <em>the man who spake unto Ithiel, even unto Ithiel and Ucal</em> (Proverbs 30:1), though the identity of these addressees and the exact meaning of the superscription have been disputed. Agur presents himself with remarkable humility — <em>Surely I am more brutish than any man, and have not the understanding of a man. I neither learned wisdom, nor have the knowledge of the holy</em> (Proverbs 30:2–3) — before launching into a series of numerical proverbs that observe patterns in the natural world with precise, almost scientific attention.</p><p>Agur is identified neither with Solomon nor with any known Israelite figure, and some scholars have suggested he may have been a sage from a non-Israelite tradition incorporated into the canon of wisdom. His prayer in Proverbs 30:7–9 — asking for neither poverty nor riches, only the daily bread that preserves from both denial and excess — is among the most theologically balanced petitions in the wisdom literature.</p>",
        "hitchcock_meaning": "stranger; gathered together",
        "source_ids": {"easton": "agur", "smith": "agur", "isbe": "agur"},
        "key_refs": ["Proverbs 30:1", "Proverbs 30:7"]
    },
    "ah": {
        "id": "ah",
        "term": "Ah!",
        "category": "concepts",
        "intro": "<p>Ah! is an exclamation in the biblical text expressing grief, distress, or lamentation. In Psalms 35:25, the cry <em>Aha! So would we have it</em> is the mocking shout of enemies over the afflicted psalmist, while the distress-cry <em>Ah!</em> itself voices the anguish of the speaker or the grief of God himself. Isaiah opens with it — <em>Ah sinful nation, a people laden with iniquity</em> (Isaiah 1:4) — as a prophetic cry of mourning over Israel's condition. Jeremiah uses it at his prophetic call: <em>Ah, Lord GOD! behold, I cannot speak: for I am a child</em> (Jeremiah 1:6).</p><p>The exclamation also appears in contexts of divine lamentation and threat. In Isaiah 1:24, God himself employs it: <em>Ah, I will ease me of mine adversaries</em> — a phrase denoting the divine resolve to act in judgment. In Ezekiel and Jeremiah, similar interjections mark moments of prophetic anguish or divine pathos. The particle thus functions as a marker of deep emotional engagement — mourning, alarm, and lamentation — throughout the prophetic literature.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ah", "isbe": "ah"},
        "key_refs": ["Psalms 35:25", "Isaiah 1:4", "Jeremiah 1:6"]
    },
    "aha": {
        "id": "aha",
        "term": "Aha!",
        "category": "concepts",
        "intro": "<p>Aha! is an exclamation occurring in Scripture as an expression of triumphant mockery or malicious satisfaction at another's misfortune. Psalm 35:21 records the taunting cry of the psalmist's enemies — <em>Aha, aha, our eye hath seen it</em> — at his distress, and Psalm 40:15 and 70:3 use the same cry in pleas to God to shame those who rejoice at the speaker's trouble: <em>Let them be desolate for a reward of their shame that say unto me, Aha, aha!</em></p><p>In Isaiah 44:16, the same interjection appears in a quite different register — the ironist's description of the idol-maker warming himself at the fire and exclaiming <em>Aha, I am warm, I have seen the fire</em> — before carving the remaining wood into a god to prostrate himself before. Here the exclamation is turned against its speaker, illustrating the absurdity of idol worship through the mundane self-satisfaction of the craftsman. In Job 39:25, the war horse's cry at the sound of the trumpet echoes the same vivid interjection of excited response.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "aha"},
        "key_refs": ["Psalms 35:21", "Psalms 40:15", "Isaiah 44:16"]
    },
    "ahab": {
        "id": "ahab",
        "term": "Ahab",
        "category": "people",
        "intro": "<p>Ahab (meaning <em>father's brother</em> or <em>uncle</em>) was the son of Omri and the seventh king of the northern kingdom of Israel, reigning approximately 874–853 B.C. His marriage to Jezebel, daughter of the king of Sidon, proved catastrophic for Israel's religious life: Jezebel introduced the cult of Baal and Asherah on a state scale, persecuted the prophets of the Lord, and exercised a dominating influence over the king. The historian of Kings summarizes Ahab's reign as more provocative to the God of Israel than all the kings before him.</p><p>Ahab's reign is dominated in the biblical narrative by his conflict with the prophet Elijah, who announced a three-year drought, challenged the prophets of Baal on Carmel, and pronounced doom on Ahab's house for the judicial murder of Naboth and the seizure of his vineyard. Ahab died at Ramoth-gilead, killed by a random arrow in battle against Aram — the fulfillment of Elijah's prophecy that where dogs had licked Naboth's blood they would lick Ahab's. The prophet Micah and later the writer of Chronicles cite Ahab's apostasy as a paradigm of royal wickedness. Yet Ahab's partial repentance after Elijah's pronouncement (1 Kings 21:27–29) moved God to delay the full punishment to his son's generation.</p>",
        "hitchcock_meaning": "uncle, or father's brother",
        "source_ids": {"easton": "ahab", "smith": "ahab", "isbe": "ahab"},
        "key_refs": ["1 Kings 16:30", "1 Kings 21:19", "1 Kings 22:37"]
    },
    "ahasuerus": {
        "id": "ahasuerus",
        "term": "Ahasuerus",
        "category": "people",
        "intro": "<p>Ahasuerus is the Hebrew form of a Persian royal title that designates three different kings in the Old Testament. The first is the father of Darius the Mede (Daniel 9:1), a figure of the Persian imperial succession. The second, identified by most scholars with Xerxes I (r. 486–465 B.C.), is the Persian king of the book of Esther — a monarch of vast power whose empire stretched from India to Ethiopia and who is depicted as capricious, susceptible to flattery, and ultimately moved by the courage of Esther to reverse Haman's edict against the Jews. A third brief reference appears in Ezra 4:6, where an Ahasuerus receives a complaint against the Jews of Jerusalem.</p><p>The Esther narrative presents Ahasuerus as a complex figure: the great imperial power under whose governance the Jewish diaspora lived, whose favor could mean salvation and whose anger meant death, and who was eventually moved to protect his Jewish queen and her people through Mordecai's disclosures and Esther's courageous advocacy. The book of Esther's theology of providential preservation operates through precisely this kind of ambiguous royal power working within — and despite — its own political calculations.</p>",
        "hitchcock_meaning": "prince; head; chief",
        "source_ids": {"easton": "ahasuerus", "smith": "ahasuerus"},
        "key_refs": ["Daniel 9:1", "Ezra 4:6", "Esther 1:1"]
    },
    "ahava": {
        "id": "ahava",
        "term": "Ahava",
        "category": "places",
        "intro": "<p>Ahava (meaning <em>essence</em> or <em>being</em>) was a river or canal in Babylonia beside which Ezra assembled the returning Jewish exiles before their journey to Jerusalem. Ezra 8:15 records that he gathered the people there for three days, and it was at Ahava that he discovered there were no Levites among the assembled company — a lack he remedied by sending for representatives of that priestly tribe from Casiphia. The assembly at the river Ahava also became the occasion for a fast and a prayer for divine protection during the journey, since Ezra had assured the king that God's hand was on all who sought him.</p><p>The exact location of the river Ahava is unknown, but it was evidently near a settlement of the same name and functioned as a staging point for the caravan that would eventually carry the gold, silver, and sacred vessels from Babylon to the restored temple in Jerusalem. The episode is one of the most detailed accounts in Ezra of the logistics and spirituality of the return from exile.</p>",
        "hitchcock_meaning": "essence; being; generation",
        "source_ids": {"easton": "ahava", "smith": "ahava", "isbe": "ahava"},
        "key_refs": ["Ezra 8:15", "Ezra 8:21"]
    },
    "ahaz": {
        "id": "ahaz",
        "term": "Ahaz",
        "category": "people",
        "intro": "<p>Ahaz (meaning <em>possessor</em> or <em>one who grasps</em>) is the name of two men in the Old Testament. The more significant was the son and successor of Jotham and the twelfth king of Judah, reigning c. 735–715 B.C. His reign was marked by profound religious apostasy: he sacrificed his son in the fire according to the abominations of the nations (2 Kings 16:3), closed the temple, and introduced Assyrian altar forms into Jerusalem's worship. When threatened by the Syro-Ephraimite coalition of Rezin and Pekah, Ahaz appealed to Tiglath-pileser III of Assyria for help — stripping the temple treasury as payment — rather than trusting the word of God delivered through Isaiah.</p><p>It was to Ahaz that Isaiah addressed the Immanuel prophecy (Isaiah 7:14): <em>Behold, a virgin shall conceive and bear a son, and shall call his name Immanuel</em>. Ahaz refused to ask for a sign of God's faithfulness and thus stands in the narrative as the faithless king against whom the promise of the divine sign is given. The New Testament cites the Immanuel text in Matthew 1:23 as fulfilled in the birth of Jesus. A lesser Ahaz was a descendant of Jonathan in the genealogy of Benjamin (1 Chronicles 8:35–36).</p>",
        "hitchcock_meaning": "one that takes or possesses",
        "source_ids": {"easton": "ahaz", "smith": "ahaz", "isbe": "ahaz"},
        "key_refs": ["2 Kings 16:3", "2 Kings 16:7", "Isaiah 7:1", "Isaiah 7:14"]
    },
    "ahaziah": {
        "id": "ahaziah",
        "term": "Ahaziah",
        "category": "people",
        "intro": "<p>Ahaziah (meaning <em>held by Jehovah</em> or <em>seizure of the Lord</em>) is the name of two kings in the Old Testament. The first was the son and successor of Ahab and Jezebel, the ninth king of Israel, reigning c. 853–852 B.C. He walked in the ways of his parents and the sins of Jeroboam, and he died after a fall through a lattice in his upper chamber in Samaria — having sent to inquire of Baal-zebub the god of Ekron rather than of the God of Israel, for which the prophet Elijah pronounced his death (2 Kings 1). He died without a son and was succeeded by his brother Jehoram.</p><p>The second Ahaziah was the son of Jehoram and Athaliah, the sixth king of Judah, reigning c. 841 B.C. — a single year. He was the grandson of Ahab through his mother Athaliah, and he walked in the counsel of Ahab's house. He was killed by Jehu of Israel during Jehu's divinely commissioned purge of the Omride dynasty, dying at Megiddo after being wounded in his chariot at Jezreel. His death set the stage for Athaliah's usurpation of the Judahite throne.</p>",
        "hitchcock_meaning": "seizure; vision of the Lord",
        "source_ids": {"easton": "ahaziah", "smith": "ahaziah", "isbe": "ahaziah"},
        "key_refs": ["1 Kings 22:51", "2 Kings 1:2", "2 Kings 8:29", "2 Kings 9:27"]
    },
    "ahiam": {
        "id": "ahiam",
        "term": "Ahiam",
        "category": "people",
        "intro": "<p>Ahiam (meaning <em>mother's brother</em> or <em>a brother of the mother</em>) was a son of Sharar (or Sacar in 1 Chronicles 11:35) the Hararite, and one of David's thirty heroes — the second tier of David's elite fighting corps. He is listed in 2 Samuel 23:33 and the parallel list in 1 Chronicles 11:35 among the military champions whose individual acts of valor are described or whose names are recorded in connection with David's campaigns against the Philistines.</p><p>Ahiam receives no individual narrative in Scripture beyond his inclusion in the roster of David's thirty. The Hararite designation — shared by other of David's warriors — likely indicates an origin in the mountainous regions of Judah or Benjamin. His inclusion among the thirty places him in the inner circle of the loyalty network that sustained David's military capacity.</p>",
        "hitchcock_meaning": "mother's brother; brother of a nation",
        "source_ids": {"easton": "ahiam", "smith": "ahiam", "isbe": "ahiam"},
        "key_refs": ["2 Samuel 23:33", "1 Chronicles 11:35"]
    },
    "ahiezer": {
        "id": "ahiezer",
        "term": "Ahiezer",
        "category": "people",
        "intro": "<p>Ahiezer (meaning <em>brother of help</em> or <em>helpful</em>) is the name of two men in the Old Testament. The first and more prominent was the son of Ammishaddai and the appointed chief of the tribe of Dan during Israel's wilderness period. He is named in the census lists of Numbers 1:12 and 2:25, commanded the rear division of the camp (Numbers 10:25), and offered the dedication offering of his tribe at the consecration of the tabernacle. The second Ahiezer was a Benjaminite archer who joined David at Ziklag while he was still a fugitive from Saul (1 Chronicles 12:3), and who was a kinsman of Saul yet chose loyalty to David.</p><p>The two figures represent distinct periods of Israelite history — the wilderness era of the Exodus and the pre-monarchic transition under David — connected only by name. The Danite Ahiezer's military role in commanding the rear guard reflects the careful organization of the wilderness march described in Numbers.</p>",
        "hitchcock_meaning": "brother of assistance",
        "source_ids": {"easton": "ahiezer", "smith": "ahiezer", "isbe": "ahiezer"},
        "key_refs": ["Numbers 1:12", "Numbers 2:25", "1 Chronicles 12:3"]
    },
    "ahihud": {
        "id": "ahihud",
        "term": "Ahihud",
        "category": "people",
        "intro": "<p>Ahihud (meaning <em>brother of union</em> or <em>brother of vanity</em>) is the name of two men in the Old Testament. The first was a son of Bela, the son of Benjamin, listed in 1 Chronicles 8:7 in the tribal genealogy of Benjamin. The second was the son of Shelomi and the appointed representative of the tribe of Asher assigned to assist in dividing the land of Canaan among the tribes; he is named in Numbers 34:27 as one of the ten leaders designated by God for this purpose.</p><p>Neither figure plays an individual narrative role in Scripture beyond these genealogical and administrative references. The second Ahihud's appointment as a representative in the land division was a position of considerable practical significance, given that the equitable distribution of the tribal inheritances was a foundational act of the settlement under Joshua.</p>",
        "hitchcock_meaning": "brother of vanity, or of darkness",
        "source_ids": {"easton": "ahihud", "smith": "ahihud", "isbe": "ahihud"},
        "key_refs": ["1 Chronicles 8:7", "Numbers 34:27"]
    },
    "ahijah": {
        "id": "ahijah",
        "term": "Ahijah",
        "category": "people",
        "intro": "<p>Ahijah (meaning <em>brother of Jehovah</em> or <em>friend of the Lord</em>) is the name of several men in the Old Testament, the most significant being Ahijah the Shilonite, the prophet who played a decisive role in the division of the kingdom. He encountered Jeroboam on the road outside Jerusalem, tore his own new garment into twelve pieces, and gave ten to Jeroboam as a sign that God would tear the kingdom from Solomon and give ten tribes to him on account of Solomon's idolatry (1 Kings 11:29–39). The prophecy also promised Jeroboam a dynasty like David's if he would obey God.</p><p>Later, when Jeroboam's son fell ill, the king sent his wife in disguise to Ahijah — by then old and blind — to inquire about the child's fate. Ahijah pronounced judgment on Jeroboam's house for the sin he had caused Israel to commit and foretold the child's death (1 Kings 14). Other men named Ahijah include the son of Ahitub the priest (1 Samuel 14:3, 18), one of Solomon's secretaries (1 Kings 4:3), and several figures in the Davidic court genealogies.</p>",
        "hitchcock_meaning": "same with Ahiah; brother of the Lord",
        "source_ids": {"easton": "ahijah", "smith": "ahijah", "isbe": "ahijah"},
        "key_refs": ["1 Kings 11:29", "1 Kings 14:2", "1 Samuel 14:3"]
    },
    "ahikam": {
        "id": "ahikam",
        "term": "Ahikam",
        "category": "people",
        "intro": "<p>Ahikam (meaning <em>brother of support</em> or <em>a brother who raises up</em>) was the son of Shaphan the royal secretary and one of the five officials sent by King Josiah to consult the prophetess Huldah about the book of the law discovered in the temple (2 Kings 22:12; 2 Chronicles 34:20). He was thus a participant in the religious renewal of Josiah's reign. After the fall of Jerusalem, when Nebuchadnezzar appointed Gedaliah as governor over those remaining in Judah, Gedaliah was revealed to be Ahikam's son — placing Ahikam's family at the center of post-destruction Judahite governance.</p><p>Ahikam's most notable individual act was his defense of the prophet Jeremiah after the latter's temple sermon, when the priests and prophets demanded Jeremiah's death (Jeremiah 26:24). <em>Nevertheless the hand of Ahikam the son of Shaphan was with Jeremiah, that they should not give him into the hand of the people to put him to death.</em> This protection was significant enough to be specifically noted by the narrator, and it likely saved Jeremiah's life at a critical juncture in his ministry.</p>",
        "hitchcock_meaning": "a brother who raises up or avenges",
        "source_ids": {"easton": "ahikam", "smith": "ahikam", "isbe": "ahikam"},
        "key_refs": ["2 Kings 22:12", "Jeremiah 26:24", "Jeremiah 40:5"]
    },
    "ahimaaz": {
        "id": "ahimaaz",
        "term": "Ahimaaz",
        "category": "people",
        "intro": "<p>Ahimaaz (meaning <em>brother of anger</em> or <em>brother of the council</em>) is the name of three men in the Old Testament. The first was the father of Ahinoam, wife of King Saul (1 Samuel 14:50). The second and most prominent was the son of Zadok the priest, who served as a courier during Absalom's rebellion and raced Cushi to bring David news of the battle's outcome (2 Samuel 18:19–33). Ahimaaz outran Cushi and arrived first, but withheld the news of Absalom's death, leaving the full report to Cushi. The third Ahimaaz was one of Solomon's twelve district commissioners, who governed the territory of Naphtali and married Solomon's daughter Basemath.</p><p>The courier scene in 2 Samuel 18 is among the most psychologically vivid in the historical books: the watchman on Jerusalem's wall identifies Ahimaaz by his distinctive running style before he arrives, and David's anxious questioning about Absalom's fate is met first with evasion and then with devastating honesty. Ahimaaz's hesitation to deliver the full report reveals both his loyalty to David and his reluctance to be the bearer of news about the king's son.</p>",
        "hitchcock_meaning": "a brother of the council",
        "source_ids": {"easton": "ahimaaz", "smith": "ahimaaz", "isbe": "ahimaaz"},
        "key_refs": ["1 Samuel 14:50", "2 Samuel 15:27", "2 Samuel 18:19", "1 Kings 4:15"]
    },
    "ahiman": {
        "id": "ahiman",
        "term": "Ahiman",
        "category": "people",
        "intro": "<p>Ahiman (meaning <em>brother of a gift</em> or <em>brother of the right hand</em>) is the name of two men in the Old Testament. The first was one of three giant Anakim brothers — Ahiman, Sheshai, and Talmai — who inhabited Hebron and whose terrifying appearance contributed to the negative report of the ten spies sent by Moses from Kadesh-barnea (Numbers 13:22, 28). Caleb drove them out of Hebron when the land was divided (Joshua 15:14), and the tribe of Judah subsequently defeated and killed them (Judges 1:10).</p><p>The second Ahiman was a Levite gatekeeper listed in 1 Chronicles 9:17 among the first inhabitants of Jerusalem after the return from Babylonian exile. The two figures are separated by many centuries and connected only by name, the first belonging to the pre-conquest era and the second to the post-exilic restoration.</p>",
        "hitchcock_meaning": "brother of the right hand",
        "source_ids": {"easton": "ahiman", "smith": "ahiman", "isbe": "ahiman"},
        "key_refs": ["Numbers 13:22", "Joshua 15:14", "Judges 1:10"]
    },
    "ahimelech": {
        "id": "ahimelech",
        "term": "Ahimelech",
        "category": "people",
        "intro": "<p>Ahimelech (meaning <em>brother of the king</em> or <em>my brother is king</em>) was the son of Ahitub and the high priest at Nob, a city of priests near Jerusalem. When David fled from Saul, Ahimelech gave him the consecrated showbread to eat and provided him with the sword of Goliath, which was kept at the sanctuary. This act of hospitality was reported to Saul by Doeg the Edomite, and Saul summoned Ahimelech and the entire priestly community of Nob before him. When Ahimelech defended his action as taken in innocent good faith, Saul ordered the massacre of the priests — eighty-five men in all — carried out by Doeg when Saul's own guards refused the command. Ahimelech's son Abiathar alone escaped.</p><p>The episode marks a moral low point of Saul's reign and explains Abiathar's loyalty to David, with whom he fled and served as priest throughout David's fugitive years and early reign. Jesus cites Ahimelech's gift of the showbread in defense of his disciples' plucking grain on the Sabbath (Matthew 12:3–4), appealing to the principle that human need may take precedence over ceremonial restriction.</p>",
        "hitchcock_meaning": "my brother is a king; my king's brother",
        "source_ids": {"easton": "ahimelech", "smith": "ahimelech", "isbe": "ahimelech"},
        "key_refs": ["1 Samuel 21:1", "1 Samuel 22:9", "1 Samuel 22:18"]
    },
    "ahinadab": {
        "id": "ahinadab",
        "term": "Ahinadab",
        "category": "people",
        "intro": "<p>Ahinadab (meaning <em>a willing brother</em> or <em>brother of liberality</em>) was the son of Iddo and one of the twelve officers whom Solomon appointed over the districts of Israel to supply provisions for the royal household. Each officer was responsible for one month of the year. Ahinadab's district was Mahanaim, the Transjordanian region that had served as Ish-bosheth's capital after Saul's death and through which Jacob had passed on his return from Paddan-aram (1 Kings 4:14).</p><p>Like the other district officers listed in 1 Kings 4, Ahinadab appears only in Solomon's administrative roster. His appointment to the Transjordanian district of Mahanaim reflects the extension of Solomon's administrative reach across the Jordan to encompass territory that had been contested in the transition from Saul to David. The system of monthly provisioning was designed to distribute the burden of royal supply equitably across the kingdom.</p>",
        "hitchcock_meaning": "a willing brother; brother of liberality",
        "source_ids": {"easton": "ahinadab", "smith": "ahinadab", "isbe": "ahinadab"},
        "key_refs": ["1 Kings 4:14"]
    },
    "ahinoam": {
        "id": "ahinoam",
        "term": "Ahinoam",
        "category": "people",
        "intro": "<p>Ahinoam (meaning <em>beauty of the brother</em> or <em>brother of pleasantness</em>) is the name of two women in the Old Testament. The first was the daughter of Ahimaaz and the wife of King Saul (1 Samuel 14:50), though she receives no further narrative treatment beyond this identification. The second Ahinoam was a woman of Jezreel who became one of David's wives during his fugitive years, along with Abigail the widow of Nabal (1 Samuel 25:43; 27:3).</p><p>Both women accompanied David to Ziklag, where they were taken captive during the Amalekite raid, and both were recovered when David pursued the raiders and defeated them (1 Samuel 30:5, 18). Ahinoam of Jezreel bore David's firstborn son, Amnon, at Hebron (2 Samuel 3:2), and thus her name appears in the list of children born to David during his Hebron reign. The Jezreelite origin of the second Ahinoam may reflect David's early connections with the valley of Jezreel during his time operating in the Carmel region.</p>",
        "hitchcock_meaning": "beauty of the brother; brother of pleasantness",
        "source_ids": {"easton": "ahinoam", "smith": "ahinoam", "isbe": "ahinoam"},
        "key_refs": ["1 Samuel 14:50", "1 Samuel 25:43", "2 Samuel 3:2"]
    },
    "ahio": {
        "id": "ahio",
        "term": "Ahio",
        "category": "people",
        "intro": "<p>Ahio (meaning <em>brotherly</em> or <em>his brethren</em>) is the name of three men in the Old Testament. The first was a son of Beriah of the tribe of Benjamin (1 Chronicles 8:14). The second was a son of Jeiel and Maacah, listed in the Gibeonite genealogy of Benjamin (1 Chronicles 8:31; 9:37). The third and most notable Ahio was the son of Abinadab, in whose house at Gibeah the ark of the Lord had rested for twenty years. When David undertook to bring the ark to Jerusalem, Ahio and his brother Uzzah drove the new cart carrying the ark, with Ahio walking in front of it (2 Samuel 6:3–4; 1 Chronicles 13:7).</p><p>The episode ended in tragedy when Uzzah reached out to steady the ark and was struck dead — an event that frightened David and caused him to leave the ark at the house of Obed-edom for three months before the successful second attempt to bring it to Jerusalem. Ahio's role in the narrative is thus primarily as a witness to one of the most sobering episodes in the ark's journey.</p>",
        "hitchcock_meaning": "his brother; his brethren",
        "source_ids": {"easton": "ahio", "smith": "ahio", "isbe": "ahio"},
        "key_refs": ["2 Samuel 6:3", "2 Samuel 6:4", "1 Chronicles 13:7"]
    },
    "ahira": {
        "id": "ahira",
        "term": "Ahira",
        "category": "people",
        "intro": "<p>Ahira (meaning <em>brother of iniquity</em> or <em>my brother is a friend</em>) was the son of Enan and the appointed chief of the tribe of Naphtali during Israel's wilderness period. He is first named in Numbers 1:15 as Naphtali's representative in the census of fighting men, where his tribe numbered 53,400. In Numbers 2:29, his division was assigned the position on the north side of the tabernacle and marched as part of the rear guard under the standard of Dan. He also offered the twelfth and final dedication offering at the consecration of the tabernacle, his offering listed in detail in Numbers 7:78–83.</p><p>As the last tribe in the marching order and the last to offer at the tabernacle dedication, Naphtali under Ahira closed out both the military organization of the wilderness camp and the twelve-day dedication ceremony. Ahira is known entirely through these administrative and ceremonial records and receives no individual narrative treatment.</p>",
        "hitchcock_meaning": "brother of iniquity; brother of a shepherd",
        "source_ids": {"easton": "ahira", "smith": "ahira", "isbe": "ahira"},
        "key_refs": ["Numbers 1:15", "Numbers 2:29"]
    },
    "ahishar": {
        "id": "ahishar",
        "term": "Ahishar",
        "category": "people",
        "intro": "<p>Ahishar (meaning <em>brother of song</em> or <em>brother of a prince</em>) held the position of officer over the household (<em>asher al-habayit</em>) in Solomon's court, a role equivalent to a chief steward or palace administrator — one of the most senior positions in the royal government. He is named in 1 Kings 4:6 in the list of Solomon's principal officials. The palace administrator in the ancient Near East managed the king's domestic affairs, personnel, and logistical support, functioning in some respects as a prime minister for internal affairs.</p><p>Ahishar appears only in this administrative roster and is otherwise unknown in the biblical narrative. His position alongside Adoniram (over the levy) and Azariah (son of Zadok, the priest) reflects the complex bureaucracy that Solomon developed to manage the demands of his ambitious building programs and court.</p>",
        "hitchcock_meaning": "brother of a prince; brother of a song",
        "source_ids": {"easton": "ahishar", "smith": "ahishar", "isbe": "ahishar"},
        "key_refs": ["1 Kings 4:6"]
    },
    "ahithophel": {
        "id": "ahithophel",
        "term": "Ahithophel",
        "category": "people",
        "intro": "<p>Ahithophel (meaning <em>brother of folly</em> or <em>brother of impiety</em>) was David's chief counselor, renowned throughout Israel for advice so reliable that it was <em>as if a man had inquired at the oracle of God</em> (2 Samuel 16:23). His defection to Absalom's rebellion was one of the most painful betrayals David experienced — reflected in the lament psalms that speak of a trusted friend lifting the heel against him (Psalm 41:9; 55:12–14). After joining Absalom in Jerusalem, Ahithophel gave two crucial pieces of counsel: that Absalom should publicly take his father's concubines (fulfilled the prophecy of Nathan in 2 Samuel 12:11–12), and that he himself should immediately lead a night pursuit with 12,000 men to catch David before he could regroup.</p><p>The second counsel was deliberately countered by David's agent Hushai, whose alternative advice Absalom followed instead. When Ahithophel saw that his counsel was not taken, he rode home, set his house in order, and hanged himself — the only suicide in the historical books apart from Saul's and Samson's. His death before the final battle meant he did not witness the defeat of the rebellion his defection had enabled. The parallel between Ahithophel and Judas — both trusted insiders whose betrayals led to their suicides — was noted by patristic commentators.</p>",
        "hitchcock_meaning": "brother of ruin or folly",
        "source_ids": {"easton": "ahithophel", "smith": "ahithophel", "isbe": "ahithophel"},
        "key_refs": ["2 Samuel 15:12", "2 Samuel 15:31", "2 Samuel 17:1", "Psalms 41:9"]
    },
    "ahitub": {
        "id": "ahitub",
        "term": "Ahitub",
        "category": "people",
        "intro": "<p>Ahitub (meaning <em>brother of goodness</em> or <em>good</em>) is the name of several priestly figures in the Old Testament, all belonging to the Aaronic lineage. The first and most prominent was the son of Phinehas and grandson of Eli. When Eli and his sons died and the ark was captured by the Philistines on the same day, the news killed Phinehas's pregnant wife, who named her son Ichabod (<em>the glory has departed</em>); Ahitub was evidently born earlier. He became the father of Ahijah and Ahimelech, both of whom served as high priests in the Saulide period.</p><p>A second Ahitub was the son of Amariah and the father of Zadok, the high priest who served alongside Abiathar during David's reign and who anointed Solomon. A third Ahitub appears in the Chronicler's postexilic priestly genealogy (1 Chronicles 6:11–12). The name recurs across multiple generations of the priestly families, making precise identification of individual bearers difficult in some passages. Together the Ahitubs represent the continuity of the Aaronic priesthood across the crisis of the Philistine wars, the consolidation of the monarchy, and the restoration after exile.</p>",
        "hitchcock_meaning": "brother of goodness",
        "source_ids": {"easton": "ahitub", "smith": "ahitub", "isbe": "ahitub"},
        "key_refs": ["1 Samuel 14:3", "1 Samuel 22:9", "1 Chronicles 6:7"]
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
    print(f'BP a2: Acts of the Apostles → Ahitub: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
