"""
BPG Curation — Batch C30: berytus → blood-revenge (gaps 2899–2998)
Gaps reviewed: 100 (score-5 isbe-scholarly B entries — Beth-* places, lexical, apocryphal)

Score-5 ISBE continues near-total names-only. Notable stubs:
Between the Testaments (400-year intertestamental period; Pharisees/Sadducees/Essenes rise),
Virgin Birth (Isa 7:14; Matt 1:18-25; Luke 1:26-38; central Christology).
2 stub-needed; 0 redirects; 98 names-only.

Script: scripts/bpg-curate-30.py
Run: python3 scripts/bpg-curate-30.py  (from project root)
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
    "berytus":                {"status": "names-only"},   # ancient Beirut; extrabiblical
    "berzelus":               {"status": "names-only"},   # apocryphal figure (1 Esd 5:38)
    "beset":                  {"status": "names-only"},   # lexical; "sin which so easily besets" (Heb 12:1 KJV)
    "beside":                 {"status": "names-only"},   # lexical
    "besiege":                {"status": "names-only"},   # lexical; military action
    "best":                   {"status": "names-only"},   # lexical
    "bestiality":             {"status": "names-only"},   # Lev 18:23; 20:15-16; Exod 22:19; purity law term
    "bestow":                 {"status": "names-only"},   # lexical
    "betane":                 {"status": "names-only"},   # minor place variant
    "beth-1":                 {"status": "names-only"},   # ISBE disambiguation; Hebrew "house of"; lexical
    "beth-2":                 {"status": "names-only"},   # ISBE disambiguation; Hebrew letter; lexical
    "beth-biri":              {"status": "names-only"},   # town in Simeon (1 Chr 4:31); minor place
    "beth-eden":              {"status": "names-only"},   # place in Syria (Amos 1:5); brief prophetic reference
    "beth-haccherem":         {"status": "names-only"},   # Neh 3:14; Jer 6:1 (beacon site); minor place
    "beth-haggan":            {"status": "names-only"},   # 2 Kgs 9:27; minor place
    "beth-hanan;-elon-beth-hanan": {"status": "names-only"},  # ISBE compound; 1 Kgs 4:9 district
    "beth-haram":             {"status": "names-only"},   # Transjordan town (Josh 13:27); minor place
    "beth-hoglah":            {"status": "names-only"},   # boundary town (Josh 15:6; 18:19,21); minor place
    "beth-horon-the-battle-of": {"status": "names-only"},  # Josh 10:10-14; covered under Joshua/Joshua's battles
    "beth-lehemite":          {"status": "names-only"},   # demonym for Bethlehem; minor epithet
    "beth-maacah":            {"status": "names-only"},   # 2 Sam 20:14-15; minor place
    "beth-merhak":            {"status": "names-only"},   # 2 Sam 15:17; minor place
    "beth-millo":             {"status": "names-only"},   # Judg 9:6,20; 2 Kgs 12:20; citadel in Shechem
    "beth-pelet":             {"status": "names-only"},   # town in Judah (Josh 15:27; Neh 11:26)
    "beth-shean;-beth-shan":  {"status": "names-only"},   # ISBE compound; covered under Beth-shean in Easton/Smith
    "beth-shemite":           {"status": "names-only"},   # demonym for Beth-shemesh; minor epithet
    "beth-zacharias":         {"status": "names-only"},   # battle site (1 Macc 6:32-33); apocryphal
    "bethasmoth":             {"status": "names-only"},   # returned exile town (1 Esd 5:18); apocryphal
    "bethbasi":               {"status": "names-only"},   # Maccabean stronghold (1 Macc 9:62); apocryphal
    "bethel-mount":           {"status": "names-only"},   # ISBE compound; mountain near Bethel; minor geographic
    "bethink":                {"status": "names-only"},   # KJV "come to oneself" (1 Kgs 8:47; 2 Chr 6:37); lexical
    "bethlehem-star-of":      {"status": "names-only"},   # Matt 2:2,7,9-10; covered under magi/nativity topics
    "bethsamos":              {"status": "names-only"},   # apocryphal figure/place
    "bethsura;-bethsuron":    {"status": "names-only"},   # ISBE compound; Beth-Zur (1 Macc 4:29); apocryphal
    "bethuel-1":              {"status": "names-only"},   # ISBE disambiguation; Rebekah's father (Gen 22:22-23)
    "bethuel-2":              {"status": "names-only"},   # ISBE disambiguation; town in Simeon (1 Chr 4:30)
    "bethulia":               {"status": "names-only"},   # fictional city in book of Judith; apocryphal
    "betimes":                {"status": "names-only"},   # KJV "early/diligently" (Job 8:5; Prov 13:24); lexical
    "betolion":               {"status": "names-only"},   # apocryphal figure/place (1 Esd 5:21)
    "betomesthaim;-betomasthaim": {"status": "names-only"},  # ISBE compound; apocryphal place
    "betray":                 {"status": "names-only"},   # lexical; Judas covered under Judas Iscariot
    "betrayers":              {"status": "names-only"},   # Acts 7:52; "betrayers and murderers"; lexical
    # The 400-year intertestamental period (Malachi to Matthew): Maccabean revolt (167–164 BC),
    # Hasmonean dynasty, Roman conquest (63 BC), rise of Pharisees/Sadducees/Essenes/Zealots,
    # development of synagogue, Diaspora; essential context for understanding why 1st-century
    # Judaism looked the way it did when Jesus arrived
    "between-the-testaments": {"status": "stub-needed"},
    "bewail":                 {"status": "names-only"},   # lexical
    "bewitch":                {"status": "names-only"},   # Gal 3:1; Acts 8:9 (Simon Magus); lexical
    "bewray;-bewrayer":       {"status": "names-only"},   # KJV "reveal/betray" (Isa 16:3; Matt 26:73); lexical
    "bezaanannim":            {"status": "names-only"},   # Josh 19:33; Judg 4:11; minor place
    "bezalel":                {"status": "names-only"},   # tabernacle craftsman (Exod 31:1-11); in Easton/Smith
    "bezeth":                 {"status": "names-only"},   # place (1 Macc 7:19); apocryphal
    "bezetha":                {"status": "names-only"},   # northern Jerusalem suburb; geographic note
    "biatas":                 {"status": "names-only"},   # apocryphal figure
    "bible-the":              {"status": "names-only"},   # "Scripture" concept covered under Word of God/canon
    "biblical-criticism":     {"status": "names-only"},   # ISBE scholarly; too specialized at score-5
    "biblical-discrepancies": {"status": "names-only"},   # ISBE apologetics; too specialized at score-5
    "biblical-theology":      {"status": "names-only"},   # ISBE scholarly discipline; too specialized at score-5
    "bid":                    {"status": "names-only"},   # lexical
    "bidden":                 {"status": "names-only"},   # lexical
    "bide":                   {"status": "names-only"},   # KJV "remain/wait"; lexical
    "bigthan;-bigthana":      {"status": "names-only"},   # ISBE compound; Esth 2:21; 6:2; minor figure
    "bikath-aven":            {"status": "names-only"},   # "plain of Aven" (Amos 1:5); minor place
    "bilgah;-bilgai":         {"status": "names-only"},   # ISBE compound; priestly figure; minor
    "bilhah-1":               {"status": "names-only"},   # ISBE disambiguation; Rachel's servant (Gen 30:3-8)
    "bilhah-2":               {"status": "names-only"},   # ISBE disambiguation; town in Simeon (1 Chr 4:29)
    "bilhan-3":               {"status": "names-only"},   # ISBE disambiguation; minor figure (1 Chr 7:10)
    "bill-of-divorcement":    {"status": "names-only"},   # Deut 24:1-4; Matt 19:7-9; covered under divorce
    "bill-bond-etc.":         {"status": "names-only"},   # Luke 16:6-7 debt ledger; lexical
    "billow":                 {"status": "names-only"},   # Ps 42:7; Job 9:8; lexical/poetic
    "bind;-bound":            {"status": "names-only"},   # ISBE compound; Matt 16:19 binding/loosing; lexical
    "bird-catcher":           {"status": "names-only"},   # Prov 6:5; Hos 9:8; cultural note
    "birds-of-abomination":   {"status": "names-only"},   # Lev 11:13-19; covered under clean/unclean animals
    "birds-of-prey":          {"status": "names-only"},   # Gen 15:11; Isa 46:11; names-only
    "birds-unclean":          {"status": "names-only"},   # Lev 11:13-19; same category as above
    "birth-new":              {"status": "names-only"},   # regeneration (John 3:3-8); covered under regeneration
    # The Virgin Birth: Isaiah's sign "a virgin shall conceive" (Isa 7:14 almah/parthenos);
    # Matthew's fulfillment (Matt 1:18-25); Gabriel's announcement to Mary (Luke 1:26-38);
    # Jesus conceived by Holy Spirit, not human father; essential to incarnation doctrine;
    # affirmed in Apostles' Creed; debate over Isaiah's almah vs parthenos
    "birth-virgin":           {"status": "stub-needed"},
    "birth-stool":            {"status": "names-only"},   # Exod 1:16 Hebrew midwifery term; lexical
    "birzaith":               {"status": "names-only"},   # 1 Chr 7:31; minor name
    "bishoprick":             {"status": "names-only"},   # KJV "office of overseer" (Acts 1:20); lexical
    "bishops-bible":          {"status": "names-only"},   # 16th-century English Bible; too specialized at score-5
    "bit-and-bridle":         {"status": "names-only"},   # Ps 32:9; Prov 26:3; cultural reference
    "bitter-water":           {"status": "names-only"},   # Num 5:18-27 jealousy ordeal; Exod 15:23 Marah; brief
    "bitter;-bitterness":     {"status": "names-only"},   # ISBE compound; lexical
    "bitterness":             {"status": "names-only"},   # Eph 4:31; "root of bitterness" (Heb 12:15); lexical
    "bitterness-water-of":    {"status": "names-only"},   # Num 5; same as bitter-water; lexical
    "biziothiah":             {"status": "names-only"},   # Josh 15:28; minor Judahite town
    "blackness":              {"status": "names-only"},   # Heb 12:18; Rev 6:12; lexical
    "blast":                  {"status": "names-only"},   # Isa 37:7; lexical; "blast" from God
    "blast;-blasting":        {"status": "names-only"},   # ISBE compound; Deut 28:22 agricultural blight; lexical
    "blaze":                  {"status": "names-only"},   # lexical
    "blessed":                {"status": "names-only"},   # Matt 5:3-12 Beatitudes context; lexical
    "blessedness":            {"status": "names-only"},   # Rom 4:6-9; Ps 1:1; lexical
    "blessing":               {"status": "names-only"},   # covered under "blessing" in Easton/Smith
    "blessing-cup-of":        {"status": "names-only"},   # 1 Cor 10:16 Lord's Supper; covered under that topic
    "blessing-valley-of":     {"status": "names-only"},   # 2 Chr 20:26; minor place reference
    "blindfold":              {"status": "names-only"},   # Luke 22:64; lexical
    "blinding":               {"status": "names-only"},   # lexical
    "blindness-judicial":     {"status": "names-only"},   # John 12:40; Isa 6:10; covered under hardening/reprobation
    "blood-and-water":        {"status": "names-only"},   # John 19:34; covered under crucifixion/atonement
    "blood-avenger-of":       {"status": "names-only"},   # Num 35; covered under cities of refuge
    "blood-issue-of":         {"status": "names-only"},   # woman with hemorrhage (Matt 9:20; Mark 5:25)
    "blood-revenge":          {"status": "names-only"},   # avenger of blood concept; covered under cities of refuge
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
    print(f'BPG Curation C30: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
