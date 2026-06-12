"""
MKT Echo Layer — Job chapter 42 (Epilogue: restoration)
Run: python3 scripts/zc-echo-job-42-42.py

Ch42: I had heard of you by the ear; now my eye sees you (42:5) — 1 Cor 13:12; Rev 22:4
      God rebukes the friends; Job intercedes for them (42:8) — Heb 10:12; Jas 5:16
      Lord restored Job's fortunes when he prayed for his friends (42:10) — Luke 6:28; Phil 2:9
      The Lord blessed the latter days of Job more than his beginning (42:12) — 2 Cor 4:17; Rev 21:4
      Job died old and full of days (42:17) — Heb 11:10; 2 Tim 4:7-8
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
  "42": {
    "5": [
      {"type": "allusion", "target": "1 Cor 13:12", "note": "I had heard of you by the hearing of the ear, but now my eye sees you — Job's confession at the theophany: the difference between secondhand report and direct vision. 1 Corinthians 13:12: 'For now we see in a mirror dimly, but then face to face. Now I know in part; then I shall know fully, even as I have been fully known.' Job's movement from hearing to seeing is the OT's most compressed form of Paul's now/then contrast. The ear-hearing (covenant tradition, secondhand report, the friends' theological categories) is not false, but it is incomplete; the face-to-face vision that Job suddenly receives is the eschatological mode of knowing that Paul places at the parousia. The cross-and-resurrection transforms hearing-faith toward its consummation in sight."},
      {"type": "allusion", "target": "Rev 22:4", "note": "Now my eye sees you — Job's direct vision of God, granted in the whirlwind. Revelation 22:4: 'They will see his face, and his name will be on their foreheads.' The beatific vision Job experiences as a preview — direct, overwhelming sight of the divine — is the permanent state of the redeemed in the new creation. Job's theophany is a temporal intrusion of what is permanently true of the eschaton; Revelation 22 is the full realization of what Job glimpsed in the whirlwind. Between the two stands the incarnation: Christ is the face of God made visible (John 14:9; 2 Cor 4:6) so that seeing him is already, in a transformed sense, seeing God."}
    ],
    "7": [
      {"type": "allusion", "target": "Jas 5:11", "note": "God rebukes Eliphaz and the friends: you have not spoken of me what is right, as my servant Job has — the divine verdict that reverses the trial's apparent outcome. James 5:11: 'You have heard of the steadfastness of Job, and you have seen the purpose of the Lord, how the Lord is compassionate and merciful.' James uses Job precisely here — the outcome of the story: the purpose of the Lord (to kelos Kyriou) is the compassionate and merciful restoration after the suffering. The very point at which God vindicates Job (saying the friends spoke wrongly) is the point James cites as the revelation of divine character: the God who appeared to be Job's adversary proves to be the God of compassion."}
    ],
    "8": [
      {"type": "allusion", "target": "Heb 10:12", "note": "Now therefore take seven bulls and seven rams and go to my servant Job and offer up a burnt offering for yourselves. And my servant Job shall pray for you, for I will accept his prayer not to deal with you according to your folly. The structure here is striking: the burnt offering alone is not sufficient — Job's intercession is also required. Hebrews 10:12: 'But when Christ had offered for all time a single sacrifice for sins, he sat down at the right hand of God.' The Job epilogue pattern — sacrifice plus ongoing intercession by the vindicated sufferer — is fulfilled in Christ: the single sacrifice offered, and the perpetual intercession of the risen priest. Job's priestly intercession for his accusers foreshadows the intercession of the one who said 'Father, forgive them' (Luke 23:34)."},
      {"type": "allusion", "target": "Jas 5:16", "note": "My servant Job shall pray for you, for I will accept his prayer — the prayer of the righteous sufferer on behalf of those who wronged him is what God requires and accepts. James 5:16: 'The prayer of a righteous person has great power as it is working.' James immediately proceeds to cite Elijah (5:17), but the deeper OT background is Job: the righteous person whose prayer God accepts is the one who has been vindicated by suffering, not the one who maintained conventional piety throughout. The gospel expands this: Christ's righteousness, not our own, is the ground of the acceptability of prayer — we pray in his name (John 16:24), covered by the intercession of the one whose prayer God unfailingly accepts."}
    ],
    "10": [
      {"type": "allusion", "target": "Luke 6:28", "note": "The Lord restored the fortunes of Job when he had prayed for his friends — the restoration is temporally linked to the intercession for his accusers. Luke 6:28: 'bless those who curse you, pray for those who abuse you.' Job's praying for those who wronged him — who accused him falsely, who added condemnation to suffering, who compounded his affliction with theological abuse — is the OT embodiment of what Jesus commands in the Sermon on the Plain. The pattern is: suffer unjustly, maintain integrity, pray for accusers, be restored. It is the pattern of Christ's own passion and intercession."},
      {"type": "allusion", "target": "Phil 2:9", "note": "The Lord restored the fortunes of Job when he prayed for his friends — the humiliated one is exalted, the stripped one is restored, the vindicated sufferer receives back double. Philippians 2:9: 'Therefore God has highly exalted him and bestowed on him the name that is above every name.' The humiliation-to-exaltation arc is the structural pattern both texts share: the one who descended to the lowest point (Phil 2:7-8: slave, death, cross; Job: boils, ash heap, abandonment) is the one whom God exalts decisively. The restoration of Job's fortunes is the OT's narrative form of the exaltation that Paul describes as the Father's response to the Son's complete humiliation."}
    ],
    "12": [
      {"type": "allusion", "target": "2 Cor 4:17", "note": "The Lord blessed the latter days of Job more than his beginning — the end-state exceeds the starting point; the restoration is not merely a return to zero but an advance beyond it. 2 Corinthians 4:17: 'For this light momentary affliction is preparing for us an eternal weight of glory beyond all comparison.' Paul's logic of affliction-to-glory is the theological generalization of the Job pattern: the suffering is real and severe, but the weight of what it prepares exceeds it immeasurably. Job's 'beginning' was itself blessed; his 'latter' doubles it. The eschatological glory the gospel promises is not the restoration of Eden but its surpassment — exactly as Job's restoration surpasses his original condition."},
      {"type": "allusion", "target": "Rev 21:4", "note": "The latter days of Job exceeded his beginning — the endpoint of his story is greater than its starting point. Revelation 21:4: 'He will wipe away every tear from their eyes, and death shall be no more, neither shall there be mourning, nor crying, nor pain anymore, for the former things have passed away.' The 'former things' of Revelation 21 correspond to Job's losses; the new creation that replaces them exceeds them as Job's latter days exceeded his beginning. The restored creation does not return the old order but introduces the new — a world where the former sufferings are not merely compensated but surpassed by a glory that makes comparison impossible."}
    ],
    "17": [
      {"type": "allusion", "target": "Heb 11:10", "note": "Job died old and full of days — the climax of the restoration narrative. In the context of the whole book, this ending is the answer to Job's Sheol-focused despair: the man who cried that his days were extinct (17:1), who anticipated only darkness and the pit, dies instead full of years and surrounded by family. Hebrews 11:10, of Abraham: 'he was looking forward to the city that has foundations, whose designer and builder is God.' Both patriarchs live the full span given them and die in the faith of a hope not yet fully realized — Job ends his story without the resurrection that his redeemer-confession (19:25) points toward; the city Hebrews describes is still ahead. The fullness of days is a partial fulfillment; the complete fulfillment is beyond the grave."},
      {"type": "allusion", "target": "2 Tim 4:7", "note": "Job died old and full of days — the life completed, the course run. 2 Timothy 4:7-8: 'I have fought the good fight, I have finished the race, I have kept the faith. Henceforth there is laid up for me the crown of righteousness.' The 'full of days' with which Job's story closes and the 'I have kept the faith' with which Paul's closes are structurally equivalent: a life of integrity maintained through suffering, brought to its appointed end. Paul explicitly awaits the crown that his having-finished the race makes available; Job's story ends before that eschatological horizon is fully disclosed — but both narratives end with the sufferer at peace, having been found faithful, awaiting what the resurrection makes available."}
    ]
  }
}

def main():
    e = load_echo('job')
    merge_echo(e, ECHOES)
    save_echo('job', e)
    count = sum(len(v) for v in ECHOES.values())
    print(f'job echo: wrote entries for {count} verses in ch 42')

if __name__ == '__main__':
    main()
