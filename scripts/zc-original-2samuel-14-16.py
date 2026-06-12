"""
MKT Original Commentary — 2 Samuel chapters 14–16
Run: python3 scripts/zc-original-2samuel-14-16.py

Ch14: The woman of Tekoa's parable — Joab's prophetic-parable technique;
      14:14 — the most profound death-and-mercy meditation in the Succession Narrative;
      ḥāšaḇ maḥăšāḇôt: YHWH devises means to bring back the banished
Ch15: David's Mount of Olives ascent — the barefoot weeping king type;
      David's submission to divine judgment: 'let him do what seems good to him'
Ch16: Shimei's cursing — patiently bearing unjust reproach as YHWH's instrument;
      David's theological interpretation of the curse

Key Hebrew terms:
- ḥāšaḇ maḥăšāḇôt (14:14): to devise/scheme plans — the divine creative purposing
- mayyim niggārîm (14:14): spilled water that cannot be gathered — mortality image
- ḥāpēṣ (15:26): divine delight/pleasure — the vocabulary of divine favor
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
  "14": {
    "14": "<p>The woman of Tekoa's theological statement is the most concentrated mercy-meditation in the Succession Narrative: <em>kî māwet namût wayyihnû kaymayim hanniggārîm ʾārṣāh ʾăšer lōʾ yēʾāsēpû wəlōʾ yiśśāʾ ʾelōhîm nepeš wəḥāšaḇ maḥăšāḇôt lᵉbiltî yiddaḥ mimmennû niddāḥ</em> — 'we must all die; we are like water spilled on the ground that cannot be gathered up again; yet God does not take away life, but devises means (<em>ḥāšaḇ maḥăšāḇôt</em>) so that the banished one will not remain an outcast.' The image of water spilled on the ground (<em>mayyim niggārîm ʾārṣāh</em>) is one of the OT's most precise mortality metaphors: the irreversibility of death — once poured out, it cannot be reconstituted. Yet the theological turn is radical: against this irreversibility, YHWH is described as the one who <em>ḥāšaḇ maḥăšāḇôt</em> (devises plans/schemes thoughts) — the same verbal root used in Gen 50:20 ('you intended it for harm but God intended it for good'), in Jer 29:11 ('plans of peace, not of harm'), and in the Servant Song (Isa 53:4-5, where YHWH's purposes involve the suffering of the Servant to restore the banished). The woman's statement is a theological anticipation of the atonement logic: YHWH <em>ḥāšaḇ</em> — purposely devises — the means by which the banished one (<em>niddāḥ</em>, the exile/outcast) can return. The word <em>niddāḥ</em> (from <em>nādaḥ</em>, to drive away/banish) appears in the great restoration texts: Isa 11:12 ('gather the <em>nidḥê</em> of Judah'), Ezek 34:16 ('I will seek the lost and bring back the strayed'), and Mic 4:6 ('I will assemble the <em>nidḥāh</em>'). The woman's plea for Absalom becomes, in the narrator's hands, a theological statement about YHWH's redemptive purpose for the banished.</p>"
  },
  "15": {
    "26": "<p>David's submission to divine judgment in the face of Absalom's coup is the most transparent covenant-submission speech in the David narrative: <em>wᵉʾim yōʾmar kōh lōʾ ḥāpaṣtî bāḵ hinnēnî yaʿăśeh lî kaʾăšer ṭôḇ bᵉʿênāyw</em> — 'but if he says, &ldquo;I have no delight (<em>ḥāpēṣ</em>) in you,&rdquo; here I am; let him do to me what seems good (<em>ṭôḇ</em>) in his eyes.' The vocabulary is theologically precise: <em>ḥāpēṣ</em> (to delight/take pleasure in) is the word used in Isa 53:10 ('it pleased YHWH to crush him') and in Ps 22:8 ('let him deliver him, for he delights in him') and in Ps 18:19 ('he rescued me because he delighted in me'). To say 'if YHWH has no <em>ḥāpēṣ</em> in me' is to surrender the very ground of covenant confidence — the divine favor that was the basis of the anointing. David's submission is not despair but naked trust: even if the anointing is revoked, even if the covenantal delight is withdrawn, 'here I am' (<em>hinnēnî</em>) — the same word of covenant availability spoken by Abraham (Gen 22:1), Isaiah (Isa 6:8), and Samuel (1 Sam 3:4). The conditional surrender (<em>hinnēnî</em> even if <em>lōʾ ḥāpaṣtî bāḵ</em>) is the OT's nearest approach to Gethsemane: 'not my will but yours be done' (Luke 22:42).</p>",
    "30": "<p>David's ascent of the Mount of Olives: <em>wədāwiḏ ʿōleh bᵉmaʿăleh hazzeytîm ʿōleh ûḇōḵeh wərōʾš lô ḥāpûy wəhû hōlēk yāḥēp</em> — 'David went up the ascent of the Mount of Olives, weeping as he went, barefoot and with his head covered.' The geography is the same ridge that descends into the Kidron Valley and rises toward Jerusalem — the same mountain from which Jesus made his triumphal entry (Luke 19:28-37) and from which he wept over Jerusalem (Luke 19:41). David ascending barefoot and weeping, driven from Jerusalem by his own son's rebellion, is the precise narrative type of Christ's suffering in the same geography. The head covering (<em>rōʾš ḥāpûy</em>) is the sign of mourning and shame — the posture of the condemned and humiliated. The Passion narrative places Jesus at this same ridge, weeping (Luke 19:41) and sweating blood (Luke 22:44), stripped of honor, about to be betrayed by one of his own. The Davidic and Christological descents/ascents share the same mountain, the same tears, and the same pattern of rejection-before-restoration.</p>"
  },
  "16": {
    "10": "<p>David's response to Abishai's request to execute Shimei for his cursing is the Succession Narrative's most counterintuitive theological statement: <em>mah lî wālāḵem bᵉnê ṣᵉrûyāh kî yᵉqallēl waYHWH ʾāmar lô qallēl ʾet dāwiḏ</em> — 'What have I to do with you, you sons of Zeruiah? Let him curse, for YHWH has said to him, &ldquo;Curse David.&rdquo;' David's interpretation of the unjust curse as YHWH's instrument (<em>YHWH ʾāmar lô qallēl</em>) is not fatalism but covenantal theology: the same theological logic by which Joseph interpreted his brothers' betrayal (Gen 50:20), by which Job refused to curse God in suffering (Job 1:21), and by which Peter interprets the crucifixion (Acts 2:23: 'this Jesus, delivered up according to the definite plan and foreknowledge of God'). The suffering king who refuses to strike down his curser exercises the same patience that 1 Pet 2:23 ascribes to Christ: 'when he suffered, he did not threaten.' David under Shimei's curse is an enacted type of the NT theology of patiently bearing reproach as YHWH's purposeful instrument.</p>"
  }
}

def main():
    c = load_comm('mkt-original', '2samuel')
    merge_comm(c, ORIGINAL)
    save_comm('mkt-original', '2samuel', c)
    count = sum(len(v) for v in ORIGINAL.values())
    print(f'2samuel mkt-original: wrote {count} verses across ch 14-16')

if __name__ == '__main__':
    main()
