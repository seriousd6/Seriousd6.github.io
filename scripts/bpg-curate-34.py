"""
BPG Curation — Batch C34: chinnereth;-chinneroth → commit (gaps 3299–3398)
Gaps reviewed: 100 (score-5 isbe-scholarly C entries — Christ compounds, lexical, apocryphal)

Notable stubs from ISBE Christ-* compound entries:
Christ as King-Priest-Prophet (threefold office / munus triplex),
Christ Humanity of (incarnation, Heb 2:14-18; 4:15),
Christ Person of (hypostatic union; Chalcedon 451 AD).
Notable redirect: christ-offices-of → christ-as-king-priest-prophet.
3 stub-needed; 1 redirect; 96 names-only.

Script: scripts/bpg-curate-34.py
Run: python3 scripts/bpg-curate-34.py  (from project root)
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
    # ISBE compound; Sea of Galilee (Num 34:11; Josh 11:2); covered under Chinnereth in Easton/Smith
    "chinnereth;-chinneroth": {"status": "names-only"},
    "chirp":                  {"status": "names-only"},   # Isa 8:19 KJV "they chirp and mutter"; lexical
    "chisleu;-chislev":       {"status": "names-only"},   # ISBE compound; 9th Hebrew month (Neh 1:1; Zech 7:1)
    "chitlish":               {"status": "names-only"},   # Josh 15:40; minor Judahite town
    "chiun-1":                {"status": "names-only"},   # Amos 5:26 KJV "Chiun/Kaiwan" = Saturn star-god; brief
    "chiun-2":                {"status": "names-only"},   # ISBE disambiguation variant
    "choba;-chobai":          {"status": "names-only"},   # ISBE compound; place (Judith 4:4; 15:4); apocryphal
    "choenix":                {"status": "names-only"},   # Greek dry measure (Rev 6:6); brief
    "choice":                 {"status": "names-only"},   # lexical
    "choke":                  {"status": "names-only"},   # Matt 13:7,22 "thorns choked it"; lexical
    "chola":                  {"status": "names-only"},   # apocryphal place (Judith 15:4)
    "choler":                 {"status": "names-only"},   # Dan 8:7; 11:11 KJV "moved with choler"; lexical
    "choose;-chosen":         {"status": "names-only"},   # ISBE compound; election; covered under election in Easton
    "chop":                   {"status": "names-only"},   # Mic 3:3 KJV "chop them in pieces"; lexical
    "chorbe":                 {"status": "names-only"},   # apocryphal figure (1 Esd 5:12)
    "chosamaeus":             {"status": "names-only"},   # apocryphal figure
    # The threefold office (munus triplex): Christ as Prophet (Deut 18:15; Heb 1:1-2; John 1:45),
    # Priest (Heb 4:14-5:10; 7:25; "once for all" atonement), and King (Luke 1:33; Rev 19:16;
    # Ps 2:6); Calvin's Institutes II.15 formulated this; illuminates all of Christ's saving work
    "christ-as-king-priest-prophet": {"status": "stub-needed"},
    # Christ's humanity: "born of a woman" (Gal 4:4); "made like his brothers in every way" (Heb 2:17);
    # "tempted in every way, just as we are" (Heb 4:15); "he learned obedience" (Heb 5:8);
    # essential for atonement — only a human could die for humans; counters Docetism
    "christ-humanity-of":     {"status": "stub-needed"},
    "christ-intercession-of": {"status": "names-only"},   # Heb 7:25; Rom 8:34; covered under intercession/priesthood
    "christ-jesus":           {"status": "names-only"},   # title compound; covered under Jesus Christ in Easton
    # ISBE compound covering same content as christ-as-king-priest-prophet; redirect
    "christ-offices-of":      {"status": "redirect-only", "redirect_to": "christ-as-king-priest-prophet"},
    # The Person of Christ: fully God (John 1:1; Col 2:9) and fully man (Heb 2:14);
    # Council of Chalcedon (451 AD) defined "one person in two natures, without confusion,
    # change, division, or separation"; combats Arianism (not fully God) and Docetism (not fully man);
    # hypostatic union; foundation of soteriology
    "christ-person-of":       {"status": "stub-needed"},
    "christ-temptation-of":   {"status": "names-only"},   # Matt 4:1-11; Heb 4:15; covered under temptation
    "christ-the-exaltation-of": {"status": "names-only"}, # Phil 2:9-11; covered under resurrection/ascension
    "christianity":           {"status": "names-only"},   # very broad; covered across many Easton/Smith articles
    "christology":            {"status": "names-only"},   # scholarly discipline; too broad at score-5
    "christs":                {"status": "names-only"},   # Matt 24:24 "false christs"; lexical
    "chronology-of-the-new-testament": {"status": "names-only"},  # ISBE scholarly; too specialized
    "chronology-of-the-old-testament": {"status": "names-only"},  # ISBE scholarly; too specialized
    "chrysoprase;-chrysoprasus": {"status": "names-only"},  # ISBE compound; Rev 21:20 gem; brief
    "church-government":      {"status": "names-only"},   # episcopal/presbyterian/congregational; too specialized
    "churches-robbers-of":    {"status": "names-only"},   # Acts 19:37; lexical
    "churches-seven":         {"status": "names-only"},   # Rev 2-3; covered under Revelation/Ephesus etc.
    "chusi":                  {"status": "names-only"},   # apocryphal figure (Judith 6:15)
    "chuzas":                 {"status": "names-only"},   # Chuza, Herod's steward (Luke 8:3); brief mention
    "cieled;-cieling":        {"status": "names-only"},   # ISBE compound; KJV "paneled" (1 Kgs 6:15); lexical
    "cirama":                 {"status": "names-only"},   # apocryphal place
    "circle":                 {"status": "names-only"},   # Isa 40:22 "circle of the earth"; lexical
    "cisai":                  {"status": "names-only"},   # apocryphal figure
    "cistern;-well;-pool;-aqueduct": {"status": "names-only"},  # ISBE compound; Jer 2:13; lexical
    "citadel":                {"status": "names-only"},   # architectural term; lexical
    "cithern":                {"status": "names-only"},   # KJV musical instrument; lexical
    "cities-of-the-plain;-ciccar": {"status": "names-only"},  # Sodom/Gomorrah; covered in Easton
    "cities-levitical":       {"status": "names-only"},   # Josh 21; covered under Levites
    "cities-store":           {"status": "names-only"},   # 1 Kgs 9:19; storage cities; brief
    "city-of-confusion":      {"status": "names-only"},   # Isa 24:10 KJV; lexical
    "city-of-david":          {"status": "names-only"},   # Jerusalem/Bethlehem; covered under David
    "city-of-destruction":    {"status": "names-only"},   # Isa 19:18 variant; brief
    "city-of-palm-trees":     {"status": "names-only"},   # Jericho (Deut 34:3; Judg 1:16); covered under Jericho
    "city-of-salt":           {"status": "names-only"},   # Josh 15:62; minor place
    "city-of-waters":         {"status": "names-only"},   # 2 Sam 12:27 Rabbah; brief
    "city-golden":            {"status": "names-only"},   # Isa 14:4 KJV; lexical
    "city-royal":             {"status": "names-only"},   # 2 Sam 12:26 KJV; lexical
    "city-rulers-of":         {"status": "names-only"},   # ISBE compound; town officials; lexical
    "clap":                   {"status": "names-only"},   # Ps 47:1; 98:8; Isa 55:12; lexical
    "clasps":                 {"status": "names-only"},   # Exod 26:6,11 tabernacle fittings; cultural
    "claw":                   {"status": "names-only"},   # Deut 14:6; split hoof purity law; brief
    "cleanse":                {"status": "names-only"},   # lexical; Ps 19:12; covered under purification
    "clear;-clearness":       {"status": "names-only"},   # ISBE compound; Exod 24:10; lexical
    "cleave":                 {"status": "names-only"},   # KJV "cling to/split" (Deut 10:20; Gen 2:24); lexical
    "cleft;-cliff;-clift":    {"status": "names-only"},   # ISBE compound; Exod 33:22 "cleft of the rock"; lexical
    "clemency":               {"status": "names-only"},   # Acts 24:4 KJV; lexical
    "cleopatra":              {"status": "names-only"},   # Maccabean-era queen; mainly apocryphal context
    "clerk":                  {"status": "names-only"},   # Acts 19:35 "city clerk"; lexical
    "cliff;-clift":           {"status": "names-only"},   # ISBE compound; variant of cleft; lexical
    "cloak;-cloke":           {"status": "names-only"},   # ISBE compound; Matt 5:40; lexical
    "clod":                   {"status": "names-only"},   # Job 7:5; 21:33; lexical
    "clopas;-cleophas":       {"status": "names-only"},   # ISBE compound; John 19:25; brief
    "close":                  {"status": "names-only"},   # lexical
    "cloth;-clothing":        {"status": "names-only"},   # ISBE compound; covered under dress in Easton
    "clothed-upon":           {"status": "names-only"},   # 2 Cor 5:2,4 KJV; lexical
    "clothes-rending-of":     {"status": "names-only"},   # ISBE compound; grief sign (Gen 37:29); cultural
    "clout":                  {"status": "names-only"},   # Jer 38:11-12 KJV "old rotten rags"; lexical
    "cloven":                 {"status": "names-only"},   # Lev 11:3 "cloven footed"; lexical
    "club":                   {"status": "names-only"},   # Prov 25:18; Job 41:29; weapon; brief
    "cluster":                {"status": "names-only"},   # Num 13:23 grapes; lexical
    "cocker":                 {"status": "names-only"},   # KJV "pamper" (Ecclus 30:9); apocryphal; lexical
    "code-of-hammurabi":      {"status": "names-only"},   # ancient law code; too specialized at score-5
    "cogitation":             {"status": "names-only"},   # Dan 7:28 KJV; lexical
    "cohort":                 {"status": "names-only"},   # Roman military unit (Acts 10:1; 27:1); brief
    "coins":                  {"status": "names-only"},   # covered under individual coin articles in Easton
    "cola":                   {"status": "names-only"},   # apocryphal figure
    "cold":                   {"status": "names-only"},   # Rev 3:16 "neither hot nor cold"; lexical
    "colius":                 {"status": "names-only"},   # apocryphal figure
    "collop":                 {"status": "names-only"},   # Job 15:27 KJV "collops of fat"; lexical
    "color;-colors":          {"status": "names-only"},   # ISBE compound; tabernacle colors; covered elsewhere
    "colt;-foal":             {"status": "names-only"},   # ISBE compound; Zech 9:9; Matt 21:5; brief
    "come":                   {"status": "names-only"},   # lexical
    "comeliness;-comely":     {"status": "names-only"},   # ISBE compound; KJV "beautiful"; lexical
    "comfort":                {"status": "names-only"},   # Isa 40:1; paraclete; covered under Holy Spirit/comfort
    "comfortably":            {"status": "names-only"},   # KJV archaic "tenderly" (Isa 40:2); lexical
    "comfortless":            {"status": "names-only"},   # John 14:18 KJV; lexical
    "coming-second":          {"status": "names-only"},   # Second Coming; covered under Second Coming in Easton
    "commandment-the-new":    {"status": "names-only"},   # John 13:34; covered under love commandment
    "commandment;-commandments": {"status": "names-only"},  # ISBE compound; covered under commandments in Easton
    "commend":                {"status": "names-only"},   # lexical
    "commentaries":           {"status": "names-only"},   # ISBE scholarly; too specialized at score-5
    "commentaries-hebrew":    {"status": "names-only"},   # ISBE scholarly; too specialized
    "commentary":             {"status": "names-only"},   # ISBE scholarly; too specialized
    "commit":                 {"status": "names-only"},   # lexical
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
    print(f'BPG Curation C34: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
