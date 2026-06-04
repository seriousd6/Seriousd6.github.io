"""
MKT Ezra chapters 1–2 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-ezra-1-2.py

Content:
- Ch 1: Cyrus's decree and its theological framing — fulfillment of Jeremiah's prophecy,
        the LORD's stirring of Cyrus's spirit, the proclamation to return and rebuild,
        Israel's neighbors assisting, and the temple vessels restored from Nebuchadnezzar's
        plunder.
- Ch 2: The return register — a census of 42,360 returnees plus 7,337 servants, organized
        by lay family, priestly family, Levites, singers, gatekeepers, Nethinim, and
        Solomon's servants; those of uncertain lineage; and a closing account of freewill
        offerings.

Translation decisions:
- H3068 (יהוה): "LORD" in L/M; "the LORD" in T. Consistent with all prior OT scripts.
- H430 (אֱלֹהִים): "God" throughout all tiers.
- H7307 (רוּחַ): In 1:1 and 1:5, human spirit (Cyrus's spirit, the returnees' spirit)
  stirred by the LORD — rendered "spirit" (lowercase) throughout. No Holy Spirit
  theology is in view; the word denotes an animating inner disposition.
- H2617 (חֶסֶד): Does not occur in these chapters.
- H1285 (בְּרִית): Does not occur in these chapters.
- H1473 (גּוֹלָה = exile/captivity): "exiles" (noun) or "captivity" (state). In 1:11
  and 2:1 it refers to the exiled community as a group — rendered "exiles" in all tiers.
- H1540 (גָּלָה = carry captive): "carried away captive" in L; "taken into exile" or
  "carried captive" in M; T renders the theological weight — "carried off to Babylon."
- H5782 (עוּר = stir up, arouse): "stirred up" in L/M; T uses "moved upon" (1:1, the
  pagan king) and "aroused within" (1:5, Israel's own leaders) to distinguish the two
  acts — external providence on Cyrus, internal divine call on the returnees.
- H5411 (נְתִינִים = Nethinim/temple servants): "Nethinim" in L (proper title);
  "temple servants" in M; T: "Nethinim, the temple bondsmen" — likely descended from
  the Gibeonites formally assigned to sanctuary labor (Josh 9; 1 Chr 9:2).
- H8660 (תִּרְשָׁתָא = Tirshatha, Persian governor title): "the Tirshatha" in L
  (transliterating the official Persian/Aramaic title); "the governor" in M and T.
- H224/H8550 (Urim/Thummim): transliterated in all tiers; T adds that these are the
  priestly oracle objects for determining divine will, not human adjudication.
- H1871 (דַּרְכְּמוֹן = daric, a Persian gold coin): "darics" in L/M; T: "darics
  (gold coins)" on first use only.
- H1121 (בֵּן = son/descendant) in genealogical lists: L renders "sons of" (literal
  kinship word); M uses "descendants of" for family-group registers; T uses "the clan
  of" (lay families) or "the priestly family of" (sacerdotal lists) to convey that
  these are extended kinship groups, not immediate children.
- Chapter 2 genealogy: The repeated register form (בְּנֵי X + number) is a sēper
  census entry. T reads these lists as covenant-community boundary documentation —
  who belongs to restored Israel is a theological claim, not merely headcount.
- Aspect notes:
  - 1:1: Waw-consecutive imperfect chain (wayyā'er, wayyōṣeʾ, wayyiktōb) narrates
    the cascade of events. The opening infinitive le-kallōt ("to fulfill") frames the
    whole sequence as providentially ordered before it begins.
  - 1:3: The jussive yaʿal ("let him go up") is permissive — Cyrus authorizes; he
    does not command. The initiative belongs to those whose spirit is stirred.
  - 1:5: The verb hēʿîr ("stirred up") is the exact root as 1:1 — the parallelism
    is intentional: the same divine action that moved Cyrus now moves Israel.
  - 2:62: The niphal wayyiggoʾălû ("they were excluded") is passive — the purity
    system removed them; they did not self-exclude.
  - 2:68-69: The verb nādab (H5068, "offered freely") matches Exod 25:2 for the
    tabernacle freewill gifts — the return community re-enacts the wilderness community.
- OT intertextuality:
  - 1:1: Jer 25:12; 29:10 (seventy-year prophecy fulfilled); Isa 44:28; 45:1,13
    (Cyrus named ~150 years before his reign).
  - 1:5: Exod 35:21 ("everyone whose heart stirred him up" — same formula for
    tabernacle contributions); the stirring of spirit becomes a covenant signature.
  - 1:7: 2 Kgs 25:14-15; 2 Chr 36:7,18 — Nebuchadnezzar's original seizure of
    the vessels; their return is the material reversal of the exile.
  - 2:63: Num 27:21; 1 Sam 14:41 — Urim employed for divine adjudication where
    human evidence is insufficient.
  - 2:68-69: Exod 25:2,8 — tabernacle freewill pattern; the returnees' offerings
    evoke the wilderness generation building the first sanctuary.
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
  "1": {
    "1": {
      "L": "In the first year of Cyrus king of Persia, to fulfill the word of LORD by the mouth of Jeremiah, the LORD stirred up the spirit of Cyrus king of Persia, and he caused a proclamation to pass through all his kingdom, and also in writing, saying:",
      "M": "In the first year of Cyrus king of Persia, so that the word of the LORD spoken through Jeremiah might be fulfilled, the LORD stirred up the spirit of Cyrus king of Persia to make a proclamation throughout all his kingdom and to put it in writing:",
      "T": "In the very first year of Cyrus king of Persia, what the LORD had spoken through Jeremiah came to pass: the LORD moved upon the spirit of Cyrus—a pagan king—who then sent a written decree throughout his entire empire:"
    },
    "2": {
      "L": "Thus says Cyrus king of Persia: All the kingdoms of the earth the LORD the God of heaven has given to me, and he has appointed me to build him a house at Jerusalem which is in Judah.",
      "M": "Thus says Cyrus king of Persia: 'The LORD, the God of heaven, has given me all the kingdoms of the earth, and he has appointed me to build him a house at Jerusalem, which is in Judah.'",
      "T": "This is the declaration of Cyrus king of Persia: 'The LORD—the God of heaven—has given me dominion over all the kingdoms of the earth, and he himself has commissioned me to build his house at Jerusalem in Judah.'"
    },
    "3": {
      "L": "Whoever is among you of all his people, may his God be with him, and let him go up to Jerusalem which is in Judah, and build the house of LORD the God of Israel—he is the God who is in Jerusalem.",
      "M": "Whoever is among you of all his people, may his God be with him, and let him go up to Jerusalem, which is in Judah, and rebuild the house of the LORD, the God of Israel—he is the God who is in Jerusalem.",
      "T": "Let any of his people who is willing go—may their God go with them—and travel up to Jerusalem in Judah to rebuild the house of the LORD, the God of Israel. He is the God who dwells in Jerusalem."
    },
    "4": {
      "L": "And everyone who remains in any place where he sojourns, let the men of his place help him with silver and with gold and with goods and with beasts, besides the freewill offering for the house of God which is in Jerusalem.",
      "M": "And let every survivor, wherever he sojourns, be assisted by the people of his place with silver and gold, with goods and livestock, besides freewill offerings for the house of God in Jerusalem.",
      "T": "Wherever a returning Israelite is now living among neighbors, those neighbors are to support him with silver, gold, supplies, and animals—and beyond that, with voluntary offerings for the house of God in Jerusalem."
    },
    "5": {
      "L": "Then rose up the heads of the fathers of Judah and Benjamin, and the priests and the Levites, everyone whose spirit God stirred up, to go up to build the house of LORD which is in Jerusalem.",
      "M": "Then the heads of the fathers' houses of Judah and Benjamin, the priests and the Levites—everyone whose spirit God had stirred up—arose to go up and build the house of the LORD in Jerusalem.",
      "T": "The same divine stirring that had moved Cyrus now worked within Israel: the clan leaders of Judah and Benjamin, the priests, and the Levites—all whose spirits God aroused from within—rose as one to go up and build the LORD's house in Jerusalem."
    },
    "6": {
      "L": "And all who were around them strengthened their hands with vessels of silver, with gold, with goods, and with beasts, and with precious things, besides all that was willingly offered.",
      "M": "All their neighbors aided them with silver vessels and gold, with goods, livestock, and costly gifts, besides everything that was freely offered.",
      "T": "Their neighbors on every side poured resources into their hands—silver vessels, gold, supplies, animals, and fine goods—over and above all that was given as a freewill offering."
    },
    "7": {
      "L": "And Cyrus the king brought out the vessels of the house of LORD that Nebuchadnezzar had brought out from Jerusalem and put in the house of his gods.",
      "M": "King Cyrus also brought out the vessels of the house of the LORD that Nebuchadnezzar had removed from Jerusalem and placed in the temple of his gods.",
      "T": "Cyrus also returned the sacred vessels of the LORD's house—the very objects Nebuchadnezzar had looted from Jerusalem and installed as war trophies in his own gods' temple."
    },
    "8": {
      "L": "Cyrus king of Persia brought them forth by the hand of Mithredath the treasurer, and he counted them out to Sheshbazzar the prince of Judah.",
      "M": "Cyrus king of Persia brought them out through Mithredath the treasurer, who counted them into the custody of Sheshbazzar the prince of Judah.",
      "T": "Cyrus formally transferred them through his treasurer Mithredath, who made a careful count and handed them over to Sheshbazzar, the designated prince of Judah."
    },
    "9": {
      "L": "And this is their number: thirty basins of gold, a thousand basins of silver, nine and twenty knives,",
      "M": "And this was their number: thirty gold basins, a thousand silver basins, twenty-nine knives,",
      "T": "The inventory read: thirty gold basins, one thousand silver basins, twenty-nine knives,"
    },
    "10": {
      "L": "thirty bowls of gold, silver bowls of a second sort four hundred and ten, and other vessels a thousand.",
      "M": "thirty gold bowls, four hundred and ten silver bowls of a second grade, and a thousand other vessels;",
      "T": "thirty gold bowls, four hundred and ten secondary-grade silver bowls, and a thousand assorted vessels;"
    },
    "11": {
      "L": "All the vessels of gold and of silver were five thousand four hundred. All these did Sheshbazzar bring up when the exiles were brought up from Babylon to Jerusalem.",
      "M": "the total of all vessels of gold and silver was five thousand four hundred. Sheshbazzar brought them all up when the exiles came up from Babylon to Jerusalem.",
      "T": "five thousand four hundred vessels in gold and silver altogether. Sheshbazzar carried them all back when the exiles made the journey from Babylon to Jerusalem—the holy objects reclaimed, the exile visibly reversing."
    }
  },
  "2": {
    "1": {
      "L": "Now these are the children of the province who went up out of the captivity of the exiles whom Nebuchadnezzar king of Babylon had carried away captive to Babylon, and who returned to Jerusalem and Judah, each to his own city.",
      "M": "Now these are the people of the province who came up out of the captivity—those whom Nebuchadnezzar king of Babylon had carried into exile in Babylon. They returned to Jerusalem and Judah, each to his own town.",
      "T": "These are the names of those in the province who came home from exile—the people Nebuchadnezzar king of Babylon had taken captive to Babylon. Now they were returning to Jerusalem and Judah, each one reclaiming his own ancestral town."
    },
    "2": {
      "L": "Who came with Zerubbabel: Jeshua, Nehemiah, Seraiah, Reelaiah, Mordecai, Bilshan, Mispar, Bigvai, Rehum, Baanah. The number of the men of the people of Israel:",
      "M": "They came with Zerubbabel, Jeshua, Nehemiah, Seraiah, Reelaiah, Mordecai, Bilshan, Mispar, Bigvai, Rehum, and Baanah. The number of the men of the people of Israel:",
      "T": "Leading them were Zerubbabel, Jeshua, Nehemiah, Seraiah, Reelaiah, Mordecai, Bilshan, Mispar, Bigvai, Rehum, and Baanah. The register of Israel's returning families follows:"
    },
    "3": {
      "L": "The sons of Parosh, two thousand one hundred and seventy-two.",
      "M": "The descendants of Parosh: two thousand one hundred and seventy-two.",
      "T": "The clan of Parosh: 2,172."
    },
    "4": {
      "L": "The sons of Shephatiah, three hundred and seventy-two.",
      "M": "The descendants of Shephatiah: three hundred and seventy-two.",
      "T": "The clan of Shephatiah: 372."
    },
    "5": {
      "L": "The sons of Arah, seven hundred and seventy-five.",
      "M": "The descendants of Arah: seven hundred and seventy-five.",
      "T": "The clan of Arah: 775."
    },
    "6": {
      "L": "The sons of Pahath-moab, of the sons of Jeshua and Joab, two thousand eight hundred and twelve.",
      "M": "The descendants of Pahath-moab, through the clans of Jeshua and Joab: two thousand eight hundred and twelve.",
      "T": "The clan of Pahath-moab, counting both the Jeshua and Joab branches: 2,812."
    },
    "7": {
      "L": "The sons of Elam, one thousand two hundred and fifty-four.",
      "M": "The descendants of Elam: one thousand two hundred and fifty-four.",
      "T": "The clan of Elam: 1,254."
    },
    "8": {
      "L": "The sons of Zattu, nine hundred and forty-five.",
      "M": "The descendants of Zattu: nine hundred and forty-five.",
      "T": "The clan of Zattu: 945."
    },
    "9": {
      "L": "The sons of Zaccai, seven hundred and sixty.",
      "M": "The descendants of Zaccai: seven hundred and sixty.",
      "T": "The clan of Zaccai: 760."
    },
    "10": {
      "L": "The sons of Bani, six hundred and forty-two.",
      "M": "The descendants of Bani: six hundred and forty-two.",
      "T": "The clan of Bani: 642."
    },
    "11": {
      "L": "The sons of Bebai, six hundred and twenty-three.",
      "M": "The descendants of Bebai: six hundred and twenty-three.",
      "T": "The clan of Bebai: 623."
    },
    "12": {
      "L": "The sons of Azgad, one thousand two hundred and twenty-two.",
      "M": "The descendants of Azgad: one thousand two hundred and twenty-two.",
      "T": "The clan of Azgad: 1,222."
    },
    "13": {
      "L": "The sons of Adonikam, six hundred and sixty-six.",
      "M": "The descendants of Adonikam: six hundred and sixty-six.",
      "T": "The clan of Adonikam: 666."
    },
    "14": {
      "L": "The sons of Bigvai, two thousand and fifty-six.",
      "M": "The descendants of Bigvai: two thousand and fifty-six.",
      "T": "The clan of Bigvai: 2,056."
    },
    "15": {
      "L": "The sons of Adin, four hundred and fifty-four.",
      "M": "The descendants of Adin: four hundred and fifty-four.",
      "T": "The clan of Adin: 454."
    },
    "16": {
      "L": "The sons of Ater, of Hezekiah, ninety-eight.",
      "M": "The descendants of Ater through Hezekiah: ninety-eight.",
      "T": "The clan of Ater, the Hezekiah branch: 98."
    },
    "17": {
      "L": "The sons of Bezai, three hundred and twenty-three.",
      "M": "The descendants of Bezai: three hundred and twenty-three.",
      "T": "The clan of Bezai: 323."
    },
    "18": {
      "L": "The sons of Jorah, one hundred and twelve.",
      "M": "The descendants of Jorah: one hundred and twelve.",
      "T": "The clan of Jorah: 112."
    },
    "19": {
      "L": "The sons of Hashum, two hundred and twenty-three.",
      "M": "The descendants of Hashum: two hundred and twenty-three.",
      "T": "The clan of Hashum: 223."
    },
    "20": {
      "L": "The sons of Gibbar, ninety-five.",
      "M": "The descendants of Gibbar: ninety-five.",
      "T": "The clan of Gibbar: 95."
    },
    "21": {
      "L": "The sons of Bethlehem, one hundred and twenty-three.",
      "M": "The men of Bethlehem: one hundred and twenty-three.",
      "T": "The town of Bethlehem: 123."
    },
    "22": {
      "L": "The men of Netophah, fifty-six.",
      "M": "The men of Netophah: fifty-six.",
      "T": "The town of Netophah: 56."
    },
    "23": {
      "L": "The men of Anathoth, one hundred and twenty-eight.",
      "M": "The men of Anathoth: one hundred and twenty-eight.",
      "T": "The town of Anathoth—Jeremiah's own birthplace—returning home: 128."
    },
    "24": {
      "L": "The sons of Azmaveth, forty-two.",
      "M": "The descendants of Azmaveth: forty-two.",
      "T": "The clan of Azmaveth: 42."
    },
    "25": {
      "L": "The sons of Kiriath-arim, Chephirah, and Beeroth, seven hundred and forty-three.",
      "M": "The men of Kiriath-arim, Chephirah, and Beeroth: seven hundred and forty-three.",
      "T": "The towns of Kiriath-arim, Chephirah, and Beeroth—the old Gibeonite territory—counted together: 743."
    },
    "26": {
      "L": "The sons of Ramah and Geba, six hundred and twenty-one.",
      "M": "The men of Ramah and Geba: six hundred and twenty-one.",
      "T": "The towns of Ramah and Geba: 621."
    },
    "27": {
      "L": "The men of Michmas, one hundred and twenty-two.",
      "M": "The men of Michmas: one hundred and twenty-two.",
      "T": "The town of Michmas: 122."
    },
    "28": {
      "L": "The men of Bethel and Ai, two hundred and twenty-three.",
      "M": "The men of Bethel and Ai: two hundred and twenty-three.",
      "T": "The towns of Bethel and Ai: 223."
    },
    "29": {
      "L": "The sons of Nebo, fifty-two.",
      "M": "The descendants of Nebo: fifty-two.",
      "T": "The clan of Nebo: 52."
    },
    "30": {
      "L": "The sons of Magbish, one hundred and fifty-six.",
      "M": "The descendants of Magbish: one hundred and fifty-six.",
      "T": "The clan of Magbish: 156."
    },
    "31": {
      "L": "The sons of the other Elam, one thousand two hundred and fifty-four.",
      "M": "The descendants of the other Elam: one thousand two hundred and fifty-four.",
      "T": "The second clan of Elam: 1,254."
    },
    "32": {
      "L": "The sons of Harim, three hundred and twenty.",
      "M": "The descendants of Harim: three hundred and twenty.",
      "T": "The clan of Harim: 320."
    },
    "33": {
      "L": "The sons of Lod, Hadid, and Ono, seven hundred and twenty-five.",
      "M": "The men of Lod, Hadid, and Ono: seven hundred and twenty-five.",
      "T": "The towns of Lod, Hadid, and Ono: 725."
    },
    "34": {
      "L": "The sons of Jericho, three hundred and forty-five.",
      "M": "The men of Jericho: three hundred and forty-five.",
      "T": "The town of Jericho: 345."
    },
    "35": {
      "L": "The sons of Senaah, three thousand six hundred and thirty.",
      "M": "The descendants of Senaah: three thousand six hundred and thirty.",
      "T": "The clan of Senaah—the largest single entry in the lay register: 3,630."
    },
    "36": {
      "L": "The priests: the sons of Jedaiah, of the house of Jeshua, nine hundred and seventy-three.",
      "M": "The priests: the descendants of Jedaiah, of the house of Jeshua, nine hundred and seventy-three.",
      "T": "The priestly families begin here. The descendants of Jedaiah, through the high-priestly house of Jeshua: 973."
    },
    "37": {
      "L": "The sons of Immer, one thousand and fifty-two.",
      "M": "The descendants of Immer: one thousand and fifty-two.",
      "T": "The priestly family of Immer: 1,052."
    },
    "38": {
      "L": "The sons of Pashhur, one thousand two hundred and forty-seven.",
      "M": "The descendants of Pashhur: one thousand two hundred and forty-seven.",
      "T": "The priestly family of Pashhur: 1,247."
    },
    "39": {
      "L": "The sons of Harim, one thousand and seventeen.",
      "M": "The descendants of Harim: one thousand and seventeen.",
      "T": "The priestly family of Harim: 1,017."
    },
    "40": {
      "L": "The Levites: the sons of Jeshua and Kadmiel, of the sons of Hodaviah, seventy-four.",
      "M": "The Levites: the descendants of Jeshua and Kadmiel, through the line of Hodaviah, seventy-four.",
      "T": "The Levites—notably few, and their scarcity will be a recurring problem in the restoration: descendants of Jeshua and Kadmiel through Hodaviah's line, only seventy-four."
    },
    "41": {
      "L": "The singers: the sons of Asaph, one hundred and twenty-eight.",
      "M": "The singers: the descendants of Asaph, one hundred and twenty-eight.",
      "T": "The temple singers, descendants of David's choir-master Asaph: 128."
    },
    "42": {
      "L": "The sons of the gatekeepers: the sons of Shallum, the sons of Ater, the sons of Talmon, the sons of Akkub, the sons of Hatita, the sons of Shobai, in all one hundred and thirty-nine.",
      "M": "The gatekeepers: the descendants of Shallum, Ater, Talmon, Akkub, Hatita, and Shobai—in all, one hundred and thirty-nine.",
      "T": "The gatekeepers—guardians of the sanctuary's threshold—six families returning: Shallum, Ater, Talmon, Akkub, Hatita, and Shobai. Total: 139."
    },
    "43": {
      "L": "The Nethinim: the sons of Ziha, the sons of Hasupha, the sons of Tabbaoth,",
      "M": "The temple servants: the descendants of Ziha, Hasupha, and Tabbaoth,",
      "T": "The Nethinim—temple bondsmen committed to Levitical support, likely heirs of the Gibeonites assigned by David—came in many family groups: Ziha, Hasupha, and Tabbaoth;"
    },
    "44": {
      "L": "the sons of Keros, the sons of Siaha, the sons of Padon,",
      "M": "the descendants of Keros, Siaha, and Padon,",
      "T": "Keros, Siaha, and Padon;"
    },
    "45": {
      "L": "the sons of Lebanah, the sons of Hagabah, the sons of Akkub,",
      "M": "the descendants of Lebanah, Hagabah, and Akkub,",
      "T": "Lebanah, Hagabah, and Akkub;"
    },
    "46": {
      "L": "the sons of Hagab, the sons of Shalmai, the sons of Hanan,",
      "M": "the descendants of Hagab, Shalmai, and Hanan,",
      "T": "Hagab, Shalmai, and Hanan;"
    },
    "47": {
      "L": "the sons of Giddel, the sons of Gahar, the sons of Reaiah,",
      "M": "the descendants of Giddel, Gahar, and Reaiah,",
      "T": "Giddel, Gahar, and Reaiah;"
    },
    "48": {
      "L": "the sons of Rezin, the sons of Nekoda, the sons of Gazzam,",
      "M": "the descendants of Rezin, Nekoda, and Gazzam,",
      "T": "Rezin, Nekoda, and Gazzam;"
    },
    "49": {
      "L": "the sons of Uzza, the sons of Paseah, the sons of Besai,",
      "M": "the descendants of Uzza, Paseah, and Besai,",
      "T": "Uzza, Paseah, and Besai;"
    },
    "50": {
      "L": "the sons of Asnah, the sons of Meunim, the sons of Nephisim,",
      "M": "the descendants of Asnah, Meunim, and Nephisim,",
      "T": "Asnah, Meunim, and Nephisim;"
    },
    "51": {
      "L": "the sons of Bakbuk, the sons of Hakupha, the sons of Harhur,",
      "M": "the descendants of Bakbuk, Hakupha, and Harhur,",
      "T": "Bakbuk, Hakupha, and Harhur;"
    },
    "52": {
      "L": "the sons of Bazluth, the sons of Mehida, the sons of Harsha,",
      "M": "the descendants of Bazluth, Mehida, and Harsha,",
      "T": "Bazluth, Mehida, and Harsha;"
    },
    "53": {
      "L": "the sons of Barkos, the sons of Sisera, the sons of Thamah,",
      "M": "the descendants of Barkos, Sisera, and Thamah,",
      "T": "Barkos, Sisera, and Thamah;"
    },
    "54": {
      "L": "the sons of Neziah, and the sons of Hatipha.",
      "M": "and the descendants of Neziah and Hatipha.",
      "T": "and Neziah and Hatipha—thirty-five Nethinim families in all, embedded in the restoration community."
    },
    "55": {
      "L": "The sons of Solomon's servants: the sons of Sotai, the sons of Sophereth, the sons of Peruda,",
      "M": "The descendants of Solomon's servants: the families of Sotai, Sophereth, and Peruda,",
      "T": "The descendants of Solomon's royal servants—another hereditary service class, distinct from the Nethinim—began with Sotai, Sophereth, and Peruda;"
    },
    "56": {
      "L": "the sons of Jaalah, the sons of Darkon, the sons of Giddel,",
      "M": "the descendants of Jaalah, Darkon, and Giddel,",
      "T": "Jaalah, Darkon, and Giddel;"
    },
    "57": {
      "L": "the sons of Shephatiah, the sons of Hattil, the sons of Pochereth-hazzebaim, and the sons of Ami.",
      "M": "the descendants of Shephatiah, Hattil, Pochereth-hazzebaim, and Ami.",
      "T": "and Shephatiah, Hattil, Pochereth-hazzebaim, and Ami."
    },
    "58": {
      "L": "All the Nethinim and the sons of Solomon's servants were three hundred and ninety-two.",
      "M": "All the temple servants and the descendants of Solomon's servants totaled three hundred and ninety-two.",
      "T": "Nethinim and Solomonic servants together: 392—the temple's inherited support personnel, preserving their identity through the exile."
    },
    "59": {
      "L": "And these were they who went up from Tel-melah, Tel-harsha, Cherub, Addan, and Immer, but they could not show their fathers' house and their seed, whether they were of Israel:",
      "M": "The following came up from Tel-melah, Tel-harsha, Cherub, Addan, and Immer, but they were unable to prove their ancestral house and descent, or whether they belonged to Israel:",
      "T": "These families came from the Babylonian settlements of Tel-melah, Tel-harsha, Cherub, Addan, and Immer—but they could produce no documentation, no ancestral record proving their Israelite lineage:"
    },
    "60": {
      "L": "the sons of Delaiah, the sons of Tobiah, the sons of Nekoda, six hundred and fifty-two.",
      "M": "the descendants of Delaiah, Tobiah, and Nekoda—six hundred and fifty-two.",
      "T": "the families of Delaiah, Tobiah, and Nekoda: 652—present among the returnees but unable to verify their identity."
    },
    "61": {
      "L": "And of the sons of the priests: the sons of Habaiah, the sons of Hakkoz, the sons of Barzillai, who took a wife of the daughters of Barzillai the Gileadite, and was called by their name.",
      "M": "And of the sons of the priests: the families of Habaiah, Hakkoz, and Barzillai—the last having taken a wife from the daughters of Barzillai the Gileadite and adopted their clan name.",
      "T": "Among the priests there were also families whose lineage was disputed: the descendants of Habaiah, of Hakkoz, and of Barzillai—a man who had married into the Gileadite family of Barzillai and taken their name, absorbing a lay identity over a priestly one."
    },
    "62": {
      "L": "These sought their registration among those enrolled in the genealogies, but it was not found; therefore they were excluded from the priesthood as unclean.",
      "M": "These searched for their names in the genealogical register but could not find them, and so they were excluded from the priesthood as ceremonially unclean.",
      "T": "They searched the written genealogical records and found no entry for themselves. The consequence was exclusion: removed from the priesthood as unclean—not by any personal failure, but because the covenant's boundaries required documented continuity."
    },
    "63": {
      "L": "And the Tirshatha said to them that they should not eat of the most holy things until a priest stood up with Urim and with Thummim.",
      "M": "The governor told them that they must not eat of the most sacred offerings until a priest could consult the Urim and Thummim.",
      "T": "The governor placed them under a holding rule: no access to the most sacred food until a priest could consult the Urim and Thummim—the sacred oracular objects by which the LORD's own verdict would settle what human records could not."
    },
    "64": {
      "L": "The whole congregation together was forty-two thousand three hundred and sixty,",
      "M": "The whole assembly together numbered forty-two thousand three hundred and sixty,",
      "T": "When all the families were counted together, the returning assembly stood at forty-two thousand three hundred and sixty—"
    },
    "65": {
      "L": "besides their male servants and their female servants, of whom there were seven thousand three hundred and thirty-seven; and they had two hundred singing men and singing women.",
      "M": "not counting their male and female servants, who numbered seven thousand three hundred and thirty-seven; and there were also two hundred singing men and singing women.",
      "T": "—not counting 7,337 servants, men and women alike, along with 200 professional singers who traveled with the community."
    },
    "66": {
      "L": "Their horses were seven hundred and thirty-six, their mules were two hundred and forty-five,",
      "M": "Their horses numbered seven hundred and thirty-six, their mules two hundred and forty-five,",
      "T": "They brought with them 736 horses and 245 mules,"
    },
    "67": {
      "L": "their camels four hundred and thirty-five, their donkeys six thousand seven hundred and twenty.",
      "M": "their camels four hundred and thirty-five, and their donkeys six thousand seven hundred and twenty.",
      "T": "435 camels and 6,720 donkeys—animal wealth sufficient for the long journey and the building program that lay ahead."
    },
    "68": {
      "L": "And some of the heads of the fathers' houses, when they came to the house of LORD which is at Jerusalem, offered freely for the house of God to set it up in its place.",
      "M": "Some of the heads of the fathers' houses, when they arrived at the house of the LORD in Jerusalem, gave freewill offerings toward rebuilding the house of God on its site.",
      "T": "When the clan leaders arrived at the ruined site of the LORD's house in Jerusalem, some gave willingly toward its reconstruction—echoing the freewill spirit of those who built the first tabernacle in the wilderness."
    },
    "69": {
      "L": "They gave according to their ability to the treasury of the work sixty-one thousand darics of gold and five thousand minas of silver and one hundred priestly garments.",
      "M": "According to their ability they contributed to the building fund: sixty-one thousand darics of gold, five thousand minas of silver, and one hundred priestly garments.",
      "T": "Each gave according to their means: 61,000 darics of gold (Persian gold coins), 5,000 minas of silver, and 100 sets of priestly vestments—materials for both the structure and the worship it would house."
    },
    "70": {
      "L": "So the priests and the Levites and some of the people and the singers and the gatekeepers and the Nethinim dwelt in their cities, and all Israel in their cities.",
      "M": "The priests, the Levites, some of the people, the singers, the gatekeepers, and the temple servants settled in their own towns, and all Israel settled in their towns.",
      "T": "Then the whole community dispersed to their ancestral towns—priests, Levites, people, singers, gatekeepers, Nethinim, and all Israel—each taking up residence in the place the register had named as their own."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'ezra')
        merge_tier(existing, EZRA, tier_key)
        save(tier_dir, 'ezra', existing)
    print('Ezra 1–2 written.')

if __name__ == '__main__':
    main()
