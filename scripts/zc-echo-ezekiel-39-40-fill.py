"""
Echo Commentary — Ezekiel 39–40
Run: python3 scripts/zc-echo-ezekiel-39-40-fill.py

Key echo nodes:
- 39:4  birds feast on the fallen → Rev 19:17-21 (great supper of God)
- 39:6  fire on Magog / coastlands → Rev 20:8-9 (Gog and Magog; fire from heaven)
- 39:8  "this is the day of which I have spoken" → Rev 16:17; John 19:30
- 39:17-20 bird-feast at the sacrifice → Rev 19:17-21
- 39:21 YHWH's glory displayed among nations → John 17:22; Rev 21:23
- 39:29 Spirit poured out; face no longer hidden → Acts 2:17-18; John 14:16
- 40:2  high mountain, city-like structure → Rev 21:10 (the new Jerusalem vision)
- 40:3  bronze-gleaming man with measuring reed → Rev 1:15; Rev 11:1
- 40:38-43 offering tables in the temple → Heb 10:1-10 (Christ's one sufficient sacrifice)
- 40:46 sons of Zadok as priests → Rev 5:10; 1 Pet 2:9 (royal priesthood)
- 40:47 inner court perfect square → Rev 21:16 (perfect cube/square of new Jerusalem)
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
    """Merge echo entries; deduplicate by (type, target) within each verse."""
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

EZEKIEL_ECHOES = {
"39": {
    "4": [
        {"type": "fulfillment", "target": "Rev 19:17", "note": "YHWH gives Gog's army to birds of every kind as food — the fallen host consumed by scavengers. Revelation 19:17-18 enacts this exactly: an angel standing in the sun calls every bird to the great supper of God to eat the flesh of kings, generals, and the mighty. John's apocalyptic bird-feast is the deliberate fulfillment of Ezekiel's Gog-oracle."}
    ],
    "6": [
        {"type": "fulfillment", "target": "Rev 20:9", "note": "Fire sent on Magog and the coastlands matches Revelation 20:8-9 precisely: 'Gog and Magog' are gathered for battle, surround the camp of God's people, and 'fire came down from heaven and devoured them.' Revelation's Gog-and-Magog episode explicitly replays the Ezekiel 38-39 oracle as the final eschatological battle."}
    ],
    "8": [
        {"type": "allusion", "target": "Rev 16:17", "note": "'It has come and it has happened... this is the day of which I have spoken' — the divine declaration of completed judgment. Revelation 16:17 uses identical closure language: 'It is done!' (Γέγονεν) when the seventh bowl is poured out. Both texts mark the eschatological completion of long-announced divine action with the same sense of irreversible accomplishment."},
        {"type": "allusion", "target": "John 19:30", "note": "The declaration 'it has happened' as the day arrives echoes Christ's τετέλεσται — 'it is finished' — at the cross. The completed divine action Ezekiel announces finds its deepest single fulfillment in the cross, which is both the definitive day of judgment absorbed and the basis for the ultimate 'it is done' of Rev 16:17."}
    ],
    "17": [
        {"type": "type", "target": "Rev 19:17", "note": "The divine command to every kind of bird and wild animal to assemble for the sacrificial feast — to eat flesh of the mighty and drink blood of princes — is the OT type fulfilled in Revelation 19:17-21's great supper of God. Ezekiel's oracle forms the source text that Revelation's angel-in-the-sun scene deliberately reenacts at history's climax."}
    ],
    "21": [
        {"type": "allusion", "target": "John 17:22", "note": "YHWH declares 'I will display my glory among the nations.' Jesus prays 'the glory you gave me I have given them, so that they may be one as we are one' (John 17:22). The divine glory displayed among nations in Ezekiel's eschatological vision is given to and reflected through the believing community in Christ's high-priestly prayer."},
        {"type": "fulfillment", "target": "Rev 21:23", "note": "The new Jerusalem needs no sun or moon 'for the glory of God gives it light, and the Lamb is its lamp' — the nations walk by that light (Rev 21:23-24). Ezekiel's promise that YHWH will display his glory among the nations reaches its ultimate fulfillment in the Lamb-illuminated city."}
    ],
    "29": [
        {"type": "fulfillment", "target": "Acts 2:17", "note": "YHWH's promise 'I have poured out my Spirit on the house of Israel' is fulfilled at Pentecost: Peter quotes Joel 2:28-29 in Acts 2:17-18 — 'in the last days, God says, I will pour out my Spirit on all people.' Ezekiel 39:29 is the Ezekielian parallel to Joel's promise, both fulfilled in the same eschatological Spirit-outpouring that inaugurates the new covenant era."},
        {"type": "fulfillment", "target": "John 14:16", "note": "YHWH's face no longer hidden; his Spirit poured out permanently. Jesus promises 'I will ask the Father, and he will give you another Advocate to help you and be with you forever — the Spirit of truth.' The permanent divine presence (no more hidden face) that Ezekiel 39:29 promises is secured through Christ's intercession and the Spirit's indwelling."}
    ]
},
"40": {
    "2": [
        {"type": "type",    "target": "Rev 21:10", "note": "Ezekiel is transported in divine visions to a very high mountain where he sees 'something like a city.' Revelation 21:10 uses the identical vision-transport formula: 'he carried me away in the Spirit to a mountain great and high, and showed me the Holy City, Jerusalem, coming down out of heaven.' The high-mountain vision of the restored temple-city in Ezekiel is the direct type of John's new Jerusalem vision."},
        {"type": "allusion", "target": "John 2:21", "note": "Ezekiel's temple vision — forty-eight chapters describing the city and sanctuary — is interpreted by Jesus as pointing to his own body: 'the temple he had spoken of was his body' (John 2:21). The entire Ezekielian temple-vision finds its fulfillment not in a rebuilt structure but in the risen Christ as the true locus of divine presence."}
    ],
    "3": [
        {"type": "allusion", "target": "Rev 1:15", "note": "The man with appearance like gleaming bronze holding a measuring cord anticipates the risen Christ in Revelation 1:15 — 'his feet were like bronze glowing in a furnace.' The bronze-gleaming divine figure who measures the temple is absorbed into the appearance of the glorified Christ."},
        {"type": "type",    "target": "Rev 11:1",  "note": "Ezekiel's man with a measuring reed is the OT type of the angel who gives John a reed like a measuring rod in Revelation 11:1: 'go and measure the temple of God and the altar.' The measuring-of-sacred-space action in Ezekiel 40-43 is replayed in Revelation's temple-measuring vision, both asserting divine ownership and protection of the sanctuary."}
    ],
    "4": [
        {"type": "allusion", "target": "Rev 1:3", "note": "The measuring man commands Ezekiel: 'Look with your eyes, hear with your ears, and fix your attention on everything I am going to show you.' Revelation's opening beatitude — 'blessed is the one who reads aloud the words of this prophecy and those who hear it' (Rev 1:3) — uses the same see/hear imperatives. Both Ezekiel's temple vision and Revelation are framed as urgent testimony that demands full attention."}
    ],
    "38": [
        {"type": "shadow", "target": "Heb 10:4", "note": "The tables for washing burnt offerings, sin offerings, and guilt offerings (40:38-43) represent the elaborate sacrificial infrastructure of Ezekiel's temple vision — the endless repetition of offerings for sin. Hebrews 10:1-4 declares that these 'repeated year after year... can never... make perfect those who draw near to worship; if it could, would they not have stopped being offered?' The whole sacrificial apparatus of Ezekiel's vision is the shadow; Christ's one offering is the substance (Heb 10:12-14)."}
    ],
    "46": [
        {"type": "type",    "target": "1 Pet 2:9", "note": "The sons of Zadok who have charge of the altar and the temple (40:46) represent the faithful priestly line set apart for YHWH's service. Peter applies the priestly category to all believers: 'you are a chosen people, a royal priesthood, a holy nation.' Ezekiel's restricted hereditary priesthood is the type; Christ expands access so that all who are in him constitute the holy priestly order."},
        {"type": "allusion", "target": "Rev 5:10",  "note": "Revelation 5:10 declares of those redeemed by the Lamb: 'you have made them to be a kingdom and priests to serve our God, and they will reign on the earth.' The sons-of-Zadok priestly service of Ezekiel's vision is universalized through the Lamb's blood — the priesthood becomes the possession of the whole redeemed community."}
    ],
    "47": [
        {"type": "allusion", "target": "Rev 21:16", "note": "The inner court measured as a perfect square — a hundred by a hundred cubits — anticipates the perfect geometry of the new Jerusalem: Revelation 21:16 — 'the city was laid out like a square, as long as it was wide.' The perfect-square temple precinct of Ezekiel 40:47 is expanded to the entire city in Revelation's vision, where the whole redeemed community inhabits the holy-of-holies dimensions."}
    ]
}
}

def main():
    existing = load_echo('ezekiel')
    merge_echo(existing, EZEKIEL_ECHOES)
    save_echo('ezekiel', existing)
    print('Ezekiel 39-40 echoes written.')

if __name__ == '__main__':
    main()
