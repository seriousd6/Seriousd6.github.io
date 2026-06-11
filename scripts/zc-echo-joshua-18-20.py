import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_comm(source, book):
    p = ROOT / 'data' / 'commentary' / source / f'{book}.json'
    if p.exists(): return json.loads(p.read_text())
    return {}

def save_comm(source, book, data):
    p = ROOT / 'data' / 'commentary' / source / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_echo(existing, new_data):
    # INTENT: Add echo entries for chapters/verses not yet present; never overwrite existing work.
    # CHANGE? If echo schema changes (type/target/note keys), update all zc-echo-*.py scripts.
    # VERIFY: After run, data/commentary/echo/joshua.json should have ch18/19/20 keys with correct verse entries.
    for ch, verses in new_data.items():
        if ch not in existing: existing[ch] = {}
        for v, entries in verses.items():
            if v not in existing[ch]: existing[ch][v] = entries

# Selective NT echoes for Joshua 18-20.
# Josh 18: tabernacle at Shiloh, Benjamin's allotment.
# Josh 19: remaining six tribal allotments, Joshua's personal inheritance.
# Josh 20: cities of refuge — the richest echo chapter.

BOOK_ECHOES = {
    "18": {
        # Congregation assembles at Shiloh; the tent of meeting is pitched there.
        # Acts 7:45 names this moment directly in Stephen's speech on Israel's history.
        "1": [
            {
                "type": "echo",
                "target": "Acts 7:45",
                "note": "Stephen's speech traces the tabernacle to Shiloh: 'our fathers brought it in with Joshua' — the same assembly this verse records."
            }
        ],
        # Lots cast before Yahweh at Shiloh to divide the land.
        # The apostles cast lots before the Lord to replace Judas — same theology of divine decision through lot.
        "10": [
            {
                "type": "echo",
                "target": "Acts 1:26",
                "note": "Casting lots 'before Yahweh' at Shiloh to assign each tribe its portion echoes the apostles casting lots to discern God's will in choosing Matthias."
            }
        ]
    },
    "19": {
        # Simeon's allotment falls within Judah's — a form of inheritance through another tribe.
        # Paul's point in Galatians that Gentiles share the inheritance 'in' the seed of Abraham follows the same logic.
        "9": [
            {
                "type": "echo",
                "target": "Gal 3:29",
                "note": "Simeon inherits within Judah's portion — belonging to the people of God through another tribe's inheritance — an early pattern of the Gentiles sharing Abraham's inheritance in Christ."
            }
        ],
        # Joshua receives Timnath-serah as his personal inheritance — last of all, after the entire people are settled.
        # Heb 4:8 names Joshua explicitly: he did not give the people true rest; the greater Joshua (Jesus) does.
        "49": [
            {
                "type": "echo",
                "target": "Heb 4:8",
                "note": "Joshua receives his own allotment last, after all Israel is settled. Hebrews 4:8 names Joshua directly: if he had given true rest, God would not speak of 'another day' — pointing to Christ as the one who gives lasting Sabbath-rest."
            }
        ],
        # The distribution concludes at Shiloh before Yahweh — the dividing work finished.
        "51": [
            {
                "type": "echo",
                "target": "Eph 1:11",
                "note": "The land allotted by lot before Yahweh at Shiloh foreshadows the elect 'obtaining an inheritance, having been predestined according to the purpose of him who works all things' (Eph 1:11)."
            }
        ]
    },
    "20": {
        # God commands the cities of refuge — echoing the Mosaic institution (Num 35, Deut 19).
        # Heb 6:18 draws on this imagery directly: fleeing for refuge to lay hold of hope.
        "2": [
            {
                "type": "echo",
                "target": "Heb 6:18",
                "note": "The divine command to appoint cities of refuge shapes Hebrews 6:18's metaphor: 'we who have fled for refuge might have strong encouragement to hold fast to the hope set before us' — Christ himself is the refuge city."
            }
        ],
        # The manslayer flees to the city gate, states his case, and is granted shelter.
        # This pictures the one who comes to Christ — no condemnation for those in him (Rom 8:1).
        "4": [
            {
                "type": "echo",
                "target": "Rom 8:1",
                "note": "The accused who reaches the city gate and is received finds no condemnation — an image of 'no condemnation for those who are in Christ Jesus' (Rom 8:1), the true refuge."
            }
        ],
        # The manslayer must remain in the refuge city until the death of the high priest.
        # The death of Israel's high priest releases the fugitive; Christ's death as high priest releases all humanity from the guilt of sin.
        "6": [
            {
                "type": "echo",
                "target": "Heb 9:15",
                "note": "The fugitive's release upon the high priest's death typifies Christ's death: 'he is the mediator of a new covenant, so that those who are called may receive the promised eternal inheritance' (Heb 9:15) — his death as high priest sets the condemned free."
            }
        ],
        # Six cities appointed — three west, three east.
        # The completeness (six = work finished) and accessibility (spread throughout the land) picture the universal reach of Christ's atonement.
        "9": [
            {
                "type": "echo",
                "target": "1 John 2:2",
                "note": "Six cities spread throughout the land so that any manslayer could reach one quickly pictures the universal scope of Christ's propitiation: 'not for our sins only but also for the sins of the whole world' (1 John 2:2)."
            }
        ]
    }
}

def main():
    existing = load_comm('echo', 'joshua')
    merge_echo(existing, BOOK_ECHOES)
    save_comm('echo', 'joshua', existing)
    # Report coverage
    il_path = ROOT / 'data' / 'interlinear' / 'joshua.json'
    il = json.loads(il_path.read_text())
    for ch in ['18', '19', '20']:
        il_count = len(il.get(ch, {}))
        echo_count = len(existing.get(ch, {}))
        print(f'  ch{ch}: {echo_count} echo entries / {il_count} IL verses')

if __name__ == '__main__':
    main()
