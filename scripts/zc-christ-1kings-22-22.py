"""
MKT Christ Commentary — 1 Kings chapter 22
Run: python3 scripts/zc-christ-1kings-22-22.py

Ch22: Micaiah ben Imlah — the true prophet who speaks only what YHWH says / John 12:49-50;
      the lying spirit / YHWH's sovereignty over false prophecy / 2 Thess 2:11;
      Ahab's death in disguise — the divine decree fulfilled despite evasion / Acts 2:23;
      Jehoshaphat's cry and YHWH's turning away wrath — intercession type

Key typological connections:
- 22:14: Micaiah speaks only what YHWH says → John 12:49-50 (the Son speaks only the Father's words)
- 22:28: 'If you return in peace, YHWH has not spoken by me' → John 16:33 / the vindicated prophet
- 22:34: random arrow finds the gap in armor → Acts 2:23 (crucifixion by definite plan / foreknowledge)
- 22:47: Jehoshaphat's cry / YHWH's mercy → Heb 5:7 (Christ's cry heard; divine mercy in extremity)
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_comm(layer, book):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_comm(layer, book, data):
    p = ROOT / 'data' / 'commentary' / layer / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_comm(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

CHRIST = {
  "22": {
    "14": "<p>Micaiah&rsquo;s declaration to Ahab&rsquo;s messenger — <em>ḥay YHWH kî ʾet ʾăšer yōmar ʾēlay YHWH ʾōtô ʾăḏabbēr</em>, &lsquo;as YHWH lives, what YHWH says to me, that I will speak&rsquo; — is the paradigmatic prophetic commission: the true prophet speaks only what he receives from YHWH, not what the audience wants to hear. Jesus in John 12:49-50 names the same principle as the ground of his own teaching: <em>hoti egō ex emautou ouk elalēsa, all&rsquo; ho pempsas me patēr autos moi entolēn dedōken ti eipō kai ti lalēsō</em> — &lsquo;for I have not spoken on my own authority, but the Father who sent me has himself given me a commandment — what to say and what to speak.&rsquo; The obedient prophet who speaks only what he is given stands against the court prophets who speak what the king wants. Micaiah&rsquo;s willingness to deliver a death-oracle against the king who imprisons him (v27) is the OT&rsquo;s type of the prophetic courage that costs everything. Jesus faces the same structure in reverse: his speaking the Father&rsquo;s words — including the temple-destruction oracle, the judgment on Jerusalem, the resurrection prediction — is what generates the pressure that leads to the cross. The true prophet speaks truthfully into hostile power; the cost is identical across both testaments.</p>",
    "34": "<p>The random arrow that finds the disguised Ahab — <em>wᵉʾîš māšaḵ baqqešet lᵉtummô wayyakkeh ʾet melek yiśrāʾēl bên haḏḏᵉḇāqîm ûḇên hašširyān</em>, &lsquo;a certain man drew his bow at random and struck the king of Israel between the scale armor and the breastplate&rsquo; — is the narrative&rsquo;s densest theological moment: divine decree fulfilled through an act directed at no particular target. The archer aimed at no one; the arrow found the one man whose death had been decreed in the divine council (v19-23). Acts 2:23 articulates the same structure in the passion: <em>touton tē hōrismenē boulē kai prognōsei tou theou ekdoton dia cheiros anomōn prosēxantes aneilate</em> — &lsquo;this Jesus, delivered up according to the definite plan and foreknowledge of God, you crucified and killed by the hands of lawless men.&rsquo; The crucifixion — executed by Roman soldiers following a Jewish council&rsquo;s political pressure, driven by fear, expediency, and betrayal — was, from below, a concatenation of human agents pursuing their own ends; from above, the definite plan of the divine council. Ahab&rsquo;s disguise failed to nullify the decree; the cosmic powers that crucified Christ (1 Cor 2:8) did not know they were fulfilling it.</p>"
  }
}

def main():
    c = load_comm('mkt-christ', '1kings')
    merge_comm(c, CHRIST)
    save_comm('mkt-christ', '1kings', c)
    count = sum(len(v) for v in CHRIST.values())
    print(f'1kings mkt-christ: wrote {count} verses across ch 22')

if __name__ == '__main__':
    main()
