"""
MKT 1 Chronicles chapters 6–10 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-1chronicles-6-10.py

Content:
- Ch 6: Levitical genealogies — high priestly line (vv.1–15), Levitical families (vv.16–30),
  temple singers (vv.31–47), Aaronic altar service (vv.48–53), Levitical cities (vv.54–81)
- Ch 7: Tribal genealogies — Issachar, Benjamin, Naphtali, Manasseh, Ephraim, Asher
- Ch 8: Benjaminite genealogy, culminating in Saul's lineage
- Ch 9: Post-exilic Jerusalem inhabitants; temple personnel; Saul genealogy repeated
- Ch 10: Saul's death at Gilboa — narrative and theological verdict (vv.13–14)

Translation decisions:
- H3068 (יהוה): "LORD" in L/M; "the LORD" in T. Consistent with all prior OT scripts.
- H430 (אֱלֹהִים): "God" throughout all tiers.
- H3205 (ילד hiphil "begat"): "fathered" in L/M/T. Avoids archaic "begat."
- H4054 (מִגְרָשׁ): "open pasturelands" in L; "pasturelands" in M/T. KJV "suburbs" is archaic;
  the term refers to the common grazing land around each Levitical city (cf. Num 35:2–5).
- H4733 (מִקְלָט "city of refuge"): "city of refuge" / "cities of refuge" in all tiers.
- H7891/H7892 (שִׁיר/שָׁרַר "song/singer"): "singer" in L/M; "cantor" in T when leading
  formal temple worship; "song" for the abstract noun.
- H5975 (עָמַד "stood/stationed"): "stood" in L/M; "were stationed" in T (Levitical service).
- H6635 (צָבָא): in Levitical context = "service/duty"; in military context = "army/forces."
- H898 (בָּגַד "act treacherously/unfaithfully") at 10:13: "acted unfaithfully" in L/M;
  "broke faith" in T. This is the Chronicler's theological verdict on Saul's entire reign.
- H1875 (דָּרַשׁ "inquire/seek") at 10:13–14: "inquire of" in L/M; "seek the LORD" in T.
  Saul consulted a medium instead — the contrast is the heart of the indictment.
- H178 (אוֹב "medium/familiar spirit") at 10:13: "medium" in L/M; "ghost-diviner" in T
  (one who consults the dead, explicitly forbidden, Lev 19:31, Deut 18:11).
- H4191 (מוּת "die"): "put him to death" in L/M at 10:14; "struck him down" in T.
- Aspect: all genealogical chains use qatals = simple past throughout. Ch 10 uses
  waw-consecutive imperfects = narrative past. The theological summary (10:13–14) uses
  qatals in retrospective summary — T gives these full weight.

OT intertextuality:
- 6:33: Heman traces through Joel to Samuel (the prophet). T notes this at v.33.
- 6:39: Asaph is the founder of the Asaph psalms (Ps 50, 73–83). T notes at v.39.
- 6:44: Ethan/Jeduthun is associated with Ps 89. T notes at v.44.
- 6:49: Aaron's altar service echoes Num 18 — the Aaronic covenant of salt.
- 6:54: Levitical cities repeat Josh 21 almost verbatim. T notes this echo at v.54.
- 9:1: The exile editorial note frames the entire 9-chapter genealogical prologue.
- 9:19: Phinehas son of Eleazar connects temple gatekeeping to Num 25 (his zeal turned
  away God's wrath). T notes at v.19.
- 10:13–14: The Chronicler adds this theological commentary not found in 1 Sam 31. It
  echoes Deut 17:14–20 (the king's law) and 1 Sam 28 (Saul and the medium). T surfaces both.
"""

import json, pathlib

ROOT  = pathlib.Path(__file__).parent.parent
DRAFT = ROOT / 'data' / 'translation' / 'draft'

def load(tier, book):
    p = DRAFT / tier / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save(tier, book, data):
    p = DRAFT / tier / f'{book}.json'
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_tier(existing, new_data, tier_key):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, tiers in verses.items():
            existing[ch][v] = tiers[tier_key]

