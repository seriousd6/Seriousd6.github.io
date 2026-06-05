"""
mkt-christ layer — 1 Corinthians all 16 chapters
Output: data/commentary/mkt-christ/1corinthians.json

1 Corinthians presents Christ as crucified wisdom (ch1-2),
the foundation of the church (ch3), the Passover lamb (ch5),
the spiritual rock (ch10), the head of the eucharistic body (ch11),
and the firstfruits of the resurrection (ch15).
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_comm(layer, book):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_comm(layer, book, data):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_comm(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

CHRIST = {
  "1": {
    "18": "<p>A direct revelation: 'The word of the cross is foolishness to those who are perishing, but to us who are being saved it is the power of God.' Paul's theologia crucis (theology of the cross) is the irreducible Christological claim: God's power is revealed not in imperial might or philosophical sophistry but in the crucified Christ. The cross does not merely illustrate a timeless spiritual principle — it is the specific historical event in which God's wisdom and power are concentrated and disclosed. Every Corinthian pretension to superior wisdom is measured against this standard: does it stand or fall before the cross?</p>",

    "30": "<p>A direct revelation: 'He is the source of your life in Christ Jesus, whom God made our wisdom, righteousness, sanctification, and redemption.' Christ as the personified Wisdom of God (cf. Prov 8:22-31; Sir 24; Wis 7:22-8:1) answers Corinthian competition over human wisdom with a Christological absorbing of all wisdom into one person. The four nouns (wisdom, righteousness, sanctification, redemption) are not merely metaphors but ontological claims: in Christ, believers receive these realities as gifts, not achievements. This is the Christological inversion of the Torah: where Torah promised blessing through obedience, Christ provides the reality the Torah pointed toward.</p>"
  },
  "5": {
    "7": "<p>A fulfillment: 'Christ our Passover lamb has been sacrificed.' <em>Pascha hemon etythē Christos</em> — Paul's most explicit identification of Christ with the Passover sacrifice. The Passover lamb (Exod 12) was killed at the appointed time, its blood placed on doorposts, its eating a communal participation in deliverance. Paul applies all three registers to Christ: appointed time (the cross at Passover), blood as protection, and communal participation (the Lord's Supper as new Passover meal). The command 'let us celebrate the festival' (v. 8) invites believers into ongoing Christological Passover-living: sincerity and truth as the unleavened bread that accompanies the feast.</p>"
  },
  "10": {
    "4": "<p>A type: 'They drank from the spiritual rock that followed them, and the rock was Christ.' Paul applies a midrashic tradition (the rock of Exod 17:6 and Num 20:11 that followed Israel in the wilderness — attested in various Second Temple sources) and identifies it typologically with Christ. The wilderness generation had Christological benefits before the incarnation: they ate the spiritual food (manna) and drank the spiritual drink (water from the rock) that pointed forward to and derived its sustaining power from Christ. Christ was the substance that every wilderness provision shadowed.</p>"
  },
  "11": {
    "26": "<p>A direct revelation: 'For as often as you eat this bread and drink this cup, you proclaim the Lord's death until he comes.' The Eucharist is not merely commemorative but kerygmatic — every celebration is a proclamation (<em>kataggellō</em>) of the Lord's death. This death-proclamation has an eschatological horizon: 'until he comes' (<em>achris hou elthe</em>). The Lord's Supper situates the community between the cross and the parousia, making every meal a re-entry into the narrative of Christ's saving death and an anticipation of its completion at the return. Christology is embedded in liturgical practice.</p>"
  },
  "15": {
    "20": "<p>A direct revelation: 'But in fact Christ has been raised from the dead, the firstfruits of those who have fallen asleep.' The resurrection of Christ is the pivotal fact on which Paul's entire argument turns — not a theological principle but a historical event (<em>Christos egegertai</em>: he has been raised, perfect tense, with present ongoing state). The firstfruits designation makes the resurrection of believers not an optional addendum but the structurally necessary completion of Christ's resurrection: God's harvest of humanity is underway, Christ being the guarantee of the rest. The resurrection hope is not escape from creation but transformation into a new, glorified mode of embodied existence.</p>",

    "45": "<p>A direct revelation: 'The last Adam became a life-giving spirit.' The Adam-Christ typology here reaches its Christological climax. Adam was the representative head who brought death by disobedience into the created order; Christ is the new representative head who brings life by obedience (and resurrection). The <em>eschatos Adam</em> (last Adam) terminology is unique to Paul: Christ is not merely another Adam in a sequence but the final, definitive human through whom the Adamic story reaches its appointed end. As the life-giving spirit (<em>pneuma zoopoioun</em>), the risen Christ is the source of the Spirit that will transform resurrection-bodies at the last day.</p>",

    "57": "<p>A direct revelation: 'Thanks be to God who gives us the victory through our Lord Jesus Christ.' The doxology concludes the resurrection argument: the victory over death, sin, and law (v. 56) is not achieved by believers but given (<em>didonti</em>) by God. The mode of giving is 'through our Lord Jesus Christ' — his resurrection is the mediating event through which God's victory becomes the believer's possession. The personal pronoun 'our' Lord Jesus Christ makes the cosmic Christological triumph intimately personal: this victory is given to those who belong to him.</p>"
  }
}

def main():
    existing = load_comm('mkt-christ', '1corinthians')
    merge_comm(existing, CHRIST)
    save_comm('mkt-christ', '1corinthians', existing)
    total = sum(len(v) for v in existing.values())
    print(f'1 Corinthians mkt-christ: {len(existing)} chapters, {total} verses.')

if __name__ == '__main__':
    main()
