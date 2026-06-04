"""
MKT 2 Chronicles chapters 34–36 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-2chronicles-34-36.py

Content:
- Ch 34: Josiah's reform in two stages (eighth year: personal seeking; twelfth year: public purge);
         discovery of the Book of the Law in the temple during the repair project; Huldah the
         prophetess delivers the covenant verdict; Josiah's covenant renewal ceremony; Torah read
         publicly to the entire assembly.
- Ch 35: Josiah's Passover — the greatest since Samuel; priestly and Levitical organization;
         the king's provision; the ark returned to its place; death of Josiah at Megiddo after
         refusing the word of God spoken through Neco of Egypt; Jeremiah's lament.
- Ch 36: The rapid collapse: Jehoahaz (3 months), Jehoiakim (11 years), Jehoiachin (3 months
         10 days), Zedekiah (11 years); Babylonian deportations; burning of the temple; the exile
         as the land's Sabbath rest; Cyrus decree — the ending that is a beginning.

Translation decisions (carried forward from mkt-2chronicles-31-33.py):
- H3068 (יהוה): "LORD" in L/M; "the LORD" in T. Consistent throughout OT scripts.
- H430 (אֱלֹהִים): "God" throughout all tiers.
- H7307 (רוּחַ): does not appear prominently; no standalone decision required.
- H2617 (חֶסֶד): not prominent in these chapters.
- H1285 (בְּרִית): "covenant" — appears in ch 34's renewal ceremony.
- "groves" (H842, asherah poles): L: "Asherah poles"; M: "Asherah poles"; T: contextual —
  consistent with 31-33 decisions.

New decisions for chs 34–36:
- 34:14 "book of the law of the LORD given by Moses": L: "book of the law of the LORD given
  through Moses"; M: same; T: interprets as a Torah scroll (likely Deuteronomy or the Pentateuch
  in some form), the foundational covenant document — not merely a legal code but the living
  constitution of Israel's covenant existence. Significance of its being *found* (H4672, matsa)
  documented in T.
- 35:3 "it shall not be a burden upon your shoulders": the ark was being transported — presumably
  moved during the temple repair or purge — and Josiah directed its permanent emplacement.
  L: "it shall not be a burden upon your shoulders"; M: "You no longer need to carry it on your
  shoulders"; T: surfaces the theological significance of the end of the ark's mobile existence.
  This is the last reference to the ark in Chronicles.
- 35:21 "God commanded me to make haste / forbear from meddling with God": Neco's claim that
  God authorized his campaign. The Chronicler's v22 makes explicit that these words were
  "from the mouth of God." L/M reproduce the claim; T surfaces the theological problem — God
  speaking through a pagan king, and Josiah's failure to hear it, which echoes Ahab's fatal
  battle in 2 Chr 18. The "disguised himself" verb (H2664) is the same word used of Ahab at
  Ramoth-Gilead.
- 36:9 "Jehoiachin was eight years old": MT of Chronicles gives 8 years; 2 Kgs 24:8 gives 18.
  Known textual variant — a scribe likely dropped a digit. L/M follow the Chronicler's text (8);
  T notes the variant and the probable co-regency explanation.
- 36:21 "land had enjoyed her sabbaths": the Sabbatical year theology (Lev 26:34-35). The exile
  as the land receiving the rest it had been denied. L: "until the land had enjoyed her sabbaths";
  M: "until the land had made up for its Sabbaths"; T: expounds the Levitical mechanism and the
  Jeremiah 25/29 seventy-year prophecy.
- 36:23 Cyrus decree — end of Chronicles and of the Hebrew canon in MT ordering. T surfaces
  the significance of the book ending with an invitation ("let him go up") rather than with
  destruction, and the connection to Ezra 1:1-3.
- Aspect notes:
  - Ch 34: Josiah's reform uses waw-consecutive imperfects throughout the narrative (completed
    sequential acts). The discovery of the scroll shifts the register — Hilkiah's report is
    perfect tense (I have found). Huldah's oracle uses imperfects and perfects in covenant-curse
    and grace patterns typical of prophetic speech.
  - Ch 35: the Passover organization is described in a series of stative perfects and waw-
    consecutive imperfects — everything was done in orderly sequence. Josiah's death moves to
    rapid narrative imperfects: "they shot," "the king said," "his servants took," "he died."
  - Ch 36: the rapid succession chapters use compressed perfect-tense verdicts for each king.
    The exile description (vv17-20) accumulates with relentless imperfects. The Cyrus pericope
    (vv22-23) shifts to the hiphil perfect "stirred up" — God's sovereign single act — followed
    by Cyrus's proclamation in direct speech.
- OT intertextuality:
  - 34:2 "did not turn aside to the right or the left": the Deuteronomic standard (Deut 17:20)
    applied to kings; last used of Hezekiah (31:20-21); Josiah now embodies it completely.
  - 34:3 "seeking the God of his father David": the Chronicler's covenant theorem language
    (2 Chr 15:2, 26:5); the seeking begins at sixteen, six years before the public reform.
  - 34:4-5 burning bones on altars: fulfills the prophecy of the unnamed man of God at Bethel
    who named Josiah before his birth (1 Kgs 13:2) — a detail the Chronicler does not cite but
    which readers of the full canon would recognize.
  - 34:22 Huldah in the Second Quarter: a female prophet receiving a delegation including the
    high priest — the prophetic gift transcending gender, consistent with Deborah (Judg 4-5).
  - 35:3 the ark: last prominent in 2 Chr 5 (temple dedication); now emplaced permanently as
    the ark's mobile wilderness-journey function is formally superseded.
  - 35:22 "disguised himself": exact verbal echo of 2 Chr 18:29 (Ahab at Ramoth-Gilead). The
    Chronicler's readers were meant to hear the echo and understand the theological parallel.
  - 36:21 Jeremiah's seventy years (Jer 25:11-12; 29:10) interpreted through Lev 26:34-35. The
    exile duration as cosmic Sabbath rest for a land denied its mandated rest.
  - 36:22-23 the Cyrus decree: fulfills Isaiah's prophecy (Isa 44:28; 45:1) naming Cyrus
    before his birth. Chronicles ends where Ezra begins — the books were originally continuous.
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
  "34": {
    "1": {
      "L": "Josiah was eight years old when he began to reign, and he reigned thirty and one years in Jerusalem.",
      "M": "Josiah was eight years old when he became king, and he reigned thirty-one years in Jerusalem.",
      "T": "Eight years old. The youngest king since Joash, who had also been crowned as a child from hiding (2 Chr 22–23). The contrast with his father Amon — assassinated after two years of rapid moral decline — could not be sharper. Josiah would have thirty-one years, and he would use every one of them."
    },
    "2": {
      "L": "And he did that which was right in the sight of the LORD, and walked in the ways of David his father, and declined neither to the right hand, nor to the left.",
      "M": "He did what was right in the sight of the LORD, walking in the ways of his ancestor David and not turning aside to the right or to the left.",
      "T": "The highest praise the Chronicler can give a king: walking in the ways of David without deviation. 'Right hand or left' comes from the Deuteronomic standard for kings (Deut 17:20) and the commission of Joshua (Josh 1:7) — total covenant conformity, not selective faithfulness. The last king to receive this commendation was Hezekiah (31:20–21). Between them lay Manasseh's fifty-five years of apostasy and Amon's two years of intensification. Josiah arrived at eight and proved to be the last hope of the monarchy."
    },
    "3": {
      "L": "For in the eighth year of his reign, while he was yet young, he began to seek after the God of David his father: and in the twelfth year he began to purge Judah and Jerusalem from the high places, and the groves, and the carved images, and the molten images.",
      "M": "For in the eighth year of his reign, while still young, he began to seek the God of his ancestor David. In the twelfth year he began to purge Judah and Jerusalem of the high places, Asherah poles, carved images, and molten images.",
      "T": "The Chronicler gives us a chronology of personal development that Kings does not. At sixteen — the eighth year of his reign — Josiah began to seek the God of David. This was a personal turn, not a political decision. At twenty — the twelfth year — that seeking broke into action: the public purge began. The gap between seeking and acting is the gap between conviction and courage. Josiah had to consolidate enough authority, while still being supervised by the officials who had governed around him since childhood, to begin tearing down the religious infrastructure of Manasseh's fifty-five years. The reform preceded the discovery of the Torah scroll by six years — Josiah did not need to read the law to know that the high places and idols were wrong."
    },
    "4": {
      "L": "And they brake down the altars of Baalim in his presence; and the images, that were on high above them, he cut down; and the groves, and the carved images, and the molten images, he brake in pieces, and made dust of them, and strowed it upon the graves of them that had sacrificed unto them.",
      "M": "They demolished the altars of the Baals in his presence; he cut down the incense altars that were above them; he smashed the Asherah poles, the carved images, and the molten images, ground them to powder, and scattered it over the graves of those who had sacrificed to them.",
      "T": "A deliberate act of ritual contempt. The graves of those who had worshiped at these altars were desecrated with the ground-up remains of the objects they had worshiped — a visual statement that both the worshipers and their gods were dead and dishonored. The comprehensive scope of the demolition covers every form of the false worship: Baal altars, incense stands, Asherah poles, carved images, molten images. Everything Manasseh had built and Amon had perpetuated. The king was present — 'in his presence' — because these were public acts of royal authority, not clandestine removals. Josiah watched the demolition personally."
    },
    "5": {
      "L": "And he burnt the bones of the priests upon their altars, and cleansed Judah and Jerusalem.",
      "M": "He burned the bones of the priests on their own altars and cleansed Judah and Jerusalem.",
      "T": "The ultimate desecration of the false altars: the bones of the pagan priests burned on the very surfaces where they had officiated. This act echoes the three-hundred-year-old prophecy of the unnamed man of God at Bethel who had named Josiah before his birth and predicted this exact act (1 Kgs 13:2) — a prophecy the Chronicler does not cite but which readers of the full canon would recognize. Human bones permanently defiled a site under Mosaic purity law, ensuring that the demolished altars could never be restored to cultic use. Josiah was not merely destroying; he was defiling, making restoration impossible."
    },
    "6": {
      "L": "And so did he in the cities of Manasseh, and Ephraim, and Simeon, even unto Naphtali, with their mattocks round about.",
      "M": "He did the same in the towns of Manasseh, Ephraim, and Simeon, even as far as Naphtali, in their ruins round about.",
      "T": "The reform extended north of Judah's borders into what had been the territory of the former northern kingdom — still under Assyrian provincial administration since 722 BC. Manasseh, Ephraim, Simeon, Naphtali: the whole stretch of the former Israel. Josiah understood himself as king of all Israel, not merely its surviving southern remnant. The 'ruined places' refers to the depopulated and partly resettled towns of the north after the Assyrian conquest. Josiah was cleaning the ruins of a destroyed kingdom."
    },
    "7": {
      "L": "And when he had broken down the altars and the groves, and had beaten the graven images into powder, and cut down all the idols throughout all the land of Israel, he returned to Jerusalem.",
      "M": "After he had torn down the altars and the Asherah poles, ground the carved images to powder, and cut down all the incense altars throughout the land of Israel, he returned to Jerusalem.",
      "T": "The reform complete — or as complete as one person and one campaign could make it across the full extent of the land, north and south. Josiah acted as the covenant king for the entire people of God, not just the surviving southern remnant. His return to Jerusalem marks the end of the first phase of the reform: the external, physical dismantling of the false worship infrastructure. The second phase — the positive reconstruction grounded in the Torah — will be catalyzed by the discovery of a scroll in the temple during a repair project."
    },
    "8": {
      "L": "Now in the eighteenth year of his reign, when he had purged the land, and the house, he sent Shaphan the son of Azaliah, and Maaseiah the governor of the city, and Joah the son of Joahaz the recorder, to repair the house of the LORD his God.",
      "M": "In the eighteenth year of his reign, after he had purged the land and the house, he sent Shaphan son of Azaliah, Maaseiah the governor of the city, and Joah son of Joahaz the recorder to repair the house of the LORD his God.",
      "T": "Six years after the reform began, at age twenty-six, Josiah turned from tearing down to building up. The three officials he dispatched were a carefully chosen team: Shaphan the scribe (administrative authority), Maaseiah the city governor (civil authority), and Joah the recorder (archival and communications authority). The same institutional pattern as Joash's temple repair (2 Chr 24:5–14): royal initiative, collection of funds, dispatch of workers, oversight by named officials. But what would be found in the course of the repair would transform the reform from a purge into a covenant renewal."
    },
    "9": {
      "L": "And when they came to Hilkiah the high priest, they delivered the money that was brought into the house of God, which the Levites that kept the doors had gathered of the hand of Manasseh and Ephraim, and of all the remnant of Israel, and of all Judah and Benjamin, and they returned to Jerusalem.",
      "M": "When they came to Hilkiah the high priest, they delivered the money that had been brought into the house of God — which the Levites who kept the threshold had collected from the people of Manasseh, Ephraim, and all the remnant of Israel, and from all Judah and Benjamin and the inhabitants of Jerusalem.",
      "T": "The collection came from the whole reconstituted people of God: not just Judah and Benjamin but from Manasseh, Ephraim, and 'all the remnant of Israel' — the fragments of the northern kingdom that remained in the land and had participated in Josiah's reform. The money passed through the Levitical gatekeepers — the same accountability structure that had ensured the integrity of Joash's collection (24:8–9). The high priest Hilkiah received it. It was he who, in the course of processing these funds, would make the discovery that changed everything."
    },
    "10": {
      "L": "And they put it in the hand of the workmen that had the oversight of the house of the LORD, and they gave it to the workmen that wrought in the house of the LORD, to repair and amend the house:",
      "M": "They put it in the hands of the workmen assigned to oversee the house of the LORD. These workmen who labored in the LORD's house gave it for repairing and restoring the house.",
      "T": "The money moved through an accountable chain: from the collection point to the high priest to the supervising workmen to the laborers. The same kind of trustworthy administration that Hezekiah had established for the tithe distributions (31:12–19): when holy goods are handled, named people bear named responsibility. The workers went to work — and in the course of the work, something was found."
    },
    "11": {
      "L": "Even to the artificers and builders gave they it, to buy hewn stone, and timber for couplings, and to floor the houses which the kings of Judah had destroyed.",
      "M": "They gave it to the craftsmen and builders to buy quarried stone and timber for joinery and to provide beams for the buildings that the kings of Judah had allowed to fall into ruin.",
      "T": "The practical details of temple repair: quarried stone for walls, timber for roof beams and structural joinery, rebuilding sections that generations of neglectful or hostile kings had damaged. 'The kings of Judah had destroyed' is a damning phrase. The temple had suffered from active misuse as much as from neglect. Ahaz had stripped the temple and closed its doors (28:24); Manasseh had filled its courts with altars to foreign gods. The physical structure bore the marks of the monarchy's spiritual history."
    },
    "12": {
      "L": "And the men did the work faithfully: and the overseers of them were Jahath and Obadiah, the Levites, of the sons of Merari; and Zechariah and Meshullam, of the sons of the Kohathites, to set it forward; and other of the Levites, all that could skill of instruments of musick.",
      "M": "The men performed the work faithfully. Their supervisors were Jahath and Obadiah the Levites from the sons of Merari, and Zechariah and Meshullam from the sons of the Kohathites — appointed to oversee. And Levites who were skilled in musical instruments",
      "T": "The word 'faithfully' (emunah) echoes its use in chapter 31 for the tithes administration — the covenant quality of reliable, trustworthy action. The four named supervisors represent the two major non-priestly Levitical clans: the sons of Merari (who had carried the tabernacle's structural elements) and the Kohathites (who had carried the ark and the holy furniture). The oversight committee carried institutional memory in its very lineage. The Levites skilled in musical instruments served in a broader administrative capacity — their literacy and organizational training made them useful for project management as well as liturgical service."
    },
    "13": {
      "L": "Also they were over the bearers of burdens, and were overseers of all that wrought the work in any manner of service: and of the Levites there were scribes, and officers, and porters.",
      "M": "They also directed the burden-bearers and supervised all who did work in every kind of service. And some of the Levites were scribes, officers, and gatekeepers.",
      "T": "A division of Levitical labor that mirrors the organizational complexity of a major construction project: scribes for record-keeping, officers for logistics coordination, gatekeepers for access control. The repair was not merely physical but administrative — requiring documentation, scheduling, and security. The same body of people who led Israel in worship could, when needed, manage a national construction project. The temple workers were servants of the word; they were also institutional professionals."
    },
    "14": {
      "L": "And when they brought out the money that was brought into the house of the LORD, Hilkiah the priest found a book of the law of the LORD given by Moses.",
      "M": "While they were bringing out the money that had been brought into the house of the LORD, Hilkiah the priest found the book of the law of the LORD given through Moses.",
      "T": "The pivot on which the entire chapter turns. In the course of the repair — moving money, shifting storage — Hilkiah the high priest found a scroll. The Chronicler calls it 'the book of the law of the LORD given through Moses,' making explicit what 2 Kings 22:8 leaves simply as 'the book of the law.' Whatever exactly the scroll contained — Deuteronomy in some form, or a more complete Torah — its authority was unambiguous: it came through Moses, meaning it was the foundational covenant document of Israel's existence as a people. That it had been lost — or buried, or deliberately hidden from Manasseh's purges — and found now, in the eighteenth year of Josiah's reign, during a temple repair project, is one of the most theologically charged moments in the history of Israel."
    },
    "15": {
      "L": "And Hilkiah answered and said to Shaphan the scribe, I have found the book of the law in the house of the LORD. And Hilkiah delivered the book to Shaphan.",
      "M": "Hilkiah said to Shaphan the secretary, 'I have found the book of the law in the house of the LORD.' And Hilkiah gave the book to Shaphan.",
      "T": "The transmission is simple: priest to scribe. The scroll passed from the man who found it to the man who could read it to the king. Hilkiah's words — 'I have found' — are the most consequential words spoken in any temple renovation project in history. What he had found was not a treasure in the ordinary sense but the covenant document on which Josiah's entire reform had been implicitly operating without full knowledge of its demands. The scroll would be read aloud to the king, and everything would change."
    },
    "16": {
      "L": "And Shaphan carried the book to the king, and brought the king word back again, saying, All that was committed to thy servants, they do it.",
      "M": "Shaphan brought the book to the king and further reported, saying, 'Everything committed to your servants they are doing.'",
      "T": "Shaphan was a diligent official. Before reporting the extraordinary find, he gave the king the administrative update first — all the repair work proceeds on schedule, the money is being managed properly, the workmen are faithful. The order of reporting tells us something about Shaphan's character: methodical, accountable, professional even while carrying something world-changing under his arm. The repair project was on track. And by the way, there is a scroll."
    },
    "17": {
      "L": "And they have gathered together the money that was found in the house of the LORD, and have delivered it into the hand of the overseers, and to the hand of the workmen.",
      "M": "They have collected all the money found in the LORD's house and delivered it into the hands of the overseers and the workmen.",
      "T": "The accounting closes cleanly. Every shekel collected has been accounted for and delivered to its designated purpose. Shaphan was telling the king: the institution is functioning; the reform is running correctly; the house is being repaired. The scroll he was about to report was not a critique of the administration; it was going to reveal something far larger than an administrative matter."
    },
    "18": {
      "L": "Then Shaphan the scribe told the king, saying, Hilkiah the priest hath given me a book. And Shaphan read it before the king.",
      "M": "Then Shaphan the secretary told the king, 'Hilkiah the priest has given me a book.' And Shaphan read it aloud before the king.",
      "T": "The reading aloud was the decisive act. The words of the Torah, unheard in Manasseh's long reign and Amon's brief one, spoken publicly before a king who had been reforming his kingdom for six years without their full authority. Shaphan read; Josiah heard. What the king heard in that reading would not be a theological affirmation of what he had been doing — it would be a devastating confrontation with what had not been done, what could not now be undone, and what was coming."
    },
    "19": {
      "L": "And it came to pass, when the king had heard the words of the law, that he rent his clothes.",
      "M": "When the king heard the words of the law, he tore his clothes.",
      "T": "The tearing of clothes — the most intense physical expression of grief and horror in the ancient Near East, the gesture reserved for death, catastrophe, and uncontainable sorrow. Josiah heard the Torah read and understood immediately: the covenant curses of Deuteronomy 27–28 were exactly what his nation had been accumulating for generations. The reform he had been conducting was necessary but insufficient; the distance between where the law required Israel to be and where Israel actually was, measured across Manasseh's fifty-five years, was too great to close by demolishing altars. He tore his clothes because he understood that the reading was also a verdict. The text was not only old instruction; it was active covenant accusation."
    },
    "20": {
      "L": "And the king commanded Hilkiah, and Ahikam the son of Shaphan, and Abdon the son of Micah, and Shaphan the scribe, and Asaiah a servant of the king's, saying,",
      "M": "The king commanded Hilkiah, Ahikam son of Shaphan, Abdon son of Micah, Shaphan the secretary, and Asaiah the king's servant,",
      "T": "A committee of five, representing the religious, administrative, and royal household leadership: Hilkiah the high priest; Ahikam son of Shaphan (his father the scribe was standing in the room); Abdon son of Micah; Shaphan the scribe personally; and Asaiah a royal servant. Five witnesses to the commission; five who would carry the king's urgent question to the prophet. Josiah sent everyone who mattered, because what he had just heard from the scroll was not a routine policy question."
    },
    "21": {
      "L": "Go, enquire of the LORD for me, and for them that are left in Israel and in Judah, concerning the words of the book that is found: for great is the wrath of the LORD that is poured out upon us, because our fathers have not kept the word of the LORD, to do after all that is written in this book.",
      "M": "Go, inquire of the LORD for me and for all who remain in Israel and Judah concerning the words of the book that has been found. For the wrath of the LORD is poured out greatly on us, because our fathers did not keep the word of the LORD to do all that is written in this book.",
      "T": "The prayer request is comprehensive: for me, and for all the remnant in Israel and Judah. Not just Josiah's court; not just Judah; the remnant of the entire people of God, north and south. The urgency in his words is theological: the wrath is not a future threat but a present reality — 'is poured out' uses the perfect tense: it has already been activated. The disasters of Manasseh's time and the Assyrian conquest of the north were the covenant curses operating. The Torah scroll had just made the mechanism explicit. Josiah's response was not academic; it was existential."
    },
    "22": {
      "L": "And Hilkiah, and they that the king had appointed, went to Huldah the prophetess, the wife of Shallum the son of Tokhath, the son of Hasrah, keeper of the wardrobe; (now she dwelt in Jerusalem in the college;) and they spake to her to that effect.",
      "M": "So Hilkiah and those the king appointed went to Huldah the prophetess, wife of Shallum son of Tokhath, son of Hasrah, who kept the wardrobe. She was living in Jerusalem in the Second Quarter, and they spoke to her about this.",
      "T": "They went to Huldah. Not to Jeremiah — who was in the early years of his ministry — not to Zephaniah his contemporary. They went to Huldah, a woman who lived in the Second Quarter of Jerusalem, a newer residential district likely north of the old city, whose husband kept the royal wardrobe. She had prophetic authority recognized by the high priest himself. The delegation of five men, including Hilkiah, going to a woman for the authoritative word of the LORD was unremarkable to the Chronicler — the prophetic gift was the determining credential. What Huldah said would stand as the authoritative interpretation of the Torah scroll's implications for Josiah's generation."
    },
    "23": {
      "L": "And she answered them, Thus saith the LORD God of Israel, Tell ye the man that sent you to me,",
      "M": "She said to them, 'Thus says the LORD, the God of Israel: Tell the man who sent you to me,'",
      "T": "The prophetic formula — 'Thus says the LORD, the God of Israel' — is the claim that what follows is not the prophet's own analysis but the authoritative word of the covenant God. Huldah received the delegation with the full weight of her prophetic office. The message would come in two parts: a word of covenant judgment on Jerusalem, and a word of personal grace to Josiah. Both would be delivered with equal authority."
    },
    "24": {
      "L": "Thus saith the LORD, Behold, I will bring evil upon this place, and upon the inhabitants thereof, even all the curses that are written in the book which they have read before the king of Judah:",
      "M": "Thus says the LORD: Behold, I will bring disaster upon this place and upon its inhabitants — all the curses written in the book that was read before the king of Judah.",
      "T": "The word of judgment is direct and without qualification on one level: disaster is coming. The 'curses written in the book' refers to the covenant curses of Deuteronomy 28–30 and Leviticus 26 — the comprehensive catalogue of consequences promised for covenant violation: famine, disease, military defeat, exile. Josiah's reforms, genuine as they were, could not retroactively cancel the accumulated covenant deficit of Manasseh's reign. The word through Huldah confirmed what Josiah had feared when he tore his clothes: the covenant mechanism was operating, and judgment was already determined."
    },
    "25": {
      "L": "Because they have forsaken me, and have burned incense unto other gods, that they might provoke me to anger with all the works of their hands; therefore my wrath shall be poured out upon this place, and shall not be quenched.",
      "M": "Because they have abandoned me and made offerings to other gods, provoking me to anger with all the works of their hands — therefore my wrath will be poured out on this place and will not be quenched.",
      "T": "The reason stated in covenantal precision: abandonment of the LORD, worship of other gods, provocation. The three-stage structure matches the prophetic indictments running from Hosea through Jeremiah. 'Will not be quenched' — the language of fire that cannot be put out, divine judgment set in motion that will run its course. This is the sober center of Huldah's oracle: even Josiah's exceptional faithfulness cannot stop what Manasseh's exceptional wickedness set in motion. The reform is real and important; it cannot save the city."
    },
    "26": {
      "L": "And as for the king of Judah, who sent you to enquire of the LORD, so shall ye say unto him, Thus saith the LORD God of Israel concerning the words which thou hast heard;",
      "M": "But to the king of Judah who sent you to inquire of the LORD, say this to him: Thus says the LORD, the God of Israel, concerning the words you have heard —",
      "T": "The pivot from the word of judgment to the word of personal grace. 'But to the king of Judah' — a distinction is made. The disaster is coming on the place and the people; but the man who sent the delegation receives a different word. The covenant theorem that runs through Chronicles as its central organizing principle now operates in Josiah's favor: the king who sought the LORD, even with a broken heart and a torn garment, is heard."
    },
    "27": {
      "L": "Because thine heart was tender, and thou didst humble thyself before God, when thou heardest his words against this place, and against the inhabitants thereof, and humbledst thyself before me, and didst rend thy clothes, and weep before me; I have even heard thee also, saith the LORD.",
      "M": "Because your heart was tender and you humbled yourself before God when you heard his words against this place and its inhabitants, and you have humbled yourself before me and torn your clothes and wept before me, I have also heard you, declares the LORD.",
      "T": "Three acts named as the basis for the personal grace: a tender heart, humility before God, and the physical acts of mourning — torn clothes and weeping. These were not performative gestures; the king had been among his own court when the reading was done. The response was genuine. The covenant theorem states that God is found by those who seek him and hears those who humble themselves before him. Josiah's response to the Torah reading was an act of the heart — and the LORD who searches hearts saw it and responded to it. 'I have heard you' is the same language used of every answered prayer in Chronicles."
    },
    "28": {
      "L": "Behold, I will gather thee to thy fathers, and thou shalt be gathered to thy grave in peace, neither shall thine eyes see all the evil that I will bring upon this place, and upon the inhabitants of the same. So they brought the king word again.",
      "M": "Behold, I will gather you to your fathers, and you will be gathered to your grave in peace. Your eyes will not see all the disaster I am about to bring upon this place and its inhabitants.' So they brought back word to the king.",
      "T": "The grace given to Josiah is the grace of timing: he will die before the catastrophe falls. 'Gathered to your grave in peace' — which Josiah, who died of wounds at Megiddo (35:24), will fulfill in a different way than we might expect. The word 'peace' (shalom) here means covenant wholeness, not the absence of violent death. He will not see Jerusalem burning; he will not watch the temple destroyed; he will not live through the exile the law had announced. The grace was a merciful ending before a terrible history. The delegation brought this word to the king — and Josiah would act on it immediately and completely."
    },
    "29": {
      "L": "Then the king sent and gathered together all the elders of Judah and Jerusalem.",
      "M": "Then the king summoned all the elders of Judah and Jerusalem.",
      "T": "The covenant response to the covenant word: assembly. The elders were the representative heads of the community, the men through whom covenant commitments were made communally effective. Josiah did not keep Huldah's word private or act on it in isolation. The covenant was communal — made with the nation as a whole — and its renewal would have to be communal too."
    },
    "30": {
      "L": "And the king went up into the house of the LORD, and all the men of Judah, and the inhabitants of Jerusalem, and the priests, and the Levites, and all the people, great and small: and he read in their ears all the words of the book of the covenant that was found in the house of the LORD.",
      "M": "The king went up to the house of the LORD with all the men of Judah, the inhabitants of Jerusalem, the priests, the Levites, and all the people, both great and small. He read aloud to them all the words of the Book of the Covenant that had been found in the house of the LORD.",
      "T": "The covenant assembly: king, men of Judah, inhabitants of Jerusalem, priests, Levites, all the people — great and small, meaning without distinction of status, everyone included. The reading was public and total. The 'Book of the Covenant' is the scroll's formal designation, the same title used for the Sinai document (Exod 24:7). The public reading of the Torah to the assembled community was the act Moses had commanded be performed every seven years at the Feast of Booths (Deut 31:10–13). It had apparently not been done in living memory. The people heard the law, perhaps for the first time in their lives."
    },
    "31": {
      "L": "And the king stood in his place, and made a covenant before the LORD, to walk after the LORD, and to keep his commandments, and his testimonies, and his statutes, with all his heart, and with all his soul, to perform the words of the covenant which are written in this book.",
      "M": "The king stood in his place and made a covenant before the LORD, to follow the LORD and keep his commandments, testimonies, and statutes with all his heart and all his soul, and to perform the words of the covenant written in this book.",
      "T": "The king stood in his place — the royal position before the altar — and made a public covenant. The formula is the full Deuteronomic statement of covenant commitment: with all his heart, with all his soul, the total self-investment of the person in the covenant. 'Commandments, testimonies, statutes' — the three categories of Torah regulation covering every domain of life, ceremony, ethics, and social order. The covenant Josiah made was not a general pledge of religious sincerity; it was a specific commitment to the specific text of a specific scroll he had just heard read. He bound himself to it in the presence of the entire assembly. The same act that Asa had performed (2 Chr 15:12) and Jehoiada had facilitated for Joash (23:16) was performed again by Josiah with greater deliberateness and wider scope than any predecessor."
    },
    "32": {
      "L": "And he caused all that were present in Jerusalem and Benjamin to stand to it. And the inhabitants of Jerusalem did according to the covenant of God, the God of their fathers.",
      "M": "He required all who were present in Jerusalem and Benjamin to stand to it. And the inhabitants of Jerusalem acted in accordance with the covenant of God, the God of their fathers.",
      "T": "The covenant was not left as the king's private commitment; it became the community's. 'Stand to it' — in Hebrew covenant ceremonies, the act of physically presenting oneself as a party to the agreement. Every person present was required to stand before God as a covenant member. And they did — the Chronicler records that the inhabitants of Jerusalem acted according to the covenant. The communal dimension of the covenant renewal was its greatest strength and also its greatest vulnerability: when it broke down again, it would break down from within the community."
    },
    "33": {
      "L": "And Josiah took away all the abominations out of all the countries that pertained to the children of Israel, and made all that were present in Israel to serve, even to serve the LORD their God. And all his days they departed not from following the LORD, the God of their fathers.",
      "M": "Josiah removed all the abominations from all the territories belonging to the people of Israel and required all who were present in Israel to serve the LORD their God. Throughout all his days they did not turn away from following the LORD, the God of their fathers.",
      "T": "A summary of extraordinary scope and a verdict of remarkable consistency: throughout all his days — all thirty-one years — not one departure from following the LORD. In a book that has recorded the theological careers of twenty kings, most of whom were faithful for some years and faithless for others, to receive the verdict 'did not turn away throughout all his days' is the highest possible praise. Josiah was the last great king, and he was great without qualification. The next chapter will show what happened when that life ended at Megiddo and the final four kings led the kingdom in rapid succession toward fire."
    }
  },
  "35": {
    "1": {
      "L": "Moreover Josiah kept a passover unto the LORD in Jerusalem: and they killed the passover on the fourteenth day of the first month.",
      "M": "Josiah kept a Passover to the LORD in Jerusalem, and they slaughtered the Passover lamb on the fourteenth day of the first month.",
      "T": "The Passover was not an afterthought to the covenant renewal but its sacramental center. The annual memorial of the exodus — Israel's foundational liberation — was reactivated by Josiah as the covenant people recommitted to the covenant God. The fourteenth day of the first month was the exact date prescribed by Moses (Exod 12:6); the precision honored both the command and the memory. Josiah's Passover, as v18 will declare, had no precedent since the days of Samuel — not even Hezekiah's, which had been kept a month late on an emergency dispensation (2 Chr 30:2–3). This one was by the book, in every detail."
    },
    "2": {
      "L": "And he set the priests in their charges, and encouraged them to the service of the house of the LORD.",
      "M": "He stationed the priests in their divisions and encouraged them in the service of the house of the LORD.",
      "T": "Before the Passover was slaughtered, the organizational structure was established. Hezekiah had done the same (31:2); the Chronicler shows a consistent pattern: covenant celebration requires structural preparation, not just spiritual zeal. The encouragement Josiah gave the priests was not ceremonial flattery but real leadership — speaking to people who would manage thousands of animals in a single day and strengthening their resolve to do it precisely. The priests needed to know that the king was behind them and that the work mattered."
    },
    "3": {
      "L": "And said unto the Levites that taught all Israel, which were holy unto the LORD, Put the holy ark into the house which Solomon the son of David king of Israel did build; it shall not be a burden upon your shoulders: serve now the LORD your God, and his people Israel.",
      "M": "He said to the Levites who taught all Israel and were consecrated to the LORD, 'Put the holy ark in the house that Solomon son of David king of Israel built. You no longer need to carry it on your shoulders. Now serve the LORD your God and his people Israel.'",
      "T": "A remarkable instruction that marks a theological boundary in Israel's history: the ark was in transit — apparently moved during the temple repair or the purge of the courts — and Josiah directed its permanent emplacement. 'It shall not be a burden on your shoulders': the portable-sanctuary role that the Levites had carried since Moses, transporting the ark through the wilderness and the land, was formally superseded. The ark belonged in Solomon's house, and now that the house was repaired and cleansed, it should stay there. This is the last reference to the ark in Chronicles. With its final emplacement, the wilderness journey was over."
    },
    "4": {
      "L": "And prepare yourselves by the houses of your fathers, after your courses, according to the writing of David king of Israel, and according to the writing of Solomon his son.",
      "M": "Prepare yourselves according to your ancestral families and divisions, as prescribed in the writing of David king of Israel and the document of Solomon his son.",
      "T": "The Davidic organization — the twenty-four priestly courses and the Levitical assignments (1 Chr 23–26) — was the constitution of the temple's liturgical life. Josiah directed the Passover to be organized according to that inherited structure, supplemented by Solomon's additional specifications. Both the father who designed the system and the son who built the house had left written instructions, and those instructions were to be followed precisely. Josiah's Passover was self-consciously modeled on the full Mosaic-Davidic-Solomonic pattern of covenant worship."
    },
    "5": {
      "L": "And stand in the holy place according to the divisions of the families of the fathers of your brethren the people, and after the division of the families of the Levites.",
      "M": "Stand in the Holy Place according to the groupings of the ancestral families of your brothers the lay people, and according to the Levitical divisions of families.",
      "T": "The spatial organization of the Passover: Levites positioned according to both the lay family groupings they were serving and their own Levitical clan assignments. The coordination ensured that every family was covered — not only those who could push to the front, but the whole community served systematically. The holy place here refers not to the most holy place (the holy of holies) but to the general sanctuary courts where the Levites served."
    },
    "6": {
      "L": "So kill the passover, and sanctify yourselves, and prepare your brethren, that they may do according to the word of the LORD by the hand of Moses.",
      "M": "Slaughter the Passover offerings, consecrate yourselves, and prepare your brothers so that they may act according to the word of the LORD given through Moses.",
      "T": "The three-part charge: slaughter, consecrate, prepare the brothers. The order is significant — ritual action, personal holiness, then service to the community. The authority behind the instruction was not Josiah's royal will but 'the word of the LORD given through Moses' — the Torah that had just been found and read. The Passover was being kept because Moses had commanded it and the LORD had instituted it. Josiah was executing an ancient divine order, not inventing a new one."
    },
    "7": {
      "L": "And Josiah gave to the people, of the flock, lambs and kids, all for the passover offerings, for all that were present, to the number of thirty thousand, and three thousand bullocks: these were of the king's substance.",
      "M": "Josiah contributed to the lay people from the flock 30,000 lambs and young goats for Passover offerings, along with 3,000 bulls — all from the king's own possessions.",
      "T": "The royal provision: 30,000 small animals and 3,000 bulls from Josiah's personal wealth. The same pattern as Hezekiah's contribution to his own Passover (30:24) and to the daily burnt offerings (31:3): a king who funds the public worship from his own resources places his personal wealth at the service of the covenant community. The numbers are enormous — far exceeding what individuals could provide — and they speak to both Josiah's wealth and his generosity. Every family present would receive from the king's abundance."
    },
    "8": {
      "L": "And his princes gave willingly unto the people, to the priests, and to the Levites: Hilkiah and Zechariah and Jehiel, rulers of the house of God, gave unto the priests for the passover offerings two thousand and six hundred small cattle, and three hundred oxen.",
      "M": "His officials contributed willingly to the people, the priests, and the Levites. Hilkiah, Zechariah, and Jehiel, the chief officers of the house of God, gave the priests 2,600 small cattle and 300 bulls for the Passover offerings.",
      "T": "The officials followed the king's example. 'Willingly' — the same voluntary generosity that marked the great moments of covenant celebration in Chronicles: the tabernacle offerings (Exod 35–36), David's preparation for the temple (1 Chr 29:9), the tithes under Hezekiah (31:5). Hilkiah, Zechariah, and Jehiel — the three senior temple officers — contributed from the temple's institutional resources or their personal wealth. Their gift went specifically to the priests: 2,600 small animals and 300 bulls. The institutional leaders of the temple community funded the Passover workers."
    },
    "9": {
      "L": "Conaniah also, and Shemaiah and Nethaneel, his brethren, and Hashabiah and Jeiel and Jozabad, chief of the Levites, gave unto the Levites for passover offerings five thousand small cattle, and five hundred oxen.",
      "M": "Conaniah also, and Shemaiah and Nethanel his brothers, and Hashabiah and Jeiel and Jozabad, leaders of the Levites, gave 5,000 small animals and 500 bulls for Passover offerings to the Levites.",
      "T": "Six Levitical leaders contributed the portion for the Levites themselves — 5,000 animals and 500 bulls. The Levites' share was larger than the priests' because they were the larger body of workers, managing the slaughter and distribution for the whole assembly. Conaniah had appeared in a similar administrative role in Hezekiah's tithe distribution (31:12–13). The tradition of Levitical institutional generosity was being maintained across the decades. The entire professional religious leadership of Judah was pooling its resources for the community's Passover."
    },
    "10": {
      "L": "So the service was prepared, and the priests stood in their place, and the Levites in their courses, according to the king's commandment.",
      "M": "When the service had been prepared, the priests stood in their positions and the Levites in their divisions according to the king's command.",
      "T": "Everything in order before the slaughter began. Priests at their stations, Levites in their designated positions, the whole coordinated system of covenant worship activated by royal command. The phrase 'according to the king's command' in Chronicles marks moments when the Davidic order is being fully realized — where the king's authority aligns with the divine order rather than replacing it. Josiah's command was the implementation of Mosaic instruction mediated through Davidic institutional form."
    },
    "11": {
      "L": "And they killed the passover, and the priests sprinkled the blood from their hands, and the Levites flayed them.",
      "M": "They slaughtered the Passover lambs, and the priests sprinkled the blood received from the Levites, while the Levites did the skinning.",
      "T": "The choreography of the slaughter: the Levites killed (since the volume — 30,000-plus animals — exceeded what the priests alone could handle), handed the blood to the priests for sprinkling on the altar, and then processed the carcasses. The division of labor was not improvised but reflected the organizational structure Josiah had laid out. Hundreds of Levites working simultaneously, each with an assigned task, in the largest coordinated liturgical event the second temple period had yet seen."
    },
    "12": {
      "L": "And they removed the burnt offerings, that they might give according to the divisions of the families of the people, to offer unto the LORD, as it is written in the book of Moses. And so did they with the oxen.",
      "M": "They set aside the burnt offerings to distribute them to the family groupings of the lay people, to offer to the LORD as written in the Book of Moses. And they did the same with the bulls.",
      "T": "The Passover and the burnt offerings were separate categories requiring separate handling. The burnt offerings were distributed by family grouping so that every household had its offering presented. The reference to 'as it is written in the Book of Moses' points directly back to the Torah scroll just found and read: this Passover was being conducted with unprecedented Torah fidelity. The scroll had been found; it had been read; now it was being obeyed, literally, in detail, on the fourteenth day of the first month."
    },
    "13": {
      "L": "And they roasted the passover with fire according to the ordinance: but the other holy offerings sod they in pots, and in caldrons, and in pans, and divided them speedily among all the people.",
      "M": "They roasted the Passover lambs over the fire as prescribed, while the other holy offerings were boiled in pots, cauldrons, and pans, and distributed quickly among all the lay people.",
      "T": "Fire-roasting for the Passover — Exodus 12:8–9 explicitly requires fire-roasting and prohibits boiling; the Levites followed the letter of the law. The other sacrificial meat — the fellowship offerings and additional sacrifices — was boiled in the standard method. The careful distinction between cooking methods reflects the Torah's precision: the Passover is unique in its preparation because it memorializes a unique night. The quick distribution ensured that the entire assembly received their portion before the offering became unclean — a logistical feat for an event serving tens of thousands."
    },
    "14": {
      "L": "And afterward they made ready for themselves, and for the priests: because the priests the sons of Aaron were busied in offering of burnt offerings and the fat until night; therefore the Levites prepared for themselves, and for the priests the sons of Aaron.",
      "M": "Afterward they prepared for themselves and for the priests, because the priests, the sons of Aaron, were occupied offering the burnt offerings and fat portions until nightfall. So the Levites prepared portions for themselves and for the priests the sons of Aaron.",
      "T": "Service before self. The Levites served the entire lay assembly first — distributing the Passover meat to tens of thousands — and only then prepared their own portions and those of the occupied priests. The priests were still at the altar, managing the burnt offerings and fat portions that had to be consumed by fire, working until nightfall. The Levites' care for the priests was the covenant institution functioning as designed: the sons of Levi sustaining the sons of Aaron through a day of uninterrupted work. Each body covered for the other's need."
    },
    "15": {
      "L": "And the singers the sons of Asaph were in their place, according to the commandment of David, and Asaph, and Heman, and Jeduthun the king's seer: and the porters waited at every gate; they might not depart from their service; for their brethren the Levites prepared for them.",
      "M": "The singers, the sons of Asaph, were in their assigned places according to the command of David, Asaph, Heman, and Jeduthun the king's seer. The gatekeepers were at each gate; they did not need to leave their posts, for their brothers the Levites prepared for them.",
      "T": "Every part of the temple's institutional life was functioning simultaneously and in coordination. The singers maintained the liturgical worship throughout the day — the psalms being sung, the musical accompaniment continuing without interruption. The gatekeepers held their posts, maintaining the security and order of the sacred space. Neither singers nor gatekeepers had to abandon their assigned work to find food; the Levitical workers covered them. The covenant institution operating at full designed capacity: every role filled, every person supported, the whole greater than the sum of its parts."
    },
    "16": {
      "L": "So all the service of the LORD was prepared the same day, to keep the passover, and to offer burnt offerings upon the altar of the LORD, according to the commandment of king Josiah.",
      "M": "So all the service of the LORD was prepared that day for keeping the Passover and offering burnt offerings on the altar of the LORD, according to the command of King Josiah.",
      "T": "The summary of the day: all the service prepared, all the worship completed, Passover and burnt offerings both offered, according to Josiah's command. That command in turn derived from Moses, David, and the newly found Torah scroll. The chain of authority: Torah — David's institutional order — Josiah's royal command — the priests and Levites in their places. Every link held. The day was theologically complete."
    },
    "17": {
      "L": "And the children of Israel that were present kept the passover at that time, and the feast of unleavened bread seven days.",
      "M": "The Israelites who were present kept the Passover at that time, and the Feast of Unleavened Bread for seven days.",
      "T": "Both parts of the Passover complex: the Passover meal itself on the fourteenth day, and the seven-day Feast of Unleavened Bread that followed (Exod 12:15–20). Together they formed the full commemoration of the exodus. The eight days were not Josiah's innovation; they were the Mosaic calendar followed precisely. 'The children of Israel who were present' — the phrase used throughout Chronicles to describe the covenant community at its great moments, inclusive of all who are there regardless of tribal origin."
    },
    "18": {
      "L": "And there was no passover like to that kept in Israel from the days of Samuel the prophet; neither did all the kings of Israel keep such a passover as Josiah kept, and the priests, and the Levites, and all Judah and Israel that were present, and the inhabitants of Jerusalem.",
      "M": "No Passover like this had been kept in Israel since the days of Samuel the prophet. None of the kings of Israel had kept such a Passover as Josiah kept, with the priests and Levites, all Judah and Israel who were present, and the inhabitants of Jerusalem.",
      "T": "The superlative verdict: unprecedented since Samuel, the last judge and first prophet, who bridged the pre-monarchic and monarchic periods. This surpassed even Hezekiah's praised Passover (30:26). Why? Because it combined the full Mosaic prescription (the correct date, the fire-roasting, the full week), the Davidic institutional organization (the divisions, the musical worship, the coordination), and the covenantal impetus of the newly found Torah scroll. It was the Passover as it was meant to be, and it had not been done this way in four centuries."
    },
    "19": {
      "L": "In the eighteenth year of the reign of Josiah was this passover kept.",
      "M": "This Passover was kept in the eighteenth year of Josiah's reign.",
      "T": "A timestamp on the theological high point: the eighteenth year, age twenty-six. The same year as the finding of the Torah scroll, Huldah's oracle, and the covenant renewal ceremony. The Passover capped the reform's most decisive year. The year that began with the Torah's discovery ended with the greatest Passover in four centuries. Josiah had heard the law, renewed the covenant, and kept the Passover. The chapter's next word is 'After all this' — and the empire would come."
    },
    "20": {
      "L": "After all this, when Josiah had prepared the temple, Necho king of Egypt came up to fight against Carchemish by Euphrates: and Josiah went out against him.",
      "M": "After all this, when Josiah had put the temple in order, Neco king of Egypt came up to fight at Carchemish on the Euphrates, and Josiah went out to confront him.",
      "T": "The phrase 'after all this' carries the same ominous weight as its use in 32:1, where Sennacherib arrived 'after all these acts of faithfulness.' The greatest celebration of the covenant is followed by the empire. Neco II of Egypt (609 BC) was marching north to support the failing Assyrian empire against the rising Babylonian threat at Carchemish. He was not threatening Judah; his route passed through the Jezreel Valley and the Megiddo pass. Josiah's decision to intercept him is one of the most puzzling strategic choices in the Judean monarchy. He was not defending his territory from attack; he was blocking an army that had not come for him. The next verse explains what Neco said — and what Josiah failed to hear."
    },
    "21": {
      "L": "But he sent ambassadors to him, saying, What have I to do with thee, thou king of Judah? I come not against thee this day, but against the house wherewith I have war: for God commanded me to make haste: forbear thee from meddling with God, who is with me, that he destroy thee not.",
      "M": "But Neco sent envoys to him, saying, 'What do we have to do with each other, king of Judah? I am not coming against you today, but against the house with which I am at war. God has commanded me to hurry. Stop opposing God, who is with me, or he will destroy you.'",
      "T": "The most theologically unsettling verse in the chapter. Neco claimed that God had commanded his campaign — that he was acting under divine authorization, and that Josiah was opposing God by blocking him. The Chronicler's v22 makes the verdict explicit: Josiah 'did not listen to the words of Neco from the mouth of God.' The implication is uncomfortable but clear: the claim was true. The LORD was using the Egyptian king as his instrument for purposes Josiah did not understand — the same pattern as Sennacherib as a divine instrument (32:26), the same as Nebuchadnezzar in the chapters to come. The LORD uses pagan empires for his covenant purposes, and Josiah's failure to hear the divine word through a foreign king's mouth cost him his life."
    },
    "22": {
      "L": "Nevertheless Josiah would not turn his face from him, but disguised himself, that he might fight with him, and hearkened not unto the words of Necho from the mouth of God, and came to fight in the valley of Megiddo.",
      "M": "Nevertheless Josiah did not turn away from him but disguised himself to fight with him. He did not listen to the words of Neco, which came from the mouth of God, and went to fight in the Valley of Megiddo.",
      "T": "He disguised himself — the same verb used of Ahab before his fatal battle at Ramoth-Gilead (1 Kgs 22:30; 2 Chr 18:29). The echo is intentional and devastating: the greatest reformer of the southern kingdom, in his final act, reenacted the strategic and theological error of the faithless Ahab. Ahab disguised himself and went into battle against prophetic warning; Josiah disguised himself and went into battle against a word from God. Both died in battle. The disguise suggests that Josiah knew something was wrong — you disguise yourself when you are afraid of what will happen if you are identified — but he went forward anyway. 'Did not listen to the words of Neco, which came from the mouth of God': the Chronicler makes the verdict inescapable."
    },
    "23": {
      "L": "And the archers shot at king Josiah; and the king said to his servants, Have me away; for I am sore wounded.",
      "M": "The archers shot King Josiah, and the king said to his servants, 'Take me away, for I am badly wounded.'",
      "T": "The death of Josiah, the best king since David, was brief and militarily inglorious — struck by Egyptian archers in the Jezreel Valley, carried from the battlefield, dead in Jerusalem. There was no angelic intervention, no last-minute deliverance, no miraculous rescue of the kind the covenant had provided for his predecessors at their critical moments. Huldah had said he would 'go to his grave in peace' (34:28), and in the deeper sense that was true: he would not see the temple burn. But the manner of his death was the sign that even the best king was not exempt from mortality — and that the grace God gave him was protection from witnessing the catastrophe, not exemption from the sword."
    },
    "24": {
      "L": "His servants therefore took him out of that chariot, and put him in the second chariot that he had; and they brought him to Jerusalem, and he died, and was buried in one of the sepulchres of his fathers. And all Judah and Jerusalem mourned for Josiah.",
      "M": "So his servants removed him from his chariot, placed him in his second chariot, and brought him to Jerusalem, where he died and was buried in the tombs of his fathers. All Judah and Jerusalem mourned for Josiah.",
      "T": "He made it back to Jerusalem to die — which was a mercy, and perhaps the fulfillment of the 'in peace' promise in the most literal available sense: he died not on a foreign battlefield, unburied and dishonored, but in his city, in his tombs, with his people mourning him. The national mourning was real and deep. Josiah was the last king who had given Judah reason for genuine hope; with his death, the theological momentum of the reform began to dissipate immediately. The four kings who followed him in thirty-four years would lead to the destruction of everything he had built and restored."
    },
    "25": {
      "L": "And Jeremiah lamented for Josiah: and all the singing men and the singing women spake of Josiah in their lamentations to this day, and made them an ordinance in Israel: and, behold, they are written in the lamentations.",
      "M": "Jeremiah lamented for Josiah, and all the male and female singers commemorated Josiah in their laments — a custom observed to this day. These were recorded in the Laments.",
      "T": "Jeremiah was young — perhaps twenty or twenty-five years old — when Josiah died. His lament for the king was one of the early outputs of a prophetic career that would go on to produce the longest prophetic book in the Hebrew canon. The Chronicler notes that the lament tradition for Josiah was formalized into an ongoing communal practice. 'Recorded in the Laments' may refer to a collection that did not survive, or may be connected to the tradition surrounding Lamentations (though that book mourns Jerusalem's later destruction). The literary memorial to Josiah was the covenant community's declaration: this king mattered; this loss was irreplaceable."
    },
    "26": {
      "L": "Now the rest of the acts of Josiah, and his goodness, according to that which was written in the law of the LORD,",
      "M": "The rest of the acts of Josiah and his faithful deeds, as written in the law of the LORD,",
      "T": "The citation of sources begins with 'the law of the LORD' as the standard — Josiah's deeds are measured against the Torah, the same scroll that had shaped his reign. His acts are characterized as his 'goodness' (tovot), his faithful acts. The Chronicler rarely uses this word for a king's legacy; it signals the highest assessment available."
    },
    "27": {
      "L": "And his deeds, first and last, behold, they are written in the book of the kings of Israel and Judah.",
      "M": "His acts, first and last, are recorded in the Book of the Kings of Israel and Judah.",
      "T": "The double source — the law of the LORD (v26) and the royal annals (v27) — frames Josiah's legacy as uniquely documented: measured by Torah and preserved in history. 'First and last' covers the entire span: from the seeking God at sixteen to the death at Megiddo at thirty-nine. Everything is preserved. The Chronicler closes the account of Judah's last great king and turns to the four-king slide into exile."
    }
  },
  "36": {
    "1": {
      "L": "Then the people of the land took Jehoahaz the son of Josiah, and made him king in his father's stead in Jerusalem.",
      "M": "The people of the land took Jehoahaz son of Josiah and made him king in his father's place in Jerusalem.",
      "T": "The am-ha'aretz — the people of the land, the covenant community's permanent constituency — made the succession choice, as they had after Amon's assassination (33:25). They chose Jehoahaz over his older brother Eliakim, suggesting a popular preference that would be immediately overridden by Egyptian imperial power. The 'people of the land' had tried to keep the Davidic line and the covenant trajectory alive; Pharaoh Neco had other ideas."
    },
    "2": {
      "L": "Jehoahaz was three and twenty years old when he began to reign, and he reigned three months in Jerusalem.",
      "M": "Jehoahaz was twenty-three years old when he became king, and he reigned three months in Jerusalem.",
      "T": "Three months: the minimum duration the Chronicler records before external power intervened. Jehoahaz was the people's choice, and the empire removed him immediately. The three-month reign was not enough time to establish a policy or demonstrate a character. He exists in the record primarily as the first domino in the cascade of end-of-kingdom kings who would carry Judah to its destruction in four rapid reigns."
    },
    "3": {
      "L": "And the king of Egypt put him down at Jerusalem, and condemned the land in an hundred talents of silver and a talent of gold.",
      "M": "Then the king of Egypt deposed him at Jerusalem and imposed a tribute on the land of a hundred talents of silver and a talent of gold.",
      "T": "Neco reached back into Jerusalem and removed the king the people had chosen, extracting a punishing tribute in the process. A hundred talents of silver and one talent of gold: enormous sums, draining the treasury that Hezekiah's covenant faithfulness had accumulated (32:27). Judah's economy was being bled to pay for its new vassalage to Egypt. The tribute was also the price of Josiah's decision at Megiddo — the king's death had cost his kingdom its political independence."
    },
    "4": {
      "L": "And the king of Egypt made Eliakim his brother king over Judah and Jerusalem, and turned his name to Jehoiakim. And Necho took Jehoahaz his brother, and carried him to Egypt.",
      "M": "The king of Egypt made Eliakim his brother king over Judah and Jerusalem, renaming him Jehoiakim. Neco took Jehoahaz his brother and carried him to Egypt.",
      "T": "The name change was an imperial declaration of ownership: Neco gave Eliakim ('God establishes') the throne name Jehoiakim ('the LORD establishes'), signaling that the king's legitimacy was now derived from Egyptian sponsorship rather than from the covenant community's choice. Jehoahaz was deported to Egypt, where he would die in exile (Jer 22:10–12). The pattern that would repeat twice more — foreign powers deposing Judean kings and carrying them away — was being set by Egypt before Babylon arrived. Judah had lost control of its own succession."
    },
    "5": {
      "L": "Jehoiakim was twenty and five years old when he began to reign, and he reigned eleven years in Jerusalem: and he did that which was evil in the sight of the LORD his God.",
      "M": "Jehoiakim was twenty-five years old when he became king, and he reigned eleven years in Jerusalem. He did what was evil in the sight of the LORD his God.",
      "T": "Eleven years — the longest of the final four kings' reigns, entirely under Egyptian and then Babylonian suzerainty. The verdict is immediate: evil in the sight of the LORD. Jeremiah's oracles against Jehoiakim (Jer 22:13–19; 36:23) give us the texture of this evil: forced labor for personal building projects, shedding innocent blood, exploitation of the poor. Most strikingly, when Jeremiah's scroll of oracles was read to him, Jehoiakim cut it up column by column and burned it in the fire (Jer 36:23). The king who burned the prophet's scroll was the precise inverse of the king who tore his clothes when the Torah scroll was read. Jehoiakim was the complete reversal of Josiah's covenant renewal."
    },
    "6": {
      "L": "Against him came up Nebuchadnezzar king of Babylon, and bound him in fetters, to carry him to Babylon.",
      "M": "Nebuchadnezzar king of Babylon came up against him and bound him in bronze chains to take him to Babylon.",
      "T": "The new empire arrived. Nebuchadnezzar defeated Egypt at Carchemish in 605 BC — the battle Josiah had tried to prevent — and then extended his power southward into Judah. Jehoiakim, the Egyptian-installed king, was humiliated: bound in chains for transport to Babylon. Whether he was actually taken or whether Nebuchadnezzar left him as a vassal king (as 2 Kgs 24:1 suggests he served three years before rebelling) is left ambiguous here. The Chronicler's emphasis is on the subjugation: Jehoiakim was in chains before Nebuchadnezzar. The Egyptian overlord was gone; the Babylonian overlord had arrived."
    },
    "7": {
      "L": "Nebuchadnezzar also carried of the vessels of the house of the LORD to Babylon, and put them in his temple at Babylon.",
      "M": "Nebuchadnezzar also carried some of the vessels of the LORD's house to Babylon and placed them in his temple there.",
      "T": "The despoliation of the temple began incrementally. Some vessels — not all, not yet — were carried to Babylon and placed in Nebuchadnezzar's own temple, a theological statement as much as a military trophy: the conquering god was displaying the holy instruments of the conquered god's worship. The vessels that Solomon had made for the LORD's service (2 Chr 4) were now serving as decoration in a Babylonian shrine. The complete despoliation would come in stages, culminating in the burning of the temple (v19). But the process began here. Ezra 1:7–11 will later list 5,400 items returned by Cyrus — vessels that had been carefully preserved through decades of Babylonian custody, waiting."
    },
    "8": {
      "L": "Now the rest of the acts of Jehoiakim, and his abominations which he did, and that which was found in him, behold, they are written in the book of the kings of Israel and Judah: and Jehoiachin his son reigned in his stead.",
      "M": "The rest of the acts of Jehoiakim and the abominations he committed, and what was found against him — these are recorded in the Book of the Kings of Israel and Judah. And Jehoiachin his son succeeded him.",
      "T": "The summary of Jehoiakim's reign is pointedly negative: acts, abominations, and 'what was found in him' — a phrase suggesting hidden guilt, matters discovered that made the record even darker than what the Chronicler states. The brevity is itself a judgment: Jehoiakim does not deserve extended treatment. His son Jehoiachin took the throne and immediately faced the accumulated consequences of his father's eleven years of defiance."
    },
    "9": {
      "L": "Jehoiachin was eight years old when he began to reign, and he reigned three months and ten days in Jerusalem: and he did that which was evil in the sight of the LORD.",
      "M": "Jehoiachin was eight years old when he became king, and he reigned three months and ten days in Jerusalem. He did what was evil in the sight of the LORD.",
      "T": "Eight years old — though 2 Kings 24:8 gives eighteen, a well-known textual variant. The Chronicles number may reflect a co-regency beginning at eight with active rule at eighteen, or a scribal error in transmission (a dropped digit). The Chronicler's three months and ten days is more precise than 2 Kings' 'three months,' perhaps from a different source. The verdict — evil in the sight of the LORD — is given even to this child-king. Whatever evil was committed operated through the policies he inherited from his father and the officials who governed around him. The three-month-and-ten-day reign ended when Nebuchadnezzar came in the spring."
    },
    "10": {
      "L": "And when the year was expired, king Nebuchadnezzar sent, and brought him to Babylon, with the goodly vessels of the house of the LORD, and made Zedekiah his brother king over Judah and Jerusalem.",
      "M": "In the spring of the year, King Nebuchadnezzar sent and brought him to Babylon along with the precious vessels of the LORD's house, and made his brother Zedekiah king over Judah and Jerusalem.",
      "T": "The second deportation and the second despoliation. Jehoiachin was carried to Babylon — where he would eventually be released and honored by Evil-Merodach (2 Kgs 25:27–30), and where a large Jewish exile community would thrive for generations. The 'precious vessels' (literally 'vessels of desire,' the choicest of the temple's treasury) went with him. Zedekiah, described as Jehoiachin's brother (or uncle, as 2 Kgs 24:17 specifies), was Nebuchadnezzar's installation. The pattern was now fully established: Babylonian power chose Judah's kings as Egyptian power had before it. The covenant community no longer governed its own succession."
    },
    "11": {
      "L": "Zedekiah was one and twenty years old when he began to reign, and reigned eleven years in Jerusalem.",
      "M": "Zedekiah was twenty-one years old when he became king and reigned eleven years in Jerusalem.",
      "T": "Eleven years — equal to Jehoiakim's reign, the final eleven years of the Judean monarchy. Zedekiah was the last king of Judah, the last descendant of David to rule from Jerusalem before the Babylonian conquest. He was also the one whose specific decisions would determine the final outcome. The Chronicler's account identifies the precise theological failures that made destruction inevitable rather than a contingent tragedy."
    },
    "12": {
      "L": "And he did that which was evil in the sight of the LORD his God, and humbled not himself before Jeremiah the prophet speaking from the mouth of the LORD.",
      "M": "He did what was evil in the sight of the LORD his God. He did not humble himself before Jeremiah the prophet, who spoke from the mouth of the LORD.",
      "T": "The specific failure named for Zedekiah is not idolatry or military alliance alone but the refusal to humble himself before the prophetic word. Jeremiah was still alive, still speaking, still available. The prophet who had lamented Josiah was now the senior voice of the covenant's demands, and Zedekiah refused to hear him. The contrast with Josiah is exact and deliberate: Josiah heard the Torah read and immediately tore his clothes in grief; Zedekiah heard Jeremiah and hardened himself. The capacity for covenant hearing that had made Josiah the greatest king was precisely what Zedekiah lacked."
    },
    "13": {
      "L": "And he also rebelled against king Nebuchadnezzar, who had made him swear by God: but he stiffened his neck, and hardened his heart from turning unto the LORD God of Israel.",
      "M": "He also rebelled against King Nebuchadnezzar, who had made him swear by God. He stiffened his neck and hardened his heart against turning to the LORD, the God of Israel.",
      "T": "The double rebellion: against Nebuchadnezzar, breaking a sworn oath that had been made by God's name (making it a covenant violation as well as a political betrayal), and against the LORD by refusing to return in repentance. An oath sworn by God bound the swearer before God; to break it was theological treachery. Ezekiel elaborates at length on the weight of Zedekiah's broken oath (Ezek 17:11–21). The 'stiffened neck' and 'hardened heart' are the vocabulary of Pharaoh in Exodus — Zedekiah, the covenant king, had become like the pagan oppressor whose stubbornness was the original occasion for the plagues. The covenant community's king was reenacting the covenant's enemy."
    },
    "14": {
      "L": "Moreover all the chief of the priests, and the people, transgressed very much after all the abominations of the heathen; and polluted the house of the LORD which he had hallowed in Jerusalem.",
      "M": "Moreover, all the leading priests and the people greatly multiplied their unfaithfulness, following all the abominations of the nations and polluting the house of the LORD that he had made holy in Jerusalem.",
      "T": "The failure was not the king's alone. The priests — the leading priests, those responsible for maintaining the covenant's purity — were themselves deeply unfaithful. The abominations of the nations had returned; Manasseh's era of pollution had been driven out by Josiah and had come back. The house that the LORD had hallowed — where the divine name had been placed (2 Chr 6–7), that Josiah had repaired and in which the Torah had been found — was polluted again. The completeness of the reversal is the Chronicler's point: within a generation of Josiah's death, everything the reform had achieved had been undone."
    },
    "15": {
      "L": "And the LORD God of their fathers sent to them by his messengers, rising up betimes, and sending; because he had compassion on his people, and on his dwelling place:",
      "M": "The LORD, the God of their fathers, sent word to them persistently through his messengers because he had compassion on his people and on his dwelling place.",
      "T": "The grace that precedes judgment is among the Chronicler's most consistent theological emphases: before God acts in punishment, he speaks through his servants the prophets. 'Rising up early and sending' is a recurring idiom in Jeremiah (Jer 7:13, 25; 26:5; 32:33) for God's urgent, persistent communication — the LORD going to extraordinary lengths to reach a people that did not want to be reached. The compassion that motivated the sending was real: God did not want to destroy his people or his dwelling place. He sent messengers because he was trying to prevent what was coming."
    },
    "16": {
      "L": "But they mocked the messengers of God, and despised his words, and misused his prophets, until the wrath of the LORD arose against his people, till there was no remedy.",
      "M": "But they kept mocking the messengers of God, despising his words and scoffing at his prophets, until the wrath of the LORD arose against his people, until there was no remedy.",
      "T": "Three verbs for the rejection of the prophetic word: mocked, despised, scoffed at. The escalation implies not one refusal but a pattern of accumulated contempt across years and generations. The messengers were not merely ignored; they were mocked — treated as ridiculous, their warnings dismissed. The despising of the divine word was the exact inversion of the covenant requirement: 'Hear, O Israel.' The people heard and sneered. The result: the wrath arose, and there was no remedy. The Hebrew ein marpeh — literally 'no healing,' no way back from the wound. The covenant relationship had passed the point of repair."
    },
    "17": {
      "L": "Therefore he brought upon them the king of the Chaldeans, who slew their young men with the sword in the house of their sanctuary, and had no compassion upon young man or maiden, old man, or him that stooped for age: he gave them all into his hand.",
      "M": "Therefore he brought against them the king of the Chaldeans, who killed their young men with the sword in the house of their sanctuary — showing no compassion on young man or virgin, old man or the aged. God gave them all into his hand.",
      "T": "The covenant curse operating: military defeat described in the language that Lamentations (written at this moment by the prophet who had been mocked) would use to mourn it. 'In the house of their sanctuary' — the killing reached the temple precincts, the holy space. The absence of compassion was total: the Babylonians made no exceptions — youth, women, the elderly, the infirm. The theological note is essential: 'God gave them all into his hand.' This was not simply military defeat; it was the covenant God using Nebuchadnezzar as his instrument, exactly as he had used Assyria in earlier generations. The same God who had protected Jerusalem against Sennacherib at Hezekiah's prayer now gave Jerusalem to Nebuchadnezzar. The difference was not God's power but the covenant community's standing."
    },
    "18": {
      "L": "And all the vessels of the house of God, great and small, and the treasures of the house of the LORD, and the treasures of the king, and of his princes; all these he carried to Babylon.",
      "M": "All the vessels of the house of God, great and small, and the treasures of the house of the LORD and of the king and his officials — all these Nebuchadnezzar brought to Babylon.",
      "T": "The complete despoliation that had begun incrementally in Jehoiakim's day (v7) was now total. Every vessel — the great and the small, the functional and the ornamental, the sacred and the administrative — was carried to Babylon. The treasures of the royal household accompanied the temple's sacred objects. Solomon's great works of bronze and gold, crafted for the glory of the LORD's house (2 Chr 4), were now trophies in a Babylonian temple. Ezra 1:7–11 will later list 5,400 items returned by Cyrus — these vessels, carefully preserved through decades of Babylonian custody, waiting for the day when the exile would end."
    },
    "19": {
      "L": "And they burnt the house of God, and brake down the wall of Jerusalem, and burnt all the palaces thereof with fire, and destroyed all the goodly vessels thereof.",
      "M": "They burned the house of God and broke down the wall of Jerusalem. They burned all its palaces with fire and destroyed all its precious objects.",
      "T": "The destruction of everything Josiah had repaired, everything Solomon had built, everything David had prepared and Solomon had realized. The house of God — the temple whose dedication had been the theological center of the monarchy's highest moment, where the cloud of glory had filled the priests' sight and the people had fallen prostrate (2 Chr 5–7) — was burned. The wall that had protected Jerusalem since David's time was broken down. The palaces where the Davidic kings had ruled were consumed. In one campaign, the entire physical infrastructure of the covenant community's national existence was erased. This is the nadir of Chronicles. But the Chronicler will not end here."
    },
    "20": {
      "L": "And them that had escaped from the sword carried he away to Babylon; where they were servants to him and his sons until the reign of the kingdom of Persia:",
      "M": "He took into exile in Babylon those who had escaped from the sword. They became servants to him and his sons until the kingdom of Persia came to power.",
      "T": "The survivors of the sword became servants in Babylon — the covenant community in its lowest state, the full experience of the exile that Moses had prophesied (Lev 26:33; Deut 28:64). Servants to Nebuchadnezzar and his sons: the Babylonian dynasty that would rule until Cyrus the Persian ended it in 539 BC. The exile that began in 587 BC with the temple's destruction would last approximately fifty years, though the prophetic interpretation rounded to seventy (v21). The people who had been given the land, the covenant, the temple, and the promise were now slaves in Babylon. But the verse does not end at Babylon; it ends with 'until the reign of Persia.' The exile had a terminus."
    },
    "21": {
      "L": "To fulfil the word of the LORD by the mouth of Jeremiah, until the land had enjoyed her sabbaths: for as long as she lay desolate she kept sabbath, to fulfil threescore and ten years.",
      "M": "This fulfilled the word of the LORD spoken through Jeremiah, until the land had enjoyed its Sabbaths. All the days it lay desolate it kept Sabbath, fulfilling seventy years.",
      "T": "One of the most remarkable theological interpretations in the Hebrew Bible. The Chronicler connects the Babylonian exile to Leviticus 26:34–35, where God had promised that if Israel violated the covenant the land would lie desolate and 'make up for its Sabbaths.' The Sabbatical year system — leaving the land fallow every seventh year (Lev 25:1–7) — had apparently not been observed for generations across the monarchy's span. The land was owed its rest, and the exile was the mechanism by which it received what had been denied. Seventy years of desolation corresponding to seventy Sabbatical years unpaid over a 490-year span (70 × 7). Jeremiah had prophesied seventy years (Jer 25:11–12; 29:10), and the Chronicler connects that prophecy to the Levitical mechanism. The exile was not only punishment; it was cosmic accounting. The land was resting. And rest ends."
    },
    "22": {
      "L": "Now in the first year of Cyrus king of Persia, that the word of the LORD spoken by the mouth of Jeremiah might be accomplished, the LORD stirred up the spirit of Cyrus king of Persia, that he made a proclamation throughout all his kingdom, and put it also in writing, saying,",
      "M": "Now in the first year of Cyrus king of Persia, in order to fulfill the word of the LORD spoken through Jeremiah, the LORD stirred up the spirit of Cyrus king of Persia, so that he made a proclamation throughout all his kingdom and also put it in writing:",
      "T": "The pivot from judgment to hope — the word 'Now' opening the final movement of Chronicles and of the Hebrew canon in its traditional ordering. Cyrus came to power in 538 BC, and in his first year issued the decree allowing the Jewish exiles to return and rebuild the temple. The Chronicler frames this as the fulfillment of Jeremiah's seventy-year prophecy and as the result of the LORD stirring up Cyrus's spirit. The hiphil perfect 'stirred up' — God's sovereign single act — names what happened in a pagan king's heart as a divine initiative. Isaiah had named Cyrus explicitly as the LORD's anointed (Isa 44:28; 45:1) before Cyrus was born. The book of Ezra (1:1–3) begins with nearly these exact words; Chronicles and Ezra were originally one continuous work, and this passage is the seam."
    },
    "23": {
      "L": "Thus saith Cyrus king of Persia, All the kingdoms of the earth hath the LORD God of heaven given me; and he hath charged me to build him an house in Jerusalem, which is in Judah. Who is there among you of all his people? The LORD his God be with him, and let him go up.",
      "M": "Thus says Cyrus king of Persia: The LORD, the God of heaven, has given me all the kingdoms of the earth, and he has charged me to build him a house at Jerusalem, which is in Judah. Whoever among you is of all his people — may the LORD his God be with him, and let him go up.",
      "T": "The last words of Chronicles are an invitation: 'Let him go up.' The Hebrew canon, in its traditional order ending with Chronicles, closes not with the temple in ashes but with a Persian king's open invitation to rebuild. Cyrus acknowledges the LORD as the God of heaven who gave him all kingdoms — an extraordinary theological claim in the mouth of a Zoroastrian Persian emperor, whether derived from Isaiah's prophecy, from the Jewish community around him, or from his general policy of framing his patronage in each subject people's own theological language. The effect is the same: the exile was over. The land was waiting. The temple could be rebuilt. The final word — 'let him go up' — is not an ending but a beginning. The covenant story was not finished; it was resuming. After all the destruction, the last word of Chronicles is a door held open."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '2chronicles')
        merge_tier(existing, CHRONICLES2, tier_key)
        save(tier_dir, '2chronicles', existing)
    print('2 Chronicles 34–36 written.')

if __name__ == '__main__':
    main()
