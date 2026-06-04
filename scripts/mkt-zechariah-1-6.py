"""
MKT Zechariah chapters 1–6 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-zechariah-1-6.py

=== BOOK OVERVIEW ===

Zechariah is the longest of the Minor Prophets. Chapters 1–6 comprise the "Eight Night
Visions" (chs 1–6) given to Zechariah in 520 BC, the same year as Haggai's ministry,
during the reign of Darius I of Persia. The visions are framed by a call to repentance
(1:1–6) and conclude with the symbolic crowning of Joshua (6:9–15).

Structure of chapters 1–6:
  1:1–6     Prologue: call to repentance and return
  1:7–17    Vision 1 — Horsemen among the myrtle trees (cosmic reconnaissance)
  1:18–21   Vision 2 — Four horns and four craftsmen
  2:1–13    Vision 3 — The man with the measuring line (Jerusalem unmeasurable)
  3:1–10    Vision 4 — Joshua the high priest: accusation, cleansing, installation
  4:1–14    Vision 5 — The golden lampstand and two olive trees
  5:1–4     Vision 6 — The flying scroll (the curse)
  5:5–11    Vision 7 — The woman in the ephah (wickedness exiled to Babylon)
  6:1–8     Vision 8 — The four chariots (four spirits of heaven)
  6:9–15    Climax: the crowning of Joshua; messianic prophecy of The Branch

Key theological themes: divine jealousy for Zion; return from exile as new Exodus;
Zerubbabel's Spirit-empowered temple-building; the priestly high priest and royal Branch
as a fused messianic figure; purging of evil from the land; universal scope of Yahweh's
sovereignty.

=== CONTESTED-TERM DECISIONS ===

- H3068 (יהוה / Yahweh):
  L/M: "LORD" (small-caps convention, consistent with prior OT scripts).
  T: "Yahweh" in direct address, theophanic moments (2:10; 3:2), and climactic
  declarations (6:15); "the LORD" in narrative frames.
  Reason: T surfaces the covenant name where divine intimacy or climax demands it.

- H6635 (צְבָאוֹת / tseva'ot):
  L/M: "of hosts" — retained as the standard rendering.
  T: "the Almighty" in climactic oracles (1:3; 2:8; 4:6; 6:12–13); "of Heaven's Armies"
  in military-imagery contexts (1:16–17; 6:5).
  Reason: T surfaces the range of the title rather than flattening it.

- H6780 (צֶמַח / tsemach / BRANCH):
  All tiers: "the Branch" (3:8; 6:12) — the messianic royal figure who will sprout from
  David's line. L/M uppercase "Branch" to signal the technical Messianic title (also in
  Isa 4:2; Jer 23:5; 33:15). T: "the Branch" with interpretive context in the verse prose.
  Note: the name/title is identified with Zerubbabel by some scholars and with a future
  Davidic king by others; the T tier holds the tension without resolving it.

- H7854 (שָׂטָן / satan) in ch. 3:
  All tiers: "Satan" — in this context the term is transitioning from a role ("the accuser"
  / adversary) toward a proper name. L uses "the Accuser" to preserve the lexical force;
  M/T use "Satan" as the name is already becoming a title. This follows prior script
  convention in Daniel for the accusing figure.
  Correction: for L in 3:1–2 rendering is "the Accuser" to surface the accusatory role.

- H7307 (רוּחַ / ruach):
  4:6 — "Spirit" (divine Spirit, capital S in all tiers; this is Yahweh's Spirit enabling
  Zerubbabel's work).
  5:9 — "wind" (natural wind carrying the ephah; L/M "wind", T "great wind").
  6:5 — "spirits" / "winds" — the four spirits of heaven (divine agents); L "spirits",
  M "winds", T "four celestial spirits" to capture both senses.
  Reason: 6:5 is genuinely ambiguous (ruchot = spirits/winds); the four winds / four
  spirits of heaven interpretation is consistent with Revelation's later use.

- H430 (אֱלֹהִים / Elohim) in 6:15:
  "your God" — all tiers. The covenant formula "LORD your God" frames the conditional
  promise; rendering is standard.

- H5771 (עָוֹן / avon / iniquity):
  3:4 "iniquity" (L/M), T "guilt" — the removal of Joshua's priestly guilt is a
  forensic-covenantal act, not merely a moral cleansing.
  3:9 "iniquity of this land" — all tiers: "iniquity"; T surface the national-atonement
  scope.

- H2146 (זִכָּרוֹן / zikaron / memorial):
  6:14 "memorial/reminder" — L "memorial", M "memorial", T "lasting reminder" — the
  crowns left in the temple function as a witness to the prophetic promise.

- H3323 (יִצְהָר / yitshar) and H4899 (מָשִׁיחַ / mashiach):
  4:14 "anointed ones" — the two yitshar-ones (lit. "sons of fresh oil") standing by
  the Lord. L "sons of fresh oil", M "anointed ones", T "the two anointed ones" — Joshua
  (priest) and Zerubbabel (royal governor) as the two mediators. This verse is foundational
  for later two-messiah expectations and Revelation 11.

- OT echoes noted:
  1:2–6: The standard Deuteronomic call-and-response: the prophets called, fathers did
  not hear, Yahweh's word overtook them. Echo of Deut 30:1–10 and Jer 25.
  2:5: Wall of fire = Exodus pillar of fire (Exod 13:21); glory in the midst = Sinai and
  the tabernacle.
  2:10–11: "I will dwell in your midst" — tabernacle/temple theology; echo of Lev 26:12.
  3:2: "Brand plucked from the fire" — Israel saved from exile barely; Amos 4:11 echo.
  4:6: "Not by might nor by power but by my Spirit" — directly counters reliance on
  Babylonian imperial power; new-Exodus register.
  6:12–13: The Branch who builds the temple and sits as priest-king echoes Ps 110 (priest
  after the order of Melchizedek + royal throne).

- Textual notes:
  2:8: "After his glory he sent me" — a notoriously difficult clause. The MT has the
  messenger identifying himself as sent after/for the glory. Some read "the one who sent me"
  as the Father and the "me" as a divine messenger; L preserves the syntax, M/T interpret.
  3:5: Zechariah himself (first person) interrupts the vision to request the clean turban.
  This is significant — the prophet participates in the vision.
  4:2: "Seven lips" (or "pipes/channels") on each lamp — the exact mechanism is debated.
  Rendered "seven spouts" in L, "seven channels" in M/T.
  6:14: MT "Helem" differs from v.10 "Heldai" — likely variant name for the same person.
  Preserved in translation.
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

ZECHARIAH = {
  "1": {
    "1": {
      "L": "In the eighth month, in the second year of Darius, the word of the LORD came to Zechariah the son of Berechiah, son of Iddo the prophet, saying:",
      "M": "In the eighth month of the second year of Darius, the word of the LORD came to the prophet Zechariah son of Berechiah son of Iddo:",
      "T": "In the eighth month of Darius's second year, Yahweh's word came to the prophet Zechariah son of Berechiah son of Iddo."
    },
    "2": {
      "L": "The LORD was greatly displeased with your fathers.",
      "M": "The LORD was very angry with your ancestors.",
      "T": "Yahweh burned with anger against your ancestors — this is where you come from."
    },
    "3": {
      "L": "Therefore say to them, Thus says the LORD of hosts: Return to me, says the LORD of hosts, and I will return to you, says the LORD of hosts.",
      "M": "Therefore say to them, This is what the LORD of hosts says: Return to me, declares the LORD of hosts, and I will return to you, declares the LORD of hosts.",
      "T": "So tell them: This is the word of Yahweh the Almighty — Come back to me, and I will come back to you. The door moves from both sides."
    },
    "4": {
      "L": "Do not be like your fathers, to whom the former prophets cried out, Thus says the LORD of hosts: Return now from your evil ways and from your evil deeds. But they did not hear or give heed to me, declares the LORD.",
      "M": "Do not be like your ancestors, to whom the earlier prophets called: This is what the LORD of hosts says — Turn from your evil ways and your evil deeds. But they did not listen or pay attention to me, declares the LORD.",
      "T": "Don't repeat your ancestors' mistake. The earlier prophets called out: Yahweh commands — turn from your evil paths and your wicked deeds. They refused to listen; they refused to pay attention. Don't be them."
    },
    "5": {
      "L": "Your fathers — where are they? And the prophets, do they live forever?",
      "M": "Where are your ancestors now? And the prophets — do they live forever?",
      "T": "Your ancestors are gone. The prophets who warned them are gone. What remains is Yahweh's word — and what it did to them."
    },
    "6": {
      "L": "But my words and my statutes, which I commanded my servants the prophets, did they not overtake your fathers? So they returned and said, As the LORD of hosts purposed to do to us, according to our ways and our deeds, so has he dealt with us.",
      "M": "But did not my words and my decrees, which I commanded my servants the prophets, overtake your ancestors? So they repented and said, The LORD of hosts has dealt with us according to our ways and deeds, just as he intended.",
      "T": "But my words and my decrees — given through the prophets, my servants — those ran your ancestors down and caught them. In the end they admitted it: Yahweh the Almighty carried out exactly what he promised, deed for deed, according to what we had done."
    },
    "7": {
      "L": "On the twenty-fourth day of the eleventh month, which is the month of Shebat, in the second year of Darius, the word of the LORD came to Zechariah the son of Berechiah, son of Iddo the prophet, saying:",
      "M": "On the twenty-fourth day of the eleventh month — the month of Shebat — in the second year of Darius, the word of the LORD came to the prophet Zechariah son of Berechiah son of Iddo.",
      "T": "On the twenty-fourth of Shebat — three months into Darius's second year — Yahweh's word came again to Zechariah son of Berechiah son of Iddo."
    },
    "8": {
      "L": "I saw in the night, and behold, a man riding on a red horse! He was standing among the myrtle trees in the glen, and behind him were red, sorrel, and white horses.",
      "M": "During the night I had a vision — a man riding a red horse, standing among the myrtle trees in the ravine, with red, sorrel, and white horses behind him.",
      "T": "In the night vision a rider appeared on a red horse, standing still among myrtle trees in a shadowed ravine. Behind him, more horses — red, sorrel, white. The whole earth is under surveillance."
    },
    "9": {
      "L": "Then I said, What are these, my lord? The angel who talked with me said to me, I will show you what they are.",
      "M": "I asked, What are these, my lord? The angel who was speaking with me said, I will show you what they are.",
      "T": "I asked the angel beside me, What are all these? He said, Let me show you."
    },
    "10": {
      "L": "So the man who was standing among the myrtle trees answered and said, These are they whom the LORD has sent to patrol the earth.",
      "M": "Then the man standing among the myrtle trees spoke up and said, These are those whom the LORD has sent to patrol throughout the earth.",
      "T": "The rider among the myrtles answered: these are Yahweh's scouts — sent to patrol the whole earth."
    },
    "11": {
      "L": "And they answered the angel of the LORD who was standing among the myrtle trees and said, We have patrolled the earth, and behold, all the earth is at rest and quiet.",
      "M": "They reported to the angel of the LORD who was standing among the myrtle trees, We have patrolled the earth and found the whole earth at rest and peaceful.",
      "T": "The patrol returned their report to the angel of the LORD standing in the myrtles: We have gone through the whole earth — and it is still, it is settled. Not a nation trembles."
    },
    "12": {
      "L": "Then the angel of the LORD said, O LORD of hosts, how long will you have no mercy on Jerusalem and the cities of Judah, against which you have been angry these seventy years?",
      "M": "At this the angel of the LORD said, LORD of hosts, how long will you withhold mercy from Jerusalem and the cities of Judah? You have been angry with them for seventy years now.",
      "T": "Then the angel of the LORD prayed aloud: How long, Yahweh of Heaven's Armies? Seventy years of your anger against Jerusalem and Judah's cities — how long until you show mercy?"
    },
    "13": {
      "L": "And the LORD answered the angel who talked with me with good and comforting words.",
      "M": "The LORD answered the angel who was speaking with me with gracious and comforting words.",
      "T": "Yahweh answered — and the words were kind, words of comfort."
    },
    "14": {
      "L": "So the angel who talked with me said to me, Cry out: Thus says the LORD of hosts, I am exceedingly jealous for Jerusalem and for Zion.",
      "M": "Then the angel who was speaking with me told me, Proclaim this: This is what the LORD of hosts says — I am burning with jealousy for Jerusalem and for Zion.",
      "T": "The angel said to me, Announce this: Yahweh the Almighty declares — I am consumed with jealousy for Jerusalem, for Zion. My love for this city is as fierce as fire."
    },
    "15": {
      "L": "And I am exceedingly angry with the nations that are at ease; for while I was angry but a little, they helped forward the affliction.",
      "M": "But I am very angry with the nations that are complacent; for I was only a little angry, yet they intensified the disaster.",
      "T": "As much as I burn for Zion, I burn with fury against the nations who sat at ease. I let them serve as my instrument — but they went far beyond my anger. They made my judgment into a massacre."
    },
    "16": {
      "L": "Therefore, thus says the LORD, I have returned to Jerusalem with mercy; my house shall be built in it, declares the LORD of hosts, and a measuring line shall be stretched out over Jerusalem.",
      "M": "Therefore, this is what the LORD says: I have returned to Jerusalem with compassion. My house will be rebuilt there, declares the LORD of hosts, and a measuring line will be stretched over Jerusalem.",
      "T": "So hear Yahweh's word: I have come back to Jerusalem with compassion. The temple will be built — Yahweh of Heaven's Armies promises it. And the surveyor's line is already being stretched across Jerusalem; it is a city being rebuilt."
    },
    "17": {
      "L": "Cry out again: Thus says the LORD of hosts, My cities shall again overflow with prosperity, and the LORD shall again comfort Zion and shall again choose Jerusalem.",
      "M": "Proclaim further: This is what the LORD of hosts says — My cities will again overflow with abundance, and the LORD will again comfort Zion and again choose Jerusalem.",
      "T": "Proclaim it again: Yahweh the Almighty says — my cities will spill over with good things. The LORD will comfort Zion again; he will choose Jerusalem again, as he always has."
    },
    "18": {
      "L": "And I lifted my eyes and saw, and behold, four horns!",
      "M": "Then I looked up and saw four horns.",
      "T": "I looked up: four horns."
    },
    "19": {
      "L": "And I said to the angel who talked with me, What are these? And he said to me, These are the horns that have scattered Judah, Israel, and Jerusalem.",
      "M": "I asked the angel who was speaking with me, What are these? He answered, These are the horns that scattered Judah, Israel, and Jerusalem.",
      "T": "I asked the angel beside me, What are these? He answered: the four powers that shattered Judah, Israel, and Jerusalem — scattered them to the winds."
    },
    "20": {
      "L": "Then the LORD showed me four craftsmen.",
      "M": "Then the LORD showed me four craftsmen.",
      "T": "Then Yahweh showed me something else: four smiths."
    },
    "21": {
      "L": "And I said, What are these coming to do? He said to me, These are the horns that scattered Judah so that no man raised his head. And these craftsmen have come to terrify them, to cast down the horns of the nations that lifted up their horn against the land of Judah to scatter it.",
      "M": "I asked, What have these come to do? He said, These are the horns that scattered Judah so that no one could raise his head. Now these craftsmen have come to terrify them and to throw down the horns of the nations that raised their horn against the land of Judah to scatter its people.",
      "T": "I asked, What are they here to do? He said: These smiths have come to break the horns — the powers that shattered Judah so completely no one could even lift their head. Those nations raised their horns against Yahweh's land; now comes the counter-blow."
    }
  },
  "2": {
    "1": {
      "L": "And I lifted my eyes and saw, and behold, a man with a measuring line in his hand!",
      "M": "Then I looked up and saw a man with a measuring line in his hand.",
      "T": "I looked up: a man holding a surveyor's line."
    },
    "2": {
      "L": "Then I said, Where are you going? And he said to me, To measure Jerusalem, to see what is its width and what is its length.",
      "M": "I asked, Where are you going? He answered, To measure Jerusalem — to find out its width and its length.",
      "T": "I asked where he was going. He said: to measure Jerusalem — to calculate its width and its length."
    },
    "3": {
      "L": "And behold, the angel who talked with me came forward, and another angel came forward to meet him,",
      "M": "Then the angel who had been speaking with me went forward, and another angel came forward to meet him.",
      "T": "Then the angel who was with me stepped forward — and another angel came out to intercept him."
    },
    "4": {
      "L": "and said to him, Run, say to that young man, Jerusalem shall be inhabited as towns without walls, because of the multitude of people and livestock in it.",
      "M": "The second angel said, Run and tell that young man: Jerusalem will be filled with people and animals, spread out like open villages without walls.",
      "T": "The second angel said: Run, tell him — Jerusalem will burst its seams. So many people, so many animals, it will spread like open country with no walls to hold it."
    },
    "5": {
      "L": "For I will be to her a wall of fire all around, declares the LORD, and I will be the glory in her midst.",
      "M": "For I will be a wall of fire around her, declares the LORD, and I will be the glory within her.",
      "T": "Yahweh himself declares it: I will be her wall — a wall of fire circling her. And my glory will live inside her. No stone rampart is needed when the living God is the city's defense."
    },
    "6": {
      "L": "Up! Up! Flee from the land of the north, declares the LORD. For I have spread you abroad as the four winds of the heavens, declares the LORD.",
      "M": "Come, come! Flee from the land of the north, declares the LORD, for I have scattered you to the four winds of heaven, declares the LORD.",
      "T": "Up! Up! Get out of the north — now! says Yahweh. I scattered you like seed to the four winds of heaven; now I am gathering. Do not stay where I have called you out from."
    },
    "7": {
      "L": "Escape to Zion, O you who dwell with the daughter of Babylon!",
      "M": "Come, escape from Babylon, you who live there, daughter of Zion!",
      "T": "Escape, all you who live in Babylon's shadow — come home to Zion!"
    },
    "8": {
      "L": "For thus says the LORD of hosts: After his glory he sent me to the nations that plundered you, for he who touches you touches the apple of his eye.",
      "M": "For this is what the LORD of hosts says: After his glory he sent me against the nations that plundered you — for whoever touches you touches the apple of his eye.",
      "T": "Yahweh the Almighty speaks through the messenger: I was sent — after the glory — against the nations that plundered you. Here is the measure of how much he cares: to touch Israel is to jab a finger in Yahweh's own eye."
    },
    "9": {
      "L": "For behold, I will shake my hand over them, and they shall become plunder for those who served them. Then you will know that the LORD of hosts has sent me.",
      "M": "See, I am going to raise my hand against them, and they will become plunder for their own former servants. Then you will know that the LORD of hosts has sent me.",
      "T": "Watch: I am lifting my hand against those nations. The ones they enslaved will plunder them. And when it happens, you will know that Yahweh the Almighty sent me."
    },
    "10": {
      "L": "Sing and rejoice, O daughter of Zion! For behold, I come and I will dwell in your midst, declares the LORD.",
      "M": "Shout and rejoice, daughter of Zion! For I am coming, and I will dwell in your midst, declares the LORD.",
      "T": "Sing, Zion — shout for joy! Yahweh is coming to live among you. This is the promise of the living God."
    },
    "11": {
      "L": "And many nations shall join themselves to the LORD in that day and shall be my people. And I will dwell in your midst, and you shall know that the LORD of hosts has sent me to you.",
      "M": "Many nations will join themselves to the LORD on that day and will become my people. I will dwell in your midst, and you will know that the LORD of hosts has sent me to you.",
      "T": "On that day many nations will attach themselves to Yahweh and become his people. He will live among you, and you will know beyond doubt that Yahweh the Almighty sent me. The covenant once made with Israel will expand to encompass the nations."
    },
    "12": {
      "L": "And the LORD will inherit Judah as his portion in the holy land, and will again choose Jerusalem.",
      "M": "The LORD will take Judah as his portion in the holy land, and will once again choose Jerusalem.",
      "T": "Yahweh will claim Judah as his own inheritance in the holy land — and Jerusalem will be chosen again, as it was chosen before."
    },
    "13": {
      "L": "Be silent, all flesh, before the LORD, for he has roused himself from his holy dwelling.",
      "M": "Let all people be silent before the LORD, for he has stirred from his holy dwelling.",
      "T": "Hush — all humanity — before Yahweh. He is awake. He has risen from his holy dwelling place and is on the move."
    }
  },
  "3": {
    "1": {
      "L": "Then he showed me Joshua the high priest standing before the angel of the LORD, and the Accuser standing at his right hand to accuse him.",
      "M": "Then he showed me Joshua the high priest standing before the angel of the LORD, with Satan standing at his right hand to accuse him.",
      "T": "Then the vision shifted: Joshua the high priest stood before the angel of the LORD — and Satan stood at his right hand, ready to press charges."
    },
    "2": {
      "L": "And the LORD said to the Accuser, The LORD rebuke you, O Accuser! The LORD who has chosen Jerusalem rebuke you! Is not this a brand plucked from the fire?",
      "M": "The LORD said to Satan, The LORD rebuke you, Satan! The LORD who has chosen Jerusalem rebuke you! Is this not a burning stick snatched from the fire?",
      "T": "But Yahweh spoke directly to Satan: Yahweh rebukes you, Satan. Yahweh, who has chosen Jerusalem, rebukes you. Look at this man — he is a burning brand just pulled from the fire. You do not get to prosecute what I have rescued."
    },
    "3": {
      "L": "Now Joshua was standing before the angel, clothed with filthy garments.",
      "M": "Joshua was dressed in filthy garments as he stood before the angel.",
      "T": "Joshua stood there in filthy clothes — the accumulated filth of exile, of priestly defilement, of a people who had failed."
    },
    "4": {
      "L": "And the angel said to those who were standing before him, Remove the filthy garments from him. And to him he said, Behold, I have taken your iniquity away from you, and I will clothe you with pure vestments.",
      "M": "The angel said to those standing before him, Take off his filthy garments. Then he said to Joshua, See, I have taken your guilt away from you, and I will clothe you with fine robes.",
      "T": "The angel commanded those attending: Strip off those filthy clothes. Then, turning to Joshua: Your guilt has been removed. I am clothing you in clean garments. The old is gone."
    },
    "5": {
      "L": "And I said, Let them put a clean turban on his head. So they put a clean turban on his head and clothed him with garments. And the angel of the LORD was standing by.",
      "M": "Then I said, Let them put a clean turban on his head. So they put a clean turban on his head and clothed him in the robes, while the angel of the LORD stood nearby.",
      "T": "I called out myself: Put a clean turban on his head! So they placed the clean turban on him and clothed him fully — while the angel of the LORD stood there watching it all done."
    },
    "6": {
      "L": "And the angel of the LORD solemnly assured Joshua, saying,",
      "M": "Then the angel of the LORD gave Joshua this solemn charge:",
      "T": "Then the angel of the LORD spoke formally to Joshua — this was a charge, not a comfort:"
    },
    "7": {
      "L": "Thus says the LORD of hosts: If you will walk in my ways and keep my charge, then you shall rule my house and have charge of my courts, and I will give you the right of access among those who are standing here.",
      "M": "This is what the LORD of hosts says: If you walk in my ways and faithfully keep my requirements, then you will govern my house and have charge of my courts, and I will give you free access among those who stand here.",
      "T": "Yahweh the Almighty speaks: Joshua, if you walk in my ways and keep my charge — then I give you the oversight of my house, authority in my courts, and the right to move freely among the angels who stand in my presence. Obedience is the condition; access is the promise."
    },
    "8": {
      "L": "Hear now, O Joshua the high priest, you and your friends who sit before you, for they are men who are a sign: behold, I will bring my servant the Branch.",
      "M": "Listen, Joshua the high priest — you and your associates who sit before you, for they are men who are a sign. I am going to bring my servant, the Branch.",
      "T": "Listen, Joshua the high priest — you and all the priests sitting with you. You are men of sign, living prophecy. Here is what you are a sign of: I am about to bring my servant — the Branch."
    },
    "9": {
      "L": "For behold, the stone that I have set before Joshua — on a single stone are seven eyes. Behold, I will engrave its inscription, declares the LORD of hosts, and I will remove the iniquity of this land in a single day.",
      "M": "See, the stone I have set in front of Joshua — on that one stone are seven eyes. I am going to engrave an inscription on it, declares the LORD of hosts, and I will remove the iniquity of this land in a single day.",
      "T": "See this stone I have placed before Joshua — one stone, and on it seven eyes watching everything. I am engraving it myself, Yahweh the Almighty declares, and on a single day I will wipe out the iniquity of this land entirely. One act. One day. Everything clean."
    },
    "10": {
      "L": "In that day, declares the LORD of hosts, every one of you will invite his neighbor to come under his vine and under his fig tree.",
      "M": "On that day, declares the LORD of hosts, each of you will invite his neighbor under his vine and fig tree.",
      "T": "When that day comes — Yahweh the Almighty promises it — neighbors will call to neighbors: Come, sit under my vine. Rest under my fig tree. It is the oldest image of peace, and it will be real."
    }
  },
  "4": {
    "1": {
      "L": "And the angel who talked with me came again and woke me, like a man who is wakened out of his sleep.",
      "M": "Then the angel who had been speaking with me returned and woke me, like someone roused from sleep.",
      "T": "The angel came back and woke me — shaking me like someone startled out of a deep sleep."
    },
    "2": {
      "L": "And he said to me, What do you see? I said, I see, and behold, a lampstand all of gold, with a bowl on its top and seven lamps on it, and seven spouts to the seven lamps that are on its top.",
      "M": "He asked me, What do you see? I answered, I see a solid gold lampstand with a bowl at the top, seven lamps on it, and seven channels feeding the seven lamps at the top.",
      "T": "He asked what I saw. I told him: a lampstand, solid gold, with a bowl at its crown. Seven lamps on it, and seven channels running oil to each lamp. A design made for endless, sustained light."
    },
    "3": {
      "L": "And there are two olive trees by it, one on the right of the bowl and the other on its left.",
      "M": "There are also two olive trees beside it — one on the right of the bowl and one on the left.",
      "T": "Two olive trees stood beside it — one on the right of the bowl, one on the left. Living sources of oil, feeding the light continuously."
    },
    "4": {
      "L": "And I said to the angel who talked with me, What are these, my lord?",
      "M": "I asked the angel who was speaking with me, What are these, my lord?",
      "T": "I turned to the angel: What does this all mean?"
    },
    "5": {
      "L": "Then the angel who talked with me answered and said to me, Do you not know what these are? I said, No, my lord.",
      "M": "The angel who was speaking with me answered, Do you not know what these are? I said, No, my lord.",
      "T": "He answered my question with a question: Do you not know what these are? I admitted: No, my lord."
    },
    "6": {
      "L": "Then he said to me, This is the word of the LORD to Zerubbabel: Not by might, nor by power, but by my Spirit, says the LORD of hosts.",
      "M": "He replied, This is the word of the LORD to Zerubbabel: Not by might, nor by power, but by my Spirit, says the LORD of hosts.",
      "T": "He said: This is Yahweh's word for Zerubbabel. Not by military force. Not by human power. Only by my Spirit — says Yahweh the Almighty. The temple will be built not by what Zerubbabel can marshal, but by what God supplies."
    },
    "7": {
      "L": "Who are you, O great mountain? Before Zerubbabel you shall become a plain. And he shall bring forward the capstone amid shouts of Grace, grace to it!",
      "M": "What are you, mighty mountain? Before Zerubbabel you will become level ground! Then he will bring out the capstone with shouts of Grace, grace to it!",
      "T": "Every obstacle looming over this work — every great mountain of opposition — will become flat ground before Zerubbabel. And when he sets the capstone in place, the crowd will cry out: Grace! Grace! Yahweh's unearned favor carried this to completion."
    },
    "8": {
      "L": "Then the word of the LORD came to me, saying,",
      "M": "The word of the LORD came to me again:",
      "T": "Then Yahweh's word came to me a second time:"
    },
    "9": {
      "L": "The hands of Zerubbabel have laid the foundation of this house; his hands shall also complete it. Then you will know that the LORD of hosts has sent me to you.",
      "M": "The hands of Zerubbabel laid the foundation of this temple; his hands will also complete it. Then you will know that the LORD of hosts has sent me to you.",
      "T": "Zerubbabel's hands laid the foundation — and Zerubbabel's hands will set the final stone. Same person, start to finish. When it stands complete, you will know that Yahweh the Almighty sent me to you with this word."
    },
    "10": {
      "L": "For who has despised the day of small things? They shall rejoice and shall see the plumb line in the hand of Zerubbabel. These seven are the eyes of the LORD, which range through the whole earth.",
      "M": "Who despises the day of small beginnings? They will rejoice when they see the plumb line in the hand of Zerubbabel. These seven are the eyes of the LORD, ranging over the whole earth.",
      "T": "Who dares to despise this small beginning? Those who mocked will be the ones who rejoice when they see Zerubbabel with the plumb line in his hand — the work is real. The seven lamps are the seven eyes of Yahweh, watching everything on earth. Nothing is hidden from him; no small thing escapes his notice."
    },
    "11": {
      "L": "Then I said to him, What are these two olive trees on the right and the left of the lampstand?",
      "M": "Then I asked him, What are these two olive trees on the right and left of the lampstand?",
      "T": "I pressed him again: What are the two olive trees — one on the lampstand's right, one on its left?"
    },
    "12": {
      "L": "And I asked him a second time, What are these two branches of the olive trees that empty themselves through the two golden pipes?",
      "M": "I asked him again, What are these two olive branches that pour out golden oil through the two golden pipes?",
      "T": "I asked it more precisely: What are these two olive branches that channel golden oil through the golden pipes? Where does the supply come from, and what does it mean?"
    },
    "13": {
      "L": "He said to me, Do you not know what these are? I said, No, my lord.",
      "M": "He said to me, Do you not know what these are? I answered, No, my lord.",
      "T": "He asked again: Do you not know? And again I had to say: No, my lord. I do not."
    },
    "14": {
      "L": "Then he said, These are the two sons of fresh oil who stand by the Lord of the whole earth.",
      "M": "He said, These are the two anointed ones who stand in the presence of the Lord of the whole earth.",
      "T": "He said: These are the two anointed ones — the two who stand beside the Lord of all the earth. They are the living conduit between the divine source and the lampstand's light. Priest and king, feeding the light that illumines the world."
    }
  },
  "5": {
    "1": {
      "L": "Again I lifted my eyes and saw, and behold, a flying scroll!",
      "M": "I looked up again and saw a scroll flying through the air.",
      "T": "I looked up: a scroll flying."
    },
    "2": {
      "L": "And he said to me, What do you see? I answered, I see a flying scroll; its length is twenty cubits, and its width ten cubits.",
      "M": "He asked, What do you see? I replied, A flying scroll — thirty feet long and fifteen feet wide.",
      "T": "He asked what I saw. I told him: a scroll, in flight — thirty feet long and fifteen feet wide. Large enough to be read. Large enough to cover everything."
    },
    "3": {
      "L": "Then he said to me, This is the curse that goes out over the face of the whole land. For everyone who steals shall be cleaned out according to what is written on one side, and everyone who swears falsely shall be cleaned out according to what is written on the other side.",
      "M": "He told me, This is the curse that goes out over the whole land. According to one side of it, every thief will be removed; according to the other side, everyone who swears falsely will be removed.",
      "T": "He said: This is the curse flying over the whole land. One side covers theft; the other covers false oaths. The scroll is the Torah's covenant curse — Deuteronomy 28 made visible and mobile — hunting down every violator in the land."
    },
    "4": {
      "L": "I will send it out, declares the LORD of hosts, and it shall enter the house of the thief and the house of him who swears falsely by my name. It shall remain in his house and consume it, timber and stones.",
      "M": "I will send it out, declares the LORD of hosts, and it will enter the house of the thief and the house of whoever swears falsely in my name. It will remain in that house and destroy it, timber and stones alike.",
      "T": "Yahweh the Almighty declares: I am sending this curse. It will enter the thief's house; it will enter the house of anyone who swears falsely by my name. It will settle into the walls and consume everything — wood and stone, roof and foundation. Nothing will be left."
    },
    "5": {
      "L": "Then the angel who talked with me came forward and said to me, Lift your eyes now and see what this is that is going out.",
      "M": "Then the angel who was speaking with me came forward and said, Look up and see what this is that is appearing.",
      "T": "The angel stepped forward: Look up. Something else is coming out."
    },
    "6": {
      "L": "And I said, What is it? He said, This is the basket that is going out. And he said, This is their iniquity throughout all the land.",
      "M": "I asked, What is it? He said, This is a measuring basket going out. And he added, This represents the iniquity of the people throughout the land.",
      "T": "I asked: What is it? He said: An ephah — a measuring basket. And then: This is their iniquity, the accumulated wickedness of the whole land, gathered and concentrated."
    },
    "7": {
      "L": "And behold, a lead cover was lifted, and there was a woman sitting inside the basket.",
      "M": "Then the heavy lead cover was raised, and there was a woman sitting inside the basket.",
      "T": "The lead cover was lifted — and there was a woman sitting inside the ephah."
    },
    "8": {
      "L": "And he said, This is Wickedness. And he thrust her back into the basket and pressed the lead weight down on its opening.",
      "M": "He said, This is Wickedness. Then he pushed her back down into the basket and pressed the heavy lead lid over the opening.",
      "T": "He said simply: This is Wickedness. Then he shoved her back down and slammed the lead cover shut. Wickedness is real, it is personal, and it is being contained."
    },
    "9": {
      "L": "Then I lifted my eyes and saw, and behold, two women coming forward! The wind was in their wings. They had wings like the wings of a stork, and they lifted the basket up between earth and heaven.",
      "M": "I looked up and saw two women coming with the wind in their wings — they had wings like a stork's wings — and they lifted the basket up between earth and heaven.",
      "T": "I looked up: two women, wings like a stork's, and the wind filling their wings. They lifted the basket up between earth and sky — carrying wickedness away."
    },
    "10": {
      "L": "Then I said to the angel who talked with me, Where are they taking the basket?",
      "M": "I asked the angel who was speaking with me, Where are they taking the basket?",
      "T": "I asked the angel: Where are they taking it?"
    },
    "11": {
      "L": "He said to me, To build a house for it in the land of Shinar. When it is ready, the basket will be set down there on its base.",
      "M": "He replied, To the land of Shinar, to build a temple for it. When the temple is ready, the basket will be placed there on its pedestal.",
      "T": "He said: To Shinar — Babylon — where they will build it a shrine. Wickedness belongs in Babylon; it will be housed there, on its own pedestal, in the land where idolatry was born. It is being removed from Yahweh's land."
    }
  },
  "6": {
    "1": {
      "L": "And again I lifted my eyes and saw, and behold, four chariots coming out from between two mountains. And the mountains were mountains of bronze.",
      "M": "Again I looked up and saw four chariots coming out from between two mountains — mountains of bronze.",
      "T": "I looked up: four chariots emerging from between two bronze mountains. The image is cosmic — Yahweh's court dispatching his agents into every quarter of the world."
    },
    "2": {
      "L": "The first chariot had red horses, the second chariot had black horses,",
      "M": "The first chariot had red horses, the second had black horses,",
      "T": "Red horses pulled the first chariot; black horses the second."
    },
    "3": {
      "L": "the third chariot had white horses, and the fourth chariot had dappled horses — all of them strong.",
      "M": "the third had white horses, and the fourth had dappled horses — powerful animals.",
      "T": "White horses pulled the third; dappled horses — strong, striking — pulled the fourth."
    },
    "4": {
      "L": "Then I answered and said to the angel who talked with me, What are these, my lord?",
      "M": "I asked the angel who was speaking with me, What are these, my lord?",
      "T": "I asked the angel: What are these?"
    },
    "5": {
      "L": "And the angel answered and said to me, These are the four spirits of the heavens, going out after presenting themselves before the Lord of all the earth.",
      "M": "The angel answered, These are the four winds of heaven, going out after presenting themselves before the Lord of all the earth.",
      "T": "The angel answered: These are the four celestial spirits of heaven — Yahweh's agents going out into every quarter of the earth after standing in his presence. The whole earth is under his governance."
    },
    "6": {
      "L": "The one with the black horses goes toward the north country, the white ones go after them, and the dappled ones go toward the south country.",
      "M": "The chariot with black horses is heading north, the white horses follow them, and the dappled ones head south.",
      "T": "The black horses go north — toward Babylon, the great threat. The white follow after them. The dappled drive south. Each direction covered, each power watched."
    },
    "7": {
      "L": "When the strong horses came out, they were eager to go and patrol the earth. And he said, Go, patrol the earth. So they went and patrolled the earth.",
      "M": "When the powerful horses came out, they were straining to go and patrol the earth. He said, Go, patrol the earth. And they went and patrolled it.",
      "T": "The strong horses strained forward, impatient to be sent. He commanded: Go — patrol the earth. And they went, covering every corner."
    },
    "8": {
      "L": "Then he cried to me, Behold, those who go toward the north country have set my Spirit at rest in the north country.",
      "M": "Then he called out to me, See, those who have gone to the north country have given my Spirit rest there.",
      "T": "Then he called to me: Look — the ones who went north have settled my Spirit there. Yahweh's wrath toward the north has been satisfied. Babylon's power is broken; his anger has found its rest."
    },
    "9": {
      "L": "And the word of the LORD came to me, saying,",
      "M": "Then the word of the LORD came to me:",
      "T": "Then Yahweh's word came to me directly:"
    },
    "10": {
      "L": "Take from the exiles Heldai, Tobijah, and Jedaiah, who have arrived from Babylon, and go the same day to the house of Josiah son of Zephaniah.",
      "M": "Take silver and gold from the exiles — Heldai, Tobijah, and Jedaiah — who have come from Babylon, and go that same day to the house of Josiah son of Zephaniah.",
      "T": "Take gifts from the delegation just arrived from Babylon — Heldai, Tobijah, Jedaiah — and go that same day to Josiah son of Zephaniah's house."
    },
    "11": {
      "L": "Take silver and gold, and make crowns, and set them on the head of Joshua son of Jehozadak the high priest.",
      "M": "Take the silver and gold, fashion crowns, and place them on the head of Joshua son of Jehozadak the high priest.",
      "T": "From their silver and gold, make crowns. Place them on the head of Joshua son of Jehozadak — the high priest. This is a prophetic act: a priest wearing a crown."
    },
    "12": {
      "L": "And say to him, Thus says the LORD of hosts: Behold, the man whose name is the Branch; for he shall branch out from his place and he shall build the temple of the LORD.",
      "M": "Then say to him, This is what the LORD of hosts says: Here is the man whose name is the Branch. He will branch out from his own place and build the temple of the LORD.",
      "T": "And speak this word to him: Yahweh the Almighty says — Here is the man. His name is the Branch. He will grow up from where he is planted and build Yahweh's temple. What Zerubbabel has begun, the Branch will complete and perfect."
    },
    "13": {
      "L": "It is he who shall build the temple of the LORD and shall bear royal honor, and shall sit and rule on his throne. And there shall be a priest on his throne, and the counsel of peace shall be between them both.",
      "M": "He will build the temple of the LORD, and he will be clothed with majesty. He will sit and rule on his throne, and there will also be a priest on his throne. Peaceful counsel will exist between the two of them.",
      "T": "He will build the temple — and he will bear royal majesty. He will sit on his throne and rule. But he will also be a priest on that throne. Two roles in one person. The counsel of peace will flow between king and priest — because they are the same. This is the promise of Psalm 110 made visible: priest and king, Melchizedek's successor, at last."
    },
    "14": {
      "L": "And the crowns shall be in the temple of the LORD as a memorial to Helem, Tobijah, Jedaiah, and Hen son of Zephaniah.",
      "M": "The crowns will be kept in the temple of the LORD as a memorial to Helem, Tobijah, Jedaiah, and Hen son of Zephaniah.",
      "T": "The crowns will be hung in Yahweh's temple — a lasting reminder of Helem, Tobijah, Jedaiah, and Hen son of Zephaniah, and of what was spoken and enacted on this day."
    },
    "15": {
      "L": "And those who are far off shall come and build the temple of the LORD. And you shall know that the LORD of hosts has sent me to you. And this shall come to pass if you will diligently obey the voice of the LORD your God.",
      "M": "Those who are far away will come and help build the temple of the LORD, and you will know that the LORD of hosts has sent me to you. This will come to pass if you diligently obey the LORD your God.",
      "T": "People from distant lands will come and help build Yahweh's temple. And when they do, you will know that Yahweh the Almighty truly sent me with these words. But this is conditional: all of it comes to pass only if you faithfully obey the voice of Yahweh your God. The promise is sure; the door of obedience must be walked through."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'zechariah')
        merge_tier(existing, ZECHARIAH, tier_key)
        save(tier_dir, 'zechariah', existing)
    print('Zechariah 1–6 written.')

if __name__ == '__main__':
    main()
