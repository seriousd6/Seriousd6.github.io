"""
MKT Ezekiel chapters 23–24 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-ezekiel-23-24.py

===== TRANSLATION DECISIONS =====

Carrying forward all conventions from mkt-ezekiel-17-18.py:

- H3068 (יהוה): "LORD" in L/M throughout. "Yahweh" in T — especially for oracle
  introductions, recognition formulae ("you shall know that I am the LORD"), and
  narrative turning points. Consistent with all prior Ezekiel scripts.

- H136 + H3069 (אֲדֹנָי יְהוִה / Adonai-Yahweh): "Lord GOD" in L/M (small-caps GOD);
  "Lord Yahweh" in T. Dominates oracle introductions throughout both chapters.

- H170 / H172 (אָהֳלָה / Oholah; אָהֳלִיבָה / Oholibah): Transliterations retained in
  all three tiers. Meanings surfaced in T at 23:4: Oholah = "her tent" (Samaria's
  high places, outside Jerusalem); Oholibah = "my tent is in her" (Jerusalem, where
  God placed his Name). The name distinction is theologically loaded.

- H2181 (זָנָה / play the harlot / commit whoredom): Central verb of ch. 23. L: "played
  the harlot" / "committed whoredoms" (traditional, source-accurate). M: "played the
  harlot" / "prostituted herself." T varies — "gave herself over," "committed herself,"
  surfaces the prophetic shock intended by the explicit language. The graphic imagery is
  deliberate: Ezekiel uses sexual metaphor to convey the horror of covenant infidelity
  in terms the audience cannot sanitize.

- H5689 (עָגַב / dote / be consumed with desire): L: "doted on." M: "was consumed with
  desire for" / "was infatuated with." T: "burned with desire for" / "was obsessed
  with" — develops the pathological quality of idolatrous political attachment.

- H5315 (נֶפֶשׁ / nephesh): In 23:17-18, 22, 28 = the affections/will/desire, not the
  death-related sense. L: "soul" (traditional). M: "heart" or "mind" (context-driven).
  T: "heart" or "deepest desire." In 24:21, 25 = "soul/longing" — the totality of
  Israel's emotional attachment to the temple. L: "soul." M/T: "longing."

- H2154 (זִמָּה / zimmah / lewdness): L: "lewdness." M: "lewdness" / "depravity." T
  develops as "moral depravity," "scandalous conduct," or "utter shamelessness."

- H3563 (כּוֹס / cup): 23:31-34 — the cup of judgment. "Cup" in all three tiers. T
  develops the image of the judgment-cup as something Jerusalem must drain completely.

- H2457 (חֶלְאָה / helah / scum/rust): Ch. 24. The dross/scum that clings to the pot —
  accumulated bloodguilt. "Scum" in L/M/T. No English equivalent captures it fully;
  T notes the image represents guilt that has been baked into the city's very structure.

- H5518 (סִיר / pot/cauldron): Ch. 24 central image. "Pot" in L/M/T. T develops the
  pot as Jerusalem: the city that is set over the fire of Babylonian siege.

- H4261 (מַחְמָד / desire / delight): 23:6, 12, 23 = "desirable men" (attr. of
  Assyrian/Babylonian soldiers). 24:16 = "desire of your eyes" = Ezekiel's wife.
  24:21, 25 = "desire of your eyes" = the temple. L: "desirable" (adj.) / "desire"
  (noun). M same. T develops in the personal contexts: "the one you love most" (wife),
  "the great longing of your heart" (temple).

- H4159 (מוֹפֵת / sign/wonder): 24:24, 27 — Ezekiel as a sign to Israel. "Sign" in all
  three tiers. T notes that the prophet's person — not just his words — becomes the
  prophetic message.

- H1818 (דָּם / blood): Ch. 23:37, 45; 24:7-8 — blood guilt. "Blood" in all tiers.
  T notes the legal significance of uncovered blood in 24:7 (contrast Lev 17:13).

- H2189 (זַוְעָה / terror/horror): 23:46 — "to be removed" (KJV). Actually means "object
  of terror/horror." M/T: "object of terror" / "something the world recoils from."

- Historical note for 24:1-2: The date given (ninth year, tenth month, tenth day) is
  January 15, 588 BC — the exact date Nebuchadnezzar began his siege of Jerusalem.
  Ezekiel receives this in Babylon simultaneously. This is one of the most remarkable
  features of the book: a dated prophetic revelation that was later verified by comparing
  it with Babylonian records. T surfaces this significance.

- Sign-act in 24:15-27: The death of Ezekiel's wife and his commanded restraint of
  grief is one of the most personally costly prophetic sign-acts in the Bible. T treats
  it with appropriate seriousness — the prophet bears his grief silently as a living
  parable of what Israel must bear. The T tier also notes that when the temple falls,
  Ezekiel's "muteness" ends (v. 27) — his freedom to speak again is itself the sign.

- Aspect notes for ch. 23:
  - The narrative of Oholah (vv. 1-10) and Oholibah (vv. 11-21) uses Hebrew perfect
    forms throughout — completed past action. Rendered as simple past in all tiers.
  - The judgment oracles (vv. 22-35, 46-49) shift to imperfect (future) for the
    coming action; retained as future in all tiers.
  - The cup image (vv. 31-34) uses a mix of perfect (prophetic certainty) and imperfect;
    L/M render as future; T uses emphatic present-future to convey certainty.

- Aspect notes for ch. 24:
  - The pot parable (vv. 1-14) uses imperatives (vv. 3-5, 10) and future declarations
    (vv. 6-14); all retained.
  - V. 14 "I the LORD have spoken" = perfect tense of absolute prophetic certainty —
    rendered "have spoken" in L; "I have spoken" in M; T: "I have declared it" with
    emphasis on the irrevocability.
  - The sign-act instructions (vv. 16-17) are imperatives — retained as such.
  - "Your mouth will be opened" (v. 27) = imperfect, future certainty.

- OT intertextuality:
  - 23:3 — Israel's Egypt-rooted unfaithfulness echoes Ezekiel 20:5-9; the prophetic
    diagnosis: the disease began in Egypt itself, before Sinai.
  - 23:38-39 — simultaneous child sacrifice and sanctuary entry echoes the Molech
    worship condemned in Lev 18:21 and 20:2-5; Jeremiah 7:31 (Tophet).
  - 24:7 — "she poured it on bare rock, not on the ground to cover it" echoes Lev
    17:13 (blood of a kill must be covered with dust) and Gen 4:10 (Abel's blood crying
    from the ground). T notes both echoes.
  - 24:16 — "desire of your eyes" echoes the language of intense personal attachment;
    the parallel with the temple (24:21) makes the sign-act operate on two levels at once.
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
  "23": {
    "1": {
      "L": "The word of the LORD came again unto me, saying:",
      "M": "The word of the LORD came to me:",
      "T": "Yahweh's word came to me again:"
    },
    "2": {
      "L": "Son of man, there were two women, daughters of one mother:",
      "M": "Son of man, there were two women, daughters of one mother.",
      "T": "Son of man, consider two women born of the same mother."
    },
    "3": {
      "L": "And they committed whoredoms in Egypt; in their youth they committed whoredoms: there were their breasts pressed, and there they bruised the teats of their virginity.",
      "M": "They played the harlot in Egypt; in their youth they played the harlot. There their breasts were handled and their virgin nipples were pressed.",
      "T": "From their earliest days in Egypt they were unfaithful — they gave themselves over to sexual immorality while still young. In Egypt their bodies were possessed; their youth was the beginning of their ruin. The prophet uses graphic language deliberately: covenant unfaithfulness is not a polite abstraction."
    },
    "4": {
      "L": "And the names of them were Aholah the elder, and Aholibah her sister: and they were mine, and they bare sons and daughters. Thus were their names; Samaria is Aholah, and Jerusalem Aholibah.",
      "M": "Their names were Oholah the elder and Oholibah her sister. They became mine, and they bore sons and daughters. Now Oholah is Samaria, and Oholibah is Jerusalem.",
      "T": "The elder was Oholah — 'her tent,' the worship sites outside Jerusalem — and the younger Oholibah — 'my tent is in her,' Jerusalem, where God placed his own Name. Both became mine: I entered covenant with them; they bore children to me. Oholah is Samaria; Oholibah is Jerusalem. The younger was the more privileged — and will prove the more guilty."
    },
    "5": {
      "L": "And Aholah played the harlot when she was mine; and she doted on her lovers, on the Assyrians her neighbours,",
      "M": "Oholah played the harlot while she was mine; she was consumed with desire for her lovers — the Assyrians, her neighbors,",
      "T": "While still in covenant with me, Oholah — Samaria — gave herself to foreign powers. She burned with obsessive desire for the Assyrians, who lived close by."
    },
    "6": {
      "L": "Which were clothed with blue, captains and rulers, all of them desirable young men, horsemen riding upon horses.",
      "M": "clothed in blue — captains and rulers, all of them handsome young men, horsemen riding horses.",
      "T": "They were impressive: officers in royal blue, every one of them the kind of powerful, mounted soldier a nation finds irresistible. Samaria saw their military strength and wanted an alliance with it."
    },
    "7": {
      "L": "Thus she committed her whoredoms with them, with all them that were the chosen men of Assyria, and with all on whom she doted: with all their idols she defiled herself.",
      "M": "She committed whoredom with all the elite men of Assyria and defiled herself with all their idols — with all on whom she doted.",
      "T": "She gave herself entirely to Assyria's finest men — and in doing so took on their idols as well. Political alliance meant religious compromise: you adopted the gods of your patron. She gave herself to everyone she was infatuated with."
    },
    "8": {
      "L": "Neither left she her whoredoms brought from Egypt: for in her youth they lay with her, and they bruised the teats of her virginity, and poured their whoredom upon her.",
      "M": "She never abandoned the whoredoms she had learned in Egypt; for in her youth they had lain with her, handled her virgin breasts, and poured out their lust upon her.",
      "T": "The Egypt-habit never left her. Foreign men had first shaped Samaria in her formative years — had stamped their influence on her from the beginning, had poured their corrupting power over her. Every subsequent unfaithfulness carried Egypt with it."
    },
    "9": {
      "L": "Wherefore I have delivered her into the hand of her lovers, into the hand of the Assyrians, upon whom she doted.",
      "M": "Therefore I delivered her into the hand of her lovers, into the hand of the Assyrians on whom she had doted.",
      "T": "So I let her have them. I handed her over to the very Assyrians she had obsessed over — into their actual hands, not as a lover but as a prisoner. The object of her desire became her destroyer."
    },
    "10": {
      "L": "These discovered her nakedness: they took her sons and her daughters, and slew her with the sword: and she became famous among women; for they had executed judgment upon her.",
      "M": "They stripped her naked; they took her sons and daughters and killed her with the sword — and she became an object of infamy among women, for judgment had been executed upon her.",
      "T": "They stripped her of every protection. They took her children — her future. They put her to the sword. Among all nations she became a warning — a case study in what happens when God's people prostitute themselves to foreign powers. The Assyrian conquest of Samaria in 722 BC was not simply geopolitics. It was the judgment of God carried out through the instrument of Samaria's own chosen lovers."
    },
    "11": {
      "L": "And when her sister Aholibah saw this, she was more corrupt in her inordinate love than she, and in her whoredoms more than her sister in her whoredoms.",
      "M": "Yet her sister Oholibah saw this, and was more corrupt than her sister in her desire, and in her whoredoms more than her sister's whoredoms.",
      "T": "Jerusalem watched Samaria fall. And learned nothing. Instead of being deterred, Oholibah plunged deeper into the same pattern — more corrupt in her obsessions, more excessive in her unfaithfulness than Samaria had ever been. The warning was right there in front of her."
    },
    "12": {
      "L": "She doted upon the Assyrians her neighbours, captains and rulers clothed most gorgeously, horsemen riding upon horses, all of them desirable young men.",
      "M": "She was infatuated with the Assyrians — captains and rulers, all splendidly dressed, horsemen riding horses, every one of them a handsome young man.",
      "T": "Jerusalem too was consumed with desire for the Assyrians — the very power that had destroyed her sister. She wanted the same men, the same prestige, the same alliance. She looked at military splendor and was seized with longing."
    },
    "13": {
      "L": "Then I saw that she was defiled, that they took both one way.",
      "M": "Then I saw that she was defiled — both of them had taken the same way.",
      "T": "I saw it clearly: she was defiled. Both sisters had walked the same path — sought the same foreign powers, incurred the same guilt. Neither was innocent."
    },
    "14": {
      "L": "And that she increased her whoredoms: for when she saw men pourtrayed upon the wall, the images of the Chaldeans pourtrayed with vermilion,",
      "M": "And she increased her whoredoms; for when she saw men painted on the wall — images of Chaldeans painted in vermilion —",
      "T": "But Oholibah went further than Oholah. She saw paintings on a wall — images of Babylonian soldiers painted in vivid red — and was seized with desire."
    },
    "15": {
      "L": "Girded with girdles upon their loins, exceeding in dyed attire upon their heads, all of them princes to look to, after the manner of the Babylonians of Chaldea, the land of their nativity:",
      "M": "belted at the waist, with elaborate headdresses on their heads, all of them looking like officers, in the style of the Babylonians of Chaldea, the land of their origin —",
      "T": "Men portrayed in their military gear: belted at the waist, flowing turbans crowning their heads, every one looking like a senior commander — Babylonian fashion, Chaldean style. She fell for an image on a wall."
    },
    "16": {
      "L": "And as soon as she saw them with her eyes, she doted upon them, and sent messengers unto them into Chaldea.",
      "M": "As soon as she saw them she was inflamed with desire and sent messengers to them in Chaldea.",
      "T": "The instant she saw the images she was consumed with longing — and sent envoys all the way to Babylon to make contact. A painting on a wall was enough to set Jerusalem's foreign policy."
    },
    "17": {
      "L": "And the Babylonians came to her into the bed of love, and they defiled her with their whoredom, and she was polluted with them, and her mind was alienated from them.",
      "M": "And the Babylonians came to her into the bed of love and defiled her with their whoredom; she was polluted with them, and then her heart turned away from them.",
      "T": "The Babylonians came. The alliance was consummated — and Jerusalem was defiled by it, religiously and politically contaminated by the very relationship she had pursued. And then, as with all such obsessions, desire curdled: her heart turned cold toward them. She wanted them, had them, then despised them."
    },
    "18": {
      "L": "So she discovered her whoredoms, and discovered her nakedness: then my mind was alienated from her, like as my mind was alienated from her sister.",
      "M": "So she bared her whoredoms and uncovered her nakedness; then my heart turned from her, just as it had turned from her sister.",
      "T": "She made her unfaithfulness public — no longer pretending. She exposed herself completely. And that was when my heart withdrew. As it had turned from Samaria in disgust, now it turned from Jerusalem. The covenant had been prostituted beyond repair by her own choice."
    },
    "19": {
      "L": "Yet she multiplied her whoredoms, in calling to remembrance the days of her youth, wherein she had played the harlot in the land of Egypt.",
      "M": "Yet she multiplied her whoredoms by calling to mind the days of her youth, when she played the harlot in the land of Egypt.",
      "T": "And still she did not stop. She increased her prostitution by actively cultivating nostalgia for her earliest unfaithfulness — romanticizing her youth in Egypt as if the house of bondage were the homeland of her heart. She reached backward for the original corruption."
    },
    "20": {
      "L": "For she doted upon their paramours, whose flesh is as the flesh of asses, and whose issue is like the issue of horses.",
      "M": "She was obsessed with their lovers, whose flesh is like the flesh of donkeys and whose emission is like that of horses.",
      "T": "She was in the grip of raw, animalistic desire — fixated on men whose sexual power she imagined like that of animals: insatiable, overwhelming. This is the lowest point in the allegory. Ezekiel deliberately strips all romantic pretension from what Jerusalem's foreign entanglements actually were at the level of the desire driving them."
    },
    "21": {
      "L": "Thus thou calledst to remembrance the lewdness of thy youth, in bruising thy teats by the Egyptians for the paps of thy youth.",
      "M": "So you called to mind the lewdness of your youth, when the Egyptians pressed your breasts for the sake of your youthful nipples.",
      "T": "You were nostalgic for Egyptian exploitation. The depravity of your earliest years — being used by the Egyptians in your immaturity — you recast as a golden memory rather than a source of shame. You called your abuse home."
    },
    "22": {
      "L": "Therefore, O Aholibah, thus saith the Lord GOD; Behold, I will raise up thy lovers against thee, from whom thy mind is alienated, and I will bring them against thee on every side:",
      "M": "Therefore, O Oholibah, thus says the Lord GOD: Behold, I will raise up your lovers against you — those from whom your heart has turned — and bring them against you from every side:",
      "T": "Therefore, O Jerusalem. The Lord Yahweh says: The very men your heart has now turned from — the lovers you used and discarded — I will stir them up and direct them against you. From every direction. You no longer get to choose whom you reject."
    },
    "23": {
      "L": "The Babylonians, and all the Chaldeans, Pekod, and Shoa, and Koa, and all the Assyrians with them: all of them desirable young men, captains and rulers, great lords and renowned, all of them riding upon horses.",
      "M": "the Babylonians and all the Chaldeans — Pekod, Shoa, and Koa — and all the Assyrians with them: all of them handsome young men, captains and rulers, great lords and renowned commanders, all of them on horseback.",
      "T": "The full catalog: Babylonians, Chaldeans, Pekod, Shoa, Koa — the allied eastern peoples — and the Assyrians alongside them. All those desirable officers you once burned for. They are coming. Not as lovers. As conquerors."
    },
    "24": {
      "L": "And they shall come against thee with chariots, wagons, and wheels, and with an assembly of peoples, which shall set against thee buckler and shield and helmet round about: and I will set judgment before them, and they shall judge thee according to their judgments.",
      "M": "They shall come against you with weapons, chariots, and wagons, and with an assembly of peoples, setting against you buckler and shield and helmet all around; and I will commit the judgment to them, and they will judge you by their own ordinances.",
      "T": "They come fully armed — chariots, war wagons, a coalition of nations surrounding you with shields and helmets and weapons on every side. And I hand the judgment over to them. The nations will try you by their own standards, and those standards will not be gentle. What you invited as a lover you receive as a court."
    },
    "25": {
      "L": "And I will set my jealousy against thee, and they shall deal furiously with thee: they shall take away thy nose and thine ears; and thy remnant shall fall by the sword: they shall take thy sons and thy daughters; and thy residue shall be devoured by the fire.",
      "M": "I will direct my jealous wrath at you, and they will deal with you in fury: they will cut off your nose and your ears; your survivors will fall by the sword; they will carry off your sons and daughters; your remnant will be consumed by fire.",
      "T": "My jealousy — the burning response of a covenant God whose love has been spurned and whose honor trampled — I will unleash it through their hands. The mutilation of a convicted adulteress in the ancient world: nose and ears cut off, public shame. Your army falls by the sword. Your children are taken. Whatever remains is burned. This is what covenant-breaking produces at the end of the road."
    },
    "26": {
      "L": "They shall also strip thee out of thy clothes, and take away thy fair jewels.",
      "M": "They will also strip you of your clothing and take your fine jewelry.",
      "T": "They will take everything — even the clothes and jewelry that adorned you for your lovers. You are left with nothing."
    },
    "27": {
      "L": "Thus will I make thy lewdness to cease from thee, and thy whoredom brought from the land of Egypt: so that thou shalt not lift up thine eyes unto them, nor remember Egypt any more.",
      "M": "Thus I will bring your lewdness to an end — the whoredom you brought from Egypt — so that you will no longer look toward Egypt or remember it.",
      "T": "This is the cure. The only way to end Jerusalem's Egyptian nostalgia and Babylonian obsessions is through the very judgment she has brought on herself. After this there will be no more longing glances toward Egypt. The attraction will be completely burned out."
    },
    "28": {
      "L": "For thus saith the Lord GOD; Behold, I will deliver thee into the hand of them whom thou hatest, into the hand of them from whom thy mind is alienated:",
      "M": "For thus says the Lord GOD: Behold, I will deliver you into the hand of those you hate, into the hand of those from whom your heart has turned,",
      "T": "The Lord Yahweh says: I will give you over to the ones you now hate — the lovers you used and discarded. Your heart turned from them; now their hands will be on you."
    },
    "29": {
      "L": "And they shall deal with thee hatefully, and shall take away all thy labour, and shall leave thee naked and bare: and the nakedness of thy whoredoms shall be discovered, both thy lewdness and thy whoredoms.",
      "M": "and they will deal with you in hatred and take away all your labor, leaving you naked and bare; the nakedness of your whoredoms will be exposed — your lewdness and your whoredoms.",
      "T": "They will despise you as they act against you. Everything you built through those alliances — every advantage, every resource — they strip away. They leave you with nothing: stripped, exposed, humiliated. Your unfaithfulness, pursued in self-justification, is made completely public."
    },
    "30": {
      "L": "I will do these things unto thee, because thou hast gone a whoring after the heathen, and because thou art polluted with their idols.",
      "M": "I will do these things to you because you have gone whoring after the nations and defiled yourself with their idols.",
      "T": "The ground of the sentence: you pursued the nations and their gods. Political alliance and religious syncretism went together — you could not have one without the other. You contaminated yourself, and now you bear what you chose."
    },
    "31": {
      "L": "Thou hast walked in the way of thy sister; therefore will I give her cup into thine hand.",
      "M": "You have walked in the way of your sister; therefore I will give her cup into your hand.",
      "T": "You chose Samaria's path. Now you drink Samaria's cup. What happened to her comes to you."
    },
    "32": {
      "L": "Thus saith the Lord GOD; Thou shalt drink of thy sister's cup deep and large: thou shalt be laughed to scorn and had in derision; it containeth much.",
      "M": "Thus says the Lord GOD: You shall drink your sister's cup — deep and wide; you will be mocked and held in contempt; it holds a great deal.",
      "T": "The Lord Yahweh says: The cup is deep — a great deal in it. It is wide — nothing escapes it. You will drink it in full. And the nations who watch will not sympathize: they will laugh and mock. Judgment that falls on one who should have known better draws no pity from the gallery."
    },
    "33": {
      "L": "Thou shalt be filled with drunkenness and sorrow, with the cup of astonishment and desolation, with the cup of thy sister Samaria.",
      "M": "You will be filled with drunkenness and grief — the cup of horror and desolation — the cup of your sister Samaria.",
      "T": "What the cup produces: intoxication that undoes judgment, grief that overwhelms the spirit, horror at what has come upon you, desolation — the landscape of a city and a people utterly emptied. Samaria's cup. Jerusalem must drink it too."
    },
    "34": {
      "L": "Thou shalt even drink it and suck it out, and thou shalt break the sherds thereof, and pluck off thine own breasts: for I have spoken it, saith the Lord GOD.",
      "M": "You will drink it and drain it; you will gnaw its shards and tear out your own breasts; for I have spoken, declares the Lord GOD.",
      "T": "You drain the cup to the last drop. You gnaw the broken pottery trying to get more out of it — the judgment is total and consumes even the vessel. You tear at your own body in anguish. There is no mitigation: I have spoken it. The Lord Yahweh has declared it."
    },
    "35": {
      "L": "Therefore thus saith the Lord GOD; Because thou hast forgotten me, and cast me behind thy back, therefore bear thou also thy lewdness and thy whoredoms.",
      "M": "Therefore thus says the Lord GOD: Because you have forgotten me and cast me behind your back, therefore bear your lewdness and your whoredoms.",
      "T": "Therefore. The Lord Yahweh brings the charge down to its simplest form: you forgot me. You put me behind your back — literally discarded all knowledge of who I am. So now you carry what you chose. You bear the full weight of your own depravity and unfaithfulness."
    },
    "36": {
      "L": "The LORD said moreover unto me; Son of man, wilt thou judge Aholah and Aholibah? yea, declare unto them their abominations;",
      "M": "The LORD said to me: Son of man, will you judge Oholah and Oholibah? Then declare to them their abominations.",
      "T": "Yahweh said to me: Son of man, will you pronounce judgment against both sisters? Then here are the charges — lay them out plainly."
    },
    "37": {
      "L": "That they have committed adultery, and blood is in their hands, and with their idols have they committed adultery, and have also caused their sons, whom they bare unto me, to pass for them through the fire, to devour them.",
      "M": "For they have committed adultery, and blood is on their hands; with their idols they have committed adultery; and they have also caused their children — whom they bore to me — to pass through fire to be consumed for them.",
      "T": "The charges: spiritual adultery against the covenant; murder — blood on their hands; idolatrous adultery, giving themselves to foreign gods; and child sacrifice — offering to their idols the very children they bore to me. They gave me children and then gave those children to their idols. There is no lower point."
    },
    "38": {
      "L": "Moreover this they have done unto me: they have defiled my sanctuary in the same day, and have profaned my sabbaths.",
      "M": "Moreover, this they have done to me: they have defiled my sanctuary on the same day and profaned my sabbaths.",
      "T": "And this too: the same day they sacrificed their children to idols they came into my sanctuary — entering the holy space with blood on their hands. And they treated my sabbaths with contempt, the covenant-signs of Israel's relationship with me. They used my house as though it were simply one religious site among many."
    },
    "39": {
      "L": "For when they had slain their children to their idols, then they came the same day into my sanctuary to profane it; and, lo, thus have they done in the midst of mine house.",
      "M": "For after slaughtering their children for their idols, they came that same day into my sanctuary to profane it. Behold, this is what they did in the midst of my house.",
      "T": "To be explicit about the sequence: children killed at the idol altars in the morning, then the same people entering my sanctuary in the afternoon. The sanctuary itself defiled by the presence of those who had just committed murder in the name of other gods. This is what was happening in the city that bore my name."
    },
    "40": {
      "L": "And furthermore, that ye have sent for men to come from far, unto whom a messenger was sent; and, lo, they came: for whom thou didst wash thyself, paintedst thy eyes, and deckedst thyself with ornaments,",
      "M": "Furthermore, you sent for men from far away — a messenger was dispatched — and indeed they came. For them you bathed yourself, painted your eyes, and adorned yourself with jewelry,",
      "T": "And there was something even more calculated about Oholibah's behavior: she actively recruited distant suitors, sent out envoys, prepared herself for them as a woman preparing for a lover. She did not fall into it passively. She sought it out."
    },
    "41": {
      "L": "And satest upon a stately bed, and a table prepared before it, whereupon thou hast set mine incense and mine oil.",
      "M": "and you sat on a magnificent couch, with a table prepared before it, on which you had placed my incense and my oil.",
      "T": "She arranged herself on an exquisite bed with a table set for the feast — and on that table, as décor for a seduction scene, she placed my incense and my oil. Sacred offerings designated for my worship, used to ornament the setting for her infidelity. She took what was mine and made it part of her prostitution."
    },
    "42": {
      "L": "And a voice of a multitude being at ease was with her: and with the men of the common sort were brought Sabeans from the wilderness, which put bracelets upon their hands, and beautiful crowns upon their heads.",
      "M": "The sound of an unconcerned crowd was with her; and along with ordinary men, Sabeans were brought from the wilderness who put bracelets on their hands and beautiful crowns on their heads.",
      "T": "The setting: a crowd at ease, celebrating — the tone of a party, casual and comfortable with what was happening. Among the men brought in were desert wanderers, Sabeans, adorned with bracelets and ornamental crowns. Jerusalem entertained her lovers royally."
    },
    "43": {
      "L": "Then said I unto her that was old in adulteries, Will they now commit whoredoms with her, and she with them?",
      "M": "Then I said of her who was worn out by adulteries: Will they still commit whoredom with her — even now?",
      "T": "God's comment on the scene: she is worn out — aged and used up by her own choices — and yet they keep coming, and she keeps welcoming them. The question carries contempt: even now, even in this state, the cycle continues."
    },
    "44": {
      "L": "Yet they went in unto her, as they go in unto a woman that playeth the harlot: so went they in unto Aholah and unto Aholibah, the lewd women.",
      "M": "Yet they went in to her as men go in to a prostitute. So they went in to Oholah and to Oholibah, the lewd women.",
      "T": "And so the allegory closes with this stark statement: the two sisters were prostitutes, and they were treated as such. The nations came to them as clients, not suitors. This is what Samaria and Jerusalem had made themselves in God's sight — what their foreign policy and religious syncretism amounted to."
    },
    "45": {
      "L": "And the righteous men, they shall judge them after the manner of adulteresses, and after the manner of women that shed blood; because they are adulteresses, and blood is in their hands.",
      "M": "Righteous men will judge them as adulteresses and as women who shed blood, because they are adulteresses and blood is on their hands.",
      "T": "The verdict is passed by those who are themselves righteous — the moral order itself pronounces it. Adultery and murder: both charges proven. The sentence is death — the penalty for both crimes under the covenant law both kingdoms had sworn to uphold."
    },
    "46": {
      "L": "For thus saith the Lord GOD; I will bring up a company upon them, and will give them to be removed and spoiled.",
      "M": "For thus says the Lord GOD: I will bring up an assembly against them and make them an object of terror and plunder.",
      "T": "The Lord Yahweh commissions the execution of the verdict: a coalition of nations is called up against them. They will become an object of horror — something the watching world recoils from — and of total plunder."
    },
    "47": {
      "L": "And the company shall stone them with stones, and dispatch them with their swords; they shall slay their sons and their daughters, and burn up their houses with fire.",
      "M": "The assembly will stone them with stones and put them to the sword; they will kill their sons and daughters and burn their houses.",
      "T": "The execution: stoning for the adulteresses, sword for the rest, death for the children, fire for the city. Every element of the ancient penalty for covenant infidelity is carried out. This is what Babylon would do to Jerusalem in 586 BC — and Ezekiel names it as the fulfillment of covenant law."
    },
    "48": {
      "L": "Thus will I cause lewdness to cease out of the land, that all women may be taught not to do after your lewdness.",
      "M": "Thus I will bring lewdness to an end in the land, so that all women may be warned not to imitate your lewdness.",
      "T": "The purpose of the judgment extends beyond the two sisters: when God makes an example, the witness is for all. Covenant unfaithfulness of this kind must end — and the public nature of the reckoning is the lesson for all who observe it. Israel's judgment instructs the nations."
    },
    "49": {
      "L": "And they shall recompense your lewdness upon you, and ye shall bear the sins of your idols: and ye shall know that I am the Lord GOD.",
      "M": "Your lewdness will be returned upon you, and you will bear the guilt of your idols; and you will know that I am the Lord GOD.",
      "T": "The sentence circles back: you will receive exactly what your choices produced. The guilt of every idol you worshipped falls on you — you chose them over me, and their judgment is yours to carry. But in the end — through all of this — you will know who I am. The Lord Yahweh. Even the severest judgment carries this purpose: that those who survive, and those who watch, will know that I am God."
    }
  },
  "24": {
    "1": {
      "L": "Again in the ninth year, in the tenth month, in the tenth day of the month, the word of the LORD came unto me, saying,",
      "M": "In the ninth year, in the tenth month, on the tenth day of the month, the word of the LORD came to me:",
      "T": "Yahweh's word came to me in the ninth year of Jehoiachin's exile, on the tenth day of the tenth month — the exact date Nebuchadnezzar set his siege around Jerusalem, though Ezekiel was hundreds of miles away in Babylon. Ezekiel later records this date (24:2) as one verifiable by the exiles; it became exactly that."
    },
    "2": {
      "L": "Son of man, write thee the name of the day, even of this same day: the king of Babylon set himself against Jerusalem this same day.",
      "M": "Son of man, write down the name of this day, this very day. The king of Babylon has laid siege to Jerusalem this very day.",
      "T": "Son of man, record this date permanently. The king of Babylon has begun his siege against Jerusalem — today. Ezekiel is in Babylon and Yahweh tells him what is happening simultaneously in Jerusalem. This is not Nebuchadnezzar's war alone: it is Yahweh's judgment, announced in both places at once."
    },
    "3": {
      "L": "And utter a parable unto the rebellious house, and say unto them, Thus saith the Lord GOD; Set on a pot, set it on, and also pour water into it:",
      "M": "Speak a parable to the rebellious house and say, Thus says the Lord GOD: Set on the pot, set it on, and pour water into it.",
      "T": "Say to that stubborn, covenant-refusing house a parable. The Lord Yahweh says: Get out the pot. Put it on the fire. Fill it with water."
    },
    "4": {
      "L": "Gather the pieces thereof into it, even every good piece, the thigh, and the shoulder; fill it with the choice bones.",
      "M": "Gather into it every good piece — thigh and shoulder; fill it with choice bones.",
      "T": "Fill the pot with the best pieces of meat — thigh and shoulder, the prime cuts. Pack in the finest bones. The city of Jerusalem is the pot; her people are the pieces."
    },
    "5": {
      "L": "Take the choice of the flock, and burn also the bones under it, and make it boil well, and let them seethe the bones of it therein.",
      "M": "Take the choicest of the flock; pile up the bones under it; boil it well and let the bones seethe within it.",
      "T": "The best animal, the best fire, the best pieces — boil the whole thing until the bones themselves are seething. A rich, boiling pot: that is what Jerusalem looks like. But the fire is not the fire of abundance. It is the fire of judgment."
    },
    "6": {
      "L": "Wherefore thus saith the Lord GOD; Woe to the bloody city, to the pot whose scum is therein, and whose scum is not gone out of it! bring it out piece by piece; let no lot fall upon it.",
      "M": "Therefore thus says the Lord GOD: Woe to the city of blood — the pot whose scum is in it, whose scum has not gone out! Empty it piece by piece; let no lot be cast for it.",
      "T": "Woe — the prophetic word of doom — falls on Jerusalem, the city of blood. The pot image shifts: the scum floating on top is accumulated bloodguilt that will not come off no matter how the pot is cleaned. Take the pieces out one by one. Do not draw lots to spare any of them. Every piece comes out. No one is randomly exempted."
    },
    "7": {
      "L": "For her blood is in the midst of her; she set it upon the top of a rock; she poured it not upon the ground, to cover it with dust;",
      "M": "For her blood is within her; she placed it on a bare rock; she did not pour it on the ground to cover it with dust.",
      "T": "The detail is specific: when blood was shed in Jerusalem, it was left in the open — on bare rock where it could not be absorbed and covered, as the law required (Lev 17:13). Unjust blood cries out from the ground (Gen 4:10); this blood cries out from rock, louder and longer. Jerusalem's bloodguilt was exposed, unashamed, unburied."
    },
    "8": {
      "L": "That it might cause fury to come up to take vengeance; I have set her blood upon the top of a rock, that it should not be covered.",
      "M": "To stir up fury and to execute vengeance, I placed her blood on a bare rock so that it would not be covered.",
      "T": "God himself made the exposed blood a deliberate act: I set it there in the open. The uncovered blood is the legal proof that demands vengeance. God is not overlooking what Jerusalem has done — he is the one ensuring the record remains visible until judgment comes."
    },
    "9": {
      "L": "Therefore thus saith the Lord GOD; Woe to the bloody city! I will even make the pile for fire great.",
      "M": "Therefore thus says the Lord GOD: Woe to the city of blood! I also will make the pile of fuel great.",
      "T": "The Lord Yahweh repeats the woe — and now acts as the stoker of the fire: I will heap on the wood. The judgment that comes on Jerusalem is not Nebuchadnezzar's casual conquest. It is God deliberately feeding the flames."
    },
    "10": {
      "L": "Heap on wood, kindle the fire, consume the flesh, and spice it well, and let the bones be burned.",
      "M": "Heap on the wood, kindle the fire, cook the flesh well, mix in the spices, and let the bones be burned.",
      "T": "More fuel, more fire — cook everything through, bones and all. The siege and its aftermath: the city utterly consumed, nothing preserved."
    },
    "11": {
      "L": "Then set it empty upon the coals thereof, that the brass of it may be hot, and may burn, and that the filthiness of it may be molten in it, that the scum of it may be consumed.",
      "M": "Then set it empty on its coals, so that it may become hot and its bronze glow; that its filthiness may melt within it and its scum be consumed.",
      "T": "Now set the empty pot on the coals — still on fire after all the pieces have been removed. Let the metal itself become red-hot. The filth clinging to the metal: burn it off. The scum lining the inside: consume it. The judgment is not only on the contents — it is on the vessel itself, the city whose very walls have absorbed generations of guilt."
    },
    "12": {
      "L": "She hath wearied herself with lies, and her great scum went not forth out of her: her scum shall be in the fire.",
      "M": "She has wearied herself with deception; her great scum has not gone out of her. Into the fire with her scum!",
      "T": "Jerusalem wore herself out with pretense — false repentances, surface reforms, the appearance of covenant faithfulness without the substance. And all of it was insufficient: the scum — the embedded, baked-in guilt — did not leave. Only fire removes it now."
    },
    "13": {
      "L": "In thy filthiness is lewdness: because I have purged thee, and thou wast not purged, thou shalt not be purged from thy filthiness any more, till I have caused my fury to rest upon thee.",
      "M": "In your filthiness is lewdness. Because I tried to cleanse you and you would not be cleansed, you will not be cleansed from your filthiness until I have spent my fury upon you.",
      "T": "The tragedy: God made effort after effort to cleanse Jerusalem — prophets, warnings, partial judgments, calls to repentance. None of it took. The filth was too deep, the commitment to it too ingrained. And so the only path forward is the complete exhausting of divine wrath. It is not cruelty; it is the end of every other option."
    },
    "14": {
      "L": "I the LORD have spoken it: it shall come to pass, and I will do it; I will not go back, neither will I spare, neither will I repent: according to thy ways, and according to thy doings, shall they judge thee, saith the Lord GOD.",
      "M": "I the LORD have spoken; it shall come to pass and I will act. I will not relent, nor will I spare, nor will I repent. According to your ways and your deeds I will judge you, declares the Lord GOD.",
      "T": "I, Yahweh, have spoken this. It will happen. I will carry it through. There will be no mercy-halt, no change of mind, no final stay of execution. The sentence follows exactly the deeds — you did this, and this is what follows. The Lord Yahweh has declared it."
    },
    "15": {
      "L": "Also the word of the LORD came unto me, saying,",
      "M": "Also the word of the LORD came to me, saying:",
      "T": "Yahweh's word came to me again:"
    },
    "16": {
      "L": "Son of man, behold, I take away from thee the desire of thine eyes with a stroke: yet neither shalt thou mourn nor weep, neither shall thy tears run down.",
      "M": "Son of man, behold, I am taking from you the desire of your eyes with a sudden stroke. Yet you shall not mourn or weep, nor shall your tears run down.",
      "T": "Son of man: I am about to take from you the person you love most — suddenly, with a single blow. And you must not mourn. No tears. No lamentation. This is not a command to stop feeling; it is a command to hold the grief in silence as a prophetic sign."
    },
    "17": {
      "L": "Forbear to cry, make no mourning for the dead, bind the tire of thine head upon thee, and put on thy shoes upon thy feet, and cover not thy lips, and eat not the bread of men.",
      "M": "Sigh quietly, but make no mourning for the dead. Bind your turban on your head; put your sandals on your feet; do not cover your lips or eat the bread of mourners.",
      "T": "The mourning rites of ancient Israel: public weeping, removing sandals, covering the lower face as a sign of grief, eating the bread neighbors brought to the bereaved house. Ezekiel is commanded to do none of this — not because grief is forbidden but because the suppressed grief is itself the message. He sighs. But nothing else."
    },
    "18": {
      "L": "So I spake unto the people in the morning: and at even my wife died; and I did in the morning as I was commanded.",
      "M": "So I spoke to the people in the morning; and in the evening my wife died. And the next morning I did as I was commanded.",
      "T": "He preached in the morning. His wife died that evening. And the next day he got up and did not mourn. This is one of the most costly prophetic sign-acts in the entire Bible. The personal cost of Ezekiel's calling is made viscerally present here: he bore his grief in silence so that Israel could see in him what their own response to coming catastrophe must look like."
    },
    "19": {
      "L": "And the people said unto me, Wilt thou not tell us what these things are to us, that thou doest so?",
      "M": "And the people said to me: Will you not tell us what these things mean for us, that you are acting this way?",
      "T": "The people asked — and the question was exactly right. They sensed that his uncharacteristic silence in grief was a sign directed at them. They were not wrong."
    },
    "20": {
      "L": "Then I answered them, The word of the LORD came unto me, saying,",
      "M": "Then I answered them: The word of the LORD came to me, saying:",
      "T": "I told them: this is not my idea. Yahweh's word came to me:"
    },
    "21": {
      "L": "Speak unto the house of Israel, Thus saith the Lord GOD; Behold, I will profane my sanctuary, the excellency of your strength, the desire of your eyes, and that which your soul pitieth; and your sons and your daughters whom ye have left shall fall by the sword.",
      "M": "Speak to the house of Israel, Thus says the Lord GOD: Behold, I will profane my sanctuary — the pride of your strength, the desire of your eyes, the longing of your soul — and your sons and daughters whom you have left behind will fall by the sword.",
      "T": "Here is the meaning: I will do to my sanctuary what I did to Ezekiel's wife — take it away suddenly. The temple was everything to Israel: their pride, the desire of their eyes, the longing of their deepest being. And their children left behind in Jerusalem will be killed. Everything they hold most dear: I am removing it. This is what the siege that began today will accomplish."
    },
    "22": {
      "L": "And ye shall do as I have done: ye shall not cover your lips, nor eat the bread of men.",
      "M": "And you shall do as I have done: you shall not cover your lips or eat the bread of mourners.",
      "T": "When the news reaches the exiles in Babylon, this is how they will respond: not with the customary rites of grief but with Ezekiel's silent anguish. The catastrophe will be too large for the normal forms of mourning."
    },
    "23": {
      "L": "And your tires shall be upon your heads, and your shoes upon your feet: ye shall not mourn nor weep; but ye shall pine away for your iniquities, and mourn one toward another.",
      "M": "Your turbans will be on your heads and your sandals on your feet; you will not mourn or weep, but you will waste away in your iniquities and groan to one another.",
      "T": "The headdress stays on. The sandals stay on. No formal mourning — and yet there will be a deeper grieving: they will waste away, hollowed out by the weight of understanding that they brought this on themselves. They will groan quietly to each other, not with formal lamentation but with the inward collapse of those who have no answer to make."
    },
    "24": {
      "L": "Thus Ezekiel is unto you a sign: according to all that he hath done shall ye do: and when this cometh, ye shall know that I am the Lord GOD.",
      "M": "Thus Ezekiel is a sign to you; according to all that he has done, you shall do. When this comes, you will know that I am the Lord GOD.",
      "T": "The prophet himself is the sign. Not just his words, not just his gestures — his life, his grief, his obedience in an impossible moment. When the temple falls and your sons and daughters are killed and you cannot properly mourn: you will live out what Ezekiel lived out. And in that living you will know: I am the Lord Yahweh. The recognition formula at the end of catastrophe — not triumph but knowledge through loss."
    },
    "25": {
      "L": "Also, thou son of man, shall it not be in the day when I take from them their strength, the joy of their glory, the desire of their eyes, and that whereupon they set their minds, their sons and their daughters,",
      "M": "And you, son of man — will it not be on the day when I take from them their stronghold, the joy of their glory, the desire of their eyes, and the longing of their souls — their sons and daughters —",
      "T": "Son of man, on the day I do this — the day I remove their fortress-city, their glorious temple, the love of their eyes, the longing of everything in them — and their children —"
    },
    "26": {
      "L": "That he that escapeth in that day shall come unto thee, to cause thee to hear it with thine ears?",
      "M": "on that day a fugitive will come to you to bring the news to your ears.",
      "T": "on that day someone will arrive — a survivor, a refugee from the fallen city — and he will tell you with his own mouth what has happened."
    },
    "27": {
      "L": "In that day shall thy mouth be opened to him which is escaped, and thou shalt speak, and be no more dumb: and thou shalt be a sign unto them; and they shall know that I am the LORD.",
      "M": "On that day your mouth will be opened to the fugitive; you will speak and be mute no longer. So you will be a sign to them, and they will know that I am the LORD.",
      "T": "On that day your long silence ends. When the refugee arrives with news of the temple's fall, your mouth opens again. Your freedom to speak will itself be the sign: the judgment has been accomplished exactly as declared. And they will know — the survivors, the exiles, all who watch — that I am Yahweh."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'ezekiel')
        merge_tier(existing, EZEKIEL, tier_key)
        save(tier_dir, 'ezekiel', existing)
    print('Ezekiel 23–24 written.')

if __name__ == '__main__':
    main()
