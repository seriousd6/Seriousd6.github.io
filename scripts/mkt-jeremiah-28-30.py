"""
MKT Jeremiah chapters 28–30 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-jeremiah-28-30.py

Translation decisions (consistent with mkt-jeremiah-1-3.py through mkt-jeremiah-23-24.py):

- H3068 (יהוה): "LORD" in L/M throughout; "Yahweh" in T where the personal-name force is
  significant — oracle delivery, divine address, confrontation scenes. Narrative connector
  formulas ("declares the LORD") use "Yahweh" in T for immediacy and directness.

- H6635 (צְבָאוֹת, ṣĕbāʾôt, "hosts/armies"): "hosts" in L/M; "of hosts" retained in T
  because the military overtone — divine Commander of heaven's armies — is precisely the
  point in 29:17 (sending sword/famine/plague) and 30:8 (breaking the yoke).

- H4133 (מוֹטָה, môṭâ, "yoke bar"): ch.28 — the central sign. Hananiah breaks the wooden
  yoke bar Jeremiah had been wearing (Jer 27); Jeremiah returns the prophetic message that
  wooden yokes become iron ones. Rendered "yoke" throughout — simple and accurate.

- H4805 (מֶרִי, mĕrî, "rebellion/defiance"): 28:16 and 29:32 — "preached/taught rebellion
  against the LORD." The charge is serious: inciting Israel to reject Yahweh's word. Both
  false prophets (Hananiah and Shemaiah) earn the same verdict.

- H7965 (שָׁלוֹם, šālôm, "peace/welfare/shalom"): 29:7 — "seek the peace of the city."
  In L/M rendered "welfare" (to distinguish from mere cessation of war). In T: "shalom"
  is used once to surface the full range — prosperity, wholeness, communal flourishing.
  29:11 — H7965 recurs in "thoughts of peace" — "welfare" in L/M, "flourishing" in T.

- H8615 (תִּקְוָה, tiqwâ, "hope/future"): 29:11 — the famous "future and a hope." The word
  means "expectation/cord/thread" — something to hold on to. Rendered "future and a hope"
  in L/M; T: "a real future, a genuine hope" — surfacing that this is concrete, not vague.

- H4284 (מַחֲשָׁבוֹת, maḥšābôt, "plans/thoughts/intentions"): 29:11 — "the thoughts/plans
  I think toward you." The word spans mental design and actual plan. L: "plans I plan";
  M: "plans I have"; T: "what I have planned" — keeping the intentional, goal-directed sense.

- H3820 (לֵב, lēb, "heart"): 30:24 — "the intentions/purposes of his heart." Heart in Hebrew
  is the seat of will and resolve, not merely feeling. Rendered "heart" in L/M; T: "intention"
  to clarify the volitional force.

- H6869 (צָרָה, ṣārâ, "trouble/distress/anguish"): 30:7 — "time of Jacob's trouble." The noun
  denotes acute distress — a tight, pinched situation with no exit. Rendered "distress" in L,
  "anguish" in M, "agony" in T to honor the escalating register of the passage.

- H4148 (מוּסָר, mûsār, "discipline/correction"): 30:11 — "I will discipline/correct you
  in justice." The word can mean training through discipline or corrective punishment. Here
  Yahweh's judgment on Israel is purposive correction, not obliteration. L: "discipline";
  M/T: "discipline" / "correct you" — retaining the punitive but redemptive nuance.

- H7307 (רוּחַ): not prominent in chs. 28–30; not at issue.

- H2617 (חֶסֶד): not prominent in chs. 28–30; not at issue.

Structural and textual notes:

- Ch. 28 — The Hananiah Confrontation (dated 4th year of Zedekiah, 594 BCE).
  Hananiah's oracle is a point-by-point inversion of Jeremiah's Babylon theology (chs. 27–28):
  where Jeremiah said submit to Babylon for 70 years, Hananiah says resistance wins in 2 years.
  Jeremiah's initial response is remarkable: he says amen — "would that it were so!" (v.6).
  This is not sarcasm but genuine pastoral hope — Jeremiah does not want judgment. Only after
  the break does he receive the word that wood becomes iron.

- Ch. 28:9 — The test of the peace-prophet. This verse articulates a biblical epistemology of
  prophecy: true prophets of doom are verifiable (judgment either comes or it doesn't); true
  prophets of peace must wait for fulfillment. In the short run, false peace-prophecy is safer
  for the prophet. The passage implicitly criticizes any who choose comfort over truth.

- Ch. 28:13 — "Yokes of wood... yokes of iron": by breaking the symbolic yoke, Hananiah has
  not removed the burden but hardened it. The act of false prophecy strengthens the very
  captivity it claims to undo.

- Ch. 29 — The Letter to the Exiles (dated after 597 BCE deportation of Jeconiah).
  This is one of the most pastorally and theologically important letters in the OT. Its key
  moves: (1) stop waiting for a short exile; (2) invest fully in Babylon's welfare; (3) the
  promise of 70 years and return; (4) the famous vv. 11-13; (5) judgment on those who stayed.
  The counter-intuitive theology: exile is not divine abandonment — Yahweh is in Babylon too.

- Ch. 29:7 — "Seek the shalom of the city" is startling theology: the exiles are told to
  pray for their captor city. Cooperation with Babylon is the will of Yahweh. Political quietism
  is sacred duty — Yahweh controls Nebuchadnezzar too.

- Ch. 29:11 — One of the most-cited verses in Jeremiah. Its context is crucial: it is addressed
  to exiles in Babylon, not a generic promise of personal prosperity. The "plans" are communal
  and eschatological — the return from exile after 70 years. Appropriating v.11 as a personal
  life-verse requires holding that whole-community context.

- Ch. 29:16-19 — The dark counterpart to vv. 4-14: while the exiles receive promises, those
  who remained in Jerusalem under Zedekiah or fled to Egypt receive sword/famine/plague. The
  theological reversal is complete: exile is salvation, staying is catastrophe.

- Ch. 30 — The Book of Consolation begins (chs. 30-33 form Jeremiah's "Little Book of Hope").
  Ch. 30 opens the collection: general announcement of restoration, the description of Jacob's
  distress, and Yahweh's promise to heal and return. The tone shifts from all prior Jeremiah —
  this is the hinge of the book.

- Ch. 30:7 — "The time of Jacob's trouble" is the phrase later referenced in eschatological
  contexts (Dan 12:1; Matt 24; Rev 7). In context it describes the pre-return distress — not
  a single endpoint but a process of pressure from which Yahweh saves.

- Ch. 30:9 — "David their king" — a messianic reference to a Davidic ruler whom Yahweh will
  "raise up." This echoes 23:5 (the righteous Branch) and is part of the restoration package:
  political, spiritual, and dynastic renewal together.

- Ch. 30:21 — "Who would dare of himself to approach me?" — this is temple theology: access
  to Yahweh requires divine initiation, not human presumption. The coming leader will be granted
  direct access — a priestly-royal figure who mediates between people and God.

- Ch. 30:22 — The covenant formula ("you shall be my people; I will be your God") — the
  culminating promise of the consolation passage. First articulated in Gen 17:7-8 / Exod 6:7;
  here it marks the consummation of the restoration. Carries into Jer 31:33; Ezek 36:28;
  Rev 21:3.

- Ch. 30:23-24 — The storm oracle recapitulates 23:19-20 almost verbatim. The restoration
  promise and the judgment warning are two sides of one coin: Yahweh's anger against the wicked
  nations will execute the rescue of Israel.

OT intertextuality:
- 28:9 — The prophet-test echoes Deut 18:21-22.
- 29:5-7 — "Build, plant, pray" mirrors the restoration imagery of Isa 65:21-22.
- 29:11-14 — The seek-and-find language anticipates Deut 4:29-30 (seeking Yahweh in exile).
- 30:9 — "David their king" echoes Hos 3:5; Ezek 34:23-24; 37:24-25.
- 30:22 — Covenant formula: Gen 17:7-8; Exod 6:7; Lev 26:12; Jer 31:33; Rev 21:3.
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


JEREMIAH = {
  "28": {
    "1": {
      "L": "And it came to pass in that year, in the beginning of the reign of Zedekiah king of Judah, in the fourth year, in the fifth month, that Hananiah the son of Azzur the prophet, who was of Gibeon, spoke to me in the house of the LORD, in the presence of the priests and of all the people, saying:",
      "M": "In that same year, at the beginning of the reign of Zedekiah king of Judah — the fourth year, the fifth month — the prophet Hananiah son of Azzur from Gibeon spoke to me in the house of the LORD in the presence of the priests and all the people. He said:",
      "T": "It happened in the fourth year of Zedekiah's reign over Judah, in the fifth month, that Hananiah son of Azzur, a prophet from Gibeon, confronted me in Yahweh's temple. The priests and the whole gathered people were listening when he spoke:"
    },
    "2": {
      "L": "Thus says the LORD of hosts, the God of Israel: I have broken the yoke of the king of Babylon.",
      "M": "Thus says the LORD of hosts, the God of Israel: I have broken the yoke of the king of Babylon.",
      "T": "This is what Yahweh of hosts, the God of Israel, declares: I have shattered the yoke of Babylon's king."
    },
    "3": {
      "L": "Within two full years I will bring back to this place all the vessels of the LORD's house that Nebuchadnezzar king of Babylon took from this place and carried to Babylon.",
      "M": "Within two years I will bring back to this place all the vessels of the LORD's temple that Nebuchadnezzar king of Babylon removed from this place and carried to Babylon.",
      "T": "Within two full years I will return every vessel of Yahweh's temple to this very place — everything Nebuchadnezzar took and hauled off to Babylon."
    },
    "4": {
      "L": "And Jeconiah the son of Jehoiakim, king of Judah, and all the captives of Judah who went to Babylon, I will bring back to this place, says the LORD; for I will break the yoke of the king of Babylon.",
      "M": "And Jeconiah son of Jehoiakim, king of Judah, and all the exiles of Judah who went to Babylon — I will bring them all back to this place, declares the LORD, for I will break the yoke of the king of Babylon.",
      "T": "And Jeconiah son of Jehoiakim, Judah's king, along with all the Judahite exiles in Babylon — I will bring them all home. The yoke of Babylon's king will be broken. Yahweh's word."
    },
    "5": {
      "L": "Then the prophet Jeremiah said to the prophet Hananiah in the presence of the priests and in the presence of all the people who stood in the house of the LORD,",
      "M": "Then the prophet Jeremiah said to the prophet Hananiah in the presence of the priests and all the people who were standing in the house of the LORD:",
      "T": "Then Jeremiah, prophet that he was, answered Hananiah, prophet that he was — in front of the priests and the whole gathered assembly, right there in Yahweh's temple:"
    },
    "6": {
      "L": "Amen! May the LORD do so! May the LORD perform your words that you have prophesied, to bring back the vessels of the LORD's house and all the captives from Babylon to this place.",
      "M": "Amen! May the LORD do so! May the LORD fulfill the words you have prophesied, and bring back the vessels of the LORD's temple and all the exiles from Babylon to this place.",
      "T": "Yes — amen! Would that Yahweh would do exactly what you say! Would that he fulfilled every word you have prophesied and brought the temple vessels and all the exiles home from Babylon!"
    },
    "7": {
      "L": "Nevertheless, hear now this word that I speak in your ears and in the ears of all the people:",
      "M": "But hear now this word that I am speaking in your hearing and in the hearing of all the people:",
      "T": "But hear me out — there is a word I must speak in your ears and in the ears of every person standing here:"
    },
    "8": {
      "L": "The prophets who were before me and before you from of old prophesied against many lands and great kingdoms, of war and of evil and of pestilence.",
      "M": "The prophets who preceded you and me from ancient times prophesied war, disaster, and plague against many lands and great kingdoms.",
      "T": "Every prophet who came before us — every authentic voice from antiquity — brought oracles of war, disaster, and plague against nations and kingdoms. That is the default register of true prophecy."
    },
    "9": {
      "L": "The prophet who prophesies peace — when the word of that prophet comes to pass, the prophet will be known as one whom the LORD has truly sent.",
      "M": "As for the prophet who prophesies peace: only when his word comes true will it be known that the LORD has truly sent him.",
      "T": "A prophet who promises peace? Fine — but let's wait and see. When his word actually comes to pass, that is when we will know that Yahweh genuinely sent him."
    },
    "10": {
      "L": "Then Hananiah the prophet took the yoke from off the neck of the prophet Jeremiah and broke it.",
      "M": "Then the prophet Hananiah took the yoke bar from the neck of the prophet Jeremiah and broke it.",
      "T": "At that, Hananiah the prophet reached over, lifted the yoke from Jeremiah's neck, and broke it in pieces."
    },
    "11": {
      "L": "And Hananiah spoke in the presence of all the people, saying: Thus says the LORD; Just so will I break the yoke of Nebuchadnezzar king of Babylon from the neck of all nations within two full years. And the prophet Jeremiah went his way.",
      "M": "And Hananiah spoke in the presence of all the people: 'Thus says the LORD: This is how I will break the yoke of Nebuchadnezzar king of Babylon from the neck of all nations — within two years!' And the prophet Jeremiah walked away.",
      "T": "Hananiah proclaimed to the whole crowd: 'This is what Yahweh says: This is exactly how I will break Nebuchadnezzar's yoke from the neck of every nation — within two full years!' And Jeremiah simply turned and walked away."
    },
    "12": {
      "L": "Then the word of the LORD came to Jeremiah the prophet, after Hananiah the prophet had broken the yoke from off the neck of the prophet Jeremiah, saying:",
      "M": "After the prophet Hananiah had broken the yoke from the neck of the prophet Jeremiah, the word of the LORD came to Jeremiah:",
      "T": "After Hananiah had broken the yoke bar from Jeremiah's neck, Yahweh's word came to Jeremiah:"
    },
    "13": {
      "L": "Go, speak to Hananiah, saying: Thus says the LORD: You have broken yokes of wood, but in their place you shall make yokes of iron.",
      "M": "Go and tell Hananiah: Thus says the LORD: You have broken yokes of wood, but you have made yokes of iron to replace them.",
      "T": "Go back and tell Hananiah: This is what Yahweh says — You smashed wooden yokes, but you have forged iron yokes to take their place."
    },
    "14": {
      "L": "For thus says the LORD of hosts, the God of Israel: I have placed a yoke of iron on the neck of all these nations that they may serve Nebuchadnezzar king of Babylon; and they shall serve him; I have also given him the beasts of the field.",
      "M": "For thus says the LORD of hosts, the God of Israel: I have placed a yoke of iron on the neck of all these nations so that they may serve Nebuchadnezzar king of Babylon; and serve him they will. I have even given him dominion over the wild animals.",
      "T": "This is what Yahweh of hosts, the God of Israel, says: I have fitted an iron yoke to the neck of all these nations — they will serve Nebuchadnezzar king of Babylon, and they have no choice. I have even placed the wild animals under his hand."
    },
    "15": {
      "L": "And the prophet Jeremiah said to the prophet Hananiah: Hear now, Hananiah! The LORD has not sent you, but you are making this people trust in a lie.",
      "M": "Then the prophet Jeremiah said to the prophet Hananiah: Listen, Hananiah! The LORD has not sent you, and you are making this people put their trust in a lie.",
      "T": "So Jeremiah said to Hananiah directly: Listen carefully, Hananiah. Yahweh never sent you. What you are doing is making this people stake their lives on a lie."
    },
    "16": {
      "L": "Therefore thus says the LORD: Behold, I am about to send you away from the face of the earth; this year you shall die, because you have preached rebellion against the LORD.",
      "M": "Therefore thus says the LORD: I am about to remove you from the face of the earth. This very year you will die, because you have preached rebellion against the LORD.",
      "T": "So this is what Yahweh says: I am removing you from the land of the living. You will die this year, because you spoke in Yahweh's name to incite rebellion against him."
    },
    "17": {
      "L": "So Hananiah the prophet died in that year, in the seventh month.",
      "M": "And the prophet Hananiah died that same year, in the seventh month.",
      "T": "Hananiah the prophet died that very year — in the seventh month."
    }
  },
  "29": {
    "1": {
      "L": "Now these are the words of the letter that the prophet Jeremiah sent from Jerusalem to the residue of the elders among the captives, and to the priests, and to the prophets, and to all the people, whom Nebuchadnezzar had carried away captive from Jerusalem to Babylon;",
      "M": "These are the words of the letter that the prophet Jeremiah sent from Jerusalem to the surviving elders among the exiles, to the priests, the prophets, and all the people whom Nebuchadnezzar had deported from Jerusalem to Babylon.",
      "T": "This is the letter that Jeremiah the prophet sent from Jerusalem to the elders still living among the exiles — to the priests, the prophets, and all the people Nebuchadnezzar had carried off from Jerusalem to Babylon."
    },
    "2": {
      "L": "(After Jeconiah the king and the queen mother and the court officials, the princes of Judah and Jerusalem, and the craftsmen and the smiths had departed from Jerusalem)",
      "M": "This was after King Jeconiah, the queen mother, the court officials, the princes of Judah and Jerusalem, and the craftsmen and metalworkers had left Jerusalem.",
      "T": "This came after King Jeconiah, the queen mother, the court officials, the princes of Judah and Jerusalem, and all the craftsmen and metalworkers had been taken from Jerusalem."
    },
    "3": {
      "L": "by the hand of Elasah the son of Shaphan and Gemariah the son of Hilkiah, whom Zedekiah king of Judah sent to Babylon, to Nebuchadnezzar king of Babylon, saying:",
      "M": "Jeremiah entrusted the letter to Elasah son of Shaphan and Gemariah son of Hilkiah, whom Zedekiah king of Judah was sending as envoys to Nebuchadnezzar king of Babylon. It said:",
      "T": "The letter traveled by the hand of Elasah son of Shaphan and Gemariah son of Hilkiah — the envoys King Zedekiah was dispatching to Nebuchadnezzar in Babylon. This is what it said:"
    },
    "4": {
      "L": "Thus says the LORD of hosts, the God of Israel, to all the captives whom I have carried into exile from Jerusalem to Babylon:",
      "M": "Thus says the LORD of hosts, the God of Israel, to all the exiles whom I have sent into exile from Jerusalem to Babylon:",
      "T": "This is what Yahweh of hosts, the God of Israel, says to all of you whom I have sent into exile from Jerusalem to Babylon:"
    },
    "5": {
      "L": "Build houses and dwell in them; plant gardens and eat their fruit.",
      "M": "Build houses and settle in them; plant gardens and eat what they produce.",
      "T": "Build houses — put down roots in them. Plant gardens — eat what they yield."
    },
    "6": {
      "L": "Take wives and beget sons and daughters; take wives for your sons and give your daughters to husbands, so that they may bear sons and daughters; multiply there, and do not decrease.",
      "M": "Marry and have sons and daughters. Find wives for your sons and give your daughters in marriage, so that they too may have sons and daughters. Multiply there; do not diminish.",
      "T": "Marry, and raise children. Find wives for your sons and give your daughters to husbands, so that your grandchildren fill Babylon too. Grow in number — do not shrink."
    },
    "7": {
      "L": "And seek the welfare of the city to which I have carried you captive, and pray to the LORD on its behalf; for in its welfare you shall have welfare.",
      "M": "Seek the welfare of the city where I have sent you into exile, and pray to the LORD on its behalf; for in its welfare you will find your own welfare.",
      "T": "Seek the shalom of the city where I have placed you in exile — pray to Yahweh for it — because when that city flourishes, you flourish with it."
    },
    "8": {
      "L": "For thus says the LORD of hosts, the God of Israel: Let not your prophets who are among you and your diviners deceive you, and do not listen to the dreams that you dream.",
      "M": "For thus says the LORD of hosts, the God of Israel: Do not let the prophets and diviners among you deceive you, and do not listen to the dreams they dream.",
      "T": "This is what Yahweh of hosts, the God of Israel, says: Do not let the prophets and fortune-tellers in your community deceive you. Do not pay attention to the dreams they conjure."
    },
    "9": {
      "L": "For they are prophesying falsely to you in my name; I have not sent them, says the LORD.",
      "M": "For they are prophesying lies to you in my name; I have not sent them, declares the LORD.",
      "T": "They are speaking lies and calling it my word. I never commissioned a single one of them. Yahweh says so."
    },
    "10": {
      "L": "For thus says the LORD: When seventy years are accomplished for Babylon, I will visit you and fulfill my good word to you, in bringing you back to this place.",
      "M": "For thus says the LORD: When seventy years for Babylon are complete, I will come to you and fulfill my good promise, bringing you back to this place.",
      "T": "This is what Yahweh says: When Babylon's seventy years are over, I will act on your behalf and make good on my promise — I will bring you back to this very place."
    },
    "11": {
      "L": "For I know the plans I plan for you, says the LORD, plans for welfare and not for evil, to give you a future and a hope.",
      "M": "For I know the plans I have for you, declares the LORD, plans for welfare and not for harm, to give you a future and a hope.",
      "T": "I know exactly what I have planned for you — Yahweh declares it. Plans for your flourishing, not your ruin. Plans to give you a real future, a genuine hope."
    },
    "12": {
      "L": "Then you will call upon me and come and pray to me, and I will hear you.",
      "M": "Then you will call on me and come and pray to me, and I will listen to you.",
      "T": "Then you will call out to me. You will come to me and pray — and I will hear every word."
    },
    "13": {
      "L": "You will seek me and find me, when you seek me with all your heart.",
      "M": "You will seek me and find me, when you search for me with all your heart.",
      "T": "You will search for me — and you will find me — when you seek with your whole heart, not halfway."
    },
    "14": {
      "L": "I will be found by you, says the LORD, and I will restore your fortunes and gather you from all the nations and all the places where I have driven you, says the LORD, and I will bring you back to the place from which I sent you into exile.",
      "M": "I will let myself be found by you, declares the LORD. I will restore your fortunes, gather you from all the nations and all the places where I have scattered you, declares the LORD, and bring you back to the place from which I sent you into exile.",
      "T": "I will be found — Yahweh declares it. I will turn your captivity around and gather you from every nation and every land where I drove you. Yahweh's word: I will bring you home to the very place from which you were exiled."
    },
    "15": {
      "L": "Because you have said, The LORD has raised up prophets for us in Babylon —",
      "M": "You may be saying, 'The LORD has appointed prophets for us here in Babylon' —",
      "T": "But you are saying: 'Yahweh has given us prophets even here in Babylon.' —"
    },
    "16": {
      "L": "Know that thus says the LORD concerning the king who sits on the throne of David and all the people who dwell in this city, your brothers who have not gone out with you into exile:",
      "M": "Know that this is what the LORD says concerning the king who sits on David's throne and all the people who remain in this city — your fellow Judeans who were not taken into exile with you:",
      "T": "Then hear what Yahweh says about the king now sitting on David's throne and all the people still in Jerusalem — your own kin who were not carried off into exile with you:"
    },
    "17": {
      "L": "Thus says the LORD of hosts: Behold, I am sending against them sword, famine, and pestilence, and I will make them like vile figs that cannot be eaten, they are so bad.",
      "M": "Thus says the LORD of hosts: I am going to send sword, famine, and pestilence against them, and make them like rotten figs that are too spoiled to eat.",
      "T": "Yahweh of hosts says this: I am sending sword, famine, and plague against them — making them like inedible, rotten figs, repulsive to the core."
    },
    "18": {
      "L": "I will pursue them with sword, famine, and pestilence, and will make them a horror to all the kingdoms of the earth, a curse, a devastation, an object of hissing, and a reproach among all the nations where I have driven them,",
      "M": "I will pursue them with sword, famine, and pestilence, and make them a horror to all the kingdoms of the earth, a curse, a devastation, an object of hissing, and a reproach among all the nations where I have driven them.",
      "T": "I will hunt them down with sword, starvation, and plague, and scatter them as a curse and a horror and an object of hissing among all the kingdoms of the earth — a byword of ruin in every nation where I drive them."
    },
    "19": {
      "L": "because they did not heed my words, says the LORD, which I sent to them by my servants the prophets, sending them persistently; but you would not listen, says the LORD.",
      "M": "because they did not obey my words, declares the LORD — which I sent to them persistently through my servants the prophets — but they would not listen, declares the LORD.",
      "T": "All of this because they refused to hear my words — Yahweh declares it — the words I sent them through my servants the prophets, urgently, again and again. They would not listen."
    },
    "20": {
      "L": "Hear therefore the word of the LORD, all you of the captivity whom I have sent from Jerusalem to Babylon:",
      "M": "So hear the word of the LORD, all you exiles whom I have sent from Jerusalem to Babylon:",
      "T": "So hear the word of Yahweh — all of you whom I have sent from Jerusalem into exile in Babylon:"
    },
    "21": {
      "L": "Thus says the LORD of hosts, the God of Israel, concerning Ahab the son of Kolaiah and Zedekiah the son of Maaseiah, who are prophesying a lie to you in my name: Behold, I will give them into the hand of Nebuchadnezzar king of Babylon, and he shall strike them down before your eyes.",
      "M": "Thus says the LORD of hosts, the God of Israel, concerning Ahab son of Kolaiah and Zedekiah son of Maaseiah, who are prophesying lies to you in my name: I will hand them over to Nebuchadnezzar king of Babylon, and he will execute them before your very eyes.",
      "T": "This is what Yahweh of hosts, the God of Israel, says about Ahab son of Kolaiah and Zedekiah son of Maaseiah — those two who peddle lies in my name: I am handing them over to Nebuchadnezzar king of Babylon, who will execute them before your eyes."
    },
    "22": {
      "L": "And because of them a curse shall be used by all the captives of Judah in Babylon, saying: The LORD make you like Zedekiah and like Ahab, whom the king of Babylon burned in the fire —",
      "M": "Because of them, this curse-saying will be used among all the Judean exiles in Babylon: 'May the LORD make you like Zedekiah and like Ahab, whom the king of Babylon burned in the fire!'",
      "T": "Their fate will become a curse-formula on the lips of every Judean exile in Babylon: 'May Yahweh make you like Zedekiah and Ahab, whom Babylon's king roasted alive.'"
    },
    "23": {
      "L": "because they have done a vile thing in Israel, and have committed adultery with their neighbors' wives, and have spoken lying words in my name that I did not command them; I am the one who knows, and I am a witness, says the LORD.",
      "M": "For they have done a disgraceful thing in Israel: they committed adultery with their neighbors' wives and spoke false words in my name that I did not command. I myself know, and I am a witness, declares the LORD.",
      "T": "What they did in Israel is obscene — adultery with their neighbors' wives, and then fabricating oracles and calling them mine, words I never authorized. I know every detail. I am the witness. Yahweh says so."
    },
    "24": {
      "L": "To Shemaiah the Nehelamite you shall speak, saying:",
      "M": "To Shemaiah the Nehelamite you are to say:",
      "T": "And you are to send a word to Shemaiah the Nehelamite — this message:"
    },
    "25": {
      "L": "Thus says the LORD of hosts, the God of Israel: You have sent letters in your name to all the people who are at Jerusalem, and to Zephaniah the son of Maaseiah the priest, and to all the priests, saying:",
      "M": "Thus says the LORD of hosts, the God of Israel: You sent letters in your own name to all the people in Jerusalem, to Zephaniah son of Maaseiah the priest, and to all the priests, saying:",
      "T": "This is what Yahweh of hosts, the God of Israel, says: You have sent letters under your own signature to all the people in Jerusalem — including Zephaniah son of Maaseiah the priest and the entire priesthood — and in those letters you wrote:"
    },
    "26": {
      "L": "The LORD has made you priest in place of Jehoiada the priest, to have charge in the house of the LORD over every man who is mad and makes himself a prophet, that you should put him in the stocks and collar.",
      "M": "The LORD has appointed you priest in place of Jehoiada the priest, to be in charge of the house of the LORD — so that you may arrest any madman who plays at being a prophet and put him in the stocks and in an iron collar.",
      "T": "Yahweh has placed you as chief priest in Jehoiada's stead, with authority over the temple. Any madman who sets himself up as a prophet is to be arrested, put in the stocks, and locked in an iron collar."
    },
    "27": {
      "L": "So why have you not rebuked Jeremiah of Anathoth who plays the prophet to you?",
      "M": "Why then have you not rebuked Jeremiah of Anathoth, who is playing the prophet among you?",
      "T": "So why have you not silenced Jeremiah of Anathoth, who keeps playing the prophet in your midst?"
    },
    "28": {
      "L": "For he has sent to us in Babylon, saying: Your captivity is long; build houses and dwell in them, and plant gardens and eat their fruit.",
      "M": "For he has sent word to us in Babylon, saying: Your exile will be long; build houses and settle in them, and plant gardens and eat their fruit.",
      "T": "Because — consider — he actually sent word to us in Babylon: 'Your exile is going to be a long one. Build houses, settle in, plant gardens, eat what they produce.' That is what he told us!"
    },
    "29": {
      "L": "Zephaniah the priest read this letter in the ears of the prophet Jeremiah.",
      "M": "Zephaniah the priest read this letter aloud to the prophet Jeremiah.",
      "T": "Zephaniah the priest read the letter aloud to Jeremiah the prophet."
    },
    "30": {
      "L": "Then the word of the LORD came to Jeremiah, saying:",
      "M": "Then the word of the LORD came to Jeremiah:",
      "T": "Then Yahweh's word came to Jeremiah:"
    },
    "31": {
      "L": "Send word to all the captives, saying: Thus says the LORD concerning Shemaiah the Nehelamite — Because Shemaiah has prophesied to you, though I did not send him, and has made you trust in a lie —",
      "M": "Send word to all the exiles: Thus says the LORD concerning Shemaiah the Nehelamite — Because Shemaiah has prophesied to you when I did not send him, and has made you trust in a lie —",
      "T": "Send this message to all the exiles: Yahweh speaks concerning Shemaiah the Nehelamite. Because he prophesied to you without any commission from me, and led you to build your lives on a lie —"
    },
    "32": {
      "L": "therefore thus says the LORD: Behold, I will punish Shemaiah the Nehelamite and his offspring; he shall not have a man to dwell among this people; he shall not see the good that I will do for my people, says the LORD, because he has preached rebellion against the LORD.",
      "M": "therefore thus says the LORD: I am going to punish Shemaiah the Nehelamite and his descendants. None of them will live among this people to see the good I intend to do for my people, declares the LORD, because he preached rebellion against the LORD.",
      "T": "this is what Yahweh says: I will bring punishment on Shemaiah the Nehelamite and his entire line. None of his descendants will live to see the day when I restore my people — Yahweh declares it — because he spent his life inciting rebellion against Yahweh."
    }
  },
  "30": {
    "1": {
      "L": "The word that came to Jeremiah from the LORD, saying:",
      "M": "The word that came to Jeremiah from the LORD:",
      "T": "This is the word that came to Jeremiah from Yahweh:"
    },
    "2": {
      "L": "Thus says the LORD, the God of Israel: Write in a book all the words that I have spoken to you.",
      "M": "Thus says the LORD, the God of Israel: Write in a book all the words I have spoken to you.",
      "T": "This is what Yahweh, the God of Israel, says: Write down every word I have spoken to you — record it all in a scroll."
    },
    "3": {
      "L": "For behold, the days are coming, says the LORD, when I will restore the fortunes of my people Israel and Judah, says the LORD, and I will bring them back to the land that I gave to their fathers, and they shall take possession of it.",
      "M": "For the days are coming, declares the LORD, when I will restore the fortunes of my people Israel and Judah, declares the LORD, and bring them back to the land I gave their fathers; and they shall possess it.",
      "T": "Days are coming — Yahweh declares it — when I will turn the captivity of my people Israel and Judah around and bring them back to the land I gave their ancestors. It will be theirs again."
    },
    "4": {
      "L": "These are the words that the LORD spoke concerning Israel and concerning Judah.",
      "M": "These are the words the LORD spoke concerning Israel and Judah.",
      "T": "These are Yahweh's words for Israel and for Judah."
    },
    "5": {
      "L": "For thus says the LORD: A voice of trembling we have heard, of dread and not of peace.",
      "M": "Thus says the LORD: We have heard a cry of terror, of dread — not of peace.",
      "T": "This is what Yahweh says: The sound that reaches us is sheer terror — panic, not peace."
    },
    "6": {
      "L": "Ask now and see: can a man bear a child? Why then do I see every man with his hands on his stomach like a woman in labor? Why have all faces turned pale?",
      "M": "Ask yourselves and look: can a man give birth? Then why is every man clutching his sides like a woman in labor, and why has every face gone pale?",
      "T": "Ask yourself, look carefully: do men give birth? Then why does every man grip his sides like a woman in the agony of labor? Why has every face drained to ash?"
    },
    "7": {
      "L": "Alas! For that day is great; there is none like it; it is a time of distress for Jacob, but he shall be saved from it.",
      "M": "How terrible that day will be! There has never been another like it. It is a time of anguish for Jacob — but he will be saved out of it.",
      "T": "What a day that will be — unmatched in its horror! It is the hour of Jacob's agony. Yet he will be rescued from it."
    },
    "8": {
      "L": "And it shall come to pass in that day, says the LORD of hosts, that I will break his yoke from your neck and burst your bonds, and strangers shall no more make you serve them.",
      "M": "On that day, declares the LORD of hosts, I will break the yoke from your neck and snap your bonds. Foreigners will no longer make you their servant.",
      "T": "On that day — Yahweh of hosts declares it — I will shatter the yoke on your neck and tear your chains apart. Never again will a foreign master own you."
    },
    "9": {
      "L": "But they shall serve the LORD their God and David their king, whom I will raise up for them.",
      "M": "Instead they will serve the LORD their God and David their king, whom I will raise up for them.",
      "T": "Instead they will serve Yahweh their God and David their king — the one I will raise up for them."
    },
    "10": {
      "L": "Therefore fear not, O my servant Jacob, says the LORD; be not dismayed, O Israel; for behold, I am saving you from far away and your offspring from the land of their captivity; Jacob shall return and be at rest and be quiet, and none shall make him afraid.",
      "M": "So do not be afraid, my servant Jacob, declares the LORD; do not be dismayed, O Israel. For I am going to save you from far away, and your descendants from the land of their captivity. Jacob will return and have rest and peace — no one will terrorize him.",
      "T": "So do not be afraid, Jacob my servant — Yahweh declares it. Do not panic, Israel. I am bringing you home from a great distance, your children from the land of their exile. Jacob will come back and live in peace and security — nothing will make him tremble."
    },
    "11": {
      "L": "For I am with you, says the LORD, to save you; for I will make a full end of all the nations among whom I have scattered you, but of you I will not make a full end. I will discipline you in justice, but I will by no means leave you unpunished.",
      "M": "For I am with you, declares the LORD, to save you. Though I will completely destroy all the nations where I have scattered you, I will not completely destroy you. I will discipline you with justice, but I will not let you go entirely without punishment.",
      "T": "I am with you — Yahweh declares it — to deliver you. Though I bring every nation where I scattered you to complete ruin, I will not bring you to complete ruin. I will correct you, and the correction will be just — but I will not simply let you off."
    },
    "12": {
      "L": "For thus says the LORD: Your hurt is incurable, your wound is grievous.",
      "M": "For thus says the LORD: Your injury is incurable, your wound is severe.",
      "T": "This is what Yahweh says: Your wound is past all human healing. Your injury is beyond treatment."
    },
    "13": {
      "L": "There is no one to plead your cause; for your wound there is no healing medicine; there is no recovery for you.",
      "M": "There is no one to plead your case; you have no medicines for your wound — no recovery for you.",
      "T": "No advocate will rise to argue your case. No physician has medicine for this wound. There is no recovery to be had from any human source."
    },
    "14": {
      "L": "All your lovers have forgotten you; they seek you not; for I have struck you with the wound of an enemy, with the chastisement of a ruthless one, because your guilt is great and your sins are many.",
      "M": "All your allies have abandoned you; they no longer care about you. For I have struck you as an enemy would strike, with the discipline of a ruthless foe, because your guilt is great and your sins are many.",
      "T": "Every ally you relied on has forgotten you and stopped caring whether you live or die. Because I myself struck you as an enemy strikes — with the severity of a merciless adversary — because your guilt is enormous and your sins have piled up beyond measure."
    },
    "15": {
      "L": "Why do you cry out over your hurt? Your pain is incurable. Because your guilt is great and your sins are many, I have done these things to you.",
      "M": "Why do you cry out over your wound? Your pain is incurable. Because your guilt is great and your sins are many, I have done these things to you.",
      "T": "Why do you keep crying out about your suffering? Your pain is incurable — and it is deserved. It is because your guilt is so great and your sins have gone on so long that I have brought all this on you."
    },
    "16": {
      "L": "Therefore all who devour you shall be devoured, and all your adversaries, every one of them, shall go into captivity; those who plunder you shall be plundered, and all who prey upon you I will make prey.",
      "M": "Therefore all who devour you will be devoured, and all your adversaries will go into captivity; those who plunder you will be plundered, and all who prey on you I will make into prey.",
      "T": "But this is where it turns: everyone who consumed you will themselves be consumed. All your enemies will go into their own exile. Those who stripped you bare will be stripped. Those who preyed on you — I will make them the prey."
    },
    "17": {
      "L": "For I will restore health to you and heal your wounds, says the LORD, because they called you an outcast: It is Zion, for whom no one cares!",
      "M": "For I will restore your health and heal your wounds, declares the LORD, because they called you Outcast — 'This is Zion; no one cares about her.'",
      "T": "I will restore you to health and close every wound — Yahweh declares it. Why? Because they said you were an outcast, said that nobody wants Zion, nobody comes looking for her. I am coming."
    },
    "18": {
      "L": "Thus says the LORD: Behold, I will restore the fortunes of Jacob's tents and have compassion on his dwellings; the city shall be rebuilt on its mound, and the palace shall stand where it used to be.",
      "M": "Thus says the LORD: I am going to restore the fortunes of Jacob's tents and have compassion on his dwelling places. The city will be rebuilt on its hill, and the palace will stand as it did before.",
      "T": "This is what Yahweh says: I am turning Jacob's exile around, showing compassion on every home that now lies empty. The city will rise again on its ancient mound, and the royal palace will stand where it stood before."
    },
    "19": {
      "L": "And out of them shall come thanksgiving and the sound of merrymakers; I will multiply them and they shall not be few; I will make them honored and they shall not be small.",
      "M": "From them will come songs of thanksgiving and the sound of rejoicing. I will multiply them so that they will not be few; I will honor them so that they will not be insignificant.",
      "T": "From those rebuilt streets will come songs of praise and the sound of celebration. I will multiply their numbers — they will not be a remnant rump. I will give them dignity — they will not be a forgotten footnote among the nations."
    },
    "20": {
      "L": "Their children shall be as in former times, and their congregation shall be established before me, and I will punish all who oppress them.",
      "M": "Their children will be as they were in former times, and their congregation will be established before me; and I will punish all who oppress them.",
      "T": "Their children will flourish as they did in the old days. Their community will stand firm before me. And every nation that oppresses them — I will deal with them."
    },
    "21": {
      "L": "Their ruler shall be one of themselves, and their governor shall come forth from their midst; I will make him draw near, and he shall approach me; for who would dare of himself to approach me? says the LORD.",
      "M": "Their leader will come from among them, and their governor will emerge from their own midst. I will bring him close, and he will approach me — for who would dare on his own to approach me? declares the LORD.",
      "T": "Their ruler will be one of their own — no foreign governor placed over them from outside. Their leader will rise from among themselves. I will draw him close, and he will have access to me. For who would ever presume on their own to approach me? Yahweh asks."
    },
    "22": {
      "L": "And you shall be my people, and I will be your God.",
      "M": "You will be my people, and I will be your God.",
      "T": "You will be my people. I will be your God."
    },
    "23": {
      "L": "Behold, the storm of the LORD! Wrath has gone forth, a whirling tempest; it shall burst upon the head of the wicked.",
      "M": "See, the storm of the LORD! His wrath has gone forth, a sweeping whirlwind; it will break upon the head of the wicked.",
      "T": "Look — the storm of Yahweh is breaking out! His fury sweeps forward like a howling whirlwind, crashing down on the heads of the wicked."
    },
    "24": {
      "L": "The fierce anger of the LORD will not turn back until he has accomplished and performed the purposes of his heart. In the latter days you will understand this.",
      "M": "The fierce anger of the LORD will not turn back until he has done and performed the purposes of his heart. In the latter days you will understand this.",
      "T": "Yahweh's fierce anger will not relent until every intention of his heart is executed and complete. In the days that are coming — then you will understand it."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'jeremiah')
        merge_tier(existing, JEREMIAH, tier_key)
        save(tier_dir, 'jeremiah', existing)
    print('Jeremiah 28–30 written.')

if __name__ == '__main__':
    main()
