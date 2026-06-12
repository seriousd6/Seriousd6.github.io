"""
MKT Original Commentary — 1 Chronicles chapters 26–28
Run: python3 scripts/zc-original-1chronicles-26-28.py

Ch27: Stars-of-heaven promise invoked in census restraint (27:23) — Gen 15:5; 22:17
Ch28: YHWH searches all hearts — ḥāqar + yeṣer vocabulary (28:9) / Heb 4:13
      tabnît (blueprint) — David receives temple plan as Moses received tabernacle (28:19) / Heb 8:5
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
  "27": {
    "23": "<p>The note that David did not number those under twenty years old — <em>lōʾ nāśāʾ dāwîḏ mispārām lᵉmibben ʿeśrîm šānāh wāmaṭṭāh kî ʾāmar YHWH lᵉharbôt ʾet yiśrāʾēl kᵉḵôḵᵉḇê haššāmāyim</em>, &lsquo;David did not number those twenty years and under, for YHWH had said he would make Israel as numerous as the stars of heaven&rsquo; — invokes the Abrahamic stellar-promise (Gen 15:5; 22:17) as the explicit warrant for census-restraint. The connection is significant: the census of ch21 (which brought plague) was a failure to reckon with this same promise. By counting the full military population, David treated Israel&rsquo;s numbers as knowable human data rather than as YHWH&rsquo;s promise-in-progress. The exemption of those under twenty recalls the wilderness census (Num 1:3: those twenty and above who can go to war), but the Chronicler&rsquo;s gloss deepens it: the &lsquo;uncounted&rsquo; are those still being added in fulfillment of the promise. The Abrahamic <em>kᵉḵôḵᵉḇê haššāmāyim</em> (as numerous as the stars of heaven) is the OT&rsquo;s formula for the uncountable covenant-gift: Heb 11:12 applies it to Abraham&rsquo;s descendants &lsquo;as many as the stars of heaven and as innumerable as the grains of sand by the seashore.&rsquo; David&rsquo;s restraint here acknowledges that the covenant-multiplication cannot be audited.</p>"
  },
  "28": {
    "9": "<p>David&rsquo;s charge to Solomon — <em>kî YHWH ḥōqēr kol lᵉḇāḇôt wᵉḵol yeṣer maḥăšāḇôt mēḇîn</em>, &lsquo;for YHWH searches all hearts and understands every plan and thought&rsquo; — uses two key vocabulary items. The verb <em>ḥāqar</em> (to search, probe, investigate) appears in Ps 139:1 (<em>YHWH ḥᵉqartanî wattēḏāʿ</em>, &lsquo;O YHWH, you have searched me and known me&rsquo;) and Jer 17:10 (<em>ʾănî YHWH ḥōqēr lēḇ</em>, &lsquo;I YHWH search the heart&rsquo;). The noun <em>yeṣer</em> (inclination, plan, formation — from <em>yāṣar</em>, to form/shape) appears in Gen 6:5 where &lsquo;every <em>yeṣer</em> of the thoughts of the human heart was only evil continually&rsquo; — the diagnosis that precedes the flood. Here David uses the same <em>yeṣer</em> in the context of worship-formation: if Solomon seeks YHWH, the <em>yeṣer maḥăšāḇôt</em> (inclination of his thoughts) will be known and approved; if he forsakes YHWH, he will be cast off. The NT applies the same divine heart-knowledge: Heb 4:13 (<em>panta de gymna kai tetrachēlismena tois ophthalmois autou</em>, &lsquo;all are naked and exposed to the eyes of him to whom we must give account&rsquo;) and John 2:25 (&lsquo;he himself knew what was in man&rsquo;). The <em>ḥōqēr lēḇāḇôt</em> is the consistent OT attribute that grounds both judgment and pastoral care: YHWH&rsquo;s searching is not surveillance but the omniscience of the covenant God who knows what his covenant partner needs before asking.</p>",
    "19": "<p>The divine inscription of the temple plan — <em>hakkōl bikᵉtāḇ miyyaḏ YHWH ʿālay hiśkîl kōl malʾᵉḵôt hattabnît</em>, &lsquo;all this in writing from the hand of YHWH; he made me understand all the works of the plan&rsquo; — frames the temple blueprint (<em>tabnît</em>) as divinely revealed, parallel to the tabernacle blueprint given to Moses. In Exod 25:9, YHWH instructs Moses: <em>kᵉḵōl ʾăšer ʾănî marʾeh ʾôtᵉḵā ʾēt tabnît hammiškan</em>, &lsquo;according to all that I show you, the <em>tabnît</em> of the tabernacle&rsquo;; in Exod 25:40, the command is to make everything <em>bᵉtabnîtām</em> (according to their pattern), the verse that Heb 8:5 cites: <em>horate, phēsin, poiēseis panta kata ton typon ton deichthenta soi en tō orei</em> — &lsquo;see that you make everything according to the pattern that was shown you on the mountain.&rsquo; The Chronicler&rsquo;s use of <em>tabnît</em> for both the tabernacle-vocabulary and the temple-plan creates a deliberate parallel: David receives the temple-tabnît as Moses received the tabernacle-tabnît — both from YHWH, both in writing or vision, both then executed by a designated builder (Moses by Bezalel; David by Solomon). Hebrews reads the tabernacle&rsquo;s <em>tabnît</em> as a shadow of the heavenly sanctuary (Heb 8:5; 9:23-24); the Chronicler&rsquo;s extension of the same pattern to the temple suggests the entire earthly sanctuary sequence (tabernacle → temple) is a single divine pedagogical movement toward what Heb 9:11 calls &lsquo;the greater and more perfect tent, not made with hands.&rsquo;</p>"
  }
}

def main():
    c = load_comm('mkt-original', '1chronicles')
    merge_comm(c, ORIGINAL)
    save_comm('mkt-original', '1chronicles', c)
    count = sum(len(v) for v in ORIGINAL.values())
    print(f'1chronicles mkt-original: wrote {count} verses across ch 26-28')

if __name__ == '__main__':
    main()
