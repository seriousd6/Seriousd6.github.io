"""
BP Article Synthesis — a1: Aaron → Acre
Covers Easton entries: Aaron through Acre (73 entries)

Sources consulted:
  - data/dictionary/index.json (Easton briefs)
  - data/dictionary/{slug}.json (Easton full HTML + refs, per entry)
  - data/smith/index.json (Smith briefs)
  - data/isbe/index.json (ISBE briefs)
  - data/hitchcock/index.json (name meanings)

Category logic applied:
  - people:   Named biblical individuals
  - places:   Geographic locations (cities, rivers, mountains, regions, valleys)
  - concepts: Theological terms, ritual practices, linguistic entries, units of measure
  - events:   Specific biblical occurrences
  - names:    Hitchcock-only (none in this range — all have Easton entries)

Script: scripts/bp-a1.py
Run: python3 scripts/bp-a1.py
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
    "aaron": {
        "id": "aaron",
        "term": "Aaron",
        "category": "people",
        "intro": "<p>Aaron, the eldest son of Amram and Jochebed and elder brother of Moses, was the first High Priest of Israel. His name is variously interpreted as <em>mountain of strength</em>, <em>mountaineer</em>, or <em>illuminator</em>. Born in Egypt three years before Moses, Aaron served as his brother's spokesman before Pharaoh during the plagues, and was later consecrated to the priesthood at the tabernacle, establishing the Aaronic line that ministered at the sanctuary for generations.</p><p>Though he shared responsibility for the golden calf incident—a grave failure of leadership during Moses's absence on Sinai—Aaron was restored to priestly service. He died on Mount Hor at the age of one hundred and twenty-three, transferring the high-priestly vestments to his son Eleazar. The New Testament Epistle to the Hebrews cites Aaron as a type whose office prefigures the eternal high priesthood of Christ.</p>",
        "hitchcock_meaning": "a teacher; lofty; mountain of strength",
        "source_ids": {"easton": "aaron", "smith": "aaron", "isbe": "aaron"},
        "key_refs": ["Exodus 6:20", "Exodus 4:14", "Exodus 28:1", "Numbers 20:28", "Hebrews 5:4"],
        "sections": []
    },
    "aaronites": {
        "id": "aaronites",
        "term": "Aaronites",
        "category": "people",
        "intro": "<p>The Aaronites were the priestly descendants of Aaron, constituting the hereditary priesthood of Israel. As a distinct group they appear most prominently in the military and administrative records of David's reign: Jehoiada the son of Benaiah led 3,700 Aaronites as fighting men to support David at Hebron. Eleazar the son of Aaron served as their chief during the wilderness period, and Zadok held that leadership role in the time of David.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "aaronites", "smith": "aaronites", "isbe": "aaronites"},
        "key_refs": ["1 Chronicles 12:27", "Numbers 3:32", "1 Chronicles 27:17"],
        "sections": []
    },
    "abaddon": {
        "id": "abaddon",
        "term": "Abaddon",
        "category": "concepts",
        "intro": "<p>Abaddon (meaning <em>destruction</em> or <em>the destroyer</em>) is the Hebrew name of the angel of the bottomless pit, whose Greek equivalent is Apollyon. In the poetic books of the Old Testament—Job, Proverbs, and Psalms—the word appears as a personification of the realm of the dead or the place of ruin, parallel to Sheol. The Revised Version retains the word untranslated in several passages.</p><p>In the New Testament, Abaddon appears in Revelation 9:11 as the name of the angel-king who rules over the locusts of the fifth trumpet judgment. Whether the figure represents Satan himself or a subordinate demonic power, the term in both Testaments conveys the concept of thoroughgoing destruction and the dominion of death.</p>",
        "hitchcock_meaning": "the destroyer",
        "source_ids": {"easton": "abaddon", "smith": "abaddon", "isbe": "abaddon"},
        "key_refs": ["Revelation 9:11", "Job 26:6", "Job 28:22", "Proverbs 15:11"],
        "sections": []
    },
    "abagtha": {
        "id": "abagtha",
        "term": "Abagtha",
        "category": "people",
        "intro": "<p>Abagtha (meaning <em>father of the wine-press</em>) was one of the seven eunuchs who served King Ahasuerus (Xerxes) at his court in Shushan. He is named in Esther 1:10 among those commanded to bring Queen Vashti before the royal feast. Beyond this single episode he is not mentioned elsewhere in Scripture.</p>",
        "hitchcock_meaning": "father of the wine-press",
        "source_ids": {"easton": "abagtha", "smith": "abagtha", "isbe": "abagtha"},
        "key_refs": ["Esther 1:10"],
        "sections": []
    },
    "abana": {
        "id": "abana",
        "term": "Abana",
        "category": "places",
        "intro": "<p>Abana (or Amanah in some manuscripts, meaning <em>stony</em> or <em>perennial</em>) was the chief river of Damascus, known to the Greeks as the Chrysorrhoas (<em>golden stream</em>) and identified with the modern Barada. It rises in the Anti-Lebanon range about twenty-three miles northwest of Damascus, flows south, then divides into three streams that water the city and its surrounding plain, giving Damascus its exceptional fertility.</p><p>Abana is mentioned in 2 Kings 5:12, where Naaman the Syrian general protests that the rivers of Damascus are superior to all the waters of Israel—a remark that reflects the river's renown and its importance to the region's prosperity.</p>",
        "hitchcock_meaning": "made of stone; a building",
        "source_ids": {"easton": "abana"},
        "key_refs": ["2 Kings 5:12"],
        "sections": []
    },
    "abarim": {
        "id": "abarim",
        "term": "Abarim",
        "category": "places",
        "intro": "<p>Abarim (meaning <em>regions beyond</em> or <em>passages</em>) is a mountain range east of the Jordan River, situated in the land of Moab opposite Jericho, along the northeastern shore of the Dead Sea. The name broadly describes the highlands on the Transjordanian plateau. Among its summits is Mount Nebo (Pisgah), from whose top Moses surveyed the Promised Land before his death, being denied entry because of the incident at Meribah.</p><p>The Israelites camped in the mountains of Abarim during their wilderness journey before descending to the plains of Moab. The prophet Jeremiah also alludes to Abarim in the context of Israel's national mourning.</p>",
        "hitchcock_meaning": "passages; passengers",
        "source_ids": {"easton": "abarim", "smith": "abarim"},
        "key_refs": ["Deuteronomy 32:49", "Deuteronomy 3:27", "Numbers 33:47", "Numbers 33:48"],
        "sections": []
    },
    "abba": {
        "id": "abba",
        "term": "Abba",
        "category": "concepts",
        "intro": "<p>Abba is a Syriac and Chaldee word meaning <em>father</em>, used in intimate address to a parent. It appears three times in the New Testament—in Jesus's prayer at Gethsemane (Mark 14:36), in Paul's letter to the Romans (8:15), and in Galatians (4:6)—always paired with its Greek equivalent <em>ho Patēr</em>. The term expresses warm filial affection and confident trust rather than formal address.</p><p>Paul uses Abba in both theological passages to describe the Spirit-enabled cry of adopted children of God, contrasting it with the spirit of slavery and fear. The word passed into ecclesiastical usage as the root of the Latin <em>abbot</em>, the title for the head of a monastery.</p>",
        "hitchcock_meaning": "father",
        "source_ids": {"easton": "abba", "smith": "abba", "isbe": "abba"},
        "key_refs": ["Mark 14:36", "Romans 8:15", "Galatians 4:6"],
        "sections": []
    },
    "abda": {
        "id": "abda",
        "term": "Abda",
        "category": "people",
        "intro": "<p>Abda (meaning <em>servant</em> or <em>servitude</em>) is the name of two men in Scripture. (1.) The father of Adoniram, whom Solomon appointed over the forced labor levy (1 Kings 4:6). (2.) A Levite of the family of Jeduthun who settled in Jerusalem after the exile (Nehemiah 11:17), also identified as Obadiah in 1 Chronicles 9:16.</p>",
        "hitchcock_meaning": "a servant; servitude",
        "source_ids": {"easton": "abda", "smith": "abda", "isbe": "abda"},
        "key_refs": ["1 Kings 4:6", "Nehemiah 11:17", "1 Chronicles 9:16"],
        "sections": []
    },
    "abdeel": {
        "id": "abdeel",
        "term": "Abdeel",
        "category": "people",
        "intro": "<p>Abdeel (meaning <em>a vapor</em> or <em>a cloud of God</em>) was the father of Shelemiah, one of the officials whom King Jehoiakim commanded to arrest the prophet Jeremiah and the scribe Baruch after the reading of Jeremiah's scroll (Jeremiah 36:26). The arrest was not carried out, as the LORD hid both men.</p>",
        "hitchcock_meaning": "a vapor; a cloud of God",
        "source_ids": {"easton": "abdeel", "isbe": "abdeel"},
        "key_refs": ["Jeremiah 36:26"],
        "sections": []
    },
    "abdi": {
        "id": "abdi",
        "term": "Abdi",
        "category": "people",
        "intro": "<p>Abdi (meaning <em>my servant</em>) is the name of three men in the Old Testament: (1.) A Levite ancestor of the musician Ethan appointed by David (1 Chronicles 6:44). (2.) A Levite who assisted in the temple cleansing under Hezekiah (2 Chronicles 29:12). (3.) A member of the clan of Elam who had married a foreign wife during the time of Ezra (Ezra 10:26).</p>",
        "hitchcock_meaning": "my servant",
        "source_ids": {"easton": "abdi", "smith": "abdi", "isbe": "abdi"},
        "key_refs": ["1 Chronicles 6:44", "2 Chronicles 29:12", "Ezra 10:26"],
        "sections": []
    },
    "abdiel": {
        "id": "abdiel",
        "term": "Abdiel",
        "category": "people",
        "intro": "<p>Abdiel (meaning <em>servant of God</em>) was a Gadite chief registered in the genealogical records during the reigns of Jotham king of Judah and Jeroboam king of Israel (1 Chronicles 5:15). He is the son of Guni and appears only in this genealogical notice.</p>",
        "hitchcock_meaning": "servant of God",
        "source_ids": {"easton": "abdiel", "isbe": "abdiel"},
        "key_refs": ["1 Chronicles 5:15"],
        "sections": []
    },
    "abdon": {
        "id": "abdon",
        "term": "Abdon",
        "category": "people",
        "intro": "<p>Abdon (meaning <em>servile</em> or <em>servant</em>) is the name of several persons and one city in the Old Testament. Most prominently, Abdon the son of Hillel, a Pirathonite, served as the tenth judge of Israel; he had forty sons and thirty grandsons who rode on seventy donkeys, a sign of considerable status. He judged Israel eight years and was buried at Pirathon in Ephraim. Two other individuals bear this name: a firstborn son of Gibeon of Benjamin, and a court official under King Josiah.</p>",
        "hitchcock_meaning": "servant; cloud of judgment",
        "source_ids": {"easton": "abdon", "isbe": "abdon"},
        "key_refs": ["Judges 12:13", "Judges 12:14", "Judges 12:15", "2 Chronicles 34:20"],
        "sections": []
    },
    "abednego": {
        "id": "abednego",
        "term": "Abednego",
        "category": "people",
        "intro": "<p>Abednego (meaning <em>servant of Nebo</em>, the Babylonian deity) was the Chaldean name given to Azariah, one of the three young Judean nobles who accompanied Daniel into Babylonian captivity under Nebuchadnezzar. Together with Shadrach (Hananiah) and Meshach (Mishael), he refused to bow before the king's golden image on the plain of Dura and was cast into a superheated furnace, from which all three emerged unharmed through divine intervention. The account, recorded in Daniel 3, became a foundational narrative of faithful endurance under pagan coercion.</p>",
        "hitchcock_meaning": "servant of light; shining",
        "source_ids": {"easton": "abednego", "smith": "abednego"},
        "key_refs": ["Daniel 2:49", "Daniel 3:12", "Daniel 3:28", "Daniel 3:30"],
        "sections": []
    },
    "abel": {
        "id": "abel",
        "term": "Abel",
        "category": "people",
        "intro": "<p>Abel (Hebrew <em>Hebhel</em>, meaning <em>breath</em> or <em>vanity</em>) was the second son of Adam and Eve and the first martyr of Scripture. A keeper of flocks, Abel offered to God the firstlings of his flock and their fat portions—an offering that God accepted, in contrast to the grain offering of his brother Cain. Moved by jealousy, Cain killed Abel, making him the first murder victim recorded in Scripture. The brief account in Genesis 4 emphasizes that Abel's blood cried out to God from the ground.</p><p>In the New Testament, Abel is cited as a paradigm of righteous faith (Hebrews 11:4), the first in a long line of righteous sufferers (Matthew 23:35), and one whose blood spoke less powerfully than the sprinkled blood of Christ (Hebrews 12:24).</p>",
        "hitchcock_meaning": "vanity; breath; vapor",
        "source_ids": {"easton": "abel"},
        "key_refs": ["Genesis 4:1", "Genesis 4:8", "1 John 3:12", "Matthew 23:35", "Hebrews 11:4"],
        "sections": []
    },
    "abel-beth-maachah": {
        "id": "abel-beth-maachah",
        "term": "Abel-beth-maachah",
        "category": "places",
        "intro": "<p>Abel-beth-maachah (meaning <em>meadow of the house of Maachah</em>) was a fortified city in the far north of Israel, near Dan and Ijon in the territory of Naphtali. It was described as a <em>mother in Israel</em>—that is, a significant regional center. The city appears in three episodes: it was besieged by Joab during his pursuit of the rebel Sheba son of Bichri; it was later captured by Ben-hadad of Syria; and it was taken by Tiglath-pileser III of Assyria during his campaign that carried its population into exile.</p>",
        "hitchcock_meaning": "mourning to the house of Maachah",
        "source_ids": {"easton": "abel-beth-maachah"},
        "key_refs": ["2 Samuel 20:14", "2 Samuel 20:19", "1 Kings 15:20", "2 Kings 15:29"],
        "sections": []
    },
    "abel-cheramim": {
        "id": "abel-cheramim",
        "term": "Abel-cheramim",
        "category": "places",
        "intro": "<p>Abel-cheramim (rendered in the King James Version as <em>plain of the vineyards</em>) was a village of the Ammonites, mentioned in Judges 11:33 as the limit of Jephthah's pursuit of the Ammonite forces following his victory. The Revised Version preserves the transliterated name rather than the interpretive rendering. Its exact location is uncertain.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "abel-cheramim", "isbe": "abel-cheramim"},
        "key_refs": ["Judges 11:33"],
        "sections": []
    },
    "abel-meholah": {
        "id": "abel-meholah",
        "term": "Abel-meholah",
        "category": "places",
        "intro": "<p>Abel-meholah (meaning <em>meadow of dancing</em>) was a town in the tribe of Issachar, situated near Beth-shean in the fertile valley where the Wady el-Maleh opens into the Jordan valley. It is most notable as the birthplace and home of the prophet Elisha, where Elijah found him plowing with twelve yoke of oxen when called to prophetic service. The city is also mentioned in the account of Gideon's defeat of the Midianites, to whose territory the routed enemy fled.</p>",
        "hitchcock_meaning": "mourning of sickness",
        "source_ids": {"easton": "abel-meholah", "isbe": "abel-meholah"},
        "key_refs": ["1 Kings 19:16", "1 Kings 4:12", "Judges 7:22"],
        "sections": []
    },
    "abel-mizraim": {
        "id": "abel-mizraim",
        "term": "Abel-mizraim",
        "category": "places",
        "intro": "<p>Abel-mizraim (meaning <em>meadow of Egypt</em> or <em>mourning of Egypt</em>) was a place west of the Jordan at the threshing floor of Atad, where the Egyptians and Israelites mourned seventy days for the patriarch Jacob before carrying his body to burial in Canaan (Genesis 50:4–11). The name reflects both the nationality of those who mourned there and the mourning itself. Its precise location is unknown.</p>",
        "hitchcock_meaning": "the mourning of Egyptians",
        "source_ids": {"easton": "abel-mizraim", "isbe": "abel-mizraim"},
        "key_refs": ["Genesis 50:4", "Genesis 50:11"],
        "sections": []
    },
    "abel-shittim": {
        "id": "abel-shittim",
        "term": "Abel-shittim",
        "category": "places",
        "intro": "<p>Abel-shittim (meaning <em>meadow of the acacias</em>), commonly called simply Shittim, was a location in the plains of Moab east of the Jordan, nearly opposite Jericho. It served as the forty-second and final encampment of Israel before crossing into Canaan. There Israel sinned with the daughters of Moab (Numbers 25), and from there Joshua sent the two spies to Jericho (Joshua 2:1). The prophet Micah invokes the memory of Shittim in recalling God's saving acts from Egypt to Canaan.</p>",
        "hitchcock_meaning": "mourning of thorns",
        "source_ids": {"easton": "abel-shittim", "isbe": "abel-shittim"},
        "key_refs": ["Numbers 25:1", "Numbers 33:49", "Joshua 2:1", "Micah 6:5"],
        "sections": []
    },
    "abez": {
        "id": "abez",
        "term": "Abez",
        "category": "places",
        "intro": "<p>Abez (meaning <em>tin</em> or <em>white</em>) was a town in the northern part of the plain of Esdraelon, allotted to the tribe of Issachar (Joshua 19:20). It is tentatively identified with the ruins of el-Beida. Beyond its inclusion in the tribal allotment list, no further narrative mentions it.</p>",
        "hitchcock_meaning": "an egg; muddy",
        "source_ids": {"easton": "abez", "smith": "abez", "isbe": "abez"},
        "key_refs": ["Joshua 19:20"],
        "sections": []
    },
    "abi-albon": {
        "id": "abi-albon",
        "term": "Abi-albon",
        "category": "people",
        "intro": "<p>Abi-albon (meaning <em>father of strength</em>, i.e., <em>valiant</em>) was a warrior of Arabah who served in David's elite bodyguard of thirty mighty men (2 Samuel 23:31). He is also called Abiel in the parallel list of 1 Chronicles 11:32. Nothing further is recorded of him beyond his name and rank.</p>",
        "hitchcock_meaning": "most intelligent father",
        "source_ids": {"easton": "abi-albon", "isbe": "abi-albon"},
        "key_refs": ["2 Samuel 23:31", "1 Chronicles 11:32"],
        "sections": []
    },
    "abia": {
        "id": "abia",
        "term": "Abia",
        "category": "people",
        "intro": "<p>Abia is the Greek form of the Hebrew name Abijah (meaning <em>my father is the LORD</em>). It occurs in the New Testament genealogy of Jesus (Matthew 1:7) and in Luke 1:5, where it names the priestly division to which Zechariah the father of John the Baptist belonged—the eighth of the twenty-four priestly courses established by David (1 Chronicles 24:10). The form Abiah also appears in 1 Chronicles 7:8 for a son of Becher of Benjamin.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "abia"},
        "key_refs": ["Matthew 1:7", "Luke 1:5", "1 Chronicles 24:10"],
        "sections": []
    },
    "abiasaph": {
        "id": "abiasaph",
        "term": "Abiasaph",
        "category": "people",
        "intro": "<p>Abiasaph (meaning <em>father of gathering</em> or <em>the gatherer</em>) was the youngest of the three sons of Korah the Levite and the head of a Korhite family (Exodus 6:24). He is also called Ebisaph in the Chronicles genealogies (1 Chronicles 6:37). His descendants, the Korahites, were among the gatekeepers and musicians of the temple.</p>",
        "hitchcock_meaning": "consuming father; gathering",
        "source_ids": {"easton": "abiasaph", "smith": "abiasaph", "isbe": "abiasaph"},
        "key_refs": ["Exodus 6:24", "1 Chronicles 6:37"],
        "sections": []
    },
    "abiathar": {
        "id": "abiathar",
        "term": "Abiathar",
        "category": "people",
        "intro": "<p>Abiathar (meaning <em>father of abundance</em> or <em>my father excels</em>) was the son of Ahimelech and the tenth high priest of Israel, fourth in descent from Eli. When Saul slaughtered the priests of Nob, Abiathar alone escaped, fleeing to David with the ephod. He remained David's faithful companion through the years of exile, became a priest of the Davidic court, and served alongside Zadok during David's reign.</p><p>When the succession struggle arose at the end of David's life, Abiathar supported Adonijah's claim over Solomon's. After Solomon's accession, he was stripped of his priestly office and banished to his estate at Anathoth—fulfilling the earlier judgment against the house of Eli—while Zadok assumed sole high-priestly authority. Jesus alludes to Abiathar in Mark 2:26 when recounting David's eating of the showbread.</p>",
        "hitchcock_meaning": "excellent father; father of the remnant",
        "source_ids": {"easton": "abiathar", "smith": "abiathar", "isbe": "abiathar"},
        "key_refs": ["1 Samuel 22:20", "1 Samuel 23:6", "1 Kings 2:26", "1 Kings 2:27"],
        "sections": []
    },
    "abib": {
        "id": "abib",
        "term": "Abib",
        "category": "concepts",
        "intro": "<p>Abib (meaning <em>an ear of corn</em> or <em>green fruit</em>) was the name of the first month of the Hebrew religious calendar, corresponding roughly to late March and April. It was designated the head of the ecclesiastical year in connection with the Exodus and the institution of Passover (Exodus 12:2; 13:4). The month took its name from the stage of the barley crop at that season. After the Babylonian captivity, the month was renamed Nisan, the name used in Nehemiah 2:1 and Esther 3:7.</p>",
        "hitchcock_meaning": "green fruit; ears of corn",
        "source_ids": {"easton": "abib", "smith": "abib", "isbe": "abib"},
        "key_refs": ["Exodus 13:4", "Exodus 23:15", "Nehemiah 2:1", "Leviticus 23:4"],
        "sections": []
    },
    "abida": {
        "id": "abida",
        "term": "Abida",
        "category": "people",
        "intro": "<p>Abida (or Abidah, meaning <em>father of knowledge</em>) was one of the five sons of Midian, who was himself the son of Abraham by his wife Keturah (1 Chronicles 1:33; Genesis 25:4). Abida appears to have been the chief of an Arab tribe. Nothing is recorded of his activities beyond his genealogical position.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "abida", "isbe": "abida"},
        "key_refs": ["1 Chronicles 1:33"],
        "sections": []
    },
    "abidan": {
        "id": "abidan",
        "term": "Abidan",
        "category": "people",
        "intro": "<p>Abidan (meaning <em>father of judgment</em> or <em>judge</em>) was the son of Gideoni and the head of the tribe of Benjamin at the time of the Exodus (Numbers 1:11). He served as Benjamin's representative in the census of the wilderness, commanded the Benjaminite division during the march, and brought his tribe's offering at the dedication of the tabernacle (Numbers 7:60–65).</p>",
        "hitchcock_meaning": "father of judgment",
        "source_ids": {"easton": "abidan", "smith": "abidan", "isbe": "abidan"},
        "key_refs": ["Numbers 1:11", "Numbers 2:22", "Numbers 7:60"],
        "sections": []
    },
    "abieezer": {
        "id": "abieezer",
        "term": "Abieezer",
        "category": "people",
        "intro": "<p>Abieezer (meaning <em>father of help</em>, i.e., <em>helpful</em>) is the name of two Old Testament figures. (1.) A descendant of Manasseh through Hammoleketh; his family clan, the Abiezrites, was the clan of Gideon (Joshua 17:2; Judges 6:34). Gideon invoked Abiezrite loyalty at the threshing floor of Ophrah, and Abieezer's men supported his campaigns. (2.) One of David's thirty mighty men, from Anathoth of Benjamin (2 Samuel 23:27), who also served as the ninth monthly commander of David's rotating military divisions.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "abieezer"},
        "key_refs": ["1 Chronicles 7:18", "Joshua 17:2", "Judges 6:34", "2 Samuel 23:27"],
        "sections": []
    },
    "abiel": {
        "id": "abiel",
        "term": "Abiel",
        "category": "people",
        "intro": "<p>Abiel (meaning <em>father of God</em> or <em>pious</em>) is the name of two men in the Old Testament. (1.) The son of Zeror and father of Ner, making him the great-grandfather of King Saul (1 Samuel 14:51; 1 Chronicles 8:33; 9:39). In 1 Samuel 9:1 he may be identified as the grandfather of Saul directly. (2.) One of David's thirty mighty men, an Arbathite (1 Chronicles 11:32), also called Abi-albon in 2 Samuel 23:31.</p>",
        "hitchcock_meaning": "God my father",
        "source_ids": {"easton": "abiel", "isbe": "abiel"},
        "key_refs": ["1 Samuel 14:51", "1 Chronicles 8:33", "1 Chronicles 11:32"],
        "sections": []
    },
    "abiezrite": {
        "id": "abiezrite",
        "term": "Abiezrite",
        "category": "people",
        "intro": "<p>An Abiezrite was a member of the clan descended from Abieezer of Manasseh. The family was based at Ophrah, and it was to the Abiezrite Joash that the angel of the LORD appeared when he commissioned Joash's son Gideon to deliver Israel from Midian (Judges 6:11). Gideon is repeatedly identified as an Abiezrite (Judges 6:24; 8:32), associating the clan with Israel's deliverance in that period of the judges.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "abiezrite", "isbe": "abiezrite"},
        "key_refs": ["Judges 6:11", "Judges 6:24", "Judges 8:32"],
        "sections": []
    },
    "abigail": {
        "id": "abigail",
        "term": "Abigail",
        "category": "people",
        "intro": "<p>Abigail (meaning <em>father's joy</em> or <em>leader of joy</em>) is the name of two women in the Old Testament. (1.) The wife of the wealthy but churlish Nabal of Carmel, described as a woman of good understanding and beautiful appearance. When David's men came to Nabal seeking provisions and were rudely refused, Abigail intervened with gifts and a persuasive speech that dissuaded David from a violent reprisal. After Nabal died of shock upon learning of his near-ruin, David took Abigail as his wife. She shared his years of exile and bore him his son Chileab.</p><p>(2.) A sister of David who married Jether the Ishmaelite and became the mother of Amasa, the commander whom Absalom appointed over his rebel army (2 Samuel 17:25).</p>",
        "hitchcock_meaning": "the father's joy",
        "source_ids": {"easton": "abigail", "smith": "abigail"},
        "key_refs": ["1 Samuel 25:3", "1 Samuel 25:14", "1 Samuel 25:39", "1 Chronicles 2:16"],
        "sections": []
    },
    "abihail": {
        "id": "abihail",
        "term": "Abihail",
        "category": "people",
        "intro": "<p>Abihail (meaning <em>father of might</em>) is the name of five persons in the Old Testament: (1.) A Levite of the family of Merari (Numbers 3:35). (2.) A woman of the tribe of Judah, wife of Abishur (1 Chronicles 2:29). (3.) A Gadite chief (1 Chronicles 5:14). (4.) A wife of King Rehoboam, descendant of Eliab, David's eldest brother (2 Chronicles 11:18). (5.) The father of Esther and uncle of Mordecai (Esther 2:15; 9:29)—the last being the most significant for biblical narrative, as his daughter became queen of Persia.</p>",
        "hitchcock_meaning": "the father of strength",
        "source_ids": {"easton": "abihail", "smith": "abihail", "isbe": "abihail"},
        "key_refs": ["Numbers 3:35", "2 Chronicles 11:18", "Esther 2:15"],
        "sections": []
    },
    "abihu": {
        "id": "abihu",
        "term": "Abihu",
        "category": "people",
        "intro": "<p>Abihu (meaning <em>he is my father</em> or <em>worshipper of God</em>) was the second son of Aaron and Elisheba (Exodus 6:23). He was consecrated alongside his father and brothers to the Aaronic priesthood, and he ascended the slopes of Sinai with Aaron, Nadab, and seventy elders to witness the divine glory (Exodus 24:1). His priestly career was cut short when he and his brother Nadab offered <em>strange fire</em> before the LORD—incense kindled contrary to divine command—and both died by fire from the LORD's presence (Leviticus 10:1–2). The incident established foundational principles of priestly worship, and Abihu died without sons.</p>",
        "hitchcock_meaning": "he is my father",
        "source_ids": {"easton": "abihu", "smith": "abihu", "isbe": "abihu"},
        "key_refs": ["Exodus 6:23", "Exodus 24:1", "Leviticus 10:1", "Leviticus 10:2", "Numbers 3:4"],
        "sections": []
    },
    "abihud": {
        "id": "abihud",
        "term": "Abihud",
        "category": "people",
        "intro": "<p>Abihud (meaning <em>father of renown</em>) is the name of two persons: (1.) A son of Bela the firstborn of Benjamin (1 Chronicles 8:3), also called Ahihud in verse 7. (2.) A descendant of Zerubbabel who appears in the genealogy of Jesus in Matthew 1:13 (as Abiud in the Greek) and in the parallel Lucan genealogy (Luke 3:26 as Juda). Both are brief genealogical references with no narrative detail.</p>",
        "hitchcock_meaning": "father of praise; confession",
        "source_ids": {"easton": "abihud", "smith": "abihud", "isbe": "abihud"},
        "key_refs": ["1 Chronicles 8:3", "Matthew 1:13"],
        "sections": []
    },
    "abijah": {
        "id": "abijah",
        "term": "Abijah",
        "category": "people",
        "intro": "<p>Abijah (meaning <em>the LORD is my father</em>) is one of the more common names in the Old Testament, borne by at least eight individuals. The most historically significant is the king of Judah, son of Rehoboam and grandson of Solomon, who reigned three years and was known for his confrontation with Jeroboam king of Israel—a confrontation in which he claimed the legitimacy of the Davidic covenant even while his own reign was morally ambiguous (1 Kings 15:1–8; 2 Chronicles 13). A second notable Abijah was the second son of Samuel, whose corrupt conduct as a judge at Beer-sheba contributed to the popular demand for a king (1 Samuel 8:2).</p>",
        "hitchcock_meaning": "the Lord is my father",
        "source_ids": {"easton": "abijah", "isbe": "abijah"},
        "key_refs": ["1 Kings 15:1", "2 Chronicles 13:1", "1 Samuel 8:2", "1 Chronicles 24:10"],
        "sections": []
    },
    "abijam": {
        "id": "abijam",
        "term": "Abijam",
        "category": "people",
        "intro": "<p>Abijam (meaning <em>father of the sea</em>) is the name used in the books of Kings for the king of Judah known elsewhere as Abijah—the son and successor of Rehoboam (1 Kings 15:1–8). He reigned three years in Jerusalem. His mother was Maachah the daughter of Abishalom. Though he walked in his father's sins, the kingdom was preserved for David's sake. For a fuller account see <strong>Abijah</strong>.</p>",
        "hitchcock_meaning": "father of the sea",
        "source_ids": {"easton": "abijam", "smith": "abijam", "isbe": "abijam"},
        "key_refs": ["1 Kings 15:1", "1 Kings 15:7", "1 Kings 15:8"],
        "sections": []
    },
    "abilene": {
        "id": "abilene",
        "term": "Abilene",
        "category": "places",
        "intro": "<p>Abilene was a district on the eastern slope of the Anti-Lebanon mountains, named after its chief city Abila. It lay in the Suk Wady Barada between Baalbek and Damascus, approximately eighteen miles northwest of Damascus. In the New Testament it appears only in Luke 3:1, where it is identified as the territory administered by Lysanias as tetrarch at the time John the Baptist began his ministry. It was subsequently incorporated into the growing kingdom of Herod Agrippa I.</p>",
        "hitchcock_meaning": "the father of mourning",
        "source_ids": {"easton": "abilene", "smith": "abilene", "isbe": "abilene"},
        "key_refs": ["Luke 3:1"],
        "sections": []
    },
    "abimael": {
        "id": "abimael",
        "term": "Abimael",
        "category": "people",
        "intro": "<p>Abimael (meaning <em>father sent from God</em>) was a son of Joktan in the Semitic table of nations (Genesis 10:28; 1 Chronicles 1:22). He is listed among the thirteen sons of Joktan who settled in the Arabian peninsula. No further narrative details are recorded; the name appears only in genealogical contexts.</p>",
        "hitchcock_meaning": "a father sent from God",
        "source_ids": {"easton": "abimael", "smith": "abimael", "isbe": "abimael"},
        "key_refs": ["Genesis 10:28", "1 Chronicles 1:22"],
        "sections": []
    },
    "abimelech": {
        "id": "abimelech",
        "term": "Abimelech",
        "category": "people",
        "intro": "<p>Abimelech (meaning <em>my father a king</em> or <em>father of a king</em>) functioned as a dynastic or royal title among Philistine kings, analogous to <em>Pharaoh</em> in Egypt. Two distinct Philistine kings of Gerar bear this name in the patriarchal narratives: one who took Sarah into his household in the time of Abraham and was warned by God in a dream (Genesis 20), and another in the time of Isaac with whom a covenant was made at Beer-sheba (Genesis 26).</p><p>The name is also borne by Abimelech the son of Gideon by a Shechemite concubine, who murdered seventy of his brothers to seize rule over Israel and reigned three years before being fatally wounded by a millstone dropped by a woman at Thebez (Judges 9)—a cautionary account of illegitimate kingship. The superscription of Psalm 34 uses the name for the Philistine king with whom David sought refuge.</p>",
        "hitchcock_meaning": "father of the king",
        "source_ids": {"easton": "abimelech", "smith": "abimelech", "isbe": "abimelech"},
        "key_refs": ["Genesis 20:1", "Genesis 26:1", "Judges 9:1", "Judges 9:53", "Psalms 34:1"],
        "sections": []
    },
    "abinadab": {
        "id": "abinadab",
        "term": "Abinadab",
        "category": "people",
        "intro": "<p>Abinadab (meaning <em>father of nobleness</em> or <em>noble</em>) is the name of four men in the Old Testament. The most prominent is the Levite of Kirjath-jearim in whose house the ark of the covenant rested for twenty years after its return from Philistine territory, until David brought it to Jerusalem. His son Eleazar was consecrated to keep the ark; his other sons Uzzah and Ahio drove the cart on which it was transported (1 Samuel 7:1; 2 Samuel 6:3). The name is also borne by the second son of Jesse passed over when Samuel anointed David (1 Samuel 16:8), a son of Saul killed at Gilboa (1 Samuel 31:2), and a son-in-law of Solomon (1 Kings 4:11).</p>",
        "hitchcock_meaning": "father of a vow, or of willingness",
        "source_ids": {"easton": "abinadab", "smith": "abinadab", "isbe": "abinadab"},
        "key_refs": ["1 Samuel 7:1", "2 Samuel 6:3", "1 Samuel 16:8", "1 Samuel 31:2"],
        "sections": []
    },
    "abinoam": {
        "id": "abinoam",
        "term": "Abinoam",
        "category": "people",
        "intro": "<p>Abinoam (meaning <em>father of kindness</em>) was the father of Barak, the military leader who accompanied the prophetess Deborah in the campaign against Sisera and the army of Jabin king of Canaan (Judges 4:6). He is mentioned only in Judges 4:6 and 5:1 in connection with his son's name. No further biographical information is recorded.</p>",
        "hitchcock_meaning": "father of beauty",
        "source_ids": {"easton": "abinoam", "smith": "abinoam", "isbe": "abinoam"},
        "key_refs": ["Judges 4:6", "Judges 5:1"],
        "sections": []
    },
    "abiram": {
        "id": "abiram",
        "term": "Abiram",
        "category": "people",
        "intro": "<p>Abiram (meaning <em>father of height</em>, i.e., <em>proud</em>) is the name of two men in the Old Testament. (1.) The son of Eliab of the tribe of Reuben, who joined Korah's conspiracy against the authority of Moses and Aaron in the wilderness. When Moses summoned him, he refused to appear. The divine judgment that followed swallowed Abiram, his household, and the other conspirators in an earthquake, while fire consumed the 250 who offered incense. The event is cited in Psalms 106:17 and Numbers 26:9 as a perpetual warning. (2.) The firstborn son of Hiel of Bethel, who died when his father laid the foundations of Jericho—fulfilling Joshua's curse (1 Kings 16:34).</p>",
        "hitchcock_meaning": "high father; father of deceit",
        "source_ids": {"easton": "abiram", "smith": "abiram", "isbe": "abiram"},
        "key_refs": ["Numbers 16:1", "Numbers 16:27", "Psalms 106:17", "1 Kings 16:34"],
        "sections": []
    },
    "abishag": {
        "id": "abishag",
        "term": "Abishag",
        "category": "people",
        "intro": "<p>Abishag (meaning <em>ignorance of the father</em> or <em>given to error</em>) was a young woman of Shunem, distinguished for her beauty, who was chosen to minister to the aged King David by lying close to him for warmth. Though she became his wife, David had no conjugal relations with her (1 Kings 1:3–4). After David's death, Adonijah requested Abishag as his wife through Bathsheba, an appeal Solomon interpreted as a veiled claim to the throne—leading to Adonijah's execution (1 Kings 2:17–25). Abishag thus became an unintended flashpoint in the Solomonic succession.</p>",
        "hitchcock_meaning": "ignorance of the father",
        "source_ids": {"easton": "abishag", "smith": "abishag", "isbe": "abishag"},
        "key_refs": ["1 Kings 1:3", "1 Kings 1:15", "1 Kings 2:17", "1 Kings 2:22"],
        "sections": []
    },
    "abishai": {
        "id": "abishai",
        "term": "Abishai",
        "category": "people",
        "intro": "<p>Abishai (meaning <em>the present of my father</em> or <em>desirous of a gift</em>) was the eldest son of Zeruiah, David's sister, and the brother of Joab and Asahel. He was one of David's most loyal and fierce warriors. He accompanied David alone into Saul's camp and restrained the king from killing Saul himself (1 Samuel 26:5–9). He commanded a third of David's army at the battle of Mahanaim against Absalom, rescued David when he was in danger from Ishbi-benob the Philistine, and killed Sheba son of Bichri's rebellion along with Joab. Though valiant, he shared in some of Joab's more violent excesses.</p>",
        "hitchcock_meaning": "the present of my father",
        "source_ids": {"easton": "abishai", "isbe": "abishai"},
        "key_refs": ["1 Samuel 26:5", "2 Samuel 18:2", "2 Samuel 21:17", "1 Chronicles 2:16"],
        "sections": []
    },
    "abishua": {
        "id": "abishua",
        "term": "Abishua",
        "category": "people",
        "intro": "<p>Abishua (meaning <em>father of welfare</em> or <em>fortunate</em>) is the name of two men in the Old Testament: (1.) A grandson of Benjamin through Bela (1 Chronicles 8:4). (2.) The son of Phinehas the high priest and grandson of Eleazar, making him the great-grandson of Aaron. He is listed in the high-priestly genealogy in 1 Chronicles 6:4–5 and in the priestly line of Ezra (Ezra 7:5).</p>",
        "hitchcock_meaning": "father of salvation",
        "source_ids": {"easton": "abishua", "isbe": "abishua"},
        "key_refs": ["1 Chronicles 6:4", "1 Chronicles 6:5", "Ezra 7:5"],
        "sections": []
    },
    "abishur": {
        "id": "abishur",
        "term": "Abishur",
        "category": "people",
        "intro": "<p>Abishur (meaning <em>father of the wall</em>, i.e., <em>mason</em>) was a son of Shammai of the tribe of Judah (1 Chronicles 2:28–29). His wife was Abihail, and his sons were Ahban and Molid. He appears only in the genealogical records of Judah's family.</p>",
        "hitchcock_meaning": "father of the wall; father of uprightness",
        "source_ids": {"easton": "abishur", "smith": "abishur", "isbe": "abishur"},
        "key_refs": ["1 Chronicles 2:28", "1 Chronicles 2:29"],
        "sections": []
    },
    "abital": {
        "id": "abital",
        "term": "Abital",
        "category": "people",
        "intro": "<p>Abital (meaning <em>father of dew</em> or <em>fresh</em>) was the fifth wife of David, who bore him Shephatiah at Hebron during his seven-and-a-half-year reign over Judah before becoming king over all Israel (2 Samuel 3:4; 1 Chronicles 3:3).</p>",
        "hitchcock_meaning": "the father of the dew; or of the shadow",
        "source_ids": {"easton": "abital", "smith": "abital", "isbe": "abital"},
        "key_refs": ["2 Samuel 3:4", "1 Chronicles 3:3"],
        "sections": []
    },
    "abitub": {
        "id": "abitub",
        "term": "Abitub",
        "category": "people",
        "intro": "<p>Abitub (meaning <em>father of goodness</em>) was a Benjamite, son of Shaharaim by his wife Hushim (1 Chronicles 8:11). He appears only in the genealogical records of Benjamin.</p>",
        "hitchcock_meaning": "father of goodness",
        "source_ids": {"easton": "abitub", "smith": "abitub", "isbe": "abitub"},
        "key_refs": ["1 Chronicles 8:11"],
        "sections": []
    },
    "abjects": {
        "id": "abjects",
        "term": "Abjects",
        "category": "concepts",
        "intro": "<p>Abjects is the translation in Psalm 35:15 of a Hebrew word meaning <em>smiters</em>, applied to persons who struck at David with their tongues—likely slanderers and mockers. Easton notes the parallel with Jeremiah 18:18, where the same hostile use of speech appears. The English rendering has fallen from use; modern translations render the Hebrew more variously as <em>slanderers</em> or <em>assailants</em>.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "abjects"},
        "key_refs": ["Psalms 35:15", "Jeremiah 18:18"],
        "sections": []
    },
    "ablution": {
        "id": "ablution",
        "term": "Ablution",
        "category": "concepts",
        "intro": "<p>Ablution, or ritual washing, was a pervasive element of Israelite worship and purity law. Its principal occasions included: the consecration of priests before investiture (Leviticus 8:6); the required handwashing of priests before approaching the altar (Exodus 30:17–21); purification after contact with uncleanness, childbirth, or a corpse (Leviticus 12; Numbers 19); and the symbolic washing of hands to disclaim bloodguilt (Deuteronomy 21:1–6; cf. Psalm 26:6; Matthew 27:24).</p><p>In the New Testament, Jesus and Paul both distinguish the inner transformation of the heart from mere outward washing (Mark 7:1–8; Colossians 2:16–17), while Christian baptism reinterprets ritual ablution as the sign of spiritual cleansing and union with Christ's death and resurrection.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ablution", "smith": "ablution", "isbe": "ablution"},
        "key_refs": ["Leviticus 8:6", "Exodus 30:17", "Psalms 26:6", "Matthew 27:24"],
        "sections": []
    },
    "abner": {
        "id": "abner",
        "term": "Abner",
        "category": "people",
        "intro": "<p>Abner (meaning <em>father of light</em> or <em>enlightening</em>) was the son of Ner, the uncle of Saul, and commander-in-chief of Saul's army. He introduced David to the court after the defeat of Goliath (1 Samuel 17:57). After Saul's death at Gilboa, Abner supported the claim of Ish-bosheth against David's kingship over Judah, commanding the northern tribes' forces in the prolonged civil conflict that followed.</p><p>When Abner quarreled with Ish-bosheth over a concubine of Saul, he opened secret negotiations to transfer his allegiance to David. The negotiations were nearly complete when Joab, whose brother Asahel Abner had killed in battle, ambushed and murdered Abner at Hebron. David's public mourning over Abner, including a lament and a formal funeral, demonstrated his innocence in the killing and won the loyalty of Israel's tribes.</p>",
        "hitchcock_meaning": "father of light",
        "source_ids": {"easton": "abner", "smith": "abner", "isbe": "abner"},
        "key_refs": ["1 Samuel 14:50", "2 Samuel 2:8", "2 Samuel 3:27", "2 Samuel 3:31"],
        "sections": []
    },
    "abomination": {
        "id": "abomination",
        "term": "Abomination",
        "category": "concepts",
        "intro": "<p>Abomination translates several Hebrew and Greek words denoting something morally or ceremonially detestable to God or to the sensibilities of a people. In the Old Testament the term covers a wide range: practices that violate purity distinctions (such as eating unclean animals), the sacrificial offerings of apostate Israel which became loathsome to God, and idolatry in its many forms. In one specific sense, the term entered eschatological language in Daniel's references to the <em>abomination of desolation</em>—a desecrating presence in the sanctuary—which Jesus cited as a future sign in his Olivet discourse (Matthew 24:15; Mark 13:14).</p><p>Culturally, the Egyptians considered sharing meals with foreigners an abomination; Israelite law declared the practices of Canaanite nations abominations; and the New Testament uses the concept to describe that which is exalted among humans but detestable before God (Luke 16:15).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "abomination", "isbe": "abomination"},
        "key_refs": ["Genesis 43:32", "Leviticus 18:22", "Daniel 9:27", "Matthew 24:15"],
        "sections": []
    },
    "abraham": {
        "id": "abraham",
        "term": "Abraham",
        "category": "people",
        "intro": "<p>Abraham (meaning <em>father of a multitude</em>), the son of Terah, was the founding patriarch of the nation of Israel and, in the New Testament's reckoning, the spiritual ancestor of all who believe. Originally called Abram (<em>exalted father</em>), he was born in Ur of the Chaldeans and migrated with his father's household to Haran, where he remained until his father's death. At the age of seventy-five he obeyed God's call to leave kindred and country for an unspecified land, which proved to be Canaan—a faith-response cited in Hebrews 11:8 as the paradigm of obedience.</p><p>The divine covenant with Abraham—promising land, descendants, and a blessing to extend to all nations—is the theological axis on which the entire scriptural narrative turns. His faith was demonstrated supremely in the near-sacrifice of his son Isaac (Genesis 22), which became for Paul the defining instance of justification by faith rather than works (Romans 4; Galatians 3). Jesus appealed to Abraham's testimony against his opponents (John 8:56) and affirmed the resurrection through reference to the God of Abraham (Matthew 22:32).</p>",
        "hitchcock_meaning": "father of a great multitude",
        "source_ids": {"easton": "abraham", "smith": "abraham", "isbe": "abraham"},
        "key_refs": ["Genesis 12:1", "Genesis 15:6", "Genesis 22:1", "Romans 4:3", "Hebrews 11:8"],
        "sections": []
    },
    "abrahams-bosom": {
        "id": "abrahams-bosom",
        "term": "Abraham's bosom",
        "category": "concepts",
        "intro": "<p>Abraham's bosom is an expression appearing in Jesus's parable of the rich man and Lazarus (Luke 16:22–23), where the poor Lazarus dies and is carried by angels to rest at Abraham's side—a place of comfort, rest, and honor. The image reflects the custom of reclining at table on couches, where a guest's head would rest near the chest of the person reclining above him; to be <em>in Abraham's bosom</em> was thus to occupy the place of closest intimacy and honor at the patriarch's banquet table in Paradise.</p><p>In Jewish thought the phrase described the highest state of blessedness in the afterlife, and Jesus employs it to affirm both the reversal of earthly fortunes after death and the reality of conscious existence and distinction in the intermediate state.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "abrahams-bosom", "isbe": "abrahams-bosom"},
        "key_refs": ["Luke 16:22", "Luke 16:23", "Matthew 8:11"],
        "sections": []
    },
    "abram": {
        "id": "abram",
        "term": "Abram",
        "category": "people",
        "intro": "<p>Abram (meaning <em>exalted father</em> or <em>high father</em>) was the birth name of the patriarch Abraham before God changed it at the institution of the covenant of circumcision (Genesis 17:5). The name Abram is used throughout the narrative of Genesis 11:27–17:4; subsequent references to him as Abram in later books are typically retrospective. For a full treatment, see <strong>Abraham</strong>.</p>",
        "hitchcock_meaning": "high father",
        "source_ids": {"easton": "abram", "smith": "abram", "isbe": "abram"},
        "key_refs": ["Genesis 11:27", "Genesis 17:5"],
        "sections": []
    },
    "abronah": {
        "id": "abronah",
        "term": "Abronah",
        "category": "places",
        "intro": "<p>Abronah (called Ebronah in the King James Version) was one of Israel's halting-places in the wilderness, listed in Numbers 33:34–35 as the encampment just before Ezion-gaber on the shore of the Red Sea. No narrative event is attached to the site, and its precise location is unknown.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "abronah", "isbe": "abronah"},
        "key_refs": ["Numbers 33:34", "Numbers 33:35"],
        "sections": []
    },
    "absalom": {
        "id": "absalom",
        "term": "Absalom",
        "category": "people",
        "intro": "<p>Absalom (meaning <em>father of peace</em>) was the third son of David and Maachah, daughter of the king of Geshur, renowned in Scripture for his striking physical beauty and the extraordinary abundance of his hair. His public career began with the blood-revenge he executed against his half-brother Amnon for the rape of his sister Tamar, an act that drove him into a three-year exile in Geshur. Recalled by Joab's stratagem, he was eventually restored to David's presence, only to orchestrate a full-scale rebellion that briefly drove David from Jerusalem.</p><p>Absalom was defeated in the forest of Ephraim, where his famously long hair caught in an oak tree, leaving him suspended and vulnerable. Joab killed him contrary to David's express command, and David's lament—<em>O my son Absalom!</em>—became one of Scripture's most moving expressions of paternal grief (2 Samuel 18:33).</p>",
        "hitchcock_meaning": "father of peace",
        "source_ids": {"easton": "absalom", "smith": "absalom"},
        "key_refs": ["2 Samuel 3:3", "2 Samuel 14:25", "2 Samuel 15:10", "2 Samuel 18:14", "2 Samuel 18:33"],
        "sections": []
    },
    "acacia": {
        "id": "acacia",
        "term": "Acacia",
        "category": "concepts",
        "intro": "<p>Acacia (Hebrew <em>shittah</em>, plural <em>shittim</em>) refers most probably to <em>Acacia seyal</em>, the gum-arabic tree, a thorny, gnarled species resembling the hawthorn, capable of reaching a height of twenty feet. Its wood—dense, close-grained, and resistant to decay and insects—was the material of choice for the principal furnishings of the tabernacle: the ark of the covenant, the table of showbread, the altar of incense, and the altar of burnt offering, as well as the upright boards of the structure itself (Exodus 25–27; 36–38).</p><p>The tree is also called the <em>shittah tree</em> in Isaiah 41:19, where it appears among trees God promises to plant in the wilderness as a sign of restoration. Its association with the tabernacle gave the wood a place of singular importance in Israel's sacred architecture.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "acacia", "isbe": "acacia"},
        "key_refs": ["Exodus 25:5", "Exodus 26:15", "Isaiah 41:19"],
        "sections": []
    },
    "accad": {
        "id": "accad",
        "term": "Accad",
        "category": "places",
        "intro": "<p>Accad (meaning <em>highland</em> or <em>spark</em>) was one of the four cities that formed Nimrod's original kingdom in the land of Shinar, alongside Babel, Erech, and Calneh (Genesis 10:10). It was also the name of the broader region of northern Babylonia of which the city was the capital. The Accadians, who migrated from the eastern highlands after the flood, attained a high level of civilization and contributed significantly to the literary and cultural heritage of ancient Mesopotamia.</p>",
        "hitchcock_meaning": "a vessel; pitcher; spark",
        "source_ids": {"easton": "accad", "smith": "accad"},
        "key_refs": ["Genesis 10:10"],
        "sections": []
    },
    "accho": {
        "id": "accho",
        "term": "Accho",
        "category": "places",
        "intro": "<p>Accho (meaning <em>sultry</em> or <em>pressed together</em>) was a harbor town and port on the Phoenician coast, allotted to the tribe of Asher but never actually subdued by them (Judges 1:31). In the Hellenistic period it was renamed Ptolemais after Ptolemy II of Egypt. Paul landed there on his final journey to Jerusalem (Acts 21:7). During the Crusades it was known as Acra and later as St. Jean d'Acre, or simply Acre—a name retained in its modern form as Akko on the Bay of Haifa.</p>",
        "hitchcock_meaning": "close; pressed together",
        "source_ids": {"easton": "accho", "smith": "accho"},
        "key_refs": ["Judges 1:31", "Acts 21:7"],
        "sections": []
    },
    "accuser": {
        "id": "accuser",
        "term": "Accuser",
        "category": "concepts",
        "intro": "<p>Accuser is one of the primary designations of Satan in Scripture. Revelation 12:10 calls him <em>the accuser of our brothers</em>, one who brings charges against believers before God day and night. The same role is implied in Job 1–2, where the adversary (Hebrew <em>śāṭān</em>) appears in the heavenly court to question Job's integrity, and in Zechariah 3:1, where an accuser stands at the right hand of Joshua the high priest to resist him.</p><p>In the New Testament the Greek <em>diabolos</em> (slanderer) captures the same concept. Jesus also refers to the devil as <em>the accuser</em> in John 8:44. The accusatory role is overcome not by defensiveness but by the blood of the Lamb and the testimony of the saints (Revelation 12:11).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "accuser", "isbe": "accuser"},
        "key_refs": ["Revelation 12:10", "Job 1:6", "Zechariah 3:1", "John 8:44"],
        "sections": []
    },
    "aceldama": {
        "id": "aceldama",
        "term": "Aceldama",
        "category": "places",
        "intro": "<p>Aceldama (Aramaic for <em>field of blood</em>) was the name the Jerusalem residents gave to the potter's field purchased with the thirty pieces of silver returned by Judas Iscariot after the betrayal of Jesus. Matthew 27:6–8 records that the chief priests, unable to return the blood-money to the temple treasury, used it to buy the potter's field as a burial place for foreigners. Acts 1:18–19 offers a complementary account in which Judas himself acquired the field, which became associated with his death.</p><p>The site lies on a narrow terrace on the south face of the Valley of Hinnom, where it meets the Kidron Valley. Its modern Arabic name is Hak ed-Damm.</p>",
        "hitchcock_meaning": "field of blood",
        "source_ids": {"easton": "aceldama", "smith": "aceldama", "isbe": "aceldama"},
        "key_refs": ["Matthew 27:7", "Matthew 27:8", "Acts 1:19"],
        "sections": []
    },
    "achaia": {
        "id": "achaia",
        "term": "Achaia",
        "category": "places",
        "intro": "<p>Achaia was originally a narrow coastal district in the northwest of the Peloponnesus, but by New Testament times the name designated the entire southern half of Greece—the Roman province administered from Corinth, with Macedonia as its northern counterpart. Paul first visited it on his second missionary journey, preaching in Athens and establishing a congregation in Corinth, where he remained eighteen months and before whose proconsul Gallio he was arraigned (Acts 18:12).</p><p>Achaia figures prominently in Paul's letters: he commends the churches of Macedonia and Achaia for their generosity toward Jerusalem (Romans 15:26), reports on the first converts of the region (1 Corinthians 16:15), and in 2 Corinthians praises their participation in the collection. Apollos strengthened the disciples there after Priscilla and Aquila had instructed him (Acts 18:27).</p>",
        "hitchcock_meaning": "grief; trouble",
        "source_ids": {"easton": "achaia", "smith": "achaia", "isbe": "achaia"},
        "key_refs": ["Acts 18:12", "Romans 15:26", "1 Corinthians 16:15", "2 Corinthians 1:1"],
        "sections": []
    },
    "achaichus": {
        "id": "achaichus",
        "term": "Achaichus",
        "category": "people",
        "intro": "<p>Achaichus was a member of the church at Corinth who, together with Fortunatus and Stephanas, visited Paul during his extended stay at Ephesus (1 Corinthians 16:17). Paul describes their visit as having supplied what was lacking in his contact with the Corinthian congregation. The three men are generally understood to have been the bearers of the letter from Corinth to which Paul responds in 1 Corinthians 7:1. Nothing further is known about Achaichus beyond this single reference.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "achaichus"},
        "key_refs": ["1 Corinthians 16:17", "1 Corinthians 7:1"],
        "sections": []
    },
    "achan": {
        "id": "achan",
        "term": "Achan",
        "category": "people",
        "intro": "<p>Achan (also called Achar, meaning <em>one who troubles</em>) was a man of the tribe of Judah whose covert sin brought military defeat on Israel at Ai. During the conquest of Jericho, which had been placed under the ban of total dedication to the LORD, Achan secretly took a Babylonian garment, two hundred shekels of silver, and a wedge of gold, hiding them under his tent floor. Israel's subsequent defeat at Ai was traced to this violation of the sacred ban.</p><p>Joshua's casting of lots identified Achan, who confessed. He and his household and possessions were taken to the Valley of Achor, stoned, and burned. The place-name Achor (<em>trouble</em>) preserved the memory of the episode, while the prophets Isaiah and Hosea later reinterpreted the Valley of Achor as a place of hope and restoration (Isaiah 65:10; Hosea 2:15).</p>",
        "hitchcock_meaning": "or Achar, he that troubleth",
        "source_ids": {"easton": "achan", "smith": "achan", "isbe": "achan"},
        "key_refs": ["Joshua 7:1", "Joshua 7:20", "Joshua 7:24", "1 Chronicles 2:7"],
        "sections": []
    },
    "achbor": {
        "id": "achbor",
        "term": "Achbor",
        "category": "people",
        "intro": "<p>Achbor (meaning <em>gnawing</em> or <em>mouse</em>) is the name of two men in the Old Testament: (1.) An Edomite king who reigned before Israel had any king (Genesis 36:38; 1 Chronicles 1:49). (2.) An official of King Josiah, son of Micaiah, who was sent with others to the prophetess Huldah to inquire of the LORD concerning the book of the law discovered during temple repairs (2 Kings 22:12, 14). His son Elnathan later served under Jehoiakim.</p>",
        "hitchcock_meaning": "a rat; bruising",
        "source_ids": {"easton": "achbor", "smith": "achbor", "isbe": "achbor"},
        "key_refs": ["Genesis 36:38", "2 Kings 22:12", "2 Kings 22:14"],
        "sections": []
    },
    "achish": {
        "id": "achish",
        "term": "Achish",
        "category": "people",
        "intro": "<p>Achish (possibly a royal title among the Philistines, meaning <em>thus it is</em>) was the king of the Philistine city of Gath. David sought refuge at his court twice during his flight from Saul. On the first visit, sensing the danger of his situation, David feigned madness to escape (1 Samuel 21:10–15)—an episode recalled in the superscription of Psalm 34, where the king is called Abimelech. On the second occasion David came with six hundred warriors, and Achish allocated him Ziklag as a residence. Achish trusted David as a loyal vassal, but the other Philistine lords refused to allow David to join their campaign against Saul, sending him back to Ziklag (1 Samuel 29:2–11).</p>",
        "hitchcock_meaning": "thus it is; how is this",
        "source_ids": {"easton": "achish", "smith": "achish", "isbe": "achish"},
        "key_refs": ["1 Samuel 21:10", "1 Samuel 27:5", "1 Samuel 29:2", "Psalms 34:1"],
        "sections": []
    },
    "achmetha": {
        "id": "achmetha",
        "term": "Achmetha",
        "category": "places",
        "intro": "<p>Achmetha (Ecbatana in Greek and classical sources) was the capital of ancient Media, situated on the site of the modern Iranian city of Hamadan. It served as the summer residence of the Persian kings and earlier of the Median monarchs, and of Cyrus and Cambyses. Ezra 6:2 records that a royal memorandum confirming Cyrus's original decree permitting the rebuilding of the Jerusalem temple was found there in the royal archives. Achmetha's elevation (about 6,000 feet) and cool climate made it a preferred retreat from the heat of Persepolis and Susa.</p>",
        "hitchcock_meaning": "brother of death",
        "source_ids": {"easton": "achmetha", "smith": "achmetha", "isbe": "achmetha"},
        "key_refs": ["Ezra 6:2"],
        "sections": []
    },
    "achor": {
        "id": "achor",
        "term": "Achor",
        "category": "places",
        "intro": "<p>Achor (meaning <em>trouble</em>) was a valley near Jericho where Achan and his household were executed following the discovery of his sin after Israel's defeat at Ai (Joshua 7:24–26). The name became proverbial for the source of Israel's corporate calamity. The prophets Isaiah and Hosea later transformed the valley's connotations: Isaiah envisions the Valley of Achor as fertile grazing land in the coming restoration (Isaiah 65:10), while Hosea promises it will become a <em>door of hope</em> in God's renewed covenant with Israel (Hosea 2:15)—a theological reversal of the judgment it originally commemorated.</p>",
        "hitchcock_meaning": "trouble",
        "source_ids": {"easton": "achor", "isbe": "achor"},
        "key_refs": ["Joshua 7:24", "Joshua 7:26", "Isaiah 65:10", "Hosea 2:15"],
        "sections": []
    },
    "achsah": {
        "id": "achsah",
        "term": "Achsah",
        "category": "people",
        "intro": "<p>Achsah (meaning <em>anklet</em> or <em>bursting the veil</em>) was the only daughter of Caleb the son of Jephunneh. Caleb offered her as a prize of marriage to whoever would take the city of Debir (Kirjath-sepher). Othniel son of Kenaz succeeded and received Achsah as his wife. She then persuaded her father to give her springs of water in addition to the land in the Negev—a request Caleb granted by giving her both upper and lower springs (Joshua 15:16–19; Judges 1:9–15). Her initiative is cited as an example of resourceful advocacy.</p>",
        "hitchcock_meaning": "adorned; bursting the veil",
        "source_ids": {"easton": "achsah", "smith": "achsah", "isbe": "achsah"},
        "key_refs": ["Joshua 15:16", "Joshua 15:17", "Joshua 15:19", "Judges 1:12"],
        "sections": []
    },
    "achshaph": {
        "id": "achshaph",
        "term": "Achshaph",
        "category": "places",
        "intro": "<p>Achshaph (meaning <em>fascination</em> or <em>tricks</em>) was a royal Canaanite city in the northern reaches of Palestine whose king joined the coalition assembled by Jabin of Hazor against Joshua's army (Joshua 11:1). After the Israelite victory it was listed among the conquered Canaanite kingdoms (Joshua 12:20) and assigned as a boundary landmark of the tribe of Asher (Joshua 19:25). It is tentatively identified with the modern ruins of Yasif or Kesaf, northeast of Accho.</p>",
        "hitchcock_meaning": "poison; tricks",
        "source_ids": {"easton": "achshaph", "smith": "achshaph", "isbe": "achshaph"},
        "key_refs": ["Joshua 11:1", "Joshua 12:20", "Joshua 19:25"],
        "sections": []
    },
    "achzib": {
        "id": "achzib",
        "term": "Achzib",
        "category": "places",
        "intro": "<p>Achzib (meaning <em>falsehood</em> or <em>liar</em>, possibly in the sense of a brook that fails in summer) is the name of two Israelite towns. (1.) A town in the Shephelah lowlands of Judah, probably the same as Chezib where Judah's son Shelah was born (Genesis 38:5; Joshua 15:44). (2.) A Phoenician coastal city north of Accho, assigned to the tribe of Asher but never wrested from its Phoenician inhabitants (Joshua 19:29; Judges 1:31). The Greeks called this northern site Ecdippa. The prophet Micah uses the name Achzib in a wordplay to describe the towns of Judah as a <em>deception</em> to the kings of Israel (Micah 1:14).</p>",
        "hitchcock_meaning": "liar; lying; one that runs",
        "source_ids": {"easton": "achzib", "smith": "achzib", "isbe": "achzib"},
        "key_refs": ["Joshua 15:44", "Joshua 19:29", "Judges 1:31", "Micah 1:14"],
        "sections": []
    },
    "acre": {
        "id": "acre",
        "term": "Acre",
        "category": "concepts",
        "intro": "<p>Acre, in the biblical sense, is the translation of the Hebrew <em>tse'med</em> (literally a <em>yoke</em>), denoting the area of land that a yoke of oxen could plow in a single day—roughly equivalent to an English acre. The unit appears in two passages: Isaiah 5:10, where it forms part of a prophetic threat of agricultural failure, and 1 Samuel 14:14, which uses it to describe the space of ground across which Jonathan and his armor-bearer struck down the Philistines. The yoke-based measure was a practical field unit common in the ancient Near East.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "acre"},
        "key_refs": ["Isaiah 5:10", "1 Samuel 14:14"],
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
    print(f'BP a1: Aaron → Acre: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
