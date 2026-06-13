"""
BPG Curation — Batch C35: commodious → countenance (gaps 3399–3498)
Gaps reviewed: 100 (all score-5 isbe-scholarly entries, C range continued)

Mix of theological concepts (condescension-of-christ, confusion-of-tongues,
consummation, cosmogony, cosmology, conqueror, conviction → names-only),
ISBE word studies (common, compare, compel, conceit, concourse, confound,
consist, contain, contend, content, contrary, convince), and scholarly topics
(comparative-religion, concordance, coptic-versions → names-only).

Apocryphal: cor-ashan (1 Sam 30:30), corbe (1 Esd variant), corinthus
(Acts 18 city, covered under corinth in Easton), cords-small, coronation.

Redirects: communion;-fellowship → communion; concubinage → concubine;
constellations → constellation; corruption-mount-of → mount-of-corruption.

Script: scripts/bpg-curate-35.py
Run: python3 scripts/bpg-curate-35.py  (from project root)
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
    "commodious":                           {"status": "names-only"},   # ISBE; Acts 27:12 KJV "not commodious"; word study
    "common":                               {"status": "names-only"},   # ISBE word study (Acts 10:14-15)
    "commonwealth":                         {"status": "names-only"},   # ISBE word study (Eph 2:12); general
    "commune;-communicate;-communication":  {"status": "names-only"},   # ISBE combined word study
    "communion-with-demons;-devils":        {"status": "names-only"},   # ISBE; 1 Cor 10:20-21; covered under Lord's Supper
    # ISBE combined; Easton has communion.json (1 Cor 10:16; fellowship concept)
    "communion;-fellowship":                {"status": "redirect-only", "redirect_to": "communion"},
    "community-of-goods":                   {"status": "names-only"},   # ISBE; Acts 2:44-45; 4:32-35; word study
    "compact;-compacted":                   {"status": "names-only"},   # ISBE combined word study (Eph 4:16)
    "company":                              {"status": "names-only"},   # ISBE word study
    "comparative-religion":                 {"status": "names-only"},   # ISBE scholarly discipline; score-5
    "compare":                              {"status": "names-only"},   # ISBE word study
    "compass;-compasses":                   {"status": "names-only"},   # ISBE combined; Isa 44:13 drawing tool; word study
    "compassion":                           {"status": "names-only"},   # ISBE word study; general
    "compel":                               {"status": "names-only"},   # ISBE word study (Matt 5:41; Luke 14:23)
    "complaining":                          {"status": "names-only"},   # ISBE word study
    "complete":                             {"status": "names-only"},   # ISBE word study
    "composition;-compound":               {"status": "names-only"},   # ISBE combined; Exod 30:25 holy anointing oil
    "comprehend":                           {"status": "names-only"},   # ISBE word study (John 1:5)
    "conceal":                              {"status": "names-only"},   # ISBE word study
    "conceit":                              {"status": "names-only"},   # ISBE word study (Rom 12:16)
    "conception-immaculate":                {"status": "names-only"},   # ISBE; Catholic doctrine; score-5 → names-only
    "conception;-conceive":                 {"status": "names-only"},   # ISBE combined word study
    "concerning":                           {"status": "names-only"},   # ISBE word study
    "conclude":                             {"status": "names-only"},   # ISBE word study (Rom 11:32 KJV)
    "conclusion":                           {"status": "names-only"},   # ISBE word study
    "concordance":                          {"status": "names-only"},   # ISBE; Bible reference tool; general
    "concourse":                            {"status": "names-only"},   # ISBE word study (Acts 19:40; Prov 1:21)
    # ISBE; Deut 21:10-14; Gen 30:3-12 practice; Easton has concubine.json
    "concubinage":                          {"status": "redirect-only", "redirect_to": "concubine"},
    "condemn;-condemnation":                {"status": "names-only"},   # ISBE combined word study; general
    "condescension-of-christ":              {"status": "names-only"},   # ISBE; Phil 2:5-8 kenosis; covered under incarnation
    "conduct":                              {"status": "names-only"},   # ISBE word study
    "confection;-confectionary":            {"status": "names-only"},   # ISBE combined; Exod 30:35 spice mixture; word study
    "confederate;-confederacy":             {"status": "names-only"},   # ISBE combined word study; general
    "confer;-conference":                   {"status": "names-only"},   # ISBE combined word study (Gal 1:16)
    "confidence":                           {"status": "names-only"},   # ISBE word study; general
    "confirm;-confirmation":                {"status": "names-only"},   # ISBE combined word study; general
    "confiscation":                         {"status": "names-only"},   # ISBE; Ezra 7:26; word study
    "conflict":                             {"status": "names-only"},   # ISBE word study (Phil 1:30)
    "conform;-conformable":                 {"status": "names-only"},   # ISBE combined word study (Rom 8:29; Phil 3:10)
    "confound":                             {"status": "names-only"},   # ISBE word study
    "confusion":                            {"status": "names-only"},   # ISBE word study
    "confusion-of-tongues":                 {"status": "names-only"},   # ISBE; Gen 11:1-9 Tower of Babel; covered under dispersal
    "congregation-mount-of":               {"status": "names-only"},   # ISBE; Isa 14:13 "mount of assembly"; word study
    "conqueror":                            {"status": "names-only"},   # ISBE word study (Rom 8:37)
    "consecrate;-consecration":             {"status": "names-only"},   # ISBE combined word study; general
    "consent":                              {"status": "names-only"},   # ISBE word study
    "consider":                             {"status": "names-only"},   # ISBE word study
    "consist":                              {"status": "names-only"},   # ISBE word study (Col 1:17)
    "consolation":                          {"status": "names-only"},   # ISBE word study (Luke 2:25; 2 Cor 1:3-7)
    "consort":                              {"status": "names-only"},   # ISBE word study (Acts 17:4)
    "conspiracy":                           {"status": "names-only"},   # ISBE word study; general
    "constant;-constantly":                 {"status": "names-only"},   # ISBE combined word study
    # ISBE; Job 9:9; 38:31-32; Amos 5:8 star clusters; Easton has constellation.json
    "constellations":                       {"status": "redirect-only", "redirect_to": "constellation"},
    "constrain":                            {"status": "names-only"},   # ISBE word study (2 Cor 5:14)
    "consult":                              {"status": "names-only"},   # ISBE word study
    "consume":                              {"status": "names-only"},   # ISBE word study
    "consummation":                         {"status": "names-only"},   # ISBE; Matt 24:3 "end of the age"; word study
    "consumption":                          {"status": "names-only"},   # ISBE; Deut 28:22 disease; Isa 10:22-23; word study
    "contain":                              {"status": "names-only"},   # ISBE word study (1 Cor 7:9)
    "contend;-contention":                  {"status": "names-only"},   # ISBE combined word study
    "content;-contentment":                 {"status": "names-only"},   # ISBE combined; Phil 4:11; 1 Tim 6:6; word study
    "continency":                           {"status": "names-only"},   # ISBE; self-restraint; 1 Cor 7:9; word study
    "continual;-continually":               {"status": "names-only"},   # ISBE combined word study
    "continuance":                          {"status": "names-only"},   # ISBE word study (Rom 2:7)
    "contradiction":                        {"status": "names-only"},   # ISBE word study (Heb 12:3)
    "contrary":                             {"status": "names-only"},   # ISBE word study
    "contribution":                         {"status": "names-only"},   # ISBE word study (Rom 15:26)
    "contrite;-contrition":                 {"status": "names-only"},   # ISBE combined; Isa 57:15; Ps 51:17; word study
    "controversy":                          {"status": "names-only"},   # ISBE word study (Mic 6:2; 1 Tim 3:16)
    "convenient":                           {"status": "names-only"},   # ISBE word study
    "convent":                              {"status": "names-only"},   # ISBE; monastic term; extra-biblical
    "conversant":                           {"status": "names-only"},   # ISBE word study (Josh 8:35 KJV)
    "convict;-conviction":                  {"status": "names-only"},   # ISBE combined word study (John 16:8)
    "convince":                             {"status": "names-only"},   # ISBE word study (Tit 1:9)
    "convulsing":                           {"status": "names-only"},   # ISBE; Mark 1:26; 9:20 demon manifestation; word study
    "cool":                                 {"status": "names-only"},   # ISBE word study (Gen 3:8; Luke 16:24)
    "coping":                               {"status": "names-only"},   # ISBE; architectural term; 1 Kgs 7:9; word study
    "coppersmith":                          {"status": "names-only"},   # ISBE; 2 Tim 4:14 Alexander the coppersmith; word study
    "coptic-versions":                      {"status": "names-only"},   # ISBE; Bible translation; scholarly
    "cor-ashan":                            {"status": "names-only"},   # ISBE; 1 Sam 30:30 Judah town; minor place
    "corbe":                                {"status": "names-only"},   # ISBE; 1 Esd variant; apocryphal
    "cords-small":                          {"status": "names-only"},   # ISBE; John 2:15 "small cords"; word study
    "corinthus":                            {"status": "names-only"},   # ISBE; Acts 18 city; covered under corinth in Easton
    "corner-gate":                          {"status": "names-only"},   # ISBE; 2 Kgs 14:13; Jer 31:38 Jerusalem gate
    "corners-of-the-earth":                 {"status": "names-only"},   # ISBE; Isa 11:12 "four corners"; cosmological
    "cornfloor":                            {"status": "names-only"},   # ISBE; Hos 9:1 KJV threshing floor; word study
    "coronation":                           {"status": "names-only"},   # ISBE; Israelite kingship ceremony; general
    "corpse":                               {"status": "names-only"},   # ISBE word study
    "correction":                           {"status": "names-only"},   # ISBE word study; general
    "corruption":                           {"status": "names-only"},   # ISBE word study (Acts 2:27; Rom 8:21)
    # ISBE; 2 Kgs 23:13 "Mount of Corruption" (Olivet); Easton has mount-of-corruption.json
    "corruption-mount-of":                  {"status": "redirect-only", "redirect_to": "mount-of-corruption"},
    "cos":                                  {"status": "names-only"},   # ISBE; Aegean island (Acts 21:1); general place
    "cosmogony":                            {"status": "names-only"},   # ISBE scholarly; Genesis/creation origins theory
    "cosmology":                            {"status": "names-only"},   # ISBE scholarly; biblical worldview
    "costliness":                           {"status": "names-only"},   # ISBE word study (Rev 18:19)
    "couching-place":                       {"status": "names-only"},   # ISBE; Ezek 25:5 resting place; word study
    "council;-councillor":                  {"status": "names-only"},   # ISBE combined word study; general
    "counsel;-counsellor":                  {"status": "names-only"},   # ISBE combined word study; general
    "count":                                {"status": "names-only"},   # ISBE word study
    "countenance":                          {"status": "names-only"},   # ISBE word study; general
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
    print(f'BPG Curation C35: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
