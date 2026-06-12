"""
Echo Layer — 1 Samuel chapters 13–14
Run: python3 scripts/zc-echo-1samuel-13-14-fill.py

Ch13 already has v14 (Acts 13:22 — "man after his own heart").
This script adds ch14 entries only; ch13 entries are preserved by merge_echo.

Key echo connections:
- 14:6  — Jonathan's "nothing prevents YHWH from saving by many or few"
            → Gideon's army reduction (Judg 7:2-7); Zech 4:6; 2 Cor 12:9
- 14:15 — divine terror/panic (ḥărāḏāh from God)
            → holy-war divine panic pattern (Josh 10:10; Exod 23:27)
- 14:23 — "YHWH saved Israel that day"
            → the salvation-of-YHWH formula (Exod 14:13; Luke 1:68-71)
- 14:29 — Jonathan's "enlightened eyes" after honey
            → Ps 19:8 (the commandment enlightening the eyes)
- 14:45 — people ransom Jonathan from death sentence
            → shadow of Christ's trial (reverse: the crowd chose against the
               righteous; here the crowd chooses for him)
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

SAMUEL_ECHOES = {
  "14": {
    "3": [
      {
        "type": "theme",
        "target": "1 Sam 2:27-36",
        "note": "Ahijah wears the ephod at Saul's camp — he is a descendant of Eli's line (Phinehas, Ichabod's brother). The presence of a priest from the condemned Shilonite house alongside a king who will also be rejected signals the convergence of two failed institutions. Samuel's earlier oracle against Eli's house (2:27-36) is quietly being enacted."
      }
    ],
    "6": [
      {
        "type": "theme",
        "target": "Judg 7:2",
        "note": "Jonathan's declaration — 'Nothing prevents YHWH from saving, whether by many or by few' — is the same theological principle that governs Gideon's army reduction: YHWH deliberately strips Israel of military advantage so that the victory cannot be attributed to human strength. Jonathan acts on this conviction without divine command, making him a more spontaneous expression of the principle than Gideon."
      },
      {
        "type": "theme",
        "target": "Zech 4:6",
        "note": "The divine freedom to save 'by many or by few' anticipates Zechariah's word: 'Not by might, nor by power, but by my Spirit, says the LORD of hosts.' The Philistine garrison represents overwhelming human advantage; Jonathan's advance without waiting for numbers is an act of trust in the Spirit-power of YHWH independent of military calculus."
      }
    ],
    "12": [
      {
        "type": "theme",
        "target": "Judg 7:9-11",
        "note": "The confirmatory sign — 'come up to us' as the indicator that YHWH has given them into Jonathan's hand — follows the Gideon pattern of seeking a divine sign before a bold military action. The sign is based on the enemy's own words rather than a miraculous event, showing YHWH's providential control over the speech of his enemies."
      }
    ],
    "15": [
      {
        "type": "type",
        "target": "Josh 10:10",
        "note": "The divine terror (ḥărāḏāh gedôlāh, 'great trembling/panic from God') thrown into the Philistine camp is the standard holy-war panic: YHWH throws the enemy into confusion so that Israel's human action strikes a demoralized foe. Joshua 10:10 uses the identical motif. The ground itself shakes — the trembling extends from human hearts to the earth, a sign of cosmic divine action."
      },
      {
        "type": "shadow",
        "target": "Hag 2:21",
        "note": "The shaking of the ground (wayyirʿaš hāʾāreṣ) anticipates the eschatological shaking — 'I am about to shake the heavens and the earth' (Hag 2:21; Heb 12:26-27). The Michmash earthquake is a temporal foretaste of the final divine upheaval in which all human powers are overturned."
      }
    ],
    "23": [
      {
        "type": "theme",
        "target": "Exod 14:13",
        "note": "'YHWH saved Israel that day' (wayyôšaʿ YHWH bayôm hahûʾ) is the salvation-of-YHWH formula first established at the Red Sea: 'stand firm and see the salvation of YHWH' (Exod 14:13). The yəšûʿāh vocabulary links every judge-deliverance and royal victory to the Exodus pattern; Christ's work (Heb. Yēšûaʿ, salvation) fulfills the formula permanently."
      }
    ],
    "29": [
      {
        "type": "allusion",
        "target": "Ps 19:8",
        "note": "Jonathan's eyes were 'enlightened' (ʾôrû ʿênāyw) after tasting honey, in direct contrast to the enfeebling effect of Saul's oath. Ps 19:8 uses the same construction: 'the commandment of the LORD is pure, enlightening the eyes.' The true life-giving word from YHWH restores and illuminates; Saul's oath, made in YHWH's name but against YHWH's purposes, does the opposite."
      }
    ],
    "35": [
      {
        "type": "theme",
        "target": "Gen 12:8",
        "note": "Saul builds an altar to YHWH — the text notes this is the first altar he built. The king constructing a personal altar follows the patriarchal pattern (Abraham, Gen 12:8; Isaac, Gen 26:25), but in Saul's context the altar comes after a series of unauthorized decisions; the gesture of worship does not compensate for the pattern of disobedience that the chapter documents."
      }
    ],
    "45": [
      {
        "type": "shadow",
        "target": "Mark 15:11",
        "note": "The people ransom Jonathan from Saul's death sentence: 'Should Jonathan die — the one who brought this great deliverance to Israel? Far from it! As the LORD lives, not one hair of his head will fall.' The crowd's intervention saves the righteous man from a wrongful death-sentence. The narrative inverts the Barabbas scene (Mark 15:11-15): at Golgotha, the crowd chose the guilty man; at Michmash, they chose the innocent one. The contrast illuminates how extraordinary the Barabbas decision was — the normal moral instinct, as demonstrated here, is to save the one who actually delivered them."
      }
    ]
  }
}

def main():
    existing = load_echo('1samuel')
    merge_echo(existing, SAMUEL_ECHOES)
    save_echo('1samuel', existing)
    print('1 Samuel 13-14 echoes written.')

if __name__ == '__main__':
    main()
