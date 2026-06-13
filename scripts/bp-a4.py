"""
BP Article Synthesis — a4: Anamim → Areopagus
Covers Easton entries: Anamim through Areopagus (75 entries)

Sources consulted:
  - data/dictionary/index.json (Easton briefs)
  - data/dictionary/{slug}.json (Easton full HTML + refs, per entry)
  - data/smith/index.json (Smith briefs)
  - data/isbe/index.json (ISBE briefs)
  - data/hitchcock/index.json (name meanings)

Category logic applied:
  - people:   biblical persons and tribal groups
  - places:   cities, regions, geographic features
  - concepts: theological terms, objects, practices, roles
  - events:   battles, feasts, historical events

Script: scripts/bp-a4.py
Run: python3 scripts/bp-a4.py
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
    "anamim": {
        "id": "anamim",
        "term": "Anamim",
        "category": "people",
        "intro": "<p>Anamim, whose name is thought to mean <em>a fountain</em> or <em>affliction</em>, is listed in the Table of Nations as a tribal people descended from Mizraim, son of Ham (Gen. 10:13; 1 Chr. 1:11). The name designates one of several Mizraite groups that settled in the region of Egypt and northeastern Africa in the generations following the dispersion at Babel. Beyond the two genealogical notices, Scripture offers no further historical detail about this people.</p><p>Ancient sources and modern scholarship have not reached consensus on the precise location of the Anamim, though they are grouped with other Mizraite peoples such as the Ludim, Lehabim, and Naphtuhim. Their appearance in both Genesis and Chronicles reflects the biblical concern to trace all nations back to the sons of Noah, underscoring the common origin of humanity within the framework of covenant history.</p>",
        "hitchcock_meaning": "a fountain; answer; affliction",
        "source_ids": {"easton": "anamim", "smith": "anamim", "isbe": "anamim"},
        "key_refs": ["Genesis 10:13", "1 Chronicles 1:11"],
        "sections": []
    },
    "anammelech": {
        "id": "anammelech",
        "term": "Anammelech",
        "category": "concepts",
        "intro": "<p>Anammelech was a Babylonian deity worshipped by the Sepharvite colonists whom the Assyrian king settled in Samaria after the fall of the northern kingdom of Israel (2 Kings 17:31). The name is interpreted as <em>Anu is the prince</em>, connecting it to Anu, the Babylonian sky-god. Children were burned in fire as sacrifices to this god alongside Adrammelech, reflecting the syncretistic and deeply foreign religious practices imported into the land.</p><p>The mention of Anammelech illustrates the theological crisis that the author of Kings identifies as the cause of Israel&#39;s exile: the people served gods of the nations rather than Yahweh alone. The cult of Anammelech represents one of several pagan imports that corrupted the religious life of Samaria during the period of Assyrian domination, a situation the text presents as a direct fulfillment of covenant warnings against idolatry.</p>",
        "hitchcock_meaning": "answer; poverty of the king",
        "source_ids": {"easton": "anammelech", "smith": "anammelech", "isbe": "anammelech"},
        "key_refs": ["2 Kings 17:31"],
        "sections": []
    },
    "anan": {
        "id": "anan",
        "term": "Anan",
        "category": "people",
        "intro": "<p>Anan, meaning <em>cloud</em>, was one of the leaders of the people who set his seal to the solemn covenant of national renewal recorded in Nehemiah 10 (Neh. 10:26). This covenant, made under the leadership of Nehemiah and Ezra following the return from Babylonian exile, committed the community to faithful observance of the law of Moses, including prohibitions on foreign marriages, Sabbath commerce, and neglect of the temple.</p><p>Anan is listed among the heads of the people who signed alongside priests and Levites, indicating his standing within the restored community of Judah. Though no further biographical details are given, his participation in this covenant ceremony places him within the circle of lay leaders who helped reconstitute Israel&#39;s religious and social life in the post-exilic period.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "anan", "smith": "anan", "isbe": "anan"},
        "key_refs": ["Nehemiah 10:26"],
        "sections": []
    },
    "ananiah": {
        "id": "ananiah",
        "term": "Ananiah",
        "category": "places",
        "intro": "<p>Ananiah, meaning <em>protected by Jehovah</em>, is a town in the tribe of Benjamin listed among the settlements reoccupied by Benjaminites after the return from Babylonian exile (Neh. 11:32). Its location between Nob and Hazor suggests it lay in the hill country north of Jerusalem, and it is generally identified with the modern site of Beit Hanina, northwest of the city.</p><p>The name Ananiah is also borne by an individual in the post-exilic period: a man described as the grandfather of Azariah, who assisted in repairing the wall of Jerusalem under Nehemiah (Neh. 3:23). Whether the personal name and the place name share a common origin or simply reflect the widespread use of theophoric names in Judah during this period cannot be determined from the biblical text alone.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ananiah", "smith": "ananiah", "isbe": "ananiah"},
        "key_refs": ["Nehemiah 11:32", "Nehemiah 3:23"],
        "sections": []
    },
    "ananias": {
        "id": "ananias",
        "term": "Ananias",
        "category": "people",
        "intro": "<p>Ananias, meaning <em>the cloud of the Lord</em> or <em>Jehovah is gracious</em>, is the name of three distinct individuals in the New Testament. The most prominent is Ananias of Jerusalem, who with his wife Sapphira conspired to deceive the apostles regarding the proceeds from a land sale, dying suddenly as a consequence (Acts 5:1&#8211;11). A second Ananias was the Damascus disciple sent by God to restore Paul&#39;s sight following the apostle&#39;s encounter with the risen Christ on the road to Damascus (Acts 9:10&#8211;19).</p><p>The third Ananias served as high priest in Jerusalem during Paul&#39;s trials before the Sanhedrin and the procurator Felix, commanding that Paul be struck on the mouth before the council (Acts 23:2; 24:1). The Josephus mentions his death during the Jewish revolt. Together, the three men of this name in Acts illustrate contrasting responses to the early Christian movement: deceptive resistance, faithful obedience, and hostile authority.</p>",
        "hitchcock_meaning": "the cloud of the Lord",
        "source_ids": {"easton": "ananias", "smith": "ananias"},
        "key_refs": ["Acts 5:5", "Acts 9:10", "Acts 23:2", "Acts 24:1"],
        "sections": []
    },
    "anath": {
        "id": "anath",
        "term": "Anath",
        "category": "people",
        "intro": "<p>Anath, whose name means <em>answer</em> or is connected with a Canaanite war goddess of the same name, is known in Scripture solely as the father of Shamgar, one of the minor judges of Israel (Judg. 3:31; 5:6). Shamgar delivered Israel from Philistine oppression by striking down six hundred Philistines with an ox goad. The name Anath suggests possible Canaanite ancestry or cultural influence, raising questions scholars have noted about the ethnic background of this judge and his family.</p><p>Anath himself receives no biographical treatment in the biblical text; his significance is entirely derivative, defined by his son&#39;s exploit. Deborah&#39;s song references the period of Shamgar son of Anath as a time of great insecurity on the roads of Israel (Judg. 5:6), placing the family within the turbulent early period of the judges when tribal life was repeatedly disrupted by foreign threats.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "anath", "smith": "anath", "isbe": "anath"},
        "key_refs": ["Judges 3:31", "Judges 5:6"],
        "sections": []
    },
    "anathema": {
        "id": "anathema",
        "term": "Anathema",
        "category": "concepts",
        "intro": "<p>Anathema, from the Greek meaning <em>a thing set apart</em> or <em>devoted</em>, corresponds to the Hebrew <em>cherem</em>, the solemn dedication of persons or things to God, sometimes involving their destruction. In the Old Testament, items devoted to God under cherem could not be redeemed; they were either destroyed or transferred permanently to the sanctuary (Lev. 27:28&#8211;29; Num. 18:14). The term carried both the sense of sacred consecration and irrevocable judgment.</p><p>In the New Testament the word carries a primarily negative force: to pronounce something anathema is to declare it under divine curse and cut off from the community. Paul invokes this sense when he declares that anyone who preaches a different gospel should be anathema (Gal. 1:8&#8211;9), and when he describes his willingness to be accursed for the sake of his kinsmen (Rom. 9:3). The phrase <em>Anathema Maranatha</em> in 1 Corinthians 16:22 combines a curse with the Aramaic invocation of the Lord&#39;s coming.</p>",
        "hitchcock_meaning": "separated; set apart",
        "source_ids": {"easton": "anathema", "smith": "anathema", "isbe": "anathema"},
        "key_refs": ["Leviticus 27:28", "Galatians 1:8", "Romans 9:3", "1 Corinthians 16:22"],
        "sections": []
    },
    "anathoth": {
        "id": "anathoth",
        "term": "Anathoth",
        "category": "places",
        "intro": "<p>Anathoth, meaning <em>answers to prayer</em>, was a priestly city in the territory of Benjamin assigned to the Levites (Josh. 21:18), located about three miles northeast of Jerusalem. It served as a city of refuge and was the hometown of the prophet Jeremiah, whose ministry was marked by his own townspeople&#39;s hostility and a plot against his life (Jer. 1:1; 11:21). Several of David&#39;s mighty men also came from Anathoth, including Abiezer and Jehu (2 Sam. 23:27; 1 Chr. 12:3).</p><p>The city features in the narrative of Solomon&#39;s early reign, when the king exiled the priest Abiathar to Anathoth following his support of Adonijah&#39;s attempted usurpation (1 Kings 2:26). Jeremiah&#39;s famous purchase of a field in Anathoth during the Babylonian siege became a prophetic sign of future restoration, affirming that houses, fields, and vineyards would again be bought in the land (Jer. 32:7&#8211;9).</p>",
        "hitchcock_meaning": "answer; song; poverty",
        "source_ids": {"easton": "anathoth", "smith": "anathoth", "isbe": "anathoth"},
        "key_refs": ["Joshua 21:18", "Jeremiah 1:1", "Jeremiah 11:21", "Jeremiah 32:7", "1 Kings 2:26"],
        "sections": []
    },
    "anchor": {
        "id": "anchor",
        "term": "Anchor",
        "category": "concepts",
        "intro": "<p>Anchors in the ancient Mediterranean world were heavy objects, typically made of stone or iron, used to hold ships in place. The account of Paul&#39;s shipwreck in Acts 27 provides the most detailed biblical description of their use: the crew cast four anchors from the stern to prevent the vessel from being driven onto the rocks, and later cut them loose before attempting to beach the ship (Acts 27:29&#8211;40). Roman ships commonly carried multiple anchors of different sizes for use in varying conditions.</p><p>The anchor carries significant theological weight in the New Testament through its metaphorical use in Hebrews 6:19, where the believer&#39;s hope in God&#39;s promises is described as &#8220;an anchor for the soul, sure and steadfast.&#8221; This image, drawn from everyday maritime life, became one of the earliest Christian symbols, appearing prominently in catacombs and early church art as a sign of hope and steadfast faith in Christ.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "anchor", "smith": "anchor"},
        "key_refs": ["Acts 27:29", "Acts 27:40", "Hebrews 6:19"],
        "sections": []
    },
    "ancient-of-days": {
        "id": "ancient-of-days",
        "term": "Ancient of Days",
        "category": "concepts",
        "intro": "<p>Ancient of Days is a divine title appearing three times in Daniel&#39;s vision of the heavenly throne room (Dan. 7:9, 13, 22). The Aramaic expression conveys the eternity and supreme authority of God, depicted as an aged figure whose garment is white as snow and whose hair is like pure wool, seated on a throne of flames with wheels of burning fire. Before him a river of fire flows, and ten thousand times ten thousand stand in attendance as the heavenly court opens its books of judgment.</p><p>The vision depicts the Ancient of Days delivering judgment against the four great beasts representing successive world empires, and granting everlasting dominion to &#8220;one like a son of man&#8221; who comes on the clouds of heaven (Dan. 7:13&#8211;14). Jesus applied this son-of-man imagery to himself during his trial before the Sanhedrin (Matt. 26:64), making Daniel&#39;s vision central to New Testament Christology and eschatology. The title emphasizes that history moves under divine sovereignty toward a predetermined conclusion.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ancient-of-days", "isbe": "ancient-of-days"},
        "key_refs": ["Daniel 7:9", "Daniel 7:13", "Daniel 7:22"],
        "sections": []
    },
    "andrew": {
        "id": "andrew",
        "term": "Andrew",
        "category": "people",
        "intro": "<p>Andrew, whose name means <em>manly</em> or <em>strong man</em>, was one of the twelve apostles of Jesus and the brother of Simon Peter. A native of Bethsaida in Galilee and a fisherman by trade, he was among the earliest followers of John the Baptist before transferring his allegiance to Jesus after John identified him as the Lamb of God (John 1:35&#8211;40). Andrew then brought his brother Peter to Jesus, making him the first missionary in the Gospel of John.</p><p>Called by Jesus from his nets on the Sea of Galilee to become a fisher of men (Matt. 4:18&#8211;19), Andrew appears in several notable Gospel episodes: he brings the boy with five loaves and two fish to Jesus before the feeding of the five thousand (John 6:8&#8211;9), and he relays the request of certain Greeks who seek an audience with Jesus (John 12:22). In Acts he is listed among the apostles present in the upper room after the ascension. Church tradition holds that he preached in Scythia and Greece and was martyred on an X-shaped cross at Patras.</p>",
        "hitchcock_meaning": "a strong man",
        "source_ids": {"easton": "andrew", "smith": "andrew", "isbe": "andrew"},
        "key_refs": ["John 1:40", "Matthew 4:18", "John 6:8", "John 12:22"],
        "sections": []
    },
    "andronicus": {
        "id": "andronicus",
        "term": "Andronicus",
        "category": "people",
        "intro": "<p>Andronicus, a name meaning <em>man-conquering</em>, is greeted by Paul in Romans 16:7 as a Jewish Christian who was his kinsman and had shared his imprisonment. Paul describes him and Junia as &#8220;outstanding among the apostles&#8221; who were in Christ before him, indicating they were among the earliest converts to the faith, possibly from the Jerusalem community. The precise meaning of &#8220;of note among the apostles&#8221; has been debated, with some interpreters understanding it to mean they were themselves notable apostles and others that they were well-regarded by the apostles.</p><p>A second Andronicus appears in 2 Maccabees as a deputy of Antiochus Epiphanes who committed murder at the king&#39;s behest, though this figure has no connection to the Christian named by Paul. The Andronicus of Romans represents the kind of early Jewish believer whose conversion predated Paul&#39;s own, reminding readers of the deep Jewish roots of the church at Rome.</p>",
        "hitchcock_meaning": "a man excelling others",
        "source_ids": {"easton": "andronicus", "smith": "andronicus", "isbe": "andronicus"},
        "key_refs": ["Romans 16:7"],
        "sections": []
    },
    "anem": {
        "id": "anem",
        "term": "Anem",
        "category": "places",
        "intro": "<p>Anem, meaning <em>two springs</em>, was a Levitical city in the territory of Issachar assigned to the Gershonite clan of the Levites (1 Chr. 6:73). It is generally identified with En-gannim of Joshua 19:21 and 21:29, a town on the southwestern border of Issachar near the Valley of Jezreel. The alternate form of the name reflects a common pattern in which the same site appears under slightly different designations in different biblical lists.</p><p>En-gannim, meaning &#8220;spring of gardens,&#8221; suggests a well-watered location, consistent with the fertile terrain of the Jezreel Valley region. Levitical cities like Anem served as residential and administrative centers for the tribe of Levi, which received no territorial allotment but was distributed throughout Israel to provide religious instruction and priestly service to the other tribes.</p>",
        "hitchcock_meaning": "or Anen, an answer; their affliction",
        "source_ids": {"easton": "anem", "smith": "anem", "isbe": "anem"},
        "key_refs": ["1 Chronicles 6:73", "Joshua 19:21"],
        "sections": []
    },
    "aner": {
        "id": "aner",
        "term": "Aner",
        "category": "people",
        "intro": "<p>Aner, whose name may mean <em>a boy</em> or <em>affliction</em>, appears in two distinct contexts in Scripture. The first and more prominent is a Canaanite chieftain and ally of Abraham who joined the pursuit of Chedorlaomer along with his brothers Mamre and Eshcol after the kings of the east carried away Lot and the inhabitants of Sodom (Gen. 14:13, 24). Abraham refused to take any plunder from the recovered spoil for himself, though he acknowledged that Aner and his companions were entitled to their share.</p><p>A second Aner is a Levitical city on the west bank of the Jordan in the territory of Manasseh, assigned to the Kohathite Levites (1 Chr. 6:70). It may correspond to Taanach, which appears in the parallel list in Joshua 21:25. The name thus designates both a historical ally of the patriarchal period and a geographic site in the later tribal settlement of Canaan.</p>",
        "hitchcock_meaning": "answer; song; affliction",
        "source_ids": {"easton": "aner", "smith": "aner"},
        "key_refs": ["Genesis 14:13", "Genesis 14:24", "1 Chronicles 6:70"],
        "sections": []
    },
    "angel": {
        "id": "angel",
        "term": "Angel",
        "category": "concepts",
        "intro": "<p>Angel derives from both the Hebrew <em>mal&#39;akh</em> and the Greek <em>angelos</em>, both meaning <em>messenger</em>. The term is applied in Scripture to human messengers (Luke 7:24), to the prophets as God&#39;s spokesmen (Hag. 1:13; Mal. 3:1), and preeminently to the heavenly beings who serve as God&#39;s agents in carrying out his will. Angels are described as a vast host arranged in orders of authority, including cherubim, seraphim, and archangels, who worship God, deliver divine messages, protect God&#39;s people, and execute judgment on his enemies.</p><p>The Angel of the Lord occupies a distinctive role in the Old Testament, often appearing as a theophanic representative of God himself, speaking in the first person as Yahweh (Gen. 22:11&#8211;12; Exod. 3:2&#8211;4). In the New Testament angels announce the birth and resurrection of Jesus, minister to him after the temptation, and figure prominently in the eschatological events of Revelation. The epistle to the Hebrews argues that Christ is superior to angels, who are &#8220;ministering spirits sent out to serve for the sake of those who are to inherit salvation&#8221; (Heb. 1:14).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "angel", "isbe": "angel"},
        "key_refs": ["Hebrews 1:14", "Luke 7:24", "Revelation 5:11", "Genesis 22:11"],
        "sections": []
    },
    "anger": {
        "id": "anger",
        "term": "Anger",
        "category": "concepts",
        "intro": "<p>Anger in Scripture is treated both as a natural human emotion and as a moral quality requiring careful governance. The Old Testament uses several Hebrew words for anger, most commonly <em>aph</em> (nostril, face) and <em>chemah</em> (heat), reflecting the physical experience of the emotion. Human anger is not universally condemned; Moses, Nehemiah, and Jesus all exhibit righteous anger in the face of injustice and profanation. The psalms and wisdom literature, however, repeatedly warn against hasty anger and its destructive consequences (Prov. 14:17; 15:18; 29:22).</p><p>The anger of God occupies substantial space in both Testaments. Divine wrath is consistently portrayed as a response to idolatry, injustice, and covenant violation rather than as arbitrary passion; it is always tempered by God&#39;s commitment to mercy. The New Testament continues this pattern while emphasizing that human anger must be swift to subside: &#8220;Be angry and do not sin; do not let the sun go down on your anger&#8221; (Eph. 4:26). Paul includes wrath among the vices to be put off in favor of the character of the new humanity in Christ (Col. 3:8).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "anger", "isbe": "anger"},
        "key_refs": ["Ephesians 4:26", "Colossians 3:8", "Psalms 7:11", "Matthew 5:22"],
        "sections": []
    },
    "anim": {
        "id": "anim",
        "term": "Anim",
        "category": "places",
        "intro": "<p>Anim, meaning <em>fountains</em> or <em>springs</em>, was a city in the hill country of Judah listed in the tribal allotment of Joshua (Josh. 15:50). It appears alongside Eshtemoh and Goshen in the southern hill-country district, and is generally identified with the modern site of Khirbet Ghuwein el-Tahta, approximately ten miles southwest of Hebron.</p><p>The name reflects the common practice in ancient Palestine of identifying settlements by their water sources, a critical geographical feature in an arid region where reliable springs determined habitation patterns. Anim is not mentioned again after its appearance in the Judahite city list, suggesting it was a relatively minor settlement in the highland zone. Its inclusion in the biblical record nonetheless attests to the systematic nature of the tribal territorial descriptions preserved in Joshua 15.</p>",
        "hitchcock_meaning": "answerings; singings; afflicted",
        "source_ids": {"easton": "anim", "smith": "anim", "isbe": "anim"},
        "key_refs": ["Joshua 15:50"],
        "sections": []
    },
    "animal": {
        "id": "animal",
        "term": "Animal",
        "category": "concepts",
        "intro": "<p>The biblical treatment of animals reflects a theology in which the creature world is God&#39;s creation, placed under human stewardship. The Levitical law introduced a systematic division of animals into clean and unclean categories, governing which could be eaten (Lev. 11; Deut. 14) and which were suitable for sacrifice. Clean land animals must chew the cud and have divided hooves; clean water creatures must have fins and scales; clean birds are distinguished from a list of prohibited species including birds of prey. The reason for many distinctions remains debated, with interpretations ranging from hygiene to symbolic holiness.</p><p>Animals play varied roles throughout Scripture: as sacrificial offerings establishing atonement, as object lessons in wisdom literature (Prov. 6:6; 30:24&#8211;28), as symbols in prophetic visions, and as signs of divine provision and care. Noah&#39;s preservation of animals in the ark and God&#39;s covenant with &#8220;every living creature&#8221; after the flood (Gen. 9:10) demonstrate the scope of divine concern for the animal creation, a theme echoed in Jesus&#39; reference to God&#39;s care for sparrows (Matt. 10:29).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "animal"},
        "key_refs": ["Genesis 7:2", "Leviticus 11:1", "Deuteronomy 14:3", "Genesis 9:10"],
        "sections": []
    },
    "anise": {
        "id": "anise",
        "term": "Anise",
        "category": "concepts",
        "intro": "<p>Anise appears in Scripture only in Matthew 23:23, where Jesus rebukes the scribes and Pharisees for tithing mint, anise, and cummin while neglecting the weightier matters of the law&#8212;justice, mercy, and faithfulness. The Greek word <em>anethon</em> translated &#8220;anise&#8221; in the King James Version is more precisely identified as dill (<em>Anethum graveolens</em>), an aromatic annual herb cultivated across the ancient Near East for its seeds and leaves. True anise (<em>Pimpinella anisum</em>) was known in the ancient world but the Greek term points to dill.</p><p>The Pharisaic practice of tithing garden herbs, extending the tithe requirement even to small domestic plants, illustrated a scrupulous concern for the letter of the law in minute matters. Jesus did not condemn this precision in itself&#8212;&#8220;these you ought to have done&#8221;&#8212;but criticized the neglect of the moral and relational dimensions of Torah in favor of ritual exactness. The passage remains a key text in discussions of legal interpretation and the relationship between ritual observance and ethical living in Judaism and Christianity.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "anise", "smith": "anise"},
        "key_refs": ["Matthew 23:23"],
        "sections": []
    },
    "anna": {
        "id": "anna",
        "term": "Anna",
        "category": "people",
        "intro": "<p>Anna, meaning <em>grace</em>, was an aged prophetess of the tribe of Asher who was present at the Jerusalem temple when the infant Jesus was brought for his presentation (Luke 2:36&#8211;38). The daughter of Phanuel, she had been widowed after seven years of marriage and had since devoted herself to the temple, fasting and praying night and day. At the moment of Jesus&#39; presentation she gave thanks to God and spoke of the child &#8220;to all who were waiting for the redemption of Jerusalem,&#8221; making her one of the earliest human witnesses to the Messiah.</p><p>Anna is grouped with the prophetesses of the Old Testament&#8212;Miriam, Deborah, and Huldah&#8212;as a woman recognized for her prophetic gift. Her great age (she was either eighty-four years old or had been a widow for eighty-four years, the text admits both readings) and her ceaseless temple ministry make her a model of patient, prayer-centered expectation. Her brief appearance in Luke&#39;s infancy narrative pairs with Simeon&#39;s canticle to provide both male and female witness to the identity of the child as the fulfillment of Israel&#39;s hope.</p>",
        "hitchcock_meaning": "gracious; one who gives",
        "source_ids": {"easton": "anna", "smith": "anna", "isbe": "anna"},
        "key_refs": ["Luke 2:36", "Luke 2:37", "Luke 2:38"],
        "sections": []
    },
    "annas": {
        "id": "annas",
        "term": "Annas",
        "category": "people",
        "intro": "<p>Annas, whose name means <em>one who answers</em> or <em>humble</em>, served as high priest of Israel from approximately A.D. 6 to 15, when he was deposed by the Roman prefect Valerius Gratus. Despite his removal from office, Annas retained enormous personal authority and is described in Luke 3:2 as sharing the high priesthood alongside his son-in-law Caiaphas during the ministry of John the Baptist&#8212;a reflection of his continued political and religious influence.</p><p>Following Jesus&#39; arrest in Gethsemane, he was first brought before Annas for a preliminary examination before being sent to Caiaphas for the formal trial before the Sanhedrin (John 18:13, 19&#8211;24). Annas also appears among the ruling authorities who interrogated Peter and John after the healing of the lame man at the temple gate (Acts 4:6). Five of Annas&#39;s sons and his son-in-law Caiaphas served as high priests during the first century, making him the patriarch of the most powerful priestly family in Jerusalem during the period of the Second Temple.</p>",
        "hitchcock_meaning": "one who answers; humble",
        "source_ids": {"easton": "annas", "smith": "annas", "isbe": "annas"},
        "key_refs": ["John 18:13", "Luke 3:2", "Acts 4:6", "John 18:19"],
        "sections": []
    },
    "anoint": {
        "id": "anoint",
        "term": "Anoint",
        "category": "concepts",
        "intro": "<p>Anointing with oil was a widespread practice among the Hebrews, carrying both ordinary and sacred significance. In everyday life, anointing the body with olive oil was a common act of hygiene and hospitality, and its absence could signal mourning or distress (2 Sam. 12:20; Matt. 6:17). The ritual anointing of objects and persons with specially prepared sacred oil was prescribed in the Mosaic law for the consecration of the tabernacle, its furnishings, and the priests who served within it (Exod. 30:26&#8211;29; Lev. 8:10&#8211;12).</p><p>Kings, priests, and occasionally prophets were anointed to mark their divine appointment to office, establishing the Hebrew title <em>mashiach</em> (anointed one) as the designation of the divinely commissioned ruler. The Greek equivalent, <em>christos</em>, became the title of Jesus of Nazareth, who was understood by his followers to be the ultimate fulfillment of the anointed offices of prophet, priest, and king. The New Testament describes Jesus being anointed by the Holy Spirit at his baptism (Acts 10:38) and by a woman at Bethany in anticipation of his burial (Mark 14:3&#8211;9).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "anoint"},
        "key_refs": ["Exodus 30:26", "Leviticus 8:10", "Acts 10:38", "Mark 14:3"],
        "sections": []
    },
    "ant": {
        "id": "ant",
        "term": "Ant",
        "category": "concepts",
        "intro": "<p>The ant is mentioned in Scripture twice, both times in the book of Proverbs as an example of industrious wisdom (Prov. 6:6; 30:25). The Hebrew <em>nemalah</em>, related to a root meaning to cut off or to creep, refers to the common ant species of Palestine. Proverbs 6:6&#8211;8 commends the ant to the sluggard as a model: though it has no commander or ruler, it prepares its food in summer and gathers its harvest in autumn&#8212;a picture of self-directed diligence. Proverbs 30:25 lists the ant among four creatures that are small yet exceedingly wise.</p><p>The zoological accuracy of the observation has been noted by modern naturalists: Palestinian harvester ants (<em>Messor semirufus</em>) do indeed collect and store grain during the harvest season. In the ancient Near East and later rabbinic tradition, the ant served as a standard illustration of foresight and industry. Its appearance in the wisdom literature reflects the broader biblical principle that attentiveness to the natural order yields moral and practical insight.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ant", "smith": "ant", "isbe": "ant"},
        "key_refs": ["Proverbs 6:6", "Proverbs 30:25"],
        "sections": []
    },
    "antichrist": {
        "id": "antichrist",
        "term": "Antichrist",
        "category": "concepts",
        "intro": "<p>Antichrist, meaning <em>against Christ</em> or <em>in place of Christ</em>, is a term used exclusively by the apostle John in his epistles (1 John 2:18, 22; 4:3; 2 John 7). John identifies the antichrist as one who denies that Jesus is the Christ and denies the Father and the Son, placing the term firmly in the context of false teaching and apostasy within the Christian community rather than geopolitical power alone. Notably, John speaks of &#8220;many antichrists&#8221; already present in his day, indicating that the spirit of antichrist was an active force in the first-century church.</p><p>The concept is related to, though not identical with, the &#8220;man of lawlessness&#8221; described by Paul (2 Thess. 2:3&#8211;4) and the beast of Revelation 13. Interpreters have proposed a wide range of identifications across history, from specific historical rulers to institutional entities to a final eschatological figure. Across the varying interpretive traditions, the antichrist represents the ultimate human embodiment of opposition to Christ and his rule, whose appearance precedes and is overcome by the return of the Lord.</p>",
        "hitchcock_meaning": "an adversary to Christ",
        "source_ids": {"easton": "antichrist", "smith": "antichrist", "isbe": "antichrist"},
        "key_refs": ["1 John 2:18", "1 John 2:22", "2 Thessalonians 2:3", "Revelation 13:1"],
        "sections": []
    },
    "antioch": {
        "id": "antioch",
        "term": "Antioch",
        "category": "places",
        "intro": "<p>Two cities named Antioch appear in the New Testament. Antioch of Syria, the more prominent, was built on the Orontes River about sixteen miles from the Mediterranean coast and three hundred miles north of Jerusalem. Founded by Seleucus I around 300 B.C. and named for his father Antiochus, it grew to become the third largest city of the Roman Empire after Rome and Alexandria. It was here that followers of Jesus were first called Christians (Acts 11:26), making it the birthplace of the Christian name and the strategic base from which Paul launched all three of his missionary journeys.</p><p>Antioch of Pisidia, in Asia Minor, was a Roman colony in the province of Galatia. Paul and Barnabas visited it on the first missionary journey, preaching in the synagogue with significant initial success before being expelled by Jewish opposition (Acts 13:14&#8211;52). This Antioch appears again in Acts 14:19&#8211;21 and in Paul&#39;s account of his sufferings in 2 Timothy 3:11. Both cities illustrate the urban strategy of early Christian mission, targeting population centers with established Jewish communities as initial points of contact.</p>",
        "hitchcock_meaning": "speedy as a chariot",
        "source_ids": {"easton": "antioch", "smith": "antioch"},
        "key_refs": ["Acts 11:26", "Acts 13:14", "Acts 14:19", "Acts 11:19"],
        "sections": []
    },
    "antiochus": {
        "id": "antiochus",
        "term": "Antiochus",
        "category": "people",
        "intro": "<p>Antiochus was the name of several Seleucid kings of Syria whose reigns intersected with the history of the Jewish people between approximately 280 and 65 B.C. The most significant for biblical history is Antiochus IV Epiphanes (175&#8211;163 B.C.), whose brutal suppression of Jewish religion and desecration of the Jerusalem temple in 167 B.C.&#8212;sacrificing pigs on the altar and installing the &#8220;abomination of desolation&#8221;&#8212;sparked the Maccabean revolt. His campaigns are described in detail in 1 and 2 Maccabees, and his rise and fall are prophesied in Daniel 11.</p><p>Antiochus III the Great (223&#8211;187 B.C.) figures in Daniel 11:10&#8211;19 as the king of the north who swept into Palestine and was eventually defeated by Rome. His reign marked the transfer of Judea from Ptolemaic to Seleucid control. The Antiochus dynasty represents the collision between Hellenistic culture and Jewish religious identity that defined the intertestamental period, making the name Antiochus a byword for pagan hostility to the covenant people in later Jewish and Christian literature.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "antiochus", "smith": "antiochus", "isbe": "antiochus"},
        "key_refs": ["Daniel 11:13", "1 Maccabees 1:54"],
        "sections": []
    },
    "antipas": {
        "id": "antipas",
        "term": "Antipas",
        "category": "people",
        "intro": "<p>Antipas is the name of two figures in the New Testament. Herod Antipas, son of Herod the Great by his Samaritan wife Malthace, ruled as tetrarch of Galilee and Perea from 4 B.C. to A.D. 39. He is best known for ordering the beheading of John the Baptist at the request of his stepdaughter following John&#39;s condemnation of Antipas&#39;s marriage to his brother Philip&#39;s wife Herodias (Matt. 14:1&#8211;12). Jesus referred to him as &#8220;that fox&#8221; (Luke 13:32), and it was Antipas to whom Pilate sent Jesus for examination during the Passion, an episode Luke alone records (Luke 23:7&#8211;12).</p><p>The second Antipas is described in Revelation 2:13 as a faithful martyr at Pergamum, &#8220;my witness, my faithful one, who was killed among you, where Satan dwells.&#8221; Church tradition holds that he was roasted to death in a bronze bull during the reign of Domitian, though this cannot be verified from contemporary sources. His mention as a martyr at Pergamum, the seat of emperor worship in Asia Minor, illustrates the cost of Christian faithfulness in the face of Roman imperial religion.</p>",
        "hitchcock_meaning": "for all, or against all",
        "source_ids": {"easton": "antipas", "smith": "antipas", "isbe": "antipas"},
        "key_refs": ["Matthew 14:1", "Luke 13:32", "Luke 23:7", "Revelation 2:13"],
        "sections": []
    },
    "antipatris": {
        "id": "antipatris",
        "term": "Antipatris",
        "category": "places",
        "intro": "<p>Antipatris was a city rebuilt by Herod the Great on an ancient site and named in honor of his father Antipater. Located at the foot of the Judean hills where the coastal plain begins, on the road from Jerusalem northward to Caesarea Maritima, it occupied a strategically important position controlling passage between the hill country and the coast. The site is associated with ancient Aphek and the modern location of Ras el-Ain.</p><p>Antipatris appears in the New Testament in the account of Paul&#39;s transfer under military escort from Jerusalem to Caesarea for his hearing before the procurator Felix (Acts 23:31). The soldiers accompanying Paul traveled through the night to reach Antipatris and then returned to Jerusalem, while the cavalry continued with Paul to Caesarea. The city thus appears in a single but vivid biblical episode as a way-station on one of the most important roads in Roman Palestine.</p>",
        "hitchcock_meaning": "for, or against the father",
        "source_ids": {"easton": "antipatris", "isbe": "antipatris"},
        "key_refs": ["Acts 23:31"],
        "sections": []
    },
    "antonia": {
        "id": "antonia",
        "term": "Antonia",
        "category": "places",
        "intro": "<p>Antonia was a massive fortress-palace situated at the northwest corner of the temple mount in Jerusalem, rebuilt and enlarged by Herod the Great and named in honor of his patron Mark Antony. It dominated the northern approaches to the temple complex, serving as both a military garrison and a symbol of Roman authority over the religious heart of the city. The fortress was connected to the temple courts by staircases and passages, allowing Roman troops rapid access in the event of disturbance during the great festivals when Jerusalem was crowded with pilgrims.</p><p>The Antonia features in the New Testament as &#8220;the barracks&#8221; or &#8220;the castle&#8221; where Paul was taken after being seized by a mob in the temple courts (Acts 21:34, 37). It was from the steps of the Antonia that Paul addressed the crowd in Hebrew (Acts 22:1&#8211;21). The fortress was destroyed by Titus during the Roman siege of Jerusalem in A.D. 70, along with the temple itself, leaving no physical trace above ground today.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "antonia", "smith": "antonia"},
        "key_refs": ["Acts 21:34", "Acts 21:37", "Acts 22:1"],
        "sections": []
    },
    "antothite": {
        "id": "antothite",
        "term": "Antothite",
        "category": "people",
        "intro": "<p>Antothite is a gentillic designation meaning &#8220;a native of Anathoth,&#8221; applied in the biblical text to warriors from the Benjaminite city of Anathoth who served among David&#39;s mighty men. The title appears in two forms: &#8220;Antothite&#8221; in 1 Chronicles 11:28 and 12:3, and &#8220;Anethothite&#8221; in 2 Samuel 23:27, both referring to inhabitants of the priestly city northeast of Jerusalem. Abiezer the Antothite was one of David&#39;s thirty mighty men and also served as commander of the ninth monthly division of David&#39;s army (1 Chr. 27:12).</p><p>Jehu the son of Shemaah, also called an Antothite, was one of the ambidextrous Benjaminite warriors who joined David at Ziklag (1 Chr. 12:3). The repeated association of Anathoth with skilled warriors alongside its later fame as the hometown of Jeremiah and the exile-home of the priest Abiathar reflects the multi-dimensional character of this Benjaminite town in Israelite history.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "antothite", "smith": "antothite", "isbe": "antothite"},
        "key_refs": ["1 Chronicles 11:28", "1 Chronicles 12:3", "2 Samuel 23:27"],
        "sections": []
    },
    "anvil": {
        "id": "anvil",
        "term": "Anvil",
        "category": "concepts",
        "intro": "<p>The anvil appears in the English Bible only at Isaiah 41:7, where the prophet describes craftsmen encouraging one another in the making of an idol: the smith smooths the work with a hammer and the one who beats on the anvil pronounces the soldering good. The Hebrew word translated &#8220;anvil&#8221; (<em>pa&#39;am</em>, meaning &#8220;a beat&#8221; or &#8220;stroke&#8221;) reflects the function of the anvil as the surface against which metal is shaped by repeated hammering.</p><p>Isaiah&#39;s ironic portrait of idol-making craftsmen toiling with meticulous care over objects that are ultimately powerless stands in sharp contrast to the portrait of Yahweh that frames it: the God who calls the nations to account and who raises up Cyrus from the east to accomplish his redemptive purposes. The detailed description of the ironworker&#39;s craft in this passage provides one of the more realistic glimpses of ancient metalworking in the Hebrew prophetic literature.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "anvil", "isbe": "anvil"},
        "key_refs": ["Isaiah 41:7"],
        "sections": []
    },
    "ape": {
        "id": "ape",
        "term": "Ape",
        "category": "concepts",
        "intro": "<p>Apes are mentioned twice in Scripture, in the parallel accounts of Solomon&#39;s trading fleet (1 Kings 10:22; 2 Chr. 9:21). Every three years the ships of Tarshish returned with gold, silver, ivory, apes, and peacocks&#8212;luxury imports that signaled the extraordinary wealth and international reach of Solomon&#39;s kingdom. The Hebrew word <em>qoph</em> is widely recognized as a loanword from the Tamil <em>kapi</em> or Sanskrit <em>kapi</em>, indicating that the animals were obtained through trade with India.</p><p>The inclusion of apes among Solomon&#39;s imports reflects the ancient taste for exotic animals as symbols of royal prestige, a practice well attested in Egyptian and Mesopotamian royal records. While apes played a religious role in Egyptian culture&#8212;baboons were sacred to Thoth&#8212;the biblical text treats them simply as luxury commodities demonstrating the scope of Solomonic prosperity. The passage is frequently cited in discussions of the location of Tarshish and the routes of ancient maritime trade.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ape", "isbe": "ape"},
        "key_refs": ["1 Kings 10:22", "2 Chronicles 9:21"],
        "sections": []
    },
    "apelles": {
        "id": "apelles",
        "term": "Apelles",
        "category": "people",
        "intro": "<p>Apelles, whose name means <em>exclusion</em> or <em>separation</em>, is a Christian at Rome greeted by Paul in Romans 16:10 with the commendation that he is &#8220;approved in Christ&#8221;&#8212;a phrase suggesting a man whose faith had been tested and found genuine, perhaps through suffering or persecution. No further biographical details are provided in the New Testament, and he is not mentioned elsewhere in Scripture.</p><p>The name Apelles was common in the Greco-Roman world, known especially from the famous Greek painter of the fourth century B.C., and was also used by Jews in the diaspora. Some early church traditions, without strong historical basis, identify the Apelles of Romans 16 with one of the seventy disciples sent out by Jesus or with a bishop of Smyrna or Heracleia. His brief mention alongside other believers in the Roman church illustrates the diverse community of Jews and Gentiles that had gathered in Rome before Paul&#39;s arrival.</p>",
        "hitchcock_meaning": "exclusion; separation",
        "source_ids": {"easton": "apelles", "smith": "apelles", "isbe": "apelles"},
        "key_refs": ["Romans 16:10"],
        "sections": []
    },
    "apharsachites": {
        "id": "apharsachites",
        "term": "Apharsachites",
        "category": "people",
        "intro": "<p>Apharsachites were one of the foreign peoples transplanted into Samaria by the Assyrian kings following the fall of the northern kingdom of Israel. They appear in the Aramaic section of Ezra, where they are listed among the officials and colonists who sent a letter to the Persian king Artaxerxes protesting the rebuilding of Jerusalem (Ezra 5:6; 6:6). The exact ethnic or geographic origin of the Apharsachites is uncertain; they may have been an administrative or military class rather than a distinct national group.</p><p>Their appearance in the Ezra narrative illustrates the complex, multi-ethnic character of Persian-era Palestine, where Assyrian deportation policies had produced a mixed population in the former northern kingdom. The correspondence they sent to the Persian court reflects the political tensions surrounding the Jewish restoration under Cyrus and Darius, as neighboring groups sought to impede the rebuilding of Jerusalem and its temple.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "apharsachites"},
        "key_refs": ["Ezra 5:6", "Ezra 6:6"],
        "sections": []
    },
    "apharsites": {
        "id": "apharsites",
        "term": "Apharsites",
        "category": "people",
        "intro": "<p>Apharsites were among the various peoples settled in Samaria by the Assyrian king Asnappar (generally identified with Ashurbanipal) following his deportation of the native population. They are listed in the letter sent to Artaxerxes by the opponents of Jerusalem&#39;s rebuilding (Ezra 4:9). The relationship between the Apharsites and the Apharsachites mentioned in Ezra 5 and 6 is disputed; they may be variant forms of the same group or distinct populations.</p><p>Like the other peoples enumerated in Ezra 4:9, the Apharsites illustrate the thoroughness of Assyrian population engineering as a tool of imperial control. By replacing conquered populations with foreign settlers, the Assyrians disrupted existing social and religious networks and created new communities with loyalties defined by imperial appointment rather than ancestral tradition. The descendants of these transplanted peoples remained in the region through the Persian period, forming part of the complex demographic background of Samaria in the era of Ezra and Nehemiah.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "apharsites", "isbe": "apharsites"},
        "key_refs": ["Ezra 4:9"],
        "sections": []
    },
    "aphik": {
        "id": "aphik",
        "term": "Aphik",
        "category": "places",
        "intro": "<p>Aphik (also spelled Aphek) was a city in the territory of Asher from which the Israelites failed to drive out the Canaanite inhabitants during the conquest (Judg. 1:31). Its location is generally placed in the Plain of Acco near the Phoenician coast. The same or related site appears in Joshua 13:4 in connection with the land still to be conquered, and in Joshua 19:30 as part of the Asherite allotment.</p><p>Two other sites named Aphek appear in the biblical narrative: one near Jezreel that served as a Philistine staging point before both the battle in which the ark was captured (1 Sam. 4:1) and Saul&#39;s final battle (1 Sam. 29:1), and another in Transjordan associated with the Syrian wars of Ahab (1 Kings 20:26&#8211;30). The name, meaning &#8220;stronghold&#8221; or &#8220;fortress,&#8221; was applied to multiple sites, which has complicated the task of identifying each with certainty in the archaeological record.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "aphik", "smith": "aphik", "isbe": "aphik"},
        "key_refs": ["Judges 1:31", "Joshua 13:4", "1 Samuel 4:1"],
        "sections": []
    },
    "apocalypse": {
        "id": "apocalypse",
        "term": "Apocalypse",
        "category": "concepts",
        "intro": "<p>Apocalypse derives from the Greek <em>apokalypsis</em>, meaning <em>uncovering</em> or <em>revelation</em>, and is the title of the final book of the New Testament canon, commonly called the Book of Revelation. In this specific sense it refers to the visionary disclosure given to John on the island of Patmos concerning the risen Christ, the heavenly worship, the tribulations of the church, the judgment of evil powers, and the consummation of all things in the new creation (Rev. 1:1).</p><p>As a literary genre, &#8220;apocalyptic&#8221; describes a body of Jewish and early Christian literature characterized by visionary journeys, angelic interpreters, symbolic imagery, cosmic dualism, and eschatological expectation. Major examples include Daniel, 1 Enoch, 4 Ezra, and 2 Baruch alongside the canonical Revelation. The genre flourished in periods of crisis and persecution, offering assurance that God&#39;s sovereignty over history remained intact and that present suffering would give way to ultimate divine vindication. The Apocalypse of John is distinguished from other apocalyptic works by its explicit identification of the author and its direct address to seven historical churches in Asia Minor.</p>",
        "hitchcock_meaning": "uncovering, revelation",
        "source_ids": {"easton": "apocalypse", "smith": "apocalypse"},
        "key_refs": ["Revelation 1:1"],
        "sections": []
    },
    "apocrypha": {
        "id": "apocrypha",
        "term": "Apocrypha",
        "category": "concepts",
        "intro": "<p>Apocrypha, from the Greek meaning <em>hidden</em> or <em>concealed</em>, refers to a collection of Jewish religious writings produced between approximately 300 B.C. and A.D. 100 that are included in the Greek Septuagint and the Latin Vulgate but are not part of the Hebrew canon. The principal books include 1 and 2 Maccabees, Judith, Tobit, Wisdom of Solomon, Ecclesiasticus (Sirach), Baruch, and additions to Daniel and Esther. The Roman Catholic and Eastern Orthodox churches received these books as deuterocanonical scripture at the Council of Trent (1546), while Protestant traditions following the Reformers classify them as useful but non-canonical.</p><p>The term has also been applied more broadly to a range of pseudepigraphical writings attributed to biblical figures but excluded from all canonical lists. The Apocrypha proper is historically valuable for understanding Judaism and early Christianity in the intertestamental period: 1 and 2 Maccabees provide the primary historical account of the Maccabean revolt, while Sirach and Wisdom illuminate the development of wisdom theology. Their presence in the Septuagint meant they were read and cited in early Christian communities, leaving traces in New Testament vocabulary and thought.</p>",
        "hitchcock_meaning": "hidden",
        "source_ids": {"easton": "apocrypha", "smith": "apocrypha", "isbe": "apocrypha"},
        "key_refs": [],
        "sections": []
    },
    "apollonia": {
        "id": "apollonia",
        "term": "Apollonia",
        "category": "places",
        "intro": "<p>Apollonia was a city in the Roman province of Macedonia, situated on the Egnatian Way between Amphipolis to the east and Thessalonica to the west, approximately thirty-six miles from each. Paul and Silas passed through Apollonia on the second missionary journey as they traveled westward from Philippi toward Thessalonica (Acts 17:1). The text suggests they did not stop to establish a congregation there, moving directly to Thessalonica where a Jewish synagogue provided an initial platform for preaching.</p><p>The city was one of several Macedonian towns named after Apollo, the Greek god of music and prophecy. Its location on the principal Roman highway across the northern Aegean region made it a significant waypoint for both commerce and communication between the eastern and western parts of the empire. Though Apollonia receives no further mention in the New Testament, its appearance in Acts 17 illustrates the strategic use of Roman road infrastructure in the early Christian mission.</p>",
        "hitchcock_meaning": "perdition, destruction",
        "source_ids": {"easton": "apollonia", "smith": "apollonia", "isbe": "apollonia"},
        "key_refs": ["Acts 17:1"],
        "sections": []
    },
    "apollos": {
        "id": "apollos",
        "term": "Apollos",
        "category": "people",
        "intro": "<p>Apollos was a Jewish Christian from Alexandria, described in Acts as &#8220;an eloquent man, competent in the Scriptures&#8221; who had been instructed in the way of the Lord and taught accurately about Jesus, though he knew only the baptism of John (Acts 18:24&#8211;25). When Priscilla and Aquila heard him speaking boldly in the Ephesian synagogue, they took him aside and explained the way of God more accurately. He then moved to Achaia, where he proved to be a powerful apologist, &#8220;vigorously refuting the Jews in public and showing by the Scriptures that the Christ was Jesus&#8221; (Acts 18:28).</p><p>In the Corinthian correspondence, Apollos emerges as an unwitting cause of party division: some Corinthians declared themselves followers of Apollos in contrast to followers of Paul or Peter (1 Cor. 1:12; 3:4). Paul firmly denies any rivalry, describing himself and Apollos as fellow servants who plant and water while God gives the growth (1 Cor. 3:5&#8211;9). Paul&#39;s commendation of Apollos as a fellow worker and his apparent difficulty in persuading Apollos to return to Corinth (1 Cor. 16:12) suggest a relationship of mutual respect between the two men.</p>",
        "hitchcock_meaning": "one who destroys; destroyer",
        "source_ids": {"easton": "apollos", "smith": "apollos", "isbe": "apollos"},
        "key_refs": ["Acts 18:24", "Acts 18:28", "1 Corinthians 1:12", "1 Corinthians 3:6"],
        "sections": []
    },
    "apollyon": {
        "id": "apollyon",
        "term": "Apollyon",
        "category": "concepts",
        "intro": "<p>Apollyon, the Greek word for <em>destroyer</em>, is the name given in Revelation 9:11 to the angel of the abyss who rules over the demonic locusts released at the sounding of the fifth trumpet. His Hebrew name Abaddon carries the same meaning and is used in the Old Testament as a term for the realm of the dead or destruction (Job 26:6; Prov. 15:11). As king of the abyss, Apollyon commands a hellish army whose torment is compared to that of a scorpion sting&#8212;painful but not lethal.</p><p>The identification of Apollyon with specific historical figures or institutions has been debated across centuries of interpretation, ranging from Antiochus Epiphanes and the Roman emperors to later ecclesiastical and political figures. In the context of Revelation&#39;s symbolic world, Apollyon represents the organizing intelligence of demonic forces unleashed in the final period of tribulation. John Bunyan gave the name enduring literary currency by making Apollyon the monstrous adversary whom Christian encounters and defeats in <em>The Pilgrim&#39;s Progress</em>.</p>",
        "hitchcock_meaning": "a destroyer",
        "source_ids": {"easton": "apollyon", "smith": "apollyon", "isbe": "apollyon"},
        "key_refs": ["Revelation 9:11"],
        "sections": []
    },
    "apostle": {
        "id": "apostle",
        "term": "Apostle",
        "category": "concepts",
        "intro": "<p>Apostle derives from the Greek <em>apostolos</em>, one who is sent forth as an authoritative representative. Jesus is once designated an apostle in this sense (Heb. 3:1), and the term applies in a general sense to early Christian missionaries (2 Cor. 8:23; Phil. 2:25). In its primary New Testament meaning, however, &#8220;the apostles&#8221; refers to the twelve men specially chosen by Jesus, named in the Gospels and Acts, who were witnesses to his resurrection and were commissioned to lay the foundation of the church (Matt. 10:1&#8211;4; Acts 1:26; Eph. 2:20).</p><p>The qualifications for this original apostolate included direct call by Christ and personal witness of the resurrection (Acts 1:21&#8211;22), which is why Paul&#39;s apostleship, grounded in his Damascus road encounter with the risen Christ, required vigorous defense (Gal. 1:1; 1 Cor. 9:1). The apostles&#39; teaching, preserved in the New Testament, carries foundational authority for the church in all generations. Paul also uses the term more broadly for certain authoritative ministers such as Barnabas (Acts 14:14) and possibly Andronicus and Junia (Rom. 16:7), generating ongoing discussion about the scope of the apostolic office.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "apostle", "smith": "apostle", "isbe": "apostle"},
        "key_refs": ["Hebrews 3:1", "Matthew 10:1", "Acts 1:22", "Ephesians 2:20"],
        "sections": []
    },
    "apothecary": {
        "id": "apothecary",
        "term": "Apothecary",
        "category": "concepts",
        "intro": "<p>Apothecary, rendered &#8220;perfumer&#8221; in the Revised Version and modern translations, designates the craftsman who prepared the sacred anointing oil and incense prescribed by Mosaic law for use in the tabernacle and temple. The Hebrew <em>roqeach</em> describes one skilled in compounding aromatic substances, and the office appears in Exodus 30:25, 35 and 37:29 in connection with the precise formulas given to Moses for the holy oil and incense. Ecclesiastes 10:1 employs the related term to note that dead flies corrupt the perfumer&#39;s ointment, illustrating how small corruptions spoil what is excellent.</p><p>The daughter of Shallum is among those described as helping repair the Jerusalem wall under Nehemiah (Neh. 3:8), and a guild of apothecaries is mentioned in 1 Samuel 8:13 among the royal household servants Solomon would require. The preparation of sacred aromatics demanded specialized knowledge of imported spices and resins, including myrrh, cinnamon, cassia, and calamus, and the prohibition against replicating the holy oil for personal use (Exod. 30:32&#8211;33) underlines the consecrated character of the apothecary&#39;s work in the cultic context.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "apothecary", "isbe": "apothecary"},
        "key_refs": ["Exodus 30:25", "Exodus 37:29", "Ecclesiastes 10:1"],
        "sections": []
    },
    "apparel": {
        "id": "apparel",
        "term": "Apparel",
        "category": "concepts",
        "intro": "<p>Apparel in the Bible encompasses the full range of clothing worn by men and women in ancient Israel and the broader Near Eastern world. The Mosaic law maintained a distinction between male and female dress, prohibiting cross-dressing as an abomination (Deut. 22:5), though the precise differences in garment style between the sexes were not always sharp. Basic garments included an inner tunic of linen or wool, an outer robe, and a girdle or belt; footwear consisted of sandals. Quality, color, and material signaled social status, with fine linen, purple, and scarlet associated with royalty and wealth.</p><p>Scripture addresses apparel in multiple theological registers. Sackcloth served as the garment of mourning and repentance; the high priestly vestments were elaborately prescribed as garments of glory and beauty (Exod. 28). The prophets condemned luxury in dress as a sign of spiritual complacency (Isa. 3:16&#8211;24). In the New Testament, Paul and Peter both urge believers, especially women, to prioritize inner character over outward adornment (1 Tim. 2:9; 1 Pet. 3:3), while James warns against favoritism toward the richly dressed (James 2:2&#8211;4). The white robes of the redeemed in Revelation symbolize righteousness and purity (Rev. 7:9).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "apparel", "isbe": "apparel"},
        "key_refs": ["Deuteronomy 22:5", "Exodus 28:2", "1 Timothy 2:9", "Revelation 7:9"],
        "sections": []
    },
    "appeal": {
        "id": "appeal",
        "term": "Appeal",
        "category": "concepts",
        "intro": "<p>Appeal as a legal concept in Scripture refers to the referral of a difficult case from a lower judicial authority to a higher one. Moses established a graduated court system in the wilderness at Jethro&#39;s suggestion: lesser disputes were decided by appointed judges, while only the &#8220;hard cases&#8221; were brought to Moses himself (Exod. 18:13&#8211;26). Deuteronomy 17:8&#8211;13 extends this principle by directing that cases too difficult for local courts be brought to the priests, Levites, and judge at the central sanctuary.</p><p>The New Testament&#39;s most significant appeal is that of Paul before Festus, the Roman procurator of Judea. When Festus proposed transferring his case to Jerusalem, Paul formally invoked his right as a Roman citizen: &#8220;I appeal to Caesar&#8221; (Acts 25:11). This appeal to the imperial tribunal at Rome was a recognized right of Roman citizens that removed the case from provincial jurisdiction and necessitated Paul&#39;s voyage to Rome. The appeal thus served, ironically, as the mechanism by which Paul fulfilled his intention to witness in the imperial capital (Acts 19:21; 23:11).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "appeal", "smith": "appeal", "isbe": "appeal"},
        "key_refs": ["Exodus 18:26", "Acts 25:11", "Acts 25:12", "Deuteronomy 17:8"],
        "sections": []
    },
    "apphia": {
        "id": "apphia",
        "term": "Apphia",
        "category": "people",
        "intro": "<p>Apphia, whose name is thought to mean <em>productive</em> or <em>fruitful</em>, is a female Christian addressed alongside Philemon and Archippus in Paul&#39;s letter to Philemon (Philem. 1:2). She is identified as &#8220;the sister,&#8221; a designation indicating her membership in the Christian community; many interpreters understand her to be the wife of Philemon, making the household at Colosse the setting for the meeting of the church mentioned in the same verse.</p><p>Beyond this single reference, no further information about Apphia is available from the New Testament. Early church tradition in some martyrologies lists her as having been martyred alongside Philemon and Archippus during a period of persecution at Colossae, though these accounts lack independent historical verification. Her inclusion in the opening address of the letter suggests that the matter of Onesimus, the runaway slave whom Paul was returning, directly concerned her household and that Paul sought her support along with Philemon&#39;s in the reception of Onesimus as a brother in Christ.</p>",
        "hitchcock_meaning": "productive; fruitful",
        "source_ids": {"easton": "apphia", "smith": "apphia", "isbe": "apphia"},
        "key_refs": ["Philemon 1:2"],
        "sections": []
    },
    "appii-forum": {
        "id": "appii-forum",
        "term": "Appii Forum",
        "category": "places",
        "intro": "<p>Appii Forum, meaning &#8220;the market-place of Appius,&#8221; was a town on the Appian Way, the great Roman road connecting Rome to Brundisium (Brindisi) in southern Italy. Situated approximately forty-three miles south of Rome, it was a busy posting station on a canal route through the Pontine Marshes, known in ancient sources as a rough town frequented by merchants and boatmen. The Roman poet Horace described it with some disdain as crowded with shopkeepers and surly boatmen.</p><p>Appii Forum is mentioned in Acts 28:15 as one of the two points where Roman Christians came out to meet Paul as he made his final journey under guard toward the capital. Seeing them, Paul &#8220;thanked God and took courage,&#8221; a brief phrase that captures both his emotional state and the providential significance of Christian fellowship. A second delegation met him at the Three Taverns, about ten miles closer to Rome. The episode illustrates the existence of a vital Christian community in Rome before Paul&#39;s arrival and the news network that had spread word of his approach.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "appii-forum", "smith": "appii-forum", "isbe": "appii-forum"},
        "key_refs": ["Acts 28:15"],
        "sections": []
    },
    "apple": {
        "id": "apple",
        "term": "Apple",
        "category": "concepts",
        "intro": "<p>Apple appears in the King James Version as the translation of the Hebrew <em>tappuah</em>, meaning &#8220;fragrance,&#8221; though scholars widely hold that the true apple (<em>Malus domestica</em>) did not flourish in the climate of ancient Palestine and that the apricot or quince is the more likely referent. The tappuah tree is celebrated in the Song of Solomon for its shade and sweet fruit (Song 2:3; 8:5), and appears in Joel 1:12 in a lament over withered orchards. Proverbs 25:11 uses the image of golden apples in silver settings as a metaphor for a well-spoken word.</p><p>The phrase &#8220;apple of the eye&#8221; (Heb. <em>ishon</em>, literally the &#8220;little man&#8221; visible in the pupil) appears in Deuteronomy 32:10, Psalm 17:8, Proverbs 7:2, and Zechariah 2:8 as a figure for something infinitely precious and carefully protected. This idiom&#8212;applied to Israel as the object of God&#39;s protective care and to the law as the object of personal devotion&#8212;has passed into English idiom through the King James translation and remains in common use today.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "apple"},
        "key_refs": ["Proverbs 25:11", "Deuteronomy 32:10", "Psalms 17:8", "Song of Solomon 2:3"],
        "sections": []
    },
    "apron": {
        "id": "apron",
        "term": "Apron",
        "category": "concepts",
        "intro": "<p>Apron appears twice in the English Bible with different referents. In Genesis 3:7, following the fall, Adam and Eve sewed fig leaves together and made themselves &#8220;aprons&#8221; (Hebrew <em>chagor</em>, more precisely &#8220;girdles&#8221; or &#8220;loincloths&#8221;) as the first human attempt to cover their newly experienced shame. This act of self-covering stands in contrast to the later divine provision of garments of skin, suggesting the inadequacy of human remedies for moral guilt.</p><p>In Acts 19:12, the word translates the Greek <em>simikinthion</em>, a craftsman&#39;s working apron or short cloth that Paul wore during his tentmaking work in Ephesus. Handkerchiefs and aprons that had touched Paul&#39;s body were carried to the sick, who were healed and delivered from evil spirits&#8212;an episode that underlines the extraordinary character of Paul&#39;s ministry in Ephesus and echoes the Gospel accounts of people being healed by touching the fringe of Jesus&#39; garment. The narrative does not suggest that the healing power resided in the objects themselves but in the God who acted through them.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "apron", "isbe": "apron"},
        "key_refs": ["Genesis 3:7", "Acts 19:12"],
        "sections": []
    },
    "aquila": {
        "id": "aquila",
        "term": "Aquila",
        "category": "people",
        "intro": "<p>Aquila, whose name means <em>eagle</em>, was a Jewish Christian tentmaker originally from Pontus on the Black Sea coast who had settled in Rome until the emperor Claudius expelled all Jews from the city around A.D. 49. He and his wife Priscilla (Prisca) then moved to Corinth, where Paul met them on his first visit and worked with them at their shared trade (Acts 18:2&#8211;3). The couple became close associates of Paul, accompanying him as far as Ephesus when he left Corinth, and there they instructed the eloquent Apollos more fully in the Christian faith (Acts 18:18&#8211;26).</p><p>Paul&#39;s letters reveal a remarkably mobile couple who hosted house churches wherever they settled. They are greeted in Romans 16:3&#8211;5, where Paul notes they &#8220;risked their necks&#8221; for his life, in 1 Corinthians 16:19, and in 2 Timothy 4:19. The mention of a church in their house in both Rome and Ephesus suggests they moved back to Rome after Claudius&#39;s edict lapsed, making them a concrete example of the household-based Christian communities that characterized the first-century church.</p>",
        "hitchcock_meaning": "an eagle",
        "source_ids": {"easton": "aquila", "smith": "aquila", "isbe": "aquila"},
        "key_refs": ["Acts 18:2", "Acts 18:26", "Romans 16:3", "2 Timothy 4:19"],
        "sections": []
    },
    "arab": {
        "id": "arab",
        "term": "Arab",
        "category": "places",
        "intro": "<p>Arab was a city in the hill country of Judah, listed in the tribal allotment of Joshua 15:52 among the towns in the mountainous southern district of the tribe. Its name, meaning <em>ambush</em>, may reflect a topographical feature of the site&#8212;perhaps a hidden valley or concealed approach. The city is generally identified with Khirbet er-Rabiyeh, located in the southern Judean highlands approximately twelve miles southwest of Hebron.</p><p>Arab is not mentioned elsewhere in the biblical narrative, and no significant events are recorded there. Its inclusion in the Judahite city list of Joshua 15 nevertheless attests to the systematic settlement of the hill country by the tribe of Judah following the initial conquest, filling in a landscape that would later be familiar from references to cities like Hebron, Eshtemoa, and Debir in the same district.</p>",
        "hitchcock_meaning": "multiplying; sowing sedition; a window; a locust",
        "source_ids": {"easton": "arab", "smith": "arab", "isbe": "arab"},
        "key_refs": ["Joshua 15:52"],
        "sections": []
    },
    "arabah": {
        "id": "arabah",
        "term": "Arabah",
        "category": "places",
        "intro": "<p>Arabah, from a Hebrew root meaning <em>burnt up</em> or <em>arid</em>, designates the great rift valley running from the Sea of Galilee southward through the Dead Sea to the Gulf of Aqaba. The term appears both as a proper geographic name and as a common noun for desert or wilderness terrain. In the Revised Version it replaces the King James &#8220;plain&#8221; in numerous passages, giving readers a clearer sense of the distinct geographic feature involved (2 Kings 14:25; Josh. 3:16).</p><p>The Arabah played a significant role in Israel&#39;s history. The Israelites traveled through it during the wilderness wandering, and its southern section served as the route of march in several later military campaigns. Amos 6:14 names the &#8220;brook of the Arabah&#8221; as a boundary marker, and the Israelite copper mines in the Arabah south of the Dead Sea (the Wadi Arabah) supplied material for the Solomonic building projects. The term&#39;s various applications&#8212;to the Jordan valley, to the Dead Sea region, and to the broader rift depression&#8212;reflect the flexibility of Hebrew geographic terminology.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "arabah", "smith": "arabah", "isbe": "arabah"},
        "key_refs": ["Joshua 3:16", "2 Kings 14:25", "Amos 6:14"],
        "sections": []
    },
    "arabia": {
        "id": "arabia",
        "term": "Arabia",
        "category": "places",
        "intro": "<p>Arabia is a vast peninsula in southwest Asia bounded by the Red Sea to the west, the Persian Gulf and the Gulf of Oman to the east, and the Syrian and Mesopotamian deserts to the north. In the Old Testament it appears under various designations, most commonly as the homeland of desert-dwelling nomadic peoples and as the source of luxury trade goods&#8212;gold, spices, and precious stones. Solomon received tribute from the kings of Arabia (2 Chr. 9:14), and caravans from Arabia with spices, gold, and precious stones were part of the wealth that flowed through the ancient Near East.</p><p>In the New Testament Arabia is most significant in Paul&#39;s account of his movements after his Damascus road conversion: he went away into Arabia before returning to Damascus (Gal. 1:17). The duration and purpose of this Arabian sojourn are not described, though it evidently preceded his first Jerusalem visit by three years. Paul may have preached in the Nabataean kingdom, whose governor later sought to arrest him at Damascus (2 Cor. 11:32). The Arabians present at Pentecost (Acts 2:11) represent the southernmost extent of the diaspora Jewish community gathered in Jerusalem.</p>",
        "hitchcock_meaning": "evening; desert; ravens",
        "source_ids": {"easton": "arabia", "smith": "arabia", "isbe": "arabia"},
        "key_refs": ["Genesis 10:7", "2 Chronicles 9:14", "Galatians 1:17", "Acts 2:11"],
        "sections": []
    },
    "arad": {
        "id": "arad",
        "term": "Arad",
        "category": "places",
        "intro": "<p>Arad designates both a Canaanite city and a personal name in the Old Testament. The city of Arad lay in the Negev, approximately twenty miles south of Hebron, and its king attacked the Israelites during the wilderness period, taking captives. Israel responded with a vow to destroy it, and the LORD delivered Arad&#39;s cities into their hand (Num. 21:1&#8211;3; 33:40). The Kenite clan of Hobab, Moses&#39; father-in-law, settled in the vicinity of Arad following the conquest (Judg. 1:16). Archaeological excavations at Tell Arad have uncovered important evidence of Iron Age occupation, including a Judahite temple and a collection of Hebrew ostraca.</p><p>As a personal name, Arad appears in 1 Chronicles 8:15 as a Benjaminite, son of Beriah. The name likely means <em>a wild ass</em> or <em>a dragon</em>, reflecting the rugged terrain of the Negev with which the city was associated. The repeated mention of Arad in the wilderness and conquest narratives places it among the more significant points of conflict in Israel&#39;s southward approach to Canaan.</p>",
        "hitchcock_meaning": "a wild ass; a dragon",
        "source_ids": {"easton": "arad", "smith": "arad", "isbe": "arad"},
        "key_refs": ["Numbers 21:1", "Numbers 33:40", "Judges 1:16"],
        "sections": []
    },
    "aram": {
        "id": "aram",
        "term": "Aram",
        "category": "people",
        "intro": "<p>Aram, meaning <em>highness</em> or <em>magnificence</em>, is first a son of Shem in the Table of Nations (Gen. 10:22), making him the eponymous ancestor of the Aramean peoples who occupied the region of Syria and Mesopotamia. A second Aram appears as a grandson of Nahor, Abraham&#39;s brother (Gen. 22:21). In Matthew 1:3&#8211;4 and Luke 3:33, the name appears in the genealogy of Jesus, representing the generation from Hezron to Amminadab.</p><p>As a geographic and ethnic designation, Aram identified the broad region of Syria and upper Mesopotamia, with compound forms specifying particular areas: Aram-naharaim (Aram of the two rivers, i.e., Mesopotamia), Aram-zobah (an Aramean state northeast of Damascus), and Aram-Damascus (the dominant Aramean kingdom in the period of the divided monarchy). The Arameans were both trading partners and persistent military adversaries of Israel, and their language&#8212;Aramaic&#8212;eventually became the common tongue of the ancient Near East and the everyday language spoken in Palestine during the New Testament period.</p>",
        "hitchcock_meaning": "highness, magnificence, one that deceives; curse",
        "source_ids": {"easton": "aram", "smith": "aram", "isbe": "aram"},
        "key_refs": ["Genesis 10:22", "Genesis 22:21", "Matthew 1:3", "Luke 3:33"],
        "sections": []
    },
    "aram-naharaim": {
        "id": "aram-naharaim",
        "term": "Aram-naharaim",
        "category": "places",
        "intro": "<p>Aram-naharaim, meaning <em>Aram of the two rivers</em>, is the biblical designation for upper Mesopotamia, the region between the Euphrates and the Tigris&#8212;or, more precisely, between the Euphrates and its tributary the Habor (Khabur). It corresponds to the region the Greeks called Mesopotamia and is so rendered in the Septuagint and in Acts 7:2. Abraham&#39;s family settled here before his call, at Haran in Paddan-aram (Gen. 24:10; 28:2), and this is the homeland to which Abraham sent his servant to find a wife for Isaac.</p><p>Psalm 60 bears the superscription &#8220;When he strove with Aram-naharaim,&#8221; linking it to David&#39;s campaigns against the Aramean states of the north. Hosea 12:12 recalls Jacob&#39;s service in Aram as background for an appeal to national humility. The region&#39;s cultural and linguistic links to Israel&#8212;the patriarchs were themselves Aramean by descent (Deut. 26:5)&#8212;make Aram-naharaim a crucial geographic and theological reference point in the narrative of Israel&#39;s origins.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "aram-naharaim"},
        "key_refs": ["Genesis 24:10", "Psalms 60:1", "Hosea 12:12"],
        "sections": []
    },
    "aram-zobah": {
        "id": "aram-zobah",
        "term": "Aram-zobah",
        "category": "places",
        "intro": "<p>Aram-zobah was an Aramean kingdom located between the Euphrates River and the Orontes, in the region north and east of Damascus. It appears in the superscription of Psalm 60 in connection with David&#39;s wars against the Aramean states: &#8220;When he strove with Aram-naharaim and with Aram-zobah.&#8221; Zobah was a significant military power during the early monarchy, and its king Hadadezer clashed repeatedly with both Saul and David.</p><p>David defeated Hadadezer of Zobah and subjugated his kingdom, garrisoning the territory and receiving tribute (2 Sam. 8:3&#8211;8; 1 Chr. 18:3&#8211;8). The Arameans of Zobah allied with the Ammonites against David (2 Sam. 10:6&#8211;19), but were defeated again, effectively eliminating Zobah as a major independent power. The region subsequently came under the influence of Damascus, which emerged as the dominant Aramean state from the time of Solomon onward. Psalm 60 is generally understood as a liturgical response to the crises of these northern campaigns.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "aram-zobah"},
        "key_refs": ["Psalms 60:1", "2 Samuel 8:3"],
        "sections": []
    },
    "aran": {
        "id": "aran",
        "term": "Aran",
        "category": "people",
        "intro": "<p>Aran, whose name means <em>wild goat</em> or has been connected with the idea of an ark, was a Horite chieftain, son of Dishan and grandson of Seir, listed in the genealogy of the original inhabitants of the land of Edom (Gen. 36:28; 1 Chr. 1:42). The Horites were the pre-Edomite population of the region later known as Edom or Seir, and their chiefs are enumerated in Genesis 36:20&#8211;30 as part of the comprehensive account of Esau&#39;s descendants and the political history of the region south of the Dead Sea.</p><p>Aran is not mentioned again beyond these two genealogical notices, and no narrative events are associated with him. His inclusion in the Horite chief list reflects the biblical interest in the peoples displaced by Esau&#39;s descendants, whom God is said to have given the land of Seir as their possession, paralleling Israel&#39;s own dispossession of Canaan (Deut. 2:12, 22).</p>",
        "hitchcock_meaning": "an ark; their curse",
        "source_ids": {"easton": "aran", "smith": "aran", "isbe": "aran"},
        "key_refs": ["Genesis 36:28", "1 Chronicles 1:42"],
        "sections": []
    },
    "ararat": {
        "id": "ararat",
        "term": "Ararat",
        "category": "places",
        "intro": "<p>Ararat designates a mountainous region in what is now eastern Turkey and Armenia, known in Assyrian sources as Urartu. The Hebrew text of Genesis 8:4 states that Noah&#39;s ark &#8220;rested on the mountains of Ararat&#8221; after the floodwaters receded. The plural &#8220;mountains&#8221; suggests a range rather than a single peak, though later tradition, followed by much popular usage, identified the resting place with the volcanic massif now called Mount Ararat (Agri Dagi), rising to approximately 17,000 feet.</p><p>Ararat also appears in the prophetic literature as the territory to which the assassins of the Assyrian king Sennacherib fled (2 Kings 19:37; Isa. 37:38), identifying it as a distinct political entity northwest of Assyria. Jeremiah 51:27 summons &#8220;the kingdoms of Ararat, Minni, and Ashkenaz&#8221; as agents of divine judgment against Babylon. The repeated association of Ararat with the ark&#39;s resting place gave the region a lasting symbolic significance in Jewish, Christian, and Islamic traditions as the site of humanity&#39;s new beginning after the flood.</p>",
        "hitchcock_meaning": "the curse of trembling",
        "source_ids": {"easton": "ararat", "isbe": "ararat"},
        "key_refs": ["Genesis 8:4", "2 Kings 19:37", "Jeremiah 51:27"],
        "sections": []
    },
    "araunah": {
        "id": "araunah",
        "term": "Araunah",
        "category": "people",
        "intro": "<p>Araunah (also called Ornan in Chronicles) was a Jebusite who owned a threshing floor on the summit of Mount Moriah in Jerusalem. When a plague struck Israel following David&#39;s census, the prophet Gad instructed the king to erect an altar on Araunah&#39;s threshing floor. Araunah offered the site freely, along with oxen for sacrifice and threshing sledges for fuel, but David refused the gift, declaring, &#8220;I will not offer burnt offerings to the LORD my God that cost me nothing&#8221; (2 Sam. 24:24; 1 Chr. 21:24). David paid the full price&#8212;fifty shekels of silver, or according to Chronicles six hundred shekels of gold&#8212;and built the altar there.</p><p>This purchase became the site of Solomon&#39;s temple, and 2 Chronicles 3:1 explicitly identifies Mount Moriah, the location of Araunah&#39;s threshing floor, with the place where Abraham had been commanded to offer Isaac. The convergence of these three narratives&#8212;the Abrahamic sacrifice, David&#39;s purchase, and Solomon&#39;s temple&#8212;makes the site of Araunah&#39;s threshing floor one of the most theologically laden locations in the entire biblical narrative.</p>",
        "hitchcock_meaning": "ark; song; joyful cry",
        "source_ids": {"easton": "araunah", "smith": "araunah", "isbe": "araunah"},
        "key_refs": ["2 Samuel 24:24", "1 Chronicles 21:24", "2 Chronicles 3:1"],
        "sections": []
    },
    "arba": {
        "id": "arba",
        "term": "Arba",
        "category": "people",
        "intro": "<p>Arba, whose name means <em>four</em>, was a giant of the Anakim described as &#8220;the greatest man among the Anakim&#8221; (Josh. 14:15). From him the city of Hebron derived its earlier name Kirjath-arba, meaning &#8220;city of Arba&#8221; or possibly &#8220;city of four.&#8221; His son or descendant Anak gave his name to the Anakim, the race of giants whose presence in Canaan had terrified the ten unfaithful spies sent from Kadesh-barnea (Num. 13:28, 33).</p><p>After the conquest, Caleb specifically requested Hebron&#8212;the inheritance of the Anakim&#8212;as his portion, and the text notes that &#8220;Arba was the greatest man among the Anakim&#8221; as justification for the significance of Caleb&#39;s request (Josh. 14:15). Caleb subsequently drove out the three sons of Anak from Hebron (Josh. 15:13&#8211;14), and the city became his inheritance and later served as David&#39;s capital during the seven years before he captured Jerusalem. The ancient name Kirjath-arba continued to be used alongside Hebron in later texts (Gen. 23:2; Neh. 11:25).</p>",
        "hitchcock_meaning": "four",
        "source_ids": {"easton": "arba", "smith": "arba", "isbe": "arba"},
        "key_refs": ["Joshua 14:15", "Joshua 15:13", "Genesis 23:2"],
        "sections": []
    },
    "arbathite": {
        "id": "arbathite",
        "term": "Arbathite",
        "category": "people",
        "intro": "<p>Arbathite is a gentillic designation meaning &#8220;a native of the Arabah&#8221; or, more specifically, a native of Beth-arabah, one of the towns in the Judean wilderness near the northern end of the Dead Sea (Josh. 15:61). The title appears in the lists of David&#39;s mighty men, applied to Abi-albon (also called Abiel in 1 Chr. 11:32), who served among David&#39;s elite warriors known as the Thirty (2 Sam. 23:31; 1 Chr. 11:32).</p><p>Beth-arabah lay in the desolate Jordan rift valley, assigned to both Judah (Josh. 15:6, 61) and Benjamin (Josh. 18:22) in the tribal allotments, reflecting its position on the boundary between the two tribes. Warriors identified by their place of origin in the military records of David&#39;s reign reflect the practice of recruiting men from across the tribal territories, with even the arid desert regions of the Arabah contributing to the royal military establishment.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "arbathite", "smith": "arbathite", "isbe": "arbathite"},
        "key_refs": ["2 Samuel 23:31", "1 Chronicles 11:32"],
        "sections": []
    },
    "arch": {
        "id": "arch",
        "term": "Arch",
        "category": "concepts",
        "intro": "<p>Arch as an architectural term appears in the English Bible only in Ezekiel&#39;s vision of the restored temple (Ezek. 40:16, 21, 22, 26, 29), where the Hebrew word <em>ayil</em> is variously rendered &#8220;arch,&#8221; &#8220;post,&#8221; or &#8220;pillar&#8221; depending on the translation. The precise architectural feature intended is debated, with some interpreters understanding it as a pillared porch or vestibule (&#8220;elam&#8221;) rather than a true semicircular arch in the later Roman sense.</p><p>Whether the ancient Israelites used the true voussoir arch&#8212;constructed of wedge-shaped stones&#8212;remains a matter of archaeological discussion, though examples of corbelled arches and post-and-lintel construction are well attested in Bronze and Iron Age Palestine. Ezekiel&#39;s precise measurements and descriptions in chapters 40&#8211;48 reflect either a visionary ideal or an architectural tradition whose technical vocabulary was not always preserved with perfect clarity through the transmission of the Hebrew text.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "arch", "isbe": "arch"},
        "key_refs": ["Ezekiel 40:16", "Ezekiel 40:22"],
        "sections": []
    },
    "archangel": {
        "id": "archangel",
        "term": "Archangel",
        "category": "concepts",
        "intro": "<p>Archangel, meaning <em>chief angel</em> or <em>prince of angels</em>, designates the highest rank within the angelic hierarchy. The term appears only twice in the New Testament: in 1 Thessalonians 4:16, where &#8220;the voice of an archangel&#8221; accompanies the descent of the Lord at the second coming, and in Jude 9, where Michael is identified as &#8220;the archangel&#8221; who disputed with the devil over the body of Moses. The definite article in Jude suggests a unique office or a specific recognized title.</p><p>Michael is the only figure explicitly designated archangel in canonical Scripture. Daniel 10:13 calls him &#8220;one of the chief princes,&#8221; and Daniel 12:1 identifies him as &#8220;the great prince who has charge of your people.&#8221; The intertestamental literature, particularly 1 Enoch, develops the archangel concept more fully, naming seven archangels including Gabriel, Raphael, and others. Gabriel is described in Daniel 8:16 and 9:21 as sent to interpret visions and later announces the births of John the Baptist and Jesus in Luke&#39;s Gospel, though the canonical text does not explicitly designate him an archangel.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "archangel"},
        "key_refs": ["1 Thessalonians 4:16", "Jude 1:9", "Daniel 12:1"],
        "sections": []
    },
    "archelaus": {
        "id": "archelaus",
        "term": "Archelaus",
        "category": "people",
        "intro": "<p>Archelaus, whose name means <em>ruler of the people</em>, was the son of Herod the Great by his Samaritan wife Malthace, and thus a full brother of Herod Antipas. On Herod&#39;s death in 4 B.C., Archelaus received Judea, Samaria, and Idumea as his share of the divided kingdom, though Augustus declined to give him the title of king, granting him only the lesser rank of ethnarch with the promise of kingship if he proved worthy. He was educated in Rome alongside his brother Antipas, and both traveled there after Herod&#39;s death to contest the terms of the will before the emperor.</p><p>Archelaus&#39;s reign was notoriously brutal. He massacred three thousand people in the temple courts at Passover early in his rule. Both Jewish and Samaritan delegations eventually appealed to Rome against his tyranny, and Augustus exiled him to Gaul in A.D. 6, converting his territory into the Roman province of Judaea under a prefect. Matthew 2:22 records that Joseph, warned in a dream, avoided Judea on returning from Egypt precisely because Archelaus was ruling there, choosing instead to settle in Galilee under the milder rule of Antipas.</p>",
        "hitchcock_meaning": "the prince of the people",
        "source_ids": {"easton": "archelaus", "smith": "archelaus", "isbe": "archelaus"},
        "key_refs": ["Matthew 2:22"],
        "sections": []
    },
    "archer": {
        "id": "archer",
        "term": "Archer",
        "category": "concepts",
        "intro": "<p>Archery was among the most important military skills in the ancient Near East, and archers are mentioned throughout the biblical narrative from the patriarchal period onward. Ishmael became a skilled archer in the wilderness (Gen. 21:20), and Isaac&#39;s blessing of his sons was connected to Esau&#39;s hunting prowess with the bow (Gen. 27:3). Saul was wounded by Philistine archers at the battle of Gilboa (1 Chr. 10:3), and Jonathan&#39;s bow is celebrated in David&#39;s lament (2 Sam. 1:22). The tribe of Benjamin was particularly noted for its archers, some of whom were ambidextrous (1 Chr. 12:2).</p><p>In the prophetic literature, the bow and arrow serve as powerful images of divine judgment. Jeremiah 49:35 announces that God will break the bow of Elam, the source of its military strength, and Hosea 1:5 declares that the bow of Israel will be broken in the Valley of Jezreel. Archery also figures in military training (1 Sam. 31:3; 2 Sam. 11:24; 2 Kings 13:15&#8211;19), and the metaphorical use of arrows for words, afflictions, and divine wrath is common across the Psalms and prophetic literature.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "archer"},
        "key_refs": ["Genesis 21:20", "1 Chronicles 10:3", "Psalms 7:13", "Jeremiah 49:35"],
        "sections": []
    },
    "archevite": {
        "id": "archevite",
        "term": "Archevite",
        "category": "people",
        "intro": "<p>Archevites were among the foreign peoples resettled in Samaria by the Assyrian king Asnappar following the deportation of the northern Israelite population. They are listed in Ezra 4:9 as signatories to a letter sent to Artaxerxes opposing the rebuilding of Jerusalem. The name is generally connected with Erech (Uruk), one of the most ancient cities of Mesopotamia, located in southern Babylon. Their presence in Samaria reflects the Assyrian and later Babylonian practice of using population transfers as tools of imperial control.</p><p>Like the other groups named in Ezra 4:9&#8212;Dinaites, Apharsathchites, Tarpelites, Apharsites, and others&#8212;the Archevites represent the diverse, ethnically mixed population that had developed in the former northern kingdom over the century and a half between the Assyrian conquest and the Persian restoration of Judah. Their opposition to Jerusalem&#39;s rebuilding reflects the political interests of a settled population who had no desire to see Judean national institutions restored.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "archevite", "isbe": "archevite"},
        "key_refs": ["Ezra 4:9"],
        "sections": []
    },
    "archi": {
        "id": "archi",
        "term": "Archi",
        "category": "places",
        "intro": "<p>Archi was a locality on the boundary between the tribes of Ephraim and Benjamin (Josh. 16:2), situated between Bethel to the east and Beth-horon the Nether to the west. The site gave its name to the Archites, a clan or community whose most notable member was Hushai, &#8220;David&#39;s friend&#8221; and royal counselor (2 Sam. 15:32; 16:16; 17:5; 1 Chr. 27:33). The precise location of Archi is uncertain, though the boundary description in Joshua 16 places it in the territory between the central ridge and the Aijalon Valley descent toward the coastal plain.</p><p>Archi appears only once as a place name in the biblical text, though the gentillic &#8220;Archite&#8221; recurs several times in connection with Hushai. His designation as the Archite identifies him by his village or clan origin, a common convention in biblical narrative for distinguishing individuals bearing common names. The proximity of Archi to Bethel and the main routes between Jerusalem and the coastal plain gives the location strategic significance in the narrative of Absalom&#39;s revolt.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "archi", "smith": "archi"},
        "key_refs": ["Joshua 16:2"],
        "sections": []
    },
    "archippus": {
        "id": "archippus",
        "term": "Archippus",
        "category": "people",
        "intro": "<p>Archippus, whose name means <em>master of the horse</em>, was a Christian leader at Colossae addressed by Paul in both the letter to the Colossians and the letter to Philemon. In Philemon 1:2 he is called &#8220;our fellow soldier,&#8221; a term Paul uses for those engaged alongside him in the work of the gospel. Colossians 4:17 contains a direct charge to the church: &#8220;See that you fulfill the ministry that you have received in the Lord.&#8221;</p><p>The specific nature of Archippus&#39;s ministry is not defined, and the exhortation to fulfill it has generated speculation about whether he was being reminded to complete a task, exhorted in the face of discouragement, or simply publicly commissioned by apostolic letter. Some interpreters, noting the household context in both letters, suggest he may have been a son of Philemon and Apphia, placed in pastoral charge of the house church at Colossae. Church tradition in later martyrologies links him to the fate of Philemon and Apphia at Colossae, though these accounts are unverifiable.</p>",
        "hitchcock_meaning": "a master of horses",
        "source_ids": {"easton": "archippus", "smith": "archippus", "isbe": "archippus"},
        "key_refs": ["Philemon 1:2", "Colossians 4:17"],
        "sections": []
    },
    "archite": {
        "id": "archite",
        "term": "Archite",
        "category": "people",
        "intro": "<p>Archite is the designation applied to Hushai, one of the most important figures in the narrative of Absalom&#39;s revolt against David (2 Sam. 15:32; 16:16; 17:5, 14; 1 Chr. 27:33). The title identifies him as a native of Archi, a locality on the Benjamin-Ephraim border. Hushai is called &#8220;the king&#39;s friend,&#8221; a formal court title denoting a trusted royal advisor of the highest rank. When David fled Jerusalem during Absalom&#39;s coup, he sent Hushai back to the city as a counterspy with instructions to undermine the counsel of Ahithophel.</p><p>Hushai&#39;s successful counterintelligence operation&#8212;persuading Absalom to reject Ahithophel&#39;s strategically sound advice and adopt a delay that allowed David time to escape and regroup&#8212;was decisive in determining the outcome of the revolt. The narrative frames this outcome as the LORD&#39;s overruling of Ahithophel&#39;s counsel (2 Sam. 17:14). Hushai thus represents a model of loyal service and courageous deception employed in the service of the divinely anointed king.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "archite"},
        "key_refs": ["2 Samuel 15:32", "2 Samuel 17:14", "1 Chronicles 27:33"],
        "sections": []
    },
    "arcturus": {
        "id": "arcturus",
        "term": "Arcturus",
        "category": "concepts",
        "intro": "<p>Arcturus appears twice in the book of Job as part of a list of star formations cited in God&#39;s speech from the whirlwind (Job 9:9; 38:32). The Hebrew term rendered &#8220;Arcturus&#8221; in the King James Version (<em>&#39;ash</em> or <em>&#39;ayish</em>) is now more commonly translated &#8220;the Bear&#8221; by modern versions, identifying the constellation Ursa Major (the Great Bear, or the Plough). Arcturus itself is the brightest star in the constellation Bootes, adjacent to Ursa Major, and ancient translators associated the Hebrew term with this conspicuous star.</p><p>The context of both Job passages is God&#39;s challenge to Job&#39;s understanding of the created order: &#8220;Can you bind the chains of the Pleiades or loose the belt of Orion? Can you lead forth the Mazzaroth in their season, or can you guide the Bear with its children?&#8221; (Job 38:31&#8211;32). The rhetorical questions invoke the predictable but humanly uncontrollable movements of the stars as evidence of divine power and wisdom that far exceeds human comprehension, one of the most sustained passages in Scripture on the theological significance of the cosmos.</p>",
        "hitchcock_meaning": "a gathering together",
        "source_ids": {"easton": "arcturus", "smith": "arcturus"},
        "key_refs": ["Job 9:9", "Job 38:32"],
        "sections": []
    },
    "ard": {
        "id": "ard",
        "term": "Ard",
        "category": "people",
        "intro": "<p>Ard, whose name means <em>one that descends</em> or <em>fugitive</em>, was a descendant of Benjamin and head of one of the Israelite clans that entered Egypt with Jacob&#39;s household. In Numbers 26:38&#8211;40, Ard is listed as a son of Bela and grandson of Benjamin, counted among the clans of Benjamin in the wilderness census; his descendants are called the Ardites. The parallel account in Genesis 46:21 lists Ard among the sons of Benjamin directly, which may reflect a difference in genealogical reckoning or a textual variant.</p><p>In 1 Chronicles 8:3, the corresponding figure is called Addar, a name closely related to Ard and likely representing the same individual. The Ardite clan descended from him was among the Benjaminite families that survived to the time of the second wilderness census, despite the heavy losses sustained by some tribes during the wilderness period. Ard&#39;s significance is entirely genealogical, placing him as an ancestor of the tribal subgroups that formed the post-conquest Benjaminite community.</p>",
        "hitchcock_meaning": "one that commands; he that descends",
        "source_ids": {"easton": "ard", "smith": "ard", "isbe": "ard"},
        "key_refs": ["Numbers 26:38", "1 Chronicles 8:3", "Genesis 46:21"],
        "sections": []
    },
    "ardon": {
        "id": "ardon",
        "term": "Ardon",
        "category": "people",
        "intro": "<p>Ardon, whose name is thought to mean <em>descendant</em> or <em>ruling</em>, was the third of three sons born to Caleb son of Hezron by his wife Azubah (1 Chr. 2:18). He is mentioned alongside his brothers Jesher and Shobab in the Judahite genealogy preserved in 1 Chronicles 2. Caleb son of Hezron belongs to the broader Judahite lineage and is distinct from the more famous Caleb son of Jephunneh, the spy and conqueror of Hebron.</p><p>No narrative material accompanies Ardon&#39;s mention in Scripture; his significance lies entirely in his place within the genealogical record of Judah. The genealogies of 1 Chronicles 2&#8211;4 preserve detailed clan records of the tribe of Judah that are not found elsewhere in the Old Testament, and Ardon&#39;s inclusion reflects the care with which the Chronicler traced the extended family structures of Israel&#39;s most prominent tribe from the patriarchal period into the settlement era.</p>",
        "hitchcock_meaning": "ruling; a judgment of malediction",
        "source_ids": {"easton": "ardon", "smith": "ardon", "isbe": "ardon"},
        "key_refs": ["1 Chronicles 2:18"],
        "sections": []
    },
    "areopagite": {
        "id": "areopagite",
        "term": "Areopagite",
        "category": "people",
        "intro": "<p>Areopagite designates a member of the ancient Athenian court of the Areopagus, the council that convened on Mars&#39; Hill to deliberate on matters of law, morals, and religion. In the New Testament the term applies to Dionysius, who is identified as one of the few converts made during Paul&#39;s address on the Areopagus during his visit to Athens (Acts 17:34). The brief notice&#8212;&#8220;But some men joined him and believed, among whom also was Dionysius the Areopagite and a woman named Damaris&#8221;&#8212;suggests that while Paul&#39;s Athens ministry did not produce a large church, it did win over a member of the city&#39;s most prestigious judicial body.</p><p>The historical Dionysius the Areopagite of Acts has been distinguished from the corpus of mystical theological writings attributed to &#8220;Dionysius the Areopagite&#8221; that circulated from the late fifth century onward, now known to scholars as the Pseudo-Dionysian corpus. This later body of work exercised enormous influence on medieval Christian mysticism, but its authorship by the Athenian convert of Acts 17 is universally rejected on historical grounds.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "areopagite", "smith": "areopagite"},
        "key_refs": ["Acts 17:34"],
        "sections": []
    },
    "areopagus": {
        "id": "areopagus",
        "term": "Areopagus",
        "category": "places",
        "intro": "<p>Areopagus, meaning <em>hill of Ares</em> (Mars&#39; Hill in the King James Version), is a bare rocky outcrop northwest of the Acropolis in Athens. It was the site of the ancient Athenian council of the same name, one of the most venerable institutions of classical Greece, which had jurisdiction over matters of religion, morals, and education. Paul was brought before this council&#8212;or to this location&#8212;during his visit to Athens, apparently to explain the new teaching he had been proclaiming in the agora (Acts 17:19, 22).</p><p>Paul&#39;s Areopagus address (Acts 17:22&#8211;31) is one of the most studied speeches in the New Testament, notable for its engagement with Stoic and Epicurean philosophy, its citation of Greek poets, and its movement from creation theology to the resurrection. Paul uses the Athenians&#39; altar &#8220;to an unknown God&#8221; as a point of entry, arguing that this unknown God is the Creator of all who does not dwell in man-made temples. The speech concludes with a call to repentance in light of the coming judgment, with Jesus&#39; resurrection as its guarantee. The mixed response&#8212;some mocked, some wanted to hear more, a few believed&#8212;anticipates the range of reactions the gospel would encounter throughout the Hellenistic world.</p>",
        "hitchcock_meaning": "the hill of Mars",
        "source_ids": {"easton": "areopagus", "isbe": "areopagus"},
        "key_refs": ["Acts 17:22", "Acts 17:19", "Acts 17:31"],
        "sections": []
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
    print(f'BP a4: Anamim → Areopagus: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
