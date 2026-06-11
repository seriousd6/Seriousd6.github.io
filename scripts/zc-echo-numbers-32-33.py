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
    # Ch32: Reuben and Gad settle Transjordan; vanguard agreement
    "32": {
        "6": [
            # Moses rebukes: will you settle here while your brothers go to war?
            {"type": "echo", "target": "1 Cor 9:24", "note": "run to obtain the prize — Moses challenges early settlement as abandoning the corporate calling; Paul challenges running to win, not stopping short"},
            {"type": "echo", "target": "Heb 12:1", "note": "run with endurance the race set before us — the Transjordanian tribes temptation to settle before the conquest echoes the call not to drop out mid-race"}
        ],
        "14": [
            # a brood of sinful men — intensifying the fathers' sin
            {"type": "echo", "target": "Matt 23:32", "note": "fill up the measure of your fathers — Jesus applies the same generational-sin logic to those who reject him as Moses applies it here"},
            {"type": "echo", "target": "1 Thess 2:16", "note": "filling up the measure of their sins — Pauline echo of the accumulating-sin pattern warned against here"}
        ],
        "23": [
            # your sin will find you out
            {"type": "echo", "target": "Gal 6:7", "note": "whatever one sows, that will he also reap — the proverbial certainty of Num 32:23 reappears as a Pauline agricultural metaphor"},
            {"type": "echo", "target": "1 Tim 5:24", "note": "sins of some people are conspicuous, going before them to judgment, but the sins of others appear later — direct echo of sin finding out its perpetrator"},
            {"type": "echo", "target": "Heb 4:13", "note": "no creature is hidden from his sight — everything is naked and exposed before him to whom we must give account; the divine omniscience behind sin finding you out"}
        ],
        "17": [
            # we will take up arms and go before the people of Israel
            {"type": "type", "target": "Eph 6:13", "note": "put on the whole armor of God — the Transjordanian tribes going as armed vanguard typifies the Christian who arms for battle on behalf of the community before receiving full inheritance"},
            {"type": "echo", "target": "Josh 1:14", "note": "all your mighty men shall cross over armed before your brothers — Joshua's covenant-enforcement of the Transjordanian vanguard promise fulfills what Moses secured here"}
        ]
    },
    # Ch33: Wilderness itinerary — 42 stages from Egypt to Moab
    "33": {
        "2": [
            # Moses wrote down their starting places stage by stage at the command of YHWH
            {"type": "echo", "target": "Rev 20:12", "note": "books were opened — the divine command to record the wilderness journey anticipates the eschatological record-keeping of all deeds before God"},
            {"type": "echo", "target": "Exod 17:14", "note": "write this as a memorial in a book — the pattern of divinely-commanded written records of Israel's journey through the wilderness"}
        ],
        "3": [
            # departed from Rameses on the day after the Passover
            {"type": "echo", "target": "1 Cor 5:7", "note": "Christ our Passover lamb has been sacrificed — the exodus from Rameses the morning after Passover is the prototype of liberation through sacrificial death"},
            {"type": "type", "target": "John 8:36", "note": "if the Son sets you free you will be free indeed — departure from Egypt as the archetype of liberation from bondage, fulfilled in Christ's redemption"}
        ],
        "38": [
            # Aaron the priest went up Mount Hor at the command of YHWH and died there
            {"type": "type", "target": "Heb 7:23", "note": "the former priests were many in number because they were prevented by death from continuing in office — Aaron's death at Hor exemplifies the mortal limitation that the eternal Melchizedekian priesthood of Christ transcends"},
            {"type": "echo", "target": "Heb 5:4", "note": "no one takes this honor for himself, but only when called by God, just as Aaron was — Aaron dies at the divinely appointed moment as he was divinely appointed to office"}
        ],
        "52": [
            # drive out the inhabitants; destroy their figured stones and molten images
            {"type": "echo", "target": "2 Cor 6:17", "note": "come out from among them and be separate — the command to expel idols from the land is the prototype of the Pauline call to holiness in the new covenant community"},
            {"type": "echo", "target": "Rev 21:27", "note": "nothing unclean will ever enter it — the purging of idolaters from the promised land anticipates the perfect purity of the new Jerusalem"}
        ],
        "55": [
            # if you do not drive them out, those who remain shall be thorns in your sides
            {"type": "echo", "target": "Judg 2:3", "note": "their gods shall be a snare to you — Judges 2 pronounces exactly the judgment Moses warned of here; the unfulfilled conquest became Israel's downfall throughout the period of Judges"},
            {"type": "echo", "target": "2 Cor 12:7", "note": "a thorn in the flesh was given me — Paul repurposes the thorns-in-the-side imagery for the affliction that disciplines pride; the OT curse-image becomes a spiritual refining instrument"},
            {"type": "echo", "target": "Heb 12:15", "note": "see to it that no root of bitterness springs up — the spiritual application of allowing corrupting elements to remain; echoes the pastoral urgency of the Mosaic warning"}
        ]
    }
}

data = load_echo('numbers')
merge_echo(data, NEW_ECHOES)
save_echo('numbers', data)
