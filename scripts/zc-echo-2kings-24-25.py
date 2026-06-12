"""
echo — 2 Kings 24–25
run: python3 scripts/zc-echo-2kings-24-25.py

Ch24: Nebuchadnezzar's first deportation — Jehoiakim, then Jehoiachin taken; 10,000 captives
Ch25: Fall of Jerusalem; temple burned; Gedaliah; Jehoiachin released — flickering lamp of hope
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_echo(book, data):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_echo(existing, new_data):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, entries in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entries
            else:
                seen = {(e['type'], e['target']) for e in existing[ch][v]}
                for e in entries:
                    if (e['type'], e['target']) not in seen:
                        existing[ch][v].append(e)
                        seen.add((e['type'], e['target']))

KINGS2_ECHO = {
  "24": {
    "3": [
      {"type": "allusion", "target": "Matt 23:35", "note": "YHWH sends the Babylonian raiding parties against Judah to remove them from his sight for the sins of Manasseh — specifically for the innocent blood he shed, which YHWH was not willing to pardon (v4); the principle that accumulated covenant-breaking and innocent blood eventually demands reckoning on a single generation is the same structure Jesus announces in Matt 23:35-36: that upon you may come all the righteous blood shed on earth, from the blood of righteous Abel to the blood of Zechariah — all this will come upon this generation; Manasseh's generation deferred judgment; Jehoiakim's generation received it"},
      {"type": "allusion", "target": "Luke 11:50", "note": "The exile under Nebuchadnezzar is explicitly attributed to Manasseh's sin of innocent blood (v3-4) — YHWH was not willing to pardon this; Jesus in Luke 11:50-51 announces the same principle of generational reckoning: the blood of all the prophets, shed from the foundation of the world, may be charged against this generation; both texts show the same divine economy: covenant communities accumulate guilt over generations; that guilt is eventually collected at a point of crisis-judgment"}
    ]
  },
  "25": {
    "9": [
      {"type": "fulfillment", "target": "Matt 24:2", "note": "Nebuzaradan burned the house of YHWH and the king's house and all the houses of Jerusalem — the great buildings of Jerusalem destroyed; 1 Kgs 9:7-9 had warned that if Israel turned from YHWH the house he had consecrated for his name would be cut off and destroyed, and all who passed by it would be appalled; Jesus announces the second fulfillment of this pattern in Matt 24:2: truly I say to you, there will not be left here one stone upon another that will not be thrown down; the 586 BC destruction is the type of which AD 70 is the antitype, both expressing the same divine logic of consecrated-space-forfeited-by-covenant-breaking"},
      {"type": "allusion", "target": "John 2:19", "note": "The destruction of the temple in v9 is the historical culmination of the repeated warnings from Solomon's dedication prayer (1 Kgs 8:46-53) and YHWH's response (1 Kgs 9:6-9): unfaithfulness costs the house; Jesus in John 2:19 — destroy this temple and in three days I will raise it up — announces himself as the true and indestructible temple, the reality to which the Solomonic house pointed; after the 586 destruction, Ezekiel's glory-departure (Ezek 10-11) prepares for the radical re-centering of YHWH's presence in the person of the Messiah"}
    ],
    "27": [
      {"type": "allusion", "target": "Matt 1:12", "note": "Evil-merodach king of Babylon released Jehoiachin from prison in the thirty-seventh year of his exile and spoke kindly to him and gave him a seat above the seats of the kings who were with him in Babylon — the book of Kings ends not with Zedekiah in captivity but with the legitimate Davidic heir Jehoiachin eating at the king's table; Jehoiachin (= Jeconiah) appears in Matt 1:12 in the genealogy of Jesus: after the deportation to Babylon, Jechoniah was the father of Shealtiel; the flickering lamp of 2 Kgs 8:19 and 1 Kgs 11:36 has been kept alive through exile and prison to carry the Davidic line to its fulfillment in Christ"},
      {"type": "fulfillment", "target": "Luke 1:33", "note": "Jehoiachin's elevation to the king's table is the final act of 2 Kings — and its structural function is to show that the Davidic lamp (2 Kgs 8:19; 1 Kgs 11:36; Ps 132:17) has not been extinguished by exile; the kingdom is in suspense, not ended; the angel's announcement to Mary in Luke 1:33 — of his kingdom there will be no end — is the ultimate resolution of this suspension: the son who would occupy David's throne forever is the one Jehoiachin's preserved lineage made possible; the book of Kings ends with Davidic hope deferred; Luke 1 announces the deferral over"}
    ]
  }
}

def main():
    e = load_echo('2kings')
    merge_echo(e, KINGS2_ECHO)
    save_echo('2kings', e)
    print('2kings ch24-25 echo: done')

if __name__ == '__main__':
    main()
