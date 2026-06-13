"""
BPG Curation — Batch C33: casdim → chimney (gaps 3199–3298)
Gaps reviewed: 100 (all score-5 isbe-scholarly entries, C range)

Heavy on apocryphal figures (cathua, ceilan, cendebaeus, ceras, cetab, chabris,
chadias-they-of, chaereas, chalphi, chanuneus, chaphenatha, charaathalan, characa,
charax, charchus, charea, charme, charmis, chaseba, chelcias, chellians, chellus,
chelod, cheluhi, childhood-gospels-of-the → all names-only) and ISBE word studies
(case, cast, cause, cease, change, chant, charge, charm, cheer, cherish, chief).

Redirects: cenchreae → cenchrea; chaldea;-chaldeans → chaldea;
chanaan;-chanaanite → canaan; chavah → eve;
cherubim-1 → cherub; cherubim-2 → cherub; chettiim → chittim.

Script: scripts/bpg-curate-33.py
Run: python3 scripts/bpg-curate-33.py  (from project root)
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
    "casdim":                               {"status": "names-only"},   # ISBE; Chaldean people variant (Gen 22:22)
    "case":                                 {"status": "names-only"},   # ISBE word study
    "casphon":                              {"status": "names-only"},   # ISBE; 1 Macc 5:26 Maccabean battle site
    "casphor":                              {"status": "names-only"},   # ISBE; 1 Macc 5:36 variant; apocryphal
    "caspin;-caspis":                       {"status": "names-only"},   # ISBE combined; 2 Macc 12:13; apocryphal
    "cast":                                 {"status": "names-only"},   # ISBE word study
    "castanets":                            {"status": "names-only"},   # ISBE; musical percussion; general
    "cat":                                  {"status": "names-only"},   # ISBE; Bar 6:21 (Letter of Jeremiah); apocryphal
    "catechist;-catechumen":                {"status": "names-only"},   # ISBE combined; early church instruction; general
    "cathua":                               {"status": "names-only"},   # ISBE; 1 Esd 5:30 variant; apocryphal
    "cause":                                {"status": "names-only"},   # ISBE word study
    "causeway;-causey":                     {"status": "names-only"},   # ISBE combined; 1 Chr 26:16,18 KJV; word study
    "cease":                                {"status": "names-only"},   # ISBE word study
    "ceilan":                               {"status": "names-only"},   # ISBE; 1 Esd 5:15 variant; apocryphal
    "ceiled;-ceiling":                      {"status": "names-only"},   # ISBE combined word study; temple paneling
    "celebrate":                            {"status": "names-only"},   # ISBE word study
    "celestial":                            {"status": "names-only"},   # ISBE word study (1 Cor 15:40)
    # ISBE; Macedonian seaport (Acts 18:18); Easton has cenchrea.json
    "cenchreae":                            {"status": "redirect-only", "redirect_to": "cenchrea"},
    "cendebaeus":                           {"status": "names-only"},   # ISBE; Seleucid general (1 Macc 15:38); apocryphal
    "ceras":                                {"status": "names-only"},   # ISBE; 1 Esd variant; apocryphal
    "certain;-certainly;-certainty":        {"status": "names-only"},   # ISBE combined word study
    "certify":                              {"status": "names-only"},   # ISBE word study (Gal 1:11 KJV)
    "cetab":                                {"status": "names-only"},   # ISBE; 1 Esd variant; apocryphal
    "chabris":                              {"status": "names-only"},   # ISBE; Jdt 6:15 figure; apocryphal
    "chadias-they-of;-chadiasai":           {"status": "names-only"},   # ISBE combined; 1 Esd 5:20 variant; apocryphal
    "chaereas":                             {"status": "names-only"},   # ISBE; 2 Macc 10:32 figure; apocryphal
    "chafe":                                {"status": "names-only"},   # ISBE word study (2 Sam 17:8)
    "chain;-chains":                        {"status": "names-only"},   # ISBE combined word study; general
    "chair":                                {"status": "names-only"},   # ISBE word study; general
    # ISBE combined variant; Easton has chaldea.json (Babylonian region; Dan 1:4)
    "chaldea;-chaldeans":                   {"status": "redirect-only", "redirect_to": "chaldea"},
    "chalkstone":                           {"status": "names-only"},   # ISBE; Isa 27:9 "chalk stones"; word study
    "challenge":                            {"status": "names-only"},   # ISBE word study
    "chalphi":                              {"status": "names-only"},   # ISBE; 1 Macc 11:70 Maccabean figure; apocryphal
    "chamber-roof":                         {"status": "names-only"},   # ISBE; Judg 3:20-24 roof chamber; word study
    "chambers-in-the-heavens":             {"status": "names-only"},   # ISBE; Job 9:9 constellation chambers; word study
    "chambers-in-the-south":               {"status": "names-only"},   # ISBE; Job 9:9 southern stars; word study
    "chambers-of-imagery":                  {"status": "names-only"},   # ISBE; Ezek 8:12 idolatry rooms; word study
    "champaign":                            {"status": "names-only"},   # ISBE; KJV "plains/steppe" (Deut 11:30); word study
    # ISBE combined variant; Easton has canaan.json (promised land; Gen 12:5)
    "chanaan;-chanaanite":                  {"status": "redirect-only", "redirect_to": "canaan"},
    "change":                               {"status": "names-only"},   # ISBE word study
    "change-of-raiment":                    {"status": "names-only"},   # ISBE; gift of clothing (Gen 45:22; Judg 14:12)
    "changer":                              {"status": "names-only"},   # ISBE; money-changer (John 2:14-15); word study
    "chanoch;-hanochites":                  {"status": "names-only"},   # ISBE combined; Reuben's son Hanoch + clan (Num 26:5)
    "chant":                                {"status": "names-only"},   # ISBE word study (Amos 6:5)
    "chanuneus":                            {"status": "names-only"},   # ISBE; 1 Esd 9:29 variant; apocryphal
    "chaphenatha":                          {"status": "names-only"},   # ISBE; 1 Macc 12:37 Jerusalem district; apocryphal
    "chapt":                                {"status": "names-only"},   # ISBE; KJV "cracked/parched" (Jer 14:4); word study
    "charaathalan":                         {"status": "names-only"},   # ISBE; 1 Esd 5:36 variant; apocryphal
    "characa":                              {"status": "names-only"},   # ISBE; 2 Macc 12:17 place; apocryphal
    "charax;-characa":                      {"status": "names-only"},   # ISBE combined; apocryphal place variants
    "charchus":                             {"status": "names-only"},   # ISBE; 1 Esd variant; apocryphal
    "charea":                               {"status": "names-only"},   # ISBE; 1 Esd 5:32 variant; apocryphal
    "charge;-chargeable":                   {"status": "names-only"},   # ISBE combined word study
    "charges":                              {"status": "names-only"},   # ISBE word study
    "chariots-of-the-sun":                  {"status": "names-only"},   # ISBE; 2 Kgs 23:11 Josiah's reform; word study
    "charitably":                           {"status": "names-only"},   # ISBE word study (Rom 14:15 KJV)
    "charm":                                {"status": "names-only"},   # ISBE; incantation/magic; Isa 47:12; word study
    "charme":                               {"status": "names-only"},   # ISBE; 1 Esd 5:25 variant; apocryphal
    "charmis":                              {"status": "names-only"},   # ISBE; Jdt 6:15 figure; apocryphal
    "chaseba":                              {"status": "names-only"},   # ISBE; 1 Esd 5:31 variant; apocryphal
    "chaste;-chastity":                     {"status": "names-only"},   # ISBE combined word study; Tit 2:5; 1 Pet 3:2
    "chastening;-chastisement":             {"status": "names-only"},   # ISBE combined; Heb 12:5-11; covered under discipline
    "chatter":                              {"status": "names-only"},   # ISBE word study (Isa 38:14)
    # ISBE; Hebrew name for Eve (Gen 3:20 chavvah = "living"); Easton has eve.json
    "chavah":                               {"status": "redirect-only", "redirect_to": "eve"},
    "check":                                {"status": "names-only"},   # ISBE word study
    "checker-work;-network":                {"status": "names-only"},   # ISBE combined; 1 Kgs 7:17 temple decoration
    "cheek-teeth":                          {"status": "names-only"},   # ISBE; Joel 1:6 "cheek teeth of a lion"; word study
    "cheek;-cheekbone":                     {"status": "names-only"},   # ISBE combined word study
    "cheer;-cheerfulness":                  {"status": "names-only"},   # ISBE combined word study
    "chelcias":                             {"status": "names-only"},   # ISBE; Jdt 8:1 ancestor; apocryphal
    "chellians":                            {"status": "names-only"},   # ISBE; Jdt 2:23 people; apocryphal
    "chellus":                              {"status": "names-only"},   # ISBE; Jdt 1:9 place; apocryphal
    "chelod":                               {"status": "names-only"},   # ISBE; Jdt 1:6 place; apocryphal
    "cheluhi":                              {"status": "names-only"},   # ISBE; Ezra 10:35 figure; minor
    "chephar-ammoni":                       {"status": "names-only"},   # ISBE; Josh 18:24 Benjamin town; minor place
    "chephar-haamoni":                      {"status": "names-only"},   # ISBE variant of chephar-ammoni; same town
    "cherish":                              {"status": "names-only"},   # ISBE word study (1 Kgs 1:2,4; Eph 5:29)
    "cherubic-forms-in-the-constellations": {"status": "names-only"},   # ISBE; astronomical/symbolic speculation
    # ISBE numbered disambiguation; Easton has cherub.json (Ezek 1; Gen 3:24)
    "cherubim-1":                           {"status": "redirect-only", "redirect_to": "cherub"},
    # ISBE numbered disambiguation; Easton has cherub.json
    "cherubim-2":                           {"status": "redirect-only", "redirect_to": "cherub"},
    "chesnut":                              {"status": "names-only"},   # KJV "plane tree" (Gen 30:37; Ezek 31:8); word study
    "cheth":                                {"status": "names-only"},   # ISBE; Hebrew letter ח; Ps 119:57-64 section
    # ISBE variant spelling of Chittim/Kittim; Easton has chittim.json (Gen 10:4; Num 24:24)
    "chettiim":                             {"status": "redirect-only", "redirect_to": "chittim"},
    "chew;-cud":                            {"status": "names-only"},   # ISBE combined; Lev 11:3-7 clean animal law
    "chicken":                              {"status": "names-only"},   # ISBE; poultry; Matt 23:37 hen imagery
    "chide":                                {"status": "names-only"},   # ISBE word study (Exod 17:2)
    "chidon-the-threshing-floor-of":        {"status": "names-only"},   # ISBE; 1 Chr 13:9 (cf. 2 Sam 6:6 Nachon)
    "chief":                                {"status": "names-only"},   # ISBE word study
    "chief-friends;-good-men":             {"status": "names-only"},   # ISBE; 1 Macc 2:18 "king's friends"; word study
    "chief-musician":                       {"status": "names-only"},   # ISBE; Ps superscriptions למנצח; word study
    "chief-seats":                          {"status": "names-only"},   # ISBE; Matt 23:6 synagogue honor seats; word study
    "child-bearing":                        {"status": "names-only"},   # ISBE word study (1 Tim 2:15)
    "child;-children":                      {"status": "names-only"},   # ISBE combined word study
    "childhood-gospels-of-the":             {"status": "names-only"},   # ISBE; apocryphal infancy gospels
    "children-of-eden":                     {"status": "names-only"},   # ISBE; 2 Kgs 19:12; Isa 37:12 conquered people
    "children-of-god":                      {"status": "names-only"},   # ISBE; John 1:12; 1 John 3:1; word study/concept
    "children-of-israel":                   {"status": "names-only"},   # ISBE; covered under Israel; word study
    "children-of-the-bridechamber":         {"status": "names-only"},   # ISBE; Matt 9:15 "sons of the bride chamber"; word study
    "children-of-the-east":                 {"status": "names-only"},   # ISBE; Gen 29:1; Judg 6:3 Qedem peoples; word study
    "chimney":                              {"status": "names-only"},   # ISBE; Hos 13:3 KJV "chimney/window"; word study
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
    print(f'BPG Curation C33: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
