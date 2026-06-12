"""
MKT Christ Commentary — 2 Samuel chapters 8–11
Run: python3 scripts/zc-christ-2samuel-8-11.py

Ch8:  mišpāṭ ûṣᵉdāqāh — David's royal justice formula as Messianic prototype
Ch9:  Mephibosheth at the king's table — the great banquet / adoptive sonship type
Ch11: 'wife of Uriah' — the Bathsheba-Uriah scandal in the Messianic genealogy

Typological links:
- 8:15 → Jer 23:5-6; Isa 9:7; Rev 19:11 — Davidic justice → Messianic righteousness
- 9:7  → Luke 14:21; Luke 22:30; Eph 2:12-13 — ḥeseḏ table-fellowship / banquet type
- 9:13 → John 1:12; Gal 4:5-7 — lameness + royal table = adoption before wholeness
- 11:3 → Matt 1:6 — 'wife of Uriah' in the genealogy; grace through genealogical scandal
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
    "15": "<p>The narrator&rsquo;s summary of David&rsquo;s reign — <em>wayhî dāwiḏ ʿōśeh mišpāṭ ûṣᵉdāqāh lᵉkol ʿammô</em>, &lsquo;David administered justice and equity to all his people&rsquo; — is the OT&rsquo;s royal ideal stated in its fullest form, and it is also a prototype that survives its historical embodiments as a Messianic promise. The <em>mišpāṭ ûṣᵉdāqāh</em> formula appears verbatim in the central Messianic oracle of the prophets: Jer 23:5-6 &lsquo;I will raise up for David a righteous Branch (<em>ṣemaḥ ṣaddîq</em>) who shall reign as king and deal wisely, and shall execute justice and righteousness (<em>mišpāṭ ûṣᵉdāqāh</em>) in the land. And this is the name by which he will be called: YHWH is our righteousness (<em>YHWH ṣidqēnû</em>).&rsquo; The Messianic branch does not merely practice the formula but embodies it as a personal name — the king&rsquo;s righteousness and the people&rsquo;s righteousness become identical. Isa 9:7 places the same formula in the eternal Messianic kingdom: &lsquo;with justice and righteousness (<em>bᵉmišpāṭ ûbᵉṣᵉdāqāh</em>) from this time forth and forevermore.&rsquo; Rev 19:11 closes the trajectory: the rider on the white horse judges &lsquo;in righteousness (<em>en dikaiosynē</em>)&rsquo; — the final administration of what the Davidic formula required. The narrative irony of 2 Samuel is that David himself will fail catastrophically by this standard (ch11): the king who administered justice for all his people will commit the supreme injustice against Uriah. The formula survives David&rsquo;s violation of it as a promise pointing beyond David to the one who would be <em>YHWH ṣidqēnû</em> — not merely an administrator of righteousness but its source.</p>"
  },
  "9": {
    "7": "<p>David&rsquo;s promise to Mephibosheth — <em>lōʾ tîrāʾ kî ʿāśōh ʾeʿeśeh ʿimmᵉḵā ḥeseḏ biʿăḇûr yᵉhônātān ʾāḇîḵā</em>, &lsquo;do not fear, for I will surely show you kindness for the sake of your father Jonathan&rsquo; — is one of the most typologically dense scenes in the Davidic narrative. Three elements converge: (1) <em>ḥeseḏ</em> (covenant-loyalty) extended to the one who has no claim on it, (2) inheritance restored (<em>wᵉhašiḇōtî lᵉḵā ʾet kol śᵉdēh šāʾûl</em>), and (3) permanent table-fellowship (<em>tāmîd</em>, &lsquo;always&rsquo;). Mephibosheth arrives crippled in both feet (v3), summoned from Lo-debar (&lsquo;no pasture&rsquo; — the place of nothing), with every reason to fear political execution as a rival claimant. What he receives instead is <em>ḥeseḏ</em> grounded in a prior covenant relationship he did not himself make. This is the formal structure of the gospel: those brought to the Messianic table are brought on the basis of a covenant made between another and the King, not on their own merit or wholeness. Luke 14:21 consciously echoes this scene: &lsquo;go out quickly to the streets and lanes of the city and bring in the poor and crippled and blind and lame (<em>ptōchous kai anapeirous kai typhlous kai chōlous</em>).&rsquo; Luke 22:30 is the eschatological <em>tāmîd</em>: &lsquo;that you may eat and drink at my table in my kingdom.&rsquo; Eph 2:12-13 supplies the theological structure: those who were &lsquo;strangers to the covenants of promise, having no hope and without God in the world&rsquo; are brought near &lsquo;by the blood of Christ&rsquo; — the <em>ḥeseḏ</em> of a covenant extended across the gap of unworthiness.</p>",
    "13": "<p>The narrator&rsquo;s closing statement of the Mephibosheth episode — <em>wayyēšeḇ mᵉpîḇōšet bîrûšālaim kî ʿal šulḥan hammelek tāmîd hûʾ ʾōḵēl wᵉhûʾ pissēaḥ šᵉtê raglāyw</em>, &lsquo;so Mephibosheth lived in Jerusalem, for he ate at the king&rsquo;s table always; now he was lame in both feet&rsquo; — juxtaposes permanent table-honor and permanent lameness without resolving the tension. His lameness is not healed; it is noted alongside his station at the royal table. This juxtaposition is the typological key: adoption precedes transformation. Mephibosheth does not receive wholeness as the condition of his welcome; he receives <em>ḥeseḏ</em> while still broken, and the narrative preserves the brokenness as a permanent marker of his identity at the table. Verse 11b&rsquo;s statement that David treated him &lsquo;like one of the king&rsquo;s sons&rsquo; (<em>kᵉʾaḥaḏ mibbanê hammelek</em>) applies the adoption category: not a servant, not a tolerated guest, but a son. Gal 4:5-7 is the NT formal equivalent: &lsquo;so that we might receive adoption as sons... so you are no longer a slave, but a son, and if a son, then an heir through God.&rsquo; John 1:12: &lsquo;to all who did receive him... he gave the right to become children of God.&rsquo; The crippled man at the king&rsquo;s table, treated as a son, permanently resident in Jerusalem — this is the eschatological picture of the church as the adopted household of the Messianic king, still marked by the fall&rsquo;s effects, already welcomed to the table that will be set &lsquo;always.&rsquo;</p>"
  },
  "11": {
    "3": "<p>The narrator&rsquo;s parenthetical identification of Bathsheba as <em>ʾēšet ʾûriyyāh haḥittî</em> — &lsquo;the wife of Uriah the Hittite&rsquo; — is preserved verbatim in Matthew&rsquo;s genealogy of Jesus (Matt 1:6: <em>ek tēs tou Ouriou</em>, &lsquo;by her of Uriah&rsquo;). Matthew includes four women in the Messianic genealogy (Tamar, Rahab, Ruth, and &lsquo;her of Uriah&rsquo;), and in each case the inclusion emphasizes an irregular, scandalous, or Gentile connection through which the Messianic line passes. Bathsheba is designated not by her own name but by her murdered husband&rsquo;s — which preserves the double crime (adultery and murder) in the genealogy without concealment. This is the genealogical argument against any claim that the Messianic ancestry validates human virtue: the lineage of the Son of God runs through precisely the moral catastrophes that would disqualify a merely human claim to righteousness. 1 Cor 1:27-28: &lsquo;God chose what is low and despised in the world... so that no human being might boast in the presence of God.&rsquo; Rom 5:20: &lsquo;where sin increased, grace abounded all the more.&rsquo; The retention of &lsquo;wife of Uriah&rsquo; in the genealogy is the genealogical embodiment of this principle: grace is not embarrassed by the scandal; grace runs through it. The Messiah who is born of this lineage is the one who will bear not merely the genealogical weight of human sin but its full judicial weight — which is why the genealogy can afford to include what human constructions of honor would delete.</p>"
  }
}

def main():
    c = load_comm('mkt-christ', '2samuel')
    merge_comm(c, CHRIST)
    save_comm('mkt-christ', '2samuel', c)
    count = sum(len(v) for v in CHRIST.values())
    print(f'2samuel mkt-christ: wrote {count} verses across ch 8-11')

if __name__ == '__main__':
    main()
