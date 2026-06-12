"""
MKT Context Commentary — 1 Chronicles chapters 4–5
Run: python3 scripts/zc-context-1chronicles-4-5.py

Ch4: The prayer of Jabez — name-pain etymology, petition structure, scribal-colony context (4:10)
Ch5: Reuben's birthright transfer — ANE primogeniture and succession practices (5:1-2)
     Beerah exiled by Tiglath-pileser III — confirmed by Assyrian annals (5:6)
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
  "4": {
    "10": "<p>The prayer of Jabez (4:9-10) is one of the OT&rsquo;s briefest embedded prayers, set within a genealogical list without narrative context — a single pericope preserved as a liturgical or devotional tradition. The name <em>yaʿbēṣ</em> (Jabez) is linked to the root <em>ʿāṣaḇ</em> (to pain, grieve, hurt): &lsquo;because I bore him in pain (<em>bᵉʿōṣeḇ</em>).&rsquo; The prayer reverses the name-content: Jabez asks that God would &lsquo;keep me from harm/evil (<em>rāʿāh</em>) so that it might not bring me pain (<em>wᵉlōʾ yiʿaṣᵉḇênî</em>)&rsquo; — the same verbal root. The prayer thus performs a name-reversal: the man born in pain asks to be kept from pain, and God grants it. The four-part structure (bless me, enlarge my territory, let your hand be with me, keep me from harm) reflects the Israelite petition-formula pattern attested in the Psalms of lament (petition + confidence). The geographical notation of v23 (&lsquo;those who lived among plantings and in enclosures; they lived there with the king in his service&rsquo;) places a group of royal craftsmen/potters in the vicinity, possibly at Kiriath-jearim/the district of Jabez (cf. Judg 1:16), where a scribal guild is mentioned in v23. The Jabez prayer preserves, embedded in genealogy, the OT&rsquo;s clearest statement that individual petition within a genealogical/tribal context is legitimate and answered: YHWH responds to specific, named persons within the covenant people, not only to the nation collectively.</p>",
    "2": "<p>The opening of 1 Chr 5 provides the Chronicler&rsquo;s explanation for an anomaly in tribal history: Reuben was Jacob&rsquo;s firstborn (<em>bᵉḵôr</em>) but did not receive the firstborn&rsquo;s double-portion inheritance. The reason given is Gen 35:22 (Reuben&rsquo;s violation of Bilhah, Jacob&rsquo;s concubine) — the loss of the birthright is a consequence of moral failure. The Chronicler then separates two distinct forms of inheritance: the birthright (<em>bᵉḵōrāh</em>) goes to Joseph&rsquo;s sons (= two tribes, Ephraim and Manasseh, the double portion), but the ruling-dignity (<em>nāgîḏ</em>) goes to Judah. This distinction between double-portion inheritance and governing leadership parallels ANE succession practices. In Mesopotamia, the firstborn typically received the family estate (<em>aplum</em> in Akkadian, comparable to <em>bᵉḵōrāh</em>), but kingship could pass to a non-firstborn son by divine designation or ability — Assyrian succession documents, particularly from the reigns of Sargon II and Esarhaddon, record the formal transfer of kingship to younger sons with theological legitimation. The Chronicler&rsquo;s theological point is that the Davidic kingship (from Judah) is not an accident of birth-order but a divine allocation that the tribal system reflects: Reuben&rsquo;s moral failure, Joseph&rsquo;s double-portion, and Judah&rsquo;s messianic designation all serve the same canonical structure.</p>"
  },
  "5": {
    "6": "<p>The deportation of Beerah the Reubenite chief by Tiglath-pileser king of Assyria — <em>ʾōtô hᵉglāh tilgat pilneser melek ʾaššûr</em>, &lsquo;him Tiglath-pileser king of Assyria carried into exile&rsquo; — is confirmed by Assyrian royal records. Tiglath-pileser III (744-727 BCE), known in Babylonian sources as Pul (cf. 5:26 where the Chronicler equates Pul and Tiglath-pileser), conducted systematic deportation campaigns in the Transjordanian territories during 734-732 BCE. His annals and the Iran Stele record the deportation of populations from &lsquo;the wide land of Bit-Humria&rsquo; (the house of Omri = Israel/Samaria) and surrounding regions; 2 Kgs 15:29 records the same Transjordanian deportation. The Chronicler&rsquo;s equation of Pul and Tiglath-pileser in v26 is historically accurate: Pul was Tiglath-pileser&rsquo;s Babylonian throne-name (he ruled Babylon as Pulu from 728 BCE), and the confusion of two separate deportations in popular memory required clarification. The specific naming of Beerah as a named tribal chief who was exiled (unlike the mass of the population who remain anonymous) reflects the Assyrian practice of targeting tribal leaders and elites for deportation to dissolve local resistance structures — Tiglath-pileser&rsquo;s own annals boast of deporting named leaders from conquered territories and resettling them far from their power bases. The Chronicler preserves this Reubenite tradition as a specific historical memory of the Assyrian destruction of the Transjordanian tribal structures.</p>"
  }
}

def main():
    c = load_comm('mkt-context', '1chronicles')
    merge_comm(c, CONTEXT)
    save_comm('mkt-context', '1chronicles', c)
    count = sum(len(v) for v in CONTEXT.values())
    print(f'1chronicles mkt-context: wrote {count} verses across ch 4-5')

if __name__ == '__main__':
    main()
