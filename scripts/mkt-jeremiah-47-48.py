"""
MKT Jeremiah chapters 47–48 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-jeremiah-47-48.py

Translation decisions (consistent with mkt-jeremiah-1-3.py through mkt-jeremiah-37-39.py):

- H3068 (יהוה): "LORD" in L/M throughout; "Yahweh" in T where the personal-name force is
  significant — oracle delivery, divine address, and oath-bond contexts. Narrative formulas
  ("declares the LORD") use "Yahweh" in T for immediacy.

- H430 (אֱלֹהִים): "God" throughout for the God of Israel (48:1); "gods" for Moab's
  national deity context (48:35 — "his gods"). Chemosh is named explicitly in 48:7,13,46
  and is not called "god" but "Chemosh" — the proper name carries the shame.

- H6635 (צְבָאוֹת): "hosts" in L/M; retained in T as "Yahweh of hosts" — the divine
  military-commander title frames the oracle's sovereign authority. Appears at 48:1,15.

- H5315 (נֶפֶשׁ): "lives" in 47:6 context; the idiom "save your lives" (48:6) is natural
  in all three tiers. No Hebrew soul-as-immaterial-substance is in view — only embodied
  survival.

- H7622 (שְׁבוּת / šĕbût): 48:47 "restore the fortunes of Moab" — this is the fixed idiom
  שׁוּב שְׁבוּת, not simply "bring back the captivity." The idiom means to reverse a people's
  entire plight: loss of land, honor, population. Rendered "restore the fortunes" in L/M;
  T: "reverse the fate."

- H8105 (שְׁמָרִים / šĕmārîm): "lees/sediment" in 48:11. The metaphor is of wine left
  undisturbed on its dregs — retaining full flavor but growing stale, never refined by
  hardship. L preserves the literal form; M: "dregs"; T: "sediment" with the full metaphor
  extended. This is one of Jeremiah's sharpest portraits of complacency.

- H1343/H1346/H1347 (pride vocabulary at 48:29): Three distinct Hebrew roots (gēʾût,
  gaʾăwâ, gāʾôn) together with H1363 (gōbah, loftiness) and H7312 (rûm, haughtiness).
  All five words appear in a single verse describing Moab's pride. Each is given a distinct
  English rendering in all three tiers to honor the accumulation: pride, arrogance,
  insolence, haughtiness, self-exaltation.

- H3645 (כְּמוֹשׁ / Kemôš, "Chemosh"): Moab's national deity, named without gloss.
  The shame of Chemosh going into exile (48:7) and the comparison with Bethel (48:13)
  are deliberate theological taunts: the god in whom Moab trusted will prove as useless
  as Israel's apostate cult site. In T, the irony is drawn out.

- H6807 (צְעָדָה) / H6541 (פַּרְסָה): "hoofs" and "stamping" in 47:3 — the sound of
  the Babylonian cavalry described through the visceral noise of a cavalry advance.
  L preserves the compound: "stamping of hoofs... rushing of chariots... rumbling of wheels."
  T draws out the terror: the noise alone collapses paternal care.

- H1820 (דָּמַם): "silenced/laid low" in 47:5 — Ashkelon is "silenced" (dāmam = to be
  still, cut off, destroyed). Ambiguity between "silent" and "destroyed" is real; both
  tones are present. L: "silenced"; M: "destroyed"; T: "lies silent and broken."

- H2719 (חֶרֶב): "sword" in 47:6-7 — the "sword of the LORD" is addressed directly in
  a lament-speech; the sword is personified and commanded to sheathe itself — only to be
  told it cannot rest while the LORD has appointed it. L/M: "sword"; T: surfaces the
  personification.

- H5826 (עֵזֶר): "helper" in 47:4 — cutting off every helper from Tyre and Sidon.
  Tyre and Sidon were Phoenician city-states with trade and military ties to Philistia.
  Caphtor (H3731 / כַּפְתּוֹר) is the Aegean/Cretan homeland from which the Philistines
  originally migrated (Amos 9:7; Deut 2:23). L: "remnant of the coastland of Caphtor";
  T: "last survivors from the shores of Caphtor."

- Mourning rites (47:5; 48:37): Shaving the head (baldness), cutting/gashing the hands,
  clipping the beard, wearing sackcloth — standard ANE mourning gestures. The self-gashing
  in 47:5 (H1413, gādad) is also associated with ecstatic prophetic rites (1 Kgs 18:28).
  L preserves the literal; T draws out the extent of grief.

Structural and textual notes:

- Ch. 47 — Oracle against the Philistines: one of the shortest foreign-nation oracles
  in Jeremiah (7 verses). Framed by the "word of the LORD" superscription (v1) and
  closed by the rhetorical Q&A about the sword (vv.6-7). The historical event cited
  in v1 (Pharaoh striking Gaza) is uncertain — possibly Neco II's 609 BCE campaign,
  though the grammar of v1 is debated (whether "before Pharaoh struck" means the oracle
  came prior to the strike, or that the oracle is set in that context).

- 47:2 — The "waters rising from the north" is a standard Jeremianic metaphor for Babylon
  (cf. 4:6; 6:1; 10:22). The flood imagery is not supernatural but military — the army
  overwhelming the landscape. "All the fullness" echoes Ps 24:1 (the earth's fullness
  belongs to the LORD — here claimed by conquest).

- 47:3-4 — The fathers who cannot turn back for their children: honour-shame culture
  context. The highest failure is to abandon your children in battle — but feebleness
  of hands (H7510, riphyôn) is the cause: the noise alone produces paralysis.
  This is the same idiom as the "weakening of hands" in 38:4 — courage dissolving.

- 47:6-7 — The personification of the sword is unique in Jeremiah. The sword "of the LORD"
  is addressed in lament-speech, asked to rest and sheathe itself — then denied that rest
  because the LORD himself appointed it against the seacoast. The passage shows Jeremiah's
  ambivalence: the destruction is from God, and it cannot be stopped.

- Ch. 48 — Oracle against Moab: the longest foreign-nation oracle in Jeremiah
  (47 verses) and one of the most sustained laments in the book. It draws heavily from
  Isaiah 15-16 and Numbers 21. The structure moves through: destruction of cities (vv1-10),
  the complacency metaphor (vv11-17), mourning rites and city roll (vv18-36),
  and the lament conclusion with a future restoration promise (vv37-47).

- 48:7 — "You trusted in your works and your treasures." Moab's confidence was in
  self-made prosperity and stored wealth — the antithesis of trust in Yahweh. The same
  indictment that falls on Judah in Jer 17:5-8 now falls on Moab.

- 48:10 — "Cursed is he who does the work of the LORD deceitfully, cursed is he who
  withholds his sword from blood." This disturbing verse contextualizes the destruction:
  the agents of judgment (Babylon) are themselves under obligation to execute it fully.
  Halfhearted judgment is its own sin. L preserves the stark form; T draws out the logic.

- 48:11-12 — The wine/lees metaphor is one of the book's finest images. Moab like
  undisturbed wine has never been tested, poured out, or refined. The LORD will send
  "tippers" (pōrîm — those who tilt the vessel) who will empty and shatter him.
  The play on "taste unchanged, scent unaltered" (v11) and the shattered jars (v12)
  is the contrast between false stability and violent disruption.

- 48:13 — Chemosh/Bethel parallel: the shame Israel felt at Bethel (the golden calf cult
  of Jeroboam, 1 Kgs 12:28-29) is the analogy for Moab's coming shame at Chemosh.
  Both were real trust misplaced in a god that could not deliver.

- 48:29 — The pride catalogue (five Hebrew words) is almost identical to Isa 16:6.
  The accumulation is satirical: the very excess of pride vocabulary mocks Moab's
  self-regard. T names each quality distinctly.

- 48:31-36 — The LORD weeps for Moab. This is theologically significant: Yahweh is
  not indifferent to the destruction he sends. The divine grief parallels Jeremiah's
  own grief for Judah throughout the book. The weeping "like pipes" (v36) echoes the
  mourning music of the period.

- 48:43-44 — The fear-pit-snare triad is a near-quotation of Isa 24:17-18, applying
  the same cosmic judgment language to Moab. The inescapability is the point: every
  exit is blocked.

- 48:45-46 — Quotation of Num 21:28-29 (the ancient Song of Heshbon against Moab after
  Sihon's victory). The prophetic re-use of this older war song applies an Israelite
  victory taunt to Babylon's advance. L marks the quotation; T makes the re-application
  explicit in the rendering.

- 48:47 — The promise of restoration is unexpected and genuine — not ironic. The same
  formula applies to Ammon (49:6) and Elam (49:39). Moab's fate is not final; the
  "latter days" retain a reversal. This reflects the consistent Jeremianic theology that
  the LORD's judgment is purposive, not annihilatory.

OT intertextuality:
- 47:2 — "waters rising from the north" echoes 4:6; 6:1; 10:22 (Babylon as flood).
- 47:2 — "all its fullness" echoes Ps 24:1 (earth's fullness belongs to the LORD).
- 48:6 — "be like the heath in the wilderness" echoes Jer 17:6 (same word H6176, ʿărôʿēr,
  a bare desert shrub — the opposite of Jer 17:8's tree by water).
- 48:10 — The curse on halfhearted judgment echoes 1 Sam 15:3,9 (Saul's incomplete
  devotion of Amalek — the same failure of nerve in executing judgment).
- 48:13 — Chemosh/Bethel comparison echoes Hos 10:5-6 (shame of Bethel); 1 Kgs 12:28-29.
- 48:26-27 — "As Israel was a derision to you" echoes the anti-Moab sentiment of Ps 60:8;
  83:6. Moab had mocked Israel in her weakness.
- 48:29 — The five-fold pride catalogue echoes Isa 16:6 almost verbatim.
- 48:32 — "Weeping of Jazer" echoes Isa 16:8-9 (Sibmah vine).
- 48:34 — Echoes Isa 15:4-6 (Heshbon to Elealeh; Nimrim waters).
- 48:36 — Echoes Isa 15:7; 16:11 (pipes mourning for Moab).
- 48:43-44 — Near-quotation of Isa 24:17-18 (fear-pit-snare triad).
- 48:45-46 — Quotes Num 21:28-29 (Song of Heshbon / fire from Sihon) and echoes
  Num 21:29 ("woe to you, O Moab; people of Chemosh").
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
  "47": {
    "1": {
      "L": "The word of the LORD that came to Jeremiah the prophet against the Philistines, before Pharaoh struck Gaza.",
      "M": "The word of the LORD that came to the prophet Jeremiah concerning the Philistines, before Pharaoh attacked Gaza.",
      "T": "This is Yahweh's word that came to Jeremiah the prophet against the Philistines — before Pharaoh struck Gaza."
    },
    "2": {
      "L": "Thus says the LORD: Behold, waters are rising out of the north and shall become an overflowing torrent; they shall overflow the land and all its fullness, the city and those who dwell in it. The men shall cry out and every inhabitant of the land shall howl.",
      "M": "Thus says the LORD: See, waters are rising from the north and will become an overflowing flood. They will swamp the land and everything in it — the cities and all their inhabitants. People will cry out and every inhabitant of the land will wail.",
      "T": "This is what Yahweh says: Look — waters are surging up from the north, swelling into a flood that will overwhelm the land and everything in it, every city and all its people. Men will cry out; every person in the land will wail."
    },
    "3": {
      "L": "At the noise of the stamping of the hoofs of his stallions, at the rushing of his chariots, the rumbling of his wheels, fathers shall not look back to their children from feebleness of hands —",
      "M": "At the thunder of hoofs, the charge of chariots, and the rattling of wheels, fathers will not turn back for their children — their hands go limp.",
      "T": "At the thunder of stampeding hoofs, the charge of chariots, the rattling of their wheels — fathers will not even look back for their children. Their hands hang limp in helpless dread."
    },
    "4": {
      "L": "because of the day that comes to destroy all the Philistines, to cut off from Tyre and Sidon every remaining helper; for the LORD is about to destroy the Philistines, the remnant of the coastland of Caphtor.",
      "M": "For the day has come to lay waste all the Philistines and to cut off from Tyre and Sidon every remaining ally; for the LORD is destroying the Philistines, the last remnant from the coastlands of Caphtor.",
      "T": "For the day has come for Yahweh to ruin all the Philistines and to cut off every last ally — from Tyre and Sidon there will be no help. Yahweh is destroying the Philistines, every last survivor from the shores of Caphtor."
    },
    "5": {
      "L": "Baldness has come upon Gaza; Ashkelon is silenced. O remnant of their valley, how long will you gash yourself?",
      "M": "Gaza is shaved bald; Ashkelon is destroyed. O remnant of their valley, how long will you slash yourself in grief?",
      "T": "Gaza is shaved bare; Ashkelon lies silent and broken. O you few left in the valley — how long will you go on slashing yourselves in grief?"
    },
    "6": {
      "L": "Ah, sword of the LORD! How long until you rest? Return to your scabbard; be still and cease.",
      "M": "O sword of the LORD, how long before you rest? Return to your sheath; be still and stop.",
      "T": "O sword of Yahweh — how long? When will you finally rest? Go back into your sheath. Be still. Stop."
    },
    "7": {
      "L": "But how can it rest when the LORD has commanded it? Against Ashkelon and against the seashore he has appointed it.",
      "M": "But how can it be still when the LORD has given it its charge? Against Ashkelon and the seacoast — there he has set it.",
      "T": "But how can it rest when Yahweh himself has given it its assignment? Against Ashkelon, against the seacoast — there he has sent it to its work."
    }
  },
  "48": {
    "1": {
      "L": "Concerning Moab, thus says the LORD of hosts, the God of Israel: Woe to Nebo, for it is laid waste! Kiriathaim is put to shame and taken; the fortress is put to shame and dismayed.",
      "M": "Concerning Moab, thus says the LORD of hosts, the God of Israel: Woe to Nebo, for it is devastated! Kiriathaim is shamed and seized; the stronghold is shamed and shattered.",
      "T": "Concerning Moab, this is what Yahweh of hosts, the God of Israel, says: Woe to Nebo — it is laid waste! Kiriathaim is shamed and taken. The fortress is shamed and broken."
    },
    "2": {
      "L": "The praise of Moab is no more; in Heshbon they have devised disaster against it: Come, let us cut it off from being a nation. You also, Madmen, shall be silenced; the sword shall pursue you.",
      "M": "There is no more glory for Moab. In Heshbon they have plotted its ruin: Come, let us wipe it out as a nation. You too, Madmen, will be silenced; the sword will pursue you.",
      "T": "Moab's fame is finished. In Heshbon they are plotting its end: Come — let us erase it from the roll of nations. And you, Madmen, you too will be silenced. The sword is coming after you."
    },
    "3": {
      "L": "A voice of crying from Horonaim — desolation and great destruction!",
      "M": "A cry is heard from Horonaim — ruin and terrible destruction!",
      "T": "From Horonaim comes a shriek — ruin and catastrophic destruction!"
    },
    "4": {
      "L": "Moab is broken; her little ones have cried out.",
      "M": "Moab is shattered; her young ones raise a cry.",
      "T": "Moab is shattered. Even her youngest cry aloud."
    },
    "5": {
      "L": "For at the ascent of Luhith they go up with weeping upon weeping; for at the descent to Horonaim the enemies have heard a cry of distress.",
      "M": "For on the ascent to Luhith they go up with continuous weeping; for on the road down to Horonaim the enemies hear a cry of anguish.",
      "T": "Going up to Luhith, there is nothing but weeping all the way. Going down to Horonaim, the enemy hears the shriek of ruin."
    },
    "6": {
      "L": "Flee! Save your lives and be like the juniper in the wilderness.",
      "M": "Flee! Save yourselves and be like a desert shrub in the wilderness.",
      "T": "Run! Save your lives! Be like a bare desert shrub — alone, stripped down, surviving on nothing."
    },
    "7": {
      "L": "For because you trusted in your works and in your treasures, you also shall be taken; and Chemosh shall go out into exile, his priests and his officials together.",
      "M": "For because you trusted in your own accomplishments and your stored wealth, you too will be captured; and Chemosh will go into exile together with his priests and his officials.",
      "T": "Because you put your confidence in your achievements and your accumulated wealth — you too will be seized. Chemosh will march into exile with his priests and his officials, all of them together."
    },
    "8": {
      "L": "And the destroyer shall come upon every city, and no city shall escape; the valley also shall perish and the plain shall be laid waste, as the LORD has spoken.",
      "M": "The destroyer will come to every city; not one city will escape. The valley will be ruined and the plain laid waste, exactly as the LORD has decreed.",
      "T": "The destroyer will sweep through every city. Not one will escape. The valley will be laid waste, the plain destroyed — exactly as Yahweh has spoken."
    },
    "9": {
      "L": "Give wings to Moab, that she may fly away; her cities shall become desolate with no one dwelling in them.",
      "M": "Give Moab wings so she may flee away; for her cities will become desolate with no one left to live in them.",
      "T": "Give Moab wings so she can fly — for her cities will be emptied out, no one left to dwell in them."
    },
    "10": {
      "L": "Cursed is he who does the work of the LORD deceitfully, and cursed is he who withholds his sword from blood.",
      "M": "Cursed is the one who carries out the LORD's work negligently, and cursed is the one who holds his sword back from bloodshed.",
      "T": "Cursed is the man who carries out Yahweh's work halfheartedly. Cursed is the man who pulls back his sword from blood."
    },
    "11": {
      "L": "Moab has been at ease from his youth and has settled on his lees; he has not been emptied from vessel to vessel and has not gone into exile; therefore his taste remains unchanged and his scent is not altered.",
      "M": "Moab has been undisturbed from his youth, settled quietly on his dregs. He has never been poured from vessel to vessel or sent into exile. So his flavor has stayed the same and his aroma has not changed.",
      "T": "Moab has been at ease since his youth — like wine left untouched, settled on its sediment. He has never been poured from vessel to vessel, never sent into exile. His taste is unchanged; his scent has never been stirred. He has never known what it is to be tested."
    },
    "12": {
      "L": "Therefore, behold, the days are coming, declares the LORD, when I will send tippers to him and they shall tip him; they shall empty his vessels and shatter his jars.",
      "M": "Therefore, the days are coming, declares the LORD, when I will send men to tilt him; they will pour him out and empty his vessels and smash his containers.",
      "T": "So look — days are coming, Yahweh declares, when I will send men who will tip him over. They will pour him out, drain every vessel, and smash every jar."
    },
    "13": {
      "L": "And Moab shall be put to shame because of Chemosh, as the house of Israel was put to shame because of Bethel, their confidence.",
      "M": "Then Moab will be ashamed of Chemosh, just as the house of Israel was ashamed of Bethel, the god they had relied on.",
      "T": "Moab will be shamed by Chemosh — just as the house of Israel was shamed by Bethel, the god they had counted on to save them."
    },
    "14": {
      "L": "How do you say, 'We are warriors and mighty men ready for battle'?",
      "M": "How can you claim, 'We are heroes, battle-hardened men'?",
      "T": "How can you say, 'We are warriors — men proven in battle'?"
    },
    "15": {
      "L": "Moab is laid waste and his cities have been come up against; and his finest young men have gone down to the slaughter, declares the King, whose name is the LORD of hosts.",
      "M": "Moab is devastated; his cities have been overrun; his best young men have gone down to be slaughtered — declares the King, whose name is the LORD of hosts.",
      "T": "Moab is ruined. His cities have been stormed; his finest young men have gone down to slaughter. The King speaks — and his name is Yahweh of hosts."
    },
    "16": {
      "L": "The calamity of Moab is near to come and his disaster hastens very swiftly.",
      "M": "Moab's disaster is close at hand; his ruin is coming very quickly.",
      "T": "Moab's doom is near — his ruin is racing to meet him."
    },
    "17": {
      "L": "All you who are around him, bemoan him; and all you who know his name, say: How is the mighty staff broken, the glorious rod!",
      "M": "All who surround him, mourn for him! All who know his name, say: How is the powerful scepter broken, the glorious staff!",
      "T": "All who surround him — mourn for him! All who know his name — say it: How the mighty scepter is broken! How the glorious staff lies shattered!"
    },
    "18": {
      "L": "Come down from your glory, sit in thirst, O inhabitant, daughter of Dibon; for the destroyer of Moab has come up against you and has destroyed your strongholds.",
      "M": "Come down from your glory and sit in thirst, O people of Dibon; for the destroyer of Moab has come up against you and ruined your fortresses.",
      "T": "Come down from your throne of pride and sit in thirst, daughter Dibon — the destroyer of Moab has come against you and laid your strongholds in ruins."
    },
    "19": {
      "L": "Stand by the road and watch, O inhabitant of Aroer; ask the one who flees and the one who escapes; say: What has happened?",
      "M": "Take your stand by the road and watch, O people of Aroer; question the one fleeing and the one escaping: What has happened?",
      "T": "Take your post on the road and watch, you who live in Aroer. Stop the one who flees, stop the refugee, and ask: What happened?"
    },
    "20": {
      "L": "Moab is put to shame, for it is dismayed; wail and cry out; tell it in Arnon that Moab is laid waste.",
      "M": "Moab is put to shame, for it is shattered; wail and cry! Announce it at the Arnon — Moab is destroyed.",
      "T": "Moab is shamed — broken and humiliated. Wail! Cry out! Spread the word at the Arnon: Moab is devastated."
    },
    "21": {
      "L": "Judgment has come upon the plateau — upon Holon, upon Jahzah, upon Mephaath,",
      "M": "Judgment has come to the plateau — upon Holon, upon Jahzah, upon Mephaath,",
      "T": "Judgment has come to the plateau — to Holon, to Jahzah, to Mephaath,"
    },
    "22": {
      "L": "and upon Dibon, and upon Nebo, and upon Beth-diblathaim,",
      "M": "upon Dibon, upon Nebo, upon Beth-diblathaim,",
      "T": "to Dibon, to Nebo, to Beth-diblathaim,"
    },
    "23": {
      "L": "and upon Kiriathaim, and upon Beth-gamul, and upon Beth-meon,",
      "M": "upon Kiriathaim, upon Beth-gamul, upon Beth-meon,",
      "T": "to Kiriathaim, to Beth-gamul, to Beth-meon,"
    },
    "24": {
      "L": "and upon Kerioth, and upon Bozrah, and upon all the cities of the land of Moab, far and near.",
      "M": "upon Kerioth, upon Bozrah, upon all the cities of the land of Moab, far and near.",
      "T": "to Kerioth, to Bozrah — to every city of Moab, near and far."
    },
    "25": {
      "L": "The horn of Moab is cut off and his arm is broken, declares the LORD.",
      "M": "The horn of Moab is hewn off and his arm is broken, declares the LORD.",
      "T": "Moab's horn is hacked off. His arm is broken. Yahweh declares it."
    },
    "26": {
      "L": "Make him drunk, for he magnified himself against the LORD; and Moab shall wallow in his vomit, and he also shall be in derision.",
      "M": "Make him drunk, for he has exalted himself against the LORD. Moab will wallow in his own vomit and become an object of ridicule.",
      "T": "Get him drunk — for he lifted himself up against Yahweh. Moab will reel and wallow in his own vomit, and he will become a laughingstock."
    },
    "27": {
      "L": "For was not Israel a derision to you? Was he found among thieves, that whenever you spoke of him you shook your head?",
      "M": "Was not Israel a laughingstock to you? Was he caught among thieves? For whenever you spoke of him you wagged your head.",
      "T": "Did you not mock Israel? Was he some thief caught in the act, that you wagged your head at him every time his name came up?"
    },
    "28": {
      "L": "Leave the cities and dwell in the rock, O inhabitants of Moab; be like the dove that nests in the sides of the mouth of the gorge.",
      "M": "Abandon your cities and make your home among the rocks, O people of Moab; be like the dove that builds its nest deep in the walls of a ravine.",
      "T": "Abandon your cities and take refuge in the rocky crags, O people of Moab. Be like the dove that builds its nest in the face of the gorge, deep in the cleft of the rock."
    },
    "29": {
      "L": "We have heard of the pride of Moab — he is exceedingly proud — of his arrogance and his pride and his haughtiness and the loftiness of his heart.",
      "M": "We have heard of Moab's pride — he is exceedingly arrogant — his insolence, his self-exaltation, his haughtiness, and the towering conceit of his heart.",
      "T": "We have heard of Moab's pride — and it is immense: his arrogance, his insolence, his self-exaltation, his haughtiness, the towering conceit of his heart. Five words — none of them adequate."
    },
    "30": {
      "L": "I know his insolence, declares the LORD, but it is empty; his boastings have accomplished nothing.",
      "M": "I know his arrogance, declares the LORD — but it comes to nothing; his empty boasts accomplish nothing.",
      "T": "I know his rage, declares Yahweh — but it is hollow. All his boasting amounts to nothing. It will not stand."
    },
    "31": {
      "L": "Therefore I will wail for Moab; for all of Moab I will cry out; for the men of Kir-hareseth I will mourn.",
      "M": "Therefore I will wail for Moab; I will cry out for all of Moab; I will mourn for the men of Kir-hareseth.",
      "T": "Therefore I will wail for Moab. I will cry out for all of Moab. I will mourn for the men of Kir-hareseth."
    },
    "32": {
      "L": "More than the weeping of Jazer I will weep for you, O vine of Sibmah; your branches passed over the sea, reaching to the sea of Jazer; upon your summer harvest and your vintage the destroyer has fallen.",
      "M": "I weep for you, O vine of Sibmah, with more than Jazer's own tears; your tendrils spread across the sea, reaching as far as the sea of Jazer; the destroyer has swept down on your summer fruit and your vintage.",
      "T": "O vine of Sibmah — I weep for you more than Jazer's own tears. Your branches once spread across the sea, reaching to the sea of Jazer. Now the destroyer has come crashing down on your summer harvest and your vintage."
    },
    "33": {
      "L": "Joy and gladness are taken away from the fruitful field and from the land of Moab; and I have made wine cease from the winepresses; no one treads with shouting — the shouting is no shouting.",
      "M": "Gladness and joy have been stripped from the fertile fields and from the land of Moab; I have stopped the wine from flowing in the presses; no one treads grapes with harvest shouts — the only shouting is not of joy.",
      "T": "Joy and celebration have been stripped from the fertile fields of Moab. I have silenced the wine in the presses. No one treads the grapes with harvest shouts now — the only sounds are not of joy."
    },
    "34": {
      "L": "From the cry of Heshbon to Elealeh, to Jahaz they raise their voice; from Zoar to Horonaim like a heifer of three years; for the waters of Nimrim also shall be desolate.",
      "M": "From the cry of Heshbon to Elealeh, to Jahaz they lift their voice; from Zoar to Horonaim like a three-year-old heifer's bellow; for the waters of Nimrim too will be dried up.",
      "T": "From Heshbon's cry the sound reaches Elealeh and Jahaz; from Zoar to Horonaim it rings out like the bellow of a young heifer. And even the waters of Nimrim will run dry."
    },
    "35": {
      "L": "Moreover I will cause to cease in Moab, declares the LORD, him who offers sacrifice on the high place and burns incense to his gods.",
      "M": "I will put an end in Moab, declares the LORD, to anyone who brings offerings up to the high places and burns incense to his gods.",
      "T": "I will put an end in Moab — Yahweh declares it — to every man who climbs the high places to sacrifice, to every man who burns incense to his gods."
    },
    "36": {
      "L": "Therefore my heart moans for Moab like flutes, and my heart moans like flutes for the men of Kir-hareseth; because the wealth they acquired has perished.",
      "M": "Therefore my heart wails for Moab like flutes, and my heart wails like flutes for the men of Kir-hareseth — for the riches they gathered have perished.",
      "T": "That is why my heart wails for Moab like a mourning flute — wails for the men of Kir-hareseth — for the wealth they built up is all gone."
    },
    "37": {
      "L": "For every head is bald and every beard is clipped; on all the hands are gashes and on the loins is sackcloth.",
      "M": "For every head is shaved bald and every beard is cut off; there are gashes on every hand and sackcloth around every waist.",
      "T": "Every head is shaved bare, every beard is shorn. Gashes on every hand. Sackcloth on every waist."
    },
    "38": {
      "L": "On all the housetops of Moab and in her streets everywhere is lamentation; for I have broken Moab like a vessel in which no one delights, declares the LORD.",
      "M": "On all the rooftops of Moab and in all her streets there is mourning everywhere; for I have shattered Moab like a pot no one wants, declares the LORD.",
      "T": "On every rooftop in Moab, in every street — nothing but mourning. I have smashed Moab like a vessel that no one wants. Yahweh declares it."
    },
    "39": {
      "L": "How is it shattered! How Moab has turned his back in shame! So Moab shall become a derision and a horror to all those around him.",
      "M": "How it is broken! How Moab has turned away in shame! So Moab will become an object of ridicule and terror to all the nations around him.",
      "T": "How it lies in pieces! How Moab has turned and fled in shame! So Moab becomes a mockery and a horror to every nation around him."
    },
    "40": {
      "L": "For thus says the LORD: Behold, he shall swoop like an eagle and spread his wings over Moab.",
      "M": "For thus says the LORD: See, he shall swoop down like an eagle and spread his wings over Moab.",
      "T": "For this is what Yahweh says: Watch — he swoops like an eagle and spreads his wings over Moab."
    },
    "41": {
      "L": "Kerioth is taken and the strongholds are seized; the hearts of the warriors of Moab on that day shall be like the heart of a woman in labor.",
      "M": "Kerioth is captured and the fortresses are taken; on that day the hearts of Moab's warriors will be like the heart of a woman in labor.",
      "T": "Kerioth is captured; the fortresses are seized. On that day Moab's warriors will have hearts like a woman in the grip of labor."
    },
    "42": {
      "L": "And Moab shall be destroyed as a people because he exalted himself against the LORD.",
      "M": "Moab will be destroyed as a nation because he lifted himself up against the LORD.",
      "T": "Moab will be wiped out as a people — because he exalted himself against Yahweh."
    },
    "43": {
      "L": "Fear and pit and snare are upon you, O inhabitant of Moab, declares the LORD.",
      "M": "Terror and pit and trap are upon you, O people of Moab, declares the LORD.",
      "T": "Dread and pit and snare are set against you, O people of Moab. Yahweh declares it."
    },
    "44": {
      "L": "He who flees from the fear shall fall into the pit, and he who gets up out of the pit shall be caught in the snare; for I will bring upon Moab the year of their punishment, declares the LORD.",
      "M": "Whoever flees from the terror will fall into the pit, and whoever climbs out of the pit will be caught in the snare; for I will bring upon Moab the year of their reckoning, declares the LORD.",
      "T": "Run from the dread and you fall into the pit. Climb out of the pit and the snare catches you. For I will bring upon Moab the year of their reckoning. Yahweh declares it."
    },
    "45": {
      "L": "In the shadow of Heshbon the fugitives stood without strength; for fire went forth from Heshbon and a flame from within Sihon, and it devoured the border of Moab and the crown of the head of the sons of tumult.",
      "M": "The fugitives stopped, exhausted, in the shadow of Heshbon; but fire flashed out from Heshbon and flame from within Sihon, devouring the border of Moab and the scalp of the noisy sons.",
      "T": "The refugees stopped, spent, in the shadow of Heshbon — but fire burst from Heshbon, a flame from within Sihon, devouring the frontier of Moab, the heads of the proud and noisy sons. The ancient taunt finds its fulfillment."
    },
    "46": {
      "L": "Woe to you, O Moab! The people of Chemosh are ruined; for your sons are taken captive and your daughters into captivity.",
      "M": "Woe to you, O Moab! The people of Chemosh are destroyed; your sons have been taken prisoner and your daughters led into captivity.",
      "T": "Woe to you, O Moab! The people of Chemosh are ruined — your sons hauled off as captives, your daughters marched away into exile."
    },
    "47": {
      "L": "Yet I will restore the fortunes of Moab in the latter days, declares the LORD. Thus far is the judgment of Moab.",
      "M": "Yet in the latter days I will restore the fortunes of Moab, declares the LORD. This is the end of the judgment of Moab.",
      "T": "Yet in the days to come I will reverse the fate of Moab. Yahweh declares it. This far — and no further — is the judgment of Moab."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'jeremiah')
        merge_tier(existing, JEREMIAH, tier_key)
        save(tier_dir, 'jeremiah', existing)
    print('Jeremiah 47–48 written.')

if __name__ == '__main__':
    main()
