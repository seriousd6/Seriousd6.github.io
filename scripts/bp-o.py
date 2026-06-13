#!/usr/bin/env python3
"""BP O: Oak → Ozni (63 Easton entries)"""
import json, os

OUT_DIR = 'data/biblepedia/articles'
os.makedirs(OUT_DIR, exist_ok=True)

def load_article(slug):
    fp = os.path.join(OUT_DIR, f'{slug}.json')
    if os.path.exists(fp):
        with open(fp) as f:
            return json.load(f)
    return None

def save_article(slug, data):
    fp = os.path.join(OUT_DIR, f'{slug}.json')
    with open(fp, 'w') as f:
        json.dump(data, f, indent=2)

def merge_article(slug, data):
    if load_article(slug) is not None:
        return False
    save_article(slug, data)
    return True

ARTICLES = {
    "oak": {
        "id": "oak",
        "term": "Oak",
        "category": "concepts",
        "intro": "<p>The oak was one of the most prominent trees of ancient Palestine and appears frequently in the biblical narrative as a landmark, a place of burial, and a site of sacred significance. Several Hebrew words are rendered <em>oak</em> in English translations — <em>allon</em>, <em>elon</em>, and <em>elah</em> — reflecting the multiple species of oak that grow in the region, including the Valonia oak (<em>Quercus aegilops</em>) and the Palestine oak (<em>Quercus infectoria</em>). The great oaks of Bashan were proverbial for their strength (Isaiah 2:13; Ezekiel 27:6).</p><p>Oaks served as landmarks and burial sites: Deborah, Rebekah's nurse, was buried under an oak at Bethel (Genesis 35:8), and Absalom's hair caught in an oak during the battle in the forest of Ephraim, where Joab killed him (2 Samuel 18:9–10). Isaiah uses the oak as a symbol of idolatrous practice — Israel cutting oaks for idol-making while God's holy seed endures as the stump after the tree is cut down (Isaiah 6:13; 57:5).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "oak", "isbe": "oak"},
        "key_refs": ["Genesis 14:6", "Isaiah 2:13", "Isaiah 6:13", "Genesis 35:8"]
    },
    "oath": {
        "id": "oath",
        "term": "Oath",
        "category": "concepts",
        "intro": "<p>An oath in the biblical world was a solemn affirmation or promise, invoking God as witness and guarantor and calling down divine punishment for perjury. The Hebrew word <em>shevuah</em> is related to the word <em>seven</em> — possibly because ancient oaths were sealed by seven sacrificial animals or sevenfold repetition. Oaths were used to ratify covenants (Genesis 26:31), confirm testimony (Exodus 22:11), bind vows (Numbers 30), and establish legal agreements. The phrase <em>as the LORD lives</em> was a standard oath formula invoking divine witness.</p><p>The Mosaic law regulated oaths strictly: swearing falsely profaned God's name and was a form of bearing it in vain (Leviticus 19:12). Deuteronomy 6:13 commands swearing only by the LORD's name. God himself swore oaths by his own name (Genesis 22:16; Hebrews 6:13–17) to give unbreakable assurance of his promises. Jesus taught his disciples to let their yes be yes and no be no, avoiding oaths entirely (Matthew 5:33–37), while affirming the validity of an oath under judicial examination when he responded to the high priest's adjuration (Matthew 26:63–64).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "oath", "isbe": "oath"},
        "key_refs": ["Deuteronomy 6:13", "Hebrews 6:13", "Matthew 5:34", "Leviticus 19:12"]
    },
    "obadiah": {
        "id": "obadiah",
        "term": "Obadiah",
        "category": "people",
        "intro": "<p>Obadiah (meaning <em>servant of the LORD</em>) was a common Israelite name borne by at least thirteen individuals in the Old Testament. The most important was Obadiah the steward of Ahab's palace, who <em>feared the LORD greatly</em> and secretly sheltered one hundred prophets from Jezebel's persecution, hiding them in two caves and feeding them (1 Kings 18:3–4). His encounter with Elijah, when Elijah commanded him to announce his presence to Ahab, reveals a man caught between conflicting loyalties — loyal to God yet dependent on the wicked king for his position.</p><p>Other notable bearers of the name include Obadiah the prophet, who is treated in the entry on the Book of Obadiah; various Levites who assisted in the religious reforms of Hezekiah and Josiah; a Gadite warrior who joined David at Ziklag (1 Chronicles 12:9); and a post-exilic leader under Nehemiah. The frequency of the name reflects the deep Israelite tradition of servant-of-God naming.</p>",
        "sections": [],
        "hitchcock_meaning": "servant of the Lord",
        "source_ids": {"easton": "obadiah", "smith": "obadiah", "isbe": "obadiah"},
        "key_refs": ["1 Kings 18:3", "1 Kings 18:13", "1 Chronicles 12:9"]
    },
    "obadiah-book-of": {
        "id": "obadiah-book-of",
        "term": "Obadiah, Book of",
        "category": "concepts",
        "intro": "<p>The Book of Obadiah is the shortest book in the Old Testament — a single chapter of 21 verses — a prophecy against Edom, the nation descended from Esau, Jacob's brother. The prophet Obadiah is otherwise unknown; his book is undated, though many scholars place it shortly after the Babylonian destruction of Jerusalem in 586 BC, when Edomites aided or gloated over the conquest of their Israelite kinsmen. Obadiah 1:11–14 accuses Edom of standing aloof, rejoicing at Jerusalem's fall, and cutting off its fugitives.</p><p>The book's central theme is divine retribution against Edom's pride: <em>The pride of your heart has deceived you, you who live in the clefts of the rock... Though you soar aloft like the eagle, though your nest is set among the stars, from there I will bring you down, says the LORD</em> (verses 3–4). It closes with a vision of the restoration of Israel's fortunes and the declaration that <em>the kingdom shall be the LORD's</em> (verse 21). Paul may echo Obadiah's theme in Romans 9:13 (<em>Jacob I loved, but Esau I hated</em>), a quotation from Malachi that encapsulates the same Esau/Edom tradition.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "obadiah-book-of", "isbe": "obadiah-book-of"},
        "key_refs": ["Obadiah 1:3", "Obadiah 1:11", "Obadiah 1:21"]
    },
    "obal": {
        "id": "obal",
        "term": "Obal",
        "category": "people",
        "intro": "<p>Obal (meaning <em>inconvenience of old age</em> or <em>stripped bare</em>) was a son of Joktan and a descendant of Shem in the Table of Nations (Genesis 10:28). He is likely the same as Ebal in the parallel list of 1 Chronicles 1:22, the difference reflecting variant spellings in manuscript transmission. As a Joktanite, Obal was an ancestor of one of the Arabian peoples of ancient south Arabia. His name may correspond to a toponym in the Arabian peninsula, though no certain identification has been established.</p>",
        "sections": [],
        "hitchcock_meaning": "inconvenience of old age",
        "source_ids": {"easton": "obal"},
        "key_refs": ["Genesis 10:28"]
    },
    "obed": {
        "id": "obed",
        "term": "Obed",
        "category": "people",
        "intro": "<p>Obed (meaning <em>a servant</em> or <em>worshipper</em>) was the son of Boaz and Ruth the Moabitess, and the grandfather of King David (Ruth 4:21–22; Matthew 1:5). His birth was celebrated by the women of Bethlehem as a gift of God to Naomi in her old age — they declared that Naomi had a son and gave him the name Obed (Ruth 4:17). Through Obed the story of Ruth's faithfulness and Boaz's redemption found its providential outcome: the Davidic and, ultimately, messianic lineage.</p><p>Several other figures bear the name Obed in the Old Testament: a mighty man in David's army (1 Chronicles 11:47), a gatekeeper descended from Obed-edom (1 Chronicles 26:7), and an ancestor of Azariah the reforming prophet (2 Chronicles 23:1). Luke's genealogy of Jesus includes an Obed in the line from Judah to David (Luke 3:32).</p>",
        "sections": [],
        "hitchcock_meaning": "a servant; workman",
        "source_ids": {"easton": "obed", "smith": "obed"},
        "key_refs": ["Ruth 4:21", "Ruth 4:22", "Matthew 1:5"]
    },
    "obed-edom": {
        "id": "obed-edom",
        "term": "Obed-Edom",
        "category": "people",
        "intro": "<p>Obed-edom (meaning <em>servant of Edom</em>) was a Gittite — a man from Gath — in whose house the ark of the covenant rested for three months after the death of Uzzah had halted its transfer to Jerusalem. During those three months the LORD blessed the household of Obed-edom and everything he had (2 Samuel 6:11; 1 Chronicles 13:14), a fact that prompted David to resume the ark's transfer. The blessing on Obed-edom's household became a sign of the ark's potency and, by implication, the cost of approaching it wrongly (as Uzzah had) versus hosting it with reverence.</p><p>A Levite named Obed-edom son of Jeduthun was appointed as a doorkeeper of the ark (1 Chronicles 15:18, 24) and later as a musician and gatekeeper of the temple treasuries (1 Chronicles 26:4–8). His descendants, a numerous family of porters, occupied a prominent place in the temple's administrative structure.</p>",
        "sections": [],
        "hitchcock_meaning": "servant of Edom",
        "source_ids": {"easton": "obed-edom", "smith": "obed-edom"},
        "key_refs": ["2 Samuel 6:11", "1 Chronicles 13:14", "1 Chronicles 26:4"]
    },
    "obeisance": {
        "id": "obeisance",
        "term": "Obeisance",
        "category": "concepts",
        "intro": "<p>Obeisance refers to a deep bow or prostration performed as a sign of respect, submission, or worship. In the biblical world it was the customary gesture of respect before a king, a patriarch, or anyone of higher social standing — bowing to the ground with the face touching the earth. The Hebrew verb <em>shachah</em> covers both reverential bowing before humans and the act of worship before God, reflecting the ancient world's continuity between social and sacred hierarchies.</p><p>Joseph's brothers performed obeisance before him in Egypt (Genesis 42:6; 43:28), fulfilling Joseph's earlier dreams of sheaves and stars bowing to him. The verb's use for worship of God and idols alike underlies the first and second commandments' prohibition of serving other gods: <em>you shall not bow down to them or serve them</em> (Exodus 20:5). In the New Testament, the Magi worshipped (proskuneō) the infant Jesus, the same gesture rendered obeisance in OT contexts.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "obeisance"},
        "key_refs": ["Genesis 42:6", "Exodus 20:5"]
    },
    "obil": {
        "id": "obil",
        "term": "Obil",
        "category": "people",
        "intro": "<p>Obil (meaning <em>that weeps</em> or <em>who deserves to be bewailed</em>) was an Ishmaelite who served as the official in charge of King David's camels (1 Chronicles 27:30). He appears in the list of David's administrative officials overseeing the royal herds and flocks. The fact that a foreigner — an Ishmaelite — managed this important asset of the royal economy reflects the cosmopolitan character of David's court, which drew skilled specialists from multiple ethnic backgrounds for administrative roles.</p>",
        "sections": [],
        "hitchcock_meaning": "that weeps; who deserves to be bewailed",
        "source_ids": {"easton": "obil"},
        "key_refs": ["1 Chronicles 27:30"]
    },
    "oboth": {
        "id": "oboth",
        "term": "Oboth",
        "category": "places",
        "intro": "<p>Oboth (meaning <em>bottles</em>, <em>waterskins</em>, or <em>fathers</em>) was a wilderness campsite of the Israelites during the Exodus journey, recorded in Numbers 21:10–11 and in the summary itinerary of Numbers 33:43–44. Israel camped there after defeating the Amorite king Sihon and before encamping at Iye-abarim on the boundary of Moab. The exact location in the Arabah east of Edom is uncertain, though some scholars place it near modern Ain el-Weiba. Oboth represents one of the many transient stops in the long wilderness march east of the Rift Valley.</p>",
        "sections": [],
        "hitchcock_meaning": "dragons; fathers; desires",
        "source_ids": {"easton": "oboth"},
        "key_refs": ["Numbers 21:10", "Numbers 33:43"]
    },
    "oded": {
        "id": "oded",
        "term": "Oded",
        "category": "people",
        "intro": "<p>Oded was the name of two figures in the Old Testament. The first was the father of the prophet Azariah, who went out to meet King Asa of Judah after his victory over Zerah the Ethiopian and encouraged him to reform (2 Chronicles 15:1–8). The second and more remarkable Oded was a prophet of the LORD in Samaria who intervened when the army of the northern kingdom brought 200,000 captives from Judah to Samaria after a victory under King Pekah. Oded confronted the soldiers at the city gate, declaring that God's wrath had permitted the victory but that they had gone beyond divine mandate in enslaving their kinsmen — and that they too stood guilty before God. His bold intervention, supported by four leading men of Ephraim, succeeded: the captives were clothed from the spoil and returned to Jericho (2 Chronicles 28:9–15).</p>",
        "sections": [],
        "hitchcock_meaning": "to sustain, hold or lift up",
        "source_ids": {"easton": "oded", "smith": "oded"},
        "key_refs": ["2 Chronicles 15:1", "2 Chronicles 28:9", "2 Chronicles 28:15"]
    },
    "offence": {
        "id": "offence",
        "term": "Offence",
        "category": "concepts",
        "intro": "<p>In biblical usage, offence denotes both a moral transgression against God's law and, more specifically in the New Testament, a <em>stumbling block</em> (<em>skandalon</em>) — something that causes another to fall into sin. The Greek <em>skandalon</em> (from which <em>scandal</em> derives) originally referred to the trigger of a trap, then metaphorically to any obstacle or inducement to sin. Jesus warned with great severity against causing <em>one of these little ones</em> to stumble — it would be better to be drowned with a millstone (Matthew 18:6–7).</p><p>Paul develops the concept pastorally: the strong have an obligation not to use their freedom in ways that cause the weak to stumble (Romans 14:13–20; 1 Corinthians 8:9–13). The cross itself is a <em>skandalon</em> — a stumbling block to Jews and foolishness to Greeks (1 Corinthians 1:23; Galatians 5:11). The category thus spans from culpable sin to the paradox of the gospel's offensiveness to human pride.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "offence", "isbe": "offence"},
        "key_refs": ["Matthew 18:6", "Romans 14:13", "1 Corinthians 1:23"]
    },
    "offering": {
        "id": "offering",
        "term": "Offering",
        "category": "concepts",
        "intro": "<p>Offerings — gifts presented to God in worship, atonement, or thanksgiving — form the backbone of Old Testament sacrificial religion. The Mosaic law distinguished numerous types: the <em>olah</em> (burnt offering), wholly consumed on the altar; the <em>minchah</em> (grain offering); the <em>shelamim</em> (peace or fellowship offering), of which part was returned to the worshipper; the <em>hattat</em> (sin offering) and <em>asham</em> (guilt offering) for atonement; and various firstfruits, votive, and freewill offerings. Each communicated a different aspect of the covenant relationship between God and Israel.</p><p>The New Testament interprets the entire sacrificial system as a shadow pointing forward to Christ's single, final, sufficient self-offering. The letter to the Hebrews argues at length that Jesus, as the eternal High Priest, offered himself once for all, rendering the Levitical system obsolete (Hebrews 9–10). Paul exhorts believers to present their bodies as a living sacrifice — a spiritual act of worship (Romans 12:1), reinterpreting offering language in terms of consecrated Christian life.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "offering", "isbe": "offering"},
        "key_refs": ["Leviticus 1:3", "Hebrews 10:10", "Romans 12:1"]
    },
    "og": {
        "id": "og",
        "term": "Og",
        "category": "people",
        "intro": "<p>Og was the Amorite king of Bashan, celebrated in the Old Testament as the last survivor of the Rephaim — the giant race of pre-Israelite Canaan. His kingdom, which included sixty fortified cities, was conquered by Israel under Moses east of the Jordan (Numbers 21:33–35; Deuteronomy 3:1–7). Deuteronomy 3:11 notes that his iron bedstead (<em>eres</em>) was nine cubits long and four cubits wide (approximately 13 by 6 feet), kept at Rabbah of the Ammonites as evidence of his extraordinary size.</p><p>The defeat of Og and the parallel defeat of Sihon king of the Amorites became formulaic paradigms of divine power in Israelite liturgy: Psalms 135:11 and 136:20 name Sihon and Og together among God's mighty acts at the conquest. Nehemiah 9:22 and Amos 2:9 also invoke the defeat of the Amorites as evidence of God's faithfulness. The memory of Og represents Israel's confidence that divine power prevails over the most formidable human opposition.</p>",
        "sections": [],
        "hitchcock_meaning": "a cake; bread baked in ashes",
        "source_ids": {"easton": "og", "smith": "og", "isbe": "og"},
        "key_refs": ["Deuteronomy 3:1", "Deuteronomy 3:11", "Psalms 135:11", "Psalms 136:20"]
    },
    "ohad": {
        "id": "ohad",
        "term": "Ohad",
        "category": "people",
        "intro": "<p>Ohad (meaning <em>praising</em> or <em>confessing</em>) was the third son of Simeon listed in the genealogy of Genesis 46:10 and Exodus 6:15. He appears only in these two genealogical notices and is not mentioned as the ancestor of any later Simeonite clan. His name is absent from the clan list of Numbers 26:12–14, suggesting that his line may have died out before the second generation of the wilderness period. Ohad is one of several Simeonite names that disappear from the later tribal records.</p>",
        "sections": [],
        "hitchcock_meaning": "praising; confessing",
        "source_ids": {"easton": "ohad"},
        "key_refs": ["Genesis 46:10", "Exodus 6:15"]
    },
    "ohel": {
        "id": "ohel",
        "term": "Ohel",
        "category": "people",
        "intro": "<p>Ohel (meaning <em>tent</em> or <em>tabernacle</em>) was a son of Zerubbabel, the governor of Judah who led the first return from the Babylonian exile. He is listed among Zerubbabel's children in 1 Chronicles 3:20. As a grandson of Shealtiel and a member of the Davidic royal family, Ohel was part of the messianic line through which Israel's hopes for restoration were focused in the post-exilic period. He is otherwise unknown beyond this genealogical notice.</p>",
        "sections": [],
        "hitchcock_meaning": "tent; tabernacle; brightness",
        "source_ids": {"easton": "ohel"},
        "key_refs": ["1 Chronicles 3:20"]
    },
    "oil": {
        "id": "oil",
        "term": "Oil",
        "category": "concepts",
        "intro": "<p>Olive oil was the primary oil of ancient Palestine and the most versatile commodity in Israelite life — used for food, lighting, medicine, cosmetics, and sacred anointing. The Hebrew <em>shemen</em> appears hundreds of times in the Old Testament. Israel's land was characterized by its olive trees and oil (Deuteronomy 8:8), and the triennial abundance or failure of the olive harvest determined the prosperity of the whole community. Oil was stored in jars and applied to bread, used to anoint honored guests (Psalm 23:5; Luke 7:46), and burned in lamps to provide light.</p><p>In the sacred sphere, oil was the medium of anointing — priests, kings, and the tabernacle furniture were consecrated with specially formulated holy anointing oil (Exodus 30:25). The anointing oil could not be reproduced for ordinary use under penalty of death. Oil also featured in grain offerings (Leviticus 2:1–7) and in the rituals of cleansing lepers (Leviticus 14:10–18). In the New Testament, oil is associated with healing prayer (James 5:14) and with the parable of the ten virgins (Matthew 25:3–8).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "oil", "smith": "oil", "isbe": "oil"},
        "key_refs": ["Exodus 29:7", "Psalms 23:5", "James 5:14", "Exodus 30:25"]
    },
    "oil-tree": {
        "id": "oil-tree",
        "term": "Oil-tree",
        "category": "concepts",
        "intro": "<p>The oil-tree (<em>ets shemen</em> in Hebrew, literally <em>tree of oil</em>) is mentioned in Isaiah 41:19 in a promise of wilderness transformation — along with cedar, myrtle, and fir — and in 1 Kings 6:23 and 6:31–33, where the cherubim in Solomon's temple and the doors of the inner sanctuary were made from oil-tree wood. The exact species is debated: proposed identifications include the oleaster or wild olive (<em>Elaeagnus angustifolia</em>), the Aleppo pine, or simply a richly oiled variety of olive. It is distinct from the common olive tree (<em>zayith</em>).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "oil-tree", "isbe": "oil-tree"},
        "key_refs": ["1 Kings 6:23", "Isaiah 41:19"]
    },
    "ointment": {
        "id": "ointment",
        "term": "Ointment",
        "category": "concepts",
        "intro": "<p>Ointments (aromatic oil preparations used for personal hygiene, medicinal treatment, and sacred anointing) were valued commodities throughout the ancient Near East. The Hebrew and Greek terms (<em>shemen</em>, <em>myron</em>) overlap with the words for oil, but ointment usually implies a thicker, perfumed preparation. The sacred anointing oil of Exodus 30:23–25 was a specially compounded ointment of myrrh, cinnamon, calamus, cassia, and olive oil.</p><p>Ointments feature prominently in several Gospel narratives. Mary of Bethany anointed Jesus's feet with a pound of expensive <em>nard</em> ointment — an act Jesus interpreted as preparation for his burial (John 12:3–8; Matthew 26:12). An unnamed woman anointed Jesus's head with an alabaster jar of costly spikenard in the house of Simon the leper. The women who came to the tomb on Easter morning brought spices and ointments to complete the burial preparation (Luke 24:1). Psalm 133:2 uses anointing oil as a symbol of blessing and brotherly unity.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ointment", "isbe": "ointment"},
        "key_refs": ["Exodus 30:25", "Psalms 133:2", "John 12:3", "Matthew 26:7"]
    },
    "old-gate": {
        "id": "old-gate",
        "term": "Old gate",
        "category": "places",
        "intro": "<p>The Old Gate (also called the Jeshanah Gate in some translations) was one of the gates of Jerusalem repaired during Nehemiah's rebuilding of the city walls (Nehemiah 3:6). It was repaired by Jehoiada son of Paseah and Meshullam son of Besodeiah. The gate likely stood in the northern wall of the city. Its name (<em>sha'ar hayyeshanah</em>, the gate of the old city or the ancient gate) suggests it was associated with an older section of Jerusalem — possibly dating to the pre-exilic period. In Nehemiah 12:39 it is named among the stations in the great procession celebrating the wall's dedication.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "old-gate"},
        "key_refs": ["Nehemiah 3:6", "Nehemiah 12:39"]
    },
    "olive": {
        "id": "olive",
        "term": "Olive",
        "category": "concepts",
        "intro": "<p>The olive (<em>Olea europaea</em>) was the most economically and symbolically significant tree of ancient Palestine — a cornerstone of the Mediterranean agricultural triad of grain, wine, and oil. Olive trees required seven to ten years to mature after planting but then bore fruit for centuries; the trees on the Mount of Olives may trace to the Roman period. Harvesting involved beating the branches with long poles (Deuteronomy 24:20), shaking the tree, or hand-picking. The resulting olives were pressed in stone presses to yield oil for food, lighting, and anointing.</p><p>The olive appears throughout the biblical narrative as a symbol of abundance, peace, and divine blessing. A dove brought Noah an olive branch, signaling the end of the Flood (Genesis 8:11). Jotham's parable in Judges 9:8–9 portrays the olive as the most honored of trees, refusing to be king over lesser trees. Paul's extended metaphor in Romans 11:17–24 uses the cultivated olive and its wild counterpart to depict Israel's election, Gentile inclusion, and the mystery of God's grafting purposes.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "olive", "smith": "olive", "isbe": "olive"},
        "key_refs": ["Genesis 8:11", "Judges 9:9", "Romans 11:17", "Deuteronomy 24:20"]
    },
    "olive-tree": {
        "id": "olive-tree",
        "term": "Olive-tree",
        "category": "concepts",
        "intro": "<p>The olive tree in biblical literature functions both as an agricultural reality and as a richly layered symbol. As a tree it is described as <em>good</em> in Jotham's fable (Judges 9:9), its oil described as that which <em>honors God and man.</em> The Psalmist describes the righteous man as <em>a green olive tree in the house of God</em> (Psalm 52:8). The two witnesses of Revelation 11:4 are described as <em>the two olive trees and the two lampstands</em> — imagery drawn from Zechariah's vision of the golden lampstand flanked by two olive trees representing the divine supply of anointing (Zechariah 4:3–14).</p><p>Cultivation of olive trees was a major occupation in biblical Canaan. Their deep roots and ability to regrow from the stump after cutting made them a fitting symbol of resilience and renewal. The Davidic royal line, whose potential seemed extinguished at the Exile, was compared to a stump from which a shoot would grow — an image that recalls the olive's regenerative power (Isaiah 11:1).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "olive-tree", "isbe": "olive-tree"},
        "key_refs": ["Judges 9:9", "Psalms 52:8", "Zechariah 4:3", "Revelation 11:4"]
    },
    "olves-mount-of": {
        "id": "olves-mount-of",
        "term": "Olives, Mount of",
        "category": "places",
        "intro": "<p>The Mount of Olives is a limestone ridge running north-south along the eastern side of Jerusalem, separated from the Temple Mount by the Kidron valley. It rises approximately 200 feet above the temple platform and commands a panoramic view of the city. Its name reflects the extensive olive groves that covered its slopes in antiquity. In the Old Testament it appears as the site of David's sorrowful ascent during Absalom's rebellion (2 Samuel 15:30) and as the location where Solomon built high places for Ashtoreth, Chemosh, and Milcom — idols that Josiah later desecrated (1 Kings 11:7; 2 Kings 23:13).</p><p>Its New Testament significance far surpasses its Old Testament role. Jesus regularly crossed from Jerusalem to the Mount of Olives, and Luke notes he spent nights there during the Passion week (Luke 21:37). The Garden of Gethsemane lay at its western foot (Matthew 26:36). From its summit Jesus wept over Jerusalem (Luke 19:41) and delivered the Olivet Discourse (Matthew 24; Mark 13). The ascension took place from its slopes (Acts 1:12), and Zechariah's prophecy that the LORD's feet would stand on it in the Day of the LORD (Zechariah 14:4) has shaped Christian eschatological expectation.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "olves-mount-of", "smith": "olves-mount-of"},
        "key_refs": ["2 Samuel 15:30", "Zechariah 14:4", "Luke 21:37", "Acts 1:12"]
    },
    "olympas": {
        "id": "olympas",
        "term": "Olympas",
        "category": "people",
        "intro": "<p>Olympas (meaning <em>heavenly</em>) was a Christian at Rome greeted by Paul in Romans 16:15: <em>Greet Philologus, Julia, Nereus and his sister, and Olympas, and all the saints who are with them.</em> The name is a shortened form of Olympiodorus (<em>gift of Olympus</em>). Nothing further is known about Olympas beyond this brief mention, though the grouping with Philologus, Julia, and Nereus suggests a household church unit meeting together. Ancient tradition identifies Olympas as one of the seventy disciples sent out by Jesus (Luke 10:1) and as a later martyr, but these traditions are not verifiable.</p>",
        "sections": [],
        "hitchcock_meaning": "heavenly",
        "source_ids": {"easton": "olympas"},
        "key_refs": ["Romans 16:15"]
    },
    "omar": {
        "id": "omar",
        "term": "Omar",
        "category": "people",
        "intro": "<p>Omar (meaning <em>he that speaks</em> or <em>eloquent</em>) was the second son of Eliphaz the firstborn of Esau (Genesis 36:11; 1 Chronicles 1:36), and thus a grandson of Esau and one of the chiefs of Edom (Genesis 36:15). He is listed among the Edomite chiefs — the <em>dukes of Esau</em> — whose names became the names of Edomite clans or districts. The exact territory associated with the clan of Omar is unknown; he appears only in these genealogical and administrative lists.</p>",
        "sections": [],
        "hitchcock_meaning": "he that speaks; bitter",
        "source_ids": {"easton": "omar"},
        "key_refs": ["Genesis 36:11", "1 Chronicles 1:36"]
    },
    "omega": {
        "id": "omega",
        "term": "Omega",
        "category": "concepts",
        "intro": "<p>Omega is the last letter of the Greek alphabet, used in the New Testament exclusively in the title <em>Alpha and Omega</em> — a divine self-designation meaning <em>the first and the last</em> or <em>the beginning and the end.</em> The title appears three times in Revelation: attributed to the LORD God in 1:8 (<em>I am the Alpha and the Omega, the beginning and the ending, says the Lord God who is and who was and who is to come, the Almighty</em>); to the risen Christ in 22:13 (<em>I am the Alpha and the Omega, the first and the last, the beginning and the end</em>); and in 21:6 where God declares the same.</p><p>The title echoes the Hebrew prophetic formula in Isaiah 41:4; 44:6; and 48:12, where God identifies himself as the first and the last. By claiming this title in Revelation, Christ is identified with the eternal God of Israel — the one who encompasses all of history and whose sovereign purpose spans from creation to new creation.</p>",
        "sections": [],
        "hitchcock_meaning": "the last letter of the Greek alphabet; long O",
        "source_ids": {"easton": "omega", "isbe": "omega"},
        "key_refs": ["Revelation 1:8", "Revelation 22:13", "Isaiah 44:6"]
    },
    "omer": {
        "id": "omer",
        "term": "Omer",
        "category": "concepts",
        "intro": "<p>The omer was a unit of dry measure in ancient Israel, equal to one-tenth of an ephah (Exodus 16:36) — approximately 2.3 liters or just over 2 quarts. It appears primarily in the context of the manna in the wilderness: each person was to gather one omer per day (Exodus 16:16), and a double omer on the sixth day for the sabbath. A jar containing an omer of manna was preserved in the ark of the covenant as a perpetual memorial of God's provision (Exodus 16:33). The omer should be distinguished from the <em>Omer</em> of post-biblical Jewish practice — the seven-week count from Passover to Pentecost.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "omer"},
        "key_refs": ["Exodus 16:16", "Exodus 16:33", "Exodus 16:36"]
    },
    "omri": {
        "id": "omri",
        "term": "Omri",
        "category": "people",
        "intro": "<p>Omri was the sixth king of the northern kingdom of Israel (c. 885–874 BC), founder of the Omride dynasty that produced Ahab, Ahaziah, and Joram. He came to power by defeating his rival Tibni in a civil war following the assassination of Zimri, who had himself killed Elah (1 Kings 16:15–22). Omri's political and military accomplishments were significant: he purchased the hill of Samaria and built a new capital city there (1 Kings 16:24), securing a strategic and politically neutral site for the northern monarchy, and he subdued Moab — attested on the Mesha Stele, where Israel is called <em>the land of Omri.</em></p><p>In Assyrian records the northern kingdom was referred to as <em>Bit-Humri</em> (House of Omri) for more than a century after his dynasty ended, testifying to his regional impact. Despite his political achievement, the biblical narrative judges him the worst king yet in Israel: he <em>did worse than all who were before him</em> and walked in the sins of Jeroboam (1 Kings 16:25–26). Micah 6:16 cites <em>the statutes of Omri</em> as a paradigm of social injustice and apostasy.</p>",
        "sections": [],
        "hitchcock_meaning": "sheaf of corn",
        "source_ids": {"easton": "omri", "smith": "omri", "isbe": "omri"},
        "key_refs": ["1 Kings 16:24", "1 Kings 16:25", "Micah 6:16"]
    },
    "on": {
        "id": "on",
        "term": "On",
        "category": "places",
        "intro": "<p>On (Egyptian: <em>Iunu</em>; Greek: <em>Heliopolis</em>, <em>city of the sun</em>) was the principal center of sun-worship in ancient Egypt, located in the Nile Delta approximately ten miles northeast of modern Cairo. It was home to the great temple of Ra-Atum-Khepri and its famous obelisks, and its high priest was among the most powerful religious officials in Egypt. The biblical patriarch Joseph married Asenath, the daughter of Potiphera, priest of On (Genesis 41:45, 50), cementing his integration into Egyptian elite society.</p><p>The prophets of Israel directed oracles against On as a symbol of Egyptian idolatry: Jeremiah 43:13 predicts that Nebuchadnezzar will break the obelisks of Beth-shemesh (House of the Sun, i.e., Heliopolis) and burn the temples of Egypt's gods. Ezekiel 30:17 prophesies that the young men of On and of Pi-beseth will fall by the sword. Isaiah 19:18 speaks mysteriously of a <em>City of the Sun</em> that will one day speak the language of Canaan and swear allegiance to the LORD.</p>",
        "sections": [],
        "hitchcock_meaning": "pain; force; iniquity",
        "source_ids": {"easton": "on", "smith": "on", "isbe": "on"},
        "key_refs": ["Genesis 41:45", "Jeremiah 43:13", "Ezekiel 30:17"]
    },
    "onan": {
        "id": "onan",
        "term": "Onan",
        "category": "people",
        "intro": "<p>Onan was the second son of Judah and a Canaanite woman named Shua, and the central figure of a morally complex episode in Genesis 38. After his older brother Er died childless, Judah instructed Onan to fulfill the duty of levirate marriage — to take Er's widow Tamar and raise up offspring to perpetuate his brother's name (Deuteronomy 25:5–6; Genesis 38:8). Onan, unwilling to produce an heir who would legally belong to his dead brother rather than to himself, deliberately prevented conception. The LORD regarded this as wicked and put him to death (Genesis 38:9–10).</p><p>The narrative's theological point is Onan's failure of covenant obligation — his refusal to perform levirate duty to preserve his brother's lineage — rather than a general prohibition. The episode is part of the larger providential story of how Judah's line was preserved through Tamar's unconventional persistence, leading eventually to the birth of Perez and the Davidic and messianic lineage.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "onan", "smith": "onan"},
        "key_refs": ["Genesis 38:4", "Genesis 38:9", "Deuteronomy 25:5"]
    },
    "onesimus": {
        "id": "onesimus",
        "term": "Onesimus",
        "category": "people",
        "intro": "<p>Onesimus (meaning <em>profitable</em> or <em>useful</em>) was a slave who had run away from his master Philemon, a wealthy Christian in Colossae, and eventually came into contact with the imprisoned Paul — possibly in Rome or Ephesus. Under Paul's ministry Onesimus became a Christian (Philemon 10) and proved so useful that Paul was tempted to keep him as an assistant. Instead, Paul sent him back to Philemon with the short letter that bears Philemon's name, appealing to Philemon to receive Onesimus <em>no longer as a slave, but better than a slave, as a dear brother</em> (Philemon 16), and offering to repay anything Onesimus owed.</p><p>Colossians 4:9 identifies Onesimus as a <em>faithful and dear brother,</em> traveling with Tychicus to Colossae. The letter to Philemon is the New Testament's most sustained engagement with the institution of slavery, demonstrating how the gospel's logic of brotherhood and mutual obligation worked within and against the social structures of the Roman world. A second-century bishop of Ephesus named Onesimus, mentioned by Ignatius, may or may not be the same person.</p>",
        "sections": [],
        "hitchcock_meaning": "profitable; useful",
        "source_ids": {"easton": "onesimus", "smith": "onesimus", "isbe": "onesimus"},
        "key_refs": ["Philemon 1:10", "Philemon 1:16", "Colossians 4:9"]
    },
    "onesiphorus": {
        "id": "onesiphorus",
        "term": "Onesiphorus",
        "category": "people",
        "intro": "<p>Onesiphorus (meaning <em>who brings profit</em> or <em>profit-bringer</em>) was a Christian from Ephesus warmly commended by Paul in 2 Timothy 1:16–18 for his loyal friendship. When Paul was in chains in Rome — a circumstance that had caused others to abandon him — Onesiphorus searched for Paul diligently and found him, refreshing his spirits and not being ashamed of his chains. Paul expresses gratitude both for Onesiphorus's service in Ephesus and for this final act of courage in Rome, praying that the Lord would grant him mercy on the Day of the Lord. His household is greeted in 2 Timothy 4:19.</p>",
        "sections": [],
        "hitchcock_meaning": "who brings profit",
        "source_ids": {"easton": "onesiphorus"},
        "key_refs": ["2 Timothy 1:16", "2 Timothy 4:19"]
    },
    "onion": {
        "id": "onion",
        "term": "Onion",
        "category": "concepts",
        "intro": "<p>Onions (<em>betsalim</em> in Hebrew) appear in the Bible in a single passage that reveals much about the Israelites' nostalgia for Egyptian food during the wilderness march. In Numbers 11:5, the people lament: <em>We remember the fish we ate in Egypt for nothing, the cucumbers, the melons, the leeks, the onions, and the garlic.</em> Egyptian onions were famous in antiquity — large, sweet, and consumed raw, cooked, and in relishes. The complaint reflects the genuine hardship of a diet limited to manna and the human tendency to idealize past comforts while minimizing the circumstances of oppression that accompanied them.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "onion"},
        "key_refs": ["Numbers 11:5"]
    },
    "ono": {
        "id": "ono",
        "term": "Ono",
        "category": "places",
        "intro": "<p>Ono was a town in the territory of Benjamin in the Sharon plain, built (or rebuilt) by Shamed, a Benjaminite (1 Chronicles 8:12), along with Lod and their surrounding villages. It is paired with Lod repeatedly in the post-exilic lists: Ezra 2:33 and Nehemiah 7:37 record that 725 men of Lod, Hadid, and Ono returned from the Babylonian captivity. In Nehemiah 6:2, Sanballat and Geshem used Ono as a neutral meeting place to which they invited Nehemiah — a summons he wisely refused, recognizing it as a plot against him. The town is identified with modern Kafr Ana, near Jaffa.</p>",
        "sections": [],
        "hitchcock_meaning": "grief or strength or iniquity of him",
        "source_ids": {"easton": "ono"},
        "key_refs": ["1 Chronicles 8:12", "Ezra 2:33", "Nehemiah 6:2"]
    },
    "onycha": {
        "id": "onycha",
        "term": "Onycha",
        "category": "concepts",
        "intro": "<p>Onycha (<em>shecheleth</em> in Hebrew; <em>onyx</em> in the Septuagint, though likely a different substance) was one of the four aromatic ingredients in the sacred incense burned before the LORD in the tabernacle (Exodus 30:34). The three other ingredients were stacte, galbanum, and pure frankincense. Onycha is generally identified with the operculum — the horny, claw-like covering of a sea snail (<em>Strombus</em> or <em>Murex</em>) from the Red Sea, which when burned produces a musky, animal-like fragrance. The burning of this compound incense was reserved exclusively for sacred use; its formula was not to be replicated (Exodus 30:37).</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "onycha", "isbe": "onycha"},
        "key_refs": ["Exodus 30:34"]
    },
    "onyx": {
        "id": "onyx",
        "term": "Onyx",
        "category": "concepts",
        "intro": "<p>Onyx (<em>shoham</em> in Hebrew) was a precious stone used extensively in the construction and ornamentation of the tabernacle and the high priest's vestments. Two large onyx stones were mounted in gold settings on the shoulder pieces of the ephod, engraved with the names of the twelve tribes of Israel — six names on each stone — so that Aaron bore the names of Israel's sons before the LORD as a memorial (Exodus 28:9–12). The breastpiece also contained an onyx stone (Exodus 28:20). Onyx was among the precious stones in the garden of Eden (Genesis 2:12) and among the materials contributed for the tabernacle (Exodus 35:27). In the Hebrew the term <em>shoham</em> may refer to the true onyx (a banded chalcedony) or to beryl or sardonyx.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "onyx", "isbe": "onyx"},
        "key_refs": ["Exodus 28:9", "Genesis 2:12", "Job 28:16"]
    },
    "open-place": {
        "id": "open-place",
        "term": "Open place",
        "category": "concepts",
        "intro": "<p>The <em>open place</em> or <em>broad place</em> (<em>rechob</em> in Hebrew) refers to the plaza, square, or wide street at the city gate in ancient Israelite towns. This civic space served as the principal venue for public life: legal proceedings and judicial decisions (Deuteronomy 21:19), public readings of the law (Nehemiah 8:1–3), lamentation (Ezra 10:9), and commercial activity. Ezra assembled all the men of Judah and Benjamin at the broad place before the house of God in Jerusalem to deal with the issue of foreign marriages.</p><p>The prophet Jeremiah commanded Baruch to read the scroll publicly in the broad place at the New Gate of the temple (Jeremiah 36:10). Amos 5:10 uses the gate as a metonym for the city's justice system: <em>they hate him who reproves in the gate.</em> The open place was where the social and legal fabric of the community was most visibly woven and torn.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "open-place"},
        "key_refs": ["Nehemiah 8:1", "Ezra 10:9", "Amos 5:10"]
    },
    "ophel": {
        "id": "ophel",
        "term": "Ophel",
        "category": "places",
        "intro": "<p>Ophel (meaning <em>a mound</em>, <em>bulge</em>, or <em>fortified hill</em>) was a prominent spur on the southeastern hill of Jerusalem, lying between the City of David to the south and the temple mount to the north. It served as an important defensive and administrative zone from the pre-Israelite period onward. Jotham and Manasseh both built extensively on the Ophel (2 Chronicles 27:3; 33:14), and Nehemiah 3:26–27 records the Nethinim (temple servants) living and working there during the wall rebuilding.</p><p>Archaeological excavations on the Ophel spur by Eilat Mazar and others have uncovered substantial Iron Age walls, storehouses, and inscriptions — including a bulla that may bear the name of the prophet Isaiah — confirming its importance as a functioning quarter of the royal city. Micah 4:8 uses <em>Ophel</em> or <em>tower of the flock</em> as a poetic designation for Jerusalem in a prophecy of restoration.</p>",
        "sections": [],
        "hitchcock_meaning": "a tower; darkness; small white cloud",
        "source_ids": {"easton": "ophel", "smith": "ophel", "isbe": "ophel"},
        "key_refs": ["2 Chronicles 27:3", "Nehemiah 3:26", "Micah 4:8"]
    },
    "ophir": {
        "id": "ophir",
        "term": "Ophir",
        "category": "places",
        "intro": "<p>Ophir was a land of legendary wealth in the ancient world, famous as the destination of the joint trading expeditions of Solomon and Hiram king of Tyre. The fleet sailed from Ezion-geber on the Red Sea and returned with gold, almug wood, precious stones, silver, ivory, apes, and peacocks (1 Kings 9:26–28; 10:11, 22). The gold of Ophir became proverbial in Hebrew poetry: Job 22:24 and 28:16 compare the finest gold to Ophir's gold, and Isaiah 13:12 uses it as a simile for extreme rarity.</p><p>The location of Ophir has been debated for centuries. Proposed identifications include southern Arabia (Yemen), the African coast of Somalia, the Indian subcontinent (Gujarat), Zimbabwe (associated with ancient gold mines), and southern Sudan. The combination of products — gold, apes, peacocks, almug wood — best fits the Indian Ocean littoral. The Ophir of Genesis 10:29 is a Joktanite people of Arabia, which may be distinct from the trading destination.</p>",
        "sections": [],
        "hitchcock_meaning": "fruitful region",
        "source_ids": {"easton": "ophir", "smith": "ophir", "isbe": "ophir"},
        "key_refs": ["1 Kings 9:28", "1 Kings 10:11", "Job 28:16"]
    },
    "ophni": {
        "id": "ophni",
        "term": "Ophni",
        "category": "places",
        "intro": "<p>Ophni (meaning <em>wearisomeness</em> or <em>folding together</em>) was a town in the territory of Benjamin listed in Joshua 18:24 among the cities allotted to that tribe. It is mentioned only here and has not been positively identified, though several sites in the Benjaminite hill country north of Jerusalem have been proposed. Ophni is one of several obscure Benjaminite towns known only from this administrative list.</p>",
        "sections": [],
        "hitchcock_meaning": "wearisomeness; folding together",
        "source_ids": {"easton": "ophni"},
        "key_refs": ["Joshua 18:24"]
    },
    "ophrah": {
        "id": "ophrah",
        "term": "Ophrah",
        "category": "places",
        "intro": "<p>Ophrah (meaning <em>fawn</em> or <em>lead</em>) was the name of two towns in ancient Israel and a personal name. The most significant was Ophrah of the Abiezrites in Manasseh — the hometown of Gideon (Joash the Abiezrite's son), where the angel of the LORD appeared to him under the oak tree and commissioned him to deliver Israel from Midian (Judges 6:11–24). Gideon built an altar there called <em>Yahweh is Peace</em> and later made a gold ephod there from the spoils of battle, which became a snare to Israel (Judges 8:27). He was buried at Ophrah (Judges 8:32).</p><p>A second Ophrah was a town in Benjamin (Joshua 18:23; 1 Samuel 13:17), possibly the modern village of et-Taiyibeh north of Bethel. The personal name Ophrah also appears in 1 Chronicles 4:14 as a Judahite.</p>",
        "sections": [],
        "hitchcock_meaning": "dust; lead; a fawn",
        "source_ids": {"easton": "ophrah", "smith": "ophrah"},
        "key_refs": ["Judges 6:11", "Judges 6:24", "Judges 8:27", "Judges 8:32"]
    },
    "oracle": {
        "id": "oracle",
        "term": "Oracle",
        "category": "concepts",
        "intro": "<p>An oracle in the biblical context is a divine communication — a word spoken by God, mediated by a prophet, and delivered to human recipients. The Hebrew <em>massa</em> (translated <em>burden</em> or <em>oracle</em>) often introduces the prophetic speeches of the writing prophets (Isaiah, Nahum, Habakkuk, Malachi), carrying the sense of a weighty divine declaration. In the New Testament, the Greek <em>logia</em> (oracles, sayings) is used for the body of God's revealed word: Romans 3:2 describes the Jews as entrusted with the <em>oracles of God</em>; Hebrews 5:12 speaks of <em>the first principles of the oracles of God</em>; and Acts 7:38 uses it for the law given through Moses.</p><p>In 1 Kings 6:5, 16, 19–23, the inner sanctuary of Solomon's temple — the Holy of Holies — is called the <em>oracle</em> (<em>devir</em> in Hebrew, from the root <em>dabar</em>, word/speak), the place where God's presence spoke. The term thus bridges the localized divine dwelling and the verbally mediated divine communication.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "oracle", "isbe": "oracle"},
        "key_refs": ["Romans 3:2", "1 Kings 6:16", "Hebrews 5:12"]
    },
    "oreb": {
        "id": "oreb",
        "term": "Oreb",
        "category": "people",
        "intro": "<p>Oreb (meaning <em>a raven</em>) was one of two Midianite princes killed by the Ephraimites during the rout of the Midianite army after Gideon's night attack. Judges 7:24–25 records that Gideon sent messengers to Ephraim to intercept the retreating Midianites at the fords of the Jordan; the Ephraimites captured Oreb and Zeeb (meaning <em>wolf</em>) and killed them — Oreb at the rock of Oreb and Zeeb at the winepress of Zeeb. Their heads were brought to Gideon beyond the Jordan. The names suggest a poetic pairing: raven and wolf as emblems of predatory raiding.</p><p>The defeat of Oreb and Zeeb became a paradigm of divine deliverance in Israelite memory, invoked in Psalm 83:11 and in Isaiah 10:26, where God's coming judgment on Assyria is compared to his striking down of the Midianites at the rock of Oreb.</p>",
        "sections": [],
        "hitchcock_meaning": "a raven",
        "source_ids": {"easton": "oreb", "smith": "oreb"},
        "key_refs": ["Judges 7:25", "Psalms 83:11", "Isaiah 10:26"]
    },
    "oreb-the-rock-of": {
        "id": "oreb-the-rock-of",
        "term": "Oreb, The rock of",
        "category": "places",
        "intro": "<p>The rock of Oreb was the site east of the Jordan, on the western side of the Arabah or the Jordan valley, where the Midianite prince Oreb was captured and executed by the Ephraimites during the rout following Gideon's victory (Judges 7:25). The site was memorable enough to be named after the event. Isaiah 10:26 invokes it in a promise of God's coming judgment on Assyria: <em>as when he struck Midian at the rock of Oreb.</em> The exact location has not been identified.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "oreb-the-rock-of"},
        "key_refs": ["Judges 7:25", "Isaiah 10:26"]
    },
    "oren": {
        "id": "oren",
        "term": "Oren",
        "category": "people",
        "intro": "<p>Oren (meaning <em>a pine tree</em> or <em>cedar</em>, cognate with Arabic <em>aran</em>) was a son of Jerahmeel, listed in the genealogy of the tribe of Judah in 1 Chronicles 2:25. He is one of Jerahmeel's sons by his first wife, alongside Ram, Bunah, Ahijah, and Onam. Oren appears only in this genealogical notice; no deeds, descendants, or associations are recorded for him.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "oren"},
        "key_refs": ["1 Chronicles 2:25"]
    },
    "organ": {
        "id": "organ",
        "term": "Organ",
        "category": "concepts",
        "intro": "<p>The <em>organ</em> in the KJV is the translation of the Hebrew <em>ugab</em>, a wind instrument mentioned in Genesis 4:21, Job 21:12, Job 30:31, and Psalm 150:4. The instrument appears to have been a pipe or flute rather than anything resembling the modern pipe organ — likely a simple reed flute or a set of pipes blown by the mouth. In Genesis 4:21, Jubal is said to be the father of all those who play the harp and organ, identifying them as the founders of instrumental music. Modern translations typically render <em>ugab</em> as <em>pipe</em> or <em>flute.</em></p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "organ"},
        "key_refs": ["Genesis 4:21", "Psalms 150:4", "Job 21:12"]
    },
    "orion": {
        "id": "orion",
        "term": "Orion",
        "category": "concepts",
        "intro": "<p>Orion is the brilliant winter constellation — one of the most recognizable in the night sky — referenced three times in the Old Testament as part of the biblical witness to God's creative sovereignty over the cosmos. Job 9:9 and 38:31 cite Orion alongside the Pleiades and Bear as constellations that only God can bind or loose: <em>Can you bind the chains of the Pleiades or loose the cords of Orion?</em> The Hebrew word is <em>Kesil</em> (meaning <em>a fool</em> or <em>a great one</em>), interpreted by ancient translators as corresponding to Orion the hunter. Amos 5:8 names the maker of Orion and Pleiades — <em>he who made the Pleiades and Orion</em> — as the LORD who judges Israel.</p><p>The grouping of Orion with the Pleiades in both Job and Amos suggests a traditional pairing of these two prominent star clusters, both visible in the winter sky over the ancient Near East. Their use in theological argument underscores the biblical claim that the natural order is entirely within God's governance.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "orion", "smith": "orion", "isbe": "orion"},
        "key_refs": ["Job 9:9", "Job 38:31", "Amos 5:8"]
    },
    "ornan": {
        "id": "ornan",
        "term": "Ornan",
        "category": "people",
        "intro": "<p>Ornan (also called Araunah in 2 Samuel 24) was a Jebusite — a member of the pre-Israelite inhabitants of Jerusalem — who owned the threshing floor on the summit of Mount Moriah that David purchased to erect an altar after the plague caused by his census. When David saw the angel of the LORD standing at Ornan's threshing floor with his sword outstretched over Jerusalem, he interceded for the people and was directed to build an altar there (1 Chronicles 21:18). Ornan offered to give the site and oxen freely to David, but David insisted on paying the full price: <em>I will not take what is yours for the LORD, nor offer burnt offerings with what costs me nothing</em> (1 Chronicles 21:24). David paid six hundred shekels of gold.</p><p>The threshing floor of Ornan/Araunah became the site of Solomon's temple (2 Chronicles 3:1), connecting it to the ancient place where Abraham prepared to sacrifice Isaac (Genesis 22:2 — <em>the land of Moriah</em>).</p>",
        "sections": [],
        "hitchcock_meaning": "that rejoices",
        "source_ids": {"easton": "ornan", "smith": "ornan"},
        "key_refs": ["1 Chronicles 21:18", "1 Chronicles 21:24", "2 Chronicles 3:1"]
    },
    "orpah": {
        "id": "orpah",
        "term": "Orpah",
        "category": "people",
        "intro": "<p>Orpah was the Moabite wife of Kilion (Chilion), the son of Elimelech and Naomi, and the sister-in-law of Ruth. After the deaths of Elimelech, Mahlon, and Kilion, Naomi urged both daughters-in-law to return to their mothers' houses and remarry in Moab (Ruth 1:8). Orpah kissed her mother-in-law goodbye, wept, and returned to her people and her gods — a decision presented without condemnation in the text. The contrast with Ruth's famous declaration of loyalty (<em>where you go I will go</em>, Ruth 1:16) is the narrative's way of heightening the extraordinary character of Ruth's faithfulness.</p><p>Orpah's choice was rational and culturally expected; Ruth's was exceptional. Orpah disappears from the narrative after Ruth 1:14 and is not mentioned again. Rabbinic tradition, elaborated in midrash, sometimes associates Orpah with the Philistine giant Goliath.</p>",
        "sections": [],
        "hitchcock_meaning": "the neck or skull",
        "source_ids": {"easton": "orpah", "smith": "orpah"},
        "key_refs": ["Ruth 1:4", "Ruth 1:14"]
    },
    "orphans": {
        "id": "orphans",
        "term": "Orphans",
        "category": "concepts",
        "intro": "<p>Orphans (Hebrew <em>yatom</em>, Greek <em>orphanos</em>) — fatherless children — are among the most consistently protected classes in biblical law and prophetic ethics. The Mosaic law repeatedly commands care for the fatherless: they were to share in the triennial tithe (Deuteronomy 14:29; 26:12), glean the harvest margins (Deuteronomy 24:19–21), and receive justice in the courts. Exploiting the fatherless was explicitly cursed (Deuteronomy 27:19) and listed among the sins that provoked God's judgment on Israel (Isaiah 1:23; Ezekiel 22:7).</p><p>God himself is described as a <em>father to the fatherless</em> (Psalm 68:5) and the one who <em>executes justice for the fatherless</em> (Deuteronomy 10:18). The prophets made care for orphans a litmus test of genuine religion: Isaiah 1:17 commands <em>defend the fatherless</em> as part of learning to do good. James 1:27 defines pure religion as caring for orphans and widows in their distress. Jesus uses the term <em>orphans</em> (<em>orphanous</em>) in John 14:18 to describe what he will not leave his disciples as: <em>I will not leave you as orphans; I will come to you.</em></p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "orphans", "isbe": "orphans"},
        "key_refs": ["Psalms 68:5", "Deuteronomy 24:19", "James 1:27", "John 14:18"]
    },
    "osprey": {
        "id": "osprey",
        "term": "Osprey",
        "category": "concepts",
        "intro": "<p>The osprey (Hebrew <em>ozniyyah</em>, from the root <em>oz</em>, strong) appears in the lists of unclean birds in Leviticus 11:13 and Deuteronomy 14:12. The exact species is uncertain; proposed identifications include the osprey (<em>Pandion haliaetus</em>), the black vulture, the short-toed eagle, or the bearded vulture (lammergeier). All these large raptors were apparently prohibited as food along with other birds of prey. The osprey, which feeds almost exclusively on fish caught in spectacular plunge-dives, would have been a familiar sight over the Sea of Galilee and the Jordan valley in antiquity.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "osprey", "isbe": "osprey"},
        "key_refs": ["Leviticus 11:13", "Deuteronomy 14:12"]
    },
    "ossifrage": {
        "id": "ossifrage",
        "term": "Ossifrage",
        "category": "concepts",
        "intro": "<p>The ossifrage (from Latin <em>ossifragus</em>, bone-breaker) appears in the lists of unclean birds in Leviticus 11:13 and Deuteronomy 14:12 (KJV). The Hebrew <em>peres</em> most likely refers to the bearded vulture or lammergeier (<em>Gypaetus barbatus</em>), a magnificent raptor of the mountains that drops bones from great heights to smash them on rocks below and then feeds on the marrow. This remarkable feeding behavior is the basis for both the Hebrew name and the Latin translation. Modern translations render <em>peres</em> as <em>vulture</em> or <em>ossifrage.</em></p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ossifrage"},
        "key_refs": ["Leviticus 11:13", "Deuteronomy 14:12"]
    },
    "ostrich": {
        "id": "ostrich",
        "term": "Ostrich",
        "category": "concepts",
        "intro": "<p>The ostrich is described in one of the Bible's most remarkable zoological passages — God's answer to Job from the whirlwind (Job 39:13–18). The passage describes the ostrich leaving her eggs in the sand to be warmed by the earth, showing no concern for their vulnerability (<em>she forgets that a foot may crush them</em>), yet capable of extraordinary speed: <em>she laughs at the horse and its rider.</em> The apparent carelessness is attributed to God's withholding of wisdom from her, while her speed surpasses even the war horse.</p><p>The Hebrew word <em>bat ya'anah</em> (daughter of the desert) also appears in lament contexts: ostriches and jackals inhabiting desolate ruins symbolize total devastation (Isaiah 13:21; 34:13; Micah 1:8). The ostrich (<em>Struthio camelus</em>) formerly inhabited the desert regions of the Near East and is now extinct in the wild in the Middle East. Its disconsolate cry is alluded to in Lamentations 4:3.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ostrich", "isbe": "ostrich"},
        "key_refs": ["Job 39:13", "Lamentations 4:3", "Isaiah 13:21"]
    },
    "othni": {
        "id": "othni",
        "term": "Othni",
        "category": "people",
        "intro": "<p>Othni (meaning <em>my time</em> or <em>my hour</em>, or possibly <em>lion of God</em> — a shorter form of Othniel) was one of David's mighty men and a gatekeeper of the temple, listed in 1 Chronicles 26:7 as a son of Shemaiah the Obed-edomite. He was a man of valor among the family of Obed-edom appointed to the temple gatekeeping and treasury duties. Othni should not be confused with his uncle Othniel the judge, though the names are closely related.</p>",
        "sections": [],
        "hitchcock_meaning": "my time; my hour",
        "source_ids": {"easton": "othni"},
        "key_refs": ["1 Chronicles 26:7"]
    },
    "othniel": {
        "id": "othniel",
        "term": "Othniel",
        "category": "people",
        "intro": "<p>Othniel son of Kenaz, the younger brother (or nephew) of Caleb, was the first judge of Israel after the death of Joshua and a paradigmatic figure for the entire period of the judges. He first distinguished himself by capturing Debir (Kiriath-sepher) for which Caleb promised his daughter Achsah in marriage — a feat that established his valor (Joshua 15:16–17; Judges 1:12–13). When Israel fell into the sin cycle of the judges period — serving the Baals and being oppressed by Cushan-rishathaim king of Mesopotamia for eight years — Othniel was raised up as deliverer (Judges 3:9–11).</p><p>The spirit of the LORD came upon him, he judged Israel, went to war, and the LORD gave Cushan-rishathaim into his hand. The land rested for forty years until Othniel died. His story serves as the structural template for all subsequent judge narratives: sin, servitude, supplication, salvation, silence. Smith describes him as <em>lion of God</em>, reflecting the name's probable meaning.</p>",
        "sections": [],
        "hitchcock_meaning": "the hour of God",
        "source_ids": {"easton": "othniel", "smith": "othniel", "isbe": "othniel"},
        "key_refs": ["Joshua 15:17", "Judges 3:9", "Judges 3:11"]
    },
    "ouches": {
        "id": "ouches",
        "term": "Ouches",
        "category": "concepts",
        "intro": "<p>Ouches is an archaic English word appearing in the KJV for the gold settings or sockets (<em>mishbetzot</em> in Hebrew) in which the onyx stones of the high priest's ephod were mounted (Exodus 28:11, 13–14; 39:6, 13, 16, 18). The word derives from Old French <em>nouche</em> (brooch, clasp) and refers to the ornate gold filigree or twisted wire settings that held precious stones in ancient Near Eastern jewelry. Each of the two onyx stones on the high priest's shoulders was set in such a golden mounting. Modern translations render the term as <em>settings</em>, <em>sockets</em>, or <em>filigree</em>.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ouches"},
        "key_refs": ["Exodus 28:11", "Exodus 28:13"]
    },
    "oven": {
        "id": "oven",
        "term": "Oven",
        "category": "concepts",
        "intro": "<p>The oven (<em>tannur</em> in Hebrew) in ancient Israel was a cylindrical clay vessel about three feet tall and two feet in diameter, wider at the bottom than the top, heated by burning wood or dried dung inside its cavity. Flat bread was baked by sticking it to the inner sides of the heated vessel or on a griddle placed over the opening. The intense heat of a furnace or oven became a natural metaphor for intense suffering or testing: <em>I have tried you in the furnace of affliction</em> (Isaiah 48:10).</p><p>Hosea 7:4–7 uses the metaphor of a heated oven for the burning passion of adulterers and the conspiracies of princes against the kings of Israel. Malachi 4:1 warns of the Day of the LORD coming like an oven in which the arrogant and evildoers will be consumed as stubble. The communal baking oven in Leviticus 26:26 — ten women baking in one oven — symbolizes extreme scarcity and the breakdown of social life under judgment.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "oven", "isbe": "oven"},
        "key_refs": ["Hosea 7:4", "Malachi 4:1", "Leviticus 26:26"]
    },
    "owl": {
        "id": "owl",
        "term": "Owl",
        "category": "concepts",
        "intro": "<p>Several Hebrew words are translated <em>owl</em> in English versions, covering a range of nocturnal birds. The owls mentioned in the unclean bird lists of Leviticus 11:16–18 and Deuteronomy 14:15–17 include the little owl (<em>kos</em>) and the great owl (<em>yanshuf</em>). The mournful cry of the owl and its association with ruins and desolation make it a powerful prophetic symbol: Isaiah 13:21; 34:11, 13–15; Jeremiah 50:39; and Micah 1:8 all use owls among the wild inhabitants of desolate Babylon or Samaria. Psalm 102:6 uses the solitary owl of the wilderness as a metaphor for the psalmist's lonely grief: <em>I am like an owl of the waste places.</em></p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "owl", "isbe": "owl"},
        "key_refs": ["Leviticus 11:16", "Psalms 102:6", "Isaiah 34:11"]
    },
    "ox": {
        "id": "ox",
        "term": "Ox",
        "category": "concepts",
        "intro": "<p>The ox (Hebrew <em>shor</em>; also <em>aleph</em>, the letter-name deriving from the word for ox) was the principal draft animal and a major sacrificial animal in ancient Israel. Oxen plowed fields, threshed grain (by treading or dragging a sledge), and transported loads. Their economic importance is reflected in the extensive legal protections: the law of the goring ox in Exodus 21:28–36 established liability principles; the commandment not to muzzle an ox while threshing (Deuteronomy 25:4) Paul interprets as a principle of fair compensation for workers (1 Corinthians 9:9).</p><p>In sacrifice, oxen were the most prestigious offering — David offered oxen and fatted cattle at the ark's installation (2 Samuel 6:13) and Solomon sacrificed 22,000 oxen at the temple's dedication (1 Kings 8:63). The four living creatures of Ezekiel 1:10 and Revelation 4:7 include one with a face like an ox, representing strength and service in the divine court. The ox appears in the manger imagery of Luke 2 only by tradition; the text does not name specific animals.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ox", "isbe": "ox"},
        "key_refs": ["Exodus 21:28", "Deuteronomy 25:4", "1 Corinthians 9:9", "1 Kings 8:63"]
    },
    "ox-goad": {
        "id": "ox-goad",
        "term": "Ox goad",
        "category": "concepts",
        "intro": "<p>An ox goad was a long pointed stick used to urge oxen forward while plowing. In ancient Israel the goad was typically a wooden shaft six to eight feet long with an iron or bronze tip. Shamgar the judge killed six hundred Philistines with an ox goad (Judges 3:31), demonstrating improvisational heroism comparable to Samson's use of a donkey's jawbone. The goad is also proverbially associated with the wisdom literature: <em>the words of the wise are like goads</em> (Ecclesiastes 12:11).</p><p>Jesus's word to Saul on the Damascus road — <em>it is hard for you to kick against the goads</em> (Acts 26:14) — uses the image of an ox resisting the goad, a common Greek and Roman proverb for futile resistance to an irresistible force. Saul's persecution of Christians, in this metaphor, was resistance to the divine impulse already working in his conscience.</p>",
        "sections": [],
        "hitchcock_meaning": None,
        "source_ids": {"easton": "ox-goad"},
        "key_refs": ["Judges 3:31", "Ecclesiastes 12:11", "Acts 26:14"]
    },
    "ozem": {
        "id": "ozem",
        "term": "Ozem",
        "category": "people",
        "intro": "<p>Ozem (meaning <em>that fasts</em> or <em>their eagerness</em>) was the name of two figures in the Old Testament. The first was the sixth son of Jesse and thus an older brother of King David (1 Chronicles 2:15). The second was a son of Jerahmeel in the tribe of Judah (1 Chronicles 2:25). Both appear only in genealogical lists and are otherwise unknown. The genealogy of Jesse's sons in 1 Chronicles 2:13–15 lists only seven sons before David (the eighth), suggesting that one of the brothers named elsewhere died without distinction or is counted differently from the account in 1 Samuel 16.</p>",
        "sections": [],
        "hitchcock_meaning": "that fasts; their eagerness",
        "source_ids": {"easton": "ozem"},
        "key_refs": ["1 Chronicles 2:15", "1 Chronicles 2:25"]
    },
    "ozias": {
        "id": "ozias",
        "term": "Ozias",
        "category": "people",
        "intro": "<p>Ozias is the Greek form of the Hebrew name Uzziah (<em>strength of the LORD</em>), used in Matthew's genealogy of Jesus (Matthew 1:8–9) for the king of Judah known in the Old Testament as Uzziah (2 Chronicles 26) or Azariah (2 Kings 14:21; 15:1–7). He was one of Judah's most capable and prosperous kings — reigning approximately 52 years (c. 792–740 BC), rebuilding Elath, strengthening Jerusalem's fortifications, organizing the army, and expanding Judah's territory — but ended his reign as a leper, struck down when he presumptuously entered the temple to burn incense (2 Chronicles 26:16–21). Isaiah's inaugural vision (Isaiah 6:1) is dated to <em>the year that King Uzziah died.</em></p>",
        "sections": [],
        "hitchcock_meaning": "strength from the Lord",
        "source_ids": {"easton": "ozias"},
        "key_refs": ["Matthew 1:8", "2 Chronicles 26:1", "2 Chronicles 26:16"]
    },
    "ozni": {
        "id": "ozni",
        "term": "Ozni",
        "category": "people",
        "intro": "<p>Ozni (meaning <em>an ear</em> or <em>my hearkening</em>) was a son of Gad and the ancestor of the Oznite clan within the tribe of Gad (Numbers 26:16). He is listed in the second census of Israel in the wilderness. The same individual appears as Ezbon in Genesis 46:16, the parallel list of Gad's sons who went to Egypt — a discrepancy likely due to scribal variation or an alternate name. As a founding clan member of a Gadite family, Ozni's descendants were among those who settled the Transjordan territory east of the Jordan River.</p>",
        "sections": [],
        "hitchcock_meaning": "an ear; my hearkening",
        "source_ids": {"easton": "ozni"},
        "key_refs": ["Numbers 26:16", "Genesis 46:16"]
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
    print(f'BP O: Oak → Ozni: wrote {written}, skipped {skipped} existing.')

if __name__ == '__main__':
    main()
