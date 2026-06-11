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
        if ch not in existing: existing[ch] = {}
        for v, entries in verses.items():
            if v not in existing[ch]: existing[ch][v] = entries

ECHOES = {
  "23": {
    "9": [
      {"type": "allusion", "target": "John 17:16", "note": "Balaam's oracle: 'a people dwelling alone, and not counting itself among the nations.' The church inherits Israel's distinct-people identity; Jesus prays: 'They are not of the world, just as I am not of the world' (John 17:16). Peter applies it directly: 'a chosen race, a royal priesthood, a holy nation, a people for his own possession' (1 Pet 2:9) — the called-out community that does not count itself among the nations."}
    ],
    "19": [
      {"type": "allusion", "target": "Heb 6:18", "note": "Balaam's second oracle: 'God is not man, that he should lie, or a son of man, that he should change his mind.' Heb 6:18: 'it is impossible for God to lie' — grounding the believer's hope in the divine oath. Titus 1:2: 'God, who never lies.' The oracle establishes divine reliability as the bedrock of Israel's blessing; Hebrews makes it the ground of the believer's confidence in Christ's eternal priesthood."},
      {"type": "allusion", "target": "Titus 1:2", "note": "The contrast between human changeability and divine constancy in Balaam's oracle (v19) is the OT ground for Paul's 'God, who never lies' (Titus 1:2) and the 'promise before the ages began' — Christ's redemptive purpose established in the God who does not lie or change his mind."}
    ],
    "21": [
      {"type": "allusion", "target": "Matt 1:23", "note": "Balaam declares: 'the shout of a king is among them' (YHWH their God is with them). The divine presence in the midst of Israel — announced by an enemy prophet who cannot curse — becomes Emmanuel: 'God with us' (Matt 1:23). What Balaam saw as Israel's protective advantage ('YHWH their God is with them') finds its ultimate form in the incarnation where God is literally in the midst of his people in human flesh."}
    ],
    "23": [
      {"type": "allusion", "target": "Rom 8:31", "note": "Balaam: 'there is no enchantment against Jacob, no divination against Israel.' The impossibility of curse for the people God has blessed is the OT form of Paul's rhetorical climax in Rom 8:31-34: 'If God is for us, who can be against us?... Who shall bring any charge against God's elect? It is God who justifies.' Balaam, hired to curse, can only bless — because God has blessed; those justified in Christ face no condemnation (Rom 8:1)."}
    ]
  }
}

def main():
    e = load_echo('numbers')
    merge_echo(e, ECHOES)
    save_echo('numbers', e)
    print('Numbers 22-24 echo addendum (ch23) written.')

if __name__ == '__main__':
    main()
