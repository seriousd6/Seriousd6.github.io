"""
MKT 1 Chronicles chapters 1-5 -- three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-1chronicles-1-5.py

Translation decisions:
- H3068 (yhwh): "LORD" in L/M throughout; "the LORD" in T. Consistent with Kings/Samuel scripts.
- H430 (elohim): "God" in all tiers.
- H1121 (ben): "son" in L; "son" or "fathered" in M/T depending on context.
- H3205 (yalad): "begot" in L; "fathered" in M/T for genealogical chains.
- H441 (allup): "chief" in all tiers -- not the archaic "duke."
- H4940 (mishpachah): "clan/family" in M/T; "family/families" in L.
- H1755 (dor): "generation/generations" throughout.
- H8269 (sar): "prince/leader" in all tiers -- context determines which.
- H1061 (bikkur): Not prominent here.
- H5315 (nephesh): Embodied self; not the Greek immortal soul. Not prominent in chs 1-5.
- H7307 (ruach): 5:26 "spirit" (of the king) = inner drive/impulse. No capitalisation -- not the
  divine Spirit here.
- H2617 (hesed): Not prominent in chs 1-5.
- H1285 (berit): Not prominent in chs 1-5.

Textual notes:
- 1:17: Chronicles has "Meshech" where Gen 10:23 has "Mash." The Chronicler's reading is retained.
- 1:36: Timna appears as a son of Eliphaz; Gen 36:12 calls Timna a concubine. Both may reflect
  clan-name usage where personal and group names overlap.
- 2:7: "Achar" (troubler/oker) rather than "Achan" (Josh 7). The Chronicler's wordplay is
  preserved by retaining "Achar" in all tiers.
- 2:15: David listed as seventh son; 1 Sam 17:12 implies eight sons. Textual variant preserved.
- 3:1: "Daniel" (Chronicles) vs. "Chileab" (2 Sam 3:3). Same person; different sources.
- 5:26: "Pul" and "Tilgath-pilneser" are the same king; the Chronicler uses both names.
  Rendered as "Pul -- that is, Tilgath-pilneser" in M/T.

Hebrew aspect: Waw-consecutive imperfects throughout the narrative sections = simple past in English.
Genealogical formulas (X ben Y, wayyoled) = "X son of Y, fathered" in standard English order.
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
  "1": {
    "1": {
      "L": "Adam, Seth, Enosh.",
      "M": "Adam, Seth, Enosh.",
      "T": "The Chronicler begins at the origin of all things: Adam, Seth, Enosh -- humanity's first fathers, before Israel, before the covenant."
    },
    "2": {
      "L": "Kenan, Mahalalel, Jared.",
      "M": "Kenan, Mahalalel, Jared.",
      "T": "Kenan, Mahalalel, Jared -- the chain of life continuing from Adam toward the flood."
    },
    "3": {
      "L": "Enoch, Methuselah, Lamech.",
      "M": "Enoch, Methuselah, Lamech.",
      "T": "Enoch, Methuselah, Lamech -- the pre-flood elders, each a link in the line moving toward Noah."
    },
    "4": {
      "L": "Noah, Shem, Ham, and Japheth.",
      "M": "Noah. The sons of Noah: Shem, Ham, and Japheth.",
      "T": "Noah, and his three sons -- Shem, Ham, Japheth -- through whom the world was repopulated after the flood. All nations trace their origin here."
    },
    "5": {
      "L": "The sons of Japheth: Gomer, Magog, Madai, Javan, Tubal, Meshech, and Tiras.",
      "M": "The sons of Japheth: Gomer, Magog, Madai, Javan, Tubal, Meshech, and Tiras.",
      "T": "Japheth's seven sons -- Gomer, Magog, Madai, Javan, Tubal, Meshech, and Tiras -- ancestors of the northern and western nations, from Asia Minor to the far shores."
    },
    "6": {
      "L": "The sons of Gomer: Ashkenaz, Riphath, and Togarmah.",
      "M": "The sons of Gomer: Ashkenaz, Riphath, and Togarmah.",
      "T": "Gomer's sons -- Ashkenaz, Riphath, and Togarmah -- peoples of the Anatolian highlands and beyond."
    },
    "7": {
      "L": "The sons of Javan: Elishah, Tarshish, Kittim, and Dodanim.",
      "M": "The sons of Javan: Elishah, Tarshish, Kittim, and Dodanim.",
      "T": "Javan's sons -- Elishah, Tarshish, Kittim, Dodanim -- the Greeks and the seafaring Mediterranean peoples whose ships carried trade to the ends of the known world."
    },
    "8": {
      "L": "The sons of Ham: Cush, Egypt, Put, and Canaan.",
      "M": "The sons of Ham: Cush, Egypt, Put, and Canaan.",
      "T": "Ham's four sons -- Cush (Ethiopia), Egypt, Put (Libya), and Canaan -- the peoples of Africa and the Levantine coast, including the nations Israel was called to dispossess."
    },
    "9": {
      "L": "The sons of Cush: Seba, Havilah, Sabta, Raamah, and Sabteca. The sons of Raamah: Sheba and Dedan.",
      "M": "The sons of Cush: Seba, Havilah, Sabta, Raamah, and Sabteca. The sons of Raamah: Sheba and Dedan.",
      "T": "Cush's sons -- Seba, Havilah, Sabta, Raamah, and Sabteca -- and Raamah's sons Sheba and Dedan, the Arabian trading peoples whose caravans would later bring gifts to Solomon."
    },
    "10": {
      "L": "Cush begot Nimrod; he began to be mighty upon the earth.",
      "M": "Cush fathered Nimrod, who became the first mighty warrior on earth.",
      "T": "Cush fathered Nimrod -- the first empire-builder, the one who 'began to be mighty.' Genesis frames him as the archetype of human power built outside God's ordering; the Chronicler notes him without comment."
    },
    "11": {
      "L": "And Egypt begot the Ludim, the Anamim, the Lehabim, and the Naphtuhim,",
      "M": "Egypt fathered the Ludites, Anamites, Lehabites, and Naphtuhites,",
      "T": "From Egypt came the Ludites, Anamites, Lehabites, and Naphtuhites --"
    },
    "12": {
      "L": "and the Pathrusim and the Casluhim, from whom came the Philistines, and the Caphthorim.",
      "M": "and the Pathrusites and the Casluhites, from whom the Philistines came, and the Caphtorites.",
      "T": "-- and the Pathrusites and Casluhites. From the Casluhites came the Philistines, Israel's most persistent adversaries; and the Caphtorites."
    },
    "13": {
      "L": "And Canaan begot Sidon his firstborn, and Heth,",
      "M": "Canaan fathered Sidon his firstborn, and Heth,",
      "T": "Canaan's firstborn was Sidon, ancestor of the Phoenicians; and Heth, ancestor of the Hittites --"
    },
    "14": {
      "L": "and the Jebusite, and the Amorite, and the Girgashite,",
      "M": "and the Jebusites, the Amorites, the Girgashites,",
      "T": "-- and the Jebusites (Jerusalem's pre-conquest inhabitants), the Amorites, the Girgashites,"
    },
    "15": {
      "L": "and the Hivite, and the Arkite, and the Sinite,",
      "M": "and the Hivites, the Arkites, the Sinites,",
      "T": "the Hivites, the Arkites, the Sinites,"
    },
    "16": {
      "L": "and the Arvadite, and the Zemarite, and the Hamathite.",
      "M": "and the Arvadites, the Zemarites, and the Hamathites.",
      "T": "the Arvadites, Zemarites, and Hamathites -- the full catalogue of Canaan's peoples, every one of them within the boundaries of the Promised Land."
    },
    "17": {
      "L": "The sons of Shem: Elam, Asshur, Arphaxad, Lud, Aram, Uz, Hul, Gether, and Meshech.",
      "M": "The sons of Shem: Elam, Asshur, Arphaxad, Lud, Aram, Uz, Hul, Gether, and Meshech.",
      "T": "Shem's sons -- Elam (ancestral Persia), Asshur (Assyria), Arphaxad (the Abrahamic line), Lud, Aram, and their descendants Uz, Hul, Gether, Meshech -- the Semitic peoples from Mesopotamia to Arabia."
    },
    "18": {
      "L": "And Arphaxad begot Shelah, and Shelah begot Eber.",
      "M": "Arphaxad fathered Shelah, and Shelah fathered Eber.",
      "T": "Arphaxad fathered Shelah, and Shelah fathered Eber -- the ancestor whose name may stand behind the very word 'Hebrew.'"
    },
    "19": {
      "L": "To Eber were born two sons; the name of the one was Peleg, for in his days the earth was divided; and the name of his brother was Joktan.",
      "M": "Eber had two sons: the first was named Peleg, because in his time the earth was divided; his brother was named Joktan.",
      "T": "Eber had two sons. He named the first Peleg -- 'division' -- because in his days the earth was divided among the nations. His brother was Joktan, ancestor of the Arabian peoples."
    },
    "20": {
      "L": "And Joktan begot Almodad, Sheleph, Hazarmaveth, and Jerah,",
      "M": "Joktan fathered Almodad, Sheleph, Hazarmaveth, and Jerah,",
      "T": "Joktan's sons begin: Almodad, Sheleph, Hazarmaveth, and Jerah,"
    },
    "21": {
      "L": "and Hadoram, Uzal, and Diklah,",
      "M": "and Hadoram, Uzal, and Diklah,",
      "T": "Hadoram, Uzal, and Diklah,"
    },
    "22": {
      "L": "and Ebal, Abimael, and Sheba,",
      "M": "and Ebal, Abimael, and Sheba,",
      "T": "Ebal, Abimael, and Sheba,"
    },
    "23": {
      "L": "and Ophir, Havilah, and Jobab. All these were the sons of Joktan.",
      "M": "and Ophir, Havilah, and Jobab. All these were sons of Joktan.",
      "T": "-- and Ophir, Havilah, and Jobab. Thirteen sons of Joktan -- the Arabian peoples of the south and east, the world beyond the promise."
    },
    "24": {
      "L": "Shem, Arphaxad, Shelah,",
      "M": "Shem, Arphaxad, Shelah,",
      "T": "Now the Chronicler narrows the lens: from the wide Table of Nations, the line runs: Shem, Arphaxad, Shelah,"
    },
    "25": {
      "L": "Eber, Peleg, Reu,",
      "M": "Eber, Peleg, Reu,",
      "T": "Eber, Peleg, Reu,"
    },
    "26": {
      "L": "Serug, Nahor, Terah,",
      "M": "Serug, Nahor, Terah,",
      "T": "Serug, Nahor, Terah --"
    },
    "27": {
      "L": "Abram, that is, Abraham.",
      "M": "Abram, that is, Abraham.",
      "T": "-- Abram, renamed Abraham. The universal genealogy has narrowed from all humanity to a single man and a single promise. Everything that follows flows from here."
    },
    "28": {
      "L": "The sons of Abraham: Isaac and Ishmael.",
      "M": "The sons of Abraham: Isaac and Ishmael.",
      "T": "Abraham's two sons -- Isaac and Ishmael -- two lines, two destinies, both within the scope of God's blessing, though only one carries the covenant."
    },
    "29": {
      "L": "These are their generations: the firstborn of Ishmael, Nebaioth; then Kedar, Adbeel, and Mibsam,",
      "M": "These are the names of Ishmael's sons in birth order: the firstborn Nebaioth; then Kedar, Adbeel, and Mibsam,",
      "T": "Ishmael's sons in birth order: Nebaioth the firstborn, then Kedar -- the great Arab tribe cited by the prophets -- Adbeel, and Mibsam,"
    },
    "30": {
      "L": "Mishma, Dumah, Massa, Hadad, and Tema,",
      "M": "Mishma, Dumah, Massa, Hadad, and Tema,",
      "T": "Mishma, Dumah, Massa, Hadad, and Tema,"
    },
    "31": {
      "L": "Jetur, Naphish, and Kedemah. These are the sons of Ishmael.",
      "M": "Jetur, Naphish, and Kedemah. These were the sons of Ishmael.",
      "T": "-- Jetur, Naphish, and Kedemah. Twelve sons of Ishmael, twelve Arab tribes -- a fulfilment of God's promise that Ishmael too would become a great nation."
    },
    "32": {
      "L": "And the sons of Keturah, Abraham's concubine: she bore Zimran, Jokshan, Medan, Midian, Ishbak, and Shuah. And the sons of Jokshan: Sheba and Dedan.",
      "M": "The sons of Keturah, Abraham's concubine: she bore Zimran, Jokshan, Medan, Midian, Ishbak, and Shuah. The sons of Jokshan: Sheba and Dedan.",
      "T": "Keturah, Abraham's concubine, bore six sons -- Zimran, Jokshan, Medan, Midian, Ishbak, and Shuah -- ancestors of Arab and Midianite peoples. Jokshan's sons Sheba and Dedan were desert caravan peoples known across the ancient world."
    },
    "33": {
      "L": "And the sons of Midian: Ephah, Epher, Hanoch, Abida, and Eldaah. All these were the sons of Keturah.",
      "M": "The sons of Midian: Ephah, Epher, Hanoch, Abida, and Eldaah. All these were the descendants of Keturah.",
      "T": "Midian's sons -- Ephah, Epher, Hanoch, Abida, and Eldaah -- the Midianite clans. All these descend from Keturah, Abraham's second family -- the wider circle of his fruitfulness."
    },
    "34": {
      "L": "And Abraham begot Isaac. The sons of Isaac: Esau and Israel.",
      "M": "Abraham fathered Isaac. The sons of Isaac: Esau and Israel.",
      "T": "Abraham fathered Isaac. And Isaac's two sons -- Esau and Israel -- divided into two peoples, Edom and the covenant nation. The Chronicler surveys Edom's line before turning to Israel alone."
    },
    "35": {
      "L": "The sons of Esau: Eliphaz, Reuel, Jeush, Jalam, and Korah.",
      "M": "The sons of Esau: Eliphaz, Reuel, Jeush, Jalam, and Korah.",
      "T": "Esau's five sons -- Eliphaz, Reuel, Jeush, Jalam, and Korah -- the founding fathers of the Edomite clans."
    },
    "36": {
      "L": "The sons of Eliphaz: Teman, Omar, Zephi, Gatam, Kenaz, Timna, and Amalek.",
      "M": "The sons of Eliphaz: Teman, Omar, Zephi, Gatam, Kenaz, Timna, and Amalek.",
      "T": "Eliphaz's sons include Teman -- from whom the Temanites took their name -- and Amalek, Israel's perpetual adversary, here traced to a cousin-line. Timna's appearance as both a son here and a concubine in Genesis reflects the overlap of personal and clan names."
    },
    "37": {
      "L": "The sons of Reuel: Nahath, Zerah, Shammah, and Mizzah.",
      "M": "The sons of Reuel: Nahath, Zerah, Shammah, and Mizzah.",
      "T": "Reuel's four sons -- Nahath, Zerah, Shammah, and Mizzah -- the southern Edomite clans."
    },
    "38": {
      "L": "And the sons of Seir: Lotan, Shobal, Zibeon, Anah, Dishon, Ezer, and Dishan.",
      "M": "The sons of Seir: Lotan, Shobal, Zibeon, Anah, Dishon, Ezer, and Dishan.",
      "T": "The native Horite inhabitants of Edom -- Seir's sons: Lotan, Shobal, Zibeon, Anah, Dishon, Ezer, and Dishan. These were the people who occupied the land before Esau's descendants displaced them."
    },
    "39": {
      "L": "And the sons of Lotan: Hori and Homam; and Lotan's sister was Timna.",
      "M": "The sons of Lotan: Hori and Homam. Lotan's sister was Timna.",
      "T": "Lotan's sons were Hori and Homam; his sister Timna -- whose name also appears in Eliphaz's line -- was a significant figure linking the Horite and Edomite peoples."
    },
    "40": {
      "L": "The sons of Shobal: Alian, Manahath, Ebal, Shephi, and Onam. The sons of Zibeon: Aiah and Anah.",
      "M": "The sons of Shobal: Alian, Manahath, Ebal, Shephi, and Onam. The sons of Zibeon: Aiah and Anah.",
      "T": "Shobal's five sons -- Alian, Manahath, Ebal, Shephi, Onam; and Zibeon's two -- Aiah and Anah."
    },
    "41": {
      "L": "The son of Anah: Dishon. And the sons of Dishon: Hamran, Eshban, Ithran, and Cheran.",
      "M": "Anah's son: Dishon. The sons of Dishon: Hamran, Eshban, Ithran, and Cheran.",
      "T": "Anah's son was Dishon; Dishon's sons were Hamran, Eshban, Ithran, and Cheran -- the inner Horite clans."
    },
    "42": {
      "L": "The sons of Ezer: Bilhan, Zaavan, and Jaakan. The sons of Dishan: Uz and Aran.",
      "M": "The sons of Ezer: Bilhan, Zaavan, and Jaakan. The sons of Dishan: Uz and Aran.",
      "T": "Ezer's sons -- Bilhan, Zaavan, Jaakan; Dishan's sons -- Uz and Aran. The Horite genealogy is complete; the native people of Seir have been accounted for."
    },
    "43": {
      "L": "Now these are the kings who reigned in the land of Edom before any king reigned over the sons of Israel: Bela son of Beor, and the name of his city was Dinhabah.",
      "M": "These are the kings who reigned in Edom before any king reigned over Israel: Bela son of Beor, whose city was Dinhabah.",
      "T": "Edom had kings before Israel did. The Chronicler records them without embarrassment: Bela son of Beor, reigning from Dinhabah, was the first. Israel's monarchy would come later and prove greater."
    },
    "44": {
      "L": "And Bela died, and Jobab son of Zerah of Bozrah reigned in his stead.",
      "M": "When Bela died, Jobab son of Zerah from Bozrah reigned in his place.",
      "T": "Bela died; Jobab son of Zerah of Bozrah succeeded him."
    },
    "45": {
      "L": "And Jobab died, and Husham of the land of the Temanites reigned in his stead.",
      "M": "When Jobab died, Husham of the land of the Temanites reigned in his place.",
      "T": "Jobab died; Husham of the Temanite territory took the throne."
    },
    "46": {
      "L": "And Husham died, and Hadad son of Bedad, who struck Midian in the field of Moab, reigned in his stead; and the name of his city was Avith.",
      "M": "When Husham died, Hadad son of Bedad reigned in his place -- he had defeated Midian on the territory of Moab; his city was Avith.",
      "T": "Husham died; Hadad son of Bedad seized power -- a warrior-king who had crushed Midian on Moab's soil. His capital was Avith."
    },
    "47": {
      "L": "And Hadad died, and Samlah of Masrekah reigned in his stead.",
      "M": "When Hadad died, Samlah of Masrekah reigned in his place.",
      "T": "Hadad died; Samlah of Masrekah succeeded him."
    },
    "48": {
      "L": "And Samlah died, and Shaul of Rehoboth-on-the-River reigned in his stead.",
      "M": "When Samlah died, Shaul of Rehoboth-by-the-River reigned in his place.",
      "T": "Samlah died; Shaul of Rehoboth-on-the-River took the throne -- a king whose city name evokes the wide plains."
    },
    "49": {
      "L": "And Shaul died, and Baal-hanan son of Achbor reigned in his stead.",
      "M": "When Shaul died, Baal-hanan son of Achbor reigned in his place.",
      "T": "Shaul died; Baal-hanan son of Achbor succeeded him."
    },
    "50": {
      "L": "And Baal-hanan died, and Hadad reigned in his stead; and the name of his city was Pai; and his wife's name was Mehetabel daughter of Matred, daughter of Me-zahab.",
      "M": "When Baal-hanan died, Hadad reigned in his place. His city was Pai, and his wife was Mehetabel daughter of Matred, daughter of Me-zahab.",
      "T": "Baal-hanan died; the second Hadad reigned from Pai. His wife Mehetabel -- daughter of Matred, granddaughter of Me-zahab -- is one of the few Edomite women named in the record, her lineage preserved as a mark of royal dignity."
    },
    "51": {
      "L": "Then Hadad died. And the chiefs of Edom were: chief Timna, chief Aliah, chief Jetheth,",
      "M": "Hadad also died. The chiefs of Edom: chief Timna, chief Aliah, chief Jetheth,",
      "T": "Hadad too died. The royal line ends; now come the territorial chiefs of Edom: Timna, Aliah, Jetheth,"
    },
    "52": {
      "L": "chief Oholibamah, chief Elah, chief Pinon,",
      "M": "chief Oholibamah, chief Elah, chief Pinon,",
      "T": "Oholibamah, Elah, Pinon,"
    },
    "53": {
      "L": "chief Kenaz, chief Teman, chief Mibzar,",
      "M": "chief Kenaz, chief Teman, chief Mibzar,",
      "T": "Kenaz, Teman, Mibzar,"
    },
    "54": {
      "L": "chief Magdiel, chief Iram. These are the chiefs of Edom.",
      "M": "chief Magdiel, and chief Iram. These were the chiefs of Edom.",
      "T": "-- Magdiel and Iram. Eleven chiefs in all. The long survey of Edom closes here; the Chronicler now turns his full attention to Israel."
    }
  },
  "2": {
    "1": {
      "L": "These are the sons of Israel: Reuben, Simeon, Levi, Judah, Issachar, and Zebulun,",
      "M": "These are the sons of Israel: Reuben, Simeon, Levi, Judah, Issachar, and Zebulun,",
      "T": "Here the Chronicler arrives at Israel -- Jacob's twelve sons, the twelve tribes from whom the covenant nation took its shape. Reuben, Simeon, Levi, Judah, Issachar, Zebulun,"
    },
    "2": {
      "L": "Dan, Joseph, Benjamin, Naphtali, Gad, and Asher.",
      "M": "Dan, Joseph, Benjamin, Naphtali, Gad, and Asher.",
      "T": "-- Dan, Joseph, Benjamin, Naphtali, Gad, and Asher. Twelve names; twelve peoples. The whole nation stands here in a single verse."
    },
    "3": {
      "L": "The sons of Judah: Er, Onan, and Shelah; these three were born to him by Bath-shua the Canaanitess. And Er, Judah's firstborn, was evil in the sight of the LORD, and he put him to death.",
      "M": "Judah's sons: Er, Onan, and Shelah -- these three born to him by Bath-shua the Canaanite woman. But Er, Judah's firstborn, was evil in the LORD's sight, and the LORD put him to death.",
      "T": "Judah's three sons by Bath-shua the Canaanite woman -- Er, Onan, and Shelah. But the line nearly died at its first step: Er was so wicked that the LORD himself cut him off."
    },
    "4": {
      "L": "And Tamar his daughter-in-law bore him Perez and Zerah. All the sons of Judah were five.",
      "M": "Tamar his daughter-in-law bore him Perez and Zerah. Judah had five sons in all.",
      "T": "Tamar, Judah's own daughter-in-law, bore him Perez and Zerah -- the line that would carry David. The continuation of Judah's promise came through an act of unexpected faithfulness from an unexpected source."
    },
    "5": {
      "L": "The sons of Perez: Hezron and Hamul.",
      "M": "The sons of Perez: Hezron and Hamul.",
      "T": "Perez's sons -- Hezron and Hamul. Through Hezron the line will run directly to David."
    },
    "6": {
      "L": "And the sons of Zerah: Zimri, Ethan, Heman, Calcol, and Dara -- five of them in all.",
      "M": "The sons of Zerah: Zimri, Ethan, Heman, Calcol, and Dara -- five in all.",
      "T": "Zerah's five sons -- Zimri, Ethan, Heman, Calcol, and Dara. Ethan and Heman are names later associated with wisdom and psalmody; their Judaean lineage is noted here."
    },
    "7": {
      "L": "And the son of Carmi: Achar, the troubler of Israel, who violated the ban on devoted things.",
      "M": "The son of Carmi: Achar, the troubler of Israel, who broke faith by taking from the things devoted to destruction.",
      "T": "Carmi's son was Achar -- the Chronicler deliberately spells his name as 'oker' (troubler) rather than 'Achan,' making the wordplay explicit: this is the man whose theft of devoted plunder at Jericho brought disaster on all Israel."
    },
    "8": {
      "L": "And the son of Ethan: Azariah.",
      "M": "The son of Ethan: Azariah.",
      "T": "Ethan's son was Azariah -- one name, the wisdom line persisting."
    },
    "9": {
      "L": "The sons of Hezron that were born to him: Jerahmeel, Ram, and Chelubai.",
      "M": "The sons born to Hezron: Jerahmeel, Ram, and Chelubai.",
      "T": "Hezron's three sons -- Jerahmeel, Ram, and Chelubai (also called Caleb). Ram is the branch that leads to David."
    },
    "10": {
      "L": "And Ram begot Amminadab, and Amminadab begot Nahshon, prince of the sons of Judah;",
      "M": "Ram fathered Amminadab, and Amminadab fathered Nahshon, the prince of the tribe of Judah.",
      "T": "Ram fathered Amminadab, who fathered Nahshon -- the tribal prince of Judah at the time of the Exodus, Aaron's brother-in-law, one of the great names on the road from Egypt to David."
    },
    "11": {
      "L": "and Nahshon begot Salma, and Salma begot Boaz,",
      "M": "Nahshon fathered Salma, and Salma fathered Boaz,",
      "T": "Nahshon fathered Salma, and Salma fathered Boaz --"
    },
    "12": {
      "L": "and Boaz begot Obed, and Obed begot Jesse,",
      "M": "Boaz fathered Obed, and Obed fathered Jesse,",
      "T": "-- Boaz, the kinsman-redeemer who married Ruth the Moabitess; Boaz fathered Obed, Obed fathered Jesse --"
    },
    "13": {
      "L": "and Jesse begot his firstborn Eliab, and Abinadab the second, and Shimma the third,",
      "M": "Jesse fathered Eliab his firstborn, Abinadab the second, and Shimma the third,",
      "T": "Jesse's sons in birth order: Eliab the firstborn -- the one who looked like a king but was passed over -- Abinadab second, Shimma third,"
    },
    "14": {
      "L": "Nethanel the fourth, Raddai the fifth,",
      "M": "Nethanel the fourth, Raddai the fifth,",
      "T": "Nethanel fourth, Raddai fifth,"
    },
    "15": {
      "L": "Ozem the sixth, David the seventh.",
      "M": "Ozem the sixth, David the seventh.",
      "T": "Ozem sixth, David seventh. David the youngest, the least expected -- the one God had chosen before his brothers could imagine it."
    },
    "16": {
      "L": "And their sisters were Zeruiah and Abigail. And the sons of Zeruiah: Abishai, Joab, and Asahel -- three.",
      "M": "Their sisters were Zeruiah and Abigail. The sons of Zeruiah: Abishai, Joab, and Asahel -- three.",
      "T": "David's sisters Zeruiah and Abigail are recorded -- rare in genealogy. Zeruiah's three sons -- Abishai, Joab, and Asahel -- were David's most formidable warriors and most complicated relatives."
    },
    "17": {
      "L": "And Abigail bore Amasa; and the father of Amasa was Jether the Ishmaelite.",
      "M": "Abigail bore Amasa; his father was Jether the Ishmaelite.",
      "T": "Abigail bore Amasa, a nephew of David who would later betray him for Absalom. His Ishmaelite father marks a thread of foreign blood in David's own family."
    },
    "18": {
      "L": "And Caleb son of Hezron fathered children by his wife Azubah and by Jerioth; and these were her sons: Jesher, Shobab, and Ardon.",
      "M": "Caleb son of Hezron had children with his wife Azubah and Jerioth. Her sons were Jesher, Shobab, and Ardon.",
      "T": "Caleb son of Hezron -- the forefather of the great spy Caleb -- had sons by Azubah and Jerioth: Jesher, Shobab, and Ardon."
    },
    "19": {
      "L": "And when Azubah died, Caleb took Ephrath, and she bore him Hur.",
      "M": "After Azubah died, Caleb married Ephrath, who bore him Hur.",
      "T": "After Azubah died, Caleb married Ephrath; she bore him Hur, founder of the Ephrathah clans and ancestor of Bezalel."
    },
    "20": {
      "L": "And Hur begot Uri, and Uri begot Bezalel.",
      "M": "Hur fathered Uri, and Uri fathered Bezalel.",
      "T": "Hur fathered Uri, who fathered Bezalel -- the master craftsman filled by God's Spirit to build the tabernacle. This genealogy grounds the great artisan squarely in Judah's line."
    },
    "21": {
      "L": "And afterward Hezron went in to the daughter of Machir the father of Gilead, whom he married when he was sixty years old; and she bore him Segub.",
      "M": "Later, Hezron married the daughter of Machir the father of Gilead -- he was sixty years old at the time -- and she bore him Segub.",
      "T": "In his later years, Hezron married a daughter of Machir of Gilead. At sixty he fathered Segub -- a union bridging Judah and the trans-Jordan, with consequences for territory still felt generations later."
    },
    "22": {
      "L": "And Segub begot Jair, who had twenty-three cities in the land of Gilead.",
      "M": "Segub fathered Jair, who possessed twenty-three towns in the land of Gilead.",
      "T": "Segub fathered Jair, who held twenty-three towns in Gilead -- a man of real territorial power, his inheritance spanning the eastern side of the Jordan."
    },
    "23": {
      "L": "And Geshur and Aram took from them the towns of Jair, and Kenath and its villages, sixty towns. All these belonged to the sons of Machir the father of Gilead.",
      "M": "But Geshur and Aram took the towns of Jair from them -- along with Kenath and its villages, sixty towns in all. All these had belonged to the sons of Machir the father of Gilead.",
      "T": "Yet those sixty towns were lost to Geshur and Aram -- a reminder that territorial possession is always precarious without the LORD's protection. They had all once belonged to Machir's descendants."
    },
    "24": {
      "L": "And after Hezron died in Caleb-ephrathah, Hezron's wife Abijah bore him Ashhur the father of Tekoa.",
      "M": "After Hezron died at Caleb-ephrathah, his wife Abijah bore him Ashhur the founder of Tekoa.",
      "T": "After Hezron's death at Caleb-ephrathah, Abijah his widow bore Ashhur -- the founding father of Tekoa, the city that would later produce the prophet Amos."
    },
    "25": {
      "L": "And the sons of Jerahmeel the firstborn of Hezron were Ram his firstborn, Bunah, Oren, Ozem, and Ahijah.",
      "M": "The sons of Jerahmeel, Hezron's firstborn: Ram his firstborn, Bunah, Oren, Ozem, and Ahijah.",
      "T": "Jerahmeel's sons -- Ram, Bunah, Oren, Ozem, and Ahijah -- the extended family running parallel to the main Davidic branch."
    },
    "26": {
      "L": "Jerahmeel also had another wife, whose name was Atarah; she was the mother of Onam.",
      "M": "Jerahmeel had another wife named Atarah; she was the mother of Onam.",
      "T": "Jerahmeel's second wife Atarah bore Onam -- a second branch off the same trunk."
    },
    "27": {
      "L": "And the sons of Ram, the firstborn of Jerahmeel: Maaz, Jamin, and Eker.",
      "M": "The sons of Ram, Jerahmeel's firstborn: Maaz, Jamin, and Eker.",
      "T": "Ram's sons -- Maaz, Jamin, Eker -- a branch that keeps the name 'Ram' alive within Jerahmeel's wider family."
    },
    "28": {
      "L": "And the sons of Onam were Shammai and Jada. And the sons of Shammai: Nadab and Abishur.",
      "M": "Onam's sons: Shammai and Jada. The sons of Shammai: Nadab and Abishur.",
      "T": "Onam's sons were Shammai and Jada; Shammai's sons were Nadab and Abishur."
    },
    "29": {
      "L": "And the name of the wife of Abishur was Abihail; and she bore him Ahban and Molid.",
      "M": "Abishur's wife was named Abihail; she bore him Ahban and Molid.",
      "T": "Abishur's wife Abihail bore Ahban and Molid -- their names preserved here as the Chronicler fills out every living branch of Judah's clan-tree."
    },
    "30": {
      "L": "And the sons of Nadab: Seled and Appaim; and Seled died without children.",
      "M": "The sons of Nadab: Seled and Appaim. Seled died without children.",
      "T": "Nadab's sons were Seled and Appaim -- but Seled died childless, his branch ending there. The Chronicler notes extinctions as carefully as continuations."
    },
    "31": {
      "L": "And the son of Appaim: Ishi. And the son of Ishi: Sheshan. And the son of Sheshan: Ahlai.",
      "M": "The son of Appaim: Ishi. The son of Ishi: Sheshan. The son of Sheshan: Ahlai.",
      "T": "Appaim fathered Ishi, Ishi fathered Sheshan, Sheshan fathered Ahlai -- a thin but surviving line, each generation down to a single heir."
    },
    "32": {
      "L": "And the sons of Jada the brother of Shammai: Jether and Jonathan; and Jether died without children.",
      "M": "The sons of Jada, Shammai's brother: Jether and Jonathan. Jether died without children.",
      "T": "Jada's sons -- Jether and Jonathan. Again a branch cut short: Jether died without sons."
    },
    "33": {
      "L": "And the sons of Jonathan: Peleth and Zaza. These were the sons of Jerahmeel.",
      "M": "The sons of Jonathan: Peleth and Zaza. These were the descendants of Jerahmeel.",
      "T": "Jonathan's sons -- Peleth and Zaza -- close the Jerahmeel branch. Every surviving twig of this extended family has been traced."
    },
    "34": {
      "L": "Now Sheshan had no sons, only daughters; and Sheshan had an Egyptian servant whose name was Jarha.",
      "M": "Sheshan had no sons, only daughters. He had an Egyptian servant named Jarha.",
      "T": "Sheshan faced the genealogical crisis of having no sons -- only daughters. His Egyptian slave Jarha becomes the unexpected solution. The line will continue through an outsider."
    },
    "35": {
      "L": "And Sheshan gave his daughter to Jarha his servant as wife; and she bore him Attai.",
      "M": "Sheshan gave his daughter to Jarha his servant in marriage, and she bore Attai.",
      "T": "Sheshan gave his daughter to Jarha -- a remarkable social crossing, a free Israelite woman married to a slave. She bore Attai, and the line continued through an Egyptian-Israelite union embedded permanently in Judah's record."
    },
    "36": {
      "L": "And Attai begot Nathan, and Nathan begot Zabad,",
      "M": "Attai fathered Nathan, Nathan fathered Zabad,",
      "T": "Attai fathered Nathan, Nathan fathered Zabad --"
    },
    "37": {
      "L": "and Zabad begot Ephlal, and Ephlal begot Obed,",
      "M": "Zabad fathered Ephlal, Ephlal fathered Obed,",
      "T": "-- Zabad, Ephlal, Obed --"
    },
    "38": {
      "L": "and Obed begot Jehu, and Jehu begot Azariah,",
      "M": "Obed fathered Jehu, Jehu fathered Azariah,",
      "T": "-- Jehu, Azariah --"
    },
    "39": {
      "L": "and Azariah begot Helez, and Helez begot Eleasah,",
      "M": "Azariah fathered Helez, Helez fathered Eleasah,",
      "T": "-- Helez, Eleasah --"
    },
    "40": {
      "L": "and Eleasah begot Sisamai, and Sisamai begot Shallum,",
      "M": "Eleasah fathered Sisamai, Sisamai fathered Shallum,",
      "T": "-- Sisamai, Shallum --"
    },
    "41": {
      "L": "and Shallum begot Jekamiah, and Jekamiah begot Elishama.",
      "M": "Shallum fathered Jekamiah, and Jekamiah fathered Elishama.",
      "T": "-- Jekamiah and Elishama. Thirteen generations from Attai to Elishama -- the Egyptian-Israelite line fully integrated into Judah's genealogical record."
    },
    "42": {
      "L": "Now the sons of Caleb the brother of Jerahmeel: Mesha his firstborn, who was the father of Ziph; and the sons of Mareshah the father of Hebron.",
      "M": "The sons of Caleb, Jerahmeel's brother: Mesha his firstborn, who founded Ziph; and the sons of Mareshah, the founder of Hebron.",
      "T": "Caleb (Jerahmeel's brother, distinct from the famous spy) had Mesha as firstborn -- founder of Ziph. His descendants also founded Mareshah and Hebron, key towns in Judah's heartland."
    },
    "43": {
      "L": "And the sons of Hebron: Korah, Tappuah, Rekem, and Shema.",
      "M": "The sons of Hebron: Korah, Tappuah, Rekem, and Shema.",
      "T": "Hebron's sons -- Korah, Tappuah, Rekem, and Shema -- the clans of this pivotal city, Abraham's burial site and David's first capital."
    },
    "44": {
      "L": "And Shema begot Raham the father of Jorkoam; and Rekem begot Shammai.",
      "M": "Shema fathered Raham the founder of Jorkoam; Rekem fathered Shammai.",
      "T": "Shema fathered Raham, who founded Jorkoam; Rekem fathered Shammai."
    },
    "45": {
      "L": "And the son of Shammai was Maon; and Maon was the father of Beth-zur.",
      "M": "The son of Shammai was Maon; Maon founded Beth-zur.",
      "T": "Shammai's son Maon founded Beth-zur, a fortified city in the Judaean hills that would later appear in the Maccabean wars."
    },
    "46": {
      "L": "And Ephah, Caleb's concubine, bore Haran, Moza, and Gazez; and Haran begot Gazez.",
      "M": "Ephah, Caleb's concubine, bore Haran, Moza, and Gazez. Haran also fathered Gazez.",
      "T": "Caleb's concubine Ephah bore Haran, Moza, and Gazez; Haran in turn fathered another Gazez -- a doubled name suggesting a prominent and wide-spread clan."
    },
    "47": {
      "L": "And the sons of Jahdai: Regem, Jotham, Geshan, Pelet, Ephah, and Shaaph.",
      "M": "The sons of Jahdai: Regem, Jotham, Geshan, Pelet, Ephah, and Shaaph.",
      "T": "Jahdai's six sons -- Regem, Jotham, Geshan, Pelet, Ephah, and Shaaph."
    },
    "48": {
      "L": "Maacah, Caleb's concubine, bore Sheber and Tirhanah.",
      "M": "Caleb's concubine Maacah bore Sheber and Tirhanah.",
      "T": "Caleb's concubine Maacah bore Sheber and Tirhanah -- a second household alongside Ephah's."
    },
    "49": {
      "L": "She also bore Shaaph the father of Madmannah, and Sheva the father of Machbenah and the father of Gibea; and the daughter of Caleb was Achsah.",
      "M": "She also bore Shaaph the founder of Madmannah, and Sheva the founder of Machbenah and Gibea. Caleb's daughter was Achsah.",
      "T": "Maacah also bore Shaaph (founder of Madmannah) and Sheva (founder of Machbenah and Gibea). The note that Caleb's daughter was Achsah recalls the bold young woman who asked her father for the springs of water -- and got them."
    },
    "50": {
      "L": "These were the sons of Caleb the son of Hur, the firstborn of Ephrathah: Shobal the father of Kiriath-jearim,",
      "M": "These were the descendants of Caleb son of Hur, the firstborn of Ephrathah: Shobal the founder of Kiriath-jearim,",
      "T": "From Caleb son of Hur -- Ephrathah's firstborn -- came sons of great importance: Shobal, who founded Kiriath-jearim, where the ark of God would rest for twenty years before David brought it to Jerusalem,"
    },
    "51": {
      "L": "Salma the father of Bethlehem, and Hareph the father of Beth-gader.",
      "M": "Salma the founder of Bethlehem, and Hareph the founder of Beth-gader.",
      "T": "-- Salma, who founded Bethlehem -- David's own city -- and Hareph, who founded Beth-gader."
    },
    "52": {
      "L": "And Shobal the father of Kiriath-jearim had sons: Haroeh and half of the Manahathites.",
      "M": "Shobal the founder of Kiriath-jearim had sons: Haroeh and half the Manahathites.",
      "T": "Shobal's descendants -- Haroeh and half the Manahathite clans -- governed Kiriath-jearim, the city divided between two family-groups."
    },
    "53": {
      "L": "And the families of Kiriath-jearim: the Ithrites, the Puthites, the Shumathites, and the Mishraites. From these came the Zorathites and the Eshtaolites.",
      "M": "The clans of Kiriath-jearim: the Ithrites, the Puthites, the Shumathites, and the Mishraites. From these came the Zorathites and the Eshtaolites.",
      "T": "Kiriath-jearim's clans -- the Ithrites, Puthites, Shumathites, and Mishraites -- including the Zorathites and Eshtaolites who inhabited the territory of Zorah and Eshtaol, the landscape of Samson's story."
    },
    "54": {
      "L": "The sons of Salma: Bethlehem, the Netophathites, Atroth-beth-joab, and half of the Manahathites, the Zorites.",
      "M": "The sons of Salma: Bethlehem, the Netophathites, Atroth-beth-joab, and half the Manahathites, the Zorites.",
      "T": "Salma's descendants settled Bethlehem, Netophah, Atroth-beth-joab, and half the Manahathites -- the villages and clans radiating out from David's birthplace."
    },
    "55": {
      "L": "And the families of the scribes who dwelt at Jabez: the Tirathites, the Shimeathites, and the Sucathites. These are the Kenites who came from Hammath, the father of the house of Rechab.",
      "M": "The families of scribes who settled at Jabez: the Tirathites, the Shimeathites, and the Sucathites. These are the Kenites descended from Hammath, the father of the house of Rechab.",
      "T": "The scribal guilds settled at Jabez -- Tirathites, Shimeathites, Sucathites -- identified as Kenites from the house of Rechab. These are Israel's embedded outsiders: non-Israelites whose loyalty to the LORD went back to Moses' day, and whose descendants Jeremiah would later hold up as a model of faithfulness."
    }
  },
  "3": {
    "1": {
      "L": "Now these were the sons of David who were born to him in Hebron: the firstborn, Amnon by Ahinoam the Jezreelite; the second, Daniel by Abigail the Carmelite;",
      "M": "These were the sons of David born to him in Hebron: the firstborn Amnon, whose mother was Ahinoam the Jezreelite; the second Daniel, by Abigail the Carmelite;",
      "T": "David's sons born in Hebron during his seven-year reign over Judah: firstborn Amnon by Ahinoam of Jezreel; second, Daniel (called Chileab in 2 Samuel -- the same person, different tradition) by Abigail of Carmel --"
    },
    "2": {
      "L": "the third, Absalom the son of Maacah the daughter of Talmai king of Geshur; the fourth, Adonijah the son of Haggith;",
      "M": "the third Absalom, son of Maacah daughter of Talmai king of Geshur; the fourth Adonijah, son of Haggith;",
      "T": "-- third, Absalom, son of the Geshurite princess Maacah -- royal foreign blood that would feed his ambition; fourth, Adonijah by Haggith --"
    },
    "3": {
      "L": "the fifth, Shephatiah by Abital; the sixth, Ithream by his wife Eglah.",
      "M": "the fifth Shephatiah by Abital; the sixth Ithream by his wife Eglah.",
      "T": "-- fifth, Shephatiah by Abital; sixth, Ithream by Eglah. Six sons, six mothers -- David's Hebron household before the Jerusalem chapter began."
    },
    "4": {
      "L": "These six were born to him in Hebron. He reigned there seven years and six months; and in Jerusalem he reigned thirty-three years.",
      "M": "These six were born to him in Hebron, where he reigned seven years and six months. He then reigned thirty-three years in Jerusalem.",
      "T": "Six sons born in Hebron, seven and a half years of reign over Judah alone. Then Jerusalem: thirty-three years more. Forty years of kingship in total -- a reign shaped like the wilderness generation."
    },
    "5": {
      "L": "And these were born to him in Jerusalem: Shimea, Shobab, Nathan, and Solomon -- four -- by Bathshua the daughter of Ammiel;",
      "M": "These were born to him in Jerusalem: Shimea, Shobab, Nathan, and Solomon -- four sons -- by Bathshua daughter of Ammiel.",
      "T": "In Jerusalem, Bathshua (Bathsheba) daughter of Ammiel bore David four sons: Shimea, Shobab, Nathan, and Solomon. Nathan carries the Davidic line in Luke's genealogy of Jesus; Solomon carries it in Matthew's."
    },
    "6": {
      "L": "and Ibhar, Elishama, and Eliphelet,",
      "M": "and Ibhar, Elishama, and Eliphelet,",
      "T": "and Ibhar, Elishama, and Eliphelet --"
    },
    "7": {
      "L": "and Nogah, Nepheg, and Japhia,",
      "M": "and Nogah, Nepheg, and Japhia,",
      "T": "-- Nogah, Nepheg, Japhia --"
    },
    "8": {
      "L": "and Elishama, Eliada, and Eliphelet -- nine.",
      "M": "and Elishama, Eliada, and Eliphelet -- nine more.",
      "T": "-- and Elishama, Eliada, and Eliphelet. Nine additional sons in Jerusalem. Some names recur, suggesting different mothers or the use of multiple source documents."
    },
    "9": {
      "L": "All these were the sons of David, besides the sons of the concubines; and Tamar was their sister.",
      "M": "All these were David's sons, in addition to the sons of his concubines. Their sister was Tamar.",
      "T": "All these were David's acknowledged sons -- the concubines' children go unnamed. Tamar alone among the daughters is remembered: she who was violated by Amnon, whose grief was silenced by her father, whose story fractured the royal house."
    },
    "10": {
      "L": "And Solomon's son was Rehoboam, Abijah his son, Asa his son, Jehoshaphat his son,",
      "M": "Solomon's son was Rehoboam; then Abijah, Asa, and Jehoshaphat.",
      "T": "The royal succession: Solomon fathered Rehoboam, who lost the northern ten tribes; Rehoboam fathered Abijah; Abijah fathered Asa, who walked in David's ways; Asa fathered Jehoshaphat --"
    },
    "11": {
      "L": "Joram his son, Ahaziah his son, Joash his son,",
      "M": "Joram his son, Ahaziah his son, Joash his son,",
      "T": "-- Joram (who married Ahab's daughter and nearly destroyed the Davidic house), Ahaziah, Joash (rescued as an infant from Athaliah's purge) --"
    },
    "12": {
      "L": "Amaziah his son, Azariah his son, Jotham his son,",
      "M": "Amaziah his son, Azariah his son, Jotham his son,",
      "T": "-- Amaziah, Azariah (also called Uzziah -- the great king whose pride cost him his throne and his health), Jotham --"
    },
    "13": {
      "L": "Ahaz his son, Hezekiah his son, Manasseh his son,",
      "M": "Ahaz his son, Hezekiah his son, Manasseh his son,",
      "T": "-- Ahaz (who gave his son to fire and called on Assyria), Hezekiah (who trusted the LORD and saw Jerusalem delivered), Manasseh (the worst king -- yet the one who repented in captivity) --"
    },
    "14": {
      "L": "Amon his son, Josiah his son.",
      "M": "Amon his son, Josiah his son.",
      "T": "-- Amon, and Josiah. The reform king stands near the dynasty's end. The exile is coming."
    },
    "15": {
      "L": "And the sons of Josiah: the firstborn Johanan, the second Jehoiakim, the third Zedekiah, the fourth Shallum.",
      "M": "The sons of Josiah: the firstborn Johanan, Jehoiakim the second, Zedekiah the third, Shallum the fourth.",
      "T": "Josiah's four sons -- Johanan (who apparently died before ruling), Jehoiakim (installed by Pharaoh), Zedekiah (the last king of Jerusalem), and Shallum (also called Jehoahaz, deposed by Egypt) -- the dynasty fracturing in real time."
    },
    "16": {
      "L": "And the sons of Jehoiakim: Jeconiah his son, Zedekiah his son.",
      "M": "The sons of Jehoiakim: Jeconiah his son and Zedekiah his son.",
      "T": "Jehoiakim's sons: Jeconiah (also called Coniah and Jehoiachin) -- the king Babylon carried into exile at eighteen -- and Zedekiah. Jeconiah is the pivot point: everything after him is post-exile Davidic lineage."
    },
    "17": {
      "L": "And the sons of Jeconiah the captive: Shealtiel his son,",
      "M": "The sons of Jeconiah the captive: Shealtiel his son,",
      "T": "Jeconiah is named 'the captive' -- the king who went to Babylon and never returned. His son Shealtiel links the pre-exilic and post-exilic Davidic lines."
    },
    "18": {
      "L": "and Malchiram, Pedaiah, Shenazzar, Jekamiah, Hoshama, and Nedabiah.",
      "M": "and Malchiram, Pedaiah, Shenazzar, Jekamiah, Hoshama, and Nedabiah.",
      "T": "-- and his brothers: Malchiram, Pedaiah, Shenazzar, Jekamiah, Hoshama, Nedabiah -- sons of the exile, raised in Babylon but bearing Hebrew names, the covenant identity maintained in captivity."
    },
    "19": {
      "L": "And the sons of Pedaiah: Zerubbabel and Shimei. And the sons of Zerubbabel: Meshullam and Hananiah; and Shelomith was their sister.",
      "M": "The sons of Pedaiah: Zerubbabel and Shimei. The sons of Zerubbabel: Meshullam and Hananiah; their sister was Shelomith.",
      "T": "Pedaiah fathered Zerubbabel -- the governor who led the first return from Babylon and laid the foundation of the second temple. Zerubbabel's sons were Meshullam and Hananiah; their sister Shelomith is named alongside them."
    },
    "20": {
      "L": "And Hashubah, Ohel, Berechiah, Hasadiah, and Jushabhesed -- five.",
      "M": "And Hashubah, Ohel, Berechiah, Hasadiah, and Jushabhesed -- five more.",
      "T": "Five more sons of Zerubbabel -- Hashubah, Ohel, Berechiah, Hasadiah, and Jushabhesed. The Davidic line persists into the post-exilic generation; the promise has not died."
    },
    "21": {
      "L": "And the sons of Hananiah: Pelatiah and Jeshaiah; the sons of Rephaiah, the sons of Arnan, the sons of Obadiah, the sons of Shechaniah.",
      "M": "The sons of Hananiah: Pelatiah and Jeshaiah; then the sons of Rephaiah, the sons of Arnan, the sons of Obadiah, the sons of Shechaniah.",
      "T": "The post-exilic Davidic line branches further: Hananiah's sons -- Pelatiah and Jeshaiah -- and the lines of Rephaiah, Arnan, Obadiah, and Shechaniah. The Chronicler looks forward; restoration remains possible."
    },
    "22": {
      "L": "And the son of Shechaniah: Shemaiah. And the sons of Shemaiah: Hattush, Igeal, Bariah, Neariah, and Shaphat -- six.",
      "M": "The son of Shechaniah: Shemaiah. The sons of Shemaiah: Hattush, Igeal, Bariah, Neariah, and Shaphat -- six.",
      "T": "Shechaniah fathered Shemaiah, who fathered six sons including Hattush -- a name that appears in the return from exile under Ezra, suggesting these were not just names but living contemporaries of the Chronicler."
    },
    "23": {
      "L": "And the sons of Neariah: Elioenai, Hezekiah, and Azrikam -- three.",
      "M": "The sons of Neariah: Elioenai, Hezekiah, and Azrikam -- three.",
      "T": "Neariah's three sons -- Elioenai, Hezekiah, Azrikam -- generations removed from the exile, yet still enrolled in the Davidic register."
    },
    "24": {
      "L": "And the sons of Elioenai: Hodaviah, Eliashib, Pelaiah, Akkub, Johanan, Delaiah, and Anani -- seven.",
      "M": "The sons of Elioenai: Hodaviah, Eliashib, Pelaiah, Akkub, Johanan, Delaiah, and Anani -- seven.",
      "T": "Seven sons of Elioenai close the genealogy -- Hodaviah, Eliashib, Pelaiah, Akkub, Johanan, Delaiah, and Anani. The Davidic line extends to the Chronicler's own day. God's covenant with David has not been abandoned; the dynasty lives, awaiting its fulfilment."
    }
  },
  "4": {
    "1": {
      "L": "The sons of Judah: Perez, Hezron, Carmi, Hur, and Shobal.",
      "M": "The sons of Judah: Perez, Hezron, Carmi, Hur, and Shobal.",
      "T": "The Chronicler returns to Judah with a second genealogical sweep, gathering threads not covered in chapter 2: Perez, Hezron, Carmi, Hur, and Shobal."
    },
    "2": {
      "L": "And Reaiah the son of Shobal begot Jahath, and Jahath begot Ahumai and Lahad. These are the families of the Zorathites.",
      "M": "Reaiah son of Shobal fathered Jahath, and Jahath fathered Ahumai and Lahad. These were the clans of the Zorathites.",
      "T": "Shobal's line: Reaiah fathered Jahath, who fathered Ahumai and Lahad -- the founding clans of Zorah, the birthplace of Samson."
    },
    "3": {
      "L": "And these were of the father of Etam: Jezreel, Ishma, and Idbash; and the name of their sister was Hazelelponi.",
      "M": "These were the sons of the father of Etam: Jezreel, Ishma, and Idbash. Their sister was named Hazelelponi.",
      "T": "The founder of Etam had sons Jezreel, Ishma, and Idbash; their sister Hazelelponi is named -- one of only a handful of women remembered by name in these genealogies."
    },
    "4": {
      "L": "And Penuel was the father of Gedor, and Ezer was the father of Hushah. These are the sons of Hur, the firstborn of Ephrathah, the father of Bethlehem.",
      "M": "Penuel was the founder of Gedor, and Ezer was the founder of Hushah. These were the sons of Hur, the firstborn of Ephrathah and the founder of Bethlehem.",
      "T": "Penuel founded Gedor; Ezer founded Hushah. These descended from Hur, Ephrathah's firstborn -- the line that connects back through Caleb to the Bethlehem where David would be born."
    },
    "5": {
      "L": "And Ashhur the father of Tekoa had two wives, Helah and Naarah.",
      "M": "Ashhur the founder of Tekoa had two wives, Helah and Naarah.",
      "T": "Ashhur, who founded Tekoa, had two wives -- Helah and Naarah."
    },
    "6": {
      "L": "And Naarah bore him Ahuzzam, Hepher, Temeni, and Haahashtari. These were the sons of Naarah.",
      "M": "Naarah bore him Ahuzzam, Hepher, Temeni, and Haahashtari. These were Naarah's sons.",
      "T": "Naarah bore four sons -- Ahuzzam, Hepher, Temeni, and Haahashtari -- to carry Tekoa's heritage."
    },
    "7": {
      "L": "And the sons of Helah: Zereth, Izhar, and Ethnan.",
      "M": "The sons of Helah: Zereth, Izhar, and Ethnan.",
      "T": "Helah bore Zereth, Izhar, and Ethnan -- the second branch of Ashhur's family."
    },
    "8": {
      "L": "And Koz begot Anub and Zobebah, and the families of Aharhel the son of Harum.",
      "M": "Koz fathered Anub and Zobebah, and the clans of Aharhel son of Harum.",
      "T": "Koz fathered Anub and Zobebah, and his descendants included the clans of Aharhel son of Harum."
    },
    "9": {
      "L": "And Jabez was more honoured than his brothers; and his mother had called his name Jabez, saying, Because I bore him in sorrow.",
      "M": "Jabez was more honoured than his brothers. His mother had named him Jabez, saying, 'I gave birth to him in pain.'",
      "T": "Jabez stood above his brothers in honour, yet carried a wound in his very name. His mother named him Jabez -- 'pain-bearer' -- at the moment of his birth: 'I bore him in sorrow.' A name that was a mark before it was ever a hope."
    },
    "10": {
      "L": "And Jabez called on the God of Israel, saying, Oh that you would bless me and enlarge my border, and that your hand might be with me, and that you would keep me from evil so that it does not grieve me! And God granted what he asked.",
      "M": "Jabez called on the God of Israel: 'Oh, that you would bless me and enlarge my territory! Let your hand be with me, and keep me from evil, so that I will be free from pain.' And God granted his request.",
      "T": "Jabez prayed to the God of Israel: 'Truly bless me -- expand my horizons. Keep your hand on me and guard me from evil, so that the sorrow that named me never defines me.' The prayer is brief, bold, and rooted in covenant trust. The root word for pain echoes his own name -- he is praying to be freed from the very thing he was called. God answered: yes."
    },
    "11": {
      "L": "And Chelub the brother of Shuah begot Mehir, who was the father of Eshton.",
      "M": "Chelub, Shuah's brother, fathered Mehir, who was the father of Eshton.",
      "T": "Chelub brother of Shuah fathered Mehir, who fathered Eshton."
    },
    "12": {
      "L": "And Eshton begot Beth-rapha, Paseah, and Tehinnah the father of Ir-nahash. These are the men of Recah.",
      "M": "Eshton fathered Beth-rapha, Paseah, and Tehinnah the founder of Ir-nahash. These were the men of Recah.",
      "T": "Eshton fathered Beth-rapha, Paseah, and Tehinnah who founded Ir-nahash. These are the men of Recah -- a place not otherwise located, their identity preserved here alone."
    },
    "13": {
      "L": "And the sons of Kenaz: Othniel and Seraiah; and the sons of Othniel: Hathath and Meonothai.",
      "M": "The sons of Kenaz: Othniel and Seraiah. The sons of Othniel: Hathath and Meonothai.",
      "T": "Kenaz's sons include Othniel -- the first judge of Israel, who delivered the nation from Cushan-rishathaim. His sons were Hathath and Meonothai; his legacy was liberation."
    },
    "14": {
      "L": "And Meonothai begot Ophrah; and Seraiah begot Joab the father of Ge-harashim, for they were craftsmen.",
      "M": "Meonothai fathered Ophrah; and Seraiah fathered Joab the founder of Ge-harashim, for they were craftsmen.",
      "T": "Meonothai fathered Ophrah; Seraiah fathered Joab, who founded Ge-harashim -- 'the valley of craftsmen' -- a guild community whose identity as skilled workers became their lasting legacy."
    },
    "15": {
      "L": "And the sons of Caleb the son of Jephunneh: Iru, Elah, and Naam; and the son of Elah: Kenaz.",
      "M": "The sons of Caleb son of Jephunneh: Iru, Elah, and Naam. The son of Elah: Kenaz.",
      "T": "The famous Caleb son of Jephunneh -- the faithful spy who wholly followed the LORD -- had sons Iru, Elah, and Naam. Elah's son Kenaz carries the family name into the next generation."
    },
    "16": {
      "L": "And the sons of Jehallelel: Ziph, Ziphah, Tiria, and Asarel.",
      "M": "The sons of Jehallelel: Ziph, Ziphah, Tiria, and Asarel.",
      "T": "Jehallelel's sons -- Ziph, Ziphah, Tiria, and Asarel -- the clans of the Ziphites, in whose hill country David once sheltered from Saul."
    },
    "17": {
      "L": "And the sons of Ezrah: Jether, Mered, Epher, and Jalon; and Mered's wife bore Miriam, Shammai, and Ishbah the father of Eshtemoa.",
      "M": "The sons of Ezrah: Jether, Mered, Epher, and Jalon. Mered fathered Miriam, Shammai, and Ishbah the founder of Eshtemoa.",
      "T": "Ezrah's sons -- Jether, Mered, Epher, and Jalon. Mered's wife bore Miriam (a daughter named like Moses' sister), Shammai, and Ishbah who founded Eshtemoa."
    },
    "18": {
      "L": "And his Jewish wife bore Jered the father of Gedor, Heber the father of Socho, and Jekuthiel the father of Zanoah. And these are the sons of Bithiah the daughter of Pharaoh, whom Mered took.",
      "M": "His Jewish wife bore Jered the founder of Gedor, Heber the founder of Socho, and Jekuthiel the founder of Zanoah. These are the sons of Bithiah the daughter of Pharaoh, whom Mered had taken as wife.",
      "T": "Mered's Jewish wife bore three town-founders: Jered (Gedor), Heber (Socho), and Jekuthiel (Zanoah). His other wife was Bithiah, daughter of Pharaoh -- an Egyptian princess embedded in Judah's genealogy, mirroring Jarha the Egyptian slave in chapter 2. Both outsiders became insiders through covenant family."
    },
    "19": {
      "L": "And the sons of the wife of Hodiah, the sister of Naham, were the father of Keilah the Garmite, and Eshtemoa the Maachathite.",
      "M": "The sons of Hodiah's wife, sister of Naham: the founder of Keilah the Garmite settlement, and Eshtemoa the Maachathite.",
      "T": "Hodiah's wife -- sister of Naham -- bore the founders of Keilah and Eshtemoa, placing those towns in Judah's genealogical network."
    },
    "20": {
      "L": "And the sons of Shimon: Amnon, Rinnah, Ben-hanan, and Tilon. And the sons of Ishi: Zoheth and Ben-zoheth.",
      "M": "The sons of Shimon: Amnon, Rinnah, Ben-hanan, and Tilon. The sons of Ishi: Zoheth and Ben-zoheth.",
      "T": "Shimon's sons -- Amnon, Rinnah, Ben-hanan, and Tilon; Ishi's sons -- Zoheth and Ben-zoheth."
    },
    "21": {
      "L": "The sons of Shelah the son of Judah: Er the father of Lecah, and Laadah the father of Mareshah, and the families of the house of linen workers at Beth-ashbea,",
      "M": "The sons of Shelah son of Judah: Er the founder of Lecah, Laadah the founder of Mareshah, and the clans of the linen-workers' guild at Beth-ashbea,",
      "T": "Judah's third line through Shelah: Er founded Lecah, Laadah founded Mareshah, and the linen-workers' guild at Beth-ashbea preserved their Judaean lineage through their craft."
    },
    "22": {
      "L": "and Jokim, and the men of Chozeba, and Joash, and Saraph, who ruled in Moab and returned to Lehem. Now these records are ancient.",
      "M": "and Jokim, the men of Chozeba, Joash, and Saraph, who once ruled in Moab but later returned to Bethlehem. These are ancient records.",
      "T": "-- and Jokim, the men of Chozeba, Joash, and Saraph -- men who held authority in Moab at some earlier time before returning to Bethlehem. The Chronicler adds his own note: 'these are ancient records' -- an appeal to a venerable tradition no longer fully traceable."
    },
    "23": {
      "L": "These were the potters and those who dwelt among plants and hedges; they dwelt there with the king for his work.",
      "M": "These were the potters living among the farms and gardens; they lived there in the king's service.",
      "T": "Royal craftsmen -- potters living amid the cultivated gardens and hedgerows, in service to the crown. Another professional guild embedded in Judah's memory, their identity as skilled workers outlasting their individual names."
    },
    "24": {
      "L": "The sons of Simeon: Nemuel, Jamin, Jarib, Zerah, and Shaul;",
      "M": "The sons of Simeon: Nemuel, Jamin, Jarib, Zerah, and Shaul;",
      "T": "The Chronicler turns south to Simeon -- the tribe whose territory lay inside Judah's, its identity absorbed into the larger tribe. Simeon's five sons: Nemuel, Jamin, Jarib, Zerah, and Shaul --"
    },
    "25": {
      "L": "Shallum his son, Mibsam his son, Mishma his son.",
      "M": "his son Shallum, his son Mibsam, his son Mishma.",
      "T": "-- Shaul's descending line: Shallum, Mibsam, Mishma."
    },
    "26": {
      "L": "And the sons of Mishma: Hamuel his son, Zaccur his son, Shimei his son.",
      "M": "The sons of Mishma: Hamuel his son, Zaccur his son, Shimei his son.",
      "T": "Mishma's line continued: Hamuel, Zaccur, Shimei."
    },
    "27": {
      "L": "And Shimei had sixteen sons and six daughters; but his brothers did not have many children, nor did all their clan multiply like the sons of Judah.",
      "M": "Shimei had sixteen sons and six daughters, but his brothers did not multiply greatly, and their whole clan did not increase as much as the sons of Judah.",
      "T": "Shimei had sixteen sons and six daughters -- an unusually large family -- yet even this could not offset Simeon's diminishment as a tribe. Jacob's darkest blessing had come true: Simeon was scattered within Israel."
    },
    "28": {
      "L": "And they dwelt at Beer-sheba, Moladah, and Hazar-shual,",
      "M": "They settled at Beer-sheba, Moladah, and Hazar-shual,",
      "T": "Simeon's settlements within Judah's territory: Beer-sheba -- the ancient covenant-city of Abraham and Isaac -- Moladah, and Hazar-shual,"
    },
    "29": {
      "L": "at Bilhah, at Ezem, and at Tolad,",
      "M": "at Bilhah, Ezem, and Tolad,",
      "T": "Bilhah, Ezem, and Tolad --"
    },
    "30": {
      "L": "and at Bethuel, at Hormah, and at Ziklag,",
      "M": "at Bethuel, Hormah, and Ziklag,",
      "T": "-- Bethuel, Hormah, and Ziklag, the city that would later become David's refuge during his outlaw years,"
    },
    "31": {
      "L": "at Beth-marcaboth, Hazar-susim, Beth-biri, and Shaaraim. These were their cities until the reign of David.",
      "M": "at Beth-marcaboth, Hazar-susim, Beth-biri, and Shaaraim. These were their cities until the time of David.",
      "T": "-- Beth-marcaboth, Hazar-susim, Beth-biri, and Shaaraim. These were Simeon's towns until David's reign reorganised the tribal territories."
    },
    "32": {
      "L": "And their five villages were Etam, Ain, Rimmon, Tochen, and Ashan --",
      "M": "Their five villages: Etam, Ain, Rimmon, Tochen, and Ashan --",
      "T": "Five villages: Etam, Ain, Rimmon, Tochen, and Ashan --"
    },
    "33": {
      "L": "and all their villages that were around these cities as far as Baal. These are their settlements, and they kept their genealogy.",
      "M": "and all the villages surrounding these cities as far as Baal. These were their settlements; they maintained their genealogical records.",
      "T": "-- and all the surrounding villages as far as Baal. These settlements and their genealogies were carefully kept. Even a diminished tribe preserves its identity in writing."
    },
    "34": {
      "L": "And Meshobab, Jamlech, and Joshah the son of Amaziah,",
      "M": "Meshobab, Jamlech, and Joshah son of Amaziah,",
      "T": "Among Simeon's later princes: Meshobab, Jamlech, Joshah son of Amaziah,"
    },
    "35": {
      "L": "and Joel and Jehu the son of Joshibiah, the son of Seraiah, the son of Asiel,",
      "M": "Joel and Jehu son of Joshibiah, son of Seraiah, son of Asiel,",
      "T": "Joel and Jehu, whose lineage ran Joshibiah -- Seraiah -- Asiel,"
    },
    "36": {
      "L": "and Elioenai, Jaakobah, Jeshohaiah, Asaiah, Adiel, Jesimiel, and Benaiah,",
      "M": "and Elioenai, Jaakobah, Jeshohaiah, Asaiah, Adiel, Jesimiel, and Benaiah,",
      "T": "and Elioenai, Jaakobah, Jeshohaiah, Asaiah, Adiel, Jesimiel, and Benaiah --"
    },
    "37": {
      "L": "and Ziza the son of Shiphi, the son of Allon, the son of Jedaiah, the son of Shimri, the son of Shemaiah --",
      "M": "and Ziza son of Shiphi, son of Allon, son of Jedaiah, son of Shimri, son of Shemaiah --",
      "T": "-- and Ziza, whose lineage reached back through Shiphi, Allon, Jedaiah, Shimri, to Shemaiah."
    },
    "38": {
      "L": "these mentioned by name were princes in their families; and their fathers' houses increased greatly.",
      "M": "These men, listed by name, were leaders of their clans, and their families grew greatly in number.",
      "T": "These named men were princes of their clans -- men of standing whose families multiplied, a late flourishing for the diminished tribe."
    },
    "39": {
      "L": "And they went to the entrance of Gedor, to the east side of the valley, to seek pasture for their flocks.",
      "M": "They journeyed to the entrance of Gedor, toward the eastern side of the valley, to find pasture for their flocks.",
      "T": "They migrated east toward Gedor's valley in search of grazing land -- shepherds following their flocks to open country."
    },
    "40": {
      "L": "And they found rich and good pasture, and the land was broad and quiet and peaceable; for those who had lived there before were of Ham.",
      "M": "There they found rich, good pasture in a broad, peaceful, undisturbed land. Its former inhabitants were of Hamite descent.",
      "T": "The land they found was rich and wide, peaceful and quiet -- previously held by Hamites with no claim to the covenant territory. The Simeonites saw an opportunity."
    },
    "41": {
      "L": "And these, written by name, came in the days of Hezekiah king of Judah, and attacked their tents and the Meunim who were found there, and devoted them to destruction to this day, and dwelt in their place, because there was pasture there for their flocks.",
      "M": "These men, listed by name, came in the days of Hezekiah king of Judah. They attacked and destroyed the settlements and the Meunim who were found there, devoting them to destruction, as remains the case to this day. They settled there, for the pasture was good for their flocks.",
      "T": "In Hezekiah's reign these Simeonite leaders made their move -- striking the Meunim encampments, destroying them utterly. The Chronicler notes it holds 'to this day.' What looks like opportunism is framed as territorial reclamation within the pattern of Israel's wider settlement."
    },
    "42": {
      "L": "And some of them, five hundred men of the sons of Simeon, went to Mount Seir, having as their leaders Pelatiah, Neariah, Rephaiah, and Uzziel, the sons of Ishi.",
      "M": "A group of five hundred Simeonites went to Mount Seir, led by Pelatiah, Neariah, Rephaiah, and Uzziel, the sons of Ishi.",
      "T": "Five hundred Simeonites -- led by Ishi's four sons, Pelatiah, Neariah, Rephaiah, and Uzziel -- pushed south into Mount Seir, Edom's ancestral heartland, seeking further territory."
    },
    "43": {
      "L": "And they struck the remnant of the Amalekites who had escaped, and they have dwelt there to this day.",
      "M": "They struck down the remaining Amalekites who had escaped, and have lived there to this day.",
      "T": "There they finished off the surviving Amalekites -- the remnant of Israel's perpetual enemy, traced back in chapter 1 to Esau's grandson. The unfinished business of the conquest is completed here, quietly, at the margins of history, by a diminished tribe pursuing its flocks."
    }
  },
  "5": {
    "1": {
      "L": "Now the sons of Reuben the firstborn of Israel (for he was the firstborn; but because he defiled his father's bed, his birthright was given to the sons of Joseph the son of Israel, so that he is not enrolled in the genealogy according to the birthright);",
      "M": "The sons of Reuben the firstborn of Israel. Though Reuben was the firstborn, he defiled his father's bed; therefore his birthright was given to the sons of Joseph son of Israel. He is not listed first in the genealogy by birthright.",
      "T": "Reuben was Jacob's firstborn -- but he forfeited his birthright by sleeping with Bilhah, his father's concubine. The double portion of land passed to Joseph's sons instead. The Chronicler explains this openly so readers understand why Judah, not Reuben, carries the royal line."
    },
    "2": {
      "L": "though Judah prevailed over his brothers, and the chief came from him, yet the birthright was Joseph's --",
      "M": "Though Judah prevailed among his brothers, and the ruler came from him, the birthright itself belonged to Joseph --",
      "T": "A careful distinction: Judah's supremacy is leadership -- the sceptre, the king. Joseph's claim is the double portion of land. Both streams of Jacob's blessing flow, but they flow through different channels."
    },
    "3": {
      "L": "the sons of Reuben, the firstborn of Israel: Hanoch, Pallu, Hezron, and Carmi.",
      "M": "the sons of Reuben, the firstborn of Israel: Hanoch, Pallu, Hezron, and Carmi.",
      "T": "Reuben's four sons -- Hanoch, Pallu, Hezron, and Carmi -- the founding clans of the tribe that settled east of the Jordan."
    },
    "4": {
      "L": "The sons of Joel: Shemaiah his son, Gog his son, Shimei his son,",
      "M": "The sons of Joel: his son Shemaiah, his son Gog, his son Shimei,",
      "T": "Joel's Reubenite descent: Shemaiah, Gog, Shimei --"
    },
    "5": {
      "L": "Micah his son, Reaiah his son, Baal his son,",
      "M": "his son Micah, his son Reaiah, his son Baal,",
      "T": "-- Micah, Reaiah, Baal --"
    },
    "6": {
      "L": "Beerah his son, whom Tilgath-pilneser king of Assyria carried away into exile. He was a prince of the Reubenites.",
      "M": "and his son Beerah, whom Tilgath-pilneser king of Assyria took into exile. He was a leader of the Reubenites.",
      "T": "-- and Beerah, the last named. He was a prince of the Reubenites -- and Tiglath-pileser III carried him into Assyrian exile. A genealogy that ends in deportation, the tribe swallowed by empire."
    },
    "7": {
      "L": "And his kinsmen by their clans, when the genealogy was registered according to their generations: the chief Jeiel, and Zechariah,",
      "M": "His relatives, listed by clan in their genealogical records: Jeiel the chief and Zechariah,",
      "T": "The wider Reubenite register lists Jeiel the clan-chief and Zechariah -- leaders who persisted after Beerah's deportation."
    },
    "8": {
      "L": "and Bela the son of Azaz, the son of Shema, the son of Joel, who dwelt in Aroer, as far as Nebo and Baal-meon.",
      "M": "and Bela son of Azaz, son of Shema, son of Joel, who lived in Aroer as far as Nebo and Baal-meon.",
      "T": "Bela son of Azaz held territory from Aroer to Nebo and Baal-meon -- the Reubenite plateau east of the Dead Sea, the land Moses himself had viewed from Nebo."
    },
    "9": {
      "L": "And he settled to the east as far as the beginning of the desert from the river Euphrates, because their livestock had multiplied in the land of Gilead.",
      "M": "He settled eastward as far as the edge of the desert at the Euphrates, because their livestock had multiplied in the land of Gilead.",
      "T": "Reuben's clans expanded eastward to the Euphrates fringe -- not conquest but pasture, their flocks driving them to the far reaches of the Gilead plateau."
    },
    "10": {
      "L": "And in the days of Saul they waged war against the Hagrites, who fell by their hand; and they dwelt in their tents throughout all the area east of Gilead.",
      "M": "In the days of Saul they made war against the Hagrites, who were defeated; and the Reubenites settled in their tents throughout the entire region east of Gilead.",
      "T": "In Saul's time Reuben went to war against the Hagrites and won, occupying their encampments across eastern Gilead. Military success here, before the theological failure noted later."
    },
    "11": {
      "L": "The sons of Gad dwelt opposite them in the land of Bashan as far as Salecah:",
      "M": "The sons of Gad lived opposite them in the land of Bashan as far as Salecah.",
      "T": "Next: Gad. Gad's territory stretched across the Jordan in Bashan up to Salecah -- the northern edge of the Transjordanian plateau, a land of rich soil and wide skies."
    },
    "12": {
      "L": "Joel the chief, Shapham the second, then Janai and Shaphat in Bashan.",
      "M": "Joel was chief, Shapham second, then Janai and Shaphat in Bashan.",
      "T": "Gad's four tribal leaders in Bashan: Joel chief, Shapham second, Janai and Shaphat."
    },
    "13": {
      "L": "And their kinsmen by their fathers' houses: Michael, Meshullam, Sheba, Jorai, Jacan, Zia, and Eber -- seven.",
      "M": "Their relatives by family: Michael, Meshullam, Sheba, Jorai, Jacan, Zia, and Eber -- seven in all.",
      "T": "Seven clan-heads: Michael, Meshullam, Sheba, Jorai, Jacan, Zia, and Eber -- the full council of Gad's tribal leadership."
    },
    "14": {
      "L": "These were the sons of Abihail the son of Huri, the son of Jaroah, the son of Gilead, the son of Michael, the son of Jeshishai, the son of Jahdo, the son of Buz.",
      "M": "These were sons of Abihail son of Huri, son of Jaroah, son of Gilead, son of Michael, son of Jeshishai, son of Jahdo, son of Buz.",
      "T": "Their lineage traced eight generations back to Buz -- through Jahdo, Jeshishai, Michael, Gilead, Jaroah, Huri, to Abihail. Deep roots anchoring the Gadite claim to Bashan."
    },
    "15": {
      "L": "Ahi the son of Abdiel, the son of Guni, was chief of their fathers' house.",
      "M": "Ahi son of Abdiel, son of Guni, was the head of their family.",
      "T": "The family head was Ahi son of Abdiel, whose grandfather Guni gave the clan its deepest ancestral identity."
    },
    "16": {
      "L": "And they dwelt in Gilead, in Bashan and its towns, and in all the pasturelands of Sharon to their borders.",
      "M": "They lived in Gilead, in Bashan and its towns, and throughout the pasturelands of Sharon to their borders.",
      "T": "Gad's holdings stretched across Gilead and Bashan with its towns, and the Sharon pasturelands along the borders -- a wide, fertile trans-Jordan territory."
    },
    "17": {
      "L": "All of these were registered by genealogies in the days of Jotham king of Judah and in the days of Jeroboam king of Israel.",
      "M": "All of these were enrolled by genealogy during the days of Jotham king of Judah and Jeroboam king of Israel.",
      "T": "The Gadite register was formalised in the reigns of Jotham of Judah and Jeroboam II of Israel -- a mid-eighth-century dating, a generation before the Assyrian storm swept the east."
    },
    "18": {
      "L": "The sons of Reuben, the Gadites, and the half-tribe of Manasseh had valiant men who carried shield and sword and drew the bow, trained in battle -- forty-four thousand seven hundred and sixty, fit for warfare.",
      "M": "The Reubenites, Gadites, and half-tribe of Manasseh fielded forty-four thousand seven hundred and sixty skilled warriors -- men trained in battle who bore shield, sword, and bow.",
      "T": "Together the three Transjordanian tribes could field 44,760 trained warriors -- an army of shield-bearers, swordsmen, and archers. A significant military force on Israel's eastern frontier."
    },
    "19": {
      "L": "And they waged war against the Hagrites, Jetur, Naphish, and Nodab.",
      "M": "They went to war against the Hagrites, Jetur, Naphish, and Nodab.",
      "T": "The three tribes fought a coalition of eastern peoples -- the Hagrites and the Ishmaelite-descended tribes of Jetur, Naphish, and Nodab."
    },
    "20": {
      "L": "And they were helped against them, and the Hagrites and all who were with them were given into their hand, because they cried out to God in battle, and he answered their plea, because they trusted in him.",
      "M": "They were helped against these enemies; the Hagrites and all who were with them were handed over to them, because they cried to God during the battle, and he answered them because they trusted in him.",
      "T": "The decisive factor was not numbers but prayer. They cried out to God in the middle of the battle, and he answered -- because they trusted him. The Chronicler's theology is clear: victory is God's gift to those who depend on him, not a reward for military superiority."
    },
    "21": {
      "L": "And they carried off their livestock: fifty thousand camels, two hundred fifty thousand sheep, two thousand donkeys, and one hundred thousand persons.",
      "M": "They took the livestock: fifty thousand camels, two hundred fifty thousand sheep, two thousand donkeys, and one hundred thousand prisoners.",
      "T": "The spoils were vast -- 50,000 camels, 250,000 sheep, 2,000 donkeys, and 100,000 captives. Total military and economic victory on the eastern frontier, the reward of faith-driven warfare."
    },
    "22": {
      "L": "For many fell slain, because the war was from God. And they dwelt in their place until the exile.",
      "M": "Many fell in battle, for the war was God's doing. The Israelites settled in their territory until the exile.",
      "T": "Many fell, for 'the war was from God' -- a phrase that frames this campaign as divinely directed, not merely human aggression. They held the land until the Assyrian exile swept them away. Faithfulness brought the land; unfaithfulness would cost it."
    },
    "23": {
      "L": "The members of the half-tribe of Manasseh dwelt in the land; they spread from Bashan to Baal-hermon, Senir, and Mount Hermon.",
      "M": "The people of the half-tribe of Manasseh lived in the land, extending from Bashan to Baal-hermon, Senir, and Mount Hermon.",
      "T": "The half-tribe of Manasseh occupied the northern Transjordan -- from Bashan up to Baal-hermon, Senir (the Amorite name for Hermon), and the great mountain itself. A wide and elevated territory."
    },
    "24": {
      "L": "These were the heads of their fathers' houses: Epher, Ishi, Eliel, Azriel, Jeremiah, Hodaviah, and Jahdiel -- mighty warriors, famous men, heads of their fathers' houses.",
      "M": "These were the heads of their clans: Epher, Ishi, Eliel, Azriel, Jeremiah, Hodaviah, and Jahdiel -- mighty men of valour, famous men, heads of their families.",
      "T": "Seven clan-heads of eastern Manasseh: Epher, Ishi, Eliel, Azriel, Jeremiah, Hodaviah, and Jahdiel -- warriors of renown, each the anchor of a family. Their names are preserved because their deeds were remembered."
    },
    "25": {
      "L": "But they broke faith with the God of their fathers and whored after the gods of the peoples of the land, whom God had destroyed before them.",
      "M": "But they were unfaithful to the God of their fathers and prostituted themselves to the gods of the peoples of the land -- the very peoples God had destroyed to make room for them.",
      "T": "Yet they betrayed the God who gave them the land. They turned to the gods of the peoples God had driven out before them -- worshipping in the emptied shrines of a defeated culture. The Chronicler's verdict is devastating in its irony: they served the gods of the dispossessed."
    },
    "26": {
      "L": "So the God of Israel stirred up the spirit of Pul king of Assyria, and the spirit of Tilgath-pilneser king of Assyria, and he carried them away -- the Reubenites, the Gadites, and the half-tribe of Manasseh -- and brought them to Halah, Habor, Hara, and the river of Gozan, to this day.",
      "M": "So the God of Israel stirred up the spirit of Pul king of Assyria -- that is, Tilgath-pilneser king of Assyria -- and he exiled the Reubenites, the Gadites, and the half-tribe of Manasseh, bringing them to Halah, Habor, Hara, and the Gozan River, where they remain to this day.",
      "T": "God himself moved Assyria. Pul -- Tiglath-pileser III -- was the instrument, not the cause. The three faithful-turned-faithless Transjordanian tribes were swept into exile: Halah, Habor, Hara, the Gozan River. They are 'there to this day,' the Chronicler notes -- still in Assyria, still not home. The arc of these five chapters bends from Adam to exile: all humanity, narrowed to Israel, narrowed to Judah and its hope -- while those who forgot the covenant were scattered."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '1chronicles')
        merge_tier(existing, CHRONICLES1, tier_key)
        save(tier_dir, '1chronicles', existing)
    print('1 Chronicles 1-5 written.')

if __name__ == '__main__':
    main()
