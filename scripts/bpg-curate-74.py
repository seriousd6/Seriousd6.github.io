"""
BPG Curation — Batch C74: well-jacobs → zedekiah-2 (gaps 7469–7573)
Gaps reviewed: 105 (score-5 isbe-scholarly W–Z entries)

Score-5 W–Z ISBE entries: lexical KJV terms, minor Z-name disambiguations,
apocryphal figures, Hebrew letter names. Notable stubs: Wisdom (Prov 8 personification;
fear of the LORD motif), Wisdom Literature (Job/Psalms/Prov/Eccl/Song as category),
Word (Logos, John 1:1-14).
3 stub-needed; 2 redirect-only; 100 names-only.

Script: scripts/bpg-curate-74.py
Run: python3 scripts/bpg-curate-74.py  (from project root)
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
    "well-jacobs":           {"status": "names-only"},   # Gen 29:2; covered under wells/patriarchs
    "wellspring":            {"status": "names-only"},   # Prov 4:23 "wellspring of life"; lexical
    "wen":                   {"status": "names-only"},   # KJV Lev 22:22 skin disease; lexical
    "wench":                 {"status": "names-only"},   # KJV 2 Sam 17:17 "servant girl"; lexical
    "west":                  {"status": "names-only"},   # directional; lexical
    "whelp":                 {"status": "names-only"},   # KJV "young lion cub" (Gen 49:9); lexical
    "whirlwind":             {"status": "names-only"},   # 2 Kgs 2:11 Elijah; Job 38:1; covered elsewhere
    "white-horse":           {"status": "names-only"},   # Rev 6:2; 19:11; covered under Revelation
    "whitewash":             {"status": "names-only"},   # Ezek 13:10-16; Matt 23:27; covered under hypocrisy
    "whole;-wholesome":      {"status": "names-only"},   # ISBE compound; lexical
    "whore;-whoredom":       {"status": "names-only"},   # covered under harlot/adultery in Easton
    "wickedness":            {"status": "names-only"},   # covered under sin/evil in Easton; lexical
    "wife-brothers":         {"status": "names-only"},   # levirate context; covered under levirate marriage
    "wild-beast":            {"status": "names-only"},   # Dan 7; Rev 13 symbolic; covered under apocalyptic
    "wild-ox":               {"status": "names-only"},   # Num 23:22; Ps 22:21; lexical; botanical/fauna
    "will":                  {"status": "names-only"},   # lexical
    "will-volition":         {"status": "names-only"},   # philosophical; covered under free will concepts
    "will-worship":          {"status": "names-only"},   # Col 2:23 KJV "self-imposed worship"; lexical
    "willow-tree":           {"status": "names-only"},   # Ps 137:2 "willows of Babylon"; botanical
    "wind":                  {"status": "names-only"},   # lexical; spirit/ruach connection lexical here
    "windows-of-heaven":     {"status": "names-only"},   # Gen 7:11; 2 Kgs 7:2; Mal 3:10; lexical
    "wine-skins":            {"status": "names-only"},   # Matt 9:17 new wine old wineskins; lexical
    "wine;-wine-press":      {"status": "names-only"},   # ISBE compound; covered under wine in Easton
    "winebibber":            {"status": "names-only"},   # KJV "drunkard" (Matt 11:19); lexical
    "winefat;-wine-press;-winevat": {"status": "names-only"},  # compound; covered under winepress
    "winevat":               {"status": "names-only"},   # KJV winepress variant; lexical
    "wings":                 {"status": "names-only"},   # Ps 91:4; Ruth 2:12; lexical/symbolic
    "wink":                  {"status": "names-only"},   # Prov 6:13; Acts 17:30; lexical
    "winter":                {"status": "names-only"},   # seasonal; lexical
    "winter-house":          {"status": "names-only"},   # Jer 36:22; Amos 3:15; cultural
    # "The fear of the LORD is the beginning of wisdom" (Prov 9:10; Ps 111:10); personified in
    # Prov 8 ("I was beside him, like a master workman"); practical theology of Proverbs/Ecclesiastes;
    # NT: "Christ… the wisdom of God" (1 Cor 1:24); James 1:5 "ask God who gives generously"
    "wisdom":                {"status": "stub-needed"},
    # Five books: Job, Psalms, Proverbs, Ecclesiastes, Song of Songs; characteristics: observation
    # of creation, retribution theology debate (Job), personified wisdom, Sitz im Leben; essential
    # framework for reading OT poetry and practical theology
    "wisdom-literature":     {"status": "stub-needed"},
    "wisdom-of-god":         {"status": "names-only"},   # divine attribute; covered under God in Easton
    # "The Wisdom of Jesus son of Sirach" = Sirach / Ecclesiasticus (deuterocanonical); redirect
    "wisdom-of-jesus":       {"status": "redirect-only", "redirect_to": "sirach"},
    "wisdom-of-solomon-the": {"status": "names-only"},   # deuterocanonical; too specialized at score-5
    "wise-man":              {"status": "names-only"},   # covered under magi and wise men in Easton
    "wish":                  {"status": "names-only"},   # lexical
    "wist-witty-wot":        {"status": "names-only"},   # KJV archaic terms; lexical
    "witch;-witchcraft":     {"status": "names-only"},   # covered under magic/divination in Easton
    "withered":              {"status": "names-only"},   # lexical; miracles (Mark 3:1-5) covered elsewhere
    "withes-withs-green":    {"status": "names-only"},   # KJV Judg 16:7-8 Samson's ropes; lexical
    "witty":                 {"status": "names-only"},   # KJV Prov 8:12 "inventive/clever"; lexical
    "wonder;-wonderful":     {"status": "names-only"},   # covered under miracles/signs in Easton
    "wood-of-ephraim":       {"status": "names-only"},   # 2 Sam 18:6-8 Absalom's death; geographic
    "woof":                  {"status": "names-only"},   # KJV Lev 13:48 "weft of fabric"; lexical
    # "In the beginning was the Word… and the Word was God" (John 1:1-14); OT dabar/logos connection;
    # "Word of God" as Scripture (Heb 4:12); Christ as the Living Word; foundational Christology
    "word":                  {"status": "stub-needed"},
    "work;-works":           {"status": "names-only"},   # covered under justification/faith in Easton
    "worker;-workfellow;-workman": {"status": "names-only"},  # lexical
    "world-general":         {"status": "names-only"},   # ISBE sub-entry; lexical
    "world-cosmological":    {"status": "names-only"},   # philosophical; names-only
    "world-end-of-the":      {"status": "names-only"},   # covered under eschatology in Easton
    "worm;-scarlet-worm":    {"status": "names-only"},   # Ps 22:6; Isa 66:24; lexical
    "wormwood-the-star":     {"status": "names-only"},   # Rev 8:10-11; covered under Revelation
    "worship-image":         {"status": "names-only"},   # ISBE sub-topic; covered under idolatry
    "worthies":              {"status": "names-only"},   # general; lexical
    "wot":                   {"status": "names-only"},   # KJV "know" (Gen 21:26); lexical
    "wrath-anger":           {"status": "names-only"},   # ISBE compound; covered under wrath in Easton
    "wrest":                 {"status": "names-only"},   # KJV "pervert" (Exod 23:2); lexical
    "wrinkle":               {"status": "names-only"},   # Eph 5:27; lexical
    "xanthicus":             {"status": "names-only"},   # Macedonian month (2 Macc 11:30); apocryphal
    # Persian king = Ahasuerus of Esther (Esth 1:1); redirect to canonical article
    "xerxes":                {"status": "redirect-only", "redirect_to": "ahasuerus"},
    "yea":                   {"status": "names-only"},   # KJV affirmative; lexical
    "years-seventy":         {"status": "names-only"},   # Jer 25:11; Dan 9; covered under Daniel/Jeremiah
    "yellow":                {"status": "names-only"},   # Lev 13:30; Ps 68:13; lexical
    "yodh":                  {"status": "names-only"},   # Hebrew letter; names-only
    "young;-men-young-women": {"status": "names-only"},  # ISBE compound; lexical
    "zaanannim;-plain-or-oak-of": {"status": "names-only"},  # Judg 4:11 Sisera; geographic
    "zabadaeans":            {"status": "names-only"},   # 1 Macc 12:31 Arabian tribe; apocryphal
    "zabadaias":             {"status": "names-only"},   # apocryphal variant; names-only
    "zabadeas":              {"status": "names-only"},   # apocryphal; names-only
    "zabdeus":               {"status": "names-only"},   # apocryphal (1 Esd 8:39); names-only
    "zacharias-1":           {"status": "names-only"},   # ISBE disambiguation; Zechariah/Zacharias
    "zacharias-2":           {"status": "names-only"},   # disambiguation; names-only
    "zachary":               {"status": "names-only"},   # variant of Zechariah; names-only
    "zain":                  {"status": "names-only"},   # Hebrew letter variant; names-only
    "zaketan":               {"status": "names-only"},   # minor figure (1 Esd 8:32); apocryphal
    "zalmunnah":             {"status": "names-only"},   # Midianite king (Judg 8); covered under Gideon
    "zambis":                {"status": "names-only"},   # apocryphal; names-only
    "zambri":                {"status": "names-only"},   # variant of Zimri (1 Macc 2:26); names-only
    "zamoth":                {"status": "names-only"},   # apocryphal (1 Esd 9:28); names-only
    "zaphenath-paneah-zaphnath-paaneah": {"status": "names-only"},  # Joseph's Egyptian name (Gen 41:45); covered under Joseph
    "zara":                  {"status": "names-only"},   # NT genealogy Matt 1:3 (Zerah); names-only
    "zaraces":               {"status": "names-only"},   # apocryphal variant; names-only
    "zaraias":               {"status": "names-only"},   # apocryphal variant (1 Esd 8:2); names-only
    "zarakes":               {"status": "names-only"},   # apocryphal; names-only
    "zardeus":               {"status": "names-only"},   # apocryphal (1 Esd 8:39); names-only
    "zareathites":           {"status": "names-only"},   # demonym for Zorah (1 Chr 2:53); names-only
    "zarethan":              {"status": "names-only"},   # Josh 3:16; 1 Kgs 4:12 geographic; names-only
    "zarezth-shahar":        {"status": "names-only"},   # Reuben border (Josh 13:19); minor place
    "zarhites":              {"status": "names-only"},   # Zerahite clan (Num 26:13); names-only
    "zathoes":               {"status": "names-only"},   # returned exiles (1 Esd 5:28); apocryphal
    "zathui":                {"status": "names-only"},   # apocryphal (1 Esd 8:32); names-only
    "zayin":                 {"status": "names-only"},   # Hebrew letter; names-only
    "zealot;-zealots":       {"status": "names-only"},   # ISBE compound; covered under zealot/Simon in Easton
    "zebah-and-zalmunna":    {"status": "names-only"},   # Midianite kings (Judg 8); covered under Gideon
    "zebidah":               {"status": "names-only"},   # Jehoiakim's mother (2 Kgs 23:36); minor figure
    "zebulunites":           {"status": "names-only"},   # demonym; covered under Zebulun
    "zechariah-1":           {"status": "names-only"},   # ISBE disambiguation; covered under Zechariah in Easton
    "zechariah-2":           {"status": "names-only"},   # disambiguation; names-only
    "zechariah-book-of":     {"status": "names-only"},   # covered under Zechariah in Easton
    "zecher":                {"status": "names-only"},   # minor Benjaminite (1 Chr 8:31); names-only
    "zechrias":              {"status": "names-only"},   # apocryphal variant; names-only
    "zedechias":             {"status": "names-only"},   # apocryphal variant of Zedekiah; names-only
    "zedekiah-1":            {"status": "names-only"},   # last king of Judah; covered in Easton
    "zedekiah-2":            {"status": "names-only"},   # disambiguation; names-only
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
    print(f'BPG Curation C74: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
