"""
Echo layer — Matthew chapters 23–24 (Woes + Olivet Discourse part 1)
Output: data/echoes/matthew.json (adds ch23-24)

Ch23: Seven woes against scribes and Pharisees; lament over Jerusalem.
Ch24: Olivet Discourse — signs of the end, abomination of desolation,
      coming of the Son of Man.
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
  "23": {
    "35": [
      {"type": "allusion", "target": "Gen 4:8", "note": "From the blood of Abel to the blood of Zechariah — Abel (Genesis, first book) to Zechariah (2 Chr 24:20-22, last book in Hebrew canon); Jesus names the canonical range of prophetic martyrdom as the charge against this generation"},
      {"type": "allusion", "target": "2 Chr 24:20-22", "note": "Zechariah the son of Barachiah, whom you murdered between the sanctuary and the altar — the murder of Zechariah in the temple court; his dying words (may the LORD see and avenge) now being answered in judgment"}
    ],
    "37": [
      {"type": "allusion", "target": "Ps 17:8", "note": "How often would I have gathered your children together as a hen gathers her chicks under her wings — YHWH shelters under the shadow of his wings; Jesus uses the divine-protection image for his own longing over Jerusalem"},
      {"type": "allusion", "target": "Deut 32:11", "note": "As an eagle stirs up its nest and hovers over its young — YHWH's protective wing over Israel in the wilderness; the mother-bird sheltering image applied to Jesus's desire to gather Jerusalem"}
    ],
    "39": [
      {"type": "fulfillment", "target": "Ps 118:26", "note": "You will not see me again until you say: Blessed is he who comes in the name of the LORD — the triumphal entry Psalm cited at the final departure from the temple; the Psalm-cry that came at entry will mark the eschatological return"}
    ]
  },
  "24": {
    "15": [
      {"type": "fulfillment", "target": "Dan 9:27", "note": "The abomination of desolation spoken of by the prophet Daniel, standing in the holy place — the Danielic abomination (shiqquts meshomem) fulfilled in the desolating sacrilege of the temple; Jesus applies the Danielic oracle to the imminent crisis"}
    ],
    "21": [
      {"type": "allusion", "target": "Dan 12:1", "note": "For then there will be great tribulation such as has not been since the beginning of the world — Daniel's time of trouble, such as never was since there was a nation (Dan 12:1); the great tribulation language is directly Danielic"}
    ],
    "29": [
      {"type": "fulfillment", "target": "Isa 13:10", "note": "The sun will be darkened and the moon will not give its light and the stars will fall from heaven — the Day of the LORD cosmic signs of Isa 13:10 (the stars of heaven and their constellations will not give their light); the Son of Man coming borrows the Day-of-LORD cosmic language"},
      {"type": "allusion", "target": "Joel 2:10", "note": "The sun and the moon are darkened and the stars withdraw their shining — Joel's Day-of-the-LORD cosmological signs; Matthew's apocalyptic imagery draws from the prophetic Day-of-LORD tradition"}
    ],
    "30": [
      {"type": "fulfillment", "target": "Dan 7:13-14", "note": "They will see the Son of Man coming on the clouds of heaven with power and great glory — the Danielic vision of one like a Son of Man coming with the clouds of heaven; Jesus applies this directly to his own eschatological coming"},
      {"type": "allusion", "target": "Zech 12:10", "note": "They will look on the one they have pierced and mourn — the mourning at the Son of Man's coming echoes the Zecharian mourning when Jerusalem sees the pierced one; grief and recognition at the parousia"}
    ],
    "31": [
      {"type": "allusion", "target": "Isa 27:13", "note": "He will send out his angels with a great trumpet call — the great trumpet blown (shofar gadol) to gather Israel from exile; the eschatological ingathering with the trumpet as the signal"}
    ],
    "37": [
      {"type": "allusion", "target": "Gen 6:5-12", "note": "As were the days of Noah, so will be the coming of the Son of Man — eating and drinking, marrying, until the flood came; the normalcy-before-judgment pattern of Noah's generation repeated before the parousia"}
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
