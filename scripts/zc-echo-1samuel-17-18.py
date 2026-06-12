"""
MKT Echo — 1 Samuel chapters 17–18
Run: python3 scripts/zc-echo-1samuel-17-18.py

Ch 17: David and Goliath — shepherd-warrior defeats the champion of the Philistines.
Ch 18: Jonathan's covenant with David; Saul's jealousy; David's successful rise.

Echo anchors:
- Ch17: shepherd-king pattern; "the battle is YHWH's"; stone/sling vs. armor; giant's head
- Ch18: covenant friendship (Jonathan); Spirit-departure from Saul; jealousy pattern; wisdom/favor
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

ECHOES = {
  "17": {
    "4": [
      {"type": "theme", "target": "Rev 13:5", "note": "Goliath comes out of the Philistine ranks to 'defy' (<em>ḥārap</em>) Israel — the champion's boastful challenge, repeated morning and evening for forty days, is the form that ANE single combat took to resolve inter-tribal conflict. The forty-day defiance and the mouth 'speaking great things' echo the beast's 'mouth uttering haughty and blasphemous words' (Rev 13:5). The Philistine champion as prototype of the final Adversary who challenges the people of God before their champion defeats him."}
    ],
    "26": [
      {"type": "allusion", "target": "John 12:28", "note": "David asks: 'Who is this uncircumcised Philistine, that he should defy the armies of the living God (<em>ʾĕlōhîm ḥayyîm</em>)?' — the name 'living God' as the ground of confidence against an opponent who cannot withstand divine life. Jesus invokes the same logic in John 12:28 ('Father, glorify your name') in the face of the hour of his death — the glory of the living God is what makes the champion undefeatable. David's confidence in YHWH's living power is the OT basis for all NT faith under threat."}
    ],
    "34": [
      {"type": "type", "target": "John 10:11", "note": "David's defense of his shepherd vocation — 'Your servant used to keep sheep for his father. When a lion or a bear came and took a lamb from the flock, I went after it and struck it and delivered the lamb from its mouth' — is the paradigm behind Jesus's self-identification: 'I am the good shepherd. The good shepherd lays down his life for the sheep' (John 10:11). David's risk of life to rescue the lamb from the predator's mouth is the precise OT action-type that the NT fulfills in Christ's incarnation as shepherd-rescuer facing a greater predator."}
    ],
    "45": [
      {"type": "allusion", "target": "Rev 19:11", "note": "David says to Goliath: 'You come against me with sword and spear and javelin, but I come against you in the name of YHWH of hosts (<em>bəšēm YHWH ṣəḇāʾôt</em>), the God of the armies of Israel, whom you have defied.' The contrast between military equipment and YHWH's name is the OT theology of divine warfare that Revelation 19:11 executes eschatologically: the rider on the white horse is called 'Faithful and True' and makes war not with conventional weapons but by the word of God (v13,15). David's unarmed confidence in YHWH's name is the seed of the NT's theology of spiritual warfare."}
    ],
    "47": [
      {"type": "theme", "target": "1 Cor 1:27-28", "note": "'For the battle is YHWH's (<em>kî-laYHWH hammilḥāmāh</em>) and he will give you into our hand' — David's declaration inverts every assumption of power. The stone against armor, the shepherd boy against the military champion, the name of YHWH against iron and bronze: the entire structure of 1 Samuel 17 is the OT paradigm for Paul's 'God chose what is foolish in the world to shame the wise; God chose what is weak in the world to shame the strong' (1 Cor 1:27-28). The cross is the ultimate David-stone against the Goliath of death."}
    ],
    "54": [
      {"type": "allusion", "target": "Gen 3:15", "note": "David cuts off Goliath's head with the giant's own sword — the enemy is destroyed by his own weapon. The seed of the woman crushing the serpent's head (Gen 3:15) finds its first dramatic historical enactment in David's beheading of Goliath. The pattern recurs at the cross: death is defeated by death, the enemy's weapon turned against him. Goliath's severed head carried to Jerusalem anticipates the victor's entry into the holy city with proof of the enemy's defeat."}
    ]
  },
  "18": {
    "1": [
      {"type": "theme", "target": "John 15:13", "note": "Jonathan's soul was knit to David's soul (<em>niqšərāh nepeš-yĕhônātān bənepeš dāwīḏ</em>) and Jonathan loved him as his own soul — the covenant bond formed at David's victory is the OT's deepest human friendship type. Jesus defines its fulfillment: 'Greater love has no one than this, that someone lay down his life for his friends' (John 15:13). Jonathan will repeatedly risk his life and ultimately forfeit his inheritance (the kingship) for David. The Jonathan-David covenant is the historical prototype of the self-sacrificial love Christ embodies and commands."}
    ],
    "3": [
      {"type": "allusion", "target": "Heb 9:15", "note": "Jonathan made a covenant with David (<em>kārat bərît</em>) because he loved him as his own soul — the covenant-cutting (lit. 'cutting' a covenant, from cutting sacrificial animals) that formalizes the David-Jonathan bond. The covenantal love that Jonathan extends to David regardless of Saul's hostility is the OT shadow of the new covenant mediator Christ who cuts the covenant at the cost of his own life: 'He is the mediator of a new covenant' (Heb 9:15). All NT covenant language about the church's union with Christ has the Jonathan-David bond as its OT structural type."}
    ],
    "7": [
      {"type": "allusion", "target": "John 11:48", "note": "'Saul has struck his thousands, and David his ten thousands' — the women's victory song that triggers Saul's murderous jealousy. The pattern of the true deliverer drawing popular acclaim that threatens the established leader is exactly the dynamic the Jerusalem establishment diagnoses in John 11:48: 'If we let him go on like this, everyone will believe in him.' Saul's 'what more can he have but the kingdom?' parallels the Sanhedrin's 'the Romans will come and take away both our place and our nation.' Jealousy of the true king is the response of those whose power he displaces."}
    ],
    "12": [
      {"type": "theme", "target": "Heb 6:4-6", "note": "YHWH was with David but had departed from Saul (<em>YHWH sār mēʿim šāʾûl</em>) — the theological hinge of chapters 16-18. The Spirit that came on Saul (10:6) and made him a new man has departed, replaced by an evil spirit from YHWH (16:14). The divine presence that cannot coexist with persistent covenant rebellion — and whose departure is irrevocable for Saul — is the OT background for Hebrews 6:4-6's warning about those who have tasted the heavenly gift and then fallen away. Saul's story is the warning behind the NT's most severe apostasy text."}
    ],
    "14": [
      {"type": "theme", "target": "Luke 2:52", "note": "David had success in all his undertakings, for YHWH was with him (<em>wayeḥî dāwīḏ maśkîl bəḵol dərāḵāyw wYHWH ʿimmô</em>) — the combination of wisdom-growth and divine favor in the rising king. Luke applies the same pattern to Jesus: 'And Jesus increased in wisdom and in stature and in favor with God and man' (Luke 2:52). The ideal king grows in wisdom and divine favor before his public ministry — David's pattern is fulfilled in Christ's hidden Nazareth years where the same combination of wisdom and divine presence marks the anointed one."}
    ],
    "20": [
      {"type": "theme", "target": "Matt 10:16", "note": "Michal loved David and Saul saw it and used her as a snare against him — Saul sets conditions that expose David to Philistine killing (the hundred foreskins) while appearing to be a bride price. The disciple's life in a hostile world where even domestic relationships become instruments of the enemy's strategy is what Jesus warns about in Matthew 10:16: 'be wise as serpents and innocent as doves.' David must navigate Saul's covert hostility while maintaining covenant faithfulness — the same posture Jesus calls his disciples to in a world where authority becomes adversarial."}
    ],
    "28": [
      {"type": "allusion", "target": "Acts 5:39", "note": "Saul saw and knew that YHWH was with David and that all Israel loved him, and he was even more afraid of David — the recognition that divine favor cannot be defeated by political opposition. Gamaliel's principle in Acts 5:39 — 'you will not be able to overthrow them. You might even be found opposing God!' — is exactly what Saul's fear acknowledges. The more Saul plots against David, the more David prospers. Saul's dread is the dread of one who knows he is fighting against YHWH's anointed and cannot win."}
    ]
  }
}

def main():
    existing = load_echo('1samuel')
    merge_echo(existing, ECHOES)
    save_echo('1samuel', existing)
    print('1samuel ch 17-18: echoes written')

if __name__ == '__main__':
    main()
