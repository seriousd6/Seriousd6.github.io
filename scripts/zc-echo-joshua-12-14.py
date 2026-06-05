"""
Echo layer — Joshua 12–14
Run: python3 scripts/zc-echo-joshua-12-14.py

OT→NT direction: target = NT verse that takes up the OT passage.

Key decisions:
- Ch 12 (list of kings) → 1 Cor 15:25 / Rev 19:19: the catalog of conquered
  enemies is the OT archetype of Christ's eschatological subjugation of all
  powers; classified 'type'.
- Ch 13 (land still to possess) → Heb 4:8-9: the explicit NT argument — if Joshua
  had completed the rest, God would not have spoken of another day. The incompleteness
  is the argument's premise; classified 'allusion'.
- Ch 14 (Caleb's inheritance) → Heb 11:1 / Heb 6:12: Caleb is the exemplar of
  faith-sustained perseverance across 45 years; classified 'allusion'.
- No parallels file entries for chs 12–14.
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

JOSHUA_ECHOES_12_14 = {
    "12": {
        "7": [
            {"type": "type", "target": "1 Cor 15:25",
             "note": "The catalog of thirty-one defeated Canaanite kings is the paradigm of conquest: one by one, the enemies of God's people are overcome and their territories claimed. Paul declares the ultimate antitype: 'he must reign until he has put all his enemies under his feet' (1 Cor 15:25). Joshua's conquest list is the OT picture of what Christ's resurrection has begun and his return will complete — total subjugation of every hostile power."},
            {"type": "allusion", "target": "Rev 19:19",
             "note": "The kings who resisted Israel's advance and were defeated before the ark of the covenant anticipate 'the kings of the earth with their armies, gathered to make war against him who was sitting on the horse and against his army' (Rev 19:19) — who are likewise defeated. The pattern of earthly kings arrayed against the LORD's anointed runs from Canaan to the Apocalypse."}
        ]
    },
    "13": {
        "1": [
            {"type": "allusion", "target": "Heb 4:8",
             "note": "'There remains yet very much land to possess' — even at Joshua's old age, after the major campaigns, the inheritance was only partially realized. The author of Hebrews cites this incompleteness as his argument: 'if Joshua had given them rest, God would not have spoken of another day later on. So then, there remains a Sabbath rest for the people of God' (Heb 4:8-9). The land-rest Joshua administered was real but partial; it pointed to an eschatological rest that Joshua could not deliver."}
        ]
    },
    "14": {
        "7": [
            {"type": "allusion", "target": "Heb 6:12",
             "note": "Caleb recounts his forty-five years of faithful waiting: 'I was forty years old when Moses the servant of the LORD sent me...and I wholly followed the LORD my God' (v.8). After all those years of wilderness wandering and waiting for others to die, Caleb arrives to claim his inheritance at eighty-five years old. Hebrews 6:12 calls the community to 'imitate those who through faith and patience inherit the promises' — Caleb is the OT embodiment of this patient, persevering faith."},
            {"type": "allusion", "target": "Heb 11:1",
             "note": "Caleb 'wholly followed the LORD' for forty-five years — his confidence in God's promise (Num 14:24: 'my servant Caleb has a different spirit') sustained him through the entire wilderness generation's collapse. This is Hebrews 11:1 enacted: 'faith is the assurance of things hoped for, the conviction of things not seen.' Caleb never saw the inheritance during the wilderness years, yet he held it as certain and claimed it as his own the moment the door opened."}
        ],
        "11": [
            {"type": "allusion", "target": "2 Cor 4:16",
             "note": "Caleb at eighty-five: 'I am still as strong today as I was in the day that Moses sent me; my strength now is as my strength was then.' The outer man has not determined the inner man — the faith-vigor of the forty-year-old spy remained undimmed. Paul's principle 'though our outer self is wasting away, our inner self is being renewed day by day' (2 Cor 4:16) is Caleb's biography: physical age did not diminish his capacity for the kingdom's demands."}
        ]
    }
}


def main():
    existing = load_echo('joshua')
    merge_echo(existing, JOSHUA_ECHOES_12_14)
    save_echo('joshua', existing)
    ch_count = len(existing)
    v_count = sum(len(vs) for vs in existing.values())
    print(f'  Joshua echo: {ch_count} chapters, {v_count} verses with connections')


if __name__ == '__main__':
    main()
