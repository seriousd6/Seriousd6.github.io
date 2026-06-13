"""
BPG Curation — Batch C49: infidel → jacimus (gaps 4899–4998)
Gaps reviewed: 100 (score-5 isbe-scholarly I–J entries — infidel/infinity, israel
compound articles, ishmael variants, ishmaelites, island forms, izhar demonym,
ivvah/ije-abarim redirects, J-name entries beginning with Ja)

Notable redirects: israel compounds (history-of, religion-of, israelite) → israel;
ishmael-1/2 disambiguations → ishmael; ishi-1/2 → ishi; island/isles-of-gentiles → island;
ishbaal (= Ish-bosheth) → ish-bosheth. Most I entries are lexical word studies,
apocryphal variants, or minor OT names.
0 stub-needed; 21 redirects; 79 names-only.

Script: scripts/bpg-curate-49.py
Run: python3 scripts/bpg-curate-49.py  (from project root)
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
    "infidel":                   {"status": "names-only"},   # 2 Cor 6:15; 1 Tim 5:8 KJV; lexical
    "infinite;-infinitude":      {"status": "names-only"},   # ISBE compound; God's infinity; theological; names-only
    "infirmity":                 {"status": "names-only"},   # John 5:5; Rom 8:26; lexical
    "inflame;-enflame":          {"status": "names-only"},   # ISBE compound; Isa 5:11; 57:5; lexical
    "inflammation":              {"status": "names-only"},   # Deut 28:22; medical; names-only
    "influences":                {"status": "names-only"},   # Job 38:31 KJV "sweet influences of Pleiades"; lexical
    # Exod 23:16; 34:22; Feast of Tabernacles/Ingathering; Easton has feast.json
    "ingathering-feasts-of":     {"status": "redirect-only", "redirect_to": "feast"},
    "inhabit;-inhabitant":       {"status": "names-only"},   # ISBE compound; lexical
    "iniquity":                  {"status": "names-only"},   # general; covered under sin/transgression in Easton
    "injoin":                    {"status": "names-only"},   # KJV archaic "enjoin" (Philem 8; Heb 11:22); lexical
    "injurious":                 {"status": "names-only"},   # 1 Tim 1:13 KJV; lexical
    "injury":                    {"status": "names-only"},   # lexical
    "ink":                       {"status": "names-only"},   # Jer 36:18; 2 Cor 3:3; covered under inkhorn
    "inner-man":                 {"status": "names-only"},   # Rom 7:22; Eph 3:16; covered under anthropology/sanctification
    "innocence;-innocency;-innocent": {"status": "names-only"},  # ISBE compound; Matt 27:24; lexical
    "innocents-massacre-of-the": {"status": "names-only"},   # Matt 2:16-18; Herod; names-only
    "inordinate":                {"status": "names-only"},   # Col 3:5 KJV "inordinate affection"; lexical
    "inquire":                   {"status": "names-only"},   # lexical
    "inquisition":               {"status": "names-only"},   # Deut 19:18; Ps 9:12 KJV; lexical
    "inscription":               {"status": "names-only"},   # Acts 17:23; John 19:19-22; names-only
    "insects":                   {"status": "names-only"},   # Lev 11:20-23; dietary classification; names-only
    "instruction":               {"status": "names-only"},   # Prov 1:2; 2 Tim 3:16; lexical
    "instrument":                {"status": "names-only"},   # Ps 33:2; lexical
    "instruments-of-music":      {"status": "names-only"},   # 1 Chr 23:5; covered under music in Easton
    "insurrection":              {"status": "names-only"},   # Acts 18:12 KJV; lexical
    "integrity":                 {"status": "names-only"},   # Job 2:3; Ps 25:21; lexical
    "intelligence":              {"status": "names-only"},   # Dan 11:30 KJV; lexical
    "intend;-intent":            {"status": "names-only"},   # ISBE compound; lexical
    "inter-testamental-history-and-literature": {"status": "names-only"},  # ISBE scholarly; 400 "silent years"; score-5
    "intercession":              {"status": "names-only"},   # Gen 18:23-32; covered under intercession-of-christ.json
    "interest":                  {"status": "names-only"},   # Exod 22:25; "usury/interest"; covered under usury
    "intermeddle":               {"status": "names-only"},   # KJV Prov 14:10; 18:1; lexical
    "intermediate-state":        {"status": "names-only"},   # soul between death and resurrection; covered under hades
    "interpretation":            {"status": "names-only"},   # lexical
    "interpretation-of-tongues": {"status": "names-only"},   # 1 Cor 12:10; spiritual gift; covered under gifts-spiritual
    "interrogation":             {"status": "names-only"},   # 1 Pet 3:21 KJV; lexical
    "intreat;-intreaty;-entreat":{"status": "names-only"},   # ISBE compound; lexical
    "inward-man":                {"status": "names-only"},   # lexical; same concept as inner-man
    "inward-part":               {"status": "names-only"},   # lexical
    "iob":                       {"status": "names-only"},   # Gen 46:13 KJV variant of Jashub or Job; names-only
    "iphdeiah":                  {"status": "names-only"},   # 1 Chr 8:25; minor Benjaminite figure
    "iphtah":                    {"status": "names-only"},   # Josh 15:43; Judah lowland town; minor place
    "iphtah-el":                 {"status": "names-only"},   # Josh 19:14,27; Zebulun/Asher boundary valley; minor
    # ISBE disambiguation; metal iron; Easton has iron.json
    "iron-1":                    {"status": "redirect-only", "redirect_to": "iron"},
    "iron-2":                    {"status": "names-only"},   # Josh 19:38 Naphtali city "Yiron"; minor place
    "irreverence":               {"status": "names-only"},   # lexical
    "isaac-testament-of":        {"status": "names-only"},   # pseudepigraphal; apocryphal; extracanonical
    "isaiah-ascension-of":       {"status": "names-only"},   # pseudepigraphal; apocryphal; extracanonical
    "isdael":                    {"status": "names-only"},   # 1 Esd 9:34 variant; apocryphal
    "ish":                       {"status": "names-only"},   # Hebrew "man" (ish); lexical
    "ish-sechel":                {"status": "names-only"},   # 1 Sam 25:3; Nabal "a man of Belial"; names-only
    # Ish-baal = Ish-bosheth (2 Sam 2:8); Easton has ish-bosheth.json
    "ishbaal":                   {"status": "redirect-only", "redirect_to": "ish-bosheth"},
    "ishhod":                    {"status": "names-only"},   # 1 Chr 7:18; minor Manassite figure
    # ISBE disambiguation; 2 Sam 23:30; Easton has ishi.json
    "ishi-1":                    {"status": "redirect-only", "redirect_to": "ishi"},
    # ISBE disambiguation; 1 Chr 2:31; Easton has ishi.json
    "ishi-2":                    {"status": "redirect-only", "redirect_to": "ishi"},
    # ISBE disambiguation; Gen 16:15; Abraham's son; Easton has ishmael.json
    "ishmael-1":                 {"status": "redirect-only", "redirect_to": "ishmael"},
    # ISBE disambiguation; 2 Kgs 25:25; Jer 40:8; murdered Gedaliah; Easton has ishmael.json
    "ishmael-2":                 {"status": "redirect-only", "redirect_to": "ishmael"},
    # ISBE; Gen 37:25-28; Easton has ishmeelites.json
    "ishmaelites":               {"status": "redirect-only", "redirect_to": "ishmeelites"},
    "ishpah":                    {"status": "names-only"},   # 1 Chr 8:16; minor Benjaminite
    "ishuah;-isuah":             {"status": "names-only"},   # ISBE compound; Gen 46:17; 1 Chr 7:30; Asher's son
    "ishuai-ishui":              {"status": "names-only"},   # ISBE compound; 1 Sam 14:49; Saul's son
    "ishvah":                    {"status": "names-only"},   # Gen 46:17; 1 Chr 7:30 variant; Asher's son
    "ishvi":                     {"status": "names-only"},   # Gen 46:17; 1 Chr 7:30; Asher's son
    # ISBE compound; Ps 72:10; Acts 13:6; Easton has island.json
    "island;-isle":              {"status": "redirect-only", "redirect_to": "island"},
    # ISBE; Gen 10:5; coastal Mediterranean peoples; Easton has island.json
    "isles-of-the-gentiles":     {"status": "redirect-only", "redirect_to": "island"},
    "ismael":                    {"status": "names-only"},   # apocryphal/variant of Ishmael; names-only
    "ismaerus":                  {"status": "names-only"},   # 1 Esd 9:34 variant; apocryphal
    "ismaiah":                   {"status": "names-only"},   # 1 Chr 12:4; Gibeonite warrior; minor figure
    # ISBE scholarly; Easton has israel.json
    "israel-history-of":         {"status": "redirect-only", "redirect_to": "israel"},
    # ISBE scholarly; Easton has israel.json
    "israel-religion-of":        {"status": "redirect-only", "redirect_to": "israel"},
    # ISBE compound demonym; Easton has israel.json
    "israelite;-israelitish":    {"status": "redirect-only", "redirect_to": "israel"},
    "isshiah":                   {"status": "names-only"},   # 1 Chr 7:3; 24:21; minor Levite figure
    "isshijah":                  {"status": "names-only"},   # Ezra 10:31; minor OT figure
    "issue":                     {"status": "names-only"},   # lexical
    "issue-of-blood":            {"status": "names-only"},   # Matt 9:20; Luke 8:43-44; covered under miracles/healing
    "issues":                    {"status": "names-only"},   # Ps 68:20 KJV "issues from death"; lexical
    "istalcurus":                {"status": "names-only"},   # 1 Esd 9:44 variant; apocryphal
    "isvah":                     {"status": "names-only"},   # 1 Chr 7:30 variant spelling; minor
    "itala-version":             {"status": "names-only"},   # Old Latin Bible (Vetus Latina); scholarly
    "itch":                      {"status": "names-only"},   # Deut 28:27 KJV; medical; names-only
    "ithiel-and-ucal":           {"status": "names-only"},   # Prov 30:1 KJV; uncertain proper names; names-only
    "ithlah":                    {"status": "names-only"},   # Josh 19:42; Dan boundary town; minor place
    # Song 7:4 "neck like the tower of ivory"; Easton has ivory.json
    "ivory-tower-of":            {"status": "redirect-only", "redirect_to": "ivory"},
    # 2 Kgs 18:34; 19:13; Aram city; Easton has ivah.json
    "ivvah":                     {"status": "redirect-only", "redirect_to": "ivah"},
    "ivy":                       {"status": "names-only"},   # 2 Macc 6:7; Dionysiac wreath; apocryphal
    "iyar":                      {"status": "names-only"},   # Hebrew calendar month (April-May); names-only
    # Num 21:11; 33:44-45; wilderness encampment; Easton has ije-abarim.json
    "iye-abarim":                {"status": "redirect-only", "redirect_to": "ije-abarim"},
    "iyim":                      {"status": "names-only"},   # Num 33:45 wilderness camp; minor place
    "iyyar":                     {"status": "names-only"},   # variant spelling of Iyar; duplicate
    # Num 3:27; 1 Chr 26:23; Kohathite clan; Easton has izhar.json
    "izharites":                 {"status": "redirect-only", "redirect_to": "izhar"},
    "izliah;-jezliah":           {"status": "names-only"},   # ISBE compound; 1 Chr 8:18; minor Benjaminite
    "izziah":                    {"status": "names-only"},   # Ezra 10:25 KJV; minor OT figure
    # ISBE compound; Neh 7:58; Easton has jaala.json
    "jaala;-jaalah":             {"status": "redirect-only", "redirect_to": "jaala"},
    "jaar":                      {"status": "names-only"},   # Ps 132:6 "fields of Jaar" = Kirjath-jearim; brief
    "jaareshiah":                {"status": "names-only"},   # 1 Chr 8:27; minor Benjaminite figure
    # ISBE compound; Ezra 10:37; Easton has jaasau.json
    "jaasai;-jaasau":            {"status": "redirect-only", "redirect_to": "jaasau"},
    # ISBE compound variant; same figure; Easton has jaasau.json
    "jaasu;-jassai;-jaasau":     {"status": "redirect-only", "redirect_to": "jaasau"},
    # ISBE compound; Josh 15:11; 2 Chr 26:6; Easton has jabneel.json (Josh 15:11)
    "jabneel;-jabneh":           {"status": "redirect-only", "redirect_to": "jabneel"},
    "jacan":                     {"status": "names-only"},   # 1 Chr 5:13; minor Gadite figure
    "jacimus":                   {"status": "names-only"},   # 1 Macc 7:9-25; Maccabean figure; apocryphal
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
    print(f'BPG Curation C49: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
