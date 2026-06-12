"""
MKT Original Commentary — 2 Samuel chapters 8–11
Run: python3 scripts/zc-original-2samuel-8-11.py

Ch8: David's administration of justice and equity (mišpāṭ ûṣᵉdāqāh) — the royal ideal;
     Moab measured with a line — ḥebel as measure of fate
Ch9: ḥesed toward Mephibosheth — the crippled man at the king's table as covenant type
Ch10: Joab's battle speech — human faithfulness + divine sovereignty in holy war
Ch11: wayyirʾ wayyišlaḥ — the lust sequence echoing Genesis 3;
      Uriah's loyal letter-bearing as the deepest irony of the chapter

Key Hebrew terms:
- mišpāṭ ûṣᵉdāqāh (8:15): the royal justice pair — Ps 72:1-2, Isa 9:7
- ḥesed (9:1,7): covenantal loyalty beyond obligation
- wayyirʾ wayyišlaḥ (11:3-4): the see-send sequence of lust-action
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
  "8": {
    "15": "<p>The summary of David's reign: <em>wayyimlōk dāwiḏ ʿal kol yiśrāʾēl wayhî dāwiḏ ʿōśeh mišpāṭ ûṣᵉdāqāh lᵉḵol ʿammô</em> — 'David reigned over all Israel and David administered justice (<em>mišpāṭ</em>) and righteousness (<em>ṣᵉdāqāh</em>) to all his people.' The paired nouns <em>mišpāṭ ûṣᵉdāqāh</em> constitute the OT's standard formulation of the royal ideal: the king's obligation to administer the covenantal legal order (<em>mišpāṭ</em>) and the relational right-standing that supports it (<em>ṣᵉdāqāh</em>). This pair appears in the Davidic Psalms' royal ideal (Ps 72:1-2: 'Give the king your <em>mišpāṭîm</em>, O God, and your <em>ṣᵉdāqāh</em> to the royal son'), in Isaiah's messianic oracle (Isa 9:7: 'to uphold it with <em>mišpāṭ</em> and with <em>ṣᵉdāqāh</em>'), and in Jeremiah's messianic title (Jer 23:5: 'the Branch of righteousness who shall execute <em>mišpāṭ</em> and <em>ṣᵉdāqāh</em>'). The formula in 2 Sam 8:15 is not merely administrative summary but the theological claim that David's reign embodied the royal ideal that will find its perfect realization in the Davidic Messiah whose justice will be universal and eternal.</p>"
  },
  "9": {
    "7": "<p>David's words to Mephibosheth — <em>ʾal tîrāʾ kî ʾāśôh ʾāśeh ʿimmᵉḵā ḥesed bᵉʿăḇûr yôhônātān ʾāḇîḵā wᵉhăšiḇōtî lᵉḵā ʾet kol śᵉdeh šāʾûl ʾāḇîḵā wᵉʾattāh tōʾkal leḥem ʿal šulḥānî tāmîḏ</em> — 'Do not fear, for I will surely show you <em>ḥesed</em> for the sake of your father Jonathan, and I will restore to you all the land of Saul your grandfather, and you shall eat at my table always' — is the most concentrated narrative embodiment of <em>ḥesed</em> in the Samuel narratives. <em>Ḥesed</em> is the Hebrew term for the covenant loyalty that goes beyond legal obligation — the love that acts for the benefit of the covenant partner even when no reciprocal benefit is possible. Mephibosheth has nothing to offer: he is crippled in both feet (v3), the last survivor of the household that attempted to kill David, an object of potential political threat rather than benefit. David's <em>ḥesed</em> to Mephibosheth is motivated purely by his covenant with Jonathan (1 Sam 20:14-17), not by any calculation of advantage. The phrase <em>ʾal tîrāʾ</em> ('do not fear') — spoken to the one who falls on his face before the king — is the standard formula of divine reassurance: the same formula YHWH speaks to the patriarchs. The table-fellowship that follows is the covenant sign: the lame man eating at the king's table as equals is the OT image that Jesus will deploy as the image of the kingdom banquet (Luke 14:21: 'Go out quickly to the streets and lanes of the city and bring in the poor and crippled and blind and lame').</p>"
  },
  "10": {
    "12": "<p>Joab's speech to Abishai before the double-front battle is the OT's most succinct statement of the theology of holy-war courage: <em>ḥăzaq wᵉniḥăzaq bᵉʿaḏ ʿammēnû ûbᵉʿaḏ ʿārê ʾelōhênû waYHWH yaʿăśeh haṭṭôḇ bᵉʿênāyw</em> — 'Be strong, and let us be strong for the sake of our people and for the sake of the cities of our God; and YHWH will do what seems good in his eyes.' The speech pairs maximal human effort (<em>ḥăzaq</em> — the same verb used for David strengthening himself at Ziklag, 1 Sam 30:6) with maximal divine freedom: Joab does not claim to know the outcome but fully commits to the action. The theological grammar is: our faithfulness is the human dimension, YHWH's judgment is the divine dimension, and neither is collapsed into the other. The <em>ṭôḇ bᵉʿênāyw</em> ('what is good in his eyes') is the formula for divine sovereign discretion — the same formula that governs Eli's submission (1 Sam 3:18), Hannah's release to YHWH (1 Sam 1:23), and Paul's missionary freedom (1 Cor 4:4: 'it is the Lord who judges me'). Joab's battle theology is not fatalism but covenant confidence: fight fully, trust the outcome to YHWH.</p>"
  },
  "11": {
    "2": "<p>The sequence that opens David's fall: <em>wayyarʾ ʾiššāh rōḥeṣet</em> — 'he saw a woman bathing.' The three-step sequence of lust-to-sin that follows — seeing, sending, taking — mirrors the Genesis 3:6 pattern: Eve saw (<em>wattarʾ</em>), desired, and took (<em>wattiqaḥ</em>). The verb <em>rāʾāh</em> (to see) is theologically loaded in the David narrative: YHWH looks on the heart while humans look on the outward appearance (1 Sam 16:7 — the same verb root). David's kingship began with YHWH correcting his seeing; it collapses when David's seeing reverts to the human pattern of desire. James 1:14-15 maps the identical sequence: 'each person is tempted when they are lured and enticed by their own desire; then desire when it has conceived gives birth to sin, and sin when it is fully grown brings forth death.' The narrative demonstrates James's abstract principle with biographical precision: the desire conceived in v2 gives birth to adultery in v4, and brings forth the death of Uriah in v15.</p>",
    "15": "<p>The irony of the letter Uriah carries is the narrative's theological coup de grâce: <em>wayyiktōḇ bassēper ʾel yôʾāb wayyišlaḥ bəyad ûriyyāh</em> — 'he wrote in the letter to Joab and sent it by the hand of Uriah.' Uriah the Hittite — the Canaanite proselyte who is more loyal to the covenant than the covenant king — carries his own death warrant without knowing it. The compound irony: (1) Uriah's covenant loyalty (refusal to go home while the Ark is in a tent, v11) is precisely the quality that makes him exploitable; (2) David's position of covenantal authority is precisely what enables his crime; (3) the foreigner is the righteous man and the anointed is the criminal. The narrative is a theological inversion of everything the anointing of ch16 established. The phrase <em>wayyišlaḥ bəyad ûriyyāh</em> echoes the earlier <em>wayyišlaḥ dāwiḏ</em> in vv4 and 6 — the same verb of royal sending, now dispatching the loyal soldier to his death. The three-fold use of <em>šālaḥ</em> (to send) in this chapter — send for Bathsheba, send Uriah to Joab, send the letter — maps the progressive deepening of the abuse of royal power.</p>"
  }
}

def main():
    c = load_comm('mkt-original', '2samuel')
    merge_comm(c, ORIGINAL)
    save_comm('mkt-original', '2samuel', c)
    count = sum(len(v) for v in ORIGINAL.values())
    print(f'2samuel mkt-original: wrote {count} verses across ch 8-11')

if __name__ == '__main__':
    main()
