"""
MKT Christ Commentary — Isaiah chapter 18
Run: python3 scripts/zc-christ-isaiah-18.py

Source data used:
- data/interlinear/isaiah.json
- data/translation/draft/mediating/isaiah.json

Key decisions in this range:
- v. 3: shadow — nes (signal/banner) on mountains; universal summons; Christ lifted up John 12:32
- v. 7: shadow — feared distant nation brings gifts to Zion; Matt 2 Magi connection
- vv. 4-5: revelation of God — divine patience and precise timing of judgment
"""
import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_comm(source, book):
    p = ROOT / 'data' / 'commentary' / source / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_comm(source, book, data):
    p = ROOT / 'data' / 'commentary' / source / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_comm(existing, new_data):
    # INTENT: Non-destructive merge — existing entries are never overwritten, safe to re-run
    for ch, verses in new_data.items():
        if ch not in existing: existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]: existing[ch][v] = html

ISAIAH = {
"18": {
"1": "<p>A revelation of God: the oracle opens to the land of Cush (Ethiopia) — the most distant, feared people at the edges of the known world. YHWH's prophetic word reaches even there, establishing his universal sovereignty. This oracle prepares the ground for v. 7: the same distant people who are addressed in judgment become those who bring gifts to Zion. The God who speaks to the margins of the earth is the God who gathers those same margins to himself.</p>",
"2": "<p>A revelation of God: swift messengers sent to a people tall and smooth, feared near and far (<em>gôy yerā' ûmôrā'</em> — a nation dreaded and awe-inspiring). YHWH's messengers go to every nation — not only Israel. The divine word is not geographically bounded. This anticipates the missionary sending of Acts 1:8 (<em>to the ends of the earth</em>) and the specific inclusion of Ethiopia in the early church (Acts 8:26-39: the Ethiopian eunuch).</p>",
"3": "<p>A shadow: <em>kol-yōšĕb̠ê tēb̠ēl wĕšōkĕnê 'āreṣ</em> — all inhabitants of the world, all who dwell on the earth — when the signal (<em>nēs</em>) is lifted on the mountains, look! The banner raised on the mountain is the same <em>nēs</em> of Isaiah 11:10,12 — the messianic standard around which all nations gather. Christ identifies himself as the fulfillment of this signal in John 12:32: <em>when I am lifted up from the earth, I will draw all people to myself</em>. The elevation of the cross is the raising of the banner that summons all the earth.</p>",
"4": "<p>A revelation of God: YHWH will be still and look from his dwelling — <em>kĕḥōm ṣaḥ 'ălê-'ôr</em> — like the clear heat of sunlight, like a cloud of dew in harvest heat. Divine stillness before judgment is not inactivity but sovereign watchfulness. This is the patience of God (2 Pet 3:9: not willing that any should perish) that the NT frames as the space between Christ's ascension and return — the appointed time when the gospel goes to all nations.</p>",
"5": "<p>A revelation of God: at the right moment YHWH cuts the growing shoot, removes the spreading branches — <em>wĕkārat 'et-hazyalzallîm b̠ammazmerôt</em>. The precise timing of divine judgment — when the blossom is over and the flower becomes a ripening grape — models what the NT calls <em>the fullness of time</em> (Gal 4:4). YHWH acts not at human impatience but at the moment of maximum effectiveness. The vine-pruning imagery connects to John 15:1-2 (the Father prunes every branch).</p>",
"6": "<p>A revelation of God: the pruned branches left to birds of prey and to the beasts of the earth — summer and winter alike. The abandoned branches are the aftermath of opposed divine purpose. This stark image of judgment establishes the reality that YHWH's patience (v. 4) has an endpoint — the pruning will come. Christ uses similar imagery (Matt 13:40-42: the weeds gathered and burned at the harvest).</p>",
"7": "<p>A shadow: <em>b̠ā'ēt hahî' yûb̠al-šay lĕYHWH ṣĕb̠ā'ôt</em> — at that time gifts will be brought to YHWH of hosts from the tall and smooth people, the feared and conquering nation, to Mount Zion. The most distant, feared, and powerful nation becomes a gift-bearer to Zion — the complete reversal of the oracle's opening. This is the eschatological ingathering of all nations (Isa 60:6-7; Ps 72:10). Matthew 2:1-12 (the Magi from the east bringing gifts) is an initial fulfillment; Revelation 21:24-26 (the kings of the earth bringing glory and honor into the new Jerusalem) is its consummation. The feared nation of Isa 18:2 and 18:7 becomes the gift-bearing nation before the enthroned King.</p>"
}
}

def main():
    existing = load_comm('mkt-christ', 'isaiah')
    merge_comm(existing, ISAIAH)
    save_comm('mkt-christ', 'isaiah', existing)
    v = sum(len(vs) for vs in ISAIAH.values())
    print(f'Isaiah 18 mkt-christ: {v} verses written.')

if __name__ == '__main__':
    main()
