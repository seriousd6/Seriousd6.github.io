"""
MKT Ezra chapters 3–6 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-ezra-3-6.py

Translation decisions:
- H3068 (יהוה): "LORD" (small-caps convention) in L and M; "the LORD" in T. Consistent with
  Chronicles and other completed OT scripts.
- H430 (אֱלֹהִים) / H426 (Aramaic אֱלָהּ): "God" throughout all three tiers; divine epithets
  "God of Israel," "God of heaven" preserved as given. The Aramaic H426 is Ezra's own usage
  in the diplomatic sections and carries the same weight as H430.
- H2617 (חֶסֶד): occurs in 3:11 ("his mercy endures forever"). Rendered "steadfast love" in L/M,
  "covenant faithfulness" in T — capturing the covenantal, active-loyalty sense the Psalmic
  formula carries.
- H1004 (בַּיִת): "house" (of God/LORD) throughout L and M; "temple" used freely in T where it
  reads more naturally for modern audiences.
- Aramaic sections: Ezra 4:8–6:18 is in Aramaic in the MT (a switch into the imperial
  diplomatic register). Translated naturally without marking this in the English text itself,
  but the Aramaic idioms (royal address formulas, bureaucratic language) are honored. Aramaic
  H4430 (king) and H426 (God) are the semantic equivalents of Hebrew H4428 and H430.
- 4:14 "salt from the palace" (H4415 = lit. salt/maintenance): rendered as "in the service of
  the palace" — the idiom means loyalty to the crown, not literally eating salt.
- 6:22 "king of Assyria": the Persian king is called "king of Assyria" by an anachronistic
  title honoring the ancient hegemony of the region. Retained literally in L/M; T explains
  the political significance.
- H5930 (burnt offerings): "burnt offerings" in L and M; varied to "offerings" in T where
  phrase rhythm demands.
- Aspect notes: Hebrew narrative uses waw-consecutive imperfect (past sequence). Aramaic
  sections use perfect and imperfect for state descriptions. Translated as simple narrative
  past throughout.
- OT echoes: 3:11 quotes the Psalm 136 / 2 Chr 5:13 refrain ("for he is good, his steadfast
  love endures forever"). This is the great dedication psalm of Solomon's temple — its
  reuse at the laying of the second foundation is deliberately retrospective. T surfaces this.
  3:12–13 mirrors Haggai 2:3 — the weeping of those who saw the first temple.
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
  "3": {
    "1": {
      "L": "And when the seventh month arrived and the children of Israel were in their cities, the people gathered as one to Jerusalem.",
      "M": "When the seventh month came and the Israelites had settled in their towns, the people assembled together as one in Jerusalem.",
      "T": "In the seventh month, with Israel settled throughout their towns, the whole people gathered as one body to Jerusalem."
    },
    "2": {
      "L": "And Jeshua son of Jozadak arose, and his brothers the priests, and Zerubbabel son of Shealtiel and his brothers, and they built the altar of the God of Israel, to offer burnt offerings upon it, as it is written in the law of Moses the man of God.",
      "M": "Jeshua son of Jozadak and his fellow priests, along with Zerubbabel son of Shealtiel and his kinsmen, rose up and built the altar of the God of Israel to offer burnt offerings on it, as written in the law of Moses the man of God.",
      "T": "Jeshua son of Jozadak and his priestly brothers, and Zerubbabel son of Shealtiel and his kinsmen, rose up together and built the altar of Israel's God, so they could offer burnt offerings upon it exactly as Moses the man of God had commanded in the Torah."
    },
    "3": {
      "L": "And they set the altar on its foundations, for dread was upon them from the peoples of the lands, and they offered burnt offerings upon it to the LORD, burnt offerings morning and evening.",
      "M": "They set up the altar on its base, though they feared the peoples of the surrounding lands, and offered burnt offerings to the LORD upon it, morning and evening.",
      "T": "They erected the altar on its original base—fear of the surrounding peoples pressing upon them—and offered burnt offerings to the LORD morning and evening, refusing to let opposition silence their worship."
    },
    "4": {
      "L": "And they kept the Feast of Tabernacles as it is written, and offered the daily burnt offerings by number, according to the ordinance, the duty of each day.",
      "M": "They also observed the Feast of Tabernacles as prescribed, offering the required number of burnt offerings day by day according to the rule.",
      "T": "They celebrated the Feast of Tabernacles as the Torah prescribed, presenting the daily burnt offerings in the proper number according to the ordinance—each day's requirement met precisely."
    },
    "5": {
      "L": "And after that, the continual burnt offering—also for the new moons and all the appointed feasts of the LORD that were set apart—and for everyone who willingly offered a freewill offering to the LORD.",
      "M": "They also restored the regular burnt offering for the new moons and all the LORD's appointed feasts, and accepted freewill offerings from everyone who volunteered.",
      "T": "Beyond the daily sacrifice they restored the monthly new-moon offerings and all the LORD's appointed feasts, and welcomed whatever freewill offerings the people brought to the LORD."
    },
    "6": {
      "L": "From the first day of the seventh month they began to offer burnt offerings to the LORD; but the foundation of the house of the LORD was not yet laid.",
      "M": "From the first day of the seventh month they began offering burnt offerings to the LORD, though the foundation of the LORD's house had not yet been laid.",
      "T": "On the very first day of the seventh month, altar-smoke rose again to the LORD—even before a single foundation stone of the temple had been set."
    },
    "7": {
      "L": "And they gave silver to the stonecutters and to the woodworkers, and food and drink and oil to the Sidonians and the Tyrians, to bring cedar timber from Lebanon by sea to Joppa, according to the authorization of Cyrus king of Persia.",
      "M": "They paid silver to the stonecutters and carpenters, and provided food, drink, and oil to the people of Sidon and Tyre, who were to bring cedar logs by sea from Lebanon to Joppa—all in accordance with the grant Cyrus king of Persia had given them.",
      "T": "They hired craftsmen and stonecutters with silver and supplied the Phoenicians of Sidon and Tyre with food, drink, and oil in exchange for cedar logs rafted down from Lebanon to Joppa by sea—working under the authorization Cyrus king of Persia had granted."
    },
    "8": {
      "L": "And in the second year of their coming to the house of God at Jerusalem, in the second month, Zerubbabel son of Shealtiel and Jeshua son of Jozadak began—and the remnant of their brothers the priests and Levites, and all who had come from the captivity to Jerusalem—and they appointed the Levites from twenty years old and upward to oversee the work of the house of the LORD.",
      "M": "In the second year after their arrival at the house of God in Jerusalem, in the second month, Zerubbabel son of Shealtiel, Jeshua son of Jozadak, and all the rest of their fellow priests and Levites—everyone who had come from the captivity—began work, appointing the Levites twenty years old and older to supervise the construction of the LORD's house.",
      "T": "Two years after the returnees reached Jerusalem—in the second month of that year—Zerubbabel son of Shealtiel and Jeshua son of Jozadak set things in motion. Together with the priests, Levites, and all who had come home from Babylon, they put the Levites twenty years and older in charge of supervising the building of the LORD's house."
    },
    "9": {
      "L": "Then Jeshua stood with his sons and his brothers, and Kadmiel and his sons, the sons of Judah, together to oversee the workers on the house of God—the sons of Henadad with their sons and their brothers the Levites.",
      "M": "Jeshua with his sons and brothers, and Kadmiel with his sons, the Judahite Levites, together with the sons of Henadad, their sons and brothers, all stood together to direct the workmen on the house of God.",
      "T": "Jeshua and his kinsmen, Kadmiel and his family—all Levitical lines of Judah and Henadad—took up their posts together to direct the workers building God's house."
    },
    "10": {
      "L": "And when the builders laid the foundation of the house of the LORD, the priests were stationed in their vestments with trumpets, and the Levites, the sons of Asaph, with cymbals, to praise the LORD, after the order of David king of Israel.",
      "M": "When the builders laid the foundation of the LORD's house, the priests took their places in their vestments with trumpets, and the Levites—the sons of Asaph—with cymbals, to praise the LORD according to the directions of King David of Israel.",
      "T": "The moment the builders set the foundation of the LORD's house, the priests put on their vestments and took up their trumpets; the Levites—Asaph's heirs—took up their cymbals; and together they praised the LORD as David king of Israel had commanded."
    },
    "11": {
      "L": "And they sang responsively in praising and giving thanks to the LORD, 'For he is good, for his steadfast love endures forever toward Israel.' And all the people shouted with a great shout when they praised the LORD, because the foundation of the house of the LORD was laid.",
      "M": "They sang antiphonally, praising and giving thanks to the LORD: 'For he is good, his steadfast love toward Israel endures forever.' And all the people shouted with a great shout as they praised the LORD, for the foundation of the LORD's house had been laid.",
      "T": "They sang in alternating voices the ancient refrain of praise and thanksgiving—the same song lifted at Solomon's dedication: 'He is good; his covenant faithfulness toward Israel endures forever.' And at the sound of the foundation stones going down, the whole assembly erupted in a great shout of praise to the LORD."
    },
    "12": {
      "L": "But many of the priests and Levites and heads of fathers' houses, elderly men who had seen the first house, wept with a loud voice when the foundation of this house was laid before their eyes; and many shouted aloud for joy—",
      "M": "Yet many of the priests, Levites, and family heads—old men who had seen the first temple—wept aloud when they saw the foundation of this house being laid. Others shouted for joy,",
      "T": "But many of the older priests, Levites, and family heads—those who had seen Solomon's temple with their own eyes—broke into loud weeping when they watched this foundation go down. Others were shouting with joy."
    },
    "13": {
      "L": "And the people could not distinguish the sound of the joyful shout from the sound of the weeping of the people, for the people raised a great shout and the sound was heard from afar.",
      "M": "No one could distinguish the sound of the joyful shouting from the sound of the people's weeping, for the people raised such a great shout that the sound was heard far away.",
      "T": "Shout and sob mingled into a single great sound—joy and grief inseparable, past and future colliding—and the roar of it carried far across the land."
    }
  },
  "4": {
    "1": {
      "L": "And the adversaries of Judah and Benjamin heard that the children of the captivity were building a house for the LORD, the God of Israel.",
      "M": "When the adversaries of Judah and Benjamin heard that the returned exiles were building a house for the LORD, the God of Israel,",
      "T": "The opponents of Judah and Benjamin got word that the returned exiles were raising a house for the LORD, the God of Israel."
    },
    "2": {
      "L": "They came to Zerubbabel and to the heads of the fathers' houses and said to them, 'Let us build with you, for like you we seek your God, and we have been sacrificing to him since the days of Esarhaddon king of Assyria, who brought us here.'",
      "M": "They approached Zerubbabel and the family heads and said, 'Let us build with you, for we worship your God just as you do. We have been sacrificing to him since Esarhaddon king of Assyria brought us here.'",
      "T": "They came to Zerubbabel and the family heads with a proposal: 'Let us build alongside you—we too seek your God and have been sacrificing to him since Esarhaddon of Assyria settled us in this land.' Their appeal claimed shared devotion."
    },
    "3": {
      "L": "And Zerubbabel and Jeshua and the rest of the heads of the fathers of Israel said to them, 'You have no part with us in building a house for our God; but we alone will build for the LORD, the God of Israel, as Cyrus king of Persia has commanded us.'",
      "M": "But Zerubbabel, Jeshua, and the other Israelite family heads replied, 'You have no share with us in building a house for our God; we alone will build it for the LORD, the God of Israel, as King Cyrus of Persia commanded us.'",
      "T": "Zerubbabel, Jeshua, and the family heads refused flatly: 'You have no part in this project. We will build for the LORD, the God of Israel, alone—it is the mandate Cyrus king of Persia gave to us.'"
    },
    "4": {
      "L": "And the people of the land weakened the hands of the people of Judah and troubled them in building.",
      "M": "So the people of the land discouraged the people of Judah and unsettled them as they built.",
      "T": "Rebuffed, the peoples of the land shifted to sabotage: they wore down Judah's resolve and harassed them throughout the building."
    },
    "5": {
      "L": "And they hired counselors against them to frustrate their plan, all the days of Cyrus king of Persia, even until the reign of Darius king of Persia.",
      "M": "They hired advisers to thwart the Judahites' plans throughout the reign of Cyrus king of Persia and on into the reign of Darius king of Persia.",
      "T": "They even hired political agents to block the project at court—a campaign of obstruction that ran through the entire reign of Cyrus and into the reign of Darius."
    },
    "6": {
      "L": "And in the reign of Ahasuerus, at the beginning of his reign, they wrote against the inhabitants of Judah and Jerusalem an accusation.",
      "M": "In the reign of Ahasuerus, at the beginning of his rule, they filed a formal accusation against the inhabitants of Judah and Jerusalem.",
      "T": "When Ahasuerus took the throne, the opponents lost no time: they filed a formal charge against the people of Judah and Jerusalem at the very start of his reign."
    },
    "7": {
      "L": "And in the days of Artaxerxes, Bishlam, Mithredath, Tabeel, and the rest of their associates wrote to Artaxerxes king of Persia; and the letter was written in Aramaic and translated in Aramaic.",
      "M": "In the days of Artaxerxes, Bishlam, Mithredath, Tabeel, and their colleagues wrote to Artaxerxes king of Persia. The letter was written and rendered in Aramaic.",
      "T": "During the reign of Artaxerxes, Bishlam, Mithredath, Tabeel, and their associates sent yet another letter to the Persian king, composed in the Aramaic diplomatic language of the empire."
    },
    "8": {
      "L": "Rehum the commander and Shimshai the scribe wrote a letter against Jerusalem to King Artaxerxes as follows:",
      "M": "Rehum the commander and Shimshai the scribe composed the following letter against Jerusalem to King Artaxerxes:",
      "T": "Rehum the royal commissioner and Shimshai the secretary drafted an official letter against Jerusalem addressed to King Artaxerxes. It read:"
    },
    "9": {
      "L": "Then Rehum the commander and Shimshai the scribe, and the rest of their associates—the judges, the Persians, the people of Erech, the Babylonians, the Susanchites, the Dehavites, and the Elamites—",
      "M": "Rehum the commander and Shimshai the scribe, together with the rest of their colleagues—the Dinaites, the Apharsathchites, the Tarpelites, the Apharsites, the Archevites, the Babylonians, the Susanchites, the Dehavites, and the Elamites—",
      "T": "The letter came from Rehum the commissioner and Shimshai the secretary, along with their coalition of colleagues—a consortium of peoples settled in the region: Dinaites, Apharsathchites, Tarpelites, Apharsites, Archevites, Babylonians, Susanchites, Dehavites, and Elamites—"
    },
    "10": {
      "L": "and the rest of the nations whom the great and noble Osnappar deported and settled in the cities of Samaria and the rest of Trans-Euphrates—and now:",
      "M": "and the rest of the peoples whom the great and noble Osnappar had deported and settled in the cities of Samaria and elsewhere in Trans-Euphrates. And now:",
      "T": "—and the other nations whom the great Osnappar had exiled and resettled throughout Samaria and the province west of the Euphrates. Their joint address began:"
    },
    "11": {
      "L": "This is the copy of the letter they sent to him, to King Artaxerxes: 'To King Artaxerxes—your servants of Trans-Euphrates. And now:'",
      "M": "This is the copy of the letter they sent to King Artaxerxes: 'To King Artaxerxes, from your servants of Trans-Euphrates. And now:'",
      "T": "'To King Artaxerxes, from your servants, the peoples of Trans-Euphrates:'"
    },
    "12": {
      "L": "'Be it known to the king that the Jews who came up from you to us have arrived at Jerusalem, building the rebellious and wicked city, having set up its walls and repaired the foundations.'",
      "M": "'Let it be known to the king that the Jews who came up from you have arrived in Jerusalem and are rebuilding that rebellious and wicked city. They have set up the walls and repaired the foundations.'",
      "T": "'Be advised, O king: the Jews who left your court have gone to Jerusalem and are rebuilding that city of chronic rebellion. They have already raised the walls and repaired the foundations.'"
    },
    "13": {
      "L": "'Now let it be known to the king that if this city is rebuilt and its walls set up, they will not pay tribute, tax, or toll, and the royal treasury will suffer loss.'",
      "M": "'Now let the king know that if this city is rebuilt and its walls restored, they will not pay tribute, tax, or duty, and the king's revenue will suffer.'",
      "T": "'Know this, O king: once that city is rebuilt and walled, the people will stop paying tribute, tax, and customs—a blow to the royal treasury that will compound over time.'"
    },
    "14": {
      "L": "'Now because we are in the service of the palace and it is not fitting for us to see the king dishonored, therefore we have sent and informed the king,'",
      "M": "'Since we are in the service of the palace and it is not proper for us to stand by while the king is dishonored, we have sent word to inform the king,'",
      "T": "'Since our loyalty is to the royal court and we cannot in conscience watch the king's honor be undermined, we have sent this report to alert you.'"
    },
    "15": {
      "L": "'that search may be made in the record book of your fathers; and you will find in the record book and know that this city is a rebellious city, harmful to kings and provinces, and that revolt has been incited in it from ancient times—for this reason was this city destroyed.'",
      "M": "'Search the record books of your predecessors; you will find that this city has long been rebellious and harmful to kings and provinces, that it has been the source of revolt since ancient times—which is why it was destroyed.'",
      "T": "'Search your royal archives—the chronicles of former kings—and you will discover that Jerusalem has a documented history of rebellion, dangerous to kings and provinces alike. Sedition is its heritage; that is precisely why it was destroyed in the first place.'"
    },
    "16": {
      "L": "'We make known to the king that if this city is built and its walls set up, you will have no portion in Trans-Euphrates.'",
      "M": "'We inform the king that if this city is rebuilt and its walls restored, you will have no portion left in Trans-Euphrates.'",
      "T": "'We are warning you plainly: if Jerusalem is rebuilt and walled, your hold on Trans-Euphrates will be gone.'"
    },
    "17": {
      "L": "The king sent a reply to Rehum the commander and Shimshai the scribe and the rest of their associates who lived in Samaria and the rest of Trans-Euphrates: 'Greetings. And now:'",
      "M": "The king sent his answer to Rehum the commander, Shimshai the scribe, and their associates living in Samaria and throughout Trans-Euphrates: 'Greetings. Now then:'",
      "T": "The king's response was addressed to Rehum the commissioner, Shimshai the secretary, and their coalition in Samaria and throughout Trans-Euphrates: 'Peace. And now my reply:'"
    },
    "18": {
      "L": "'The letter that you sent to us has been read plainly before me.'",
      "M": "'The letter you sent has been read aloud in my presence in full.'",
      "T": "'The letter you sent has been read to me in full.'"
    },
    "19": {
      "L": "'And I issued a decree, and search was made, and it was found that this city from ancient times has risen against kings, and that revolt and sedition have occurred in it.'",
      "M": "'I ordered a search, and it was found that this city has a long history of rising against kings and that rebellion and revolt have occurred there.'",
      "T": "'I commanded a search of the records, and it has been confirmed: Jerusalem has a documented history of rising against its overlords, and of harboring sedition and revolt.'"
    },
    "20": {
      "L": "'And mighty kings have ruled over Jerusalem, who held sway over all Trans-Euphrates, and tribute, tax, and toll were paid to them.'",
      "M": "'Powerful kings once ruled in Jerusalem and had authority over all Trans-Euphrates; tribute, tax, and customs were paid to them.'",
      "T": "'The historical record shows that Jerusalem once commanded the entire region west of the Euphrates, with tribute and taxes flowing to its kings—an imperial reach we cannot afford to see revived.'"
    },
    "21": {
      "L": "'Give now a command to make these men stop, and that this city not be built until a command is issued by me.'",
      "M": "'Issue a command now to stop these men. This city must not be rebuilt until I give a further order.'",
      "T": "'Issue the order at once: halt these men. Jerusalem is not to be rebuilt until I give further instruction.'"
    },
    "22": {
      "L": "'Take care that you do not neglect this. Why should damage increase to the harm of the kings?'",
      "M": "'Be careful not to neglect this. Why should this harm grow and hurt the king's interests?'",
      "T": "'Do not be careless about this. Why let harm accumulate to the detriment of the crown?'"
    },
    "23": {
      "L": "Then when the copy of King Artaxerxes' letter was read before Rehum and Shimshai the scribe and their companions, they went in haste to Jerusalem to the Jews and stopped them by force and power.",
      "M": "As soon as the copy of King Artaxerxes' letter was read before Rehum, Shimshai the scribe, and their associates, they hurried to Jerusalem and forcibly compelled the Jews to stop.",
      "T": "The moment the king's letter was read before Rehum and Shimshai and their allies, they rushed to Jerusalem and stopped the building by force—swiftly, decisively, with full imperial authority behind them."
    },
    "24": {
      "L": "Then the work on the house of God in Jerusalem ceased; and it remained at a halt until the second year of the reign of Darius king of Persia.",
      "M": "At that point the work on God's house in Jerusalem stopped—and it remained halted until the second year of the reign of Darius king of Persia.",
      "T": "The building of God's house in Jerusalem came to a complete stop. It would not resume until the second year of King Darius of Persia."
    }
  },
  "5": {
    "1": {
      "L": "Then Haggai the prophet and Zechariah son of Iddo prophesied to the Jews in Judah and Jerusalem in the name of the God of Israel, even to them.",
      "M": "Then the prophets Haggai and Zechariah son of Iddo prophesied to the Jews in Judah and Jerusalem in the name of the God of Israel.",
      "T": "Then the word of God came through Haggai the prophet and Zechariah son of Iddo: both prophesied to the Jewish communities of Judah and Jerusalem, speaking in the name of Israel's God."
    },
    "2": {
      "L": "Then Zerubbabel son of Shealtiel and Jeshua son of Jozadak rose up and began to build the house of God in Jerusalem, and with them the prophets of God supporting them.",
      "M": "Zerubbabel son of Shealtiel and Jeshua son of Jozadak rose up and resumed building God's house in Jerusalem, with the prophets of God giving them support.",
      "T": "Zerubbabel son of Shealtiel and Jeshua son of Jozadak rose to the prophetic summons and restarted the work on God's house in Jerusalem. The prophets stood alongside them, lending their authority to the project."
    },
    "3": {
      "L": "At that time Tattenai, governor of Trans-Euphrates, and Shetharboznai and their associates came to them and said, 'Who gave you authorization to build this house and to complete this wall?'",
      "M": "At that time Tattenai, governor of Trans-Euphrates, and Shetharboznai and their associates came to them and demanded, 'Who authorized you to build this house and complete this wall?'",
      "T": "That very moment, Tattenai the governor of Trans-Euphrates and Shetharboznai arrived on site with their delegation and challenged them: 'Who gave you authority to build this house and raise these walls?'"
    },
    "4": {
      "L": "Then we said to them accordingly, 'What are the names of the men who are building this structure?'",
      "M": "We also asked them, 'What are the names of the men carrying out this building?'",
      "T": "They pressed further, demanding the names of every man involved in the building."
    },
    "5": {
      "L": "But the eye of their God was upon the elders of the Jews, so that they could not make them stop until the report reached Darius and the reply was returned by letter in this matter.",
      "M": "But the eye of their God was on the elders of the Jews, so the officials could not stop them until the report reached Darius and a reply was sent back by letter.",
      "T": "But God's eye was on the elders of the Jewish community—his watchful care overrode official pressure—and the work continued while the matter was referred all the way to Darius, awaiting his reply."
    },
    "6": {
      "L": "The copy of the letter that Tattenai, governor of Trans-Euphrates, and Shetharboznai and his companions the Apharsachites in Trans-Euphrates, sent to King Darius:",
      "M": "Here is a copy of the letter Tattenai, governor of Trans-Euphrates, and Shetharboznai and their associates the Apharsachites in Trans-Euphrates sent to King Darius:",
      "T": "What follows is the text of the letter Tattenai the governor of Trans-Euphrates, together with Shetharboznai and the Apharsachite council, sent to King Darius:"
    },
    "7": {
      "L": "They sent a letter to him, and in it was written thus: 'To Darius the king, all peace.'",
      "M": "They sent him a letter with these words: 'To King Darius, all greetings.'",
      "T": "'To King Darius—peace in full.'"
    },
    "8": {
      "L": "'Be it known to the king that we went to the province of Judah, to the house of the great God, which is being built with large stones and with timber set in the walls. This work proceeds diligently and prospers in their hands.'",
      "M": "'Let it be known to the king that we went to the province of Judah, to the house of the great God. It is being built with large cut stones and with timbers set into the walls. The work moves forward energetically and is succeeding.'",
      "T": "'Know, O king, that we traveled to the province of Judah and inspected the house of the great God. It is being built with massive stones and timber beams embedded in the walls—the work is advancing rapidly and clearly prospering.'"
    },
    "9": {
      "L": "'Then we asked those elders and said to them thus: Who commanded you to build this house and to complete these walls?'",
      "M": "'We questioned the elders and asked them, Who authorized you to build this house and complete these walls?'",
      "T": "'We questioned the community elders directly: By whose authority are you building this house and raising these walls?'"
    },
    "10": {
      "L": "'We also asked their names to inform you, that we might write down the names of the men who are their leaders.'",
      "M": "'We also asked for their names, so that we could record the names of their leaders and inform you.'",
      "T": "'We asked for the names of their leaders as well, so we could document them and report them to you.'"
    },
    "11": {
      "L": "'And thus they returned us answer, saying: We are the servants of the God of heaven and earth, and we are rebuilding the house that was built many years ago, which a great king of Israel built and established.'",
      "M": "'They gave us this answer: We are servants of the God of heaven and earth. We are rebuilding the house that was constructed many years ago by a great king of Israel.'",
      "T": "'They replied: We are servants of the God of heaven and earth, and we are rebuilding a house that a great king of Israel constructed many years ago—and we rebuild it by right.'"
    },
    "12": {
      "L": "'But because our fathers angered the God of heaven, he gave them into the hand of Nebuchadnezzar king of Babylon, the Chaldean, who destroyed this house and carried the people into exile in Babylon.'",
      "M": "'But because our ancestors provoked the God of heaven to anger, he handed them over to Nebuchadnezzar king of Babylon, the Chaldean, who destroyed this house and exiled the people to Babylon.'",
      "T": "'But our ancestors provoked the God of heaven to wrath, and he handed them over to Nebuchadnezzar the Chaldean king of Babylon, who demolished this house and drove the people into exile.'"
    },
    "13": {
      "L": "'But in the first year of Cyrus king of Babylon, Cyrus the king issued a decree to build this house of God.'",
      "M": "'Then in the first year of Cyrus king of Babylon, Cyrus the king issued a decree to rebuild this house of God.'",
      "T": "'In the first year of Cyrus king of Babylon, however, Cyrus himself issued a decree to rebuild this house of God.'"
    },
    "14": {
      "L": "'And the gold and silver vessels of the house of God, which Nebuchadnezzar had taken from the temple in Jerusalem and brought to the temple of Babylon, Cyrus the king retrieved from the temple of Babylon and delivered to one named Sheshbazzar, whom he had appointed governor.'",
      "M": "'Moreover, the gold and silver vessels of God's house that Nebuchadnezzar had taken from the Jerusalem temple and placed in the Babylonian temple were retrieved by Cyrus and handed over to Sheshbazzar, the man he appointed as governor.'",
      "T": "'Furthermore, the gold and silver vessels that Nebuchadnezzar had looted from the Jerusalem temple and stored in the Babylonian temple—Cyrus himself retrieved these and entrusted them to Sheshbazzar, the governor he appointed.'"
    },
    "15": {
      "L": "'And he said to him, Take these vessels, go, carry them to the temple that is in Jerusalem, and let the house of God be built in its place.'",
      "M": "'Cyrus told him, Take these vessels, bring them to the temple in Jerusalem, and let God's house be rebuilt where it stood before.'",
      "T": "'Cyrus charged him: Take these vessels, return them to the temple in Jerusalem, and see that God's house is rebuilt on its original site.'"
    },
    "16": {
      "L": "'Then Sheshbazzar came and laid the foundation of the house of God in Jerusalem, and from that time until now it has been under construction, yet it is not finished.'",
      "M": "'Then Sheshbazzar came and laid the foundation of God's house in Jerusalem. From that time to now it has been under construction, though it is not yet complete.'",
      "T": "'Sheshbazzar came and laid the foundation of God's house in Jerusalem. Work has been ongoing from that day to this—though the building is still not finished.'"
    },
    "17": {
      "L": "'Now therefore, if it seems good to the king, let search be made in the royal archives in Babylon, whether a decree was issued by Cyrus the king to build this house of God in Jerusalem; and let the king send us his decision in this matter.'",
      "M": "'Now, if it pleases the king, let a search be made in the royal archives in Babylon to verify whether Cyrus the king did in fact issue a decree to rebuild God's house in Jerusalem. Then let the king's decision be communicated to us.'",
      "T": "'We therefore request, if it please the king, that the royal archives in Babylon be searched to verify whether Cyrus issued such a decree. Then let the king's decision be communicated to us.'"
    }
  },
  "6": {
    "1": {
      "L": "Then King Darius issued a decree, and search was made in the house of the archives, in the treasury at Babylon.",
      "M": "Then King Darius issued a decree, and a search was made in the house of archives where the records were stored in Babylon.",
      "T": "King Darius issued the order, and a search was conducted in the Babylonian treasury archives where the official records were kept."
    },
    "2": {
      "L": "And there was found at Ecbatana, in the palace that is in the province of Media, a scroll; and in it was a record written as follows:",
      "M": "A scroll was found at Ecbatana, in the fortress-palace in the province of Media. In it was the following record:",
      "T": "In the fortress-palace of Ecbatana, the Median capital, a scroll was found containing this entry:"
    },
    "3": {
      "L": "In the first year of Cyrus the king, Cyrus the king issued a decree: Concerning the house of God at Jerusalem, let the house be built, the place where sacrifices are offered, and let its foundations be firmly laid; its height sixty cubits and its breadth sixty cubits,",
      "M": "In the first year of King Cyrus, King Cyrus issued this decree: Concerning God's house in Jerusalem—let the house be built as the place where sacrifices are offered. Its foundations shall be firmly laid, its height sixty cubits, and its width sixty cubits.",
      "T": "'Year one of King Cyrus. Royal decree: The house of God in Jerusalem is to be rebuilt as a site for sacrifice. Its foundation is to be solidly laid; height sixty cubits, width sixty cubits.'"
    },
    "4": {
      "L": "with three courses of large stones and one course of timber; and let the expense be paid from the royal treasury.",
      "M": "The structure shall have three courses of large stones and one course of timber; all expenses to be paid from the royal treasury.",
      "T": "'Three rows of large stones, then a row of timber. All costs to be paid from the royal treasury.'"
    },
    "5": {
      "L": "And also let the gold and silver vessels of the house of God, which Nebuchadnezzar took from the temple in Jerusalem and brought to Babylon, be returned to the temple in Jerusalem, each to its place, to be placed in the house of God.",
      "M": "Furthermore, the gold and silver vessels of God's house that Nebuchadnezzar took from Jerusalem and brought to Babylon are to be returned and replaced in the temple in Jerusalem, each piece in its proper place in God's house.",
      "T": "'The sacred gold and silver vessels looted by Nebuchadnezzar from the Jerusalem temple and brought to Babylon are to be returned and restored to their proper places in God's house in Jerusalem.'"
    },
    "6": {
      "L": "Now therefore, Tattenai, governor of Trans-Euphrates, and Shetharboznai and your colleagues the Apharsachites in Trans-Euphrates—stay away from there.",
      "M": "Therefore, Tattenai, governor of Trans-Euphrates, Shetharboznai, and your fellow Apharsachites in Trans-Euphrates—keep away from there.",
      "T": "'Therefore, Tattenai—governor of Trans-Euphrates—together with Shetharboznai and the Apharsachite council: stay out of this matter.'"
    },
    "7": {
      "L": "Leave the work of this house of God alone; let the governor of the Jews and the elders of the Jews build this house of God in its place.",
      "M": "Do not interfere with the work on this house of God. Let the governor of the Jews and the Jewish elders rebuild God's house on its site.",
      "T": "'Do not interfere with the construction. Let the governor of Judah and the Jewish elders rebuild God's house where it stands.'"
    },
    "8": {
      "L": "Moreover, I issue a decree concerning what you are to do for these Jewish elders in building this house of God: from the royal revenue of Trans-Euphrates, let expenses be promptly paid to these men, so that the work is not hindered.",
      "M": "Moreover, I hereby decree what you are to do for these Jewish elders as they build God's house: from the royal revenue of Trans-Euphrates, pay these men's expenses promptly so the work is not interrupted.",
      "T": "'Furthermore, here is your obligation toward the Jewish elders building God's house: pay their full expenses from the royal tribute of Trans-Euphrates—immediately, without delay or obstruction.'"
    },
    "9": {
      "L": "And whatever they need—young bulls, rams, and lambs for burnt offerings to the God of heaven, wheat, salt, wine, and oil, according to the word of the priests in Jerusalem—let it be given to them day by day without fail,",
      "M": "Whatever they need—young bulls, rams, and lambs for burnt offerings to the God of heaven, along with wheat, salt, wine, and oil, as the Jerusalem priests direct—give it to them without fail, day by day,",
      "T": "'Whatever they require for offerings to the God of heaven—young bulls, rams, lambs, wheat, salt, wine, oil, as the Jerusalem priests specify—provide it daily without exception.'"
    },
    "10": {
      "L": "so that they may offer pleasing sacrifices to the God of heaven and pray for the life of the king and his sons.",
      "M": "so that they may offer acceptable sacrifices to the God of heaven and pray for the welfare of the king and his sons.",
      "T": "'So that they may present offerings pleasing to the God of heaven—and pray for the life of the king and his sons.'"
    },
    "11": {
      "L": "Also I have decreed that if anyone alters this edict, a beam is to be pulled from his house and he shall be impaled on it, and his house made a dunghill on account of this.",
      "M": "I have further decreed that anyone who defies this order shall have a beam pulled from his own house, be impaled on it, and his house turned into a refuse heap for this offense.",
      "T": "'I further decree: anyone who tampers with this order will have a beam ripped from his house, hoisted up, and be impaled on it. His house will be turned into a dunghill. This is the penalty.'"
    },
    "12": {
      "L": "And may the God who has caused his name to dwell there overthrow any king or people who shall attempt to alter this, to destroy this house of God in Jerusalem. I, Darius, have decreed it; let it be done with all diligence.",
      "M": "May the God who has caused his name to dwell there overthrow any king or people who tries to alter this and destroy God's house in Jerusalem. I, Darius, have issued this decree. Let it be carried out promptly.",
      "T": "'And may the God who has chosen Jerusalem as the dwelling place of his name bring ruin upon any king or nation that raises a hand against this temple. I, Darius, have decreed it. Execute it without delay.'"
    },
    "13": {
      "L": "Then Tattenai, governor of Trans-Euphrates, and Shetharboznai and their companions carried out all that Darius the king had decreed, promptly.",
      "M": "Then Tattenai, governor of Trans-Euphrates, Shetharboznai, and their associates carried out everything King Darius had decreed, and they did it promptly.",
      "T": "Tattenai, governor of Trans-Euphrates, Shetharboznai, and their colleagues acted at once, executing every provision of King Darius' decree."
    },
    "14": {
      "L": "And the elders of the Jews built and prospered through the prophesying of Haggai the prophet and Zechariah son of Iddo; and they built and completed it by the command of the God of Israel and by the decree of Cyrus and Darius and Artaxerxes king of Persia.",
      "M": "The Jewish elders built and prospered under the prophetic encouragement of Haggai and Zechariah son of Iddo. They built and completed the work by the command of the God of Israel and by the decrees of Cyrus, Darius, and Artaxerxes king of Persia.",
      "T": "The Jewish elders built forward and prospered—propelled by the prophetic ministry of Haggai and Zechariah son of Iddo. And they completed it: by the mandate of Israel's God, confirmed in succession by the decrees of Cyrus, Darius, and Artaxerxes."
    },
    "15": {
      "L": "And this house was finished on the third day of the month Adar, in the sixth year of the reign of King Darius.",
      "M": "The house was completed on the third day of the month of Adar in the sixth year of King Darius' reign.",
      "T": "The temple was finished on the third of Adar in Darius' sixth year—a moment the nation would remember as God's faithfulness made visible."
    },
    "16": {
      "L": "And the children of Israel, the priests, the Levites, and the rest of the returned exiles kept the dedication of this house of God with joy,",
      "M": "The Israelites—priests, Levites, and the rest of the returned exiles—celebrated the dedication of God's house with joy.",
      "T": "The whole community—priests, Levites, all the returned exiles of Israel—gathered to dedicate God's house with overflowing joy."
    },
    "17": {
      "L": "and offered at the dedication of this house of God one hundred bulls, two hundred rams, four hundred lambs, and twelve male goats as a sin offering for all Israel, according to the number of the tribes of Israel.",
      "M": "At the dedication they offered one hundred bulls, two hundred rams, four hundred lambs, and twelve male goats as a sin offering for all Israel—one for each of the twelve tribes.",
      "T": "The dedication offerings were: a hundred bulls, two hundred rams, four hundred lambs—and twelve male goats as a sin offering for all Israel, the number twelve deliberately invoking the twelve tribes of a people still largely scattered."
    },
    "18": {
      "L": "And they stationed the priests in their divisions and the Levites in their courses for the service of God in Jerusalem, as it is written in the book of Moses.",
      "M": "They appointed the priests to their divisions and the Levites to their courses for the worship of God in Jerusalem, as prescribed in the Book of Moses.",
      "T": "The priests were assigned to their divisions and the Levites to their courses for the ongoing worship of God in Jerusalem—all as the Book of Moses prescribes."
    },
    "19": {
      "L": "And the children of the captivity kept the Passover on the fourteenth day of the first month.",
      "M": "The returned exiles observed the Passover on the fourteenth day of the first month.",
      "T": "The returned exiles kept the Passover on the fourteenth day of the first month."
    },
    "20": {
      "L": "For the priests and Levites had purified themselves together; all of them were clean. And they slaughtered the Passover lamb for all the returned exiles, and for their brother priests, and for themselves.",
      "M": "The priests and Levites had all purified themselves; they were all ritually clean. They slaughtered the Passover lamb for all the returned exiles, for their fellow priests, and for themselves.",
      "T": "The priests and Levites had prepared themselves with a communal act of purification—all of them clean—and they slaughtered the Passover for the entire body of returned exiles, for their fellow priests, and for themselves."
    },
    "21": {
      "L": "And the children of Israel who had returned from captivity ate, along with all who had separated themselves from the uncleanness of the peoples of the land to seek the LORD God of Israel.",
      "M": "The returned Israelites ate the Passover, along with everyone who had separated themselves from the impurity of the surrounding peoples to seek the LORD God of Israel.",
      "T": "The Passover meal was shared by two groups: the returned exiles of Israel, and any from among the surrounding peoples who had broken with their neighbors' impurity to seek the LORD, the God of Israel."
    },
    "22": {
      "L": "And they kept the Feast of Unleavened Bread seven days with joy, for the LORD had made them joyful and had turned the heart of the king of Assyria toward them, to strengthen their hands in the work of the house of God, the God of Israel.",
      "M": "They celebrated the Feast of Unleavened Bread with joy for seven days, for the LORD had filled them with joy and had turned the king of Assyria's heart toward them to support their work on the house of God, the God of Israel.",
      "T": "For seven days they kept the Feast of Unleavened Bread in full joy—for the LORD himself had filled them with gladness and had bent even the heart of a pagan king—called here by the ancient title 'king of Assyria' for the old imperial seat—to favor them and strengthen their hands as they built the house of Israel's God."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'ezra')
        merge_tier(existing, EZRA, tier_key)
        save(tier_dir, 'ezra', existing)
    print('Ezra 3–6 written.')

if __name__ == '__main__':
    main()
