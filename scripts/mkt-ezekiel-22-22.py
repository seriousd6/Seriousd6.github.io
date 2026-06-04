"""
MKT Ezekiel chapter 22 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-ezekiel-22-22.py

=== CHAPTER OVERVIEW ===
Ezekiel 22 is the "Bloody City" oracle — a concentrated theological indictment of Jerusalem
across three sections: (1) vv. 1–16, a comprehensive catalogue of Jerusalem's sins; (2)
vv. 17–22, the smelting-furnace metaphor — Israel reduced to dross; (3) vv. 23–31, the
verdict on every social class (prophets, priests, princes, people), climaxing in the
devastating "no one stood in the gap" declaration of v. 30.

=== CONTESTED-TERM DECISIONS ===

- H3068 (יהוה): "LORD" in L/M throughout. "Yahweh" in T — especially in the recognition
  formula ("you shall know that I am the LORD"), the oath-formula ("as I live"), and narrative
  pivot points. Consistent with all prior Ezekiel scripts.

- H136 + H3069 (אֲדֹנָי יְהוִה / Lord GOD): "Lord GOD" in L/M (small-caps GOD following
  convention). "Lord Yahweh" in T. The combined form introduces oracle sections in Ezekiel.

- H5315 (נֶפֶשׁ / soul/life/person): In v. 25 "devoured souls" (אָכְלוּ נְפָשׁוֹת) = destroyed
  lives/persons. L: "souls" (traditional). M: "people/persons" where the sense is "persons
  destroyed." T: "lives" or "lives of people" — the embodied whole person, not a spiritual
  substance separate from the body. In v. 27 "to destroy souls" = "to destroy people's lives."

- H5509 (סִיג / dross): The central metaphor of vv. 18–22. All three tiers: "dross" — the
  slag or waste residue left after smelting precious metal. In T this is expanded: dross is
  what is left when the refining process intended to purify instead reveals there was no
  silver to begin with. "Slag" used occasionally in T for variety.

- H2154 (זִמָּה / lewdness/depravity): v. 9, 11. "Lewdness" in L (traditional). "Depravity"
  in M/T — captures the moral shamelessness the word carries in Ezekiel's legal contexts.

- H1215 (בֶּצַע / dishonest gain): vv. 13, 27. "Dishonest gain" in L/M. "Ill-gotten profit"
  in T — draws out the economic predation subtext.

- H8199 (שָׁפַט / judge): v. 2 — the doubled form (שָׁפֹוט תִּשְׁפֹּט) is the emphatic
  infinitive absolute + finite verb = "will you indeed judge." L preserves the doubled form
  "wilt thou judge, wilt thou judge." M: "Will you judge — will you pronounce verdict on."
  T: "Will you judge this city — will you actually do it?"

- H8441 (תּוֹעֵבָה / abomination): v. 2 ("her abominations"). "Abominations" in L/M.
  T: "abominable deeds" or "every detestable practice" — the plural refers to specific acts
  catalogued in what follows, not a vague category.

- H2490 (חָלַל / profane/violate): v. 8 (sabbaths profaned), v. 26 (holy things profaned,
  law violated). "Profaned" in L/M. T: "desecrated" or "treated as worthless" — the word
  means taking something sacred and treating it as if common/unholy.

- H6233 (עֹשֶׁק / oppression) / H6231 (עָשַׁק / oppress): vv. 7, 29. "Oppression" in L/M.
  T: "exploitation" or "crushing abuse of power" — often refers specifically to the economic
  victimization of the vulnerable.

- H1616 (גֵּר / stranger/sojourner): vv. 7, 29. "Stranger" in L. "Resident alien/foreigner"
  in M. T: "the foreigner among you" or "those who came to live among you" — the sojourner
  who had legal protection under Mosaic covenant (Deut 24:17) but was being systematically
  violated.

- H5030 (נָבִיא / prophet): vv. 25, 28. "Prophets" throughout. In v. 25 the LXX reads
  "princes" (נְשִׂיאֶיהָ vs. נְבִיאֶיהָ — textual variant). MT reads "prophets"; followed
  here. In T, the distinction matters: prophets are the false prophets who prophesy comfort
  while whitewashing atrocities.

- H2902 (טוּחַ / daub/whitewash): v. 28. "Daubed with untempered morter" = whitewashed with
  thin plaster. L: "daubed them with untempered mortar." M: "whitewashed their deeds with
  flimsy plaster." T: developed as the definitive image of false prophecy: giving divine
  authorization to what God never authorized.

- H6556 (פֶּרֶץ / breach/gap): v. 30. The key image — a breach in the city wall. Someone
  who "stands in the gap" repairs the breach and thereby saves the city. "Gap" in L/M.
  T: the full weight of the image — the intercessor who steps into the dangerous opening
  between God's wrath and the people's doom. God looked for one such person and found none.
  This is the most desolate verse in Ezekiel 22.

- H1447 (גָּדֵר / wall/hedge): v. 30. "Hedge/wall" in L. "Wall/barrier" in M. T: "protective
  wall" — the image of communal protection that depends on someone being willing to repair it.

- H16 (v. 16 — nḥlt): The verb in v. 16 is textually contested. MT (נִחֲלַת) = "you will
  be profaned/desecrated" (from H2490, to profane) or "you will be your own inheritance"
  (from H5157, to inherit). Context favors "profaned" — the chapter's theme is the defilement
  of Jerusalem before the nations. L/M: "thou shalt be profaned / you will be profaned."
  T: "you will be exposed in your own shame" — the defilement becomes public disgrace.

=== ASPECT / TENSE NOTES ===

- The catalogue of sins (vv. 6–12) uses Hebrew perfect forms describing completed, established
  acts — characterizing what Jerusalem has already done. English present perfect ("they have
  not shown difference") or simple past captures this.
- The threat oracle (vv. 13–16, 19–22) uses imperfect first-person ("I will scatter / I will
  gather") — future certainty. Retained as future in all tiers.
- The furnace simile (vv. 20–22) uses the כַּאֲשֶׁר / כֵּן (as…so) structure — direct
  comparison. Preserved in all tiers.
- The comprehensive indictment (vv. 25–29) uses perfect forms — these are ongoing realities
  now described as established fact.

=== OT INTERTEXTUALITY ===

- The catalogue of social sins (vv. 7–12) echoes Lev 18–20 (sexual prohibitions), Deut
  24 (widow, orphan, stranger protections), and Ex 22:22–24 (oppression of widow and orphan).
  T surfaces these when relevant.
- The priests' failure to distinguish holy/profane, clean/unclean (v. 26) directly echoes
  the Aaronic commission of Lev 10:10. The priests were the designated guardians of this
  distinction; their failure is dereliction of their central duty.
- The "gap-stander" image (v. 30) echoes Moses' intercession (Ex 32:30–32, Ps 106:23)
  and anticipates Jeremiah's failed intercession (Jer 15:1). God says even Moses and Samuel
  would fail here (Jer 15:1). T notes the full weight of v. 30 as the darkest moment in
  the chapter.
- The furnace metaphor (vv. 18–22) echoes the earlier Egyptian slavery reference ("iron
  furnace" = Deut 4:20, 1 Ki 8:51) but inverts it: Egypt was the furnace from which Israel
  was delivered; now God himself makes Jerusalem the furnace of judgment.
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
  "22": {
    "1": {
      "L": "Moreover the word of the LORD came unto me, saying:",
      "M": "The word of the LORD came to me:",
      "T": "Yahweh's word came to me:"
    },
    "2": {
      "L": "Now thou, son of man, wilt thou judge, wilt thou judge the bloody city? Yea, thou shalt shew her all her abominations.",
      "M": "And you, son of man — will you judge, will you pronounce verdict on the city of bloodshed? Then declare to her all her abominable deeds.",
      "T": "Son of man — will you judge this city? Will you actually do it? Then do it: lay before the city of blood every abominable practice she has committed."
    },
    "3": {
      "L": "Then say thou: Thus saith the Lord GOD: The city sheddeth blood in the midst of it, that her time may come, and maketh idols against herself to defile herself.",
      "M": "Say: Thus says the Lord GOD: The city sheds blood in its own midst, making its time of judgment come, and makes idols against itself to defile itself.",
      "T": "Say from the Lord Yahweh: This city has been shedding blood in its own streets — blood that fills up the measure and makes the hour of reckoning inevitable. And she manufactures idols against her own soul, defiling herself with every hand-made god."
    },
    "4": {
      "L": "Thou art become guilty in thy blood that thou hast shed, and hast defiled thyself in thine idols which thou hast made; and thou hast caused thy days to draw near, and art come even unto thy years; therefore have I made thee a reproach unto the heathen, and a mocking to all countries.",
      "M": "You have become guilty by the blood you have shed and have defiled yourself by the idols you have made; you have brought your day of judgment near and have arrived at your appointed years. Therefore I have made you a reproach among the nations and a mockery to all the lands.",
      "T": "Your blood-guilt is established. Your idolatry is recorded. You yourself have accelerated the arrival of your judgment day — each act of violence, each idol carved, drew it nearer. And so I have made you a byword of shame among the nations and an object of ridicule in every surrounding land."
    },
    "5": {
      "L": "Those that be near, and those that be far from thee, shall mock thee, which art infamous and much vexed.",
      "M": "Both those near and those far from you will mock you, you who are defiled in name and full of turmoil.",
      "T": "Your neighbors and those who hear of you from far away will all mock you alike — the city whose name is synonymous with corruption, the city torn apart by its own violence."
    },
    "6": {
      "L": "Behold, the princes of Israel, every one were in thee to their power to shed blood.",
      "M": "See — the rulers of Israel within you have each used their power to shed blood.",
      "T": "Look at the leaders of Israel. Every one of them has used whatever authority they held as a license to shed blood. Power meant impunity. Rank meant violence."
    },
    "7": {
      "L": "In thee have they set light by father and mother; in the midst of thee have they dealt by oppression with the stranger; the fatherless and the widow have they vexed in thee.",
      "M": "In you they have dishonored father and mother; they have oppressed the resident foreigner in your midst; in you they have wronged the fatherless and the widow.",
      "T": "They despise father and mother — the foundational covenant relationship of family honor is worthless to them. They crush the foreigner living among them, the one who came to you for protection and has none. The orphan and the widow — the most vulnerable, for whom the law was explicit — they abuse them without conscience."
    },
    "8": {
      "L": "Thou hast despised mine holy things, and hast profaned my sabbaths.",
      "M": "You have despised my holy things and desecrated my sabbaths.",
      "T": "You treat the things I declared sacred as if they were ordinary — meaningless, expendable. My sabbaths, which I ordained as a covenant sign between us, you have treated as nothing."
    },
    "9": {
      "L": "In thee are men that carry tales to shed blood; and in thee they eat upon the mountains; in the midst of thee they commit lewdness.",
      "M": "Within you there are men who slander in order to shed blood; and in you they eat at the mountain shrines; in your midst they commit depravity.",
      "T": "Informers and slanderers operate within you — men who lie about the innocent to get them killed. At the mountain altars, people eat sacrificial meals before idols. Right in your middle, every form of depravity is practiced openly."
    },
    "10": {
      "L": "In thee have they discovered their fathers' nakedness: in thee have they humbled her that was set apart for pollution.",
      "M": "Within you they have uncovered their fathers' nakedness; within you they have violated the woman set apart in her uncleanness.",
      "T": "They violate the most foundational prohibitions of the family: exposing the nakedness that belongs to a father — a form of incest the law condemned without exception. And they approach women in ritual impurity, treating the law's boundaries as irrelevant."
    },
    "11": {
      "L": "And one hath committed abomination with his neighbour's wife; and another hath lewdly defiled his daughter in law; and another in thee hath humbled his sister, his father's daughter.",
      "M": "One man commits abomination with his neighbor's wife; another defiles his daughter-in-law in depravity; and another violates his sister, his father's daughter.",
      "T": "Adultery with a neighbor's wife. Sexual violation of a daughter-in-law. Incest with a half-sister. Every boundary the covenant established for the protection of women and the integrity of the family — Jerusalem has dismantled them all."
    },
    "12": {
      "L": "In thee have they taken gifts to shed blood; thou hast taken usury and increase, and thou hast greedily gained of thy neighbours by extortion, and hast forgotten me, saith the Lord GOD.",
      "M": "Within you they accept bribes to shed blood; you have taken interest and profit from loans, and you have greedily extorted gain from your neighbors — and you have forgotten me, declares the Lord GOD.",
      "T": "Judges accept bribes that result in innocent deaths. Lenders charge interest that the law of Moses explicitly forbade, squeezing profit from those already desperate. Neighbors are extorted for whatever can be extracted. And underneath all of it — the source of all of it — is this: you have forgotten me. The Lord Yahweh says it."
    },
    "13": {
      "L": "Behold, therefore I have smitten mine hand at thy dishonest gain which thou hast made, and at thy blood which hath been in the midst of thee.",
      "M": "Behold, therefore I have clapped my hand at your ill-gotten gain that you have made and at the blood that has been shed in your midst.",
      "T": "I clap my hands in fury and in disgust — at the profit you extracted by violence, at the blood pooled throughout your streets. This is the gesture of righteous outrage, and it is mine."
    },
    "14": {
      "L": "Can thine heart endure, or can thine hands be strong in the days that I shall deal with thee? I the LORD have spoken it, and will do it.",
      "M": "Will your heart endure or your hands remain strong in the days when I deal with you? I the LORD have spoken, and I will do it.",
      "T": "When I begin to deal with you — when judgment falls — will your courage hold? Will your hands have any strength left? I am Yahweh. I have declared it. It will happen."
    },
    "15": {
      "L": "And I will scatter thee among the heathen, and disperse thee in the countries, and will consume thy filthiness out of thee.",
      "M": "I will scatter you among the nations and disperse you through the lands, and I will purge your uncleanness out of you.",
      "T": "I will scatter you. Among every nation, through every land — dispersed and broken as a people. And in that scattering, the impurity that has accumulated in you will be burned away. Exile is not only punishment; it is a brutal purification."
    },
    "16": {
      "L": "And thou shalt be profaned in thyself in the sight of the heathen; and thou shalt know that I am the LORD.",
      "M": "You will be profaned in yourself in the sight of the nations, and you will know that I am the LORD.",
      "T": "Before the watching nations, you will be exposed and desecrated — your sacred pretensions stripped away, your defilement made public. And through it, you will come to know that I am Yahweh: the one whose word always stands."
    },
    "17": {
      "L": "And the word of the LORD came unto me, saying:",
      "M": "The word of the LORD came to me:",
      "T": "Yahweh's word came to me again:"
    },
    "18": {
      "L": "Son of man, the house of Israel is become dross unto me: all they are brass, and tin, and iron, and lead, in the midst of the furnace; they are even the dross of silver.",
      "M": "Son of man, the house of Israel has become dross to me: all of them are bronze, tin, iron, and lead within the furnace — they are the very dross of silver.",
      "T": "Son of man, Israel has become dross to me — worthless slag. The smelting process that was supposed to refine them has revealed what is actually there: not silver but base metals — bronze, tin, iron, lead — all mixed together in the crucible, all of it waste. They are the dross left over when silver is sought and nothing is found."
    },
    "19": {
      "L": "Therefore thus saith the Lord GOD: Because ye are all become dross, behold, therefore I will gather you into the midst of Jerusalem.",
      "M": "Therefore thus says the Lord GOD: Because you have all become dross, I will therefore gather you into the midst of Jerusalem.",
      "T": "Therefore, the Lord Yahweh says: You have become entirely dross — all of you. So I am doing what a smelter does with waste: I gather it together. Jerusalem will be the furnace. I am gathering you into it."
    },
    "20": {
      "L": "As they gather silver, and brass, and iron, and lead, and tin, into the midst of the furnace, to blow the fire upon it, to melt it; so will I gather you in mine anger and in my fury, and I will leave you there, and melt you.",
      "M": "As men gather silver, bronze, iron, lead, and tin into the furnace to blow the fire on them and melt them, so I will gather you in my anger and in my wrath; I will place you there and melt you.",
      "T": "The smelter sweeps everything into the crucible — silver, bronze, iron, lead, tin — lights the fire and drives it with bellows until the heat is fierce enough to reduce everything to liquid. That is what I am doing. In my anger, in my burning wrath, I am gathering you into Jerusalem. I will place you there in the fire, and I will melt you."
    },
    "21": {
      "L": "Yea, I will gather you, and blow upon you in the fire of my wrath, and ye shall be melted in the midst thereof.",
      "M": "Yes, I will gather you and blow upon you with the fire of my wrath, and you will be melted in the midst of it.",
      "T": "I will gather you — all of you — and drive the fire of my wrath through the bellows until you cannot stand. You will be melted down in the center of it. Nothing will remain in its former shape."
    },
    "22": {
      "L": "As silver is melted in the midst of the furnace, so shall ye be melted in the midst thereof; and ye shall know that I the LORD have poured out my fury upon you.",
      "M": "As silver is melted in a furnace, so you will be melted in the midst of it; and you will know that I the LORD have poured out my wrath upon you.",
      "T": "Silver melts in the furnace — that is the image, and it will be your reality. You will be melted, reshaped by force because you refused to be reshaped by covenant. And when it is over, you will know without any remaining doubt: I, Yahweh, poured out my wrath upon you. It was not accident, not enemy power — it was me."
    },
    "23": {
      "L": "And the word of the LORD came unto me, saying:",
      "M": "The word of the LORD came to me:",
      "T": "Yahweh's word came to me:"
    },
    "24": {
      "L": "Son of man, say unto her: Thou art the land that is not cleansed, nor rained upon in the day of indignation.",
      "M": "Son of man, say to her: You are a land that has not been cleansed, on which no rain has fallen in the day of indignation.",
      "T": "Son of man, say this to the land: You are a land that has not been purified — and in the day when wrath falls, no rain will come to you. Drought is covenant curse (Deut 28:24); the withholding of rain is God's signature on a broken covenant. The land itself bears the mark of what its people have done."
    },
    "25": {
      "L": "There is a conspiracy of her prophets in the midst thereof, like a roaring lion ravening the prey; they have devoured souls; they have taken the treasure and precious things; they have made her many widows in the midst thereof.",
      "M": "There is a conspiracy of prophets within her, like a roaring lion tearing the prey; they have devoured people, seized treasure and precious things, and made many widows within her.",
      "T": "Her prophets form a conspiracy — a coordinated predatory alliance. They operate like a roaring lion that has already torn its prey: they devour the vulnerable, consume the wealth of others, and leave behind a trail of widows — women made destitute by what the prophets did to their husbands. These are the men who claim to speak for God."
    },
    "26": {
      "L": "Her priests have violated my law, and have profaned mine holy things: they have put no difference between the holy and profane, neither have they shewed difference between the unclean and the clean, and have hid their eyes from my sabbaths, and I am profaned among them.",
      "M": "Her priests have violated my law and desecrated my holy things; they have made no distinction between the holy and the common, and have shown no difference between the unclean and the clean; they have shut their eyes to my sabbaths, and I am desecrated among them.",
      "T": "The priests — whose entire vocation was to maintain the boundary between holy and common, clean and unclean (Lev 10:10) — have collapsed those distinctions entirely. They teach no difference. They model no difference. They look away from the sabbath. The consequence is that I, the Holy One, am treated as profane in the middle of my own people. When the guardians of sacred boundaries abandon their post, the holy itself is profaned."
    },
    "27": {
      "L": "Her princes in the midst thereof are like wolves ravening the prey, to shed blood, and to destroy souls, to get dishonest gain.",
      "M": "Her officials within her are like wolves tearing the prey — shedding blood, destroying people's lives, to get dishonest gain.",
      "T": "Her rulers operate like wolves in the middle of the flock they are supposed to protect. They shed blood, they destroy the lives of people beneath them — and the motive underneath it all is ill-gotten profit. Power is simply a more efficient form of theft."
    },
    "28": {
      "L": "And her prophets have daubed them with untempered morter, seeing vanity, and divining lies unto them, saying: Thus saith the Lord GOD, when the LORD hath not spoken.",
      "M": "Her prophets have whitewashed these deeds with flimsy plaster — seeing false visions and divining lies — saying 'Thus says the Lord GOD,' when the LORD has not spoken.",
      "T": "And the prophets cover it all with a coat of whitewash — thin plaster spread over crumbling walls, making destruction look stable. They see visions that are not from God. They divine messages that are lies. And then they stamp it with 'Thus says the Lord Yahweh' — the formula of divine authority applied to whatever God never said. This is the completion of the system: every layer of society reinforces the other in its corruption."
    },
    "29": {
      "L": "The people of the land have used oppression, and exercised robbery, and have vexed the poor and needy: yea, they have oppressed the stranger wrongfully.",
      "M": "The people of the land have practiced oppression and committed robbery; they have wronged the poor and needy and oppressed the foreigner without justice.",
      "T": "And the people themselves — not just the leaders, not just the priests, not just the prophets — the ordinary people of the land have taken up the same patterns. They oppress. They rob. They grind down the poor and the needy. They abuse the foreigner who came to live among them, who has no clan protection. The rot is total. Every class, every layer of society, has failed."
    },
    "30": {
      "L": "And I sought for a man among them, that should make up the hedge, and stand in the gap before me for the land, that I should not destroy it: but I found none.",
      "M": "I looked for someone among them who would build up the wall and stand in the breach before me on behalf of the land, so that I would not destroy it — but I found no one.",
      "T": "I searched. I looked through all of them — through the prophets, the priests, the princes, the people — for one person who would step into the breach. Someone who would repair the gap in the wall between a holy God and a people bent on destruction. Someone who would stand before me and intercede, as Moses stood (Ex 32:30–32), throwing himself into the gap to hold back judgment for the sake of the land. I found no one. Not one. The silence of that finding is the most terrible moment in this chapter."
    },
    "31": {
      "L": "Therefore have I poured out mine indignation upon them; I have consumed them with the fire of my wrath: their own way have I recompensed upon their heads, saith the Lord GOD.",
      "M": "Therefore I have poured out my indignation upon them; I have consumed them with the fire of my wrath; I have repaid their own conduct upon their heads, declares the Lord GOD.",
      "T": "So it falls. I have poured out my indignation — the full measure of accumulated wrath over accumulated iniquity. I have consumed them in the fire of my fury. And what I have returned upon their heads is nothing alien, nothing arbitrary: it is their own way, their own choices, returned to them in kind. The Lord Yahweh says it and it stands."
    }
  }
}

def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'ezekiel')
        merge_tier(existing, EZEKIEL, tier_key)
        save(tier_dir, 'ezekiel', existing)
    print('Ezekiel 22 written.')

if __name__ == '__main__':
    main()
