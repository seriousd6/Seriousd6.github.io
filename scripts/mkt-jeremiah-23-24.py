"""
MKT Jeremiah chapters 23–24 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-jeremiah-23-24.py

Translation decisions (consistent with mkt-jeremiah-1-3.py through mkt-jeremiah-19-22.py):

- H3068 (יהוה): "LORD" in L/M throughout; "Yahweh" in T where personal-name force is
  significant — oracle delivery, divine soliloquy, address to the prophet, response
  to lament. Narrative formulas use "Yahweh" in T for immediacy.

- H7462 (רָעָה, rō'îm, "shepherds/pastors"): rendered "shepherds" in L/M. In 23:1-4 the
  shepherds are the kings and rulers of Israel and Judah — the shepherd-king metaphor
  is standard ANE royal ideology, and Jeremiah inverts it against the failing monarchy.
  The T tier surfaces this explicitly: "rulers" = "shepherds" — both terms in play.

- H6780 (צֶמַח, tsemakh, "Branch"): 23:5 — the messianic title. Rendered "Branch" in all
  three tiers (capital B), consistent with its technical usage in Jer 33:15, Zech 3:8, 6:12.
  This is not a generic botanical word here but a royal-messianic term coined by Jeremiah.

- H6664+H3068 (יהוה צִדְקֵנוּ, "THE LORD OUR RIGHTEOUSNESS"): 23:6 — rendered in L as
  the all-caps transliterated name to signal its character as a divine name-title. In M:
  "The LORD Our Righteousness." In T: "Yahweh-Tsidkenu — Yahweh is our righteousness."
  The Hebrew name encodes both the promise and the critique: Zedekiah's name means
  "Yahweh is righteous," but the coming king will embody what Zedekiah failed to be.

- H4853 (מַשָּׂא, maśśāʾ, "burden/oracle"): 23:33-40 — the critical wordplay section.
  The word means both "load/burden" and "prophetic oracle." The false prophets use it
  as a badge ("Yahweh's burden = our oracle"), so Yahweh turns the word against them:
  "You are the burden and I will cast you off." L renders "burden" consistently to preserve
  the pun. M renders "burden" where the physical sense is active, "oracle" where the
  prophetic sense is active. T unpacks the entire pun in each verse.

- H2472 (חֲלֹום, khălôm, "dream"): 23:25-32 — the dream vs. word contrast. The false
  prophets claim divine dreams; Yahweh contrasts their straw with the fire of his word.
  Rendered "dream" in all tiers consistently.

- H6951 (עֵצָה) / H4853 wordplay: 23:18, 22 — "standing in the counsel/council of the
  LORD" — different from the "burden/oracle" H4853 pun. H5475 (סוֹד, sôd) = "council/
  intimate assembly." Rendered "council" (divine assembly) in all tiers.

- H8384 (תְּאֵנָה, te'ênâ, "figs"): ch. 24 — the central sign-act metaphor. Two baskets
  of figs represent the exiles (good figs) and Zedekiah's party (bad figs). The word for
  "bad/naughty" figs (H7451, rā') is the same root used for "evil" throughout Jeremiah.
  The T tier surfaces this: "rotten figs" = the people whose evil has made them unfit.

- H3820 (לֵב, lēb, "heart"): 24:7 — "I will give them a heart to know me." The heart
  in Hebrew thought is the seat of will, understanding, and decision — not merely feeling.
  Rendered "heart" in L/M; T surfaces the volitional sense: "capacity to know."

- H7725 (שׁוּב, šûb, "return/turn"): 24:7 — "they shall return to me with their whole
  heart." The great covenant-return word throughout Jeremiah; rendered "return" in L/M;
  T: "come back" for naturalness while retaining the directional force.

- H3045 (יָדַע, yāda', "know"): 24:7 — "to know that I am the LORD" — covenant knowing,
  not merely cognitive. As in 22:16: knowing Yahweh is enacted, not just acknowledged.
  T surfaces this: "to truly know."

- H3068 pattern continuity: 23:6 "says the LORD" and "the LORD Our Righteousness" — the
  divine name appears in the very messianic title, an ironic contrast with Zedekiah whose
  name means "the LORD is righteous" but who failed to practice it.

Textual and structural notes:

- 23:1-4 — Woe oracle against shepherds (= rulers/kings). The passage opens with an "Ah!"
  (H1945, hôy) lament-curse against the whole shepherding class. Picks up from ch. 22's
  royal indictments. The promise of a new shepherd-king (v. 4) leads directly to the
  explicit messianic oracle of vv. 5-6.

- 23:5-6 — The Righteous Branch oracle. One of the clearest pre-exilic messianic texts.
  The Branch (Heb. tsemakh) will "reign wisely" (H7919, śākal — to be prudent, to prosper
  through wisdom) — quite the opposite of the kings just indicted. The divine name given
  to this king echoes but inverts Zedekiah: the coming king will be what Zedekiah was not.

- 23:7-8 — The new Exodus oracle. In the coming age, the defining salvation event will not
  be the Exodus from Egypt but the return from exile (the "north country" = Babylon). This
  parallels Isa 43:18-19 ("remember not the former things").

- 23:9-40 — The false-prophet polemic. The longest sustained attack on false prophecy in
  the Hebrew Bible. Three waves: vv. 9-15 (Jeremiah's anguish; comparing prophets of
  Samaria and Jerusalem); vv. 16-22 (warning not to heed them; the divine council test);
  vv. 23-32 (the dream-versus-word contrast; Yahweh's omniscience); vv. 33-40 (the "burden"
  pun — a sustained ironic deconstruction of prophetic speech).

- 23:18 — "the council (sôd) of the LORD": this is the heavenly assembly/divine court, not
  merely "counsel" (advice). The test of true prophecy: has the prophet stood in that
  assembly and received an actual commission? (See 1 Kgs 22:19-22; Isa 6; Job 1-2.)

- 23:29 — "Is not my word like fire... and like a hammer?" — the two images are
  complementary: fire consumes, the hammer fractures solid rock. The living word is
  irresistible force; the dream-words of false prophets are straw by comparison.

- 23:33-40 — The maśśāʾ pun: the word means both "prophetic oracle" and "heavy burden/
  load." When the people keep demanding "What is the LORD's oracle?" (i.e., what exciting
  new word do you have for us?), Yahweh answers: you yourselves are the burden — the
  weight I am going to fling off. The prophets abused the term; it is therefore banned
  and replaced with direct discourse ("What did the LORD say? What did the LORD answer?").

- 24:1-10 — The Two Baskets of Figs. A vision dated to shortly after the first deportation
  (597 BCE, the exile of Jehoiachin/Jeconiah). Counterintuitively, the "good figs" are
  the exiles — those already taken — while the "bad figs" are those who remained with
  Zedekiah or fled to Egypt. The theological point: exile is not Yahweh's abandonment but
  his redemptive removal; staying in the land under false security is the real catastrophe.
  24:7 — "a heart to know me" anticipates the new covenant promise of 31:31-34.

OT intertextuality:
- 23:5 — "righteous Branch" echoes and grounds Zech 3:8; 6:12 (both depend on this text).
- 23:7-8 — parallels Isa 43:18-19; the new-exodus motif recurs in the Book of Consolation
  (Jer 30-33).
- 23:14 — "like Sodom... like Gomorrah": echoes Gen 18-19; Isa 1:9-10. Jerusalem's moral
  collapse makes the Sodom comparison apt.
- 23:19 — "storm / whirlwind of the LORD": picks up the theophanic storm language of Amos
  1:14; Nah 1:3; anticipates the whirlwind of Ezek 1:4.
- 24:7 — "they shall be my people and I will be their God" — the covenant formula of Gen
  17:7-8; Exod 6:7; Lev 26:12; picked up in Jer 31:33; Ezek 36:28; Rev 21:3.
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
  "23": {
    "1": {
      "L": "Woe to the shepherds who destroy and scatter the sheep of my pasture! says the LORD.",
      "M": "Woe to the shepherds who destroy and scatter the sheep of my pasture! declares the LORD.",
      "T": "Doom on the rulers who ravage and scatter my flock! — Yahweh's word."
    },
    "2": {
      "L": "Therefore thus says the LORD, the God of Israel, against the shepherds who feed my people: You have scattered my flock and have driven them away, and have not visited them; behold, I will visit upon you the evil of your doings, says the LORD.",
      "M": "Therefore thus says the LORD, the God of Israel, concerning the shepherds who tend my people: You have scattered my flock and driven them away, and have not cared for them. So I am calling you to account for your evil deeds, declares the LORD.",
      "T": "This is what Yahweh, the God of Israel, says against the rulers who tend my people: You scattered my flock, drove them away, and never looked after them. Now I am coming after you for what you have done. Yahweh declares it."
    },
    "3": {
      "L": "And I myself will gather the remnant of my flock from all the countries where I have driven them, and will bring them back to their fold, and they shall be fruitful and increase.",
      "M": "I myself will gather the remnant of my flock from all the lands where I have driven them, bring them back to their pasture, and they will be fruitful and multiply.",
      "T": "But I — I myself — will gather what remains of my scattered flock from every land where I drove them, bring them home to their pasture, and they will thrive and grow."
    },
    "4": {
      "L": "And I will raise up over them shepherds who will feed them, and they shall fear no more, neither be dismayed, and none shall be lacking, says the LORD.",
      "M": "I will raise up shepherds who will truly care for them; they will no longer be afraid or terrified, and none will be lost, declares the LORD.",
      "T": "I will appoint over them true shepherds who will actually tend them — then the flock will know no more fear or panic, and not one sheep will be missing. Yahweh's promise."
    },
    "5": {
      "L": "Behold, the days are coming, says the LORD, when I will raise up to David a righteous Branch, and a King shall reign and prosper, and shall execute justice and righteousness in the earth.",
      "M": "The days are coming, declares the LORD, when I will raise up for David a righteous Branch who will reign wisely and establish justice and righteousness in the land.",
      "T": "Days are coming — Yahweh declares it — when I will cause a righteous Branch to spring from David's line. He will reign wisely, and justice and righteousness will define his rule over the land."
    },
    "6": {
      "L": "In his days Judah shall be saved and Israel shall dwell safely; and this is his name whereby he shall be called: THE LORD OUR RIGHTEOUSNESS.",
      "M": "In his days Judah will be saved and Israel will live in safety. This is the name by which he will be called: The LORD Our Righteousness.",
      "T": "Under his reign Judah will be rescued and Israel will live secure. The name he will bear is this: Yahweh-Tsidkenu — Yahweh is our righteousness."
    },
    "7": {
      "L": "Therefore behold, the days are coming, says the LORD, when they shall say no more, As the LORD lives who brought up the children of Israel out of the land of Egypt,",
      "M": "So the days are coming, declares the LORD, when no one will say any longer, 'As the LORD lives who brought the Israelites up from the land of Egypt,'",
      "T": "The time is coming — Yahweh declares it — when no one will invoke the old oath: 'As Yahweh lives who brought Israel up from Egypt.'"
    },
    "8": {
      "L": "but, As the LORD lives who brought up and who led the seed of the house of Israel out of the north country and out of all countries where I had driven them; and they shall dwell in their own land.",
      "M": "but, 'As the LORD lives who brought up the descendants of Israel from the north country and from all the lands where he had driven them.' And they will live in their own land.",
      "T": "Instead the oath will be: 'As Yahweh lives who brought back the offspring of Israel from the north and from all the scattered lands where he had driven them.' And they will live again on their own soil."
    },
    "9": {
      "L": "Concerning the prophets: My heart is broken within me; all my bones shake; I am like a drunken man, like a man whom wine has overcome, because of the LORD and because of the words of his holiness.",
      "M": "Concerning the prophets: My heart is broken within me; all my bones tremble. I am like a drunken man, like a man overcome by wine, because of the LORD and his holy words.",
      "T": "Turning now to the prophets — I am shattered inside; every bone in me shakes. I stagger like someone drunk on wine, overwhelmed, because of what Yahweh has revealed in all his holiness."
    },
    "10": {
      "L": "For the land is full of adulterers; because of the curse the land mourns; the pleasant pastures of the wilderness are dried up; their course is evil and their force is not right.",
      "M": "For the land is full of adulterers. Because of the curse the land mourns; the wilderness pastures are dried up. Their ways are wicked and their power is misused.",
      "T": "The land is overrun with covenant-breakers. Because of this great curse the land is in mourning — the wilderness meadows have shriveled. Their conduct is corrupt from start to finish."
    },
    "11": {
      "L": "For both prophet and priest are profane; yea, in my house have I found their wickedness, says the LORD.",
      "M": "Both prophet and priest are godless; even in my own house I have found their wickedness, declares the LORD.",
      "T": "Prophet and priest alike — both are corrupt. I have uncovered their evil practices even inside my own temple. Yahweh's word."
    },
    "12": {
      "L": "Therefore their way shall be unto them as slippery paths in the darkness; they shall be driven on and fall therein; for I will bring evil upon them, even the year of their visitation, says the LORD.",
      "M": "Therefore their path will be like slippery ground in the darkness; they will be driven stumbling along it and fall; for I will bring disaster on them in the year of their reckoning, declares the LORD.",
      "T": "So their road leads nowhere but a dark, slick path — they are pushed along it until they fall. The year of their reckoning is coming, when I bring ruin down on them. Yahweh declares it."
    },
    "13": {
      "L": "And I have seen folly in the prophets of Samaria; they prophesied by Baal and caused my people Israel to err.",
      "M": "In the prophets of Samaria I saw a repulsive thing: they prophesied by Baal and led my people Israel astray.",
      "T": "What I saw in Samaria's prophets was revolting enough — they spoke in Baal's name and led Israel off course."
    },
    "14": {
      "L": "I have seen also in the prophets of Jerusalem a horrible thing: they commit adultery and walk in lies; they strengthen also the hands of evildoers, that none returns from his wickedness; they are all of them unto me as Sodom, and the inhabitants thereof as Gomorrah.",
      "M": "But in the prophets of Jerusalem I have seen something even more horrible: they commit adultery and live by lies; they encourage evildoers so that no one turns from his evil. To me they have all become like Sodom, their inhabitants like Gomorrah.",
      "T": "But Jerusalem's prophets are worse — I have seen something truly monstrous among them. They commit adultery, traffic in lies, and shore up wrongdoers so that no one changes course. Before me they have become another Sodom, their people another Gomorrah."
    },
    "15": {
      "L": "Therefore thus says the LORD of hosts concerning the prophets: Behold, I will feed them with wormwood and make them drink the water of gall; for from the prophets of Jerusalem profaneness has gone out into all the land.",
      "M": "Therefore thus says the LORD of hosts concerning the prophets: I am going to feed them wormwood and give them poisoned water to drink, for from the prophets of Jerusalem ungodliness has spread throughout all the land.",
      "T": "So this is what Yahweh of hosts says about those prophets: I will feed them bitter poison and make them drink toxic water — because it was Jerusalem's prophets who exported their corruption to the whole land."
    },
    "16": {
      "L": "Thus says the LORD of hosts: Hearken not unto the words of the prophets that prophesy unto you; they make you vain; they speak a vision of their own heart, and not out of the mouth of the LORD.",
      "M": "This is what the LORD of hosts says: Do not listen to the prophets who are prophesying to you. They are filling you with false hopes; they speak visions from their own imagination, not from the mouth of the LORD.",
      "T": "Yahweh of hosts says this: Stop listening to those prophets who speak to you. They are feeding you delusions — what comes out of their mouths is their own invention, not a word from Yahweh."
    },
    "17": {
      "L": "They say still unto every one that walketh after the imagination of his own heart: No evil shall come upon you; and to every one that despiseth the word of the LORD they say: It shall be well with you.",
      "M": "They keep telling those who follow the stubbornness of their own heart, 'No disaster will come upon you'; and to everyone who despises the word of the LORD they say, 'It shall be well with you.'",
      "T": "To those going their own stubborn way they keep promising, 'Nothing bad is coming.' To those who reject Yahweh's word they whisper, 'Everything will be fine.'"
    },
    "18": {
      "L": "For who hath stood in the council of the LORD and hath perceived and heard his word? Who hath listened and hath heard?",
      "M": "For which of them has stood in the LORD's council to see and hear his word? Who has listened and actually heard?",
      "T": "But has a single one of them ever stood in Yahweh's divine council — seen and heard what passes there? Has even one truly listened?"
    },
    "19": {
      "L": "Behold, a whirlwind of the LORD has gone forth in fury, even a grievous whirlwind; it shall fall grievously upon the head of the wicked.",
      "M": "Behold, the storm of the LORD! His wrath has gone out, a swirling tempest; it will fall violently on the head of the wicked.",
      "T": "Look — the storm of Yahweh is already unleashed! His fury sweeps forward like a howling whirlwind, bearing down on the heads of the wicked."
    },
    "20": {
      "L": "The anger of the LORD shall not return until he have executed and till he have performed the thoughts of his heart; in the latter days ye shall understand it perfectly.",
      "M": "The LORD's anger will not turn back until he has accomplished the purposes of his heart. In the latter days you will understand it clearly.",
      "T": "Yahweh's anger will not relent until every purpose of his heart is carried out to the last detail. When those days arrive, you will look back and understand fully."
    },
    "21": {
      "L": "I have not sent these prophets, yet they ran; I have not spoken to them, yet they prophesied.",
      "M": "I did not send these prophets, yet they went running; I did not speak to them, yet they prophesied.",
      "T": "I never commissioned those prophets, yet off they went. I never spoke to them, yet words poured from their mouths."
    },
    "22": {
      "L": "But if they had stood in my counsel and had caused my people to hear my words, then they should have turned them from their evil way and from the evil of their doings.",
      "M": "But if they had stood in my council and proclaimed my words to my people, they would have turned them from their evil ways and evil deeds.",
      "T": "If they had truly stood in my council and spoken my actual words, my people would have turned — turned from the evil road they are on, turned from the wreckage of their ways."
    },
    "23": {
      "L": "Am I a God at hand, says the LORD, and not a God afar off?",
      "M": "Am I only a God nearby, declares the LORD, and not a God far away?",
      "T": "Do they imagine I am only a local God, a nearby presence they can outmaneuver? Am I not the God of the far distance too? — Yahweh asks."
    },
    "24": {
      "L": "Can any hide himself in secret places that I shall not see him? says the LORD. Do not I fill heaven and earth? says the LORD.",
      "M": "Can anyone hide in secret places where I cannot see him? declares the LORD. Do I not fill heaven and earth? declares the LORD.",
      "T": "Is there any hiding place deep enough that I cannot see what goes on there? Yahweh asks. Heaven and earth — do I not fill them both?"
    },
    "25": {
      "L": "I have heard what the prophets said, that prophesy lies in my name, saying: I have dreamed, I have dreamed.",
      "M": "I have heard what the prophets are saying who prophesy lies in my name: 'I have dreamed, I have dreamed!'",
      "T": "I have heard what those prophets keep announcing — the ones who peddle lies under my name: 'I had a dream! I had a dream!'"
    },
    "26": {
      "L": "How long shall this be in the heart of the prophets that prophesy lies? Yea, they are prophets of the deceit of their own heart,",
      "M": "How long shall there be lies in the heart of these prophets who prophesy falsehood, who prophesy the deceit of their own hearts?",
      "T": "How long will this go on? Lying at the core, prophesying out of their own wishful hearts, trafficking in self-made delusion — when does it stop?"
    },
    "27": {
      "L": "who think to cause my people to forget my name by their dreams which they tell every man to his neighbour, as their fathers have forgotten my name for Baal.",
      "M": "They intend to make my people forget my name through the dreams they tell one another, just as their fathers forgot my name for Baal.",
      "T": "Their dreams are designed to erase my name from Israel's memory — they pass them around like gossip — just as their ancestors swapped my name out for Baal."
    },
    "28": {
      "L": "The prophet that hath a dream, let him tell a dream; and he that hath my word, let him speak my word faithfully. What is the chaff to the wheat? says the LORD.",
      "M": "Let the prophet who has a dream tell the dream — but let the one who has my word speak my word faithfully. What does straw have to do with wheat? declares the LORD.",
      "T": "Let the dreamer tell his dream if he likes — but the one who carries my word, let him speak that word honestly and without distortion. What does chaff have to do with wheat? Yahweh asks."
    },
    "29": {
      "L": "Is not my word like a fire? says the LORD; and like a hammer that breaketh the rock in pieces?",
      "M": "Is not my word like fire, declares the LORD, and like a hammer that shatters rock?",
      "T": "My word is fire, Yahweh says — and a hammer that breaks solid rock into pieces. Can a handful of straw compete with that?"
    },
    "30": {
      "L": "Therefore behold, I am against the prophets, says the LORD, that steal my words every one from his neighbour.",
      "M": "Therefore, I am against the prophets, declares the LORD, who steal my words from each other.",
      "T": "So I stand against those prophets — Yahweh declares it — the ones who plagiarize each other's messages and stamp my name on them."
    },
    "31": {
      "L": "Behold, I am against the prophets, says the LORD, that use their tongues and say, He saith.",
      "M": "I am against the prophets, declares the LORD, who wag their own tongues and say, 'This is what the LORD declares.'",
      "T": "I stand against the prophets — Yahweh declares it — who put their own tongues to work and then announce: 'Yahweh said it.'"
    },
    "32": {
      "L": "Behold, I am against them that prophesy false dreams, says the LORD, and do tell them, and cause my people to err by their lies, and by their lightness; yet I sent them not, nor commanded them; therefore they shall not profit this people at all, says the LORD.",
      "M": "I am against those who prophesy lying dreams, declares the LORD — who tell them and lead my people astray with their lies and their recklessness, when I neither sent them nor commissioned them. They are of no benefit whatsoever to this people, declares the LORD.",
      "T": "I stand against the false dreamers — Yahweh declares it — who pass on those dreams and drag my people into error through their lies and empty bravado. I never sent them, never gave them any commission. They offer this people nothing. Nothing at all."
    },
    "33": {
      "L": "And when this people, or the prophet, or a priest, shall ask thee, saying: What is the burden of the LORD? then shalt thou tell them: What burden? I will even forsake you, says the LORD.",
      "M": "When this people, or a prophet or a priest, asks you, 'What is the burden of the LORD?' you shall say to them, 'You are the burden, and I will cast you off, declares the LORD.'",
      "T": "When anyone — people, prophet, or priest — asks you, 'What is Yahweh's oracle?' you shall tell them: You yourselves are the burden he is carrying — and he is casting you off. Yahweh's word."
    },
    "34": {
      "L": "And as for the prophet, and the priest, and the people, that shall say, The burden of the LORD, I will even punish that man and his house.",
      "M": "As for the prophet, the priest, or any person who says 'The burden of the LORD,' I will punish that person and his household.",
      "T": "As for any prophet, priest, or ordinary person who says 'Yahweh's burden,' I will hold that person and their whole household accountable."
    },
    "35": {
      "L": "Thus shall ye say every one to his neighbour and every one to his brother: What hath the LORD answered? and, What hath the LORD spoken?",
      "M": "This is what you are to say to one another, each person to his neighbor and brother: 'What has the LORD answered?' or 'What has the LORD spoken?'",
      "T": "Instead, this is how you speak among yourselves — neighbor to neighbor, one brother to another: 'What did Yahweh say?' 'What was Yahweh's answer?'"
    },
    "36": {
      "L": "And the burden of the LORD shall ye mention no more; for every man's word shall be his burden; for ye have perverted the words of the living God, of the LORD of hosts our God.",
      "M": "You must no longer speak of 'the burden of the LORD,' for the burden is every person's own word, and you have perverted the words of the living God, the LORD of hosts, our God.",
      "T": "Stop using the phrase 'Yahweh's burden' altogether. Because what you call the burden is nothing but your own words — and in calling it Yahweh's you twist and pervert the speech of the living God, Yahweh of hosts, our God."
    },
    "37": {
      "L": "Thus shalt thou say to the prophet: What hath the LORD answered thee? and, What hath the LORD spoken?",
      "M": "And this is what you are to say to the prophet: 'What has the LORD answered you?' or 'What has the LORD spoken?'",
      "T": "When speaking to a prophet, ask it plainly: 'What did Yahweh say to you?' 'What was Yahweh's word?'"
    },
    "38": {
      "L": "But since ye say, The burden of the LORD, therefore thus says the LORD: Because ye say this word, The burden of the LORD, when I sent unto you, saying, Ye shall not say, The burden of the LORD,",
      "M": "But if you say 'the burden of the LORD,' thus says the LORD: Because you have spoken these words — 'the burden of the LORD' — when I sent word to you that you were not to say 'the burden of the LORD,'",
      "T": "Yet if you insist on saying 'Yahweh's burden' — then listen to what Yahweh says: Because you keep using that phrase after I explicitly told you not to,"
    },
    "39": {
      "L": "Therefore, behold, I, even I, will utterly forget you, and I will forsake you, and the city that I gave you and your fathers, out of my presence,",
      "M": "therefore, behold, I will surely lift you up and fling you away from my presence — you and the city I gave to you and your fathers.",
      "T": "I will hoist you up and hurl you out of my presence — you and the city I gave as a gift to you and your ancestors."
    },
    "40": {
      "L": "And I will bring an everlasting reproach upon you, and a perpetual shame, which shall not be forgotten.",
      "M": "And I will bring on you everlasting disgrace and lasting shame that will not be forgotten.",
      "T": "What follows will be an everlasting shame — a lasting, unforgettable disgrace branded into your memory and into the memory of all who come after."
    }
  },
  "24": {
    "1": {
      "L": "The LORD showed me, and behold, two baskets of figs were set before the temple of the LORD. This came to pass after Nebuchadrezzar king of Babylon had carried away captive Jeconiah the son of Jehoiakim, king of Judah, and the princes of Judah, with the craftsmen and smiths, from Jerusalem, and had brought them to Babylon.",
      "M": "The LORD showed me: there before me were two baskets of figs placed before the temple of the LORD, after Nebuchadnezzar king of Babylon had taken into exile from Jerusalem Jeconiah son of Jehoiakim, king of Judah, along with the officials of Judah and the craftsmen and metalworkers, and brought them to Babylon.",
      "T": "Yahweh gave me a vision: two baskets of figs set out before the temple. This was after Nebuchadnezzar had deported Jeconiah, son of Jehoiakim, Judah's king, together with Judah's officials, its craftsmen and metalworkers — all carried off to Babylon."
    },
    "2": {
      "L": "One basket had very good figs, like the figs that are first ripe; and the other basket had very naughty figs, which could not be eaten, they were so bad.",
      "M": "One basket had very good figs, like first-ripe figs, but the other basket had very bad figs, so rotten they could not be eaten.",
      "T": "The first basket held beautiful figs — premium, early-season fruit. The second held figs so spoiled and rotten they were utterly inedible."
    },
    "3": {
      "L": "Then said the LORD unto me: What seest thou, Jeremiah? And I said: Figs; the good figs, very good; and the evil, very evil, that cannot be eaten, they are so evil.",
      "M": "Then the LORD said to me, 'What do you see, Jeremiah?' I said, 'Figs — the good figs very good, and the bad very bad, so rotten they cannot be eaten.'",
      "T": "Then Yahweh asked me, 'What do you see, Jeremiah?' I said, 'Figs — the good ones are excellent, the bad ones are appalling, too rotten to eat.'"
    },
    "4": {
      "L": "Again the word of the LORD came to me, saying:",
      "M": "Then the word of the LORD came to me:",
      "T": "Then Yahweh's word came to me:"
    },
    "5": {
      "L": "Thus says the LORD, the God of Israel: Like these good figs, so will I acknowledge them that are carried away captive of Judah, whom I have sent out of this place into the land of the Chaldeans, for their good.",
      "M": "Thus says the LORD, the God of Israel: Like these good figs, I will look favorably on the exiles of Judah whom I sent away from this place to the land of the Chaldeans — for their good.",
      "T": "This is what Yahweh, the God of Israel, says: Like these good figs, I will treat well the exiles of Judah whom I sent out of this place to Babylonia. Yes — for their good."
    },
    "6": {
      "L": "For I will set mine eyes upon them for good, and I will bring them again to this land; and I will build them, and not pull them down; and I will plant them, and not pluck them up.",
      "M": "I will keep my eyes on them for good, and I will bring them back to this land. I will build them and not tear them down; I will plant them and not uproot them.",
      "T": "My eye will be on them for their good — I will bring them back to this land. I will build them up and not tear them down. I will plant them and never pull them out."
    },
    "7": {
      "L": "And I will give them an heart to know me, that I am the LORD; and they shall be my people, and I will be their God; for they shall return unto me with their whole heart.",
      "M": "I will give them a heart to know me, that I am the LORD. They will be my people and I will be their God, for they will return to me with all their heart.",
      "T": "And I will give them a heart to know me — to truly know that I am Yahweh. They will be my people and I will be their God, because they will come back to me with their whole heart."
    },
    "8": {
      "L": "And as the evil figs, which cannot be eaten, they are so evil — surely thus says the LORD — so will I give Zedekiah the king of Judah, and his princes, and the residue of Jerusalem, that remain in this land, and them that dwell in the land of Egypt.",
      "M": "But as for the bad figs that are so rotten they cannot be eaten — thus says the LORD — so I will treat Zedekiah king of Judah, his officials, the remnant of Jerusalem who remain in this land, and those who live in the land of Egypt.",
      "T": "But the rotten figs — the ones too spoiled to eat — that is what I will make of Zedekiah king of Judah, his officials, what remains of Jerusalem still in the land, and those who have fled to Egypt. This is Yahweh's word."
    },
    "9": {
      "L": "And I will deliver them to be removed into all the kingdoms of the earth for their hurt, to be a reproach and a proverb, a taunt and a curse, in all places whither I shall drive them.",
      "M": "I will make them a horror to all the kingdoms of the earth — a reproach, a byword, a taunt, and a curse in every place where I drive them.",
      "T": "I will make them a thing of horror throughout every kingdom on earth — a reproach and a proverb, a taunt and a curse, in every land where I scatter them."
    },
    "10": {
      "L": "And I will send the sword, the famine, and the pestilence among them, till they be consumed from off the land that I gave unto them and to their fathers.",
      "M": "And I will send the sword, famine, and pestilence against them until they are completely destroyed from the land I gave to them and to their fathers.",
      "T": "And sword, starvation, and plague — I will unleash all three until they are utterly consumed, driven from the land I gave them and their ancestors."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'jeremiah')
        merge_tier(existing, JEREMIAH, tier_key)
        save(tier_dir, 'jeremiah', existing)
    print('Jeremiah 23–24 written.')

if __name__ == '__main__':
    main()
