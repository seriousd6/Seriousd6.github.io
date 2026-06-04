"""
MKT Nehemiah chapters 12–13 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-nehemiah-12-13.py

Translation decisions:
- H3068 (יהוה): "LORD" in L and M; "the LORD" in T — consistent with prior Nehemiah scripts.
- H430 (אֱלֹהִים): "God" throughout. "house of God" is the characteristic Nehemiah formulation
  (בֵּית הָאֱלֹהִים), used eight times in chapter 13; preserved in all tiers.
- H2617 (חֶסֶד, hesed) at 13:14, 22: "good deeds" (13:14) is not hesed but H2617 refers to
  "steadfast love/mercy" at 13:22. At 13:14 the noun is H2617 but used in the phrase "my goodness"
  — rendered "steadfast love" in L/M for 13:22; "mercy" also valid. T uses "steadfast love"
  to mark the covenantal weight of the term.
- H8451 (תּוֹרָה, Torah): "the Law" in L and M; "the Torah" or "the Book of Moses" in T
  where context makes the broader resonance useful.
- H7676 (שַׁבָּת, Shabbat): "Sabbath" throughout all tiers. No variation.
- H2598 (חֲנֻכָּה, hanukkah): "dedication" in L and M; T adds "the Hanukkah of the wall"
  at 12:27 — the word literally means dedication/consecration; the festival name derives from it.
- H4521 (מְנָה, portions): "portions" in L/M; T explains the temple support system when
  helpful (12:44–47, 13:10).
- H7218 (ראשׁ, head/chief): "chief" in L; "leading" or "heads of families" in M/T depending
  on context (priestly families vs. Levitical leaders).
- H1984 (הלל, hallel): "praise" in L/M; T notes the antiphonal choir structure at 12:24.
- H8426 (תּוֹדָה, todah): "thanksgiving" throughout. At 12:31, 38, 40 it refers to the two
  processional choirs — "thanksgiving choirs" in M/T; L preserves "companies of them that
  gave thanks" on first mention.
- High priestly succession (12:10-11): Jeshua → Joiakim → Eliashib → Joiada →
  Jonathan/Johanan → Jaddua. "Begat" used in L to preserve the genealogical register feel;
  "fathered" in M; T groups and contextualizes the succession.
- Chapter 13 reform episodes: Each of Nehemiah's four reforms (temple defilement, Levite
  support, Sabbath, mixed marriage) ends with the prayer "Remember me, O my God." T surfaces
  the structural pattern and its theological weight — Nehemiah appeals to God as covenant
  partner and divine auditor of his service.
- 12:43 "the joy of Jerusalem was heard far off": the acoustic detail signifies providential
  vindication against the enemies who had mocked the wall-building (cf. 2:19; 4:1-3). T names
  this echo.
- 12:22 Darius the Persian: most likely Darius II (423–404 BC), though some scholars identify
  Darius III. Jaddua was high priest during Alexander's conquest (332 BC), suggesting these
  records extended well into the Greek period. T notes the temporal breadth without over-specifying.
- 13:8 Nehemiah's physical expulsion of Tobiah's belongings: a deliberate act of boundary-setting
  consistent with his governorship. Not a temper tantrum — a public, authoritative reclamation
  of sacred space. T frames this.
- 13:25 Physical confrontation (striking, pulling hair): this was an exercise of governmental
  authority in an ancient Near Eastern context, not uncontrolled violence. T contextualizes.
- 13:28-29 Priest as son-in-law of Sanballat: probable reference to Manasseh, known from
  Josephus (Antiquities XI.302-312), who founded the Samaritan temple on Gerizim. This may
  be the most consequential marriage in the chapter. T notes the possible historical link.
- Aspect: Hebrew narrative past (waw-consecutive imperfect) throughout. Chapter 13 alternates
  between third-person narration and first-person Nehemiah memoir — T preserves the shift.
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
  "12": {
    "1": {
      "L": "Now these are the priests and the Levites that went up with Zerubbabel the son of Shealtiel, and Jeshua: Seraiah, Jeremiah, Ezra,",
      "M": "These are the priests and Levites who went up with Zerubbabel son of Shealtiel and Jeshua: Seraiah, Jeremiah, Ezra,",
      "T": "The priests and Levites who came up with Zerubbabel son of Shealtiel and Jeshua in the first return from exile: Seraiah, Jeremiah, Ezra,"
    },
    "2": {
      "L": "Amariah, Malluch, Hattush,",
      "M": "Amariah, Malluch, Hattush,",
      "T": "Amariah, Malluch, Hattush,"
    },
    "3": {
      "L": "Shechaniah, Rehum, Meremoth,",
      "M": "Shechaniah, Rehum, Meremoth,",
      "T": "Shechaniah, Rehum, Meremoth,"
    },
    "4": {
      "L": "Iddo, Ginnetho, Abijah,",
      "M": "Iddo, Ginnetho, Abijah,",
      "T": "Iddo, Ginnetho, Abijah,"
    },
    "5": {
      "L": "Miamin, Maadiah, Bilgah,",
      "M": "Miamin, Maadiah, Bilgah,",
      "T": "Miamin, Maadiah, Bilgah,"
    },
    "6": {
      "L": "Shemaiah, Joiarib, Jedaiah.",
      "M": "Shemaiah, Joiarib, Jedaiah.",
      "T": "Shemaiah, Joiarib, Jedaiah."
    },
    "7": {
      "L": "These were the chiefs of the priests and of their brothers in the days of Jeshua.",
      "M": "These were the leading priests and their associates in the days of Jeshua.",
      "T": "Sixteen priestly houses — these were the leading priestly families who returned and served under the first high priest Jeshua after the exile."
    },
    "8": {
      "L": "Moreover the Levites: Jeshua, Binnui, Kadmiel, Sherebiah, Judah, and Mattaniah, who with his brothers was in charge of thanksgiving.",
      "M": "The Levites: Jeshua, Binnui, Kadmiel, Sherebiah, Judah, and Mattaniah, who with his brothers led the songs of thanksgiving.",
      "T": "The Levites who returned: Jeshua, Binnui, Kadmiel, Sherebiah, Judah, and Mattaniah — the last of these led the thanksgiving choirs together with his associates."
    },
    "9": {
      "L": "And Bakbukiah and Unni and their brothers stood opposite them in the service watches.",
      "M": "Bakbukiah and Unni and their associates stood opposite them during the service watches.",
      "T": "Bakbukiah and Unni and their associates stood facing them in antiphonal response — two choirs stationed across from each other for the Levitical worship watches."
    },
    "10": {
      "L": "And Jeshua begat Joiakim, and Joiakim begat Eliashib, and Eliashib begat Joiada,",
      "M": "Jeshua fathered Joiakim, Joiakim fathered Eliashib, and Eliashib fathered Joiada,",
      "T": "The high priestly line of succession: Jeshua begat Joiakim; Joiakim begat Eliashib; Eliashib begat Joiada;"
    },
    "11": {
      "L": "and Joiada begat Jonathan, and Jonathan begat Jaddua.",
      "M": "Joiada fathered Jonathan, and Jonathan fathered Jaddua.",
      "T": "Joiada begat Jonathan; Jonathan begat Jaddua. Six generations of high priests, spanning the first return through the later Persian period."
    },
    "12": {
      "L": "And in the days of Joiakim were priests, the chiefs of the fathers' houses: of Seraiah, Meraiah; of Jeremiah, Hananiah;",
      "M": "In the days of Joiakim, the heads of the priestly families were: from Seraiah's line, Meraiah; from Jeremiah's line, Hananiah;",
      "T": "The priests who headed the family lines in Joiakim's day: Meraiah (from Seraiah), Hananiah (from Jeremiah),"
    },
    "13": {
      "L": "of Ezra, Meshullam; of Amariah, Jehohanan;",
      "M": "from Ezra's line, Meshullam; from Amariah's line, Jehohanan;",
      "T": "Meshullam (from Ezra), Jehohanan (from Amariah),"
    },
    "14": {
      "L": "of Mellicu, Jonathan; of Shebaniah, Joseph;",
      "M": "from Malluch's line, Jonathan; from Shebaniah's line, Joseph;",
      "T": "Jonathan (from Malluch), Joseph (from Shebaniah),"
    },
    "15": {
      "L": "of Harim, Adna; of Meraioth, Helkai;",
      "M": "from Harim's line, Adna; from Meraioth's line, Helkai;",
      "T": "Adna (from Harim), Helkai (from Meraioth),"
    },
    "16": {
      "L": "of Iddo, Zechariah; of Ginnethon, Meshullam;",
      "M": "from Iddo's line, Zechariah; from Ginnethon's line, Meshullam;",
      "T": "Zechariah (from Iddo), Meshullam (from Ginnethon),"
    },
    "17": {
      "L": "of Abijah, Zichri; of Miniamin; of Moadiah, Piltai;",
      "M": "from Abijah's line, Zichri; from Miniamin's and Moadiah's lines, Piltai;",
      "T": "Zichri (from Abijah), Piltai (from Miniamin/Moadiah),"
    },
    "18": {
      "L": "of Bilgah, Shammua; of Shemaiah, Jehonathan;",
      "M": "from Bilgah's line, Shammua; from Shemaiah's line, Jehonathan;",
      "T": "Shammua (from Bilgah), Jehonathan (from Shemaiah),"
    },
    "19": {
      "L": "And of Joiarib, Mattenai; of Jedaiah, Uzzi;",
      "M": "from Joiarib's line, Mattenai; from Jedaiah's line, Uzzi;",
      "T": "Mattenai (from Joiarib), Uzzi (from Jedaiah),"
    },
    "20": {
      "L": "Of Sallai, Kallai; of Amok, Eber;",
      "M": "from Sallai's line, Kallai; from Amok's line, Eber;",
      "T": "Kallai (from Sallai), Eber (from Amok),"
    },
    "21": {
      "L": "of Hilkiah, Hashabiah; of Jedaiah, Nethaneel.",
      "M": "from Hilkiah's line, Hashabiah; from Jedaiah's line, Nethanel.",
      "T": "Hashabiah (from Hilkiah), Nethanel (from Jedaiah)."
    },
    "22": {
      "L": "The Levites in the days of Eliashib, Joiada, and Johanan, and Jaddua, were recorded the chiefs of the fathers' houses; also the priests, to the reign of Darius the Persian.",
      "M": "The Levites were registered as family heads in the days of Eliashib, Joiada, Johanan, and Jaddua, as were the priests, down to the reign of Darius the Persian.",
      "T": "Through the high priesthoods of Eliashib, Joiada, Johanan, and Jaddua — spanning the entire Persian period to the reign of Darius — the Levites were enrolled by family heads in the official registers. The priests were as well. These records extended across multiple generations of Persian rule."
    },
    "23": {
      "L": "The sons of Levi, the chiefs of the fathers' houses, were written in the Book of the Chronicles until the days of Johanan the son of Eliashib.",
      "M": "The Levite family heads were recorded in the Book of the Chronicles down to the days of Johanan son of Eliashib.",
      "T": "The Levitical family heads — sons of Levi — were listed in the official temple annals as far down as the time of Johanan son of Eliashib. These were not census documents alone but the institutional memory of the covenant community."
    },
    "24": {
      "L": "And the chiefs of the Levites: Hashabiah, Sherebiah, and Jeshua the son of Kadmiel, with their brothers over against them, to praise and to give thanks, according to the commandment of David the man of God, watch opposite watch.",
      "M": "The leading Levites were Hashabiah, Sherebiah, and Jeshua son of Kadmiel, with their associates standing opposite them to offer praise and thanksgiving, as David the man of God had commanded, division facing division.",
      "T": "The chief Levites — Hashabiah, Sherebiah, Jeshua son of Kadmiel — led their companies in antiphonal praise and thanksgiving. The arrangement followed the commandment of David the man of God: watch facing watch, choir answering choir across the sanctuary."
    },
    "25": {
      "L": "Mattaniah, Bakbukiah, Obadiah, Meshullam, Talmon, and Akkub were gatekeepers keeping the watch at the storehouses of the gates.",
      "M": "Mattaniah, Bakbukiah, Obadiah, Meshullam, Talmon, and Akkub served as gatekeepers keeping guard at the storerooms beside the gates.",
      "T": "Mattaniah, Bakbukiah, Obadiah, Meshullam, Talmon, and Akkub held the gatekeeper posts, stationed at the store-chambers of the city gates."
    },
    "26": {
      "L": "These were in the days of Joiakim the son of Jeshua, son of Jozadak, and in the days of Nehemiah the governor, and of Ezra the priest, the scribe.",
      "M": "These men served in the days of Joiakim son of Jeshua son of Jozadak, and in the days of Nehemiah the governor and Ezra the priest and scribe.",
      "T": "All of these served during the high priesthood of Joiakim son of Jeshua son of Jozadak — and more broadly, in the era of Nehemiah the governor and Ezra the priest and scribe. The three great figures of the restoration overlap here: priest, scribe, and governor, all serving together."
    },
    "27": {
      "L": "And at the dedication of the wall of Jerusalem, they sought the Levites from all their places, to bring them to Jerusalem, to hold the dedication with gladness, both with thanksgiving and with singing, with cymbals, harps, and lyres.",
      "M": "For the dedication of the wall of Jerusalem, they sent to bring the Levites from all their towns to celebrate the dedication with joy and thanksgiving — with singing, cymbals, harps, and lyres.",
      "T": "The wall was finished. Now came the dedication — the Hanukkah of the wall. Levites were summoned from every town throughout Judah to come to Jerusalem for a celebration of gladness: thanksgivings, singing, cymbals, harps, and lyres. The wall that enemies had mocked was going to be consecrated to God."
    },
    "28": {
      "L": "And the sons of the singers gathered together, both from the plain country around Jerusalem, and from the villages of the Netophathites,",
      "M": "The singers' guilds gathered from the area around Jerusalem and from the villages of the Netophathites,",
      "T": "The singers came from the surrounding countryside — from the Netophathite villages south of Jerusalem —"
    },
    "29": {
      "L": "and from the house of Gilgal, and from the fields of Geba and Azmaveth; for the singers had built themselves villages round about Jerusalem.",
      "M": "from Beth-gilgal and from the fields of Geba and Azmaveth, for the singers had established their own villages around Jerusalem.",
      "T": "and from Beth-gilgal and the fields of Geba and Azmaveth. The singers had established their own settlements in a ring around Jerusalem — always within reach when the temple needed them."
    },
    "30": {
      "L": "And the priests and the Levites purified themselves, and they purified the people and the gates and the wall.",
      "M": "The priests and Levites purified themselves, then purified the people, the gates, and the wall.",
      "T": "Before the celebration could begin, there was ritual preparation: the priests and Levites first purified themselves, then extended that purification to the people, the gates, and the wall itself. The wall was a sacred project; it would be consecrated as such."
    },
    "31": {
      "L": "Then I brought up the princes of Judah upon the wall, and appointed two great companies of them that gave thanks, that went in procession. One went on the right hand upon the wall toward the Dung Gate.",
      "M": "I brought the leaders of Judah up onto the top of the wall and organized two large thanksgiving choirs for the procession. The first company moved to the right along the wall toward the Dung Gate.",
      "T": "Nehemiah organized the ceremony. He led the princes of Judah up onto the top of the wall and formed two great processional choirs — one moving to the right, southward along the wall toward the Dung Gate."
    },
    "32": {
      "L": "And after them went Hoshaiah and half of the princes of Judah,",
      "M": "Hoshaiah followed with half of the leaders of Judah,",
      "T": "Behind the first choir walked Hoshaiah and half the leaders of Judah,"
    },
    "33": {
      "L": "and Azariah, Ezra, and Meshullam,",
      "M": "along with Azariah, Ezra, and Meshullam,",
      "T": "Azariah, Ezra, Meshullam,"
    },
    "34": {
      "L": "Judah and Benjamin and Shemaiah and Jeremiah,",
      "M": "Judah, Benjamin, Shemaiah, and Jeremiah,",
      "T": "Judah, Benjamin, Shemaiah, Jeremiah,"
    },
    "35": {
      "L": "and certain of the sons of the priests with trumpets: Zechariah son of Jonathan, son of Shemaiah, son of Mattaniah, son of Michaiah, son of Zaccur, son of Asaph,",
      "M": "and some of the priests with trumpets — Zechariah son of Jonathan, son of Shemaiah, son of Mattaniah, son of Michaiah, son of Zaccur, son of Asaph —",
      "T": "and priests carrying trumpets — chief among them Zechariah son of Jonathan, son of Shemaiah, son of Mattaniah, son of Michaiah, son of Zaccur, son of Asaph —"
    },
    "36": {
      "L": "and his brothers Shemaiah, Azarael, Milalai, Gilalai, Maai, Nethaneel, Judah, and Hanani, with the instruments of music of David the man of God; and Ezra the scribe was before them.",
      "M": "accompanied by his brothers Shemaiah, Azarel, Milalai, Gilalai, Maai, Nethanel, Judah, and Hanani, playing the musical instruments of David the man of God; and Ezra the scribe led the way.",
      "T": "— and his associates: Shemaiah, Azarel, Milalai, Gilalai, Maai, Nethanel, Judah, Hanani, playing the instruments David the man of God had ordained. Ezra the scribe walked before them all."
    },
    "37": {
      "L": "And at the Fountain Gate they went straight ahead, by the stairs of the City of David, at the ascent of the wall, above the house of David, even to the Water Gate on the east.",
      "M": "At the Fountain Gate they went straight ahead, up the stairs of the City of David along the wall's ascent, past the house of David, and on to the Water Gate on the east.",
      "T": "At the Fountain Gate they climbed the stairs of the City of David — Zion's ancient slope — moving along the wall's ascent, past the house of David, and on to the Water Gate on the eastern side of the city."
    },
    "38": {
      "L": "And the other company of them that gave thanks went the opposite way, and I after them, with the half of the people, upon the wall, from beyond the Tower of the Furnaces even to the Broad Wall,",
      "M": "The second thanksgiving choir went in the opposite direction, with me and half the people following behind, walking along the wall from beyond the Tower of the Furnaces to the Broad Wall,",
      "T": "Meanwhile, the second great choir moved in the opposite direction — westward along the wall. I followed with the other half of the people, going from the Tower of the Furnaces around to the Broad Wall —"
    },
    "39": {
      "L": "and above the gate of Ephraim, and by the old gate, and by the fish gate, and the tower of Hananel, and the tower of Meah, even unto the sheep gate: and they stood still in the gate of the guard.",
      "M": "past the Gate of Ephraim, the Old Gate, the Fish Gate, the Tower of Hananel, the Tower of the Hundred, and on to the Sheep Gate, where they halted at the Gate of the Guard.",
      "T": "— past the Gate of Ephraim, the Old Gate, the Fish Gate, the Tower of Hananel, the Tower of the Hundred — all the way to the Sheep Gate, where they halted at the Gate of the Guard. The entire circuit of Jerusalem's wall had been walked in procession."
    },
    "40": {
      "L": "So stood the two companies of them that gave thanks in the house of God, and I and the half of the rulers with me.",
      "M": "Both thanksgiving choirs took their places in the house of God, with me and half of the leaders beside us.",
      "T": "Both great choirs converged at the house of God — the two processions that had gone around opposite sides of the wall now standing together at the temple. Nehemiah stood there with half the leaders."
    },
    "41": {
      "L": "and the priests Eliakim, Maaseiah, Miniamin, Michaiah, Elioenai, Zechariah, and Hananiah, with trumpets,",
      "M": "The priests Eliakim, Maaseiah, Miniamin, Michaiah, Elioenai, Zechariah, and Hananiah sounded their trumpets,",
      "T": "Priests with trumpets: Eliakim, Maaseiah, Miniamin, Michaiah, Elioenai, Zechariah, Hananiah."
    },
    "42": {
      "L": "and Maaseiah and Shemaiah and Eleazar and Uzzi and Jehohanan and Malchijah and Elam and Ezer. And the singers sang aloud, with Jezrahiah their overseer.",
      "M": "And Maaseiah, Shemaiah, Eleazar, Uzzi, Jehohanan, Malchijah, Elam, and Ezer. The singers sang loudly under Jezrahiah their director.",
      "T": "And Maaseiah, Shemaiah, Eleazar, Uzzi, Jehohanan, Malchijah, Elam, and Ezer took their places with them. The singers raised their voices — loud, full-throated singing under the direction of Jezrahiah. The sound carried across the city."
    },
    "43": {
      "L": "Also that day they offered great sacrifices and rejoiced; for God had made them rejoice with great joy, so that the wives also and the children rejoiced: and the joy of Jerusalem was heard even far off.",
      "M": "That day they offered great sacrifices and rejoiced, for God had given them great joy. The women and children also rejoiced, and the sound of Jerusalem's joy was heard far away.",
      "T": "The sacrifices were great, and the rejoicing was greater. God himself had filled them with joy — not just the leaders, not just the men, but the wives and children too. The shout of Jerusalem that day was so loud it was heard from a distance. The wall that enemies had mocked (cf. 2:19; 4:1-3) was resounding with the praise of God."
    },
    "44": {
      "L": "And at that time were some appointed over the chambers for the stores, for the contributions, for the firstfruits, and for the tithes, to gather into them out of the fields of the cities the portions required by the Law for the priests and for the Levites; for Judah rejoiced over the priests and the Levites that served.",
      "M": "That same day men were appointed to oversee the storerooms for contributions, firstfruits, and tithes — to collect from the surrounding towns the portions the Law required for the priests and Levites. For Judah rejoiced in the priests and Levites who were serving.",
      "T": "With the celebration still underway, the community turned to practical permanence: they appointed stewards over the storerooms for contributions, firstfruits, and tithes — all that the Law required to support the priests and Levites from the produce of the surrounding towns. For Judah rejoiced in its priests and Levites who were faithfully fulfilling their ministry."
    },
    "45": {
      "L": "And both the singers and the porters kept the ward of their God, and the ward of the purification, according to the commandment of David and of Solomon his son.",
      "M": "The singers and the gatekeepers kept their appointed duties, including the requirements of purification, as David and his son Solomon had commanded.",
      "T": "The singers and the gatekeepers fulfilled their appointed functions — including the requirements of ritual purification — all in accordance with the commands that David and his son Solomon had laid down centuries before. The old order was being faithfully restored."
    },
    "46": {
      "L": "For in the days of David and Asaph of old there were chiefs of the singers, and songs of praise and giving thanks to God.",
      "M": "For in the days of David and Asaph, long ago, there had been directors of the singers and songs of praise and thanksgiving to God.",
      "T": "This had ancient precedent: in the days of David and Asaph there had been choir directors and the same songs of praise and thanksgiving to God. What Nehemiah was restoring had been practiced for five centuries."
    },
    "47": {
      "L": "And all Israel in the days of Zerubbabel and in the days of Nehemiah gave the daily portions for the singers and the porters. And they sanctified the holy things to the Levites; and the Levites sanctified them to the children of Aaron.",
      "M": "In the days of Zerubbabel and in the days of Nehemiah, all Israel provided daily portions for the singers and gatekeepers. They set apart what was holy for the Levites, and the Levites set apart what was holy for the descendants of Aaron.",
      "T": "From Zerubbabel's day to Nehemiah's day, all Israel had maintained daily support for the singers and gatekeepers — each day its portion. The sacred portions flowed in the proper order: Israel gave to the Levites; the Levites consecrated the portions for the Aaronic priests. The covenant service was properly and permanently sustained."
    }
  },
  "13": {
    "1": {
      "L": "On that day they read in the book of Moses in the hearing of the people, and therein was found written that the Ammonite and the Moabite should not come into the congregation of God for ever,",
      "M": "On that day they read from the Book of Moses in the hearing of the people, and it was found written there that no Ammonite or Moabite should ever enter the assembly of God,",
      "T": "On the same day they read aloud from the Book of Moses before the whole assembly — and they came upon the passage prohibiting Ammonites and Moabites from ever entering the congregation of God."
    },
    "2": {
      "L": "because they met not the children of Israel with bread and with water, but hired Balaam against them to curse them: howbeit our God turned the curse into a blessing.",
      "M": "They had not welcomed Israel with food and water, but had hired Balaam to curse them — yet our God turned the curse into a blessing.",
      "T": "The reason the Law gave: these nations had refused Israel hospitality in the wilderness and paid Balaam to curse them. But the LORD had overturned the curse and turned it into a blessing. The Law remembered what the nations would not acknowledge. (See Deuteronomy 23:3-5; Numbers 22–24.)"
    },
    "3": {
      "L": "Now it came to pass when they had heard the law, that they separated from Israel all the mixed multitude.",
      "M": "When the people heard the law, they separated from Israel all those of foreign descent.",
      "T": "When the people heard this portion of the Law, they acted on it immediately: they separated from Israel all those of mixed foreign descent. The reading of the covenant text produced covenant reformation on the spot."
    },
    "4": {
      "L": "And before this, Eliashib the priest, having the oversight of the chamber of the house of our God, was allied to Tobiah,",
      "M": "Now before this, Eliashib the priest, who had charge of the storerooms of the house of our God, had formed an alliance with Tobiah",
      "T": "But something had gone deeply wrong during Nehemiah's absence. Eliashib the priest — the one entrusted with the storerooms of the house of God — had formed a personal alliance with Tobiah,"
    },
    "5": {
      "L": "and had prepared for him a great chamber, where before had they laid the meal offerings, the frankincense, and the vessels, and the tithes of the corn, the new wine, and the oil, which was commanded to be given to the Levites, and the singers, and the porters; and the offerings of the priests.",
      "M": "and had set aside a large room for him that had previously held the grain offerings, the incense, the temple vessels, and the tithes of grain, new wine, and oil designated for the Levites, singers, and gatekeepers, and the contributions for the priests.",
      "T": "— and had cleared out a large storeroom in the temple complex and given it to Tobiah as private accommodation. Before that, the room had held the grain offerings, incense, sacred vessels, and the tithes — the grain, wine, and oil designated for the Levites, singers, and gatekeepers, and the contributions for the priests. Sacred space had been converted to private use for an enemy of Israel."
    },
    "6": {
      "L": "But in all this time was not I at Jerusalem: for in the two and thirtieth year of Artaxerxes king of Babylon came I unto the king, and after certain days I obtained leave from the king:",
      "M": "While all this was happening, I was not in Jerusalem. In the thirty-second year of Artaxerxes king of Babylon I had returned to the king, and after some time I obtained leave from the king",
      "T": "All of this had happened while Nehemiah was away. In the thirty-second year of Artaxerxes, he had returned to Babylon as his obligations to the king required. After an interval he asked the king's permission to return —"
    },
    "7": {
      "L": "and I came to Jerusalem, and understood of the evil that Eliashib had done for Tobiah, in preparing him a chamber in the courts of the house of God.",
      "M": "and came back to Jerusalem. There I discovered the evil Eliashib had done on behalf of Tobiah, preparing a room for him in the courts of the house of God.",
      "T": "— and returned to Jerusalem. What he found was a scandal: Eliashib had prepared private quarters for Tobiah inside the courts of God's house. An Ammonite opponent of Israel's restoration had been installed in the temple complex."
    },
    "8": {
      "L": "And it grieved me sore: therefore I cast forth all the household stuff of Tobiah out of the chamber.",
      "M": "I was deeply displeased and threw all of Tobiah's household belongings out of the room.",
      "T": "Nehemiah was furious. He did not deliberate. He threw everything belonging to Tobiah — every piece of furniture, every possession — out of the room. The eviction was immediate and total."
    },
    "9": {
      "L": "Then I commanded, and they cleansed the chambers; and thither brought I again the vessels of the house of God, with the meal offering and the frankincense.",
      "M": "Then I ordered the rooms to be cleansed, and I brought back the vessels of the house of God along with the grain offerings and incense.",
      "T": "Then he ordered the rooms ritually cleansed — purified after their defilement by an unauthorized resident — and restored to their proper contents: the sacred vessels, the grain offerings, the incense. Order was re-established by decisive action."
    },
    "10": {
      "L": "And I perceived that the portions of the Levites had not been given them; for the Levites and the singers that did the work were fled every one to his field.",
      "M": "I also discovered that the portions due the Levites had not been given to them, and that the Levites and singers who served had each fled back to their own fields.",
      "T": "The problem was deeper than one room. The tithes and portions that should have supported the Levites had not been paid. So the Levites and singers — the men whose vocation was to maintain the house of God — had abandoned their posts and gone back to farming, because there was nothing else to sustain them."
    },
    "11": {
      "L": "Then contended I with the rulers, and said, Why is the house of God forsaken? And I gathered them together, and set them in their place.",
      "M": "I brought charges against the officials and said, 'Why is the house of God forsaken?' Then I gathered the Levites and singers together and restored them to their posts.",
      "T": "'Why is God's house forsaken?' Nehemiah confronted the officials with the failure directly. Then he gathered the scattered Levites and singers and restored them to their places of service. The personnel crisis required addressing, and so did the financial one behind it."
    },
    "12": {
      "L": "Then brought all Judah the tithe of the corn and the new wine and the oil unto the treasuries.",
      "M": "Then all Judah brought the tithes of grain, new wine, and oil into the storehouses.",
      "T": "When Nehemiah addressed the failure publicly, Judah responded: the people brought their tithes of grain, wine, and oil into the storehouses as the Law required."
    },
    "13": {
      "L": "And I made treasurers over the treasuries, Shelemiah the priest, and Zadok the scribe, and of the Levites, Pedaiah: and next to them was Hanan the son of Zaccur, the son of Mattaniah: for they were counted faithful, and their office was to distribute unto their brethren.",
      "M": "I appointed Shelemiah the priest, Zadok the scribe, and Pedaiah of the Levites as treasurers over the storehouses, with Hanan son of Zaccur son of Mattaniah assisting them. These men were regarded as faithful, and their task was to distribute the portions to their fellow priests and Levites.",
      "T": "The structural fix: four men chosen specifically for their reputation for faithfulness — Shelemiah the priest, Zadok the scribe, Pedaiah the Levite, and Hanan son of Zaccur son of Mattaniah as assistant. Their function was to receive the tithes and distribute the proper portions to the priests and Levites. The system had failed through neglect; now it was rebuilt with accountable stewards."
    },
    "14": {
      "L": "Remember me, O my God, concerning this, and wipe not out my good deeds that I have done for the house of my God, and for the offices thereof.",
      "M": "Remember me, O my God, for this, and do not blot out the good deeds I have done for the house of my God and its services.",
      "T": "Then Nehemiah turned to God and prayed: 'Remember me, O my God, for these things. Do not let what I have done for your house and its ministry be erased.' These brief, mid-narrative prayers are characteristic of the Nehemiah memoir — covenant appeals to God as the divine auditor who does not forget what has been done in faithful service."
    },
    "15": {
      "L": "In those days saw I in Judah some treading wine presses on the sabbath, and bringing in sheaves, and lading asses; as also wine, grapes, and figs, and all manner of burdens, which they brought into Jerusalem on the sabbath day: and I testified against them in the day wherein they sold victuals.",
      "M": "In those days I saw people in Judah treading winepresses on the Sabbath and hauling in loads of grain on donkeys, along with wine, grapes, figs, and all kinds of goods that they were bringing into Jerusalem on the Sabbath. I warned them on the very day they were selling food.",
      "T": "The second reform: Sabbath violation. Nehemiah observed Judeans treading winepresses on the Sabbath, loading donkeys with grain, hauling in wine, grapes, figs, and every kind of burden into Jerusalem for sale. He confronted them immediately, on the spot, on the day they were doing it."
    },
    "16": {
      "L": "There dwelt men of Tyre also therein, which brought fish, and all manner of ware, and sold on the sabbath unto the children of Judah, and in Jerusalem.",
      "M": "Tyrians living in the city also brought in fish and all kinds of merchandise and sold it on the Sabbath to the people of Judah in Jerusalem.",
      "T": "And it was not only Jews. Tyrian merchants who had settled in Jerusalem were bringing fish and all manner of goods and selling them openly in the city on the Sabbath — to Judeans who were willing to buy."
    },
    "17": {
      "L": "Then I contended with the nobles of Judah, and said unto them, What evil thing is this that ye do, and profane the sabbath day?",
      "M": "I confronted the nobles of Judah and said to them, 'What is this evil thing you are doing — profaning the Sabbath day?'",
      "T": "'What is this evil thing you are doing?' Nehemiah brought the charge to the nobles of Judah — the people with the authority to permit or prevent it. 'You are profaning the Sabbath.'"
    },
    "18": {
      "L": "Did not your fathers thus, and did not our God bring all this evil upon us, and upon this city? yet ye bring more wrath upon Israel by profaning the sabbath.",
      "M": "'Did your ancestors not do the same, and did our God not bring all this disaster on us and on this city? Yet you are bringing more wrath on Israel by profaning the Sabbath.'",
      "T": "'Your own ancestors did exactly this — and that covenant violation is precisely what brought the catastrophe of exile on Jerusalem. Do you not see what you are doing? You are inviting the same judgment. Every Sabbath you profane is more wrath heaped on Israel.' The exile was recent memory. Its cause was being repeated."
    },
    "19": {
      "L": "And it came to pass that when the gates of Jerusalem began to be dark before the sabbath, I commanded that the gates should be shut, and charged that they should not be opened till after the sabbath: and some of my servants set I at the gates, that there should no burden be brought in on the sabbath day.",
      "M": "As dusk fell on Jerusalem before the Sabbath, I ordered the gates shut and commanded that they not be opened again until after the Sabbath. I also stationed some of my own servants at the gates to ensure that no load was brought in on the Sabbath day.",
      "T": "He took structural action: as the pre-Sabbath twilight came on Jerusalem, he ordered the gates closed — and kept closed until the Sabbath ended. His own servants stood guard at the gates. No load would enter the city on the Sabbath."
    },
    "20": {
      "L": "So the merchants and sellers of all kind of ware lodged without Jerusalem once or twice.",
      "M": "The merchants and various traders camped outside Jerusalem one or two times.",
      "T": "For a time the merchants camped outside the walls, waiting for the gate to open. They stayed a night or two."
    },
    "21": {
      "L": "Then I testified against them, and said unto them, Why lodge ye about the wall? if ye do so again, I will lay hands on you. From that time forth came they no more on the sabbath.",
      "M": "But I warned them: 'Why are you spending the night outside the wall? If you do this again, I will use force against you.' After that they stopped coming on the Sabbath.",
      "T": "Nehemiah went out and warned them directly: 'Why are you camped outside the wall? If you come again on the Sabbath, I will arrest you.' After that clear warning, they stopped coming. The boundary held."
    },
    "22": {
      "L": "And I commanded the Levites that they should cleanse themselves, and that they should come and keep the gates, to sanctify the sabbath day. Remember me, O my God, concerning this also, and spare me according to the greatness of thy mercy.",
      "M": "I also commanded the Levites to purify themselves and come guard the gates, to keep the Sabbath day holy. Remember me, O my God, for this as well, and spare me according to the greatness of your steadfast love.",
      "T": "He assigned the Levites — ritually purified and publicly authorized — to stand guard at the gates and sanctify the Sabbath by their presence. And again Nehemiah prayed: 'Remember me, O my God, for this too. Spare me — according to the greatness of your steadfast love.' He knew the Sabbath reform had eternal weight, not only political."
    },
    "23": {
      "L": "In those days also saw I the Jews that had married wives of Ashdod, of Ammon, and of Moab:",
      "M": "In those days I also saw Jews who had married women from Ashdod, Ammon, and Moab.",
      "T": "The third reform: mixed marriages. Nehemiah discovered that Jews had married women from Ashdod, Ammon, and Moab — the very nations whose exclusion from the assembly had just been read aloud from the Law."
    },
    "24": {
      "L": "and their children spake half in the speech of Ashdod, and could not speak in the Jews' language, but according to the language of each people.",
      "M": "Half of their children spoke the language of Ashdod and could not speak the language of Judah, but only the language of the foreign parent.",
      "T": "The practical consequence had already arrived in the next generation: half the children of these mixed households could speak Ashdodite but not Hebrew. The language of Torah was going silent in the homes of Israel. Identity was dissolving within a single generation."
    },
    "25": {
      "L": "And I contended with them, and cursed them, and smote certain of them, and plucked off their hair, and made them swear by God, saying, Ye shall not give your daughters unto their sons, nor take their daughters unto your sons, or for yourselves.",
      "M": "I confronted them, called down curses on them, struck some of them, and pulled out their hair. I made them swear before God: 'You must not give your daughters to their sons or take their daughters for your sons or for yourselves.'",
      "T": "Nehemiah's response was physical and public. He rebuked them harshly — pronouncing curses, striking some, pulling hair. Then he extracted a sworn oath before God: no more intermarriage with these foreign nations. The physical actions were those of a governor executing covenant discipline, not uncontrolled rage; in ancient Near Eastern culture, such acts were recognized exercises of gubernatorial authority."
    },
    "26": {
      "L": "Did not Solomon king of Israel sin by these things? yet among many nations was there no king like him, who was beloved of his God, and God made him king over all Israel: nevertheless even him did outlandish women cause to sin.",
      "M": "'Was it not because of women like these that Solomon king of Israel sinned? Among the many nations there was no king like him, and he was loved by his God, who made him king over all Israel — yet even he was led into sin by foreign women.'",
      "T": "'Solomon! The greatest king Israel ever had — loved by God, admired by all nations — and even he was brought down by exactly this. Foreign wives drew him into idolatry and fractured his legacy. Are you telling me you can resist what Solomon could not?'"
    },
    "27": {
      "L": "Shall we then hearken unto you to do all this great evil, to transgress against our God in marrying strange wives?",
      "M": "'Are we then to listen to you and do all this great evil and be unfaithful to our God by marrying foreign women?'",
      "T": "'Must we be told again?' Nehemiah pressed. 'This is great evil — treachery against your God. It is not a cultural preference; it is covenant betrayal.'"
    },
    "28": {
      "L": "And one of the sons of Joiada, the son of Eliashib the high priest, was son in law to Sanballat the Horonite: therefore I chased him from me.",
      "M": "One of the sons of Joiada son of Eliashib the high priest had married the daughter of Sanballat the Horonite, so I drove him away from me.",
      "T": "The problem reached the highest level: a son of Joiada — grandson of the high priest Eliashib — had married the daughter of Sanballat the Horonite. Sanballat: the man who had consistently opposed God's work in Jerusalem from the beginning. Nehemiah expelled him. A priest who had allied himself with Israel's enemy through marriage could not remain in the community's service. (Later tradition identifies this priest as Manasseh, who is said to have founded the rival Samaritan temple on Mount Gerizim.)"
    },
    "29": {
      "L": "Remember them, O my God, because they have defiled the priesthood, and the covenant of the priesthood, and of the Levites.",
      "M": "'Remember them, O my God, for they have defiled the priesthood and the covenant of the priests and Levites.'",
      "T": "'Remember them, O God.' Not a blessing but a covenant lawsuit. Nehemiah submitted the defilement of the priesthood to the divine Judge: the sacred covenant of the priesthood had been broken from within; let God take account of it."
    },
    "30": {
      "L": "Thus cleansed I them from all strangers, and appointed the wards of the priests and the Levites, every one in his work,",
      "M": "Thus I purged everything foreign from the community and assigned the priests and Levites their duties, each in his appointed work,",
      "T": "Nehemiah summarizes his reforming work: he purged the foreign elements from the community and restored the organized structure of priestly and Levitical service — each person assigned to their proper post."
    },
    "31": {
      "L": "And for the wood offering, at times appointed, and for the firstfruits. Remember me, O my God, for good.",
      "M": "and arranged for the wood offering at appointed times and for the firstfruits. Remember me, O my God, for good.",
      "T": "He also arranged the wood offering — the fuel for the altar fire, brought in rotation at appointed times — and provision for the firstfruits. Then the book ends with the prayer it has returned to throughout: 'Remember me, O my God, for good.' It is the prayer of a man who has served faithfully in a hard post and who entrusts his account to God alone."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'nehemiah')
        merge_tier(existing, NEHEMIAH, tier_key)
        save(tier_dir, 'nehemiah', existing)
    print('Nehemiah 12–13 written.')

if __name__ == '__main__':
    main()
