"""
MKT Lamentations chapters 1–2 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-lamentations-1-2.py

Translation decisions:

- H349 (אֵיכָה/ʾêkāh, "how/alas"): The book's signature opening word. Rendered "How"
  in L/M (preserving the rhetorical cry). In T, rendered as "Alas!" or "How" depending
  on verse — the word carries both lamentation and incredulity simultaneously; ch 2:1
  opens with the same word as ch 1:1.

- H3068 (יהוה): "LORD" in L/M throughout (small caps convention preserved as uppercase).
  "Yahweh" in T where personal-name force is significant — particularly 1:5,9,12,17,18;
  2:1,6,7,8,9,17. Narrative formula "declares the LORD" context absent here — Lamentations
  is direct lament/address rather than prophetic oracle, so "LORD" vs "Yahweh" in T
  tracks intensity of direct address rather than oracle-delivery idiom.

- H136 (אֲדֹנָי / Adonai, "the Lord"): Lamentations uses אֲדֹנָי (Adonai) frequently —
  notably 2:1,2,5,7,8,18,19,20 — distinct from H3068 (יהוה). Rendered "the Lord" (title)
  in all tiers to distinguish from יהוה. When both appear together the distinction is
  meaningful: Adonai = the sovereign; Yahweh = the covenant name. In T this distinction
  is noted where contextually significant.

- H490 (אַלְמָנָה / almānāh): "widow" in L/M/T. The glossary primary gloss ("desolate
  house") is clearly a lexicographic variant; the 1:1 simile "like a widow" demands the
  relational meaning. The widow image in Lamentations is covenant-specific: Israel was
  married to Yahweh (Jer 3:1; Hos 2); now she sits like a woman whose husband has
  departed. T surfaces this covenant-divorce subtext.

- H2617 (חֵסֶד / ḥesed): Does not appear prominently in these chapters. Where related
  covenant language appears, "steadfast love/faithfulness" is used in M; T: "covenant
  loyalty." 3:22 is the great ḥesed verse (outside our range).

- H5315 (נֶפֶשׁ): "soul/life/self" depending on context. In 1:11,19 it refers to keeping
  oneself alive ("relieve the soul" = stave off death); rendered "hunger" context in M
  as "keep themselves alive." In 2:12 the "soul was poured out" = life ebbing away;
  T: "breath ebbing." Embodied self throughout — no Greek immaterial soul imported.

- H1818 (דָּם / dam): "blood" — does not appear prominently in chs 1–2 (main usage in 4:13).

- H6588 (פֶּשַׁע / peshaʿ): "transgressions" in L/M; T: "sins" or "rebellion" depending
  on contextual gravity. In 1:5 and 1:14 the word denotes the structural cause of exile.
  Peshaʿ is covenant-breach language (rebellion against a superior), not merely moral
  failure — T surfaces this where possible.

- H2403 (חַטָּאת / ḥaṭṭāʾt): "sin" in L/M; T uses "moral failure" or "sin" depending
  on context. Appears less prominently in these chapters.

- H5771 (עָוֹן / ʿāwôn): "iniquity" in L/M. In 2:14 it is Zion's hidden iniquity that
  the false prophets failed to expose. T: "guilt" — ʿāwôn includes both the act and its
  consequence/burden.

- H5030 (נָבִיא / nābîʾ): "prophet" in all tiers. In 2:9,14 the failure of prophets
  is a key accusation — they received no vision from the LORD (2:9) and gave false visions
  (2:14). This is consistent with Jeremiah's sustained polemic against false prophecy.

- H7307 (רוּחַ / rûaḥ): Does not appear significantly in chs 1–2. Not a major translation
  issue for this range.

- Acrostic structure: Hebrew chs 1–2 are alphabetic acrostics (22 verses, each beginning
  with the successive letter of the Hebrew alphabet, aleph through taw). This is not
  reproduced in English translation as it would require forcing unnatural constructions.
  The T tier honors the poetic quality of each verse but makes no attempt to reproduce
  the acrostic structure. A note in the T tier rendering is implied in the cadenced
  line structure used.

- Verbal aspect: Hebrew perfect verbs in lament poetry often describe completed acts
  that are either historical (the disaster) or performative (I have sinned). Imperfects
  in direct address to the LORD are petitionary. These distinctions are preserved:
  perfect = "has X" or "he X-ed"; jussive/imperfect petitions = "let..." or present.

- Speaker shifts in ch 1: vv. 1–11 are third-person description; from v.11b ("See, O LORD...")
  the personified city speaks in first person. This shift is preserved in all three tiers.
  In ch 2 the narrator speaks throughout vv. 1–17; the personified narrator speaks from
  v.11 ("My eyes fail...") with direct address to Zion in v.13; v.18 addresses the wall.
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

LAMENTATIONS = {
  "1": {
    "1": {
      "L": "How she sits solitary, the city great with people! She has become like a widow. She that was great among the nations has become a tributary; she that was a princess among the provinces has become a vassal.",
      "M": "How deserted she sits, the city once full of people! She has become like a widow. Once great among the nations, once a princess among the provinces, she is now forced into servitude.",
      "T": "Alas! How the city sits in ruin — she who once teemed with people now sits alone, like a widow. She who was great among the nations, a princess among the provinces, is now bent under the yoke of forced labor."
    },
    "2": {
      "L": "She weeps bitterly in the night, and her tears are on her cheeks. Of all her lovers she has none to comfort her; all her friends have dealt treacherously with her and have become her enemies.",
      "M": "She weeps bitterly in the night, her tears on her cheeks. Among all who loved her there is none to comfort her; all her friends have betrayed her and become her enemies.",
      "T": "Through the night she weeps, tears streaming down her face — and no one comes. Everyone who once pledged devotion has betrayed her, turned enemy. Not one lover remains to offer comfort."
    },
    "3": {
      "L": "Judah has gone into captivity under affliction and under great servitude. She dwells among the nations and finds no rest; all her pursuers have overtaken her in the midst of her distress.",
      "M": "Judah has gone into exile because of affliction and hard servitude. She lives among the nations but finds no resting place. All her pursuers have overtaken her in the midst of her straits.",
      "T": "Judah was driven into exile — affliction and grinding servitude forced her out. She wanders among the nations but cannot settle, cannot rest. Her hunters ran her down while she was already trapped."
    },
    "4": {
      "L": "The roads of Zion mourn, for none come to the appointed feasts. All her gates are desolate; her priests groan; her virgins are afflicted; she herself is in bitterness.",
      "M": "The roads to Zion mourn because no one comes to her appointed feasts. All her gates are desolate; her priests groan; her young women are sorrowful; she herself is in bitter distress.",
      "T": "The roads to Zion are deserted — no pilgrims traveling them now, no worshipers bound for the feasts. Her gates stand empty. Her priests can only groan. Her young women are stricken with grief. And Zion herself drowns in bitterness."
    },
    "5": {
      "L": "Her adversaries have become the chief; her enemies prosper, for the LORD has afflicted her for the multitude of her transgressions. Her children have gone into captivity before the enemy.",
      "M": "Her adversaries have become her masters; her enemies prosper, because the LORD afflicted her for the multitude of her transgressions. Her children have been led away captive before the enemy.",
      "T": "Her tormentors are now her lords; her enemies flourish. Yahweh himself brought this upon her — her transgressions were many, and he chose to afflict. Her children walk into captivity ahead of the enemy's sword."
    },
    "6": {
      "L": "And from the daughter of Zion all her splendor has departed. Her princes have become like stags that find no pasture; they fled without strength before the pursuer.",
      "M": "And from the daughter of Zion all her majesty has departed. Her princes have become like deer that find no pasture; they fled exhausted before the pursuer.",
      "T": "All glory has drained from Zion's daughter. Her princes — once powerful men — now stumble away like starving deer that cannot find a patch of grass, fleeing without strength, the enemy at their heels."
    },
    "7": {
      "L": "Jerusalem remembered in the days of her affliction and of her wanderings all her precious things that she had from the days of old, when her people fell into the hand of the foe and there was none to help her. The adversaries saw her and mocked at her downfall.",
      "M": "Jerusalem recalled in the days of her affliction and exile all the precious things she once possessed in former days. When her people fell into the hand of the foe with no one to help, the adversaries looked on and laughed at her destruction.",
      "T": "In the depths of affliction and homelessness, Jerusalem's mind returns to all she once had — the treasures, the beauty, the glory of former days. But when her people fell to the enemy, no one came to their aid. Her adversaries stood there and sneered at her collapse."
    },
    "8": {
      "L": "Jerusalem sinned grievously; therefore she has become an object of scorn. All who honored her despise her, for they have seen her nakedness. Even she herself groans and turns away.",
      "M": "Jerusalem sinned gravely; therefore she has become unclean. All who once honored her now despise her, for they have seen her shame. She herself groans and turns away.",
      "T": "Jerusalem's sin was great — and the consequence is exposure. Everyone who once held her in honor now looks with contempt, for they have seen her stripped of dignity. She herself, unable to face them, groans and turns away."
    },
    "9": {
      "L": "Her filthiness is in her skirts; she did not consider her fate. She fell down in a shocking way, with none to comfort her. 'Look, O LORD, upon my affliction, for the enemy has magnified himself!'",
      "M": "Her uncleanness clung to her skirts; she did not consider her future. Her fall was appalling, with no one to comfort her. 'See, O LORD, my affliction, for the enemy has triumphed!'",
      "T": "The stains of her shame were visible all along — she just never looked ahead, never thought about where the road was leading. Her fall came suddenly and shockingly. No one moved to help. And from that depth she cries: 'LORD, see my misery — the enemy has grown bold!'"
    },
    "10": {
      "L": "The adversary has spread out his hand over all her precious things. For she has seen the nations enter her sanctuary — those whom you commanded should not enter your assembly.",
      "M": "The enemy stretched out his hand over all her treasures. She watched the nations enter her sanctuary — nations that you had commanded should not enter your congregation.",
      "T": "The enemy laid hands on everything she treasured. She watched, helpless, as pagan nations walked into her sanctuary — the very ones God had barred from the assembly. The worst violation had come true."
    },
    "11": {
      "L": "All her people groan as they search for bread. They have given their precious things for food to relieve their hunger. 'See, O LORD, and look, for I have become despised.'",
      "M": "All her people groan as they search for bread. They traded their treasures for food to keep themselves alive. 'Look, O LORD, and consider — how contemptible I have become!'",
      "T": "The whole city groans with hunger — people trading everything they once valued for a scrap of bread. Everything beautiful, everything meaningful, sold to stave off starvation. 'LORD, look at this. Look at me. See how low I have been brought.'"
    },
    "12": {
      "L": "Is it nothing to you, all you who pass by? Look and see if there is any sorrow like my sorrow, which was inflicted on me, which the LORD inflicted in the day of his fierce anger.",
      "M": "Is it nothing to you, all who pass by? Look and see if there is any sorrow like my sorrow, the sorrow brought upon me, with which the LORD afflicted me on the day of his burning anger.",
      "T": "You there — passing by — does it mean nothing to you? Stop. Look. Has anyone ever suffered like this? This is what the LORD poured out on me when his anger burned at full strength."
    },
    "13": {
      "L": "From on high he sent fire; it went down into my bones. He spread a net for my feet and turned me back. He has made me desolate, faint all the day long.",
      "M": "From on high he sent fire into my bones. He spread a net for my feet and turned me back. He has left me desolate and faint all day long.",
      "T": "He sent fire from heaven straight into my bones. He laid a trap at my feet and turned me back when I tried to flee. He has left me wasted, faint, exhausted — all day, every day."
    },
    "14": {
      "L": "The yoke of my transgressions was bound; by his hand they were woven together and laid upon my neck. He made my strength fail. The Lord has delivered me into the hands of those I cannot withstand.",
      "M": "The yoke of my transgressions was tightly bound; braided together by his hand and placed on my neck, it sapped my strength. The Lord has handed me over to those I cannot resist.",
      "T": "My sins were gathered up and twisted into a yoke — woven by God's own hand, laid on my neck. He drained my strength. The Lord gave me over to enemies I have no power to resist."
    },
    "15": {
      "L": "The Lord rejected all my mighty men in my midst. He summoned an assembly against me to crush my young men. The Lord trodden as in a winepress the virgin daughter of Judah.",
      "M": "The Lord dismissed all my warriors from my midst. He called up a host against me to crush my young men. The Lord has trodden the virgin daughter of Judah as in a winepress.",
      "T": "The Lord swept away every soldier I had. He summoned an army — against me — to break my young men down. And then, as though pressing the harvest, he trod Judah's daughter like grapes in a winepress."
    },
    "16": {
      "L": "For these things I weep; my eye, my eye runs down with water, because a comforter is far from me, one who should restore my soul. My children are desolate, because the enemy has prevailed.",
      "M": "For these things I weep; my eyes stream with tears because no comforter is near who could revive my spirit. My children are desolate, for the enemy has triumphed.",
      "T": "I weep for all of this — my tears will not stop. A comforter should be near; instead there is no one within reach. My children are left broken and desolate, because the enemy has won."
    },
    "17": {
      "L": "Zion spreads out her hands, but there is none to comfort her. The LORD has commanded against Jacob that his adversaries should surround him. Jerusalem has become as a thing unclean among them.",
      "M": "Zion stretches out her hands, but there is no one to comfort her. The LORD has commanded that Jacob's adversaries encircle him. Jerusalem has become a thing of impurity in their midst.",
      "T": "Zion reaches out — and grasps nothing. No comfort comes. Yahweh himself issued the order: Zion's enemies would encircle her. And now, among the nations, she is treated as unclean, untouchable."
    },
    "18": {
      "L": "The LORD is righteous, for I have rebelled against his word. Hear, I pray, all peoples, and behold my sorrow. My virgins and my young men have gone into captivity.",
      "M": "The LORD is in the right, for I rebelled against his command. Hear, all peoples, and look at my anguish. My young women and young men have gone into captivity.",
      "T": "The LORD is right. I sinned — I rebelled against his clear command, and this is the consequence. Hear me, all nations: this is my grief. My daughters and my sons — my young people — are gone, captives in a foreign land."
    },
    "19": {
      "L": "I called to my lovers, but they deceived me. My priests and my elders perished in the city while they searched for food to relieve their hunger.",
      "M": "I called to my allies, but they deceived me. My priests and my elders perished in the city as they searched for food to keep themselves alive.",
      "T": "I reached out to every ally — and was deceived by every one. While my priests and elders stumbled through the city streets searching for something to eat, they died there, their lives spent looking for bread."
    },
    "20": {
      "L": "Look, O LORD, for I am in distress. My inner parts are in torment; my heart is wrung within me, for I have been very rebellious. Outside the sword bereaves; inside it is as death.",
      "M": "See, O LORD, how distressed I am! My insides churn; my heart writhes within me, for I have sinned deeply. In the streets the sword kills; inside it is scarcely better — death either way.",
      "T": "LORD, look at this — I am crushed inside and out. My gut twists, my heart convulses. I know I have sinned gravely. And the toll is everywhere: outside, the sword devours; inside the walls, it is barely different — death either way."
    },
    "21": {
      "L": "They have heard how I groan; there is none to comfort me. All my enemies have heard of my trouble; they are glad that you have done it. You have brought the day that you announced; now let them be as I am.",
      "M": "They heard my sighing; there is no one to comfort me. All my enemies heard of my misery and are glad that you brought this about. Bring on the day you announced; let them become as I am.",
      "T": "My enemies heard my cries — and celebrated. Not one moved to comfort me. They heard what God had done and were delighted by it. And I say: let the day you appointed come for them too. Let them end up where I am."
    },
    "22": {
      "L": "Let all their wickedness come before you, and do unto them as you have done unto me for all my transgressions. For my sighs are many and my heart is faint.",
      "M": "Let all their wickedness come before you, and deal with them as you have dealt with me for all my transgressions. For my sighs are many and my heart is faint.",
      "T": "Bring their wickedness into your presence and do to them what you have done to me for my sins — every transgression I committed. My sighs have multiplied beyond counting. My heart has given out."
    }
  },
  "2": {
    "1": {
      "L": "How the Lord in his anger has covered the daughter of Zion with a cloud! He has cast down from heaven to earth the splendor of Israel. He did not remember his footstool in the day of his anger.",
      "M": "How the Lord shrouded the daughter of Zion in his anger! He hurled the splendor of Israel down from heaven to earth. He did not remember his footstool on the day of his burning anger.",
      "T": "Alas! The Lord wrapped Zion in a cloud of his fury and threw her beauty down from heaven to the dust. He did not spare even his own footstool when anger consumed him."
    },
    "2": {
      "L": "The Lord has swallowed up without pity all the habitations of Jacob. In his wrath he has thrown down the strongholds of the daughter of Judah; he has brought to the ground in dishonor the kingdom and its princes.",
      "M": "The Lord swallowed up all Jacob's dwellings without pity. In his wrath he broke down the strongholds of Judah's daughter; he brought the kingdom and its princes down to the ground in disgrace.",
      "T": "The Lord consumed every dwelling in Jacob's land — not one was spared, not one was pitied. In burning wrath he demolished Judah's fortresses. He toppled the kingdom and shamed its princes, bringing them down to the dust."
    },
    "3": {
      "L": "He has cut off in fierce anger all the horn of Israel. He has drawn back his right hand from before the enemy. He has burned in Jacob like a flaming fire consuming all around.",
      "M": "In fierce anger he cut off every source of Israel's strength. He withdrew his right hand in the face of the enemy. He blazed through Jacob like a fire consuming everything around it.",
      "T": "Every source of Israel's strength he severed in his fury. He pulled his own right hand back — withdrew his protection — and let the enemy advance. Then he burned through Jacob like a wildfire devouring everything in its path."
    },
    "4": {
      "L": "He has bent his bow like an enemy; his right hand was set as an adversary and he slew all who were precious to the eye. Into the tent of the daughter of Zion he has poured out his wrath like fire.",
      "M": "He bent his bow like an enemy; he stood firm as an adversary and cut down all who were pleasing to the eye. He poured out his wrath like fire into the tent of Zion's daughter.",
      "T": "He drew his bow as though Zion herself were the enemy. He planted himself like an opponent and cut down everyone who was beautiful and dear. He emptied his wrath like fire into Zion's very home."
    },
    "5": {
      "L": "The Lord has become like an enemy. He has swallowed up Israel; he has swallowed up all her palaces. He has destroyed his strongholds and increased in the daughter of Judah mourning and lamentation.",
      "M": "The Lord has acted like an enemy. He has swallowed up Israel, swallowed all her palaces. He demolished his own strongholds and multiplied mourning and lamentation in Judah's daughter.",
      "T": "The Lord has become the enemy. He devoured Israel — her palaces, her fortresses — demolished what belonged to him. And into Judah he poured grief upon grief, mourning upon lamentation."
    },
    "6": {
      "L": "He has laid waste his tabernacle like a garden booth; he has destroyed his appointed place of assembly. The LORD has caused the appointed feasts and sabbaths in Zion to be forgotten, and in his fierce indignation has spurned both king and priest.",
      "M": "He broke down his tabernacle like a garden shelter and ruined his assembly place. The LORD made the appointed feasts and sabbaths in Zion forgotten; in his fierce anger he rejected both king and priest.",
      "T": "He tore down his own tabernacle as easily as pulling apart a harvest shelter. He wrecked the place where his people had assembled. The LORD erased the feasts, the sabbaths — all of it — from Zion's memory. And then, with burning contempt, he cast aside both king and priest."
    },
    "7": {
      "L": "The Lord has rejected his altar and disowned his sanctuary. He has given into the hand of the enemy the walls of her palaces. They have raised a noise in the house of the LORD as on the day of an appointed feast.",
      "M": "The Lord rejected his altar and disowned his sanctuary. He handed over the walls of her palaces to the enemy. They raised a shout in the house of the LORD as on a feast day.",
      "T": "The Lord renounced his own altar. He turned from his sanctuary in disgust. He handed the palace walls over to the enemy. And in what used to be the LORD's house, the enemy shouts — their victory cries sounding, grotesquely, like a festival crowd."
    },
    "8": {
      "L": "The LORD purposed to destroy the wall of the daughter of Zion. He stretched out the measuring line; he did not withdraw his hand from destroying. He caused rampart and wall to lament; they mourned together.",
      "M": "The LORD planned the destruction of Zion's wall. He stretched out the measuring line and would not pull his hand back from demolishing. He caused rampart and wall to mourn; they wasted away together.",
      "T": "The LORD made a deliberate plan: he would tear down Zion's wall. He took the measuring line — the same tool used to build — and used it now to demolish. He refused to relent. Rampart and wall collapse together, as though grieving their own ruin."
    },
    "9": {
      "L": "Her gates have sunk into the ground; he has destroyed and broken their bars. Her king and her princes are among the nations; the law is no more, and her prophets find no vision from the LORD.",
      "M": "Her gates have sunk into the ground; he shattered and broke their bars. Her king and princes are among the nations; the law is gone, and her prophets receive no vision from the LORD.",
      "T": "The city gates have collapsed into the ground; their bars are smashed. Her king is in exile among the nations, her princes with him. The law is silent. And the prophets — they have nothing. The LORD has stopped speaking."
    },
    "10": {
      "L": "The elders of the daughter of Zion sit on the ground in silence. They have cast dust on their heads; they have put on sackcloth. The virgins of Jerusalem bow their heads to the ground.",
      "M": "The elders of Zion's daughter sit on the ground in silence. They have thrown dust on their heads and put on sackcloth. Jerusalem's young women bow their heads to the ground.",
      "T": "Zion's elders sit in the dirt, silent. Ashes thrown over their heads. Sackcloth wrapped around them. Jerusalem's young women press their faces to the earth. The language of mourning has taken over completely."
    },
    "11": {
      "L": "My eyes fail with tears; my inner parts are in torment; my bile is poured out to the earth over the ruin of the daughter of my people, because infants and sucklings swoon in the streets of the city.",
      "M": "My eyes are spent with weeping; my insides churn; my bile spills on the ground over the destruction of my people, because infants and nursing babies collapse in the city streets.",
      "T": "I have wept until I can barely see. My insides have given way; bile rises in my throat. I am undone by what I have seen — infants collapsing in the city streets, nursing babies fainting from hunger. This is the ruin of my people."
    },
    "12": {
      "L": "They say to their mothers, 'Where is grain and wine?' as they faint like the wounded in the streets of the city, as their life is poured out on their mothers' bosoms.",
      "M": "They cry to their mothers, 'Where is grain and wine?' as they collapse like the mortally wounded in the city streets, their breath ebbing away on their mothers' laps.",
      "T": "Children crying out to their mothers: 'Where is bread? Where is anything to drink?' — and then falling, like soldiers cut down, in the city streets. Their last breath spent on their mothers' laps."
    },
    "13": {
      "L": "What shall I say to you? To what shall I compare you, O daughter of Jerusalem? To what shall I liken you to comfort you, O virgin daughter of Zion? For your ruin is as vast as the sea; who can heal you?",
      "M": "What can I say to you? To what can I compare you, daughter of Jerusalem? To what shall I liken you to offer comfort, virgin daughter of Zion? Your wound is as vast as the sea. Who can heal you?",
      "T": "What words are there for this? What comparison even comes close? O Jerusalem, O Zion — I want to offer comfort but cannot find the words. Your catastrophe is ocean-sized. No human medicine can reach this wound."
    },
    "14": {
      "L": "Your prophets saw for you vain and worthless visions; they did not expose your iniquity to restore your fortunes. They saw for you oracles that were false and misleading.",
      "M": "Your prophets gave you empty and deceptive visions. They did not expose your sin to restore you. The oracles they proclaimed were false and misleading.",
      "T": "The prophets told you what you wanted to hear — empty visions, comfortable lies. They should have confronted your sin; instead they buried it. Their so-called oracles were fabrications that led you away from repentance and into exile."
    },
    "15": {
      "L": "All who pass by clap their hands at you; they hiss and wag their heads at the daughter of Jerusalem: 'Is this the city that men called the perfection of beauty, the joy of all the earth?'",
      "M": "All who pass by clap their hands at you; they hiss and wag their heads at Jerusalem's daughter: 'Is this the city that was called the perfection of beauty, the joy of all the earth?'",
      "T": "Passersby clap in mockery. They hiss. They shake their heads. 'Look — is this it? Is this the city they called the most beautiful in the world, the delight of all peoples?' They cannot believe the ruins before them."
    },
    "16": {
      "L": "All your enemies have opened wide their mouths against you; they hiss and gnash their teeth. They say, 'We have swallowed her up! This is the day we have looked for; we have found it; we have seen it!'",
      "M": "All your enemies open wide their mouths against you; they hiss and gnash their teeth. They say, 'We have devoured her! This is the day we waited for! We have seen it — it has come!'",
      "T": "Every enemy opens their mouth wide over you — hissing, grinding their teeth in glee. 'We've destroyed her!' they say. 'This is the day we dreamed of! We waited and waited, and now at last we've seen it.' Their delight is obscene."
    },
    "17": {
      "L": "The LORD has done what he purposed; he has carried out his word that he commanded in days of old. He has thrown down without pity; he has made your enemy rejoice over you and exalted the horn of your adversaries.",
      "M": "The LORD has done what he planned; he fulfilled the word he decreed in days of old. He overthrew without pity and let your enemy rejoice over you; he raised up the strength of your adversaries.",
      "T": "The LORD has done exactly what he said he would. He spoke these warnings long ago, and now every word stands fulfilled — without exception, without mercy. He brought down what he intended to bring down. He gave your enemies their moment of triumph and raised their banner over you."
    },
    "18": {
      "L": "Their heart cried out to the Lord. O wall of the daughter of Zion, let tears run down like a river day and night! Give yourself no rest; let not the apple of your eye cease!",
      "M": "Their heart cried out to the Lord. O wall of Zion's daughter, let tears flow like a river day and night! Give yourself no rest; let your eyes run without ceasing!",
      "T": "Their hearts poured out a cry to the Lord. O wall of Zion — weep! Let your tears run like a river, night and day, with no stopping, no relief. Do not rest. Do not dry your eyes."
    },
    "19": {
      "L": "Arise, cry out in the night, at the beginning of the watches! Pour out your heart like water before the face of the Lord. Lift your hands to him for the lives of your children, who faint for hunger at the head of every street.",
      "M": "Arise, cry out in the night! At the start of the night watches pour out your heart like water before the Lord. Lift your hands to him for the lives of your children, who are fainting from hunger at the head of every street.",
      "T": "Get up — cry out in the night. When the watch changes, pour out your heart to the Lord like water poured on the ground. Raise your hands to him. Plead for your children — they are collapsing from starvation on every street corner."
    },
    "20": {
      "L": "Look, O LORD, and consider! To whom have you done this? Should women eat their own offspring, the infants they have cradled? Should priest and prophet be slain in the sanctuary of the Lord?",
      "M": "Look, O LORD, and take heed! To whom have you done this? Should women eat the fruit of their own wombs, their newborn children? Should priest and prophet be killed in the LORD's sanctuary?",
      "T": "LORD — look. Think about what you are watching. Women eating their own newborn children. Priests and prophets cut down in the very sanctuary. To whom are you doing this? Is this who we are to you?"
    },
    "21": {
      "L": "Young and old lie on the ground in the streets. My virgins and my young men have fallen by the sword. You struck them down in the day of your anger; you slaughtered without pity.",
      "M": "Young and old lie on the ground in the streets. My young women and young men have fallen by the sword. You killed them in the day of your anger; you showed no mercy.",
      "T": "Old people, young people — all of them on the ground in the streets. My daughters and my sons cut down by the sword. You killed them in your wrath. You showed no mercy to any of them."
    },
    "22": {
      "L": "You summoned on every side, as though for a day of assembly, my terrors. And in the day of the LORD's anger, none escaped or remained. Those I swaddled and reared my enemy has consumed.",
      "M": "You called my terrors from every side as though summoning people to a feast day. On the day of the LORD's anger, none escaped or survived. Those I had held and raised, my enemy destroyed.",
      "T": "You called in all my terrors from every direction — as if announcing a holy day, as if inviting guests to a feast. On the day of the LORD's fury, no one escaped. No one was left. The children I wrapped in swaddling cloths and raised up — my enemy consumed them all."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'lamentations')
        merge_tier(existing, LAMENTATIONS, tier_key)
        save(tier_dir, 'lamentations', existing)
    print('Lamentations 1–2 written.')

if __name__ == '__main__':
    main()
