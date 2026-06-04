"""
MKT Isaiah chapters 58–60 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-isaiah-58-60.py

Translation decisions:
- H3068 (יהוה): "LORD" (L/M) / "Yahweh" (T) — consistent with all prior Isaiah scripts.
- H430 (אֱלֹהִים): "God" in all tiers throughout these chapters.
- H6918 (קָדוֹשׁ יִשְׂרָאֵל): "Holy One of Israel" — capitalised, consistent with all prior Isaiah
  scripts. Appears at 60:9, 60:14.
- H7307 (רוּחַ): 59:19 rendered "the Spirit of the LORD" (capital S) — theologically charged; the
  wind/Spirit image is driving the divine warrior motif. 59:21 "My Spirit" — capital S; this is the
  covenant Spirit given to Israel across generations. T preserves both instances at full theological
  weight.
- H5315 (נֶפֶשׁ): 58:3,5 "afflict our/his soul" = fasting idiom for "deny ourselves"; rendered as
  reflexive in L, natural English in M. 58:10 "draw out your soul to the hungry" = pour yourself
  out; T renders as embodied self-giving. 58:11 "satisfy your soul" rendered "satisfy you" in M/T.
- H6664 (צֶדֶק) / H6666 (צְדָקָה): "righteousness" (L/M) throughout; T varies: 59:16–17 uses
  "righteousness" because the warrior/breastplate sense is in view; 59:9/14 where community-justice
  breakdown is the issue T uses "righteousness cannot find its way to us" / "stands at a distance"
  to preserve both senses. Ch. 60 retains "righteousness" because the cosmic ordering is primary.
- H3444 (יְשׁוּעָה) / H3468 (יֶשַׁע): "salvation" (L/M); T uses "deliverance" at 59:11 for the
  communal-lament tone; 60:18 "Salvation" capitalised as a proper name for the walls of Zion —
  following the naming idiom of the verse ("you shall call your walls Salvation").
- H1285 (בְּרִית): 59:21 "covenant" — formal oath-bound relationship preserved in all tiers.
- H1350 (גֹּאֵל): 59:20 "Redeemer" capitalised as a title; 60:16 likewise.
- H2617 (חֶסֶד): does not appear in these chapters.
- H6635 (צְבָאוֹת): "of hosts" — does not appear in chs. 58–60.
- H8416 (תְּהִלָּה): 60:18 "Praise" — the gates of Zion named "Praise" as proper noun. L/M both
  preserve the naming act.
- H46 (אֲבִיר): 60:16 "Mighty One" — title for God, rendered as a proper divine title in all tiers.

Structural notes:
  Ch. 58 — The True Fast. Structure: rebuke of empty fasting (vv. 1–7) → conditional promises
  for authentic covenantal practice (vv. 8–12) → sabbath unit (vv. 13–14). The rhetorical pivot is
  "Is not this the fast I choose?" (v. 6) contrasted with the hollow formalism of v. 5. The social
  justice commands (vv. 6–7) — release the oppressed, share bread, clothe the naked, do not hide
  from your own kin — are the heart of prophetic religion against its reduction to ritual.
  T captures the contrast between religious form and covenantal substance throughout.

  Ch. 59 — Why God Seems Absent. Structure: declaration of divine capability (vv. 1–2) →
  detailed sin catalog (vv. 3–8) → communal lament/confession (vv. 9–15a) → Yahweh arms himself
  as divine warrior (vv. 15b–19) → oracle of redemption (vv. 20–21). One of Isaiah's most
  sustained moral analyses. The warrior-armor image (vv. 16b–17) is echoed in Ephesians 6:14–17
  and 1 Thessalonians 5:8. The Redeemer oracle (vv. 20–21) is quoted in Romans 11:26–27.
  T preserves the NT-echo material without narrowing it to a christological reading in advance.

  Ch. 60 — The Light of Zion. One of Isaiah's great eschatological visions. Entirely poetry;
  T uses full line-break treatment throughout. Structure: proclamation of light (vv. 1–3) →
  ingathering of children and nations' wealth (vv. 4–9) → nations serve (vv. 10–16) → new order
  of peace and righteousness (vv. 17–18) → eternal light (vv. 19–20) → final promise (vv. 21–22).
  Verses 19–20 are virtually quoted at Revelation 21:23–24; v. 11 at Revelation 21:25; v. 6
  echoed at Matthew 2:11 (gold and incense).

OT echoes:
  58:6–7 — covenantal community obligations echoing Deut 15 (release of debts, care of poor).
  58:8 — "your righteousness shall go before you, the glory of the LORD shall be your rear guard"
  echoes the Exodus pillar-of-cloud imagery (Exod 14:19; Num 10:33). T marks this explicitly.
  59:16 — "his own arm brought salvation" anticipates the arm-of-the-LORD theme of Isa 53:1.
  59:17 — Armor: righteousness/breastplate, salvation/helmet, vengeance/garments, zeal/cloak.
  Paul adapts (Eph 6:14–17) but does not replace the original divine-warrior imagery.
  59:20–21 — new-covenant promise; echoes Jer 31:33 ("I will put my law within them"). The Spirit
  and the word persisting across generations is the covenant-renewal idiom.
  60:1–3 — echoes Isa 9:2 ("the people who walked in darkness have seen a great light").
  60:19–20 — anticipates Rev 21:23 and John 8:12; T preserves the forward-looking orientation.

Aspect notes:
  58:8 conditional sequence: the waw-consecutive imperfects that follow "if you fast truly" are
  confident futures. T gives them present-tense immediacy.
  59:1 stative perfects: "is not shortened... is not heavy" — permanent qualities of Yahweh's arm
  and ear; L preserves the stative force.
  59:15b–19 — weqatal sequence: Yahweh's purposeful acts as divine warrior narrated as a
  determinate chain.
  60:1 imperatives: "Arise! Shine!" — urgent present calls to a future that is already arriving.
  60:22 paradox of scheduled urgency: "I will hasten it in its time" — the time is fixed; the
  arrival will be sudden. T honours both.
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
  "58": {
    "1": {
      "L": "Cry aloud; spare not; lift up your voice like a trumpet; declare to my people their transgression and to the house of Jacob their sins.",
      "M": "Cry out loudly; do not hold back; raise your voice like a trumpet and tell my people their rebellion and the house of Jacob their sins.",
      "T": "Cry out at full volume — do not hold back. Raise your voice like a trumpet. Tell my people what they have done wrong; tell the house of Jacob their sins."
    },
    "2": {
      "L": "Yet they seek me daily and delight to know my ways, as if they were a nation that practiced righteousness and did not forsake the ordinance of their God; they ask of me righteous ordinances; they delight to draw near to God.",
      "M": "Yet day after day they seek me and are eager to know my ways, as though they were a nation that practices righteousness and has not abandoned the law of their God; they ask of me just decrees and are pleased to draw near to God.",
      "T": "And yet — every single day they seek me. They are eager to know my ways, as if they were a people who actually practiced righteousness, who never abandoned their God's commands. They ask me for just decrees. They claim to delight in coming near to God."
    },
    "3": {
      "L": "Why have we fasted, and you see it not? Why have we humbled ourselves, and you take no knowledge of it? Behold, in the day of your fast you seek your own pleasure and drive all your workers hard.",
      "M": "They say, 'Why have we fasted, but you do not notice? Why have we denied ourselves, and you take no account of it?' Look — on your fast day you pursue your own interests and push all your laborers.",
      "T": "They ask: 'Why have we fasted if you don't see it? Why have we afflicted ourselves and you take no notice?' Here is why: on the very day of your fasting you are chasing your own pleasure — and driving your workers to the bone."
    },
    "4": {
      "L": "Behold, you fast only to quarrel and to fight, to strike with a wicked fist. You shall not fast as you do today to make your voice heard on high.",
      "M": "Look, you fast only to quarrel and brawl and to strike with a wicked fist. You cannot fast as you do today and expect your voice to be heard on high.",
      "T": "Look — you fast so you can get into arguments and throw punches. A fast like that will never send your prayers to heaven."
    },
    "5": {
      "L": "Is this the fast that I choose, a day for a person to humble himself — to bow down his head like a bulrush and spread sackcloth and ashes under him? Will you call this a fast and a day acceptable to the LORD?",
      "M": "Is this the kind of fast I have chosen — merely a day for people to deny themselves, to bow their heads like a reed and spread sackcloth and ashes beneath them? Is that what you call a fast, a day acceptable to the LORD?",
      "T": "Is that the fast I have chosen — a day of self-deprivation? Bowing your head like a reed? Lying in sackcloth and ashes? Is that what you call a fast? Is that an acceptable day before Yahweh?"
    },
    "6": {
      "L": "Is not this the fast that I choose: to loose the bonds of wickedness, to undo the straps of the yoke, to let the oppressed go free, and to break every yoke?",
      "M": "Is not this the fast I choose: to release the bonds of injustice, to untie the ropes of the yoke, to set the oppressed free, and to break every yoke?",
      "T": "This is the fast I choose: loosen every chain of injustice. Untie the ropes of every yoke. Set the oppressed free. Break every yoke — every single one."
    },
    "7": {
      "L": "Is it not to share your bread with the hungry and bring the homeless poor into your house; when you see the naked, to cover him, and not to hide yourself from your own flesh?",
      "M": "Is it not to share your food with the hungry, to bring the wandering poor into your home, to clothe the naked when you see them, and not to look away from your own kin?",
      "T": "It is to break your bread with the hungry. To open your home to the homeless poor. To clothe the naked when you see one. Not to look the other way when it is your own family."
    },
    "8": {
      "L": "Then your light shall break forth like the dawn, and your healing shall spring up speedily; your righteousness shall go before you, and the glory of the LORD shall be your rear guard.",
      "M": "Then your light will break out like the dawn, and your recovery will come quickly; your righteousness will lead the way before you, and the glory of the LORD will be your rear guard.",
      "T": "Then your light will burst out like the dawn. Your healing will spring up without delay. Your righteousness will march before you like a vanguard, and the glory of Yahweh will cover your back — as it did in the old Exodus."
    },
    "9": {
      "L": "Then you shall call, and the LORD will answer; you shall cry, and he will say, 'Here I am.' If you remove the yoke from your midst, the pointing of the finger, and speaking wickedness,",
      "M": "Then you will call and the LORD will answer; you will cry and he will say, 'Here I am.' If you remove the yoke from among you, stop the pointing finger, and stop speaking wickedness,",
      "T": "Then you will call out and Yahweh will answer. You will cry and he will say: 'Here I am.' If you stop putting the yoke on people's necks, if you stop pointing the accusing finger, if you stop muttering malice —"
    },
    "10": {
      "L": "if you pour out your soul to the hungry and satisfy the desire of the afflicted, then your light shall rise in the darkness and your gloom shall be as the noonday.",
      "M": "if you give yourself to the hungry and satisfy the needs of the oppressed, then your light will rise in the darkness and your deepest night will become as bright as noon.",
      "T": "if you pour yourself out for the hungry and meet the need of the suffering — then your light will rise in the darkness and your darkest night will blaze like midday."
    },
    "11": {
      "L": "And the LORD will guide you continually and satisfy your desire in parched places and make your bones strong; and you shall be like a watered garden, like a spring of water whose waters do not fail.",
      "M": "The LORD will guide you continually and satisfy you in dry places and strengthen your bones; you will be like a well-watered garden, like a spring whose waters never run dry.",
      "T": "Yahweh will be your constant guide. He will satisfy you in the scorched wilderness and give strength to your bones. You will be like a garden that is always well-watered, like a spring whose waters never fail."
    },
    "12": {
      "L": "And your people shall rebuild the ancient ruins; you shall raise up the foundations of many generations; you shall be called the Repairer of the Breach, the Restorer of Streets to Dwell In.",
      "M": "Your people will rebuild the ancient ruins; you will raise up the foundations of many generations; you will be called the Repairer of the Breach, the Restorer of Paths to Live In.",
      "T": "Your people will rebuild what was ruined long ago. You will raise up foundations that go back generations. You will be called the Repairer of the Breach, the Restorer of Streets to Live In."
    },
    "13": {
      "L": "If you turn back your foot from the Sabbath, from doing your own pleasure on my holy day, and call the Sabbath a delight and the holy day of the LORD honorable; if you honor it by not going your own ways, or seeking your own pleasure, or speaking idle words,",
      "M": "If you keep your feet from breaking the Sabbath and refrain from doing as you please on my holy day; if you call the Sabbath a delight and the LORD's holy day worthy of honor; if you honor it by not following your own ways or pursuing your own pleasures or talking idly,",
      "T": "If you hold back from the Sabbath — stop doing what you please on my holy day — and call the Sabbath a delight, and the LORD's holy day something worth honoring; if you honor it by not going your own way, not chasing your own pleasure, not filling it with empty chatter —"
    },
    "14": {
      "L": "then you shall take delight in the LORD, and I will make you ride upon the heights of the earth; I will feed you with the heritage of Jacob your father, for the mouth of the LORD has spoken.",
      "M": "then you will find your joy in the LORD, and I will make you ride on the heights of the earth; I will nourish you with the heritage of Jacob your father — for the mouth of the LORD has spoken.",
      "T": "then you will find your delight in Yahweh, and I will set you riding on the high places of the earth. I will feed you on the heritage of Jacob your father. The mouth of Yahweh has spoken it."
    }
  },
  "59": {
    "1": {
      "L": "Behold, the LORD's hand is not shortened, that it cannot save, nor his ear heavy, that it cannot hear;",
      "M": "See, the LORD's arm is not too short to save, nor his ear too dull to hear;",
      "T": "Look — Yahweh's arm is not too short to rescue. His ear has not gone deaf."
    },
    "2": {
      "L": "but it is your iniquities that have made a separation between you and your God, and your sins have hidden his face from you so that he does not hear.",
      "M": "but your iniquities have created a barrier between you and your God, and your sins have caused him to hide his face from you so that he does not hear.",
      "T": "No — it is your own wrongs that have cut you off from your God. Your sins have made him hide his face from you, which is why he does not hear."
    },
    "3": {
      "L": "For your hands are defiled with blood and your fingers with iniquity; your lips have spoken lies; your tongue mutters wickedness.",
      "M": "For your hands are stained with blood and your fingers with guilt; your lips have spoken lies and your tongue mutters deceit.",
      "T": "Your hands are stained with blood. Your fingers are soaked in guilt. Your lips have lied. Your tongue mutters its corruption."
    },
    "4": {
      "L": "No one calls for justice; no one pleads in truth; they rely on empty arguments, they speak lies; they conceive mischief and bring forth iniquity.",
      "M": "No one calls for justice; no one pleads with integrity; they depend on worthless arguments and speak lies; they conceive evil and give birth to wickedness.",
      "T": "No one is calling for justice. No one is arguing in good faith. They lean on worthless charges, they speak what is false. They are pregnant with mischief — and they will give birth to wickedness."
    },
    "5": {
      "L": "They hatch adder's eggs and weave the spider's web; whoever eats their eggs dies, and from a crushed egg a viper is hatched.",
      "M": "They hatch the eggs of vipers and weave a spider's web; whoever eats their eggs will die, and if one is cracked, a poisonous snake emerges.",
      "T": "They are hatching snake eggs and spinning spider webs. Eat one of those eggs and you die. Crack one open and a viper crawls out."
    },
    "6": {
      "L": "Their webs will not serve as clothing; they cannot cover themselves with what they make. Their works are works of iniquity, and deeds of violence are in their hands.",
      "M": "Their webs will not serve as clothing; they cannot cover themselves with what they weave. Their works are works of wickedness, and their hands carry out violence.",
      "T": "You cannot wear a spider's web. You cannot cover yourself with something that falls apart. Everything they make is wickedness. Violence is what their hands are full of."
    },
    "7": {
      "L": "Their feet run to evil, and they make haste to shed innocent blood; their thoughts are thoughts of iniquity; desolation and destruction are in their paths.",
      "M": "Their feet rush toward evil, and they are quick to shed innocent blood; their thoughts are plots of wickedness; ruin and destruction mark their ways.",
      "T": "They sprint toward evil. They cannot wait to spill innocent blood. Wickedness is all they think about. Wherever they go, they leave devastation behind."
    },
    "8": {
      "L": "The way of peace they do not know, and there is no justice in their paths; they have made their roads crooked; no one who walks on them knows peace.",
      "M": "They do not know the way of peace, and there is no justice in their tracks; they have bent every path crooked, and no one who walks them knows peace.",
      "T": "They do not know the way of peace. There is no justice in any of their tracks. They have twisted every road they travel — and anyone who takes those roads finds no peace."
    },
    "9": {
      "L": "Therefore justice is far from us, and righteousness does not overtake us; we hope for light, but behold, there is darkness; for brightness, but we walk in gloom.",
      "M": "Therefore justice is far from us, and righteousness does not reach us; we wait for light, but there is only darkness; for brightness, but we walk in deep shadow.",
      "T": "That is why justice stays far from us. Righteousness cannot find its way to us. We wait for light — and what comes is darkness. We wait for brightness — and we walk in shadow."
    },
    "10": {
      "L": "We grope for the wall like the blind; we grope like those who have no eyes; we stumble at noon as in the twilight; among those in full vigor we are like dead men.",
      "M": "We grope along the wall like blind men; we fumble like those with no eyes; we stumble at midday as in the dusk; among the healthy we are like the dead.",
      "T": "We feel along the wall like the blind, groping in the dark as if we have no eyes at all. We trip in the noon sun as if it were midnight. Among the living, we are like the dead."
    },
    "11": {
      "L": "We all growl like bears; we moan and moan like doves; we look for justice, but there is none; for salvation, but it is far from us.",
      "M": "We all growl like bears and moan like doves; we look for justice, but there is none; for deliverance, but it is far away.",
      "T": "We growl like bears, the whole lot of us. We moan like doves. We long for justice — there is none. We look for deliverance — it is far away."
    },
    "12": {
      "L": "For our transgressions are multiplied before you, and our sins testify against us; our transgressions are with us, and we know our iniquities:",
      "M": "For our rebellions are multiplied before you, and our sins testify against us; we are deeply aware of our transgressions and we know our own iniquities:",
      "T": "Our rebellions have piled up before you. Our sins stand against us as witnesses. We cannot deny our transgressions — we know our own wrongs:"
    },
    "13": {
      "L": "transgressing and denying the LORD, and turning back from following our God, speaking oppression and revolt, conceiving and uttering from the heart lying words.",
      "M": "We have rebelled against and denied the LORD; we have turned away from following our God; we have spoken oppression and treachery, we have conceived and repeated from our hearts words of falsehood.",
      "T": "We have rebelled against Yahweh. We have denied him. We have turned our backs on our God. We spoke oppression. We plotted revolt. We conceived lies in our hearts and gave them voice."
    },
    "14": {
      "L": "Justice is turned back, and righteousness stands far off; for truth has stumbled in the public squares, and uprightness cannot enter.",
      "M": "So justice has been driven back, and righteousness stands at a distance; for truth has fallen in the streets, and honesty cannot get through.",
      "T": "Justice has been turned on its head. Righteousness stands at a distance. Truth has collapsed in the public square. Honesty cannot find a way in."
    },
    "15": {
      "L": "Truth is lacking, and he who departs from evil makes himself a prey. The LORD saw it, and it was evil in his eyes that there was no justice.",
      "M": "Truth has vanished, and anyone who turns from evil exposes himself to attack. The LORD saw it, and it displeased him that there was no justice.",
      "T": "Truth has gone missing. Anyone who refuses to go along with evil becomes a target. Yahweh saw it all — and he was appalled that there was no justice left."
    },
    "16": {
      "L": "He saw that there was no man, and wondered that there was no one to intercede; then his own arm brought him salvation, and his righteousness sustained him.",
      "M": "He saw that there was no man, and was astounded that there was no one to intervene; so his own arm achieved salvation for him, and his own righteousness upheld him.",
      "T": "He looked — there was no one. Not a single person willing to step in. He was astonished that no one was interceding. So his own arm brought the rescue needed, and his own righteousness held him up."
    },
    "17": {
      "L": "He put on righteousness as a breastplate, and a helmet of salvation on his head; he put on garments of vengeance for clothing, and wrapped himself in zeal as a cloak.",
      "M": "He put on righteousness as a breastplate and a helmet of salvation on his head; he clothed himself in garments of vengeance and wrapped himself in zeal like a cloak.",
      "T": "He armed himself with righteousness as a breastplate. He put on salvation as a helmet. He dressed in garments of vengeance. He wrapped himself in zeal like a war-cloak."
    },
    "18": {
      "L": "According to their deeds, so will he repay — wrath to his adversaries, repayment to his enemies; to the coastlands he will render repayment.",
      "M": "According to what they have done, so he will repay — fury to his foes, punishment to his enemies; he will pay back even the distant coastlands.",
      "T": "He will pay everyone according to what they have done: fury to his adversaries, judgment to his enemies — the distant coastlands included. No one is exempt."
    },
    "19": {
      "L": "So they shall fear the name of the LORD from the west, and his glory from the rising of the sun; for he will come like a pent-up flood which the Spirit of the LORD drives along.",
      "M": "And from the west they will fear the name of the LORD, and from the east his glory; for he will come like a rushing torrent driven by the Spirit of the LORD.",
      "T": "And so, from west to east — from the setting sun to the rising —\nthey will fear the name of Yahweh,\nthey will fear his glory.\nFor he will come like a flooding river,\ndriven forward by the Spirit of Yahweh."
    },
    "20": {
      "L": "And a Redeemer will come to Zion, to those in Jacob who turn from transgression, declares the LORD.",
      "M": "A Redeemer will come to Zion, to those in Jacob who turn from their rebellion, declares the LORD.",
      "T": "A Redeemer will come to Zion — to those in Jacob who have turned back from their rebellion. Yahweh declares it."
    },
    "21": {
      "L": "And as for me, this is my covenant with them, says the LORD: My Spirit that is upon you, and my words that I have put in your mouth, shall not depart from your mouth or from the mouth of your offspring or from the mouth of your children's offspring, says the LORD, from this time forth and forevermore.",
      "M": "And as for me, this is my covenant with them, says the LORD: My Spirit that is upon you and my words that I have placed in your mouth shall not leave your mouth, nor the mouth of your children, nor the mouth of your grandchildren, says the LORD, from now on and forever.",
      "T": "And this is my covenant with them — Yahweh speaks it: My Spirit, which rests on you, and my words, which I have placed in your mouth — they will not leave your mouth, nor the mouth of your children, nor the mouth of your grandchildren, says Yahweh — from this moment and for all time to come."
    }
  },
  "60": {
    "1": {
      "L": "Arise, shine, for your light has come, and the glory of the LORD has risen upon you.",
      "M": "Arise, shine, for your light has come; the glory of the LORD has risen over you.",
      "T": "Rise up! Shine!\nFor your light has come,\nand the glory of Yahweh\nhas risen upon you."
    },
    "2": {
      "L": "For behold, darkness shall cover the earth, and thick darkness the peoples; but the LORD will arise over you, and his glory will be seen upon you.",
      "M": "For darkness covers the earth, and thick darkness the peoples; but the LORD will rise over you, and his glory will appear upon you.",
      "T": "See — darkness covers the earth,\nand deep darkness blankets the nations;\nbut Yahweh rises over you,\nand his glory appears on you."
    },
    "3": {
      "L": "And nations shall come to your light, and kings to the brightness of your rising.",
      "M": "Nations will come to your light, and kings to the brightness of your dawn.",
      "T": "Nations will walk toward your light.\nKings will come to the brightness of your rising."
    },
    "4": {
      "L": "Lift up your eyes all around and see; they all gather and come to you; your sons shall come from afar, and your daughters shall be carried on the hip.",
      "M": "Lift your eyes all around and look: they are all assembling and coming to you; your sons will come from far away, and your daughters will be carried on the arm.",
      "T": "Lift your eyes — look around — they are all gathering, all coming to you.\nYour sons are coming from far away;\nyour daughters are being carried on the hip."
    },
    "5": {
      "L": "Then you shall see and be radiant; your heart shall thrill and rejoice, because the abundance of the sea shall be turned to you, the wealth of the nations shall come to you.",
      "M": "Then you will see and be radiant; your heart will thrill and overflow, because the wealth of the seas will be channeled to you and the riches of the nations will come to you.",
      "T": "When you see it, you will shine.\nYour heart will pound with joy — it will overflow —\nbecause the wealth of the seas is streaming toward you\nand the riches of the nations are coming."
    },
    "6": {
      "L": "A multitude of camels shall cover you, the young camels of Midian and Ephah; all those from Sheba shall come. They shall bring gold and incense, and shall proclaim the praises of the LORD.",
      "M": "A great herd of camels will cover your land — the young camels of Midian and Ephah; all from Sheba will come, bringing gold and incense and proclaiming the praises of the LORD.",
      "T": "A flood of camels will cover you —\nthe young camels of Midian and Ephah.\nAll of them coming from Sheba,\nbringing gold and incense,\nproclaiming the praises of Yahweh."
    },
    "7": {
      "L": "All the flocks of Kedar shall be gathered to you; the rams of Nebaioth shall minister to you; they shall come up with acceptance on my altar, and I will beautify my beautiful house.",
      "M": "All the flocks of Kedar shall be gathered to you; the rams of Nebaioth shall serve you; they shall come up as acceptable offerings on my altar, and I will adorn my glorious house.",
      "T": "Every flock of Kedar will be gathered to you.\nThe rams of Nebaioth will come as your servants —\ngoing up to my altar as acceptable offerings.\nI will make my glorious house more glorious still."
    },
    "8": {
      "L": "Who are these that fly like a cloud, like doves to their windows?",
      "M": "Who are these that fly along like a cloud, like doves returning to their nests?",
      "T": "Who are these — flying like a cloud,\nlike doves banking toward their home?"
    },
    "9": {
      "L": "For the coastlands shall wait for me, the ships of Tarshish first, to bring your children from afar, their silver and gold with them, for the name of the LORD your God, and for the Holy One of Israel, because he has made you beautiful.",
      "M": "Surely the coastlands wait for me, and the ships of Tarshish are first, to bring your children from afar, their silver and gold with them, for the name of the LORD your God and for the Holy One of Israel, for he has made you glorious.",
      "T": "The coastlands are waiting for me — Tarshish's ships are first in line —\nto bring your children from far away,\ntheir silver and gold with them,\nfor the name of Yahweh your God,\nfor the Holy One of Israel —\nbecause he has made you beautiful."
    },
    "10": {
      "L": "Foreigners shall build up your walls, and their kings shall serve you; for in my wrath I struck you, but in my favor I have had mercy on you.",
      "M": "Foreigners will rebuild your walls and their kings will serve you; though in my anger I struck you, in my compassion I have shown mercy to you.",
      "T": "Foreigners will rebuild your walls.\nTheir kings will be your servants.\nFor in my anger I struck you —\nbut in my favor I have had compassion on you."
    },
    "11": {
      "L": "Your gates shall be open continually; day and night they shall not be shut, that people may bring to you the wealth of the nations, with their kings led in procession.",
      "M": "Your gates will stand open continually; they will not be shut by day or night, so that people may bring you the wealth of the nations, with their kings escorted in.",
      "T": "Your gates will stand open without ceasing —\nday and night they will never be shut —\nso that the wealth of the nations may keep flowing in,\nand their kings led in procession."
    },
    "12": {
      "L": "For the nation and kingdom that will not serve you shall perish; those nations shall be utterly laid waste.",
      "M": "For the nation and kingdom that will not serve you shall be destroyed; such nations shall be completely devastated.",
      "T": "The nation that refuses to serve you will perish.\nThe kingdom that will not submit — it will be utterly laid waste."
    },
    "13": {
      "L": "The glory of Lebanon shall come to you — the cypress, the plane, and the pine — to adorn the place of my sanctuary, and I will make the place of my feet glorious.",
      "M": "The splendor of Lebanon will come to you — the juniper, the fir, and the box tree together — to adorn the place of my sanctuary, and I will make the place where my feet rest glorious.",
      "T": "Lebanon's glory will come to you —\ncypress, pine, and box tree together —\nto adorn the place of my sanctuary\nand to make the place of my feet glorious."
    },
    "14": {
      "L": "The sons of those who oppressed you shall come bowing to you; all who despised you shall bow down at your feet; they shall call you the City of the LORD, the Zion of the Holy One of Israel.",
      "M": "The descendants of those who tormented you will come bowing down before you; all who despised you will prostrate themselves at your feet; they will call you the City of the LORD, the Zion of the Holy One of Israel.",
      "T": "The children of those who once crushed you\nwill come and bow themselves before you.\nAll who despised you will fall at your feet\nand call you the City of Yahweh —\nthe Zion of the Holy One of Israel."
    },
    "15": {
      "L": "Whereas you have been forsaken and hated, with no one passing through, I will make you an eternal majesty, a joy from generation to generation.",
      "M": "Although you have been forsaken and despised, with no one traveling through you, I will make you an everlasting pride and a source of joy for all generations.",
      "T": "You were forsaken. You were despised.\nNo one walked through you.\nBut I will make you a glory that lasts forever,\na joy from one generation to the next."
    },
    "16": {
      "L": "You shall suck the milk of nations; you shall nurse at the breast of kings; and you shall know that I, the LORD, am your Savior and your Redeemer, the Mighty One of Jacob.",
      "M": "You will drink the milk of the nations and nurse at the breast of kings; and you will know that I, the LORD, am your Savior, your Redeemer, the Mighty One of Jacob.",
      "T": "You will feed on the wealth of nations;\nyou will draw from the abundance of kings.\nAnd you will know that I, Yahweh, am your Savior —\nyour Redeemer, the Mighty One of Jacob."
    },
    "17": {
      "L": "Instead of bronze I will bring gold, and instead of iron I will bring silver; instead of wood, bronze, and instead of stones, iron. I will make your overseers peace and your taskmasters righteousness.",
      "M": "Instead of bronze I will bring gold, and instead of iron, silver; instead of wood, bronze, and instead of stones, iron. I will make peace your governor and righteousness your ruler.",
      "T": "Where there was bronze, I will bring gold.\nWhere there was iron, silver.\nWhere there was wood, bronze.\nWhere there were stones, iron.\nI will appoint Peace as your governor,\nand Righteousness as your ruling power."
    },
    "18": {
      "L": "Violence shall no more be heard in your land, devastation or destruction within your borders; you shall call your walls Salvation, and your gates Praise.",
      "M": "Violence will no longer be heard in your land, nor ruin or destruction within your borders; you will name your walls Salvation and your gates Praise.",
      "T": "No more will violence be heard in your land —\nno devastation, no ruin within your borders.\nYou will call your walls Salvation.\nYou will call your gates Praise."
    },
    "19": {
      "L": "The sun shall be no more your light by day, nor shall the moon give you light for brightness; but the LORD will be your everlasting light, and your God will be your glory.",
      "M": "The sun will no longer be your light by day, nor will the brightness of the moon give you light; but the LORD will be your everlasting light, and your God will be your glory.",
      "T": "The sun will no longer be your daylight.\nThe moon will no longer be your brightness.\nYahweh himself will be your everlasting light,\nand your God will be your glory."
    },
    "20": {
      "L": "Your sun shall no more go down, nor shall your moon withdraw itself; for the LORD will be your everlasting light, and your days of mourning shall be ended.",
      "M": "Your sun will never set again, nor will your moon wane; for the LORD will be your everlasting light, and your days of grief will be over.",
      "T": "Your sun will never set again.\nYour moon will not withdraw.\nYahweh is your everlasting light —\nand your days of mourning will be finished."
    },
    "21": {
      "L": "Your people shall all be righteous; they shall possess the land forever, the branch of my planting, the work of my hands, that I might be glorified.",
      "M": "Your people will all be righteous; they will possess the land forever — the shoot I have planted, the work of my hands — so that I might be glorified.",
      "T": "Your people — every one of them — will be righteous.\nThey will possess the land forever.\nThey are the shoot I planted,\nthe work of my own hands,\nso that I might be glorified."
    },
    "22": {
      "L": "The least one shall become a clan, and the smallest one a mighty nation; I, the LORD, will hasten it in its time.",
      "M": "The least will become a thousand, and the smallest a mighty nation; I, the LORD, will bring it to pass at the right time.",
      "T": "The least among them will become a whole clan.\nThe smallest will become a mighty nation.\nI, Yahweh, will bring it to pass —\nand I will hasten it when the time comes."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'isaiah')
        merge_tier(existing, ISAIAH, tier_key)
        save(tier_dir, 'isaiah', existing)
    print('Isaiah 58–60 written.')

if __name__ == '__main__':
    main()
