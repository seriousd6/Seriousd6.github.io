"""
BP Article Synthesis — e2: Elisabeth → Eshtaol
Covers Easton entries: Elisabeth through Eshtaol (75 entries)

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

Script: scripts/bp-e2.py
Run: python3 scripts/bp-e2.py
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
    "elisabeth": {
        "id": "elisabeth",
        "term": "Elisabeth",
        "category": "people",
        "intro": "<p>Elisabeth (also spelled Elizabeth) was a descendant of the priestly family of Aaron, wife of the priest Zacharias, and mother of John the Baptist. Her name, meaning <em>God is my oath</em> or <em>consecrated to God</em>, reflects her devout character. Luke's Gospel describes her as righteous before God, blameless in her observance of the Law, yet long barren—a condition that carried social stigma in ancient Israel.</p><p>Her miraculous conception of John in old age, announced by the angel Gabriel, parallels the stories of Sarah and Hannah. When her kinswoman Mary visited bearing the news of her own conception, Elisabeth was filled with the Holy Spirit and pronounced the blessing, \"Blessed are you among women.\" She remained in seclusion for five months after conceiving, and her son John would become the forerunner who prepared the way for Jesus.</p>",
        "sections": [],
        "hitchcock_meaning": "the oath, or fullness, of God",
        "source_ids": {
            "easton": "elisabeth",
            "smith": "elisabeth",
            "isbe": "elisabeth"
        },
        "key_refs": ["Luke 1:5", "Luke 1:13", "Luke 1:41", "Luke 1:60"]
    },
    "elishah": {
        "id": "elishah",
        "term": "Elishah",
        "category": "people",
        "intro": "<p>Elishah was the eldest son of Javan, the grandson of Noah through Japheth, and is reckoned among the seventy nations of the table of nations in Genesis 10. His name, meaning <em>God is salvation</em>, associates him with a branch of early post-diluvian humanity. Scholars have proposed various identifications, with proposals including the Greeks of Elis in the Peloponnese, the Aeolians, or inhabitants of the island of Cyprus or Sicily.</p><p>Ezekiel refers to the isles of Elishah as a source of blue and purple dye used for the awnings of Tyrian ships, linking the name to a seafaring Mediterranean people renowned for their textile trade. The geographical uncertainty reflects the ancient table's concern with ancestral origins rather than precise cartographic boundaries, and Elishah stands as one of the shadowy progenitors through whom Genesis traces the peopling of the post-flood world.</p>",
        "sections": [],
        "hitchcock_meaning": "it is God; the lamb of God",
        "source_ids": {
            "easton": "elishah",
            "smith": "elishah",
            "isbe": "elishah"
        },
        "key_refs": ["Genesis 10:4", "Ezekiel 27:7"]
    },
    "elisha": {
        "id": "elisha",
        "term": "Elisha",
        "category": "people",
        "intro": "<p>Elisha son of Shaphat, of Abel-meholah, was the disciple and successor of Elijah as prophet in Israel. His name, meaning <em>God is salvation</em>, summarizes the ministry of miraculous deliverance he exercised across some sixty years during the reigns of Joram, Jehu, Jehoahaz, and Joash. Called while plowing with twelve yoke of oxen, he burned his equipment and slaughtered his oxen as an irreversible break with his former life before following Elijah.</p><p>After Elijah's translation, Elisha received a double portion of his spirit and performed more recorded miracles than any other Old Testament figure: healing the waters of Jericho, raising the Shunammite's son, multiplying oil and bread, cleansing Naaman of leprosy, and blinding and restoring sight to Syrian soldiers. His ministry was notably more public and national than Elijah's, engaging kings and commanders. The New Testament notes him as an example of divine grace extending to Gentiles.</p>",
        "sections": [],
        "hitchcock_meaning": "salvation of God",
        "source_ids": {
            "easton": "elisha",
            "smith": "elisha",
            "isbe": "elisha"
        },
        "key_refs": ["1 Kings 19:19", "2 Kings 2:9", "2 Kings 5:1", "Luke 4:27"]
    },
    "elishama": {
        "id": "elishama",
        "term": "Elishama",
        "category": "people",
        "intro": "<p>Elishama, meaning <em>God hath heard</em>, is a name shared by several biblical figures. The most prominent was the son of Ammihud and prince of the tribe of Ephraim, who served as the tribe's leader during the wilderness journey and assisted Moses in the first census of Israel. He presented the offering for his tribe at the dedication of the altar.</p><p>Other bearers of the name include a son of King David born in Jerusalem, a royal scribe whose chamber held the written scroll of Jeremiah's prophecies, a son of the royal line of Judah descended from David through Elishama, and a priest sent by Jehoshaphat to teach the law in the cities of Judah. The frequency of the name reflects the widespread practice of names compounded with the divine element <em>El</em>, expressing a family's faith that God had responded to their prayer.</p>",
        "sections": [],
        "hitchcock_meaning": "God hath heard",
        "source_ids": {
            "easton": "elishama",
            "smith": "elishama",
            "isbe": "elishama"
        },
        "key_refs": ["Numbers 1:10", "Numbers 7:48", "2 Samuel 5:16", "Jeremiah 36:12"]
    },
    "elishaphat": {
        "id": "elishaphat",
        "term": "Elishaphat",
        "category": "people",
        "intro": "<p>Elishaphat son of Zichri was one of the five military commanders recruited by the priest Jehoiada to support the coup that overthrew the usurper Queen Athaliah and placed the young king Joash on the throne of Judah. His name means <em>my God hath judged</em>, and his role in the conspiracy was to command one of the corps of Levites and palace guards who secured the temple and palace precincts during the coronation.</p><p>The account in 2 Chronicles 23 describes how Jehoiada organized the priests and Levites into rotating companies, arming them from David's stored weapons in the temple. Elishaphat's participation represents the alliance of military loyalty and priestly authority that restored the Davidic line after Athaliah's six-year reign. He is mentioned only in this single episode and otherwise unknown in the biblical record.</p>",
        "sections": [],
        "hitchcock_meaning": "my God hath judged",
        "source_ids": {
            "easton": "elishaphat",
            "smith": "elishaphat"
        },
        "key_refs": ["2 Chronicles 23:1"]
    },
    "elisheba": {
        "id": "elisheba",
        "term": "Elisheba",
        "category": "people",
        "intro": "<p>Elisheba, daughter of Amminadab and sister of Naashon, was the wife of Aaron the high priest and thus the foundational matriarch of the entire Aaronic priesthood. Her name, meaning <em>God is an oath</em> or <em>God my swearing</em>, is the Hebrew equivalent of Elisabeth, and the same name reappears in the New Testament for the mother of John the Baptist. Through Aaron she became the mother of Nadab, Abihu, Eleazar, and Ithamar.</p><p>Elisheba stands at the intersection of two great Israelite tribal genealogies: her brother Naashon was the prince of Judah during the wilderness wandering, and her husband Aaron was the brother of Moses and the founder of Israel's priestly order. The concise reference to her in Exodus 6:23 contains unusual genealogical detail for a woman, suggesting that the narrator wished to mark the honor of her lineage and the importance of her priestly descendants.</p>",
        "sections": [],
        "hitchcock_meaning": "fullness of God",
        "source_ids": {
            "easton": "elisheba",
            "smith": "elisheba"
        },
        "key_refs": ["Exodus 6:23"]
    },
    "elishua": {
        "id": "elishua",
        "term": "Elishua",
        "category": "people",
        "intro": "<p>Elishua was one of the sons born to David in Jerusalem after he became king over all Israel, listed among the children of his various wives and concubines. His name, meaning <em>God is my salvation</em>, reflects the God-exalting naming conventions common in the Davidic court. He appears in both the Samueline and Chronicles genealogies of David's Jerusalem-born sons, distinguishing him from sons born in Hebron.</p><p>Beyond this genealogical placement, Elishua plays no individual role in the narrative of Scripture. His presence in the lists of David's sons underscores the royal dynasty's expansion in Jerusalem and the multiplication of the Davidic family that formed the background for succession struggles. The name closely resembles Elisha and may represent a variant spelling in the transmission of the genealogical record.</p>",
        "sections": [],
        "hitchcock_meaning": "God is my salvation",
        "source_ids": {
            "easton": "elishua",
            "smith": "elishua"
        },
        "key_refs": ["2 Samuel 5:15", "1 Chronicles 14:5"]
    },
    "elkosh": {
        "id": "elkosh",
        "term": "Elkosh",
        "category": "places",
        "intro": "<p>Elkosh was the birthplace of the prophet Nahum, as identified in the opening verse of his book. The name, sometimes interpreted as <em>God the ensnarer</em> or connected to a root meaning <em>hardness</em>, is otherwise unattested in Scripture. Its precise location has been disputed since antiquity, with several rival identifications proposed by scholars and travelers.</p><p>Three main theories have been advanced: that Elkosh was a village in Galilee near the modern site of el-Kauze (which later Jewish tradition favored and for which a tomb of Nahum was venerated), that it was a town in Judah in the Shephelah, or that it was located in Assyria near Nineveh (a tradition preserved by Eastern Christians who pointed to a tomb near Alqosh in Iraq). The Galilean or Judean identification is favored by most modern scholars, and the Galilean site aligns with a tradition attested as early as Jerome in the fourth century.</p>",
        "sections": [],
        "hitchcock_meaning": "hardness, my bow, or the God that is jealous",
        "source_ids": {
            "easton": "elkosh",
            "smith": "elkosh",
            "isbe": "elkosh"
        },
        "key_refs": ["Nahum 1:1"]
    },
    "elkanah": {
        "id": "elkanah",
        "term": "Elkanah",
        "category": "people",
        "intro": "<p>The most prominent Elkanah in Scripture was the Ephraimite father of the prophet Samuel. Described as a devout man who made annual pilgrimages to Shiloh to worship and offer sacrifice, he had two wives: Peninnah, who bore children, and Hannah, who was barren. His patient kindness toward the grieving Hannah—asking \"Am I not better to you than ten sons?\"—reveals a tenderness unusual in depictions of patriarchal households.</p><p>The name Elkanah, meaning <em>God hath possessed</em> or <em>God hath created</em>, is shared by numerous Levitical figures throughout the Old Testament, including a son of Korah, several Levites in the genealogies of Chronicles, and a doorkeeper for the ark in the time of David. The frequency of the name suggests it was a common Levitical designation. Samuel's father is identified in Chronicles as a Levite despite being called an Ephraimite in Samuel, a discrepancy reconciled by noting he was a Levite residing in Ephraimite territory.</p>",
        "sections": [],
        "hitchcock_meaning": "God the jealous; the zeal of God",
        "source_ids": {
            "easton": "elkanah",
            "smith": "elkanah",
            "isbe": "elkanah"
        },
        "key_refs": ["1 Samuel 1:1", "1 Samuel 1:8", "1 Samuel 2:20", "1 Chronicles 6:23"]
    },
    "ellasar": {
        "id": "ellasar",
        "term": "Ellasar",
        "category": "places",
        "intro": "<p>Ellasar was the kingdom of Arioch, one of the four kings who defeated the five kings of the cities of the plain in the war described in Genesis 14. The identification of Ellasar has been extensively debated among biblical geographers and Assyriologists. One prominent theory equates it with Larsa, the ancient Babylonian city in southern Mesopotamia that was a major power in the early second millennium BC.</p><p>Alternatively, some scholars have associated Ellasar with Ilansura in northern Mesopotamia or with Assur itself. The Genesis 14 narrative is one of the most historically complex passages in the Pentateuch, involving a coalition of eastern kings raiding as far as the Negev and the Dead Sea region, and the identities of their home territories remain uncertain. Whatever its precise location, Ellasar stands as one of the eastern powers that Genesis presents as having had their reach interrupted by Abraham's intervention on behalf of Lot.</p>",
        "sections": [],
        "hitchcock_meaning": "God is chastisement there; the oak of Assyria",
        "source_ids": {
            "easton": "ellasar",
            "smith": "ellasar",
            "isbe": "ellasar"
        },
        "key_refs": ["Genesis 14:1", "Genesis 14:9"]
    },
    "elnathan": {
        "id": "elnathan",
        "term": "Elnathan",
        "category": "people",
        "intro": "<p>Elnathan, whose name means <em>God hath given</em>, appears in several distinct contexts in the Old Testament. The most historically significant was the son of Achbor, a court official sent by King Jehoiakim to Egypt to extradite the prophet Uriah, who had fled there after prophesying against Jerusalem. Elnathan carried out the mission, returning Uriah to Judah where he was executed. Yet this same Elnathan, along with other officials, urged the king not to burn Jeremiah's scroll—a gesture of restraint that the king ignored.</p><p>Another Elnathan was the father of Nehushta, the mother of King Jehoiachin, making him the maternal grandfather of a king of Judah. Ezra records three men of the name among the leading men and Levites gathered at the Ahava River before the second return from exile. The name was evidently common enough in late preexilic and postexilic Judah to be borne by multiple unrelated individuals.</p>",
        "sections": [],
        "hitchcock_meaning": "God hath given; the gift of God",
        "source_ids": {
            "easton": "elnathan",
            "smith": "elnathan",
            "isbe": "elnathan"
        },
        "key_refs": ["2 Kings 24:8", "Jeremiah 26:22", "Jeremiah 36:12", "Ezra 8:16"]
    },
    "el-paran": {
        "id": "el-paran",
        "term": "El-paran",
        "category": "places",
        "intro": "<p>El-paran, meaning <em>the oak (or terebinth) of Paran</em>, was the southernmost point reached by the eastern coalition of four kings in the campaign described in Genesis 14 before they turned northward to attack the cities of the plain. The narrative traces their route southward through Transjordan and the Negev before this turning point.</p><p>El-paran is associated with the wilderness of Paran, the broad desert region of the Sinai peninsula and northern Arabia through which the Israelites also journeyed during the Exodus. The phrase suggests a notable tree or grove in the Paran wilderness that served as a landmark. Some commentators identify it with a location near Elath (Ezion-geber) at the head of the Gulf of Aqaba, on the edge of the wilderness through which caravan routes passed. The brief mention captures a geographical sweep of the ancient near eastern world from Mesopotamia to the far south.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "el-paran",
            "smith": "el-paran"
        },
        "key_refs": ["Genesis 14:6"]
    },
    "elymas": {
        "id": "elymas",
        "term": "Elymas",
        "category": "people",
        "intro": "<p>Elymas was the surname of Bar-jesus, a Jewish false prophet and sorcerer attached to the court of Sergius Paulus, the Roman proconsul of Cyprus. When Barnabas and Paul visited the island during their first missionary journey, Sergius Paulus summoned them to hear the word of God, but Elymas actively opposed them, seeking to turn the proconsul away from the faith. The name Elymas is understood to mean <em>wise man</em> or <em>sorcerer</em>, functioning as an Arabic translation of his title.</p><p>Paul, filled with the Holy Spirit, confronted Elymas directly, denouncing him as a son of the devil, an enemy of righteousness, and a perverter of the ways of God. Paul then pronounced a temporary blindness on him, and the sorcerer immediately groped in darkness seeking someone to lead him by the hand. Witnessing this miracle of judgment, Sergius Paulus believed. The episode demonstrates the power of the gospel over the competing spiritual authorities of the Roman world.</p>",
        "sections": [],
        "hitchcock_meaning": "a magician, a corrupter",
        "source_ids": {
            "easton": "elymas",
            "smith": "elymas",
            "isbe": "elymas"
        },
        "key_refs": ["Acts 13:6", "Acts 13:8", "Acts 13:11", "Acts 13:12"]
    },
    "embalming": {
        "id": "embalming",
        "term": "Embalming",
        "category": "concepts",
        "intro": "<p>Embalming—the preservation of a body through the application of aromatic spices, oils, and occasionally more elaborate techniques—was practiced in the biblical world primarily under Egyptian influence. In the Old Testament, only two individuals are explicitly said to have been embalmed: Jacob and his son Joseph, both of whom died in Egypt. The account in Genesis 50 notes that Joseph commanded his servants the physicians to embalm his father, a process that took forty days and was followed by seventy days of Egyptian mourning.</p><p>Joseph himself was embalmed at death and his body kept in a coffin in Egypt until Moses carried his bones out at the Exodus, fulfilling Joseph's sworn request. Among the Hebrews generally, burial rather than embalming was the norm, typically accomplished rapidly and with simpler preparations of washing, anointing, and wrapping. The New Testament references to wrapping the bodies of Lazarus and Jesus in linen with spices represent a form of honorable burial preparation, though not necessarily the elaborate Egyptian process. The anointing of Jesus's body was additionally associated with messianic consecration in early Christian thought.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "embalming",
            "smith": "embalming",
            "isbe": "embalming"
        },
        "key_refs": ["Genesis 50:2", "Genesis 50:26", "John 19:40", "John 11:44"]
    },
    "embroider": {
        "id": "embroider",
        "term": "Embroider",
        "category": "concepts",
        "intro": "<p>Embroidery in the biblical world referred to the skilled needlework that decorated sacred textiles, royal garments, and items of prestige. The Hebrew term <em>raqam</em> (to variegate or weave in colors) distinguishes embroidered work from plain weaving and from woven tapestry. Bezalel and Aholiab were divinely gifted craftsmen commissioned to execute the embroidered work of the tabernacle, including the screen at the gate of the court, the screen at the door of the tent, and elements of the high priestly garments.</p><p>The priestly vestments featured embroidery extensively: the linen coat of Aaron was \"woven work,\" and the girdle was \"the work of the embroiderer.\" Fine embroidered linen from Egypt was a prized trade commodity in the ancient Near East, and Ezekiel uses such luxury textiles metaphorically to describe the splendor and subsequent corruption of Tyre. Embroidery thus carried associations of both divine worship—the beauty fitting for the presence of God—and the wealth and craftsmanship of the surrounding civilizations.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "embroider",
            "isbe": "embroidery"
        },
        "key_refs": ["Exodus 28:39", "Exodus 35:35", "Exodus 38:18", "Ezekiel 27:7"]
    },
    "emerald": {
        "id": "emerald",
        "term": "Emerald",
        "category": "concepts",
        "intro": "<p>The emerald was among the most prized gemstones of the ancient world, valued for its deep green color. In the Old Testament the Hebrew <em>nophek</em> appears in the second row of the high priest's breastplate, though its precise identification is disputed—some scholars render it as carbuncle or turquoise rather than emerald. The Septuagint renders it as <em>anthrax</em> (carbuncle or garnet), while the Vulgate gives <em>carbunculus</em>.</p><p>In the New Testament, the Greek <em>smaragdos</em> appears in the Apocalypse: Revelation 4:3 describes a rainbow around the throne of God that looked like an emerald in appearance, evoking a vivid green radiance surrounding the divine throne. The emerald also appears in the foundation stones of the New Jerusalem in Revelation 21:19. Ezekiel's description of the king of Tyre's covering includes precious stones with <em>nophek</em> among them. The rarity and brilliance of the emerald made it a natural symbol of divine glory and the consummate beauty of celestial realities.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "emerald",
            "smith": "emerald",
            "isbe": "emerald"
        },
        "key_refs": ["Exodus 28:18", "Ezekiel 28:13", "Revelation 4:3", "Revelation 21:19"]
    },
    "emerod": {
        "id": "emerod",
        "term": "Emerod",
        "category": "concepts",
        "intro": "<p>Emerods (from the Old French <em>emorroides</em>, hemorrhoids) is the term used in the King James Version for the affliction that struck the Philistines when they captured the ark of the covenant and kept it in their territory. The Hebrew word <em>ophalim</em> (or <em>techorim</em> in the Ketiv/Qere reading) describes tumors or swellings—possibly hemorrhoids, tumors, or pustular swellings associated with bubonic plague—that broke out among the people of Ashdod, Gath, Ekron, and the surrounding regions.</p><p>The connection between the emerods, a plague of mice (or rats), and the sudden deaths in the Philistine cities has led many commentators to interpret the episode as an outbreak of bubonic plague, in which rodents serve as vectors and lymphatic swellings (buboes) are a characteristic symptom. As part of the guilt offering sent with the returned ark, the Philistines fashioned five golden emerods and five golden mice, one for each of the five Philistine lords, acknowledging the divine punishment and seeking relief.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "emerod",
            "smith": "emerod",
            "isbe": "emerods"
        },
        "key_refs": ["1 Samuel 5:6", "1 Samuel 5:12", "1 Samuel 6:4", "1 Samuel 6:5"]
    },
    "emims": {
        "id": "emims",
        "term": "Emims",
        "category": "people",
        "intro": "<p>The Emims were an ancient race of giants who inhabited the territory east of the Jordan, specifically the region that later became the land of Moab. Described in Deuteronomy 2:10–11 as a people great and many, and tall as the Anakim, they were counted among the Rephaim, the broad biblical category of pre-Israelite giant peoples. Their name in Hebrew (<em>ʾêmîm</em>) is interpreted as <em>the terrible ones</em> or <em>the dreadful ones</em>, reflecting the terror they inspired.</p><p>The Moabites displaced the Emims and occupied their territory, just as the Edomites displaced the Horites from Mount Seir. Genesis 14 records them as inhabiting Shaveh-kiriathaim when the eastern coalition kings swept through the region in the time of Abraham, providing the earliest biblical reference to their presence. The note about the Emims functions in Deuteronomy as encouragement to Israel: if God enabled Moab to displace giants, he could surely enable Israel to take Canaan, despite the intimidating reports of large peoples there.</p>",
        "sections": [],
        "hitchcock_meaning": "fears, terrors",
        "source_ids": {
            "easton": "emims",
            "smith": "emims",
            "isbe": "emim"
        },
        "key_refs": ["Genesis 14:5", "Deuteronomy 2:10", "Deuteronomy 2:11"]
    },
    "emmanuel": {
        "id": "emmanuel",
        "term": "Emmanuel",
        "category": "concepts",
        "intro": "<p>Emmanuel (Hebrew <em>Immanuel</em>, meaning <em>God with us</em>) is the prophetic name given in Isaiah 7:14 to a child whose birth would serve as a sign to King Ahaz during the Syro-Ephraimite crisis. The sign promised that before the child was old enough to discern good from evil, the two threatening kings would be gone. Matthew 1:23 explicitly applies this prophecy to Jesus, citing the Septuagint rendering and interpreting the virgin birth as its ultimate fulfillment.</p><p>The theological weight of the name lies in the affirmation of divine presence and identification. Throughout Isaiah's prophecy the concept of God's presence with Israel as deliverer recurs as a theme (Isaiah 8:8, 8:10), and by the New Testament's application the name becomes a christological title affirming the incarnation—God taking on human nature to dwell among his people. The name does not function as a regular personal name for Jesus in the New Testament but rather as a prophetic designation capturing the meaning of the incarnation: God has come to be among humanity.</p>",
        "sections": [],
        "hitchcock_meaning": "God with us",
        "source_ids": {
            "easton": "emmanuel",
            "smith": "immanuel",
            "isbe": "immanuel"
        },
        "key_refs": ["Isaiah 7:14", "Isaiah 8:8", "Matthew 1:23"]
    },
    "emmaus": {
        "id": "emmaus",
        "term": "Emmaus",
        "category": "places",
        "intro": "<p>Emmaus was a village some distance from Jerusalem to which two disciples of Jesus were traveling on the afternoon of the day of resurrection, when the risen Christ joined them incognito. The name is of uncertain etymology, possibly derived from a Hebrew root meaning <em>warm springs</em> or <em>warm baths</em>. The Gospel of Luke records the distance as sixty stadia (about seven miles), though some manuscripts give 160 stadia, a discrepancy that has fueled debate about the site's identification.</p><p>The narrative of the Emmaus road is among the most detailed resurrection accounts in the Gospels: the disciples' downcast conversation, Christ's exposition of scripture from Moses and the prophets, and the moment of recognition at the breaking of bread in which he vanished from sight. The episode has been profoundly influential in Christian liturgy and spirituality as a paradigm of Christ's presence in scripture and the Eucharist. Several sites have been proposed for Emmaus, including Nicopolis (Imwas), Abu Ghosh, and el-Qubeibeh, without scholarly consensus.</p>",
        "sections": [],
        "hitchcock_meaning": "people despised or obscure",
        "source_ids": {
            "easton": "emmaus",
            "smith": "emmaus",
            "isbe": "emmaus"
        },
        "key_refs": ["Luke 24:13", "Luke 24:15", "Luke 24:29", "Luke 24:35"]
    },
    "emmor": {
        "id": "emmor",
        "term": "Emmor",
        "category": "people",
        "intro": "<p>Emmor is the Greek New Testament form (Acts 7:16) of the Hebrew Hamor, the Hivite prince and father of Shechem who negotiated with Jacob's sons after his son Shechem violated Dinah. The name means <em>an ass</em> in Hebrew, a detail that some commentators regard as a reflection on his character or as a livestock-related family name common among Canaanite traders. Stephen's speech in Acts references the purchase of the tomb at Shechem from the sons of Emmor (Hamor), summarizing the patriarchal narratives in compressed form.</p><p>The reference in Acts 7:16 presents a condensed account that combines details from different burial traditions—Jacob's burial at Machpelah (Genesis 50) and the burial of Joseph's bones at Shechem (Joshua 24:32)—suggesting Stephen was drawing on a tradition of compressed genealogical summary familiar in the synagogue. Hamor/Emmor himself is the figure who negotiated the Shechemite males' agreement to be circumcised in exchange for intermarriage, a condition exploited by Simeon and Levi in the massacre that followed.</p>",
        "sections": [],
        "hitchcock_meaning": "an ass; clay; dirt",
        "source_ids": {
            "easton": "emmor",
            "smith": "hamor"
        },
        "key_refs": ["Acts 7:16", "Genesis 33:19", "Genesis 34:2"]
    },
    "encamp": {
        "id": "encamp",
        "term": "Encamp",
        "category": "concepts",
        "intro": "<p>The verb <em>to encamp</em> and the related noun <em>encampment</em> describe the formal, structured halting and setting up of camp that characterized Israel's wilderness movements. The Hebrew <em>ḥānâ</em> conveys settling down, resting, or pitching camp, and the Israelite encampment around the tabernacle was explicitly organized: the Levites surrounded the sanctuary in the innermost ring, with the twelve tribes arranged in groups of three on each of the four sides. This arrangement gave spatial expression to the theological reality of God dwelling in the midst of his people.</p><p>The encampment motif carries additional theological dimensions. Psalm 34:7 declares that the angel of the LORD encamps around those who fear him, transforming the military concept of a protective perimeter into a metaphor for divine guardianship of the faithful. The careful choreography of Israel's encampments—each tribe to its own standard, each family in its appointed place—modeled the ordered community life intended for those in covenant relationship with God, pointing forward to the eschatological vision of the people of God gathered around their king.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "encamp",
            "isbe": "camp-encampment"
        },
        "key_refs": ["Numbers 2:2", "Numbers 2:17", "Psalm 34:7"]
    },
    "enchantments": {
        "id": "enchantments",
        "term": "Enchantments",
        "category": "concepts",
        "intro": "<p>Enchantments in the biblical world referred to various forms of magic, sorcery, and divination that Israel was forbidden to practice. The Hebrew vocabulary is extensive: <em>laḥash</em> (whispering charms), <em>ḥeber</em> (binding spells), <em>naḥash</em> (divination by omens, especially serpents), and <em>qesem</em> (divination by lot or oracle) all fall within the scope of practices condemned in Deuteronomy 18 as abominations practiced by the nations being displaced before Israel.</p><p>The Egyptian magicians who opposed Moses are described as performing signs through their enchantments, though their power was ultimately limited and surpassed. Balaam's attempted curse-oracles are associated with enchantments in Numbers 24:1. The condemnation of enchantments reflects the theological principle that Israel's life was to be governed by the word of God through authorized prophets and priests, not by manipulation of spiritual forces through pagan techniques. The repeated association of enchantments with foreign religion underscored their incompatibility with covenant fidelity.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "enchantments",
            "smith": "magic",
            "isbe": "enchantment"
        },
        "key_refs": ["Exodus 7:11", "Exodus 7:22", "Numbers 24:1", "Deuteronomy 18:10"]
    },
    "end": {
        "id": "end",
        "term": "End",
        "category": "concepts",
        "intro": "<p>The concept of the <em>end</em> in Scripture encompasses both temporal finality and eschatological consummation. The Hebrew <em>qēṣ</em> and the Greek <em>telos</em> and <em>synteleia</em> carry a range of meanings: the physical termination of a thing, the completion or goal of a process, and the climactic end of the present age. The disciples' question about the end of the age in Matthew 24 reflects the Jewish apocalyptic framework in which history moves toward a divinely ordained culmination.</p><p>Daniel's prophecies repeatedly employ <em>qēṣ</em> for the end appointed for the kingdoms and tribulations of history, while the New Testament's <em>synteleia tou aiōnos</em> (consummation of the age) describes the wrap-up of the present era preceding the final judgment. The concept of the end is never purely temporal in biblical thought—it carries the freight of God's sovereign purpose, the fulfillment of his redemptive plan, and the transition from present conditions of sin and death to the eternal state. The end is thus both a terminus and a beginning, the closing of one economy and the opening of another.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "end",
            "isbe": "eschatology-of-the-ot"
        },
        "key_refs": ["Daniel 8:17", "Matthew 24:3", "Matthew 24:14", "1 Corinthians 15:24"]
    },
    "endor": {
        "id": "endor",
        "term": "En-dor",
        "category": "places",
        "intro": "<p>En-dor (<em>fountain of Dor</em> or <em>spring of the dwelling</em>) was a town on the northern slope of the hill of Moreh in the territory of Issachar, allocated to the half-tribe of Manasseh. Its most prominent biblical appearance is as the home of the woman who was a medium or witch, whom Saul consulted on the eve of his final battle with the Philistines at Jezreel. Disguising himself and approaching her by night, Saul asked her to call up the spirit of Samuel, receiving instead a terrifying prophecy of his own death.</p><p>Psalm 83:10 also mentions En-dor as the location where Jabin and Sisera were destroyed, identifying it with the battlefield of the Kishon where Deborah and Barak defeated the Canaanite coalition. The modern identification is with the village of Endour (Indur) on the northern face of Little Hermon, roughly four miles from the spring of Jezreel. The site sits in the fertile Jezreel valley, explaining its repeated association with military campaigns that converged on that strategically critical plain.</p>",
        "sections": [],
        "hitchcock_meaning": "fountain of Dor, of generation, or of habitation",
        "source_ids": {
            "easton": "en-dor",
            "smith": "en-dor",
            "isbe": "en-dor"
        },
        "key_refs": ["Joshua 17:11", "1 Samuel 28:7", "Psalm 83:10"]
    },
    "en-eglaim": {
        "id": "en-eglaim",
        "term": "En-eglaim",
        "category": "places",
        "intro": "<p>En-eglaim, meaning <em>fountain of two calves</em>, appears only once in Scripture, in Ezekiel 47:10, where the visionary river flowing eastward from the restored temple is said to bring life to waters from En-gedi to En-eglaim. Fishermen would stand along the Dead Sea shore from one spring to the other, indicating that the passage envisions a complete transformation of the salt sea into fresh, teeming waters.</p><p>The precise location of En-eglaim is uncertain. Some geographers place it near the northern end of the Dead Sea, on the east bank, in the vicinity of modern Ain Feshkha or a corresponding site opposite it. Others have proposed sites near the mouth of the Jordan. Its pairing with En-gedi—located on the western shore about midway along the sea—suggests it lay at the opposite end of the Dead Sea's inhabitable coastline, framing the entire shoreline as the site of future blessing. The name thus functions partly as a geographical marker for totality in Ezekiel's eschatological vision.</p>",
        "sections": [],
        "hitchcock_meaning": "fountain of calves",
        "source_ids": {
            "easton": "en-eglaim",
            "smith": "en-eglaim"
        },
        "key_refs": ["Ezekiel 47:10"]
    },
    "en-gannim": {
        "id": "en-gannim",
        "term": "En-gannim",
        "category": "places",
        "intro": "<p>En-gannim, meaning <em>fountain of gardens</em>, was the name of two distinct biblical towns. The first was a town in the lowland Shephelah of Judah, listed in Joshua 15:34 among the towns of the tribe of Judah in the vicinity of Zorah and Eshtaol. The second, more prominent En-gannim was a town in the territory of Issachar assigned to the Levites, identified with the Anem of 1 Chronicles 6:73.</p><p>This second En-gannim is generally identified with the modern Jenin, located at the southern entrance to the Jezreel Valley where a spring emerges, consistent with the name's meaning. The town controlled the main pass from Samaria into the Jezreel plain, making it a significant waypoint for travelers and armies moving between the coastal plain and the Galilee highlands. The name reflects the agricultural productivity associated with well-watered sites in ancient Palestine, where springs enabled garden cultivation in an otherwise arid landscape.</p>",
        "sections": [],
        "hitchcock_meaning": "fountain of gardens",
        "source_ids": {
            "easton": "en-gannim",
            "smith": "en-gannim",
            "isbe": "en-gannim"
        },
        "key_refs": ["Joshua 15:34", "Joshua 19:21", "Joshua 21:29"]
    },
    "engines": {
        "id": "engines",
        "term": "Engines",
        "category": "concepts",
        "intro": "<p>Engines of war in the biblical period referred to mechanical devices for offensive and defensive siege operations. The Hebrew <em>ḥishshābôn</em>, rendered <em>engines</em> in the KJV, appears in 2 Chronicles 26:15 to describe the devices that King Uzziah had constructed for placement on the towers and corners of Jerusalem's walls, designed to shoot arrows and hurl great stones against attackers. This is one of the earliest references in the Bible to mechanical military technology.</p><p>By the time of the later prophets and the New Testament era, siege engines included the battering ram (<em>kar</em>), towers for overlooking walls, and catapult-like artillery. Ezekiel's prophecy against Tyre (Ezekiel 26:9) envisions Nebuchadnezzar deploying engines of war against its walls. The development of siege technology in the ancient Near East drove corresponding innovations in fortification architecture, and the reference to Uzziah's engines reflects the escalating arms competition of the Iron Age period in which city defenses and offensive capabilities were constantly being updated.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "engines",
            "isbe": "war"
        },
        "key_refs": ["2 Chronicles 26:15", "Ezekiel 26:9"]
    },
    "en-hakkore": {
        "id": "en-hakkore",
        "term": "En-hakkore",
        "category": "places",
        "intro": "<p>En-hakkore, meaning <em>spring of the caller</em> or <em>fountain of him who called</em>, was the name given to a spring that God miraculously opened at Lehi after Samson's great victory over the Philistines with the jawbone of a donkey. Exhausted and desperately thirsty after slaying a thousand men, Samson cried out to God in prayer—the one recorded prayer of his life—acknowledging that if he died of thirst, the uncircumcised Philistines would claim the victory.</p><p>God opened a hollow in the rocky ground from which water burst forth, and the place was named En-hakkore to commemorate both the divine provision and Samson's act of calling on God. The site at Lehi is otherwise unidentified with certainty, though some proposed locations include sites in the Shephelah. The episode is theologically significant as one of the rare moments in the Samson cycle when the judge explicitly acknowledges his dependence on God, and the name memorializes both the prayer (the calling) and the miraculous answer.</p>",
        "sections": [],
        "hitchcock_meaning": "the fountain of him who called, or prayed",
        "source_ids": {
            "easton": "en-hakkore",
            "smith": "en-hakkore"
        },
        "key_refs": ["Judges 15:19"]
    },
    "en-rogel": {
        "id": "en-rogel",
        "term": "En-rogel",
        "category": "places",
        "intro": "<p>En-rogel, meaning <em>fountain of the fuller</em> or <em>the spy's fountain</em>, was a spring located just south of Jerusalem at the junction of the Kidron and Hinnom valleys, on the boundary between the territories of Judah and Benjamin. Its water source served the lower city and was prominent enough to serve as a boundary marker in the tribal land allotments.</p><p>En-rogel appears several times in the historical narratives: Jonathan and Ahimaaz positioned themselves there as intelligence couriers during Absalom's rebellion, receiving information from a servant girl and relaying it to David. Later it was the site where Adonijah held a feast and sacrificed oxen and fatlings when he attempted to seize the throne before Solomon's coronation—an act close enough to Jerusalem to be politically significant yet outside the immediate palace precincts. The spring was distinct from the Gihon spring, which lay to the north and was the source used for Solomon's anointing. Modern identification is with Bir Ayyub (Job's Well) at the confluence of the two valleys.</p>",
        "sections": [],
        "hitchcock_meaning": "the fuller's fountain",
        "source_ids": {
            "easton": "en-rogel",
            "smith": "en-rogel",
            "isbe": "en-rogel"
        },
        "key_refs": ["Joshua 15:7", "2 Samuel 17:17", "1 Kings 1:9"]
    },
    "en-shemesh": {
        "id": "en-shemesh",
        "term": "En-shemesh",
        "category": "places",
        "intro": "<p>En-shemesh, meaning <em>spring of the sun</em>, was a spring on the boundary between the territories of Judah and Benjamin, lying east of Jerusalem on the road toward Jericho. It served as a landmark point on the dividing line between the two tribes as described in the book of Joshua, lying between Adummim and the waters of En-rogel.</p><p>The site is identified with the modern Ain Haud (Spring of the Apostles), located about two miles east of Jerusalem on the Jericho road, just before the descent toward the Jordan valley begins. The name suggests the spring was oriented or visible such that it caught the morning sun, or that it lay in the direction of sunrise from Jerusalem. En-shemesh's role as a tribal boundary marker reflects the careful geographical precision of the Joshua land allotments, in which springs, ridgelines, and valleys served as the demarcation points between tribal inheritances.</p>",
        "sections": [],
        "hitchcock_meaning": "fountain of the sun",
        "source_ids": {
            "easton": "en-shemesh",
            "smith": "en-shemesh"
        },
        "key_refs": ["Joshua 15:7", "Joshua 18:17"]
    },
    "engedi": {
        "id": "engedi",
        "term": "En-gedi",
        "category": "places",
        "intro": "<p>En-gedi (<em>fountain of the kid</em>) was a celebrated oasis on the western shore of the Dead Sea, roughly midway along its length, known for its powerful spring that cascades down the cliff face to the desert below. The lush vegetation sustained by this spring in an otherwise barren desert made En-gedi remarkable: the Song of Solomon compares the beloved to a cluster of henna blossoms in the vineyards of En-gedi, and Ezekiel 47:10 uses it as one endpoint of the eschatological renewal of the Dead Sea region.</p><p>En-gedi served as a refuge for David during his flight from Saul, and it was there in one of the cave strongholds of the region that David spared Saul's life, cutting off only a piece of his robe when he could have killed him. The ancient site corresponds to Tell el-Jurn, above which the modern Kibbutz Ein Gedi operates. Its fresh water, warm springs, and subtropical micro-climate made it a uniquely fertile enclave, and its identification as an Amorite city of Hazazon-tamar in Genesis 14 connects it to the earliest historical stratum of Canaanite settlement in the region.</p>",
        "sections": [],
        "hitchcock_meaning": "fountain of the goat, or kid",
        "source_ids": {
            "easton": "engedi",
            "smith": "en-gedi",
            "isbe": "en-gedi"
        },
        "key_refs": ["1 Samuel 23:29", "1 Samuel 24:1", "Song of Solomon 1:14", "Ezekiel 47:10"]
    },
    "engraver": {
        "id": "engraver",
        "term": "Engraver",
        "category": "concepts",
        "intro": "<p>Engraving and the craftsmen who practiced it (Hebrew <em>ḥārash</em>, a general artisan term, and <em>pattîsh</em> for inscriber) played important roles in the production of sacred objects in ancient Israel. The stones of the high priest's ephod were engraved with the names of the twelve tribes, and the gold plate of the high priest's mitre was engraved with the inscription <em>HOLINESS TO THE LORD</em>. Bezalel, the chief craftsman of the tabernacle, was specifically endowed with skill in engraving stones and in carving wood for the sanctuary's appointed furnishings.</p><p>Engraving extended beyond sacred objects to personal seals, which were used to authenticate documents and authority. Signet rings bore engraved emblems or names, as did the seal stones of the high priest's breastplate, each engraved with a tribe's name <em>as a seal is engraved</em>. The metaphor of engraving on the heart (Jeremiah 17:1; Proverbs 3:3) employed this technical skill as an image of indelible inscription, contrasting the permanence of engraving with the transience of writing on perishable materials.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "engraver",
            "isbe": "arts-and-crafts"
        },
        "key_refs": ["Exodus 28:11", "Exodus 28:36", "Exodus 35:33", "Jeremiah 17:1"]
    },
    "enmity": {
        "id": "enmity",
        "term": "Enmity",
        "category": "concepts",
        "intro": "<p>Enmity in Scripture denotes deep, active hostility between parties. The Hebrew <em>ʾêbâ</em> and Greek <em>echthra</em> both convey a settled, structural opposition rather than mere temporary disagreement. The foundational instance is the enmity God placed between the serpent and the woman in Genesis 3:15—the protoevangelium—where the hostility between the seed of the serpent and the seed of the woman is established as a defining feature of all subsequent history, culminating in the crushing of the serpent's head by the woman's seed.</p><p>Paul employs the concept theologically in multiple ways in his epistles. The carnal mind is characterized as enmity against God, incapable of submission to his law (Romans 8:7). Christ's atoning work is described as abolishing the enmity between Jew and Gentile—the dividing wall of the law's ordinances—reconciling both into one body and making peace (Ephesians 2:15–16). The redemptive narrative thus moves from the declaration of enmity at the fall to its resolution in the cross, where Christ himself became the peace between estranged parties.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "enmity",
            "isbe": "enmity"
        },
        "key_refs": ["Genesis 3:15", "Romans 8:7", "Ephesians 2:15", "James 4:4"]
    },
    "enoch": {
        "id": "enoch",
        "term": "Enoch",
        "category": "people",
        "intro": "<p>The name Enoch (<em>ḥănôkh</em>, meaning <em>initiated</em> or <em>dedicated</em>) is shared by two notable figures in Genesis. The first was the son of Cain, after whom Cain named the first city he built. The second, far more significant, was the seventh-generation descendant of Adam through the line of Seth: the son of Jared and father of Methuselah. This Enoch stands unique in the antediluvian genealogy of Genesis 5 for a lifespan of only 365 years—brief compared to contemporaries—and for the remarkable note that <em>he walked with God, and he was not, for God took him.</em></p><p>This translation without death made Enoch a figure of intense interest in Second Temple Judaism, which developed extensive literature in his name (the books of Enoch) attributing to him heavenly visions, angelic revelations, and calendrical wisdom. The New Testament references him in the genealogy of Jesus in Luke 3 and in Hebrews 11 as a hero of faith who pleased God and was taken without tasting death. Jude quotes the Book of Enoch's prophecy attributed to him concerning divine judgment. Enoch's translation foreshadows the bodily ascension and serves in Christian theology as a type of the resurrection.</p>",
        "sections": [],
        "hitchcock_meaning": "dedicated; disciplined",
        "source_ids": {
            "easton": "enoch",
            "smith": "enoch",
            "isbe": "enoch"
        },
        "key_refs": ["Genesis 5:21", "Genesis 5:24", "Hebrews 11:5", "Jude 1:14"]
    },
    "enos": {
        "id": "enos",
        "term": "Enos",
        "category": "people",
        "intro": "<p>Enos (Hebrew <em>ʾĕnôsh</em>, meaning <em>man</em> or <em>mortal</em>) was the son of Seth and grandson of Adam, the third generation of humanity in the Sethite line. He is notable in Genesis 4:26 for being the generation in whose time <em>men began to call upon the name of the LORD</em>—a statement the biblical text presents as the beginning of formal, public worship. Whether this marks the inauguration of corporate prayer, liturgical invocation, or the designation of God by his personal name YHWH has been variously interpreted.</p><p>Enos lived 905 years according to the Masoretic text, fathering Cainan at age ninety. He appears in the genealogies of both Chronicles and Luke's gospel in the line from Adam to Jesus. Jewish tradition and rabbinic commentary sometimes read the Genesis 4:26 note as a transitional point distinguishing the period before public religion from the subsequent age of covenant worship, though the passage is susceptible to multiple interpretations depending on how one renders the Hebrew <em>hûḥal</em> (began, or was profaned).</p>",
        "sections": [],
        "hitchcock_meaning": "mortal man; sick; unhealthy",
        "source_ids": {
            "easton": "enos",
            "smith": "enos",
            "isbe": "enos"
        },
        "key_refs": ["Genesis 4:26", "Genesis 5:6", "1 Chronicles 1:1", "Luke 3:38"]
    },
    "ensign": {
        "id": "ensign",
        "term": "Ensign",
        "category": "concepts",
        "intro": "<p>An ensign in the biblical world was a visible signal or standard used to rally troops, mark tribal identity, or call nations to attention. The Hebrew terms <em>nēs</em> (standard, signal), <em>degel</em> (banner, standard), and <em>ʾôth</em> (sign) overlap in meaning and usage. Numbers 2 describes each of the four divisions of Israel's wilderness camp as having its own standard (<em>degel</em>), around which the designated tribes assembled—a military ordering of the covenant community.</p><p>The prophetic literature employs the ensign as a powerful metaphor. Isaiah 11:10 describes the root of Jesse standing as an ensign for the peoples, to which the Gentile nations would rally, and Isaiah 49:22 pictures God lifting a standard to summon the nations to carry Israel's exiles home. The lifting of an ensign on a mountain (Isaiah 13:2; 18:3) was a signal visible for long distances, serving as a communication technology for mustering armies or announcing judgment. In Christian interpretation the ensign of Jesse has been read as a prophecy of Christ as the gathering point for all nations.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "ensign",
            "isbe": "banner"
        },
        "key_refs": ["Numbers 2:2", "Isaiah 11:10", "Isaiah 13:2", "Isaiah 49:22"]
    },
    "entertain": {
        "id": "entertain",
        "term": "Entertain",
        "category": "concepts",
        "intro": "<p>Hospitality—the entertainment of guests and strangers—was a foundational social and religious obligation throughout the biblical world. The Hebrew and Greek conventions of hospitality (<em>ḥesed</em>-based generosity; Greek <em>philoxenia</em>, love of strangers) expected hosts to provide food, water, shelter, and protection to travelers and visitors. Abraham's lavish reception of the three visitors at Mamre (Genesis 18) became the paradigmatic hospitality narrative, interpreted by Hebrews 13:2 as an instance of entertaining angels unawares.</p><p>The Mosaic law consistently emphasized care for the alien and stranger, and the Proverbs tradition praised the generous host. Jesus's parables frequently feature banquet hosting as a metaphor for the kingdom of God. The New Testament exhortation to hospitality (<em>philoxenia</em>) in Romans 12:13 and Hebrews 13:2 roots the practice in the possibility of unrecognized divine encounter. The concept of entertaining connects the practical ethics of generosity with the theological reality that all provision comes from God, who entertains his own people at his table.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "entertain",
            "isbe": "hospitality"
        },
        "key_refs": ["Genesis 18:1", "Hebrews 13:2", "Romans 12:13", "1 Peter 4:9"]
    },
    "epaenetus": {
        "id": "epaenetus",
        "term": "Epaenetus",
        "category": "people",
        "intro": "<p>Epaenetus, whose Greek name means <em>praised</em>, holds the distinction of being identified by Paul in Romans 16:5 as <em>the firstfruits of Asia unto Christ</em>—that is, the first convert from the Roman province of Asia (western Asia Minor) to embrace the Christian faith. Paul greets him warmly as his beloved friend, indicating a relationship of personal affection and shared ministry.</p><p>Beyond this single verse, nothing further is known of Epaenetus. His designation as the firstfruits of Asia suggests he may have been among the earliest converts of Paul's Ephesian ministry or the mission in the province of Asia that preceded it. The term <em>firstfruits</em> carries both temporal priority and the theological weight of dedication to God—the firstfruits were holy, set apart for divine purpose. In Christian tradition Epaenetus has been counted among the seventy disciples sent out by Jesus, though this is a later ecclesiastical tradition without direct scriptural support.</p>",
        "sections": [],
        "hitchcock_meaning": "laudable; praised",
        "source_ids": {
            "easton": "epaenetus",
            "smith": "epaenetus",
            "isbe": "epaenetus"
        },
        "key_refs": ["Romans 16:5"]
    },
    "epaphras": {
        "id": "epaphras",
        "term": "Epaphras",
        "category": "people",
        "intro": "<p>Epaphras was the founder of the church at Colosse and its representative to Paul during his imprisonment. A native of Colosse (Colossians 4:12), he appears to have been converted through Paul's Ephesian ministry and then returned to his home city to preach the gospel, planting the congregation there. His name is a contraction of Epaphroditus, though most scholars regard him as distinct from the Epaphroditus of the Philippian letters.</p><p>Paul speaks of him in the highest terms: a beloved fellow servant, a faithful minister of Christ, and one who labored earnestly in prayer for the Colossians, Laodiceans, and Hieropolitans that they might stand mature and fully assured in the will of God (Colossians 4:12–13). In Philemon 23 Paul refers to him as a fellow prisoner, suggesting he shared Paul's captivity voluntarily or was himself detained. The church in Colosse likely depended on Epaphras's communication with Paul as the channel through which the Colossian letter was generated and its specific errors addressed.</p>",
        "sections": [],
        "hitchcock_meaning": "covered with foam",
        "source_ids": {
            "easton": "epaphras",
            "smith": "epaphras",
            "isbe": "epaphras"
        },
        "key_refs": ["Colossians 1:7", "Colossians 4:12", "Philemon 1:23"]
    },
    "epaphroditus": {
        "id": "epaphroditus",
        "term": "Epaphroditus",
        "category": "people",
        "intro": "<p>Epaphroditus was the emissary sent by the church at Philippi to deliver their financial gift to Paul in prison and to serve his needs. His name, meaning <em>charming</em> or <em>devoted to Aphrodite</em>, reflects his Gentile background, though he had become a devoted servant of Christ. Paul calls him brother, fellow worker, and fellow soldier—a triad of increasingly intense relationship—and honors him as the Philippians' messenger and minister to his need.</p><p>During his time with Paul, Epaphroditus fell gravely ill, to the point of near death, causing deep concern both to the apostle and to the Philippians when word reached them. God had mercy on him and restored his health, and Paul sent him back to Philippi with the letter, urging the church to receive him with joy and hold him in honor because he had risked his life in service to Christ. The episode illustrates the real dangers of travel and ministry in the first-century world, and Epaphroditus's self-sacrificing service is held up as an example of the Philippian partnership in the gospel.</p>",
        "sections": [],
        "hitchcock_meaning": "agreeableness; handsome; charming",
        "source_ids": {
            "easton": "epaphroditus",
            "smith": "epaphroditus",
            "isbe": "epaphroditus"
        },
        "key_refs": ["Philippians 2:25", "Philippians 2:27", "Philippians 4:18"]
    },
    "ephah": {
        "id": "ephah",
        "term": "Ephah",
        "category": "concepts",
        "intro": "<p>The ephah was the standard Hebrew unit of dry measure, equivalent to one-tenth of a homer and approximately equal to a bath in liquid measure. Estimates of its capacity vary among scholars, with figures ranging from roughly 3.5 to 8 gallons (approximately 13 to 30 liters), with most modern calculations settling around 5.8 gallons (22 liters). The ephah served as the basic unit for measuring grain, flour, and other dry commodities in commerce and cultic offerings.</p><p>The Law required that the ephah be just and true, with the dishonest use of an undersize ephah explicitly condemned in Leviticus 19:36, Deuteronomy 25:14, Proverbs 20:10, and the prophets Amos and Micah. Zechariah's vision of a woman seated in an ephah-basket represents wickedness being removed from the land and transported to Babylon—the ephah serving as a container large enough for symbolic narrative purposes. The grain offerings at the sanctuary were frequently measured in tenths of an ephah, making it a unit with both civic and sacrificial significance in Israelite life.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "ephah",
            "smith": "weights-and-measures",
            "isbe": "weights-and-measures"
        },
        "key_refs": ["Exodus 16:36", "Leviticus 19:36", "Zechariah 5:6", "Amos 8:5"]
    },
    "epher": {
        "id": "epher",
        "term": "Epher",
        "category": "people",
        "intro": "<p>Epher is a name borne by several distinct figures in the Old Testament. The most prominent was the second son of Midian, who was the son of Abraham by his concubine Keturah; through this genealogical placement, Epher became an ancestor of a Midianite tribal clan. His name, meaning <em>a calf</em> or <em>young deer</em>, follows a pattern of zoological names common in ancient Semitic genealogies.</p><p>A second Epher was a son of Ezra, listed in the genealogies of Judah in 1 Chronicles 4. A third was a chief man among the half-tribe of Manasseh east of Jordan in 1 Chronicles 5, one of those who were carried into exile by the Assyrian king Tiglath-pileser. The name's repetition across different tribal genealogies suggests it was a common Israelite personal name rather than a marker of any particular religious or historical significance. Each Epher appears only in genealogical lists without further narrative development.</p>",
        "sections": [],
        "hitchcock_meaning": "dust; lead; ashes",
        "source_ids": {
            "easton": "epher",
            "smith": "epher"
        },
        "key_refs": ["Genesis 25:4", "1 Chronicles 4:17", "1 Chronicles 5:24"]
    },
    "ephes-dammim": {
        "id": "ephes-dammim",
        "term": "Ephes-dammim",
        "category": "places",
        "intro": "<p>Ephes-dammim, meaning <em>boundary of blood</em> or <em>border of blood</em> (possibly referring to past battles or a notable reddish soil), was a place between Socoh and Azekah in the Shephelah of Judah where the Philistines camped before the battle of Elah. It was in the valley between the two armies there that Goliath issued his challenge to Israel, and where David killed him with a sling-stone.</p><p>In 1 Chronicles 11:13 the site is called Pas-dammim (also <em>Pasdammim</em>), where David's mighty men made a heroic stand among the lentil fields and struck down the Philistines—one of the great exploits of his warriors. The two names likely refer to the same location, with variant spellings reflecting different manuscript traditions or dialect variations. The site sat at a militarily sensitive junction controlling access between the Philistine coastal plain and the hill country of Judah, making it a recurring arena for the conflicts of the period.</p>",
        "sections": [],
        "hitchcock_meaning": "border of blood-drops",
        "source_ids": {
            "easton": "ephes-dammim",
            "smith": "ephes-dammim"
        },
        "key_refs": ["1 Samuel 17:1", "1 Chronicles 11:13"]
    },
    "ephesians-epistle-to-the": {
        "id": "ephesians-epistle-to-the",
        "term": "Ephesians, Epistle to the",
        "category": "concepts",
        "intro": "<p>The Epistle to the Ephesians is one of Paul's Prison Epistles, traditionally dated to his Roman imprisonment of approximately AD 60–62. The letter is structured in two halves: three chapters of dense theological exposition on the mystery of the church, the body of Christ, and God's eternal plan of redemption for both Jews and Gentiles; and three chapters of ethical application flowing from those doctrines into household codes and spiritual warfare. Its elevated style and cosmic scope have led some scholars to question direct Pauline authorship, while others maintain it as authentically Pauline, possibly a circular letter intended for multiple congregations.</p><p>The phrase <em>in Ephesus</em> (Ephesians 1:1) is absent from some early manuscripts, strengthening the circular letter hypothesis. The letter's theology of the church as Christ's body and the fullness of him who fills all in all, its teaching on election before the foundation of the world, and its vision of the cosmos being summed up in Christ have made Ephesians one of the most theologically rich and influential documents in the New Testament. Its concluding passage on the full armor of God (Ephesians 6:10–20) has become foundational for Christian teaching on spiritual warfare.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "ephesians-epistle-to-the",
            "smith": "ephesians-epistle-to-the",
            "isbe": "ephesians-epistle-to-the"
        },
        "key_refs": ["Ephesians 1:3", "Ephesians 2:8", "Ephesians 3:6", "Ephesians 6:10"]
    },
    "ephesus": {
        "id": "ephesus",
        "term": "Ephesus",
        "category": "places",
        "intro": "<p>Ephesus was one of the great cities of the ancient world, located on the western coast of Asia Minor (modern Turkey) at the mouth of the Cayster River, and served as the capital of the Roman province of Asia. A leading commercial, cultural, and religious center, it was home to the Temple of Artemis (Diana), one of the Seven Wonders of the ancient world. Its harbor made it a natural hub of Mediterranean trade, and its population of several hundred thousand made it among the largest cities in the eastern Roman Empire.</p><p>Paul spent approximately three years in Ephesus on his third missionary journey (Acts 19), his longest sustained ministry in any city, during which he taught daily in the school of Tyrannus and the gospel spread throughout the province. The silversmiths' riot over diminishing sales of Artemis shrines captures the economic and religious tensions his preaching provoked. Ephesus received one of the seven letters of Revelation, praised for its doctrinal vigilance but rebuked for having left its first love. The city was the base of John's later ministry, and tradition associates it with the Gospel of John and the Johannine Epistles.</p>",
        "sections": [],
        "hitchcock_meaning": "desirable",
        "source_ids": {
            "easton": "ephesus",
            "smith": "ephesus",
            "isbe": "ephesus"
        },
        "key_refs": ["Acts 19:1", "Acts 19:24", "1 Corinthians 15:32", "Revelation 2:1"]
    },
    "ephod": {
        "id": "ephod",
        "term": "Ephod",
        "category": "concepts",
        "intro": "<p>The ephod was one of the most significant vestments of the high priest, described in detail in Exodus 28 and 39. Made of fine twisted linen and woven with gold, blue, purple, and scarlet threads, it was essentially a short sleeveless garment fastened at the shoulders by two onyx stones, each engraved with six tribal names, which served as memorial stones before God. The breastplate of judgment, holding the Urim and Thummim, was attached to the ephod's front.</p><p>The ephod thus functioned as the central element of the high priestly oracular apparatus through which God's will was discerned for Israel. Several troubling uses of the term appear in Judges: Gideon made an ephod from war plunder that became an object of idolatrous worship, and the Danites stole a Levite-made ephod for their illegitimate sanctuary. A simpler linen ephod worn by ordinary priests and even by David when dancing before the ark appears to have been a different, less elaborate garment. The rich symbolic function of the high priest's ephod—bearing the names of Israel before God—foreshadows the intercessory role of Christ as great high priest.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "ephod",
            "smith": "ephod",
            "isbe": "ephod"
        },
        "key_refs": ["Exodus 28:6", "Exodus 28:30", "Judges 8:27", "1 Samuel 2:18"]
    },
    "ephphatha": {
        "id": "ephphatha",
        "term": "Ephphatha",
        "category": "concepts",
        "intro": "<p>Ephphatha is the Aramaic word, meaning <em>be opened</em>, spoken by Jesus when he healed a deaf man with a speech impediment in the region of the Decapolis (Mark 7:34). Jesus took the man aside privately, put his fingers into his ears and touched his tongue with spittle, looked up to heaven, sighed, and spoke the word. Immediately the man's hearing was restored and his speech impediment removed.</p><p>Mark, writing primarily for a Gentile audience, translates the term for his readers (as he does with other Aramaic words preserved in the tradition), suggesting that the actual Aramaic word was retained in the oral tradition as particularly significant—perhaps because the eyewitnesses remembered the exact utterance. The healing is notable for its intimate and deliberate method, contrasting with healings by mere word at a distance, and for the crowd's response of astonishment: <em>He has done all things well; he makes the deaf hear and the mute speak</em>—echoing Isaiah's description of messianic miracles. Ephphatha has been retained in some liturgical rites as an element of baptismal ceremonies, symbolizing the opening of ears to hear the gospel.</p>",
        "sections": [],
        "hitchcock_meaning": "be opened",
        "source_ids": {
            "easton": "ephphatha",
            "smith": "ephphatha",
            "isbe": "ephphatha"
        },
        "key_refs": ["Mark 7:34", "Isaiah 35:5"]
    },
    "ephraim": {
        "id": "ephraim",
        "term": "Ephraim",
        "category": "people",
        "intro": "<p>Ephraim was the younger of the two sons of Joseph and his Egyptian wife Asenath, born in Egypt during the years of plenty before the famine. His name, meaning <em>double fruitfulness</em>, expressed Joseph's gratitude that God had made him fruitful in the land of his affliction. When Jacob blessed Joseph's sons on his deathbed, he deliberately crossed his hands, placing his right hand on Ephraim the younger rather than Manasseh the elder, granting Ephraim the superior blessing despite Joseph's objection—a reversal that established a pattern consistent with divine election of the younger son throughout Genesis.</p><p>The tribe of Ephraim became the dominant tribe of the northern kingdom of Israel; indeed, the northern kingdom is frequently called Ephraim in the prophetic literature (Hosea, Isaiah, Jeremiah). The tribe's territory, centered in the central hill country with Shechem as a key city, was among the most productive in Canaan. Joshua himself was an Ephraimite, and the central sanctuary at Shiloh lay within Ephraim's boundaries. The prophets look toward a future reunion of Ephraim and Judah under a single Davidic king as part of the eschatological restoration of all Israel.</p>",
        "sections": [],
        "hitchcock_meaning": "fruitful; increasing",
        "source_ids": {
            "easton": "ephraim",
            "smith": "ephraim",
            "isbe": "ephraim"
        },
        "key_refs": ["Genesis 41:52", "Genesis 48:14", "Hosea 4:17", "Ezekiel 37:16"]
    },
    "ephraim-mount": {
        "id": "ephraim-mount",
        "term": "Ephraim, Mount",
        "category": "places",
        "intro": "<p>Mount Ephraim (Hebrew <em>har ʾephrāyim</em>) refers to the central hill country of Canaan occupied by the tribe of Ephraim, a highland region of approximately 50 by 35 miles in extent, situated between the valleys of Jezreel to the north and Aijalon to the south. The terrain is rugged, with elevations reaching over 3,000 feet, cut by valleys that drain both eastward to the Jordan and westward toward the coastal plain.</p><p>The region provided natural defensibility and was densely forested in antiquity, with productive soils in its many valleys. Joshua's allotment placed Ephraim in this central highland, and his own burial ground at Timnath-serah lay here. Shiloh, the first permanent home of the tabernacle, sat within this region. The term Mount Ephraim functions in the prophetic books as a synecdoche for the northern kingdom's heartland, and Jeremiah's promise of return includes the call for watchmen on the hills of Ephraim to announce the way back for the exiles (Jeremiah 31:6).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "ephraim-mount",
            "smith": "ephraim-mount",
            "isbe": "ephraim-mount-of"
        },
        "key_refs": ["Joshua 17:15", "Judges 4:5", "1 Samuel 1:1", "Jeremiah 31:6"]
    },
    "ephraim-gate-of": {
        "id": "ephraim-gate-of",
        "term": "Ephraim, Gate of",
        "category": "places",
        "intro": "<p>The Gate of Ephraim was one of the named gates in the northern wall of Jerusalem, mentioned in the Old Testament in connection with festivals and the repair of the city walls. Its name indicated that the gate opened toward the road leading north to the territory of Ephraim. The gate is referenced in 2 Kings 14:13, where Jehoash king of Israel broke down four hundred cubits of Jerusalem's wall from the Gate of Ephraim to the Corner Gate after his victory over Amaziah.</p><p>Nehemiah 8:16 records that the people built booths for the Feast of Tabernacles in the street of the Gate of Ephraim as part of the post-exilic revival under Ezra. The gate also appears in Nehemiah 12:39 in the description of the processional route taken by the two choirs at the dedication of the rebuilt wall. The precise location within the northern wall circuit of ancient Jerusalem has been debated by archaeologists, with estimates placing it in the vicinity of the Second Quarter or somewhere along the northern alignment of the city's defenses.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "ephraim-gate-of",
            "smith": "ephraim-gate-of"
        },
        "key_refs": ["2 Kings 14:13", "Nehemiah 8:16", "Nehemiah 12:39"]
    },
    "ephraim-wood-of": {
        "id": "ephraim-wood-of",
        "term": "Ephraim, Wood of",
        "category": "places",
        "intro": "<p>The Wood of Ephraim was the forested terrain in Transjordan where the decisive battle was fought between the forces of David and the army of Absalom during the civil war of Absalom's rebellion. Despite its name suggesting an Ephraimite connection—perhaps a forest named after an ancient settlement or battle involving Ephraim—the wood lay east of the Jordan in the territory of Gilead, in the vicinity of Mahanaim where David had established his temporary capital.</p><p>The battle in the wood of Ephraim was catastrophic for Absalom's forces: twenty thousand were slain, and the forest consumed more men than the sword, as soldiers fled into the dense woodland and were swallowed by it. It was there that Absalom's hair caught in the branches of an oak as his mule passed beneath, leaving him hanging helpless until Joab killed him against David's explicit orders. The wood thus became the unlikely instrument of the rebellion's end and the occasion of David's anguished lament for his son.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "ephraim-wood-of",
            "smith": "ephraim-wood-of"
        },
        "key_refs": ["2 Samuel 18:6", "2 Samuel 18:8", "2 Samuel 18:14"]
    },
    "ephraim-in-the-wilderness": {
        "id": "ephraim-in-the-wilderness",
        "term": "Ephraim in the Wilderness",
        "category": "places",
        "intro": "<p>Ephraim in the Wilderness (or Ephraim near the desert) is mentioned only in John 11:54 as the town to which Jesus withdrew with his disciples after the council of the chief priests and Pharisees determined to put him to death following the raising of Lazarus. He remained there until just before Passover, when he began his final journey to Jerusalem.</p><p>The site is generally identified with the ancient city of Ophrah in Benjamin, lying approximately fifteen miles northeast of Jerusalem on the edge of the Judean wilderness. It corresponds to the modern et-Taiyibeh, a village on a prominent hill overlooking the desert slopes toward Jericho and the Jordan valley. The name indicates its location near the barren wilderness, a liminal zone between the cultivated hill country and the arid Jordan rift. Jesus's retreat there represents a deliberate withdrawal from the dangerous political situation in Jerusalem while awaiting the appointed hour of his passion.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "ephraim-in-the-wilderness",
            "smith": "ephraim-in-the-wilderness",
            "isbe": "ephraim-4"
        },
        "key_refs": ["John 11:54"]
    },
    "ephratah": {
        "id": "ephratah",
        "term": "Ephratah",
        "category": "places",
        "intro": "<p>Ephratah (or Ephrathah) is an ancient name for Bethlehem, the significance of which is preserved in the double designation <em>Bethlehem Ephratah</em> in Micah 5:2. The name may mean <em>fruitfulness</em> or may derive from Ephrath, the wife of Caleb, after whom the region was named in the genealogies of Chronicles. Ruth 4:11 pairs it with Bethlehem as the place from which the clan of Boaz originated.</p><p>Micah's prophecy—<em>But you, Bethlehem Ephratah, though you are small among the clans of Judah, out of you will come for me one who will be ruler over Israel, whose origins are from of old, from ancient times</em>—became the key text cited by the scribes when Herod inquired where the Christ was to be born (Matthew 2:6). The double name Bethlehem Ephratah thus carries the weight of both Davidic origin (David was a Bethlehemite) and messianic expectation, and its very smallness in Micah's oracle underscores the paradox of divine election of the humble and overlooked.</p>",
        "sections": [],
        "hitchcock_meaning": "abundance; bearing fruit",
        "source_ids": {
            "easton": "ephratah",
            "smith": "ephratah",
            "isbe": "ephrathah"
        },
        "key_refs": ["Genesis 35:19", "Ruth 4:11", "Micah 5:2", "Matthew 2:6"]
    },
    "ephrathite": {
        "id": "ephrathite",
        "term": "Ephrathite",
        "category": "people",
        "intro": "<p>Ephrathite is a gentillic term used in the Old Testament in two distinct senses. In the books of Samuel and Judges it refers to a native of Ephrath (Bethlehem) in Judah: Jesse, David's father, is called an Ephrathite of Bethlehem in Judah (1 Samuel 17:12), and the family of Elimelech in Ruth similarly belongs to this Bethlehemite clan. The term thus connects the Davidic line explicitly to its Bethlehemite origins.</p><p>Separately, in 1 Samuel 1:1, Elkanah the father of Samuel is described as an Ephrathite of Ramathaim-zophim in Mount Ephraim, suggesting the term could also denote a member of an Ephraimite clan called Ephrathites—a sub-group of the tribe of Ephraim. A similar usage appears in Judges 12:5, where certain Gileadites distinguish themselves from Ephrathites in a confrontation at the Jordan ford. The ambiguity reflects the overlapping usage of eponymic tribal and geographic names in biblical Hebrew, where the same gentillic could derive from different ancestral or geographic referents.</p>",
        "sections": [],
        "hitchcock_meaning": "bearing fruit; growing; increasing",
        "source_ids": {
            "easton": "ephrathite",
            "smith": "ephrathite"
        },
        "key_refs": ["1 Samuel 17:12", "Ruth 1:2", "1 Kings 11:26"]
    },
    "ephron": {
        "id": "ephron",
        "term": "Ephron",
        "category": "people",
        "intro": "<p>Ephron son of Zohar was the Hittite from whom Abraham purchased the cave of Machpelah as a family burial ground after the death of Sarah. The transaction in Genesis 23 is one of the most fully narrated commercial negotiations in the Old Testament, conducted with formal deference at the city gate before witnesses. Ephron initially offered the field and cave as a gift, in keeping with Near Eastern courtesy conventions, but when Abraham insisted on paying the full price, Ephron named four hundred shekels of silver—a sum the text implies was high—which Abraham weighed out without objection.</p><p>The legal precision of the account—naming the field, the cave, all trees on the property, witnesses, and the measurement of silver—reflects the ancient conventions for validating a real estate transaction before community witnesses. The site of Machpelah, traditionally identified with the Haram el-Khalil in Hebron, became the burial place of Abraham, Sarah, Isaac, Rebekah, Leah, and Jacob. Ephron himself is a Hittite chieftain; his ready negotiation with Abraham reflects the kind of commercial interaction between patriarchs and Canaanite populations depicted throughout Genesis.</p>",
        "sections": [],
        "hitchcock_meaning": "dust; lead; ashes",
        "source_ids": {
            "easton": "ephron",
            "smith": "ephron",
            "isbe": "ephron"
        },
        "key_refs": ["Genesis 23:8", "Genesis 23:14", "Genesis 23:17", "Genesis 49:30"]
    },
    "epicureans": {
        "id": "epicureans",
        "term": "Epicureans",
        "category": "people",
        "intro": "<p>The Epicureans were followers of the Greek philosopher Epicurus (341–270 BC), who taught that the chief good was pleasure—specifically the calm, moderate pleasure of <em>ataraxia</em> (tranquility) achieved through friendship, philosophical study, and the avoidance of pain and anxiety. Epicurean philosophy denied divine providence and personal immortality, taught that the gods took no interest in human affairs, and held that death was simply the dissolution of the atoms composing the person, after which nothing remained.</p><p>Paul encountered both Epicureans and Stoics in Athens when they brought him to the Areopagus to hear his new teaching (Acts 17:18). The Epicureans likely found his preaching about resurrection particularly objectionable, since it contradicted their core conviction that death ended consciousness. Some scholars see the Areopagus speech as carefully engaging both schools: addressing Stoic cosmic theology and the Epicurean concern with the nature of the divine. The Epicureans' dismissal of Paul as a <em>babbler</em> (literally a seed-picker, one who picks up fragments of ideas) reflects philosophical condescension rather than genuine engagement with his message.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "epicureans",
            "smith": "epicureans",
            "isbe": "epicureans"
        },
        "key_refs": ["Acts 17:18", "Acts 17:32"]
    },
    "elon": {
        "id": "elon",
        "term": "Elon",
        "category": "people",
        "intro": "<p>Elon (Hebrew <em>ʾêlôn</em>, meaning <em>oak</em> or <em>strong</em>) is shared by several figures in the Old Testament. The most notable was Elon the Zebulunite, who judged Israel for ten years before dying and being buried at Aijalon in Zebulun. He is one of the so-called minor judges, described with minimal narrative detail in Judges 12:11–12, standing between the figures of Ibzan and Abdon in the list. His judgeship represents a period of relative stability in the tribal confederation.</p><p>Other bearers of the name include: a son of Zebulun and ancestor of the Elonite clan (Genesis 46:14; Numbers 26:26); a Hittite whose daughter Adah was one of Esau's wives (Genesis 26:34); and Elon-beth-hanan, a town in the second administrative district of Solomon's kingdom (1 Kings 4:9). The multiple instances of the name reflect its common usage as a personal name derived from the widespread oak tree, a natural landmark and symbol of strength in the landscape of ancient Palestine.</p>",
        "sections": [],
        "hitchcock_meaning": "oak; strong; body of the sun",
        "source_ids": {
            "easton": "elon",
            "smith": "elon",
            "isbe": "elon"
        },
        "key_refs": ["Judges 12:11", "Genesis 46:14", "Genesis 26:34"]
    },
    "eltekeh": {
        "id": "eltekeh",
        "term": "Eltekeh",
        "category": "places",
        "intro": "<p>Eltekeh was a Levitical city in the territory of Dan, assigned to the Kohathite clan of Levites according to Joshua 21:23. It lay in the Shephelah or foothills region west of Judah's highland core. The site's identification is uncertain; proposals have included Khirbet el-Muqanna (Tell Miqne, more commonly identified with Ekron) and other sites in the western plain between the coastal settlements and the hill country.</p><p>The area around Eltekeh became strategically significant in 701 BC when Sennacherib king of Assyria defeated an Egyptian and Ethiopian coalition near the city in the same campaign that culminated in the siege of Jerusalem under Hezekiah. The Assyrian annals record a battle at Eltekeh as part of the western campaign, one of the rare points where Assyrian and biblical chronology can be directly correlated. The city's Levitical designation and its proximity to Philistine territory made it a border community between the Israelite and Philistine cultural zones during the monarchic period.</p>",
        "sections": [],
        "hitchcock_meaning": "your fear of God",
        "source_ids": {
            "easton": "eltekeh",
            "smith": "eltekeh"
        },
        "key_refs": ["Joshua 19:44", "Joshua 21:23"]
    },
    "elul": {
        "id": "elul",
        "term": "Elul",
        "category": "concepts",
        "intro": "<p>Elul was the sixth month of the Hebrew sacred calendar, corresponding to the end of summer in the Julian calendar (roughly August–September). The name likely derives from a Babylonian or Akkadian root, reflecting the influence of Mesopotamian calendar terminology adopted during or after the Babylonian exile. It appears only once in the canonical Old Testament by name, in Nehemiah 6:15, where the rebuilding of Jerusalem's walls is said to have been completed on the twenty-fifth of Elul, in fifty-two days.</p><p>In the Jewish religious calendar, Elul held special significance as the month of preparation preceding the High Holy Days of Tishri: Rosh Hashanah (New Year) and Yom Kippur (Day of Atonement). Rabbinic tradition developed an elaborate penitential spirituality for Elul, with the sounding of the shofar daily throughout the month as a call to self-examination and return to God. The agricultural character of the month was marked by the grape harvest and the completion of summer grain threshing, making it a time of both agricultural abundance and spiritual preparation.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "elul",
            "isbe": "elul"
        },
        "key_refs": ["Nehemiah 6:15"]
    },
    "erastus": {
        "id": "erastus",
        "term": "Erastus",
        "category": "people",
        "intro": "<p>Erastus appears three times in the New Testament in what may represent two or three distinct individuals. Acts 19:22 mentions an Erastus whom Paul sent ahead from Ephesus to Macedonia along with Timothy. Romans 16:23 greets an Erastus who is identified as the city treasurer (Greek <em>oikonomos</em>) of Corinth—a significant civic office that places this Erastus among the more socially prominent members of the Corinthian church. 2 Timothy 4:20 notes that Erastus stayed behind at Corinth.</p><p>The Corinthian Erastus has attracted considerable archaeological interest. A first-century Latin inscription discovered in Corinth reads: <em>Erastus, in return for his aedileship, laid this pavement at his own expense</em>—an inscription that some scholars identify with the biblical figure, though the civic titles <em>aedile</em> and <em>oikonomos</em> (treasurer) may not be identical. If the identification is correct, Erastus represents one of the most socially elevated Christians mentioned by name in Paul's letters, an example of the gospel reaching the upper strata of Roman colonial society.</p>",
        "sections": [],
        "hitchcock_meaning": "lovely; amiable",
        "source_ids": {
            "easton": "erastus",
            "smith": "erastus",
            "isbe": "erastus"
        },
        "key_refs": ["Acts 19:22", "Romans 16:23", "2 Timothy 4:20"]
    },
    "esarhaddon": {
        "id": "esarhaddon",
        "term": "Esarhaddon",
        "category": "people",
        "intro": "<p>Esarhaddon (Assyrian <em>Ashshur-ahu-iddina</em>, <em>Assur has given a brother</em>) was king of Assyria from 681 to 669 BC, the son and successor of Sennacherib. After Sennacherib was murdered by his sons Adrammelech and Sharezer (2 Kings 19:37; Isaiah 37:38), Esarhaddon defeated his brothers in civil war and secured the throne. He proved to be one of Assyria's most capable administrators and military commanders.</p><p>His most celebrated achievement was the conquest and rebuilding of Babylon, which his father had destroyed, a policy reversal that enhanced his prestige with Babylonian religious and civic elites. He also led two campaigns into Egypt, finally conquering Memphis in 671 BC and installing Assyrian governors over Lower Egypt—the apex of Assyrian imperial reach. In the biblical record, Esarhaddon is mentioned in Ezra 4:2 as the king who brought colonists to resettle Samaria after the Assyrian deportation, a policy consistent with his practice of population transfers to pacify conquered territories. He is also mentioned in 2 Kings 19:37 as the successor of Sennacherib.</p>",
        "sections": [],
        "hitchcock_meaning": "I will make black the point or ridges",
        "source_ids": {
            "easton": "esarhaddon",
            "smith": "esarhaddon",
            "isbe": "esarhaddon"
        },
        "key_refs": ["2 Kings 19:37", "Ezra 4:2", "Isaiah 37:38"]
    },
    "esau": {
        "id": "esau",
        "term": "Esau",
        "category": "people",
        "intro": "<p>Esau was the elder twin son of Isaac and Rebekah, born red and hairy, and the ancestor of the Edomite people. His name, possibly meaning <em>hairy</em> or connected to the word for <em>done/made</em>, is linked in the narrative to his rugged, outdoorsy character as a hunter favored by his father for the venison he brought home. The defining episodes of his life—selling his birthright for a bowl of red stew and losing his father's blessing to the deception of his mother and brother Jacob—set the course of subsequent Israelite and Edomite history.</p><p>Esau's Edomite descendants occupied the region south of the Dead Sea (Mount Seir), and the prophets repeatedly use Edom as a symbol of the nations hostile to Israel. Yet the reunion of Esau and Jacob in Genesis 33 presents Esau receiving his returning brother with unexpected graciousness. Paul cites the divine election of Jacob over Esau before birth as a paradigm of sovereign grace: <em>Jacob I have loved, but Esau I have hated</em>—not a statement of divine hatred but of covenant selection (Romans 9:13, citing Malachi 1:2–3). Hebrews 12:16 warns against being a profane person like Esau, who sold his birthright for a single meal.</p>",
        "sections": [],
        "hitchcock_meaning": "he that acts or finishes; who operates",
        "source_ids": {
            "easton": "esau",
            "smith": "esau",
            "isbe": "esau"
        },
        "key_refs": ["Genesis 25:25", "Genesis 25:33", "Genesis 33:4", "Romans 9:13"]
    },
    "esaias": {
        "id": "esaias",
        "term": "Esaias",
        "category": "people",
        "intro": "<p>Esaias is the Greek form of the Hebrew name Isaiah, used consistently in the Septuagint and carried over into the New Testament. The name means <em>the LORD is salvation</em> or <em>Yah saves</em>, encapsulating the prophetic ministry of its bearer. Isaiah son of Amoz prophesied in Jerusalem during the reigns of Uzziah, Jotham, Ahaz, and Hezekiah, spanning roughly the latter half of the eighth century BC.</p><p>The New Testament cites Isaiah (Esaias) more frequently than any other Old Testament prophet, with particularly heavy use in the Gospel of John, Paul's letter to the Romans, and the synoptic Gospels' infancy and passion narratives. Matthew 3:3 opens John the Baptist's ministry with a quotation from Isaiah 40; Matthew 12:17–21 applies the servant song of Isaiah 42 to Jesus's healing ministry; and John 12:38–41 uses Isaiah 53 and 6 in tandem. The christological density of Isaiah's prophecy—Immanuel, the suffering servant, the year of the LORD's favor—made it the foundational prophetic source for New Testament theology of Jesus as the fulfillment of Israel's messianic hope.</p>",
        "sections": [],
        "hitchcock_meaning": "the salvation of the Lord",
        "source_ids": {
            "easton": "esaias",
            "smith": "isaiah",
            "isbe": "isaiah-the-prophet"
        },
        "key_refs": ["Matthew 3:3", "Matthew 12:17", "John 12:38", "Romans 10:16"]
    },
    "eshbaal": {
        "id": "eshbaal",
        "term": "Eshbaal",
        "category": "people",
        "intro": "<p>Eshbaal was the fourth son of King Saul, listed in 1 Chronicles 8:33 and 9:39 under his original name, which means <em>man of Baal</em> or <em>Baal exists</em>. The same individual is referred to throughout 2 Samuel as Ish-bosheth (<em>man of shame</em>), a scribal substitution of the derogatory term <em>bosheth</em> (shame) for the theophoric element <em>Baal</em>—a pious alteration to avoid preserving the name of the Canaanite deity in connection with Israel's first royal family.</p><p>After Saul's death at Jezreel, Abner son of Ner took Ish-bosheth and made him king over Israel in Mahanaim, where he reigned two years in opposition to David's rule over Judah. His reign was weak from the start: Abner was the real power, and when Abner defected to David following a dispute over Saul's concubine Rizpah, Ish-bosheth's position became untenable. He was subsequently assassinated in his bed by two of his own officers, Baanah and Rechab, who hoped to gain David's favor—but David executed them for their crime. His death cleared the way for the elders of Israel to anoint David king over all Israel.</p>",
        "sections": [],
        "hitchcock_meaning": "in the idol's fire; a man of shame",
        "source_ids": {
            "easton": "eshbaal",
            "smith": "ish-bosheth",
            "isbe": "ish-bosheth"
        },
        "key_refs": ["1 Chronicles 8:33", "2 Samuel 2:8", "2 Samuel 4:5", "2 Samuel 4:12"]
    },
    "eschew": {
        "id": "eschew",
        "term": "Eschew",
        "category": "concepts",
        "intro": "<p>Eschew is an archaic English verb meaning to shun, avoid, or keep away from, used in the King James Version and other early English translations to render Hebrew and Greek terms of avoidance, turning aside, and departure from evil. In Psalm 34:14 and 1 Peter 3:11, the same Greek exhortation (<em>ekklino apo kakou</em>, depart from evil) is translated using this word, creating a direct New Testament echo of a wisdom Psalm.</p><p>The concept of eschewal belongs to the biblical ethics of separation: the righteous person is characterized not only by what they pursue (peace, good) but by what they actively avoid (evil). Job 1:1, 1:8, and 2:3 describe Job as a man who <em>feared God and eschewed evil</em>, making it part of the fullest description of an upright human life in the entire book. The verb's presence in the KJV reflects the ethical seriousness with which the translation rendered the Hebrew and Greek vocabulary of moral avoidance, emphasizing that holiness requires both positive pursuit and deliberate rejection of what is contrary to God's character.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {
            "easton": "eschew",
            "isbe": "eschew"
        },
        "key_refs": ["Job 1:1", "Psalm 34:14", "1 Peter 3:11"]
    },
    "eshcol": {
        "id": "eshcol",
        "term": "Eshcol",
        "category": "people",
        "intro": "<p>Eshcol (<em>cluster of grapes</em>) is the name of both an Amorite chieftain and the valley associated with him near Hebron. Eshcol was the brother of Mamre and Aner, all three of whom were confederates of Abraham and joined him in the pursuit of the four kings who had captured Lot (Genesis 14:13, 24). He represents the kind of local alliances Abraham maintained in Canaan, receiving a share of the spoils after the rescue.</p><p>The valley of Eshcol became more famous through its association with the twelve spies sent by Moses to survey Canaan. From the valley near Hebron they cut a single cluster of grapes so enormous that it required two men to carry it on a pole—along with pomegranates and figs—as tangible proof of the land's extraordinary fertility (Numbers 13:23–24). The valley's name, taken from the chieftain or named for the cluster the spies found there, became a symbol of Canaan's abundance. The grapes of Eshcol reappear in Deuteronomy 1:24 as Moses recalls that fruitful evidence and the failure of faith that prevented the first generation from entering.</p>",
        "sections": [],
        "hitchcock_meaning": "a bunch of grapes",
        "source_ids": {
            "easton": "eshcol",
            "smith": "eshcol",
            "isbe": "eshcol"
        },
        "key_refs": ["Genesis 14:13", "Numbers 13:23", "Deuteronomy 1:24"]
    },
    "esdraelon": {
        "id": "esdraelon",
        "term": "Esdraelon",
        "category": "places",
        "intro": "<p>Esdraelon (Greek form of the Hebrew Jezreel) is the great triangular plain stretching across the heart of northern Canaan between the Carmel range to the northwest, the hills of Galilee to the north, and the hills of Samaria to the southeast. Bounded by the rivers Kishon and Jalud, the plain measures roughly twenty miles from north to south and fifteen miles across at its widest point, and its fertile volcanic soil made it among the most productive agricultural land in all of ancient Palestine.</p><p>The strategic importance of Esdraelon derives from its position as the main corridor between the coastal highway and the Transjordanian routes, making it the battlefield of Israel's history: here Deborah and Barak routed Sisera's chariot army; here Gideon defeated the Midianites; here Saul fell at the hands of the Philistines on Mount Gilboa; here Josiah died opposing Pharaoh Necho at Megiddo. The plain was so associated with decisive conflict that Revelation 16:16 uses the Hebrew form Armageddon (Hill of Megiddo, overlooking the plain) for the site of the final eschatological battle.</p>",
        "sections": [],
        "hitchcock_meaning": "region of God",
        "source_ids": {
            "easton": "esdraelon",
            "smith": "esdraelon",
            "isbe": "esdraelon"
        },
        "key_refs": ["Judges 4:13", "1 Samuel 31:1", "2 Kings 23:29", "Revelation 16:16"]
    },
    "esek": {
        "id": "esek",
        "term": "Esek",
        "category": "places",
        "intro": "<p>Esek, meaning <em>contention</em> or <em>strife</em>, was the name Isaac gave to the first of two wells dug by his servants in the valley of Gerar after the death of Abraham. The Philistines of Gerar disputed ownership of the well, claiming its waters as their own, prompting Isaac's servants to name it Esek as a memorial of the quarrel. This episode belongs to the cycle of well-disputes in the patriarchal narratives that reflect the constant tension over water rights in the arid Negev region.</p><p>The narrative of Isaac's well-digging in Genesis 26 deliberately echoes Abraham's earlier experiences with Abimelech and the Philistines (Genesis 21), establishing Isaac as the legitimate heir of his father's covenant relationship with both God and the surrounding peoples. Each disputed well—Esek, Sitnah (the second), and finally Rehoboth (<em>broad places</em>, where there was at last no quarrel)—represents a stage in Isaac's patient persistence until God made room for him. The episode culminates in the covenant at Beersheba, establishing peaceful relations with the Philistine king.</p>",
        "sections": [],
        "hitchcock_meaning": "contention; strife",
        "source_ids": {
            "easton": "esek",
            "smith": "esek"
        },
        "key_refs": ["Genesis 26:20"]
    },
    "eshtaol": {
        "id": "eshtaol",
        "term": "Eshtaol",
        "category": "places",
        "intro": "<p>Eshtaol was a town in the Shephelah on the border between the territories of Judah and Dan, mentioned frequently in the Samson narratives. Listed in Joshua 15:33 among the towns of Judah in the lowland, it also appears in Joshua 19:41 among the towns of Dan, reflecting the ambiguity of tribal boundaries in the western foothills. Eshtaol is consistently paired with Zorah, a neighboring town a mile or two to the east, in references to the Danite tribal territory.</p><p>Samson was born near Zorah, and the Spirit of the LORD first moved upon him between Zorah and Eshtaol—a geographical detail suggesting the locale was associated with divine presence or a sacred encampment. After Samson's death at Gaza, his body was brought back and buried in the tomb of his father Manoah between Zorah and Eshtaol (Judges 16:31). The 600 Danites who scouted and then seized Laish (Judges 18) departed from Zorah and Eshtaol, making this district the staging point for the Danite migration northward. Modern identification is with Eshwa, east of Beth-shemesh.</p>",
        "sections": [],
        "hitchcock_meaning": "a strong woman",
        "source_ids": {
            "easton": "eshtaol",
            "smith": "eshtaol",
            "isbe": "eshtaol"
        },
        "key_refs": ["Joshua 15:33", "Judges 13:25", "Judges 16:31", "Judges 18:2"]
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
    print(f'BP e2: Elisabeth → Eshtaol: wrote {written}, skipped {skipped} existing.')


if __name__ == '__main__':
    main()
