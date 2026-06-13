"""
BP Article Synthesis — gap-persons: Named biblical persons and places (Smith score-35)
34 entries — Smith/ISBE sources, no Easton entry

Script: scripts/bp-gap-persons.py
Run: python3 scripts/bp-gap-persons.py
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
    "abiezer": {
        "id": "abiezer",
        "term": "Abiezer",
        "category": "people",
        "intro": "<p>Abiezer (meaning <em>father of help</em>), the eldest son of Gilead and a descendant of Manasseh, gave his name to the Abiezrite clan that settled in the hill country of Ephraim during the Israelite conquest of Canaan. His lineage is recorded in <a class=\"ref\" data-ref=\"Joshua 17:2\">Joshua 17:2</a> and <a class=\"ref\" data-ref=\"1 Chronicles 7:18\">1 Chronicles 7:18</a> among the allotments given to the half-tribe of Manasseh west of the Jordan. The town of Ophrah in Abiezrite territory became the home of Joash son of Abiezer, and it was beneath the oak at Ophrah that the angel of the LORD called Joash's son Gideon to deliver Israel from Midianite oppression (<a class=\"ref\" data-ref=\"Judges 6:11\">Judges 6:11</a>).</p><p>Abiezer's most lasting significance is as the ancestral clan of Gideon, one of Israel's greatest judges. When the Spirit of the LORD clothed Gideon, he mustered his own clan first: \"the Abiezrites were called out to follow him\" (<a class=\"ref\" data-ref=\"Judges 6:34\">Judges 6:34</a>). The name also appears among David's mighty men — an Abiezrite named Abi-albon or Abiezer served among the thirty (<a class=\"ref\" data-ref=\"2 Samuel 23:27\">2 Samuel 23:27</a>; <a class=\"ref\" data-ref=\"1 Chronicles 27:12\">1 Chronicles 27:12</a>), indicating that the clan continued to produce notable warriors into the monarchic period.</p>",
        "sections": [],
        "hitchcock_meaning": "father of help",
        "source_ids": {"easton": None, "smith": "abiezer", "isbe": "abiezer"},
        "key_refs": ["Joshua 17:2", "1 Chronicles 7:18", "Judges 6:11", "Judges 6:34"]
    },
    "achaicus": {
        "id": "achaicus",
        "term": "Achaicus",
        "category": "people",
        "intro": "<p>Achaicus (meaning <em>native of Achaia</em>, or <em>sorrowing</em>) was a Christian from the Roman province of Achaia — the region encompassing most of mainland Greece — who appears in the New Testament as one of three brethren whose visit to the apostle Paul at Ephesus proved a source of great encouragement. Writing his first letter to the Corinthians, Paul says: \"I rejoice at the coming of Stephanas and Fortunatus and Achaicus, because they have made up for your absence, for they refreshed my spirit as well as yours. Give recognition to such men\" (<a class=\"ref\" data-ref=\"1 Corinthians 16:17\">1 Corinthians 16:17–18</a>).</p><p>The three had apparently traveled from Corinth bearing news of the congregation and perhaps carrying the letter of inquiry that prompted much of 1 Corinthians. The household of Stephanas is also mentioned as the firstfruits of Achaia who devoted themselves to the service of the saints (<a class=\"ref\" data-ref=\"1 Corinthians 16:15\">1 Corinthians 16:15</a>), suggesting these three men were recognized community leaders. Achaicus is not mentioned again in Scripture, but his inclusion in Paul's warm commendation marks him as a trusted representative of the Corinthian church and a genuine partner in the apostolic network connecting Greece with Paul's wider mission.</p>",
        "sections": [],
        "hitchcock_meaning": "a native of Achaia; sorrowing; sad",
        "source_ids": {"easton": None, "smith": "achaicus", "isbe": "achaicus"},
        "key_refs": ["1 Corinthians 16:17", "1 Corinthians 16:15"]
    },
    "adonizedek": {
        "id": "adonizedek",
        "term": "Adonizedek",
        "category": "people",
        "intro": "<p>Adonizedek (meaning <em>lord of justice</em> or <em>my lord is righteous</em>) was the Amorite king of Jerusalem at the time of Joshua's conquest of Canaan. When word reached him that Joshua had destroyed Ai and that Gibeon had made a separate peace with Israel, Adonizedek organized a coalition of five southern kings — including the kings of Hebron, Jarmuth, Lachish, and Eglon — to punish Gibeon and resist the Israelite advance (<a class=\"ref\" data-ref=\"Joshua 10:1\">Joshua 10:1–5</a>). Gibeon appealed to Joshua, who marched through the night from Gilgal to relieve the city.</p><p>In the ensuing battle the LORD threw the Amorite forces into confusion, rained down great hailstones on them, and famously caused the sun to stand still over Gibeon and the moon over the Valley of Aijalon while Israel pressed its victory (<a class=\"ref\" data-ref=\"Joshua 10:12\">Joshua 10:12–14</a>). The five kings fled and hid in a cave at Makkedah; Joshua commanded them brought out, defeated, executed, and their bodies hung on five trees until evening, then buried in the cave (<a class=\"ref\" data-ref=\"Joshua 10:26\">Joshua 10:26–27</a>). Adonizedek's defeat broke the southern Amorite coalition and opened the Shephelah and hill country to continued Israelite conquest.</p>",
        "sections": [],
        "hitchcock_meaning": "justice of the Lord; lord of justice",
        "source_ids": {"easton": None, "smith": "adonizedek", "isbe": None},
        "key_refs": ["Joshua 10:1", "Joshua 10:3", "Joshua 10:12", "Joshua 10:26"]
    },
    "aeneas": {
        "id": "aeneas",
        "term": "Aeneas",
        "category": "people",
        "intro": "<p>Aeneas (meaning <em>praised</em> or <em>praiseworthy</em>) was a man of Lydda, a town on the coastal plain of Sharon, who had been paralyzed and bedridden for eight years when the apostle Peter passed through the region. His healing is one of the most concise miracle accounts in Acts: \"Peter said to him, 'Aeneas, Jesus Christ heals you; rise and make your bed.' And immediately he rose\" (<a class=\"ref\" data-ref=\"Acts 9:33\">Acts 9:33–34</a>). The text does not specify whether Aeneas was already a believer before his healing, though he was clearly known to the local community of saints.</p><p>The significance of his healing extended well beyond the individual miracle. Luke records that \"all the residents of Lydda and Sharon saw him, and they turned to the Lord\" (<a class=\"ref\" data-ref=\"Acts 9:35\">Acts 9:35</a>), making Aeneas's restoration a catalyst for widespread evangelization along the coastal plain. His story in Acts 9 stands alongside the resurrection of Tabitha (Dorcas) at nearby Joppa, framing Peter's coastal ministry as a concentrated display of the same healing power that had characterized Jesus' ministry in Galilee and demonstrating that the risen Christ continued to act through his apostles in extending the church into new territory.</p>",
        "sections": [],
        "hitchcock_meaning": "praised; praiseworthy",
        "source_ids": {"easton": None, "smith": "aeneas", "isbe": "aeneas"},
        "key_refs": ["Acts 9:33", "Acts 9:34", "Acts 9:35"]
    },
    "agrippa": {
        "id": "agrippa",
        "term": "Agrippa",
        "category": "people",
        "intro": "<p>Agrippa is the family name of two members of the Herodian dynasty prominent in the New Testament. Herod Agrippa I (died AD 44), grandson of Herod the Great, was the last Jewish king to rule over a substantial portion of Palestine under Roman sanction. He persecuted the early church, executing James the son of Zebedee with the sword and imprisoning Peter (<a class=\"ref\" data-ref=\"Acts 12:1\">Acts 12:1–3</a>), intending to execute him after Passover. His dramatic death — struck down by an angel in Caesarea because he accepted divine honors from the crowd (<a class=\"ref\" data-ref=\"Acts 12:23\">Acts 12:23</a>) — is treated by Luke as a divine judgment on his pride.</p><p>Herod Agrippa II (born AD 28), his son, appeared before Paul during Paul's imprisonment at Caesarea, presiding with the Roman governor Festus and his sister Bernice over an extended hearing in Acts 25–26. Paul's eloquent testimony of his conversion and apostolic commission drew the famous response: \"In a short time would you persuade me to be a Christian?\" (<a class=\"ref\" data-ref=\"Acts 26:28\">Acts 26:28</a>). Agrippa concluded with Festus that Paul had done nothing deserving death or imprisonment and could have been freed had he not appealed to Caesar, making him the last royal figure to hear Paul's defense in Judea before his voyage to Rome.</p>",
        "sections": [],
        "hitchcock_meaning": "one who causes great pain at his birth",
        "source_ids": {"easton": None, "smith": "agrippa", "isbe": "agrippa"},
        "key_refs": ["Acts 12:1", "Acts 12:23", "Acts 25:23", "Acts 26:28"]
    },
    "aphek": {
        "id": "aphek",
        "term": "Aphek",
        "category": "places",
        "intro": "<p>Aphek (meaning <em>strength</em> or <em>fortress</em>) is the name of several distinct cities in ancient Palestine. The most historically significant stood on the coastal plain of Sharon controlling the key pass on the route between Egypt and Mesopotamia. A royal Canaanite city whose king was defeated by Joshua (<a class=\"ref\" data-ref=\"Joshua 12:18\">Joshua 12:18</a>), it was likely here or nearby that the Philistines camped before two of Israel's most catastrophic battles — the engagement at Ebenezer where the ark of God was captured (<a class=\"ref\" data-ref=\"1 Samuel 4:1\">1 Samuel 4:1</a>) and the battle of Jezreel where Saul fell (<a class=\"ref\" data-ref=\"1 Samuel 29:1\">1 Samuel 29:1</a>). This Aphek is generally identified with Tel Aphek (Antipatris) at the source of the Yarkon River.</p><p>A second Aphek lay in the extreme north of Asher (<a class=\"ref\" data-ref=\"Joshua 19:30\">Joshua 19:30</a>), from which the Canaanites were never expelled (Judges 1:31). A third Aphek in Transjordan was the site where Ben-hadad of Syria encamped against Israel, and where Elisha prophesied Syria's defeat: \"You shall strike down the Syrians in Aphek until you have made an end of them\" (<a class=\"ref\" data-ref=\"1 Kings 20:26\">1 Kings 20:26–30</a>). The multiplicity of sites bearing this name reflects the widespread use of the word as a topographical designation for fortified strongholds throughout Canaan.</p>",
        "sections": [],
        "hitchcock_meaning": "strength; a rapid torrent",
        "source_ids": {"easton": None, "smith": "aphek", "isbe": "aphek"},
        "key_refs": ["Joshua 12:18", "1 Samuel 4:1", "1 Samuel 29:1", "1 Kings 20:26"]
    },
    "artemas": {
        "id": "artemas",
        "term": "Artemas",
        "category": "people",
        "intro": "<p>Artemas (meaning <em>whole</em> or <em>sound</em>; possibly a shortened form of Artemidoros, \"gift of Artemis\") was a trusted companion and associate of the apostle Paul, mentioned once in the Epistle to Titus. Paul writes: \"When I send Artemas or Tychicus to you, do your best to come to me at Nicopolis, for I have decided to spend the winter there\" (<a class=\"ref\" data-ref=\"Titus 3:12\">Titus 3:12</a>). The pairing with Tychicus — one of Paul's most reliable delegates (Ephesians 6:21; Colossians 4:7; 2 Timothy 4:12) — suggests Artemas was of comparable stature and capability, able to assume oversight of the Cretan churches in Titus's absence.</p><p>Beyond this single reference, Artemas's career is attested only in later church tradition. Dorotheus and other early ecclesiastical writers identified him as one of the seventy disciples sent out by Jesus (Luke 10:1) and assigned him the bishopric of Lystra in Asia Minor — the city where Paul and Barnabas had worked and where Timothy originated. These traditions cannot be confirmed from Scripture, but Paul's naming of Artemas as a potential replacement for Titus in the important mission field of Crete indicates he was an experienced, trusted church worker in the apostolic circle whose administrative and pastoral gifts were well established.</p>",
        "sections": [],
        "hitchcock_meaning": "whole, sound",
        "source_ids": {"easton": None, "smith": "artemas", "isbe": "artemas"},
        "key_refs": ["Titus 3:12"]
    },
    "ashima": {
        "id": "ashima",
        "term": "Ashima",
        "category": "concepts",
        "intro": "<p>Ashima was a deity introduced into the territory of Samaria by the Hamathite colonists settled there after the Assyrian deportation of the northern tribes of Israel (c. 722 BC). When the Assyrian king repopulated the vacant Israelite territories with peoples from various nations, each group brought its own gods: \"The men of Hamath made Ashima\" (<a class=\"ref\" data-ref=\"2 Kings 17:30\">2 Kings 17:30</a>). This statement appears in the catalogue of foreign gods — alongside Succoth-benoth, Nergal, Nibhaz, Tartak, Adrammelech, and Anammelech — that the biblical narrator uses to illustrate the religious corruption of the mixed population in the former northern kingdom.</p><p>The identity and nature of Ashima remain obscure. Some scholars connect the name with an Aramaic word for \"guilt\" or \"transgression\"; others have tentatively identified Ashima with a goat-deity or with a figure resembling the Greek Pan. The biblical text's primary concern is not the precise character of Ashima but what it represents: the syncretism that resulted when foreign settlers combined the worship of the LORD with their own national cults, \"fearing the LORD but also serving their own gods\" (<a class=\"ref\" data-ref=\"2 Kings 17:33\">2 Kings 17:33</a>). This is the same pattern of faithlessness the author of Kings had condemned in the northern kingdom, now replicated by its foreign replacements on the same land.</p>",
        "sections": [],
        "hitchcock_meaning": "crime; offense",
        "source_ids": {"easton": None, "smith": "ashima", "isbe": "ashima"},
        "key_refs": ["2 Kings 17:30", "2 Kings 17:33"]
    },
    "ashur": {
        "id": "ashur",
        "term": "Ashur",
        "category": "people",
        "intro": "<p>Ashur (also spelled Ashhur) was the posthumous son of Hezron by his second wife Abiah, born after Hezron's death (<a class=\"ref\" data-ref=\"1 Chronicles 2:24\">1 Chronicles 2:24</a>). His genealogy appears among the descendants of Judah in the early chapters of 1 Chronicles, and he is identified as the \"father\" — meaning founder or progenitor — of the town of Tekoa (<a class=\"ref\" data-ref=\"1 Chronicles 4:5\">1 Chronicles 4:5</a>). In ancient Israelite genealogical usage, \"father of [a city]\" designates the ancestor or settler who established the community associated with that place, indicating that Ashur's family gave its identity to the settlement of Tekoa in the hill country of Judah.</p><p>Tekoa, the city connected with Ashur's name, later became significant in Israelite history. It was the hometown of the prophet Amos, a shepherd and dresser of sycamore figs called from Tekoa to prophesy to the northern kingdom (<a class=\"ref\" data-ref=\"Amos 1:1\">Amos 1:1</a>). The wise woman whom Joab dispatched to persuade David to receive Absalom was also from Tekoa (<a class=\"ref\" data-ref=\"2 Samuel 14:2\">2 Samuel 14:2</a>), suggesting the town was associated with notable wisdom. Ashur himself, though appearing only in a genealogical list, represents the kind of founding figure whose descendants shaped the geography and character of Judah's heartland during the early settlement period.</p>",
        "sections": [],
        "hitchcock_meaning": "who is happy; or walks; or looks",
        "source_ids": {"easton": None, "smith": "ashur", "isbe": "ashur"},
        "key_refs": ["1 Chronicles 2:24", "1 Chronicles 4:5", "Amos 1:1", "2 Samuel 14:2"]
    },
    "asyncritus": {
        "id": "asyncritus",
        "term": "Asyncritus",
        "category": "people",
        "intro": "<p>Asyncritus (meaning <em>incomparable</em>) was a Christian at Rome to whom the apostle Paul sent greetings in the closing chapter of his letter to the Romans: \"Greet Asyncritus, Phlegon, Hermes, Patrobas, Hermas, and the brothers who are with them\" (<a class=\"ref\" data-ref=\"Romans 16:14\">Romans 16:14</a>). He is grouped with four other named individuals and an unnamed circle of brothers, suggesting these five may have formed a distinct household church or fellowship group within the larger Roman Christian community. The phrase \"the brothers who are with them\" implies they were a recognized cluster of believers, perhaps meeting in the same home.</p><p>Nothing further is known of Asyncritus from Scripture. The name (Greek: <em>Asunkritos</em>) appears in inscriptions from Rome, including records associated with the imperial household, leading some scholars to suggest that Asyncritus may have been a slave or freedman connected with the emperor's service. Paul's extensive list of named greetings in Romans 16 is remarkable for its personal specificity, indicating prior acquaintance with many Roman believers before his planned visit. Asyncritus's inclusion marks him as a recognized member of the capital's Christian community — a name that Paul knew, honored, and thought worthy of apostolic acknowledgment as he prepared to bring the gospel to Rome itself.</p>",
        "sections": [],
        "hitchcock_meaning": "incomparable",
        "source_ids": {"easton": None, "smith": "asyncritus", "isbe": "asyncritus"},
        "key_refs": ["Romans 16:14"]
    },
    "attalia": {
        "id": "attalia",
        "term": "Attalia",
        "category": "places",
        "intro": "<p>Attalia was a seaport city on the southern coast of Asia Minor in the ancient region of Pamphylia, situated where the Catarrhactes River (modern Karpuz Çayı) meets the Mediterranean. It was founded in the second century BC by Attalus II Philadelphus, king of Pergamon (reigned 159–138 BC), who gave it his name. The city's naturally sheltered harbor made it the principal port of Pamphylia and the gateway to the interior of Asia Minor, and it functioned as a major hub of eastern Mediterranean trade throughout the Roman period.</p><p>Attalia appears in Scripture in the account of Paul and Barnabas's first missionary journey. After completing their preaching in Perga in Pamphylia, \"they went down to Attalia, and from there they sailed to Antioch\" (<a class=\"ref\" data-ref=\"Acts 14:25\">Acts 14:25–26</a>). The city thus served as the point of embarkation for their return voyage to Syrian Antioch, where they reported to the church that had commissioned them and gave thanks for all that God had done. The modern city of Antalya, Turkey, stands on the same site, preserving in slightly modified form the ancient name, making Attalia one of the most directly identifiable New Testament locations in the present-day landscape.</p>",
        "sections": [],
        "hitchcock_meaning": "that increases or sends",
        "source_ids": {"easton": None, "smith": "attalia", "isbe": "attalia"},
        "key_refs": ["Acts 14:25", "Acts 14:26"]
    },
    "baca": {
        "id": "baca",
        "term": "Baca, Valley of",
        "category": "places",
        "intro": "<p>The Valley of Baca appears in a single passage of the Old Testament — the great pilgrimage psalm of Psalm 84 — where it describes a place the faithful must traverse on their journey to the sanctuary of the LORD at Zion: \"Blessed are those whose strength is in you, in whose heart are the highways to Zion. As they go through the Valley of Baca they make it a spring; the early rain also covers it with pools\" (<a class=\"ref\" data-ref=\"Psalms 84:5\">Psalm 84:5–6</a>). The Hebrew word <em>baka'</em> is connected with weeping or lamentation, suggesting the Valley of Baca is a \"valley of weeping\" — a dry, difficult, or sorrowful stretch of the pilgrim route that must be crossed to reach the house of God.</p><p>The precise geographical location of Baca is unknown and has been debated since antiquity; some place it in the Sinai region, others near Jerusalem. In the context of the psalm, the location matters less than the theological transformation it represents: the valley of weeping becomes a place of springs through the pilgrims' trust in God. This inversion — hardship turned to refreshment, tears turned to pools — has made the Valley of Baca a classic text in the spirituality of pilgrimage and suffering, read across centuries as a promise that the journey through difficulty, undertaken in faith, becomes itself the path into the presence of God.</p>",
        "sections": [],
        "hitchcock_meaning": "a mulberry-tree",
        "source_ids": {"easton": None, "smith": "baca", "isbe": "baca"},
        "key_refs": ["Psalms 84:5", "Psalms 84:6"]
    },
    "berith": {
        "id": "berith",
        "term": "Berith",
        "category": "concepts",
        "intro": "<p>Berith is the abbreviated name for Baal-berith (\"lord of the covenant\"), the Canaanite deity whose temple at Shechem plays a pivotal role in the narrative of Abimelech in Judges 9. After Gideon's death the people of Shechem \"went whoring after the Baals and made Baal-berith their god\" (<a class=\"ref\" data-ref=\"Judges 8:33\">Judges 8:33</a>). The temple of Berith at Shechem served as the city's treasury: Abimelech received seventy pieces of silver from \"the house of Baal-berith\" to fund his campaign to murder his seventy brothers and seize sole rule (<a class=\"ref\" data-ref=\"Judges 9:4\">Judges 9:4</a>). The funding of fratricide from a god's treasury is presented as emblematic of Shechem's moral corruption.</p><p>The deity's name combines <em>baal</em> (lord) with <em>berith</em> (covenant), suggesting a god who presided over treaty-making or alliances in Canaanite religious practice. Later in the same chapter (Judges 9:46), when Abimelech attacked Shechem, the citizens took refuge \"in the stronghold of the house of El-berith\" — the same deity under a variant title. Abimelech burned the stronghold with its occupants inside, fulfilling the curse of Jotham's parable of the thornbush king (<a class=\"ref\" data-ref=\"Judges 9:20\">Judges 9:20</a>). The destruction of the Berith temple stands as the judgment on Shechem's apostasy and illustrates the self-destructive consequences of political and religious compromise with Canaanite cult.</p>",
        "sections": [],
        "hitchcock_meaning": "covenant",
        "source_ids": {"easton": None, "smith": "berith", "isbe": "berith"},
        "key_refs": ["Judges 8:33", "Judges 9:4", "Judges 9:46", "Judges 9:20"]
    },
    "carpus": {
        "id": "carpus",
        "term": "Carpus",
        "category": "people",
        "intro": "<p>Carpus (meaning <em>fruit</em> or <em>fruitful</em>) was a Christian at Troas on the Aegean coast of Asia Minor with whom the apostle Paul had left possessions during an earlier visit. Paul mentions him in his final letter to Timothy, written from his second Roman imprisonment (c. AD 67): \"When you come, bring the cloak that I left with Carpus at Troas, also the books, and above all the parchments\" (<a class=\"ref\" data-ref=\"2 Timothy 4:13\">2 Timothy 4:13</a>). The request reveals that Carpus had been entrusted with a traveling cloak, writing codices, and what were probably parchment manuscripts of Scripture or other documents, left behind at Paul's last stop in Troas before his final arrest.</p><p>The detail is remarkable for what it shows of Paul's situation and priorities at the end of his life: the cloak suggests cold prison conditions, and the insistence on receiving the books and parchments \"above all\" indicates his continuing intellectual and pastoral work even under the prospect of execution. Carpus is not mentioned elsewhere in Scripture, but the easy familiarity of the request — assuming Timothy would know exactly who Carpus is and where he lives — points to a continuing relationship between the apostolic circle and this Christian household at Troas, the same city where Paul had raised Eutychus from the dead (<a class=\"ref\" data-ref=\"Acts 20:9\">Acts 20:9–12</a>) and received the Macedonian vision (<a class=\"ref\" data-ref=\"Acts 16:8\">Acts 16:8–9</a>).</p>",
        "sections": [],
        "hitchcock_meaning": "fruit; fruitful",
        "source_ids": {"easton": None, "smith": "carpus", "isbe": "carpus"},
        "key_refs": ["2 Timothy 4:13", "Acts 20:9", "Acts 16:8"]
    },
    "charchemish": {
        "id": "charchemish",
        "term": "Carchemish",
        "category": "places",
        "intro": "<p>Carchemish (also spelled Charchemish) was a major city and strategic ford on the upper Euphrates River, situated near the modern Turkish-Syrian border (identified with Jerablus/Europos). The city controlled the most important crossing point of the Euphrates River on the route between Mesopotamia and the Mediterranean world, making it one of the most contested prizes in ancient Near Eastern geopolitics. It served successively as a Hittite capital, an Assyrian provincial center, and a key staging point for the campaigns of later empires.</p><p>Carchemish appears in Scripture in two pivotal contexts. First, it was the site of a decisive battle in 605 BC when Nebuchadnezzar II of Babylon crushed the Egyptian army of Pharaoh Necho II, ending Egypt's bid for control of Syria-Palestine and ushering in Babylonian supremacy (<a class=\"ref\" data-ref=\"Jeremiah 46:2\">Jeremiah 46:2</a>). This battle had been preceded by the death of King Josiah at Megiddo when he fatally intercepted Necho's march north (<a class=\"ref\" data-ref=\"2 Chronicles 35:20\">2 Chronicles 35:20–24</a>), marking the beginning of Judah's final decline. Second, Isaiah cited Carchemish among the cities already swept up by Assyrian power as a warning to Israel that no earthly fortress could stand against divine judgment (<a class=\"ref\" data-ref=\"Isaiah 10:9\">Isaiah 10:9</a>).</p>",
        "sections": [],
        "hitchcock_meaning": "a lamb; as taken away; withdrawn",
        "source_ids": {"easton": None, "smith": "charchemish", "isbe": "charchemish"},
        "key_refs": ["Jeremiah 46:2", "2 Chronicles 35:20", "Isaiah 10:9"]
    },
    "cozbi": {
        "id": "cozbi",
        "term": "Cozbi",
        "category": "people",
        "intro": "<p>Cozbi (meaning <em>deceitful</em> or <em>sliding away</em>) was a Midianite woman whose brazen liaison with an Israelite man during the apostasy at Baal-peor precipitated both a plague and a decisive act of priestly zeal. While Israel was engaging in sexual immorality with Moabite women and worshipping their gods — an apostasy that brought a plague killing twenty-four thousand people — an Israelite named Zimri publicly brought Cozbi, daughter of the Midianite chief Zur, into the camp in full view of the weeping congregation and Moses (<a class=\"ref\" data-ref=\"Numbers 25:6\">Numbers 25:6–8</a>). The priest Phinehas son of Eleazar rose, took a spear, followed them, and ran them both through, ending the plague.</p><p>Cozbi's father Zur was \"head of the people of a father's house in Midian\" (<a class=\"ref\" data-ref=\"Numbers 25:15\">Numbers 25:15</a>), making her a chieftain's daughter whose presence in the Israelite camp was no accident. The LORD cited her death specifically when commanding Israel to treat the Midianites as enemies, because they \"have harassed you with their wiles\" in the affair of Peor (<a class=\"ref\" data-ref=\"Numbers 25:18\">Numbers 25:18</a>). Phinehas's act was counted to him as righteousness \"from generation to generation forever\" (<a class=\"ref\" data-ref=\"Psalms 106:31\">Psalm 106:31</a>), and the Levitical priesthood derived special honor from his decisive intervention in this crisis of Israel's covenant faithfulness.</p>",
        "sections": [],
        "hitchcock_meaning": "a liar; sliding away",
        "source_ids": {"easton": None, "smith": "cozbi", "isbe": "cozbi"},
        "key_refs": ["Numbers 25:6", "Numbers 25:15", "Numbers 25:18", "Psalms 106:31"]
    },
    "eubulus": {
        "id": "eubulus",
        "term": "Eubulus",
        "category": "people",
        "intro": "<p>Eubulus (meaning <em>prudent</em> or <em>of good counsel</em>) was a Christian at Rome, one of Paul's companions during his final imprisonment, who sent greetings to Timothy in the closing words of 2 Timothy: \"Eubulus sends greetings to you, as do Pudens and Linus and Claudia and all the brothers\" (<a class=\"ref\" data-ref=\"2 Timothy 4:21\">2 Timothy 4:21</a>). Paul's second letter to Timothy — widely regarded as his last surviving correspondence, composed shortly before his execution — conveys both pastoral urgency and personal warmth. The greeting from Eubulus and his companions underscores the contrast between Paul's isolation at his first defense (\"no one came to stand by me,\" 4:16) and the continuing loyalty of those who remained faithful.</p><p>Eubulus is not mentioned elsewhere in the New Testament, and his subsequent history is not recorded. His name appears in Roman inscriptions and was common in the Hellenistic world. Notably, he is listed alongside Linus, whom early church tradition unanimously identifies as the first bishop of Rome after Peter and Paul, suggesting Eubulus was a recognized member of the Roman church's leadership circle. His brief appearance at the very end of Paul's final letter is a small window onto the community of faith that sustained Paul in his last days and maintained the church's life in the imperial capital during the apostolic generation.</p>",
        "sections": [],
        "hitchcock_meaning": "prudent; good counselor",
        "source_ids": {"easton": None, "smith": "eubulus", "isbe": "eubulus"},
        "key_refs": ["2 Timothy 4:21"]
    },
    "herod": {
        "id": "herod",
        "term": "Herod",
        "category": "people",
        "intro": "<p>Herod is the dynastic name of the Idumean family that governed various portions of Palestine as client rulers under Roman authority from 37 BC to the late first century AD. Herod the Great (reigned 37–4 BC) was appointed king of Judea by the Roman Senate and undertook massive building projects including the reconstruction of the Jerusalem temple. The New Testament introduces him as the king who, alarmed by reports of a newborn \"king of the Jews,\" ordered the massacre of infant boys in Bethlehem (<a class=\"ref\" data-ref=\"Matthew 2:1\">Matthew 2:1–18</a>). His kingdom was divided after his death among his sons Archelaus, Antipas, and Philip.</p><p>Herod Antipas (reigned 4 BC–AD 39), tetrarch of Galilee and Perea, imprisoned and beheaded John the Baptist (<a class=\"ref\" data-ref=\"Matthew 14:1\">Matthew 14:1–12</a>) and briefly examined Jesus during the Passion (<a class=\"ref\" data-ref=\"Luke 23:7\">Luke 23:7–12</a>). Two later members of the dynasty appear prominently in Acts: Herod Agrippa I, who executed James and imprisoned Peter before his judgment death (<a class=\"ref\" data-ref=\"Acts 12:1\">Acts 12:1–23</a>), and Herod Agrippa II, before whom Paul delivered one of his most memorable defenses (<a class=\"ref\" data-ref=\"Acts 26:28\">Acts 26:28</a>). The Herodian dynasty thus appears at multiple pivotal moments in both the Gospels and Acts, its ambivalent relationship with Judaism and Rome forming a recurring backdrop to the New Testament story.</p>",
        "sections": [],
        "hitchcock_meaning": "son of a hero",
        "source_ids": {"easton": None, "smith": "herod", "isbe": "herod"},
        "key_refs": ["Matthew 2:1", "Matthew 14:1", "Acts 12:1", "Acts 26:28"]
    },
    "joses": {
        "id": "joses",
        "term": "Joses",
        "category": "people",
        "intro": "<p>Joses (a form of Joseph, meaning <em>he will add</em>) is the name of several figures in the New Testament. Most prominent is Joses listed among the brothers of Jesus — \"Is not this the carpenter's son? Is not his mother called Mary? And are not his brothers James and Joses and Simon and Judas?\" (<a class=\"ref\" data-ref=\"Matthew 13:55\">Matthew 13:55</a>; cf. <a class=\"ref\" data-ref=\"Mark 6:3\">Mark 6:3</a>). The nature of this relationship — whether full brothers, half-brothers through Joseph by a prior marriage, or cousins — has been a matter of theological debate since the patristic period. A woman named Mary the mother of Joses appears at the crucifixion and tomb (<a class=\"ref\" data-ref=\"Matthew 27:56\">Matthew 27:56</a>; Mark 15:40, 47).</p><p>The most consequential figure bearing the name Joses is Joses surnamed Barnabas by the apostles — the Levite from Cyprus who sold a field and laid the proceeds at the apostles' feet in the early Jerusalem community (<a class=\"ref\" data-ref=\"Acts 4:36\">Acts 4:36</a>), an act of generosity standing in sharp contrast to the deception of Ananias and Sapphira. As Barnabas, he became one of the most significant figures in the gentile mission: championing Paul after his conversion, accompanying him on the first missionary journey through Cyprus and Asia Minor, and later working independently in Cyprus with Mark. The nickname \"son of encouragement\" (Barnabas) effectively replaced the name Joses entirely in the tradition that preserved his memory.</p>",
        "sections": [],
        "hitchcock_meaning": "same as Jose",
        "source_ids": {"easton": None, "smith": "joses", "isbe": "joses"},
        "key_refs": ["Matthew 13:55", "Mark 6:3", "Matthew 27:56", "Acts 4:36"]
    },
    "lahairoi": {
        "id": "lahairoi",
        "term": "Beer-lahai-roi",
        "category": "places",
        "intro": "<p>Beer-lahai-roi (\"well of the Living One who sees me\"), sometimes referred to as Lahairoi, was a well or spring in the wilderness on the road to Shur, south and west of Canaan toward Egypt. Its naming records one of the most theologically profound encounters in the patriarchal narratives: Hagar, the Egyptian servant of Sarah, had fled from her mistress's harshness when the angel of the LORD found her at the spring. After delivering the promise of a son and a command to return, the angel departed and Hagar said: \"You are a God of seeing... Truly here I have seen him who looks after me\" (<a class=\"ref\" data-ref=\"Genesis 16:13\">Genesis 16:13–14</a>). Her words gave the well its name — a memorial to divine care extended to the marginalized.</p><p>The well appears again in the lives of the patriarchs as a place of habitation and perhaps of prayer. When Rebekah first saw Isaac, he was coming from Beer-lahai-roi where he had gone to meditate in the field at evening (<a class=\"ref\" data-ref=\"Genesis 24:62\">Genesis 24:62</a>), and after Abraham's death, Isaac settled near the well (<a class=\"ref\" data-ref=\"Genesis 25:11\">Genesis 25:11</a>). These details connect Beer-lahai-roi to the founding of successive generations of the patriarchal line. Its precise location in the Negev wilderness remains unidentified, but its significance in Genesis lies in its testimony that God sees and provides for those whom human society has cast aside — a theme that runs through the entire arc of Hagar's story.</p>",
        "sections": [],
        "hitchcock_meaning": "who liveth and seeth me",
        "source_ids": {"easton": None, "smith": "lahairoi", "isbe": None},
        "key_refs": ["Genesis 16:13", "Genesis 16:14", "Genesis 24:62", "Genesis 25:11"]
    },
    "lasea": {
        "id": "lasea",
        "term": "Lasea",
        "category": "places",
        "intro": "<p>Lasea was a coastal town on the southern shore of the island of Crete, mentioned once in Scripture in connection with Paul's sea voyage to Rome. Acts 27:8 records the ship's difficult progress: \"With difficulty we sailed along it and came to a place called Fair Havens, near which was the city of Lasea.\" The proximity of Lasea to Fair Havens (Kaloi Limenes) places it a few miles east of that harbor on Crete's south coast, in the district of ancient Gortyn. The area was considered an exposed anchorage unsuitable for wintering a large vessel.</p><p>Lasea was virtually unknown to modern scholarship until its ruins were discovered in 1856, approximately five miles east of Fair Havens, confirming Luke's geographical precision. At Fair Havens the centurion in charge of Paul's voyage held a consultation about whether to remain for winter or press on to the better harbor of Phoenix on Crete's western end. Paul urged staying, warning of disaster, but was overruled (<a class=\"ref\" data-ref=\"Acts 27:9\">Acts 27:9–12</a>). The ill-fated decision to sail led to the famous storm and shipwreck on Malta that forms one of the most vivid travel narratives in Acts. Lasea's mention in this account contributes to the nautical accuracy that characterizes Luke's description of the voyage, widely noted for its technical maritime precision and geographical detail.</p>",
        "sections": [],
        "hitchcock_meaning": "thick; wise",
        "source_ids": {"easton": None, "smith": "lasea", "isbe": "lasea"},
        "key_refs": ["Acts 27:8", "Acts 27:9"]
    },
    "linus": {
        "id": "linus",
        "term": "Linus",
        "category": "people",
        "intro": "<p>Linus (meaning <em>net</em>) was a Christian at Rome who sent greetings to Timothy in Paul's final letter: \"Eubulus sends greetings to you, as do Pudens and Linus and Claudia and all the brothers\" (<a class=\"ref\" data-ref=\"2 Timothy 4:21\">2 Timothy 4:21</a>). In Scripture this is his only appearance, but his significance in early church history is considerable: the unanimous testimony of ancient writers — including Irenaeus (<em>Against Heresies</em> III.3.3, c. AD 180), Tertullian, Hegesippus (cited by Eusebius), and the Apostolic Constitutions — identifies Linus as the first bishop of Rome after the apostles Peter and Paul, governing the Roman church from approximately AD 67 to 79.</p><p>Irenaeus, in establishing the apostolic succession of the Roman church as a check against heresy, lists Linus by name as the first bishop, followed by Anacletus and then Clement of Rome. This identification of the Linus of 2 Timothy with the first post-apostolic Roman bishop has been accepted by virtually all ancient sources, making Paul's single greeting a significant data point in the early history of Roman church leadership. The context of 2 Timothy — Paul facing imminent execution, deserted by many, clinging to faithful remnants — gives the mention of Linus an additional poignancy: the man who would carry forward the apostolic oversight of the mother church of the West is present beside Paul in his final days.</p>",
        "sections": [],
        "hitchcock_meaning": "net",
        "source_ids": {"easton": None, "smith": "linus", "isbe": "linus"},
        "key_refs": ["2 Timothy 4:21"]
    },
    "milcom": {
        "id": "milcom",
        "term": "Milcom",
        "category": "concepts",
        "intro": "<p>Milcom (meaning <em>their king</em>), also known as Molech or Moloch, was the national deity of the Ammonites and one of the most condemned idols in the Old Testament. The name derives from the Hebrew root for \"king\" (<em>melek</em>), presenting this god as the divine sovereign of the Ammonite people. Milcom was closely related in character and cult to the Moabite god Chemosh, and both were classified in the biblical tradition among the \"abominations\" of the surrounding nations. The rite most associated with Milcom worship was the offering of children in fire — a practice explicitly prohibited in the Mosaic law (<a class=\"ref\" data-ref=\"Leviticus 18:21\">Leviticus 18:21</a>; <a class=\"ref\" data-ref=\"Leviticus 20:2\">20:2–5</a>; <a class=\"ref\" data-ref=\"Deuteronomy 18:10\">Deuteronomy 18:10</a>).</p><p>Solomon's apostasy in his old age included building a high place for Milcom on the hill east of Jerusalem, called an \"abomination of the Ammonites\" (<a class=\"ref\" data-ref=\"1 Kings 11:5\">1 Kings 11:5</a>, 7), which was dismantled only by Josiah's reform (<a class=\"ref\" data-ref=\"2 Kings 23:13\">2 Kings 23:13</a>). The valley of Hinnom, called Topheth, became the site of Molech worship under later Judean kings — a place where children were burned in fire, an act Jeremiah condemned as something God had never commanded (<a class=\"ref\" data-ref=\"Jeremiah 32:35\">Jeremiah 32:35</a>). The valley's defilement under Josiah transformed it into Gehenna, the enduring biblical symbol of final judgment and the destruction that follows the rejection of God's covenant.</p>",
        "sections": [],
        "hitchcock_meaning": "their king",
        "source_ids": {"easton": None, "smith": "milcom", "isbe": "milcom"},
        "key_refs": ["1 Kings 11:5", "2 Kings 23:13", "Leviticus 18:21", "Jeremiah 32:35"]
    },
    "prochorus": {
        "id": "prochorus",
        "term": "Prochorus",
        "category": "people",
        "intro": "<p>Prochorus (meaning <em>leader of the chorus</em>) was one of the seven men chosen by the Jerusalem church to oversee the daily distribution to the Hellenistic widows, freeing the apostles to concentrate on prayer and the ministry of the word (<a class=\"ref\" data-ref=\"Acts 6:1\">Acts 6:1–6</a>). He is listed third in canonical order: \"they chose Stephen, a man full of faith and of the Holy Spirit, and Philip, and Prochorus, and Nicanor, and Timon, and Parmenas, and Nicolaus, a proselyte of Antioch\" (<a class=\"ref\" data-ref=\"Acts 6:5\">Acts 6:5</a>). The seven were presented to the apostles, who prayed and laid hands on them, formally commissioning them for the work.</p><p>While Stephen and Philip go on to starring roles in Acts — Stephen as the first martyr and Philip as the evangelist in Samaria and on the Gaza road — Prochorus is not mentioned again in the canonical New Testament. Later tradition, however, makes him a significant figure: the apocryphal <em>Acts of John</em> identifies him as the apostle John's companion and secretary, accompanying him into exile on Patmos and writing the Book of Revelation from John's dictation. Some manuscript traditions of Revelation's prologue name Prochorus explicitly. Church tradition further identifies him as bishop of Nicomedia in Bithynia and later of Antioch, commemorated as a martyr in Eastern Christianity, though these claims are not confirmed by Scripture.</p>",
        "sections": [],
        "hitchcock_meaning": "he that presides over the choirs",
        "source_ids": {"easton": None, "smith": "prochorus", "isbe": "prochorus"},
        "key_refs": ["Acts 6:5"]
    },
    "ramah": {
        "id": "ramah",
        "term": "Ramah",
        "category": "places",
        "intro": "<p>Ramah (meaning <em>height</em> or <em>high place</em>) is the name of multiple hilltop settlements in the Old Testament landscape, reflecting the widespread use of this topographical term. The most theologically significant is Ramah of Benjamin — also called Ramathaim-zophim or Ramah of Ephraim — a town approximately five miles north of Jerusalem identified with modern er-Ram. It sat on the ridge road through the central hill country near Gibeah (<a class=\"ref\" data-ref=\"Judges 4:5\">Judges 4:5</a>; 19:13), and its population returned from Babylonian exile among the early groups of returnees (<a class=\"ref\" data-ref=\"Ezra 2:26\">Ezra 2:26</a>).</p><p>This Ramah was the town most deeply connected with the prophet Samuel: it was his home and the center of his judicial circuit (<a class=\"ref\" data-ref=\"1 Samuel 7:17\">1 Samuel 7:17</a>), his official residence, the site of his altar, and his burial place (<a class=\"ref\" data-ref=\"1 Samuel 25:1\">1 Samuel 25:1</a>). It was here that the people came to demand a king (<a class=\"ref\" data-ref=\"1 Samuel 8:4\">1 Samuel 8:4</a>), and here that Saul first encountered Samuel. Ramah also appears in Jeremiah's lament: \"A voice is heard in Ramah, lamentation and bitter weeping. Rachel is weeping for her children\" (<a class=\"ref\" data-ref=\"Jeremiah 31:15\">Jeremiah 31:15</a>) — a prophecy Matthew quotes in connection with Herod's massacre of the Bethlehem infants (<a class=\"ref\" data-ref=\"Matthew 2:18\">Matthew 2:18</a>), giving Ramah eschatological resonance in the New Testament story of redemption.</p>",
        "sections": [],
        "hitchcock_meaning": "same as Ram",
        "source_ids": {"easton": None, "smith": "ramah", "isbe": "ramah"},
        "key_refs": ["1 Samuel 7:17", "1 Samuel 25:1", "Jeremiah 31:15", "Matthew 2:18"]
    },
    "sanhedrin": {
        "id": "sanhedrin",
        "term": "Sanhedrin",
        "category": "concepts",
        "intro": "<p>The Sanhedrin (from Greek <em>synedrion</em>, \"sitting together\" or \"council\") was the supreme judicial, legislative, and religious council of the Jewish people during the Second Temple period. In its classic form it consisted of seventy-one members — a presiding officer (nasi) plus seventy elders — tracing its symbolic ancestry to the seventy elders Moses appointed to assist in governing Israel (<a class=\"ref\" data-ref=\"Numbers 11:16\">Numbers 11:16–17</a>). Its membership included chief priests, elders of prominent families, and Pharisaic scribes, with the high priest generally presiding. Meeting in Jerusalem, the body exercised authority over religious law, communal governance, and (under Roman oversight) capital cases.</p><p>The Sanhedrin plays a central role in the New Testament. Jesus was examined by the council after his arrest (<a class=\"ref\" data-ref=\"Matthew 26:59\">Matthew 26:59</a>; Mark 14:55; Luke 22:66), and the same body condemned Stephen (<a class=\"ref\" data-ref=\"Acts 6:12\">Acts 6:12</a>) and repeatedly interrogated Peter, John, and Paul (<a class=\"ref\" data-ref=\"Acts 4:5\">Acts 4:5</a>; 5:27; 22:30). Paul's strategic use of the Pharisee-Sadducee division over resurrection — \"Brothers, I am a Pharisee\" — split the council against itself and required Roman soldiers to rescue him (<a class=\"ref\" data-ref=\"Acts 23:6\">Acts 23:6–10</a>). After the destruction of Jerusalem in AD 70, the Sanhedrin reconstituted itself at Yavneh and later Tiberias as a purely religious body, eventually dissolving in late antiquity.</p>",
        "sections": [],
        "hitchcock_meaning": "sitting together",
        "source_ids": {"easton": None, "smith": "sanhedrin", "isbe": "sanhedrin"},
        "key_refs": ["Numbers 11:16", "Matthew 26:59", "Acts 4:5", "Acts 23:6"]
    },
    "shalmaneser": {
        "id": "shalmaneser",
        "term": "Shalmaneser",
        "category": "people",
        "intro": "<p>Shalmaneser was the name of several Assyrian kings, of whom two are relevant to biblical history. Shalmaneser III (reigned 858–824 BC) is not named in the Hebrew Bible but appears in Assyrian records connected with Israelite kings: the Black Obelisk of Shalmaneser III depicts Jehu of Israel — or his envoy — bowing to pay tribute, the earliest known visual representation of an Israelite king. Shalmaneser V (reigned 727–722 BC), however, is the king most prominently associated with the fall of the northern kingdom of Israel and is directly named in Scripture.</p><p>When Hoshea, the last king of Israel, stopped paying tribute to Assyria and sought Egyptian support, Shalmaneser V invaded Palestine, captured Hoshea, and placed him in prison (<a class=\"ref\" data-ref=\"2 Kings 17:3\">2 Kings 17:3–4</a>). He then laid siege to the capital Samaria, a siege that lasted three years (<a class=\"ref\" data-ref=\"2 Kings 17:5\">2 Kings 17:5</a>). Assyrian annals credit the final capture of Samaria to Sargon II, who may have succeeded to the throne during the siege, but Shalmaneser V's campaign initiated the process that ended the northern kingdom and led to the deportation of the ten tribes — an event of permanent theological significance in the prophetic interpretation of Israel's history and the mystery of the \"lost tribes.\"</p>",
        "sections": [],
        "hitchcock_meaning": "peace; tied; chained; perfection; retribution",
        "source_ids": {"easton": None, "smith": "shalmaneser", "isbe": "shalmaneser"},
        "key_refs": ["2 Kings 17:3", "2 Kings 17:5", "2 Kings 18:9"]
    },
    "shinar": {
        "id": "shinar",
        "term": "Shinar",
        "category": "places",
        "intro": "<p>Shinar was the ancient name for the great alluvial plain of lower Mesopotamia through which the Tigris and Euphrates pass before reaching the sea — the region later known as Babylonia or Chaldea. The land is characterized in Genesis as a flat plain where brick replaced quarried stone and bitumen replaced mortar, conditions accurately describing the geology of the Mesopotamian floodplain. Among its cities were Babel (Babylon), Erech (Uruk), Accad (Akkad), and Calneh (<a class=\"ref\" data-ref=\"Genesis 10:10\">Genesis 10:10</a>). The territory thus encompasses the cradle of the world's earliest urban civilization.</p><p>Shinar appears at three pivotal moments in biblical history. It is the setting of the tower of Babel, where humanity gathered \"on the plain in the land of Shinar\" to build a city with a tower reaching to the heavens, resulting in the divine confusion of languages and the scattering of the nations (<a class=\"ref\" data-ref=\"Genesis 11:2\">Genesis 11:2–9</a>). It is the realm of Amraphel king of Shinar, one of the four kings who raided Canaan and captured Lot, prompting Abraham's rescue mission (<a class=\"ref\" data-ref=\"Genesis 14:1\">Genesis 14:1</a>). And Daniel places the beginning of Judah's exile in Shinar: Nebuchadnezzar brought the temple vessels \"to the land of Shinar, to the house of his god\" (<a class=\"ref\" data-ref=\"Daniel 1:2\">Daniel 1:2</a>). Isaiah prophesied a second exodus in which God would recover his scattered people \"from Shinar\" (<a class=\"ref\" data-ref=\"Isaiah 11:11\">Isaiah 11:11</a>).</p>",
        "sections": [],
        "hitchcock_meaning": "watch of him that sleeps",
        "source_ids": {"easton": None, "smith": "shinar", "isbe": "shinar"},
        "key_refs": ["Genesis 11:2", "Genesis 14:1", "Daniel 1:2", "Isaiah 11:11"]
    },
    "shishak": {
        "id": "shishak",
        "term": "Shishak",
        "category": "people",
        "intro": "<p>Shishak (identified with the Egyptian pharaoh Sheshonk I, first ruler of the Twenty-second or Bubastite Dynasty, reigned c. 945–924 BC) is the first Egyptian monarch whose name and actions can be directly correlated between the biblical text and Egyptian archaeological records, providing one of the earliest confirmed synchronisms of Egyptian and Israelite chronology. At the beginning of his reign Shishak gave asylum to the fugitive Jeroboam when Solomon sought to kill him (<a class=\"ref\" data-ref=\"1 Kings 11:40\">1 Kings 11:40</a>), positioning himself to influence the succession crisis in Israel.</p><p>In the fifth year of Rehoboam's reign (c. 925 BC), Shishak invaded Judah, captured the fortified cities, and advanced on Jerusalem. Rehoboam surrendered the treasures of the temple and the palace, including the gold shields Solomon had made, which Rehoboam replaced with bronze (<a class=\"ref\" data-ref=\"1 Kings 14:25\">1 Kings 14:25–26</a>; <a class=\"ref\" data-ref=\"2 Chronicles 12:2\">2 Chronicles 12:2–9</a>). The Egyptian record of this campaign survives on the walls of the temple of Amun at Karnak, where Sheshonk I listed more than 150 cities he claimed to have conquered in Canaan — including sites in both Judah and the northern kingdom — independently corroborating the biblical account and establishing Shishak as a significant synchronism between biblical and Egyptian history.</p>",
        "sections": [],
        "hitchcock_meaning": "present of the bag; of the pot; of the thigh",
        "source_ids": {"easton": None, "smith": "shishak", "isbe": "shishak"},
        "key_refs": ["1 Kings 11:40", "1 Kings 14:25", "2 Chronicles 12:2"]
    },
    "silvanus": {
        "id": "silvanus",
        "term": "Silvanus",
        "category": "people",
        "intro": "<p>Silvanus is the Roman literary name for Silas, the prominent early Christian leader who served as Paul's missionary companion on his second journey and co-author of several Pauline letters. In Acts he is consistently called Silas; in the epistles he appears as Silvanus (<a class=\"ref\" data-ref=\"2 Corinthians 1:19\">2 Corinthians 1:19</a>; <a class=\"ref\" data-ref=\"1 Thessalonians 1:1\">1 Thessalonians 1:1</a>; <a class=\"ref\" data-ref=\"2 Thessalonians 1:1\">2 Thessalonians 1:1</a>). This dual naming reflects his status as a Jew with Roman citizenship who operated comfortably in both Jewish and Roman cultural registers. He is introduced as one of the \"leading men among the brothers\" of the Jerusalem church, sent with Paul and Barnabas to deliver the council decree to Antioch (<a class=\"ref\" data-ref=\"Acts 15:22\">Acts 15:22</a>).</p><p>After Paul and Barnabas separated over Mark, Silas became Paul's new missionary partner. Together they revisited churches in Syria and Cilicia, preached in Philippi (where both were imprisoned and miraculously freed, <a class=\"ref\" data-ref=\"Acts 16:25\">Acts 16:25–34</a>), worked in Thessalonica, Berea, and Corinth. His mention as co-author of the Thessalonian letters (written from Corinth, c. AD 50) confirms his full participation in Paul's apostolic work. Peter's statement in 1 Peter 5:12 — \"By Silvanus, a faithful brother as I regard him, I have written briefly to you\" — suggests he also served the Petrine circle as amanuensis or editorial agent, indicating a ministry spanning both apostolic traditions.</p>",
        "sections": [],
        "hitchcock_meaning": "who loves the forest",
        "source_ids": {"easton": None, "smith": "silvanus", "isbe": "silvanus"},
        "key_refs": ["Acts 15:22", "Acts 15:40", "1 Thessalonians 1:1", "1 Peter 5:12"]
    },
    "tiberius": {
        "id": "tiberius",
        "term": "Tiberius",
        "category": "people",
        "intro": "<p>Tiberius (full name Tiberius Claudius Nero Caesar Augustus, reigned AD 14–37) was the second Roman emperor and stepson of Augustus, under whose rule virtually the entire public ministry of Jesus and the early expansion of the church in Judea took place. He is mentioned by name in <a class=\"ref\" data-ref=\"Luke 3:1\">Luke 3:1</a> — \"In the fifteenth year of the reign of Tiberius Caesar, Pontius Pilate being governor of Judea\" — the famous synchronism that anchors the beginning of John the Baptist's ministry (and the Gospel narrative) in Roman historical chronology, corresponding to approximately AD 28–29. Every reference to \"Caesar\" in the Gospels and Acts implies Tiberius or his successors.</p><p>Tiberius was born on 18 November 42 BC and had a distinguished military career before succeeding Augustus. His reign became increasingly overshadowed by the influence of his Praetorian prefect Sejanus, whose fall in AD 31 may have affected Roman policy toward the Jews in Judea. Pontius Pilate, who presided at Jesus' trial, was a Tiberian appointee, serving in Judea from AD 26 to 36. The denarius with Caesar's image shown to Jesus in the question about taxes — \"Render to Caesar the things that are Caesar's\" (<a class=\"ref\" data-ref=\"Matthew 22:21\">Matthew 22:21</a>) — would have borne the image of Tiberius. He died at Misenum on 16 March AD 37, less than two years before Paul's conversion on the Damascus road.</p>",
        "sections": [],
        "hitchcock_meaning": "the son of Tiber",
        "source_ids": {"easton": None, "smith": "tiberius", "isbe": "tiberius"},
        "key_refs": ["Luke 3:1", "Matthew 22:21"]
    },
    "tiglathpileser": {
        "id": "tiglathpileser",
        "term": "Tiglath-pileser",
        "category": "people",
        "intro": "<p>Tiglath-pileser III (reigned 745–727 BC), also referred to in Scripture as Tilgath-pilneser (<a class=\"ref\" data-ref=\"1 Chronicles 5:26\">1 Chronicles 5:26</a>; 2 Chronicles 28:20), was one of the most militarily capable kings of the Neo-Assyrian Empire and the second Assyrian ruler to come into direct conflict with Israel. He reorganized the Assyrian imperial administration and replaced the older policy of tribute collection with direct annexation, making conquest more permanent and the Assyrian grip on conquered territories far more thorough than that of his predecessors.</p><p>When Pekah king of Israel withheld tribute, Tiglath-pileser invaded the northern territories (c. 733–732 BC), taking Ijon, Abel-beth-maachah, Janoah, Kedesh, Hazor, Gilead, Galilee, and all the land of Naphtali, and carrying their populations captive to Assyria (<a class=\"ref\" data-ref=\"2 Kings 15:29\">2 Kings 15:29</a>) — the first phase of the deportation of the northern tribes. Ahaz of Judah then appealed to Tiglath-pileser for help against the Syro-Ephraimite coalition threatening Jerusalem (<a class=\"ref\" data-ref=\"2 Kings 16:7\">2 Kings 16:7</a>; Isaiah 7), effectively making Judah an Assyrian vassal and ignoring Isaiah's counsel to trust in the LORD. Tiglath-pileser responded by capturing Damascus and deporting the Aramaeans (<a class=\"ref\" data-ref=\"2 Kings 16:9\">2 Kings 16:9</a>), completing the destruction of Israel's northern alliance. His successors Shalmaneser V and Sargon II finished the conquest he had begun.</p>",
        "sections": [],
        "hitchcock_meaning": "that binds or takes away captivity",
        "source_ids": {"easton": None, "smith": "tiglathpileser", "isbe": None},
        "key_refs": ["2 Kings 15:29", "2 Kings 16:7", "2 Kings 16:9", "1 Chronicles 5:26"]
    },
    "tirzah": {
        "id": "tirzah",
        "term": "Tirzah",
        "category": "places",
        "intro": "<p>Tirzah (meaning <em>benevolent</em>, <em>complaisant</em>, or <em>pleasing</em>) was a Canaanite royal city and later the first capital of the northern kingdom of Israel. Joshua defeated its king during the conquest (<a class=\"ref\" data-ref=\"Joshua 12:24\">Joshua 12:24</a>), and Tirzah subsequently became the seat of Israelite kings from Jeroboam through the early reign of Omri. Jeroboam's home was at Tirzah (<a class=\"ref\" data-ref=\"1 Kings 14:17\">1 Kings 14:17</a>), Baasha reigned and died there (1 Kings 15:21, 33), and it was at Tirzah that the usurper Zimri made his brief seven-day bid for the throne before Omri besieged the city. Omri then ruled from Tirzah six years before moving the capital to the newly purchased hill of Samaria (<a class=\"ref\" data-ref=\"1 Kings 16:23\">1 Kings 16:23–24</a>). The site is identified with Tell el-Far'ah North, approximately seven miles northeast of Shechem.</p><p>The city retained sufficient beauty and fame to appear in the Song of Solomon: \"You are beautiful as Tirzah, my love, lovely as Jerusalem, awesome as an army with banners\" (<a class=\"ref\" data-ref=\"Song of Solomon 6:4\">Song of Solomon 6:4</a>). The same name was also borne by the youngest of the five daughters of Zelophehad, who brought a landmark inheritance case before Moses when their father died with no sons (<a class=\"ref\" data-ref=\"Numbers 26:33\">Numbers 26:33</a>; 27:1; 36:11; Joshua 17:3). The daughters' successful petition established daughters' rights of inheritance in the absence of male heirs — a ruling the LORD confirmed and incorporated into Israelite law.</p>",
        "sections": [],
        "hitchcock_meaning": "benevolent; complaisant; pleasing",
        "source_ids": {"easton": None, "smith": "tirzah", "isbe": "tirzah"},
        "key_refs": ["Joshua 12:24", "1 Kings 14:17", "Song of Solomon 6:4", "Numbers 26:33"]
    },
    "tryphosa": {
        "id": "tryphosa",
        "term": "Tryphosa",
        "category": "people",
        "intro": "<p>Tryphosa (meaning <em>thrice shining</em> or <em>delicate</em>) was a Christian woman at Rome whom Paul commended together with her companion Tryphaena in his letter to the Romans: \"Greet those workers in the Lord, Tryphaena and Tryphosa\" (<a class=\"ref\" data-ref=\"Romans 16:12\">Romans 16:12</a>). The Greek word translated \"workers\" (<em>kopiosai</em>) is the same term Paul applies to himself and other apostolic laborers (1 Corinthians 15:10; Galatians 4:11; Philippians 2:16), indicating that Tryphaena and Tryphosa were engaged in substantive, recognized ministry — not merely social support. The similarity of their names suggests they may have been sisters, perhaps twins.</p><p>Beyond this single verse, nothing further is known of Tryphosa from Scripture or from confirmed historical records. Her name appears in Roman epigraphic evidence and was not uncommon in the Hellenistic world. The pattern of Romans 16 — in which Paul greets more than two dozen individuals by name, including Phoebe, Prisca, Mary, Junia, and Persis alongside Tryphosa and Tryphaena — reflects the significant and diverse contribution of women to the early Roman church's ministry and leadership. Tryphosa's inclusion in this carefully composed list marks her as a known and honored worker in the apostolic network, whose faithful labor in Rome was remembered and commended by Paul across the distance of his Mediterranean mission.</p>",
        "sections": [],
        "hitchcock_meaning": "thrice shining",
        "source_ids": {"easton": None, "smith": "tryphosa", "isbe": "tryphosa"},
        "key_refs": ["Romans 16:12"]
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
