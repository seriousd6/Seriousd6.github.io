"""
BPG Curation — Batch C47: health → holy-spirit (gaps 4699–4798)
Gaps reviewed: 100 (score-5 isbe-scholarly H entries — heaven compounds, Hebrew/Hebrews,
Hebron variants, Hezekiah compound articles, hill compounds, hermonites, hinnom,
holy-spirit, and miscellaneous H lexical/apocryphal entries)

Key redirects: heaven-host-of→host-of-heaven; heavens→heaven; hebron-1/2/hebronites→hebron;
hezekiah compounds (4 entries)→hezekiah; hill compounds→hill; hinnom-valley-of→hinnom;
holy-spirit→holy-ghost (Easton uses "holy-ghost" slug).
Apocryphal entries (hegemonides, heliodorus, herakles, hercules, hiereel, hieremoth,
hierielus, hiermas, hircanus, holm-tree) all names-only.
0 stub-needed; 21 redirects; 79 names-only.

Script: scripts/bpg-curate-47.py
Run: python3 scripts/bpg-curate-47.py  (from project root)
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
    "health":                    {"status": "names-only"},   # general; covered under healing/medicine in Easton
    "heartily":                  {"status": "names-only"},   # Col 3:23 KJV; lexical
    "heat":                      {"status": "names-only"},   # lexical; "heat of the day" (Gen 18:1)
    # 2 Kgs 17:16; Zeph 1:5; Deut 4:19; Easton has host-of-heaven.json
    "heaven-host-of":            {"status": "redirect-only", "redirect_to": "host-of-heaven"},
    "heaven-ordinances-of":      {"status": "names-only"},   # Job 38:33; cosmic laws; names-only
    "heaven-windows-of":         {"status": "names-only"},   # Gen 7:11; 8:2; Mal 3:10; idiom for rain; names-only
    "heavenly":                  {"status": "names-only"},   # lexical; "heavenly things" (John 3:12)
    # ISBE; plural; Easton has heaven.json (Deut 10:14; 1 Kgs 8:27)
    "heavens":                   {"status": "redirect-only", "redirect_to": "heaven"},
    "heavens-new-and-earth-new": {"status": "names-only"},   # Rev 21:1; 2 Pet 3:13; eschatological; no dedicated Easton article
    "heavy;-heaviness":          {"status": "names-only"},   # ISBE compound; lexical
    "heberites":                 {"status": "names-only"},   # Num 26:45; clan of Heber son of Beriah; minor
    # ISBE compound; Easton has hebrew.json (Gen 14:13; Phil 3:5)
    "hebrew;-hebrewess":         {"status": "redirect-only", "redirect_to": "hebrew"},
    "hebrews-gospel-according-to-the": {"status": "names-only"},  # apocryphal Jewish-Christian gospel; extracanonical
    "hebrews-religion-of-the":   {"status": "names-only"},   # ISBE scholarly; too broad at score-5
    # ISBE disambiguation; Gen 13:18; 23:2-19; city/cave of Machpelah; Easton has hebron.json
    "hebron-1":                  {"status": "redirect-only", "redirect_to": "hebron"},
    # ISBE disambiguation; 1 Chr 2:42-43; minor personal name; Easton has hebron.json
    "hebron-2":                  {"status": "redirect-only", "redirect_to": "hebron"},
    # ISBE; Num 3:27; 26:58; Kohathite clan; Easton has hebron.json
    "hebronites":                {"status": "redirect-only", "redirect_to": "hebron"},
    "hedgehog":                  {"status": "names-only"},   # Isa 14:23; 34:11 (bittern/hedgehog); animal/lexical
    "heed":                      {"status": "names-only"},   # lexical; "take heed" (1 Cor 10:12)
    "heel":                      {"status": "names-only"},   # Gen 3:15; 25:26; "bruise his heel"; lexical
    "hegai;-hege":               {"status": "names-only"},   # ISBE compound; Esth 2:3,8,15; eunuch of Ahasuerus
    "hegemonides":               {"status": "names-only"},   # 2 Macc 13:24; Seleucid governor; apocryphal
    # Num 19:1-10; red heifer purification ritual; Easton has heifer.json
    "heifer-red":                {"status": "redirect-only", "redirect_to": "heifer"},
    "height;-heights":           {"status": "names-only"},   # ISBE compound; lexical
    "helchiah":                  {"status": "names-only"},   # variant of Hilkiah; minor OT priestly name
    "heliodorus":                {"status": "names-only"},   # 2 Macc 3; Seleucid official struck in Temple; apocryphal
    "helkias":                   {"status": "names-only"},   # 1 Esd 1:8; apocryphal variant of Hilkiah
    "hellenism;-hellenist":      {"status": "names-only"},   # ISBE compound; Acts 6:1; 9:29; covered under Greeks/Grecians
    "helm":                      {"status": "names-only"},   # Jas 3:4 KJV "helm/rudder"; nautical; names-only
    "help":                      {"status": "names-only"},   # lexical; "God is our help" (Ps 46:1)
    # ISBE disambiguation; 1 Cor 12:28 spiritual gift "helps"; Easton has helps.json
    "helps-1":                   {"status": "redirect-only", "redirect_to": "helps"},
    # ISBE disambiguation; Acts 27:17 nautical "helps" (cables); Easton has helps.json
    "helps-2":                   {"status": "redirect-only", "redirect_to": "helps"},
    "helve":                     {"status": "names-only"},   # Deut 19:5 KJV "helve" = axe handle; lexical
    "hen-1":                     {"status": "names-only"},   # ISBE disambiguation; Matt 23:37 "as a hen"; lexical
    "hen-2":                     {"status": "names-only"},   # ISBE disambiguation; Zech 6:14 minor OT figure
    "henna":                     {"status": "names-only"},   # Song 1:14; 4:13 "camphire/henna"; botanical/cultural
    # ISBE compound; Josh 12:17; 17:2-3; Easton has hepher.json
    "hepher;-hepherites":        {"status": "redirect-only", "redirect_to": "hepher"},
    "herakles":                  {"status": "names-only"},   # 2 Macc 4:19-20; Greek mythological; apocryphal
    "hercules":                  {"status": "names-only"},   # 2 Macc 4:18-20; apocryphal; same as Herakles
    "here":                      {"status": "names-only"},   # lexical
    "hereafter":                 {"status": "names-only"},   # lexical
    "hereby":                    {"status": "names-only"},   # lexical
    "heredity":                  {"status": "names-only"},   # ISBE; biological/theological; names-only
    "herein":                    {"status": "names-only"},   # lexical
    "hereof":                    {"status": "names-only"},   # lexical
    "hereth-the-forest-of":      {"status": "names-only"},   # 1 Sam 22:5; forest where David hid; minor place
    "heretic;-heretical":        {"status": "names-only"},   # ISBE compound; Tit 3:10; covered under heresy
    "heretofore":                {"status": "names-only"},   # KJV; lexical
    "hereunto":                  {"status": "names-only"},   # KJV; lexical
    "herewith":                  {"status": "names-only"},   # KJV; lexical
    "heritage":                  {"status": "names-only"},   # Ps 16:6; 127:3; 1 Pet 5:3; lexical
    "hermeneutics":              {"status": "names-only"},   # ISBE scholarly; biblical interpretation; names-only
    "hermes-1":                  {"status": "names-only"},   # ISBE disambiguation; Acts 14:12 Greek god (Mercury)
    "hermes-2":                  {"status": "names-only"},   # ISBE disambiguation; Rom 16:14; Christian at Rome
    # ISBE; Ps 42:6 "Hermonites"; Easton has hermonites-the.json
    "hermonites":                {"status": "redirect-only", "redirect_to": "hermonites-the"},
    "hesed-son-of":              {"status": "names-only"},   # 1 Kgs 4:10; Solomon's district officer; minor figure
    "heth-1":                    {"status": "names-only"},   # ISBE disambiguation; Gen 10:15; 23:3; Hittite ancestor
    "heth-2":                    {"status": "names-only"},   # ISBE disambiguation; Hebrew letter (8th); lexical
    "hewer":                     {"status": "names-only"},   # Josh 9:21,23,27; "hewers of wood and drawers of water"; cultural
    "hexateuch":                 {"status": "names-only"},   # ISBE scholarly; Gen–Josh as a unit; names-only
    # ISBE disambiguation; 2 Kgs 18–20; king of Judah; Easton has hezekiah.json
    "hezekiah-1":                {"status": "redirect-only", "redirect_to": "hezekiah"},
    # ISBE disambiguation; Zeph 1:1; ancestor of Zephaniah; Easton has hezekiah.json
    "hezekiah-2":                {"status": "redirect-only", "redirect_to": "hezekiah"},
    # ISBE; 2 Kgs 20:1-11; the illness and sundial sign; Easton has hezekiah.json
    "hezekiahs-sickness":        {"status": "redirect-only", "redirect_to": "hezekiah"},
    # ISBE; Prov 25:1 scribes who copied Solomon's proverbs; Easton has hezekiah.json
    "hezekiah-the-men-of":       {"status": "redirect-only", "redirect_to": "hezekiah"},
    "hezro;-hezrai":             {"status": "names-only"},   # ISBE compound; 2 Sam 23:35; 1 Chr 11:37; minor warrior
    "hezron-1":                  {"status": "names-only"},   # ISBE disambiguation; Gen 46:12; Judah's son; minor
    "hezron-2":                  {"status": "names-only"},   # ISBE disambiguation; Josh 15:3; Judah's border; minor
    "hidden":                    {"status": "names-only"},   # lexical; "hidden things" (Ps 19:12; Deut 29:29)
    "hiereel":                   {"status": "names-only"},   # 1 Esd 9:27; apocryphal variant name
    "hieremoth":                 {"status": "names-only"},   # 1 Esd 9:27; apocryphal variant name
    "hierielus":                 {"status": "names-only"},   # 1 Esd 9:22; apocryphal name
    "hiermas":                   {"status": "names-only"},   # 1 Esd 9:21; apocryphal name
    "high-day":                  {"status": "names-only"},   # John 19:31 KJV "high day" = Passover Sabbath; brief
    "high-things":               {"status": "names-only"},   # Rom 12:16; 2 Cor 10:5 KJV; lexical
    "high-most":                 {"status": "names-only"},   # "Most High" El Elyon; covered under god/names of God
    "highest":                   {"status": "names-only"},   # Luke 1:32,35,76 "the Highest"; covered under God
    "highminded":                {"status": "names-only"},   # 1 Tim 6:17; 2 Tim 3:4 KJV; lexical
    # ISBE compound; hill / hill-country; Easton has hill.json
    "hill-hill-country":         {"status": "redirect-only", "redirect_to": "hill"},
    # ISBE major compound; Easton has hill.json
    "hill;-mount;-mountain":     {"status": "redirect-only", "redirect_to": "hill"},
    # ISBE; Ps 22 superscription; Easton has hind.json (Gen 49:21)
    "hind-of-the-morning-the":   {"status": "redirect-only", "redirect_to": "hind"},
    # ISBE; Jer 7:31; 32:35; "valley of slaughter"; Easton has hinnom.json
    "hinnom-valley-of":          {"status": "redirect-only", "redirect_to": "hinnom"},
    "hip":                       {"status": "names-only"},   # Judg 15:8 "hip and thigh"; lexical
    "hircanus":                  {"status": "names-only"},   # ISBE; John Hyrcanus Hasmonean ruler; historical; names-only
    "hire":                      {"status": "names-only"},   # lexical; "the laborer deserves his hire" (Luke 10:7)
    "his":                       {"status": "names-only"},   # lexical/grammatical
    "hitherto":                  {"status": "names-only"},   # KJV; lexical
    # ISBE; Josh 9:7; 11:3; singular of Hivites; Easton has hivites.json
    "hivite":                    {"status": "redirect-only", "redirect_to": "hivites"},
    "hizki":                     {"status": "names-only"},   # 1 Chr 8:17; minor Benjaminite figure
    "hoar-frost;-hoary":         {"status": "names-only"},   # ISBE compound; Exod 16:14; Job 38:29; lexical
    "hoar;-hoary":               {"status": "names-only"},   # ISBE compound; Lev 19:32; lexical
    "hobaiah":                   {"status": "names-only"},   # Ezra 2:61; Neh 7:63; variant of Habaiah; priestly family
    "hock":                      {"status": "names-only"},   # Josh 11:6,9; 2 Sam 8:4 KJV "hough" = hamstring; lexical
    "hodiah;-hodijah":           {"status": "names-only"},   # ISBE compound; Neh 8:7; 10:10-13; Levite/interpreter
    "hoise":                     {"status": "names-only"},   # Acts 27:40 KJV archaic "hoist"; nautical/lexical
    "holding":                   {"status": "names-only"},   # lexical; "holding forth the word" (Phil 2:16)
    "hollow":                    {"status": "names-only"},   # Gen 32:25 KJV "hollow of his thigh"; lexical
    "holm-tree":                 {"status": "names-only"},   # Dan 13:58 (Susanna); holm oak; apocryphal tree
    "holy-ghost-spirit-sin-against-the": {"status": "names-only"},  # Matt 12:31-32; covered under holy-ghost.json
    "holy-one":                  {"status": "names-only"},   # "the Holy One" divine title; covered under holiness/god
    # ISBE; John 14:26; Acts 2:4; Easton uses "holy-ghost" as canonical slug
    "holy-spirit":               {"status": "redirect-only", "redirect_to": "holy-ghost"},
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
    print(f'BPG Curation C47: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
