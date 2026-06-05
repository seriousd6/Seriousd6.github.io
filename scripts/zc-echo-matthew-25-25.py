"""
Echo layer — Matthew chapter 25 (Olivet Discourse conclusion)
Output: data/echoes/matthew.json (adds ch25)

Ch25: Ten virgins; talents; sheep and goats.
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
  "25": {
    "1": [
      {"type": "allusion", "target": "Isa 62:5", "note": "The parable of the ten virgins: the bridegroom delayed — as the bridegroom rejoices over the bride, so shall your God rejoice over you; the messianic bridegroom-coming as the frame for the virgins parable"},
      {"type": "allusion", "target": "Song 3:4", "note": "I found him whom my soul loves — the beloved sought and found at night; the virgins watching for the bridegroom in the Song's seeking-beloved tradition"}
    ],
    "11": [
      {"type": "allusion", "target": "Ps 24:7-10", "note": "Lord, Lord, open to us — the gate that must open for the king to enter (Lift up your heads, O gates, that the King of glory may come in); the closed door of the unprepared echoes the gate that only opens for those who are ready"}
    ],
    "14": [
      {"type": "allusion", "target": "Prov 31:13-16", "note": "The parable of the talents: each according to his own ability — the capable wife (eshet hayil) puts her hands to the distaff, makes profitable investments, does not waste; the talent-steward exercising profitable management"},
      {"type": "allusion", "target": "Isa 22:20-22", "note": "A man going on a journey put his servants in charge — the steward entrusted with the house in the master's absence; the talent-parable draws on the master-steward tradition of the wisdom literature"}
    ],
    "30": [
      {"type": "allusion", "target": "Dan 12:3", "note": "Cast the worthless servant into the outer darkness — those who do not shine like stars will be in everlasting contempt; the outer darkness of judgment vs. the brightness of the wise"}
    ],
    "31": [
      {"type": "fulfillment", "target": "Dan 7:13-14", "note": "When the Son of Man comes in his glory and all the angels with him — the Danielic coming of the Son of Man with the court assembled; the judgment-throne scene of the sheep and goats is the fulfillment of the Danielic vision"},
      {"type": "allusion", "target": "Joel 3:2", "note": "All the nations will be gathered before him — I will gather all the nations and bring them down to the Valley of Jehoshaphat; the universal gathering for judgment at the eschatological court"}
    ],
    "34": [
      {"type": "allusion", "target": "Gen 1:3", "note": "Come, you who are blessed by my Father, inherit the kingdom prepared for you from the foundation of the world — the kingdom prepared before creation; the eschatological inheritance pre-existing in the divine purpose from creation's beginning"}
    ],
    "40": [
      {"type": "allusion", "target": "Prov 19:17", "note": "Truly I say to you, as you did it to one of the least of these my brothers, you did it to me — whoever is generous to the poor lends to the LORD; Jesus radicalizes the wisdom principle: care for the poor-and-needy is care for the King himself"}
    ]
  }
}

def main():
    existing = load_echo('matthew')
    merge_echo(existing, ECHOES)
    save_echo('matthew', existing)
    total = sum(len(v) for v in existing.values())
    print(f'Matthew echo: {len(existing)} chapters, {total} verses with connections.')

if __name__ == '__main__':
    main()
