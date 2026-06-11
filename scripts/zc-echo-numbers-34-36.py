"""
echo | Numbers 34-36 | Land boundaries, cities of refuge, Zelophehad inheritance
Run: python3 scripts/zc-echo-numbers-34-36.py

Ch 34: Boundaries of Canaan as Israel's inheritance.
  - Joshua (Yeshua) distributes the inheritance → Christ distributes the true inheritance
  - The land as type of heavenly inheritance (Heb 11:14-16; 1 Pet 1:4)

Ch 35: Six cities of refuge — the richest Christ-type in Numbers.
  - Flee to the city from the blood avenger → Heb 6:18 (fled for refuge to hold on to hope)
  - Open to aliens and foreigners → Eph 2:12-13 (strangers brought near)
  - Manslayer must stay until the HIGH PRIEST DIES; then he goes free → the most precise
    type: Christ's death as High Priest is what releases the guilty from liability
  - Land atonement by blood only (35:33) → Heb 9:22

Ch 36: Zelophehad's daughters must marry within their tribe to keep the inheritance.
  - Daughters inherit land → Gal 3:28-29 (heirs in Christ regardless of gender)
  - Inheritance must not transfer between tribes → integrity of the covenant people
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
    "34": {
        # v.2 — the land as inheritance
        "2": [
            {
                "type": "typology",
                "target": "1 Pet 1:4",
                "note": "The land of Canaan is assigned to Israel as their inheritance (naḥalah). Peter applies this inheritance language to the eschatological hope: 'an inheritance that is imperishable, undefiled, and unfading, kept in heaven for you' — the earthly Canaan being the type of the heavenly country.",
            },
            {
                "type": "typology",
                "target": "Heb 11:14-16",
                "note": "The patriarchs and Israel looked toward a land inheritance that the OT itself acknowledged was only a down payment. Hebrews says they were 'seeking a homeland... a better country, that is, a heavenly one.' The Canaan boundary map of Num 34 is the earthly silhouette of an eternal reality.",
            },
        ],
        # v.17 — Joshua and Eleazar divide the land
        "17": [
            {
                "type": "typology",
                "target": "John 14:2-3",
                "note": "Joshua (Yeshua = Jesus) is commissioned alongside Eleazar the priest to distribute the land as inheritance to each tribe. Christ, the one whose very name is Joshua, promises to prepare a place and bring his people into their inheritance — the true Joshua distributing the true land.",
            },
        ],
        # v.29 — men commissioned to divide the inheritance
        "29": [
            {
                "type": "fulfillment",
                "target": "Eph 1:11",
                "note": "The commissioning of tribal leaders to allocate the inheritance foreshadows the divine administration of the heavenly inheritance: 'In him we have obtained an inheritance, having been predestined according to the purpose of him who works all things according to the counsel of his will.'",
            },
        ],
    },
    "35": {
        # v.6 — six cities of refuge established
        "6": [
            {
                "type": "typology",
                "target": "Heb 6:18",
                "note": "The six cities of refuge where any accidental killer could flee and be protected from the blood avenger are the most explicit OT type of Christ as refuge. Hebrews cites this institution directly: 'we who have fled for refuge to lay hold of the hope set before us' — the city is Christ himself.",
            },
        ],
        # v.11 — designate cities where accidental killer may flee
        "11": [
            {
                "type": "typology",
                "target": "Rom 8:1",
                "note": "Inside the city of refuge, the blood avenger has no jurisdiction. 'There is therefore now no condemnation for those who are in Christ Jesus' (Rom 8:1) — the city's protection from the avenger is the type; being 'in Christ' is the antitype. The spatial metaphor ('in the city') maps directly onto the Pauline 'in Christ.'",
            },
        ],
        # v.12 — protection from the blood avenger until judged
        "12": [
            {
                "type": "typology",
                "target": "John 5:24",
                "note": "The manslayer in the city of refuge is protected while the case is judged. Jesus promises those who believe: 'he does not come into judgment, but has passed from death to life' — the final verdict is already rendered for those who are in him, not pending.",
            },
        ],
        # v.15 — open to Israelites, resident aliens, and foreigners
        "15": [
            {
                "type": "fulfillment",
                "target": "Eph 2:12-13",
                "note": "The cities of refuge are open not only to Israelites but to resident aliens and foreigners — anyone who kills unintentionally may flee there. Paul writes that those formerly 'strangers to the covenants of promise, having no hope and without God' are 'now brought near by the blood of Christ.' The city's universal welcome anticipates the gospel's universal offer.",
            },
        ],
        # v.25 — manslayer remains in city until the high priest dies
        "25": [
            {
                "type": "typology",
                "target": "Heb 7:27",
                "note": "The manslayer's fate is tied to the high priest's life: he must remain in the city until the high priest dies. This creates the most precise typological structure in Numbers: freedom from liability comes through the high priest's death. Christ 'offered up himself' once — the High Priest's death is itself the act that releases the guilty from the avenger's jurisdiction.",
            },
        ],
        # v.28 — after the high priest dies, the manslayer goes free and returns home
        "28": [
            {
                "type": "fulfillment",
                "target": "Gal 5:1",
                "note": "The law that the manslayer goes free at the high priest's death, able to return to his own land without liability, finds its fulfillment in Christ's high-priestly death. 'For freedom Christ has set us free; stand firm therefore, and do not submit again to a yoke of slavery.' The death of the High Priest is the moment of permanent release.",
            },
        ],
        # v.30 — two witnesses required for conviction
        "30": [
            {
                "type": "allusion",
                "target": "John 8:17",
                "note": "The legal requirement of two witnesses to sustain a death penalty (Num 35:30; Deut 17:6) is cited by Jesus in the debate about his testimony: 'In your Law it is written that the testimony of two people is true' — he claims that his witness and the Father's constitute the required two.",
            },
        ],
        # v.33 — atonement for the land requires blood
        "33": [
            {
                "type": "fulfillment",
                "target": "Heb 9:22",
                "note": "Num 35:33 states the axiom: 'there is no atonement for the land except through the blood of the one who shed it.' Hebrews applies this principle universally: 'without the shedding of blood there is no forgiveness of sins.' The land-defilement atonement law is the ground-level form of the gospel's central claim.",
            },
        ],
        # v.34 — YHWH dwells among the Israelites; the land must be kept clean
        "34": [
            {
                "type": "fulfillment",
                "target": "1 Cor 3:16-17",
                "note": "The land must not be defiled because YHWH himself dwells in it among Israel. The threat to the dwelling-place of God is the gravest possible desecration. Paul translates this to the new covenant community: 'you are God's temple and God's Spirit dwells in you... God's temple is holy, and you are that temple.'",
            },
        ],
    },
    "36": {
        # v.2 — daughters can inherit (connection to Num 27)
        "2": [
            {
                "type": "typology",
                "target": "Gal 3:28-29",
                "note": "The daughters of Zelophehad's right to inherit land (established in Num 27, confirmed here in 36) is an anticipation of the principle Paul announces in Christ: 'there is neither male nor female, for you are all one in Christ Jesus... heirs according to promise.' The daughters' inheritance prefigures the full inclusion of all heirs regardless of gender.",
            },
        ],
        # v.7 — tribal inheritance must not transfer between tribes
        "7": [
            {
                "type": "allusion",
                "target": "Eph 1:14",
                "note": "The insistence that each tribe preserve its own inheritance intact anticipates the sealing of the Spirit as 'the guarantee of our inheritance until we acquire possession of it.' The covenant inheritance is guarded, not lost — what God has given in Christ cannot pass away or be transferred to another.",
            },
        ],
        # v.13 — Numbers colophon: commandments given through Moses on the plains of Moab
        "13": [
            {
                "type": "typology",
                "target": "John 1:17",
                "note": "The Numbers colophon (parallel to Lev 27:34 and Deut 34:12) marks the close of the book's legal code: commandments given through Moses at the Jordan threshold. John's prologue places this Mosaic legislation within a larger frame: 'the law was given through Moses; grace and truth came through Jesus Christ.' The book of Numbers ends at Moab; the true Joshua will take Israel in.",
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
