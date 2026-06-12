"""
MKT Context Commentary — 2 Chronicles chapters 25–28
Run: python3 scripts/zc-context-2chronicles-25-28.py

Ch25: gêʾ hammelaḥ — Valley of Salt geography and Dead Sea campaign routes (25:11)
      Edomite gods / Qos-worship — epigraphic evidence of Seir's pantheon (25:14)
Ch26: Uzziah's building program — towers at Jerusalem; cisterns for agro-pastoral expansion (26:9-10)
      ḥiššᵉḇōnôt — earliest biblical reference to mechanical artillery / siege engines (26:15)
Ch27: Ammonite tribute formula — 100 talents silver + commodity tribute; comparative records (27:5)
Ch28: Syro-Ephraimite War — 735–732 BCE; best-attested military coalition in the prophetic record (28:5-6)
      Ahaz and Tiglath-pileser III — Assyrian annals confirm the vassal-tribute relationship (28:16-21)
      Damascus gods — Aramean pantheon and the syncretism of 28:23
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

DATA = {
  "25": {
    "11": "<p>The <em>gêʾ hammelaḥ</em> (Valley of Salt) is one of the few campaign sites in Chronicles that can be located with confidence. The valley is most likely the Wadi el-Milh southeast of Beersheba or the salt flats at the southern end of the Dead Sea (modern Nahal Hamelaḥ). Salt valleys appear in ancient Near Eastern records as traditional sites for decisive engagements on the margins of controlled territory — neutral, uninhabitable ground ideal for pitched battles. The same location appears in 2 Sam 8:13 (David's campaign) and 1 Chr 18:12 (Abishai). Amaziah's victory against 10,000 Edomites and the execution of 10,000 captives thrown from a cliff (<em>hasselaʿ</em>) likely refers to a rocky escarpment in the Arabah region south of the Dead Sea — comparable to the cliff-executions attested in Neo-Assyrian records of campaign prisoners.</p>",
    "14": "<p>The Edomite gods Amaziah imports after his victory are not named, but the primary deity of Edom was <em>Qos</em> (or <em>Qaus</em>), attested in numerous personal names from the epigraphic record: Qosgabar, Qosmalak, Qosanal. Qos appears at Tell el-Kheleifeh (Ezion-geber), at Kuntillet Ajrud, and in Assyrian vassal lists. The deity was likely a weather/storm god analogous to Baal; some inscriptions from the Negev show Qos appearing alongside YHWH in blessing formulas. The Chronicler's irony is pointed: Amaziah defeats Edom's gods in their home territory (their armies failed), then installs those same defeated gods in Jerusalem. The divine messenger's rhetorical question (v. 15) — 'why have you sought the gods of a people who could not deliver their own people from your hand?' — frames the episode as absurdist covenant failure.</p>"
  },
  "26": {
    "9": "<p>Uzziah's building program in vv. 9-10 represents some of the most archaeologically recoverable royal activity in Chronicles. The corner gate (<em>šaʿar hapinnāh</em>) and valley gate (<em>šaʿar hagêʾ</em>) towers at Jerusalem, and the towers at the <em>hammiqṣôaʿ</em> (the Millo/corner), correspond to areas of Iron IIb construction visible in the excavations of Eilat Mazar and the Kenyon-era trenches in the Ophel. Uzziah's agricultural development — the cisterns (<em>bōrôt</em>) in the <em>midbar</em> (wilderness/steppe) and <em>šᵉpēlāh</em> (lowlands) for livestock — reflects a period of Judahite territorial expansion into the Negev confirmed by the proliferation of Iron IIb farmsteads and storage facilities at sites like Tel Beer-sheba, Tel Masos, and Aroer. The reference to his love of the <em>ʾaḏāmāh</em> (agricultural land) marks him as a farmer-king in the tradition of ANE royal estate management.</p>",
    "15": "<p>The <em>ḥiššᵉḇōnôt</em> (26:15) — translated 'engines,' 'machines,' 'devices' — represents the earliest mention of mechanical military technology in the Hebrew Bible. The noun derives from the root <em>ḥāšaḇ</em> (to devise, calculate) and refers to catapult or artillery-type devices for projecting stones and large arrows from the walls and towers of Jerusalem. Comparable siege equipment is well-attested in Assyrian reliefs from the 9th–8th centuries (Sennacherib's palace at Nineveh depicts elaborate siege towers and counter-machinery); Mesopotamian texts describe stone-throwing siege engines in campaigns against walled cities. The verse notes these were 'devised by skillful men' — the same craft-wisdom vocabulary used for Bezalel. Uzziah's investment in defensive technology during a period of military expansion (vv. 6-8) reflects the pattern of Iron Age Levantine kingdoms upgrading fortification systems as Assyrian power increased.</p>"
  },
  "27": {
    "5": "<p>The Ammonite tribute Jotham imposes — 100 talents of silver, 10,000 kors of wheat, 10,000 of barley — is one of the most specific tribute amounts in Chronicles. The quantities are substantial: 100 talents of silver (~3.4 metric tons) is comparable to the tribute Menahem of Israel paid Tiglath-pileser III (2 Kgs 15:19-20: 1,000 talents). The grain amounts (kors = large capacity measures) suggest a three-year obligation (<em>šānāh bᵉšānāh</em> — year after year — is the formula for regular tribute rather than one-time payment). Comparative tribute records from Neo-Assyrian annals show similar silver + commodity (grain, oil, livestock) combination formats for vassal payments, and the proportions here are consistent with Iron Age II Levantine regional power. The Ammonites' payment ending in the third year (implicitly) is a realistic diplomatic detail suggesting a renegotiated treaty rather than full subjugation.</p>"
  },
  "28": {
    "5": "<p>The Syro-Ephraimite War (c. 735–732 BCE) is the historical backdrop for 2 Chr 28:5-21 and one of the best-attested events of the divided monarchy period. The coalition of Rezin of Aram (Damascus) and Pekah of Israel (2 Kgs 16:5; Isa 7:1) attacked Ahaz of Judah, pressuring him to join an anti-Assyrian coalition. The Assyrian king Tiglath-pileser III's own annals (ANET 282-284) record the subjugation of Israel, the taking of Philistine and Galilean territories, and the execution of Pekah's successor — providing an external check on the biblical sequence. Isaiah's Immanuel oracle (Isa 7) was delivered in this context, promising that both Rezin and Pekah would fall within 65 years. The Chronicler's account focuses on Judah's military catastrophe (120,000 killed, 200,000 captives) as covenantal consequence of Ahaz's idolatry rather than on the geopolitical dynamics.</p>",
    "16": "<p>Ahaz's appeal to Tiglath-pileser III of Assyria is confirmed by multiple external sources. The Assyrian annals record Ahaz (spelled <em>Ia-u-ha-zi</em> in cuneiform) as a vassal who brought tribute: gold, silver, tin, iron, linen, purple wool. Ahaz's tribute in 2 Kgs 16:8 ('took the silver and gold found in the temple of YHWH') maps onto this pattern of stripping cult resources to pay imperial tribute. The Chronicler's note that Tiglath-pileser 'distressed him but did not help him' (v. 20) reflects the Assyrian pattern: receiving tribute from Ahaz while simultaneously campaigning against his neighbors, the Assyrian presence in the region turned the hoped-for ally into an overlord extracting additional payment. Tel Dan Stele, the Mesha Stele, and the Black Obelisk of Shalmaneser III provide the broader context of how Assyria processed Levantine vassals.</p>",
    "23": "<p>The 'gods of Damascus' Ahaz sacrifices to after his defeat by Aram (28:23) — reasoning that Aram's gods helped them win — draws on the standard ancient Near Eastern logic of divine patron selection by military outcome: victorious gods are powerful gods. The Aramean pantheon at Damascus was headed by Hadad (= Baal-Hadad), the storm deity, with Rimmon (= Rammon, attested in Naaman's story: 2 Kgs 5:18) as a significant variant or epithet. Aramean religious influence in the Levant is well-documented: Aramaic spread as the diplomatic lingua franca and Hadad-worship left traces in Judahite personal names (Hadadezer, Ben-hadad) and in cultic installations at sites like Tell Halaf and Arslan Tash. The Chronicler's theological judgment — 'the gods of the kings of Aram help them' is Ahaz's reasoning, which the text presents as catastrophically wrong — reflects the pattern of covenant-breaking through theological opportunism.</p>"
  }
}

def main():
    c = load_comm('mkt-context', '2chronicles')
    merge_comm(c, DATA)
    save_comm('mkt-context', '2chronicles', c)
    count = sum(len(v) for v in DATA.values())
    print(f'2chronicles mkt-context: wrote {count} verses across ch 25-28')

if __name__ == '__main__':
    main()
