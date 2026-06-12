"""
MKT Context Commentary — 1 Samuel chapters 22–24
Run: python3 scripts/zc-context-1samuel-22-24.py

Ch22: David at Adullam; the Nob massacre — Doeg the Edomite kills 85 priests;
      Abiathar escapes with the ephod; Psalms 52 and 34 as companions
Ch23: David at Keilah and the Wilderness of Ziph; Jonathan's last visit;
      the ephod inquiry; Ziph betrayal and divine protection
Ch24: David at En Gedi; the first sparing of Saul; the garment-cutting;
      David's legal-theological argument; Psalm 57 as companion

Geographical/ANE context:
- Adullam (22:1): Tell esh-Sheikh Madhkur in the Shephelah, commanding valley
- Nob (22:9): the priestly city north of Jerusalem, now a refugee sanctuary
- Keilah (23:1): Tell Qila in the lowland foothills of Judah
- En Gedi (24:1): an oasis on the western Dead Sea shore — Ain Jidi
- These chapters form the 'wilderness of Judah' period of David's fugitive years,
  corresponding to several 'cave' and 'wilderness' Psalms (34, 52, 54, 57, 63, 142)
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

CONTEXT = {
  "22": {
    "1": "<p>The cave of Adullam (<em>meʿārat ʿădullām</em>) is identified with Tell esh-Sheikh Madhkur in the Shephelah (the Judahite foothills), approximately 13 km southwest of Bethlehem. The area commanded several ancient routes between the Judahite highlands and the coastal plain. Adullam is mentioned in Josh 15:35 as a Judahite city and appears in the Amarna Letters (14th century BCE) under the Akkadian form <em>Addulama</em>. The cave complex in the limestone formations of the Shephelah provided natural fortifications. David's gathering of 400 men in 'distress' (<em>māṣôq</em>), 'debt' (<em>nōšeʾ</em>), and 'bitterness of soul' (<em>mar nepeš</em>) — the three categories of social marginalization — creates a community that anticipates the social makeup of Jesus's following: the poor, the excluded, the indebted. The Psalms 34 (superscription: 'when he feigned madness before Abimelech') and 142 ('A Maskil of David, when he was in the cave') are associated with this period.</p>",
    "9": "<p>Doeg the Edomite's denunciation of Ahimelech to Saul initiates the Nob massacre — the single most catastrophic act of violence against the Israelite priesthood in the pre-exilic period. Doeg (<em>dôʾēg</em>, 'anxious/fearful') is identified as Saul's chief herdsman (<em>ʾăbîr hārōʿîm</em>) and an Edomite — a foreigner in the Israelite court who is willing to do what Saul's own soldiers refuse (v17: the king's servants would not kill the priests). Doeg's act is the fulfillment of the 'man of God' oracle against Eli's house (2:31-36): the priests of Nob are descendants of Eli's line through Phinehas, and their slaughter completes the judgment. The Psalm 52 superscription explicitly links this psalm to Doeg: 'when Doeg the Edomite came and told Saul and said to him, David has come to the house of Ahimelech.' Ps 52 is a meditation on the use of the tongue as a weapon of destruction — the context being Doeg's deadly informing.</p>",
    "20": "<p>Abiathar's escape with the ephod is narratively crucial: he brings to David the only remaining means of legitimate divine oracle. The ephod (<em>ʾēpôḏ</em>) used for inquiry is the priestly vestment containing the Urim and Thummim (the lot-oracle devices), distinct from the golden ephod of Gideon (Judg 8:27). With the destruction of the Nob priesthood, Abiathar and the ephod become David's exclusive access to YHWH's guidance during the wilderness years (23:6, 9-12; 30:7-8). The pattern — the last legitimate priest with the last legitimate means of divine inquiry attached to the fugitive anointed king — is the narrative's way of showing that YHWH's official covenantal apparatus has transferred from Saul's court to David's camp, even before David has any political power.</p>"
  },
  "23": {
    "1": "<p>Keilah (<em>qᵉʿîlāh</em>, modern Tell Qila) is a Judahite city in the Shephelah lowlands, approximately 8 km north of Lachish. Its identification is secure from both the LXX transliteration and the site archaeology. The Philistine raid on Keilah's threshing floors at harvest time is consistent with the ANE pattern of seasonal raids against agricultural communities — the threshing floors (<em>gōrānôt</em>) are the most economically vulnerable moment of the agricultural year, when the season's grain is exposed and concentrated. David's decision to defend Keilah despite his men's reluctance, and confirmed by double ephod inquiry (vv2, 4), is the first time in the narrative that the fugitive David acts in the mode of a judge — protecting the covenant people from their enemies. His subsequent withdrawal when Keilah's citizens would have handed him to Saul (vv11-12) maps the pattern of the rejected deliverer whose service is not recognized by those he rescues.</p>",
    "18": "<p>Jonathan's final visit to David at Horesh in the Wilderness of Ziph — the last meeting of the two covenant partners — is one of the most theologically condensed scenes in the narrative: <em>wayyāqom yôhônātān ben šāʾûl wayyēlek ʾel dāwiḏ ḥōrᵉšāh wayyḥazzēq ʾet yāḏô bēlōhîm</em> — 'Jonathan rose and went to David at Horesh and strengthened his hand (<em>ḥizzaq yāḏ</em>) in God.' The phrase <em>ḥizzēq yāḏ bēlōhîm</em> (to strengthen a hand in God) is a rare idiom meaning to encourage someone's faith and commitment — the covenant partner acting as the means of divine encouragement. Jonathan's final words — 'you shall be king over Israel, and I shall be next to you' (v17) — are his covenant acknowledgment of David's election. No subsequent meeting between them is recorded; the next we hear of Jonathan is his death at Jezreel (31:2). This is thus the valediction of the most remarkable friendship in the OT.</p>"
  },
  "24": {
    "3": "<p>En Gedi (<em>ʿên geḏî</em>, 'spring of the kid/goat') is the most dramatic oasis on the western shore of the Dead Sea, approximately 50 km southeast of Jerusalem. The site sits at the foot of limestone cliffs rising 300-500 meters, with abundant springs feeding a rich vegetation zone — fig trees, palms, balsam — surrounded by the arid Judean wilderness. The area contains numerous large caves in the cliffsides, consistent with the narrative of Saul entering the cave to relieve himself while David and his men lurk in its recesses. Archaeological excavations at Tel Goren (the lower site) and ʿEin Gedi (the spring area) confirm occupation throughout the Iron Age. The Psalm 63 superscription reads: 'A Psalm of David, when he was in the Wilderness of Judah' — most naturally associated with this En Gedi period of David's fugitive years. The Wilderness of Judah/En Gedi region was also the setting for John the Baptist's ministry (Matt 3:1-6) — the same geography of prophetic withdrawal from the religious establishment.</p>",
    "4": "<p>The cave encounter's legal dimension: David's men urge him to kill Saul with the theological-opportunistic argument — &lsquo;This is the day that YHWH said to you, &ldquo;Behold, I will give your enemy into your hand&rdquo;&rsquo; — a claim to prophetic authorization not found in the narrative record. David cuts the corner of Saul's robe (<em>kānat hammᵉʿîl</em>) instead, then his heart strikes him for this act (v5). The cutting of the robe corner is not merely symbolic: in ANE legal practice, a garment hem or corner (<em>kānat</em>) could represent personal authority and legal identity — cuneiform texts show contracts sealed with the hem of a garment impressed in clay. David's cutting of Saul's robe-hem is a legal appropriation of royal authority, which is why it troubles him: he has symbolically taken what he has not yet been given. His subsequent speech to Saul (vv9-15) is a formal legal argument for his own innocence — a forensic self-defense before the king.</p>",
    "14": "<p>David's closing forensic argument to Saul: <em>ʾaḥărê mî yāṣāʾ melek yiśrāʾēl ʾaḥărê mî ʾattāh rōḏēp</em> — 'After whom has the king of Israel come out? After whom are you pursuing? After a dead dog! After a single flea!' The self-deprecation formula (<em>keleb mēt</em>, dead dog; <em>parʿōš ʾeḥāḏ</em>, a single flea) is an ANE diplomatic idiom for humility before a superior — it appears in the Amarna Letters where Canaanite vassals address Pharaoh using identical language. The reference to YHWH as the judge between them (v15 — <em>YHWH yihyeh lᵉdayyān</em>) invokes the formal legal structure of covenant dispute: appealing to the divine suzerain rather than taking personal vengeance is the canonical form of covenant faithfulness under unjust treatment. David becomes the model for NT teaching on patient endurance under unjust suffering (1 Pet 2:23 — 'he committed himself to him who judges justly').</p>"
  }
}

def main():
    c = load_comm('mkt-context', '1samuel')
    merge_comm(c, CONTEXT)
    save_comm('mkt-context', '1samuel', c)
    count = sum(len(v) for v in CONTEXT.values())
    print(f'1samuel mkt-context: wrote {count} verses across ch 22-24')

if __name__ == '__main__':
    main()
