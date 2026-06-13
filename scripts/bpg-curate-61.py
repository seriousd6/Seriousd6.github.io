"""
BPG Curation — Batch C61: plain-of-moab → prognosticators-monthly (gaps 6214–6313)
Gaps reviewed: 100 (score-5 isbe-scholarly P entries — plain compounds, plane/plane-tree,
plow/plough, pool, porch of Solomon, poti-phera, potter/pottery, praetorian,
prayer-lords, priest-high, prisca/priscilla, prison)

Redirects: plain-cities-of-the→plain; plane→plane-tree; plow→plough;
pommel→pommels; pool/pond/reservoir→pool; porch-portico-solomons→porch-solomons;
port/porter→porter; poti-phera→potipherah; potter/pottery→pottery;
praetorian-guard→praetorium; prayer-lords→lords-prayer;
priest-high→priest; prisca/priscilla→priscilla; prison/prisoner→prison.
0 stub-needed; 14 redirects; 86 names-only.

Script: scripts/bpg-curate-61.py
Run: python3 scripts/bpg-curate-61.py  (from project root)
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
    "plain-of-moab":             {"status": "names-only"},   # Num 22:1; 36:13; specific OT locale; names-only
    "plain-of-the-pillar":       {"status": "names-only"},   # Judg 9:6; Shechem area; names-only
    "plain-of-the-vineyards":    {"status": "names-only"},   # Num 21:22 KJV; names-only
    # ISBE; Gen 13:12 "cities of the plain"; Easton has plain.json
    "plain-cities-of-the":       {"status": "redirect-only", "redirect_to": "plain"},
    "plain;-plainly":            {"status": "names-only"},   # ISBE compound; lexical
    "plaister":                  {"status": "names-only"},   # Lev 14:42,43; Deut 27:2 KJV "plaster"; lexical
    "plaiting":                  {"status": "names-only"},   # 1 Pet 3:3 KJV; cultural; names-only
    # ISBE; Isa 44:13; Gen 30:37; Easton has plane-tree.json
    "plane":                     {"status": "redirect-only", "redirect_to": "plane-tree"},
    "planets":                   {"status": "names-only"},   # 2 Kgs 23:5 KJV; lexical
    "plank":                     {"status": "names-only"},   # Ezek 27:5; 1 Kgs 6:15; lexical
    "plant-plants":              {"status": "names-only"},   # ISBE compound; Gen 2:5; Ps 128:3; lexical
    "plaster-1":                 {"status": "names-only"},   # ISBE disambiguation; Lev 14:42; names-only
    "plaster-2":                 {"status": "names-only"},   # ISBE disambiguation; architectural; names-only
    "plastering":                {"status": "names-only"},   # Lev 14:42-43; architectural; names-only
    "plate":                     {"status": "names-only"},   # Exod 28:36; Num 16:38; lexical
    "platter":                   {"status": "names-only"},   # Matt 23:25; Luke 11:39 KJV; lexical
    "play":                      {"status": "names-only"},   # lexical
    "plead":                     {"status": "names-only"},   # Isa 1:17; Mic 6:2; lexical
    "pleasure":                  {"status": "names-only"},   # lexical
    "pleroma":                   {"status": "names-only"},   # ISBE; Col 1:19; Eph 1:23 "fullness"; names-only
    # ISBE; Isa 28:24; Easton has plough.json
    "plow":                      {"status": "redirect-only", "redirect_to": "plough"},
    "plucking-off-the-hair":     {"status": "names-only"},   # Neh 13:25; Isa 50:6; cultural; names-only
    "plumb-line;-plummet":       {"status": "names-only"},   # ISBE compound; Amos 7:7-8; names-only
    "pochereth-hazzebaim":       {"status": "names-only"},   # Ezra 2:57; Neh 7:59; temple servant; names-only
    "poet":                      {"status": "names-only"},   # Acts 17:28; names-only
    "poetry-new-testament":      {"status": "names-only"},   # ISBE scholarly; names-only
    "points":                    {"status": "names-only"},   # lexical
    "pole":                      {"status": "names-only"},   # Num 21:8-9; Isa 30:17 KJV; lexical
    "policy":                    {"status": "names-only"},   # Dan 8:25 KJV; names-only
    "polished":                  {"status": "names-only"},   # lexical
    "poll":                      {"status": "names-only"},   # Num 1:2,18,20 KJV "by the poll"; Ezek 44:20; lexical
    "pollution":                 {"status": "names-only"},   # Ezek 20:30-31; lexical
    # ISBE; 1 Kgs 7:41-42; Easton has pommels.json
    "pommel":                    {"status": "redirect-only", "redirect_to": "pommels"},
    "ponder":                    {"status": "names-only"},   # Prov 4:26; Luke 2:19; lexical
    # ISBE compound; John 5:2; Isa 22:11; Easton has pool.json
    "pool;-pond;-reservoir":     {"status": "redirect-only", "redirect_to": "pool"},
    # ISBE; John 10:23; Acts 3:11; Easton has porch-solomons.json
    "porch-portico-solomons":    {"status": "redirect-only", "redirect_to": "porch-solomons"},
    "porcupine":                 {"status": "names-only"},   # Isa 14:23; 34:11 KJV "bittern"; names-only
    "porphyry":                  {"status": "names-only"},   # Esth 1:6; precious stone; names-only
    "porpoise":                  {"status": "names-only"},   # Exod 25:5 (some translations); tabernacle covering; names-only
    # ISBE compound; 2 Kgs 7:10-11; Neh 2:8; Easton has porter.json
    "port;-porter":              {"status": "redirect-only", "redirect_to": "porter"},
    "portion;-part":             {"status": "names-only"},   # ISBE compound; lexical
    "posidonius":                {"status": "names-only"},   # 2 Macc 14:19; Seleucid envoy; apocryphal
    "possess;-possession":       {"status": "names-only"},   # ISBE compound; lexical
    "possession-demoniacal":     {"status": "names-only"},   # ISBE; demon possession; names-only
    "potentate":                 {"status": "names-only"},   # 1 Tim 6:15 KJV "blessed potentate"; lexical
    # ISBE; Gen 41:45; Easton has potipherah.json
    "poti-phera":                {"status": "redirect-only", "redirect_to": "potipherah"},
    "potsherd-gate":             {"status": "names-only"},   # Jer 19:2; Jerusalem gate; names-only
    # ISBE compound; Jer 18:2-6; Easton has pottery.json
    "potter;-pottery":           {"status": "redirect-only", "redirect_to": "pottery"},
    "poverty":                   {"status": "names-only"},   # Prov 13:18; 2 Cor 8:9; names-only
    "powders":                   {"status": "names-only"},   # Song 3:6; names-only
    "power":                     {"status": "names-only"},   # lexical
    "power-of-keys":             {"status": "names-only"},   # Matt 16:19; "power of the keys"; names-only
    # ISBE; Phil 1:13; Easton has praetorium.json
    "praetorian-guard":          {"status": "redirect-only", "redirect_to": "praetorium"},
    "praise":                    {"status": "names-only"},   # Ps 150; names-only
    "prayer-of-habakkuk":        {"status": "names-only"},   # Hab 3; names-only
    "prayer-of-joseph":          {"status": "names-only"},   # pseudepigraphal; apocryphal; extracanonical
    "prayer-of-manasses":        {"status": "names-only"},   # deuterocanonical/apocryphal; extracanonical
    "prayer-hours-of":           {"status": "names-only"},   # Acts 3:1 "ninth hour of prayer"; names-only
    # ISBE compound; Matt 6:9-13; Easton has lords-prayer.json
    "prayer-lords":              {"status": "redirect-only", "redirect_to": "lords-prayer"},
    "prayers-of-christ":         {"status": "names-only"},   # John 17; ISBE; names-only
    "preacher;-preaching":       {"status": "names-only"},   # ISBE compound; names-only
    "precept":                   {"status": "names-only"},   # Ps 119:4,15; lexical
    "precious":                  {"status": "names-only"},   # lexical
    "precious-stones":           {"status": "names-only"},   # ISBE; Exod 28:17-20; names-only
    "precipitation":             {"status": "names-only"},   # ISBE; rainfall/weather; names-only
    "preeminence":               {"status": "names-only"},   # 3 John 9; Col 1:18; names-only
    "prefer":                    {"status": "names-only"},   # lexical
    "preparation":               {"status": "names-only"},   # Matt 27:62; John 19:14; names-only
    "presbyter;-presbytery":     {"status": "names-only"},   # ISBE compound; 1 Tim 4:14; covered under elder
    "presence":                  {"status": "names-only"},   # Exod 33:14; names-only
    "present":                   {"status": "names-only"},   # lexical
    "presently":                 {"status": "names-only"},   # KJV archaic "immediately"; lexical
    "press":                     {"status": "names-only"},   # Mark 2:4; Luke 8:19; lexical
    "pressfat":                  {"status": "names-only"},   # Hag 2:16 KJV "wine press"; archaic/lexical
    "presume;-presumptuous;-presumptuously": {"status": "names-only"},  # ISBE compound; Num 15:30; lexical
    "prevent":                   {"status": "names-only"},   # KJV archaic "come before"; Ps 119:148; lexical
    "prey":                      {"status": "names-only"},   # Gen 49:9; Isa 53:12; lexical
    "price":                     {"status": "names-only"},   # lexical
    "prick":                     {"status": "names-only"},   # Acts 9:5 "pricks against the goads"; lexical
    "priest-christ-as":          {"status": "names-only"},   # ISBE; Heb 4:14-16; 7:17-27; names-only
    # ISBE compound; Heb 4:14; Easton has priest.json
    "priest-high":               {"status": "redirect-only", "redirect_to": "priest"},
    "priesthood":                {"status": "names-only"},   # 1 Pet 2:5,9; names-only
    "priesthood-in-the-new-testament": {"status": "names-only"},  # ISBE scholarly; names-only
    "priests-and-levites":       {"status": "names-only"},   # ISBE; covered under priest and levite; names-only
    "primogeniture":             {"status": "names-only"},   # ISBE; Gen 25:31-33; right of firstborn; names-only
    "princes-the-seven":         {"status": "names-only"},   # Esth 1:14; names-only
    "princess":                  {"status": "names-only"},   # 1 Kgs 11:3; names-only
    "principal":                 {"status": "names-only"},   # Lev 6:5; Neh 11:17 KJV; lexical
    "principles":                {"status": "names-only"},   # Heb 5:12; 6:1; lexical
    "print;-printing;-printed":  {"status": "names-only"},   # ISBE compound; Job 13:27 KJV; lexical
    # ISBE compound; Acts 18:2; Rom 16:3; Easton has priscilla.json
    "prisca;-priscilla":         {"status": "redirect-only", "redirect_to": "priscilla"},
    "prison-garments":           {"status": "names-only"},   # Jer 52:33 KJV; names-only
    "prison-spirits-in":         {"status": "names-only"},   # 1 Pet 3:19; names-only
    # ISBE compound; Easton has prison.json
    "prison;-prisoner":          {"status": "redirect-only", "redirect_to": "prison"},
    "privy;-privily":            {"status": "names-only"},   # ISBE compound; Ps 11:2; Matt 2:7 KJV; lexical
    "prize":                     {"status": "names-only"},   # 1 Cor 9:24; Phil 3:14 KJV; lexical
    "probation-second":          {"status": "names-only"},   # ISBE scholarly; "second probation" doctrine; names-only
    "profane":                   {"status": "names-only"},   # Ezek 28:16; 1 Tim 1:9; lexical
    "profess;-profession":       {"status": "names-only"},   # ISBE compound; Heb 4:14; lexical
    "prognosticators-monthly":   {"status": "names-only"},   # Isa 47:13 KJV; lexical
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
    print(f'BPG Curation C61: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
