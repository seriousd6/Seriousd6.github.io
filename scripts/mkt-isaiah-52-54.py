"""
MKT Isaiah chapters 52–54 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-isaiah-52-54.py

Translation decisions:
- H3068 (יהוה): "LORD" (L/M) / "Yahweh" (T) — carried forward from all prior Isaiah scripts.
- H430 (אֱלֹהִים): "God" throughout all tiers — consistent with prior Isaiah scripts.
- H136+H3069 (אֲדֹנָי יְהוִה): "Lord GOD" (L) / "Sovereign LORD" (M) / "Sovereign Yahweh" (T) —
  52:4 only; the doubled divine title signals the covenantal authority of the speaker.
- H1350 (גָּאַל): "redeemed" / "Redeemer" — kinsman-redeemer obligation; covenantal rescue,
  not merely generic deliverance; also translated "Kinsman-Redeemer" in T at 54:5 to
  surface the legal/relational background.
- H2617 (חֶסֶד): "steadfast love" (L) / "covenant love" (M) / "love that will never end" or
  "covenant loyalty" (T) — 54:8,10; the Hebrew's irreducible combination of obligation and
  active loving-kindness; T makes duration and covenant quality explicit.
- H1285 (בְּרִית): "covenant" — 54:10 "covenant of peace"; the formal, oath-bound relationship.
- H5650 (עֶבֶד): "servant" throughout — the Servant Songs designation; 52:13 opens the Fourth
  Servant Song; 53 is its central body.
- H5771 (עָוֹן): "iniquities" (L/M) / "guilt" or "guilt we accumulated" (T) — 53:6,11; the
  accumulated moral debt/distortion borne by the Servant.
- H6588 (פֶּשַׁע): "transgressions" (L/M) / "rebellions" (T) — 53:5,8,12; willful covenant
  violation; T uses "rebellions" to surface the active defiance in the word.
- H817 (אָשָׁם): "guilt offering" (L) / "guilt offering" (M) / "atoning sacrifice" (T) — 53:10;
  the specific sacrificial category for reparatory atonement (Lev 5:14-19); this is the only
  OT use outside Levitical law that applies it to a person; T renders "atoning sacrifice" to
  convey its weight without being merely technical.
- H2483 (חֳלִי): "griefs" (L) / "sicknesses" (M) / "sicknesses" (T) — 53:4; the Hebrew root
  denotes illness/disease before sorrow; Matt 8:17 applies this verse to physical healing;
  T and M surface the physical sense; L retains "griefs" as the traditional rendering while
  noting the semantic range.
- H4341 (מַכְאֹב): "sorrows" (L/M) / "pain" (T) — 53:3,4; physical and emotional suffering;
  parallel with חֳלִי; T uses "pain" to match the bodily register.
- H5315 (נֶפֶשׁ): 53:10,11,12 — "soul" (L) but in context always refers to the Servant's
  embodied person/life; M renders "life" at 53:10,12; T renders "life" throughout to avoid
  importing Greek immaterial-soul concepts into a Hebrew text.
- H6662 (צַדִּיק): "righteous one" (L/M/T) — 53:11; the Servant is morally faultless;
  the causative verb H6663 (צָדַק hiphil) = "justify / make righteous / acquit" — rendered
  "justify" (L) / "make righteous" (M) / "make righteous" (T); this is the forensic
  declaration and its transformative result held together.
- H7307 (רוּחַ): 54:6 "grieved in spirit" — human emotional spirit, not divine; lowercase.
- H4893 (מִשְׁחַת): 52:14 — "marred / disfigured beyond human form"; the extreme physical
  destruction of the Servant's appearance is part of the scandal; T names it explicitly.
- H5137 (נָזָה): 52:15 — traditionally "sprinkle" (a priestly act of cleansing/consecration);
  some scholars prefer "startle"; retained as "sprinkle" (L), contextualised as "startle" in
  M/T following the wider interpretive tradition that sees both meanings operative (the
  nations are both shocked and purified/consecrated).
- Poetry/prose: Chs. 52 and 54 are prophetic poetry; T uses line breaks. Ch. 53 is the
  Fourth Servant Song — highly structured poetry; T uses line breaks throughout and aims
  for poetic cadence appropriate to this uniquely weighty text.
- 52:4-6 prose interruption: these three verses shift to prose explanation within the poem;
  L/M reflect prose; T uses looser structure.
- 53:8 — "cut off from the land of the living" is a death idiom; the verse describes a
  judicial execution; "by a corrupt trial" (T) reflects the Hebrew sense of a perversion
  of mishpat (H4941, justice/judgment).
- 53:9 — "his grave with the wicked / burial with the rich": the paradox (wicked burial /
  rich tomb) is preserved; this is one of the most discussed textual details; both the MT
  and LXX support the duality; T preserves the tension.
- 54:11 — H6320 (פּוּךְ) is antimony/black eye-paint used as mortar to make stones gleam;
  rendered "brilliant colour" in M/T to convey the decorative lustre without the obscure
  technical term; L retains "antimony" to mark the specific material.
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
  "52": {
    "1": {
      "L": "Awake, awake, put on your strength, O Zion; put on your beautiful garments, O Jerusalem, the holy city; for never again shall the uncircumcised and the unclean enter you.",
      "M": "Wake up, wake up! Clothe yourself with strength, O Zion! Put on your beautiful garments, Jerusalem, holy city! The uncircumcised and the unclean will enter you no more.",
      "T": "Wake up! Wake up, Zion —\nput on your strength!\nDress yourself in your finest, Jerusalem, the holy city!\nThe uncircumcised and the unclean\nwill never walk your streets again."
    },
    "2": {
      "L": "Shake yourself from the dust, arise, sit down, O Jerusalem; loose yourself from the bonds of your neck, O captive daughter of Zion.",
      "M": "Shake off the dust, rise up, sit enthroned, Jerusalem! Loose yourself from the chains around your neck, captive daughter of Zion!",
      "T": "Shake the dust from yourself — rise up, Jerusalem!\nTake your throne!\nFree yourself from the chains around your neck,\ncaptive daughter of Zion."
    },
    "3": {
      "L": "For thus says the LORD: You were sold for nothing, and you shall be redeemed without silver.",
      "M": "For this is what the LORD says: 'You were sold for nothing, and without silver you will be redeemed.'",
      "T": "For here is what Yahweh says:\n'You went into slavery for nothing —\nno price was paid for you.\nAnd no price will be required to set you free.'"
    },
    "4": {
      "L": "For thus says the Lord GOD: My people went down to Egypt at the first to sojourn there, and the Assyrian has oppressed them without cause.",
      "M": "For this is what the Sovereign LORD says: 'My people first went down to Egypt to live there as foreigners, and the Assyrian oppressed them for no reason.'",
      "T": "For here is what the Sovereign Yahweh says:\n'My people went down to Egypt in the beginning —\nthey went as strangers seeking refuge.\nThen Assyria crushed them, for no reason at all.'"
    },
    "5": {
      "L": "Now therefore what have I here, declares the LORD? For my people is taken away for nothing; those who rule over them wail, declares the LORD, and continually all the day my name is despised.",
      "M": "'What, then, do I have here?' declares the LORD. 'My people have been taken away for nothing; those who rule over them howl,' declares the LORD, 'and day after day my name is constantly despised.'",
      "T": "'So what do I gain from this?' declares Yahweh.\n'My people are taken away without payment.\nTheir rulers strut and mock,' declares Yahweh,\n'and day after day my name is treated with contempt.'"
    },
    "6": {
      "L": "Therefore my people shall know my name; therefore on that day they shall know that it is I who speak; here am I.",
      "M": "'Therefore my people will know my name; therefore on that day they will know that I am the one who says, Here I am.'",
      "T": "'Therefore my people will know who I am.\nOn that day they will recognise the one who speaks:\nHere I am.'"
    },
    "7": {
      "L": "How beautiful upon the mountains are the feet of him who brings good news, who proclaims peace, who brings good news of good, who proclaims salvation, who says to Zion, Your God reigns!",
      "M": "How beautiful on the mountains are the feet of the messenger who brings good news, who proclaims peace, who brings tidings of good and announces salvation — who says to Zion, 'Your God reigns!'",
      "T": "How beautiful on the mountains\nare the feet of the herald who brings good news —\nwho announces peace,\nwho proclaims what is good,\nwho brings the news of rescue\nand says to Zion: Your God is King!"
    },
    "8": {
      "L": "The voice of your watchmen — they lift up their voice; together they sing for joy; for eye to eye they see the return of the LORD to Zion.",
      "M": "Listen! Your watchmen raise their voices; together they shout for joy! For they see eye to eye when the LORD returns to Zion.",
      "T": "Listen — your watchmen are shouting together!\nThey break into joyful singing —\nfor with their own eyes, right in front of them,\nthey see Yahweh returning to Zion."
    },
    "9": {
      "L": "Break forth together into singing, you waste places of Jerusalem, for the LORD has comforted his people; he has redeemed Jerusalem.",
      "M": "Burst together into singing, you ruins of Jerusalem! For the LORD has comforted his people; he has redeemed Jerusalem.",
      "T": "Burst into song together, you ruins of Jerusalem —\nfor Yahweh has comforted his people;\nhe has redeemed Jerusalem."
    },
    "10": {
      "L": "The LORD has bared his holy arm before the eyes of all the nations, and all the ends of the earth shall see the salvation of our God.",
      "M": "The LORD has bared his holy arm in the sight of all the nations, and all the ends of the earth will see the salvation of our God.",
      "T": "Yahweh has rolled back his sleeve —\nhis holy arm bare before every nation.\nEvery corner of the earth will see\nwhat our God does to save."
    },
    "11": {
      "L": "Depart, depart, go out from there; touch no unclean thing; go out from the midst of her; purify yourselves, you who carry the vessels of the LORD.",
      "M": "Leave! Leave! Come out from there! Touch nothing unclean. Come out from among them; purify yourselves, you who carry the vessels of the LORD.",
      "T": "Go! Leave that place!\nTouch nothing unclean!\nCome out from among them —\npurify yourselves, you who carry the holy vessels of Yahweh."
    },
    "12": {
      "L": "For you shall not go out in haste, and you shall not go in flight; for the LORD will go before you, and the God of Israel will be your rear guard.",
      "M": "But you will not leave in a hurry or flee in panic, for the LORD will go before you, and the God of Israel will guard your rear.",
      "T": "But you will not flee this time.\nNo desperate scramble out the back.\nFor Yahweh goes ahead of you —\nand the God of Israel guards your rear."
    },
    "13": {
      "L": "Behold, my servant shall act wisely; he shall be exalted and lifted up and shall be very high.",
      "M": "See, my servant will act wisely; he will be raised and lifted up and highly exalted.",
      "T": "Watch — my Servant will understand what he is doing.\nHe will be lifted up, raised high,\nexalted above all."
    },
    "14": {
      "L": "As many were astonished at you — his appearance was so marred, more than any man, and his form beyond that of the sons of men —",
      "M": "Just as many were appalled at him — his appearance was disfigured beyond that of any person, his form marred beyond human likeness —",
      "T": "Just as many were horrified when they saw him —\nhis face so disfigured it no longer looked human,\nhis form altered beyond all recognition —"
    },
    "15": {
      "L": "so shall he sprinkle many nations; kings shall shut their mouths because of him; for what had not been told them they see, and what they had not heard they understand.",
      "M": "so he will sprinkle many nations; kings will be struck silent because of him; for they will see what they were never told, and understand what they had never heard.",
      "T": "— so he will astonish and consecrate many nations.\nKings will be struck silent at the sight.\nFor they will see what no one told them.\nThey will grasp what no one ever announced."
    }
  },
  "53": {
    "1": {
      "L": "Who has believed what they heard from us? And to whom has the arm of the LORD been revealed?",
      "M": "Who has believed what we proclaimed? To whom has the arm of the LORD been revealed?",
      "T": "Who actually believed what we told them?\nWho saw the LORD's power revealed in this?"
    },
    "2": {
      "L": "For he grew up before him like a tender plant, and like a root out of dry ground; he had no form nor beauty that we should look at him, and no appearance that we should desire him.",
      "M": "He grew up before the LORD like a tender shoot, like a root from dry soil. There was nothing attractive in his appearance that would make us look at him, nothing beautiful that would make us desire him.",
      "T": "Before the LORD's eyes he grew up\nlike a sapling pushing through cracked desert ground —\nnothing impressive about his appearance,\nnothing that would make us want to look at him,\nnothing beautiful that would draw our desire."
    },
    "3": {
      "L": "He was despised and rejected by men, a man of sorrows and acquainted with grief; and as one from whom men hide their faces he was despised, and we esteemed him not.",
      "M": "He was despised and rejected by people — a man who knew suffering, familiar with grief. Like one from whom people hide their faces, he was despised, and we did not value him.",
      "T": "He was despised — pushed away by everyone.\nA man who knew what pain was,\nwell acquainted with grief.\nWe turned our faces from him as if ashamed.\nHe was despised, and we paid him no regard."
    },
    "4": {
      "L": "Surely he has borne our griefs and carried our sorrows; yet we esteemed him stricken, smitten by God, and afflicted.",
      "M": "Yet he was the one who took up our sicknesses and carried our pain. We, however, assumed he was being struck down and afflicted by God.",
      "T": "And yet — he was the one who carried what was ours:\nour sicknesses, our pain.\nWe assumed he was being punished by God,\nstruck down, suffering for his own wrongs."
    },
    "5": {
      "L": "But he was pierced for our transgressions; he was crushed for our iniquities; the chastisement of our peace was upon him, and by his stripes we are healed.",
      "M": "But he was pierced because of our transgressions; he was crushed because of our iniquities. The punishment that brings us peace fell on him, and by his wounds we are healed.",
      "T": "But he was pierced through for our rebellions —\ncrushed for the guilt we had accumulated.\nThe discipline that makes us whole fell on him.\nBy his wounds, we are healed."
    },
    "6": {
      "L": "All we like sheep have gone astray; we have turned every one to his own way, and the LORD has laid on him the iniquity of us all.",
      "M": "We all went astray like sheep; each of us turned to his own way. And the LORD laid on him the iniquity of us all.",
      "T": "We all wandered off like sheep —\nevery one of us turning down our own path.\nAnd Yahweh placed on him\nthe guilt of all of us."
    },
    "7": {
      "L": "He was oppressed and he was afflicted, yet he opened not his mouth; like a lamb that is led to slaughter, and like a sheep that before its shearers is silent, so he opened not his mouth.",
      "M": "He was oppressed and afflicted, yet he never opened his mouth. Like a lamb being led to slaughter, like a sheep silent before its shearers, he did not open his mouth.",
      "T": "He was pressed under oppression and affliction,\nyet he never opened his mouth.\nLike a lamb being led to the slaughter —\nlike a sheep that goes silent before the shearers —\nhe did not open his mouth."
    },
    "8": {
      "L": "By oppression and judgment he was taken away; and as for his generation, who considered that he was cut off from the land of the living, stricken for the transgression of my people?",
      "M": "By a perversion of justice he was taken away. Who gave any thought to his fate — that he was cut off from the land of the living, struck down for the transgression of my people?",
      "T": "Through a corrupt trial he was swept away.\nWho paused to consider what it meant —\nthat he was cut off from among the living,\nstruck down for the sins of my people?"
    },
    "9": {
      "L": "And they made his grave with the wicked and with a rich man in his death, although he had done no violence, and there was no deceit in his mouth.",
      "M": "He was assigned a grave among the wicked, yet his burial was with the rich — though he had done no violence, and there was no deceit in his mouth.",
      "T": "He was assigned a grave among the wicked —\nyet his burial was with the rich.\nNot because of any violence he had done;\nnot a word of deceit had ever crossed his lips."
    },
    "10": {
      "L": "Yet it was the will of the LORD to crush him; he has put him to grief. When his soul is made a guilt offering, he shall see his offspring; he shall prolong his days; the will of the LORD shall prosper in his hand.",
      "M": "Yet it was the LORD's will to crush him and make him suffer. When his life is given as a guilt offering, he will see his offspring and prolong his days, and the LORD's will shall succeed through him.",
      "T": "Yet Yahweh's purpose was to crush him, to make him suffer.\nWhen his life is offered as the atoning sacrifice,\nhe will see his descendants — he will live long —\nand Yahweh's purpose will be accomplished through him."
    },
    "11": {
      "L": "Out of the anguish of his soul he shall see and be satisfied; by his knowledge shall the righteous one, my servant, justify many, and he shall bear their iniquities.",
      "M": "Out of the anguish of his life he will see and be satisfied. By his knowledge my righteous servant will make many righteous, and he will bear their iniquities.",
      "T": "When the anguish of his life is past,\nhe will see what it accomplished — and be satisfied.\nBy what he knows, my servant, the righteous one,\nwill make many righteous —\nfor he will carry their guilt."
    },
    "12": {
      "L": "Therefore I will divide him a portion with the many, and he shall divide the spoil with the strong, because he poured out his soul to death and was numbered with the transgressors; yet he bore the sin of many, and makes intercession for the transgressors.",
      "M": "Therefore I will give him a portion among the great, and he will share the plunder with the strong — because he poured out his life unto death, and was counted with the transgressors; for he bore the sin of many, and makes intercession for the transgressors.",
      "T": "Therefore I will give him his share among the mighty\nand let him divide the plunder with the strong —\nbecause he poured out his life in death,\nbecause he was counted among the rebels,\nbecause he carried the sin of many,\nand still speaks up for those who rebel."
    }
  },
  "54": {
    "1": {
      "L": "Sing, O barren one, who did not bear; break forth into singing and cry aloud, you who have not been in labor! For the children of the desolate one shall be more than the children of her who has a husband, says the LORD.",
      "M": "Sing for joy, barren woman who has never given birth! Break into singing, cry out with joy — you who have never been in labor! For the children of the desolate woman will outnumber the children of the married woman, says the LORD.",
      "T": "Sing, barren woman — you who never gave birth!\nBreak into joyful singing, cry out loud —\nyou who never knew labor's pain!\nFor the desolate woman will have more children\nthan the woman who has a husband —\ndeclares Yahweh."
    },
    "2": {
      "L": "Enlarge the place of your tent, and let the curtains of your habitations be stretched out; do not hold back; lengthen your cords and strengthen your stakes.",
      "M": "Enlarge the space of your tent and stretch out the curtains of your dwelling; do not hold back — lengthen your ropes and drive your tent pegs deeper.",
      "T": "Make room — stretch your tent wider.\nLet the canopy of your home spread out.\nDon't hold back.\nLengthen the ropes, drive the pegs deeper —\nyou are going to need the space."
    },
    "3": {
      "L": "For you will spread out to the right and to the left, and your offspring will possess the nations and will settle the desolate cities.",
      "M": "For you will spread out to the right and to the left; your descendants will reclaim nations and resettle the ruined cities.",
      "T": "For you will expand — right and left, in every direction.\nYour children will claim nations as their own\nand repopulate cities long abandoned."
    },
    "4": {
      "L": "Fear not, for you will not be ashamed; be not confounded, for you will not be disgraced; for you will forget the shame of your youth, and the reproach of your widowhood you will remember no more.",
      "M": "Do not be afraid; you will not be put to shame. Do not be confounded; you will not be humiliated. For you will forget the disgrace of your youth, and the reproach of your widowhood you will no longer remember.",
      "T": "Do not be afraid — you will not be humiliated.\nDo not cringe — you will not be disgraced.\nYou will forget the shame of your younger years;\nthe reproach of your widowhood will be forgotten."
    },
    "5": {
      "L": "For your Maker is your husband — the LORD of hosts is his name — and the Holy One of Israel is your Redeemer; the God of the whole earth he shall be called.",
      "M": "For your Maker is your husband — the LORD of hosts is his name — and your Redeemer is the Holy One of Israel; he is called the God of the whole earth.",
      "T": "For the one who made you is your husband —\nYahweh of armies is his name —\nand your Kinsman-Redeemer is the Holy One of Israel,\nthe God of the whole earth — that is who he is."
    },
    "6": {
      "L": "For the LORD has called you like a wife forsaken and grieved in spirit, like a wife of youth when she is cast off, says your God.",
      "M": "For the LORD has called you back like a wife who was abandoned and heartbroken — like a wife taken in youth and then rejected, says your God.",
      "T": "For Yahweh has called you back —\nlike a wife who was abandoned and heartbroken,\nlike a wife taken in the years of youth and then sent away.\nYour God says this."
    },
    "7": {
      "L": "For a brief moment I forsook you, but with great compassion I will gather you.",
      "M": "For a brief moment I abandoned you, but with great compassion I will bring you back.",
      "T": "For one brief, terrible moment I left you.\nBut with overflowing compassion I am bringing you home."
    },
    "8": {
      "L": "In a surge of anger I hid my face from you for a moment, but with everlasting steadfast love I will have compassion on you, says the LORD, your Redeemer.",
      "M": "In a surge of anger I hid my face from you for a moment, but with everlasting covenant love I will have compassion on you, says the LORD, your Redeemer.",
      "T": "In a surge of anger I turned my face away —\njust for a moment.\nBut with love that will never run out,\nI will have compassion on you —\ndeclares Yahweh, your Redeemer."
    },
    "9": {
      "L": "This is like the days of Noah to me: as I swore that the waters of Noah should no more go over the earth, so I have sworn that I will not be angry with you and will not rebuke you.",
      "M": "To me this is like the days of Noah: just as I swore that the waters of Noah would never again cover the earth, so now I swear I will never again be angry with you or rebuke you.",
      "T": "To me, this is the same oath I made in Noah's day:\nI swore then that the floodwaters would never again\ncover the earth.\nNow I swear:\nI will never be angry with you again.\nI will never rebuke you again."
    },
    "10": {
      "L": "For the mountains shall depart, and the hills shall be removed; but my steadfast love shall not depart from you, and my covenant of peace shall not be removed, says the LORD, who has compassion on you.",
      "M": "Though the mountains should move and the hills be shaken, my covenant love will not move from you, and my covenant of peace will not be shaken, says the LORD, who has compassion on you.",
      "T": "Mountains may crumble.\nHills may fall.\nBut my covenant loyalty will not leave you.\nMy covenant of peace will not be shaken.\nThis is what Yahweh says —\nthe one who has compassion on you."
    },
    "11": {
      "L": "O afflicted one, storm-tossed and not comforted, behold, I will set your stones in antimony, and lay your foundations with sapphires.",
      "M": "O afflicted city, tossed by storms and without comfort — look: I will set your stones in brilliant color and lay your foundations with sapphires.",
      "T": "O city battered and storm-driven, without comfort —\nlisten:\nI will embed your stones in brilliant color;\nI will lay your foundations with sapphires."
    },
    "12": {
      "L": "I will make your pinnacles of rubies, your gates of sparkling gems, and all your boundary wall of precious stones.",
      "M": "I will make your towers of rubies, your gates of sparkling jewels, and all your walls of precious stones.",
      "T": "Your towers will be set with rubies.\nYour gates will be crystal.\nEvery wall around you — precious stones."
    },
    "13": {
      "L": "All your children shall be taught by the LORD, and great shall be the peace of your children.",
      "M": "All your children will be taught by the LORD, and great will be their peace.",
      "T": "Every one of your children will be taught by Yahweh himself —\nand their peace will be profound."
    },
    "14": {
      "L": "In righteousness you shall be established; you shall be far from oppression, for you shall not fear; and from terror, for it shall not come near you.",
      "M": "You will be established in righteousness; you will be far from oppression and will not fear; terror will not come near you.",
      "T": "Righteousness will be your foundation.\nOppression will be far from you — nothing to fear.\nTerror will not come near you."
    },
    "15": {
      "L": "If anyone stirs up strife, it is not from me; whoever stirs up strife with you shall fall because of you.",
      "M": "If anyone attacks you, it is not my doing; whoever assembles against you will fall before you.",
      "T": "If anyone comes to attack you, it will not be because of me.\nWhoever assembles against you will fall before you."
    },
    "16": {
      "L": "Behold, I have created the smith who blows the fire of coals and produces a weapon for its purpose. I have also created the ravager to destroy.",
      "M": "See — I am the one who created the blacksmith who fans the coals and forges a weapon fit for its purpose. And I am the one who created the destroyer to cause ruin.",
      "T": "I am the one who made the blacksmith\nwho fans the coals and forges the weapon.\nAnd I am the one who made the destroyer who lays waste.\nEven the weapons arrayed against you come from my workshop."
    },
    "17": {
      "L": "No weapon that is fashioned against you shall succeed, and every tongue that rises against you in judgment you shall refute. This is the heritage of the servants of the LORD, and their righteousness is from me, declares the LORD.",
      "M": "No weapon formed against you will succeed, and every tongue that accuses you in court you will refute. This is the inheritance of the LORD's servants, and their vindication comes from me, declares the LORD.",
      "T": "No weapon forged against you will succeed.\nEvery voice raised against you in court — you will answer it.\nThis is the inheritance of Yahweh's servants:\ntheir righteousness comes from me.\n— declares Yahweh."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'isaiah')
        merge_tier(existing, ISAIAH, tier_key)
        save(tier_dir, 'isaiah', existing)
    print('Isaiah 52–54 written.')

if __name__ == '__main__':
    main()
