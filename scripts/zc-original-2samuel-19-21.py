"""
MKT Original Commentary — 2 Samuel chapters 19–21
Run: python3 scripts/zc-original-2samuel-19-21.py
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
  "19": {
    "23": "<p>David's declaration to Shimei: <em>lŏʼ tāmūt</em> — 'you shall not die.' The three-word royal pardon is the covenantal counterpart to the death sentence: just as the king can decree <em>môt yāmūt</em> (he shall surely die), the king can speak <em>lŏʼ tāmūt</em> (you shall not die). The formula appears in YHWH's direct pardon speech: in 2 Sam 12:13 Nathan tells David <em>gam YHWH heʿeăbír ḥaṭṭāʾẑḿkā lŏʼ tāmūt</em> ('YHWH has put away your sin; you shall not die'), making the royal pardon of Shimei a deliberate echo of the divine pardon of David. The king who was himself pardoned by the divine king now extends pardon to one who deserved death. This is the OT narrative pattern of the pardoned pardoner — the pattern that underlies the Parable of the Unforgiving Servant (Matt 18:23-35): the servant who was forgiven ten thousand talents and then refused to forgive a hundred denarii has violated the logic of the <em>lŏʼ tāmūt</em> economy. David's pardon of Shimei demonstrates the opposite: the recipient of royal grace extending royal grace.</p>"
  },
  "20": {
    "1": "<p>Sheba's rebellion-cry: <em>ʾên lānû ḥēleq bᵉdāwiḏ wəlōʾ naḥălāh lānû bᵉben yišay</em> — 'we have no portion (<em>ḥēleq</em>) in David, and we have no inheritance (<em>naḥălāh</em>) in the son of Jesse.' The paired nouns <em>ḥēleq</em> (portion, lot, share) and <em>naḥălāh</em> (inheritance, allotted land) are the covenant-territorial vocabulary of the Promised Land distribution — each tribe's <em>ḥēleq</em> and <em>naḥălāh</em> was their divinely apportioned share in the covenant land. To say 'we have no <em>ḥēleq</em> in David' is to formally renounce membership in the Davidic covenant — the act of self-exclusion from the covenantal community. This formula is repeated verbatim in 1 Kgs 12:16 at the northern kingdom's secession: it becomes the fixed idiom of covenant rupture and dissolution of the Davidic union. In the NT, to have 'no portion in David' becomes the language of inclusion or exclusion from the Davidic Messiah's kingdom (John 13:8: Jesus replies 'if I do not wash you, you have no portion [<em>meros</em>, the LXX term for <em>ḥēleq</em>] with me').</p>"
  },
  "21": {
    "1": "<p>The three-year famine is traced to Saul's unresolved bloodguilt against the Gibeonites: <em>ʾel šāʾūl wỽʾel bît hadāmîm ʾal ʾăšer hēmît ʾet haggibʾōnîm</em>. The Gibeonites were covenant partners with Israel from the days of Joshua (Josh 9:15-27) — an irrevocable <em>bỽrît</em> sworn in YHWH's name. Saul's massacre violated an oath sworn to YHWH, and the land bears the guilt of the unresolved covenant violation a generation later. The theological principle that unresolved bloodguilt (<em>dāmîm</em>) pollutes the land is grounded in Num 35:33: 'bloodshed pollutes the land, and no atonement can be made for the land for the blood that is shed in it, except by the blood of the one who shed it.' Covenant violations do not dissolve with time but await resolution. The NT carries this logic into the atonement: the accumulated bloodguilt of humanity requires not the passage of time but the shedding of the blood of the One in whom all covenant violations converge (Heb 9:22: 'without the shedding of blood there is no forgiveness').</p>",
    "17": "<p>After David nearly dies in battle, his men vow: <em>lŏʼ tēṣʾēʼ ʾwôd ʾittanū lammilḥāmāh wỽlŏʼ tỽkabbîh ʾet nēr yiśrāʾēl</em> — 'you shall not go out with us to battle anymore, lest you quench the lamp (<em>nēr</em>) of Israel.' The phrase <em>nēr yiśrāʾēl</em> (lamp of Israel) is the narrative's first explicit royal metaphor for the king as the source of national light and continuity. The <em>nēr</em> metaphor for the Davidic dynasty appears in 1 Kgs 11:36, 15:4, and 2 Kgs 8:19 — the lamp that YHWH has kept burning in Jerusalem as the sign of covenantal continuity. In the prophetic tradition, the light-bringer becomes explicitly messianic: Isa 9:2 ('the people who walked in darkness have seen a great light') and 42:6 ('I will make you a light for the nations'). Jesus's self-identification as the Light of the world (John 8:12) is the ultimate declaration that the <em>nēr yiśrāʾēl</em> motif reaches its fulfillment not in any son of David who can be killed in battle, but in the Son of David whose light is inextinguishable.</p>"
  }
}

def main():
    c = load_comm('mkt-original', '2samuel')
    merge_comm(c, ORIGINAL)
    save_comm('mkt-original', '2samuel', c)
    count = sum(len(v) for v in ORIGINAL.values())
    print(f'2samuel mkt-original: wrote {count} verses across ch 19-21')

if __name__ == '__main__':
    main()
