"""
BPG Curation — Batch C39: doorpost → eleutherus (gaps 3799–3898)
Gaps reviewed: 100 (all score-5 isbe-scholarly entries, D–E range)

Word studies: doorpost, dote, double, doubt, drop-dropping, drove, drowning,
drum, drunkenness, due, dure, duty, dye/dyeing, dysentery, eanes, early,
earring, earthen-vessels, earthly, ease, edge, edification, eduth, effect,
either, el-elyon, el-roi, el-shaddai, ela, elect, election, electrum, element.

Apocryphal: dorymenes, dotaea, dragon-bel-and-the, drama-mimic, ebionites-gospel,
ecanus, ecce-homo, eddias, eddinus, edos, egyptian-the, egyptians-gospel,
ekrebel, elasa, elberith, elcia, eldad-and-modad-book-of, eleasa, eleazurus,
elephantine, eleutherus.

Scholarly ISBE: dualism, drachma, ecclesiastes-the-preacher, ebionism/ebionites,
egyptian-kings-later, egyptian-versions.

Redirects: dor;-dora → dor; drachma;-dram → dram; dung;-dung-gate → dung;
ebal;-obal → ebal; eden-children-of → eden; eden-house-of → eden;
eder-1 → eder; eder-2 → eder; edom;-edomites → edom;
eglon-1 → eglon; eglon-2 → eglon; egypt-brook-river-stream-of → egypt;
ekron;-ekronite → ekron; elah-1 → elah; elah-2 → elah;
elah-vale-of → elah; elam;-elamites → elam;
elder-in-the-new-testament → elder; elder-in-the-old-testament → elder.

Script: scripts/bpg-curate-39.py
Run: python3 scripts/bpg-curate-39.py  (from project root)
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
    "doorpost":                             {"status": "names-only"},   # ISBE; Exod 12:7 mezuzah/blood; word study
    # ISBE combined; Easton has dor.json (Josh 11:2; 1 Kgs 4:11 coastal city)
    "dor;-dora":                            {"status": "redirect-only", "redirect_to": "dor"},
    "dorymenes":                            {"status": "names-only"},   # ISBE; 2 Macc 4:45 Seleucid figure; apocryphal
    "dotaea":                               {"status": "names-only"},   # ISBE; Jdt 3:9 variant of Dothan; apocryphal
    "dote":                                 {"status": "names-only"},   # ISBE word study (1 Tim 6:4)
    "double":                               {"status": "names-only"},   # ISBE word study; general
    "doubt":                                {"status": "names-only"},   # ISBE word study (Matt 14:31; Rom 14:23)
    "doxology":                             {"status": "names-only"},   # ISBE; liturgical praise formula; score-5 → names-only
    # ISBE combined; Ezra 2:69; Neh 7:70-72 coin; Easton has dram.json
    "drachma;-dram":                        {"status": "redirect-only", "redirect_to": "dram"},
    "dragon-bel-and-the":                   {"status": "names-only"},   # ISBE; apocryphal addition to Daniel
    "dragon-red":                           {"status": "names-only"},   # ISBE; Rev 12:3 scarlet dragon; word study
    "drama-mimic":                          {"status": "names-only"},   # ISBE; theatrical performance; extrabiblical
    "draught":                              {"status": "names-only"},   # ISBE word study (Matt 15:17 KJV "draught/toilet")
    "dream;-dreamer":                       {"status": "names-only"},   # ISBE combined; Gen 37:5-11; Dan 2; word study
    "drink-offering":                       {"status": "names-only"},   # ISBE; Num 28:7-10 libation; general
    "drop-dropping":                        {"status": "names-only"},   # ISBE combined word study (Prov 19:13)
    "drove":                                {"status": "names-only"},   # ISBE word study (Gen 32:16 "droves")
    "drowning":                             {"status": "names-only"},   # ISBE word study (Matt 18:6)
    "drum":                                 {"status": "names-only"},   # ISBE; timbrel/tabret percussion; general
    "drunkenness":                          {"status": "names-only"},   # ISBE word study; Eph 5:18; general
    "dualism":                              {"status": "names-only"},   # ISBE scholarly; good vs. evil cosmology; score-5
    "due":                                  {"status": "names-only"},   # ISBE word study
    # ISBE combined; Neh 2:13 Jerusalem gate; Easton has dung.json (Neh 2:13)
    "dung;-dung-gate":                      {"status": "redirect-only", "redirect_to": "dung"},
    "dure":                                 {"status": "names-only"},   # ISBE; KJV "endure" (Matt 13:21); word study
    "duty":                                 {"status": "names-only"},   # ISBE word study
    "dye;-dyeing":                          {"status": "names-only"},   # ISBE combined; Ezek 23:15 dyed garments; general
    "dysentery":                            {"status": "names-only"},   # ISBE; Acts 28:8 disease; general
    "eanes":                                {"status": "names-only"},   # ISBE; 1 Esd 9:21 variant; apocryphal
    "early":                                {"status": "names-only"},   # ISBE word study
    "earring":                              {"status": "names-only"},   # ISBE; Exod 32:2-3; Gen 35:4 jewelry; general
    "earth-circle-of-the":                  {"status": "names-only"},   # ISBE; Isa 40:22 cosmological; word study
    "earth-corners-of-the":                 {"status": "names-only"},   # ISBE; Isa 11:12; Rev 7:1 cosmological; word study
    "earth-ends-of-the":                    {"status": "names-only"},   # ISBE; Ps 2:8; Isa 45:22 cosmological; word study
    "earth-pillars-of-the":                 {"status": "names-only"},   # ISBE; 1 Sam 2:8 cosmological; word study
    "earth-the-new":                        {"status": "names-only"},   # ISBE; Rev 21:1; Isa 65:17 eschatological; word study
    "earth-vault-of-the":                   {"status": "names-only"},   # ISBE; Amos 9:6 cosmological; word study
    "earthen-vessels":                      {"status": "names-only"},   # ISBE; 2 Cor 4:7; Jer 18-19; word study
    "earthly":                              {"status": "names-only"},   # ISBE word study (John 3:12; Phil 3:19)
    "ease":                                 {"status": "names-only"},   # ISBE word study
    "east-eastern-sea":                     {"status": "names-only"},   # ISBE; Dead Sea (Joel 2:20; Ezek 47:18); word study
    "east-country":                         {"status": "names-only"},   # ISBE; Gen 25:6; Zech 8:7 geographic; word study
    # ISBE combined; Easton has ebal.json (Josh 8:30-33; Deut 27-28)
    "ebal;-obal":                           {"status": "redirect-only", "redirect_to": "ebal"},
    "eben-bohan":                           {"status": "names-only"},   # ISBE; Josh 15:6 boundary stone; minor place
    "eben-ezel":                            {"status": "names-only"},   # ISBE; 1 Sam 20:19 KJV "stone Ezel"; minor place
    "ebez":                                 {"status": "names-only"},   # ISBE; Josh 19:20 Issachar town; minor place
    "ebionism;-ebionites":                  {"status": "names-only"},   # ISBE combined; Jewish-Christian sect; score-5
    "ebionites-gospel-of-the":              {"status": "names-only"},   # ISBE; apocryphal gospel; extracanonical
    "ebron":                                {"status": "names-only"},   # ISBE; Josh 19:28 Asher town; minor place
    "ecanus":                               {"status": "names-only"},   # ISBE; 2 Esd 14:24 scribe; apocryphal
    "ecce-homo":                            {"status": "names-only"},   # ISBE; John 19:5 "Behold the man"; word study
    "ecclesiastes-the-preacher":            {"status": "names-only"},   # ISBE; book intro; covered under Ecclesiastes canon
    "eddias":                               {"status": "names-only"},   # ISBE; 1 Esd 9:26 variant; apocryphal
    "eddinus":                              {"status": "names-only"},   # ISBE; 1 Esd 9:35 variant; apocryphal
    # ISBE; 2 Kgs 19:12; Isa 37:12 Assyrian-conquered Eden; Easton has eden.json (Gen 2:8-15)
    "eden-children-of":                     {"status": "redirect-only", "redirect_to": "eden"},
    # ISBE; Amos 1:5 "house/Beth-Eden" in Aram; Easton has eden.json
    "eden-house-of":                        {"status": "redirect-only", "redirect_to": "eden"},
    # ISBE disambiguation; Josh 15:21 Judah town; Easton has eder.json
    "eder-1":                               {"status": "redirect-only", "redirect_to": "eder"},
    # ISBE disambiguation; 1 Chr 23:23 Levite; Easton has eder.json
    "eder-2":                               {"status": "redirect-only", "redirect_to": "eder"},
    "edes":                                 {"status": "names-only"},   # ISBE; 1 Esd 9:35 variant; apocryphal
    "edge":                                 {"status": "names-only"},   # ISBE word study
    "edification;-edify":                   {"status": "names-only"},   # ISBE combined; 1 Cor 14:12; Rom 14:19; word study
    "edna":                                 {"status": "names-only"},   # ISBE; Tobit 7:2 Raguel's wife; apocryphal
    # ISBE combined; Easton has edom.json (Gen 25:30; 36:1 Esau's land)
    "edom;-edomites":                       {"status": "redirect-only", "redirect_to": "edom"},
    "edos":                                 {"status": "names-only"},   # ISBE; 1 Esd 9:35 variant; apocryphal
    "eduth":                                {"status": "names-only"},   # ISBE; Ps 60 title "testimony"; word study
    "effect;-effectual":                    {"status": "names-only"},   # ISBE combined word study (1 Cor 16:9; Jas 5:16)
    "eglath-shelishiyah":                   {"status": "names-only"},   # ISBE; Isa 15:5; Jer 48:34 Moabite place
    # ISBE disambiguation; Moabite king (Judg 3:12-30); Easton has eglon.json
    "eglon-1":                              {"status": "redirect-only", "redirect_to": "eglon"},
    # ISBE disambiguation; Canaanite city (Josh 10:3); Easton has eglon.json
    "eglon-2":                              {"status": "redirect-only", "redirect_to": "eglon"},
    # ISBE; Wadi el-Arish (Num 34:5; 1 Kgs 8:65); Easton has egypt.json
    "egypt-brook-river-stream-of":          {"status": "redirect-only", "redirect_to": "egypt"},
    "egyptian-kings-later":                 {"status": "names-only"},   # ISBE scholarly; Ptolemaic/late dynasty; score-5
    "egyptian-versions":                    {"status": "names-only"},   # ISBE; Bible translations; scholarly
    "egyptian-the":                         {"status": "names-only"},   # ISBE; Acts 21:38 false prophet; word study
    "egyptians-gospel-according-to-the":    {"status": "names-only"},   # ISBE; apocryphal gospel; extracanonical
    "either":                               {"status": "names-only"},   # ISBE word study
    "ekrebel":                              {"status": "names-only"},   # ISBE; Jdt 7:18 place; apocryphal
    # ISBE combined; Easton has ekron.json (Josh 13:3; 1 Sam 5:10 Philistine city)
    "ekron;-ekronite":                      {"status": "redirect-only", "redirect_to": "ekron"},
    "el":                                   {"status": "names-only"},   # ISBE; Hebrew generic name for God; word study
    "el-elyon":                             {"status": "names-only"},   # ISBE; Gen 14:18-20 "God Most High"; word study
    "el-roi":                               {"status": "names-only"},   # ISBE; Gen 16:13 "God who sees"; word study
    "el-shaddai":                           {"status": "names-only"},   # ISBE; Gen 17:1 "God Almighty"; word study
    "ela":                                  {"status": "names-only"},   # ISBE; 1 Kgs 4:18 Solomon's officer's father; minor
    # ISBE disambiguation; 1 Kgs 16:8-14 king of Israel; Easton has elah.json
    "elah-1":                               {"status": "redirect-only", "redirect_to": "elah"},
    # ISBE disambiguation; Valley of Elah (1 Sam 17:2); Easton has elah.json
    "elah-2":                               {"status": "redirect-only", "redirect_to": "elah"},
    # ISBE; Valley of Elah where David fought Goliath; Easton has elah.json
    "elah-vale-of":                         {"status": "redirect-only", "redirect_to": "elah"},
    # ISBE combined; Easton has elam.json (Gen 10:22; Isa 21:2 ancient nation)
    "elam;-elamites":                       {"status": "redirect-only", "redirect_to": "elam"},
    "elasa":                                {"status": "names-only"},   # ISBE; 1 Macc 9:5 battle site; apocryphal
    "elberith":                             {"status": "names-only"},   # ISBE; Judg 9:46 "god of the covenant" temple; minor
    "elcia":                                {"status": "names-only"},   # ISBE; Jdt 8:1 ancestor; apocryphal
    "eldad-and-modad-book-of":              {"status": "names-only"},   # ISBE; apocryphal pseudepigrapha; extracanonical
    # ISBE scholarly; NT elder (1 Tim 3:1-7; Tit 1:5-9); Easton has elder.json
    "elder-in-the-new-testament":           {"status": "redirect-only", "redirect_to": "elder"},
    # ISBE scholarly; OT elder (Exod 3:16; Num 11:16-25); Easton has elder.json
    "elder-in-the-old-testament":           {"status": "redirect-only", "redirect_to": "elder"},
    "eleadah;-eladah":                      {"status": "names-only"},   # ISBE combined; 1 Chr 7:20 Ephraimite; minor
    "eleasa":                               {"status": "names-only"},   # ISBE; 1 Macc 2:5 Maccabean figure; apocryphal
    "eleazurus":                            {"status": "names-only"},   # ISBE; 1 Esd variant; apocryphal
    "elect":                                {"status": "names-only"},   # ISBE word study (Matt 24:22; Rom 8:33)
    "election":                             {"status": "names-only"},   # ISBE; Eph 1:4-5; Rom 9:11; word study/concept
    "electrum":                             {"status": "names-only"},   # ISBE; Ezek 1:4 KJV "amber"; metal alloy; word study
    "element;-elements":                    {"status": "names-only"},   # ISBE combined; Gal 4:3,9; Col 2:8,20; word study
    "elephantine":                          {"status": "names-only"},   # ISBE; Yeb/Jewish colony in Egypt; archaeological
    "eleutherus":                           {"status": "names-only"},   # ISBE; 1 Macc 11:7 river in Lebanon; apocryphal
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
    print(f'BPG Curation C39: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
