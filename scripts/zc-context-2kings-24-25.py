"""
MKT Context Commentary — 2 Kings chapters 24–25
Run: python3 scripts/zc-context-2kings-24-25.py

Ch24: The two sieges of Jerusalem (597 and 586 BCE) — Babylonian Chronicles attestation;
      Jehoiachin's deportation; the craftsmen and élite taken first
Ch25: The destruction of Jerusalem 586 BCE — Nebuzaradan, the temple burned;
      Gedaliah's assassination; Jehoiachin's release — the open ending

ANE/historical context:
- 24:10-12: Babylonian Chronicles (BM 21946) attest the 597 BCE siege and deportation
- 25:8-9: The Babylonian destruction of Jerusalem confirmed by archaeology (ash layers)
- 25:27-30: Jehoiachin's rations in Babylon — the Weidner Tablets (Babylonian ration lists)
- 25:22-25: Gedaliah at Mizpah — the Mizpah/Tell en-Nasbeh excavations
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
  "24": {
    "10": "<p>The first Babylonian siege and deportation (597 BCE) — Nebuchadnezzar coming against Jerusalem, Jehoiachin surrendering after three months, the king and his court taken to Babylon — is independently documented in the Babylonian Chronicles (British Museum tablet BM 21946, first published 1956 by Donald Wiseman). The Babylonian Chronicle for Nebuchadnezzar&rsquo;s seventh year reads: &lsquo;In the seventh year, in the month Kislev, the king of Akkad mustered his troops... and encamped against the city of Judah... on the second day of the month of Adar he seized the city and captured the king. He appointed there a king of his own choice, received its heavy tribute, and sent (them) to Babylon.&rsquo; The detail of &lsquo;a king of his own choice&rsquo; (Zedekiah) and the tribute match 2 Kgs 24:12-17 precisely. The date &lsquo;second day of Adar&rsquo; (March 16, 597 BCE) is one of the most precisely dated events in the entire OT, confirmed by an external source. The historical solidity of the 597 siege is the archaeological anchor for understanding the entire exile narrative: Ezekiel&rsquo;s dates (Ezek 1:1-2), Jeremiah&rsquo;s letters to the exiles (Jer 29), and Daniel&rsquo;s narrative (Dan 1:1-3) all presuppose the 597 deportation as their historical foundation.</p>"
  },
  "25": {
    "9": "<p>The destruction of Jerusalem in 586 BCE — the burning of the temple, the palace, and &lsquo;all the houses of Jerusalem; every great house he burned down&rsquo; — is corroborated by archaeological evidence across the city. Excavations in the Jewish Quarter of the Old City (Nahman Avigad&rsquo;s excavations, 1970s) exposed the &lsquo;Burnt Room&rsquo; and &lsquo;Burnt House,&rsquo; containing ash deposits, arrowheads of Babylonian type, and collapsed walls consistent with a major conflagration in the early 6th century BCE. The City of David excavations have similarly identified destruction layers with Babylonian-period ash and pottery. The Lachish Letters (ostraca found at Tell ed-Duweir/Lachish, 1935) — written in the final weeks before Lachish&rsquo;s fall to Nebuchadnezzar — document the desperate military communications of the last days of the Judahite cities, confirming the general picture of the Babylonian advance. The city&rsquo;s destruction was so complete that the archaeological record shows a near-total break in occupation for much of the 6th century: the burned layers are followed by minimal or no occupation deposits until the Persian period, corroborating 25:12&rsquo;s &lsquo;the rest of the people who were left in the land.&rsquo;</p>",
    "27": "<p>Jehoiachin&rsquo;s release from prison by Evil-merodach (Amel-Marduk, 562-560 BCE) and his elevation to eat at the king&rsquo;s table — the final verses of 2 Kings — is not only narratively significant but archaeologically corroborated. The Weidner Tablets (four cuneiform tablets found in Babylon, published 1939 by Ernst Weidner) are Babylonian royal ration lists from the reign of Nebuchadnezzar listing ration allocations for captives and foreign workers. Among the recipients listed are &lsquo;Ia-ʾu-kīnu, king of the land of Ia-a-ḫu-du&rsquo; (Jehoiachin, king of the land of Judah) and his five sons — dated to approximately 592 BCE, during Jehoiachin&rsquo;s captivity under Nebuchadnezzar. The Weidner Tablets confirm that Jehoiachin was alive in Babylon, identified by his royal title, and receiving official rations — consistent with the house-arrest situation implied by 2 Kgs 24:15 and the eventual release of 25:27-30. The tablets corroborate not only the historical details but the preservation of the royal title: Babylon acknowledged Jehoiachin as king even in captivity, which explains the continued Judahite expectation of restoration through the Davidic line (Ezek 1:2 dates his visions to &lsquo;the fifth year of Jehoiachin&rsquo;s exile&rsquo; — treating him as the legitimate regnant).</p>"
  }
}

def main():
    c = load_comm('mkt-context', '2kings')
    merge_comm(c, CONTEXT)
    save_comm('mkt-context', '2kings', c)
    count = sum(len(v) for v in CONTEXT.values())
    print(f'2kings mkt-context: wrote {count} verses across ch 24-25')

if __name__ == '__main__':
    main()
