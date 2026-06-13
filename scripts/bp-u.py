#!/usr/bin/env python3
import json, os

OUT_DIR = '../data/biblepedia/articles'
os.makedirs(OUT_DIR, exist_ok=True)

def merge_article(slug, data):
    path = os.path.join(OUT_DIR, f'{slug}.json')
    if os.path.exists(path):
        return False
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
    return True

ARTICLES = {
"ucal": {
  "id": "ucal",
  "term": "Ucal",
  "category": "people",
  "intro": "<p>Ucal is one of the two named recipients of the words of Agur son of Jakeh in Proverbs 30:1: \"The words of Agur the son of Jakeh, even the prophecy: the man spake unto Ithiel, even unto Ithiel and Ucal.\" Beyond this single verse, nothing is known of Ucal in the canonical Scriptures. Some scholars have proposed that \"Ithiel\" and \"Ucal\" are not personal names but rather Hebrew phrases (<em>\"I have wearied myself, O God\"</em> and <em>\"I am consumed\"</em>), reading the verse as Agur's own confession of exhaustion before God rather than an address to disciples.</p><p>If personal names are intended, Ucal and Ithiel were apparently students or associates to whom Agur directed his wisdom reflections — a form of address common in ancient Near Eastern wisdom literature, where the sage speaks to a named younger person or son.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Proverbs 30:1"]
},
"ulai": {
  "id": "ulai",
  "term": "Ulai",
  "category": "places",
  "intro": "<p>The Ulai (identified with the Eulaeus of Greek writers) was a river or canal of Susiana — the province of ancient Elam centered on Susa — formed by the eastern branch of the Choasper (modern Kerkha) River, which divided approximately twenty miles above its mouth into two channels before joining the Persian Gulf. The Ulai is mentioned in Scripture in connection with Daniel's vision of the ram and the he-goat: Daniel found himself standing \"by the river of Ulai\" when the angel Gabriel appeared to him and interpreted the vision of the two empires (Dan. 8:2, 16).</p><p>The vision at the Ulai — depicting the rise and fall of Medo-Persian and Greek power and looking forward to the \"time of the end\" — is one of the most detailed prophetic visions in the Old Testament. The specific geographical location at Susa, the Persian administrative capital, gives the vision historical concreteness, situating Daniel at the very heart of the empire whose rise and fall he foresaw.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Daniel 8:2", "Daniel 8:16"]
},
"ummah": {
  "id": "ummah",
  "term": "Ummah",
  "category": "places",
  "intro": "<p>Ummah (meaning: <em>vicinity</em> or <em>association</em>) was a town in the tribal allotment of Asher, listed among its border cities in Joshua 19:30. Its precise location has not been positively identified, though some have proposed sites in the Acre plain or the northern coastal region of Galilee where Asher's territory lay. The town is mentioned only in this single boundary list and plays no further role in the biblical narrative.</p><p>The Asher tribal list in Joshua 19:24–31 names twenty-two cities, of which several remain unidentified with confidence. Ummah's obscurity reflects the general challenge of locating minor Galilean settlements from this period, whose ancient names have often been replaced or lost in the subsequent centuries of occupation and settlement.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Joshua 19:30"]
},
"unction": {
  "id": "unction",
  "term": "Unction",
  "category": "concepts",
  "intro": "<p>Unction (from the Latin <em>unctio</em>, anointing) refers to the ritual application of oil as a sign of divine consecration and empowerment. In the Old Testament kings (1 Sam. 10:1), priests (Ex. 28:41), and sometimes prophets (1 Kings 19:16) were anointed with oil as the outward sign of God's Spirit coming upon them for their appointed office. The Messiah himself — the <em>mashiach</em>, the Anointed One — bears this as his defining title.</p><p>In the New Testament John uses the term in its spiritual application: \"But ye have an unction from the Holy One\" (1 John 2:20, 27; Revised Version: \"anointing\"). This unction is the Holy Spirit given to every believer, who teaches and guides them into truth without need of an external intermediary — a democratization of the prophetic anointing that the Old Testament promised for the new covenant age (Joel 2:28). The distinction between the royal/priestly anointing of the few and the spiritual anointing of all believers marks the theological advance from old to new covenant.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["1 John 2:20", "1 John 2:27", "Isaiah 61:1"]
},
"unicorn": {
  "id": "unicorn",
  "term": "Unicorn",
  "category": "concepts",
  "intro": "<p>The \"unicorn\" of the Authorized Version (nine occurrences: Num. 23:22; 24:8; Deut. 33:17; Job 39:9, 10; Ps. 22:21; 29:6; 92:10; Isa. 34:7) translates the Hebrew <em>re'em</em>, which the Revised Version consistently renders as \"wild ox\" (with \"ox-antelope\" in the margin at some places). The <em>re'em</em> was evidently a large, powerful, and untameable animal — described as impossible to domesticate or yoke (Job 39:9–10), associated with great strength (Num. 23:22), and used as an emblem of power in both blessing and judgment. The Septuagint translated it <em>monokeros</em> (one-horned) — the origin of the unicorn tradition in Western translation.</p><p>Modern scholars generally identify the <em>re'em</em> with the aurochs (<em>Bos primigenius</em>), the ancestor of domestic cattle, which was indeed a massive and ferocious wild ox attested in Mesopotamian art as a symbol of royal and divine power. The aurochs was extinct in Palestine by the first millennium B.C. but was known in earlier periods, explaining both its power in folk memory and the difficulty of precise translation.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Numbers 23:22", "Job 39:9", "Deuteronomy 33:17", "Isaiah 34:7"]
},
"unni": {
  "id": "unni",
  "term": "Unni",
  "category": "people",
  "intro": "<p>Unni (meaning: <em>afflicted</em> or <em>humbled of the LORD</em>) is the name of two Levites in the post-exilic period. (1) A Levite whom David appointed to play the psaltery (a stringed instrument) as part of the musical procession bringing the ark of the covenant from the house of Obed-edom to Jerusalem (1 Chr. 15:18, 20). He is listed among the second-rank Levitical musicians appointed for this occasion. (2) A Levite who served in the temple during the time of Zerubbabel and Joshua the high priest, mentioned in Nehemiah 12:9 among those who led in the thanksgiving and prayers opposite their brethren.</p><p>The name's recurrence across two distinct periods reflects the continuity of Levitical musical tradition from David's era through the post-exilic restoration, when the same family structures and musical offices were reconstituted.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["1 Chronicles 15:18", "1 Chronicles 15:20", "Nehemiah 12:9"]
},
"upharsin": {
  "id": "upharsin",
  "term": "Upharsin",
  "category": "concepts",
  "intro": "<p>Upharsin (Aramaic: <em>u-pharsin</em>, meaning <em>and they divide</em>) is the third word of the mysterious inscription written by a supernatural hand on the wall of Belshazzar's palace during his great feast (Dan. 5:25): <em>MENE, MENE, TEKEL, UPHARSIN</em>. It is a plural participle of the Aramaic root <em>paras</em> (to divide or break), closely related to the word <em>Peres</em> (one that divides) which Daniel uses in his interpretation.</p><p>Daniel's reading of the inscription connected the three words to three judgments on Belshazzar: MENE — God has numbered the days of his kingdom and finished it; TEKEL — he has been weighed in the balances and found wanting; PERES (singular of UPHARSIN) — his kingdom is divided and given to the Medes and Persians. The wordplay on PERES also evoked \"Persia\" (<em>Paras</em> in Aramaic), giving the interpretation a prophetic double meaning. That very night Belshazzar was killed (Dan. 5:30).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Daniel 5:25", "Daniel 5:28"]
},
"uphaz": {
  "id": "uphaz",
  "term": "Uphaz",
  "category": "places",
  "intro": "<p>Uphaz is mentioned in Jeremiah 10:9 as a source of fine gold used in the fashioning of idols: \"Silver spread into plates is brought from Tarshish, and gold from Uphaz.\" Daniel 10:5 also uses the phrase \"fine gold of Uphaz\" to describe the brilliant appearance of the angelic figure in Daniel's final vision. The location of Uphaz is uncertain: many scholars identify it with Ophir, the famous gold-producing region reached by Solomon's ships (1 Kings 9:28), suggesting that Uphaz may be a variant spelling or textual variant of Ophir.</p><p>Other proposals place Uphaz in Yemen (southern Arabia) or along the Indian Ocean coast. The Revised Version and several modern translations follow the reading \"Ophir\" rather than \"Uphaz\" in some manuscripts. Whether the two names refer to the same location or to distinct gold sources, both contexts use the gold as a symbol of the highest quality and the greatest wealth.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Jeremiah 10:9", "Daniel 10:5"]
},
"ur": {
  "id": "ur",
  "term": "Ur",
  "category": "places",
  "intro": "<p>Ur of the Chaldees was the birthplace of Abram's father Haran and the city from which Terah led his family on the journey toward Canaan that ended at Haran (Gen. 11:28–31). God's call to Abraham to leave his country and kindred is thus rooted in this departure from Ur, the greatest city of ancient Mesopotamia and a major center of the moon-god Nanna (Sin). Ur lay in southern Babylonia, near the mouth of the Euphrates, and was one of the most sophisticated urban centers of the ancient Near East, with extensive royal tombs, a massive ziggurat, commercial archives, and a literate scribal culture.</p><p>Excavations at Tell el-Muqayyar by Leonard Woolley (1922–1934) uncovered the Royal Cemetery of Ur with its extraordinary grave goods, confirming Ur's wealth and cultural sophistication. Stephen's speech in Acts 7:2–4 places God's call to Abraham as occurring \"in Mesopotamia, before he dwelt in Haran,\" situating the divine summons at Ur itself. Abraham's departure from this prosperous city \"by faith\" (Heb. 11:8) — \"not knowing where he was going\" — became the paradigm of radical obedience to God's call.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Genesis 11:28", "Genesis 11:31", "Acts 7:2", "Hebrews 11:8"]
},
"uriah": {
  "id": "uriah",
  "term": "Uriah",
  "category": "people",
  "intro": "<p>Uriah (meaning: <em>the LORD is my light</em>) is the name of several men in the Old Testament, the most significant being Uriah the Hittite. (1) Uriah the Hittite was a loyal soldier in David's army, one of the thirty mighty men (2 Sam. 23:39), and the husband of Bathsheba. After David committed adultery with Bathsheba, he arranged for Uriah to be placed at the front of the battle and abandoned so that he would be killed — a calculated murder that the prophet Nathan condemned as a grievous sin against God (2 Sam. 11–12). David's subsequent confession (Ps. 51) and the death of his infant son with Bathsheba are the consequences narrated in Scripture. Uriah appears in the genealogy of Jesus (Matt. 1:6) as a reminder of David's sin and God's grace.</p><p>(2) Urijah the high priest in the reign of Ahaz constructed an idolatrous altar on the king's order following a pattern seen in Damascus (2 Kings 16:10–16). (3) A prophet named Urijah son of Shemaiah was killed by Jehoiakim for prophesying against Jerusalem (Jer. 26:20–23). (4) A priest who assisted Ezra at the public reading of the law (Neh. 8:4).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["2 Samuel 11:15", "2 Samuel 12:9", "Matthew 1:6", "Psalms 51:1"]
},
"uriel": {
  "id": "uriel",
  "term": "Uriel",
  "category": "people",
  "intro": "<p>Uriel (meaning: <em>God is my light</em>) is the name of two men in the Old Testament. (1) A Levite of the family of Kohath, ancestor of the prophet Samuel, listed in the genealogy of 1 Chronicles 6:24. (2) The chief of the Kohathites — one hundred and twenty of his brethren — whom David summoned to assist in bringing the ark of the covenant from the house of Obed-edom to Jerusalem (1 Chr. 15:5, 11). This Uriel is the most prominent of the two, as his leadership of the Kohathite levitical order placed him at the center of the great liturgical procession David organized for the ark's transfer.</p><p>A third person named Uriel (or Michaiah, as the son) appears as the father of Maachah (or Michaiah), the favorite wife of King Rehoboam of Judah and mother of Abijah (2 Chr. 13:2). His connection to Gibeah of Benjamin is noted in this reference.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["1 Chronicles 6:24", "1 Chronicles 15:5", "2 Chronicles 13:2"]
},
"urijah": {
  "id": "urijah",
  "term": "Urijah",
  "category": "people",
  "intro": "<p>Urijah (meaning: <em>the LORD is my light</em>) is the name of three persons in the Old Testament. (1) A high priest under King Ahaz of Judah who, at the king's direction, constructed an altar in Jerusalem modeled on one Ahaz had seen in Damascus, and performed the offerings on it before the legitimate bronze altar of the Lord — an act representing the religious apostasy of Ahaz's reign (2 Kings 16:10–16). Isaiah took him as a faithful witness in a legal matter (Isa. 8:2). (2) A prophet son of Shemaiah from Kirjath-jearim who prophesied against Jerusalem and Judah in the same terms as Jeremiah during the reign of Jehoiakim. When Jehoiakim sought to kill him, Urijah fled to Egypt but was extradited and executed, his body thrown into a common grave (Jer. 26:20–23). (3) A priest who stood with Ezra when he read the law to the assembled people after the return from exile (Neh. 8:4).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["2 Kings 16:10", "Jeremiah 26:20", "Nehemiah 8:4"]
},
"urim": {
  "id": "urim",
  "term": "Urim",
  "category": "concepts",
  "intro": "<p>The Urim (meaning: <em>lights</em>) were part of the sacred divinatory objects — the Urim and Thummim — placed in the breastplate of the high priest and used to determine the divine will in matters of national importance (Ex. 28:30; Lev. 8:8; Num. 27:21; Deut. 33:8). The precise nature of the Urim and Thummim is unknown: proposals include two stones or lots that gave binary (yes/no) answers, a set of twelve stones associated with the twelve tribes, or sacred objects of unknown form. The Septuagint renders Urim and Thummim as \"revelation\" and \"truth\" (or \"manifestation\" and \"truth\"), suggesting an oracular function.</p><p>The Urim and Thummim were used throughout the period of the Judges and early monarchy — Joshua inquired of God through the priest Eleazar using the Urim (Num. 27:21), and Saul's failure to receive an answer via Urim at Gilboa signaled divine abandonment (1 Sam. 28:6). They were absent from the second temple but expected to return in the messianic age (Ezra 2:63; Neh. 7:65). Their function was replaced in the new covenant era by the indwelling Spirit and the completed prophetic word.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Exodus 28:30", "Numbers 27:21", "1 Samuel 28:6", "Ezra 2:63"]
},
"usury": {
  "id": "usury",
  "term": "Usury",
  "category": "concepts",
  "intro": "<p>Usury in biblical usage means simply interest — the sum paid for the use of borrowed money — not the modern sense of excessive or predatory interest. The Mosaic law absolutely forbade Israelites from charging interest on loans to fellow Israelites, whether money, food, or anything else (Lev. 25:35–37; Deut. 23:19), grounding this prohibition in the covenantal obligation of solidarity: within the covenant community, the poor were not to be exploited through debt. Interest could lawfully be charged to foreigners (<em>nokrim</em>), who stood outside this covenant relationship (Deut. 23:20).</p><p>The prophets condemned usury as a mark of covenant violation and social injustice (Ezek. 18:8; 22:12; Neh. 5:7–10). The Psalms declare that the righteous man lends without interest (Ps. 15:5). In the New Testament, Jesus's parable of the talents has a master expecting his money back \"with usury\" (Matt. 25:27; Luke 19:23) — here the word simply means financial return, with no moral judgment implied on interest itself in commercial contexts. The parable's point is spiritual fruitfulness, not economic policy.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Leviticus 25:36", "Deuteronomy 23:19", "Ezekiel 18:8", "Psalms 15:5"]
},
"uz": {
  "id": "uz",
  "term": "Uz",
  "category": "people",
  "intro": "<p>Uz is the name of three persons in the Old Testament, each representing distinct lineages. (1) The son of Aram and grandson of Shem (Gen. 10:23; 1 Chr. 1:17), an ancestor of the Aramean peoples — the eponymous founder of a Semitic tribe. (2) One of the Horite chieftains (\"dukes\") in the land of Edom, a son of Dishan (Gen. 36:28). (3) A son of Nahor by his concubine Reumah (Gen. 22:21), a nephew of Abraham and ancestor of another Aramean group.</p><p>The name Uz also designates the land where Job lived (Job 1:1), which was probably named after one of these eponymous ancestors — most likely the Aramean Uz, placing the land east or southeast of Palestine in or near the territory of Edom and northern Arabia (see Lam. 4:21; Jer. 25:20). The diverse genealogical uses of the name illustrate the ancient practice of naming regions after ancestral founders.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Genesis 10:23", "Genesis 22:21", "Genesis 36:28", "Job 1:1"]
},
"uz-the-land-of": {
  "id": "uz-the-land-of",
  "term": "Uz, Land of",
  "category": "places",
  "intro": "<p>The land of Uz was the homeland of Job (Job 1:1), situated somewhere east or southeast of Palestine. Its precise location is debated, but the biblical evidence suggests a region bordering on or overlapping with Edom: Lamentations 4:21 addresses the \"daughter of Edom that dwellest in the land of Uz,\" and Jeremiah 25:20 lists the \"kings of the land of Uz\" alongside kings of Philistia, Edom, Moab, and Ammon, placing it in the Transjordanian or Edomite sphere.</p><p>The land of Uz was thus probably located in the region east of the Jordan and the Dead Sea — the territory of northern Arabia or the desert frontier between Edom and the Aramean lands. Its semi-arid, pastoral character fits the description of Job's wealth in flocks and herds, and the Sabeans and Chaldeans who raided his livestock suggest a position along the caravan routes between Arabia and Mesopotamia.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["Job 1:1", "Jeremiah 25:20", "Lamentations 4:21"]
},
"uzal": {
  "id": "uzal",
  "term": "Uzal",
  "category": "places",
  "intro": "<p>Uzal (meaning: <em>a wanderer</em>) was a descendant of Joktan son of Eber, listed in the Table of Nations (Gen. 10:27; 1 Chr. 1:21) as one of the founders of the South Arabian peoples. Uzal is generally identified with the ancient capital of Yemen — Sanaa (Arabic: <em>Azal</em>), which retained the ancient name in its Arabic form. Ezekiel 27:19 mentions Vedan and Javan from Uzal trading bright iron, cassia, and calamus with Tyre, confirming Uzal's association with the Arabian trade in luxury goods.</p><p>The identification of Uzal with the Yemeni capital makes it one of the better-established geographical identifications in the Table of Nations, linking the biblical genealogy to a historically continuous city. Its trade goods — iron and spices — reflect the prosperity of pre-Islamic South Arabia as a commercial crossroads between the Indian Ocean and the Mediterranean world.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Genesis 10:27", "Ezekiel 27:19"]
},
"uzza": {
  "id": "uzza",
  "term": "Uzza",
  "category": "places",
  "intro": "<p>Uzza (meaning: <em>strength</em>) was the name of a garden in Jerusalem in which kings Manasseh and his son Amon were buried (2 Kings 21:18, 26). The garden was probably near the royal palace in the southern part of Jerusalem, and may have been part of the palace grounds rather than a separate public garden. The burial of Manasseh in his own house's garden rather than in the royal tombs of the City of David may reflect a mark of partial disfavor or simply the practice of late monarchy burial customs.</p><p>The garden name Uzza is also the name of several people in the Old Testament (most notably Uzzah son of Abinadab — see Uzzah), reflecting the common Hebrew root meaning of strength. The garden's association with the burial of two notably wicked kings — Manasseh, who filled Jerusalem with innocent blood (2 Kings 21:16), and Amon, who forsook God entirely — gives it a somber place in the history of the Judean monarchy.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["2 Kings 21:18", "2 Kings 21:26"]
},
"uzzah": {
  "id": "uzzah",
  "term": "Uzzah",
  "category": "people",
  "intro": "<p>Uzzah (meaning: <em>strength</em>) was the son of Abinadab of Kirjath-jearim, in whose house the ark of the covenant had been kept for twenty years after its return from Philistia (1 Sam. 7:1). When David organized a great procession to bring the ark up to Jerusalem on a new cart, Uzzah walked alongside it. When the oxen stumbled and the ark threatened to fall, Uzzah reached out and took hold of the ark to steady it — and God struck him dead on the spot (2 Sam. 6:6–7; 1 Chr. 13:9–10). The place was called Perez-uzzah (\"the breach of Uzzah\") in memory of the event.</p><p>The death of Uzzah is one of the most troubling episodes in the Old Testament for modern readers. The theological point is the absolute holiness of God's presence and the strict Levitical regulations governing the ark's transport (Num. 4:15): only the Kohathite Levites were to carry it on poles inserted through its rings; it was not to be placed on a cart nor touched even by Levites under penalty of death. David's failure to follow these instructions — adopting the Philistine model of transport — was the root cause. The incident prompted David to investigate the law of God more carefully before the second, successful procession (1 Chr. 15:2, 13).</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["2 Samuel 6:6", "1 Chronicles 13:10", "Numbers 4:15", "1 Chronicles 15:13"]
},
"uzzen-sherah": {
  "id": "uzzen-sherah",
  "term": "Uzzen-sherah",
  "category": "places",
  "intro": "<p>Uzzen-sherah (meaning: <em>the portion of Sherah</em> or <em>the ear of Sherah</em>) was a town built or named after Sherah, the daughter of Ephraim's son Beriah — or possibly of Ephraim directly (1 Chr. 7:24). Sherah is one of the few women in the Old Testament credited with founding or building towns: she built both the lower and upper Beth-horon and Uzzen-sherah. The location of Uzzen-sherah is uncertain, but it lay in the vicinity of Beth-horon in the territory of Ephraim, in the hill country west of Bethel.</p><p>The mention of Sherah as a builder reflects the occasional presence of women as significant figures in the settlement and construction of Ephraimite territory, a role otherwise rare in the tribal records of Joshua and Chronicles. Uzzen-sherah's identification with a specific daughter of the tribe preserves a fragment of early Israelite social history.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton"],
  "key_refs": ["1 Chronicles 7:24"]
},
"uzzi": {
  "id": "uzzi",
  "term": "Uzzi",
  "category": "people",
  "intro": "<p>Uzzi (meaning: <em>the LORD is my strength</em>) is the name of several persons in the Old Testament. (1) The son of Bukki and a descendant of Aaron in the high-priestly line, listed in both 1 Chronicles 6:5–6, 51 and Ezra 7:4 as an ancestor of Ezra. (2) A grandson of Issachar through Tola, who is listed as a mighty man of valor whose descendants numbered 22,600 fighting men at the time of David's census (1 Chr. 7:2–3). (3) A son of Bela of Benjamin (1 Chr. 7:7). (4) A Benjaminite who was the father of Elah, a post-exilic settler in Jerusalem (1 Chr. 9:8). (5) A Levite overseer of the Levites who dwelt in Jerusalem, son of Bani, in Nehemiah's time (Neh. 11:22). (6) A priest who participated in the dedication of the rebuilt walls of Jerusalem (Neh. 12:42).</p><p>The frequency of the name Uzzi across multiple tribes and periods reflects its theological meaning's broad appeal as an affirmation of divine strength.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["1 Chronicles 6:5", "Ezra 7:4", "Nehemiah 11:22", "Nehemiah 12:42"]
},
"uzziah": {
  "id": "uzziah",
  "term": "Uzziah",
  "category": "people",
  "intro": "<p>Uzziah (also called Azariah; meaning: <em>the LORD is my strength</em>) was king of Judah for fifty-two years (c. 792–740 B.C.), one of the longest reigns in Judah's history, succeeding his father Amaziah at age sixteen (2 Kings 14:21; 2 Chr. 26:1). During his long reign he strengthened the kingdom militarily, subdued the Philistines and Ammonites, rebuilt Elath, reorganized the army with sophisticated weapons, and promoted agriculture. \"His name spread far abroad; for he was marvellously helped, till he was strong\" (2 Chr. 26:15).</p><p>Uzziah's downfall came when he presumed to burn incense in the temple — an act reserved for priests — in violation of the Mosaic law. The priests confronted him; he responded in anger; and God struck him with leprosy on his forehead as he stood in the sanctuary. He remained a leper until his death, living in a separate house while his son Jotham co-reigned (2 Chr. 26:16–23; 2 Kings 15:5). Isaiah's inaugural vision came \"in the year that king Uzziah died\" (Isa. 6:1), marking the end of an era. Amos, Hosea, and Isaiah all prophesied during his reign.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["2 Chronicles 26:1", "2 Chronicles 26:16", "2 Kings 15:5", "Isaiah 6:1"]
},
"uzziel": {
  "id": "uzziel",
  "term": "Uzziel",
  "category": "people",
  "intro": "<p>Uzziel (meaning: <em>strength of God</em>) is the name of several persons in the Old Testament. (1) The fourth son of Kohath and grandson of Levi, and therefore uncle of Aaron and Moses (Ex. 6:18; Lev. 10:4). His descendants — the Uzzielites — formed one of the four divisions of the Kohathite Levites responsible for carrying the most sacred objects of the tabernacle (Num. 3:30). (2) A Simeonite captain who led 500 men against the remnant of Amalekites on Mount Seir in the days of Hezekiah (1 Chr. 4:39–43). (3) A son of Bela of Benjamin (1 Chr. 7:7). (4) One of David's musicians, a son of Heman (1 Chr. 25:4), leader of the twenty-fourth priestly division. (5) A Levite who assisted Hezekiah in cleansing and reopening the temple (2 Chr. 29:14). (6) A goldsmith who repaired a section of Jerusalem's wall under Nehemiah (Neh. 3:8).</p><p>The Kohathite Uzziel and his descendants are the most significant biblically, as the Uzzielites' role in bearing the ark and its furnishings placed them at the heart of Israel's sanctuary service.</p>",
  "sections": [],
  "hitchcock_meaning": "",
  "source_ids": ["easton", "smith"],
  "key_refs": ["Exodus 6:18", "Numbers 3:30", "2 Chronicles 26:1", "Nehemiah 3:8"]
},
}

def main():
    written = skipped = 0
    for slug, data in ARTICLES.items():
        if merge_article(slug, data):
            written += 1
        else:
            skipped += 1
    print(f"BP u: Ucal → Uzziel: wrote {written}, skipped {skipped} existing.")

main()
