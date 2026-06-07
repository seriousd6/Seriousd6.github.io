"""
mkt-christ layer — 1 Peter chapter 5 (all 14 verses)
Output: data/commentary/mkt-christ/1peter.json
Run: python3 scripts/zc-christ-1peter-5-5-full.py

Interpretation decisions:
- The 'Chief Shepherd' (archipoimenos, v4) is Christ at his parousia — the same one
  whose sufferings Peter witnessed (v1); the elder-shepherd pattern mirrors Christ's own
  shepherd-identity (John 10:11; Heb 13:20).
- 'God's mighty hand' (v6) echoes the Exodus formula and is fulfilled in Christ's own
  exaltation (Acts 2:33: exalted to the right hand of God).
- The devil as roaring lion (v8) is defeated by the same resurrection-power that raised
  Christ (Col 2:15: disarmed the powers at the cross).
"""
import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_comm(source, book):
    p = ROOT / 'data' / 'commentary' / source / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_comm(source, book, data):
    p = ROOT / 'data' / 'commentary' / source / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_comm(existing, new_data):
    # INTENT: Merge new verse entries without overwriting already-present keys — safe to re-run.
    # CHANGE? If commentary JSON structure changes from {ch:{v:html}}, update this traversal.
    # VERIFY: Re-running the script should produce identical output.
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

