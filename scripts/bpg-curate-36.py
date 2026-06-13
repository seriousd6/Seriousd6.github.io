"""
BPG Curation — Batch C36: counter-charm → dagger (gaps 3499–3598)
Gaps reviewed: 100 (score-5 isbe-scholarly C–D entries — covenant compounds, lexical, apocryphal)

Entirely names-only batch. Covenant-in-NT/OT compounds covered under main Easton covenant article.
Court-of-Gentiles covered under temple articles. Creator covered under creation/God.
0 stub-needed; 0 redirects; 100 names-only.

Script: scripts/bpg-curate-36.py
Run: python3 scripts/bpg-curate-36.py  (from project root)
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
    "counter-charm":          {"status": "names-only"},   # Jer 8:17 enchantment context; lexical
    "counterfeit":            {"status": "names-only"},   # general concept; lexical
    "countervail":            {"status": "names-only"},   # KJV Esth 7:4 "compensate"; lexical
    "country":                {"status": "names-only"},   # lexical
    "countryman":             {"status": "names-only"},   # lexical
    "couple":                 {"status": "names-only"},   # lexical
    "coupling":               {"status": "names-only"},   # Exod 26:4-5 tabernacle loops; architectural
    "courage":                {"status": "names-only"},   # Josh 1:6-9; covered under strength/virtue topics
    "course":                 {"status": "names-only"},   # lexical
    "course-of-priests-and-levites": {"status": "names-only"},  # 1 Chr 24; Luke 1:5; covered under Levites/priests
    "court-of-the-gentiles":  {"status": "names-only"},   # outer Temple court; covered under Temple/Herod's Temple
    "court-of-the-sabbath":   {"status": "names-only"},   # 2 Kgs 16:18 KJV; architectural; brief
    "court-of-the-sanctuary;-tabernacle;-temple": {"status": "names-only"},  # ISBE compound; covered under tabernacle/temple
    "courts-judicial":        {"status": "names-only"},   # Jewish court system; covered under Sanhedrin
    "cousin":                 {"status": "names-only"},   # Luke 1:36 Elizabeth/Mary; lexical
    "coutha":                 {"status": "names-only"},   # apocryphal place
    "covenant-of-salt":       {"status": "names-only"},   # Num 18:19; 2 Chr 13:5; brief
    "covenant-ark-of-the":    {"status": "names-only"},   # covered under ark of the covenant in Easton/Smith
    "covenant-book-of-the":   {"status": "names-only"},   # Exod 24:7; covenant scroll; brief
    "covenant-in-the-new-testament": {"status": "names-only"},  # Jer 31:31; Heb 8; covered under covenant in Easton
    "covenant-in-the-old-testament": {"status": "names-only"},  # Abrahamic/Mosaic/Davidic; covered under covenant
    "covenant-the-new":       {"status": "names-only"},   # ISBE compound; same as above; names-only
    "cover;-covering":        {"status": "names-only"},   # ISBE compound; Ps 32:1 "covering of sins"; lexical
    "covered-way":            {"status": "names-only"},   # 2 Kgs 16:18; architectural; brief
    "covering-for-the-head":  {"status": "names-only"},   # 1 Cor 11:4-16; covered under head covering topic
    "covert":                 {"status": "names-only"},   # KJV "shelter/thicket" (1 Sam 25:20; Ps 61:4); lexical
    "covet":                  {"status": "names-only"},   # 10th commandment; covered under covetousness in Easton
    "cow;-kine":              {"status": "names-only"},   # ISBE compound; Gen 41:2-4 Pharaoh's dream; brief
    "cozeba":                 {"status": "names-only"},   # 1 Chr 4:22; minor place
    "cracknel":               {"status": "names-only"},   # 1 Kgs 14:3 KJV hard biscuit; lexical
    "craft;-craftiness;-crafty": {"status": "names-only"},  # ISBE compound; 2 Cor 4:2; Eph 4:14; lexical
    "crafts":                 {"status": "names-only"},   # Acts 19:25; covered under trade/occupations
    "crag":                   {"status": "names-only"},   # Job 39:28; 1 Sam 14:4; geological; brief
    "crashing":               {"status": "names-only"},   # Zeph 1:10 KJV; lexical
    "crates":                 {"status": "names-only"},   # apocryphal figure (2 Macc 4:29)
    "creator":                {"status": "names-only"},   # God as Creator; covered under creation/God in Easton
    "creature-living":        {"status": "names-only"},   # Ezek 1:5; Rev 4:6-8; covered under cherubim/seraphim
    "credit":                 {"status": "names-only"},   # lexical
    "creed;-creeds":          {"status": "names-only"},   # ISBE compound; covered under individual creed articles
    "creek":                  {"status": "names-only"},   # Acts 27:39; lexical
    "creeping-thing":         {"status": "names-only"},   # Gen 1:24-25; Lev 11; brief
    "cremation":              {"status": "names-only"},   # burial practice; brief
    "crescents":              {"status": "names-only"},   # Isa 3:18; Judg 8:21 ornaments; cultural
    "crib":                   {"status": "names-only"},   # Isa 1:3; Prov 14:4; lexical
    "cricket":                {"status": "names-only"},   # Lev 11:22 clean insect; brief
    "crier":                  {"status": "names-only"},   # Dan 3:4 "herald"; lexical
    "crime;-crimes":          {"status": "names-only"},   # ISBE compound; lexical
    "cripple":                {"status": "names-only"},   # Acts 14:8; covered under healing miracles
    "criticism":              {"status": "names-only"},   # ISBE scholarly; biblical criticism; too specialized
    "criticism-and-archaeology": {"status": "names-only"},  # ISBE scholarly; too specialized
    "criticism-of-the-bible": {"status": "names-only"},   # ISBE scholarly; too specialized
    "crocodile":              {"status": "names-only"},   # possible Leviathan meaning (Job 41); brief
    "crocodile-land":         {"status": "names-only"},   # Ezek 29:3 KJV geographic note; brief
    "crook-backed":           {"status": "names-only"},   # Lev 21:20 KJV "hunchback"; priestly law; lexical
    "crooked":                {"status": "names-only"},   # Isa 40:4; Phil 2:15; lexical
    "crooked-serpent":        {"status": "names-only"},   # Job 26:13; Isa 27:1; lexical/poetic
    "crop":                   {"status": "names-only"},   # Lev 1:16 bird crop; brief
    "crossway":               {"status": "names-only"},   # Obad 14; lexical
    "cruel;-cruelty":         {"status": "names-only"},   # ISBE compound; Prov 12:10; Eph 4:31; lexical
    "crumb":                  {"status": "names-only"},   # Matt 15:27; Luke 16:21; lexical
    "cry-crying":             {"status": "names-only"},   # ISBE compound; lexical
    "cub":                    {"status": "names-only"},   # Ezek 30:5 KJV; geographic variant; brief
    "cuckow;-cuckoo":         {"status": "names-only"},   # Lev 11:16 KJV unclean bird; brief
    "cucumber":               {"status": "names-only"},   # Num 11:5; Isa 1:8; botanical
    "cud":                    {"status": "names-only"},   # Lev 11:3-7; clean animal purity law; brief
    "culture":                {"status": "names-only"},   # general concept; too broad
    "cumber;-cumbered":       {"status": "names-only"},   # KJV "encumber" (Luke 10:40; 13:7); lexical
    "cumi":                   {"status": "names-only"},   # Mark 5:41 Aramaic "talitha cumi"; lexical
    "cun":                    {"status": "names-only"},   # 1 Chr 18:8; minor place in Syria
    "cunning":                {"status": "names-only"},   # KJV "skillful/crafty" (Exod 31:4); lexical
    "cupboard":               {"status": "names-only"},   # cultural; brief
    "curdle":                 {"status": "names-only"},   # Job 10:10; lexical/poetic
    "cure;-cures":            {"status": "names-only"},   # ISBE compound; covered under healing/miracles
    "curious":                {"status": "names-only"},   # KJV "skillfully made" (Exod 28:8); lexical
    "current-money":          {"status": "names-only"},   # Gen 23:16; lexical
    "cush-1":                 {"status": "names-only"},   # ISBE disambiguation; son of Ham (Gen 10:6)/Ethiopia
    "cush-2":                 {"status": "names-only"},   # ISBE disambiguation; variant
    "cushan-rishathaim":      {"status": "names-only"},   # Judg 3:8; Mesopotamian oppressor; names-only
    "cushion":                {"status": "names-only"},   # Mark 4:38; brief
    "cushite-woman;-ethiopian-woman": {"status": "names-only"},  # ISBE compound; Num 12:1; brief
    "custody":                {"status": "names-only"},   # Acts 21:34; lexical
    "custom-1":               {"status": "names-only"},   # ISBE disambiguation; taxes/toll (Matt 9:9); lexical
    "custom-2":               {"status": "names-only"},   # ISBE disambiguation; tradition/practice; lexical
    "cut;-cutting":           {"status": "names-only"},   # ISBE compound; "cut off" divine judgment; lexical
    "cuth;-cuthah":           {"status": "names-only"},   # ISBE compound; 2 Kgs 17:24,30; Samaritan settlers
    "cutha":                  {"status": "names-only"},   # variant of cuth; names-only
    "cuthean;-cuthite":       {"status": "names-only"},   # ISBE compound; Samaritan demonym; brief
    "cutting-asunder":        {"status": "names-only"},   # Dan 2:5 KJV punishment; lexical
    "cutting-off":            {"status": "names-only"},   # Lev 7:20-21 "cut off from his people"; lexical
    "cyamon":                 {"status": "names-only"},   # apocryphal place (Judith 7:3)
    "cymbal":                 {"status": "names-only"},   # Ps 150:5; 1 Cor 13:1; covered under instruments
    "cyprians":               {"status": "names-only"},   # inhabitants of Cyprus; demonym
    "cyrama":                 {"status": "names-only"},   # apocryphal place
    "cyrenian;-cyrenians":    {"status": "names-only"},   # ISBE compound; Simon of Cyrene; covered under that
    "cyria":                  {"status": "names-only"},   # 2 John 1 "chosen lady"; brief
    "dabbesheth":             {"status": "names-only"},   # Josh 19:11; minor place
    "dabria":                 {"status": "names-only"},   # apocryphal figure (2 Esd 14:24)
    "dacubi;-dacobi":         {"status": "names-only"},   # ISBE compound; apocryphal figure
    "daddeus":                {"status": "names-only"},   # apocryphal figure
    "dagger":                 {"status": "names-only"},   # Judg 3:16 Ehud's dagger; cultural/brief
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
    print(f'BPG Curation C36: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
