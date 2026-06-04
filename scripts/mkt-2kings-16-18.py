"""
MKT 2 Kings chapters 16–18 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-2kings-16-18.py

Translation decisions:
- H3068 (יהוה): "LORD" (small-caps convention) in L/M throughout; "the LORD" in T.
  Consistent with all prior 2 Kings scripts.
- H430 (אֱלֹהִים): "God" in all tiers. Used as title throughout this range.
- H982 (בָּטַח): "trust/trusted" — the key term evaluated in 18:5. The same root (בִּטָּחוֹן)
  appears in the Rabshakeh's speech (18:19-25,30), turning Hezekiah's defining virtue into
  the target of psychological attack. L: "trust"; M: "trust/rely on"; T surfaces the
  relational-covenantal weight of the word.
- H1116 (בָּמָה): "high places" throughout. Hezekiah's removal of them (18:4) is the highest
  praise any Judean king received for cultic faithfulness.
- H842 (אֲשֵׁרָה): "Asherah pole(s)" in L/M (the cult object); T notes the goddess dimension
  where relevant.
- H5178 (נְחֹשֶׁת) / Nehushtan (18:4): L/M: "Nehushtan"; T explains that the name is
  Hezekiah's contemptuous dismissal — nəḥōšet = just a bronze thing — of an object with a
  legitimate Mosaic origin (Num 21:8-9) that had become an idol. The destruction is
  the act of a king clear-eyed enough to dismantle even a venerable sacred object.
- H1285 (בְּרִית): "covenant" where it occurs (17:15,35,38). The covenant terminology
  in 17:7-23 is dense and carefully distinguished: statutes, ordinances, laws, commandments,
  covenant — each carries distinct legal weight. L preserves the distinctions.
- H8451 (תּוֹרָה) and related terms in 17:13,34-40: "law" / "commandment" / "statute" /
  "ordinance" / "testimony" — each Hebrew term preserved distinctly, not collapsed.
- H5674 (עָבַר) in the fire (16:3): "pass through the fire" in L/M; T: "offered his own
  son in the fire" — the Molech child-sacrifice connection is surfaced explicitly.
- H4196 (מִזְבֵּח): "altar" throughout. Chapter 16 turns on the displacement of the bronze
  altar (commanded by God) by Ahaz's Aramean import. L preserves the contrast.
- H5930 (עֹלָה): "burnt offering"; H4503 (מִנְחָה): "grain offering";
  H8002 (שֶׁלֶם): "peace offering"; H5262 (נֶסֶךְ): "drink offering" — all kept distinct,
  matching the standard sacrificial vocabulary used throughout Kings.
- H7965 (שָׁלוֹם): "peace" in the Rabshakeh's speech (18:31,36) and in the messengers'
  query formula. The Rabshakeh weaponizes the vocabulary of covenant peace.
- H1697 (דָּבָר) + prophetic word: 17:13,23 — the prophetic word as historical causation.
  T surfaces the phrase "nothing of the word of the LORD shall fall" (cf. 10:10).
- H2090 / H5438 — "conspiracy" (17:4): Hoshea's secret embassy to Egypt is the act that
  triggers Assyrian reprisal. The word used (קֶשֶׁר) = a binding together, a plot.
- Aspect decisions:
  - Wayyiqtol (waw-consecutive imperfect) = narrative past throughout.
  - 17:7-23: The extended theological commentary shifts register; qatal perfects = completed
    acts viewed as a whole; the "they did / they rejected / they served" series is iterative
    perfect, rendered in English simple past.
  - Rabshakeh's speech (18:19-35): interrogative, imperative, and conditional forms preserved.
    His speech is masterful rhetoric; the three arguments (Egypt is unreliable; the LORD is
    alienated; no god has ever stopped Assyria) must retain their rhetorical force in M and T.
- OT intertextuality:
  - 16:3: Ahaz's child sacrifice echoes the abominations of the pre-conquest nations
    (Deut 18:10); the same act condemned in the surrounding nations is now practiced by the
    king of Judah. T notes the inversion.
  - 17:7-23: The entire passage is a Deuteronomistic theology-of-exile summary, echoing
    Deut 28 (covenant curses), Deut 4:25-28 (exile as consequence of idolatry), and
    Deut 32 (God's testimony against Israel). T tier reads it as the narrator's sermon.
  - 17:14: "hardened their necks" echoes Exod 32:9 (golden calf), Deut 9:6,13 — Israel's
    persistent character flaw from the wilderness onward.
  - 17:15: "went after vanity and became vain" — a theological principle: we become like
    what we worship. The idols are hevel (breath, vanity); those who serve them become hevel.
  - 17:18: "removed them from his sight" echoes the Cain narrative (Gen 4:16) and the Eden
    expulsion — exile as un-creation.
  - 18:4: Nehushtan's destruction — the bronze serpent of Num 21:8-9 had saved Israel's
    life in the wilderness; centuries later it had become an object of incense-burning.
    The legitimate instrument of grace had become a snare. Hezekiah's act is iconoclasm
    in the service of covenant purity.
  - 18:5: "none like him among all the kings of Judah" — the superlative is echoed in 23:25
    (Josiah). Both are the highest possible evaluations; they assess different qualities:
    Hezekiah for trust (בָּטַח), Josiah for covenant-keeping (Deut 6:5 language).
  - 18:6: "clave to the LORD" — דָּבַק, the same covenant-loyalty verb as Deut 10:20;
    11:22; Ruth 1:14.
  - 18:21: Egypt as "broken reed" — the image the Rabshakeh uses was stock prophetic
    critique (Isa 30:1-7; 31:1-3; Ezek 29:6-7). He was quoting Israel's own prophetic
    tradition against them.
  - 18:31-32: The vine, fig tree, cistern, grain, wine, olive, honey — covenant-land
    vocabulary (Deut 8:7-10; 1 Kgs 4:25; Mic 4:4). The Rabshakeh offers Assyrian exile
    using the language of the Promised Land. The seduction borrows from Israel's own scripture.
  - 18:34-35: "Samaria out of mine hand" — Samaria fell because of covenant violation, not
    divine weakness. The Rabshakeh's category error: he treats the LORD as a national deity
    comparable to Chemosh or Dagon. Hezekiah's prayer (ch. 19) directly corrects this.
- Jezebel/Ahaz pattern note: 16:17-18 (Ahaz's dismantling of temple furnishings) echoes
  Ahab's religious compromises. The narrator draws a line from the north's apostasy into
  Judah's monarchy through Ahaz.
- Chapter 18 structural note: vv. 1-8 (Hezekiah's faithful reign) and vv. 13-16
  (Hezekiah's tribute) stand in apparent tension. The narrative does not resolve this tension
  neatly; T tier acknowledges it rather than harmonizing it.
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

KINGS2 = {
  "16": {
    "1": {
      "L": "In the seventeenth year of Pekah son of Remaliah, Ahaz son of Jotham king of Judah began to reign.",
      "M": "In the seventeenth year of Pekah son of Remaliah, Ahaz son of Jotham king of Judah became king.",
      "T": "It was the seventeenth year of Pekah son of Remaliah's reign when Ahaz son of Jotham came to the throne of Judah."
    },
    "2": {
      "L": "Twenty years old was Ahaz when he began to reign, and sixteen years he reigned in Jerusalem; and he did not do that which is right in the eyes of the LORD his God, as his father David had done.",
      "M": "Ahaz was twenty years old when he became king and reigned sixteen years in Jerusalem. He did not do what was right in the eyes of the LORD his God, as his ancestor David had done.",
      "T": "Ahaz came to the throne at twenty years old and reigned sixteen years in Jerusalem — but unlike his forefather David, he refused to do what was right in the LORD's sight."
    },
    "3": {
      "L": "But he walked in the way of the kings of Israel; yea, he made his son to pass through the fire, according to the abominations of the heathen whom the LORD cast out before the children of Israel.",
      "M": "Instead, he walked in the ways of the kings of Israel and even made his son pass through the fire, following the abominable practices of the nations the LORD had driven out before the Israelites.",
      "T": "He walked in the path of the northern kings, and went further still — offering his own son in the fire, imitating the detestable rites of the nations the LORD had expelled from before Israel."
    },
    "4": {
      "L": "And he sacrificed and burned incense in the high places and on the hills and under every green tree.",
      "M": "He offered sacrifices and burned incense at the high places, on the hills, and under every spreading green tree.",
      "T": "He scattered his worship across every pagan site — hillside shrines, heights, and the green trees that marked the old Canaanite holy places."
    },
    "5": {
      "L": "Then Rezin king of Syria and Pekah son of Remaliah king of Israel came up to Jerusalem to war; and they besieged Ahaz, but could not conquer him.",
      "M": "Then Rezin king of Syria and Pekah son of Remaliah king of Israel marched against Jerusalem and besieged it, but they could not conquer Ahaz.",
      "T": "In response, Rezin of Syria and Pekah of Israel mounted a combined assault on Jerusalem, surrounding the city — yet despite Ahaz's faithlessness, they could not take it."
    },
    "6": {
      "L": "At that time Rezin king of Syria recovered Elath to Syria, and drove the Jews from Elath; and the Syrians came to Elath and dwelt there unto this day.",
      "M": "At that time Rezin king of Syria recovered Elath for Syria and expelled the Judeans from it; the Syrians came to Elath and have lived there ever since.",
      "T": "In that same campaign, Rezin retook the port city of Elath, expelling its Judean population — the Syrians settled there and the city remained in their hands from that time on."
    },
    "7": {
      "L": "And Ahaz sent messengers to Tiglath-pileser king of Assyria, saying, I am thy servant and thy son; come up and save me out of the hand of the king of Syria and out of the hand of the king of Israel, who rise up against me.",
      "M": "So Ahaz sent messengers to Tiglath-pileser king of Assyria, saying, 'I am your servant and your son. Come up and rescue me from the king of Syria and the king of Israel who are attacking me.'",
      "T": "In desperation, Ahaz sent envoys to Tiglath-pileser of Assyria with a humiliating proposal: 'I am your servant, even your son — come and save me from Syria and Israel who press in on every side.' The plea traded Judah's independence for Assyrian protection."
    },
    "8": {
      "L": "And Ahaz took the silver and gold that was found in the house of the LORD and in the treasures of the king's house, and sent it for a present to the king of Assyria.",
      "M": "Ahaz took the silver and gold found in the temple of the LORD and in the royal treasury and sent it as tribute to the king of Assyria.",
      "T": "To seal the bargain, Ahaz stripped the silver and gold from both the temple and his own palace vaults, sending the plundered sacred and royal wealth as payment to Tiglath-pileser."
    },
    "9": {
      "L": "And the king of Assyria hearkened unto him; and the king of Assyria went up against Damascus and took it, and carried the people of it captive to Kir, and slew Rezin.",
      "M": "The king of Assyria answered his appeal. He marched against Damascus, captured it, deported its people to Kir, and executed Rezin.",
      "T": "Tiglath-pileser answered — at a price. He struck Damascus, took the city, deported its population to Kir, and put Rezin to death. Ahaz's enemy was gone, but at the cost of Judah's vassalage to the world's superpower."
    },
    "10": {
      "L": "And king Ahaz went to Damascus to meet Tiglath-pileser king of Assyria, and saw the altar that was at Damascus; and king Ahaz sent to Urijah the priest the fashion of the altar and the pattern of it, according to all the workmanship thereof.",
      "M": "When King Ahaz went to Damascus to meet Tiglath-pileser, he saw the altar there. He sent Urijah the priest the design and pattern of the altar in all its details.",
      "T": "When Ahaz made his vassal visit to Tiglath-pileser in Damascus, something caught his eye — the Aramean altar. He sent its exact specifications back to Jerusalem to his priest Urijah, instructing him to build a replica."
    },
    "11": {
      "L": "And Urijah the priest built an altar; according to all that king Ahaz had sent from Damascus, so Urijah the priest made it against king Ahaz came from Damascus.",
      "M": "Urijah the priest built the altar exactly as King Ahaz had specified from Damascus — and had it ready before the king returned.",
      "T": "Urijah the priest executed the commission faithfully: he built the foreign altar to the king's exact specifications and completed it before Ahaz had even returned from Damascus."
    },
    "12": {
      "L": "And when the king was come from Damascus, the king saw the altar; and the king approached to the altar and went up upon it.",
      "M": "When the king returned from Damascus, he saw the altar. He approached it and mounted it.",
      "T": "On his return, Ahaz went immediately to the new altar — approached it, mounted it, and made it his own."
    },
    "13": {
      "L": "And he burned his burnt offering and his grain offering, and poured his drink offering, and sprinkled the blood of his peace offerings upon the altar.",
      "M": "He burned his burnt offering and grain offering, poured out his drink offering, and splashed the blood of his peace offerings on the altar.",
      "T": "He performed the full liturgy of Israelite sacrifice — burnt offering, grain offering, drink offering, the blood of peace offerings — but on a pagan Aramean altar. The forms of worship remained; the address had changed."
    },
    "14": {
      "L": "And the brazen altar, which was before the LORD, he brought from the forefront of the house, from between the altar and the house of the LORD, and put it on the north side of the altar.",
      "M": "He moved the bronze altar that had stood before the LORD away from its place between his new altar and the temple, repositioning it to the north side.",
      "T": "The bronze altar — the authorized altar of the LORD — was shunted aside to the north, displaced by the Aramean import. The old was demoted; the new pagan design took the central position before the temple."
    },
    "15": {
      "L": "And king Ahaz commanded Urijah the priest, saying, Upon the great altar burn the morning burnt offering, and the evening grain offering, and the king's burnt offering, and his grain offering, with the burnt offering of all the people of the land, and their grain offering, and their drink offerings; and sprinkle upon it all the blood of the burnt offering, and all the blood of the sacrifice; and the brasen altar shall be for me to inquire by.",
      "M": "King Ahaz instructed Urijah the priest: 'On the great altar, offer the morning burnt offering, the evening grain offering, the king's burnt offering and grain offering, the people's burnt offering and grain offering, and all their drink offerings. Throw all the blood of burnt offerings and sacrifices on it. The bronze altar will be reserved for my personal inquiry.'",
      "T": "Ahaz formalized the arrangement: the new Aramean altar would now host all official worship — morning and evening offerings, royal offerings, the full popular liturgy. The ancient bronze altar, divinely commanded, was reduced to the king's private divination stand. Public worship was redirected to a pagan design; the LORD's altar was sidelined."
    },
    "16": {
      "L": "Thus did Urijah the priest, according to all that king Ahaz commanded.",
      "M": "Urijah the priest did everything King Ahaz commanded.",
      "T": "Urijah carried out the king's orders without recorded objection — a priest who served the crown more faithfully than the covenant."
    },
    "17": {
      "L": "And king Ahaz cut off the borders of the bases, and removed the laver from off them; and took down the sea from off the brasen oxen that were under it, and put it upon a pavement of stones.",
      "M": "King Ahaz cut off the side panels of the wheeled stands and removed the basins from them. He lifted the great bronze sea off the twelve bronze oxen that supported it and set it on a stone pavement.",
      "T": "Ahaz stripped the temple of its remaining bronze furnishings — the elaborate wheeled stands and their basins (Hiram's masterwork from 1 Kgs 7:27-39) were dismantled, and the magnificent bronze sea was taken down from its twelve oxen and laid on bare stone. Payment toward Tiglath-pileser's account, at the expense of the temple's glory."
    },
    "18": {
      "L": "And the covert for the sabbath that they had built in the house, and the king's entry without, turned he from the house of the LORD for the king of Assyria.",
      "M": "He also removed the covered Sabbath walkway that had been built in the temple, and altered the king's outer entrance — modifications made to comply with the demands of the king of Assyria.",
      "T": "Finally Ahaz restructured the temple's royal infrastructure — dismantling the Sabbath colonnade and blocking or relocating the king's special entrance. The house of the LORD was reshaped to fit the requirements of Judah's Assyrian overlord."
    },
    "19": {
      "L": "Now the rest of the acts of Ahaz which he did, are they not written in the book of the chronicles of the kings of Judah?",
      "M": "The rest of the deeds of Ahaz are recorded in the Book of the Chronicles of the Kings of Judah.",
      "T": "The full record of Ahaz's reign is in the royal annals. The narrator has selected only what is necessary — a portrait of apostasy from start to finish."
    },
    "20": {
      "L": "And Ahaz slept with his fathers, and was buried with his fathers in the city of David; and Hezekiah his son reigned in his stead.",
      "M": "Ahaz rested with his ancestors and was buried with them in the city of David. His son Hezekiah became king in his place.",
      "T": "Ahaz died and was buried in Jerusalem — but not in the royal tombs (2 Chron 28:27 specifies he was denied the kings' burial ground). His son Hezekiah took the throne, and with him everything changed."
    }
  },
  "17": {
    "1": {
      "L": "In the twelfth year of Ahaz king of Judah began Hoshea the son of Elah to reign in Samaria over Israel nine years.",
      "M": "In the twelfth year of Ahaz king of Judah, Hoshea son of Elah became king of Israel in Samaria, and he reigned nine years.",
      "T": "Nine years — that is all that was left to the northern kingdom when Hoshea son of Elah came to power in Samaria in the twelfth year of Ahaz."
    },
    "2": {
      "L": "And he did that which was evil in the sight of the LORD, but not as the kings of Israel that were before him.",
      "M": "He did what was evil in the LORD's sight, though not to the degree of the kings of Israel before him.",
      "T": "He did evil — but the narrator notes a distinction: not as bad as his predecessors. The faint praise of a dynasty in its final hours."
    },
    "3": {
      "L": "Against him came up Shalmaneser king of Assyria; and Hoshea became his servant and gave him presents.",
      "M": "Shalmaneser king of Assyria marched against Hoshea, who became his vassal and paid him tribute.",
      "T": "Shalmaneser of Assyria came against him, and Hoshea submitted — paying tribute and becoming an Assyrian vassal. What Ahaz had chosen voluntarily, Hoshea accepted under compulsion."
    },
    "4": {
      "L": "And the king of Assyria found conspiracy in Hoshea; for he had sent messengers to So king of Egypt, and brought no present to the king of Assyria, as he had done year by year; therefore the king of Assyria shut him up and bound him in prison.",
      "M": "But the king of Assyria uncovered a conspiracy: Hoshea had sent envoys to So king of Egypt and withheld the annual tribute. So the king of Assyria arrested him and put him in prison.",
      "T": "But Hoshea gambled: he sent secret envoys to Egypt's king So, seeking an alliance, and stopped paying tribute. The gamble failed. Shalmaneser discovered the conspiracy and had Hoshea arrested and jailed. The last king of Israel ended his reign in an Assyrian prison."
    },
    "5": {
      "L": "Then the king of Assyria came up throughout all the land, and went up to Samaria, and besieged it three years.",
      "M": "The king of Assyria invaded the whole land and besieged Samaria for three years.",
      "T": "Shalmaneser then swept through the entire territory and laid Samaria under siege. For three years the capital held out — a remarkable resistance, but ultimately futile."
    },
    "6": {
      "L": "In the ninth year of Hoshea the king of Assyria took Samaria, and carried Israel away into Assyria, and placed them in Halah and in Habor by the river of Gozan, and in the cities of the Medes.",
      "M": "In the ninth year of Hoshea, the king of Assyria captured Samaria and deported the Israelites to Assyria, settling them in Halah, along the Habor River in Gozan, and in the Median cities.",
      "T": "In Hoshea's ninth year, Samaria fell. The population of the northern kingdom was uprooted and scattered across the Assyrian empire — to Halah, to the Habor valley in Gozan, to the cities of the Medes. The ten tribes dispersed and, from the narrator's perspective, never returned."
    },
    "7": {
      "L": "For so it was, that the children of Israel had sinned against the LORD their God, who had brought them up out of the land of Egypt from under the hand of Pharaoh king of Egypt, and had feared other gods,",
      "M": "This happened because the Israelites had sinned against the LORD their God, who had brought them out of Egypt from under Pharaoh's power, and they had worshiped other gods.",
      "T": "The narrator pauses to explain the theological meaning of what has just happened. The exile was not geopolitical accident — it was the consequence of covenant violation stretching back centuries. Israel had abandoned the God who had freed them from Egypt and gone after other gods."
    },
    "8": {
      "L": "And walked in the statutes of the heathen, whom the LORD cast out before the children of Israel, and of the kings of Israel, which they had made.",
      "M": "They followed the practices of the nations the LORD had driven out before them, and the customs their own kings had introduced.",
      "T": "They adopted the religious customs of the nations Israel had displaced — the very peoples expelled because of these same abominations — and layered on that the innovations of their own corrupt kings."
    },
    "9": {
      "L": "And the children of Israel did secretly those things that were not right against the LORD their God, and they built them high places in all their cities, from the tower of the watchmen to the fenced city.",
      "M": "The Israelites secretly did things against the LORD their God that were not right. They set up high places in all their towns, from the smallest watchtower to the largest fortified city.",
      "T": "The word 'secretly' is the narrator's indictment: they knew it was wrong and hid it. Across the entire land — from the loneliest watchtower to the walled cities — shrines proliferated."
    },
    "10": {
      "L": "And they set them up images and groves in every high hill, and under every green tree;",
      "M": "On every high hill and under every green tree they erected sacred pillars and Asherah poles.",
      "T": "Stone pillars to Baal and Asherah poles dotted every hilltop and shaded tree — the full apparatus of Canaanite religion reconstructed throughout the land."
    },
    "11": {
      "L": "And there they burnt incense in all the high places, as did the heathen whom the LORD carried away before them; and wrought wicked things to provoke the LORD to anger;",
      "M": "They burned offerings at all the high places as the nations had done — nations the LORD had expelled before them — and did evil things that provoked the LORD to anger.",
      "T": "The irony is stark: they worshiped as the expelled nations had worshiped. The LORD had driven those nations out for these very practices, and Israel was now replicating them — storing up for themselves the same judgment."
    },
    "12": {
      "L": "For they served idols, whereof the LORD had said unto them, Ye shall not do this thing.",
      "M": "They served idols, despite the LORD's explicit prohibition: 'You must not do this.'",
      "T": "They served idols — doing precisely what God had explicitly forbidden them to do. The prohibition had been clear; the disobedience was willful."
    },
    "13": {
      "L": "Yet the LORD testified against Israel and against Judah by all the prophets and all the seers, saying, Turn ye from your evil ways, and keep my commandments and my statutes, according to all the law which I commanded your fathers, and which I sent to you by my servants the prophets.",
      "M": "Yet the LORD had warned Israel and Judah through every prophet and seer: 'Turn from your evil ways. Keep my commandments and statutes — all the law I gave your ancestors and sent to you through my servant the prophets.'",
      "T": "God had not left them without warning. Prophet after prophet, seer after seer had carried the same urgent message: turn back, keep the covenant. The law was not unknown — it had been given at Sinai and renewed repeatedly. The prophets were the last voice of a covenant still held open. Israel refused to listen."
    },
    "14": {
      "L": "Notwithstanding they would not hear, but hardened their necks, like to the neck of their fathers, that did not believe in the LORD their God.",
      "M": "But they would not listen. They were as stubborn as their ancestors who had not trusted in the LORD their God.",
      "T": "They refused. The stiff neck — the idiom for stubborn defiance — is the image of Exodus 32-33 (the golden calf) and Deuteronomy 9-10 (the wilderness generation). Israel in the land was just like Israel in the wilderness: faithless, resistant, unable to believe."
    },
    "15": {
      "L": "And they rejected his statutes and his covenant that he made with their fathers, and his testimonies which he testified against them; and they followed vanity and became vain, and went after the heathen that were round about them, concerning whom the LORD had charged them, that they should not do like them.",
      "M": "They rejected his statutes and the covenant he had made with their ancestors, along with the warnings he had given them. They pursued worthless idols and became worthless themselves, following the surrounding nations the LORD had told them not to imitate.",
      "T": "The covenant community dissolved: they threw off the statutes, broke the covenant, ignored the warnings. 'Went after vanity and became vain' captures a deep theological principle — we become like what we worship. They imitated the nations they were supposed to be distinct from, and the distinctiveness of Israel evaporated."
    },
    "16": {
      "L": "And they left all the commandments of the LORD their God, and made them molten images, even two calves, and made a grove, and worshipped all the host of heaven, and served Baal.",
      "M": "They abandoned all the commandments of the LORD their God. They cast two metal calves, made an Asherah pole, worshiped the whole host of heaven, and served Baal.",
      "T": "The complete apostasy is catalogued: the two gold calves of Jeroboam (1 Kgs 12), Asherah poles, the astral cult of the heavenly host, and Baal worship. Every forbidden form of religion was embraced."
    },
    "17": {
      "L": "And they caused their sons and their daughters to pass through the fire, and used divination and enchantments, and sold themselves to do evil in the sight of the LORD, to provoke him to anger.",
      "M": "They burned their sons and daughters in the fire, practiced divination and sorcery, and gave themselves over completely to doing evil in the LORD's sight, provoking him to anger.",
      "T": "Child sacrifice — passing children through the fire — was the ultimate desecration of the covenant people's children. Added to this were divination, sorcery, and the complete surrender to evil: they 'sold themselves,' the language of slavery, into the service of wickedness. Every possible outrage against the covenant was committed."
    },
    "18": {
      "L": "Therefore the LORD was very angry with Israel, and removed them out of his sight; there was none left but the tribe of Judah only.",
      "M": "So the LORD was extremely angry with Israel and expelled them from his sight. Only the tribe of Judah remained.",
      "T": "The judgment: God removed Israel 'from his sight' — the same idiom used of the expulsion from Eden (Gen 4:16). The exile is a theological act, not merely a political one. Only Judah was left, and that, as the next verse warns, only for now."
    },
    "19": {
      "L": "Also Judah kept not the commandments of the LORD their God, but walked in the statutes of Israel which they made.",
      "M": "Judah also did not obey the commands of the LORD their God but followed the practices that Israel had introduced.",
      "T": "Judah is not let off the hook. The Deuteronomistic narrator signals what the reader already suspects: the same infection spread south. The fall of Israel is a warning Judah is also failing to heed."
    },
    "20": {
      "L": "And the LORD rejected all the seed of Israel, and afflicted them, and delivered them into the hand of spoilers, until he had cast them out of his sight.",
      "M": "The LORD rejected all the descendants of Israel, afflicted them, and handed them over to raiders, until he had expelled them from his sight.",
      "T": "The rejection of Israel was total: delivered into the hands of raider after raider, afflicted repeatedly, until the final expulsion. 'Cast them out of his sight' echoes the Eden judgment — exile as un-creation, the reversal of all God's redeeming work."
    },
    "21": {
      "L": "For he rent Israel from the house of David; and they made Jeroboam the son of Nebat king; and Jeroboam drave Israel from following the LORD, and made them sin a great sin.",
      "M": "When Israel was torn away from the house of David, they made Jeroboam son of Nebat king. Jeroboam led Israel away from following the LORD and caused them to commit great sin.",
      "T": "The historical root of the catastrophe is traced to the original schism: Jeroboam's break with David's dynasty (1 Kgs 12). Every subsequent sin in the north is traced back to 'the sin of Jeroboam' — the gold calves at Bethel and Dan. He set the trajectory; two centuries of kings followed it."
    },
    "22": {
      "L": "For the children of Israel walked in all the sins of Jeroboam which he did; they departed not from them;",
      "M": "The Israelites continued in all the sins Jeroboam had committed; they never turned away from them,",
      "T": "Generation after generation, the north followed the path Jeroboam had set. Not one northern king broke the pattern — the sin of Jeroboam was Israel's defining and fatal legacy."
    },
    "23": {
      "L": "Until the LORD removed Israel out of his sight, as he had said by all his servants the prophets. So was Israel carried away out of their own land to Assyria unto this day.",
      "M": "until the LORD removed Israel from his sight, just as he had declared through all his servants the prophets. So Israel was carried into exile from their land to Assyria — where they remain to this day.",
      "T": "The exile was the fulfillment of precisely what the prophets had warned. History confirmed the prophetic word: Israel removed from the land, scattered in Assyria — a fact that remained true for the narrator's own generation. The prophetic word did not fall to the ground."
    },
    "24": {
      "L": "And the king of Assyria brought men from Babylon, and from Cuthah, and from Ava, and from Hamath, and from Sepharvaim, and placed them in the cities of Samaria instead of the children of Israel; and they possessed Samaria and dwelt in the cities thereof.",
      "M": "The king of Assyria brought settlers from Babylon, Cuthah, Avva, Hamath, and Sepharvaim and installed them in the cities of Samaria to replace the Israelites. They took over Samaria and occupied its cities.",
      "T": "Standard Assyrian policy: the conquered are scattered, the land repopulated with foreign deportees. The cities of Samaria were filled with people from across the empire — Babylonians, Cutheans, Avvites, Hamathites, Sepharvites. The land of Israel now had no Israelites."
    },
    "25": {
      "L": "And so it was at the beginning of their dwelling there, that they feared not the LORD; therefore the LORD sent lions among them, which slew some of them.",
      "M": "When they first settled there, they did not worship the LORD. So the LORD sent lions among them, which killed some of them.",
      "T": "The land still belonged to the LORD, and the new settlers discovered this: they paid no attention to the God of the land, and lions attacked them. The narrator presents it as the LORD's warning — the land will not tolerate those who ignore its God."
    },
    "26": {
      "L": "Wherefore they spake to the king of Assyria, saying, The nations which thou hast removed and placed in the cities of Samaria know not the manner of the God of the land; therefore he hath sent lions among them, and behold, they slay them, because they know not the manner of the God of the land.",
      "M": "Someone reported to the king of Assyria: 'The peoples you deported to the cities of Samaria do not know the requirements of the god of the land. He has sent lions among them that are killing people because they don't know his requirements.'",
      "T": "Word reached the Assyrian king: the deportees were suffering because they didn't know how to honor the local deity. The pagan diagnosis was correct as far as it went — they recognized that the land's god required specific worship. They were simply wrong about what that worship entailed."
    },
    "27": {
      "L": "Then the king of Assyria commanded, saying, Carry thither one of the priests whom ye brought from thence; and let them go and dwell there, and let him teach them the manner of the God of the land.",
      "M": "The king of Assyria ordered: 'Send back one of the priests you took from there. Have him go and live there and teach the people the requirements of the god of the land.'",
      "T": "The Assyrian king's response was pragmatic: send back a displaced Israelite priest to teach the new settlers how to satisfy the local deity. The intention was not true worship but political pacification of a troublesome territory."
    },
    "28": {
      "L": "Then one of the priests whom they had carried away from Samaria came and dwelt in Bethel, and taught them how they should fear the LORD.",
      "M": "So one of the exiled priests from Samaria returned and settled in Bethel, where he taught the people how to worship the LORD.",
      "T": "One displaced priest returned and settled at Bethel — the very city where Jeroboam had installed his golden calves. He taught the new inhabitants 'how to fear the LORD.' The irony is deep: orthodox instruction given at the most compromised religious site in the land's history."
    },
    "29": {
      "L": "Howbeit every nation made gods of their own, and put them in the houses of the high places which the Samaritans had made, every nation in their cities wherein they dwelt.",
      "M": "However, every national group continued making idols of their own and placed them in the shrines at the high places the Samaritans had built — each people in the cities where they were settled.",
      "T": "But the priestly instruction produced syncretism, not conversion. Each national group kept their own gods and installed them in the local shrines. The LORD was added to an already crowded pantheon."
    },
    "30": {
      "L": "And the men of Babylon made Succoth-benoth, and the men of Cuth made Nergal, and the men of Hamath made Ashima,",
      "M": "The Babylonians made Succoth-benoth, the Cutheans made Nergal, and the Hamathites made Ashima.",
      "T": "The roll call of foreign gods installed in Samaria: Succoth-benoth (a Babylonian deity), Nergal (the underworld god of Cuth), Ashima (Hamath's deity). The land once dedicated to the LORD had become a theological marketplace."
    },
    "31": {
      "L": "And the Avites made Nibhaz and Tartak, and the Sepharvites burnt their children in fire to Adrammelech and Anammelech, the gods of Sepharvaim.",
      "M": "The Avvites made Nibhaz and Tartak, and the Sepharvites burned their children in the fire as offerings to Adrammelech and Anammelech, the gods of Sepharvaim.",
      "T": "The Avvites brought their obscure deities Nibhaz and Tartak. Most horrifyingly, the Sepharvites revived child sacrifice — offering children to their fire-gods Adrammelech and Anammelech. The atrocity Ahaz had introduced into Judah (16:3) was now practiced systematically in what had been Israel's land."
    },
    "32": {
      "L": "So they feared the LORD, and made unto themselves of the lowest of them priests of the high places, which sacrificed for them in the houses of the high places.",
      "M": "They also professed to fear the LORD and appointed from their own ranks priests for the high places, who performed sacrifices in the shrines.",
      "T": "They added the LORD to their religious portfolio. Improvised priests — drawn from their own number, with no Levitical credentials — officiated at the high places. The fear of the LORD had become one item in a diverse religious program."
    },
    "33": {
      "L": "They feared the LORD and served their own gods, after the manner of the nations whom they carried away from thence.",
      "M": "They worshiped the LORD, but they also served their own gods in the way of the nations from which they had come.",
      "T": "The summary statement: they feared the LORD and served their own gods. The two verbs stand side by side without resolution. This is the Samaritan religious compromise — the theological position around which later Samaritan-Jewish tensions would form."
    },
    "34": {
      "L": "Unto this day they do after the former manners; they fear not the LORD, neither do they after their statutes, or after their ordinances, or after the law and commandment which the LORD commanded the children of Jacob, whom he named Israel;",
      "M": "To this day they follow their original practices. They do not truly fear the LORD or observe the statutes, ordinances, laws, and commandments he gave to the descendants of Jacob, whom he named Israel.",
      "T": "The narrator's judgment is sharp: what they call 'fearing the LORD' is not the real thing. To fear the LORD means to keep his statutes, ordinances, and commandments — the whole covenantal framework given to Jacob-Israel. Mixing that with other gods is not partial worship; it is no worship at all."
    },
    "35": {
      "L": "With whom the LORD had made a covenant, and charged them, saying, Ye shall not fear other gods, nor bow yourselves to them, nor serve them, nor sacrifice to them;",
      "M": "When the LORD made a covenant with them, he commanded: 'You must not worship other gods or bow down to them or serve them or sacrifice to them.'",
      "T": "The covenant prohibition is rehearsed in full: no other gods, no bowing, no service, no sacrifice. The first commandment in Sinai language. Even those who were not originally party to the covenant with Israel were now being held to its terms, because they lived in the covenant land."
    },
    "36": {
      "L": "But the LORD, who brought you up out of the land of Egypt with great power and a stretched-out arm, him shall ye fear, and him shall ye worship, and to him shall ye do sacrifice.",
      "M": "Rather, fear the LORD, who brought you out of Egypt with great power and an outstretched arm. Bow to him and offer sacrifices to him.",
      "T": "The basis for exclusive loyalty is the Exodus: the LORD brought Israel out of Egypt with the mighty arm that overthrew Pharaoh. That act of redemption grounds the demand for exclusive worship. Worship is given to the Redeemer, not merely the strongest local deity."
    },
    "37": {
      "L": "And the statutes and the ordinances, and the law and the commandment, which he wrote for you, ye shall observe to do for evermore; and ye shall not fear other gods.",
      "M": "You shall carefully observe forever the statutes, ordinances, laws, and commandments he wrote for you. You shall not worship other gods.",
      "T": "The written Torah — the law Moses wrote down — was the covenant's permanent expression. 'Forever' is the word: these obligations do not expire. The settler peoples receiving this instruction were being invited into the same exclusive loyalty that Israel had rejected."
    },
    "38": {
      "L": "And the covenant that I have made with you ye shall not forget; neither shall ye fear other gods.",
      "M": "Do not forget the covenant I have made with you. Do not worship other gods.",
      "T": "The covenant must not be forgotten — forgetting it is the first step toward abandoning it. Memory is a covenant obligation, not merely a pious sentiment."
    },
    "39": {
      "L": "But the LORD your God ye shall fear; and he shall deliver you out of the hand of all your enemies.",
      "M": "Fear only the LORD your God, and he will rescue you from all your enemies.",
      "T": "The incentive is practical as well as theological: exclusive loyalty to the LORD brings the protection he alone can provide. The nations now living in Samaria had already experienced what the land's God could do. Deliverance belongs to the one God alone."
    },
    "40": {
      "L": "Howbeit they did not hearken, but they did after their former manner.",
      "M": "But they would not listen; they kept to their old ways.",
      "T": "They heard, and they did not change. The religious syncretism remained fixed. The instruction had been given; it was not received."
    },
    "41": {
      "L": "So these nations feared the LORD, and served their graven images, both their children, and their children's children; as did their fathers, so do they unto this day.",
      "M": "So these peoples worshiped the LORD but also served their own idols. Their children and grandchildren do the same today, just as their ancestors did.",
      "T": "The concluding irony: they feared the LORD and served their idols — and passed this syncretistic inheritance down to every subsequent generation. 'So they do to this day' is the narrator's contemporary observation: the Samaritan compromise is a living reality, not ancient history."
    }
  },
  "18": {
    "1": {
      "L": "Now it came to pass in the third year of Hoshea son of Elah king of Israel, that Hezekiah the son of Ahaz king of Judah began to reign.",
      "M": "In the third year of Hoshea son of Elah king of Israel, Hezekiah son of Ahaz king of Judah became king.",
      "T": "While Hoshea was in his third year — with the northern kingdom's final countdown already running — Hezekiah son of Ahaz came to the throne in Jerusalem."
    },
    "2": {
      "L": "Twenty and five years old was he when he began to reign; and he reigned twenty and nine years in Jerusalem. His mother's name also was Abi, the daughter of Zachariah.",
      "M": "He was twenty-five years old when he became king and reigned twenty-nine years in Jerusalem. His mother's name was Abi daughter of Zechariah.",
      "T": "Twenty-five years old, twenty-nine year reign — opposite his father Ahaz in every way. Even the notice of his mother's name (a detail reserved for queens who influenced the reign for good) signals that Hezekiah's story will be different."
    },
    "3": {
      "L": "And he did that which was right in the sight of the LORD, according to all that David his father did.",
      "M": "He did what was right in the eyes of the LORD, just as his ancestor David had done.",
      "T": "The royal verdict formula applied at its highest: 'right in the sight of the LORD — just as David did.' No qualification, no caveat. Ahaz's son reversed every dimension of his father's policy."
    },
    "4": {
      "L": "He removed the high places, and brake the images, and cut down the groves, and brake in pieces the brasen serpent that Moses had made; for until those days the children of Israel did burn incense to it; and he called it Nehushtan.",
      "M": "He demolished the high places, smashed the sacred pillars, and cut down the Asherah poles. He broke in pieces the bronze serpent Moses had made, because up to that time the Israelites had been burning incense to it. It was called Nehushtan.",
      "T": "Hezekiah's reform went further than any previous king's. High places, pillars, Asherah poles — all destroyed. But the most remarkable act was breaking the Nehushtan: the very bronze serpent Moses had made in the wilderness (Num 21:8-9), which God himself had commanded as an instrument of healing. It had become an idol; centuries of incense-burning had made it a snare. Hezekiah dismissed it with a contemptuous name — 'Nehushtan,' just a bronze thing (nəḥōšet). What begins as a means of grace can become an object of false worship; Hezekiah was clear-eyed enough to destroy even the venerable."
    },
    "5": {
      "L": "He trusted in the LORD God of Israel; so that after him was none like him among all the kings of Judah, nor any that were before him.",
      "M": "He trusted in the LORD God of Israel. Among all the kings of Judah there was no one like him — neither before nor after him.",
      "T": "The narrator's superlative evaluation: Hezekiah trusted in the LORD — and no king of Judah, from David's line to the last, matched him in this. The word is trust (בָּטַח), not mere obedience. It is a relational confidence, a whole-life orientation toward God. This quality will be tested to its limit in the Sennacherib crisis ahead."
    },
    "6": {
      "L": "For he clave to the LORD, and departed not from following him, but kept his commandments, which the LORD commanded Moses.",
      "M": "He clung to the LORD and did not turn away from him; he kept the commandments the LORD had given Moses.",
      "T": "He clung to the LORD — the verb (דָּבַק) is the covenant-loyalty word of Ruth clinging to Naomi (Ruth 1:14) and the Deuteronomic call to 'hold fast' to the LORD (Deut 10:20; 11:22). Steadfast personal loyalty, not merely formal compliance."
    },
    "7": {
      "L": "And the LORD was with him; and he prospered whithersoever he went forth; and he rebelled against the king of Assyria, and served him not.",
      "M": "The LORD was with him; he succeeded in everything he undertook. He rebelled against the king of Assyria and refused to submit.",
      "T": "The covenant formula: 'the LORD was with him.' Where the LORD is present, blessing follows. Hezekiah's rebellion against Assyria was not political adventurism — it was the exercise of a faith that the LORD's protection made submission to foreign powers unnecessary."
    },
    "8": {
      "L": "He smote the Philistines, even unto Gaza, and the borders thereof, from the tower of the watchmen to the fenced city.",
      "M": "He defeated the Philistines as far as Gaza and its surrounding territory, from the smallest outpost to the largest fortified city.",
      "T": "His military reach extended to Gaza — the Philistine heartland. Where Ahaz had paid tribute to Assyria and lost Elath to Syria, Hezekiah pushed Judah's borders outward. The LORD's presence translated into territorial confidence."
    },
    "9": {
      "L": "And it came to pass in the fourth year of king Hezekiah, which was the seventh year of Hoshea son of Elah king of Israel, that Shalmaneser king of Assyria came up against Samaria and besieged it.",
      "M": "In the fourth year of King Hezekiah — which was the seventh year of Hoshea son of Elah king of Israel — Shalmaneser king of Assyria marched against Samaria and besieged it.",
      "T": "The narrative synchronizes the fall of Samaria with Hezekiah's reign, reinforcing the contrast: while Hezekiah was prospering in the south under the LORD's blessing, the faithless north was entering its final siege."
    },
    "10": {
      "L": "And at the end of three years they took it; even in the sixth year of Hezekiah, that is the ninth year of Hoshea king of Israel, Samaria was taken.",
      "M": "After three years they captured it. In the sixth year of Hezekiah — the ninth year of Hoshea king of Israel — Samaria fell.",
      "T": "Three years of siege; the sixth year of Hezekiah's faithful reign coinciding with the final collapse of the faithless north. The juxtaposition is the narrator's theology of history made visible in synchronism."
    },
    "11": {
      "L": "And the king of Assyria did carry away Israel unto Assyria, and put them in Halah and in Habor by the river of Gozan, and in the cities of the Medes;",
      "M": "The king of Assyria deported the Israelites to Assyria, settling them in Halah, along the Habor River in Gozan, and in the Median cities.",
      "T": "The deportation, already narrated in chapter 17, is summarized again here — linking it explicitly to Hezekiah's reign. The exile of the north happened on Hezekiah's watch, and Judah was now alone."
    },
    "12": {
      "L": "Because they obeyed not the voice of the LORD their God, but transgressed his covenant, and all that Moses the servant of the LORD commanded, and would not hear them, nor do them.",
      "M": "This happened because they did not listen to the LORD their God but violated his covenant — everything Moses the servant of the LORD had commanded. They neither listened nor obeyed.",
      "T": "The cause is restated: not military weakness, not geopolitical misfortune — covenant violation. The fall of Israel was the outworking of Deuteronomy 28's covenant curses. They heard the law through Moses; they neither listened to it nor acted on it."
    },
    "13": {
      "L": "Now in the fourteenth year of king Hezekiah did Sennacherib king of Assyria come up against all the fenced cities of Judah, and took them.",
      "M": "In the fourteenth year of King Hezekiah, Sennacherib king of Assyria invaded and captured all the fortified cities of Judah.",
      "T": "Year fourteen of Hezekiah's reign: the crisis arrives. Sennacherib of Assyria — a greater power than Shalmaneser — swept through Judah's fortified cities. The king evaluated as 'none like him' was about to face the supreme test of his trust."
    },
    "14": {
      "L": "And Hezekiah king of Judah sent to the king of Assyria to Lachish, saying, I have offended; return from me; that which thou puttest on me will I bear. And the king of Assyria appointed unto Hezekiah king of Judah three hundred talents of silver and thirty talents of gold.",
      "M": "Hezekiah king of Judah sent word to the king of Assyria at Lachish: 'I have sinned. Withdraw from me, and I will pay whatever you impose.' The king of Assyria levied three hundred talents of silver and thirty talents of gold on Hezekiah.",
      "T": "Hezekiah's trust apparently faltered at first — he sent a submission and a confession of fault. Whether this was tactical maneuvering or a collapse of faith the text does not clarify. The tribute demanded was enormous: three hundred talents of silver and thirty of gold. Whatever trust he had expressed in chapter 18's opening verses would have to be recovered."
    },
    "15": {
      "L": "And Hezekiah gave him all the silver that was found in the house of the LORD and in the treasures of the king's house.",
      "M": "Hezekiah handed over all the silver found in the temple of the LORD and in the royal treasury.",
      "T": "The temple and the palace were stripped. What Ahaz had done to appease Assyria (16:8), Hezekiah now repeated — but the situation was more desperate and the amounts far larger."
    },
    "16": {
      "L": "At that time did Hezekiah cut off the gold from the doors of the temple of the LORD, and from the pillars which Hezekiah king of Judah had overlaid, and gave it to the king of Assyria.",
      "M": "At that time Hezekiah stripped the gold from the doors of the LORD's temple and from the doorposts he himself had plated, and gave it to the king of Assyria.",
      "T": "Hezekiah cut the gold overlay from temple doors he had himself installed — his own previous act of devotion was now sacrificed to political survival. Gold stripped from the house of God, like his father before him. The irony is pointed: the most faithful king was brought to the same act as the most faithless."
    },
    "17": {
      "L": "And the king of Assyria sent Tartan and Rabsaris and Rabshakeh from Lachish to king Hezekiah with a great host against Jerusalem. And they went up and came to Jerusalem. And when they were come up, they came and stood by the conduit of the upper pool, which is in the highway of the fuller's field.",
      "M": "The king of Assyria sent the Tartan, the Rab-saris, and the Rabshakeh from Lachish to King Hezekiah at Jerusalem with a massive army. They came to Jerusalem and took position by the aqueduct of the Upper Pool on the road to the Fuller's Field.",
      "T": "The tribute had bought only a pause — now Sennacherib sent three senior officers with a massive force directly to Jerusalem's walls. The position they chose — the conduit of the Upper Pool — was the city's water supply. Standing there was a statement: we can cut off your water. The psychological pressure was calculated."
    },
    "18": {
      "L": "And when they had called to the king, there came out to them Eliakim the son of Hilkiah, which was over the household, and Shebna the scribe, and Joah the son of Asaph the recorder.",
      "M": "When they called for the king, Eliakim son of Hilkiah, the palace administrator, came out to them, along with Shebna the secretary and Joah son of Asaph the recorder.",
      "T": "The king did not come out. His three senior officials faced the Assyrian delegation — the palace administrator (Eliakim), the royal secretary (Shebna), and the recorder (Joah). This was the full diplomatic team; Hezekiah remained inside the walls."
    },
    "19": {
      "L": "And Rabshakeh said unto them, Speak ye now to Hezekiah, Thus saith the great king, the king of Assyria, What confidence is this wherein thou trustest?",
      "M": "The Rabshakeh told them, 'Say to Hezekiah: This is what the great king, the king of Assyria, says: What is the basis of this trust of yours?'",
      "T": "The Rabshakeh opened with a theological challenge: 'What is the basis of this trust of yours?' The word is בִּטָּחוֹן — the same root as Hezekiah's defining virtue (18:5). The Assyrian commander had intelligence on Hezekiah's theology, and he targeted it directly."
    },
    "20": {
      "L": "Thou sayest, but they are but vain words, I have counsel and strength for the war. Now on whom dost thou trust, that thou rebellest against me?",
      "M": "'You say you have strategy and military strength for war — but these are empty words. On whom are you relying that you dare to rebel against me?'",
      "T": "'You have strategy, you have strength for war.' The Rabshakeh concedes these claims — then dismisses them as empty words. The interrogation strips away each possible foundation of trust. What, precisely, is this confidence built on?"
    },
    "21": {
      "L": "Now, behold, thou trustest upon the staff of this bruised reed, even upon Egypt, on which if a man lean, it will go into his hand and pierce it; so is Pharaoh king of Egypt unto all that trust on him.",
      "M": "'You are relying on Egypt, that broken staff of a reed — when a man leans on it, it pierces his hand. That is what Pharaoh king of Egypt is to everyone who trusts him.'",
      "T": "'Egypt — that is what you are resting on.' The image is savage: not a walking staff but a broken reed, one that punctures the very hand of the man who leans on it. The Rabshakeh was quoting what Israel's own prophets had said about Egypt (Isa 30:1-7; 31:1-3). He had done his research — he was turning Israel's prophetic tradition into a weapon of psychological warfare."
    },
    "22": {
      "L": "But if ye say unto me, We trust in the LORD our God; is not that he, whose high places and whose altars Hezekiah hath taken away, and hath said to Judah and Jerusalem, Ye shall worship before this altar in Jerusalem?",
      "M": "'And if you tell me you trust in the LORD your God — isn't he the one whose high places and altars Hezekiah removed, ordering Judah and Jerusalem to worship only before this altar in Jerusalem?'",
      "T": "'All right, you trust the LORD. But Hezekiah tore down his altars across the whole country — how can the LORD help you when his worship sites have been dismantled?' The Rabshakeh had intelligence on Hezekiah's reform, but he fundamentally misread it: he interpreted the centralization of worship as the destruction of the LORD's support base, not as the purification of it. Brilliant rhetoric, entirely wrong theology."
    },
    "23": {
      "L": "Now therefore, I pray thee, give pledges to my lord the king of Assyria, and I will deliver thee two thousand horses, if thou be able on thy part to set riders upon them.",
      "M": "'Come now, make a wager with my master the king of Assyria: I will give you two thousand horses, if you can find riders for them.'",
      "T": "'Two thousand horses — if you can even find the men to ride them.' The mockery is the point: Judah's military is so depleted that even a generous gift of horses would be useless for lack of cavalry. The challenge is contemptuous."
    },
    "24": {
      "L": "How then wilt thou turn away the face of one captain of the least of my master's servants, and put thy trust on Egypt for chariots and for horsemen?",
      "M": "'How can you repel even one of the least of my master's officers? Yet you are counting on Egypt for chariots and cavalry!'",
      "T": "'You cannot face the least of Assyria's officers — yet you are trusting Egypt's cavalry.' Three lines of attack, each devastating: no military strength, no reliable ally, and now even a single Assyrian officer would suffice to crush them. The rhetoric was designed to induce surrender by making resistance feel hopeless."
    },
    "25": {
      "L": "Am I now come up without the LORD against this place to destroy it? The LORD said to me, Go up against this land, and destroy it.",
      "M": "'Do you think I came up against this place without the LORD's authority? The LORD himself told me: Go up against this land and destroy it.'",
      "T": "'The LORD sent me.' The Rabshakeh's masterstroke: the claim that the God of Israel had commissioned the Assyrian invasion. Perhaps he had heard of Isaiah's 'the Assyrian, the rod of my anger' (Isa 10:5-6) — or perhaps this was pure improvised propaganda. Either way, it was the most unsettling argument of all: what if God himself is against you?"
    },
    "26": {
      "L": "Then said Eliakim the son of Hilkiah, and Shebna, and Joah, unto Rabshakeh, Speak, I pray thee, to thy servants in the Syrian language; for we understand it; and talk not with us in the Jews' language in the ears of the people that are on the wall.",
      "M": "Then Eliakim son of Hilkiah, Shebna, and Joah said to the Rabshakeh, 'Please speak to us in Aramaic, since we understand it. Don't speak Hebrew within the hearing of the people on the wall.'",
      "T": "The Judean officials understood exactly what was happening: the Rabshakeh was not negotiating — he was conducting psychological warfare aimed at the defenders on the wall. The Hebrew was deliberate, meant to reach the common people. Eliakim's request to switch to Aramaic (the diplomatic language of the ancient Near East) was an attempt to contain the damage before it demoralized the garrison."
    },
    "27": {
      "L": "But Rabshakeh said unto them, Hath my master sent me to thy master, and to thee, to speak these words? hath he not sent me to the men which sit on the wall, that they may eat their own dung, and drink their own piss with you?",
      "M": "But the Rabshakeh replied, 'Did my master send me to speak these things only to you and your master? Wasn't it also to the men on the wall — who will have to eat their own excrement and drink their own urine along with you in the siege?'",
      "T": "'My message is for the people on the wall.' The refusal was deliberate and brutal — the reference to eating dung and drinking urine painted the horror of a prolonged siege in visceral terms. The Rabshakeh was a master of psychological warfare: give the population enough fear of starvation, and surrender becomes attractive."
    },
    "28": {
      "L": "Then Rabshakeh stood and cried with a loud voice in the Jews' language, and spake, saying, Hear the word of the great king, the king of Assyria.",
      "M": "The Rabshakeh then stood and shouted in Hebrew at the top of his voice: 'Listen to what the great king, the king of Assyria, says!'",
      "T": "Ignoring the request entirely, the Rabshakeh raised his voice and addressed the walls directly in Hebrew. The diplomatic pretense was over; this was now direct psychological assault on the city's defenders."
    },
    "29": {
      "L": "Thus saith the king, Let not Hezekiah deceive you; for he shall not be able to deliver you out of his hand.",
      "M": "'The king's message: Don't let Hezekiah mislead you. He cannot rescue you from my power.'",
      "T": "'Don't trust Hezekiah.' The word is 'deceive' — he reframes Hezekiah's trust in the LORD as a deception of the people. Every piece of the speech targets the one thing the Rabshakeh fears: that faith might hold."
    },
    "30": {
      "L": "Neither let Hezekiah make you trust in the LORD, saying, The LORD will surely deliver us, and this city shall not be delivered into the hand of the king of Assyria.",
      "M": "'Don't let Hezekiah persuade you to trust in the LORD by saying, \"The LORD will certainly rescue us; this city will not fall to the king of Assyria.\"'",
      "T": "'The LORD will deliver us' — the Rabshakeh quotes what he imagines Hezekiah is saying to the people. He understands that Hezekiah's leadership is rooted in theological confidence, and he is trying to undermine it directly. He is attacking faith itself."
    },
    "31": {
      "L": "Hearken not to Hezekiah; for thus saith the king of Assyria, Make an agreement with me by a present, and come out to me, and then eat ye every man of his own vine, and every one of his fig tree, and drink ye every one the waters of his cistern;",
      "M": "'Don't listen to Hezekiah. The king of Assyria says: Make peace with me, surrender, and everyone will eat from his own vine and fig tree and drink water from his own cistern.'",
      "T": "'Come out to me, and you will have peace.' The Rabshakeh now shifts to seduction: the vine and fig tree are the biblical image of covenant shalom (1 Kgs 4:25; Mic 4:4; Zech 3:10). He was offering Israel's own covenant vocabulary as the reward for surrender — the devil's use of scripture: the good thing, obtained by betrayal."
    },
    "32": {
      "L": "Until I come and take you away to a land like your own land, a land of corn and wine, a land of bread and vineyards, a land of oil-olive and of honey, that ye may live, and not die; and hearken not unto Hezekiah, when he persuadeth you, saying, The LORD will deliver us.",
      "M": "'Then I will come and take you to a land just like your own — a land of grain, wine, bread, vineyards, olive trees, and honey. Choose life, not death. Do not listen to Hezekiah when he says, \"The LORD will deliver us.\"'",
      "T": "'A land like your own' — the description echoes the promised land of Deuteronomy 8:7-10 (grain, wine, olive oil, honey). The Rabshakeh was offering an Assyrian version of the Promised Land. The lie was seductive precisely because it borrowed from Israel's own theology of the good land. Then the climax: 'Do not listen to Hezekiah when he says the LORD will deliver us' — naming the one thing that would make resistance possible, and urging the people to reject it."
    },
    "33": {
      "L": "Hath any of the gods of the nations delivered at all his land out of the hand of the king of Assyria?",
      "M": "'Has any god of the nations ever rescued his land from the king of Assyria?'",
      "T": "'Name one.' The gods of every nation Assyria had defeated had failed to protect their people. From the Assyrian perspective this was an empirical observation: the gods had always been overcome. The Rabshakeh's category error was treating the LORD as one more national deity among many — and he would learn otherwise."
    },
    "34": {
      "L": "Where are the gods of Hamath, and of Arpad? where are the gods of Sepharvaim, Hena, and Ivah? have they delivered Samaria out of mine hand?",
      "M": "'Where are the gods of Hamath and Arpad? Where are the gods of Sepharvaim, Hena, and Ivvah? Did they rescue Samaria from me?'",
      "T": "'Samaria fell.' The most powerful single argument: the northern kingdom, whose god the Samaritan deportees were supposedly now learning to worship, had just been destroyed. The Rabshakeh does not know — cannot know — the narrator's answer: Samaria fell because of covenant violation, not because of divine weakness."
    },
    "35": {
      "L": "Who are they among all the gods of the countries, that have delivered their country out of mine hand, that the LORD should deliver Jerusalem out of mine hand?",
      "M": "'Which of all the gods of these lands has rescued his territory from me? How then will the LORD rescue Jerusalem from me?'",
      "T": "'No god has ever stopped me.' The inductive argument from history: every nation, every god, every city has fallen to Assyria. Why should Jerusalem be different? It is a powerful argument, and it assumes the LORD is simply another national deity. Hezekiah's prayer in the next chapter (19:15-19) directly corrects this: 'You alone are God; you made heaven and earth.' A god who made heaven and earth is in a different category from the gods of Hamath."
    },
    "36": {
      "L": "But the people held their peace, and answered him not a word; for the king's commandment was, saying, Answer him not.",
      "M": "The people remained silent and said nothing in reply, because the king had ordered, 'Do not answer him.'",
      "T": "Silence — disciplined, deliberate silence. Hezekiah had anticipated the speech and given the instruction: do not engage. The silence was not helplessness; it was strategic. Faith does not need to answer every taunt. The people's silence is itself a form of trust."
    },
    "37": {
      "L": "Then came Eliakim the son of Hilkiah, which was over the household, and Shebna the scribe, and Joah the son of Asaph the recorder, to Hezekiah with their clothes rent, and told him the words of Rabshakeh.",
      "M": "Eliakim son of Hilkiah, the palace administrator, Shebna the secretary, and Joah son of Asaph the recorder came to Hezekiah with their clothes torn and reported what the Rabshakeh had said.",
      "T": "They came back to Hezekiah with torn clothes — the ancient sign of grief and distress. The speech had been devastating; they could not pretend otherwise. The burden of the Rabshakeh's words now fell on the king. What Hezekiah does next, in chapter 19, is the answer of faith under pressure."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '2kings')
        merge_tier(existing, KINGS2, tier_key)
        save(tier_dir, '2kings', existing)
    print('2 Kings 16–18 written.')

if __name__ == '__main__':
    main()
