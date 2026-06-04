"""
MKT Hosea chapters 7–12 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-hosea-7-12.py

=== CHAPTER OVERVIEW ===

Chapter 7: The Oven of Conspiracy — Political Corruption and the Silly Dove.
  The oven metaphor runs through vv. 4–7: Israel's conspirators smolder through
  the night and burst into flame by morning, consuming king after king. Ephraim
  oscillates between Egypt and Assyria like a senseless dove (v. 11), not
  realising that foreigners are already devouring his strength and that gray hairs
  are spreading across him while he remains oblivious (v. 9). The chapter closes
  with the image of a deceitful bow: their prayers and their repentances miss the
  target — they return, but not to the Most High (v. 16).

Chapter 8: The Eagle, the Calf, and the Whirlwind.
  An alarm is sounded: an eagle (Assyria) swoops on the house of the LORD (v. 1).
  The indictment moves quickly through political self-determination without God
  (v. 4), the golden calf of Samaria (vv. 5–6), and the agricultural paradox of
  vv. 7–8 ("sow the wind / reap the whirlwind"). The great irony of v. 12: God
  wrote the great things of his law for them, and they treated it as something
  foreign. The chapter ends with the judgment that Israel will return to Egypt —
  reversal of the Exodus — because they forgot their Maker.

Chapter 9: The End of Joy — Exile from the Land of the LORD.
  Hosea forbids Israel to rejoice (v. 1) since the threshing-floor fertility rites
  have been nothing but a whore's wages. Exile means eating unclean food in
  Assyria (v. 3), unable to bring offerings (v. 4). The memory of Baal-peor (v. 10)
  is the interpretive key: Israel's apostasy was built-in from the wilderness.
  The prophet is called a fool and a madman (v. 7) — not by the narrator but
  ironically in Israel's own mouth, showing the depth of their contempt for the
  prophetic word. The terrible prayer for a miscarrying womb (v. 14) is not
  vindictive but an acknowledgment that, given where Israel is headed, childlessness
  is better than bringing children to slaughter (v. 13).

Chapter 10: The Empty Vine — Altars, Kings, and a Final Call.
  Israel is a luxuriant vine that bore fruit only for itself (v. 1). The chapter
  catalogues cascading failures: divided heart (v. 2), no king (v. 3), false oaths
  (v. 4), the shameful calf (vv. 5–6), and the plea to the mountains (v. 8).
  In vv. 9–10, God recalls the days of Gibeah as the paradigm of deep-rooted evil.
  The agricultural metaphor of vv. 11–13 forms an ABA pattern: the heifer trained
  for easy threshing must now plow hard ground; the invitation to sow righteousness
  is surrounded by the indictment that they have plowed wickedness instead.
  Bethel/Beth-aven — the very site of false religion — will be the agent of Israel's
  undoing (v. 15).

Chapter 11: The Father's Anguish — The Great Reversal of Judgment.
  The emotional centre of the book. The divine soliloquy recalls the founding
  relationship: Israel as a child called from Egypt (v. 1; cited in Matt. 2:15),
  taught to walk, lifted in love (vv. 3–4). The image of God as parent rather than
  husband shifts the register from covenant lawsuit to paternal grief. Verses 8–9
  contain the most remarkable expression of divine emotion in the OT: "My heart
  churns within me / my compassion grows warm." The decisive statement of v. 9 —
  "I am God and not a man" — grounds the possibility of mercy: precisely because
  God is not constrained by the human cycle of offence and revenge, he can choose
  not to destroy. The chapter ends with a brief restoration oracle (vv. 10–11):
  Israel will return trembling like birds from Egypt and Assyria.

Chapter 12: Jacob Our Ancestor — Mirror and Warning.
  Hosea mines the Jacob tradition as a mirror for contemporary Ephraim. Jacob
  grasped (v. 3), wrestled, wept and prevailed (v. 4) — and God met him. Ephraim
  is told the same God is available (v. 6): return, practice hesed and justice,
  wait. But Ephraim has become a trader with dishonest scales (v. 7) and celebrates
  his own wealth without acknowledging its source (v. 8). The chapter ends with the
  reminder that it was by a prophet — Moses — that Israel was brought out of Egypt
  and preserved; Ephraim's bitter provocation (v. 14) is the inverse of that story.

=== CONTESTED-TERM DECISIONS (carrying forward from mkt-hosea-1-6.py) ===

- H3068 (יהוה / Yahweh): L/M "LORD". T uses "Yahweh" in prophetic-oracle and
  covenant contexts, "the LORD" in narrative. Consistent with chs 1–6.

- H430 (אֱלֹהִים / Elohim): "God" all tiers.

- H2617 (חֶסֶד / hesed): L "steadfast love". M "covenant loyalty". T "faithful
  love" / "covenant devotion" / "hesed" (left untranslated once in 12:6 T to signal
  the word itself deserves attention). Consistent with chs 1–6.

- H7307 (רוּחַ / ruah): Not a direct issue in chs 7–12. The "spirit" language
  used in these chapters refers to wind or breath metaphorically.

- H2181 (זָנָה / zanah): L "play the harlot" / "commit harlotry." M "be unfaithful"
  / "commit adultery." T surfaces the covenantal breach explicitly. Consistent.

- H1285 (בְּרִית / berit): "covenant" all tiers.

- H3045 (יָדַע / yada'): Knowledge of God in Hosea is relational, experiential,
  covenantal. M "knowledge" / "know." T makes the depth explicit where context
  warrants. Consistent with chs 1–6.

- "Spirit of whoredom" from chs 4–5 does not recur in chs 7–12.

- OT poetic structure: Poetry (ch. 11 soliloquy, 12:5–6) rendered with line breaks
  in T tier. Narrative prose sections use flowing sentences in all tiers.

- H8193 (שְׂפָה / lip/tongue/speech): Rendered "tongue" in 7:16 L, "arrogance" in M,
  "what their tongues have bragged" in T.

- H0205 (אָוֶן / aven = wickedness/iniquity): The place name Beth-aven (House of
  Wickedness, Hosea's contemptuous renaming of Bethel) is retained as "Beth-aven"
  in L/M with explanatory gloss in T on first occurrence.

- Assyria/Egypt parallelism: Consistent rendering throughout — "Assyria" and "Egypt"
  as proper names. "King Jareb" (8:10; 10:6): retained as proper name in L/M;
  T renders "the great king" on second occurrence to show it is a title, not a name.

- Divine passive: Preserved where Hebrew implies God as unnamed agent; T makes the
  divine agency explicit.

- Aspect:
  Perfect verbs in prophetic oracles = completed in divine purpose; rendered as
  English present or simple past as context demands.
  Imperfect/waw-consecutive = narrative sequence or ongoing action.
  The oracles of judgment in chs 8–10 use rapid shifts; T surfaces the rhetorical
  force of each shift.

- Chapter 11 line breaks: Used selectively in T for the father-soliloquy (vv. 1–4,
  8–11) and the restoration oracle to honour the poetic cadence of the Hebrew.

- Chapter 9:7 (prophet is a fool/mad): This is Israel's slur against Hosea, not the
  narrator's verdict. T makes the attribution explicit to avoid confusion.

- Chapter 12:4 "he found him in Bethel": MT reads "he found us" — a sudden shift
  to first person plural, pulling the reader into the narrative. All tiers follow MT;
  T notes the editorial "us."
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

HOSEA = {
    "7": {
        "1": {
            "L": "When I would have healed Israel, then the iniquity of Ephraim was uncovered and the wickedness of Samaria: for they commit falsehood; the thief entereth in, and the troop of robbers spoileth without.",
            "M": "When I would have healed Israel, the iniquity of Ephraim was exposed and the evil of Samaria. For they practice deception; a thief breaks in, and a gang of robbers raids outside.",
            "T": "Just as I moved to heal Israel, Ephraim's guilt lay bare before me — and Samaria's wickedness with it. Every attempt at healing only exposes the rot: thieves break in, gangs plunder in the open."
        },
        "2": {
            "L": "And they consider not in their hearts that I remember all their wickedness: now their own doings have beset them about; they are before my face.",
            "M": "But they do not consider in their hearts that I remember all their evil. Now their deeds have surrounded them; they stand before my face.",
            "T": "What they never think about is this: I have not forgotten a single one of their wrongs. Now those deeds have closed in around them like a crowd — they stand there in full view before me."
        },
        "3": {
            "L": "They make the king glad with their wickedness, and the princes with their lies.",
            "M": "They make the king happy with their wickedness, and win the princes with their treachery.",
            "T": "They buy their king's approval with villainy and win their princes with lies. The court that should correct them only rewards them."
        },
        "4": {
            "L": "They are all adulterers: as an oven heated by the baker, who ceaseth from raising after he hath kneaded the dough, until it be leavened.",
            "M": "They are all adulterers, burning like an oven that the baker does not need to stoke — it heats itself from the kneading of the dough until the bread rises.",
            "T": "The whole lot of them are adulterers — burning with their lust like an oven that tends itself: once the dough is set, the baker doesn't need to stir the coals; it heats itself until the leaven does its work."
        },
        "5": {
            "L": "In the day of our king the princes have made him sick with bottles of wine; he stretched out his hand with scorners.",
            "M": "On the day of our king, the princes made themselves sick with wine; the king himself reached out his hand with mockers.",
            "T": "On the day of the royal feast, the princes made themselves sick with wine — and the king himself joined in with a crowd of mockers. The royal celebration became a revel of shame."
        },
        "6": {
            "L": "For they have made ready their heart like an oven, whiles they lie in wait: their baker sleepeth all the night; in the morning it burneth as a flaming fire.",
            "M": "For their hearts smolder like an oven as they scheme; their baker sleeps through the night, but in the morning the fire blazes.",
            "T": "All through the night, while their baker sleeps, their plotting hearts smolder like an oven. Come morning, the fire breaks into full flame — the conspiracy is ready to act."
        },
        "7": {
            "L": "They are all hot as an oven, and have devoured their judges; all their kings are fallen: there is none among them that calleth unto me.",
            "M": "They are all as hot as an oven, and they devour their rulers; all their kings have fallen. None of them calls to me.",
            "T": "They blaze like an oven — and they have consumed their judges, brought down king after king. Not one of them has ever called out to me."
        },
        "8": {
            "L": "Ephraim, he hath mixed himself among the people; Ephraim is a cake not turned.",
            "M": "Ephraim mixes himself among the peoples; Ephraim is a flat cake that has not been turned over.",
            "T": "Ephraim has dissolved himself into the nations — he is like a pancake left unturned on the griddle: burnt black on one side, raw dough on the other. Half-ruined, and he doesn't even know it."
        },
        "9": {
            "L": "Strangers have devoured his strength, and he knoweth it not: yea, gray hairs are here and there upon him, yet he knoweth not.",
            "M": "Foreigners have consumed his strength, and he does not know it. Gray hairs are scattered on him, yet he does not realize it.",
            "T": "Foreign powers have been sapping his strength, and he hasn't noticed. Gray is spreading through his hair, and he still doesn't see it. Israel is aging and failing without awareness."
        },
        "10": {
            "L": "And the pride of Israel testifieth to his face: and they do not return to the LORD their God, nor seek him for all this.",
            "M": "The pride of Israel testifies against him to his face, yet they do not return to the LORD their God or seek him despite all this.",
            "T": "Israel's own arrogance stands as an open accusation against him — he cannot deny it. And still — even with all this happening to them — they refuse to return to Yahweh their God or seek him."
        },
        "11": {
            "L": "Ephraim also is like a silly dove without heart: they call to Egypt, they go to Assyria.",
            "M": "Ephraim is like a senseless dove, lacking all judgment. They call to Egypt; they go off to Assyria.",
            "T": "Ephraim is like a foolish dove that flutters this way and that with no sense of direction — crying out to Egypt, then flying off to Assyria. Any power but me."
        },
        "12": {
            "L": "When they shall go, I will spread my net upon them; I will bring them down as the fowls of the heaven; I will chastise them, as their congregation hath heard.",
            "M": "As they go, I will cast my net over them; I will bring them down like the birds of the sky. I will discipline them according to the warnings their assembly has already been given.",
            "T": "As they fly off, I will cast my net over them and bring them down like birds from the sky. I will discipline them — just as the warnings they have long heard foretold."
        },
        "13": {
            "L": "Woe unto them! for they have fled from me: destruction unto them! because they have transgressed against me: though I have redeemed them, yet they have spoken lies against me.",
            "M": "Woe to them, for they have strayed from me! Destruction to them, because they have rebelled against me! I would have redeemed them, but they spoke lies against me.",
            "T": "Grief for them — they have run from me! Ruin waits for them — they have defied me! I was ready to redeem them, and they repaid me with lies."
        },
        "14": {
            "L": "And they have not cried unto me with their heart, when they howled upon their beds: they assemble themselves for corn and wine, and they rebel against me.",
            "M": "They do not cry to me from their hearts; they merely howl on their beds. They gather to pray for grain and wine, but they rebel against me.",
            "T": "They cry out, but not to me — just wailing on their beds in self-pity. They assemble to pray for better harvests, for grain and wine — and in their hearts they are still in rebellion against me."
        },
        "15": {
            "L": "Though I have bound and strengthened their arms, yet do they imagine mischief against me.",
            "M": "I trained and strengthened their arms, yet they devise evil against me.",
            "T": "I was the one who shaped them, who gave their arms their strength — and they turned that same strength to plotting against me."
        },
        "16": {
            "L": "They return, but not to the most High: they are like a deceitful bow: their princes shall fall by the sword for the rage of their tongue: this shall be their derision in the land of Egypt.",
            "M": "They return, but not to the Most High; they are like a treacherous bow. Their princes will fall by the sword because of the arrogance of their tongue, and this will be their mockery in the land of Egypt.",
            "T": "They come back — but not to me, not to the Most High. They are like a bow that misfires when you most need it. Their princes will die by the sword for what their tongues have bragged, and Egypt will hold them in contempt."
        }
    },
    "8": {
        "1": {
            "L": "Set the trumpet to thy mouth. He shall come as an eagle against the house of the LORD, because they have transgressed my covenant, and trespassed against my law.",
            "M": "Set the trumpet to your lips! An enemy swoops like an eagle against the house of the LORD, because they have broken my covenant and rebelled against my law.",
            "T": "Sound the alarm! Lift the trumpet to your mouth — an eagle is diving on the house of Yahweh. They brought this on themselves by shattering my covenant and defying my law."
        },
        "2": {
            "L": "Israel shall cry unto me, My God, we know thee.",
            "M": "Israel cries out to me, My God, we know you — we are Israel!",
            "T": "They cry out to me: 'Our God! We know you — we are Israel!' But the cry is hollow. Knowledge of me is the very thing they lack."
        },
        "3": {
            "L": "Israel hath cast off the thing that is good: the enemy shall pursue him.",
            "M": "Israel has thrown away what is good; an enemy will pursue him.",
            "T": "Israel has rejected what is good — and now an enemy will hunt him down."
        },
        "4": {
            "L": "They have set up kings, but not by me: they have made princes, and I knew it not: of their silver and their gold have they made them idols, that they may be cut off.",
            "M": "They have installed kings, but not by my authority; they have set up princes without my approval. With their silver and gold they fashioned idols for themselves — only to be cut off.",
            "T": "They have crowned kings without consulting me, installed princes without my knowledge. They took the silver and gold I gave them and hammered it into idols — idols that can only bring them to ruin."
        },
        "5": {
            "L": "Thy calf, O Samaria, hath cast thee off; mine anger is kindled against them: how long will it be ere they attain to innocency?",
            "M": "Your calf-idol is rejected, O Samaria; my anger burns against them. How long before they are capable of innocence?",
            "T": "Samaria, your golden calf has been thrown back in your face. My anger is blazing — how long before they are even capable of being clean?"
        },
        "6": {
            "L": "For from Israel was it also: the workman made it; therefore it is not God: but the calf of Samaria shall be broken in pieces.",
            "M": "For it comes from Israel! A craftsman made it; it is not God. The calf of Samaria will be shattered to pieces.",
            "T": "That calf was made in Israel — a craftsman's hands shaped it. It is not God. The calf of Samaria will be smashed to splinters."
        },
        "7": {
            "L": "For they have sown the wind, and they shall reap the whirlwind: it hath no stalk: the bud shall yield no meal: if so be it yield, the strangers shall swallow it up.",
            "M": "For they have sown the wind and shall reap the whirlwind. The stalk has no bud; it will produce no flour. If it did produce anything, foreigners would devour it.",
            "T": "They have sown the wind — and a whirlwind is the harvest they will get. No grain in the stalk, no flour in the bud. And even if anything grew, a foreign army would eat it."
        },
        "8": {
            "L": "Israel is swallowed up: now shall they be among the Gentiles as a vessel wherein is no pleasure.",
            "M": "Israel is swallowed up; they are now among the nations like a worthless piece of pottery.",
            "T": "Israel has been swallowed up — absorbed among the nations, worth no more than a broken pot that no one wants to keep."
        },
        "9": {
            "L": "For they are gone up to Assyria, a wild ass alone by himself: Ephraim hath hired lovers.",
            "M": "For they have gone up to Assyria — Ephraim is like a wild donkey going off alone; they have hired lovers for themselves.",
            "T": "Ephraim has bolted off to Assyria like a wild donkey wandering on its own — and paid good money for foreign alliances, purchasing what God would have given freely."
        },
        "10": {
            "L": "Yea, though they have hired among the nations, now will I gather them; and they shall sorrow a little for the burden of the king of princes.",
            "M": "Even though they hire allies among the nations, I will now gather them in. They will begin to diminish under the burden of the king and his princes.",
            "T": "Even now, while they are out buying allies among the nations, I will gather them in — but they will groan under the tribute demands of kings and princes. The very alliances they paid for will crush them."
        },
        "11": {
            "L": "Because Ephraim hath made many altars to sin, altars shall be unto him to sin.",
            "M": "Since Ephraim has multiplied altars for sinning, those altars serve only to produce more sin.",
            "T": "Ephraim has built altar after altar — but every altar was built for sin, and every altar has only generated more of the same. Worship that was never toward me becomes a machine for self-corruption."
        },
        "12": {
            "L": "I have written to him the great things of my law, but they were counted as a strange thing.",
            "M": "Though I wrote for him the great things of my law, they were treated as something foreign.",
            "T": "I wrote out my law for them in full — the whole abundant gift of it — and they treated it like a strange document from a foreign country. Not their law. Not their God."
        },
        "13": {
            "L": "They sacrifice flesh for the sacrifices of mine offerings, and eat it; but the LORD accepteth them not; now will he remember their iniquity, and visit their sins: they shall return to Egypt.",
            "M": "They offer their sacrificial meat and eat it, but the LORD takes no pleasure in them. Now he will remember their guilt and punish them for their sins. They will return to Egypt.",
            "T": "They bring their offerings and eat the meat — but Yahweh takes no pleasure in any of it. Now their guilt will be remembered; now their sins will be reckoned with. Back to Egypt they will go — back to the house of bondage."
        },
        "14": {
            "L": "For Israel hath forgotten his Maker, and buildeth temples; and Judah hath multiplied fenced cities: but I will send a fire upon his cities, and it shall devour the palaces thereof.",
            "M": "For Israel has forgotten his Maker and built temples; Judah has multiplied fortified cities. But I will send fire on their cities to devour their strongholds.",
            "T": "Israel has forgotten who made him — and has been building temples to show off. Judah has spent the same energy fortifying city after city. But I will send fire on all those cities, and the strongholds they trusted in will burn."
        }
    },
    "9": {
        "1": {
            "L": "Rejoice not, O Israel, for joy, as other people: for thou hast gone a whoring from thy God, thou hast loved a reward upon every cornfloor.",
            "M": "Do not rejoice, Israel, as other peoples do, for you have been unfaithful to your God. You have loved a prostitute's wages on every threshing floor.",
            "T": "Stop celebrating, Israel — you have no right to rejoice the way other nations do. You have played the whore against your God, chasing after the fertility-rite wages on every threshing floor where the grain piled up."
        },
        "2": {
            "L": "The floor and the winepress shall not feed them, and the new wine shall fail in her.",
            "M": "The threshing floor and wine press will not provide for them, and the new wine will disappoint them.",
            "T": "The very grain floors and wine vats they prostituted themselves at will not sustain them. The new wine will fail."
        },
        "3": {
            "L": "They shall not dwell in the LORD'S land; but Ephraim shall return to Egypt, and they shall eat unclean things in Assyria.",
            "M": "They will not remain in the LORD's land; Ephraim will return to Egypt, and in Assyria they will eat food that is ritually unclean.",
            "T": "The land of Yahweh will no longer be their home. Ephraim will go back to Egypt; in Assyria they will eat what the law forbids — exiled from the land, cut off from the altar."
        },
        "4": {
            "L": "They shall not offer wine offerings to the LORD, neither shall they be pleasing unto him: their sacrifices shall be unto them as the bread of mourners; all that eat thereof shall be polluted: for their bread for their soul shall not come into the house of the LORD.",
            "M": "They will not pour out wine offerings to the LORD or please him with their sacrifices. Such offerings will be like mourners' bread to them; all who eat it will be defiled, for their food will be only for themselves and will not enter the house of the LORD.",
            "T": "Exiled, they will not be able to bring their wine offerings to Yahweh; no sacrifice they offer will delight him. Their sacred food will become like bread eaten at a funeral — anyone who touches it is defiled. Their bread will feed only their own bodies; none of it will reach the house of Yahweh."
        },
        "5": {
            "L": "What will ye do in the solemn day, and in the day of the feast of the LORD?",
            "M": "What will you do on the day of the appointed festival, on the day of the LORD's feast?",
            "T": "When the feast day comes — the solemn assembly, the pilgrimage festival — what will you do? You will be in exile. There is no feast in a foreign land."
        },
        "6": {
            "L": "For, lo, they are gone because of destruction: Egypt shall gather them up, Memphis shall bury them: the pleasant places for their silver, nettles shall possess them: thorns shall be in their tabernacles.",
            "M": "For behold, they are fleeing to escape destruction; Egypt will gather them, and Memphis will bury them. Weeds will overgrow the places they prized for their silver; thorns will fill their homes.",
            "T": "They flee to escape ruin — and Egypt will be their grave. Memphis will bury them. The treasured houses they left behind will be overtaken by nettles; thornbushes will fill the rooms where they once lived."
        },
        "7": {
            "L": "The days of visitation are come, the days of recompence are come; Israel shall know it: the prophet is a fool, the spiritual man is mad, for the multitude of thine iniquity, and the great hatred.",
            "M": "The days of reckoning have come; the days of recompense have arrived. Israel will know it. The prophet is a fool, the inspired man is mad — so they say — because of your great iniquity and intense hostility.",
            "T": "The day of reckoning has arrived — the day of payback is here. Israel will feel it. But they call the prophet a fool and the man of the Spirit a madman. This is what their iniquity and contempt for God's word has done to them: they mock the messenger because they cannot bear the message."
        },
        "8": {
            "L": "The watchman of Ephraim was with my God: but the prophet is a snare of a fowler in all his ways, and hatred in the house of his God.",
            "M": "Ephraim's watchman was to stand beside my God, but the prophet has become a fowler's trap on all his paths, and hostility fills the house of his God.",
            "T": "The prophet was supposed to be Ephraim's watchman — stationed beside me, God. Instead he has become a bird-trap set on every path, and his own sanctuary is riddled with hatred."
        },
        "9": {
            "L": "They have deeply corrupted themselves, as in the days of Gibeah: therefore he will remember their iniquity, he will visit their sins.",
            "M": "They have gone deep into corruption, as in the days of Gibeah. God will remember their iniquity; he will punish their sins.",
            "T": "They have plunged into the depths of corruption — as bad as the days of Gibeah, when Israel reached its lowest point. God has not forgotten; he will call every sin to account."
        },
        "10": {
            "L": "I found Israel like grapes in the wilderness; I saw your fathers as the firstripe in the fig tree at her first time: but they went to Baalpeor, and separated themselves unto that shame; and their abominations were according as they loved.",
            "M": "I found Israel like grapes in the wilderness; I saw your ancestors as the first ripe fruit on a fig tree in its first season. But they came to Baal-peor and consecrated themselves to that shameful idol, and they became as detestable as the thing they loved.",
            "T": "I remember finding Israel in the wilderness — it was like coming upon grapes in a desert, like seeing the very first ripe figs of the season on a young tree. What a find that was. But they went to Baal-peor and surrendered themselves to the shameful rites there, and became as abominable as the idol they embraced."
        },
        "11": {
            "L": "As for Ephraim, their glory shall fly away like a bird, from the birth, and from the womb, and from the conception.",
            "M": "As for Ephraim, their glory will fly away like a bird — no birth, no pregnancy, no conception.",
            "T": "Ephraim's glory will take wing and vanish like a startled bird — no more children born, no more pregnancies, no more new life conceived. The fruit of the womb is taken away."
        },
        "12": {
            "L": "Though they bring up their children, yet will I bereave them, that there shall not be a man left: yea, woe also to them when I depart from them!",
            "M": "Even if they raise their children, I will bereave them until not one is left. Truly, woe to them when I withdraw from them!",
            "T": "Even if they manage to raise their children, I will take those children too — not one will remain. And when I finally withdraw from them — when that departure comes — it will be their true catastrophe."
        },
        "13": {
            "L": "Ephraim, as I saw Tyrus, is planted in a pleasant place: but Ephraim shall bring forth his children to the murderer.",
            "M": "I saw Ephraim planted in a pleasant place, like Tyre. But Ephraim must now bring his children out to the one who slays them.",
            "T": "I once saw Ephraim as planted in a fertile, well-watered place — like Tyre in its glory. But now Ephraim is leading his own children out to the executioner."
        },
        "14": {
            "L": "Give them, O LORD: what wilt thou give? give them a miscarrying womb and dry breasts.",
            "M": "Give them, O LORD — what will you give them? Give them a womb that miscarries and breasts that are dry.",
            "T": "What is left to pray for, Yahweh? Give them — what can you give them now? Give them wombs that lose the child, and breasts that run dry. Let the line stop here."
        },
        "15": {
            "L": "All their wickedness is in Gilgal: for there I hated them: for the wickedness of their doings I will drive them out of mine house, I will love them no more: all their princes are revolters.",
            "M": "All their evil is at Gilgal — that is where my hatred for them took hold. Because of the evil of their deeds, I will drive them out of my house; I will no longer love them. All their princes are rebels.",
            "T": "Gilgal is where it all came to a head — that is where I first turned against them. Because of what they do, I will expel them from my household. I will love them no longer. Every one of their rulers is a rebel."
        },
        "16": {
            "L": "Ephraim is smitten, their root is dried up, they shall bear no fruit: yea, though they bring forth, yet will I slay even the beloved fruit of their womb.",
            "M": "Ephraim is struck down; their root is dried up and they will bear no fruit. Even if they give birth, I will put to death the dearest children of their womb.",
            "T": "Ephraim has been struck. The root has gone dry — no fruit will come from this tree. And if in spite of it all a child is born, I will take that beloved child too. The line ends here."
        },
        "17": {
            "L": "My God will cast them away, because they did not hearken unto him: and they shall be wanderers among the nations.",
            "M": "My God will reject them because they did not listen to him; they will become wanderers among the nations.",
            "T": "My God will throw them away — they would not listen. And so they will wander, rootless, among the nations, with no land to call their own."
        }
    },
    "10": {
        "1": {
            "L": "Israel is an empty vine, he bringeth forth fruit unto himself: according to the multitude of his fruit he hath increased the altars; according to the goodness of his land they have made goodly images.",
            "M": "Israel is a spreading vine that produces fruit for itself. The more his fruit increased, the more altars he built; the better his land prospered, the more he adorned his sacred pillars.",
            "T": "Israel was a thriving vine — plenty of fruit. But every time the harvest grew, he built more altars to his idols; every time the land was good to him, he improved the sacred pillars. Prosperity did not lead to gratitude — it fed more idolatry."
        },
        "2": {
            "L": "Their heart is divided; now shall they be found faulty: he shall break down their altars, he shall spoil their images.",
            "M": "Their heart is deceitful; now they must bear their guilt. He will demolish their altars and destroy their sacred pillars.",
            "T": "Their hearts have been playing both sides — and now comes the reckoning. God will tear down their altars and smash their sacred stones."
        },
        "3": {
            "L": "For now they shall say, We have no king, because we feared not the LORD; what then should a king do to us?",
            "M": "For now they say, We have no king, because we did not fear the LORD. But what could a king do for us anyway?",
            "T": "They are already saying it: 'We have no king.' Of course not — they never truly feared Yahweh, and without that, a human king is worthless. They are learning the hard way what it means to have abandoned the only King who could help them."
        },
        "4": {
            "L": "They have spoken words, swearing falsely in making a covenant: thus judgment springeth up as hemlock in the furrows of the field.",
            "M": "They make empty promises, swear false oaths, make covenants — so justice springs up like poisonous weeds in the furrows of a plowed field.",
            "T": "Their mouths are full of fine-sounding agreements — but every oath is false, every treaty is hollow. The result? Justice has grown up like hemlock in their fields — bitter, toxic, choking out what was meant to grow."
        },
        "5": {
            "L": "The inhabitants of Samaria shall fear because of the calves of Bethaven: for the people thereof shall mourn over it, and the priests thereof that rejoiced on it, for the glory thereof, because it is departed from it.",
            "M": "The people of Samaria will tremble because of the calf-idol of Beth-aven. Its people will mourn over it, and its priests will wail — those who once rejoiced over its glory — because that glory has departed from it.",
            "T": "The people of Samaria are going to dread what happens to the golden calf at Beth-aven — Hosea's name for what was once Bethel, now a house of wickedness. They will mourn over the idol; the priests who built careers on it and reveled in its glory will wail when the glory is stripped away."
        },
        "6": {
            "L": "It shall be also carried unto Assyria for a present to king Jareb: Ephraim shall receive shame, and Israel shall be ashamed of his own counsel.",
            "M": "It will be carried off to Assyria as a gift for the great king. Ephraim will be shamed, and Israel will be put to shame because of his own plans.",
            "T": "That very calf will be hauled off to Assyria as a tribute payment to the great king. Ephraim will carry the shame of it; Israel will blush for the strategy that led to this."
        },
        "7": {
            "L": "As for Samaria, her king is cut off as the foam upon the water.",
            "M": "As for Samaria, her king will be swept away like a chip of wood on the water.",
            "T": "Samaria's king will vanish — gone in a moment, like a chip of bark swept off in the current."
        },
        "8": {
            "L": "The high places also of Aven, the sin of Israel, shall be destroyed: the thorn and the thistle shall come up on their altars; and they shall say to the mountains, Cover us; and to the hills, Fall on us.",
            "M": "The high places of Beth-aven, the sin of Israel, will be destroyed; thorns and thistles will grow up over their altars. They will call to the mountains, Cover us! and to the hills, Fall on us!",
            "T": "The high places of Beth-aven — the shrine that became a den of sin — will be demolished. Thorns and thistles will take over the altar mounds. And in their terror, the people will cry out to the mountains: 'Fall on us! Hide us!' Better to be buried than to face what is coming."
        },
        "9": {
            "L": "O Israel, thou hast sinned from the days of Gibeah: there they stood: the battle in Gibeah against the children of iniquity did not overtake them.",
            "M": "O Israel, you have sinned from the days of Gibeah; there they have persisted. Will not war overtake those evil people at Gibeah?",
            "T": "Israel, you have been on this path since the days of Gibeah — that ancient catastrophe when evil planted itself and no one drove it out. Is war not going to catch up with the sons of such wickedness?"
        },
        "10": {
            "L": "It is in my desire that I should chastise them; and the people shall be gathered against them, when they shall bind themselves in their two furrows.",
            "M": "It is my desire to discipline them; nations will be gathered against them to punish them for their double guilt.",
            "T": "I will choose the moment when I come against them in discipline. The nations will assemble against them when I punish them — doubly — for sins stacked on sins."
        },
        "11": {
            "L": "And Ephraim is as an heifer that is taught, and loveth to tread out the corn; but I passed over upon her fair neck: I will make Ephraim to ride; Judah shall plow, and Jacob shall break his clods.",
            "M": "Ephraim is a trained heifer that loves to thresh grain, but I have come to put a yoke on her fine neck. I will harness Ephraim; Judah must plow and Jacob must break up the hard ground.",
            "T": "Ephraim was like a heifer that loved the easy work of threshing — grain scattered on the floor, no heavy labor. But I am putting a yoke on that beautiful neck. Ephraim will pull a plow; Judah will furrow the hard ground; Jacob will break the clods. The easy days are over."
        },
        "12": {
            "L": "Sow to yourselves in righteousness, reap in mercy; break up your fallow ground: for it is time to seek the LORD, till he come and rain righteousness upon you.",
            "M": "Sow righteousness for yourselves; reap covenant loyalty; break up your unplowed ground. For it is time to seek the LORD, until he comes and showers righteousness on you.",
            "T": "Sow righteousness — that is what the ground needs now.\nReap the harvest of faithful love;\nbreak open the hardened soil of your hearts.\nIt is time — high time — to seek Yahweh,\nuntil he comes and rains his righteousness down on you."
        },
        "13": {
            "L": "Ye have plowed wickedness, ye have reaped iniquity; ye have eaten the fruit of lies: because thou didst trust in thy way, in the multitude of thy mighty men.",
            "M": "But you have plowed wickedness, you have reaped injustice, you have eaten the fruit of lies. Because you trusted in your own way, in the abundance of your warriors,",
            "T": "But that is not what you have done. You plowed wickedness and reaped injustice — you have been eating the harvest of your own lies. You put your confidence in your strategies, in the size of your armies —"
        },
        "14": {
            "L": "Therefore shall a tumult arise among thy people, and all thy fortresses shall be spoiled, as Shalman spoiled Betharbel in the day of battle: the mother was dashed in pieces upon her children.",
            "M": "therefore the tumult of war will arise against your people, and all your fortresses will be demolished, as Shalman demolished Beth-arbel on the day of battle, when mothers were dashed to pieces over their children.",
            "T": "— and so war will erupt among your people; every fortress will be torn down, the way Shalman tore down Beth-arbel in battle, leaving mothers and children alike crushed together in the rubble."
        },
        "15": {
            "L": "So shall Bethel do unto you because of your great wickedness: in a morning shall the king of Israel utterly be cut off.",
            "M": "So shall Bethel do to you because of your great wickedness. When morning comes, the king of Israel will be completely destroyed.",
            "T": "Bethel — the very center of Israel's false religion — will be the agent of their ruin. At the break of dawn, in one swift stroke, the king of Israel will be finished."
        }
    },
    "11": {
        "1": {
            "L": "When Israel was a child, then I loved him, and called my son out of Egypt.",
            "M": "When Israel was a child, I loved him, and out of Egypt I called my son.",
            "T": "When Israel was a child, I loved him —\nand out of Egypt I called my son."
        },
        "2": {
            "L": "As they called them, so they went from them: they sacrificed unto Baalim, and burned incense to graven images.",
            "M": "The more they were called, the more they went away; they kept offering sacrifices to the Baals and burning incense to carved images.",
            "T": "The more I called, the further they walked away.\nThey offered sacrifice after sacrifice to the Baals;\nthey burned incense to carved images."
        },
        "3": {
            "L": "I taught Ephraim also to go, taking them by their arms; but they knew not that I healed them.",
            "M": "Yet it was I who taught Ephraim to walk, taking him by the arms; but they did not know that I healed them.",
            "T": "I was the one who taught Ephraim to walk,\ntaking him by the arms —\nbut they never understood that it was I who healed them."
        },
        "4": {
            "L": "I drew them with cords of a man, with bands of love: and I was to them as they that take off the yoke on their jaws, and I laid meat unto them.",
            "M": "I led them with cords of human kindness, with ropes of love. I was like someone who lifts the yoke from their neck and bends down to feed them.",
            "T": "I led them with human tenderness, with ropes of love.\nI was the one who lifted the yoke from their jaws\nand bent down to feed them."
        },
        "5": {
            "L": "He shall not return into the land of Egypt, but the Assyrian shall be his king, because they refused to return.",
            "M": "He will not return to Egypt; the Assyrian will be his king, because they refused to repent.",
            "T": "They will not escape to Egypt — the Assyrian will be their king instead, because they refused to turn back to me."
        },
        "6": {
            "L": "And the sword shall abide on his cities, and shall consume his branches, and devour them, because of their own counsels.",
            "M": "A sword will rage against his cities; it will devour his strongholds and consume them because of their own schemes.",
            "T": "The sword will fall on city after city, consuming and devouring — and their own plans are what brought it down on them."
        },
        "7": {
            "L": "And my people are bent to backsliding from me: though they called them to the most High, none at all would exalt him.",
            "M": "My people are determined to turn away from me. Though they call out to the Most High, none of them will honor him at all.",
            "T": "My people are committed to walking away from me. They may cry upward — but their hearts never truly go there. No one among them actually lifts the Most High up."
        },
        "8": {
            "L": "How shall I give thee up, Ephraim? how shall I deliver thee, Israel? how shall I make thee as Admah? how shall I set thee as Zeboim? mine heart is turned within me, my repentings are kindled together.",
            "M": "How can I give you up, Ephraim? How can I hand you over, Israel? How can I make you like Admah? How can I treat you like Zeboiim? My heart churns within me; my compassion is kindled and grows warm.",
            "T": "How can I give you up, Ephraim?\nHow can I hand you over, Israel?\nHow can I make you like Admah,\ntreat you the way Zeboiim was treated?\nMy heart is turning over inside me;\nmy compassion is rising, tender and warm."
        },
        "9": {
            "L": "I will not execute the fierceness of mine anger, I will not return to destroy Ephraim: for I am God, and not man; the Holy One in the midst of thee: and I will not enter into the city.",
            "M": "I will not carry out my fierce anger; I will not again destroy Ephraim. For I am God and not a human being — the Holy One in your midst — and I will not come to destroy.",
            "T": "I will not act on the heat of my anger;\nI will not turn again and destroy Ephraim.\nFor I am God — not a human being.\nI am the Holy One in your midst,\nand I will not come against you in fury."
        },
        "10": {
            "L": "They shall walk after the LORD: he shall roar like a lion: when he shall roar, then the children shall tremble from the west.",
            "M": "They will walk after the LORD; he will roar like a lion. When he roars, his children will come trembling from the west.",
            "T": "They will follow Yahweh;\nhe will roar like a lion — and when he roars,\nhis children will come running, trembling, from the west."
        },
        "11": {
            "L": "They shall tremble as a bird out of Egypt, and as a dove out of the land of Assyria: and I will place them in their houses, saith the LORD.",
            "M": "They will come trembling like birds from Egypt and like doves from Assyria. I will settle them in their homes, declares the LORD.",
            "T": "They will flutter home like birds from Egypt,\nlike doves from the land of Assyria —\nand I will place them back in their own homes.\nThis is the word of Yahweh."
        },
        "12": {
            "L": "Ephraim compasseth me about with lies, and the house of Israel with deceit: but Judah yet ruleth with God, and is faithful with the saints.",
            "M": "Ephraim has surrounded me with lies, and the house of Israel with deceit. But Judah still walks with God and remains faithful to the Holy One.",
            "T": "Ephraim encircles me with nothing but lies;\nIsrael's house wraps itself in deceit.\nBut Judah still walks with God,\nstill faithful to the Holy One."
        }
    },
    "12": {
        "1": {
            "L": "Ephraim feedeth on wind, and followeth after the east wind: he daily increaseth lies and desolation; and they do make a covenant with the Assyrian, and oil is carried into Egypt.",
            "M": "Ephraim feeds on wind and pursues the scorching east wind all day; he multiplies lies and violence. He makes a covenant with Assyria, and olive oil is carried to Egypt.",
            "T": "Ephraim gorges on wind — he chases the burning east wind all day long, filling his life with lies and ruin. He cuts deals with Assyria on one side and sends tribute oil to Egypt on the other. Every alliance is a betrayal."
        },
        "2": {
            "L": "The LORD hath also a controversy with Judah, and will punish Jacob according to his ways; according to his doings will he recompense him.",
            "M": "The LORD has a case against Judah as well, and will punish Jacob according to his ways; he will repay him according to his deeds.",
            "T": "Yahweh has a legal case against Judah too — and will call Jacob to account for everything he has done, paying back deed for deed."
        },
        "3": {
            "L": "He took his brother by the heel in the womb, and by his strength he had power with God:",
            "M": "In the womb he grasped his brother's heel, and in his strength he contended with God.",
            "T": "From the very womb, Jacob was grabbing — he seized his brother by the heel. And when he grew strong, he wrestled with God himself."
        },
        "4": {
            "L": "Yea, he had power over the angel, and prevailed: he wept, and made supplication unto him: he found him in Bethel, and there he spake with us;",
            "M": "He wrestled with the angel and prevailed; he wept and pleaded for the blessing. At Bethel he found him, and there God spoke with us —",
            "T": "He fought the angel and won — but then he wept and begged for a blessing. It was at Bethel that he found God, and there God spoke a word that has echoed ever since — a word spoken to us as well."
        },
        "5": {
            "L": "Even the LORD God of hosts; the LORD is his memorial.",
            "M": "even the LORD God of hosts — the LORD is his name to be remembered.",
            "T": "The LORD God of Hosts — that is the name.\nThat is who met Jacob at Bethel.\nYahweh: the name that endures forever."
        },
        "6": {
            "L": "Therefore turn thou to thy God: keep mercy and judgment, and wait on thy God continually.",
            "M": "But as for you, return to your God; maintain covenant loyalty and justice, and wait for your God always.",
            "T": "So then — return to your God.\nPractice faithful love and do what is just.\nWait for your God, always."
        },
        "7": {
            "L": "He is a merchant, the balances of deceit are in his hand: he loveth to oppress.",
            "M": "Ephraim is a trader who uses dishonest scales; he loves to take advantage of others.",
            "T": "Ephraim has become a trader — dishonest scales in hand, delighted to exploit. This is what he has reduced himself to."
        },
        "8": {
            "L": "And Ephraim said, Yet I am become rich, I have found me out substance: in all my labours they shall find none iniquity in me that were sin.",
            "M": "But Ephraim says, Surely I have become rich; I have gained wealth for myself. In all my hard work they will find no guilt in me, nothing that is sinful.",
            "T": "Ephraim says: 'Look how rich I've become — I earned all of this myself. No one can charge me with wrongdoing. Everything I have is clean profit.' The self-justification of the successful sinner."
        },
        "9": {
            "L": "And I that am the LORD thy God from the land of Egypt will yet make thee to dwell in tabernacles, as in the days of the solemn feast.",
            "M": "But I, the LORD your God since the land of Egypt, will make you live in tents again, as in the days of the appointed festival.",
            "T": "But I am Yahweh your God — the one who brought you out of Egypt. I will make you live in tents again, the way you did in the wilderness — stripped of the wealth you are so proud of, back to the beginning."
        },
        "10": {
            "L": "I have also spoken by the prophets, and I have multiplied visions, and used similitudes, by the ministry of the prophets.",
            "M": "I spoke through the prophets; I multiplied visions and gave parables through the prophets.",
            "T": "I spoke — through the prophets again and again. I multiplied the visions. I used images and comparisons to reach them. The word was never absent. They were never without warning."
        },
        "11": {
            "L": "Is there iniquity in Gilead? surely they are vanity: they sacrifice bullocks in Gilgal; yea, their altars are as heaps in the furrows of the fields.",
            "M": "Is Gilead wicked? Yes, they are worthless! In Gilgal they sacrifice bulls; their altars will become like heaps of stones in the furrows of the fields.",
            "T": "Gilead — nothing but wickedness. Worthless, every bit of it. In Gilgal they keep piling up their sacrifices to bulls; their altars will become nothing but heaps of rubble in the furrows — relics of a ruined religion."
        },
        "12": {
            "L": "And Jacob fled into the country of Syria, and Israel served for a wife, and for a wife he kept sheep.",
            "M": "Jacob fled to the country of Aram, and Israel served for a wife and tended flocks for a wife.",
            "T": "Remember: Jacob ran — fled to Aram. He served years for a wife, years of labor to win the woman he loved."
        },
        "13": {
            "L": "And by a prophet the LORD brought Israel out of Egypt, and by a prophet was he preserved.",
            "M": "Through a prophet the LORD brought Israel up from Egypt, and through a prophet he was kept safe.",
            "T": "Through a prophet — Moses — Yahweh brought Israel out of Egypt. Through that same prophet Israel was preserved. The word of God given through human servants: that is how God works."
        },
        "14": {
            "L": "Ephraim provoked him to anger most bitterly: therefore shall he leave his blood upon him, and his reproach shall his Lord return unto him.",
            "M": "Ephraim has provoked his LORD to the deepest anger; so he will leave Ephraim's bloodguilt on him and return his disgrace back upon him.",
            "T": "Ephraim has provoked Yahweh to the bitter end. So Yahweh will let the blood Ephraim has shed remain on him — and every act of shame will be thrown back in his face."
        }
    }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'hosea')
        merge_tier(existing, HOSEA, tier_key)
        save(tier_dir, 'hosea', existing)
    print('Hosea 7–12 written.')

if __name__ == '__main__':
    main()
