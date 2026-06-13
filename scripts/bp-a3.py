"""
BP Article Synthesis — a3: Ahlab → Anakim
Covers Easton entries: Ahlab through Anakim (75 entries)

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

Script: scripts/bp-a3.py
Run: python3 scripts/bp-a3.py
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
    "ahlab": {
        "id": "ahlab",
        "term": "Ahlab",
        "category": "places",
        "intro": "<p>Ahlab, whose name means <em>fatness</em> or <em>made of fat</em>, was a Canaanite town lying within the tribal territory of Asher in northern Canaan. It appears once in Scripture, in the catalogue of cities whose inhabitants Israel failed to drive out following the conquest (Judg. 1:31). The persistence of Canaanite enclaves in Asher's allotment was a recurring pattern in the north, and Ahlab stands as one example of the incomplete occupation that would generate ongoing tensions for Israel throughout the period of the judges.</p>",
        "hitchcock_meaning": "made of milk, or of fat; brother of the heart",
        "source_ids": {"easton": "ahlab", "smith": "ahlab", "isbe": "ahlab"},
        "key_refs": ["Judges 1:31"],
        "sections": []
    },
    "ahoah": {
        "id": "ahoah",
        "term": "Ahoah",
        "category": "people",
        "intro": "<p>Ahoah, meaning <em>a live brother</em> or <em>my thorn</em>, was one of the sons of Bela, the firstborn of Benjamin, appearing in the genealogical registers of 1 Chronicles (8:4; 7:7). His significance lies chiefly in having given his name to the Ahohite clan, a designation borne by several of David's most distinguished warriors, including Dodo the father of Eleazar (one of the three chief mighty men) and Zalmon (2 Sam. 23:9, 28). The clan's military prominence despite Benjamin's Saulide associations illustrates how individual families transcended tribal politics in service to David.</p>",
        "hitchcock_meaning": "a live brother; my thorn or thistle",
        "source_ids": {"easton": "ahoah", "smith": "ahoah", "isbe": "ahoah"},
        "key_refs": ["1 Chronicles 8:4", "1 Chronicles 7:7", "2 Samuel 23:9", "2 Samuel 23:28"],
        "sections": []
    },
    "ahohite": {
        "id": "ahohite",
        "term": "Ahohite",
        "category": "concepts",
        "intro": "<p>Ahohite is a gentile designation applied in the Old Testament to two of David's elite warriors: Dodo the father of Eleazar (one of the three chief mighty men) and Zalmon, one of the thirty (2 Sam. 23:9, 28; 1 Chr. 11:12, 29). The term denotes descent from Ahoah, son of Bela of the tribe of Benjamin. Its use in the military rosters of 2 Samuel 23 and 1 Chronicles 11 and 27 highlights the Benjaminite contribution to David's professional army, reflecting the integration of soldiers from Saul's tribe into the Davidic military establishment.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ahohite", "smith": "ahohite", "isbe": "ahohite"},
        "key_refs": ["1 Chronicles 27:4", "2 Samuel 23:9", "1 Chronicles 11:12", "2 Samuel 23:28", "1 Chronicles 11:29"],
        "sections": []
    },
    "aholah": {
        "id": "aholah",
        "term": "Aholah",
        "category": "concepts",
        "intro": "<p>Aholah, meaning <em>she has her own tent</em>, is the allegorical name given by the prophet Ezekiel to the northern kingdom of Israel (Samaria) in the extended parable of Ezekiel 23. In the allegory, Aholah and her sister Aholibah represent the two kingdoms as unfaithful wives of the Lord, having committed spiritual adultery through political and religious alliances with Egypt and Assyria. The name implies that Samaria erected its own unauthorized place of worship rather than worshipping at the divinely appointed sanctuary.</p><p>The parable draws on the history of the northern kingdom's persistent idolatry from Jeroboam's reign onward, culminating in the Assyrian exile. Though Aholah is a symbolic figure, Ezekiel's imagery allowed him to convey the gravity of covenant unfaithfulness in terms his audience would find inescapable.</p>",
        "hitchcock_meaning": "his tabernacle; his tent",
        "source_ids": {"easton": "aholah", "isbe": "aholah"},
        "key_refs": ["Psalms 78:67", "1 Kings 12:25", "2 Chronicles 11:13"],
        "sections": []
    },
    "aholiab": {
        "id": "aholiab",
        "term": "Aholiab",
        "category": "people",
        "intro": "<p>Aholiab, meaning <em>tent of the father</em>, was an artisan of the tribe of Dan chosen by God to assist Bezaleel in the construction of the tabernacle and its furnishings. He is described as specially endowed with wisdom, understanding, and knowledge in all manner of craftsmanship — cutting stones, carving wood, and working in textiles (Exod. 31:6; 35:34). His tribal origin in Dan is notable: while Bezaleel came from the royal tribe of Judah, the collaboration between Judah and Dan in the sanctuary's construction symbolized the shared responsibility of all Israel.</p><p>Aholiab was particularly skilled in embroidery and weaving, contributing to the priestly garments and the tabernacle curtains. His Spirit-given abilities represent one of the earliest explicit accounts of divine equipping for skilled labor in service of God's dwelling place.</p>",
        "hitchcock_meaning": "the tent of the father",
        "source_ids": {"easton": "aholiab", "smith": "aholiab", "isbe": "aholiab"},
        "key_refs": ["Exodus 31:6", "Exodus 35:34", "Exodus 36:1", "Exodus 36:2", "Exodus 38:23"],
        "sections": []
    },
    "aholibah": {
        "id": "aholibah",
        "term": "Aholibah",
        "category": "concepts",
        "intro": "<p>Aholibah, meaning <em>my tent is in her</em>, is the allegorical name applied by Ezekiel to the southern kingdom of Judah (Jerusalem) in the parable of Ezekiel 23. She is the sister of Aholah (Israel/Samaria) and is depicted as having surpassed her sister in unfaithfulness by pursuing alliances and idolatry with Assyria and then Babylon. The name implies that God's sanctuary resided in Jerusalem, making Judah's apostasy all the more inexcusable.</p><p>Ezekiel's parable culminates in a divine pronouncement of judgment echoing the fate of Aholah — exile at the hands of the very nations she had courted. The allegory functions as a theological explanation for the Babylonian destruction of Jerusalem, locating its cause in Judah's covenant breach rather than Babylon's military superiority.</p>",
        "hitchcock_meaning": "my tent, or my tabernacle, in her",
        "source_ids": {"easton": "aholibah", "isbe": "aholibah"},
        "key_refs": ["Ezekiel 23:4", "Ezekiel 23:11", "Ezekiel 23:22", "Ezekiel 23:36", "Ezekiel 23:44"],
        "sections": []
    },
    "aholibamah": {
        "id": "aholibamah",
        "term": "Aholibamah",
        "category": "people",
        "intro": "<p>Aholibamah, meaning <em>tent of the high place</em> or <em>my tabernacle is exalted</em>, is the name given to Judith, one of the wives of Esau and a daughter of Anah the Hivite. She is listed in Genesis 36 as the mother of three of Esau's sons — Jeush, Jaalam, and Korah — who became chiefs (dukes) of Edom. The same passage also lists an Aholibamah among the Edomite chiefs, likely a descendant bearing the same name who lent it to a clan or territory. Her Canaanite origin, noted at Genesis 26:34–35 under the name Judith, caused grief to Isaac and Rebekah.</p>",
        "hitchcock_meaning": "my tabernacle is exalted",
        "source_ids": {"easton": "aholibamah", "isbe": "aholibamah"},
        "key_refs": ["Genesis 26:34", "Genesis 36:2"],
        "sections": []
    },
    "ai": {
        "id": "ai",
        "term": "Ai",
        "category": "places",
        "intro": "<p>Ai (meaning <em>ruins</em>) was one of the royal Canaanite cities lying east of Bethel, near which Abraham pitched his tent and built an altar after entering Canaan (Gen. 12:8; 13:3). It is most prominent in the conquest narrative: Israel's first assault was routed — a defeat traced to Achan's hidden theft of devoted spoil from Jericho (Josh. 7). After Achan's judgment, Joshua returned with a larger force and destroyed Ai by means of an ambush, burning the city and making it a permanent ruin (Josh. 8).</p><p>The site is tentatively identified with et-Tell or a nearby location, though archaeological debate continues. A later resettlement appears as Aiath or Aija in Isaiah 10:28. The story of Ai stands as a central lesson in the conquest narrative: Israel's military success depended absolutely on covenant faithfulness before God.</p>",
        "hitchcock_meaning": "or Hai, mass; heap",
        "source_ids": {"easton": "ai", "smith": "ai", "isbe": "ai"},
        "key_refs": ["Joshua 10:1", "Genesis 12:8", "Genesis 13:3", "Joshua 7:2", "Joshua 8:1"],
        "sections": []
    },
    "aijeleth-shahar": {
        "id": "aijeleth-shahar",
        "term": "Aijeleth Shahar",
        "category": "concepts",
        "intro": "<p>Aijeleth Shahar, meaning <em>hind of the dawn</em>, appears as the title of Psalm 22 in the Hebrew superscription. It is understood as a musical direction, likely indicating either the name of a familiar melody to which the psalm was sung, or the designation of an instrument associated with its performance. Psalm 22, with its opening cry of desolation (<em>My God, my God, why have you forsaken me?</em>) and its movement toward praise, is among the most extensively cited psalms in the New Testament passion narratives, lending the title a resonance beyond its original technical musical function.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "aijeleth-shahar", "smith": "aijeleth-shahar"},
        "key_refs": ["Psalms 22"],
        "sections": []
    },
    "air": {
        "id": "air",
        "term": "Air",
        "category": "concepts",
        "intro": "<p>Air in biblical usage refers primarily to the atmosphere — the region between earth and the higher heavens. In the New Testament it carries additional theological significance: Paul describes believers being caught up to meet the Lord <em>in the air</em> at the resurrection (1 Thess. 4:17), while he also refers to Satan as <em>the prince of the power of the air</em> (Eph. 2:2), characterizing the spiritual realm associated with the fallen domain. Revelation associates the pouring of the seventh bowl upon the air (Rev. 16:17) with the final judgment.</p><p>In everyday usage the term describes breath and wind (Job 41:16) and can denote purposeless speech, as in Paul's warning against speaking into the air in an unintelligible tongue (1 Cor. 14:9).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "air", "isbe": "air"},
        "key_refs": ["1 Thessalonians 4:17", "Revelation 9:2", "Revelation 16:17", "Job 41:16", "1 Corinthians 14:9"],
        "sections": []
    },
    "ajalon": {
        "id": "ajalon",
        "term": "Ajalon",
        "category": "places",
        "intro": "<p>Ajalon (also spelled Aijalon, meaning <em>place of deer</em>) was a town and valley of strategic importance in the Shephelah. Originally assigned to Dan and later to Benjamin, it was among the Levitical cities given to the Kohathite priests (1 Chr. 6:69). The valley of Ajalon is most famous as the site of Joshua's command for the sun and moon to stand still while Israel pursued the five Amorite kings (Josh. 10:12), a miracle extending daylight long enough to complete the rout.</p><p>Rehoboam fortified the town (2 Chr. 11:10), and it later fell to Philistine attack during Ahaz's reign (2 Chr. 28:18). Its position commanding the gateway between the coastal plain and the Judean highlands made it a recurrently contested site throughout the monarchy period.</p>",
        "hitchcock_meaning": "a chain; strength; a stag",
        "source_ids": {"easton": "ajalon", "isbe": "ajalon"},
        "key_refs": ["Judges 1:35", "1 Chronicles 6:69", "2 Chronicles 28:18", "2 Chronicles 11:10", "1 Samuel 14:31"],
        "sections": []
    },
    "akkub": {
        "id": "akkub",
        "term": "Akkub",
        "category": "people",
        "intro": "<p>Akkub (a variant of Jacob, meaning <em>foot-print</em> or <em>supplanting</em>) is the name of several distinct individuals in the Old Testament. The most prominent is the head of a family of Levitical gatekeepers at the temple whose descendants returned from Babylonian exile with Zerubbabel (1 Chr. 9:17; Ezra 2:42; Neh. 7:45). A second Akkub was among the descendants of David's royal line in the post-exilic period (1 Chr. 3:24). A third was a leader of the Nethinim whose descendants also returned from Babylon (Ezra 2:45). The name's repeated occurrence among gatekeeping and temple-servant families reflects its use across multiple generations of those who maintained the sanctuary's service.</p>",
        "hitchcock_meaning": "foot-print; supplanting; crookedness; lewdness",
        "source_ids": {"easton": "akkub", "smith": "akkub", "isbe": "akkub"},
        "key_refs": ["Ezra 2:45", "1 Chronicles 9:17", "Ezra 2:42", "Nehemiah 7:45", "1 Chronicles 3:24"],
        "sections": []
    },
    "akrabbim": {
        "id": "akrabbim",
        "term": "Akrabbim",
        "category": "places",
        "intro": "<p>Akrabbim (meaning <em>scorpions</em>) was the name given to a mountain pass in the southern desert forming part of the boundary of Canaan and of the tribe of Judah. The Ascent of Akrabbim (also called Maaleh-acrabbim) is mentioned as the southern extremity of the promised land (Num. 34:4) and of Judah's allotment (Josh. 15:3). The name reflects the scorpions inhabiting the rocky Negev terrain. It is tentatively identified with the Naqb es-Safa pass in the wilderness south of the Dead Sea, which remains a natural boundary marker between the Arabah and the Sinai highlands.</p>",
        "hitchcock_meaning": "scorpions",
        "source_ids": {"easton": "akrabbim", "smith": "akrabbim", "isbe": "akrabbim"},
        "key_refs": ["Numbers 34:4", "Joshua 15:3"],
        "sections": []
    },
    "alabaster": {
        "id": "alabaster",
        "term": "Alabaster",
        "category": "concepts",
        "intro": "<p>Alabaster is a fine-grained, translucent stone used in the ancient Near East for perfume and ointment containers. In Scripture it appears in the New Testament accounts of a woman who broke an alabaster flask of precious nard and poured it on Jesus (Matt. 26:7; Mark 14:3; Luke 7:37). The stone's smooth, impermeable quality made it the preferred material for storing costly aromatic substances, preventing evaporation. Ancient vessels of this type were narrow-necked and sealed, typically broken at the neck to release their full contents at once.</p><p>The costliness of the ointment within the alabaster box was integral to the symbolic weight of the act. Jesus interpreted the anointing as a preparation for his burial and declared that the woman's act would be told as a memorial wherever the gospel is proclaimed (Matt. 26:13).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "alabaster", "smith": "alabaster", "isbe": "alabaster"},
        "key_refs": ["Matthew 26:7", "Mark 14:3", "Luke 7:37"],
        "sections": []
    },
    "alamoth": {
        "id": "alamoth",
        "term": "Alamoth",
        "category": "concepts",
        "intro": "<p>Alamoth (meaning <em>virgins</em> or <em>maidens</em>) is a Hebrew musical term occurring in the superscription of Psalm 46 and in 1 Chronicles 15:20, where it designates the type of voice or pitch for which a group of Levitical musicians performed. It is generally understood to indicate the soprano register — either that instruments were played at a high pitch or that the performance involved female or boy voices. The term stands in contrast to Sheminith (<em>the eighth</em>), which likely denotes a lower octave. Alamoth thus reflects the organized musical structure of tabernacle and temple worship established under David's appointments.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "alamoth", "smith": "alamoth", "isbe": "alamoth"},
        "key_refs": ["1 Chronicles 15:20", "Psalms 46"],
        "sections": []
    },
    "alarm": {
        "id": "alarm",
        "term": "Alarm",
        "category": "concepts",
        "intro": "<p>Alarm in the biblical context refers to a specific staccato sound produced by the silver trumpets to signal particular actions for the congregation of Israel. Numbers 10:5–6 distinguishes between a sustained blast summoning the assembly and the alarm (<em>teruah</em>), which signaled the tribes to break camp and march in prescribed order. The prophets later employed the war-alarm to announce divine judgment: Jeremiah uses it of the approaching Babylonian army (Jer. 4:19; 49:2), and Zephaniah applies it to the day of the Lord as a day of <em>trumpet blast and battle cry</em> (Zeph. 1:16).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "alarm", "isbe": "alarm"},
        "key_refs": ["Numbers 10:5", "Numbers 10:6", "Jeremiah 4:19", "Jeremiah 49:2", "Zephaniah 1:16"],
        "sections": []
    },
    "alemeth": {
        "id": "alemeth",
        "term": "Alemeth",
        "category": "people",
        "intro": "<p>Alemeth (meaning <em>hiding</em> or <em>covering</em>) is the name of two individuals and one town in the Old Testament. As a personal name it belongs to (1) one of the nine sons of Becher, son of Benjamin (1 Chr. 7:8), and (2) a son of Jehoadah (or Jarah) in the genealogy of Saul's Benjaminite line (1 Chr. 8:36; 9:42). The same name designates a Levitical city in Benjamin, also called Almon (Josh. 21:18), assigned to priests of Aaron's line. The overlapping personal and place names suggest a possible ancestral connection between the Benjaminite clan and the priestly city.</p>",
        "hitchcock_meaning": "hiding; youth; worlds; upon the dead",
        "source_ids": {"easton": "alemeth", "smith": "alemeth", "isbe": "alemeth"},
        "key_refs": ["1 Chronicles 7:8", "1 Chronicles 8:36", "1 Chronicles 6:60", "Joshua 21:18"],
        "sections": []
    },
    "alexander": {
        "id": "alexander",
        "term": "Alexander",
        "category": "people",
        "intro": "<p>Alexander (meaning <em>one who assists men</em>) is the name of several distinct individuals in the New Testament. (1) A relative of Annas the high priest present at the interrogation of Peter and John (Acts 4:6). (2) Simon of Cyrene's son, referenced in Mark 15:21 as apparently known to Mark's Roman audience. (3) A Jew put forward during the Ephesian riot to dissociate the Jewish community from Paul (Acts 19:33). (4) A man who made shipwreck of his faith alongside Hymenaeus (1 Tim. 1:19–20). (5) Alexander the coppersmith who did Paul much harm (2 Tim. 4:14).</p><p>Whether figures (4) and (5) are the same person is debated. The name's frequency in the Greco-Roman world makes identification across texts uncertain.</p>",
        "hitchcock_meaning": "one who assists men",
        "source_ids": {"easton": "alexander", "smith": "alexander", "isbe": "alexander"},
        "key_refs": ["Acts 4:6", "Mark 15:21", "Acts 19:33", "1 Timothy 1:19", "2 Timothy 4:14"],
        "sections": []
    },
    "alexander-the-great": {
        "id": "alexander-the-great",
        "term": "Alexander the Great",
        "category": "people",
        "intro": "<p>Alexander the Great (356–323 BC), king of Macedonia and conqueror of the Persian Empire, transformed the ancient Near East in ways that shaped the background of the later Old Testament period and the entire New Testament world. Though not named in the canonical text, he is widely understood to be the figure represented in Daniel's visions — the <em>notable horn</em> of the he-goat (Dan. 8) whose swift conquests from west to east mirror his campaigns against Persia, and whose sudden death and division of his kingdom among four successors corresponds to the Diadochi kingdoms.</p><p>Alexander's spread of Greek language and culture (Hellenization) created the linguistic environment in which the Septuagint was translated and the New Testament was written. His founding of Alexandria in Egypt established the city that became a major center of Jewish diaspora life and early Christian scholarship.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "alexander-the-great", "isbe": "alexander-the-great"},
        "key_refs": ["Daniel 2:32"],
        "sections": []
    },
    "alexandria": {
        "id": "alexandria",
        "term": "Alexandria",
        "category": "places",
        "intro": "<p>Alexandria, founded by Alexander the Great on the Mediterranean coast of Egypt in 332 BC, became one of the most important cities of the ancient world and a principal center of Jewish diaspora life. The city's large Jewish population produced the Septuagint, the Greek translation of the Hebrew scriptures, beginning in the third century BC. In the New Testament, Alexandria appears most prominently in the person of Apollos, described as <em>an Alexandrian by birth, mighty in the scriptures</em> (Acts 18:24), who became a significant early Christian teacher.</p><p>The Alexandrian synagogue in Jerusalem was among those opposing Stephen (Acts 6:9). Ships from Alexandria are mentioned in Paul's voyage to Rome (Acts 27:6; 28:11). The city later became a formative center of early Christian theology, associated with figures such as Clement and Origen.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "alexandria", "isbe": "alexandria"},
        "key_refs": ["Acts 18:24", "Acts 6:9"],
        "sections": []
    },
    "algum": {
        "id": "algum",
        "term": "Algum",
        "category": "concepts",
        "intro": "<p>Algum is a variety of precious wood mentioned in connection with the construction of Solomon's temple (2 Chr. 2:8; 9:10–11), appearing also as <em>almug</em> in 1 Kings 10:11–12. The wood was imported from Lebanon and Ophir and used by Solomon for pillars in the temple and palace, as well as for harps and psalteries for the musicians. Its precise botanical identity remains uncertain; proposed identifications include red sandalwood, juniper, and other aromatic hardwoods. The Chronicler notes that never before had such quantities of this wood been seen in Jerusalem, underscoring its exotic and costly character.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "algum"},
        "key_refs": ["2 Chronicles 2:8", "2 Chronicles 9:10", "2 Chronicles 9:11", "1 Kings 10:11"],
        "sections": []
    },
    "alien": {
        "id": "alien",
        "term": "Alien",
        "category": "concepts",
        "intro": "<p>An alien in biblical usage is a person residing in a land not their own — a foreigner living among the covenant people of Israel. The Hebrew terms <em>ger</em> (sojourner) and <em>nokri</em> (foreigner) cover related but distinct categories, with the sojourner enjoying greater legal protections as an integrated resident. The Mosaic law made extensive provision for aliens: they were not to be oppressed (Lev. 19:33), were entitled to gleanings from harvests, and were to be treated with the love reserved for native Israelites, with the reminder that Israel had itself been alien in Egypt (Deut. 10:19).</p><p>At the same time, the law maintained distinctions between resident aliens and native Israelites in certain ritual and civic obligations. The New Testament extends the language of alien to describe believers who, as citizens of heaven, are <em>strangers and pilgrims</em> in the present world (1 Pet. 2:11; Heb. 11:13).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "alien", "isbe": "alien"},
        "key_refs": ["Leviticus 22:10", "Psalms 39:12", "Leviticus 19:33", "Leviticus 19:34", "Deuteronomy 10:19"],
        "sections": []
    },
    "allegory": {
        "id": "allegory",
        "term": "Allegory",
        "category": "concepts",
        "intro": "<p>Allegory as a literary and interpretive device appears in the Bible both as a compositional form and as an explicit method of reading existing texts. The word itself occurs in the New Testament only once — in Galatians 4:24, where Paul states that the account of Abraham's two sons (by Hagar and Sarah) <em>is an allegory</em>. He reads the historical narrative as representing two covenants: Hagar corresponding to Mount Sinai and bondage, and Sarah to the promise and freedom. This interpretive approach reflects a practice familiar in both Jewish and Hellenistic contexts.</p><p>In the Old Testament, allegory functions as a compositional device in Ezekiel's parables (the vine, the eagles, the harlot sisters), in wisdom literature (Ecclesiastes 12:2–6), and in Nathan's parable to David (2 Sam. 12:1). The term must be distinguished from typology: typology preserves the historical meaning of events while seeing them as prefiguring later realities; allegory in the strict sense replaces the literal meaning with a figurative one.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "allegory", "smith": "allegory", "isbe": "allegory"},
        "key_refs": ["Galatians 4:24", "2 Samuel 12:1", "Ecclesiastes 12:2"],
        "sections": []
    },
    "alleluia": {
        "id": "alleluia",
        "term": "Alleluia",
        "category": "concepts",
        "intro": "<p>Alleluia (or Hallelujah) is the Greek transliteration of the Hebrew liturgical exclamation <em>Hallelu-Jah</em>, meaning <em>praise ye the Lord</em>. The Hebrew form occurs throughout the Psalter, particularly in the Hallel psalms (Pss. 111–118; 146–150), as an expression of congregational praise. The Greek form Alleluia appears four times in the New Testament, all in Revelation 19:1–6, where it frames the heavenly choir's celebration of God's righteous judgment on Babylon and the proclamation of the marriage supper of the Lamb.</p><p>Its survival as an untranslated word in Christian liturgical tradition across centuries reflects its status as a living link between Hebrew temple worship and the church's inheritance of the Psalter. It remains one of the most widely recognizable liturgical acclamations in world Christianity.</p>",
        "hitchcock_meaning": "praise the Lord",
        "source_ids": {"easton": "alleluia", "smith": "alleluia", "isbe": "alleluia"},
        "key_refs": ["Revelation 19:1", "Revelation 19:3", "Revelation 19:4", "Revelation 19:6"],
        "sections": []
    },
    "alliance": {
        "id": "alliance",
        "term": "Alliance",
        "category": "concepts",
        "intro": "<p>Alliance in the biblical world referred to formal treaties or covenants between nations, city-states, or individuals, typically ratified by oath and sometimes by sacrifice. The Old Testament records numerous examples: Abraham's covenant with Mamre, Eshcol, and Aner (Gen. 14:13); Israel's inadvertent treaty with the Gibeonites (Josh. 9); and David's standing relationship with Hiram of Tyre. The Mosaic law warned against covenants with the Canaanite nations (Exod. 23:32; Deut. 7:2), foreseeing that such alliances would lead to religious compromise.</p><p>The prophets consistently condemned Israel and Judah for seeking military security through alliances with Egypt or Assyria rather than trusting God — a central theme in Isaiah, Jeremiah, and Ezekiel. The underlying concern was that reliance on foreign powers represented a practical denial of God's sufficiency as Israel's protector. Paul draws on the concept in 2 Corinthians 6:14's warning against being unequally yoked with unbelievers.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "alliance", "isbe": "alliance"},
        "key_refs": ["Genesis 14:13", "Joshua 9:3", "Leviticus 18:3"],
        "sections": []
    },
    "allon": {
        "id": "allon",
        "term": "Allon",
        "category": "people",
        "intro": "<p>Allon (meaning <em>an oak</em> or <em>strong</em>) appears in the Old Testament with uncertain classification. In Joshua 19:33, the Hebrew word may represent either a proper place name (a landmark oak tree on Naphtali's border) or the common noun for oak, as the Revised Version renders it. As a personal name, Allon appears in 1 Chronicles 4:37 as the father of Shiphi, a leader in Simeon during the time of Hezekiah. The convergence of tree name and personal name was common in the ancient world, where natural landmarks frequently generated family and clan designations.</p>",
        "hitchcock_meaning": "an oak; strong",
        "source_ids": {"easton": "allon", "smith": "allon", "isbe": "allon"},
        "key_refs": ["Joshua 19:33", "1 Chronicles 4:37"],
        "sections": []
    },
    "allon-bachuth": {
        "id": "allon-bachuth",
        "term": "Allon-bachuth",
        "category": "places",
        "intro": "<p>Allon-bachuth, meaning <em>oak of weeping</em>, was a tree near Bethel beneath which Deborah, the nurse of Rebekah, was buried (Gen. 35:8). The memorial name given to the site reflects the ancient Near Eastern practice of commemorating significant deaths at notable natural landmarks. This Deborah is distinct from Deborah the prophetess-judge of Judges 4–5. Her burial on Jacob's journey back to Bethel marked a moment of personal grief embedded within the larger narrative of God's covenant renewal with the patriarch at that sacred site.</p>",
        "hitchcock_meaning": "the oak of weeping",
        "source_ids": {"easton": "allon-bachuth"},
        "key_refs": ["Genesis 35:8", "Judges 4:5"],
        "sections": []
    },
    "almodad": {
        "id": "almodad",
        "term": "Almodad",
        "category": "people",
        "intro": "<p>Almodad (meaning <em>measure of God</em> or <em>immeasurable</em>) was the first named of the sons of Joktan in the Table of Nations (Gen. 10:26), descended from Shem through Eber. Joktan's thirteen sons are understood as ancestors of various Arabian tribes, making Almodad a progenitor of a Semitic people in the southern Arabian Peninsula. He is not mentioned elsewhere in Scripture. His name may be preserved in ancient Yemeni tribal or geographic designations, though precise identification remains uncertain.</p>",
        "hitchcock_meaning": "measure of God",
        "source_ids": {"easton": "almodad", "smith": "almodad", "isbe": "almodad"},
        "key_refs": ["Genesis 10:26"],
        "sections": []
    },
    "almon": {
        "id": "almon",
        "term": "Almon",
        "category": "places",
        "intro": "<p>Almon (meaning <em>hidden</em>) was one of the sacerdotal cities in the territory of Benjamin assigned to the descendants of Aaron (Josh. 21:18). It appears in 1 Chronicles 6:60 as Alemeth, confirming that both names refer to the same city. The site has been tentatively identified with Khirbet Almit, approximately one mile northeast of Anathoth near Jerusalem. As one of the Levitical cities, Almon provided residence and support for the priestly families dispersed across the tribal lands.</p>",
        "hitchcock_meaning": "hidden",
        "source_ids": {"easton": "almon", "smith": "almon", "isbe": "almon"},
        "key_refs": ["Joshua 21:18", "1 Chronicles 6:60"],
        "sections": []
    },
    "almond": {
        "id": "almond",
        "term": "Almond",
        "category": "concepts",
        "intro": "<p>The almond tree (<em>Prunus dulcis</em>) is native to Syria and Palestine and is among the first trees to blossom in the year, flowering in January before its leaves appear. In Hebrew the almond is called <em>shaqed</em>, meaning <em>the wakeful one</em> — a name reflecting its early awakening from winter dormancy. This wordplay is exploited by Jeremiah, where God shows him an almond branch (<em>shaqed</em>) and declares, <em>I am watching (shoqed) over my word to perform it</em> (Jer. 1:11–12).</p><p>The almond held important symbolic significance in Israelite worship: the cups of the golden lampstand in the tabernacle were shaped like almond blossoms (Exod. 25:33). Aaron's rod that budded, blossomed, and bore almonds overnight as a sign of divinely chosen priesthood is among the most celebrated miracles of the wilderness period (Num. 17:8). In Ecclesiastes 12:5 the almond tree's white blossoms serve as a poetic image for the white hair of old age.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "almond", "isbe": "almond"},
        "key_refs": ["Ecclesiastes 12:5", "Jeremiah 1:11", "Genesis 43:11", "Numbers 17:8", "Hebrews 9:4"],
        "sections": []
    },
    "alms": {
        "id": "alms",
        "term": "Alms",
        "category": "concepts",
        "intro": "<p>Alms refers to charitable giving to the poor, a practice rooted in the covenant obligations of the Mosaic law even though the specific word does not appear in most Old Testament translations. The law commanded gleaning rights for the poor (Lev. 19:9–10), provision in the seventh year for the needy (Deut. 15:7–11), and open-handed generosity: <em>you shall open wide your hand to your brother</em> (Deut. 15:11). The Psalms and Proverbs associate generosity with righteousness (Ps. 41:1; 112:9; Prov. 14:31), and the prophets condemned Israel for neglecting this duty.</p><p>In the New Testament, almsgiving is assumed as a regular practice of Jewish piety. Jesus addresses it in the Sermon on the Mount, warning against performing it for public recognition (Matt. 6:1–4). Cornelius's alms are noted as having come before God as a memorial offering (Acts 10:4), and Paul's collection for the Jerusalem church was understood as a corporate act of generosity with theological weight as an expression of Gentile solidarity with Jewish believers.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "alms", "smith": "alms"},
        "key_refs": ["Leviticus 25:35", "Deuteronomy 15:7", "Psalms 41:1", "Psalms 112:9", "Proverbs 14:31"],
        "sections": []
    },
    "almug": {
        "id": "almug",
        "term": "Almug",
        "category": "concepts",
        "intro": "<p>Almug (also appearing as <em>algum</em> in Chronicles) was a precious wood brought from Ophir by the fleet of Hiram of Tyre for Solomon's building projects (1 Kgs. 10:11–12). Solomon used it for pillars in the temple and palace, and to make harps and lyres for the Levitical musicians. The text notes the quantities were so remarkable that nothing like them had ever been seen in Jerusalem before. Botanical identifications proposed by scholars include red sandalwood, juniper, and other aromatic hardwoods; the precise species remains undetermined. The same wood imported from Lebanon is called algum in 2 Chronicles 2:8.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "almug"},
        "key_refs": ["1 Kings 10:11", "1 Kings 10:12", "2 Chronicles 2:8", "2 Chronicles 9:10", "2 Chronicles 9:11"],
        "sections": []
    },
    "aloes": {
        "id": "aloes",
        "term": "Aloes",
        "category": "concepts",
        "intro": "<p>Aloes in the Old Testament refers not to the succulent plant known today by that name, but to a fragrant heartwood derived from the <em>Aquilaria</em> tree (eagle wood or lign aloes), native to India and Southeast Asia. This aromatic wood was highly prized in the ancient Near East as a perfume. It appears in Numbers 24:6 as a simile for Israel's encampments; in Psalm 45:8 and Proverbs 7:17 as a scent applied to garments; and in Song of Solomon 4:14 among the spices of the beloved's garden.</p><p>In the New Testament, Nicodemus brought a mixture of myrrh and aloes — about a hundred pounds — to prepare Jesus's body for burial (John 19:39), reflecting both the costliness of the preparation and the depth of Nicodemus's devotion, demonstrated openly at the moment of greatest apparent defeat.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "aloes"},
        "key_refs": ["Numbers 24:6", "Psalms 45:8", "Proverbs 7:17", "Song of Solomon 4:14", "John 19:39"],
        "sections": []
    },
    "alphaeus": {
        "id": "alphaeus",
        "term": "Alphaeus",
        "category": "people",
        "intro": "<p>Alphaeus is the name of two individuals in the New Testament. (1) The father of James the Less, one of the twelve apostles, consistently distinguished in apostolic lists as <em>James the son of Alphaeus</em> (Matt. 10:3; Mark 3:18; Luke 6:15; Acts 1:13). Some scholars propose identifying this Alphaeus with the Clopas (or Cleophas) of John 19:25, suggesting that Mary the mother of James was the wife of Clopas. (2) The father of Levi (Matthew), the tax collector called by Jesus (Mark 2:14).</p><p>Whether these two fathers named Alphaeus are the same person — which would make James and Matthew brothers — is a question debated since antiquity. The name's ordinary occurrence in the Greco-Roman world makes identification uncertain.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "alphaeus", "smith": "alphaeus", "isbe": "alphaeus"},
        "key_refs": ["Matthew 10:3", "Mark 3:18", "Luke 6:15", "Acts 1:13", "John 19:25"],
        "sections": []
    },
    "altar": {
        "id": "altar",
        "term": "Altar",
        "category": "concepts",
        "intro": "<p>The altar (Hebrew <em>mizbeah</em>, from a root meaning <em>to slaughter</em>) was the central structure of Israelite worship — a raised platform or table on which sacrifices and offerings were presented to God. Altars appear from the earliest pages of Scripture, built by Noah after the flood, Abraham at Shechem and Bethel, and the patriarchs at moments of divine encounter. The Mosaic law specified two principal altars for the tabernacle: the altar of burnt offering in the outer court, made of acacia wood overlaid with bronze (Exod. 27:1–8), and the altar of incense within the Holy Place, made of acacia wood overlaid with gold (Exod. 30:1–10). Only priests of Aaron's line were authorized to officiate at these altars.</p><p>The altar of burnt offering was the place where sin offerings, burnt offerings, peace offerings, and thank offerings were presented, providing the mechanism of atonement and communion at the center of Israel's covenant worship. The New Testament interprets Christ's sacrifice as the definitive fulfillment of the altar's function (Heb. 9–10), and Hebrews 13:10 declares that Christians have an altar from which those who serve the tabernacle have no right to eat.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "altar", "smith": "altar", "isbe": "altar"},
        "key_refs": ["Exodus 20:24", "Genesis 22:9", "Ezekiel 6:3", "2 Kings 23:12", "2 Kings 16:4"],
        "sections": []
    },
    "altaschith": {
        "id": "altaschith",
        "term": "Altaschith",
        "category": "concepts",
        "intro": "<p>Altaschith (meaning <em>destroy not</em>) is a Hebrew phrase appearing in the superscriptions of Psalms 57, 58, 59, and 75. It is generally understood as a musical direction, possibly the opening words of a familiar song or melody to which these psalms were to be performed, analogous to other tune references in the Psalter. The phrase corresponds to the words of Moses (<em>Destroy them not</em>, Deut. 9:26) and to David's restraint toward Saul (1 Sam. 26:9), suggesting it may have evoked a mood of appeal for divine mercy or restraint of judgment in liturgical performance.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "altaschith", "smith": "altaschith"},
        "key_refs": ["Psalms 57:1", "Psalms 58:1", "Psalms 59:1"],
        "sections": []
    },
    "alush": {
        "id": "alush",
        "term": "Alush",
        "category": "places",
        "intro": "<p>Alush (meaning <em>mingling together</em>) was one of the stations of Israel's wilderness journey, listed in Numbers 33:13–14 as the encampment between Dophkah and Rephidim on the route from Egypt to Sinai. The site has not been identified with certainty, though it lay somewhere in the Sinai Peninsula in the region traversed between the Wilderness of Sin and the camp at Rephidim, where water was later provided from the rock at Horeb.</p>",
        "hitchcock_meaning": "mingling together",
        "source_ids": {"easton": "alush", "smith": "alush", "isbe": "alush"},
        "key_refs": ["Numbers 33:13", "Numbers 33:14"],
        "sections": []
    },
    "amalek": {
        "id": "amalek",
        "term": "Amalek",
        "category": "people",
        "intro": "<p>Amalek (meaning <em>a people that licks up</em> or <em>dweller in a valley</em>) was the son of Eliphaz, the firstborn of Esau, by his concubine Timna (Gen. 36:12; 1 Chr. 1:36). He is listed among the chiefs of Edom (Gen. 36:16) and is the eponymous ancestor of the Amalekites, the nomadic people who inhabited the region of Sinai, the Negev, and the northern Arabian Peninsula. A reference to <em>the country of the Amalekites</em> in Genesis 14:7, before Amalek's birth in the narrative, has led some to distinguish between Amalek the individual and an earlier, similarly named people group, though others regard the Genesis 14 reference as anachronistic in name only.</p>",
        "hitchcock_meaning": "a people that licks up",
        "source_ids": {"easton": "amalek", "smith": "amalek", "isbe": "amalek"},
        "key_refs": ["Genesis 36:12", "1 Chronicles 1:36", "Genesis 36:16"],
        "sections": []
    },
    "amalekite": {
        "id": "amalekite",
        "term": "Amalekite",
        "category": "concepts",
        "intro": "<p>The Amalekites were an ancient nomadic people inhabiting Arabia Petraea — the Sinai Peninsula, the Negev, and the region between Havilah and Shur. They were among the first peoples to oppose Israel after the exodus, attacking Israel's rear guard at Rephidim (Exod. 17:8–16), an act that resulted in a divine decree of perpetual war between the Lord and Amalek. Balaam's oracle described them as <em>the first of the nations</em> (Num. 24:20).</p><p>Their encounters with Israel continued through the period of the judges via raids with Moab and Midian. King Saul was commanded to utterly destroy them but spared King Agag, a disobedience that cost Saul his dynasty (1 Sam. 15). David later defeated a raiding party that had sacked Ziklag (1 Sam. 30). The last recorded Amalekites are those killed by Simeonites in the time of Hezekiah (1 Chr. 4:43).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "amalekite"},
        "key_refs": ["Genesis 14:7", "Numbers 13:29", "1 Samuel 15:7", "Numbers 24:7", "1 Samuel 15:8"],
        "sections": []
    },
    "amana": {
        "id": "amana",
        "term": "Amana",
        "category": "places",
        "intro": "<p>Amana (meaning <em>perennial</em> or <em>integrity</em>) appears in two distinct biblical contexts. (1) The Hebrew margin of 2 Kings 5:12 suggests that the Abana River — one of the rivers of Damascus praised by Naaman the Syrian — may alternatively be read as Amana. (2) In Song of Solomon 4:8 the beloved is invited to come from Amana alongside Hermon and other northern peaks, suggesting a mountain in the Anti-Lebanon range near Damascus, possibly the source of the Abana River. The name thus identifies a geographic feature in the Syrian highlands north of Israel.</p>",
        "hitchcock_meaning": "integrity; truth; a nurse",
        "source_ids": {"easton": "amana", "smith": "amana", "isbe": "amana"},
        "key_refs": ["2 Kings 5:12", "Song of Solomon 4:8"],
        "sections": []
    },
    "amariah": {
        "id": "amariah",
        "term": "Amariah",
        "category": "people",
        "intro": "<p>Amariah (meaning <em>the Lord says</em> or <em>the integrity of the Lord</em>) is a name borne by at least nine distinct individuals in the Old Testament, reflecting its popularity among priestly and Levitical families. Prominent figures include: (1) Amariah son of Meraioth, a high priest in the line of Eleazar (1 Chr. 6:7, 52); (2) Amariah son of Azariah, who served as chief priest over religious matters under Jehoshaphat (2 Chr. 19:11); (3) a Levite son of Hebron in David's organization (1 Chr. 23:19; 24:23); (4) a distributor of priestly portions under Hezekiah (2 Chr. 31:15); (5) a priest who returned with Zerubbabel (Neh. 12:2). The name's concentration among priestly families underscores its association with the temple service across multiple generations.</p>",
        "hitchcock_meaning": "the Lord says; the integrity of the Lord",
        "source_ids": {"easton": "amariah", "smith": "amariah", "isbe": "amariah"},
        "key_refs": ["1 Chronicles 6:7", "1 Chronicles 6:52", "1 Chronicles 23:19", "1 Chronicles 24:23", "2 Chronicles 19:11"],
        "sections": []
    },
    "amasa": {
        "id": "amasa",
        "term": "Amasa",
        "category": "people",
        "intro": "<p>Amasa (meaning <em>burden</em> or <em>sparing the people</em>) is the name of two individuals in the Old Testament. (1) The son of Abigail, a sister of King David, making him David's nephew and a cousin of Joab. During Absalom's rebellion he served as commander of the rebel army (2 Sam. 17:25). After Absalom's defeat, David appointed Amasa to replace Joab as army commander (2 Sam. 19:13). Joab, refusing to accept this displacement, murdered him treacherously at Gibeon while appearing to embrace him (2 Sam. 20:8–10) — a killing for which Solomon later held Joab accountable. (2) A son of Hadlai who opposed the enslavement of Judean captives brought to Samaria by Israel during Ahaz's reign (2 Chr. 28:12).</p>",
        "hitchcock_meaning": "sparing the people",
        "source_ids": {"easton": "amasa", "smith": "amasa", "isbe": "amasa"},
        "key_refs": ["1 Chronicles 2:17", "2 Samuel 17:25", "2 Samuel 19:13", "2 Samuel 20:4", "2 Chronicles 28:12"],
        "sections": []
    },
    "amasai": {
        "id": "amasai",
        "term": "Amasai",
        "category": "people",
        "intro": "<p>Amasai (meaning <em>burdensome</em> or <em>strong</em>) is the name of three individuals in the Old Testament. (1) A Levite, son of Elkanah, ancestor of the singer Heman (1 Chr. 6:25, 35). (2) The most memorable Amasai was chief of thirty warriors who came to David at Ziklag; the Spirit of God came upon him and he declared, <em>We are yours, O David, and on your side, O son of Jesse</em> (1 Chr. 12:18) — one of the most explicit descriptions of Spirit-inspired loyalty in the historical books. (3) A priest who blew a trumpet before the ark when David brought it to Jerusalem (1 Chr. 15:24). A fourth Amasai, a Levite, participated in Hezekiah's temple cleansing (2 Chr. 29:12).</p>",
        "hitchcock_meaning": "strong",
        "source_ids": {"easton": "amasai", "isbe": "amasai"},
        "key_refs": ["1 Chronicles 6:25", "1 Chronicles 6:35", "1 Chronicles 12:18", "1 Chronicles 15:24", "2 Chronicles 29:12"],
        "sections": []
    },
    "amashai": {
        "id": "amashai",
        "term": "Amashai",
        "category": "people",
        "intro": "<p>Amashai (meaning <em>the people's gift</em>) was the son of Azareel, a priest designated by Nehemiah to reside in Jerusalem during the resettlement of the city following the return from exile (Neh. 11:13). He is listed among the priestly families who volunteered or were appointed to inhabit the holy city, helping to populate and maintain Jerusalem's religious infrastructure in the mid-fifth century BC.</p>",
        "hitchcock_meaning": "the people's gift",
        "source_ids": {"easton": "amashai"},
        "key_refs": ["Nehemiah 11:13"],
        "sections": []
    },
    "amasiah": {
        "id": "amasiah",
        "term": "Amasiah",
        "category": "people",
        "intro": "<p>Amasiah (meaning <em>burden of Jehovah</em> or <em>sustained by Jehovah</em>) was a military officer under King Jehoshaphat of Judah, described as <em>the son of Zichri, who willingly offered himself unto the LORD</em> (2 Chr. 17:16). This description may indicate a special voluntary consecration to military service in honor of God. He commanded a force of two hundred thousand men as part of the large army Jehoshaphat organized for Judah's defense, reflecting the spirit of holy-war tradition in which warriors consecrated themselves to the Lord's service (Judg. 5:9).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "amasiah", "smith": "amasiah", "isbe": "amasiah"},
        "key_refs": ["2 Chronicles 17:16", "Judges 5:9"],
        "sections": []
    },
    "amaziah": {
        "id": "amaziah",
        "term": "Amaziah",
        "category": "people",
        "intro": "<p>Amaziah (meaning <em>the strength of the Lord</em>) is most prominently the ninth king of Judah (c. 796–767 BC), son of Joash. After consolidating his rule, he executed his father's assassins but spared their children in accordance with the Mosaic law (2 Kgs. 14:5–6). He won a significant victory over Edom in the Valley of Salt, taking the city of Selah (2 Chr. 25:11–12). However, he then worshipped Edomite gods and rejected prophetic rebuke, leading to divine judgment.</p><p>Emboldened by his Edomite success, Amaziah challenged Jehoash of Israel and was decisively defeated at Beth-shemesh; Jerusalem's wall was breached and the temple treasury plundered (2 Kgs. 14:11–14). He was eventually killed in a conspiracy at Lachish. The Chronicler attributes his decline directly to his embrace of Edomite idols. Three other bearers of this name include a Levite ancestor of the singer Ethan, the priest of Bethel who opposed Amos, and a Simeonite leader.</p>",
        "hitchcock_meaning": "the strength of the Lord",
        "source_ids": {"easton": "amaziah", "smith": "amaziah", "isbe": "amaziah"},
        "key_refs": ["1 Chronicles 6:45", "2 Kings 14:1", "2 Chronicles 25:3", "2 Chronicles 25:5", "2 Chronicles 25:6"],
        "sections": []
    },
    "ambassador": {
        "id": "ambassador",
        "term": "Ambassador",
        "category": "concepts",
        "intro": "<p>The ambassador in the ancient Near East was a diplomatic envoy sent by a ruler to convey messages, negotiate terms, or represent sovereign interests in a foreign court. The Old Testament employs several Hebrew terms for such envoys (<em>tsir</em>, <em>malak</em>), seen in Joshua 9:4 (the Gibeonites' deceptive embassy), Isaiah 18:2 (Egyptian ambassadors), Jeremiah 49:14 and Obadiah 1:1 (envoys called among nations). The sending of ambassadors accompanied treaties, tribute negotiations, and declarations of war throughout the ancient world.</p><p>In the New Testament, Paul applies the title to his own apostolic calling: <em>we are ambassadors for Christ, God making his appeal through us</em> (2 Cor. 5:20), and again in Ephesians 6:20 he calls himself <em>an ambassador in chains</em>. The metaphor frames the apostolic ministry as representing the heavenly sovereign in the world, bearing a message of reconciliation with the full authority of the one who sent the envoy.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ambassador", "smith": "ambassador", "isbe": "ambassador"},
        "key_refs": ["Joshua 9:4", "Proverbs 13:17", "Isaiah 18:2", "Jeremiah 49:14", "Obadiah 1:1"],
        "sections": []
    },
    "amber": {
        "id": "amber",
        "term": "Amber",
        "category": "concepts",
        "intro": "<p>Amber appears in English translations of Ezekiel 1:4, 27 and 8:2 (Authorized Version) as the rendering of the Hebrew <em>hashmal</em>, a rare term of uncertain meaning. The Septuagint translates it as <em>elektron</em>, which in Greek referred to a bright alloy of gold and silver (electrum) rather than fossilized resin. Ezekiel uses the term to describe a brilliant, glowing substance associated with the divine appearances in his visions — the color of the central fire in his inaugural vision (Ezek. 1:4) and of the figure on the sapphire throne (Ezek. 1:27; 8:2). Modern scholars generally favor electrum or polished metal over amber as a translation, since the latter does not convey the incandescent quality Ezekiel describes.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "amber", "smith": "amber", "isbe": "amber"},
        "key_refs": ["Ezekiel 1:4", "Ezekiel 1:27", "Ezekiel 8:2"],
        "sections": []
    },
    "ambush": {
        "id": "ambush",
        "term": "Ambush",
        "category": "concepts",
        "intro": "<p>Ambush as a military tactic — the concealment of troops to surprise an enemy — appears several times in the Old Testament as a legitimate and divinely directed strategy of warfare. The most detailed example is Joshua's capture of Ai (Josh. 8), where God instructed Joshua to place thirty thousand soldiers in ambush behind the city while a smaller force feigned retreat, drawing out the defenders before the concealed troops seized and burned the undefended city. Judges records Abimelech's use of ambush against Shechem (Judg. 9:30–45), and Jeremiah employs the imagery of ambush in his oracle against Babylon (Jer. 51:12).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ambush", "isbe": "ambush"},
        "key_refs": ["Joshua 8:4", "Judges 9:30", "Jeremiah 51:12"],
        "sections": []
    },
    "amen": {
        "id": "amen",
        "term": "Amen",
        "category": "concepts",
        "intro": "<p>Amen is a Hebrew word meaning <em>firm</em>, <em>certain</em>, or <em>faithful</em>, derived from the root <em>'aman</em> (to confirm or support). In liturgical use it functions as a solemn affirmation of a prayer, doxology, or blessing — equivalent to <em>so be it</em> or <em>it is true</em>. The Psalms close three of their five books with doxologies ending in Amen (Pss. 41:13; 72:19; 89:52), and the congregation's Amen in response to Levitical blessings appears in Deuteronomy 27. In synagogue and early church practice, the responsive Amen ratified the public prayer of the leader (1 Cor. 14:16).</p><p>Jesus employed Amen in a distinctive way by prefacing his own declarations with <em>Amen I say to you</em> (translated <em>Verily</em> in the Authorized Version), an unprecedented formula asserting personal rather than derived authority. Revelation 3:14 applies the title <em>the Amen</em> to Christ himself, identifying him as the faithful and true witness in whom all of God's promises are confirmed (cf. 2 Cor. 1:20).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "amen", "smith": "amen", "isbe": "amen"},
        "key_refs": ["Revelation 3:14", "Isaiah 65:16", "Psalms 41:13", "Psalms 72:19", "Psalms 89:52"],
        "sections": []
    },
    "amethyst": {
        "id": "amethyst",
        "term": "Amethyst",
        "category": "concepts",
        "intro": "<p>Amethyst (Hebrew <em>'ahlamah</em>; Greek <em>amethystos</em>) is a purple variety of quartz prized as a gemstone in the ancient world. It was set in the third row of the high priest's breastplate, the twelfth stone in the four-by-three arrangement of twelve gems representing the twelve tribes of Israel (Exod. 28:19; 39:12). In Revelation 21:20 amethyst is listed as the twelfth stone in the foundations of the walls of the New Jerusalem, maintaining a symbolic correspondence with the breastplate's arrangement. Ancient Egyptians and Greeks used amethyst extensively for seals and amulets; the Greek name derives from a belief that the stone prevented intoxication.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "amethyst", "smith": "amethyst", "isbe": "amethyst"},
        "key_refs": ["Exodus 28:19", "Exodus 39:12", "Revelation 21:20"],
        "sections": []
    },
    "amittai": {
        "id": "amittai",
        "term": "Amittai",
        "category": "people",
        "intro": "<p>Amittai (meaning <em>true</em> or <em>fearing</em>) was the father of the prophet Jonah, identified as a native of Gath-hepher in the territory of Zebulun (2 Kgs. 14:25; Jon. 1:1). He is named only in connection with his son: once in the historical record identifying Jonah as the prophet who predicted Jeroboam II's restoration of Israel's borders, and once in the opening verse of the Book of Jonah. Nothing further is known of Amittai, making him one of the many minor figures in prophetic superscriptions whose significance lies solely in their connection to a greater personality.</p>",
        "hitchcock_meaning": "true; fearing",
        "source_ids": {"easton": "amittai", "smith": "amittai", "isbe": "amittai"},
        "key_refs": ["2 Kings 14:25", "Jonah 1:1"],
        "sections": []
    },
    "ammah": {
        "id": "ammah",
        "term": "Ammah",
        "category": "places",
        "intro": "<p>Ammah (meaning <em>a cubit</em> or <em>my people</em>) was a hill in the territory of Benjamin near Giah, east of Gibeon, to which Joab and Abishai pursued Abner and his men after the battle at the pool of Gibeon (2 Sam. 2:24). It was at Ammah that Abner called for a cessation of pursuit, and Joab agreed, allowing the army of Ish-bosheth to withdraw. The site marks a critical moment in the prolonged contest between the houses of David and Saul in the years following David's establishment at Hebron. Its precise location has not been identified.</p>",
        "hitchcock_meaning": "my, or his, people",
        "source_ids": {"easton": "ammah", "smith": "ammah", "isbe": "ammah"},
        "key_refs": ["2 Samuel 2:24"],
        "sections": []
    },
    "ammi": {
        "id": "ammi",
        "term": "Ammi",
        "category": "concepts",
        "intro": "<p>Ammi (meaning <em>my people</em>) is a prophetic name given by God to Israel in Hosea 2:1, standing in deliberate contrast to Lo-ammi (<em>not my people</em>) pronounced earlier as a sign of divine rejection (Hos. 1:9). The oracle of Hosea 2:1 envisions a future restoration in which God would again claim Israel as his covenant people, reversing the name of rejection. Paul cites this reversal in Romans 9:25–26 to support his argument that God's sovereign mercy extends beyond ethnic Israel to include Gentiles who were previously <em>not my people</em>, giving the name concentrated theological weight regarding covenant, rejection, and restoration.</p>",
        "hitchcock_meaning": "same as Ammah",
        "source_ids": {"easton": "ammi", "smith": "ammi", "isbe": "ammi"},
        "key_refs": ["Hosea 2:1", "Hosea 2:23", "Romans 9:25", "Romans 9:26"],
        "sections": []
    },
    "ammiel": {
        "id": "ammiel",
        "term": "Ammiel",
        "category": "people",
        "intro": "<p>Ammiel (meaning <em>the people of God</em>) is the name of four distinct individuals in the Old Testament. (1) The spy from the tribe of Dan sent by Moses to explore Canaan who brought a discouraging report and died in the subsequent plague (Num. 13:12; 14:37). (2) The father of Machir of Lo-debar, who cared for Mephibosheth, Jonathan's lame son; David later restored Mephibosheth's inheritance through this connection (2 Sam. 9:4). (3) The father of Bath-sheba, listed in 1 Chronicles 3:5 as Ammiel, though 2 Samuel 11:3 gives her father's name as Eliam — names that appear to be the same elements inverted. (4) A Levitical gatekeeper in the temple service under David (1 Chr. 26:5).</p>",
        "hitchcock_meaning": "the people of God",
        "source_ids": {"easton": "ammiel", "smith": "ammiel", "isbe": "ammiel"},
        "key_refs": ["Numbers 13:12", "Numbers 14:37", "2 Samuel 9:4"],
        "sections": []
    },
    "ammihud": {
        "id": "ammihud",
        "term": "Ammihud",
        "category": "people",
        "intro": "<p>Ammihud (meaning <em>people of glory</em> or <em>renowned people</em>) is the name of several individuals in the Old Testament, primarily fathers of tribal leaders during the wilderness period. (1) Elishama the son of Ammihud was the prince of Ephraim in the wilderness census (Num. 1:10; 2:18; 7:48, 53). (2) Shemuel the son of Ammihud represented Simeon in the allotment of Canaan (Num. 34:20). (3) Pedahel the son of Ammihud represented Naphtali in the same commission (Num. 34:28). (4) A Judahite son of Omri settled in Jerusalem after the exile (1 Chr. 9:4). The name's concentration among tribal representatives reflects its use in prominent Israelite families across multiple tribes.</p>",
        "hitchcock_meaning": "people of praise",
        "source_ids": {"easton": "ammihud", "smith": "ammihud", "isbe": "ammihud"},
        "key_refs": ["Numbers 1:10", "Numbers 2:18", "Numbers 7:48", "Numbers 7:53", "Numbers 34:20"],
        "sections": []
    },
    "amminadab": {
        "id": "amminadab",
        "term": "Amminadab",
        "category": "people",
        "intro": "<p>Amminadab (meaning <em>kindred of the prince</em> or <em>my people are willing</em>) is most importantly the father of Nahshon (leader of the tribe of Judah in the wilderness) and the father of Elisheba (Aaron's wife, Exod. 6:23). Through both connections — the priestly line of Aaron and the royal line of David — Amminadab stands at a significant genealogical juncture in salvation history. He appears in the genealogy of Christ in both Matthew 1:4 and Luke 3:33, placing him in the direct ancestral line of Jesus.</p><p>A second Amminadab was a Levite, son of Kohath, who played a role in transporting the ark to Jerusalem under David (1 Chr. 6:22; 15:10–11). His name being shared by figures in both Judah and Levi illustrates the cross-tribal connections common in this period.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "amminadab", "smith": "amminadab", "isbe": "amminadab"},
        "key_refs": ["Numbers 1:7", "Numbers 2:3", "Numbers 7:12", "Numbers 7:17", "Numbers 10:14"],
        "sections": []
    },
    "amminadib": {
        "id": "amminadib",
        "term": "Amminadib",
        "category": "people",
        "intro": "<p>Amminadib appears in the obscure phrase of Song of Solomon 6:12, where the beloved says her soul made her <em>like the chariots of Amminadib</em>. Interpretation is divided between treating this as a proper name of an otherwise unknown individual renowned for swift chariots, and reading it as a phrase (<em>am-mi-nadib</em> = <em>my willing people</em>) describing eager movement. The Revised Version and many modern translations favor the common-noun reading. If it is a proper name, Amminadib is otherwise unknown in biblical literature, and the proverbial reference to his chariots would have evoked a context now lost.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "amminadib", "smith": "amminadib", "isbe": "amminadib"},
        "key_refs": ["Song of Solomon 6:12"],
        "sections": []
    },
    "ammishaddai": {
        "id": "ammishaddai",
        "term": "Ammishaddai",
        "category": "people",
        "intro": "<p>Ammishaddai (meaning <em>the people of the Almighty</em> or <em>the Almighty is my kinsman</em>) was the father of Ahiezer, the appointed leader of the tribe of Dan in the wilderness period (Num. 1:12; 2:25). Ahiezer commanded the rear guard of the Israelite camp as it marched through the wilderness, and Ammishaddai is mentioned exclusively as his father's identifier. His name, incorporating the divine title <em>Shaddai</em> (God Almighty), reflects the theophoric naming practices common among Israelites of the patriarchal and early tribal period.</p>",
        "hitchcock_meaning": "the people of the Almighty; the Almighty is with me",
        "source_ids": {"easton": "ammishaddai", "isbe": "ammishaddai"},
        "key_refs": ["Numbers 1:12", "Numbers 2:25"],
        "sections": []
    },
    "ammizabad": {
        "id": "ammizabad",
        "term": "Ammizabad",
        "category": "people",
        "intro": "<p>Ammizabad (meaning <em>people of the giver</em> or <em>dowry of the people</em>) was the son of Benaiah, one of David's most renowned mighty men and later Solomon's commander of the army. Ammizabad served in his father's place commanding the third monthly division of David's rotating military organization (1 Chr. 27:6). His appointment reflects the Davidic practice of distributing military command across a broad officer class, with capable sons inheriting their fathers' positions in royal service.</p>",
        "hitchcock_meaning": "dowry of the people",
        "source_ids": {"easton": "ammizabad", "smith": "ammizabad", "isbe": "ammizabad"},
        "key_refs": ["1 Chronicles 27:6"],
        "sections": []
    },
    "ammon": {
        "id": "ammon",
        "term": "Ammon",
        "category": "people",
        "intro": "<p>Ammon is the name given to Ben-ammi, the son of Lot by his younger daughter, born after the destruction of Sodom (Gen. 19:38). He became the eponymous ancestor of the Ammonites, a people who settled east of the Jordan River between the Arnon and Jabbok rivers. The name Ben-ammi means <em>son of my people</em>, and the Ammonites are consistently identified in Scripture as descended from Lot, making them distant kinsmen of Israel. The narrative of their origin in incest is typically read as an etiology explaining the fraught coexistence between Israel and Ammon throughout the biblical period.</p>",
        "hitchcock_meaning": "a people; the son of my people",
        "source_ids": {"easton": "ammon", "smith": "ammon"},
        "key_refs": ["Genesis 19:38", "Psalms 83:7"],
        "sections": []
    },
    "ammonite": {
        "id": "ammonite",
        "term": "Ammonite",
        "category": "concepts",
        "intro": "<p>The Ammonites were the descendants of Ben-ammi (Ammon), son of Lot, who occupied the territory east of the Jordan between the Arnon and Jabbok rivers with their capital at Rabbah (modern Amman). As kinsmen of Israel through Lot, they were excluded from the Israelite assembly to the tenth generation (Deut. 23:3) but were not to be dispossessed of their land, which God had given to them as Lot's descendants (Deut. 2:19).</p><p>During the judges period, Ammonites joined Moabite coalitions against Israel (Judg. 3:13) and later oppressed the Transjordanian tribes, prompting Jephthah's campaign (Judg. 10–11). Nahash the Ammonite's siege of Jabesh-gilead galvanized support for Saul's kingship (1 Sam. 11). David fought successful wars against Ammon (2 Sam. 10–12). Solomon's Ammonite wives led him to worship Milcom (1 Kgs. 11:5). The prophets pronounced repeated judgment on Ammon for their hostility toward Israel (Jer. 49:1–6; Ezek. 25:1–7; Amos 1:13–15).</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ammonite"},
        "key_refs": ["Genesis 19:38", "Deuteronomy 2:16", "Judges 10:11", "2 Chronicles 20:1"],
        "sections": []
    },
    "amnon": {
        "id": "amnon",
        "term": "Amnon",
        "category": "people",
        "intro": "<p>Amnon (meaning <em>faithful</em> or <em>tutor</em>) was the eldest son of David, born of Ahinoam of Jezreel (2 Sam. 3:2; 1 Chr. 3:1). He is remembered primarily for his violation of his half-sister Tamar, the full sister of Absalom (2 Sam. 13). After the assault, he turned against her with contempt equal to his former obsession. David was furious but did not punish him, and Absalom harbored hatred for two years before orchestrating Amnon's murder at a sheep-shearing feast in Baal-hazor (2 Sam. 13:28–29). Amnon's death removed the first claimant to David's throne and set in motion the chain of dynastic violence culminating in Absalom's rebellion.</p>",
        "hitchcock_meaning": "faithful and true; tutor",
        "source_ids": {"easton": "amnon", "smith": "amnon", "isbe": "amnon"},
        "key_refs": ["1 Chronicles 4:20", "1 Chronicles 3:1", "2 Samuel 3:2", "2 Samuel 13:28", "2 Samuel 13:29"],
        "sections": []
    },
    "amon": {
        "id": "amon",
        "term": "Amon",
        "category": "people",
        "intro": "<p>Amon (meaning <em>builder</em> or <em>faithful</em>) is the name of three biblical figures. (1) The governor of Samaria under Ahab, to whom the prophet Micaiah was committed after predicting Israel's defeat at Ramoth-gilead (1 Kgs. 22:26; 2 Chr. 18:25). (2) The son and successor of Manasseh as king of Judah (c. 642–640 BC). Amon continued his father's idolatries but reigned only two years before being assassinated by his own servants. His son Josiah, succeeding at age eight, later reversed course with sweeping reforms. Amon appears in the genealogy of Christ (Matt. 1:10). (3) Amon (No-Amon) was also the chief deity of Thebes in Egypt, one of the gods upon whom Jeremiah pronounced divine judgment (Jer. 46:25).</p>",
        "hitchcock_meaning": "faithful; true",
        "source_ids": {"easton": "amon", "smith": "amon", "isbe": "amon"},
        "key_refs": ["1 Kings 22:26", "2 Chronicles 18:25", "2 Kings 21:18", "2 Chronicles 33:20", "Jeremiah 46:25"],
        "sections": []
    },
    "amorites": {
        "id": "amorites",
        "term": "Amorites",
        "category": "concepts",
        "intro": "<p>The Amorites (meaning <em>highlanders</em> or <em>westerners</em>) were one of the pre-Israelite peoples of Canaan, descended from Canaan the son of Ham (Gen. 10:16). The name is used in the Old Testament with varying scope: at times it designates a specific hill-country people distinct from the coastal Canaanites (Num. 13:29; Deut. 1:7), and at other times it serves as a comprehensive name for all the pre-Israelite inhabitants of the land (Gen. 15:16; Josh. 24:15).</p><p>By the time of the exodus, the Amorite kingdoms of Sihon and Og controlled Transjordan and were defeated by Israel before the Jordan crossing (Num. 21:21–35). Earlier, Abraham had Amorite confederates (Gen. 14:13). In Genesis 15:16, God informs Abraham that Israel will return to Canaan when <em>the iniquity of the Amorites is not yet complete</em>, framing the conquest as a delayed act of moral judgment. The Amorites largely disappear from the biblical record after the Davidic period.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "amorites", "isbe": "amorites"},
        "key_refs": ["Genesis 14:7", "Deuteronomy 1:7", "Deuteronomy 1:19", "Deuteronomy 1:20", "Deuteronomy 3:8"],
        "sections": []
    },
    "amos": {
        "id": "amos",
        "term": "Amos",
        "category": "people",
        "intro": "<p>Amos (meaning <em>borne</em> or <em>a burden</em>) was a prophet from Tekoa in the hill country of Judah who exercised his ministry in the northern kingdom of Israel, primarily at Bethel, during the reign of Jeroboam II (c. 760 BC). He is the earliest of the writing prophets whose oracles have been preserved in a canonical book. By his own account, Amos was neither a professional prophet nor the son of a prophet, but a shepherd and dresser of sycamore trees whom God called directly from agricultural work (Amos 7:14–15).</p><p>His book opens with oracles against surrounding nations before pivoting sharply to denounce Israel for social injustice, economic exploitation, religious formalism, and empty festival observance. He announced the day of the Lord not as a time of deliverance but of divine judgment — a radical reversal of popular expectation. The priest Amaziah of Bethel opposed and expelled him (Amos 7:10–13). His visions of the plumb line and the basket of summer fruit are among the most compact prophetic images in Scripture.</p>",
        "hitchcock_meaning": "loading; weighty",
        "source_ids": {"easton": "amos", "smith": "amos"},
        "key_refs": ["Amos 1:1", "Amos 7:14", "Amos 7:15", "Zechariah 14:5", "Joel 3:16"],
        "sections": []
    },
    "amoz": {
        "id": "amoz",
        "term": "Amoz",
        "category": "people",
        "intro": "<p>Amoz (meaning <em>strong</em> or <em>robust</em>) was the father of the prophet Isaiah, mentioned only in the superscriptions of Isaiah's prophecies (Isa. 1:1; 2:1; etc.) and in the parallel historical account of 2 Kings 19:2 and 20:1. Nothing more is known of Amoz from the biblical text. Jewish tradition in the Talmud suggests he was himself a prophet and a brother of King Amaziah of Judah, which would make Isaiah a member of the royal family — though this identification is not found in Scripture and cannot be verified.</p>",
        "hitchcock_meaning": "strong; robust",
        "source_ids": {"easton": "amoz", "smith": "amoz", "isbe": "amoz"},
        "key_refs": ["2 Kings 19:2", "Isaiah 1:1", "Isaiah 2:1"],
        "sections": []
    },
    "amphipolis": {
        "id": "amphipolis",
        "term": "Amphipolis",
        "category": "places",
        "intro": "<p>Amphipolis (meaning <em>city on both sides</em>) was a major Macedonian city situated on a peninsula almost entirely surrounded by the Strymon River, approximately thirty-three miles southwest of Philippi. Founded as an Athenian colony in 437 BC, it became the capital of the first district of Macedonia under Roman administration. Paul and Silas passed through Amphipolis on their journey from Philippi to Thessalonica during the second missionary journey (Acts 17:1), apparently without stopping to establish a congregation — suggesting there was no synagogue there to serve as the customary starting point for Paul's ministry.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "amphipolis", "smith": "amphipolis", "isbe": "amphipolis"},
        "key_refs": ["Acts 17:1"],
        "sections": []
    },
    "amplias": {
        "id": "amplias",
        "term": "Amplias",
        "category": "people",
        "intro": "<p>Amplias (meaning <em>large</em> or <em>extensive</em>) was a Christian at Rome greeted by Paul in Romans 16:8 as <em>my beloved in the Lord</em>. The name was common among Roman slaves and freedmen. Inscriptions in the Catacomb of Domitilla in Rome include the name Ampliatus in a context suggesting early Christian use, possibly preserving a memory of this individual. If so, he may have belonged to the household of a prominent Roman family, explaining how Paul could identify him by name in a church he had never personally visited.</p>",
        "hitchcock_meaning": "large; extensive",
        "source_ids": {"easton": "amplias", "smith": "amplias", "isbe": "amplias"},
        "key_refs": ["Romans 16:8"],
        "sections": []
    },
    "amram": {
        "id": "amram",
        "term": "Amram",
        "category": "people",
        "intro": "<p>Amram (meaning <em>exalted people</em> or <em>friend of Jehovah</em>) was the father of Moses, Aaron, and Miriam, the son of Kohath and grandson of Levi (Exod. 6:18, 20; Num. 3:19). He married Jochebed his father's sister — a union later forbidden by Mosaic law but predating that legislation — who bore him the three leaders of the exodus generation. Amram lived to the age of one hundred and thirty-seven (Exod. 6:20). His descendants, the Amramites, formed one of four Kohathite families responsible for carrying the most sacred elements of the sanctuary (Num. 3:27; 1 Chr. 26:23). A second Amram in the post-exilic period was a son of Bani who had married a foreign wife (Ezra 10:34).</p>",
        "hitchcock_meaning": "an exalted people; their sheaves; handfuls of corn",
        "source_ids": {"easton": "amram", "smith": "amram", "isbe": "amram"},
        "key_refs": ["Exodus 6:18", "Exodus 6:20", "Numbers 3:19", "Numbers 3:27", "1 Chronicles 26:23"],
        "sections": []
    },
    "amraphel": {
        "id": "amraphel",
        "term": "Amraphel",
        "category": "people",
        "intro": "<p>Amraphel was the king of Shinar (southern Mesopotamia/Babylonia) who led a coalition of four eastern kings in the campaign against five Canaanite city-kings described in Genesis 14. He is one of the four kings who defeated the kings of the Jordan plain and took Lot captive, prompting Abraham's rescue mission. Scholars of an earlier generation proposed to identify Amraphel with Hammurabi (c. 1792–1750 BC), the Babylonian lawgiver, largely on phonetic similarity, but this identification is now generally rejected due to chronological difficulties and linguistic problems with the proposed equation.</p>",
        "hitchcock_meaning": "one that speaks of secrets",
        "source_ids": {"easton": "amraphel", "smith": "amraphel", "isbe": "amraphel"},
        "key_refs": ["Genesis 14:1", "Genesis 14:4"],
        "sections": []
    },
    "anab": {
        "id": "anab",
        "term": "Anab",
        "category": "places",
        "intro": "<p>Anab (meaning <em>grape-town</em> or <em>a grape</em>) was a city in the hill country of Judah associated with the Anakim, the formidable inhabitants of Canaan. Joshua drove out the Anakim from the mountains of Judah including Hebron, Debir, and Anab, destroying them and their cities (Josh. 11:21). The site was later assigned to Judah (Josh. 15:50) and has been tentatively identified with Khirbet Anab es-Saghir or Anab el-Kebir, located about seven miles southwest of Hebron in the Judean highlands.</p>",
        "hitchcock_meaning": "a grape; a knot",
        "source_ids": {"easton": "anab", "smith": "anab", "isbe": "anab"},
        "key_refs": ["Joshua 11:21", "Joshua 15:50"],
        "sections": []
    },
    "anah": {
        "id": "anah",
        "term": "Anah",
        "category": "people",
        "intro": "<p>Anah (meaning <em>one who answers</em> or <em>afflicted</em>) is the name of two individuals in the Genesis 36 genealogy of Edom. (1) Anah son of Seir the Horite, one of the chiefs of the Horites who inhabited the land before Esau's descendants displaced them (Gen. 36:20, 29; 1 Chr. 1:38). (2) Anah son of Zibeon (also a son of Seir), who is credited with discovering something remarkable — either hot springs or a species of mule, as ancient versions differ — while pasturing his father's donkeys in the wilderness (Gen. 36:24). This Anah's daughter Aholibamah became one of the wives of Esau (Gen. 36:2, 14), making him the father-in-law of the patriarch.</p>",
        "hitchcock_meaning": "one who answers; afflicted",
        "source_ids": {"easton": "anah", "smith": "anah", "isbe": "anah"},
        "key_refs": ["Genesis 36:20", "Genesis 36:29", "1 Chronicles 1:38", "Genesis 36:18", "Genesis 36:24"],
        "sections": []
    },
    "anak": {
        "id": "anak",
        "term": "Anak",
        "category": "people",
        "intro": "<p>Anak (meaning <em>long-necked</em> or <em>a collar</em>) was the son of Arba, the founder of Kiriath-arba (Hebron), and patriarch of the Anakim — a people renowned for their great stature who inhabited the hill country of Canaan (Josh. 15:13; 21:11). Anak's three sons — Ahiman, Sheshai, and Talmai — still occupied Hebron when the twelve spies arrived (Num. 13:22), and their imposing presence contributed to the ten spies' discouraging report that the Israelites felt like grasshoppers by comparison. Caleb later drove out these three sons and took possession of Hebron as his inheritance (Josh. 15:14; Judg. 1:20).</p>",
        "hitchcock_meaning": "a collar; ornament",
        "source_ids": {"easton": "anak", "isbe": "anak"},
        "key_refs": ["Joshua 15:13", "Joshua 21:11"],
        "sections": []
    },
    "anakim": {
        "id": "anakim",
        "term": "Anakim",
        "category": "concepts",
        "intro": "<p>The Anakim (descendants of Anak, meaning <em>long-necked people</em>) were a people of exceptional stature inhabiting the hill country of Canaan, particularly the region around Hebron, before and during the Israelite conquest. When the twelve spies surveyed the land, the Anakim at Hebron produced the fearful report that Israel was like grasshoppers by comparison (Num. 13:28, 33). The same passage associates them with the Nephilim of Genesis 6, though the exact relationship is debated. Deuteronomy 9:2 describes them as a <em>great and tall people</em> against whom no one was thought able to stand.</p><p>Joshua's campaign against the Anakim was therefore a signal demonstration of divine power: he cut them off from the mountains of Hebron, Debir, and the southern highlands, driving survivors to Gaza, Gath, and Ashdod in Philistia (Josh. 11:21–22). Caleb's personal victory over Anak's three sons at Hebron (Josh. 14:12–15; 15:14) exemplified the faith the conquest demanded. Later Philistine giants such as Goliath may represent remnants of the Anakim who found refuge among the Philistines.</p>",
        "hitchcock_meaning": None,
        "source_ids": {"easton": "anakim", "smith": "anakim", "isbe": "anakim"},
        "key_refs": ["Joshua 11:21", "Numbers 13:33", "Deuteronomy 9:2", "Genesis 23:2", "Joshua 15:13"],
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
    print(f'BP Article Synthesis — a3: Ahlab → Anakim: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
