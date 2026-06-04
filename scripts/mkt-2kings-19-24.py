"""
MKT 2 Kings chapters 19–24 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-2kings-19-24.py

Translation decisions:
- H3068 (יהוה): "LORD" (small-caps convention) in L/M; "the LORD" in T. Consistent with
  all prior 2 Kings scripts.
- H430 (אֱלֹהִים): "God" in all tiers.
- H6918 (קָדוֹשׁ): "Holy One" — Isaiah's characteristic title "Holy One of Israel" preserved
  in all three tiers. The title grounds the whole oracle against Sennacherib in 19:22.
- H7307 (רוּחַ) in 19:7: "a blast / a spirit" in L/M; "a foreboding" in T. This is not
  the divine Spirit — it is an induced impulse God puts in Sennacherib driving his retreat.
  The same root can mean Spirit, wind, or breath; context here demands the psychological sense.
- H8052 (שְׁמוּעָה): "rumour" (19:7) in L; "a report" in M; "disturbing news" in T.
- H1285 (בְּרִית): "covenant" throughout. 23:3 is the pivotal covenant-renewal scene — the
  threefold structure (LORD/king/people) echoes 2 Sam 5:3, Josh 24:25, and Deut 17:18-20.
  T notes the constitutional weight.
- H8451 (תּוֹרָה): "law" / "Book of the Law" (22:8,11). T notes the probable Deuteronomic
  character without resolving the identification debate.
- H4687 (מִצְוָה): "commandments" throughout.
- H2708 (חֻקָּה): "statutes" throughout.
- H5715 (עֵדוּת): "testimonies" in 23:3.
- H3820/H3824 (לֵב/לֵבָב): "heart" throughout; 23:3,25 use the Shema vocabulary of Deut 6:5.
- H5315 (נֶפֶשׁ): "soul" in 23:3,25 (Shema context — all three Deut 6:5 terms must be
  preserved); "life" in survival/physical contexts.
- H3966 (מְאֹד): "might" in 23:3,25 — the third Shema term. 23:25 is unique in all of Kings:
  the only verse evaluating a king using all three terms of Deut 6:5. T surfaces this.
- H1116 (בָּמָה): "high places" throughout.
- H842 (אֲשֵׁרָה): "Asherah pole" (L/M) when the cult object is meant; "the Asherah" in T
  where the goddess-dimension is in view.
- H4432 (מֹלֶךְ): "Molech" throughout. The Topheth/Molech practices involve child sacrifice;
  T notes the theological inversion of covenant.
- H6453 (פֶּסַח): "Passover" throughout. 23:21-23: unprecedented since the judges — T notes
  this frames Josiah's reform as a new-exodus reconstitution of the covenant people.
- H4519 (מְנַשֶּׁה) / Manasseh: His reign (21:1-18) is explicitly the cause of Judah's exile
  (23:26-27; 24:3-4). Even Josiah's perfect reform cannot avert the judgment his generation
  stored up. T surfaces this as the theological spine of the final chapters of Kings.
- H639 (אַף) + H2740 (חֲרוֹן): "fierce burning anger" in L; "fierce anger" in M; "blazing
  wrath" in T (23:26).
- H1540 (גָּלָה): "exile/carried away into captivity" — the terminus Kings has been building
  toward. T: "carried off into exile."
- H5019 (נְבוּכַדְנֶאצַּר): "Nebuchadnezzar" — standard English form.
- H4983 (מַתַּנְיָה) / Zedekiah: name changed from Mattaniah = "gift of God" to Zedekiah =
  "righteousness of the LORD." T notes the bitter irony given his subsequent rebellion.
- Aspect decisions:
  - Waw-consecutive imperfects = narrative past throughout.
  - Hezekiah's prayers (19:15-19; 20:2-3) use cohortative/petition register — rendered
    as solemn direct address.
  - Isaiah's oracle (19:21-34) contains prophetic perfects and imperfects — T renders the
    assured future confidently: "he will," "he shall."
- OT intertextuality (woven into T tier throughout):
  - 19:15: Hezekiah's prayer echoes Solomon's dedicatory prayer (1 Kgs 8:23ff).
  - 19:25: "I formed it long ago, planned it from ancient days" echoes Second Isaiah
    (Isa 40:21-26, 46:9-11) — these texts share a theological tradition.
  - 19:30-31: The remnant language echoes Isa 10:20-23 and Amos 5:15.
  - 20:3: "walked before you in faithfulness" = the Davidic standard language.
  - 20:17-18: Isaiah's Babylonian exile prophecy in the Hezekiah narrative is deliberate
    narrative irony — the instrument of eventual destruction is introduced at the moment
    of deliverance.
  - 21:7-8: God's promise cited from 1 Kgs 9:3 (Solomon's dedication) — the standard
    Manasseh violates.
  - 22:8: The scroll discovery echoes Deut 31:24-26 (Moses' scroll beside the ark).
  - 23:21-23: The Passover frames Josiah's reform as recapitulating the conquest-generation
    covenant (Josh 5:10-11).
  - 23:25: Josiah = the only king evaluated by Moses' standard (Deut 6:5), not merely David's.
  - 24:13: "as the LORD had said" — explicit cross-reference to 20:17.
  - 24:20: Double causation — Zedekiah's rebellion and the LORD's anger operate simultaneously.
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
  "19": {
    "1": {
      "L": "And it came to pass, when king Hezekiah heard, that he rent his clothes and covered himself with sackcloth and went into the house of the LORD.",
      "M": "When King Hezekiah heard the report, he tore his clothes, wrapped himself in sackcloth, and went to the house of the LORD.",
      "T": "When Hezekiah heard Rabshakeh's speech, he tore his royal robes, put on sackcloth, and went straight to the LORD's temple."
    },
    "2": {
      "L": "And he sent Eliakim who was over the household, and Shebna the scribe, and the elders of the priests, covered with sackcloth, to Isaiah the prophet the son of Amoz.",
      "M": "He sent Eliakim the palace administrator, Shebna the secretary, and the senior priests, all dressed in sackcloth, to the prophet Isaiah son of Amoz.",
      "T": "He dispatched Eliakim the palace administrator, Shebna the state secretary, and the senior priests — all in sackcloth — to the prophet Isaiah ben Amoz."
    },
    "3": {
      "L": "And they said to him, Thus says Hezekiah: This day is a day of distress and rebuke and blasphemy, for the children have come to the birth and there is no strength to bring forth.",
      "M": "They said to him, 'This is what Hezekiah says: Today is a day of distress, rebuke, and disgrace. The children have come to the point of birth, but there is no strength to deliver them.'",
      "T": "Their message to Isaiah: 'Hezekiah says — today is a day of crisis, humiliation, and contempt for God. We are like a woman in labor with no strength left to push.'"
    },
    "4": {
      "L": "Perhaps the LORD your God will hear all the words of Rabshakeh, whom the king of Assyria his master has sent to reproach the living God, and will reprove the words which the LORD your God has heard; therefore lift up your prayer for the remnant that is left.",
      "M": "Perhaps the LORD your God will hear all the words of Rabshakeh, whom the king of Assyria his master sent to mock the living God, and will rebuke him for the words the LORD your God has heard. So offer a prayer for the surviving remnant.",
      "T": "It may be that the LORD your God has heard everything Rabshakeh said — the blasphemy his master, Assyria's king, sent him to deliver against the living God. Perhaps the LORD will act on what he has heard. Pray for the remnant still alive."
    },
    "5": {
      "L": "So the servants of king Hezekiah came to Isaiah.",
      "M": "King Hezekiah's servants came to Isaiah.",
      "T": "The delegation reached Isaiah."
    },
    "6": {
      "L": "And Isaiah said to them, Thus shall you say to your master, Thus says the LORD: Do not be afraid of the words which you have heard, with which the servants of the king of Assyria have blasphemed me.",
      "M": "Isaiah told them, 'Say this to your master: This is what the LORD says — Do not be afraid because of the words you have heard, the words with which the servants of the king of Assyria have blasphemed me.'",
      "T": "Isaiah answered them: 'Tell your master: This is the LORD's word — Do not be afraid. Those words Assyria's servants spoke against me — I have heard them.'"
    },
    "7": {
      "L": "Behold, I will send a blast upon him, and he shall hear a rumour and return to his own land, and I will cause him to fall by the sword in his own land.",
      "M": "I am going to put a spirit in him so that he will hear a report and return to his own land, where I will cause him to fall by the sword.",
      "T": "I will plant a foreboding in him. He will hear disturbing news and go back to his own country — and there I will bring him down by the sword."
    },
    "8": {
      "L": "So Rabshakeh returned and found the king of Assyria warring against Libnah, for he had heard that he had departed from Lachish.",
      "M": "Rabshakeh returned and found the king of Assyria fighting against Libnah, since he had heard that the king had left Lachish.",
      "T": "Rabshakeh went back and found the Assyrian king now attacking Libnah, having pulled out of Lachish."
    },
    "9": {
      "L": "And when he heard concerning Tirhakah king of Ethiopia, Behold, he is come out to fight against you, he sent messengers again to Hezekiah, saying,",
      "M": "When Sennacherib heard that Tirhakah king of Ethiopia had come out to fight against him, he sent messengers again to Hezekiah with this message:",
      "T": "Word reached him that Tirhakah king of Ethiopia was advancing to engage him. He responded by sending another round of messengers to Hezekiah:"
    },
    "10": {
      "L": "Thus shall you speak to Hezekiah king of Judah, saying, Do not let your God in whom you trust deceive you, saying, Jerusalem shall not be delivered into the hand of the king of Assyria.",
      "M": "Say this to Hezekiah king of Judah: Do not let your God, in whom you are trusting, deceive you by saying that Jerusalem will not be handed over to the king of Assyria.",
      "T": "Tell Hezekiah king of Judah: Don't let the God you trust talk you into thinking Jerusalem is safe from Assyria's king."
    },
    "11": {
      "L": "Behold, you have heard what the kings of Assyria have done to all lands, by destroying them utterly; and shall you be delivered?",
      "M": "You have heard what the kings of Assyria have done to all the countries — utterly destroying them. Do you think you can escape?",
      "T": "You've heard what Assyria's kings have done to every country in their path — they wiped them out. Why should you be any different?"
    },
    "12": {
      "L": "Have the gods of the nations delivered them, which my fathers have destroyed — Gozan and Haran and Rezeph and the children of Eden who were in Thelasar?",
      "M": "Did the gods of those nations deliver them — the nations my fathers destroyed: Gozan, Haran, Rezeph, and the people of Eden in Telassar?",
      "T": "Did the gods of Gozan, Haran, Rezeph, the Edenites of Telassar rescue any of them from my ancestors? Not one."
    },
    "13": {
      "L": "Where is the king of Hamath, and the king of Arpad, and the king of the city of Sepharvaim, of Hena, and Ivah?",
      "M": "Where are the kings of Hamath, Arpad, Sepharvaim, Hena, and Ivah?",
      "T": "Where are the kings of Hamath, Arpad, Sepharvaim, Hena, and Ivah now?"
    },
    "14": {
      "L": "And Hezekiah received the letter from the hand of the messengers and read it; and Hezekiah went up to the house of the LORD and spread it before the LORD.",
      "M": "Hezekiah received the letter from the messengers and read it. Then he went up to the house of the LORD and spread it out before the LORD.",
      "T": "Hezekiah took the letter, read it, then went to the LORD's temple and spread it open before God."
    },
    "15": {
      "L": "And Hezekiah prayed before the LORD and said, O LORD God of Israel, who dwells between the cherubim, you are the God, you alone, of all the kingdoms of the earth; you have made heaven and earth.",
      "M": "Hezekiah prayed to the LORD: 'LORD, God of Israel, enthroned between the cherubim, you alone are God over all the kingdoms of the earth; you have made heaven and earth.'",
      "T": "Then Hezekiah prayed: 'O LORD God of Israel, enthroned above the cherubim — you alone are God over every kingdom on earth. You made heaven and earth."
    },
    "16": {
      "L": "LORD, bow down your ear and hear; LORD, open your eyes and see; and hear the words of Sennacherib, which he has sent to reproach the living God.",
      "M": "Incline your ear, LORD, and hear; open your eyes, LORD, and see. Listen to all the words Sennacherib has sent to mock the living God.",
      "T": "Lean down and listen, LORD. Open your eyes and see. Hear every word Sennacherib has sent to insult the living God."
    },
    "17": {
      "L": "It is true, LORD, that the kings of Assyria have laid waste the nations and their lands,",
      "M": "It is true, LORD, that the kings of Assyria have destroyed these nations and their lands.",
      "T": "Yes, LORD — Assyria's kings have devastated nation after nation. That part is true."
    },
    "18": {
      "L": "and have cast their gods into the fire; for they were no gods, but the work of men's hands, wood and stone; therefore they have destroyed them.",
      "M": "They have thrown their gods into the fire — for those were no gods at all, merely human handiwork, wood and stone — and so they could destroy them.",
      "T": "They threw their gods into the fire, and why not? Those were no gods — just wood and stone carved by human hands, and fire burns them perfectly well."
    },
    "19": {
      "L": "Now therefore, O LORD our God, I beseech you, save us from his hand, that all the kingdoms of the earth may know that you, O LORD, are God alone.",
      "M": "Now, O LORD our God, deliver us from his hand, so that all the kingdoms of the earth may know that you, LORD, are God alone.'",
      "T": "So now, LORD our God, save us from Sennacherib's grip — so that every kingdom on earth will know that you and you alone are God.'"
    },
    "20": {
      "L": "Then Isaiah the son of Amoz sent to Hezekiah, saying, Thus says the LORD God of Israel, That which you have prayed to me against Sennacherib king of Assyria I have heard.",
      "M": "Then Isaiah son of Amoz sent word to Hezekiah: 'This is what the LORD, the God of Israel, says: I have heard your prayer about Sennacherib king of Assyria.'",
      "T": "Isaiah ben Amoz sent Hezekiah a message: 'The LORD God of Israel says — your prayer about Sennacherib has been answered.'"
    },
    "21": {
      "L": "This is the word that the LORD has spoken concerning him: The virgin daughter of Zion has despised you and mocked you; the daughter of Jerusalem has shaken her head at you.",
      "M": "This is the word the LORD has spoken against him: 'The virgin daughter of Zion despises and mocks you; the daughter of Jerusalem shakes her head behind you.'",
      "T": "And the LORD's oracle against Sennacherib: 'The virgin daughter of Zion scorns you and laughs in your face; Jerusalem's daughter tosses her head as you retreat."
    },
    "22": {
      "L": "Whom have you reproached and blasphemed? And against whom have you exalted your voice and lifted up your eyes on high? Against the Holy One of Israel.",
      "M": "Who is it you have mocked and blasphemed? Against whom have you raised your voice and lifted your eyes in pride? Against the Holy One of Israel.",
      "T": "You reproached and blasphemed — who exactly? You raised your voice and lifted your arrogant eyes — against whom? Against the Holy One of Israel."
    },
    "23": {
      "L": "By the hand of your messengers you have reproached the Lord, and you have said, With the multitude of my chariots I have ascended the height of the mountains, to the sides of Lebanon; and I will cut down its tall cedar trees and its choice fir trees, and I will enter the lodgings of its remotest border, the forest of its Carmel.",
      "M": "Through your messengers you have taunted the Lord, saying, 'With my many chariots I climbed to the top of the mountains, to the far reaches of Lebanon. I cut down its tallest cedars and finest pines. I reached its most distant lodging place, its densest forest.'",
      "T": "Through your royal dispatches you taunted the Lord himself — boasting: With my chariot legions I scaled the mountain peaks, the remotest heights of Lebanon. I felled its towering cedars and finest firs. I reached the furthest edge, the deepest forest."
    },
    "24": {
      "L": "I have dug and drunk foreign waters, and with the sole of my feet I have dried up all the rivers of the besieged places.",
      "M": "I dug wells and drank foreign water; with the soles of my feet I dried up all the streams of Egypt.",
      "T": "I sank wells and drank water in foreign lands; I marched through the streams of Egypt until they ran dry under my feet."
    },
    "25": {
      "L": "Have you not heard? Long ago I did it; from ancient times I formed it. Now I have brought it to pass, that you should make fenced cities into ruinous heaps.",
      "M": "Have you not heard? I determined long ago what I would do; from ancient times I planned it. Now I have brought it about — that you would reduce fortified cities to heaps of rubble.",
      "T": "Have you not heard? I settled all this long ages ago — I planned it from eternity. And now I have brought it to pass: you have been my instrument to turn fortified cities into rubble."
    },
    "26": {
      "L": "Therefore their inhabitants were of little strength, they were dismayed and confounded; they were as the grass of the field and the green herb, as the grass on the housetops and the corn blasted before it be grown up.",
      "M": "That is why their inhabitants had so little power — they were shattered and ashamed. They were like plants in a field, like tender green shoots, like grass on a rooftop, scorched before it can grow.",
      "T": "That is why their people had no real power — they collapsed and were put to shame. They were like field grass, like rooftop weeds, scorched by the east wind before they had a chance to grow."
    },
    "27": {
      "L": "But I know your sitting down and your going out and your coming in, and your raging against me.",
      "M": "But I know where you live and when you come and go, and I know your rage against me.",
      "T": "I know everything about you — where you live, your comings and goings, and this fury you've been directing at me."
    },
    "28": {
      "L": "Because your raging against me and your tumult has come up into my ears, therefore I will put my hook in your nose and my bridle in your lips, and I will turn you back by the way by which you came.",
      "M": "Because your fury against me and your arrogance have reached my ears, I will put my hook in your nose and my bridle in your mouth, and send you back the way you came.",
      "T": "Your raging fury against me and your boasting have reached my ears. So I will thread my hook through your nose and my bit between your lips — and drive you back the way you came, like a tamed beast.'"
    },
    "29": {
      "L": "And this shall be a sign to you: This year you shall eat such things as grow of themselves, and in the second year that which springs of the same; and in the third year sow and reap, and plant vineyards and eat the fruits thereof.",
      "M": "And this will be the sign for you: This year you will eat what grows on its own, and in the second year what springs from that. But in the third year sow and reap, plant vineyards and eat their fruit.",
      "T": "And here is your sign, Hezekiah: this year you eat whatever grows wild; next year, what springs up on its own. But the third year — sow and harvest, plant vineyards and eat them. Life returning to normal is itself the sign that God has acted."
    },
    "30": {
      "L": "And the remnant that is escaped of the house of Judah shall yet again take root downward and bear fruit upward.",
      "M": "The surviving remnant of the house of Judah will again take root downward and bear fruit upward.",
      "T": "The remnant of Judah that survives will send its roots deep into the ground and bear fruit toward heaven."
    },
    "31": {
      "L": "For out of Jerusalem shall go forth a remnant, and they that escape out of mount Zion: the zeal of the LORD of hosts shall do this.",
      "M": "For a remnant will go out from Jerusalem, and survivors from Mount Zion. The zeal of the LORD of hosts will accomplish this.",
      "T": "From Jerusalem and Mount Zion a remnant will go forth — a company of survivors. The fierce passion of the LORD of hosts will make it happen."
    },
    "32": {
      "L": "Therefore thus says the LORD concerning the king of Assyria: He shall not come into this city, nor shoot an arrow there, nor come before it with shield, nor cast a bank against it.",
      "M": "Therefore this is what the LORD says about the king of Assyria: He will not enter this city, shoot an arrow here, come before it with a shield, or build a siege ramp against it.",
      "T": "So the LORD's verdict on Assyria's king: he will not enter this city. Not a single arrow will fly into it; no soldier will approach it shield in hand; no siege ramp will be raised against it."
    },
    "33": {
      "L": "By the way that he came, by the same shall he return, and shall not come into this city, says the LORD.",
      "M": "He will go back the same way he came and will not enter this city, declares the LORD.",
      "T": "He will turn around and leave by the same road he came — and he will not set foot inside this city, declares the LORD."
    },
    "34": {
      "L": "For I will defend this city, to save it, for mine own sake, and for my servant David's sake.",
      "M": "I will defend this city and save it, for my own sake and for the sake of my servant David.",
      "T": "I will shield this city and deliver it — for my own honor, and for my servant David's sake."
    },
    "35": {
      "L": "And it came to pass that night that the angel of the LORD went out and struck a hundred and eighty-five thousand in the camp of the Assyrians; and when they arose early in the morning, behold, they were all dead corpses.",
      "M": "That night the angel of the LORD went out and struck down a hundred and eighty-five thousand men in the Assyrian camp. When people got up the next morning, all of them were dead bodies.",
      "T": "That night the angel of the LORD moved through the Assyrian camp and put to death a hundred and eighty-five thousand soldiers. When morning came, the entire camp was littered with corpses."
    },
    "36": {
      "L": "So Sennacherib king of Assyria departed, and went and returned, and dwelt at Nineveh.",
      "M": "So Sennacherib king of Assyria broke camp and withdrew and returned to Nineveh, where he stayed.",
      "T": "Sennacherib struck camp and retreated. He went home to Nineveh and stayed there."
    },
    "37": {
      "L": "And it came to pass, as he was worshipping in the house of Nisroch his god, that Adrammelech and Sharezer his sons smote him with the sword; and they escaped into the land of Ararat; and Esarhaddon his son reigned in his stead.",
      "M": "One day, while he was worshipping in the temple of his god Nisroch, his sons Adrammelech and Sharezer killed him with a sword and escaped to the land of Ararat. His son Esarhaddon became king in his place.",
      "T": "He met his end while worshipping in the temple of his god Nisroch: his own sons Adrammelech and Sharezer cut him down with a sword, then fled to Ararat. His son Esarhaddon took the throne."
    }
  },
  "20": {
    "1": {
      "L": "In those days was Hezekiah sick unto death. And Isaiah the prophet the son of Amoz came to him and said, Thus says the LORD, Set your house in order; for you shall die, and not live.",
      "M": "In those days Hezekiah became ill and was at the point of death. The prophet Isaiah son of Amoz came to him and said, 'This is what the LORD says: Put your house in order, for you are going to die; you will not recover.'",
      "T": "Around that time Hezekiah fell gravely ill. The prophet Isaiah ben Amoz came with this word: 'The LORD says — set your affairs in order. You are dying; you will not pull through.'"
    },
    "2": {
      "L": "Then he turned his face to the wall and prayed to the LORD, saying,",
      "M": "Hezekiah turned his face to the wall and prayed to the LORD,",
      "T": "Hezekiah turned his face to the wall and prayed:"
    },
    "3": {
      "L": "I beseech you, O LORD, remember now how I have walked before you in truth and with a perfect heart, and have done that which is good in your sight. And Hezekiah wept sore.",
      "M": "'Please, LORD, remember how I have walked before you faithfully and wholeheartedly, and have done what is good in your sight.' And Hezekiah wept bitterly.",
      "T": "'Please, LORD — remember. I have walked before you faithfully and with an undivided heart. I have done what was right in your eyes.' And he wept uncontrollably."
    },
    "4": {
      "L": "And it came to pass, afore Isaiah was gone out into the middle court, that the word of the LORD came to him, saying,",
      "M": "Before Isaiah had left the middle courtyard, the word of the LORD came to him:",
      "T": "Isaiah had barely left the inner courtyard when the LORD's word came to him:"
    },
    "5": {
      "L": "Turn again and tell Hezekiah the captain of my people, Thus says the LORD the God of David your father, I have heard your prayer, I have seen your tears; behold, I will heal you; on the third day you shall go up to the house of the LORD.",
      "M": "Go back and tell Hezekiah, the leader of my people: This is what the LORD, the God of your ancestor David, says — I have heard your prayer and seen your tears. I will heal you, and on the third day you will go up to the house of the LORD.",
      "T": "Go back to Hezekiah, leader of my people, and say: The LORD, the God of your ancestor David, says — I have heard your prayer. I have seen your tears. I am going to heal you. Three days from now you will be in my temple."
    },
    "6": {
      "L": "And I will add to your days fifteen years; and I will deliver you and this city out of the hand of the king of Assyria; and I will defend this city for mine own sake, and for my servant David's sake.",
      "M": "I will add fifteen years to your life. And I will rescue you and this city from the hand of the king of Assyria. I will defend this city for my own sake and for the sake of my servant David.",
      "T": "I am adding fifteen years to your life. I will deliver you and this city from the grip of the Assyrian king. I will defend this city — for my own honor and for my servant David's sake."
    },
    "7": {
      "L": "And Isaiah said, Take a lump of figs. And they took and laid it on the boil, and he recovered.",
      "M": "Then Isaiah said, 'Prepare a poultice of figs.' They prepared it and applied it to the boil, and he recovered.",
      "T": "Isaiah gave a practical instruction: get a fig compress. They made one, applied it to the infected sore, and Hezekiah got better."
    },
    "8": {
      "L": "And Hezekiah said to Isaiah, What shall be the sign that the LORD will heal me, and that I shall go up to the house of the LORD the third day?",
      "M": "Hezekiah asked Isaiah, 'What will be the sign that the LORD will heal me and that I will go up to the house of the LORD on the third day?'",
      "T": "Hezekiah asked Isaiah, 'What is the sign that the LORD will actually heal me, and that I'll be well enough for the temple in three days?'"
    },
    "9": {
      "L": "And Isaiah said, This shall be the sign to you from the LORD, that the LORD will do the thing that he has spoken: shall the shadow go forward ten degrees, or go back ten degrees?",
      "M": "Isaiah replied, 'This is the LORD's sign that he will do what he has promised: shall the shadow advance ten steps or retreat ten steps?'",
      "T": "Isaiah said, 'Here is the sign from the LORD that he will keep his word — shall the shadow on the sundial move forward ten steps, or move backward ten?'"
    },
    "10": {
      "L": "And Hezekiah answered, It is a light thing for the shadow to go down ten degrees; nay, but let the shadow return backward ten degrees.",
      "M": "Hezekiah answered, 'It is easy for the shadow to go forward ten steps; rather, let it go back ten steps.'",
      "T": "Hezekiah answered: 'Going forward ten steps would be easy enough. Let it go backward ten steps.'"
    },
    "11": {
      "L": "And Isaiah the prophet cried to the LORD, and he brought the shadow ten degrees backward, by which it had gone down in the dial of Ahaz.",
      "M": "Then the prophet Isaiah called out to the LORD, and the LORD made the shadow go back the ten steps it had descended on the stairway of Ahaz.",
      "T": "Isaiah called out to the LORD, and the LORD reversed the shadow ten steps on Ahaz's sundial — moving it back the full distance it had already descended."
    },
    "12": {
      "L": "At that time Berodachbaladan the son of Baladan, king of Babylon, sent letters and a present to Hezekiah; for he had heard that Hezekiah had been sick.",
      "M": "At that time Merodach-Baladan son of Baladan, king of Babylon, sent letters and a gift to Hezekiah, because he had heard that Hezekiah had been ill.",
      "T": "Around that time Merodach-Baladan son of Baladan, king of Babylon, sent envoys with letters and a gift to Hezekiah — he had heard about the king's illness."
    },
    "13": {
      "L": "And Hezekiah hearkened to them, and showed them all the house of his precious things, the silver and the gold and the spices and the precious ointment, and all the house of his armour, and all that was found in his treasures; there was nothing in his house, nor in all his dominion, that Hezekiah did not show them.",
      "M": "Hezekiah welcomed them and showed them his entire treasure house — the silver, the gold, the spices, the finest oils, his armory, and everything found among his treasures. There was nothing in his palace or in all his realm that Hezekiah did not show them.",
      "T": "Hezekiah received them warmly and opened his entire palace to them — every storeroom of silver and gold, every fragrant spice and fine oil, every weapon and piece of armor, every treasure he possessed. He held nothing back."
    },
    "14": {
      "L": "Then came Isaiah the prophet to king Hezekiah and said to him, What said these men? And from where came they to you? And Hezekiah said, They are come from a far country, even from Babylon.",
      "M": "Then the prophet Isaiah went to King Hezekiah and asked him, 'What did these men say? Where did they come from?' Hezekiah answered, 'They came from a distant land — from Babylon.'",
      "T": "The prophet Isaiah came to King Hezekiah with a pointed question: 'What did those men say to you? Where did they come from?' Hezekiah told him, 'They came from Babylon — a long way off.'"
    },
    "15": {
      "L": "And he said, What have they seen in your house? And Hezekiah answered, All the things that are in my house have they seen; there is nothing among my treasures that I have not shown them.",
      "M": "Isaiah asked, 'What did they see in your palace?' Hezekiah replied, 'They saw everything. There was nothing among my treasures that I did not show them.'",
      "T": "Isaiah pressed further: 'Everything in the palace?' Hezekiah confirmed: 'Everything. I showed them every last thing I own.'"
    },
    "16": {
      "L": "And Isaiah said to Hezekiah, Hear the word of the LORD.",
      "M": "Then Isaiah said to Hezekiah, 'Listen to the word of the LORD.'",
      "T": "Isaiah said quietly: 'Now hear what the LORD has to say.'"
    },
    "17": {
      "L": "Behold, the days come, that all that is in your house, and that which your fathers have laid up in store unto this day, shall be carried into Babylon: nothing shall be left, says the LORD.",
      "M": "'Look — days are coming when everything in your palace, and everything your ancestors have stored up to this day, will be carried off to Babylon. Not a thing will be left,' says the LORD.",
      "T": "'The days are coming when everything you just showed those visitors — and everything your ancestors stockpiled before you — will be hauled off to Babylon. The LORD says: nothing will be left.'"
    },
    "18": {
      "L": "And of your sons that shall issue from you, which you shall beget, shall they take away; and they shall be eunuchs in the palace of the king of Babylon.",
      "M": "'And some of your own descendants will be taken away and become eunuchs in the palace of the king of Babylon.'",
      "T": "'And some of your own sons — men born from your own body — will be taken away to serve as court eunuchs in the palace of Babylon's king.'"
    },
    "19": {
      "L": "Then said Hezekiah to Isaiah, Good is the word of the LORD which you have spoken. And he said, Is it not good, if peace and truth be in my days?",
      "M": "Hezekiah replied to Isaiah, 'The word of the LORD that you have spoken is good.' Then he said, 'Will there not be peace and security in my lifetime?'",
      "T": "Hezekiah responded to Isaiah: 'The LORD's word is good.' And he added — perhaps to himself as much as to Isaiah — 'At least there will be peace and security in my own lifetime.'"
    },
    "20": {
      "L": "And the rest of the acts of Hezekiah, and all his might, and how he made a pool and a conduit and brought water into the city, are they not written in the book of the chronicles of the kings of Judah?",
      "M": "The rest of the acts of Hezekiah, all his achievements, and how he built the pool and the tunnel and brought water into the city, are they not written in the book of the annals of the kings of Judah?",
      "T": "The rest of Hezekiah's history — his accomplishments, including the great tunnel he cut through the rock to bring water into the city — is recorded in the Book of the Annals of the Kings of Judah."
    },
    "21": {
      "L": "And Hezekiah slept with his fathers; and Manasseh his son reigned in his stead.",
      "M": "Hezekiah rested with his ancestors, and his son Manasseh became king in his place.",
      "T": "Hezekiah died and was buried with his ancestors. His son Manasseh succeeded him."
    }
  },
  "21": {
    "1": {
      "L": "Manasseh was twelve years old when he began to reign, and he reigned fifty and five years in Jerusalem; and his mother's name was Hephzibah.",
      "M": "Manasseh was twelve years old when he became king, and he reigned fifty-five years in Jerusalem. His mother's name was Hephzibah.",
      "T": "Manasseh was only twelve when he came to the throne. He reigned fifty-five years in Jerusalem — longer than any other king of Judah. His mother was Hephzibah."
    },
    "2": {
      "L": "And he did that which was evil in the sight of the LORD, after the abominations of the heathen whom the LORD cast out before the children of Israel.",
      "M": "He did what was evil in the sight of the LORD, following the detestable practices of the nations the LORD had driven out before the Israelites.",
      "T": "He did what was evil in the LORD's sight — deliberately copying the detestable practices of the nations God had expelled from the land to make room for Israel."
    },
    "3": {
      "L": "For he built up again the high places which Hezekiah his father had destroyed; and he reared up altars for Baal, and made a grove, as did Ahab king of Israel; and worshipped all the host of heaven, and served them.",
      "M": "He rebuilt the high places his father Hezekiah had demolished. He erected altars to Baal and made an Asherah pole, as Ahab king of Israel had done. He bowed down to all the starry hosts and served them.",
      "T": "He rebuilt every high place Hezekiah had torn down. He raised altars to Baal and set up an Asherah pole — replicating exactly what Ahab of Israel had done. He prostrated himself before the entire host of heaven and served them."
    },
    "4": {
      "L": "And he built altars in the house of the LORD, of which the LORD said, In Jerusalem will I put my name.",
      "M": "He built altars in the house of the LORD, of which the LORD had said, 'In Jerusalem I will put my Name.'",
      "T": "He even installed pagan altars inside the LORD's own temple — the very house where God had declared, 'Jerusalem is where I have placed my name.'"
    },
    "5": {
      "L": "And he built altars for all the host of heaven in the two courts of the house of the LORD.",
      "M": "In both courts of the house of the LORD he built altars to all the starry hosts.",
      "T": "In both courtyards of the LORD's temple he erected shrines to the stars."
    },
    "6": {
      "L": "And he made his son pass through the fire, and observed times, and used enchantments, and dealt with familiar spirits and wizards; he wrought much wickedness in the sight of the LORD, to provoke him to anger.",
      "M": "He sacrificed his son in the fire, practiced divination, sought omens, and consulted mediums and spiritists. He did much evil in the sight of the LORD, arousing his anger.",
      "T": "He burned his own son as a sacrifice. He practiced divination, consulted omens, communed with spirits and mediums. He went to extraordinary lengths to provoke the LORD's anger."
    },
    "7": {
      "L": "And he set a graven image of the grove that he had made in the house, of which the LORD said to David and to Solomon his son, In this house and in Jerusalem, which I have chosen out of all tribes of Israel, will I put my name for ever.",
      "M": "He placed the carved Asherah pole he had made inside the temple — the place about which the LORD had told David and his son Solomon: 'In this temple and in Jerusalem, which I have chosen from all the tribes of Israel, I will put my Name forever.'",
      "T": "He installed his carved Asherah idol inside the LORD's temple — the very house about which God had promised David and Solomon: 'In this house, in Jerusalem chosen above all other cities of Israel, I will put my name forever.'"
    },
    "8": {
      "L": "Neither will I make the feet of Israel move any more out of the land which I gave their fathers; only if they will observe to do according to all that I have commanded them, and according to all the law that my servant Moses commanded them.",
      "M": "I will no longer make Israel's feet wander from the land I gave their ancestors — only if they carefully obey everything I have commanded them, according to all the law my servant Moses commanded them.",
      "T": "God had said: I will not again uproot Israel from the land I gave their ancestors — on one condition: that they keep every command I have given them, all the law handed down through my servant Moses."
    },
    "9": {
      "L": "But they hearkened not: and Manasseh seduced them to do more evil than did the nations whom the LORD destroyed before the children of Israel.",
      "M": "But they did not listen. Manasseh led them astray, so that they did more evil than the nations the LORD had destroyed before the Israelites.",
      "T": "But they would not listen. Manasseh led Judah so far into wickedness that they out-sinned the very nations God had originally destroyed to give Israel the land."
    },
    "10": {
      "L": "And the LORD spake by his servants the prophets, saying,",
      "M": "The LORD said through his servants the prophets:",
      "T": "The LORD sent word through his prophets:"
    },
    "11": {
      "L": "Because Manasseh king of Judah has done these abominations, and has done wickedly above all that the Amorites did which were before him, and has made Judah also to sin with his idols,",
      "M": "'Because Manasseh king of Judah has committed these detestable acts and has done more evil than all the Amorites before him, and has led Judah into sin with his idols,'",
      "T": "'Because Manasseh king of Judah has done all these abominations — more wickedly than the Amorites who lived here before Israel — and has dragged Judah into the same idolatry with him,'"
    },
    "12": {
      "L": "Therefore thus says the LORD God of Israel, Behold, I am bringing such evil upon Jerusalem and Judah, that whosoever hears of it, both his ears shall tingle.",
      "M": "therefore this is what the LORD, the God of Israel, says: I am going to bring such disaster on Jerusalem and Judah that it will make the ears of everyone who hears about it tingle.",
      "T": "'this is the LORD God of Israel's verdict: I am bringing a catastrophe on Jerusalem and Judah so severe that everyone who hears of it will feel it like a physical shock.'"
    },
    "13": {
      "L": "And I will stretch over Jerusalem the line of Samaria, and the plummet of the house of Ahab; and I will wipe Jerusalem as a man wipes a dish, wiping it and turning it upside down.",
      "M": "I will stretch over Jerusalem the measuring line used against Samaria and the plumb line used against the house of Ahab; I will wipe Jerusalem as one wipes a dish, wiping it and turning it upside down.",
      "T": "'I will apply to Jerusalem the same measuring line I used to condemn Samaria, the same plumb line that brought down Ahab's dynasty. I will wipe Jerusalem clean like a man scrubbing a bowl — and set it upside down to drain.'"
    },
    "14": {
      "L": "And I will forsake the remnant of my inheritance, and deliver them into the hand of their enemies; and they shall become a prey and a spoil to all their enemies;",
      "M": "I will abandon the remnant of my inheritance and hand them over to their enemies. They will be plundered and looted by all their enemies,",
      "T": "'I will abandon the last of my inheritance — give them over to their enemies to be plundered and robbed by all who hate them.'"
    },
    "15": {
      "L": "Because they have done that which was evil in my sight, and have provoked me to anger, since the day their fathers came forth out of Egypt, even unto this day.",
      "M": "because they have done what is evil in my sight and have provoked my anger from the day their ancestors came out of Egypt until this day.",
      "T": "'Because from the day their ancestors left Egypt right up to now, they have been doing what is evil in my sight and provoking my anger without stopping.'"
    },
    "16": {
      "L": "Moreover Manasseh shed innocent blood very much, till he had filled Jerusalem from one end to another; beside his sin wherewith he made Judah to sin, in doing that which was evil in the sight of the LORD.",
      "M": "Moreover, Manasseh shed so much innocent blood that he filled Jerusalem from end to end — in addition to the sin he led Judah into by doing what was evil in the sight of the LORD.",
      "T": "Beyond everything else, Manasseh shed innocent blood in Jerusalem on a massive scale — so much that it ran from one side of the city to the other. This was in addition to the sin he dragged Judah into."
    },
    "17": {
      "L": "Now the rest of the acts of Manasseh, and all that he did, and his sin that he sinned, are they not written in the book of the chronicles of the kings of Judah?",
      "M": "As for the rest of Manasseh's acts and everything he did, including the sin he committed, are they not written in the book of the annals of the kings of Judah?",
      "T": "The rest of Manasseh's history, including every detail of his crimes, is recorded in the Book of the Annals of the Kings of Judah."
    },
    "18": {
      "L": "And Manasseh slept with his fathers, and was buried in the garden of his own house, in the garden of Uzza; and Amon his son reigned in his stead.",
      "M": "Manasseh rested with his ancestors and was buried in the garden of his palace, in the garden of Uzza. His son Amon became king in his place.",
      "T": "Manasseh died and was buried in the garden of his own palace — the garden of Uzza. His son Amon became king."
    },
    "19": {
      "L": "Amon was twenty and two years old when he began to reign, and he reigned two years in Jerusalem; and his mother's name was Meshullemeth the daughter of Haruz of Jotbah.",
      "M": "Amon was twenty-two years old when he became king, and he reigned two years in Jerusalem. His mother's name was Meshullemeth daughter of Haruz from Jotbah.",
      "T": "Amon was twenty-two when he came to the throne. He reigned for two years. His mother was Meshullemeth daughter of Haruz of Jotbah."
    },
    "20": {
      "L": "And he did that which was evil in the sight of the LORD, as his father Manasseh did.",
      "M": "He did what was evil in the sight of the LORD, as his father Manasseh had done.",
      "T": "He did what was evil in the LORD's sight, just as his father Manasseh had done."
    },
    "21": {
      "L": "And he walked in all the way that his father walked in, and served the idols that his father served, and worshipped them.",
      "M": "He walked in the same path as his father, worshipping the same idols his father had worshipped and bowing down to them.",
      "T": "He followed his father's path completely — serving the same idols, bowing before the same shrines."
    },
    "22": {
      "L": "And he forsook the LORD God of his fathers, and walked not in the way of the LORD.",
      "M": "He abandoned the LORD, the God of his ancestors, and did not walk in the way of the LORD.",
      "T": "He turned his back on the LORD God of his fathers and refused to walk in God's ways."
    },
    "23": {
      "L": "And the servants of Amon conspired against him, and slew the king in his own house.",
      "M": "Amon's officials conspired against him and assassinated the king in his own palace.",
      "T": "Amon's own officials plotted against him and murdered him in the palace."
    },
    "24": {
      "L": "And the people of the land slew all them that had conspired against king Amon; and the people of the land made Josiah his son king in his stead.",
      "M": "Then the people of the land killed all who had conspired against King Amon, and they made his son Josiah king in his place.",
      "T": "The people of the land executed everyone who had taken part in the plot, then put Josiah, Amon's son, on the throne."
    },
    "25": {
      "L": "Now the rest of the acts of Amon which he did, are they not written in the book of the chronicles of the kings of Judah?",
      "M": "As for the rest of Amon's acts and what he did, are they not written in the book of the annals of the kings of Judah?",
      "T": "The rest of Amon's history is recorded in the Book of the Annals of the Kings of Judah."
    },
    "26": {
      "L": "And he was buried in his sepulchre in the garden of Uzza; and Josiah his son reigned in his stead.",
      "M": "He was buried in his tomb in the garden of Uzza, and his son Josiah became king in his place.",
      "T": "He was buried in the garden of Uzza. Josiah his son succeeded him."
    }
  },
  "22": {
    "1": {
      "L": "Josiah was eight years old when he began to reign, and he reigned thirty and one years in Jerusalem; and his mother's name was Jedidah the daughter of Adaiah of Boscath.",
      "M": "Josiah was eight years old when he became king, and he reigned thirty-one years in Jerusalem. His mother's name was Jedidah daughter of Adaiah from Bozkath.",
      "T": "Josiah was eight years old when he became king. He reigned thirty-one years in Jerusalem. His mother was Jedidah daughter of Adaiah of Bozkath."
    },
    "2": {
      "L": "And he did that which was right in the sight of the LORD, and walked in all the way of David his father, and turned not aside to the right hand or to the left.",
      "M": "He did what was right in the sight of the LORD and followed completely the way of his ancestor David, not turning aside to the right or to the left.",
      "T": "He did what was right in the LORD's eyes. He followed his ancestor David's path without deviation — neither to the right nor to the left."
    },
    "3": {
      "L": "And it came to pass in the eighteenth year of king Josiah, that the king sent Shaphan the son of Azaliah the son of Meshullam the scribe to the house of the LORD, saying,",
      "M": "In the eighteenth year of King Josiah, the king sent Shaphan son of Azaliah, son of Meshullam the secretary, to the house of the LORD with this instruction:",
      "T": "When Josiah had been king for eighteen years, he sent the state secretary Shaphan son of Azaliah, son of Meshullam, to the LORD's temple with these orders:"
    },
    "4": {
      "L": "Go up to Hilkiah the high priest, that he may sum the silver which is brought into the house of the LORD, which the keepers of the door have gathered of the people.",
      "M": "'Go to the high priest Hilkiah and have him count the money that has been brought into the house of the LORD, which the gatekeepers have collected from the people.'",
      "T": "'Go to the high priest Hilkiah and have him count and account for all the silver that has been brought into the LORD's temple — what the gatekeepers have collected from the worshippers.'"
    },
    "5": {
      "L": "And let them deliver it into the hand of the doers of the work, that have the oversight of the house of the LORD; and let them give it to the doers of the work which is in the house of the LORD, to repair the breaches of the house.",
      "M": "Have them entrust it to the supervisors of the work on the house of the LORD, and let them pay the workers who repair the damage to the house.",
      "T": "'Have the money paid out to the contractors overseeing the temple work, so they can pay the workmen repairing the building.'"
    },
    "6": {
      "L": "Unto carpenters, and builders, and masons, and to buy timber and hewn stone to repair the house.",
      "M": "This includes carpenters, builders, and stonemasons, and to purchase timber and dressed stone for the repairs.",
      "T": "'Pay the carpenters, builders, and stonemasons, and buy whatever timber and cut stone the work requires.'"
    },
    "7": {
      "L": "Howbeit there was no reckoning made with them of the money that was delivered into their hand, because they dealt faithfully.",
      "M": "They were not required to keep accounts for the money entrusted to them, because they were acting honestly.",
      "T": "No detailed audit was required — these workmen had proven themselves completely trustworthy."
    },
    "8": {
      "L": "And Hilkiah the high priest said to Shaphan the scribe, I have found the book of the law in the house of the LORD. And Hilkiah gave the book to Shaphan, and he read it.",
      "M": "The high priest Hilkiah said to Shaphan the secretary, 'I have found the Book of the Law in the house of the LORD.' Hilkiah gave the book to Shaphan, who read it.",
      "T": "Then Hilkiah the high priest told Shaphan the secretary: 'I have found the Book of the Law in the LORD's temple.' He handed it to Shaphan, who read through it."
    },
    "9": {
      "L": "And Shaphan the scribe came to the king, and brought the king word again, and said, Your servants have gathered the money that was found in the house, and have delivered it into the hand of them that do the work, that have the oversight of the house of the LORD.",
      "M": "Shaphan the secretary went to the king and reported: 'Your servants have paid out the money that was in the house of the LORD. They have entrusted it to the workers who have oversight of the LORD's temple.'",
      "T": "Shaphan reported back to the king: 'Your officials have distributed the silver from the temple to the contractors managing the repair work.'"
    },
    "10": {
      "L": "And Shaphan the scribe showed the king, saying, Hilkiah the priest has delivered me a book. And Shaphan read it before the king.",
      "M": "Then Shaphan the secretary informed the king, 'The priest Hilkiah has given me a book.' And Shaphan read it aloud to the king.",
      "T": "Then Shaphan added: 'There's something else — the priest Hilkiah gave me a scroll.' And he read it aloud in the king's presence."
    },
    "11": {
      "L": "And it came to pass, when the king had heard the words of the book of the law, that he rent his clothes.",
      "M": "When the king heard the words of the Book of the Law, he tore his clothes.",
      "T": "The moment the king heard the words of the Book of the Law read aloud, he tore his robes."
    },
    "12": {
      "L": "And the king commanded Hilkiah the priest, and Ahikam the son of Shaphan, and Achbor the son of Michaiah, and Shaphan the scribe, and Asahiah a servant of the king's, saying,",
      "M": "He commanded the priest Hilkiah, Ahikam son of Shaphan, Achbor son of Micaiah, the secretary Shaphan, and the king's attendant Asaiah:",
      "T": "He gave orders to Hilkiah the priest, Ahikam son of Shaphan, Achbor son of Micaiah, the secretary Shaphan, and his attendant Asaiah:"
    },
    "13": {
      "L": "Go, inquire of the LORD for me, and for the people, and for all Judah, concerning the words of this book that is found; for great is the wrath of the LORD that is kindled against us, because our fathers have not hearkened to the words of this book, to do according unto all that which is written concerning us.",
      "M": "'Go and inquire of the LORD for me, for the people, and for all Judah about what is written in this book that has been found. The LORD's anger is burning fiercely against us because our ancestors did not obey the words of this book and do everything written there concerning us.'",
      "T": "'Go and seek the LORD's word — for me, for the people, for all Judah — about what is written in this scroll. The LORD's anger is blazing against us. Our ancestors did not obey a word of this book, and everything written here applies directly to us.'"
    },
    "14": {
      "L": "So Hilkiah the priest, and Ahikam, and Achbor, and Shaphan, and Asahiah, went to Huldah the prophetess, the wife of Shallum the son of Tikvah, the son of Harhas, keeper of the wardrobe; now she dwelt in Jerusalem in the college; and they communed with her.",
      "M": "So Hilkiah the priest, Ahikam, Achbor, Shaphan, and Asaiah went to consult the prophetess Huldah, wife of Shallum son of Tikvah, son of Harhas, keeper of the wardrobe. She lived in Jerusalem in the Second District, and they consulted her.",
      "T": "The delegation went to Huldah the prophetess, wife of Shallum son of Tikvah, son of Harhas, who kept the royal wardrobe. She lived in the Second Quarter of Jerusalem. They brought her the question."
    },
    "15": {
      "L": "And she said to them, Thus says the LORD God of Israel, Tell the man that sent you to me,",
      "M": "She said to them, 'This is what the LORD, the God of Israel, says: Tell the man who sent you to me,'",
      "T": "Her response: 'The LORD God of Israel says — tell the man who sent you this:'"
    },
    "16": {
      "L": "Thus says the LORD, Behold, I will bring evil upon this place, and upon the inhabitants thereof, even all the words of the book which the king of Judah has read.",
      "M": "'This is what the LORD says: I am going to bring disaster on this place and its people, according to everything written in the book the king of Judah has read.'",
      "T": "'I am bringing catastrophe on this place and its people — every word written in that scroll that Judah's king just heard read.'"
    },
    "17": {
      "L": "Because they have forsaken me, and have burned incense to other gods, that they might provoke me to anger with all the works of their hands; therefore my wrath shall be kindled against this place, and shall not be quenched.",
      "M": "Because they have abandoned me and burned incense to other gods, provoking my anger through everything they have done, my wrath will burn against this place and will not be quenched.",
      "T": "'Because they abandoned me and offered incense to foreign gods — deliberately provoking me with everything their hands have made — my wrath will be ignited against this place and it will not go out.'"
    },
    "18": {
      "L": "But to the king of Judah who sent you to inquire of the LORD, thus shall you say to him, Thus says the LORD God of Israel, As touching the words which you have heard;",
      "M": "As for the king of Judah who sent you to inquire of the LORD, say this to him: This is what the LORD, the God of Israel, says concerning the words you have heard:",
      "T": "'But to the king who sent you — here is what the LORD God of Israel says about what he has just heard:'"
    },
    "19": {
      "L": "Because your heart was tender, and you have humbled yourself before the LORD, when you heard what I spake against this place, and against the inhabitants thereof, that they should become a desolation and a curse, and have rent your clothes, and wept before me; I also have heard you, says the LORD.",
      "M": "Because your heart was responsive and you humbled yourself before the LORD when you heard what I spoke against this place and its people — that they would become a curse and a ruin — and because you tore your robes and wept before me, I have also heard you, declares the LORD.",
      "T": "'Because your heart was broken and you humbled yourself before the LORD the moment you heard what I had decreed against this place and its people — desolation and a curse — and because you tore your clothes and wept before me, I have heard you. This is the LORD's word.'"
    },
    "20": {
      "L": "Behold therefore, I will gather you to your fathers, and you shall be gathered into your grave in peace; and your eyes shall not see all the evil which I will bring upon this place. And they brought the king word again.",
      "M": "Therefore I will gather you to your ancestors, and you will be buried in peace. Your eyes will not see all the disaster I am going to bring on this place.' They brought the report back to the king.",
      "T": "'Therefore I will gather you to your ancestors. You will go to your grave in peace — your own eyes will not see the calamity I am bringing on this place.' They carried this word back to the king."
    }
  },
  "23": {
    "1": {
      "L": "And the king sent, and they gathered to him all the elders of Judah and of Jerusalem.",
      "M": "Then the king summoned all the elders of Judah and Jerusalem, and they assembled before him.",
      "T": "The king sent word and gathered every elder of Judah and Jerusalem."
    },
    "2": {
      "L": "And the king went up into the house of the LORD, and all the men of Judah and all the inhabitants of Jerusalem with him, and the priests, and the prophets, and all the people, both small and great; and he read in their ears all the words of the book of the covenant which was found in the house of the LORD.",
      "M": "The king went up to the house of the LORD with all the men of Judah and all the inhabitants of Jerusalem — the priests, the prophets, and all the people, young and old alike. He read aloud all the words of the Book of the Covenant that had been found in the house of the LORD.",
      "T": "The king went to the LORD's temple, and with him went every man of Judah and every resident of Jerusalem — priests, prophets, and all the people from the youngest to the greatest. He read the entire Book of the Covenant aloud so everyone could hear."
    },
    "3": {
      "L": "And the king stood by a pillar, and made a covenant before the LORD, to walk after the LORD, and to keep his commandments and his testimonies and his statutes with all their heart and all their soul, to perform the words of this covenant that were written in this book. And all the people stood to the covenant.",
      "M": "The king stood beside the pillar and renewed the covenant before the LORD — to follow the LORD and keep his commands, statutes, and decrees with all his heart and all his soul, to carry out the terms of the covenant written in this book. And all the people pledged themselves to the covenant.",
      "T": "The king stood at his post beside the pillar and made a solemn covenant before the LORD: to follow the LORD, to keep his commands, his testimonies, and his statutes — with heart, soul, and everything he had — and to enact every word of this covenant scroll. The entire assembly pledged themselves to it as well."
    },
    "4": {
      "L": "And the king commanded Hilkiah the high priest, and the priests of the second order, and the keepers of the door, to bring forth out of the temple of the LORD all the vessels that were made for Baal, and for the grove, and for all the host of heaven; and he burned them without Jerusalem in the fields of Kidron, and carried the ashes of them unto Bethel.",
      "M": "The king ordered the high priest Hilkiah, the priests of the second rank, and the doorkeepers to remove from the LORD's temple all the articles made for Baal, for Asherah, and for all the starry hosts. He burned them outside Jerusalem in the fields of the Kidron Valley and carried their ashes to Bethel.",
      "T": "The king instructed Hilkiah the high priest, the second-tier priests, and the gatekeepers to clear every object from the LORD's temple that was associated with Baal, Asherah, or the starry hosts. He burned them all in the Kidron Valley outside Jerusalem and hauled their ashes to Bethel."
    },
    "5": {
      "L": "And he put down the idolatrous priests, whom the kings of Judah had ordained to burn incense in the high places in the cities of Judah, and in the places round about Jerusalem; them also that burned incense to Baal, to the sun, and to the moon, and to the planets, and to all the host of heaven.",
      "M": "He did away with the idolatrous priests the kings of Judah had appointed to burn incense at the high places in the towns of Judah and the surrounding area of Jerusalem — those who burned incense to Baal, to the sun and moon, to the constellations and all the starry hosts.",
      "T": "He removed from service the priests the previous kings of Judah had installed to burn offerings at the high places throughout Judah's towns and the suburbs around Jerusalem — all who had been offering incense to Baal, the sun, the moon, the constellations, and every heavenly body."
    },
    "6": {
      "L": "And he brought out the grove from the house of the LORD, without Jerusalem, unto the brook Kidron, and burned it at the brook Kidron, and stamped it small to powder, and cast the powder thereof upon the graves of the children of the people.",
      "M": "He took the Asherah pole from the house of the LORD to the Kidron Valley outside Jerusalem, burned it there, ground it to powder, and scattered the powder over the graves of the common people.",
      "T": "He dragged the Asherah pole out of the LORD's temple, burned it to ash in the Kidron Valley, ground the ash to powder, and scattered it over the common burial ground."
    },
    "7": {
      "L": "And he brake down the houses of the sodomites, that were by the house of the LORD, where the women wove hangings for the grove.",
      "M": "He demolished the quarters of the male shrine prostitutes that were in the house of the LORD, the quarters where women did weaving for the Asherah.",
      "T": "He tore down the shrine-rooms alongside the LORD's temple where male cult prostitutes lived and where women had been weaving sacred hangings for the Asherah."
    },
    "8": {
      "L": "And he brought all the priests out of the cities of Judah, and defiled the high places where the priests had burned incense, from Geba to Beersheba, and brake down the high places of the gates that were in the entering in of the gate of Joshua the governor of the city, which were on a man's left hand at the gate of the city.",
      "M": "He brought all the priests from the cities of Judah, and desecrated the high places, from Geba to Beersheba, where they had burned incense. He demolished the shrines at the gates that stood at the entrance of the gate of Joshua the city governor — the one on the left as you entered the city gate.",
      "T": "He brought all the priests of Judah's towns to Jerusalem and desecrated the high places where they had been burning offerings, stretching from Geba in the north to Beersheba in the south. He also demolished the gateway shrines at the entrance of the city governor Joshua's gate — the shrines on the left side as you came in."
    },
    "9": {
      "L": "Nevertheless the priests of the high places came not up to the altar of the LORD in Jerusalem, but they did eat of the unleavened bread among their brethren.",
      "M": "The priests from the high places did not serve at the altar of the LORD in Jerusalem, but they ate unleavened bread with their fellow priests.",
      "T": "Those priests were not permitted to serve at the LORD's altar in Jerusalem, but they were allowed to eat the unleavened bread among their fellow priests."
    },
    "10": {
      "L": "And he defiled Topheth, which is in the valley of the children of Hinnom, that no man might make his son or his daughter to pass through the fire to Molech.",
      "M": "He desecrated Topheth, which is in the Valley of Ben-Hinnom, so that no one could use it to sacrifice his son or daughter in the fire to Molech.",
      "T": "He desecrated the Topheth shrine in the Valley of Ben-Hinnom, making it permanently unfit for use — so that no one could ever again burn their child as a sacrifice to Molech. Child sacrifice is the ultimate inversion of covenant: the covenant God gives life; Molech demands it."
    },
    "11": {
      "L": "And he took away the horses that the kings of Judah had given to the sun, at the entering in of the house of the LORD, by the chamber of Nathanmelech the chamberlain, which was in the suburbs; and burned the chariots of the sun with fire.",
      "M": "He removed from the entrance of the house of the LORD the horses that the kings of Judah had dedicated to the sun. These were near the room of the official Nathan-Melek in the court. He then burned the chariot of the sun.",
      "T": "He removed the horses the kings of Judah had dedicated to the sun god — they stood at the entrance of the LORD's temple, near the chamber of the court official Nathan-Melek. He burned the sun-chariots."
    },
    "12": {
      "L": "And the altars that were on the top of the upper chamber of Ahaz, which the kings of Judah had made, and the altars which Manasseh had made in the two courts of the house of the LORD, did the king beat down, and brake them down from thence, and cast the dust of them into the brook Kidron.",
      "M": "He pulled down the altars the kings of Judah had built on the roof of the upper room of Ahaz, as well as the altars Manasseh had built in the two courts of the LORD's house. He smashed them, removed the rubble, and threw the dust into the Kidron Valley.",
      "T": "He demolished the altars that Judah's kings had built on the roof of Ahaz's upper chamber, and the altars Manasseh had set up in both temple courts. He smashed them all, ground them to dust, and threw the debris into the Kidron."
    },
    "13": {
      "L": "And the high places that were before Jerusalem, which were on the right hand of the mount of corruption, which Solomon the king of Israel had builded for Ashtoreth the abomination of the Zidonians, and for Chemosh the abomination of the Moabites, and for Milcom the abomination of the children of Ammon, did the king defile.",
      "M": "The king desecrated the high places that were east of Jerusalem on the south side of the Mount of Corruption — the shrines Solomon king of Israel had built for Ashtoreth the detestable goddess of the Sidonians, for Chemosh the detestable god of Moab, and for Milcom the detestable god of the Ammonites.",
      "T": "He desecrated the hilltop shrines east of Jerusalem, on the south slope of the Mount of Corruption — the very shrines Solomon had built for the gods of his foreign wives: Ashtoreth of the Sidonians, Chemosh of Moab, and Milcom of Ammon. Three abominations, standing for three centuries."
    },
    "14": {
      "L": "And he brake in pieces the images, and cut down the groves, and filled their places with the bones of men.",
      "M": "He smashed the sacred stones and cut down the Asherah poles and covered the sites with human bones.",
      "T": "He shattered the standing stones, cut down the Asherah poles, and desecrated the sites by strewing them with human bones — making the ground permanently unclean under Levitical law."
    },
    "15": {
      "L": "Moreover the altar that was at Bethel, and the high place which Jeroboam the son of Nebat, who made Israel to sin, had made, both that altar and the high place he brake down, and burned the high place, and stamped it small to powder, and burned the grove.",
      "M": "Even the altar at Bethel, the high place made by Jeroboam son of Nebat, who had caused Israel to sin — even that altar and high place he demolished. He burned the high place and ground it to powder, and burned the Asherah pole.",
      "T": "Even the altar at Bethel — the one Jeroboam son of Nebat had built at the very beginning of the northern kingdom's apostasy — Josiah pulled down and demolished. He burned the high place to ash, ground everything to powder, and burned the Asherah pole as well."
    },
    "16": {
      "L": "And as Josiah turned himself, he spied the sepulchres that were there in the mount, and sent, and took the bones out of the sepulchres, and burned them upon the altar, and polluted it, according to the word of the LORD which the man of God proclaimed, who proclaimed these words.",
      "M": "As Josiah looked around, he noticed the tombs there on the hillside. He sent and had the bones taken from them and burned on the altar to defile it, in keeping with the word of the LORD proclaimed by the man of God who had foretold these things.",
      "T": "As he surveyed the site, Josiah spotted the ancient graves on the hillside. He had the bones dug up and burned on the altar — deliberately defiling it, exactly as the man of God from Judah had prophesied three centuries before."
    },
    "17": {
      "L": "Then he said, What title is that that I see? And the men of the city told him, It is the sepulchre of the man of God, which came from Judah, and proclaimed these things that you have done against the altar of Bethel.",
      "M": "Josiah asked, 'What is that monument I see?' The people of the city told him, 'It is the tomb of the man of God who came from Judah and announced the things you have done against this altar.'",
      "T": "Josiah pointed to a nearby grave marker: 'What tomb is that?' The townspeople told him: 'That is the tomb of the man of God who came from Judah and predicted everything you have just done to this altar.'"
    },
    "18": {
      "L": "And he said, Let him alone; let no man move his bones. So they let his bones alone, with the bones of the prophet that came out of Samaria.",
      "M": "'Leave him alone,' he said. 'Let no one disturb his bones.' So they left his bones undisturbed, together with the bones of the prophet who had come from Samaria.",
      "T": "'Leave it,' the king said. 'Don't disturb his bones.' So they left his bones untouched, along with the bones of the Samarian prophet buried nearby."
    },
    "19": {
      "L": "And all the houses also of the high places that were in the cities of Samaria, which the kings of Israel had made to provoke the LORD to anger, Josiah took away, and did to them according to all the acts that he had done in Bethel.",
      "M": "Josiah removed all the shrines at the high places that the kings of Israel had built in the towns of Samaria, which had provoked the LORD to anger. He treated them exactly as he had treated the shrine at Bethel.",
      "T": "Josiah extended his reform into the former northern kingdom: every high-place shrine the kings of Israel had built in Samaria's towns — every one that had fueled the LORD's anger — he dismantled and treated the same way he had treated Bethel."
    },
    "20": {
      "L": "And he slew all the priests of the high places that were there upon the altars, and burned men's bones upon them, and returned to Jerusalem.",
      "M": "He slaughtered all the priests of the high places on their own altars and burned human bones on them. Then he returned to Jerusalem.",
      "T": "He executed every priest of those high places on their own altars and burned human bones on them to desecrate them permanently. Then he returned to Jerusalem."
    },
    "21": {
      "L": "And the king commanded all the people, saying, Keep the passover unto the LORD your God, as it is written in the book of this covenant.",
      "M": "The king commanded all the people, 'Celebrate the Passover to the LORD your God, as it is written in this Book of the Covenant.'",
      "T": "The king gave the entire nation a single command: 'Observe the Passover for the LORD your God, exactly as this covenant scroll directs.'"
    },
    "22": {
      "L": "Surely there was not holden such a passover from the days of the judges that judged Israel, nor in all the days of the kings of Israel, nor of the kings of Judah.",
      "M": "Not since the days of the judges who led Israel, nor throughout the entire period of the kings of Israel and the kings of Judah, had any such Passover been observed.",
      "T": "No Passover like this one had been celebrated since the days of the judges — not under any of Israel's kings or Judah's kings had anything like this been done."
    },
    "23": {
      "L": "But in the eighteenth year of king Josiah, wherein this passover was holden to the LORD in Jerusalem.",
      "M": "It was only in the eighteenth year of King Josiah that this Passover was celebrated to the LORD in Jerusalem.",
      "T": "It took the eighteenth year of Josiah's reign to see this Passover properly observed in Jerusalem — the first of its kind in living memory, a national act of covenant renewal as sweeping as the reforms that preceded it."
    },
    "24": {
      "L": "Moreover the workers with familiar spirits, and the wizards, and the images, and the idols, and all the abominations that were spied in the land of Judah and in Jerusalem, did Josiah put away, that he might perform the words of the law which were written in the book that Hilkiah the priest found in the house of the LORD.",
      "M": "Furthermore, Josiah removed the mediums and spiritists, the household gods, the idols, and all the other detestable things seen in Judah and Jerusalem. He did this in order to fulfill the requirements of the law written in the book that the priest Hilkiah had found in the house of the LORD.",
      "T": "Josiah also purged from Judah and Jerusalem every medium, every spiritist, every household idol and sacred image, every abomination that could be found — carrying out to the letter everything written in the law scroll that Hilkiah had discovered in the LORD's temple."
    },
    "25": {
      "L": "And like unto him was there no king before him, that turned to the LORD with all his heart, and with all his soul, and with all his might, according to all the law of Moses; neither after him arose there any like him.",
      "M": "Neither before nor after Josiah was there a king like him who turned to the LORD with all his heart and with all his soul and with all his strength, in accordance with all the Law of Moses.",
      "T": "No king before or after Josiah matched him. He turned back to the LORD with his whole heart, his whole soul, his whole strength. He is the only king in all of Kings evaluated in the exact language of the Shema (Deut 6:5) — heart, soul, and might. He kept the law of Moses without compromise."
    },
    "26": {
      "L": "Notwithstanding the LORD turned not from the fierceness of his great wrath, wherewith his anger was kindled against Judah, because of all the provocations that Manasseh had provoked him withal.",
      "M": "Nevertheless, the LORD did not turn away from the fierce burning of his great anger, which blazed against Judah because of all the provocations with which Manasseh had provoked him.",
      "T": "And yet — the LORD's blazing wrath did not cool. The fury that Manasseh's generation had accumulated against Judah could not be undone, not even by Josiah's perfect faithfulness. The book of Kings names this starkly: one generation's unfaithfulness can store up a judgment that outlasts even the most righteous of successors."
    },
    "27": {
      "L": "And the LORD said, I will remove Judah also out of my sight, as I have removed Israel, and will cast off this city Jerusalem which I have chosen, and the house of which I said, My name shall be there.",
      "M": "So the LORD said, 'I will remove Judah from my sight as I removed Israel. I will reject Jerusalem, the city I chose, and this temple, about which I said, My Name shall be there.'",
      "T": "The LORD's verdict was fixed: 'I will push Judah away from my presence just as I pushed Israel away. I will reject Jerusalem — the city I chose. I will abandon the temple about which I said, My name shall live there.'"
    },
    "28": {
      "L": "Now the rest of the acts of Josiah, and all that he did, are they not written in the book of the chronicles of the kings of Judah?",
      "M": "As for the rest of the acts of Josiah and all that he did, are they not written in the book of the annals of the kings of Judah?",
      "T": "The rest of Josiah's history and all his accomplishments are recorded in the Book of the Annals of the Kings of Judah."
    },
    "29": {
      "L": "In his days Pharaohnechoh king of Egypt went up against the king of Assyria to the river Euphrates; and king Josiah went against him; and he slew him at Megiddo, when he had seen him.",
      "M": "While he was king, Pharaoh Necho king of Egypt marched up to the Euphrates River to help the king of Assyria. King Josiah set out to confront him, but at Megiddo, Necho met him and killed him.",
      "T": "During Josiah's reign, Pharaoh Necho of Egypt marched north toward the Euphrates to support Assyria. Josiah went out to intercept him — and at Megiddo, the moment Necho saw him, he killed him. The greatest reforming king of Judah died on a foreign battlefield, and the text offers no explanation."
    },
    "30": {
      "L": "And his servants carried him in a chariot dead from Megiddo, and brought him to Jerusalem, and buried him in his own sepulchre. And the people of the land took Jehoahaz the son of Josiah, and anointed him, and made him king in his father's stead.",
      "M": "His servants brought his body by chariot from Megiddo to Jerusalem and buried him in his own tomb. The people of the land took Jehoahaz son of Josiah, anointed him, and made him king in his father's place.",
      "T": "His servants transported his body from Megiddo to Jerusalem by chariot and buried him in his own tomb. The people of the land then took Jehoahaz, Josiah's son, anointed him, and made him king in his father's place."
    },
    "31": {
      "L": "Jehoahaz was twenty and three years old when he began to reign; and he reigned three months in Jerusalem; and his mother's name was Hamutal the daughter of Jeremiah of Libnah.",
      "M": "Jehoahaz was twenty-three years old when he became king, and he reigned three months in Jerusalem. His mother's name was Hamutal daughter of Jeremiah from Libnah.",
      "T": "Jehoahaz was twenty-three when he became king. He lasted only three months. His mother was Hamutal daughter of Jeremiah of Libnah."
    },
    "32": {
      "L": "And he did that which was evil in the sight of the LORD, according to all that his fathers had done.",
      "M": "He did what was evil in the sight of the LORD, just as his predecessors had done.",
      "T": "He did what was evil in the LORD's sight, following the same pattern as his fathers."
    },
    "33": {
      "L": "And Pharaohnechoh put him in bands at Riblah in the land of Hamath, that he might not reign in Jerusalem; and put the land to a tribute of an hundred talents of silver, and a talent of gold.",
      "M": "Pharaoh Necho imprisoned him at Riblah in the land of Hamath so that he could not reign in Jerusalem, and he imposed a tribute on Judah of a hundred talents of silver and a talent of gold.",
      "T": "Pharaoh Necho had him arrested at Riblah in Hamath — removing him from power in Jerusalem — and levied a punishing tribute on the land: a hundred talents of silver and one talent of gold."
    },
    "34": {
      "L": "And Pharaohnechoh made Eliakim the son of Josiah king in the room of Josiah his father, and turned his name to Jehoiakim, and took Jehoahaz away; and he came to Egypt, and died there.",
      "M": "Pharaoh Necho made Eliakim son of Josiah king in place of his father Josiah and changed Eliakim's name to Jehoiakim. He took Jehoahaz to Egypt, where he died.",
      "T": "Pharaoh Necho installed Eliakim, another of Josiah's sons, on the throne — renaming him Jehoiakim, signaling his vassalage. Jehoahaz was taken to Egypt, where he died."
    },
    "35": {
      "L": "And Jehoiakim gave the silver and the gold to Pharaoh; but he taxed the land to give the money according to the commandment of Pharaoh; he exacted the silver and the gold of the people of the land, of every one according to his taxation, to give it unto Pharaohnechoh.",
      "M": "Jehoiakim paid Pharaoh the required silver and gold. To raise it, he taxed the land and required each person to pay according to his assessment of their means.",
      "T": "Jehoiakim raised the tribute for Pharaoh by taxing the people — assessing each man his individual portion and passing it all up the chain to Necho."
    },
    "36": {
      "L": "Jehoiakim was twenty and five years old when he began to reign; and he reigned eleven years in Jerusalem; and his mother's name was Zebudah the daughter of Pedaiah of Rumah.",
      "M": "Jehoiakim was twenty-five years old when he became king, and he reigned eleven years in Jerusalem. His mother's name was Zebidah daughter of Pedaiah from Rumah.",
      "T": "Jehoiakim was twenty-five when he took the throne. He reigned eleven years. His mother was Zebidah daughter of Pedaiah of Rumah."
    },
    "37": {
      "L": "And he did that which was evil in the sight of the LORD, according to all that his fathers had done.",
      "M": "He did what was evil in the sight of the LORD, just as his predecessors had done.",
      "T": "He did what was evil in the LORD's sight, following the same pattern as his fathers."
    }
  },
  "24": {
    "1": {
      "L": "In his days Nebuchadnezzar king of Babylon came up, and Jehoiakim became his servant three years; then he turned and rebelled against him.",
      "M": "During Jehoiakim's reign, Nebuchadnezzar king of Babylon invaded the land. Jehoiakim became his vassal for three years, but then he turned against him and rebelled.",
      "T": "During Jehoiakim's reign, Nebuchadnezzar king of Babylon came and imposed his rule. Jehoiakim submitted as his vassal for three years — then turned and rebelled."
    },
    "2": {
      "L": "And the LORD sent against him bands of the Chaldees, and bands of the Syrians, and bands of the Moabites, and bands of the children of Ammon, and sent them against Judah to destroy it, according to the word of the LORD, which he spake by his servants the prophets.",
      "M": "The LORD sent Babylonian, Aramean, Moabite, and Ammonite raiding parties against Jehoiakim. He sent them against Judah to destroy it, in accordance with the word of the LORD proclaimed through his servants the prophets.",
      "T": "The LORD sent Chaldean, Aramean, Moabite, and Ammonite raiding parties against Jehoiakim — launching them against Judah to destroy it. This was the LORD's own doing, the fulfillment of what he had spoken through his servants the prophets."
    },
    "3": {
      "L": "Surely at the commandment of the LORD came this upon Judah, to remove them out of his sight, for the sins of Manasseh, according to all that he did.",
      "M": "Certainly this came upon Judah according to the LORD's command, to remove them from his sight because of the sins of Manasseh and all that he had done.",
      "T": "It was the LORD's own decree that brought this on Judah — to drive them out of his sight. The cause: Manasseh's sins and everything he had done."
    },
    "4": {
      "L": "And also for the innocent blood that he shed; for he filled Jerusalem with innocent blood; which the LORD would not pardon.",
      "M": "This included the innocent blood he had shed — he had filled Jerusalem with innocent blood — and the LORD was not willing to forgive.",
      "T": "And the bloodshed — Manasseh had saturated Jerusalem with innocent blood. This the LORD would not forgive."
    },
    "5": {
      "L": "Now the rest of the acts of Jehoiakim, and all that he did, are they not written in the book of the chronicles of the kings of Judah?",
      "M": "As for the rest of the acts of Jehoiakim and all that he did, are they not written in the book of the annals of the kings of Judah?",
      "T": "The rest of Jehoiakim's history is recorded in the Book of the Annals of the Kings of Judah."
    },
    "6": {
      "L": "So Jehoiakim slept with his fathers; and Jehoiachin his son reigned in his stead.",
      "M": "Jehoiakim rested with his ancestors, and his son Jehoiachin became king in his place.",
      "T": "Jehoiakim died and Jehoiachin his son succeeded him."
    },
    "7": {
      "L": "And the king of Egypt came not again any more out of his land; for the king of Babylon had taken from the river of Egypt unto the river Euphrates all that pertained to the king of Egypt.",
      "M": "The king of Egypt did not come out of his land again, because the king of Babylon had taken everything belonging to the king of Egypt, from the Wadi of Egypt to the Euphrates River.",
      "T": "Egypt never invaded again after that — Nebuchadnezzar had stripped Pharaoh of every territory from the border stream of Egypt all the way to the Euphrates."
    },
    "8": {
      "L": "Jehoiachin was eighteen years old when he began to reign, and he reigned in Jerusalem three months; and his mother's name was Nehushta the daughter of Elnathan of Jerusalem.",
      "M": "Jehoiachin was eighteen years old when he became king, and he reigned in Jerusalem three months. His mother's name was Nehushta daughter of Elnathan from Jerusalem.",
      "T": "Jehoiachin was eighteen when he became king. He reigned three months. His mother was Nehushta daughter of Elnathan of Jerusalem."
    },
    "9": {
      "L": "And he did that which was evil in the sight of the LORD, according to all that his father had done.",
      "M": "He did what was evil in the sight of the LORD, just as his father had done.",
      "T": "He did what was evil in the LORD's sight, following his father's pattern."
    },
    "10": {
      "L": "At that time the servants of Nebuchadnezzar king of Babylon came up against Jerusalem, and the city was besieged.",
      "M": "At that time the servants of Nebuchadnezzar king of Babylon marched against Jerusalem and laid siege to it.",
      "T": "At that time Nebuchadnezzar's army came up and put Jerusalem under siege."
    },
    "11": {
      "L": "And Nebuchadnezzar king of Babylon came against the city, and his servants did besiege it.",
      "M": "Nebuchadnezzar king of Babylon came to the city while his troops were besieging it.",
      "T": "Nebuchadnezzar came in person while his army maintained the siege."
    },
    "12": {
      "L": "And Jehoiachin the king of Judah went out to the king of Babylon, he, and his mother, and his servants, and his princes, and his officers; and the king of Babylon took him in the eighth year of his reign.",
      "M": "Jehoiachin king of Judah, his mother, his attendants, his nobles, and his officials all surrendered to the king of Babylon. The king of Babylon took him prisoner in the eighth year of his own reign.",
      "T": "Jehoiachin king of Judah surrendered — he went out to Nebuchadnezzar with his mother, his household, his nobles, and his officials. Nebuchadnezzar took him prisoner in the eighth year of his own reign."
    },
    "13": {
      "L": "And he carried out thence all the treasures of the house of the LORD, and the treasures of the king's house, and cut in pieces all the vessels of gold which Solomon king of Israel had made in the temple of the LORD, as the LORD had said.",
      "M": "He carried off all the treasures of the house of the LORD and the treasures of the royal palace, and cut up all the gold objects that Solomon king of Israel had made for the LORD's temple — just as the LORD had predicted.",
      "T": "He stripped the temple of everything — every treasure from the LORD's house and the royal palace. He smashed and removed all the gold articles Solomon had made for the temple. The LORD had said this would happen (20:17). It happened."
    },
    "14": {
      "L": "And he carried away all Jerusalem, and all the princes, and all the mighty men of valour, even ten thousand captives, and all the craftsmen and smiths; none remained, save the poorest sort of the people of the land.",
      "M": "He carried into exile all Jerusalem — all the officers and all the fighting men, ten thousand captives, and all the craftsmen and metalworkers. Only the poorest people of the land were left.",
      "T": "He deported all of Jerusalem — every official, every fighting man, ten thousand prisoners in all, every craftsman and metalworker. Only the poorest people of the land were left behind."
    },
    "15": {
      "L": "And he carried away Jehoiachin to Babylon, and the king's mother, and the king's wives, and his officers, and the mighty of the land, those carried he into captivity from Jerusalem to Babylon.",
      "M": "He carried Jehoiachin into exile to Babylon. He also took the king's mother, the king's wives, his court officials, and the leading men of the land — all of them deported from Jerusalem to Babylon.",
      "T": "Jehoiachin himself was taken to Babylon, along with his mother, his wives, his court officials, and the leading men of the land — all carried from Jerusalem to Babylon."
    },
    "16": {
      "L": "And all the men of might, even seven thousand, and craftsmen and smiths a thousand, all that were strong and apt for war, even them the king of Babylon brought captive to Babylon.",
      "M": "The king of Babylon also brought to Babylon seven thousand fighting men who were strong and fit for military service, and a thousand craftsmen and metalworkers.",
      "T": "Seven thousand soldiers — all able-bodied fighters — and a thousand craftsmen and metalworkers: Nebuchadnezzar took them all to Babylon, stripping Judah of its military and skilled workforce in a single blow."
    },
    "17": {
      "L": "And the king of Babylon made Mattaniah his father's brother king in his stead, and changed his name to Zedekiah.",
      "M": "The king of Babylon installed Mattaniah, Jehoiachin's uncle, as king in his place, changing his name to Zedekiah.",
      "T": "Nebuchadnezzar installed Mattaniah, Jehoiachin's uncle, as a puppet king, and renamed him Zedekiah — 'righteousness of the LORD,' an irony the narrative will make plain."
    },
    "18": {
      "L": "Zedekiah was twenty and one years old when he began to reign, and he reigned eleven years in Jerusalem; and his mother's name was Hamutal the daughter of Jeremiah of Libnah.",
      "M": "Zedekiah was twenty-one years old when he became king, and he reigned eleven years in Jerusalem. His mother's name was Hamutal daughter of Jeremiah from Libnah.",
      "T": "Zedekiah was twenty-one when he came to the throne. He reigned eleven years. His mother was Hamutal daughter of Jeremiah of Libnah."
    },
    "19": {
      "L": "And he did that which was evil in the sight of the LORD, according to all that Jehoiakim had done.",
      "M": "He did what was evil in the sight of the LORD, just as Jehoiakim had done.",
      "T": "He did what was evil in the LORD's sight, following the same pattern as Jehoiakim."
    },
    "20": {
      "L": "For through the anger of the LORD it came to pass in Jerusalem and Judah, until he had cast them out from his presence, that Zedekiah rebelled against the king of Babylon.",
      "M": "It was because of the LORD's anger that all this happened to Jerusalem and Judah, until he finally thrust them from his presence. And Zedekiah rebelled against the king of Babylon.",
      "T": "The LORD's anger was the ultimate cause of everything that came on Jerusalem and Judah — the force driving events until God finally expelled them from his presence. And then Zedekiah rebelled against Babylon, and the end began."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, '2kings')
        merge_tier(existing, KINGS2, tier_key)
        save(tier_dir, '2kings', existing)
    print('2 Kings 19–24 written.')

if __name__ == '__main__':
    main()
