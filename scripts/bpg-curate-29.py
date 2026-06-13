"""
BPG Curation — Batch C29: barodis → berries (gaps 2799–2898)
Gaps reviewed: 100 (all score-5 isbe-scholarly entries, B range)

Clusters: apocryphal variants (1 Esd: barodis, basaloth, bassa, bassai, bastai,
basthai, beelsarus, beeltethmus, belemus, belmaim → names-only), Solomon's district
officers (ben-abinadab/deker/geber/hesed/hur → all names-only), ISBE word studies
(before, begin, beginning, beloved, benefit, berries).

Redirects: basemath;-bashemath;-basmath → bashemath; benjamite → benjamin;
beroea → berea.

Script: scripts/bpg-curate-29.py
Run: python3 scripts/bpg-curate-29.py  (from project root)
"""

import json

GAPS_FILE = 'data/biblepedia/gaps.json'


def load_gaps():
    with open(GAPS_FILE, encoding='utf-8') as f:
        return json.load(f)


def save_gaps(gaps):
    with open(GAPS_FILE, 'w', encoding='utf-8') as f:
        json.dump(gaps, f, ensure_ascii=False, indent=2)


DECISIONS = {
    "barodis":                       {"status": "names-only"},   # ISBE; 1 Esd 5:34 variant; apocryphal
    "barren;-barrenness":            {"status": "names-only"},   # ISBE word study
    "barsabas;-barsabbas":           {"status": "names-only"},   # ISBE; Acts 1:23/15:22; no Easton barsabbas.json
    "bartacus":                      {"status": "names-only"},   # ISBE; 1 Esd 4:29; apocryphal figure
    "bartholomew-gospel-of":         {"status": "names-only"},   # ISBE; apocryphal gospel; extracanonical
    "baruch-apocalypse-of":          {"status": "names-only"},   # ISBE; 2 Baruch; apocryphal pseudepigrapha
    "basaloth":                      {"status": "names-only"},   # ISBE; 1 Esd variant; apocryphal
    "bascama":                       {"status": "names-only"},   # ISBE place; 1 Macc 13:23; apocryphal
    "base":                          {"status": "names-only"},   # ISBE word study
    # ISBE triple combined; Easton has bashemath.json (Esau's wife; Gen 26:34)
    "basemath;-bashemath;-basmath":  {"status": "redirect-only", "redirect_to": "bashemath"},
    "bashan-havvoth-jair":           {"status": "names-only"},   # ISBE; Deut 3:14 Jair's tent-villages
    "basin;-bason":                  {"status": "names-only"},   # ISBE combined; KJV vessel; word study
    "bason":                         {"status": "names-only"},   # ISBE KJV variant of "basin"; word study
    "bassa":                         {"status": "names-only"},   # ISBE; 1 Esd 5:16 variant; apocryphal
    "bassai":                        {"status": "names-only"},   # ISBE; 1 Esd variant; apocryphal
    "bastai":                        {"status": "names-only"},   # ISBE; 1 Esd variant; apocryphal
    "basthai":                       {"status": "names-only"},   # ISBE; 1 Esd variant; apocryphal
    "batanaea":                      {"status": "names-only"},   # ISBE; Bashan/Gaulanitis region; general
    "bath-kol":                      {"status": "names-only"},   # ISBE; Jewish "daughter of a voice"; general
    "bath-rabbim-the-gate-of":       {"status": "names-only"},   # ISBE; Song 7:4 gate at Heshbon
    "bath-zacharias":                {"status": "names-only"},   # ISBE; 1 Macc 6:32 battle site; apocryphal
    "battle":                        {"status": "names-only"},   # ISBE word study; general
    "bavvai":                        {"status": "names-only"},   # ISBE; Neh 3:18 wall-builder; minor figure
    "bay-1":                         {"status": "names-only"},   # ISBE numbered; bay tree or sea bay
    "bay-2":                         {"status": "names-only"},   # ISBE place; sea inlet; numbered
    "bayith":                        {"status": "names-only"},   # ISBE place; Isa 15:2 Moabite temple site
    "bazlith;-bazluth":              {"status": "names-only"},   # ISBE combined; Ezra 2:52 servant family
    "beach":                         {"status": "names-only"},   # ISBE word study
    "bean":                          {"status": "names-only"},   # ISBE; 2 Sam 17:28 food; plant; general
    "bear-the-arcturus":             {"status": "names-only"},   # ISBE; Arcturus/bear constellation (Job 38:32)
    "bear;-born":                    {"status": "names-only"},   # ISBE word study
    "bear;-borne":                   {"status": "names-only"},   # ISBE word study
    "beast-fight":                   {"status": "names-only"},   # ISBE; 1 Cor 15:32 "fought with beasts"
    "beating":                       {"status": "names-only"},   # ISBE word study
    "beatitudes":                    {"status": "names-only"},   # ISBE; Matt 5:3-12; score-5 → names-only
    "beauty":                        {"status": "names-only"},   # ISBE word study
    "beauty-and-bands":              {"status": "names-only"},   # ISBE; Zech 11:7 two staves (variant entry)
    "because":                       {"status": "names-only"},   # ISBE word study
    "beck;-beckon":                  {"status": "names-only"},   # ISBE word study
    "become":                        {"status": "names-only"},   # ISBE word study
    "becorath":                      {"status": "names-only"},   # ISBE; Saul's ancestor (1 Sam 9:1)
    "bectileth":                     {"status": "names-only"},   # ISBE place; Jdt 2:21; apocryphal
    "bed;-bedchamber;-bedstead":     {"status": "names-only"},   # ISBE combined; furniture; general
    "beef":                          {"status": "names-only"},   # ISBE; food reference; general
    "beelsarus":                     {"status": "names-only"},   # ISBE; 1 Esd 5:8 variant; apocryphal
    "beeltethmus":                   {"status": "names-only"},   # ISBE; 1 Esd 2:16 variant; apocryphal
    "beeroth-bene-jaakan":           {"status": "names-only"},   # ISBE; Deut 10:6 desert station
    "beerothite;-berothite":         {"status": "names-only"},   # ISBE combined; from Beeroth; demonym
    "before":                        {"status": "names-only"},   # ISBE word study
    "beg;-beggar;-begging":          {"status": "names-only"},   # ISBE combined word study
    "beggarly":                      {"status": "names-only"},   # ISBE word study (Gal 4:9)
    "begin":                         {"status": "names-only"},   # ISBE word study
    "beginning":                     {"status": "names-only"},   # ISBE word study; general
    "begotten":                      {"status": "names-only"},   # ISBE word study; general
    "beguile":                       {"status": "names-only"},   # ISBE word study
    "behalf":                        {"status": "names-only"},   # ISBE word study
    "behavior":                      {"status": "names-only"},   # ISBE word study
    "beheading":                     {"status": "names-only"},   # ISBE; decapitation; general
    "beholding":                     {"status": "names-only"},   # ISBE word study
    "behoove":                       {"status": "names-only"},   # KJV "it behoved" (Luke 24:46); word study
    "beirut":                        {"status": "names-only"},   # ISBE; modern Beirut = ancient Berytus
    "beka":                          {"status": "names-only"},   # ISBE; half-shekel weight (Exod 38:26)
    "bel-and-the-dragon":            {"status": "names-only"},   # ISBE; apocryphal addition to Daniel
    "bela;-belah":                   {"status": "names-only"},   # ISBE combined; Edomite king (Gen 36:32)
    "belaites":                      {"status": "names-only"},   # ISBE; Bela's clan (Num 26:38)
    "belch":                         {"status": "names-only"},   # ISBE word study (Ps 59:7 KJV)
    "belemus":                       {"status": "names-only"},   # ISBE; 1 Esd variant; apocryphal
    "belie":                         {"status": "names-only"},   # ISBE word study
    "belief":                        {"status": "names-only"},   # ISBE word study; general
    "believers":                     {"status": "names-only"},   # ISBE word study; general
    "belmaim":                       {"status": "names-only"},   # ISBE; Jdt 4:4; apocryphal place
    "belmen;-belmon":                {"status": "names-only"},   # ISBE combined; variant place names
    "belomancy":                     {"status": "names-only"},   # ISBE; divination by arrows (Ezek 21:21)
    "beloved":                       {"status": "names-only"},   # ISBE word study; general
    "belt":                          {"status": "names-only"},   # ISBE; clothing; general
    "belus-temple-of":               {"status": "names-only"},   # ISBE; Babylonian temple of Bel
    "ben-abinadab":                  {"status": "names-only"},   # ISBE; Solomon's district officer (1 Kgs 4:11)
    "ben-deker":                     {"status": "names-only"},   # ISBE; Solomon's officer (1 Kgs 4:9)
    "ben-geber":                     {"status": "names-only"},   # ISBE; Solomon's officer (1 Kgs 4:13)
    "ben-hesed":                     {"status": "names-only"},   # ISBE; Solomon's officer (1 Kgs 4:10)
    "ben-hur":                       {"status": "names-only"},   # ISBE; Solomon's officer (1 Kgs 4:8)
    "ben-jaakan":                    {"status": "names-only"},   # ISBE; Beeroth-bene-jaakan (Deut 10:6)
    "beneath":                       {"status": "names-only"},   # ISBE word study
    "benediction":                   {"status": "names-only"},   # ISBE; blessing formula; score-5 → names-only
    "benefactor":                    {"status": "names-only"},   # ISBE word study (Luke 22:25)
    "benefit":                       {"status": "names-only"},   # ISBE word study
    "benevolence":                   {"status": "names-only"},   # ISBE word study (1 Cor 7:3 KJV)
    "benjamin-gate-of":              {"status": "names-only"},   # ISBE; Jer 20:2; 37:13 Jerusalem gate
    # ISBE demonym; Easton has benjamin.json (Rachel's son; Gen 35:18)
    "benjamite":                     {"status": "redirect-only", "redirect_to": "benjamin"},
    "beracah":                       {"status": "names-only"},   # ISBE; 1 Chr 12:3 David's warrior; minor
    "beracah-valley-of":             {"status": "names-only"},   # ISBE; 2 Chr 20:26 Valley of Blessing
    "bereave;-bereaver;-bereft":     {"status": "names-only"},   # ISBE combined word study
    "bered-1":                       {"status": "names-only"},   # ISBE numbered; Shuthela's son (Gen 46:20 variant)
    "bered-2":                       {"status": "names-only"},   # ISBE place; near Kadesh (Gen 16:14)
    "beriah;-beriites":              {"status": "names-only"},   # ISBE combined; Asher's son (Gen 46:17) + clan
    "berites":                       {"status": "names-only"},   # ISBE; 2 Sam 20:14; obscure people
    # ISBE place; Macedonian Berea; Easton has berea.json (Acts 17:10-11)
    "beroea":                        {"status": "redirect-only", "redirect_to": "berea"},
    "beroth":                        {"status": "names-only"},   # ISBE; Ezra/Neh variant of Beeroth
    "berothite":                     {"status": "names-only"},   # ISBE; demonym variant of Beerothite
    "berries":                       {"status": "names-only"},   # ISBE word study (Jas 3:12; Isa 17:6)
}


def main():
    gaps = load_gaps()
    idx = {g['id']: g for g in gaps}
    updated = 0
    missing = []
    for gid, decision in DECISIONS.items():
        if gid in idx:
            idx[gid].update(decision)
            updated += 1
        else:
            missing.append(gid)
    if missing:
        print(f'WARNING: {len(missing)} gap ids not found: {missing}')
    save_gaps(list(idx.values()))
    print(f'BPG Curation C29: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
