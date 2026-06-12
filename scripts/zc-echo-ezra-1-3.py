"""
Echo Layer — Ezra chapters 1–3 (gap-fill: ch 2 missing)
Run: python3 scripts/zc-echo-ezra-1-3.py

Ch 1 and Ch 3 already have entries from zc-echo-ezra-1-4.py.
This script adds the missing Ch 2 echo entries:
- v2: Zerubbabel and Jeshua (Joshua) as the two leaders of the return — Zechariah
  interprets these as messianic types (Davidic king + priestly messiah); they appear
  in Matthew's genealogy as ancestral markers for the true king-priest
- v64: The 42,360 remnant — census echoing Num 26 before the second entry to the land;
  Paul's 'remnant chosen by grace' (Rom 11:5) is the NT fulfillment of the remnant theology
- v68: Freewill offerings for the temple — echoes Exod 35 voluntary tabernacle offerings
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

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

EZRA_ECHO = {
  "2": {
    "2": [
      {"type": "type", "target": "Zech 4:6-9", "note": "Zerubbabel heads the list of returning leaders — Zechariah later interprets Zerubbabel as the Davidic figure whose hands will complete the second temple by divine Spirit rather than military might (Zech 4:6-9); alongside Jeshua the high priest (Zech 3:1-10; 6:11-13), they form a dual king-priest prototype of the one who will 'bear the glory and sit and rule on his throne — a priest on his throne' (Zech 6:13), fulfilled in Christ who is both Davidic king and eternal high priest"},
      {"type": "allusion", "target": "Matt 1:12-13", "note": "Zerubbabel, son of Shealtiel, heads the list of returnees — the same Zerubbabel appears in Matthew's genealogy of Jesus (Matt 1:12-13), making the leader of the post-exilic return a direct ancestor of Christ; his inclusion marks the Davidic line as continuous through the exile and return, reaching its terminus in the one who fulfills all that Zerubbabel typified"}
    ],
    "64": [
      {"type": "allusion", "target": "Rom 11:5", "note": "The whole assembly together was 42,360 — the counted, named remnant who returned from Babylonian exile to rebuild the temple; their enumeration echoes the second census of Israel (Num 26) before entering the promised land, presenting the return as a new Exodus into a new inheritance; Paul's 'so too at the present time there is a remnant chosen by grace' (Rom 11:5) is the theological fulfillment: the true Israel is always a counted, grace-constituted remnant, not the mass of ethnic descent"}
    ],
    "68": [
      {"type": "allusion", "target": "2 Cor 9:7", "note": "Some of the heads of families, when they came to the house of YHWH in Jerusalem, made freewill offerings for the house of God — voluntary, generous giving for the rebuilding of the temple echoes the voluntary contributions for the tabernacle (Exod 35:4-29, where the people gave freely until Moses had to stop them); Paul's 'each one must give as he has decided in his heart, not reluctantly or under compulsion, for God loves a cheerful giver' (2 Cor 9:7) applies the same voluntary-offering principle to the new-covenant community building the living temple of the church"}
    ]
  }
}

def main():
    e = load_echo('ezra')
    before_chs = set(e.keys())
    merge_echo(e, EZRA_ECHO)
    after_chs = set(e.keys())
    new_chs = after_chs - before_chs
    save_echo('ezra', e)
    print(f'ezra echo ch 1-3: added ch2 entries ({len(EZRA_ECHO["2"])} verses); ch2 now complete')
    if new_chs:
        print(f'  new chapters added: {sorted(new_chs, key=int)}')

if __name__ == '__main__':
    main()
