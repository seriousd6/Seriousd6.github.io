"""
BPG Curation — Batch C63: reason;-reasonable;-reasoning → rock-badger (gaps 6419–6523)
Gaps reviewed: 105 (score-5 isbe-scholarly R entries — rechab, reconciliation, redemption,
reed, refiner, regeneration, rehoboth, rephaim, resurrection, revelation, reubenites,
rimmon compounds, robbery)

Redirects: rechab;-rechabites→rechab; reconcile;-reconciliation→reconcilation;
redeemer;-redemption→redeemer; reed-measuring/reed-grass→reed; refiner;-refining→refiner;
regeneration-baptismal→regeneration; rehoboth-by-the-river/rehoboth-ir→rehoboth;
rephaim-vale-of→rephaim-valley-of; resurrection→resurrection-of-the-dead;
resurrection-of-jesus-christ-the→resurrection-of-christ; reubenites→reuben-tribe-of;
revelation-of-john→revelation-book-of; rimmon-1/2/rock-of/rimmonah;-rimmono→rimmon;
rimmon-perez→rimmon-parez; river-the-great→river; robber;-robbery→robbery.
0 stub-needed; 22 redirects; 83 names-only.

Script: scripts/bpg-curate-63.py
Run: python3 scripts/bpg-curate-63.py  (from project root)
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
    "reason;-reasonable;-reasoning": {"status": "names-only"},   # ISBE compound; lexical
    "rebuke":                   {"status": "names-only"},   # 2 Tim 4:2; Tit 1:13; lexical
    "recah":                    {"status": "names-only"},   # 1 Chr 4:12; place; names-only
    "receipt-of-custom":        {"status": "names-only"},   # Matt 9:9 KJV "tax collector's booth"; archaic
    "receiver":                 {"status": "names-only"},   # lexical
    # ISBE compound; Jer 35; Easton has rechab.json
    "rechab;-rechabites":       {"status": "redirect-only", "redirect_to": "rechab"},
    "reclining":                {"status": "names-only"},   # table posture at meals; cultural; names-only
    # ISBE compound; Rom 5:10-11; 2 Cor 5:18-20; Easton has reconcilation.json (note Easton slug typo)
    "reconcile;-reconciliation": {"status": "redirect-only", "redirect_to": "reconcilation"},
    "record":                   {"status": "names-only"},   # lexical
    "recover":                  {"status": "names-only"},   # lexical
    "red":                      {"status": "names-only"},   # color; covered under "colors"
    "red-dragon":               {"status": "names-only"},   # Rev 12:3; symbolic; brief
    "red-heifer":               {"status": "names-only"},   # Num 19; purification rite; names-only
    "red-horse":                {"status": "names-only"},   # Zech 1:8; 6:2; Rev 6:4; symbolic; brief
    # ISBE compound; Isa 41:14; Tit 2:14; Easton has redeemer.json
    "redeemer;-redemption":     {"status": "redirect-only", "redirect_to": "redeemer"},
    "redness-of-eyes":          {"status": "names-only"},   # Prov 23:29 KJV; cultural; names-only
    "redound":                  {"status": "names-only"},   # 2 Cor 4:15 KJV "overflow"; archaic/lexical
    # ISBE; Ezek 40:5; 42:16; Easton has reed.json
    "reed-measuring":           {"status": "redirect-only", "redirect_to": "reed"},
    # ISBE; Exod 2:3; Job 8:11; Easton has reed.json
    "reed-grass":               {"status": "redirect-only", "redirect_to": "reed"},
    "reelias":                  {"status": "names-only"},   # Ezra 2:2 variant; apocryphal
    "reesaias":                 {"status": "names-only"},   # 1 Esd 5:8 variant; apocryphal
    # ISBE compound; Mal 3:2-3; Prov 17:3; Easton has refiner.json
    "refiner;-refining":        {"status": "redirect-only", "redirect_to": "refiner"},
    "reform":                   {"status": "names-only"},   # lexical
    "reformation":              {"status": "names-only"},   # Heb 9:10 KJV "time of reformation"; brief
    "refresh;-refreshing":      {"status": "names-only"},   # ISBE compound; Acts 3:19 "times of refreshing"; lexical
    "refuge":                   {"status": "names-only"},   # general; covered under "cities of refuge"
    "refuse":                   {"status": "names-only"},   # lexical
    "refute":                   {"status": "names-only"},   # lexical
    # ISBE; Tit 3:5 "renewing/washing of regeneration"; Easton has regeneration.json
    "regeneration-baptismal":   {"status": "redirect-only", "redirect_to": "regeneration"},
    "region":                   {"status": "names-only"},   # lexical
    "register":                 {"status": "names-only"},   # Ezra 2:62; Neh 7:64; lexical
    "rehearse":                 {"status": "names-only"},   # KJV "report/recount"; archaic
    # ISBE; Gen 36:37 city of Saul king of Edom; Easton has rehoboth.json
    "rehoboth-by-the-river":    {"status": "redirect-only", "redirect_to": "rehoboth"},
    # ISBE; Gen 10:11 city of Assyria; Easton has rehoboth.json
    "rehoboth-ir":              {"status": "redirect-only", "redirect_to": "rehoboth"},
    "reign":                    {"status": "names-only"},   # lexical
    "relationships-family":     {"status": "names-only"},   # ISBE scholarly; names-only
    "release":                  {"status": "names-only"},   # covered under "sabbatical year" and "jubilee"
    "religion":                 {"status": "names-only"},   # lexical
    "religion-comparative":     {"status": "names-only"},   # ISBE scholarly; names-only
    "religion-science-of":      {"status": "names-only"},   # ISBE scholarly; names-only
    "remainder":                {"status": "names-only"},   # lexical
    "remember;-remembrance":    {"status": "names-only"},   # ISBE compound; lexical
    "remission-of-sins":        {"status": "names-only"},   # covered under "forgiveness" in Easton
    "remnant":                  {"status": "names-only"},   # Isa 10:20-22; Rom 11:5; no Easton article
    "rending-of-garments":      {"status": "names-only"},   # mourning custom; Gen 37:29; 2 Sam 3:31; names-only
    "renew":                    {"status": "names-only"},   # lexical
    "repair":                   {"status": "names-only"},   # lexical
    "repetitions":              {"status": "names-only"},   # Matt 6:7 KJV "vain repetitions"; lexical
    # ISBE; 2 Sam 5:18,22; Easton has rephaim-valley-of.json
    "rephaim-vale-of":          {"status": "redirect-only", "redirect_to": "rephaim-valley-of"},
    "reproof;-reprove":         {"status": "names-only"},   # ISBE compound; 2 Tim 3:16; lexical
    "reptile":                  {"status": "names-only"},   # general; covered under specific animals
    "reputation":               {"status": "names-only"},   # lexical
    "require":                  {"status": "names-only"},   # lexical
    "resaias":                  {"status": "names-only"},   # apocryphal variant; 1 Esd 5:8
    "reservoir":                {"status": "names-only"},   # covered under "pool"
    "resh":                     {"status": "names-only"},   # Hebrew letter; covered under "Hebrew alphabet"
    "residue":                  {"status": "names-only"},   # lexical
    "respect-of-persons":       {"status": "names-only"},   # Acts 10:34; Jas 2:9; lexical
    "restitution;-restoration": {"status": "names-only"},   # ISBE compound; covered under specific articles
    "restoration":              {"status": "names-only"},   # covered under prophetic articles
    # ISBE general overview; Easton has resurrection-of-the-dead.json
    "resurrection":             {"status": "redirect-only", "redirect_to": "resurrection-of-the-dead"},
    # ISBE compound; Easton has resurrection-of-christ.json
    "resurrection-of-jesus-christ-the": {"status": "redirect-only", "redirect_to": "resurrection-of-christ"},
    "resurrection-gospel-of-the": {"status": "names-only"},  # apocryphal; too specialized
    "retain":                   {"status": "names-only"},   # lexical
    "retaliation":              {"status": "names-only"},   # "eye for eye"; covered under "law"
    "retention-of-sins":        {"status": "names-only"},   # John 20:23; covered under "forgiveness"
    "retribution":              {"status": "names-only"},   # covered under "judgment"
    # ISBE; Num 26:7; Easton has reuben-tribe-of.json
    "reubenites":               {"status": "redirect-only", "redirect_to": "reuben-tribe-of"},
    # ISBE; Easton has revelation-book-of.json
    "revelation-of-john":       {"status": "redirect-only", "redirect_to": "revelation-book-of"},
    "revellings":               {"status": "names-only"},   # Gal 5:21 KJV; lexical
    "revenge;-revenger":        {"status": "names-only"},   # ISBE compound; covered under "avenger of blood"
    "revenue":                  {"status": "names-only"},   # lexical
    "reverence":                {"status": "names-only"},   # lexical
    "revile":                   {"status": "names-only"},   # lexical
    "revive;-reviving":         {"status": "names-only"},   # ISBE compound; lexical
    "reward":                   {"status": "names-only"},   # lexical
    "rhinoceros":               {"status": "names-only"},   # translation of re'em; covered under "unicorn"
    "rhodocus":                 {"status": "names-only"},   # 2 Macc 13:21; apocryphal traitor
    "rib":                      {"status": "names-only"},   # Gen 2:21-22; anatomical; brief
    "ribband":                  {"status": "names-only"},   # Num 15:38 KJV "twisted cord"; archaic
    "riches":                   {"status": "names-only"},   # lexical; no dedicated Easton article
    "rid;-riddance":            {"status": "names-only"},   # ISBE compound; lexical
    "rie":                      {"status": "names-only"},   # Exod 9:32 KJV "rye/spelt"; archaic botanical
    "right":                    {"status": "names-only"},   # lexical
    # ISBE disambiguation; Judg 20:45; Easton has rimmon.json
    "rimmon-1":                 {"status": "redirect-only", "redirect_to": "rimmon"},
    # ISBE disambiguation; 2 Kgs 5:18 Syrian god; Easton has rimmon.json
    "rimmon-2":                 {"status": "redirect-only", "redirect_to": "rimmon"},
    # ISBE; Judg 20:45,47; Easton has rimmon.json
    "rimmon-rock-of":           {"status": "redirect-only", "redirect_to": "rimmon"},
    # ISBE variant spelling; Num 33:19-20; Easton has rimmon-parez.json
    "rimmon-perez":             {"status": "redirect-only", "redirect_to": "rimmon-parez"},
    # ISBE compound; Josh 19:13; 1 Chr 6:77; Easton has rimmon.json
    "rimmonah;-rimmono":        {"status": "redirect-only", "redirect_to": "rimmon"},
    "ringleader":               {"status": "names-only"},   # Acts 24:5 KJV; lexical
    "ringstreaked":             {"status": "names-only"},   # Gen 30:35-43 KJV "speckled/spotted"; archaic
    "riot":                     {"status": "names-only"},   # lexical
    "rising":                   {"status": "names-only"},   # lexical
    # ISBE; Gen 15:18 "great river, the Euphrates"; Easton has river.json
    "river-the-great":          {"status": "redirect-only", "redirect_to": "river"},
    "rivers-of-eden":           {"status": "names-only"},   # Gen 2:10-14; covered under "Eden"
    "rizia":                    {"status": "names-only"},   # 1 Chr 7:39 Asherite; minor
    "road-inroad":              {"status": "names-only"},   # ISBE compound; 1 Sam 27:10; lexical
    "road-way":                 {"status": "names-only"},   # lexical
    "roast":                    {"status": "names-only"},   # culinary; brief
    # ISBE compound; Isa 61:8; Nah 3:1; Easton has robbery.json
    "robber;-robbery":          {"status": "redirect-only", "redirect_to": "robbery"},
    "robbers-of-temples":       {"status": "names-only"},   # Acts 19:37 KJV; brief
    "robe":                     {"status": "names-only"},   # covered under "dress"
    "roboam":                   {"status": "names-only"},   # Greek form of Rehoboam; covered under rehoboam
    "rock-of-ages":             {"status": "names-only"},   # Isa 26:4; hymn reference; covered under "rock"
    "rock-badger":              {"status": "names-only"},   # Lev 11:5; hyrax/coney; covered under "coney"
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
    print(f'BPG Curation C63: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
