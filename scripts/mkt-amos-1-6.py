"""
MKT Amos chapters 1–6 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-amos-1-6.py

=== CHAPTER OVERVIEW ===

Amos was a shepherd and sheep-breeder (H5349 noqed) from Tekoa in Judah, called to
prophesy against the northern kingdom of Israel during the prosperous reigns of Uzziah
(Judah) and Jeroboam II (Israel), two years before an earthquake Zechariah 14:5 also
remembers. He is the earliest writing prophet whose book survives.

Chapters 1–2: Seven oracle-judgments against surrounding nations using the graduated
  numerical formula ("For three crimes... and for four..."), culminating in the full
  indictment of Israel (2:6–16). The rhetoric traps the audience — each oracle draws
  approval until the final blow lands at home.

Chapter 3: The logic of election reversed. Israel's privileged knowledge of the LORD
  makes her more — not less — accountable for sin (3:2). A series of rhetorical questions
  (3:3–8) establishes the necessity of prophecy and of divine action.

Chapter 4: The "cows of Bashan" — wealthy Samaritan women who exploit the poor (4:1–3).
  Ironic summons to multiply sin at Bethel and Gilgal (4:4–5). Six "yet you did not
  return to me" statements cataloguing divine chastisements Israel ignored (4:6–11).
  Climactic call: "Prepare to meet your God" (4:12) followed by the creator-doxology (4:13).

Chapter 5: Funeral lament for Israel (5:1–3). Competing calls — seek the LORD, not
  Bethel (5:4–7). Creator doxology (5:8–9). Social critique: corruption at the gate
  (5:10–13). Renewed ethical call (5:14–15). Wailing announced (5:16–17). Reversal of
  the Day of the LORD from expected deliverance to certain darkness (5:18–20). Rejection
  of worthless worship; the demand for justice like flowing water (5:21–24). Closing
  indictment of idolatry (5:25–27).

Chapter 6: Woe to the complacent aristocracy of Zion and Samaria (6:1–7). Divine oath
  of revulsion against Jacob's pride (6:8). Scenes of mass death (6:9–10). Absurdity of
  their moral inversions (6:11–13). Prophetic announcement of the coming oppressor (6:14).

=== CONTESTED-TERM DECISIONS ===

- H3068 (יהוה / Yahweh): Following the Joel convention (mkt-joel-1-3.py).
  L/M: "LORD" (small-caps convention). T: "Yahweh" in oracle introductions, direct
  divine speech, and covenantally/eschatologically weighted contexts; "the LORD" in
  lighter narrative references.

- H136 (אֲדֹנָי / Adonai): L/M: "the Lord" when standing alone; as part of the
  compound title with H3068: L/M "the Lord GOD"; T "the Sovereign LORD." This compound
  title (אֲדֹנָי יְהוִה) is characteristic of Amos — occurring far more than any other
  prophet at this length.

- H3069: The special YHWH ketiv used when paired with Adonai to avoid double-LORD.
  Part of "the Lord GOD" / "the Sovereign LORD" compound noted above.

- Oracle formula "For three transgressions of X, and for four":
  L: "For three transgressions of X and for four, I will not turn it back"
     (literally "I will not return it" — the divine decree is irrevocable).
  M: "For three crimes of X, and for four, I will not revoke judgment —"
  T: "Three crimes, four — and X will not escape judgment" with the specific
     charge following. This formula is the backbone of chs. 1–2; variations preserved.

- H6588 (פֶּשַׁע / pesha): L: "transgressions"; M: "crimes"; T: "crimes" (maintains
  the judicial register Amos deliberately activates by indicting the nations).

- H4941 (מִשְׁפָּט / mishpat): "justice" in all tiers throughout. At 5:7 and 5:24
  the word stands in structural parallel with H6666 (tsedaqah / righteousness).

- H6666 (צְדָקָה / tsedaqah): "righteousness" in L/M. In T, where the prophetic
  context is judicial/ethical, "righteousness" is maintained; T at 5:24 uses
  "righteousness" to keep the parallelism visible.

- H8451 (תּוֹרָה / Torah) at 2:4: L: "law"; M: "instruction"; T: "Torah" — the word
  signals the Sinai covenant document, not merely generic religious law.

- H5349 (נֹקְדִים / noqdim) at 1:1: "herdsmen" (L) / "sheep breeders" (M/T) — the
  specific term for a stock-handler/breeder; not the generic "shepherd" (ro'eh).
  Cf. 2 Kgs 3:4 where Mesha king of Moab is also called noqed.

- H7307 (רוּחַ / ruah) at 4:13: "wind" in all tiers. This is the natural meteorological
  phenomenon God creates — not the divine Spirit. No capital.

- H7015 (קִינָה / qinah) at 5:1: The characteristic funeral dirge / lamentation meter.
  L: "lamentation"; M: "funeral song"; T: "funeral dirge." T tier in 5:1–3 uses
  broken-line structure to echo the qinah rhythm.

- יוֹם יְהוָה (Day of the LORD) at 5:18–20: L/M: "the day of the LORD" (lower case,
  standard). T: "the Day of the LORD" (capitalised) to flag the book's eschatological
  weight; Amos is the first prophet to make this reversal explicit.

- H5522 (סִכּוּת / sikkuth) and H3594 (כִּיּוּן / kiyyun) at 5:26: Assyrian deity names.
  L/M use the Hebrew forms "Sikkuth" and "Kiyyun." T keeps the same forms with a
  brief contextual gloss. Acts 7:43 follows the LXX reading ("Moloch," "Rephan") but
  the MT is preferred here. H4428 (melek = "king") in this verse is read as the title
  "your king," not the deity-name Molech.

- 6:13 Lo-debar wordplay: לֹא דָבָר (Lo-debar) literally means "no-thing / nothing."
  T surfaces the wordplay. Karnaim (= "two horns") symbolises military strength; T
  notes this contrast.

- 5:17 "I will pass through" (H5674 avar): Deliberate echo of the Passover/Exodus
  event, but the one passing through is now judgment, not deliverance. T makes this
  inversion visible.

- Doxologies (4:13 and 5:8–9): Hymnic participial fragments identifying the creator-God.
  T uses line breaks and elevated register to preserve their hymnic quality.

- 2:4 H3577 (כָּזָב / kazbim): "lies" (L) / "false gods" (M/T) — the word can mean
  both "lies" and "deceptive things/idols." The referent in context is the false gods
  that led the ancestors astray. M/T prefer "false gods" to surface the idolatry charge.

- Poetic structure: Chapters 1–2 are rhetorical prose-poetry (the oracle series). Chs.
  3–6 mix prophetic poetry with prose. T tier uses line breaks for 5:1–3 (dirge),
  the doxologies (4:13, 5:8–9), the woe oracles (5:18–20, 6:1–7), and the justice
  call (5:24). M uses flowing prose throughout. L preserves source word order.

- Hebrew aspect: Prophetic perfects in the oracle "I will send fire" express certainty
  of future execution — rendered as "I will send" (future indicative). The repeated
  refrain "yet you did not return to me" (4:6–11) is past narrative; the six instances
  are rendered consistently across tiers.
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

AMOS = {
  "1": {
    "1": {
      "L": "The words of Amos, who was among the herdsmen of Tekoa, which he saw concerning Israel in the days of Uzziah king of Judah and in the days of Jeroboam son of Joash king of Israel, two years before the earthquake.",
      "M": "The words of Amos, a sheep breeder from Tekoa, which he received as vision concerning Israel in the days of Uzziah king of Judah and Jeroboam son of Joash king of Israel — two years before the earthquake.",
      "T": "These are the words of Amos — a sheep breeder from Tekoa — the vision he received concerning Israel, in the reign of Uzziah over Judah and Jeroboam son of Joash over Israel, two years before the earthquake struck."
    },
    "2": {
      "L": "And he said: The LORD roars from Zion and utters his voice from Jerusalem; and the pastures of the shepherds shall mourn, and the top of Carmel shall wither.",
      "M": "He said: The LORD roars from Zion and thunders his voice from Jerusalem; the shepherds' pastures wither in mourning and the summit of Carmel dries up.",
      "T": "He declared: Yahweh roars from Zion, / his voice thunders out of Jerusalem — / the shepherds' meadows turn to mourning, / the crown of Carmel shrivels and dies."
    },
    "3": {
      "L": "Thus says the LORD: For three transgressions of Damascus and for four I will not turn it back, because they threshed Gilead with threshing sledges of iron.",
      "M": "This is what the LORD says: For three crimes of Damascus, and for four, I will not revoke judgment — because they threshed Gilead with iron threshing sledges.",
      "T": "Thus says Yahweh: Three crimes, four — and Damascus will not escape judgment, for they ground Gilead to dust beneath iron threshing sledges."
    },
    "4": {
      "L": "But I will send fire on the house of Hazael, and it shall devour the palaces of Ben-hadad.",
      "M": "I will send fire against the house of Hazael, and it will consume the fortresses of Ben-hadad.",
      "T": "I will send fire on Hazael's dynasty, and it will devour the citadels of Ben-hadad."
    },
    "5": {
      "L": "And I will break the bar of Damascus and cut off the inhabitant from the Valley of Aven and the one who holds the scepter from Beth-eden; and the people of Aram shall go into exile to Kir, says the LORD.",
      "M": "I will break the gate-bar of Damascus; I will cut off the ruler from the Valley of Aven and the scepter-bearer from Beth-eden — and the people of Aram will go into exile to Kir, says the LORD.",
      "T": "The gate-bar of Damascus I will shatter; / the lord of the Valley of Aven will be cut down, / the scepter-bearer of Beth-eden driven out — / and Aram's people will be exiled to Kir. / Yahweh has spoken."
    },
    "6": {
      "L": "Thus says the LORD: For three transgressions of Gaza and for four I will not turn it back, because they carried into exile a whole community to deliver them to Edom.",
      "M": "This is what the LORD says: For three crimes of Gaza, and for four, I will not revoke judgment — because they deported a whole people to deliver them to Edom.",
      "T": "Thus says Yahweh: Three crimes, four — and Gaza will not escape judgment, for they uprooted whole communities and handed them over to Edom."
    },
    "7": {
      "L": "But I will send fire on the wall of Gaza, and it shall devour her palaces.",
      "M": "I will send fire on the wall of Gaza, and it will consume her fortresses.",
      "T": "I will send fire against Gaza's walls — it will devour her citadels to ash."
    },
    "8": {
      "L": "And I will cut off the inhabitant from Ashdod and the one who holds the scepter from Ashkelon; and I will turn my hand against Ekron, and the remnant of the Philistines shall perish, says the Lord GOD.",
      "M": "I will cut off the ruler of Ashdod and the scepter-bearer of Ashkelon; I will turn my hand against Ekron, and the remnant of the Philistines will perish, says the Lord GOD.",
      "T": "The lord of Ashdod I will cut down; / the scepter of Ashkelon will be broken; / I will turn against Ekron — / and the last of the Philistines will be destroyed. / So says the Sovereign LORD."
    },
    "9": {
      "L": "Thus says the LORD: For three transgressions of Tyre and for four I will not turn it back, because they delivered up a whole community to Edom and did not remember the covenant of brotherhood.",
      "M": "This is what the LORD says: For three crimes of Tyre, and for four, I will not revoke judgment — because they handed over a whole people to Edom and showed no regard for the covenant of brotherhood.",
      "T": "Thus says Yahweh: Three crimes, four — and Tyre will not escape judgment, for they sold whole peoples into Edom's hands and trampled the covenant that bound them as brothers."
    },
    "10": {
      "L": "But I will send fire on the wall of Tyre, and it shall devour her palaces.",
      "M": "I will send fire on the wall of Tyre, and it will consume her fortresses.",
      "T": "I will send fire against the walls of Tyre — it will consume her citadels."
    },
    "11": {
      "L": "Thus says the LORD: For three transgressions of Edom and for four I will not turn it back, because he pursued his brother with the sword and cast off all pity, and his anger tore perpetually and he kept his wrath forever.",
      "M": "This is what the LORD says: For three crimes of Edom, and for four, I will not revoke judgment — because he hunted down his brother with the sword, stifled all compassion, and sustained his rage unceasingly, nursing his fury without end.",
      "T": "Thus says Yahweh: Three crimes, four — and Edom will not escape judgment, for he hunted down his own brother with the sword, killed all compassion within himself, and kept his rage burning — an undying fury nursed through every generation."
    },
    "12": {
      "L": "But I will send fire upon Teman, and it shall devour the palaces of Bozrah.",
      "M": "I will send fire on Teman, and it will consume the fortresses of Bozrah.",
      "T": "I will send fire on Teman — it will devour the citadels of Bozrah."
    },
    "13": {
      "L": "Thus says the LORD: For three transgressions of the sons of Ammon and for four I will not turn it back, because they ripped open the pregnant women of Gilead to enlarge their territory.",
      "M": "This is what the LORD says: For three crimes of the Ammonites, and for four, I will not revoke judgment — because they tore open pregnant women in Gilead in order to extend their territory.",
      "T": "Thus says Yahweh: Three crimes, four — and Ammon will not escape judgment, for they ripped open pregnant women in Gilead — a war crime against the unborn — all to push their border wider."
    },
    "14": {
      "L": "But I will kindle a fire on the wall of Rabbah, and it shall devour her palaces, with shouting on the day of battle, with a tempest on the day of the whirlwind.",
      "M": "I will kindle fire on the wall of Rabbah, and it will consume her fortresses, amid battle cries on the day of war and a storm on the day of the whirlwind.",
      "T": "I will kindle fire against the walls of Rabbah — her citadels will burn amid the war-shouts of battle, in the roar of the whirlwind."
    },
    "15": {
      "L": "And their king shall go into exile, he and his princes together, says the LORD.",
      "M": "Their king will go into exile, together with his officials, says the LORD.",
      "T": "Their king will be marched into exile — he and all his princes together. Yahweh has spoken."
    }
  },
  "2": {
    "1": {
      "L": "Thus says the LORD: For three transgressions of Moab and for four I will not turn it back, because he burned the bones of the king of Edom to lime.",
      "M": "This is what the LORD says: For three crimes of Moab, and for four, I will not revoke judgment — because they burned the bones of Edom's king to lime.",
      "T": "Thus says Yahweh: Three crimes, four — and Moab will not escape judgment, for they burned the bones of Edom's king to lime — desecrating the dead."
    },
    "2": {
      "L": "But I will send fire upon Moab, and it shall devour the palaces of Kerioth, and Moab shall die amid tumult, with shouting and the sound of the trumpet.",
      "M": "I will send fire on Moab, and it will consume the fortresses of Kerioth; Moab will fall in turmoil, in the din of shouts and trumpets.",
      "T": "I will send fire on Moab — the citadels of Kerioth will burn; / Moab will die in the din of battle, / in shouts and the blast of the trumpet."
    },
    "3": {
      "L": "And I will cut off the judge from its midst and slay all its princes with him, says the LORD.",
      "M": "I will cut off the ruler from its midst and kill all its princes with him, says the LORD.",
      "T": "I will cut down the ruler from among them, and every prince will fall with him. Yahweh has spoken."
    },
    "4": {
      "L": "Thus says the LORD: For three transgressions of Judah and for four I will not turn it back, because they have despised the law of the LORD and have not kept his statutes, and their lies have led them astray, those after which their fathers walked.",
      "M": "This is what the LORD says: For three crimes of Judah, and for four, I will not revoke judgment — because they have rejected the instruction of the LORD and have not kept his statutes; their false gods have led them astray, the same ones their ancestors followed.",
      "T": "Thus says Yahweh: Three crimes, four — and Judah will not escape judgment, for they have spurned the LORD's Torah and refused his statutes; they have been led astray by the same false gods their fathers chased."
    },
    "5": {
      "L": "But I will send fire upon Judah, and it shall devour the palaces of Jerusalem.",
      "M": "I will send fire on Judah, and it will consume the fortresses of Jerusalem.",
      "T": "I will send fire on Judah — it will devour Jerusalem's citadels."
    },
    "6": {
      "L": "Thus says the LORD: For three transgressions of Israel and for four I will not turn it back, because they sell the righteous for silver and the poor for a pair of sandals.",
      "M": "This is what the LORD says: For three crimes of Israel, and for four, I will not revoke judgment — because they sell the innocent for silver and the needy for a pair of sandals.",
      "T": "Thus says Yahweh: Three crimes, four — and Israel will not escape judgment, for they sell the righteous man for silver and the destitute for a pair of sandals."
    },
    "7": {
      "L": "They who trample on the head of the poor into the dust of the earth and turn aside the way of the afflicted; and a man and his father go in to the same girl, to profane my holy name.",
      "M": "They trample the heads of the poor into the dust and push the afflicted off the road; father and son go to the same woman, so they profane my holy name.",
      "T": "They grind the poor man's face into the dust; / they shove the afflicted off the road. / Father and son share the same girl — / defiling my holy name."
    },
    "8": {
      "L": "Upon clothes taken in pledge they lay themselves down beside every altar, and in the house of their God they drink the wine of those who have been fined.",
      "M": "They spread out pledged garments beside every altar, and in the house of their God they drink wine acquired through court fines.",
      "T": "On garments seized as collateral they sprawl beside every altar; / in the temple of their own God they drink wine wrung from the poor through court fines."
    },
    "9": {
      "L": "Yet it was I who destroyed the Amorite before them, whose height was like the height of the cedars and who was as strong as the oaks; and I destroyed his fruit above and his roots below.",
      "M": "Yet it was I who destroyed the Amorite before them, whose height was like that of the cedars and whose strength was like the oaks; I cut off his fruit above and his roots below.",
      "T": "And yet — I was the one who destroyed the Amorite before them, / tall as cedars, strong as oaks; / I cut off his fruit above / and his roots below."
    },
    "10": {
      "L": "Also I brought you up from the land of Egypt and led you forty years through the wilderness to possess the land of the Amorite.",
      "M": "I also brought you up from the land of Egypt, led you through the wilderness for forty years, and gave you the land of the Amorite.",
      "T": "I brought you up from Egypt; / I led you through the wilderness forty years / to put you in possession of the Amorite's land."
    },
    "11": {
      "L": "And I raised up from among your sons prophets and from among your young men Nazirites. Is it not so, O sons of Israel? says the LORD.",
      "M": "I raised up prophets from among your sons and Nazirites from among your young men. Is this not so, O people of Israel? declares the LORD.",
      "T": "I raised up prophets from among your own sons, / Nazirites from your own young men. / Is this not true, Israel? / So Yahweh declares."
    },
    "12": {
      "L": "But you gave wine to the Nazirites to drink and commanded the prophets saying, Do not prophesy.",
      "M": "But you gave the Nazirites wine to drink and ordered the prophets: Do not prophesy.",
      "T": "But you gave the Nazirites wine to drink / and silenced the prophets: 'Do not prophesy.'"
    },
    "13": {
      "L": "Behold, I am pressing you down in your place, as a cart full of sheaves presses down.",
      "M": "Watch — I will crush you in your tracks, as a cart loaded with sheaves presses down.",
      "T": "Now watch — I will press you down where you stand, / as a loaded harvest cart crushes the grain beneath it."
    },
    "14": {
      "L": "Flight shall perish from the swift, and the strong shall not strengthen himself, and the mighty shall not save his life.",
      "M": "Flight will fail the swift, the strong will find no strength, and the warrior will not escape with his life.",
      "T": "The fastest runner will have nowhere to flee; / the strongest man will find his strength gone; / the warrior will not save his own life."
    },
    "15": {
      "L": "The one who handles the bow shall not stand, and the swift of foot shall not escape, and the one who rides the horse shall not save his life.",
      "M": "The bowman will not hold his ground; the swift-footed soldier will not escape; the horseman will not save his life.",
      "T": "The archer will not stand his ground; / the fast-footed soldier will not escape; / the mounted warrior will not save his life."
    },
    "16": {
      "L": "And the courageous among the mighty shall flee away naked in that day, says the LORD.",
      "M": "Even the most courageous warrior will flee away naked on that day, declares the LORD.",
      "T": "Even the bravest of soldiers / will run away naked on that day. / Yahweh has spoken."
    }
  },
  "3": {
    "1": {
      "L": "Hear this word that the LORD has spoken against you, O sons of Israel, against the whole family that I brought up from the land of Egypt, saying:",
      "M": "Hear this word that the LORD has spoken against you, O people of Israel — against the whole family I brought up from the land of Egypt:",
      "T": "Hear this word that Yahweh has spoken against you, O people of Israel — against the whole family he brought up from Egypt:"
    },
    "2": {
      "L": "You only have I known of all the families of the earth; therefore I will punish you for all your iniquities.",
      "M": "You alone of all the families of the earth have I known — therefore I will hold you accountable for all your iniquities.",
      "T": "You — only you — of all the families of the earth have I known in covenant. / That is exactly why I must call every sin of yours to account."
    },
    "3": {
      "L": "Do two walk together unless they have agreed?",
      "M": "Can two people walk together unless they have made an appointment?",
      "T": "Do two people travel together unless they have arranged to meet?"
    },
    "4": {
      "L": "Does a lion roar in the forest when it has no prey? Does a young lion cry out from its den if it has caught nothing?",
      "M": "Does a lion roar in the forest when it has no prey? Does a young lion growl from its lair when it has caught nothing?",
      "T": "Does a lion roar in the forest when there is no prey? / Does the lion's cub snarl from its den if it has caught nothing?"
    },
    "5": {
      "L": "Does a bird fall into a snare on the earth when there is no trap for it? Does a snare spring up from the ground when it has taken nothing?",
      "M": "Does a bird fall to the ground in a snare when no trap has been set? Does a trap spring from the ground when it has caught nothing?",
      "T": "Does a bird fall to the ground in a trap / unless a snare was set for it? / Does a trap spring shut / unless it has caught something?"
    },
    "6": {
      "L": "If a trumpet is blown in a city will the people not be afraid? If there is disaster in a city has the LORD not done it?",
      "M": "When a ram's horn sounds the alarm in a city, do the people not tremble? When disaster strikes a city, has it not been the LORD's doing?",
      "T": "When the trumpet sounds the alarm in a city, don't the people tremble? / When disaster strikes a city — hasn't the LORD done it?"
    },
    "7": {
      "L": "For the Lord GOD does nothing without revealing his counsel to his servants the prophets.",
      "M": "For the Lord GOD does nothing without first disclosing his plans to his servants the prophets.",
      "T": "The Sovereign LORD does nothing in the world without first revealing his purpose to his servants the prophets."
    },
    "8": {
      "L": "The lion has roared; who will not fear? The Lord GOD has spoken; who can do other than prophesy?",
      "M": "The lion has roared — who will not be afraid? The Lord GOD has spoken — who can withhold prophecy?",
      "T": "A lion has roared — who would not be afraid? / The Sovereign LORD has spoken — who can help but prophesy?"
    },
    "9": {
      "L": "Proclaim upon the palaces of Ashdod and upon the palaces in the land of Egypt, and say: Assemble on the mountains of Samaria and see the great tumults within her, and the oppression in her midst.",
      "M": "Proclaim to the citadels of Ashdod and to the strongholds in the land of Egypt: Gather on the mountains of Samaria and witness the great disorders within her and the oppression inside her.",
      "T": "Announce it to the citadels of Ashdod, / proclaim it to the strongholds of Egypt: / 'Come, gather on the hills of Samaria — / see the chaos that seethes within her, / see the crushed people in her midst.'"
    },
    "10": {
      "L": "For they do not know how to do right, says the LORD, those who store up violence and robbery in their palaces.",
      "M": "They do not know how to act with integrity, declares the LORD — those who hoard violence and plunder in their fortresses.",
      "T": "They have lost all knowledge of what is right — so Yahweh declares — / they who stuff their citadels with violence and robbery."
    },
    "11": {
      "L": "Therefore thus says the Lord GOD: An adversary shall surround the land, and he shall bring down your strength from you, and your palaces shall be plundered.",
      "M": "Therefore this is what the Lord GOD says: An enemy will surround the land; he will strip away your defenses, and your fortresses will be plundered.",
      "T": "And so — this is the word of the Sovereign LORD: / An enemy will encircle the land; / your military power will be stripped away, / your citadels looted."
    },
    "12": {
      "L": "Thus says the LORD: As the shepherd rescues from the mouth of the lion two legs or a piece of an ear, so shall the sons of Israel dwelling in Samaria be rescued — with the corner of a couch and the leg of a bed.",
      "M": "This is what the LORD says: As the shepherd snatches from the lion's mouth two legs or a scrap of an ear, so will the Israelites who live in Samaria be rescued — with nothing but a corner of a bed and a fragment of a couch.",
      "T": "Thus says Yahweh: The way a shepherd grabs from a lion's jaws / two bone-legs and a torn ear-scrap, / so will it be for the Israelites who live in Samaria — / rescued with nothing but a corner of a couch, / a splinter of a bed."
    },
    "13": {
      "L": "Hear and testify against the house of Jacob, says the Lord GOD, the God of hosts.",
      "M": "Hear this and testify against the house of Jacob, declares the Lord GOD, the God of armies.",
      "T": "Hear and bear witness against the house of Jacob — so says the Sovereign LORD, the God of heavenly armies."
    },
    "14": {
      "L": "For on the day I punish Israel for his transgressions I will also punish the altars of Bethel, and the horns of the altar shall be cut off and fall to the ground.",
      "M": "On the day I call Israel to account for its crimes, I will also strike down the altars of Bethel; the altar's horns will be cut off and fall to the ground.",
      "T": "On the day I bring Israel to judgment for its sins, / I will strike at the altars of Bethel — / the altar horns will be hacked off / and topple to the ground."
    },
    "15": {
      "L": "And I will strike the winter house along with the summer house, and the ivory houses shall perish and the great houses shall come to an end, says the LORD.",
      "M": "I will demolish both the winter house and the summer house; the houses adorned with ivory will perish and the great mansions will come to an end, declares the LORD.",
      "T": "I will smash the winter palace together with the summer retreat; / the ivory-paneled mansions will be brought down; / the great houses — all of them — will end. / Yahweh has spoken."
    }
  },
  "4": {
    "1": {
      "L": "Hear this word, you cows of Bashan who are on the mountain of Samaria, who oppress the poor, who crush the needy, who say to their masters, Bring, that we may drink.",
      "M": "Hear this word, you cows of Bashan on Mount Samaria — you who oppress the poor and crush the needy and say to your husbands, 'Bring us something to drink!'",
      "T": "Hear this, you pampered cows of Bashan / lounging on the hills of Samaria — / you who grind the poor underfoot / and demand of your husbands: 'Bring us drinks!'"
    },
    "2": {
      "L": "The Lord GOD has sworn by his holiness: Behold, days are coming upon you when they shall lift you away with hooks and the last of you with fish-hooks.",
      "M": "The Lord GOD has sworn by his holiness: days are coming upon you when they will drag you away with hooks — even the last of you with fishhooks.",
      "T": "The Sovereign LORD swears it by his own holiness: / Days are coming upon you / when they will drag you out with hooks — / drag every last one of you away with fishhooks."
    },
    "3": {
      "L": "And you shall go out through the breaches, each woman straight ahead, and you shall be cast toward Harmon, says the LORD.",
      "M": "You will be dragged through the breaches in the walls, each woman straight out before her, and flung toward Harmon, declares the LORD.",
      "T": "Through the gaping breaches in the walls you will be shoved, / one by one, straight out before you, / and hurled toward Harmon. / Yahweh has spoken."
    },
    "4": {
      "L": "Come to Bethel and transgress; to Gilgal, and multiply transgressions; bring your sacrifices every morning, your tithes every three days.",
      "M": "Come to Bethel and rebel; go to Gilgal and multiply your rebellion; bring your sacrifices every morning, your tithes every three days.",
      "T": "Come on then — go to Bethel and sin, / go to Gilgal and sin all the more! / Bring your sacrifices every morning, / your tithes every three days."
    },
    "5": {
      "L": "And offer a sacrifice of thanksgiving from leavened bread, and proclaim freewill offerings, publish them; for so you love to do, O sons of Israel, says the Lord GOD.",
      "M": "Offer your leavened thanksgiving sacrifices and proclaim your freewill offerings, announce them publicly — for this is what you love to do, O people of Israel, says the Lord GOD.",
      "T": "Burn leavened bread as a thanksgiving offering; / announce your freewill gifts, trumpet them about — / because this is what you love to do, Israel! / So says the Sovereign LORD."
    },
    "6": {
      "L": "I also gave you cleanness of teeth in all your cities and lack of bread in all your places, yet you did not return to me, says the LORD.",
      "M": "I gave you empty mouths in all your cities and shortage of food in all your towns — yet you did not return to me, declares the LORD.",
      "T": "I struck you with famine — / empty mouths in every city, / no bread anywhere in the land — / and still you did not come back to me. / Yahweh's word."
    },
    "7": {
      "L": "And also I withheld the rain from you when there were yet three months to the harvest; I caused it to rain on one city and caused it not to rain on another city; one piece of land was rained upon, and the piece on which it did not rain withered.",
      "M": "I also withheld the rain from you three months before harvest; I sent rain on one city but not another; one piece of ground received rain while another dried up.",
      "T": "I held back the rain from you / when the harvest was three months away — / sending rain on one city / but withholding it from another; / one field drenched, another parched."
    },
    "8": {
      "L": "So two or three cities wandered to one city to drink water and were not satisfied, yet you did not return to me, says the LORD.",
      "M": "Two or three cities staggered to another city for water and could not get enough — yet you did not return to me, declares the LORD.",
      "T": "Two cities, three, staggered to another city just to find water, / and still went thirsty — / yet you did not come back to me. / Yahweh's word."
    },
    "9": {
      "L": "I struck you with blight and mildew; your many gardens and your vineyards and your fig trees and your olive trees the cutting locust devoured, yet you did not return to me, says the LORD.",
      "M": "I struck your crops with blight and mildew; locusts devoured your many gardens and vineyards, your fig trees and olive trees — yet you did not return to me, declares the LORD.",
      "T": "I struck your crops with blight and mildew; / locust after locust stripped your gardens, / your vineyards, your fig trees, your olives — / and still you did not come back to me. / Yahweh's word."
    },
    "10": {
      "L": "I sent among you a pestilence after the manner of Egypt; I killed your young men with the sword and took your horses, and I caused the stench of your camp to rise up into your nostrils, yet you did not return to me, says the LORD.",
      "M": "I sent among you a plague like those of Egypt; I killed your young men with the sword, took your horses captive, and made the stench of your camps rise into your nostrils — yet you did not return to me, declares the LORD.",
      "T": "I sent plague through your ranks like Egypt's plagues; / I cut down your young men with the sword; / I led your horses away as plunder / and made the stench of your camps rise to your nostrils — / and still you did not come back to me. / Yahweh's word."
    },
    "11": {
      "L": "I overthrew some of you, as when God overthrew Sodom and Gomorrah, and you were like a brand plucked from the burning, yet you did not return to me, says the LORD.",
      "M": "I overthrew some of you as God overthrew Sodom and Gomorrah; you were like a stick snatched from the fire — yet you did not return to me, declares the LORD.",
      "T": "I overthrew some of you the way God overthrew Sodom and Gomorrah; / you were like a smoldering stick yanked from the fire — / and still you did not come back to me. / Yahweh's word."
    },
    "12": {
      "L": "Therefore thus I will do to you, O Israel; and because I will do this to you, prepare to meet your God, O Israel.",
      "M": "Therefore, because I will do this to you, O Israel, prepare yourself to meet your God, Israel.",
      "T": "Therefore this is what I will do to you, Israel — / and because I am doing this to you, / prepare yourself to face your God, O Israel."
    },
    "13": {
      "L": "For behold, the one who forms the mountains and creates the wind and declares to man what is his thought, who makes the morning darkness and treads on the high places of the earth — the LORD, the God of hosts, is his name.",
      "M": "For this is he who forms the mountains and creates the wind, who reveals to humanity what he is thinking, who turns dawn into darkness and strides over the high places of the earth — the LORD, the God of armies, is his name.",
      "T": "For he is the one who shapes the mountains / and stirs the wind into being, / who tells a human being what he is pondering — / who turns the dawn to darkness / and strides over the high places of the earth: / Yahweh, the God of heavenly armies — that is his name."
    }
  },
  "5": {
    "1": {
      "L": "Hear this word that I take up against you as a lamentation, O house of Israel:",
      "M": "Hear this word — the funeral song I take up over you, O house of Israel:",
      "T": "Hear this word — this funeral dirge I raise over you, house of Israel:"
    },
    "2": {
      "L": "Fallen, she shall rise no more — the virgin of Israel; forsaken on her land, with none to raise her up.",
      "M": "She has fallen, never to rise again — the virgin Israel; abandoned on her own land, with no one to lift her up.",
      "T": "She has fallen and will not rise again — / the virgin Israel; / she lies abandoned on her land, / and no one comes to help her up."
    },
    "3": {
      "L": "For thus says the Lord GOD: The city that went out a thousand shall have a hundred remaining, and that which went out a hundred shall have ten remaining to the house of Israel.",
      "M": "For this is what the Lord GOD says: The city that sent out a thousand men will have a hundred survivors; the one that sent out a hundred will have ten left to the house of Israel.",
      "T": "For this is what the Sovereign LORD says: / The city that once sent out a thousand soldiers — / a hundred will come home. / The city that sent a hundred — / ten will survive for the house of Israel."
    },
    "4": {
      "L": "For thus says the LORD to the house of Israel: Seek me and live.",
      "M": "For this is what the LORD says to the house of Israel: Seek me and live.",
      "T": "This is what Yahweh says to the house of Israel: Seek me, and you will live."
    },
    "5": {
      "L": "But do not seek Bethel, and do not enter into Gilgal and do not cross over to Beersheba; for Gilgal shall surely go into exile, and Bethel shall come to nothing.",
      "M": "Do not seek Bethel; do not go to Gilgal or travel to Beersheba — for Gilgal will certainly go into exile, and Bethel will be reduced to nothing.",
      "T": "Do not go to Bethel; / do not go to Gilgal; / do not make the journey to Beersheba — / for Gilgal is going into exile for certain, / and Bethel — the house of God — will become nothing at all."
    },
    "6": {
      "L": "Seek the LORD and live, lest he break out like fire in the house of Joseph and it devour, with none to quench it for Bethel.",
      "M": "Seek the LORD and live, or he will sweep through the house of Joseph like a fire, devouring it with no one to put it out at Bethel.",
      "T": "Seek Yahweh and live — / or he will sweep like fire through the house of Joseph, / devouring it with no one there to quench it — / no one to save Bethel."
    },
    "7": {
      "L": "You who turn justice to wormwood and cast down righteousness to the earth —",
      "M": "You who twist justice into bitter poison and hurl righteousness to the ground —",
      "T": "You who warp justice into bitter wormwood / and throw righteousness into the dirt —"
    },
    "8": {
      "L": "He who made the Pleiades and Orion and turns deep darkness into the morning and darkens the day into night, who calls for the waters of the sea and pours them out on the face of the earth — the LORD is his name.",
      "M": "He who made the Pleiades and Orion, who turns deep darkness into dawn and darkens the day into night, who summons the waters of the sea and pours them over the land — the LORD is his name.",
      "T": "— seek him who made the Pleiades and Orion, / who turns midnight into dawn / and darkens the day to night, / who calls for the waters of the sea / and pours them across the face of the earth — / Yahweh is his name."
    },
    "9": {
      "L": "Who makes destruction flash against the strong so that destruction comes upon the fortress.",
      "M": "He sends destruction flashing against the powerful so that ruin comes upon the fortified city.",
      "T": "He sends ruin flashing against the powerful, / so that destruction falls on the fortress."
    },
    "10": {
      "L": "They hate him who reproves in the gate, and they abhor him who speaks the truth.",
      "M": "They hate the judge who rebukes them at the gate, and they despise the one who tells the truth.",
      "T": "They hate the one who challenges injustice at the city gate; / they loathe the one who speaks straight."
    },
    "11": {
      "L": "Therefore because you trample on the poor and take from him a levy of grain, houses of hewn stone you have built but you shall not dwell in them; pleasant vineyards you have planted but you shall not drink their wine.",
      "M": "Therefore because you crush the poor and impose a grain tax on him, you have built houses of dressed stone but will not live in them; you have planted fine vineyards but will not drink their wine.",
      "T": "Therefore — because you grind the poor into the ground / and levy grain taxes on their backs — / you have built houses of fine-cut stone, / but you will never live in them; / you have planted lush vineyards, / but you will never drink their wine."
    },
    "12": {
      "L": "For I know how many are your transgressions and how great are your sins — you who afflict the righteous, who take bribes and turn aside the poor in the gate.",
      "M": "I know how numerous your crimes are and how great your sins — you who oppress the innocent, accept bribes, and deny justice to the needy at the gate.",
      "T": "I know exactly how many crimes you have — how great your sins are — / you who crush the innocent, take bribes, / and push the poor aside at the gate."
    },
    "13": {
      "L": "Therefore the prudent man keeps silent in such a time, for it is an evil time.",
      "M": "Therefore the wise man stays silent at a time like this, for it is an evil time.",
      "T": "And so the wise stay silent in such a time — / because it is a time of evil."
    },
    "14": {
      "L": "Seek good and not evil, that you may live; and so the LORD, the God of hosts, will be with you, as you have said.",
      "M": "Seek good and not evil, that you may live; and then the LORD, the God of armies, will be with you as you claim.",
      "T": "Seek good and not evil — then you will live; / and the LORD, the God of heavenly armies, will be with you, / as you keep saying he already is."
    },
    "15": {
      "L": "Hate evil and love good, and establish justice in the gate; perhaps the LORD, the God of hosts, will be gracious to the remnant of Joseph.",
      "M": "Hate evil and love good; establish justice at the gate — perhaps the LORD, the God of armies, will be gracious to the remnant of Joseph.",
      "T": "Hate evil, love good, / make justice stand at the city gate — / perhaps then Yahweh, the God of heavenly armies, / will show grace to what remains of Joseph."
    },
    "16": {
      "L": "Therefore thus says the LORD, the God of hosts, the Lord: In all the squares there shall be wailing, and in all the streets they shall say, Alas! Alas! They shall call the farmer to mourning and the skilled mourners to lamentation.",
      "M": "Therefore this is what the LORD, the God of armies, the Lord, says: In all the public squares there will be wailing; in all the streets people will cry, 'Alas! Alas!' Farmers will be summoned to mourn and professional mourners to lead the lament.",
      "T": "And so — this is what Yahweh, the God of heavenly armies, my Lord, declares: / Wailing in every public square; / 'Alas! Alas!' in every street. / The farmers will be called to mourn; / those who know lamentation will be called to lead it."
    },
    "17": {
      "L": "And in all vineyards there shall be wailing, for I will pass through your midst, says the LORD.",
      "M": "There will be wailing in every vineyard, for I will pass through your midst, declares the LORD.",
      "T": "Wailing even in the vineyards — / for I will pass through your midst. / Yahweh has spoken."
    },
    "18": {
      "L": "Woe to you who desire the day of the LORD! Why do you want the day of the LORD? It is darkness and not light.",
      "M": "Woe to you who long for the day of the LORD! Why would you want the day of the LORD? It is darkness, not light.",
      "T": "Woe to those who crave the Day of the LORD! / What do you expect from the Day of the LORD? / It is darkness — not light."
    },
    "19": {
      "L": "As if a man fled from a lion and a bear met him, or went into a house and leaned his hand on the wall and a serpent bit him.",
      "M": "It will be like a man who fled from a lion and ran into a bear, or escaped into his house and put his hand on the wall only to be bitten by a snake.",
      "T": "Like a man who runs from a lion / and is met by a bear — / who escapes into his house / and leans his hand against the wall / only to be bitten by a serpent."
    },
    "20": {
      "L": "Is not the day of the LORD darkness and not light, even very dark with no brightness in it?",
      "M": "Is not the day of the LORD darkness and not light — pitch dark, with no gleam of brightness?",
      "T": "Is the Day of the LORD not darkness, not light — / absolute darkness, without a ray of brightness?"
    },
    "21": {
      "L": "I hate, I despise your feast days, and I take no delight in your solemn assemblies.",
      "M": "I hate and despise your religious festivals; I take no pleasure in your solemn gatherings.",
      "T": "I hate, I utterly despise your festivals; / I take no pleasure in your solemn assemblies."
    },
    "22": {
      "L": "Even though you offer me burnt offerings and grain offerings, I will not accept them; and the peace offerings of your fattened animals, I will not look on them.",
      "M": "Even when you bring me burnt offerings and grain offerings, I will not accept them; when you offer the fellowship offerings of your fattened animals, I will not look at them.",
      "T": "Even if you bring me burnt offerings and grain offerings, / I will not receive them; / even your choice fellowship offerings — / I will not look at them."
    },
    "23": {
      "L": "Take away from me the noise of your songs; to the melody of your harps I will not listen.",
      "M": "Away with the noise of your songs! I will not listen to the music of your harps.",
      "T": "Stop the racket of your songs — / I will not listen to the music of your harps."
    },
    "24": {
      "L": "But let justice roll down like waters and righteousness like an ever-flowing stream.",
      "M": "But let justice roll down like waters, and righteousness like an ever-flowing stream.",
      "T": "Instead — let justice roll down like a river, / and righteousness like a stream that never runs dry."
    },
    "25": {
      "L": "Did you bring me sacrifices and offerings during the forty years in the wilderness, O house of Israel?",
      "M": "Did you bring me sacrifices and offerings during the forty years in the wilderness, O house of Israel?",
      "T": "Was it sacrifices and offerings you brought me / in the forty years of the wilderness, house of Israel?"
    },
    "26": {
      "L": "You shall take up Sikkuth your king and Kiyyun your star-god, your images which you made for yourselves.",
      "M": "You carried your shrine of Sikkuth your king and Kiyyun your star-god — the idols you made for yourselves.",
      "T": "No — you carried your idol-shrines: / Sikkuth your king, / Kiyyun your star-god — / images you had made for yourselves."
    },
    "27": {
      "L": "Therefore I will take you into exile beyond Damascus, says the LORD, whose name is the God of hosts.",
      "M": "Therefore I will send you into exile beyond Damascus, says the LORD, whose name is the God of armies.",
      "T": "Therefore I will drive you into exile beyond Damascus — / so says Yahweh, whose name is the God of heavenly armies."
    }
  },
  "6": {
    "1": {
      "L": "Woe to those who are at ease in Zion and to those who trust in the mountain of Samaria — notable men of the foremost of the nations, to whom the house of Israel comes.",
      "M": "Woe to those who are complacent in Zion and those who feel secure on the mountain of Samaria — the prominent men of the foremost nation, to whom the house of Israel turns.",
      "T": "Woe to those lounging at ease in Zion, / trusting in the security of Samaria's hill — / the leading men of the first among nations, / to whom Israel itself looks."
    },
    "2": {
      "L": "Cross over to Calneh and see; and from there go to Hamath the great; then go down to Gath of the Philistines. Are they better than these kingdoms? Or is their territory greater than your territory?",
      "M": "Cross over to Calneh and look; then go to Hamath the great, and go down to Gath of the Philistines. Are they any better off than these kingdoms? Is their territory any larger than yours?",
      "T": "Go look at Calneh; / go to Hamath the great; / go down to Gath of the Philistines. / Are those kingdoms any better than yours? / Is their territory wider than yours?"
    },
    "3": {
      "L": "You who put far away the day of disaster and bring near the seat of violence.",
      "M": "You who dismiss the day of disaster as far away yet draw the throne of violence close,",
      "T": "You who push the day of disaster out of your minds / while bringing the seat of violence nearer —"
    },
    "4": {
      "L": "who lie on beds of ivory and stretch themselves out on their couches, and eat lambs from the flock and calves from the stall,",
      "M": "who lounge on beds inlaid with ivory and sprawl on their couches, who feast on lambs from the flock and calves from the fattening pen,",
      "T": "who lounge on ivory-inlaid beds / and sprawl across their couches, / feasting on lambs from the flock / and veal from the fattening stalls —"
    },
    "5": {
      "L": "who sing to the sound of the harp and like David devise for themselves instruments of music,",
      "M": "who improvise to the melody of the harp and compose music for themselves like David,",
      "T": "who strum away on the harp / and compose songs for themselves like David —"
    },
    "6": {
      "L": "who drink wine in bowls and anoint themselves with the finest oils, but are not grieved over the ruin of Joseph.",
      "M": "who drink wine by the bowlful and anoint themselves with the finest perfumes — but feel no anguish over the collapse of Joseph.",
      "T": "who drink wine by the bowlful / and douse themselves with expensive oils — / but they feel nothing / for the ruin of Joseph."
    },
    "7": {
      "L": "Therefore they shall now be the first of those who go into exile, and the revelry of those who stretched out shall pass away.",
      "M": "Therefore they will be the first to go into exile, and the revelry of those who sprawl will end.",
      "T": "And so they will be the first ones led away into exile — / the banqueting of those who sprawled will be over."
    },
    "8": {
      "L": "The Lord GOD has sworn by himself — declares the LORD, the God of hosts: I abhor the pride of Jacob and hate his palaces, and I will deliver up the city and all that is in it.",
      "M": "The Lord GOD has sworn by himself — the LORD, the God of armies, declares: I loathe the pride of Jacob and hate his fortresses, and I will hand over the city along with everything in it.",
      "T": "The Sovereign LORD has sworn — by himself — / so Yahweh, the God of heavenly armies, declares: / I am revolted by Jacob's pride; / I hate his citadels. / I will hand over the city and everything in it."
    },
    "9": {
      "L": "And it shall come to pass, if ten men remain in one house, they shall die.",
      "M": "And if ten men are left in a single house, they will all die.",
      "T": "And if ten people survive in one house, they will all die."
    },
    "10": {
      "L": "And when a man's uncle, the one who burns him, comes to bring the bones out of the house and calls to someone in the innermost part of the house, Is there still anyone with you? he will say, No. And he will say, Silence — we must not mention the name of the LORD.",
      "M": "When a relative who must prepare the body comes to carry the bones out of the house and asks the person in the back room, 'Is there anyone still with you?' the answer will be, 'No.' Then he says, 'Say nothing — we must not mention the name of the LORD.'",
      "T": "When a relative comes to burn the body and carry the bones from the house, / and calls to someone still hiding inside: 'Is there anyone else with you?' — / the answer comes back: 'No, no one.' / Then he says: 'Silence — / we must not invoke the name of Yahweh.'"
    },
    "11": {
      "L": "For behold, the LORD commands and the great house shall be struck down into ruins and the little house into fragments.",
      "M": "For the LORD has commanded: the great house will be smashed to rubble and the small house to pieces.",
      "T": "For the LORD has issued his command: / the great house will be smashed to rubble; / the small house, to splinters."
    },
    "12": {
      "L": "Do horses run on rock? Does one plow rock with oxen? Yet you have turned justice into poison and the fruit of righteousness into wormwood.",
      "M": "Can horses gallop on bare rock? Can one plow rock with oxen? Yet you have turned justice into poison and the fruit of righteousness into bitter wormwood.",
      "T": "Horses don't gallop on bare rock; / oxen don't plow stone. / But you have turned justice into poison / and righteousness into bitter wormwood."
    },
    "13": {
      "L": "You who rejoice in Lo-debar, who say, Have we not taken Karnaim for ourselves by our own strength?",
      "M": "You who celebrate the capture of Lo-debar and boast, 'Have we not taken Karnaim for ourselves by our own strength?'",
      "T": "You who celebrate your conquest of Lo-debar — Nothing! — / and boast: 'Have we not seized Karnaim, the Two Horns, / by our own power?'"
    },
    "14": {
      "L": "For behold, I will raise up against you a nation, O house of Israel, says the LORD, the God of hosts; and they shall oppress you from Lebo-hamath to the brook of the Arabah.",
      "M": "For I am about to raise up a nation against you, O house of Israel, declares the LORD, the God of armies; and they will oppress you from Lebo-hamath to the Wadi of the Arabah.",
      "T": "For look — I am raising up a nation against you, house of Israel — / so Yahweh, the God of heavenly armies, declares — / and they will press you hard / from the entrance of Hamath to the Wadi of the Arabah."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'amos')
        merge_tier(existing, AMOS, tier_key)
        save(tier_dir, 'amos', existing)
    print('Amos 1–6 written.')

if __name__ == '__main__':
    main()
