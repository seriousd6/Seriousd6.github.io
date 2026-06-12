"""
MKT Original Commentary — 1 Chronicles chapters 2–3
Run: python3 scripts/zc-original-1chronicles-2-3.py

Ch2: Achar/Achan wordplay — the troubler of Israel / ʿāḵān → ʿāḵār name-pun
Ch3: Jeconiah "the captive" (hāʾăsîr) — the Davidic line descending through a prisoner
     The post-exilic Davidic line through Zerubbabel into the Chronicler's era
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
  "2": {
    "7": "<p>The Chronicler names Achan as <em>ʿāḵār</em> — not the form used in Joshua (where the name is <em>ʿāḵān</em>, Josh 7:1-26) — and immediately glosses it: <em>ʿōḵēr yiśrāʾēl ʾăšer māʿal maʿal bᵉḥērem</em>, &lsquo;the troubler of Israel who broke faith in the matter of the devoted thing.&rsquo; The name <em>ʿāḵār</em> is a deliberate morphological pun on the verb <em>ʿāḵar</em> (to trouble, disturb, bring calamity) — the same root that appears in Josh 7:25, where Joshua says <em>meh ʿăḵartānû YHWH yaʿkorᵉḵā hayyôm hazzeh</em>, &lsquo;Why did you bring trouble on us? YHWH brings trouble on you today.&rsquo; The valley of execution is subsequently named <em>ʿēmeq ʿāḵôr</em>, &lsquo;Valley of Achor/Trouble&rsquo; (Josh 7:26; Hos 2:15; Isa 65:10). The Chronicler&rsquo;s renaming of Achan as Achar encodes the interpretation into the name itself: the man whose act brought <em>ʿāḵar</em> on Israel is remembered by the name of his deed. This is the genealogy&rsquo;s only explicit negative notation in the Judahite line — a single name that carries the full weight of the ḥērem-violation and its consequences. The principle that one person&rsquo;s covenant-breach affects the entire community (Josh 7:1: &lsquo;the people of Israel broke faith&rsquo;) is what the Achar/ʿāḵar wordplay encodes.</p>"
  },
  "3": {
    "17": "<p>The designation of Jeconiah (Jehoiachin) as <em>hāʾăsîr</em> — &lsquo;the captive&rsquo; or &lsquo;the prisoner&rsquo; — in the genealogy (v17) is the Chronicler&rsquo;s recognition that the Davidic line passed through a deposed and imprisoned king. The word <em>ʾāsîr</em> (prisoner, captive) marks Jeconiah as the king taken to Babylon in 597 BCE (2 Kgs 24:8-16) where he remained in prison until Evil-merodach released him in 561 BCE (2 Kgs 25:27-30). The Chronicler&rsquo;s post-exilic Davidic genealogy (vv17-24) continues through this prisoner — Shealtiel, Zerubbabel, and six more generations — demonstrating that the exile and imprisonment of the Davidic king did not sever the covenant line. Zerubbabel (v19) is the key post-exilic Davidic figure, governor of Judah under Persia (Hag 1:1; Zech 4:6-10) and ancestor of Jesus in Luke&rsquo;s genealogy (Luke 3:27). Matt 1:11-12 includes <em>Iechonias</em> at the Babylon deportation as the hinge-point of the genealogy — the break and the continuity simultaneously — echoing the Chronicler&rsquo;s own ambivalent designation: the <em>ʾāsîr</em> through whom the Messiah would come. The word <em>ʾāsîr</em> also carries the resonance of Isa 53:8 (<em>meʿōṣer ûmimmišpāṭ luqqāḥ</em>, &lsquo;by oppression and judgment he was taken away&rsquo;) — the Servant whose suffering is encompassed in the same vocabulary of imprisonment and removal.</p>"
  }
}

def main():
    c = load_comm('mkt-original', '1chronicles')
    merge_comm(c, ORIGINAL)
    save_comm('mkt-original', '1chronicles', c)
    count = sum(len(v) for v in ORIGINAL.values())
    print(f'1chronicles mkt-original: wrote {count} verses across ch 2-3')

if __name__ == '__main__':
    main()
