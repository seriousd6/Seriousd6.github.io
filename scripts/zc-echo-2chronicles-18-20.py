"""
MKT Echo Layer — 2 Chronicles chapters 18–20
Run: python3 scripts/zc-echo-2chronicles-18-20.py

Ch18: Sheep without a shepherd (18:16) — Matt 9:36; Mark 6:34
Ch20: Abraham friend of God (20:7) — Jas 2:23
      Not knowing what to do, eyes on God (20:12) — 2 Cor 1:9
      Battle belongs to YHWH (20:15) — Eph 6:10-13
      Singing praise before the battle (20:21) — Rev 19:6; Ps 118:1
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

ECHOES = {
  "18": {
    "16": [
      {"type": "allusion", "target": "Matt 9:36", "note": "Micaiah's vision — 'I saw all Israel scattered on the mountains as sheep that have no shepherd' — is the OT source for Jesus's compassion-description: 'When he saw the crowds, he had compassion for them, because they were harassed and helpless, like sheep without a shepherd.' The language of the leaderless flock scattered on mountains describes both the covenant people without their king and the crowds without their true Shepherd."},
      {"type": "allusion", "target": "Mark 6:34", "note": "Markan parallel — Jesus saw a great crowd and had compassion, for they were like sheep without a shepherd, and he began to teach them many things. Micaiah's prophetic vision of Israel-scattered-without-a-shepherd is fulfilled when the true Shepherd arrives and begins to gather."}
    ]
  },
  "20": {
    "7": [
      {"type": "allusion", "target": "Jas 2:23", "note": "Jehoshaphat's prayer addresses God as the one who gave the land to 'the descendants of Abraham your friend' — the title 'friend of God' (YHWH's name for Abraham, also in Isa 41:8) is cited in James 2:23 as evidence that faith was credited as righteousness: 'Abraham believed God and it was counted to him as righteousness — and he was called a friend of God.' The prayer in 2 Chr 20 appeals to the covenant with the divine Friend; James grounds justification by faith in the same divine friendship."}
    ],
    "12": [
      {"type": "allusion", "target": "2 Cor 1:9", "note": "We do not know what to do, but our eyes are on you — Jehoshaphat's prayer of total dependence before the coalition attack is the OT form of Paul's testimony in 2 Cor 1:9: 'we had the sentence of death within ourselves so that we would not trust in ourselves but in God who raises the dead.' The prayer of acknowledged helplessness and directed attention to God is the covenant posture that both the Chronicler and Paul present as the ground of divine rescue."}
    ],
    "15": [
      {"type": "allusion", "target": "Eph 6:10", "note": "Do not be afraid or dismayed at this great horde, for the battle is not yours but God's — the promise that YHWH fights the battle that Israel cannot win is the foundation of the NT's spiritual-warfare theology. Ephesians 6:10: 'Be strong in the Lord and in the strength of his might.' The battle is divine; the human role is to stand, equipped with God's armor. The same pattern governs 2 Chr 20:17: 'stand and see the salvation of the LORD on your behalf.'"}
    ],
    "21": [
      {"type": "allusion", "target": "Rev 19:6", "note": "They appointed those who sang to the LORD and those who praised in holy attire, as they went before the army, saying 'Give thanks to the LORD, for his steadfast love endures forever' — the ḥesed-refrain sung before the battle is the OT form of the heavenly choir's acclamation in Rev 19:6: 'Hallelujah! For the Lord our God the Almighty reigns.' Praise precedes the divine victory in both texts."},
      {"type": "allusion", "target": "1 Chr 16:34", "note": "The praise-refrain 'Give thanks to the LORD, for his steadfast love endures forever' is the same formula David appointed at the Ark's installation (1 Chr 16:34 = Ps 118:1). Its deployment before the battle in 2 Chr 20:21 shows the liturgical formula functioning as a covenant-confidence declaration in the face of overwhelming odds."}
    ]
  }
}

def main():
    e = load_echo('2chronicles')
    merge_echo(e, ECHOES)
    save_echo('2chronicles', e)
    count = sum(len(v) for v in ECHOES.values())
    print(f'2chronicles echo: wrote entries for {count} verses across ch 18-20')

if __name__ == '__main__':
    main()
