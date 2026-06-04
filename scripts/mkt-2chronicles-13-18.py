"""
MKT 2 Chronicles chapters 13–18 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-2chronicles-13-18.py

Content:
- Ch 13: Abijah's reign; battle speech at Zemaraim; God strikes Jeroboam's army; Jeroboam dies
- Ch 14: Asa's early reform; fortification; Zerah the Ethiopian routed at Mareshah
- Ch 15: Azariah's prophecy to Asa; covenant renewal at Jerusalem; removal of Maacah
- Ch 16: Asa's treaty with Syria; Hanani the seer rebuked and imprisoned; Asa's diseased feet; death
- Ch 17: Jehoshaphat's reign; teaching mission throughout Judah; military census; peace
- Ch 18: Jehoshaphat joins Ahab; Micaiah's prophecy; battle of Ramoth-gilead; Ahab's death

Translation decisions (carried forward from mkt-2chronicles-7-12.py):
- H3068 (יהוה): "LORD" in L/M; "the LORD" in T. Consistent throughout OT scripts.
- H430 (אֱלֹהִים): "God" throughout all tiers.
- H2617 (חֶסֶד): "steadfast love" in L/M; "covenant loyalty" in T.
- H1285 (בְּרִית): "covenant" throughout; 15:12 has a solemn covenant-renewal ceremony.
- H5178 (נְחֹשֶׁת): "bronze" not "brass."
- H8034 (שֵׁם): "name" — the Name-theology carries through.
- H7307 (רוּחַ): "Spirit" (capitalized) at 15:1 where it is the divine Spirit coming upon Azariah;
  carries prophetic agency, not wind or breath.
- H3665 (humble/humbled): niphal reflexive — "humbled themselves"; same pattern as ch. 12.

New decisions for chs 13–18:
- H4417 (מֶלַח, "salt") at 13:5: "covenant of salt" — a perpetual, unalterable covenant.
  Salt was used in ancient treaties as a preservative symbol of permanence; cf. Num 18:19 and
  Lev 2:13. T names this explicitly.
- H8172 (שָׁעַן, "rely/lean") at 13:18 and 16:7-8: the key theological verb "rely on."
  In Chronicles the verb marks the watershed between faithfulness and unfaithfulness.
  Judah relies on (shaan) the LORD → victory; Asa relies on Ben-hadad → defeat.
  L/M: "relied on"; T: "rested their weight on" or "leaned on" to surface the physical metaphor.
- H5315 (נֶפֶשׁ) at 15:12: "soul" — the whole person committing to seek God with entire being.
- H2617 at 15:15: the people "sought him with their whole desire" — rendered literally in L;
  M reads naturally; T emphasizes the wholeness of the seeking.
- H7200 (רָאָה, saw) and the heavenly vision at 18:18-22: Micaiah's throne vision is rendered
  carefully. The "lying spirit" (18:21-22) presents a genuine theological difficulty — not
  God lying, but God permitting a deceiving spirit to execute judgment. T notes this explicitly.
- H8083 (eight hundred thousand) at 13:3: the battle numbers (400k vs 800k) are astronomical;
  either they are hyperbolic conventions for "overwhelming force" (as ancient Near Eastern battle
  narratives routinely used) or symbolic. L/M preserve the numbers as given; T notes the
  rhetorical function.
- Asa and physicians at 16:12: H7495 (רָפָא, heal) for physicians. The rebuke is not anti-
  medicine but about the heart's direction: Asa's failure was seeking physicians instead of
  seeking the LORD first — the same pattern as his alliance with Syria.
- Aspect notes:
  - Ch 13: Abijah's speech uses perfect tenses for historical facts (the covenant was given,
    Jeroboam rebelled); the battle narrative uses waw-consecutive imperfects for sequential action.
  - Ch 14: Asa's prayer (14:11) uses imperative and cohortative forms — urgent pleading;
    T renders the directness of the prayer.
  - Ch 15: Azariah's prophecy uses conditional-prophetic forms; v. 2 is the Chronicler's
    thesis statement for the entire section.
  - Ch 16: Hanani's oracle uses perfect and imperfect to balance past opportunity (already
    lost) with future consequence (now unavoidable).
  - Ch 18: Micaiah first echoes the false prophets sarcastically (v. 14) before delivering
    the true oracle (v. 16); the irony is preserved in all three tiers.
- OT intertextuality:
  - 13:5: "covenant of salt" echoes Num 18:19 (Aaronic covenant of salt) and Lev 2:13;
    the Davidic covenant is being claimed as equally permanent.
  - 13:11: Abijah's description of Judah's legitimate worship (lamps, showbread, burnt offerings)
    echoes the tabernacle instructions of Exod 25-30 and Lev 24. His point: Judah has the real
    worship; Israel has substitutes.
  - 14:11: Asa's prayer ("it is nothing for you to help, whether with many or with those who
    have no power") echoes the theological pattern of Gideon (Judg 7), Jonathan (1 Sam 14:6),
    and eventually Hezekiah. God's victories are always achieved through impossible odds to
    demonstrate that the strength is his.
  - 15:2: "If you seek him, he will be found by you; if you forsake him, he will forsake you"
    is the Chronicler's governing theorem, repeated in multiple registers throughout the book.
    It echoes Deut 4:29 and foreshadows 2 Chr 7:14.
  - 16:9: "The eyes of the LORD run to and fro throughout the whole earth" echoes Zech 4:10
    (the seven eyes of the LORD surveying all the earth). God's omniscience is active watchfulness
    in behalf of those who trust him — not surveillance for punishment but searching for
    opportunity to show himself strong.
  - 18:16: Micaiah's vision of Israel "scattered like sheep without a shepherd" uses the
    sheep/shepherd image that runs from Num 27:17 (Moses praying for a successor) through
    Ezek 34 to Jesus's compassion for the crowds (Matt 9:36; John 10).
  - 18:18-22: The heavenly court scene echoes Job 1-2 (the sons of God presenting themselves
    before the LORD) and 1 Kgs 22 (the parallel account). The portrait of divine sovereignty
    operating through secondary causes (including deceptive ones) is part of the Bible's honest
    account of how God governs a fallen world.
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
  "13": {
    "1": {
      "L": "In the eighteenth year of King Jeroboam, Abijah began to reign over Judah.",
      "M": "In the eighteenth year of Jeroboam's reign, Abijah became king over Judah.",
      "T": "Abijah stepped onto the throne of Judah while Jeroboam was still king in the north — the divided kingdom was a generation old, and the northern and southern dynasties had been locked in low-level warfare since Rehoboam's folly at Shechem. Abijah's reign began in the shadow of that conflict."
    },
    "2": {
      "L": "He reigned three years in Jerusalem. His mother's name was Micaiah the daughter of Uriel of Gibeah. And there was war between Abijah and Jeroboam.",
      "M": "He reigned three years in Jerusalem. His mother was Micaiah daughter of Uriel of Gibeah. There was war between Abijah and Jeroboam.",
      "T": "Three years — a short reign by any measure, but it contained one decisive engagement. His mother Micaiah was the granddaughter of Absalom through her father Uriel of Gibeah. The war with Jeroboam that had simmered since Rehoboam's day now came to a head."
    },
    "3": {
      "L": "Abijah set the battle in array with an army of valiant men of war, four hundred thousand chosen men; Jeroboam drew up his battle line against him with eight hundred thousand chosen men, mighty men of valor.",
      "M": "Abijah deployed for battle with an army of four hundred thousand valiant warriors; Jeroboam drew up against him with eight hundred thousand chosen, mighty fighters.",
      "T": "The numbers are staggering — four hundred thousand against eight hundred thousand, Judah's force outnumbered two to one. Whether these figures are precise military tallies or the hyperbolic convention of ancient battle narrative (where armies are described by overwhelming scale to glorify the victory), the theological point is identical: Judah was badly outnumbered, and what happened next could only be explained by God."
    },
    "4": {
      "L": "Then Abijah stood up on Mount Zemaraim, which is in the hill country of Ephraim, and said, 'Hear me, O Jeroboam and all Israel!'",
      "M": "Abijah took his position on Mount Zemaraim in the hill country of Ephraim and called out: 'Listen to me, Jeroboam and all Israel!'",
      "T": "Before the battle began, Abijah ascended Zemaraim — a ridge in the central highlands — and delivered a pre-battle oration. This was a recognized convention: the leader spoke to both armies, claiming moral and theological authority for his cause. Abijah's speech is one of the most theologically substantial in Chronicles."
    },
    "5": {
      "L": "'Ought you not to know that the LORD God of Israel gave the kingship over Israel forever to David and his sons by a covenant of salt?'",
      "M": "'Do you not know that the LORD God of Israel gave David and his sons the kingship over Israel forever through a covenant of salt?'",
      "T": "Abijah begins with the covenant. The covenant of salt — salt being the ancient symbol of permanence, incorruptibility, the covenant sworn at table and sealed with the seasoning that does not spoil — was the Davidic grant of dynastic succession. Numbers 18:19 uses the same phrase for the Aaronic covenant. Abijah's claim was foundational: God gave this kingdom to David's line unconditionally and permanently. Jeroboam's northern kingdom was rebellion against a covenant, not an alternative government."
    },
    "6": {
      "L": "'Yet Jeroboam the son of Nebat, a servant of Solomon the son of David, rose up and rebelled against his lord.'",
      "M": "'But Jeroboam son of Nebat, who was a servant of Solomon son of David, rose up and rebelled against his master.'",
      "T": "The history given with precision. Jeroboam was not a king who established a rival dynasty from independent authority; he was a servant — a royal administrator under Solomon — who rebelled against the master he served. The rebellion was not political realignment but covenant treason."
    },
    "7": {
      "L": "'And worthless scoundrels gathered around him and strengthened themselves against Rehoboam the son of Solomon, when Rehoboam was young and tenderhearted and could not withstand them.'",
      "M": "'Worthless troublemakers rallied around him and overpowered Rehoboam son of Solomon, when Rehoboam was young and inexperienced and unable to resist them.'",
      "T": "Abijah's characterization of the Shechem crisis is politically pointed: the men who drove the kingdom's division were 'sons of Belial' — the Hebrew phrase for men of worthlessness, the morally dissolute. He does not excuse Rehoboam's foolishness, but he attributes the effective political force to the agitators around Jeroboam. Rehoboam was young, tender-hearted, not yet hardened into leadership — and he was surrounded by the wrong advisers. Abijah is making the case that the north's existence owes more to rabble-rousing than to legitimate political grievance."
    },
    "8": {
      "L": "'And now you think to withstand the kingdom of the LORD in the hand of the sons of David, because you are a great multitude and have with you the golden calves that Jeroboam made for you as gods.'",
      "M": "'Now you plan to oppose the kingdom of the LORD, held by David's descendants. You are a great crowd, and you have the golden calves Jeroboam made as your gods.'",
      "T": "The charge turns theological: the northern kingdom is not merely rebellious against David's dynasty but against the kingdom of the LORD. And the golden calves — Jeroboam's substitute worship system installed at Bethel and Dan to prevent his people from going to Jerusalem — are named as the emblem of that rebellion. You bring numbers and idols; we bring the LORD."
    },
    "9": {
      "L": "'Have you not driven out the priests of the LORD, the sons of Aaron, and the Levites, and made priests for yourselves like the peoples of other lands? Whoever comes to consecrate himself with a young bull or seven rams becomes a priest of what are not gods.'",
      "M": "'Have you not expelled the LORD's priests — the sons of Aaron and the Levites — and appointed priests for yourselves as the other nations do? Anyone who brings a young bull and seven rams for consecration becomes a priest of what are no gods at all.'",
      "T": "The indictment of the northern priesthood is precise and damning. Jeroboam had expelled the Levites (as the Chronicler already noted in chapter 11) and opened the priesthood to anyone willing to bring the required animals. The contrast with the Aaronic priesthood — divinely appointed, genealogically specified, consecrated through rigorous ceremony — could not be starker. What is called priesthood in the north is an office open to purchase; what are called gods are golden cattle. Abijah names the emptiness directly: not gods."
    },
    "10": {
      "L": "'But as for us, the LORD is our God, and we have not forsaken him. We have priests ministering to the LORD who are sons of Aaron, and Levites for their service.'",
      "M": "'But we have the LORD as our God, and we have not abandoned him. The sons of Aaron serve as priests of the LORD, and the Levites assist them.'",
      "T": "The contrast is stated plainly: we have not forsaken the LORD. While Israel was establishing a counterfeit worship system, Judah maintained the legitimate one. Aaronic priests. Levitical ministers. The system that Moses established in the wilderness, that David organized for the temple, that Solomon implemented at the dedication — still running, still faithful, still legitimate."
    },
    "11": {
      "L": "'Every morning and every evening they offer burnt offerings and fragrant incense to the LORD, and set out the showbread on the pure table, and tend the lampstand of gold with its lamps burning every evening. For we keep the charge of the LORD our God, but you have forsaken him.'",
      "M": "'Morning and evening they present burnt offerings and fragrant incense to the LORD, arrange the showbread on the pure table, and light the gold lampstand every evening — because we maintain the service of the LORD our God. But you have abandoned him.'",
      "T": "The daily liturgy of the Jerusalem temple — burnt offerings, incense, showbread, lampstand — is recited like a liturgical argument. These were the prescriptions of Exodus 25-30 and Leviticus 24, the worship God commanded through Moses. Judah is not merely politically legitimate; it is liturgically faithful. The morning and evening offerings have continued uninterrupted. The lampstand burns. The showbread is set out. While Israel improvised a substitute religion, Judah maintained the practice of the tabernacle. 'But you have forsaken him' — the verdict of the speech, delivered with the daily offerings as its evidence."
    },
    "12": {
      "L": "'Behold, God is with us at our head, and his priests with battle trumpets to sound the alarm against you. O children of Israel, do not fight against the LORD, the God of your fathers, for you cannot succeed.'",
      "M": "'God is with us at our head, his priests are here with trumpets to sound the call against you. People of Israel, do not fight against the LORD, the God of your ancestors — you will not succeed.'",
      "T": "The speech ends with a warning that is also an invitation. God himself stands at the head of Judah's army. The priests hold the battle trumpets, the instruments that summoned the divine warrior to battle (Num 10:9). The warning is stark: if God is on our side and you fight us, you are fighting God — and no one wins that fight. 'You cannot succeed' is not a threat but a theological statement about the direction of history. The sermon is over. The armies are about to move."
    },
    "13": {
      "L": "Jeroboam had sent an ambush around to come upon them from behind; his troops were in front of Judah, and the ambush was behind them.",
      "M": "But Jeroboam had sent troops around to attack from behind; his forces were in front of Judah while the ambush was behind them.",
      "T": "While Abijah was still speaking, Jeroboam was already acting. The battle speech was delivered into the face of a military trap already closing: an ambush behind them, the main force before them. Judah was completely surrounded. This was Jeroboam's response to the theological argument — not words but encirclement. The situation, humanly speaking, was hopeless."
    },
    "14": {
      "L": "And when Judah looked, behold, the battle was in front of and behind them. And they cried to the LORD, and the priests blew the trumpets.",
      "M": "When the men of Judah looked, they faced battle on every side. They cried out to the LORD, and the priests blew their trumpets.",
      "T": "Judah turned and saw the trap. Front and rear — no escape. In that moment of total military exposure, they did exactly what Abijah's speech had told them to do: they cried to the LORD, and the priests sounded the trumpets. The battle trumpets were not a signal to attack; they were a call on God. Numbers 10:9 had promised: 'When you go to war in your land against the adversary who oppresses you, you shall sound an alarm with the trumpets, that you may be remembered before the LORD your God, and you shall be saved from your enemies.' They remembered the promise in the moment of greatest need."
    },
    "15": {
      "L": "Then the men of Judah raised the battle shout. And when the men of Judah shouted, God struck Jeroboam and all Israel before Abijah and Judah.",
      "M": "The men of Judah raised a battle cry. As they shouted, God struck Jeroboam and all Israel down before Abijah and Judah.",
      "T": "The shout of battle — not the clash of weapons but the shout — was the moment God acted. As Judah's voices rose in the cry that mingled prayer and battle-call, God struck. Not Abijah struck, not Judah's army struck — God struck Jeroboam and all Israel. The military battle was the visible aftermath of the divine intervention. Surrounded, outnumbered two to one, trapped in an ambush, Judah shouted — and the LORD fought for them."
    },
    "16": {
      "L": "The children of Israel fled before Judah, and God delivered them into their hand.",
      "M": "The Israelites fled before the men of Judah, and God gave them into Judah's power.",
      "T": "Flight — the same army that had set the ambush now ran. God delivered them: the verb is natan, gave, handed over. The army of Israel was not defeated by superior tactics or equipment; it was handed to Judah by the One who had watched the whole confrontation from the beginning. The theological language is exact."
    },
    "17": {
      "L": "Abijah and his people struck them with a great blow, so there fell slain of Israel five hundred thousand chosen men.",
      "M": "Abijah and his army inflicted a crushing defeat — five hundred thousand chosen men of Israel fell dead.",
      "T": "Five hundred thousand — an astronomical number, again following the ancient Near Eastern convention of hyperbolic scale to communicate overwhelming divine-enabled victory. If the battle numbers are symbolic rather than literal, the theological claim stands with equal force: the defeat of Israel that day was total. God's intervention on behalf of those who cried to him was decisive."
    },
    "18": {
      "L": "Thus the children of Israel were brought low at that time, and the children of Judah prevailed, because they relied on the LORD, the God of their fathers.",
      "M": "Israel was humbled at that time, and Judah prevailed because they relied on the LORD, the God of their ancestors.",
      "T": "The Chronicler's theological summary: Israel humbled, Judah prevailing — because they relied on the LORD. The word 'relied' (shaan) is the key. It means to lean on, to rest one's weight against. Judah had leaned on the LORD in the worst possible military moment — surrounded, outnumbered, no escape — and the LORD had held them. This verse will echo forward into chapter 16, when Asa does the opposite: relies on Ben-hadad instead of the LORD, and loses what he should have won."
    },
    "19": {
      "L": "And Abijah pursued Jeroboam and took cities from him: Bethel with its villages, Jeshanah with its villages, and Ephrain with its villages.",
      "M": "Abijah pursued Jeroboam and captured cities from him — Bethel and its surrounding villages, Jeshanah with its villages, and Ephrain with its villages.",
      "T": "The pursuit extended the victory. Abijah captured Bethel — the very city where Jeroboam had installed the golden calves as the northern worship site. The symbolic weight of this is heavy: Abijah, who had just denounced the calves in his speech, now controlled the city that housed them. Bethel, the house of God by name, had become the house of idols; now it was in the hands of the Davidic king who preached the true worship."
    },
    "20": {
      "L": "Jeroboam did not regain his power in the days of Abijah. The LORD struck him down, and he died.",
      "M": "Jeroboam never recovered his strength during Abijah's lifetime. The LORD struck him, and he died.",
      "T": "Jeroboam, who had ruled the north for decades, never recovered from this defeat. The LORD struck him — not a natural death but divine judgment on the man who had established the counterfeit priesthood and the golden calves. He died. The founder of Israel's apostasy was removed. But his system would outlast him for two more centuries."
    },
    "21": {
      "L": "But Abijah grew mighty. He took fourteen wives and had twenty-two sons and sixteen daughters.",
      "M": "Abijah, however, grew strong. He married fourteen wives and had twenty-two sons and sixteen daughters.",
      "T": "Abijah, so recently outnumbered and surrounded, grew mighty — the Chronicler's term for the covenant blessing of strength that came with faithfulness. Fourteen wives, thirty-eight children: the royal household expanded with the kingdom's prosperity. The victory at Zemaraim was not just a battle won but a reign established."
    },
    "22": {
      "L": "The rest of the acts of Abijah, his ways and his sayings, are written in the story of the prophet Iddo.",
      "M": "The rest of Abijah's acts, his conduct and his words, are recorded in the chronicle of the prophet Iddo.",
      "T": "Iddo the prophet again — the seer whose chronicle preserved what the official records did not: the theological interpretation of events. The 'story' or midrash of Iddo contained not just facts but explanation, not just sequence but meaning. Abijah's three-year reign ends with a battle and a reference to a prophetic archive. He is gone from the stage as quickly as he entered it."
    }
  },
  "14": {
    "1": {
      "L": "So Abijah slept with his fathers, and they buried him in the city of David. And Asa his son reigned in his place. In his days the land had rest for ten years.",
      "M": "Abijah rested with his ancestors and was buried in the city of David. His son Asa reigned in his place. The land enjoyed ten years of rest during his reign.",
      "T": "Abijah's brief three years ended; Asa's forty-one began. Ten years of peace — the Chronicler reports this as the immediate inheritance of Asa's reign. Faithful kings bring rest to the land; this is a pattern that runs through every chapter of Chronicles. The peace is not political fortune; it is the fruit of the faithfulness that will be described in the verses that follow."
    },
    "2": {
      "L": "And Asa did what was good and right in the eyes of the LORD his God.",
      "M": "Asa did what was good and right in the sight of the LORD his God.",
      "T": "The royal verdict — good and right in the LORD's sight — is given before the evidence. The Chronicler presents the moral conclusion and then provides the details. Asa was one of the better kings; his reign of forty-one years would end in failure, but it began with genuine faithfulness."
    },
    "3": {
      "L": "He removed the foreign altars and the high places and broke down the pillars and cut down the Asherim",
      "M": "He removed the foreign altars and the high places, smashed the sacred pillars, and cut down the Asherah poles.",
      "T": "The reform program: systematic, comprehensive, deliberate. Foreign altars (the worship of Baal and other Canaanite gods that had crept back into Judah under Rehoboam and through the corrupt Maacah influence). High places (the unauthorized local shrines). Sacred standing stones (massebot — the phallic or memorial pillars used in Canaanite worship). Asherah poles (the wooden cult symbols of the Canaanite fertility goddess). Asa cut through all of it. This was the work of a king who understood that reform meant removal, not accommodation."
    },
    "4": {
      "L": "and commanded Judah to seek the LORD, the God of their fathers, and to keep the law and the commandment.",
      "M": "He commanded the people of Judah to seek the LORD, the God of their ancestors, and to observe the law and commandments.",
      "T": "Removal without replacement produces a vacuum; Asa filled the vacuum with command. Seek the LORD — the active, purposeful orientation of a nation's life toward its God. Keep the law and commandments — the covenant structure that organized that seeking into concrete life practice. Asa did not merely clear the land of idols; he redirected the nation's worship toward the true God."
    },
    "5": {
      "L": "He also removed from all the cities of Judah the high places and the incense altars. And the kingdom had rest under him.",
      "M": "He removed the high places and incense altars from every town in Judah, and the kingdom was at peace under him.",
      "T": "The reform extended to every city — not just Jerusalem, not just the prominent shrines, but every town in Judah. The incense altars (hammamin — the sun-pillars or incense stands associated with Baal worship) were taken down. And the kingdom had rest. The connection is the Chronicler's causal: peace follows faithfulness. The land rested because the people turned to the LORD."
    },
    "6": {
      "L": "And he built fortified cities in Judah, for the land had rest. He had no war in those years, for the LORD had given him rest.",
      "M": "He built fortified cities in Judah during those years of peace, because the LORD gave him rest and no war came against him.",
      "T": "Asa used the years of peace to build. This is the pattern of faithful kings in Chronicles: the peace that God provides creates the conditions for constructive work, and the wise king uses the quiet season to strengthen the kingdom for the inevitable tests ahead. The peace was not luck but a gift: the LORD gave him rest."
    },
    "7": {
      "L": "He said to Judah, 'Let us build these cities and surround them with walls and towers, gates and bars. The land is still ours, because we have sought the LORD our God. We have sought him, and he has given us peace on every side.' So they built and prospered.",
      "M": "'Let us build these cities and surround them with walls, towers, gates, and bars,' he told Judah. 'The land is still ours because we have sought the LORD our God. We sought him and he has given us rest on every side.' So they built and prospered.",
      "T": "Asa's building speech is a theology of provision: the land is ours because we have sought him. The prosperity is not autonomous; it flows directly from the seeking. He names the cause openly, in public address, before the building begins. The people need to know why they have peace and why the building is possible, so that the connection between faithfulness and flourishing is not forgotten when the next test comes. They built — and they prospered, the verb that marks covenant blessing."
    },
    "8": {
      "L": "Asa had an army of three hundred thousand from Judah, armed with large shields and spears, and two hundred and eighty thousand men from Benjamin who carried shields and drew bows — all these were mighty men of valor.",
      "M": "Asa's army consisted of three hundred thousand shield-and-spear warriors from Judah and two hundred and eighty thousand archers with shields from Benjamin — all mighty fighting men.",
      "T": "Five hundred and eighty thousand — a substantial force drawn from both the tribes of Judah and Benjamin that made up the southern kingdom. Heavy infantry from Judah, archers from Benjamin. The military was well organized and well armed. But numbers and weapons, as the next episode will demonstrate, are not the decisive factor."
    },
    "9": {
      "L": "Zerah the Ethiopian came out against them with an army of a million men and three hundred chariots, and came as far as Mareshah.",
      "M": "Zerah the Cushite marched out against them with a force of a million men and three hundred chariots, advancing as far as Mareshah.",
      "T": "Zerah the Cushite — likely a military commander from the upper Nile region, possibly acting as a general under Egyptian command, though the Chronicler presents him as an independent threat. A million men and three hundred chariots: again, numbers that describe overwhelming force. Judah had nearly six hundred thousand warriors; Zerah brought nearly twice that number plus armored vehicles. He advanced to Mareshah — the same Judean foothills city where Abijah had won his great victory. The same terrain, a larger threat."
    },
    "10": {
      "L": "Asa went out against him, and they drew up their battle lines in the Valley of Zephathah at Mareshah.",
      "M": "Asa went out to meet him, and they drew up for battle in the Valley of Zephathah near Mareshah.",
      "T": "Asa met the threat directly rather than retreating to Jerusalem. The Valley of Zephathah at Mareshah: the same general region where Judah had fought before. The armies deployed. The overwhelming numerical disadvantage was visible to everyone on the field."
    },
    "11": {
      "L": "And Asa cried to the LORD his God, 'O LORD, there is none like you to help, between the mighty and the weak. Help us, O LORD our God, for we rely on you, and in your name we have come against this multitude. O LORD, you are our God; let not man prevail against you.'",
      "M": "Asa called out to the LORD his God: 'LORD, only you can help the powerless against the mighty. Help us, LORD our God, for we rely on you and have come against this vast army in your name. LORD, you are our God — do not let any man prevail against you.'",
      "T": "One of the greatest battle prayers in all of Scripture. Asa does not pray for his army to be strong; he prays by acknowledging his army's weakness: there is no one like you to help between the mighty and those who have no strength. The prayer strips away all pretense of military confidence and rests everything on the character of God. 'We rely on you' — the same verb shaan that will mark the theological turning point in chapter 16 when Asa leans on Syria instead. Here, at Mareshah, he leans on the LORD. 'In your name we have come' — the battle is not about Asa's kingdom but God's honor; what happens here reflects on who the LORD is. The final petition is remarkable: let not man prevail against you — make this about your glory, not ours."
    },
    "12": {
      "L": "So the LORD struck the Ethiopians before Asa and before Judah, and the Ethiopians fled.",
      "M": "So the LORD struck down the Cushites before Asa and Judah, and they fled.",
      "T": "The LORD struck. Not Asa's army, not the military strategy — the LORD struck the Ethiopians, and they ran. The prayer was heard the moment it was prayed; the battle was won before it was fought, because the God who holds all armies in his hand had already decided the outcome. Asa prayed the right prayer — 'we have no strength, only you' — and the God who shows himself strong on behalf of those with no strength did exactly that."
    },
    "13": {
      "L": "Asa and the people who were with him pursued them as far as Gerar, and the Ethiopians fell until none remained alive, for they were broken before the LORD and his army. The men of Judah carried away very much spoil.",
      "M": "Asa and his forces pursued them all the way to Gerar. The Cushites fell until none could survive, for they were shattered before the LORD and his army. Judah carried off enormous plunder.",
      "T": "The pursuit extended the rout thirty miles or more from Mareshah south and west to Gerar. The destruction was total: 'none remained alive' — the language of a divinely ordained victory in which the enemy is utterly broken. 'They were broken before the LORD' — the passive construction naming God as the active force. The army of Judah pursued; the LORD broke. The roles are clear. The plunder that Shishak had taken from Jerusalem's treasury in Rehoboam's day was now partially repaid from the wreckage of Zerah's campaign."
    },
    "14": {
      "L": "And they attacked all the cities around Gerar, for the fear of the LORD was upon them. They plundered all the cities, for there was much plunder in them.",
      "M": "They struck all the towns around Gerar, for the terror of the LORD had fallen on those towns. They plundered all of them, for there was great plunder to be had.",
      "T": "The fear of the LORD — the reverential dread that accompanies the recognition of divine power at work — fell on the entire region around Gerar. The cities did not resist; they could not. When the LORD of armies fights, the terror precedes the troops. This is the same dynamic that had worked for Joshua in Canaan (Josh 2:9-11) and for Israel crossing the Jordan. God's victories come with a psychological dimension: the enemies know something supernatural is happening and are undone by it."
    },
    "15": {
      "L": "They also attacked the tents of those who had livestock and carried off sheep in abundance and camels. Then they returned to Jerusalem.",
      "M": "They also raided the pastoralists' camps and took large numbers of sheep and camels. Then they returned to Jerusalem.",
      "T": "The pastoral herds of the region — livestock, sheep, camels — were swept up in the spoil. The Chronicler notes the return to Jerusalem: the campaign that began with Zerah's threat ended with the army coming home loaded with the wealth of their enemies. The same principle at work in the campaign: the nation that sought the LORD, fought in his name, and prayed the prayer of total dependence came home carrying more than it left with."
    }
  },
  "15": {
    "1": {
      "L": "The Spirit of God came upon Azariah the son of Oded,",
      "M": "The Spirit of God came upon Azariah son of Oded,",
      "T": "The Spirit of God — resting on a man named Azariah son of Oded, otherwise unknown to us. The prophetic Spirit comes where it will, on the person God chooses, not necessarily the great or famous. Azariah appears once in all of Scripture — at this moment, to deliver one decisive message to the king who needed to hear it."
    },
    "2": {
      "L": "and he went out to meet Asa and said to him, 'Hear me, Asa, and all Judah and Benjamin: the LORD is with you while you are with him. If you seek him, he will be found by you, but if you forsake him, he will forsake you.'",
      "M": "'Listen to me, Asa and all Judah and Benjamin: the LORD is with you as long as you are with him. Seek him and he will let you find him, but if you abandon him, he will abandon you.'",
      "T": "This is the Chronicler's governing theorem, spoken in its clearest form. Seven words in Hebrew set the entire framework: the LORD is with you while you are with him. The divine presence is not unconditional in the human sense — it is covenantally responsive. The God who is always faithful will be 'with' those who are 'with' him in the sense of covenantal loyalty. Seek him: the active posture of a people who turn toward God. He will be found — God is findable; he does not hide. But forsake him: the word azab again, the covenant word for abandonment. If you abandon the covenant, the covenant's blessings withdraw. This verse echoes Deuteronomy 4:29 and anticipates 2 Chronicles 7:14. It is the hermeneutical key to everything that follows in Asa's reign — and in all of Chronicles."
    },
    "3": {
      "L": "'For a long time Israel was without the true God, without a teaching priest, and without law.'",
      "M": "'For many years Israel had no true God, no teaching priest, and no law.'",
      "T": "Azariah reaches back into Israel's history — likely the period of the judges or the worst of the divided monarchy — as a warning from memory. Three absences that compounded into catastrophe: no true God (not that God was absent, but that Israel had abandoned him for idols); no teaching priest (the Levitical office of instruction, not just sacrifice, had collapsed); no law (the Torah as the organizing structure of national life, forgotten or ignored). The list names what happens when a nation forsakes the LORD: the entire infrastructure of covenant life — worship, instruction, law — falls apart. This is where Israel goes without the faithfulness Azariah is urging."
    },
    "4": {
      "L": "'But when in their trouble they turned to the LORD, the God of Israel, and sought him, he was found by them.'",
      "M": "'But when in their distress they turned to the LORD, the God of Israel, and sought him, he let them find him.'",
      "T": "And even then — even after all three pillars of covenant life had collapsed — when they turned back, he was found. This is the persistent mercy at the heart of the Chronicler's theology. No abandonment is so complete that return is impossible. Turn, seek, find: three verbs of restoration available at any moment to any generation that chooses them. The same God who was forsaken can be sought and found again."
    },
    "5": {
      "L": "'In those times there was no peace for the one going out or coming in, for great disturbances afflicted all the inhabitants of the lands.'",
      "M": "'In those times it was dangerous to travel, for great turmoil troubled everyone in every land.'",
      "T": "The social consequence of abandoning God: violence and instability so pervasive that no journey was safe. 'Going out or coming in' — the idiom for ordinary daily life, commerce, travel — was disrupted by 'great tumults.' The political and social order that God's covenant maintains collapsed when the covenant was abandoned. The nations descended into mutual violence. This is not merely ancient history; it is the Chronicler's description of what unfaithfulness produces at the civilizational level."
    },
    "6": {
      "L": "'They were broken in pieces, nation against nation and city against city, for God troubled them with every kind of distress.'",
      "M": "'Nation fought nation and city attacked city, for God sent every kind of adversity to trouble them.'",
      "T": "God troubled them — the divine agency is explicit. The chaos that follows covenant abandonment is not random; it is divinely permitted or even directed judgment. Nations turn against each other; cities against cities; the social fabric shreds. God does not passively watch; he 'troubles' the nations that forsake him, as he promised in Deuteronomy 28. The disintegration is purposeful: to bring them to their senses, to drive them back to the seeking that produces peace."
    },
    "7": {
      "L": "'But you, be strong and do not let your hands be weak, for your work shall be rewarded.'",
      "M": "'But as for you, be strong, and do not give up, for your work will be rewarded.'",
      "T": "The oracle pivots from warning to encouragement. All the historical description — the periods of apostasy and punishment, the divine troubles and social violence — is context for this final word: be strong, don't weaken, your work will be rewarded. Asa has just won the greatest military victory of his reign; now the prophet tells him that the real battle is ahead, in the interior work of ongoing faithfulness. Your work — the reform, the seeking, the covenant maintenance — will not be wasted. God sees it and will honor it."
    },
    "8": {
      "L": "When Asa heard these words, the prophecy of Azariah the son of Oded the prophet, he took courage and removed the abominable idols from all the land of Judah and Benjamin and from the cities that he had captured in the hill country of Ephraim. And he repaired the altar of the LORD that was in front of the vestibule of the house of the LORD.",
      "M": "When Asa heard these words and the prophecy of Azariah son of Oded, he took courage and removed the detestable idols from all of Judah and Benjamin and from the towns he had captured in the hill country of Ephraim. He also restored the LORD's altar in front of the temple portico.",
      "T": "The prophecy had the intended effect: Asa took courage. The word literally means he grasped strength; the prophet's word gave him what he needed to act. He extended the reform into the newly captured territory — the hill country of Ephraim that Abijah had taken from Jeroboam. And he repaired the altar of the LORD, possibly neglected or fallen into disrepair during the years of Rehoboam's unfaithfulness. The prophecy of a single unknown man drove the most comprehensive reform Judah had seen in generations."
    },
    "9": {
      "L": "And he gathered all Judah and Benjamin, and those from Ephraim, Manasseh, and Simeon who were residing with them, for great numbers had deserted to him from Israel when they saw that the LORD his God was with him.",
      "M": "He assembled all Judah and Benjamin, along with settlers from Ephraim, Manasseh, and Simeon who had come to live among them — for many had defected from Israel to Asa when they saw that the LORD his God was with him.",
      "T": "The gathering was pan-Israelite in spirit even if not in territory. From all three of Judah's tribes — and then from Ephraim, Manasseh, Simeon: northern tribes whose faithful members had been crossing the border to find legitimate worship ever since Jeroboam's expulsion of the Levites. They came because they saw that the LORD was with Asa. The divine presence is visible; it draws the faithful across political and tribal boundaries. What the covenant promises as blessing, the watching world recognizes."
    },
    "10": {
      "L": "They gathered at Jerusalem in the third month of the fifteenth year of the reign of Asa.",
      "M": "They assembled in Jerusalem in the third month of the fifteenth year of Asa's reign.",
      "T": "The third month — the month of the Feast of Weeks, Shavuot, the harvest festival fifty days after Passover. The gathering at Jerusalem for covenant renewal echoed Joshua 24, where Israel had assembled at Shechem to renew the covenant after the conquest. The timing is not incidental; the harvest season, when the land's productivity was most visible, was the moment chosen to publicly acknowledge the Giver of all harvests."
    },
    "11": {
      "L": "They sacrificed to the LORD on that day from the spoil that they had brought — seven hundred oxen and seven thousand sheep.",
      "M": "On that day they sacrificed to the LORD from the plunder they had brought — seven hundred cattle and seven thousand sheep.",
      "T": "The spoil of Zerah's defeat — the livestock carried back from Gerar — was transformed into sacrifice. What God gave in victory was returned to God in worship. Seven hundred oxen and seven thousand sheep: the abundance of the offering matched the abundance of the victory. The generosity of the sacrifice was the community's acknowledgment that everything they had, including the plunder, belonged to God."
    },
    "12": {
      "L": "And they entered into a covenant to seek the LORD, the God of their fathers, with all their heart and with all their soul.",
      "M": "They entered into a covenant to seek the LORD, the God of their ancestors, with all their heart and soul.",
      "T": "A covenant — formal, oath-bound, publicly enacted. Not a resolution but a legal commitment: we bind ourselves to seek the LORD with our whole being. 'All their heart and with all their soul' — the Shema's language (Deut 6:5), the words of total allegiance. The covenant renewal at Jerusalem in Asa's fifteenth year was Israel at its best: a people who had seen God fight for them, gathering to publicly commit themselves to him."
    },
    "13": {
      "L": "Whoever would not seek the LORD, the God of Israel, should be put to death, whether young or old, man or woman.",
      "M": "Anyone who refused to seek the LORD, the God of Israel, was to be put to death, whether young or old, man or woman.",
      "T": "The covenant had teeth. This is not casual commitment; it is the covenant-renewal structure of Deuteronomy 17:12 and 13:6-11, where public apostasy carried the death penalty. The community was constituting itself as a people under the LORD's sovereignty; those who publicly rejected that sovereignty placed themselves outside the covenant community and within the covenant's curse. The severity reflects the seriousness of what was being renewed: this was not a religious program but a national identity."
    },
    "14": {
      "L": "They swore an oath to the LORD with a loud voice and with shouting and with trumpets and with horns.",
      "M": "They swore their oath to the LORD with a loud voice, with shouting, and with trumpets and horns.",
      "T": "The oath was audible and exuberant: loud voices, shouting, the trumpet blasts of the priestly instruments, the ram's-horn blasts of the people. The covenant was sworn in full voice, publicly, before God and each other. This was not private religion; it was a national act performed with full ceremony and maximum sound. The LORD, who had come in fire to Solomon's temple, was now being acclaimed in sound by a people who had just seen him fight for them."
    },
    "15": {
      "L": "And all Judah rejoiced over the oath, for they had sworn with all their heart and sought him with their whole desire, and he was found by them, and the LORD gave them rest on every side.",
      "M": "All Judah rejoiced over the oath, for they swore it wholeheartedly, sought him eagerly, and he was found by them. The LORD gave them rest on every side.",
      "T": "Joy, wholehearted seeking, found — the sequence maps exactly onto Azariah's prophecy: if you seek him, he will be found by you. They sought with their whole desire: the Hebrew word naphash suggests a reaching-out of the whole self, the soul extending toward the object of its longing. And they found him. And the LORD gave rest on every side — the covenant blessing of shalom, the comprehensive peace that signifies right relationship with God expressed in the conditions of national life. This is Asa's peak moment."
    },
    "16": {
      "L": "Even Maacah, his mother, King Asa removed from being queen mother because she had made an abominable image for Asherah. Asa cut down her image, crushed it, and burned it at the brook Kidron.",
      "M": "King Asa even deposed his grandmother Maacah from her position as queen mother because she had made a repulsive image of Asherah. Asa cut down the image, crushed it, and burned it in the Kidron Valley.",
      "T": "The hardest act of the reform. Maacah — his grandmother, Rehoboam's favorite wife (2 Chr 11:21-22), the queen mother whose political influence in the court would have been enormous — had erected a repulsive idol to Asherah. Asa deposed her. He then destroyed the idol: cut it down, crushed it to fragments, burned it in the Kidron — the ravine outside Jerusalem where refuse was disposed. The reform was not selective; it did not spare family or politics. This is the Chronicler's example of the courage required by covenant faithfulness: the willingness to remove from honor those who dishonor the LORD, even when they are the people closest to you."
    },
    "17": {
      "L": "But the high places were not removed from Israel. Nevertheless the heart of Asa was wholly true all his days.",
      "M": "The high places were not eliminated from Israel. Yet Asa's heart remained fully devoted throughout his life.",
      "T": "The qualification the Chronicler cannot omit. The high places — the local shrines used for both legitimate and illegitimate worship — were not fully removed from Israel (probably meaning the northern kingdom, or more broadly throughout the land outside Judah proper). Asa's reform was comprehensive in Judah but not total across Israel. And yet — the Chronicler's pastoral judgment: Asa's heart was wholly true all his days. The incomplete work does not invalidate the sincere heart. The assessment is not 'he failed because the high places remained' but 'he was faithful even though the work was not finished.' God judges the heart."
    },
    "18": {
      "L": "And he brought into the house of God the sacred gifts of his father and his own sacred gifts, silver, gold, and vessels.",
      "M": "He brought into the house of God the sacred offerings of his father and his own dedicated gifts — silver, gold, and vessels.",
      "T": "The covenant renewal was followed by a treasury offering: Asa brought to the temple the things his father Abijah and he himself had vowed and set apart — silver, gold, vessels. The momentum of the revival expressed itself in generosity toward the house of the LORD. What had been accumulated in personal vows was now deposited in the common treasury of God's house."
    },
    "19": {
      "L": "And there was no more war until the thirty-fifth year of the reign of Asa.",
      "M": "There was no war until the thirty-fifth year of Asa's reign.",
      "T": "Twenty more years of peace — from the covenant renewal in year fifteen to the trouble that began in year thirty-six. Twenty years of rest, purchased by the faithfulness of a king who sought the LORD, deposed his grandmother, and brought the nation to covenant renewal. The peace was long. The test, when it came, would reveal whether the faithfulness of year fifteen had become the character of year thirty-six."
    }
  },
  "16": {
    "1": {
      "L": "In the thirty-sixth year of the reign of Asa, Baasha king of Israel went up against Judah and built Ramah, that he might permit no one to go out or come in to Asa king of Judah.",
      "M": "In the thirty-sixth year of Asa's reign, Baasha king of Israel attacked Judah and fortified Ramah to prevent any movement in or out of Judah.",
      "T": "The twenty years of peace ended when Baasha king of Israel — the northern kingdom's current ruler — fortified Ramah, the strategic city guarding the main road between the north and Jerusalem, only five miles from the capital. The blockade was economic and political: nothing could move to or from Judah without Baasha's permission. The test that Azariah's prophecy had anticipated was now present."
    },
    "2": {
      "L": "Then Asa took silver and gold from the treasuries of the house of the LORD and the king's house and sent them to Ben-hadad king of Syria, who lived in Damascus, saying,",
      "M": "Asa took silver and gold from the treasuries of the LORD's house and the palace and sent them to Ben-hadad king of Syria in Damascus, with this message:",
      "T": "The fateful decision. Asa faced a military threat and turned — not to the LORD in prayer, as he had done at Mareshah — but to the treasuries. He stripped the house of the LORD and the royal palace of their silver and gold to purchase an alliance. The contrast with Mareshah is total: there he had no strength and prayed; here he had wealth and spent it. What he carried in that moment to Ben-hadad was not just silver and gold — it was the evidence that his heart had drifted from the place it had been in year fifteen."
    },
    "3": {
      "L": "'There is a covenant between me and you, as there was between my father and your father. Behold, I am sending you silver and gold. Go, break your covenant with Baasha king of Israel, that he may withdraw from me.'",
      "M": "'Let there be a treaty between you and me, as between our fathers. I'm sending you silver and gold — break your alliance with Baasha king of Israel so he will withdraw from me.'",
      "T": "Asa's diplomacy: invoke an existing relationship, pay a price, buy a betrayal. He asked Ben-hadad to break his treaty with Baasha — to use Aram's military power on Judah's behalf in exchange for the treasure of the LORD's house. It was politically clever. It would work in the short term. And it was, according to Hanani the seer, the worst decision of Asa's reign."
    },
    "4": {
      "L": "And Ben-hadad listened to King Asa and sent the commanders of his armies against the cities of Israel, and they conquered Ijon, Dan, Abel-maim, and all the store cities of Naphtali.",
      "M": "Ben-hadad agreed with King Asa and sent his commanders against Israel's cities. They captured Ijon, Dan, Abel-maim, and all the store cities of Naphtali.",
      "T": "The strategy worked. Ben-hadad, bought by Asa's gold, attacked Israel's northern cities — forcing Baasha to abandon the Ramah project and pull his forces home to defend the north. Syria struck Ijon, Dan, Abel-maim, and the Naphtali storage network. From a military-political standpoint, it was a success. But what Asa had paid for it — and what it cost him spiritually — was about to be delivered by a prophet."
    },
    "5": {
      "L": "When Baasha heard of it, he stopped building Ramah and let his work cease.",
      "M": "When Baasha heard about it, he stopped fortifying Ramah and abandoned the project.",
      "T": "Baasha stopped. The blockade ended. The immediate threat was removed. Asa's plan had achieved its tactical objective. On the surface, the crisis was resolved. But Hanani the seer was already coming."
    },
    "6": {
      "L": "Then King Asa took all Judah, and they carried away the stones of Ramah and its timber, with which Baasha had been building, and with them he built Geba and Mizpah.",
      "M": "King Asa mobilized all Judah to haul away the stones and timber Baasha had used at Ramah. With these materials he fortified Geba and Mizpah.",
      "T": "Asa recycled Baasha's building materials to fortify his own positions — turning the enemy's construction into Judah's defenses. Geba guarded the northeastern approach to Jerusalem; Mizpah controlled the Benjamin plateau. Asa was strategically efficient. But he was building with silver he had taken from the house of the LORD and with materials from a project he ended by purchasing foreign help rather than calling on God."
    },
    "7": {
      "L": "At that time Hanani the seer came to Asa king of Judah and said to him, 'Because you relied on the king of Syria, and did not rely on the LORD your God, the army of the king of Syria has escaped you.'",
      "M": "At that time Hanani the seer came to King Asa and said: 'Because you relied on the king of Syria and not on the LORD your God, the Syrian army escaped your grasp.'",
      "T": "Hanani the seer — the prophetic voice God sends when kings make wrong decisions. His rebuke is structured around a single contrast: you relied on the king of Syria, not on the LORD your God. The word relied (shaan) is the same verb from chapter 13: Judah prevailed because they relied on the LORD. Here Asa does the opposite — and the consequence is named immediately: the Syrian army, which could have been Judah's prize, has escaped. If Asa had prayed instead of paid, he could have had two victories: Baasha's retreat and Ben-hadad's army. He got only one. What he purchased was inferior to what faith would have provided for free."
    },
    "8": {
      "L": "'Were not the Ethiopians and the Libyans a huge army with very many chariots and horsemen? Yet because you relied on the LORD, he delivered them into your hand.'",
      "M": "'Remember the Cushites and Libyans — weren't they a massive force with great numbers of chariots and cavalry? Yet because you relied on the LORD, he gave them into your hand.'",
      "T": "Hanani reaches back to Mareshah — the same battle where Asa had prayed the prayer of total dependence and won a victory against impossible odds. That was the standard: rely on the LORD, and he delivers the enemy. The contrast between then and now is devastating. Then: a million-man army, no human ally, total prayer, total victory. Now: a manageable crisis, a Syrian ally, a stripped treasury, and a missed opportunity. What Asa had in year fifteen, he lost in year thirty-six. The prophet holds the two moments side by side."
    },
    "9": {
      "L": "'For the eyes of the LORD run to and fro throughout the whole earth, to give strong support to those whose heart is blameless toward him. You have done foolishly in this matter, and from now on you will have wars.'",
      "M": "'The eyes of the LORD range throughout the earth to strengthen those whose hearts are fully committed to him. You have acted foolishly in this, and from now on you will face war.'",
      "T": "One of the great verses of Chronicles and of the entire Hebrew Bible. The eyes of the LORD run to and fro throughout the whole earth — not surveillance for punishment but active searching for those whose hearts are blameless toward him, so he can give them strong support. The omniscient God is looking for faith to reward. This is the theology that undergirds every battle prayer in Chronicles: call on the LORD, and his searching eyes find you, and he acts. But Asa did not call; he spent. And the verdict is 'foolishly' — the same word used for Rehoboam's scorpion speech. Folly is not ignorance; it is the choice of the inferior thing when the superior thing was available. From now on you will have wars: not because God is vindictive but because Asa has chosen the path that produces war rather than the path that produces rest."
    },
    "10": {
      "L": "Then Asa was angry with the seer and put him in the stocks in prison, for he was in a rage with him because of this. And Asa inflicted cruelties on some of the people at the same time.",
      "M": "Asa was furious with the seer and threw him in prison, for he was enraged at him over this. Asa also oppressed some of the people at that time.",
      "T": "The response to a true word badly received: imprisonment of the prophet and abuse of the people. Asa, who had deposed his grandmother for idolatry, now imprisoned a prophet for truth-telling. The hardness of heart that begins in the refusal to pray is confirmed in the refusal to hear. A king who will not call on God will not tolerate those who call on God's behalf. The violence against 'some of the people' is unexplained — perhaps officials who sided with Hanani, or those who questioned the Syrian alliance. The reign that had peaked at the covenant renewal of year fifteen had, by year thirty-six, become capable of persecuting prophets. The descent is not sudden; it is the accumulation of small decisions that moved the heart's orientation degree by degree."
    },
    "11": {
      "L": "The acts of Asa, from first to last, are written in the Book of the Kings of Judah and Israel.",
      "M": "The acts of Asa, from beginning to end, are recorded in the Book of the Kings of Judah and Israel.",
      "T": "The prophetic archive. Asa's full history — the reforms, the victories, the covenant renewal, the Syrian alliance, the imprisonment of Hanani — is all on record. The Chronicler cites his source and moves to the final chapter of Asa's reign."
    },
    "12": {
      "L": "In the thirty-ninth year of his reign Asa was diseased in his feet, and his disease became severe. Yet even in his disease he did not seek the LORD, but sought help from physicians.",
      "M": "In the thirty-ninth year of his reign, Asa developed a severe foot disease. Yet even in his illness he did not seek the LORD but turned only to physicians.",
      "T": "The final pattern repeated at the personal level: Asa becomes ill and does not seek the LORD. The same failure that characterized the Syrian alliance — choosing the human resource over the divine — now played out in his own body. The Chronicler is not condemning medicine; physicians were legitimate means of healing. The rebuke is about the direction of the heart: even in his disease he did not seek the LORD. The covenant theorem of verse 2 — if you seek him, he will be found by you — was still true, still available. Asa did not reach for it."
    },
    "13": {
      "L": "And Asa slept with his fathers, dying in the forty-first year of his reign.",
      "M": "Asa died in the forty-first year of his reign and rested with his ancestors.",
      "T": "Forty-one years — a long reign by any measure, longer than Solomon's, longer than David's. A reign that had begun with ten years of peace, won the greatest defensive victory in Judah's history, held the most comprehensive covenant renewal since Joshua, and then — in the final years — chose Syria over God, imprisoned a prophet, and faced his mortal illness without calling on the LORD. The ending is muted. There is no praise, no 'he did what was right.' He rested with his fathers. That is all."
    },
    "14": {
      "L": "They buried him in the tomb that he had cut for himself in the city of David. They laid him on a bier that had been filled with various kinds of spices prepared by the perfumer's art, and they made a very great fire in his honor.",
      "M": "They buried him in the tomb he had made for himself in the city of David. He was laid on a bed perfumed with various blended spices, and they lit a very great fire in his honor.",
      "T": "The state funeral: his own tomb, cut for himself — the preparation of a man who knew death was coming. A bed of spices prepared by expert hands. A great fire lit in honor — a royal cremation of spices and aromatics, not of the body but as a mark of honor. The Chronicler gives Asa's burial more dignity than his death deserved. The ceremony honored the king he had been; the silence of the surrounding verses honored the truth of how he had ended."
    }
  },
  "17": {
    "1": {
      "L": "Jehoshaphat his son reigned in his place and strengthened himself against Israel.",
      "M": "His son Jehoshaphat became king in his place and consolidated his position against Israel.",
      "T": "A new king and a new era. Jehoshaphat — whose name means 'the LORD judges' — stepped into the forty-one years his father had left and immediately moved to secure the northern border against Israel. 'Strengthened himself against Israel' means he fortified the defensive line between the two kingdoms, preventing the kind of incursion that Baasha had made in Asa's thirty-sixth year."
    },
    "2": {
      "L": "He placed forces in all the fortified cities of Judah and set garrisons in the land of Judah, and in the cities of Ephraim that Asa his father had captured.",
      "M": "He stationed troops in all Judah's fortified cities and placed garrisons throughout Judah and in the Ephraimite towns his father Asa had captured.",
      "T": "The military disposition covered both Judah's own fortified cities and the Ephraimite territory in the hill country north of Jerusalem that Abijah had captured and Asa had maintained. Jehoshaphat was not content to hold the heartland; he pushed the perimeter forward into the borderlands that provided a buffer against northern incursion."
    },
    "3": {
      "L": "The LORD was with Jehoshaphat, because he walked in the earlier ways of his father David and did not seek the Baals.",
      "M": "The LORD was with Jehoshaphat because he followed the earlier example of his ancestor David and did not seek the Baals.",
      "T": "The theological verdict is given immediately and unambiguously: the LORD was with Jehoshaphat. The reason: he walked in the first ways of his father David — the David of covenant faithfulness, the David of seeking God, the David who despite failures kept his heart oriented toward the LORD. And he did not seek the Baals — the fertility gods of Canaan who promised rain and harvest and were the constant temptation of agricultural Israel. Jehoshaphat began right."
    },
    "4": {
      "L": "But he sought the God of his father and walked in his commandments, and not in the ways of Israel.",
      "M": "He sought the God of his father and followed his commands, not the practices of Israel.",
      "T": "The positive and negative of his covenant loyalty: seeking the God of his father (David's God, the covenant God of Abraham and Moses), walking in his commandments (the Torah as the structured practice of covenant life), and deliberately not following the ways of the northern kingdom — the Jeroboam system of golden calves and unauthorized priesthood. Jehoshaphat's faithfulness was specific: he knew what Israel was doing and chose differently."
    },
    "5": {
      "L": "Therefore the LORD established the kingdom in his hand. And all Judah brought tribute to Jehoshaphat, and he had great riches and honor.",
      "M": "The LORD therefore established his rule firmly. All Judah brought him tribute, and he had great riches and honor.",
      "T": "The covenant equation runs as reliably as gravity: seek the LORD, the kingdom is established; faithfulness produces honor and wealth. All Judah brought tribute — a voluntary acknowledgment of legitimate royal authority, not tribute extracted by force but given by a people who recognized that their king was aligned with their God. Great riches and honor: the same pairing the Chronicler had used for Solomon (9:22). Jehoshaphat's faithfulness placed him in that succession."
    },
    "6": {
      "L": "His heart was courageous in the ways of the LORD. And furthermore, he took the high places and the Asherim out of Judah.",
      "M": "His heart was devoted to the LORD's ways. He also removed the high places and Asherah poles from Judah.",
      "T": "Courageous in the ways of the LORD — not just compliant but wholehearted, not just avoiding wrong but actively committed to right. And the courage expressed itself in reform: the high places and Asherim that Asa had not fully removed, Jehoshaphat continued clearing. Each faithful king took the reform one step further, none completing it entirely, but each making progress. The Chronicler notes this with quiet praise: he did not leave the work undone that was his to do."
    },
    "7": {
      "L": "In the third year of his reign he sent his officials Ben-hail, Obadiah, Zechariah, Nethanel, and Micaiah to teach in the cities of Judah;",
      "M": "In his third year he sent his officials — Ben-hail, Obadiah, Zechariah, Nethanel, and Micaiah — to teach in the towns of Judah.",
      "T": "The third year — not waiting until the kingdom was settled, but within the first years of his reign, Jehoshaphat launched the most ambitious educational program in Judah's royal history. He sent officials — the royal civil servants, the men of the court — to the cities of Judah not for taxation or military conscription but to teach. Five named officials dispatched across the kingdom with an educational mission."
    },
    "8": {
      "L": "and with them the Levites, Shemaiah, Nethaniah, Zebadiah, Asahel, Shemiramoth, Jehonathan, Adonijah, Tobijah, and Tob-adonijah; and with these Levites, the priests Elishama and Jehoram.",
      "M": "With them he sent Levites — Shemaiah, Nethaniah, Zebadiah, Asahel, Shemiramoth, Jehonathan, Adonijah, Tobijah, and Tob-adonijah — along with the priests Elishama and Jehoram.",
      "T": "The teaching team was comprehensive: royal officials, Levites, priests. This was not a partisan political message but a covenant education mission. The Levites held the traditional teaching office (Deut 33:10: 'They shall teach Jacob your rules and Israel your law'); the priests carried the authority of the sanctuary; the royal officials provided the administrative reach of the king. Together they constituted a mobile teaching faculty with royal authorization, priestly authority, and Levitical expertise."
    },
    "9": {
      "L": "And they taught in Judah, having the Book of the Law of the LORD with them. They went about through all the cities of Judah and taught among the people.",
      "M": "They taught throughout Judah, taking with them the Book of the Law of the LORD. They traveled to every town in Judah and instructed the people.",
      "T": "The Book of the Law — the Torah, the Mosaic covenant document — was the curriculum. They carried the actual scroll with them to every city in Judah, reading it to the people, explaining it, teaching its commands and its promises and its warnings. This is what Moses had envisioned (Deut 31:12-13: 'that they may hear and learn to fear the LORD your God, and be careful to do all the words of this law'). Jehoshaphat fulfilled Moses's vision by mobilizing a national teaching program. The land was saturated with the Word."
    },
    "10": {
      "L": "And the fear of the LORD fell upon all the kingdoms of the lands that were around Judah, and they did not make war against Jehoshaphat.",
      "M": "The terror of the LORD came upon all the surrounding kingdoms so that they did not make war against Jehoshaphat.",
      "T": "Peace as the fruit of faithfulness — but here it extends beyond Judah's borders. The fear of the LORD falling on surrounding nations is the Chronicler's recurring pattern: when God's people are faithful, the nations are impressed not by military strength but by the evident divine backing. Nations that would ordinarily test the edges of a new king's power held back. Jehoshaphat could teach the Torah to his people in peace because God's presence made the kingdom untouchable."
    },
    "11": {
      "L": "Some of the Philistines brought Jehoshaphat presents and silver for tribute, and the Arabians also brought him flocks: seven thousand seven hundred rams and seven thousand seven hundred male goats.",
      "M": "Some Philistines brought Jehoshaphat gifts and silver as tribute, and the Arabs brought him flocks — seven thousand seven hundred rams and seven thousand seven hundred male goats.",
      "T": "Tribute from the Philistines — Israel's ancient coastal adversaries — and from the Arabian tribes of the south and east. The number seven thousand seven hundred is symmetrical and perhaps symbolic, though the point is the direction of the flow: resources coming toward Jerusalem, nations acknowledging Judah's God-given prosperity. The kingdom that taught the Torah was also the kingdom that received tribute."
    },
    "12": {
      "L": "And Jehoshaphat grew steadily greater. He built in Judah fortresses and store cities,",
      "M": "Jehoshaphat continued to grow in power. He built fortresses and supply cities throughout Judah",
      "T": "Steadily greater — the Chronicler's steady-state description of blessing. Not a sudden windfall but the accumulation of divinely-backed growth over time. Jehoshaphat built the infrastructure of prosperity: fortresses for defense, store cities for surplus — the agricultural and military supply network of a well-organized kingdom."
    },
    "13": {
      "L": "and he had large supplies in the cities of Judah. He had soldiers, mighty men of valor, in Jerusalem.",
      "M": "and he kept large stores in Judah's cities, with mighty fighting men stationed in Jerusalem.",
      "T": "The wealth of the storehouses and the strength of the army in Jerusalem: both material and military abundance as the expression of the blessing that follows faithfulness. The city of the temple was also the city of the king's army. Sacred and political capital, worship and defense, housed in the same place."
    },
    "14": {
      "L": "These were their numbers by fathers' houses: Of Judah, the commanders of thousands: Adnah the commander, with three hundred thousand mighty men of valor;",
      "M": "This was the muster by their ancestral divisions: From Judah, the commanders of thousands — Adnah the commander with three hundred thousand valiant fighters;",
      "T": "The military census of Jehoshaphat's army, organized by tribe and commander. From Judah three divisions; from Benjamin two. The detail preserved by the Chronicler gives us not just numbers but names — the individual commanders who led the forces that God had built during the years of Jehoshaphat's faithfulness."
    },
    "15": {
      "L": "and next to him Jehohanan the commander, with two hundred and eighty thousand;",
      "M": "next to him Jehohanan the commander with two hundred and eighty thousand;",
      "T": "Jehohanan — 'the LORD is gracious' — leading two hundred and eighty thousand. The names of Jehoshaphat's commanders are names of covenant faithfulness: Adonijah means 'my Lord is the LORD'; Jehozabad means 'the LORD has endowed.' The naming conventions embedded in the army's leadership tell their own story about the culture of Jehoshaphat's court."
    },
    "16": {
      "L": "and next to him Amasiah the son of Zichri, a volunteer for the LORD, with two hundred thousand mighty men of valor.",
      "M": "and Amasiah son of Zichri, who had volunteered for the LORD's service, with two hundred thousand valiant fighters.",
      "T": "Amasiah — 'the LORD carries' or 'the LORD bears burdens' — son of Zichri, a volunteer for the LORD. This phrase is unique: not drafted, not obligated by birth or position, but a volunteer whose military service was a form of devotion to God. The army included men who served because they chose to, because they understood their military role as covenant faithfulness. Amasiah's two hundred thousand were, in a sense, the spiritual descendants of the men who had cried out at Zemaraim and Mareshah."
    },
    "17": {
      "L": "Of Benjamin: Eliada, a mighty man of valor, with two hundred thousand armed with bow and shield;",
      "M": "From Benjamin: the mighty Eliada with two hundred thousand archers and shield-bearers;",
      "T": "Benjamin's first division — the archer-and-shield combination that had characterized Benjamin's military tradition since the time of the judges (Judg 20:16: Benjamin's famous left-handed slingers). Eliada, 'God knows,' led the two hundred thousand."
    },
    "18": {
      "L": "and next to him Jehozabad, with a hundred and eighty thousand armed for war.",
      "M": "and Jehozabad with a hundred and eighty thousand equipped for war.",
      "T": "The total of Jehoshaphat's standing army from these five divisions alone: three hundred thousand plus two hundred eighty thousand plus two hundred thousand plus two hundred thousand plus one hundred eighty thousand — over one million, one hundred sixty thousand. If the numbers function as symbolic indicators of overwhelming strength, the point is clear: under Jehoshaphat's faithful rule, Judah was more militarily capable than at any point since Solomon. Faithfulness produced strength."
    },
    "19": {
      "L": "These were in the service of the king, besides those whom the king had put in the fortified cities throughout all Judah.",
      "M": "These served the king, in addition to those he had stationed in the fortified cities throughout Judah.",
      "T": "The Jerusalem garrison was only a part of the whole; the fortified cities throughout Judah held additional forces not counted in this census. The kingdom's military depth was substantial. Jehoshaphat had inherited Asa's defensive network and the Ephraimite cities; he had added to it, stocked it, manned it. The nation was at peace and prepared. The teaching mission and the military census together paint a portrait of a king who understood that faithfulness to God and responsible stewardship of his kingdom were not competing obligations but a single vocation."
    }
  },
  "18": {
    "1": {
      "L": "Now Jehoshaphat had great riches and honor, and he made a marriage alliance with Ahab.",
      "M": "Jehoshaphat had great wealth and honor, and he formed a marriage alliance with Ahab.",
      "T": "Three words that signal a turning point: made a marriage alliance with Ahab. Everything else in the verse — the riches, the honor, the blessing of Jehoshaphat's faithful reign — is there as the backdrop against which this decision stands out. Why would a prosperous, faithful, honored king align himself with the most notoriously faithless king in Israel? The Chronicler will let the Micaiah episode answer that question."
    },
    "2": {
      "L": "After some years he went down to Ahab in Samaria. And Ahab killed sheep and oxen in abundance for him and for the people who were with him, and induced him to go up against Ramoth-gilead.",
      "M": "Some years later he visited Ahab in Samaria, and Ahab slaughtered great numbers of sheep and cattle for him and his entourage. Then Ahab persuaded him to attack Ramoth-gilead.",
      "T": "The visit began with feasting — Ahab's hospitality was lavish, and the social debt created by shared table in the ancient world was real. Then the persuasion: join me in recovering Ramoth-gilead from the Arameans. Jehoshaphat, full of Ahab's meat and sitting in his house, was in the worst possible position to exercise independent judgment. The alliance marriage had already made them family; the feast had made them friends; the request came in that context. Jehoshaphat said yes — or something close to it."
    },
    "3": {
      "L": "Ahab king of Israel said to Jehoshaphat king of Judah, 'Will you go with me to Ramoth-gilead?' And he answered him, 'I am as you are, my people as your people. We will be with you in the battle.'",
      "M": "Ahab asked Jehoshaphat, 'Will you go with me to Ramoth-gilead?' He answered, 'I am with you, and my people are with your people — we will join you in battle.'",
      "T": "I am as you are — the language of the alliance marriage fully activated: our identities are merged, your cause is my cause, your army is my army. Jehoshaphat committed himself and Judah to Ahab's military campaign with a single sentence. The problem was not the politics; it was the theology. Ahab was the king who had murdered Naboth for his vineyard, who had built Baal temples at his Phoenician wife Jezebel's request, who would be condemned by Elijah as the most wicked king of the northern dynasty. To say 'I am as you are' to Ahab was to say a great deal more than Jehoshaphat intended."
    },
    "4": {
      "L": "And Jehoshaphat said to the king of Israel, 'Inquire first for the word of the LORD.'",
      "M": "Jehoshaphat added, 'But first, let's inquire for the word of the LORD.'",
      "T": "Even inside the alliance, even after committing his army, even at Ahab's feast — Jehoshaphat remembered. Inquire first for the word of the LORD. This is the reflex of a man who had taught the Torah across Judah, who had seen the miracle of Mareshah, who knew the covenant theorem. He was compromised in his alliance but not yet in his faith. Before the campaign begins, consult God. It is a late addition of wisdom to what was already a questionable commitment — but it is better than nothing, and it sets the stage for Micaiah."
    },
    "5": {
      "L": "So the king of Israel gathered the prophets together, four hundred men, and said to them, 'Shall we go to battle against Ramoth-gilead, or shall I refrain?' And they said, 'Go up, for God will give it into the hand of the king.'",
      "M": "The king of Israel assembled four hundred prophets and asked them: 'Should we go to battle against Ramoth-gilead or not?' They said: 'Go up — God will deliver it into the king's hand.'",
      "T": "Four hundred prophets — the court prophets of the northern kingdom, employed to speak what the king wanted to hear. They gave the right answer in four hundred voices: go up, God will give you victory. Unanimity in prophecy is not evidence of truth; it is often evidence of institutional pressure. Jehoshaphat, who had heard real prophets speak — Azariah, Hanani — heard four hundred say the same thing and was not satisfied."
    },
    "6": {
      "L": "But Jehoshaphat said, 'Is there not here another prophet of the LORD of whom we may inquire?'",
      "M": "But Jehoshaphat asked, 'Is there another prophet of the LORD here we could consult?'",
      "T": "Another prophet — Jehoshaphat was unconvinced. Perhaps the unanimity itself disturbed him; genuine prophets disagreed, debated, challenged kings. Perhaps he recognized the court prophets for what they were. Whatever the reason, he pushed past the four hundred to ask for one more voice, an independent voice, a voice that might say something other than what the king wanted to hear. This instinct for honest prophecy, in the middle of a questionable military alliance, was the best thing Jehoshaphat did that day."
    },
    "7": {
      "L": "And the king of Israel said to Jehoshaphat, 'There is yet one man by whom we may inquire of the LORD, Micaiah the son of Imlah; but I hate him, for he never prophesies good concerning me, but always evil.' And Jehoshaphat said, 'Let not the king say so.'",
      "M": "The king of Israel answered, 'There is one more — Micaiah son of Imlah — but I hate him because he never predicts anything good for me, only evil.' 'Don't say that,' Jehoshaphat replied.",
      "T": "I hate him because he never prophesies good concerning me — one of the most self-condemning statements in all of Kings and Chronicles. Ahab's criterion for evaluating a prophet was whether the prophet agreed with him. A prophet who consistently says what the king does not want to hear is, by definition, a reliable prophet. Ahab's hatred of Micaiah was his most telling confession: he knew who told the truth, and he hated the truth-teller. Jehoshaphat's gentle rebuke — 'don't say that' — recognized the absurdity. But Micaiah was sent for."
    },
    "8": {
      "L": "Then the king of Israel summoned an officer and said, 'Bring quickly Micaiah the son of Imlah.'",
      "M": "So the king of Israel called an officer and said, 'Bring Micaiah son of Imlah at once.'",
      "T": "The summons was issued. Micaiah, in whatever cell or village or holding place he occupied between royal interrogations, was fetched. The man Ahab hated was about to stand before two kings and tell the truth."
    },
    "9": {
      "L": "Now the king of Israel and Jehoshaphat the king of Judah were sitting on their thrones, arrayed in their robes, at the threshing floor at the entrance of the gate of Samaria, and all the prophets were prophesying before them.",
      "M": "The king of Israel and Jehoshaphat king of Judah were seated on their thrones in their royal robes at the threshing floor near Samaria's gate, with all the prophets prophesying before them.",
      "T": "The scene is carefully staged: two kings in their robes, on thrones, at the city gate — the place of public ceremony and legal decision in the ancient world. Four hundred prophets performing before them. It had the appearance of a proper covenant consultation: the king seeks the LORD's word before battle. But the prophets' unanimity and Jehoshaphat's unease had already exposed the hollow center of the performance."
    },
    "10": {
      "L": "And Zedekiah the son of Chenaanah made for himself horns of iron and said, 'Thus says the LORD, \"With these you shall push the Syrians until they are destroyed.\"'",
      "M": "Zedekiah son of Chenaanah had made iron horns for himself and said: 'This is what the LORD says: With these you will gore the Arameans until they are destroyed.'",
      "T": "Zedekiah — the most prominent of the four hundred — had prepared props: iron horns, the symbol of a charging bull, the emblem of irresistible military force. His prophecy was theatrical, confident, and wrong. The iron horns were a brilliant piece of prophetic theater and a complete lie. Zedekiah would face Micaiah's response and discover what true prophecy sounded like."
    },
    "11": {
      "L": "And all the prophets prophesied so and said, 'Go up to Ramoth-gilead and triumph; the LORD will give it into the hand of the king.'",
      "M": "All the other prophets agreed: 'March on Ramoth-gilead and be victorious — the LORD will hand it over to the king!'",
      "T": "The chorus was unanimous: victory, triumph, the LORD's hand delivering Ramoth-gilead. Four hundred voices saying the same thing. The institutional pressure on Micaiah to join them was enormous — prophets who broke the court consensus faced exactly the kind of imprisonment that Hanani had suffered under Asa. Micaiah knew what disagreement cost. He also knew what truth required."
    },
    "12": {
      "L": "And the messenger who went to summon Micaiah said to him, 'Behold, the words of the prophets with one accord are favorable to the king. Let your word be like the word of one of them, and speak favorably.'",
      "M": "The messenger who had summoned Micaiah told him: 'Look — all the prophets are speaking favorably to the king. Make sure your word agrees with theirs and be positive.'",
      "T": "The pressure was applied before Micaiah even entered the throne room. The messenger told him plainly: match the chorus, say the favorable thing. This was both a warning (don't make trouble) and an opportunity (you can make this easy on yourself). Micaiah's answer established everything that followed."
    },
    "13": {
      "L": "But Micaiah said, 'As the LORD lives, what my God says, that I will speak.'",
      "M": "Micaiah replied, 'As the LORD lives, I will speak only what my God tells me.'",
      "T": "As the LORD lives — the oath that invokes God's existence as the guarantor of the statement that follows. Micaiah's prophetic integrity was grounded not in courage as a personality trait but in the living reality of the God he served. He could not say what his God had not said; to do so would be to invoke God's name for a lie. The oath was also a commitment: whatever he was about to say, it would cost him — and he said it anyway."
    },
    "14": {
      "L": "And when he had come to the king, the king said to him, 'Micaiah, shall we go to Ramoth-gilead to battle, or shall I refrain?' And he answered, 'Go up and triumph; they will be given into your hand.'",
      "M": "When he appeared before the king, Ahab asked, 'Micaiah, should we march on Ramoth-gilead or hold back?' 'March on and win,' he answered. 'It will be handed over to you.'",
      "T": "Micaiah's first answer is the four hundred's answer — delivered with unmistakable sarcasm, in the exact words of the court prophets, in a tone that every reader can detect as false. He was not lying; he was parodying. The king had asked for a prophecy; Micaiah gave him the official prophecy, word for word, in a tone that made its emptiness audible. The king immediately recognized it for what it was."
    },
    "15": {
      "L": "But the king said to him, 'How many times shall I make you swear that you speak to me nothing but the truth in the name of the LORD?'",
      "M": "But the king said, 'How many times must I make you swear to tell me only the truth in the LORD's name?'",
      "T": "Ahab heard the irony and called it out: how many times do I have to extract an oath from you to get the truth? This is a remarkable exchange. The king who hated Micaiah because he always spoke evil recognized a false prophecy from Micaiah in the first sentence — because Ahab knew, instinctively, what Micaiah speaking truth sounded like. The king who rejected truth was also the king who could identify it. The tragedy of Ahab is this double knowledge: he knew truth from flattery, chose flattery anyway, and died for it."
    },
    "16": {
      "L": "And Micaiah said, 'I saw all Israel scattered on the mountains, as sheep that have no shepherd. And the LORD said, \"These have no master; let each return to his home in peace.\"'",
      "M": "Micaiah answered: 'I saw all Israel scattered over the mountains like sheep without a shepherd. The LORD said, \"They have no master — let each one go home in peace.\"'",
      "T": "The true oracle: all Israel scattered on the mountains, shepherdless. The image is ancient — Moses had prayed for a successor so Israel would not be 'like sheep without a shepherd' (Num 27:17); Ezekiel would later develop it in the great shepherd discourse (Ezek 34); Jesus would look at the crowds and feel compassion because they were 'like sheep without a shepherd' (Matt 9:36). Here the scattered sheep are Israel after Ahab's death. The king will not return; 'let each return to his home in peace' means there will be no king to return to. This is the prophecy that told Ahab his death. He heard it clearly."
    },
    "17": {
      "L": "And the king of Israel said to Jehoshaphat, 'Did I not tell you that he would not prophesy good concerning me, but evil?'",
      "M": "The king of Israel said to Jehoshaphat, 'Didn't I tell you? He never prophesies good about me, only disaster.'",
      "T": "Confirmed. Ahab's self-justifying complaint to Jehoshaphat was simply what he had said before the prophet arrived. But notice: Ahab did not say the prophecy was false. He did not challenge Micaiah's vision. He complained that it was unfavorable. The truth of the oracle was not in question; only its acceptability was. Ahab's response to true prophecy was not refutation but grievance."
    },
    "18": {
      "L": "And Micaiah said, 'Therefore hear the word of the LORD: I saw the LORD sitting on his throne, with all the host of heaven standing on his right hand and on his left.'",
      "M": "Micaiah continued: 'Then hear the word of the LORD. I saw the LORD enthroned, with all the heavenly host standing at his right and left.'",
      "T": "The heavenly throne room — the seat of all reality, the place from which all earthly events are governed. I saw the LORD sitting. This is the prophet's claim: not an opinion, not a political analysis, but a vision granted by God of the council in heaven. The heavenly host standing at his right and left: the divine council that we also see in Job 1-2 and Isaiah 6. Heaven is not distant from earth; it is the engine room from which earth's history is directed."
    },
    "19": {
      "L": "'And the LORD said, \"Who will entice Ahab the king of Israel, that he may go up and fall at Ramoth-gilead?\" And one said one thing, and another said another.'",
      "M": "'The LORD asked: \"Who will lure Ahab king of Israel into attacking Ramoth-gilead so he will fall there?\" Various suggestions were offered.'",
      "T": "The divine question is stark: who will bring about Ahab's death at Ramoth-gilead? The question does not cause the death; Ahab has already been sentenced by the blood of Naboth and the Baal temples. The question is how. The heavenly council offers strategies. God permits the discussion; the outcome is already determined. What Micaiah is seeing is not a negotiation with God but an account of how divine sovereignty works through secondary causes — including free choices, including deception."
    },
    "20": {
      "L": "'Then a spirit came forward and stood before the LORD, saying, \"I will entice him.\" And the LORD said to him, \"How?\"'",
      "M": "'Then a spirit came forward and stood before the LORD: \"I will entice him.\" The LORD asked: \"How?\"'",
      "T": "A spirit — not identified further, not named as good or evil at this point in the narrative. It volunteered. The LORD did not command; the spirit offered. The divine question 'How?' acknowledges the spirit's agency and invites the plan. The architecture of the vision is deliberately complex: God is sovereign, secondary agents have genuine initiative, and the outcome serves God's determined purpose."
    },
    "21": {
      "L": "'And it said, \"I will go out and be a lying spirit in the mouth of all his prophets.\" And he said, \"You will entice him, and you shall succeed. Go out and do so.\"'",
      "M": "'It said, \"I will become a lying spirit in the mouths of all his prophets.\" The LORD said: \"You will succeed in enticing him. Go and do it.\"'",
      "T": "A lying spirit in the mouths of all his prophets. The theological difficulty here is real, and the Chronicler does not smooth it over. The four hundred prophets who spoke with unified conviction were not simply wrong; they were operating under a deceptive spiritual influence that God permitted and authorized. This is not God lying — Micaiah is standing here at this moment telling the truth, which means truth and lie exist simultaneously in Ahab's court, and Ahab has chosen which to hear. The lying spirit is the natural consequence of a king who has habitually preferred false prophets to true ones: eventually, God allows the preference to become a trap. The man who will not hear truth is given over to believing lies."
    },
    "22": {
      "L": "'So now behold, the LORD has put a lying spirit in the mouth of these your prophets. The LORD has declared disaster for you.'",
      "M": "'So the LORD has put a lying spirit in the mouths of your prophets, and the LORD has decreed disaster for you.'",
      "T": "The verdict spoken plainly: the LORD has decreed disaster for you. Not 'might' or 'if' — decreed. The death of Ahab at Ramoth-gilead was the declared intention of the God of Israel. The four hundred prophets who said 'go up and triumph' were instruments of a divine judgment already rendered. Ahab had the opportunity to hear the truth from Micaiah; what he did with it was his choice, and it had already been made."
    },
    "23": {
      "L": "Then Zedekiah the son of Chenaanah came near and struck Micaiah on the cheek and said, 'Which way did the Spirit of the LORD go from me to speak to you?'",
      "M": "Zedekiah son of Chenaanah stepped forward and slapped Micaiah on the cheek, saying: 'Which way did the Spirit of the LORD go when he left me to speak to you?'",
      "T": "Zedekiah's response to the supernatural challenge of Micaiah's oracle was physical violence and a theological taunt: you claim the Spirit, but where did he go from me? He was asserting that he too had the Spirit — that Micaiah's vision did not trump his performance. The slap was an insult and a provocation, the response of a man who had been publicly exposed as a false prophet and could not answer the exposure with argument. Micaiah said nothing in reply to the slap. The oracle stood."
    },
    "24": {
      "L": "And Micaiah said, 'Behold, you shall see on that day when you go into an inner room to hide yourself.'",
      "M": "Micaiah replied: 'You will find out on the day you go into an inner room to hide.'",
      "T": "The inner room — the hiding place of a man fleeing for his life, the last refuge when armies are routing and there is nowhere else to go. Micaiah's counter-prophecy to Zedekiah was personal and specific: you will know the truth when you are cowering in a back room. The army's defeat would be the answer to Zedekiah's taunt. It would not be delivered in a debate; it would be delivered in a rout."
    },
    "25": {
      "L": "And the king of Israel said, 'Seize Micaiah and take him back to Amon the governor of the city and to Joash the king's son,",
      "M": "The king of Israel ordered: 'Arrest Micaiah and take him to Amon the city governor and Joash the king's son.",
      "T": "Imprisonment was the predictable response — the same response Asa had given to Hanani. Kings who reject unwelcome prophecy do not argue with prophets; they silence them. Micaiah was handed to the city governor and the king's son — civil and royal authority working together to neutralize the inconvenient voice."
    },
    "26": {
      "L": "and say, \"Thus says the king: Put this fellow in prison and feed him with meager rations of bread and water until I return in peace.\"'",
      "M": "'Tell them: \"The king's orders — put this man in prison and keep him on reduced bread and water until I return safely.\"'",
      "T": "Bread and water of affliction — the minimum ration, the prison diet that kept a man alive while making his imprisonment as unpleasant as possible. Ahab's phrase 'until I return in peace' was an unwitting prophecy of his own: he would not return. The imprisonment was the king's last act of power against the prophet before he went to his death."
    },
    "27": {
      "L": "And Micaiah said, 'If you return in peace, the LORD has not spoken by me.' And he said, 'Hear, all you peoples!'",
      "M": "Micaiah said: 'If you return safely, the LORD has not spoken through me.' Then he added: 'All you peoples — take note!'",
      "T": "Micaiah staked his prophetic credibility on the outcome — and in doing so, staked Ahab's life on it. If Ahab returns, Micaiah is a false prophet. If Micaiah is a true prophet, Ahab does not return. The last words — 'Hear, all you peoples!' — called the crowd, the soldiers, everyone present as witnesses to what had just been said. The prophecy was delivered publicly, on the record, before the battle. No one would be able to say they had not been warned."
    },
    "28": {
      "L": "So the king of Israel and Jehoshaphat the king of Judah went up to Ramoth-gilead.",
      "M": "So the king of Israel and Jehoshaphat king of Judah marched on Ramoth-gilead.",
      "T": "They went anyway. Micaiah's vision, Micaiah's personal oracle to Ahab, the oracle to Zedekiah — none of it stopped the campaign. Two kings, their combined armies, the four hundred prophets saying go up and triumph, and one prophet saying the LORD has decreed disaster — and they went up. This is the final statement about the will to self-deception: when a man has decided what he wants to do, the voice of truth, however clear, will not be heard."
    },
    "29": {
      "L": "The king of Israel said to Jehoshaphat, 'I will disguise myself and go into battle, but you wear your robes.' So the king of Israel disguised himself, and they went into battle.",
      "M": "The king of Israel told Jehoshaphat: 'I will disguise myself when we go into battle, but you wear your royal robes.' So the king of Israel disguised himself, and they went to fight.",
      "T": "Ahab's disguise: having dismissed the prophecy of his death, he took precautions against it. The irony is complete. He did not believe Micaiah — and he dressed to avoid being identified. He trusted the four hundred — and he hid. The disguise was simultaneously an act of unbelief (the prophecy is false) and belief (the prophecy might be true). He tried to outmaneuver the sovereign word of God with a change of clothes. Jehoshaphat, perhaps not understanding the danger to himself, wore his royal robes."
    },
    "30": {
      "L": "Now the king of Syria had commanded the captains of his chariots, 'Fight with neither small nor great, but only with the king of Israel.'",
      "M": "The king of Aram had ordered his chariot commanders: 'Don't fight with anyone — small or great — except the king of Israel.'",
      "T": "The order from Syria: everyone else is irrelevant; find and kill the king of Israel. Ben-hadad had his own intelligence about what this battle meant; kill Ahab and the campaign is over. The targeting order would prove providentially significant when Jehoshaphat, in his royal robes, was mistaken for Ahab."
    },
    "31": {
      "L": "As soon as the captains of the chariots saw Jehoshaphat, they said, 'It is the king of Israel.' So they turned to fight against him. And Jehoshaphat cried out, and the LORD helped him; God drew them away from him.",
      "M": "When the chariot commanders spotted Jehoshaphat, they said, 'That's the king of Israel!' and turned to attack him. Jehoshaphat cried out, and the LORD helped him — God drew the attackers away from him.",
      "T": "Jehoshaphat's royal robes — Ahab's 'protection' — became Jehoshaphat's mortal danger. The Syrian chariot commanders converged on the man in royal robes. Jehoshaphat cried out — the same verb used for the crying out at Zemaraim and Mareshah, the prayer in extremity. And the LORD helped him: God moved the Syrians away from him. Jehoshaphat's cry was answered; his alliance with Ahab had put him in a death trap, and the LORD extracted him from it. The pattern is consistent: the man who calls on the LORD in the moment of total need finds the LORD acting on his behalf."
    },
    "32": {
      "L": "When the captains of the chariots saw that it was not the king of Israel, they turned back from pursuing him.",
      "M": "When the chariot commanders realized he was not the king of Israel, they stopped pursuing him.",
      "T": "They turned back — God's intervention through the most natural of mechanisms: the commanders saw the face of the man they were chasing and recognized it wasn't Ahab. The salvation was ordinary and extraordinary simultaneously: the same eyes that God had opened to see the wrong man, God moved away from Jehoshaphat. The divine movement behind the human recognition."
    },
    "33": {
      "L": "But a certain man drew his bow at random and struck the king of Israel between the scale armor and the breastplate. Therefore he said to the driver of his chariot, 'Turn around and carry me out of the battle, for I am wounded.'",
      "M": "But someone drew his bow without any particular aim and shot the king of Israel between the joints of his armor. Ahab said to his chariot driver, 'Turn around and get me out of here — I've been wounded.'",
      "T": "At random — the Hebrew is l'tummo, literally 'in his simplicity,' in his innocence, without knowing what he was doing. The arrow that killed Ahab was shot by a man with no target, no plan, no knowledge that he was fulfilling prophecy. The random arrow found the gap between Ahab's armor pieces — the precise spot that only random chance could find. God's sovereignty worked through the accidental act of an anonymous soldier to fulfill a prophetic word spoken before the battle began. Ahab had disguised himself against identified attackers; he died from an arrow shot by a man who wasn't aiming at anyone."
    },
    "34": {
      "L": "And the battle continued escalating that day, and the king of Israel was propped up in his chariot facing the Syrians until evening. Then at sunset he died.",
      "M": "The battle grew more intense throughout the day. The king of Israel was propped up in his chariot facing the Arameans until evening, and at sunset he died.",
      "T": "Propped up in his chariot — mortally wounded, bleeding out, kept upright to prevent panic in the ranks, facing the enemy until the sun went down. Ahab died at the moment Micaiah had described: scattered like sheep, no shepherd, return home in peace. The stubborn courage of the dying king — holding his position in the chariot through a long afternoon's battle — is not celebrated by the Chronicler, but it is visible. A man who refused to hear the prophecy that promised him defeat died refusing to abandon the battlefield. The man who hid under a disguise died in full view of both armies, propped up in his chariot, visible to everyone, as the sun went down."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '2chronicles')
        merge_tier(existing, CHRONICLES2, tier_key)
        save(tier_dir, '2chronicles', existing)
    print('2 Chronicles 13–18 written.')

if __name__ == '__main__':
    main()
