"""
Echo layer — 1 Corinthians chapters 9–11
Output: data/echoes/1corinthians.json (adds chs9-11)

Key OT resonances:
- 9:9 = Deut 25:4 (don't muzzle the ox) — explicit citation
- 9:13 = Num 18:8 / Deut 18:1 (temple ministry and eating)
- 10:1-2 = Exod 13-14 (cloud and sea)
- 10:3 = Exod 16 / Ps 78:24-25 (manna as spiritual food)
- 10:4 = Num 20:11 (the accompanying rock)
- 10:5 = Num 14:29-35 (laid low in the wilderness)
- 10:7 = Exod 32:6 (golden calf revelry) — explicit citation
- 10:8 = Num 25:1-9 (Baal Peor)
- 10:9 = Num 21:4-6 (venomous snakes)
- 10:10 = Num 16:41-49 (grumbling and the destroying angel)
- 10:20 = Deut 32:17 (sacrifices to demons)
- 10:22 = Deut 32:21 / Exod 34:14 (provoking divine jealousy)
- 10:26 = Ps 24:1 (earth is the Lord's) — explicit citation
- 11:7 = Gen 1:26-27 (image and glory of God)
- 11:8-9 = Gen 2:21-23 (woman from man)
- 11:25 = Jer 31:31-34 (new covenant in my blood)
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_echo(book, data):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_echo(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, entries in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entries
            else:
                seen = {(e['type'], e['target']) for e in existing[ch][v]}
                for e in entries:
                    if (e['type'], e['target']) not in seen:
                        existing[ch][v].append(e)
                        seen.add((e['type'], e['target']))

ECHOES = {
  "9": {
    "9": [
      {"type": "quote", "target": "Deut 25:4", "note": "Do not muzzle an ox while it is treading out grain — Paul cites Deut 25:4 directly to argue that workers in God's service deserve support. His interpretive move is exegetically provocative: he claims the command was not primarily about oxen but 'written for our sake.' This typological reading treats the agricultural law as a prefigurement of the apostolic situation, the ox as a figure for the human laborer in God's harvest."}
    ],
    "13": [
      {"type": "allusion", "target": "Num 18:8-10", "note": "I am giving you the responsibility of the offerings presented to me... whatever is set apart from the holy offerings the Israelites present to the LORD I give to you and your sons — YHWH's provision for the priests from the altar-portions establishes the paradigm Paul applies: those who serve at the altar eat from the altar. The priestly maintenance from temple offerings is the OT precedent he argues the gospel ministry follows."},
      {"type": "allusion", "target": "Deut 18:1-2", "note": "The Levitical priests... shall have no allotment or inheritance with Israel. They shall live on the food offerings presented to the LORD — Moses reaffirms the priestly support principle in Deuteronomy, grounding the Levites' livelihood directly in their service at the altar. Paul invokes this dual-Torah witness (both Num 18 and Deut 18) to establish the ministry-support principle across the whole Torah tradition."}
    ]
  },
  "10": {
    "1": [
      {"type": "type", "target": "Exod 13:21-22", "note": "By day the LORD went ahead of them in a pillar of cloud to guide them on their way and by night in a pillar of fire — the cloud that accompanied Israel through the wilderness is the first of Paul's five types in vv.1-4. The cloud (divine presence and protection) and the sea together constitute the original saving event; Paul's community participates in its antitype through baptism and the Supper."},
      {"type": "type", "target": "Exod 14:19-22", "note": "The angel of God withdrew and went behind them. The pillar of cloud also moved from in front of them and stood behind them... Moses stretched out his hand over the sea... the Israelites went through the sea on dry ground — the sea-crossing is the second type; as Israel passed through the sea under the cloud and was thereby constituted as YHWH's redeemed people, so baptism constitutes the new community."}
    ],
    "3": [
      {"type": "type", "target": "Exod 16:14-15", "note": "When the dew was gone, thin flakes like frost on the ground appeared on the desert floor... Moses said to them: It is the bread the LORD has given you to eat — the manna is the third type: spiritual food from heaven that sustained the community in the wilderness. Paul reads the manna as a type of the eucharistic bread, both pointing to the divine provision that sustains the covenant community through the wilderness of this age."},
      {"type": "allusion", "target": "Ps 78:24-25", "note": "He rained down manna for the people to eat; he gave them the grain of heaven. Human beings ate the bread of angels — the psalmist's reflective interpretation of the manna as heavenly bread (bread of angels, lehem abirim) already elevated the manna beyond ordinary provision. Paul builds on this interpretive tradition when he calls it spiritual food (pneumatikon broma)."}
    ],
    "4": [
      {"type": "type", "target": "Num 20:2-11", "note": "So Moses took the staff from the LORD's presence, as he commanded him. He and Aaron gathered the assembly together in front of the rock and Moses said to them... Moses raised his arm and struck the rock twice with his staff. Water gushed out — the rock-water miracle is the fourth type: spiritual drink from the accompanying rock. Paul identifies the rock with Christ, making the pre-incarnate Christ the source of Israel's wilderness water — a striking typological claim about Christ's presence in the first Exodus."},
      {"type": "allusion", "target": "Num 21:16-17", "note": "From there they continued on to Beer, where the well was that the LORD spoke of when he said to Moses: Gather the people together and I will give them water — the second rock-water provision in Numbers, also in a wilderness context. Rabbinic tradition (b. Taanit 9a) elaborated this into a traveling well that accompanied Israel throughout the wilderness; Paul's language of a rock that accompanied them may engage this midrashic tradition."}
    ],
    "5": [
      {"type": "allusion", "target": "Num 14:29-30", "note": "In this wilderness your bodies will fall — every one of you twenty years old or more who was counted in the census and who has grumbled against me. Not one of you will enter the land I swore with uplifted hand to make your home — God's judgment on the exodus generation who received every benefit of the cloud, the sea, the manna, and the water, but fell in the wilderness through unbelief. The sacramental gifts are not automatic protection; reception without faith leads to judgment."}
    ],
    "7": [
      {"type": "quote", "target": "Exod 32:6", "note": "The people sat down to eat and drink and got up to indulge in revelry — Paul cites Exod 32:6 directly as the first of four wilderness-failure examples. The golden calf episode is the paradigmatic instance of idolatry: while Moses received the Torah on Sinai, the people demanded a visible god and celebrated its making with eating, drinking, and revelry. Paul applies this directly to the Corinthian problem of food offered to idols at pagan festivals."}
    ],
    "8": [
      {"type": "allusion", "target": "Num 25:1-9", "note": "While Israel was staying in Shittim, the men began to indulge in sexual immorality with Moabite women, who invited them to the sacrifices to their gods — the Baal Peor incident is Paul's second wilderness-failure example: sexual immorality specifically connected to idolatrous cult meals. The double failure (immorality + idol worship) maps precisely onto the Corinthian problem of attending temple banquets where both occurred."}
    ],
    "9": [
      {"type": "allusion", "target": "Num 21:4-6", "note": "The people grew impatient on the way; they spoke against God and against Moses, saying... Then the LORD sent venomous snakes among them; they bit the people and many Israelites died — Paul's third example: testing Christ (who was the rock in the wilderness) as Israel tested God at Massah and in the bronze serpent incident. The snakes were divine judgment on Israel's grumbling-as-testing; the parallel is to the Corinthians testing God's patience by their conduct at the Supper."}
    ],
    "10": [
      {"type": "allusion", "target": "Num 16:41-49", "note": "The next day the whole Israelite community grumbled against Moses and Aaron... plague had started among the people, and 14,700 people died from the plague, in addition to those who had died — the grumbling of Israel after the Korah-Dathan-Abiram judgment brought the destroying angel (the plague). Paul's fourth example targets the Corinthians who murmur against Paul's authority, analogizing them to Israel who grumbled against Moses."}
    ],
    "20": [
      {"type": "allusion", "target": "Deut 32:17", "note": "They sacrificed to false gods, which are not God — gods they had not known, gods that recently appeared, gods your ancestors did not fear — Paul's identification of pagan idol-sacrifices as offered to demons (daimonia) draws directly on Deut 32:17 (LXX: they sacrificed to demons, not to God). The Song of Moses in Deut 32 is Paul's OT authority for the claim that behind pagan idol-worship stands demonic reality, making participation in idol meals a communion with demons rather than mere cultural accommodation."}
    ],
    "22": [
      {"type": "allusion", "target": "Deut 32:21", "note": "They made me jealous by what is no god and angered me with their worthless idols — the Song of Moses (Deut 32:21) provides Paul's framework for the jealousy-language: as Israel provoked divine jealousy through idol-worship, so the Corinthians who participate in both the Lord's table and the demon's table provoke the same jealousy. Paul's rhetoric Are we stronger than he? recalls the Song's assertion that YHWH's jealousy leads to judgment."},
      {"type": "allusion", "target": "Exod 34:14", "note": "Do not worship any other god, for the LORD, whose name is Jealous, is a jealous God — YHWH's name Jealous (qanna) at the covenant renewal after the golden calf establishes the theological basis for Paul's warning: to share in both the Lord's table and the demon's table is to invoke the divine jealousy that is definitional to the covenant."}
    ],
    "26": [
      {"type": "quote", "target": "Ps 24:1", "note": "The earth is the LORD's, and everything in it, the world, and all who live in it — Paul cites Ps 24:1 to ground the principle that meat sold in the market (even if previously offered to idols) is not spiritually contaminated, because the earth and all its produce belong to YHWH, not to the idols. The same psalm grounds both the freedom to eat (everything belongs to God) and, by implication, the limit: one may not eat where it would suggest sharing in the demonic."}
    ]
  },
  "11": {
    "7": [
      {"type": "allusion", "target": "Gen 1:26-27", "note": "Let us make mankind in our image, in our likeness... so God created mankind in his own image, in the image of God he created them; male and female he created them — Paul grounds the head-covering argument in the creation order: man as the image and glory of God (Gen 1:26-27). His distinction between man as image-of-God and woman as glory-of-man works from the Genesis sequence and the creation purpose narrative in Genesis 2."}
    ],
    "8": [
      {"type": "allusion", "target": "Gen 2:21-23", "note": "So the LORD God caused the man to fall into a deep sleep; and while he was sleeping, he took one of the man's ribs and then closed up the place with flesh. Then the LORD God made a woman from the rib he had taken out of the man — the origin of woman from man (v.8: man did not come from woman, but woman from man) is grounded in the rib-creation narrative of Gen 2. Paul reads Genesis 2 as establishing a creational order that is reflected in the worship assembly's decorum."}
    ],
    "9": [
      {"type": "allusion", "target": "Gen 2:18", "note": "The LORD God said: It is not good for the man to be alone. I will make a helper suitable for him — the purpose of woman's creation (a helper suitable for him) is Paul's OT basis for v.9: man was not created for the sake of woman, but woman for the sake of man. The creation-order argument draws from the sequential narrative of Gen 2 to establish the relational structure that worship decorum reflects."}
    ],
    "25": [
      {"type": "fulfillment", "target": "Jer 31:31-34", "note": "The days are coming, declares the LORD, when I will make a new covenant with the people of Israel and with the people of Judah... I will put my law in their minds and write it on their hearts — the eucharistic cup as the new covenant in my blood (v.25) directly cites Jeremiah's new covenant promise. The covenant that Jeremiah prophesied — replacing the Sinai covenant broken by Israel — is inaugurated in Jesus's blood. The Lord's Supper is the new-covenant meal, replacing the covenant-meal of Exod 24:9-11 (the elders who ate and drank in the presence of God on Sinai)."},
      {"type": "allusion", "target": "Exod 24:8", "note": "Moses then took the blood, sprinkled it on the people and said: This is the blood of the covenant that the LORD has made with you in accordance with all these words — the Sinai covenant was ratified by blood sprinkled on the altar and the people; Jesus's word This cup is the new covenant in my blood echoes this covenant-blood formula while announcing a covenant that supersedes Sinai."}
    ]
  }
}

def main():
    existing = load_echo('1corinthians')
    merge_echo(existing, ECHOES)
    save_echo('1corinthians', existing)
    total = sum(len(v) for v in existing.values())
    print(f'1 Corinthians echo: {len(existing)} chapters, {total} verses with connections.')

if __name__ == '__main__':
    main()
