"""
MKT 2 Chronicles chapters 22–24 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-2chronicles-22-24.py

Content:
- Ch 22: Ahaziah's brief reign; alliance with Ahab's house; killed by Jehu's purge;
         Athaliah destroys all royal seed; Joash hidden in temple by Jehoshabeath
- Ch 23: Jehoiada's coup in the seventh year; Joash crowned with crown and testimony;
         Athaliah slain at the Horse Gate; covenant renewal; Baal temple demolished; city at rest
- Ch 24: Joash's forty-year reign; temple repair under Jehoiada; Jehoiada's death at 130;
         apostasy after nobles' influence; Zechariah son of Jehoiada stoned in temple court;
         small Syrian army defeats great Judah by divine judgment; Joash assassinated;
         buried outside the royal tombs

Translation decisions (carried forward from mkt-2chronicles-13-18.py):
- H3068 (יהוה): "LORD" in L/M; "the LORD" in T. Consistent throughout OT scripts.
- H430 (אֱלֹהִים): "God" throughout all tiers.
- H2617 (חֶסֶד): "kindness" at 24:22 — narrative usage is personal rather than covenantal
  (Joash forgot the particular kindness Jehoiada had shown him). L/M: "kindness";
  T: "covenant loyalty" to surface the full hesed weight — the compound of loyalty and
  active goodness that no single English word captures.
- H7307 (רוּחַ): "Spirit" (capitalized) at 24:20 — same prophetic Spirit coming upon Zechariah
  as came upon Azariah at 15:1. Clearly divine prophetic agency, not wind or breath.
- H1285 (בְּרִית): "covenant" throughout at 23:1, 3, 16.

New decisions for chs 22–24:
- 22:2 textual note: MT reads "forty-two years old" for Ahaziah's accession age; the parallel
  2 Kgs 8:26 reads "twenty-two years." If 42 were correct, Ahaziah would have been born before
  his father Jehoram became king and two years older than Jehoram himself. 42 is almost
  certainly a scribal error (a waw joined to mem: מ + ו = מב instead of כב). L/M render the
  MT as given; T notes the manuscript difficulty.
- 22:2 "daughter of Omri" — the MT says Omri; the parallel 2 Kgs 8:26 says "daughter of Ahab."
  Most scholars understand "daughter of Omri" as a loose dynastic designation (granddaughter
  through Ahab). L/M: "daughter of Omri" (MT as written); T notes the probable meaning.
- 22:6 "Azariah" — the MT uses Azariah here for Ahaziah; this is a well-attested variant-name
  situation in 2 Chronicles (cf. 2 Kgs 8:29 which uses Ahaziah). L/M follow the MT text;
  T identifies the person as Ahaziah.
- 22:7 "was of God that the downfall of Ahaziah came through Joram" — the divine passive names
  God as the governing agent of Ahaziah's fate. Unusual in Chronicles to name God so directly
  in a pagan-king context; preserved in all three tiers; T surfaces the theological significance.
- 23:11 "the testimony" — the 'eduth placed in the king's hand at coronation was a copy of the
  covenant law (cf. Deut 17:18-19; Ps 132:12). L/M: "the testimony"; T notes the Deuteronomic
  covenant significance of the king receiving Torah at the moment of anointing.
- 24:6 "collection Moses the servant of God laid upon Israel" — echoes Exod 30:11-16, the
  half-shekel census tax for tabernacle maintenance. The temple repair levy is positioned as
  continuous with Mosaic covenant provision.
- 24:20 Spirit on Zechariah echoes 15:1 (Azariah son of Oded) — same prophetic pattern;
  the message inverts the positive form of the covenant theorem to its negative fulfilment.
- 24:22 Zechariah's dying words ("May the LORD see and avenge") — cited explicitly by Jesus
  in Matt 23:35 and Luke 11:51 as the last OT martyr cry. T surfaces this NT echo. The verb
  "require" (darash) is the covenant term for God acting as avenger of blood.
- 24:24 small Syrian force defeating great Judah — direct theological reversal of ch 14
  (Zerah's vast army fleeing before Asa's smaller force). The principle operates in both
  directions: outcome is never about numbers but about the LORD's presence or absence.
  T draws this connection explicitly.
- Aspect notes:
  - Ch 22: narrative uses waw-consecutive imperfects throughout; the pivotal theological
    statement at v7 ("was of God") uses a qal perfect, marking it as the interpretive
    hinge of the episode.
  - Ch 23: Jehoiada's instructions in vv4-7 use imperfect/jussive command forms; the
    execution of the plan uses waw-consecutive narrative sequence.
  - Ch 24: the period of faithfulness is marked by a duration formula ("all the days of
    Jehoiada the priest"); the post-Jehoiada apostasy breaks cleanly. Zechariah's
    oracle at v20 uses prophetic perfect forms.
- OT intertextuality:
  - 22:9: "grandson of Jehoshaphat, who sought the LORD with all his heart" — Jehoshaphat's
    faithfulness (17:3-6) still casts its shadow two generations later; even in judgment,
    the righteous grandfather's name bought the wicked grandson a grave.
  - 23:3: "as the LORD has spoken concerning the sons of David" — Davidic covenant of
    2 Sam 7:12-16; the legitimacy of the restoration is covenantal, not merely political.
  - 23:16: three-party covenant (LORD, king, people) echoes Deut 29 and Josh 24; every
    major turning point in Chronicles is marked by a formal covenant ceremony.
  - 23:18: "as it is written in the law of Moses, with rejoicing and with singing" — Deut 12:12
    and the Mosaic worship prescriptions; the Chronicler always ties restored temple worship
    to both Mosaic foundation and Davidic elaboration.
  - 24:20: Spirit on Zechariah echoes 15:1 (Azariah son of Oded); both oracles invoke
    the covenant theorem of 15:2 — here in its negative form.
  - 24:22 dying words: echo of Gen 4:10 (Abel's blood crying out); explicit NT citation in
    Matt 23:35/Luke 11:51 makes this the OT's last martyr cry before the Baptist.
  - 24:24: theological reversal of ch 14 — small force defeats great army; the LORD
    determines outcomes, not military math.
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

CHRONICLES2 = {
  "22": {
    "1": {
      "L": "And the inhabitants of Jerusalem made Ahaziah his youngest son king in his place, for the company of men that came with the Arabians to the camp had slain all the elder sons. So Ahaziah the son of Jehoram king of Judah reigned.",
      "M": "The residents of Jerusalem made Ahaziah, his youngest son, king in his place, for the raiding band that came with the Arabians to the camp had killed all the older sons. So Ahaziah son of Jehoram king of Judah began to reign.",
      "T": "The youngest son became king because the older ones were dead — killed not by a foreign army in open battle but by the Arab raiders who had swept through the camp during Jehoram's disastrous reign (21:16-17). Ahaziah inherited a throne stripped of alternatives. Jerusalem made him king not from choice but from necessity: he was all that remained of the royal line. The circumstances of his accession were themselves the first sign that this reign would be defined by Ahab's house."
    },
    "2": {
      "L": "Forty and two years old was Ahaziah when he began to reign, and he reigned one year in Jerusalem. His mother's name also was Athaliah the daughter of Omri.",
      "M": "Ahaziah was forty-two years old when he became king, and he reigned one year in Jerusalem. His mother was Athaliah the daughter of Omri.",
      "T": "Forty-two years — almost certainly a scribal error for twenty-two. The parallel 2 Kings 8:26 reads 'twenty-two years,' and if forty-two were correct Ahaziah would have been born before his own father Jehoram became king, and two years older than Jehoram himself. A single letter separates the Hebrew for twenty (כ) from forty (מ); an added waw gives forty-two instead of twenty-two. The Chronicler's purpose here is not arithmetic but dynasty: his mother was Athaliah the daughter of Omri — or more precisely, Omri's granddaughter through Ahab, since 'daughter of Omri' was a dynastic designation for the whole northern apostate line. Ahaziah was not merely influenced by Ahab's household; he was born from it."
    },
    "3": {
      "L": "He also walked in the ways of the house of Ahab, for his mother was his counselor to do wickedly.",
      "M": "He too walked in the ways of the house of Ahab, for his mother was his counselor in wickedness.",
      "T": "The mother who counseled him to wickedness: Athaliah, daughter of Ahab and Jezebel — the woman who had introduced Baal worship into the northern kingdom at scale — now held the position of queen mother in Jerusalem and used it to direct a king who lacked the formation or the will to resist her. 'His mother was his counselor' is the Chronicler's precise explanation. Ahaziah did not stumble into the Ahab ways; he was guided into them by the woman closest to him."
    },
    "4": {
      "L": "Wherefore he did evil in the sight of the LORD like the house of Ahab, for they were his counselors after the death of his father, to his destruction.",
      "M": "He did evil in the sight of the LORD like the house of Ahab, for after his father's death they became his advisers and led him to his ruin.",
      "T": "After Jehoram died, the Ahab connection became structural: the entire circle of Ahab's surviving courtiers and relatives now advised the new king. 'To his destruction' — the Chronicler states the outcome in advance. The counsel Ahaziah received was not merely politically bad; it was the kind whose end is written from the beginning. The house of Ahab was already marked for judgment. To take their counsel was to bind oneself to their fate."
    },
    "5": {
      "L": "And he walked after their counsel, and went with Jehoram the son of Ahab king of Israel to war against Hazael king of Syria at Ramoth-gilead: and the Syrians smote Joram.",
      "M": "Following their advice, he joined Jehoram son of Ahab king of Israel in battle against Hazael king of Syria at Ramoth-gilead. The Syrians wounded Joram.",
      "T": "The chain of consequences ran with terrible logic: advised by Ahab's house, he fought alongside Ahab's son. Ramoth-gilead was the city where Ahab himself had been mortally wounded (18:28-34); now his son Joram fought there again and again came away wounded. The location was haunted by covenant judgment. Jehoshaphat had gone to Ramoth-gilead with Ahab and barely escaped with his life. Ahaziah, grandson of the man who had been warned not to ally with Ahab, now completed the pattern his grandfather had begun."
    },
    "6": {
      "L": "And he returned to be healed in Jezreel because of the wounds which were given him at Ramah, when he fought with Hazael king of Syria. And Azariah the son of Jehoram king of Judah went down to see Jehoram the son of Ahab at Jezreel, because he was sick.",
      "M": "Joram returned to Jezreel to recover from the wounds received at Ramah in the battle with Hazael king of Syria. Ahaziah son of Jehoram king of Judah went down to Jezreel to visit Joram son of Ahab, who was ill.",
      "T": "Joram retreated north to Jezreel — the royal residence built by Ahab next to Naboth's vineyard, the ground cursed by the blood Ahab had spilled to acquire it (1 Kgs 21:19). Ahaziah followed him there, the Davidic king making a sickroom visit to the Omride. The Chronicler here uses the alternate name Azariah for Ahaziah — a scribal variant attested in the MT — but the person is Ahaziah king of Judah. The visit to Jezreel was also a visit to the place where the dogs had licked Ahab's blood and where Elijah had declared the end of the Omride dynasty. All the threads of judgment were converging there."
    },
    "7": {
      "L": "And the destruction of Ahaziah was of God by coming to Joram: for when he was come, he went out with Jehoram against Jehu the son of Nimshi, whom the LORD had anointed to cut off the house of Ahab.",
      "M": "Ahaziah's downfall came about through God's design — when he arrived, he went out with Jehoram against Jehu son of Nimshi, whom the LORD had anointed to destroy the house of Ahab.",
      "T": "The Chronicler states it plainly: Ahaziah's destruction was of God. The timing of the visit, the encounter with Jehu, the end that followed — these were not random but governed. God had anointed Jehu through Elisha (2 Kgs 9:6-10) to execute judgment on the house of Ahab. Ahaziah, who had bound himself to Ahab's house by alliance and by accepting their counsel, was caught in the net of that judgment. He was not killed because God hated him specifically but because he had joined himself to a dynasty under sentence, and the sentence fell on all within its orbit. When you ally with what God has condemned, you inherit the condemnation."
    },
    "8": {
      "L": "And it came to pass, that when Jehu was executing judgment upon the house of Ahab, and found the princes of Judah, and the sons of the brethren of Ahaziah, that ministered to Ahaziah, he slew them.",
      "M": "While Jehu was carrying out judgment on the house of Ahab, he found the princes of Judah and the sons of Ahaziah's brothers who were in attendance on him, and he killed them.",
      "T": "The judgment fell not only on Ahaziah but on all who had woven themselves into Ahab's circle. The princes of Judah who accompanied him, the sons of his brothers who had survived the Arab raid and now served at court — they were at Jezreel because Ahaziah had brought them there as his royal entourage. By following the counsel of Ahab's house into the very presence of Jehu's purge, Ahaziah had placed his own household officials within range of the divine judgment on Ahab's dynasty. The innocent-seeming sickroom visit had become a massacre."
    },
    "9": {
      "L": "And he sought Ahaziah: and they caught him, (for he was hid in Samaria,) and brought him to Jehu, and when they had slain him, they buried him: Because, said they, he is the son of Jehoshaphat, who sought the LORD with all his heart. So the house of Ahaziah had no power to keep still the kingdom.",
      "M": "Jehu searched for Ahaziah, found him hiding in Samaria, brought him to Jehu, and put him to death. They buried him, saying, 'He is the grandson of Jehoshaphat, who sought the LORD with all his heart.' Then the house of Ahaziah had no one capable of holding the kingdom.",
      "T": "Ahaziah fled and hid in Samaria — the capital of the northern kingdom, the city of Ahab and Jezebel. The man who had gone to Jezreel to visit Ahab's son died in the land of Ahab's dynasty. He was hunted down and killed. But here the Chronicler pauses to note something: they buried him. The reason given is the reason the Chronicler wants remembered — not because of anything Ahaziah had done, but because he was the grandson of Jehoshaphat, the king who had sought the LORD with his whole heart. The righteousness of the faithful grandfather extended to the wicked grandson's burial. Covenant faithfulness casts a long shadow; even two generations later, Jehoshaphat's name bought Ahaziah a grave. With Ahaziah dead and the rest of the princes slain, the house of David's royal line was, for the first time in centuries, without a clear successor."
    },
    "10": {
      "L": "But when Athaliah the mother of Ahaziah saw that her son was dead, she arose and destroyed all the seed royal of the house of Judah.",
      "M": "When Athaliah the mother of Ahaziah saw that her son was dead, she rose up and eliminated the entire royal family of Judah.",
      "T": "Athaliah moved with the speed of a woman who had prepared for this moment. The queen mother — daughter of Ahab and Jezebel, granddaughter of Omri — had watched the Davidic dynasty destroy her family in the north. Now, with Ahaziah dead, she turned the structure of Judah's royal household into a killing field. All the seed royal: every prince, every potential heir, every Davidic descendant within reach. Athaliah was not content to be regent; she intended to eliminate the line entirely and rule in her own name. The dynasty that God had sworn to David (2 Sam 7:12-16) appeared, in this moment, to be within a few breaths of complete extinction."
    },
    "11": {
      "L": "But Jehoshabeath, the daughter of the king, took Joash the son of Ahaziah, and stole him from among the king's sons that were slain, and put him and his nurse in a bedchamber. So Jehoshabeath, the daughter of king Jehoram, the wife of Jehoiada the priest, (for she was the sister of Ahaziah,) hid him from Athaliah; so that she slew him not.",
      "M": "But Jehoshabeath, the king's daughter, took Ahaziah's son Joash and stole him away from among the princes being killed, and put him and his nurse in a bedroom. Jehoshabeath, daughter of King Jehoram and wife of the priest Jehoiada — and Ahaziah's sister — hid him from Athaliah so that she did not kill him.",
      "T": "One woman preserved the Davidic line from extinction. Jehoshabeath — whose name means 'the LORD is my oath' — was the king's daughter and the priest's wife: she sat at the intersection of the royal house and the priestly house, which gave her access to both the palace where the killing was happening and the temple where she could hide the child. She stole Joash from among the bodies of his brothers. The verb echoes the saving thefts of Scripture: as the Hebrew midwives stole infant boys from Pharaoh's death edict, as Moses' mother hid him in the reeds, Jehoshabeath reached into the slaughter and took one child back. She hid him in a bedchamber — and then, as the next verse tells us, in the house of God itself for six years. The Davidic heir lived in the sanctuary, hidden from the woman trying to destroy the covenant line."
    },
    "12": {
      "L": "And he was with them hid in the house of God six years: and Athaliah reigned over the land.",
      "M": "He remained hidden with them in the house of God for six years while Athaliah ruled the land.",
      "T": "Six years. Athaliah sat on David's throne for six years — the only woman to rule Judah in its entire history, the granddaughter of Omri governing from Jerusalem while the true heir grew up in the temple. The Chronicler states it simply: and Athaliah reigned over the land. The parallel structure of the verse carries the entire weight: the false queen in the palace, the hidden king in the sanctuary. God's covenant was not broken; it was concealed. The preservation of Joash in the house of God was the preservation of the messianic line — the promise that from David's seed would come the one in whom all the promises would be fulfilled."
    }
  },
  "23": {
    "1": {
      "L": "And in the seventh year Jehoiada strengthened himself, and took the captains of hundreds, Azariah the son of Jeroham, and Ishmael the son of Jehohanan, and Azariah the son of Obed, and Maaseiah the son of Adaiah, and Elishaphat the son of Zichri, into covenant with him.",
      "M": "In the seventh year Jehoiada took courage and entered into a covenant with five captains of hundreds: Azariah son of Jeroham, Ishmael son of Jehohanan, Azariah son of Obed, Maaseiah son of Adaiah, and Elishaphat son of Zichri.",
      "T": "After six years of Athaliah's reign, Jehoiada acted. The Chronicler says he 'strengthened himself' — the same verb used of Jehoshaphat establishing his reign, of Asa taking courage after Azariah's prophecy, of faithful kings in Chronicles gathering the resolve to do what the covenant requires. Jehoiada had been protecting Joash in the temple for six years; now the child was old enough to be presented, and the priest had waited long enough. He brought five captains of hundreds — the leaders of Judah's military companies — into covenant with him. The coup would be executed by the army with the priest at its head."
    },
    "2": {
      "L": "And they went about in Judah, and gathered the Levites out of all the cities of Judah, and the chief of the fathers of Israel, and they came to Jerusalem.",
      "M": "They traveled through Judah and assembled the Levites from all the towns of Judah and the heads of the ancestral families of Israel, and they came to Jerusalem.",
      "T": "The network was broad: Levites from every city in Judah, heads of the ancestral families — the religious and civil infrastructure of the nation. Jehoiada was not planning a palace coup with a small band of loyalists; he was organizing a national restoration with the participation of the people's established leaders. The Levites, who would serve as the coup's security force, were gathered from across the land. Everyone came to Jerusalem for what would be presented, publicly, as a covenant ceremony — because that is precisely what it was."
    },
    "3": {
      "L": "And all the congregation made a covenant with the king in the house of God. And he said unto them, Behold, the king's son shall reign, as the LORD hath said of the sons of David.",
      "M": "All the assembly made a covenant with the king in the house of God. Jehoiada said to them, 'The king's son shall reign, as the LORD promised concerning the sons of David.'",
      "T": "The covenant was made in the house of God — the place where the six-year-old Joash had been hidden, the place that Athaliah had never controlled. Jehoiada did not merely announce a political change; he established the restoration on covenantal grounds. The LORD had promised: from David's sons, one shall reign (2 Sam 7:12-16). Athaliah's six-year usurpation had not cancelled the promise; it had only deferred its fulfillment. The covenant made in the temple that day was the nation's formal acknowledgment that God's word to David stood, that the hiding of Joash had been the preservation of that word, and that what was about to happen was not a coup but a covenant fulfilment."
    },
    "4": {
      "L": "This is the thing that ye shall do; A third part of you entering on the sabbath, of the priests and of the Levites, shall be porters of the doors;",
      "M": "This is what you are to do: a third of you — the priests and Levites coming on duty on the Sabbath — will be gatekeepers at the temple entrances;",
      "T": "The plan was careful and precise. Using the regular rotation of Sabbath temple service as cover, Jehoiada divided the forces into three groups. The Sabbath change of guard provided a legitimate reason for large numbers of armed men to be present in and around the temple complex. A third would control the entrances — keeping the situation contained and preventing Athaliah's forces from flooding the temple area once the coronation began."
    },
    "5": {
      "L": "And a third part shall be at the king's house; and a third part at the gate of the foundation: and all the people shall be in the courts of the house of the LORD.",
      "M": "A third will be at the palace, a third at the Foundation Gate, and all the people will be in the courts of the LORD's house.",
      "T": "The three-part deployment covered the strategic points: the temple gates, the royal palace (Athaliah's residence), and the Foundation Gate to the south. The assembled people filled the temple courts, making the coronation a public event that could not be isolated or suppressed. Athaliah would not learn of it from a spy; she would hear the shout of the crowd."
    },
    "6": {
      "L": "But let none come into the house of the LORD, save the priests, and they that minister of the Levites; they shall go in, for they are holy: but all the people shall keep the watch of the LORD.",
      "M": "No one is to enter the LORD's house except the priests and the ministering Levites, for they are holy. All the people are to keep watch at their assigned posts.",
      "T": "The holiness boundary maintained even in a political crisis. The temple was not to become a general assembly hall or a military staging area. The priests and Levites consecrated for temple service would enter; everyone else would hold their positions outside. The sanctity of the house of God was to be protected even while it served as the site of covenant restoration. Jehoiada, who had protected a child in that house for six years, would not profane it in the moment of the child's vindication."
    },
    "7": {
      "L": "And the Levites shall compass the king round about, every man with his weapons in his hand; and whosoever else cometh into the house, he shall be put to death: but be ye with the king when he cometh in, and when he goeth out.",
      "M": "The Levites are to surround the king, each man with his weapons in hand. Anyone who tries to enter the house is to be put to death. Stay with the king wherever he goes.",
      "T": "The Levites' traditional role was worship and instruction, not military protection — but in this moment, bearing weapons was an act of covenant faithfulness. The king they were about to coronate was the sole surviving descendant of David; to guard him was to guard the covenant. 'Whoever else comes into the house shall be put to death' — the perimeter was absolute. This was not merely protecting a political pretender but defending the LORD's anointed, whose life was the visible sign of God's faithfulness to his promise."
    },
    "8": {
      "L": "So the Levites and all Judah did according to all things that Jehoiada the priest commanded, and took every man his men that were to come in on the sabbath, with them that were to go out on the sabbath: for Jehoiada the priest dismissed not the courses.",
      "M": "So the Levites and all Judah carried out exactly what Jehoiada the priest commanded. Each captain took his men — those coming on duty on the Sabbath and those going off duty — for Jehoiada did not release the divisions.",
      "T": "The priest's planning extended to the rotation schedule: he kept both the incoming and outgoing Sabbath guard active simultaneously, doubling the force on duty without raising suspicion by issuing unusual orders. The men coming on for the Sabbath would normally relieve those going off; Jehoiada kept both companies present. The practical effect was that the force surrounding the temple was twice its normal size, positioned before any of Athaliah's loyalists could realize what was happening. Jehoiada the priest was also, in this moment, a tactician."
    },
    "9": {
      "L": "Moreover Jehoiada the priest delivered to the captains of hundreds spears, and bucklers, and shields, that had been king David's, which were in the house of God.",
      "M": "Jehoiada the priest issued to the captains of hundreds the spears, bucklers, and shields that had belonged to King David, which were stored in the house of God.",
      "T": "David's weapons from the temple armory — the arms the great king had dedicated to the LORD after his victories and placed in the sanctuary as covenant trophies. For Jehoiada to arm the captains with David's own weapons was to make a theological statement: this restoration was continuous with David's covenant, equipped by the resources David had consecrated to the LORD. The weapons that had won the kingdom for David were now being deployed to restore David's line."
    },
    "10": {
      "L": "And he set all the people, every man having his weapon in his hand, from the right side of the temple to the left side of the temple, along by the altar and the temple, by the king round about.",
      "M": "He stationed all the people with weapons in hand from the south side to the north side of the temple — along the altar and the house, surrounding the king.",
      "T": "The human perimeter around the young king was a wall of bodies from altar to house. The altar — the place of sacrifice and covenant — was the visual center of it. Joash would be crowned within sight of the altar where the Davidic kings had offered. The weapons surrounding him were not merely military; they were the people's embodied declaration that this child's life was worth dying for."
    },
    "11": {
      "L": "Then they brought out the king's son, and put upon him the crown, and gave him the testimony, and made him king. And Jehoiada and his sons anointed him, and said, God save the king.",
      "M": "They brought out the king's son, placed the crown on him, and gave him the testimony. They made him king, and Jehoiada and his sons anointed him, calling out, 'Long live the king!'",
      "T": "The crown and the testimony together: the crown was the visible symbol of royal authority; the testimony was the copy of the covenant law that Deuteronomy 17:18-19 required the king to write for himself and read all his days. Joash received both at once — political authority and covenantal obligation bound together in a single ceremony. He was not crowned as an absolute monarch but as a covenant king, sworn to the LORD's Torah from the first moment of his reign. Jehoiada anointed him with oil — the priestly act that transformed a child into the LORD's anointed. 'Long live the king': after six years of hiding and six years of false rule, the Davidic line was publicly restored."
    },
    "12": {
      "L": "And when Athaliah heard the noise of the people running and praising the king, she came to the people into the house of the LORD:",
      "M": "When Athaliah heard the noise of the people running and praising the king, she came to the people at the LORD's house.",
      "T": "She heard it from the palace: the noise of a crowd, running and shouting praise. Six years of rule had not taught Athaliah what was happening in the temple she had never properly controlled. She came — not cautiously, not with guards deployed, but came in person to see what the noise meant. The woman who had killed all the royal seed walked toward the place where the seed she had failed to kill was being crowned."
    },
    "13": {
      "L": "And she looked, and, behold, the king stood at his pillar at the entering in, and the princes and the trumpets by the king: and all the people of the land rejoiced, and sounded with trumpets, also the singers with instruments of musick, and such as taught to sing praise. Then Athaliah rent her clothes, and said, Treason, Treason.",
      "M": "She looked and saw the king standing by his pillar at the entrance, with the officers and trumpets beside him. All the people of the land were rejoicing and sounding trumpets, with singers and musicians leading praise. Athaliah tore her clothes and cried, 'Treason! Treason!'",
      "T": "The scene that greeted her was everything she had worked to prevent: the king at his pillar — the standing place of Davidic kings at covenant ceremonies (cf. 2 Chr 34:31; 2 Kgs 11:14) — surrounded by officers, trumpets sounding, the entire people rejoicing in music and praise. The child she had hunted for six years stood in the sight of the city as its anointed king. Athaliah tore her robes — the ancient gesture of grief and horror at what cannot be reversed. Then she cried treason: the woman who had killed all the royal heirs and seized power by violence called the lawful coronation of the legitimate king an act of treason. The irony is the Chronicler's final word on Athaliah's reign."
    },
    "14": {
      "L": "Then Jehoiada the priest brought out the captains of hundreds that were set over the host, and said unto them, Have her forth of the ranges: and whoso followeth her, let him be slain with the sword. For the priest said, Slay her not in the house of the LORD.",
      "M": "Jehoiada the priest brought out the captains who commanded the troops and ordered them: 'Take her outside the ranks, and put to death anyone who follows her — but do not kill her in the LORD's house.'",
      "T": "Jehoiada's command combined urgency with scruple: remove her immediately, kill anyone who tries to defend her — but not in the temple. The LORD's house would not be defiled with blood even of this usurper. The sanctity that Jehoiada had protected for six years while harboring a fugitive king inside was to be honored in the moment of victory. He could have allowed a summary execution in the temple court; he insisted on order, legitimacy, and a clean separation between the place of worship and the place of judgment."
    },
    "15": {
      "L": "So they laid hands on her; and when she was come to the entering of the horse gate by the king's house, they slew her there.",
      "M": "So they seized her, and when she reached the entrance of the Horse Gate at the palace, they killed her there.",
      "T": "She was taken to the Horse Gate — the entry to the royal stables, at the edge of the palace complex, well outside the temple courts. It was an unglamorous location for an unglamorous end. Athaliah the daughter of Ahab and Jezebel, the only woman to sit on David's throne, ended her six years of usurped rule at a stable gate. The Chronicler gives the location and the fact and nothing more. The end was as abrupt as the beginning."
    },
    "16": {
      "L": "And Jehoiada made a covenant between him, and between all the people, and between the king, that they should be the LORD's people.",
      "M": "Jehoiada made a covenant between himself, all the people, and the king — that they would be the LORD's people.",
      "T": "The formal covenant came after the execution, not before. First the false was removed; then the true was established. The three-party covenant — priest, people, king, all binding themselves to the LORD — echoed the covenant structures of Deuteronomy 29 and Joshua 24. Every major turning point in Israel's history was marked by a covenant ceremony; Jehoiada understood that this political restoration was incomplete without covenantal reconstitution. The people had lived under Athaliah's rule for six years — years when the covenant framework had frayed. To be the LORD's people required a formal recommitment, not just a change of regime."
    },
    "17": {
      "L": "Then all the people went to the house of Baal, and brake it down, and brake his altars and his images in pieces, and slew Mattan the priest of Baal before the altars.",
      "M": "All the people then went to the house of Baal and tore it down. They smashed his altars and images, and killed Mattan the priest of Baal in front of the altars.",
      "T": "Covenant renewal required the removal of what the covenant forbade. The house of Baal — built or maintained under Athaliah's influence — was torn down by the people who had just covenanted to be the LORD's. Mattan the Baal priest was killed before the altars he had served. The pattern is consistent throughout Chronicles: every genuine covenant renewal is accompanied by physical, visible destruction of the idolatrous infrastructure. The Chronicler does not present this as religious violence; it is covenant housecleaning — the concrete expression of the community's declaration that it belonged to the LORD."
    },
    "18": {
      "L": "Also Jehoiada appointed the offices of the house of the LORD by the hand of the priests the Levites, whom David had distributed in the house of the LORD, to offer the burnt offerings of the LORD, as it is written in the law of Moses, with rejoicing and with singing, as it was ordained by David.",
      "M": "Jehoiada also reestablished the temple administration under the priests and Levites — the divisions David had appointed — to offer burnt offerings as prescribed in the law of Moses, with the rejoicing and singing that David had ordained.",
      "T": "The temple was restored to its proper governance immediately: the Levitical divisions that David had organized, the worship patterns that Moses had established, the sacrificial system that ran from Sinai through Solomon's dedication and had been interrupted by Athaliah's years. The Chronicler notes both the Mosaic prescription (what to offer) and the Davidic elaboration (how to offer it — with rejoicing and singing). Temple worship in Chronicles is always both: the foundational commands of Moses and the celebratory additions of David. To restore the temple was to restore both streams of tradition simultaneously."
    },
    "19": {
      "L": "And he set the porters at the gates of the house of the LORD, that none which was unclean in any thing should enter in.",
      "M": "He stationed gatekeepers at the entrances to the LORD's house to ensure that nothing unclean in any way could enter.",
      "T": "The boundary of holiness was the final act of the restoration. Jehoiada, who had used the temple as a hiding place for a fugitive king, who had turned its courts into a coronation ground, who had organized a coup from within its precincts — now re-established its sacred boundary. The gates were guarded not against political enemies but against ritual impurity. The house that had sheltered the future king was returned to its proper function: the dwelling place of the holy God, to which only the clean might approach."
    },
    "20": {
      "L": "And he took the captains of hundreds, and the nobles, and the governors of the people, and all the people of the land, and brought down the king from the house of the LORD: and they came through the upper gate into the king's house, and set the king upon the throne of the kingdom.",
      "M": "He took the captains of hundreds, the nobles, the governors, and all the people of the land, and brought the king down from the LORD's house. They came through the upper gate into the palace and seated the king on the royal throne.",
      "T": "The procession from temple to palace carried the symbolic weight of the entire day: the king had been found in the house of God; now he was enthroned in the house of the king. The route through the upper gate was a public procession — every step visible to the city, every face in the crowd a witness to the reversal of six years of false rule. The captains, nobles, governors, and all the people: the entire social structure of the kingdom accompanied the child from sanctuary to throne. The child who had grown up in the temple now sat on the throne that the covenant had always promised his family."
    },
    "21": {
      "L": "And all the people of the land rejoiced, and the city was quiet, after that they had slain Athaliah with the sword.",
      "M": "All the people of the land rejoiced, and the city was at peace after Athaliah had been killed with the sword.",
      "T": "The chapter ends with two things: joy and quiet. The joy was the whole people's — the communal release of six years of legitimate grief at an illegitimate queen, now reversed. The quiet was the peace that comes when the false thing is removed and the true thing is restored. Throughout Chronicles, faithful kings produce rest; the removal of apostasy produces peace. Athaliah's death did not only remove a usurper; it ended the six-year interruption of the Davidic covenant's visible expression. The city was quiet because the city was once again aligned with the covenant."
    }
  },
  "24": {
    "1": {
      "L": "Joash was seven years old when he began to reign, and he reigned forty years in Jerusalem. His mother's name also was Zibiah of Beersheba.",
      "M": "Joash was seven years old when he became king, and he reigned forty years in Jerusalem. His mother was Zibiah of Beersheba.",
      "T": "Seven years old — the child who had been hidden in the temple for six years was now enthroned. He would reign forty years, a reign of extraordinary length. His mother was Zibiah of Beersheba — a Judean woman, not an Omride. The dynasty was now drawing from its own people rather than from the northern apostate house. Beersheba, the ancient site of the patriarchal covenants (Gen 21:31-33; 26:23-25), was a fitting home for the mother of a king whose reign would be defined, at its best, by covenant restoration."
    },
    "2": {
      "L": "And Joash did that which was right in the sight of the LORD all the days of Jehoiada the priest.",
      "M": "Joash did what was right in the sight of the LORD all the days of Jehoiada the priest.",
      "T": "The most important phrase in Joash's biography, and the most sobering: all the days of Jehoiada the priest. The qualification is built into the praise itself. Joash was right — but conditionally, derivatively, dependently. His righteousness was inseparable from the presence of his mentor, protector, and father-figure. What would happen when Jehoiada was no longer present has already been implied by the careful wording of the commendation. The covenant faithfulness of Joash was real; but it was borrowed, not owned."
    },
    "3": {
      "L": "And Jehoiada took for him two wives; and he begat sons and daughters.",
      "M": "Jehoiada chose two wives for him, and he had sons and daughters.",
      "T": "Jehoiada continued to guide the king even in personal matters: he arranged the marriages, ensuring that the Davidic line would have heirs. Two wives, sons and daughters — the covenant continuity of the dynasty secured. The detail is small but it underlines how completely Jehoiada shaped every dimension of Joash's reign. The king who was right in the LORD's sight was also the king whose wives were chosen by the priest."
    },
    "4": {
      "L": "And it came to pass after this, that Joash was minded to repair the house of the LORD.",
      "M": "After this, Joash decided to repair the LORD's house.",
      "T": "The temple repair is the defining project of Joash's faithful years. The house of God had suffered: Athaliah's sons had broken into it and stripped it for Baal worship (v7). The six years of her reign had left it damaged, depleted, dishonored. Joash's decision to repair it was simultaneously a statement about priorities — the house of the LORD comes first — and an act of covenantal piety under Jehoiada's influence. The king who had grown up in the temple now turned his reign's resources toward its restoration."
    },
    "5": {
      "L": "And he gathered together the priests and the Levites, and said to them, Go out unto the cities of Judah, and gather of all Israel money to repair the house of your God from year to year, and see that ye hasten the matter. Howbeit the Levites hastened it not.",
      "M": "He assembled the priests and Levites and told them: 'Go out to the towns of Judah and collect money from all Israel year by year to repair the house of your God. Do this promptly.' But the Levites did not act promptly.",
      "T": "The instruction was clear, the authority legitimate, the urgency stated. But the Levites moved slowly. The Chronicler records this without explanation, which makes the failure more pointed: the sacred system that Jehoiada had restored to full function had already developed institutional inertia. The men tasked with gathering the repair fund for the house of God found reasons to delay. Even the best systems, under the best leadership, struggle with the gap between instruction and execution. Joash had to call Jehoiada to account before the project began in earnest."
    },
    "6": {
      "L": "And the king called for Jehoiada the chief, and said unto him, Why hast thou not required of the Levites to bring in out of Judah and out of Jerusalem the collection, according to the commandment of Moses the servant of God, and of the congregation of Israel, for the tabernacle of witness?",
      "M": "The king summoned Jehoiada the chief priest and asked: 'Why haven't you required the Levites to bring in the contribution from Judah and Jerusalem — the collection ordered by Moses the servant of God and the assembly of Israel for the tent of testimony?'",
      "T": "Joash invoked Moses explicitly: the half-shekel census tax of Exodus 30:11-16 was the biblical precedent for the collection. The king was not inventing a new levy but restoring an ancient covenant provision. The tent of testimony — the tabernacle, the original dwelling place of the LORD before the temple — was the reference point. The temple was the heir of the tabernacle, and the obligation to maintain it descended from the same covenantal legislation that had funded the wilderness sanctuary. Joash's frustration with the Levites was a frustration about covenant obedience, not merely institutional efficiency."
    },
    "7": {
      "L": "For the sons of Athaliah, that wicked woman, had broken up the house of God; and also all the dedicated things of the house of the LORD did they bestow upon Baalim.",
      "M": "For the sons of that wicked woman Athaliah had broken into the house of God and used all its dedicated things for the Baals.",
      "T": "The damage Joash was trying to repair: Athaliah's sons had treated the temple as a resource for Baal worship, stripping the dedicated items — the vessels, the gold, the furnishings consecrated to the LORD — and redirecting them to the Baal shrines. What Moses had prescribed for the tabernacle and David had enriched for the temple had been plundered in six years of apostate rule. Joash's repair project was not routine maintenance; it was the recovery of a house that had been systematically violated."
    },
    "8": {
      "L": "And at the king's commandment they made a chest, and set it without at the gate of the house of the LORD.",
      "M": "At the king's command they made a chest and placed it outside the gate of the LORD's house.",
      "T": "The chest at the gate: a visible, accessible collection point that could receive contributions from anyone entering the temple complex. By placing it outside the gate rather than inside, it was accessible to all who came to worship, not just to priests managing the interior. The parallel account in 2 Kings 12:9 notes that Jehoiada bored a hole in the lid, making it a one-way box that could be filled but not emptied by unauthorized hands. The king wanted accountability; the chest provided it."
    },
    "9": {
      "L": "And they made a proclamation through Judah and Jerusalem, to bring in to the LORD the collection that Moses the servant of God laid upon Israel in the wilderness.",
      "M": "They issued a proclamation throughout Judah and Jerusalem to bring to the LORD the contribution that Moses the servant of God had required of Israel in the wilderness.",
      "T": "The proclamation reached the entire land. This was not a quiet administrative order but a public announcement connecting the temple repair to the Mosaic foundation of Israel's covenant life. 'Moses the servant of God laid upon Israel' — the half-shekel was not Joash's invention; it was Moses's prescription, now being called back into effect. The nation that had forgotten the tabernacle provision in six years of apostasy was being called to remember its covenantal obligations."
    },
    "10": {
      "L": "And all the princes and all the people rejoiced, and brought in, and cast into the chest, until they had made an end.",
      "M": "All the princes and all the people rejoiced and brought their contributions, casting them into the chest until it was full.",
      "T": "They rejoiced. The giving was not grudging or merely compliant; it was celebratory. This was the same spirit that had filled the tabernacle with more gold than could be used (Exod 36:5-7), the same overflow that had followed David's offering for the temple materials (1 Chr 29:9). When the house of God is being restored after desecration, the generosity of the covenant people tends to exceed what was asked. The chest filled quickly. The project that the Levites had delayed was funded by the people's rejoicing."
    },
    "11": {
      "L": "Now it came to pass, that at what time the chest was brought unto the king's office by the hand of the Levites, and when they saw that there was much money, the king's scribe and the high priest's officer came and emptied the chest, and took it, and carried it to his place again. Thus they did day by day, and gathered money in abundance.",
      "M": "Whenever the Levites brought the chest to the king's officers and they saw that there was much money, the king's secretary and the chief priest's officer would come and empty it, then carry it back to its place. They did this day after day and collected a great amount of money.",
      "T": "The accountability system worked: the chest was brought by Levites, emptied in the presence of both the king's secretary and the chief priest's officer, then returned for another day's contributions. Neither party could access the funds alone; joint oversight prevented both royal appropriation and priestly misappropriation. The king who had learned from Jehoiada the importance of the covenant's integrity designed the collection process to honor that integrity. Day after day, the dual oversight worked, and the money accumulated in abundance."
    },
    "12": {
      "L": "And the king and Jehoiada gave it to such as did the work of the service of the house of the LORD, and hired masons and carpenters to repair the house of the LORD, and also such as wrought iron and brass to mend the house of the LORD.",
      "M": "The king and Jehoiada gave the money to those who supervised the work on the LORD's house. They hired masons and carpenters to restore it, and also ironworkers and bronzesmiths to repair it.",
      "T": "The money was directed immediately to the work: craftsmen of all the necessary trades — stone, wood, iron, bronze — were hired and deployed. Jehoiada and the king worked together in direct oversight of the distribution, ensuring the funds reached the work rather than the treasury. This was the practical expression of the covenant principle: resources gathered in the name of God's house were used for God's house. The temple that Athaliah's sons had broken was being rebuilt by the community that her reign had broken."
    },
    "13": {
      "L": "So the workmen wrought, and the work was perfected by them, and they set the house of God in his state, and strengthened it.",
      "M": "So the workmen did their work and completed the repairs. They restored the house of God to its proper condition and reinforced it.",
      "T": "The temple was restored and strengthened: not merely patched but set in its state — a full restoration to its original design and dignity, and then reinforcement beyond what it had been. The work done under Joash exceeded mere repair; it returned the house of God to the condition the LORD deserved and the people needed. The physical restoration of the temple was the material expression of the covenantal restoration Jehoiada had accomplished."
    },
    "14": {
      "L": "And when they had finished it, they brought the rest of the money before the king and Jehoiada, whereof were made vessels for the house of the LORD, even vessels to minister, and to offer withal, and spoons, and vessels of gold and silver. And they offered burnt offerings in the house of the LORD continually all the days of Jehoiada.",
      "M": "When they finished, they brought the remaining money to the king and Jehoiada. From it they made vessels for the LORD's house — vessels for service and offerings, spoons and vessels of gold and silver. They offered burnt offerings in the LORD's house continually all the days of Jehoiada.",
      "T": "The surplus went to what the structural repairs could not provide: the sacred vessels. What Athaliah's sons had stripped for the Baals was now replaced by what the people's rejoicing had funded. The gold and silver spoons, the serving vessels, the implements of worship — all restored from freely-given contributions. And the continuous burnt offerings: the daily sacrifice that marked the house of the LORD as a living sanctuary, not a monument. All the days of Jehoiada — the qualification appears again, as gentle and ominous as the first time. While the priest lived, the offerings continued without interruption."
    },
    "15": {
      "L": "But Jehoiada waxed old, and was full of days when he died; and he was an hundred and thirty years old was he when he died.",
      "M": "But Jehoiada grew old and full of years, and he died at the age of one hundred and thirty.",
      "T": "One hundred and thirty years: the Chronicler records the number without apology or qualification. Jehoiada was given years that matched the scope of his fidelity. He had served through Athaliah's six-year usurpation and Joash's forty-year reign. The fullness of days language echoes the patriarchal death notices — Abraham died 'full of years' (Gen 25:8), Isaac the same (Gen 35:29). The Chronicler uses the formula to mark Jehoiada as a figure of patriarchal stature in the covenant story, a man whose length of life was itself a kind of testimony to the faithfulness he had practiced."
    },
    "16": {
      "L": "And they buried him in the city of David among the kings, because he had done good in Israel, both toward God, and toward his house.",
      "M": "They buried him in the city of David among the kings, because he had served Israel well — both toward God and toward his house.",
      "T": "The priest was buried among kings — an honor not given to any other priest in the entire Old Testament. The reason is stated precisely: he had done good in Israel toward God and toward his house. Not toward his own house — toward God's. Jehoiada's entire public life had been organized around the preservation and service of two things: the covenant God and the covenant king. He had saved Joash, restored the temple, renewed the covenant, organized the worship. He was buried with kings because he had done the work of kings — the work of maintaining the covenant — more faithfully than most kings had."
    },
    "17": {
      "L": "Now after the death of Jehoiada came the princes of Judah, and made obeisance to the king. Then the king hearkened unto them.",
      "M": "After Jehoiada's death, the officials of Judah came and bowed before the king. Then the king listened to them.",
      "T": "The transition is abrupt in the text and devastating in its implication: after Jehoiada died, the nobles came. The king hearkened. That is all the Chronicler needs to say. The same king who had needed Jehoiada to organize his marriages, direct his reform, design his collection system, and maintain his covenant fidelity — that king, now suddenly unguided — listened to the nobles instead. The nobles bowing before the king is a patron-client gesture: we honor you, and we want something in return. What they wanted would cost more than the temple repairs."
    },
    "18": {
      "L": "And they left the house of the LORD God of their fathers, and served groves and idols: and wrath came upon Judah and Jerusalem for this trespass.",
      "M": "They abandoned the house of the LORD, the God of their ancestors, and served the Asherah poles and idols. Wrath came upon Judah and Jerusalem because of this guilt.",
      "T": "The reversal was total. The house of the LORD that Joash had spent his early reign repairing was now forsaken. The Asherah poles and idols that the covenant renewal of chapter 23 had removed were back. The verb abandoned — azab — is the same word Azariah had warned of in 15:2: if you forsake him, he will forsake you. Joash had heard that prophecy during his reign; he had funded its application when he restored the temple. Now he fulfilled the second half of it. The wrath that came upon Judah was covenantally precise: the abandonment brought the consequence the covenant had always promised."
    },
    "19": {
      "L": "Yet he sent prophets to them, to bring them again unto the LORD; and they testified against them: but they would not give ear.",
      "M": "Yet he sent prophets among them to bring them back to the LORD, and they testified against them — but they would not listen.",
      "T": "The grace before the judgment: prophets were sent, the testimony was given, the warning was clear. This is the Chronicler's consistent pattern — before every major punishment in Chronicles, God first sends messengers. The pattern runs through the whole arc of Israel's history: prophets, warnings, rejection, then judgment. The key phrase is 'they would not listen.' Not 'they could not' but 'they would not.' The refusal was chosen. And one of those prophets was the son of the man who had preserved Joash's life. The next verse will name him."
    },
    "20": {
      "L": "And the Spirit of God came upon Zechariah the son of Jehoiada the priest, which stood above the people, and said unto them, Thus saith God, Why transgress ye the commandments of the LORD, that ye cannot prosper? because ye have forsaken the LORD, he hath also forsaken you.",
      "M": "Then the Spirit of God clothed Zechariah son of Jehoiada the priest. He stood above the people and said: 'This is what God says: Why do you transgress the LORD's commandments so that you cannot prosper? Because you have forsaken the LORD, he has forsaken you.'",
      "T": "The Spirit of God clothed Zechariah — the word for clothed (lavash) is the image of the Spirit enveloping a person like a garment, so that what they speak is not their own but God's. Zechariah stood above the people and said what the Spirit gave him: the same message Azariah had spoken to Asa in chapter 15, now applied in its inverse form — you have forsaken the LORD; he has forsaken you. The covenant theorem of 15:2 was exact and inexorable. The prophet who delivered this message was the son of the man who had given Joash everything: his life, his throne, his wives, his temple. The king who owed everything to Jehoiada's faithfulness was now hearing judgment from Jehoiada's own son."
    },
    "21": {
      "L": "And they conspired against him, and stoned him with stones at the commandment of the king in the court of the house of the LORD.",
      "M": "But they conspired against him and, at the king's command, stoned him to death in the court of the LORD's house.",
      "T": "Stoned in the temple court — the very ground where Joash had been crowned, where Jehoiada's coup had played out, where Joash had repaired and beautified. The king commanded the killing of the son of the man who had saved his life, in the place where that salvation had been publicly celebrated. The stoning of Zechariah in the temple court is one of the most shocking moments in Chronicles. Jesus would later cite it as the final prophetic martyrdom of the Old Testament era (Matt 23:35; Luke 11:51), bookending the whole history of Israel's violence against its prophets from Abel's blood to Zechariah's. The blood fell in the courts of the LORD's house."
    },
    "22": {
      "L": "Thus Joash the king remembered not the kindness which Jehoiada his father had done to him, but slew his son. And when he died, he said, The LORD look upon it, and require it.",
      "M": "So King Joash did not remember the kindness that Jehoiada his father had shown him, but killed his son. As Zechariah was dying, he said, 'May the LORD see and avenge.'",
      "T": "Did not remember: the opposite of the great covenant verb zakar — to remember, to act in faithful response to what was done for you. Joash forgot the covenant loyalty of the man who had saved him, hidden him, raised him, and given him everything. And he killed his son. The dying words of Zechariah — 'May the LORD see and avenge' — are the cry of a martyr who has no court of appeal except God. The Hebrew require (darash) is the covenant verb for God acting as avenger of blood, the protector of those who have no other protector. Zechariah entrusted his cause to the only judge who could hear it. This cry echoes through Scripture: Abel's blood crying from the ground (Gen 4:10), the psalmists' laments, and Jesus's own citation of this verse as the watershed of Israel's prophetic martyrdom. The LORD saw. The avenging would not be long."
    },
    "23": {
      "L": "And it came to pass at the end of the year, that the host of Syria came up against him: and they came to Judah and Jerusalem, and destroyed all the princes of the people from among the people, and sent all the spoil of them unto the king of Damascus.",
      "M": "At the turn of the year the Syrian army came against him. They invaded Judah and Jerusalem and destroyed all the leaders of the people, sending all their plunder to the king of Damascus.",
      "T": "At the turn of the year — the season when kings go out to war. The Syrian army came, and all the princes of the people — the very nobles who had come to Joash after Jehoiada's death and led him into apostasy — were killed. The judgment was precise: those who had advised the king to forsake the LORD were the first to fall when the LORD's avenging came. Their plunder went to Damascus. The covenant that had brought wealth to faithful kings now ran in reverse: the resources of Jerusalem's unfaithful rulers were stripped and carried north."
    },
    "24": {
      "L": "For the army of the Syrians came with a small company of men, and the LORD delivered a very great host into their hand, because they had forsaken the LORD God of their fathers. So they executed judgment against Joash.",
      "M": "Though the Syrian army came with only a small force, the LORD handed a very great army over to them, because Judah had abandoned the LORD, the God of their ancestors. Thus they executed judgment on Joash.",
      "T": "The exact reversal of chapter 14. At Mareshah, a vast Cushite army fled before Asa's smaller Judean force — because Asa relied on the LORD. Here, a small Syrian company routed Joash's much larger Judean army — because Judah had forsaken the LORD. The principle is stated explicitly: the LORD handed the great army to the small force. Victory and defeat in Chronicles are never primarily about numbers; they are always about the covenant. The text announces this as 'judgment on Joash' — not random military misfortune but covenantally precise punishment for what had been done in the temple court. Zechariah's dying cry — 'May the LORD see and avenge' — had been heard."
    },
    "25": {
      "L": "And when they were departed from him, (for they left him in great diseases,) his own servants conspired against him for the blood of the son of Jehoiada the priest, and slew him on his bed, and he died: and they buried him in the city of David, but they buried him not in the sepulchres of the kings.",
      "M": "When the Syrians departed they left him severely wounded. His own servants conspired against him because of the blood of the son of Jehoiada the priest, and they killed him on his bed. So he died and was buried in the city of David, but not in the tombs of the kings.",
      "T": "The final indignity: not killed in battle but struck down by his own servants, lying wounded on his bed, unable to defend himself. The motive is named — the blood of Jehoiada's son. The servants who killed Joash did so as avengers of Zechariah's blood, the blood that Joash had commanded to be shed in the temple court. 'May the LORD see and avenge' — the avenging came through the least likely instruments: servants, not soldiers. And the burial: in the city of David but not in the tombs of the kings. The city honored the dynasty; the tombs withheld their honor from the man. The king who had repaired the house of God and then forsaken it, who had benefited from Jehoiada's faithfulness and then murdered his son, was interred at the edge of the dynasty he had disgraced. The Chronicler's silence is the verdict."
    },
    "26": {
      "L": "And these are they that conspired against him; Zabad the son of Shimeath an Ammonitess, and Jehozabad the son of Shimrith a Moabitess.",
      "M": "The conspirators were Zabad son of Shimeath the Ammonite woman, and Jehozabad son of Shimrith the Moabite woman.",
      "T": "The Chronicler preserves the names and the matrilines of Joash's killers. Both were sons of foreign women — an Ammonitess and a Moabitess — serving in the royal household. The detail is not incidental: the king who had received Jehoiada's entirely faithful guidance and rejected it ended his life at the hands of foreign-born servants. The trajectory of Joash's late reign was away from the covenant people and its structures; the agents of his end came from outside those structures."
    },
    "27": {
      "L": "Now concerning his sons, and the greatness of the burdens laid upon him, and the repairing of the house of God, behold, they are written in the story of the book of the kings. And Amaziah his son reigned in his stead.",
      "M": "As for his sons, the many oracles about him, and the rebuilding of the house of God — these are recorded in the commentary on the book of the kings. Amaziah his son succeeded him.",
      "T": "A summary that names three things the Chronicler considers worth noting about Joash's reign: his sons (the continuation of the Davidic line), the burdens and oracles that attended his reign (the covenantal weight of what he did and suffered), and the temple repair (the achievement that defined his faithful years). Amaziah succeeded him: the dynasty continued despite everything. This is the Chronicler's quiet insistence throughout — even when kings fail catastrophically, even when blood falls in the temple court, the covenant line does not break. David's seed endures."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '2chronicles')
        merge_tier(existing, CHRONICLES2, tier_key)
        save(tier_dir, '2chronicles', existing)
    print('2 Chronicles 22–24 written.')

if __name__ == '__main__':
    main()
