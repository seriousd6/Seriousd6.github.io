"""
Echo data — Psalms chapters 68–70 (gap-fill: only ch 70 missing; 68, 69 already present)
Run: python3 scripts/zc-echo-psalms-68-70.py

Psalm 70 is an abbreviated parallel of Psalm 40:13-17 — David's urgent five-verse
lament for divine rescue. Its brevity belies its NT freight:

- v1: "O God, hurry to deliver me / O LORD, make haste to help me" — The urgent
  prayer for swift rescue is the language of Gethsemane (Matt 26:39, 42; Heb 5:7:
  Christ offered prayers with loud cries to the one who could save him from death).
- v5: "I am poor and needy; hurry to me, O God! You are my help and my deliverer" —
  2 Cor 8:9: Christ became poor so that through his poverty we might become rich.
  The psalmist's poverty-and-dependence is the condition Christ entered for our sake.
- v4: "let those who love your salvation say always, 'God is great!'" — Phil 4:4 /
  Rev 15:3-4 (the doxology of the redeemed).
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

# INTENT: Echo data for Psalm 70 only — the urgent five-verse lament that Christ
#   inhabits in his passion (Heb 5:7 / Gethsemane), and whose 'poor and needy'
#   self-identification maps onto the incarnation of the one who became poor
#   for our sake (2 Cor 8:9).
# CHANGE? If data/echoes/psalms.json structure changes, update load_echo/save_echo
#   per Z_COMMENTARY_SCRIPT_GUIDE.md.
# VERIFY: python3 -c "import json; d=json.load(open('data/echoes/psalms.json')); print(len(d.get('70',{})), 'verses in ch70')" should print "3 verses in ch70".

PSALMS_ECHOES = {
  "70": {
    "1": [
      {
        "type": "allusion",
        "target": "Heb 5:7",
        "note": "O God, hurry to deliver me! O LORD, make haste to help me! — 'During the days of Jesus' life on earth, he offered up prayers and petitions with fervent cries and tears to the one who could save him from death' (Heb 5:7). The urgent cry of Psalm 70:1 — make haste, do not delay — is the cry of Gethsemane. The Psalm provides the vocabulary for Christ's passion prayer, the one addressed to the one who could save from death, though salvation came through rather than from the death."
      },
      {
        "type": "allusion",
        "target": "Matt 26:39",
        "note": "O God, hurry to deliver me! — 'My Father, if it is possible, may this cup be taken from me. Yet not as I will, but as you will' (Matt 26:39). The urgency of Psalm 70:1 — the plea for swift divine rescue — is the shape of Gethsemane. Christ prays the Psalm's prayer with his own submission added: 'make haste to help me' but 'not my will but yours.' The Psalm is both fulfilled and transformed: the rescue comes through the cross, not from it."
      }
    ],
    "4": [
      {
        "type": "allusion",
        "target": "Phil 4:4",
        "note": "But let all who seek you rejoice and be glad in you; let those who love your salvation say always, 'God is great!' — 'Rejoice in the Lord always. I will say it again: Rejoice!' (Phil 4:4). The Psalm's doxological refrain of those who love divine salvation is Paul's command to the church. The 'God is great!' of Psalm 70:4 becomes the sustained posture of the redeemed, grounded not in circumstances but in the salvation accomplished through Christ."
      }
    ],
    "5": [
      {
        "type": "allusion",
        "target": "2 Cor 8:9",
        "note": "But I am poor and needy; hurry to me, O God! You are my help and my deliverer — 'For you know the grace of our Lord Jesus Christ, that though he was rich, yet for your sake he became poor, so that you through his poverty might become rich' (2 Cor 8:9). The Psalmist's self-identification as 'poor and needy' dependent entirely on divine rescue is the condition Christ voluntarily entered in the incarnation. He who was rich took the posture of the poor-and-needy Psalmist so that those who are genuinely poor and needy might be raised to his riches."
      },
      {
        "type": "allusion",
        "target": "Heb 2:18",
        "note": "I am poor and needy; hurry to me, O God! You are my help and my deliverer — 'Because he himself suffered when he was tempted, he is able to help those who are being tempted' (Heb 2:18). The one who prayed this psalm in his poverty and need now stands as the deliverer who can help. The helper (v5: 'you are my help') becomes the help himself — the one who passed through the 'poor and needy' condition is the sympathetic deliverer for all who pray this psalm."
      }
    ]
  }
}

def main():
    existing = load_echo('psalms')
    merge_echo(existing, PSALMS_ECHOES)
    save_echo('psalms', existing)
    for ch in ['68', '69', '70']:
        entries = len(existing.get(ch, {}))
        print(f"  ch{ch}: {entries} verses with entries")
    print("Psalms 68–70 echoes complete.")

if __name__ == '__main__':
    main()
