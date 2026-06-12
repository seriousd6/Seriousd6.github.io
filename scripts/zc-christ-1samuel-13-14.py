"""
MKT Christ Commentary — 1 Samuel chapters 13–14
Run: python3 scripts/zc-christ-1samuel-13-14.py

Ch13: Saul's unlawful sacrifice — the failed priest-king who conflates offices;
      the oracle of rejection and David's 'man after my heart';
      the kingdom that cannot continue prepares the way for the eternal king
Ch14: Jonathan's single-handed faith assault on the garrison — the lone deliverer
      entering the enemy stronghold; Saul's rash oath vs. Christ's life-giving word;
      Jonathan condemned and rescued — the intercession-rescue pattern
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
  "13": {
    "8": "<p>Saul's unlawful sacrifice — offering the burnt offering himself when Samuel delays — is the narrative's first portrayal of the fatal confusion of offices that will define his reign. The king and the priest are distinct offices in Israel, each bearing distinct consecration and distinct accountability to YHWH. Saul's forced offering (<em>wayyaʿal hāʿōlāh</em>) without prophetic authorization is the usurpation of the priestly role by the royal — the inversion of the divinely ordered distinction. The NT resolution of the priest-king tension is not Saul's fusion of the offices by force but the Melchizedekian order of Christ: the one who is both king and priest by <em>divine appointment</em> (Ps 110:4 — 'You are a priest forever after the order of Melchizedek'). Hebrews 7:14-17 makes explicit what Psalm 110 implies: Jesus's priesthood is legitimate not by Levitical lineage but by divine oath, by the power of an indestructible life. Saul is the antitype who shows what the unauthorized conflation of offices produces — rejection. Christ is the archetype who holds both offices by divine right and without usurpation.</p>",
    "14": "<p>Samuel's oracle of rejection contains the most theologically freighted phrase in the entire Samuel narrative: <em>biqqēš YHWH lô ʾîš kilᵉḇābô</em> — 'YHWH has sought for himself a man after (<em>kil</em>) his heart/mind (<em>lēḇāḇ</em>).' The preposition <em>kil</em> (literally 'like' or 'according to') marks the standard of conformity: YHWH is seeking a king whose inner disposition is conformed to YHWH's own. This oracle is cited verbatim by Paul in the Antioch synagogue sermon (Acts 13:22) as the direct theological preparation for the announcement of Jesus: 'Of this man's offspring God has brought to Israel a Savior, Jesus, as he promised' (Acts 13:23). The Davidic lineage fulfills the <em>kilᵉḇābô</em> oracle, but the fulfillment is not merely genetic — it is the reality that David typologically anticipates and Jesus literally embodies. Jesus's own claim — 'I always do the things that are pleasing to him' (John 8:29) — is the definitive realization of the man after YHWH's heart: not merely conformed to YHWH's desires but ontologically one with the Father's will. Saul's rejection is the shadow that makes the Davidic election intelligible; the Davidic election is the shadow that makes the Incarnation intelligible.</p>"
  },
  "14": {
    "6": "<p>Jonathan's declaration before his armor-bearer is one of the most compact faith-statements in the OT: <em>ʾên laYHWH māṣôr lᵉhôšîaʿ bᵉrab ʾô bimᵉʿāṭ</em> — 'there is nothing to YHWH preventing him from saving by many or by few.' The theological premise — that YHWH's capacity to save is not conditioned by military numbers — is the same premise David will articulate at Goliath (17:47: 'the battle is YHWH's'), that Gideon's 300 demonstrate (Judg 7), and that the angel of YHWH embodies when he strikes 185,000 Assyrians in a single night (2 Kgs 19:35). Jonathan enters the Philistine garrison with one companion, the theological precursor to Christ entering the realm of the enemy with no human army: 'I have trodden the winepress alone, and from the peoples no one was with me' (Isa 63:3). The single champion who achieves what no army could is the pattern of OT holy war fulfilled in Christ's solitary descent into death and his resurrection. Gabriel's annunciation employs the same theological logic: 'nothing will be impossible with God' (Luke 1:37) — the direct NT deployment of Jonathan's <em>ʾên māṣôr</em> premise.</p>",
    "27": "<p>The honey-and-darkness sequence is the narrative's sharpest image of law-versus-grace. Saul's oath has plunged the army into darkness (<em>yaʿap hāʿām</em>, 14:28 — the people were faint/exhausted), withholding the very energy the land offered freely. Jonathan, not having heard the oath, dips his staff in the honeycomb: <em>wayyāʾornāh ʿênāyw</em> — 'his eyes brightened/lit up.' The word <em>ʾôr</em> (light, to be illuminated) is the same root used in Ps 19:8 — 'the commandment of YHWH is pure, enlightening the eyes.' The irony is deliberate: the king's <em>sworn law</em> extinguishes light; the freely received honey — the provision of the land YHWH gives — illuminates. Paul's analysis in 2 Cor 3:6 ('the letter kills but the Spirit gives life') and in Gal 3:21 ('if a law had been given that could give life, then righteousness would indeed be by the law') maps directly onto this narrative. Jonathan's illuminated eyes contrast with Saul's life-draining prohibition; the honey of the land contrasts with the curse of the oath. The typological structure points to Christ as the one who comes not to drain life from his people through impossible demands but to give life: 'I came that they may have life and have it abundantly' (John 10:10).</p>",
    "45": "<p>The rescue of Jonathan from Saul's death sentence — <em>wayyipdeh hāʿām ʾet yôhônātān wᵉlōʾ mēt</em>, 'the people redeemed Jonathan and he did not die' — completes a typological arc in the chapter. Jonathan has acted rightly, achieved the victory, and yet been condemned to death by his own father's ill-considered oath. The people interpose themselves as redeemers (<em>pādāh</em>, to ransom/redeem by substitution): 'As YHWH lives, not one hair of his head shall fall to the ground.' The phrase 'not one hair of his head shall fall to the ground' echoes in Jesus's own promise of providential care (Luke 21:18: 'not a hair of your head will perish') and in Paul's promise to the sailors (Acts 27:34). But the deeper typological weight is the rescue-by-intercession structure itself: the innocent person rightly condemned, the community standing between the condemned and the unjust execution, the substitutionary redemption. This prefigures Christ's atonement in reverse: where the community rescues the innocent Jonathan by interposing themselves, Christ rescues the guilty community by interposing himself — the direction of the substitution is inverted, but the structural pattern of interposition-for-the-condemned is the same.</p>"
  }
}

def main():
    c = load_comm('mkt-christ', '1samuel')
    merge_comm(c, CHRIST)
    save_comm('mkt-christ', '1samuel', c)
    count = sum(len(v) for v in CHRIST.values())
    print(f'1samuel mkt-christ: wrote {count} verses across ch 13-14')

if __name__ == '__main__':
    main()
