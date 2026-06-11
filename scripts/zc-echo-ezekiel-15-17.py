"""
echo layer: Ezekiel 15-17
Key echo clusters:
  - ch15 useless vine wood → John 15:6 (branches thrown into fire)
  - ch16 abandoned infant → Eph 2:1-5; everlasting covenant → Heb 13:20
  - ch16 Sodom comparison → Matt 11:23-24; spiritual adultery → James 4:4
  - ch17 cedar twig on mountain → Mark 4:32 (mustard-tree/birds nesting); messianic Branch
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / "data" / "echoes" / f"{book}.json"
    return json.loads(p.read_text()) if p.exists() else {}

def save_echo(book, data):
    p = ROOT / "data" / "echoes" / f"{book}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f"  wrote {p.relative_to(ROOT)}")

def merge_echo(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, entries in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entries
            else:
                seen = {(e["type"], e["target"]) for e in existing[ch][v]}
                for e in entries:
                    if (e["type"], e["target"]) not in seen:
                        existing[ch][v].append(e)
                        seen.add((e["type"], e["target"]))

EZEKIEL_ECHOES = {
  "15": {
    "2": [
      {"type": "allusion", "target": "John 15:1-6", "note": "How is the wood of the vine better than any tree of the forest? — the rhetorical question of the useless vine frames Jesus's true-vine discourse: I am the true vine and my Father is the vinedresser (John 15:1); the vine that fails to produce fruit is cut off and thrown into the fire (John 15:6), precisely the fate Ezekiel's useless vine wood faces — good only for burning"}
    ],
    "6": [
      {"type": "allusion", "target": "John 15:6", "note": "As I have given the vine wood to the fire for fuel, so have I given up the inhabitants of Jerusalem — the judgment that falls on the fruitless vine is the backdrop for Jesus's warning: if anyone does not abide in me he is thrown away like a branch and withers; and the branches are gathered, thrown into the fire, and burned (John 15:6); the burned inhabitants of Jerusalem are the eschatological pattern Jesus applies to branches that fail to abide in him"}
    ]
  },
  "16": {
    "6": [
      {"type": "allusion", "target": "Eph 2:1-5", "note": "When I passed by you and saw you lying in your blood, I said to you, Live! — the divine address to the abandoned, blood-covered infant who has no right to life is the OT type of the grace described in Eph 2:1-5: you were dead in trespasses and sins ... but God, being rich in mercy, because of the great love with which he loved us, even when we were dead in our trespasses, made us alive together with Christ; Israel found lying in its blood is humanity found dead in sin"},
      {"type": "allusion", "target": "Rom 5:8", "note": "I saw you lying in your blood and said, Live! — God's election of the abandoned infant who had no claim on life is Paul's pattern for grace: God shows his love for us in that while we were still sinners, Christ died for us (Rom 5:8); the grace that precedes all human response or merit is enacted in Ezekiel's foundling narrative"}
    ],
    "8": [
      {"type": "allusion", "target": "Rev 19:7-9", "note": "I spread the corner of my garment over you and covered your nakedness; I gave you my oath and entered into a covenant with you — the covenant-marriage initiated by God (covering nakedness, pledge of faithfulness) is the OT type of the marriage supper of the Lamb (Rev 19:7-9): the bride has made herself ready and fine linen is the righteous deeds of the saints; the nakedness covered by God's covenant oath is the nakedness clothed in Christ's righteousness"},
      {"type": "allusion", "target": "Ruth 3:9", "note": "I spread the corner of my garment over you — Boaz's spreading of his garment over Ruth at the threshing floor (Ruth 3:9) enacts the same covenant-marriage gesture; Boaz as kinsman-redeemer anticipates the one who spreads the divine garment over the abandoned, covering all covenant shame with pledged faithfulness"}
    ],
    "32": [
      {"type": "allusion", "target": "Matt 12:39", "note": "You are an adulterous wife who receives strangers instead of her husband — Jesus calls his generation an evil and adulterous generation (Matt 12:39; 16:4), drawing on the prophetic tradition (Ezekiel, Hosea, Jeremiah) of Israel's covenant unfaithfulness as spiritual adultery; seeking signs from Jesus while rejecting him is the adultery of receiving strangers instead of the covenant husband"},
      {"type": "allusion", "target": "Jas 4:4", "note": "The adulterous wife who pursues lovers rather than her covenant husband — James applies this exact tradition directly to NT believers: do you not know that friendship with the world is enmity with God? Whoever therefore wishes to be a friend of the world makes himself an enemy of God (Jas 4:4); the Ezekielian adultery metaphor becomes the NT's vocabulary for idolatrous attachment to worldly systems"}
    ],
    "48": [
      {"type": "allusion", "target": "Matt 11:23-24", "note": "Your sister Sodom and her daughters have not done what you and your daughters have done — Ezekiel's shocking comparison (Jerusalem is worse than Sodom) is the background for Jesus's even more shocking pronouncement: if the mighty works done in Capernaum had been done in Sodom it would have remained until this day; it will be more tolerable on the day of judgment for Sodom than for you (Matt 11:23-24); those who reject the gospel are worse than Sodom's pre-gospel paganism"}
    ],
    "60": [
      {"type": "fulfillment", "target": "Heb 13:20", "note": "I will remember my covenant with you from the days of your youth and establish for you an everlasting covenant — despite Israel's radical unfaithfulness, God's covenant fidelity persists; Hebrews 13:20 identifies the new covenant as the fulfillment of this promise: the God of peace who brought again from the dead our Lord Jesus, the great shepherd of the sheep, by the blood of the eternal covenant (<em>diathēkē aiōnion</em>); the everlasting covenant Ezekiel promises is the covenant sealed by Christ's blood"},
      {"type": "fulfillment", "target": "2 Cor 5:21", "note": "When I make atonement for you for all that you have done (v. 63) — the divine promise to make atonement for Israel despite the broken covenant is fulfilled in Christ: God made him to be sin who knew no sin, so that in him we might become the righteousness of God (2 Cor 5:21); the atonement that silences shame and covers covenant-breaking is the cross"}
    ]
  },
  "17": {
    "22": [
      {"type": "fulfillment", "target": "Isa 11:1", "note": "I myself will take a shoot from the topmost branch of the high cedar and plant it on a high and lofty mountain — the tender young twig from the cedar's crown is the messianic Branch of Isaiah 11:1 (a shoot from the stump of Jesse; a branch from his roots shall bear fruit); both passages use the same botanical imagery for the Davidic Messiah who springs from apparent ending to become a great tree; Ezekiel's twig planted by God is the divine initiative of the incarnation"},
      {"type": "fulfillment", "target": "Zech 6:12", "note": "I myself will take a tender twig and plant it — the divine first-person planting of the messianic shoot on the mountain of Israel connects to Zechariah's Branch oracle: Behold, the man whose name is the Branch: for he shall branch out from his place and shall build the temple of the LORD (Zech 6:12); what God plants in Ezekiel's vision the Branch builds in Zechariah's — both refer to the Davidic Messiah established by divine initiative on Mount Zion"}
    ],
    "23": [
      {"type": "fulfillment", "target": "Mark 4:32", "note": "Under it every kind of bird will live; in the shadow of its branches they will nest — the cedar planted on Israel's mountain where birds from all nations nest is the OT type Jesus takes up in the parable of the mustard seed: when grown it is greater than all garden plants and becomes a tree, so that the birds of the air come and make nests in its branches (Mark 4:32; Matt 13:32; Luke 13:19); the nations sheltering under the Messianic tree is Ezekiel's vision applied to the kingdom of God that grows from the small seed of Jesus's ministry"},
      {"type": "allusion", "target": "Dan 4:12", "note": "Every kind of bird nesting in the shadow of its branches — Daniel's vision of the great tree (Dan 4:12) uses the identical imagery of birds nesting in a great tree's branches; both Ezekiel's planted cedar and Daniel's cosmic tree draw on the ancient Near Eastern image of the world-tree sheltering all peoples; Jesus's mustard-seed parable deliberately invokes this tradition to describe the kingdom of God"}
    ],
    "24": [
      {"type": "allusion", "target": "Luke 1:52", "note": "I the LORD bring down the high tree, exalt the low tree, dry out the green tree, and make the dry tree flourish — the divine reversal of human status hierarchies (high/low, green/dry) is the pattern Mary sings at the Magnificat: he has brought down the mighty from their thrones and exalted those of humble estate (Luke 1:52); the tree-reversals of Ezekiel's oracle are the cosmic pattern of God's kingdom that Jesus's advent enacts"}
    ]
  }
}

def main():
    e = load_echo("ezekiel")
    merge_echo(e, EZEKIEL_ECHOES)
    save_echo("ezekiel", e)
    for ch in ["15", "16", "17"]:
        vv = e.get(ch, {})
        print(f"  ch{ch}: {len(vv)} verse(s) with echoes")

if __name__ == "__main__":
    main()
