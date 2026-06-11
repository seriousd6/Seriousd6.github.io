"""
MKT Echo Layer — Jeremiah chapters 37–40
Run: python3 scripts/zc-echo-jeremiah-37-40-fill.py

Key echo decisions:
- Ch 37 is structurally the most direct Jeremiah/Jesus parallel: the imprisoned
  prophet falsely accused, interviewed privately by the ruler who asks for a word from
  God. Pilate's private interrogation of Jesus (John 18:33-38) recapitulates the
  Zedekiah/Jeremiah pattern.
- 37:18 'what wrong have I done?' → 1 Pet 2:22-23 (he committed no sin; when they
  hurled insults at him he did not retaliate)
- 38:4-6: officials' charge 'put to death — he demoralizes the people' → Luke 23:2
  (the charge against Jesus); 38:6 cistern-without-water → Ps 69:2 (most-cited
  passion Psalm in NT)
- 38:7-13: Ebed-melech the Ethiopian rescues Jeremiah while covenant people condemn
  him → pattern of Gentile fidelity contrasted with covenant-people rejection
- 39:17-18: faith-and-escape promise to Ebed-melech → Eph 2:8 (saved through faith)
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

JER_ECHOES = {
  "37": {
    "17": [
      {
        "type": "type",
        "target": "John 18:33",
        "note": "Zedekiah's private nighttime interrogation of the imprisoned Jeremiah — 'Is there any word from the LORD?' — is structurally the prototype for Pilate's private interrogation of Jesus: 'Are you the king of the Jews?' (John 18:33-38). Both scenes feature a wavering ruler who privately seeks truth from the condemned prophet/messiah but lacks the courage to act on what he hears."
      }
    ],
    "18": [
      {
        "type": "allusion",
        "target": "1 Pet 2:22",
        "note": "Jeremiah's protest of innocence to Zedekiah — 'What wrong have I done to you, your servants, or this people, that you have put me in prison?' — is the prophetic precursor to 1 Peter's description of Christ: 'he committed no sin, and no deceit was found in his mouth. When they hurled insults at him, he did not retaliate' (1 Pet 2:22-23, quoting Isa 53:9). Both the prophet and the Servant suffer imprisonment without cause."
      }
    ]
  },
  "38": {
    "4": [
      {
        "type": "type",
        "target": "Luke 23:2",
        "note": "The officials' charge against Jeremiah — 'this man must be put to death; he is demoralizing the soldiers and the whole people' — is the direct structural type of the Sanhedrin's charge against Jesus before Pilate: 'we found this man subverting our nation ... stirring up the people all over Judea' (Luke 23:2, 5). In both cases, the covenant establishment charges the faithful prophet with sedition to secure a death sentence from a reluctant ruler."
      }
    ],
    "6": [
      {
        "type": "allusion",
        "target": "Ps 69:2",
        "note": "Jeremiah thrown into the waterless cistern where he sinks in the mud echoes Psalm 69:2 ('I sink in the miry depths, where there is no foothold; I have come into the deep waters') — the psalm of the suffering righteous one that is cited more often in the NT passion narrative than any other OT text (John 2:17; 15:25; 19:28-29; Rom 15:3; Acts 1:20). Jeremiah's cistern is a historical enactment of the psalm's imagery."
      }
    ],
    "7": [
      {
        "type": "theme",
        "target": "Matt 27:54",
        "note": "Ebed-melech the Ethiopian — a foreign court official — hears of Jeremiah's unjust imprisonment and intercedes for him when the covenant people have condemned him. The pattern of Gentile fidelity contrasted with covenant-people rejection culminates at the cross: the Roman centurion declares 'surely this was the Son of God' (Matt 27:54) while the chief priests and scribes mock. Both scenes feature a Gentile outsider who recognizes the innocence that insiders deny."
      }
    ]
  },
  "39": {
    "8": [
      {
        "type": "fulfillment",
        "target": "Matt 24:2",
        "note": "The Chaldeans' burning the royal palace and tearing down the walls of Jerusalem is the historical fulfillment that stands behind Jesus's prediction in Matt 24:2: 'not one stone here will be left on another; every one will be thrown down.' Jesus predicts a second fulfillment in 70 CE of the same pattern — covenant judgment expressed as temple and city destruction — that 39:8 records for 586 BCE."
      }
    ],
    "18": [
      {
        "type": "allusion",
        "target": "Eph 2:8",
        "note": "YHWH's promise to Ebed-melech — 'I will certainly save you; you will not fall by the sword. You will escape with your life, because you have trusted in me' — links salvation explicitly to faith in YHWH's word. This is the OT pattern that Paul systematizes in Eph 2:8: 'it is by grace you have been saved, through faith.' The Ethiopian's trust in YHWH's covenant faithfulness becomes the model of the faith-salvation connection that the NT universalizes."
      }
    ]
  },
  "40": {
    "2": [
      {
        "type": "theme",
        "target": "Luke 23:47",
        "note": "Nebuzaradan the Babylonian captain accurately interprets Jerusalem's fall as YHWH's covenant judgment: 'The LORD your God pronounced this disaster against this place ... because you sinned against the LORD.' A pagan military officer correctly discerns divine action that the covenant people missed. This mirrors Luke 23:47: the Roman centurion who declares 'surely this was a righteous man' after witnessing Jesus's death — a pagan perceiving what the religious establishment denied."
      }
    ]
  }
}

def main():
    existing = load_echo('jeremiah')
    merge_echo(existing, JER_ECHOES)
    save_echo('jeremiah', existing)

    out = json.loads((ROOT / 'data/echoes/jeremiah.json').read_text())
    for ch in range(37, 41):
        ck = str(ch)
        entries = out.get(ck, {})
        status = 'done' if entries else 'MISSING'
        count = sum(len(v) for v in entries.values())
        print(f'  ch {ch}: {status} ({count} echo entries across {len(entries)} verses)')

if __name__ == '__main__':
    main()
