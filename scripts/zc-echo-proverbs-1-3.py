"""
echo — Proverbs 1–3
Run: python3 scripts/zc-echo-proverbs-1-3.py
Ch1 (v7) and ch3 (v11, v34) already have entries; this script adds ch2.
Key echoes: seeking wisdom (James 1:5), wisdom from God's mouth (Col 2:3 / 1 Cor 1:24),
  stored wisdom (Col 2:3), wisdom entering the heart (Jer 31:33), land inheritance (Matt 5:5).
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

PROVERBS_ECHOES = {
  "2": {
    "3": [
      {
        "type": "allusion",
        "target": "Jas 1:5",
        "note": "If you call out for insight and cry aloud for understanding — Proverbs 2:3-5 frames the search for wisdom as urgent petition; James 1:5 issues the same invitation under the new covenant: 'If any of you lacks wisdom, let him ask God, who gives generously to all without reproach, and it will be given him.' The receptive posture of crying out is retained; the source is made explicit — God in Christ."
      }
    ],
    "6": [
      {
        "type": "allusion",
        "target": "1 Cor 1:24",
        "note": "For the LORD gives wisdom; from his mouth come knowledge and understanding — the divine source of wisdom becomes personal in Christ: 'Christ the power of God and the wisdom of God' (1 Cor 1:24). The mouth from which wisdom proceeds in Proverbs 2:6 is identified in John 1:1 with the Word who became flesh; the wisdom that was God's gift is now God's person."
      },
      {
        "type": "allusion",
        "target": "Col 2:3",
        "note": "Knowledge and understanding given from God's mouth — Paul says that in Christ 'are hidden all the treasures of wisdom and knowledge' (Col 2:3); what Proverbs locates in God's mouth, Paul locates in the person of Christ, showing that the gift of wisdom and the Giver have become one in the incarnation."
      }
    ],
    "7": [
      {
        "type": "allusion",
        "target": "Col 2:3",
        "note": "He stores up sound wisdom for the upright — the divine treasury of wisdom described here is directly echoed in Colossians 2:3: in Christ 'are hidden all the treasures of wisdom and knowledge.' The stored wisdom of Proverbs 2:7 is not an impersonal divine reserve but a person: Jesus Christ, in whom the fullness of God's wisdom dwells bodily (Col 2:9)."
      }
    ],
    "10": [
      {
        "type": "allusion",
        "target": "Jer 31:33",
        "note": "For wisdom will enter your heart, and knowledge will be pleasant to your soul — the internalization of wisdom (heart-entry) anticipates the new covenant promise of Jeremiah 31:33: 'I will put my law within them, and I will write it on their hearts.' What Proverbs frames as the goal of the wise life becomes the new covenant gift; the Spirit who produces wisdom from within (1 Cor 2:12-13) is the fulfillment of Proverbs' vision of wisdom-in-the-heart."
      }
    ],
    "18": [
      {
        "type": "allusion",
        "target": "John 14:6",
        "note": "Her house sinks down to death, and her paths to the departed — the way of Folly leads to Sheol; the contrast with Wisdom's way (v9: 'every good path') reaches its fulfillment in Christ's claim 'I am the way, the truth, and the life' (John 14:6). The two paths of Proverbs 2 (Wisdom's way of life vs. Folly's way to death) are concentrated in two persons: Christ the living Way, and death itself which he has conquered (Rev 1:18)."
      }
    ],
    "21": [
      {
        "type": "allusion",
        "target": "Matt 5:5",
        "note": "For the upright will inhabit the land, and the blameless will remain in it — the land-inheritance promise here (also Ps 37:11, 29) is the Wisdom tradition's application of the Deuteronomic blessing to the righteous life. Jesus's beatitude 'blessed are the meek, for they shall inherit the earth' (Matt 5:5) cites Psalm 37:11 but widens the scope to the whole earth: the land promise of Proverbs 2:21 reaches its eschatological fulfillment in the meek inheriting the renewed creation through Christ."
      }
    ]
  }
}

def main():
    existing = load_echo('proverbs')
    merge_echo(existing, PROVERBS_ECHOES)
    save_echo('proverbs', existing)
    print('proverbs echo: wrote ch2 entries (6 verses); ch1+3 already present')

if __name__ == '__main__':
    main()
