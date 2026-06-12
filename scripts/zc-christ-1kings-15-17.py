"""
MKT Christ Commentary — 1 Kings chapters 15–17
Run: python3 scripts/zc-christ-1kings-15-17.py

Ch15: Asa's reform and lēḇ šālēm — undivided heart / Matt 22:37 fulfilled in Christ;
      David as the covenant type against which all kings are measured
Ch16: Elijah announced without introduction — the prophet who suddenly appears / John 1:6
Ch17: Elijah fed by ravens — YHWH's unexpected provision type;
      widow's son raised — first resurrection type / Luke 7:14; Heb 11:35

Key typological connections:
- 15:5: David's heart perfect (except Uriah) → contrast with Christ's perfect obedience (Heb 4:15)
- 17:6: ravens bringing bread/meat → John 6:35 (true bread from heaven)
- 17:14: flour/oil not failing → John 6:35; Luke 4:26 (Gentile inclusion type)
- 17:22: widow's son raised from death → Luke 7:14; Heb 11:35 (resurrection type)
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
  "15": {
    "5": "<p>The narrator&rsquo;s parenthetical commendation of David — <em>ʾăšer ʿāśāh dāwîḏ hayyāšār bᵉʿênê YHWH wᵉlōʾ sār mikkōl ʾăšer ṣiwwāhû kol yᵉmê ḥayyāyw raq biddᵉḇar ʾûriyyāh haḥittî</em>, &lsquo;David did what was right in the eyes of YHWH and did not turn aside from anything he commanded all the days of his life, except in the matter of Uriah the Hittite&rsquo; — establishes David as the positive covenant standard while noting the single catastrophic exception. The Deuteronomistic History uses David as the baseline against which every subsequent king is measured: &lsquo;he did not do as his father David had done&rsquo; (14:8, 15:11) or &lsquo;he walked in all the way of his father David&rsquo; (15:11 of Asa). But David&rsquo;s own &lsquo;except in the matter of Uriah&rsquo; reveals that the standard itself was imperfect — the very model-king had the exception clause. Heb 4:15 names the fulfillment of what the David-standard pointed toward but could not itself achieve: <em>pepeirasmenon de kata panta kath&rsquo; homoiotēta chōris hamartias</em> — &lsquo;one who in every respect has been tempted as we are, yet without sin.&rsquo; Jesus is the king who has no exception clause: no &lsquo;except in the matter of.&rsquo; The Davidic covenant found its definitive embodiment in the one who fulfilled David&rsquo;s role without David&rsquo;s exception — whose obedience was truly undivided where David&rsquo;s was not.</p>"
  },
  "17": {
    "6": "<p>YHWH&rsquo;s provision for Elijah at the Wadi Cherith — <em>wᵉhāʿōrᵉḇîm mᵉḇîʾîm lô leḥem ûbāśār babbōqer wᵉleḥem ûbāśār bāʿereḇ</em>, &lsquo;the ravens brought him bread and meat in the morning and bread and meat in the evening&rsquo; — is a type of divine provision through unlikely agents. Ravens are unclean birds (Lev 11:15); YHWH feeds his prophet through instruments the covenant would exclude from the sanctuary. The typological point: divine provision for the servant in extremity comes through unexpected channels, not through the established cultic system. Jesus in John 6:35 names himself as the fulfillment of the provision-from-heaven pattern: <em>egō eimi ho artos tēs zōēs; ho erchomenos pros eme ou mē peinasē</em> — &lsquo;I am the bread of life; whoever comes to me shall not hunger.&rsquo; The ravens at Cherith are one in the sequence: manna in the wilderness, ravens at Cherith, flour/oil for the Zarephath widow, the feeding of the five thousand — all are types of the one true bread that descends from heaven and gives life to the world (John 6:33). The provision comes from above, to those in the wilderness, through agents the world does not recognize.</p>",
    "22": "<p>The raising of the widow of Zarephath&rsquo;s son — <em>wayyišmaʿ YHWH bᵉqôl ʾēliyyāhû wayyāšāḇ nefaš hayyeled ʿal qirbô wayyeḥî</em>, &lsquo;YHWH listened to the voice of Elijah, and the life of the child came into him again and he revived&rsquo; — is the OT&rsquo;s first recorded individual resurrection. The sequence of acts — Elijah stretches himself over the child three times and cries to YHWH (vv21-22); the child lives — establishes the type-pattern: the prophet intercedes physically and personally with his whole body over the dead, YHWH hears, life returns. Luke 7:14-15 narrates Jesus&rsquo;s raising of the widow of Nain&rsquo;s son in deliberate structural echo: a widow, a dead son, a restoration, the crowd&rsquo;s response that &lsquo;a great prophet has arisen among us.&rsquo; Heb 11:35 in its honor roll of faith includes &lsquo;women [who] received back their dead by resurrection&rsquo; — the Zarephath widow is the first. The sequence from Elijah&rsquo;s raising to Elisha&rsquo;s raising (2 Kgs 4), to Jesus&rsquo;s multiple raisings (Nain, Jairus, Lazarus), to the general resurrection is the OT&rsquo;s incremental witness that YHWH is the God who gives life to the dead — and Jesus is the one in whom that giving is no longer miraculous exception but constitutive identity: &lsquo;I am the resurrection and the life&rsquo; (John 11:25).</p>"
  }
}

def main():
    c = load_comm('mkt-christ', '1kings')
    merge_comm(c, CHRIST)
    save_comm('mkt-christ', '1kings', c)
    count = sum(len(v) for v in CHRIST.values())
    print(f'1kings mkt-christ: wrote {count} verses across ch 15-17')

if __name__ == '__main__':
    main()
