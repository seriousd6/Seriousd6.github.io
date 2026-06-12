#!/usr/bin/env python3
"""echo layer — Judges 14–17 (Samson cycle and Micah's shrine)
Run: python3 scripts/zc-echo-judges-14-17.py
Key NT echoes: Spirit-empowerment and Heb 11:32-34; riddle/gospel-paradox (John 12:24; 1 Cor 1:25);
water from rock (John 7:38); Gaza gate-posts (Matt 16:18); 'remember me' prayer (Luke 23:42);
death that bears more fruit (John 12:24); 'everyone right in own eyes' (John 18:37).
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent

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
  "14": {
    "4": [
      {
        "type": "typology",
        "target": "Acts 2:23",
        "note": "YHWH used Samson's sinful desire as the occasion to work judgment on the Philistines — 'this was from the LORD.' Divine sovereignty working through human sin and weakness is the grammar of the Incarnation: Christ was 'delivered up according to the definite plan and foreknowledge of God' (Acts 2:23); even betrayal and crucifixion are woven into the redemptive purpose."
      }
    ],
    "6": [
      {
        "type": "typology",
        "target": "Heb 11:34",
        "note": "The Spirit of YHWH rushing upon Samson to tear a lion barehanded — strength made available through the Spirit for the impossible — belongs to the paradigm honored in Hebrews 11:34: those who 'through faith became mighty in war, put foreign armies to flight.' Spirit-given power over what destroys foreshadows the resurrection strength poured out at Pentecost (Acts 1:8)."
      }
    ],
    "9": [
      {
        "type": "typology",
        "target": "John 12:24",
        "note": "Honey from the dead lion's carcass — life and sweetness coming out of the place of death — is the OT visual of the gospel paradox that Jesus names in John 12:24: 'Unless a grain of wheat falls into the earth and dies, it remains alone; but if it dies, it bears much fruit.' Life from death is not just resurrection doctrine but the structural logic of redemption."
      }
    ],
    "14": [
      {
        "type": "echo",
        "target": "1 Cor 1:25",
        "note": "Samson's riddle — 'Out of the eater came something to eat; out of the strong came something sweet' — is the most compressed OT statement of the cross-logic: life from death, sweetness from the destroyer, strength revealed through apparent defeat. Paul identifies this as the pattern of God's wisdom: 'the foolishness of God is wiser than human wisdom, and the weakness of God is stronger than human strength' (1 Cor 1:25)."
      }
    ]
  },
  "15": {
    "14": [
      {
        "type": "allusion",
        "target": "Heb 11:34",
        "note": "The Spirit of YHWH rushing upon Samson at Lehi — bonds bursting, a thousand slain with a donkey's jawbone — is the paradigmatic act of Spirit-enabled impossible victory that Hebrews 11:34 honors: 'became mighty in war, put foreign armies to flight.' The weapon is absurd; the victory is total; the power is entirely the Spirit's — the pattern of every gospel act of power."
      }
    ],
    "18": [
      {
        "type": "echo",
        "target": "Phil 4:6",
        "note": "Samson's first recorded prayer — crying out to YHWH in thirst after his greatest military victory — models covenant dependence: bringing every need to God even from the peak of achievement. Philippians 4:6: 'in everything by prayer and supplication with thanksgiving let your requests be made known to God.' The mightiest act of faith requires the prayer of the weakest moment."
      }
    ],
    "19": [
      {
        "type": "typology",
        "target": "John 7:38",
        "note": "God split open the hollow place at Lehi and water poured out — the same rock-water miracle as Meribah (Exod 17:6), which Paul identifies as the pre-incarnate Christ providing for Israel (1 Cor 10:4). Jesus applies the pattern to himself: 'Whoever believes in me, as the Scripture has said, rivers of living water will flow from his heart' (John 7:38). The rock that gives drink in the place of death is Christ."
      }
    ]
  },
  "16": {
    "3": [
      {
        "type": "echo",
        "target": "Matt 16:18",
        "note": "Samson tears up the gate-posts of Gaza — the city that tried to trap and kill him — and carries them on his shoulders to a hilltop. Jesus promises that 'the gates of hell will not prevail against my church' (Matt 16:18); both use city-gates as the emblem of hostile power that cannot hold the covenant servant. The gate-bearer on a hill points forward to the cross-bearer on Golgotha."
      }
    ],
    "20": [
      {
        "type": "echo",
        "target": "Rev 3:20",
        "note": "Samson did not know that the LORD had departed from him — the tragedy of habitual sin eroding awareness of the Spirit's presence until his absence goes unnoticed. Revelation 3:20 addresses the same condition in Laodicea: Christ standing outside the door of his own church, knocking. The danger of spiritual numbness — continuing the motions while the presence has withdrawn — is the deepest warning of the Samson cycle."
      }
    ],
    "28": [
      {
        "type": "allusion",
        "target": "Luke 23:42",
        "note": "Samson's prayer at the pillars — 'Remember me and strengthen me just this once, O God' — echoes in the penitent thief's 'remember me when you come into your kingdom' (Luke 23:42). Both men at the moment of final humiliation appeal to divine memory as the ground for one last act of grace. Both deaths accomplish more than their lives. Christ's 'today you will be with me in paradise' is the answer Samson hoped for."
      }
    ],
    "30": [
      {
        "type": "typology",
        "target": "John 12:24",
        "note": "Samson's death killed more Philistines than he had killed in his entire life — the greatest victory came through dying. Hebrews 11:32-34 honors him among those made mighty through faith. Jesus identifies this as the universal principle of redemption: 'unless a grain of wheat falls into the earth and dies, it remains alone; but if it dies, it bears much fruit' (John 12:24). The power of Samson's death is the shadow of the power of the cross."
      }
    ]
  },
  "17": {
    "5": [
      {
        "type": "echo",
        "target": "Col 2:23",
        "note": "Micah's private shrine — ephod, teraphim, self-installed priest — represents religion designed by personal preference while using YHWH's name and vocabulary. Colossians 2:23 warns against 'self-made religion' that has 'an appearance of wisdom' but is disconnected from Christ, the head. The Micah episode begins the Judges epilogue that explains how Israel arrives at civil war: the same logic that produces idolatry produces violence."
      }
    ],
    "6": [
      {
        "type": "echo",
        "target": "John 18:37",
        "note": "The epilogue's signature refrain — 'there was no king in Israel; everyone did what was right in his own eyes' — diagnoses the root crisis of the Judges era as the absence of a true king whose word defines right and wrong. Jesus came 'to bear witness to the truth' as the king whose reign establishes the only reliable standard (John 18:37); Deuteronomy 17:18-20 anticipated a king who would read the Torah all his days. Christ is that king."
      }
    ]
  }
}

if __name__ == '__main__':
    e = load_echo('judges')
    merge_echo(e, ECHOES)
    save_echo('judges', e)

    chs = sorted(e.keys(), key=int)
    print(f'Judges echo chapters now present: {chs}')
    for ch in ['14', '15', '16', '17']:
        vv = list(e.get(ch, {}).keys())
        print(f'  ch{ch}: {len(vv)} verse(s) with entries — {"OK" if vv else "MISSING"}')
