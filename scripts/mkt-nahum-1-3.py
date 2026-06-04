"""
MKT Nahum chapters 1–3 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-nahum-1-3.py

=== BOOK OVERVIEW ===

Nahum is a singularly focused oracle: the fall of Nineveh is announced,
celebrated, and described in unsparing detail. It is the harshest of the
Twelve in tone, closest in spirit to Obadiah (against Edom). There is
virtually no call to repentance — only verdict and fulfillment.

Three structural movements:

  Ch. 1  — Theophany hymn + dual oracle (comfort to Judah / doom to Nineveh)
            The acrostic poem (vv.2-10, following the Hebrew alphabet through
            Kaph/כ) is the book's most formal literary passage. The divine-
            warrior theophany (vv.3b-6) echoes Psalm 18 and Habakkuk 3.
  Ch. 2  — Battle description: the assault and plunder of Nineveh.
            Highly staccato, cinematic. The lion metaphor (vv.11-13) closes
            the chapter and prepares for ch.3's extended lion imagery.
  Ch. 3  — The "Woe" oracle: Nineveh convicted as a bloodstained harlot-city.
            The comparison to No-Amon/Thebes (vv.8-10) grounds the prophecy
            historically — Nineveh itself sacked Thebes in 663 BCE; now she
            faces the same fate. The bitter irony permeates the final chapter.

Historical note: Nineveh fell to the Medo-Babylonian coalition in 612 BCE.
Nahum likely wrote between 663 BCE (fall of Thebes, used as past event in 3:8)
and 612 (fall of Nineveh, still future throughout the book).

=== TEXTUAL NOTES ===

- 1:2: The triple repetition of יהוה is intentional and emphatic; preserved
  in all three tiers.
- 1:2 H1167 (בַּעַל): literally "lord/master" — here used idiomatically as
  "possessor of wrath" = one who rages, rendered "wrathful" / "full of wrath."
- 1:3 H5352 (נָקָה, Piel repeated): "will by no means acquit" — the doubled
  infinitive absolute in Hebrew signals emphatic negation; carried into all tiers.
- 2:7 H5324 (נִצָּב): Textual crux. Traditionally read as the proper name
  "Huzzab" (a queen of Nineveh). More likely a hofal participle: "it is fixed /
  decreed." Modern scholarship broadly favors reading it as "she is stripped /
  uncovered / decreed to be led away." Rendered "the decree goes out" in M/T
  to reflect the probable verbal reading.
- 3:8 H4996 (נֹא): No-Amon = Thebes, the great Egyptian capital, sacked by
  Assyria in 663 BCE. The comparison is devastatingly ironic: Nineveh, which
  destroyed Thebes, will itself be destroyed in the same manner.
- 3:13: "Like women" is a conventional ancient Near Eastern military idiom for
  soldiers who have lost their will to fight; it is not a comment on women's
  courage but a cultural idiom for total demoralization.

=== CONTESTED-TERM DECISIONS ===

- H3068 (יהוה / Yahweh):
  L/M: "LORD" (small-caps convention throughout).
  T: "Yahweh" in direct oracle / theophanic passages (1:2, 1:7, 1:14, 2:2,
  2:13, 3:5); "the LORD" in narrative or comfort clauses.
  Reason: surfaces the personal divine name at points of greatest theological
  weight; "LORD" in L/M follows the consistent OT convention across all prior scripts.

- H7072 (קַנּוֹא / jealous):
  L/M: "jealous" (standard primary gloss; covenant term).
  T: "jealous" retained — Nahum 1:2 is not a pastoral context where "zealous"
  softens the edge; the exclusivity of the covenant claim is the point.

- H5492 (סוּפָה / whirlwind) / H8183 (שְׂעָרָה / storm):
  Rendered "whirlwind and storm" in L, "whirlwind and tempest" in M,
  "hurricane and tempest" in T (escalating register to match the T tier's
  more dramatic voice).

- H2617 (חֶסֶד / steadfast love): Not prominently featured in Nahum.
  No direct occurrence in these chapters; no ruling needed.

- H5315 (נֶפֶשׁ / nephesh): Does not appear in these chapters.

- H4941 (מִשְׁפָּט / mishpat): Does not appear prominently; no specific ruling needed.

- H6635 (צְבָאוֹת / hosts):
  Rendered "of hosts" in L/M (the standard formula "LORD of hosts").
  T: "of armies" where the military connotation is foregrounded (2:13, 3:5);
  "LORD of hosts" where the formula functions as a title.

- H3715 / H738 (כְּפִיר / young lion / אַרְיֵה / lion):
  The lion cluster in 2:11-13 uses multiple Hebrew words for lion by age and sex.
  L preserves each precisely; M and T use natural English variety:
  "lion / young lion / lioness / lion's cub."

- H2183 (זְנוּנִים / harlotries / prostitutions):
  L: "harlotries" (traditional rendering, preserves archaic force).
  M: "prostitutions" (direct modern equivalent).
  T: "seductions" in 3:4 where the metaphor of luring and enslaving nations is
  the point; "prostitutions" where the commercial/transactional aspect is primary.

- 3:4 — The metaphor of Nineveh as harlot and sorceress represents the ancient
  theological critique of imperial power as spiritual corruption, not a statement
  about gender. The T tier keeps the metaphor vivid while pointing to its imperial-
  political referent.
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

NAHUM = {
  "1": {
    "1": {
      "L": "The burden of Nineveh. The book of the vision of Nahum the Elkoshite.",
      "M": "A pronouncement concerning Nineveh. The record of the vision of Nahum from Elkosh.",
      "T": "An oracle against Nineveh. What Nahum of Elkosh saw."
    },
    "2": {
      "L": "A jealous and avenging God is the LORD; the LORD is an avenger and wrathful; the LORD takes vengeance on his adversaries and keeps wrath for his enemies.",
      "M": "The LORD is a jealous God who avenges; the LORD takes vengeance and is full of wrath; the LORD takes vengeance on his adversaries and reserves anger for his enemies.",
      "T": "Yahweh is a jealous God — and he avenges. Hear it three times: Yahweh avenges his adversaries; Yahweh reserves wrath for his enemies. He is not indifferent."
    },
    "3": {
      "L": "The LORD is slow to anger and great in power, and the LORD will by no means acquit the wicked. His way is in the whirlwind and the storm, and the clouds are the dust of his feet.",
      "M": "The LORD is slow to anger but immense in power, and he will by no means leave the wicked unpunished. His path is in the whirlwind and the storm; clouds are the dust beneath his feet.",
      "T": "Slow to anger — but immense in power. Yahweh will never simply acquit the guilty; that patience is not weakness. His road runs through hurricane and tempest; the storm clouds trail behind him like dust from his footfall."
    },
    "4": {
      "L": "He rebukes the sea and makes it dry; he dries up all the rivers. Bashan and Carmel wither; the blossom of Lebanon withers.",
      "M": "He rebukes the sea and dries it up; he causes all the rivers to run dry. Bashan and Carmel languish; the blossoms of Lebanon fade.",
      "T": "He rebukes the sea — and it dries up. Every river drains at his command. The lush uplands of Bashan go brown; Carmel's crest withers; Lebanon's flowers drop. Fertility itself retreats before him."
    },
    "5": {
      "L": "The mountains quake before him, and the hills melt; the earth is lifted up before his face — the world and all who dwell in it.",
      "M": "The mountains quake at his presence and the hills melt away; the earth heaves before him — the world and all its inhabitants.",
      "T": "Mountains quake when he draws near; hills dissolve. The whole earth convulses before his face — land and every living soul. Nothing holds still."
    },
    "6": {
      "L": "Who can stand before his indignation? And who can abide in the fierceness of his anger? His fury is poured out like fire, and the rocks are broken down before him.",
      "M": "Who can stand before his indignation? Who can endure the heat of his anger? His wrath is poured out like fire, and the rocks are shattered before him.",
      "T": "Who keeps their footing when his wrath breaks out? Who survives the burning of his anger? It floods like fire; it shatters stone. Nothing stands."
    },
    "7": {
      "L": "The LORD is good, a stronghold in the day of trouble; and he knows those who take refuge in him.",
      "M": "The LORD is good — a fortress in the day of trouble; he knows those who shelter in him.",
      "T": "But the LORD is good. When trouble comes, he is the fortress. He knows every one who trusts him — knows them by name."
    },
    "8": {
      "L": "But with an overrunning flood he will make a complete end of her place, and darkness shall pursue his enemies.",
      "M": "But with an overflowing flood he will bring her place to a complete end, and will drive his enemies into darkness.",
      "T": "Against Nineveh he unleashes a flood that sweeps the place entirely clean; and his enemies he chases into the blackest dark."
    },
    "9": {
      "L": "What do you devise against the LORD? He will make a complete end; affliction shall not rise up a second time.",
      "M": "What are you plotting against the LORD? He himself will make a complete end of it; distress will not arise a second time.",
      "T": "Whatever scheme you hatch against Yahweh — he ends it completely. He will not have to act twice. One blow is enough."
    },
    "10": {
      "L": "For while they are folded together like thorns and soaked like drunkards, they shall be devoured as fully dry stubble.",
      "M": "For they are tangled like thorns and sodden with drink like drunkards; they will be consumed entirely like dry stubble.",
      "T": "They are a tangle of thornbush, and drunk besides — and they will burn like bone-dry straw. Gone in a flash."
    },
    "11": {
      "L": "From you there came one who devised evil against the LORD, a counselor of wickedness.",
      "M": "Out of you there came one who plotted evil against the LORD — a counselor of wickedness.",
      "T": "From your midst, Nineveh, came the one who schemed against Yahweh — the architect of disaster."
    },
    "12": {
      "L": "Thus says the LORD: Though they are at full strength and many, yet they shall be cut down and pass away. Though I have afflicted you, I will afflict you no more.",
      "M": "This is what the LORD says: Even though they are at full strength and numerous, they will be cut down and pass away. Though I brought affliction upon you, I will afflict you no more.",
      "T": "This is what Yahweh says: No matter how strong and numerous they stand — they will be sheared down and swept away. I put you through the fire, Judah. But I am done. The punishment is over."
    },
    "13": {
      "L": "For now I will break his yoke from off you and burst your bonds apart.",
      "M": "And now I will break his yoke off your neck and tear your bonds apart.",
      "T": "And now — Yahweh acts: the yoke cracks, the chains snap. You are free."
    },
    "14": {
      "L": "And the LORD has commanded concerning you: no more of your name shall be sown; from the house of your gods I will cut off the carved image and the cast image; I will make your grave, for you are vile.",
      "M": "The LORD has issued his decree against you: your name will be perpetuated no longer; I will cut off the carved idol and the cast idol from the house of your gods; I will prepare your grave, for you are contemptible.",
      "T": "Yahweh has pronounced his sentence on Nineveh: the name is finished — no descendant will carry it forward. His idols — destroyed. His temple — emptied. His grave — already dug. Contemptible beyond recovery."
    },
    "15": {
      "L": "Behold, upon the mountains the feet of him who brings good news, who proclaims peace! Keep your feasts, O Judah; perform your vows; for the worthless one shall pass through you no more; he is utterly cut off.",
      "M": "See — upon the mountains the feet of the messenger who brings good news, who announces peace! Celebrate your feasts, O Judah; fulfill your vows; for the wicked will never again pass through you; he is utterly destroyed.",
      "T": "Look! There on the mountains — a runner, bringing the good news of peace! Celebrate, Judah! Keep your festivals; pay what you vowed. Nineveh is finished. The one who trampled you will never march through again — cut off, utterly, forever."
    }
  },
  "2": {
    "1": {
      "L": "The scatterer has come up against your face. Guard the ramparts; keep watch on the road; brace your loins; summon all your strength.",
      "M": "The destroyer has come up against you. Man the fortifications, watch the road, gather your strength, summon all your power.",
      "T": "The Smasher has come. Post every defender on the walls; watch every road; gird yourselves; pour out every last ounce of strength. (For all the good it will do.)"
    },
    "2": {
      "L": "For the LORD restores the excellency of Jacob as the excellency of Israel, for the emptiers have emptied them out and ruined their vine branches.",
      "M": "For the LORD is restoring the pride of Jacob as he restores the pride of Israel; for plunderers have plundered them and destroyed their vine branches.",
      "T": "For Yahweh is reclaiming the honor of Jacob and restoring Israel's dignity — because the strippers stripped them bare and wrecked every branch of their vine. Nineveh's fall is Jacob's restoration."
    },
    "3": {
      "L": "The shield of his mighty men is made red; the valiant men are clad in scarlet; the chariots blaze with torches in the day of his preparation; the cypress spears are furiously brandished.",
      "M": "The shields of his warriors are red; his fighting men are clothed in scarlet. The chariots blaze with torches on the day of muster; the cypress lances are poised to strike.",
      "T": "Blood-red shields; soldiers clad in scarlet. Chariots catching the light like torches on the day of battle. Spears of cypress raised and trembling — ready to fall."
    },
    "4": {
      "L": "The chariots race madly in the streets; they rush to and fro in the broad ways; they appear like torches; they dart like lightning.",
      "M": "The chariots race wildly through the streets; they careen through the plazas; they flash like torches; they dart like bolts of lightning.",
      "T": "Chariots screaming through the streets, crashing through the squares — flashing past like torches, vanishing like lightning. The city is consumed in its own panic."
    },
    "5": {
      "L": "He summons his officers; they stumble as they go; they hasten to the wall, and the defensive cover is set in place.",
      "M": "He calls up his officers; they stumble in their advance; they rush to the wall, and the siege shield is erected.",
      "T": "He calls his officers — but they trip over each other scrambling to the walls. Too late. The enemy's siege shield is already going up outside."
    },
    "6": {
      "L": "The gates of the rivers are opened, and the palace dissolves.",
      "M": "The floodgates of the rivers are opened, and the palace collapses.",
      "T": "The river floodgates burst. The palace itself is swept away."
    },
    "7": {
      "L": "It is decreed: she is stripped, she is led away; her attendants moan like doves, beating upon their breasts.",
      "M": "The decree goes out: she is uncovered and carried into exile; her slave girls moan like doves, beating their breasts.",
      "T": "The sentence is final. The queen of Nineveh is stripped and led away. Her attendants wail like doves — beating their chests — and follow her into captivity."
    },
    "8": {
      "L": "And Nineveh is like a pool of water whose waters run away. 'Stand! Stand!' they cry, but none turns back.",
      "M": "Nineveh is like a pool whose water drains away. 'Stop, stop!' they call — but no one turns around.",
      "T": "Nineveh is a draining pool — her people streaming out like water spilling from a cracked vessel. They shout, 'Stop! Stand and fight!' Not one looks back."
    },
    "9": {
      "L": "Plunder the silver; plunder the gold! There is no end to the store; wealth from all precious vessels.",
      "M": "Plunder the silver! Plunder the gold! The supply is endless; treasures from every precious vessel.",
      "T": "Take the silver! Take the gold! Centuries of tribute piled up — no end to it. Treasure from every storehouse in the world, looted there and now looted again."
    },
    "10": {
      "L": "She is empty, void, and waste; the heart melts and the knees knock together; anguish is in all loins, and all faces gather blackness.",
      "M": "Empty, void, and devastated! Hearts melting, knees knocking; agony in every belly; every face drained of color.",
      "T": "Empty. Hollow. Destroyed. Every heart dissolves; every knee buckles; every belly cramps with dread; every face goes ashen. This is Nineveh, stripped to nothing."
    },
    "11": {
      "L": "Where is the den of the lions, and the feeding place of the young lions, where the lion walked, the old lion and the lioness, and the lion's cub, and none made them afraid?",
      "M": "Where is the den of the lions now? Where is the place the young lions fed? Where the lion and the lioness and the lion's cubs walked without fear — and no one dared disturb them?",
      "T": "Where is the lion's den now? Where the great pride gathered — the old lion, the lioness, the cubs — and the whole earth trembled to approach? Gone. As if it never was."
    },
    "12": {
      "L": "The lion tore enough prey for his cubs and strangled prey for his lionesses; he filled his lairs with torn flesh and his dens with prey.",
      "M": "The lion tore prey enough for his cubs and strangled prey for his lionesses; he filled his dens with carcasses and his lairs with torn flesh.",
      "T": "Not long ago the lion fed the whole pride from the kill — tore and strangled without restraint. The dens ran with blood; the lairs were stacked with the flesh of nations. Nations that no longer exist."
    },
    "13": {
      "L": "Behold, I am against you, declares the LORD of hosts, and I will burn your chariots in smoke; the sword shall devour your young lions; I will cut off your prey from the earth, and the voice of your messengers shall no more be heard.",
      "M": "I am against you, declares the LORD of hosts. I will burn your chariots to smoke; the sword will devour your young warriors; I will end your plundering of the earth, and the voice of your envoys will be silenced forever.",
      "T": "Here is the verdict of Yahweh of armies: I am against you, Nineveh. Your war-machine burns. Your soldiers — devoured. Your empire of stolen wealth — ended. Your ambassadors will never again be heard giving orders to anyone."
    }
  },
  "3": {
    "1": {
      "L": "Woe to the city of blood — all of it full of lies, full of plunder; the prey never ceases!",
      "M": "Woe to the city of blood — completely full of lies, full of violent plunder, where the prey never stops!",
      "T": "Woe to the blood-soaked city! Built on lies, gorged with plunder — the killing never stops."
    },
    "2": {
      "L": "The crack of the whip, and the rumble of the wheel, and the galloping horse, and the bounding chariot!",
      "M": "Cracking whips! Rumbling wheels! Charging horses! Jolting chariots!",
      "T": "Hear it — the whip cracking! The wheels thundering! Horses at full gallop; chariots lurching and crashing through the streets!"
    },
    "3": {
      "L": "The charging horseman, the flashing sword, and the glittering spear — heaps of the slain, a great number of corpses; there is no end to the bodies; they stumble over corpses.",
      "M": "Horsemen charging, swords flashing, spears glittering — piles of the dead, heaps of corpses, no end to the bodies. They stumble over the dead.",
      "T": "Cavalry charging. Swords catching the light. Spears everywhere. The dead lie in heaps — too many to count. The living trip over those who just fell."
    },
    "4": {
      "L": "Because of the many harlotries of the harlot, graceful and deadly in sorceries, who sold nations through her harlotries and peoples through her witchcrafts —",
      "M": "Because of the countless prostitutions of the prostitute — seductive, a mistress of sorcery — who ensnared nations with her prostitutions and peoples with her witchcraft —",
      "T": "Because of the endless seductions of Nineveh — graceful, lethal, a sorceress — luring nations into ruin, enslaving whole peoples with her dark arts and imperial sorcery —"
    },
    "5": {
      "L": "Behold, I am against you, declares the LORD of hosts, and I will lift your skirts over your face and show the nations your nakedness and the kingdoms your shame.",
      "M": "I am against you, declares the LORD of hosts; I will pull your skirts up over your face; I will expose your nakedness to the nations and your shame to every kingdom.",
      "T": "This is what Yahweh of armies says: I am against you, Nineveh. I will strip you bare before the watching nations. The humiliation you dealt out — you will receive it in full public view."
    },
    "6": {
      "L": "And I will throw abominable filth at you and make you vile and set you as a spectacle.",
      "M": "I will hurl filth at you, make you contemptible, and put you on display as a public spectacle.",
      "T": "I will cover you in filth. I will make you an object of contempt. Every nation will come to stare at what has become of you."
    },
    "7": {
      "L": "And all who see you will flee from you and say, 'Nineveh is devastated; who will mourn for her?' Where shall I find comforters for you?",
      "M": "All who see you will recoil from you and say, 'Nineveh is in ruins — who will grieve for her?' Where can I find anyone to comfort you?",
      "T": "Everyone who passes will flinch and turn away: 'Nineveh — destroyed. Who weeps for her?' And there will be no one. No mourners. No comforters. No one at all."
    },
    "8": {
      "L": "Are you better than No-Amon, that sat among the rivers, the waters being round about her, whose rampart was the sea and whose wall was the sea?",
      "M": "Are you better than No-Amon — Thebes — situated among the channels of the Nile, surrounded by water, whose rampart and wall were the sea itself?",
      "T": "Are you greater than Thebes — great No-Amon — encircled by the Nile, the sea itself as her fortress wall? She thought herself invincible too. Do you not remember what happened to her?"
    },
    "9": {
      "L": "Ethiopia was her strength, and Egypt — and it was without limit; Put and Libya were among her helpers.",
      "M": "Ethiopia was her strength, along with Egypt — limitless forces; Put and Libya were counted among her allies.",
      "T": "Her coalition was massive — Ethiopia, Egypt, unlimited in numbers; Libya and the western peoples fighting at her side. Every great power of the known world stood with Thebes."
    },
    "10": {
      "L": "Yet she went into exile; she was led into captivity; also her young children were dashed in pieces at the head of every street; lots were cast for her honored men, and all her great ones were bound in chains.",
      "M": "Yet even she was exiled, taken into captivity. Her infants were dashed against the pavement at every crossroads; lots were cast for her nobles; all her leading men were shackled in chains.",
      "T": "And yet Thebes fell. Carried away in chains. Her infants smashed on the cobblestones at every street corner. Her nobles auctioned off by lot. Her great men dragged away in irons. This happened — to a city mightier than you, Nineveh."
    },
    "11": {
      "L": "You also will be drunk; you will be hidden; you also will seek refuge from the enemy.",
      "M": "You too will be staggering and helpless; you will go into hiding; you too will seek rescue from the enemy.",
      "T": "You too will reel like a drunk man. You too will vanish into hiding. You too will be begging for someone to rescue you. And no one will come."
    },
    "12": {
      "L": "All your strongholds are like fig trees with first-ripe figs — when they are shaken, they fall into the mouth of the eater.",
      "M": "All your fortresses are like fig trees laden with first-ripe figs — give them one shake and they fall right into the mouth of whoever is hungry.",
      "T": "Your fortresses — every one — are overripe figs hanging loose. One shake and they drop straight into your enemy's open mouth."
    },
    "13": {
      "L": "Behold, your people are as women in the midst of you; the gates of your land are opened wide to your enemies; fire consumes your bars.",
      "M": "Look — your fighters have lost all will in the midst of your city; the gates of your land stand wide open to your enemies; fire has devoured your gate bars.",
      "T": "Look at your defenders — they have no fight left in them. Your city gates stand open; your enemies walk straight in. The bars that should have held them are already ash."
    },
    "14": {
      "L": "Draw water for the siege; strengthen your fortresses; go into the mud and tread the clay; take hold of the brick mold!",
      "M": "Draw water for the siege! Strengthen your defenses! Go into the mud, tread the clay, take hold of the brick mold!",
      "T": "Get your water stored! Reinforce every wall! Get into the mud — tread the clay — man the brickworks and build! Build, build! None of it will save you."
    },
    "15": {
      "L": "There the fire will consume you; the sword will cut you off; it will devour you like the locust. Make yourself many as the locust; make yourself many as the grasshopper!",
      "M": "There fire will consume you; the sword will cut you down; it will devour you like a locust swarm. Multiply your numbers like a swarm of locusts, like a plague of grasshoppers!",
      "T": "In those very preparations fire will find you. The sword will finish what the fire starts. You'll be eaten like a field of grain in a locust swarm. So yes — multiply like locusts! What does it matter? The devourer is already coming."
    },
    "16": {
      "L": "You have multiplied your merchants more than the stars of heaven; the locust sheds its covering and flies away.",
      "M": "You have multiplied your merchants more than the stars of the sky; the locust strips off its casing and flies away.",
      "T": "Your merchants outnumbered the stars — trading across the whole world, enriching you with the wealth of nations. But they are like locusts: they strip the land bare, then lift their wings and vanish. In your day of disaster, not one will stay."
    },
    "17": {
      "L": "Your guards are like locusts and your officials like swarms of grasshoppers that settle in the hedges on a cold day; when the sun rises they fly away, and no one knows where they have gone.",
      "M": "Your guards are like locusts and your officials like locust swarms that camp in the walls on a cold day; when the sun rises they scatter, and no one can say where they went.",
      "T": "Your generals, your palace officials — like grasshoppers sunning themselves on a cold wall. Let the sun get hot and they vanish. Gone. No one will find them."
    },
    "18": {
      "L": "Your shepherds are sleeping, O king of Assyria; your nobles have lain down in the dust; your people are scattered on the mountains, and none gathers them.",
      "M": "Your shepherds have fallen asleep, O king of Assyria; your nobles lie fallen in the dust; your people are scattered across the mountains with no one to gather them.",
      "T": "Your generals sleep in death, O king of Assyria. Your nobles lie face-down in the dust. Your people are scattered across every mountain and valley — and not a shepherd left to find them."
    },
    "19": {
      "L": "There is no healing of your wound; your blow is fatal. All who hear the news about you clap their hands over you — for who has not felt your wickedness passing over them continually?",
      "M": "There is no healing for your wound; your injury is fatal. All who hear the news about you clap their hands — for who has not suffered your endless cruelty?",
      "T": "No cure for what has come upon you, Nineveh. The wound is mortal. When the news breaks, every nation will clap — not in grief but in relief. For who among them has not felt the lash of your endless cruelty?"
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'nahum')
        merge_tier(existing, NAHUM, tier_key)
        save(tier_dir, 'nahum', existing)
    print('Nahum 1–3 written.')

if __name__ == '__main__':
    main()
