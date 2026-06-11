"""
Echo Layer — Exodus chapters 39–40
Run: python3 scripts/zc-echo-exodus-39-40.py

Ch 39: Completion of all priestly garments exactly as commanded; Moses's inspection
       and blessing. Connects to the high priestly imagery of Hebrews and the New
       Jerusalem's gem-adorned foundations.
Ch 40: Erection of the tabernacle; anointing; the glory-cloud fills the tent of meeting,
       making it inaccessible to Moses. This is the OT's climax of divine presence —
       fulfilled and superseded in the Incarnation (John 1:14) and the new creation
       (Rev 21:3).
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

EXODUS_ECHOES = {
  "39": {
    "7": [
      {"type": "type", "target": "Rev 21:12", "note": "The onyx stones on the high priest's shoulders engraved with the names of the twelve tribes (Exod 28:9-12; 39:6-7) are the OT type for the twelve gates of the New Jerusalem each bearing a tribal name — the covenant people's identity permanently inscribed in the new creation's architecture"},
      {"type": "type", "target": "Rev 21:19-20", "note": "The twelve gemstones of the high priest's breastplate (one per tribe) are the type for the twelve foundation stones of the New Jerusalem adorned with twelve gems — the priestly breastplate's ordered beauty becomes the new city's permanent foundation"}
    ],
    "30": [
      {"type": "allusion", "target": "Zech 14:20", "note": "The inscription 'HOLINESS TO THE LORD' (qodesh la-YHWH) engraved on the high priest's golden plate is the eschatological vision of Zechariah 14:20-21: even the bells on horses and the cooking pots will be 'HOLINESS TO THE LORD' — the priestly inscription that once belonged to one person will mark all of creation"},
      {"type": "allusion", "target": "Rev 4:8", "note": "The golden plate declaring YHWH's holiness at the entrance to his presence (worn by the high priest on his forehead when entering) finds its eschatological counterpart in the four living creatures who cry 'Holy, holy, holy is the Lord God Almighty' before the divine throne — the priestly declaration of holiness becomes the ceaseless song of heaven"}
    ],
    "32": [
      {"type": "allusion", "target": "Heb 8:5", "note": "The tabernacle work completed 'just as the LORD had commanded Moses' (the phrase repeated throughout chs. 39-40) establishes the earthly tabernacle as an exact copy of the heavenly pattern shown to Moses — Hebrews argues the Mosaic tabernacle was 'a copy and shadow of what is in heaven,' which Christ now ministers in as high priest"},
      {"type": "allusion", "target": "John 17:4", "note": "Moses's inspection finding everything done 'just as the LORD commanded' (39:42-43) is the formal completion formula of the tabernacle project — Jesus's prayer 'I have brought you glory on earth by finishing the work you gave me to do' (John 17:4) uses the same completed-work structure, with Christ's obedient life and atoning death as the antitype to the obedient craftsmen's tabernacle work"}
    ],
    "43": [
      {"type": "type", "target": "Heb 3:3", "note": "Moses inspects the completed tabernacle work and blesses the craftsmen — his authority as the one who receives the pattern and oversees its execution is the type that Hebrews uses to frame Christ's superiority: Jesus has been counted worthy of more glory than Moses, as the builder of a house has more honor than the house itself"}
    ]
  },
  "40": {
    "9": [
      {"type": "type", "target": "Acts 10:38", "note": "The anointing of the tabernacle and all its furnishings with the sacred anointing oil (Exod 40:9-15) is the OT type for the Messianic anointing: 'God anointed Jesus of Nazareth with the Holy Spirit and power' — the Messiah (Hebrew mashiach = anointed one) is the person whom the tabernacle-anointing typified; the oil consecrating the earthly sanctuary pointed to the Spirit consecrating the living temple"}
    ],
    "15": [
      {"type": "type", "target": "Heb 7:24", "note": "The anointing of Aaron's sons establishes 'a lasting priesthood throughout their generations' (Exod 40:15), but this Aaronic priesthood passed from father to son because of death. Hebrews contrasts this with Christ's permanent priesthood: 'because Jesus lives forever, he has a permanent priesthood' — what the Aaronic succession sought to perpetuate through generational succession is achieved definitively in Christ's indestructible life"}
    ],
    "20": [
      {"type": "type", "target": "Heb 9:4", "note": "Moses places the testimony tablets in the ark and sets the mercy seat on top — establishing the Most Holy Place as the site of the stored covenant documents overlaid by the seat of atonement. Hebrews describes this ark as containing 'the golden jar of manna, Aaron's staff that had budded, and the stone tablets of the covenant' — the three objects representing provision, priesthood, and law that together pointed to Christ as the bread of life, the living high priest, and the fulfiller of Torah"}
    ],
    "34": [
      {"type": "fulfillment", "target": "John 1:14", "note": "The glory of the LORD filling the tabernacle (Exod 40:34-35) is the OT climax of divine presence — the moment YHWH takes up residence in his constructed dwelling. John 1:14 explicitly reads the Incarnation through this event: 'the Word became flesh and tabernacled (<em>eskēnōsen</em>) among us, and we have seen his glory' — the tabernacle-filling glory is now the glory of the Father's only Son, dwelling permanently in a human body rather than a tent of meeting"},
      {"type": "fulfillment", "target": "Rev 21:3", "note": "The glory filling the tent of meeting — YHWH dwelling with Israel in the wilderness — points forward to Revelation's ultimate fulfillment: 'God's dwelling (skēnē) is now among the people, and he will dwell (skēnōsei) with them' — the tabernacle-pattern of divine presence (Exod 25:8, 'make me a sanctuary so I may dwell among them') reaches its final permanent form in the new creation where God himself tabernacles with redeemed humanity forever"}
    ],
    "35": [
      {"type": "type", "target": "Heb 9:8", "note": "Moses cannot enter the tent of meeting because the divine glory has filled it (Exod 40:35) — the very presence that the tabernacle was built to contain makes it temporarily inaccessible to the high priest. Hebrews interprets this as the Holy Spirit signifying 'that the way into the Most Holy Place had not yet been disclosed as long as the first tabernacle was still functioning' — the barrier that even Moses faced is the same barrier Christ removes by his atoning blood (Heb 10:19-20)"}
    ],
    "38": [
      {"type": "type", "target": "1 Cor 10:1-2", "note": "The cloud of the LORD resting on the tabernacle by day and fire by night — visible to all Israel throughout their journeys — is the ongoing divine guidance that Paul calls the Israelites being 'under the cloud' and 'all baptized into Moses in the cloud and in the sea' (1 Cor 10:1-2). The pillar of cloud and fire that guided Israel is the type for Spirit-guidance of the new covenant community: the Spirit who dwells in the community of Christ is the antitype of the cloud-fire presence that led Israel through the wilderness"}
    ]
  }
}

def main():
    existing = load_echo('exodus')
    merge_echo(existing, EXODUS_ECHOES)
    save_echo('exodus', existing)
    print('Exodus 39-40 echo written.')

if __name__ == '__main__':
    main()
