"""
MKT 1 Chronicles chapters 23–25 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-1chronicles-23-25.py

Content:
- Ch 23: David's final organization of the Levites — numbering, age-requirement change to 20, duties
- Ch 24: The twenty-four courses of priests (Aaronic) and remaining Levites assigned by lot
- Ch 25: The twenty-four courses of musicians — Asaph, Jeduthun, Heman; prophesying with instruments

Translation decisions:
- H3068 (יהוה): "LORD" in L/M; "the LORD" in T. Consistent with all prior OT scripts.
- H430 (אֱלֹהִים): "God" throughout all tiers.
- H4256 (מַחְלֹקֶת, "courses/divisions"): "courses" in L/M/T — the organizational unit of the worship
  calendar. David establishes 24 courses of priests and 24 courses of musicians, each serving in
  rotation.
- H4931 (מִשְׁמֶרֶת, "charge/duty/guard"): "charge" in L/M; "sacred duty" in T. Connotes solemn
  responsibility held in trust before God.
- H5656 (עֲבֹדָה, "service/work"): "service" in worship contexts; "work" where labor is in view.
- H5012 (נָבָא, "prophesy"): "prophesy" in all tiers at 25:1–3. Musical prophecy is not metaphor —
  the Chronicler presents inspired utterance through instruments as genuinely prophetic. The same
  verb used for ecstatic and writing prophets (1 Sam 10:5–6).
- H1486 (גּוֹרָל, "lot"): "lot" in L/M/T. Prov 16:33: "the lot is cast into the lap, but its every
  decision is from the LORD." Human technique, divine outcome.
- H3027 (יָד, "hand"): "under the direction of" (lit. "under the hands of") — conducting was done
  with physical hand movements; the phrase indicates musical leadership.
- H5769 (עוֹלָם, "forever"): "forever" at 23:25 — the LORD has given rest and dwells permanently.
- Age-requirement change (23:24–27): David lowered the Levitical service age from 30 (Num 4:3)
  to 20. His stated reason: the LORD has given rest; the tabernacle no longer travels. The portage
  role of the Levites is obsolete; a permanent sanctuary replaces the portable one. Covenant forms
  adapt when fulfillment arrives. T notes this principle.
- Nadab and Abihu (24:2): They died for offering unauthorized fire (Lev 10:1–2). The Chronicler
  notes their death without naming the cause — the reader is assumed to know. Their childlessness
  meant the priestly line continued only through Eleazar and Ithamar.
- Heman's sons in 25:4 form a hidden prayer-poem in Hebrew when read sequentially:
  חָנֵּנִי יָהּ חָנֵּנִי אַתָּה אֵלִי גִּדַּלְתִּי וְרוֹמַמְתִּי עֶזְרִי יֹשֵׁב בַּצָּרוֹת אָמַרְתִּי מַחְזִיאוֹת
  "Have mercy on me, O Yah; have mercy on me; you are my God; I magnify and exalt my help;
  dwelling in adversities, I declare visions." A prayer encoded in a name-list. T notes at 25:4.
- Abijah course (24:10): The eighth priestly course. Zechariah the priest — father of John the
  Baptist — served in this course when the angel appeared to him (Luke 1:5, 8). T notes.
- Jehoiarib (24:7): First priestly course. The Maccabees (Mattathias, Judas) descended from this
  family (1 Macc 2:1). T notes.
- OT intertextuality: The 24-course system for both priests and musicians creates the permanent
  liturgical framework that will serve through the first temple era, the return from exile, and into
  the second temple period — documented in the Dead Sea Scrolls (4Q320–330).
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
  "23": {
    "1": {
      "L": "Now when David was old and full of days, he made his son Solomon king over Israel.",
      "M": "When David had grown old and had lived a full life, he made his son Solomon king over Israel.",
      "T": "The reign that began with a shepherd's anointing at Bethlehem was coming to its close. David — old and full of days, the Hebrew idiom for a life completely and richly lived — designated Solomon as his successor. What followed in chapters 23–29 is David's final act: organizing the entire worship structure of the temple he would never build."
    },
    "2": {
      "L": "And he gathered together all the princes of Israel with the priests and the Levites.",
      "M": "He assembled all the leaders of Israel together with the priests and Levites.",
      "T": "David's final administrative act was comprehensive: every political leader, every priest, every Levite gathered together. Nothing was improvised. The organization of permanent temple worship was being done publicly, with full institutional witness."
    },
    "3": {
      "L": "And the Levites were numbered from the age of thirty years and upward; and their number, man by man, was thirty-eight thousand.",
      "M": "The Levites were counted, those thirty years old and above; their total, counted individually, was thirty-eight thousand.",
      "T": "Thirty-eight thousand Levites — an enormous body of dedicated servants of the sanctuary. The census followed the ancient Mosaic standard (Num 4:3): thirty years, the age of mature service-readiness. But David was about to revise even this requirement, and his reasons were sound."
    },
    "4": {
      "L": "Of which, twenty-four thousand were to set forward the work of the house of the LORD; and six thousand were officers and judges;",
      "M": "Of these, twenty-four thousand were assigned to oversee the work of the LORD's house, and six thousand were to serve as officials and judges.",
      "T": "The largest cohort — twenty-four thousand — was dedicated to the hands-on work of the sanctuary. Six thousand served in administrative and judicial roles: the temple and the kingdom required both worship and governance, and the Levitical body was large enough to supply both."
    },
    "5": {
      "L": "Moreover four thousand were gatekeepers; and four thousand praised the LORD with the instruments which I made, said David, to praise therewith.",
      "M": "Four thousand were gatekeepers, and four thousand praised the LORD with the instruments David had made for worship.",
      "T": "The gatekeepers held the threshold between the holy and the common — their role was not menial but sacred, the living boundary of the sanctuary. The four thousand musicians used instruments David had personally commissioned: he could not build the temple, but he had designed the instruments that would fill it with praise. The organization of worship was David's last gift."
    },
    "6": {
      "L": "And David divided them into courses among the sons of Levi, namely, Gershon, Kohath, and Merari.",
      "M": "David organized them into divisions according to the three sons of Levi: Gershon, Kohath, and Merari.",
      "T": "The three great clans of Levi — Gershon, Kohath, Merari — became the organizing structure of the temple workforce. The ancient genealogy of Israel's priestly and Levitical families was honored in the arrangement: who you were descended from determined where you served."
    },
    "7": {
      "L": "Of the Gershonites were Laadan and Shimei.",
      "M": "The Gershonite clans: Laadan and Shimei.",
      "T": "Gershon's two primary family lines — Laadan and Shimei — became the units through which Gershonite service was organized. Ancestral names became institutional categories; the dead continued to shape the living through the family structures they had established."
    },
    "8": {
      "L": "The sons of Laadan: the chief was Jehiel, and Zetham, and Joel, three.",
      "M": "The sons of Laadan: Jehiel the head, Zetham, and Joel — three in all.",
      "T": "Three sons of Laadan with Jehiel at their head. These names anchored the Gershonite roster: each head of a family unit would become the identifier for a specific service assignment in the rotation."
    },
    "9": {
      "L": "The sons of Shimei: Shelomith, and Haziel, and Haran, three. These were the chief of the fathers of Laadan.",
      "M": "The sons of Shimei: Shelomith, Haziel, and Haran — three. These were the clan heads belonging to Laadan.",
      "T": "Note the embedded complexity: these are identified as sons of Shimei but are listed as clan heads of Laadan. Shimei was a sub-clan within Laadan's line, and his sons served as family heads within that larger grouping. The precision reflects careful record-keeping that made the permanent rotation system work."
    },
    "10": {
      "L": "And the sons of Shimei were Jahath, Zina, Jeush, and Beriah; these four were the sons of Shimei.",
      "M": "The sons of Shimei were Jahath, Zina, Jeush, and Beriah — four sons.",
      "T": "Shimei also had four sons of his own, giving the Shimei line four potential clan units. The specificity of these lists was not mere archivism: each name represented a family that would rotate through temple service in perpetuity — generation after generation defined by a lot drawn in David's assembly."
    },
    "11": {
      "L": "And Jahath was the chief, Zizah the second; but Jeush and Beriah had not many sons, therefore they were reckoned in one household according to their father's house.",
      "M": "Jahath was the head and Zizah the second. But Jeush and Beriah did not have many sons, so they were counted together as a single family unit.",
      "T": "Jeush and Beriah — two brothers with too few descendants to form independent service units — were merged into a single administrative household. The system adapted to demographic reality: not every family was the same size, but every family was included. The small were accommodated, not excluded."
    },
    "12": {
      "L": "The sons of Kohath: Amram, Izhar, Hebron, and Uzziel, four.",
      "M": "The sons of Kohath: Amram, Izhar, Hebron, and Uzziel — four clans.",
      "T": "Kohath's four sons carried enormous theological weight. Amram was the father of Moses and Aaron — the great lawgiver and the founding high priest came from this same clan. Kohath's line was the most sacred branch of Levi, entrusted with carrying the ark and the innermost sanctuary vessels through the wilderness (Num 3:31)."
    },
    "13": {
      "L": "The sons of Amram: Aaron and Moses. And Aaron was separated, that he should sanctify the most holy things, he and his sons for ever, to burn incense before the LORD, to minister to him, and to bless in his name for ever.",
      "M": "The sons of Amram were Aaron and Moses. Aaron was set apart to consecrate the most holy things — he and his sons in perpetuity — to burn incense before the LORD, to minister to him, and to pronounce blessing in his name forever.",
      "T": "The great separation: from one father, two radically different destinies. Aaron was 'set apart' — הִבְדִּיל hibdil, the same word used for God's act of separating light from darkness in Genesis 1. Aaron's consecration was not earned merit but divine election: to the incense altar, the holy ministry, the Aaronic blessing (Num 6:24–26). His sons would hold this office 'forever' — until the great High Priest arrived who would make every Aaronic type obsolete."
    },
    "14": {
      "L": "Now concerning Moses the man of God, his sons were named of the tribe of Levi.",
      "M": "As for Moses the man of God, his sons were counted among the tribe of Levi.",
      "T": "Moses — called here אִישׁ הָאֱלֹהִים, 'the man of God,' the highest prophetic designation — had sons who did not inherit his unique mediatorial role. They served as Levites, not priests, not prophets. The offices that Moses and Aaron embodied were not dynastically transmissible; Aaron's priesthood passed through his sons, but Moses's prophetic greatness died with him."
    },
    "15": {
      "L": "The sons of Moses were Gershom and Eliezer.",
      "M": "Moses had two sons: Gershom and Eliezer.",
      "T": "Gershom — born in Midian exile, his name meaning 'I have been a stranger there' (Exod 2:22) — and Eliezer — 'my God is help,' named after the escape from Pharaoh (Exod 18:4). Moses's biography was encoded in his sons' names: first a stranger in a foreign land, then rescued by God's helping hand."
    },
    "16": {
      "L": "Of the sons of Gershom: Shebuel was the chief.",
      "M": "The head of Gershom's descendants was Shebuel.",
      "T": "Moses's line continued in Levitical ministry; it simply occupied a different stratum than Aaron's priestly line. Shebuel led Moses's Gershomite descendants in the temple's Levitical service — a son of the greatest prophet serving the sanctuary his father had worshiped in, but from outside the veil."
    },
    "17": {
      "L": "And the sons of Eliezer were Rehabiah the chief. And Eliezer had no other sons, but the sons of Rehabiah were very many.",
      "M": "Eliezer had only one son, Rehabiah, who was the head of his line. Eliezer had no other sons, but Rehabiah's descendants were very numerous.",
      "T": "A narrow root, a wide crown: one son, then many descendants. The fruitfulness of the covenant does not follow human calculation; the thinnest lineage can produce the most abundant fruit. Eliezer's single heir became the ancestor of a great Levitical family — the promise of multiplication continuing through unlikely conduits."
    },
    "18": {
      "L": "Of the sons of Izhar: Shelomith was the chief.",
      "M": "The head of Izhar's line was Shelomith.",
      "T": "Izhar — Kohath's second son, Aaron and Moses's uncle — contributed Shelomith as the family head. The Kohathite clan was being populated with names that would anchor permanent temple assignments; Izhar's descendants took their place in the service structure alongside their more famous cousins."
    },
    "19": {
      "L": "Of the sons of Hebron: Jeriah the first, Amariah the second, Jahaziel the third, and Jekameam the fourth.",
      "M": "Hebron's sons: Jeriah the first, Amariah the second, Jahaziel the third, and Jekameam the fourth.",
      "T": "Four sons of Hebron, each holding a numbered position in the service rotation. The ordinals — first, second, third, fourth — reflect the practical organization of duty assignments: when the rotation came around, these families knew exactly where they stood in the schedule."
    },
    "20": {
      "L": "Of the sons of Uzziel: Michah the first, and Jesiah the second.",
      "M": "Uzziel's sons: Michah the first and Jesiah the second.",
      "T": "Uzziel's two sons completed the Kohathite roster. All four sons of Kohath — Amram, Izhar, Hebron, Uzziel — were represented in the service structure, each contributing family units to the temple workforce. The covenant genealogy had found its institutional expression."
    },
    "21": {
      "L": "The sons of Merari: Mahli and Mushi. The sons of Mahli: Eleazar and Kish.",
      "M": "The sons of Merari: Mahli and Mushi. Mahli's sons: Eleazar and Kish.",
      "T": "Merari — Levi's third son — rounded out the Levitical structure. His two sons gave rise to distinct family branches, each contributing to the temple workforce. The Merarites had originally been responsible for the tabernacle's structural components in the wilderness — now their descendants would maintain the permanent structure that replaced the portable one."
    },
    "22": {
      "L": "And Eleazar died and had no sons, only daughters; and their brothers the sons of Kish married them.",
      "M": "Eleazar died without sons, leaving only daughters. Their cousins, the sons of Kish, married them.",
      "T": "Another inheritance gap resolved by marriage within the family — the pattern established in Numbers 27 and 36 for daughters without brothers: when the male line failed, the family name continued through daughters who married within their clan. The system preserved family continuity and service assignment together, adapting the covenant structure to biological reality."
    },
    "23": {
      "L": "The sons of Mushi: Mahli, and Eder, and Jeremoth, three.",
      "M": "Mushi's sons: Mahli, Eder, and Jeremoth — three sons.",
      "T": "Three sons of Mushi completed the Merarite roster. With this verse the full Levitical structure had been catalogued: Gershon, Kohath, Merari, and all their descendants were located, named, and placed in the service structure of the house of God."
    },
    "24": {
      "L": "These were the sons of Levi after the house of their fathers, even the chief of the fathers, as they were counted by number of names, man by man, who did the work for the service of the house of the LORD, from the age of twenty years and upward.",
      "M": "These were the sons of Levi, organized by their ancestral houses — the heads of families counted individually — all who carried out the service of the LORD's house, from twenty years old and above.",
      "T": "The concluding summary introduces the new age standard: twenty, not thirty. The roll was complete; the assignments were ready. Every Levite from twenty upward had a place in the permanent service structure — a structural change grounded in theological argument, which David provides in the next two verses."
    },
    "25": {
      "L": "For David said, 'The LORD God of Israel has given rest to his people, and he dwells in Jerusalem forever.'",
      "M": "David had said, 'The LORD God of Israel has given his people rest, and he lives in Jerusalem permanently.'",
      "T": "'The LORD has given rest.' The theological logic behind the age change: the rest promised in the Davidic covenant (17:9) had arrived. The wilderness wandering was over; the portable tabernacle would be replaced by a permanent house. When the form of God's presence changes from traveling to dwelling, the forms of service appropriate to travel are no longer required. Fulfillment reshapes the structures that were designed for the journey."
    },
    "26": {
      "L": "And also the Levites shall no more carry the tabernacle or any vessels of it for the service thereof.",
      "M": "The Levites would no longer need to carry the tabernacle or any of its equipment.",
      "T": "The portage role of the Levites — established at the wilderness command of Numbers 4, requiring the physical strength of men aged thirty to fifty to bear the sacred furniture through desert years — was now fulfilled and ended. The tabernacle age was over. What had been the Levites' primary burden became their released obligation. A new era of service had begun."
    },
    "27": {
      "L": "For by the last words of David the Levites were numbered from twenty years old and above.",
      "M": "It was by David's final ordinances that the Levites were counted from twenty years old and up.",
      "T": "David's last official acts were administrative and liturgical ones. 'Last words' here is legislative language — his final authoritative ordinances, not a deathbed whisper. The age revision was a considered statutory change, backed by the theological argument of verses 25–26: a new era of God's dwelling among his people required a recalibrated service framework."
    },
    "28": {
      "L": "Because their office was to wait on the sons of Aaron for the service of the house of the LORD, in the courts, and in the chambers, and in the purifying of all holy things, and the work of the service of the house of God.",
      "M": "Their responsibility was to assist the priests — the sons of Aaron — in the service of the LORD's house: in the courts, in the chambers, in the purification of all holy things, and in the work of the sanctuary.",
      "T": "The Levites' primary function in the permanent temple was assisting: supporting the Aaronic priests who held the innermost responsibilities. Courts, chambers, purification — the complex liturgical life of the sanctuary required specialized support as much as it required the priests themselves. Every Levitical role, however supporting, participated in what the sanctuary accomplished before God. No service was menial; all of it held the holy."
    },
    "29": {
      "L": "Both for the rows of bread, and for the fine flour for the grain offering, and for the unleavened cakes, and for that which is baked in the pan, and for that which is fried, and for all manner of measure and size,",
      "M": "This included the rows of bread and the fine flour for the grain offering — the unleavened cakes, baked goods, fried offerings — and all kinds of measuring and weighing.",
      "T": "The practical detail is remarkable: flour, baking pans, frying pots, measuring vessels. Holy service was not only incense and blood; it was the daily, patient preparation of grain offerings and bread. The holiness of the sanctuary extended into every cooking pot, every measured portion of flour. The hands that carried holy vessels also carried flour-covered pots, and both sets of hands served the LORD."
    },
    "30": {
      "L": "And to stand every morning to thank and praise the LORD, and likewise at evening.",
      "M": "They were also to stand every morning to give thanks and praise to the LORD, and again every evening.",
      "T": "The rhythm of praise: morning and evening, the two hinges of the day, each bracketed with deliberate thanksgiving. The Levitical singers did not perform for audiences; they stood before God — the verb 'stand' (עָמַד amad) carries the sense of presenting oneself before a great person for service. This was court attendance, not concert-giving. Morning and evening they took their posts in God's courts."
    },
    "31": {
      "L": "And to offer all burnt sacrifices unto the LORD in the sabbaths, in the new moons, and on the set feasts, by number, according to the order commanded unto them, continually before the LORD.",
      "M": "And to present all burnt offerings to the LORD on the sabbaths, at the new moons, and at the appointed festivals — in the proper number and according to the prescribed order — as a regular and ongoing practice before the LORD.",
      "T": "Sabbaths, new moons, appointed feasts — the calendar of worship was a covenant calendar, its structure derived from the LORD's own ordinances. The Levites served within this structure 'continually': the worship of God was not occasional but permanent, the unbroken backdrop of Israel's national life. Whatever else changed in the kingdom, the calendar of praise endured."
    },
    "32": {
      "L": "And that they should keep the charge of the tent of meeting, and the charge of the holy place, and the charge of the sons of Aaron their brothers, in the service of the house of the LORD.",
      "M": "They were also responsible for the care of the tent of meeting, the care of the holy place, and the supporting care of the Aaronic priests in the service of the LORD's house.",
      "T": "The final summary of Levitical responsibility: three concentric duties — guarding the meeting place, maintaining the holy area, supporting their priestly brothers. The Levites surrounded and sustained the innermost core of Israel's worship. They did not enter where Aaron's sons entered; they made it possible for Aaron's sons to enter. Their service was indispensable precisely because it was supporting, not self-sufficient."
    }
  },
  "24": {
    "1": {
      "L": "Now these are the divisions of the sons of Aaron: the sons of Aaron were Nadab, Abihu, Eleazar, and Ithamar.",
      "M": "These are the divisions of Aaron's sons. Aaron had four sons: Nadab, Abihu, Eleazar, and Ithamar.",
      "T": "The priestly organization begins with a list shadowed by loss. All four sons of Aaron are named before the tragedy is acknowledged — the full line must be honored before explaining why two of its four branches bore no fruit. Nadab and Abihu stand at the head of the list, not erased from Israel's memory even though their line ended in fire."
    },
    "2": {
      "L": "But Nadab and Abihu died before their father, and had no children; therefore Eleazar and Ithamar executed the priest's office.",
      "M": "Nadab and Abihu died before their father and left no sons, so Eleazar and Ithamar served as the priests.",
      "T": "Nadab and Abihu — felled by fire from the LORD when they offered unauthorized incense (Lev 10:1–2) — died without sons. The priesthood that should have flowed through four channels ran through two. Later, the family of Eli — traced to Ithamar's line — would be removed for corruption (1 Sam 2:31–36), concentrating the high priesthood permanently in Eleazar's Zadokite branch. Two branches lost, one diminished, one dominant: the history of the Aaronic priesthood was shaped by a series of deaths and judgments."
    },
    "3": {
      "L": "David with Zadok from the sons of Eleazar, and Ahimelech from the sons of Ithamar, distributed them according to their offices in their service.",
      "M": "David, together with Zadok from Eleazar's line and Ahimelech from Ithamar's line, assigned them according to their duties and service roles.",
      "T": "David organized the priests through the two senior representatives of the surviving priestly lines: Zadok — who had remained loyal through Absalom's rebellion and would outlast Abiathar to become Solomon's sole high priest — and Ahimelech, Abiathar's son, representing the Ithamar line. The partnership was real but already asymmetrical; the Zadokite line would eventually stand alone."
    },
    "4": {
      "L": "There were more chief men found among the sons of Eleazar than among the sons of Ithamar, and thus were they divided. Among the sons of Eleazar there were sixteen heads of ancestral houses, and eight among the sons of Ithamar.",
      "M": "More family heads were found among Eleazar's descendants than among Ithamar's, so the assignment reflected this: sixteen family heads from Eleazar's line and eight from Ithamar's.",
      "T": "The unequal distribution — sixteen courses from Eleazar, eight from Ithamar — reflected demographic reality. Eleazar's line had grown larger. The organization honored the actual families rather than imposing artificial equality. The lot would later equalize the service schedule, but the number of families was what it was: God's sovereignty working through the history of each household."
    },
    "5": {
      "L": "Thus were they divided by lot, one sort with another; for the governors of the sanctuary, and governors of the house of God, were of the sons of Eleazar and of the sons of Ithamar.",
      "M": "They were assigned by lot — both groups together — for the leaders of the sanctuary and the leaders of God's house were found in both Eleazar's and Ithamar's lines.",
      "T": "The lot equalized what demographics had made unequal: though Eleazar had twice as many families, each family received its service slot by the same divine mechanism. Neither line could claim seniority in the rotation schedule. The lot made God the scheduler — Proverbs 16:33 applies with full weight here: 'the lot is cast into the lap, but its every decision is from the LORD.'"
    },
    "6": {
      "L": "And Shemaiah the son of Nethaneel the scribe, one of the Levites, wrote them before the king and the princes and Zadok the priest and Ahimelech the son of Abiathar, and the heads of the ancestral houses of the priests and Levites; one father's house being drawn for Eleazar and one for Ithamar.",
      "M": "Shemaiah son of Nethaneel, a Levitical scribe, recorded the assignments before the king and the officials, Zadok the priest, Ahimelech son of Abiathar, and the heads of the priestly and Levitical families — alternating one draw from Eleazar's line, then one from Ithamar's.",
      "T": "The scribe Shemaiah recorded everything in the presence of every authority: king, princes, high priest, deputy priest, family heads. The process was fully transparent and publicly witnessed — divine selection through the lot verified by every human institution simultaneously. The alternating draw (one from Eleazar, then one from Ithamar) ensured that the unequal numbers did not result in a lopsided schedule: the two lines served in pairs through the first sixteen courses, then Eleazar's remaining eight filled the final slots."
    },
    "7": {
      "L": "Now the first lot fell to Jehoiarib, the second to Jedaiah,",
      "M": "The first lot fell to Jehoiarib, the second to Jedaiah,",
      "T": "The lots began to fall. Twenty-four courses of priests, each bearing a name that would define a family's service rotation for generations. Jehoiarib first: this is the family that would one day produce the Hasmonean dynasty — Mattathias and Judas Maccabeus descended from this line (1 Macc 2:1). A lot drawn in David's assembly determined the ancestral course of Israel's great liberators."
    },
    "8": {
      "L": "the third to Harim, the fourth to Seorim,",
      "M": "the third to Harim, the fourth to Seorim,",
      "T": "Harim and Seorim — the third and fourth courses assigned. Harim appears among the priests who returned from Babylon with Zerubbabel (Ezra 2:39) and whose descendants made covenant pledges in Nehemiah's time (Neh 10:5). These lot-drawn course names outlasted the monarchy and the temple destruction."
    },
    "9": {
      "L": "the fifth to Malchijah, the sixth to Mijamin,",
      "M": "the fifth to Malchijah, the sixth to Mijamin,",
      "T": "Malchijah — the fifth course — whose descendants appear in Nehemiah 3:11 among those who repaired Jerusalem's walls after the exile. The priests assigned by this lot would serve, be exiled, survive, and return to rebuild the very city whose sanctuary they had served. Course assignments written here endured through catastrophe."
    },
    "10": {
      "L": "the seventh to Hakkoz, the eighth to Abijah,",
      "M": "the seventh to Hakkoz, the eighth to Abijah,",
      "T": "The eighth course: Abijah. This is the course in which Zechariah the priest served when the angel Gabriel appeared to him at the incense altar and announced that his aged wife Elizabeth would conceive and bear a son named John (Luke 1:5, 8–17). The lot drawn in David's tent echoed through centuries into the story of the forerunner of the Messiah. Course assignments have long reach."
    },
    "11": {
      "L": "the ninth to Jeshua, the tenth to Shecaniah,",
      "M": "the ninth to Jeshua, the tenth to Shecaniah,",
      "T": "Jeshua — the ninth course — whose priestly family returned with Zerubbabel from Babylon as one of the leading families of the restoration community (Ezra 2:2, 36). These lot-numbers assigned in David's assembly were the framework within which Israel's priestly service continued across centuries of exile and return."
    },
    "12": {
      "L": "the eleventh to Eliashib, the twelfth to Jakim,",
      "M": "the eleventh to Eliashib, the twelfth to Jakim,",
      "T": "Eliashib — the eleventh course — a name that recurs prominently in Nehemiah's day, when the high priest Eliashib helped build the Sheep Gate and later compromised by installing Tobiah the Ammonite in the temple storeroom (Neh 3:1; 13:4–9). The courses of David's arrangement carried the full arc of Israel's priesthood — faithfulness and failure alike."
    },
    "13": {
      "L": "the thirteenth to Huppah, the fourteenth to Jeshebeab,",
      "M": "the thirteenth to Huppah, the fourteenth to Jeshebeab,",
      "T": "Courses thirteen and fourteen — families whose names appear rarely if ever again in the biblical record beyond this list. Most of the twenty-four courses left no other trace in Scripture; they served faithfully in their rotation for centuries, unnamed in history but present before God. The lot assigned them equally with the dynastically prominent families."
    },
    "14": {
      "L": "the fifteenth to Bilgah, the sixteenth to Immer,",
      "M": "the fifteenth to Bilgah, the sixteenth to Immer,",
      "T": "Immer — the sixteenth course — the family of Pashhur son of Immer, the temple official who struck Jeremiah the prophet and put him in the stocks (Jer 20:1–3). The same priestly family that received a sacred duty assignment from this lot would, centuries later, produce an adversary of God's word. The courses were hereditary; the faithfulness within them was not."
    },
    "15": {
      "L": "the seventeenth to Hezir, the eighteenth to Aphses,",
      "M": "the seventeenth to Hezir, the eighteenth to Aphses,",
      "T": "Courses seventeen and eighteen. The Dead Sea Scrolls (4Q320–330) document all twenty-four priestly courses as the backbone of a liturgical calendar used at Qumran. These names, assigned by lot here, became the organizing framework of Israel's worship for over a thousand years."
    },
    "16": {
      "L": "the nineteenth to Pethahiah, the twentieth to Jehezekel,",
      "M": "the nineteenth to Pethahiah, the twentieth to Jehezekel,",
      "T": "Nineteen and twenty assigned. The calendar was nearly complete — each course a family, each family a week's service twice yearly in the regular rotation, with all twenty-four courses serving together at Passover, Pentecost, and Tabernacles."
    },
    "17": {
      "L": "the twenty-first to Jachin, the twenty-second to Gamul,",
      "M": "the twenty-first to Jachin, the twenty-second to Gamul,",
      "T": "Twenty-one and twenty-two. Two lots remained. The lot-drawing that had begun with Jehoiarib was almost finished, and the complete calendar of priestly service would be established."
    },
    "18": {
      "L": "the twenty-third to Delaiah, the twenty-fourth to Maaziah.",
      "M": "the twenty-third to Delaiah, the twenty-fourth to Maaziah.",
      "T": "Twenty-four courses complete. From Jehoiarib to Maaziah — twenty-four families, twenty-four lots, a full annual cycle of priestly service organized by divine selection. The lot had accomplished what no human scheduler could: made the arrangement simultaneously fair, irreversible, and sacred. No family could protest; the LORD had determined it."
    },
    "19": {
      "L": "These were the orderings of them in their service to enter into the house of the LORD according to their custom, under Aaron their father, as the LORD God of Israel had commanded him.",
      "M": "These were the service assignments for entering the LORD's house according to their prescribed procedure — following their father Aaron's pattern, as the LORD God of Israel had commanded him.",
      "T": "The closing stamp of authority: this arrangement followed the LORD's command to Aaron, not a human innovation. David organized and formalized what God had already ordained at Sinai. The twenty-four courses were not a new creation but the permanent institutional expression of the Aaronic priesthood that God had established through Moses. Order, not improvisation, defined Israel's approach to the holy."
    },
    "20": {
      "L": "Now for the rest of the sons of Levi: from the sons of Amram, Shubael; from the sons of Shubael, Jehdeiah.",
      "M": "Now for the remaining Levites: from Amram's line, Shubael; from Shubael's line, Jehdeiah.",
      "T": "Having organized the priests, the text returns to the broader Levitical family — the non-priestly Levites who also required formal assignment. Shubael descended from Gershom son of Moses (23:16); Jehdeiah was his chief representative. Moses's line, excluded from the priesthood, nonetheless held honored Levitical appointments in the temple service."
    },
    "21": {
      "L": "Concerning Rehabiah: from the sons of Rehabiah, Isshiah the head.",
      "M": "From Rehabiah's line: Isshiah the head.",
      "T": "Rehabiah — the only son of Eliezer (Moses's son), from whom 'very many' descendants came (23:17) — was represented here by Isshiah as family head. The promise of fruitfulness given to Moses's line through Rehabiah was now being channeled into specific, named service assignments."
    },
    "22": {
      "L": "Of the Izharites, Shelomoth; from the sons of Shelomoth, Jahath.",
      "M": "From the Izharite line: Shelomoth; from Shelomoth's line, Jahath.",
      "T": "The Izharite line through Shelomoth (23:18) with Jahath as the next-generation representative. Each entry in this extended Levitical list anchored a family in a permanent place in the service rotation: both the family head and his immediate successor were identified, ensuring continuity across generations."
    },
    "23": {
      "L": "And the sons of Hebron: Jeriah the first, Amariah the second, Jahaziel the third, and Jekameam the fourth.",
      "M": "Hebron's sons: Jeriah the first, Amariah the second, Jahaziel the third, Jekameam the fourth.",
      "T": "The four sons of Hebron from 23:19 reappear in this lot-assignment list — each holding a numbered position in the service calendar. Their repetition here signals that the organizational list in chapter 23 and this lot-drawing list in chapter 24 are complementary records, together establishing both genealogy and assignment."
    },
    "24": {
      "L": "Of the sons of Uzziel, Michah; of the sons of Michah, Shamir.",
      "M": "From Uzziel's line: Michah; from Michah's line, Shamir.",
      "T": "Michah from Uzziel's line (23:20) with his son Shamir in the extended assignment list. The service structure reached into the next generation: not only the founding family heads but their immediate heirs were identified for specific duty, ensuring unbroken continuity of service."
    },
    "25": {
      "L": "The brother of Michah was Isshiah; of the sons of Isshiah, Zechariah.",
      "M": "Michah's brother was Isshiah; Isshiah's son was Zechariah.",
      "T": "Sibling lines were carefully tracked: Michah's branch and his brother Isshiah's branch each contributed to the Levitical workforce. The second generation — Zechariah son of Isshiah — was already named and placed. The institutional memory was deep, reaching across at least three generations from Uzziel."
    },
    "26": {
      "L": "The sons of Merari: Mahli and Mushi. The sons of Jaaziah, his son, Beno.",
      "M": "The sons of Merari: Mahli and Mushi. And from Jaaziah — another of Merari's descendants — his son Beno.",
      "T": "Merari's standard two sons (Mahli and Mushi) are joined by a third branch through Jaaziah — a name not mentioned in Numbers 3 or 1 Chronicles 23, suggesting either an additional branch not previously recorded, or a family head who had established a recognized Merarite sub-clan between David's census of 23:6 and this lot-drawing. Every Merarite family had a place."
    },
    "27": {
      "L": "The sons of Merari by Jaaziah: Beno, Shoham, Zaccur, and Ibri.",
      "M": "Jaaziah's descendants in the Merarite line: Beno, Shoham, Zaccur, and Ibri.",
      "T": "Four sons of the Jaaziah branch — four additional Levitical family units available for service. The roster was comprehensive: the goal was to leave no Levitical family without a place in the permanent service structure, whether their line was ancient or recently established."
    },
    "28": {
      "L": "Of Mahli: Eleazar, who had no sons.",
      "M": "Mahli's son Eleazar had no sons.",
      "T": "Eleazar of Mahli — the same situation noted in 23:22 — died without male heirs. His daughters married within the family (23:22), continuing the line biologically; but his personal branch in the service register ended here. The childless are named; their absence in the next generation is honestly recorded. Nothing is edited out of the family history."
    },
    "29": {
      "L": "Of Kish: the son of Kish was Jerahmeel.",
      "M": "Kish's line: his son Jerahmeel.",
      "T": "Kish — who had married Eleazar's daughters to continue that line (23:22) — was represented here by his son Jerahmeel. The family that had been extended through adoption served in the rotation fully legitimately: Jerahmeel stood in the service register as his grandfather Kish's heir, the biological gap bridged by covenant marriage."
    },
    "30": {
      "L": "The sons of Mushi also: Mahli, Eder, and Jerimoth. These were the sons of the Levites after their ancestral houses.",
      "M": "Also Mushi's sons: Mahli, Eder, and Jerimoth. These were the Levites, organized by their ancestral families.",
      "T": "Mushi's three sons completed the Merarite roster (23:23). The closing formula — 'these were the sons of the Levites after their ancestral houses' — sealed the entire enumeration. Every family, every branch, every descendant had been located, named, and placed in the service structure. The register was complete; the service could begin."
    },
    "31": {
      "L": "These also cast lots over against their brothers the sons of Aaron, in the presence of King David and Zadok and Ahimelech and the heads of the ancestral houses of the priests and Levites, chief fathers as well as the younger brothers.",
      "M": "These Levites also cast lots alongside their priestly brothers the sons of Aaron, before King David, Zadok, Ahimelech, and the heads of the priestly and Levitical families — regardless of whether they were senior or junior.",
      "T": "The Levitical lot-drawing mirrored the priestly one exactly: same witnesses, same procedure, same governing principle. Senior families and junior families cast lots together — no seniority exemption, no family privilege. The lot made every service slot equally dignified and equally God's to assign. Before the king, the priests, and all the family heads, the permanent organization of Israel's worship was completed."
    }
  },
  "25": {
    "1": {
      "L": "Moreover David and the commanders of the host set apart for the service the sons of Asaph, and of Heman, and of Jeduthun, who should prophesy with harps, with psalteries, and with cymbals; and the number of those doing the service was:",
      "M": "David and the military commanders set apart for service the sons of Asaph, Heman, and Jeduthun, who were to prophesy with harps, lyres, and cymbals. The roster of those serving was:",
      "T": "Music as prophecy: the Chronicler uses נָבָא ('prophesy') three times in this chapter (vv.1–3), making unmistakably clear that the temple musicians were not merely performers but prophetic voices. Their harps and lyres were instruments of inspired utterance — the same Hebrew verb used for the ecstatic bands of Samuel's era (1 Sam 10:5–6) and for the great writing prophets. Sacred music is revelation in sound: it does not merely describe God but enacts his presence. David and his military commanders — the men who organized armies for battle — organized this corps of musical prophets, understanding that what happened before God's throne required inspired proclamation as much as ritual precision."
    },
    "2": {
      "L": "Of the sons of Asaph: Zaccur, Joseph, Nethaniah, and Asarelah, sons of Asaph, under the direction of Asaph, who prophesied according to the order of the king.",
      "M": "From Asaph's line: Zaccur, Joseph, Nethaniah, and Asarelah — Asaph's sons, serving under Asaph's direction, who prophesied according to the king's command.",
      "T": "Asaph — author of Psalms 50 and 73–83, the great temple poet of prophetic insight — directed his four sons in inspired musical ministry. 'According to the order of the king' does not reduce the prophecy to royal performance: David himself was a man of prophetic Spirit (2 Sam 23:2), and his commission carried the weight of covenant authorization. Asaph's sons prophesied because a spirit-filled king commanded them to, and a God-given gift enabled them to."
    },
    "3": {
      "L": "Of Jeduthun: the sons of Jeduthun; Gedaliah, Zeri, Jeshaiah, Shimei, Hashabiah, and Mattithiah, six, under the direction of their father Jeduthun, who prophesied with the harp in giving thanks and praising the LORD.",
      "M": "From Jeduthun's line: his sons Gedaliah, Zeri, Jeshaiah, Shimei, Hashabiah, and Mattithiah — six — under their father Jeduthun's direction, who prophesied with the harp, giving thanks and praising the LORD.",
      "T": "Jeduthun — also known as Ethan (1 Chr 6:44; 15:17) — led six sons in harp-prophecy of thanksgiving and praise. The content of prophetic music here was not primarily predictive but doxological: announcing what is true about God right now. Thanksgiving and praise are a form of truthful proclamation — they declare the character and acts of God into the ears of the worshiping community. The prophet who praises is telling the truth about reality."
    },
    "4": {
      "L": "Of Heman: the sons of Heman: Bukkiah, Mattaniah, Uzziel, Shebuel, Jerimoth, Hananiah, Hanani, Eliathah, Giddalti, Romamtiezer, Joshbekashah, Mallothi, Hothir, and Mahazioth.",
      "M": "From Heman's line: his sons Bukkiah, Mattaniah, Uzziel, Shebuel, Jerimoth, Hananiah, Hanani, Eliathah, Giddalti, Romamtiezer, Joshbekashah, Mallothi, Hothir, and Mahazioth.",
      "T": "Heman had fourteen sons — more than Asaph's four or Jeduthun's six. But these names carry a secret: read sequentially in Hebrew, they form a prayer-poem — חָנֵּנִי יָהּ חָנֵּנִי אַתָּה אֵלִי גִּדַּלְתִּי וְרוֹמַמְתִּי עֶזְרִי יֹשֵׁב בַּצָּרוֹת אָמַרְתִּי מַחְזִיאוֹת — 'Have mercy on me, O Yah; have mercy on me; you are my God; I magnify and exalt my help; dwelling in adversities, I declare visions.' The names in this family register encode a confession of faith. Heman did not merely name his children — he inscribed a prayer into the genealogical record itself. The seer's name-list was his last song."
    },
    "5": {
      "L": "All these were sons of Heman the king's seer, in the words of God, to lift up the horn. And God gave Heman fourteen sons and three daughters.",
      "M": "All these were sons of Heman, the king's seer — given according to God's word to exalt his horn. God had given Heman fourteen sons and three daughters.",
      "T": "Heman was the king's חֹזֶה, 'the seer' — the prophetic musician whose inspired vision served the royal court. His fourteen sons were not only biological offspring but the fulfillment of a divine word: God had given them 'to lift up the horn' — to raise the banner of praise and prophetic proclamation before God's throne. Three daughters were also given; the women of this family participated in the sacred music ministry. The whole household was recruited into the service of God's house."
    },
    "6": {
      "L": "All these were under the direction of their father for song in the house of the LORD, with cymbals, psalteries, and harps, for the service of the house of God, according to the king's order to Asaph, Jeduthun, and Heman.",
      "M": "All these sons served under their father's direction in music for the LORD's house, with cymbals, lyres, and harps, for the service of God's house — under the king's order given to Asaph, Jeduthun, and Heman.",
      "T": "Three master musicians, three inspired voices — Asaph, Jeduthun, Heman — each leading a family choir under the king's sacred commission. Cymbals, lyres, harps: percussion, plucked strings, resonant strings — the full range of ancient sacred sound filled the courts. The house of God would not be silent. It would be filled with the voices of sons trained by fathers whose music was itself a form of prophecy — art in the service of revelation."
    },
    "7": {
      "L": "So the number of them, with their brethren that were instructed in the songs of the LORD, even all that were skilled, was two hundred and eighty-eight.",
      "M": "Including their skilled fellow musicians who were trained in the LORD's songs, the total was 288.",
      "T": "Two hundred eighty-eight trained musicians — twelve for each of the twenty-four courses. The word 'instructed' (מְלֻמָּד mulamad) means taught, shaped, formed through sustained practice: these were not naturals performing raw talent but artists who had been patiently trained in the tradition. Sacred music, like all worship that truly honors God, requires discipline as much as inspiration. Gift and formation together — the combination the Chronicler consistently honors."
    },
    "8": {
      "L": "And they cast lots, ward against ward, as well the small as the great, the teacher as the scholar.",
      "M": "They cast lots for their duty assignments, regardless of rank — whether great or small, teacher or student alike.",
      "T": "The lot leveled every hierarchy: master musicians cast lots alongside apprentices; senior figures received the same divine assignment process as junior ones. No one could claim a preferred service week by seniority, reputation, or family size. The lot made God the scheduler and made all service equally honored before him. Great and small stood at the same table, shook the same cup, and waited for God's decision."
    },
    "9": {
      "L": "Now the first lot came forth for Asaph to Joseph: he and his brothers and sons, twelve. The second to Gedaliah: he and his brothers and sons, twelve.",
      "M": "The first lot fell to Joseph from Asaph's family — he and his brothers and sons, twelve. The second fell to Gedaliah — he and his brothers and sons, twelve.",
      "T": "The lots began. Joseph son of Asaph drew the first course — Asaph's family opened the worship calendar. Gedaliah son of Jeduthun drew second. In the very first two courses the lot had already moved between two master musicians' families, signaling that the rotation would genuinely interleave all three traditions of prophetic music throughout the year."
    },
    "10": {
      "L": "The third to Zaccur: his sons and brothers, twelve.",
      "M": "The third lot fell to Zaccur — his sons and brothers, twelve.",
      "T": "Zaccur from Asaph's line drew third. Three courses assigned and the rotation had already drawn from both Asaph and Jeduthun — no single master's family would dominate the schedule."
    },
    "11": {
      "L": "The fourth to Izri: his sons and brothers, twelve.",
      "M": "The fourth lot fell to Izri — his sons and brothers, twelve.",
      "T": "Izri — likely 'Zeri' of verse 3, under a variant spelling — from Jeduthun's family drew fourth. The lot moved freely between families, creating a genuinely mixed calendar rather than a sequential family block."
    },
    "12": {
      "L": "The fifth to Nethaniah: his sons and brothers, twelve.",
      "M": "The fifth lot fell to Nethaniah — his sons and brothers, twelve.",
      "T": "Nethaniah from Asaph's line (v.2). The fifth course was his — a service slot that would fall twice a year in the standard rotation, with all courses joining for the three great pilgrimage feasts."
    },
    "13": {
      "L": "The sixth to Bukkiah: his sons and brothers, twelve.",
      "M": "The sixth lot fell to Bukkiah — his sons and brothers, twelve.",
      "T": "Bukkiah — the first of Heman's fourteen sons (v.4) — drew the sixth course. Heman's large family entered the rotation here, contributing its first service slot to the calendar of temple worship."
    },
    "14": {
      "L": "The seventh to Jesharelah: his sons and brothers, twelve.",
      "M": "The seventh lot fell to Jesharelah — his sons and brothers, twelve.",
      "T": "Jesharelah — 'Asarelah' of verse 2 under a variant spelling — from Asaph's family. The seventh course filled."
    },
    "15": {
      "L": "The eighth to Jeshaiah: his sons and brothers, twelve.",
      "M": "The eighth lot fell to Jeshaiah — his sons and brothers, twelve.",
      "T": "Jeshaiah from Jeduthun's line (v.3). The second third of the calendar was being filled, and all three master musicians had now contributed to the rotation."
    },
    "16": {
      "L": "The ninth to Mattaniah: his sons and brothers, twelve.",
      "M": "The ninth lot fell to Mattaniah — his sons and brothers, twelve.",
      "T": "Mattaniah from Heman's line (v.4). The lot moved freely among all three traditions. Nine courses placed; fifteen to go."
    },
    "17": {
      "L": "The tenth to Shimei: his sons and brothers, twelve.",
      "M": "The tenth lot fell to Shimei — his sons and brothers, twelve.",
      "T": "Shimei — from Jeduthun's line (v.3). Ten courses complete: the first third of the year's worship calendar assigned by divine lot."
    },
    "18": {
      "L": "The eleventh to Azareel: his sons and brothers, twelve.",
      "M": "The eleventh lot fell to Azareel — his sons and brothers, twelve.",
      "T": "Azareel — likely 'Uzziel' of verse 4 under a variant spelling — from Heman's line. Eleven courses down; the second half approached."
    },
    "19": {
      "L": "The twelfth to Hashabiah: his sons and brothers, twelve.",
      "M": "The twelfth lot fell to Hashabiah — his sons and brothers, twelve.",
      "T": "Hashabiah from Jeduthun's line (v.3). Halfway through the calendar — twelve courses drawn, twelve remaining. The worship structure of the temple was half built by the lot."
    },
    "20": {
      "L": "The thirteenth to Shubael: his sons and brothers, twelve.",
      "M": "The thirteenth lot fell to Shubael — his sons and brothers, twelve.",
      "T": "Shubael from Heman's line (v.4). The second half of the year's service courses had begun. The lot continued its unbiased march through the family rosters."
    },
    "21": {
      "L": "The fourteenth to Mattithiah: his sons and brothers, twelve.",
      "M": "The fourteenth lot fell to Mattithiah — his sons and brothers, twelve.",
      "T": "Mattithiah from Jeduthun's line (v.3). Fourteen of twenty-four assigned — the musical calendar more than half built. Each lot drawn bound a family to a service week that would recur twice annually for as long as the temple stood."
    },
    "22": {
      "L": "The fifteenth to Jeremoth: his sons and brothers, twelve.",
      "M": "The fifteenth lot fell to Jeremoth — his sons and brothers, twelve.",
      "T": "Jeremoth from Heman's line (v.4). The arrangement continued its steady progress. Nine courses remained."
    },
    "23": {
      "L": "The sixteenth to Hananiah: his sons and brothers, twelve.",
      "M": "The sixteenth lot fell to Hananiah — his sons and brothers, twelve.",
      "T": "Hananiah from Heman's line (v.4). Sixteen of twenty-four complete. The calendar's final third was being shaped."
    },
    "24": {
      "L": "The seventeenth to Joshbekashah: his sons and brothers, twelve.",
      "M": "The seventeenth lot fell to Joshbekashah — his sons and brothers, twelve.",
      "T": "Joshbekashah from Heman's line (v.4). The lots had created a genuinely divine calendar — not alphabetical, not ordered by family preference, not ranked by seniority. The sequence was irreducible to human logic, which was exactly the point: this was not human scheduling but divine assignment."
    },
    "25": {
      "L": "The eighteenth to Hanani: his sons and brothers, twelve.",
      "M": "The eighteenth lot fell to Hanani — his sons and brothers, twelve.",
      "T": "Hanani from Heman's line (v.4). Eighteen of twenty-four placed; the worship calendar was nearly complete. Six service slots remained."
    },
    "26": {
      "L": "The nineteenth to Mallothi: his sons and brothers, twelve.",
      "M": "The nineteenth lot fell to Mallothi — his sons and brothers, twelve.",
      "T": "Mallothi from Heman's line (v.4). Five courses remained after this one. The final stretch of lot-drawing was underway."
    },
    "27": {
      "L": "The twentieth to Eliathah: his sons and brothers, twelve.",
      "M": "The twentieth lot fell to Eliathah — his sons and brothers, twelve.",
      "T": "Eliathah from Heman's line (v.4). Four courses to go. The long family of Heman — the king's seer with fourteen sons — had contributed many of the final courses, their large roster filling the latter portion of the calendar."
    },
    "28": {
      "L": "The twenty-first to Hothir: his sons and brothers, twelve.",
      "M": "The twenty-first lot fell to Hothir — his sons and brothers, twelve.",
      "T": "Hothir from Heman's line (v.4). Three courses left. The prayer that Heman encoded in his sons' names — 'Have mercy on me, O Yah' — was about to be fully expressed in the service rotation his family would perform before God."
    },
    "29": {
      "L": "The twenty-second to Giddalti: his sons and brothers, twelve.",
      "M": "The twenty-second lot fell to Giddalti — his sons and brothers, twelve.",
      "T": "Giddalti from Heman's line (v.4). Two courses remained. The worship calendar was almost finished."
    },
    "30": {
      "L": "The twenty-third to Mahazioth: his sons and brothers, twelve.",
      "M": "The twenty-third lot fell to Mahazioth — his sons and brothers, twelve.",
      "T": "Mahazioth from Heman's line (v.4). The twenty-third course placed. One lot remained."
    },
    "31": {
      "L": "The twenty-fourth to Romamtiezer: his sons and brothers, twelve.",
      "M": "The twenty-fourth lot fell to Romamtiezer — his sons and brothers, twelve.",
      "T": "Romamtiezer — 'I have exalted help' — drew the final lot and completed the calendar. Twenty-four courses of musicians: Asaph's four sons, Jeduthun's six, and Heman's fourteen — all interleaved by divine lot into a year-round ministry of prophetic music before God. The great seer's hidden prayer was now woven into the permanent fabric of Israel's worship. Every week someone would stand before the LORD and lift up the song that Heman had encoded in his children's names."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '1chronicles')
        merge_tier(existing, CHRONICLES1, tier_key)
        save(tier_dir, '1chronicles', existing)
    print('1 Chronicles 23–25 written.')

if __name__ == '__main__':
    main()
