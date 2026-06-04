"""
MKT Ezekiel chapters 28–30 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-ezekiel-28-30.py

=== CHAPTER OVERVIEW ===
Ch 28: Two oracles against Tyre (Prince/King) + oracle against Sidon + Israel restoration promise.
  vv. 1–10: Oracle against the Prince (נָשִׂיא) of Tyre — pride claims divinity ("I am a god").
  vv. 11–19: Lament (qinah) over the King (מֶלֶךְ) of Tyre — the Eden/cherub passage. The king
    is described in terms that invoke Eden (v.13), the anointed guardian cherub (v.14), perfection
    until iniquity (v.15), cast from the mountain of God (vv.16–17). Primary referent is the
    historical king; the Adamic/angelic resonance is preserved in T tier without over-reading.
  vv. 20–26: Oracle against Sidon; closing promise of Israel's restoration and safety in the land.
Ch 29: Oracle against Egypt/Pharaoh as the great dragon (תַּנִּין) of the Nile.
  vv. 1–16: Pharaoh the dragon dragged out and left for carrion; 40-year desolation; reduced to
    a lowly kingdom no longer tempting Israel.
  vv. 17–21: The latest-dated oracle in Ezekiel (27th year). Nebuchadnezzar given Egypt as
    payment for the unpaid labor of the Tyre siege. Ezekiel's prophetic mouth reopened.
Ch 30: The Day of the LORD against Egypt and her allies.
  vv. 1–19: The day of cloud — sword, plague, and fire through the length of Egypt and her
    allied nations; catalogue of Egyptian cities destroyed.
  vv. 20–26: Pharaoh's arm broken and left unbound; Babylon's arms strengthened; the sword
    of Yahweh given to Nebuchadnezzar.

=== CONTESTED-TERM DECISIONS ===

- H3068 (יהוה): "LORD" in L/M throughout. "Yahweh" in T — especially in the recognition
  formula ("they shall know that I am Yahweh"), oracle-opening formulas, and direct speech.
  Consistent with all prior Ezekiel scripts.

- H136 + H3069 (אֲדֹנָי יְהוִה / Lord GOD): "Lord GOD" in L/M (small-caps GOD convention).
  "Lord Yahweh" in T. The combined form introduces oracle sections throughout Ezekiel.

- H410 (אֵל / god/deity): In 28:2 and 28:9 the Prince of Tyre claims "אֵל אָנִי" — "I am
  a god." This is rendered "I am a God" in L (preserving the capitalized traditional rendering),
  "I am a god" in M (indefinite, making clear this is a claim, not a title), "I am a god" in T
  (same — the indefinite signals the false claim). The contrast with "וְאַתָּה אָדָם וְלֹא-אֵל"
  (you are adam, not El) is preserved in all three tiers.

- H8577 (תַּנִּין / dragon/sea creature): In 29:3 Pharaoh is "הַתַּנִּים הַגָּדוֹל" — the great
  sea creature/dragon. L: "great dragon" (traditional KJV); M: "great sea creature" (accurate
  to ancient Near Eastern chaos imagery — probably a Nile crocodile but evoking the mythic
  sea dragon); T: "great dragon" — the chaos-sea imagery is worth evoking in T, as it activates
  the OT background of Yahweh defeating the sea dragon (Isa 51:9, Ps 74:13).

- H3742 (כְּרוּב / cherub): In 28:14, 16 the King of Tyre is identified as "כְּרוּב מִמְשַׁח
  הַסּוֹכֵךְ" — the anointed guardian cherub. "Cherub" in L/M; "guardian cherub" in T where
  the full function is worth expressing.

- H4473 (מִמְשַׁח / anointed): "Anointed" in all three tiers — the term marks the King of
  Tyre as specially appointed, with royal/priestly overtones.

- H7307 (רוּחַ): Not a major contested term in these chapters.

- H5315 (נֶפֶשׁ): Not prominent in these chapters.

- Recognition formula "וְיָדְעוּ כִּי-אֲנִי יְהוָה": Standard Ezekiel signature. L: "they shall
  know that I am the LORD"; M: "they will know that I am the LORD"; T: "they will know that
  I am Yahweh." This formula drives ch. 28–30 as a theological refrain.

- H7161 (קֶרֶן / horn): In 29:21 "אַצְמִיחַ קֶרֶן לְבֵית יִשְׂרָאֵל" — "I will cause the horn
  of Israel to sprout." "Horn" in L/M (traditional); "strength" or "the horn of power" in T —
  the horn is the symbol of military strength/royal power (Ps 132:17).

- H6936 (קָדְקֹד) / shoulder imagery in 29:18: The soldiers had their heads made bald
  (מֻקְרָח) and shoulders rubbed raw (מְרוּטָה) from the prolonged siege labor. L preserves
  the literalism. M and T bring out the image of exhausted, worn-down soldiers.

=== ASPECT / TENSE NOTES ===

- Oracle against Prince of Tyre (28:1–10): Present/perfect for the prince's established
  sin ("thou hast said," "thou hast gotten"); future for divine judgment ("I will bring").
- Eden lament (28:11–19): Past for the original state of glory ("thou wast," "thou hast been");
  perfect for the fall ("iniquity was found," "thou hast sinned"); past perfect for the expulsion
  ("I cast thee out"). T uses present-tense narration to heighten immediacy.
- Egypt oracles (29–30): First-person divine speech in imperfect = future certainty. Retained
  as future in all tiers.
- 40-year desolation (29:11): Hebrew "לֹא תֵשֵׁב" = imperfect, "it shall not be inhabited."
  Rendered as future certainty.

=== OT INTERTEXTUALITY ===

- 28:2 — The prince's claim "I am a god" (אֵל אָנִי) echoes the original temptation: "you
  will be like God" (Gen 3:5). T surfaces this.
- 28:13 — "Thou hast been in Eden the garden of God" — the Eden resonance is explicit. The
  king of Tyre is compared to the original human in the garden; his fall echoes Adam's.
- 28:14 — "Stones of fire" (אַבְנֵי-אֵשׁ) and "mountain of God" — imagery from the divine
  throne-room and the theophany of Ezekiel 1. The cherub walks where the divine fire burns.
- 29:3 — Pharaoh as תַּנִּין echoes the Exodus dragon imagery (Ex 7:9–12, where Aaron's rod
  becomes a תַּנִּין) and the creation battle against the sea monster (Ps 74:13, Isa 51:9).
  T notes this.
- 30:3 — "Day of the LORD" (יוֹם יְהוָה) echoes Amos 5:18, Joel 2:1–2, Zephaniah 1. The
  "day of cloud" formula is drawn from theophany language.
- 29:21 — "Horn will sprout for Israel" anticipates messianic horn imagery (Ps 132:17,
  Luke 1:69). T notes the forward trajectory.
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
  "28": {
    "1": {
      "L": "And the word of the LORD came unto me, saying:",
      "M": "The word of the LORD came to me:",
      "T": "Yahweh's word came to me:"
    },
    "2": {
      "L": "Son of man, say unto the prince of Tyre: Thus saith the Lord GOD: Because thine heart is lifted up, and thou hast said, I am a God, I sit in the seat of God, in the midst of the seas; yet thou art a man, and not God, though thou dost set thine heart as the heart of God.",
      "M": "Son of man, say to the prince of Tyre: Thus says the Lord GOD: Because your heart is proud and you have said, 'I am a god; I sit in the seat of gods in the heart of the seas' — yet you are a man and not a god, though you set your heart as the heart of a god.",
      "T": "Son of man, deliver this to the prince of Tyre: The Lord Yahweh says: Your heart has risen up in pride, and you have said, 'I am a god — I sit on the divine throne in the midst of the seas.' But you are a man, adam, flesh and breath — not god. You have set your heart to think like a god, but you are not one. The original temptation ('you will be like God') has been fully embraced, and it ends the same way."
    },
    "3": {
      "L": "Behold, thou art wiser than Daniel; there is no secret that is hidden from thee:",
      "M": "Behold, you are wiser than Daniel — no secret is hidden from you.",
      "T": "You count yourself wiser than Daniel — the legendary wise man — with no mystery beyond your reach. The very claim is the indictment."
    },
    "4": {
      "L": "With thy wisdom and with thine understanding thou hast gotten thee riches, and hast gotten gold and silver into thy treasuries:",
      "M": "By your wisdom and understanding you have gained wealth for yourself and accumulated gold and silver in your treasuries.",
      "T": "Your wisdom and commercial skill built an empire of wealth. Gold and silver fill your vaults. Every transaction went in your favor."
    },
    "5": {
      "L": "By thy great wisdom and by thy traffic hast thou increased thy riches, and thine heart is lifted up because of thy riches.",
      "M": "By your great wisdom and in your trading you have increased your wealth, and your heart has become proud because of your wealth.",
      "T": "Your trading brought greater and greater wealth, and as the wealth grew your pride grew with it — fed by success, inflated by the very wisdom that built your fortune. The gift became the corrupting agent."
    },
    "6": {
      "L": "Therefore thus saith the Lord GOD: Because thou hast set thine heart as the heart of God,",
      "M": "Therefore thus says the Lord GOD: Because you have set your heart as the heart of a god,",
      "T": "Therefore the Lord Yahweh says: Because you have placed your heart where God's heart belongs —"
    },
    "7": {
      "L": "Behold, therefore I will bring strangers upon thee, the terrible of the nations; and they shall draw their swords against the beauty of thy wisdom, and they shall defile thy brightness.",
      "M": "Behold, I will bring strangers against you, the most ruthless of the nations; they will draw their swords against the beauty of your wisdom and defile your splendor.",
      "T": "I will bring them — the most terrifying nations on earth, ruthless conquerors. They will unsheathe their swords against everything you are most proud of: the beauty and brilliance you have made your identity. They will desecrate your glory."
    },
    "8": {
      "L": "They shall bring thee down to the pit, and thou shalt die the deaths of them that are slain in the midst of the seas.",
      "M": "They will thrust you down into the Pit, and you will die the death of the slain in the heart of the seas.",
      "T": "They will thrust you down into the Pit — into the grave, into the deep. You will die the violent death of the battle-slain, there in the middle of the seas that you claimed as your throne."
    },
    "9": {
      "L": "Wilt thou yet say before him that slayeth thee, I am a God? But thou shalt be a man, and no God, in the hand of him that slayeth thee.",
      "M": "Will you still say, 'I am a god,' before the one who kills you? But you will be a mere man in the hand of the one who wounds you, not a god.",
      "T": "Will you still claim to be a god when the blade is at your throat? Before the one who kills you, the claim will mean nothing. You will be what you always were: a man, adam, mortal flesh — held fast in the hand of the one who strikes you down."
    },
    "10": {
      "L": "Thou shalt die the deaths of the uncircumcised by the hand of strangers: for I have spoken it, saith the Lord GOD.",
      "M": "You will die the death of the uncircumcised by the hand of foreigners, for I have spoken, declares the Lord GOD.",
      "T": "You will die the death of the uncircumcised — the death of those outside covenant, without honor, without protection, at the hand of foreign conquerors. I, the Lord Yahweh, have declared it."
    },
    "11": {
      "L": "Moreover the word of the LORD came unto me, saying:",
      "M": "The word of the LORD came to me:",
      "T": "Yahweh's word came to me again:"
    },
    "12": {
      "L": "Son of man, take up a lamentation upon the king of Tyre, and say unto him: Thus saith the Lord GOD: Thou sealest up the sum, full of wisdom, and perfect in beauty.",
      "M": "Son of man, raise a lamentation over the king of Tyre and say to him: Thus says the Lord GOD: You were the seal of perfection, full of wisdom and perfect in beauty.",
      "T": "Son of man, raise a lament over the king of Tyre. Say from the Lord Yahweh: You were the very seal of perfection — wisdom complete in you, beauty without flaw. This is the lament: not for what you have become, but for what you were."
    },
    "13": {
      "L": "Thou hast been in Eden the garden of God; every precious stone was thy covering: the sardius, topaz, and the diamond, the beryl, the onyx, and the jasper, the sapphire, the emerald, and the carbuncle, and gold; the workmanship of thy tabrets and of thy pipes was prepared in thee in the day that thou wast created.",
      "M": "You were in Eden, the garden of God; every precious stone adorned you: ruby, topaz, and crystal, beryl, onyx, and jasper, lapis lazuli, turquoise, and emerald, and gold throughout — the craftsmanship of your settings and engravings was prepared in you on the day you were created.",
      "T": "You were in Eden — the garden of God. Every precious stone was your covering: ruby and topaz and crystal, beryl and onyx and jasper, lapis lazuli and turquoise and emerald, and gold throughout. Every detail of your adornment was prepared for you on the day of your creation. You were made for glory. The comparison to Adam is deliberate: here is another creature made perfect, placed in the garden, who fell."
    },
    "14": {
      "L": "Thou art the anointed cherub that covereth; and I have set thee so: thou wast upon the holy mountain of God; thou hast walked up and down in the midst of the stones of fire.",
      "M": "You were the anointed guardian cherub; I had appointed you. You were on the holy mountain of God; you walked among the stones of fire.",
      "T": "You were the anointed guardian cherub — the highest of created beings, set in place by me, appointed to your station. You stood on the holy mountain of God. You walked among the blazing stones of fire in the presence of the Holy One. This is what you were before the fall."
    },
    "15": {
      "L": "Thou wast perfect in thy ways from the day that thou wast created, till iniquity was found in thee.",
      "M": "You were blameless in your ways from the day you were created until iniquity was found in you.",
      "T": "From the day of your creation you were without flaw. The created perfection held — until the day iniquity was found in you. Not placed in you by another. Found — as something that had grown there, hidden, until it could no longer be concealed."
    },
    "16": {
      "L": "By the multitude of thy merchandise they have filled the midst of thee with violence, and thou hast sinned: therefore I will cast thee as profane out of the mountain of God; and I will destroy thee, O covering cherub, from the midst of the stones of fire.",
      "M": "Through the abundance of your trade you were filled inwardly with violence, and you sinned; so I cast you out as profane from the mountain of God, and I destroyed you, O guardian cherub, from the midst of the stones of fire.",
      "T": "Your vast commerce filled you from within with violence. Trade was the corrupting force — the accumulation, the dealings, the relentless expansion — and it opened the door to sin. So I expelled you, cast you out as profane from the mountain of God. The guardian cherub, the being of blazing stones and created glory — driven away, destroyed from that holy place."
    },
    "17": {
      "L": "Thine heart was lifted up because of thy beauty; thou hast corrupted thy wisdom by reason of thy brightness: I will cast thee to the ground, I will lay thee before kings, that they may behold thee.",
      "M": "Your heart was proud because of your beauty; you corrupted your wisdom for the sake of your splendor. I have cast you to the ground and exposed you before kings so they might gaze on you.",
      "T": "Your beauty was your downfall. The very splendor that marked you as unique became the thing you turned inward, doted on, and finally worshipped. And in worshipping your own glory you corrupted the wisdom that had been your gift. So I threw you to the earth — exposed before kings, made a spectacle of shame by the one who made you."
    },
    "18": {
      "L": "Thou hast defiled thy sanctuaries by the multitude of thine iniquities, by the iniquity of thy traffic; therefore will I bring forth a fire from the midst of thee, it shall devour thee, and I will bring thee to ashes upon the earth in the sight of all them that behold thee.",
      "M": "By the abundance of your iniquities and the wrongdoing of your trade you defiled your sanctuaries; therefore I brought out fire from your midst — it consumed you, and I turned you to ashes on the earth in the sight of all who look on you.",
      "T": "The mass of your iniquities — piled up through every corrupt commercial dealing — defiled even your own sacred places. And so the fire that destroys you comes from within you, not from without. I bring it out from your own interior, and it consumes you. You are reduced to ash on the earth, in full view of every watching eye. The glory that was your identity becomes its own funeral pyre."
    },
    "19": {
      "L": "All they that know thee among the people shall be astonished at thee: thou shalt be a terror, and never shalt thou be any more.",
      "M": "All who knew you among the peoples are appalled at you; you have become a horror and shall be no more forever.",
      "T": "Everyone who knew you among the nations stands aghast. You who were the talk of the trading world, the pinnacle of human achievement — you have become a horror to look at. And then nothing. You are gone. Forever."
    },
    "20": {
      "L": "Again the word of the LORD came unto me, saying:",
      "M": "The word of the LORD came to me:",
      "T": "Yahweh's word came to me:"
    },
    "21": {
      "L": "Son of man, set thy face against Zidon, and prophesy against it,",
      "M": "Son of man, set your face against Sidon and prophesy against it.",
      "T": "Son of man, turn your face toward Sidon and prophesy against it —"
    },
    "22": {
      "L": "And say: Thus saith the Lord GOD: Behold, I am against thee, O Zidon; and I will be glorified in the midst of thee: and they shall know that I am the LORD, when I shall have executed judgments in her, and shall be sanctified in her.",
      "M": "Say: Thus says the Lord GOD: Behold, I am against you, Sidon; I will be glorified in your midst. They will know that I am the LORD when I execute judgments in her and display my holiness in her.",
      "T": "Say: The Lord Yahweh says: I am against you, Sidon. Through your judgment I will be glorified — my holiness vindicated in plain sight. When the judgments fall, those watching will know that I am Yahweh."
    },
    "23": {
      "L": "For I will send into her pestilence, and blood into her streets; and the wounded shall be judged in the midst of her by the sword upon her on every side; and they shall know that I am the LORD.",
      "M": "I will send pestilence into her and blood into her streets; the slain will fall in her midst by the sword that comes against her from every side — and they will know that I am the LORD.",
      "T": "I will send plague into her and blood will run in her streets. The sword will fall on her from every direction and the slain will pile up in her center. Through this they will know that I am Yahweh."
    },
    "24": {
      "L": "And there shall be no more a pricking brier unto the house of Israel, nor any grieving thorn of all that are round about them, that despised them; and they shall know that I am the Lord GOD.",
      "M": "There will no longer be a painful brier or a piercing thorn from any of the surrounding peoples who showed contempt for Israel; and they will know that I am the Lord GOD.",
      "T": "When Sidon falls, the house of Israel will no longer have to endure the thorn in its side — that painful, wounding neighbor that showed only contempt. And through it all they will come to know that I am the Lord Yahweh."
    },
    "25": {
      "L": "Thus saith the Lord GOD: When I shall have gathered the house of Israel from the people among whom they are scattered, and shall be sanctified in them in the sight of the heathen, then shall they dwell in their land that I have given to my servant Jacob.",
      "M": "Thus says the Lord GOD: When I gather the house of Israel from the peoples among whom they have been scattered, and display my holiness in them before the eyes of the nations, then they will dwell in their own land that I gave to my servant Jacob.",
      "T": "The Lord Yahweh says: When I gather Israel back from every people among whom they have been scattered — when my holiness is made visible through that gathering before the nations' eyes — then they will dwell in the land I gave to Jacob my servant. The promises to the ancestors are not cancelled. They are deferred, not dead."
    },
    "26": {
      "L": "And they shall dwell safely therein, and shall build houses, and plant vineyards; yea, they shall dwell with confidence, when I have executed judgments upon all those that despise them round about them; and they shall know that I am the LORD their God.",
      "M": "They will dwell in it safely and build houses and plant vineyards. They will live with confidence when I have executed judgments against all their surrounding neighbors who showed them contempt. And they will know that I am the LORD their God.",
      "T": "They will live there in safety. They will build houses. They will plant vineyards. The ordinary, unhurried life of covenant blessing — the life that exile interrupted — will be restored. When I have dealt with every surrounding nation that treated them with contempt, they will settle in peace. And they will know that I am Yahweh their God. Not just Yahweh — their God. The covenantal intimacy, restored."
    }
  },
  "29": {
    "1": {
      "L": "In the tenth year, in the tenth month, in the twelfth day of the month, the word of the LORD came unto me, saying:",
      "M": "In the tenth year, in the tenth month, on the twelfth day of the month, the word of the LORD came to me:",
      "T": "Tenth year, tenth month, twelfth day — Yahweh's word came to me:"
    },
    "2": {
      "L": "Son of man, set thy face against Pharaoh king of Egypt, and prophesy against him and against all Egypt:",
      "M": "Son of man, set your face against Pharaoh king of Egypt and prophesy against him and against all Egypt.",
      "T": "Son of man, turn your face toward Pharaoh king of Egypt — prophesy against him and against all Egypt together."
    },
    "3": {
      "L": "Speak, and say: Thus saith the Lord GOD: Behold, I am against thee, Pharaoh king of Egypt, the great dragon that lieth in the midst of his rivers, which hath said: My river is mine own, and I have made it for myself.",
      "M": "Speak and say: Thus says the Lord GOD: Behold, I am against you, Pharaoh king of Egypt — the great sea creature lying in the midst of your rivers — who has said, 'My Nile is my own; I made it for myself.'",
      "T": "Say from the Lord Yahweh: I am against you, Pharaoh king of Egypt — the great dragon, sprawled in the middle of your Nile, lord of the waters you claim as your own creation. 'My river is mine,' you say. 'I made it.' That claim is the sin. The creator of a river is God alone; Pharaoh has stolen the title."
    },
    "4": {
      "L": "But I will put hooks in thy jaws, and I will cause the fish of thy rivers to stick unto thy scales, and I will bring thee up out of the midst of thy rivers, and all the fish of thy rivers shall stick unto thy scales.",
      "M": "I will put hooks in your jaws and make the fish of your rivers cling to your scales; I will haul you up out of the midst of your rivers with all the fish of your rivers clinging to your scales.",
      "T": "I will drive hooks into your jaws. The fish of your Nile will cling to your scales as I drag you out of the water — you and all the teeming life that depended on you, pulled up together, helpless."
    },
    "5": {
      "L": "And I will leave thee thrown into the wilderness, thee and all the fish of thy rivers: thou shalt fall upon the open fields; thou shalt not be brought together, nor gathered: I have given thee for meat to the beasts of the field and to the fowls of the heaven.",
      "M": "I will throw you into the wilderness, you and all the fish of your rivers; you will fall on the open fields and not be gathered or collected. I have given you as food to the beasts of the field and the birds of the air.",
      "T": "You will be thrown into the wilderness — you and all the life you sustained. Left on the open ground, unburied, uncollected. The birds and the wild animals will eat you. This is the end of the great dragon: food for scavengers, left unburied in the open field."
    },
    "6": {
      "L": "And all the inhabitants of Egypt shall know that I am the LORD, because they have been a staff of reed to the house of Israel.",
      "M": "All the inhabitants of Egypt will know that I am the LORD, because they have been a staff of reed to the house of Israel.",
      "T": "All Egypt will know that I am Yahweh — and the reason is specific: because Egypt was a reed staff to Israel. It looked like support. It was hollow."
    },
    "7": {
      "L": "When they took hold of thee by thy hand, thou didst break, and rend all their shoulder: and when they leaned upon thee, thou brakest, and madest all their loins to be at a stand.",
      "M": "When they grasped you with their hand, you splintered and tore all their shoulder; and when they leaned on you, you broke and made all their limbs give way.",
      "T": "When Israel reached out and grabbed hold of Egypt for support, you shattered in their grip — driving splinters into their shoulder. When they leaned on you, you snapped beneath them and left them sprawling. That is what Egypt is as an ally: a reed that breaks under pressure and wounds the hand that grasps it."
    },
    "8": {
      "L": "Therefore thus saith the Lord GOD: Behold, I will bring a sword upon thee, and cut off man and beast out of thee:",
      "M": "Therefore thus says the Lord GOD: Behold, I will bring a sword against you and will cut off both man and beast from you.",
      "T": "Therefore the Lord Yahweh says: I am bringing a sword against you. Man and animal alike will be cut off from your land."
    },
    "9": {
      "L": "And the land of Egypt shall be desolate and waste; and they shall know that I am the LORD: because he hath said, The river is mine, and I have made it.",
      "M": "The land of Egypt will become a desolation and a waste, and they will know that I am the LORD — because he said, 'The Nile is mine and I made it.'",
      "T": "Egypt's land will become a desolation, a ruin. They will know that I am Yahweh. The reason is the claim: Pharaoh said 'The Nile is mine — I made it.' The creator of a river is answerable only to himself. But the Nile's creator is Yahweh, and Pharaoh is accountable to him."
    },
    "10": {
      "L": "Behold, therefore I am against thee, and against thy rivers, and I will make the land of Egypt utterly waste and desolate, from the tower of Syene even unto the border of Ethiopia.",
      "M": "Behold, I am against you and against your rivers, and I will make the land of Egypt a complete waste and desolation — from Migdol to Syene, as far as the border of Cush.",
      "T": "I am against you — and against your rivers, the very arteries of your civilization. The entire length of Egypt will become waste and desolation: from Migdol in the north to Syene in the south, all the way to the border of Cush. Nothing exempted."
    },
    "11": {
      "L": "No foot of man shall pass through it, nor foot of beast shall pass through it, neither shall it be inhabited forty years.",
      "M": "No human foot will pass through it, no animal's foot will pass through it, and it will not be inhabited for forty years.",
      "T": "For forty years — not a human foot, not an animal's foot, will cross that land. It will sit empty, silent, desolate. Forty years: the measure of a generation's wilderness, the number of complete judgment."
    },
    "12": {
      "L": "And I will make the land of Egypt desolate in the midst of the countries that are desolate, and her cities among the cities that are laid waste shall be desolate forty years: and I will scatter the Egyptians among the nations, and will disperse them through the countries.",
      "M": "I will make the land of Egypt a desolation in the midst of desolated lands, and her cities will be in ruins for forty years among ruined cities. I will scatter the Egyptians among the nations and disperse them through the lands.",
      "T": "Egypt will be one more ruin among ruins — her cities desolate for forty years alongside the other broken cities of the region. And the Egyptians themselves will be scattered: dispersed among the nations, spread across every land. The great empire brought to the same condition as those it had dominated."
    },
    "13": {
      "L": "Yet thus saith the Lord GOD: At the end of forty years will I gather the Egyptians from the people whither they were scattered:",
      "M": "Yet thus says the Lord GOD: At the end of forty years I will gather the Egyptians from the peoples among whom they were scattered,",
      "T": "Yet the Lord Yahweh says: After forty years — after the full measure of judgment has run — I will gather the Egyptians from every nation among which they were scattered."
    },
    "14": {
      "L": "And I will bring again the captivity of Egypt, and will cause them to return into the land of Pathros, into the land of their habitation; and they shall be there a base kingdom.",
      "M": "I will restore the fortunes of Egypt and bring them back to the land of Pathros, the land of their origin. There they will be a lowly kingdom.",
      "T": "I will restore Egypt's fortunes — bring them home to Pathros, the land of their origin. But they will return as a diminished kingdom, lowly among the nations. Restoration, but without the old imperial ambition. This is mercy and limitation together."
    },
    "15": {
      "L": "It shall be the basest of the kingdoms; neither shall it exalt itself any more above the nations: for I will diminish them, that they shall no more rule over the nations.",
      "M": "It will be the humblest of kingdoms and will no longer exalt itself over the nations. I will diminish them so that they will no longer rule over the nations.",
      "T": "Egypt will be the smallest of kingdoms — her days of imperial dominance done. She will not again lift herself over the nations. I have diminished her, permanently, so that she never again lords it over the peoples she once enslaved."
    },
    "16": {
      "L": "And it shall be no more the confidence of the house of Israel, which bringeth their iniquity to remembrance, when they shall look after them: but they shall know that I am the Lord GOD.",
      "M": "Egypt will no longer be a source of confidence for the house of Israel but will bring iniquity to remembrance when they turn to it for help. Then they will know that I am the Lord GOD.",
      "T": "Egypt will no longer serve as Israel's false refuge. Every time Israel looked to Egypt for deliverance, it was a betrayal of Yahweh — a returning toward the house of slavery, an act of unfaithfulness that called the covenant into question. That temptation will be removed. And they will know that I am the Lord Yahweh."
    },
    "17": {
      "L": "And it came to pass in the seven and twentieth year, in the first month, in the first day of the month, the word of the LORD came unto me, saying:",
      "M": "In the twenty-seventh year, in the first month, on the first day of the month, the word of the LORD came to me:",
      "T": "Twenty-seventh year, first month, first day — Yahweh's word came to me. This is the latest date in all of Ezekiel's oracles:"
    },
    "18": {
      "L": "Son of man, Nebuchadrezzar king of Babylon caused his army to serve a great service against Tyrus: every head was made bald, and every shoulder was peeled: yet had he no wages, nor his army, for Tyrus, for the service that he had served against it:",
      "M": "Son of man, Nebuchadnezzar king of Babylon made his army labor strenuously against Tyre; every head went bald and every shoulder was rubbed raw — yet he and his army received no payment from Tyre for the service they performed against it.",
      "T": "Son of man, Nebuchadnezzar king of Babylon drove his army through an exhausting siege against Tyre — every soldier went bald from helmet-wear, every shoulder raw from carrying siege equipment — and in the end he got nothing from Tyre for all that work. The campaign was a labor for which no wages came."
    },
    "19": {
      "L": "Therefore thus saith the Lord GOD: Behold, I will give the land of Egypt unto Nebuchadrezzar king of Babylon; and he shall take her multitude, and take her spoil, and take her prey; and it shall be the wages for his army.",
      "M": "Therefore thus says the Lord GOD: Behold, I am giving the land of Egypt to Nebuchadnezzar king of Babylon; he will carry off its wealth, take its spoil, and seize its plunder — that will be the payment for his army.",
      "T": "Therefore the Lord Yahweh says: I am giving Egypt to Nebuchadnezzar as payment. He will carry off Egypt's multitudes, plunder her wealth, strip her bare — and all of it becomes the wages for the army I used to execute my purposes. History is not a series of random conquests. I am the one who pays the contractors."
    },
    "20": {
      "L": "I have given him the land of Egypt for his labour wherewith he served against it, because they wrought for me, saith the Lord GOD.",
      "M": "I have given him the land of Egypt as his wage for what he did, because he and his army worked for me, declares the Lord GOD.",
      "T": "I gave him Egypt as his wage — the land itself, as compensation for what he accomplished. Because, though he did not know it, he worked for me. The Lord Yahweh says it."
    },
    "21": {
      "L": "In that day will I cause the horn of the house of Israel to bud forth, and I will give thee the opening of the mouth in the midst of them; and they shall know that I am the LORD.",
      "M": "On that day I will cause a horn to sprout for the house of Israel, and I will open your mouth to speak among them; and they will know that I am the LORD.",
      "T": "On that same day, I will cause Israel's strength to spring up — the horn of power that had been cut down will bud again. And to you, Ezekiel, I will give open mouth among them: the word will come, and you will speak it, and they will know that I am Yahweh. The judgment of the nations becomes the signal for Israel's vindication. The horn that sprouts here anticipates the messianic horn (Ps 132:17, Luke 1:69)."
    }
  },
  "30": {
    "1": {
      "L": "The word of the LORD came again unto me, saying:",
      "M": "The word of the LORD came to me:",
      "T": "Yahweh's word came to me:"
    },
    "2": {
      "L": "Son of man, prophesy and say: Thus saith the Lord GOD: Howl ye, Woe worth the day!",
      "M": "Son of man, prophesy and say: Thus says the Lord GOD: Wail — alas for the day!",
      "T": "Son of man, prophesy. Say from the Lord Yahweh: Wail! Cry out! For the day is coming."
    },
    "3": {
      "L": "For the day is near, even the day of the LORD is near, a cloudy day; it shall be the time of the heathen.",
      "M": "For the day is near — the day of the LORD is near — a day of cloud. It will be the time of the nations.",
      "T": "The day is near — the Day of Yahweh is near. A day of cloud and darkness, the theophanic storm inverted into judgment. It will be the hour of reckoning for the nations: when the nations face what Israel has already faced."
    },
    "4": {
      "L": "And the sword shall come upon Egypt, and great pain shall be in Ethiopia, when the slain shall fall in Egypt, and they shall take away her multitude, and her foundations shall be broken down.",
      "M": "The sword will come against Egypt, and anguish will grip Ethiopia when the slain fall in Egypt; her wealth will be carried off and her foundations torn down.",
      "T": "The sword will come against Egypt. When the slain begin to fall there, the shock wave will reach Ethiopia — great anguish, great pain among Egypt's neighbors. Egypt's wealth will be stripped, her foundations demolished."
    },
    "5": {
      "L": "Ethiopia, and Libya, and Lydia, and all the mingled people, and Chub, and the men of the land that is in league, shall fall with them by the sword.",
      "M": "Cush, Put, and Lud, and all the mixed peoples, Cub, and the people of the land that is in league with them — all will fall by the sword.",
      "T": "Cush, Put, Lud, all the foreign auxiliaries, Cub, the mercenaries from allied nations — everyone in alliance with Egypt will fall by the same sword. The alliance offers no protection when the judgment is Yahweh's."
    },
    "6": {
      "L": "Thus saith the LORD: They also that uphold Egypt shall fall; and the pride of her power shall come down: from the tower of Syene shall they fall in it by the sword, saith the Lord GOD.",
      "M": "Thus says the LORD: Those who support Egypt will fall, and her proud strength will collapse. From Migdol to Syene they will fall by the sword within her, declares the Lord GOD.",
      "T": "Yahweh says: Egypt's supporters will fall with her. The proud strength of Egypt — the thing she trusted most — will collapse. From Migdol in the north to Syene in the south, the sword will cut through her. The Lord Yahweh declares it."
    },
    "7": {
      "L": "And they shall be desolate in the midst of the countries that are desolate, and her cities shall be in the midst of the cities that are wasted.",
      "M": "They will be desolate in the midst of desolated lands, and her cities will lie among ruined cities.",
      "T": "Egypt's cities will join the company of ruined cities — desolation in the midst of desolation. Nothing to distinguish Egypt from all the other kingdoms Yahweh has judged."
    },
    "8": {
      "L": "And they shall know that I am the LORD, when I have set a fire in Egypt, and when all her helpers shall be destroyed.",
      "M": "They will know that I am the LORD when I set fire to Egypt and all her helpers are broken.",
      "T": "When the fire falls on Egypt and every nation that helped her is shattered — then they will know that I am Yahweh. The recognition comes through destruction."
    },
    "9": {
      "L": "In that day shall messengers go forth from me in ships to make the careless Ethiopians afraid, and great pain shall come upon them, as in the day of Egypt: for, lo, it cometh.",
      "M": "In that day messengers will go out from me by ship to terrify the complacent Cush, and anguish will come over them on the day of Egypt's fall — for, behold, it is coming.",
      "T": "On that day, messengers will go out by sea from before me — sent to alarm the Ethiopians who are living in false security. Great anguish will overtake them when they see what happened to Egypt. Because what is coming is coming. It cannot be stopped."
    },
    "10": {
      "L": "Thus saith the Lord GOD: I will also make the multitude of Egypt to cease by the hand of Nebuchadrezzar king of Babylon.",
      "M": "Thus says the Lord GOD: I will put an end to the multitude of Egypt by the hand of Nebuchadnezzar king of Babylon.",
      "T": "The Lord Yahweh says: I will bring Egypt's teeming masses to a halt — through the hand of Nebuchadnezzar king of Babylon. He is my instrument."
    },
    "11": {
      "L": "He and his people with him, the terrible of the nations, shall be brought to destroy the land: and they shall draw their swords against Egypt, and fill the land with the slain.",
      "M": "He and his people with him — the most ruthless of nations — will be brought to destroy the land. They will unsheathe their swords against Egypt and fill the land with the slain.",
      "T": "He comes — Nebuchadnezzar — with his forces, the most feared soldiers in the world. Brought specifically to destroy this land. Their swords will be drawn against Egypt and the land will be filled with the slain. This is what I am bringing."
    },
    "12": {
      "L": "And I will make the rivers dry, and sell the land into the hand of the wicked: and I will make the land waste, and all that is therein, by the hand of strangers: I the LORD have spoken it.",
      "M": "I will make the Nile channels run dry and sell the land into the hand of evil men; I will lay waste the land and everything in it by the hand of foreigners. I the LORD have spoken.",
      "T": "I will dry up the Nile — the source of Egypt's life, her agriculture, her civilization. And I will sell the land — give it over to foreigners to lay waste, every field and city in it. I, Yahweh, have spoken. That is sufficient."
    },
    "13": {
      "L": "Thus saith the Lord GOD: I will also destroy the idols, and I will cause their images to cease out of Noph; and there shall be no more a prince of the land of Egypt: and I will put a fear in the land of Egypt.",
      "M": "Thus says the Lord GOD: I will destroy the idols and put an end to the images in Memphis; there will no longer be a prince in the land of Egypt, and I will spread dread throughout the land of Egypt.",
      "T": "The Lord Yahweh says: I will destroy Egypt's idols — the whole apparatus of her religion will be torn down. The cult images of Memphis will be made to cease. There will no longer be a native ruler in Egypt — their monarchy ended. And through it all I will spread dread throughout the land. Egypt will fear, but too late."
    },
    "14": {
      "L": "And I will make Pathros desolate, and will set fire in Zoan, and will execute judgments in No.",
      "M": "I will make Pathros a desolation and set fire to Zoan and execute judgments on Thebes.",
      "T": "Pathros will be made desolate. Fire will fall on Zoan. Judgment will be executed against Thebes — the great city, the seat of Amun, the most sacred city in Egypt."
    },
    "15": {
      "L": "And I will pour my fury upon Sin, the strength of Egypt; and I will cut off the multitude of No.",
      "M": "I will pour out my wrath on Pelusium, the stronghold of Egypt, and cut off the multitude of Thebes.",
      "T": "I will pour my fury on Pelusium — the fortress that guards Egypt's northeastern approach — and cut down the teeming population of Thebes. No stronghold is strong enough against my wrath."
    },
    "16": {
      "L": "And I will set fire in Egypt: Sin shall have great pain, and No shall be rent asunder, and Noph shall have distresses daily.",
      "M": "I will set fire throughout Egypt: Pelusium will writhe in anguish, Thebes will be breached, and Memphis will face daily distress.",
      "T": "Fire throughout Egypt. Pelusium will writhe. Thebes will be broken open. Memphis will face assault day after day, without relief. The great cities of Egypt reduced to agony."
    },
    "17": {
      "L": "The young men of Aven and of Pibeseth shall fall by the sword: and these cities shall go into captivity.",
      "M": "The young men of On and Bubastis will fall by the sword, and these cities will go into exile.",
      "T": "The young men of Heliopolis and Bubastis will fall by the sword — the men of military age, the defense of those cities, cut down. The cities themselves will go into captivity."
    },
    "18": {
      "L": "At Tehaphnehes also the day shall be darkened, when I shall break there the yokes of Egypt: and the pomp of her strength shall cease in her: as for her, a cloud shall cover her, and her daughters shall go into captivity.",
      "M": "At Tahpanhes the day will grow dark when I break the yokes of Egypt there; her proud strength will come to an end. A cloud will cover her, and her daughters will go into captivity.",
      "T": "At Tahpanhes, the day itself will go dark — when I break the yokes of Egypt right there. Egypt's proud strength will stop, cut off. A cloud will cover her — but not the cloud of divine presence and glory; this cloud is the darkness of judgment. Her outlying towns and villages will go into captivity."
    },
    "19": {
      "L": "Thus will I execute judgments in Egypt: and they shall know that I am the LORD.",
      "M": "Thus I will execute judgments in Egypt, and they will know that I am the LORD.",
      "T": "This is how I will execute my judgments against Egypt. And through every blow, they will come to know that I am Yahweh."
    },
    "20": {
      "L": "And it came to pass in the eleventh year, in the first month, in the seventh day of the month, that the word of the LORD came unto me, saying:",
      "M": "In the eleventh year, in the first month, on the seventh day of the month, the word of the LORD came to me:",
      "T": "Eleventh year, first month, seventh day — Yahweh's word came to me:"
    },
    "21": {
      "L": "Son of man, I have broken the arm of Pharaoh king of Egypt; and, lo, it shall not be bound up to be healed, to put a roller to bind it, to make it strong to hold the sword.",
      "M": "Son of man, I have broken the arm of Pharaoh king of Egypt, and it has not been bound up to heal it — no bandage applied, no splint wrapped around it to make it strong enough to hold a sword.",
      "T": "Son of man, I have broken Pharaoh's arm — his military power, his capacity to wage war. And no one has bandaged it, no healer has set it and wrapped it tight so it could grip a sword again. The wound has been left open, the military capacity permanently compromised."
    },
    "22": {
      "L": "Therefore thus saith the Lord GOD: Behold, I am against Pharaoh king of Egypt, and will break his arms, the strong, and that which was broken; and I will cause the sword to fall out of his hand.",
      "M": "Therefore thus says the Lord GOD: Behold, I am against Pharaoh king of Egypt — I will break his arms, both the strong one and the already broken one, and I will make the sword fall from his hand.",
      "T": "Therefore the Lord Yahweh says: I am against Pharaoh king of Egypt. I will break both arms — the one that was already broken and the one that is still strong. I will make the sword drop from his hand. He will be defenseless."
    },
    "23": {
      "L": "And I will scatter the Egyptians among the nations, and will disperse them through the countries.",
      "M": "I will scatter the Egyptians among the nations and disperse them through the lands.",
      "T": "I will scatter the Egyptians — break their national coherence and spread them among every nation, dispersed through every land."
    },
    "24": {
      "L": "And I will strengthen the arms of the king of Babylon, and put my sword in his hand: but I will break Pharaoh's arms, and he shall groan before him with the groanings of a deadly wounded man.",
      "M": "I will strengthen the arms of the king of Babylon and put my sword in his hand; but I will break Pharaoh's arms, and he will groan before him with the groaning of a mortally wounded man.",
      "T": "I will strengthen Babylon's arms — put my own sword in Nebuchadnezzar's hand. And as I do, Pharaoh's arms will break, and he will groan the way a fatally wounded man groans: helpless, spent, watching his power drain away before his enemy."
    },
    "25": {
      "L": "But I will strengthen the arms of the king of Babylon, and the arms of Pharaoh shall fall down; and they shall know that I am the LORD, when I shall put my sword into the hand of the king of Babylon, and he shall stretch it out upon the land of Egypt.",
      "M": "I will strengthen the arms of the king of Babylon, but Pharaoh's arms will fall; and they will know that I am the LORD when I put my sword in the hand of the king of Babylon and he extends it over the land of Egypt.",
      "T": "I strengthen Babylon's arms; Pharaoh's arms collapse. They will know that I am Yahweh — the moment I put my sword in the king of Babylon's hand and he stretches it out over Egypt. The sword is mine. He is the hand I use."
    },
    "26": {
      "L": "And I will scatter the Egyptians among the nations, and disperse them among the countries; and they shall know that I am the LORD.",
      "M": "I will scatter the Egyptians among the nations and disperse them through the lands; and they will know that I am the LORD.",
      "T": "I will scatter the Egyptians among the nations and spread them through every land. And through this — all of it, every act of judgment, every exile, every broken arm — they will know that I am Yahweh."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'ezekiel')
        merge_tier(existing, EZEKIEL, tier_key)
        save(tier_dir, 'ezekiel', existing)
    print('Ezekiel 28–30 written.')

if __name__ == '__main__':
    main()
