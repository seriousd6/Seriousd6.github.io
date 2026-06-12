"""
MKT Original Commentary — 2 Kings chapters 24–25
Run: python3 scripts/zc-original-2kings-24-25.py

Ch24: gālāh / gōlāh — the exile vocabulary; the deportation of craftsmen and the royal court
Ch25: šārap ʾet bêt YHWH bāʾēš — burned the house of YHWH with fire;
      śar ṭabāḥîm nᵉḇûzarʾăḏān — the captain of the guard and the Babylonian destruction;
      yôyāḵîn nāśāʾ ʾet rōʾšô — Jehoiachin's head lifted = the open ending

Key Hebrew terms:
- gālāh (24:14-16): to go into exile — the exile vocabulary
- šārap bāʾēš (25:9): burned with fire — the enacted covenant curse of 1 Kgs 9:7-9
- nāśāʾ ʾet rōʾšô (25:27): lifted up his head — the ambiguous ending / hope signal
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
  "24": {
    "14": "<p>The first Babylonian deportation under Nebuchadnezzar — <em>wayyigel ʾet kol yᵉrûšālaim wᵉʾet kol haśśārîm wᵉʾet kol gibborê hāḥayil ʿăśārāh ʾălāpîm gōleh ûkol heḥārāš wᵉhammassēr lōʾ nišʾar zûlatî dallat ʿam hāʾāreṣ</em> — removes the élite and skilled workers first: princes, warriors, craftsmen, smiths. The Hebrew <em>gōlāh</em> (exile, the exiled community) and its verbal root <em>gālāh</em> (to be uncovered, to go into exile) carry the imagery of the captive community exposed and displaced. The craftsmen (<em>ḥārāš</em>) are particularly significant: their removal was strategic military policy (to prevent weapon-making) but has the unintended effect of preparing a skilled exilic community who will contribute to Babylon&rsquo;s cultural life (Dan 1:4-5). Isa 40:1-2 addresses the <em>gōlāh</em>-community: <em>naḥămû naḥămû ʿammî</em>, &lsquo;Comfort, comfort my people&rsquo; — the opening address of the second Isaiah is directed precisely at those whom 2 Kgs 24:14 counted among the deported. The apostolic use of <em>paroikia</em> (sojourning/exile) and <em>diaspora</em> (dispersion) in 1 Pet 1:1, 17 and Jas 1:1 applies the exile vocabulary theologically to the church: &lsquo;to those who are elect exiles of the Dispersion&rsquo; — the new covenant community shares the structural condition of the <em>gōlāh</em>, living in the world as those whose true homeland is elsewhere.</p>"
  },
  "25": {
    "9": "<p>Nebuzaradan&rsquo;s burning of the temple — <em>wᵉʾet bêt YHWH wᵉʾet bêt hammelek wᵉʾēt kol bātê yᵉrûšālaim wᵉʾet kol bêt gāḏôl śārap bāʾēš</em>, &lsquo;he burned the house of YHWH and the king&rsquo;s house and all the houses of Jerusalem; every great house he burned down&rsquo; — is the enacted fulfillment of the conditional covenant curse of 1 Kgs 9:7-9: <em>wᵉhabbayit hazzeh yihyeh ʿelyôn</em>, &lsquo;this house will become a heap of ruins.&rsquo; The burning is not a historical accident but a covenant consequence: YHWH did exactly what he warned he would do. Lam 2:6-8 narrates the theological shock: YHWH himself is the destroyer — <em>wayyaḥmōs kᵉgān śukkô šiḥēt môʿāḏô</em>, &lsquo;he has laid waste his booth like a garden, laid in ruins his place of meeting.&rsquo; Jer 7:14 had warned that calling out &lsquo;the temple of YHWH&rsquo; was not protection: &lsquo;I will do to the house that is called by my name, and in which you trust, and to the place that I gave to you and to your fathers, as I did to Shiloh.&rsquo; The burning fulfills what Jeremiah had said would be the final answer to false temple-confidence. Heb 9:26 identifies the NT resolution: Christ &lsquo;has appeared once for all at the end of the ages to put away sin by the sacrifice of himself&rsquo; — the temple that bore the sin of the people is gone; the sacrifice that finally addressed it has been made.</p>",
    "27": "<p>The final note of 2 Kings — <em>nāśāʾ ʾet rōʾš yôyāḵîn melek yᵉhûḏāh mibêt keleʾ</em>, &lsquo;Evil-merodach king of Babylon, in the year he began to reign, lifted up the head of Jehoiachin king of Judah out of prison&rsquo; — ends the narrative on a deliberately open, ambiguous note. The idiom <em>nāśāʾ ʾet rōʾš</em> (to lift up the head) means to restore to honor (cf. Gen 40:13, where Pharaoh &lsquo;lifts up the head&rsquo; of the cupbearer = restoration to office). Jehoiachin is released, given a throne, and fed at the king&rsquo;s table for the rest of his life (vv28-30). He is not a free king — but he is alive, honored, and at the royal table. The Davidic line has not ended; the last king of Judah dies not in prison or in battle but at a king&rsquo;s table. Von Rad reads this as the canonical signal of hope: the narrator ends not with the heap of ruins but with a Davidic heir alive. Matthew&rsquo;s genealogy includes Jehoiachin (<em>Iechonias</em>, Matt 1:11-12) in the line from David to Jesus — the exile-king who was lifted up, honored, and whose seed continued, is placed in the chain that leads to the one whom God raises from the dead to a throne not in Babylon but at his right hand (Acts 2:33).</p>"
  }
}

def main():
    c = load_comm('mkt-original', '2kings')
    merge_comm(c, ORIGINAL)
    save_comm('mkt-original', '2kings', c)
    count = sum(len(v) for v in ORIGINAL.values())
    print(f'2kings mkt-original: wrote {count} verses across ch 24-25')

if __name__ == '__main__':
    main()
