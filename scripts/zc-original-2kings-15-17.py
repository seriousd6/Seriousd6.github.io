"""
MKT Original Commentary — 2 Kings chapters 15–17
Run: python3 scripts/zc-original-2kings-15-17.py

Ch15: yāsap ʿôḏ — 'added yet more' (the sin formula); rapid-fire king succession
Ch16: mōlēḵ / hammōleḵ ʾet bᵉnô bāʾēš — passing son through fire (child sacrifice)
Ch17: wayyihyû yᵉrēʾîm ʾet YHWH — 'they feared YHWH but also served their own gods'
      The double-service problem — ûgôyîm hayyû (mixed service as the Samaritan synthesis)

Key Hebrew terms:
- hammōleḵ (16:3): the Molech/Molek sacrifice — fire-passing as child sacrifice
- yᵉrēʾîm ʾet YHWH (17:32, 33): feared/worshipped YHWH — syncretistic use of yārēʾ
- wayyihyû yᵉrēʾîm ʾet YHWH wᵉhāyû ʿōḇᵉdîm (17:33): feared YHWH AND served their gods
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
  "16": {
    "3": "<p>The notice that Ahaz &lsquo;burned his son as an offering (<em>wayyaʿăḇēr ʾet bᵉnô bāʾēš</em>)&rsquo; — the <em>heʿăḇîr bāʾēš</em> formula (&lsquo;to cause to pass through the fire&rsquo;) — is the OT&rsquo;s technical expression for child sacrifice associated with the <em>Mōleḵ</em> cult. The formula appears throughout the Deuteronomistic literature (Deut 18:10; 2 Kgs 17:17; 21:6; 23:10; Jer 32:35) and the underlying practice is attested in the Hinnom valley (<em>Gê Hinnom</em>), where the Topheth installation was the site of the sacrifices. The Hebrew vocalization <em>Mōleḵ</em> has the consonants of <em>melek</em> (king) but the vowels of <em>bōšet</em> (shame) — the same scribal degradation applied to Baal-zebub and to Baal in personal names. Whether the formula describes actual child-burning or a rite of dedication-through-fire is debated (Mosca, Heider, Day), but the Deuteronomistic condemnation is consistent and unambiguous: this is the covenant-abomination of the nations, and Ahaz is the first Judahite king to practice it openly. Matt 25:41 (&lsquo;depart from me, you cursed, into the eternal fire prepared for the devil and his angels&rsquo;) and Rev 20:14-15 transpose the fire-of-sacrifice into the fire-of-judgment: the <em>Gê Hinnom</em> becomes <em>Gehenna</em> in the NT as the permanent destination of what the Topheth prefigured in miniature.</p>"
  },
  "17": {
    "33": "<p>The narrator&rsquo;s description of the Assyrian settlers&rsquo; religion — <em>ʾet YHWH hāyû yᵉrēʾîm wᵉʾet ʾelōhêhem hāyû ʿōḇᵉdîm</em>, &lsquo;they feared YHWH but also served their own gods&rsquo; — is the OT&rsquo;s most precise formulation of religious syncretism. The verb pair is diagnostic: <em>yārēʾ</em> (to fear/revere) is the proper response to YHWH (&lsquo;the fear of YHWH is the beginning of wisdom,&rsquo; Prov 9:10); <em>ʿāḇaḏ</em> (to serve/worship) is the proper response to YHWH (&lsquo;you shall serve YHWH your God,&rsquo; Exod 23:25). The Samaritan settlers use both words — but split them: YHWH receives <em>yārēʾ</em>; their own gods receive <em>ʿāḇaḏ</em>. The Hebrew grammar is exact: both participles are simultaneous — not sequential or alternating, but contemporaneous double-allegiance. V34 undercuts even the <em>yārēʾ</em>: &lsquo;to this day they do not fear YHWH according to the statutes and rules&rsquo; — the <em>yārēʾ</em> without Torah-conformity is not genuine fear but a cultural add-on. Jesus in Matt 4:10 (quoting Deut 6:13) names the final resolution: <em>Kyriō tō theō sou proskyneseis kai autō monō latreusei</em> — &lsquo;you shall worship the Lord your God and him <em>alone</em> shall you serve.&rsquo; The <em>monō</em> (alone) is the antithesis of 2 Kgs 17:33&rsquo;s simultaneous double-service: the covenant demands undivided allegiance, not the YHWH-fear/idol-service split that the Samaritan synthesis institutionalized.</p>",
    "41": "<p>The final summary verse of the Samaritan settlement — <em>wayhî hag gôyîm hāʾēlleh yᵉrēʾîm ʾet YHWH wᵉʾet pᵉsîlêhem hāyû ʿōḇᵉdîm gam bᵉnêhem ûḇᵉnê bᵉnêhem kaʾăšer ʿāśû ʾăḇōtām hēm ʿōśîm ʿaḏ hayyôm hazzeh</em>, &lsquo;these nations feared YHWH and also served their carved images. Their children did likewise, and their children&rsquo;s children — as their fathers did, so they do to this day&rsquo; — marks the Samaritan synthesis as intergenerationally transmitted. The phrase <em>ʿaḏ hayyôm hazzeh</em> (&lsquo;to this day&rsquo;) is the Deuteronomistic historian&rsquo;s marker of a condition that persists into the narrator&rsquo;s own time. The woman at the well in John 4:20 — &lsquo;our fathers worshipped on this mountain&rsquo; (Gerizim) — is the NT&rsquo;s voice of the &lsquo;to this day&rsquo; syncretism, still practicing a YHWH-worship whose legitimacy is contested. Jesus&rsquo;s response (John 4:23-24) addresses both the Samaritan syncretism of 2 Kgs 17 and the Jerusalem-temple localism: &lsquo;true worshippers will worship the Father in spirit and truth, for the Father is seeking such people to worship him.&rsquo; The <em>ʿaḏ hayyôm hazzeh</em> of the Samaritan double-service is answered by Jesus&rsquo;s <em>erchesthai hōra kai nyn estin</em> (John 4:23: &lsquo;the hour is coming, and is now here&rsquo;) — the present eschatological moment that transcends the Gerizim/Jerusalem division and the double-service problem alike.</p>"
  }
}

def main():
    c = load_comm('mkt-original', '2kings')
    merge_comm(c, ORIGINAL)
    save_comm('mkt-original', '2kings', c)
    count = sum(len(v) for v in ORIGINAL.values())
    print(f'2kings mkt-original: wrote {count} verses across ch 15-17')

if __name__ == '__main__':
    main()