NEW_DATA = {
  "5": {
    "1": "<p>Peter appeals as a 'fellow elder and a witness of Christ's sufferings' — the eyewitness credential is Christological: Peter was present at Gethsemane, the arrest, the trials, and (at a distance) the crucifixion. His personal witness of Christ's passion is the Christological ground for everything he is about to command the elders. Those who watched the Shepherd suffer now shepherd his flock; the elders' authority is derivative from the suffering Christ's authority over the sheep he purchased with his own blood (Acts 20:28: the church of God, which he obtained with his own blood).</p>",
    "2": "<p>'Be shepherds of God's flock' — the shepherd-title was applied to God in Israel's tradition (Ps 23:1; Isa 40:11; Ezek 34:11-16) and to Christ by Jesus himself (John 10:11: I am the good shepherd; John 10:14-15) and by other NT writers (Heb 13:20: the great Shepherd of the sheep; Rev 7:17: the Lamb will be their shepherd). Elders who shepherd are participating in Christ's own shepherding role — not replacing him but extending his care under his authority. The willing service rather than compelled service mirrors Christ's own voluntary self-giving (John 10:18: no one takes my life from me, I lay it down of my own accord).</p>",
    "3": "<p>'Being examples (<em>typoi</em>) to the flock' — the Christological model of leading by embodiment: Christ himself is the <em>typos</em> (pattern, example) that both Peter and the elders trace. Peter explicitly calls Christ the exemplar in 2:21 (leaving you an example that you should follow in his steps). The chain: Christ gave himself as the pattern → Peter traces that pattern as apostle → elders trace it in their communities → the flock traces it in their lives. The non-domination is part of the pattern: Christ who had all authority washed feet (John 13:14-15: I have set you an example).</p>",
    "4": "<p>'When the Chief Shepherd (<em>archipoimenos</em>) appears, you will receive the crown of glory' — the parousia of Christ as the Chief Shepherd is the Christological horizon that frames all human shepherding. The elders' service will be evaluated by the one who is himself the supreme Shepherd. Christ's description of himself as the good shepherd who knows his sheep and gives his life for them (John 10:14-15) provides the qualitative standard: the Chief Shepherd who sacrificed himself will recognize and reward the under-shepherds who served with the same self-giving pattern. The unfading crown of glory contrasts with the fading civic crowns that a Roman provincial elder might covet.</p>",
    "5": "<p>'Clothe yourselves with humility toward one another, because God opposes the proud but shows favor to the humble' (Prov 3:34) — the humility that Peter commands is the garment that Christ himself wore at the Last Supper: he took off his outer garment, tied a towel around himself, and washed the disciples' feet (John 13:4-5). The clothing metaphor is the same: Christ 'clothed himself' with humility in the most literal act of servant-lowering. Peter's command to 'clothe yourselves with humility' is the Christological imperative to put on the disposition that Christ embodied — the Phil 2:5-8 pattern of self-emptying in the form of a servant.</p>",
    "6": "<p>'Humble yourselves under God's mighty hand, that he may lift you up in due time' — the humbling-and-exaltation pattern is the Christ-pattern that Peter has invoked throughout the letter: Christ suffered, was put to death, was raised, and was exalted to God's right hand (3:18-22). The 'mighty hand of God' (<em>krataia cheir</em>) that believers are to humble themselves under is the same hand that exalted Christ (Acts 2:33: exalted to the right hand of God). Humbling oneself under God's mighty hand is submitting to the same divine hand that raised Christ from the dead — trusting that the same exaltation pattern will be repeated for those who follow Christ's humiliation path.</p>",
    "7": "<p>'Cast all your anxiety on him because he cares for you' — the Christological ground of the casting: the God who cares for the community demonstrated the ultimate form of care in sending his Son (Rom 8:32: he who did not spare his own Son but gave him up for us all, how will he not also give us all things with him?). The anxiety-casting is not a technique but a theological act of trust grounded in the cross: if God cared enough to give Christ, he cares about everything the community is anxious about. Christ's own teaching on anxiety (Matt 6:25-34: do not be anxious) is the Christological form of the same assurance.</p>",
    "8": "<p>'Your enemy the devil prowls around like a roaring lion looking for someone to devour' — the devil who opposes the community is the same adversary who sought to destroy Christ (Matt 4:1-11: the temptation; John 13:2: the devil prompted Judas; 14:30: the prince of this world is coming). The community's vulnerability to demonic attack is the Christological participation: as Christ was attacked by the devil and the powers, so his community is attacked. The Christological resource for resistance: Christ has already defeated the devil through the cross (Col 2:15: he disarmed the rulers and authorities and put them to open shame by triumphing over them in him; Heb 2:14: that through death he might destroy the one who has the power of death, that is, the devil).</p>",
    "9": "<p>'Resist him, standing firm in the faith, because you know that the family of believers throughout the world is undergoing the same kind of sufferings' — the resistance of the devil is the Christ-pattern applied communally. Christ resisted the devil in the wilderness through the word of God (Matt 4:4, 7, 10: it is written). The community that 'stands firm in the faith' — in the Christological proclamation — is using the same weapon. The worldwide solidarity of suffering communities is a Christological reality: the one body of Christ (1 Cor 12:26: if one part suffers, every part suffers with it) means the suffering is shared not only horizontally but in the body of the Christ who suffered first.</p>",
    "10": "<p>'And the God of all grace, who called you to his eternal glory in Christ, after you have suffered a little while, will himself restore you and make you strong, firm, and steadfast' — the calling 'to his eternal glory in Christ' is the eschatological goal: participation in the glory of Christ who has already entered into his eternal glory through the resurrection (John 17:5: glorify me in your own presence with the glory I had with you before the world existed). The four acts of God (restore, make strong, firm, steadfast) are the acts of the one who raised Christ from the dead (Rom 4:24; 1 Cor 15:15) — the same power applied to the community through their 'little while' of suffering.</p>",
    "11": "<p>'To him be the power for ever and ever. Amen' — the doxology to God is a Christological act: the praise offered to God is offered to the God known through Christ, the God who has acted in the Christ-event. The 'power' (<em>kratos</em>) for which God is praised is the resurrection-power that Peter has described throughout the letter: the power that raised Christ from the dead (1:3), that brought salvation to completion in the last times (1:5, 20), that overcame the imprisoned spirits and cosmic powers (3:18-22), and that will ultimately restore the suffering community (5:10). The Amen is the community's ratification of the entire Christological claim.</p>",
    "12": "<p>'I have written to you briefly, encouraging you and testifying that this is the true grace of God. Stand fast in it' — the letter's summary: 'the true grace of God' (<em>alēthinēn charin tou theou</em>) is the entire Christological proclamation that Peter has set forth — the new birth through Christ's resurrection (1:3), the redemption by Christ's blood (1:18-19), the living stone and cornerstone (2:4-8), the Christ-suffering pattern (2:21-25; 3:18-22), the eschatological glory (4:13; 5:4, 10). To 'stand fast in it' is to stand fast in Christ — the one in whom the grace of God has definitively appeared and acted.</p>",
    "13": "<p>'She who is in Babylon, chosen together with you, sends you greetings, and so does my son Mark' — the 'co-elect' Roman community (Babylon) and Peter's son Mark are gathered under the Christological identity 'in Christ' (v. 14: peace to all who are in Christ). Mark, who once deserted Paul's missionary journey (Acts 13:13) and later was reconciled (2 Tim 4:11), represents the grace of Christ that restores the failing disciple and reintegrates him into apostolic mission. The same grace that Peter experienced in his own restoration after the denial (John 21:15-17) is the grace that restored Mark. The Petrine-Mark connection is the living evidence that the suffering-restoration pattern is real.</p>",
    "14": "<p>'Greet one another with a kiss of love. Peace to all of you who are in Christ' — the closing benediction is Christological location: 'those who are in Christ' (<em>tois en Christō</em>) are those whose identity, security, and future are determined by their union with the risen Lord. The 'peace' (<em>eirēnē</em>) that Peter pronounces is not merely a social wish but the Christological peace — the peace Christ made through the blood of his cross (Col 1:20), the peace that surpasses understanding (Phil 4:7), the peace that Christ gave as his legacy (John 14:27: my peace I give to you). The letter that began with the Trinitarian election of the scattered exiles ends with all those exiles located 'in Christ' — their home is not in any province of the Roman empire but in the risen Lord."
  }
}

if __name__ == '__main__':
    existing = load_comm('mkt-christ', '1peter')
    merge_comm(existing, NEW_DATA)
    save_comm('mkt-christ', '1peter', existing)
    import json as _json
    il = _json.load(open(ROOT / 'data' / 'interlinear' / '1peter.json'))
    all_ok = True
    for ch in ['5']:
        missing = set(il.get(ch, {}).keys()) - set(existing.get(ch, {}).keys())
        if missing:
            print(f'  ch {ch} STILL MISSING: {sorted(missing, key=int)}')
            all_ok = False
        else:
            print(f'  ch {ch}: complete ({len(existing.get(ch, {}))} verses)')
    if all_ok:
        print('All verses present')
