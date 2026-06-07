"""
MKT Echo Layer — 2 Timothy chapter 1 (ch2-4 already present; adding ch1)
Run: python3 scripts/zc-echo-2timothy-1-4.py

Key OT connections in ch1:
- v5: multigenerational faith transmission (Deut 6:7; Ps 78:3-6)
- v6: laying on of hands ordination (Num 27:18-23 Joshua type)
- v8: not ashamed / suffering (Isa 50:6-7 Servant songs)
- v9: called with holy calling / predestination (Isa 43:1; Jer 1:5)
- v10: death abolished / immortality (Isa 25:8; Hos 13:14)
- v11: herald/apostle (Isa 40:9; Isa 52:7)
- v12: entrusted deposit / I know whom I believe (Isa 43:10-11; Ps 31:5)
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

ECHOES_2TIM = {
  "1": {
    "5": [
      {"type": "allusion", "target": "Deut 6:7", "note": "Sincere faith which first lived in your grandmother Lois and your mother Eunice — the Deuteronomic command to transmit the faith across generations (teach them diligently to your children, Deut 6:7) finds its personal embodiment in Timothy's family; the multigenerational chain of sincere faith is the lived reality of Moses's instruction"},
      {"type": "allusion", "target": "Ps 78:3-6", "note": "Faith transmitted from grandmother to mother to son — the psalmist's call to tell the next generation the praiseworthy deeds of YHWH (Ps 78:3-6: 'what our ancestors have told us... so the next generation would know them') is the theological framework for multigenerational faith transmission"}
    ],
    "6": [
      {"type": "allusion", "target": "Num 27:18-23", "note": "The gift of God through the laying on of my hands — the ordination of Joshua by Moses (Num 27:18-23: 'Take Joshua son of Nun, a man in whom is the spirit; lay your hand on him') is the foundational OT type for the laying-on-of-hands as a rite of commissioning for ministry succession; Timothy's ordination follows the Mosaic pattern"}
    ],
    "8": [
      {"type": "allusion", "target": "Isa 50:6-7", "note": "Do not be ashamed of the testimony... join me in suffering — the Servant who did not hide his face from shame and spitting (Isa 50:6) and 'set his face like flint' (Isa 50:7) rather than be disgraced is the OT paradigm for the unflinching witness; Paul's call not to be ashamed of chains activates the Servant's shameless suffering as the pattern for Timothy's own public witness"}
    ],
    "9": [
      {"type": "allusion", "target": "Isa 43:1", "note": "Called us with a holy calling... grace given to us in Christ Jesus before the ages began — YHWH's address to Israel 'I have called you by name, you are mine' (Isa 43:1) is the prophetic antecedent for the NT calling language; the gracious, personal, pre-temporal call grounds Paul's election theology in the Servant-Israel calling of Second Isaiah"},
      {"type": "allusion", "target": "Jer 1:5", "note": "Called before the ages began — Jeremiah's prophetic commission 'before you were born I consecrated you; I appointed you a prophet to the nations' (Jer 1:5) is the OT precedent for pre-temporal divine calling; Paul applies this prophetic-calling template to the entire people of God in Christ"}
    ],
    "10": [
      {"type": "allusion", "target": "Isa 25:8", "note": "Who abolished death and brought life and immortality to light — the eschatological promise of Isa 25:8 ('he will swallow up death forever; the Lord GOD will wipe away tears from all faces') is fulfilled in the appearing of Christ Jesus who has destroyed death; the Isaianic abolition of death is the OT ground for the gospel's claim"},
      {"type": "allusion", "target": "Hos 13:14", "note": "Abolished death — Hosea's ransom oracle 'I will ransom them from the power of Sheol; I will redeem them from Death' (Hos 13:14) stands behind the death-abolition language; Paul cites this text explicitly in 1 Cor 15:55, and the same OT ground underlies 2 Tim 1:10"}
    ],
    "11": [
      {"type": "allusion", "target": "Isa 52:7", "note": "Appointed a herald and apostle and teacher of this gospel — the herald of good news whose feet are beautiful on the mountains (Isa 52:7: 'how beautiful are the feet of him who brings good news') is the OT image for the gospel-proclaimer; Paul's self-designation as 'herald' (kēryx) directly echoes the Isaianic herald-figure of the new exodus"},
      {"type": "allusion", "target": "Isa 40:9", "note": "Herald of the gospel — the herald who climbs the mountain to say to the cities of Judah 'Here is your God!' (Isa 40:9) provides the OT commission for the apostolic herald; the herald of the new-exodus good news (Isa 40:9; 52:7) is the prophetic antecedent for Paul's apostolic role"}
    ],
    "12": [
      {"type": "allusion", "target": "Isa 43:10-11", "note": "I know whom I have believed, and I am convinced he is able to guard what I have entrusted — YHWH's declaration 'you are my witnesses... that I am he; before me no god was formed, nor shall there be any after me' (Isa 43:10-11) is the OT ground for the certainty of personal knowledge of God; Paul's 'I know whom I have believed' echoes the witness-testimony language of Second Isaiah"},
      {"type": "allusion", "target": "Ps 31:5", "note": "What I have entrusted to him until that day — the psalmist's 'into your hands I commit my spirit' (Ps 31:5, cited by Jesus on the cross, Luke 23:46) is the OT pattern for the personal deposit of trust; Paul's commitment of his life and ministry to God's keeping follows the same act of entrusting all to the faithful God"}
    ]
  }
}

def main():
    existing = load_echo('2timothy')
    merge_echo(existing, ECHOES_2TIM)
    save_echo('2timothy', existing)

    chs_present = sorted(existing.keys(), key=int)
    print(f'  2 Timothy echo chapters now present: {chs_present}')
    for ch in ['1', '2', '3', '4']:
        count = len(existing.get(ch, {}))
        status = f'{count} verse-entries' if count else 'MISSING'
        print(f'  ch{ch}: {status}')

if __name__ == '__main__':
    main()
