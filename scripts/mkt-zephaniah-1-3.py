"""
MKT Zephaniah chapters 1–3 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-zephaniah-1-3.py

=== BOOK OVERVIEW ===

Zephaniah prophesied during the reign of Josiah of Judah (ca. 640–609 BCE), likely
before the Josianic reform of 621. His four-generation genealogy (traced to Hezekiah)
gives him unusual royal pedigree among the prophets.

Structure:
  1:1         — Superscription
  1:2–18      — The Day of the LORD: universal and comprehensive judgment
  2:1–3:8     — Call to repentance; oracles against Philistia, Moab, Ammon, Cush,
                 Assyria; then against Jerusalem itself
  3:9–20      — Restoration: purified speech, humble remnant, the great homecoming

Zephaniah is the prophetic source of the Dies Irae (1:15–16), drawn directly from
his accumulation of "day" epithets. The book ends with arguably the warmest
divine portrait in the Twelve (3:17): God singing over his people.

=== TEXTUAL NOTES ===

- 1:2: The Hebrew uses the infinitive absolute ʾāsōp ʾăsēp (H5486 twice) — "gather-
  gathering I will gather" — an emphatic construction for total annihilation.
- 1:3: The reversal of creation order (humans > animals > birds > fish) deliberately
  echoes Genesis 1 in reverse; the T tier makes this explicit.
- 1:9: "Leap over the threshold" (H1801) may reference the Philistine practice of
  avoiding Dagon's threshold (1 Sam 5:5), here applied to Jerusalem officials
  performing syncretistic rites.
- 2:1: H3700 (not desired / shameless) — the nation has ceased to long for God.
  The KJV "not desired" is precise; "shameless" captures the moral texture in M/T.
- 2:4: The Hebrew contains wordplays: Gaza (ʿazzāh) = "forsaken" (ʿăzûbāh);
  Ekron (ʿeqrôn) = "uprooted" (teʿāqēr). The T tier surfaces the pun.
- 3:9: "Pure lip/speech" (H8193 + H1305) — a reversal of Babel (Gen 11). Noted
  in T tier.
- 3:17: H2790 (be silent/rest) in the phrase "he will be silent in his love" is
  often rendered "he will renew" following LXX. The Hebrew qal of חָשָׁה means
  "to be still, to rest" — the image is of God resting in quiet love rather than
  speaking. T retains the more distinctive sense.

=== CONTESTED-TERM DECISIONS ===

- H3068 (יהוה / Yahweh):
  L/M: "LORD" (small-caps convention) throughout.
  T: "Yahweh" in direct address, oracle closings, and climactic declarations
     (1:2, 1:7, 2:3, 2:9, 3:8, 3:17, 3:20); "the LORD" in narrative/descriptive
     clauses. Reason: same policy as Micah and the prior Minor Prophets.

- H2617 (חֶסֶד / chesed) — not directly present in Zephaniah but H160 (ʾahabāh,
  love) appears in 3:17. Rendered "love" in L/M; "love that holds still" in T
  (capturing the H2790 / silence dynamic of the verse).

- H5315 (נֶפֶשׁ / nephesh) — not prominent here; occurs implicitly in several
  verses. Where used: "my soul" in L; "soul" or natural equivalent in M/T
  depending on whether Platonic resonance would mislead.

- H7307 (רוּחַ / ruach) — not present in Zephaniah.

- H5678 / H2740 (עֶבְרָה / ḥărôn, wrath/anger):
  L: "wrath" / "fierce anger" (lexical words).
  M: same.
  T: "fury" / "blazing wrath" where the context is most severe (1:15, 1:18).

- H7068 (קִנְאָה / qinʾāh, jealousy/zeal):
  L: "jealousy" (primary gloss).
  M: "jealousy" (retained; the divine jealousy is always covenant jealousy).
  T: "jealous love" in 1:18 and 3:8 — the zeal of the covenant God is never mere
     possessiveness but the fierce love of a spurned suzerain.

- H430 (אֱלֹהִים / Elohim):
  Rendered "God" throughout; no shift between tiers needed in Zephaniah's usage.

- H6664 (צְדָקָה / tsedaqah, righteousness) — appears in 2:3:
  L/M: "righteousness".
  T: "right living" (context is ethical conduct, not forensic status).

- H4941 (מִשְׁפָּט / mishpat, justice/judgment):
  L: "judgment" (lexical term).
  M: "justice" in the sense of just ordering; "judgments" where legal verdicts
     are meant.
  T: context-dependent: "verdict", "justice", or "righteous order".
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

ZEPHANIAH = {
  "1": {
    "1": {
      "L": "The word of the LORD that came to Zephaniah the son of Cushi, the son of Gedaliah, the son of Amariah, the son of Hezekiah, in the days of Josiah the son of Amon, king of Judah.",
      "M": "The word of the LORD that came to Zephaniah son of Cushi, son of Gedaliah, son of Amariah, son of Hezekiah, during the reign of Josiah son of Amon, king of Judah.",
      "T": "This is the word Yahweh spoke to Zephaniah — son of Cushi, son of Gedaliah, son of Amariah, son of Hezekiah — in the days when Josiah son of Amon sat on the throne of Judah."
    },
    "2": {
      "L": "I will utterly sweep away everything from the face of the land, declares the LORD.",
      "M": "I will completely sweep away everything from the face of the land, declares the LORD.",
      "T": "I will sweep everything away from the face of the earth — utterly, without remainder, declares Yahweh."
    },
    "3": {
      "L": "I will sweep away man and beast; I will sweep away the birds of the heavens and the fish of the sea, and the stumblingblocks with the wicked; and I will cut off mankind from the face of the land, declares the LORD.",
      "M": "I will destroy both people and animals; I will destroy the birds of the sky and the fish of the sea. Together with the wicked I will remove what causes stumbling, and I will cut off humanity from the face of the land, declares the LORD.",
      "T": "People, animals, birds, fish — I will consume them all in sequence. This is creation being unmade in reverse. Along with the wicked I will sweep away everything that leads others astray, and humanity will be cut off from the earth, declares Yahweh."
    },
    "4": {
      "L": "I will stretch out my hand against Judah and against all the inhabitants of Jerusalem; and I will cut off from this place the remnant of Baal and the name of the Chemarim-priests with the priests,",
      "M": "I will stretch out my hand against Judah and against all the inhabitants of Jerusalem. I will cut off from this place every remnant of Baal — the very name of the idolatrous priests along with the priests,",
      "T": "I will move against Judah and every person living in Jerusalem. I will wipe out every trace of Baal — his last remnant, his idolatrous shrine-priests, every priest who tolerated him. Their names will be erased from this place."
    },
    "5": {
      "L": "and those who bow down on the rooftops to the host of the heavens, and those who bow down swearing to the LORD and swearing also by Malcam,",
      "M": "those who bow down on the rooftops to the host of the heavens; those who swear allegiance to the LORD while also swearing by Malcam;",
      "T": "those who prostrate themselves on their rooftops to the army of stars; those who swear by Yahweh and in the same breath swear by Malcam — trying to hold both allegiances at once, belonging to neither;"
    },
    "6": {
      "L": "and those who have turned back from following the LORD, and those who have not sought the LORD and have not inquired of him.",
      "M": "and those who have turned away from following the LORD — those who have not sought the LORD and have not asked after him.",
      "T": "and those who have simply turned their backs on Yahweh — who have never once sought him, never once asked where he is. They live as if he does not exist."
    },
    "7": {
      "L": "Be silent before the Lord GOD! For the day of the LORD is near; the LORD has prepared a sacrifice; he has consecrated his guests.",
      "M": "Be silent before the Lord GOD! The day of the LORD is near. The LORD has prepared a sacrifice and has set apart those he has invited.",
      "T": "Silence — stand in awe before the Lord GOD. The day of Yahweh is almost here. He has prepared a sacrifice, and you are the ones he has consecrated to be offered at it."
    },
    "8": {
      "L": "And it shall come to pass on the day of the LORD's sacrifice, that I will punish the princes and the king's sons and all who are clothed in foreign apparel.",
      "M": "On the day of the LORD's sacrifice I will punish the princes and the king's sons — and all who clothe themselves in foreign garments.",
      "T": "On that day of sacrifice I will single out the princes and the royal household — and every official who has dressed himself in foreign fashions, trading his identity for another nation's style."
    },
    "9": {
      "L": "On that same day I will punish everyone who leaps over the threshold, who fill their masters' houses with violence and deceit.",
      "M": "On that same day I will punish all who leap over the threshold — those who fill their lords' houses with violence and dishonesty.",
      "T": "On that day I will deal with those who hop over the threshold performing their ritual rites, while their hands pile their lords' houses high with what they have seized by violence and fraud."
    },
    "10": {
      "L": "On that day, declares the LORD, there will be the sound of a cry from the Fish Gate, a wailing from the Second Quarter, and a great crash from the hills.",
      "M": "On that day, declares the LORD, a cry will come from the Fish Gate, a wail from the Second Quarter of the city, and a great crash from the hills.",
      "T": "On that day, declares Yahweh, the cries will come in waves: screaming from the Fish Gate, howling from the newer quarter of the city, the thunder of catastrophe rolling in from the hills above."
    },
    "11": {
      "L": "Wail, O inhabitants of the Maktesh! For all the merchant people are cut off; all who weigh out silver are cut down.",
      "M": "Wail, inhabitants of the Maktesh! For every merchant has been destroyed; all who deal in silver have been cut down.",
      "T": "Howl, you who live in the Maktesh — the trading hollow of the city! Every merchant has been silenced; every money-changer swept away. Commerce itself has ended."
    },
    "12": {
      "L": "At that time I will search Jerusalem with lamps, and I will punish the men who are thickening on their dregs, who say in their hearts, 'The LORD will not do good, nor will he do ill.'",
      "M": "At that time I will search Jerusalem with lamps and punish those who have grown complacent, settled like wine thick on its dregs — those who say to themselves, 'The LORD will do nothing, neither good nor harm.'",
      "T": "When that time comes I will take a lamp and go through Jerusalem room by room. I am after the ones who have grown sluggish and self-satisfied, like wine left too long on its sediment — the people who have told themselves: 'Yahweh will never act. Nothing will happen.' They are wrong."
    },
    "13": {
      "L": "Their goods shall become plunder, and their houses a desolation. They shall build houses but not inhabit them; they shall plant vineyards but not drink their wine.",
      "M": "Their wealth will be looted, and their houses will become ruins. They will build houses but not live in them; they will plant vineyards but not drink their wine.",
      "T": "Everything they accumulated will be stripped away; their houses will stand empty as ruins. They will build — but others will move in. They will plant — but someone else will drink the wine. The covenant curses they ignored will fall on them in full."
    },
    "14": {
      "L": "The great day of the LORD is near; it is near and hastening greatly. The voice of the day of the LORD is bitter; the mighty man cries out there.",
      "M": "The great day of the LORD is near — near and coming very quickly. The sound of the day of the LORD is bitter; even the warrior cries out in anguish.",
      "T": "The great Day of Yahweh is almost here — bearing down at full speed. Listen: the sound of that day is the sound of bitter weeping. Even the battle-hardened soldier will cry out in that day."
    },
    "15": {
      "L": "That day is a day of wrath, a day of distress and anguish, a day of ruin and devastation, a day of darkness and gloom, a day of clouds and thick darkness,",
      "M": "That day is a day of wrath, a day of distress and anguish, a day of ruin and desolation, a day of darkness and gloom, a day of clouds and thick darkness,",
      "T": "That day — a day of wrath, a day of distress and anguish, a day of ruin and devastation, a day of darkness and thick gloom, a day of cloud and dense shadow — each word heaping up the dread of what is coming."
    },
    "16": {
      "L": "a day of trumpet blast and battle cry against the fortified cities and against the high corner towers.",
      "M": "a day of trumpet blast and war cry against the fortified cities and the high corner towers.",
      "T": "the trumpet sounding, the battle cry rising against every fortified city and every high tower that men trusted for their safety."
    },
    "17": {
      "L": "I will bring distress on mankind, so that they shall walk like the blind, because they have sinned against the LORD; their blood shall be poured out like dust, and their flesh like dung.",
      "M": "I will bring such distress on the people that they will grope about like the blind — because they have sinned against the LORD. Their blood will be poured out like dust, and their bodies like dung.",
      "T": "I will press such terror on humanity that they stumble and grope like the blind — the consequence of their sin against Yahweh. Their blood will be scattered like loose soil; their bodies treated like refuse in the street."
    },
    "18": {
      "L": "Neither their silver nor their gold shall be able to deliver them on the day of the LORD's wrath. In the fire of his jealousy the whole land shall be consumed; for he will make a full and sudden end of all the inhabitants of the land.",
      "M": "Neither their silver nor their gold will be able to rescue them on the day of the LORD's wrath. The whole land will be consumed in the fire of his jealousy, for he will bring a swift and complete end to all who live in the land.",
      "T": "Silver is useless; gold is useless — on the day Yahweh's wrath breaks loose, no wealth buys escape. The fire of his jealous love will consume the whole earth. He will make a swift and total end of everyone who has made this land their foundation while defying him."
    }
  },
  "2": {
    "1": {
      "L": "Gather together, gather yourselves, O shameless nation,",
      "M": "Come together, gather yourselves, O shameless nation,",
      "T": "Gather what you have left, you nation that no longer yearns for God —"
    },
    "2": {
      "L": "before the decree takes effect — before the day passes away like chaff — before there comes upon you the fierce anger of the LORD, before there comes upon you the day of the LORD's anger.",
      "M": "before the appointed decree arrives — before the day passes like chaff — before the LORD's burning anger reaches you, before the day of the LORD's anger comes upon you.",
      "T": "— before the sentence falls, before the day blows past like chaff in the wind. Act before Yahweh's blazing wrath breaks on you; act before that day of his anger arrives."
    },
    "3": {
      "L": "Seek the LORD, all you humble of the land, who have carried out his justice; seek righteousness, seek humility; perhaps you may be hidden on the day of the LORD's anger.",
      "M": "Seek the LORD, all you humble people of the land who have carried out his commands. Seek righteousness; seek humility. Perhaps you will be sheltered on the day of the LORD's anger.",
      "T": "You who are truly lowly — you who have done what Yahweh commanded — seek him with everything you have. Pursue right living; pursue humility. Perhaps in the day of his wrath you will find a shelter. Perhaps you will be hidden."
    },
    "4": {
      "L": "For Gaza shall be forsaken, and Ashkelon a desolation; Ashdod's people shall be driven out at noon, and Ekron shall be uprooted.",
      "M": "For Gaza will be abandoned and Ashkelon laid waste; the people of Ashdod will be driven out at midday, and Ekron will be uprooted.",
      "T": "Gaza will be abandoned — its name a prophecy of its own desertion. Ashkelon will be a wasteland. Ashdod's people will be chased out in broad daylight. Ekron will be torn up by the roots."
    },
    "5": {
      "L": "Woe to the inhabitants of the seacoast, the nation of the Cherethites! The word of the LORD is against you, O Canaan, land of the Philistines; I will destroy you until no inhabitant remains.",
      "M": "Woe to the inhabitants of the seacoast, the Cherethite nation! The word of the LORD is against you, Canaan, land of the Philistines. I will destroy you until no one is left.",
      "T": "Woe to those who live along the sea — the Cherethites, the Philistines, the whole Canaanite coastline. Yahweh's word stands against you: I will bring you so low that not one person will be left to inhabit what remains."
    },
    "6": {
      "L": "The seacoast shall become pastures, meadows for shepherds and folds for flocks.",
      "M": "The seacoast will become meadows, with pastures for shepherds and pens for flocks.",
      "T": "That coastline of cities and commerce will be reduced to open pasture — grass for shepherds, pens for their animals. The civilization will be gone."
    },
    "7": {
      "L": "The seacoast shall belong to the remnant of the house of Judah; they shall graze there. In the houses of Ashkelon they shall lie down in the evening; for the LORD their God will attend to them and restore their fortunes.",
      "M": "The coast will belong to the remnant of the house of Judah; they will find pasture there. In the evening they will lie down in the houses of Ashkelon, for the LORD their God will attend to them and restore their prosperity.",
      "T": "But that same coast will one day belong to the remnant of Judah. They will graze on Philistine land; they will rest in the houses of Ashkelon as evening falls. For Yahweh their God will come to them — visit them, attend to them — and he will bring them back from captivity."
    },
    "8": {
      "L": "I have heard the taunts of Moab and the revilings of the Ammonites, how they taunted my people and boasted against their territory.",
      "M": "I have heard the insults of Moab and the mockery of the Ammonites — how they taunted my people and boasted over their borders.",
      "T": "I have been listening. Moab's taunts, Ammon's jeers — the sneering at my people, the boasting over their territory. None of it has been forgotten."
    },
    "9": {
      "L": "Therefore, as I live, declares the LORD of hosts, the God of Israel: Moab shall become like Sodom, and Ammon like Gomorrah — a possession of nettles and salt pits and a wasteland forever. The remnant of my people shall plunder them, and the survivors of my nation shall possess them.",
      "M": "Therefore, as I live, declares the LORD of Hosts, the God of Israel: Moab will become like Sodom, and Ammon like Gomorrah — a land of nettles and salt pits, a desolation forever. The remnant of my people will plunder them, and the survivors of my nation will inherit their land.",
      "T": "Therefore — as I live, declares Yahweh of Armies, the God of Israel — Moab will end up like Sodom, Ammon like Gomorrah: thorn-choked, salt-caked, an everlasting ruin. And the very people they mocked will possess their land. The survivors of my nation will claim what was once used to jeer at them."
    },
    "10": {
      "L": "This shall be their lot in return for their pride, because they taunted and boasted against the people of the LORD of hosts.",
      "M": "This is what they will receive for their pride — for taunting and boasting against the people of the LORD of Hosts.",
      "T": "This is the price of pride: they mocked the people of Yahweh of Armies, and so they will be brought to nothing. Pride that raises itself against God's people raises itself against God."
    },
    "11": {
      "L": "The LORD will be terrifying against them; for he will make all the gods of the earth waste away, and every person in his own place shall worship him — all the coasts and islands of the nations.",
      "M": "The LORD will be fearsome toward them, for he will reduce all the gods of the earth to nothing; and every nation in its own land will bow down to him — all the shores and islands of the nations.",
      "T": "Yahweh himself will be what terrifies them — because he is starving out every foreign god, stripping away their power until there is nothing left. And then, from every corner of the earth, people in their own homelands will bow down to him. No rival will remain."
    },
    "12": {
      "L": "You also, O Cushites — you shall be slain by my sword.",
      "M": "You too, O Cushites — you will be killed by my sword.",
      "T": "And you, O Cushites — my sword will reach you as well."
    },
    "13": {
      "L": "And he will stretch out his hand against the north and destroy Assyria, and he will make Nineveh a desolation, dry as the wilderness.",
      "M": "He will also stretch out his hand against the north and destroy Assyria, making Nineveh a desolation as dry as a desert.",
      "T": "Then his hand will reach northward: Assyria will fall. Nineveh — the great and proud capital — will be dried up and emptied, as barren as desert sand."
    },
    "14": {
      "L": "Flocks shall lie down in her midst, every kind of wild creature; both the pelican and the owl shall lodge in her capitals; the owl shall hoot at the window; desolation shall be on the threshold; for the cedar work is laid bare.",
      "M": "Flocks will bed down in the middle of the city — every kind of wild animal. The pelican and the owl will roost in the carved columns; something will hoot at the windows; desolation will stand at every threshold; for the cedar paneling will be stripped away.",
      "T": "Where once armies marched, flocks will lie down — wild animals of every kind at home in the ruins. Pelicans and owls will nest in what were once grand capitals. Something will cry out through the windows at night; desolation will stand in every doorway. The cedar paneling — the trophy of Nineveh's wealth — will be ripped away and scattered."
    },
    "15": {
      "L": "This is the exultant city that lived in security, that said in her heart, 'I am, and there is no one else.' What a desolation she has become, a lair for wild animals! Everyone who passes by her hisses and shakes his fist at her.",
      "M": "This is the carefree city that felt so secure, that said to itself, 'I am supreme — there is nothing like me.' What a ruin she has become, a haunt for wild animals! Everyone who passes by hisses and makes a gesture of contempt.",
      "T": "This is the city that lounged in complacency, telling itself, 'I am supreme — there is nothing like me.' Look at her now: a wasteland where wild animals bed down. Every traveler who passes stops to hiss in disbelief and waves her away in scorn. The greatest city in the world has come to this."
    }
  },
  "3": {
    "1": {
      "L": "Woe to her who is filthy and defiled, to the oppressing city!",
      "M": "Woe to the rebellious, defiled, oppressing city!",
      "T": "Woe to the city soaked in rebellion — corrupt, defiled, grinding down the helpless."
    },
    "2": {
      "L": "She listened to no voice; she accepted no correction. She did not trust in the LORD; she did not draw near to her God.",
      "M": "She has not listened to any voice; she has accepted no correction. She has not trusted in the LORD; she has not drawn near to her God.",
      "T": "She has heard every warning — and ignored them all. She has refused correction. She has placed no trust in Yahweh and made no move toward her God. Four failures: deaf, unteachable, faithless, estranged."
    },
    "3": {
      "L": "Her officials within her are roaring lions; her judges are evening wolves that leave nothing for the morning.",
      "M": "Her officials within her are roaring lions; her judges are wolves of the evening that leave no bone by morning.",
      "T": "Her officials are roaring lions — authority put to work devouring. Her judges are wolves at dusk, tearing through the night and leaving not a scrap for morning. Those appointed to protect are the predators."
    },
    "4": {
      "L": "Her prophets are reckless, faithless men; her priests have profaned the sanctuary; they have done violence to the law.",
      "M": "Her prophets are reckless and treacherous; her priests have defiled the sanctuary and done violence to the law.",
      "T": "Her prophets are reckless frauds. Her priests have treated the sanctuary as though it were nothing — desecrating it — and have done violence to the very law they were appointed to guard."
    },
    "5": {
      "L": "The LORD within her is righteous; he does no injustice; every morning he brings his justice to light — he does not fail — but the unjust person knows no shame.",
      "M": "The LORD within her is righteous; he does no wrong. Morning after morning he brings his justice to light; he never fails. Yet the unjust person feels no shame.",
      "T": "And yet — Yahweh himself is in her midst, just and unswerving. Every single morning he brings his righteous verdict into the light; he never misses an injustice. But the crooked feel nothing. No shame reaches them at all."
    },
    "6": {
      "L": "I have cut off nations; their corner towers are in ruins; I have laid waste their streets so that none walks in them; their cities are devastated, with no man, no inhabitant.",
      "M": "I have cut off nations; their corner towers lie in ruins; I have laid their streets waste so that no one passes through. Their cities are destroyed — no one remains, no one lives there.",
      "T": "I have already done it to nations before you: towers broken, streets emptied, cities reduced to silence — no one left to walk them. This is what judgment looks like. I did it. Remember."
    },
    "7": {
      "L": "I said, 'Surely you will fear me; you will accept correction. Your dwelling will not be cut off according to all that I appointed against you.' But they were eager to make all their deeds corrupt.",
      "M": "I said, 'Surely you will fear me now; you will accept instruction. Your home will not be cut off — despite all the punishment I have brought against you.' But they rose early and made all their actions corrupt.",
      "T": "I kept thinking: Surely this will finally break through — surely she will fear me, take correction, and then her dwelling will be preserved, whatever it has cost to reach her there. But instead they rose early each morning, eager to heap corruption upon corruption."
    },
    "8": {
      "L": "Therefore wait for me, declares the LORD, until the day I rise up to plunder; for my decision is to gather nations, to assemble kingdoms, to pour out upon them my indignation, all my burning anger; for in the fire of my jealousy all the earth shall be consumed.",
      "M": "Therefore wait for me, declares the LORD, until the day I rise to act; for I have decided to gather the nations, to assemble the kingdoms, to pour out my indignation upon them — all my fierce anger. For the whole earth will be consumed in the fire of my jealousy.",
      "T": "So wait for me — this is Yahweh's word. Wait for the day I rise to claim what is mine. I have determined to gather every nation, assemble every kingdom, and pour out on them the full force of my fury. The earth will be consumed in the fire of my jealous love. This is coming, and it will not be stopped."
    },
    "9": {
      "L": "For at that time I will change the speech of the peoples to a pure speech, that all of them may call upon the name of the LORD and serve him with one accord.",
      "M": "At that time I will give the peoples a pure language, so that all of them may call on the name of the LORD and serve him with one purpose.",
      "T": "Then I will restore to the nations a pure speech — a cleansed and unifying language — so that every people can call on the name of Yahweh and serve him together as one. The division of Babel will be reversed."
    },
    "10": {
      "L": "From beyond the rivers of Cush my worshipers, the daughter of my dispersed ones, shall bring my offering.",
      "M": "From beyond the rivers of Cush, those who worship me — the scattered ones I claimed — will bring me their offerings.",
      "T": "Even from beyond the rivers of Cush — from the far end of the known world — those who belong to me, whom I scattered among the nations, will come back. They will bring their worship to me."
    },
    "11": {
      "L": "On that day you shall not be put to shame because of all the deeds by which you have rebelled against me; for then I will remove from your midst your proudly exulting ones, and you shall no longer be haughty on my holy mountain.",
      "M": "On that day you will not be put to shame for any of the deeds by which you have transgressed against me, for I will remove from your midst your arrogantly boasting ones, and you will no longer be proud on my holy mountain.",
      "T": "On that day your past shame will be lifted — all the rebellion, all the transgression, gone. Because I will have removed from among you the ones drunk on their own importance. On my holy mountain there will be no more strutting, no more arrogance."
    },
    "12": {
      "L": "But I will leave in your midst a people humble and poor, and they shall take refuge in the name of the LORD.",
      "M": "I will leave in your midst a people who are humble and poor; they will find refuge in the name of the LORD.",
      "T": "What I will leave behind will be a people stripped of pretension — humble, poor, with nothing to trust but the name of Yahweh. And that trust will prove more than enough."
    },
    "13": {
      "L": "The remnant of Israel shall do no injustice and speak no lies; a deceitful tongue shall not be found in their mouths. For they shall graze and lie down, and no one shall make them afraid.",
      "M": "The remnant of Israel will commit no wrong and speak no falsehood; a deceitful tongue will not be found among them. They will graze and lie down with no one to make them afraid.",
      "T": "This remnant will be different: no wrongdoing, no lies, no deceit woven through their speech. They will live like a flock at rest — grazing in peace, lying down in safety, with nothing left in all the world to threaten them."
    },
    "14": {
      "L": "Sing aloud, O daughter of Zion! Shout, O Israel! Rejoice and exult with all your heart, O daughter of Jerusalem!",
      "M": "Sing aloud, O daughter of Zion! Shout, O Israel! Rejoice and exult with all your heart, O daughter of Jerusalem!",
      "T": "Sing out, Daughter of Zion — sing at the top of your voice! Shout, Israel! Let your whole heart burst open with joy, Daughter of Jerusalem. The darkness is done."
    },
    "15": {
      "L": "The LORD has taken away your judgments; he has cleared away your enemies. The King of Israel, the LORD, is in your midst; you shall no longer fear evil.",
      "M": "The LORD has set aside your sentences of judgment and driven out your enemies. The King of Israel — the LORD — is in your midst; you will no longer dread disaster.",
      "T": "Yahweh has set aside every verdict against you. He has thrown out your enemies. The King of Israel — Yahweh himself — stands in your midst, and there is no evil left to fear. The charges dropped; the enemy gone; the King present."
    },
    "16": {
      "L": "On that day it shall be said to Jerusalem: 'Fear not, O Zion; do not let your hands hang limp.'",
      "M": "On that day this word will be spoken to Jerusalem: 'Fear not, Zion; do not let your hands go limp.'",
      "T": "On that day a voice will speak to Jerusalem: 'Do not be afraid, Zion. Do not let your hands fall slack — there is still work ahead, and God is doing it.'"
    },
    "17": {
      "L": "The LORD your God is in your midst, a mighty one who saves; he will rejoice over you with gladness; he will be silent in his love; he will exult over you with loud singing.",
      "M": "The LORD your God is in your midst — a warrior who saves. He will rejoice over you with joy; he will be still in his love; he will exult over you with singing.",
      "T": "Yahweh your God is here — right here in your midst — the Mighty One who saves. He is not merely tolerating you; he is rejoicing over you with joy. In his love he holds perfectly still, completely at rest. And then he breaks that silence with singing — exulting over you. The God who judged the nations is singing over his people."
    },
    "18": {
      "L": "I will gather those from you who grieve over the appointed feasts; on them the reproach of it was a burden.",
      "M": "I will gather those who grieve over the sacred festivals — those for whom the reproach was a heavy burden.",
      "T": "I am gathering the ones who grieved in exile — who mourned every sacred feast they could not keep, who have carried the reproach of their captivity like a crushing weight. I see them. I will bring them home."
    },
    "19": {
      "L": "Behold, at that time I will deal with all your oppressors; I will save the lame and gather the outcast; I will give them praise and honor in every land where they were put to shame.",
      "M": "At that time I will deal with all who have oppressed you. I will rescue the lame and gather those who were driven away; I will give them praise and honor in every land where they suffered shame.",
      "T": "At that moment I will settle every score with those who oppressed you. The ones who limped in disgrace, the ones driven out — I will rescue them and bring them home. In every place that once knew their shame, I will give them praise and honor instead. Their story will be rewritten."
    },
    "20": {
      "L": "At that time I will bring you home; at the time when I gather you, I will make you renowned and praised among all the peoples of the earth, when I restore your fortunes before your eyes, says the LORD.",
      "M": "At that time I will bring you home, when I gather you together; I will give you a name and praise among all the peoples of the earth, when I restore your fortunes before your eyes, says the LORD.",
      "T": "When that time comes I will bring you home — gather you in — and give you a name and renown among every people on earth. You will watch with your own eyes as Yahweh turns your captivity around. This is his word. He has spoken it."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'zephaniah')
        merge_tier(existing, ZEPHANIAH, tier_key)
        save(tier_dir, 'zephaniah', existing)
    print('Zephaniah 1–3 written.')

if __name__ == '__main__':
    main()
