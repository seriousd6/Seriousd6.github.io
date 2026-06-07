"""
MKT Christ Commentary — 3 John ch1
13 missing verses (v7 already present)
Run: python3 scripts/zc-christ-3john-1-1.py

Christological threads:
- "The truth" throughout the letter = Christological truth (John 14:6: "I am the truth")
- Gaius's hospitality to missionaries = receiving Christ (Matt 25:35; John 13:20)
- Diotrephes's philoproteuo contrasts with Christ's self-emptying (Phil 2:6-7)
- "The truth itself" bearing witness to Demetrius (v12) — personalized truth = Christ
- Peace benediction as risen Christ's greeting (John 20:19, 21, 26)
- Greeting by name echoes the Shepherd who calls his own by name (John 10:3)
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
    """Merge new_data into existing without overwriting present entries."""
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

CHRIST = {
  "1": {
    "1": '<p>The elder loves Gaius "in the truth" (<em>en alētheia</em>) — in Johannine usage, truth is not merely factual accuracy but the personal reality of Christ himself: "I am the way, the truth, and the life" (John 14:6). Love "in the truth" is love shaped, bounded, and motivated by the Christological reality that the elder and Gaius share. It is the same formulation as 2 John 1 ("whom I love in truth") and points to the same christocentric foundation: the elder\'s pastoral bond with Gaius exists within the person of Christ who is the Truth.</p>',
    "2": '<p>"I pray that you may enjoy good health and that all may go well with you, even as your soul is getting along well" — the health-prayer presupposes a holistic anthropology that resists the Docetic dualism the letter implicitly opposes. The missionaries denied in v7 (who go out "for the Name") have real bodies that need real hospitality; the Gaius who "walks in truth" has a soul and a body that both flourish. The incarnation validates bodily well-being as a legitimate prayer-concern: the Word who became flesh (John 1:14) sanctifies embodied existence as a category worthy of God\'s care.</p>',
    "3": '<p>"When some believers came and testified about your faithfulness to the truth" — the word for "testified" (<em>emartyresan</em>) is the Johannine witness-vocabulary that runs through the Gospel and Epistles of John (John 1:7-8; 5:31-39; 1 John 5:9-11). In Johannine thought, witness ultimately traces back to Christ, the faithful witness (<em>ho martys ho pistos</em>, Rev 1:5). Gaius\'s faithfulness to the truth is itself a form of witness, and those who testify to it participate in the same chain of testimony that began with the Son\'s witness to the Father.</p>',
    "4": '<p>"I have no greater joy than to hear that my children are walking in the truth" — the elder\'s joy mirrors Christ\'s own joy in the faithfulness of his disciples: "I have told you this so that my joy may be in you and that your joy may be complete" (John 15:11). To "walk in truth" is to live with Christ as both path and companion (John 14:6: "I am the way"). The father-child metaphor for the pastoral relationship (Paul uses it too: 1 Cor 4:15; Gal 4:19) reflects the new-family structure of the church grounded in the Father-Son relationship of the Trinity.</p>',
    "5": '<p>"You are faithful in what you are doing for the brothers and sisters, even though they are strangers to you" — receiving strangers in Christ\'s name is receiving Christ himself: "I was a stranger and you welcomed me... whatever you did for one of the least of these brothers and sisters of mine, you did for me" (Matt 25:35, 40). The missionaries Gaius hosts travel "for the sake of the Name" (v7); to receive them is to receive the Name they carry. Hospitality to Christian workers is not merely social generosity but a Christological act — the host participates in the mission by receiving its agents.</p>',
    "6": '<p>"Please send them on their way in a manner that honors God (<em>axios tou theou</em>)" — the phrase <em>axios tou theou</em> (worthy of God) is the Pauline standard for Christian conduct: "live a life worthy of God, who calls you into his kingdom and glory" (1 Thess 2:12). The missionary sending that Gaius is asked to facilitate mirrors Christ\'s own commissioning: "As the Father has sent me, even so I am sending you" (John 20:21). To send missionaries "worthily of God" is to extend the chain of sending that originates in the Father\'s sending of the Son.</p>',
    "8": '<p>"We ought therefore to show hospitality to such people so that we may work together for the truth" — <em>synergoi</em> (fellow workers, co-laborers) is Paul\'s word for those who share in the missional enterprise (1 Cor 3:9: "we are God\'s fellow workers"; Phil 4:3; Rom 16:3, 9, 21). To support missionaries through hospitality is to become a co-laborer in the gospel of Christ. The truth for which they work together is not an abstraction but the person of Christ (John 14:6); <em>synergoi tē alētheia</em> (co-workers for the truth) is functionally equivalent to co-workers for Christ.</p>',
    "9": '<p>"Diotrephes, who loves to be first (<em>philoproteueōn</em>), will not welcome us" — <em>philoproteueōn</em> (loving preeminence) is the precise inversion of Christ\'s own self-disposition: "who, being in very nature God, did not count equality with God a thing to be grasped, but emptied himself" (Phil 2:6-7). Christ, who had every right to first place, took the last (Mark 10:44-45: "whoever wants to be first among you must be the slave of all; for even the Son of Man did not come to be served, but to serve"). Diotrephes\'s grasping for preeminence is a structural repudiation of the servant-Christology that defines the community\'s life.</p>',
    "10": '<p>"I will call attention to what he is doing, spreading malicious nonsense about us. Not satisfied with that, he even refuses to welcome other believers" — the elder\'s promised personal visit for accountability echoes the pattern of the risen Christ\'s letters to the seven churches (Rev 2-3), where the same Christ who commends also corrects and promises to "come to you" in judgment if patterns are not changed (Rev 2:5, 16; 3:3). Church leadership is accountable to the Lord\'s own standard of servant care; Diotrephes\'s conduct of malicious speech, refusal of welcome, and expulsion of members violates every element of Christ\'s shepherding pattern.</p>',
    "11": '<p>"Anyone who does good is from God. Anyone who does evil has not seen God" — the sight of God is Christological in Johannine theology: "whoever has seen me has seen the Father" (John 14:9); "no one who abides in him keeps on sinning; no one who keeps on sinning has either seen him or known him" (1 John 3:6). To "not have seen God" is to not have encountered the Christ in whom God is fully visible. The contrast between Diotrephes (the evil model, v10) and Gaius/Demetrius (the good model) is ultimately a Christological contrast: one has seen the Lord, the other has not.</p>',
    "12": '<p>"Demetrius is well spoken of by everyone — and even by the truth itself" — "the truth itself" (<em>hypo autes tēs alētheias</em>) bearing witness is striking. In Johannine theology truth is not an impersonal quality but has the character of a person: the Spirit who is "the Spirit of truth" (John 14:17; 15:26; 16:13) guides into all truth and bears witness to Christ. When "the truth itself" testifies to Demetrius, it is the Christological reality — mediated by the Spirit of truth — that vouches for his character. Demetrius is authenticated not by human reputation alone but by participation in the Christ who is the Truth.</p>',
    "13": '<p>"I have much to write to you, but I do not want to do so with pen and ink" — the preference for personal presence over written communication reflects the incarnation-logic: the Word did not remain at a transcendent distance in written form but "became flesh and tabernacled among us" (John 1:14). The letter acknowledges its own limitation relative to the presence it anticipates. Written apostolic letters are the proxy of presence; the personal visit is the fuller form of pastoral care — as Christ\'s own Parousia will be the full presence that the letters of consolation anticipate.</p>',
    "14": '<p>"Peace to you. The friends here send their greetings. Greet the friends there by name" — the peace-benediction (<em>eirēnē soi</em>) is the characteristic greeting of the risen Christ to his gathered disciples: "Peace be with you" (John 20:19, 21, 26). To close with Christ\'s own resurrection-greeting is to locate the community\'s life within the sphere of his Parousia. The greeting of friends "by name" (<em>kat\' onoma</em>) echoes the Shepherd\'s own pattern: "he calls his own sheep by name and leads them out" (John 10:3). The community\'s mutual naming is a participation in Christ\'s own knowing and calling of each of his own.</p>'
  }
}

def main():
    existing = load_comm('mkt-christ', '3john')
    merge_comm(existing, CHRIST)
    save_comm('mkt-christ', '3john', existing)

    il = json.loads((ROOT / 'data' / 'interlinear' / '3john.json').read_text())
    il_vv = set(il.get('1', {}).keys())
    out_vv = set(existing.get('1', {}).keys())
    missing = sorted(il_vv - out_vv, key=int)
    if missing:
        print(f'  ch1: still missing {missing}')
    else:
        print(f'  ch1: complete ({len(out_vv)} verses) ✓')

if __name__ == '__main__':
    main()
