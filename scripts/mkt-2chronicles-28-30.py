"""
MKT 2 Chronicles chapters 28–30 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-2chronicles-28-30.py

Content:
- Ch 28: Ahaz's apostate reign — Baal worship, child sacrifice in Valley of Hinnom,
         military defeats by Syria and Israel; Israel's merciful return of captives
         (prophet Oded); Ahaz's appeal to Assyria; deepening apostasy; death with
         dishonored burial outside royal tombs
- Ch 29: Hezekiah's reform — temple doors reopened in first month of his reign;
         Levites called to sanctify and cleanse the temple; Levitical roster;
         temple purification completed in 16 days; national atonement sacrifice;
         Davidic worship order restored with prophetic warrant; people's freewill
         burnt offerings overflow — all done suddenly
- Ch 30: Hezekiah's Passover — invitations sent to all Israel including Ephraim and
         Manasseh; held in second month by Num 9 exception; northern tribes mostly
         mock but some humble themselves; Jerusalem assembles for feast; altars removed;
         unclean northerners receive Hezekiah's intercessory prayer for pardon; feast
         extended another seven days; no such Passover since Solomon

Translation decisions carried forward from mkt-2chronicles-22-24.py:
- H3068 (יהוה): "LORD" in L/M; "the LORD" in T throughout.
- H430 (אֱלֹהִים): "God" throughout all tiers.
- H1285 (בְּרִית): "covenant" throughout (29:10).
- H7307 (רוּחַ): not prominent in these chapters.
- H2617 (חֶסֶד): not the primary term; 30:9 uses H2587 (חַנּוּן) and H7349 (רַחוּם) —
  the pair from Exod 34:6. L/M: "gracious and merciful"; T: notes the Exodus 34:6
  covenantal self-declaration of the divine name.

New decisions for chs 28–30:
- 28:3 child sacrifice in Valley of Hinnom: L/M render literally; T names the Molech
  practice and the Deuteronomic prohibition (Deut 18:10; Lev 18:21).
- 28:5-6 Syro-Ephraimite coalition of 734-732 BC: background to Isaiah 7 and the
  Immanuel prophecy. T notes the connection.
- 28:15 "city of palm trees" = Jericho: L/M keep the Hebrew idiom; T identifies the
  city and notes the covenant geography of returning captives to Israelite territory.
- 28:19 H6544 (פָּרַע / "made naked/let run wild"): L/M "brought Judah low" (contextual);
  T surfaces the shame-exposure metaphor — Ahaz uncovered and dishonored the nation.
- 28:21-23: Ahaz strips temple to pay Assyria, then when Assyria fails, worships Syrian
  gods — the double apostasy deepens. T traces the logic of substitution: failed
  human alliances drive him further from the covenant rather than back toward it.
- 29:3 "first year, first month": Hezekiah begins with the temple — the typological
  inversion of Ahaz, who ended by shutting it. T draws the contrast explicitly.
- 29:6 H6203 (עֹרֶף / "back of neck") in "turned their backs": same root as stiffnecked;
  Sinai rebellion echo. T surfaces this.
- 29:25 Davidic worship order has prophetic authorization, not merely royal tradition.
  The Chronicler insists: the commandment was from the LORD through his prophets.
  T draws the implication for the authority of Levitical music in temple worship.
- 29:34 Levites more upright than priests in consecrating themselves: one of the
  Chronicler's pointed defenses of Levitical dignity. T notes the inversion of
  typical priestly priority.
- 30:2 second-month Passover: invokes Num 9:9-11 (second Passover provision) as
  legitimate precedent applied to the whole nation. T explains the legal basis.
- 30:6 "children of Israel" address to Ephraim/Manasseh: pan-Israelite vision of
  Chronicles. The divided kingdom is a theological anomaly; Hezekiah's invitation
  is a covenant summons to what should never have been divided.
- 30:9 "gracious and merciful": Exod 34:6 echo — the LORD's own self-description after
  the golden calf. Hezekiah grounds his appeal to the north on the LORD's covenant
  character, not on political argument.
- 30:18-19 Hezekiah's prayer for the unclean: heart-orientation accepted in place of
  ritual purity. One of Chronicles' most theologically significant moments.
  T draws the full weight: God healed the people — responding to the prayer as prayer,
  not as a legal exception.
- 30:26 comparison to Solomon's time: the Chronicler's highest praise. T notes it will
  be echoed at Josiah's Passover (35:18) as part of the progressive covenant renewal arc.

Aspect notes:
- Ch 28: waw-consecutive imperfects dominate; pivotal theological statements use
  qal perfects. The delivered-into-hand formulas at vv5-6 mark divine causation.
- Ch 29: Hezekiah's speech uses imperatives and jussives; temple cleansing narrative
  uses waw-consecutive sequence. The song and worship at vv28-30 use participles
  (ongoing action) against the completed burnt offering (infinitive construct).
- Ch 30: proclamation letter (vv6-9) uses imperatives and jussives; festival narrative
  uses waw-consecutive; the final blessing (v27) uses waw-consecutive perfect for
  the prayer ascending to heaven.

OT intertextuality:
- 28:3: Topheth / Molech — Lev 18:21; Deut 18:10; Jer 7:31 (Jeremiah's Hinnom sermon)
- 28:5-6: Syro-Ephraimite coalition — historical backdrop of Isaiah 7's Immanuel sign
- 28:15: Jericho as site of return echoes Josh 2-6 covenant geography
- 29:6: "turned their backs" = stiffnecked language of Exod 32-34 and Num 14
- 29:10: covenant-making echoes Asa (15:12), Jehoshaphat (20:3), Joash (23:16)
- 29:25: Levitical music given by prophetic revelation — 1 Chr 25:1-6; same authority
  as the Mosaic law in the Chronicler's theological framework
- 30:9: "gracious and merciful" = Exod 34:6; the name declared after Israel's worst
  failure is the ground for Hezekiah's appeal to the northern remnant
- 30:26: comparison to Solomon — the gold standard of Chronicles; will recur at 35:18
  for Josiah's Passover, marking both as peaks of the covenant renewal arc
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
  "28": {
    "1": {
      "L": "Ahaz was twenty years old when he began to reign, and he reigned sixteen years in Jerusalem. And he did not do what was right in the sight of the LORD, as his father David had done.",
      "M": "Ahaz was twenty years old when he became king, and he reigned sixteen years in Jerusalem. He did not do what was right in the sight of the LORD as his ancestor David had done.",
      "T": "The opening formula announces failure before a single act is recorded. Every king of Judah is measured against David — the standard the Chronicler holds constant through every generation. Ahaz fails that measurement immediately. He is twenty years old at accession and will reign sixteen years — years the Chronicler will fill with an accelerating catalogue of apostasy. He is one of only two kings of Judah (with Manasseh) whose record is entirely negative in Chronicles. The formula 'did not do what was right' is not a mild reservation; in the Chronicler's theological vocabulary it is a death sentence on a reign."
    },
    "2": {
      "L": "For he walked in the ways of the kings of Israel, and also made molten images for the Baals.",
      "M": "He walked in the ways of the kings of Israel and even made cast images for the Baals.",
      "T": "The northern kingdom's kings are the Chronicler's negative benchmark — the line of Jeroboam's golden calves, the Omride alliance with Baal worship, the systematic dismantling of Mosaic covenant fidelity. For a Davidic king to walk in the ways of Israel's kings is to adopt the identity of the wrong dynasty. And then Ahaz exceeded even that: he made cast images for the Baals — physical manufactured objects of worship in the city of David and Solomon, in the capital that the temple dominated. The Baals (plural) signals not a single competing deity but a systematic alternative worship economy."
    },
    "3": {
      "L": "And he made offerings in the Valley of the Son of Hinnom, and burned his children in the fire, according to the abominations of the nations whom the LORD had driven out before the children of Israel.",
      "M": "He made offerings in the Valley of Ben-hinnom and burned his sons in the fire, according to the abominations of the nations the LORD had driven out before Israel.",
      "T": "The Valley of Ben-hinnom — later called Gehenna — was the place of the Topheth, where Molech was worshiped with child sacrifice. The Mosaic code had prohibited this with absolute clarity (Lev 18:21; Deut 18:10). The Chronicler says Ahaz burned his sons: plural, more than one child. The phrase 'according to the abominations of the nations whom the LORD had driven out' is a precise theological accusation: Israel had been brought into Canaan precisely because the nations had done these things; to do them now was to become what Israel was meant to replace. Jeremiah would later make the Hinnom valley the center of his most devastating sermon (Jer 7:31), naming it the place that defines the depth to which Israel had fallen."
    },
    "4": {
      "L": "And he sacrificed and burned incense on the high places and on the hills and under every green tree.",
      "M": "He sacrificed and burned incense on the high places, on the hills, and under every green tree.",
      "T": "High places, hills, green trees — the full catalogue of syncretistic worship sites that the Deuteronomic code demanded be destroyed (Deut 12:2-3). Each location represents a different modality of Canaanite religious geography: the bamah (high place) as a formalized worship site, the hilltops as sky-deity worship locations, the green trees as fertility cult shrines. Ahaz did not merely permit these; he personally participated. The king who was supposed to centralize worship at Jerusalem had instead populated the entire landscape of Judah with competing altars."
    },
    "5": {
      "L": "Therefore the LORD his God gave him into the hand of the king of Syria, and they defeated him and took from him a great multitude captive and brought them to Damascus. He was also given into the hand of the king of Israel, who defeated him with great slaughter.",
      "M": "Therefore the LORD his God handed him over to the king of Syria, who defeated him and carried off a great number of captives to Damascus. He was also handed over to the king of Israel, who inflicted a great slaughter on him.",
      "T": "The delivered-into-hand formula is the Chronicler's signature for covenant punishment. God himself gave Ahaz to his enemies — not as an accident of military history but as direct divine action. The Syro-Ephraimite coalition of 734-732 BC (the historical background for Isaiah 7) here becomes the instrument of the LORD's judgment. The same Isaiah who brought Ahaz the Immanuel promise in that crisis (Isa 7:14) did so because Ahaz refused to trust the LORD; what Chronicles records is the covenant mechanism that made the crisis necessary. Both Syria and Israel were used: the northern kingdom, itself under judgment, was permitted to become the instrument of judgment against its southern sibling."
    },
    "6": {
      "L": "For Pekah the son of Remaliah killed 120,000 from Judah in one day, all valiant men, because they had forsaken the LORD, the God of their fathers.",
      "M": "Pekah son of Remaliah killed 120,000 in Judah in a single day — all valiant men — because they had forsaken the LORD, the God of their fathers.",
      "T": "One hundred twenty thousand valiant men in one day: the scale of the defeat is almost incomprehensible. The Chronicler uses it to establish the principle explicitly — 'because they had forsaken the LORD.' The military catastrophe was not the result of inferior strategy, inferior numbers, or inferior weapons. It was the result of an inferior relationship with the God who determines outcomes. The same principle that had given Asa victory over a vast Cushite army with a smaller Judean force (ch 14) here operated in reverse. The forsaking of the LORD did not merely fail to help; it actively handed the battle to the enemy."
    },
    "7": {
      "L": "And Zichri, a mighty man of Ephraim, killed Maaseiah the king's son, and Azrikam the commander of the palace, and Elkanah who was next to the king.",
      "M": "Zichri, a warrior of Ephraim, killed Maaseiah the king's son, Azrikam the palace commander, and Elkanah who was second to the king.",
      "T": "The Chronicler gives names to the dead: the king's son, the palace commander, the second-in-command. These were not anonymous casualties but the specific human infrastructure of Ahaz's court — the next generation of the royal house, the men who ran the machinery of government. Zichri, an Ephraimite warrior, cut the top off Judah's leadership in a single engagement. The dynasty survived only because Ahaz himself was not killed; but the men who stood nearest to the throne and might have been kings or counselors after him were gone."
    },
    "8": {
      "L": "And the people of Israel took captive 200,000 from their brothers — women, sons, and daughters — and also took away much spoil, and brought the spoil to Samaria.",
      "M": "The people of Israel took 200,000 captives from their fellow Israelites — women, sons, and daughters — along with a great amount of plunder, and brought them to Samaria.",
      "T": "Two hundred thousand people — a catastrophic human loss, and the Chronicler notes the most painful dimension: these were brothers. The northern Israelites carried into slavery men and women who shared with them the covenant at Sinai, the calling from the God of Abraham, Isaac, and Jacob. The Chronicler describes them as 'brothers' to make the moral point that Israel was enslaving Israel — a violation of the covenant solidarity that was supposed to bind the twelve tribes regardless of the political rupture. The spoil that followed the captives northward was everything Judah had accumulated under more faithful kings, now stripped away."
    },
    "9": {
      "L": "But a prophet of the LORD was there, whose name was Oded, and he went out before the army that came to Samaria and said to them, 'Behold, because the LORD, the God of your fathers, was angry with Judah, he gave them into your hand, but you have killed them in a rage that has reached up to heaven.'",
      "M": "But there was a prophet of the LORD there named Oded, who went out to meet the army returning to Samaria and said to them: 'Look — the LORD, the God of your fathers, was angry with Judah and handed them over to you. But you have slaughtered them in a fury that has reached up to heaven.'",
      "T": "Oded is one of the Bible's most striking minor figures: a prophet in the northern kingdom who confronts his own victorious army at the moment of its greatest triumph. His argument is theologically sophisticated. He does not dispute the military facts; he explains them — the LORD was angry with Judah, so he gave them to you. He acknowledges divine causation. But then he drives the wedge: you exceeded your commission. God used you to punish Judah; you did not merely punish, you massacred. The rage that drove the killing 'reached up to heaven' — the standard biblical idiom for a cry or an act so extreme that it demands divine attention and response. The victors had crossed the line between instrument of judgment and authors of sin."
    },
    "10": {
      "L": "'And now you intend to subjugate the children of Judah and Jerusalem for male and female slaves to you: but are there not with you, even with you, sins against the LORD your God?'",
      "M": "'And now you are planning to make the people of Judah and Jerusalem your male and female slaves — but are you yourselves without sin against the LORD your God?'",
      "T": "The rhetorical question cuts to the center: before you enslave your brothers for their sin, examine your own account before God. The northern kingdom had its own catalogue of covenant violations — Jeroboam's calves, the Baal worship introduced by Ahab and Jezebel, the persistent rejection of the Mosaic covenant structures. Oded is not making a relativistic argument ('everyone sins'); he is making a covenant argument: those who stand under the same obligation have no standing to permanently subjugate those who have violated it alongside them. The enslavement of fellow Israelites — who shared the covenant, the patriarchal inheritance, the Exodus — was itself a sin that would compound the north's already-heavy account."
    },
    "11": {
      "L": "'Now hear me, and deliver the captives again whom you have taken captive from your brothers, for the fierce wrath of the LORD is upon you.'",
      "M": "'Now listen to me: return the captives you have taken from your brothers, for the fierce anger of the LORD is upon you.'",
      "T": "The command is direct and the threat is explicit: the LORD's fierce anger is already upon the north for what has been done. Oded does not ask the army to consider its feelings about the captives; he tells them what they must do and what is at stake if they do not. The return of the captives is not an act of magnanimity but of covenant obedience — and a recognition that you cannot claim to have served as God's instrument of judgment and then continue to exploit those you judged beyond what God authorized."
    },
    "12": {
      "L": "Then certain of the chiefs of the men of Ephraim — Azariah the son of Johanan, Berechiah the son of Meshillemoth, and Jehizkiah the son of Shallum, and Amasa the son of Hadlai — stood up against those who were coming from the war.",
      "M": "Some of the leading men of Ephraim — Azariah son of Johanan, Berechiah son of Meshillemoth, Jehizkiah son of Shallum, and Amasa son of Hadlai — rose up against those returning from the battle.",
      "T": "Four named leaders of Ephraim blocked the returning army at the gates of Samaria. The Chronicler gives their names because they deserve to be remembered — men in a northern kingdom that had largely abandoned the covenant who responded to a prophet's word with immediate action. Their intervention demonstrates that the prophetic tradition retained moral authority even in the apostate north: when Oded spoke, men of standing listened and acted. They did not wait for the king of Israel to order the captives' release; they stood against the army themselves."
    },
    "13": {
      "L": "And said to them, 'You shall not bring the captives in here, for you intend to bring upon us guilt against the LORD in addition to our sins and our guilt; for our trespass is great, and there is fierce wrath against Israel.'",
      "M": "They said, 'You must not bring the captives here. You would add guilt against the LORD to our sins and our existing guilt — our trespass is already great, and fierce wrath is already against Israel.'",
      "T": "The four chiefs make Oded's argument in concrete terms: our guilt account before the LORD is already full. Bringing these captives in to enslave them would be to add a new and specific sin on top of an existing mountain of covenant violation. The phrase 'fierce wrath is against Israel' shows that the north understood itself to be under divine judgment — not from the outside but from within. They were blocking their own army not from humanitarian sentiment but from covenant self-awareness: we cannot afford this sin."
    },
    "14": {
      "L": "So the armed men left the captives and the spoil before the princes and all the congregation.",
      "M": "So the armed soldiers released the captives and handed the plunder over to the officials and the whole assembly.",
      "T": "The army complied. An armed victorious force, carrying two hundred thousand captives and great spoil, stood down because four civic leaders invoked a prophet's word. This is one of the genuinely surprising moments in the Ahaz narrative — the goodness that appeared at Samaria while Ahaz was making alliances with Assyria and setting up Baal altars in Jerusalem. The response was not universal across the north; these four leaders, these princes, acted. But they acted, and the army listened. The captives were released."
    },
    "15": {
      "L": "And the men who were called by name rose up and took the captives, and from the spoil they clothed all who were naked among them, and arrayed them and shod them and gave them food and drink and anointed them, and all the feeble they carried on donkeys, and brought them to Jericho, the city of palm trees, to their brothers. Then they returned to Samaria.",
      "M": "Then the men designated by name rose and took charge of the captives. From the spoil they clothed everyone who was naked, gave them sandals, provided food and drink, anointed them, and carried all the weak on donkeys. They brought them to Jericho, the City of Palms, to their kinsmen. Then they returned to Samaria.",
      "T": "What the four leaders organized was not merely a release but a restoration: they clothed the naked from the spoil, shod the barefoot, fed the hungry, gave water to the thirsty, anointed the wounded, and carried those too weak to walk on donkeys. The care described is comprehensive and deliberate — the complete reversal of the condition of captivity. And the destination was Jericho, the first city of Israel's covenant possession in the promised land, the place where Joshua's conquest began (Josh 2-6). To return Judean captives to Jericho was to return them to Israelite covenant territory. The city of palm trees, on the Jordan plain, was the gateway back. After delivering them there, the four leaders and their men returned to Samaria — unnamed rescuers who appear for a single episode and disappear, their act preserved only in Chronicles."
    },
    "16": {
      "L": "At that time King Ahaz sent to the kings of Assyria to help him.",
      "M": "At that time King Ahaz sent to the kings of Assyria for help.",
      "T": "The juxtaposition is devastating. While men of Ephraim were clothing Judean captives and carrying the weak to Jericho on donkeys — while the north was enacting mercy — Ahaz was writing to Assyria. His response to military disaster was not repentance toward the LORD but alliance with the dominant imperial power. Isaiah had explicitly told him to trust the LORD and not to send to Assyria (Isa 7:4-9); Ahaz's letter to Tiglath-pileser was the refusal of the prophet's counsel in concrete political form. The appeal to Assyria that follows produces not rescue but further degradation."
    },
    "17": {
      "L": "For again the Edomites had come and smitten Judah and carried away captives.",
      "M": "For the Edomites had come again, attacked Judah, and carried off captives.",
      "T": "Edom strikes again — the traditional enemy on the southern flank. The word 'again' signals that this was not a new threat but a recurring one, a sign of Judah's weakening strategic position. Edom had been subdued under Jehoshaphat and earlier kings; now they raided Judah's borders and took captives freely. The multiple simultaneous threats — Syria from the north, Israel from the north, Edom from the south, Philistia from the west (v18) — picture a Judah in covenant collapse, abandoned by the LORD on every frontier simultaneously."
    },
    "18": {
      "L": "The Philistines also had made raids on the cities of the Shephelah and the Negeb of Judah, and had taken Beth-shemesh, Aijalon, Gederoth, Soco with its villages, Timnah with its villages, and Gimzo with its villages. And they settled there.",
      "M": "The Philistines had also raided the cities of the Shephelah and the Negeb of Judah, capturing Beth-shemesh, Aijalon, Gederoth, Soco with its villages, Timnah with its villages, and Gimzo with its villages — and they settled in them.",
      "T": "The Philistine penetration into the Shephelah — the lowland buffer zone between the coastal plain and the Judean hill country — was strategically catastrophic. Beth-shemesh, Aijalon, and Timnah were towns that David had secured; the Chronicler's list of captured cities reads like a reversal of the Davidic conquests. 'They settled there' is the final phrase: these were not raids but occupations. Judah was not merely losing battles; it was losing territory permanently. What the covenant faithfulness of earlier kings had won, Ahaz's covenant violation was forfeiting city by city."
    },
    "19": {
      "L": "For the LORD brought Judah low because of Ahaz king of Judah, for he had brought Judah to ruin and acted most unfaithfully against the LORD.",
      "M": "For the LORD humbled Judah because of King Ahaz, who had brought Judah low and had been utterly faithless to the LORD.",
      "T": "The Chronicler names the king as cause. It was Ahaz — not the enemies, not the military situation, not strategic geography — who brought Judah low. The verb pari' (let loose, strip bare, expose) carries the shame-language of the honor-shame world: Ahaz had uncovered Judah, stripped away its covenantal covering, exposed it to enemies on every side by removing the LORD's protection through faithlessness. The losses to Syria, Israel, Edom, and Philistia were not four separate military problems; they were one theological problem displayed on four fronts."
    },
    "20": {
      "L": "And Tiglath-pileser king of Assyria came to him and distressed him instead of strengthening him.",
      "M": "Tiglath-pileser king of Assyria came to him — but he oppressed him rather than helping him.",
      "T": "The Assyrian king came — but as an oppressor, not an ally. Ahaz had paid Tiglath-pileser with silver and gold stripped from the temple and his own treasury (2 Kgs 16:8); the Assyrian came, took the money, and gave Ahaz not relief but increased pressure. This is the logic of every failed human alliance in Chronicles: the help bought from imperial power costs more than it delivers and leaves the buyer weaker, not stronger. Ahaz had bypassed the LORD in favor of Assyria; Assyria took what was offered and gave distress in return."
    },
    "21": {
      "L": "For Ahaz took away a portion from the house of the LORD and from the house of the king and from the princes, and gave tribute to the king of Assyria; but it did not help him.",
      "M": "For Ahaz had stripped a portion from the LORD's house, from the royal palace, and from the officials, and paid tribute to the king of Assyria — but it brought no help.",
      "T": "Ahaz plundered three treasuries to pay Assyria: the temple (the house of the LORD), the palace (the king's house), and the nobles' private wealth. He stripped the sacred, the royal, and the civic simultaneously. The contrast with David and Solomon, who poured their personal wealth into the house of God, is the inverse image of covenant generosity: what the faithful brought to God's house, the unfaithful king took from it to give to a pagan king. And even on its own transactional terms — as a political investment — it failed. The tribute bought nothing."
    },
    "22": {
      "L": "In the time of his distress he became yet more unfaithful to the LORD — this is that King Ahaz.",
      "M": "In the time of his distress he became even more unfaithful to the LORD. This was King Ahaz.",
      "T": "The phrase 'this is that King Ahaz' is the Chronicler's rhetorical marker of infamy — pointing to Ahaz as the paradigm case of a truth about human nature under covenant pressure: distress, when met without the LORD, drives people not back toward him but further away. Every failed alliance produced not repentance but a new attempt at human solution. The accumulating disasters of Ahaz's reign — Syria, Israel, Edom, Philistia, Assyria — each one a covenantal signal — produced no reversal. In the time when suffering might have produced return, Ahaz trespassed more. The Chronicler's epitaph — this is that King Ahaz — is final."
    },
    "23": {
      "L": "For he sacrificed to the gods of Damascus that had defeated him and said, 'Because the gods of the kings of Syria helped them, I will sacrifice to them, that they may help me.' But they were the ruin of him and of all Israel.",
      "M": "He sacrificed to the gods of Damascus that had struck him down, reasoning that since the gods of the kings of Syria had helped the Syrians, he would sacrifice to them so they would help him too. But they became his ruin and the ruin of all Israel.",
      "T": "The theological logic of Ahaz's final apostasy is stated and exposed. He reasoned empirically: Syria defeated me; Syria's gods helped them; therefore I should worship Syria's gods. It is the logic of the uncommitted heart — you worship whoever seems to be winning. But the premise was false. Syria's gods had not defeated Ahaz; the LORD had, using Syria as an instrument (v5). Ahaz misread the mechanism of his own punishment and drew the precisely wrong conclusion. Worshiping the instrument of the LORD's judgment as though it were the cause of it, he added theological treason to military defeat. They became his ruin and the ruin of all Israel — the pan-Israelite dimension of a Judean king's apostasy: one king's spiritual logic has consequences that extend to the whole covenant people."
    },
    "24": {
      "L": "And Ahaz gathered together the vessels of the house of God and cut in pieces the vessels of the house of God, and shut the doors of the house of the LORD. And he made himself altars in every corner of Jerusalem.",
      "M": "Ahaz collected the vessels of the house of God, smashed them, shut the doors of the LORD's house, and set up altars in every corner of Jerusalem.",
      "T": "The desecration moved from worship to destruction: gathering the sacred vessels to break them was not merely sacrilege but a deliberate act of dismantling. The verb cut in pieces is used elsewhere of idols being broken; Ahaz applied it to the holy vessels of the temple. Then the doors were shut — the physical closing of the LORD's house, the point at which what Hezekiah will reverse in his first month (29:3) reaches its nadir. And in every corner of Jerusalem — Ahaz filled the capital of the Davidic covenant with competing altars, a systematic religious terraforming of the city that was meant to be the place where the LORD's name dwelt."
    },
    "25": {
      "L": "And in every several city of Judah he made high places to burn incense to other gods, and provoked the LORD, the God of his fathers, to anger.",
      "M": "In every city of Judah he set up high places to burn incense to other gods, provoking the LORD, the God of his fathers, to anger.",
      "T": "The destruction spread from Jerusalem to the entire land. Every city in Judah received a high place — a permanent installation of alternative worship. Ahaz was not merely personally apostate; he was constructing an infrastructure of idolatry that would outlast his reign. Many of these high places would still be standing when Hezekiah and Josiah undertook their reforms. The phrase 'God of his fathers' is the Chronicler's reminder that the God being provoked was not abstract or distant but the specific God who had been faithful to David, Solomon, and the dynasty — the God who had preserved Joash in the temple for six years and restored the covenant through Jehoiada. This was not ignorant paganism; it was chosen rejection."
    },
    "26": {
      "L": "Now the rest of his acts and all his ways, from first to last, behold, they are written in the Book of the Kings of Judah and Israel.",
      "M": "The rest of his acts and all his ways, from beginning to end, are recorded in the Book of the Kings of Judah and Israel.",
      "T": "The Chronicler closes Ahaz's reign with the standard archival reference and nothing more. No achievement is mentioned, no moment of the reign is singled out for praise, no warrior honored, no building project noted. For every good king, the Chronicler's closing summary names accomplishments; for Ahaz, the archive reference stands alone. The reign that opened with a failure to match David closed without a single positive notation. What the Book of Kings records about Ahaz is available to those who want more detail; what the Chronicler preserves is the theological verdict."
    },
    "27": {
      "L": "And Ahaz slept with his fathers, and they buried him in the city of Jerusalem; but they did not bring him into the tombs of the kings of Israel. And Hezekiah his son reigned in his place.",
      "M": "Ahaz rested with his ancestors and was buried in Jerusalem, but he was not placed in the tombs of the kings of Israel. His son Hezekiah succeeded him.",
      "T": "Buried in the city but not in the royal tombs: the same dishonor that Joash received (24:25) and that Jehoram had received before him (21:20). The dynasty acknowledged his death and his place in the family line; the tombs withheld their honor. After the child sacrifices, the Baal altars, the broken vessels, the shut temple doors, and the altars in every corner of Jerusalem, Ahaz was interred as a king who had forfeited the honors due to David's heirs. Hezekiah his son reigned in his place: the dynasty continued. The covenant would not be broken by one faithless king."
    }
  },
  "29": {
    "1": {
      "L": "Hezekiah began to reign when he was twenty-five years old, and he reigned twenty-nine years in Jerusalem. And his mother's name was Abijah the daughter of Zechariah.",
      "M": "Hezekiah was twenty-five years old when he became king and reigned twenty-nine years in Jerusalem. His mother was Abijah daughter of Zechariah.",
      "T": "The contrast begins with the opening verse. Ahaz's mother was never named in Chronicles — the Chronicler withheld even that honor from his record. Hezekiah's mother is named: Abijah, daughter of Zechariah. The name Abijah means 'the LORD is my father' — a covenant name given by parents who still lived in the vocabulary of faithfulness. After the sixteen years of Ahaz's reign, the reader is ready for a king whose very maternal heritage signals return."
    },
    "2": {
      "L": "And he did that which was right in the sight of the LORD, according to all that David his father had done.",
      "M": "He did what was right in the sight of the LORD, just as his ancestor David had done.",
      "T": "The Davidic standard that Ahaz had failed, Hezekiah fulfills — without qualification, without the limiting clause 'all the days of the priest' that had qualified Joash's praise. What follows in chapters 29-32 is the Chronicler's most expansive account of any single king's reform, matching Josiah in length and exceeding it in the scope of covenant restoration. The declaration that Hezekiah did 'according to all that David had done' is the highest commendation the Chronicler can give."
    },
    "3": {
      "L": "He in the first year of his reign, in the first month, opened the doors of the house of the LORD, and repaired them.",
      "M": "In the first year of his reign, in the first month, he opened the doors of the LORD's house and repaired them.",
      "T": "First year, first month, first act: the temple. What Ahaz had closed — shut deliberately, as a theological statement of rejection — Hezekiah opened immediately, as a theological statement of return. The doors are not merely architectural features; they are the boundary between the LORD's presence and its denial. Ahaz's closing of the doors was the culmination of his reign; Hezekiah's opening of them is the inauguration of his. The repair that followed was not cosmetic: sixteen years of neglect, deliberate damage by Athaliah's sons (24:7) compounded by Ahaz's active plundering, had left the building in genuine disrepair. Hezekiah would not simply unlock the doors and resume; he would rebuild the entire worship system from the foundation."
    },
    "4": {
      "L": "And he brought in the priests and the Levites, and gathered them together into the east street.",
      "M": "He assembled the priests and Levites and gathered them in the open square on the east side.",
      "T": "The first meeting of the new reign was not with the political officers or military commanders but with the priests and Levites — the religious personnel whose entire purpose was the maintenance of the LORD's house and its worship. Hezekiah understood the priority. The east square was the large open area between the eastern gate and the temple complex itself — public, accessible, able to hold the gathered religious leadership of the nation. He summoned them not with a written order but in person, demonstrating that what was about to happen was not delegated bureaucratic business but the king's own priority."
    },
    "5": {
      "L": "And said to them, 'Hear me, O Levites! Now consecrate yourselves, and consecrate the house of the LORD, the God of your fathers, and carry out the filthiness from the holy place.'",
      "M": "He said to them: 'Listen to me, O Levites! Consecrate yourselves now, and consecrate the house of the LORD, the God of your ancestors. Remove the filth from the holy place.'",
      "T": "The address is to the Levites specifically — not the priests first, but the Levites, whose role in the cleansing would be primary. The speech contains three imperatives: consecrate yourselves, consecrate the house, remove the filth. The order matters: personal consecration precedes service, personal service precedes institutional renewal. You cannot carry holy work to God's house while remaining unholy yourself; the external cleansing flows from internal consecration. The 'filth' in the holy place was both ritual — the defilement left by years of neglect and misuse — and theological: the presence of the wrong things in the wrong place, the sacred vessels broken and the Baal-apparatus installed."
    },
    "6": {
      "L": "For our fathers have trespassed and done what was evil in the eyes of the LORD our God, and have forsaken him, and have turned away their faces from the dwelling of the LORD, and turned their backs.",
      "M": "For our fathers were unfaithful and did what was evil in the sight of the LORD our God. They forsook him, turned their faces away from the LORD's dwelling, and turned their backs on him.",
      "T": "Hezekiah does not distance himself from the failure. He says 'our fathers' — not Ahaz's error but the pattern of a generation, and a pattern in which the current Levites and priests had participated by their silence and inaction. 'Turned their faces away' is a deliberate reversal of the priestly blessing direction (Num 6:25-26 — the LORD make his face shine upon you); the fathers had turned their faces away from the place of the blessing. 'Turned their backs' — the neck-language of Exodus 32-34, the stiff-necked rebels at Sinai. Hezekiah places the current apostasy in the long tradition of Israel's wilderness rebellion, making the restoration not merely a political reset but a covenantal return from deeply rooted sin."
    },
    "7": {
      "L": "Also they have shut the doors of the vestibule, and put out the lamps, and have not burned incense nor offered burnt offerings in the holy place to the God of Israel.",
      "M": "They also shut the doors of the vestibule, extinguished the lamps, and stopped burning incense and offering burnt offerings in the holy place to the God of Israel.",
      "T": "Three specific acts of liturgical dismantling: the shut doors (the exclusion of worshipers), the extinguished lamps (the darkening of the menorah, the sign of the LORD's presence), the cessation of incense and burnt offerings (the end of the daily sacrifice that marked Israel as a covenant people). Each of these had Mosaic precedent — the menorah was to burn continually (Lev 24:2), the daily burnt offering was to be perpetual (Exod 29:38-42), the incense was the fragrant memorial of Israel before God (Exod 30:7-8). Ahaz had not merely sinned; he had specifically dismantled the three perpetual signs of the LORD's dwelling in Israel's midst."
    },
    "8": {
      "L": "Therefore the wrath of the LORD was upon Judah and Jerusalem, and he has given them over to trouble, to horror, and to hissing, as you see with your own eyes.",
      "M": "Therefore the LORD's wrath fell on Judah and Jerusalem, and he has made them an object of horror, terror, and mockery, as you yourselves can see.",
      "T": "Hezekiah addresses the visible reality: look around you. The trouble, the horror, the hissing — these were not abstract theological concepts but lived experience. The military defeats, the captives taken, the loss of cities, the presence of Assyrian pressure — all of this was what the assembled Levites and priests had watched happen during Ahaz's sixteen years. Hezekiah does not say 'this is what might happen if we don't reform'; he says 'this is what has happened, and you have seen it.' The reform he is calling for is not a prophylactic against future disaster; it is the response to present disaster that has already arrived."
    },
    "9": {
      "L": "For behold, our fathers have fallen by the sword, and our sons and daughters and our wives are in captivity for this cause.",
      "M": "And behold, our fathers have fallen by the sword, and our sons and daughters and wives are in captivity because of this.",
      "T": "The human cost is named: fathers dead in battle, families in captivity. Hezekiah is not speaking to men who have avoided suffering; he is speaking to men whose families had been among the two hundred thousand Judeans recently carried north by Israel, among those taken by Edom, among those displaced by Philistine occupation of the Shephelah. The word 'for this cause' points directly back to what the fathers had done. The captivity of the sons and daughters is not random misfortune; it is the covenant consequence of the fathers' covenant violation. To understand this is to understand what the reform is for."
    },
    "10": {
      "L": "Now it is in my heart to make a covenant with the LORD, the God of Israel, that his fierce anger may turn away from us.",
      "M": "Now I intend to make a covenant with the LORD, the God of Israel, so that his fierce anger may turn away from us.",
      "T": "The covenant Hezekiah proposes is not new — it is the renewal of the covenant already in place. The LORD was already the God of Israel; Israel was already committed by covenant to him. What Ahaz's apostasy had done was to create a functional breach that required formal re-covenant. The covenant theorem of Chronicles operates in both directions (2 Chr 15:2): if you return to him, he will return to you. Hezekiah is applying the theorem: the fierce anger will turn away when the covenant is genuinely renewed. The initiative comes from the king, but the framework is the LORD's own established structure of return."
    },
    "11": {
      "L": "My sons, be not now negligent, for the LORD has chosen you to stand before him, to serve him, and to be his ministers and burn incense to him.",
      "M": "My sons, do not be negligent now, for the LORD has chosen you to stand before him, to minister to him and to burn incense to him.",
      "T": "The close of Hezekiah's speech moves from historical analysis to personal appeal. He calls them 'my sons' — a king addressing the religious servants of the house with paternal warmth, not merely royal command. The appeal is to their calling, not merely their duty: the LORD has chosen you. The Levitical call in Chronicles is not an administrative assignment; it is divine election, the same vocabulary of chosenness used of David, of Solomon, of Jerusalem itself. Those who have been chosen for this specific purpose — to stand before God, to serve him, to carry the incense — have no legitimate reason for negligence. Their hesitation has cost the nation. Now is the time to act."
    },
    "12": {
      "L": "Then the Levites arose: Mahath the son of Amasai and Joel the son of Azariah, of the sons of the Kohathites; and of the sons of Merari, Kish the son of Abdi and Azariah the son of Jehaleleel; and of the Gershonites, Joah the son of Zimmah and Eden the son of Joah;",
      "M": "Then the Levites rose up: Mahath son of Amasai and Joel son of Azariah, from the Kohathites; Kish son of Abdi and Azariah son of Jehaleleel, from the Merarites; Joah son of Zimmah and Eden son of Joah, from the Gershonites;",
      "T": "The Chronicler provides the full roster of fourteen Levites who led the consecration — two representatives from each of the seven Levitical families. The specificity is characteristic of Chronicles: these were real people whose obedience to Hezekiah's call deserved to be named and remembered. The three main divisions — Kohath, Merari, and Gershon — are the sons of Levi; within them, the sub-families of Elizaphan, Asaph, Heman, and Jeduthun represent the musical and service orders established by David. The full institutional breadth of the Levitical order responded."
    },
    "13": {
      "L": "and of the sons of Elizaphan, Shimri and Jeiel; and of the sons of Asaph, Zechariah and Mattaniah;",
      "M": "Shimri and Jeiel from the sons of Elizaphan; Zechariah and Mattaniah from the sons of Asaph;",
      "T": "Asaph's line appears here — the same Asaph whose psalms Hezekiah will invoke at the end of the worship ceremony (v30). The presence of an Asaphite in the leadership of the consecration mission is appropriate: the worship-leaders were among the first to rise and serve."
    },
    "14": {
      "L": "and of the sons of Heman, Jehiel and Shimei; and of the sons of Jeduthun, Shemaiah and Uzziel.",
      "M": "Jehiel and Shimei from the sons of Heman; Shemaiah and Uzziel from the sons of Jeduthun.",
      "T": "Heman and Jeduthun complete the four Levitical musical families — Asaph, Heman, Jeduthun, and Elizaphan — that David had organized in 1 Chronicles 25. All four respond to Hezekiah's call. The musical and liturgical infrastructure that David had established with such care and prophetic authorization was still present, still organized, still capable of being activated. The faithlessness of Ahaz had shut the doors; it had not dissolved the Levitical order. The structure was there, waiting for a king who would call it back to life."
    },
    "15": {
      "L": "And they gathered their brothers and consecrated themselves and came, according to the commandment of the king, by the words of the LORD, to cleanse the house of the LORD.",
      "M": "They gathered their fellow Levites, consecrated themselves, and went in — as the king commanded, by the word of the LORD — to purify the house of the LORD.",
      "T": "Two sources of authority govern their action: the commandment of the king and the words of the LORD. The Chronicler insists on both: the reform has royal authorization and divine mandate. They consecrated themselves before entering — personal purification as the precondition of institutional service. And they gathered their brothers: the fourteen leaders recruited and organized the full corps of Levites. What began as a speech by the king in the east square became a coordinated institutional movement of the entire Levitical order toward the task of restoring the LORD's house."
    },
    "16": {
      "L": "The priests went into the inner part of the house of the LORD to cleanse it, and they brought out all the uncleanness they found in the temple of the LORD into the court of the house of the LORD. And the Levites took it to carry it out to the brook Kidron.",
      "M": "The priests went into the inner sanctuary to cleanse it and brought all the uncleanness they found in the LORD's temple out to the court. The Levites then took it and carried it out to the Kidron Brook.",
      "T": "The division of labor follows the holiness gradient of the temple: the priests, authorized to enter the inner sanctuary, did the work of removal from the holy of holies and the holy place. The Levites, authorized for the outer courts and the service of carrying, transported the uncleanness from the court to outside the temple precincts altogether — to the Kidron, the valley east of Jerusalem that served as the city's disposal point for sacred debris. The same Kidron into which Asa had burned Maacah's Asherah pole (15:16), into which the unclean materials from the Passover preparation would also be cast (30:14). The Kidron was where the defilements of Israel's unfaithfulness ended up when faith was restored."
    },
    "17": {
      "L": "They began to consecrate on the first day of the first month. On the eighth day of the month they came to the vestibule of the LORD. And they consecrated the house of the LORD in eight days, and on the sixteenth day of the first month they made an end.",
      "M": "They began consecrating on the first day of the first month, reached the vestibule of the LORD by the eighth day, and finished consecrating the LORD's house in eight days — completing it on the sixteenth day of the first month.",
      "T": "The dating is precise and significant: beginning the first of the first month, they worked outward from the inner sanctuary toward the vestibule, completing the work on the sixteenth day. The Passover was supposed to be held on the fourteenth (Lev 23:5). By the time the temple was clean, Passover had already passed — which is why Hezekiah will invoke the second-month Passover provision of Numbers 9 in the next chapter. The Chronicler records the dates not as a failure but as a circumstance that will lead to one of the most extraordinary theological moments in the book: the extension of Passover to those who could not be ready in time, including thousands of northerners who had come to Jerusalem in unexpected response to the royal invitation."
    },
    "18": {
      "L": "Then they went in to King Hezekiah and said, 'We have cleansed all the house of the LORD, the altar of burnt offering with all its vessels, and the table of showbread with all its vessels.'",
      "M": "They went to King Hezekiah and reported: 'We have purified the entire house of the LORD, including the altar of burnt offering with all its vessels and the table of the showbread with all its vessels.'",
      "T": "The report to the king is the completion of the royal commission: what Hezekiah had commanded in his opening speech was now done. The altar of burnt offering — the central installation where the daily sacrifice was offered — had been restored to ritual purity along with all its implements. The table of showbread — the twelve loaves representing the twelve tribes in the presence of the LORD — was cleansed and its vessels were ready. The two objects mentioned are the most theologically loaded furnishings of the outer holy place: the altar (where Israel's offering went up to God) and the showbread table (where Israel's presence was maintained before God). Both were ready to function again."
    },
    "19": {
      "L": "'All the vessels that King Ahaz discarded in his reign in his unfaithfulness, we have prepared and consecrated, and behold, they are before the altar of the LORD.'",
      "M": "'All the vessels that King Ahaz set aside during his unfaithful reign we have prepared and consecrated — they are now before the altar of the LORD.'",
      "T": "Even the vessels that Ahaz had cut to pieces (v24) — or at least those that remained recoverable — were consecrated and returned to service. The Chronicler's detail here makes a quiet point: the desecration was more reversible than it had seemed. What an apostate king had broken and discarded, the Levites gathered, repaired, and re-consecrated. The instruments of covenant worship that Ahaz had treated as scrap material were restored to their proper place before the altar. The damage of Ahaz's reign was deep; it was not permanent."
    },
    "20": {
      "L": "Then Hezekiah the king rose early and gathered the rulers of the city and went up to the house of the LORD.",
      "M": "King Hezekiah rose early, gathered the city's officials, and went up to the LORD's house.",
      "T": "Rising early is the biblical marker of eager obedience — Abraham rose early to sacrifice Isaac (Gen 22:3), Joshua rose early before battle, the Levites rose early to serve. Hezekiah did not wait; the moment the report came that the temple was clean, he rose early and went. The officials of the city accompanied him — this was not a priestly ceremony that the king attended as a guest, but a public covenant event led by the king with the civic leadership of the nation. The worship that was about to happen was the whole community's act, not merely the temple guild's."
    },
    "21": {
      "L": "And they brought seven bulls, seven rams, seven lambs, and seven male goats for a sin offering for the kingdom and for the sanctuary and for Judah. And he commanded the priests, the sons of Aaron, to offer them on the altar of the LORD.",
      "M": "They brought seven bulls, seven rams, seven lambs, and seven male goats as a sin offering for the kingdom, for the sanctuary, and for Judah. He commanded the priests, the sons of Aaron, to offer them on the altar of the LORD.",
      "T": "Seven sevens: the number of completeness and covenant fullness — seven of each animal, covering four quadrants of concern: the whole kingdom, the sanctuary itself, and all Judah. This was not a routine sin offering but a comprehensive national atonement, covering the full scope of Ahaz's apostasy and its effects on every part of the covenant community. The priests, the sons of Aaron, are specified for the altar sacrifice — their distinct role from the Levites maintained even in this unusual ceremony. Hezekiah had not conflated the offices; he had restored each to its proper function."
    },
    "22": {
      "L": "So they killed the bulls, and the priests received the blood and sprinkled it on the altar: likewise when they had killed the rams, they sprinkled the blood upon the altar: they killed also the lambs and sprinkled the blood upon the altar.",
      "M": "They slaughtered the bulls, and the priests received the blood and sprinkled it on the altar; then the rams, and they sprinkled that blood on the altar; then the lambs, and they sprinkled that blood on the altar too.",
      "T": "The triple repetition of the blood-sprinkling sequence is not literary padding; it is liturgical precision. Each type of animal was killed and its blood sprinkled separately — the full Mosaic rite for each, performed in sequence. The blood is the life, and the blood on the altar is the mechanism of atonement (Lev 17:11): the shed life placed on the altar as the covenantal cost of reconciliation. Hezekiah was not abbreviating the rite; he was performing it in its complete form for three of the four categories of offering animal."
    },
    "23": {
      "L": "And they brought forth the male goats for the sin offering before the king and the congregation, and they laid their hands upon them.",
      "M": "The male goats for the sin offering were brought before the king and the assembly, who laid their hands on them.",
      "T": "The laying of hands distinguished the sin offering from the burnt offerings: the offerer identified personally with the animal, transferring in a symbolic act the burden of the sin to be atoned. The king laid his hands first — he bore responsibility for the nation's covenant failure in a way that no private citizen did. The congregation also laid their hands: the communal identification of the whole people with the need for atonement. Before the blood was shed, the sin had to be owned."
    },
    "24": {
      "L": "And the priests killed them, and made sin offering with their blood upon the altar to make atonement for all Israel; for the king had commanded that the burnt offering and the sin offering should be made for all Israel.",
      "M": "The priests slaughtered them and made a sin offering with their blood on the altar to atone for all Israel. For the king had commanded that the burnt offering and the sin offering be made for all Israel.",
      "T": "For all Israel: the scope of the atonement was pan-Israelite. Hezekiah did not offer these sacrifices for Judah and Jerusalem alone, though that was where he was king. His theological vision was the whole twelve-tribe people of God. The northern kingdom, under Assyrian pressure and political domination, had no king offering atonement for it. Hezekiah stepped into that vacuum with a covenant act that claimed all Israel as his pastoral responsibility. This is the same instinct that will drive the Passover invitation of chapter 30: one king of David's line taking covenantal initiative for the entire covenant people."
    },
    "25": {
      "L": "And he stationed the Levites in the house of the LORD with cymbals, harps, and lyres, according to the commandment of David and of Gad the king's seer and of Nathan the prophet, for the commandment was from the LORD by his prophets.",
      "M": "He stationed the Levites in the LORD's house with cymbals, harps, and lyres, as commanded by David, by Gad the king's seer, and by Nathan the prophet — for the commandment was from the LORD through his prophets.",
      "T": "The triple prophetic authorization of the Levitical music is central to the Chronicler's argument. The Davidic worship order was not David's invention; it was given to David by Gad and Nathan — the prophets of the Davidic era — who received it from the LORD. This means the elaborate Levitical musical system has the same authority as the Mosaic legislation it supplements. Those who might have dismissed the Levitical choirs as an optional addition to the essential priestly sacrificial system were confronted with this claim: the LORD commanded it through his prophets. The music was not decoration; it was covenant obligation."
    },
    "26": {
      "L": "And the Levites stood with the instruments of David, and the priests with the trumpets.",
      "M": "The Levites stood with the instruments David had prescribed, and the priests with the trumpets.",
      "T": "The two orders in their proper roles: Levites with the stringed and percussion instruments David had specified, priests with the silver trumpets that Moses had prescribed at Sinai (Num 10:8-10). The division preserved by Hezekiah was the division that David and Moses had established. Even after sixteen years of Ahaz's liturgical destruction, the framework was being restored in precise conformity with its original design."
    },
    "27": {
      "L": "And Hezekiah commanded to offer the burnt offering upon the altar. And when the burnt offering began, the song of the LORD began also, with the trumpets, and with the instruments of David king of Israel.",
      "M": "Hezekiah gave the command to offer the burnt offering on the altar. At the moment the burnt offering began, the song to the LORD also began, with the trumpets and the instruments of David king of Israel.",
      "T": "The moment of ignition: sacrifice and song began simultaneously, by the king's command. The Chronicler's description of this moment is one of the most beautiful in Chronicles. The liturgy did not proceed in two separate phases — first the offering, then the music. They began together: the ascending sacrifice and the ascending praise were a single act. David had organized the worship so that the singing of the LORD's presence accompanied the offering of the people's lives. Hezekiah restored both in one commanded moment."
    },
    "28": {
      "L": "And all the congregation worshipped, and the singers sang, and the trumpeters sounded, and all this continued until the burnt offering was finished.",
      "M": "The whole congregation bowed in worship while the singers sang and the trumpeters sounded, continuing until the burnt offering was complete.",
      "T": "The whole congregation worshipped — not merely observed but participated in the prostration that acknowledged the LORD's presence made real in the sacrifice and the music. The singers, the trumpeters, the assembly — all moving in liturgical unity through the duration of the offering. This was the restored Israel in miniature: king, priests, Levites, and people, each in their proper role, all oriented toward the LORD together. The image is the structural opposite of Ahaz's Jerusalem: high places scattered across every city, each person worshipping their own choice of deity, the temple closed. Hezekiah's Jerusalem was one people, one God, one house, one offering."
    },
    "29": {
      "L": "And when they had made an end of offering, the king and all who were present with him bowed down and worshipped.",
      "M": "When the offering was finished, the king and everyone with him bowed and worshipped.",
      "T": "The completion of the offering was a moment of communal silence and prostration. The king bowed with everyone else — not as a spectator who had commissioned a ceremony, but as a worshiper who shared in its culmination. In Chronicles, the king who worships together with his people is the faithful king; the king who stands apart from covenant worship (like Uzziah who tried to usurp the priestly role) is the king who falls. Hezekiah bowed."
    },
    "30": {
      "L": "Moreover Hezekiah the king and the princes commanded the Levites to sing praise to the LORD with the words of David and of Asaph the seer: and they sang praises with gladness, and they bowed their heads and worshipped.",
      "M": "King Hezekiah and the officials commanded the Levites to sing praise to the LORD in the words of David and of Asaph the seer. They sang praises with joy, and they bowed their heads and worshipped.",
      "T": "David's psalms and Asaph's psalms — the canonical corpus of temple praise — were the vehicle for the Levitical singing. Hezekiah did not commission new worship music for the occasion; he called the community back to the inherited language of covenant praise, the words that Israel's greatest worshippers had given them. Asaph the seer: the Chronicler's designation of Asaph as both singer and prophet reinforces the point made in v25 — the musical tradition was prophetically authorized, not merely traditionally maintained. The Levites sang with gladness and bowed their heads. Gladness is the Chronicler's word for the inner texture of authentic worship; it distinguishes the restored service from the grudging compliance that sometimes masquerades as religion."
    },
    "31": {
      "L": "Then Hezekiah answered and said, 'Now you have consecrated yourselves to the LORD. Come near and bring sacrifices and thank offerings into the house of the LORD.' And the congregation brought in sacrifices and thank offerings, and all who were of a free heart burnt offerings.",
      "M": "Then Hezekiah said: 'Now that you have consecrated yourselves to the LORD, come and bring your sacrifices and thank offerings to the LORD's house.' So the congregation brought sacrifices and thank offerings, and all who were willing of heart brought burnt offerings.",
      "T": "The king's invitation shifted the ceremony from the communal national atonement (the sin offerings for all Israel, commanded by the king) to voluntary personal worship. Now that the public obligation was discharged, he invited individuals to bring what their hearts prompted. 'Willing of heart' is the vocabulary of the tabernacle freewill offering (Exod 35:5, 22, 29) — the same spirit that had funded Moses's wilderness sanctuary and David's temple preparations. Hezekiah was not legislating private piety; he was creating space for it to emerge. And it emerged: the congregation brought burnt offerings out of willing hearts."
    },
    "32": {
      "L": "And the number of the burnt offerings which the congregation brought was seventy bulls, a hundred rams, and two hundred lambs — all these were for a burnt offering to the LORD.",
      "M": "The burnt offerings the congregation brought numbered 70 bulls, 100 rams, and 200 lambs — all for a burnt offering to the LORD.",
      "T": "Three hundred seventy animals from voluntary offering — an astonishing outpouring for a nation that had been under Ahaz's religious regime for sixteen years. The people had been spiritually starved; when the temple was opened and worship was restored, the desire to offer poured out in excess. The numbers are given precisely because they matter: this was not a modest resumption of service but a flood of covenant devotion that had been dammed up and was now released. The Chronicler preserves the count to honor both the giving and the God toward whom it was directed."
    },
    "33": {
      "L": "And the consecrated things were six hundred oxen and three thousand sheep.",
      "M": "The consecrated offerings amounted to 600 oxen and 3,000 sheep.",
      "T": "Beyond the burnt offerings, the consecrated offerings — animals dedicated to the LORD for shared feasting and priestly provision — numbered thirty-six hundred animals. In the sacrificial economy, the consecrated offering was the celebration feast: after the altar portions were burned, the rest was eaten by the priests and the worshippers together. The scale of the consecrated offerings meant that the worship would be followed by a great communal meal — the covenant people eating together in the LORD's presence. The restoration of worship was simultaneously a restoration of covenant community."
    },
    "34": {
      "L": "But the priests were too few, so that they could not flay all the burnt offerings; therefore their brothers the Levites helped them until the work was ended, and until the other priests had consecrated themselves; for the Levites were more upright in heart to consecrate themselves than the priests.",
      "M": "But there were not enough priests to skin all the burnt offerings, so their Levite brothers helped them until the work was done and the remaining priests had consecrated themselves — for the Levites had been more diligent in consecrating themselves than the priests.",
      "T": "One of the Chronicler's more pointed institutional observations: the Levites had been more diligent than the priests in the rush of consecration before the ceremony. The priestly corps that was supposed to lead had been caught insufficiently prepared; the Levitical order stepped in to fill the gap. This is not a harsh rebuke — the Chronicler notes it without drama, and the priests were consecrating themselves even as the work proceeded — but it is a clear signal that the Levitical order, which later priestly tradition sometimes treated as secondary, had in this pivotal moment of national restoration shown greater readiness than the priests themselves. The Chronicler returns to this theme because it matters to his argument about the dignity and faithfulness of the Levites."
    },
    "35": {
      "L": "Also the burnt offerings were in abundance, with the fat of the peace offerings and the drink offerings for every burnt offering. So the service of the house of the LORD was set in order.",
      "M": "The burnt offerings were plentiful, along with the fat of the fellowship offerings and the drink offerings for each burnt offering. So the service of the LORD's house was restored to order.",
      "T": "Three streams flowing together: the burnt offerings (wholly consumed on the altar), the fat portions of the peace offerings (the LORD's portion from the communal feast), and the drink offerings poured out as libations — the full complex of Mosaic worship operating simultaneously. 'Set in order' — the Hebrew kiyn, established, prepared, made ready. This is the word used when David prepared the temple (1 Chr 15:1), when Solomon established his kingdom (2 Chr 1:1). The service of the LORD's house was not merely resumed; it was reconstituted as a complete, ordered system after years of dismantlement."
    },
    "36": {
      "L": "And Hezekiah rejoiced, and all the people, because of what God had prepared for the people; for the thing was done suddenly.",
      "M": "Hezekiah and all the people rejoiced over what God had prepared for the people, for it had all happened so quickly.",
      "T": "The word suddenly — pit'om — is the key to the Chronicler's wonder at what chapter 29 records. The entire cleansing, consecration, and restoration of full temple worship happened within sixteen days of Hezekiah's accession. No one had planned this in advance; the king simply called the Levites, the Levites responded, and in less than three weeks the house of the LORD was fully operational with abundant voluntary worship underway. The Chronicler credits this to God: what God had prepared for the people. The suddenness was a sign of divine initiative — the reform that seemed humanly initiated was actually the LORD moving through a willing king. Hezekiah and all the people rejoiced because they recognized they had received more than they had organized."
    }
  },
  "30": {
    "1": {
      "L": "And Hezekiah sent to all Israel and Judah, and also wrote letters to Ephraim and Manasseh, that they should come to the house of the LORD at Jerusalem to keep the passover to the LORD, the God of Israel.",
      "M": "Hezekiah sent word to all Israel and Judah, and also wrote letters to Ephraim and Manasseh, inviting them to come to the LORD's house in Jerusalem to celebrate the Passover to the LORD, the God of Israel.",
      "T": "The invitation expanded beyond the borders of Judah. Hezekiah sent messengers and letters — official royal communications — to Ephraim and Manasseh, the two dominant tribes of the northern kingdom that Assyria had already begun to dismantle (Tiglath-pileser had taken the Galilee and Transjordan in 733-732 BC). Hezekiah was writing to a people under imperial pressure and political fragmentation and addressing them as 'all Israel' — the Chronicler's pan-Israelite vision in its most concrete political expression. The divided kingdom was theologically anomalous; the Passover invitation was the covenant summons to what the kingdom should never have stopped being."
    },
    "2": {
      "L": "For the king had taken counsel, and his princes, and all the congregation in Jerusalem, to keep the passover in the second month.",
      "M": "The king had consulted with his officials and the whole congregation in Jerusalem and decided to celebrate the Passover in the second month.",
      "T": "The decision to hold the Passover in the second month was not improvised but deliberated: the king, the princes, and the Jerusalem congregation all participated in the decision. Chronicles honors communal discernment — even a king with Hezekiah's authority did not unilaterally declare a liturgical exception; he consulted. The second month Passover invoked the precedent of Numbers 9:9-11, which permitted those who were ritually unclean or on a journey during the first month to keep the Passover a month later. Hezekiah extended this individual provision to the whole nation — a creative application of the Mosaic law that would be vindicated by the LORD's response."
    },
    "3": {
      "L": "For they could not keep it at the appointed time because the priests had not consecrated themselves in sufficient number, nor had the people gathered themselves to Jerusalem.",
      "M": "They could not keep it at the regular time because not enough priests had consecrated themselves and the people had not assembled at Jerusalem.",
      "T": "Two legitimate reasons: insufficient priestly consecration and insufficient popular assembly. The temple cleansing had extended to the sixteenth day — two days past the Passover date (14th of the first month, Lev 23:5). The priests who needed to be sanctified had not had time to complete the process before the appointed date passed. And the broader Israel that Hezekiah wanted to include — the northerners who would need time to travel to Jerusalem — could not have gathered by the fourteenth of the first month even if they had known to come. The second-month date solved both problems simultaneously: it gave the priests time to consecrate themselves fully, and it gave messengers time to reach the northern tribes."
    },
    "4": {
      "L": "And the thing was right in the eyes of the king and all the congregation.",
      "M": "The plan seemed right to the king and the whole assembly.",
      "T": "The simple sentence carries significant weight in the Chronicler's framework: when the king and the congregation agreed, the Chronicler records it as a mark of divine ordering. The 'one heart' language that will appear at v12 for Judah is anticipated here in the unanimity of Jerusalem's leaders. A community aligned in its discernment is a community ready for what God is about to do."
    },
    "5": {
      "L": "So they established a decree to make proclamation throughout all Israel, from Beersheba to Dan, that they should come to keep the passover to the LORD, the God of Israel, at Jerusalem, for they had not done it in great numbers as it was written.",
      "M": "They issued a decree to proclaim throughout all Israel — from Beersheba to Dan — that everyone should come to Jerusalem to keep the Passover to the LORD, the God of Israel, for it had not been celebrated in great numbers as prescribed.",
      "T": "From Beersheba to Dan: the traditional formula for the entire extent of the land, from the southernmost city of Judah to the northernmost city of the northern kingdom. The proclamation claimed the whole geographic scope of the covenant land. 'As it was written' establishes the standard: not as a new festival Hezekiah invented, but as the prescribed covenant celebration of Exodus 12 that had not been kept in the way Moses commanded — in great numbers, at the central sanctuary, by the whole people — since the division of the kingdom. Hezekiah was not innovating; he was restoring."
    },
    "6": {
      "L": "So the posts went with the letters from the king and his princes throughout all Israel and Judah, with the commandment of the king, saying, 'Children of Israel, return to the LORD, the God of Abraham, Isaac, and Israel, that he may return to the remnant who have escaped from the hand of the kings of Assyria.'",
      "M": "The royal couriers went with letters from the king and his officials throughout all Israel and Judah, bearing the king's command: 'People of Israel, return to the LORD, the God of Abraham, Isaac, and Israel, so that he may return to the survivors who remain from the hand of the kings of Assyria.'",
      "T": "The letter is a covenant summons written in the language of the prophets. 'Return to the LORD' — shuv, the fundamental call of prophetic preaching throughout the Old Testament — frames the Passover invitation as what it actually was: not merely a festival observance but a call to covenant return. The patriarchal names — Abraham, Isaac, and Israel — ground the appeal in the deepest layer of covenant history. And 'the survivors who remain from the hand of the kings of Assyria': Hezekiah is writing to a remnant. The deportations of 733-732 had already stripped large parts of the northern population; those who remained were the survivors, and Hezekiah addressed them as people the LORD still wanted. The covenant had not terminated with Assyrian conquest; the God of the patriarchs was still calling."
    },
    "7": {
      "L": "'And be not like your fathers and your brothers, who were faithless to the LORD, the God of their fathers, so that he made them a desolation, as you see.'",
      "M": "'Do not be like your fathers and brothers, who were unfaithful to the LORD, the God of their ancestors, so that he made them a horror, as you can see.'",
      "T": "The appeal includes the warning: do not repeat what brought the disaster you are living in the middle of. The desolation Hezekiah pointed to was visible and recent — the devastated territories, the empty cities, the demographic gaps left by Assyrian deportations. The northern kingdom's covenant violation had produced exactly the covenantal consequence that Moses had warned about (Deut 28:25-37). 'As you see' — the survivors could look at their own landscape and understand what faithlessness had cost. The letter did not speculate about hypothetical consequences; it pointed to the concrete reality around them."
    },
    "8": {
      "L": "'Now do not be stiff-necked as your fathers were, but yield yourselves to the LORD and come to his sanctuary, which he has consecrated forever, and serve the LORD your God, that his fierce anger may turn away from you.'",
      "M": "'Do not be stiff-necked like your ancestors, but submit to the LORD. Come to his sanctuary, which he has consecrated forever, and serve the LORD your God, so that his fierce anger may turn away from you.'",
      "T": "Stiff-necked — the word from Sinai (Exod 32:9; 33:3,5; 34:9) that the LORD had used of Israel immediately after the golden calf. Hezekiah borrowed the precise vocabulary of Israel's foundational failure to name what the northern tribes had perpetuated. But the negative warning is immediately paired with a positive: yield yourselves — the Hebrew natan yad, literally 'give the hand,' a gesture of submission and renewed allegiance. And come to the sanctuary which he has consecrated forever: the temple's permanent status as the LORD's dwelling is the ground of the invitation. Whatever political boundaries divided Israel from Judah, the sanctuary in Jerusalem was consecrated for all Israel, and it remained so."
    },
    "9": {
      "L": "'For if you return to the LORD, your brothers and your children will find compassion before those who led them captive, and return to this land; for the LORD your God is gracious and merciful and will not turn away his face from you if you return to him.'",
      "M": "'For if you return to the LORD, your brothers and children will find compassion from their captors and come back to this land. The LORD your God is gracious and merciful — he will not turn his face away from you if you return to him.'",
      "T": "The promise embedded in the letter: if you return, your captive relatives will be shown compassion. This is the covenant theorem of Chronicles (2 Chr 15:2; 7:14) applied to international politics: the LORD's dealings with Assyria on behalf of captive Israelites were contingent on the response of those still free. More remarkably, Hezekiah grounds the appeal in Exodus 34:6 — the LORD's own self-declaration at Sinai after the golden calf: 'gracious and merciful.' At the moment of Israel's worst failure, the LORD had revealed his character as the foundation of hope for those who return. Hezekiah applied the same revelation to the north: the God who forgave the golden calf generation is the same God who will not turn away his face from returning northerners. The covenant character of the LORD is the ground of all hope."
    },
    "10": {
      "L": "So the posts passed from city to city through the country of Ephraim and Manasseh, even to Zebulun; but they laughed them to scorn and mocked them.",
      "M": "The couriers went from city to city through Ephraim and Manasseh, all the way to Zebulun — but the people laughed and mocked them.",
      "T": "The invitation that had seemed so promising was mostly rejected. The couriers traveled the full length of the northern territory — Ephraim, Manasseh, and even into Zebulun in the far north — and were laughed at. The word for mocked (laytz) is the same used of the arrogant scoffer in Proverbs who cannot receive instruction (Prov 1:22; 9:7-8). The northern response to a covenant summons was scorn. The Chronicler does not explain why — the rejection stands as a judgment on those who refused the king's invitation. But he also does not end there."
    },
    "11": {
      "L": "Nevertheless some men of Asher, Manasseh, and Zebulun humbled themselves and came to Jerusalem.",
      "M": "Nevertheless, some men from Asher, Manasseh, and Zebulun humbled themselves and came to Jerusalem.",
      "T": "Some came. Three northern tribes produced the faithful remnant: Asher on the Mediterranean coast, Manasseh in the central hill country, Zebulun in the Galilee. The verb humbled themselves (kana') is the key term in Chronicles for the response that averts judgment and attracts the LORD's favor. These were men who heard the letter not as an insult or a political manipulation but as a genuine covenant summons, and they responded by making the journey south to Jerusalem. In the broader context of scorn and rejection, the Chronicler honors their names and their tribes. They came. The Passover would not be only for Judah."
    },
    "12": {
      "L": "Also in Judah the hand of God was to give them one heart to do the commandment of the king and of the princes by the word of the LORD.",
      "M": "In Judah too God's hand gave them one heart to carry out the command of the king and the officials, as the word of the LORD directed.",
      "T": "While the northern response was mostly mocking, Judah's response was unified — and the Chronicler names the cause: the hand of God. The 'one heart' given to Judah was not the result of particularly effective royal communication or political pressure; it was divine gift. The same LORD who had moved in the Levites to rise and consecrate (ch 29) now moved in Judah to respond with communal unanimity. The 'word of the LORD' governed the response: not merely royal command, not merely festival tradition, but the living word that the LORD was actively working through Hezekiah's proclamation."
    },
    "13": {
      "L": "And there assembled at Jerusalem much people to keep the feast of unleavened bread in the second month — a very great congregation.",
      "M": "A large crowd — a very great assembly — gathered at Jerusalem to celebrate the Festival of Unleavened Bread in the second month.",
      "T": "The scale of the gathering surprised even the organizers — 'a very great congregation' implies numbers that exceeded what the arrangements had been designed to accommodate. Judah had come with unity (v12), and some of the north had come despite the mockery of their neighbors (vv10-11), and together they filled Jerusalem in a way that the Chronicler marked with the rare superlative 'very great.' Hezekiah had hoped people would come; God ensured that the gathering exceeded what any human planning could have produced."
    },
    "14": {
      "L": "And they arose and removed the altars that were in Jerusalem, and all the altars for burning incense they removed, and cast them into the brook Kidron.",
      "M": "They rose up and removed the altars in Jerusalem, and they cleared away all the incense altars and threw them into the Kidron Brook.",
      "T": "Before the Passover could be celebrated, the idolatrous infrastructure of Ahaz's Jerusalem had to be dismantled. The altars in every corner of the city (28:24) — the physical legacy of sixteen years of systematic idolatry — were torn down and their materials thrown into the Kidron. The congregation that had come for a Passover feast began with cleanup. This was covenant housecleaning enacted by the people themselves: not commanded specifically in the narrative, but arising naturally from the context of return. You cannot keep Passover — the celebration of redemption from Egypt — alongside the altars of Egypt's gods."
    },
    "15": {
      "L": "Then they killed the passover lamb on the fourteenth day of the second month; and the priests and the Levites were ashamed and consecrated themselves and brought burnt offerings into the house of the LORD.",
      "M": "They slaughtered the Passover lamb on the fourteenth day of the second month. The priests and Levites were ashamed and consecrated themselves and brought burnt offerings into the LORD's house.",
      "T": "The shame of the priests and Levites is significant. The laity — the gathered congregation of Judah and the northerners who had come — had shamed the religious professionals by their own eagerness to worship. The congregation that had removed Ahaz's altars with their own hands before the Passover date had demonstrated a readiness that the priestly corps had not fully matched. Shame in this context is a productive theological response: it produced action. The priests and Levites consecrated themselves urgently and brought the burnt offerings — the pressure of the congregation's devotion moved the professionals to catch up."
    },
    "16": {
      "L": "And they stood in their place after their manner, according to the law of Moses the man of God; the priests sprinkled the blood received from the hand of the Levites.",
      "M": "They took their positions as prescribed, following the law of Moses the man of God. The priests sprinkled the blood that the Levites had received.",
      "T": "Order was restored in the midst of the unusual circumstances: each person in their prescribed position, according to the Mosaic law. Moses the man of God — the Chronicler's title for Moses as the one through whom the LORD's instructions came — was the authority governing the ceremony, even this unusual second-month version of it. The blood-ritual was divided as always: Levites received it from the slaughterers, priests sprinkled it on the altar. The division of labor between the orders was maintained even in the emergency adaptations required by the unclean congregation's presence."
    },
    "17": {
      "L": "For there were many in the congregation that had not consecrated themselves; therefore the Levites were in charge of killing the Passover lamb for everyone who was not clean, to consecrate them to the LORD.",
      "M": "For many in the congregation had not consecrated themselves, so the Levites took charge of slaughtering the Passover lambs for all who were not ritually clean, in order to consecrate them to the LORD.",
      "T": "The Mosaic Passover prescription required each household to slaughter its own lamb (Exod 12:3-6). But many of the northerners — men who had traveled from Ephraim, Manasseh, and Zebulun — had not undergone the ritual purification that Passover participation required. The Levites stepped into the gap: they became the slaughterers for those whose ritual status disqualified them from doing it themselves. The effect was to make participation possible for people who could not qualify under normal rules — a pastoral adaptation that the next two verses will theologize into one of the book's most significant statements about the relationship between heart and ritual."
    },
    "18": {
      "L": "For a great multitude of the people — many from Ephraim, Manasseh, Issachar, and Zebulun — had not cleansed themselves, yet they ate the Passover otherwise than it was written. But Hezekiah prayed for them, saying, 'May the good LORD pardon everyone",
      "M": "A large number of the people — many from Ephraim, Manasseh, Issachar, and Zebulun — had not purified themselves, yet they ate the Passover contrary to what was written. But Hezekiah prayed for them: 'May the good LORD forgive everyone",
      "T": "The tension is stated plainly: they ate the Passover contrary to what was written. The Chronicler does not hide the irregularity. But between the violation and the consequence stands Hezekiah's prayer — the intercession of the king on behalf of people whose desire to worship exceeded their ritual qualification. The prayer begins with a remarkable address: 'the good LORD.' Not merely the LORD, not merely the LORD of hosts — the good LORD, invoking divine goodness as the specific ground for asking pardon. This was not a theological argument; it was a relational plea to a God known to be good."
    },
    "19": {
      "L": "who sets his heart to seek God, the LORD the God of his fathers, though he is not cleansed according to the purification of the sanctuary.'",
      "M": "who has set his heart to seek God, the LORD, the God of his ancestors, even if he is not cleansed as the sanctuary requires.'",
      "T": "The criterion Hezekiah offers is the orientation of the heart: who sets his heart to seek God. The Hebrew darash — to seek, to inquire, to turn toward — is the Chronicler's primary word for genuine religious orientation. The one who truly seeks the LORD, even while failing the ritual requirement, is different from the one who is ritually pure but does not seek the LORD at all. Hezekiah does not dissolve the ritual requirement — he acknowledges that these people were not purified according to the sanctuary's standards. He simply asks whether the LORD, who knows the heart, will respond to the heart's orientation when the ritual has not been met. The answer in v20 is that the LORD did."
    },
    "20": {
      "L": "And the LORD listened to Hezekiah and healed the people.",
      "M": "And the LORD listened to Hezekiah and healed the people.",
      "T": "Five words in Hebrew; five words in translation; the entire theological weight of the episode rests here. The LORD listened — he heard the prayer, accepted the argument about the heart's orientation, and responded. Healed the people — the word rapha' is used when the LORD acts to remove a curse or a condition that would otherwise bring death. The ritual violation that might have brought divine punishment was met instead with divine healing. The LORD's response to Hezekiah's intercession was not tolerance of the irregularity but active grace that covered what the irregular worshipers lacked. The prayer was answered as prayer: directly, personally, mercifully."
    },
    "21": {
      "L": "And the children of Israel who were present at Jerusalem kept the feast of unleavened bread seven days with great gladness; and the Levites and the priests praised the LORD day by day, singing to the LORD with loud instruments.",
      "M": "The Israelites present in Jerusalem celebrated the Festival of Unleavened Bread for seven days with great joy. The Levites and priests praised the LORD every day with resounding instruments.",
      "T": "Seven days of great gladness — the Chronicler's characteristic mark of authentic worship. The feast that had begun with the removal of altars and the surprise of a very great congregation was now a week of sustained, daily, exuberant praise. The Levites and priests led with loud instruments — the same instruments that had accompanied the restored burnt offering in chapter 29. The gathered Israel, north and south, healed and clean, fed on the Passover and the unleavened bread, praised the LORD together every day for a week."
    },
    "22": {
      "L": "And Hezekiah spoke encouragingly to all the Levites who showed good skill in the service of the LORD. So they ate throughout the feast seven days, offering peace offerings and giving thanks to the LORD, the God of their fathers.",
      "M": "Hezekiah spoke encouragingly to all the Levites who showed skill and understanding in the LORD's service. They ate throughout the seven-day feast, offering fellowship offerings and confessing praise to the LORD, the God of their ancestors.",
      "T": "The king who had commissioned the Levites, called them 'my sons,' and stood with them through the ceremony of chapter 29 now spoke to them with personal encouragement. 'Good skill' — lev tov, a good heart, the combination of competence and devotion. Hezekiah recognized those who had served with both technical ability and spiritual orientation. The feast was extended through seven days with peace offerings — the fellowship meals that the whole community shared together — and confession to the LORD. Confession here is todah — the acknowledgment of the LORD's character and acts, the verbal accompaniment to the communal feast."
    },
    "23": {
      "L": "And the whole assembly took counsel together to keep the feast another seven days. So they kept it another seven days with gladness.",
      "M": "Then the whole assembly decided to celebrate for another seven days, and they did so with great joy.",
      "T": "The congregation did not want to go home. After seven days of restored worship and communal feast, the assembly — all of them — took counsel together and decided to extend the celebration another seven days. No king commanded this; no priest decreed it. The people voted with their presence and their desire to remain. The fourteen-day Passover that resulted was unprecedented in scale — not commanded by Moses, but not forbidden; an overflow of covenant joy that the LORD had produced and the people recognized as gift. The decision to extend was itself an act of worship: recognizing that what was happening was too good to end on schedule."
    },
    "24": {
      "L": "For Hezekiah king of Judah gave to the congregation a thousand bulls and seven thousand sheep, and the princes gave to the congregation a thousand bulls and ten thousand sheep. And a great number of priests consecrated themselves.",
      "M": "Hezekiah king of Judah contributed 1,000 bulls and 7,000 sheep for the congregation, and the officials contributed 1,000 bulls and 10,000 sheep. A great number of priests consecrated themselves.",
      "T": "Nineteen thousand animals — the provision for fourteen days of feasting for a very great congregation. The king gave first, and the princes matched and exceeded him: together the royal house and the civic leadership provided enough for an extension that no one had planned. This is the Davidic generosity that flows through Chronicles' covenant highlights: at the dedication of Solomon's temple, at David's temple offering — leadership gives generously, the people respond, the giving overflows. The priests who had been shamed into consecrating themselves during the first week (v15) now consecrated themselves in great numbers for the extension — the seven extra days gave them the time they had lacked."
    },
    "25": {
      "L": "And all the congregation of Judah, with the priests and the Levites, and all the congregation that came out of Israel, and the strangers that came from the land of Israel, and that dwelt in Judah, rejoiced.",
      "M": "The whole congregation of Judah rejoiced — the priests, the Levites, all who came from Israel, the foreigners who had come from Israel, and those who lived in Judah.",
      "T": "The five-fold enumeration of those who rejoiced is the Chronicler's deliberate picture of a fully inclusive covenant community: Judah (the host community), priests and Levites (the religious establishment), those who came from Israel (the northern pilgrims who had responded), strangers from the land of Israel (non-Israelites living in the north who had joined the pilgrimage), and resident aliens in Judah. The covenant feast that Hezekiah had organized had gathered the widest possible circle of people who could be gathered — the whole community, defined at its broadest. They all rejoiced."
    },
    "26": {
      "L": "So there was great joy in Jerusalem, for since the time of Solomon the son of David king of Israel there had been nothing like this in Jerusalem.",
      "M": "There was great joy in Jerusalem — nothing like it had been seen in Jerusalem since the time of Solomon son of David king of Israel.",
      "T": "The Solomonic comparison is the Chronicler's highest superlative. Solomon's dedication of the temple (2 Chr 5-7) had been the pinnacle of Israel's covenant history — the moment when all twelve tribes gathered, the ark was installed, and the glory of the LORD filled the house. To say that Hezekiah's Passover equaled that moment is extraordinary praise. And the comparison will be echoed once more in Chronicles — at Josiah's Passover (35:18), which surpassed even Hezekiah's. The progressive covenant renewal arc of Chronicles moves through these peaks: Solomon's dedication, Hezekiah's Passover, Josiah's Passover — each one a restoration that reaches back to the foundational event and in reaching back points forward."
    },
    "27": {
      "L": "Then the priests the Levites arose and blessed the people, and their voice was heard, and their prayer came up to his holy dwelling place, even to heaven.",
      "M": "Then the priests and Levites stood up to bless the people. Their voice was heard, and their prayer ascended to his holy dwelling place — to heaven.",
      "T": "The final verse of the Passover account is the final verse of the festival: the priestly blessing, the ascending prayer, the dwelling place in heaven. The Aaronic blessing of Numbers 6:24-26 — may the LORD make his face shine upon you — was the completion of the fourteen-day celebration. And 'their voice was heard': the same declaration made of Solomon's prayer at the temple dedication (2 Chr 7:1 — the fire came down) — the LORD received the prayer, the voice penetrated from the court of priests in Jerusalem to the holy dwelling place in heaven. The God who had healed the unclean northerners at Hezekiah's intercession (v20) was now receiving the blessing with which the Passover ended. Heaven heard. The feast that had begun with the removal of Ahaz's altars ended with the LORD's own acceptance of the blessing spoken in his name."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '2chronicles')
        merge_tier(existing, CHRONICLES2, tier_key)
        save(tier_dir, '2chronicles', existing)
    print('2 Chronicles 28–30 written.')

if __name__ == '__main__':
    main()
