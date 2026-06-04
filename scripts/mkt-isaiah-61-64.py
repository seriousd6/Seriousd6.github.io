"""
MKT Isaiah chapters 61–64 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-isaiah-61-64.py

Translation decisions:
- H3068 (יהוה): "LORD" (L/M) / "Yahweh" (T) — carried forward from all prior Isaiah scripts.
- H136 + H3069 (אֲדֹנָי יֱהוִה): "Lord GOD" in all tiers — the Adonai-Yahweh combination,
  standard rendering used throughout Isaiah for this double divine title.
- H430 (אֱלֹהִים): "God" in all tiers throughout.
- H7307 (רוּחַ): capitalised "Spirit" in all tiers when the divine Spirit is clearly meant:
    61:1 — "Spirit of the Lord GOD is upon me" = clear anointing by divine Spirit → "Spirit" (cap.)
    63:10 — "grieved his Holy Spirit" → "Spirit" (cap.)
    63:11 — "his Holy Spirit within them" → "Spirit" (cap.)
    63:14 — "the Spirit of the LORD gave them rest" → "Spirit" (cap.)
    64:6 — "like the wind" (ruach carrying away) → "wind" (lower case) — clearly not divine.
- H2617 (חֶסֶד): "lovingkindnesses" (L, pl. as in 63:7 ḥasdê YHWH); "steadfast love" (M);
  "faithful love" (T). The plural ḥasdê YHWH in 63:7 carries the full covenantal weight of
  God's long faithfulness — T expands to "steadfast lovingkindnesses" to signal the plurality.
- H1350 (גָּאַל): "Redeemer / redeemed" — 63:4,16. In 63:16 it is a divine title used as
  vocative address; T capitalises: "our Redeemer." In 63:4 it is "my redeemed" (the rescued).
- H5315 (נֶפֶשׁ): 61:10 — "my soul shall be joyful" — the embodied self in exultation; L keeps
  "my soul"; M renders "I will exult"; T keeps "my whole self" to honour the Hebraic holism
  without importing Greek immaterial-soul concepts.
- H6664/H6666 (צֶדֶק/צְדָקָה): "righteousness" throughout (L/M). T uses "righteousness" where
  the legal/relational sense is primary; 61:3 "oaks of righteousness" = trees (L) but the idiom
  means people firmly rooted in right standing; 62:1 "righteousness shines out" = saving-vindicating
  action; 64:6 "all our righteous deeds" = human moral performance before God.
- H4941 (מִשְׁפָּט): 61:8 — "justice" in all tiers.
- H1285 (בְּרִית): 61:8 — "covenant" in all tiers.
- H6918 (קָדוֹשׁ יִשְׂרָאֵל): not prominent in these chapters; where "holy" functions as a divine
  name-descriptor (63:15 "your holy and glorious habitation"; 64:10 "your holy cities") it is
  rendered "holy" as adjective only.
- H8057/H7442 (שִׂמְחָה/רָנַן): 61:7 — "everlasting joy"; 61:10 "I will greatly rejoice" — both
  rendered with the full force of Hebrew jubilation.
- H6726 (צִיּוֹן): "Zion" — unchanged throughout.
- H3389 (יְרוּשָׁלַם): "Jerusalem" — unchanged.
- OT / NT echo notes:
  61:1-3 — Quoted by Jesus in Luke 4:18-19 as his inaugural mission statement in Nazareth.
    This is one of the most significant Christological fulfilment passages in the NT. T does not
    add NT gloss but allows the full weight of the "anointed" / "good news to the poor" language
    to stand on its own terms. The interplay of "year of the LORD's favour" (Jubilee language)
    and "day of vengeance" in v.2 is a deliberate pairing: grace and judgment are not opposed —
    grace for some is judgment for others.
  61:10 — "robe of righteousness" and bridegroom / bride imagery prefigures Rev 19:7-8 and
    John 3:29. T preserves the marital joy imagery.
  62:4 — "Hephzibah" (my delight is in her) and "Beulah" (married) — these Hebraic names are
    preserved in T as proper names with translations. They are divine promises embedded in names.
  62:11 — "See, your salvation comes" echoes Zech 9:9 (the triumphal entry text) and is quoted
    in Matt 21:5. T preserves the arrival-announcement form.
  63:1-6 — The divine warrior oracle is one of the most vivid theophany texts in the OT. Rev 19:13
    ("garments dipped in blood") echoes this passage. T renders the dramatic dialogue form explicitly.
  63:9 — "The angel of his presence" (malaʾak pānāyw) — one of the most discussed OT texts on
    divine presence and pre-incarnate mediators. L preserves "angel of his presence" literally.
    M uses "angel of his presence"; T uses the same — resisting both flattening (to "God himself")
    and over-specification.
  63:10 — "grieved his Holy Spirit" — quoted in Eph 4:30 ("do not grieve the Holy Spirit of God").
  63:16 / 64:8 — "You are our Father" — Jesus teaches his disciples to pray "Our Father"; the
    Isaianic base for Father-language about God is here. T honours this by preserving the direct
    address with full covenantal resonance.
  64:4 — "No eye has seen" — cited by Paul in 1 Cor 2:9. T preserves the parallel structure
    (ear / eye) without NT gloss.
- Structural notes:
  Ch. 61 — The Servant's anointed mission statement (vv. 1-3), then the transformation of the
    restored community (vv. 4-9), followed by a hymn of praise (vv. 10-11). The triple exchange
    in v.3 (garland/ashes, oil of joy/mourning, garment of praise/faint spirit) is liturgical
    and deliberate — T preserves it as a three-line structure.
  Ch. 62 — Yahweh's vow of relentless intercession for Zion (vv. 1-5), the watchmen commission
    (vv. 6-7), the oath against foreign exploitation (vv. 8-9), and the eschatological herald
    cry (vv. 10-12). T breaks the poetry into lines throughout.
  Ch. 63 — Tripartite: the divine warrior from Edom (vv. 1-6, high dramatic dialogue), the hymn
    of recollection / Israel's lament (vv. 7-14), and the intercessory prayer (vv. 15-19).
    The lament-prayer continues into ch. 64 — these two chapters form one continuous intercessory
    unit, among the most theologically rich in all the OT prophets.
  Ch. 64 — The lament continues: theophany plea (vv. 1-3), appeal to God's uniqueness (v.4),
    confession of sin and unworthiness (vv. 5-7), the potter/clay image (v.8), and a closing
    appeal to look on the ruins (vv. 9-12). T preserves the emotional arc: awe → yearning →
    confession → hope.
- Aspect notes:
  61:1 imperfects (divine commission): ongoing sent-ness — present aspect in L.
  62:1 "I will not be silent" — cohortative first-person vow — rendered as solemn declaration.
  63:3 "I have trodden" — perfect aspect (completed past act with present result visible on garments).
  63:7 — the deliberate move from past acts of ḥesed to future implications.
  64:1 "would rend" — jussive wishing construction (oh that you would…) — rendered as longing.
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
            if v not in existing[ch]:
                existing[ch][v] = tiers[tier_key]

ISAIAH = {
  "61": {
    "1": {
      "L": "The Spirit of the Lord GOD is upon me, because the LORD has anointed me to bring good news to the poor; he has sent me to bind up the brokenhearted, to proclaim liberty to the captives and the opening of the prison to those who are bound,",
      "M": "The Spirit of the Lord GOD is upon me, because the LORD has anointed me to bring good news to the afflicted; he has sent me to bind up the brokenhearted, to proclaim freedom to the captives and the opening of prison to those who are bound,",
      "T": "The Spirit of the Lord GOD is upon me —\nbecause Yahweh has anointed me\nto bring good news to the poor.\nHe has sent me to bind up the brokenhearted,\nto proclaim liberty to the captives\nand the opening of the prison to those who are bound,"
    },
    "2": {
      "L": "to proclaim the year of the LORD's favor, and the day of vengeance of our God; to comfort all who mourn;",
      "M": "to proclaim the year of the LORD's favor and the day of vengeance of our God; to comfort all who mourn;",
      "T": "to proclaim the year of Yahweh's favor —\nand the day of vengeance of our God —\nto comfort all who mourn;"
    },
    "3": {
      "L": "to appoint to those who mourn in Zion — to give them a garland instead of ashes, the oil of joy instead of mourning, the garment of praise instead of a faint spirit; that they may be called oaks of righteousness, the planting of the LORD, that he might be glorified.",
      "M": "to bestow on those who mourn in Zion — to give them a garland instead of ashes, the oil of joy instead of mourning, the garment of praise instead of a spirit of despair; so that they may be called oaks of righteousness, the planting of the LORD, for his glory.",
      "T": "to bestow on those who mourn in Zion —\na garland instead of ashes,\nthe oil of joy instead of mourning,\nthe garment of praise instead of a spirit of despair.\nThey will be called oaks of righteousness —\nthe planting of Yahweh — for his glory."
    },
    "4": {
      "L": "They shall build up the ancient ruins; they shall raise up the former desolations; they shall repair the devastated cities, the desolations of many generations.",
      "M": "They will rebuild the ancient ruins; they will raise up the former desolations; they will restore the cities that were devastated, the ruins of many generations.",
      "T": "They will rebuild the ancient ruins.\nThey will raise up the former desolations.\nThey will restore the devastated cities — the ruins of generation after generation."
    },
    "5": {
      "L": "Strangers shall stand and tend your flocks; foreigners shall be your plowmen and your vinedressers.",
      "M": "Strangers will stand and tend your flocks; foreigners will be your farmers and your vinedressers.",
      "T": "Strangers will stand and tend your flocks; foreigners will farm your fields and work your vineyards."
    },
    "6": {
      "L": "but you shall be called the Priests of the LORD; they shall speak of you as the Ministers of our God; you shall eat the wealth of the nations, and in their glory you shall boast.",
      "M": "But you will be called the Priests of the LORD; you will be named the Ministers of our God; you will eat the wealth of the nations, and in their glory you will boast.",
      "T": "But you — you will be called the Priests of Yahweh; people will name you Ministers of our God. You will feast on the wealth of nations; in their honor you will take pride."
    },
    "7": {
      "L": "Instead of your shame there shall be a double portion; instead of dishonor they shall rejoice in their lot; therefore in their land they shall possess a double portion; everlasting joy shall be theirs.",
      "M": "Instead of shame you will receive a double portion; instead of dishonor you will rejoice in your inheritance; therefore you will possess a double portion in your land; everlasting joy will be yours.",
      "T": "Instead of shame — a double portion.\nInstead of dishonor — joy in your inheritance.\nYou will possess double in your land.\nEverlasting joy will be yours."
    },
    "8": {
      "L": "For I the LORD love justice; I hate robbery and iniquity; I will faithfully give them their recompense, and I will make an everlasting covenant with them.",
      "M": "For I, the LORD, love justice; I hate robbery and wrongdoing; I will faithfully give them their reward, and I will make an everlasting covenant with them.",
      "T": "For I, Yahweh, love justice. I hate robbery and iniquity. I will faithfully give them their reward, and I will make an everlasting covenant with them."
    },
    "9": {
      "L": "Their offspring shall be known among the nations, and their descendants in the midst of the peoples; all who see them shall acknowledge them, that they are an offspring the LORD has blessed.",
      "M": "Their descendants will be known among the nations, and their offspring among the peoples; all who see them will recognize that they are a people the LORD has blessed.",
      "T": "Their descendants will be known among the nations, their offspring among the peoples. All who see them will acknowledge: these are the people Yahweh has blessed."
    },
    "10": {
      "L": "I will greatly rejoice in the LORD; my soul shall be joyful in my God, for he has clothed me with the garments of salvation; he has covered me with the robe of righteousness, as a bridegroom decks himself with a garland, and as a bride adorns herself with her jewels.",
      "M": "I will greatly rejoice in the LORD; my soul will exult in my God, for he has clothed me with the garments of salvation; he has wrapped me in the robe of righteousness, as a bridegroom adorns himself with a garland, and as a bride adorns herself with her jewels.",
      "T": "I will greatly rejoice in Yahweh;\nmy whole self will exult in my God —\nfor he has clothed me with the garments of salvation;\nhe has wrapped me in the robe of righteousness,\nas a bridegroom crowns himself with a garland,\nas a bride adorns herself with jewels."
    },
    "11": {
      "L": "For as the earth brings forth its sprouts, and as a garden causes what is sown in it to spring up, so the Lord GOD will cause righteousness and praise to spring up before all the nations.",
      "M": "For as the earth brings forth its sprouts, and as a garden makes what is planted in it spring up, so the Lord GOD will make righteousness and praise spring up before all the nations.",
      "T": "As the earth brings forth its growth, as a garden makes its seeds spring up — so the Lord GOD will cause righteousness and praise to spring up before all the nations."
    }
  },
  "62": {
    "1": {
      "L": "For Zion's sake I will not keep silent, and for Jerusalem's sake I will not be still, until her righteousness goes out as brightness, and her salvation as a burning torch.",
      "M": "For Zion's sake I will not keep silent, and for Jerusalem's sake I will not rest, until her righteousness shines out as brightness and her salvation blazes like a torch.",
      "T": "For Zion's sake I will not keep silent.\nFor Jerusalem's sake I will not be still —\nnot until her righteousness blazes out like the dawn,\nnot until her salvation burns like a torch."
    },
    "2": {
      "L": "The nations shall see your righteousness, and all the kings your glory, and you shall be called by a new name that the mouth of the LORD will give.",
      "M": "The nations will see your righteousness and all the kings your glory; you will be called by a new name that the LORD himself will bestow.",
      "T": "The nations will see your righteousness; every king will see your glory. You will be called by a new name — a name Yahweh's own mouth will speak."
    },
    "3": {
      "L": "You shall be a crown of beauty in the hand of the LORD, and a royal diadem in the hand of your God.",
      "M": "You will be a crown of beauty in the hand of the LORD and a royal diadem in the hand of your God.",
      "T": "You will be a glorious crown in the hand of Yahweh — a royal diadem in the hand of your God."
    },
    "4": {
      "L": "You shall no more be called Forsaken, and your land shall no more be called Desolate; but you shall be called My Delight Is in Her, and your land Married; for the LORD delights in you, and your land shall be espoused.",
      "M": "You will no longer be called Forsaken, nor your land Desolate; but you will be called My Delight Is in Her, and your land Married; for the LORD delights in you, and your land will be wedded.",
      "T": "No more will they call you Forsaken.\nNo more will your land be called Desolate.\nYou will be called Hephzibah — 'My Delight Is in Her' —\nand your land Beulah — 'Married' —\nfor Yahweh delights in you,\nand your land will be wed."
    },
    "5": {
      "L": "For as a young man marries a young woman, so shall your sons marry you, and as the bridegroom rejoices over the bride, so shall your God rejoice over you.",
      "M": "For as a young man marries a young woman, so your sons will marry you; and as a bridegroom rejoices over his bride, so your God will rejoice over you.",
      "T": "As a young man takes a young woman as his own, so your sons will take you. As the bridegroom exults over his bride, so your God will exult over you."
    },
    "6": {
      "L": "On your walls, O Jerusalem, I have set watchmen; all the day and all the night they shall never be silent. You who put the LORD in remembrance, take no rest,",
      "M": "On your walls, O Jerusalem, I have stationed watchmen; they will never be silent day or night. You who remind the LORD, give yourselves no rest,",
      "T": "On your walls, Jerusalem, I have posted watchmen.\nAll day and all night, they must never fall silent.\nYou who call Yahweh to remembrance — take no rest,"
    },
    "7": {
      "L": "and give him no rest until he establishes Jerusalem and makes it a praise in the earth.",
      "M": "and give him no rest until he establishes Jerusalem and makes her a glory in the earth.",
      "T": "give him no rest until he establishes Jerusalem\nand makes her the praise of all the earth."
    },
    "8": {
      "L": "The LORD has sworn by his right hand and by his mighty arm: I will not again give your grain to your enemies for food, nor shall foreigners drink your new wine for which you have labored;",
      "M": "The LORD has sworn by his right hand and by his strong arm: Never again will I give your grain to your enemies as food, nor will foreigners drink the new wine for which you have labored;",
      "T": "Yahweh has sworn by his right hand — by his powerful arm: I will never again hand your grain to your enemies for food. Foreigners will not drink the new wine you toiled to produce."
    },
    "9": {
      "L": "but those who harvest it shall eat it and praise the LORD, and those who gather it shall drink it in the courts of my sanctuary.",
      "M": "but those who have gathered it will eat it and praise the LORD, and those who bring it in will drink it in the courts of my sanctuary.",
      "T": "Those who harvest it will eat it and praise Yahweh. Those who gather it in will drink it in the courts of my sanctuary."
    },
    "10": {
      "L": "Go through, go through the gates; prepare the way for the people; build up, build up the highway; clear it of stones; lift up a signal over the peoples.",
      "M": "Pass through, pass through the gates; prepare the way for the people; build up the highway, clear it of stones; raise a banner over the nations.",
      "T": "Go through, go through the gates!\nPrepare the way for the people!\nBuild up the highway — clear it of stones!\nLift a banner over the nations!"
    },
    "11": {
      "L": "Behold, the LORD has proclaimed to the end of the earth: Say to daughter Zion, 'Behold, your salvation comes; behold, his reward is with him, and his recompense before him.'",
      "M": "The LORD has declared to the ends of the earth: Say to daughter Zion, 'See, your salvation is coming; his reward is with him and his recompense before him.'",
      "T": "Yahweh has proclaimed to the ends of the earth — say to daughter Zion: Look, your salvation is coming! His reward is with him; his recompense goes before him."
    },
    "12": {
      "L": "And they shall be called The Holy People, The Redeemed of the LORD; and you shall be called Sought Out, A City Not Forsaken.",
      "M": "They will be called the Holy People, the Redeemed of the LORD; and you will be named Sought Out, A City Not Forsaken.",
      "T": "They will be called the Holy People — the Redeemed of Yahweh. And you will be called Sought Out: A City Not Forsaken."
    }
  },
  "63": {
    "1": {
      "L": "Who is this who comes from Edom, with crimsoned garments from Bozrah, this one who is glorious in his apparel, marching in the greatness of his strength? It is I, speaking in righteousness, mighty to save.",
      "M": "Who is this coming from Edom, with garments reddened from Bozrah — this one glorious in his attire, striding forward in his great strength? I am the one who speaks in righteousness, mighty to save.",
      "T": "Who is this coming from Edom —\ngarments dyed deep red from Bozrah —\nthis one glorious in his attire,\nstriding forward in his great might?\n'I am the one who speaks in righteousness —\nmighty to save.'"
    },
    "2": {
      "L": "Why is your apparel red, and your garments like one who treads in the winepress?",
      "M": "Why are your garments red, as if you had been treading in a winepress?",
      "T": "'Why are your garments red —\nyour clothes like someone who treads in the winepress?'"
    },
    "3": {
      "L": "I have trodden the winepress alone, and from the peoples no one was with me; I trod them in my anger and trampled them in my wrath; their lifeblood is sprinkled on my garments, and I have stained all my apparel.",
      "M": "I have trodden the winepress alone, and from the nations no one helped me; I trod them in my anger and trampled them in my fury; their blood is sprinkled on my garments, and I have stained all my clothing.",
      "T": "'I trod the winepress alone.\nFrom all the nations, no one helped me.\nI trod them in my anger;\nI trampled them in my fury.\nTheir blood is sprinkled on my garments;\nI have stained all my clothing."
    },
    "4": {
      "L": "For the day of vengeance was in my heart, and the year of my redeemed had come.",
      "M": "For the day of vengeance was in my heart, and the year of my redemption had arrived.",
      "T": "The day of vengeance was in my heart —\nand the year of my redeemed had come."
    },
    "5": {
      "L": "I looked, but there was no one to help; I was appalled, but there was none to uphold; so my own arm brought me salvation, and my wrath upheld me.",
      "M": "I looked, but there was no one to help; I was appalled that there was none to sustain me; so my own arm brought salvation, and my fury sustained me.",
      "T": "I looked — but there was no one to help.\nI was appalled that no one sustained me.\nSo my own arm brought me salvation;\nmy own fury upheld me.'"
    },
    "6": {
      "L": "I trod down the peoples in my anger; I made them drunk in my fury, and I poured out their lifeblood on the earth.",
      "M": "I trampled the peoples in my anger; I made them drunk in my fury, and I poured their blood down to the ground.",
      "T": "I trampled the peoples in my anger;\nI made them drunk in my fury;\nI poured their blood down to the earth."
    },
    "7": {
      "L": "I will recount the lovingkindnesses of the LORD and the praises of the LORD, according to all that the LORD has granted us, and the great goodness to the house of Israel that he has granted them according to his compassion and the abundance of his steadfast loves.",
      "M": "I will recount the steadfast lovingkindnesses of the LORD and his praises, for all that the LORD has bestowed on us — the great goodness to the house of Israel that he granted them according to his compassion and his abundant steadfast love.",
      "T": "I will recount the steadfast lovingkindnesses of Yahweh —\nthe praises of Yahweh —\nfor all that Yahweh has done for us:\nthe great goodness he showed to the house of Israel,\nbestowed according to his compassion,\naccording to the abundance of his faithful love."
    },
    "8": {
      "L": "For he said, 'Surely they are my people, children who will not act falsely'; and he became their Savior.",
      "M": "For he said, 'Surely they are my people, children who will not prove false'; and so he became their Savior.",
      "T": "He said, 'Surely these are my people — children who will not prove false.' And so he became their Savior."
    },
    "9": {
      "L": "In all their affliction he was afflicted, and the angel of his presence saved them; in his love and in his pity he redeemed them; he lifted them up and carried them all the days of old.",
      "M": "In all their affliction he was afflicted, and the angel of his presence saved them; in his love and compassion he redeemed them; he lifted them up and carried them through all the days of old.",
      "T": "In all their affliction, he too was afflicted.\nThe angel of his presence saved them.\nIn his love and compassion he redeemed them;\nhe lifted them up and carried them\nthrough all the days of old."
    },
    "10": {
      "L": "But they rebelled and grieved his Holy Spirit; therefore he was turned to be their enemy, and himself fought against them.",
      "M": "But they rebelled and grieved his Holy Spirit; so he turned against them as their enemy and himself fought against them.",
      "T": "But they rebelled and grieved his Holy Spirit — and he turned to be their enemy; he himself fought against them."
    },
    "11": {
      "L": "Then he remembered the days of old, of Moses and his people. Where is he who brought them up out of the sea with the shepherds of his flock? Where is he who put in the midst of them his Holy Spirit,",
      "M": "Then he remembered the ancient days, the time of Moses and his people. Where is the one who brought them up out of the sea with the shepherd of his flock? Where is the one who placed his Holy Spirit among them,",
      "T": "Then he remembered the ancient days — the time of Moses and his people. Where is the one who brought them up from the sea with the shepherd of his flock? Where is the one who placed his Holy Spirit in their midst —"
    },
    "12": {
      "L": "who led Moses by the right hand with his glorious arm, who divided the waters before them to make for himself an everlasting name,",
      "M": "who led Moses by the right hand with his glorious arm, dividing the waters before them to make an everlasting name for himself,",
      "T": "who led Moses by his glorious right arm — who divided the waters before them to win for himself an everlasting name —"
    },
    "13": {
      "L": "who led them through the depths? Like a horse in the desert, they did not stumble.",
      "M": "who led them through the depths? Like a horse in the desert, they did not stumble.",
      "T": "who led them through the deep as a horse walks through the desert, never stumbling —"
    },
    "14": {
      "L": "Like livestock that go down into the valley, the Spirit of the LORD gave them rest. So you led your people, to make for yourself a glorious name.",
      "M": "As cattle descend into a valley to rest, the Spirit of the LORD gave them rest. So you led your people to make yourself a glorious name.",
      "T": "as cattle go down into the valley to rest.\nThe Spirit of Yahweh gave them rest.\nSo you led your people —\nto make for yourself a glorious name."
    },
    "15": {
      "L": "Look down from heaven and see, from your holy and glorious habitation. Where is your zeal and your might? The stirring of your inner being and your compassion are withheld from me.",
      "M": "Look down from heaven and see, from your holy and glorious dwelling. Where are your zeal and your strength? The yearning of your heart and your compassion are withheld from me.",
      "T": "Look down from heaven and see —\nfrom your holy and glorious dwelling.\nWhere is your zeal?\nWhere is your might?\nThe yearning of your compassion and mercy toward me — it is withheld."
    },
    "16": {
      "L": "For you are our Father, though Abraham does not know us and Israel does not acknowledge us; you, O LORD, are our Father, our Redeemer from of old is your name.",
      "M": "For you are our Father, though Abraham does not know us and Israel does not acknowledge us; you, LORD, are our Father; our Redeemer from of old — that is your name.",
      "T": "You are our Father —\neven if Abraham does not know us,\neven if Israel does not recognize us.\nYou, Yahweh, are our Father.\nOur Redeemer from of old — that is your name."
    },
    "17": {
      "L": "O LORD, why do you make us wander from your ways and harden our heart, so that we do not fear you? Return for the sake of your servants, the tribes of your heritage.",
      "M": "LORD, why do you let us stray from your ways and harden our hearts from fearing you? Turn back for the sake of your servants, the tribes of your inheritance.",
      "T": "Yahweh — why do you let us wander from your ways?\nWhy do you harden our heart so we no longer fear you?\nTurn back — for the sake of your servants,\nthe tribes of your inheritance."
    },
    "18": {
      "L": "Your holy people held possession of your sanctuary for a little while; our adversaries have trampled down your sanctuary.",
      "M": "Your holy people possessed your sanctuary for a little while; now our adversaries have trampled it down.",
      "T": "Your holy people held your sanctuary for only a little while — now our adversaries have trampled it down."
    },
    "19": {
      "L": "We have become like those over whom you have never ruled, like those who are not called by your name.",
      "M": "We have become like those you never ruled, like those who were never called by your name.",
      "T": "We have become like those you never ruled — like those who were never called by your name."
    }
  },
  "64": {
    "1": {
      "L": "Oh that you would rend the heavens and come down, that the mountains might quake at your presence —",
      "M": "Oh, that you would tear open the heavens and come down, that the mountains would quake at your presence —",
      "T": "Oh, that you would tear the heavens open and come down —\nthat the mountains would shudder at your presence —"
    },
    "2": {
      "L": "as fire kindles brushwood and causes water to boil — to make your name known to your enemies, and that the nations might tremble at your presence!",
      "M": "as when fire kindles brushwood and water boils — to make your name known to your enemies, so that the nations would tremble at your presence!",
      "T": "as fire sets the dry wood ablaze,\nas fire makes water boil —\nmake your name known to your enemies!\nLet the nations tremble before you!"
    },
    "3": {
      "L": "When you did awesome things that we did not expect, you came down, the mountains quaked at your presence.",
      "M": "When you did awe-inspiring things we did not expect, you came down; the mountains quaked at your presence.",
      "T": "When you did those awesome things we never expected — you came down! The mountains shuddered at your presence."
    },
    "4": {
      "L": "From of old no one has heard, no ear has perceived, no eye has seen a God besides you, who acts for those who wait for him.",
      "M": "From ancient times no one has heard, no ear has perceived, no eye has seen any God besides you, who acts on behalf of those who wait for him.",
      "T": "From of old no one has heard it —\nno ear perceived it,\nno eye has seen a God besides you\nwho acts for those who wait for him."
    },
    "5": {
      "L": "You meet him who rejoices in doing righteousness, those who remember you in your ways. Behold, you were angry, and we sinned; in our sins we have long continued, and how then can we be saved?",
      "M": "You come to the aid of those who joyfully do right, those who remember you in your ways. But you were angry, and we sinned; in our sins we have long continued — and how can we be saved?",
      "T": "You come to meet the one who rejoices in doing right,\nwho remembers you in your ways.\nYou were angry — and we sinned.\nWe have long continued in our sins.\nCan we still be saved?"
    },
    "6": {
      "L": "We have all become like one who is unclean, and all our righteous deeds are like a polluted garment; we all fade like a leaf, and our iniquities, like the wind, take us away.",
      "M": "We have all become like one who is unclean; all our righteous deeds are like a filthy rag; we all wither like a leaf, and our iniquities, like the wind, sweep us away.",
      "T": "We have all become like the unclean.\nAll our righteous deeds are like a filthy garment.\nWe fade like a leaf —\nand our iniquities, like a wind, carry us away."
    },
    "7": {
      "L": "There is no one who calls upon your name, who rouses himself to take hold of you; for you have hidden your face from us, and have made us melt in the hand of our iniquities.",
      "M": "There is no one who calls on your name, who stirs himself to take hold of you; for you have hidden your face from us and given us over to the power of our iniquities.",
      "T": "No one calls on your name;\nno one stirs himself to take hold of you.\nFor you have hidden your face from us\nand given us over to the power of our iniquities."
    },
    "8": {
      "L": "But now, O LORD, you are our Father; we are the clay, and you are our potter; we are all the work of your hand.",
      "M": "But now, LORD, you are our Father; we are the clay, and you are our potter; we are all the work of your hands.",
      "T": "And yet — you are our Father, Yahweh.\nWe are the clay; you are our potter.\nWe are all the work of your hands."
    },
    "9": {
      "L": "Be not so very angry, O LORD, and remember not iniquity forever. Behold, please look — we are all your people.",
      "M": "Do not be exceedingly angry, LORD; do not remember iniquity forever. Please look — we are all your people.",
      "T": "Do not be furious beyond measure, Yahweh.\nDo not remember iniquity forever.\nLook — we are all your people."
    },
    "10": {
      "L": "Your holy cities have become a wilderness; Zion has become a wilderness, Jerusalem a desolation.",
      "M": "Your holy cities have become a wasteland; Zion is a wilderness, Jerusalem a desolation.",
      "T": "Your holy cities are a wasteland.\nZion is a wilderness;\nJerusalem — a desolation."
    },
    "11": {
      "L": "Our holy and beautiful house, where our fathers praised you, has been burned with fire, and all our pleasant places have become ruins.",
      "M": "Our holy and glorious house where our fathers praised you has been burned with fire, and all our cherished places have become desolate.",
      "T": "Our holy and glorious house —\nwhere our fathers praised you —\nhas been burned to the ground.\nAll our cherished places are laid waste."
    },
    "12": {
      "L": "Will you restrain yourself at these things, O LORD? Will you keep silent, and afflict us so severely?",
      "M": "Will you hold yourself back for all this, LORD? Will you keep silent while you afflict us so grievously?",
      "T": "Will you hold yourself back in the face of all this, Yahweh?\nWill you keep silent while you afflict us so grievously?"
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'isaiah')
        merge_tier(existing, ISAIAH, tier_key)
        save(tier_dir, 'isaiah', existing)
    print('Isaiah 61–64 written.')

if __name__ == '__main__':
    main()
