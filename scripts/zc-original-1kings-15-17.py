"""
MKT Original Commentary — 1 Kings chapters 15–17
Run: python3 scripts/zc-original-1kings-15-17.py

Ch15: lēḇ šālēm — Asa's whole heart; the regnal evaluation formula;
      šālēm/šālôm root; the OT's highest royal verdict and its consistent failure
Ch16: hāḇlêhem — 'their vanities'; idols as heḇel (vapor); Qohelet / Rom 1 connection
Ch17: Elijah's lᵉpānāyw formula — prophet as divine-council attendee;
      wayyitmōdad — 'measured himself against the child'; physical resurrection prayer

Key Hebrew terms:
- lēḇ šālēm (15:14): whole/perfect heart — šālēm = complete, at peace (cf. šālôm)
- hāḇlêhem (16:13): their vanities — heḇel = vapor, Qohelet's keynote; idols as non-being
- lᵉpānāyw (17:1): before him — the standing-before-YHWH formula of prophetic access
- wayyitmōdad (17:21): stretched/measured himself — hitpael of mādad (to measure)
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

ORIGINAL = {
  "15": {
    "14": "<p>The regnal evaluation of Asa — <em>wᵉlēḇ ʾāsāʾ hāyāh šālēm ʿim YHWH kol yāmāyw</em>, &lsquo;Asa&rsquo;s heart was wholly true (<em>šālēm</em>) to YHWH all his days&rsquo; — is the Deuteronomistic historian&rsquo;s highest royal verdict. The adjective <em>šālēm</em> (whole, complete, undivided, at peace) is the root of <em>šālôm</em> (peace, well-being) and of Solomon&rsquo;s name (<em>šᵉlōmōh</em>): the <em>lēḇ šālēm</em> is the heart that has found its integration and rest in YHWH alone, undivided by rival loyalties. 2 Chr 16:9 extends the principle as a divine promise: &lsquo;the eyes of YHWH run to and fro throughout the whole earth, to give strong support to those whose heart is <em>šālēm</em> toward him.&rsquo; The regnal evaluations of Kings and Chronicles use the <em>šālēm</em> standard as their binary — each king either maintains wholeness or fragments it. Asa himself fails this standard in 2 Chr 16:7-12, where he trusts in the king of Aram rather than YHWH in his final years, and his heart ceases to be <em>šālēm</em>. The NT appropriation of the whole-heart standard: Deut 6:5 (&lsquo;you shall love YHWH your God with all your heart, <em>bᵉkol lᵉḇāḇᵉḵā</em>&rsquo;) is what Jesus identifies in Matt 22:37 as the first and greatest commandment — the <em>lēḇ šālēm</em> as the definition of the covenant&rsquo;s core demand. The fact that no king fully sustained the <em>lēḇ šālēm</em> across an entire reign is the OT&rsquo;s implied argument for why the Davidic promise requires a greater son.</p>"
  },
  "16": {
    "13": "<p>The explanation for the fall of Baasha&rsquo;s dynasty names the instrument of provocation as <em>hāḇlêhem</em> — &lsquo;their idols,&rsquo; literally &lsquo;their vapors/vanities.&rsquo; The noun <em>heḇel</em> (breath, vapor, vanity) is the OT&rsquo;s theological critique of idolatry in one word: idols are as insubstantial and transient as a breath of air. <em>Heḇel</em> is the keynote word of Qohelet: <em>heḇel hăḇālîm</em> (Eccl 1:2, &lsquo;vanity of vanities&rsquo;) — the same root used there for all human striving under the sun without the fear of God. When the OT describes idols as <em>hăḇālîm</em>, it places them in the same category as the futile: things that exist but have no solid being, no life-giving capacity, no <em>rûaḥ</em> (breath/spirit) of their own. Jer 10:15: <em>heḇel hēmmāh maʿăśēh taʿtuʿîm</em> — &lsquo;they are vanity, a work of delusion.&rsquo; The LXX translates <em>heḇel</em> as <em>mataios</em> (vain, futile), which Paul uses in Acts 14:15 (&lsquo;turn from these vain things, <em>tōn mataion</em>, to a living God&rsquo;) and in Rom 1:21 (&lsquo;they became futile, <em>emataiōthēsan</em>, in their thinking&rsquo;). The OT&rsquo;s <em>heḇel</em>-critique of idolatry is the precise theological vocabulary on which Paul builds his argument in Rom 1:18-25: to exchange the glory of the incorruptible God for an image is to exchange substance for vapor.</p>"
  },
  "17": {
    "1": "<p>Elijah&rsquo;s drought announcement opens with the formula: <em>ḥay YHWH ʾelōhê yiśrāʾēl ʾăšer ʿāmadtî lᵉpānāyw</em> — &lsquo;As YHWH the God of Israel lives, before whom I stand (<em>lᵉpānāyw</em> — to/before his face).&rsquo; The phrase <em>ʿāmad lᵉpānāyw</em> (stand before him) is the formula of prophetic investiture: the one who stands before YHWH has access to the divine council (<em>sôḏ YHWH</em>) and delivers its decrees as the divine messenger. Jer 23:18 makes this the mark of true prophecy: &lsquo;for who among them has stood in the council of YHWH (<em>baʿăṣat YHWH</em>) to see and to hear his word?&rsquo; The false prophet speaks without standing; the true prophet speaks from standing before YHWH. The same formula describes the seraphim (&lsquo;standing above him,&rsquo; Isa 6:2), the angelic court in Job 1:6, and the Levitical ministry (&lsquo;to stand before YHWH to serve him,&rsquo; Deut 10:8). Heb 7:25 applies the standing-before-God formula to Christ&rsquo;s perpetual intercession: &lsquo;he always lives to make intercession for them&rsquo; — his permanent <em>lᵉpānāyw</em> presence before the Father is the fulfillment of what the prophet&rsquo;s standing before YHWH anticipated, now without intermission and without the distance of messenger-relationship.</p>",
    "21": "<p>Elijah&rsquo;s prayer over the widow&rsquo;s dead son uses an unusual verb: <em>wayyitmōdad ʿal hayyelεḏ šālōš pᵉʿāmîm</em> — &lsquo;he stretched/measured himself upon the child three times.&rsquo; The verb <em>mādad</em> (to measure) in the hitpael (reflexive/intensive) means &lsquo;to stretch oneself out measuring against&rsquo; — a physical alignment of the prophet&rsquo;s living body against the child&rsquo;s dead body, repeated three times. The three-fold repetition (<em>šālōš pᵉʿāmîm</em>) marks intensity of intercessory prayer rather than mechanical technique: the life that returns comes from Elijah&rsquo;s prayer (v21b: <em>wayyiqrāʾ ʾel YHWH</em>, &lsquo;he cried to YHWH&rsquo;), not from the physical posture alone. The Elisha parallel (2 Kgs 4:34: <em>wayyiggahar ʿālaw</em>, &lsquo;he stretched himself over him&rsquo;) establishes this as a prophetic pattern: physical closeness of the life-bearing prophet to the dead child as the vehicle of divine life-transfer. Paul over Eutychus (Acts 20:10: <em>epipesōn autō</em>, fell upon him) continues the pattern in apostolic form. The underlying theological claim in all three instances is that life-giving is a divine prerogative mediated through the prophet/apostle&rsquo;s bodily and intercessory presence — a pattern whose ultimate ground is the incarnation: the Life of the world (John 11:25) taking on a body in order to give life through physical presence and sacrificial death.</p>"
  }
}

def main():
    c = load_comm('mkt-original', '1kings')
    merge_comm(c, ORIGINAL)
    save_comm('mkt-original', '1kings', c)
    count = sum(len(v) for v in ORIGINAL.values())
    print(f'1kings mkt-original: wrote {count} verses across ch 15-17')

if __name__ == '__main__':
    main()
