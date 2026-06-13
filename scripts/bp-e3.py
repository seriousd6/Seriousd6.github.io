"""
BP Article Synthesis — e3: Eshtemoa → Ezri
Covers Easton entries: Eshtemoa through Ezri (47 entries)

Sources consulted:
  - data/dictionary/index.json (Easton briefs)
  - data/dictionary/{slug}.json (Easton full HTML + refs, per entry)
  - data/smith/index.json (Smith briefs)
  - data/isbe/index.json (ISBE briefs)
  - data/hitchcock/index.json (name meanings)

Script: scripts/bp-e3.py
Run: python3 scripts/bp-e3.py
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
    "eshtemoa": {
        "id": "eshtemoa",
        "term": "Eshtemoa",
        "category": "places",
        "intro": "<p>Eshtemoa (meaning <em>the bosom of a woman</em> or <em>obedience</em>) was a Levitical city in the hill country of Judah, assigned to the Kohathite Levites from the territory of Judah (Joshua 21:14; 1 Chronicles 6:57). It is listed among the cities of Judah in the Shephelah (Joshua 15:50) and was one of the towns to which David sent spoil after his victory over the Amalekites during his time at Ziklag (1 Samuel 30:28). The site is generally identified with modern es-Samu, a village about nine miles south of Hebron. The name was also borne by a man, a descendant of Judah through the line of Caleb (1 Chronicles 4:17, 19).</p>",
        "hitchcock_meaning": "the bosom of a woman",
        "source_ids": {"easton": "eshtemoa", "smith": "eshtemoa", "isbe": "eshtemoa"},
        "key_refs": ["Joshua 21:14", "1 Chronicles 6:57", "1 Samuel 30:28"],
        "sections": []
    },
    "espouse": {
        "id": "espouse",
        "term": "Espouse",
        "category": "concepts",
        "intro": "<p>To espouse in Scripture means to betroth or pledge in marriage — a formal legal commitment carrying nearly the same legal weight as marriage itself in ancient Israel and the Near East. In Hebrew law, a betrothed woman was treated as a wife for purposes of the law: violation of a betrothed virgin was equivalent to adultery (Deuteronomy 22:23–27). David was betrothed (espoused) to Michal (2 Samuel 3:14), and Jeremiah speaks of the LORD's covenant relationship with Israel as a time of betrothal (Jeremiah 2:2). Mary was espoused to Joseph when the angel appeared to announce the conception of Jesus (Matthew 1:18). Paul uses the imagery of betrothal when he writes that he has presented the Corinthians as a pure bride to one husband, Christ (2 Corinthians 11:2).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "espouse"},
        "key_refs": ["2 Samuel 3:14", "Matthew 1:18", "2 Corinthians 11:2"],
        "sections": []
    },
    "essenes": {
        "id": "essenes",
        "term": "Essenes",
        "category": "concepts",
        "intro": "<p>The Essenes were a Jewish ascetic movement that flourished approximately from 150 B.C. to A.D. 70, characterized by communal living, ritual purity, celibacy (in some groups), shared property, and intense study of Scripture and law. They are not mentioned by name in the New Testament but are known from the Jewish historians Josephus and Philo and from the Dead Sea Scrolls discovered at Qumran, which most scholars associate with an Essene or Essene-related community. The Essenes rejected the Jerusalem temple establishment as corrupt and anticipated a coming messianic age. Possible New Testament allusions include passages addressing asceticism and angel worship (Colossians 2:8, 18, 23) and sayings about celibacy (Matthew 19:11–12). John the Baptist's desert ministry and lifestyle has often been compared to Essene practice, though a direct connection is debated.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "essenes", "smith": "essenes", "isbe": "essenes"},
        "key_refs": ["Matthew 19:11", "Colossians 2:8", "Colossians 2:18"],
        "sections": []
    },
    "esther": {
        "id": "esther",
        "term": "Esther",
        "category": "people",
        "intro": "<p>Esther (meaning <em>hidden</em> or <em>secret</em>, or possibly Persian <em>star</em>) was a Jewish woman who became queen of the Persian empire and saved her people from genocide. Born Hadassah (myrtle), she was the cousin and adoptive daughter of Mordecai, a Benjaminite exile in Susa. When King Ahasuerus (Xerxes I) deposed Queen Vashti, Esther was selected from among the women of the empire to replace her, keeping her Jewish identity secret at Mordecai's direction (Esther 2:7, 10). When the royal official Haman plotted the destruction of all Jews in the empire, Mordecai urged Esther to intercede, famously saying: \"Who knows whether you have not come to the kingdom for such a time as this?\" (Esther 4:14). At great personal risk she approached the king unbidden, secured his favor, and exposed Haman's plot, leading to his execution and the deliverance of the Jews. The annual Feast of Purim commemorates this deliverance.</p>",
        "hitchcock_meaning": "secret; hidden",
        "source_ids": {"easton": "esther", "smith": "esther", "isbe": "esther"},
        "key_refs": ["Esther 2:7", "Esther 4:14", "Esther 7:3"],
        "sections": []
    },
    "esther-book-of": {
        "id": "esther-book-of",
        "term": "Esther, Book of",
        "category": "concepts",
        "intro": "<p>The Book of Esther is a historical narrative set in the Persian court of Ahasuerus (Xerxes I, 486–465 B.C.) and tells the story of how the Jewish people in the diaspora were preserved from extermination through the courage of Esther and the wisdom of Mordecai. The book is distinctive in the Hebrew Bible for never explicitly mentioning God's name, yet the providential working of God through seemingly coincidental events is evident throughout. It provides the scriptural basis for the Jewish feast of Purim (Esther 9:20–32). The book's place in the canon was debated in early Judaism (the Qumran community appears not to have used it), and it is quoted nowhere in the New Testament. Nevertheless its themes of divine providence, covenant faithfulness, and deliverance of the persecuted have made it central to Jewish identity through the centuries.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "esther-book-of", "smith": "esther-book-of", "isbe": "esther-book-of"},
        "key_refs": ["Esther 9:20", "Esther 4:14"],
        "sections": []
    },
    "etam": {
        "id": "etam",
        "term": "Etam",
        "category": "places",
        "intro": "<p>Etam (meaning <em>their bird</em> or <em>their covering</em>) is the name of several places in the Old Testament. (1.) A rock or cave in Judah where Samson took refuge after slaying the Philistines at Lehi; from there the Judahites bound him and delivered him to the Philistines (Judges 15:8, 11). (2.) A village in the territory of Simeon listed in 1 Chronicles 4:32. (3.) A town in Judah fortified by Rehoboam (2 Chronicles 11:6), possibly to be identified with Ain Atan near Bethlehem, associated in later tradition with King Solomon's gardens and pools. The name also occurs as a man's name in the Judahite genealogy (1 Chronicles 4:3).</p>",
        "hitchcock_meaning": "their bird, their covering",
        "source_ids": {"easton": "etam", "smith": "etam", "isbe": "etam"},
        "key_refs": ["Judges 15:8", "1 Chronicles 4:32", "2 Chronicles 11:6"],
        "sections": []
    },
    "eternal-death": {
        "id": "eternal-death",
        "term": "Eternal Death",
        "category": "concepts",
        "intro": "<p>Eternal death in Scripture designates the final, irreversible judgment of the unrepentant — the ultimate consequence of sin and the antithesis of eternal life. It is variously described as everlasting punishment (Matthew 25:46), eternal fire prepared for the devil and his angels (Matthew 25:41), everlasting destruction away from the presence of the Lord (2 Thessalonians 1:9), the second death (Revelation 20:14; 21:8), and eternal judgment (Hebrews 6:2). The phrase \"eternal\" (<em>aiōnios</em>) modifies both \"life\" and \"punishment\" in Matthew 25:46 with identical grammatical force, establishing their parallel durations. Eternal death is thus not annihilation but ongoing existence in separation from the life of God — the ultimate fulfillment of sin's logic of choosing self over God. Its reality is one of Scripture's most sobering and consistently repeated warnings.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "eternal-death"},
        "key_refs": ["Matthew 25:46", "2 Thessalonians 1:9", "Revelation 20:14"],
        "sections": []
    },
    "eternal-life": {
        "id": "eternal-life",
        "term": "Eternal Life",
        "category": "concepts",
        "intro": "<p>Eternal life in Scripture encompasses far more than unending duration: it is the quality of life belonging to the age to come, the life of God himself shared with redeemed humanity. The Old Testament glimpses it in Daniel 12:2, where the resurrection leads some to \"everlasting life.\" In John's Gospel, eternal life is repeatedly defined in personal rather than temporal terms — it is knowing the Father and the Son (John 17:3), a present possession that begins at conversion (John 5:24; 1 John 3:14) and reaches fullness in the resurrection. Jesus describes it as the goal of true discipleship (Matthew 19:29; Mark 10:17) and promises that those who believe in him will never perish but have eternal life (John 3:16; 10:28). Paul frames it as the free gift of God in contrast to the wages of sin, which is death (Romans 6:23), and as the future inheritance secured by the Spirit (Titus 3:7).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "eternal-life"},
        "key_refs": ["Daniel 12:2", "John 3:16", "John 17:3", "Romans 6:23"],
        "sections": []
    },
    "eth-baal": {
        "id": "eth-baal",
        "term": "Eth-baal",
        "category": "people",
        "intro": "<p>Eth-baal (meaning <em>with Baal</em> or <em>Baal is with him</em>) was the king of Sidon and father of Jezebel, whose marriage to Ahab king of Israel introduced Baal worship as a state religion into the northern kingdom (1 Kings 16:31). Josephus identifies him as a priest of Astarte who seized the Sidonian throne by murdering his predecessor, and names him Ithobalus. His daughter Jezebel's ruthless promotion of Baal and Asherah worship and her persecution of the prophets of the LORD made the Eth-baal connection one of the most consequential foreign political alliances in Israel's history, setting the stage for Elijah's ministry and the subsequent religious crises of the north.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "eth-baal"},
        "key_refs": ["1 Kings 16:31"],
        "sections": []
    },
    "etham": {
        "id": "etham",
        "term": "Etham",
        "category": "places",
        "intro": "<p>Etham (meaning <em>their strength</em> or <em>their sign</em>) was the second stopping place of the Israelites after leaving Egypt, at the edge of the wilderness (Exodus 13:20; Numbers 33:6–8). It was located at the eastern edge of the Nile delta region, where the cultivated land of Egypt gave way to the desert of the Sinai Peninsula. From Etham the Israelites were redirected to encamp before Pi-hahiroth, between Migdol and the sea, in the episode leading to the crossing of the Red Sea. The exact location of Etham remains uncertain, but it is associated with the ancient fortification line guarding Egypt's eastern frontier.</p>",
        "hitchcock_meaning": "their strength; their sign",
        "source_ids": {"easton": "etham", "smith": "etham", "isbe": "etham"},
        "key_refs": ["Exodus 13:20", "Numbers 33:6"],
        "sections": []
    },
    "ethan": {
        "id": "ethan",
        "term": "Ethan",
        "category": "people",
        "intro": "<p>Ethan (meaning <em>strong</em> or <em>the gift of the island</em>) is the name of several men in the Old Testament. (1.) Ethan the Ezrahite, a man of renowned wisdom against whom Solomon's superior wisdom was measured (1 Kings 4:31), credited with composing Psalm 89. He was a son of Zerah of the tribe of Judah (1 Chronicles 2:6). (2.) A Levite of the family of Gershon, an ancestor of Asaph (1 Chronicles 6:42). (3.) Ethan son of Kishi (also called Kushaiah), a Levite musician appointed by David to serve before the ark, playing the bronze cymbals in the processional (1 Chronicles 6:44; 15:17–19). He may be the same as Jeduthun, one of the three chief musicians. These men of Ethan's skill in music and wisdom made the name a byword for excellence.</p>",
        "hitchcock_meaning": "strong; the gift of the island",
        "source_ids": {"easton": "ethan", "smith": "ethan", "isbe": "ethan"},
        "key_refs": ["1 Kings 4:31", "1 Chronicles 6:44", "1 Chronicles 15:17"],
        "sections": []
    },
    "ethanim": {
        "id": "ethanim",
        "term": "Ethanim",
        "category": "concepts",
        "intro": "<p>Ethanim (meaning <em>strong</em> or <em>valiant</em>, possibly from <em>perennial streams</em>) was the seventh month of the ancient Hebrew sacred calendar, corresponding to the later Babylonian name Tishri, spanning approximately September–October. It is mentioned by name in 1 Kings 8:2 as the month in which Solomon assembled all Israel to Jerusalem for the dedication of the temple and the transfer of the ark. The month contained the great autumn festivals: the Feast of Trumpets (Rosh Hashanah) on the first day, the Day of Atonement on the tenth, and the Feast of Tabernacles from the fifteenth to the twenty-second. After the Babylonian exile, the month was regularly called Tishri, the name still used in the Jewish calendar.</p>",
        "hitchcock_meaning": "strong; valiant",
        "source_ids": {"easton": "ethanim", "smith": "ethanim", "isbe": "ethanim"},
        "key_refs": ["1 Kings 8:2"],
        "sections": []
    },
    "ethiopia": {
        "id": "ethiopia",
        "term": "Ethiopia",
        "category": "places",
        "intro": "<p>Ethiopia (Greek, <em>land of burnt faces</em>) is the rendering of the Hebrew <em>Cush</em> throughout the Old Testament, denoting the region south of Egypt along the Nile, corresponding roughly to modern Sudan and northern Ethiopia. One of the rivers of Eden flowed through the land of Cush (Genesis 2:13), and Cush was a son of Ham (Genesis 10:6). Ethiopia figures in the Table of Nations as an early civilization and appears throughout the prophets as a distant power allied with or threatened alongside Egypt. Its armies were formidable — Zerah the Ethiopian commanded a million-man army against Asa of Judah (2 Chronicles 14:9). The prophets envision Ethiopia's ultimate submission to the LORD (Psalm 68:31; 87:4; Isaiah 45:14; Zephaniah 3:10). The Ethiopian eunuch's conversion (Acts 8:27–39) was an early fulfillment of this prophetic vision, bringing the gospel to sub-Saharan Africa.</p>",
        "hitchcock_meaning": "blackness; heat",
        "source_ids": {"easton": "ethiopia", "smith": "ethiopia", "isbe": "ethiopia"},
        "key_refs": ["Genesis 2:13", "2 Kings 19:9", "Psalms 68:31", "Acts 8:27"],
        "sections": []
    },
    "ethiopian-eunuch": {
        "id": "ethiopian-eunuch",
        "term": "Ethiopian Eunuch",
        "category": "people",
        "intro": "<p>The Ethiopian eunuch was a high official — the treasurer — of Candace, queen of Ethiopia, who had come to Jerusalem to worship and was returning by chariot when Philip the evangelist was sent by the Spirit to meet him (Acts 8:26–40). He was reading aloud from Isaiah 53 when Philip came alongside and explained that the passage referred to Jesus. Upon Philip's instruction he believed and was baptized, and the Spirit immediately carried Philip away. The eunuch's conversion is one of the most significant episodes in the early chapters of Acts: it represents the gospel's first recorded witness to sub-Saharan Africa, fulfills Isaiah's prophecy that eunuchs who love God will have a name better than sons and daughters (Isaiah 56:3–5), and anticipates the Spirit's continued dissolution of ethnic and geographic boundaries in Acts 10–11. Ethiopian Christian tradition regards this unnamed man as the founder of the Ethiopian church.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ethiopian-eunuch", "isbe": "ethiopian-eunuch"},
        "key_refs": ["Acts 8:27", "Acts 8:38", "Isaiah 53:7"],
        "sections": []
    },
    "ethiopian-woman": {
        "id": "ethiopian-woman",
        "term": "Ethiopian Woman",
        "category": "people",
        "intro": "<p>The Ethiopian (Cushite) woman is mentioned in Numbers 12:1 as the wife Moses had taken — or possibly the woman he took in addition to Zipporah — whose marriage provoked the complaint of Miriam and Aaron. God's rebuke of Miriam and Aaron for this criticism, and Miriam's subsequent leprosy, is often interpreted as a divine vindication of Moses's marriage and a rebuke of ethnic prejudice. Some scholars identify the Ethiopian woman with Zipporah herself (a Midianite, and Midian was sometimes associated with Cush), but most treat her as a distinct person. The episode is the only recorded domestic conflict in Moses's married life and emphasizes that divine appointment, not ethnic purity, was the criterion for prophetic leadership.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ethiopian-woman", "smith": "ethiopian-woman", "isbe": "ethiopian-woman"},
        "key_refs": ["Numbers 12:1"],
        "sections": []
    },
    "eunice": {
        "id": "eunice",
        "term": "Eunice",
        "category": "people",
        "intro": "<p>Eunice (meaning <em>good victory</em>) was the mother of Timothy and the daughter of Lois, both remembered for their sincere faith (2 Timothy 1:5). She was a Jewish woman who had married a Greek (Acts 16:1), and it was she who, alongside her mother Lois, nurtured Timothy in the Scriptures from infancy (2 Timothy 3:15). When Paul met Timothy at Lystra on his second missionary journey, Timothy's reputation among the brethren was already well established. Paul's reference to the faith that \"dwelt first in your grandmother Lois and your mother Eunice\" (2 Timothy 1:5) makes Eunice and Lois the New Testament's most explicit example of faith transmitted across generations through the instruction of women in the home.</p>",
        "hitchcock_meaning": "good victory",
        "source_ids": {"easton": "eunice", "smith": "eunice", "isbe": "eunice"},
        "key_refs": ["Acts 16:1", "2 Timothy 1:5", "2 Timothy 3:15"],
        "sections": []
    },
    "eunuch": {
        "id": "eunuch",
        "term": "Eunuch",
        "category": "concepts",
        "intro": "<p>A eunuch in the ancient world was typically a castrated male employed in royal households as a court official, chamberlain, or guardian of the harem — a practice common in Assyrian, Babylonian, Persian, and other Near Eastern courts. In Scripture the term sometimes retains its literal meaning (2 Kings 9:32; Esther 2:3, 15; Isaiah 56:3–5) and sometimes designates a court official without necessarily implying castration (Daniel 1:3, 7–18). The Mosaic law excluded eunuchs from the assembly (Deuteronomy 23:1), a restriction explicitly overturned in Isaiah 56:3–5, which promises eunuchs who keep the Sabbath and hold fast the covenant a memorial name better than sons and daughters. Jesus uses the term in Matthew 19:12 in three metaphorical senses — those born so, those made so by others, and those who choose celibacy for the sake of the kingdom — commending the latter as a gift to those able to receive it.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "eunuch", "smith": "eunuch", "isbe": "eunuch"},
        "key_refs": ["Deuteronomy 23:1", "Isaiah 56:3", "Matthew 19:12", "Acts 8:27"],
        "sections": []
    },
    "euodias": {
        "id": "euodias",
        "term": "Euodia",
        "category": "people",
        "intro": "<p>Euodia (KJV: Euodias; meaning <em>sweet scent</em> or <em>prosperous journey</em>) was a woman in the church at Philippi whom Paul urges by name to be reconciled with Syntyche, another woman in the same congregation (Philippians 4:2). He describes both women as having \"labored side by side with me in the gospel together with Clement and the rest of my fellow workers\" — language suggesting significant ministry partnership. The dispute between Euodia and Syntyche was evidently significant enough to threaten the unity of the Philippian church and to merit Paul's personal intervention by name from prison. Their roles as co-laborers in the gospel are among the clearest New Testament evidence for women's active participation in the missionary work of the early church.</p>",
        "hitchcock_meaning": "sweet scent",
        "source_ids": {"easton": "euodias", "smith": "euodias"},
        "key_refs": ["Philippians 4:2"],
        "sections": []
    },
    "euphrates": {
        "id": "euphrates",
        "term": "Euphrates",
        "category": "places",
        "intro": "<p>The Euphrates (Hebrew <em>Perath</em>, meaning <em>that makes fruitful</em>) is the longest and most significant river of western Asia, rising in the mountains of eastern Turkey, flowing some 1,700 miles through Syria and Iraq, and emptying into the Persian Gulf. It is one of the four rivers of Eden (Genesis 2:14) and formed the northeastern boundary of the land promised to Abraham (Genesis 15:18; Deuteronomy 1:7; 11:24). It is referred to throughout the Old Testament simply as \"the River\" or \"the great river.\" The Euphrates marked the boundary between Assyrian and Egyptian spheres of influence, and it was at Carchemish on this river that Nebuchadnezzar destroyed the Egyptian army in 605 B.C. In Revelation, the drying up of the Euphrates to prepare the way of the kings from the east is one of the eschatological signs of the sixth bowl judgment (Revelation 16:12).</p>",
        "hitchcock_meaning": "that makes fruitful",
        "source_ids": {"easton": "euphrates", "smith": "euphrates", "isbe": "euphrates"},
        "key_refs": ["Genesis 2:14", "Genesis 15:18", "Deuteronomy 1:7", "Revelation 16:12"],
        "sections": []
    },
    "euroclydon": {
        "id": "euroclydon",
        "term": "Euroclydon",
        "category": "concepts",
        "intro": "<p>Euroclydon (also rendered Euraquilo in some manuscripts) was the violent northeastern storm that struck the ship carrying Paul to Rome, driving it off course and ultimately causing the shipwreck on the island of Malta (Acts 27:14). The name combines the Greek <em>euros</em> (east wind) and <em>klydon</em> (a wave), describing a tempestuous north-northeast wind that stirred up severe seas in the Mediterranean. Ancient sailors in the Mediterranean feared this seasonal storm, which could develop rapidly in autumn and drove vessels helplessly before it. The account of Paul's sea voyage and shipwreck in Acts 27 is considered one of the most vivid and nautically accurate storm narratives in ancient literature.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "euroclydon", "smith": "euroclydon"},
        "key_refs": ["Acts 27:14"],
        "sections": []
    },
    "eutychus": {
        "id": "eutychus",
        "term": "Eutychus",
        "category": "people",
        "intro": "<p>Eutychus (meaning <em>happy</em> or <em>fortunate</em>) was a young man of Troas who fell asleep during Paul's extended teaching late into the night and fell from a third-story window, being taken up dead (Acts 20:9). Paul went down, embraced him, and declared that his life was in him — and the young man was found alive. The episode occurred during a Sunday evening gathering at which the church broke bread and Paul spoke until midnight. The miracle closely parallels Elijah's raising of the widow's son (1 Kings 17:21) and Elisha's restoration of the Shunammite's son (2 Kings 4:34). It is the final miracle recorded in Paul's missionary journeys and confirms his apostolic authority. Ironically, the young man's name (<em>fortunate</em>) proved apt in the end.</p>",
        "hitchcock_meaning": "happy; fortunate",
        "source_ids": {"easton": "eutychus", "smith": "eutychus", "isbe": "eutychus"},
        "key_refs": ["Acts 20:9"],
        "sections": []
    },
    "evangelist": {
        "id": "evangelist",
        "term": "Evangelist",
        "category": "concepts",
        "intro": "<p>Evangelist (from Greek <em>euangelistēs</em>, publisher of good news) designates a ministry office or function in the early church focused on the itinerant proclamation of the gospel to those who had not yet heard it. It is listed alongside apostles, prophets, shepherds, and teachers among the gifts Christ gave to his church for its edification (Ephesians 4:11). Philip the deacon is explicitly called an evangelist (Acts 21:8) and his ministry in Samaria, with the Ethiopian eunuch, and along the coastal cities exemplifies the evangelistic function. Paul exhorts Timothy to \"do the work of an evangelist\" (2 Timothy 4:5), suggesting it is a role that could be exercised by those not formally designated by the title. Evangelists were thus primarily missionary preachers who planted the gospel in new territory, as distinguished from pastors who settled and shepherded established congregations.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "evangelist", "smith": "evangelist", "isbe": "evangelist"},
        "key_refs": ["Ephesians 4:11", "Acts 21:8", "2 Timothy 4:5"],
        "sections": []
    },
    "eve": {
        "id": "eve",
        "term": "Eve",
        "category": "people",
        "intro": "<p>Eve (Hebrew <em>Chavvah</em>, meaning <em>living</em> or <em>life-giver</em>) was the first woman, formed by God from Adam's rib while he slept and brought to him as a partner and companion (Genesis 2:21–22). Adam named her Woman (<em>ishah</em>) upon their first meeting, recognizing her as \"bone of my bones and flesh of my flesh\" (Genesis 2:23), and later called her Eve, \"because she was the mother of all living\" (Genesis 3:20). In the Garden of Eden she was deceived by the serpent and ate the forbidden fruit, then gave to Adam who also ate — an act that brought sin, shame, and death into human experience (Genesis 3:1–7). God pronounced the first gospel promise in response, that the offspring of the woman would crush the serpent's head (Genesis 3:15). She bore Cain and Abel and later Seth (Genesis 4:1–2; 25). Paul cites her deception as both historical event and theological paradigm (2 Corinthians 11:3; 1 Timothy 2:13–14).</p>",
        "hitchcock_meaning": "living; enlivening",
        "source_ids": {"easton": "eve", "smith": "eve"},
        "key_refs": ["Genesis 2:21", "Genesis 3:20", "Genesis 3:15", "2 Corinthians 11:3"],
        "sections": []
    },
    "evening": {
        "id": "evening",
        "term": "Evening",
        "category": "concepts",
        "intro": "<p>Evening in the Hebrew day marked the beginning of the new day, since the biblical reckoning ran from sunset to sunset following the creation account's pattern of \"evening and morning\" (Genesis 1:5, 8, 13). The Hebrew word <em>erev</em> (twilight, evening) designated the period between sunset and full darkness. Sacrificial offerings were made at evening — the second daily burnt offering was at the ninth hour (approximately 3 p.m.), which coincided with \"between the evenings\" (Exodus 16:12; Leviticus 23:5). The Passover lamb was slain at this time. Evening also appears in Jesus's parable of the householder who hired workers throughout the day and paid them at evening (Matthew 20:1–8). Mark 13:35 names evening as one of the four night-watches (evening, midnight, cockcrow, dawn) when the master might return.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "evening"},
        "key_refs": ["Genesis 1:5", "Leviticus 23:5", "Mark 13:35"],
        "sections": []
    },
    "everlasting": {
        "id": "everlasting",
        "term": "Everlasting",
        "category": "concepts",
        "intro": "<p>Everlasting (Hebrew <em>olam</em>, Greek <em>aiōnios</em>) in Scripture denotes enduring permanence — from age to age, without defined end. It is used of God himself: the \"everlasting God\" (<em>El Olam</em>, Genesis 21:33; Deuteronomy 33:27; Psalm 90:2), whose years are without end and who existed before creation. Divine covenant commitments are described as everlasting: the Noahic covenant (Genesis 9:16), the Abrahamic covenant (Genesis 17:7–8), and the Davidic covenant (2 Samuel 23:5). The gates of Jerusalem will be open everlastingly to receive the tribute of nations (Isaiah 60:11). The messianic kingdom is an everlasting dominion (Daniel 7:14). In the New Testament, <em>aiōnios</em> qualifies both the life of the redeemed and the punishment of the lost with identical force (Matthew 25:46), establishing the symmetrical eternality of both destinies.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "everlasting", "isbe": "everlasting"},
        "key_refs": ["Genesis 21:33", "Deuteronomy 33:27", "Psalms 90:2", "Daniel 7:14"],
        "sections": []
    },
    "evil-eye": {
        "id": "evil-eye",
        "term": "Evil Eye",
        "category": "concepts",
        "intro": "<p>The evil eye in Scripture is a metaphorical expression for stinginess, envy, or malice — not the superstitious belief in a literal harmful gaze common in ancient Near Eastern folk religion. Deuteronomy 15:9 warns against the \"evil eye\" (KJV: \"wicked thought\") toward a poor brother in the sabbatical year, meaning a begrudging refusal to lend. Proverbs 23:6 counsels against eating with a stingy man who has an evil eye. Jesus uses the expression in Matthew 20:15 (\"Is your eye evil because I am good?\") to describe envy of others' generosity, and in Matthew 6:23 (\"If your eye is evil, your whole body will be full of darkness\") to describe a mean-spirited or distorted moral vision that darkens one's whole outlook. The idiom is thus consistently connected to attitudes of covetousness, envy, and hardheartedness rather than magical harm.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "evil-eye", "isbe": "evil-eye"},
        "key_refs": ["Proverbs 23:6", "Deuteronomy 15:9", "Matthew 20:15"],
        "sections": []
    },
    "evil-merodach": {
        "id": "evil-merodach",
        "term": "Evil-merodach",
        "category": "people",
        "intro": "<p>Evil-merodach (meaning <em>the fool of Merodach</em> or <em>man of Marduk</em>) was the son and successor of Nebuchadnezzar as king of Babylon, reigning approximately 562–560 B.C. He is noted in Scripture for releasing Jehoiachin, the exiled king of Judah, from prison in the first year of his reign, speaking kindly to him, giving him a seat of honor above all other captive kings, and supplying him with a regular allowance for the rest of his life (2 Kings 25:27–30; Jeremiah 52:31–34). This act of royal favor to Jehoiachin was theologically significant: it preserved the Davidic line during the exile and provided a tangible token that God had not abandoned his covenant with David. Evil-merodach was killed in a conspiracy led by his brother-in-law Neriglissar after only two years of reign.</p>",
        "hitchcock_meaning": "the fool of Merodach; the fool grinds bitterly",
        "source_ids": {"easton": "evil-merodach", "isbe": "evil-merodach"},
        "key_refs": ["2 Kings 25:27", "Jeremiah 52:31"],
        "sections": []
    },
    "evil-speaking": {
        "id": "evil-speaking",
        "term": "Evil-speaking",
        "category": "concepts",
        "intro": "<p>Evil-speaking in the New Testament refers broadly to the sins of the tongue — slander, defamation, blasphemy, and speaking maliciously about others. Titus 3:2 commands believers to \"speak evil of no one,\" placing it alongside quarreling and hostility as behaviors incompatible with Christian conduct. James 4:11 warns against speaking evil of one's brother, arguing that to do so is to speak evil of the law and to set oneself up as judge. Paul includes <em>blasphemos</em> (evil-speaking, slander) in lists of sins that characterize the ungodly (1 Corinthians 5:11; 6:10). Peter calls believers to put away all evil-speaking (1 Peter 2:1). The consistent New Testament emphasis is that the tongue's power for evil is a particular test of genuine faith (James 3:1–12) and that the new life in Christ is to be marked by gracious, edifying speech.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "evil-speaking", "isbe": "evil-speaking"},
        "key_refs": ["Titus 3:2", "James 4:11", "1 Peter 2:1"],
        "sections": []
    },
    "example": {
        "id": "example",
        "term": "Example",
        "category": "concepts",
        "intro": "<p>Example in Scripture functions both as a pattern to follow and as a warning to avoid. Christ set the supreme positive example: \"I have given you an example, that you also should do just as I have done to you\" (John 13:15), said as he washed the disciples' feet. Paul repeatedly invites imitation of his own conduct as it reflects Christ (Philippians 3:17; 2 Thessalonians 3:9; 1 Corinthians 11:1), and calls Timothy and Titus to be examples to their congregations in speech, conduct, love, faith, and purity (1 Timothy 4:12; Titus 2:7). Peter urges elders to serve not for gain but as examples to the flock (1 Peter 5:3). The negative use is equally prominent: Israel's wilderness failures serve as examples of what to avoid (1 Corinthians 10:11), and Peter describes the punishment of Sodom and Gomorrah as \"an example\" of the judgment coming upon the ungodly (2 Peter 2:6).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "example", "isbe": "example"},
        "key_refs": ["John 13:15", "1 Peter 5:3", "1 Corinthians 10:11"],
        "sections": []
    },
    "executioner": {
        "id": "executioner",
        "term": "Executioner",
        "category": "concepts",
        "intro": "<p>Executioner in the New Testament (Greek <em>spekoulator</em>, from Latin <em>speculator</em>, a scout or guard) refers to the soldier of Herod Antipas's bodyguard sent to behead John the Baptist in the prison at Machaerus following Herod's rash oath to the dancing daughter of Herodias (Mark 6:27). The term <em>speculator</em> described a royal bodyguard who also performed executions on the king's order, similar to the Persian royal executioners. In the Old Testament context, executions were typically carried out by stoning (Leviticus 24:14; John 8:5) or by the sword, often by a designated official or by the community collectively. The figure of the executioner underscores both the arbitrary power of Herodian rule and the cost of prophetic faithfulness.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "executioner", "smith": "executioner"},
        "key_refs": ["Mark 6:27"],
        "sections": []
    },
    "exercise-bodily": {
        "id": "exercise-bodily",
        "term": "Exercise, Bodily",
        "category": "concepts",
        "intro": "<p>Bodily exercise is addressed by Paul in 1 Timothy 4:8: \"Bodily exercise profits a little, but godliness is profitable for all things, having promise of the life that now is and of that which is to come.\" The statement does not denigrate physical training but relativizes it: it has some benefit, but spiritual discipline yields benefits in both this age and the age to come. The comparison draws on Greco-Roman athletic culture familiar to Timothy's Ephesian context, where gymnasium exercise was a significant aspect of civic life. Paul's athletic metaphors elsewhere (1 Corinthians 9:25–27; 2 Timothy 2:5) similarly use physical training as a positive analogy for spiritual effort, suggesting his point here is one of proportion and priority rather than contempt for the body.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "exercise-bodily"},
        "key_refs": ["1 Timothy 4:8"],
        "sections": []
    },
    "exile": {
        "id": "exile",
        "term": "Exile",
        "category": "events",
        "intro": "<p>Exile in the biblical narrative refers principally to the forced removal of Israel's population from their land as a covenant curse for persistent apostasy, most fully realized in the Assyrian deportation of the northern kingdom (722/721 B.C.) and the Babylonian deportation of Judah in three waves (605, 597, and 586 B.C.). The prophets interpreted exile not merely as military defeat but as the LORD himself driving his people out of his land in fulfillment of the covenant warnings of Leviticus 26 and Deuteronomy 28. Yet they equally proclaimed a coming restoration: Israel would be brought back, the land renewed, and a new covenant established (Jeremiah 31:31–34; Ezekiel 36:24–28; Isaiah 40–55). The New Testament frames the return from exile as only partially fulfilled and envisions a deeper, cosmic exile from God addressed by the gospel of Christ's death and resurrection (Luke 4:18–19; 2 Corinthians 5:19–20).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "exile", "isbe": "exile"},
        "key_refs": ["2 Kings 17:6", "2 Kings 25:11", "Jeremiah 31:31"],
        "sections": []
    },
    "exodus": {
        "id": "exodus",
        "term": "Exodus",
        "category": "events",
        "intro": "<p>The Exodus (Greek, <em>departure</em>) was the foundational saving event of the Old Testament — the deliverance of the Israelites from Egyptian slavery under Moses through a series of ten plagues culminating in the Passover and the crossing of the Red Sea, traditionally dated around 1446 B.C. (based on the 480-year figure of 1 Kings 6:1) or alternatively in the thirteenth century B.C. The event is the defining act of God's covenant relationship with Israel: \"I am the LORD your God who brought you out of the land of Egypt, out of the house of slavery\" (Exodus 20:2; Deuteronomy 5:6). The Passover, the Red Sea crossing, the wilderness provision of manna and water, and the covenant at Sinai all belong to the Exodus complex. The prophets frame the coming restoration from Babylon as a new and greater exodus (Isaiah 43:16–21; 51:9–11). The New Testament interprets Christ's death and resurrection as the ultimate Passover and exodus — Luke records that Moses and Elijah spoke with Jesus at the transfiguration about his \"exodus\" (departure) to be accomplished at Jerusalem (Luke 9:31).</p>",
        "hitchcock_meaning": "going out, departure",
        "source_ids": {"easton": "exodus", "smith": "exodus"},
        "key_refs": ["Exodus 12:51", "Deuteronomy 26:8", "Psalms 114:1", "Luke 9:31"],
        "sections": []
    },
    "exodus-book-of": {
        "id": "exodus-book-of",
        "term": "Exodus, Book of",
        "category": "concepts",
        "intro": "<p>The Book of Exodus is the second book of the Pentateuch and the narrative of Israel's birth as a nation — from the oppression in Egypt through the ten plagues, the Passover, the Red Sea crossing, the covenant at Sinai, and the construction of the tabernacle. The Hebrew name is <em>Shemot</em> (\"names\"), from its opening words; the Greek name Exodus (\"departure\") reflects its central event. Its two major sections are the narrative of redemption (chapters 1–18) and the giving of the law and building of the tabernacle (chapters 19–40). The Decalogue (chapters 20), the book of the covenant (chapters 20–23), and the detailed instructions for the tabernacle (chapters 25–31, 35–40) together constitute a foundational document for Israel's worship, ethics, and national identity. Galatians 3:17 notes that the law came 430 years after the Abrahamic promise, a figure deriving from the Exodus chronology (Exodus 12:40–41).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "exodus-book-of"},
        "key_refs": ["Galatians 3:17"],
        "sections": []
    },
    "exorcist": {
        "id": "exorcist",
        "term": "Exorcist",
        "category": "concepts",
        "intro": "<p>Exorcists in the ancient world were practitioners who claimed the ability to cast out evil spirits through rituals, incantations, and invocations of divine names. Jewish exorcism is attested in Second Temple sources; Jesus acknowledged that Jewish exorcists (\"your sons\") cast out demons (Matthew 12:27; Luke 11:19), and the seven sons of Sceva are described as Jewish exorcists who attempted to use Jesus's name without personal relationship or authority (Acts 19:13–16). The evil spirit's response — \"Jesus I know, and Paul I recognize, but who are you?\" — followed by a violent attack — underscored that genuine authority over evil spirits resided not in the name as a formula but in apostolic commission. Jesus himself was accused of casting out demons by Beelzebul (Matthew 12:24), to which he responded by pointing to his exorcisms as evidence of the kingdom's arrival (Matthew 12:28).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "exorcist", "smith": "exorcist"},
        "key_refs": ["Acts 19:13", "Matthew 12:27", "Mark 9:38"],
        "sections": []
    },
    "expiation": {
        "id": "expiation",
        "term": "Expiation",
        "category": "concepts",
        "intro": "<p>Expiation refers to the removal of guilt and defilement through the payment of a penalty or the offering of a substitute — the objective aspect of atonement focused on dealing with sin itself rather than satisfying divine wrath (which is termed <em>propitiation</em>). In the biblical sacrificial system, sin was expiated when the blood of the offering was applied in the manner God prescribed, covering or removing the defilement of sin. The Hebrew <em>kipper</em> (to cover, to atone) underlies the Day of Atonement rites (Leviticus 16). Modern translations often render the Greek <em>hilasmos</em> and <em>hilastērion</em> as \"expiation\" (RSV) or \"propitiation\" (ESV, NASB), a longstanding debate reflecting the question of whether Christ's atonement primarily removes sin's defilement or turns away God's wrath — most Reformed scholars arguing the two are inseparable in biblical theology. See also <strong>Atonement</strong>.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "expiation", "smith": "expiation", "isbe": "expiation"},
        "key_refs": ["Leviticus 16:6", "Romans 3:25", "1 John 2:2"],
        "sections": []
    },
    "eye": {
        "id": "eye",
        "term": "Eye",
        "category": "concepts",
        "intro": "<p>Eye in Scripture functions both as the literal organ of vision and as a rich metaphor for moral perception, desire, spiritual illumination, and divine oversight. The \"eye of the LORD\" is upon those who fear him (Psalm 33:18; 34:15), expressing his omniscient watchful care. In wisdom literature, the eye that sees and the ear that hears are both made by the LORD (Proverbs 20:12). Jesus teaches that the eye is the lamp of the body: if the eye is healthy (single, generous), the body is full of light; if the eye is evil (envious, stingy), the body is full of darkness (Matthew 6:22–23). The command not to let the eye spare in executing God's judgment (Deuteronomy 7:16; 19:13) expresses the demand for wholehearted covenant obedience. In Numbers 11:7 manna is compared in appearance to the eye of bdellium. Paul prays for the eyes of the understanding to be enlightened (Ephesians 1:18).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "eye", "smith": "eye", "isbe": "eye"},
        "key_refs": ["Psalms 33:18", "Matthew 6:22", "Ephesians 1:18"],
        "sections": []
    },
    "ezekias": {
        "id": "ezekias",
        "term": "Ezekias",
        "category": "people",
        "intro": "<p>Ezekias is the Greek form of the Hebrew name Hezekiah, occurring in Matthew 1:9–10 in the genealogy of Jesus Christ, listed as the son of Ahaz and father of Manasseh in the Davidic line. For the full account of his life and reign as king of Judah, see <strong>Hezekiah</strong>. His inclusion in Matthew's genealogy is significant: Hezekiah was one of Judah's most faithful reforming kings, whose trust in God delivered Jerusalem from the Assyrian siege of Sennacherib. The Greek form Ezekias was standard in Hellenistic Jewish usage, as in the Septuagint and in the Greek New Testament.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ezekias", "smith": "ezekias", "isbe": "ezekias"},
        "key_refs": ["Matthew 1:9", "Matthew 1:10"],
        "sections": []
    },
    "ezekiel": {
        "id": "ezekiel",
        "term": "Ezekiel",
        "category": "people",
        "intro": "<p>Ezekiel (meaning <em>God will strengthen</em> or <em>the strength of God</em>) was a priest and prophet of the Babylonian exile, son of Buzi the priest, who was among the deportees carried to Babylon with King Jehoiachin in 597 B.C. (Ezekiel 1:2–3). He settled at Tel-abib on the river Chebar, a canal in Babylonia, where he received his extraordinary visions and prophetic commissions from 593 to at least 571 B.C. His ministry was roughly contemporary with Jeremiah's in Jerusalem and Daniel's in the Babylonian court. Known for his elaborate symbolic actions and visions — the four living creatures and the divine chariot (Ezekiel 1), the valley of dry bones (Ezekiel 37), and the vision of the restored temple (Ezekiel 40–48) — Ezekiel addressed both the exilic community's need for hope and the persistent idolatry that had brought judgment. His theology of individual moral responsibility (Ezekiel 18) and the promise of the new heart and new spirit (Ezekiel 36:26–27) were theologically formative for both Judaism and Christianity.</p>",
        "hitchcock_meaning": "the strength of God",
        "source_ids": {"easton": "ezekiel", "smith": "ezekiel", "isbe": "ezekiel"},
        "key_refs": ["Ezekiel 1:3", "Ezekiel 37:1", "Ezekiel 36:26"],
        "sections": []
    },
    "ezekiel-book-of": {
        "id": "ezekiel-book-of",
        "term": "Ezekiel, Book of",
        "category": "concepts",
        "intro": "<p>The Book of Ezekiel is the third of the major prophetic books, containing forty-eight chapters of oracles, symbolic actions, and visions spanning Ezekiel's ministry from 593 to c. 571 B.C. in Babylonian exile. It divides into three broad sections: oracles of judgment against Judah and Jerusalem (chapters 1–24); oracles against foreign nations — Ammon, Moab, Edom, Philistia, Tyre, Sidon, Egypt (chapters 25–32); and oracles of restoration and hope (chapters 33–48). The book's most celebrated passages include the initial throne-chariot vision (chapters 1–3), the enacted prophecies of Jerusalem's fall (chapters 4–5), the vision of the valley of dry bones as a metaphor for national restoration (chapter 37), and the detailed architectural vision of the eschatological temple (chapters 40–48). Its rich imagery and apocalyptic character deeply influenced later Jewish apocalyptic literature and the book of Revelation. Its opening vision was the basis of the <em>merkabah</em> mystical tradition in Judaism.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ezekiel-book-of"},
        "key_refs": ["Ezekiel 1:1", "Ezekiel 37:1", "Ezekiel 40:2"],
        "sections": []
    },
    "ezel": {
        "id": "ezel",
        "term": "Ezel",
        "category": "places",
        "intro": "<p>Ezel (meaning <em>going abroad</em> or <em>walk</em>) was a stone or landmark near Gibeah used as a secret meeting point and signal location in the arrangement between David and Jonathan. At Ezel, Jonathan was to shoot arrows to signal whether it was safe for David to return to Saul's court (1 Samuel 20:19). The name may refer to a particular rock formation serving as a recognized landmark in the area. The entire account of the signal system at Ezel reflects the deep covenant friendship between David and Jonathan and their ingenious means of communicating under dangerous conditions. The stone is mentioned only in this single narrative and has not been identified with a modern site.</p>",
        "hitchcock_meaning": "going abroad; walk",
        "source_ids": {"easton": "ezel", "smith": "ezel", "isbe": "ezel"},
        "key_refs": ["1 Samuel 20:19"],
        "sections": []
    },
    "ezer": {
        "id": "ezer",
        "term": "Ezer",
        "category": "people",
        "intro": "<p>Ezer (meaning <em>a help</em>) is the name of several men in the Old Testament. (1.) A son of Seir the Horite and Edomite chieftain (Genesis 36:21, 27, 30; 1 Chronicles 1:38, 42). (2.) A son of Ephraim who was killed in a cattle raid by the men of Gath while his father still lived (1 Chronicles 7:21). (3.) A Judahite from Hushah (1 Chronicles 4:4). (4.) A warrior from Gad who joined David at Ziklag (1 Chronicles 12:9). (5.) A son of Jeshua who helped repair the Jerusalem wall under Nehemiah (Nehemiah 3:19). (6.) A priest who participated in the dedication of Jerusalem's rebuilt walls under Nehemiah (Nehemiah 12:42). The name was evidently common in Israel's history.</p>",
        "hitchcock_meaning": "a help",
        "source_ids": {"easton": "ezer", "smith": "ezer", "isbe": "ezer"},
        "key_refs": ["Genesis 36:21", "1 Chronicles 7:21", "Nehemiah 3:19"],
        "sections": []
    },
    "ezion-geber": {
        "id": "ezion-geber",
        "term": "Ezion-geber",
        "category": "places",
        "intro": "<p>Ezion-geber (meaning <em>the wood of the man</em> or <em>backbone of a man</em>) was an Israelite port city at the northern tip of the Gulf of Aqaba (the eastern arm of the Red Sea), near modern Eilat in Israel. The Israelites encamped there during the wilderness wanderings (Numbers 33:35–36; Deuteronomy 2:8). Solomon built a fleet of ships at Ezion-geber with the assistance of Hiram of Tyre, sailing to Ophir for gold (1 Kings 9:26–28; 2 Chronicles 8:17–18). Jehoshaphat of Judah also built a trading fleet there, but the ships were wrecked before they could sail — interpreted as divine judgment (1 Kings 22:48–49; 2 Chronicles 20:36–37). Archaeological excavations at Tell el-Kheleifeh have revealed a significant Iron Age settlement, though its identification with Ezion-geber is debated.</p>",
        "hitchcock_meaning": "the wood of the man",
        "source_ids": {"easton": "ezion-geber", "isbe": "ezion-geber"},
        "key_refs": ["Numbers 33:35", "1 Kings 9:26", "2 Chronicles 8:17"],
        "sections": []
    },
    "ezra": {
        "id": "ezra",
        "term": "Ezra",
        "category": "people",
        "intro": "<p>Ezra (meaning <em>help</em> or <em>court</em>) was a priestly scribe of the highest lineage — a direct descendant of Aaron through Seraiah the last chief priest before the Babylonian exile (Ezra 7:1–5) — who led the second major return of Jewish exiles from Babylon to Jerusalem in 458 B.C., in the seventh year of Artaxerxes I. A \"skilled scribe in the Law of Moses\" (Ezra 7:6), he obtained from Artaxerxes a royal commission granting him authority to enforce the law of God among the Jewish community. His reforms in Jerusalem focused especially on the dissolution of marriages with foreign women (Ezra 9–10) and the public reading and exposition of the Torah in the great assembly (Nehemiah 8). Ezra is traditionally regarded as the restorer of the Scriptures after the exile, and later Jewish tradition credited him with organizing the canon and establishing the Great Synagogue. He exemplified the priestly-scribal model of piety — study, practice, and teaching of God's word (Ezra 7:10).</p>",
        "hitchcock_meaning": "help; court",
        "source_ids": {"easton": "ezra", "smith": "ezra", "isbe": "ezra"},
        "key_refs": ["Ezra 7:1", "Ezra 7:10", "Nehemiah 8:1"],
        "sections": []
    },
    "ezra-book-of": {
        "id": "ezra-book-of",
        "term": "Ezra, Book of",
        "category": "concepts",
        "intro": "<p>The Book of Ezra is a historical narrative covering the first two waves of Jewish return from Babylon to Jerusalem: the first return under Sheshbazzar and Zerubbabel (chapters 1–6, 538–516 B.C.), which resulted in the rebuilding of the temple, and the second return under Ezra himself (chapters 7–10, 458 B.C.). It was originally combined with Nehemiah as a single work and may have been composed by the same author who wrote Chronicles. The book is notable for its extensive use of Aramaic (Ezra 4:8–6:18; 7:12–26) in the official Persian correspondence, and for including authentic Persian royal decrees from Cyrus, Darius I, and Artaxerxes I. Its theological concern is the restoration of proper temple worship, Levitical order, and Torah obedience in a purified community — prefiguring the new covenant community of the New Testament. The book makes no explicit messianic claim but its entire orientation is toward the restoration of the covenant people for the fulfillment of God's promises.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ezra-book-of", "smith": "ezra-book-of"},
        "key_refs": ["Ezra 1:1", "Ezra 7:10"],
        "sections": []
    },
    "ezrahite": {
        "id": "ezrahite",
        "term": "Ezrahite",
        "category": "people",
        "intro": "<p>Ezrahite is a term appearing in the superscriptions of Psalms 88 and 89, where it describes Heman the Ezrahite (Psalm 88) and Ethan the Ezrahite (Psalm 89), both renowned for their wisdom (1 Kings 4:31; 1 Chronicles 2:6). The meaning of Ezrahite is debated: it may mean a descendant of Zerah son of Judah (connecting these men to the Judahite genealogy in 1 Chronicles 2:6), or it may be a clan designation related to an otherwise unknown ancestor. The parallel between \"sons of Mahol\" in 1 Kings 4:31 and \"sons of Zerah\" in 1 Chronicles 2:6 suggests they were Judahites, though the Levitical Heman (1 Chronicles 6:33) has been proposed as a separate individual from the Ezrahite Heman of Psalm 88. The title underscores the antiquity and prestige of these psalmists.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ezrahite", "isbe": "ezrahite"},
        "key_refs": ["1 Kings 4:31", "Psalms 89:1", "1 Chronicles 2:6"],
        "sections": []
    },
    "ezri": {
        "id": "ezri",
        "term": "Ezri",
        "category": "people",
        "intro": "<p>Ezri (meaning <em>my help</em>) was a son of Chelub appointed by David as the overseer of those who worked the royal agricultural lands (1 Chronicles 27:26). He is listed among David's officials responsible for the produce of the fields, appearing in the catalog of the twelve monthly officers who administered the affairs of the king. Beyond this single verse, nothing further is recorded of Ezri in Scripture. His role as overseer of the royal farmlands reflects the elaborate administrative organization David established for the management of the Israelite kingdom, which Solomon would inherit and expand.</p>",
        "hitchcock_meaning": "my help",
        "source_ids": {"easton": "ezri", "smith": "ezri", "isbe": "ezri"},
        "key_refs": ["1 Chronicles 27:26"],
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
    print(f'BP e3: Eshtemoa → Ezri: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
