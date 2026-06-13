"""
BP Article Synthesis — p1: Paarai → Peor
Covers Easton entries: Paarai through Peor (75 entries)

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

Script: scripts/bp-p1.py
Run: python3 scripts/bp-p1.py
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
    "paarai": {
        "id": "paarai",
        "term": "Paarai",
        "category": "people",
        "intro": "<p>Paarai (meaning: <em>opening of the Lord</em>), identified as <em>the Arbite</em>, was one of the thirty mighty men of David's elite warrior corps. He is listed in the roster of David's heroes in 2 Samuel 23:35 and appears under the variant name Naarai the son of Ezbai in 1 Chronicles 11:37. Like the others in this distinguished group, Paarai distinguished himself in battle on behalf of the king.</p><p>His designation <em>the Arbite</em> links him to Arab, a town in the hill country of Judah. Beyond his inclusion in this celebrated list, no individual exploits of Paarai are recorded in Scripture. His name stands as part of the permanent record of those who were closest to David in his military campaigns.</p>",
        "hitchcock_meaning": "opening of the Lord",
        "source_ids": {"easton": "paarai", "smith": "paarai", "isbe": "paarai"},
        "key_refs": ["2 Samuel 23:35", "1 Chronicles 11:37"]
    },
    "padan": {
        "id": "padan",
        "term": "Padan",
        "category": "places",
        "intro": "<p>Padan, meaning <em>a plain</em> or <em>table-land</em>, appears only once in Scripture (Genesis 48:7), where it serves as a shortened reference to the region of Padan-aram. Jacob uses it in recounting the death of his wife Rachel: <em>Rachel died by me in the land of Canaan in the way, when yet there was but a little way to come unto Ephrath</em>, having departed from Padan.</p><p>The name essentially designates the broad fertile plain of Mesopotamia — the upper region of the Euphrates valley in what is today northern Syria. It was the homeland of Abraham's family and the land to which he sent his servant to find a wife for Isaac. The full form, Padan-aram, appears far more commonly in the patriarchal narratives.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "padan", "smith": "padan"},
        "key_refs": ["Genesis 48:7"]
    },
    "padan-aram": {
        "id": "padan-aram",
        "term": "Padan-aram",
        "category": "places",
        "intro": "<p>Padan-aram, meaning <em>the plain of Aram</em> or <em>the plain of the highlands</em>, designates the broad fertile region of upper Mesopotamia centered on Haran in what is now northern Syria. It figures centrally in the patriarchal narratives as the homeland of Abraham's family, the land to which Abraham's servant traveled to find a bride for Isaac (Genesis 24), and the refuge to which Jacob fled from Esau (Genesis 28:2–5).</p><p>Jacob spent twenty years in Padan-aram under his uncle Laban, where he married Leah and Rachel and fathered eleven of his twelve sons. The region was thus the cradle of the tribes of Israel. The name is used interchangeably with Aram-naharaim (<em>Aram of the two rivers</em>) and Mesopotamia in different biblical texts, all referring to the same upper Euphrates plain.</p>",
        "hitchcock_meaning": "cultivated field or table-land of Syria",
        "source_ids": {"easton": "padan-aram"},
        "key_refs": ["Genesis 25:20", "Genesis 28:2", "Genesis 28:5", "Genesis 31:18"]
    },
    "pagiel": {
        "id": "pagiel",
        "term": "Pagiel",
        "category": "people",
        "intro": "<p>Pagiel (meaning: <em>God allots</em> or <em>lot of God</em>) was a prince of the tribe of Asher appointed to assist Moses in the first census of Israel in the wilderness. He is mentioned in Numbers 1:13 as the son of Ocran and appears repeatedly in the early chapters of Numbers representing Asher in the census, in the arrangement of the camp, and in the dedication offerings of the tribal leaders at the tabernacle's consecration.</p><p>As Asher's tribal chief during the wilderness period, Pagiel offered the tenth dedication offering at the tabernacle altar (Numbers 7:72). His name, emphasizing divine apportionment, reflects the Israelite conviction that tribal boundaries and leadership were assigned by God rather than by human ambition.</p>",
        "hitchcock_meaning": "lot of God",
        "source_ids": {"easton": "pagiel", "smith": "pagiel", "isbe": "pagiel"},
        "key_refs": ["Numbers 1:13", "Numbers 2:27", "Numbers 7:72", "Numbers 10:26"]
    },
    "pahath-moab": {
        "id": "pahath-moab",
        "term": "Pahath-moab",
        "category": "concepts",
        "intro": "<p>Pahath-moab, meaning <em>governor of Moab</em>, is the name of an Israelite family or clan whose ancestors apparently held some administrative connection with Moab. This family is first recorded among those who returned from the Babylonian captivity with Zerubbabel, with 2,812 members listed in Ezra 2:6. A further contingent of 200 returned with Ezra himself (Ezra 8:4).</p><p>Members of the Pahath-moab clan appear prominently in the restoration period: some had taken foreign wives and agreed to put them away at Ezra's direction (Ezra 10:30), and a Pahath-moab descendant named Hashub helped repair a section of Jerusalem's wall under Nehemiah (Nehemiah 3:11). A leader of the family sealed the covenant renewal in Nehemiah 10:14. The clan represents one of the larger lay families of the return community.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "pahath-moab", "isbe": "pahath-moab"},
        "key_refs": ["Ezra 2:6", "Ezra 8:4", "Ezra 10:30", "Nehemiah 3:11"]
    },
    "paint": {
        "id": "paint",
        "term": "Paint",
        "category": "concepts",
        "intro": "<p>The practice of painting the face and eyes was known in ancient Israel, though Scripture consistently associates it with vanity or moral reproach. Jezebel <em>painted her face</em> before confronting Jehu (2 Kings 9:30), and the prophets Jeremiah (4:30) and Ezekiel (23:40) use the image of eye-painting to characterize the seductive unfaithfulness of Israel and Judah toward foreign alliances, comparing the nation to a harlot adorning herself for lovers.</p><p>The Hebrew term <em>pukh</em> (antimony or stibium) refers to a dark powder applied around the eyes to make them appear larger and more lustrous — a cosmetic widely attested in Egyptian and Mesopotamian cultures. Wall painting, a distinct usage, also appears in Scripture: Jehoiakim's ill-advised decoration of his cedar palace with vermilion is condemned by the prophet Jeremiah (22:14) as a symbol of hollow prosperity without justice.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "paint", "smith": "paint", "isbe": "paint"},
        "key_refs": ["2 Kings 9:30", "Jeremiah 4:30", "Ezekiel 23:40", "Jeremiah 22:14"]
    },
    "palace": {
        "id": "palace",
        "term": "Palace",
        "category": "concepts",
        "intro": "<p>The word <em>palace</em> translates several Hebrew and Greek terms in Scripture, all designating a grand royal or administrative residence. The Hebrew <em>armon</em> refers to a citadel or fortified mansion, while <em>biran</em> and <em>hekal</em> describe the temple-palace complexes of ancient Near Eastern kings. David's palace in Jerusalem was built with cedar from Lebanon, and Solomon's palace complex took thirteen years to complete — longer than the seven-year construction of the temple itself (1 Kings 7:1).</p><p>The Daniel narratives use the Aramaic <em>bira</em> for the royal fortress at Shushan, and Nehemiah references it as the administrative center of Persia. In the New Testament, the Greek <em>aule</em> (courtyard or hall) is rendered palace in the accounts of Jesus's trial before Pilate and Herod. Prophetically, the palaces of Nineveh and Babylon became symbols of pride destined for judgment.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "palace", "smith": "palace", "isbe": "palace"},
        "key_refs": ["Nehemiah 1:1", "Daniel 8:2", "1 Chronicles 29:1", "Daniel 1:4"]
    },
    "palestine": {
        "id": "palestine",
        "term": "Palestine",
        "category": "places",
        "intro": "<p>Palestine, derived from <em>Philistia</em> — the land of the Philistines — is the name by which the land of Canaan came to be known in the classical and post-biblical world. In the Hebrew Bible, the term <em>Palestina</em> or <em>Philistia</em> originally designated only the coastal strip occupied by the Philistines (Exodus 15:14; Isaiah 14:29). The broader use of <em>Palestine</em> to denote the entire region west of the Jordan, from Dan to Beersheba, is a later geographical convention popularized in Greek and Roman sources.</p><p>The land is bounded by the Mediterranean Sea to the west, the Lebanon ranges to the north, the Syrian and Arabian deserts to the east, and the Sinai Peninsula to the south. Its strategic position as a land bridge between Egypt and Mesopotamia made it the crossroads of ancient civilizations and the stage for much of biblical history. Today the term encompasses modern Israel, the Palestinian territories, and portions of Jordan.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "palestine", "isbe": "palestine"},
        "key_refs": ["Exodus 15:14", "Isaiah 14:29", "Isaiah 14:31", "Joel 3:4"]
    },
    "pallu": {
        "id": "pallu",
        "term": "Pallu",
        "category": "people",
        "intro": "<p>Pallu (meaning: <em>separated</em> or <em>distinguished</em>) was the second son of Reuben, Jacob's firstborn, and thus a grandson of the patriarch Jacob. He is listed among the seventy souls who accompanied Jacob into Egypt (Genesis 46:9) and appears in the tribal census records as the founder of the Palluite family within Reuben's clan (Numbers 26:5). His son Eliab, and grandson Dathan, became notorious as two of the leaders of the Korah rebellion against Moses in the wilderness (Numbers 16).</p><p>Though Pallu himself played no prominent role, the notoriety of his descendants cast a shadow over his lineage. The tribe of Reuben, despite being Jacob's firstborn, forfeited the preeminence that might have belonged to it, a theme the biblical narrative traces from Reuben's own moral failures.</p>",
        "hitchcock_meaning": "separated, distinguished",
        "source_ids": {"easton": "pallu", "smith": "pallu"},
        "key_refs": ["Genesis 46:9", "Exodus 6:14", "Numbers 26:5", "Numbers 26:8"]
    },
    "palm-tree": {
        "id": "palm-tree",
        "term": "Palm Tree",
        "category": "concepts",
        "intro": "<p>The date palm (<em>Phoenix dactylifera</em>), designated by the Hebrew <em>tamar</em>, was among the most characteristic and valued trees of ancient Palestine. It thrives in hot, dry climates, grows to considerable height, and bears abundant fruit for decades. The palm was associated with Jericho, called <em>the city of palm trees</em> (Deuteronomy 34:3), and its abundance throughout the land symbolized the prosperity and blessing of the covenant people.</p><p>In Scripture the palm carries rich symbolic weight. Psalm 92:12 uses it as a metaphor for the flourishing of the righteous: <em>The righteous shall flourish like the palm tree</em>. Palm branches were strewn before Jesus at his triumphal entry into Jerusalem (John 12:13), recalling the festival of Tabernacles, and in Revelation 7:9 the redeemed multitude stands before the throne holding palm branches, symbols of victory and eternal joy.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "palm-tree", "smith": "palm-tree", "isbe": "palm-tree"},
        "key_refs": ["Psalms 92:12", "Deuteronomy 34:3", "Revelation 7:9", "John 12:13"]
    },
    "palm-trees-the-city-of": {
        "id": "palm-trees-the-city-of",
        "term": "Palm Trees, The City of",
        "category": "places",
        "intro": "<p>The city of palm trees is a biblical designation for Jericho, the ancient fortified city situated in the Jordan valley near the northern end of the Dead Sea. The name reflects the abundant groves of date palms for which the region was famous in antiquity. It occurs in Deuteronomy 34:3, where Moses views Jericho from Mount Nebo, and in Judges 1:16 and 3:13, where the location is referenced in connection with the Kenites and with Eglon king of Moab.</p><p>Jericho was one of the oldest continuously occupied sites in the ancient world, and its palm-laden oasis setting made it a prized agricultural and strategic center. The title <em>city of palm trees</em> evokes the lush character of the Jordan valley in contrast to the surrounding wilderness, and continued to serve as a poetic synonym for Jericho in later usage.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "palm-trees-the-city-of"},
        "key_refs": ["Deuteronomy 34:3", "Judges 1:16", "Judges 3:13"]
    },
    "palmer-worm": {
        "id": "palmer-worm",
        "term": "Palmer-worm",
        "category": "concepts",
        "intro": "<p>The palmer-worm translates the Hebrew <em>gazam</em>, one of several insect terms in the prophetic literature associated with devastating agricultural plagues. The term appears in Joel 1:4, where four different destructive insects — the palmer-worm, the locust, the cankerworm, and the caterpillar — are named as agents of a comprehensive devastation of crops: <em>That which the palmer-worm hath left hath the locust eaten.</em></p><p>The precise identity of <em>gazam</em> is uncertain; it may denote a specific species of locust or caterpillar, or it may function as a generic term for a crop-devouring insect. Some scholars interpret the four insects of Joel 1:4 as four stages of the locust's development rather than four distinct species. The passage is used by the Lord in Joel 2:25 as a promise of restoration: God will repay the years the palmer-worm has eaten, making the agricultural imagery a vehicle for covenant hope.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "palmer-worm", "isbe": "palmer-worm"},
        "key_refs": ["Joel 1:4", "Joel 2:25", "Amos 4:9"]
    },
    "palsy": {
        "id": "palsy",
        "term": "Palsy",
        "category": "concepts",
        "intro": "<p>Palsy, a shortened form of <em>paralysis</em>, describes the condition of bodily immobility caused by nerve or muscle dysfunction. In the New Testament it translates the Greek <em>paralytikos</em> and appears frequently in the healing accounts of Jesus's ministry. Matthew 4:24 records that among those brought to Jesus were <em>those taken with palsy</em>, and his healings of paralyzed individuals became prominent signs of his messianic authority.</p><p>The most celebrated palsy healing is that of the paralytic lowered through the roof by four friends in Capernaum (Mark 2:1–12), where Jesus first pronounced forgiveness of sins and then commanded the man to rise and walk — demonstrating his authority over both spiritual and physical infirmity. Peter also healed a man named Aeneas who had been bedridden with palsy for eight years at Lydda (Acts 9:33–34). These healings fulfilled Isaiah's prophecy that the Messiah would cause the lame to leap.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "palsy", "smith": "palsy"},
        "key_refs": ["Matthew 4:24", "Matthew 9:2", "Mark 2:3", "Acts 9:33"]
    },
    "palti": {
        "id": "palti",
        "term": "Palti",
        "category": "people",
        "intro": "<p>Palti (meaning: <em>deliverance of the Lord</em>), the son of Raphu, was appointed the representative spy from the tribe of Benjamin sent by Moses to explore the land of Canaan (Numbers 13:9). He was thus one of the twelve men who entered the land and returned with a report to Moses and the congregation at Kadesh-barnea. He is not identified among those who gave the <em>evil report</em> that discouraged Israel, though only Caleb and Joshua explicitly gave the minority report of faith.</p><p>A second person named Palti (also called Paltiel, <em>deliverance of God</em>) was the son of Laish from Gallim, to whom Saul gave his daughter Michal in marriage after her separation from David (1 Samuel 25:44). This Palti is depicted with touching grief when David later demanded Michal's return (2 Samuel 3:15–16).</p>",
        "hitchcock_meaning": "deliverance",
        "source_ids": {"easton": "palti", "smith": "palti", "isbe": "palti"},
        "key_refs": ["Numbers 13:9", "1 Samuel 25:44", "2 Samuel 3:15"]
    },
    "paltiel": {
        "id": "paltiel",
        "term": "Paltiel",
        "category": "people",
        "intro": "<p>Paltiel (meaning: <em>deliverance of God</em>) is the name of two distinct individuals in Scripture. The first was a prince of the tribe of Issachar who assisted Moses and Eleazar in apportioning the land of Canaan among the tribes (Numbers 34:26). He served as one of the official representatives chosen to oversee the fair distribution of the promised land.</p><p>The second and more prominent Paltiel was the son of Laish from Gallim, to whom King Saul gave his daughter Michal — originally David's wife — after David's flight from Saul's court (1 Samuel 25:44; also called Palti). When David was restored to power and demanded Michal's return, Paltiel followed her weeping all the way to Bahurim before being ordered back by Abner (2 Samuel 3:15–16). This brief but poignant scene is one of the most humanly touching episodes in the David narrative.</p>",
        "hitchcock_meaning": "deliverance of God",
        "source_ids": {"easton": "paltiel", "smith": "paltiel", "isbe": "paltiel"},
        "key_refs": ["Numbers 34:26", "1 Samuel 25:44", "2 Samuel 3:15", "2 Samuel 3:16"]
    },
    "paltite": {
        "id": "paltite",
        "term": "Paltite",
        "category": "concepts",
        "intro": "<p>The Paltite is a gentillic designation identifying Helez, one of David's thirty mighty men, as a native of or connected with a place called Palti or Peleti. In 2 Samuel 23:26 Helez the Paltite is listed among the heroes of David's elite warrior corps. The same individual is called Helez the Pelonite in 1 Chronicles 11:27, suggesting a slight textual variation between the parallel lists.</p><p>Helez the Paltite also served as the commander over the seventh monthly division of David's standing army as described in 1 Chronicles 27:10, responsible for the Ephraimite contingent in the seventh month. The town or clan from which the designation <em>Paltite</em> derives is not clearly identified in Scripture, though it may reference the same Peleti associated with the Pelethites who formed part of David's royal guard.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "paltite", "isbe": "paltite"},
        "key_refs": ["2 Samuel 23:26", "1 Chronicles 11:27", "1 Chronicles 27:10"]
    },
    "pamphylia": {
        "id": "pamphylia",
        "term": "Pamphylia",
        "category": "places",
        "intro": "<p>Pamphylia was a coastal district on the southern shore of Asia Minor (modern Turkey), situated between Lycia to the west and Cilicia to the east, and bounded to the north by the Taurus mountain range. Its principal cities were Perga, Attalia (modern Antalya), and Aspendus. Pamphylians were present in Jerusalem at Pentecost when the Holy Spirit descended (Acts 2:10), among those who heard the disciples speaking in their own language.</p><p>The region features in Paul's first missionary journey: sailing from Cyprus, Paul and Barnabas arrived at Perga in Pamphylia (Acts 13:13), where John Mark departed from the mission and returned to Jerusalem. Paul later revisited Attalia on his return voyage (Acts 14:24–25). Pamphylia appears in the list of provinces subject to Roman governors and is mentioned in connection with the distribution of Maccabean-era correspondence (1 Maccabees 15:23).</p>",
        "hitchcock_meaning": "a nation made up of every tribe",
        "source_ids": {"easton": "pamphylia", "smith": "pamphylia", "isbe": "pamphylia"},
        "key_refs": ["Acts 2:10", "Acts 13:13", "Acts 14:24", "Acts 15:38"]
    },
    "pan": {
        "id": "pan",
        "term": "Pan",
        "category": "concepts",
        "intro": "<p>Several Hebrew words in the Old Testament are translated <em>pan</em> in English versions, all referring to vessels used in cooking, baking, or culinary preparation in the ancient Israelite household and sanctuary. The term <em>machabath</em> denotes a flat griddle or baking pan used for preparing grain offerings (Leviticus 2:5; 6:21); <em>kiyor</em> can refer to a basin; and <em>tsallachath</em> indicates a deeper dish or bowl.</p><p>Pans appear in the tabernacle and temple inventory as liturgical vessels for carrying coals or ashes from the altar (Exodus 27:3; Numbers 16:6). In domestic settings pans were central to preparing the daily grain-based diet of ancient Israelites. The narrative in 2 Samuel 13:9 mentions Tamar using a pan to bake cakes for her brother Amnon, illustrating the household use of such vessels. The variety of Hebrew terms reflects a rich vocabulary for culinary implements in biblical culture.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "pan", "smith": "pan", "isbe": "pan"},
        "key_refs": ["Leviticus 2:5", "Leviticus 6:21", "Exodus 27:3", "Numbers 11:8"]
    },
    "pannag": {
        "id": "pannag",
        "term": "Pannag",
        "category": "concepts",
        "intro": "<p>Pannag appears once in Scripture, in Ezekiel 27:17, in the list of commodities traded by Israel with Tyre: <em>Judah, and the land of Israel, they were thy merchants: they traded in thy market wheat of Minnith, and Pannag, and honey, and oil, and balm.</em> The precise meaning of <em>pannag</em> remains uncertain; suggestions include a type of millet, a confection or sweet cake, early figs, or a place name designating a specific grain variety.</p><p>The Septuagint renders it as a resinous substance, while rabbinic tradition and some modern scholars favor a form of pastry or confection. The Revised Version margin notes <em>perhaps a kind of confection</em>. Whatever its exact nature, pannag was evidently a valued agricultural or culinary product of the land of Israel, traded in the thriving commercial markets of Phoenician Tyre during the period before its fall to Nebuchadnezzar.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "pannag", "smith": "pannag", "isbe": "pannag"},
        "key_refs": ["Ezekiel 27:17"]
    },
    "paper": {
        "id": "paper",
        "term": "Paper",
        "category": "concepts",
        "intro": "<p>The word <em>paper</em> in the Authorized Version of Isaiah 19:7 translates the Hebrew <em>aroth</em>, referring to the papyrus plant that grew abundantly along the Nile Delta in ancient Egypt. Papyrus (<em>Cyperus papyrus</em>) was the principal writing material of the ancient Near Eastern and Mediterranean world, manufactured by cutting the pith of the plant into strips, pressing them together, and drying them into sheets. Egypt was the primary supplier of papyrus to the ancient world.</p><p>In the New Testament, the Greek <em>chartes</em> (2 John 12) clearly means a sheet of papyrus writing material, as John writes that he has many things to say but prefers not to write them with <em>paper and ink</em>, hoping to speak face to face. This indicates that papyrus was the ordinary medium for correspondence in the first-century Roman world. Parchment (made from animal skin) was a more durable alternative used for important documents, including the <em>parchments</em> Paul requests in 2 Timothy 4:13.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "paper", "smith": "paper", "isbe": "paper"},
        "key_refs": ["Isaiah 19:7", "2 John 1:12"]
    },
    "paphos": {
        "id": "paphos",
        "term": "Paphos",
        "category": "places",
        "intro": "<p>Paphos was the capital city and chief administrative center of the Roman province of Cyprus, situated on the southwestern coast of the island. It served as the residence of the Roman proconsul who governed Cyprus, and it was in Paphos that Paul and Barnabas encountered the Jewish sorcerer Bar-Jesus (also called Elymas) during their first missionary journey (Acts 13:6–12).</p><p>The confrontation in Paphos is significant in early church history: Paul rebuked Elymas for opposing the gospel before Sergius Paulus, the proconsul, who was seeking to hear the word of God. When Elymas was struck temporarily blind, the proconsul believed, becoming one of the earliest recorded conversions of a Roman official to Christianity. It is also at this point in Acts that Saul is consistently called Paul. The city had a much older history as a center of Aphrodite worship, with a famous temple nearby at Old Paphos.</p>",
        "hitchcock_meaning": "which boils or is very hot",
        "source_ids": {"easton": "paphos", "smith": "paphos", "isbe": "paphos"},
        "key_refs": ["Acts 13:6", "Acts 13:7", "Acts 13:8", "Acts 13:12"]
    },
    "parable": {
        "id": "parable",
        "term": "Parable",
        "category": "concepts",
        "intro": "<p>A parable (Greek <em>parabole</em>, meaning <em>a placing beside</em> or <em>comparison</em>; equivalent to the Hebrew <em>mashal</em>) is a short narrative or figure of speech in which a familiar, earthly scene is set beside a spiritual truth to illuminate it. The form appears throughout the Old Testament in proverbs, riddles, and extended comparisons (Numbers 23:7; Ezekiel 17), but it reaches its fullest development in the teaching of Jesus, who employed it as his primary mode of public instruction (Matthew 13:34).</p><p>Jesus explained his use of parables as a way of revealing truth to those with hearts prepared to receive it while concealing it from the unresponsive (Matthew 13:11–13), fulfilling the pattern of Isaiah 6:9–10. The parables cover a wide range of themes: the kingdom of God, repentance and forgiveness, stewardship, prayer, judgment, and the nature of discipleship. Parables such as the Prodigal Son (Luke 15), the Good Samaritan (Luke 10), and the Sower (Mark 4) rank among the most celebrated literary forms in world literature.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "parable", "smith": "parable", "isbe": "parable"},
        "key_refs": ["Matthew 13:3", "Matthew 13:34", "Mark 4:2", "Luke 15:3"]
    },
    "paradise": {
        "id": "paradise",
        "term": "Paradise",
        "category": "concepts",
        "intro": "<p>Paradise is a Persian loanword (<em>pardes</em>) originally meaning a <em>pleasure-ground</em>, <em>park</em>, or <em>enclosed garden</em>. It enters biblical usage as a designation for the Garden of Eden in the Septuagint translation of Genesis 2–3, where the garden God planted for Adam and Eve is rendered <em>paradeisos</em>. In later Jewish and Christian thought, paradise became a term for the abode of the righteous dead and ultimately for the renewed creation of the final age.</p><p>In the New Testament, paradise appears three times. Jesus promised the repentant thief on the cross, <em>Today shalt thou be with me in paradise</em> (Luke 23:43), locating paradise as the immediate destination of the righteous after death. Paul describes being caught up to <em>the third heaven</em>, equating it with paradise (2 Corinthians 12:4). In Revelation 2:7, the risen Christ promises the overcomer the right to eat from the tree of life in <em>the paradise of God</em> — an image that evokes the restoration of Eden and the healing of creation's original wound.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "paradise", "smith": "paradise", "isbe": "paradise"},
        "key_refs": ["Luke 23:43", "2 Corinthians 12:4", "Revelation 2:7", "Genesis 2:8"]
    },
    "parah": {
        "id": "parah",
        "term": "Parah",
        "category": "places",
        "intro": "<p>Parah (meaning: <em>heifer</em>) was a town in the tribal territory of Benjamin, listed among the settlements assigned to that tribe in Joshua 18:23. Its location is generally identified with modern Khirbet el-Farah, situated several miles northeast of Jerusalem in the hill country. The town gave its name to the Wady Farah, a valley that drains toward the Jordan.</p><p>Parah is mentioned only once in Scripture (Joshua 18:23), in the boundary and settlement list of Benjamin, and no events of biblical significance are recorded there. Its name possibly reflects the presence of cattle or agricultural activity in the region. The site's identification remains approximate, based on the geographical sequence of the Benjamin town list and the preservation of the ancient name in the modern wadi designation.</p>",
        "hitchcock_meaning": "heifer, cow, fruitful",
        "source_ids": {"easton": "parah", "smith": "parah", "isbe": "parah"},
        "key_refs": ["Joshua 18:23"]
    },
    "paran": {
        "id": "paran",
        "term": "Paran",
        "category": "places",
        "intro": "<p>Paran (meaning: <em>abounding in foliage</em> or <em>abounding in caverns</em>) designates a wilderness region south and southeast of Canaan, roughly corresponding to the northeastern Sinai Peninsula and extending toward Edom. It was in the wilderness of Paran that Hagar and Ishmael settled after their expulsion from Abraham's household (Genesis 21:21), and it was from Paran that Moses sent the twelve spies into Canaan (Numbers 13:3, 26).</p><p>Paran served as a major encampment site during Israel's wilderness wanderings; the cloud of the Lord rested over it as the congregation moved through the region (Numbers 10:12). The wilderness of Paran is associated with the region of Kadesh-barnea, the launching point for the abortive attempt to enter the land. In the prophetic poems of Deuteronomy 33:2 and Habakkuk 3:3, Mount Paran appears alongside Sinai and Seir as a location associated with the theophanic march of God to rescue his people.</p>",
        "hitchcock_meaning": "beauty, glory, ornament",
        "source_ids": {"easton": "paran"},
        "key_refs": ["Genesis 21:21", "Numbers 10:12", "Numbers 13:3", "Deuteronomy 33:2"]
    },
    "paran-mount": {
        "id": "paran-mount",
        "term": "Paran, Mount",
        "category": "places",
        "intro": "<p>Mount Paran refers to the elevated highland wilderness region associated with the wilderness of Paran in the northern Sinai–southern Negev area. It appears in two theophanic passages: Deuteronomy 33:2, where Moses's final blessing declares that the Lord <em>shined forth from Mount Paran</em> alongside his appearance from Sinai and Seir, and Habakkuk 3:3, where the prophet's vision of divine judgment describes God coming from Teman with his <em>glory</em> covering the heavens, and the <em>Holy One from Mount Paran</em>.</p><p>In both texts, Mount Paran functions as a poetic landmark of divine self-disclosure, evoking the era of the exodus and wilderness theophany when God marched with his people through the southern wilderness. Its precise geographical identification remains uncertain, but it is associated with the rugged highland terrain of the central Sinai massif or its northeastern extensions toward Edom.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "paran-mount"},
        "key_refs": ["Deuteronomy 33:2", "Habakkuk 3:3"]
    },
    "parbar": {
        "id": "parbar",
        "term": "Parbar",
        "category": "places",
        "intro": "<p>Parbar (also written <em>Parvar</em>) designates a structure or court associated with the western precinct of Solomon's temple in Jerusalem. It is mentioned in 1 Chronicles 26:18 in connection with the assignment of Levitical gatekeepers: <em>At Parbar westward, four at the causeway, and two at Parbar.</em> The term also appears in 2 Kings 23:11, where Josiah removes horses dedicated to the sun from the area near the entry of the house of the Lord, specifically <em>by the chamber of Nathan-melech the chamberlain, which was in the suburbs</em> — a location the Hebrew renders similarly.</p><p>The precise architectural character of the Parbar is uncertain. Suggestions include a colonnade or open portico, a suburb or outer court, or a building for the accommodation of temple functionaries. Some scholars connect the term to a Persian or Aramaic loanword meaning <em>outside</em> or <em>suburb</em>, making it a general designation for the outer temple precincts.</p>",
        "hitchcock_meaning": "a suburb, being pure",
        "source_ids": {"easton": "parbar", "smith": "parbar", "isbe": "parbar"},
        "key_refs": ["1 Chronicles 26:18", "2 Kings 23:11"]
    },
    "parched-ground": {
        "id": "parched-ground",
        "term": "Parched Ground",
        "category": "concepts",
        "intro": "<p>Parched ground renders the Hebrew <em>sharab</em> in Isaiah 35:7, a term describing the shimmering mirage that appears over heated desert terrain — the optical illusion of water hovering above sun-baked ground. The phenomenon, familiar in the Sinai and Arabian deserts, was well-known to ancient travelers and is a natural symbol of false hope and deceptive appearances.</p><p>Isaiah 35:7 employs the image in a dramatic reversal: <em>And the parched ground shall become a pool, and the thirsty land springs of water.</em> In the context of Isaiah's vision of the future restoration of the wilderness highway on which the redeemed will return to Zion, the transformation of the mirage into actual water represents the radical inversion of desert conditions under divine blessing. What once deceived the weary traveler with the illusion of refreshment will become genuine abundance. The image powerfully captures the eschatological reversal of curse into blessing.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "parched-ground"},
        "key_refs": ["Isaiah 35:7"]
    },
    "parchment": {
        "id": "parchment",
        "term": "Parchment",
        "category": "concepts",
        "intro": "<p>Parchment is writing material prepared from the treated skin of sheep or goats, as distinct from papyrus, which was made from a plant. Its name derives from the city of Pergamos (Pergamum) in Asia Minor, where the material was perfected and promoted as an alternative to Egyptian papyrus, perhaps after a trade embargo on papyrus supply. Parchment proved more durable than papyrus, capable of withstanding moisture and folding, and eventually became the preferred medium for important manuscripts.</p><p>The sole explicit New Testament reference to parchment occurs in 2 Timothy 4:13, where Paul, writing from prison near the end of his life, asks Timothy to bring <em>the cloke that I left at Troas with Carpus, and the books, but especially the parchments.</em> The Greek word <em>membrana</em> (Latin loanword) clearly indicates parchment notebooks or scrolls, likely including personal copies of Scripture or other documents Paul valued for his continued study and ministry even in confinement.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "parchment", "smith": "parchment", "isbe": "parchment"},
        "key_refs": ["2 Timothy 4:13"]
    },
    "pardon": {
        "id": "pardon",
        "term": "Pardon",
        "category": "concepts",
        "intro": "<p>Pardon in Scripture denotes the divine act of forgiveness by which God releases the guilty from the penalty and guilt of sin, restoring the broken covenant relationship. The Old Testament presents pardon as freely given (Isaiah 43:25), readily available to those who repent (Nehemiah 9:17; Psalm 86:5), and linked to God's abundant mercy rather than human merit. Isaiah 55:7 extends the invitation to the wicked to return to the Lord, <em>for he will abundantly pardon</em> (<em>yarbeh lisloach</em> — he will multiply forgiveness).</p><p>Pardon in the OT is grounded in the sacrificial system and God's covenant steadfast love (<em>hesed</em>), while the NT grounds it in the atoning work of Christ. Paul's language of justification and Romans 5:20 — <em>where sin abounded, grace did much more abound</em> — reflects the same theology of abundant divine forgiveness. Micah 7:18 celebrates God as one who <em>delighteth in mercy</em>, pardoning iniquity as an expression of his very character, not merely his policy.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "pardon", "isbe": "pardon"},
        "key_refs": ["Isaiah 43:25", "Nehemiah 9:17", "Isaiah 55:7", "Micah 7:18"]
    },
    "parlour": {
        "id": "parlour",
        "term": "Parlour",
        "category": "concepts",
        "intro": "<p>The word <em>parlour</em> appears in several Old Testament passages, translating different Hebrew terms that denote a private inner chamber, an audience hall, or a cool upper room. In Judges 3:20–24, Eglon king of Moab is killed by Ehud in his <em>summer parlour</em> — a cool upper chamber typical of ancient Near Eastern palace design, where latticed windows allowed ventilation. The servants, believing the king was <em>covering his feet</em> (a euphemism for relieving himself), delayed long enough for Ehud to escape.</p><p>In 1 Chronicles 28:11, the parlour (Hebrew <em>cheder</em>) refers to the inner chambers of Solomon's temple complex as revealed to David by the Spirit. In 1 Samuel 9:22, Samuel brought Saul and his servant into the <em>parlour</em> of the place of sacrifice and gave them the chief place among the invited guests. The word thus spans both sacred and royal domestic architecture in the biblical world.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "parlour"},
        "key_refs": ["Judges 3:20", "1 Samuel 9:22", "1 Chronicles 28:11"]
    },
    "parmashta": {
        "id": "parmashta",
        "term": "Parmashta",
        "category": "people",
        "intro": "<p>Parmashta (meaning: <em>stronger than all</em> or <em>strong-fisted</em>) was one of the ten sons of Haman the Agagite, the enemy of the Jewish people in the court of the Persian king Ahasuerus (Xerxes). Following the reversal of Haman's plot against the Jews — when the king's decree permitted the Jewish people to defend themselves — Parmashta and his nine brothers were slain in Shushan the palace on the thirteenth day of Adar (Esther 9:9).</p><p>His death, along with that of his brothers and father, is presented in the book of Esther as the vindication of the Jewish people and the just consequence of the murderous plot Haman had devised. The ten sons of Haman are listed by name in Esther 9:7–10 as a permanent record of the defeat of those who sought Israel's destruction. Their names may be of Persian or Babylonian origin.</p>",
        "hitchcock_meaning": "stronger than all",
        "source_ids": {"easton": "parmashta", "smith": "parmashta", "isbe": "parmashta"},
        "key_refs": ["Esther 9:9"]
    },
    "parmenas": {
        "id": "parmenas",
        "term": "Parmenas",
        "category": "people",
        "intro": "<p>Parmenas (meaning: <em>constant</em> or <em>that abides</em>) was one of the seven men chosen by the Jerusalem congregation to oversee the daily distribution of food to the Hellenistic Jewish widows who had been neglected in the common meals (Acts 6:1–6). He is listed fifth among the seven in Acts 6:5. These seven men, often called the first deacons, were required to be of good reputation, full of the Holy Spirit, and full of wisdom.</p><p>Beyond his selection and naming in Acts 6, no further details about Parmenas are recorded in the New Testament. His Greek name suggests he was part of the Greek-speaking Jewish community in Jerusalem, the same group whose widows had been overlooked. Early church tradition variously assigns him a subsequent ministry in various regions, but these accounts are late and non-canonical. He stands as one of the quiet servants whose faithful administration undergirded the early church's growth.</p>",
        "hitchcock_meaning": "that abides, or is permanent",
        "source_ids": {"easton": "parmenas", "smith": "parmenas", "isbe": "parmenas"},
        "key_refs": ["Acts 6:5"]
    },
    "parshandatha": {
        "id": "parshandatha",
        "term": "Parshandatha",
        "category": "people",
        "intro": "<p>Parshandatha (meaning: <em>given by prayer</em> or <em>interpreter of the law</em>) was the eldest son of Haman, the chief minister of King Ahasuerus (Xerxes) of Persia who plotted the annihilation of the Jewish people. When Haman's plot was reversed and the Jews were permitted to defend themselves, Parshandatha and his nine brothers were killed in Shushan the palace on the day the Jews' enemies had planned to destroy them (Esther 9:7).</p><p>The ten sons of Haman are named in Esther 9:7–10 as a permanent memorial of the defeat of those who sought Israel's destruction, and their names are traditionally written in a distinctive typographical arrangement in Hebrew scrolls of the book of Esther. Parshandatha's name, like those of his brothers, is of uncertain etymological origin — possibly Old Persian. Their deaths concluded the events commemorated in the festival of Purim.</p>",
        "hitchcock_meaning": "given by prayer",
        "source_ids": {"easton": "parshandatha", "smith": "parshandatha", "isbe": "parshandatha"},
        "key_refs": ["Esther 9:7"]
    },
    "parthians": {
        "id": "parthians",
        "term": "Parthians",
        "category": "concepts",
        "intro": "<p>The Parthians were an Iranian people whose empire at its height extended from the Euphrates River to eastern Iran, making them the dominant power east of Rome from the second century BC to the third century AD. They were formidable mounted archers, famous for the <em>Parthian shot</em> — firing arrows while retreating on horseback — and repeatedly defeated Roman legions attempting to expand eastward.</p><p>Parthians are mentioned in Scripture only once, in Acts 2:9, where they appear first in the list of Jewish diaspora communities present in Jerusalem at Pentecost who heard the disciples speaking in their own native languages. This places Jewish communities within the Parthian empire — corresponding to ancient Media, Persia, Elam, and Mesopotamia — among the earliest witnesses to the outpouring of the Holy Spirit. The Jewish diaspora in Parthia was substantial, descended partly from the Assyrian and Babylonian deportations of the eighth and sixth centuries BC.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "parthians", "smith": "parthians", "isbe": "parthians"},
        "key_refs": ["Acts 2:9"]
    },
    "partridge": {
        "id": "partridge",
        "term": "Partridge",
        "category": "concepts",
        "intro": "<p>The partridge (Hebrew <em>kore</em>, meaning <em>caller</em> or <em>crier</em>, from its characteristic call) is mentioned twice in the Old Testament, both times in figurative contexts. In 1 Samuel 26:20, David uses the image of hunting the partridge in the mountains to describe Saul's relentless pursuit of him: <em>the king of Israel is come out to seek a flea, as when one doth hunt a partridge in the mountains</em> — evoking the exhausting chase of an elusive quarry across rocky terrain.</p><p>Jeremiah 17:11 employs the partridge in a proverb about ill-gotten wealth: <em>As the partridge sitteth on eggs, and hatcheth them not; so he that getteth riches, and not by right, shall leave them in the midst of his days.</em> The reference to a partridge gathering eggs it did not lay — a behavior observed in nature — becomes a metaphor for wealth accumulated through injustice that ultimately cannot be kept. The Caccabis species common to Palestine would fit both references.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "partridge", "smith": "partridge", "isbe": "partridge"},
        "key_refs": ["1 Samuel 26:20", "Jeremiah 17:11"]
    },
    "paruah": {
        "id": "paruah",
        "term": "Paruah",
        "category": "people",
        "intro": "<p>Paruah (meaning: <em>flourishing</em> or <em>blossoming</em>) was the father of Jehoshaphat, one of the twelve officers whom Solomon appointed to provide provisions for the royal household, each responsible for supplying the palace for one month of the year. His son Jehoshaphat served as the officer over the tribe of Issachar (1 Kings 4:17).</p><p>Paruah himself is mentioned only in this genealogical notice; beyond being the father of Solomon's Issachar officer, no further details are recorded about him in Scripture. The administrative system Solomon established — with rotating provincial officers responsible for supplying the court — represented a sophisticated bureaucratic achievement, and the listing of each officer's father and territory reflects the official character of the arrangement.</p>",
        "hitchcock_meaning": "flourishing",
        "source_ids": {"easton": "paruah", "smith": "paruah", "isbe": "paruah"},
        "key_refs": ["1 Kings 4:17"]
    },
    "parvaim": {
        "id": "parvaim",
        "term": "Parvaim",
        "category": "places",
        "intro": "<p>Parvaim is an unidentified region or country from which Solomon obtained gold for the decoration of the temple in Jerusalem (2 Chronicles 3:6). The verse states that Solomon overlaid the temple with precious stones for beauty, and the gold he used was gold of Parvaim. Beyond this single reference, Parvaim does not appear elsewhere in Scripture.</p><p>Proposed identifications have included regions of southern Arabia, eastern Africa (Ophir-related), or even a place in the Far East; none has achieved scholarly consensus. Some have suggested it may be a poetic or archaic term for an exceptionally fine quality of gold rather than a specific geographical location. The context alongside Solomon's broader use of exotic materials — cedar from Lebanon, stones from Hiram's men — suggests a distant and prestigious source, fitting the temple's character as a monument of unparalleled wealth and craftsmanship.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "parvaim", "smith": "parvaim", "isbe": "parvaim"},
        "key_refs": ["2 Chronicles 3:6"]
    },
    "pas-dammim": {
        "id": "pas-dammim",
        "term": "Pas-dammim",
        "category": "places",
        "intro": "<p>Pas-dammim, meaning <em>border of blood</em> or <em>portion of blood</em>, was a site in the Shephelah lowlands of Judah, situated between Shochoh and Azekah. It is identified with Ephes-dammim (1 Samuel 17:1), the Philistine encampment opposite Israel's forces in the valley of Elah where the confrontation between David and Goliath took place. The name's reference to blood may recall the site of repeated bloody engagements between Israel and the Philistines.</p><p>A later battle at Pas-dammim is recorded in 1 Chronicles 11:13, where it is listed as the site of a heroic stand by Eleazar the son of Dodo, one of David's three mighty men. There, when Israel's troops had retreated, Eleazar stood his ground and struck down the Philistines until his hand was weary and clung to his sword — one of the memorable acts of valor that defined David's elite warriors.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "pas-dammim", "isbe": "pas-dammim"},
        "key_refs": ["1 Samuel 17:1", "1 Chronicles 11:13"]
    },
    "pasach": {
        "id": "pasach",
        "term": "Pasach",
        "category": "people",
        "intro": "<p>Pasach (meaning: <em>clearing</em> or <em>dividing</em>) was a son of Japhlet, a descendant of Asher, mentioned in the genealogical register of the tribe of Asher in 1 Chronicles 7:33. He appears alongside his brothers Bimhal and Ashvath in the listing of Japhlet's sons. The name Pasach occurs only in this single genealogical reference.</p><p>No events or achievements are ascribed to Pasach beyond his inclusion in the tribal genealogy of Asher. The Asherite genealogies in 1 Chronicles 7:30–40 are among the more complete tribal records in the Chronicler's work, listing the clans and notable warriors of the tribe. Pasach's inclusion marks him as a recognized ancestor within the Asherite family tree, though his significance beyond the genealogical record is not elaborated.</p>",
        "hitchcock_meaning": "thy cleft",
        "source_ids": {"easton": "pasach", "smith": "pasach", "isbe": "pasach"},
        "key_refs": ["1 Chronicles 7:33"]
    },
    "pashur": {
        "id": "pashur",
        "term": "Pashur",
        "category": "people",
        "intro": "<p>Pashur is the name of several individuals in the Old Testament, the most prominent being Pashur the son of Immer, a priest and <em>chief governor in the house of the Lord</em> who became a fierce opponent of the prophet Jeremiah. When Jeremiah prophesied the destruction of Jerusalem, Pashur had him beaten and placed in stocks overnight at the Benjamin Gate of the temple (Jeremiah 20:1–3). Jeremiah responded by giving him the name <em>Magor-missabib</em> — <em>terror on every side</em> — and prophesying that he and his household would die in Babylon.</p><p>A second Pashur, the son of Malchiah, was among the officials who had Jeremiah thrown into a cistern for prophesying that Jerusalem would fall (Jeremiah 38:1–6). A third Pashur was a priest whose descendants returned from Babylon with Zerubbabel (Ezra 2:38; Nehemiah 7:41). The name may reflect an Egyptian origin (<em>portion of Horus</em>) introduced through early contacts.</p>",
        "hitchcock_meaning": "that extends or multiplies",
        "source_ids": {"easton": "pashur", "smith": "pashur"},
        "key_refs": ["Jeremiah 20:1", "Jeremiah 20:3", "Jeremiah 38:1", "Ezra 2:38"]
    },
    "passage": {
        "id": "passage",
        "term": "Passage",
        "category": "concepts",
        "intro": "<p>The word <em>passage</em> in Scripture translates several Hebrew terms and denotes a ford, crossing point, mountain pass, or narrow defile — locations of critical strategic and narrative importance throughout the biblical story. The Jabbok ford served as the site of Jacob's wrestling with the divine messenger (Genesis 32:22). The crossing of the Jordan River by Joshua's Israel (Joshua 3–4) was a defining passage-event, reenacting the Red Sea crossing.</p><p>In the tribal and military narratives, control of passages was decisive. The Gileadites controlled the fords of the Jordan to identify Ephraimite fugitives by their pronunciation of <em>Shibboleth</em> (Judges 12:5–6). The passage of Michmash (1 Samuel 13:23; 14:4) was the narrow defile where Jonathan and his armor-bearer launched their audacious raid on the Philistine garrison. In prophetic literature (Isaiah 10:29), the advance of the Assyrian army is traced pass by pass, building dramatic tension as it approaches Jerusalem.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "passage", "smith": "passage"},
        "key_refs": ["Judges 12:5", "1 Samuel 13:23", "1 Samuel 14:4"]
    },
    "passion": {
        "id": "passion",
        "term": "Passion",
        "category": "concepts",
        "intro": "<p>Passion, in its specific biblical usage, refers to the sufferings of Jesus Christ in the period leading to and including his crucifixion. The word appears once in the Authorized Version, in Acts 1:3, where Luke writes that Jesus <em>showed himself alive after his passion by many infallible proofs</em>. The Greek word underlying it is <em>pathein</em> (to suffer), from the same root as <em>pathos</em>, distinguishing the suffering and death of Christ from his subsequent resurrection appearances.</p><p>The <em>Passion narrative</em> — a term derived from this usage — designates the accounts of Jesus's arrest, trial, crucifixion, and burial in all four Gospels. These narratives occupy a disproportionately large share of each Gospel, reflecting the early church's conviction that the death of Christ was the central event of salvation history. Paul summarizes the apostolic proclamation as <em>Christ crucified</em> (1 Corinthians 1:23; 2:2), and the entire sacrificial system of the Old Testament is understood in the New Testament as pointing forward to this defining Passion.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "passion"},
        "key_refs": ["Acts 1:3", "1 Corinthians 1:23", "Isaiah 53:3"]
    },
    "passover": {
        "id": "passover",
        "term": "Passover",
        "category": "events",
        "intro": "<p>The Passover (<em>Pesach</em>) is the first and foundational festival of the Israelite sacred calendar, commemorating the night of the tenth plague in Egypt when the angel of death passed over the blood-marked homes of Israel while striking the firstborn of Egypt (Exodus 12). God commanded that a lamb without blemish be slaughtered at twilight on the fourteenth of Nisan, its blood applied to the doorposts, and the meal eaten in haste — sandals on feet, staff in hand — as the people prepared for their departure. This meal, with unleavened bread and bitter herbs, became the annual Passover feast.</p><p>The Passover stands at the heart of Israelite identity as the founding act of national redemption, and its observance was central to covenant renewal under Joshua, Hezekiah, Josiah, and Ezra. In the New Testament, Jesus deliberately chose the Passover setting for the Last Supper, interpreting his imminent death through its imagery. Paul explicitly calls Christ <em>our passover</em> who has been <em>sacrificed for us</em> (1 Corinthians 5:7), making the exodus deliverance a type of atonement fulfilled in Christ.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "passover", "smith": "passover", "isbe": "passover"},
        "key_refs": ["Exodus 12:13", "Exodus 12:14", "1 Corinthians 5:7", "Mark 14:1"]
    },
    "patara": {
        "id": "patara",
        "term": "Patara",
        "category": "places",
        "intro": "<p>Patara was a prominent seaport city on the southwestern coast of the Roman province of Lycia (modern Turkey), situated at the mouth of the Xanthus River. It was a commercial and administrative center of some importance, functioning as a principal port for ships crossing the eastern Mediterranean. Patara is mentioned in Acts 21:1–2, where Paul and his companions, sailing from Miletus toward Jerusalem after the third missionary journey, stopped at Cos and Rhodes before arriving at Patara, where they transferred to a ship crossing directly to Phoenicia.</p><p>In some manuscript traditions of Acts 21:1, the port of Myra appears alongside Patara, suggesting a slightly different itinerary. Patara also had significance as the site of a famous oracle of Apollo, one of the notable oracular shrines of the ancient world, though the New Testament account makes no mention of this. The city's role as a major transit port made it a natural stopping point on the eastern Mediterranean sea routes used by Paul in his missionary travels.</p>",
        "hitchcock_meaning": "trodden underfoot",
        "source_ids": {"easton": "patara", "smith": "patara", "isbe": "patara"},
        "key_refs": ["Acts 21:1", "Acts 21:2"]
    },
    "pathros": {
        "id": "pathros",
        "term": "Pathros",
        "category": "places",
        "intro": "<p>Pathros is the biblical name for Upper Egypt (the Thebaid of Greek geographers), the long southern region of the Nile valley extending from Memphis toward the first cataract at Aswan. The name likely derives from the Egyptian <em>Pa-to-res</em>, meaning <em>the southern land</em>. Pathros is mentioned in Isaiah 11:11 as one of the distant lands from which God will gather the scattered remnant of Israel in the great future restoration.</p><p>The prophet Jeremiah addressed significant communities of Jewish exiles who had fled to Egypt after Jerusalem's fall, specifically targeting those who had settled in Pathros and continued to worship the Queen of Heaven (Jeremiah 44:1, 15). Ezekiel prophesied judgment on Egypt including Pathros (Ezekiel 29:14; 30:14), declaring it would become a lowly kingdom. The Table of Nations in Genesis 10:14 identifies Pathrusim — inhabitants of Pathros — as a son of Mizraim (Egypt), establishing the region's place in the genealogical record of nations.</p>",
        "hitchcock_meaning": "mouthful of dough",
        "source_ids": {"easton": "pathros", "smith": "pathros", "isbe": "pathros"},
        "key_refs": ["Isaiah 11:11", "Jeremiah 44:1", "Ezekiel 30:14", "Genesis 10:14"]
    },
    "patmos": {
        "id": "patmos",
        "term": "Patmos",
        "category": "places",
        "intro": "<p>Patmos is a small, rocky, and largely barren island in the Aegean Sea, part of the Dodecanese group known in antiquity as the Sporades, located approximately 37 miles southwest of Miletus off the coast of Asia Minor (modern Turkey). Its rugged terrain and relative isolation made it a location used by Roman authorities for the banishment of political prisoners and troublemakers.</p><p>Patmos holds singular significance in Christian history as the place where the apostle John received the visions recorded in the book of Revelation. John states in Revelation 1:9 that he was <em>in the isle that is called Patmos, for the word of God, and for the testimony of Jesus Christ</em> — indicating he had been exiled there on account of his Christian witness, most likely during the reign of the emperor Domitian (c. AD 95). On the island, on the Lord's day, he heard a voice like a trumpet and received the apocalyptic visions addressed to the seven churches of Asia and concerning the ultimate triumph of God. A cave on the island, traditionally called the Cave of the Apocalypse, is venerated as the site of John's vision.</p>",
        "hitchcock_meaning": "my killing",
        "source_ids": {"easton": "patmos", "smith": "patmos", "isbe": "patmos"},
        "key_refs": ["Revelation 1:9"]
    },
    "patriarch": {
        "id": "patriarch",
        "term": "Patriarch",
        "category": "concepts",
        "intro": "<p>Patriarch (Greek <em>patriarches</em>, from <em>pater</em>, father, and <em>arche</em>, rule or origin) designates the father-rulers of ancient Israel, particularly the founding ancestors of the Hebrew people. The term appears in the New Testament applied to Abraham (Hebrews 7:4), to the twelve sons of Jacob (Acts 7:8–9), and notably to David (Acts 2:29), acknowledging his foundational status in the line of covenant promises.</p><p>In its broader theological and historical sense, <em>the patriarchs</em> refers to the three great covenant ancestors: Abraham, Isaac, and Jacob. The patriarchal period — roughly the second millennium BC — encompasses the narratives of Genesis 12–50, in which God established his covenant with Abraham's family, promised them the land of Canaan, and multiplied them in preparation for the nation of Israel. The patriarchs are invoked throughout Scripture as the anchors of God's covenant faithfulness, and Paul grounds the inclusion of the Gentiles in salvation within the Abrahamic promises (Romans 4; Galatians 3).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "patriarch", "smith": "patriarch"},
        "key_refs": ["Hebrews 7:4", "Acts 7:8", "Acts 7:9", "Romans 9:5"]
    },
    "patrobas": {
        "id": "patrobas",
        "term": "Patrobas",
        "category": "people",
        "intro": "<p>Patrobas (meaning: <em>life of his father</em> or <em>father's life</em>) was a Christian in Rome to whom the apostle Paul sent greetings in his letter to the Romans (Romans 16:14). He is mentioned alongside Asyncritus, Phlegon, Hermas, and Hermes as members of a distinct house-church or fellowship circle within the Roman Christian community, as Paul adds: <em>and the brethren which are with them.</em></p><p>The Greek name Patrobas was common in the Roman world and was borne by a freedman of the emperor Nero who was put to death by Galba. Whether the Patrobas of Romans 16 had any connection to this figure is unknown. Like many of those greeted in Romans 16, Patrobas appears to have been part of the diverse community of Jewish and Gentile Christians who made up the Roman church before Paul's own visit to the city.</p>",
        "hitchcock_meaning": "life of his father",
        "source_ids": {"easton": "patrobas", "smith": "patrobas", "isbe": "patrobas"},
        "key_refs": ["Romans 16:14"]
    },
    "pau": {
        "id": "pau",
        "term": "Pau",
        "category": "places",
        "intro": "<p>Pau (also written <em>Pai</em> in 1 Chronicles 1:50, meaning <em>bleating</em> or <em>screaming</em>) was the royal city of Hadar (or Hadad), the last-named of the eight kings of Edom who reigned before any king ruled over Israel (Genesis 36:39). The city thus belonged to the pre-monarchic period of Edomite history, contemporary with the patriarchal era or the time of the judges.</p><p>Beyond its identification as a royal Edomite city, Pau is not located with certainty on the ancient landscape. No significant events beyond the mention of Hadar's reign are associated with it, and the city appears to have had little subsequent history in the biblical record. The parallel passage in 1 Chronicles 1:50 preserves the variant spelling Pai. The parallel lists of Edomite kings in Genesis 36 and 1 Chronicles 1 represent one of the earliest examples of king-list conventions in biblical literature.</p>",
        "hitchcock_meaning": "gold, the place or mouth",
        "source_ids": {"easton": "pau", "smith": "pau", "isbe": "pau"},
        "key_refs": ["Genesis 36:39", "1 Chronicles 1:50"]
    },
    "paul": {
        "id": "paul",
        "term": "Paul",
        "category": "people",
        "intro": "<p>Paul (Latin <em>Paulus</em>, small), originally named Saul, was the apostle to the Gentiles and the most prolific author of the New Testament. Born in Tarsus of Cilicia to a Jewish family of the tribe of Benjamin, he held Roman citizenship from birth — a status that shaped his ministry and trials. Educated in Jerusalem under the Pharisaic master Gamaliel, Saul was a zealous persecutor of the early church until his dramatic encounter with the risen Christ on the road to Damascus (Acts 9), which transformed him into the faith's most energetic advocate.</p><p>Paul's three missionary journeys, recorded in Acts 13–21, carried the gospel from Antioch through Asia Minor, Macedonia, Greece, and toward Rome. His fourteen epistles — ranging from the theological heights of Romans to the pastoral intimacy of Philemon — shaped Christian doctrine on justification, the church, resurrection, and eschatology more than any other author. Arrested in Jerusalem, imprisoned in Caesarea, and tried before Roman officials, Paul eventually reached Rome where he was martyred, traditionally under Nero. He stands as the towering figure of early Christian mission and theology.</p>",
        "hitchcock_meaning": "small, little",
        "source_ids": {"easton": "paul", "smith": "paul"},
        "key_refs": ["Acts 9:1", "Philippians 3:5", "Galatians 1:11", "2 Timothy 4:7"]
    },
    "pavement": {
        "id": "pavement",
        "term": "Pavement",
        "category": "concepts",
        "intro": "<p>Pavement in Scripture most notably refers to the stone-paved platform or judgment seat (Greek <em>lithostroton</em>, Latin <em>Gabbatha</em>) in Jerusalem where Pontius Pilate sat to pronounce judgment on Jesus (John 19:13). The Aramaic name <em>Gabbatha</em> means <em>elevated place</em> or <em>ridge</em>, while <em>lithostroton</em> (stone-pavement) describes its surface. Archaeologists have identified a large paved area associated with the Antonia Fortress as a candidate for this site.</p><p>The elaborate pavement of Solomon's temple court — described in 2 Chronicles 7:3 as the place where the congregation prostrated themselves as the glory of the Lord filled the temple — represents the grander use of the term in the Old Testament. Esther 1:6 describes the elaborate pavement of colored stones in the court of the Persian king's garden in Shushan: <em>a pavement of red, and blue, and white, and black marble</em>. Archaeological excavations at Persepolis and Susa confirm the lavish stone-paving characteristic of Persian royal architecture.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "pavement", "smith": "pavement", "isbe": "pavement"},
        "key_refs": ["John 19:13", "2 Chronicles 7:3", "Esther 1:6"]
    },
    "pavilion": {
        "id": "pavilion",
        "term": "Pavilion",
        "category": "concepts",
        "intro": "<p>Pavilion translates several Hebrew words in Scripture denoting a tent, booth, canopy, or sheltered enclosure. The term appears both in literal military contexts and in figurative theological ones. In 1 Kings 20:12–16, Ben-hadad of Syria is found drinking with his allied kings in their pavilions — field tents or portable booths — while besieging Samaria, a detail that contributes to the narrative irony of his subsequent defeat.</p><p>The richest theological use of the image is in the Psalms, where God's pavilion becomes a metaphor for his protective presence and hidden shelter. Psalm 27:5 declares: <em>In the time of trouble he shall hide me in his pavilion; in the secret of his tabernacle shall he hide me.</em> Psalm 18:11 describes God making darkness his secret place, his pavilion round about him of dark waters and thick clouds. The pavilion thus evokes the divine glory concealed within the cloud of the tabernacle, where God's presence both reveals and hides itself — accessible to those he shelters, overwhelming to those who oppose him.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "pavilion", "smith": "pavilion", "isbe": "pavilion"},
        "key_refs": ["Psalms 27:5", "Psalms 18:11", "1 Kings 20:12", "Jeremiah 43:10"]
    },
    "peace-offerings": {
        "id": "peace-offerings",
        "term": "Peace Offerings",
        "category": "concepts",
        "intro": "<p>The peace offerings (Hebrew <em>shelamim</em>, from <em>shalom</em>, peace or wholeness) formed one of the central categories of Israelite sacrifice prescribed in the Mosaic law, detailed extensively in Leviticus 3 and 7:11–36. Unlike the burnt offering, which was entirely consumed on the altar, the peace offering was a shared meal: the fat and certain organs were burned on the altar for the Lord, the breast and right thigh were given to the priests, and the remainder was eaten by the worshiper and family in a festive communal meal before the Lord.</p><p>The peace offering expressed fellowship, gratitude, and covenant communion between God and his people. It came in three forms: the thank offering (<em>todah</em>) for God's specific mercies; the vow offering, fulfilling a pledge made in distress; and the freewill offering, a spontaneous act of devotion. The New Testament understands Christ's sacrifice as inaugurating the ultimate peace offering, restoring the broken fellowship between God and humanity and making possible a new covenant communion (Ephesians 2:14–17; Colossians 1:20).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "peace-offerings"},
        "key_refs": ["Leviticus 3:1", "Leviticus 7:11", "Leviticus 7:29", "Ephesians 2:14"]
    },
    "peacock": {
        "id": "peacock",
        "term": "Peacock",
        "category": "concepts",
        "intro": "<p>The peacock (Hebrew <em>tuk</em>, apparently borrowed from the Tamil <em>tokei</em>) is mentioned twice in the Old Testament as one of the exotic imports brought to Solomon by his fleet from Ophir (1 Kings 10:22; 2 Chronicles 9:21). Every three years the king's ships of Tarshish returned bearing gold, silver, ivory, apes, and <em>peacocks</em> — a list suggesting distant tropical trade, possibly with India or the Horn of Africa, where peacocks were indigenous.</p><p>A separate Hebrew word (<em>renanim</em>) in Job 39:13 is translated <em>peacock</em> in the Authorized Version, though modern translators more often render it ostrich, since the context describes a bird that abandons its eggs on the ground. The peacock's stunning plumage made it a prized luxury commodity in the ancient Near East, symbolic of the extraordinary wealth and cosmopolitan reach of Solomon's commercial empire. The bird does not carry theological symbolism in Scripture beyond this association with royal magnificence.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "peacock", "isbe": "peacock"},
        "key_refs": ["1 Kings 10:22", "2 Chronicles 9:21", "Job 39:13"]
    },
    "pearl": {
        "id": "pearl",
        "term": "Pearl",
        "category": "concepts",
        "intro": "<p>Pearls were among the most prized gemstones of the ancient world, formed by oysters in the Persian Gulf, the Red Sea, and the Indian Ocean. The Hebrew <em>gabish</em> (Job 28:18) and Greek <em>margarites</em> (Matthew 7:6; 13:46) both designate the pearl, which ranked alongside gold and precious stones as the highest measure of value. In ancient trade, pearls commanded extraordinary prices, sometimes exceeding the value of equivalent-weight gold.</p><p>In the teaching of Jesus, the pearl appears in two memorable contexts. In Matthew 7:6, Jesus warns against casting <em>pearls before swine</em> — offering what is holy to those incapable of valuing it. In the Parable of the Pearl of Great Price (Matthew 13:45–46), the kingdom of heaven is compared to a merchant who discovers a pearl of supreme worth and sells everything to acquire it. In Revelation 21:21, the twelve gates of the New Jerusalem are each made of a single pearl — the ultimate image of unimaginable divine generosity. The New Testament explicitly links pearl adornment with excess and false values (1 Timothy 2:9; Revelation 17:4).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "pearl", "smith": "pearl", "isbe": "pearl"},
        "key_refs": ["Matthew 13:46", "Matthew 7:6", "Revelation 21:21", "Job 28:18"]
    },
    "peculiar": {
        "id": "peculiar",
        "term": "Peculiar",
        "category": "concepts",
        "intro": "<p>Peculiar in its biblical usage does not mean <em>strange</em> or <em>odd</em> but rather <em>one's own special possession</em>. It translates the Hebrew <em>segullah</em> (Exodus 19:5; Psalm 135:4; Malachi 3:17) and the Greek <em>peripoiesis</em> (Ephesians 1:14; 1 Peter 2:9), both denoting a treasured personal possession distinguished from common property. When God declares Israel his <em>peculiar treasure</em> at Sinai (Exodus 19:5), he uses the language of a king's personal jewels — property set apart from the general treasury as uniquely precious.</p><p>The New Testament applies the same concept to the church: 1 Peter 2:9 calls believers <em>a peculiar people</em> (<em>laos eis peripoiesin</em> — a people for God's own possession), identifying them as the continuation and fulfillment of the Sinai election. Titus 2:14 adds that Christ gave himself to <em>purify unto himself a peculiar people, zealous of good works.</em> The concept undergirds the biblical theology of election: God's choice of a people is not arbitrary favoritism but the constitutive act by which he creates a community to bear his name and reflect his character to the nations.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "peculiar", "isbe": "peculiar"},
        "key_refs": ["Exodus 19:5", "1 Peter 2:9", "Titus 2:14", "Malachi 3:17"]
    },
    "pedahel": {
        "id": "pedahel",
        "term": "Pedahel",
        "category": "concepts",
        "intro": "<p>Pedahel (meaning: <em>God redeems</em> or <em>redeemed of God</em>) was a prince of the tribe of Naphtali appointed by God as one of the commissioners tasked with assisting Moses and Eleazar the priest in dividing the land of Canaan among the tribes (Numbers 34:28). He is mentioned only in this single appointment, which reflects the representative structure of the land distribution — each tribe contributing a leader to oversee fair allocation.</p><p>Pedahel was the son of Ammihud, a common priestly or noble name in the period. His name, meaning divine redemption, was fitting for a leader involved in the fulfillment of God's covenant promise to give Israel the land. Beyond this administrative appointment, no further record of Pedahel's activities appears in Scripture. He represents the largely anonymous cadre of tribal leaders whose faithful service in specific administrative roles made possible the ordered settlement of Canaan.</p>",
        "hitchcock_meaning": "God redeems",
        "source_ids": {"easton": "pedahel", "smith": "pedahel", "isbe": "pedahel"},
        "key_refs": ["Numbers 34:28"]
    },
    "pedahzur": {
        "id": "pedahzur",
        "term": "Pedahzur",
        "category": "people",
        "intro": "<p>Pedahzur (meaning: <em>the rock redeems</em> or <em>rock of redemption</em>) was the father of Gamaliel, the prince appointed over the tribe of Manasseh for the first census in the wilderness (Numbers 1:10; 2:20). He appears in the repeated formulas of Numbers 1–10, where each tribal leader is identified by name and patronym in the various administrative lists of the wilderness community.</p><p>Pedahzur himself held no listed office; he is known entirely through his son Gamaliel, who represented Manasseh in the census, led the tribe's contingent in the marching order (Numbers 2:20), and brought Manasseh's dedication offering at the consecration of the tabernacle (Numbers 7:54). The name Pedahzur, built on the divine epithet <em>rock</em> (<em>tsur</em>), reflects the theological conviction expressed throughout the Psalms that God is the refuge and redeemer of his people.</p>",
        "hitchcock_meaning": "the rock redeems",
        "source_ids": {"easton": "pedahzur", "isbe": "pedahzur"},
        "key_refs": ["Numbers 1:10", "Numbers 2:20", "Numbers 7:54"]
    },
    "pedaiah": {
        "id": "pedaiah",
        "term": "Pedaiah",
        "category": "people",
        "intro": "<p>Pedaiah (meaning: <em>redemption of the Lord</em>) is the name of several individuals in the Old Testament, primarily active in the period of the monarchy and restoration. One Pedaiah was the father of Zebudah, the mother of King Jehoiakim of Judah (2 Kings 23:36), placing him in the royal family circle. Another was a descendant of Jeconiah (Jehoiachin) in the post-exilic Davidic genealogy (1 Chronicles 3:17–19), who appears as either the father or the uncle of Zerubbabel, the governor who led the first return from Babylon.</p><p>Additional men named Pedaiah include a prince of the tribe of Manasseh in David's administration (1 Chronicles 27:20), a man who helped repair the wall of Jerusalem near the Water Gate under Nehemiah (Nehemiah 3:25), a Levite who stood at Ezra's left hand during the public reading of the law (Nehemiah 8:4), and a man appointed as temple treasurer (Nehemiah 13:13). The name's frequency reflects the popularity of names expressing divine redemption in the periods of national crisis and restoration.</p>",
        "hitchcock_meaning": "redemption of the Lord",
        "source_ids": {"easton": "pedaiah", "smith": "pedaiah", "isbe": "pedaiah"},
        "key_refs": ["2 Kings 23:36", "1 Chronicles 3:18", "Nehemiah 3:25", "Nehemiah 8:4"]
    },
    "pekah": {
        "id": "pekah",
        "term": "Pekah",
        "category": "people",
        "intro": "<p>Pekah (meaning: <em>open-eyed</em> or <em>watchful</em>), the son of Remaliah, was a military captain who assassinated King Pekahiah of Israel and seized the throne (2 Kings 15:25), becoming the eighteenth king of the northern kingdom. He reigned approximately 732–730 BC. Pekah formed a coalition with Rezin of Damascus against Judah, launching the Syro-Ephraimite War described in 2 Kings 16 and Isaiah 7, in an attempt to force Judah into their anti-Assyrian alliance.</p><p>His aggression against Judah provoked King Ahaz to appeal to the Assyrian emperor Tiglath-pileser III (Pul) for help. The Assyrian king responded by devastating Israel's northern territories and deporting their populations (2 Kings 15:29) — precisely the catastrophe Pekah's policy had aimed to prevent. Pekah was subsequently assassinated by Hoshea the son of Elah, who became Israel's last king. Isaiah's prophecy in Isaiah 7:1–9, addressed during the Syro-Ephraimite crisis, contains the famous Immanuel sign.</p>",
        "hitchcock_meaning": "he that opens",
        "source_ids": {"easton": "pekah", "smith": "pekah", "isbe": "pekah"},
        "key_refs": ["2 Kings 15:25", "2 Kings 15:29", "2 Kings 15:30", "Isaiah 7:1"]
    },
    "pekahiah": {
        "id": "pekahiah",
        "term": "Pekahiah",
        "category": "people",
        "intro": "<p>Pekahiah (meaning: <em>the Lord has opened his eyes</em> or <em>watchfulness of the Lord</em>) was the son and successor of Menahem on the throne of Israel, reigning as the seventeenth king of the northern kingdom for approximately two years (c. 741–740 BC). The biblical account describes his reign in the standard formulaic terms of Israelite apostasy: he did evil in the sight of the Lord and maintained the sins of Jeroboam the son of Nebat (2 Kings 15:24).</p><p>His brief reign ended violently when his military captain Pekah the son of Remaliah conspired against him with fifty men of the Gileadites, assassinated him in the palace at Samaria in the tower of the king's house, and took the throne (2 Kings 15:25). Pekahiah's short reign and violent end exemplify the political instability of the northern kingdom's final decades, a period of rapid succession and repeated assassination that characterized the collapse leading to the Assyrian conquest of 722 BC.</p>",
        "hitchcock_meaning": "the Lord opens the eyes",
        "source_ids": {"easton": "pekahiah", "smith": "pekahiah", "isbe": "pekahiah"},
        "key_refs": ["2 Kings 15:22", "2 Kings 15:23", "2 Kings 15:24", "2 Kings 15:25"]
    },
    "pekod": {
        "id": "pekod",
        "term": "Pekod",
        "category": "places",
        "intro": "<p>Pekod was a region and probably a tribe in eastern Babylonia, mentioned in Jeremiah 50:21 and Ezekiel 23:23 in oracles against Babylon. In Jeremiah 50:21, God commands the invaders of Babylon: <em>Go up against the land of Merathaim, even against it, and against the inhabitants of Pekod</em> — where Merathaim (double bitterness) and Pekod (visitation) may function as symbolic wordplays on the judgment theme as well as geographical references.</p><p>In Ezekiel 23:23, Pekod is listed alongside Shoa and Koa as Babylonian and Chaldean forces associated with the <em>lovers</em> of Oholibah (Jerusalem), who will turn against her in judgment. Assyrian records mention a people called the Puqūdu in the marshlands and eastern border regions of Babylonia, identified with the biblical Pekod. The name's Hebrew meaning (<em>visitation</em> or <em>punishment</em>) lent itself to prophetic wordplay in contexts of divine judgment.</p>",
        "hitchcock_meaning": "visitation, commandment, obedience",
        "source_ids": {"easton": "pekod", "smith": "pekod", "isbe": "pekod"},
        "key_refs": ["Jeremiah 50:21", "Ezekiel 23:23"]
    },
    "pelaiah": {
        "id": "pelaiah",
        "term": "Pelaiah",
        "category": "people",
        "intro": "<p>Pelaiah (meaning: <em>distinguished of the Lord</em> or <em>the Lord does wonders</em>) is the name of two individuals in the post-exilic period. The first was a descendant of David through Jeconiah (Jehoiachin), listed in the royal genealogy preserved in 1 Chronicles 3:24 — evidence that the Davidic line continued to be tracked after the end of the monarchy and through the Babylonian exile.</p><p>The second Pelaiah was a Levite who assisted Ezra in the great public reading of the Torah (Nehemiah 8:7), one of the thirteen Levites who helped the congregation understand the law as it was read. He also appears among those who sealed the covenant renewal document under Nehemiah (Nehemiah 10:10). Both figures represent the religious leadership of the restoration community, committed to preserving and transmitting the covenant traditions through the crisis of exile and return.</p>",
        "hitchcock_meaning": "the Lord's wonders",
        "source_ids": {"easton": "pelaiah", "smith": "pelaiah", "isbe": "pelaiah"},
        "key_refs": ["1 Chronicles 3:24", "Nehemiah 8:7", "Nehemiah 10:10"]
    },
    "pelatiah": {
        "id": "pelatiah",
        "term": "Pelatiah",
        "category": "people",
        "intro": "<p>Pelatiah (meaning: <em>deliverance of the Lord</em>) is the name of several individuals in Scripture. One was a son of Hananiah and grandson of Zerubbabel, preserving the Davidic line in the post-exilic period (1 Chronicles 3:21). Another sealed the covenant renewal under Nehemiah (Nehemiah 10:22). A third was a Simeonite captain who led his clan against the Amalekite remnant in the hill country of Seir during Hezekiah's reign (1 Chronicles 4:42).</p><p>The most theologically significant Pelatiah was a prince of the people whom Ezekiel encountered in a vision at the east gate of the temple (Ezekiel 11:1). Along with Jaazaniah the son of Azzur, he was giving wicked counsel to Jerusalem's leaders, urging false confidence rather than repentance as the Babylonian threat loomed. As Ezekiel prophesied against them, Pelatiah fell dead — an acted judgment within the vision that illustrated the fate awaiting Jerusalem's corrupt leadership and moved Ezekiel to intercede for the remnant (Ezekiel 11:13).</p>",
        "hitchcock_meaning": "deliverance of the Lord",
        "source_ids": {"easton": "pelatiah", "smith": "pelatiah", "isbe": "pelatiah"},
        "key_refs": ["Ezekiel 11:1", "Ezekiel 11:13", "1 Chronicles 3:21", "Nehemiah 10:22"]
    },
    "peleg": {
        "id": "peleg",
        "term": "Peleg",
        "category": "people",
        "intro": "<p>Peleg (meaning: <em>division</em>) was a son of Eber and a great-great-grandson of Shem, listed in the Table of Nations (Genesis 10:25) and the genealogy from Shem to Abraham (Genesis 11:16–19). His name is given a specific explanation in the text: <em>for in his days was the earth divided</em> (<em>niphlegah ha'aretz</em>). This notice in Genesis 10:25 is one of the most discussed cryptic references in the Pentateuch.</p><p>The <em>division</em> associated with Peleg's time is most naturally understood as the dispersion of peoples following the confusion of languages at Babel (Genesis 11:1–9), an event placed in the same general period as Peleg's generation. Alternative interpretations have proposed a division of the land through irrigation canals or even continental separation, but the textual context most strongly supports the post-Babel dispersion of nations. Through Peleg's line runs the genealogy from Shem to Abraham (Genesis 11:16–26), making him an ancestor of the covenant people.</p>",
        "hitchcock_meaning": "division",
        "source_ids": {"easton": "peleg", "smith": "peleg", "isbe": "peleg"},
        "key_refs": ["Genesis 10:25", "Genesis 11:16", "Luke 3:35"]
    },
    "pelet": {
        "id": "pelet",
        "term": "Pelet",
        "category": "concepts",
        "intro": "<p>Pelet (meaning: <em>deliverance</em> or <em>swiftness</em>) is the name of two individuals mentioned briefly in the genealogical and military records of the Old Testament. The first was a descendant of Judah through Caleb's line, listed among the sons of Jahdai in 1 Chronicles 2:47. The second was a son of Azmaveth and one of the Benjamite warriors who joined David at Ziklag before his accession to the throne (1 Chronicles 12:3), listed among those who were skilled with the bow and could use both hands in slinging stones and shooting arrows.</p><p>Neither Pelet is accorded individual narrative significance beyond these genealogical and military notices. Their inclusion in the Chronicler's lists reflects the comprehensive character of that work's effort to trace the families and warriors who shaped the early Davidic kingdom.</p>",
        "hitchcock_meaning": "deliverance, flight",
        "source_ids": {"easton": "pelet", "smith": "pelet", "isbe": "pelet"},
        "key_refs": ["1 Chronicles 2:47", "1 Chronicles 12:3"]
    },
    "peleth": {
        "id": "peleth",
        "term": "Peleth",
        "category": "concepts",
        "intro": "<p>Peleth (meaning: <em>swiftness</em> or <em>separation</em>) is the name of two individuals in the Old Testament. The first and more notable was a Reubenite whose son On joined the rebellion of Korah, Dathan, and Abiram against Moses and Aaron in the wilderness (Numbers 16:1). On the son of Peleth is named among the conspirators, though he does not appear again in the subsequent account of the rebellion and its judgment, leading some to suggest he may have withdrawn from the conspiracy.</p><p>The second Peleth was a son of Jonathan in the tribe of Judah and the father of Onam, listed in the Judahite genealogy in 1 Chronicles 2:33. He is a descendant of Jerahmeel, representing a branch of Judah's clan structure. Beyond these two genealogical appearances, the name Peleth carries no further narrative significance in Scripture.</p>",
        "hitchcock_meaning": "swiftness, liberation",
        "source_ids": {"easton": "peleth", "smith": "peleth", "isbe": "peleth"},
        "key_refs": ["Numbers 16:1", "1 Chronicles 2:33"]
    },
    "pelethites": {
        "id": "pelethites",
        "term": "Pelethites",
        "category": "people",
        "intro": "<p>The Pelethites were a group of elite royal soldiers who served alongside the Cherethites as David's personal bodyguard throughout his reign. The two groups are consistently mentioned together (2 Samuel 8:18; 15:18; 20:7; 1 Kings 1:38, 44) and formed the core of David's standing professional military force, distinct from the broader tribal army. Their commander was Benaiah the son of Jehoiada, one of David's most trusted officers.</p><p>The origin of the Pelethites is debated. Their name may connect them to the Philistines (<em>Pelishtim</em>), suggesting they were Philistine mercenaries who had attached themselves to David during his time in Philistine territory — similar to the six hundred Gittites under Ittai who remained loyal to David during Absalom's revolt (2 Samuel 15:18–22). They remained loyal to David through Absalom's rebellion and to Solomon against Adonijah's attempted usurpation, escorting Solomon to his anointing at Gihon (1 Kings 1:38). After David's reign, the Pelethites disappear from the biblical record.</p>",
        "hitchcock_meaning": "judges, destroyers",
        "source_ids": {"easton": "pelethites", "smith": "pelethites", "isbe": "pelethites"},
        "key_refs": ["2 Samuel 8:18", "2 Samuel 15:18", "2 Samuel 20:7", "1 Kings 1:38"]
    },
    "pelicans": {
        "id": "pelicans",
        "term": "Pelicans",
        "category": "concepts",
        "intro": "<p>The pelican (Hebrew <em>qa'ath</em>) appears in the Old Testament in lists of unclean birds (Leviticus 11:18; Deuteronomy 14:17) and in prophetic passages where desolate ruins are inhabited by lonely birds. Psalm 102:6 presents the most memorable image: <em>I am like a pelican of the wilderness: I am like an owl of the desert</em> — depicting extreme solitude and desolation in a context of suffering and prayer. The large, ungainly pelican in an arid setting was an arresting image of utter abandonment.</p><p>Zephaniah 2:14 and Isaiah 34:11 both describe the <em>pelican</em> (<em>qa'ath</em>) inhabiting the ruins of once-proud cities — Nineveh and Edom respectively — as an emblem of divine judgment. These large waterbirds, common at the Sea of Galilee and the waters of Merom in ancient Israel, would have been familiar to biblical readers. The precise species behind <em>qa'ath</em> is debated; the pelican is the traditional identification, though some modern translators prefer <em>owl</em> or <em>desert owl</em>.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "pelicans"},
        "key_refs": ["Leviticus 11:18", "Psalms 102:6", "Isaiah 34:11", "Zephaniah 2:14"]
    },
    "penny": {
        "id": "penny",
        "term": "Penny",
        "category": "concepts",
        "intro": "<p>The penny of the New Testament translates the Greek <em>denarion</em> (Latin <em>denarius</em>), the standard silver coin of the Roman Empire and the common daily wage of a laborer in first-century Palestine. It bore the image of the reigning emperor on one face and was the most widely circulating coin in the Roman world. One denarius represented a full day's wage for agricultural workers, as illustrated in the Parable of the Laborers in the Vineyard (Matthew 20:2), where the landowner agrees to pay each worker <em>a penny a day</em>.</p><p>The denarius appears in several significant Gospel scenes: Jesus asks whose image is on the coin when questioned about paying tribute to Caesar, prompting his famous reply, <em>Render to Caesar the things that are Caesar's, and to God the things that are God's</em> (Matthew 22:19–21). In Revelation 6:6, one denarius buys only a quart of wheat or three quarts of barley — a day's wage for a day's food — depicting the famine conditions of the third seal. The Authorized Version consistently renders <em>denarion</em> as <em>penny</em>, though its purchasing power was considerably greater than a modern penny.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "penny", "isbe": "penny"},
        "key_refs": ["Matthew 20:2", "Matthew 22:19", "Mark 6:37", "Revelation 6:6"]
    },
    "pentateuch": {
        "id": "pentateuch",
        "term": "Pentateuch",
        "category": "concepts",
        "intro": "<p>The Pentateuch (from the Greek <em>pentateuchos</em>, five-volumed) designates the first five books of the Old Testament: Genesis, Exodus, Leviticus, Numbers, and Deuteronomy. In Hebrew tradition these books are collectively called the <em>Torah</em> (instruction or law) and are regarded as the foundational revelation of God to Israel through Moses. The division into five books reflects the format of ancient scrolls rather than any internal thematic break, and the five books form a continuous narrative from creation through Moses's death on the plains of Moab.</p><p>The Pentateuch establishes the narrative and theological foundations of all subsequent Scripture: the creation and fall, the covenant with Abraham, the exodus from Egypt, the Sinai covenant and law, and the forty-year wilderness journey. Moses is the dominant human figure and the instrument of divine revelation throughout. The New Testament repeatedly appeals to the Pentateuch as authoritative Scripture, and Jesus's affirmation that <em>Moses wrote of me</em> (John 5:46) anchors a Christological reading of the five books that runs throughout the New Testament epistles and the Gospels.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "pentateuch", "isbe": "pentateuch"},
        "key_refs": ["Exodus 24:4", "Deuteronomy 31:24", "Luke 24:44", "John 5:46"]
    },
    "pentecost": {
        "id": "pentecost",
        "term": "Pentecost",
        "category": "events",
        "intro": "<p>Pentecost (Greek <em>pentekoste</em>, fiftieth) was the second of the three great annual pilgrimage festivals of the Israelite calendar, celebrated fifty days after Passover. In the Old Testament it is called the Feast of Weeks (<em>Shavuot</em>) or the Feast of Harvest (Exodus 23:16; 34:22; Leviticus 23:15–21; Numbers 28:26), marking the completion of the grain harvest with the offering of two leavened loaves of bread — uniquely including leaven, unlike most offerings — and joyful celebration before the Lord.</p><p>The festival acquired its defining significance in Christian history when, fifty days after the resurrection of Christ, the Holy Spirit descended upon the assembled disciples in Jerusalem with wind, fire, and speech in multiple languages (Acts 2:1–4). Peter's proclamation of the risen Christ to the gathered pilgrims from across the Jewish diaspora resulted in approximately three thousand conversions, traditionally regarded as the birthday of the church. Paul's reference to Pentecost in 1 Corinthians 16:8 shows that the date continued to structure apostolic travel plans, maintaining the original festival's calendar significance even within the new covenant community.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "pentecost", "smith": "pentecost", "isbe": "pentecost"},
        "key_refs": ["Acts 2:1", "Acts 2:4", "Leviticus 23:15", "1 Corinthians 16:8"]
    },
    "penuel": {
        "id": "penuel",
        "term": "Penuel",
        "category": "places",
        "intro": "<p>Penuel (meaning: <em>face of God</em>) was a site east of the Jordan River, not far from Succoth, in the territory of Gad. It takes its name from the defining event recorded in Genesis 32:24–32, where Jacob wrestled through the night with a divine figure (identified in Hosea 12:4 as an angel and in Genesis 32:30 as God himself) at the ford of Jabbok. Having prevailed, Jacob named the place Penuel, saying: <em>I have seen God face to face, and my life is preserved.</em> There Jacob received both a wound — the shrinking of his thigh sinew — and a blessing, along with his new name Israel.</p><p>The site appears later in Israel's history: Gideon, pursuing the fleeing Midianites, requested bread from Penuel's inhabitants and was refused; he later destroyed the tower of Penuel and killed its men as punishment (Judges 8:8–9, 17). Jeroboam the son of Nebat subsequently built or fortified Penuel as part of his administrative construction in Transjordan (1 Kings 12:25). The city's theological identity, however, remains permanently linked to Jacob's nocturnal struggle and transformation.</p>",
        "hitchcock_meaning": "face or sight of God",
        "source_ids": {"easton": "penuel", "smith": "penuel", "isbe": "penuel"},
        "key_refs": ["Genesis 32:30", "Hosea 12:4", "Judges 8:8", "1 Kings 12:25"]
    },
    "peor": {
        "id": "peor",
        "term": "Peor",
        "category": "places",
        "intro": "<p>Peor (meaning: <em>opening</em> or <em>gap</em>) designates both a mountain peak in Moab and the Baal cult associated with a sanctuary on that peak. Mount Peor was the third and final location to which Balak king of Moab brought the prophet Balaam in an attempt to curse Israel as they camped in the plains of Moab before entering Canaan (Numbers 23:28). From Peor, Balaam looked out over the Israelite encampment and, constrained by God, blessed rather than cursed the people.</p><p>The name Peor became permanently associated with Israel's catastrophic apostasy recorded in Numbers 25: Israelite men <em>joined themselves to Baal-peor</em>, the Canaanite deity worshipped at this mountain sanctuary, participating in the ritual sexual immorality that accompanied that cult. The resulting plague killed twenty-four thousand and was only stopped when Phinehas executed the offenders. This event at Peor became a defining cautionary memory in Israel (Deuteronomy 4:3; Psalm 106:28), cited by Moses, Joshua (Joshua 22:17), and the apostle Paul (1 Corinthians 10:8) as a warning against spiritual adultery.</p>",
        "hitchcock_meaning": "hole, pit, or opening",
        "source_ids": {"easton": "peor", "smith": "peor", "isbe": "peor"},
        "key_refs": ["Numbers 23:28", "Numbers 25:3", "Deuteronomy 4:3", "Psalm 106:28"]
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
