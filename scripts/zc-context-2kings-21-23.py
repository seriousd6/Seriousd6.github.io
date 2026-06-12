"""
MKT Context Commentary — 2 Kings chapters 21–23
Run: python3 scripts/zc-context-2kings-21-23.py

Ch21: Manasseh's reign — the longest and most evil; the sin that made exile inevitable;
      child sacrifice in Hinnom valley; Assyrian vassal-cult context
Ch22: Finding the Book of the Law — Deuteronomy's rediscovery; Huldah the prophetess;
      scroll-discovery and covenant renewal in ANE context
Ch23: Josiah's reform — the most comprehensive reform in Kings; cult centralization;
      Josiah's death at Megiddo 609 BCE; the Passover of 23:21-23

ANE/historical context:
- 21:6: Manasseh's list of abominations — Assyrian vassal-cult practices
- 22:8: scroll discovery — parallels in ANE temple-library rediscovery narratives
- 22:14: Huldah the prophetess — female prophetic office in Israel and ANE
- 23:29: Megiddo 609 BCE — the Egyptian-Babylonian geopolitical context (Neco II)
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
  "21": {
    "6": "<p>The catalogue of Manasseh&rsquo;s abominations — child sacrifice in Hinnom valley, divination, omens, sorcery, mediums and necromancers — reflects a systematic incorporation of Assyrian vassal-cult practices alongside indigenous Canaanite religion. The Assyrian Empire regularly imposed elements of its religious system on vassal states: Neo-Assyrian documents from the 8th-7th century BCE show that vassal treaties required acknowledgment of the Assyrian gods and often installation of their symbols. Manasseh&rsquo;s 55-year reign (the longest of any Judahite king) coincided with the peak of Assyrian power under Esarhaddon and Ashurbanipal; the Assyrian annals mention Manasseh as a vassal king who provided materials for building projects in Nineveh. The <em>sārim</em> (servants of the host of heaven, v3) reflects the Assyrian <em>šamê u erṣeti</em> (heaven and earth) oath-formula; the installation of altars to the host of heaven in the two courts of the temple (v5) is the visual marker of Assyrian religious hegemony in the Jerusalem cult. 2 Chr 33:11-13 records a tradition of Manasseh&rsquo;s deportation to Babylon and repentance that the Kings account omits — the theological verdict in Kings (24:3: &lsquo;because of the sins of Manasseh&rsquo;) is the historian&rsquo;s assessment of the long-term covenant damage that even a repentant Manasseh could not undo.</p>"
  },
  "22": {
    "8": "<p>Hilkiah the high priest&rsquo;s discovery of the Book of the Law during temple repairs — <em>sēper hattôrāh māṣāʾtî bᵉḇêt YHWH</em>, &lsquo;I have found the Book of the Law in the house of YHWH&rsquo; — and the dramatic reading before the king with the tearing of garments as the response (v11) is one of the OT&rsquo;s most significant literary events. The scroll is almost universally identified by scholars as the core of Deuteronomy (or a Deuteronomy-like law code), and its discovery/reading triggers Josiah&rsquo;s comprehensive reform (ch23). ANE parallels exist for the discovery of ancient texts in temples: the Babylonian text known as the &lsquo;Cruciform Monument&rsquo; narrates Naram-Sin&rsquo;s discovery of an ancient royal inscription in a temple; Neo-Babylonian kings speak of restoring temples &lsquo;according to the original plans&rsquo; found in archives. The scroll-discovery narrative is, in historical terms, possibly the recovery of a Mosaic legal tradition that had been suppressed under Manasseh; in theological terms, it is the confrontation of the covenant community with the full weight of their covenant obligations after a generation of apostasy — the reading of the law that produces repentance and reform is the OT&rsquo;s pattern that Nehemiah&rsquo;s Ezra-reading (Neh 8) and Jesus&rsquo;s synagogue reading (Luke 4) continue.</p>",
    "14": "<p>Josiah sends to consult &lsquo;Huldah the prophetess, wife of Shallum son of Tikvah&rsquo; — <em>ḥuldāh hannᵉḇîʾāh ʾēšet šallum</em> — rather than the contemporaneous Jeremiah or Zephaniah, both prophetically active in this period. The choice is not explained; the narrative simply records that she was the authoritative prophetic voice consulted at this moment of covenant crisis. Female prophets in Israel include Miriam (Exod 15:20), Deborah (Judg 4:4), and Isaiah&rsquo;s wife (Isa 8:3). In the broader ANE, female prophets are attested at Mari (the <em>āpiltu</em> prophetess) and in Assyrian texts. Huldah&rsquo;s role is formally identical to male court prophets: she delivers an authoritative YHWH-oracle to the king&rsquo;s delegation in standard prophetic form (<em>kōh ʾāmar YHWH</em>, v15). The oracle she delivers is the oracle that confirms Josiah&rsquo;s reform as theologically warranted and promises him a peaceful death (v20 — a promise that the narrator allows to stand as fulfilled: Josiah dies in battle, but the verse&rsquo;s &lsquo;gathered to your grave in peace&rsquo; is understood as deliverance from seeing the exile). The NT&rsquo;s Anna (Luke 2:36-38) and Philip&rsquo;s daughters (Acts 21:9) continue the Huldah-pattern of female prophetic ministry within the covenant community.</p>"
  },
  "23": {
    "29": "<p>Josiah&rsquo;s death at Megiddo — <em>wayyēlek liqrāʾtô wayyᵉmîtēhû bᵉmegiddô kᵉrōʾtô</em>, &lsquo;he went to meet him and Pharaoh Neco killed him at Megiddo when he saw him&rsquo; — occurs in the context of the geopolitical transition between Assyrian and Babylonian hegemony. The year 609 BCE was the critical transition year: Assyria was collapsing under Babylonian pressure; Egypt under Pharaoh Neco II was marching north to support the remnant Assyrian forces and establish Egyptian control over the Levantine corridor before Babylon could fill the vacuum. Josiah&rsquo;s interception of Neco&rsquo;s march at Megiddo — the classic strategic chokepoint controlling the road from Egypt through the Jezreel Valley — is his attempt to prevent a hostile power from crossing Israelite territory. The strategic reasoning was sound; the outcome was fatal. Megiddo&rsquo;s historical identity as the decisive battle-site is embedded in the name: Rev 16:16 uses <em>Har Megiddon</em> (Mount Megiddo) as the site of the final eschatological battle — Armageddon — drawing on Megiddo&rsquo;s accumulated symbolic weight as the place where decisive battles are fought and kings die. The Chronicler (2 Chr 35:20-24) provides additional detail, including Neco&rsquo;s claim that his march was at God&rsquo;s command — an oracle Josiah did not heed, adding to the theological complexity of the narrative.</p>"
  }
}

def main():
    c = load_comm('mkt-context', '2kings')
    merge_comm(c, CONTEXT)
    save_comm('mkt-context', '2kings', c)
    count = sum(len(v) for v in CONTEXT.values())
    print(f'2kings mkt-context: wrote {count} verses across ch 21-23')

if __name__ == '__main__':
    main()
