"""
MKT Obadiah chapter 1 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-obadiah-1-1.py

=== BOOK OVERVIEW ===

Obadiah is the shortest book in the Old Testament: a single chapter, 21 verses.
It is an oracle of judgment against Edom (= Esau), Judah's perennial enemy and
blood relative, for its role in Jerusalem's fall — standing by, gloating, blocking
escape routes, and plundering. The oracle pivots in v.15 from Edom's judgment
to the universal Day of the LORD, and closes (vv.17–21) with a vision of Israel's
restoration and the kingdom's consummation under Yahweh.

The book is almost entirely prophetic poetry, with strong parallelism. The T tier
uses line breaks throughout to honour this structure.

=== CONTESTED-TERM DECISIONS ===

- H3068 (יהוה / Yahweh): Following established convention from Joel and all prior OT books.
  L/M: "LORD" (small-caps convention). T: "Yahweh" in oracle-introduction and
  eschatological passages (vv.1, 4, 8, 15, 18, 21); "the LORD" in v.16 closing line.

- H136 (אֲדֹנָי / Adonai): In v.1, the Hebrew has אֲדֹנָי יְהוִה (Adonai YHWH).
  Standard rendering: "the Lord GOD" in all tiers (Adonai = Lord, YHWH = GOD in
  this compound).

- H123 (אֱדוֹם / Edom) and H6215 (עֵשָׂו / Esau): Both names designate the same
  people and nation. The text uses them interchangeably for poetic variation.
  All tiers preserve both names exactly where the Hebrew has them — no collapsing.

- H2555 (חָמָס / hamas): "violence" in all tiers (v.10). This is covenant-breaking
  violent treachery — stronger than mere force. L/M: "violence." T: "violence" with
  context supplied by the surrounding verse.

- H1285 (בְּרִית / berit) in v.7: Here it refers to a political treaty (covenant
  of alliance), not the Mosaic covenant. L: "covenant" (preserves the lexical word).
  M: "treaty" (contextually accurate). T: "treaty-partners / allies" (surfaces the
  diplomatic betrayal dynamic).

- Day of the LORD (יוֹם יְהוָה, v.15): Following Joel's convention.
  L/M: "the day of the LORD" (lowercase standard). T: "the Day of the LORD"
  (capitalised to signal the eschatological weight).

- The repeated אַל + jussive in vv.12–14 (eight prohibitions): Hebrew uses the
  prohibitive particle with jussive (negative command) referring to past action
  Edom already performed. The English idiom "you should not have..." captures the
  moral force of prohibition-as-accusation. L preserves a closer rendering;
  M/T use "you should not have..." throughout.

- H5955 (עֹלֵלָה / gleanings, v.5): The gleanings left by harvesters (Lev 19:9–10
  requires leaving them for the poor). L/M: "gleanings." T: supplies the social
  context.

- H5614 (סְפָרַד / Sepharad, v.20): Location uncertain — ancient proposals include
  Sardis (Lydia), Media, or Spain (hence Spanish "Sephardim"). All tiers preserve
  "Sepharad" as a proper noun; T notes the diaspora-pointing character.

- H6726 (צִיּוֹן / Zion): "Mount Zion" or "Zion" throughout — no change across tiers.
  It is both the physical mountain and the symbolic seat of Yahweh's reign.

- Aspect notes:
  The oracle uses Hebrew perfects for certainty of the future (prophetic perfect —
  the judgment is so certain it speaks as already done). L renders these as simple
  future ("shall be"); M follows suit; T occasionally notes the certainty with phrasing
  like "has sealed it" or similar.
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


OBADIAH = {
    "1": {
        "1": {
            "L": "The vision of Obadiah. Thus says the Lord GOD concerning Edom: A report we have heard from the LORD, and a messenger among the nations has been sent: 'Arise! And let us rise up against her for battle!'",
            "M": "The vision of Obadiah. This is what the Lord GOD says about Edom: We have heard a report from the LORD, and a herald has been sent among the nations: 'Rise up! Let us go to war against her!'",
            "T": "The vision of Obadiah.\nThus speaks the Lord GOD concerning Edom:\nA summons has gone out from Yahweh;\na herald races among the nations —\n'Rise up! Let us march against her!'"
        },
        "2": {
            "L": "Behold, small among the nations I have made you; you are greatly despised.",
            "M": "Look — I have made you the least among the nations; you are utterly despised.",
            "T": "See what I have done:\nI have made you the least of nations —\nan object of contempt among them all."
        },
        "3": {
            "L": "The pride of your heart has deceived you, O dweller in the clefts of the rock, in the height of your dwelling, who says in his heart, 'Who will bring me down to the ground?'",
            "M": "The pride of your heart has deceived you — you who live in the clefts of the rock, who make your home on the heights, saying to yourself, 'Who can bring me down to earth?'",
            "T": "Pride has deceived you through and through.\nYou nest in the mountain crevices;\nyou make your home in the heights\nand say to yourself: 'Who can drag me down?'\nBut it is pride itself that has blinded you."
        },
        "4": {
            "L": "Though you exalt yourself like the eagle, and though among the stars your nest is set, from there I will bring you down — declares the LORD.",
            "M": "Even if you soar as high as the eagle, even if your nest is set among the stars, from there I will bring you down — declares the LORD.",
            "T": "Soar like the eagle if you can;\nset your nest among the very stars —\nfrom there Yahweh will pull you down.\nThe LORD has declared it."
        },
        "5": {
            "L": "If thieves came to you, if robbers by night — how you are destroyed! — would they not steal only until they had enough? If grape-gatherers came to you, would they not leave gleanings?",
            "M": "If thieves came to you — robbers by night — how you have been ruined! — would they not steal only what they wanted? If grape-gatherers came to you, would they not leave some gleanings?",
            "T": "Thieves take only enough and leave the rest.\nHarvesters strip a vineyard but leave gleanings behind.\nBut you, Edom — you have been stripped utterly bare,\nnothing left, nothing overlooked.\nHow completely you have been destroyed!"
        },
        "6": {
            "L": "How the things of Esau have been searched out! His hidden treasures sought up!",
            "M": "How thoroughly Esau has been ransacked! His hidden stores laid bare!",
            "T": "Every cache Esau had has been tracked down;\nnot a single hidden store escaped the plunderer's eye."
        },
        "7": {
            "L": "All the men of your covenant have sent you to the border; the men of your peace have deceived you and prevailed against you; those who eat your bread have laid a trap under you — there is no understanding in him.",
            "M": "All your treaty-allies have driven you to the border; those at peace with you have deceived you and overpowered you; those who shared your food have set a snare beneath you — there is no discernment left in Edom.",
            "T": "Every nation you trusted as an ally\nhas pushed you to the frontier and abandoned you there.\nYour friends deceived you and got the upper hand.\nThe ones who broke bread with you were the ones who laid the trap.\nNot a shred of wisdom remained in Edom — none saw it coming."
        },
        "8": {
            "L": "Will I not in that day — declares the LORD — destroy the wise men from Edom and understanding from the mount of Esau?",
            "M": "Will I not on that day — declares the LORD — destroy the wise men from Edom and all understanding from the mount of Esau?",
            "T": "On that day — Yahweh's own word —\nevery sage in Edom will be swept away;\nno wisdom, no counsel, no discernment\nwill remain on the highland of Esau."
        },
        "9": {
            "L": "And your warriors shall be dismayed, O Teman, so that every man from the mount of Esau shall be cut off by slaughter.",
            "M": "Your warriors will be shattered, O Teman, so that every man in the mount of Esau will be cut off by slaughter.",
            "T": "Even your warriors, O Teman, will be struck with terror —\nand every man on Esau's mountain\nwill fall to the slaughter."
        },
        "10": {
            "L": "For your violence against your brother Jacob, shame shall cover you, and you shall be cut off forever.",
            "M": "Because of the violence done to your brother Jacob, shame shall cover you, and you shall be cut off forever.",
            "T": "Your violence against Jacob — your own brother —\nhas sealed your verdict.\nShame will wrap itself around you like a burial shroud,\nand you will be erased from history forever."
        },
        "11": {
            "L": "In the day you stood aloof, in the day strangers carried away his wealth and foreigners entered his gates and cast lots over Jerusalem — even you were like one of them.",
            "M": "On the day you stood aside, when strangers carried off his wealth and foreigners entered his gates and cast lots over Jerusalem — you were like one of them.",
            "T": "That day you stood at a distance and watched.\nStrangers carried off the city's wealth;\nforeigners walked through the gates;\nthey threw dice over Jerusalem.\nYou stood apart and did nothing —\nand that silence made you one of the invaders."
        },
        "12": {
            "L": "You should not have looked on the day of your brother, on the day of his misfortune; you should not have rejoiced over the people of Judah on the day of their ruin; you should not have opened your mouth proudly on the day of distress.",
            "M": "You should not have gloated over your brother on the day of his misfortune; you should not have rejoiced over the people of Judah on the day of their ruin; you should not have spoken so arrogantly on the day of their distress.",
            "T": "Three failures on the day your brother fell:\nYou should not have stood there gloating.\nYou should not have celebrated Judah's collapse.\nYou should not have opened your mouth in triumph\non the very day they were in agony."
        },
        "13": {
            "L": "You should not have entered the gate of my people on the day of their calamity; you should not have looked on their affliction on the day of their calamity; you should not have laid hands on their wealth on the day of their calamity.",
            "M": "You should not have entered the gate of my people on the day of their calamity; you should not have looked on their disaster on the day of their calamity; you should not have seized their goods on the day of their calamity.",
            "T": "Three more on that same dark day:\nYou should not have marched through Jerusalem's gate.\nYou should not have feasted your eyes on their ruin.\nYou should not have stretched out your hand to plunder.\nEach act on the day of their calamity. Each one a betrayal of brotherhood."
        },
        "14": {
            "L": "You should not have stood at the crossroads to cut off his fugitives; you should not have delivered up his survivors on the day of distress.",
            "M": "You should not have stationed yourself at the crossroads to cut off his escapees; you should not have handed over his survivors on the day of distress.",
            "T": "And the worst of all:\nYou blocked the mountain passes — hunting down those trying to flee.\nYou handed the survivors over to their enemies\non the very day they were running for their lives."
        },
        "15": {
            "L": "For near is the day of the LORD upon all the nations; as you have done, it shall be done to you; your deeds shall return upon your own head.",
            "M": "For the day of the LORD is near for all the nations. As you have done, it shall be done to you; your deeds will return upon your own head.",
            "T": "The Day of the LORD draws near —\nand it comes not for Judah alone but for every nation.\nThe law of return is absolute:\nwhat you did will be done to you;\neverything you set in motion will land on your own head."
        },
        "16": {
            "L": "For as you have drunk on my holy mountain, so all the nations shall drink continually; they shall drink and swallow down, and shall be as though they had not been.",
            "M": "For just as you drank on my holy mountain, so all the nations shall drink without end; they shall drink and stagger, and be as though they had never existed.",
            "T": "You drank your fill of triumph on my holy mountain.\nNow every nation will be made to drink —\nnot celebration but the cup of judgment —\ndrinking on and on, swallowing, staggering,\nuntil they vanish from the earth as if they had never been."
        },
        "17": {
            "L": "But on Mount Zion there shall be those who escape, and it shall be holy; and the house of Jacob shall possess their possessions.",
            "M": "But on Mount Zion there shall be a delivered remnant, and it shall be holy; and the house of Jacob shall take back what is theirs.",
            "T": "But Mount Zion will be a place of rescue —\na holy remnant standing on holy ground.\nThe house of Jacob will repossess\neverything that was stripped from them."
        },
        "18": {
            "L": "The house of Jacob shall be a fire, and the house of Joseph a flame, and the house of Esau for stubble; they shall burn them and consume them, and no survivor shall remain of the house of Esau — for the LORD has spoken.",
            "M": "The house of Jacob will be a fire, and the house of Joseph a flame, but the house of Esau will be stubble; they will set it ablaze and consume it, and no survivor will remain of the house of Esau — for the LORD has spoken.",
            "T": "Jacob will be the fire.\nJoseph will be the flame.\nEsau will be dry stubble.\nTogether they will burn through him and leave nothing —\nnot a single survivor from the house of Esau.\nYahweh has spoken it, and it is done."
        },
        "19": {
            "L": "And those of the Negev shall possess the mount of Esau, and those of the Shephelah the Philistines; and they shall possess the field of Ephraim and the field of Samaria, and Benjamin shall possess Gilead.",
            "M": "The people of the Negev will possess the mount of Esau, and those of the Shephelah will possess the land of the Philistines; they will possess the fields of Ephraim and the fields of Samaria, and Benjamin will possess Gilead.",
            "T": "Israel's land will overflow its ancient borders:\nthe southern tribes will take Edom's highlands;\nthe lowland people will push into Philistia;\nEphraim and Samaria's fields will be reclaimed;\nBenjamin will extend east into Gilead."
        },
        "20": {
            "L": "And the exiles of this host of the children of Israel shall possess the land of the Canaanites as far as Zarephath, and the exiles of Jerusalem who are in Sepharad shall possess the cities of the Negev.",
            "M": "The exiles of Israel's forces will possess the land of the Canaanites as far as Zarephath, and the exiles of Jerusalem who are in Sepharad will possess the cities of the Negev.",
            "T": "Even the scattered exiles will return with an inheritance:\nthose dispersed as far north as Zarephath\nwill reclaim the land of Canaan;\nthose exiled to far-off Sepharad — wherever that distant place may be —\nwill come home to settle the cities of the south.\n(Sepharad is the endpoint of diaspora: no exile is beyond the reach of restoration.)"
        },
        "21": {
            "L": "And saviours shall go up onto Mount Zion to judge the mount of Esau, and the kingdom shall be the LORD's.",
            "M": "Then deliverers will go up to Mount Zion to govern the mount of Esau, and the kingdom will be the LORD's.",
            "T": "Then saviours will ascend Mount Zion\nand rule over the highlands of Esau —\nand when that day comes,\nthe kingdom will belong to Yahweh alone."
        }
    }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'obadiah')
        merge_tier(existing, OBADIAH, tier_key)
        save(tier_dir, 'obadiah', existing)
    print('Obadiah 1 written.')

if __name__ == '__main__':
    main()
