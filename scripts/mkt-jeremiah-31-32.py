"""
MKT Jeremiah chapters 31–32 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-jeremiah-31-32.py

Translation decisions (consistent with mkt-jeremiah-1-3.py through mkt-jeremiah-28-30.py):

- H3068 (יהוה): "LORD" in L/M throughout; "Yahweh" in T — oracle delivery formulas, direct
  address, and the covenant-name force in 31:31-34 and 32:38-40. Narrative connectors retain
  "Yahweh" in T for directness.

- H3069 (אֲדֹנָי יהוה, Adonai-Yahweh): "Lord GOD" in L/M (KJV convention), "Lord Yahweh"
  in T — used in Jeremiah's prayer (32:17, 32:25). The doubled divine address signals high-
  register petition.

- H2617 (חֶסֶד): 31:3 — "lovingkindness" in L (traditional), "steadfast love" in M (modern
  standard), "covenant faithfulness" in T — foregrounding the loyalty-and-action combination
  that distinguishes chesed from mere sentiment. 32:18 same pattern.

- H1285 (בְּרִית): "covenant" throughout all three tiers. This is the central theological term
  of 31:31-34 (the New Covenant) and 32:40 (the everlasting covenant). No deviation.

- H8451 (תּוֹרָה): 31:33 — "law" in L (literal, preserves the ambiguity), "instruction" in M
  and T — emphasizing that Torah is teaching, not merely legal code. The New Covenant context
  is about internalized teaching, not imposed statute.

- H3820 (לֵב): "heart" in L/M. In T, "heart" where emotional/personal, "mind" where volitional
  (32:35 "never entered my mind"), "inner self" in 31:33 (written on their hearts = internalized).

- H5315 (נֶפֶשׁ): 31:12 "their soul shall be like a watered garden"; 31:14 "satiate the soul
  of the priests"; 32:41 "with all my soul." Rendered "soul" in L; "whole being" or "soul" in M
  depending on natural English; in T: "whole selves" / "soul" contextually.

- H6635 (צְבָאוֹת): "hosts" in L/M; retained in T — the military overtone (LORD of heaven's
  armies) is theologically weight-bearing in the restoration oracles.

- H7965 (שָׁלוֹם): not prominent in chs. 31–32 (contrast ch. 29). Not a contested issue here.

- H6226 / H5769 (עוֹלָם): "everlasting" in L/M; "unending" or "that will never end" in T —
  the eternal-covenant language of 31:3, 32:40.

- H5002 (נְאֻם): the prophetic "declares" formula — "says" in L, "declares" in M, "Yahweh
  declares it" / "Yahweh's word" in T (to keep the spoken-oracle force).

- 31:22b — "A woman encircles a man" (נְקֵבָה תְּסוֹבֵב גָּבֶר): One of the most debated
  half-verses in Jeremiah. The plain sense is sexual-social reversal: in the restoration age
  the woman pursues/envelops the warrior (reversed social order as sign of the new creation).
  Rendered literally in L ("a woman encircles a man"), naturally in M ("a woman will court a
  man"), interpretively in T ("a woman will seek out a man") — signaling the reversed world
  of restoration without over-interpreting. Noted as deliberately enigmatic.

- 31:26 — "Upon this I awoke and looked, and my sleep was pleasant": an unusual editorial
  intrusion, possibly marking the end of a night-vision sequence. Not attributed to Yahweh
  but to Jeremiah. Translated as written.

- 32:1-44 structure: The field-purchase sign-act (vv. 1–15), Jeremiah's great prayer
  (vv. 16–25), and Yahweh's extended answer (vv. 26–44). The sign-act is programmatic:
  purchasing land during a siege is prophetic theater — Jeremiah puts his money where his
  mouth is. The restoration promises in vv. 36–44 echo the New Covenant promises of ch. 31.

- "Behold, the days are coming" (H935 + H3117): recurring formula in the Book of Consolation.
  L: "Behold, the days are coming"; M: "The days are coming"; T: "Days are coming" — direct
  and declarative, allowing the content to carry the weight.

OT intertextuality:
- 31:3 — "I have drawn you with lovingkindness": echoes Hos 11:4; covenant-loyalty language.
- 31:9 — "I am a father to Israel, Ephraim is my firstborn": Exod 4:22; Hos 11:1.
- 31:15 — Rachel weeping: echoed in Matt 2:18; the northern exile as prototype for Herod's
  massacre of the innocents.
- 31:22 — "new thing in the earth": echoes Isa 43:19 ("I am doing a new thing").
- 31:29-30 — Sour grapes proverb: contested and answered also in Ezek 18.
- 31:31-34 — The New Covenant: cited verbatim in Heb 8:8-12 and 10:16-17; foundational to NT
  theology of the new covenant in Christ's blood.
- 31:33 — "I will put my law in their inward parts": resonates with Ezek 36:26-27 (new heart,
  new spirit).
- 31:34 — "I will forgive their iniquity": the ground of the covenant is divine forgiveness,
  not human performance.
- 31:35-37 — Cosmic guarantees: echoes Isa 54:9-10 (the oath never to rebuke Israel again).
- 32:17 — "Nothing too hard for you": echoes Gen 18:14 (the question to Abraham at Mamre).
- 32:27 — Yahweh's echo of Jeremiah's prayer: same phrase returned, confirmed.
- 32:37-41 — Restoration gathering: echoes Deut 30:3-5; Ezek 36:24-28.
- 32:38 — Covenant formula: Gen 17:7-8; Exod 6:7; Lev 26:12; Jer 31:33; Rev 21:3.
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
  "31": {
    "1": {
      "L": "At that time, says the LORD, I will be God to all the families of Israel, and they shall be my people.",
      "M": "At that time, declares the LORD, I will be the God of all the families of Israel, and they shall be my people.",
      "T": "At that time — Yahweh declares it — I will be God to every family of Israel. They will be my people."
    },
    "2": {
      "L": "Thus says the LORD: The people who survived the sword found grace in the wilderness — Israel, as it went to find rest.",
      "M": "Thus says the LORD: The people who survived the sword found grace in the wilderness — Israel, as it went seeking rest.",
      "T": "This is what Yahweh says: The survivors of the sword found unexpected grace out in the wilderness — Israel, trudging toward rest."
    },
    "3": {
      "L": "The LORD appeared to me from afar, saying: With an everlasting love I have loved you; therefore with lovingkindness I have drawn you.",
      "M": "The LORD appeared to me from long ago, saying: I have loved you with an everlasting love; therefore with steadfast love I have drawn you to myself.",
      "T": "From ages past Yahweh spoke to me: I have loved you with a love that has no end. That is why I have drawn you close — with covenant faithfulness that never gave up on you."
    },
    "4": {
      "L": "Again I will build you, and you shall be built, O virgin Israel; again you shall adorn yourself with your tambourines and go out in the dances of the merrymakers.",
      "M": "I will build you up again, and you will be rebuilt, O virgin Israel. Once more you will take up your tambourines and go out to join the dances of the joyful.",
      "T": "I will build you up again, Israel — you who are beloved, who have been kept. You will be rebuilt. You will pick up your tambourines and dance again with those who make merry."
    },
    "5": {
      "L": "Again you shall plant vineyards on the mountains of Samaria; the planters shall plant and shall enjoy the fruit.",
      "M": "Again you will plant vineyards on the mountains of Samaria; those who plant them will enjoy their fruit.",
      "T": "Once more vineyards will go in on the hills of Samaria. Those who plant them will live to eat the fruit with their own hands."
    },
    "6": {
      "L": "For there shall be a day when watchmen shall cry on the hills of Ephraim: Arise, and let us go up to Zion, to the LORD our God.",
      "M": "For a day is coming when watchmen on the hills of Ephraim will call out: Rise up! Let us go up to Zion, to the LORD our God.",
      "T": "A day is coming when watchmen on the heights of Ephraim will shout the call: Rise up! We are going up to Zion — to Yahweh our God!"
    },
    "7": {
      "L": "For thus says the LORD: Sing with gladness for Jacob, and shout among the chief of the nations; proclaim, give praise, and say: O LORD, save your people, the remnant of Israel.",
      "M": "For thus says the LORD: Sing out with joy for Jacob, and shout at the head of the nations. Announce it, praise it, and say: O LORD, save your people, the remnant of Israel.",
      "T": "This is what Yahweh says: Break into song for Jacob — rejoice! Shout it out before all the nations. Announce it, praise it, cry it out: Save your people, Yahweh! Save the remnant of Israel!"
    },
    "8": {
      "L": "Behold, I am bringing them from the land of the north and gathering them from the farthest parts of the earth, among them the blind and the lame, the woman with child and she who is in labor together; a great company shall return here.",
      "M": "Look! I am bringing them from the land of the north and gathering them from the far corners of the earth — among them the blind and the lame, the pregnant woman and the woman in labor. A great throng will return here.",
      "T": "Watch — I am bringing them home from the north country, gathering them from the ends of the earth. No one is left out: blind and lame, pregnant women and those in the grip of labor — all of them coming together in one great procession."
    },
    "9": {
      "L": "They shall come with weeping, and with supplications I will lead them; I will cause them to walk by rivers of water, in a straight way where they shall not stumble; for I am a father to Israel, and Ephraim is my firstborn.",
      "M": "They will come with weeping, and with prayers I will lead them. I will make them walk by streams of water, on a level path where they will not stumble. For I am a father to Israel, and Ephraim is my firstborn.",
      "T": "They will come home weeping — and with their prayers still rising from their lips I will lead them. I will set them on a level road beside flowing water, where no foot will stumble. For I am Israel's father, and Ephraim is my firstborn son."
    },
    "10": {
      "L": "Hear the word of the LORD, O nations, and declare it in the coastlands far away; say: He who scattered Israel will gather him, and keep him as a shepherd keeps his flock.",
      "M": "Hear the word of the LORD, O nations, and announce it in the distant coastlands: He who scattered Israel will gather him and watch over him as a shepherd watches his flock.",
      "T": "Nations — hear the word of Yahweh! Carry it to the farthest coastlands. Say it: The one who scattered Israel will gather him back. He will guard him the way a shepherd guards his flock."
    },
    "11": {
      "L": "For the LORD has ransomed Jacob and has redeemed him from the hand of one stronger than he.",
      "M": "For the LORD has ransomed Jacob and redeemed him from the hand of one who was too strong for him.",
      "T": "Yahweh has ransomed Jacob — bought him back, liberated him from a grip too powerful for him to break."
    },
    "12": {
      "L": "They shall come and sing on the height of Zion, and they shall beam over the goodness of the LORD, over grain and wine and oil, and over the young of the flock and the herd; their soul shall be like a watered garden, and they shall languish no more.",
      "M": "They will come and sing on the heights of Zion, radiant over the goodness of the LORD — over grain and wine and oil, over the young of the flock and the herd. Their very being will be like a well-watered garden; they will languish no more.",
      "T": "They will stream to the heights of Zion, singing, their faces lit up by the beauty of Yahweh's generosity — grain, wine, oil, the young of flocks and herds, all of it overflowing. Their whole selves will be like a garden with deep springs, and never again will they pine away."
    },
    "13": {
      "L": "Then shall the young women rejoice in the dance, and the young men and the old together; for I will turn their mourning into joy; I will comfort them and give them gladness from sorrow.",
      "M": "Then the young women will rejoice in the dance, and the young men and old men together, for I will turn their mourning into joy; I will comfort them and give them joy in place of sorrow.",
      "T": "Young women will dance. Young men and elders will join them together. For I will transform their grief into joy — I will comfort them and trade their sorrow in for exuberance."
    },
    "14": {
      "L": "I will satisfy the soul of the priests with fatness, and my people shall be satisfied with my goodness, says the LORD.",
      "M": "I will fill the priests with abundance, and my people will be satisfied with my goodness, declares the LORD.",
      "T": "The priests will eat their fill of richness; my people will be satisfied with every good thing I provide. Yahweh declares it."
    },
    "15": {
      "L": "Thus says the LORD: A voice is heard in Ramah, lamentation and bitter weeping; Rachel weeping for her children, refusing to be comforted for her children, because they are no more.",
      "M": "Thus says the LORD: A voice is heard in Ramah — lamentation and bitter weeping. Rachel is weeping for her children; she refuses to be comforted, because her children are no more.",
      "T": "This is what Yahweh says: A voice is heard in Ramah — a sound of lament and bitter, bitter weeping. Rachel weeping for her children. She will not be comforted. Her children are gone."
    },
    "16": {
      "L": "Thus says the LORD: Restrain your voice from weeping and your eyes from tears, for there is a reward for your labor, says the LORD; and they shall return from the land of the enemy.",
      "M": "Thus says the LORD: Hold back your voice from weeping and your eyes from tears, for your labor will be rewarded, declares the LORD. They will return from the land of the enemy.",
      "T": "This is what Yahweh says: Stop the weeping. No more tears. Your anguish was not wasted. Your children will come back from the land of the enemy. Yahweh has spoken."
    },
    "17": {
      "L": "And there is hope for your future, says the LORD; your children shall return to their own territory.",
      "M": "There is hope for your future, declares the LORD, and your children will return to their own land.",
      "T": "There is a future — Yahweh declares it — and there is hope. Your children will come home to their own ground."
    },
    "18": {
      "L": "I have surely heard Ephraim bemoaning himself: You disciplined me and I was disciplined, like an unbroken calf; bring me back that I may be restored, for you are the LORD my God.",
      "M": "I have indeed heard Ephraim's lament: 'You disciplined me, and I received the discipline, like an untrained calf. Restore me, and I will be restored, for you are the LORD my God.'",
      "T": "I have heard every word of Ephraim grieving: 'You broke me, and I was broken — like a calf that has never been under the yoke. Bring me back. Turn me around. Only you can do it — Yahweh, my God.'"
    },
    "19": {
      "L": "For after I turned I repented; and after I was instructed I struck my thigh; I was ashamed, and even confounded, because I bore the reproach of my youth.",
      "M": "For after I turned away I repented; after I was made to understand I struck my thigh in shame. I was ashamed and deeply humiliated, because I still bore the disgrace of my youth.",
      "T": "After I turned away, I came to my senses — I was filled with regret. When I finally understood what I had done, I struck my thigh in shame. I was embarrassed to the core, still carrying the reproach of my foolish early years."
    },
    "20": {
      "L": "Is Ephraim my dear son? Is he a pleasant child? For as often as I speak against him I earnestly remember him still; therefore my inmost being yearns for him; I will surely have mercy on him, says the LORD.",
      "M": "Is Ephraim not my dear son? Is he not my darling child? Even when I speak against him, I still remember him with longing; therefore my heart is deeply moved for him. I will surely have compassion on him, declares the LORD.",
      "T": "Is Ephraim not still my dear son? My beloved child? Even when I must speak against him, I keep thinking about him — longing for him. My whole being is moved with tenderness. I will have mercy. I will surely have mercy. Yahweh declares it."
    },
    "21": {
      "L": "Set up road markers for yourself; make yourself guideposts; set your heart toward the highway, the way by which you went; return, O virgin Israel, return to these your cities.",
      "M": "Set up road markers for yourself; establish guideposts. Keep your heart set on the highway — the way you traveled when you left. Come back, O virgin Israel; come back to your towns.",
      "T": "Plant your own guideposts on the road. Mark the way you went. Fix your attention on the highway — that road you traveled when you were taken away. Now come back on it. Come home, Israel. Every town that was yours is waiting."
    },
    "22": {
      "L": "How long will you waver, O faithless daughter? For the LORD has created a new thing in the earth: a woman encircles a man.",
      "M": "How long will you waver, O faithless daughter? For the LORD has created a new thing on the earth: a woman will court a man.",
      "T": "How long will you keep wavering, faithless Israel? Yahweh has done something unprecedented — created a new thing in the earth: a woman will seek out a man."
    },
    "23": {
      "L": "Thus says the LORD of hosts, the God of Israel: When I restore their fortunes in the land of Judah and in its cities, they shall yet say: The LORD bless you, O habitation of righteousness, O holy mountain.",
      "M": "Thus says the LORD of hosts, the God of Israel: When I restore their fortunes in the land of Judah and its cities, they will once again say: May the LORD bless you, O home of righteousness, O holy mountain.",
      "T": "This is what Yahweh of hosts, the God of Israel, says: When I turn Judah's fortunes around, when the cities fill with life again, people will say to one another: Yahweh bless you — dwelling place of justice, holy mountain!"
    },
    "24": {
      "L": "And Judah and all its cities shall dwell there together, the farmers and those who go forth with flocks.",
      "M": "And Judah and all its towns will dwell there together — farmers and those who move with their flocks.",
      "T": "Judah and all its towns will fill with life — farmers working the land, shepherds ranging the pastures — all of them together."
    },
    "25": {
      "L": "For I have satiated the weary soul, and every soul that is sorrowful I have replenished.",
      "M": "For I have satisfied the weary and replenished every soul that is faint.",
      "T": "I have given the exhausted what they could not find on their own. Every aching soul I have filled to the full."
    },
    "26": {
      "L": "Upon this I awoke and looked, and my sleep had been pleasant to me.",
      "M": "At this I awoke and looked around, and my sleep had been sweet.",
      "T": "Then I woke, and looked about me, and found that my sleep had been sweet."
    },
    "27": {
      "L": "Behold, the days are coming, says the LORD, when I will sow the house of Israel and the house of Judah with the seed of man and the seed of beast.",
      "M": "The days are coming, declares the LORD, when I will sow the house of Israel and the house of Judah with the seed of human beings and the seed of animals.",
      "T": "Days are coming — Yahweh declares it — when I will plant both Israel and Judah with new life: human beings and animals spreading across the land like seed scattered from a sower's hand."
    },
    "28": {
      "L": "And as I have watched over them to pluck up, to break down, to overthrow, to destroy, and to bring harm, so I will watch over them to build and to plant, says the LORD.",
      "M": "Just as I watched over them to uproot, tear down, overthrow, destroy, and bring disaster, so I will watch over them to build and to plant, declares the LORD.",
      "T": "In the past I watched over them with the full force of my judgment — uprooting, tearing down, overthrowing, destroying. With that same relentless attention I will now watch over them to build and to plant. Yahweh declares it."
    },
    "29": {
      "L": "In those days they shall no longer say: The fathers have eaten sour grapes, and the children's teeth are set on edge.",
      "M": "In those days they will no longer say: The fathers have eaten sour grapes, and the children's teeth are set on edge.",
      "T": "In those days no one will use this proverb anymore: The parents ate the sour grapes, but the children's teeth feel the bitterness."
    },
    "30": {
      "L": "But each shall die for his own iniquity; every man who eats sour grapes, his own teeth shall be set on edge.",
      "M": "Instead, everyone will die for their own iniquity. Every person who eats sour grapes — their own teeth will be set on edge.",
      "T": "Instead: each person bears their own sin. If you eat the sour grape, your own teeth feel it. Personal accountability — not inherited guilt."
    },
    "31": {
      "L": "Behold, the days are coming, says the LORD, when I will cut a new covenant with the house of Israel and with the house of Judah,",
      "M": "The days are coming, declares the LORD, when I will make a new covenant with the house of Israel and the house of Judah —",
      "T": "Days are coming — Yahweh declares it — when I will establish a new covenant with the house of Israel and the house of Judah —"
    },
    "32": {
      "L": "not like the covenant that I made with their fathers on the day when I took them by the hand to lead them out of the land of Egypt, my covenant which they broke, though I was their husband, says the LORD.",
      "M": "not like the covenant I made with their ancestors when I took them by the hand to lead them out of Egypt — a covenant they broke, even though I was their husband, declares the LORD.",
      "T": "not the covenant I made with their ancestors the day I took them by the hand and led them out of Egypt. They broke that covenant, even though I was their husband. Yahweh declares it."
    },
    "33": {
      "L": "But this is the covenant that I will make with the house of Israel after those days, says the LORD: I will put my law in their inward parts, and write it on their hearts; and I will be their God, and they shall be my people.",
      "M": "But this is the covenant I will make with the house of Israel after those days, declares the LORD: I will put my instruction within them and write it on their hearts. I will be their God, and they will be my people.",
      "T": "But this is the covenant I will make with the house of Israel when those days have come — Yahweh declares it: I will put my teaching inside them. I will inscribe it on their hearts. I will be their God, and they will be my people."
    },
    "34": {
      "L": "And they shall no more teach every man his neighbor and every man his brother, saying: Know the LORD; for they shall all know me, from the least of them to the greatest of them, says the LORD; for I will forgive their iniquity, and their sin I will remember no more.",
      "M": "No longer will they teach one another, or each their brother, saying, 'Know the LORD,' for they will all know me, from the least to the greatest, declares the LORD. For I will forgive their iniquity and remember their sin no more.",
      "T": "There will be no more need to teach a fellow citizen or a sibling — 'Learn to know Yahweh' — because they will all know me already, from the smallest child to the most prominent elder. Yahweh declares it. Because I will have pardoned their wrongdoing. Their sin — I will not call it to mind again."
    },
    "35": {
      "L": "Thus says the LORD, who gives the sun for light by day, and the fixed order of the moon and the stars for light by night, who stirs the sea so that its waves roar — LORD of hosts is his name:",
      "M": "Thus says the LORD, who gives the sun for light by day and the fixed order of the moon and stars for light by night, who stirs up the sea so that its waves roar — the LORD of hosts is his name:",
      "T": "This is what Yahweh says — he who set the sun to light the day, who arranged the moon and stars as lamps for the night, who stirs the sea until its waves thunder — Yahweh of hosts is his name:"
    },
    "36": {
      "L": "If these fixed orders depart from before me, says the LORD, then the offspring of Israel shall also cease from being a nation before me forever.",
      "M": "Only if this fixed order departs from before me, declares the LORD, would the offspring of Israel cease to be a nation before me forever.",
      "T": "Only if those cosmic ordinances fail — only if they depart from before me, Yahweh declares — only then would the descendants of Israel cease to be a people before me. It will never happen."
    },
    "37": {
      "L": "Thus says the LORD: If the heavens above can be measured and the foundations of the earth beneath can be searched out, then I will also cast off all the offspring of Israel for all that they have done, says the LORD.",
      "M": "Thus says the LORD: Only if the heavens above can be measured and the foundations of the earth below fully explored would I reject all the offspring of Israel for all that they have done, declares the LORD.",
      "T": "This is what Yahweh says: Could someone measure the full expanse of heaven? Could they probe the foundations beneath the earth? If they could — only then would I reject Israel in its entirety, for everything they have done. Yahweh declares it: I will not."
    },
    "38": {
      "L": "Behold, the days are coming, says the LORD, when the city shall be built for the LORD from the Tower of Hananeel to the Corner Gate.",
      "M": "The days are coming, declares the LORD, when the city will be rebuilt for the LORD, from the Tower of Hananeel to the Corner Gate.",
      "T": "Days are coming — Yahweh declares it — when the city will be rebuilt and consecrated to Yahweh, from the Tower of Hananeel all the way to the Corner Gate."
    },
    "39": {
      "L": "And the measuring line shall go forth again, straight ahead to the hill of Gareb, and shall turn about to Goah.",
      "M": "The measuring line will extend straight ahead to the hill of Gareb, then turn toward Goah.",
      "T": "The surveyor's line will run straight to the hill of Gareb, then curve around toward Goah."
    },
    "40": {
      "L": "And the whole valley of the dead bodies and the ashes, and all the fields to the brook Kidron, to the corner of the Horse Gate toward the east, shall be holy to the LORD; it shall not be plucked up or thrown down anymore forever.",
      "M": "The entire valley of dead bodies and ashes — all the fields to the Wadi Kidron, to the corner of the Horse Gate on the east — will be holy to the LORD. It will never again be uprooted or demolished.",
      "T": "Even the valley of corpses and ash — even those defiled fields stretching to the Kidron Brook, to the corner of the Horse Gate on the east — all of it will become holy to Yahweh. Never to be torn up or torn down. Not ever again. Forever."
    }
  },
  "32": {
    "1": {
      "L": "The word that came to Jeremiah from the LORD in the tenth year of Zedekiah king of Judah, which was the eighteenth year of Nebuchadnezzar.",
      "M": "This is the word that came to Jeremiah from the LORD in the tenth year of Zedekiah king of Judah, which was the eighteenth year of Nebuchadnezzar.",
      "T": "In the tenth year of Zedekiah king of Judah — Nebuchadnezzar's eighteenth year of reign — this word came to Jeremiah from Yahweh."
    },
    "2": {
      "L": "At that time the army of the king of Babylon was besieging Jerusalem, and Jeremiah the prophet was shut up in the court of the guard that was in the king of Judah's palace.",
      "M": "At that time the army of the king of Babylon was besieging Jerusalem, and Jeremiah the prophet was confined in the court of the guard in the palace of the king of Judah.",
      "T": "The Babylonian army was surrounding Jerusalem when all this happened. Jeremiah the prophet was under confinement in the guardhouse court inside Judah's royal palace."
    },
    "3": {
      "L": "For Zedekiah king of Judah had shut him up, saying: Why do you prophesy and say, Thus says the LORD: Behold, I am giving this city into the hand of the king of Babylon, and he shall take it?",
      "M": "For Zedekiah king of Judah had imprisoned him, saying: 'Why do you keep prophesying? You say: Thus says the LORD — I am going to hand this city to the king of Babylon, and he will capture it.'",
      "T": "Zedekiah king of Judah had locked him up with this charge: 'Why do you keep prophesying? Why do you keep saying: This is what Yahweh declares — I am handing this city to Babylon's king, and he will take it?'"
    },
    "4": {
      "L": "And Zedekiah king of Judah shall not escape from the hand of the Chaldeans, but shall surely be given into the hand of the king of Babylon; and he shall speak with him mouth to mouth, and his eyes shall see his eyes;",
      "M": "Zedekiah king of Judah will not escape from the Chaldeans. He will surely be handed over to the king of Babylon; he will speak with him face to face and see him with his own eyes.",
      "T": "And Zedekiah king of Judah will not slip away from the Chaldeans. He will be handed over personally to Babylon's king. He will stand before him face to face, eye to eye."
    },
    "5": {
      "L": "and he shall lead Zedekiah to Babylon, and there he shall remain until I attend to him, says the LORD; though you fight against the Chaldeans, you shall not succeed.",
      "M": "Zedekiah will be taken to Babylon and remain there until I deal with him, declares the LORD. If you fight against the Chaldeans, you will not succeed.",
      "T": "Zedekiah will be taken to Babylon and will stay there until the day I act on his case. Yahweh declares it: however long you fight against the Chaldeans, it will come to nothing."
    },
    "6": {
      "L": "And Jeremiah said: The word of the LORD came to me, saying:",
      "M": "Jeremiah said: The word of the LORD came to me:",
      "T": "Jeremiah continued his account: Yahweh's word came to me."
    },
    "7": {
      "L": "Behold, Hanamel the son of Shallum your uncle is coming to you, saying: Buy my field that is in Anathoth, for the right of redemption by purchase belongs to you.",
      "M": "Hanamel son of your uncle Shallum is going to come to you and say: Buy my field at Anathoth, for the right of redemption and purchase belongs to you.",
      "T": "Your cousin Hanamel son of Shallum is going to come to you and say: Buy my field at Anathoth — you have the right of first redemption, the right of purchase."
    },
    "8": {
      "L": "So Hanamel my uncle's son came to me in the court of the guard, in accordance with the word of the LORD, and said to me: Buy my field that is in Anathoth in the land of Benjamin, for the right of possession and redemption belongs to you; buy it. Then I knew that this was the word of the LORD.",
      "M": "So Hanamel, my uncle's son, came to me in the court of the guard, as the LORD had said. He told me: 'Buy my field at Anathoth in the land of Benjamin. The right of possession and redemption is yours — buy it.' I knew then that this was the word of the LORD.",
      "T": "And just as Yahweh had said, my cousin Hanamel came to me in the guardhouse courtyard. He said: 'Buy my field at Anathoth in Benjamin territory — as next of kin you have the right of redemption. It belongs to you. Buy it.' I knew then with certainty: this was Yahweh's word."
    },
    "9": {
      "L": "And I bought the field at Anathoth from Hanamel my uncle's son, and weighed out the money to him, seventeen shekels of silver.",
      "M": "I bought the field at Anathoth from Hanamel my uncle's son and weighed out the purchase price — seventeen shekels of silver.",
      "T": "I bought the field at Anathoth from my cousin Hanamel. I weighed out the price — seventeen shekels of silver."
    },
    "10": {
      "L": "I signed the deed and sealed it, called witnesses and weighed the money on balances.",
      "M": "I signed the deed, sealed it, brought in witnesses, and weighed the silver on scales.",
      "T": "I signed the deed and sealed it, brought in witnesses, and weighed out the silver on the scales."
    },
    "11": {
      "L": "Then I took the deed of purchase, both that which was sealed according to law and custom, and that which was open.",
      "M": "Then I took the deed of purchase — both the sealed copy containing the terms and conditions, and the open copy.",
      "T": "I took both copies of the deed — the sealed copy with the full legal terms inside, and the open copy for public inspection."
    },
    "12": {
      "L": "And I gave the deed of purchase to Baruch the son of Neriah, son of Mahseiah, in the presence of Hanamel my uncle's son and in the presence of the witnesses who signed the deed of purchase, and in the presence of all the Jews sitting in the court of the guard.",
      "M": "I gave the deed of purchase to Baruch son of Neriah son of Mahseiah, in the presence of my cousin Hanamel, in the presence of the witnesses who had signed the deed of purchase, and before all the Judeans sitting in the court of the guard.",
      "T": "I handed the deed to Baruch son of Neriah son of Mahseiah, with my cousin Hanamel, all the signing witnesses, and every Judean sitting in the guardhouse court watching the whole transaction."
    },
    "13": {
      "L": "And I charged Baruch in their presence, saying:",
      "M": "Then I gave Baruch these instructions in their presence:",
      "T": "Right there in front of them all I instructed Baruch:"
    },
    "14": {
      "L": "Thus says the LORD of hosts, the God of Israel: Take these deeds, both this sealed deed of purchase and this open deed, and put them in an earthen vessel, so that they may last for many days.",
      "M": "Thus says the LORD of hosts, the God of Israel: Take these deeds — the sealed deed of purchase and the open deed — and place them in a clay jar so that they will be preserved for a long time.",
      "T": "This is what Yahweh of hosts, the God of Israel, says: Take these documents — the sealed deed and the open copy — and put them in a clay jar. Seal them in so they will last for many years to come."
    },
    "15": {
      "L": "For thus says the LORD of hosts, the God of Israel: Houses and fields and vineyards shall yet again be bought in this land.",
      "M": "For thus says the LORD of hosts, the God of Israel: Houses and fields and vineyards will once again be bought in this land.",
      "T": "Because this is what Yahweh of hosts, the God of Israel, says: Houses, fields, and vineyards will be bought and sold again in this land."
    },
    "16": {
      "L": "After I had given the deed of purchase to Baruch the son of Neriah, I prayed to the LORD, saying:",
      "M": "After I had given the deed of purchase to Baruch son of Neriah, I prayed to the LORD:",
      "T": "After handing the deed to Baruch son of Neriah, I turned to Yahweh in prayer:"
    },
    "17": {
      "L": "Ah, Lord GOD! It is you who have made the heavens and the earth by your great power and by your outstretched arm! Nothing is too hard for you.",
      "M": "Ah, Lord GOD! You have made the heavens and the earth by your great power and your outstretched arm. Nothing is too difficult for you.",
      "T": "Ah, Lord Yahweh! You made the heavens and the earth with your great power and your outstretched arm. There is nothing — nothing — too hard for you."
    },
    "18": {
      "L": "showing steadfast love to thousands and repaying the iniquity of the fathers into the bosom of their children after them, O Great, O Mighty God, the LORD of hosts is his name;",
      "M": "You show steadfast love to thousands but repay the iniquity of the fathers into the laps of their children after them. O Great and Mighty God, whose name is the LORD of hosts,",
      "T": "You show covenant faithfulness to thousands, yet you repay the guilt of parents into the hands of their children who come after. Great God, Mighty God — Yahweh of hosts is your name."
    },
    "19": {
      "L": "great in counsel and mighty in work, whose eyes are open to all the ways of the sons of man, to give to each one according to his ways and according to the fruit of his deeds;",
      "M": "great in counsel and mighty in deed, whose eyes are open to all the ways of the children of mankind, rewarding each according to their ways and according to the fruit of their deeds.",
      "T": "Vast in wisdom, mighty in action. Your eyes are open to every path every human being walks, and you give each one what their life has earned — the full fruit of what they have done."
    },
    "20": {
      "L": "who have set signs and wonders in the land of Egypt to this day, and in Israel and among mankind, and have made yourself a name, as at this day;",
      "M": "You performed signs and wonders in the land of Egypt and have continued to do so to this day in Israel and among all humanity; you have made a name for yourself that endures to this day.",
      "T": "You performed signs and wonders in Egypt, and that mighty work has reverberated through Israel and among all humanity right up to this day. You made your name known — and it remains known."
    },
    "21": {
      "L": "and have brought your people Israel out of the land of Egypt with signs and wonders, with a strong hand and an outstretched arm, and with great terror.",
      "M": "You brought your people Israel out of the land of Egypt with signs and wonders, with a strong hand and an outstretched arm, and with great terror.",
      "T": "You brought Israel your people out of Egypt — with signs and wonders, with a powerful hand and an outstretched arm, with tremendous and awe-inspiring force."
    },
    "22": {
      "L": "And you gave them this land, which you swore to their fathers to give them, a land flowing with milk and honey.",
      "M": "You gave them this land, which you had sworn to their ancestors to give them — a land flowing with milk and honey.",
      "T": "You gave them this very land, the land you swore to their ancestors — a land flowing with milk and honey."
    },
    "23": {
      "L": "And they came in and possessed it, but they did not obey your voice or walk in your law; they did nothing of all that you commanded them to do; therefore you have caused all this evil to come upon them.",
      "M": "They entered and took possession of it, but they did not obey your voice or walk in your law. They did nothing of all you commanded them to do. That is why you brought all this disaster on them.",
      "T": "They entered and took possession — and then did none of what you commanded. No obedience to your voice, no walking in your law, nothing from the entire list of what you required. So you brought every one of these disasters on them."
    },
    "24": {
      "L": "Behold, the siege ramps have come up to the city to take it, and the city is given into the hand of the Chaldeans who are fighting against it, because of sword and famine and pestilence; and what you spoke has come to pass, and behold, you see it.",
      "M": "Look! The siege ramps have come up against the city to capture it. The city is being given into the hands of the Chaldeans fighting against it because of sword, famine, and pestilence. What you said has come true, and you yourself see it happening.",
      "T": "The siege ramps are up against the city walls. The city is being handed to the Chaldeans attacking it — sword, famine, and plague doing their work. Everything you said has come true. You yourself are watching it happen right now."
    },
    "25": {
      "L": "Yet you, O Lord GOD, have said to me: Buy the field for money and get witnesses — even though the city is given into the hand of the Chaldeans.",
      "M": "Yet you, O Lord GOD, have told me: Buy the field with money and get witnesses — even though the city is being handed over to the Chaldeans.",
      "T": "And yet you, Lord Yahweh, told me to buy the field. Pay for it. Get witnesses. Even while the city is being surrendered to the Chaldeans."
    },
    "26": {
      "L": "Then the word of the LORD came to Jeremiah, saying:",
      "M": "Then the word of the LORD came to Jeremiah:",
      "T": "Then Yahweh's word came to Jeremiah."
    },
    "27": {
      "L": "Behold, I am the LORD, the God of all flesh; is there anything too difficult for me?",
      "M": "I am the LORD, the God of all humanity. Is there anything too hard for me?",
      "T": "I am Yahweh — God of all flesh. Is there anything too difficult for me?"
    },
    "28": {
      "L": "Therefore thus says the LORD: Behold, I am giving this city into the hand of the Chaldeans and into the hand of Nebuchadnezzar king of Babylon, and he shall take it.",
      "M": "Therefore thus says the LORD: I am handing this city over to the Chaldeans and to Nebuchadnezzar king of Babylon, and he will capture it.",
      "T": "Therefore this is what Yahweh says: I am handing this city over — to the Chaldeans and to Nebuchadnezzar king of Babylon. He will take it."
    },
    "29": {
      "L": "And the Chaldeans who are fighting against this city shall come and set this city on fire and burn it, with the houses on whose roofs they have offered incense to Baal and poured out drink offerings to other gods, to provoke me to anger.",
      "M": "The Chaldeans fighting against this city will come, set it on fire, and burn it — along with the houses on whose rooftops they burned incense to Baal and poured out drink offerings to other gods to provoke me.",
      "T": "The Chaldeans attacking this city will come and torch it — the city and all the houses where incense burned to Baal on the rooftops and libations were poured out to foreign gods, all of it done deliberately to provoke me."
    },
    "30": {
      "L": "For the children of Israel and the children of Judah have only done evil before me from their youth; the children of Israel have only provoked me to anger with the work of their hands, says the LORD.",
      "M": "For the people of Israel and the people of Judah have done nothing but evil in my sight from their youth. The Israelites have done nothing but provoke me with what their hands have made, declares the LORD.",
      "T": "Because both Israel and Judah have done nothing but what is evil in my eyes — from the very days of their youth. Israel especially has done nothing but provoke me with everything their hands built and offered. Yahweh declares it."
    },
    "31": {
      "L": "For this city has been to me a provocation of my anger and my fury from the day they built it to this day, so that I must remove it from my presence,",
      "M": "This city has provoked my anger and fury from the day it was built to this day, so that I must remove it from my presence —",
      "T": "This city has been provoking my anger and my fury from the day it was built right down to today. Now I must remove it from before my face —"
    },
    "32": {
      "L": "because of all the evil of the children of Israel and the children of Judah which they have done to provoke me to anger — their kings, their officials, their priests, their prophets, the men of Judah, and the inhabitants of Jerusalem.",
      "M": "because of all the evil that the people of Israel and Judah have done to provoke me — their kings, their officials, their priests, their prophets, the men of Judah, and the residents of Jerusalem.",
      "T": "because of everything Israel and Judah have done to provoke me — their kings, their officials, their priests, their prophets, the men of Judah, the citizens of Jerusalem — every layer of the society, from top to bottom."
    },
    "33": {
      "L": "And they have turned to me the back and not the face; though I taught them persistently, they would not listen to receive instruction.",
      "M": "They have turned their backs to me and not their faces. Even though I taught them persistently, they would not listen or accept correction.",
      "T": "They turned their backs to me — refused to face me. Though I kept on teaching them, rising early to teach them again and again, they would not listen and would not take it in."
    },
    "34": {
      "L": "They set their abominations in the house that is called by my name, to defile it.",
      "M": "They placed their detestable idols in the temple that bears my name, defiling it.",
      "T": "They erected their foul idols right inside the temple that bears my name — defiling the very place where I put my name."
    },
    "35": {
      "L": "They built the high places of Baal in the Valley of the Son of Hinnom, to make their sons and daughters pass through fire to Molech, which I did not command them, nor did it enter my mind, that they should do this abomination, so as to cause Judah to sin.",
      "M": "They built the high places of Baal in the Valley of Ben-Hinnom, to make their sons and daughters pass through the fire to Molech — something I never commanded, nor did it ever enter my mind that they should do such a detestable thing, causing Judah to sin.",
      "T": "They built Baal's high places in the Valley of Hinnom and made their own children pass through fire as offerings to Molech — something I never commanded, something that never crossed my mind to want. And through it all they were dragging Judah into sin."
    },
    "36": {
      "L": "Now therefore thus says the LORD, the God of Israel, concerning this city of which you say, It is given into the hand of the king of Babylon by sword, by famine, and by pestilence:",
      "M": "Now therefore this is what the LORD, the God of Israel, says concerning this city about which you are saying, It is being handed to the king of Babylon by sword, famine, and plague:",
      "T": "Even so — this is what Yahweh, the God of Israel, says about this city you are saying will fall to Babylon's king by sword, starvation, and plague:"
    },
    "37": {
      "L": "Behold, I will gather them from all the lands to which I drove them in my anger and in my fury and in great wrath; I will bring them back to this place and make them dwell in safety.",
      "M": "I will gather them from all the lands where I drove them in my anger and fury and great wrath. I will bring them back to this place and make them live in safety.",
      "T": "I will gather them from every land where I drove them in my anger, my fury, my burning wrath. I will bring them back to this very place and let them live here in peace and security."
    },
    "38": {
      "L": "And they shall be my people, and I will be their God.",
      "M": "They will be my people, and I will be their God.",
      "T": "They will be my people. I will be their God."
    },
    "39": {
      "L": "And I will give them one heart and one way, that they may fear me forever, for their own good and the good of their children after them.",
      "M": "I will give them one heart and one way of life, that they may fear me always, for their own good and the good of their children after them.",
      "T": "I will give them a single heart and a single path — unified loyalty to me. They will revere me always, and it will be for their benefit and for their children's benefit long after them."
    },
    "40": {
      "L": "And I will make an everlasting covenant with them, that I will not turn away from doing good to them; and I will put my fear in their hearts, that they may not depart from me.",
      "M": "I will make an everlasting covenant with them: I will never turn away from doing good to them, and I will put reverence for me in their hearts so that they will not turn away from me.",
      "T": "I will make a covenant with them that will never end — my commitment to bless them will never be withdrawn. And I will plant in their hearts a genuine reverence for me, so that they will never want to walk away from me."
    },
    "41": {
      "L": "Yes, I will rejoice in doing them good and will plant them in this land in faithfulness, with all my heart and all my soul.",
      "M": "I will rejoice in doing them good and will plant them firmly in this land, with all my heart and all my soul.",
      "T": "I will take delight in blessing them and will plant them deeply in this land — faithfully, with all my heart, with all my soul, holding nothing back."
    },
    "42": {
      "L": "For thus says the LORD: Just as I have brought all this great disaster upon this people, so I will bring upon them all the good that I am promising them.",
      "M": "For thus says the LORD: Just as I have brought all this great disaster on this people, so I will bring on them all the good that I have promised.",
      "T": "This is what Yahweh says: With the same certainty that I brought every one of these disasters on this people, I will bring every promised blessing I have declared over them."
    },
    "43": {
      "L": "Fields shall be bought in this land of which you say: It is a desolation, without man or beast; it is given into the hand of the Chaldeans.",
      "M": "Fields will be bought in this land about which you now say: It is desolate, without man or beast, given into the hands of the Chaldeans.",
      "T": "Fields will be bought and sold in this very land — the land you are right now calling desolate, emptied of people and animals, handed over to the Chaldeans."
    },
    "44": {
      "L": "Men shall buy fields for money and sign and seal deeds and get witnesses, in the land of Benjamin, in the places about Jerusalem, and in the cities of Judah, in the cities of the hill country, in the cities of the lowland, and in the cities of the Negeb; for I will restore their fortunes, says the LORD.",
      "M": "People will buy fields for silver, sign and seal deeds, and call in witnesses — in the land of Benjamin, in the towns around Jerusalem, in the towns of Judah, in the towns of the hill country, of the foothills, and of the Negev. For I will restore their fortunes, declares the LORD.",
      "T": "People will buy fields for silver, sign and seal documents, bring in witnesses — in Benjamin, around Jerusalem, in Judah's towns, in the hill country, the foothills, and the Negev. Because I will turn their captivity around. Yahweh declares it."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'jeremiah')
        merge_tier(existing, JEREMIAH, tier_key)
        save(tier_dir, 'jeremiah', existing)
    print('Jeremiah 31–32 written.')

if __name__ == '__main__':
    main()
