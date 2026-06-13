"""
BPG Curation — Batch C59: ornament → pelishtim (gaps 6009–6108)
Gaps reviewed: 100 (score-5 isbe-scholarly O–P entries — orphan, ospray,
owl compounds, paddan/aram redirects, pallu/palsy, parchments, pashhur,
passion, patriarch, paul compounds, peace-offering)

Redirects: orphan→orphans; ospray→osprey; owl-great/little/screech→owl;
paddan→padan; paddan-aram→padan-aram; pallu/palluites→pallu;
palsy/paralysis→palsy; paralysis-paralytic→palsy;
parchments→parchment; pashhur/pashur→pashur; passion/passions→passion;
patriarch/patriachs→patriarch; paul-the-apostle→paul;
paul-voyage-and-shipwreck→paul; peace-offering→peace-offerings.
0 stub-needed; 17 redirects; 83 names-only.

Script: scripts/bpg-curate-59.py
Run: python3 scripts/bpg-curate-59.py  (from project root)
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
    "ornament":                  {"status": "names-only"},   # Exod 33:4-6; Isa 3:18-24; names-only
    # ISBE; Jas 1:27; Easton has orphans.json
    "orphan":                    {"status": "redirect-only", "redirect_to": "orphans"},
    "orthosia":                  {"status": "names-only"},   # 1 Macc 15:37; Phoenician city; apocryphal
    "osaias":                    {"status": "names-only"},   # 1 Esd 9:48 variant; apocryphal
    "osea":                      {"status": "names-only"},   # 1 Esd 9:48 variant; apocryphal
    "oseas":                     {"status": "names-only"},   # Greek form of Hosea/Joshua; names-only
    "osee":                      {"status": "names-only"},   # Rom 9:25 Greek form of Hosea; lexical
    "osnappar":                  {"status": "names-only"},   # Ezra 4:10 KJV variant of Ashurbanipal; names-only
    # Lev 11:13; Deut 14:12; Easton has osprey.json
    "ospray":                    {"status": "redirect-only", "redirect_to": "osprey"},
    "ostraca":                   {"status": "names-only"},   # ISBE scholarly; ancient pottery-shard inscriptions; names-only
    "othonias":                  {"status": "names-only"},   # 1 Esd 9:28 variant; apocryphal
    "outcast":                   {"status": "names-only"},   # Isa 11:12; 16:3; lexical
    "outer":                     {"status": "names-only"},   # KJV "outer darkness" (Matt 8:12); lexical
    "outgoing":                  {"status": "names-only"},   # Josh 17:18; 19:14 KJV boundary term; lexical
    "outlandish":                {"status": "names-only"},   # Neh 13:26 KJV "outlandish women"; lexical
    "outrage;-outrageous":       {"status": "names-only"},   # ISBE compound; Eccl 5:8 KJV; lexical
    "outroads":                  {"status": "names-only"},   # Judg 9:25; military raids; names-only
    "outward-man":               {"status": "names-only"},   # 2 Cor 4:16; same as man-outward; names-only
    "overcharge":                {"status": "names-only"},   # Luke 21:34 KJV; lexical
    "overpass":                  {"status": "names-only"},   # Jer 5:28 KJV; lexical
    "overplus":                  {"status": "names-only"},   # Lev 25:27 KJV; lexical
    "overseer":                  {"status": "names-only"},   # Acts 20:28; Phil 1:1; covered under bishop/elder
    # ISBE disambiguation; Lev 11:17; Deut 14:16; Easton has owl.json
    "owl-great":                 {"status": "redirect-only", "redirect_to": "owl"},
    # ISBE disambiguation; Lev 11:17; Easton has owl.json
    "owl-little":                {"status": "redirect-only", "redirect_to": "owl"},
    # ISBE disambiguation; Isa 34:14; Easton has owl.json
    "owl-screech":               {"status": "redirect-only", "redirect_to": "owl"},
    "owner":                     {"status": "names-only"},   # lexical
    "ox-1":                      {"status": "names-only"},   # ISBE disambiguation; names-only
    "ox-2":                      {"status": "names-only"},   # ISBE disambiguation; names-only
    "ox-goad":                   {"status": "names-only"},   # Judg 3:31; Eccl 12:11; agricultural; names-only
    "oziel":                     {"status": "names-only"},   # 1 Esd 9:44 variant; apocryphal
    "oznites":                   {"status": "names-only"},   # Num 26:16; clan of Ozni; minor demonym
    "ozora":                     {"status": "names-only"},   # 1 Esd 9:34 variant; apocryphal
    "pacatiana":                 {"status": "names-only"},   # ISBE; Roman province; names-only
    "pace":                      {"status": "names-only"},   # 2 Sam 6:13; lexical
    "pachon":                    {"status": "names-only"},   # Egyptian calendar month; 3 Macc 6:38; apocryphal
    # ISBE; Gen 28:2-7; Easton has padan.json
    "paddan":                    {"status": "redirect-only", "redirect_to": "padan"},
    # ISBE; Gen 25:20; Easton has padan-aram.json
    "paddan-aram":               {"status": "redirect-only", "redirect_to": "padan-aram"},
    "paddle":                    {"status": "names-only"},   # Deut 23:13 KJV "paddle/shovel"; lexical
    "pain":                      {"status": "names-only"},   # lexical
    "painfulness":               {"status": "names-only"},   # 2 Cor 11:27 KJV; lexical
    "painting":                  {"status": "names-only"},   # Jer 22:14 KJV; cultural; names-only
    "pair":                      {"status": "names-only"},   # lexical
    "palaestra-palestra":        {"status": "names-only"},   # 2 Macc 4:9,12 Greek wrestling arena; apocryphal
    "palanquin":                 {"status": "names-only"},   # Song 3:9 KJV "chariot/palanquin"; names-only
    "palestine-exploration":     {"status": "names-only"},   # ISBE scholarly; archaeology; names-only
    # ISBE compound; Gen 46:9; Num 26:5; Easton has pallu.json
    "pallu-palluites":           {"status": "redirect-only", "redirect_to": "pallu"},
    "palm-of-the-hand":          {"status": "names-only"},   # 1 Sam 5:4; Isa 49:16; lexical
    # ISBE compound; Matt 8:6; Mark 2:3-12; Easton has palsy.json
    "palsy;-paralysis":          {"status": "redirect-only", "redirect_to": "palsy"},
    "panoply":                   {"status": "names-only"},   # Eph 6:11 "whole armour"; names-only
    "pap":                       {"status": "names-only"},   # Luke 11:27; Rev 1:13 KJV; lexical
    "paper-reeds":               {"status": "names-only"},   # Isa 19:7 KJV; botanical; names-only
    "papyrus":                   {"status": "names-only"},   # ISBE scholarly; ancient writing material; names-only
    "papyrus-vessels-of":        {"status": "names-only"},   # Isa 18:2 KJV; names-only
    "paraclete":                 {"status": "names-only"},   # John 14:16,26; covered under holy-ghost in Easton
    # ISBE compound; Matt 9:2; Acts 9:33; Easton has palsy.json
    "paralysis-paralytic":       {"status": "redirect-only", "redirect_to": "palsy"},
    "paramour":                  {"status": "names-only"},   # Ezek 23:20 KJV; lexical
    "parcel":                    {"status": "names-only"},   # Josh 24:32; Ruth 4:3; lexical
    "parched":                   {"status": "names-only"},   # lexical
    "parched-corn-grain":        {"status": "names-only"},   # Lev 23:14; Ruth 2:14; lexical
    # ISBE; 2 Tim 4:13; Easton has parchment.json
    "parchments":                {"status": "redirect-only", "redirect_to": "parchment"},
    "pare-the-nails":            {"status": "names-only"},   # Deut 21:12; cultural; names-only
    "parent":                    {"status": "names-only"},   # lexical
    "park":                      {"status": "names-only"},   # Neh 2:8 KJV "forest/park" = pardes; lexical
    "parousia":                  {"status": "names-only"},   # ISBE; Greek "presence/coming"; no dedicated Easton slug
    "part":                      {"status": "names-only"},   # lexical
    "particular-particularly":   {"status": "names-only"},   # ISBE compound; Heb 9:5 KJV; lexical
    "partition-the-middle-wall-of": {"status": "names-only"},  # Eph 2:14; names-only
    # ISBE compound; Jer 20:1; 38:1; Easton has pashur.json
    "pashhur-pashur":            {"status": "redirect-only", "redirect_to": "pashur"},
    "pass-passage-passenger":    {"status": "names-only"},   # ISBE compound; lexical
    "passing-of-mary-the":       {"status": "names-only"},   # apocryphal "Dormition of Mary"; extracanonical
    "passion-gospel-of-the":     {"status": "names-only"},   # apocryphal; same as nicodemus-gospel-of; extracanonical
    # ISBE compound; Acts 1:3; 14:15; Easton has passion.json
    "passion-passions":          {"status": "redirect-only", "redirect_to": "passion"},
    "pastor":                    {"status": "names-only"},   # Eph 4:11; Jer 23:1-4; names-only
    "pastoral-epistles":         {"status": "names-only"},   # ISBE scholarly; 1-2 Tim, Titus; names-only
    "pasturage;-pasture":        {"status": "names-only"},   # ISBE compound; Gen 47:4; Ps 23:2; names-only
    "pate":                      {"status": "names-only"},   # Ps 7:16 KJV "pate" = top of head; lexical
    "path;-pathway":             {"status": "names-only"},   # ISBE compound; Ps 16:11; Prov 4:18; lexical
    "patheus":                   {"status": "names-only"},   # 1 Esd 9:23 variant; apocryphal
    "patience":                  {"status": "names-only"},   # Heb 12:1; Jas 5:11; no dedicated Easton article
    # ISBE compound; Heb 7:4; Acts 2:29; Easton has patriarch.json
    "patriarch;-patriachs":      {"status": "redirect-only", "redirect_to": "patriarch"},
    "patriarchs-testaments-of-the-twelve": {"status": "names-only"},  # pseudepigraphal; apocryphal; extracanonical
    "patrimony":                 {"status": "names-only"},   # Deut 18:8 KJV; lexical
    "patroclus":                 {"status": "names-only"},   # 2 Macc 8:9; Seleucid officer; apocryphal
    "pattern":                   {"status": "names-only"},   # Exod 25:9,40; Heb 8:5; lexical
    # ISBE; Acts 13:9; Gal 1:13; Easton has paul.json
    "paul-the-apostle":          {"status": "redirect-only", "redirect_to": "paul"},
    # ISBE; Acts 27-28; Easton has paul.json
    "paul-voyage-and-shipwreck-of": {"status": "redirect-only", "redirect_to": "paul"},
    "pauline-theology":          {"status": "names-only"},   # ISBE scholarly; names-only
    "paulus-sergius":            {"status": "names-only"},   # ISBE; Acts 13:7-12; covered under sergius paulus; names-only
    "paw":                       {"status": "names-only"},   # Lev 11:27; 1 Sam 17:37; lexical
    "pe":                        {"status": "names-only"},   # Hebrew letter (17th); Ps 119:129-136; lexical
    "peace":                     {"status": "names-only"},   # Phil 4:7; Matt 5:9; names-only
    # ISBE; Lev 3; Easton has peace-offerings.json
    "peace-offering":            {"status": "redirect-only", "redirect_to": "peace-offerings"},
    "peacemaker":                {"status": "names-only"},   # Matt 5:9; names-only
    "pedestal":                  {"status": "names-only"},   # Exod 26:19-25 "socket/base"; names-only
    "pedias":                    {"status": "names-only"},   # 1 Esd 9:35 variant; apocryphal
    "pedigree":                  {"status": "names-only"},   # Num 1:18 KJV; lexical
    "peel;-pill":                {"status": "names-only"},   # ISBE compound; Gen 30:37-38; Ezek 29:18 KJV; lexical
    "peep":                      {"status": "names-only"},   # Isa 8:19; 10:14 KJV; lexical
    "pelias":                    {"status": "names-only"},   # 1 Esd 9:34 variant; apocryphal
    "pelishtim":                 {"status": "names-only"},   # ISBE; Hebrew "Philistines"; covered under philistines
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
    print(f'BPG Curation C59: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
