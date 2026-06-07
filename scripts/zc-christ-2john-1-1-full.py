"""
mkt-christ layer — 2 John chapter 1 (all 13 verses)
Output: data/commentary/mkt-christ/2john.json
Run: python3 scripts/zc-christ-2john-1-1-full.py

Pre-existing: ch1v3 — merge_comm will skip it.

Interpretation decisions:
- The 'truth' throughout (vv. 1-4) is Christological: Jesus is the truth (John 14:6),
  and walking in truth is walking in conformity with the incarnate Christ.
- v7 'Jesus Christ coming in the flesh' (erchomonon = present participle): the Johannine
  test is not just acknowledgement of the past incarnation but of the ongoing/returning
  Christ; the antichrist denies both.
- v9 'teaching of Christ' = both the teaching ABOUT Christ (objective genitive) and the
  teaching OF Christ himself (subjective genitive); both senses are active.
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
  "1": {
    "1": "<p>'The elder to the elect lady and her children, whom I love in truth' — 'in truth' (<em>en alētheia</em>) is Christological from the first word of the body: the love the elder has for this community is grounded in Christ, who is himself the truth (John 14:6: I am the way and the truth and the life). The love is not merely affectionate but participates in the truth-reality that Christ is; the elder and the community are bound by a love that has its origin and character in Christ. The 'elect lady' (whether an individual or a personified local church) is 'chosen' (<em>eklektē</em>) — the Christological election that Peter also applies to the scattered communities (1 Pet 1:1: elect exiles).</p>",
    "2": "<p>'Because of the truth that abides in us and will be with us forever' — the truth that 'abides in us' is the Spirit of truth (John 14:17: the Spirit of truth... he abides with you and will be in you; 16:13: the Spirit of truth will guide you into all truth), and the Spirit is the Spirit of Christ (Rom 8:9). To have truth abiding in one is to have Christ's own presence mediated through the Spirit; the permanence — 'forever' (<em>eis ton aiōna</em>) — is the permanence of Christ's own presence, which he promised would never leave (John 14:18: I will not leave you as orphans; Matt 28:20: I am with you always).</p>",
    "4": "<p>'I was greatly rejoiced to find some of your children walking in the truth, just as we received a command from the Father' — walking in truth (<em>peripatounta en alētheia</em>) is the Christological ethic: conformity in life and conduct to the truth that Christ is. The command 'from the Father' to walk in truth is fulfilled by walking in conformity with the Son who is the truth; there is no obedience to the Father's command that bypasses the Son's reality. The elder's joy at finding truth-walkers mirrors Christ's own joy over those who abide in his love (John 15:11: that my joy may be in you, and that your joy may be full).</p>",
    "5": "<p>'And now I ask you, dear lady — not as writing a new command to you but one we have had from the beginning — that we love one another' — the love command 'from the beginning' is Christ's own command given at the Last Supper (John 13:34: a new command I give you: love one another as I have loved you). It is 'new' in the sense of being the defining command of the new age inaugurated by Christ, but it has been 'from the beginning' of the community's life because it was given with Christ's first formation of the disciples. The love commanded is the same love that Christ demonstrated and commands: agapē modeled on the cross.</p>",
    "6": "<p>'And this is love, that we walk according to his commands. This is the command, just as you heard from the beginning, that you walk in it' — the identification of love with obedience to Christ's commands is the Johannine Christological logic: love for Christ is expressed in keeping his commands (John 14:15: if you love me, you will keep my commands; 15:10: if you keep my commands, you will abide in my love, just as I have kept my Father's commands and abide in his love). The command and the love are not two separate things; walking in Christ's commands is itself the love-walk. The tautology in the verse is deliberate: love = obedience = love, because Christ is the content of both.</p>",
    "7": "<p>'Because many deceivers have gone out into the world — those who do not confess Jesus Christ coming in the flesh. This is the deceiver and the antichrist' — the Christological test for authentic teaching: confession of 'Jesus Christ coming in the flesh' (<em>Iēsoun Christon erchomenon en sarki</em>). The present participle <em>erchomenon</em> (coming, not merely 'who came') may point to both the first advent (the historical incarnation) and the parousia (the coming-again); the antichrist denies both the reality of the incarnation and the returning Christ. This confession — that the eternal Word became and remains flesh (John 1:14: the Word became flesh and dwelt among us) — is the irreducible Christological minimum that separates true teaching from the Docetic deception.</p>",
    "8": "<p>'Watch yourselves, so that you may not lose what we have worked for but may win a full reward' — the Christological vigilance: what is at risk is the fullness of reward that Christ will give at his appearing (cf. 1 Pet 5:4: the unfading crown of glory; 1 Cor 3:14: the one whose work survives will receive a reward). To 'lose what we have worked for' is to abandon the Christological confession of v.7 and thereby to fall out of the relationship with the Son that makes the reward possible. The reward is not earned but received by those who remain in Christ — who 'continue in the teaching of Christ' (v.9).</p>",
    "9": "<p>'Everyone who goes on ahead and does not abide in the teaching of Christ does not have God. Whoever abides in the teaching has both the Father and the Son' — the most concentrated Christological claim in the letter: the relationship with God the Father is inseparable from the relationship with the Son mediated through the Son's teaching. To have God is to have the Father-and-Son together; to abandon the teaching of Christ is to lose the Father as well (John 5:23: whoever does not honor the Son does not honor the Father; 14:6: no one comes to the Father except through me). The 'teaching of Christ' is both what Christ taught and what the apostles taught about Christ — to advance 'beyond' it into speculative Christology (Docetism) is not progress but apostasy.</p>",
    "10": "<p>'If anyone comes to you and does not bring this teaching, do not receive him into your house or give him any greeting' — the exclusion is Christological, not social: to welcome a teacher who denies the incarnation is to provide a platform for antichrist teaching within the community's gathering-space (the house church). The household was the primary location of the Christ-community's worship and teaching; welcoming a false teacher into the house was welcoming the deception into the body. The severity of the command is proportional to the severity of what is denied: the incarnation is not a peripheral teaching but the foundation of the entire redemptive work.</p>",
    "11": "<p>'For whoever greets him takes part in his wicked works' — the Christological solidarity works in both directions: just as participation in Christ's community means sharing in his life and work (1 John 1:3: our fellowship is with the Father and with his Son Jesus Christ), participation in the antichrist teacher's hospitality means sharing in the destructive work of denying Christ. The greeting (<em>chairein</em>) in the ancient world was not casual social courtesy but a formal expression of fellowship and endorsement; extending it to a denier of the incarnation was a public affirmation of their ministry.</p>",
    "12": "<p>'Though I have much to write to you, I do not want to use paper and ink. Instead I hope to come to you and talk face to face, so that our joy may be complete' — the elder's desire for face-to-face (<em>stoma pros stoma</em>, literally mouth to mouth) encounter is the Christological value of incarnate presence: the same word-become-flesh logic that underlies the entire letter (v.7: coming in the flesh) is reflected in the preference for personal presence over written communication. Christ himself is the ultimate expression of this: God's desire to speak to humanity was fulfilled not through texts alone but through the Word becoming flesh. The 'complete joy' (<em>hē chara hēmōn peplērōmenē</em>) echoes Christ's own prayer for the community's joy (John 15:11; 17:13).</p>",
    "13": "<p>'The children of your elect sister greet you' — the greeting from the 'elect sister' (another local church) expresses the solidarity of the whole body of Christ: communities that share the Christological confession and the love command are sisters to one another, bound by the same election (1 Pet 1:1: elect exiles), the same Lord, and the same truth (v.1). The simple greeting carries the full theological weight of the letter: they are 'elect' (chosen in Christ), they are family (born of the same Father through the same Son), and their fellowship is 'in truth and love' (v.3) — in Christ himself.</p>"
  }
}

if __name__ == '__main__':
    existing = load_comm('mkt-christ', '2john')
    merge_comm(existing, NEW_DATA)
    save_comm('mkt-christ', '2john', existing)
    import json as _json
    il = _json.load(open(ROOT / 'data' / 'interlinear' / '2john.json'))
    all_ok = True
    for ch in ['1']:
        missing = set(il.get(ch, {}).keys()) - set(existing.get(ch, {}).keys())
        if missing:
            print(f'  ch {ch} STILL MISSING: {sorted(missing, key=int)}')
            all_ok = False
        else:
            print(f'  ch {ch}: complete ({len(existing.get(ch, {}))} verses)')
    if all_ok:
        print('All verses present')
