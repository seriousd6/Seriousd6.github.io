"""
Echo layer — 2 Corinthians all 13 chapters
Output: data/echoes/2corinthians.json

2 Corinthians is the most personally revealing of Paul's letters.
Key echo zones: the new exodus theology of ch3 (Exod 34; Jer 31),
the 'servant of the Lord' suffering pattern (Isa 53),
the new creation (Isa 65:17-25), and the triumphal procession (Isa 52:7-10).
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

ECHOES = {
  "1": {
    "20": [
      {"type": "fulfillment", "target": "Num 23:19", "note": "All God's promises find their Yes in Christ — God is not a man that he should lie; every promise made through the patriarchs and prophets is ratified in the 'Yes' of Christ's faithfulness, fulfilling what the prophets spoke and the Torah promised"}
    ]
  },
  "3": {
    "3": [
      {"type": "fulfillment", "target": "Jer 31:33", "note": "Written not with ink but with the Spirit of the living God, not on tablets of stone but on tablets of human hearts — Paul's new covenant ministry description fulfills Jeremiah's new covenant promise precisely: the law written on hearts rather than stone; the Spirit as the writing-agent replacing Moses's tablets"}
    ],
    "6": [
      {"type": "fulfillment", "target": "Jer 31:31-34", "note": "God has made us ministers of a new covenant (<em>kaines diathekes</em>) — the new covenant that Jeremiah promised, distinguished from the Mosaic covenant by its internality (heart-law), universality, and permanent forgiveness"},
      {"type": "allusion", "target": "Ezek 11:19", "note": "A new spirit I will put within them; I will remove the heart of stone and give them a heart of flesh — Ezekiel's new covenant promise of the Spirit transforming stony hearts into living hearts; Paul's 'tablets of human hearts' echoes Ezek 11:19/36:26"}
    ],
    "13": [
      {"type": "allusion", "target": "Exod 34:33-35", "note": "Moses put a veil over his face — Paul's midrash on the Sinai theophany: the veil Moses wore was to prevent Israel from seeing the fading of the Mosaic covenant's glory; the veil remains on Israel's mind when reading the old covenant, but is removed in Christ"}
    ],
    "18": [
      {"type": "fulfillment", "target": "Exod 34:29-35", "note": "Beholding the glory of the Lord, we are being transformed into the same image from one degree of glory to another — Moses's face shone with reflected glory after encountering YHWH; now believers behold Christ's glory with unveiled faces and are transformed progressively into that same glory; the Mosaic type fulfilled in Christian experience"}
    ]
  },
  "4": {
    "6": [
      {"type": "allusion", "target": "Gen 1:3", "note": "God who said Let light shine out of darkness has shone in our hearts — the creation-light of Gen 1:3 is the type; the new creation-light of the gospel in the face of Christ is the antitype; conversion is a new-creation event"},
      {"type": "allusion", "target": "Isa 9:2", "note": "The people walking in darkness have seen a great light — the Isaianic light-in-darkness oracle; Paul identifies the light of the gospel with the prophetic light that was to dawn in the messianic age"}
    ]
  },
  "5": {
    "17": [
      {"type": "fulfillment", "target": "Isa 65:17", "note": "If anyone is in Christ, he is a new creation; the old has passed away, the new has come — Paul's new creation language directly echoes Isa 65:17 (I am creating new heavens and a new earth; the former things shall not be remembered); the eschatological new creation promised by Isaiah is present already in union with Christ"}
    ],
    "21": [
      {"type": "fulfillment", "target": "Isa 53:6", "note": "For our sake he made him to be sin who knew no sin — the substitutionary exchange (sinless one made sin; sinners made righteous) fulfills the Servant logic of Isa 53:6 where YHWH 'laid on him the iniquity of us all'; the great exchange of 2 Cor 5:21 is Isa 53 compressed into a single sentence"}
    ]
  },
  "6": {
    "2": [
      {"type": "fulfillment", "target": "Isa 49:8", "note": "In a favorable time I listened to you and in a day of salvation I have helped you — Paul quotes Isa 49:8 (LXX) and applies it to the present moment of gospel proclamation: 'Behold, now is the favorable time; now is the day of salvation.' The Isaianic day of YHWH's rescue is declared to have arrived in the gospel age"}
    ],
    "16": [
      {"type": "fulfillment", "target": "Lev 26:11-12", "note": "I will live in them and walk among them, and I will be their God, and they shall be my people — Paul's catena of OT quotations on the temple-community: Lev 26:11-12 (YHWH dwelling with Israel) is the first; the promise of the Shekinah-presence with Israel is fulfilled in the community of believers as the Spirit's temple"},
      {"type": "fulfillment", "target": "Isa 52:11", "note": "Come out from their midst and be separate, says the Lord — the second catena quote: Isa 52:11's call for the priests carrying the temple vessels to be ritually pure on the new exodus from Babylon; Paul applies the call to separation from idolatry to the Christian community"}
    ]
  },
  "8": {
    "9": [
      {"type": "allusion", "target": "Isa 53:2-3", "note": "Though he was rich, yet for your sake he became poor — the self-emptying of the pre-existent Christ echoes the Servant who had no form or majesty (Isa 53:2); the poverty of incarnation and cross parallels the Servant's voluntary humiliation for others' benefit"}
    ]
  },
  "12": {
    "9": [
      {"type": "allusion", "target": "Isa 40:29-31", "note": "My power is made perfect in weakness — YHWH gives power to the faint and increases the strength of the weak; Paul's experience of Christ's power through weakness is the Isaianic pattern of divine strength in human insufficiency reaching its Christological application"}
    ]
  }
}

def main():
    existing = load_echo('2corinthians')
    merge_echo(existing, ECHOES)
    save_echo('2corinthians', existing)
    total = sum(len(v) for v in existing.values())
    print(f'2 Corinthians echo: {len(existing)} chapters, {total} verses with connections.')

if __name__ == '__main__':
    main()
