"""
MKT Nehemiah chapters 7–8 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-nehemiah-7-8.py

Translation decisions:
- H3068 (יהוה): "LORD" in L and M; "the LORD" in T — consistent with mkt-nehemiah-1-3.py.
- H430 (אֱלֹהִים): "God" throughout. "God of heaven" preserved as the characteristic
  Nehemiah-era divine title where it occurs.
- H8451 (תּוֹרָה, Torah): "the Law" in L and M; expanded in T where the full context
  warrants ("the Law of Moses," "the Torah"). Chapter 8 centers on its public reading —
  a covenant-renewal watershed in Israel's post-exilic history.
- H4581 (מָעוֹז, maoz) at 8:10: glossed "strength" in L/M. T renders "stronghold /
  fortified refuge" — maoz is military vocabulary for a fortress, not merely personal
  vitality. The clause "the joy of the LORD is your stronghold" carries a defense-of-the-
  city resonance that the wall-building context makes vivid.
- H2304 (חֶדְוָה, chedvah) at 8:10: "joy" in all three tiers — correct and unambiguous.
- "Tirshatha" (7:65, 7:70): the Persian loanword for the province's governor. L preserves
  "the Tirshatha" as a technical term; M uses "the governor"; T: "the governor—Nehemiah's
  Persian title—" explaining that Nehemiah is the referent.
- H2232 / H6635 ("Urim and Thummim", 7:65): preserved in all tiers. The appeal to a
  future priest who can consult these is forward-looking, almost messianic: a definitive
  answer is expected but not yet available. T notes this.
- Chapter 7 genealogical census: nearly identical to Ezra 2:1-67. This is not literary
  padding — Nehemiah found the register and used it to reconstitute the covenant community
  for the repopulation of Jerusalem (7:4-5). L and M follow list structure faithfully.
  T frames the theological function at v5 and notes anomalies: the priests excluded for
  missing genealogy (7:63-65), the total discrepancy at v66, and the closing transition
  to the seventh month (v73) that leads directly into the Torah reading.
- 7:66 total (42,360): the sum of all named groups falls short of the stated total —
  a well-known discrepancy going back to the earliest manuscripts. The total apparently
  includes groups not individually enumerated. T notes this without over-explaining.
- 8:8 "gave the sense / gave understanding in the reading" (וַיָּבִינוּ בַּמִּקְרָא):
  The Levites interpreted the text as it was read — the earliest textual hint of what
  later became the Aramaic Targum practice. T surfaces this.
- 8:10 "the joy of the LORD is your strength": the fuller rendering is discussed above
  under H4581. T also notes the contextual irony: people weeping at the Law's weight are
  told that the LORD's own joy over them is a fortified wall.
- 8:14-15: The immediate obedience pattern — read → discover → proclaim → build — is
  a covenant renewal sequence. T marks this.
- 8:17 "since the days of Jeshua son of Nun": not an absolute claim that Sukkot was
  never observed between Joshua and Nehemiah, but that this celebration — all returned
  exiles together, in the rebuilt city, with daily public Torah reading — was unprecedented
  in completeness and scale. T qualifies this.
- 8:18 OT echo: "on the eighth day there was a solemn assembly, according to the rule" —
  Numbers 29:35 and Leviticus 23:36. T names the Mosaic authority behind the eighth-day
  assembly.
- Aspect: Hebrew narrative past (waw-consecutive imperfect) throughout both chapters.
  Chapter 8 has vivid present-tense urgency in the narrative sequence — T captures this.
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
  "7": {
    "1": {
      "L": "Now when the wall was built and I had set up the doors, the gatekeepers, the singers, and the Levites were appointed.",
      "M": "After the wall was built and the doors had been set in place, I appointed the gatekeepers, singers, and Levites.",
      "T": "Once the wall stood complete and the gates were in place, Nehemiah turned to the interior order of the city: gatekeepers, singers, and Levites were assigned their posts."
    },
    "2": {
      "L": "And I gave my brother Hanani, and Hananiah the commander of the castle, charge over Jerusalem, for he was a more faithful and God-fearing man than many.",
      "M": "I put my brother Hanani and Hananiah the commander of the citadel in charge of Jerusalem, for Hananiah was a more faithful and God-fearing man than most.",
      "T": "I appointed my kinsman Hanani, together with Hananiah the commander of the citadel, to govern Jerusalem. The reason: Hananiah was genuinely faithful—a man who feared God more than most."
    },
    "3": {
      "L": "And I said to them, 'Let not the gates of Jerusalem be opened until the sun is hot. And while they are still standing guard, let them shut the doors and bar them. Appoint guards from among the inhabitants of Jerusalem, each at his watch post and each in front of his own house.'",
      "M": "I instructed them: 'Do not open the gates of Jerusalem until the sun is high. While the guards are still on duty, have them shut and bar the doors. Appoint residents of Jerusalem as guards, each at his watch post and each in front of his own house.'",
      "T": "'Do not open Jerusalem's gates until the sun is fully up,' I told them. 'And while the guards are still in position, shut and bar the doors. Station the city's own residents as the watch—each at his post, each responsible for the stretch in front of his own home.' A sparsely-peopled city had to guard itself with strict discipline."
    },
    "4": {
      "L": "The city was wide and large, but the people within it were few, and no houses had been rebuilt.",
      "M": "Now the city was large and spacious, but the population was small, and the houses had not yet been rebuilt.",
      "T": "Jerusalem was large and open—its walls spacious—but its population was thin, and most of the houses were still rubble. The shell of the city had been rebuilt; the community inside it was not yet filled."
    },
    "5": {
      "L": "Then my God put it into my heart to assemble the nobles, the officials, and the people to be registered by genealogy. And I found the book of the genealogy of those who came up first, and I found written in it:",
      "M": "Then my God put it into my heart to assemble the nobles, the officials, and the people for a genealogical registration. And I found the book of the genealogy of those who had come up first, with the following written in it:",
      "T": "Then God moved me to act: to gather the nobles, the officials, and the ordinary people for a genealogical census. The covenant community needed to be reconstituted on paper as it had been reconstituted in stone. I found the register of the first wave of returning exiles—and this is what it contained:"
    },
    "6": {
      "L": "These are the people of the province who came up out of the captivity of those exiles whom Nebuchadnezzar the king of Babylon had carried into exile. They returned to Jerusalem and Judah, each to his own town.",
      "M": "These are the people of the province who came up from the captivity of the exiles whom Nebuchadnezzar king of Babylon had deported. They returned to Jerusalem and Judah, each to his own hometown.",
      "T": "These are the members of the restored community—descendants of those whom Nebuchadnezzar king of Babylon had deported. They came back to Jerusalem and Judah, each family to the town they had been pulled from."
    },
    "7": {
      "L": "They came with Zerubbabel, Jeshua, Nehemiah, Azariah, Raamiah, Nahamani, Mordecai, Bilshan, Mispereth, Bigvai, Nehum, and Baanah. The number of the men of the people of Israel:",
      "M": "They came with Zerubbabel, Jeshua, Nehemiah, Azariah, Raamiah, Nahamani, Mordecai, Bilshan, Mispereth, Bigvai, Nehum, and Baanah. The count of the Israelite men was as follows:",
      "T": "They came under the leadership of Zerubbabel, Jeshua, Nehemiah, Azariah, Raamiah, Nahamani, Mordecai, Bilshan, Mispereth, Bigvai, Nehum, and Baanah. The count of the Israelite men:"
    },
    "8": {
      "L": "The children of Parosh, two thousand one hundred and seventy-two.",
      "M": "The descendants of Parosh: 2,172.",
      "T": "Parosh: 2,172."
    },
    "9": {
      "L": "The children of Shephatiah, three hundred and seventy-two.",
      "M": "The descendants of Shephatiah: 372.",
      "T": "Shephatiah: 372."
    },
    "10": {
      "L": "The children of Arah, six hundred and fifty-two.",
      "M": "The descendants of Arah: 652.",
      "T": "Arah: 652."
    },
    "11": {
      "L": "The children of Pahath-moab, of the children of Jeshua and Joab, two thousand eight hundred and eighteen.",
      "M": "The descendants of Pahath-moab, through the line of Jeshua and Joab: 2,818.",
      "T": "Pahath-moab (through Jeshua and Joab): 2,818."
    },
    "12": {
      "L": "The children of Elam, one thousand two hundred and fifty-four.",
      "M": "The descendants of Elam: 1,254.",
      "T": "Elam: 1,254."
    },
    "13": {
      "L": "The children of Zattu, eight hundred and forty-five.",
      "M": "The descendants of Zattu: 845.",
      "T": "Zattu: 845."
    },
    "14": {
      "L": "The children of Zaccai, seven hundred and sixty.",
      "M": "The descendants of Zaccai: 760.",
      "T": "Zaccai: 760."
    },
    "15": {
      "L": "The children of Binnui, six hundred and forty-eight.",
      "M": "The descendants of Binnui: 648.",
      "T": "Binnui: 648."
    },
    "16": {
      "L": "The children of Bebai, six hundred and twenty-eight.",
      "M": "The descendants of Bebai: 628.",
      "T": "Bebai: 628."
    },
    "17": {
      "L": "The children of Azgad, two thousand three hundred and twenty-two.",
      "M": "The descendants of Azgad: 2,322.",
      "T": "Azgad: 2,322."
    },
    "18": {
      "L": "The children of Adonikam, six hundred and sixty-seven.",
      "M": "The descendants of Adonikam: 667.",
      "T": "Adonikam: 667."
    },
    "19": {
      "L": "The children of Bigvai, two thousand and sixty-seven.",
      "M": "The descendants of Bigvai: 2,067.",
      "T": "Bigvai: 2,067."
    },
    "20": {
      "L": "The children of Adin, six hundred and fifty-five.",
      "M": "The descendants of Adin: 655.",
      "T": "Adin: 655."
    },
    "21": {
      "L": "The children of Ater, namely of Hezekiah, ninety-eight.",
      "M": "The descendants of Ater, that is of Hezekiah: 98.",
      "T": "Ater (of Hezekiah): 98."
    },
    "22": {
      "L": "The children of Hashum, three hundred and twenty-eight.",
      "M": "The descendants of Hashum: 328.",
      "T": "Hashum: 328."
    },
    "23": {
      "L": "The children of Bezai, three hundred and twenty-four.",
      "M": "The descendants of Bezai: 324.",
      "T": "Bezai: 324."
    },
    "24": {
      "L": "The children of Hariph, one hundred and twelve.",
      "M": "The descendants of Hariph: 112.",
      "T": "Hariph: 112."
    },
    "25": {
      "L": "The children of Gibeon, ninety-five.",
      "M": "The descendants of Gibeon: 95.",
      "T": "Gibeon: 95."
    },
    "26": {
      "L": "The men of Bethlehem and Netophah, one hundred and eighty-eight.",
      "M": "The men of Bethlehem and Netophah: 188.",
      "T": "Bethlehem and Netophah: 188."
    },
    "27": {
      "L": "The men of Anathoth, one hundred and twenty-eight.",
      "M": "The men of Anathoth: 128.",
      "T": "Anathoth: 128."
    },
    "28": {
      "L": "The men of Beth-azmaveth, forty-two.",
      "M": "The men of Beth-azmaveth: 42.",
      "T": "Beth-azmaveth: 42."
    },
    "29": {
      "L": "The men of Kirjath-jearim, Chephirah, and Beeroth, seven hundred and forty-three.",
      "M": "The men of Kiriath-jearim, Chephirah, and Beeroth: 743.",
      "T": "Kiriath-jearim, Chephirah, and Beeroth: 743."
    },
    "30": {
      "L": "The men of Ramah and Geba, six hundred and twenty-one.",
      "M": "The men of Ramah and Geba: 621.",
      "T": "Ramah and Geba: 621."
    },
    "31": {
      "L": "The men of Michmas, one hundred and twenty-two.",
      "M": "The men of Michmas: 122.",
      "T": "Michmas: 122."
    },
    "32": {
      "L": "The men of Bethel and Ai, one hundred and twenty-three.",
      "M": "The men of Bethel and Ai: 123.",
      "T": "Bethel and Ai: 123."
    },
    "33": {
      "L": "The men of the other Nebo, fifty-two.",
      "M": "The men of the other Nebo: 52.",
      "T": "Other Nebo: 52."
    },
    "34": {
      "L": "The children of the other Elam, one thousand two hundred and fifty-four.",
      "M": "The descendants of the other Elam: 1,254.",
      "T": "Other Elam: 1,254."
    },
    "35": {
      "L": "The children of Harim, three hundred and twenty.",
      "M": "The descendants of Harim: 320.",
      "T": "Harim: 320."
    },
    "36": {
      "L": "The children of Jericho, three hundred and forty-five.",
      "M": "The descendants of Jericho: 345.",
      "T": "Jericho: 345."
    },
    "37": {
      "L": "The children of Lod, Hadid, and Ono, seven hundred and twenty-one.",
      "M": "The descendants of Lod, Hadid, and Ono: 721.",
      "T": "Lod, Hadid, and Ono: 721."
    },
    "38": {
      "L": "The children of Senaah, three thousand nine hundred and thirty.",
      "M": "The descendants of Senaah: 3,930.",
      "T": "Senaah: 3,930."
    },
    "39": {
      "L": "The priests: the children of Jedaiah, namely of the house of Jeshua, nine hundred and seventy-three.",
      "M": "The priests: the descendants of Jedaiah, of the house of Jeshua: 973.",
      "T": "Priests — Jedaiah (house of Jeshua): 973."
    },
    "40": {
      "L": "The children of Immer, one thousand and fifty-two.",
      "M": "The descendants of Immer: 1,052.",
      "T": "Immer: 1,052."
    },
    "41": {
      "L": "The children of Pashur, one thousand two hundred and forty-seven.",
      "M": "The descendants of Pashur: 1,247.",
      "T": "Pashur: 1,247."
    },
    "42": {
      "L": "The children of Harim, one thousand and seventeen.",
      "M": "The descendants of Harim: 1,017.",
      "T": "Harim: 1,017."
    },
    "43": {
      "L": "The Levites: the children of Jeshua, namely of Kadmiel and of the children of Hodevah, seventy-four.",
      "M": "The Levites: the descendants of Jeshua, that is of Kadmiel and Hodevah: 74.",
      "T": "Levites — Jeshua, Kadmiel, Hodevah: 74."
    },
    "44": {
      "L": "The singers: the children of Asaph, one hundred and forty-eight.",
      "M": "The singers: the descendants of Asaph: 148.",
      "T": "Singers — Asaph: 148."
    },
    "45": {
      "L": "The gatekeepers: the children of Shallum, the children of Ater, the children of Talmon, the children of Akkub, the children of Hatita, the children of Shobai, one hundred and thirty-eight.",
      "M": "The gatekeepers: the descendants of Shallum, Ater, Talmon, Akkub, Hatita, and Shobai: 138.",
      "T": "Gatekeepers — Shallum, Ater, Talmon, Akkub, Hatita, Shobai: 138."
    },
    "46": {
      "L": "The temple servants: the children of Ziha, the children of Hashupha, the children of Tabbaoth,",
      "M": "The temple servants: the descendants of Ziha, Hashupha, and Tabbaoth,",
      "T": "Temple servants (Nethinim): Ziha, Hashupha, Tabbaoth,"
    },
    "47": {
      "L": "the children of Keros, the children of Sia, the children of Padon,",
      "M": "the descendants of Keros, Sia, and Padon,",
      "T": "Keros, Sia, Padon,"
    },
    "48": {
      "L": "the children of Lebana, the children of Hagaba, the children of Shalmai,",
      "M": "the descendants of Lebana, Hagaba, and Shalmai,",
      "T": "Lebana, Hagaba, Shalmai,"
    },
    "49": {
      "L": "the children of Hanan, the children of Giddel, the children of Gahar,",
      "M": "the descendants of Hanan, Giddel, and Gahar,",
      "T": "Hanan, Giddel, Gahar,"
    },
    "50": {
      "L": "the children of Reaiah, the children of Rezin, the children of Nekoda,",
      "M": "the descendants of Reaiah, Rezin, and Nekoda,",
      "T": "Reaiah, Rezin, Nekoda,"
    },
    "51": {
      "L": "the children of Gazzam, the children of Uzza, the children of Phaseah,",
      "M": "the descendants of Gazzam, Uzza, and Phaseah,",
      "T": "Gazzam, Uzza, Phaseah,"
    },
    "52": {
      "L": "the children of Besai, the children of Meunim, the children of Nephishesim,",
      "M": "the descendants of Besai, Meunim, and Nephishesim,",
      "T": "Besai, Meunim, Nephishesim,"
    },
    "53": {
      "L": "the children of Bakbuk, the children of Hakupha, the children of Harhur,",
      "M": "the descendants of Bakbuk, Hakupha, and Harhur,",
      "T": "Bakbuk, Hakupha, Harhur,"
    },
    "54": {
      "L": "the children of Bazlith, the children of Mehida, the children of Harsha,",
      "M": "the descendants of Bazlith, Mehida, and Harsha,",
      "T": "Bazlith, Mehida, Harsha,"
    },
    "55": {
      "L": "the children of Barkos, the children of Sisera, the children of Tamah,",
      "M": "the descendants of Barkos, Sisera, and Tamah,",
      "T": "Barkos, Sisera, Tamah,"
    },
    "56": {
      "L": "the children of Neziah, the children of Hatipha.",
      "M": "the descendants of Neziah and Hatipha.",
      "T": "Neziah, Hatipha."
    },
    "57": {
      "L": "The children of Solomon's servants: the children of Sotai, the children of Sophereth, the children of Perida,",
      "M": "The descendants of Solomon's servants: the descendants of Sotai, Sophereth, and Perida,",
      "T": "Solomon's servants: Sotai, Sophereth, Perida,"
    },
    "58": {
      "L": "the children of Jaala, the children of Darkon, the children of Giddel,",
      "M": "the descendants of Jaala, Darkon, and Giddel,",
      "T": "Jaala, Darkon, Giddel,"
    },
    "59": {
      "L": "the children of Shephatiah, the children of Hattil, the children of Pochereth-hazzebaim, the children of Amon.",
      "M": "the descendants of Shephatiah, Hattil, Pochereth-hazzebaim, and Amon.",
      "T": "Shephatiah, Hattil, Pochereth-hazzebaim, Amon."
    },
    "60": {
      "L": "All the temple servants and the children of Solomon's servants were three hundred and ninety-two.",
      "M": "All the temple servants and descendants of Solomon's servants totaled 392.",
      "T": "The combined total of all temple servants and Solomon's servants: 392."
    },
    "61": {
      "L": "These were those who came up from Telmelah, Telharesha, Cherub, Addon, and Immer, but they could not prove their fathers' house or their descent, whether they were from Israel:",
      "M": "The following came from Tel-melah, Tel-harsha, Cherub, Addon, and Immer, but they could not establish their family descent or prove their lineage was Israelite:",
      "T": "Some had come from Tel-melah, Tel-harsha, Cherub, Addon, and Immer—Babylonian locations—but they could not produce records demonstrating their Israelite ancestry:"
    },
    "62": {
      "L": "the children of Delaiah, the children of Tobiah, the children of Nekoda, six hundred and forty-two.",
      "M": "the descendants of Delaiah, Tobiah, and Nekoda: 642.",
      "T": "Delaiah, Tobiah, Nekoda: 642—included in the community but with unresolved identity."
    },
    "63": {
      "L": "Also, of the priests: the children of Hobaiah, the children of Hakkoz, the children of Barzillai (who had taken a wife from the daughters of Barzillai the Gileadite and was called by their name).",
      "M": "Among the priests: the descendants of Hobaiah, Hakkoz, and Barzillai—a man who had married a daughter of Barzillai the Gileadite and had taken that family's name.",
      "T": "Among the priests, three families faced the same problem: the descendants of Hobaiah, Hakkoz, and Barzillai. This last case is striking: a priest had married into the Gileadite family of Barzillai and adopted their name, effectively erasing his priestly genealogical identity."
    },
    "64": {
      "L": "These sought their registration among those enrolled in the genealogies, but it was not found there, so they were excluded from the priesthood as unclean.",
      "M": "These searched for their names in the genealogical records but could not find them, so they were disqualified from the priesthood as unclean.",
      "T": "They searched the registers. Their names were not there. And so they were barred from priestly service—not as a permanent punishment, but set aside until the question could be properly resolved. The covenant community's cultic purity required documentation."
    },
    "65": {
      "L": "And the Tirshatha told them that they were not to partake of the most holy food until there should be a priest to consult with the Urim and Thummim.",
      "M": "The governor told them they were not to eat any of the most holy food until a priest appeared who could consult the Urim and Thummim.",
      "T": "The governor—the Tirshatha, Nehemiah's Persian administrative title—ruled: these families could not eat the most sacred priestly foods until a priest arose who could consult the Urim and Thummim and give a definitive answer. The ruling was forward-looking: someone was coming who could resolve what parchment could not."
    },
    "66": {
      "L": "The whole assembly together was forty-two thousand three hundred and sixty,",
      "M": "The whole assembly together numbered 42,360,",
      "T": "The grand total of the whole assembly: 42,360. (When the individual family tallies are added, the sum falls short of this figure—a discrepancy present in the earliest manuscripts and paralleled in Ezra 2. The total appears to include groups not individually broken out in the list.)"
    },
    "67": {
      "L": "besides their male and female servants, of whom there were seven thousand three hundred and thirty-seven. And they had two hundred and forty-five male and female singers.",
      "M": "in addition to their 7,337 male and female servants. They also had 245 male and female singers.",
      "T": "Not counted in the 42,360: 7,337 servants, men and women, and 245 musicians—men and women who sang."
    },
    "68": {
      "L": "Their horses were seven hundred and thirty-six, their mules two hundred and forty-five,",
      "M": "Their horses numbered 736 and their mules 245,",
      "T": "Horses: 736. Mules: 245."
    },
    "69": {
      "L": "their camels four hundred and thirty-five, and their donkeys six thousand seven hundred and twenty.",
      "M": "their camels 435, and their donkeys 6,720.",
      "T": "Camels: 435. Donkeys: 6,720."
    },
    "70": {
      "L": "Now some of the heads of fathers' houses gave to the work. The governor gave to the treasury one thousand drachmas of gold, fifty basins, and five hundred and thirty priests' garments.",
      "M": "Some of the family heads contributed to the work. The governor gave to the treasury 1,000 gold darics, 50 basins, and 530 priestly garments.",
      "T": "The community also gave to fund the rebuilding. The governor's personal contribution: 1,000 gold darics to the treasury, 50 ceremonial basins, 530 priestly garments."
    },
    "71": {
      "L": "And some of the heads of fathers' houses gave into the treasury of the work twenty thousand gold drachmas and two thousand two hundred minas of silver.",
      "M": "Some family heads gave to the treasury 20,000 gold darics and 2,200 minas of silver.",
      "T": "The heads of the ancestral houses gave: 20,000 gold darics and 2,200 minas of silver to the work treasury."
    },
    "72": {
      "L": "And what the rest of the people gave was twenty thousand drachmas of gold, and two thousand minas of silver, and sixty-seven priests' garments.",
      "M": "The rest of the people gave 20,000 gold darics, 2,000 minas of silver, and 67 priestly garments.",
      "T": "The broader community gave: 20,000 gold darics, 2,000 minas of silver, and 67 priestly garments."
    },
    "73": {
      "L": "So the priests, the Levites, the gatekeepers, the singers, some of the people, the temple servants, and all Israel settled in their towns. And when the seventh month came, the people of Israel were in their towns.",
      "M": "So the priests, the Levites, the gatekeepers, the singers, some of the people, the temple servants, and all Israel settled in their towns. When the seventh month came, the Israelites were all in their towns.",
      "T": "Priests, Levites, gatekeepers, singers, temple servants, and all Israel settled back into the towns the register had named. Then the seventh month arrived—and with it, the pivot of the story that follows."
    }
  },
  "8": {
    "1": {
      "L": "And all the people gathered as one man into the square before the Water Gate. And they told Ezra the scribe to bring the Book of the Law of Moses that the LORD had commanded Israel.",
      "M": "All the people came together as one in the square in front of the Water Gate. They asked Ezra the scribe to bring the Book of the Law of Moses, which the LORD had commanded for Israel.",
      "T": "On the first day of the seventh month, all the people gathered as one in the open square before the Water Gate. They made a collective demand: 'Bring the book.' They called for Ezra the scribe to bring out the Torah of Moses—the law the LORD had commanded Israel to live by."
    },
    "2": {
      "L": "So Ezra the priest brought the Law before the assembly, both men and women and all who could understand what they heard, on the first day of the seventh month.",
      "M": "Ezra the priest brought the Law before the assembly—men, women, and all who were old enough to understand—on the first day of the seventh month.",
      "T": "Ezra the priest brought out the Torah on the first day of the seventh month—the feast-day that opens the Days of Awe—and stood before the whole assembly: men, women, and all who were old enough to comprehend."
    },
    "3": {
      "L": "He read from it facing the square before the Water Gate from early morning until midday, in the presence of the men and the women and those who could understand. And the ears of all the people were attentive to the Book of the Law.",
      "M": "He read from it in the square before the Water Gate from early morning until noon, in the presence of men, women, and those who could understand. All the people listened attentively to the Book of the Law.",
      "T": "He read from it facing the square before the Water Gate—from first light until noon—in the presence of men, women, and all who could understand. For hours the people stood and listened. Their ears were fixed on every word."
    },
    "4": {
      "L": "And Ezra the scribe stood on a wooden platform that they had made for the purpose. And beside him stood Mattithiah, Shema, Anaiah, Uriah, Hilkiah, and Maaseiah on his right hand, and Pedaiah, Mishael, Malchijah, Hashum, Hashbaddanah, Zechariah, and Meshullam on his left hand.",
      "M": "Ezra the scribe stood on a wooden platform that had been built for the occasion. Beside him on his right stood Mattithiah, Shema, Anaiah, Uriah, Hilkiah, and Maaseiah; on his left stood Pedaiah, Mishael, Malchijah, Hashum, Hashbaddanah, Zechariah, and Meshullam.",
      "T": "Ezra stood on a wooden platform—a raised pulpit built specifically for this reading. At his right hand: Mattithiah, Shema, Anaiah, Uriah, Hilkiah, and Maaseiah. At his left: Pedaiah, Mishael, Malchijah, Hashum, Hashbaddanah, Zechariah, and Meshullam. Thirteen men flanked the text on a platform above the crowd."
    },
    "5": {
      "L": "And Ezra opened the book in the sight of all the people, for he was above all the people, and as he opened it all the people stood.",
      "M": "Ezra opened the book in full view of all the people. He was standing above them, and when he opened it, everyone stood up.",
      "T": "Ezra opened the scroll where all could see him—he was elevated above the crowd. When he opened it, the entire assembly rose to their feet. The standing was an act of honor given to the Word."
    },
    "6": {
      "L": "And Ezra blessed the LORD, the great God, and all the people answered, 'Amen, Amen,' lifting up their hands. And they bowed their heads and worshiped the LORD with their faces to the ground.",
      "M": "Ezra praised the LORD, the great God, and all the people responded, 'Amen! Amen!' as they lifted their hands. Then they bowed down and worshiped the LORD with their faces to the ground.",
      "T": "'Blessed be the LORD, the great God!' Ezra called out. 'Amen! Amen!' the people answered, lifting their hands toward heaven. Then they bowed low—faces to the ground before the LORD. The response was total: voice, hands, and body."
    },
    "7": {
      "L": "Also Jeshua, Bani, Sherebiah, Jamin, Akkub, Shabbethai, Hodijah, Maaseiah, Kelita, Azariah, Jozabad, Hanan, Pelaiah, the Levites, helped the people understand the Law, while the people remained in their places.",
      "M": "Jeshua, Bani, Sherebiah, Jamin, Akkub, Shabbethai, Hodijah, Maaseiah, Kelita, Azariah, Jozabad, Hanan, and Pelaiah—the Levites—helped the people understand the Law, while the people remained standing in their places.",
      "T": "Thirteen Levites—Jeshua, Bani, Sherebiah, Jamin, Akkub, Shabbethai, Hodijah, Maaseiah, Kelita, Azariah, Jozabad, Hanan, and Pelaiah—moved through the crowd explaining the Law to those who remained standing in their positions. The reading came from the platform; the teaching went into the crowd."
    },
    "8": {
      "L": "They read from the book, from the Law of God, clearly, and they gave the sense, so that the people understood the reading.",
      "M": "They read from the Book of the Law of God, explaining it clearly and giving the meaning, so that the people understood what was being read.",
      "T": "They read from the book—the Law of God—clearly and distinctly, and they gave interpretation alongside the reading, so that people could grasp what they were hearing. This is the earliest biblical glimpse of what later became the Targum tradition: Torah read in Hebrew, explained in the vernacular, so the covenant could be received and not merely recited."
    },
    "9": {
      "L": "And Nehemiah, who was the governor, and Ezra the priest and scribe, and the Levites who taught the people said to all the people, 'This day is holy to the LORD your God; do not mourn or weep.' For all the people wept as they heard the words of the Law.",
      "M": "Nehemiah the governor, Ezra the priest and scribe, and the Levites who were instructing the people said to everyone, 'This day is holy to the LORD your God. Do not mourn or weep.' For all the people had been weeping as they heard the words of the Law.",
      "T": "Nehemiah the governor, Ezra the priest and scribe, and the teaching Levites had to address the assembly: 'This day is holy to the LORD your God—do not mourn; do not weep.' They had to say it because the whole crowd was weeping. The Law had landed with its full weight on a people who had lived without it."
    },
    "10": {
      "L": "Then he said to them, 'Go your way. Eat the fat and drink sweet wine and send portions to anyone who has nothing ready, for this day is holy to our Lord. And do not be grieved, for the joy of the LORD is your strength.'",
      "M": "He continued, 'Go and enjoy choice food and sweet drinks, and send some to those who have nothing prepared. This day is holy to our Lord. Do not grieve, for the joy of the LORD is your strength.'",
      "T": "'Go and eat rich food,' he told them. 'Drink something sweet. Send portions to people who have nothing prepared—because this day is holy to our Lord. Do not let grief take hold of you. The joy of the LORD is your stronghold.' The word is maoz—fortress, fortified refuge. The LORD's own gladness over his restored people is a wall of defense around them."
    },
    "11": {
      "L": "So the Levites calmed all the people, saying, 'Be quiet, for this day is holy; do not be grieved.'",
      "M": "The Levites quieted all the people, saying, 'Hush! This day is holy. Do not grieve.'",
      "T": "The Levites moved through the crowd quieting people: 'Still. Be still. This day is holy. Grief is not what this day asks of you.'"
    },
    "12": {
      "L": "And all the people went their way to eat and drink and to send portions and to make great rejoicing, because they had understood the words that were declared to them.",
      "M": "Then all the people went away to eat and drink and to share food and to celebrate with great joy, because they now understood the words that had been explained to them.",
      "T": "With that, the assembly dispersed—to eat and drink, to send food to neighbors, to celebrate with genuine joy. The weeping had become gladness. The cause of both was the same: they understood the words."
    },
    "13": {
      "L": "On the second day the heads of fathers' houses of all the people, with the priests and the Levites, came together to Ezra the scribe in order to study the words of the Law.",
      "M": "On the second day, the heads of all the families came together with the priests and the Levites to study the words of the Law with Ezra the scribe.",
      "T": "The next day the community's leaders—heads of families, priests, and Levites—gathered around Ezra to go deeper. Yesterday's reading was for the whole people; today's study was for those responsible for transmitting the Torah."
    },
    "14": {
      "L": "And they found it written in the Law that the LORD had commanded by Moses that the people of Israel should dwell in booths during the feast of the seventh month,",
      "M": "They found written in the Law—which the LORD had commanded through Moses—that the Israelites were to live in shelters during the feast of the seventh month,",
      "T": "In the text they found the command: the LORD had charged Moses that Israel was to dwell in booths during the feast of the seventh month—"
    },
    "15": {
      "L": "and that they should proclaim it and publish this word in all their cities and in Jerusalem: 'Go out to the hills and bring branches of olive, wild olive, myrtle, palm, and other leafy trees to make booths, as it is written.'",
      "M": "and that they should proclaim and publish this word in all their towns and in Jerusalem: 'Go out to the hill country and bring back branches of olive, wild olive, myrtle, palm, and other leafy trees to make shelters, as it is written.'",
      "T": "—and that they were to announce it everywhere, in all the towns and throughout Jerusalem: 'Go out to the hills! Bring back olive branches, wild olive, myrtle, palm, and thick leafy boughs—and build shelters, just as the written text commands.' So they did."
    },
    "16": {
      "L": "So the people went out and brought them and made booths for themselves, each on his roof, and in their courts and in the courts of the house of God, and in the square at the Water Gate and in the square at the Gate of Ephraim.",
      "M": "So the people went out and brought leafy branches and built shelters for themselves—on their rooftops, in their courtyards, in the courts of the house of God, in the square by the Water Gate, and in the square by the Gate of Ephraim.",
      "T": "The people went out and came back with branches. Shelters rose everywhere: on the flat rooftops, in private courtyards, in the temple courts, in the open square before the Water Gate, and in the square at the Gate of Ephraim. The whole city became a wilderness camp, as Israel had been in the days of the wandering."
    },
    "17": {
      "L": "And all the assembly of those who had returned from the captivity made booths and lived in the booths, for from the days of Jeshua the son of Nun to that day the people of Israel had not done so. And there was very great gladness.",
      "M": "The whole assembly of those who had returned from exile built shelters and lived in them. From the days of Joshua son of Nun until that day, the Israelites had not celebrated this way. And there was very great joy.",
      "T": "Every member of the assembly—everyone who had returned from exile—built a shelter and lived in it for the feast. Nothing like it had been seen since the days of Joshua son of Nun. Not that Sukkot had never been observed in the intervening centuries, but this celebration—all the returned exiles together, in the rebuilt city, with the Law read aloud every day—was unprecedented in completeness and scale. The gladness was immense."
    },
    "18": {
      "L": "And day by day, from the first day to the last day, he read from the Book of the Law of God. They kept the feast seven days, and on the eighth day there was a solemn assembly, according to the rule.",
      "M": "Day by day, from the first day to the last, Ezra read from the Book of the Law of God. They observed the feast for seven days, and on the eighth day there was a solemn assembly, according to the ordinance.",
      "T": "Every single day, from the first through the seventh, Ezra read aloud from the Book of God's Law. Seven days of feasting in booths; seven days of Torah given to the whole people. On the eighth day—as Numbers 29:35 and the Mosaic ordinance required—there was a solemn assembly. The covenant had been renewed in word and in deed."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'nehemiah')
        merge_tier(existing, NEHEMIAH, tier_key)
        save(tier_dir, 'nehemiah', existing)
    print('Nehemiah 7–8 written.')

if __name__ == '__main__':
    main()
