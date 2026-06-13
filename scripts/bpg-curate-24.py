"""
BPG Curation — Batch C24: aeon → amerce (gaps 2299–2398)
Gaps reviewed: 100 (all score-5 isbe-scholarly entries, A range continued)

Pure ISBE-scholarly batch. Heavy on word studies (affect, affirm, again, agree,
aim, alive, all, allege, almighty, alms, along, also, altogether, amazed, amerce),
KJV archaisms (afoot, afore, agone, albeit, allure, aloft, amain, ambushment,
amerce), and minor figures/places from Apocrypha and Nehemiah/Chronicles.

Redirects: aggaeus (Greek form of Haggai) → haggai; ahasuerus;-asseurus → ahasuerus;
alpha-and-omega → omega; amalek;-amalekite → amalek; amath;-amathis → hamath.

Script: scripts/bpg-curate-24.py
Run: python3 scripts/bpg-curate-24.py  (from project root)
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
    "aeon":                     {"status": "names-only"},   # ISBE; Greek "age/eternity"; covered under eschatology
    "aesora":                   {"status": "names-only"},   # ISBE place; Judith 4:4; apocryphal
    "affect;-affection":        {"status": "names-only"},   # ISBE word study
    "affirm;-affirmatives":     {"status": "names-only"},   # ISBE word study
    "affliction":               {"status": "names-only"},   # ISBE word study; covered under afflictions stub
    "affright":                 {"status": "names-only"},   # KJV for "terrify"; ISBE word study
    "afoot":                    {"status": "names-only"},   # ISBE word study
    "afore":                    {"status": "names-only"},   # KJV "before"; ISBE word study
    "afresh":                   {"status": "names-only"},   # ISBE word study
    "africa":                   {"status": "names-only"},   # ISBE geographic; general
    "after;-afterward":         {"status": "names-only"},   # ISBE word study
    "afternoon":                {"status": "names-only"},   # ISBE word study
    "agaba":                    {"status": "names-only"},   # ISBE variant; minor figure
    "agade":                    {"status": "names-only"},   # ISBE place; Akkad; ancient city
    "again":                    {"status": "names-only"},   # ISBE word study
    "again;-born":              {"status": "names-only"},   # ISBE; "born again" entry; covered under regeneration
    "against":                  {"status": "names-only"},   # ISBE word study
    "agape":                    {"status": "names-only"},   # ISBE; Greek love word; score-5 → names-only
    "agarenes":                 {"status": "names-only"},   # ISBE variant of Hagarenes (Ps 83:6)
    "age;-old-age":             {"status": "names-only"},   # ISBE word study
    "ages-rock-of":             {"status": "names-only"},   # ISBE; "Rock of Ages" hymnology term; not biblical term
    "aggaba":                   {"status": "names-only"},   # ISBE variant; minor figure
    # Greek form of Haggai; Easton has haggai.json
    "aggaeus":                  {"status": "redirect-only", "redirect_to": "haggai"},
    "agia":                     {"status": "names-only"},   # ISBE; obscure
    "agone":                    {"status": "names-only"},   # KJV "ago" (1 Sam 30:13); ISBE word study
    "agrapha":                  {"status": "names-only"},   # ISBE; unwritten sayings of Jesus; apocryphal
    "agrarian-laws":            {"status": "names-only"},   # ISBE scholarly article; general
    "agree":                    {"status": "names-only"},   # ISBE word study
    "ah;-aha":                  {"status": "names-only"},   # ISBE word study; exclamations
    "ahab-and-zedekiah":        {"status": "names-only"},   # false prophets (Jer 29:21); minor combined entry
    "aharahel":                 {"status": "names-only"},   # 1 Chr 4:8; Judah descendant; minor figure
    # ISBE combined variant; Easton has ahasuerus.json (Persian king; Esther)
    "ahasuerus;-asseurus":      {"status": "redirect-only", "redirect_to": "ahasuerus"},
    "ahaz-dial-of":             {"status": "names-only"},   # sundial of Ahaz (2 Kgs 20:11); single reference
    "ahi;-ah":                  {"status": "names-only"},   # ISBE variant entry; minor figures
    "ahiramite":                {"status": "names-only"},   # Ahiram's clan demonym (Num 26:38)
    "ahitob":                   {"status": "names-only"},   # ISBE variant of Ahitub; multiple minor figures
    "aholiah":                  {"status": "names-only"},   # ISBE variant of Oholiab (Exod 31:6)
    "ahuzzam;-ahuzam":          {"status": "names-only"},   # Caleb descendant (1 Chr 4:6 variant)
    "ahzai":                    {"status": "names-only"},   # Neh 11:13; minor priest figure
    "aid":                      {"status": "names-only"},   # ISBE word study
    "aijalon":                  {"status": "names-only"},   # ISBE place; Dan/Zebulun town (Josh 10:12); no Easton article
    "aijeleth-hash-shahar":     {"status": "names-only"},   # Ps 22 musical notation; "the doe of the dawn"
    "ail":                      {"status": "names-only"},   # ISBE word study
    "aim":                      {"status": "names-only"},   # ISBE word study
    "ain-1":                    {"status": "names-only"},   # ISBE numbered; Hebrew letter/spring
    "ain-2":                    {"status": "names-only"},   # ISBE place; Simeon town (Josh 15:32)
    "airus":                    {"status": "names-only"},   # ISBE; 1 Esd 5:31 variant; apocryphal
    "ajah":                     {"status": "names-only"},   # Seir's son (Gen 36:24 variant of Aiah)
    "akatan":                   {"status": "names-only"},   # ISBE; Ezra 8:12 variant of Hakkatan
    "akkad;-akkadians":         {"status": "names-only"},   # ISBE; ancient Mesopotamia (Gen 10:10)
    "akkos":                    {"status": "names-only"},   # ISBE variant of Hakkoz (Ezra 2:61)
    "akrabattine":              {"status": "names-only"},   # ISBE; 1 Macc 5:3; Maccabean region
    "al-tashheth;-al-taschith": {"status": "names-only"},   # ISBE; Ps 57–59, 75 musical notation
    "albeit":                   {"status": "names-only"},   # KJV conjunction; ISBE word study
    "alcimus":                  {"status": "names-only"},   # ISBE; Maccabean high priest (1 Macc 7:5)
    "alcove":                   {"status": "names-only"},   # ISBE; architectural term (Ezek 40:7 NIV)
    "alema":                    {"status": "names-only"},   # ISBE place; 1 Macc 5:26; apocryphal
    "aleph":                    {"status": "names-only"},   # ISBE; first Hebrew letter; general
    "aleppo":                   {"status": "names-only"},   # ISBE; Syrian city; modern reference
    "alexander-balas":          {"status": "names-only"},   # ISBE; Maccabean king (1 Macc 10:1)
    "alienate":                 {"status": "names-only"},   # ISBE word study
    "alive":                    {"status": "names-only"},   # ISBE word study
    "all":                      {"status": "names-only"},   # ISBE word study
    "allammelech":              {"status": "names-only"},   # ISBE place; Asher town (Josh 19:26)
    "allar":                    {"status": "names-only"},   # ISBE; Ezra 2:59 variant; apocryphal
    "allay":                    {"status": "names-only"},   # ISBE word study
    "allege":                   {"status": "names-only"},   # KJV Acts 17:3 "opening and alleging"; word study
    "allegiance":               {"status": "names-only"},   # ISBE word study
    "allemeth":                 {"status": "names-only"},   # ISBE place; Benjamin town variant of Alemeth
    "allied":                   {"status": "names-only"},   # ISBE word study
    "allom":                    {"status": "names-only"},   # ISBE; 1 Esd 5:34 variant; apocryphal
    "allon-bacuth":             {"status": "names-only"},   # "Oak of Weeping" (Gen 35:8); single reference
    "allow;-allowance":         {"status": "names-only"},   # ISBE word study
    "alloy":                    {"status": "names-only"},   # ISBE word study; metals
    "allure":                   {"status": "names-only"},   # ISBE word study (Hos 2:14; 2 Pet 2:18)
    "almighty":                 {"status": "names-only"},   # ISBE; El Shaddai; score-5 → names-only; covered under shaddai
    "almost":                   {"status": "names-only"},   # ISBE word study
    "alms;-almsgiving":         {"status": "names-only"},   # ISBE; charitable giving (Matt 6:2); score-5 → names-only
    "almug;-algum":             {"status": "names-only"},   # ISBE; wood type (1 Kgs 10:11); general
    "alnathan":                 {"status": "names-only"},   # ISBE variant of Elnathan; minor figures
    "aloes;-lignaloes":         {"status": "names-only"},   # ISBE; plant/burial spice (John 19:39)
    "aloft":                    {"status": "names-only"},   # ISBE word study
    "along":                    {"status": "names-only"},   # ISBE word study
    # ISBE; divine title (Rev 1:8); Easton has omega.json
    "alpha-and-omega":          {"status": "redirect-only", "redirect_to": "omega"},
    "also":                     {"status": "names-only"},   # ISBE word study
    "altaneus":                 {"status": "names-only"},   # ISBE; 1 Esd 9:33 variant; apocryphal
    "altogether":               {"status": "names-only"},   # ISBE word study
    "alway;-always":            {"status": "names-only"},   # ISBE word study
    "amadatha;-amadathus":      {"status": "names-only"},   # ISBE; Haman's father (Esth 3:1 variant)
    "amain":                    {"status": "names-only"},   # ISBE word study; archaic "at full speed"
    # ISBE place variant; Easton has amalek.json (desert people; Exod 17:8; 1 Sam 15)
    "amalek;-amalekite":        {"status": "redirect-only", "redirect_to": "amalek"},
    "amarias":                  {"status": "names-only"},   # ISBE variant of Amariah; multiple figures
    "amarna-tell-el":           {"status": "names-only"},   # ISBE; Tell el-Amarna tablets; archaeological
    "amashsai":                 {"status": "names-only"},   # ISBE; Neh 11:13 variant of Amashai
    # ISBE combined variant; Easton has hamath.json (Aramean city; Num 34:8; Amos 6:2)
    "amath;-amathis":           {"status": "redirect-only", "redirect_to": "hamath"},
    "amatheis":                 {"status": "names-only"},   # ISBE; 1 Esd 9:29 variant; apocryphal
    "amazed":                   {"status": "names-only"},   # ISBE word study
    "ambitious":                {"status": "names-only"},   # ISBE word study
    "ambushment":               {"status": "names-only"},   # KJV "ambush" (2 Chr 13:13); word study
    "amerce":                   {"status": "names-only"},   # KJV "fine/punish" (Deut 22:19); word study
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
    print(f'BPG Curation C24: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
