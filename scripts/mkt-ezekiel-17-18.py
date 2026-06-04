"""
MKT Ezekiel chapters 17–18 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-ezekiel-17-18.py

Translation decisions (carrying forward all conventions from mkt-ezekiel-13-15.py):

- H3068 (יהוה): "LORD" in L/M throughout. "Yahweh" in T — especially for the recognition
  formula ("you shall know that I am the LORD"), the oracle-oath formula ("as I live"),
  and narrative turning points. Consistent with all prior Ezekiel scripts.

- H136 + H3069 (אֲדֹנָי יְהוִה / Adonai-Yahweh): "Lord GOD" in L/M (small-caps GOD);
  "Lord Yahweh" in T. The combined form dominates Ezekiel's oracle introductions.

- H7307 (רוּחַ): Ch. 17:10 uses "east wind" (רוּחַ הַקָּדִים) — purely atmospheric, rendered
  "east wind" / "wind" in all three tiers. Ch. 18:31 "new spirit" (רוּחַ חֲדָשָׁה) = spiritual
  renewal; rendered "spirit" (lowercase, since this is the human spirit being transformed,
  not a divine title) in L/M; T: "transformed inner life" or "new spirit."

- H5315 (נֶפֶשׁ / soul/life/person): Pivotal in ch. 18. The formula "the soul that sinneth,
  it shall die" (18:4, 20) uses נֶפֶשׁ as "the individual person." L preserves "soul"
  (traditional and Strong's-accurate). M uses "person" where the individual-accountability
  sense is primary. T unpacks the personal nature of the verdict.

- H1285 (בְּרִית / covenant): Major term in ch. 17. Zedekiah's covenant with Nebuchadnezzar,
  and (by extension) with God who ratified the oath. "Covenant" in all tiers; T surfaces the
  formal, oath-bound, legally structured nature of the relationship.

- H423 (אָלָה / oath/curse): Ch. 17 — the oath Zedekiah swore to Babylon (vv. 13, 16, 18, 19).
  "Oath" in L/M. T develops the sacred weight of the covenant oath in the ancient world:
  swearing by God's name means God is the guarantor; to despise it is to insult God himself.

- H4912 / H2420 (מָשָׁל / parable; חִידָה / riddle): The allegory of the two eagles is
  introduced as both a riddle and a parable (17:2). L/M: "riddle" and "parable" respectively.
  T: "riddle" / "allegory" — the word "allegory" better captures the extended sustained
  metaphor in English than "parable" (which implies a narrative of human characters).

- H5404 (נֶשֶׁר / eagle): Both eagles = great imperial powers (Babylon and Egypt). "Eagle"
  in all tiers. The first eagle = Nebuchadnezzar of Babylon; the second eagle = Pharaoh
  of Egypt; both identifications are given by the text itself at v. 12 and v. 15.

- H730 (אֶרֶז / cedar): "Cedar" in all tiers. The cedar = the Davidic royal line / Israelite
  kingship. The topmost branch = Jehoiachin (taken to Babylon, 597 BC). The tender shoot
  planted on the mountain at vv. 22–24 = the messianic restoration — God himself planting
  the royal line on Israel's mountain. The allegory moves from judgment to eschatological hope.

- H6788 (צַמֶּרֶת / crown/topmost branch): The crown of the cedar. L: "highest branch."
  M: "top / topmost." T: "topmost crown" or "crown" to capture the regal symbolism.

- H4775 (מָרַד / rebelled): Zedekiah's political rebellion = covenant faithlessness. "Rebelled"
  in L/M; T: "rebelled against / broke faith with."

- H6743 (צָלַח / prosper): 17:9, 10, 15 — "Shall it/he prosper?" The rhetorical question
  format is maintained across all tiers. The answer in all three cases is implied: No.

- H6662 / H7563 (צַדִּיק / righteous; רָשָׁע / wicked): The central moral categories of ch. 18.
  "Righteous" and "wicked" in L/M throughout. T may contextually expand to "a person
  who is just / a person who is wicked" where the individual-accountability emphasis calls
  for it.

- H6588 (פֶּשַׁע / transgression/rebellion): "Transgressions" in L/M. T: "acts of rebellion"
  where the covenant-violation meaning is prominent.

- H7725 (שׁוּב / turn/repent/return): The call to repentance in 18:21, 27, 30, 32. L: "turn."
  M: "turn / repent." T: "turn, repent" where the full English vocabulary of moral
  conversion best captures the covenantal return.

- H4603/H4604 (מָעַל / trespass/faithlessness): Ch. 17:20 — Zedekiah's covenant-trespass
  against God. "Trespass" in L; "faithlessness" in M/T — this is the technical covenant-
  breach term for violating a sacred trust.

- H8505 (תָּכֵן / equal/weigh): 18:25, 29 — "Is not my way equal?" The word means weighed,
  assessed, measured equally. L: "equal." M: "fair." T: "fair/just" — develops the
  accusation that God applies unequal standards (which he refutes).

- H2421 / H4191 (חָיָה / live; מוּת / die): The antithetical formula throughout ch. 18:
  "he shall surely live" and "he shall surely die." The emphatic infinitive absolute is
  preserved with "surely" in L/M; T varies for natural emphasis.

- Aspect notes for ch. 17:
  - The allegory (vv. 3–10) uses predominantly Hebrew perfect forms describing completed
    actions, but vv. 9–10 shift to rhetorical questions about future outcome (imperfect).
    L/M/T follow the tense signal: allegory in past, questions in future/conditional.
  - The interpretation (vv. 12–21) uses prophetic perfect for the coming judgment — rendered
    as future throughout.
  - The restoration oracle (vv. 22–24) is introduced by "I will" (imperfect first person)
    — explicitly eschatological future.

- Aspect notes for ch. 18:
  - The two long case studies (righteous man vv. 5–9; wicked son vv. 10–13) use Hebrew
    perfect consistently — completed conduct characterizing a type. English present perfect
    ("He has not done X") or simple present ("He does not X") captures this in M/T.
  - The formula "he shall surely live" (חָיֹה יִחְיֶה) = emphatic infinitive absolute +
    imperfect = absolute certainty; preserved as "he shall surely live" in L, "he will
    certainly live" optional in M/T.
  - The call to repentance (vv. 30–32) uses imperatives — retained as imperatives in all tiers.

- OT intertextuality:
  - Ch. 17:22–24 echoes Daniel 4 (great tree sheltering all nations), Isaiah 2:2 (mountain
    of the Lord), and Psalm 80 (vine from Egypt). The messianic cedar on Israel's mountain
    reverses the allegory of the failed vine (Zedekiah). T surfaces these connections.
  - Ch. 18 is a theological counterpoint to Exodus 20:5 ("visiting the iniquity of the
    fathers upon the children"). The tension is real: Ezekiel's individual accountability
    doctrine is not a contradiction of corporate solidarity but a pastoral correction for
    a specific misuse of that doctrine as an excuse. T notes this.
  - The "new heart and new spirit" of 18:31 anticipates the explicitly divine gift of
    36:26–27 ("I will give you a new heart"). Here it is a command; there it is a promise.
    T notes the escalation.
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
  "17": {
    "1": {
      "L": "And the word of the LORD came unto me, saying:",
      "M": "The word of the LORD came to me:",
      "T": "Yahweh's word came to me:"
    },
    "2": {
      "L": "Son of man, put forth a riddle, and speak a parable unto the house of Israel.",
      "M": "Son of man, propound a riddle and speak a parable to the house of Israel.",
      "T": "Son of man, set a riddle before them — and frame it as an allegory for the house of Israel."
    },
    "3": {
      "L": "And say: Thus saith the Lord GOD: A great eagle with great wings, long-winged, full of feathers which had divers colours, came unto Lebanon, and took the highest branch of the cedar.",
      "M": "Say: Thus says the Lord GOD: A great eagle with great wings, long-winged and full of colorful feathers, came to Lebanon and took the topmost branch of the cedar.",
      "T": "Say from the Lord Yahweh: A great eagle — enormous wings, long pinions, covered in plumage of every color — swooped down on Lebanon and seized the topmost crown of the cedar."
    },
    "4": {
      "L": "He cropped off the top of his young twigs and carried it into a land of traffick; he set it in a city of merchants.",
      "M": "He cropped off the topmost of its young shoots and carried it to a land of traders; he set it down in a city of merchants.",
      "T": "He snapped off the crown-shoot — the topmost growth — and carried it away to a trading land, setting it down in a merchant city. This is Babylon receiving Jehoiachin."
    },
    "5": {
      "L": "He took also of the seed of the land, and planted it in a fruitful field; he placed it by great waters, and set it as a willow tree.",
      "M": "He also took some of the seed of the land and planted it in fertile soil; he set it beside abundant water, like a willow tree.",
      "T": "Then he took a seed from the land itself — a cutting from Israel's own stock — and planted it in rich, well-watered ground, setting it like a willow at the river's edge. This is Zedekiah, installed in the land under Babylonian care."
    },
    "6": {
      "L": "And it grew, and became a spreading vine of low stature, whose branches turned toward him, and the roots thereof were under him; so it became a vine, and brought forth branches, and shot forth sprigs.",
      "M": "It grew and became a spreading vine of low height, whose branches turned toward the eagle and whose roots reached under him; so it became a vine, producing branches and sending out shoots.",
      "T": "It grew — spreading, sprawling, low to the ground. Its branches stretched back toward the eagle who planted it; its roots ran under him. A vine rather than a cedar: humble, dependent, alive only because of Babylonian sponsorship."
    },
    "7": {
      "L": "There was also another great eagle with great wings and many feathers: and behold, this vine did bend her roots toward him, and shot forth her branches toward him, that he might water it by the furrows of her plantation.",
      "M": "But there was another great eagle with great wings and many feathers — and behold, this vine bent its roots toward him and stretched its branches toward him to be watered by him, from the furrows of its planting.",
      "T": "But there was a second eagle — also great-winged, also well-feathered. And this vine, dissatisfied with its Babylonian water, bent its roots away from the first eagle and stretched toward the second, seeking irrigation from him instead. This is Zedekiah turning to Egypt."
    },
    "8": {
      "L": "It was planted in a good soil by great waters, that it might bring forth branches, and that it might bear fruit, that it might be a goodly vine.",
      "M": "It had been planted in good soil beside abundant water, to produce branches and bear fruit — to become a fine vine.",
      "T": "The planting was good — rich soil, abundant water, conditions perfectly suited to make it flourish. There was no legitimate reason to seek another water source. The vine had everything it needed from its planter."
    },
    "9": {
      "L": "Say thou: Thus saith the Lord GOD: Shall it prosper? Shall he not pull up the roots thereof, and cut off the fruit thereof, that it wither? Yea, all the leaves of her spring shall wither, even without great power or many people to pluck it up by the roots thereof.",
      "M": "Say: Thus says the Lord GOD: Will it prosper? Will he not pull up its roots and cut off its fruit so that all its fresh shoots wither? It will not take great force or many people to pull it up by the roots.",
      "T": "Say from the Lord Yahweh: Will this vine prosper — the vine that abandoned the one who planted it? No. Its roots will be pulled up. Its fruit stripped off. Every fresh new shoot will wither down to nothing. And it will not even take much force to destroy it — Zedekiah's treachery has made him easy to uproot."
    },
    "10": {
      "L": "Yea, behold, being planted, shall it prosper? Shall it not utterly wither when the east wind toucheth it? It shall wither in the furrows where it grew.",
      "M": "Behold, though it is planted, will it prosper? Will it not utterly wither when the east wind strikes it? It will wither in the very furrows where it grew.",
      "T": "Even planted in good soil — will it live? No. One touch of the east wind and it withers completely. The east wind is Babylon, Nebuchadnezzar's campaign sweeping in from the east. The vine will wither right there in the soil that was supposed to sustain it."
    },
    "11": {
      "L": "Moreover the word of the LORD came unto me, saying:",
      "M": "The word of the LORD came to me again:",
      "T": "Yahweh's word came to me again:"
    },
    "12": {
      "L": "Say now to the rebellious house: Know ye not what these things mean? Tell them: Behold, the king of Babylon is come to Jerusalem, and hath taken the king thereof, and the princes thereof, and led them with him to Babylon.",
      "M": "Say to the rebellious house: Do you not understand what these things mean? Tell them: The king of Babylon came to Jerusalem and took its king and its officials and brought them with him to Babylon.",
      "T": "Say to the rebellious house — and call them what they are: do you not understand this allegory? Let me be plain. Nebuchadnezzar came to Jerusalem. He took the king — Jehoiachin — and his officials, and brought them all to Babylon. That is the first eagle seizing the topmost branch."
    },
    "13": {
      "L": "And hath taken of the king's seed, and made a covenant with him, and hath taken an oath of him; he hath also taken the mighty of the land.",
      "M": "He took one from the royal seed and made a covenant with him, binding him under oath; he also took away the leading men of the land.",
      "T": "He then selected someone from the royal line — Zedekiah — installed him as king, and bound him by covenant and sworn oath to Babylon. And he removed the powerful men of the land, leaving only the most manageable."
    },
    "14": {
      "L": "That the kingdom might be base, that it might not lift itself up, but that by keeping his covenant it might stand.",
      "M": "This was to keep the kingdom low, unable to rise — but it would stand by keeping its covenant with Babylon.",
      "T": "The arrangement was designed to keep Judah politically submissive — unable to assert independence — sustained only by faithfully honoring the treaty. Dependence was the condition of survival."
    },
    "15": {
      "L": "But he rebelled against him in sending his ambassadors into Egypt, that they might give him horses and much people. Shall he prosper? Shall he escape that doeth such things? Or shall he break the covenant, and be delivered?",
      "M": "But he rebelled against Nebuchadnezzar by sending ambassadors to Egypt to obtain horses and a large army. Will he succeed? Can someone who does such things escape? Can he break a covenant and still be delivered?",
      "T": "And he rebelled. He sent messengers to Egypt — seeking horses, troops, a military alliance to break free from Babylon. Will it work? Can someone who shatters a solemn oath escape the consequences? Can he break the covenant and still be saved? The questions are rhetorical."
    },
    "16": {
      "L": "As I live, saith the Lord GOD, surely in the place where the king dwelleth that made him king, whose oath he despised and whose covenant he brake, even with him in the midst of Babylon he shall die.",
      "M": "As I live, declares the Lord GOD: In the place of the king who made him king — in Babylon itself — whose oath he despised and whose covenant he broke, there he will die.",
      "T": "By my own life — the Lord Yahweh swears it — Zedekiah will die in Babylon, in the very court of the king who installed him, whose oath he treated as worthless and whose covenant he tore apart. He sought Egypt's protection; he will meet Babylon's judgment."
    },
    "17": {
      "L": "Neither shall Pharaoh with his mighty army and great company make for him in the war, by casting up mounts and building forts, to cut off many persons.",
      "M": "Pharaoh will not help him in the war with his mighty army and great company when siege mounds are cast up and siege works are built to cut off many lives.",
      "T": "Pharaoh will not come through. When Babylon builds its siege ramps and towers around Jerusalem — when the trap fully closes — Egypt will not appear with its great army to rescue Zedekiah. Egypt's alliance was a mirage. Jerusalem will face the siege alone."
    },
    "18": {
      "L": "Seeing he despised the oath by breaking the covenant, when lo he had given his hand, and hath done all these things, he shall not escape.",
      "M": "Because he despised the oath by breaking the covenant — though he had pledged his hand — and did all these things, he will not escape.",
      "T": "He pledged his hand — a formal, physical act of covenant ratification — and then despised that oath by breaking the covenant. The deliberateness is the indictment: he chose to break what he had publicly sworn. He will not escape."
    },
    "19": {
      "L": "Therefore thus saith the Lord GOD: As I live, surely mine oath that he hath despised, and my covenant that he hath broken, even it will I recompense upon his own head.",
      "M": "Therefore thus says the Lord GOD: As I live, I will bring his despising of my oath and his breaking of my covenant back upon his own head.",
      "T": "The Lord Yahweh says — by my life — this covenant was not merely Nebuchadnezzar's. When Israel's king swears in my name and then despises the oath, he has broken my covenant. And I will return the full weight of that treachery upon his own head."
    },
    "20": {
      "L": "And I will spread my net upon him, and he shall be taken in my snare; and I will bring him to Babylon, and will plead with him there for his trespass that he hath trespassed against me.",
      "M": "I will spread my net over him and he will be caught in my snare; I will bring him to Babylon and contend with him there for the faithlessness he committed against me.",
      "T": "I will cast my net over him — he will walk directly into my snare. I will bring him to Babylon, and there I will deal with him directly for the faithlessness he showed me. The judgment is mine to execute, not merely Nebuchadnezzar's."
    },
    "21": {
      "L": "And all his fugitives with all his bands shall fall by the sword, and they that remain shall be scattered toward all winds; and ye shall know that I the LORD have spoken it.",
      "M": "All his fugitives with all his troops will fall by the sword, and those who survive will be scattered in every direction — and you will know that I the LORD have spoken.",
      "T": "His elite troops, his entire military force — all will fall to the sword. Whatever remains of his army will be scattered to the four winds. And this is how you will know that I, Yahweh, have spoken: it will happen exactly as declared."
    },
    "22": {
      "L": "Thus saith the Lord GOD: I will also take of the highest branch of the high cedar, and will set it; I will crop off from the top of his young twigs a tender one, and will plant it upon an high mountain and eminent.",
      "M": "Thus says the Lord GOD: I myself will take a shoot from the topmost branch of the high cedar and plant it; I will crop off from its crown a tender young twig and plant it on a high and lofty mountain.",
      "T": "The Lord Yahweh says: Now I will act as the eagle. The first eagle took the topmost branch for Babylon's purposes; now I take a tender young shoot from the crown of the high cedar — and I will plant it myself, on a high and prominent mountain. Not Babylon. Not Egypt. Israel's own height."
    },
    "23": {
      "L": "In the mountain of the height of Israel will I plant it; and it shall bring forth boughs, and bear fruit, and be a goodly cedar: and under it shall dwell all fowl of every wing; in the shadow of the branches thereof shall they dwell.",
      "M": "On the mountain height of Israel I will plant it; it will produce branches and bear fruit and become a noble cedar — and under it every kind of bird will live; in the shadow of its branches they will nest.",
      "T": "On Israel's mountain heights — that is where I plant it. And this cedar will not be the weak, dependent vine of Zedekiah. It will grow into a noble cedar, producing branches and bearing fruit, and every kind of bird will make its home in its shade. All peoples will find rest under it. The kingdom God himself establishes is the opposite of every human kingdom that fell."
    },
    "24": {
      "L": "And all the trees of the field shall know that I the LORD have brought down the high tree, have exalted the low tree, have dried up the green tree, and have made the dry tree to flourish. I the LORD have spoken and have done it.",
      "M": "And all the trees of the field will know that I the LORD bring down the high tree, exalt the low tree, dry out the green tree, and make the dry tree flourish. I the LORD have spoken, and I will do it.",
      "T": "Every tree of the field will know — every power and every kingdom that watches — that I am Yahweh: the one who brings down what stands tall in human strength and lifts up what has been brought low; who withers what appears to flourish and causes the withered to bloom. This is my sovereign pattern, my signature in history. I have spoken it. I will bring it to pass."
    }
  },
  "18": {
    "1": {
      "L": "The word of the LORD came unto me again, saying:",
      "M": "The word of the LORD came to me:",
      "T": "Yahweh's word came to me:"
    },
    "2": {
      "L": "What mean ye, that ye use this proverb concerning the land of Israel, saying: The fathers have eaten sour grapes, and the children's teeth are set on edge?",
      "M": "What do you mean by using this proverb about the land of Israel: 'The fathers have eaten sour grapes, and the children's teeth are set on edge'?",
      "T": "What are you doing by repeating this proverb across the land of Israel? 'The fathers ate sour grapes — and the children's teeth are on edge.' This is a proverb of excuse: we suffer for what our ancestors did, not for anything we ourselves have done."
    },
    "3": {
      "L": "As I live, saith the Lord GOD, ye shall not have occasion any more to use this proverb in Israel.",
      "M": "As I live, declares the Lord GOD, you shall have no more occasion to use this proverb in Israel.",
      "T": "The Lord Yahweh says — by my own life — this proverb ends now. You will not go on repeating it in Israel."
    },
    "4": {
      "L": "Behold, all souls are mine; as the soul of the father, so also the soul of the son is mine: the soul that sinneth, it shall die.",
      "M": "Behold, every person belongs to me — the parent and the child alike: the person who sins is the one who will die.",
      "T": "Here is the foundation: every living person belongs to me. Father and son, parent and child — all lives are mine. The person who sins — that specific person, and not another — is the one who dies for it."
    },
    "5": {
      "L": "But if a man be just, and do that which is lawful and right —",
      "M": "But if a man is just and does what is lawful and right —",
      "T": "Consider a man who is just — who actually does what is right and lawful."
    },
    "6": {
      "L": "And hath not eaten upon the mountains, neither hath lifted up his eyes to the idols of the house of Israel, neither hath defiled his neighbour's wife, neither hath come near to a menstruous woman,",
      "M": "He has not eaten at the mountain shrines or lifted his eyes to the idols of the house of Israel; he has not defiled his neighbor's wife or approached a woman during her period of uncleanness —",
      "T": "He has not worshipped at the mountain altars; he has not turned his heart toward Israel's idols. He has not violated his neighbor's wife or approached a woman in her time of ritual impurity."
    },
    "7": {
      "L": "And hath not oppressed any, but hath restored to the debtor his pledge, hath spoiled none by violence, hath given his bread to the hungry, and hath covered the naked with a garment —",
      "M": "He has not oppressed anyone; he has returned a debtor's pledge; he has not robbed by violence; he has given his food to the hungry and covered the naked with a garment —",
      "T": "He has not ground down the vulnerable. He returns what he held as security when the debtor needs it back. He does not steal by force. He shares his food with the hungry and gives clothing to those who have none."
    },
    "8": {
      "L": "He that hath not given forth upon usury, neither hath taken any increase, that hath withdrawn his hand from iniquity, hath executed true judgment between man and man —",
      "M": "He has not lent money at interest or taken profit from a loan; he has held back from wrongdoing and rendered honest judgment between one person and another —",
      "T": "He does not lend at interest or charge profit on loans — he understands that exploiting need is itself a form of theft. He keeps his hands clear of every form of wrongdoing and gives impartial, honest judgment when disputes come before him."
    },
    "9": {
      "L": "Hath walked in my statutes, and hath kept my judgments, to deal truly — he is just, he shall surely live, saith the Lord GOD.",
      "M": "He has walked in my statutes and kept my ordinances faithfully — he is just; he shall surely live, declares the Lord GOD.",
      "T": "He walks by my statutes. He keeps my ordinances with genuine commitment. He is righteous. He will live — certainly, without question. The Lord Yahweh declares it."
    },
    "10": {
      "L": "If he beget a son that is a robber, a shedder of blood, and that doeth the like to any one of these things —",
      "M": "But if that man has a son who is violent, a murderer, who does any of these things —",
      "T": "But suppose that just man has a son who is a robber and a killer — who does all the things his father refused to do."
    },
    "11": {
      "L": "And that doeth not any of those duties, but even hath eaten upon the mountains, and defiled his neighbour's wife —",
      "M": "Who does none of those righteous things but instead eats at mountain shrines and defiles his neighbor's wife —",
      "T": "He does nothing of his father's righteousness. He worships at the mountain altars. He violates his neighbor's wife."
    },
    "12": {
      "L": "Hath oppressed the poor and needy, hath spoiled by violence, hath not restored the pledge, and hath lifted up his eyes to the idols, hath committed abomination —",
      "M": "He has oppressed the poor and needy, robbed by violence, not restored the pledge, lifted his eyes to idols, and committed abomination —",
      "T": "He crushes the poor and helpless. He robs by force. He keeps the pledged item instead of returning it. He gives his heart over to idols. He does what is utterly detestable."
    },
    "13": {
      "L": "Hath given forth upon usury, and hath taken increase: shall he then live? He shall not live. He hath done all these abominations; he shall surely die; his blood shall be upon him.",
      "M": "He has lent at interest and taken profit. Shall he live? He shall not live. He has committed all these abominations; he shall surely die; his blood is upon his own head.",
      "T": "He lends at interest and takes profit from loans. Will he live? He will not live. He has done all these abominable things — he will die, and that death rests on his own head alone."
    },
    "14": {
      "L": "Now lo, if he beget a son, that seeth all his father's sins which he hath done, and considereth, and doeth not such like —",
      "M": "But if he in turn has a son who sees all the sins his father committed, considers them, and does not do the same —",
      "T": "But what if that wicked man has a son — a son who watches his father's life, sees all those sins clearly, takes them to heart, and chooses not to live that way?"
    },
    "15": {
      "L": "That hath not eaten upon the mountains, neither hath lifted up his eyes to the idols of the house of Israel, hath not defiled his neighbour's wife —",
      "M": "He has not eaten at the mountain shrines or lifted his eyes to the idols of the house of Israel; he has not defiled his neighbor's wife —",
      "T": "He has not worshipped at mountain altars. He has not given his heart to Israel's idols. He has not violated his neighbor's wife."
    },
    "16": {
      "L": "Neither hath oppressed any, hath not withholden the pledge, neither hath spoiled by violence, but hath given his bread to the hungry, and hath covered the naked with a garment —",
      "M": "He has not oppressed anyone; he has not withheld the pledge; he has not robbed by violence; he has given his food to the hungry and covered the naked with clothing —",
      "T": "He does not oppress. He does not withhold what should be returned. He does not steal by force. He feeds the hungry and clothes those who have nothing."
    },
    "17": {
      "L": "That hath taken off his hand from the poor, that hath not received usury nor increase, hath executed my judgments, hath walked in my statutes — he shall not die for the iniquity of his father; he shall surely live.",
      "M": "He has held back from wronging the poor, has not taken interest or profit, has carried out my ordinances and walked in my statutes — he shall not die for his father's iniquity; he shall surely live.",
      "T": "He keeps his hands off the poor. He charges no interest, takes no profit. He upholds my ordinances and walks in my statutes. He will not die for his father's iniquity — he will live. His father's choices do not determine his fate."
    },
    "18": {
      "L": "As for his father, because he cruelly oppressed, spoiled his brother by violence, and did that which is not good among his people, behold, even he shall die in his iniquity.",
      "M": "As for his father — because he practiced cruel oppression, robbed his brother by violence, and did what was not good among his people — he will die in his iniquity.",
      "T": "The father — who crushed people with his cruelty, who robbed his own kinsmen, who contributed nothing good to his community — he dies in his own iniquity. His. Not his son's."
    },
    "19": {
      "L": "Yet say ye: Why doth not the son bear the iniquity of the father? When the son hath done that which is lawful and right, and hath kept all my statutes, and hath done them, he shall surely live.",
      "M": "Yet you say: Why does the son not bear the iniquity of the father? When the son has done what is lawful and right and kept all my statutes, he shall surely live.",
      "T": "But you say: Why doesn't the son carry his father's guilt? Here is the answer: when a son has done what is right and lawful — when he has kept all my statutes faithfully — he will live. His own conduct determines his outcome, not his lineage."
    },
    "20": {
      "L": "The soul that sinneth, it shall die. The son shall not bear the iniquity of the father, neither shall the father bear the iniquity of the son: the righteousness of the righteous shall be upon him, and the wickedness of the wicked shall be upon him.",
      "M": "The person who sins is the one who will die. The son will not bear the iniquity of the father, nor will the father bear the iniquity of the son. The righteousness of the righteous person belongs to him, and the wickedness of the wicked person falls on him.",
      "T": "The person who sins — that person dies. Not their child. Not their parent. The son does not carry the father's guilt; the father does not carry the son's. The righteous person's righteousness is credited to them; the wicked person's wickedness falls on them. Every account stands on its own."
    },
    "21": {
      "L": "But if the wicked will turn from all his sins that he hath committed, and keep all my statutes, and do that which is lawful and right, he shall surely live; he shall not die.",
      "M": "But if the wicked man turns from all his sins that he has committed, keeps all my statutes, and does what is lawful and right, he will surely live; he will not die.",
      "T": "But if the wicked person turns — genuinely turns, away from every sin they have committed — and keeps my statutes and does what is right, they will live. They will not die. The past does not imprison them."
    },
    "22": {
      "L": "All his transgressions that he hath committed, they shall not be mentioned unto him: in his righteousness that he hath done he shall live.",
      "M": "All the transgressions he has committed will not be held against him; in the righteousness he now practices he will live.",
      "T": "All those transgressions — the full record of what he did — will not be mentioned against him. In the righteousness he now actually lives by, he will live. The turn is complete. The record is closed."
    },
    "23": {
      "L": "Have I any pleasure at all that the wicked should die? saith the Lord GOD: and not that he should return from his ways, and live?",
      "M": "Do I have any pleasure in the death of the wicked? declares the Lord GOD. Is it not rather that he should turn from his ways and live?",
      "T": "Does the Lord Yahweh take pleasure in the death of the wicked? The answer is no. What I want is that the wicked person would turn from their path and live. Judgment is not my goal. Life is."
    },
    "24": {
      "L": "But when the righteous turneth away from his righteousness, and committeth iniquity, and doeth according to all the abominations that the wicked man doeth, shall he live? All his righteousness that he hath done shall not be mentioned: in his trespass that he hath trespassed, and in his sin that he hath sinned, in them shall he die.",
      "M": "But when a righteous person turns from their righteousness and commits iniquity — doing all the abominations of the wicked — shall they live? None of their righteousness will be remembered. In the faithlessness they committed and the sin they chose, they will die.",
      "T": "But what if the righteous person turns away from their righteousness and descends into wickedness — committing every abomination that characterizes the wicked? Will past righteousness protect them? No. It will not even be remembered. In the faithlessness they chose, in the sin they committed, they will die. Righteousness is not a credit balance that offsets future evil."
    },
    "25": {
      "L": "Yet ye say: The way of the Lord is not equal. Hear now, O house of Israel: Is not my way equal? are not your ways unequal?",
      "M": "Yet you say: 'The way of the Lord is not fair.' Hear, O house of Israel: Are my ways not fair? Are not your ways the ones that are unfair?",
      "T": "And still you say: Yahweh's way is not fair. Hear me, house of Israel: Is it my way that is unjust? Or is it your ways? You expect ancestral guilt to be inherited and ancestral righteousness to be a shield for the unrighteous. I hold each person accountable for their own choices. Which is fairer?"
    },
    "26": {
      "L": "When a righteous man turneth away from his righteousness, and committeth iniquity, and dieth in them; for his iniquity that he hath done shall he die.",
      "M": "When a righteous person turns from their righteousness and commits iniquity, they will die in it; for the iniquity they committed they will die.",
      "T": "When a righteous person turns away from their righteousness into wickedness and dies in that wickedness — they die for the iniquity they chose. Their prior righteousness does not override that choice."
    },
    "27": {
      "L": "Again, when the wicked man turneth away from his wickedness that he hath committed, and doeth that which is lawful and right, he shall save his soul alive.",
      "M": "Again, when a wicked person turns from the wickedness they committed and does what is lawful and right, they will save their own life.",
      "T": "And again: when the wicked person turns away from the wickedness they have been living in and begins to do what is right — that person saves their own life."
    },
    "28": {
      "L": "Because he considereth, and turneth away from all his transgressions that he hath committed, he shall surely live; he shall not die.",
      "M": "Because he has considered his ways and turned from all the transgressions he committed, he will surely live; he will not die.",
      "T": "Because he stopped. He took stock of what he was doing — saw it clearly for what it was — and turned away from all of it. He will live. He will not die. Repentance is real, and it works."
    },
    "29": {
      "L": "Yet saith the house of Israel: The way of the Lord is not equal. O house of Israel, are not my ways equal? are not your ways unequal?",
      "M": "Yet the house of Israel says: 'The way of the Lord is not fair.' O house of Israel, are my ways not fair? Are not your ways the ones that are unfair?",
      "T": "But the house of Israel keeps saying: Yahweh's way is not fair. House of Israel — are my ways unjust? Or are your ways? You want each person to bear the weight of their ancestors' choices but escape the weight of their own. I give every person exactly what their own life has chosen."
    },
    "30": {
      "L": "Therefore I will judge you, O house of Israel, every one according to his ways, saith the Lord GOD. Repent and turn yourselves from all your transgressions; so iniquity shall not be your ruin.",
      "M": "Therefore I will judge you, O house of Israel, each one according to their own ways, declares the Lord GOD. Repent and turn from all your transgressions, so that iniquity will not be your downfall.",
      "T": "Therefore I will judge you, house of Israel — each person according to their own ways. The Lord Yahweh declares it. So turn. Repent. Turn from every act of rebellion. Do not let your iniquity be the thing that destroys you."
    },
    "31": {
      "L": "Cast away from you all your transgressions whereby ye have transgressed; and make you a new heart and a new spirit: for why will ye die, O house of Israel?",
      "M": "Cast away from you all the transgressions by which you have rebelled, and make yourselves a new heart and a new spirit — for why should you die, O house of Israel?",
      "T": "Throw off every act of rebellion you have committed. Get yourselves a new heart and a new spirit — not just changed behavior but a transformed inner life. Why should you die, house of Israel? This is not what I want for you. Note: here God commands what he will later promise to give (36:26). The command is already mercy — he would not command what is impossible."
    },
    "32": {
      "L": "For I have no pleasure in the death of him that dieth, saith the Lord GOD: wherefore turn yourselves, and live ye.",
      "M": "For I have no pleasure in the death of anyone who dies, declares the Lord GOD. Therefore turn and live!",
      "T": "I take no pleasure in the death of anyone. The Lord Yahweh says it plainly and finally. So turn — turn back to me — and live."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'ezekiel')
        merge_tier(existing, EZEKIEL, tier_key)
        save(tier_dir, 'ezekiel', existing)
    print('Ezekiel 17–18 written.')

if __name__ == '__main__':
    main()
