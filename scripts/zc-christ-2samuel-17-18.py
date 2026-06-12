"""
MKT Christ Commentary — 2 Samuel chapters 17–18
Run: python3 scripts/zc-christ-2samuel-17-18.py

Ch17: 'YHWH ordained to defeat the good counsel of Ahithophel' — divine overruling
      of human wisdom as the cross-pattern; Ahithophel as betrayer-type (Ps 41:9)
Ch18: Absalom hanging cursed between heaven and earth — Gal 3:13 anti-type;
      David's 'would I had died instead of you' — substitutionary lament type

Typological links:
- 17:14 → 1 Cor 1:25; Acts 2:23 — divine wisdom defeats human wisdom / cross-pattern
- 17:23 → Ps 41:9; John 13:18; Acts 1:16 — Ahithophel suicide = betrayer-type
- 18:9  → Gal 3:13; Deut 21:23 — cursed hanging; anti-type of Christ's accursed death
- 18:33 → Rom 5:8; Gen 22:13; Luke 15:20 — taḥat substitutionary lament
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
  "17": {
    "14": "<p>The narrator&rsquo;s theological comment on Absalom&rsquo;s choice of Hushai&rsquo;s militarily inferior counsel over Ahithophel&rsquo;s strategically superior plan — <em>kî YHWH ṣiwwāh lᵉhāpēr ʾet ʿăṣat ʾăḥîṯōpel haṭṭôḇāh lᵉmaʿan hāḇîʾ YHWH ʾel ʾaḇšālôm ʾet hārāʿāh</em>, &lsquo;for YHWH had ordained to defeat the good counsel of Ahithophel, so that YHWH might bring harm upon Absalom&rsquo; — establishes the theological structure that 1 Cor 1:25 names as a cross-principle: &lsquo;the foolishness of God is wiser than men, and the weakness of God is stronger than men.&rsquo; The political deliberation that chose the weaker plan is the human surface of a divine act: YHWH overturns what human wisdom rightly identifies as best. The parallel to the crucifixion is exact in structure: the cross appears to the rulers of this age as a defeat, an execution of the Messianic claimant — and it is precisely the divinely-ordained vehicle of cosmic victory. 1 Cor 2:8: &lsquo;none of the rulers of this age understood this, for if they had, they would not have crucified the Lord of glory.&rsquo; Acts 2:23 names the same dual causality: &lsquo;this Jesus, delivered up according to the definite plan and foreknowledge of God, you crucified and killed by the hands of lawless men&rsquo; — both divine ordination and human agency fully operative simultaneously. The narrative irony in both cases is the same: the human actors who choose the &lsquo;better&rsquo; option from within their own frame of reference are executing the divine plan while opposing it. What looks like wisdom to Absalom&rsquo;s council is disaster; what looks like defeat to Pilate&rsquo;s court is redemption.</p>",
    "23": "<p>Ahithophel&rsquo;s response to the rejection of his counsel — <em>wayyaḥăbōš ʾet ḥămōrô wayyāqom wayyēlek ʾel bêtô ʾel ʿîrô wayyᵉṣaw ʾel bêtô wayyēḥānaq wayyāmot</em>, &lsquo;he saddled his donkey, went home to his own city, set his house in order, and hanged himself&rsquo; — is the narrative foreground of the typological chain that Ps 41:9 and John 13:18 trace. Ahithophel is David&rsquo;s most intimate counselor (&lsquo;his counsel was like the word of God,&rsquo; 16:23), the advisor who ate at the king&rsquo;s table — and he betrays David by joining Absalom&rsquo;s rebellion. Ps 41:9 — &lsquo;even my close friend in whom I trusted, who ate my bread, has lifted his heel against me&rsquo; — is the Davidic reflection on this betrayal, and its Christological application is explicit in John 13:18, where Jesus applies the verse to Judas: &lsquo;I am not speaking of all of you; I know whom I have chosen. But the Scripture will be fulfilled, &ldquo;He who ate my bread has lifted his heel against me.&rdquo;&rsquo; Acts 1:16 cites the psalm as fulfilled in Judas&rsquo;s death. The typological chain is: Ahithophel (historical referent of David&rsquo;s lament in Ps 41) → Ps 41:9 (David&rsquo;s prophetic language about the betrayer) → John 13:18 (Jesus&rsquo;s self-identification with the psalmist over Judas) → Acts 1:16-20 (the Judas-betrayal as fulfillment). In both cases, the betrayer&rsquo;s death is by hanging, after a betrayal of the Lord&rsquo;s anointed from a position of intimate trust. The Succession Narrative provides the historical ground on which the Davidic psalms develop the betrayer-type that the NT reads as predictive.</p>"
  },
  "18": {
    "9": "<p>Absalom&rsquo;s death — hanging between heaven and earth (<em>wayyunnah bên haššāmayim ûbên hāʾāreṣ</em>) from the great terebinth — is the anti-type of Gal 3:13&rsquo;s account of Christ&rsquo;s crucifixion. Deut 21:23 declared that &lsquo;a hanged man is cursed of God,&rsquo; and the suspension between heaven and earth is the form of that curse: belonging to neither realm, excluded from both the divine and the earthly communities. Absalom&rsquo;s hanging is his deserved judgment — the usurper who grasped the kingdom by rebellion dies in precisely the form that Torah marks as the death of the accursed. Gal 3:13 applies the Deuteronomy formula to Christ&rsquo;s crucifixion: &lsquo;Christ redeemed us from the curse of the law by becoming a curse for us — for it is written, &ldquo;Cursed is everyone who is hanged on a tree.&rdquo;&rsquo; The anti-typology turns on moral inversion: Absalom hangs accursed for his own rebellion; Christ hangs accursed for the rebellion of others. Absalom is suspended between heaven and earth because he deserves exclusion from both; Christ is suspended between heaven and earth as the one who, in Phil 2:6, &lsquo;did not count equality with God a thing to be grasped&rsquo; — the one who never seized what was not his. The form of the death is identical; the moral valence is precisely reversed. What the narrative shows as Absalom&rsquo;s shameful end Gal 3:13 identifies as the mechanism of atonement: the cursed death, voluntarily assumed by the guiltless, exhausts the curse rather than confirming it.</p>",
    "33": "<p>David&rsquo;s lament over Absalom — <em>mî yittēn môtî ʾănî taḥtêḵā ʾaḇšālôm bᵉnî bᵉnî</em>, &lsquo;who will grant that I had died instead of you, O Absalom, my son, my son&rsquo; — is the most concentrated substitutionary statement in the OT outside of Isa 53. The word <em>taḥat</em> (instead of, in the place of) is the preposition of substitution: it appears in the binding of Isaac narrative (Gen 22:13: the ram &lsquo;<em>taḥat</em> his son&rsquo;), in ransom formulas, and in the explicit substitutionary logic of Isa 53:5-6. David&rsquo;s wish — &lsquo;I instead of you&rsquo; — is the articulate expression of the substitutionary impulse: the desire of the father to absorb the death the son has incurred. The theological density of the scene lies in what David&rsquo;s lament reveals about the object of that desire: he does not grieve for a faithful son. He grieves for the rebel who had stolen his throne, violated his concubines, and driven him into exile — and wishes to die in that rebel&rsquo;s place. This is Rom 5:8 in the register of paternal grief: &lsquo;while we were still sinners, Christ died for us.&rsquo; The father of Luke 15:20 who runs to meet the returning prodigal is the same impulse in a different narrative mode. David&rsquo;s wish is unfulfillable — his death could not serve as a substitute for Absalom&rsquo;s, and even if it could, his own guilt would make the exchange inadequate. The NT&rsquo;s claim is that what David&rsquo;s lament expresses and cannot achieve, Christ accomplishes: dying <em>taḥat</em> those who had rebelled against the Father&rsquo;s household (Gal 4:4-5), &lsquo;to redeem those who were under the law, so that we might receive adoption as sons.&rsquo;</p>"
  }
}

def main():
    c = load_comm('mkt-christ', '2samuel')
    merge_comm(c, CHRIST)
    save_comm('mkt-christ', '2samuel', c)
    count = sum(len(v) for v in CHRIST.values())
    print(f'2samuel mkt-christ: wrote {count} verses across ch 17-18')

if __name__ == '__main__':
    main()
