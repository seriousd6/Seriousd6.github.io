"""
BPG Curation — Batch C26: appoint → ashhur (gaps 2499–2598)
Gaps reviewed: 100 (all score-5 isbe-scholarly entries, A range continued)

Clusters: Aramean kingdoms (aram-dammesek/maacah/rehob → names-only), apocryphal
figures (1 Esd variants: ararah, ararath, arbatta, arna, arom, asadias, etc. → all
names-only), archaeology/language scholarly articles (aramaic-versions, arabic-versions,
armenian-versions → names-only), and minor Asher/Ash- entries.

Redirects: arab;-arabians/arabian → arabia; arimathaea → arimathea;
ark-of-bulrushes/ark-of-noah/ark-of-testimony → ark; arpachshad → arphaxad;
asher-1 → asher.

Script: scripts/bpg-curate-26.py
Run: python3 scripts/bpg-curate-26.py  (from project root)
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
    "appoint":                          {"status": "names-only"},   # ISBE word study
    "apprehend":                        {"status": "names-only"},   # ISBE word study
    "approve":                          {"status": "names-only"},   # ISBE word study
    "apt":                              {"status": "names-only"},   # ISBE word study (1 Tim 3:2)
    "aqueduct":                         {"status": "names-only"},   # ISBE; Hezekiah's tunnel etc.; general
    "ar-ar-of-moab":                    {"status": "names-only"},   # ISBE place; Moabite city (Num 21:15); no Easton
    # ISBE combined variant; Easton has arabia.json (desert people; Gal 1:17)
    "arab;-arabians":                   {"status": "redirect-only", "redirect_to": "arabia"},
    "arabattine":                       {"status": "names-only"},   # ISBE; 1 Macc 5:3; apocryphal region
    # ISBE demonym; Easton has arabia.json
    "arabian":                          {"status": "redirect-only", "redirect_to": "arabia"},
    "arabic-gospel-of-the-infancy":     {"status": "names-only"},   # ISBE; apocryphal NT text
    "arabic-history-of-joseph-the-carpenter": {"status": "names-only"},  # ISBE; apocryphal text
    "arabic-language":                  {"status": "names-only"},   # ISBE; Semitic language; general
    "arabic-versions":                  {"status": "names-only"},   # ISBE; Bible translation history
    "araboth":                          {"status": "names-only"},   # ISBE variant of Arabah; Jordan valley
    "aradus":                           {"status": "names-only"},   # ISBE place; Phoenician island (1 Macc 15:23)
    "aram-dammesek":                    {"status": "names-only"},   # ISBE; "Aram of Damascus"; 2 Sam 8:5
    "aram-maacah":                      {"status": "names-only"},   # ISBE; Aramean kingdom (1 Chr 19:6)
    "aram-rehob":                       {"status": "names-only"},   # ISBE; Aramean kingdom (2 Sam 10:8)
    "aramaeans;-arameans":              {"status": "names-only"},   # ISBE; Aramean peoples; general
    "aramaic-versions":                 {"status": "names-only"},   # ISBE; Targumim; scholarly
    "aramaic;-aramaic-language":        {"status": "names-only"},   # ISBE; Daniel/Ezra language; scholarly
    "ararah":                           {"status": "names-only"},   # ISBE; 1 Esd 5:36 variant; apocryphal
    "ararath":                          {"status": "names-only"},   # ISBE; 1 Esd variant; apocryphal
    "arathes":                          {"status": "names-only"},   # ISBE; 1 Macc 15:22 Cappadocian king
    "arba-city-of":                     {"status": "names-only"},   # ISBE; Hebron (Josh 15:13; 21:11)
    "arbatta":                          {"status": "names-only"},   # ISBE; 1 Macc 5:23; apocryphal region
    "arbela":                           {"status": "names-only"},   # ISBE; 1 Macc 9:2; apocryphal battle site
    "arbonai":                          {"status": "names-only"},   # ISBE; obscure variant
    "archaeology-of-asia-minor":        {"status": "names-only"},   # ISBE scholarly article; specialized
    "archaeology;-archaeology-and-criticism": {"status": "names-only"},  # ISBE scholarly; general reference
    "archites":                         {"status": "names-only"},   # ISBE; people of Archi (Josh 16:2)
    "archives":                         {"status": "names-only"},   # ISBE word study; Ezra 4:15
    "ardat":                            {"status": "names-only"},   # ISBE; 4 Ezra; apocryphal
    "arelites":                         {"status": "names-only"},   # ISBE; Arel's clan (Num 26:17)
    "areopolis":                        {"status": "names-only"},   # ISBE; Moabite city; general
    "ares":                             {"status": "names-only"},   # ISBE; Greek war god; Acts 17:28 context
    "argob-1":                          {"status": "names-only"},   # ISBE numbered; 2 Kgs 15:25 person/region
    "argob-2":                          {"status": "names-only"},   # ISBE place; Bashan region (Deut 3:4)
    "argue":                            {"status": "names-only"},   # ISBE word study
    "ariarathes":                       {"status": "names-only"},   # ISBE; Cappadocian king (1 Macc 15:22)
    "aright":                           {"status": "names-only"},   # ISBE word study
    # ISBE place; Joseph of Arimathea's hometown; Easton has arimathea.json
    "arimathaea":                       {"status": "redirect-only", "redirect_to": "arimathea"},
    "arithmetic":                       {"status": "names-only"},   # ISBE; numbers in Bible; general
    "arius":                            {"status": "names-only"},   # ISBE; Spartan king (1 Macc 12:7)
    # Moses' basket (Exod 2:3); Easton has ark.json (covers both ark of covenant and Noah's ark)
    "ark-of-bulrushes":                 {"status": "redirect-only", "redirect_to": "ark"},
    # Noah's ark (Gen 6-9); Easton has ark.json
    "ark-of-noah":                      {"status": "redirect-only", "redirect_to": "ark"},
    # ISBE; "ark of testimony" = ark of the covenant; Easton has ark.json
    "ark-of-testimony":                 {"status": "redirect-only", "redirect_to": "ark"},
    "armenian-versions-of-the-bible":   {"status": "names-only"},   # ISBE; scholarly; specialized
    "armenian;-aryan;-religion":        {"status": "names-only"},   # ISBE; comparative religion; specialized
    "armhole":                          {"status": "names-only"},   # KJV "armpit" (Jer 38:12); word study
    "armor-bearer":                     {"status": "names-only"},   # ISBE; military role (Judg 9:54); general
    "armor;-arms":                      {"status": "names-only"},   # ISBE combined; weapons/warfare; general
    "armory":                           {"status": "names-only"},   # ISBE; Song 4:4; Neh 3:19; general
    "army-roman":                       {"status": "names-only"},   # ISBE; Roman military; general
    "arna":                             {"status": "names-only"},   # ISBE; 1 Esd 8:43 variant; apocryphal
    "arom":                             {"status": "names-only"},   # ISBE; 1 Esd 5:16 variant; apocryphal
    # ISBE variant of Arphaxad (Gen 10:22); Easton has arphaxad.json
    "arpachshad":                       {"status": "redirect-only", "redirect_to": "arphaxad"},
    "arpad;-arphad":                    {"status": "names-only"},   # ISBE place; Aramean city (2 Kgs 18:34)
    "array":                            {"status": "names-only"},   # ISBE word study
    "arrest-and-trial-of-jesus":        {"status": "names-only"},   # ISBE; passion narrative; covered elsewhere
    "arrive":                           {"status": "names-only"},   # ISBE word study
    "arrogancy":                        {"status": "names-only"},   # ISBE word study (1 Sam 2:3; Isa 13:11)
    "arrow":                            {"status": "names-only"},   # ISBE; weapon; general
    "arrows-divination-by":             {"status": "names-only"},   # ISBE; belomancy (Ezek 21:21); general
    "arrowsnake":                       {"status": "names-only"},   # ISBE; KJV Isa 34:15 animal translation
    "arsaces":                          {"status": "names-only"},   # ISBE; Arsacid/Parthian king (1 Macc 14:2)
    "arsareth":                         {"status": "names-only"},   # ISBE; 4 Ezra; apocryphal place
    "arsiphurith":                      {"status": "names-only"},   # ISBE; 1 Esd variant; apocryphal
    "artemis":                          {"status": "names-only"},   # ISBE; Diana/Ephesus (Acts 19:24-35); general
    "artisan":                          {"status": "names-only"},   # ISBE; craftsman; general
    "arts":                             {"status": "names-only"},   # ISBE; magic arts; general
    "arubboth;-aruboth":                {"status": "names-only"},   # ISBE; Solomon's district (1 Kgs 4:10)
    "arvad;-arvadites":                 {"status": "names-only"},   # ISBE place; Phoenician island (Gen 10:18)
    "arzareth":                         {"status": "names-only"},   # ISBE; 4 Ezra; apocryphal place
    "as":                               {"status": "names-only"},   # ISBE word study
    "asadias":                          {"status": "names-only"},   # ISBE; 1 Macc 2:1 variant; apocryphal
    "asael":                            {"status": "names-only"},   # ISBE variant of Asahel; multiple figures
    "asana":                            {"status": "names-only"},   # ISBE; 1 Esd variant; apocryphal
    "asara":                            {"status": "names-only"},   # ISBE; 1 Esd variant; apocryphal
    "asaramel":                         {"status": "names-only"},   # ISBE; 1 Macc 14:28 Hasmonean title
    "asarel":                           {"status": "names-only"},   # ISBE; Judah descendant (1 Chr 4:16)
    "asbacaphath":                      {"status": "names-only"},   # ISBE; 1 Esd variant; apocryphal
    "asbasareth":                       {"status": "names-only"},   # ISBE; 1 Esd variant; apocryphal
    "ascend":                           {"status": "names-only"},   # ISBE word study
    "ascension-of-isaiah":              {"status": "names-only"},   # ISBE; apocryphal/pseudepigraphical text
    "ascent":                           {"status": "names-only"},   # ISBE word study
    "aschenaz":                         {"status": "names-only"},   # ISBE variant of Ashkenaz (Gen 10:3)
    "aseas":                            {"status": "names-only"},   # ISBE; 1 Esd variant; apocryphal
    "asebebias":                        {"status": "names-only"},   # ISBE; 1 Esd variant; apocryphal
    "asebias":                          {"status": "names-only"},   # ISBE; 1 Esd variant; apocryphal
    "aserer":                           {"status": "names-only"},   # ISBE; 1 Esd variant; apocryphal
    "ash-1":                            {"status": "names-only"},   # ISBE numbered; ash tree (Isa 44:14 KJV)
    "ash-2":                            {"status": "names-only"},   # ISBE numbered; minor entry
    "ashamed":                          {"status": "names-only"},   # ISBE word study
    "asharelah;-asarelah":              {"status": "names-only"},   # ISBE combined; Levite (1 Chr 25:2 variant)
    "ashbel;-ashbelite":                {"status": "names-only"},   # ISBE combined; Benjamin's son (Gen 46:21)
    "ashdoth-pisgah":                   {"status": "names-only"},   # ISBE; "slopes of Pisgah" (Deut 3:17)
    # ISBE numbered; Easton has asher.json (tribe of Asher; Gen 30:13)
    "asher-1":                          {"status": "redirect-only", "redirect_to": "asher"},
    "asher-2":                          {"status": "names-only"},   # ISBE place; town near Shechem (Josh 17:7)
    "ashhur":                           {"status": "names-only"},   # ISBE place; Judah descendant (1 Chr 2:24)
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
    print(f'BPG Curation C26: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
