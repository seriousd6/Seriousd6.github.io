"""
echo | Numbers 19-21 | Red heifer, Meribah, Aaron's death, bronze serpent
Run: python3 scripts/zc-echo-numbers-19-21.py

Ch 19 already had 19:9 → Heb 9:13. This pass adds the richer red-heifer connections:
- outside-the-camp burning (Heb 13:11-13)
- blood+water (John 19:34)
- seven-fold blood sprinkling toward the sanctuary

Ch 20 (Meribah + Aaron's death) was completely missing:
- Strike the rock / speak to the rock (1 Cor 10:4; John 7:37-38)
- Moses/Aaron's failure to enter Canaan (Heb 3:19)
- Aaron dies; priesthood passes to Eleazar (Heb 7:23-24)

Ch 21 already had 21:4 → 1 Cor 10:6-10 and 21:8 → John 3:14-15 (bronze serpent).
Adding the well song (21:17-18) → John 4:14 / 1 Cor 10:4.
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
    "19": {
        # v.2 — red heifer without blemish, never yoked
        "2": [
            {
                "type": "typology",
                "target": "Heb 9:13-14",
                "note": "The red heifer without blemish on which no yoke has come is the quintessential type: Hebrews explicitly contrasts the 'ashes of a heifer sprinkling the defiled' with Christ's blood that purifies the conscience. Both involve the sacrifice of an unblemished animal outside the camp.",
            },
        ],
        # v.4 — blood sprinkled seven times toward the front of the tent
        "4": [
            {
                "type": "typology",
                "target": "Heb 10:22",
                "note": "The sevenfold blood sprinkling toward the sanctuary by Eleazar foreshadows the promised cleansing of 'hearts sprinkled clean from an evil conscience' — the inner transformation that the external rite could only symbolize.",
            },
        ],
        # v.6 — cedar wood, hyssop, scarlet yarn thrown into the fire
        "6": [
            {
                "type": "allusion",
                "target": "John 19:29",
                "note": "Cedar wood, hyssop, and scarlet yarn — the same cluster as the leper's cleansing rite (Lev 14:4) — are thrown into the heifer's fire. Hyssop appears again at the cross (John 19:29), tying the red heifer, the leper rite, and the crucifixion into a single web of purification imagery.",
            },
        ],
        # v.9 — ashes stored outside the camp as purification water (already has Heb 9:13)
        # skipped — already present
        # v.13 — defiles the tabernacle; cut off from Israel
        "13": [
            {
                "type": "fulfillment",
                "target": "Heb 9:14",
                "note": "The defilement that required the red heifer's ashes was contact with death — making the conscience 'dead' before a holy God. Hebrews declares Christ's blood cleanses 'the conscience from dead works to serve the living God,' the inner reality the ashes could only shadow.",
            },
        ],
        # v.17 — ashes + fresh running water poured into a vessel
        "17": [
            {
                "type": "typology",
                "target": "John 19:34",
                "note": "The purification water is prepared by adding fresh (living) water to the red heifer's ashes in a vessel. Blood and water combined as the purifying agent prefigures the blood and water that flowed from Christ's pierced side — the antitype of every OT blood-and-water cleansing rite.",
            },
        ],
    },
    "20": {
        # v.8 — speak to the rock; it will give water
        "8": [
            {
                "type": "fulfillment",
                "target": "John 7:37-38",
                "note": "God commands Moses to speak to the rock and it will give its water freely. Jesus stands up on the last day of the feast and cries out: 'If anyone thirsts, let him come to me and drink.' The command to speak to the rock finds its fulfillment in Christ, the true rock who responds to the cry of faith with rivers of living water.",
            },
        ],
        # v.11 — Moses struck the rock twice; water poured out
        "11": [
            {
                "type": "fulfillment",
                "target": "1 Cor 10:4",
                "note": "Moses struck the rock at Meribah and water poured out abundantly. Paul declares that the rock that gave Israel water in the wilderness 'was Christ' — the spiritual rock from which the new exodus community drinks. The rock struck at Meribah is the type; Christ struck at Calvary is the antitype.",
            },
        ],
        # v.12 — Moses and Aaron will not enter the land due to unbelief
        "12": [
            {
                "type": "typology",
                "target": "Heb 3:19",
                "note": "YHWH tells Moses and Aaron they will not bring the congregation into the promised land because of their failure of faith at the waters. The wilderness generation's exclusion due to unbelief (Heb 3:19) is embodied in Israel's human leaders — both prophet and priest fail to enter. The greater Moses (Heb 3:3-6) brings his people all the way in.",
            },
        ],
        # v.26 — Aaron's vestments removed and placed on Eleazar
        "26": [
            {
                "type": "typology",
                "target": "Heb 7:23-24",
                "note": "Aaron's high-priestly vestments are transferred to Eleazar before Aaron dies — a succession that marks the Levitical priesthood's dependence on continuous replacement. Hebrews draws this contrast directly: 'The former priests were many in number because they were prevented by death from continuing in office, but he holds his priesthood permanently.'",
            },
        ],
        # v.28 — Aaron dies on the mountaintop; Eleazar becomes high priest
        "28": [
            {
                "type": "fulfillment",
                "target": "Heb 7:24",
                "note": "Aaron's death on Mount Hor and the transfer of the high priesthood to Eleazar is the paradigm case Hebrews uses when it declares that Christ 'holds his priesthood permanently, because he continues forever.' Every high priestly death makes the type's limitation explicit — and calls for the priest who will never die.",
            },
        ],
        # v.29 — all Israel mourned Aaron 30 days
        "29": [
            {
                "type": "typology",
                "target": "Heb 4:14",
                "note": "Israel mourned the death of their high priest for thirty days. The mourning expresses both loss and the anxiety of an unmediated people. Hebrews' exhortation to 'hold fast' to Jesus the great High Priest who 'has passed through the heavens' answers the 30-day mourning of Num 20:29 with a High Priest who cannot be mourned because he cannot die.",
            },
        ],
    },
    "21": {
        # v.17 — the well song: 'Spring up, O well'
        "17": [
            {
                "type": "allusion",
                "target": "John 4:14",
                "note": "Israel sings to the well that sprang up at Beer: 'Spring up, O well!' Jesus promises the Samaritan woman water that becomes 'a spring of water welling up to eternal life' — the well-song of Num 21 finds its answer in the one who is himself the inexhaustible source.",
            },
        ],
        # v.18 — nobles dug the well with their staffs
        "18": [
            {
                "type": "typology",
                "target": "1 Cor 10:4",
                "note": "Rabbinic tradition identified this well with the rock of Horeb that followed Israel, a tradition Paul draws on when he writes 'the rock was Christ.' The water-giving well of Num 21 is one more expression of the same spiritual reality: Christ is the source from whom the wilderness community drank throughout their journey.",
            },
        ],
    },
}


def main():
    data = load_echo("numbers")
    merge_echo(data, NUMBERS_ECHOES)
    save_echo("numbers", data)


if __name__ == "__main__":
    main()
