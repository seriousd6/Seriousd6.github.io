"""
MKT 2 Chronicles chapters 31–33 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-2chronicles-31-33.py

Content:
- Ch 31: Hezekiah's dismantling of the high places (post-Passover); reorganization of priestly and
         Levitical divisions; collection of tithes and firstfruits; Cononiah's oversight; summary of
         Hezekiah's wholehearted faithfulness
- Ch 32: Sennacherib's invasion and siege threat; Hezekiah's military preparations and speech;
         Sennacherib's blasphemous letters and messengers; Hezekiah and Isaiah pray; the angel
         destroys the Assyrian army; Sennacherib killed by his sons; Hezekiah's illness, pride,
         repentance; his wealth, the Siloam tunnel; the Babylonian envoys test; closing notices
- Ch 33: Manasseh's fifty-five year reign of unprecedented wickedness; idols in the temple;
         child sacrifice in Hinnom; Assyrian captivity; prison-cell repentance; return; partial
         reform; death. Amon's two-year reign; assassination; counter-coup by the people.

Translation decisions (carried forward from mkt-2chronicles-22-24.py):
- H3068 (יהוה): "LORD" in L/M; "the LORD" in T. Consistent throughout OT scripts.
- H430 (אֱלֹהִים): "God" throughout all tiers.
- H7307 (רוּחַ): does not appear prominently in chs 31–33; no decision required here.
- H2617 (חֶסֶד): does not appear directly; no decision required.
- H1285 (בְּרִית): no covenant-ceremony occurrence in these chapters; carried as "covenant" if needed.

New decisions for chs 31–33:
- 31:1 "groves" (H842, asherah poles) — L: "Asherah poles" is more accurate than "groves";
  the word refers to the cult object associated with Asherah worship, not generic forest.
  L: "Asherah poles"; M: "Asherah poles"; T: contextual explanation of the cult object's
  function as a fertility symbol tied to Baal worship.
- 31:19 "fields of the suburbs" — the migrash land attached to Levitical cities for common
  use (Num 35:2-5). L: "fields of common land"; M: "open pasturelands"; T: "the common
  pastureland surrounding their cities."
- 32:1 "the fenced cities" (H1219, betzer) — fortified cities; L: "fortified cities";
  M: "fortified cities"; T: contextual use preserved.
- 32:4 "brook" (H5158, nahal) — a seasonal wadi-brook; L: "brook"; M: "brook"; T: "seasonal
  streambed." Hezekiah's engineering feat (the Siloam tunnel, referenced in v30) is the NT
  backdrop; the first act here is the simpler above-ground diversion.
- 32:8 "arm of flesh" — the Hebrew 'arm' (H2220, zeroa) is the covenant metaphor for active
  power; "arm of flesh" contrasts fallen human strength with divine power. A stark contrast.
  L/M: "an arm of flesh"; T: surfaces the honour-shame contrast and the covenant background.
- 32:21 angel — the LORD sent a malak (H4397/G32 equivalent) who struck the Assyrian camp.
  The parallel is 2 Kgs 19:35: 185,000 killed in one night. The Chronicler does not give the
  number, only the result. L/M: "an angel"; T: notes the devastating brevity of the account.
- 32:25 "did not make return" — the verb shub (H7725) means to turn back, to return, to
  respond in kind. Hezekiah did not respond to the benefit he had received. L: "did not make
  return"; M: "did not respond"; T: "did not give back."
- 32:31 "God left him to himself" — the verb azab (H5800) is the same verb used of Judah
  forsaking the LORD (24:18). God withdrew his guiding presence to test Hezekiah's own heart.
  The parallel to 1 Chr 21:1 (the Satan test / God's anger) is theologically significant.
  L: "God left him"; M: "God withdrew from him"; T: surfaces the testing dynamic.
- 33:6 "burn his sons" — Molech child sacrifice in the Valley of Hinnom (Gehinnom), the same
  valley that later gave its name to Gehenna as a metonym for divine judgment. L: "burned his
  sons as an offering"; M: "burned his sons as offerings"; T: names the valley's full
  theological significance.
- 33:11 "hooks" (H2336, hoah) — likely a nose-hook or cage, a standard Assyrian prisoner
  deportation technique depicted in Assyrian reliefs. L: "with hooks"; M: "with hooks";
  T: "with a hook through his nose, in the style of Assyrian prisoner reliefs."
- 33:12–13 Manasseh's repentance — one of the most theologically remarkable episodes in
  Chronicles: the wickedest king of Judah repents and is restored. The Chronicler alone
  records this. L/M present the facts plainly; T surfaces the theological weight of the grace
  shown to the most evil king.
- 33:23 "incurred guilt more and more" (H7235 + H819) — Amon multiplied his trespass. L:
  "trespassed more and more"; M: "grew more and more guilty"; T: surfaces the contrast with
  Manasseh's trajectory: Manasseh went down and was brought up; Amon went down and stayed.
- Aspect notes:
  - Ch 31: narrative uses waw-consecutive imperfects throughout; the summary of Hezekiah at
    v20-21 shifts to qal perfect, marking it as a completed characterization.
  - Ch 32: Hezekiah's speech to the army (vv6-8) uses imperatives and jussive forms — the
    rhetorical register of military address. Sennacherib's letters use repeated qal perfect
    forms claiming past accomplishments as precedent for future victories. The angel's action
    is a single waw-consecutive imperfect — one stroke, complete.
  - Ch 33: the catalogue of Manasseh's sins (vv3-9) accumulates with relentless waw-
    consecutive imperfects. His humbling (v12) is a qal infinitive absolute + hiphil perfect —
    intensive, complete. His prayer (v13) is answered in a qal perfect (God heard) plus a
    hiphil imperfect (God brought him back). Amon's reign is sparse: he sinned, he multiplied
    guilt, he was killed — the brevity reflects the Chronicler's assessment.
- OT intertextuality:
  - 31:1: echoes 2 Chr 14:3-5 (Asa's removal of altars), 17:6 (Jehoshaphat), and 19:3
    (Jehoshaphat still left high places) — Hezekiah completes the reform work his predecessors
    only partially achieved, and crucially extends it to the northern territory (Ephraim,
    Manasseh) during the post-Passover euphoria.
  - 31:21 "sought his God… with all his heart… and prospered": the exact language of the
    Chronicler's covenant theorem stated positively — cf. 15:2, 26:5. Hezekiah is the model.
  - 32:7-8 "more with us than with them… arm of flesh vs. LORD our God": echoes Elisha's
    word to his servant at Dothan (2 Kgs 6:16 — "those who are with us are more than those
    who are with them") and the principle of 2 Chr 14:11 (Asa: not strength but trust).
  - 32:20 Isaiah + Hezekiah praying together: the Chronicler compresses the story told at
    length in 2 Kgs 18-19 and Isa 36-37. Both sources are explicit sources cited in v32.
  - 32:31 Babylonian envoys: the theological test reads in light of what Hezekiah did with
    those envoys (2 Kgs 20:12-19; Isa 39) — he showed them everything and Isaiah pronounced
    Babylonian captivity as the result. The Chronicler makes God's testing explicit: Hezekiah
    failed his heart test with Babylon, the very empire that would later devour Jerusalem.
  - 33:6 Valley of Hinnom: the site of Ahaz's child sacrifice (2 Chr 28:3); now Manasseh
    repeats and amplifies it. The valley's name (Ben-Hinnom → Gehinnom → Gehenna) became
    NT vocabulary for the place of eschatological judgment.
  - 33:7 "In this house… I will put my name forever": the divine promise of 2 Chr 6-7,
    given at the temple dedication. Manasseh sets an idol precisely where Solomon had received
    that promise — the most direct possible desecration.
  - 33:12-13 Manasseh's repentance: unique to Chronicles. The Books of Kings condemn Manasseh
    categorically (2 Kgs 21:1-18) and make his sins the ultimate cause of Jerusalem's later
    fall (2 Kgs 24:3-4). Chronicles shows God's grace even to him — the worst becoming an
    instance of the covenant theorem operating in extremis. The prayer of Manasseh (an
    apocryphal text, not canonical) expands this scene.
  - 33:25 "the people of the land" (am-ha'aretz) put Josiah on the throne — the same
    constituency that crowned Joash after Athaliah's death (23:20-21). A recurring pattern:
    when royal succession is disrupted by conspiracy, the covenant people themselves restore it.
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
  "31": {
    "1": {
      "L": "Now when all this was finished, all Israel that were present went out to the cities of Judah, and brake the images in pieces, and cut down the groves, and threw down the high places and the altars out of all Judah and Benjamin, in Ephraim also and Manasseh, until they had utterly destroyed them all. Then all the children of Israel returned, every man to his possession, into their own cities.",
      "M": "When all this was finished, all the Israelites present went out to the towns of Judah and smashed the sacred pillars, cut down the Asherah poles, and demolished the high places and altars throughout Judah and Benjamin, and in Ephraim and Manasseh as well, until they had destroyed them all. Then all the people of Israel returned, each to his own property in his own city.",
      "T": "The Passover had lit a fire that could not be contained inside Jerusalem. After the celebration ended, the gathered Israelites — northerners and southerners together, in a moment of rare unity — went out across the land and dismantled everything that the covenant forbade. The Asherah poles, the high places, the stone pillars: the whole apparatus of Canaanite-derived worship that had survived in Judah through the reigns of compromised kings was now pulled down, not by royal decree alone but by the people themselves, with their own hands. They went not only through Judah and Benjamin but into the former northern territories of Ephraim and Manasseh — a remarkable reach, showing the extent of the Passover's spiritual momentum. Then they returned to their own cities. The reform was thorough because it was popular."
    },
    "2": {
      "L": "And Hezekiah appointed the courses of the priests and the Levites after their courses, every man according to his service, the priests and Levites for burnt offerings and for peace offerings, to minister, and to give thanks, and to praise in the gates of the camp of the LORD.",
      "M": "Hezekiah organized the divisions of the priests and Levites according to their assignments, each in his specific service — priests and Levites for burnt offerings and peace offerings, for ministering, for giving thanks, and for praising at the gates of the LORD's encampment.",
      "T": "The reform required structure to sustain it. Hezekiah did not leave the temple worship to improvise; he organized it with the precision of David's original plan. The priests in their divisions, the Levites in their assignments, each person with a defined role. The phrase 'the gates of the LORD's camp' (machaneh) is unusual — it frames the temple as a military encampment, the LORD's dwelling among his host, with the priestly corps as his standing guard and service staff. The burnt offerings maintained the constant consecration; the peace offerings marked communion and celebration; the ministry, thanksgiving, and praise were the daily texture of a people living before their God."
    },
    "3": {
      "L": "He appointed also the king's portion of his substance for the burnt offerings, to wit, for the morning and evening burnt offerings, and the burnt offerings for the sabbaths, and for the new moons, and for the set feasts, as it is written in the law of the LORD.",
      "M": "The king contributed from his own possessions the burnt offerings: the morning and evening burnt offerings, and those for the Sabbaths, new moons, and appointed feasts, as prescribed in the law of the LORD.",
      "T": "The king funded the public worship out of his personal wealth. The daily burnt offerings — morning and evening — were the heartbeat of the sanctuary; the Sabbath and new moon offerings marked the rhythms of sacred time; the feast-day offerings marked the covenant calendar's high points. All of it was 'as written in the law of the LORD' — Hezekiah was not inventing a personal piety but restoring the Mosaic system precisely as prescribed. A king who funds the worship of his God from his own substance rather than diverting temple revenue to himself was, in the Chronicler's framework, a king in right covenant relationship."
    },
    "4": {
      "L": "Moreover he commanded the people that dwelt in Jerusalem to give the portion of the priests and the Levites, that they might be encouraged in the law of the LORD.",
      "M": "He commanded the people living in Jerusalem to give the portion due to the priests and Levites, so that they could devote themselves fully to the law of the LORD.",
      "T": "The logic is simple and important: priests and Levites who must scramble for their own food cannot devote themselves to study and service of the Torah. Hezekiah commanded the Jerusalem residents to fund the sacred workers so that the sacred workers could do their work without distraction. The 'portion' (manah) was the customary allotment — their income from the worship system. A well-funded priesthood was the precondition of a well-taught people. Hezekiah understood that institutional support for the ministers of the word was not generosity but covenant common sense."
    },
    "5": {
      "L": "And as soon as the commandment came abroad, the children of Israel brought in abundance the firstfruits of corn, wine, and oil, and honey, and of all the increase of the field; and the tithe of all things brought they in abundantly.",
      "M": "As soon as the order spread, the Israelites brought in abundance the firstfruits of grain, wine, oil, honey, and all the produce of the field, and they brought in the tithe of everything in abundance.",
      "T": "The response to the command was not reluctant compliance but overflow. The word went out, and the firstfruits came: grain, wine, oil, honey — the whole range of the land's produce, representing the best of everything the ground had given. Then the tithes of all things, in abundance. The same spirit that had filled Solomon's temple dedication (2 Chr 7) and funded the temple repair under Joash (24:10) — the spontaneous generosity of a people whose hearts have been turned — was at work again. When the covenant is alive, the people give more than is asked."
    },
    "6": {
      "L": "And concerning the children of Israel and Judah, that dwelt in the cities of Judah, they also brought in the tithe of oxen and sheep, and the tithe of holy things which were consecrated unto the LORD their God, and laid them by heaps.",
      "M": "The people of Israel and Judah living in the towns of Judah also brought in the tithe of cattle and sheep and the tithe of the dedicated things consecrated to the LORD their God, laying them out in heaps.",
      "T": "Not just agricultural produce but livestock — cattle, sheep — and the dedicated things already set apart for the LORD. The combination produced a visual spectacle: heaps of goods piling up in and around the temple precincts. The tithe of the dedicated things is a supplementary category — items already formally consecrated to the LORD, now being brought to their proper place. The breadth of the giving — grain, oil, honey, livestock, dedicated items — represented the full range of the economy of a pastoral-agricultural society. Nothing productive was exempt from the covenant's claim."
    },
    "7": {
      "L": "In the third month they began to lay the foundation of the heaps, and finished them in the seventh month.",
      "M": "They began piling up the heaps in the third month and finished in the seventh month.",
      "T": "Four months of accumulation: from the third month (Sivan — the month of the harvest festival, Shavuot) to the seventh (Tishri — the month of Rosh Hashanah, Yom Kippur, and Sukkot). The calendar marks the high point of the agricultural cycle, the season of harvests and offerings. The heaps grew for the entire harvest quarter and into the autumn festival season. By the time they were finished, the visual evidence of Israel's covenantal response was impossible to ignore."
    },
    "8": {
      "L": "And when Hezekiah and the princes came and saw the heaps, they blessed the LORD, and his people Israel.",
      "M": "When Hezekiah and the officials came and saw the heaps, they blessed the LORD and his people Israel.",
      "T": "The heaps were a sign, and Hezekiah read the sign correctly. He and the officials blessed the LORD — thanking God for the people's response, recognizing the abundance as evidence of divine favor. Then they blessed the people — acknowledging that what the people had done was an act of covenant faithfulness worthy of honor. The blessing of the people by the king echoes the great moments of covenant celebration in Israel's history: Moses blessing the people at the tabernacle's completion (Exod 39:43), Solomon blessing the assembly at the temple dedication (1 Kgs 8:14). The heaps of tithes were the people's answer to the question of whether Hezekiah's reform had taken hold."
    },
    "9": {
      "L": "Then Hezekiah questioned with the priests and the Levites concerning the heaps.",
      "M": "Hezekiah questioned the priests and the Levites about the heaps.",
      "T": "A brief verse that sets up the answer to come. The king wanted to understand what he was seeing. The piles were large — larger than could be accounted for by normal temple operations. Hezekiah questioned the administrators of the system: priests, Levites, those who knew the numbers. He was not suspicious; the context is wonder. He needed to hear from those who managed the collections what the abundance meant."
    },
    "10": {
      "L": "And Azariah the chief priest of the house of Zadok answered him, and said, Since the people began to bring the offerings into the house of the LORD, we have had enough to eat, and have left plenty: for the LORD hath blessed his people; and that which is left is this great store.",
      "M": "Azariah the chief priest of the house of Zadok answered him: 'Since the people began bringing offerings to the LORD's house, we have had enough to eat, with plenty left over — for the LORD has blessed his people, and what remains is this great abundance.'",
      "T": "The chief priest's answer is a testimony: the system the Mosaic law designed, when operating as intended, produces abundance. The priests had been eating — fully, sufficiently — and there was still this enormous surplus. Azariah named the reason directly: the LORD has blessed his people. The abundance was not merely organizational success; it was theological evidence. When the covenant is honored, the covenant God responds with provision. The great store remaining was not just food; it was a material sign of divine favor on a people that had returned to their God with their whole heart."
    },
    "11": {
      "L": "Then Hezekiah commanded to prepare chambers in the house of the LORD; and they prepared them,",
      "M": "Hezekiah commanded that storage chambers be prepared in the house of the LORD, and they prepared them.",
      "T": "The practical response to the theological abundance: build storage. The surplus that testified to God's blessing needed to be housed properly, managed wisely, and distributed fairly. Hezekiah immediately turned gratitude into administration. The temple complex had rooms — the same word used for the chamber in which Joash had been hidden (22:11) — and now those rooms would hold the overflow of the people's offering. The house of God would store what the people of God had given."
    },
    "12": {
      "L": "And brought in the offerings and the tithes and the dedicated things faithfully: over which Cononiah the Levite was ruler, and Shimei his brother was the next.",
      "M": "They faithfully brought in the contributions, tithes, and dedicated things. Cononiah the Levite was in charge of them, with his brother Shimei as his assistant.",
      "T": "The key word is 'faithfully' (emunaah) — the same root as 'amen,' the word for reliable, steadfast, trustworthy action. The collections were handled with integrity. Cononiah the Levite was the chief administrator — his name means 'the LORD has established' — and his brother Shimei supported him. The naming of specific administrators signals accountability: these were real people with real responsibility for real goods dedicated to the real God. Faithful stewardship of holy things is itself an act of worship."
    },
    "13": {
      "L": "And Jehiel, and Azaziah, and Nahath, and Asahel, and Jerimoth, and Jozabad, and Eliel, and Ismachiah, and Mahath, and Benaiah, were overseers under the hand of Cononiah and Shimei his brother, at the commandment of Hezekiah the king, and Azariah the ruler of the house of God.",
      "M": "Jehiel, Azaziah, Nahath, Asahel, Jerimoth, Jozabad, Eliel, Ismachiah, Mahath, and Benaiah were overseers under Cononiah and Shimei his brother, by appointment of King Hezekiah and Azariah the chief officer of the house of God.",
      "T": "Ten overseers under Cononiah and Shimei: a distribution of supervisory authority that prevented any single person from controlling the flow of dedicated goods. The appointment came from both the king and the chief officer of the temple — dual authority, civil and sacred, watching over the same operation. The Chronicler's careful naming of these officials serves the same purpose as the accountability system Joash built for the temple repair fund: when holy goods are handled, the community needs to know who is responsible and by whose authority they act."
    },
    "14": {
      "L": "And Kore the son of Imnah the Levite, the porter toward the east, was over the freewill offerings of God, to distribute the oblations of the LORD, and the most holy things.",
      "M": "Kore son of Imnah the Levite, keeper of the East Gate, was in charge of the freewill offerings to God, distributing the contributions reserved for the LORD and the most holy things.",
      "T": "The East Gate keeper — a significant position, since the East Gate was the primary entrance to the temple courts. Kore son of Imnah managed the freewill offerings, which were given beyond the required tithes and firstfruits, and was responsible for distributing the most holy things — the portions of the offerings that belonged to the priests for their consumption. The freewill offerings, precisely because they were voluntary, were the thermometer of the community's heart. Managing them well required both integrity and discernment."
    },
    "15": {
      "L": "And next him were Eden, and Miniamin, and Jeshua, and Shemaiah, Amariah, and Shecaniah, in the cities of the priests, in their set office, to give to their brethren by courses, as well to the great as to the small:",
      "M": "Under him were Eden, Miniamin, Jeshua, Shemaiah, Amariah, and Shecaniah in the priestly cities, faithfully distributing portions to their brothers in the priestly divisions, great and small alike.",
      "T": "Six assistants for the distribution network across the priestly cities — the Levitical towns scattered throughout Judah where the priests and their families lived. The distribution reached everyone: great and small alike. Seniority or status did not determine access to the covenant provision; the system was designed for equity. The priests in the outlying cities were not disadvantaged relative to those in Jerusalem. The whole network, from Cononiah at the center to these six in the towns, was built for thoroughness and fairness."
    },
    "16": {
      "L": "Beside their genealogy of males, from three years old and upward, even unto every one that entereth into the house of the LORD, his daily portion for their service in their charges according to their courses;",
      "M": "Besides those enrolled by genealogy, they also distributed daily portions to every male from three years old and upward who entered the LORD's house, for their service in their assignments by their divisions.",
      "T": "The distribution was not limited to adult priests in active service. From three years old — the age at which temple ministry might begin in a preparatory sense, when a child could be presented and begin to learn — every male who came to the house of the LORD received his daily portion. The genealogical rolls and the daily presence both created claims. A child old enough to come to the temple was old enough to receive the covenant's provision. The system was designed to sustain the entire priestly household across generations."
    },
    "17": {
      "L": "Both to the genealogy of the priests by the house of their fathers, and the Levites from twenty years old and upward, in their charges by their courses;",
      "M": "This included the priests enrolled by their ancestral families and the Levites from twenty years old and upward, in their assigned positions by their divisions.",
      "T": "A double register: the priests enrolled by ancestral lineage — their right to serve derived from birth — and the Levites from twenty years old upward. Twenty was the age at which Levites entered active service (cf. 1 Chr 23:24-27, where David adjusted the entry age from thirty to twenty). The distinction between priestly genealogical enrollment and Levitical age-based enrollment reflects the different qualifications for each: the priests' standing was hereditary through Aaron; the Levites' service began with maturity and training."
    },
    "18": {
      "L": "And to the genealogy of all their little ones, their wives, and their sons, and their daughters, through all the congregation: for in their set office they sanctified themselves in holiness:",
      "M": "And included in the genealogy were all their little children, their wives, their sons and daughters — the entire assembly — for they faithfully consecrated themselves in holiness.",
      "T": "The provision extended to the entire household: wives, sons, daughters, little ones — everyone dependent on the priest or Levite received care from the covenant system. The reason given is significant: they consecrated themselves in holiness. The families of those set apart for holy service were themselves part of the holy community. The provision was not merely welfare; it was recognition of the priestly household's corporate consecration. When a man gives himself to the service of God's house, his family shares in both the vocation and the provision."
    },
    "19": {
      "L": "Also of the sons of Aaron the priests, which were in the fields of the suburbs of their cities, in every several city, the men that were expressed by name, to give portions to all the males among the priests, and to all that were reckoned by genealogies among the Levites.",
      "M": "Also for the sons of Aaron the priests who lived in the common pasturelands of their cities, designated men were appointed by name in every city to distribute portions to every male among the priests and to all Levites enrolled by genealogy.",
      "T": "The system reached the farthest edge of the priestly network: the priests living not in Jerusalem but in the open pasturelands around their assigned Levitical cities, the migrash — the common land that Mosaic law had set aside for Levitical use (Num 35:2-5). These were the rural priests, the ones easiest to overlook in an administrative system organized around the central sanctuary. Hezekiah made sure that named individuals in every city were responsible for their portion. No priest anywhere in the network fell through the gaps. The reform was not a Jerusalem phenomenon; it was national."
    },
    "20": {
      "L": "And thus did Hezekiah throughout all Judah, and wrought that which was good and right and truth before the LORD his God.",
      "M": "Thus Hezekiah acted throughout all Judah, doing what was good and right and faithful before the LORD his God.",
      "T": "The summary reaches across the whole chapter. What Hezekiah did throughout Judah — the purge of high places, the organization of the temple personnel, the collection and distribution of tithes — was, in the Chronicler's compressed moral vocabulary, 'good and right and faithful' before the LORD. Three words that together describe covenant integrity in its completeness: good in character, right in conduct, and faithful — emet, truth, the quality of doing what one says, of covenant reliability. Hezekiah's reign, at this point, is the positive model the Chronicler will use to measure all subsequent failures."
    },
    "21": {
      "L": "And in every work that he began in the service of the house of God, and in the law, and in the commandments, to seek his God, he did it with all his heart, and prospered.",
      "M": "In every work he undertook in the service of the house of God, in the law, and in the commandments, seeking his God with all his heart — he prospered.",
      "T": "The covenant theorem stated in its most complete positive form: seeking God with the whole heart produces prosperity. The Chronicler established this principle in 15:2 (Azariah to Asa: 'If you seek him, he will be found by you') and illustrated it through generations of kings. Hezekiah embodies the theorem perfectly — his service was total, his law-keeping was from the heart, his seeking was undivided, and the result was prosperity. The word for prospered (tsalach) carries the sense of a project breaking through, succeeding against resistance. Everything Hezekiah put his hand to moved forward. This is the high point of the narrative; the next chapter will immediately test whether that prosperity can survive the pressure of empire."
    }
  },
  "32": {
    "1": {
      "L": "After these things, and the establishment thereof, Sennacherib king of Assyria came, and entered into Judah, and encamped against the fenced cities, and thought to win them for himself.",
      "M": "After these acts of faithfulness, Sennacherib king of Assyria came and invaded Judah, encamping against the fortified cities and intending to take them by force.",
      "T": "The word 'after' is deliberately ominous: after all the faithfulness, the reform, the tithes, the covenant renewal — immediately after — Sennacherib arrived. The Chronicler does not soften the apparent contradiction: Hezekiah did everything right, and the empire came anyway. This is the testing that 32:31 will later name explicitly. The Assyrian king did not enter Judah as a passing threat; he encamped against the fortified cities with the intention of permanent conquest. Hezekiah had just built a kingdom on the covenant; now he would find out whether the covenant was enough."
    },
    "2": {
      "L": "And when Hezekiah saw that Sennacherib was come, and that he was purposed to fight against Jerusalem,",
      "M": "When Hezekiah saw that Sennacherib had come with the intention of fighting against Jerusalem,",
      "T": "Hezekiah saw — the verb is simple but the situation is stark. The greatest military power in the world had entered his territory and fixed its eye on Jerusalem. The city where the LORD had placed his name, where the temple stood, where the tithes had just been piled in abundance, was about to be besieged by an army that had never failed to take a city it set out to take. Hezekiah's response in the next verses will show whether his covenant confidence was performative or real."
    },
    "3": {
      "L": "He took counsel with his princes and his mighty men to stop the waters of the fountains which were without the city: and they did help him.",
      "M": "He consulted his officials and military commanders about stopping up the water sources outside the city. They agreed to help him.",
      "T": "The first strategic decision: deny the enemy water. The springs and streams outside Jerusalem's walls would supply a besieging army for months; Hezekiah decided to deprive them of that resource. His officials and commanders agreed — a good sign that the leadership was unified behind the king's resolve. The engineering project that followed (referenced in v30 — the Siloam tunnel) was the permanent solution; the immediate work here was the above-ground diversion. Practical wisdom and faith are not opposites in Chronicles: Hezekiah trusted the LORD and also closed the springs."
    },
    "4": {
      "L": "So there was gathered much people together, who stopped all the fountains, and the brook that ran through the midst of the land, saying, Why should the kings of Assyria come, and find much water?",
      "M": "A large force assembled and stopped up all the springs and the brook running through the region, saying, 'Why should the kings of Assyria come and find plenty of water?'",
      "T": "The entire community mobilized. Stopping water sources was not merely an engineering task but a statement of corporate defiance: we will not make this easy for you. The question the workers asked — 'why should the kings of Assyria find water here?' — captures the spirit of active resistance. They were not passive victims waiting for divine rescue; they were a covenant community doing everything within their human power and expecting God to do what was beyond their power. The brook running through the region may refer to the Kidron or a surface channel of the Gihon, which the later tunnel made unnecessary."
    },
    "5": {
      "L": "Also he strengthened himself, and built up all the wall that was broken down, and raised it up to the towers, and another wall without, and repaired Millo in the city of David, and made darts and shields in abundance.",
      "M": "He also strengthened himself and rebuilt all the broken-down sections of the wall, raised it up to the towers, built another wall outside it, reinforced the Millo in the city of David, and made weapons and shields in great quantities.",
      "T": "Walls, towers, an outer wall, the Millo — the full engineering vocabulary of a city preparing for siege. The Millo was the ancient fill structure in the city of David, perhaps a terracing system, which had been part of Jerusalem's defenses since David's time (2 Sam 5:9). Hezekiah strengthened everything. Weapons and shields in abundance: the city's garrison was armed. The preparation was comprehensive and energetic. A king who says 'the LORD is with us' and then builds walls understands something important: faith does not cancel prudence; it enables it."
    },
    "6": {
      "L": "And he set captains of war over the people, and gathered them together to him in the street of the gate of the city, and spake comfortably to them, saying,",
      "M": "He appointed military commanders over the people, assembled them in the city gate square, and spoke encouragingly to them:",
      "T": "Command structure, assembly, address: the three elements of military leadership before a siege. The city gate square was the traditional civic gathering point — where legal decisions were made, where leaders addressed the people, where the community's public life happened. Hezekiah gathered everyone there. His speech would not be tactical instructions but spiritual grounding. The organizational work was done; now the people needed to know what they were fighting for and who was with them."
    },
    "7": {
      "L": "Be strong and courageous, be not afraid nor dismayed for the king of Assyria, nor for all the multitude that is with him: for there be more with us than with him:",
      "M": "Be strong and courageous. Do not be afraid or dismayed before the king of Assyria and all the horde with him, for there are more with us than with him.",
      "T": "The echo is deliberate: Elisha had said exactly this to his terrified servant at Dothan when surrounded by Aramean forces — 'Those who are with us are more than those who are with them' (2 Kgs 6:16). Hezekiah was not coining a new theology; he was repeating the standing testimony of Israel's history. The invisible army that protects the covenant community has always outnumbered the visible armies that oppose it. 'Be strong and courageous' is the language of Joshua's commissioning (Josh 1:6-9) — the command given to those who are about to face what they cannot handle in their own strength, and who therefore must rely on a strength not their own."
    },
    "8": {
      "L": "With him is an arm of flesh; but with us is the LORD our God to help us, and to fight our battles. And the people rested themselves upon the words of Hezekiah king of Judah.",
      "M": "With him is an arm of flesh, but with us is the LORD our God to help us and to fight our battles.' And the people took confidence from the words of Hezekiah king of Judah.",
      "T": "An arm of flesh: the entire military might of Assyria — its infantry, cavalry, siege engineers, the veterans of a hundred conquests — reduced to a single phrase. Flesh, the material of creaturely existence, strong until it fails. Against that arm stands the LORD. The contrast is not between two arms of equal but different kinds; it is between creaturely power and the Creator who made and sustains all things. The people rested themselves upon these words. The verb suggests a physical leaning, a weight transferred — as a tired man leans against a wall, the people transferred the weight of their fear to the king's words, and through the king's words to the God the words named. The army outside the walls had not changed; but the people inside them had."
    },
    "9": {
      "L": "After this did Sennacherib king of Assyria send his servants to Jerusalem, (but he himself laid siege against Lachish, and all his power with him,) unto Hezekiah king of Judah, and unto all Judah that were at Jerusalem, saying,",
      "M": "After this, while Sennacherib king of Assyria was at Lachish with all his forces laying siege to it, he sent his officials to Jerusalem with a message to Hezekiah king of Judah and all the people of Judah who were in Jerusalem.",
      "T": "The siege of Lachish is attested in Assyrian reliefs and annals — Sennacherib had it depicted on the walls of his palace at Nineveh, proud enough of its capture to commission a room-length tableau of the assault. From that siege, with Judah's second city in his hands, he sent a delegation to Jerusalem. The tactic was psychological: soften the capital while the king himself watched another city fall. The words his servants brought were designed to replicate in Jerusalem the demoralization that siege conditions produced elsewhere — without a single arrow being fired at the city gates."
    },
    "10": {
      "L": "Thus saith Sennacherib king of Assyria, Whereon do ye trust, that ye abide in the siege in Jerusalem?",
      "M": "Sennacherib king of Assyria says this: On what are you relying, that you remain in Jerusalem under siege?",
      "T": "The opening question targets the city's spiritual center: what are you trusting? Sennacherib had heard Hezekiah's answer in v8 — 'the LORD our God is with us' — and he was about to systematically dismantle that confidence. The question 'on what do you trust?' is the most important question that can be asked of any community under pressure. Hezekiah's answer had been right. Sennacherib was about to argue that the right answer was wrong. The battle for Jerusalem would be fought in the minds of its defenders before it was fought at its walls."
    },
    "11": {
      "L": "Doth not Hezekiah persuade you to give over yourselves to die by famine and by thirst, saying, The LORD our God shall deliver us out of the hand of the king of Assyria?",
      "M": "Is not Hezekiah deceiving you into surrendering yourselves to death by famine and thirst when he says, 'The LORD our God will deliver us from the hand of the king of Assyria'?",
      "T": "The message reframes Hezekiah's faith as manipulation. The king who has closed the springs and strengthened the walls is accused of engineering his own people's death. The Assyrian logic: if you trust a god who cannot deliver, you will stay in a city that will starve. The argument was not purely cynical — sieges did produce famine, and the outcome of such sieges was reliably the same across the ancient Near East. Sennacherib was using history as a weapon. But the Chronicler places this speech alongside Hezekiah's speech precisely to let the reader hear the clash of two worldviews — and then watch which one was right."
    },
    "12": {
      "L": "Hath not the same Hezekiah taken away his high places and his altars, and commanded Judah and Jerusalem, saying, Ye shall worship before one altar, and burn incense upon it?",
      "M": "Has not this same Hezekiah removed his high places and altars and commanded Judah and Jerusalem: 'You shall worship before one altar and burn incense upon it'?",
      "T": "Sennacherib's most sophisticated argument: Hezekiah has offended the Judean gods by tearing down their shrines. By removing the high places and centralizing worship at the Jerusalem altar, Hezekiah has, in Assyrian theological logic, alienated the regional deities who might have protected Judah. The argument would have made perfect sense to anyone with a polytheistic framework: more shrines meant more divine protection; fewer shrines meant fewer gods willing to fight for you. Hezekiah had reduced Judah's divine protection — or so the Assyrian framing went. The argument only failed if the LORD was not one god among many but the only God, and if Hezekiah's centralization had been exactly what that one God required."
    },
    "13": {
      "L": "Know ye not what I and my fathers have done unto all the people of other lands? were the gods of the nations of those lands any ways able to deliver their lands out of mine hand?",
      "M": "Do you not know what I and my fathers have done to all the peoples of other lands? Were the gods of those nations able to deliver their lands from my hand?",
      "T": "The appeal to history: a catalog of imperial success deployed as theological argument. Sennacherib was not wrong about the facts. Nation after nation had fallen to Assyria; their gods had not stopped the advance. The Assyrian empire in 701 BC was the most successful military machine in history to that point, and its track record with besieged cities was perfect. From a purely empirical standpoint, Sennacherib's argument was unassailable. Every city that had trusted its gods had fallen. Every god had proven insufficient against the Assyrian war machine. The argument failed not on historical grounds but on categorical grounds: the LORD was not a national deity like Baal or Marduk; he was the Creator before whom Sennacherib himself existed."
    },
    "14": {
      "L": "Who was there among all the gods of those nations that my fathers utterly destroyed, that could deliver his people out of mine hand, that your God should be able to deliver you out of my hand?",
      "M": "Who among all the gods of those nations that my fathers devoted to destruction was able to deliver his people from my hand? How then can your God deliver you from my hand?",
      "T": "The rhetorical question assumes the answer: none. No god had delivered. Therefore your God cannot deliver. The logic is sound within its own framework, but the framework contains a fatal error: the equation of the LORD with the gods of the nations. Sennacherib had catalogued gods he had defeated. He was about to find out that he had not been fighting gods but idols — objects that could neither act nor resist — and that the God of Jerusalem was of a different order altogether. The arrogance of Sennacherib was not ignorance but theological error dressed up as empirical confidence."
    },
    "15": {
      "L": "Now therefore let not Hezekiah deceive you, nor persuade you on this manner, neither yet believe him: for no god of any nation or kingdom was able to deliver his people out of mine hand, and out of the hand of my fathers: how much less shall your God deliver you out of my hand?",
      "M": "Therefore do not let Hezekiah deceive or mislead you in this way. Do not believe him, for no god of any nation or kingdom has been able to deliver his people from my hand or from the hand of my fathers. How much less, then, will your God deliver you out of my hand?",
      "T": "The climax of the argument: categorical denial of any possible divine rescue, with 'how much less your God' as the final blow. The Assyrian messenger has saved the most insulting claim for last — your God is not only unable to deliver you, he is less able than the gods that have already failed. It was a brilliant piece of psychological warfare designed to produce exactly one response: despair, and then surrender. The messengers were not making a theological argument in good faith; they were trying to break the will of a city that had just spent its Passover week renewing its covenant with its God. The speech ends, and the next verse will skip to the response — Hezekiah and Isaiah praying."
    },
    "16": {
      "L": "And his servants spake yet more against the LORD God, and against his servant Hezekiah.",
      "M": "His servants said still more against the LORD God and against his servant Hezekiah.",
      "T": "The Chronicler summarizes without quoting: there was more, and it was worse. The delegation's full speech went beyond even what has been recorded. The target was double — the LORD God and his servant Hezekiah. To attack the king was to attack the king's God, and to attack the God was to undermine the king. The strategy was coherent: destroy confidence in the covenant and you destroy the will to resist. What the servants said is not recorded, but the Chronicler's summary says enough: they spoke against the LORD God. That categorization carries its own verdict. History would judge who was right."
    },
    "17": {
      "L": "He wrote also letters to rail on the LORD God of Israel, and to speak against him, saying, As the gods of the nations of other lands have not delivered their people out of mine hand, so shall not the God of Hezekiah deliver his people out of mine hand.",
      "M": "He also wrote letters to insult the LORD, the God of Israel, saying: 'As the gods of the nations of other lands did not deliver their people from my hand, so the God of Hezekiah will not deliver his people from my hand.'",
      "T": "Written correspondence: the insult was made permanent, official, documented. The letter reduced the LORD to a comparandum — one more national deity in Sennacherib's collection of defeated gods. The parallel sentence construction ('as they did not... so he will not') was a confident prediction. Sennacherib's letter went to Hezekiah; we know from Isaiah 37 what Hezekiah did with it. He spread it before the LORD in the temple and prayed over it. The letter designed to produce despair became the occasion for one of the great prayers of the Old Testament. What Sennacherib wrote as a threat, Hezekiah turned into a petition."
    },
    "18": {
      "L": "Then they cried with a loud voice in the Jews' language unto the people of Jerusalem that were on the wall, to affright them, and to trouble them; that they might take the city.",
      "M": "They cried out in a loud voice in the Judean language to the people of Jerusalem on the wall, trying to frighten and terrify them in order to capture the city.",
      "T": "The switch to the Judean language (Hebrew) was deliberate. The Assyrian officials knew that Aramaic was the diplomatic language — used in public settings so that the common people could not understand negotiations (cf. 2 Kgs 18:26, where Hezekiah's officials ask Sennacherib's delegation to speak Aramaic rather than Hebrew). The Assyrian messengers rejected that convention. They shouted in Hebrew, directly at the people on the walls, bypassing the leadership to work on the population directly. The psychological warfare was targeting the most vulnerable layer: the ordinary soldiers and civilians who would have to endure the siege and who might not share their king's faith."
    },
    "19": {
      "L": "And they spake against the God of Jerusalem, as against the gods of the people of the earth, which were the work of men's hands.",
      "M": "They spoke against the God of Jerusalem as they would speak against the gods of the peoples of the earth — gods that are the work of human hands.",
      "T": "The Chronicler's editorial note is devastating in its irony: they equated the LORD with gods that are the work of human hands. They had the categories exactly inverted. The idols of the nations that Assyria had defeated were indeed the work of human hands — wood, stone, metal shaped by craftsmen. The God of Jerusalem was the one who had made human hands, and everything else. Sennacherib's entire theological argument rested on a category error so fundamental that its refutation required not a clever argument but a night's work by a single angel."
    },
    "20": {
      "L": "And for this cause Hezekiah the king, and the prophet Isaiah the son of Amoz, prayed and cried to heaven.",
      "M": "Because of this, King Hezekiah and the prophet Isaiah son of Amoz prayed and cried out to heaven.",
      "T": "Two men praying: the king and the prophet, the political authority and the prophetic voice, together crying to heaven. The Chronicler compresses into a single verse what the parallel accounts in 2 Kings 19 and Isaiah 37 expand into prayers and oracles. But the compression is itself theological: the content of the prayer is not the point. The direction is the point — to heaven, to the God who is not made of human hands, to the LORD whom Sennacherib had just compared to blocks of wood. Hezekiah and Isaiah took the insult to the one who had been insulted, and left the response in his hands."
    },
    "21": {
      "L": "And the LORD sent an angel, which cut off all the mighty men of valour, and the leaders and captains in the camp of the king of Assyria. So he returned with shame to his own land. And when he was come into the house of his god, they that came forth of his own bowels slew him there with the sword.",
      "M": "And the LORD sent an angel who struck down every mighty warrior, commander, and officer in the camp of the king of Assyria. Sennacherib returned to his own land in disgrace. When he entered the house of his god, his own sons cut him down with the sword.",
      "T": "One verse for the defeat of the greatest empire in the world. The brevity is the point. The LORD sent an angel — one agent, one night (2 Kgs 19:35 says 185,000 soldiers died before morning). Every commander and officer, the entire military leadership, struck down. Sennacherib went home. The king who had written letters boasting of his ability to overcome any god returned to his own country in shame — the Hebrew word is the covenant word for dishonor, the opposite of the glory he had claimed. And the final humiliation: not killed in battle by an enemy army, but cut down in his own temple by his own sons. The God he had mocked as unable to deliver his people did not need to lift a weapon himself. One angel, and then the empire's own household, finished the job."
    },
    "22": {
      "L": "Thus the LORD saved Hezekiah and the inhabitants of Jerusalem from the hand of Sennacherib the king of Assyria, and from the hand of all other, and guided them on every side.",
      "M": "So the LORD saved Hezekiah and the inhabitants of Jerusalem from the hand of Sennacherib king of Assyria and from all other enemies, and gave them rest on every side.",
      "T": "Saved and guided: the two verbs of covenant care. The LORD was not merely the agent of one crisis-deliverance; he guided the city on every side — from every direction, against every threat. The rest on every side echoes the summary language of Chronicles for faithful reigns: David gave Solomon rest from enemies (22:9), Solomon built in a time of rest (2 Chr 14:6-7). Rest was not passivity; it was the peace that comes when the covenant protector is actively at work on behalf of the covenant community. Jerusalem, surrounded by the ruins of Sennacherib's ambitions, was at rest."
    },
    "23": {
      "L": "And many brought gifts unto the LORD to Jerusalem, and presents to Hezekiah king of Judah: so that he was magnified in the sight of all nations from thenceforth.",
      "M": "Many brought gifts to the LORD in Jerusalem and valuable presents to Hezekiah king of Judah. From then on he was exalted in the eyes of all nations.",
      "T": "The reversal of empire: nations that had been clients of Sennacherib, or had watched his campaign with the calculation of those who survive by reading power correctly, now brought gifts to Jerusalem. Not tribute exacted by conquest, but gifts voluntarily offered — the recognition that something had happened at Jerusalem that had no precedent in the history of siege warfare. The God of Israel had done what no other god had done, and the nations knew it. Hezekiah's exaltation in the sight of all nations was the international recognition of a covenant theorem operating at full scale: those who trust the LORD will not be put to shame."
    },
    "24": {
      "L": "In those days Hezekiah was sick to the death, and prayed unto the LORD: and he spake unto him, and he gave him a sign.",
      "M": "In those days Hezekiah became mortally ill. He prayed to the LORD, who answered him and gave him a sign.",
      "T": "The illness came hard on the heels of the victory — another test, this time inward and private rather than external and public. The parallel account in 2 Kings 20 and Isaiah 38 gives the detail the Chronicler omits: the fifteen-year extension, the sundial sign, the written prayer. The Chronicler's brevity focuses on what matters for his theological portrait: Hezekiah prayed, the LORD answered, a sign was given. The same pattern as Sennacherib's siege: crisis — prayer — divine response. But the next verse will introduce a complication that the Sennacherib episode did not have: Hezekiah's heart."
    },
    "25": {
      "L": "But Hezekiah rendered not again according to the benefit done unto him; for his heart was lifted up: therefore there was wrath upon him, and upon Judah and Jerusalem.",
      "M": "But Hezekiah did not respond in proportion to the benefit he had received, for his heart was proud. Therefore wrath came upon him and upon Judah and Jerusalem.",
      "T": "The great king's failure: pride. Not the spectacular idolatry of Manasseh, not the military alliance-seeking of Ahaz, but the quiet lifting up of the heart that comes when a man has survived empire, conquered illness, and been honored by all nations. Hezekiah had everything, and 'did not return according to the benefit' — the covenant language of grateful response, of living in proportion to what one has received. The pride that follows extraordinary deliverance is one of the most common spiritual failures in Chronicles. The wrath came on him and on Jerusalem — collective consequence for a king's individual failure, because the community was bound together in the covenant and shared in its effects."
    },
    "26": {
      "L": "Notwithstanding Hezekiah humbled himself for the pride of his heart, both he and the inhabitants of Jerusalem, so that the wrath of the LORD came not upon them in the days of Hezekiah.",
      "M": "But Hezekiah humbled himself for the pride of his heart, he and the inhabitants of Jerusalem, so that the LORD's wrath did not come upon them during Hezekiah's lifetime.",
      "T": "The humbling was rapid and complete, and it was corporate. Hezekiah did not repent alone; he led Jerusalem in repentance — the same communal act of covenant self-correction that had characterized the best moments of his reign. The wrath that had gathered was deflected in his lifetime. The Chronicler adds that qualification deliberately: in the days of Hezekiah. The pride episode would have consequences that extended beyond him — the Babylonian envoys incident, and ultimately the Babylonian captivity that Isaiah announced — but Hezekiah himself would not see those consequences. His humbling bought time for his generation."
    },
    "27": {
      "L": "And Hezekiah had exceeding much riches and honour: and he made himself treasuries for silver, and for gold, and for precious stones, and for spices, and for shields, and for all manner of pleasant jewels;",
      "M": "Hezekiah had great wealth and honor. He built treasuries for silver, gold, precious stones, spices, shields, and all kinds of valuable things.",
      "T": "The wealth of covenant faithfulness, catalogued. The Chronicler delights in these inventory lists because they are the material evidence of divine blessing on faithful kings — just as the stripped Jerusalem and looted temple are the material evidence of covenant judgment on unfaithful ones. Silver, gold, precious stones, spices, shields, costly vessels: the full range of ancient Near Eastern royal wealth. The shields in the treasury echo Solomon's great shields of gold (9:15-16); Hezekiah's reign was being measured against the golden standard of Solomon's."
    },
    "28": {
      "L": "Storehouses also for the increase of corn, and wine, and oil; and stalls for all manner of beasts, and cotes for flocks.",
      "M": "He also built storehouses for the yield of grain, wine, and oil, and stalls for all kinds of livestock, and sheepfolds for his flocks.",
      "T": "Agricultural abundance alongside precious-metal wealth: the covenant's provision extended to every layer of the economy. The storehouses for grain, wine, and oil were the same categories that the people had brought as firstfruits and tithes in chapter 31. The king who had organized the collection of the covenant tithes was now himself the beneficiary of the covenant's material blessing. The stalls for livestock and sheepfolds for flocks: Hezekiah was a wealthy man in the full ancient sense — precious metals, agricultural stores, and herds of living animals."
    },
    "29": {
      "L": "Moreover he provided him cities, and possessions of flocks and herds in abundance: for God gave him substance very much.",
      "M": "He also established cities for himself and acquired flocks and herds in great abundance, for God had given him very great wealth.",
      "T": "The summary attribution is the point: 'for God had given him very great wealth.' Hezekiah's wealth was not the outcome of his own commercial cleverness or military acquisitiveness; it was the covenant blessing on a man who had sought God with all his heart. The principle of 31:21 — seek God fully and prosper — had its material expression in the cities, flocks, herds, and treasuries of chapter 32's closing summary. Wealth in Chronicles is not morally neutral; it is either the sign of covenant faithfulness or the spoil of covenant failure, and in Hezekiah's case it is unambiguously the former."
    },
    "30": {
      "L": "This same Hezekiah also stopped the upper watercourse of Gihon, and brought it straight down to the west side of the city of David. And Hezekiah prospered in all his works.",
      "M": "This same Hezekiah was the one who blocked the upper outlet of the waters of Gihon and channeled them straight down to the west side of the city of David. Hezekiah prospered in all his works.",
      "T": "The Siloam Tunnel — one of the engineering masterpieces of the ancient world. The inscription left by the tunnelers when they broke through, discovered in 1880 CE, describes the moment the two teams working from opposite ends heard each other's pickaxes and broke through the rock that separated them. Hezekiah's engineers cut through approximately 533 meters of solid limestone to bring the Gihon spring water into a pool within the city walls, making Jerusalem siege-proof from a water standpoint. This is the engineering reality behind the military preparation of vv3-4. 'Hezekiah prospered in all his works': the summary statement that closes this extraordinary reign within the chapter. The tunnel that carries his name is still walkable today."
    },
    "31": {
      "L": "Howbeit in the business of the ambassadors of the princes of Babylon, who sent unto him to enquire of the wonder that was done in the land, God left him, to try him, that he might know all that was in his heart.",
      "M": "But when the envoys of Babylon's princes came to inquire about the sign that had occurred in the land, God withdrew from him in order to test him and to know everything that was in his heart.",
      "T": "The Babylonian envoys came ostensibly to ask about the astronomical sign — the shadow going backward on the sundial (Isa 38:8). But the theological note the Chronicler adds is explosive: God withdrew from him to test him. The same verb — azab — that describes Israel forsaking the LORD is here used of the LORD withdrawing from Hezekiah. Not abandoning him permanently, but stepping back, removing the guiding presence, to see what was in the king's heart when left to himself. The test that followed is described in 2 Kings 20 and Isaiah 39: Hezekiah showed the Babylonian envoys everything — all his treasure houses, his armory, everything in his kingdom. Isaiah's verdict was immediate: those men, and their descendants, would carry all of this to Babylon. The man who had trusted God through Sennacherib's siege did not trust God when the Babylonians came asking friendly questions. His heart, when left to itself, turned toward human alliance. God knew it now, and so did history."
    },
    "32": {
      "L": "Now the rest of the acts of Hezekiah, and his goodness, behold, they are written in the vision of Isaiah the prophet, the son of Amoz, and in the book of the kings of Judah and Israel.",
      "M": "The rest of the acts of Hezekiah and his good deeds are recorded in the vision of Isaiah the prophet son of Amoz, and in the Book of the Kings of Judah and Israel.",
      "T": "A double citation: the prophetic record and the royal annals. The Chronicler directs readers to Isaiah's vision — the scroll that now forms Isaiah 36-39 — and to the royal annals. Hezekiah was so significant a king that two different documentary traditions preserved his acts. The word 'goodness' (hesed-related concept here as tovah — his good things, his acts of covenant faithfulness) frames the entire chapter's portrait. Despite the pride episode and the Babylonian test failure, Hezekiah's goodness was the dominant note. He was a good king — better than most, better than what followed him."
    },
    "33": {
      "L": "And Hezekiah slept with his fathers, and they buried him in the chiefest of the sepulchres of the sons of David: and all Judah and the inhabitants of Jerusalem did him honour at his death. And Manasseh his son reigned in his stead.",
      "M": "Hezekiah rested with his fathers, and they buried him in the upper part of the tombs of the sons of David. All Judah and the inhabitants of Jerusalem honored him at his death. And Manasseh his son succeeded him.",
      "T": "He was buried in the finest part of the royal tombs — not just among the kings but in the highest section. The honor done by all Judah and all Jerusalem at his death is the Chronicler's final assessment of his standing: the entire covenant community, from capital to countryside, recognized what it had lost. Hezekiah had been the best king since Jehoshaphat, perhaps since David. He had reformed worship, destroyed idols, funded the temple, organized the priests, defeated an empire, prayed through illness, and humbled himself when pride rose. His son Manasseh's name is placed at the end of the verse, and the shadow it casts is immediate. The next chapter will be the darkest in the history of Judah's monarchy."
    }
  },
  "33": {
    "1": {
      "L": "Manasseh was twelve years old when he began to reign, and he reigned fifty and five years in Jerusalem:",
      "M": "Manasseh was twelve years old when he became king, and he reigned fifty-five years in Jerusalem.",
      "T": "Twelve years old and fifty-five years of reign: the youngest age at which any Judean king began and the longest reign in Judah's entire history. The numbers are chosen by the Chronicler to frame what follows: this was not a brief episode of apostasy but the longest single reign in the monarchy's history, during which the covenant was systematically dismantled by a king who had grown up in the palace of the most faithful man Jerusalem had known. Manasseh had been born to Hezekiah sometime after the Sennacherib crisis and the fifteen-year extension of his father's life. The son of Judah's greatest king became Judah's worst."
    },
    "2": {
      "L": "But did that which was evil in the sight of the LORD, like unto the abominations of the heathen, whom the LORD had cast out before the children of Israel.",
      "M": "He did what was evil in the sight of the LORD, according to the detestable practices of the nations that the LORD had driven out before the Israelites.",
      "T": "The Chronicler's verdict is immediate and total: evil, like the nations. The nations whose practices had made them forfeit their land — whose 'abominations' were the specific reason the LORD had dispossessed them before Israel in the conquest — Manasseh replicated their worship patterns in full. The covenant had been given precisely to mark Israel as different from those nations. Manasseh erased the difference deliberately and comprehensively. He did not merely tolerate surviving pockets of Canaanite religion; he actively reproduced them on a royal scale."
    },
    "3": {
      "L": "For he built again the high places which Hezekiah his father had broken down, and he reared up altars for Baalim, and made groves, and worshipped all the host of heaven, and served them.",
      "M": "He rebuilt the high places that his father Hezekiah had torn down, erected altars to the Baals, made Asherah poles, and worshiped and served all the host of heaven.",
      "T": "A systematic reversal of his father's life work. Every high place Hezekiah had demolished, Manasseh rebuilt. Every altar that had been torn down went back up. The Asherah poles — the wooden cult pillars associated with the Canaanite fertility goddess — were re-erected. And beyond the Canaanite local cults, Manasseh added astral worship: the host of heaven, the sun, moon, and stars venerated across the ancient Near East from Babylon to Canaan. He had apparently absorbed something from his father's encounter with the Babylonian envoys; the Babylonian astrological religion was included in the syncretism. Every false religious system available in the ancient world seems to have found a home in Manasseh's Jerusalem."
    },
    "4": {
      "L": "Also he built altars in the house of the LORD, whereof the LORD had said, In Jerusalem shall my name be for ever.",
      "M": "He also built altars inside the LORD's house — the place of which the LORD had said, 'In Jerusalem my name shall be forever.'",
      "T": "The desecration moved from the hills and high places into the center. The temple — the house that Solomon had built, where the LORD had appeared twice (2 Chr 7:1-3, 12), where the covenant promise of the divine name had been given — now had altars to other gods inside it. The quoted promise ('In Jerusalem my name shall be forever') is the promise that Manasseh's altars were directly violating. He was not ignorant of what the temple meant; he had grown up in the palace next to it. He built the altars inside the house of the covenant God precisely because it was the house of the covenant God. The desecration was intentional."
    },
    "5": {
      "L": "And he built altars for all the host of heaven in the two courts of the house of the LORD.",
      "M": "He built altars to all the host of heaven in both courts of the LORD's house.",
      "T": "Both courts — the inner and outer — filled with altars to the astral deities. The architecture that Solomon had consecrated to the worship of the LORD alone was converted into an open-air pantheon. The two courts were the primary gathering spaces for Israel's worship; now they were claimed for the worship of the heavens. The deliberate totality of the desecration — not one altar in one corner but altars in both courts — suggests that Manasseh was making a programmatic statement: the LORD does not have exclusive claim on his own house. This is the worst moment in the physical history of the temple before its destruction."
    },
    "6": {
      "L": "And he caused his children to pass through the fire in the valley of the son of Hinnom: also he observed times, and used enchantments, and used witchcraft, and dealt with a familiar spirit, and with wizards: he wrought much evil in the sight of the LORD, to provoke him to anger.",
      "M": "He burned his sons as offerings in the Valley of Ben-Hinnom, and practiced omens, divination, and sorcery, and consulted mediums and necromancers. He did much evil in the sight of the LORD, provoking him to anger.",
      "T": "Child sacrifice in the Valley of Ben-Hinnom — the Gehinnom, which became the New Testament's vocabulary for hell. The valley south of Jerusalem had been the site of Ahaz's child sacrifice (28:3); now Manasseh repeated and amplified it. His own sons, burned as offerings to Molech. Then the full catalogue of prohibited occult practices: divination from signs and times, augury, sorcery, consulting the dead through mediums, consulting necromancers. Deuteronomy 18:9-12 lists all of these as the specific reasons the Canaanites had forfeited their land. Manasseh was not experimenting; he was deliberately implementing every form of religious practice the covenant forbade. 'To provoke him to anger' — the Hebrew verb kaas names the specific kind of anger that rises in response to covenant violation, the grief-anger of one whose fidelity has been publicly dishonored."
    },
    "7": {
      "L": "And he set a carved image, the idol which he had made, in the house of God, of which God had said to David, and to Solomon his son, In this house, and in Jerusalem, which I have chosen before all the tribes of Israel, will I put my name for ever:",
      "M": "He set up the carved image he had made in the house of God, of which God had said to David and to Solomon his son, 'In this house and in Jerusalem, which I have chosen from all the tribes of Israel, I will put my name forever.'",
      "T": "The final and most deliberate desecration: the idol in the holy of holies, or at least in the inner precinct where the ark and the divine presence had dwelt. The same house where God had appeared to Solomon in fire (2 Chr 7:1), where the priests could not stand because of the glory-cloud (2 Chr 5:14), where the divine name had been placed as the LORD's permanent residence — Manasseh put a carved image there. The Chronicler quotes the divine promise at length precisely to measure the distance between what God had said and what Manasseh had done. The gap between 'I will put my name here forever' and 'he put an idol here' is the measure of the apostasy."
    },
    "8": {
      "L": "Neither will I any more remove the foot of Israel from out of the land which I have appointed for your fathers; so that they will take heed to do all that I have commanded them, according to the whole law and the statutes and the ordinances by the hand of Moses.",
      "M": "I will no longer remove Israel's foot from the land I appointed for your ancestors, if only they are careful to do all that I have commanded them — all the law, the statutes, and the ordinances given through Moses.",
      "T": "The full conditional promise, quoted in context: permanent land tenure, if they obey. The conditional clause is the point — 'if only they will be careful to do all that I have commanded.' Manasseh's idol in the temple was the exact violation that broke the condition. The land tenure that God had promised was contingent on Torah faithfulness. Manasseh had placed an idol in the temple while the promise of land conditional on Torah obedience was inscribed on the walls. The Chronicler is laying out the theological logic of what will eventually happen to the land: it will be lost because the condition was broken."
    },
    "9": {
      "L": "So Manasseh made Judah and the inhabitants of Jerusalem to err, and to do worse than the heathen, whom the LORD had destroyed before the children of Israel.",
      "M": "Manasseh led Judah and the inhabitants of Jerusalem astray, so that they did more evil than the nations that the LORD had destroyed before the Israelites.",
      "T": "The final verdict on the scope of Manasseh's influence: he did not merely sin personally but led the whole community into sin deeper than the nations. The nations had been driven out for their abominations; Manasseh made Judah worse. The language 'led them astray' carries the sense of active misdirection — not passive bad example but deliberate influence. A king who builds altars in the temple courts and burns his own children in the valley is communicating to his people what religion is. Judah learned. The people became worse than the nations, and worse than they had been under any previous apostate king. The Books of Kings do not soften this verdict; they add that Manasseh's sins were the proximate cause of Jerusalem's eventual destruction (2 Kgs 24:3-4)."
    },
    "10": {
      "L": "And the LORD spake to Manasseh, and to his people: but they would not hearken.",
      "M": "The LORD spoke to Manasseh and his people, but they would not listen.",
      "T": "Grace before judgment — the consistent pattern in Chronicles. Before any major covenant punishment, God speaks first. Prophets are sent, words are given, the warning is clear. 'They would not listen' — the Hebrew shabat: they did not give ear, they did not incline toward the message. The refusal was active, not merely negligent. Manasseh and his people heard the prophetic word and turned away from it. The judgment that followed was therefore not arbitrary; it was the precise outcome that the covenant had always promised for those who hear and refuse."
    },
    "11": {
      "L": "Wherefore the LORD brought upon them the captains of the host of the king of Assyria, which took Manasseh among the thorns, and bound him with fetters, and carried him to Babylon.",
      "M": "Therefore the LORD brought against them the commanders of the Assyrian army, who captured Manasseh, put hooks through him, bound him with bronze chains, and took him to Babylon.",
      "T": "The empire as divine instrument. Assyrian military forces — the same nation that Hezekiah had defeated through prayer — now captured his son. The hooks through his nose or jaw were a standard Assyrian prisoner-transport technique, depicted on Assyrian relief sculptures: a metal hook through the lip or nose, a rope attached, the captive led like an animal. Manasseh, who had worshiped the stars and built altars to Baal in the temple courts, found himself transported to Babylon — the capital of the empire he had been courting, the city of the astral deities he had been worshiping. The judgment matched the sin with bitter irony: Babylon had always been in Manasseh's spiritual imagination; now he would see it in chains."
    },
    "12": {
      "L": "And when he was in affliction, he besought the LORD his God, and humbled himself greatly before the God of his fathers:",
      "M": "In his distress he sought the favor of the LORD his God and humbled himself greatly before the God of his fathers.",
      "T": "The most theologically surprising verse in Chronicles. In a Babylonian prison — hooked, chained, stripped of his throne, separated from every structure of power he had built — Manasseh sought the LORD. Not the Baals, not the host of heaven, not the mediums and necromancers he had patronized for decades. The LORD, his God, the God of his fathers. The 'humbled himself greatly' uses the intensive infinitive absolute: he deeply, genuinely, thoroughly humbled himself. The worst king of Judah, in the worst circumstances of his life, did what the Chronicler has shown is the single decisive act in the covenant: he humbled himself before the God he had spent his reign dishonoring. The covenant theorem that runs through Chronicles applies even here — and the next verse will show it."
    },
    "13": {
      "L": "And prayed unto him: and he was intreated of him, and heard his supplication, and brought him again to Jerusalem into his kingdom. Then Manasseh knew that the LORD he was God.",
      "M": "He prayed to him, and God was moved by his prayer and heard his plea and brought him back to Jerusalem and restored his kingdom. Then Manasseh knew that the LORD is God.",
      "T": "God heard Manasseh. This is the Chronicler's most radical application of the covenant theorem — and perhaps the most important passage in 2 Chronicles. The man who had put an idol in the temple, burned his children in Hinnom, filled both courts with altars to the host of heaven, practiced every form of sorcery the Torah forbade, and led the whole nation into sin deeper than the dispossessed Canaanites — that man prayed in a Babylonian prison, and God was moved by his entreaty. 'Moved by his entreaty' translates a Hebrew verb that means to be opened toward, to be persuaded, to relent toward a petitioner. God was not unmoved by Manasseh's prayer. He brought him back. The worst king returned to Jerusalem and his kingdom. And Manasseh knew — the qal perfect, the knowledge that comes from experienced reality, not theological proposition — that the LORD is God. Not one of the gods. Not the head of a pantheon. God, the only one. The prison had taught him what fifty years of idolatrous reign had not."
    },
    "14": {
      "L": "Now after this he built a wall without the city of David, on the west side of Gihon, in the valley, even to the entering in at the fish gate, and compassed about Ophel, and raised it up a very great height, and put captains of war in all the fenced cities of Judah.",
      "M": "After this he built an outer wall for the city of David, west of Gihon in the valley, extending to the entrance of the Fish Gate and encircling Ophel, raising it to a great height. He also stationed military commanders in all the fortified cities of Judah.",
      "T": "Repentance produced action. Manasseh's first act after his return was to strengthen Jerusalem's defenses — expanding the walls northward to include the Fish Gate area and strengthening the Ophel ridge south of the temple mount. The engineering was practical (the Assyrian threat remained real after his return) but also symbolic: the king who had dismantled his father's spiritual legacy now resumed his father's pattern of building and fortifying. Placing commanders in the fortified cities throughout Judah restored the military infrastructure. A returned man does not just feel differently; he acts differently."
    },
    "15": {
      "L": "And he took away the strange gods, and the idol out of the house of the LORD, and all the altars that he had built in the mount of the house of the LORD, and in Jerusalem, and cast them out of the city.",
      "M": "He removed the foreign gods and the idol from the LORD's house, and all the altars he had built on the temple mount and in Jerusalem, and threw them outside the city.",
      "T": "The reversal of his own reign. The idol he had placed in the temple — removed. The altars in the two courts — torn down. The foreign gods — expelled from the city. Manasseh could not undo fifty-five years of influence on a population, but he could undo the physical symbols of his apostasy, and he did. The act required humility: to tear down what you built is to publicly acknowledge that you built wrong. Manasseh, who had worshiped the stars in the temple courts, now cleared those courts himself. The same hands that had built the altars dismantled them."
    },
    "16": {
      "L": "And he repaired the altar of the LORD, and sacrificed thereon peace offerings and thank offerings, and commanded Judah to serve the LORD God of Israel.",
      "M": "He restored the altar of the LORD and offered on it sacrifices of peace offerings and thank offerings, and commanded Judah to serve the LORD, the God of Israel.",
      "T": "The Chronicler marks the authenticity of Manasseh's repentance by the altar: he repaired what he had desecrated and began to use it rightly. The peace offerings and thank offerings were the sacrifices of restored relationship — you bring a peace offering when the relationship is well, when you are before God in wholeness rather than breach. The thank offering (todah) was specifically for deliverance received: the perfect sacrifice for a man who had been brought out of a Babylonian prison. And he commanded Judah to serve the LORD, the God of Israel. The man who had led the nation into deeper sin than the Canaanites now turned and commanded them back. He had the authority because of his office; whether they would follow was another question (v17 will answer it)."
    },
    "17": {
      "L": "Nevertheless the people did sacrifice still in the high places, yet unto the LORD their God only.",
      "M": "Nevertheless the people still sacrificed at the high places, though only to the LORD their God.",
      "T": "The reform was partial and the habits were deep. The people continued using the high places — the local worship sites that Hezekiah had demolished but Manasseh had rebuilt — but now they used them for the LORD rather than for Baal. The Chronicler notes the distinction: 'only to the LORD their God.' It was not a return to Baal worship, but it was not the centralized, Mosaic-pattern temple worship that Hezekiah had established either. Fifty-five years of normalization had made the high places the default worship infrastructure for ordinary people, and a few years of Manasseh's reformation could not fully undo it. The reform was real but incomplete. The next king would undo even that."
    },
    "18": {
      "L": "Now the rest of the acts of Manasseh, and his prayer to his God, and the words of the seers that spake to him in the name of the LORD God of Israel, behold, they are written in the book of the kings of Israel.",
      "M": "The rest of the acts of Manasseh, his prayer to his God, and the words of the seers who spoke to him in the name of the LORD, the God of Israel — these are recorded in the Book of the Kings of Israel.",
      "T": "A source citation unusual for Chronicles: the prayer is specifically mentioned as a recorded document. The apocryphal 'Prayer of Manasseh' may be a later expansion of this tradition, though it is not the document cited here. The 'words of the seers who spoke to him in the name of the LORD' — prophets sent to Manasseh, whose words are preserved in a source the Chronicler acknowledges but does not quote. The Chronicler is telling us that more happened in Manasseh's fifty-five years than can be told in one chapter — and the prayer is important enough to be named as a separate document."
    },
    "19": {
      "L": "His prayer also, and how God was intreated of him, and all his sins, and his trespass, and the sites in which he built high places, and set up groves and graven images, before he was humbled: behold, they are written among the sayings of the seers.",
      "M": "His prayer, how God received his entreaty, all his sins and unfaithfulness, and the sites where he built high places and erected Asherah poles and carved images before he humbled himself — these are recorded in the Chronicles of the Seers.",
      "T": "A second source, separate from the royal annals: the Chronicles of the Seers, a prophetic record that apparently documented both the prayer and the full extent of the pre-repentance sins. The Chronicler cites it to establish that the record of Manasseh's apostasy — all the sites of the high places, all the Asherah poles, all the carved images — was preserved in full alongside the record of his prayer. The two could not be separated: you cannot understand the grace without knowing the depth of the sin. The 'Chronicles of the Seers' saw everything, recorded everything, and the Chronicler wants his readers to know that nothing was hidden."
    },
    "20": {
      "L": "So Manasseh slept with his fathers, and they buried him in his own house: and Amon his son reigned in his stead.",
      "M": "Manasseh rested with his fathers, and they buried him in his own house. And Amon his son succeeded him.",
      "T": "Buried in his own house — not in the royal tombs of the city of David, not in the special upper section where Hezekiah had been interred with great honor. In his own house: the private burial of a king whose reputation, despite his repentance, could not be fully recovered. The contrast with his father Hezekiah's honored burial (32:33) is the Chronicler's quiet final word on Manasseh's legacy: the worst king of Judah died as a penitent, not as an honored saint. His son Amon inherited the throne — and not, as we will see, the father's late wisdom."
    },
    "21": {
      "L": "Amon was two and twenty years old when he began to reign, and reigned two years in Jerusalem.",
      "M": "Amon was twenty-two years old when he became king, and he reigned two years in Jerusalem.",
      "T": "Two years: the briefest reign in Judah's history. Twenty-two years old — born during Manasseh's apostate years, before the Babylonian captivity and repentance. Amon had grown up watching his father worship Baal and burn children in Hinnom; whatever repentance-period influence his father had tried to exercise, it had not reached the son. The brevity of his reign is itself a judgment: he did not live long enough to do lasting damage, but he did live long enough to demonstrate conclusively that Manasseh's repentance had not produced a covenant household."
    },
    "22": {
      "L": "But he did that which was evil in the sight of the LORD, as did Manasseh his father: for Amon sacrificed unto all the carved images which Manasseh his father had made, and served them;",
      "M": "He did what was evil in the sight of the LORD, as his father Manasseh had done. Amon sacrificed to all the carved images that Manasseh his father had made, and served them.",
      "T": "Amon took the worst of his father and ignored the best. The repentance, the prayer, the restoration, the return, the altar repairs — none of it shaped the son. He found the idols that Manasseh had removed (v15) and brought back — or found others made in their image — and sacrificed to them. He served the carved images that his father had eventually expelled. The Chronicler's point is stark: a father's late repentance does not automatically form a son's whole life. The transmission of covenant faith across generations is not guaranteed by parental conversion. It must be taught, embodied, and received."
    },
    "23": {
      "L": "And humbled not himself before the LORD, as Manasseh his father had humbled himself; but Amon trespassed more and more.",
      "M": "He did not humble himself before the LORD as his father Manasseh had humbled himself, but Amon incurred guilt more and more.",
      "T": "The contrast is the key. Manasseh humbled himself — intensively, genuinely, with the full weight of the verb — and was restored. Amon did not humble himself at all. He went in the opposite direction: multiplied trespass, increased guilt, compounded sin. The verb 'more and more' (hirbah) suggests a trajectory: not a static level of wickedness but an escalating pattern. Manasseh had gone down into captivity and then up into repentance; Amon only went down. The two-year reign was long enough to establish the direction but not long enough to reach the bottom. His own servants ended it for him."
    },
    "24": {
      "L": "And his servants conspired against him, and slew him in his own house.",
      "M": "His servants conspired against him and put him to death in his house.",
      "T": "Killed by his own household staff — not by a foreign army, not by a military coup d'état, but by the people nearest to him. The pattern echoes Joash (24:25): a king who dishonored the covenant ended at the hands of his own servants. Whether the conspiracy was politically motivated (frustration at the incompetent son of a great king) or had a moral dimension (servants who remembered Manasseh's later reform and were appalled by Amon's regression) the Chronicler does not say. The fact is stated plainly: he was killed where he lived, by those who served him. The shortest reign ended the quickest way."
    },
    "25": {
      "L": "But the people of the land slew all them that had conspired against king Amon; and the people of the land made Josiah his son king in his stead.",
      "M": "But the people of the land struck down all who had conspired against King Amon, and the people of the land made Josiah his son king in his place.",
      "T": "The people of the land — the am-ha'aretz, the covenant community in its broadest sense, the landed population of Judah — intervened. They killed the conspirators. Not because Amon had been a good king — he had not — but because the succession must follow the covenant pattern. Legitimate royal succession belonged to the house of David, and the conspirators had disrupted it. The same am-ha'aretz that had crowned Joash after Athaliah's death (23:20-21) now restored order after Amon's assassination. They placed Josiah on the throne — the eight-year-old son who would become the last great reforming king of Judah. The next chapter belongs to him."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '2chronicles')
        merge_tier(existing, CHRONICLES2, tier_key)
        save(tier_dir, '2chronicles', existing)
    print('2 Chronicles 31–33 written.')

if __name__ == '__main__':
    main()
