"""
MKT Echo — Amos chapters 6–9 (ch9:11 already exists)
Run: python3 scripts/zc-echo-amos-6-9.py

Key NT connections:
  6:1   — complacent at ease in Zion → Rev 3:17 (Laodicea)
  6:4-6 — luxurious feasting, not grieving → Luke 16:19-25 (rich man/Lazarus)
  7:2,5 — Amos interceding for small Jacob → Heb 7:25 (Christ intercedes for the weak)
  8:9   — sun goes down at noon, earth darkened → Matt 27:45 (crucifixion darkness)
  8:11  — famine of hearing the word of the LORD → John 6:35 / Rev 22:17
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
    print(f'wrote {p.relative_to(ROOT)}')

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

AMOS_ECHOES = {
  "6": {
    "1": [
      {"type": "allusion", "target": "Rev 3:17", "note": "Woe to those who are complacent in Zion and those who feel secure on the mountain of Samaria — the prophet's woe against the prosperous, self-satisfied elite of Israel is the OT form of Christ's rebuke to Laodicea: you say I am rich and prosperous and need nothing, not knowing that you are wretched and pitiable and poor and blind and naked (Rev 3:17); covenantal ease and complacency are equally fatal in both testaments"},
      {"type": "allusion", "target": "Luke 6:25", "note": "Woe to those at ease... the prominent men of the first nation — Jesus's woes in Luke 6:24-25 (woe to you who are rich / woe to you who are full now) are the NT form of Amos's woe-oracle: the privileged position of being first in the covenant nation (or being wealthy) does not confer safety but increases accountability"}
    ],
    "4": [
      {"type": "allusion", "target": "Luke 16:23", "note": "Who lounge on beds inlaid with ivory and sprawl on their couches, who feast on lambs from the flock and calves from the stall — the portrait of the ruling elite's luxurious feasting while the ruin of Joseph is ignored is the OT form of the rich man in Hades who feasted every day in purple and fine linen while Lazarus lay at his gate (Luke 16:19); both the comfort and the indifference to the suffering of the poor are the structural parallels; the reversal in both cases is exile and torment for the prosperous, rest for the afflicted"}
    ]
  },
  "7": {
    "2": [
      {"type": "allusion", "target": "Heb 7:25", "note": "I said: O Lord GOD, please forgive! How can Jacob stand? For he is so small — Amos intercedes for the vulnerable, small community on the basis of their weakness rather than their merit: they cannot stand; the intercession pleads incapacity, not innocence; Christ's intercession in Hebrews 7:25 (he always lives to make intercession for them) is for those who are likewise too small and weak to stand on their own; the OT prophet interceding for the failing covenant people is a type of the High Priest who intercedes for those who cannot stand without him"}
    ],
    "14": [
      {"type": "allusion", "target": "1 Cor 1:27", "note": "I am not a prophet, nor a prophet's son; I am a herdsman and a dresser of sycamore figs. But the LORD took me from following the flock and the LORD said to me, Go, prophesy to my people Israel — Amos's call bypasses the professional prophetic guilds; he is a layman, a livestock herder and agricultural worker, chosen directly by YHWH; Paul's principle in 1 Cor 1:27-28 (God chose what is low and despised in the world to shame the things that are) is the theological principle behind Amos's commission; the pattern of divine calling overriding human qualifications and institutional credentials runs from Amos through the fishermen-apostles to Paul himself"}
    ]
  },
  "8": {
    "9": [
      {"type": "allusion", "target": "Matt 27:45", "note": "In that day, declares the Lord GOD, I will cause the sun to go down at noon and darken the earth in broad daylight — the cosmic sign of the Day of the LORD as midday darkness; Matthew records that from the sixth hour (noon) there was darkness over all the land until the ninth hour at the crucifixion (Matt 27:45); Luke 23:44-45 specifies the sun's light failed; the darkness at the cross is the Day of the LORD darkness that Amos announces falling upon the one who bore the covenant curse; the 'day of disaster' (Amos 6:3) that Israel dismissed as far away arrives at noon on Good Friday"}
    ],
    "11": [
      {"type": "allusion", "target": "John 6:35", "note": "Behold, the days are coming, declares the Lord GOD, when I will send a famine on the land — not a famine of bread, nor a thirst for water, but of hearing the words of the LORD — the most devastating famine is the withdrawal of the prophetic word; Jesus declares himself the bread of life (John 6:35: I am the bread of life; whoever comes to me shall not hunger, and whoever believes in me shall never thirst) — the reversal of Amos's famine through the one who is himself the living Word; those who reject the word experience the famine; those who receive Christ have the hunger of Amos 8:11 permanently satisfied"},
      {"type": "allusion", "target": "Rev 22:17", "note": "They will wander from sea to sea, and from north to east; they will run to and fro, seeking the word of the LORD, but they will not find it — the desperate wandering in search of the word they had rejected is the OT image of the spiritual homelessness that results from rejecting the prophetic word; Revelation's final invitation (22:17: let the one who is thirsty come; let the one who desires take the water of life without price) is the reversal of Amos's famine-curse: those who come to Christ find what the wanderers of Amos 8:12 could not find"}
    ]
  }
}

def main():
    existing = load_echo('amos')
    merge_echo(existing, AMOS_ECHOES)
    save_echo('amos', existing)
    print('Amos 6–9 echo written.')

if __name__ == '__main__':
    main()
