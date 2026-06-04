"""
MKT Ezekiel chapter 16 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-ezekiel-16-16.py

Ezekiel 16 is the longest chapter in Ezekiel and one of the most extended allegorical
passages in the entire Old Testament. It presents Jerusalem as an abandoned infant whom
God rescued, raised, adorned, and married — who then prostituted herself to every
neighbouring nation and sank lower than Sodom. The chapter ends in covenant restoration.
Structure: vv. 1-5 (abandoned infant), 6-14 (rescue and marriage), 15-34 (the harlotry),
35-43 (the judgment), 44-58 (Sodom and Samaria comparison), 59-63 (everlasting covenant).

Translation decisions (carrying forward all Ezekiel conventions from prior scripts):

- H3068 (יהוה): "LORD" in L/M throughout. "Yahweh" in T — especially the covenant
  formula "declares Yahweh" and the recognition formula "you shall know that I am Yahweh."
  Consistent with all prior Ezekiel scripts.

- H136 + H3069 (אֲדֹנָי יְהוִה / Adonai-Yahweh): "Lord GOD" in L/M (small-caps GOD);
  "Lord Yahweh" in T. The combined form appears throughout this chapter as oracle-marker.

- H7307 (רוּחַ / Spirit/wind/breath): Does not appear centrally in ch. 16; the driving
  force here is covenant and shame, not the prophetic Spirit.

- H5315 (נֶפֶשׁ / soul/life/person): v. 5 — "of thy person" in the token gloss, referring
  to the infant's being. L: "soul" (Strong's-accurate). M: "person." T: "you" (the whole
  abandoned child, not a detachable soul). This follows established Ezekiel practice.

- H2181 (זָנָה / play the harlot) and H8457 (תַּזְנוּת / whoredoms/fornications): The
  dominant vocabulary of vv. 15-34. L: "played the harlot / whoredoms" (Strong's-accurate
  and traditional). M: "played the prostitute / prostitution." T: allows more vivid
  rendering — "sold yourself / betrayal / harlotry." The sexual metaphor represents
  covenant idolatry; it must not be softened but also not be gratuitously explicit.

- H5003 (נָאַף / commit adultery): v. 32, 38. L/M: "commit adultery." T: "adulteress."

- H868 (אֶתְנַן / hire/reward): vv. 31, 33, 34, 41. The fee paid to or by a prostitute.
  L/M: "hire/payment." T: "payment." The irony (Jerusalem paid her lovers) is explicit
  in the text and must be preserved in all tiers.

- H1285 (בְּרִית / covenant): vv. 8, 59, 60, 61, 62. The covenant in v. 8 is a marriage
  covenant sealed by oath and garment-covering (the ancient Near Eastern betrothal rite).
  The covenant in vv. 59-62 is the "everlasting covenant" (H5769) that God will establish
  unilaterally despite Jerusalem's faithlessness. L/M/T: "covenant" throughout; "everlasting
  covenant" for the H5769 compound in v. 60.

- H7650 (שָׁבַע / swear/take an oath): v. 8. God's oath of betrothal. L: "I sware."
  M: "I gave you my oath." T: "I swore an oath." This is not mere promise but covenant
  self-binding.

- H3671 (כָּנָף / skirt/corner of garment): v. 8. The act of spreading the garment-corner
  over a woman is the betrothal act (cf. Ruth 3:9; Deut. 22:30). L: "my skirt."
  M: "the corner of my garment." T: "the hem of my robe."

- H1544 (גִּלּוּלִים / idols): v. 36. Ezekiel's characteristic contemptuous term, possibly
  derived from a root meaning "dung-pellets" or "logs." L/M: "idols." T: "idols."

- H2534 (חֵמָה / fury) + H7068 (קִנְאָה / jealousy): vv. 38, 42. God's covenant wrath.
  L: "fury and jealousy." M: "fury and jealousy." T: "fury, the burning jealousy of the
  God whose covenant you broke." Both words are covenantal — jealousy (H7068) is not
  envy but the exclusive-love demand of the marriage bond (cf. Exod. 20:5).

- H5467 (סְדֹם / Sodom) and H8111 (שֹׁמְרֹון / Samaria): vv. 44-58. The sister-comparison
  is the climax of the indictment. Jerusalem's sin exceeded both Sodom's (pride, ease,
  neglect of the poor — v. 49) and Samaria's. L/M: "Sodom/Samaria" (transliterated).

- H1347 (גָּאוֹן / pride): v. 49. Sodom's first sin is pride. L/M: "pride." T: "pride."

- H7622 (שְׁבוּת / captivity/fortunes): vv. 53, 55. The phrase שׁוּב שְׁבוּת is idiomatic —
  "restore the fortunes of" rather than "bring back the captivity of." Modern scholarship
  (BDB, HALOT) supports "restore fortunes" as the primary sense. L: "bring again their
  captivity" (traditional KJV rendering). M: "restore the fortunes of." T: "restore."

- H5769 (עוֹלָם / everlasting/age): v. 60. בְּרִית עוֹלָם — "everlasting covenant." This is
  unilateral grace — God remembers what Jerusalem has forgotten. L/M: "everlasting
  covenant." T: "a covenant that will never end."

- H3722 (כָּפַר / make atonement/be pacified): v. 63. The verb here is niphal passive —
  "when I am pacified/when I make atonement for you." The same root as the sacrificial
  atonement vocabulary. This is extraordinary: God atones for the unfaithful wife's sins
  to make covenant restoration possible. L: "when I am pacified toward you." M: "when I
  make atonement for you." T: "because I will make atonement for everything you have done."

- The divine oath "as I live" (H2416 + H589): v. 48. God's self-pledge (cf. 14:16, 18, 20).
  L/M: "As I live." T: "By my own life I swear."

- Aspect notes specific to ch. 16:
  - The narrative past (wayyiqtol) frames the foundling story (vv. 4-14) as historical
    memory; English past tense is used consistently.
  - The judgment oracles (vv. 35-43) shift to future tense (yiqtol) for the announced
    punishment; English future tense is used.
  - The restoration (vv. 59-63) uses both perfect (I will remember — H2142) and imperfect
    (I will establish — H6965); both rendered as English future to reflect the prophetic-
    perfect certainty of the promise.

- OT intertextuality: The garment-spreading betrothal (v. 8) echoes Ruth 3:9 and Deut.
  22:30. The abandoned infant motif may echo ancient Near Eastern foundling narratives
  (Sargon legend). The Sodom inventory of sins (v. 49) is the fullest biblical definition
  of Sodom's crime — pride and neglect of the poor, not only sexual sin. The "everlasting
  covenant" (v. 60) anticipates Jer. 31:31-34 and Ezek. 36-37.
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

EZEKIEL = {
  "16": {
    "1": {
      "L": "The word of the LORD came again unto me, saying:",
      "M": "The word of the LORD came to me, saying:",
      "T": "Again the word of Yahweh came to me:"
    },
    "2": {
      "L": "Son of man, cause Jerusalem to know her abominations.",
      "M": "Son of man, confront Jerusalem with her abominations.",
      "T": "Son of man, make Jerusalem face what she has done — lay her abominations before her."
    },
    "3": {
      "L": "And say, Thus says the Lord GOD unto Jerusalem: Your birth and your nativity are of the land of Canaan; your father was an Amorite, and your mother a Hittite.",
      "M": "Say: This is what the Lord GOD says to Jerusalem: Your origins and your birth are in the land of Canaan. Your father was an Amorite and your mother a Hittite.",
      "T": "Say this: Lord Yahweh speaks to Jerusalem — you do not trace your roots to the patriarchs but to Canaan; your father was an Amorite, your mother a Hittite. No noble lineage here."
    },
    "4": {
      "L": "And as for your nativity, in the day you were born your navel was not cut, neither were you washed in water to cleanse you; you were not salted at all, nor swaddled at all.",
      "M": "When you were born, your navel cord was not cut, you were not washed with water to cleanse you, you were not rubbed with salt, and you were not wrapped in cloths.",
      "T": "On the day of your birth no one cut your cord, no one washed you, no one rubbed salt into your skin to make you firm, no one swaddled you. You received nothing."
    },
    "5": {
      "L": "No eye pitied you, to do any of these things unto you, to have compassion upon you; but you were cast out in the open field, to the loathing of your person, in the day you were born.",
      "M": "No one looked on you with pity or compassion to do any of these things for you. You were cast out into the open field, despised, on the day you were born.",
      "T": "No one looked at you with pity. No one took you up. You were flung into an open field — unwanted, rejected, discarded on the very day of your birth."
    },
    "6": {
      "L": "And when I passed by you, and saw you polluted in your own blood, I said unto you in your blood, Live! Yea, I said unto you in your blood, Live!",
      "M": "When I passed by you and saw you lying in your blood, I said to you, 'Live!' Yes, as you lay in your blood I said to you, 'Live!'",
      "T": "I passed by you — and found you lying in your blood, dying — and I spoke life over you. 'Live,' I said. Even there, in your blood, I said: 'Live.'"
    },
    "7": {
      "L": "I have caused you to multiply as the bud of the field, and you have increased and waxen great, and you came to excellent ornaments; your breasts were fashioned, and your hair was grown, but you were naked and bare.",
      "M": "I made you thrive like a plant of the field. You grew and became great and came to full womanhood — your breasts developed, your hair grew — yet you were still naked and bare.",
      "T": "I gave you life, and life flourished. You grew into womanhood — full and strong. But you were still naked. No one had yet clothed you."
    },
    "8": {
      "L": "Now when I passed by you, and looked upon you, behold, your time was the time of love; and I spread my skirt over you, and covered your nakedness: yea, I sware unto you, and entered into a covenant with you, says the Lord GOD, and you became mine.",
      "M": "When I passed by you again and looked at you, you were at the age for love. I spread the corner of my garment over you and covered your nakedness. I gave you my oath and entered into a covenant with you, declares the Lord GOD, and you became mine.",
      "T": "The next time I passed by you, I looked and you were ready — a woman, of age, the time of love upon you. I covered your nakedness with the hem of my robe. I swore an oath. I entered covenant with you — declares Lord Yahweh — and you became mine."
    },
    "9": {
      "L": "Then washed I you with water; yea, I throughly washed away your blood from you, and I anointed you with oil.",
      "M": "I bathed you with water, washed the blood from you completely, and anointed you with oil.",
      "T": "I washed you — all the blood of your abandoned beginnings — I washed it away and anointed you with fragrant oil."
    },
    "10": {
      "L": "I clothed you also with embroidered work, and shod you with badgers' skin, and I girded you about with fine linen, and I covered you with silk.",
      "M": "I clothed you in embroidered fabric, put fine leather sandals on your feet, dressed you in fine linen, and covered you with silk.",
      "T": "I dressed you in embroidered cloth and fine leather sandals, in linen and silk — a queen's wardrobe."
    },
    "11": {
      "L": "I decked you also with ornaments, and I put bracelets upon your hands, and a chain on your neck.",
      "M": "I adorned you with jewelry, bracelets on your wrists and a chain around your neck.",
      "T": "I hung jewelry on you — bracelets for your wrists, a necklace for your neck."
    },
    "12": {
      "L": "And I put a jewel on your nose, and earrings in your ears, and a beautiful crown upon your head.",
      "M": "I put a ring in your nose, earrings in your ears, and a beautiful crown on your head.",
      "T": "A ring in your nose, gold in your ears, a crown on your head — I made you magnificent."
    },
    "13": {
      "L": "Thus were you decked with gold and silver; and your raiment was of fine linen, and silk, and embroidered work; you ate fine flour, and honey, and oil: and you were exceeding beautiful, and you did prosper into a kingdom.",
      "M": "You were adorned with gold and silver. Your clothing was fine linen, silk, and embroidered cloth. You ate fine flour, honey, and oil. You were exceedingly beautiful and advanced to royalty.",
      "T": "Gold and silver on your body, the finest clothes, the finest food — fine flour and honey and olive oil. Your beauty was extraordinary. You rose to queenly splendor."
    },
    "14": {
      "L": "And your renown went forth among the nations for your beauty; for it was perfect through my comeliness, which I had put upon you, says the Lord GOD.",
      "M": "Your fame spread among the nations because of your beauty, which was perfect through the splendor I had given you, declares the Lord GOD.",
      "T": "Your fame spread to every nation — all of it your beauty, and all of your beauty my gift. It was perfect. Declares Lord Yahweh: I made you what you were."
    },
    "15": {
      "L": "But you did trust in your own beauty, and played the harlot because of your renown, and poured out your fornications on every one that passed by; his it was.",
      "M": "But you trusted in your beauty and played the whore because of your fame, and lavished your prostitution on every passerby — your beauty became his.",
      "T": "But you turned that beauty against me. You trusted in it and sold yourself — to every one who passed by, to any taker. All I gave you, you gave away."
    },
    "16": {
      "L": "And of your garments you did take, and decked your high places with divers colours, and played the harlot thereupon: the like things shall not come, neither shall it be so.",
      "M": "You took some of your garments and made yourself colorful high places, and played the whore on them. Such a thing has never been done and never should be.",
      "T": "You took the beautiful clothes I gave you, decorated your pagan shrines with them in gaudy colors, and turned those altars into beds. Nothing like this had ever been done. Nothing should ever be."
    },
    "17": {
      "L": "You have also taken your fair jewels of my gold and of my silver, which I had given you, and made to yourself images of men, and did commit whoredom with them.",
      "M": "You took your beautiful jewelry — my gold and my silver that I had given you — and made male idols for yourself, and played the whore with them.",
      "T": "The gold and silver I gave you — you melted them down into images of men and worshipped them in idolatrous rites. My gifts became your idols."
    },
    "18": {
      "L": "And took your broidered garments, and covered them: and you have set my oil and mine incense before them.",
      "M": "You took your embroidered garments to clothe them and set my oil and my incense before them.",
      "T": "You dressed your idols in the robes I gave you and burned my oil and my incense before them — as though they were the God who loved you."
    },
    "19": {
      "L": "My meat also which I gave you, fine flour, and oil, and honey, wherewith I fed you, you have even set it before them for a sweet savour: and thus it was, says the Lord GOD.",
      "M": "My food that I gave you — the fine flour, oil, and honey with which I fed you — you placed before them as a pleasing aroma. And so it was, declares the Lord GOD.",
      "T": "The bread I put on your table — fine flour and honey and oil — you spread it before your idols as an offering. Everything I gave to sustain you, you offered to them. Declares Lord Yahweh: it happened."
    },
    "20": {
      "L": "Moreover you have taken your sons and your daughters, whom you have borne unto me, and these have you sacrificed unto them to be devoured. Is this of your whoredoms a small matter?",
      "M": "And you took your sons and daughters whom you had borne to me and sacrificed them to be devoured. Were your prostitutions not enough?",
      "T": "Then you took your own children — children you bore for me — and you sacrificed them to be consumed by your idols. Was all your other betrayal not enough?"
    },
    "21": {
      "L": "That you have slain my children, and delivered them to cause them to pass through the fire for them?",
      "M": "You slaughtered my children and made them pass through the fire as offerings to your idols.",
      "T": "You killed your own children — my children — and burned them as offerings. This."
    },
    "22": {
      "L": "And in all your abominations and your whoredoms you have not remembered the days of your youth, when you were naked and bare, and were polluted in your blood.",
      "M": "In all your abominations and prostitutions you did not remember the days of your youth, when you were naked and bare, lying in your blood.",
      "T": "Through all of it — every abomination, every act of betrayal — you never once remembered. You forgot the field. You forgot the blood. You forgot what I found you in."
    },
    "23": {
      "L": "And it came to pass after all your wickedness — woe, woe unto you! says the Lord GOD —",
      "M": "After all your wickedness — woe, woe to you! declares the Lord GOD —",
      "T": "After all of this — woe to you, woe! declares Lord Yahweh —"
    },
    "24": {
      "L": "That you have also built unto you an eminent place, and have made you a high place in every street.",
      "M": "you built yourself a vaulted shrine and made yourself a high place in every public square.",
      "T": "you built yourself shrines in every street, platforms of prostitution in every public square."
    },
    "25": {
      "L": "You have built your high place at every head of the way, and have made your beauty to be abhorred, and have opened yourself to every one that passed by, and multiplied your whoredoms.",
      "M": "You built your high place at the head of every street, made your beauty an abomination, and offered yourself to every passerby, multiplying your prostitutions.",
      "T": "At every crossroads you set up your high place. You made your God-given beauty revolting. You offered yourself to every passerby — again and again and again."
    },
    "26": {
      "L": "You have also committed fornication with the Egyptians your neighbours, great of flesh; and have increased your whoredoms, to provoke me to anger.",
      "M": "You played the whore with the Egyptians, your neighbors who are great of flesh, and multiplied your prostitution to provoke me to anger.",
      "T": "You turned to Egypt — your neighbors, their power so prized — and whored yourself there too, multiplying your betrayal, provoking me to my face."
    },
    "27": {
      "L": "Behold, therefore I have stretched out my hand over you, and have diminished your ordinary food, and delivered you unto the will of them that hate you, the daughters of the Philistines, which are ashamed of your lewd way.",
      "M": "So I stretched out my hand against you and reduced your allotment, and handed you over to the will of your enemies, the daughters of the Philistines, who were ashamed of your lewd conduct.",
      "T": "So I moved against you — I cut back what I gave you and handed you over to those who hate you, even the Philistines. Even they were ashamed of what you had become."
    },
    "28": {
      "L": "You have played the whore also with the Assyrians, because you were unsatiable; yea, you have played the harlot with them, and yet could not be satisfied.",
      "M": "You also played the whore with the Assyrians because you were insatiable; you played the harlot with them and still were not satisfied.",
      "T": "And then Assyria. Still not satisfied. You went to them too, gave yourself to them — and still came back hungry."
    },
    "29": {
      "L": "You have moreover multiplied your fornication in the land of Canaan unto Chaldea; and yet you were not satisfied herewith.",
      "M": "You multiplied your prostitution into the land of Chaldea, and still you were not satisfied.",
      "T": "Then Babylon. The traders of Chaldea. Even then you were not satisfied."
    },
    "30": {
      "L": "How weak is your heart, says the Lord GOD, seeing you do all these things, the work of an imperious whorish woman;",
      "M": "How debased is your heart, declares the Lord GOD, that you did all these things — the deeds of a shameless prostitute —",
      "T": "How diseased your heart! — declares Lord Yahweh — to do all of this: the work of a prostitute who feels no shame,"
    },
    "31": {
      "L": "In that you build your eminent place in the head of every way, and make your high place in every street; and have not been as a harlot, in that you scorn hire;",
      "M": "building your vaulted shrine at the head of every street and your high place in every square. Yet you were unlike a prostitute, for you scorned payment.",
      "T": "who built her platforms at every crossroads and her shrines in every square — and was not even a prostitute, because a prostitute at least demands payment. You scorned it."
    },
    "32": {
      "L": "But as a wife that commits adultery, which takes strangers instead of her husband!",
      "M": "You are an adulterous wife who receives strangers instead of her own husband.",
      "T": "An adulteress — preferring strangers to the husband who loved her."
    },
    "33": {
      "L": "They give gifts to all whores: but you give your gifts to all your lovers, and hire them, that they may come unto you on every side for your whoredom.",
      "M": "Men give gifts to all prostitutes, but you gave your gifts to all your lovers, bribing them to come to you from every side for your prostitution.",
      "T": "Every prostitute gets paid — but you paid. You gave your gifts to your lovers, bribed them to take you, hired them to use you. Every side, every direction, you spent yourself on them."
    },
    "34": {
      "L": "And the contrary is in you from other women in your whoredoms, whereas none follows you to commit whoredoms: and in that you give a reward, and no reward is given unto you, therefore you are contrary.",
      "M": "So you were the opposite of other women in your prostitution: no one solicited you — you solicited. You gave payment instead of receiving it. Therefore you were the opposite.",
      "T": "Everything was backward. Other women are sought; you did the seeking. Others are paid; you paid. You inverted it all — the most shameless reversal of all."
    },
    "35": {
      "L": "Wherefore, O harlot, hear the word of the LORD:",
      "M": "Therefore, prostitute, hear the word of the LORD:",
      "T": "So hear this, harlot — the word of Yahweh:"
    },
    "36": {
      "L": "Thus says the Lord GOD; Because your filthiness was poured out, and your nakedness discovered through your whoredoms with your lovers, and with all the idols of your abominations, and by the blood of your children, which you did give unto them;",
      "M": "This is what the Lord GOD says: Because your lust was poured out and your nakedness exposed in your prostitution with your lovers, and with all your abominable idols, and because of the blood of your children that you gave to them —",
      "T": "Lord Yahweh declares: Because you poured yourself out — your nakedness exposed to every lover, your worship poured on every idol, and your children's blood spilled on their altars —"
    },
    "37": {
      "L": "Behold, therefore I will gather all your lovers, with whom you have taken pleasure, and all them that you have loved, with all them that you have hated; I will even gather them round about against you, and will discover your nakedness unto them, that they may see all your nakedness.",
      "M": "therefore I will gather all your lovers with whom you took pleasure, all those you loved and all those you hated. I will gather them against you from every side and expose your nakedness to them so that they may see all of it.",
      "T": "I am gathering them — every lover you ever sought, everyone you loved, everyone you hated. I will bring them all around you and strip you bare before them. Every one of them will see."
    },
    "38": {
      "L": "And I will judge you as women that break wedlock and shed blood are judged; and I will give you blood in fury and jealousy.",
      "M": "I will judge you as adulteresses and murderers are judged, and bring bloodguilt upon you in fury and jealousy.",
      "T": "I will judge you the way adulteresses and murderers are judged — with blood, with fury, with the burning jealousy of the God whose covenant you broke."
    },
    "39": {
      "L": "And I will also give you into their hand, and they shall throw down your eminent place, and shall break down your high places: they shall strip you also of your clothes, and shall take your fair jewels, and leave you naked and bare.",
      "M": "I will hand you over to them, and they will tear down your vaulted shrines and demolish your high places. They will strip off your clothes and take your beautiful jewelry and leave you naked and bare.",
      "T": "I will hand you over to them. They will tear down everything you built, strip off everything I gave you, take the jewelry, take the robes — and leave you as I found you: naked and bare."
    },
    "40": {
      "L": "They shall also bring up a company against you, and they shall stone you with stones, and thrust you through with their swords.",
      "M": "They will bring a mob against you, stone you with stones, and cut you down with their swords.",
      "T": "A mob will come. Stones and swords. The crowd that once came to you will be the instrument of your judgment."
    },
    "41": {
      "L": "And they shall burn your houses with fire, and execute judgments upon you in the sight of many women: and I will cause you to cease from playing the harlot, and you also shall give no hire any more.",
      "M": "They will burn your houses with fire and carry out judgments against you in the sight of many women. I will put a stop to your prostitution, and you will pay no more.",
      "T": "They will burn your houses. Many women will witness the verdict carried out on you. And the harlotry will end. Not because you stop — because I stop it."
    },
    "42": {
      "L": "So will I make my fury toward you to rest, and my jealousy shall depart from you, and I will be quiet, and will be no more angry.",
      "M": "Then my fury toward you will subside and my jealousy will leave you. I will be at rest and no longer angry.",
      "T": "Then — and only then — my fury will be spent. My jealousy will lift. I will be still. The anger will be done."
    },
    "43": {
      "L": "Because you have not remembered the days of your youth, but have fretted me in all these things; behold, therefore I also will recompense your way upon your head, says the Lord GOD: and you shall not commit this lewdness above all your abominations.",
      "M": "Because you did not remember the days of your youth but provoked me with all these things, I will bring your deeds back on your own head, declares the Lord GOD. Did you not add lewdness to all your other abominations?",
      "T": "You never remembered. The field, the blood, the day I found you — you forgot all of it and raged against me with every deed. So I return it all to your own head. Declares Lord Yahweh: was your lewdness not enough? Did it have to exceed every abomination you had already committed?"
    },
    "44": {
      "L": "Behold, every one that uses proverbs shall use this proverb against you, saying, As is the mother, so is her daughter.",
      "M": "Everyone who uses proverbs will apply this proverb to you: 'Like mother, like daughter.'",
      "T": "There is a proverb everyone will speak over you: 'Like mother, like daughter.' It will fit."
    },
    "45": {
      "L": "You are your mother's daughter, that loathes her husband and her children; and you are the sister of your sisters, which loathed their husbands and their children: your mother was an Hittite, and your father an Amorite.",
      "M": "You are your mother's daughter, who loathed her husband and her children; and you are the sister of your sisters, who loathed their husbands and their children. Your mother was a Hittite and your father an Amorite.",
      "T": "You are your mother's daughter — she despised her husband and her children, just as you have done. You are the sister of your sisters — they did the same. The pattern holds from root to branch. Hittite mother, Amorite father. This is who you come from."
    },
    "46": {
      "L": "And your elder sister is Samaria, she and her daughters that dwell at your left hand: and your younger sister, that dwells at your right hand, is Sodom and her daughters.",
      "M": "Your older sister is Samaria with her daughters, living north of you, and your younger sister, living south of you, is Sodom with her daughters.",
      "T": "Your older sister is Samaria — she and her cities, to your north. Your younger sister is Sodom — she and her cities, to your south."
    },
    "47": {
      "L": "Yet have you not walked after their ways, nor done after their abominations: but as if that were a very little thing, you were corrupted more than they in all your ways.",
      "M": "You did not merely walk in their ways or act according to their abominations — as if that were too small a thing, you became more corrupt than they in all your ways.",
      "T": "You did not simply follow their example. No — as if their sin were too mild for you, you surpassed them. You went further into corruption than either of your sisters."
    },
    "48": {
      "L": "As I live, says the Lord GOD, Sodom your sister has not done, she nor her daughters, as you have done, you and your daughters.",
      "M": "As I live, declares the Lord GOD, your sister Sodom and her daughters have not done what you and your daughters have done.",
      "T": "By my own life I swear — declares Lord Yahweh — Sodom and all her cities have not done what you have done."
    },
    "49": {
      "L": "Behold, this was the iniquity of your sister Sodom, pride, fulness of bread, and abundance of idleness was in her and in her daughters, neither did she strengthen the hand of the poor and needy.",
      "M": "This was the guilt of your sister Sodom: she and her daughters had pride, excess of food, and comfortable ease, but did not help the poor and needy.",
      "T": "This is what condemned Sodom: pride — she ate well, lived in ease, had more than enough — but she never lifted a hand for the poor or the needy."
    },
    "50": {
      "L": "And they were haughty, and committed abomination before me: therefore I took them away as I saw good.",
      "M": "They were arrogant and committed abomination before me. So I removed them when I saw it.",
      "T": "They were proud. They did what is hateful in my sight. I saw it — and I removed them."
    },
    "51": {
      "L": "Neither has Samaria committed half of your sins; but you have multiplied your abominations more than they, and have justified your sisters in all your abominations which you have done.",
      "M": "Samaria has not committed half your sins. You have multiplied your abominations beyond them and made your sisters appear righteous by all the abominations you have committed.",
      "T": "Samaria? She has not done half of what you have done. Your abominations so exceeded hers that you made her look righteous. You made Sodom look righteous. That is what Jerusalem has done."
    },
    "52": {
      "L": "You also, which have judged your sisters, bear your own shame for your sins that you have committed more abominable than they: they are more righteous than you: yea, be you confounded also, and bear your shame, in that you have justified your sisters.",
      "M": "Bear your own disgrace, you who have judged your sisters. Because your sins were more abominable than theirs, they are more righteous than you. So be ashamed and bear your disgrace, for you have made your sisters appear righteous.",
      "T": "You who judged your sisters — bear your own shame. By sinning worse than they did, you justified them. They are more righteous than you. Be ashamed. Carry the weight of that."
    },
    "53": {
      "L": "When I shall bring again their captivity, the captivity of Sodom and her daughters, and the captivity of Samaria and her daughters, then will I bring again the captivity of your captives in the midst of them:",
      "M": "When I restore the fortunes of Sodom and her daughters and the fortunes of Samaria and her daughters, I will also restore your fortunes among them,",
      "T": "But I will restore — Sodom and her cities, Samaria and her cities, and you among them. When I bring back their fortunes, I will bring back yours too."
    },
    "54": {
      "L": "That you may bear your own shame, and may be confounded in all that you have done, in that you are a comfort unto them.",
      "M": "so that you may bear your disgrace and be ashamed of all you have done, having become a consolation to them.",
      "T": "So that you will bear your shame rightly — ashamed of everything you did — even becoming, in your humiliation, a kind of consolation to them."
    },
    "55": {
      "L": "When your sisters, Sodom and her daughters, shall return to their former estate, and Samaria and her daughters shall return to their former estate, then you and your daughters shall return to your former estate.",
      "M": "Your sisters, Sodom and her daughters, shall return to their former state, and Samaria and her daughters shall return to their former state, and you and your daughters shall return to your former state.",
      "T": "Sodom will be restored. Samaria will be restored. And you — Jerusalem, you too will be restored to what you were."
    },
    "56": {
      "L": "For your sister Sodom was not mentioned by your mouth in the day of your pride,",
      "M": "Your sister Sodom was not even mentioned by you in the day of your pride,",
      "T": "In the days of your pride you would not even speak Sodom's name —"
    },
    "57": {
      "L": "Before your wickedness was discovered, as at the time of your reproach of the daughters of Syria, and all that are round about her, the daughters of the Philistines, which despise you round about.",
      "M": "before your own wickedness was exposed. Now you have become an object of reproach to the daughters of Syria and all around her, and to the daughters of the Philistines who despise you on every side.",
      "T": "before your own wickedness was laid bare. Now you have become what Sodom was to you — a byword, a thing of contempt, despised by Syria and the Philistines on every side."
    },
    "58": {
      "L": "You have borne your lewdness and your abominations, says the LORD.",
      "M": "You bear the penalty of your lewdness and your abominations, declares the LORD.",
      "T": "You carry the weight of your lewdness and your abominations. Yahweh declares it."
    },
    "59": {
      "L": "For thus says the Lord GOD; I will even deal with you as you have done, which have despised the oath in breaking the covenant:",
      "M": "For this is what the Lord GOD says: I will deal with you as you deserve, you who despised the oath and broke the covenant.",
      "T": "Lord Yahweh declares: I will treat you as you have acted — you who despised your vow, who shattered the covenant —"
    },
    "60": {
      "L": "Nevertheless I will remember my covenant with you in the days of your youth, and I will establish unto you an everlasting covenant.",
      "M": "Yet I will remember my covenant with you from the days of your youth, and I will establish for you an everlasting covenant.",
      "T": "Yet I will remember. My covenant with you — from the days when you lay in the field — I will remember it. And I will establish with you a covenant that will never end."
    },
    "61": {
      "L": "Then you shall remember your ways, and be ashamed, when you shall receive your sisters, your elder and your younger: and I will give them unto you for daughters, but not by your covenant.",
      "M": "Then you will remember your ways and be ashamed when you receive your sisters, both your elder and your younger, and I give them to you as daughters — but not because of your covenant.",
      "T": "Then you will remember your own ways — and be ashamed. When I give you your sisters as daughters — Samaria and Sodom restored and given to you — it will not be because of anything in your covenant. It will be grace alone."
    },
    "62": {
      "L": "And I will establish my covenant with you; and you shall know that I am the LORD:",
      "M": "I will establish my covenant with you, and you shall know that I am the LORD,",
      "T": "I will establish my covenant with you — and then you will know, fully and truly, that I am Yahweh,"
    },
    "63": {
      "L": "That you may remember, and be confounded, and never open your mouth any more because of your shame, when I am pacified toward you for all that you have done, says the Lord GOD.",
      "M": "so that you may remember and be ashamed, and never again open your mouth in pride because of your shame, when I make atonement for you for all that you have done, declares the Lord GOD.",
      "T": "so that you will remember — and fall silent in your shame — never again lifting your voice in self-justification, because I will make atonement for everything you have done. Declares Lord Yahweh."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'ezekiel')
        merge_tier(existing, EZEKIEL, tier_key)
        save(tier_dir, 'ezekiel', existing)
    print('Ezekiel 16 written.')

if __name__ == '__main__':
    main()
