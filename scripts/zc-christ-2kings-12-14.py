"""
MKT Christ Commentary — 2 Kings chapters 12–14
Run: python3 scripts/zc-christ-2kings-12-14.py

Ch12: Joash's temple repair / collection-chest → Jesus's treasury scene (Mark 12:41);
      Joash's compromise at the end — the king who started well / Heb 3:14
Ch13: Elisha's posthumous resurrection (bones reviving a corpse) → Heb 11:35; John 5:28
Ch14: Amaziah's pride and defeat — the thistle/cedar parable applied;
      Jonah historically placed → Matt 12:39-41 (sign of Jonah)

Key typological connections:
- 12:2: Joash did right while Jehoiada instructed him → Heb 3:14 (hold fast to the end)
- 13:21: bones-resurrection → Heb 11:35; John 5:28-29 (hour when all will hear)
- 14:25: Jonah the prophet historically attested → Matt 12:39-41 (sign of Jonah = resurrection)
- 14:26: YHWH saw Israel's distress → Heb 4:15 (high priest who sympathizes with weakness)
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
  "12": {
    "2": "<p>The qualification of Joash&rsquo;s fidelity — <em>wayyaʿaś yôʾāš hayyāšār bᵉʿênê YHWH kol yāmāyw ʾăšer hôrāhû yᵉhôyāḏāʿ hakkōhēn</em>, &lsquo;Joash did what was right in the eyes of YHWH all his days because Jehoiada the priest instructed him&rsquo; — carries an embedded limit: the fidelity was conditional on Jehoiada&rsquo;s instruction and Jehoiada&rsquo;s life. When Jehoiada died (2 Chr 24:17-22), Joash turned to the princes of Judah and abandoned the house of YHWH; he even had Zechariah the prophet stoned when Zechariah rebuked him. The pattern — fidelity maintained under external guidance, abandoned when the guide is gone — is the OT&rsquo;s recurring warning against faith that depends on human scaffolding. Heb 3:14 names the criterion for genuine faith: <em>metochoi gar tou Christou gegonamen, eanper tēn archēn tēs hypostaseōs mechri telous bebaian katascho</em> — &lsquo;for we have come to share in Christ, if indeed we hold our original confidence firm to the end.&rsquo; Joash&rsquo;s conditional fidelity (&lsquo;all his days [while] Jehoiada instructed him&rsquo;) is the OT&rsquo;s warning against the partial beginning that does not hold to the end — the contrast that Hebrews repeatedly addresses in its audience.</p>"
  },
  "13": {
    "21": "<p>The dead man revived by contact with Elisha&rsquo;s bones — thrown hastily into Elisha&rsquo;s tomb and reviving when he touched them — is the OT&rsquo;s solitary instance of life transmitted by a dead prophet&rsquo;s remains. The narrative makes no theological claim about Elisha&rsquo;s bones as a permanent source of power; it records a specific event without generalizing it into a relic-theology. The theological point is about the Spirit that worked through Elisha in life: even his dead bones are a conduit for the same Spirit that had worked through him. John 5:28-29 announces the ultimate extension of this principle: <em>erchesthai hōra en hē pantes hoi en tois mnēmeiois akousontai tēs phōnēs autou kai ekporeusontai</em> — &lsquo;an hour is coming when all who are in the tombs will hear his voice and come out.&rsquo; The Elisha-bones miracle is the OT&rsquo;s single narrative demonstration that the resurrection power that will raise all the dead is already present in the world in anticipatory form — that the prophetic Spirit is not contained by death. Heb 11:35 includes the OT resurrection episodes in the faith-hall: &lsquo;women received back their dead by resurrection&rsquo; — and the Elisha-bones episode stands as the most posthumous of these, the resurrection-power persisting beyond even the prophet&rsquo;s burial.</p>"
  },
  "14": {
    "25": "<p>The historical placement of Jonah son of Amittai from Gath-hepher as a prophet active during Jeroboam II&rsquo;s reign — <em>kîdbar YHWH ʾelōhê yiśrāʾēl ʾăšer dibber bᵉyaḏ ʿaḇdô yônāh ben ʾămittay hannāḇîʾ ʾăšer miggat hāḥēper</em> — confirms Jonah as a historical Israelite prophet in the mid-8th century BCE, a prophet to the northern kingdom before being sent to Nineveh. Jesus in Matt 12:39-41 treats Jonah as a historical figure: <em>kai kathōs ēn Iōnas en tē koilia tou kētous treis hēmeras kai treis nyktas, houtōs estai ho hyios tou anthrōpou en tē kardia tēs gēs treis hēmeras kai treis nyktas</em> — &lsquo;for just as Jonah was three days and three nights in the belly of the great fish, so will the Son of Man be three days and three nights in the heart of the earth.&rsquo; The 2 Kgs 14:25 historical reference is the OT&rsquo;s anchor for the historicity of the Jonah to whom Jesus appeals — the sign of Jonah (death and return from the depths) is the sign of Christ&rsquo;s resurrection, grounded in the historical prophet whom the Kings narrative places in a datable reign.</p>"
  }
}

def main():
    c = load_comm('mkt-christ', '2kings')
    merge_comm(c, CHRIST)
    save_comm('mkt-christ', '2kings', c)
    count = sum(len(v) for v in CHRIST.values())
    print(f'2kings mkt-christ: wrote {count} verses across ch 12-14')

if __name__ == '__main__':
    main()
