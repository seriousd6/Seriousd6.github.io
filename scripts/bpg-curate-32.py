"""
BPG Curation — Batch C32: brokenfooted → carry (gaps 3099–3198)
Gaps reviewed: 100 (score-5 isbe-scholarly B–C entries — lexical, apocryphal, minor places/names)

Entirely names-only batch. No stub-needed or redirects. At score-5 ISBE, this section covers
KJV archaic terms, minor Beth-* places, apocryphal figures, and cultural/botanical brief items.
Canon of NT/OT entries covered under main "canon" article in Easton/Smith.
0 stub-needed; 0 redirects; 100 names-only.

Script: scripts/bpg-curate-32.py
Run: python3 scripts/bpg-curate-32.py  (from project root)
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
    "brokenfooted":           {"status": "names-only"},   # Lev 21:19; priestly purity law term; brief
    "brokenhanded":           {"status": "names-only"},   # Lev 21:19; same; brief
    "brokenhearted":          {"status": "names-only"},   # Ps 34:18; 51:17; Isa 61:1; poetic; covered elsewhere
    "brooch":                 {"status": "names-only"},   # Exod 35:22; ornamental item; cultural
    "brook-of-egypt-the":     {"status": "names-only"},   # Wadi el-Arish (1 Kgs 8:65; Isa 27:12); minor place
    "broom":                  {"status": "names-only"},   # 1 Kgs 19:4-5 Elijah under broom tree; botanical
    "broth":                  {"status": "names-only"},   # Judg 6:19-20 Gideon's offering; brief
    "brothers-wife":          {"status": "names-only"},   # levirate obligation; covered under levirate marriage
    "brother-in-law":         {"status": "names-only"},   # levirate obligation (Deut 25:5); covered under that
    "brotherhood":            {"status": "names-only"},   # Zech 11:14; 1 Pet 2:17; lexical
    "brotherly":              {"status": "names-only"},   # lexical
    "brotherly-kindness;-brotherly-love": {"status": "names-only"},  # ISBE compound; 2 Pet 1:7; lexical
    "brow":                   {"status": "names-only"},   # lexical; Luke 4:29 "brow of the hill"
    "brown":                  {"status": "names-only"},   # Gen 30:32-43 Laban's flocks; lexical
    "bruise;-bruised":        {"status": "names-only"},   # Gen 3:15; Isa 53:5; meaning covered under those texts
    "brute;-brutish":         {"status": "names-only"},   # KJV "foolish/unreasoning" (Ps 92:6; 2 Pet 2:12); lexical
    "bubastis":               {"status": "names-only"},   # ancient Egyptian city (Ezek 30:17 Pi-beseth); geographic
    "buckle":                 {"status": "names-only"},   # cultural item; brief
    "bud":                    {"status": "names-only"},   # Num 17:8 Aaron's rod; brief botanical
    "buffalo":                {"status": "names-only"},   # Deut 14:5 clean animal; brief
    "buffet":                 {"status": "names-only"},   # Matt 26:67; 1 Cor 4:11; lexical
    "bugean":                 {"status": "names-only"},   # apocryphal title (Esth 12:6 LXX); names-only
    "build;-building":        {"status": "names-only"},   # ISBE compound; Ps 127:1; lexical; covered elsewhere
    "builder":                {"status": "names-only"},   # Ps 118:22 "stone the builders rejected"; lexical
    "bull-wild":              {"status": "names-only"},   # Deut 14:5; Job 39:9-12 KJV; brief
    "bulls-jeroboams":        {"status": "names-only"},   # 1 Kgs 12:28-32; covered under Jeroboam/golden calf
    "bulrushes-ark-of":       {"status": "names-only"},   # Exod 2:3 Moses' basket; covered under Moses
    "bulwark":                {"status": "names-only"},   # Deut 20:20; Ps 48:13; military term; brief
    "bundle":                 {"status": "names-only"},   # 1 Sam 25:29 "bundle of the living"; lexical
    "burglary":               {"status": "names-only"},   # Exod 22:1-4; theft laws; brief
    "burier":                 {"status": "names-only"},   # Jer 14:16; Ezek 39:15; lexical
    "burn;-burning":          {"status": "names-only"},   # ISBE compound; "strange fire" (Num 3:4); lexical
    "burnt-sacrifice":        {"status": "names-only"},   # KJV compound; covered under burnt offering in Easton
    "bush-burning":           {"status": "names-only"},   # Exod 3:2-4; covered under Moses/theophany
    "bushy":                  {"status": "names-only"},   # KJV Song 5:11; lexical/poetic
    "business":               {"status": "names-only"},   # lexical
    "busybody":               {"status": "names-only"},   # 2 Thess 3:11; 1 Tim 5:13; lexical
    "buying":                 {"status": "names-only"},   # lexical; Prov 31:16; brief
    "buz;-buzi;-buzite":      {"status": "names-only"},   # ISBE compound; Elihu's clan (Job 32:2); minor
    "byblus":                 {"status": "names-only"},   # ancient Phoenician Gebal (Ezek 27:9); geographic
    "bypaths":                {"status": "names-only"},   # Judg 5:6; lexical
    "byssus":                 {"status": "names-only"},   # fine linen; Rev 18:12; lexical/cultural
    "byway":                  {"status": "names-only"},   # lexical; Judg 5:6
    "cabin":                  {"status": "names-only"},   # KJV Jer 37:16 "pit/vaulted cell"; lexical
    "caddis":                 {"status": "names-only"},   # apocryphal figure (1 Macc 2:2)
    "cades":                  {"status": "names-only"},   # variant of Kadesh; minor variant
    "cades-barne":            {"status": "names-only"},   # variant of Kadesh-barnea; covered under Kadesh
    "caesars-household":      {"status": "names-only"},   # Phil 4:22; brief NT reference
    "calamity":               {"status": "names-only"},   # lexical; Prov 17:5; 19:13
    "calamolalus":            {"status": "names-only"},   # apocryphal figure
    "calcol;-chalkol":        {"status": "names-only"},   # ISBE compound; 1 Kgs 4:31; 1 Chr 2:6; minor figure
    "caleb-ephrathah":        {"status": "names-only"},   # 1 Chr 2:24; minor place
    "calendar":               {"status": "names-only"},   # Jewish calendar system; covered under feasts/months
    "calf-image":             {"status": "names-only"},   # ISBE compound; covered under golden calf in Easton
    "calf-golden":            {"status": "names-only"},   # covered under golden calf / Exod 32 in Easton/Smith
    "calitas":                {"status": "names-only"},   # apocryphal figure (1 Esd 9:23)
    "calker":                 {"status": "names-only"},   # Ezek 27:9,27; ship caulker; brief cultural
    "callisthenes":           {"status": "names-only"},   # apocryphal figure (2 Macc 8:33)
    "calneh;-calno":          {"status": "names-only"},   # ISBE compound; Amos 6:2; Isa 10:9; minor places
    "calphi":                 {"status": "names-only"},   # apocryphal figure (1 Macc 11:70)
    "calves-of-the-lips":     {"status": "names-only"},   # Hos 14:2 "offerings of our lips"; lexical/poetic
    "cambyses":               {"status": "names-only"},   # Persian king; extrabiblical (Ezra period context)
    "camels-hair":            {"status": "names-only"},   # Matt 3:4; John the Baptist's clothing; brief
    "cana-of-galilee":        {"status": "names-only"},   # John 2:1,11; covered under Cana in Easton/Smith
    "canaan;-canaanites":     {"status": "names-only"},   # ISBE compound; covered under Canaan in Easton/Smith
    "canaanitess":            {"status": "names-only"},   # feminine demonym; brief epithet
    "canals":                 {"status": "names-only"},   # Exod 7:19; Nile irrigation; brief
    "cananaean;-canaanite":   {"status": "names-only"},   # ISBE compound; Simon the Zealot (Matt 10:4); brief
    "candle;-candlestick":    {"status": "names-only"},   # ISBE compound; covered under candlestick in Easton
    "candlestick-the-golden": {"status": "names-only"},   # ISBE compound; menorah; covered under candlestick
    "cankered":               {"status": "names-only"},   # KJV "corroded/rusted" (Jas 5:3); lexical
    "canon-of-the-new-testament": {"status": "names-only"},  # covered under canon in Easton/Smith
    "canon-of-the-old-testament": {"status": "names-only"},  # covered under canon in Easton/Smith
    "caperberry":             {"status": "names-only"},   # Eccles 12:5 LXX; botanical; brief
    "caph":                   {"status": "names-only"},   # Hebrew letter (11th); lexical
    "capharsalama":           {"status": "names-only"},   # 1 Macc 7:31; apocryphal place
    "caphenatha":             {"status": "names-only"},   # 1 Macc 12:37; apocryphal place
    "caphira":                {"status": "names-only"},   # apocryphal place
    "caphthorim":             {"status": "names-only"},   # Gen 10:14; 1 Chr 1:12; Philistine ancestry
    "captivity-epistles":     {"status": "names-only"},   # Eph/Phil/Col/Philemon covered individually
    "car":                    {"status": "names-only"},   # minor/lexical; brief
    "carabasion":             {"status": "names-only"},   # apocryphal figure
    "caravan":                {"status": "names-only"},   # Gen 37:25; cultural practice; brief
    "caravansary":            {"status": "names-only"},   # ancient inn; cultural; brief
    "carcass;-carcase":       {"status": "names-only"},   # ISBE compound; Lev 11 unclean animals; lexical
    "care;-carefulness;-careful": {"status": "names-only"},  # ISBE compound; 1 Pet 5:7; lexical
    "careful;-carefulness":   {"status": "names-only"},   # duplicate ISBE compound; lexical
    "carefully":              {"status": "names-only"},   # lexical
    "careless;-carelessly":   {"status": "names-only"},   # ISBE compound; Isa 32:9-11; lexical
    "carem":                  {"status": "names-only"},   # apocryphal place (1 Esd 5:25)
    "carites":                {"status": "names-only"},   # 2 Kgs 11:4,19; Carian mercenary guards; brief
    "carmanians":             {"status": "names-only"},   # people from Carmania (Judith 2:25); apocryphal
    "carme":                  {"status": "names-only"},   # apocryphal figure
    "carmelite":              {"status": "names-only"},   # demonym for Carmel; Nabal/Abigail epithet
    "carmelitess":            {"status": "names-only"},   # feminine demonym; Abigail (1 Chr 3:1)
    "carmonians":             {"status": "names-only"},   # variant of carmanians; apocryphal
    "carnaim":                {"status": "names-only"},   # 1 Macc 5:26,43-44; apocryphal place
    "carnion":                {"status": "names-only"},   # 1 Macc 5:44; apocryphal place
    "carousings":             {"status": "names-only"},   # 1 Pet 4:3; Gal 5:21; lexical; covered under drunkenness
    "carry":                  {"status": "names-only"},   # lexical
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
    print(f'BPG Curation C32: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
