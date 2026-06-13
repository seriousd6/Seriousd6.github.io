"""
BPG Curation — Batch C65: sand → selemias (gaps 6524–6628)
Gaps reviewed: 105 (score-5 isbe-scholarly R–S entries — sarah, satan compounds,
sceptre, sea compounds, scythians, second-coming)

Redirects: sarah;-sarai→sarah; satan-depths-of/satan-synagogue-of→satan;
sceptre;-scepter→sceptre; screech-owl→owl; scythians→scythian;
sea-of-chinnereth→chinnereth; sea-of-galilee→galilee-sea-of; sea-of-lot→dead-sea;
sea-of-tiberias→tiberias-sea-of; sea-brazen→laver;
sea-dead;-eastern→dead-sea; sea-red→red-sea; sea-salt→salt-sea;
sea-the-molten;-sea-the-brazen→laver.
1 stub-needed; 15 redirects; 89 names-only.

Script: scripts/bpg-curate-65.py
Run: python3 scripts/bpg-curate-65.py  (from project root)
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
    "sand":                     {"status": "names-only"},   # Gen 22:17; Ps 139:18; lexical
    "sand-flies":               {"status": "names-only"},   # Exod 8:24 variant; covered under "fly"
    "sand-glowing":             {"status": "names-only"},   # Isa 35:7 KJV "parched ground"; lexical
    "sand-lizard":              {"status": "names-only"},   # Lev 11:30; covered under specific animals
    "saphat":                   {"status": "names-only"},   # apocryphal variant name
    "saphatias":                {"status": "names-only"},   # apocryphal variant (1 Esd 5:9)
    "sapheth":                  {"status": "names-only"},   # apocryphal variant
    "saphuthi":                 {"status": "names-only"},   # apocryphal variant (1 Esd 5:28)
    "sarabias":                 {"status": "names-only"},   # 1 Esd 8:54 variant; apocryphal
    # ISBE compound; Gen 17:15; Easton has sarah.json
    "sarah;-sarai":             {"status": "redirect-only", "redirect_to": "sarah"},
    "saraias":                  {"status": "names-only"},   # apocryphal variant of Seraiah
    "saramel":                  {"status": "names-only"},   # 1 Macc 14:28 location; apocryphal
    "sarchedonus":              {"status": "names-only"},   # Tobit 1:21 variant of Esarhaddon; apocryphal
    "sardeus":                  {"status": "names-only"},   # apocryphal variant
    "sardite":                  {"status": "names-only"},   # Num 26:26 clan of Sered; minor demonym
    "sardius":                  {"status": "names-only"},   # Exod 28:17; Rev 4:3 gemstone; covered under "gems"
    # ISBE; Rev 2:24 "deep things of Satan"; Easton has satan.json
    "satan-depths-of":          {"status": "redirect-only", "redirect_to": "satan"},
    # ISBE; Rev 2:9; 3:9 "synagogue of Satan"; Easton has satan.json
    "satan-synagogue-of":       {"status": "redirect-only", "redirect_to": "satan"},
    "satchel":                  {"status": "names-only"},   # KJV "bag/scrip"; archaic; brief
    "sathrabuzanes":            {"status": "names-only"},   # Ezra 5:3 variant "Shethar-bozenai"; apocryphal
    "satisfaction":             {"status": "names-only"},   # Num 35:31-32; theological/legal; lexical
    "satraps":                  {"status": "names-only"},   # Persian officials; covered under "prince"
    "savaran":                  {"status": "names-only"},   # 1 Macc 6:43 Eleazar Avaran; apocryphal
    "save":                     {"status": "names-only"},   # lexical
    "savias":                   {"status": "names-only"},   # apocryphal variant (1 Esd 5:9)
    "savor":                    {"status": "names-only"},   # KJV "smell/taste" (Eph 5:2); archaic/lexical
    "sawing-asunder":           {"status": "names-only"},   # Heb 11:37 martyrdom method; brief
    "sayest":                   {"status": "names-only"},   # KJV 2nd person archaic; lexical
    "sayings-of-jesus":         {"status": "names-only"},   # ISBE scholarly; names-only
    "sayings-dark":             {"status": "names-only"},   # Ps 78:2; Prov 1:6 "dark sayings/riddles"; lexical
    "sayings-faithful":         {"status": "names-only"},   # 1 Tim 1:15; 3:1; 4:9 "faithful saying"; brief
    "sayings-unwritten":        {"status": "names-only"},   # ISBE scholarly; agrapha; too specialized
    "scab-scabbed":             {"status": "names-only"},   # Lev 13; covered under "leprosy"
    "scabbard-sheath":          {"status": "names-only"},   # Jer 47:6; sword sheath; lexical
    "scaffold":                 {"status": "names-only"},   # 2 Chr 6:13 KJV "brasen scaffold"; brief
    "scale":                    {"status": "names-only"},   # lexical
    "scales":                   {"status": "names-only"},   # covered under "weights and measures"
    "scall":                    {"status": "names-only"},   # Lev 13:30-37 KJV skin disease; covered under "leprosy"
    "scarlet-worm":             {"status": "names-only"},   # Ps 22:6 KJV; covered under "scarlet"
    "scattered-abroad":         {"status": "names-only"},   # Jas 1:1 "diaspora"; covered under "dispersion"
    "scent":                    {"status": "names-only"},   # lexical
    # ISBE compound; Gen 49:10; Esth 4:11; Easton has sceptre.json
    "sceptre;-scepter":         {"status": "redirect-only", "redirect_to": "sceptre"},
    "school":                   {"status": "names-only"},   # Acts 19:9 "school of Tyrannus"; brief
    "science":                  {"status": "names-only"},   # Dan 1:4 KJV "knowledge"; lexical
    "scimitar":                 {"status": "names-only"},   # curved sword; not specifically biblical
    "scoff;-scoffer":           {"status": "names-only"},   # ISBE compound; 2 Pet 3:3; lexical
    "scorn":                    {"status": "names-only"},   # lexical
    "scorpions-chastising-with": {"status": "names-only"},  # 1 Kgs 12:11; brief proverbial phrase
    "scourge;-scourging":       {"status": "names-only"},   # Matt 27:26; John 19:1; covered under "scourging"
    "scrabble":                 {"status": "names-only"},   # 1 Sam 21:13 KJV; archaic/lexical
    # ISBE; Isa 34:14; already redirected owl-screech; Easton has owl.json
    "screech-owl":              {"status": "redirect-only", "redirect_to": "owl"},
    "scriptures-search-the":    {"status": "names-only"},   # John 5:39; Acts 17:11; lexical
    "scroll":                   {"status": "names-only"},   # Isa 34:4; Rev 6:14; covered under "book"
    "scum":                     {"status": "names-only"},   # Ezek 24:6-12; lexical
    "scurvy":                   {"status": "names-only"},   # Lev 21:20 KJV; covered under "disease"
    # ISBE; Col 3:11; Easton has scythian.json
    "scythians":                {"status": "redirect-only", "redirect_to": "scythian"},
    # ISBE; Num 34:11; Josh 12:3; Easton has chinnereth.json
    "sea-of-chinnereth":        {"status": "redirect-only", "redirect_to": "chinnereth"},
    # ISBE; Matt 4:18; John 6:1; Easton has galilee-sea-of.json
    "sea-of-galilee":           {"status": "redirect-only", "redirect_to": "galilee-sea-of"},
    "sea-of-joppa":             {"status": "names-only"},   # Ezra 3:7; Acts 10:5; covered under "Joppa"
    # ISBE variant name for Dead Sea; Easton has dead-sea.json
    "sea-of-lot":               {"status": "redirect-only", "redirect_to": "dead-sea"},
    "sea-of-sodom-sodomitish":  {"status": "names-only"},   # variant name for Dead Sea; names-only
    "sea-of-the-arabah":        {"status": "names-only"},   # Deut 3:17; variant for Dead Sea; names-only
    "sea-of-the-philistines":   {"status": "names-only"},   # Exod 23:31 Mediterranean; names-only
    "sea-of-the-plain-arabah":  {"status": "names-only"},   # Josh 3:16; variant for Dead Sea; names-only
    # ISBE; John 6:1; 21:1; Easton has tiberias-sea-of.json
    "sea-of-tiberias":          {"status": "redirect-only", "redirect_to": "tiberias-sea-of"},
    "sea-adriatic":             {"status": "names-only"},   # Acts 27:27 "Adria"; covered under "Adria"
    # ISBE; 1 Kgs 7:23-26; Easton has laver.json
    "sea-brazen":               {"status": "redirect-only", "redirect_to": "laver"},
    # ISBE compound; Num 34:3; Ezek 47:18; Easton has dead-sea.json
    "sea-dead;-eastern":        {"status": "redirect-only", "redirect_to": "dead-sea"},
    "sea-former":               {"status": "names-only"},   # Joel 2:20; Zech 14:8; lexical directional
    "sea-hinder;-utmost;-uttermost;-western": {"status": "names-only"},  # ISBE compound; Mediterranean; lexical
    "sea-mediterranean":        {"status": "names-only"},   # no dedicated Easton slug; covered under "great sea"
    # ISBE; Exod 10:19; Num 14:25; Easton has red-sea.json
    "sea-red":                  {"status": "redirect-only", "redirect_to": "red-sea"},
    # ISBE; Num 34:12; Deut 3:17; Easton has salt-sea.json
    "sea-salt":                 {"status": "redirect-only", "redirect_to": "salt-sea"},
    "sea-the-great":            {"status": "names-only"},   # Mediterranean; no exact Easton slug; names-only
    # ISBE compound; 1 Kgs 7:23-26; 2 Chr 4:2; Easton has laver.json
    "sea-the-molten;-sea-the-brazen": {"status": "redirect-only", "redirect_to": "laver"},
    "sea-western":              {"status": "names-only"},   # Deut 11:24 Mediterranean directional; names-only
    "sea-mew":                  {"status": "names-only"},   # Lev 11:16 KJV "sea gull"; brief
    "sea-monster":              {"status": "names-only"},   # Lam 4:3 KJV; covered under "leviathan"
    "sealed-fountain":          {"status": "names-only"},   # Song 4:12; brief
    "sealskin":                 {"status": "names-only"},   # Exod 25:5 tabernacle covering; brief
    "seam;-seamless":           {"status": "names-only"},   # ISBE compound; John 19:23; brief
    "sear":                     {"status": "names-only"},   # 1 Tim 4:2 KJV "seared conscience"; lexical
    "search":                   {"status": "names-only"},   # lexical
    "search-the-scriptures":    {"status": "names-only"},   # John 5:39; Acts 17:11; lexical
    "searchings":               {"status": "names-only"},   # Judg 5:15-16 KJV; lexical
    "seat":                     {"status": "names-only"},   # lexical
    "seats-chief":              {"status": "names-only"},   # Matt 23:6; covered under "synagogue"
    "sebam":                    {"status": "names-only"},   # Num 32:3 Reubenite place; minor
    "sechenias":                {"status": "names-only"},   # apocryphal variant (1 Esd 8:32)
    # Christ's return in glory; 1 Thess 4:16-17; Matt 24:30-31; Rev 19:11-16; Acts 1:11;
    # premillennial/amillennial/postmillennial views; parousia/Second Advent;
    # core eschatological doctrine every Christian must understand
    "second-coming":            {"status": "stub-needed"},
    "second-death":             {"status": "names-only"},   # Rev 2:11; 20:6,14; 21:8; covered under eschatology
    "second-sabbath":           {"status": "names-only"},   # Lk 6:1 KJV variant reading; disputed; lexical
    "secondarily":              {"status": "names-only"},   # 1 Cor 12:28 KJV archaic; lexical
    "secret":                   {"status": "names-only"},   # lexical
    "secu":                     {"status": "names-only"},   # 1 Sam 19:22 place near Ramah; minor
    "secure;-security":         {"status": "names-only"},   # ISBE compound; lexical
    "sedecias":                 {"status": "names-only"},   # apocryphal variant of Zedekiah
    "sedekias":                 {"status": "names-only"},   # apocryphal variant of Zedekiah
    "sedition":                 {"status": "names-only"},   # Gal 5:20 KJV; lexical
    "seduce;-seducer":          {"status": "names-only"},   # ISBE compound; 1 Tim 2:14; lexical
    "see":                      {"status": "names-only"},   # lexical
    "seed":                     {"status": "names-only"},   # lexical; covered under "agriculture"
    "seirah":                   {"status": "names-only"},   # Judg 3:26 place in Ephraim; minor
    "selemia":                  {"status": "names-only"},   # 1 Esd 9:34 apocryphal variant
    "selemias":                 {"status": "names-only"},   # 1 Esd 9:22 apocryphal variant
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
    print(f'BPG Curation C65: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
