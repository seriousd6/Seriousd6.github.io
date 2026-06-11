"""
echo | Numbers 7 | Dedication offerings of the twelve tribal leaders
Run: python3 scripts/zc-echo-numbers-7-7.py

Num 7 is 89 verses: the twelve tribal leaders bring identical offerings on twelve
successive days to dedicate the newly erected tabernacle altar. The chapter ends
with Moses hearing YHWH's voice from above the kapporet (7:89) — the mercy seat
that Paul identifies as Christ the hilasterion (Rom 3:25).

Echo targets:
- v.1: tabernacle completion → true tabernacle (Heb 8:2; John 1:14)
- v.2: twelve leaders → twelve apostles / New Jerusalem gates (Rev 21:12)
- v.10-11: dedication of the altar → Heb 13:10
- v.12: Nahshon of Judah leads (he is in Christ's genealogy, Matt 1:4)
- v.14: gold incense pan → golden bowls of prayer (Rev 8:3-4)
- v.15: burnt offering → Christ's self-offering (Heb 9:14)
- v.16: sin offering (male goat) → Christ bears sins (Heb 9:28; 2 Cor 5:21)
- v.17: peace offering → Christ our peace (Eph 2:14)
- v.86: twelve gold incense pans → Rev 5:8 (incense = prayers of saints)
- v.87: twelve sin-offering goats → one offering vs. many (Heb 10:11-12)
- v.89: voice from above the kapporet → Christ the Word (John 1:1) / hilasterion (Rom 3:25)
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent


def load_echo(book):
    p = ROOT / "data" / "echoes" / f"{book}.json"
    if p.exists():
        return json.loads(p.read_text())
    return {}


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


NUMBERS_ECHOES = {
    "7": {
        # v.1 — day Moses finished setting up the tabernacle
        "1": [
            {
                "type": "fulfillment",
                "target": "John 1:14",
                "note": "The tabernacle completion is the OT climax of God dwelling with his people; John declares the Word 'tabernacled among us' (eskēnōsen) — the true and final fulfillment of what Num 7:1 inaugurates.",
            },
            {
                "type": "typology",
                "target": "Heb 8:2",
                "note": "The earthly tabernacle whose completion is celebrated in Num 7 is 'a copy and shadow' of the true tabernacle in heaven, which the Lord pitched, not humans.",
            },
        ],
        # v.2 — twelve leaders of the tribes
        "2": [
            {
                "type": "typology",
                "target": "Rev 21:12",
                "note": "The twelve tribal leaders who dedicate the altar foreshadow the twelve gates of the New Jerusalem, each bearing the name of a tribe — the full covenant people brought to completion.",
            },
            {
                "type": "typology",
                "target": "Matt 19:28",
                "note": "Jesus promises the twelve apostles they will sit on twelve thrones judging the twelve tribes, recapitulating the twelve-leader structure of Israel's tabernacle dedication.",
            },
        ],
        # v.10 — dedication offerings for the altar
        "10": [
            {
                "type": "typology",
                "target": "Heb 13:10",
                "note": "The tabernacle altar dedicated in Num 7 is the type; Hebrews announces 'we have an altar from which those who serve the tent have no right to eat' — the cross as the definitive altar of dedication.",
            },
        ],
        # v.12 — Nahshon son of Amminadab, tribe of Judah leads
        "12": [
            {
                "type": "typology",
                "target": "Matt 1:4",
                "note": "Nahshon son of Amminadab, who leads all the tribal offerings, is in the direct Davidic-messianic line (Matt 1:4; Luke 3:32-33). The tribe of Judah — through whom Christ comes — leads the dedication of the tabernacle.",
            },
        ],
        # v.13 — silver dish and basin filled with flour for grain offering
        "13": [
            {
                "type": "allusion",
                "target": "John 6:35",
                "note": "The grain offering of fine flour mixed with oil that fills the silver vessels prefigures Christ who declares himself 'the bread of life' — the true grain offering that satisfies permanently.",
            },
        ],
        # v.14 — gold pan of incense
        "14": [
            {
                "type": "typology",
                "target": "Rev 8:3-4",
                "note": "Each gold incense pan offered by the tribal leaders is a type of the golden censers and bowls of incense before God's throne in Rev 8:3-4, which are explicitly identified as 'the prayers of the saints.'",
            },
        ],
        # v.15 — burnt offering
        "15": [
            {
                "type": "typology",
                "target": "Heb 9:14",
                "note": "The burnt offering of bull, ram, and yearling lamb — the totality of the animal given — types Christ who 'through the eternal Spirit offered himself without blemish to God,' the perfect olah that consecrates the people.",
            },
        ],
        # v.16 — male goat for sin offering
        "16": [
            {
                "type": "typology",
                "target": "Heb 9:28",
                "note": "The male goat sin offering at the altar's dedication types Christ who 'was offered once to bear the sins of many' — the definitive sin offering that the repeated goat-sacrifices could only foreshadow.",
            },
            {
                "type": "fulfillment",
                "target": "2 Cor 5:21",
                "note": "God made Christ 'to be sin who knew no sin' — the sin offering becomes a person. What was enacted twelve times by twelve goats is done once and for all in the one who bore sin in his own body.",
            },
        ],
        # v.17 — peace offering
        "17": [
            {
                "type": "fulfillment",
                "target": "Eph 2:14",
                "note": "The fellowship/peace offering (shelamim) that completes each tribal dedication is fulfilled in Christ, 'who is our peace,' the one who made the two one and broke down the dividing wall.",
            },
        ],
        # v.86 — twelve gold pans full of incense
        "86": [
            {
                "type": "typology",
                "target": "Rev 5:8",
                "note": "The twelve gold pans full of incense (one per tribe, totalling 120 shekels) prefigure the golden bowls full of incense that the elders hold before the Lamb in Rev 5:8 — explicitly 'the prayers of the saints.'",
            },
        ],
        # v.87 — twelve sin-offering goats
        "87": [
            {
                "type": "typology",
                "target": "Heb 10:11-12",
                "note": "Twelve sin offerings on twelve days — the multiplication of repeated sacrifices that 'can never take away sins.' Christ offered 'a single sacrifice for sins for all time' in contrast to priests who stand daily repeating the same offerings.",
            },
        ],
        # v.89 — voice from above the kapporet
        "89": [
            {
                "type": "typology",
                "target": "John 1:1",
                "note": "YHWH's voice speaks to Moses from above the kapporet (mercy seat) between the cherubim — the place of atonement is also the place of divine speech. Christ is both the Word who was with God (John 1:1) and the mercy seat (hilasterion, Rom 3:25); the voice from above the kapporet is the voice of the one who is the kapporet.",
            },
            {
                "type": "fulfillment",
                "target": "Rom 3:25",
                "note": "The kapporet — the ark cover from which YHWH spoke — is the same word Paul uses (via the LXX hilastērion) when he says God set forth Christ 'as a propitiation/mercy seat by his blood' (Rom 3:25). The voice Moses hears is the voice of the one who will become the mercy seat.",
            },
        ],
    }
}


def main():
    data = load_echo("numbers")
    merge_echo(data, NUMBERS_ECHOES)
    save_echo("numbers", data)


if __name__ == "__main__":
    main()
