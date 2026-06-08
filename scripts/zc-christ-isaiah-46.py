"""
MKT Christ Commentary — Isaiah chapter 46
Run: python3 scripts/zc-christ-isaiah-46.py

Source data used:
- data/interlinear/isaiah.json
- data/translation/draft/mediating/isaiah.json

Key decisions in this range:
- vv. 1-2: Bel/Nebo go into captivity — revelation of God; contrast: Eph 4:8 (Christ led captivity captive)
- vv. 3-4: YHWH carries Israel, not vice versa — shadow: Matt 11:28-30; 1 Pet 5:7
- v. 5: incomparability challenge — shadow: Phil 2:9-11; Col 2:9
- vv. 9-10: end declared from the beginning — shadow: John 13:19; Luke 24:44
- vv. 12-13: righteousness and salvation not delayed, put in Zion — direct: Rom 3:21-26; 1 Cor 1:30
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
    # INTENT: Non-destructive merge — existing entries are never overwritten, safe to re-run
    for ch, verses in new_data.items():
        if ch not in existing: existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]: existing[ch][v] = html

ISAIAH = {
"46": {
"1": "<p>A revelation of God: Bel bows down, Nebo stoops (<em>Bēl kāra' Nĕb̠ô šōaḥ</em>) — the chief gods of Babylon collapse as their images are loaded onto animals for deportation. The irony is devastating: gods who should carry their worshippers are themselves carried, a burden for exhausted beasts. Paul echoes this when he describes what the Corinthians were: <em>led astray to mute idols, however you were led</em> (1 Cor 12:2). The idol-god that must be carried to safety is the anti-type of the God who carries his people — established in vv. 3-4. Christ who leads captivity captive (Eph 4:8, citing Ps 68:18) is the antitype of Bel and Nebo going into captivity.</p>",
"2": "<p>A revelation of God: they stoop and bow down together; they cannot save the burden — they themselves go into captivity. The total impotence of Babylon's gods at the moment of crisis — they cannot even save themselves, let alone their worshippers — is the verdict on every false absolute. Revelation 18:2 applies this logic to the fall of spiritual Babylon: <em>fallen, fallen is Babylon the great!</em> Every power that claims divine authority but cannot deliver at the crisis moment collapses under the weight it claimed to bear.</p>",
"3": "<p>A shadow: <em>šimĕ'û 'ēlay b̠êt ya'ăqōb̠... haśśûnim min-habeṭen hannĕśū'im min-rāḥam</em> — listen to me, house of Jacob, all who remain of Israel, who have been borne by me from before birth, carried from the womb. The contrast with the idol of vv. 1-2 is complete: the idol must be carried; YHWH carries. He has borne Israel from the womb — the parent-who-carries image. This is the God who carries that Christ reveals: Matthew 11:28-30 (<em>come to me, all who are weary and heavy-laden, and I will give you rest</em>); 1 Peter 5:7 (<em>cast all your anxieties on him, because he cares for you</em>). The God who carried Israel from the womb is the God who carries his people through the Son.</p>",
"4": "<p>A shadow: <em>wĕ'ad-ziqnāh 'ănî hû' wĕ'ad-śêb̄āh 'ănî 'esb̄ōl 'ănî 'āśîtî wĕ'ănî 'eśśā' wĕ'ănî 'esb̄ōl wĕ'ămallēṭ</em> — even to old age I am he; even to gray hairs I will carry you. I have made, and I will bear; I will carry, and I will save. The threefold carrying-promise (I will bear / I will carry / I will save) framed by the absolute <em>'ănî hû'</em> (I am he). Hebrews 13:8 (Jesus Christ is the same yesterday and today and forever) is the NT application: the faithfulness that carries Israel from womb to gray hair is the faithfulness that never changes in the incarnate Son. Christ who is the same from before creation to the last day carries his people through the whole span of existence.</p>",
"5": "<p>A revelation of God: to whom will you liken me and make me equal? — <em>lĕmî tedammĕyûnî wĕtašwû wĕtamdĕlûnî wĕnimsāl</em>. The incomparability challenge that Isaiah 40:18,25 has already raised is pressed again here after the idol-polemic. The NT's answer to the incomparability question is Christological: Philippians 2:9-11 (the name above every name); Colossians 2:9 (in him the whole fullness of deity dwells bodily); Hebrews 1:3-4 (having become as much superior to angels as the name he has inherited is more excellent than theirs). There is no one like YHWH — and the fullness of that incomparable YHWH is present in Christ.</p>",
"6": "<p>A revelation of God: those who lavish gold and weigh silver hire a goldsmith to make a god — then they bow down and worship. The economic investment in the idol (gold, silver, craftsman's fee) followed by worship is the description of all idolatry: human resources poured into what cannot save. Paul diagnoses the same dynamic in Colossians 3:5: greed is idolatry — the investment of ultimate desire in finite objects. The idol-maker of Isaiah 46:6 and the greedy man of Colossians 3:5 are engaged in the same act: constructing and worshipping what they have made.</p>",
"7": "<p>A revelation of God: they lift it to their shoulder, carry it, set it in its place — it stands there; it cannot move from its place. One cries out to it; it does not answer or save him from his trouble. The idol that cannot move, answer, or save is the consistent verdict of the idol-polemic (Ps 115:4-7; Isa 44:17-18). Christ as the true answerer: John 11:43-44 (Jesus calls, Lazarus comes out); John 14:14 (<em>if you ask me anything in my name, I will do it</em>); Hebrews 4:16 (<em>that we may receive mercy and find grace to help in time of need</em>). The idol cannot save from trouble; Christ saves from the ultimate trouble.</p>",
"8": "<p>A revelation of God: remember this and consider; recall it to mind, you transgressors. The call to memory (<em>zikrû-zō't wĕhitbōnānû</em>) is a call to intellectual engagement with the evidence — YHWH does not demand faith without reason but with it. The same epistemological seriousness underlies the NT: 2 Peter 1:16 (<em>we did not follow cleverly devised myths, but were eyewitnesses of his majesty</em>); Acts 1:3 (he presented himself alive with many proofs). The God who demands that Israel remember and reason is the God who provides evidence through the resurrection.</p>",
"9": "<p>A direct Christological claim grounding. <em>'ănî 'ēl wĕ'ên 'ôd 'Ĕlōhîm wĕ'ep̄es kāmônî</em> — I am God, and there is no other; I am God, and there is none like me. The absolute monotheism of Isaiah 46:9 is the very claim that the NT applies to Christ: John 10:30 (<em>I and the Father are one</em>); John 14:9 (<em>whoever has seen me has seen the Father</em>); Colossians 1:19 (<em>in him all the fullness of God was pleased to dwell</em>). The <em>'ên 'ôd</em> (none other) of Isaiah 46:9 is not abandoned in the NT but filled with Trinitarian content — the same YHWH who is none other now reveals himself through the Son.</p>",
"10": "<p>A direct reference. <em>maggîd mē'rēšît 'aḥărît ûmiqkedem 'ăšer lō'-na'ăśû</em> — declaring the end from the beginning, and from ancient times things not yet done. The divine capacity to declare the future and fulfill it is YHWH's unique credential. Jesus applies this to himself: John 13:19 (<em>I am telling you this now, before it takes place, so that when it does take place you may believe that I am he</em>). Luke 24:44-45 (everything written about me in the Law, the Prophets, and the Psalms must be fulfilled). The one who declares the end from the beginning in Isaiah 46:10 is the Christ who fulfills every word spoken about him.</p>",
"11": "<p>A revelation of God: the bird of prey from the east — a man of YHWH's counsel from a far country — YHWH has spoken and will bring it to pass; he has purposed and will do it. The irresistibility of divine purpose (<em>'ānî dibbartî 'ap̄-'ăb̄î'ennāh yāṣartî 'ap̄-'e'eśennāh</em> — I have spoken, and I will bring it; I have purposed, and I will do it) is the ground of eschatological confidence. Acts 4:28 applies this to the cross: those who crucified Christ did what YHWH's hand and plan had predestined. Ephesians 1:11 (in him we have an inheritance, having been predestined according to the purpose of him who works all things according to the counsel of his will) is the NT form of Isaiah 46:11's irresistibility.</p>",
"12": "<p>A direct prophecy. <em>šimĕ'û 'ēlay 'abbîrê lēb̠ hārĕḥôqîm min-haṣṣĕdāqāh</em> — listen to me, you stubborn of heart, you who are far from righteousness. The call to the hard-hearted who are far from righteousness is the posture of grace that Christ embodies: he came not to call the righteous but sinners (Matt 9:13); he ate with tax collectors and sinners (Luke 15:1-2) precisely because they were far from righteousness. The God who calls to those far from righteousness in Isaiah 46:12 is the God who draws near to them in Christ.</p>",
"13": "<p>A direct prophecy. <em>qērab̠tî ṣidqātî lō' tirḥāq ûtĕšû'ātî lō' tĕ'aḥēr</em> — I bring near my righteousness; it is not far off, and my salvation will not delay. I will put salvation in Zion for Israel my glory. This is the compressed gospel announcement: YHWH's righteousness (<em>ṣidqāh</em>) and salvation (<em>tĕšû'āh</em>) are near, not delayed, and are placed in Zion. Romans 3:21-26 announces the fulfillment: now the righteousness of God has been manifested apart from the law... the righteousness of God through faith in Jesus Christ. 1 Corinthians 1:30 (Christ Jesus became to us wisdom from God, and righteousness and sanctification and redemption). The salvation placed in Zion is the crucified and risen Christ — Israel's glory and the world's hope.</p>"
}
}

def main():
    existing = load_comm('mkt-christ', 'isaiah')
    merge_comm(existing, ISAIAH)
    save_comm('mkt-christ', 'isaiah', existing)
    v = sum(len(vs) for vs in ISAIAH.values())
    print(f'Isaiah 46 mkt-christ: {v} verses written.')

if __name__ == '__main__':
    main()
