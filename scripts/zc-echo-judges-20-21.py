"""
MKT Echo — Judges chapters 20–21
Run: python3 scripts/zc-echo-judges-20-21.py

Ch 20: The civil war against Benjamin — Israel assembles at Mizpah, three battles,
       Gibeah destroyed. Echo anchors: communal assembly/lament, purging evil,
       Phinehas interceding, YHWH's delayed victory, remnant preservation.
Ch 21: Aftermath — Israel's oath crisis, wives for Benjamin. Already has v25.
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

JUDGES_ECHOES = {
  "20": {
    "1": [
      {"type": "theme", "target": "Acts 1:14", "note": "All the children of Israel came out as one man (ke-ish echad) to Mizpah — the phrase marks unanimous communal solidarity in response to crisis. The apostles likewise gathered with one accord (homothumadon) before Pentecost; corporate unity in the face of moral catastrophe is a pattern from Judges forward."}
    ],
    "2": [
      {"type": "allusion", "target": "Heb 12:23", "note": "The chief of all the people presented themselves in the assembly (qahal) of the people of God — the full national assembly before YHWH anticipates the NT's vision of the ecclesia, the assembly of the firstborn enrolled in heaven (Heb 12:23). The OT qahal is the model from which NT ekklesia draws both its vocabulary and its covenantal logic."}
    ],
    "13": [
      {"type": "allusion", "target": "1 Cor 5:13", "note": "Deliver up the men, the worthless fellows (bene-beliyya'al) in Gibeah, that we may put them to death and purge (ba'ar) the evil from Israel — this formula, repeated from Deuteronomy, is the direct background for Paul's command to expel the sexually immoral man from the Corinthian church. Paul quotes the Deuteronomic 'purge the evil from among you' formula (Deut 17:7) in 1 Cor 5:13, applying the same principle of communal holiness."}
    ],
    "18": [
      {"type": "allusion", "target": "Rev 5:5", "note": "Which of us shall go up first to fight against the people of Benjamin? YHWH answers: Judah shall go up first — Judah's primacy in battle echoes the Davidic-messianic trajectory; the Lion of the tribe of Judah who alone opens the seals (Rev 5:5) is the ultimate fulfillment of Judah's appointed role as the first to go up in holy war."}
    ],
    "23": [
      {"type": "theme", "target": "Heb 4:16", "note": "Israel went up and wept before YHWH until evening after their first crushing defeat, asking: Shall we again draw near to fight? — this pattern of seeking YHWH in the moment of utter defeat and receiving renewed divine commission is the OT grounding of the NT call to draw near to the throne of grace with confidence even in weakness (Heb 4:16)."}
    ],
    "26": [
      {"type": "allusion", "target": "Joel 2:12", "note": "All the people of Israel went up to Bethel and wept, fasting that day until evening, and offered burnt offerings and peace offerings before YHWH — the triple action of weeping, fasting, and sacrifice before YHWH in the context of communal disaster is the pattern Joel calls Israel to in the face of the Day of YHWH: return to me with fasting, with weeping, and with mourning (Joel 2:12)."}
    ],
    "28": [
      {"type": "type", "target": "Heb 7:25", "note": "Phinehas the son of Eleazar, son of Aaron, ministered before the ark of the covenant of YHWH, asking: Shall I yet again go out to battle? — Phinehas as the interceding high priest standing before YHWH on behalf of the people is a structural type of Christ's permanent high-priestly intercession. Phinehas's intercession was remembered as atonement (Ps 106:30-31); Christ's is eternal (Heb 7:25)."}
    ],
    "35": [
      {"type": "theme", "target": "Rom 11:5", "note": "YHWH defeated Benjamin before Israel — the near-annihilation of an entire tribe, with only 600 surviving (v47), and the subsequent crisis over Israel's integrity as twelve tribes, prefigures the remnant theology that Paul applies to unbelieving Israel: even in judgment God preserves a remnant (Rom 11:5), and the apparent rupture within the people of God does not undo the covenant."}
    ],
    "48": [
      {"type": "allusion", "target": "Rev 18:8", "note": "The men of Israel turned back against the people of Benjamin and struck them with the sword — the entire city of Gibeah put to fire (v40) and all Benjamin's towns burned (v48). This total destruction of an Israelite city that had become like Sodom (Gen 18:20 → Judg 19:22) is the OT pattern behind Revelation's depiction of Babylon's sudden destruction by fire (Rev 18:8): in a single day her plagues will come."}
    ]
  },
  "21": {
    "3": [
      {"type": "theme", "target": "Rom 11:1", "note": "Why has this happened in Israel, that today one tribe should be lacking in Israel? — Israel's grief over the near-extinction of Benjamin reflects the covenant theology that no tribe can simply be lost; the wholeness of the twelve-tribe structure belongs to YHWH's promises. Paul's anguish over unbelieving Israel (Rom 11:1) stands in the same tradition: Has God rejected his people? By no means."}
    ],
    "15": [
      {"type": "theme", "target": "Luke 15:24", "note": "The people had compassion on Benjamin because YHWH had made a breach in the tribes of Israel — the grief over a tribe brought low and the effort to restore them resonates with the parable of the lost son: he was dead and is alive again, lost and is found (Luke 15:24). The instinct to restore the broken and preserve the whole belongs to YHWH's character and is ultimately expressed in the gospel."}
    ]
  }
}

def main():
    existing = load_echo('judges')
    merge_echo(existing, JUDGES_ECHOES)
    save_echo('judges', existing)
    print('judges ch 20-21: echoes written')

if __name__ == '__main__':
    main()
