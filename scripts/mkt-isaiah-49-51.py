"""
MKT Isaiah chapters 49–51 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-isaiah-49-51.py

Translation decisions:
- H3068 (יהוה): "LORD" (L/M) / "Yahweh" (T) — carried forward from all prior Isaiah scripts.
- H430 (אֱלֹהִים): "God" throughout all tiers — consistent with prior Isaiah scripts.
- H136/H3069 (אֲדֹנָי יהוה): "Lord GOD" (L/M) / "Lord Yahweh" (T) — the doubled divine address
  in ch. 50; L/M follows the traditional two-word rendering; T uses "Lord Yahweh" to keep the
  personal name audible.
- H5650 (עֶבֶד): "servant" throughout — the Servant Songs make this the defining term;
  consistent with all prior Isaiah scripts.
- H1350 (גָּאַל): "Redeemer" / "redeemed" — covenantal kinsman-redeemer; carried forward.
- H6299 (פָּדָה): 51:11 "ransomed" — the ransom/purchase word, distinct from גָּאַל.
- H6664 (צְדָקָה / צֶדֶק): "righteousness" (L/M) / "righteous purpose" or "vindication" (T)
  — in 51:4-8 צֶדֶק parallels salvation repeatedly (51:5, 6, 8); the sense shades from
  "justice" to Yahweh's saving uprightness; T uses "vindication" in those parallel lines to
  surface the covenantal-lawsuit register (Yahweh's case for his people has been proven right).
- H1285 (בְּרִית): 49:8 "covenant" throughout — the formal, oath-bound relationship; L/M/T agree.
- H5315 (נֶפֶשׁ): 49:7 — not "soul" (immaterial) but the living person/self; rendered "man" (L)
  / "man" (M) / "person" (T) in context.
- H6588 (פֶּשַׁע): "transgressions" (L/M) / "rebellions" (T) — willful covenant violation;
  carried forward from mkt-isaiah-43-44.py.
- H5771 (עָוֹן): 50:1 "iniquities" (L/M) / "guilt" (T) — accumulated moral debt; carried forward.
- H2534 (חֵמָה): "wrath" (L/M) / "fury" (T) — in 51:17, 20, 22 the cup-of-wrath imagery is
  central; T uses "fury" to convey the intensity of divine judgment being poured out.
- H7294 (רַהַב): 51:9 "Rahab" — the chaos sea-dragon of ancient Near Eastern mythology,
  equated with Egypt in the Exodus tradition (cf. Ps 87:4; 89:10; Job 9:13); left untranslated
  as a proper name in all tiers with T adding a brief gloss in phrasing.
- H8577 (תַּנִּין): 51:9 "dragon" / "sea-serpent" — the primordial chaos monster; L uses
  "dragon," M uses "sea-serpent," T uses "the dragon of the deep" to connect the cosmic register.
- H216 (אוֹר): 49:6 "light" throughout — the Servant as "light to the nations" is a key missional
  term; consistent with prior Isaiah scripts.
- H6726 (צִיּוֹן): "Zion" as a proper name throughout — the ideal Jerusalem standing for the
  covenant community.
- H3444 (יְשׁוּעָה): "salvation" (L/M) / "rescue" or "deliverance" in T when used in contexts
  of concrete liberation (49:6, 8; 51:5-6, 8); "salvation" in more comprehensive contexts.
- Servant Song tension (49:3-6): The Servant is named "Israel" in v.3 but has a mission to Israel
  in vv.5-6. This tension is real in the Hebrew; L/M preserve it without resolution; T surface-
  reads the same ambiguity. The servant figure simultaneously embodies and is sent to the nation.
- 49:24 — "lawful captive" (H6662): the Hebrew is obscure; some MSS read "tyrant" (עָרִיץ) as
  in v.25; rendered "prisoner of the powerful" (L) / "captives of a tyrant" (M) following the
  parallel with v.25.
- Poetry/prose: Ch. 49 is prophetic poetry throughout; ch. 50 is poetry; ch. 51 is poetry.
  T uses line breaks throughout. L/M are continuous prose sentences.
- 50:4-9 is the Third Servant Song. The "tongue of the taught" (limmudim) denotes a disciple
  formed by regular morning encounter with the master. The suffering of vv.6-9 is accepted, not
  escaped — the Servant does not flinch. T brings this out explicitly.
- 51:9-11 — the "awake, awake" addressed to the arm of the LORD is a reversal: elsewhere Yahweh
  calls Israel to awake (51:17); here the prophet calls on Yahweh's power to act. This
  jarring reversal is intentional and T emphasizes it.
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
  "49": {
    "1": {
      "L": "Listen to me, O coastlands, and pay attention, O peoples from afar. The LORD called me from the womb; from the body of my mother he made mention of my name.",
      "M": "Listen to me, you coastlands; pay attention, you peoples from far away. The LORD called me before I was born; before my mother gave birth, he named me.",
      "T": "Listen to me, all you distant shores.\nPay attention, peoples from the ends of the earth.\nBefore I was born, Yahweh called me.\nBefore I left my mother's womb, he spoke my name."
    },
    "2": {
      "L": "He made my mouth like a sharp sword; in the shadow of his hand he hid me. He made me a polished arrow; in his quiver he hid me away.",
      "M": "He made my mouth like a sharp sword; in the shadow of his hand he concealed me. He made me into a polished arrow; in his quiver he hid me away.",
      "T": "He shaped my mouth into a sharp sword\nand hid me in the shadow of his hand.\nHe made me a polished arrow\nand kept me hidden in his quiver."
    },
    "3": {
      "L": "And he said to me, 'You are my servant, Israel, in whom I will be glorified.'",
      "M": "He said to me, 'You are my servant, Israel — in you I will display my glory.'",
      "T": "He said to me:\n'You are my servant —\nIsrael, the one through whom I will show my glory.'"
    },
    "4": {
      "L": "But I said, 'I have labored in vain; I have spent my strength for nothing and vanity; yet surely my vindication is with the LORD and my recompense with my God.'",
      "M": "But I said, 'I have labored for nothing; I have spent my strength for emptiness and futility. Yet my cause is with the LORD, and my reward is with my God.'",
      "T": "But I said: I have worn myself out for nothing.\nI have exhausted my strength on emptiness and chaos.\nAnd yet — my vindication rests with Yahweh.\nMy reward is in my God's hands."
    },
    "5": {
      "L": "And now says the LORD, who formed me from the womb to be his servant, to bring Jacob back to him; and that Israel might be gathered to him — for I am honored in the eyes of the LORD, and my God has become my strength —",
      "M": "And now the LORD says — he who formed me in the womb to be his servant, to bring Jacob back to him, so that Israel would be gathered to him (for I am honored in the LORD's eyes, and my God has been my strength) —",
      "T": "And now Yahweh speaks —\nhe who shaped me in the womb to be his servant,\nto bring Jacob back to him,\nto gather Israel to him.\nFor I am honored in Yahweh's eyes.\nMy God has become my strength."
    },
    "6": {
      "L": "he says: 'It is too light a thing that you should be my servant to raise up the tribes of Jacob and to restore the preserved of Israel; I will make you as a light for the nations, so that my salvation may reach to the end of the earth.'",
      "M": "he says: 'It is too small a thing for you to be my servant to restore the tribes of Jacob and bring back the survivors of Israel; I will also make you a light for the nations, so that my salvation may reach to the ends of the earth.'",
      "T": "He says:\n'It is not enough for you to restore the tribes of Jacob\nand bring back those of Israel I preserved.\nI will make you a light for all the nations —\nso that my salvation reaches to the very ends of the earth.'"
    },
    "7": {
      "L": "Thus says the LORD, the Redeemer of Israel and his Holy One, to one deeply despised, abhorred by the nation, the servant of rulers: 'Kings shall see and rise up; princes, and they shall bow down, because of the LORD who is faithful, the Holy One of Israel, who has chosen you.'",
      "M": "This is what the LORD says — the Redeemer and Holy One of Israel — to the one who is despised and rejected by the nation, the servant of rulers: 'Kings will see and stand up; princes, and they will bow down, because of the LORD, who is faithful, the Holy One of Israel, who has chosen you.'",
      "T": "Here is what Yahweh says —\nRedeemer of Israel, the Holy One:\nTo the one who is despised by everyone,\nabhorred by the nation,\nthe servant under rulers' authority —\n'Kings will see you and stand to their feet.\nPrinces will bow to the ground.\nBecause Yahweh — the faithful one,\nIsrael's Holy One — has chosen you.'"
    },
    "8": {
      "L": "Thus says the LORD: 'In a time of favor I have answered you; in a day of salvation I have helped you; I will keep you and give you as a covenant for the people, to establish the land, to apportion the desolate heritages,'",
      "M": "This is what the LORD says: 'In the time of my favor I answered you; in the day of salvation I helped you. I will keep you and appoint you as a covenant for the people, to restore the land, and to redistribute the ruined inheritances,'",
      "T": "Here is what Yahweh says:\n'When the moment of favor arrived, I answered you.\nOn the day of deliverance, I came to your aid.\nI will watch over you.\nI will make you a covenant for the peoples —\nto resettle the land,\nto give back the desolate inheritances,'"
    },
    "9": {
      "L": "saying to the prisoners, 'Come out,' to those who are in darkness, 'Appear.' They shall feed along the ways; on all bare heights their pasture shall be.",
      "M": "saying to the prisoners, 'Come out,' and to those in darkness, 'Show yourselves.' They will graze along the roads; their pasture will be on all the bare heights.",
      "T": "'to say to the prisoners: Come out!\nto say to those in darkness: Step into the light!\nThey will find pasture along every road;\nthe bare hilltops will become their grazing ground.'"
    },
    "10": {
      "L": "They shall not hunger or thirst, neither scorching heat nor sun shall strike them; for he who has compassion on them will lead them, and by springs of water will guide them.",
      "M": "They will not hunger or thirst; neither the scorching heat nor the sun will beat down on them. For he who has compassion on them will lead them and guide them beside springs of water.",
      "T": "They will never hunger.\nThey will never thirst.\nThe scorching wind and the blazing sun will not touch them —\nfor he who loves them will lead them\nand guide them to flowing springs."
    },
    "11": {
      "L": "And I will make all my mountains into a road, and my highways shall be raised up.",
      "M": "I will turn all my mountains into roads, and my highways will be built up.",
      "T": "I will level my mountains into roads.\nEvery path will be raised and made ready."
    },
    "12": {
      "L": "Behold, these shall come from far away, and behold, some from the north and from the west, and others from the land of Sinim.",
      "M": "See, some will come from far away — from the north, from the west, from the land of Sinim.",
      "T": "Look — they are coming from far away.\nSome from the north, some from the west,\nothers from the distant land of Sinim."
    },
    "13": {
      "L": "Sing for joy, O heavens, and exult, O earth; break forth, O mountains, into singing! For the LORD has comforted his people and will have compassion on his afflicted ones.",
      "M": "Shout for joy, you heavens; rejoice, you earth! Break into song, you mountains! For the LORD has comforted his people and will have compassion on his afflicted.",
      "T": "Sing for joy, heavens!\nRejoice, earth!\nBreak into song, mountains!\nFor Yahweh has comforted his people —\nhe will have mercy on those who suffer."
    },
    "14": {
      "L": "But Zion said, 'The LORD has forsaken me; my Lord has forgotten me.'",
      "M": "But Zion said, 'The LORD has abandoned me; my Lord has forgotten me.'",
      "T": "But Zion said:\n'Yahweh has abandoned me.\nMy Lord has forgotten me.'"
    },
    "15": {
      "L": "Can a woman forget her nursing child, that she should have no compassion on the son of her womb? Even these may forget, yet I will not forget you.",
      "M": "Can a mother forget the baby at her breast and have no compassion on the child she has borne? Though she may forget, I will not forget you!",
      "T": "Can a mother forget the infant at her breast —\nfeel no love for the child she bore?\nEven if she could forget —\nI will never forget you."
    },
    "16": {
      "L": "Behold, I have engraved you on the palms of my hands; your walls are continually before me.",
      "M": "See, I have inscribed you on the palms of my hands; your walls are always before me.",
      "T": "Look — I have carved your name into my palms.\nYour walls are always before my eyes."
    },
    "17": {
      "L": "Your builders hurry; those who laid you waste and those who destroyed you go out from you.",
      "M": "Your builders are coming quickly; those who devastated and destroyed you will depart.",
      "T": "Your rebuilders are rushing toward you.\nThose who tore you apart and left you in ruins — they will be gone."
    },
    "18": {
      "L": "Lift up your eyes and look around; they all gather and come to you. As I live, declares the LORD, you shall put them all on like an ornament and bind them on as a bride does.",
      "M": "Lift up your eyes and look around you — they all gather and come to you. As surely as I live, declares the LORD, you will wear them all as ornaments; you will put them on like a bride's jewels.",
      "T": "Lift your eyes. Look around.\nThey are gathering — coming to you from every direction.\nAs I live, declares Yahweh —\nyou will wear them all like a bride's jewels,\nyou will bind them on and they will adorn you."
    },
    "19": {
      "L": "For your waste places and your desolate places and your devastated land — surely now you will be too crowded for your inhabitants, and those who devoured you will be far away.",
      "M": "Though your land was ruined and desolate and devastated, it will now be too small for all your people, and those who swallowed you up will be long gone.",
      "T": "Your ruined places, your empty land, your devastated ground —\nthey will be overcrowded with people.\nThose who consumed you will be driven away, far from you."
    },
    "20": {
      "L": "The children born in the time of your bereavement will yet say in your ears: 'The place is too narrow for me; make room for me to settle here.'",
      "M": "The children born during your time of loss will yet say in your hearing: 'This place is too small for us — make room for us to live here.'",
      "T": "The children you thought you would never have\nwill say in your very hearing:\n'This place is too small for us.\nMake room — we need more space to live.'"
    },
    "21": {
      "L": "Then you will say in your heart, 'Who bore these for me, since I was bereaved and barren, exiled and put away? But who brought up these? Behold, I was left alone — from where have these come?'",
      "M": "Then you will say in your heart, 'Who bore these children for me? I was bereaved and barren; I was exiled and cast away. Who brought these up? I was left all alone — where did these children come from?'",
      "T": "Then you will say to yourself:\nWho gave me all these children?\nI was bereaved. Barren. Exiled. Cast away.\nWho raised them up?\nI was left completely alone —\nwhere did all these people come from?"
    },
    "22": {
      "L": "Thus says the Lord GOD: Behold, I will lift up my hand to the nations and raise my signal to the peoples; and they shall bring your sons in their arms, and your daughters shall be carried on their shoulders.",
      "M": "This is what the Lord GOD says: 'I will beckon to the nations, I will raise my signal banner for the peoples; they will bring your sons in their arms, and your daughters will be carried on their shoulders.'",
      "T": "Here is what Lord Yahweh says:\n'I will raise my hand toward the nations.\nI will hoist my signal banner for the peoples to see.\nThey will bring your sons in their arms.\nThey will carry your daughters on their shoulders.'"
    },
    "23": {
      "L": "Kings shall be your foster fathers, and their queens your nursing mothers; with their faces to the ground they shall bow down to you and lick the dust of your feet. Then you shall know that I am the LORD; those who wait for me shall not be put to shame.",
      "M": "Kings will serve as your guardians, and their queens as your nursing mothers; they will bow down before you with their faces to the ground and lick the dust at your feet. Then you will know that I am the LORD; those who hope in me will not be put to shame.",
      "T": "Kings will serve as your guardians.\nQueens will nurse you back to strength.\nThey will bow before you — faces in the dust —\nthey will lick the ground at your feet.\nThen you will know: I am Yahweh.\nNo one who waits for me will be put to shame."
    },
    "24": {
      "L": "Can the prey be taken from the mighty, or the captives of a tyrant be rescued?",
      "M": "Can plunder be taken from a warrior, or the captive of a tyrant be set free?",
      "T": "Can anyone snatch what a warrior has seized?\nCan a tyrant's prisoner ever go free?"
    },
    "25": {
      "L": "For thus says the LORD: 'Even the captives of the mighty shall be taken away, and the prey of the tyrant shall be rescued; for I will contend with those who contend with you, and I will save your children.'",
      "M": "But this is what the LORD says: 'Yes — the warrior's captives will be taken away, and the tyrant's prey will be freed. I will fight against those who fight against you, and I will rescue your children.'",
      "T": "But here is what Yahweh says:\nYes — even what the warrior seizes will be taken back.\nEven the tyrant's prisoners will go free.\nFor I will fight whoever fights against you.\nI will rescue your children."
    },
    "26": {
      "L": "I will make your oppressors eat their own flesh, and they shall be drunk with their own blood as with sweet wine. Then all flesh shall know that I am the LORD your Savior and your Redeemer, the Mighty One of Jacob.",
      "M": "I will make your oppressors eat their own flesh, and they will be drunk with their own blood as if with wine. Then all humanity will know that I am the LORD, your Savior and Redeemer, the Mighty One of Jacob.",
      "T": "I will turn your oppressors against each other —\nthey will devour their own flesh\nand be drunk on their own blood as though on wine.\nThen everyone alive will know:\nI am Yahweh — your Savior,\nyour Redeemer,\nthe Mighty One of Jacob."
    }
  },
  "50": {
    "1": {
      "L": "Thus says the LORD: 'Where is your mother's certificate of divorce, with which I put her away? Or which of my creditors is it to whom I have sold you? Behold, for your iniquities you were sold, and for your transgressions your mother was sent away.'",
      "M": "This is what the LORD says: 'Where is the certificate of divorce by which I dismissed your mother? To which creditor did I sell you? Look — it was because of your iniquities that you were sold, and because of your transgressions that your mother was sent away.'",
      "T": "Here is what Yahweh says:\n'Where is the divorce certificate\nby which I sent your mother away?\nTo what creditor did I sell you?\nLook honestly:\nYou were sold because of your own guilt.\nYour mother was sent away because of your rebellions.'"
    },
    "2": {
      "L": "Why, when I came, was there no one? When I called, was there no one to answer? Is my hand shortened at all, that it cannot redeem? Or have I no power to deliver? Behold, by my rebuke I dry up the sea; I make the rivers a desert; their fish stink for lack of water and die of thirst.",
      "M": "Why was there no one when I came? Why did no one answer when I called? Is my hand too short to redeem? Do I lack the power to rescue? By my rebuke I dry up the sea; I turn rivers into a desert. Their fish rot for lack of water and die of thirst.",
      "T": "Why was there no one when I came?\nWhy did no one answer when I called?\nIs my arm too short to save you?\nDo I not have the power to deliver?\nI rebuke the sea and it dries up.\nI turn rivers into desert.\nThe fish rot in the waterless riverbed —\nthey die of thirst."
    },
    "3": {
      "L": "I clothe the heavens with blackness and make sackcloth their covering.",
      "M": "I clothe the heavens with darkness and make sackcloth their covering.",
      "T": "I dress the sky in blackness\nand make sackcloth the covering of the heavens."
    },
    "4": {
      "L": "The Lord GOD has given me the tongue of those who are taught, that I may know how to sustain with a word him who is weary. Morning by morning he awakens; he awakens my ear to hear as those who are taught.",
      "M": "The Lord GOD has given me a well-instructed tongue, so that I know how to encourage the weary with the right word. He awakens me morning by morning; he awakens my ear to listen like one who is being taught.",
      "T": "Lord Yahweh has given me the tongue of a disciple —\nso I know how to speak a sustaining word to the exhausted.\nMorning by morning he wakes me.\nHe opens my ear\nthe way a master opens his student's ear —\nto truly hear."
    },
    "5": {
      "L": "The Lord GOD has opened my ear, and I was not rebellious; I turned not backward.",
      "M": "The Lord GOD has opened my ear, and I have not been rebellious; I have not drawn back.",
      "T": "Lord Yahweh opened my ear.\nI did not resist.\nI did not pull away."
    },
    "6": {
      "L": "I gave my back to those who strike, and my cheeks to those who pull out the beard; I hid not my face from disgrace and spitting.",
      "M": "I offered my back to those who struck me, my cheeks to those who pulled out my beard; I did not hide my face from mockery and spitting.",
      "T": "I offered my back to those who beat me.\nI gave my cheeks to those who tore out my beard.\nI did not turn my face away from shame and spitting."
    },
    "7": {
      "L": "But the Lord GOD helps me; therefore I have not been disgraced; therefore I have set my face like a flint, and I know that I shall not be put to shame.",
      "M": "But the Lord GOD helps me; therefore I have not been put to shame. For that reason I set my face like a hard stone, and I know I will not be put to shame.",
      "T": "But Lord Yahweh is helping me.\nThat is why I have not been disgraced.\nThat is why I set my face like a flint —\nhard, unmovable.\nI know I will not be put to shame."
    },
    "8": {
      "L": "He who vindicates me is near. Who will contend with me? Let us stand up together. Who is my adversary? Let him come near to me.",
      "M": "He who declares me righteous is near. Who then will bring a charge against me? Let us face each other. Who is my accuser? Let him step forward.",
      "T": "The one who will vindicate me is close at hand.\nWho is going to bring a charge against me?\nLet us face each other.\nWho is my adversary?\nLet him come forward."
    },
    "9": {
      "L": "Behold, the Lord GOD helps me; who is he who will condemn me? Behold, all of them will wear out like a garment; the moth will eat them up.",
      "M": "Look — the Lord GOD helps me; who will condemn me? They will all wear out like a garment; moths will devour them.",
      "T": "Look — Lord Yahweh is my helper.\nWho can condemn me?\nAll my opponents will wear out like an old coat.\nThe moth will eat them up."
    },
    "10": {
      "L": "Who among you fears the LORD and obeys the voice of his servant? Let him who walks in darkness and has no light trust in the name of the LORD and rely on his God.",
      "M": "Who among you fears the LORD and heeds the voice of his servant? Whoever walks in darkness and has no light — let them trust in the name of the LORD and depend on their God.",
      "T": "Who among you fears Yahweh\nand truly listens to the voice of his servant?\nIf you walk in deep darkness\nand have no light at all —\ntrust in the name of Yahweh.\nLean on your God."
    },
    "11": {
      "L": "Behold, all you who kindle a fire, who equip yourselves with burning torches! Walk by the light of your fire and by the torches you have kindled! This you shall have from my hand: you shall lie down in torment.",
      "M": "But all of you who light your own fires and provide yourselves with flaming torches — go, walk in the light of your own fire, by the torches you have lit. This is what you will receive from my hand: you will lie down in a place of suffering.",
      "T": "But all of you who strike your own fire —\nwho light your own torches to see by —\ngo ahead: walk by the light you made for yourselves.\nThis is what you will get from my hand:\nyou will lie down in agony."
    }
  },
  "51": {
    "1": {
      "L": "Listen to me, you who pursue righteousness, you who seek the LORD: look to the rock from which you were hewn, and to the quarry from which you were dug.",
      "M": "Listen to me, you who pursue righteousness and seek the LORD: Look to the rock from which you were cut, to the quarry from which you were hewn.",
      "T": "Listen to me —\nyou who run after righteousness,\nyou who seek Yahweh:\nLook at the rock from which you were cut.\nLook at the quarry from which you were dug."
    },
    "2": {
      "L": "Look to Abraham your father and to Sarah who bore you; for when he was but one I called him, that I might bless him and multiply him.",
      "M": "Look to Abraham your father and to Sarah who gave birth to you. When I called him, he was only one person, but I blessed him and made him many.",
      "T": "Look to your father Abraham.\nLook to Sarah who bore you.\nHe was only one man when I called him —\nbut I blessed him\nand he became many."
    },
    "3": {
      "L": "For the LORD will comfort Zion; he will comfort all her waste places and will make her wilderness like Eden, and her desert like the garden of the LORD; joy and gladness shall be found in her, thanksgiving and the voice of melody.",
      "M": "For the LORD will comfort Zion; he will comfort all her ruined places and make her wilderness like Eden, her wasteland like the garden of the LORD. Joy and gladness will be found there, thanksgiving and the sound of singing.",
      "T": "For Yahweh will comfort Zion —\nhe will comfort every place that lies in ruins.\nHe will make her wilderness like Eden,\nher desert like the garden of Yahweh.\nJoy and gladness will live there.\nThanksgiving. The sound of singing."
    },
    "4": {
      "L": "Pay attention to me, my people, and give ear to me, my nation; for a law will go out from me, and I will set my justice for a light to the peoples.",
      "M": "Pay attention to me, my people; listen to me, my nation! A law will go out from me, and I will establish my justice as a light for the nations.",
      "T": "Listen to me, my people.\nGive me your attention, my nation.\nMy instruction will go out from me.\nMy justice will become a light for all peoples."
    },
    "5": {
      "L": "My righteousness is near; my salvation has gone out; and my arms will judge the peoples; the coastlands wait for me, and for my arm they hope.",
      "M": "My righteousness is near; my salvation has gone out; my arms will bring justice to the peoples. The coastlands wait for me; they put their hope in my power.",
      "T": "My vindication is close.\nMy deliverance has gone out.\nMy arm will bring justice to the nations.\nThe distant shores are waiting for me.\nThey are hoping in my strength."
    },
    "6": {
      "L": "Lift up your eyes to the heavens, and look at the earth beneath; for the heavens shall vanish like smoke, the earth shall wear out like a garment, and those who dwell in it shall die in like manner; but my salvation shall be forever, and my righteousness shall not be abolished.",
      "M": "Lift up your eyes to the sky and look down at the earth beneath: the sky will vanish like smoke, the earth will wear out like a garment, and those who live on it will die like gnats. But my salvation will endure forever, and my righteousness will never fail.",
      "T": "Lift your eyes to the heavens.\nLook down at the earth.\nThe heavens will dissolve like smoke.\nThe earth will wear thin like an old coat.\nEveryone on it will die the same way.\nBut my salvation will stand forever.\nMy vindication will never be undone."
    },
    "7": {
      "L": "Listen to me, you who know righteousness, the people in whose heart is my law; fear not the reproach of men, nor be dismayed at their revilings.",
      "M": "Listen to me, you who know what is right, you people who have my instruction in your hearts: do not fear human contempt; do not be terrified by their insults.",
      "T": "Listen to me —\nyou who know what is right,\nyou people who carry my instruction in your hearts.\nDo not be afraid of human contempt.\nDo not be shattered by their mockery."
    },
    "8": {
      "L": "For the moth will eat them up like a garment, and the worm will eat them like wool; but my righteousness shall be forever, and my salvation to all generations.",
      "M": "For the moth will devour them like a garment; the worm will eat them like wool. But my righteousness will endure forever, and my salvation through all generations.",
      "T": "The moth will consume them like a worn-out coat.\nThe worm will eat them like wool.\nBut my vindication will stand forever.\nMy salvation — through every generation."
    },
    "9": {
      "L": "Awake, awake, put on strength, O arm of the LORD; awake, as in days of old, the generations of long ago. Was it not you who cut Rahab in pieces, who pierced the dragon?",
      "M": "Wake up, wake up, arm of the LORD! Clothe yourself with strength! Wake up as you did in the ancient days, the generations long ago. Was it not you who hacked Rahab to pieces and pierced the dragon?",
      "T": "Awake! Awake!\nArm of Yahweh — put on your strength!\nWake up as you did in the days long past,\nin the generations of old.\nWas it not you who split Rahab apart\nand ran through the dragon of the deep?"
    },
    "10": {
      "L": "Was it not you who dried up the sea, the waters of the great deep, who made the depths of the sea a road for the redeemed to cross over?",
      "M": "Was it not you who dried up the sea, the waters of the great deep, who made the ocean depths into a road for the redeemed to walk on?",
      "T": "Was it not you who dried up the sea —\nthe waters of the vast deep —\nwho turned the ocean floor into a road\nfor the redeemed to walk across?"
    },
    "11": {
      "L": "And the ransomed of the LORD shall return and come to Zion with singing; everlasting joy shall be upon their heads; they shall obtain gladness and joy, and sorrow and sighing shall flee away.",
      "M": "The ransomed of the LORD will return; they will come to Zion with singing, crowned with everlasting joy. Gladness and joy will overtake them, and sorrow and sighing will flee away.",
      "T": "The ransomed of Yahweh will come home.\nThey will arrive in Zion singing,\neverlasting joy crowning their heads.\nGladness and joy will surround them.\nSorrow and grief will run away."
    },
    "12": {
      "L": "I, I am he who comforts you; who are you that you fear man who dies, of the son of man who is made like grass,",
      "M": "I — I myself — am the one who comforts you. Who are you to fear a mere mortal, a human being who will die like grass,",
      "T": "I — I am the one who comforts you.\nSo who are you to be afraid of a man who will die,\nof a human being made like grass?"
    },
    "13": {
      "L": "and have forgotten the LORD, your Maker, who stretched out the heavens and laid the foundations of the earth, and you fear continually all the day because of the wrath of the oppressor when he sets himself to destroy? And where is the wrath of the oppressor?",
      "M": "while you forget the LORD your Maker, who stretched out the heavens and laid the earth's foundations — and you live in constant dread every day because of the oppressor's rage when he is poised to destroy? Where now is the oppressor's fury?",
      "T": "You have forgotten Yahweh your Maker —\nthe one who stretched out the heavens\nand laid the foundations of the earth.\nYou cower all day long in the face of the oppressor's rage,\nas though he is about to destroy you.\nBut where is that fury now?"
    },
    "14": {
      "L": "The captive exile shall quickly be released; he shall not die and go down to the pit, and his bread shall not fail.",
      "M": "The cowering prisoner will soon be set free; he will not die in a dungeon, and his food will not run out.",
      "T": "The bent-down prisoner will soon be freed.\nHe will not die in a pit.\nHis bread will not fail."
    },
    "15": {
      "L": "For I am the LORD your God who stirs up the sea so that its waves roar — the LORD of hosts is his name.",
      "M": "For I am the LORD your God, who churns up the sea so that its waves roar — the LORD of hosts is his name.",
      "T": "For I am Yahweh your God —\nthe one who stirs the sea until its waves crash and thunder.\nYahweh of armies — that is my name."
    },
    "16": {
      "L": "And I have put my words in your mouth and covered you in the shadow of my hand, establishing the heavens and laying the foundations of the earth, and saying to Zion, 'You are my people.'",
      "M": "I have put my words in your mouth and covered you with the shadow of my hand — I who set the heavens in place and laid the foundations of the earth, who say to Zion, 'You are my people.'",
      "T": "I have placed my words in your mouth.\nI have hidden you in the shadow of my hand —\nI, who stretched out the heavens,\nwho laid the foundations of the earth,\nwho say to Zion:\n'You are my people.'"
    },
    "17": {
      "L": "Wake yourself, wake yourself, stand up, O Jerusalem, you who have drunk from the hand of the LORD the cup of his wrath; you who have drunk to the dregs the bowl, the cup of staggering.",
      "M": "Rouse yourself, rouse yourself! Stand up, Jerusalem! You who drank from the LORD's hand the cup of his wrath — you who drained to the dregs the goblet, the cup that makes you stagger.",
      "T": "Wake up! Wake up!\nGet to your feet, Jerusalem!\nYou have drunk from Yahweh's hand\nthe cup of his fury —\nyou have drained the cup of staggering\ndown to the very last drop."
    },
    "18": {
      "L": "There is none to guide her among all the sons she has borne; there is none to take her by the hand among all the sons she has brought up.",
      "M": "Of all the children she bore, there is none to lead her; of all the children she raised, there is no one to take her by the hand.",
      "T": "Of all the children she bore, none steps forward to guide her.\nOf all the children she raised, none takes her by the hand."
    },
    "19": {
      "L": "These two things have happened to you — who will grieve with you? — devastation and destruction, famine and sword; who will comfort you?",
      "M": "Two calamities have come upon you — who will mourn with you? — devastation and ruin, famine and sword. Who is there to comfort you?",
      "T": "Two disasters have overtaken you.\nWho will mourn with you?\nDevastation and ruin. Famine and the sword.\nWho is left to bring you comfort?"
    },
    "20": {
      "L": "Your sons have fainted; they lie at the head of every street like an antelope in a net; they are full of the wrath of the LORD, the rebuke of your God.",
      "M": "Your sons have collapsed; they lie at the corner of every street like an antelope caught in a net. They are filled with the LORD's wrath, the rebuke of your God.",
      "T": "Your sons have collapsed.\nThey lie sprawled at every street corner\nlike a deer caught in a net.\nThey are saturated with Yahweh's fury —\nthe full weight of your God's rebuke."
    },
    "21": {
      "L": "Therefore hear this, you who are afflicted, who are drunk, but not with wine:",
      "M": "Therefore hear this, you who are suffering, who are drunk, but not from wine:",
      "T": "So listen to this —\nyou who are crushed,\ndrunk with grief and not with wine:"
    },
    "22": {
      "L": "Thus says your Lord, the LORD, your God who pleads the cause of his people: 'Behold, I have taken from your hand the cup of staggering; the bowl of my wrath you shall drink no more;'",
      "M": "This is what your Lord says — the LORD, your God, who defends his people: 'Look — I am taking from your hand the cup that makes you stagger; the goblet of my wrath you will not drink again.'",
      "T": "Here is what your Lord says —\nYahweh your God,\nthe one who fights for his people:\n'Look — I am taking that staggering cup from your hand.\nYou will never drink from the bowl of my fury again.'"
    },
    "23": {
      "L": "and I will put it into the hand of your tormentors, who have said to you, 'Bow down, that we may pass over'; and you have made your back like the ground and like the street for them to walk over.",
      "M": "I will put it in the hand of those who tormented you, who said to you, 'Lie down, so we can walk over you' — and you made your back like the ground, like the street for them to trample.",
      "T": "'I will give it instead to those who tormented you —\nthose who told you: Get down, so we can walk over you.\nYou made your back into pavement,\nyou lay flat like a street for them to march across.\nThat is finished.'"
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'isaiah')
        merge_tier(existing, ISAIAH, tier_key)
        save(tier_dir, 'isaiah', existing)
    print('Isaiah 49–51 written.')

if __name__ == '__main__':
    main()
