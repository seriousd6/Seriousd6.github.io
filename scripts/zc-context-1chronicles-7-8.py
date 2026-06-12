"""
MKT Context Commentary — 1 Chronicles chapters 7–8
Run: python3 scripts/zc-context-1chronicles-7-8.py

Ch7: Sheerah's Beth-horons — a woman builder of strategically vital towns (7:24)
Ch8: Gibeon's Benjaminite genealogy — James Pritchard's el-Jib excavations (8:29)
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
  "7": {
    "24": "<p>The note that Sheerah &lsquo;built Lower Beth-horon and Upper Beth-horon and Uzzen-sheerah&rsquo; — <em>ûḇittô šᵉʾērāh wayyiḇen ʾet bêt ḥôrôn haṭṭaḥtônāh wᵉʾet hāʿelyônāh wᵉʾet ʾuzzên šᵉʾērāh</em> — is one of the OT&rsquo;s most striking attributions: a woman founder of towns that are strategically central to Israel&rsquo;s history. Beth-horon (Upper and Lower) controlled the ascent from the Aijalon Valley in the Shephelah into the Judean hill country — the main western approach to Jerusalem. The site appears repeatedly in Israelite military history: Joshua pursued the Amorite coalition through Beth-horon after the Gibeon battle, and YHWH threw down great stones on the fleeing enemy there (Josh 10:10-11); it marks the tribal boundary between Benjamin and Ephraim (Josh 16:3,5; 18:13-14); the Philistines raided through the Beth-horon pass (1 Sam 13:18); and Judas Maccabaeus defeated Seron at Beth-horon in 166 BCE (1 Macc 3:16-24). Solomon later fortified both towns (1 Kgs 9:17). Archaeological survey of the Beth-horon sites (Beit Ur et-Tahta and Beit Ur el-Foqa) has identified Iron Age remains consistent with their role as defended pass-towns. The Chronicler&rsquo;s attribution of the towns&rsquo; founding to Sheerah (who also gives her name to Uzzen-sheerah, &lsquo;the ear/district of Sheerah&rsquo;) preserves a tribal tradition of female civic agency that ANE genealogical texts occasionally record for shrines and chapels but rarely for military-strategic fortifications.</p>"
  },
  "8": {
    "29": "<p>The notation &lsquo;Jeiel the father of Gibeon lived in Gibeon&rsquo; — <em>ûḇigᵉḇaʿôn yāšaḇ ʾăḇî giḇᵉʿôn</em> — places the Benjaminite genealogy at Gibeon, the Hivite city-state whose covenant with Israel (Josh 9:3-27) gave it protected status as &lsquo;hewers of wood and drawers of water&rsquo; for the sanctuary. Gibeon is modern el-Jib (7 km north of Jerusalem), excavated by James Pritchard for the University of Pennsylvania (1956-62). The excavations produced several significant finds: (1) a large rock-cut pool (diameter c. 11.3 m, depth c. 10.8 m) matching the &lsquo;pool of Gibeon&rsquo; of 2 Sam 2:13 where the combat between David&rsquo;s and Ishbosheth&rsquo;s men took place; (2) jar handles inscribed with the place-name <em>gʿbn</em> (Gibeon) in Iron Age II script, confirming the site identification; (3) extensive wine-storage cellars cut into the rock, suggesting Gibeon was a major production and distribution center for wine in the 8th-7th centuries BCE. The Gibeonites&rsquo; absorption into Benjamin in the Chronicler&rsquo;s genealogy (tracing the founder back to a Benjaminite ancestor) reflects the post-exilic community&rsquo;s need to establish tribal-territorial legitimacy for towns in the Benjamin plateau — Gibeon being one of the most important sites in that region and one whose history straddled Canaanite, Hivite, and Israelite identities.</p>"
  }
}

def main():
    c = load_comm('mkt-context', '1chronicles')
    merge_comm(c, CONTEXT)
    save_comm('mkt-context', '1chronicles', c)
    count = sum(len(v) for v in CONTEXT.values())
    print(f'1chronicles mkt-context: wrote {count} verses across ch 7-8')

if __name__ == '__main__':
    main()
