"""
MKT Amos chapters 7–9 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-amos-7-9.py

=== CHAPTER OVERVIEW ===

Amos is a shepherd from Tekoa in Judah who is called to prophesy to the northern
kingdom of Israel during the reign of Jeroboam II (c. 760–750 BCE), a time of
economic prosperity masking deep injustice. Chapters 1–6 open with oracles against
the nations, then turn to Israel's own crimes. Chapters 7–9 are structured around
five visionary sequences and a biographical interlude.

Chapter 7: Three Visions + Confrontation with Amaziah.
  vv.1–3: First vision — locusts devouring the land. Amos intercedes; Yahweh relents.
  vv.4–6: Second vision — judgment by fire consuming the deep. Amos intercedes; Yahweh relents.
  vv.7–9: Third vision — the plumb line. No intercession this time; judgment is set.
  vv.10–17: Biographical interlude. Amaziah the priest of Bethel, alarmed by Amos's
    words about Jeroboam, orders him to leave. Amos explains his call — not a
    professional prophet but a shepherd taken directly by Yahweh — and pronounces
    judgment on Amaziah's household and land.

Chapter 8: Fourth Vision + Woes Against Unjust Commerce.
  vv.1–3: Fourth vision — a basket of summer fruit. A wordplay on qayits (summer fruit)
    / qets (end/ruin) signals Israel is "ripe" for judgment.
  vv.4–14: Indictment of merchants who exploit the poor, use false weights, and swear
    by the idols of Dan and Beersheba. The covenant God will bring silence,
    cosmic darkness, and an unprecedented famine — not of bread, but of his word.

Chapter 9: Fifth Vision + Inescapable Judgment + Restoration.
  vv.1–4: Fifth vision — Yahweh standing at the altar commanding total destruction.
    No escape: not underground, not in heaven, not on Carmel, not in the sea,
    not in exile.
  vv.5–6: Doxological interlude affirming Yahweh's sovereign power over creation.
  vv.7–10: Israel is no more privileged than the Cushites; the sinful kingdom will
    be destroyed. Yet the house of Jacob will not be utterly annihilated.
  vv.11–15: Restoration promise — the fallen booth of David raised up; the nations
    bearing Israel's name restored; unimaginable agricultural abundance; the
    exiles replanted on their own land, never to be uprooted again.

=== CONTESTED-TERM DECISIONS ===

- H3068 (יהוה / Yahweh): Following the Joel/Hosea convention established in
  mkt-joel-1-3.py and mkt-hosea-1-6.py. L/M: "LORD" (small-caps convention in plain
  text). T: "Yahweh" in prophetic-oracle and covenantally weighted contexts (visions,
  divine speech, oracles); "the LORD" in narrative contexts.

- H136 (אֲדֹנָי / Adonai, "the Lord / master"): "the Lord" in all three tiers,
  referring to Yahweh's sovereignty as master and ruler.

- H3069 + H136 combination (אֲדֹנָי יְהוִה / Adonai-YHWH): In Amos, the combination
  of H136 and H3069 (the ketiv form of YHWH used after Adonai to avoid
  "Adonai Adonai") renders as KJV "Lord GOD." L/M: "Lord GOD" (standard convention).
  T: "Lord Yahweh." This combination appears at 7:1, 2, 4, 5, 6; 8:1, 3, 9, 11;
  9:5, 8.

- H594 (אֲנָךְ / anak, "plumb line"): Traditional rendering "plumb line" in all tiers.
  Some scholars propose this Akkadian loanword means "tin/lead" rather than a
  plumb line per se, but the building/measuring context and ancient versions
  (LXX: adamant/diamond) all point to a measuring instrument. "Plumb line"
  is maintained for all tiers as it best captures the function of the object.

- H5521 (סֻכָּה / sukkah, "booth/tabernacle"): At 9:11 "the booth of David."
  The sukkah was a temporary shelter — Amos uses it to describe the Davidic
  dynasty as a fallen hut. L: "tabernacle" (KJV tradition; this is also the
  term used in Acts 15:16 LXX). M: "booth." T: "fallen shelter" — surfaces
  the image of a once-great structure reduced to a hut in disrepair.

- Wordplay H7019 qayits / H7093 qets (8:2): The Hebrew creates a sonic pun —
  "summer fruit" (qayits) sounds like "end" (qets). The vision is a divine
  pun: looking at ripe fruit, Amos is told the "end" has come. L/M render
  literally with a parenthetical note; T surfaces the wordplay explicitly in
  the translation prose.

- H5986 (Amos, 7:14): The Hebrew phrase "lo-nabi anoki" is verbless in Hebrew
  and could be translated either "I am not a prophet" (present) or "I was not a
  prophet" (past). Context favours the present: Amos is denying being a
  professional member of the prophetic guilds (bene ha-nevi'im), not denying
  a past state. L/M: "I am not a prophet"; T explains the guild distinction.
  This is consistent with many modern translations (ESV, NRSV, NIV).

- H3569 (כּוּשִׁי / Kushi, "Cushite/Ethiopian"): The Cushites were Nubians
  (modern Sudan/Ethiopia region). L: "Ethiopians" (traditional KJV). M/T:
  "Cushites" (more accurate ethnic/geographic rendering for modern readers).

- H5002 (נְאֻם / ne'um, "utterance/oracle"): This is the prophetic attestation
  formula, literally "the oracle of / the utterance of." L: "saith." M/T:
  "declares." This follows the Joel pattern.

- Poetic structure: Amos is largely poetic. In the T tier, the vision accounts
  (7:1–9, 8:1–3, 9:1–6), the hymnic doxologies (9:5–6), and the prophetic
  oracles (7:9, 7:17, 8:4–14, 9:7–15) are rendered with line breaks to preserve
  prophetic cadence. M uses flowing prose. L preserves source word order.

- Divine passive: Several destructive acts in the vision sequences imply Yahweh
  as the unnamed agent. L/M render passives as passives; T may make divine
  agency explicit where context warrants.

- Aspect notes:
  - Perfect verbs in divine speech (7:9, 7:17, 8:9–10) = prophetic perfect;
    rendered as English future in L/M to match the predictive context.
    T may use present tense to heighten the sense of inevitability.
  - The repeated formula "I will not pass by them again" (7:8; 8:2) = Yahweh's
    withdrawal of mercy; aspect is cessative perfect + negative.

- OT intertextuality:
  - 9:11–12 is cited in Acts 15:16–17 (LXX version), applied to the inclusion
    of the Gentiles. T renders the restoration promise with its full eschatological
    weight.
  - 9:13 echoes Joel 3:18 — the "mountains dripping sweet wine" image. Both texts
    envision eschatological abundance.
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
    "7": {
        "1": {
            "L": "Thus hath the Lord GOD shewed unto me; and behold, he formed grasshoppers in the beginning of the shooting up of the latter growth; and lo, it was the latter growth after the king's mowings.",
            "M": "This is what the Lord GOD showed me: he was forming locusts at the time the latter growth was beginning to sprout — the second crop after the king's mowings.",
            "T": "This is what the Lord Yahweh showed me:\nhe was forming swarms of locusts\nat the moment the late grass began to shoot up —\nthe second crop that comes after the king takes the first cutting."
        },
        "2": {
            "L": "And it came to pass that when they had made an end of eating the grass of the land, then I said: O Lord GOD, forgive, I beseech thee; by whom shall Jacob arise? for he is small.",
            "M": "And when they had finished eating the grass of the land, I said: 'O Lord GOD, please forgive! How can Jacob stand? For he is so small!'",
            "T": "When the locusts had stripped every blade of grass from the land,\nI cried out: 'O Lord Yahweh, forgive!\nHow will Jacob survive? He is so small!'"
        },
        "3": {
            "L": "The LORD repented for this: It shall not be, saith the LORD.",
            "M": "The LORD relented concerning this: 'It shall not be,' said the LORD.",
            "T": "Yahweh relented.\n'This will not happen,' said Yahweh."
        },
        "4": {
            "L": "Thus hath the Lord GOD shewed unto me; and behold, the Lord GOD called to contend by fire; and it devoured the great deep, and did eat up a part.",
            "M": "This is what the Lord GOD showed me: the Lord GOD was summoning a judgment by fire, and it devoured the great deep and was consuming the land.",
            "T": "This is what the Lord Yahweh showed me:\nthe Lord Yahweh was calling for judgment by fire —\nit swallowed up the great deep\nand was beginning to devour the land itself."
        },
        "5": {
            "L": "Then said I: O Lord GOD, cease, I beseech thee; by whom shall Jacob arise? for he is small.",
            "M": "Then I said: 'O Lord GOD, stop, I pray! How can Jacob stand? For he is so small!'",
            "T": "I cried out again: 'Stop, O Lord Yahweh!\nHow will Jacob survive? He is so small!'"
        },
        "6": {
            "L": "The LORD repented for this also: This also shall not be, saith the Lord GOD.",
            "M": "The LORD relented concerning this as well: 'This also shall not be,' said the Lord GOD.",
            "T": "Yahweh relented of this too.\n'This will not happen either,' said the Lord Yahweh."
        },
        "7": {
            "L": "Thus he shewed me; and behold, the Lord stood upon a wall made by a plumbline, with a plumbline in his hand.",
            "M": "This is what he showed me: the Lord was standing beside a wall that had been built true to plumb, with a plumb line in his hand.",
            "T": "This is what he showed me:\nthe Lord was standing beside a wall built straight by a plumb line,\nand he was holding a plumb line in his hand."
        },
        "8": {
            "L": "And the LORD said unto me: Amos, what seest thou? And I said: A plumbline. Then said the Lord: Behold, I will set a plumbline in the midst of my people Israel; I will not again pass by them any more.",
            "M": "The LORD said to me: 'Amos, what do you see?' I said: 'A plumb line.' Then the Lord said: 'Behold, I am setting a plumb line in the midst of my people Israel; I will no longer pass by them.'",
            "T": "'Amos, what do you see?' Yahweh asked.\n'A plumb line,' I answered.\nThen the Lord declared:\n'I am setting a plumb line against my people Israel —\nthey do not measure up.\nI will not spare them again.'"
        },
        "9": {
            "L": "And the high places of Isaac shall be desolate, and the sanctuaries of Israel shall be laid waste; and I will rise against the house of Jeroboam with the sword.",
            "M": "The high places of Isaac shall be made desolate, and the sanctuaries of Israel shall be laid waste; I will rise against the house of Jeroboam with the sword.",
            "T": "The high shrines of Isaac will be laid waste;\nIsrael's sanctuaries will be brought to ruin.\nI will rise against the royal house of Jeroboam with the sword."
        },
        "10": {
            "L": "Then Amaziah the priest of Bethel sent to Jeroboam king of Israel, saying: Amos hath conspired against thee in the midst of the house of Israel; the land is not able to bear all his words.",
            "M": "Then Amaziah the priest of Bethel sent word to Jeroboam king of Israel: 'Amos has conspired against you in the midst of the house of Israel; the land cannot endure all his words.'",
            "T": "Then Amaziah, the priest of Bethel, sent a message to Jeroboam king of Israel:\n'Amos is raising a conspiracy against you right here in Israel.\nThe land cannot bear everything he is saying.'"
        },
        "11": {
            "L": "For thus Amos saith: Jeroboam shall die by the sword, and Israel shall surely be led away captive out of their own land.",
            "M": "For Amos has said: 'Jeroboam shall die by the sword, and Israel shall surely go into exile away from its land.'",
            "T": "For Amos has been saying:\n'Jeroboam will die by the sword,\nand Israel will be carried into exile from its own land.'"
        },
        "12": {
            "L": "Also Amaziah said unto Amos: O thou seer, go, flee thee away into the land of Judah, and there eat bread, and prophesy there.",
            "M": "And Amaziah said to Amos: 'Get out, O seer! Flee to the land of Judah, earn your bread there, and prophesy there.'",
            "T": "Amaziah then spoke directly to Amos:\n'Get out of here, prophet — go back to Judah.\nEarn your living there and do your prophesying there.'"
        },
        "13": {
            "L": "But prophesy not again any more at Bethel; for it is the king's chapel, and it is the king's court.",
            "M": "But never prophesy again at Bethel, for it is the king's sanctuary and a royal palace.",
            "T": "But you will not prophesy here at Bethel again —\nthis is the king's own sanctuary, a royal house."
        },
        "14": {
            "L": "Then answered Amos, and said to Amaziah: I am no prophet, neither am I a prophet's son; but I am an herdman, and a gatherer of sycomore fruit.",
            "M": "Then Amos answered Amaziah: 'I am not a prophet, nor a prophet's son; I am a herdsman and a dresser of sycamore figs.'",
            "T": "Amos answered Amaziah:\n'I am not a prophet. I belong to no prophet's guild.\nI am a sheep-breeder — a dresser of sycamore figs.\nI have no professional standing here.'"
        },
        "15": {
            "L": "And the LORD took me as I followed the flock, and the LORD said unto me: Go, prophesy unto my people Israel.",
            "M": "But the LORD took me from following the flock, and the LORD said to me: 'Go, prophesy to my people Israel.'",
            "T": "But Yahweh took me from behind the flock\nand Yahweh said to me:\n'Go — prophesy to my people Israel.'"
        },
        "16": {
            "L": "Now therefore hear thou the word of the LORD: Thou sayest, Prophesy not against Israel, and drop not thy word against the house of Isaac.",
            "M": "Now therefore hear the word of the LORD. You say: 'Do not prophesy against Israel, and do not speak against the house of Isaac.'",
            "T": "So now — hear the word of Yahweh.\nYou say to me: 'Do not prophesy against Israel;\nstop preaching against the house of Isaac.'"
        },
        "17": {
            "L": "Therefore thus saith the LORD: Thy wife shall be an harlot in the city, and thy sons and thy daughters shall fall by the sword, and thy land shall be divided by line; and thou shalt die in a polluted land; and Israel shall surely go into captivity forth of his land.",
            "M": "Therefore thus says the LORD: 'Your wife shall be a prostitute in the city; your sons and your daughters shall fall by the sword; your land shall be divided up with the surveyor's line; and you yourself shall die in an unclean land; and Israel shall surely go into exile away from its land.'",
            "T": "Therefore this is what Yahweh says:\nYour wife will become a prostitute right in this city.\nYour sons and daughters will be cut down by the sword.\nYour land will be marked off and handed out to strangers.\nYou yourself will die in an unclean, foreign land —\nand Israel will be dragged into exile from its own homeland."
        }
    },
    "8": {
        "1": {
            "L": "Thus hath the Lord GOD shewed unto me; and behold, a basket of summer fruit.",
            "M": "This is what the Lord GOD showed me: a basket of ripe summer fruit.",
            "T": "This is what the Lord Yahweh showed me:\na basket of ripe summer fruit."
        },
        "2": {
            "L": "And he said: Amos, what seest thou? And I said: A basket of summer fruit. Then said the LORD unto me: The end is come upon my people of Israel; I will not again pass by them any more.",
            "M": "He said: 'Amos, what do you see?' I said: 'A basket of summer fruit.' Then the LORD said to me: 'The end has come upon my people Israel; I will no longer pass by them.'",
            "T": "'Amos, what do you see?' he asked.\n'A basket of ripe summer fruit,' I said.\nThen Yahweh said:\n'Summer fruit is ripe — and so is the end.\nThe end has come upon my people Israel;\nI will not spare them again.'"
        },
        "3": {
            "L": "And the songs of the temple shall be howlings in that day, saith the Lord GOD; there shall be many dead bodies; in every place they shall cast them forth with silence.",
            "M": "'In that day,' declares the Lord GOD, 'the songs of the temple will become wailings. The dead will be many; in every place they shall be cast out in silence.'",
            "T": "'On that day,' declares the Lord Yahweh,\n'the singing in the temple will turn to wailing.\nCorpses will be everywhere —\ncast out in every direction.\nNothing but silence.'"
        },
        "4": {
            "L": "Hear this, O ye that swallow up the needy, even to make the poor of the land to fail,",
            "M": "Hear this, you who trample on the needy and bring the poor of the land to ruin —",
            "T": "Listen to this — you who crush the needy\nand grind down the poor of the land —"
        },
        "5": {
            "L": "Saying: When will the new moon be gone, that we may sell corn? and the sabbath, that we may set forth wheat, making the ephah small, and the shekel great, and falsifying the balances by deceit?",
            "M": "saying, 'When will the new moon be over so we can sell grain? When will the sabbath end so we can market the wheat — making the measure small and the price high, cheating with dishonest scales?'",
            "T": "You cannot wait for the holy days to end.\n'When will the new moon be over?\nWhen will the sabbath pass\nso we can put our wheat on the market —\nwith rigged measures and inflated prices\nand scales tipped against the buyer?'"
        },
        "6": {
            "L": "That we may buy the poor for silver, and the needy for a pair of shoes; yea, and sell the refuse of the wheat?",
            "M": "buying the poor for silver and the needy for a pair of sandals, and selling the chaff of the grain?",
            "T": "Buying the desperate poor for a handful of coins,\nthe needy for a pair of sandals —\nand then selling them the swept-up floor-dust as if it were grain."
        },
        "7": {
            "L": "The LORD hath sworn by the excellency of Jacob: Surely I will never forget any of their works.",
            "M": "The LORD has sworn by the pride of Jacob: 'Surely I will never forget any of their deeds.'",
            "T": "Yahweh has taken an oath by the pride of Jacob himself:\n'Not one of these deeds will I forget — not one.'"
        },
        "8": {
            "L": "Shall not the land tremble for this, and every one mourn that dwelleth therein? and it shall rise up wholly as a flood; and it shall be cast out and drowned, as by the flood of Egypt.",
            "M": "Shall not the land tremble on account of this, and everyone who dwells in it mourn? All of it will rise up like the Nile, tossing and sinking again, like the Nile of Egypt.",
            "T": "Will the land not shake for this?\nWill not everyone in it grieve?\nThe whole earth will heave like the Nile in flood —\nswelling, churning, then sinking,\nthe way the Nile rises and falls."
        },
        "9": {
            "L": "And it shall come to pass in that day, saith the Lord GOD, that I will cause the sun to go down at noon, and I will darken the earth in the clear day.",
            "M": "'In that day,' declares the Lord GOD, 'I will cause the sun to go down at noon and darken the earth in broad daylight.'",
            "T": "'On that day,' declares the Lord Yahweh,\n'I will bring the sun down at noon —\nI will drench the earth in darkness at midday.'"
        },
        "10": {
            "L": "And I will turn your feasts into mourning, and all your songs into lamentation; and I will bring up sackcloth upon all loins, and baldness upon every head; and I will make it as the mourning of an only son, and the end thereof as a bitter day.",
            "M": "'I will turn your feasts into mourning and all your songs into lamentation; I will put sackcloth on every waist and shave every head; I will make it like the mourning for an only son — and the end of it like a bitter day.'",
            "T": "'I will turn your festivals into funerals\nand every song into a dirge.\nSackcloth on every body; shaved heads everywhere.\nThe grief will be like a father's grief for his only son —\nand it will end as bitterly as it began.'"
        },
        "11": {
            "L": "Behold, the days come, saith the Lord GOD, that I will send a famine in the land, not a famine of bread, nor a thirst for water, but of hearing the words of the LORD.",
            "M": "'Behold, the days are coming,' declares the Lord GOD, 'when I will send a famine on the land — not a famine of bread, nor a thirst for water, but of hearing the words of the LORD.'",
            "T": "'The days are coming,' declares the Lord Yahweh,\n'when I will send a famine across the land —\nnot hunger for bread, not thirst for water,\nbut a famine of hearing Yahweh's own word.'"
        },
        "12": {
            "L": "And they shall wander from sea to sea, and from the north even to the east; they shall run to and fro to seek the word of the LORD, and shall not find it.",
            "M": "They shall wander from sea to sea, and from north to east; they will run to and fro, seeking the word of the LORD, and they shall not find it.",
            "T": "People will stagger from sea to sea,\nfrom north to east, searching everywhere —\nrunning to and fro, desperately seeking a word from Yahweh.\nThey will not find one."
        },
        "13": {
            "L": "In that day shall the fair virgins and young men faint for thirst.",
            "M": "'In that day the beautiful young women and the young men shall faint from thirst.'",
            "T": "The finest young women, the strongest young men —\non that day they will collapse from thirst."
        },
        "14": {
            "L": "They that swear by the sin of Samaria, and say: The life of thy god, O Dan; and, The manner of Beersheba liveth; even they shall fall, and never rise up again.",
            "M": "Those who swear by the guilt of Samaria, who say 'As your god lives, O Dan!' or 'As the way of Beersheba lives!' — they shall fall and never rise again.",
            "T": "All who swear by the idol-shame of Samaria,\nwho take their oaths by the calf at Dan —\n'As your god lives!' —\nor make their vows by the pilgrimage at Beersheba —\nthey will fall and never get up again."
        }
    },
    "9": {
        "1": {
            "L": "I saw the Lord standing upon the altar; and he said: Smite the lintel of the door, that the posts may shake; and cut them in the head, all of them; and I will slay the last of them with the sword; he that fleeth of them shall not flee away, and he that escapeth of them shall not be delivered.",
            "M": "I saw the Lord standing beside the altar, and he said: 'Strike the capital so that the thresholds shake; break them off on the heads of all the people; and those who remain I will kill with the sword. Not one shall flee and get away; not one shall escape and survive.'",
            "T": "I saw the Lord himself standing beside the altar.\nHe commanded:\n'Strike the capitals — let the thresholds shudder!\nBring them down on the heads of all who are there.\nWhoever survives I will hunt down with the sword.\nNot one shall make it out. Not one.'"
        },
        "2": {
            "L": "Though they dig into hell, thence shall mine hand take them; though they climb up to heaven, thence will I bring them down.",
            "M": "'If they dig into Sheol, from there my hand shall take them; if they climb up to the heavens, from there I will bring them down.'",
            "T": "'They can dig all the way down to the world of the dead —\nmy hand will reach them there.\nThey can climb to the highest heaven —\nI will drag them back down.'"
        },
        "3": {
            "L": "And though they hide themselves in the top of Carmel, I will search and take them out thence; and though they be hid from my sight in the bottom of the sea, thence will I command the serpent, and he shall bite them.",
            "M": "'Though they hide on the top of Carmel, I will search them out and take them from there; and if they hide from my sight on the floor of the sea, I will command the serpent there, and it shall bite them.'",
            "T": "'They can conceal themselves on the summit of Carmel —\nI will hunt them down and drag them out.\nIf they sink to the bottom of the sea to hide from me,\nI will send the sea-serpent after them.\nIt will bite them.'"
        },
        "4": {
            "L": "And though they go into captivity before their enemies, thence will I command the sword, and it shall slay them; and I will set mine eyes upon them for evil, and not for good.",
            "M": "'Though they go into captivity before their enemies, there I will command the sword, and it shall kill them; I will set my eyes upon them for harm and not for good.'",
            "T": "'Even if their enemies march them into exile,\nI will send the sword after them there —\nit will cut them down.\nI will keep my eye on them —\nbut for disaster, not for good.'"
        },
        "5": {
            "L": "And the Lord GOD of hosts is he that toucheth the land and it shall melt, and all that dwell therein shall mourn; and it shall rise up wholly like a flood; and shall be drowned, as by the flood of Egypt.",
            "M": "The Lord GOD of hosts — he who touches the earth and it melts, so that all who dwell in it mourn; it rises up wholly like the Nile and sinks again, like the Nile of Egypt.",
            "T": "The Lord Yahweh of armies —\nhe touches the earth and it dissolves;\nevery one living on it mourns.\nThe whole land heaves like the Nile,\nrises and falls like Egypt's great river —"
        },
        "6": {
            "L": "It is he that buildeth his stories in the heaven, and hath founded his troop in the earth; he that calleth for the waters of the sea, and poureth them out upon the face of the earth: The LORD is his name.",
            "M": "He who builds his upper chambers in the heavens and has founded his vault upon the earth; who calls for the waters of the sea and pours them out upon the face of the earth — the LORD is his name.",
            "T": "the one who builds his high palace in the heavens\nand sets its foundations upon the earth,\nwho summons the waters of the sea\nand pours them across the face of the earth —\nYahweh is his name."
        },
        "7": {
            "L": "Are ye not as children of the Ethiopians unto me, O children of Israel? saith the LORD. Have not I brought up Israel out of the land of Egypt? and the Philistines from Caphtor, and the Syrians from Kir?",
            "M": "'Are you not like the Cushites to me, O people of Israel?' declares the LORD. 'Did I not bring Israel up from the land of Egypt, and the Philistines from Caphtor, and the Syrians from Kir?'",
            "T": "'Do you think you are uniquely precious to me, O Israel?' declares Yahweh.\n'Yes, I brought you up from Egypt —\nbut I also brought the Philistines from Caphtor\nand the Syrians from Kir.\nYou are no more to me than the Cushites.'"
        },
        "8": {
            "L": "Behold, the eyes of the Lord GOD are upon the sinful kingdom, and I will destroy it from off the face of the earth; saving that I will not utterly destroy the house of Jacob, saith the LORD.",
            "M": "'Behold, the eyes of the Lord GOD are upon the sinful kingdom, and I will destroy it from the face of the earth — except that I will not utterly destroy the house of Jacob,' declares the LORD.",
            "T": "'Look — the eyes of the Lord Yahweh are fixed\non this sinful kingdom.\nI will wipe it off the face of the earth.\nAnd yet — I will not completely annihilate the house of Jacob,'\ndeclares Yahweh."
        },
        "9": {
            "L": "For lo, I will command, and I will sift the house of Israel among all nations, like as corn is sifted in a sieve, yet shall not the least grain fall upon the earth.",
            "M": "'For behold, I will command and sift the house of Israel among all the nations, as one sifts grain in a sieve — but not one kernel shall fall to the ground.'",
            "T": "'Here is what I will do:\nI will shake the house of Israel through every nation —\nthe way grain is shaken in a sieve.\nBut not one good kernel will be lost to the ground.'"
        },
        "10": {
            "L": "All the sinners of my people shall die by the sword, which say: The evil shall not overtake nor prevent us.",
            "M": "'All the sinners among my people shall die by the sword — all who say: \"Disaster will never overtake or confront us.\"'",
            "T": "'Every sinner among my people will die by the sword —\nespecially those who keep telling themselves:\n\"Nothing bad will ever reach us. Disaster cannot touch us.\"'"
        },
        "11": {
            "L": "In that day will I raise up the tabernacle of David that is fallen, and close up the breaches thereof; and I will raise up his ruins, and I will build it as in the days of old.",
            "M": "'In that day I will raise up the fallen booth of David; I will repair its breaches and raise up its ruins, and rebuild it as it was in the days of old —'",
            "T": "'On that day I will raise up\nthe fallen shelter of David —\npatch every broken wall,\nlift up what has collapsed,\nand rebuild it as it stood in days of old —'"
        },
        "12": {
            "L": "That they may possess the remnant of Edom, and of all the heathen, which are called by my name, saith the LORD that doeth this.",
            "M": "'so that they may possess the remnant of Edom and all the nations that are called by my name,' declares the LORD who does this.",
            "T": "'so that Israel may reclaim the remnant of Edom\nand all the nations over whom my name has been called,'\ndeclares Yahweh, who is doing all of this."
        },
        "13": {
            "L": "Behold, the days come, saith the LORD, that the plowman shall overtake the reaper, and the treader of grapes him that soweth seed; and the mountains shall drop sweet wine, and all the hills shall melt.",
            "M": "'Behold, the days are coming,' declares the LORD, 'when the plowman shall overtake the reaper and the treader of grapes him who sows the seed; the mountains shall drip with sweet wine, and all the hills shall flow.'",
            "T": "'The days are coming,' declares Yahweh,\n'when the plowman will catch up with the reaper —\nso fast will the harvests follow —\nand the grape-treader will overtake the one who sows the seed.\nThe mountains will run with new wine;\nevery hill will flow with it.'"
        },
        "14": {
            "L": "And I will bring again the captivity of my people of Israel, and they shall build the waste cities, and inhabit them; and they shall plant vineyards, and drink the wine thereof; they shall also make gardens, and eat the fruit of them.",
            "M": "'I will restore the fortunes of my people Israel; they shall rebuild the ruined cities and inhabit them; they shall plant vineyards and drink their wine; they shall make gardens and eat their fruit.'",
            "T": "'I will bring my people Israel back from captivity.\nThey will rebuild the cities left in ruins and settle in them.\nThey will plant vineyards — and drink the wine.\nThey will cultivate gardens — and eat what they grow.'"
        },
        "15": {
            "L": "And I will plant them upon their land, and they shall no more be pulled up out of their land which I have given them, saith the LORD thy God.",
            "M": "'I will plant them on their land, and they shall never again be uprooted from the land that I have given them,' says the LORD your God.",
            "T": "'I will plant them firmly in their own land,\nand they will never be pulled up from it again —\nfrom the land I have given them,'\nsays Yahweh your God."
        }
    }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'amos')
        merge_tier(existing, AMOS, tier_key)
        save(tier_dir, 'amos', existing)
    print('Amos 7–9 written.')

if __name__ == '__main__':
    main()
