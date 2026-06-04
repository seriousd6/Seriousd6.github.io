"""
MKT Ezra chapters 7–8 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-ezra-7-8.py

Translation decisions:
- H3068 (יהוה): "LORD" in L and M; "the LORD" in T. Consistent with EZR-1b.
- H430 (אֱלֹהִים) / H426 (Aramaic אֱלָהּ): "God" throughout; epithets "God of Israel,"
  "God of heaven" preserved as given. Chapter 7:12–26 is in Aramaic in the MT; translated
  naturally without marking the switch in the English text.
- H2617 (חֶסֶד): "steadfast love" in L/M; "steadfast love" in T also (7:28 — the context
  is Ezra's personal testimony, where covenant-loyalty is the right emphasis).
- H8451 (תּוֹרָה): "law" throughout in L/M; "Torah" in T (7:6, 10, 11) — where the term
  carries its full scriptural sense, not just legal code.
- H3027 (יָד, hand): "the hand of the LORD" / "the good hand of God" (7:6, 7:9, 7:28;
  8:18, 8:22, 8:31) — Ezra's signature motif for divine providence. L/M keep "hand";
  T expands the phrase's weight without paraphrasing.
- 7:12–26 Aramaic royal charter: diplomatic register honored. The letter grants sweeping
  authority: investigation, funding, appointment of judges, exemption of temple staff.
- 7:22 salt without prescribing how much: the Hebrew/Aramaic idiom means "unlimited salt."
  Rendered "without limit" in L/M, "without restriction" in T.
- 7:28 "I was strengthened": Ezra's personal response to divine favor. The waw-consecutive
  imperfect is narrative past — simple "I was strengthened" not present tense.
- 8:21–23 fast at Ahava: theologically significant — Ezra had boasted of God's protection
  to the king and therefore was ashamed to ask for a military escort. T surfaces this irony.
- 8:35 twelve bulls / twelve goats: the number 12 deliberately invokes all twelve tribes,
  even while most of the northern tribes remain scattered. T notes this.
- OT echoes: Ezra's genealogy back to Aaron (7:1–5) establishes priestly authority;
  "study, practice, teach" sequence (7:10) is the rabbinic model's OT root.
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

EZRA = {
  "7": {
    "1": {
      "L": "Now after these things, in the reign of Artaxerxes king of Persia, Ezra son of Seraiah, son of Azariah, son of Hilkiah,",
      "M": "After these events, during the reign of Artaxerxes king of Persia, Ezra son of Seraiah, son of Azariah, son of Hilkiah,",
      "T": "Decades after the temple's dedication, in the reign of Artaxerxes king of Persia, there came onto the scene Ezra son of Seraiah, son of Azariah, son of Hilkiah,"
    },
    "2": {
      "L": "son of Shallum, son of Zadok, son of Ahitub,",
      "M": "son of Shallum, son of Zadok, son of Ahitub,",
      "T": "son of Shallum, son of Zadok, son of Ahitub—"
    },
    "3": {
      "L": "son of Amariah, son of Azariah, son of Meraioth,",
      "M": "son of Amariah, son of Azariah, son of Meraioth,",
      "T": "son of Amariah, son of Azariah, son of Meraioth,"
    },
    "4": {
      "L": "son of Zerahiah, son of Uzzi, son of Bukki,",
      "M": "son of Zerahiah, son of Uzzi, son of Bukki,",
      "T": "son of Zerahiah, son of Uzzi, son of Bukki,"
    },
    "5": {
      "L": "son of Abishua, son of Phinehas, son of Eleazar, son of Aaron the chief priest—",
      "M": "son of Abishua, son of Phinehas, son of Eleazar, son of Aaron the high priest.",
      "T": "son of Abishua, son of Phinehas, son of Eleazar, son of Aaron the high priest. His line ran directly to the founding priesthood."
    },
    "6": {
      "L": "This Ezra went up from Babylon; and he was a skilled scribe in the law of Moses, which the LORD God of Israel had given; and the king granted him all his request, according to the hand of the LORD his God upon him.",
      "M": "This Ezra came up from Babylon. He was a skilled scribe in the law of Moses, which the LORD God of Israel had given, and the king granted him everything he asked, for the hand of the LORD his God was upon him.",
      "T": "This Ezra made his way up from Babylon. He was a practiced scholar in the Torah of Moses, the law the LORD God of Israel had given—and the king granted his every request, because the LORD his God's hand was upon him."
    },
    "7": {
      "L": "And there went up with him some of the children of Israel, and the priests, and the Levites, and the singers, and the gatekeepers, and the Nethinim, to Jerusalem, in the seventh year of King Artaxerxes.",
      "M": "Some Israelites—priests, Levites, singers, gatekeepers, and Nethinim—also went up to Jerusalem in the seventh year of King Artaxerxes.",
      "T": "With him came Israelites of every order: priests, Levites, singers, gatekeepers, and temple servants—all making the journey to Jerusalem in Artaxerxes' seventh year."
    },
    "8": {
      "L": "And he came to Jerusalem in the fifth month, in the seventh year of the king.",
      "M": "He arrived in Jerusalem in the fifth month of the king's seventh year.",
      "T": "He reached Jerusalem in the fifth month of that seventh year."
    },
    "9": {
      "L": "For on the first day of the first month he began the journey from Babylon, and on the first day of the fifth month he arrived at Jerusalem, according to the good hand of his God upon him.",
      "M": "He had set out from Babylon on the first day of the first month and arrived at Jerusalem on the first day of the fifth month—according to the good hand of his God upon him.",
      "T": "He had departed Babylon on the first day of the first month and walked into Jerusalem on the first day of the fifth month—exactly four months. The good hand of his God was upon him through every step."
    },
    "10": {
      "L": "For Ezra had prepared his heart to seek the law of the LORD, and to do it, and to teach statutes and judgments in Israel.",
      "M": "Ezra had devoted himself to studying the law of the LORD, practicing it, and teaching its statutes and ordinances in Israel.",
      "T": "This was Ezra's life-program: to investigate the LORD's Torah, to live it himself, and then to teach its statutes and judgments to Israel. Study, practice, teach—in that order."
    },
    "11": {
      "L": "Now this is the copy of the letter that King Artaxerxes gave to Ezra the priest, the scribe—a scribe of the words of the commandments of the LORD and his statutes to Israel:",
      "M": "This is the text of the letter that King Artaxerxes gave to Ezra the priest, the teacher of the law—a scholar of the LORD's commandments and statutes for Israel:",
      "T": "Here is the text of the royal charter Artaxerxes gave to Ezra the priest and Torah scholar—a man devoted to the LORD's commandments and statutes for Israel:"
    },
    "12": {
      "L": "'Artaxerxes, king of kings, to Ezra the priest, scribe of the law of the God of heaven—greetings and all peace. And now:'",
      "M": "'Artaxerxes, king of kings, to Ezra the priest, scholar of the law of the God of heaven—peace in full. And now:'",
      "T": "'Artaxerxes, king of kings, to Ezra the priest and scholar of the law of the God of heaven—peace. And now my decree:'"
    },
    "13": {
      "L": "'I issue a decree that all of the people of Israel, and their priests and Levites, in my realm, who freely choose to go up to Jerusalem, may go with you.'",
      "M": "'I decree that any of the people of Israel—including their priests and Levites—in my realm who wish to go to Jerusalem of their own free will may accompany you.'",
      "T": "'I hereby decree: any Israelites—priests and Levites included—living anywhere in my kingdom who volunteer to go to Jerusalem may do so. No compulsion, no restriction.'"
    },
    "14": {
      "L": "'For you are sent by the king and his seven counsellors to make inquiry concerning Judah and Jerusalem according to the law of your God, which is in your hand;'",
      "M": "'You are sent by the king and his seven counselors to investigate the situation in Judah and Jerusalem in accordance with the law of your God, which you carry with you;'",
      "T": "'You go as the king's envoy—authorized by him and his seven counselors—to assess Judah and Jerusalem by the standard of your God's law, which you hold in your hand.'"
    },
    "15": {
      "L": "'and to carry the silver and gold that the king and his counsellors have freely offered to the God of Israel, whose dwelling is in Jerusalem;'",
      "M": "'You are also to carry the silver and gold that the king and his counselors have willingly contributed to the God of Israel, whose dwelling is in Jerusalem;'",
      "T": "'You will also carry the silver and gold that the king and his counselors have freely given to the God of Israel—the one whose dwelling is in Jerusalem.'"
    },
    "16": {
      "L": "'and all the silver and gold that you can find in all the province of Babylon, with the freewill offering of the people and of the priests, who offer willingly for the house of their God which is in Jerusalem;'",
      "M": "'along with all the silver and gold you can gather from the province of Babylon—the freewill gifts of the people and priests who offer willingly for the house of their God in Jerusalem.'",
      "T": "'Also gather whatever silver and gold is freely given in the province of Babylon—contributions from lay people and priests alike who give voluntarily for their God's house in Jerusalem.'"
    },
    "17": {
      "L": "'With this money you shall promptly buy bulls, rams, and lambs, with their grain offerings and drink offerings, and offer them on the altar of the house of your God which is in Jerusalem.'",
      "M": "'With this money buy bulls, rams, and lambs along with their grain and drink offerings, and offer them on the altar of God's house in Jerusalem.'",
      "T": "'Use this money promptly to purchase bulls, rams, lambs, and the accompanying grain and drink offerings, and present them on the altar of your God's house in Jerusalem.'"
    },
    "18": {
      "L": "'And whatever seems good to you and your brethren to do with the rest of the silver and gold, do it according to the will of your God.'",
      "M": "'Whatever you and your fellow countrymen decide to do with the remaining silver and gold, do it in accordance with the will of your God.'",
      "T": "'Whatever you and your kinsmen judge best to do with any remaining silver and gold—do it. Follow the will of your God.'"
    },
    "19": {
      "L": "'And the vessels that are given to you for the service of the house of your God—deliver those before the God of Jerusalem.'",
      "M": "'The vessels given to you for the service of God's house—present these before the God of Jerusalem.'",
      "T": "'The sacred vessels entrusted to you for God's house—deliver them into the presence of the God of Jerusalem.'"
    },
    "20": {
      "L": "'And whatever else is needed for the house of your God that you shall have occasion to provide, you may provide it from the king's treasury.'",
      "M": "'For anything else needed for your God's house that you find occasion to supply, draw it from the royal treasury.'",
      "T": "'Should you need anything more for God's house beyond what has been given, draw it from the royal treasury.'"
    },
    "21": {
      "L": "'And I, King Artaxerxes, issue a decree to all the treasurers in Trans-Euphrates: whatever Ezra the priest, scribe of the law of the God of heaven, requires of you, let it be done promptly,'",
      "M": "'I, King Artaxerxes, hereby order all the treasurers in Trans-Euphrates: whatever Ezra the priest, scholar of the law of the God of heaven, requests from you, carry it out promptly,'",
      "T": "'I, Artaxerxes the king, command all treasury officials throughout Trans-Euphrates: whatever Ezra the priest—scholar of the law of the God of heaven—requests of you, do it at once.'"
    },
    "22": {
      "L": "'up to one hundred talents of silver, one hundred measures of wheat, one hundred baths of wine, one hundred baths of oil, and salt without limit.'",
      "M": "'This includes up to one hundred talents of silver, one hundred measures of wheat, one hundred baths of wine, one hundred baths of oil, and salt without restriction.'",
      "T": "'This covers up to a hundred talents of silver, a hundred measures of wheat, a hundred baths of wine, a hundred baths of oil—and salt without limit.'"
    },
    "23": {
      "L": "'Whatever is commanded by the God of heaven, let it be done diligently for the house of the God of heaven; for why should there be wrath against the realm of the king and his sons?'",
      "M": "'Whatever the God of heaven commands, carry it out faithfully for his house; for why should wrath come upon the kingdom of the king and his sons?'",
      "T": "'Whatever the God of heaven commands regarding his house—do it diligently. There is no reason to bring his wrath down upon the king and his sons.'"
    },
    "24": {
      "L": "'Also, we declare to you that it shall not be lawful to impose tribute, tax, or toll on any of the priests, Levites, singers, gatekeepers, Nethinim, or other servants of this house of God.'",
      "M": "'We also declare that it is not lawful to impose any tribute, tax, or duty on priests, Levites, singers, gatekeepers, Nethinim, or any other temple servants.'",
      "T": "'Furthermore, be advised: no tribute, tax, or duty may be levied on any member of the temple staff—priests, Levites, singers, gatekeepers, Nethinim, or any other servant of God's house. They are exempt.'"
    },
    "25": {
      "L": "'And you, Ezra, according to the wisdom of your God that is in your hand, appoint magistrates and judges who may judge all the people in Trans-Euphrates—all who know the laws of your God; and teach those who do not know them.'",
      "M": "'And you, Ezra, using the wisdom of your God that you possess, appoint judges and magistrates to administer justice for all the people of Trans-Euphrates—those who know God's laws. Those who do not know them, teach.'",
      "T": "'You, Ezra—by the wisdom your God has given you—are to appoint judges and magistrates to govern all the people of Trans-Euphrates who live under God's law. Those who know it will be governed by it; those who do not, you will teach.'"
    },
    "26": {
      "L": "'And whoever will not do the law of your God and the law of the king, let judgment be executed swiftly upon him, whether by death, exile, confiscation of goods, or imprisonment.'",
      "M": "'Anyone who refuses to obey the law of your God and the law of the king shall be promptly sentenced—whether to death, exile, confiscation of property, or imprisonment.'",
      "T": "'Anyone who defies the law of your God or the law of the king faces swift judgment: death, exile, loss of property, or imprisonment. The authority is total.'"
    },
    "27": {
      "L": "Blessed be the LORD, the God of our fathers, who has put such a thing as this in the king's heart, to beautify the house of the LORD which is in Jerusalem;",
      "M": "Blessed be the LORD, the God of our ancestors, who put this in the king's heart—to honor the house of the LORD in Jerusalem!",
      "T": "Blessed be the LORD, the God of our fathers—who moved even a pagan king's heart to lavish honor upon the LORD's house in Jerusalem!"
    },
    "28": {
      "L": "and who has extended steadfast love to me before the king and his counsellors and before all the king's mighty officers. And I was strengthened, for the hand of the LORD my God was upon me, and I gathered out of Israel leading men to go up with me.",
      "M": "He has also shown me steadfast love in the sight of the king, his counselors, and all the king's powerful officials. Strengthened by the hand of the LORD my God upon me, I gathered the leading men of Israel to make the journey with me.",
      "T": "And he showed me steadfast love before the king, his counselors, and all the king's commanders. That love steadied me—for the hand of the LORD my God was upon me—and I gathered the leading men of Israel to go up with me."
    }
  },
  "8": {
    "1": {
      "L": "These are the heads of their fathers' houses, and this is the genealogy of those who went up with me from Babylon in the reign of King Artaxerxes.",
      "M": "These are the family heads, with their genealogical records, who came up with me from Babylon during the reign of King Artaxerxes.",
      "T": "Here are the family heads—with their genealogical records—who made the journey from Babylon with me during Artaxerxes' reign."
    },
    "2": {
      "L": "Of the sons of Phinehas: Gershom. Of the sons of Ithamar: Daniel. Of the sons of David: Hattush.",
      "M": "From the sons of Phinehas: Gershom. From the sons of Ithamar: Daniel. From the sons of David: Hattush.",
      "T": "From the line of Phinehas: Gershom. From Ithamar: Daniel. From David's line: Hattush."
    },
    "3": {
      "L": "Of the sons of Shechaniah, of the sons of Parosh: Zechariah; and with him were registered by genealogy one hundred and fifty males.",
      "M": "From the sons of Shechaniah, of the sons of Parosh: Zechariah, with one hundred and fifty males registered with him.",
      "T": "From the sons of Shechaniah, of the line of Parosh: Zechariah, with a hundred and fifty males."
    },
    "4": {
      "L": "Of the sons of Pahathmoab: Elihoenai son of Zerahiah, and with him two hundred males.",
      "M": "From the sons of Pahathmoab: Elihoenai son of Zerahiah, with two hundred males.",
      "T": "From Pahathmoab: Elihoenai son of Zerahiah, two hundred males."
    },
    "5": {
      "L": "Of the sons of Shechaniah: the son of Jahaziel, and with him three hundred males.",
      "M": "From the sons of Shechaniah: the son of Jahaziel, with three hundred males.",
      "T": "From Shechaniah: son of Jahaziel, three hundred males."
    },
    "6": {
      "L": "And of the sons of Adin: Ebed son of Jonathan, and with him fifty males.",
      "M": "From the sons of Adin: Ebed son of Jonathan, with fifty males.",
      "T": "From Adin: Ebed son of Jonathan, fifty males."
    },
    "7": {
      "L": "And of the sons of Elam: Jeshaiah son of Athaliah, and with him seventy males.",
      "M": "From the sons of Elam: Jeshaiah son of Athaliah, with seventy males.",
      "T": "From Elam: Jeshaiah son of Athaliah, seventy males."
    },
    "8": {
      "L": "And of the sons of Shephatiah: Zebadiah son of Michael, and with him eighty males.",
      "M": "From the sons of Shephatiah: Zebadiah son of Michael, with eighty males.",
      "T": "From Shephatiah: Zebadiah son of Michael, eighty males."
    },
    "9": {
      "L": "Of the sons of Joab: Obadiah son of Jehiel, and with him two hundred and eighteen males.",
      "M": "From the sons of Joab: Obadiah son of Jehiel, with two hundred and eighteen males.",
      "T": "From Joab: Obadiah son of Jehiel, two hundred and eighteen males."
    },
    "10": {
      "L": "And of the sons of Shelomith: the son of Josiphiah, and with him one hundred and sixty males.",
      "M": "From the sons of Shelomith: the son of Josiphiah, with one hundred and sixty males.",
      "T": "From Shelomith: son of Josiphiah, a hundred and sixty males."
    },
    "11": {
      "L": "And of the sons of Bebai: Zechariah son of Bebai, and with him twenty-eight males.",
      "M": "From the sons of Bebai: Zechariah son of Bebai, with twenty-eight males.",
      "T": "From Bebai: Zechariah son of Bebai, twenty-eight males."
    },
    "12": {
      "L": "And of the sons of Azgad: Johanan son of Hakkatan, and with him one hundred and ten males.",
      "M": "From the sons of Azgad: Johanan son of Hakkatan, with one hundred and ten males.",
      "T": "From Azgad: Johanan son of Hakkatan, a hundred and ten males."
    },
    "13": {
      "L": "And of the last sons of Adonikam—whose names are these: Eliphelet, Jeiel, and Shemaiah—and with them sixty males.",
      "M": "From the later sons of Adonikam—Eliphelet, Jeiel, and Shemaiah—with sixty males.",
      "T": "From the last of Adonikam's family line—Eliphelet, Jeiel, and Shemaiah—sixty males."
    },
    "14": {
      "L": "And of the sons of Bigvai: Uthai and Zabbud, and with them seventy males.",
      "M": "From the sons of Bigvai: Uthai and Zabbud, with seventy males.",
      "T": "From Bigvai: Uthai and Zabbud, seventy males."
    },
    "15": {
      "L": "And I gathered them to the river that runs to Ahava, and we camped there three days; and I reviewed the people and the priests, and found there none of the sons of Levi.",
      "M": "I assembled them at the canal that flows toward Ahava, and we camped there three days. When I reviewed the people and priests, I found that none of the Levites were there.",
      "T": "I assembled the whole company at the Ahava canal. We camped there three days while I took stock of the people and the priests—and I found that not a single Levite was among them."
    },
    "16": {
      "L": "Then I sent for Eliezer, Ariel, Shemaiah, Elnathan, Jarib, Elnathan, Nathan, Zechariah, and Meshullam, leading men; and also for Joiarib and Elnathan, men of understanding.",
      "M": "I then sent for the leading men Eliezer, Ariel, Shemaiah, Elnathan, Jarib, Elnathan, Nathan, Zechariah, and Meshullam, as well as Joiarib and Elnathan, who were men of discernment.",
      "T": "I sent for the leaders: Eliezer, Ariel, Shemaiah, Elnathan, Jarib, Elnathan, Nathan, Zechariah, Meshullam—men of standing—and also Joiarib and Elnathan, who were known for their wisdom."
    },
    "17": {
      "L": "And I sent them with instructions to Iddo the leader at the place Casiphia, telling them what to say to Iddo and his brothers, the Nethinim at Casiphia, that they should bring us ministers for the house of our God.",
      "M": "I sent them with specific instructions to Iddo the chief at Casiphia, giving them a message for Iddo and his fellow Nethinim there: they were to send us servants for the house of our God.",
      "T": "I gave them a detailed message to carry to Iddo, the leader of the Nethinim community at Casiphia—asking him and his brothers to send us qualified servants for God's house."
    },
    "18": {
      "L": "And by the good hand of our God upon us they brought us a man of understanding—Sherebiah, of the sons of Mahli son of Levi son of Israel—with his sons and brothers, eighteen;",
      "M": "By the good hand of our God upon us, they brought us Sherebiah, a man of good judgment from the sons of Mahli son of Levi son of Israel, along with his sons and brothers—eighteen in all;",
      "T": "The good hand of our God was upon us: they delivered Sherebiah—a man of discernment, from Mahli the Levite, Israel's line—along with his sons and brothers, eighteen people."
    },
    "19": {
      "L": "And Hashabiah, and with him Jeshaiah of the sons of Merari, with his brothers and their sons, twenty;",
      "M": "and Hashabiah, with Jeshaiah of the sons of Merari, along with their brothers and sons—twenty in all;",
      "T": "and Hashabiah, and Jeshaiah of the Merari line, with their brothers and sons—twenty people."
    },
    "20": {
      "L": "Also of the Nethinim, whom David and the officials had appointed for the service of the Levites—two hundred and twenty Nethinim; all of them were listed by name.",
      "M": "Also two hundred and twenty Nethinim—the temple servants whom David and the officials had appointed to assist the Levites—all listed by name.",
      "T": "In addition there were two hundred and twenty Nethinim—the temple servants instituted by David and his officials to support the Levites—every one of them named."
    },
    "21": {
      "L": "Then I proclaimed a fast there at the river of Ahava, that we might humble ourselves before our God, to seek from him a safe journey for us, and for our children, and for all our possessions.",
      "M": "There at the Ahava canal I proclaimed a fast, so that we might humble ourselves before our God and seek from him a safe road for ourselves, our children, and all our possessions.",
      "T": "There at the Ahava canal I called a fast. We would humble ourselves before our God and seek from him a protected route—for ourselves, for our children, and for everything we carried."
    },
    "22": {
      "L": "For I was ashamed to ask the king for a band of soldiers and horsemen to help us against the enemy along the way, because we had told the king, 'The hand of our God is upon all who seek him for good; but his power and his wrath are against all who forsake him.'",
      "M": "I was too ashamed to ask the king for troops and cavalry to protect us from enemies along the road, for we had told the king, 'The hand of our God is on everyone who seeks him for their good, but his power and anger are against all who forsake him.'",
      "T": "I could not bring myself to ask the king for soldiers and horsemen to guard us on the road. We had already declared to him: 'The hand of our God rests on all who seek him, for good; but his power and wrath are turned against all who abandon him.' To ask for an escort now would contradict everything we had said."
    },
    "23": {
      "L": "So we fasted and sought our God for this; and he was moved by our plea.",
      "M": "So we fasted and prayed to our God about this, and he answered our prayer.",
      "T": "We fasted and cried out to our God about it—and he heard us."
    },
    "24": {
      "L": "Then I set apart twelve of the leading priests—Sherebiah, Hashabiah, and ten of their brothers with them—",
      "M": "Then I set apart twelve leading priests—Sherebiah, Hashabiah, and ten of their fellow priests—",
      "T": "Then I chose twelve of the chief priests—Sherebiah, Hashabiah, and ten of their colleagues—"
    },
    "25": {
      "L": "and weighed out to them the silver and the gold and the vessels—the offering for the house of our God that the king and his counsellors and his princes and all Israel there present had contributed:",
      "M": "and weighed out to them the silver, gold, and vessels—the offerings for God's house that the king, his counselors, his nobles, and all Israel present had given:",
      "T": "and weighed out to them the silver, gold, and sacred vessels—all the offerings for God's house that the king, his counselors, his nobles, and the assembled people of Israel had contributed:"
    },
    "26": {
      "L": "I weighed out into their hands six hundred and fifty talents of silver, silver vessels worth one hundred talents, one hundred talents of gold,",
      "M": "Into their hands I weighed out six hundred and fifty talents of silver, a hundred talents' worth of silver vessels, a hundred talents of gold,",
      "T": "I weighed into their hands six hundred and fifty talents of silver, silver vessels worth a hundred talents, a hundred talents of gold,"
    },
    "27": {
      "L": "and twenty gold bowls worth a thousand drachmas, and two vessels of fine shining bronze, precious as gold.",
      "M": "twenty gold bowls valued at a thousand drachmas, and two vessels of fine burnished bronze—as valuable as gold.",
      "T": "twenty gold bowls valued at a thousand drachmas, and two vessels of fine polished bronze—precious as gold."
    },
    "28": {
      "L": "And I said to them, 'You are holy to the LORD, and the vessels are holy; and the silver and the gold are a freewill offering to the LORD, the God of your fathers.'",
      "M": "I told them, 'You are consecrated to the LORD, and so are these vessels. The silver and gold are a freewill offering to the LORD, the God of your fathers.'",
      "T": "'You are set apart for the LORD,' I told them, 'and so are these vessels. The silver and gold are a freewill gift to the LORD, the God of your fathers. Guard them accordingly.'"
    },
    "29": {
      "L": "Watch over them and keep them until you weigh them before the leading priests and Levites and the heads of the fathers' houses of Israel at Jerusalem, in the chambers of the house of the LORD.",
      "M": "Guard them carefully until you weigh them out before the leading priests, Levites, and family heads of Israel in the treasury rooms of the LORD's house in Jerusalem.",
      "T": "'Guard them with your lives until you hand them over—weighed and fully accounted—before the chief priests, Levites, and family heads of Israel in the treasury chambers of the LORD's house in Jerusalem.'"
    },
    "30": {
      "L": "So the priests and Levites received the weighed silver and gold and the vessels, to bring them to Jerusalem to the house of our God.",
      "M": "The priests and Levites then received the weighed silver, gold, and vessels to bring to the house of our God in Jerusalem.",
      "T": "The priests and Levites accepted custody of the weighed silver, gold, and vessels—and set their faces toward Jerusalem and God's house."
    },
    "31": {
      "L": "Then we set out from the river of Ahava on the twelfth day of the first month to go to Jerusalem; and the hand of our God was upon us, and he delivered us from the hand of the enemy and from those who lay in ambush along the way.",
      "M": "On the twelfth day of the first month we departed from the Ahava canal for Jerusalem. The hand of our God was upon us, and he rescued us from the grasp of enemies and those who had set ambushes along the road.",
      "T": "On the twelfth day of the first month we left the Ahava canal and turned toward Jerusalem. The hand of our God was upon us—he kept us safe from every enemy, from every ambush set along the road."
    },
    "32": {
      "L": "And we came to Jerusalem and remained there three days.",
      "M": "We arrived in Jerusalem and stayed there three days.",
      "T": "We arrived in Jerusalem and rested three days."
    },
    "33": {
      "L": "On the fourth day the silver and gold and the vessels were weighed in the house of our God by the hand of Meremoth son of Uriah the priest; and with him was Eleazar son of Phinehas, and with them Jozabad son of Jeshua and Noadiah son of Binnui, Levites;",
      "M": "On the fourth day the silver, gold, and vessels were weighed out in God's house, overseen by Meremoth son of Uriah the priest. With him was Eleazar son of Phinehas, and with them the Levites Jozabad son of Jeshua and Noadiah son of Binnui.",
      "T": "On the fourth day we completed the formal transfer: the silver, gold, and vessels were weighed in God's house before Meremoth son of Uriah the priest, together with Eleazar son of Phinehas and the Levites Jozabad son of Jeshua and Noadiah son of Binnui."
    },
    "34": {
      "L": "Everything was counted and weighed by piece; and the total weight was recorded at that time.",
      "M": "Everything was accounted for by number and by weight; the full total was recorded at that time.",
      "T": "Every item counted, every weight verified—and the record was written down on the spot."
    },
    "35": {
      "L": "Also the returned exiles who had come from the captivity offered burnt offerings to the God of Israel: twelve bulls for all Israel, ninety-six rams, seventy-seven lambs, and twelve male goats for a sin offering—all this was a burnt offering to the LORD.",
      "M": "The returned exiles who had come from captivity offered burnt offerings to the God of Israel: twelve bulls for all Israel, ninety-six rams, seventy-seven lambs, and twelve male goats as a sin offering—all of it a burnt offering to the LORD.",
      "T": "The returned exiles offered burnt offerings to Israel's God: twelve bulls for the whole nation, ninety-six rams, seventy-seven lambs, and twelve male goats as a sin offering—the number twelve marking the completeness of Israel across all its tribes, including those still scattered. All this went up to the LORD."
    },
    "36": {
      "L": "And they delivered the king's decrees to the king's satraps and the governors of Trans-Euphrates; and they supported the people and the house of God.",
      "M": "They then presented the king's orders to the royal satraps and governors of Trans-Euphrates, who in turn supported the people and God's house.",
      "T": "Finally they delivered the king's commissions to the royal satraps and the provincial governors of Trans-Euphrates—and those officials extended their support to the people and God's house."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'ezra')
        merge_tier(existing, EZRA, tier_key)
        save(tier_dir, 'ezra', existing)
    print('Ezra 7–8 written.')

if __name__ == '__main__':
    main()
