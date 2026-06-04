"""
MKT 2 Chronicles chapters 7–12 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-2chronicles-7-12.py

Content:
- Ch 7:  The divine fire descends; the night vision — conditional covenant (bless / curse)
- Ch 8:  Solomon's building projects; Levitical order; Ophir trade
- Ch 9:  Queen of Sheba; Solomon's wealth and wisdom; death of Solomon
- Ch 10: Rehoboam at Shechem; the kingdom divides
- Ch 11: Rehoboam fortifies Judah; priests and Levites migrate south; royal household
- Ch 12: Shishak's invasion; humbling and partial deliverance; Rehoboam's death

Translation decisions (carried forward from mkt-2chronicles-1-6.py):
- H3068 (יהוה): "LORD" in L/M; "the LORD" in T. Consistent with all prior OT scripts.
- H430 (אֱלֹהִים): "God" throughout all tiers.
- H2617 (חֶסֶד): "steadfast love" in L/M; "covenant loyalty" in T.
- H3519 (כָּבוֹד, "glory"): "glory" in L/M; T surfaces the weight and overwhelming presence.
- H1285 (בְּרִית): "covenant" throughout.
- H5178 (נְחֹשֶׁת): "bronze" throughout (not "brass").
- H8034 (שֵׁם): "name" — the Name-theology continues: the temple is the house of the Name.
- H7307 (רוּחַ): "spirit" (lower-case) at 9:4 where it means vital force/breath, not the divine Spirit.

New decisions for chs 7–12:
- H784 (אֵשׁ): "fire" — the fire from heaven at 7:1 is the divine response to Solomon's prayer,
  echoing the fire that consumed Elijah's sacrifice (1 Kgs 18:38) and the Mosaic tabernacle
  dedication (Lev 9:24). T notes all three echoes.
- H4725 (מָקוֹם) at 7:12, 15: "this place" — the Deuteronomic formula; carries full covenant weight.
- "If my people" (7:14): the famous conditional promise. L preserves the Hebrew conditional
  structure (four verbs: humble, pray, seek, turn). M renders naturally. T expounds the
  theological center: this verse is the hermeneutical key to all of Chronicles.
- H7346 (Rehoboam): "Rehoboam" throughout — no translation needed.
- H3379 (Jeroboam): "Jeroboam" throughout.
- H5923 (עֹל): "yoke" — political servitude metaphor; T surfaces the exodus resonance
  (Deut 28:48 — the curse of servitude under a foreign yoke for covenant unfaithfulness).
- H7895 (Shishak): "Shishak" — Egyptian pharaoh (Shoshenq I, ~925 BC). T notes the irony:
  Egypt, the house of slavery, returns to claim tribute from Israel's king.
- H2186 (Jeroboam's expulsion of Levites): "cast them off" at 11:14 is H2186 (zarah, reject/
  expel). The Levites' migration south was a theological self-selection: faithfulness to the
  LORD's worship drew them to where that worship was maintained. T expounds.
- H3665 (humble/humbled): key theological verb in ch 12. The Chronicler's pattern throughout:
  humility before the LORD turns judgment; pride invites it. T surfaces this as the
  Chronicler's governing principle for reading kingship.
- Aspect notes:
  - Ch 7 night vision: God's conditional clauses use qatal (completed acts as conditions) and
    imperfect jussives (divine responses). Rendered as indicative conditionals + future responses.
  - Ch 10 young-men speech: imperfect with waw-consecutive shows Rehoboam's intention;
    their speech uses perfect tense for the father's burden (confirmed fact).
  - Ch 12 verbs of humbling: niphal reflexive ("they humbled themselves") — the passive/
    reflexive distinction matters theologically: God does not humble them; they humble themselves.
- OT intertextuality:
  - 7:1: Fire from heaven echoes Lev 9:24 (tabernacle dedication) and 1 Kgs 18:38 (Elijah/
    Carmel). The temple receives the same divine authentication as the tabernacle and the
    prophetic challenge to Baal — three moments where fire from heaven ratifies worship.
  - 7:14: "my people who are called by my name" — echoes Deut 28:10 and Jer 14:9. The phrase
    is a covenant-identity marker: Israel is the people over whom the divine name is called.
  - 7:18: "as I covenanted with David your father" — the Davidic covenant (2 Sam 7; 1 Chr 17)
    remains the structural backbone of the Chronicler's theology.
  - 9:1-12: The Queen of Sheba episode is a literary chiasm with Solomon's wisdom at the center.
    Her confession in v. 8 ("because your God loved Israel to establish them forever") is the
    Chronicler's theological peak: even the foreign queen perceives the love of God for Israel.
  - 10:15: "the thing was from God" — the Chronicler inserts the divine sovereignty formula at
    the kingdom's division. What looks like Rehoboam's political folly is God fulfilling the
    word through Ahijah (1 Kgs 11:29-31). History is not random; judgment has a shape.
  - 12:8: "the service of the kingdoms of the countries" vs. God's service — the Chronicler's
    theological commentary: servitude is never abolished, only redirected. Those who refuse
    God's easy yoke will bear the weight of earthly ones.
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
  "7": {
    "1": {
      "L": "When Solomon had finished praying, fire came down from heaven and consumed the burnt offering and the sacrifices, and the glory of the LORD filled the temple.",
      "M": "When Solomon finished praying, fire descended from heaven and consumed the burnt offering and the sacrifices, and the glory of the LORD filled the temple.",
      "T": "The moment Solomon's prayer ended, the answer came not in words but in fire. Fire from heaven devoured the offerings on the altar, and the overwhelming glory of the LORD flooded the temple. This was the same divine authentication that had consecrated the tabernacle at its dedication (Lev 9:24) and vindicated Elijah against the prophets of Baal (1 Kgs 18:38). God had accepted the temple. The building project was ratified not by a royal decree but by fire from above."
    },
    "2": {
      "L": "And the priests could not enter the house of the LORD, because the glory of the LORD filled the house of the LORD.",
      "M": "The priests could not enter the LORD's house, because the glory of the LORD had filled it.",
      "T": "The glory was not decorative — it was present, overwhelming, and physically impassable. The priests, the most prepared and consecrated men in Israel, could not cross the threshold. This had happened once before at the tabernacle's dedication (Exod 40:34-35): the cloud of glory was too full for any human to enter. The repetition is the point. The God who filled the wilderness tent had now taken up residence in his permanent house."
    },
    "3": {
      "L": "When all the children of Israel saw the fire come down and the glory of the LORD on the house, they bowed with their faces to the ground on the pavement and worshiped and gave thanks to the LORD, saying, 'For he is good, for his steadfast love endures forever.'",
      "M": "When all the Israelites saw the fire descend and the glory of the LORD on the temple, they bowed to the ground, faces down on the pavement, and worshiped and praised the LORD, saying, 'He is good; his steadfast love endures forever.'",
      "T": "All Israel saw it — the fire, the glory descending on the temple they had helped build. They did not stand and applaud; they fell. Faces to the stone pavement, prostrate before the holiness of the LORD. And they sang the ancient refrain — the same song the Levites had sung when the ark was brought in (5:13), the simplest and most comprehensive statement of Israel's theology: he is good; his covenant loyalty never ends. The building program was complete. The worship had begun."
    },
    "4": {
      "L": "Then the king and all the people offered sacrifices before the LORD.",
      "M": "Then the king and all the people offered sacrifices before the LORD.",
      "T": "King and people together — no distinction of rank at the altar. In the moment of dedication, Rehoboam's future pride and the people's future unfaithfulness are still unwritten. Here they are what they were meant to be: a worshiping community before the LORD, together."
    },
    "5": {
      "L": "King Solomon offered a sacrifice of twenty-two thousand oxen and a hundred and twenty thousand sheep. So the king and all the people dedicated the house of God.",
      "M": "King Solomon offered twenty-two thousand oxen and a hundred and twenty thousand sheep as sacrifices. So the king and all the people dedicated the house of God.",
      "T": "Twenty-two thousand oxen. A hundred and twenty thousand sheep. Numbers that stretch comprehension — not a ceremony but a national outpouring. The scale of the sacrifice was the scale of the thanksgiving. Israel was dedicating not just a building but their entire future, their covenantal identity, their hope of divine presence in the land. Everything they had was laid on the altar."
    },
    "6": {
      "L": "The priests stood at their posts; the Levites also with instruments of music to the LORD that King David had made for giving thanks to the LORD — for his steadfast love endures forever — whenever David offered praises by their ministry. Opposite them the priests sounded trumpets, and all Israel stood.",
      "M": "The priests stood at their assigned positions, and the Levites with the musical instruments that King David had made for praising the LORD — 'for his steadfast love endures forever' — played whenever David used them for praise. Opposite them the priests blew the trumpets, while all Israel stood.",
      "T": "The Levitical musicians took up the instruments David had crafted — instruments dedicated to a single purpose: the praise of God's covenant loyalty. The refrain that David had written into Israel's liturgy ('his steadfast love endures forever') was sung in the moment the temple received its God. Music was not performance but proclamation. The trumpets answered the singing. All Israel stood — not passive spectators but participants in the greatest act of worship the nation had ever offered."
    },
    "7": {
      "L": "Solomon consecrated the middle of the court that was before the house of the LORD, for there he offered the burnt offerings and the fat of the peace offerings, because the bronze altar that Solomon had made was not able to receive the burnt offerings, the grain offerings, and the fat.",
      "M": "Solomon also consecrated the middle of the courtyard in front of the LORD's house for burnt offerings, because the bronze altar was too small to hold all the burnt offerings, grain offerings, and fat portions.",
      "T": "Even the great bronze altar — twenty cubits square, ten cubits high — was insufficient for the volume of worship the people brought. So Solomon consecrated additional ground, the open court itself became sacred space. When the worship overflows the designated vessels, you consecrate more space. The overflow was not a problem to be managed but an abundance to be received."
    },
    "8": {
      "L": "So Solomon held the feast at that time for seven days, and all Israel with him, a very great assembly, from Lebo-hamath to the Brook of Egypt.",
      "M": "So Solomon and all Israel with him — a very great assembly — celebrated the feast at that time for seven days, from Lebo-hamath to the Wadi of Egypt.",
      "T": "Seven days of feasting — the entire nation from its northernmost border (Lebo-hamath, where Hamath meets Israel in the far north) to its southernmost reach (the Wadi of Egypt on the Sinai frontier). All Israel. The geographic formula is deliberate: it invokes the full extent of the Davidic realm, the land as promised and possessed. The dedication feast was not a local event but a national one, the whole people celebrating the house that belonged to all of them."
    },
    "9": {
      "L": "On the eighth day they held a solemn assembly, for they had kept the dedication of the altar seven days and the feast seven days.",
      "M": "On the eighth day they held a closing assembly, having observed the altar's dedication for seven days and the feast for seven days.",
      "T": "Fourteen days total — seven for the altar's dedication and seven for the Feast of Booths (Sukkot, the seventh-month festival). Then an eighth day of solemn assembly, the sacred pause at the end of the feast. The number eight in Israel's calendar signified the day beyond the week — new beginning, renewal, the future breaking in beyond the ordinary cycle of seven. The dedication concluded on a note of holy anticipation."
    },
    "10": {
      "L": "On the twenty-third day of the seventh month he sent the people away to their tents, joyful and glad of heart for the goodness that the LORD had shown to David and Solomon and to Israel his people.",
      "M": "On the twenty-third day of the seventh month Solomon dismissed the people to their homes. They went away joyful and glad, thankful for the prosperity the LORD had granted to David, to Solomon, and to his people Israel.",
      "T": "The people went home joyful. Not relieved that it was over, not exhausted by the ceremonies — joyful. They had witnessed fire from heaven, the glory of God, sacrifices beyond counting, fourteen days of worship and feast. And they understood what it meant: the LORD had been good to David, to Solomon, to them. The goodness of God was not abstract but visible, audible, touchable. They had lived inside it for two weeks. They carried it home."
    },
    "11": {
      "L": "Thus Solomon finished the house of the LORD and the king's house. And all that came into Solomon's heart to make in the house of the LORD and in his own house he accomplished successfully.",
      "M": "Solomon had now finished the house of the LORD and the royal palace. Everything he set his heart to do in the LORD's house and his own house he carried out successfully.",
      "T": "Finished and successful — two words that close Solomon's building project. Everything David had prepared for, everything Solomon had planned and built and dedicated — completed. The Chronicler's assessment is unqualified: all that was in Solomon's heart, he accomplished. It is a rare and full benediction. The temple that began as a dream in David's heart, was handed to Solomon as an assignment, and has now been received by the fire and glory of God — finished. The rest of Solomon's reign will be measured against this moment."
    },
    "12": {
      "L": "Then the LORD appeared to Solomon in the night and said to him: 'I have heard your prayer and have chosen this place for myself as a house of sacrifice.'",
      "M": "Then the LORD appeared to Solomon at night and told him: 'I have heard your prayer and have chosen this place as my house of sacrifice.'",
      "T": "God came a second time to Solomon by night — as he had come at Gibeon after the thousand offerings (1:7). The pattern is the same: extravagant worship, then the night vision. God's first words are a direct response to the prayer of chapter 6: I have heard. Not 'I have considered' or 'I was moved' — I have heard. And I have chosen this place. The long period of unchosen-ness (6:5) is now definitively over. This house, this city, this place — chosen."
    },
    "13": {
      "L": "'When I shut up the heavens so that there is no rain, or command the locust to devour the land, or send pestilence among my people,'",
      "M": "'Whenever I close the sky so that there is no rain, or command locusts to consume the land, or send plague among my people,'",
      "T": "God speaks first of judgment, not blessing. The conditional structure begins on the dark side: drought, locusts, pestilence. These are the covenant curses of Deuteronomy 28 — the consequences of unfaithfulness catalogued by Moses. God is not promising that these things will happen; he is acknowledging that when they do (as they will, because Israel will sin), there is a way back. The covenant curses are not the end of the story."
    },
    "14": {
      "L": "'if my people who are called by my name humble themselves, and pray and seek my face and turn from their wicked ways, then I will hear from heaven and will forgive their sin and heal their land.'",
      "M": "'if my people who bear my name will humble themselves, pray, seek my face, and turn from their evil ways, then I will hear from heaven, forgive their sin, and restore their land.'",
      "T": "Four conditions, one promise. The four verbs of return: humble yourselves — acknowledge your place before God; pray — bring words to him; seek my face — orient everything toward him; turn from evil — let the orientation change the life. Not one condition but four, a complete turning. And the response: I will hear from heaven — God is still present, still listening; I will forgive — guilt is dealt with; I will heal their land — the created order is restored when the covenant relationship is restored. This verse became the hermeneutical key to all of Chronicles: every king is measured by whether the people fulfill these four conditions. Every catastrophe opens toward this door."
    },
    "15": {
      "L": "'Now my eyes will be open and my ears attentive to the prayer offered in this place.'",
      "M": "'Now my eyes will be open and my ears attentive to every prayer made in this place.'",
      "T": "Eyes open, ears attentive — permanently, unconditionally, regardless of what else is happening in the nation. The temple is the address of God's attentiveness. Whatever his judgments bring, whatever his curses enforce, this one commitment stands: when prayer rises from this place toward heaven, God is listening. The temple is not a magic charm against judgment but a covenant guarantee of access."
    },
    "16": {
      "L": "'For now I have chosen and consecrated this house that my name may be there forever. My eyes and my heart will be there for all time.'",
      "M": "'I have now chosen and consecrated this house so that my name may rest here forever. My eyes and my heart will always be here.'",
      "T": "The divine commitment is threefold: chosen, consecrated, attentive. God has not merely permitted this house to exist; he has actively chosen and set it apart. His name dwells here. His eyes watch here. His heart is engaged here. The temple is not an architectural achievement that God graciously endorses; it is the address of the divine attention, the focal point of the covenant relationship. 'My heart will be there for all time' is the warmest possible description of what God feels about this place."
    },
    "17": {
      "L": "'And as for you, if you walk before me as David your father walked, doing according to all that I have commanded you and keeping my statutes and my rules,'",
      "M": "'As for you, if you walk before me as your father David did — following all my commands and keeping my statutes and ordinances —'",
      "T": "The blessing condition for Solomon specifically: walk as David walked. The Chronicler's David is not a morally perfect figure but a man who, despite failures, maintained the fundamental orientation of his heart toward God. 'Walk before me' is the covenant idiom for a life lived in conscious awareness of the divine presence. The Davidic standard is not perfection but direction: the heart pointed toward God."
    },
    "18": {
      "L": "'then I will establish your royal throne as I covenanted with David your father, saying, \"You shall not lack a man to rule Israel.\"'",
      "M": "'then I will confirm your royal throne, as I promised your father David: \"You will always have a man to rule Israel.\"'",
      "T": "The covenant promise to David is restated for Solomon: a man on the throne of Israel — the Davidic line unbroken. The condition is covenantal obedience; the promise is dynastic continuity. The Chronicler's readers know how this story ends — the line was not maintained, the exile came. But the promise itself stands beyond any particular king's faithfulness. What Solomon is offered here is not merely a political arrangement but participation in the great covenant that runs from David to the Messiah who would sit on David's throne without end."
    },
    "19": {
      "L": "'But if you turn aside and forsake my statutes and my commandments that I have set before you, and go and serve other gods and worship them,'",
      "M": "'But if you turn away and abandon my decrees and commands that I have given you, and go and serve other gods and worship them,'",
      "T": "The dark side of the covenant. The conditional structure does not allow for a one-sided promise; the covenant has two faces. If you turn — the verb is shub, the same word used for repentance, here describing apostasy: turning away from God rather than toward him. Forsake the commandments; serve other gods. The Chronicler's readers will see this pattern play out in generation after generation of kings in the chapters that follow."
    },
    "20": {
      "L": "'then I will pluck you up from my land that I have given you, and this house that I have consecrated for my name I will cast out of my sight, and I will make it a proverb and a byword among all peoples.'",
      "M": "'then I will uproot Israel from my land that I gave them, and will reject this house I have consecrated for my name. I will make it a proverb and a mockery among all nations.'",
      "T": "The covenant curse is proportional to the covenant blessing: as the temple was chosen and consecrated, so it can be rejected and destroyed. 'My land' — God owns the land; Israel holds it conditionally. To be uprooted from it is to lose not just territory but the covenant relationship that the land represents. The temple, God's chosen house, can become a byword among the nations — the greatest shame imaginable, the house of the holy God become a punchline, a cautionary tale. The Chronicler's readers know that this happened. They are reading these words after the exile."
    },
    "21": {
      "L": "'And at this house, which was exalted, everyone passing by will be astonished and say, \"Why has the LORD done thus to this land and to this house?\"'",
      "M": "'Everyone who passes by this temple, which was so magnificent, will be appalled and ask, \"Why did the LORD do this to this land and this house?\"'",
      "T": "The ruined temple as sermon. Passersby will stop, stare at the wreckage, and ask the theological question: why? The ruin will preach. The very magnificence that made the temple a declaration of God's greatness will make its destruction a declaration of his justice. The question the nations ask is not rhetorical — it demands an answer."
    },
    "22": {
      "L": "'Then they will say, \"Because they forsook the LORD, the God of their fathers who brought them out of the land of Egypt, and laid hold of other gods and worshiped them and served them — therefore he has brought all this disaster on them.\"'",
      "M": "'The answer will be: \"Because they abandoned the LORD, the God of their ancestors who brought them out of Egypt, and they embraced other gods and worshiped and served them — that is why he brought all this disaster on them.\"'",
      "T": "The answer to the passerby's question is simple and devastating: because they forsook the LORD. The God who brought them out of Egypt — the identity marker, the foundational act of covenant — was abandoned. They reached for other gods. The disaster is not inexplicable divine violence; it is the covenant working exactly as it was designed. The exile is not the failure of God's plan but its fulfillment. The sermon that the ruined temple preaches is the same sermon Moses preached in Deuteronomy: faithfulness leads to life; unfaithfulness leads to this."
    }
  },
  "8": {
    "1": {
      "L": "At the end of twenty years, in which Solomon had built the house of the LORD and his own house,",
      "M": "At the end of the twenty years it took Solomon to build the LORD's house and his own palace,",
      "T": "Twenty years — the number marks the completion of the entire building program. The temple took seven years, the palace thirteen (1 Kgs 6:38–7:1). Now both are done, and a new phase of Solomon's reign begins. The Chronicler signals this transition precisely: twenty years, and then."
    },
    "2": {
      "L": "Solomon rebuilt the cities that Huram had given to him and settled the people of Israel in them.",
      "M": "Solomon rebuilt the towns that Huram had given him and settled Israelites in them.",
      "T": "Huram of Tyre had given Solomon twenty cities in Galilee (1 Kgs 9:11-13; that passage records Huram's disappointment with the gift, calling them Cabul — 'as good as nothing'). The Chronicler reverses the transaction's direction: Solomon rebuilt these cities and populated them with Israelites. Territory was not left empty; the land was occupied, developed, and settled. Solomon's building extended beyond Jerusalem and the temple."
    },
    "3": {
      "L": "And Solomon went to Hamath-zobah and took it.",
      "M": "Solomon marched to Hamath-zobah and captured it.",
      "T": "Hamath-zobah — a city-state at the northern edge of Solomon's sphere, where the Orontes River region met the upper Euphrates. Solomon's military campaign here extended Israelite control to its northernmost reach. The peaceable builder was also capable of strategic force when the borders required it."
    },
    "4": {
      "L": "He built Tadmor in the wilderness and all the store cities that he built in Hamath.",
      "M": "He built Tadmor in the desert and all the store cities he established in Hamath.",
      "T": "Tadmor (later called Palmyra by the Romans) — a desert oasis city on the trade route between the Euphrates and Damascus, strategically positioned to control commerce between Mesopotamia and the Mediterranean. To build Tadmor was to plant Israel's flag at a key junction of the ancient world's commercial network. Solomon was not only a temple builder but an empire builder who understood geography."
    },
    "5": {
      "L": "He also built Upper Beth-horon and Lower Beth-horon, fortified cities with walls, gates, and bars,",
      "M": "He built Upper and Lower Beth-horon as fortified cities with walls, gates, and bars,",
      "T": "The two Beth-horons guarded the main pass from the coastal plain up to Jerusalem — the strategic defile that Joshua had defended against the Amorites (Josh 10:10-11). To fortify both upper and lower Beth-horon was to seal the western approach to the capital. Every fortified city Solomon built was a piece of a deliberate strategic architecture."
    },
    "6": {
      "L": "and Baalath, and all the store cities that Solomon had, and all the cities for his chariots and the cities for his horsemen, and all that Solomon desired to build in Jerusalem, in Lebanon, and in all the land of his dominion.",
      "M": "Baalath, and all his store cities, the cities for his chariot forces and cavalry, and everything Solomon wanted to build in Jerusalem, in Lebanon, and throughout his entire realm.",
      "T": "The scope is imperial: store cities stocked with provisions and weapons, chariot cities housing military assets, Lebanon where the timber came from — all of it under Solomon's hand, all of it deliberately developed. The Chronicler presents this as the fruit of wisdom and wealth rather than as a warning, though the multiplication of chariots and horses still carries the shadow of Deuteronomy 17:16."
    },
    "7": {
      "L": "All the people who were left of the Hittites, the Amorites, the Perizzites, the Hivites, and the Jebusites, who were not of Israel,",
      "M": "As for all the non-Israelite peoples left in the land — the Hittites, Amorites, Perizzites, Hivites, and Jebusites —",
      "T": "The list of Canaanite peoples echoes the original conquest lists of Joshua. These were the nations Israel had been commanded to displace; those who remained were absorbed into the labor force. The Chronicler notes their status carefully: not Israelites, but present and conscripted."
    },
    "8": {
      "L": "from their descendants who were left after them in the land, whom the people of Israel had not destroyed — these Solomon drafted as forced laborers, as they are to this day.",
      "M": "their descendants remaining in the land after Israel had not fully eliminated them — Solomon conscripted these as forced laborers, as they still are today.",
      "T": "What Israel's military had not completed, Solomon's administration organized. The remaining Canaanite populations became the labor pool for the building projects. The Chronicler's 'as they are to this day' is an editorial note anchoring the reader in the Chronicler's own time — a practice that continued into the Persian period."
    },
    "9": {
      "L": "But of the people of Israel Solomon did not make any as slaves for his work; they were soldiers, and his officers, the commanders of his chariot force and his horsemen.",
      "M": "Solomon did not conscript Israelites as slaves for his work. They served as soldiers, officers, commanders of his chariots, and cavalry.",
      "T": "The distinction is sharp and theologically significant: Israelites were not enslaved. The memory of Egypt was too recent and too defining for Israel's king to repeat it with his own people. Israelites bore weapons and wore ranks; non-Israelites bore loads and cut stone. The Exodus shaped the structure of the kingdom."
    },
    "10": {
      "L": "And these were the chief officers of King Solomon, two hundred and fifty, who exercised authority over the people.",
      "M": "Solomon had two hundred and fifty chief officers who supervised the workers.",
      "T": "Two hundred and fifty overseers — the administrative tier that translated royal commands into actual construction. Every beam placed, every stone cut, every worker fed required someone in the middle keeping the system running. The temple was built not only by craftsmen and laborers but by managers, foremen, and administrators. Solomon's organizational capacity was as much a gift from God as his wisdom for judgment."
    },
    "11": {
      "L": "Solomon brought Pharaoh's daughter up from the city of David to the house that he had built for her, for he said, 'My wife shall not live in the house of David king of Israel, for the places to which the ark of the LORD has come are holy.'",
      "M": "Solomon moved Pharaoh's daughter from the city of David to the palace he had built for her. He said, 'My wife must not live in the house of David king of Israel, because the places where the LORD's ark has entered are holy.'",
      "T": "A remarkable sentence. Solomon builds his Egyptian wife her own palace precisely because he understands that the city of David — where the ark had dwelt in David's tent — is holy ground, and holiness makes demands on what coexists with it. The reasoning is theologically careful: the ark's presence sanctifies the space around it, and a foreign queen who does not share Israel's covenant cannot occupy that space. Solomon is not rejecting his wife; he is honoring the holiness of the ark. The irony is that his marriage to Pharaoh's daughter will later be cited as the beginning of his downfall (1 Kgs 11:1) — but here, in this moment, he is trying to manage the tension well."
    },
    "12": {
      "L": "Then Solomon offered up burnt offerings to the LORD on the altar of the LORD that he had built before the vestibule,",
      "M": "Solomon then offered burnt offerings to the LORD on the altar he had built in front of the portico.",
      "T": "The worship schedule resumes after the building narrative. Solomon fulfilled his priestly role — not personally slaughtering the animals (that was the priests' work) but ordering and presenting the offerings before the LORD. The king as worship-initiator: this is the Chronicler's Solomon, a man whose every dimension is oriented toward the temple."
    },
    "13": {
      "L": "as the duty of each day required, offering according to the commandment of Moses for the Sabbaths, the new moons, and the three annual feasts — the Feast of Unleavened Bread, the Feast of Weeks, and the Feast of Booths.",
      "M": "following the daily schedule, and offering according to Moses's command on Sabbaths, new moons, and the three annual festivals: Unleavened Bread, Weeks, and Booths.",
      "T": "The Mosaic calendar in full: daily offerings, weekly Sabbaths, monthly new moons, and the three pilgrimage festivals — Passover/Unleavened Bread in the spring, Weeks (Pentecost) at the grain harvest, and Booths at the fall ingathering. Solomon did not invent his own liturgical calendar; he inherited and maintained the one God gave through Moses. Fidelity to the pattern was itself a form of worship."
    },
    "14": {
      "L": "He appointed, according to the ruling of David his father, the divisions of the priests for their service, and the Levites for their offices to praise and minister before the priests as the duty of each day required, and the gatekeepers in their divisions for each gate, for so David the man of God had commanded.",
      "M": "Following his father David's regulations, he set up the priestly divisions for their duties and the Levites for their ministry — to lead praise and serve alongside the priests as each day required — and the gatekeepers by their divisions at each gate. This was the command of David, the man of God.",
      "T": "David's organizational blueprint — the priestly courses, Levitical assignments, and gate rotations established in 1 Chronicles 23-26 — is now implemented in the running temple. Solomon did not redesign the system; he executed his father's plan faithfully. The Chronicler calls David 'the man of God' — a title otherwise reserved for Moses and prophets. David was not merely a king who planned the temple; he was a man whose organizational vision for worship was itself divinely inspired."
    },
    "15": {
      "L": "And they did not deviate from the command of the king to the priests and Levites concerning any matter or concerning the treasuries.",
      "M": "Neither the priests nor the Levites deviated from the king's commands in any matter, including the care of the treasuries.",
      "T": "Perfect institutional compliance — and the Chronicler reports it as a good thing. Obedience to the established order of worship, maintaining the system David designed and Solomon implemented, was faithfulness. The freedom to improvise in worship was not prized; the freedom to follow the pattern precisely was."
    },
    "16": {
      "L": "Thus all the work of Solomon was carried out from the day the foundation of the house of the LORD was laid until it was finished. So the house of the LORD was completed.",
      "M": "So all of Solomon's work was carried out from the day the LORD's house was founded to the day it was finished — and the house of the LORD was complete.",
      "T": "From foundation to completion — the arc of the temple project summarized in one sentence. The Chronicler does not move on until he has said it clearly: finished, complete. Whatever complications come next in Solomon's reign, whatever failures or compromises, the temple stands as a permanent marker of what was accomplished. The house of the LORD was complete."
    },
    "17": {
      "L": "Then Solomon went to Ezion-geber and Eloth on the shore of the sea, in the land of Edom.",
      "M": "Then Solomon traveled to Ezion-geber and Eloth on the coast of the Red Sea in the land of Edom.",
      "T": "Ezion-geber (near modern Aqaba) — Israel's Red Sea port, the gateway to the Indian Ocean trade routes. Solomon's commercial ambition extended to the southern seas. Eloth on the Edomite coast gave access to Arabia, Africa, and the riches of the ancient maritime world."
    },
    "18": {
      "L": "And Huram sent him by the hand of his servants ships and servants familiar with the sea, and they went to Ophir together with the servants of Solomon and brought from there four hundred and fifty talents of gold and brought it to King Solomon.",
      "M": "Huram sent him ships crewed by his experienced sailors. Together with Solomon's servants they sailed to Ophir and brought back four hundred and fifty talents of gold to King Solomon.",
      "T": "Four hundred and fifty talents of gold — roughly 16 tons — from a single expedition to Ophir (location debated: southern Arabia, East Africa, or India). Huram's Phoenician sailors, the best navigators of the ancient world, partnered with Solomon's expedition. The Tyrian alliance that built the temple also funded the treasury. The partnership of wisdom and commercial expertise produced results neither could have achieved alone."
    }
  },
  "9": {
    "1": {
      "L": "Now when the queen of Sheba heard of the fame of Solomon, she came to Jerusalem to test him with hard questions, with a very great retinue and camels bearing spices and very much gold and precious stones. And when she came to Solomon, she told him all that was on her mind.",
      "M": "When the queen of Sheba heard of Solomon's fame, she came to Jerusalem to test him with difficult questions, bringing a large company of attendants and camels loaded with spices, abundant gold, and precious stones. She arrived and spoke to Solomon about everything on her mind.",
      "T": "Fame travels. The queen of Sheba — likely from modern Yemen, the ancient kingdom of Saba — heard of Solomon and came to investigate. Not a diplomatic mission, not a trade delegation, but a personal intellectual test: she came with hard questions. The 'hard questions' (riddles, problems, philosophical challenges) were a form of royal intellectual exchange in the ancient Near East. She brought gifts proportional to her expectations. And when she arrived, she held nothing back — she told him everything in her heart. This is what wisdom does: it invites disclosure."
    },
    "2": {
      "L": "And Solomon answered all her questions; there was nothing hidden from Solomon that he could not explain to her.",
      "M": "Solomon answered all her questions; nothing was too difficult for him to explain.",
      "T": "Nothing was hidden from him — every question she brought had an answer in Solomon. She had come prepared to stump a king; she found a man who could walk her through every question she had carried from the edge of the known world. The wisdom that God had given at Gibeon was not theoretical; it was inexhaustible in practice."
    },
    "3": {
      "L": "And when the queen of Sheba had seen the wisdom of Solomon and the house that he had built,",
      "M": "When the queen of Sheba observed Solomon's wisdom and the palace he had built,",
      "T": "She saw two things: the wisdom in his words and the wisdom in his buildings. The temple and palace were not merely architectural achievements; they were expressions of the mind that built them. To see Solomon's house was to see an argument made in stone and cedar and gold. The queen had come to test his words; she ended by seeing his whole world."
    },
    "4": {
      "L": "the food of his table, the seating of his officials, and the attendance of his servants, and their clothing, his cupbearers, and their clothing, and his burnt offerings that he offered at the house of the LORD — there was no more spirit in her.",
      "M": "the food at his table, the seating of his officials, the service of his attendants and their uniforms, his cupbearers and their uniforms, and the burnt offerings he presented at the LORD's house — she was breathless.",
      "T": "The list of what she witnessed is careful: table, seating order, servants, uniforms, cupbearers, offerings at the temple. The progression moves from the mundane (food) to the sacred (worship). Everything in Solomon's court was ordered — the meals, the hierarchy, the dress, the worship. Order was wisdom made visible. The queen of Sheba ran out of breath. The Hebrew says her spirit left her — she was overwhelmed, undone by the totality of what she encountered. She had come to test a king; she found a world."
    },
    "5": {
      "L": "And she said to the king, 'The report was true that I heard in my own land of your words and of your wisdom,",
      "M": "She told the king: 'The report I heard in my own country about your words and your wisdom was true.",
      "T": "She begins with a confession: the report was true. She had doubted, or at least wondered. Now she knows. Every word she had heard about Solomon in Sheba was accurate. This is a queen accustomed to hearing exaggerated praise; she knows the difference between reputation and reality. Solomon was the reality."
    },
    "6": {
      "L": "'but I did not believe the reports until I came and my own eyes had seen it. And behold, the half of the greatness of your wisdom was not told me; you surpass the report that I heard.",
      "M": "'but I did not believe the reports until I came and saw for myself. And not even half of your great wisdom was told to me — you far exceed the reputation I heard.'",
      "T": "The famous admission: what she heard was not exaggeration — it was understatement. The half was not told to her. No report could have prepared her. Solomon exceeded his own reputation. This is the Chronicler's point: God's gift of wisdom to Solomon was so comprehensive that human description couldn't contain it. The queen of Sheba is the most credible possible witness — she came to test him, she doubted the reports, and she is the one who says: it's not enough. You are more."
    },
    "7": {
      "L": "'Happy are your men and happy are these your servants who stand continually before you and hear your wisdom.",
      "M": "'How fortunate are your men, and how blessed are these servants of yours who stand before you continually and hear your wisdom!'",
      "T": "Blessed — the word she uses is the same word used in the Psalms and Proverbs for the person who walks in God's ways (Ps 1:1; Prov 3:13). The queen of Sheba speaks a beatitude over the servants of Solomon's court. To stand in the presence of wisdom and hear it daily — this is a kind of blessedness. Jesus would later draw the parallel explicitly: a greater than Solomon is here (Matt 12:42). The beatitude the queen pronounces over Solomon's servants is the beatitude that belongs to those who sit at the feet of Christ."
    },
    "8": {
      "L": "'Blessed be the LORD your God, who has delighted in you and set you on his throne as king for the LORD your God! Because your God loved Israel and would establish them forever, he has made you king over them to execute justice and righteousness.'",
      "M": "'Blessed be the LORD your God, who has delighted in you and placed you on his throne as king for the LORD your God! Because he loved Israel and intended to sustain them forever, he made you their king to administer justice and righteousness.'",
      "T": "The queen blesses the God of Israel. A Sheban queen, standing in the court of a Hebrew king, speaking a doxology to the LORD. She perceives what Solomon himself had confessed at Gibeon: this throne was given, not taken. God delighted in Solomon; God set him on this throne. And then she names the reason — not Solomon's virtue, not Israel's merit, but God's love for Israel. 'Because your God loved Israel to establish them forever' — the queen of Sheba is a theologian. She understands that Solomon's wisdom is not a private possession but a gift given for the sake of a people God loves. The king exists for the people; the people exist because God loves them."
    },
    "9": {
      "L": "Then she gave the king a hundred and twenty talents of gold, and spices in very great quantity, and precious stones. There was no such spice as that which the queen of Sheba gave to King Solomon.",
      "M": "She gave the king a hundred and twenty talents of gold, enormous quantities of spices, and precious stones. There had never been spices like those the queen of Sheba gave to King Solomon.",
      "T": "A hundred and twenty talents — roughly 4.5 tons of gold — plus unprecedented spices. The queen brought everything she had said and then backed it with everything she had. Her confession was matched by her gift. The spices were unique — no equivalent had ever come to Israel's king. The encounter with wisdom was costly and generous: she gave what could not be replaced."
    },
    "10": {
      "L": "Moreover, the servants of Huram and the servants of Solomon, who brought gold from Ophir, brought algum wood and precious stones.",
      "M": "The servants of Huram and Solomon who brought gold from Ophir also brought algum wood and precious stones.",
      "T": "The Ophir expedition (ch 8) contributed more than gold: algum wood, a precious timber from the south, along with gems. The trade routes that linked Israel to the southern world brought multiple currencies of value — precious metal, rare timber, stones."
    },
    "11": {
      "L": "And the king made from the algum wood steps for the house of the LORD and for the king's house, lyres also and harps for the singers. There was nothing like them seen before in the land of Judah.",
      "M": "The king used the algum wood to make steps for the LORD's house and the royal palace, as well as harps and lyres for the musicians. Nothing like them had ever been seen in Judah.",
      "T": "Algum wood for steps and instruments — the rare timber served both the architectural and the musical life of the temple. The steps (perhaps the terraced approach to the temple entrance, or a feature of the porch) and the harps and lyres made from the wood: both connected the exotic southern timber to the worship of God. The queen's gift and the trade expedition together furnished the music that filled the house of the LORD."
    },
    "12": {
      "L": "And King Solomon gave to the queen of Sheba all that she desired, whatever she asked, besides what she had brought to the king. So she turned and went back to her own land with her servants.",
      "M": "King Solomon gave the queen of Sheba everything she wanted and asked for, over and above what she had brought to him. Then she and her servants departed and returned to her own land.",
      "T": "Generosity answered generosity. She had come with extraordinary gifts; she left with everything she desired plus what she had not thought to ask. Solomon gave to the capacity of her desire, not to the limit of her request. This is a pattern of the Chronicler's Solomon: lavishness that exceeds expectation, abundance that embarrasses need. And then she left — back to Sheba, carrying a memory of Jerusalem that would reshape her understanding of the world."
    },
    "13": {
      "L": "Now the weight of gold that came to Solomon in one year was six hundred and sixty-six talents of gold,",
      "M": "The annual weight of gold that came to Solomon was six hundred and sixty-six talents,",
      "T": "Six hundred and sixty-six talents per year — roughly 25 tons of gold annually. This astronomical figure represents the convergence of all Solomon's trade networks: Ophir expeditions, tribute from vassal kings, profits from the caravan trade. The Chronicler presents this as the fulfillment of what God promised at Gibeon: riches and wealth beyond any king before or after."
    },
    "14": {
      "L": "besides what the explorers and merchants brought. And all the kings of Arabia and the governors of the land brought gold and silver to Solomon.",
      "M": "not counting what merchants and traders brought. The kings of Arabia and the regional governors also brought gold and silver to Solomon.",
      "T": "The 666 talents were the baseline, not the ceiling. On top of the Ophir expeditions came tribute from Arabia's kings, payments from regional governors, commercial profits from the merchant caravans that crossed Israel's territory. Solomon stood at the center of the ancient Near East's economic network, and the wealth of nations flowed toward him."
    },
    "15": {
      "L": "King Solomon made two hundred large shields of beaten gold; six hundred shekels of beaten gold went into each shield.",
      "M": "King Solomon made two hundred large shields of hammered gold, each requiring six hundred shekels of gold.",
      "T": "Display shields — ceremonial rather than military, hung in the House of the Forest of Lebanon as symbols of royal power and wealth. Six hundred shekels per shield: roughly 15 pounds of gold each. Two hundred of them. The visual impact would have been overwhelming — a gallery of gleaming gold, each shield a statement of what Solomon's kingdom had achieved."
    },
    "16": {
      "L": "And he made three hundred shields of beaten gold; three hundred shekels of gold went into each shield. And the king put them in the House of the Forest of Lebanon.",
      "M": "He also made three hundred smaller shields of hammered gold, each with three hundred shekels of gold. The king placed them all in the House of the Forest of Lebanon.",
      "T": "Five hundred shields total in the armory-palace — the royal arsenal as an art installation of wealth. The House of the Forest of Lebanon, named for its cedar columns (1 Kgs 7:2-5), displayed the tribute of nations in gold. Every visiting dignitary would pass through and understand what kind of king they were dealing with."
    },
    "17": {
      "L": "The king also made a great ivory throne and overlaid it with pure gold.",
      "M": "The king made a great throne of ivory and overlaid it with pure gold.",
      "T": "The throne — the seat of judgment and royal authority — was ivory and gold, the two most precious materials of the ancient world combined. To sit on this throne was to occupy the visible symbol of wisdom and wealth united. Every judgment Solomon rendered was rendered from a seat that said: this kingdom is wealthy enough and wise enough to be just."
    },
    "18": {
      "L": "The throne had six steps and a footstool of gold fastened to the throne, and on each side of the seat were armrests and two lions standing beside the armrests,",
      "M": "The throne had six steps, a gold footstool attached to it, armrests on each side of the seat, and two lions standing beside the armrests.",
      "T": "Six steps up to the throne — each step a statement of ascent, each step guarded by lions. The footstool of gold echoed the language of the temple: God's footstool is the earth (Isa 66:1), and the ark was sometimes called God's footstool. Solomon's throne, with its footstool, placed the king in a carefully calibrated relationship to the divine: below God, above the nation, accessible by six steps, guarded by lions."
    },
    "19": {
      "L": "while twelve lions stood there, one on each side of the six steps. Nothing like it was ever made in any kingdom.",
      "M": "Twelve lions stood on the six steps, one at each side of each step. Nothing like it existed in any other kingdom.",
      "T": "Twelve lions — one for each tribe of Israel, flanking every step of the ascent to the throne. To approach the king was to pass through a gallery of lions, the symbol of royalty, strength, and the tribe of Judah. The throne was unique: no king in the known world had anything like it. Solomon's magnificence was not borrowed from another tradition; it set the standard."
    },
    "20": {
      "L": "All King Solomon's drinking vessels were of gold, and all the vessels of the House of the Forest of Lebanon were of pure gold. Silver was not considered as anything in the days of Solomon.",
      "M": "All of King Solomon's drinking vessels were gold, and all the utensils of the House of the Forest of Lebanon were pure gold. Silver was considered worthless in Solomon's day.",
      "T": "Silver had become so ordinary that it was not counted. This is the Chronicler's hyperbole of abundance: when silver is common as gravel and gold is the currency of cups and spoons, the kingdom has reached a level of wealth that redefines categories. The God who promised riches beyond measure (1:12) delivered them literally. Silver was not worthless in any absolute sense — it was worthless relative to the abundance of gold."
    },
    "21": {
      "L": "For the king's ships went to Tarshish with the servants of Huram. Once every three years the ships of Tarshish used to come bringing gold, silver, ivory, apes, and peacocks.",
      "M": "The king's fleet sailed to Tarshish with Huram's crew. Every three years the Tarshish ships returned with gold, silver, ivory, apes, and peacocks.",
      "T": "Tarshish ships — the largest oceangoing vessels of the ancient world, capable of three-year voyages. Every three years the exotic cargo arrived: gold and silver from distant mines, ivory from Africa or India, apes and peacocks — living animals that would have been marvels in Jerusalem. The court of Solomon was a collection point for the wonders of the known world. The king's wealth was not merely monetary; it was a museum of the earth's abundance."
    },
    "22": {
      "L": "Thus King Solomon excelled all the kings of the earth in riches and in wisdom.",
      "M": "King Solomon surpassed all the kings of the earth in riches and wisdom.",
      "T": "The Chronicler's summary verdict: in wealth and wisdom, no one compared. This is not patriotic boasting; the queen of Sheba already confirmed it (v. 6). Solomon's excellence was double: riches sufficient to make silver worthless, wisdom sufficient to silence every hard question the world could bring. The two were inseparable — the wisdom that God gave produced the wealth, and the wealth was administered by the wisdom. Together they defined an age."
    },
    "23": {
      "L": "And all the kings of the earth sought the presence of Solomon to hear his wisdom, which God had put into his mind.",
      "M": "All the kings of the earth sought audiences with Solomon to hear the wisdom God had placed in his heart.",
      "T": "They came to him. Not diplomats making routine visits, not allies on political business — kings came to hear. The wisdom that God had put in Solomon's mind (the Hebrew says 'in his heart' — the seat of thought and will) drew the most powerful people in the world to Jerusalem. Solomon did not have to go to the nations; the nations came to him. The city of the divine name became the center of the world's intellectual gravity."
    },
    "24": {
      "L": "Every one of them brought his present, articles of silver and gold, garments, myrrh, spices, horses, and mules, so much year by year.",
      "M": "Each one brought gifts year by year: silver and gold objects, clothing, myrrh, spices, horses, and mules.",
      "T": "Tribute as appointment fee — to come to Solomon you brought gifts, and the gifts of the world's kings year after year composed a river of wealth flowing toward Jerusalem. Silver, gold, clothing, aromatics, animals. The trade catalog reads like a map of the ancient world: metallurgy from one direction, myrrh from the Arabian peninsula, horses from Anatolia or Egypt, mules from the mountain pastures. The world paid to hear wisdom."
    },
    "25": {
      "L": "And Solomon had four thousand stalls for horses and chariots, and twelve thousand horsemen, whom he stationed in the chariot cities and with the king in Jerusalem.",
      "M": "Solomon had four thousand stalls for horses and chariots, and twelve thousand horsemen stationed in the chariot cities and with the king in Jerusalem.",
      "T": "Four thousand stalls, twelve thousand horsemen — the military infrastructure of an empire. The chariot cities distributed throughout the kingdom formed a strategic network of rapid-response forces. The Chronicler reports this as capacity, not critique; but the reader who knows Deuteronomy 17:16 hears the quiet alarm: Israel's king was not supposed to multiply horses. Solomon's glory was also the first stage of his undoing."
    },
    "26": {
      "L": "And he ruled over all the kings from the Euphrates to the land of the Philistines and to the border of Egypt.",
      "M": "He ruled over all the kings from the Euphrates River to the land of the Philistines and down to the border of Egypt.",
      "T": "The Euphrates to Egypt — the full extent of the Abrahamic promise (Gen 15:18) realized in Solomon's reign. The land promised to Abraham's descendants reached its maximum geographical expression under the wisest king Israel ever had. This was the kingdom at its fullness: every border touched, every promise mapped."
    },
    "27": {
      "L": "And the king made silver as common in Jerusalem as stone, and cedar as plentiful as the sycamore of the Shephelah.",
      "M": "The king made silver as common in Jerusalem as stone, and cedar as plentiful as the sycamore trees of the foothills.",
      "T": "The same summary as chapter 1:15, bookending the account of Solomon's reign with identical images of abundance: silver as ordinary as roadside gravel, cedar as ubiquitous as the native sycamore-figs. The Chronicler frames Solomon's entire reign between these two snapshots of prosperity. The kingdom began in abundance; it ended in abundance. Whatever complications lay beneath, the age of Solomon was an age of unimagined wealth."
    },
    "28": {
      "L": "And horses were imported for Solomon from Egypt and from all lands.",
      "M": "Horses were brought to Solomon from Egypt and from all other lands.",
      "T": "From Egypt — again. The shadow of Deuteronomy 17:16 falls again over Solomon's glory. The horses came from the land of slavery, multiplied by the king who built the temple. The Chronicler does not moralize; he records. But the Deuteronomic reader knows the trajectory."
    },
    "29": {
      "L": "Now the rest of the acts of Solomon, from first to last, are they not written in the history of Nathan the prophet, and in the prophecy of Ahijah the Shilonite, and in the visions of Iddo the seer concerning Jeroboam the son of Nebat?",
      "M": "The rest of Solomon's acts, from beginning to end, are recorded in the account of Nathan the prophet, in the prophecy of Ahijah the Shilonite, and in the visions of Iddo the seer regarding Jeroboam son of Nebat.",
      "T": "Three sources, three prophetic voices. Nathan, who had confronted David and announced the Davidic covenant; Ahijah, who had prophesied the division of the kingdom; Iddo, the seer who tracked what happened to Jeroboam. The Chronicler cites prophetic sources — not merely administrative records but the writings of men who interpreted events through the lens of divine purpose. History, for the Chronicler, is prophetic history."
    },
    "30": {
      "L": "Solomon reigned in Jerusalem over all Israel forty years.",
      "M": "Solomon reigned over all Israel in Jerusalem for forty years.",
      "T": "Forty years — the number of a generation, the length of the wilderness wandering, the reign of David. Solomon's reign matched his father's in duration. What David built in military and political terms, Solomon built in temple and commercial terms — two forty-year reigns that defined Israel's golden age."
    },
    "31": {
      "L": "And Solomon slept with his fathers and was buried in the city of David his father, and Rehoboam his son reigned in his place.",
      "M": "Solomon rested with his ancestors and was buried in the city of David his father, and his son Rehoboam became king in his place.",
      "T": "He slept with his fathers — the idiom is ancient, dignified, and accurate: death as sleep in the family, the long rest among those who went before. Jerusalem, the city of David, received him in burial as it had received him in kingship. Rehoboam stepped into the throne. The forty years of glory were over. What came next would test whether anything of Solomon's legacy could survive the next generation."
    }
  },
  "10": {
    "1": {
      "L": "Rehoboam went to Shechem, for all Israel had come to Shechem to make him king.",
      "M": "Rehoboam went to Shechem, where all Israel had gathered to crown him king.",
      "T": "Shechem — not Jerusalem. The coronation of Solomon's son did not happen in the capital but in the ancient northern city where Abraham had built his first altar in Canaan (Gen 12:6), where Joshua had renewed the covenant at the end of the conquest (Josh 24), and where tribal Israel gathered. The choice of Shechem was a political statement by the northern tribes: come to us; we will see if you are fit to rule us. The crown was not automatic."
    },
    "2": {
      "L": "And as soon as Jeroboam the son of Nebat heard of it — for he was in Egypt, where he had fled from King Solomon — Jeroboam returned from Egypt.",
      "M": "When Jeroboam son of Nebat heard this — he was in Egypt, where he had fled from King Solomon — he returned from Egypt.",
      "T": "Jeroboam had been in exile in Egypt since Ahijah the prophet had told him he would rule ten tribes and Solomon had sought his life (1 Kgs 11:26-40). Solomon is dead; the threat is gone; Jeroboam returns. His return is triggered by news of the succession — the political moment he had been waiting for has arrived. The parallel between Jeroboam's exile in Egypt and Israel's bondage in Egypt is implicit: the man who will lead the northern revolt spent his waiting time in the land of slavery."
    },
    "3": {
      "L": "And they sent and called him. And Jeroboam and all Israel came and spoke to Rehoboam, saying,",
      "M": "Israel sent for him, and Jeroboam and all Israel came and spoke to Rehoboam:",
      "T": "The summons to Jeroboam is Israel's opening move. They did not merely gather to crown Rehoboam; they brought their spokesman and their grievance. The coronation at Shechem was conditional — the northern tribes were negotiating, not simply celebrating. Jeroboam served as the representative of a workforce that had been burdened for forty years."
    },
    "4": {
      "L": "'Your father made our yoke heavy. Now therefore lighten the hard service of your father and his heavy yoke on us, and we will serve you.'",
      "M": "'Your father made our yoke heavy. Now lighten the burden and the heavy yoke he imposed on us, and we will serve you.'",
      "T": "Yoke — the word that echoes all the way back to Egypt. Solomon's labor conscription, his taxation, his military levies had worn the northern tribes down. They do not ask for revolution; they ask for relief. Lighten the yoke, and we will serve you. The offer is reasonable, the condition is clear. All Rehoboam had to do was say yes. What happens next is one of the great examples in Scripture of how folly masquerading as strength destroys what wisdom could preserve."
    },
    "5": {
      "L": "He said to them, 'Come to me again in three days.' So the people went away.",
      "M": "He told them, 'Come back to me in three days.' So the people left.",
      "T": "Three days — the delay is wise, not the answer. Rehoboam did not refuse; he paused to seek counsel. The three-day interval was an opportunity for wisdom. It became an opportunity for foolishness."
    },
    "6": {
      "L": "Then King Rehoboam took counsel with the old men who had stood before Solomon his father while he was still alive, saying, 'How do you advise me to answer this people?'",
      "M": "King Rehoboam consulted the elders who had served his father Solomon during his lifetime: 'How do you advise me to respond to these people?'",
      "T": "The old men — the advisors who had spent decades in Solomon's court, who had watched the kingdom function, who had seen what the labor burden cost the people and what it produced. Their counsel would be shaped by long experience and a grasp of political reality that youth cannot manufacture. Rehoboam asked the right people first."
    },
    "7": {
      "L": "And they said to him, 'If you will be good to this people and please them and speak good words to them, then they will be your servants forever.'",
      "M": "They advised: 'If you will be generous to this people, please them, and speak kindly to them, they will be your loyal servants always.'",
      "T": "The wisdom of the old men is breathtakingly simple: be kind, and you will have them forever. Good words — the Hebrew is tov, good, the same word used for God's creation. Speak goodness to this people. Please them. The elders were not recommending weakness; they were recommending the only strategy that builds lasting loyalty. You cannot force people to serve forever; you can earn it. Rehoboam held in his hand the choice between a kingdom of free servants and a kingdom of resentful ones."
    },
    "8": {
      "L": "But he abandoned the counsel that the old men gave him and took counsel with the young men who had grown up with him and stood before him.",
      "M": "But he rejected the elders' advice and consulted instead the young men who had grown up with him and now served him.",
      "T": "He abandoned the old men's counsel. The verb is azab — forsake, leave behind — the same word used for Israel abandoning the LORD. The Chronicler's choice of word is pointed: the same spiritual failure that destroys covenant relationships also destroys political wisdom. Rehoboam forsook the counsel of experience and turned to the men who had grown up with him — his peers, his friends, the men who had never seen the consequences of bad leadership firsthand."
    },
    "9": {
      "L": "And he said to them, 'What do you advise that we answer this people who have said to me, \"Lighten the yoke that your father put on us\"?'",
      "M": "'What do you advise we tell these people who asked me to lighten the yoke my father put on them?'",
      "T": "He phrased the question correctly — the people want the yoke lightened. But the men he asked were not equipped to answer wisely. They had grown up inside the palace, accustomed to the benefits of Solomon's kingdom, without knowledge of the cost the kingdom imposed on those who bore it."
    },
    "10": {
      "L": "And the young men who had grown up with him said to him, 'Thus shall you speak to the people who said to you, \"Your father made our yoke heavy, but you lighten it for us.\" Thus shall you say to them: \"My little finger is thicker than my father's thighs.\"'",
      "M": "The young men who had grown up with him replied: 'Tell the people who said your father's yoke was heavy and asked you to lighten it: \"My little finger is thicker than my father's waist.\"'",
      "T": "The young men's advice was theater of intimidation: anatomize the comparison in the crudest possible terms. My smallest finger is bigger than my father's entire body. The bravado was designed to project overwhelming strength. What it actually projected was a complete failure of political intelligence. The people did not need to be threatened; they needed to be heard. The young men's counsel would take the coronation at Shechem and turn it into a civil war."
    },
    "11": {
      "L": "'And now, whereas my father laid on you a heavy yoke, I will add to your yoke. My father disciplined you with whips, but I will discipline you with scorpions.'",
      "M": "'Where my father burdened you with a heavy yoke, I will make it even heavier. My father punished you with whips; I will use scorpions.'",
      "T": "Whips to scorpions — the escalation of metaphorical violence. Scorpions was likely a reference to a barbed lash, a whip with metal tips that cut deeper than ordinary leather. The young men's speech offered the people not relief but explicit threat of worse suffering. This was not strength; it was the language of a man who cannot lead. The first test of Rehoboam's kingship, and the choice was scorpions over kindness."
    },
    "12": {
      "L": "So Jeroboam and all the people came to Rehoboam on the third day, as the king had directed, saying, 'Come to me again on the third day.'",
      "M": "Jeroboam and all the people came back to Rehoboam on the third day, as the king had instructed: 'Return to me on the third day.'",
      "T": "The three days had elapsed. Jeroboam and all Israel returned, ready to hear whether Rehoboam would choose wisdom or folly. They had made their request clearly and reasonably. They were about to receive an answer that would shatter the united kingdom."
    },
    "13": {
      "L": "And the king answered them harshly; and King Rehoboam abandoned the counsel of the old men,",
      "M": "King Rehoboam answered them harshly. He rejected the elders' advice",
      "T": "Harshly — the Hebrew is qashah, hard, severe, the same root used for hardening the heart in the Exodus narratives. Rehoboam hardened himself against the people as Pharaoh had hardened himself against Israel. The irony is exact: the son of the temple builder answered the people of God with the same intransigence that had enslaved Israel in Egypt."
    },
    "14": {
      "L": "and spoke to them according to the counsel of the young men, saying, 'My father made your yoke heavy, but I will add to it. My father disciplined you with whips, but I will discipline you with scorpions.'",
      "M": "and followed the young men's advice instead, telling them: 'My father made your yoke heavy; I will make it heavier. My father punished you with whips; I will use scorpions.'",
      "T": "Word for word what the young men suggested — no softening, no prudent modification, no last-minute recognition that this was a catastrophic error. Rehoboam delivered the threat in full. The kingdom he had inherited in its greatest hour was about to divide, and the division was entirely avoidable. One word of kindness — and he had forty years of his father's wealth to afford kindness — would have kept Israel united. He chose scorpions."
    },
    "15": {
      "L": "So the king did not listen to the people, for it was a turn of affairs brought about by God that the LORD might fulfill his word, which he spoke by Ahijah the Shilonite to Jeroboam the son of Nebat.",
      "M": "The king would not listen to the people, for this turn of events was from God, so that the LORD could fulfill the word he had spoken through Ahijah the Shilonite to Jeroboam son of Nebat.",
      "T": "The Chronicler inserts the theological key: the turn of affairs was from God. This does not excuse Rehoboam's folly — his pride and stupidity were his own. But God's sovereignty operates through human freedom, not against it. Ahijah had prophesied the kingdom's division (1 Kgs 11:29-39) as judgment on Solomon's unfaithfulness. Rehoboam's folly was the instrument God used to fulfill that judgment. History is not random; even political catastrophes have a shape within God's purposes."
    },
    "16": {
      "L": "And when all Israel saw that the king did not listen to them, the people answered the king, 'What portion do we have in David? We have no inheritance in the son of Jesse. Each of you to your tents, O Israel! Look now to your own house, David.' So all Israel went to their tents.",
      "M": "When all Israel saw that the king would not listen to them, they answered the king: 'What share do we have in David? We have no inheritance in the son of Jesse. Every Israelite, to your tents! See to your own house, David!' So all Israel went home.",
      "T": "The ancient separatist cry — the same words Sheba son of Bichri had used to lead a revolt in David's day (2 Sam 20:1). 'What portion do we have in David?' is a tribal declaration of independence: we have no stake in the southern dynasty; the son of Jesse is not our king. The repudiation was not spontaneous anger but the articulation of a long-standing northern grievance that Rehoboam's folly had finally allowed to break open. The united kingdom that David had fought to create and Solomon had maintained through wealth and wisdom dissolved in a day."
    },
    "17": {
      "L": "But Rehoboam reigned over the people of Israel who lived in the cities of Judah.",
      "M": "Rehoboam continued to reign over the Israelites living in the towns of Judah.",
      "T": "One tribe out of twelve — the southern rump of what had been an empire. Jerusalem, Judah, Benjamin: this was what remained. The kingdom of Solomon's forty years of glory was reduced to Rehoboam's portion in a single afternoon of foolishness."
    },
    "18": {
      "L": "Then King Rehoboam sent Hadoram, who was taskmaster over the forced labor, and the people of Israel stoned him to death. And King Rehoboam quickly mounted his chariot to flee to Jerusalem.",
      "M": "When King Rehoboam sent Hadoram, who was in charge of the forced labor, the Israelites stoned him to death. Rehoboam quickly mounted his chariot and fled to Jerusalem.",
      "T": "The first act of the divided kingdom was murder. Hadoram — the man whose position embodied everything the northern tribes resented, the overseer of the very labor burden they had begged to have lifted — was stoned to death. Rehoboam had sent exactly the wrong man at exactly the wrong moment. The king himself barely escaped with his life, fleeing in his chariot. The scorpion speech had cost him more than a kingdom; it had nearly cost him his life."
    },
    "19": {
      "L": "So Israel has been in rebellion against the house of David to this day.",
      "M": "Israel has been in rebellion against the house of David to this day.",
      "T": "The Chronicler closes the chapter with a statement that spans the centuries between Rehoboam and the Chronicler's own time: the division stands. The rebellion that began at Shechem has never been healed — not under Rehoboam, not under any subsequent king of Judah, not even after the exile. The wound of the divided kingdom is still open when the Chronicler writes. The folly of one afternoon lasted a millennium."
    }
  },
  "11": {
    "1": {
      "L": "When Rehoboam came to Jerusalem, he assembled the house of Judah and Benjamin, a hundred and eighty thousand chosen warriors, to fight against Israel to restore the kingdom to Rehoboam.",
      "M": "Back in Jerusalem, Rehoboam mobilized the house of Judah and Benjamin — a hundred and eighty thousand select warriors — to battle Israel and reclaim the kingdom.",
      "T": "Rehoboam's first instinct was military: assemble an army, reclaim the north by force. A hundred and eighty thousand chosen warriors — a serious military force, enough to make the campaign plausible. The Chronicler reports this without surprise; a king who used the language of scorpions would naturally reach for weapons when negotiations collapsed. But God had other plans."
    },
    "2": {
      "L": "But the word of the LORD came to Shemaiah the man of God, saying,",
      "M": "Then the word of the LORD came to Shemaiah the man of God:",
      "T": "The word of the LORD interrupted the mobilization. Shemaiah — 'Yahweh has heard' — is introduced without prior context; he simply appears as the bearer of a divine message at the moment the nation needs to hear it. The man of God steps into the gap between Rehoboam's army and his intended battlefield."
    },
    "3": {
      "L": "'Say to Rehoboam the son of Solomon, king of Judah, and to all Israel in Judah and Benjamin,'",
      "M": "'Say to Rehoboam son of Solomon, king of Judah, and to all Israel in Judah and Benjamin:'",
      "T": "The message is addressed to Rehoboam by name and title — the king of Judah, not all Israel. The title itself is the message: the address defines his reduced kingdom. And it is addressed to 'all Israel in Judah and Benjamin' — the Chronicler does not write off the northern tribes as apostate; they are still Israel, but the Israel that is now separate."
    },
    "4": {
      "L": "'Thus says the LORD: You shall not go up or fight against your brothers. Return every man to his home, for this thing is from me.' So they listened to the word of the LORD and returned and did not go against Jeroboam.",
      "M": "'This is what the LORD says: You are not to march out or fight against your fellow Israelites. Go home, every one of you, because this has come about through me.' They obeyed the LORD's message and turned back from going against Jeroboam.",
      "T": "Do not fight your brothers. The word 'brothers' cuts through the military logic: the northern tribes are not enemies to be conquered; they are family. And the reason for the prohibition is the same that the Chronicler named in chapter 10: this thing is from me. The division was divine judgment, not a political mishap to be reversed by force. To fight against it would be to fight against God's own purpose. They obeyed — which is more than Rehoboam's next king Amaziah would do in a similar situation. Obedience here is remarkable given the army assembled and the grievance nursed."
    },
    "5": {
      "L": "Rehoboam lived in Jerusalem, and he built cities for defense in Judah.",
      "M": "Rehoboam lived in Jerusalem and built up Judah's defenses.",
      "T": "Unable to fight northward, Rehoboam turned his energy inward — toward the territory he actually held. Fortification was the next best option: make Judah secure even if it cannot be reunited. The builder's instinct (inherited from his father) was redirected from expansion to consolidation."
    },
    "6": {
      "L": "He built Bethlehem, Etam, Tekoa,",
      "M": "He built Bethlehem, Etam, and Tekoa,",
      "T": "Bethlehem — David's birthplace, now a fortified city in his descendant's defensive network. Etam, mentioned in Judges as a place of refuge (Judg 15:8). Tekoa, home of the wise woman and later the prophet Amos. Each city added to the fortification ring around Jerusalem."
    },
    "7": {
      "L": "Beth-zur, Soco, Adullam,",
      "M": "Beth-zur, Soco, and Adullam,",
      "T": "Beth-zur commanding the southern approaches to Jerusalem. Soco in the Shephelah foothills. Adullam — the cave where David had hidden from Saul (1 Sam 22:1), now a fortified city protecting the same territory David had once sheltered in."
    },
    "8": {
      "L": "Gath, Mareshah, Ziph,",
      "M": "Gath, Mareshah, and Ziph,",
      "T": "Gath — the Philistine city David had once fled to (1 Sam 27:2), now within Judah's defensive perimeter. Mareshah and Ziph in the Judean highlands. The defensive line extended west toward the coastal plain and south into the hill country."
    },
    "9": {
      "L": "Adoraim, Lachish, Azekah,",
      "M": "Adoraim, Lachish, and Azekah,",
      "T": "Lachish — Judah's second city, the great fortress that would be the last to fall before Jerusalem when Sennacherib invaded (2 Kgs 18:14) and when Nebuchadnezzar came (Jer 34:7). Azekah guarded the Elah Valley, where David had faced Goliath (1 Sam 17:1-2). Rehoboam was building on Judah's most historically significant ground."
    },
    "10": {
      "L": "Zorah, Aijalon, and Hebron, fortified cities that are in Judah and in Benjamin.",
      "M": "Zorah, Aijalon, and Hebron — all fortified cities in Judah and Benjamin.",
      "T": "Zorah — the birthplace of Samson (Judg 13:2), now a fortress on Judah's northern edge. Aijalon — where Joshua commanded the sun to stand still (Josh 10:12), now a military strongpoint. Hebron — the city of Abraham's burial, of David's early kingship. The fifteen cities Rehoboam fortified were the geographical spine of Judah, a ring of defended places that could hold the kingdom if it could not expand."
    },
    "11": {
      "L": "He strengthened the fortresses and put commanders in them, and stores of food, oil, and wine.",
      "M": "He reinforced the strongholds, appointed commanders in them, and stockpiled food, olive oil, and wine.",
      "T": "Fortification without supply is architecture without strategy. Rehoboam stocked the cities: food for sieges, oil for lamps and wounds and fire, wine for morale and provision. The detail reveals a systematic defensive logic. He was building not just walls but a sustainable defensive infrastructure that could outlast a siege or absorb a rapid assault."
    },
    "12": {
      "L": "And in every city he put shields and spears, and made them very strong. So he held Judah and Benjamin.",
      "M": "He also put shields and spears in each city, making them very strong. Judah and Benjamin remained his.",
      "T": "Two tribes — this was Rehoboam's kingdom. Not the empire of Solomon or the confederacy of David, but Judah and Benjamin, the southern block. Shields and spears in every fortified city: the army was distributed, not centralized. Rehoboam could not reconquer the north, but he could hold the south. And in the providence of God, holding the south meant holding Jerusalem, the temple, and the line of David."
    },
    "13": {
      "L": "And the priests and the Levites who were in all Israel sided with him from all their territories.",
      "M": "From throughout Israel, the priests and Levites aligned themselves with Rehoboam.",
      "T": "The religious establishment migrated south. Priests and Levites from the northern territories — men whose whole life was ordered around legitimate worship of the LORD — abandoned their ancestral properties in the north and came to Judah. Jeroboam was about to give them no choice."
    },
    "14": {
      "L": "For the Levites left their pasturelands and their property and came to Judah and Jerusalem, because Jeroboam and his sons cast them out from serving as priests to the LORD,",
      "M": "The Levites left their pastures and landholdings and came to Judah and Jerusalem, because Jeroboam and his sons had expelled them from their priestly duties before the LORD.",
      "T": "Jeroboam expelled the Levites from their priestly office — the logical consequence of his establishing alternative worship sites and installing non-Levitical priests for the golden calves (v. 15). The Levites who would not participate in the new system were left with nothing in the north: no pastoral lands, no priestly income, no religious role. They came south because faithfulness to the LORD left them no other place to go."
    },
    "15": {
      "L": "And he appointed his own priests for the high places and for the goat demons and for the calves that he had made.",
      "M": "Jeroboam appointed his own priests for the high places, the goat idols, and the golden calves he had made.",
      "T": "Three categories of false worship: the high places (unauthorized local shrines), the goat demons (sa'irim — shaggy goat-like beings associated with wilderness spirits; cf. Lev 17:7), and the golden calves at Bethel and Dan (1 Kgs 12:28-29). Jeroboam's alternative religion was not simply a different form of Yahweh worship; it incorporated elements explicitly forbidden by the Torah. The priests he appointed were not from Levi — any willing person could take the role (1 Kgs 12:31). The system was illegitimate at every level."
    },
    "16": {
      "L": "And those who had set their hearts to seek the LORD God of Israel came after them from all the tribes of Israel to Jerusalem to sacrifice to the LORD, the God of their fathers.",
      "M": "Those from every tribe of Israel who had determined to seek the LORD God of Israel followed the Levites to Jerusalem to offer sacrifices to the LORD, the God of their ancestors.",
      "T": "The great self-selection: from all the northern tribes, the devout and the faithful packed up and moved south. They did not come because Rehoboam was a better king — he had just been foolish enough to split the kingdom. They came because the LORD was worshiped in Jerusalem with the Levitical priests, the bronze altar, and the legitimate sacrificial system. Where the worship was true, the faithful gathered. The theological gravity of the temple drew them across tribal and political boundaries."
    },
    "17": {
      "L": "They strengthened the kingdom of Judah, and for three years they made Rehoboam the son of Solomon secure, for they walked for three years in the way of David and Solomon.",
      "M": "They strengthened the kingdom of Judah and supported Rehoboam son of Solomon for three years, because for three years they followed the path of David and Solomon.",
      "T": "Three years of faithfulness produced three years of strength. The Chronicler's equation is precise: walking in the way of David and Solomon — the covenant standard — resulted in a stable, secure kingdom. Rehoboam had been given a foundation of devout refugees who chose Jerusalem for theological reasons. For three years, their presence and their faithfulness propped up a king who had disqualified himself at Shechem. Then, as verse 12:1 will show, the pattern broke."
    },
    "18": {
      "L": "Rehoboam took as wife Mahalath the daughter of Jerimoth the son of David, and of Abihail the daughter of Eliab the son of Jesse,",
      "M": "Rehoboam married Mahalath daughter of Jerimoth son of David, and Abihail daughter of Eliab son of Jesse.",
      "T": "Rehoboam's marriages linked him back to both his grandfather David (Jerimoth was a son of David, perhaps by a concubine not mentioned in the main genealogies) and David's brother Eliab (Jesse's son, passed over when Samuel anointed David, 1 Sam 16:6-7). The royal household was consciously maintaining its Davidic roots through the family connections of its wives."
    },
    "19": {
      "L": "and she bore him sons: Jeush, Shemariah, and Zaham.",
      "M": "She bore him Jeush, Shemariah, and Zaham.",
      "T": "Three sons from Mahalath — the Chronicler's genealogical record preserves names that would otherwise be lost. These are Rehoboam's sons by his first named wife, before the more politically significant marriage that follows."
    },
    "20": {
      "L": "After her he took Maacah the daughter of Absalom, who bore him Abijah, Attai, Ziza, and Shelomith.",
      "M": "After her he married Maacah daughter of Absalom, who bore him Abijah, Attai, Ziza, and Shelomith.",
      "T": "Maacah daughter of Absalom — David's rebellious son, killed in the oak tree by Joab (2 Sam 18:14-15), whose daughter (or granddaughter) became Rehoboam's favorite wife. The irony is not commented on: the son of Solomon married into the family of the man who had tried to overthrow David. And it was this wife's son, Abijah, who would succeed Rehoboam."
    },
    "21": {
      "L": "Rehoboam loved Maacah the daughter of Absalom above all his wives and concubines — he took eighteen wives and sixty concubines and fathered twenty-eight sons and sixty daughters.",
      "M": "Rehoboam loved Maacah daughter of Absalom more than all his other wives and concubines. He had eighteen wives and sixty concubines and fathered twenty-eight sons and sixty daughters.",
      "T": "Solomon's pattern reproduced on a smaller scale: many wives, beloved favorites, sons beyond the capacity of any father to know personally. Eighteen wives, sixty concubines — not empire-scale diplomacy like Solomon's seven hundred wives, but still the multiplication the Torah warned against (Deut 17:17). The beloved Maacah would have disproportionate influence — and her son Abijah would inherit the throne."
    },
    "22": {
      "L": "Rehoboam appointed Abijah the son of Maacah as chief prince among his brothers, for he intended to make him king.",
      "M": "Rehoboam appointed Abijah son of Maacah as chief among his brothers, intending to make him king.",
      "T": "The crown prince was not the eldest but the beloved wife's son. Rehoboam's heart was with Maacah, so Maacah's son would take the throne. The Chronicler reports this as a straightforward royal decision; later readers will see it as the beginning of the complication: a king chosen by his father's affection rather than birth order, a dynasty running on love rather than law."
    },
    "23": {
      "L": "And he dealt wisely and distributed some of his sons through all the districts of Judah and Benjamin, in all the fortified cities, and he gave them abundant provisions and procured wives for many of them.",
      "M": "He also acted shrewdly by distributing his other sons throughout the districts of Judah and Benjamin, placing them in the fortified cities with generous provisions and arranging many marriages for them.",
      "T": "A politically shrewd move: distribute the princes through the fortified cities, give them resources and families, create local loyalty networks throughout the kingdom. The sons became both governors and hostages of stability — men with too much to lose to rebel, too embedded in the kingdom to abandon it. Rehoboam could not reconquer the north, but he could weave his own dynasty into the fabric of the south. It was the wisest thing he did."
    }
  },
  "12": {
    "1": {
      "L": "When the rule of Rehoboam was established and he was strong, he abandoned the law of the LORD, and all Israel with him.",
      "M": "Once Rehoboam's rule was secure and he had grown strong, he abandoned the law of the LORD — and all Israel with him.",
      "T": "The Chronicler's pattern for royal failure is established here with its first clear example: when the kingdom was established and he felt strong, he forsook the LORD. Strength without accountability becomes autonomy; autonomy becomes apostasy. The three years of walking in the way of David and Solomon (11:17) had produced security, and security produced complacency. Rehoboam did not forsake the LORD because he was weak; he forsook the LORD because he felt strong enough not to need him."
    },
    "2": {
      "L": "In the fifth year of King Rehoboam, because they had been unfaithful to the LORD, Shishak king of Egypt came up against Jerusalem with twelve hundred chariots and sixty thousand horsemen.",
      "M": "In the fifth year of King Rehoboam, because they had been unfaithful to the LORD, Shishak king of Egypt attacked Jerusalem with twelve hundred chariots and sixty thousand cavalry.",
      "T": "Because they had been unfaithful — the Chronicler names the cause before the event. The invasion is not accidental. Shishak (Shoshenq I, who reigned c. 945–924 BC) was historically documented: the Bubastite Portal at Karnak lists over 150 Judean and Israelite cities he attacked. But the Chronicler's interest is not geopolitical; it is theological. Egypt returns — the land Israel fled, now chasing them again. The covenant curse of Deuteronomy 28:68 ('the LORD will bring you back to Egypt in ships') is beginning its long trajectory."
    },
    "3": {
      "L": "And the people were without number who came with him from Egypt — Libyans, Sukkiim, and Ethiopians.",
      "M": "He came with an innumerable force from Egypt: Libyans, Sukkiim, and Cushites.",
      "T": "Shishak's army was multinational: Libyans from the western desert (Shishak's own people — he was of Libyan descent), Sukkiim (an otherwise unknown people, possibly mercenary troops from the Libyan desert), and Cushites from the upper Nile. The Egyptian military machine drew soldiers from the entire northeastern corner of Africa. Against this force, Judah's fifteen fortified cities were insufficient."
    },
    "4": {
      "L": "And he took the fortified cities of Judah and came as far as Jerusalem.",
      "M": "He captured Judah's fortified cities and reached Jerusalem.",
      "T": "The fifteen fortified cities that Rehoboam had spent years building fell. One by one, the defensive network collapsed. Lachish fell. Beth-zur fell. The ring of protection that was supposed to hold Judah secure was stripped away. Shishak arrived at Jerusalem's gates. Everything Rehoboam had built to make himself strong had failed the moment it was tested by the God whose law he had forsaken."
    },
    "5": {
      "L": "Then Shemaiah the prophet came to Rehoboam and to the princes of Judah, who had gathered at Jerusalem because of Shishak, and said to them, 'Thus says the LORD: You abandoned me, so I have abandoned you to the hand of Shishak.'",
      "M": "Then the prophet Shemaiah came to Rehoboam and the Judean leaders assembled in Jerusalem because of Shishak and told them: 'This is what the LORD says: You abandoned me, so I have now abandoned you to Shishak.'",
      "T": "Shemaiah appears again — the same prophet who had stopped the war against the north (11:2-4). Now he delivers the covenant's mirror image: you abandoned me; I have abandoned you. The symmetry is exact. Rehoboam had forsaken the law of the LORD (v. 1); the LORD's response was to forsake Rehoboam's military protection. The covenant works both ways: faithfulness is rewarded, unfaithfulness is exposed. Shishak is not mentioned by name in Shemaiah's oracle — God does not need to explain his instruments, only his logic."
    },
    "6": {
      "L": "Then the princes of Israel and the king humbled themselves and said, 'The LORD is righteous.'",
      "M": "The Judean leaders and the king humbled themselves and said, 'The LORD is just.'",
      "T": "They humbled themselves — the niphal reflexive: not God humbling them but they humbling themselves before him. And their confession was theological rather than merely political: the LORD is righteous. Not 'we are sorry' or 'we will reform' — first the theological acknowledgment that God's judgment is just. Before asking for mercy, they admitted the justice of the sentence. This is the pattern of genuine repentance throughout Chronicles: acknowledge the righteousness of God's action before requesting its modification."
    },
    "7": {
      "L": "When the LORD saw that they humbled themselves, the word of the LORD came to Shemaiah: 'They have humbled themselves. I will not destroy them, but I will grant them some deliverance, and my wrath shall not be poured out on Jerusalem by the hand of Shishak.'",
      "M": "When the LORD saw that they humbled themselves, his word came to Shemaiah: 'They have humbled themselves, so I will not destroy them. I will grant them limited deliverance. My wrath will not be unleashed on Jerusalem through Shishak.'",
      "T": "God saw the humbling and responded immediately. Not just heard their words but saw the posture — the actual bending of pride before holiness. And the response was calibrated: not full deliverance, but some deliverance. Not complete destruction, but not complete restoration either. The word translated 'limited' or 'some' (me'at — a little, a small amount) is deliberate: Shishak will not be stopped entirely, but Jerusalem will not be destroyed. Partial judgment, partial mercy — the proportion matching the depth of the repentance."
    },
    "8": {
      "L": "'Nevertheless, they shall be servants to him, so that they may know my service and the service of the kingdoms of the countries.'",
      "M": "'They will become his subjects, however, so they will learn the difference between serving me and serving the kings of foreign nations.'",
      "T": "The theological payoff of the judgment: they will learn by comparison what they could have known by faith. Serving the LORD — his yoke, his requirements, his covenant loyalty — is one kind of service. Serving Shishak — tribute, humiliation, pillaged gold, foreign domination — is another. The comparison was meant to be educational. God's service, even with its covenant demands, is incomparably better than the service of any human master. The lesson was bought at the price of the temple treasury."
    },
    "9": {
      "L": "So Shishak king of Egypt came up against Jerusalem. He took away the treasures of the house of the LORD and the treasures of the king's house. He took everything. He also took away the shields of gold that Solomon had made.",
      "M": "Shishak king of Egypt attacked Jerusalem and carried off the treasures of the LORD's house and the palace. He took everything — including the gold shields Solomon had made.",
      "T": "Everything — the word is kol, comprehensive. The gold shields that the Chronicler described in such detail in chapter 9 — five hundred of them, hammered gold, the visible symbol of Solomon's incomparable wealth — were gone. Taken to Egypt. The gold that had flowed from Egypt through trade and tribute now flowed back in defeat. The circular justice was terrible: what Solomon's wisdom had gathered, Rehoboam's folly surrendered."
    },
    "10": {
      "L": "And King Rehoboam made in their place shields of bronze and committed them to the hands of the officers of the guard who kept the door of the king's house.",
      "M": "King Rehoboam replaced them with bronze shields and entrusted them to the commanders of the royal guard stationed at the palace entrance.",
      "T": "Bronze instead of gold — the reduction is eloquent. What had been gold became bronze; what had been the symbol of Solomon's superlative wealth became a functional substitute that made the function available but spoke of nothing glorious. The degradation from gold to bronze is the physical embodiment of the degradation from Solomon's reign to Rehoboam's. The guards still stood; the shields still existed; but the glory was gone."
    },
    "11": {
      "L": "And whenever the king went into the house of the LORD, the guard came and carried them and brought them back to the guard room.",
      "M": "Whenever the king went to the LORD's house, the guards would carry the shields and then return them to the guardroom.",
      "T": "The bronze shields were ceremonial still — brought out when the king entered the temple, carried back when he left. The form of kingly dignity was maintained with lesser materials. The ritual continued; the substance had been stripped. This is Rehoboam's legacy in a single image: the ceremony of Solomon's kingdom preserved in bronze by a king whose choices had made gold impossible."
    },
    "12": {
      "L": "And when he humbled himself the wrath of the LORD turned from him, so as not to make a complete destruction. Moreover, conditions were good in Judah.",
      "M": "Because he humbled himself, the LORD's anger turned from him and did not destroy him completely. Indeed, things went well in Judah.",
      "T": "The humbling worked — not to prevent judgment entirely, but to stop the worst of it. The LORD did not destroy completely. And the Chronicler adds the positive: things went well in Judah. After the truncated judgment came a period of recovery. Humility bought not return to the glory of Solomon but survival and some stability. The Chronicler does not overstate the recovery — it is modest — but he does not omit it. Repentance, even partial and belated, produces some good."
    },
    "13": {
      "L": "So King Rehoboam grew strong in Jerusalem and reigned. Rehoboam was forty-one years old when he began to reign, and he reigned seventeen years in Jerusalem, the city that the LORD had chosen out of all the tribes of Israel to put his name there. His mother's name was Naamah the Ammonitess.",
      "M": "Rehoboam reestablished himself in Jerusalem and continued his reign. He was forty-one years old when he became king and reigned seventeen years in Jerusalem, the city the LORD chose from all Israel's tribes as the place for his name. His mother was Naamah the Ammonite.",
      "T": "Forty-one years old, seventeen years of reign — Rehoboam died at fifty-eight, leaving a kingdom smaller than the one he inherited but still alive, still centered on Jerusalem, still hosting the temple. His mother Naamah the Ammonite is noted — one of Solomon's foreign wives (1 Kgs 14:21, 31), which means the mother of Judah's king was from the nation of Moab's cousin, the people of Lot. The dynasty that was supposed to represent the covenant carried foreign blood at the level of the queen mother. The Chronicler notes it without editorial; the reader supplies the irony."
    },
    "14": {
      "L": "And he did evil, for he did not set his heart to seek the LORD.",
      "M": "He did evil because he did not commit himself to seeking the LORD.",
      "T": "The verdict is simple and devastating: he did evil. But the Chronicler names the root cause rather than listing the symptoms: he did not set his heart to seek the LORD. The Chronicler's diagnostic of kingship is always first the heart. Rehoboam's failures — the division of the kingdom, the apostasy, the temple pillaged — all trace back to this: a king who never set his heart toward God. The kingdom was lost from the inside out."
    },
    "15": {
      "L": "Now the acts of Rehoboam, from first to last, are they not written in the records of Shemaiah the prophet and of Iddo the seer, in the manner of genealogies? And there were continual wars between Rehoboam and Jeroboam.",
      "M": "The acts of Rehoboam, from beginning to end, are recorded in the writings of Shemaiah the prophet and Iddo the seer in their genealogical records. There were constant wars between Rehoboam and Jeroboam throughout his reign.",
      "T": "Shemaiah and Iddo again — the prophetic record-keepers whose writings would preserve the full account. Genealogies here may refer to regnal chronicles organized by family trees. And the final note of Rehoboam's reign is 'continual wars with Jeroboam' — the kingdom he could not reunite by kindness he could not reconquer by force. Seventeen years of low-level warfare along a border that should not have existed, between brothers who need not have been enemies. The cost of the folly at Shechem was paid in blood for every year of his reign."
    },
    "16": {
      "L": "And Rehoboam slept with his fathers and was buried in the city of David. And Abijah his son reigned in his place.",
      "M": "Rehoboam rested with his ancestors and was buried in the city of David. His son Abijah succeeded him as king.",
      "T": "He slept with his fathers — the same dignified idiom used for Solomon, for David, for the kings who came before. Whatever Rehoboam's failures, the line held. He was buried in Jerusalem, the city of David; Abijah his son stepped onto the throne. The dynasty survived its first catastrophic king. The Davidic covenant, secured not by Rehoboam's faithfulness but by God's, carried the house of David into the next generation. That persistence, against all human probability, is the Chronicler's deepest theme: the God who chooses does not abandon his choice, even when the chosen behave as if they would prefer he did."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '2chronicles')
        merge_tier(existing, CHRONICLES2, tier_key)
        save(tier_dir, '2chronicles', existing)
    print('2 Chronicles 7–12 written.')

if __name__ == '__main__':
    main()
