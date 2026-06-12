"""
MKT Christ Commentary — 2 Samuel chapters 1–3
Run: python3 scripts/zc-christ-2samuel-1-3.py

Ch1: David's royal lament over Saul and Jonathan — the weeping king type;
     qinah meter as the formal root of Gethsemane's loud cries and tears
Ch2: Hebron anointing — partial/staged royal investiture; Acts 2:36 pattern
Ch3: The long war — incremental Messianic kingdom displacement (1 Cor 15:25);
     'servant David will save' — ʿeḇeḏ title as proto-Servant Song trajectory

Typological links:
- 1:19 → Luke 19:41; Heb 5:7 — royal lament/weeping as intercessory grief
- 2:4 → Acts 2:36; Matt 3:17 — staged anointing / partial enthronement
- 3:1 → 1 Cor 15:25-26; Isa 9:7 — long war / inexorable kingdom growth
- 3:18 → Acts 4:27, 30; Matt 1:21; Luke 1:69 — ʿeḇeḏ YHWH / Servant salvation
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
  "1": {
    "19": "<p>David&rsquo;s <em>qinah</em> lament over Saul and Jonathan (&lsquo;How the mighty have fallen!&rsquo;) is the first royal lament in the Davidic literary tradition, and it opens the typological thread that runs through the Psalms of Lament to Gethsemane. The <em>qinah</em> meter (3+2 stress pattern, the characteristic Hebrew mourning form) frames the weeping of the rightful king over what is lost — over the fallen king who had hunted him and the friend who had loved him — as an act of grief that transcends personal interest. This is the shape of kingly intercession: the true shepherd-king weeps not only over his friends but over his enemies. Heb 5:7 identifies this as a defining mark of the incarnate Christ: &lsquo;In the days of his flesh, Jesus offered up prayers and supplications, with loud cries and tears (<em>kraug&ecirc;s ischyr&aacute;s kai dakry&ocirc;n</em>) to him who was able to save him from death.&rsquo; The &lsquo;loud cries and tears&rsquo; of Heb 5:7 are the NT&rsquo;s interpretive key to the Gethsemane agonizing (Luke 22:44: &lsquo;his sweat became like great drops of blood falling down to the ground&rsquo;), and the formal root of that lamentation tradition is the Davidic <em>qinah</em>. David weeps over Jerusalem&rsquo;s king and hero; Jesus weeps over Jerusalem itself (Luke 19:41: &lsquo;when he drew near and saw the city, he wept over it&rsquo;) with the grief of the messianic king whose people have not received what would make for their peace. The typological structure: David&rsquo;s tears over fallen Saul (the rejected king, his own enemy) and Jonathan (the friend who died for covenant) prefigure the one who would grieve both the betrayal of a friend and the rejection by those he came to save.</p>"
  },
  "2": {
    "4": "<p>David&rsquo;s anointing at Hebron as king over the house of Judah alone is the second of three royal anointings he receives (Samuel&rsquo;s private anointing in 1 Sam 16:13; this public investiture; and finally the anointing as king over all Israel in 2 Sam 5:3), establishing the pattern of staged royal consecration: the true king is recognized and installed in steps, with the full sovereignty coming only after the long conflict with the rival house is resolved. The NT applies this same staged-enthronement structure to Jesus. Matt 3:17 (&lsquo;this is my beloved Son, in whom I am well pleased&rsquo; at the Jordan anointing) corresponds to the public royal investiture at Hebron: the Spirit descends upon the Messiah and his identity is declared, but the full enthronement comes only after the suffering and the cross. Acts 2:36 marks the second stage: &lsquo;Let all the house of Israel therefore know for certain that God has made him both Lord and Christ (<em>kai Kyrion kai Christon</em>), this Jesus whom you crucified.&rsquo; The &lsquo;making&rsquo; here is not an ontological change but a royal installation into the seat of universal lordship — the exaltation to the right hand of the Father that corresponds to David&rsquo;s enthronement over all Israel after Ish-bosheth&rsquo;s house falls. The 7-year Hebron reign (2 Sam 2:11; 5:5) maps the present age: Christ is already anointed and ruling, but the full eschatological consummation — all enemies made a footstool (Ps 110:1; Acts 2:35) — awaits the end of the long conflict between the Messianic house and the powers that oppose it.</p>"
  },
  "3": {
    "1": "<p>The summary statement of the inter-regnum conflict — <em>wattehî hammilḥāmāh ʾăreḵet bên bêt šāʾûl ûbên bêt dāwiḏ wᵉdāwiḏ hōlēḵ wᵉḥāzēq ûbêt šāʾûl hōlᵉḵîm wᵉḏallîm</em> — &lsquo;there was a long war between the house of Saul and the house of David; and David grew stronger and stronger, while the house of Saul grew weaker and weaker&rsquo; — describes the temporal structure of Messianic kingdom advance. The Davidic victory is not instantaneous but incremental: the old order weakens and the new strengthens over time, through the persistence of conflict rather than through a single decisive act. 1 Cor 15:25-26 applies this structure directly to the Messianic reign: &lsquo;for he must reign (<em>dei gar auton basileuein</em>) until he has put all his enemies under his feet. The last enemy to be destroyed is death.&rsquo; The &lsquo;must reign until&rsquo; construction presupposes the long-war pattern: Christ is already enthroned (Acts 2:36) but the displacement of the powers that oppose his reign is ongoing, proceeding from Pentecost toward the parousia. Isa 9:7 (&lsquo;of the increase of his government and of peace there will be no end&rsquo;) is the prophetic oracle for which this narrative is the historical type: a kingdom that begins partially, expands inexorably, and ends in the total displacement of every rival. The Succession Narrative&rsquo;s theological point is that this growth is YHWH&rsquo;s doing, not David&rsquo;s: the same narrated divine sovereignty that the NT applies to the advance of the Gospel through the persecuted church (Acts 6:7: &lsquo;the word of God continued to increase and spread&rsquo;).</p>",
    "18": "<p>The oracle cited in support of Abner&rsquo;s overture — &lsquo;For YHWH has promised David, saying, By the hand of my servant David I will save my people Israel from the hand of the Philistines and from the hand of all their enemies&rsquo; — invests the title <em>ʿeḇeḏ</em> (servant) with a specific salvific function: the servant saves the people. This is the proto-Servant trajectory whose fullest expression is the Isaianic Servant Songs. The chain: David as <em>ʿeḇeḏ YHWH</em> who saves Israel from its enemies (2 Sam 3:18; Ps 89:3, 20: &lsquo;I have found David my servant&rsquo;) → the Servant of YHWH in Isa 42:1; 49:3, 6; 52:13 who saves not only Israel but &lsquo;a light for the nations&rsquo; → Jesus as <em>pais tou theou</em> (the LXX translation of <em>ʿeḇeḏ</em>) in Acts 4:27, 30 (&lsquo;your holy servant Jesus, whom you anointed&rsquo;; &lsquo;through the name of your holy servant Jesus&rsquo;). The salvation function is the critical link: in 2 Sam 3:18, the servant saves the people (<em>yôšîaʿ</em>) from their enemies; in Matt 1:21, &lsquo;he will save (<em>s&ocirc;sei</em>) his people from their sins.&rsquo; The enemy has been redefined — from Philistines to sin and death — but the servant-saving-the-people structure is the same. Luke 1:69-70 fuses both registers explicitly: &lsquo;a horn of salvation in the house of his servant David, as he spoke by the mouth of his holy prophets from of old&rsquo; — the Davidic servant who saves and the prophetic servant-oracle are the two strands the incarnation ties together.</p>"
  }
}

def main():
    c = load_comm('mkt-christ', '2samuel')
    merge_comm(c, CHRIST)
    save_comm('mkt-christ', '2samuel', c)
    count = sum(len(v) for v in CHRIST.values())
    print(f'2samuel mkt-christ: wrote {count} verses across ch 1-3')

if __name__ == '__main__':
    main()
