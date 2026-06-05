"""
Exodus — all four layers (echo + original + context + christ).
Exodus contains the NT's most developed type-system: Passover, Sinai, manna, rock, tabernacle.
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_echo(book, data):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def load_comm(layer, book):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_comm(layer, book, data):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
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

def merge_comm(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

ECHO = {
  "3": {
    "2": [
      {"type": "allusion", "target": "Acts 7:30", "note": "The angel of the LORD appeared to Moses in the burning bush — Stephen's speech recounts the burning bush theophany; the angel of the LORD who appeared there is identified in NT use as the pre-incarnate Christ mediating the divine presence"}
    ],
    "6": [
      {"type": "allusion", "target": "Matt 22:32", "note": "I am the God of Abraham the God of Isaac and the God of Jacob — Jesus cites Exod 3:6 to prove the resurrection: if YHWH called himself the God of the patriarchs in the present tense after their deaths, they must be alive; the burning bush is the resurrection's OT proof-text"},
      {"type": "allusion", "target": "Acts 7:32", "note": "I am the God of your fathers — Stephen cites the divine self-identification from the burning bush as the founding moment of YHWH's covenant faithfulness to the patriarchs"}
    ],
    "14": [
      {"type": "fulfillment", "target": "John 8:58", "note": "I AM WHO I AM — the divine name ehyeh asher ehyeh revealed at the burning bush; Jesus's seven I AM statements (John) and especially John 8:58 ('before Abraham was, I am') are deliberate invocations of the Exodus 3:14 divine name, claiming for Jesus the YHWH-identity"}
    ]
  },
  "12": {
    "13": [
      {"type": "fulfillment", "target": "1 Cor 5:7", "note": "The blood shall be a sign on your houses — the Passover blood that protected Israel from the destroyer is the type of Christ's blood that protects from God's judgment; Christ our Passover has been sacrificed"},
      {"type": "fulfillment", "target": "John 1:29", "note": "The Passover lamb without blemish — John the Baptist's Behold the Lamb of God who takes away the sin of the world (John 1:29) identifies Jesus as the Passover Lamb; the Gospel of John times the crucifixion to coincide with the Passover lamb slaughter (John 19:14)"}
    ],
    "46": [
      {"type": "fulfillment", "target": "John 19:36", "note": "You shall not break a bone of it — the instruction for the Passover lamb is fulfilled in the soldiers' not breaking Jesus's legs at the crucifixion (John 19:36: these things took place that the Scripture might be fulfilled: not one of his bones will be broken)"}
    ]
  },
  "14": {
    "22": [
      {"type": "allusion", "target": "1 Cor 10:1-2", "note": "The Israelites walked through the sea on dry ground — Paul interprets the Red Sea crossing as a baptismal type: all were baptized into Moses in the cloud and in the sea; the exodus deliverance through water prefigures Christian baptism"},
      {"type": "allusion", "target": "Heb 11:29", "note": "By faith the people crossed the Red Sea as on dry land — the author of Hebrews includes the Red Sea crossing in the Hall of Faith; the Exodus generation's act of walking through the sea was faith in YHWH's promise"}
    ]
  },
  "16": {
    "4": [
      {"type": "fulfillment", "target": "John 6:31-35", "note": "Behold I am about to rain bread from heaven for you — the manna in the wilderness is the backdrop for Jesus's Bread of Life discourse; the crowd cites Ps 78:24 (he gave them bread from heaven) and Jesus corrects: my Father gives you the true bread from heaven, and I am that bread of life"},
      {"type": "allusion", "target": "1 Cor 10:3", "note": "The spiritual food of the manna — Paul calls the manna spiritual food and the rock that followed them spiritual drink; both are Christological types that point to the one spiritual sustainer: Christ"}
    ]
  },
  "17": {
    "6": [
      {"type": "fulfillment", "target": "1 Cor 10:4", "note": "Behold I will stand before you on the rock at Horeb and you shall strike the rock and water shall come out — Paul identifies this rock explicitly with Christ: the rock was Christ; the water-giving rock in the wilderness is the type of the one who gives living water (John 7:38-39)"},
      {"type": "allusion", "target": "John 7:38", "note": "Rivers of living water will flow from within him — Jesus's promise at the Feast of Tabernacles echoes the water-from-the-rock tradition; the rock that gave water is the type, Christ is the antitype who gives the Spirit as living water"}
    ]
  },
  "19": {
    "5": [
      {"type": "allusion", "target": "1 Pet 2:9", "note": "You shall be to me a kingdom of priests and a holy nation — the Sinai covenant charter (Exod 19:5-6) is applied to the church in 1 Pet 2:9: you are a chosen race, a royal priesthood, a holy nation, a people for his own possession; the church inherits the covenant community's calling"},
      {"type": "allusion", "target": "Rev 1:6", "note": "He has made us a kingdom, priests to his God and Father — Revelation applies Exod 19:6 to the redeemed: Christ has made us a kingdom and priests; the Sinai covenant's Israel-as-kingdom-of-priests is fulfilled in the church through the new covenant"}
    ]
  },
  "20": {
    "2": [
      {"type": "allusion", "target": "Matt 5:17", "note": "You shall not murder / commit adultery / steal — the Decalogue (Exod 20) is the background for the Sermon on the Mount's antitheses; Jesus does not abolish but fulfills, deepening the law to its heart-level intent"},
      {"type": "allusion", "target": "Rom 7:7", "note": "You shall not covet — Paul cites the tenth commandment as the law that showed him sin: I would not have known covetousness if the law had not said You shall not covet; the Decalogue is the very place where the law's diagnostic function is clearest"}
    ]
  },
  "24": {
    "8": [
      {"type": "fulfillment", "target": "Matt 26:28", "note": "Behold the blood of the covenant that the LORD has made with you — Moses sprinkles the covenant blood at Sinai (Exod 24:8); Jesus at the Last Supper calls the cup my blood of the covenant poured out for many; the new covenant blood corresponds to the Sinai covenant blood"},
      {"type": "fulfillment", "target": "Heb 9:20", "note": "This is the blood of the covenant that God commanded for you — Hebrews cites Exod 24:8 in the context of Christ's blood as the new covenant's ratifying blood; the old covenant's blood-sprinkling is the type of the new covenant's once-for-all blood"}
    ]
  },
  "25": {
    "9": [
      {"type": "allusion", "target": "Heb 8:5", "note": "Exactly as I show you concerning the pattern of the tabernacle — the Sinai tabernacle was built according to the heavenly pattern (tabnit); Hebrews argues that the earthly tabernacle is a shadow and copy of the heavenly sanctuary where Christ now ministers as high priest"}
    ],
    "40": [
      {"type": "allusion", "target": "Heb 9:1-5", "note": "The ark of the covenant with the mercy seat — Hebrews describes the tabernacle furnishings (golden lampstand, table, bread of the Presence, incense altar, ark with mercy seat) to show that the old covenant's physical sanctuary points to the greater heavenly sanctuary accessed through Christ's blood"}
    ]
  },
  "32": {
    "6": [
      {"type": "allusion", "target": "1 Cor 10:7", "note": "The people sat down to eat and drink and rose up to play — Paul cites Exod 32:6 (the golden calf incident) as a warning against idolatry: do not be idolaters as some of them were; the wilderness generation's failure is the warning example for the Corinthians tempted by idol feasts"}
    ]
  },
  "33": {
    "7": [
      {"type": "allusion", "target": "Heb 13:13", "note": "Moses took the tent and pitched it outside the camp — the tent of meeting outside the camp prefigures Jesus suffering outside the gate (Heb 13:12-13); the sacred meeting-space was outside the camp, as the place of sacrifice was outside Jerusalem"}
    ]
  },
  "34": {
    "29": [
      {"type": "allusion", "target": "2 Cor 3:7-18", "note": "Moses did not know that the skin of his face shone because he had been talking with God — the veil Moses put over his face (Exod 34:33-35) is Paul's central image in 2 Cor 3: the old covenant glory was fading and veiled; the new covenant's greater glory is unveiled; the veil is removed in Christ"},
      {"type": "allusion", "target": "Matt 17:2", "note": "His face shone like the sun — the Transfiguration's shining face of Jesus echoes Moses's shining face at Sinai; Jesus is the new and greater Moses whose glory is not derivative but intrinsic, not fading but permanent"}
    ]
  }
}

ORIGINAL = {
  "3": {
    "14": "<p><strong>ehyeh asher ehyeh</strong> (<em>ʾehyeh ʾăšer ʾehyeh</em>): 'I AM WHO I AM' or 'I WILL BE WHAT I WILL BE.' The divine name is derived from the verb <em>hayah</em> (to be). The Tetragrammaton (YHWH) is likely the Qal imperfect form of <em>hayah</em> — 'He is' or 'He will be.' The name declares YHWH's self-existence and sovereign freedom: he does not derive his existence from anything outside himself; his being is its own definition. John's seven I AM sayings (John 6:35; 8:12; 10:9, 11; 11:25; 14:6; 15:1) and the absolute 'I am' (John 8:58; 18:5-6) are deliberate invocations of the Exodus 3:14 name, claiming for the Son the same underived self-existence.</p>"
  },
  "12": {
    "5": "<p><strong>seh tamim</strong> (<em>śeh tāmîm</em>): 'a lamb without blemish' — the Passover lamb must be <em>tamim</em> (perfect, without defect), the sacrificial standard that applies to all Levitical offerings (Lev 22:19-20) and is applied to Christ in 1 Pet 1:19: 'without blemish or spot.' The lamb is also <em>ben shanah</em> (in its first year), symbolically in the prime of life — not old and worn out. The NT applies the typology systematically: Christ is the Passover lamb (1 Cor 5:7), his bones were not broken per Exod 12:46 (John 19:36), and his blood marks and protects the new covenant community.</p>"
  },
  "20": {
    "2": "<p><strong>anochi YHWH eloheicha asher hotzeiticha meeretz mitzraim mibeit avadim</strong>: 'I am YHWH your God, who brought you out of the land of Egypt, out of the house of slavery.' The Decalogue opens not with a command but with a redemption narrative — the commands follow from the prior act of grace. YHWH does not say 'obey me so that I will be your God and bring you out' but 'I brought you out; therefore I am your God; therefore obey.' The evangelical-imperative structure of the Decalogue is: grace, then obligation. Paul's ethical sections follow the same pattern: Romans 1-11 (gospel), then 12-16 (imperatives); Galatians 1-4 (grace), then 5-6 (walk).</p>"
  },
  "25": {
    "9": "<p><strong>kekol asher ani mareeh otcha et tabnit hamishkan veet tabnit kol kelav veken taashu</strong>: 'Exactly as I show you concerning the pattern [<em>tabnit</em>] of the tabernacle, and of all its furniture, so you shall make it.' The Hebrew <em>tabnit</em> (pattern/model) implies the earthly tabernacle is a copy of a heavenly original. Hebrews (8:5) quotes this verse explicitly (using LXX <em>typos</em> — pattern, type) to argue that the Levitical priests serve a copy and shadow of the heavenly things. The tabernacle's typological function is not a later Christian imposition but is built into the original instructions: Moses saw the heavenly original; Israel built the earthly copy.</p>"
  },
  "34": {
    "6": "<p><strong>YHWH YHWH el rachum vechanun erech apayim verav chesed veemet</strong>: 'YHWH YHWH, a God merciful and gracious, slow to anger, and abounding in steadfast love [<em>chesed</em>] and faithfulness [<em>emet</em>].' The thirteen attributes of divine mercy (mid-dot harachamim) became a cornerstone of Jewish liturgical theology, recited on fast days and festivals. <em>Chesed</em> (covenant love, steadfast love, lovingkindness) is perhaps the OT's richest theological term — it combines loyalty, love, mercy, and covenant-faithfulness into a single word. John's 'grace and truth' (John 1:14, 17) is likely a translation of <em>chesed veemet</em>, applying Exod 34:6's divine attributes to the incarnate Word.</p>"
  }
}

CONTEXT = {
  "1": {
    "11": "<p>The historical context of the Exodus is debated: the most common evangelical dating places the Exodus ca. 1446 BCE (the 'early date,' based on 1 Kings 6:1's 480 years from Exodus to Solomon's temple ca. 966 BCE), during Thutmose III's reign. The 'late date' (ca. 1270-1250 BCE, during Ramesses II's reign) is favored by many archaeologists based on the cities Pithom and Ramesses mentioned in Exod 1:11. The Merneptah Stele (ca. 1208 BCE) mentions Israel as a people already in Canaan, providing a terminus ad quem. The question remains open; the theological significance of the Exodus is independent of the exact date.</p>"
  },
  "12": {
    "1": "<p>The Passover (Heb. <em>pesach</em>) became the foundational festival of Israelite identity — the annual re-enactment and remembrance of YHWH's redemptive act. The Passover Seder developed in the Second Temple period and was the meal Jesus shared with his disciples on the night of his arrest. Jesus's identification of the cup with his blood and the bread with his body (Luke 22:19-20) reinterprets the Passover meal through the lens of his approaching death: the new exodus is accomplished through his death as the new Passover lamb. Paul's 'Christ our Passover has been sacrificed' (1 Cor 5:7) is the theological crystallization of this identification.</p>"
  },
  "19": {
    "1": "<p>The Sinai covenant is the central structuring event of the OT: it establishes the constitutional framework of Israel's relationship with YHWH. Its suzerainty-treaty structure (parallel to Hittite treaties: preamble, historical prologue, stipulations, blessings/curses, witnesses) places YHWH as the great king and Israel as his vassal. The Decalogue (20:1-17) is the covenant's summary stipulations. The Book of the Covenant (20:22-23:33) elaborates case law. The covenant-inauguration ceremony (24:1-11) seals the relationship with blood and a covenant meal. Hebrews 12:18-24 contrasts the terrors of Sinai with the joy of Zion — the old covenant's thunders and fire point forward to the new covenant's completed mediation in Christ.</p>"
  },
  "25": {
    "1": "<p>The tabernacle instructions (Exod 25-31) and their execution (35-40) occupy more chapters in Exodus than any other section. The tabernacle is the theological center of the wilderness narrative: YHWH's presence (kavod) dwelling among Israel in the portable sanctuary. Its structure (outer court, holy place, most holy place) reflects the graduated holiness of sacred space that culminates in the ark and mercy seat where YHWH meets with Israel. Solomon's temple is the permanent version of this portable structure. The NT develops the typological chain: tabernacle → temple → Christ's body (John 2:21) → the church as temple (1 Cor 3:16) → the new Jerusalem as the final dwelling of God with his people (Rev 21:3).</p>"
  }
}

CHRIST = {
  "12": {
    "13": "<p>A fulfillment: 'When I see the blood, I will pass over you, and no plague will befall you to destroy you when I strike the land of Egypt.' The Passover blood on the doorposts is the OT's most developed type of substitutionary atonement: an innocent lamb dies; its blood marks the household; the destroyer passes over those marked. Paul makes the typological identification explicit: 'Christ our Passover has been sacrificed' (1 Cor 5:7). John structures his Gospel so the crucifixion occurs when the Passover lambs are being slaughtered in the temple (John 19:14), and notes the non-breaking of bones fulfills Exod 12:46. The Passover is not merely a historical parallel but the interpretive key YHWH planted in Israel's annual liturgy to explain, centuries in advance, the theological meaning of the cross.</p>"
  },
  "14": {
    "22": "<p>A type: 'And the people of Israel went into the midst of the sea on dry ground, the waters being a wall to them on their right hand and on their left.' Paul explicitly calls the Red Sea crossing a baptismal type: 'all were baptized into Moses in the cloud and in the sea' (1 Cor 10:1-2). The structure is identical to Christian baptism: God's redemptive act through a threshold of water, from slavery into freedom, into covenant relationship. But the antitype is greater: baptism into Christ is death and resurrection with Christ (Rom 6:3-4), not merely deliverance from one earthly power. Moses led Israel through the sea; Christ leads his people through death itself.</p>"
  },
  "16": {
    "15": "<p>A type: 'It is manna' (or 'What is it?') — bread from heaven that YHWH provides. Jesus in John 6 identifies himself as the fulfillment of the manna type: 'Your fathers ate the manna in the wilderness, and they died. This is the bread that comes down from heaven, so that one may eat of it and not die. I am the living bread that came down from heaven' (John 6:49-51). The typological contrast is sharp: the manna sustained physical life temporarily; Christ gives eternal life. The manna was perishable; Christ is permanent. The manna was provided daily; Christ is given once. The Lord's Supper as ongoing eating of Christ (John 6:53-56) is the enacted fulfillment of the manna's promise.</p>"
  },
  "25": {
    "22": "<p>A type: 'There I will meet with you, and from above the mercy seat, from between the two cherubim that are on the ark of the testimony, I will speak with you.' The mercy seat (<em>kapporet</em>, from <em>kipper</em>, to atone/cover) is the lid of the ark, sprinkled with blood on Yom Kippur. Paul in Romans 3:25 calls Christ a <em>hilasterion</em> — the LXX word for the mercy seat. Christ is both the priest who offers the sacrifice and the mercy seat on which the blood is placed; he is both offerer and the place of offering, the one who makes atonement and the locus where God and humanity meet. The tabernacle's most restricted and holy object — accessible only once a year, only by the high priest, only with blood — is fulfilled in Christ who provides permanent access to God.</p>"
  }
}

def main():
    e = load_echo('exodus')
    merge_echo(e, ECHO)
    save_echo('exodus', e)

    c = load_comm('mkt-original', 'exodus')
    merge_comm(c, ORIGINAL)
    save_comm('mkt-original', 'exodus', c)

    c = load_comm('mkt-context', 'exodus')
    merge_comm(c, CONTEXT)
    save_comm('mkt-context', 'exodus', c)

    c = load_comm('mkt-christ', 'exodus')
    merge_comm(c, CHRIST)
    save_comm('mkt-christ', 'exodus', c)

    print('exodus: all 4 layers written')

if __name__ == '__main__':
    main()
