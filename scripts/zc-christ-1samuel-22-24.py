"""
MKT Christ Commentary — 1 Samuel chapters 22–24
Run: python3 scripts/zc-christ-1samuel-22-24.py

Ch22: David at Adullam — the rejected anointed gathering the outcast community;
      the Nob massacre as the innocent suffering around the anointed;
      Abiathar's escape as the priestly access preserved for the fugitive king
Ch23: Jonathan's final strengthening visit — the intercessor-friend at the nadir;
      David's deliverance at the Rock of Escape
Ch24: David refuses to grasp the kingdom prematurely — the anti-grasping pattern;
      the forensic self-entrusting to the divine judge; Saul's confession of the
      righteous sufferer's vindication
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
  "22": {
    "2": "<p>The community that gathers at Adullam is described in three categories: those in <em>māṣôq</em> (distress/straits), those with a creditor (<em>nāšāʾ</em>), and the <em>mar nepeš</em> (bitter of soul/desperate). This is the social portrait of the rejected and marginalized — those for whom the existing order has no place, gathered around the rejected anointed. David's Adullam community is the narrative type of the community Jesus gathers: 'Come to me, all who labor and are heavy laden, and I will give you rest' (Matt 11:28); the beatitudes of Matt 5:3-6 address precisely the <em>māṣôq</em>, the <em>nāšāʾ</em>, the <em>mar nepeš</em> — the poor in spirit, those who mourn, the meek, those who hunger. As David at Adullam was not yet on the throne but was already the king-in-hiding who drew the outcasts to himself, so Christ in his earthly ministry is the king-in-exile gathering those whom the existing religious order has excluded, building the community of the coming kingdom before its public establishment.</p>",
    "20": "<p>Abiathar's escape with the ephod from the Nob massacre creates the typological connection between the slaughter of the priestly community and the preservation of divine access for the fugitive anointed. The Nob massacre — Doeg killing 85 priests of YHWH — is the most violent act of the pre-exilic narrative against the sacred ministers of YHWH. Yet in its midst, the one who survives brings the means of covenantal inquiry to David. Matthew draws the explicit typological parallel in 2:16-18: Herod's slaughter of the innocents around the newly revealed king mirrors the Nob massacre, and Rachel weeping for her children (Jer 31:15) is the mourning that accompanies the birth of the anointed. In both cases, a massacre around the anointed king results in the preservation of those who serve the king's covenantal access — Abiathar with the ephod (the means of priestly inquiry) as the type of the Spirit who opens the way into the presence of God (Heb 10:19-22: access through the blood of Jesus, through the new and living way).</p>"
  },
  "23": {
    "16": "<p>Jonathan's final act of covenant friendship is described with the verb <em>ḥizzēq</em> (to strengthen, make firm): <em>wayyḥazzēq ʾet yāḏô bēlōhîm</em> — 'he strengthened his hand in God.' Jonathan comes to David at his lowest point — hunted, in the wilderness, with Saul's army closing in — and his single act is not to bring supplies or military intelligence but to strengthen David's grip on God. This is the NT ministry of intercession at its highest form. Hebrews 7:25 describes Christ's ongoing high-priestly work in identical terms: 'he always lives to make intercession for them' — the resurrected Christ perpetually <em>ḥizzēq</em>-ing the hands of his people in God. Romans 8:34 places this intercession at the right hand of the Father. Jonathan's act — coming to the fugitive anointed at his hour of need to strengthen his hand in God — is the OT narrative type of Christ's unceasing intercession for those who belong to him in the hour of their trial and despair.</p>"
  },
  "24": {
    "6": "<p>David's heart striking him for cutting the robe-hem of Saul encodes the anti-grasping theology that runs from Gen 3:6 to Phil 2:6. What David takes in the dark cave is not yet his to take — the robe-hem, as a symbol of royal authority in ANE legal practice, is not yet David's even though the kingdom has been promised to him. His conscience reacts immediately: he has symbolically appropriated what YHWH has promised but not yet given. This is the precise anti-type of the Adamic and Satanic temptations: to grasp at what God has not yet granted, to accelerate the divine timetable by force. Christ's temptation in the wilderness (Matt 4:8-10: the devil offers all the kingdoms of the world if Jesus will worship him) is the cosmic version of the Adullam cave: the shortcut to the kingdom without the cross. Jesus refuses on the same ground David refuses: not because the kingdom is not his but because the Father's means and the Father's time are not negotiable. Paul's description of the Incarnation (Phil 2:6: 'he did not count equality with God a thing to be grasped') is the definitive theological statement of what David dimly enacts in the cave: the one who has the right to all refuses to take it before the appointed time.</p>",
    "15": "<p>David's appeal to YHWH as judge — <em>YHWH yihyeh lᵉdayyān bênî ûbênêḵā</em>, 'YHWH will be judge between me and you' — and his forensic self-deprecation ('after a dead dog, after a single flea') constitute the OT's most explicit narrative enactment of the principle that 1 Peter 2:23 identifies as Christ's defining response to unjust suffering: 'when he suffered, he did not threaten; instead, he committed himself to him who judges justly.' Peter is reading David — and through David, reading Christ. The righteous sufferer who does not take vengeance but appeals to the divine judge is the prophetic portrait of Christ's passion: the one who could have called twelve legions of angels (Matt 26:53) choosing instead to commit his cause to the Father. The divine court to which David appeals is the same court to which Christ entrusts his cause; the vindication that David trusts YHWH to deliver is the resurrection that the Father grants on Easter morning — the ultimate verdict of the divine judge in favor of the righteous sufferer.</p>"
  }
}

def main():
    c = load_comm('mkt-christ', '1samuel')
    merge_comm(c, CHRIST)
    save_comm('mkt-christ', '1samuel', c)
    count = sum(len(v) for v in CHRIST.values())
    print(f'1samuel mkt-christ: wrote {count} verses across ch 22-24')

if __name__ == '__main__':
    main()
