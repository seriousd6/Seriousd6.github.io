"""
MKT Jeremiah chapters 51–52 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-jeremiah-51-52.py

Translation decisions (consistent with mkt-jeremiah-1-3.py through mkt-jeremiah-47-48.py):

- H3068 (יהוה): "LORD" in L/M throughout; "Yahweh" in T for oracle-delivery, oath-bond,
  and divine-name-force contexts. The repeated "declares the LORD" becomes "declares
  Yahweh" in T throughout ch 51's oracle. Ch 52 (narrative prose) uses "the LORD" in T
  since the narrator register differs from prophetic-voice register.

- H430 (אֱלֹהִים): "God" throughout for the God of Israel (51:5, 33; 52:2). "God of Israel"
  as title preserved in full at 51:33. "Holy One of Israel" (51:5, H6918 + H3478) is a
  title drawn from Isaiah; T preserves it as "Israel's Holy God."

- H6635 (צְבָאוֹת): "hosts" in L/M; "Yahweh of hosts" in T — the commander title frames
  the oracle's sovereign authority. Appears at 51:5, 14, 19, 33, 57, 58.

- H5315 (נֶפֶשׁ): "life/lives" in survival idioms (51:6, 45 — "save his life"); "soul"
  where the embodied self is the reference point. No Greek immaterial-soul concept is in view.

- H7307 (רוּחַ): 51:1 "a destroying wind" — wind, not spirit; the meteorological sense fits
  the battle imagery. 51:11 "the LORD has stirred up the spirit of the kings of the Medes"
  — here rûaḥ = the inner motivation/drive God stirs; L: "spirit"; M: "spirit"; T: "resolve."

- H1285 (בְּרִית): does not appear explicitly in these chapters; no decision needed.

- H2617 (חֶסֶד): does not appear in chs 51–52; no decision needed.

- H894 (בָּבֶל / Babel): "Babylon" consistently. "Sheshach" (51:41, H8347) is the atbash
  cipher for Babel (b-b-l → š-š-k in reverse alphabet). L/M: "Sheshach" with Babylon
  supplied in bracket in T: "Sheshach — Babylon itself."

- H1168 (לֵב קָמָי / Lev-kamai, 51:1): atbash cipher for Kasdim (Chaldeans). L preserves
  the cipher name; M/T supply "Chaldea" since the referent is unambiguous in context.

- H1168 / H3427 (those who dwell in Lev-kamai, 51:1): "inhabitants of Chaldea" in M/T.

- H4717 (מַפָּץ / mappēṣ, battle-axe, 51:20): "hammer/battle-axe" — the noun means a
  war-club or hammer; the metaphor in vv20-23 is God using an unidentified agent (probably
  Babylon, or Israel, or Cyrus — the identity is deliberately left open) as his instrument
  of universal destruction. L: "war-hammer"; M: "battle-axe"; T: "hammer of war."

- H2091 (זָהָב, gold, 51:7): "golden cup" — L: "a golden cup"; M: "a golden cup";
  T: "a cup of gold." The metaphor is that Babylon was the LORD's own instrument, given to
  the nations to make them drunk with judgment; now the cup is shattered.

- H6354 (פַּחַת, pit) / H6341 (פַּח, snare) / H6343 (פַּחַד, terror/dread): not in ch 51
  directly — unlike ch 48 these do not appear; no special decision needed.

- H8074 (שַׁמָּה / šammâ, horror/desolation, 51:37, 41, 43): "horror" in L/M; T: "a ruin
  fit for horror." The word signals total desolation beyond ordinary ruination.

- H7622 (שְׁבוּת / šĕbût, "restore the fortunes," 51:52 does not appear): no decision needed.

- H1166 (בַּעַל / Bel, 51:44): Bel (= Marduk) is Babylon's chief deity. Named without gloss.
  The imagery of Bel "disgorging" what he swallowed (v44) picks up v34's dragon-devouring
  metaphor. T makes the connection explicit.

- H4853 (מַשָּׂא, "burden/oracle"): ch 51 uses standard oracle-introduction formulas
  (כֹּה אָמַר / "thus says"). No direct maśśāʾ heading, so no special decision.

- Deportation statistics (52:28-30): Unique to Jeremiah — three deportations with exact
  numbers, unlike 2 Kings 25 which gives only the third. The numbers are lower than
  popular estimates and likely count only adult males of military or administrative
  significance. L/M render the numbers exactly as given; T notes this is a register document.

- 52:1-34 is the historical appendix, largely parallel to 2 Kings 25 and 2 Kings 24:18-20.
  The chapter is not Jeremiah's composition but was appended to contextualise the book's
  conclusion. Tone in T: clear narrative prose, slightly elevated — the appendix functions
  as a somber verification that everything the prophet warned came to pass.

- "Nebuchadrezzar" (52:4, 12, etc.): the Babylonian form of the name (Nabû-kudurri-uṣur),
  preferred in Jeremiah over the slightly variant "Nebuchadnezzar" of 2 Kings. Preserved
  as "Nebuchadrezzar" in L/M; T: "Nebuchadrezzar" consistently.

OT intertextuality:
- 51:15-16 = verbatim repetition of Jer 10:12-13 (the creation hymn). The hymn appears
  mid-oracle to contrast the living God who made everything with Babylon's dead idols
  (vv17-18). In T this repetition is noted as deliberate — it is the theological hinge
  of the oracle: Babylon's power is derivative; the Creator's power is absolute.
- 51:20-23 echoes Ps 2:9 (the nations shattered like pottery) and Isa 10:5-15 (the axe
  does not boast against the one who wields it). The battle-axe passage holds the same
  irony: the instrument of destruction will itself be destroyed (v24).
- 51:25 — "destroying mountain" ironically inverts Zion-as-mountain imagery. Zion is
  the holy mountain; Babylon is the destroyer-mountain. But the "burnt mountain" fate
  echoes volcanic imagery and the reversal of Babel's tower-building ambition (Gen 11).
- 51:27 — Ararat, Minni, Ashkenaz are the northern highland kingdoms (Armenian region)
  that formed the core of the Median coalition that sacked Babylon in 539 BCE under Cyrus.
  The summons echoes the divine council's mobilisation of nations in Isa 13:2-5.
- 51:34 — "He swallowed me like a monster (H8577, tannîn)": the dragon/sea-monster
  imagery. Babylon is the chaos-beast that devoured Judah. The LORD's response (v44)
  is to make Bel disgorge — a reversal of the cosmic swallowing. Echoes Ps 74:13-14
  and the Exodus sea-monster defeat.
- 51:41 — "Sheshach" (atbash for Babel) appears also at 25:26. The cipher may be
  deliberate concealment for political safety, or a literary device marking Babylon
  as the ultimate target of all the oracles.
- 51:44 — Bel/Marduk's humiliation echoes Isa 46:1-2 (Bel bows down, Nebo stoops).
- 51:53 — "Though Babylon mount up to heaven" echoes Gen 11:4 (Babel — the tower
  that tried to reach heaven). The judgment of ch 51 is the cosmic answer to Gen 11.
- 51:64 — "Thus far are the words of Jeremiah" is the book's original colophon before
  the ch 52 appendix was added. It signals the close of the prophetic collection.
- 52:28-30 — The three-deportation register is unique to Jeremiah. It counts 4,600 persons
  total across the seventh year (605 BCE), eighteenth year (597 BCE), and twenty-third
  year (582 BCE) of Nebuchadrezzar — the last deportation likely following Gedaliah's
  assassination (Jer 41).
- 52:31-34 — The release of Jehoiachin by Evil-merodach (Amel-Marduk) in 561 BCE is
  confirmed by Babylonian cuneiform ration tablets. The book ends not with destruction
  but with this small mercy: a king of David's line eating at a Babylonian king's table.
  T surfaces the theological resonance: the Davidic line is not extinct.
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


JEREMIAH = {
  "51": {
    "1": {
      "L": "Thus says the LORD: Behold, I am raising up against Babylon and against the inhabitants of Lev-kamai a destroying wind.",
      "M": "Thus says the LORD: See, I am raising up against Babylon and against the people of Chaldea a destructive wind.",
      "T": "This is what Yahweh says: I am sending a destroying wind against Babylon — against those who dwell in Chaldea."
    },
    "2": {
      "L": "And I will send against Babylon fanners who shall winnow her; they shall empty her land when they come against her from every side on the day of disaster.",
      "M": "I will send against Babylon men who will winnow her and strip her land bare; they will come against her from every side on the day of calamity.",
      "T": "I will send threshers against Babylon — men who will winnow her clean and leave her land empty. They will come at her from every direction when disaster falls."
    },
    "3": {
      "L": "Let the archer bend his bow against him who bends; let him rise up against him in his coat of mail. Do not spare her young men; devote to destruction her whole army.",
      "M": "Against him who strings his bow, let the archer draw against him; against him who stands up in his armor. Do not spare her young men; put her whole army under the ban.",
      "T": "Let the archer draw against the one who draws. Let the warrior rise against the armored fighter. Spare none of Babylon's young men — consecrate her whole force to destruction."
    },
    "4": {
      "L": "The slain shall fall in the land of the Chaldeans and the pierced-through in her streets.",
      "M": "The slain will fall in the land of the Chaldeans, and those run through with the sword in her streets.",
      "T": "The dead will lie across Chaldea's land, the sword-pierced in her streets."
    },
    "5": {
      "L": "For Israel and Judah are not forsaken by their God, the LORD of hosts, though their land is full of guilt before the Holy One of Israel.",
      "M": "For Israel and Judah have not been abandoned by their God, the LORD of hosts — even though their land is filled with sin against the Holy One of Israel.",
      "T": "Israel and Judah have not been abandoned by their God, Yahweh of hosts — even though their land is saturated with guilt before Israel's Holy God."
    },
    "6": {
      "L": "Flee from the midst of Babylon and let each man save his life; do not perish in her iniquity, for this is the time of the LORD's vengeance; he is repaying her what she deserves.",
      "M": "Flee from the heart of Babylon! Let each person save his life — do not be cut off in her punishment, for this is the LORD's time for vengeance, the payback he is giving her.",
      "T": "Get out of Babylon! Flee now — save your life! Do not be swept away in the punishment she deserves. This is Yahweh's hour of vengeance; he is paying her back in full."
    },
    "7": {
      "L": "Babylon was a golden cup in the LORD's hand, making all the earth drunk; the nations drank of her wine — therefore the nations have gone mad.",
      "M": "Babylon was a gold cup in the LORD's hand that made the whole earth drunk; the nations drank of her wine, and so the nations have gone mad.",
      "T": "Babylon was a cup of gold in Yahweh's hand — it made the whole earth drunk. The nations drank from it and went out of their minds."
    },
    "8": {
      "L": "Suddenly Babylon has fallen and been broken; wail for her! Take balm for her pain — perhaps she may be healed.",
      "M": "Suddenly Babylon has fallen and is shattered; wail for her! Bring balm for her wound — perhaps she can be healed.",
      "T": "Babylon has suddenly fallen — shattered. Wail for her! Bring medicine for her wound. Perhaps she can be healed."
    },
    "9": {
      "L": "We tried to heal Babylon but she was not healed. Forsake her and let us each go to his own land, for her judgment has reached up to heaven and has been lifted up to the very skies.",
      "M": "We tried to heal Babylon, but she could not be healed. Leave her behind — let each of us return to his own land, for her sentence has reached up to the heavens and extends to the clouds.",
      "T": "We tried to heal Babylon — she cannot be healed. Abandon her. Let every man go back to his own country. Her sentence has piled up to heaven itself, stacked to the very skies."
    },
    "10": {
      "L": "The LORD has brought forth our vindication. Come, let us declare in Zion the work of the LORD our God.",
      "M": "The LORD has established our acquittal. Come, let us announce in Zion what the LORD our God has done.",
      "T": "Yahweh has made our case good — he has vindicated us. Come, let us proclaim in Zion what Yahweh our God has done."
    },
    "11": {
      "L": "Sharpen the arrows! Take up the shields! The LORD has stirred up the spirit of the kings of the Medes, for his purpose against Babylon is to destroy it, because it is the vengeance of the LORD — the vengeance for his temple.",
      "M": "Polish the arrows! Fill the quivers! The LORD has roused the resolve of the kings of the Medes, for his plan is to lay Babylon waste — it is the LORD's vengeance, vengeance for his temple.",
      "T": "Sharpen the arrows! Fill the quivers! Yahweh has stirred the resolve of the Median kings — his plan is to ruin Babylon completely. This is Yahweh's vengeance — payback for what was done to his temple."
    },
    "12": {
      "L": "Raise a banner against the walls of Babylon; strengthen the watch; station the guards; prepare the ambushes; for the LORD has both planned and done what he spoke concerning the inhabitants of Babylon.",
      "M": "Raise the battle standard against the walls of Babylon! Reinforce the watch! Post the sentries! Prepare the ambushes! For the LORD has planned and carried out exactly what he decreed against the people of Babylon.",
      "T": "Plant the battle standard at Babylon's walls. Strengthen the watch. Post the guards. Set the ambushes. Yahweh has done exactly what he planned — everything he said about Babylon's people he is now carrying out."
    },
    "13": {
      "L": "O you who dwell by many waters, rich in treasures: your end has come, the thread of your life is cut.",
      "M": "You who live beside great waters and are loaded with treasures — your end has come, the cord of your existence is cut.",
      "T": "You who sit on many waters, fat with treasure — your end has come. The cord of your life has been cut through."
    },
    "14": {
      "L": "The LORD of hosts has sworn by himself: Surely I will fill you with men as with a swarm of locusts, and they shall raise a shout against you.",
      "M": "The LORD of hosts has sworn by himself: I will certainly fill you with men like a locust swarm, and they will raise a war cry against you.",
      "T": "Yahweh of hosts has sworn by his own life: I will pour men over you like a swarm of locusts, and they will shout their war cry against you."
    },
    "15": {
      "L": "It is he who made the earth by his power, who established the world by his wisdom, and by his understanding stretched out the heavens.",
      "M": "He made the earth by his power; he established the world by his wisdom and stretched out the heavens by his understanding.",
      "T": "He is the one who made the earth by his power, set the world in place by his wisdom, and stretched out the heavens by his understanding."
    },
    "16": {
      "L": "When he utters his voice there is a tumult of waters in the heavens, and he makes the mist rise from the ends of the earth; he makes lightning for the rain and brings forth the wind from his storehouses.",
      "M": "When he speaks, the waters in the heavens roar; he makes clouds rise from the ends of the earth; he makes lightning to go with the rain and releases the wind from his storehouses.",
      "T": "When he speaks, the heavens churn with water. He lifts clouds from the far edges of the earth, sends lightning with the rain, and lets the wind loose from his own storehouses."
    },
    "17": {
      "L": "Every man is stupid and without knowledge; every goldsmith is put to shame by his idol, for his cast image is a lie, and there is no breath in them.",
      "M": "Every person is too ignorant to understand this; every goldsmith is shamed by his idol, for his cast image is a fraud, and there is no breath in them.",
      "T": "Every human being is too dull to grasp this. Every idol-maker is put to shame by what he made — his poured image is a lie, a thing with no breath in it at all."
    },
    "18": {
      "L": "They are worthless, a work of delusion; at the time of their reckoning they shall perish.",
      "M": "They are a sham — the product of deception; when their day of judgment comes, they will be destroyed.",
      "T": "They are nothing — products of illusion. When the time of their reckoning comes, they will be swept away."
    },
    "19": {
      "L": "Not like these is the Portion of Jacob, for he is the one who formed all things; Israel is the tribe of his inheritance — the LORD of hosts is his name.",
      "M": "The Portion of Jacob is not like these, for he is the maker of everything; Israel is the tribe that belongs to him — the LORD of hosts is his name.",
      "T": "The God of Jacob is nothing like these idols. He made everything that exists. Israel is his own inheritance, his chosen people — Yahweh of hosts is his name."
    },
    "20": {
      "L": "You are my war-hammer and weapon of war: with you I shatter nations; with you I destroy kingdoms;",
      "M": "You are my battle-axe and weapon of war: with you I break nations to pieces; with you I demolish kingdoms;",
      "T": "You are my hammer of war, my weapon of destruction — with you I shatter nations, with you I break kingdoms apart;"
    },
    "21": {
      "L": "with you I shatter the horse and his rider; with you I shatter the chariot and its charioteer;",
      "M": "with you I break the horse and his rider; with you I break the chariot and its driver;",
      "T": "with you I shatter the horse and rider, with you I break apart the chariot and the one who drives it;"
    },
    "22": {
      "L": "with you I shatter man and woman; with you I shatter old man and youth; with you I shatter young man and young woman;",
      "M": "with you I break man and woman; with you I break the old and the young; with you I break the young man and the young woman;",
      "T": "with you I shatter man and woman, old man and boy, young man and girl;"
    },
    "23": {
      "L": "with you I shatter the shepherd and his flock; with you I shatter the farmer and his team; with you I shatter governors and commanders.",
      "M": "with you I break the shepherd and his flock; with you I break the farmer and his team; with you I break governors and commanders.",
      "T": "with you I shatter the shepherd and his flock, the farmer and his oxen, governors and commanders alike."
    },
    "24": {
      "L": "I will repay Babylon and all the inhabitants of Chaldea before your very eyes for all the evil they have done in Zion, declares the LORD.",
      "M": "I will pay back Babylon and all who live in Chaldea for everything they have done wrong in Zion — and you will see it with your own eyes, declares the LORD.",
      "T": "I will pay Babylon and all of Chaldea back in full for what they did to Zion — and you will watch it happen, declares Yahweh."
    },
    "25": {
      "L": "Behold, I am against you, O destroying mountain, declares the LORD, you who destroy the whole earth; I will stretch out my hand against you and roll you down from the crags and make you a burnt mountain.",
      "M": "I am against you, O mountain of ruin, declares the LORD — you who bring destruction on the whole earth. I will reach out my hand against you and roll you down from the rocks and turn you into a scorched mountain.",
      "T": "I am against you, destroying mountain — you who have ruined the whole earth, declares Yahweh. I will stretch out my hand against you, roll you down from your rocky height, and make you a blackened, burned-out mountain."
    },
    "26": {
      "L": "No stone shall be taken from you for a corner and no stone for a foundation, but you shall be a perpetual waste, declares the LORD.",
      "M": "No stone from you will be used for a cornerstone or a foundation — you will be a ruin forever, declares the LORD.",
      "T": "Not one stone of you will ever be taken for a cornerstone or a foundation. You will be a ruin for ever, declares Yahweh."
    },
    "27": {
      "L": "Raise a standard in the land! Blow a trumpet among the nations! Consecrate the nations against her; summon against her the kingdoms of Ararat, Minni, and Ashkenaz; appoint a commander against her; bring up horses like bristling locusts.",
      "M": "Raise a battle standard in the land! Sound the trumpet among the nations! Prepare the nations for war against her; summon against her the kingdoms of Ararat, Minni, and Ashkenaz; appoint a marshal against her; send up horses like a dense locust swarm.",
      "T": "Raise the battle standard across the land! Sound the trumpet among the nations! Mobilize the nations against her. Call up Ararat, Minni, and Ashkenaz against her. Appoint a commander. Bring horses thick as bristling locusts."
    },
    "28": {
      "L": "Consecrate the nations against her — the kings of the Medes, their governors and all their deputies, and every land under their dominion.",
      "M": "Prepare the nations for war against her — the kings of the Medes, with their governors and all their officials, and every land under their rule.",
      "T": "Mobilize the nations against her — the Median kings with their governors and officials, every territory they rule."
    },
    "29": {
      "L": "The land trembles and writhes, for the purposes of the LORD against Babylon stand firm — to make the land of Babylon a desolation, without inhabitant.",
      "M": "The land shakes and quakes, for the LORD's plans against Babylon hold firm — to turn the land of Babylon into a wasteland with no one living in it.",
      "T": "The land shudders and twists in pain, for Yahweh's plans against Babylon are fixed: to make it a wasteland where no one lives."
    },
    "30": {
      "L": "The warriors of Babylon have ceased to fight; they stay in their strongholds; their strength has failed; they have become like women; her buildings are set on fire; her bars are broken.",
      "M": "Babylon's soldiers have stopped fighting; they sit in their fortresses; their strength has drained away; they have become like women. Her buildings are set ablaze; her gate-bars are shattered.",
      "T": "Babylon's warriors have stopped fighting. They crouch in their fortresses, their strength gone — they have become like women. Her buildings are burning. Her gate-bars are broken."
    },
    "31": {
      "L": "One runner runs to meet another and one messenger to meet another, to tell the king of Babylon that his city is taken on every side;",
      "M": "One runner runs to meet another, one messenger to meet the next, to report to the king of Babylon that his city has been captured from every direction;",
      "T": "Messenger after messenger runs to report to the king of Babylon — runner meets runner, courier meets courier — bringing the word: your city has fallen on every side;"
    },
    "32": {
      "L": "the fords have been seized, the marshes are set on fire, and the soldiers are thrown into a panic.",
      "M": "the river crossings have been seized, the reed thickets set on fire, and the soldiers are in a panic.",
      "T": "the river crossings are cut off, the marshes are burning, and the soldiers are in full panic."
    },
    "33": {
      "L": "For thus says the LORD of hosts, the God of Israel: The daughter of Babylon is like a threshing floor at the time when it is trodden; yet a little while and the time of her harvest will come.",
      "M": "For this is what the LORD of hosts, the God of Israel, says: Daughter Babylon is like a threshing floor at the time of treading; the time to harvest her is coming very soon.",
      "T": "For this is what Yahweh of hosts, the God of Israel, says: Daughter Babylon is like a threshing floor at harvest time — the grain is being trodden. Just a little while more, and the time for her own harvest will come."
    },
    "34": {
      "L": "Nebuchadrezzar the king of Babylon has devoured me, he has crushed me; he has made me an empty vessel; he has swallowed me like a monster; he has filled his belly with my delicacies; he has rinsed me out.",
      "M": "Nebuchadrezzar the king of Babylon has eaten me up and crushed me; he has set me aside as an empty jar; he has swallowed me like a dragon and filled his stomach with my good things, then flushed me out.",
      "T": "Nebuchadrezzar king of Babylon devoured me and crushed me. He made me into an empty jar. He swallowed me like a sea-dragon, gorged himself on my best things, and spat me out empty."
    },
    "35": {
      "L": "\"The violence done to me and to my flesh be upon Babylon,\" shall the inhabitant of Zion say; \"My blood be upon the inhabitants of Chaldea,\" shall Jerusalem say.",
      "M": "\"The violence done to me and my family be upon Babylon,\" the people of Zion will say; \"My blood be on the people of Chaldea,\" Jerusalem will say.",
      "T": "\"Let the violence done to me and mine fall on Babylon,\" Zion's people will say. \"Let my blood be on Chaldea's head,\" Jerusalem will say."
    },
    "36": {
      "L": "Therefore thus says the LORD: Behold, I will plead your cause and take vengeance for you. I will dry up her sea and make her springs dry.",
      "M": "Therefore this is what the LORD says: I will defend your case and take vengeance on your behalf. I will drain her sea and make her springs run dry.",
      "T": "Therefore this is what Yahweh says: I will argue your case. I will take vengeance for you. I will drain Babylon's sea dry and stop her springs from flowing."
    },
    "37": {
      "L": "And Babylon shall become a heap of ruins, a haunt of jackals, a horror and a hissing, without inhabitant.",
      "M": "Babylon will become a heap of rubble, a den for jackals, an object of horror and scorn, with no one living there.",
      "T": "Babylon will become a rubble-heap — a den for jackals, a place so ruined it will make people shudder and hiss, empty of every living soul."
    },
    "38": {
      "L": "They shall roar together like lions; they shall growl like lion cubs.",
      "M": "They roar together like lions; they snarl like young lions.",
      "T": "They will roar together like lions, snarling like lion cubs."
    },
    "39": {
      "L": "While they are heated I will prepare their feast and make them drunk, that they may rejoice and then sleep a perpetual sleep and not wake up, declares the LORD.",
      "M": "While they are roused and hot, I will set a feast for them and make them drunk so that they celebrate — then sleep a permanent sleep and never wake up, declares the LORD.",
      "T": "When they are at full heat, I will set a banquet before them and make them drunk — let them celebrate for a moment — and then they will fall into a sleep from which they will never rise, declares Yahweh."
    },
    "40": {
      "L": "I will bring them down like lambs to the slaughter, like rams with male goats.",
      "M": "I will bring them down like lambs to the slaughter, like rams and male goats.",
      "T": "I will lead them to slaughter like lambs — like rams and goats going to the knife."
    },
    "41": {
      "L": "How is Sheshach taken! How is the praise of the whole earth seized! How has Babylon become a horror among the nations!",
      "M": "How Sheshach has been captured! How the celebrated city of all the earth has been seized! How Babylon has become a horror among the nations!",
      "T": "Sheshach — Babylon itself — is taken! The city the whole earth praised is seized! How has Babylon become a thing of horror among the nations!"
    },
    "42": {
      "L": "The sea has come up over Babylon; she is covered with its tumultuous waves.",
      "M": "The sea has surged over Babylon; she is swamped by its roaring waves.",
      "T": "The sea has risen over Babylon — she is buried under its crashing, roaring waves."
    },
    "43": {
      "L": "Her cities have become a horror, a dry and desolate land, a land where no one dwells, and through which no son of man passes.",
      "M": "Her cities are a wasteland, a parched and desert land — a land where nobody lives, where no one passes through.",
      "T": "Her cities are horror and ruin — a cracked, empty desert where no one lives and no traveler passes through."
    },
    "44": {
      "L": "And I will punish Bel in Babylon and take out of his mouth what he has swallowed up; the nations shall no longer flow to him. The wall of Babylon has fallen.",
      "M": "I will call Bel of Babylon to account and make him disgorge what he has swallowed; the nations will no longer stream to him. The wall of Babylon has collapsed.",
      "T": "I will punish Bel in Babylon and make him vomit out what he has swallowed — all the plunder gorged from the nations. They will no longer stream to him in tribute. The wall of Babylon has fallen."
    },
    "45": {
      "L": "Go out from her, my people! Let each man save his life from the fierce anger of the LORD!",
      "M": "Come out from her, my people — let everyone escape to save his life from the LORD's burning anger!",
      "T": "Come out of her, my people! Save your lives from Yahweh's burning anger!"
    },
    "46": {
      "L": "Let not your heart be faint, and be not afraid at the report that is heard in the land; when a report comes in one year and again a report in another year, and violence is in the land, and ruler rises against ruler —",
      "M": "Do not lose heart or be afraid at the rumors that spread through the land — when one report comes in one year and another in the next, with violence spreading and ruler fighting ruler —",
      "T": "Do not lose heart. Do not be terrified at the rumors sweeping the land — one report coming this year, another the next, with violence everywhere and rulers fighting rulers —"
    },
    "47": {
      "L": "therefore, behold, the days are coming when I will punish the idols of Babylon, and her whole land shall be put to shame, and all her slain shall fall in her midst.",
      "M": "therefore the days are surely coming when I will judge Babylon's idols, and her whole land will be disgraced, and all her dead will lie fallen in her midst.",
      "T": "know this: the days are coming when I will call Babylon's idols to account. Her whole land will be shamed, and her dead will lie where they fell — inside her."
    },
    "48": {
      "L": "Then the heavens and the earth and all that is in them shall shout for joy over Babylon, for the destroyers shall come against her from the north, declares the LORD.",
      "M": "Then the heavens and the earth and everything in them will shout for joy over Babylon, for her destroyers will come at her from the north, declares the LORD.",
      "T": "Then heaven and earth and everything in them will break into shouts of joy over Babylon — for her destroyers will sweep down from the north, declares Yahweh."
    },
    "49": {
      "L": "Babylon must fall for the slain of Israel, even as for Babylon have fallen the slain of all the earth.",
      "M": "Babylon must fall for the sake of Israel's slain, just as at Babylon the slain of all the earth have fallen.",
      "T": "Babylon must fall for the sake of Israel's dead — just as all the earth's dead fell because of Babylon."
    },
    "50": {
      "L": "You who have escaped the sword, go — do not stand still! Remember the LORD from far away, and let Jerusalem come into your mind:",
      "M": "You who have escaped the sword, go — do not linger! Remember the LORD from far off, and keep Jerusalem in your thoughts:",
      "T": "You who survived the sword — go, don't stand there! Remember Yahweh from far away. Let Jerusalem fill your minds:"
    },
    "51": {
      "L": "\"We are ashamed, for we have heard reproach; dishonor has covered our faces, for foreigners have come into the holy places of the LORD's house.\"",
      "M": "\"We are disgraced, for we have heard insults; shame has covered our faces, because foreigners have entered the sacred rooms of the LORD's temple.\"",
      "T": "\"We are shamed — we have heard the mockery. Dishonor has covered our faces. Foreigners have walked into the holy places of Yahweh's house.\""
    },
    "52": {
      "L": "Therefore, behold, the days are coming, declares the LORD, when I will punish her images, and through all her land the wounded shall groan.",
      "M": "Therefore the days are coming, declares the LORD, when I will call her idols to account, and throughout her whole land the mortally wounded will groan.",
      "T": "But those days are coming, declares Yahweh — I will call her idols to account, and from one end of Babylon to the other the dying will groan."
    },
    "53": {
      "L": "Though Babylon should mount up to heaven and though she should fortify her lofty stronghold, yet destroyers shall come against her from me, declares the LORD.",
      "M": "Even if Babylon were to climb up to heaven and reinforce her towering heights, destroyers would still come against her from me, declares the LORD.",
      "T": "Even if Babylon climbed up to heaven itself — even if she fortified the very heights — destroyers would still come from me against her, declares Yahweh."
    },
    "54": {
      "L": "A sound of crying from Babylon! The noise of great destruction from the land of the Chaldeans!",
      "M": "Listen — a cry from Babylon! A sound of great ruin from the land of the Chaldeans!",
      "T": "Hear it — a shriek from Babylon! The crash of catastrophic destruction from Chaldea!"
    },
    "55": {
      "L": "For the LORD is laying Babylon waste and silencing her great voice, and their waves roar like many waters; the noise of their clamor is lifted up.",
      "M": "For the LORD is destroying Babylon and silencing her loud voice; the invading waves roar like great waters as the uproar of their shouting rises.",
      "T": "Yahweh is ravaging Babylon and silencing her roar. The attacking waves crash like a flood, and the shout of the assault rises to the sky."
    },
    "56": {
      "L": "For a destroyer has come against her, against Babylon; her warriors are captured, their bows are shattered, for the LORD is a God of recompense — he will surely repay.",
      "M": "For a destroyer has come against her — against Babylon. Her warriors are taken prisoner; their bows are broken in pieces, for the LORD is a God of retribution — he will certainly pay back in full.",
      "T": "The destroyer has come against Babylon. Her soldiers are captured. Their bows are snapped. For Yahweh is a God of payback — he always repays."
    },
    "57": {
      "L": "I will make drunk her princes and her wise men, her governors and her commanders and her warriors; they shall sleep a perpetual sleep and not wake up, declares the King, whose name is the LORD of hosts.",
      "M": "I will make her officials and her wise men drunk — her governors, commanders, and soldiers. They will sleep a permanent sleep and never wake up, declares the King, whose name is the LORD of hosts.",
      "T": "I will make drunk every one of Babylon's officials and sages, her governors and commanders and soldiers. They will fall into a sleep they will never wake from — declares the King whose name is Yahweh of hosts."
    },
    "58": {
      "L": "Thus says the LORD of hosts: The broad wall of Babylon shall be leveled to the ground and her high gates shall be burned with fire; the peoples exhaust themselves for nothing, the nations weary themselves for fire.",
      "M": "This is what the LORD of hosts says: Babylon's wide walls will be demolished to the ground and her towering gates set on fire. The peoples have worn themselves out for nothing; the nations have exhausted themselves for fuel.",
      "T": "This is what Yahweh of hosts says: Babylon's massive walls will be leveled and her great gates burned to the ground. All the labor of the peoples will come to nothing — the nations have worked themselves to exhaustion for fuel."
    },
    "59": {
      "L": "The word that Jeremiah the prophet commanded Seraiah son of Neriah son of Mahseiah, when he went with Zedekiah king of Judah to Babylon in the fourth year of his reign. Seraiah was the quartermaster.",
      "M": "This is the message that the prophet Jeremiah entrusted to Seraiah son of Neriah son of Mahseiah, when he accompanied King Zedekiah of Judah to Babylon in Zedekiah's fourth year. Seraiah was the chief quartermaster.",
      "T": "This is the commission Jeremiah the prophet gave to Seraiah son of Neriah son of Mahseiah, when he traveled with King Zedekiah of Judah to Babylon in the fourth year of his reign. Seraiah was the head quartermaster."
    },
    "60": {
      "L": "Jeremiah wrote in a single scroll all the disaster that would come upon Babylon — all these words written concerning Babylon.",
      "M": "Jeremiah wrote in one scroll all the calamity that would come upon Babylon — all of these words about Babylon.",
      "T": "Jeremiah wrote out in a single scroll everything that would come upon Babylon — every word recorded here."
    },
    "61": {
      "L": "And Jeremiah said to Seraiah: When you come to Babylon, see that you read aloud all these words.",
      "M": "Jeremiah told Seraiah: When you arrive in Babylon, make sure you read all these words aloud.",
      "T": "Jeremiah instructed Seraiah: When you reach Babylon, read every one of these words aloud."
    },
    "62": {
      "L": "Then say: O LORD, you yourself have spoken against this place to cut it off, so that nothing shall dwell in it — neither man nor beast — and it shall be desolate forever.",
      "M": "Then say: O LORD, you have pronounced judgment on this place, to cut it off so that nothing will live here — neither human nor animal — and it will lie desolate forever.",
      "T": "Then say: O Yahweh, you yourself declared this place finished — cut off so completely that neither person nor animal will ever live here again. It will be desolate forever."
    },
    "63": {
      "L": "When you finish reading this scroll, tie a stone to it and throw it into the midst of the Euphrates,",
      "M": "When you have finished reading this scroll, tie a stone to it and throw it into the middle of the Euphrates,",
      "T": "When you finish reading the scroll, tie a stone to it and fling it into the middle of the Euphrates."
    },
    "64": {
      "L": "and say: Thus shall Babylon sink — to rise no more — because of the disaster that I am bringing upon it; and they shall become exhausted. Thus far are the words of Jeremiah.",
      "M": "and say: So will Babylon sink and not rise again, because of the disaster I am bringing on it. They will become weary. Thus far the words of Jeremiah.",
      "T": "Then say: This is how Babylon will sink — never to rise again — because of the disaster I am bringing upon it. They will sink exhausted. Here ends the word of Jeremiah."
    }
  },
  "52": {
    "1": {
      "L": "Zedekiah was twenty-one years old when he became king, and he reigned eleven years in Jerusalem. His mother's name was Hamutal daughter of Jeremiah of Libnah.",
      "M": "Zedekiah was twenty-one years old when he became king, and he reigned eleven years in Jerusalem. His mother's name was Hamutal daughter of Jeremiah, from Libnah.",
      "T": "Zedekiah was twenty-one years old when he came to the throne and reigned eleven years in Jerusalem. His mother was Hamutal daughter of Jeremiah of Libnah."
    },
    "2": {
      "L": "And he did what was evil in the sight of the LORD, according to all that Jehoiakim had done.",
      "M": "He did what was evil in the sight of the LORD, just as Jehoiakim had done.",
      "T": "He did what was evil in Yahweh's eyes, following Jehoiakim's example exactly."
    },
    "3": {
      "L": "For because of the anger of the LORD it came to pass in Jerusalem and Judah, until he had cast them out from his presence. And Zedekiah rebelled against the king of Babylon.",
      "M": "For it was because of the LORD's anger that all this happened to Jerusalem and Judah, until he finally expelled them from his presence. And Zedekiah rebelled against the king of Babylon.",
      "T": "All of this — Jerusalem, Judah — came about through the anger of Yahweh, until at last he drove them out of his presence. Then Zedekiah rebelled against the king of Babylon."
    },
    "4": {
      "L": "In the ninth year of his reign, in the tenth month, on the tenth day of the month, Nebuchadrezzar king of Babylon came with all his army against Jerusalem and besieged it; and they built a siege wall against it all around.",
      "M": "In the ninth year of Zedekiah's reign, on the tenth day of the tenth month, Nebuchadrezzar king of Babylon marched against Jerusalem with his entire army and laid siege to it; they built a siege ramp around it on every side.",
      "T": "In the ninth year of his reign, on the tenth day of the tenth month, Nebuchadrezzar king of Babylon came with his whole army against Jerusalem and laid siege to it, throwing up earthworks against it on every side."
    },
    "5": {
      "L": "So the city was under siege until the eleventh year of King Zedekiah.",
      "M": "The city remained under siege until the eleventh year of King Zedekiah.",
      "T": "The city remained besieged all the way to the eleventh year of Zedekiah's reign."
    },
    "6": {
      "L": "On the ninth day of the fourth month the famine was severe in the city, so that there was no food for the people of the land.",
      "M": "By the ninth day of the fourth month the famine in the city had become so severe that there was no food left for the people of the land.",
      "T": "By the ninth day of the fourth month the famine gripping the city was catastrophic — there was nothing left to eat for any of the people."
    },
    "7": {
      "L": "Then a breach was made in the city wall, and all the soldiers fled and went out from the city by night by the way of the gate between the two walls by the king's garden, while the Chaldeans were around the city; and they went in the direction of the Arabah.",
      "M": "Then a breach was made in the city wall, and all the soldiers fled, leaving the city at night through the gate between the two walls near the king's garden, even though the Chaldeans had the city surrounded. They headed toward the Arabah.",
      "T": "Then the wall was breached. Every soldier fled — slipping out of the city in the dark through the gate between the two walls beside the king's garden, even with the Chaldeans surrounding the city on every side. They headed for the Jordan Valley."
    },
    "8": {
      "L": "But the army of the Chaldeans pursued the king and overtook Zedekiah in the plains of Jericho, and all his army scattered from him.",
      "M": "But the Chaldean army pursued the king and caught up with Zedekiah in the plains of Jericho, and all his troops deserted him.",
      "T": "The Chaldean army gave chase and caught Zedekiah in the plains of Jericho. His entire army had scattered and left him."
    },
    "9": {
      "L": "Then they captured the king and brought him up to the king of Babylon at Riblah in the land of Hamath, and he pronounced judgment on him.",
      "M": "They seized the king and brought him to the king of Babylon at Riblah in the land of Hamath, where sentence was passed on him.",
      "T": "They seized Zedekiah and brought him to the king of Babylon at Riblah in the land of Hamath, where judgment was pronounced on him."
    },
    "10": {
      "L": "The king of Babylon slaughtered the sons of Zedekiah before his eyes, and also slaughtered all the officials of Judah at Riblah.",
      "M": "The king of Babylon killed Zedekiah's sons before his eyes, and had all the officials of Judah executed at Riblah as well.",
      "T": "The king of Babylon had Zedekiah's sons killed before his eyes, and all the officials of Judah were executed at Riblah as well."
    },
    "11": {
      "L": "He then put out the eyes of Zedekiah, bound him in bronze fetters, and the king of Babylon brought him to Babylon and put him in prison until the day of his death.",
      "M": "Then he blinded Zedekiah, bound him in bronze shackles, and the king of Babylon brought him to Babylon where he was kept in prison until the day he died.",
      "T": "Then Nebuchadrezzar put out Zedekiah's eyes, bound him in bronze chains, brought him to Babylon, and kept him in prison until he died."
    },
    "12": {
      "L": "In the fifth month, on the tenth day of the month — that was the nineteenth year of King Nebuchadrezzar, king of Babylon — Nebuzaradan the captain of the guard, who served the king of Babylon, entered Jerusalem.",
      "M": "On the tenth day of the fifth month — which was the nineteenth year of King Nebuchadrezzar of Babylon — Nebuzaradan the commander of the imperial guard, who served the king of Babylon, arrived in Jerusalem.",
      "T": "On the tenth day of the fifth month, in the nineteenth year of Nebuchadrezzar king of Babylon, Nebuzaradan, captain of the guard and personal servant of the king, arrived in Jerusalem."
    },
    "13": {
      "L": "And he burned the house of the LORD, the king's palace, and all the houses of Jerusalem; every great house he burned with fire.",
      "M": "He set fire to the house of the LORD, the royal palace, and all the houses of Jerusalem — every important building he burned to the ground.",
      "T": "He burned the house of Yahweh, the royal palace, and every house in Jerusalem — every significant building reduced to ash."
    },
    "14": {
      "L": "And all the army of the Chaldeans, who were with the captain of the guard, tore down all the walls around Jerusalem.",
      "M": "The entire Chaldean army under the captain of the guard tore down all the walls surrounding Jerusalem.",
      "T": "The whole Chaldean force serving under the captain of the guard demolished every wall surrounding Jerusalem."
    },
    "15": {
      "L": "And Nebuzaradan the captain of the guard carried into exile some of the poorest of the people, the rest of the people who remained in the city, the deserters who had gone over to the king of Babylon, and the rest of the craftsmen.",
      "M": "Nebuzaradan the captain of the guard deported some of the poorest of the people, the survivors remaining in the city, those who had defected to the king of Babylon, and the rest of the skilled workers.",
      "T": "Nebuzaradan deported some of the poorest remaining in the city, those who had deserted to Babylon, and whatever skilled craftsmen were left."
    },
    "16": {
      "L": "But Nebuzaradan the captain of the guard left behind some of the poorest of the land to be vinedressers and farmers.",
      "M": "But Nebuzaradan the captain of the guard left behind the very poorest of the land to work the vineyards and fields.",
      "T": "Nebuzaradan left behind only the poorest of the poor — people to tend the vineyards and work the fields."
    },
    "17": {
      "L": "The bronze pillars that were in the house of the LORD, and the stands and the bronze sea that were in the house of the LORD — the Chaldeans broke these in pieces and carried all the bronze to Babylon.",
      "M": "The Chaldeans smashed the bronze pillars that stood in the LORD's temple, along with the movable stands and the bronze sea, and carried all the bronze off to Babylon.",
      "T": "The Chaldeans smashed the bronze pillars, the bronze stands, and the great bronze sea that stood in Yahweh's house, and hauled all the bronze to Babylon."
    },
    "18": {
      "L": "And the pots, the shovels, the snuffers, the basins, the dishes, and all the bronze vessels used in the temple service — they took away.",
      "M": "They also took away the pots, shovels, snuffers, sprinkling bowls, incense dishes, and all the bronze utensils used in worship.",
      "T": "They stripped out every bronze utensil of the temple service: the pots, shovels, snuffers, sprinkling bowls, incense dishes — everything."
    },
    "19": {
      "L": "The captain of the guard took away the small bowls, the fire pans, the basins, the pots, the lampstands, the dishes, and the libation bowls — what was gold the captain took as gold, and what was silver he took as silver.",
      "M": "The captain of the guard carried off the small bowls, fire pans, basins, pots, lampstands, incense dishes, and drink-offering bowls — everything gold he took as gold, everything silver as silver.",
      "T": "The captain of the guard took everything else — the small bowls, fire pans, basins, pots, lampstands, incense dishes, and libation bowls. Gold items he took as gold; silver items as silver."
    },
    "20": {
      "L": "The two pillars, the one sea and the twelve bronze bulls under the sea, and the movable stands that King Solomon had made for the house of the LORD — the bronze of all these vessels was beyond weighing.",
      "M": "The two pillars, the single sea with its twelve bronze bulls underneath, and the movable stands that King Solomon had made for the LORD's temple — the bronze in all of these was too great to weigh.",
      "T": "The two great pillars, the bronze sea with its twelve bronze bulls beneath it, and the movable stands that Solomon had made for Yahweh's house — all this bronze was beyond measuring."
    },
    "21": {
      "L": "As for the pillars, the height of one pillar was eighteen cubits, its circumference was twelve cubits, and its thickness was four fingers; it was hollow.",
      "M": "Each pillar was eighteen cubits tall with a circumference of twelve cubits; it was four fingers thick and hollow.",
      "T": "Each pillar stood eighteen cubits high with a circumference of twelve cubits — four fingers thick, and hollow inside."
    },
    "22": {
      "L": "A capital of bronze was on top of it; the height of the one capital was five cubits, with a network and pomegranates all around the capital, all of bronze; the second pillar was the same, with pomegranates.",
      "M": "On top of each was a bronze capital five cubits high, decorated all around with bronze latticework and pomegranates. The second pillar was the same, also with pomegranates.",
      "T": "Each pillar was crowned with a bronze capital five cubits high, encircled all around with bronze latticework and pomegranates. The second pillar was identical."
    },
    "23": {
      "L": "There were ninety-six pomegranates on the open sides; all the pomegranates were one hundred on the surrounding lattice.",
      "M": "There were ninety-six pomegranates visible on the sides; altogether one hundred pomegranates hung on the surrounding lattice.",
      "T": "Ninety-six pomegranates could be seen from the sides; the full count on the surrounding lattice was one hundred."
    },
    "24": {
      "L": "The captain of the guard took Seraiah the chief priest, Zephaniah the second priest, and the three doorkeepers.",
      "M": "The captain of the guard arrested Seraiah the chief priest, Zephaniah the deputy priest, and the three gatekeepers.",
      "T": "The captain of the guard arrested Seraiah the chief priest, Zephaniah the deputy priest, and the three men who kept the threshold."
    },
    "25": {
      "L": "From the city he took an officer who had been in charge of the soldiers, and seven men of the king's council who were found in the city, and the secretary of the army commander who mustered the people of the land, and sixty men of the people of the land who were found inside the city.",
      "M": "From the city he took one officer who had commanded the soldiers, seven royal advisers who were found there, the secretary of the army commander who conscripted troops, and sixty ordinary citizens found in the city.",
      "T": "From the city he seized an officer who had commanded the troops, seven of the king's advisers who were still in the city, the secretary in charge of military conscription, and sixty ordinary citizens found there."
    },
    "26": {
      "L": "Nebuzaradan the captain of the guard took them and brought them to the king of Babylon at Riblah.",
      "M": "Nebuzaradan the captain of the guard took them all to the king of Babylon at Riblah.",
      "T": "Nebuzaradan brought all of them to the king of Babylon at Riblah."
    },
    "27": {
      "L": "And the king of Babylon struck them down and put them to death at Riblah in the land of Hamath. So Judah went into exile out of its land.",
      "M": "There the king of Babylon had them all struck down and executed at Riblah in the land of Hamath. So Judah was carried into exile from its land.",
      "T": "There at Riblah in Hamath the king of Babylon had every one of them executed. So Judah was driven from its land into exile."
    },
    "28": {
      "L": "This is the number of the people whom Nebuchadrezzar carried into exile: in the seventh year, three thousand and twenty-three people of Judah.",
      "M": "This is the count of those Nebuchadrezzar deported: in the seventh year, 3,023 Judeans.",
      "T": "Here is the register of those Nebuchadrezzar carried into exile: in his seventh year, 3,023 Judeans."
    },
    "29": {
      "L": "In the eighteenth year of Nebuchadrezzar he carried into exile from Jerusalem eight hundred and thirty-two persons.",
      "M": "In Nebuchadrezzar's eighteenth year he deported from Jerusalem 832 persons.",
      "T": "In his eighteenth year, 832 persons from Jerusalem."
    },
    "30": {
      "L": "In the twenty-third year of Nebuchadrezzar, Nebuzaradan the captain of the guard carried into exile of the Judeans seven hundred and forty-five persons. All the persons were four thousand and six hundred.",
      "M": "In Nebuchadrezzar's twenty-third year, Nebuzaradan the captain of the guard deported 745 Judeans. The total was 4,600 persons.",
      "T": "In his twenty-third year, Nebuzaradan carried away 745 more Judeans. The total for all three deportations: 4,600 persons."
    },
    "31": {
      "L": "And in the thirty-seventh year of the exile of Jehoiachin king of Judah, in the twelfth month, on the twenty-fifth day of the month, Evil-merodach king of Babylon, in the year he began to reign, lifted up the head of Jehoiachin king of Judah and brought him out of prison.",
      "M": "In the thirty-seventh year of Jehoiachin king of Judah's exile, on the twenty-fifth day of the twelfth month, Evil-merodach king of Babylon, in the first year of his reign, showed favor to Jehoiachin king of Judah and released him from prison.",
      "T": "In the thirty-seventh year of Jehoiachin's exile — on the twenty-fifth day of the twelfth month — Evil-merodach king of Babylon, in the very year he took the throne, showed mercy to Jehoiachin king of Judah and brought him out of prison."
    },
    "32": {
      "L": "He spoke kindly to him and set his throne above the thrones of the kings who were with him in Babylon.",
      "M": "He treated him with respect and gave him a seat of honor above the other captive kings in Babylon.",
      "T": "He spoke kindly to him and gave him a place of honor higher than all the other captive kings in Babylon."
    },
    "33": {
      "L": "So Jehoiachin changed his prison garments, and he ate bread regularly before him all the days of his life.",
      "M": "So Jehoiachin changed out of his prison clothes and ate regularly at the king's table for the rest of his life.",
      "T": "Jehoiachin exchanged his prison clothes for royal clothing and ate at the king's table every day for the rest of his life."
    },
    "34": {
      "L": "And for his daily allowance, a regular allowance was given to him by the king of Babylon — a portion for each day — until the day of his death, all the days of his life.",
      "M": "As for his food allowance, a regular daily portion was granted him by the king of Babylon, every day until his death, for all the remaining days of his life.",
      "T": "A daily provision was assigned to him by the king of Babylon — a fixed portion each day — for every remaining day of his life until he died. The Davidic line was not extinguished."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'jeremiah')
        merge_tier(existing, JEREMIAH, tier_key)
        save(tier_dir, 'jeremiah', existing)
    print('Jeremiah 51–52 written.')

if __name__ == '__main__':
    main()
