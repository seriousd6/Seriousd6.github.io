"""
MKT Context Commentary — 2 Samuel chapters 17–18
Run: python3 scripts/zc-context-2samuel-17-18.py

Ch17: Ahithophel vs. Hushai — the military-strategic context of the counsel contest;
      Mahanaim as David's Transjordanian refuge; Barzillai and covenant provisions
Ch18: The forest of Ephraim east of the Jordan; the royal mule and Absalom's death;
      Absalom's memorial stele — the ANE maṣṣeḇāh tradition

ANE/historical context:
- Mahanaim (17:24): Transjordanian city, Jacob's angel encounter (Gen 32:2);
  Ish-bosheth's capital; modern Tell edh-Dhahab el-Gharbi (proposed)
- The royal mule (18:9): mule as the designated royal mount in ANE Israel
  (cf. 1 Kgs 1:33 — Solomon on David's mule)
- maṣṣeḇāh (18:18): standing stone/memorial stele — the ANE monument tradition
- Barzillai the Gileadite (17:27): covenant-loyal elder; type of the faithful
  elder who serves the rejected king
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

CONTEXT = {
  "17": {
    "1": "<p>Ahithophel&rsquo;s military counsel to Absalom is presented as genuinely superior: strike immediately with 12,000 men while David is &lsquo;weary and weak-handed&rsquo; (<em>yāgēaʿ wᵉrāpeh yāḏayim</em>), kill David alone, and bring all the people back to Absalom without a general war. The assessment that &lsquo;Absalom and all the elders of Israel said, The counsel of Hushai the Archite is better than the counsel of Ahithophel&rsquo; (v14) — despite Hushai&rsquo;s counsel being militarily inferior — is where the narrator inserts the theological key: &lsquo;for YHWH had ordained to defeat the good counsel of Ahithophel, so that YHWH might bring harm upon Absalom.&rsquo; The narrative thus operates on two levels simultaneously: political deliberation on the surface, divine direction of outcomes beneath. This two-level structure is the Succession Narrative&rsquo;s characteristic theological method — YHWH governs the narrative not through direct intervention but through the decisions of human actors who are themselves directed without knowing it. The military-strategic analysis is technically competent; the theological point is that competence without divine backing is insufficient, and divine backing can work through the rejection of competence.</p>",
    "27": "<p>David&rsquo;s Transjordanian refuge at Mahanaim is supported by three figures who bring provisions: Shobi son of Nahash of Rabbah of the Ammonites, Machir son of Ammiel from Lo-debar, and Barzillai the Gileadite from Rogelim. Mahanaim (<em>maḥănayim</em>, &lsquo;two camps&rsquo;) is identified in Gen 32:2 as the place where Jacob encountered the angels of God on his return from Laban — he named it Mahanaim because &lsquo;two camps&rsquo; appeared to him (the divine camp and his own). The same location served as Ish-bosheth&rsquo;s capital during the civil war (2 Sam 2:8). Its location east of the Jordan (modern proposed site: Tell edh-Dhahab el-Gharbi in the Jabbok valley) made it a natural refuge beyond immediate reach of Jerusalem-based forces. The provision of food (<em>miškāḇ wᵉsippôt ûkᵉlî yeqar</em> — beds, basins, and earthenware vessels, v28) to the fugitive king is the ANE covenant-loyalty obligation in action: those who have received royal favor or who maintain covenant relationship with the Davidic house fulfill their obligation by sustaining the king in his exile.</p>"
  },
  "18": {
    "9": "<p>Absalom&rsquo;s death is dense with irony. He is riding his mule (<em>pereḏ</em>) — the royal mount; in Israel the mule was the king&rsquo;s designated riding animal (cf. 1 Kgs 1:33, where David commands Solomon to be set on &lsquo;my own mule&rsquo; for his anointing coronation procession). The usurper-prince dies on the royal mount. The tree that catches him — described only as &lsquo;a great terebinth&rsquo; (<em>ʾêlāh gᵉḏôlāh</em>) — catches him by his head (<em>wᵉrōʾšô heḥĕzîq bāʾêlāh</em>). That Absalom is caught by his head, not by his famous hair specifically, is the MT reading; but given the earlier emphasis on his hair (14:26: 200 shekels at the year-end cutting), ancient readers would have assumed the connection. He hangs between heaven and earth (<em>wayyunnah bên haššāmayim ûbên hāʾāreṣ</em>) — the shameful suspended death that Deut 21:23 declares accursed: &lsquo;a hanged man is cursed by God.&rsquo; Absalom&rsquo;s death fulfills in detail what he most feared: the loss of the royal office he seized, the loss of his name (v18), and death in the manner of the shamed and cursed.</p>",
    "18": "<p>The memorial stele Absalom erected in the King&rsquo;s Valley (<em>ʿemek hammelek</em>) during his lifetime reflects the ANE practice of <em>maṣṣeḇāh</em> (standing stone/stele) erection as a monument to preserve the name of one who has no heir to continue it. Absalom&rsquo;s stated reason — &lsquo;I have no son to keep my name in remembrance&rsquo; — is noteworthy given 14:27&rsquo;s statement that he had three sons and a daughter; the sons apparently died young, leaving Tamar as his only surviving child. The ANE memorial stele tradition is well attested: from Egyptian commemorative stelae to the Mesha Stele (Moabite Stone, ca. 830 BCE) to the Stele of Shalmaneser III. The Hebrew <em>maṣṣeḇāh</em> is the same term used for the standing stones Jacob erects at Bethel (Gen 28:18; 35:14), for Moses&rsquo;s twelve pillars at Sinai (Exod 24:4), and for the standing stones the prophets condemn in the context of Canaanite cult sites. Absalom&rsquo;s stele — erected to preserve a name that will be forgotten anyway — stands as the narrative&rsquo;s judgment: the one who grasped the kingdom to preserve his name and legacy ends in a pit in the forest, his stele an ironic monument to failed ambition.</p>"
  }
}

def main():
    c = load_comm('mkt-context', '2samuel')
    merge_comm(c, CONTEXT)
    save_comm('mkt-context', '2samuel', c)
    count = sum(len(v) for v in CONTEXT.values())
    print(f'2samuel mkt-context: wrote {count} verses across ch 17-18')

if __name__ == '__main__':
    main()
