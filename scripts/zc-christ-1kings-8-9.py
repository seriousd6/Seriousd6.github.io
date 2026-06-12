"""
MKT Christ Commentary — 1 Kings chapters 8–9
Run: python3 scripts/zc-christ-1kings-8-9.py

Ch8: kᵉḇôḏ filling the temple → John 1:14 (true tabernacle); Heb 9:24 (heavenly sanctuary);
     šēm theology vs. incarnation — YHWH's name/presence distinction resolved in Christ;
     forgiveness-toward-this-house → Heb 7:25 / Rom 8:34 (Christ's intercession)
Ch9: Conditional covenant curse → Gal 3:13 / Matt 27:51 (Christ takes the curse)

Key typological connections:
- 8:11: kᵉḇôḏ filling temple → John 1:14; Rev 21:3 (true dwelling of God with man)
- 8:27: heaven cannot contain YHWH → John 2:19-21 (Jesus = true temple); Acts 7:48
- 8:30: hear and forgive (intercession toward the house) → Heb 7:25 / Rom 8:34
- 9:7: temple becomes a heap of ruins (conditional curse) → Gal 3:13; Matt 27:51
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
  "8": {
    "11": "<p>The <em>kᵉḇôḏ YHWH</em> filling the temple at its dedication — <em>wᵉkāḇôḏ YHWH mālaʾ ʾet bêt YHWH</em> — is the OT&rsquo;s type of the divine presence fully inhabiting a human-constructed dwelling. John 1:14 is the NT&rsquo;s answer to what this presence ultimately was: <em>kai ho logos sarx egeneto kai eskēnōsen en hēmin, kai etheasametha tēn doxan autou</em> — &lsquo;the Word became flesh and tabernacled (<em>eskēnōsen</em>) among us, and we beheld his glory.&rsquo; The verb <em>skēnoō</em> (to pitch a tent, to tabernacle) directly evokes the Tent of Meeting and the temple tradition: the divine glory that filled Solomon&rsquo;s temple at dedication now inhabits human flesh at the incarnation. The Johannine word &lsquo;glory&rsquo; (<em>doxa</em>) translates the Hebrew <em>kāḇôḏ</em> — John is saying that what Israel saw in the cloud-filled temple, the disciples saw in the person of Jesus. Rev 21:3 (&lsquo;the dwelling of God is with man, and he will dwell with them&rsquo;) is the eschatological consummation: the presence that filled the Solomonic temple, that tabernacled in Christ, will fill the new creation without mediation. The typological sequence — tabernacle (Exod 40) → temple (1 Kgs 8) → incarnation (John 1) → new creation (Rev 21) — traces the single trajectory of divine inresidence seeking its final home.</p>",
    "27": "<p>Solomon&rsquo;s prayer — <em>hinnēh haššāmayim ûšᵉmê haššāmayim lōʾ yᵉḵalᵉlûḵāh ʾap kî habbayit hazzeh</em>, &lsquo;heaven and the highest heaven cannot contain you, how much less this house&rsquo; — poses the exact problem that the incarnation resolves. The Deuteronomic <em>šēm</em>-theology was a partial solution: YHWH&rsquo;s name dwells there, not YHWH&rsquo;s person — divine accessibility without divine containment. Stephen applies this in Acts 7:48-49 (&lsquo;the Most High does not dwell in houses made by hands&rsquo;) to argue the temple&rsquo;s obsolescence. But the NT&rsquo;s resolution is not the temple&rsquo;s abolition — it is the incarnation as the one place where the divine name and the divine person truly coincide. Jesus in John 2:19-21 responds to the demand for a temple-sign: &lsquo;destroy this temple, and in three days I will raise it up&rsquo; — and the narrator explains: <em>ekeinos de elegen peri tou naou tou sōmatos autou</em>, &lsquo;he was speaking about the temple of his body.&rsquo; The house Solomon said could not contain YHWH has its answer in the body of the Son: the one in whom &lsquo;all the fullness of the Godhead dwells bodily&rsquo; (Col 2:9) — who does not merely bear the divine name but is the Word who was with God and was God (John 1:1), now in flesh.</p>",
    "30": "<p>The dedicatory prayer&rsquo;s repeated refrain — <em>wᵉʾattāh tišmaʿ ʾel mᵉqôm šiḇtᵉḵā ʾel haššāmayim wᵉšāmaʿtā wᵉsālaḥtā</em>, &lsquo;and you will hear in your dwelling place in heaven, and when you hear you will forgive&rsquo; — establishes the temple as the mediation-point for divine forgiveness: prayer directed toward the house ascends to YHWH enthroned in heaven, who hears and forgives. Heb 7:25 names the fulfillment: <em>hothen kai sōzein eis to panteles dynatai tous proserchomenous di&rsquo; autou tō theō, pantote zōn eis to entygchanein hyper autōn</em> — &lsquo;therefore he is able to save to the uttermost those who draw near to God through him, since he always lives to make intercession for them.&rsquo; The temple&rsquo;s directional prayer-structure (&lsquo;toward this house... YHWH will hear in heaven&rsquo;) becomes in Heb 7 a person-structure: Jesus himself is the mediating point through whom prayer ascends and forgiveness descends, and he lives permanently to make that intercession. Rom 8:34 makes the same point: <em>hos kai entygchanei hyper hēmōn</em>, &lsquo;he who also intercedes for us.&rsquo; The temple&rsquo;s mediation was architectural and ritual; Christ&rsquo;s mediation is personal and unending — the fulfillment and replacement of everything the temple&rsquo;s architecture was designed to express.</p>"
  },
  "9": {
    "7": "<p>YHWH&rsquo;s conditional warning — <em>wᵉhikkrattî ʾet yiśrāʾēl mēʿal pᵉnê hāʾădāmāh... wᵉhabbayit hazzeh yihyeh ʿelyôn</em>, &lsquo;I will cut off Israel from the land... and this house will become a heap of ruins&rsquo; — is the curse-side of the Deuteronomic covenant (Deut 28:15-68). The temple&rsquo;s destruction is the enacted covenant curse: YHWH himself destroys his own house when Israel violates the covenant. Paul in Gal 3:13 names how the curse is absorbed: <em>Christos hēmas exēgorasen ek tēs kataras tou nomou genomenos hyper hēmōn katara</em> — &lsquo;Christ redeemed us from the curse of the law by becoming a curse for us.&rsquo; The conditional curse of 1 Kgs 9:7 — exile, temple-destruction, becoming &lsquo;a proverb and a byword among all peoples&rsquo; (v7) — fell in 586 BCE exactly as YHWH warned. The NT argument is that Christ entered that curse-structure and exhausted it: the temple veil torn at his death (Matt 27:51) signals the old temple&rsquo;s end and the new-temple inauguration in Christ&rsquo;s body (John 2:21). The conditional covenant&rsquo;s worst clause — the heap of ruins — was fulfilled; but it was fulfilled in the one who bore the curse so that no further fulfillment is required. Eph 2:14 (&lsquo;he himself is our peace, who has made us both one and has broken down in his flesh the dividing wall of hostility&rsquo;) describes the temple&rsquo;s replacement: not stone but flesh, not conditional covenant but grace.</p>"
  }
}

def main():
    c = load_comm('mkt-christ', '1kings')
    merge_comm(c, CHRIST)
    save_comm('mkt-christ', '1kings', c)
    count = sum(len(v) for v in CHRIST.values())
    print(f'1kings mkt-christ: wrote {count} verses across ch 8-9')

if __name__ == '__main__':
    main()
