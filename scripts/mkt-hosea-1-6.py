"""
MKT Hosea chapters 1–6 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-hosea-1-6.py

=== CHAPTER OVERVIEW ===

Hosea prophesied in the northern kingdom (Israel/Ephraim) during the reigns of
Uzziah through Hezekiah in Judah and Jeroboam II in Israel (ch. 1:1), roughly
760–720 BCE — a period of material prosperity masking spiritual apostasy. The
book is built around the prophet's marriage to Gomer, a woman of harlotry, as a
enacted parable of Israel's covenant infidelity to Yahweh.

Chapter 1: The Superscription and Symbolic Children.
  Hosea's marriage to Gomer is commanded; three children receive symbolic names:
  Jezreel (God will scatter/sow), Lo-ruhamah (No Mercy), Lo-ammi (Not My People).
  vv. 10–11: Immediate reversal — the divine rejection is bounded by a future
  restoration promise: "sons of the living God," reunified under one head.

Chapter 2: The Lawsuit and the New Covenant.
  vv. 1–13: A legal disputation between Yahweh (the wronged husband) and Israel
  (the unfaithful wife). Israel has attributed her blessings (grain, wine, oil) to
  the Baals; Yahweh will strip those blessings away and expose her shame.
  vv. 14–23: The astonishing reversal: Yahweh will allure Israel into the wilderness
  and speak tenderly to her; the Valley of Achor (Trouble) becomes a Door of Hope.
  A new marriage covenant replaces the broken one; the divine names of the children
  are reversed (vv. 1, 23: Ruhamah, Ammi). The cosmic covenant of 2:18 extends to
  the animal world and abolishes war.

Chapter 3: Hosea Redeems Gomer.
  A brief acted-out parable: Hosea buys back the adulterous woman for fifteen pieces
  of silver and a homer of barley. The restoration period of abstinence (v. 3)
  corresponds to Israel's long stateless period (v. 4) before a final return to
  Yahweh and David their king (v. 5).

Chapter 4: The LORD's Indictment of Israel.
  Yahweh brings a formal covenant lawsuit (rib): no truth, no steadfast love, no
  knowledge of God in the land (v. 1). Specific charges: the priests have abandoned
  their teaching role (v. 6); they feed on the sins of the people (v. 8); fertility-
  cult prostitution at the high places (vv. 11–14). Ephraim is joined to idols: let
  him alone (v. 17).

Chapter 5: Judgment on Priests, Israel, and Judah.
  The snare of Mizpah/Tabor (v. 1), the spirit of whoredom (v. 4), searching for
  Yahweh with flocks but not finding him (v. 6). Ephraim's pride testifies against
  him (v. 5). Judah is included in the indictment. Both kingdoms seek Assyria for
  help (v. 13); Yahweh will be like a lion to both until they acknowledge their
  guilt (vv. 14–15).

Chapter 6: Shallow Repentance and Relentless Covenant Loyalty.
  The hymnic call to return (vv. 1–3: "Come, let us return") is placed in Israel's
  mouth — but Yahweh's response (v. 4) expresses frustration: their love (hesed)
  is like morning mist. He desires hesed and knowledge of God, not sacrifices (v. 6).
  Historical charges of covenant breach in Gilead, the priests' murder at Shechem
  (vv. 7–10). Judah's harvest of judgment is set (v. 11).

=== CONTESTED-TERM DECISIONS ===

- H3068 (יהוה / Yahweh): L/M render "LORD" (small-caps convention). T uses
  "Yahweh" in prophetic-oracle and covenant contexts where the divine name is
  covenantally weighted (e.g., the covenant lawsuit of ch. 4, marriage-restoration
  passages of ch. 2), and "the LORD" in narrative passages. Documented per verse
  in the data.

- H430 (אֱלֹהִים / Elohim): "God" in all tiers. Grammatically plural, contextually
  singular (Israel's God). No tier attempts to preserve the grammatical tension
  since it reads awkwardly in English and Hosea's context is monotheistic.

- H2617 (חֶסֶד / hesed): L: "steadfast love." M: "covenant loyalty." T: "faithful
  love" (6:4, 6) or "covenant devotion" (2:19). The term combines covenant
  obligation and active mercy — no single English word suffices; the rendering
  varies slightly by context while staying consistent within each tier.

- H7307 (רוּחַ / ruah): "spirit" in L/M (lowercase — the referent is not the divine
  Spirit but a disposition or force). 4:12 ("spirit of whoredom") = a moral/spiritual
  disposition; rendered "a spirit of prostitution" in M and "a spirit that drives
  them to prostitution" in T to make the agency clear. Capital "Spirit" is not used
  here since the divine Spirit is not the referent.

- H2181 (זָנָה / zanah, "to commit prostitution/harlotry"): The marriage-covenant
  metaphor's core verb. L: "commit harlotry" / "play the harlot" (preserving the
  source idiom). M: "commit adultery" / "be unfaithful" (natural English within
  the covenant-marriage frame). T: surfaces the covenantal breach explicitly —
  "chased after other lovers," "broke covenant faith." The term covers literal
  sexual sin and metaphorical religious apostasy; context in each verse drives
  which nuance is foregrounded.

- H1285 (בְּרִית / berit, "covenant"): "covenant" in all tiers. Hosea's new
  covenant of 2:18 is the first such passage in the writing prophets.

- Symbolic names — transliterated and explained:
  H3157 (יִזְרְעֶאל / Yizreel): L/M: "Jezreel." T: "Jezreel (God Sows/Scatters)."
  H3819 (לֹא רֻחָמָה / Lo-ruhamah): L: "Lo-ruhamah." M: "Lo-ruhamah (Not Pitied)."
  T: "Lo-ruhamah — Not Shown Mercy."
  H3818 (לֹא עַמִּי / Lo-ammi): L: "Lo-ammi." M: "Lo-ammi (Not My People)."
  T: "Lo-ammi — Not My People."

- H5971 (עַם / am, "people"): "people / my people / his people" as context
  demands; L stays literal ("people"), M/T may use "nation" or "my people" as
  idiomatic.

- H1168 (בַּעַל / Baal, plural בְּעָלִים / Bealim): "Baal" / "the Baals" in all
  tiers. Not translated. Context makes clear these are Canaanite fertility gods.

- H3045 (יָדַע / yada', "to know"): In Hosea "knowledge of God" (da'at Elohim)
  is a covenant term — relational, experiential, not merely cognitive. M: "knowledge
  of God." T: "intimate knowledge of God" or "knowing God" to surface the covenant
  register. 4:6: "my people are destroyed for lack of knowledge" — T: "My people
  perish because they have refused to know me."

- "Spirit of whoredom" (H2183 + H7307, 4:12; 5:4): A moral disposition toward
  apostasy. See H7307 note above.

- OT poetic structure (ch. 2, 6): Hosea contains poetry with parallelism. In the T
  tier, poetic verses are rendered with line breaks to preserve the parallelism
  and cadence. M uses flowing prose. L preserves word order even where awkward.

- H8673 / numbers in ch. 3: "fifteen pieces of silver" — retained literally in
  all tiers as the precise purchase price.

- Divine passive: Several verbs imply God as unnamed agent (e.g., 1:4 "I will
  avenge the blood of Jezreel"). L/M name God explicitly where the Hebrew does;
  T may surface the divine agency in phrasing.

- Aspect (Hebrew perfect / imperfect):
  Perfect verbs in oracles = completed in divine purpose even if future in time;
  rendered as simple past or English present depending on context.
  Imperfect / waw-consecutive imperfect = narrative sequence or ongoing action;
  rendered with English narrative past or future as context demands.
  Hosea uses both perfects and imperfects mid-oracle, sometimes shifting abruptly;
  T makes the rhetorical force of each shift explicit.
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
    "1": {
        "1": {
            "L": "The word of the LORD that came unto Hosea the son of Beeri, in the days of Uzziah, Jotham, Ahaz, and Hezekiah, kings of Judah, and in the days of Jeroboam the son of Joash, king of Israel.",
            "M": "The word of the LORD that came to Hosea son of Beeri during the reigns of Uzziah, Jotham, Ahaz, and Hezekiah, kings of Judah, and during the reign of Jeroboam son of Joash, king of Israel.",
            "T": "This is the word Yahweh spoke to Hosea son of Beeri — during the years of Uzziah, Jotham, Ahaz, and Hezekiah in Judah, and in the days of Jeroboam son of Joash in Israel."
        },
        "2": {
            "L": "The beginning of the word of the LORD by Hosea. And the LORD said to Hosea, Go, take unto thee a wife of whoredoms and children of whoredoms, for the land hath committed great whoredom, departing from the LORD.",
            "M": "When the LORD first spoke through Hosea, the LORD said to him, Go and take a wife of unfaithfulness, and have children of unfaithfulness, for the land has committed great unfaithfulness by forsaking the LORD.",
            "T": "This was the very first word Yahweh spoke through Hosea: 'Go, marry a woman given to prostitution, and raise children of that same bent — for this land has been utterly faithless, chasing after other gods instead of me.'"
        },
        "3": {
            "L": "So he went and took Gomer the daughter of Diblaim, which conceived and bore him a son.",
            "M": "So he went and married Gomer daughter of Diblaim, and she conceived and bore him a son.",
            "T": "Hosea obeyed. He married Gomer, the daughter of Diblaim, and she became pregnant and bore him a son."
        },
        "4": {
            "L": "And the LORD said unto him, Call his name Jezreel; for yet a little while, and I will avenge the blood of Jezreel upon the house of Jehu, and will cause to cease the kingdom of the house of Israel.",
            "M": "And the LORD said to him, Name him Jezreel, for in a little while I will punish the house of Jehu for the bloodshed at Jezreel, and I will bring the kingdom of Israel to an end.",
            "T": "Yahweh told him: 'Name the boy Jezreel — for soon I will call to account the house of Jehu for the blood spilled at Jezreel, and I will break the royal power of Israel.'"
        },
        "5": {
            "L": "And it shall come to pass at that day, that I will break the bow of Israel in the valley of Jezreel.",
            "M": "On that day I will break the bow of Israel in the valley of Jezreel.",
            "T": "On that day I will shatter Israel's military might in the very valley that bears Jezreel's name."
        },
        "6": {
            "L": "And she conceived again, and bore a daughter. And God said unto him, Call her name Lo-ruhamah, for I will no more have mercy upon the house of Israel; but I will utterly take them away.",
            "M": "She conceived again and bore a daughter. And God said to him, Name her Lo-ruhamah — Not Pitied — for I will no longer show mercy to the house of Israel or forgive them at all.",
            "T": "Gomer conceived again and bore a daughter. God said: 'Name her Lo-ruhamah — Not Shown Mercy — for I will no longer extend mercy to Israel. I have reached the end of my patience with them.'"
        },
        "7": {
            "L": "But I will have mercy upon the house of Judah, and will save them by the LORD their God, and will not save them by bow, nor by sword, nor by battle, by horses, nor by horsemen.",
            "M": "But I will show mercy to the house of Judah, and I will save them by the LORD their God. I will not save them by bow, sword, battle, horses, or horsemen.",
            "T": "Judah, however, will receive my mercy. I will deliver them — but not by military force, not by bows or swords or cavalry. I, Yahweh their God, will rescue them."
        },
        "8": {
            "L": "Now when she had weaned Lo-ruhamah, she conceived and bore a son.",
            "M": "After she had weaned Lo-ruhamah, Gomer conceived again and bore a son.",
            "T": "Once Lo-ruhamah was weaned, Gomer became pregnant once more and gave birth to a son."
        },
        "9": {
            "L": "Then said God, Call his name Lo-ammi, for ye are not my people, and I will not be your God.",
            "M": "Then God said, Name him Lo-ammi — Not My People — for you are not my people, and I am not your God.",
            "T": "God said: 'Name him Lo-ammi — Not My People. For that is what you have become: not my people, and I will not be yours.'"
        },
        "10": {
            "L": "Yet the number of the children of Israel shall be as the sand of the sea, which cannot be measured nor numbered; and it shall come to pass, that in the place where it was said unto them, Ye are not my people, there it shall be said unto them, Ye are the sons of the living God.",
            "M": "Yet the number of the children of Israel will be like the sand of the sea, which cannot be measured or counted. And in the very place where they were told, You are not my people, they will be called children of the living God.",
            "T": "And yet — the descendants of Israel will multiply beyond counting, like the sand of the seashore. In the very place where they were told 'You are not my people,' they will be called 'Children of the living God.'"
        },
        "11": {
            "L": "Then shall the children of Judah and the children of Israel be gathered together, and appoint themselves one head, and they shall come up out of the land: for great shall be the day of Jezreel.",
            "M": "The children of Judah and Israel will be gathered together, and they will appoint for themselves one leader and come up from the land. Great will be the day of Jezreel.",
            "T": "Judah and Israel will be reunited. Together they will choose one leader and rise from the land of exile. That day — the day of Jezreel — will be magnificent."
        }
    },
    "2": {
        "1": {
            "L": "Say ye unto your brethren, Ammi; and to your sisters, Ruhamah.",
            "M": "Say to your brothers, My people; and to your sisters, My beloved.",
            "T": "Call your brothers 'My People' and your sisters 'My Beloved.' The names of rejection have been reversed."
        },
        "2": {
            "L": "Plead with your mother, plead: for she is not my wife, neither am I her husband: let her therefore put away her whoredoms out of her sight, and her adulteries from between her breasts;",
            "M": "Contend with your mother, contend — for she is not my wife, and I am not her husband — let her remove her unfaithfulness from her face, and her adultery from between her breasts,",
            "T": "Plead with her — plead with your mother, for I am no longer her husband, and she is no longer my wife. Let her put away her adultery, strip the tokens of her other lovers from her face and her body,"
        },
        "3": {
            "L": "Lest I strip her naked and set her as in the day that she was born, and make her as a wilderness, and set her like a dry land, and slay her with thirst.",
            "M": "or else I will strip her naked and expose her as on the day she was born, and make her like a wilderness, like a parched land, and let her die of thirst.",
            "T": "or I will strip her bare — as naked as the day she was born — and make her as desolate as a desert, as dry as cracked earth, and leave her to die of thirst."
        },
        "4": {
            "L": "And I will not have mercy upon her children; for they be the children of whoredoms.",
            "M": "I will show no compassion to her children, for they are children of unfaithfulness.",
            "T": "I will show no mercy to her children either — they were born from her faithlessness."
        },
        "5": {
            "L": "For their mother hath played the harlot: she that conceived them hath done shamefully: for she said, I will go after my lovers, that give me my bread and my water, my wool and my flax, mine oil and my drink.",
            "M": "For their mother has been unfaithful; she who conceived them has acted shamefully. She said, I will go after my lovers, who give me my bread and my water, my wool and my flax, my oil and my wine.",
            "T": "Their mother has played the whore; she who bore them has shamed herself. She said: 'I will chase after my lovers — they are the ones who give me bread and water, wool and linen, oil and wine.'"
        },
        "6": {
            "L": "Therefore, behold, I will hedge up thy way with thorns, and make a wall, that she shall not find her paths.",
            "M": "Therefore I will block her way with thorns; I will wall her in so that she cannot find her paths.",
            "T": "So I will fence her in with thorns; I will build a wall around her so she cannot find the roads she ran down."
        },
        "7": {
            "L": "And she shall follow after her lovers, but she shall not overtake them; and she shall seek them, but shall not find them: then shall she say, I will go and return to my first husband; for then was it better with me than now.",
            "M": "She will chase after her lovers but not catch them; she will seek them but not find them. Then she will say, I will go back to my first husband, for things were better for me then than now.",
            "T": "She will run after her lovers and not catch them; search for them and not find them. Then at last she will say: 'I will go back to my husband as before — my life was better then than now.'"
        },
        "8": {
            "L": "For she did not know that I gave her corn, and wine, and oil, and multiplied her silver and gold, which they prepared for Baal.",
            "M": "She did not know that it was I who gave her the grain, the wine, and the oil, and who lavished on her silver and gold — which they used for Baal.",
            "T": "She never grasped that it was I — Yahweh — who had given her the grain, the wine, the olive oil, who had enriched her with silver and gold. And she took all of it and offered it to Baal."
        },
        "9": {
            "L": "Therefore will I return, and take away my corn in the time thereof, and my wine in the season thereof, and will recover my wool and my flax given to cover her nakedness.",
            "M": "Therefore I will take back my grain when it ripens and my wine when it is ready; I will reclaim my wool and my flax, which I gave to cover her nakedness.",
            "T": "So I will take back what is mine: at harvest I will take the grain, at vintage the wine. I will reclaim the wool and the linen I gave to cover her — and she will stand exposed."
        },
        "10": {
            "L": "And now will I discover her lewdness in the sight of her lovers, and none shall deliver her out of mine hand.",
            "M": "Now I will expose her shameful nakedness before her lovers, and no one will rescue her from my hand.",
            "T": "I will expose her shame in full view of her lovers, and not one of them will be able to save her from me."
        },
        "11": {
            "L": "I will also cause all her mirth to cease, her feast days, her new moons, and her sabbaths, and all her solemn feasts.",
            "M": "I will put an end to all her celebrations — her festivals, her new moon observances, her sabbaths, and all her appointed feasts.",
            "T": "I will silence every celebration: no more festivals, no more new moon gatherings, no more sabbaths, no more sacred assemblies. The joy will be stripped away."
        },
        "12": {
            "L": "And I will destroy her vines and her fig trees, whereof she hath said, These are my rewards that my lovers have given me: and I will make them a forest, and the beasts of the field shall eat them.",
            "M": "I will ruin her vines and her fig trees, which she said were the gifts her lovers gave her. I will make them a thicket, and the wild animals will devour them.",
            "T": "I will lay waste to her vineyards and fig orchards — the ones she called 'wages my lovers paid me.' I will let them go wild; the animals of the open country will eat them down."
        },
        "13": {
            "L": "And I will visit upon her the days of the Baalim, wherein she burned incense to them, and she decked herself with her earrings and her jewels, and she went after her lovers, and forgat me, saith the LORD.",
            "M": "I will punish her for the days she burned incense to the Baals, when she adorned herself with rings and jewels and went after her lovers and forgot me, declares the LORD.",
            "T": "I will call her to account for every day she burned incense to the Baals — the days she dressed herself in rings and jewelry to chase her lovers — and forgot me completely. This is Yahweh's word."
        },
        "14": {
            "L": "Therefore, behold, I will allure her, and bring her into the wilderness, and speak comfortably unto her.",
            "M": "Therefore, behold, I will allure her, and bring her into the wilderness, and speak tenderly to her.",
            "T": "And yet — I will woo her. I will lead her out into the wilderness and speak to her heart there."
        },
        "15": {
            "L": "And I will give her her vineyards from thence, and the valley of Achor for a door of hope: and she shall sing there, as in the days of her youth, and as in the day when she came up out of the land of Egypt.",
            "M": "There I will give back her vineyards and make the Valley of Achor a door of hope. She will respond there as in the days of her youth, as on the day she came up out of the land of Egypt.",
            "T": "From that wilderness I will give her vineyards again; I will transform the Valley of Achor — the Valley of Trouble — into a gateway of hope. She will sing for me there as she sang in her youth, as she sang on the day she came out of Egypt."
        },
        "16": {
            "L": "And it shall be at that day, saith the LORD, that thou shalt call me Ishi; and shalt call me no more Baali.",
            "M": "In that day, declares the LORD, you will call me My Husband, and you will no longer call me My Master.",
            "T": "On that day — Yahweh declares — you will call me 'My Husband,' and never again 'My Baal.' The word itself will be changed."
        },
        "17": {
            "L": "For I will take away the names of Baalim out of her mouth, and they shall no more be remembered by their name.",
            "M": "For I will remove the names of the Baals from her lips, and they will be mentioned no more.",
            "T": "I will purge the names of the Baals from her mouth — she will not even speak them, let alone worship them."
        },
        "18": {
            "L": "And in that day will I make a covenant for them with the beasts of the field, and with the fowls of heaven, and with the creeping things of the ground: and I will break the bow and the sword and the battle out of the earth, and will make them to lie down safely.",
            "M": "In that day I will make a covenant for them with the wild animals, the birds of the sky, and the creatures that crawl on the ground. I will abolish the bow and the sword and warfare from the land, and I will make them lie down in safety.",
            "T": "On that day I will establish a covenant with all creation — with the wild animals, the birds of the air, the creatures of the ground. I will shatter bows and swords and end war from the earth, and my people will lie down in safety."
        },
        "19": {
            "L": "And I will betroth thee unto me for ever; yea, I will betroth thee unto me in righteousness, and in judgment, and in lovingkindness, and in mercies.",
            "M": "I will betroth you to me forever; I will betroth you in righteousness and justice, in covenant loyalty and compassion.",
            "T": "I will make you my bride forever —\nI will betroth you with righteousness and justice,\nwith faithful love and tender compassion."
        },
        "20": {
            "L": "I will even betroth thee unto me in faithfulness: and thou shalt know the LORD.",
            "M": "I will betroth you in faithfulness, and you will know the LORD.",
            "T": "I will betroth you to me in fidelity,\nand you will truly know Yahweh — not as a name but as a living presence."
        },
        "21": {
            "L": "And it shall come to pass in that day, I will hear, saith the LORD, I will hear the heavens, and they shall hear the earth;",
            "M": "In that day I will respond, declares the LORD — I will respond to the heavens, and they will respond to the earth,",
            "T": "On that day I will answer — Yahweh declares.\nI will answer the heavens, and the heavens will answer the earth,"
        },
        "22": {
            "L": "And the earth shall hear the corn, and the wine, and the oil; and they shall hear Jezreel.",
            "M": "and the earth will respond to the grain, the wine, and the oil, and they will respond to Jezreel.",
            "T": "the earth will answer the grain, the wine, and the olive oil,\nand they will answer Jezreel — God Sows."
        },
        "23": {
            "L": "And I will sow her unto me in the earth; and I will have mercy upon her that had not obtained mercy; and I will say to them which were not my people, Thou art my people; and they shall say, Thou art my God.",
            "M": "I will plant her for myself in the land, and I will show mercy to the one who was called Not Pitied; and to those who were called Not My People I will say, You are my people; and they will say, You are my God.",
            "T": "I will plant her in the land like a seed sown by my own hand.\nI will love the one I called Lo-ruhamah — Not Shown Mercy.\nI will say to Lo-ammi — Not My People — 'You are my people.'\nAnd they will answer: 'You are our God.'"
        }
    },
    "3": {
        "1": {
            "L": "Then said the LORD unto me, Go yet, love a woman beloved of her friend, yet an adulteress, according to the love of the LORD toward the children of Israel, who look to other gods, and love flagons of wine.",
            "M": "Then the LORD said to me, Go again, love a woman who is loved by another man and is an adulteress, just as the LORD loves the children of Israel though they turn to other gods and love raisin cakes.",
            "T": "Then Yahweh said to me: 'Go again — love a woman who is unfaithful, who is loved by another yet still commits adultery. Love her as I love Israel, even though they keep turning to other gods and lavishing devotion on empty things.'"
        },
        "2": {
            "L": "So I bought her to me for fifteen pieces of silver, and for an homer of barley, and an half homer of barley:",
            "M": "So I bought her back for fifteen pieces of silver and a homer and a half of barley.",
            "T": "So I bought her back — fifteen pieces of silver, and a homer and a half of barley. That was the price I paid to bring her home."
        },
        "3": {
            "L": "And I said unto her, Thou shalt abide for me many days; thou shalt not play the harlot, and thou shalt not be for another man: so will I also be for thee.",
            "M": "And I said to her, You must stay with me for many days; you are not to be a prostitute or to be with any man, and I also will be faithful to you.",
            "T": "I told her: 'You will stay with me for a long time. No prostitution. No other man. And I — I will be faithful to you.'"
        },
        "4": {
            "L": "For the children of Israel shall abide many days without a king, and without a prince, and without a sacrifice, and without an image, and without an ephod, and without teraphim:",
            "M": "For the children of Israel will live for many days without a king, without a ruler, without a sacrifice, without a sacred pillar, without an ephod, and without household idols.",
            "T": "This is what Israel's future holds: a long, suspended time — no king, no leader, no sacrifice, no sacred pillar, no priestly ephod, no household gods. A long waiting, stripped of all the props of both true and false religion."
        },
        "5": {
            "L": "Afterward shall the children of Israel return, and seek the LORD their God, and David their king; and shall fear the LORD and his goodness in the latter days.",
            "M": "Afterward the children of Israel will return and seek the LORD their God and David their king. They will come trembling to the LORD and his goodness in the last days.",
            "T": "But afterward — Israel will turn back. They will seek Yahweh their God and David their king. In the days to come, trembling with awe, they will come to Yahweh and receive his goodness."
        }
    },
    "4": {
        "1": {
            "L": "Hear the word of the LORD, ye children of Israel: for the LORD hath a controversy with the inhabitants of the land, because there is no truth, nor mercy, nor knowledge of God in the land:",
            "M": "Hear the word of the LORD, O children of Israel, for the LORD has a case against the inhabitants of the land. There is no faithfulness, no covenant loyalty, no knowledge of God in the land.",
            "T": "Listen to the word of Yahweh, O Israel — for Yahweh has a legal case against the inhabitants of this land. There is no truth, no faithful love, no knowledge of God anywhere in it."
        },
        "2": {
            "L": "By swearing, and lying, and killing, and stealing, and committing adultery, they break out, and blood toucheth blood.",
            "M": "There is cursing, lying, murder, stealing, and adultery; they break all bounds, and bloodshed follows bloodshed.",
            "T": "Cursing and deception, murder and theft and adultery are everywhere; lawlessness floods the land, and blood flows into blood without end."
        },
        "3": {
            "L": "Therefore shall the land mourn, and every one that dwelleth therein shall languish, with the beasts of the field, and with the fowls of heaven; yea, the fishes of the sea also shall be taken away.",
            "M": "Therefore the land mourns, and all who live in it waste away — the animals of the field, the birds of the sky, and even the fish of the sea are swept away.",
            "T": "The land itself is in mourning; everything on it is wasting away — the wild animals, the birds of the sky, and even the fish of the sea are being swept away. All creation suffers the covenant's breach."
        },
        "4": {
            "L": "Yet let no man strive, nor reprove another: for thy people are as they that strive with the priest.",
            "M": "Yet let no one accuse or rebuke another, for your people are like those who bring charges against a priest.",
            "T": "Let no one point fingers or bring charges — for the whole people are as guilty as those who dare to contend against a priest."
        },
        "5": {
            "L": "Therefore shalt thou fall in the day, and the prophet also shall fall with thee in the night, and I will destroy thy mother.",
            "M": "You stumble in the daylight; the prophet stumbles with you in the night; and I will destroy your mother.",
            "T": "You will stumble in broad daylight, and the prophets will stumble alongside you in the darkness. I will destroy the nation that bore you."
        },
        "6": {
            "L": "My people are destroyed for lack of knowledge: because thou hast rejected knowledge, I will also reject thee, that thou shalt be no priest to me: seeing thou hast forgotten the law of thy God, I will also forget thy children.",
            "M": "My people are destroyed for lack of knowledge. Because you have rejected knowledge, I will reject you from being a priest to me; and because you have forgotten the law of your God, I will also forget your children.",
            "T": "My people are perishing — not for lack of food, but for lack of knowledge of me. Because you have refused to know me, I will refuse to have you serve as my priests. Because you have forgotten the instruction of your God, I will forget your children."
        },
        "7": {
            "L": "As they were increased, so they sinned against me: therefore will I change their glory into shame.",
            "M": "The more they multiplied, the more they sinned against me; they exchanged their glory for something shameful.",
            "T": "The larger they grew, the deeper they sinned against me — so I will trade their glory for disgrace."
        },
        "8": {
            "L": "They eat up the sin of my people, and they set their heart on their iniquity.",
            "M": "They feed on the sins of my people; they are greedy for their iniquity.",
            "T": "The priests feed off the people's sins — they actually profit from Israel's guilt, so they have no incentive to call anyone back to me."
        },
        "9": {
            "L": "And there shall be, like people, like priest: and I will punish them for their ways, and reward them their doings.",
            "M": "And it will be: like people, like priest. I will punish them both for their ways and repay them for their deeds.",
            "T": "Priest and people are equally corrupt — the same judgment will fall on both. I will repay each according to what they have done."
        },
        "10": {
            "L": "For they shall eat, and not have enough: they shall commit whoredom, and shall not increase: because they have left off to take heed to the LORD.",
            "M": "They will eat but not be satisfied; they will pursue prostitution but not flourish, because they have abandoned the LORD to pursue these things.",
            "T": "They will eat but never be full; they will chase after fertility rites but bear no fruit — because they have forsaken Yahweh."
        },
        "11": {
            "L": "Whoredom and wine and new wine take away the heart.",
            "M": "Prostitution, wine, and new wine take away the understanding.",
            "T": "Lust and liquor have stolen their minds."
        },
        "12": {
            "L": "My people ask counsel at their stocks, and their staff declareth unto them: for the spirit of whoredoms hath caused them to err, and they have gone a whoring from under their God.",
            "M": "My people consult a piece of wood, and their divining rod gives them answers. For a spirit of prostitution has led them astray, and they have played the prostitute by forsaking their God.",
            "T": "My people seek guidance from a carved stick; a wooden rod is their oracle. A spirit that drives them to prostitution has made them wander — they have abandoned their God and gone after idols."
        },
        "13": {
            "L": "They sacrifice upon the tops of the mountains, and burn incense upon the hills, under oaks and poplars and elms, because the shadow thereof is good: therefore your daughters shall commit whoredom, and your spouses shall commit adultery.",
            "M": "They sacrifice on the mountaintops and burn incense on the hills, under oak and poplar and terebinth trees, because their shade is pleasant. Therefore your daughters will become prostitutes, and your daughters-in-law will commit adultery.",
            "T": "They climb to every hilltop and burn offerings under every shady tree — oak, poplar, terebinth — calling it sacred. The result? Your daughters are turning to prostitution, your daughters-in-law to adultery. The worship shapes the worshippers."
        },
        "14": {
            "L": "I will not punish your daughters when they commit whoredom, nor your spouses when they commit adultery: for themselves are separated with whores, and they sacrifice with harlots: therefore the people that doth not understand shall fall.",
            "M": "I will not punish your daughters when they commit prostitution, or your daughters-in-law when they commit adultery, because the men themselves consort with prostitutes and sacrifice with cult prostitutes — so a people without understanding will come to ruin.",
            "T": "I will not single out your daughters for punishment, or your daughters-in-law — not when the men themselves are the ones slipping off to prostitutes and sacrificing with cult workers at the shrines. A people who do not understand will be brought to ruin."
        },
        "15": {
            "L": "Though thou, Israel, play the harlot, yet let not Judah offend; and come not ye unto Gilgal, neither go ye up to Bethaven, nor swear, The LORD liveth.",
            "M": "Though you, Israel, commit adultery, do not let Judah become guilty. Do not go to Gilgal or journey up to Beth-aven, and do not swear, As the LORD lives.",
            "T": "Israel, your adultery is your own. Judah, do not follow. Stay away from Gilgal; do not go up to Beth-aven — that house of wickedness that once was Bethel. Do not take oaths in Yahweh's name there; the sanctuary is defiled."
        },
        "16": {
            "L": "For Israel slideth back as a backsliding heifer: now the LORD will feed them as a lamb in a large place.",
            "M": "For Israel has become stubborn, like a stubborn heifer. Can the LORD now pasture them like a lamb in open country?",
            "T": "Israel is as stubborn as a heifer that refuses the yoke. Will Yahweh now pasture them like a lamb in an open meadow? They are too wild for that mercy."
        },
        "17": {
            "L": "Ephraim is joined to idols: let him alone.",
            "M": "Ephraim is attached to idols; leave him alone.",
            "T": "Ephraim has bound himself to his idols. Leave him."
        },
        "18": {
            "L": "Their drink is sour: they have committed whoredom continually: her rulers with shame do love, Give ye.",
            "M": "Their drinking bouts are over; they have given themselves completely to prostitution. Their rulers dearly love shame.",
            "T": "Their drinking parties are a disgrace; they are given over completely to unfaithfulness. Their leaders love the shame of it — they cry out for more."
        },
        "19": {
            "L": "The wind hath bound her up in her wings; and they shall be ashamed because of their sacrifices.",
            "M": "A wind will sweep them away in its wings, and they will be ashamed of their sacrifices.",
            "T": "A wind will catch them up and carry them off — and when they land, their sacrifices will be shown for what they were: sources of their shame."
        }
    },
    "5": {
        "1": {
            "L": "Hear ye this, O priests; and hearken, ye house of Israel; and give ye ear, O house of the king; for judgment is toward you, because ye have been a snare on Mizpah, and a net spread upon Tabor.",
            "M": "Hear this, O priests! Listen, O house of Israel! Give ear, O house of the king! For judgment is coming against you. You have been a snare at Mizpah and a net spread on Tabor.",
            "T": "Listen to this — priests! Hear it — all Israel! Pay attention — royal house! The verdict is coming against you. You have laid a trap at Mizpah and stretched a net across Tabor to catch the people in your corruption."
        },
        "2": {
            "L": "And the revolters are profound to make slaughter: though I have been a rebuker of them all.",
            "M": "The rebels are deep in their corruption; though I have been a discipline to all of them.",
            "T": "The rebels are steeped in treachery; they have dug deep into slaughter — though I have been warning them all along."
        },
        "3": {
            "L": "I know Ephraim, and Israel is not hid from me: for now, O Ephraim, thou committest whoredom, and Israel is defiled.",
            "M": "I know Ephraim, and Israel is not hidden from me. Ephraim, you have now played the whore; Israel has become defiled.",
            "T": "I know Ephraim through and through; Israel holds nothing back from my sight. Ephraim, you have chosen prostitution — and all of Israel is contaminated by it."
        },
        "4": {
            "L": "They will not frame their doings to turn unto their God: for the spirit of whoredoms is in the midst of them, and they have not known the LORD.",
            "M": "Their deeds do not permit them to return to their God. A spirit of prostitution is within them, and they do not know the LORD.",
            "T": "The way they live makes it impossible to turn back. A spirit of prostitution has taken hold in the center of their being, and they have no real knowledge of Yahweh."
        },
        "5": {
            "L": "And the pride of Israel doth testify to his face: therefore shall Israel and Ephraim fall in their iniquity; Judah also shall fall with them.",
            "M": "Israel's arrogance testifies against him to his face. Israel and Ephraim will stumble in their iniquity, and Judah will stumble with them.",
            "T": "Israel's own pride stands as a witness against him — an open accusation. Israel and Ephraim will fall under the weight of their guilt, and Judah will fall alongside them."
        },
        "6": {
            "L": "They shall go with their flocks and with their herds to seek the LORD; but they shall not find him; he hath withdrawn himself from them.",
            "M": "They will go with their flocks and herds to seek the LORD, but they will not find him. He has withdrawn from them.",
            "T": "They will bring all their animals to the sanctuaries, hunting for Yahweh — but they will not find him. He has withdrawn from their midst."
        },
        "7": {
            "L": "They have dealt treacherously against the LORD: for they have begotten strange children: now shall a month devour them with their portions.",
            "M": "They have been unfaithful to the LORD, because they have borne illegitimate children. Now the new moon will devour them along with their fields.",
            "T": "They have betrayed Yahweh; the children they have raised are strangers to him. A month — a single cycle — will be enough to consume them and everything they think is theirs."
        },
        "8": {
            "L": "Blow ye the cornet in Gibeah, and the trumpet in Ramah: cry aloud at Bethaven, after thee, O Benjamin.",
            "M": "Sound the ram's horn in Gibeah, the trumpet in Ramah; raise the battle cry at Beth-aven: Behind you, Benjamin!",
            "T": "Blow the war-horn at Gibeah! Sound the trumpet at Ramah! Raise the alarm at Beth-aven: 'Enemy behind you, Benjamin!'"
        },
        "9": {
            "L": "Ephraim shall be desolate in the day of rebuke: among the tribes of Israel have I made known that which shall surely be.",
            "M": "Ephraim will be laid waste on the day of punishment. Among the tribes of Israel I have declared what is certain.",
            "T": "The day of reckoning will leave Ephraim in ruins. Among all the tribes of Israel I have spoken the undeniable word."
        },
        "10": {
            "L": "The princes of Judah were like them that remove the bound: therefore I will pour out my wrath upon them like water.",
            "M": "The princes of Judah have become like those who move boundary stones; I will pour out my wrath on them like water.",
            "T": "Judah's leaders have pushed past every boundary like landgrabbers who move the property markers. I will pour out my fury on them like a flood."
        },
        "11": {
            "L": "Ephraim is oppressed and broken in judgment, because he willingly walked after the commandment.",
            "M": "Ephraim is oppressed and crushed in justice, because he was determined to pursue worthless idols.",
            "T": "Ephraim is crushed, ground down by the very justice he rejected — because he chose to follow empty human commands instead of God."
        },
        "12": {
            "L": "Therefore will I be unto Ephraim as a moth, and to the house of Judah as rottenness.",
            "M": "I will be like a moth to Ephraim and like rot to the house of Judah.",
            "T": "To Ephraim I will be like a moth quietly eating through the garment of their strength; to the house of Judah, like dry rot working through the timber of their security."
        },
        "13": {
            "L": "When Ephraim saw his sickness, and Judah saw his wound, then went Ephraim to the Assyrian, and sent to king Jareb: yet could he not heal you, nor cure you of your wound.",
            "M": "When Ephraim saw his sickness and Judah saw his wound, Ephraim turned to Assyria and sent to the great king. But he cannot heal you or cure you of your wound.",
            "T": "When Ephraim finally saw how sick he was, when Judah felt how deep the wound was — instead of turning to me, Ephraim ran to Assyria and appealed to the great king. But that king cannot heal you. He cannot cure what is wrong with you."
        },
        "14": {
            "L": "For I will be unto Ephraim as a lion, and as a young lion to the house of Judah: I, even I, will tear and go away; I will take away, and none shall rescue him.",
            "M": "For I will be like a lion to Ephraim, like a young lion to the house of Judah. I myself will tear them apart and go away; I will carry them off with no one to rescue them.",
            "T": "I will come against Ephraim like a lion, like a young lion against the house of Judah. I myself will seize them and go — carry them off — and no one will be able to take them back."
        },
        "15": {
            "L": "I will go and return to my place, till they acknowledge their offence, and seek my face: in their affliction they will seek me early.",
            "M": "I will return to my place until they acknowledge their guilt and seek my face. In their distress they will earnestly seek me.",
            "T": "I will withdraw to my place and wait until they acknowledge what they have done and seek my face. When they are in desperate trouble — only then will they search for me with all their heart."
        }
    },
    "6": {
        "1": {
            "L": "Come, and let us return unto the LORD: for he hath torn, and he will heal us; he hath smitten, and he will bind us up.",
            "M": "Come, let us return to the LORD. He has torn us, but he will heal us; he has wounded us, but he will bind up our wounds.",
            "T": "Come — let us return to Yahweh.\nHe has torn us, yes, but he will heal us;\nhe has struck us down, but he will bind up our wounds."
        },
        "2": {
            "L": "After two days will he revive us: in the third day he will raise us up, and we shall live in his sight.",
            "M": "After two days he will revive us; on the third day he will raise us up, and we will live before him.",
            "T": "After two days he will give us life again;\non the third day he will raise us up —\nand we will live in his presence."
        },
        "3": {
            "L": "Then shall we know, if we follow on to know the LORD: his going forth is prepared as the morning; and he shall come unto us as the rain, as the latter and former rain unto the earth.",
            "M": "Let us press on to know the LORD; his appearing is as certain as the dawn. He will come to us like the rain, like the spring rain that waters the earth.",
            "T": "Let us press on to know Yahweh.\nHis rising is as sure as the morning sun;\nhe will come to us like the rain,\nlike the spring rains that drench the earth."
        },
        "4": {
            "L": "O Ephraim, what shall I do unto thee? O Judah, what shall I do unto thee? for your goodness is as a morning cloud, and as the early dew it goeth away.",
            "M": "What shall I do with you, Ephraim? What shall I do with you, Judah? Your love is like a morning cloud, like the early dew that quickly disappears.",
            "T": "What am I to do with you, Ephraim?\nWhat am I to do with you, Judah?\nYour faithful love — your hesed — is like the morning fog:\nit vanishes before the sun is fully up."
        },
        "5": {
            "L": "Therefore have I hewed them by the prophets; I have slain them by the words of my mouth: and thy judgments are as the light that goeth forth.",
            "M": "Therefore I have hewn them down by the prophets; I have slain them by the words of my mouth, and my judgments flash out like light.",
            "T": "That is why I have cut into you through the prophets,\nstruck you down with the words of my mouth —\nso my judgment would break through like light through storm cloud."
        },
        "6": {
            "L": "For I desired mercy, and not sacrifice; and the knowledge of God more than burnt offerings.",
            "M": "For I desire covenant loyalty and not sacrifice, the knowledge of God rather than burnt offerings.",
            "T": "What I want is faithful love — hesed — not ritual sacrifice;\nknowing me deeply, not the smoke of burnt offerings."
        },
        "7": {
            "L": "But they like men have transgressed the covenant: there have they dealt treacherously against me.",
            "M": "But like Adam they have transgressed the covenant; there they have dealt faithlessly with me.",
            "T": "But like Adam at the beginning, they broke the covenant —\nthere in the land of their blessing, they betrayed me."
        },
        "8": {
            "L": "Gilead is a city of them that work iniquity, and is polluted with blood.",
            "M": "Gilead is a city of evildoers, stained with blood.",
            "T": "Gilead — a city of wrongdoers, steeped in bloodguilt."
        },
        "9": {
            "L": "And as troops of robbers wait for a man, so the company of priests murder in the way by consent: for they commit lewdness.",
            "M": "As raiders lie in wait for someone, so do bands of priests. They murder on the road to Shechem; they commit the worst of crimes.",
            "T": "The priests are bandits waiting in ambush:\nthey murder on the road to Shechem,\ncovering up every outrage with collusion."
        },
        "10": {
            "L": "I have seen an horrible thing in the house of Israel: there is the whoredom of Ephraim, Israel is defiled.",
            "M": "I have seen a horrible thing in the house of Israel: Ephraim's prostitution is there; Israel is defiled.",
            "T": "I have seen a horrifying thing in Israel's house:\nEphraim has gone over entirely to prostitution;\nIsrael is unclean."
        },
        "11": {
            "L": "Also, O Judah, he hath set an harvest for thee, when I returned the captivity of my people.",
            "M": "Also, O Judah, a harvest is appointed for you, when I restore the fortunes of my people.",
            "T": "And you, Judah — a harvest is coming for you too,\nwhen I turn and restore the fortunes of my people."
        }
    }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'hosea')
        merge_tier(existing, HOSEA, tier_key)
        save(tier_dir, 'hosea', existing)
    print('Hosea 1–6 written.')

if __name__ == '__main__':
    main()
