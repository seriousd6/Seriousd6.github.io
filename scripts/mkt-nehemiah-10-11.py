"""
MKT Nehemiah chapters 10–11 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-nehemiah-10-11.py

Translation decisions:
- H3068 (יהוה): "LORD" in L and M; "the LORD" in T — consistent with all prior Nehemiah scripts.
- H430 (אֱלֹהִים): "God" throughout. "our God" where the Hebrew has אֱלֹהֵינוּ.
- H8451 (תּוֹרָה, Torah): "the Law" in L and M; "the Torah" or "the Law" in T depending on register.
- H113 (אָדוֹן, adon): "Lord" — "the LORD our Lord" (v29) distinguishes יהוה from אָדוֹן correctly.
- H5650 (עֶבֶד, eved): "servant" — Moses is "the servant of God" (v29), a formulaic Mosaic title.
- H2706 (חֹק, ḥoq): "statute" in L/M; T may vary for readability.
- H4687 (מִצְוָה, mitzvah): "commandment" in all tiers.
- H4941 (מִשְׁפָּט, mishpat): "ordinance" in L/M; T uses "ruling" or "ordinance."
- H7676 (שַׁבָּת, shabbat): "Sabbath" — preserved in all tiers.
- H423 / H7621 (oath/curse, v29): The text uses both H423 (aláh = imprecatory oath, the curse-formula
  if the pledge is broken) and H7621 (shevu'ah = solemn oath). L: "a curse and an oath." T explains
  the combined self-malediction structure: 'may this curse fall on us if we break it.'
- First-person shift (vv30–39): The text shifts from third-person narrative to first-person "we" at
  v30. This is the actual covenant document text reproduced verbatim, not Nehemiah's narration. L
  preserves the shift faithfully; M maintains it; T makes the significance explicit at the transition.
- H3027 (hand) as "debt" at 10:31: H4853 (exaction/burden) + H3027 (hand) = "the exaction of every
  hand" = cancellation of every outstanding debt. A Deuteronomy 15 sabbatical-year release. L renders
  literally; M/T render as "cancellation of every debt."
- H7992 (third part, v32): The temple tax here is one-third of a shekel, not the half-shekel of
  Exodus 30:13. The difference likely reflects postexilic economic constraints. T notes this.
- H4635 (showbread/bread of the Presence, v33): "showbread" in L/M; "bread of the Presence" in T.
- H8548 (tamid, continual, v33): "continual" in L/M; T names it "the perpetual offering (tamid)."
- H6182 (first of dough, v37): the ḥallah contribution (Numbers 15:19-21). L: "first of our dough";
  T identifies the technical term and Mosaic reference.
- Wood offering (v34): not explicitly mandated in the Mosaic law but an ancient practice; Nehemiah
  institutionalizes it by lot as a sustained covenant obligation. T notes this.
- H1486 (lots, 11:1): "lots" throughout.
- H5068 (willingly offered, 11:2): "willingly offered" in L/M; T: "volunteered beyond what the lot
  required." These went above and beyond the covenant obligation.
- "Tirshatha" (v1): Persian governor title. L preserves it; M "the governor"; T expands.
- H5411 (Nethinim): "temple servants" in M/T; L preserves "Nethinim" as a technical term.
- OT echoes: 10:30 echoes Deuteronomy 7 (no intermarriage); 10:31 echoes Deuteronomy 15 (sabbatical
  release); 10:32 echoes Exodus 30 (temple tax); 10:34 echoes Nehemiah's own administration of the
  wood supply; 10:35-36 echo Exodus 23 and Numbers 18 (firstfruits, firstborn); 10:37 echoes Numbers
  15 and 18 (ḥallah, tithes). T surfaces these connections where they shed theological light.
- Chapter 11 geographic lists: L and M follow the list structure faithfully. T frames the theological
  function (covenant lottery at the opening; reconstitution of tribal territories in the closing).
- Aspect: Hebrew narrative past (waw-consecutive imperfect) throughout the narrative sections.
  The covenant pledge sections (10:29-39) use the infinitive construct for ongoing obligations.
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

NEHEMIAH = {
  "10": {
    "1": {
      "L": "Now those who sealed were: Nehemiah the Tirshatha, the son of Hachaliah, and Zidkijah,",
      "M": "Those who sealed the document were: Nehemiah the governor, son of Hacaliah, and Zedekiah,",
      "T": "The covenant was put in writing and sealed with names. First on the document: Nehemiah the governor—the Tirshatha, his Persian administrative title—son of Hacaliah, and Zedekiah."
    },
    "2": {
      "L": "Seraiah, Azariah, Jeremiah,",
      "M": "Seraiah, Azariah, Jeremiah,",
      "T": "Priests: Seraiah, Azariah, Jeremiah,"
    },
    "3": {
      "L": "Pashur, Amariah, Malchijah,",
      "M": "Pashur, Amariah, Malchijah,",
      "T": "Pashur, Amariah, Malchijah,"
    },
    "4": {
      "L": "Hattush, Shebaniah, Malluch,",
      "M": "Hattush, Shebaniah, Malluch,",
      "T": "Hattush, Shebaniah, Malluch,"
    },
    "5": {
      "L": "Harim, Meremoth, Obadiah,",
      "M": "Harim, Meremoth, Obadiah,",
      "T": "Harim, Meremoth, Obadiah,"
    },
    "6": {
      "L": "Daniel, Ginnethon, Baruch,",
      "M": "Daniel, Ginnethon, Baruch,",
      "T": "Daniel, Ginnethon, Baruch,"
    },
    "7": {
      "L": "Meshullam, Abijah, Mijamin,",
      "M": "Meshullam, Abijah, Mijamin,",
      "T": "Meshullam, Abijah, Mijamin,"
    },
    "8": {
      "L": "Maaziah, Bilgai, Shemaiah: these were the priests.",
      "M": "Maaziah, Bilgai, Shemaiah. These were the priests.",
      "T": "Maaziah, Bilgai, Shemaiah. Twenty-one priests sealed the covenant."
    },
    "9": {
      "L": "And the Levites: Jeshua the son of Azaniah, Binnui of the sons of Henadad, Kadmiel;",
      "M": "And the Levites: Jeshua son of Azaniah, Binnui of the sons of Henadad, Kadmiel;",
      "T": "Levites: Jeshua son of Azaniah, Binnui of the Henadad line, Kadmiel;"
    },
    "10": {
      "L": "and their brethren, Shebaniah, Hodijah, Kelita, Pelaiah, Hanan,",
      "M": "and their associates: Shebaniah, Hodijah, Kelita, Pelaiah, Hanan,",
      "T": "and their colleagues: Shebaniah, Hodijah, Kelita, Pelaiah, Hanan,"
    },
    "11": {
      "L": "Micha, Rehob, Hashabiah,",
      "M": "Micha, Rehob, Hashabiah,",
      "T": "Micha, Rehob, Hashabiah,"
    },
    "12": {
      "L": "Zaccur, Sherebiah, Shebaniah,",
      "M": "Zaccur, Sherebiah, Shebaniah,",
      "T": "Zaccur, Sherebiah, Shebaniah,"
    },
    "13": {
      "L": "Hodijah, Bani, Beninu.",
      "M": "Hodijah, Bani, Beninu.",
      "T": "Hodijah, Bani, Beninu. Seventeen Levites put their names to the covenant."
    },
    "14": {
      "L": "The chiefs of the people: Parosh, Pahath-moab, Elam, Zattu, Bani,",
      "M": "The leaders of the people: Parosh, Pahath-moab, Elam, Zattu, Bani,",
      "T": "The leaders of the people: Parosh, Pahath-moab, Elam, Zattu, Bani,"
    },
    "15": {
      "L": "Bunni, Azgad, Bebai,",
      "M": "Bunni, Azgad, Bebai,",
      "T": "Bunni, Azgad, Bebai,"
    },
    "16": {
      "L": "Adonijah, Bigvai, Adin,",
      "M": "Adonijah, Bigvai, Adin,",
      "T": "Adonijah, Bigvai, Adin,"
    },
    "17": {
      "L": "Ater, Hezekiah, Azzur,",
      "M": "Ater, Hezekiah, Azzur,",
      "T": "Ater, Hezekiah, Azzur,"
    },
    "18": {
      "L": "Hodijah, Hashum, Bezai,",
      "M": "Hodijah, Hashum, Bezai,",
      "T": "Hodijah, Hashum, Bezai,"
    },
    "19": {
      "L": "Hariph, Anathoth, Nebai,",
      "M": "Hariph, Anathoth, Nebai,",
      "T": "Hariph, Anathoth, Nebai,"
    },
    "20": {
      "L": "Magpiash, Meshullam, Hezir,",
      "M": "Magpiash, Meshullam, Hezir,",
      "T": "Magpiash, Meshullam, Hezir,"
    },
    "21": {
      "L": "Meshezabeel, Zadok, Jaddua,",
      "M": "Meshezabeel, Zadok, Jaddua,",
      "T": "Meshezabeel, Zadok, Jaddua,"
    },
    "22": {
      "L": "Pelatiah, Hanan, Anaiah,",
      "M": "Pelatiah, Hanan, Anaiah,",
      "T": "Pelatiah, Hanan, Anaiah,"
    },
    "23": {
      "L": "Hoshea, Hananiah, Hasshub,",
      "M": "Hoshea, Hananiah, Hasshub,",
      "T": "Hoshea, Hananiah, Hasshub,"
    },
    "24": {
      "L": "Hallohesh, Pileha, Shobek,",
      "M": "Hallohesh, Pileha, Shobek,",
      "T": "Hallohesh, Pileha, Shobek,"
    },
    "25": {
      "L": "Rehum, Hashabnah, Maaseiah,",
      "M": "Rehum, Hashabnah, Maaseiah,",
      "T": "Rehum, Hashabnah, Maaseiah,"
    },
    "26": {
      "L": "and Ahijah, Hanan, Anan,",
      "M": "Ahijah, Hanan, Anan,",
      "T": "Ahijah, Hanan, Anan,"
    },
    "27": {
      "L": "Malluch, Harim, Baanah.",
      "M": "Malluch, Harim, Baanah.",
      "T": "Malluch, Harim, Baanah. Forty-four leaders of the people sealed the document."
    },
    "28": {
      "L": "And the rest of the people—the priests, the Levites, the gatekeepers, the singers, the Nethinim, and all who had separated themselves from the peoples of the lands to the Law of God, their wives, their sons, their daughters, all who had knowledge and understanding—",
      "M": "The rest of the people—the priests, the Levites, the gatekeepers, the singers, the temple servants, and all who had separated themselves from the surrounding peoples to follow the Law of God, along with their wives, sons, and daughters, all who were old enough to know and understand—",
      "T": "Behind the named signatories stood everyone else: the priests, Levites, gatekeepers, singers, temple servants—and all who had deliberately separated themselves from the surrounding peoples and committed to the Law of God. Their families too: wives, sons, daughters, all who were old enough to grasp what they were joining."
    },
    "29": {
      "L": "they clung to their brethren, their nobles, and entered into a curse and into an oath to walk in God's Law, which was given by Moses the servant of God, and to observe and to do all the commandments of the LORD our Lord and his ordinances and his statutes;",
      "M": "they joined with their leaders and bound themselves with a sworn oath to walk in God's Law, which was given through Moses the servant of God, and to observe and obey all the commandments, ordinances, and statutes of the LORD our Lord.",
      "T": "They threw their weight behind the leaders and entered into a binding covenant formula—both an oath and a self-imprecation: 'May this curse fall on us if we break this.' Their pledge: to walk in God's Law as it came through Moses the servant of God, and to keep every commandment, every ruling, every statute that the LORD our Lord had set down."
    },
    "30": {
      "L": "and that we would not give our daughters to the peoples of the land, nor take their daughters for our sons;",
      "M": "We commit that we will not give our daughters in marriage to the peoples of the land, nor take their daughters for our sons.",
      "T": "Here the covenant shifts to first person—the actual text of what they pledged: We will not give our daughters to the peoples of the land. We will not take their daughters for our sons. Deuteronomy 7 had named exactly this intermarriage as the path by which Israel had been drawn away from God before."
    },
    "31": {
      "L": "and if the peoples of the land bring merchandise or any grain on the Sabbath day to sell, we will not buy from them on the Sabbath or on a holy day; and we will forego the seventh year and the exaction of every debt.",
      "M": "If the peoples of the land bring merchandise or grain to sell on the Sabbath, we will not buy from them on the Sabbath or on any holy day. And we will observe the seventh year by leaving the land fallow and by canceling every outstanding debt.",
      "T": "If merchants from the surrounding peoples come with goods or grain on the Sabbath, we will not buy. Not on the Sabbath, not on any holy day. And every seventh year we will let the land rest and cancel every debt outstanding—as Deuteronomy 15 commands. The sabbatical release was a structural covenant act: the economy of Israel was supposed to breathe, to periodically reset, to refuse the permanent indebtedness that afflicted the nations around them."
    },
    "32": {
      "L": "Also we imposed upon ourselves the charge to give yearly a third part of a shekel for the service of the house of our God:",
      "M": "We also take on ourselves the obligation to give annually a third of a shekel for the service of the house of our God.",
      "T": "We also impose on ourselves a temple tax: a third of a shekel per person per year for the maintenance of the house of God. (Exodus 30:13 set the temple tax at half a shekel; the reduced amount here likely reflects the economic constraints of the returning community, or a different calculation basis. The obligation itself echoes the Mosaic precedent.)"
    },
    "33": {
      "L": "for the showbread, and the regular grain offering, and the regular burnt offering, of the Sabbaths, of the new moons, for the appointed feasts, and for the holy things, and for the sin offerings to make atonement for Israel, and for all the work of the house of our God.",
      "M": "This covers the bread of the Presence, the regular grain offering, the regular burnt offering, the Sabbath and new moon offerings, the appointed feast offerings, the dedicated holy things, the sin offerings to make atonement for Israel, and all the work of the house of our God.",
      "T": "What the tax funds: the bread of the Presence set before the LORD; the perpetual grain and burnt offerings—the tamid, the twice-daily sacrifice that marked every day as belonging to God; the Sabbath and new moon sacrifices; all the appointed-feast offerings; the holy articles set apart for God's use; the sin offerings that make atonement for all Israel; and every aspect of maintaining the house of God. The tax is small; what it sustains is the whole apparatus of Israel's covenant worship."
    },
    "34": {
      "L": "We cast lots also among the priests, the Levites, and the people for the wood offering, to bring it into the house of our God, by our fathers' houses, at times appointed, year by year, to burn on the altar of the LORD our God, as it is written in the Law.",
      "M": "We—priests, Levites, and people—cast lots for the wood offering, determining which family would bring wood to the house of our God at their appointed time each year, to burn on the altar of the LORD our God, as it is written in the Law.",
      "T": "The altar fires need fuel: someone must bring wood. We cast lots—priests, Levites, and people together—to assign each ancestral house its appointed time, year by year, so the altar of the LORD our God is never without fuel. The wood offering is not spelled out in the Mosaic text as a scheduled obligation, but Nehemiah institutionalizes it here by lot, as a matter of sustained covenant faithfulness. Nehemiah 13:31 will mark this as one of his lasting reforms."
    },
    "35": {
      "L": "And to bring the firstfruits of our ground and the firstfruits of all fruit of every tree, year by year, to the house of the LORD;",
      "M": "We commit to bring the firstfruits of our soil and the firstfruits of all fruit of every tree, year by year, to the house of the LORD;",
      "T": "We will bring the firstfruits—the first yield of the ground and of every fruit tree—year by year to the house of the LORD. The firstfruit belongs to God before it belongs to us. Exodus 23 and Numbers 18 set this pattern; this covenant renews it."
    },
    "36": {
      "L": "and also the firstborn of our sons and of our cattle, as it is written in the Law, and the firstlings of our herds and of our flocks, to bring to the house of our God, to the priests who minister in the house of our God;",
      "M": "We will also bring to the house of our God, to the priests who minister there, the firstborn of our sons and our cattle, as it is written in the Law—the firstborn of our herds and flocks.",
      "T": "We will bring the firstborn—of our sons, to be redeemed; of our cattle and flocks, to be consecrated—to the house of God, as the Law of Moses requires (Exodus 13; Numbers 18). The priests who serve in the house of God receive what belongs to God first."
    },
    "37": {
      "L": "and to bring the first of our dough, and our contributions, the fruit of every tree, the wine and the oil, to the priests, to the chambers of the house of our God; and the tithes of our ground to the Levites, for they are the Levites who receive the tithes in all our farming towns.",
      "M": "We will bring the first portion of our dough, our contributions, the fruit of every tree, the wine and oil, to the priests at the chambers of the house of our God; and we will bring a tithe of our produce to the Levites, since the Levites collect the tithes in all our farming towns.",
      "T": "The first portion of every batch of dough—the ḥallah contribution that Numbers 15:19-21 prescribes—along with all our offerings of fruit, wine, and oil, we bring to the priests, deposited in the storerooms of the temple. And a tenth of all our agricultural produce goes to the Levites: they are the designated tithe-collectors in every farming community. The system is not optional; it is the funding mechanism of the covenant community's spiritual leadership."
    },
    "38": {
      "L": "And the priest, the son of Aaron, shall be with the Levites when the Levites receive the tithes. And the Levites shall bring up a tenth of the tithes to the house of our God, to the chambers of the storehouse.",
      "M": "A priest of Aaron's line will be present with the Levites when they collect the tithes. The Levites, in turn, will bring a tenth of those tithes up to the house of our God, to the storeroom chambers.",
      "T": "Oversight is built in: an Aaronic priest accompanies the Levites when they collect the tithes—accountability flows in both directions. And the Levites themselves tithe from what they receive: a tenth of the tithes goes up to the temple storerooms. Even the ministers of God's house pay tribute to God's house."
    },
    "39": {
      "L": "For the children of Israel and the children of Levi shall bring the offering of grain, wine, and oil to the chambers where the vessels of the sanctuary are, and the priests who minister, and the gatekeepers, and the singers. And we will not forsake the house of our God.",
      "M": "For the people of Israel and the Levites are to bring their contributions of grain, wine, and oil to the chambers where the sacred vessels are kept and where the ministering priests, gatekeepers, and singers are stationed. We will not neglect the house of our God.",
      "T": "Israel and Levi together—laity and clergy—bring their contributions of grain, wine, and oil to the storerooms of the temple, where the sacred vessels are kept and where the priests, gatekeepers, and singers carry out their ministry. And then the pledge closes with the sentence that anchors the whole chapter: 'We will not forsake the house of our God.' That single line is the covenant core. The community will not let the temple go unfunded and unmanned again."
    }
  },
  "11": {
    "1": {
      "L": "And the rulers of the people settled in Jerusalem. And the rest of the people cast lots to bring one of every ten to dwell in Jerusalem the holy city, while the nine parts remained in the other cities.",
      "M": "The leaders of the people settled in Jerusalem. The rest of the people cast lots to bring one out of every ten to live in Jerusalem the holy city, while the other nine portions remained in the surrounding towns.",
      "T": "Jerusalem was repopulated by covenant obligation and by lottery. The leaders settled there as a matter of course. But the broader population drew lots: one family in ten would leave their village and relocate to Jerusalem—the holy city—while the other nine remained in their towns. The city's walls were rebuilt; its population was still too thin to fill them."
    },
    "2": {
      "L": "And the people blessed all the men who willingly offered themselves to dwell in Jerusalem.",
      "M": "The people praised all who willingly offered to live in Jerusalem.",
      "T": "Some did not wait for the lot. They volunteered. The community blessed every man who chose Jerusalem willingly—above and beyond the lottery obligation. Sacrificing one's village life for the holy city was recognized as an act of covenant devotion."
    },
    "3": {
      "L": "Now these are the chiefs of the province who dwelt in Jerusalem; but in the cities of Judah every man dwelt in his own possession in their cities—Israel, the priests, the Levites, the Nethinim, and the children of Solomon's servants.",
      "M": "These are the heads of the province who settled in Jerusalem. But in the towns of Judah, each person lived in his own inherited property—Israelites, priests, Levites, temple servants, and descendants of Solomon's servants.",
      "T": "The following are the leaders who settled in Jerusalem. The broader population of the province—Israelites, priests, Levites, temple servants, and the descendants of Solomon's royal servants—remained in their own ancestral towns throughout Judah, each family in the inheritance that had returned to them from before the exile."
    },
    "4": {
      "L": "And in Jerusalem dwelt certain of the children of Judah and of the children of Benjamin. Of the children of Judah: Athaiah the son of Uzziah, the son of Zechariah, the son of Amariah, the son of Shephatiah, the son of Mahalalel, of the children of Perez;",
      "M": "In Jerusalem there settled some from the tribe of Judah and some from the tribe of Benjamin. From Judah: Athaiah son of Uzziah, son of Zechariah, son of Amariah, son of Shephatiah, son of Mahalalel, of the Perez line;",
      "T": "In Jerusalem: settlers from Judah and from Benjamin. From Judah's line—Athaiah son of Uzziah (son of Zechariah, son of Amariah, son of Shephatiah, son of Mahalalel), a descendant of Perez the son of Judah;"
    },
    "5": {
      "L": "and Maaseiah the son of Baruch, the son of Col-hozeh, the son of Hazaiah, the son of Adaiah, the son of Joiarib, the son of Zechariah, the son of the Shilonite.",
      "M": "and Maaseiah son of Baruch, son of Col-hozeh, son of Hazaiah, son of Adaiah, son of Joiarib, son of Zechariah, son of the Shilonite.",
      "T": "and Maaseiah son of Baruch (son of Col-hozeh, son of Hazaiah, son of Adaiah, son of Joiarib, son of Zechariah)—of the Shilonite clan, descendants of Shelah, Judah's third son."
    },
    "6": {
      "L": "All the sons of Perez who dwelt in Jerusalem were four hundred and sixty-eight men of valor.",
      "M": "The total Perez descendants who settled in Jerusalem: 468 capable men.",
      "T": "The Perez branch of Judah contributed 468 men of standing to Jerusalem's population."
    },
    "7": {
      "L": "And these are the sons of Benjamin: Sallu the son of Meshullam, the son of Joed, the son of Pedaiah, the son of Kolaiah, the son of Maaseiah, the son of Ithiel, the son of Jeshaiah;",
      "M": "From Benjamin: Sallu son of Meshullam, son of Joed, son of Pedaiah, son of Kolaiah, son of Maaseiah, son of Ithiel, son of Jeshaiah;",
      "T": "From Benjamin: Sallu son of Meshullam (son of Joed, son of Pedaiah, son of Kolaiah, son of Maaseiah, son of Ithiel, son of Jeshaiah)—"
    },
    "8": {
      "L": "and after him Gabbai, Sallai: nine hundred and twenty-eight.",
      "M": "and after him Gabbai and Sallai—928 in all.",
      "T": "and with him Gabbai and Sallai. The Benjaminite settlers in Jerusalem: 928."
    },
    "9": {
      "L": "And Joel the son of Zichri was their overseer; and Judah the son of Senuah was second over the city.",
      "M": "Joel son of Zichri was their overseer, and Judah son of Senuah was second-in-command over the city.",
      "T": "Their administrative leadership: Joel son of Zichri as chief officer over the Benjaminite settlers; Judah son of Senuah as deputy governor of Jerusalem itself."
    },
    "10": {
      "L": "Of the priests: Jedaiah the son of Joiarib, Jachin,",
      "M": "From the priests: Jedaiah son of Joiarib, and Jachin,",
      "T": "Priests settled in Jerusalem: Jedaiah son of Joiarib, and Jachin—"
    },
    "11": {
      "L": "Seraiah the son of Hilkiah, the son of Meshullam, the son of Zadok, the son of Meraioth, the son of Ahitub, ruler of the house of God,",
      "M": "Seraiah son of Hilkiah, son of Meshullam, son of Zadok, son of Meraioth, son of Ahitub, the chief officer of the house of God,",
      "T": "Seraiah son of Hilkiah (son of Meshullam, son of Zadok, son of Meraioth, son of Ahitub)—the ruler of the house of God. His lineage traces straight through Zadok, the high-priestly line of Solomon's temple."
    },
    "12": {
      "L": "and their relatives who did the work of the house, eight hundred and twenty-two; and Adaiah the son of Jeroham, the son of Pelaliah, the son of Amzi, the son of Zechariah, the son of Pashur, the son of Malchijah,",
      "M": "and their relatives who served in the house—822; and Adaiah son of Jeroham, son of Pelaliah, son of Amzi, son of Zechariah, son of Pashur, son of Malchijah,",
      "T": "Their priestly relatives who worked in the house of God: 822. And then Adaiah son of Jeroham (son of Pelaliah, son of Amzi, son of Zechariah, son of Pashur, son of Malchijah)—"
    },
    "13": {
      "L": "and his relatives, chiefs of fathers' houses, two hundred and forty-two; and Amashai the son of Azarel, the son of Ahzai, the son of Meshillemoth, the son of Immer,",
      "M": "and his relatives, heads of ancestral houses—242; and Amashai son of Azarel, son of Ahzai, son of Meshillemoth, son of Immer,",
      "T": "and his kinsmen who headed their ancestral houses: 242. And Amashai son of Azarel (son of Ahzai, son of Meshillemoth, son of Immer)—"
    },
    "14": {
      "L": "and their relatives, mighty men of valor, one hundred and twenty-eight; their overseer was Zabdiel the son of Haggedolim.",
      "M": "and their relatives, men of valor—128; their chief was Zabdiel son of Haggedolim.",
      "T": "and their kinsmen, men of valor: 128. Their commanding officer: Zabdiel son of Haggedolim. His father's name means 'of the great ones'—an aristocratic priestly family."
    },
    "15": {
      "L": "Also of the Levites: Shemaiah the son of Hasshub, the son of Azrikam, the son of Hashabiah, the son of Bunni;",
      "M": "From the Levites: Shemaiah son of Hasshub, son of Azrikam, son of Hashabiah, son of Bunni;",
      "T": "Levites settled in Jerusalem: Shemaiah son of Hasshub (son of Azrikam, son of Hashabiah, son of Bunni)—"
    },
    "16": {
      "L": "and Shabbethai and Jozabad, of the chiefs of the Levites, who had oversight of the outside work of the house of God;",
      "M": "and Shabbethai and Jozabad, leaders among the Levites, who were in charge of the external affairs of the house of God;",
      "T": "and Shabbethai and Jozabad—two senior Levites responsible for the temple's external affairs: procurement, logistics, and all the work that happens outside the sanctuary walls."
    },
    "17": {
      "L": "and Mattaniah the son of Micha, the son of Zabdi, the son of Asaph, who was the leader to begin the thanksgiving in prayer; and Bakbukiah, the second among his brethren; and Abda the son of Shammua, the son of Galal, the son of Jeduthun.",
      "M": "and Mattaniah son of Micha, son of Zabdi, son of Asaph, who directed the thanksgiving in prayer; Bakbukiah, who was second among his fellow Levites; and Abda son of Shammua, son of Galal, son of Jeduthun.",
      "T": "And Mattaniah son of Micha (son of Zabdi, son of Asaph)—the principal worship leader, the one who directed the communal thanksgiving in prayer. From the guild of Asaph, David's great temple musician. Alongside him: Bakbukiah, his second; and Abda son of Shammua (son of Galal, son of Jeduthun)—of the Jeduthun guild. The worship music of Jerusalem was in experienced, inherited hands."
    },
    "18": {
      "L": "All the Levites in the holy city were two hundred and eighty-four.",
      "M": "The total number of Levites in the holy city: 284.",
      "T": "In all: 284 Levites settled in the holy city of Jerusalem."
    },
    "19": {
      "L": "Moreover the gatekeepers, Akkub and Talmon and their relatives, who kept watch at the gates, were one hundred and seventy-two.",
      "M": "The gatekeepers—Akkub, Talmon, and their relatives who kept watch at the gates—numbered 172.",
      "T": "Gatekeepers: Akkub and Talmon and their kinsmen, stationed at the city gates—172 men. The wall was built; now it was permanently staffed."
    },
    "20": {
      "L": "And the rest of Israel, of the priests, and of the Levites were in all the towns of Judah, each one in his inheritance.",
      "M": "The rest of Israel—the priests and Levites not settled in Jerusalem—lived in all the other towns of Judah, each in his ancestral property.",
      "T": "The rest of Israel—priests and Levites not assigned to Jerusalem—were dispersed across the towns of Judah, each family in the land that had been restored to them. The covenant community was spread out but reconstituted."
    },
    "21": {
      "L": "But the Nethinim dwelt in Ophel; and Ziha and Gispa were over the Nethinim.",
      "M": "The temple servants lived on the Ophel, and Ziha and Gispa were in charge of them.",
      "T": "The Nethinim—the temple servants—had their own quarter: the Ophel, the fortified hill just south of the temple mount. Ziha and Gispa were their superintendents."
    },
    "22": {
      "L": "The overseer of the Levites in Jerusalem was Uzzi the son of Bani, the son of Hashabiah, the son of Mattaniah, the son of Micha, of the sons of Asaph, the singers, who were over the service of the house of God.",
      "M": "The overseer of the Levites in Jerusalem was Uzzi son of Bani, son of Hashabiah, son of Mattaniah, son of Micha—from the Asaphite singers who were over the work of the house of God.",
      "T": "Uzzi son of Bani (son of Hashabiah, son of Mattaniah, son of Micha) was the chief administrator of all Levites in Jerusalem—himself from the Asaphite musical guild, carrying the inherited tradition of David's appointed temple musicians."
    },
    "23": {
      "L": "For it was a commandment of the king concerning them, that a fixed provision should be for the singers, as every day required.",
      "M": "For the king had issued a decree about the singers, requiring a fixed daily portion for them.",
      "T": "The singers had royal sanction: a Persian royal decree guaranteed their daily provision. The empire that had scattered Israel now underwrote the temple's worship music—one of the quiet ironies of the restoration era."
    },
    "24": {
      "L": "And Pethahiah the son of Meshezabeel, of the children of Zerah the son of Judah, was at the king's hand in all matters concerning the people.",
      "M": "Pethahiah son of Meshezabeel, from the Zerah line of Judah, was the king's liaison for all matters concerning the people.",
      "T": "Pethahiah son of Meshezabeel—of the Zerah branch of Judah—served as the royal representative: the go-between for the Persian court and the province's population in all civic affairs."
    },
    "25": {
      "L": "And for the villages, with their fields, some of the children of Judah dwelt in Kiriath-arba and its villages, and in Dibon and its villages, and in Jekabzeel and its villages,",
      "M": "As for the villages with their surrounding fields: some of the people of Judah settled in Kiriath-arba and its surrounding villages, in Dibon and its villages, and in Jekabzeel and its villages,",
      "T": "The geographic settlements now follow—a map of the restored community of Judah fanning outward from Jerusalem. From Judah's clans: Kiriath-arba (ancient Hebron's environs, a patriarchal site), Dibon, Jekabzeel—"
    },
    "26": {
      "L": "and in Jeshua, and in Moladah, and in Beth-pelet,",
      "M": "in Jeshua, Moladah, and Beth-pelet,",
      "T": "Jeshua, Moladah, Beth-pelet—"
    },
    "27": {
      "L": "and in Hazar-shual, and in Beersheba and its villages,",
      "M": "in Hazar-shual, in Beersheba and its villages,",
      "T": "Hazar-shual, Beersheba and its surrounding settlements—Beersheba, the ancestral southernmost boundary of the land—"
    },
    "28": {
      "L": "and in Ziklag, and in Meconah and its villages,",
      "M": "in Ziklag and in Meconah and its villages,",
      "T": "Ziklag, Meconah and its villages—"
    },
    "29": {
      "L": "and in En-rimmon, and in Zorah, and in Jarmuth,",
      "M": "in En-rimmon, Zorah, and Jarmuth,",
      "T": "En-rimmon, Zorah, Jarmuth—"
    },
    "30": {
      "L": "Zanoah, Adullam, and their villages, Lachish and its fields, Azekah and its villages. So they encamped from Beersheba as far as the Valley of Hinnom.",
      "M": "Zanoah, Adullam and their surrounding villages, Lachish and its fields, and Azekah and its villages. Their settlement stretched from Beersheba all the way to the Valley of Hinnom.",
      "T": "Zanoah, Adullam and their villages, Lachish and its surrounding fields, Azekah and its villages. The Judahite resettlement stretched from Beersheba in the deep south to the Valley of Hinnom at Jerusalem's southwest corner—a broad arc of the ancient tribal territory reclaimed and reinhabited."
    },
    "31": {
      "L": "The children of Benjamin also settled from Geba, at Michmash, and Aija, and Bethel and its villages,",
      "M": "The Benjaminites settled from Geba—at Michmash, Aija, Bethel and its villages,",
      "T": "The Benjaminite resettlement: beginning at Geba and spreading outward—Michmash, Aija, Bethel and its villages. These were towns heavy with the history of Saul's campaigns and the old northern border wars."
    },
    "32": {
      "L": "Anathoth, Nob, Ananiah,",
      "M": "Anathoth, Nob, Ananiah,",
      "T": "Anathoth—Jeremiah's home town, now resettled—Nob, Ananiah,"
    },
    "33": {
      "L": "Hazor, Ramah, Gittaim,",
      "M": "Hazor, Ramah, Gittaim,",
      "T": "Hazor, Ramah, Gittaim,"
    },
    "34": {
      "L": "Hadid, Zeboim, Neballat,",
      "M": "Hadid, Zeboim, Neballat,",
      "T": "Hadid, Zeboim, Neballat,"
    },
    "35": {
      "L": "Lod and Ono, the Valley of Craftsmen.",
      "M": "Lod and Ono, and the Valley of Craftsmen.",
      "T": "Lod and Ono, and the Valley of Craftsmen—an artisan district, its occupational name preserved in the settlement record."
    },
    "36": {
      "L": "And certain of the divisions of the Levites in Judah were joined to Benjamin.",
      "M": "Some of the Levitical divisions from Judah were assigned to Benjamin.",
      "T": "Finally: certain Levitical contingents that had been settled in Judah were reallocated to Benjamin—an administrative reassignment to match the new settlement pattern. The whole community, priest and laity alike, was being resettled and reordered so that the restored land had the sacred personnel it needed to function as a covenant community."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'nehemiah')
        merge_tier(existing, NEHEMIAH, tier_key)
        save(tier_dir, 'nehemiah', existing)
    print('Nehemiah 10–11 written.')

if __name__ == '__main__':
    main()