CHRONICLES1 = {
  "6": {
    "1": {
      "L": "The sons of Levi: Gershom, Kohath, and Merari.",
      "M": "The sons of Levi were Gershom, Kohath, and Merari.",
      "T": "Levi had three sons — Gershom, Kohath, and Merari — who became the founding clans of Israel's entire priestly and Levitical order."
    },
    "2": {
      "L": "And the sons of Kohath: Amram, Izhar, and Hebron and Uzziel.",
      "M": "The sons of Kohath were Amram, Izhar, Hebron, and Uzziel.",
      "T": "Kohath's four sons — Amram, Izhar, Hebron, and Uzziel — would produce Moses, Aaron, and the Levitical leaders of the wilderness generation."
    },
    "3": {
      "L": "And the children of Amram: Aaron and Moses and Miriam. And the sons of Aaron: Nadab and Abihu, Eleazar and Ithamar.",
      "M": "The children of Amram were Aaron, Moses, and Miriam. The sons of Aaron were Nadab, Abihu, Eleazar, and Ithamar.",
      "T": "Amram's children were Aaron, Moses, and Miriam — the three leaders of the exodus. Aaron's four sons were Nadab, Abihu, Eleazar, and Ithamar, though Nadab and Abihu died offering unauthorized fire before the LORD."
    },
    "4": {
      "L": "Eleazar fathered Phinehas, Phinehas fathered Abishua.",
      "M": "Eleazar fathered Phinehas, and Phinehas fathered Abishua.",
      "T": "From Eleazar came Phinehas — whose zeal at Baal-peor secured the priesthood for his line — and from Phinehas came Abishua."
    },
    "5": {
      "L": "And Abishua fathered Bukki, and Bukki fathered Uzzi.",
      "M": "Abishua fathered Bukki, and Bukki fathered Uzzi.",
      "T": "Abishua's line continued through Bukki to Uzzi."
    },
    "6": {
      "L": "And Uzzi fathered Zerahiah, and Zerahiah fathered Meraioth.",
      "M": "Uzzi fathered Zerahiah, and Zerahiah fathered Meraioth.",
      "T": "Uzzi fathered Zerahiah, and Zerahiah fathered Meraioth."
    },
    "7": {
      "L": "Meraioth fathered Amariah, and Amariah fathered Ahitub.",
      "M": "Meraioth fathered Amariah, and Amariah fathered Ahitub.",
      "T": "Meraioth fathered Amariah, and Amariah fathered Ahitub."
    },
    "8": {
      "L": "And Ahitub fathered Zadok, and Zadok fathered Ahimaaz.",
      "M": "Ahitub fathered Zadok, and Zadok fathered Ahimaaz.",
      "T": "Ahitub fathered Zadok — the great high priest of David and Solomon — and Zadok fathered Ahimaaz."
    },
    "9": {
      "L": "And Ahimaaz fathered Azariah, and Azariah fathered Johanan.",
      "M": "Ahimaaz fathered Azariah, and Azariah fathered Johanan.",
      "T": "Ahimaaz fathered Azariah, and Azariah fathered Johanan."
    },
    "10": {
      "L": "And Johanan fathered Azariah — it was he who served as priest in the house that Solomon built in Jerusalem.",
      "M": "Johanan fathered Azariah, who served as priest in the temple that Solomon built in Jerusalem.",
      "T": "Johanan fathered Azariah — an editorial note marks this Azariah as the one who exercised the priesthood in Solomon's newly built temple in Jerusalem."
    },
    "11": {
      "L": "And Azariah fathered Amariah, and Amariah fathered Ahitub.",
      "M": "Azariah fathered Amariah, and Amariah fathered Ahitub.",
      "T": "The line continued: Azariah fathered Amariah, and Amariah fathered Ahitub."
    },
    "12": {
      "L": "And Ahitub fathered Zadok, and Zadok fathered Shallum.",
      "M": "Ahitub fathered Zadok, and Zadok fathered Shallum.",
      "T": "Ahitub fathered Zadok, and Zadok fathered Shallum."
    },
    "13": {
      "L": "And Shallum fathered Hilkiah, and Hilkiah fathered Azariah.",
      "M": "Shallum fathered Hilkiah, and Hilkiah fathered Azariah.",
      "T": "Shallum fathered Hilkiah — the high priest who discovered the lost book of the Law in Josiah's day — and Hilkiah fathered Azariah."
    },
    "14": {
      "L": "And Azariah fathered Seraiah, and Seraiah fathered Jehozadak.",
      "M": "Azariah fathered Seraiah, and Seraiah fathered Jehozadak.",
      "T": "Azariah fathered Seraiah — the chief priest executed by Nebuchadnezzar at Riblah — and Seraiah fathered Jehozadak."
    },
    "15": {
      "L": "And Jehozadak went into exile when the LORD carried away Judah and Jerusalem by the hand of Nebuchadnezzar.",
      "M": "Jehozadak went into exile when the LORD sent Judah and Jerusalem into captivity by the hand of Nebuchadnezzar.",
      "T": "Jehozadak was taken into exile when the LORD drove Judah and Jerusalem away by the hand of Nebuchadnezzar — the priestly line itself going captive, the sanctuary's service suspended."
    },
    "16": {
      "L": "The sons of Levi: Gershom, Kohath, and Merari.",
      "M": "The sons of Levi were Gershom, Kohath, and Merari.",
      "T": "The three clans of Levi — Gershom, Kohath, and Merari — are now traced in their extended sub-families."
    },
    "17": {
      "L": "And these are the names of the sons of Gershom: Libni and Shimei.",
      "M": "These are the names of the sons of Gershom: Libni and Shimei.",
      "T": "Gershom's two sons were Libni and Shimei, heads of Gershomite sub-clans."
    },
    "18": {
      "L": "And the sons of Kohath were: Amram, and Izhar, and Hebron, and Uzziel.",
      "M": "The sons of Kohath were Amram, Izhar, Hebron, and Uzziel.",
      "T": "Kohath's four sons — Amram, Izhar, Hebron, and Uzziel — are enumerated again, the pivot clan of the whole Levitical system."
    },
    "19": {
      "L": "The sons of Merari: Mahli and Mushi. And these are the families of the Levites according to their fathers.",
      "M": "The sons of Merari were Mahli and Mushi. These are the Levitical families according to their fathers.",
      "T": "Merari's sons were Mahli and Mushi. Together, these three clans with their sub-families constitute the full Levitical inheritance that Israel would sustain in every generation."
    },
    "20": {
      "L": "Of Gershom: Libni his son, Jahath his son, Zimmah his son,",
      "M": "From Gershom: his son Libni, his son Jahath, his son Zimmah,",
      "T": "The Gershomite descent runs: Gershom → Libni → Jahath → Zimmah,"
    },
    "21": {
      "L": "Joah his son, Iddo his son, Zerah his son, Jeaterai his son.",
      "M": "his son Joah, his son Iddo, his son Zerah, his son Jeaterai.",
      "T": "continuing through Joah → Iddo → Zerah → Jeaterai."
    },
    "22": {
      "L": "The sons of Kohath: Amminadab his son, Korah his son, Assir his son,",
      "M": "From Kohath: his son Amminadab, his son Korah, his son Assir,",
      "T": "The Kohathite line runs: Kohath → Amminadab → Korah → Assir — this is the Korah of the wilderness rebellion, yet his descendants survived and served in the sanctuary."
    },
    "23": {
      "L": "Elkanah his son, and Ebiasaph his son, and Assir his son,",
      "M": "his son Elkanah, his son Ebiasaph, his son Assir,",
      "T": "then Elkanah → Ebiasaph → Assir,"
    },
    "24": {
      "L": "Tahath his son, Uriel his son, Uzziah his son, and Shaul his son.",
      "M": "his son Tahath, his son Uriel, his son Uzziah, his son Shaul.",
      "T": "then Tahath → Uriel → Uzziah → Shaul."
    },
    "25": {
      "L": "And the sons of Elkanah: Amasai and Ahimoth.",
      "M": "The sons of Elkanah were Amasai and Ahimoth.",
      "T": "Elkanah had two sons: Amasai and Ahimoth."
    },
    "26": {
      "L": "As for Elkanah: the sons of Elkanah — Zophai his son, and Nahath his son,",
      "M": "Of Elkanah: his son Zophai, his son Nahath,",
      "T": "A further Elkanah line continues: Zophai → Nahath,"
    },
    "27": {
      "L": "Eliab his son, Jeroham his son, Elkanah his son.",
      "M": "his son Eliab, his son Jeroham, his son Elkanah.",
      "T": "then Eliab → Jeroham → Elkanah."
    },
    "28": {
      "L": "And the sons of Samuel: the firstborn Vashni, and Abijah.",
      "M": "The sons of Samuel were the firstborn Vashni and Abijah.",
      "T": "Samuel's sons were Vashni the firstborn and Abijah — the same sons who, serving as judges, took bribes and perverted justice, prompting Israel to demand a king."
    },
    "29": {
      "L": "The sons of Merari: Mahli, Libni his son, Shimei his son, Uzza his son,",
      "M": "From Merari: his son Mahli, his son Libni, his son Shimei, his son Uzza,",
      "T": "The Merari line runs: Merari → Mahli → Libni → Shimei → Uzza,"
    },
    "30": {
      "L": "Shimea his son, Haggiah his son, Asaiah his son.",
      "M": "his son Shimea, his son Haggiah, his son Asaiah.",
      "T": "continuing through Shimea → Haggiah → Asaiah."
    },
    "31": {
      "L": "And these are they whom David set over the service of song in the house of the LORD after the ark had rest.",
      "M": "These are the men David appointed over the service of song in the house of the LORD, after the ark had found its resting place.",
      "T": "Once the ark of the LORD had been brought to rest in Jerusalem, David organized the entire liturgy of song — appointing these men as the official ministers of worship in the LORD's house."
    },
    "32": {
      "L": "And they ministered before the tabernacle of the tent of meeting with song until Solomon built the house of the LORD in Jerusalem; and they performed their service according to their order.",
      "M": "They ministered with song before the tabernacle of the tent of meeting until Solomon built the house of the LORD in Jerusalem, and they served according to their prescribed order.",
      "T": "For the duration of the tabernacle era, these singers led worship at the tent of meeting — and when Solomon's temple replaced it, the same order of worship continued without interruption, the music flowing from tent to temple."
    },
    "33": {
      "L": "And these are they who stood with their sons: from the sons of the Kohathites — Heman the singer, the son of Joel, the son of Samuel,",
      "M": "These are the ones who served with their sons: from the Kohathites, Heman the singer, son of Joel, son of Samuel,",
      "T": "The lead cantor from Kohath's line was Heman — his genealogy traces back through Joel to Samuel the prophet himself, linking Israel's greatest musical tradition to its greatest judicial and prophetic figure."
    },
    "34": {
      "L": "the son of Elkanah, the son of Jeroham, the son of Eliel, the son of Toah,",
      "M": "son of Elkanah, son of Jeroham, son of Eliel, son of Toah,",
      "T": "son of Elkanah, son of Jeroham, son of Eliel, son of Toah,"
    },
    "35": {
      "L": "the son of Zuph, the son of Elkanah, the son of Mahath, the son of Amasai,",
      "M": "son of Zuph, son of Elkanah, son of Mahath, son of Amasai,",
      "T": "son of Zuph, son of Elkanah, son of Mahath, son of Amasai,"
    },
    "36": {
      "L": "the son of Elkanah, the son of Joel, the son of Azariah, the son of Zephaniah,",
      "M": "son of Elkanah, son of Joel, son of Azariah, son of Zephaniah,",
      "T": "son of Elkanah, son of Joel, son of Azariah, son of Zephaniah,"
    },
    "37": {
      "L": "the son of Tahath, the son of Assir, the son of Ebiasaph, the son of Korah,",
      "M": "son of Tahath, son of Assir, son of Ebiasaph, son of Korah,",
      "T": "son of Tahath, son of Assir, son of Ebiasaph, son of Korah — tracing back through the very rebels of the wilderness."
    },
    "38": {
      "L": "the son of Izhar, the son of Kohath, the son of Levi, the son of Israel.",
      "M": "son of Izhar, son of Kohath, son of Levi, son of Israel.",
      "T": "son of Izhar, son of Kohath, son of Levi, son of Israel — Heman's line runs all the way back to the patriarch Jacob, anchoring Israel's worship in its founding covenant."
    },
    "39": {
      "L": "And his brother Asaph stood at his right hand — Asaph the son of Berechiah, the son of Shimea,",
      "M": "His colleague Asaph stood at his right hand: Asaph son of Berechiah, son of Shimea,",
      "T": "At Heman's right hand stood Asaph — the founder of the Asaphite psalm tradition (Psalms 50 and 73–83), son of Berechiah, son of Shimea,"
    },
    "40": {
      "L": "the son of Michael, the son of Baaseiah, the son of Malchijah,",
      "M": "son of Michael, son of Baaseiah, son of Malchijah,",
      "T": "son of Michael, son of Baaseiah, son of Malchijah,"
    },
    "41": {
      "L": "the son of Ethni, the son of Zerah, the son of Adaiah,",
      "M": "son of Ethni, son of Zerah, son of Adaiah,",
      "T": "son of Ethni, son of Zerah, son of Adaiah,"
    },
    "42": {
      "L": "the son of Ethan, the son of Zimmah, the son of Shimei,",
      "M": "son of Ethan, son of Zimmah, son of Shimei,",
      "T": "son of Ethan, son of Zimmah, son of Shimei,"
    },
    "43": {
      "L": "the son of Jahath, the son of Gershom, the son of Levi.",
      "M": "son of Jahath, son of Gershom, son of Levi.",
      "T": "son of Jahath, son of Gershom, son of Levi — Asaph's line runs through Gershom, Levi's firstborn."
    },
    "44": {
      "L": "And their brothers the sons of Merari stood at the left hand: Ethan the son of Kishi, the son of Abdi, the son of Malluch,",
      "M": "Their colleagues from the sons of Merari stood at the left hand: Ethan son of Kishi, son of Abdi, son of Malluch,",
      "T": "On Heman's left stood Ethan — the Merarite cantor associated with Psalm 89, the great lament over the Davidic covenant — son of Kishi, son of Abdi, son of Malluch,"
    },
    "45": {
      "L": "the son of Hashabiah, the son of Amaziah, the son of Hilkiah,",
      "M": "son of Hashabiah, son of Amaziah, son of Hilkiah,",
      "T": "son of Hashabiah, son of Amaziah, son of Hilkiah,"
    },
    "46": {
      "L": "the son of Amzi, the son of Bani, the son of Shamer,",
      "M": "son of Amzi, son of Bani, son of Shamer,",
      "T": "son of Amzi, son of Bani, son of Shamer,"
    },
    "47": {
      "L": "the son of Mahli, the son of Mushi, the son of Merari, the son of Levi.",
      "M": "son of Mahli, son of Mushi, son of Merari, son of Levi.",
      "T": "son of Mahli, son of Mushi, son of Merari, son of Levi — three cantors, three Levitical clans, one unified act of praise before the ark."
    },
    "48": {
      "L": "Their brothers also, the Levites, were appointed to all the service of the tabernacle of the house of God.",
      "M": "Their fellow Levites were appointed to all the other service of the tabernacle, the house of God.",
      "T": "Beyond the singers, every other task of the LORD's tabernacle — carrying, setting up, maintaining — was assigned to Levites according to their clans."
    },
    "49": {
      "L": "But Aaron and his sons offered on the altar of burnt offering and on the altar of incense, for all the work of the Most Holy Place, and to make atonement for Israel, according to all that Moses the servant of God had commanded.",
      "M": "But Aaron and his sons were responsible for sacrifices on the altar of burnt offering and the altar of incense, for all the service of the Most Holy Place, and for making atonement for Israel — exactly as Moses the servant of God had commanded.",
      "T": "The altar itself and the Most Holy Place belonged to Aaron's sons alone — the atonement-work that stood between Israel and God's consuming holiness, carried out precisely as Moses had been commanded, an unbroken chain of sacred service."
    },
    "50": {
      "L": "And these are the sons of Aaron: Eleazar his son, Phinehas his son, Abishua his son,",
      "M": "These are the sons of Aaron: his son Eleazar, his son Phinehas, his son Abishua,",
      "T": "Aaron's priestly line runs: Aaron → Eleazar → Phinehas → Abishua,"
    },
    "51": {
      "L": "Bukki his son, Uzzi his son, Zerahiah his son,",
      "M": "his son Bukki, his son Uzzi, his son Zerahiah,",
      "T": "then Bukki → Uzzi → Zerahiah,"
    },
    "52": {
      "L": "Meraioth his son, Amariah his son, Ahitub his son,",
      "M": "his son Meraioth, his son Amariah, his son Ahitub,",
      "T": "then Meraioth → Amariah → Ahitub,"
    },
    "53": {
      "L": "Zadok his son, Ahimaaz his son.",
      "M": "his son Zadok, his son Ahimaaz.",
      "T": "then Zadok → Ahimaaz — the high priestly chain reaching from Aaron's sons in the wilderness to the founding of Solomon's temple."
    },
    "54": {
      "L": "Now these are their dwelling places according to their settlements in their territory: to the sons of Aaron of the families of the Kohathites, for theirs was the first lot —",
      "M": "These are their dwelling places according to their allotted territories: the sons of Aaron from the Kohathite families received the first lot —",
      "T": "The Levitical cities are now listed — a near-repeat of Joshua 21, showing the Chronicler's readers that what Joshua established endures. Aaron's Kohathite descendants received the first allocation:"
    },
    "55": {
      "L": "they gave them Hebron in the land of Judah and the open pasturelands surrounding it.",
      "M": "they gave them Hebron in the land of Judah with its surrounding pasturelands.",
      "T": "They received Hebron in Judah with all its surrounding pasturelands — the city of the patriarchs, of Caleb, of David's early kingship, now a priestly city."
    },
    "56": {
      "L": "But the fields of the city and its villages they gave to Caleb the son of Jephunneh.",
      "M": "The open fields and villages of Hebron, however, were given to Caleb son of Jephunneh.",
      "T": "The farmland and outlying villages of Hebron remained Caleb's inheritance — the priests received the city walls and pasturelands, but Caleb's family retained the productive land."
    },
    "57": {
      "L": "To the sons of Aaron they gave the cities of refuge: Hebron, Libnah with its pasturelands, Jattir, and Eshtemoa with its pasturelands,",
      "M": "The sons of Aaron received the cities of refuge: Hebron, Libnah with its pasturelands, Jattir, and Eshtemoa with its pasturelands,",
      "T": "Aaron's sons were assigned cities of refuge — Hebron, Libnah with its pasturelands, Jattir, and Eshtemoa with its pasturelands,"
    },
    "58": {
      "L": "and Hilen with its pasturelands, Debir with its pasturelands,",
      "M": "Hilen with its pasturelands and Debir with its pasturelands,",
      "T": "Hilen and Debir, each with pasturelands,"
    },
    "59": {
      "L": "and Ashan with its pasturelands and Beth-shemesh with its pasturelands.",
      "M": "Ashan with its pasturelands and Beth-shemesh with its pasturelands.",
      "T": "and Ashan and Beth-shemesh, each with pasturelands — towns scattered across Judah to give the priestly families access throughout the tribe."
    },
    "60": {
      "L": "And from the tribe of Benjamin: Geba with its pasturelands, and Alemeth with its pasturelands, and Anathoth with its pasturelands. All their cities throughout their families were thirteen cities.",
      "M": "From the tribe of Benjamin: Geba, Alemeth, and Anathoth, each with its pasturelands. All together, their cities throughout their families were thirteen.",
      "T": "From Benjamin came three more priestly cities — Geba, Alemeth, and Anathoth (later the home of the prophet Jeremiah) — bringing the total to thirteen cities for Aaron's priestly families."
    },
    "61": {
      "L": "And to the rest of the sons of Kohath were given by lot from the tribe of the half-tribe of Manasseh ten cities.",
      "M": "The remaining sons of Kohath received by lot ten cities from the half-tribe of Manasseh.",
      "T": "The non-Aaronic Kohathites — those not in the priestly line — were assigned ten cities by lot from the half-tribe of Manasseh."
    },
    "62": {
      "L": "And to the sons of Gershom according to their families were given from the tribe of Issachar and from the tribe of Asher and from the tribe of Naphtali and from the tribe of Manasseh in Bashan thirteen cities.",
      "M": "The sons of Gershom according to their families received thirteen cities from the tribes of Issachar, Asher, Naphtali, and Manasseh in Bashan.",
      "T": "The Gershomites were scattered across the northern tribes — Issachar, Asher, Naphtali, and Manasseh in Bashan — thirteen cities distributed through the breadth of Israel's northern territory."
    },
    "63": {
      "L": "To the sons of Merari according to their families were given by lot from the tribe of Reuben and from the tribe of Gad and from the tribe of Zebulun twelve cities.",
      "M": "The sons of Merari according to their families received by lot twelve cities from the tribes of Reuben, Gad, and Zebulun.",
      "T": "The Merarites received twelve cities stretching from Transjordan — Reuben and Gad east of the Jordan — westward to Zebulun on the sea plain."
    },
    "64": {
      "L": "And the children of Israel gave to the Levites the cities with their pasturelands.",
      "M": "The Israelites gave the Levites these cities with their pasturelands.",
      "T": "Israel as a whole gave Levi what Levi had no land to earn: cities of belonging scattered in every tribe, supported by all."
    },
    "65": {
      "L": "And they gave by lot from the tribe of the children of Judah and from the tribe of the children of Simeon and from the tribe of the children of Benjamin these cities which are mentioned by name.",
      "M": "They assigned by lot from the tribes of Judah, Simeon, and Benjamin the cities that have just been named.",
      "T": "The cities in the south — drawn from Judah, Simeon, and Benjamin — were allocated by sacred lot, confirming that God himself distributed Levi's dwelling places throughout the covenant people."
    },
    "66": {
      "L": "And some of the families of the sons of Kohath had cities from their territory from the tribe of Ephraim.",
      "M": "Some of the Kohathite families received cities from the territory of the tribe of Ephraim.",
      "T": "Portions of the Kohathite clans were planted in Ephraim — the great central hill country — extending Levitical presence into the heart of the northern highlands."
    },
    "67": {
      "L": "And they gave to them the cities of refuge: Shechem with its pasturelands in the hill country of Ephraim, and Gezer with its pasturelands,",
      "M": "They gave them the cities of refuge: Shechem with its pasturelands in the hill country of Ephraim, and Gezer with its pasturelands,",
      "T": "These included Shechem — the great covenant-renewal city of Joshua — and Gezer with their pasturelands, both designated cities of refuge,"
    },
    "68": {
      "L": "and Jokmeam with its pasturelands and Beth-horon with its pasturelands,",
      "M": "Jokmeam with its pasturelands and Beth-horon with its pasturelands,",
      "T": "and Jokmeam and Beth-horon — Beth-horon guarding the main pass from the coastal plain to Jerusalem's highlands."
    },
    "69": {
      "L": "and Aijalon with its pasturelands and Gath-rimmon with its pasturelands.",
      "M": "Aijalon with its pasturelands and Gath-rimmon with its pasturelands.",
      "T": "And Aijalon — where Joshua commanded the sun to stand still — and Gath-rimmon, each with its pasturelands."
    },
    "70": {
      "L": "And from the half-tribe of Manasseh: Aner with its pasturelands and Bileam with its pasturelands, for the rest of the families of the sons of Kohath.",
      "M": "From the half-tribe of Manasseh: Aner with its pasturelands and Bileam with its pasturelands, for the remaining Kohathite families.",
      "T": "The remaining Kohathite families received Aner and Bileam from western Manasseh, completing a Kohathite presence from Judah in the south to Manasseh in the north."
    },
    "71": {
      "L": "To the sons of Gershom from the family of the half-tribe of Manasseh: Golan in Bashan with its pasturelands and Ashtaroth with its pasturelands.",
      "M": "The sons of Gershom received from the half-tribe of Manasseh: Golan in Bashan with its pasturelands and Ashtaroth with its pasturelands.",
      "T": "The Gershomites began their allotment in Bashan — the fertile tableland east of the Jordan — with Golan (itself a city of refuge) and Ashtaroth."
    },
    "72": {
      "L": "And from the tribe of Issachar: Kedesh with its pasturelands, Daberath with its pasturelands,",
      "M": "From the tribe of Issachar: Kedesh with its pasturelands and Daberath with its pasturelands,",
      "T": "From Issachar in the Jezreel Valley: Kedesh and Daberath, each with pasturelands."
    },
    "73": {
      "L": "and Ramoth with its pasturelands and Anem with its pasturelands.",
      "M": "Ramoth with its pasturelands and Anem with its pasturelands.",
      "T": "And Ramoth and Anem — four Gershomite cities in Issachar's fertile plain."
    },
    "74": {
      "L": "And from the tribe of Asher: Mashal with its pasturelands and Abdon with its pasturelands,",
      "M": "From the tribe of Asher: Mashal with its pasturelands and Abdon with its pasturelands,",
      "T": "From Asher on the northern coastal plain: Mashal and Abdon with their pasturelands,"
    },
    "75": {
      "L": "and Hukok with its pasturelands and Rehob with its pasturelands.",
      "M": "Hukok with its pasturelands and Rehob with its pasturelands.",
      "T": "and Hukok and Rehob — four cities threading the Levitical presence through Asher's coastal strip."
    },
    "76": {
      "L": "And from the tribe of Naphtali: Kedesh in Galilee with its pasturelands and Hammon with its pasturelands and Kiriathaim with its pasturelands.",
      "M": "From the tribe of Naphtali: Kedesh in Galilee with its pasturelands, Hammon with its pasturelands, and Kiriathaim with its pasturelands.",
      "T": "From Naphtali in the Galilean highlands: Kedesh in Galilee (a major city of refuge), Hammon, and Kiriathaim — the Gershomites thus spread across the entire northern tier of Israel."
    },
    "77": {
      "L": "To the rest of the Levites, the sons of Merari, from the tribe of Zebulun: Rimmono with its pasturelands and Tabor with its pasturelands.",
      "M": "The remaining Levites — the sons of Merari — received from the tribe of Zebulun: Rimmono with its pasturelands and Tabor with its pasturelands.",
      "T": "The Merarites began in Zebulun with Rimmono and Tabor — Mount Tabor, sentinel of the Jezreel Valley, a Merarite city."
    },
    "78": {
      "L": "And across the Jordan at Jericho, on the east side of the Jordan, from the tribe of Reuben: Bezer in the wilderness with its pasturelands and Jahzah with its pasturelands,",
      "M": "From the tribe of Reuben east of the Jordan opposite Jericho: Bezer in the wilderness with its pasturelands and Jahzah with its pasturelands,",
      "T": "Across the Jordan in Reuben's territory — the open steppe land east of Jericho — the Merarites received Bezer (a city of refuge in the wilderness plateau) and Jahzah,"
    },
    "79": {
      "L": "and Kedemoth with its pasturelands and Mephaath with its pasturelands.",
      "M": "Kedemoth with its pasturelands and Mephaath with its pasturelands.",
      "T": "and Kedemoth and Mephaath — four Transjordanian cities for Merari in Reuben."
    },
    "80": {
      "L": "And from the tribe of Gad: Ramoth in Gilead with its pasturelands and Mahanaim with its pasturelands,",
      "M": "From the tribe of Gad: Ramoth in Gilead with its pasturelands and Mahanaim with its pasturelands,",
      "T": "From Gad in Gilead: Ramoth in Gilead (another city of refuge, east of the Jordan) and Mahanaim — where Jacob had seen the angels of God, and where David would later flee from Absalom."
    },
    "81": {
      "L": "and Heshbon with its pasturelands and Jazer with its pasturelands.",
      "M": "Heshbon with its pasturelands and Jazer with its pasturelands.",
      "T": "And Heshbon and Jazer — completing the Merarite cities and closing the full roll of Levitical settlements distributed throughout every tribe of Israel."
    }
  },
  "7": {
    "1": {
      "L": "Now the sons of Issachar: Tola and Puah, Jashub and Shimron — four.",
      "M": "The sons of Issachar were Tola, Puah, Jashub, and Shimron — four in all.",
      "T": "Issachar had four sons: Tola, Puah, Jashub, and Shimron."
    },
    "2": {
      "L": "And the sons of Tola: Uzzi and Rephaiah and Jeriel and Jahmai and Ibsam and Samuel, heads of their fathers' houses. Of Tola — mighty men of valor in their generations; their number in the days of David was twenty-two thousand six hundred.",
      "M": "The sons of Tola were Uzzi, Rephaiah, Jeriel, Jahmai, Ibsam, and Samuel, heads of their ancestral houses. Tola's descendants were mighty warriors; their count in David's day was twenty-two thousand six hundred.",
      "T": "Tola's six sons — Uzzi, Rephaiah, Jeriel, Jahmai, Ibsam, and Samuel — each headed a clan of fighting men. By David's census, Tola's descendants numbered twenty-two thousand six hundred valiant warriors."
    },
    "3": {
      "L": "And the sons of Uzzi: Izrahiah. And the sons of Izrahiah: Michael and Obadiah and Joel and Ishiah — five, all of them chief men.",
      "M": "The son of Uzzi was Izrahiah. The sons of Izrahiah were Michael, Obadiah, Joel, and Ishiah — five, all of them leaders.",
      "T": "Uzzi's son Izrahiah had four sons — Michael, Obadiah, Joel, and Ishiah — five men of leadership including Izrahiah himself."
    },
    "4": {
      "L": "And with them by their generations, after their fathers' house, were bands of soldiers for war — thirty-six thousand, for they had many wives and sons.",
      "M": "With them, according to their family records, were thirty-six thousand troops ready for war, for they had many wives and children.",
      "T": "Their household rolls listed thirty-six thousand men fit for battle — a force grown large because Issachar's families were fruitful and their sons many."
    },
    "5": {
      "L": "And their brothers throughout all the families of Issachar — mighty men of valor — were reckoned in all by their genealogies, eighty-seven thousand.",
      "M": "Their kinsmen throughout all the families of Issachar — all of them mighty warriors — numbered eighty-seven thousand according to their genealogical records.",
      "T": "Counting all of Issachar's clans, the total of registered fighting men came to eighty-seven thousand — a substantial force from this one tribe."
    },
    "6": {
      "L": "The sons of Benjamin: Bela and Becher and Jediael — three.",
      "M": "The sons of Benjamin were Bela, Becher, and Jediael — three in all.",
      "T": "Benjamin had three sons recorded here: Bela, Becher, and Jediael."
    },
    "7": {
      "L": "And the sons of Bela: Ezbon and Uzzi and Uzziel and Jerimoth and Iri — five, heads of ancestral houses, mighty men of valor; their enrollment was twenty-two thousand and thirty-four.",
      "M": "The sons of Bela were Ezbon, Uzzi, Uzziel, Jerimoth, and Iri — five heads of ancestral houses and mighty warriors, numbering twenty-two thousand and thirty-four in their enrollment.",
      "T": "Bela's five sons — Ezbon, Uzzi, Uzziel, Jerimoth, and Iri — each led a clan; their combined enrollment reached twenty-two thousand thirty-four fighting men."
    },
    "8": {
      "L": "And the sons of Becher: Zemirah and Joash and Eliezer and Elioenai and Omri and Jerimoth and Abijah and Anathoth and Alemeth — all these were the sons of Becher.",
      "M": "The sons of Becher were Zemirah, Joash, Eliezer, Elioenai, Omri, Jerimoth, Abijah, Anathoth, and Alemeth — all these were sons of Becher.",
      "T": "Becher had nine sons: Zemirah, Joash, Eliezer, Elioenai, Omri, Jerimoth, Abijah, Anathoth, and Alemeth — a large family whose names several became place names in Benjamin's territory."
    },
    "9": {
      "L": "And their enrollment by genealogy according to their generations, heads of their ancestral houses, mighty men of valor, was twenty thousand and two hundred.",
      "M": "Their genealogical enrollment according to their generations, as heads of ancestral houses and mighty warriors, numbered twenty thousand two hundred.",
      "T": "Becher's clan rolls listed twenty thousand two hundred men — leaders and warriors enumerated by their family lines."
    },
    "10": {
      "L": "And the son of Jediael: Bilhan. And the sons of Bilhan: Jeush and Benjamin and Ehud and Chenaanah and Zethan and Tarshish and Ahishahar.",
      "M": "The son of Jediael was Bilhan. The sons of Bilhan were Jeush, Benjamin, Ehud, Chenaanah, Zethan, Tarshish, and Ahishahar.",
      "T": "Jediael's son Bilhan had seven sons — Jeush, Benjamin, Ehud, Chenaanah, Zethan, Tarshish, and Ahishahar — each heading a Benjaminite sub-clan."
    },
    "11": {
      "L": "All these were sons of Jediael, heads of ancestral houses, mighty men of valor — seventeen thousand and two hundred men fit to go out in the army for war.",
      "M": "All these were sons of Jediael — heads of ancestral houses and mighty warriors, seventeen thousand two hundred men ready to go to war.",
      "T": "From Jediael's line came seventeen thousand two hundred men of war — a formidable contingent from Benjamin's third founding son."
    },
    "12": {
      "L": "And Shuppim and Huppim were sons of Ir; and Hushim was the son of Aher.",
      "M": "Shuppim and Huppim were sons of Ir, and Hushim was the son of Aher.",
      "T": "Two other Benjaminite clans are noted briefly: Shuppim and Huppim from Ir, and Hushim from Aher."
    },
    "13": {
      "L": "The sons of Naphtali: Jahziel and Guni and Jezer and Shallum, the sons of Bilhah.",
      "M": "The sons of Naphtali were Jahziel, Guni, Jezer, and Shallum — descended from Bilhah.",
      "T": "Naphtali's four sons — Jahziel, Guni, Jezer, and Shallum — are noted as descendants of Bilhah, Rachel's servant, whose sons Dan and Naphtali completed Jacob's twelve."
    },
    "14": {
      "L": "The sons of Manasseh: Ashriel, whom his Aramean concubine bore — she bore Machir the father of Gilead.",
      "M": "The sons of Manasseh: Ashriel, born of his Aramean concubine, who also bore Machir the father of Gilead.",
      "T": "Manasseh's genealogy opens with Ashriel, born of an Aramean concubine, and Machir — the great warrior-patriarch whose very name became synonymous with the land of Gilead east of the Jordan."
    },
    "15": {
      "L": "And Machir took a wife for Huppim and for Shuppim, whose sister's name was Maachah. And the name of the second was Zelophehad, and Zelophehad had daughters.",
      "M": "Machir took wives for Huppim and Shuppim. His sister's name was Maachah, and his second son was Zelophehad, who had only daughters.",
      "T": "Machir arranged marriages within the clan for Huppim and Shuppim; his sister was Maachah. His son Zelophehad had only daughters — the women whose legal case established daughters' inheritance rights in Israel (Num 27)."
    },
    "16": {
      "L": "And Maachah the wife of Machir bore a son and she called his name Peresh; and his brother's name was Sheresh; and his sons were Ulam and Rakem.",
      "M": "Machir's wife Maachah bore a son whom she named Peresh; his brother was named Sheresh; and Sheresh's sons were Ulam and Rakem.",
      "T": "Machir's wife Maachah bore Peresh and Sheresh; Sheresh fathered Ulam and Rakem — Gilead's next generation taking root in Transjordan."
    },
    "17": {
      "L": "And the sons of Ulam: Bedan. These were the sons of Gilead the son of Machir the son of Manasseh.",
      "M": "The son of Ulam was Bedan. These were the sons of Gilead, the son of Machir, the son of Manasseh.",
      "T": "Ulam's son was Bedan — completing the Gileadite line back to its source: Gilead son of Machir son of Manasseh."
    },
    "18": {
      "L": "And his sister Hammoleketh bore Ishhod and Abiezer and Mahalah.",
      "M": "His sister Hammoleketh bore Ishhod, Abiezer, and Mahalah.",
      "T": "Machir's sister Hammoleketh — 'the queen' — bore Ishhod, Abiezer, and Mahalah, from whom notable Manassite clans descended."
    },
    "19": {
      "L": "And the sons of Shemida were Ahian and Shechem and Likhi and Aniam.",
      "M": "The sons of Shemida were Ahian, Shechem, Likhi, and Aniam.",
      "T": "Shemida — another Manassite leader — had four sons: Ahian, Shechem, Likhi, and Aniam."
    },
    "20": {
      "L": "And the sons of Ephraim: Shuthelah, and Bered his son, and Tahath his son, and Eladah his son, and Tahath his son,",
      "M": "The sons of Ephraim: Shuthelah, his son Bered, his son Tahath, his son Eladah, his son Tahath,",
      "T": "Ephraim's line runs: Shuthelah → Bered → Tahath → Eladah → Tahath — a chain of generations that would be violently interrupted in the next verse."
    },
    "21": {
      "L": "and Zabad his son, and Shuthelah his son. And Ezer and Elead — the men of Gath who were born in the land killed them, because they came down to take their livestock.",
      "M": "and his son Zabad, and his son Shuthelah. But Ezer and Elead were killed by the men of Gath who were native to that land, when they came down to raid their livestock.",
      "T": "Two of Ephraim's sons — Ezer and Elead — were killed by Gathite raiders when they attempted a cattle raid; the men born on that land struck them down. Violence shadowed Ephraim's genealogy long before the tribe inherited its hill country."
    },
    "22": {
      "L": "And Ephraim their father mourned many days, and his brothers came to comfort him.",
      "M": "Their father Ephraim mourned for them many days, and his brothers came to comfort him.",
      "T": "Ephraim grieved for his slain sons through a long season of mourning — his brothers coming to sit with him in his loss, the patriarch weeping over children taken before their time."
    },
    "23": {
      "L": "And he went in to his wife, and she conceived and bore a son, and he called his name Beriah, because evil had befallen his house.",
      "M": "Then he went in to his wife, and she conceived and bore a son. He named him Beriah, because disaster had come upon his household.",
      "T": "After his mourning Ephraim's wife conceived again, and the son born from that grief was named Beriah — 'in calamity' — a name that carried the memory of brothers lost into the next generation."
    },
    "24": {
      "L": "And his daughter was Sheerah, who built Beth-horon the lower and the upper and Uzzen-sheerah.",
      "M": "His daughter Sheerah built Lower and Upper Beth-horon and Uzzen-sheerah.",
      "T": "Ephraim also had a daughter, Sheerah, who achieved the remarkable distinction of building three towns — Lower and Upper Beth-horon and Uzzen-sheerah — among the few women in the Bible credited as city founders."
    },
    "25": {
      "L": "And Rephah was his son, and Resheph, and Telah his son, and Tahan his son,",
      "M": "His son was Rephah, and Resheph, and his son Telah, and his son Tahan,",
      "T": "The Ephraimite line continued through Rephah and Resheph, then Telah, then Tahan,"
    },
    "26": {
      "L": "Ladan his son, Ammihud his son, Elishama his son,",
      "M": "his son Ladan, his son Ammihud, his son Elishama,",
      "T": "then Ladan, Ammihud, and Elishama —"
    },
    "27": {
      "L": "Non his son, Joshua his son.",
      "M": "his son Non, his son Joshua.",
      "T": "then Non, and finally Joshua — the great conqueror who led Israel into the Promised Land stands at the end of this Ephraimite chain."
    },
    "28": {
      "L": "And their possessions and dwelling places were Bethel and its towns, and to the east Naaran, and to the west Gezer and its towns; and Shechem and its towns as far as Ayyah and its towns;",
      "M": "Their settlements and lands included Bethel and its surrounding towns, Naaran to the east, Gezer and its towns to the west, and Shechem and its towns as far as Ayyah and its towns.",
      "T": "Ephraim's territorial heartland is sketched: Bethel in the east, Gezer guarding the western pass, Shechem commanding the central ridge — the tribe that bore Joshua's name held the hill country's strategic center."
    },
    "29": {
      "L": "and along the borders of the sons of Manasseh: Beth-shean and its towns, Taanach and its towns, Megiddo and its towns, Dor and its towns. In these dwelt the sons of Joseph son of Israel.",
      "M": "Along the borders of Manasseh were Beth-shean and its towns, Taanach and its towns, Megiddo and its towns, and Dor and its towns. These were settled by the descendants of Joseph son of Israel.",
      "T": "Along the Manassite border stood Beth-shean, Taanach, Megiddo, and Dor — the great fortress cities of the Jezreel Valley. These lands belonged to Joseph's sons; the sons of Rachel's firstborn held the breadbasket and the war road of Canaan."
    },
    "30": {
      "L": "The sons of Asher: Imnah and Ishvah and Ishvi and Beriah, and Serah their sister.",
      "M": "The sons of Asher were Imnah, Ishvah, Ishvi, and Beriah, and their sister Serah.",
      "T": "Asher had four sons — Imnah, Ishvah, Ishvi, and Beriah — and a daughter, Serah, whose longevity was legendary in later tradition."
    },
    "31": {
      "L": "And the sons of Beriah: Heber and Malchiel, who is the father of Birzaith.",
      "M": "The sons of Beriah were Heber and Malchiel, who is the father of Birzaith.",
      "T": "Beriah's sons were Heber and Malchiel; Malchiel fathered the clan at Birzaith."
    },
    "32": {
      "L": "And Heber fathered Japhlet and Shomer and Hotham and their sister Shua.",
      "M": "Heber fathered Japhlet, Shomer, Hotham, and their sister Shua.",
      "T": "Heber's children were Japhlet, Shomer, Hotham, and a daughter Shua."
    },
    "33": {
      "L": "And the sons of Japhlet: Pasach and Bimhal and Ashvath. These are the sons of Japhlet.",
      "M": "The sons of Japhlet were Pasach, Bimhal, and Ashvath — these were Japhlet's sons.",
      "T": "Japhlet had three sons: Pasach, Bimhal, and Ashvath."
    },
    "34": {
      "L": "And the sons of Shemer: Ahi and Rohgah, Jehubbah and Aram.",
      "M": "The sons of Shemer were Ahi, Rohgah, Jehubbah, and Aram.",
      "T": "Shemer had four sons: Ahi, Rohgah, Jehubbah, and Aram."
    },
    "35": {
      "L": "And the sons of his brother Helem: Zophah and Imna and Shelesh and Amal.",
      "M": "The sons of his brother Helem were Zophah, Imna, Shelesh, and Amal.",
      "T": "Helem's four sons — Zophah, Imna, Shelesh, and Amal — extended the Asherite clans."
    },
    "36": {
      "L": "The sons of Zophah: Suah and Harnepher and Shual and Beri and Imrah,",
      "M": "The sons of Zophah: Suah, Harnepher, Shual, Beri, and Imrah,",
      "T": "Zophah's sons — Suah, Harnepher, Shual, Beri, and Imrah —"
    },
    "37": {
      "L": "Bezer and Hod and Shamma and Shilshah and Ithran and Beera.",
      "M": "Bezer, Hod, Shamma, Shilshah, Ithran, and Beera.",
      "T": "and Bezer, Hod, Shamma, Shilshah, Ithran, and Beera — eleven sons from Zophah alone, reflecting Asher's remarkable growth."
    },
    "38": {
      "L": "And the sons of Jether: Jephunneh and Pispa and Ara.",
      "M": "The sons of Jether were Jephunneh, Pispa, and Ara.",
      "T": "Jether's three sons were Jephunneh, Pispa, and Ara."
    },
    "39": {
      "L": "And the sons of Ulla: Arah and Hanniel and Rizia.",
      "M": "The sons of Ulla were Arah, Hanniel, and Rizia.",
      "T": "Ulla's three sons — Arah, Hanniel, and Rizia — complete the Asherite sub-families."
    },
    "40": {
      "L": "All these were sons of Asher, heads of ancestral houses, choice men, mighty warriors, chief leaders. Their enrollment by genealogies for service in war was twenty-six thousand men.",
      "M": "All these were sons of Asher, heads of ancestral houses — chosen men, mighty warriors, outstanding leaders. Their genealogical enrollment for military service was twenty-six thousand men.",
      "T": "In summary: Asher's entire genealogy produced twenty-six thousand registered fighting men from families of leading, hand-picked warriors — a small tribe with a formidable military roll, faithful to its place in Israel's covenant assembly."
    }
  },
  "8": {
    "1": {
      "L": "And Benjamin fathered Bela his firstborn, Ashbel the second, and Aharah the third,",
      "M": "Benjamin fathered Bela his firstborn, Ashbel the second, and Aharah the third,",
      "T": "Benjamin's sons begin a fresh genealogy: Bela the firstborn, then Ashbel and Aharah — this list differs from Numbers 26 and continues separately from chapter 7's Benjaminite data."
    },
    "2": {
      "L": "Nohah the fourth and Rapha the fifth.",
      "M": "Nohah the fourth and Rapha the fifth.",
      "T": "Nohah fourth and Rapha fifth — Benjamin's five sons by birth order."
    },
    "3": {
      "L": "And the sons of Bela were: Addar and Gera and Abihud,",
      "M": "The sons of Bela were Addar, Gera, and Abihud,",
      "T": "Bela, Benjamin's firstborn, had sons Addar, Gera, and Abihud,"
    },
    "4": {
      "L": "and Abishua and Naaman and Ahoah,",
      "M": "Abishua, Naaman, and Ahoah,",
      "T": "Abishua, Naaman, and Ahoah,"
    },
    "5": {
      "L": "and Gera and Shephuphan and Huram.",
      "M": "and Gera, Shephuphan, and Huram.",
      "T": "and Gera, Shephuphan, and Huram — nine sons in Bela's household."
    },
    "6": {
      "L": "These are the sons of Ehud — they are the heads of ancestral houses of the inhabitants of Geba, and they were taken into exile to Manahath:",
      "M": "These are the sons of Ehud — heads of ancestral houses of the inhabitants of Geba — who were carried into exile at Manahath:",
      "T": "The sons of Ehud — prominent clan heads in Geba — were displaced and taken to Manahath, a forced relocation that scattered this Benjaminite branch."
    },
    "7": {
      "L": "and Naaman and Ahijah and Gera — he took them into exile — and he fathered Uzza and Ahihud.",
      "M": "Naaman, Ahijah, and Gera — he removed them — and he fathered Uzza and Ahihud.",
      "T": "Naaman, Ahijah, and Gera were removed; from the last Gera came Uzza and Ahihud, continuing the line after the disruption."
    },
    "8": {
      "L": "And Shaharaim fathered children in the land of Moab after he had sent away Hushim and Baara his wives.",
      "M": "Shaharaim fathered children in the land of Moab after he had divorced his wives Hushim and Baara.",
      "T": "Shaharaim settled in Moab after sending away two wives — Hushim and Baara — and fathered a new family there, Benjaminite branches extending into Transjordan."
    },
    "9": {
      "L": "He fathered by his wife Hodesh: Jobab and Zibia and Mesha and Malcam,",
      "M": "By his wife Hodesh he fathered Jobab, Zibia, Mesha, and Malcam,",
      "T": "By Hodesh — his wife in Moab — he had Jobab, Zibia, Mesha, and Malcam,"
    },
    "10": {
      "L": "and Jeuz and Sachia and Mirmah. These were his sons, heads of ancestral houses.",
      "M": "and Jeuz, Sachia, and Mirmah. These were his sons, heads of ancestral houses.",
      "T": "and Jeuz, Sachia, and Mirmah — seven sons, each a clan head, born in foreign soil."
    },
    "11": {
      "L": "And of Hushim he fathered Abitub and Elpaal.",
      "M": "By Hushim he had fathered Abitub and Elpaal.",
      "T": "His earlier wife Hushim had borne him Abitub and Elpaal."
    },
    "12": {
      "L": "The sons of Elpaal: Eber and Misham and Shemed, who built Ono and Lod with its towns,",
      "M": "The sons of Elpaal were Eber, Misham, and Shemed — Shemed built Ono and Lod with its towns —",
      "T": "Elpaal's sons included Shemed, who built Ono and Lod — a founder of cities in the Shephelah lowlands, remembered in this genealogy for his constructive legacy."
    },
    "13": {
      "L": "and Beriah and Shema — they were heads of ancestral houses for the inhabitants of Aijalon, who put to flight the inhabitants of Gath —",
      "M": "and Beriah and Shema, who were heads of ancestral houses for the inhabitants of Aijalon, and who drove out the inhabitants of Gath —",
      "T": "Beriah and Shema were the clan leaders at Aijalon — the valley where Joshua commanded the sun to stand still — and they drove out the Gathite Philistines, reclaiming the land by force."
    },
    "14": {
      "L": "and Ahio, Shashak, and Jeremoth,",
      "M": "Ahio, Shashak, and Jeremoth,",
      "T": "among the sons also listed: Ahio, Shashak, Jeremoth,"
    },
    "15": {
      "L": "and Zebadiah and Arad and Eder,",
      "M": "Zebadiah, Arad, and Eder,",
      "T": "Zebadiah, Arad, and Eder,"
    },
    "16": {
      "L": "and Michael and Ishpah and Joha, sons of Beriah,",
      "M": "Michael, Ishpah, and Joha — sons of Beriah —",
      "T": "Michael, Ishpah, and Joha — Beriah's sons —"
    },
    "17": {
      "L": "and Zebadiah and Meshullam and Hizki and Heber,",
      "M": "Zebadiah, Meshullam, Hizki, and Heber,",
      "T": "Zebadiah, Meshullam, Hizki, and Heber,"
    },
    "18": {
      "L": "and Ishmerai and Izliah and Jobab, sons of Elpaal;",
      "M": "Ishmerai, Izliah, and Jobab — sons of Elpaal —",
      "T": "Ishmerai, Izliah, and Jobab — Elpaal's sons —"
    },
    "19": {
      "L": "and Jakim and Zichri and Zabdi,",
      "M": "Jakim, Zichri, and Zabdi,",
      "T": "Jakim, Zichri, and Zabdi,"
    },
    "20": {
      "L": "and Elienai and Zillethai and Eliel,",
      "M": "Elienai, Zillethai, and Eliel,",
      "T": "Elienai, Zillethai, and Eliel,"
    },
    "21": {
      "L": "and Adaiah and Beraiah and Shimrath, sons of Shimei;",
      "M": "Adaiah, Beraiah, and Shimrath — sons of Shimei —",
      "T": "Adaiah, Beraiah, and Shimrath — Shimei's sons —"
    },
    "22": {
      "L": "and Ishpan and Eber and Eliel,",
      "M": "Ishpan, Eber, and Eliel,",
      "T": "Ishpan, Eber, and Eliel,"
    },
    "23": {
      "L": "and Abdon and Zichri and Hanan,",
      "M": "Abdon, Zichri, and Hanan,",
      "T": "Abdon, Zichri, and Hanan,"
    },
    "24": {
      "L": "and Hananiah and Elam and Antothijah,",
      "M": "Hananiah, Elam, and Antothijah,",
      "T": "Hananiah, Elam, and Antothijah,"
    },
    "25": {
      "L": "and Iphedeiah and Penuel, sons of Shashak;",
      "M": "Iphedeiah and Penuel — sons of Shashak —",
      "T": "Iphedeiah and Penuel — Shashak's sons —"
    },
    "26": {
      "L": "and Shamsherai and Shehariah and Athaliah,",
      "M": "Shamsherai, Shehariah, and Athaliah,",
      "T": "Shamsherai, Shehariah, and Athaliah,"
    },
    "27": {
      "L": "and Jaareshiah and Elijah and Zichri, sons of Jeroham.",
      "M": "Jaareshiah, Elijah, and Zichri — sons of Jeroham.",
      "T": "Jaareshiah, Elijah, and Zichri — Jeroham's sons, completing the extended Benjaminite clan list."
    },
    "28": {
      "L": "These were heads of ancestral houses according to their generations, chief men. These dwelt in Jerusalem.",
      "M": "These were heads of ancestral houses throughout their generations — leading men who lived in Jerusalem.",
      "T": "All these Benjaminite clan heads — generation upon generation of leaders — lived in Jerusalem, Benjamin's tribe sharing the holy city with Judah from the beginning."
    },
    "29": {
      "L": "Now the father of Gibeon lived in Gibeon, and his wife's name was Maachah.",
      "M": "The father of Gibeon lived at Gibeon; his wife's name was Maachah.",
      "T": "At Gibeon — the great northern Benjaminite city, where the tabernacle would rest for a generation — lived the founding patriarch of that city; his wife was named Maachah."
    },
    "30": {
      "L": "His firstborn son was Abdon, then Zur, Kish, Baal, Nadab,",
      "M": "His firstborn son was Abdon, then Zur, Kish, Baal, and Nadab,",
      "T": "His firstborn was Abdon, followed by Zur, Kish, Baal, and Nadab —"
    },
    "31": {
      "L": "and Gedor and Ahio and Zacher.",
      "M": "Gedor, Ahio, and Zacher.",
      "T": "and Gedor, Ahio, and Zacher — notice Kish among these sons, for this line leads to Saul."
    },
    "32": {
      "L": "And Mikloth fathered Shimeah. And they too dwelt opposite their brothers in Jerusalem, along with their brothers.",
      "M": "Mikloth fathered Shimeah. They also lived in Jerusalem, across from their kinsmen.",
      "T": "Mikloth fathered Shimeah; this branch of the Gibeonite family also settled in Jerusalem — kinsmen living near each other in the city of David and Benjamin's shared inheritance."
    },
    "33": {
      "L": "And Ner fathered Kish, and Kish fathered Saul, and Saul fathered Jonathan and Malchishua and Abinadab and Eshbaal.",
      "M": "Ner fathered Kish, Kish fathered Saul, and Saul fathered Jonathan, Malchishua, Abinadab, and Eshbaal.",
      "T": "Here the royal Saulide line emerges: Ner → Kish → Saul, and Saul's four sons — Jonathan the loyal, Malchishua, Abinadab, and Eshbaal (called Ishbosheth in Samuel, his name sanitized to remove 'Baal')."
    },
    "34": {
      "L": "And the son of Jonathan was Meribbaal, and Meribbaal fathered Micah.",
      "M": "Jonathan's son was Meribbaal, and Meribbaal fathered Micah.",
      "T": "Jonathan's son was Meribbaal — the child David showed covenant kindness to, crippled from childhood (2 Sam 9); Meribbaal fathered Micah, keeping the line alive."
    },
    "35": {
      "L": "And the sons of Micah: Pithon and Melech and Tarea and Ahaz.",
      "M": "The sons of Micah were Pithon, Melech, Tarea, and Ahaz.",
      "T": "Micah had four sons — Pithon, Melech, Tarea, and Ahaz — the Saulide descent continuing past the fall of Saul's house."
    },
    "36": {
      "L": "And Ahaz fathered Jehoadah, and Jehoadah fathered Alemeth and Azmaveth and Zimri, and Zimri fathered Moza.",
      "M": "Ahaz fathered Jehoadah, Jehoadah fathered Alemeth, Azmaveth, and Zimri, and Zimri fathered Moza.",
      "T": "Ahaz → Jehoadah → Alemeth, Azmaveth, and Zimri → Moza: the Saulide line branching and persisting through the generations of David's and Solomon's reigns."
    },
    "37": {
      "L": "And Moza fathered Binea; Rapha was his son, Eleasah his son, Azel his son.",
      "M": "Moza fathered Binea; Binea's son was Rapha, his son Eleasah, his son Azel.",
      "T": "Moza → Binea → Rapha → Eleasah → Azel: five more generations of the house of Saul living in the land after the kingdom passed to David."
    },
    "38": {
      "L": "And Azel had six sons, and these are their names: Azrikam, Bocheru, Ishmael, Sheariah, Obadiah, and Hanan. All these were sons of Azel.",
      "M": "Azel had six sons: Azrikam, Bocheru, Ishmael, Sheariah, Obadiah, and Hanan — all sons of Azel.",
      "T": "Azel had six sons — Azrikam, Bocheru, Ishmael, Sheariah, Obadiah, and Hanan — a household flourishing ten generations after Saul's fall."
    },
    "39": {
      "L": "And the sons of his brother Eshek: Ulam his firstborn, Jeush the second, and Eliphelet the third.",
      "M": "The sons of his brother Eshek: Ulam the firstborn, Jeush the second, and Eliphelet the third.",
      "T": "Azel's brother Eshek had three sons — Ulam the firstborn, Jeush, and Eliphelet — extending the genealogy sideways through a collateral Saulide branch."
    },
    "40": {
      "L": "And the sons of Ulam were men of valor, archers, and had many sons and grandsons — one hundred and fifty. All these were from the sons of Benjamin.",
      "M": "The sons of Ulam were mighty warriors, skilled archers, with many sons and grandsons — one hundred and fifty in all. All these were from the sons of Benjamin.",
      "T": "Ulam's household was remarkable: one hundred and fifty sons and grandsons — all archers, all men of valor. The tribe of Benjamin, small but fierce, ends its genealogy with a house of warriors. These are Benjamin's sons."
    }
  },
  "9": {
    "1": {
      "L": "So all Israel was enrolled by genealogies, and these are written in the book of the kings of Israel. And Judah was carried into exile to Babylon because of their unfaithfulness.",
      "M": "All Israel was enrolled in genealogies, which are recorded in the book of the kings of Israel. And Judah was carried into exile in Babylon because of their unfaithfulness.",
      "T": "Here the nine-chapter genealogical prologue reaches its climax: all Israel was registered — identity preserved in lists — but then Judah was taken to Babylon for its covenant unfaithfulness. The genealogies survive the exile; the question is whether Israel will."
    },
    "2": {
      "L": "Now the first inhabitants who lived in their possessions in their cities were Israel, the priests, the Levites, and the temple servants.",
      "M": "The first people to settle in their own towns again were Israelites, priests, Levites, and temple servants.",
      "T": "When the exiles returned, those who repossessed their ancestral towns were Israelites, priests, Levites, and the Nethinim temple servants — the full spectrum of covenant community reconstituting itself on its own soil."
    },
    "3": {
      "L": "And in Jerusalem lived of the sons of Judah and of the sons of Benjamin and of the sons of Ephraim and Manasseh:",
      "M": "In Jerusalem lived people from the tribes of Judah, Benjamin, Ephraim, and Manasseh:",
      "T": "Jerusalem was rebuilt as a genuinely multi-tribal city: Judah and Benjamin who had never fully left, and northern Israelites from Ephraim and Manasseh — the post-exilic community a remnant drawn from all twelve."
    },
    "4": {
      "L": "Uthai son of Ammihud son of Omri son of Imri son of Bani, from the sons of Perez son of Judah.",
      "M": "Uthai son of Ammihud, son of Omri, son of Imri, son of Bani, from the descendants of Perez son of Judah.",
      "T": "From Judah, through the royal Perez line: Uthai, whose lineage traces back five generations — a Judahite resettler with documented ancestry."
    },
    "5": {
      "L": "And of the Shilonites: Asaiah the firstborn and his sons.",
      "M": "From the Shilonites: Asaiah the firstborn and his sons.",
      "T": "From the Shilonites — Shelah's descendants — Asaiah the firstborn resettled with his household."
    },
    "6": {
      "L": "And of the sons of Zerah: Jeuel and their brothers, six hundred and ninety.",
      "M": "From the sons of Zerah: Jeuel and his kinsmen — six hundred and ninety in all.",
      "T": "From Zerah — Judah's other royal line — Jeuel led back six hundred ninety returnees, a substantial household reclaiming their place in the city."
    },
    "7": {
      "L": "And of the sons of Benjamin: Sallu son of Meshullam son of Hodaviah son of Hasenuah,",
      "M": "From the Benjaminites: Sallu son of Meshullam, son of Hodaviah, son of Hasenuah,",
      "T": "From Benjamin, Sallu — with four generations of lineage documented — reclaimed his ancestral place in Jerusalem."
    },
    "8": {
      "L": "and Ibneiah son of Jeroham, and Elah son of Uzzi son of Michri, and Meshullam son of Shephatiah son of Reuel son of Ibnijah;",
      "M": "Ibneiah son of Jeroham, Elah son of Uzzi son of Michri, and Meshullam son of Shephatiah son of Reuel son of Ibnijah;",
      "T": "Ibneiah son of Jeroham, Elah with his documented Uzzi-Michri lineage, and Meshullam with his four-generation ancestry — Benjaminite returnees proving their identity by their family records."
    },
    "9": {
      "L": "and their brothers according to their generations — nine hundred and fifty-six. All these men were heads of ancestral houses in their fathers' houses.",
      "M": "together with their kinsmen according to their family records — nine hundred and fifty-six in all. All these were heads of ancestral households.",
      "T": "Nine hundred and fifty-six Benjaminites resettled Jerusalem — each a clan head, each with documented lineage, each reclaiming a share of the city their tribe had always shared with Judah."
    },
    "10": {
      "L": "And of the priests: Jedaiah and Jehoiarib and Jachin,",
      "M": "From the priests: Jedaiah, Jehoiarib, and Jachin,",
      "T": "The priestly families who returned to Jerusalem: Jedaiah, Jehoiarib, and Jachin — three of the twenty-four priestly divisions David had established."
    },
    "11": {
      "L": "and Azariah son of Hilkiah son of Meshullam son of Zadok son of Meraioth son of Ahitub, the chief officer of the house of God;",
      "M": "and Azariah son of Hilkiah, son of Meshullam, son of Zadok, son of Meraioth, son of Ahitub — the chief officer of the house of God;",
      "T": "And Azariah — the chief administrator of the temple — whose lineage traces six generations back through Zadok to Ahitub, the Aaronic high priestly line unbroken from before the exile."
    },
    "12": {
      "L": "and Adaiah son of Jeroham son of Pashhur son of Malchijah, and Maasai son of Adiel son of Jahzerah son of Meshullam son of Meshillemith son of Immer;",
      "M": "Adaiah son of Jeroham, son of Pashhur, son of Malchijah, and Maasai son of Adiel, son of Jahzerah, son of Meshullam, son of Meshillemith, son of Immer;",
      "T": "Adaiah from Malchijah's clan and Maasai from Immer's clan — both with deep priestly pedigrees traceable through multiple generations, their families having maintained their identity through the Babylonian captivity."
    },
    "13": {
      "L": "and their brothers, heads of their ancestral houses — one thousand seven hundred and sixty, very able men for the work of the service of the house of God.",
      "M": "together with their kinsmen, heads of their ancestral households — one thousand seven hundred and sixty capable men for the work of the house of God.",
      "T": "A total of one thousand seven hundred sixty priests returned — all heads of families, all skilled for temple service. The worship of Israel could resume; the fire of the altar would be lit again."
    },
    "14": {
      "L": "And of the Levites: Shemaiah son of Hasshub son of Azrikam son of Hashabiah, from the sons of Merari;",
      "M": "From the Levites: Shemaiah son of Hasshub, son of Azrikam, son of Hashabiah, from the sons of Merari;",
      "T": "The Levites who returned included Shemaiah from Merari's line — his four-generation pedigree anchoring him to the ancestral Levitical structure."
    },
    "15": {
      "L": "and Bakbakkar, Heresh, Galal, and Mattaniah son of Micah son of Zichri son of Asaph;",
      "M": "Bakbakkar, Heresh, Galal, and Mattaniah son of Micah, son of Zichri, son of Asaph;",
      "T": "Among the singers: Mattaniah descends from Asaph himself — the great worship leader David appointed — meaning the Asaphite choral tradition survived the exile intact and came home."
    },
    "16": {
      "L": "and Obadiah son of Shemaiah son of Galal son of Jeduthun, and Berechiah son of Asa son of Elkanah, who lived in the villages of the Netophathites.",
      "M": "Obadiah son of Shemaiah, son of Galal, son of Jeduthun, and Berechiah son of Asa, son of Elkanah, who lived in the villages of the Netophathites.",
      "T": "Obadiah from Jeduthun's line — the third of David's great cantors — also returned, and Berechiah settled in the Netophathite villages south of Jerusalem, the Levitical presence spreading through Judah's countryside."
    },
    "17": {
      "L": "And the gatekeepers: Shallum and Akkub and Talmon and Ahiman and their brothers; Shallum was the chief.",
      "M": "The gatekeepers were Shallum, Akkub, Talmon, and Ahiman, with their kinsmen; Shallum was the chief.",
      "T": "The gatekeepers — guardians of the temple's thresholds — were led by Shallum, with Akkub, Talmon, and Ahiman as his colleagues. The gates of the house of God would be manned again."
    },
    "18": {
      "L": "Until now they were at the king's gate to the east; they are the gatekeepers for the camps of the sons of Levi.",
      "M": "Formerly stationed at the king's gate to the east, they served as gatekeepers for the Levitical camps.",
      "T": "These families had historically guarded the east gate — the king's gate — when the Levites camped around the tabernacle; their hereditary post now transferred to the rebuilt temple."
    },
    "19": {
      "L": "And Shallum son of Kore son of Ebiasaph son of Korah, and his brothers of his father's house, the Korahites, were over the work of the service, guarding the thresholds of the tent, as their fathers had guarded the entrance to the camp of the LORD.",
      "M": "Shallum son of Kore, son of Ebiasaph, son of Korah, and his fellow Korahites were responsible for guarding the thresholds of the tent, just as their ancestors had guarded the entrance of the LORD's camp.",
      "T": "Shallum's lineage runs through Ebiasaph back to Korah himself — the rebel of Numbers 16 whose sons, remarkably, did not die with him (Num 26:11). His descendants became guardians of the very sanctuary their ancestor tried to usurp, the covenant grace threading through even a family of rebellion. Phinehas son of Eleazar had once overseen this threshold duty (v.20); now Korah's line carries it forward."
    },
    "20": {
      "L": "And Phinehas son of Eleazar was ruler over them in former times; the LORD was with him.",
      "M": "In earlier times Phinehas son of Eleazar was their leader; the LORD was with him.",
      "T": "Phinehas son of Eleazar — whose zeal at Baal-peor turned away God's wrath and secured the covenant of an everlasting priesthood for his line (Num 25) — had been the founding overseer of this gatekeeper duty. The LORD's presence marked his leadership."
    },
    "21": {
      "L": "Zechariah son of Meshelemiah was gatekeeper at the entrance of the tent of meeting.",
      "M": "Zechariah son of Meshelemiah was the gatekeeper at the entrance of the tent of meeting.",
      "T": "The eastern entrance to the tent of meeting had been guarded by Zechariah son of Meshelemiah — a post of highest honor, standing at the threshold where Israel met with God."
    },
    "22": {
      "L": "All these, chosen as gatekeepers at the thresholds, were two hundred and twelve. They were enrolled by genealogy in their villages. David and Samuel the seer established them in their hereditary office.",
      "M": "All those chosen as gatekeepers at the thresholds were two hundred and twelve, enrolled in their genealogical records in their own villages. David and Samuel the seer had appointed them to their hereditary office.",
      "T": "Two hundred and twelve gatekeepers — registered by family, dwelling in their own villages, and holding a post that David and Samuel together had established. The seer and the king jointly ordered Israel's worship; the post-exilic community honors that founding."
    },
    "23": {
      "L": "So they and their sons were over the gates of the house of the LORD, the house of the tent, by their wards.",
      "M": "They and their sons were responsible for the gates of the house of the LORD — the house of the tent — by their rotation of duty.",
      "T": "Generation to generation the gatekeepers guarded the same thresholds — the house built by Solomon standing where the tent of meeting had stood, and the same families manning the same doors across the centuries."
    },
    "24": {
      "L": "Toward the four winds were the gatekeepers: toward the east, west, north, and south.",
      "M": "Gatekeepers were stationed at the four directions: east, west, north, and south.",
      "T": "The whole compass surrounded by holy guardians — east, west, north, south — so that the house of God was kept from every quarter."
    },
    "25": {
      "L": "And their brothers in their villages were to come for seven days from time to time to be with them.",
      "M": "Their fellow Levites in their villages came to serve with them every seven days, in rotation.",
      "T": "The gatekeepers rotated in on a seven-day cycle from their home villages — a system ensuring the gates were always manned without requiring any family to give up their land and livelihood permanently."
    },
    "26": {
      "L": "For the four chief gatekeepers were in a position of trust; they were Levites and were over the chambers and the treasuries of the house of God.",
      "M": "The four chief gatekeepers were entrusted with their posts as Levites and were responsible for the storerooms and treasuries of the house of God.",
      "T": "The four senior gatekeepers held a position of sacred trust — overseeing not just the doors but the storerooms and treasuries, the practical heart of the temple's daily operations."
    },
    "27": {
      "L": "And they lodged around the house of God, for they had the charge over it, and they were over the opening every morning.",
      "M": "They spent the night around the house of God, for the charge of guarding it was theirs, and they opened it every morning.",
      "T": "The chief gatekeepers slept at the temple precinct — guardians who never fully left their post — and it was their hands that unlocked the gates each morning, the first act of a new day's worship."
    },
    "28": {
      "L": "And some of them were over the vessels of service, for they were to bring them in by count and take them out by count.",
      "M": "Some of them were in charge of the vessels used in worship, counting them in and out.",
      "T": "Careful inventory control: specific Levites tracked every chalice and bowl entering and leaving service, accountability built into the worship system so nothing sacred was lost or misused."
    },
    "29": {
      "L": "And some of them were appointed over the furniture and all the holy vessels, and over the fine flour and the wine and the oil and the incense and the spices.",
      "M": "Others were appointed over the furnishings and all the holy vessels, the fine flour, the wine, the oil, the incense, and the aromatic spices.",
      "T": "Every element of the altar and sanctuary — the furnishings, the grain, the wine, the oil, the fragrant incense — had a designated Levitical steward. Nothing in the worship of the LORD was left to chance."
    },
    "30": {
      "L": "And some of the sons of the priests made the ointment of the spices.",
      "M": "Some of the priests prepared the blended spice ointment.",
      "T": "The sacred anointing oil — compounded from prescribed spices — was mixed only by qualified priests; even the perfumers of the temple had hereditary credentials."
    },
    "31": {
      "L": "And Mattithiah, one of the Levites, who was the firstborn of Shallum the Korahite, had the trust over the things made in pans.",
      "M": "Mattithiah, a Levite and the firstborn of Shallum the Korahite, held trusted responsibility over the flat cakes made in pans.",
      "T": "Even the temple bakery had its assigned keeper: Mattithiah — Shallum's firstborn from the Korahite line — presided over the prepared offerings cooked in pans, no element of the daily sacrifice left without oversight."
    },
    "32": {
      "L": "And some of their brothers, of the sons of the Kohathites, were over the rows of bread, to prepare them every Sabbath.",
      "M": "Some of their Kohathite kinsmen were responsible for preparing the rows of bread for each Sabbath.",
      "T": "The showbread — twelve loaves arranged before the LORD every Sabbath — was the Kohathites' special charge; they prepared fresh bread each week, replenishing what had stood before God throughout the previous seven days."
    },
    "33": {
      "L": "And these are the singers, heads of Levitical families. In the chambers they were free from other service, for they were employed in that work day and night.",
      "M": "These were the singers, heads of Levitical families. They lived in the temple chambers, exempt from other duties, because they were on duty in their work day and night.",
      "T": "The temple singers — Levitical clan heads — were given permanent quarters in the temple precincts, excused from every other obligation. Worship was their sole work, day and night without interruption: the unceasing song that never stopped."
    },
    "34": {
      "L": "These were heads of the Levitical families throughout their generations. These chief men lived in Jerusalem.",
      "M": "These were heads of Levitical families throughout their generations — leading men who lived in Jerusalem.",
      "T": "These Levitical leaders — generation after generation of them — made Jerusalem their home; the holy city sustained by those whose whole life was the care of God's house."
    },
    "35": {
      "L": "And in Gibeon lived the father of Gibeon, Jeiel, and his wife's name was Maachah.",
      "M": "The founder of Gibeon, Jeiel, lived at Gibeon; his wife's name was Maachah.",
      "T": "The genealogy now pivots to Saul — beginning at Gibeon, the great Benjaminite city, with Jeiel its founding patriarch and his wife Maachah."
    },
    "36": {
      "L": "His firstborn son was Abdon, then Zur and Kish and Baal and Ner and Nadab,",
      "M": "His firstborn was Abdon, then Zur, Kish, Baal, Ner, and Nadab,",
      "T": "Among Jeiel's sons were Kish — who would father Saul — and Ner — who would father Abner, Saul's general. The stage is being set for both the king and his commander."
    },
    "37": {
      "L": "and Gedor and Ahio and Zechariah and Mikloth.",
      "M": "Gedor, Ahio, Zechariah, and Mikloth.",
      "T": "Gedor, Ahio, Zechariah, and Mikloth — siblings of Kish and Ner, the supporting cast of Saul's family tree."
    },
    "38": {
      "L": "And Mikloth fathered Shimeam. And they too lived opposite their brothers in Jerusalem, with their brothers.",
      "M": "Mikloth fathered Shimeam. They also lived in Jerusalem across from their kinsmen.",
      "T": "Mikloth's branch settled in Jerusalem itself — another Benjaminite household in the capital, the tribe of Saul dwelling alongside the tribe of David."
    },
    "39": {
      "L": "And Ner fathered Kish, and Kish fathered Saul, and Saul fathered Jonathan and Malchishua and Abinadab and Eshbaal.",
      "M": "Ner fathered Kish, Kish fathered Saul, and Saul fathered Jonathan, Malchishua, Abinadab, and Eshbaal.",
      "T": "The royal line crystallizes: Ner → Kish → Saul, and Saul's four sons — Jonathan, Malchishua, Abinadab, and Eshbaal. Three of these four die with their father on Gilboa. The repetition of this genealogy here (cf. 8:33) frames chapter 10's death narrative."
    },
    "40": {
      "L": "And the son of Jonathan was Meribbaal, and Meribbaal fathered Micah.",
      "M": "Jonathan's son was Meribbaal, and Meribbaal fathered Micah.",
      "T": "Jonathan's son Meribbaal survived the battle — his line continuing even as Saul's dynasty fell — because David's covenant loyalty to Jonathan (2 Sam 9) preserved him."
    },
    "41": {
      "L": "And the sons of Micah: Pithon and Melech and Tahrea.",
      "M": "The sons of Micah were Pithon, Melech, and Tahrea.",
      "T": "Micah's sons — Pithon, Melech, and Tahrea — carry Saul's bloodline into the next generation after the kingdom's transfer."
    },
    "42": {
      "L": "And Ahaz fathered Jarah, and Jarah fathered Alemeth and Azmaveth and Zimri, and Zimri fathered Moza.",
      "M": "Ahaz fathered Jarah, Jarah fathered Alemeth, Azmaveth, and Zimri, and Zimri fathered Moza.",
      "T": "The post-Saul generations continue: Ahaz → Jarah → Alemeth, Azmaveth, Zimri → Moza — the house of Saul persisting quietly through the reign of the Davidic dynasty."
    },
    "43": {
      "L": "And Moza fathered Binea, and Rephaiah was his son, Eleasah his son, Azel his son.",
      "M": "Moza fathered Binea; Binea's descendants were Rephaiah, then Eleasah, then Azel.",
      "T": "Moza → Binea → Rephaiah → Eleasah → Azel: the genealogy reaches perhaps ten or eleven generations beyond Saul, proof that his family continued long after his disgrace."
    },
    "44": {
      "L": "And Azel had six sons, and these are their names: Azrikam, Bocheru, Ishmael, Sheariah, Obadiah, and Hanan. These are the sons of Azel.",
      "M": "Azel had six sons: Azrikam, Bocheru, Ishmael, Sheariah, Obadiah, and Hanan — these are the sons of Azel.",
      "T": "Six sons of Azel — the Saulide tree still branching many generations after Gilboa. The Chronicler records this not to rehabilitate Saul but to show that God's purposes for all Israel, including Benjamin's tribe, did not end with one dynasty's failure."
    }
  },
  "10": {
    "1": {
      "L": "Now the Philistines fought against Israel, and the men of Israel fled from before the Philistines and fell down slain on Mount Gilboa.",
      "M": "The Philistines fought against Israel, and the Israelites fled before them, falling slain on Mount Gilboa.",
      "T": "The narrative strikes without warning after nine chapters of genealogy: the Philistines attack, Israel breaks and flees, and the bodies pile up on Gilboa — the battle that ends Saul's kingdom and opens the way for David."
    },
    "2": {
      "L": "And the Philistines pursued hard after Saul and his sons, and the Philistines struck down Jonathan and Abinadab and Malchishua, the sons of Saul.",
      "M": "The Philistines pressed hard after Saul and his sons, striking down Jonathan, Abinadab, and Malchishua.",
      "T": "The Philistines drove straight for the royal family — Jonathan, Abinadab, and Malchishua cut down. The sons whose names just appeared in the genealogy now fall on the same page; the list becomes an obituary."
    },
    "3": {
      "L": "The battle went hard against Saul, and the archers found him, and he was wounded by the archers.",
      "M": "The battle pressed hard against Saul; the archers overtook him and he was wounded by them.",
      "T": "Saul himself was surrounded — the archers closing in, their arrows finding him, his strength failing. A king who had once stood head and shoulders above every man in Israel was now cornered by bowmen on a mountain slope."
    },
    "4": {
      "L": "Then Saul said to his armor-bearer, 'Draw your sword and run me through with it, lest these uncircumcised men come and mistreat me.' But his armor-bearer would not, for he was very afraid. So Saul took his own sword and fell upon it.",
      "M": "Then Saul said to his armor-bearer, 'Draw your sword and run me through, so these uncircumcised men cannot abuse me.' His armor-bearer refused, being terrified, so Saul took his own sword and fell on it.",
      "T": "Saul's last command — 'kill me before the Philistines can' — captures his final humiliation: a king who feared what pagan men might do to him more than what the LORD might say. His armor-bearer, paralyzed with dread, refused. So Saul fell on his own sword — dying by his own hand on the very mountain where he had lost everything."
    },
    "5": {
      "L": "And when his armor-bearer saw that Saul was dead, he also fell on his sword and died.",
      "M": "When his armor-bearer saw that Saul was dead, he too fell on his sword and died.",
      "T": "Loyal to the end in a terrible way, the armor-bearer followed his king into death — one more casualty of a reign that had spent its people."
    },
    "6": {
      "L": "So Saul died, and his three sons died; and all his house died together.",
      "M": "So Saul died, and his three sons died, and all his household died together.",
      "T": "The house of Saul collapsed in a single day: Saul, his three sons, his household — all of them gone. The Chronicler's summary is deliberately total: this is not just a battle loss but the end of an entire royal order."
    },
    "7": {
      "L": "And when all the men of Israel who were in the valley saw that they had fled and that Saul and his sons were dead, they forsook their cities and fled, and the Philistines came and lived in them.",
      "M": "When all the Israelites in the valley saw that the army had fled and that Saul and his sons were dead, they abandoned their cities and fled, and the Philistines moved in and occupied them.",
      "T": "The collapse cascaded outward: army fled, king dead, civilians panicked and abandoned their towns. The Philistines moved into empty Israelite cities — the covenant land reverting to pagan occupation at the moment of Saul's greatest failure."
    },
    "8": {
      "L": "And on the next day, when the Philistines came to strip the slain, they found Saul and his sons fallen on Mount Gilboa.",
      "M": "The next day, when the Philistines came to strip the bodies of the slain, they found Saul and his sons lying on Mount Gilboa.",
      "T": "Morning after the battle: Philistine looters worked the field, stripping armor and weapons from the dead. Among the fallen they found the king — his sons beside him — lying on the mountain that had become his tomb."
    },
    "9": {
      "L": "And they stripped him and took his head and his armor and sent messengers throughout the land of the Philistines to carry the good news to their idols and to the people.",
      "M": "They stripped him, took his head and his armor, and sent word throughout the land of the Philistines to bring the good news to their idols and to the people.",
      "T": "The Philistines treated Saul's defeat as a victory of their gods: his head severed, his armor a trophy, heralds sent across Philistia to announce that their idols had won. The shame of Israel became the celebration of Dagon's people."
    },
    "10": {
      "L": "And they put his armor in the house of their gods and fastened his head in the temple of Dagon.",
      "M": "They placed his armor in the temple of their gods and hung his head in the temple of Dagon.",
      "T": "Saul's armor went to the Philistine gods' treasury; his skull was mounted in Dagon's temple — a gruesome trophy of divine victory in pagan eyes. The man who had been anointed with oil and the Spirit now decorated a pagan shrine."
    },
    "11": {
      "L": "And when all Jabesh-gilead heard all that the Philistines had done to Saul,",
      "M": "When all the men of Jabesh-gilead heard what the Philistines had done to Saul,",
      "T": "The men of Jabesh-gilead heard — the same people Saul had rescued at the very beginning of his reign (1 Sam 11). Loyalty ran deep in those he had once saved."
    },
    "12": {
      "L": "all the valiant men rose and took away the body of Saul and the bodies of his sons and brought them to Jabesh. And they buried their bones under the oak in Jabesh and fasted seven days.",
      "M": "all their valiant men set out, retrieved the bodies of Saul and his sons, and brought them to Jabesh. They buried their bones under the oak tree in Jabesh and fasted for seven days.",
      "T": "Jabesh-gilead's warriors crossed the battlefield at night, reclaimed the king's body and his sons', and carried them home. They buried Saul with dignity under a sacred oak and mourned seven full days — a final act of human loyalty given to a king whom God had already departed."
    },
    "13": {
      "L": "So Saul died for his unfaithfulness. He acted unfaithfully against the LORD in that he did not keep the command of the LORD, and also consulted a medium, seeking guidance.",
      "M": "Saul died because of his unfaithfulness. He acted unfaithfully against the LORD by not keeping the LORD's command and by consulting a medium for guidance.",
      "T": "Here the Chronicler adds what 1 Samuel 31 does not: the theological verdict. Saul died because he broke faith — the same verb used of Israel's deepest covenant failures. He had violated two commands simultaneously: he disobeyed the explicit word of the LORD (1 Sam 15), and he consulted a ghost-diviner (1 Sam 28), turning to the dead for guidance instead of to the living God."
    },
    "14": {
      "L": "He did not inquire of the LORD. Therefore he put him to death and turned the kingdom over to David the son of Jesse.",
      "M": "He did not seek the LORD's guidance; therefore the LORD put him to death and turned the kingdom over to David son of Jesse.",
      "T": "The summary indictment is devastating in its simplicity: Saul never truly sought the LORD. The kingdom did not merely fall — the LORD himself struck Saul down and transferred the crown to David son of Jesse. The nine chapters of genealogy were building to this moment: the legitimate king arrives not by Saul's failure alone but by the LORD's sovereign choice."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '1chronicles')
        merge_tier(existing, CHRONICLES1, tier_key)
        save(tier_dir, '1chronicles', existing)
    print('1 Chronicles 6–10 written.')

if __name__ == '__main__':
    main()
