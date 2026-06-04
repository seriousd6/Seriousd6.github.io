"""
MKT 1 Chronicles chapters 26–28 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-1chronicles-26-28.py

Content:
- Ch 26: Divisions of the gatekeepers (vv.1–19), Levitical treasurers (vv.20–28),
          Levites for outward business as officers and judges (vv.29–32)
- Ch 27: Twelve monthly military divisions of 24,000 each (vv.1–15), tribal officers (vv.16–22),
          note on the uncompleted census (vv.23–24), royal property stewards (vv.25–31),
          royal counselors (vv.32–34)
- Ch 28: David's public farewell assembly — his disqualification, God's choice of Solomon,
          the transfer of the temple plans, and his personal charge to Solomon

Translation decisions:
- H3068 (יהוה): "LORD" in L/M; "the LORD" in T. Consistent with all prior 1 Chronicles scripts.
- H430 (אֱלֹהִים): "God" throughout all tiers. In 28:20, "the LORD God, even my God" = David's
  personal identification with the covenant name.
- H4256 (מַחְלֹקֶת, "divisions/courses"): "divisions" in ch 26 (gatekeepers organized by post);
  "divisions" in ch 27 (military rotation units). Consistent with prior OT scripts; "courses" used
  in chs 23–25 for the Levitical/priestly rotation where the calendar cycle is foregrounded.
- H7307 (רוּחַ) at 28:12: "Spirit" (capitalized) in M/T. David states the temple plans were given
  to him "by the Spirit" — this is divine architectural inspiration, not mere wind or human breath.
  The same Spirit that directed the musical prophets (ch 25) directed David's architectural vision.
  "By the Spirit he had" preserves the ambiguity of the Hebrew but capitalizing signals the agent.
- H1285 (בְּרִית, "covenant") at 28:2: "covenant" — the ark is "the ark of the covenant of the
  LORD." H727 (אָרוֹן) = "ark." Both rendered plainly in all tiers.
- H3824/H3820 (לֵבָב/לֵב, "heart/mind") at 28:2, 9: "heart" in L/M; "heart" or "intention" in T
  depending on context. Hebrew leb denotes the whole inner person (intellect + will + emotion).
- H5315 (נֶפֶשׁ) at 28:9: "mind/soul" context — "with a willing mind" uses nephesh in the extended
  sense of the self's orientation. Rendered "willing mind" in L/M to reflect H2655 (willing/
  favorable) + H5315 pairing; T surfaces the Hebraic sense of the whole-self commitment.
- H7200 (רָאָה, "seer") at 26:28: "the seer" for Samuel. Prophetic designation; consistent with
  prior usage of "the man of God" for Moses.
- H7307 at 28:12 vs H7919 at 28:19: Two separate acts of divine communication — the Spirit giving
  the plans (v12) and the LORD making David understand in writing by his hand (v19). Both are
  documented separately; v19 is a claim to written divine revelation of the architectural pattern.
- Gatekeeper theology (ch 26): The Chronicler treats gatekeeping as a sacred vocation equal in
  dignity to priestly service. "Mighty men of valor" (H1368/H2428) — normally a military term —
  is applied to gatekeeper families, signaling that threshold-guarding was an act of spiritual
  warfare: defending the boundary between holy and common.
- Lot-casting (26:13): Consistent with 24:5, 31 and 25:8 — the lot as divine assignment mechanism.
  Proverbs 16:33 applies throughout: "the lot is cast into the lap, but its every decision is from
  the LORD."
- Military rotation (ch 27, vv.1–15): 12 monthly divisions of 24,000 = 288,000 total. This matches
  the 288 trained musicians in 25:7 (12 per musical course × 24 courses). The parallelism is
  deliberate: kingdom music and kingdom warfare run on the same covenant calendar.
- David's census rebuke (27:23–24): David did not count those under 20 because the Abrahamic
  promise (Gen 15:5, 22:17) renders human counting of Israel both presumptuous and unnecessary.
  Joab began a full census (2 Sam 24 / 1 Chr 21) and incurred wrath; here David is contrasted
  favorably — he excluded the very group whose counting would have been most presumptuous.
- "Wrath came upon Israel" (27:24): Cross-reference 1 Chr 21:7–14 — the plague following David's
  census. The Chronicler does not repeat the account here but assumes the reader knows it. T notes.
- 28:4 — divine election sequence: The LORD chose Judah → chose the house of Jesse → chose David.
  Three concentric elections. T surfaces the Deuteronomic theology of covenant choice (H977, בָּחַר).
- 28:9 — "If you seek him, he will be found by you; if you forsake him, he will reject you forever":
  The most explicit father-to-son theological charge in the OT outside Deuteronomy. H5800 (forsake)
  echoes the covenant lawsuit language of the prophets. This is not advice; it is covenant warning.
- 28:19 — "the LORD made me understand in writing, by his hand upon me": An extraordinary claim —
  divine authorship of architectural plans delivered to David in written form. The temple plans were
  as much a matter of revelation as the Torah. T notes this parallel to Moses receiving the
  tabernacle pattern (Exod 25:9, 40; Heb 8:5).
- OT intertextuality: 28:20 ("He will not leave you or forsake you") echoes Deut 31:8 — Moses's
  charge to Joshua before crossing the Jordan. David casts himself as Moses passing the covenant
  commission to a younger successor. The Mosaic pattern of covenant succession shapes the scene.
- Aspect notes: Most verbs in chs 26–27 are simple past narrating completed organizational acts.
  In ch 28, David's direct speech uses second-person imperatives throughout (vv.8–10, 20) —
  commands carrying covenant force. H2388 (be strong) at 28:10, 20 is an imperative of resolve,
  not ability — the same command Joshua received (Josh 1:7, 9).
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
  "26": {
    "1": {
      "L": "Concerning the divisions of the gatekeepers: of the Korhites, Meshelemiah the son of Kore, of the sons of Asaph.",
      "M": "The divisions of the gatekeepers: from the Korhites, Meshelemiah son of Kore, from the line of Asaph.",
      "T": "The organization of worship extended to the threshold. After priests, Levitical servers, musicians, and treasurers, the Chronicler turns to the gatekeepers — the families whose sacred duty was to stand at the boundary between the holy and the common. Meshelemiah the Korhite opened the register: his family would hold the east gate, the gate of primary entry, the direction from which the divine presence approached."
    },
    "2": {
      "L": "And the sons of Meshelemiah: Zechariah the firstborn, Jediael the second, Zebadiah the third, Jathniel the fourth,",
      "M": "Meshelemiah's sons: Zechariah the firstborn, Jediael the second, Zebadiah the third, Jathniel the fourth,",
      "T": "Seven sons of Meshelemiah — a large gatekeeper family contributing multiple members to the sacred threshold rotation. The ordinal numbering signals organized service, not mere genealogy: each son held a numbered post in the division, guaranteeing that the gate was never unwatched."
    },
    "3": {
      "L": "Elam the fifth, Jehohanan the sixth, Elioenai the seventh.",
      "M": "Elam the fifth, Jehohanan the sixth, Elioenai the seventh.",
      "T": "Seven sons — a complete family unit fully enrolled in the gatekeeper service. From firstborn Zechariah to seventh-born Elioenai, all served at the sanctuary threshold. The family of Meshelemiah was not divided between sacred and ordinary callings; it was wholly committed to holding the house of God."
    },
    "4": {
      "L": "Moreover the sons of Obed-edom: Shemaiah the firstborn, Jehozabad the second, Joah the third, Sacar the fourth, Nethanel the fifth,",
      "M": "Also Obed-edom's sons: Shemaiah the firstborn, Jehozabad the second, Joah the third, Sacar the fourth, Nethanel the fifth,",
      "T": "Obed-edom — the man in whose house the ark of God had rested three months during David's first ill-fated attempt to bring it to Jerusalem (13:13–14). The LORD had blessed Obed-edom visibly during those three months; the blessing was evidently biological as well as material: eight sons registered, and the fruitfulness extended into the next generation."
    },
    "5": {
      "L": "Ammiel the sixth, Issachar the seventh, Peulthai the eighth; for God blessed him.",
      "M": "Ammiel the sixth, Issachar the seventh, Peulthai the eighth — for God had blessed Obed-edom.",
      "T": "'For God blessed him.' The Chronicler drops this note like a seal at the end of the name-list: eight sons — the number of fullness and new beginning — were the visible evidence of divine favor on the family that had hosted the ark. God's blessing had a gatekeeper's address: the house of Obed-edom became a household of sanctuary servants because the ark had rested there."
    },
    "6": {
      "L": "Also to his son Shemaiah were sons born, who ruled over their father's house, for they were mighty men of valor.",
      "M": "Shemaiah his son also had sons who led their father's household, for they were men of outstanding ability.",
      "T": "The blessing multiplied: Shemaiah not only had sons but had sons who were 'mighty men of valor' — גִּבּוֹרֵי חַיִל, the same term used for David's warriors (11:26). The language of military excellence applied to gatekeeper families is intentional: threshold-guarding was a form of holy warfare. The man who stood between the sacred and the profane needed the courage of a soldier."
    },
    "7": {
      "L": "The sons of Shemaiah: Othni, Rephael, Obed, and Elzabad, and his brothers Elihu and Semachiah, men of ability.",
      "M": "Shemaiah's sons: Othni, Rephael, Obed, and Elzabad; his kinsmen Elihu and Semachiah were also men of ability.",
      "T": "Six men from Shemaiah's extended household — sons and kinsmen alike — formed a gatekeeper unit capable of covering multiple posts. The family of Obed-edom had grown from one man housing the ark to a large, multigenerational corps of sanctuary guards. Blessing begat service; service begat more blessing."
    },
    "8": {
      "L": "All these of the sons of Obed-edom, they and their sons and their brothers, able men with strength for service — sixty-two from Obed-edom.",
      "M": "All these were of Obed-edom's line — they, their sons, and their kinsmen, sixty-two men of ability for service.",
      "T": "Sixty-two descendants of Obed-edom in the gatekeeper corps. The man who had once been the incidental resting-place of the ark had become the patriarch of one of the sanctuary's largest service families. Three months of hosting the ark had set a trajectory of covenant service that extended through three generations. The gospel of Obed-edom is this: proximity to the holy transforms the ordinary into the extraordinary."
    },
    "9": {
      "L": "And Meshelemiah had sons and brothers, able men — eighteen.",
      "M": "Meshelemiah had sons and kinsmen — eighteen men of ability.",
      "T": "Eighteen from Meshelemiah's family, sixty-two from Obed-edom's: together these two families alone furnished eighty gatekeepers. The staffing of the sacred threshold was thorough, overlapping, and rotational — the house of God would not stand unguarded at any hour."
    },
    "10": {
      "L": "Also Hosah, of the sons of Merari, had sons: Simri was the chief, for though he was not the firstborn, his father appointed him chief;",
      "M": "Hosah of the Merarites had sons: Simri was the head, for though he was not the firstborn, his father had appointed him chief.",
      "T": "Primogeniture set aside by paternal judgment — the same pattern found in the house of Jesse (David chosen over his brothers) and in Jacob over Esau. The father's authority in Israel could redirect the natural inheritance order when circumstances or character warranted. Hosah saw something in Simri that warranted the chieftainship; the record simply states it without apology."
    },
    "11": {
      "L": "Hilkiah the second, Tebaliah the third, Zechariah the fourth. All the sons and brothers of Hosah were thirteen.",
      "M": "Hilkiah the second, Tebaliah the third, Zechariah the fourth. All the sons and kinsmen of Hosah: thirteen.",
      "T": "Thirteen from Hosah's Merarite family completed the gatekeeper rosters. The three great families — Meshelemiah the Korhite, Obed-edom the Gittite, and Hosah the Merarite — between them furnished the entire corps of sanctuary guardians. The gates of God's house had more than enough able hands."
    },
    "12": {
      "L": "These divisions of the gatekeepers, even their chief men, had guard assignments in the house of the LORD, one opposite another.",
      "M": "These gatekeeper divisions, along with their leaders, were assigned posts in the LORD's house, facing one another.",
      "T": "The gatekeepers stood 'opposite one another' — the Hebrew בְּמוּל suggests pairs facing each other across a gate or entrance, the symbolic image of double guardianship: nothing passed without the awareness of both watchmen. Every gate had a pair of eyes. The divine house was not guarded by lonely sentries but by accountable pairs — a design that anticipated the principle that truth is established by two witnesses."
    },
    "13": {
      "L": "They cast lots, small and great alike, according to their fathers' houses, for each gate.",
      "M": "They cast lots for each gate, small and great alike, according to their ancestral families.",
      "T": "The lot assigned the gates. As with the priests and musicians before them, the gatekeepers did not choose their posts by seniority, preference, or family status. The divine lot determined who held which threshold. 'Small and great alike' — the most significant post and the most routine one were assigned by the same sacred mechanism. No family could claim the prime gate by privilege; God assigned it."
    },
    "14": {
      "L": "The lot for the east fell to Shelemiah. Then they cast lots for his son Zechariah, a wise counselor, and his lot came out northward.",
      "M": "The east gate fell by lot to Shelemiah. His son Zechariah, a wise counselor, drew the north gate.",
      "T": "The east gate — the primary entrance, the gate facing the sunrise, the direction of approaching glory — was assigned to Shelemiah by lot. His son Zechariah, noted specifically as 'a wise counselor,' drew the north. The north and east gates flanked the primary approach to the inner courts; these were the threshold posts requiring the most experienced minds. The lot had placed wisdom where wisdom was needed."
    },
    "15": {
      "L": "To Obed-edom the south gate, and to his sons the storehouse.",
      "M": "The south gate fell to Obed-edom, and the storehouse to his sons.",
      "T": "Obed-edom's family received the south gate and the storehouse — the gate of arrival from the city and the repository of provisions. The family that had stored the ark now stored the sanctuary's provisions. Service at the threshold and stewardship of the sanctuary's material life were given to the same household: Obed-edom's blessing extended into every corner of the sanctuary's practical functioning."
    },
    "16": {
      "L": "To Shuppim and Hosah the west gate, with the Shallecheth Gate by the ascending causeway, ward beside ward.",
      "M": "Shuppim and Hosah received the west gate, with the Shallecheth Gate at the ascending road — one guard post beside another.",
      "T": "The west gate with Shallecheth — likely the main processional exit by which worshipers descended from the sanctuary after service — was given to Shuppim and Hosah's family. The ascending causeway leading to it was the route of pilgrimage; every approaching worshiper would pass through the hands of these guardians. The guard posts stood side by side: the house of God was surrounded by vigilance from every cardinal direction."
    },
    "17": {
      "L": "Eastward were six Levites, northward four each day, southward four each day, and at the storehouse two by two.",
      "M": "Eastward: six Levites; northward: four per day; southward: four per day; at the storehouse: two at each end.",
      "T": "The staffing ratios reveal the priority of the gates. The east — the primary entrance, the gate of approaching glory — received six: the fullest complement. North and south received four each; the storehouse posts two apiece. The unequal distribution was not a slight on the lesser gates but a recognition that the east faced the direction of the divine approach and warranted the greatest vigilance."
    },
    "18": {
      "L": "At Parbar on the west: four at the road and two at Parbar.",
      "M": "At Parbar on the west side: four at the roadway and two at Parbar itself.",
      "T": "Parbar — an uncertain term, possibly a western colonnade or open court area — received six additional Levites distributed between the road approach and the structure itself. The western perimeter of the sanctuary was thoroughly covered: the road to the west gate, the gate itself, and the Parbar structure all had assigned guardians. No approach to the holy was unmonitored."
    },
    "19": {
      "L": "These are the divisions of the gatekeepers, among the sons of Kore and among the sons of Merari.",
      "M": "These were the gatekeeper divisions — from the Korahite line and from the Merarite line.",
      "T": "The gatekeeper roster closed with its organizational frame: Korahites and Merarites, two of Levi's three great branches, together staffing every threshold of the sanctuary. The third branch — Gershon — contributed the musical prophets and some treasury stewards. Between them, the three branches of Levi covered every sacred function of the permanent house of God that David was organizing."
    },
    "20": {
      "L": "And of the Levites, Ahijah was over the treasuries of the house of God and over the treasuries of the dedicated things.",
      "M": "Among the Levites, Ahijah had oversight of the treasuries of God's house and the treasuries of dedicated gifts.",
      "T": "Two distinct treasuries: the house of God's operating treasury (temple equipment, materials, provisions) and the dedicated-things treasury (gifts consecrated by rulers and warriors from their spoils of war). Ahijah served as the chief overseer of both. Sacred finance required as much integrity and precision as sacred music or sacred gatekeeping; the Levitical corps that staffed it received the same honorable naming as those who stood at the gates or played the harps."
    },
    "21": {
      "L": "The sons of Ladan — the sons of the Gershonite belonging to Ladan — the heads of the fathers' houses belonging to Ladan the Gershonite were Jehieli.",
      "M": "From the sons of Ladan — the Gershonites belonging to Ladan — the heads of ancestral families were the Jehielites.",
      "T": "The Gershonite family of Ladan contributed the treasury stewards. The genealogy is careful: within the broader Gershonite clan, it was specifically the Ladan sub-clan whose heads, the Jehielites, held responsibility for the sacred finances. The right family, the right branch, the right sub-family — the organizational precision of Israel's temple service was remarkable in its detail."
    },
    "22": {
      "L": "The sons of Jehieli, Zetham and Joel his brother, were over the treasuries of the house of the LORD.",
      "M": "The sons of Jehiel — Zetham and his brother Joel — had oversight of the treasuries of the LORD's house.",
      "T": "Two brothers, Zetham and Joel, jointly superintended the primary temple treasury. The partnership model appears again: two Levites, accountable to each other, managing the material resources of the sanctuary. The treasury of the LORD was not in the hands of one unsupervised person but of a verified pair whose relationship as brothers made mutual accountability natural."
    },
    "23": {
      "L": "Of the Amramites, the Izharites, the Hebronites, and the Uzzielites:",
      "M": "Also from the Amramites, Izharites, Hebronites, and Uzzielites:",
      "T": "The four Kohathite sub-clans — all descending from Kohath son of Levi — contributed to the treasury stewardship. The same families organized for priestly service (Aaron from Amram), Levitical ministry, and musical prophecy were now also enrolled in the material stewardship of the sanctuary. Every branch of the covenant people contributed to maintaining God's house."
    },
    "24": {
      "L": "Shebuel the son of Gershom, the son of Moses, was chief officer over the treasuries.",
      "M": "Shebuel son of Gershom, son of Moses, was the chief official over the treasuries.",
      "T": "Moses's grandson as chief treasurer. The great lawgiver's family was excluded from the high priesthood — that belonged to Aaron's sons — but Moses's line was given a position of distinguished Levitical honor: oversight of the sanctuary's central treasury. The covenant honor belonging to Moses flowed to his descendants in a different channel than Aaron's honor but was honor nonetheless."
    },
    "25": {
      "L": "And his relatives through Eliezer: Rehabiah his son, Jeshaiah his son, Joram his son, Zichri his son, and Shelomith his son.",
      "M": "His relatives through Eliezer: Rehabiah, then Jeshaiah, then Joram, then Zichri, then Shelomith.",
      "T": "Five generations traced from Eliezer son of Moses down to Shelomith — a genealogy that anchored Shelomith's authority in the deepest possible roots. He was not an appointment of convenience but the fifth-generation heir of a Mosaic line that the Chronicler documented with full deliberateness. Treasury stewardship in Israel was a matter of family vocation as much as sacred music or priestly service."
    },
    "26": {
      "L": "This Shelomith and his brothers were over all the treasuries of the dedicated things which King David, the heads of the fathers' houses, the commanders of thousands and hundreds, and the commanders of the army had dedicated.",
      "M": "This Shelomith and his kinsmen oversaw all the treasuries of dedicated gifts that King David, the family heads, the military commanders of thousands and hundreds, and the army officers had consecrated.",
      "T": "Shelomith was not the treasurer of ordinary revenue but of a specific category: dedicated spoils — gifts voluntarily consecrated to God by the king and his military leaders from the wealth taken in battle. The theology of dedication ran through Israel's entire military history: when God gave victory, a portion of the victory belonged back to God. Shelomith guarded this theology in material form."
    },
    "27": {
      "L": "Out of the spoils won in battles they dedicated gifts to maintain the house of the LORD.",
      "M": "From battle spoils they had dedicated these gifts to sustain and repair the LORD's house.",
      "T": "War's fruits consecrated to the house of peace. The materials of Israel's military campaigns — the silver, gold, and goods taken in battle — were channeled into the maintenance of the sanctuary. The sword served the altar: not as a contradiction but as a covenant principle. God's victories funded God's house. The wealth of the nations flowed toward Jerusalem's sanctuary, maintaining the very place where those victories had been prayed for."
    },
    "28": {
      "L": "And whatever Samuel the seer, Saul the son of Kish, Abner the son of Ner, and Joab the son of Zeruiah had dedicated — any dedicated thing — was under the hand of Shelomith and his brothers.",
      "M": "All that Samuel the seer, Saul son of Kish, Abner son of Ner, and Joab son of Zeruiah had dedicated — whatever was a dedicated offering — was in the care of Shelomith and his kinsmen.",
      "T": "The treasury of Shelomith contained layers of history: Samuel the prophet, Saul the tragic king, Abner the soldier of divided loyalties, Joab the ruthless general — all had made dedications to God from their victories and their consciences. Men of different moral histories had consecrated things to the same sanctuary; Shelomith held them all without distinction. The treasury did not judge the donors; it honored the gifts. God received the offerings of the complicated and the faithful alike."
    },
    "29": {
      "L": "Of the Izharites, Chenaniah and his sons were for the outward work of Israel as officers and judges.",
      "M": "From the Izharites, Chenaniah and his sons handled the external affairs of Israel as officials and judges.",
      "T": "Not all Levitical service was sanctuary-based. Chenaniah's family served Israel's civil life — administering legal matters and public affairs across the nation. The Levites were Israel's administrative infrastructure as much as its liturgical corps: stationed throughout the tribal territories, they provided the educated, God-fearing judiciary and civil service that held the covenant community together outside the walls of the capital."
    },
    "30": {
      "L": "And of the Hebronites, Hashabiah and his brothers — 1,700 men of ability — were over Israel on the west side of the Jordan, for all the work of the LORD and the service of the king.",
      "M": "From the Hebronites, Hashabiah and his 1,700 capable kinsmen oversaw Israel on the west side of the Jordan for all matters relating to the LORD and the king's affairs.",
      "T": "Seventeen hundred Levites serving the western territories — a substantial civil and religious administration for the tribal areas west of the Jordan. 'All the work of the LORD and the service of the king' — the two spheres were not separated but held together by the same personnel. In Israel's covenant constitution, sacred duty and civic responsibility were not competing spheres but unified expressions of the same allegiance."
    },
    "31": {
      "L": "Among the Hebronites, Jerijah was the chief of the Hebronites according to their generations by their fathers' houses. In the fortieth year of David's reign they were sought out, and among them were found mighty men of valor at Jazer of Gilead.",
      "M": "Among the Hebronites, Jerijah was the leader, organized by the genealogies of their ancestral houses. In the fortieth year of David's reign, a search was made and mighty men of ability were found among them at Jazer in Gilead.",
      "T": "The fortieth year of David's reign — the last year of his life, when these organizational arrangements were being finalized. A formal search (H1875, the same verb used for 'seeking God') was conducted among the Hebronites in Gilead, and the result was the discovery of exceptional personnel. The organization of the kingdom was active and thorough; even in David's final year, talent was still being identified, named, and placed. The dying king was organizing for the living."
    },
    "32": {
      "L": "And his brothers were 2,700 men of ability, heads of fathers' houses, whom King David appointed over the Reubenites, the Gadites, and the half tribe of Manasseh, for every matter pertaining to God and the affairs of the king.",
      "M": "His kinsmen were 2,700 men of ability and family heads, whom King David appointed over the Reubenites, Gadites, and half tribe of Manasseh — for all matters concerning God and concerning the king.",
      "T": "Twenty-seven hundred Levites for the Transjordanian tribes — Reuben, Gad, half Manasseh — the territories east of the Jordan that were geographically separated from the sanctuary. These remote tribal communities received a proportionally larger Levitical presence to ensure that distance from Jerusalem did not mean distance from the covenant. Every matter pertaining to God and the king was covered: no Israelite community was outside the reach of the sacred administrative structure David was building."
    }
  },
  "27": {
    "1": {
      "L": "Now these are the sons of Israel, by their number, the heads of fathers' houses and the commanders of thousands and hundreds and their officers, who served the king in all matters concerning the divisions that came in and went out month by month throughout all the months of the year, each division numbering twenty-four thousand.",
      "M": "These are the Israelites organized by number — the heads of families, commanders of thousands and hundreds, and their officers — who served the king by monthly rotation throughout the year, each division numbering twenty-four thousand.",
      "T": "Israel at full military readiness: organized not for a single campaign but for permanent, rotating readiness. Twelve monthly divisions of twenty-four thousand — a standing army that never fully stood down, rotating in and out of service in a year-round cycle. The system meant the kingdom was always defended without any one portion of the nation being permanently mobilized. David had built not just an army but a sustainable military institution, a covenant force that would remain ready as long as the kingdom endured."
    },
    "2": {
      "L": "Over the first division for the first month was Jashobeam the son of Zabdiel; in his division were twenty-four thousand.",
      "M": "Jashobeam son of Zabdiel commanded the first division for the first month, with twenty-four thousand men.",
      "T": "Jashobeam opened the year. He had earlier been named as one of the Three — the elite inner circle of David's greatest warriors who had penetrated the Philistine lines to bring David water from Bethlehem's well (11:11; 2 Sam 23:8). The most storied soldier of the kingdom commanded the first course. The year began in the hands of proven valor."
    },
    "3": {
      "L": "He was of the sons of Perez, and was chief of all the commanders for the first month.",
      "M": "He was a descendant of Perez and was the senior commander for the first month.",
      "T": "Perez — the son of Judah and Tamar, the twin who thrust out his hand first and broke through (Gen 38:29). The Perezite line ran through Boaz and Ruth into the house of David himself (Ruth 4:18–22). Jashobeam's descent from Perez was not incidental: the first commander of the year was a kinsman of the king, a fellow member of Judah's most honored family line."
    },
    "4": {
      "L": "Over the division of the second month was Dodai the Ahohite; in his division was Mikloth as officer, and in his division were twenty-four thousand.",
      "M": "Dodai the Ahohite commanded the second month's division, with Mikloth as his officer and twenty-four thousand men.",
      "T": "Dodai the Ahohite — another member of the Three, whose family had produced multiple of David's most decorated warriors (2 Sam 23:9; 1 Chr 11:12). With Mikloth as his administrative officer, Dodai held the second month: February's defense of the kingdom in the hands of another proven warrior of the innermost circle."
    },
    "5": {
      "L": "The third commander, for the third month, was Benaiah the son of Jehoiada the priest, chief; and in his division were twenty-four thousand.",
      "M": "Benaiah son of Jehoiada the priest commanded the third month's division as chief, with twenty-four thousand men.",
      "T": "Benaiah the son of Jehoiada — the most personally remarkable of the Three, who had killed a lion in a pit on a snowy day and slain an Egyptian giant with the Egyptian's own spear (11:22–23). He was also a priest's son: warrior and priestly lineage combined. After Joab's execution, Benaiah would become Solomon's commander-in-chief (1 Kgs 2:35). He held the third month in the twilight of David's reign, still the formidable figure he had always been."
    },
    "6": {
      "L": "This is the Benaiah who was a mighty man of the thirty and above the thirty; and Ammizabad his son was in charge of his division.",
      "M": "This was the Benaiah who was a mighty man among the thirty and above the thirty; his son Ammizabad was in charge of his division.",
      "T": "A parenthetical note of honor: Benaiah was 'above the thirty' — a distinct category of supreme distinction that placed him alongside the Three. The text interrupts the dry military roster to honor the man; the Chronicler had a memory for greatness. Ammizabad his son administered the division — the organizational work of the third month handled by the next generation while Benaiah's legendary reputation was affirmed."
    },
    "7": {
      "L": "The fourth for the fourth month was Asahel the brother of Joab, and Zebadiah his son after him; and in his division were twenty-four thousand.",
      "M": "Asahel brother of Joab commanded the fourth month's division; after him his son Zebadiah. Their division: twenty-four thousand.",
      "T": "Asahel — the fleet-footed warrior who could not be turned from pursuing Abner and was killed for his relentlessness (2 Sam 2:18–23). He died young; his son Zebadiah inherited the fourth command. The roster carries the weight of mortality: a man listed here had already been dead for decades, his name preserved in the military record and his son carrying forward what he had begun. The covenant institution outlasted the individual."
    },
    "8": {
      "L": "The fifth for the fifth month was Shamhuth the Izrahite; and in his division were twenty-four thousand.",
      "M": "Shamhuth the Izrahite commanded the fifth month, with twenty-four thousand men.",
      "T": "Shamhuth the Izrahite — likely the Shammah of the Harodite who appears among the Thirty in 2 Samuel 23:25 (with variant spelling). The fifth month fell to a member of the broader circle of David's elite warriors. The rotating command structure drew from the full depth of Israel's military tradition."
    },
    "9": {
      "L": "The sixth for the sixth month was Ira the son of Ikkesh the Tekoite; and in his division were twenty-four thousand.",
      "M": "Ira son of Ikkesh the Tekoite commanded the sixth month, with twenty-four thousand men.",
      "T": "Ira the Tekoite — from Tekoa, the wilderness town south of Bethlehem from which the prophet Amos would later come (Amos 1:1) and whose woman had counseled David in the Absalom crisis (2 Sam 14:2). The sixth month in the hands of a soldier from the rugged south, the region of shepherds and prophets."
    },
    "10": {
      "L": "The seventh for the seventh month was Helez the Pelonite, of the sons of Ephraim; and in his division were twenty-four thousand.",
      "M": "Helez the Pelonite, from the tribe of Ephraim, commanded the seventh month, with twenty-four thousand men.",
      "T": "The seventh month — the most sacred in the Israelite calendar, containing the Day of Atonement, the Feast of Trumpets, and the Feast of Booths — was commanded by an Ephraimite. The command structure deliberately crossed tribal lines: the month of Israel's highest liturgical intensity was defended not by Judah alone but by the great central tribe of Joseph."
    },
    "11": {
      "L": "The eighth for the eighth month was Sibbecai the Hushathite, of the Zerahites; and in his division were twenty-four thousand.",
      "M": "Sibbecai the Hushathite, of the Zerahite line, commanded the eighth month, with twenty-four thousand men.",
      "T": "Sibbecai the Hushathite had distinguished himself by killing Saph the Philistine giant (2 Sam 21:18; 1 Chr 20:4) — a feat that earned him permanent honor in the tradition of Goliath's defeat. The giant-killer held the eighth month: the kingdom's borders were safe in the hands of a man who had faced the extraordinary and prevailed."
    },
    "12": {
      "L": "The ninth for the ninth month was Abiezer the Anetothite, of the Benjaminites; and in his division were twenty-four thousand.",
      "M": "Abiezer the Anetothite, from Benjamin, commanded the ninth month, with twenty-four thousand men.",
      "T": "Anathoth — a Benjaminite city of priests, the future birthplace of the prophet Jeremiah (Jer 1:1). Abiezer the Anetothite carried the military tradition of his town before Jeremiah's prophetic tradition claimed it for subsequent generations. The same soil produced soldiers and prophets in their respective seasons."
    },
    "13": {
      "L": "The tenth for the tenth month was Maharai the Netophathite, of the Zerahites; and in his division were twenty-four thousand.",
      "M": "Maharai the Netophathite, of the Zerahite line, commanded the tenth month, with twenty-four thousand men.",
      "T": "Netophah — a village near Bethlehem, home to multiple of David's soldiers (2 Sam 23:28–29). The Netophathites appear in the restoration lists as among the first to return from Babylon (Ezra 2:22). These soldiers' hometown would outlast the monarchy and reconstitute itself in the post-exilic community."
    },
    "14": {
      "L": "The eleventh for the eleventh month was Benaiah the Pirathonite, of the sons of Ephraim; and in his division were twenty-four thousand.",
      "M": "Benaiah the Pirathonite, from Ephraim, commanded the eleventh month, with twenty-four thousand men.",
      "T": "A second Benaiah — the Pirathonite from Ephraim, distinct from Benaiah son of Jehoiada who held the third month. Great commanders shared names in David's army; the roster is careful to distinguish them. The eleventh month in the hands of an Ephraimite Benaiah: the kingdom's defense was distributed across tribes, ensuring that the military structure could not be reduced to a tribal power bloc."
    },
    "15": {
      "L": "The twelfth for the twelfth month was Heldai the Netophathite, of Othniel; and in his division were twenty-four thousand.",
      "M": "Heldai the Netophathite, descended from Othniel, commanded the twelfth month, with twenty-four thousand men.",
      "T": "The year closed with Heldai of Othniel's line. Othniel — Israel's first judge, deliverer of the nation from Cushan-rishathaim (Judg 3:9–11) — was a Calebite hero whose family had contributed to Israel's covenant history for centuries. Heldai carried that heritage into the twelfth month: the year's final defense rested in the hands of a man who traced his lineage to Israel's first great liberator after Joshua."
    },
    "16": {
      "L": "Furthermore over the tribes of Israel: over the Reubenites, the ruler was Eliezer the son of Zichri; over the Simeonites, Shephatiah the son of Maacah;",
      "M": "The tribal officers: for Reuben, Eliezer son of Zichri; for Simeon, Shephatiah son of Maacah;",
      "T": "Alongside the military rotation, David maintained a parallel administrative structure: one officer per tribe responsible for the tribal affairs of the whole kingdom. The tribal identity of Israel was honored and institutionalized. The twelve-tribe structure that had defined Israel since the wilderness remained the organizational backbone of the Davidic kingdom."
    },
    "17": {
      "L": "over the Levites, Hashabiah the son of Kemuel; over Aaron, Zadok;",
      "M": "for the Levites, Hashabiah son of Kemuel; for the Aaronites, Zadok;",
      "T": "Two distinct officers for two distinct sub-groups within the tribe of Levi: one for the broader Levitical body and one for the priestly Aaronic line. Zadok — whose name would define the legitimate priesthood for generations ('Zadokite' priests) — represented the Aaronic order at the highest administrative level. The distinction between Levites and priests was maintained even in the tribal roster."
    },
    "18": {
      "L": "over Judah, Elihu, one of the brothers of David; over Issachar, Omri the son of Michael;",
      "M": "for Judah, Elihu, one of David's brothers; for Issachar, Omri son of Michael;",
      "T": "Judah's tribal officer was Elihu — one of David's brothers, a son of Jesse. The king's own family held the administrative leadership of his tribe. The personal connection between the royal house and Judah's governance was made explicit in the roster: the tribe that produced the king was led by the king's own kin."
    },
    "19": {
      "L": "over Zebulun, Ishmaiah the son of Obadiah; over Naphtali, Jerimoth the son of Azriel;",
      "M": "for Zebulun, Ishmaiah son of Obadiah; for Naphtali, Jerimoth son of Azriel;",
      "T": "Zebulun and Naphtali — the northern tribes, far from Jerusalem, the region that Isaiah would later call 'Galilee of the nations' (Isa 9:1). Their tribal officers were named and honored in the same list as Judah's. The geographical periphery was not an administrative afterthought; every tribe had its named representative before the king."
    },
    "20": {
      "L": "over the sons of Ephraim, Hoshea the son of Azaziah; over the half tribe of Manasseh, Joel the son of Pedaiah;",
      "M": "for the sons of Ephraim, Hoshea son of Azaziah; for the half tribe of Manasseh, Joel son of Pedaiah;",
      "T": "Ephraim and Manasseh — the two sons of Joseph, the great double-portion tribe of the north. Their administrative officers are named separately: Ephraim as a full tribe, and Manasseh in its two halves (the two territories divided by the Jordan). Joseph's inheritance, divided by history and geography, was nonetheless fully represented in David's tribal administration."
    },
    "21": {
      "L": "over the half tribe of Manasseh in Gilead, Iddo the son of Zechariah; over Benjamin, Jaasiel the son of Abner;",
      "M": "for Manasseh's half tribe in Gilead, Iddo son of Zechariah; for Benjamin, Jaasiel son of Abner;",
      "T": "Gilead's Manassite half received its own officer — the Transjordanian territories were not administratively merged with the western territories but governed separately. Jaasiel son of Abner represented Benjamin: a poignant note, since Abner himself had been the general who had opposed David's rise (2 Sam 3:6–11) before his murder by Joab. His son now served the Davidic kingdom he had once resisted."
    },
    "22": {
      "L": "over Dan, Azareel the son of Jeroham. These were the commanders of the tribes of Israel.",
      "M": "For Dan, Azareel son of Jeroham. These were the leaders of Israel's tribes.",
      "T": "Dan, the northernmost tribe — the territory whose later idolatry at Dan became a byword for apostasy (1 Kgs 12:29–30) — was led here by Azareel son of Jeroham in the full honor of the tribal roster. Twelve officers, twelve tribes: the covenant structure of Israel was complete and each part named before God and the king. The kingdom was not just a military and commercial entity but a federation of distinct peoples bound by a single covenant."
    },
    "23": {
      "L": "But David did not number those from twenty years old and under, because the LORD had said he would increase Israel like the stars of the heavens.",
      "M": "David did not count those twenty years old and under, because the LORD had promised to multiply Israel like the stars of the heavens.",
      "T": "A deliberate exclusion, not an oversight. The Abrahamic promise — 'I will make your descendants as numerous as the stars' (Gen 15:5; 22:17) — rendered any complete census of Israel not merely unnecessary but presumptuous. To count what God had sworn to make uncountable was to assert human arithmetic over divine promise. David's wisdom was in knowing what not to count: the young, the uncountable future of the nation, belonged to God's promise, not human administration."
    },
    "24": {
      "L": "Joab the son of Zeruiah had begun to count but did not finish; yet wrath fell upon Israel because of this, and the number was not put into the account in the chronicles of King David.",
      "M": "Joab son of Zeruiah had started counting but did not finish; wrath came upon Israel because of it, and the number was never recorded in the chronicles of King David.",
      "T": "The incomplete census — a reference to the catastrophe of 1 Chronicles 21, when David ordered a full military census and seventy thousand Israelites died in the plague that followed. Joab had resisted even then (21:3–6) and his resistance was vindicated. The number that could not be completed in obedience was never entered into the royal archives in pride: the census that brought wrath left no triumphant record. Some numbers are not meant to be totaled."
    },
    "25": {
      "L": "Over the king's storehouses was Azmaveth the son of Adiel; over the storehouses in the fields, in the cities, in the villages, and in the towers was Jonathan the son of Uzziah.",
      "M": "Azmaveth son of Adiel managed the king's storehouses; Jonathan son of Uzziah managed the storehouses in the countryside — in the fields, cities, villages, and towers.",
      "T": "The material infrastructure of the kingdom: central warehouses in the capital and distributed storage throughout the country. The same organizational precision David had applied to the sanctuary's treasuries he applied to the crown's economic resources. A kingdom requires material supply as much as military power; the stewards of grain and silver were as essential to the kingdom's permanence as the commanders of the monthly divisions."
    },
    "26": {
      "L": "Over those working in the field for the king, for the cultivation of the ground, was Ezri the son of Chelub.",
      "M": "Ezri son of Chelub oversaw those who worked the royal fields.",
      "T": "Ezri the agricultural overseer: the king's farms required managed labor, and a named Levitical administrator ran them. The kingdom ate what the fields produced; Ezri stood between the harvest and the royal household. No function of the kingdom was beneath the dignity of an administrative appointment — from the incense altar to the plowed field, every role in the covenant community was named, organized, and honored."
    },
    "27": {
      "L": "And over the vineyards was Shimei the Ramathite; and over the produce of the vineyards for the wine cellars was Zabdi the Shiphmite.",
      "M": "Shimei the Ramathite oversaw the vineyards; Zabdi the Shiphmite managed the vintage and the wine cellars.",
      "T": "Two officers for two stages of the same product: the growing vine under one manager, the harvested grape and stored wine under another. The specialization reflects sophisticated agricultural administration. Wine was both an economic product and a liturgical one — the temple's drink offerings required a continuous supply. Shimei and Zabdi together ensured that the vine from field to cellar served both the king's table and the altar of God."
    },
    "28": {
      "L": "And over the olive trees and the sycamore trees in the Shephelah was Baalhanan the Gederite; and over the stores of oil was Joash.",
      "M": "Baalhanan the Gederite managed the olive trees and sycamore trees in the lowlands; Joash managed the stores of oil.",
      "T": "Olive oil — the most versatile substance in the ancient world: food, fuel for lamps, medicine, and the anointing medium of kings and priests. Baalhanan cultivated the trees in the Shephelah, the foothills where olive groves thrived; Joash stored the pressed oil. Together they managed a substance that lit the temple lamps, consecrated Israel's leadership, and nourished the people. Nothing was incidental in the royal stewardship."
    },
    "29": {
      "L": "And over the herds that grazed in Sharon was Shitrai the Sharonite; and over the herds in the valleys was Shaphat the son of Adlai.",
      "M": "Shitrai the Sharonite managed the herds grazing in Sharon; Shaphat son of Adlai managed the herds in the valleys.",
      "T": "Sharon — the coastal plain north of Joppa, famous for its rich pastures (Isa 65:10) — grazed the most prized cattle of the kingdom. The distinction between Sharon herds and valley herds reflects not only geography but quality: Sharon's cattle were premium livestock in separate management from the more numerous valley herds. The temple's burnt offerings and the royal table both drew from these carefully tended flocks."
    },
    "30": {
      "L": "Over the camels was Obil the Ishmaelite; over the donkeys was Jehdeiah the Meronothite.",
      "M": "Obil the Ishmaelite managed the camels; Jehdeiah the Meronothite managed the donkeys.",
      "T": "Obil the Ishmaelite managed the camels — fittingly, since Ishmael's descendants had long been the masters of camel trade and desert transport (Gen 37:25; Judg 8:26). Foreign expertise in royal service: David employed the best administrators for each domain regardless of ethnicity. The camel corps that made long-distance commerce possible was in Ishmaelite hands; the local donkeys that served everyday transport were managed by Jehdeiah from Meronoth."
    },
    "31": {
      "L": "And over the flocks was Jaziz the Hagerite. All these were the stewards of King David's property.",
      "M": "Jaziz the Hagerite managed the flocks. These were all the stewards of King David's royal holdings.",
      "T": "A Hagerite managing the royal flocks — another foreigner, like Obil the Ishmaelite, placed in a position of significant responsibility in David's court. The covenant kingdom was not a closed ethnic institution but a place where competence and loyalty earned honor regardless of ancestry. David drew his stewards from Judah, Benjamin, Ephraim, Gilead, Ishmael, and Hagar's line alike: the kingdom's material prosperity was managed by the most capable available hands."
    },
    "32": {
      "L": "Also Jonathan, David's uncle, was a counselor, a man of understanding and a scribe; and Jehiel the son of Hachmoni was with the king's sons.",
      "M": "Jonathan, David's uncle, was a counselor — a man of discernment and a skilled scribe. Jehiel son of Hachmoni served the king's sons.",
      "T": "The inner circle of wisdom: Jonathan the uncle, a man of discernment (H995, the intellectual virtue of seeing through complexity to truth) and a scribe trained in the written tradition. Jehiel son of Hachmoni attended the king's sons — a tutor or guardian figure in the royal household. The kingdom required not only soldiers and stewards but men of trained intelligence who could think, write, advise, and form the next generation of leadership."
    },
    "33": {
      "L": "And Ahithophel was the king's counselor; and Hushai the Archite was the king's companion.",
      "M": "Ahithophel was the king's counselor; Hushai the Archite was the king's trusted companion.",
      "T": "Two names that carry the entire weight of Absalom's rebellion in miniature. Ahithophel — whose counsel was 'as if one inquired of the word of God' (2 Sam 16:23), who defected to Absalom and whose final counsel was rejected, after which he went home, put his house in order, and hanged himself (2 Sam 17:23). Hushai — the king's friend who feigned loyalty to Absalom and successfully countered Ahithophel's plan, saving David's life. Both men are listed here as David's advisors without a word of the rebellion, the betrayal, or the death. The administrative record holds the names; history holds the rest."
    },
    "34": {
      "L": "And after Ahithophel was Jehoiada the son of Benaiah, and Abiathar; and the general of the king's army was Joab.",
      "M": "After Ahithophel, Jehoiada son of Benaiah and Abiathar served as counselors. Joab was the commander of the king's army.",
      "T": "The final verse of the administrative register ends with Joab — Israel's most formidable soldier, David's most useful and most troublesome servant. Joab had defended the kingdom, assassinated its enemies, defied the king's mercy, and murdered without authorization. He appears here simply as 'the general of the king's army' — the briefest possible summary of a man whose shadow falls across three decades of Davidic history. The administrative record honored the role without resolving the man. That reckoning waited for Solomon's throne (1 Kgs 2:28–34)."
    }
  },
  "28": {
    "1": {
      "L": "And David assembled at Jerusalem all the officers of Israel — the princes of the tribes, the commanders of the divisions that served the king, the commanders of thousands and of hundreds, the stewards of all the property and livestock of the king and his sons, with the court officials, the mighty men, and all the men of valor.",
      "M": "David assembled at Jerusalem all the leaders of Israel: the tribal princes, the commanders of the military divisions, the commanders of thousands and hundreds, the overseers of all royal property and livestock, and the court officials, the warriors, and all the men of valor.",
      "T": "Every layer of authority in the kingdom gathered at Jerusalem for David's final public address. Tribal princes, military commanders from the monthly divisions (chapter 27), the stewards of royal property (also chapter 27), the courtiers, the warriors. The Chronicler has been building toward this scene for five chapters: the full assembly that would hear the dying king's last speech, receive the temple plans, and witness the transfer of commission to Solomon. Nothing like this gathering had occurred since Sinai."
    },
    "2": {
      "L": "Then King David rose to his feet and said, 'Hear me, my brothers and my people. I had it in my heart to build a house of rest for the ark of the covenant of the LORD, the footstool of our God, and I had prepared for the building.'",
      "M": "King David stood up and said, 'Listen to me, my brothers and my people. I intended to build a house of rest for the ark of the covenant of the LORD — the footstool of our God — and I had made preparations for the construction.'",
      "T": "The king stood — the last time David stood before the assembled nation, already near death (1 Kgs 1:1 describes him too cold to be warm). He called them 'brothers' before he called them 'people': the covenant egalitarian before the royal hierarchical. His opening word was the dream he had carried for decades: a house of rest for the ark. 'Rest' — מְנוּחָה menuchah — the same word used for God's promised rest in the land (1 Chr 22:9). The ark was not just furniture; it was the footstool of the divine throne, the point where heaven touched earth. David had wanted to give God a dwelling worthy of the name."
    },
    "3": {
      "L": "'But God said to me, You shall not build a house for my name, because you are a man of war and have shed blood.'",
      "M": "'But God said to me, You are not to build a house for my name, for you are a man of war and have shed blood.'",
      "T": "The refusal: not a moral condemnation but a vocational distinction. God did not say David was wrong to be a warrior; he had commanded those wars. The disqualification was categorical: a house of peace cannot be built by hands stained with battle-blood, however righteous the cause. The temple would be built by a man whose name meant 'peace' — שְׁלֹמֹה Shelomoh — in an era of peace that David's wars had purchased. The warrior secured the peace; the man of peace built its dwelling. Both roles were necessary; neither man could fulfill both."
    },
    "4": {
      "L": "'Yet the LORD God of Israel chose me from all my father's house to be king over Israel forever. For he chose Judah as leader, and from the house of Judah my father's house, and from among my father's sons he was pleased to make me king over all Israel.'",
      "M": "'Yet the LORD God of Israel chose me from all my father's house to be king over Israel permanently. He chose Judah as the leading tribe, then from Judah's house my father's family, and from my father's sons he was pleased to make me king over all Israel.'",
      "T": "Three concentric elections radiating outward from the divine choice: Judah from among the tribes, Jesse's house from within Judah, David from among Jesse's sons. The word H977 (בָּחַר, 'chose') appears three times — the Chronicler's way of underlining that every step of the process was God's initiative, not human merit. David had been the most unlikely candidate (1 Sam 16:11) and was now the king. What God chose, God sustained. The election was not a reward for virtue but a sovereign appointment that preceded virtue and shaped it."
    },
    "5": {
      "L": "'And of all my sons — for the LORD has given me many sons — he has chosen my son Solomon to sit on the throne of the kingdom of the LORD over Israel.'",
      "M": "'And from all my sons — for the LORD has given me many — he has chosen Solomon to sit on the throne of the LORD's kingdom over Israel.'",
      "T": "Many sons, one chosen. David acknowledges the abundance of his family and immediately redirects the assembly's attention to the divine selection within that abundance. 'The throne of the kingdom of the LORD' — not David's kingdom but the LORD's. The Davidic monarchy was always a viceroyalty: the human king sat on God's throne as a vassal ruler (1 Chr 29:23 will make this explicit). Solomon's claim to succession was not primogeniture but divine choice — the same basis on which David himself had been crowned."
    },
    "6": {
      "L": "'He said to me, It is Solomon your son who shall build my house and my courts, for I have chosen him to be my son, and I will be his father.'",
      "M": "'God said to me, Solomon your son is the one who will build my house and my courts, for I have chosen him as my son and I will be his father.'",
      "T": "The father-son language of the Davidic covenant (2 Sam 7:14; Ps 89:26–27) applied directly to Solomon: 'I have chosen him to be my son, and I will be his father.' This is adoption language — the legal formula by which a patron claimed a subordinate as his son, investing him with all the rights and responsibilities of the family. God was not merely Israel's king; he was Solomon's father. The temple-building commission came embedded in a relationship, not merely an assignment."
    },
    "7": {
      "L": "'I will establish his kingdom forever, if he is resolute in keeping my commandments and my rules, as he is today.'",
      "M": "'I will establish his kingdom forever, if he remains firm in keeping my commandments and decrees, as he has up to now.'",
      "T": "The conditional clause that runs through all the Davidic covenant promises: 'if he continues.' The 'forever' is not unconditional in its application to Solomon personally; it is unconditional in the covenant line but conditional in the individual. Solomon 'as he is today' — young, devoted, at the beginning of his reign — was the Solomon God commended. The tragedy of Solomon's later life (1 Kgs 11) casts a shadow backward on this verse: the condition was not met, and the unified kingdom was torn. But the covenant line endured; the 'forever' moved to a greater Solomon."
    },
    "8": {
      "L": "'Now therefore in the sight of all Israel, the assembly of the LORD, and in the hearing of our God, keep and seek all the commandments of the LORD your God, that you may possess this good land and leave it as an inheritance to your children after you forever.'",
      "M": "'Now therefore, before all Israel — the LORD's assembly — and in the hearing of our God: keep and seek out all the commandments of the LORD your God, so that you may possess this good land and leave it as an inheritance to your children after you forever.'",
      "T": "David turned from Solomon to the whole assembly. The charge was not only for one successor but for a nation: keep the commandments, seek them out, live them in the good land. The land itself was conditional on covenant faithfulness — the Deuteronomic principle (Deut 4:1, 26–27) spoken now in the hearing of 'all Israel, the assembly of the LORD.' The nation was witnessing its own accountability. 'In the hearing of our God' — not merely a human assembly but a covenantal gathering before the divine witness. Everything said here was sworn before heaven."
    },
    "9": {
      "L": "'And you, Solomon my son, know the God of your father, and serve him with a whole heart and with a willing mind; for the LORD searches every heart and understands every plan and thought. If you seek him, he will be found by you; but if you forsake him, he will reject you forever.'",
      "M": "'And you, Solomon my son — know the God of your father. Serve him with a whole heart and a willing spirit, for the LORD searches every heart and understands every intention and thought. If you seek him, he will be found by you; but if you abandon him, he will reject you forever.'",
      "T": "The most intimate verse in the chapter — father to son, not king to heir. 'Know the God of your father': not just acknowledge, not merely obey, but know — יְדַע yada, the Hebrew word for deep relational knowledge that includes intellect, experience, and loyalty. The God Solomon must know is not an abstract deity but the God of David's own decades of trust, failure, repentance, and restoration. Then the warning, stark and plain: if you forsake him, he will reject you forever. H2186 (cast off, reject) — God can choose to exclude what he once included. This is not theoretical; in Solomon's own lifetime it would prove true. The most theologically charged sentence David ever spoke to his son went unheeded."
    },
    "10": {
      "L": "'Be careful now, for the LORD has chosen you to build a house for the sanctuary. Be strong and do it.'",
      "M": "'Now take care — the LORD has chosen you to build a house as a sanctuary. Be strong and do it.'",
      "T": "Five words in Hebrew: הִתְחַזֵּק וַעֲשֵׂה — be strong and do. The same command Joshua received before the Jordan crossing (Josh 1:6–7, 9), the same David had given him in 1 Chronicles 22:13. The Mosaic succession pattern repeated itself in the Davidic succession: the commander who could not finish the task charges his successor to complete it. The temple was not David's project deferred; it was the next chapter of a long story, entrusted to the next keeper of the covenant."
    },
    "11": {
      "L": "Then David gave his son Solomon the plan of the portico and its buildings, its storehouses, its upper rooms, its inner chambers, and the room for the mercy seat.",
      "M": "David gave his son Solomon the plan for the temple portico, its buildings, storerooms, upper rooms, inner chambers, and the room for the mercy seat.",
      "T": "The transfer of the blueprints. What David could not build with his hands he had prepared with his mind: the full architectural plan of the sanctuary, from the outer porch to the innermost room of the mercy seat — the kapporeth, the gold covering of the ark from which God had spoken to Moses (Exod 25:22). The most sacred space in Israel's geography was described in a set of documents passed from father to son. The dream was not lost; it was organized, written, and handed over."
    },
    "12": {
      "L": "And the plan of all that he had in mind, for the courts of the house of the LORD, all the surrounding chambers, the treasuries of the house of God, and the treasuries of the dedicated gifts;",
      "M": "Also the plan for everything that had come to him by the Spirit: the courts of the LORD's house, all the surrounding chambers, the treasuries of God's house, and the treasuries of the dedicated offerings.",
      "T": "The source of the plans: the Spirit (רוּחַ). David did not design the temple as an architect draws from imagination; he received its design as a prophet receives a word. The same Spirit who inspired Asaph's music, moved on the waters at creation (Gen 1:2), and rested on the craftsman Bezalel for the tabernacle's construction (Exod 31:3) had given David the architectural vision of the permanent house. The building was not a human achievement commissioned by a king; it was a divine design communicated through a chosen vessel."
    },
    "13": {
      "L": "for the divisions of the priests and the Levites, and for all the work of the service of the house of the LORD, and for all the vessels of service in the house of the LORD.",
      "M": "Also included were the divisions of priests and Levites, all the service work of the LORD's house, and specifications for all the vessels used in its service.",
      "T": "The plans were comprehensive: not only the architectural blueprint but the organizational framework (chapters 23–26 now documented in written form) and the inventory of sacred vessels (vv.14–18). David gave Solomon a complete governance manual for the temple — its building, its personnel, and its equipment — so that the son would begin his task not from scratch but from the full fruit of his father's preparation. Every generation builds on what the previous one organized."
    },
    "14": {
      "L": "He gave of gold by weight for each golden article of service, for all the silver articles by weight for each silver article of service;",
      "M": "He specified the weight of gold for all the gold articles used in the various services, and the weight of silver for all the silver articles.",
      "T": "Weights for every article. David's precision extended to metallurgy: nothing about the temple was left to improvisation or to the personal taste of the craftsman. The gold lampstands, the silver basins, the incense altar — each had a specified weight that governed how much precious metal would go into its construction. The exactness honored the holiness of the purpose: imprecise offerings to a precise God were a form of disrespect. David specified everything."
    },
    "15": {
      "L": "the weight of gold for the lampstands and their lamps of gold, by weight for each lampstand and its lamps; and the weight of silver for the lampstand and its lamps according to the use of each lampstand.",
      "M": "For each gold lampstand and its lamps: the exact weight of gold. For the silver lampstands and their lamps: the weight of silver required for each.",
      "T": "The lampstands — menorot — whose light had filled the tabernacle since the wilderness and would fill the temple through the centuries until the Babylonian darkness extinguished them. Each one specified by weight: the lampstand that lit the holy place was as precisely governed as the altar that sanctified the sacrifice. Light and sacrifice together were the twin poles of Israel's sanctuary worship, and both were specified to the gram."
    },
    "16": {
      "L": "And the weight of gold for the tables of the bread of the Presence, for each table, and the weight of silver for the silver tables.",
      "M": "The weight of gold for each table of the bread of the Presence, and the weight of silver for the silver tables.",
      "T": "The tables of the Presence bread — lechem hapanim, 'bread of the face,' the twelve loaves renewed every Sabbath that symbolized God's provision for the twelve tribes (Lev 24:5–9). The specified gold and silver weights for these tables ensured that what sat before the face of God was worthy of the presence it acknowledged. The table feeding the divine meal was to be built with the full precision of devotion."
    },
    "17": {
      "L": "And the pure gold for the forks and the bowls and the cups; and for the golden basins, the weight of each; and for the silver basins, weight by weight for each;",
      "M": "Pure gold for the forks, basins, and cups — and the exact weight for each golden bowl; the weight of silver for each silver bowl.",
      "T": "Forks for the altar flesh, basins for the blood and libations, cups for the drink offerings: the table service of the divine sanctuary specified to the piece and to the gram. The word 'pure' (H2889, tahor) applied to the gold signifies the highest grade — unmixed, unalloyed, worthy of the holy. What touched the offering presented to God was to be as pure as what the worshiper was meant to be."
    },
    "18": {
      "L": "And for the altar of incense, refined gold by weight; and gold for the pattern of the chariot, the cherubim that spread their wings and covered the ark of the covenant of the LORD.",
      "M": "Refined gold by weight for the incense altar, and the plan for the golden chariot — the cherubim that spread their wings and covered the ark of the covenant of the LORD.",
      "T": "The climax of the plans: the cherubim-chariot over the ark. The incense altar was central to the daily liturgy — from it rose the prayers of Israel like smoke before the divine face. But the cherubim — those cosmic figures whose outstretched wings formed the throne of God over the mercy seat — were the architectural statement of the temple's ultimate purpose. The temple was not primarily a place of human worship; it was the dwelling of the divine king. The cherubim-throne made that theology visible in beaten gold."
    },
    "19": {
      "L": "All this David made understood in writing from the hand of the LORD, all the work of the plan.",
      "M": "'All this,' said David, 'came to me in writing from the LORD's hand — every detail of the plan.'",
      "T": "The most extraordinary claim of the chapter: God communicated the temple's architectural design to David in written form. As God had given Moses the tabernacle plan on the mountain — 'exactly as I show you, so you shall make it' (Exod 25:9) — God gave David the temple plan in writing. The tabernacle and the temple were both designed in heaven before they were built on earth. David was not the architect of the temple; he was the transcriptionist of a divine revelation. What Solomon would build had already been built, in principle, in the mind of God."
    },
    "20": {
      "L": "Then David said to Solomon his son, 'Be strong and courageous, and do it. Do not be afraid or dismayed, for the LORD God, even my God, is with you. He will not leave you or forsake you until all the work of the service of the house of the LORD is finished.'",
      "M": "David said to his son Solomon, 'Be strong and courageous and do it. Do not be afraid or discouraged, for the LORD God — my God — is with you. He will not abandon you or forsake you until all the work for the LORD's house is complete.'",
      "T": "The echo is unmistakable: Deuteronomy 31:8, Moses to Joshua — 'It is the LORD who goes before you. He will be with you; he will not leave you or forsake you.' David knew the pattern. He had studied Moses; he had lived the promise. Now he was Moses and Solomon was Joshua: the covenant commission passed from the one who prepared to the one who would complete. 'My God' — the possessive is personal, not merely titular. David was not invoking a theological abstraction but the God he had personally known through the cave of Adullam, the valley of Elah, the darkest hours of Bathsheba and Absalom. This God, he promised his son, would be with him."
    },
    "21": {
      "L": "And behold, the divisions of the priests and the Levites for all the service of the house of God are at your disposal; and with you in all the work are every willing craftsman for every kind of service, and the officers and all the people will be wholly at your command.",
      "M": "Look — the priestly and Levitical divisions for all the service of God's house are ready for you. With you for all the work will be every willing skilled craftsman for any service, and the officers and all the people are completely at your disposal.",
      "T": "The charge ended with a resource inventory: priests, Levites, skilled craftsmen, civil officers, and all the people — all ready, all at Solomon's command. The dying king had not given his son a task without the means to accomplish it. Twenty-eight chapters of Chronicles had established the theological grounding, the genealogical framework, the Levitical organization, the military structure, and the economic stewardship of the kingdom. Now it was Solomon's. Every willing craftsman — H5081, the word for generous, noble-minded commitment — would work alongside the organized corps. The temple would be built by willing hands serving a God who had willed it from before the first stone was laid."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '1chronicles')
        merge_tier(existing, CHRONICLES1, tier_key)
        save(tier_dir, '1chronicles', existing)
    print('1 Chronicles 26–28 written.')

if __name__ == '__main__':
    main()
