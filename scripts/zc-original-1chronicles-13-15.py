"""
MKT Original Commentary — 1 Chronicles chapters 13–15
Run: python3 scripts/zc-original-1chronicles-13-15.py

The pāraṣ (breach/break-through) leitmotif across chs 13-15:
- 13:11: Perez-uzzah (pereṣ ʿuzzāh) — YHWH's unauthorized breach
- 14:11: Baal-perazim — YHWH breaks through David's enemies
- 15:13: pāraṣ explained — the Ark-cart's violation caused YHWH's outbreak
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
  "13": {
    "11": "<p>The place-name <em>pereṣ ʿuzzāh</em> (&lsquo;Breach of Uzzah&rsquo;) that David gives to the threshing floor of Chidon encodes a double irony. The name <em>ʿuzzāh</em> derives from the root <em>ʿōz</em> (strength, might) — the man&rsquo;s name literally means &lsquo;YHWH&rsquo;s strength&rsquo; or simply &lsquo;strength.&rsquo; Uzzah is killed at the moment of deploying that strength: reaching out (<em>wayyišlaḥ yādô</em>) to steady the Ark. The verb <em>pāraṣ</em> (to breach, break out, burst forth) — <em>wayyippeṣ bô ʾelōhîm</em>, &lsquo;God broke out against him&rsquo; — names the violent, boundary-crossing force of divine holiness when it encounters unauthorized contact. The <em>pereṣ</em> (breach) that kills Uzzah is the Ark asserting its own holiness against human management. The same verb <em>pāraṣ</em> appears in 14:11 (YHWH breaks through David&rsquo;s enemies = Baal-perazim) and 15:13 (David&rsquo;s explanation of the Uzzah incident: <em>pāraṣ bānû YHWH</em>, &lsquo;YHWH broke out against us&rsquo;). The Chronicler deliberately uses this root across all three chapters to create a theological signature: <em>pāraṣ</em> is YHWH&rsquo;s characteristic verb — he breaks boundaries, whether against enemies (14:11) or against unauthorized approach (13:11). The Ark-cart episode is not merely a liturgical error; it is a failure to reckon with the pāraṣ-character of YHWH&rsquo;s holiness.</p>"
  },
  "14": {
    "11": "<p>David&rsquo;s name for the site of his victory over the Philistines — <em>baʿal pᵉrāṣîm</em>, &lsquo;Lord of breakings-through/breaches&rsquo; — uses the same root <em>pāraṣ</em> that appeared in 13:11 (&lsquo;Perez-uzzah&rsquo;) and will reappear in 15:13. David&rsquo;s own gloss is: <em>pāraṣ ʾelōhîm ʾet ʾōyᵉḇay bᵉyāḏî kᵉpereṣ mayim</em>, &lsquo;God has broken through my enemies by my hand like a breaking-through of water.&rsquo; The image is a flash flood — the <em>pereṣ mayim</em> (water-breach) being the sudden, irresistible bursting of a dam or a wadi in flood. The Philistines&rsquo; gods are abandoned on the field (v12) and burned — the decisive reversal from Eben-ezer (1 Sam 4) where the Ark was captured by the Philistines. Now the Ark is safely housed in Jerusalem (ch13 having failed; ch15 will succeed) and YHWH&rsquo;s <em>pāraṣ</em> falls on the Philistines instead. The Chronicler&rsquo;s placement of the Baal-perazim victory between the two Ark-procession accounts (ch13: failure; ch15: success) is a theological bracket: the same God who broke out against Uzzah (for inappropriate approach) breaks through the Philistines (for encroachment on Israel). <em>Pāraṣ</em> is not capricious — it is YHWH&rsquo;s consistent boundary-enforcement, whether the boundary being crossed is ritual or national.</p>"
  },
  "15": {
    "13": "<p>David&rsquo;s retrospective explanation of the Uzzah disaster — <em>kî lōʾ dᵉrašnûhû kammišpāṭ</em>, &lsquo;because we did not seek him according to the ordinance&rsquo; — introduces the specific legal failure: the Ark was carried on a cart (<em>ʿāgālāh</em>, 13:7) rather than on poles by Levites (Num 4:15; 7:9). The verb <em>pāraṣ</em> appears again: <em>pāraṣ bānû YHWH ʾelōhênû</em>, &lsquo;YHWH our God broke out against us.&rsquo; The Chronicler&rsquo;s use of <em>pāraṣ</em> in all three chapters (13:11; 14:11; 15:13) is structural: the Uzzah incident (unauthorized <em>pāraṣ</em>) is explained by David in 15:13 using the same vocabulary, with the Baal-perazim victory (authorized <em>pāraṣ</em>) sandwiched between as a theological contrast. The Philistines&rsquo; gods were &lsquo;carried away&rsquo; (nāśāʾ) and burned (14:12) — the Ark must be &lsquo;carried&rsquo; (nāśāʾ) by the Levites (15:2, 15) on poles, not transported like cargo. The linguistic echo is deliberate: the verb <em>nāśāʾ</em> (to carry, lift, bear) governs both episodes, distinguishing the proper bearing of the Ark from the improper transport. The <em>kammišpāṭ</em> (&lsquo;according to the ordinance&rsquo;) that David names as missing is the Mosaic regulation the Ark-cart circumvented — the failure was not ignorance but inattentiveness to the specific form YHWH had ordained.</p>"
  }
}

def main():
    c = load_comm('mkt-original', '1chronicles')
    merge_comm(c, ORIGINAL)
    save_comm('mkt-original', '1chronicles', c)
    count = sum(len(v) for v in ORIGINAL.values())
    print(f'1chronicles mkt-original: wrote {count} verses across ch 13-15')

if __name__ == '__main__':
    main()
