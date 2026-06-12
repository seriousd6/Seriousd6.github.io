"""
MKT Context Commentary — 1 Kings chapters 3–5
Run: python3 scripts/zc-context-1kings-3-5.py

Ch3: Solomon's Egyptian alliance — anomalous daughter-giving in ANE diplomacy;
     Gibeon theophany — ANE royal incubation dream tradition (Thutmose IV, Gudea)
Ch4: Wisdom of the East and Egypt — Mesopotamian/Egyptian wisdom traditions;
     onomastica (natural-category lists) as the intellectual frame
Ch5: Hiram of Tyre — Phoenician geopolitics; cedar timber trade; the exchange economy

ANE/historical context:
- bat parʿōh (3:1): Egyptian princess — uniquely anomalous in ANE diplomacy
- Royal incubation dream (3:4-5): standard ANE pattern (Thutmose IV sphinx stele, Gudea)
- ḥoḵmat bᵉnê qeḏem (4:29-30): eastern/Mesopotamian wisdom; onomastica of Amenemopet
- ʾarzê lᵉḇānôn (5:1-3): Lebanon cedar — the luxury timber of the ancient world
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
  "3": {
    "1": "<p>The opening note of Solomon&rsquo;s reign — his marriage to Pharaoh&rsquo;s daughter (<em>bat parʿōh</em>) — is historically extraordinary. Throughout the ancient Near East, Egypt was the empire that received foreign women in diplomatic marriage, never gave its own daughters to foreign kings. Amenhotep III&rsquo;s Amarna letter to Kadashman-Enlil of Babylon (EA 4) captures the standard Egyptian posture: when the Babylonian king requests an Egyptian princess, the Pharaoh responds that &lsquo;from time immemorial, no daughter of the king of Egypt has been given to anyone.&rsquo; Solomon&rsquo;s receipt of Pharaoh&rsquo;s daughter signals either Egyptian diplomatic weakness during the Third Intermediate Period (when the 21st&ndash;22nd Dynasty was in relative decline) or Solomon&rsquo;s remarkable standing in the ancient world&rsquo;s diplomatic hierarchy. The Deuteronomic text is quiet about the implication but pointed in its placement: this note opens the account of Solomon&rsquo;s reign immediately after the narrator&rsquo;s approval of his early piety. Deut 17:17 warns the future king &lsquo;he shall not multiply wives for himself, lest his heart turn away.&rsquo; Ch11:1-3 will make explicit what ch3:1 quietly inaugurates: the Egyptian alliance is the first thread of the fabric that will unravel Solomon&rsquo;s undivided loyalty.</p>",
    "4": "<p>The Gibeon dream oracle is formally a royal incubation dream — the practice of sleeping at a sacred site to receive divine communication was standard in ANE royal piety. Egyptian examples: the Sphinx Stele of Thutmose IV (c.1400 BCE) records the sun god&rsquo;s promise of the kingship through a dream at the Great Sphinx. Mesopotamian examples: Gudea of Lagash received temple-building instructions through dream incubation at Girsu (ca. 2100 BCE), and Assyrian kings record multiple dream-oracle consultations. In the Gilgamesh Epic, Gilgamesh receives divine commissions through dreams at the sacred mountain. The ANE pattern: the king approaches the divine at a recognized sacred site, sleeps, the deity appears in a dream, issues a commission or promise, and the king fulfills it. Solomon&rsquo;s Gibeon theophany adapts this pattern with a significant modification: YHWH does not commission Solomon but asks what he wants — the divine initiative frames the encounter, but the content of the request is Solomon&rsquo;s. Gibeon (<em>giḇʿôn</em>) was both a major Canaanite city with treaty-protection obligations (Josh 9) and the site where the tabernacle of meeting had been located (2 Chr 1:3). The &lsquo;great high place&rsquo; (<em>habbāmāh gᵉḏôlāh</em>) represents the legitimate cultic center during the transitional period before the temple&rsquo;s construction — the theophany is historically situated in the interval between tabernacle and temple.</p>"
  },
  "4": {
    "29": "<p>The comparison of Solomon&rsquo;s wisdom with &lsquo;the wisdom of all the people of the east (<em>bᵉnê qeḏem</em>) and all the wisdom of Egypt&rsquo; places Solomonic wisdom within the two dominant intellectual traditions of the ancient world. The &lsquo;wisdom of the east&rsquo; refers to the Mesopotamian wisdom tradition: the Sumerian Instructions of Shuruppak (ca. 2600 BCE), the Akkadian Counsels of Wisdom, the Babylonian Theodicy (a dialogue on suffering, ca. 1000 BCE), and the encyclopedic wisdom of Arabian desert traditions (Prov 30-31 includes wisdom attributed to Agur and King Lemuel, with apparent Arabian connections). &lsquo;All the wisdom of Egypt&rsquo; encompasses the wisdom instructions (the Instruction of Amenemopet, ca. 1200-1100 BCE, closely paralleled in Prov 22:17-24:22) and the Egyptian <em>onomastica</em> — encyclopedic lists of natural categories (plants, animals, minerals, geographical features, professions) that constituted the curriculum of scribal education. The Onomasticon of Amenemopet (ca. 1100 BCE) lists 610 categories of natural and social phenomena. Solomon&rsquo;s speaking about &lsquo;trees, from the cedar that is in Lebanon to the hyssop that grows out of the wall&rsquo; and &lsquo;beasts and birds and reptiles and fish&rsquo; (v33) is precisely the encyclopedic natural-philosophy content of the onomastic tradition — demonstrating mastery within the ANE intellectual framework while surpassing it by grounding wisdom in the fear of YHWH (Prov 1:7).</p>"
  },
  "5": {
    "1": "<p>The Tyrian-Israelite alliance with Hiram king of Tyre (<em>ḥîrām melek ṣōr</em>) builds on the prior David-Hiram relationship (v1: &lsquo;for Hiram had always loved David&rsquo;) and reflects geopolitical complementarity. Tyre was the leading city of Phoenicia, the maritime trading power that dominated the eastern Mediterranean from approximately 1200 to 500 BCE. Lebanon cedar (<em>ʾarzê lᵉḇānôn</em>, the <em>Cedrus libani</em>) was the luxury building timber of the ancient world: straight-grained, aromatic, insect-resistant, and available in lengths impossible to obtain elsewhere. Egyptian builders had imported Byblos cedar since the 4th millennium BCE (the Phoenician port city of Byblos — <em>Gbl</em> — was so central to Egyptian timber supply that the city name entered Egyptian vocabulary). Mesopotamian rulers from Gudea of Lagash to Nebuchadnezzar II quarried Lebanon cedar. Phoenician craftsmen (<em>ḥāriš ʿēṣîm</em>, v6) were the Mediterranean world&rsquo;s most skilled builders in wood and stone. The economic basis of the alliance is explicit: Hiram provides cedar, cypress, and craftsmen; Solomon provides wheat and olive oil (v11) from Israel&rsquo;s fertile agricultural zones. The two economies are complementary — each lacking what the other has in abundance — making this a partnership rather than tribute. This geopolitical logic underlies the later naval partnership at Ezion-geber (9:26-28), where Phoenician seamanship extends Solomon&rsquo;s commercial reach to the Red Sea trade.</p>"
  }
}

def main():
    c = load_comm('mkt-context', '1kings')
    merge_comm(c, CONTEXT)
    save_comm('mkt-context', '1kings', c)
    count = sum(len(v) for v in CONTEXT.values())
    print(f'1kings mkt-context: wrote {count} verses across ch 3-5')

if __name__ == '__main__':
    main()
