"""
Echo Layer — Ezekiel chapters 47–48
Run: python3 scripts/zc-echo-ezekiel-47-48-fill.py

Ch 47 already has v.1 (river → Rev 22:1). This script adds further entries to ch 47
and fills in ch 48 entirely.

Major echo clusters:
- Ch 47: The growing river — 47:5 → John 7:37-39 (rivers of living water from Christ);
  47:9 → John 1:4; 4:14 (life from the water); 47:10 → Matt 4:19 / John 21:6-11 (fishers);
  47:12 → Rev 22:2 (tree of life with monthly fruit, leaves for healing);
  47:22-23 → Eph 2:12-13,19; Gal 3:28 (aliens = fellow citizens in Christ)
- Ch 48: Tribal allotment — 48:11 → Rev 3:4 (faithful few who have not soiled garments);
  48:29 → 1 Pet 1:4 (inheritance kept in heaven); 48:31 → Rev 21:12 (twelve gates
  inscribed with tribes); 48:35 → Rev 21:3,22 (YHWH-Shammah = the Lord Is There =
  the whole city is temple; God dwells with humanity)
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echoes(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_echoes(book, data):
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

EZK_ECHOES = {
  "47": {
    "5": [
      {"type": "allusion-source", "target": "John 7:37-39", "note": "The river growing from ankle-deep to knee-deep to waist-deep to uncrossable — the escalating depth is the pattern of the Spirit's outpouring. Jesus at the Feast of Tabernacles (which drew on temple water-pouring symbolism): whoever believes in me, rivers of living water will flow from within them. John explains: this he said about the Spirit, whom those who believed in him were to receive."},
      {"type": "allusion", "target": "John 4:14", "note": "The water that keeps increasing without external source — the water I give will become in the person a spring of water welling up to eternal life. Ezekiel's river that deepens of its own accord is the image Jesus uses for the Spirit's interior work."}
    ],
    "9": [
      {"type": "allusion-source", "target": "John 1:4", "note": "Everything lives where the river goes — every living creature that swarms will live wherever the river flows. In him was life, and that life was the light of all people. Ezekiel's life-giving river is the cosmological vitality that John attributes directly to the Logos made flesh."},
      {"type": "allusion", "target": "Rev 22:17", "note": "Wherever the river flows, life follows — the Spirit and the bride say, Come. Let the one who is thirsty come; let the one who desires take the water of life freely. The open invitation of Revelation's closing echoes Ezekiel's river: both offer unlimited life to all who come."}
    ],
    "10": [
      {"type": "allusion-source", "target": "Matt 4:19", "note": "Fishermen standing along the banks from En-gedi to En-eglaim, spreading their nets in abundance — Jesus calls fishermen from their work by the sea: Follow me, and I will make you fishers of men. The eschatological fishing scene of Ezekiel 47:10 is the context for his calling."},
      {"type": "allusion", "target": "John 21:6-11", "note": "The miraculous catch of 153 large fish in John 21 — when the risen Jesus instructs the disciples to cast the net on the right side — echoes Ezekiel's fishermen of the healed sea. The great haul represents the gathering of the nations that the living-water river of the Spirit makes possible."}
    ],
    "12": [
      {"type": "allusion-source", "target": "Rev 22:2", "note": "Trees on both banks of the river, leaves not withering, bearing fresh fruit every month, leaves for healing — Revelation 22:2 reproduces this image almost exactly: on each side of the river stood the tree of life, bearing twelve kinds of fruit, yielding its fruit every month; and the leaves of the tree were for the healing of the nations. Ezekiel's river-bank trees are the tree of life in the New Jerusalem."}
    ],
    "22": [
      {"type": "allusion-source", "target": "Eph 2:19", "note": "The resident alien and the sojourner who have children among you shall be allotted an inheritance with the native-born — Paul applies this exact principle to Gentile believers: you are no longer foreigners and strangers, but fellow citizens with God's people and also members of his household. The eschatological land-inclusion of Ezekiel 47:22 is the template for Gentile inclusion in the covenant community."},
      {"type": "allusion", "target": "Gal 3:28-29", "note": "There is neither Jew nor Gentile... you are all one in Christ Jesus. If you belong to Christ, you are Abraham's seed and heirs according to the promise. The inheritance-for-sojourners principle of Ezekiel 47:22 is radicalized in Christ: the same inheritance, the same promise, the same Lord, regardless of ethnic origin."}
    ]
  },
  "48": {
    "11": [
      {"type": "allusion", "target": "Rev 3:4", "note": "The Zadokite priests who kept the divine charge and did not go astray when Israel went astray — you have a few people in Sardis who have not soiled their garments. They will walk with me, dressed in white, for they are worthy. The faithful minority who remain undefiled when the broader community falls away appears in both Ezekiel's priestly geography and the letters to the seven churches."}
    ],
    "29": [
      {"type": "allusion-source", "target": "1 Pet 1:4", "note": "The land allotted as inheritance among the tribes — Peter invokes the inheritance language for the new covenant people: an inheritance that can never perish, spoil or fade — kept in heaven for you. The tribal inheritance of Ezekiel 48 is the earthly form of the imperishable inheritance that Christ secures through his resurrection."},
      {"type": "allusion", "target": "Heb 9:15", "note": "Christ is the mediator of a new covenant, so that those who are called may receive the promised eternal inheritance. The inheritance promised to the twelve tribes in Ezekiel 48 is the OT form of what the new covenant mediator secures for the whole people of God."}
    ],
    "31": [
      {"type": "allusion-source", "target": "Rev 21:12-13", "note": "The city's twelve gates named after the twelve tribes of Israel — three on each side — is reproduced exactly in the New Jerusalem of Revelation 21: the twelve gates inscribed with the names of the twelve tribes of Israel, three gates on the east, three on the north, three on the south, three on the west. John's heavenly city is explicitly built on Ezekiel's blueprint."}
    ],
    "35": [
      {"type": "fulfillment", "target": "Rev 21:3", "note": "YHWH Shammah — The LORD Is There: the final word of Ezekiel, the closing name given to the restored city, is the concentrated promise that the entire book has been moving toward. Revelation 21:3 is its direct fulfillment: the dwelling of God is with humanity; he will dwell with them, and they will be his people, and God himself will be with them and be their God. Ezekiel's exile and departure of the Shekinah (ch 10-11) ends here with the irrevocable promise of divine presence."},
      {"type": "allusion-source", "target": "Rev 21:22", "note": "The city named YHWH-Shammah has no temple building — because YHWH himself is there. Revelation makes this explicit: I did not see a temple in the city, because the Lord God Almighty and the Lamb are its temple. The entire city becomes the sanctuary; the presence that departed from the temple in Ezekiel 10 now fills the whole city forever."},
      {"type": "allusion", "target": "Rev 22:4", "note": "The name of the city is 'The LORD Is There' — the divine face-to-face presence promised by the city's name is completed in the final promise of Revelation: they will see his face, and his name will be on their foreheads. The presence of YHWH in the city becomes the presence of the Lamb and the Father directly seen by his servants."}
    ]
  }
}

def main():
    existing = load_echoes('ezekiel')
    merge_echo(existing, EZK_ECHOES)
    save_echoes('ezekiel', existing)

    out = json.loads((ROOT / 'data/echoes/ezekiel.json').read_text())
    for ch in [47, 48]:
        ck = str(ch)
        count = sum(len(v) for v in out.get(ck, {}).values())
        status = 'done' if out.get(ck) else 'MISSING'
        print(f'ch {ch}: {status} ({len(out.get(ck, {}))} verse-keys, {count} entries total)')

    covered = sorted([int(c) for c in out])
    print(f'Total Ezekiel echo chapters covered: {len(covered)}/48')

if __name__ == '__main__':
    main()
