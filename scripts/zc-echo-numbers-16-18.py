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
    print(f'wrote {p.relative_to(ROOT)}')

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

NEW_ECHOES = {
    # Ch16: Korah rebellion — grounding + fire judgment; additional entries beyond v1/v5
    "16": {
        "31": [
            # earth swallows Korah — divine judgment on usurped priesthood
            {"type": "echo", "target": "Rev 12:16", "note": "the earth opening its mouth to swallow the enemy — apocalyptic echo of Korah judgment"},
            {"type": "echo", "target": "Heb 10:27", "note": "fiery judgment consuming adversaries of God echoes the fire that consumed the 250 men"}
        ],
        "35": [
            {"type": "echo", "target": "Rev 8:5", "note": "fire from the altar thrown to earth — incense censers and divine fire as instruments of judgment echo Korah narrative"},
            {"type": "echo", "target": "Heb 12:29", "note": "our God is a consuming fire — Korah judgment illustrates the holiness that devours unlawful approach"}
        ],
        "40": [
            # bronze censers hammered into altar covering — perpetual memorial
            {"type": "echo", "target": "1 Cor 10:10", "note": "do not grumble as some did and were destroyed — Paul explicitly cites the Korah-era rebellion as a warning"}
        ]
    },
    # Ch17: Aaron's rod that budded — vindication of chosen priesthood
    "17": {
        "8": [
            # Aaron's dead rod sprouts, buds, blossoms, bears ripe almonds overnight
            {"type": "type", "target": "John 11:25", "note": "Aaron's dead rod bursting to life typifies resurrection; Christ as the resurrection and the life vindicates his priestly office through rising from the dead"},
            {"type": "type", "target": "Heb 9:4", "note": "Aaron's rod that budded was kept in the ark of the covenant — permanent testimony to resurrection-vindicated priesthood"},
            {"type": "echo", "target": "Acts 2:24", "note": "God raised him up, loosing the pangs of death — resurrection as divine vindication of the true high priest, as Aaron's rod proved his election"},
            {"type": "echo", "target": "Rom 1:4", "note": "declared to be the Son of God in power by his resurrection — Christ's resurrection vindicates his priesthood as Aaron's rod vindicated the Aaronic line"}
        ],
        "10": [
            # rod kept before the testimony as a sign against rebels
            {"type": "echo", "target": "Heb 9:4", "note": "the ark contained Aaron's rod that budded — kept as perpetual testimony to the chosen priesthood"},
            {"type": "echo", "target": "Luke 20:17", "note": "the stone the builders rejected became the cornerstone — Christ as the rejected-then-vindicated one, echoing Aaron's rod as sign against rebels"}
        ]
    },
    # Ch18: Duties and portions of priests and Levites
    "18": {
        "7": [
            # priesthood as a gift — outsider who draws near shall be put to death
            {"type": "echo", "target": "Heb 10:19", "note": "we have confidence to enter the holy places by the blood of Jesus — the new and living way replaces the death-penalty boundary of the old priesthood"},
            {"type": "type", "target": "1 Pet 2:9", "note": "a royal priesthood, a holy nation — the church receives what the Levites held exclusively, now opened through Christ the high priest"}
        ],
        "19": [
            # covenant of salt — perpetual priestly portions
            {"type": "echo", "target": "Mark 9:49", "note": "everyone will be salted with fire — salt covenant language echoes the priestly salt covenant of perpetual consecration"},
            {"type": "echo", "target": "2 Chr 13:5", "note": "a covenant of salt — royal Davidic covenant uses the same formula, linking priestly and kingly covenants"}
        ],
        "20": [
            # YHWH to Aaron: I am your portion and your inheritance
            {"type": "type", "target": "Ps 16:5", "note": "the LORD is my chosen portion and my cup — David applies the Levitical inheritance formula to himself, fulfilled in Christ who had no earthly inheritance but the Father"},
            {"type": "echo", "target": "Ps 73:26", "note": "God is the strength of my heart and my portion forever — the Levitical portion-in-God becomes a universal spiritual reality"},
            {"type": "echo", "target": "Lam 3:24", "note": "the LORD is my portion, says my soul — Jeremiah applies the priestly portion language to faith amid exile"},
            {"type": "type", "target": "Rev 21:3", "note": "God himself will be with them as their God — the ultimate fulfillment of YHWH as portion: the whole people inherits what Aaron alone possessed"}
        ],
        "21": [
            # tithes given to Levites as inheritance for their service
            {"type": "echo", "target": "Heb 7:5", "note": "those who are descended from Levi receive a tithe from the people — Hebrews 7 builds a Melchizedekian priesthood argument directly from this verse"},
            {"type": "echo", "target": "1 Cor 9:13", "note": "those who serve at the altar share in the altar's offerings — Paul grounds ministerial support in Levitical precedent"}
        ],
        "24": [
            # tithes are the Levites' inheritance instead of land
            {"type": "echo", "target": "Heb 7:9", "note": "Levi himself paid tithes through Abraham — the tithe inheritance of Levites is the foundation of the Melchizedek argument in Heb 7"}
        ]
    }
}

data = load_echo('numbers')
merge_echo(data, NEW_ECHOES)
save_echo('numbers', data)
