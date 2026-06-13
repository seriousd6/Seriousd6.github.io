"""
BPG Curation — Batch C52: keras → law-judicial (gaps 5299–5398)
Gaps reviewed: 100 (score-5 isbe-scholarly K–L entries)

K-range names/places and early L entries. No stubs: significant concepts
(kingdom of God, lamb of God, law) are all covered in Easton. Eleven
redirects for compound/variant ISBE forms (kidron, kiriath variants,
kohath, koheleth, lake-of-fire → fire-lake-of, etc.).
0 stub-needed; 11 redirects; 89 names-only.

Script: scripts/bpg-curate-52.py
Run: python3 scripts/bpg-curate-52.py  (from project root)
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
    "keras":                  {"status": "names-only"},   # uncertain; possibly apocryphal
    "kerioth-hezron":         {"status": "names-only"},   # Judah town (Josh 15:25); minor geographic
    "kernel":                 {"status": "names-only"},   # "kernel of grain" (Num 6:4); lexical
    "kesil":                  {"status": "names-only"},   # Hebrew constellation (Orion/Scorpio); astronomical
    "ketab":                  {"status": "names-only"},   # KJV "writing/document" (Dan 10:21); lexical
    "keys-power-of-the":      {"status": "names-only"},   # "keys of the kingdom" (Matt 16:19); covered under "Keys" in Easton
    "keziah":                 {"status": "names-only"},   # Job's daughter (Job 42:14); minor name
    "khan":                   {"status": "names-only"},   # caravansary/inn; cultural
    "kick":                   {"status": "names-only"},   # "kick against the goads" (Acts 9:5; 26:14); lexical
    "kidnapping-manstealing": {"status": "names-only"},   # Exod 21:16; Deut 24:7; covered under "Law" in Easton
    "kidneys":                {"status": "names-only"},   # anatomical; Lev 3:4 sacrificial context; brief
    # ISBE compound; redirect to canonical Easton "Kidron"
    "kidron-the-brook":       {"status": "redirect-only", "redirect_to": "kidron"},
    "kilan":                  {"status": "names-only"},   # uncertain; possibly apocryphal
    "kimah":                  {"status": "names-only"},   # Pleiades (Job 9:9; Amos 5:8); astronomical
    "kin":                    {"status": "names-only"},   # lexical
    "kin-next-of":            {"status": "names-only"},   # covered under "Goel" and "Kinsman" in Easton
    "kindness":               {"status": "names-only"},   # virtue; covered in Easton
    "kindred":                {"status": "names-only"},   # lexical
    "king-of-the-jews":       {"status": "names-only"},   # title on cross (Matt 27:37); covered under "Jesus Christ"
    "kings-garden":           {"status": "names-only"},   # Jerusalem garden (2 Kings 25:4; Neh 3:15); geographic
    "kings-mother":           {"status": "names-only"},   # queen mother office; covered under "Queens" in Easton
    "kings-pool":             {"status": "names-only"},   # Neh 2:14; Jerusalem geographic
    "kings-vale":             {"status": "names-only"},   # Gen 14:17; 2 Sam 18:18; geographic
    "king-christ-as":         {"status": "names-only"},   # Christ as king; covered under "Jesus Christ" in Easton
    "king;-kingdom":          {"status": "names-only"},   # lexical/concept; covered broadly in Easton
    "kingdom-of-god-of-heaven-the": {"status": "names-only"},  # covered under "Kingdom of God" in Easton
    "kingdom-of-israel":      {"status": "names-only"},   # Northern Kingdom; covered under "Israel" in Easton
    "kingdom-of-judah":       {"status": "names-only"},   # Southern Kingdom; covered under "Judah" in Easton
    "kings-sepulchres":       {"status": "names-only"},   # Jerusalem tombs (2 Chr 32:33); geographic
    # ISBE article on 1-2 Kings; redirect to canonical Easton "Kings" (books)
    "kings-books-of":         {"status": "redirect-only", "redirect_to": "kings"},
    "kinsfolk":               {"status": "names-only"},   # lexical
    "kinsman;-kinswoman":     {"status": "names-only"},   # covered under "Kinsman" in Easton
    "kirama":                 {"status": "names-only"},   # apocryphal name
    "kiriath":                {"status": "names-only"},   # prefix "city of"; lexical/geographic
    # Ancient name for Hebron (Gen 23:2); redirect to canonical Easton "Hebron"
    "kiriath-arba":           {"status": "redirect-only", "redirect_to": "hebron"},
    # Variant of Kiriath-jearim (Ezra 2:25); redirect to canonical entry
    "kiriath-arim":           {"status": "redirect-only", "redirect_to": "kiriath-jearim"},
    # Variant name for Kiriath-jearim (Josh 15:60; 18:14); redirect
    "kiriath-baal":           {"status": "redirect-only", "redirect_to": "kiriath-jearim"},
    "kiriath-huzoth":         {"status": "names-only"},   # Balaam's location (Num 22:39); brief geographic
    "kiriath-jearim":         {"status": "names-only"},   # where ark rested (1 Sam 7:1-2); covered in Easton as "Kirjath-jearim"
    "kiriath-sannah":         {"status": "names-only"},   # variant of Debir (Josh 15:49); geographic
    "kiriath-sepher":         {"status": "names-only"},   # ancient name of Debir; covered under "Debir" in Easton
    "kiseus":                 {"status": "names-only"},   # apocryphal name
    "kislev":                 {"status": "names-only"},   # Hebrew month (Neh 1:1; Zech 7:1); calendar
    "kneading":               {"status": "names-only"},   # "kneading trough" (Exod 8:3); cultural/lexical
    "knee;-kneel":            {"status": "names-only"},   # cultural/lexical; covered briefly in Easton
    "know;-knowledge":        {"status": "names-only"},   # covered under "Knowledge" in Easton
    # ISBE compound; redirect to canonical Easton "Kohath"
    "kohath;-kohathites":     {"status": "redirect-only", "redirect_to": "kohath"},
    # Hebrew name for Ecclesiastes; redirect to canonical article
    "koheleth":               {"status": "redirect-only", "redirect_to": "ecclesiastes"},
    "konae":                  {"status": "names-only"},   # apocryphal name
    "kor":                    {"status": "names-only"},   # unit of measure; covered under "Weights and Measures" in Easton
    # ISBE compound entry; redirect to canonical Easton "Korah"
    "korahites;-sons-of-korah": {"status": "redirect-only", "redirect_to": "korah"},
    # Variant spelling; redirect to canonical Easton "Korah"
    "korathites":             {"status": "redirect-only", "redirect_to": "korah"},
    "labor":                  {"status": "names-only"},   # lexical; covered under "Work" in Easton
    "laccunus":               {"status": "names-only"},   # apocryphal name
    "lace":                   {"status": "names-only"},   # tabernacle cord (Exod 28:28); cultural/lexical
    "lack":                   {"status": "names-only"},   # lexical
    "lacunus":                {"status": "names-only"},   # apocryphal name (variant of Laccunus)
    "lad":                    {"status": "names-only"},   # lexical
    "ladan":                  {"status": "names-only"},   # Levite name (1 Chr 23:7-9; 26:21); variant of Laadan; minor
    "ladanum":                {"status": "names-only"},   # aromatic resin (Gen 37:25; 43:11); natural history
    "ladder-of-tyre":         {"status": "names-only"},   # coastal landmark (1 Macc 11:59); geographic/historical
    "lade;-lading":           {"status": "names-only"},   # KJV "load/cargo" (1 Kings 12:11; Acts 27:10); lexical
    "lady":                   {"status": "names-only"},   # "elect lady" (2 John 1:1); brief
    "lahmas":                 {"status": "names-only"},   # Judah village (Josh 15:40); minor geographic
    "laishah":                {"status": "names-only"},   # Benjamin village (Isa 10:30); minor geographic
    "lake":                   {"status": "names-only"},   # lexical
    # ISBE compound; this concept is covered under stub "fire-lake-of" created in C42
    "lake-of-fire":           {"status": "redirect-only", "redirect_to": "fire-lake-of"},
    # Alternate name for Sea of Galilee (Luke 5:1); redirect to canonical article
    "lake-of-gennesaret":     {"status": "redirect-only", "redirect_to": "galilee-sea-of"},
    "lakkum":                 {"status": "names-only"},   # Naphtali town (Josh 19:33); minor geographic
    "lamb-of-god":            {"status": "names-only"},   # covered under "Lamb" and "Jesus Christ" in Easton
    "lame":                   {"status": "names-only"},   # lexical; physical condition
    "lamedh":                 {"status": "names-only"},   # Hebrew letter; brief
    "lament":                 {"status": "names-only"},   # lexical
    "lamp;-lampstand":        {"status": "names-only"},   # covered under "Candlestick" in Easton
    "lampsacus":              {"status": "names-only"},   # city on Hellespont (1 Macc 15:23); minor geographic
    "lance;-lancer;-lancet":  {"status": "names-only"},   # KJV "spear/lance" (1 Kings 18:28; Jer 50:42); lexical
    "land":                   {"status": "names-only"},   # lexical
    "land-laws":              {"status": "names-only"},   # OT land tenure (Lev 25; Deut); covered under "Law" in Easton
    "land-crocodile":         {"status": "names-only"},   # Lev 11:29-30 (KJV); natural history/zoological
    "lane":                   {"status": "names-only"},   # lexical; Luke 14:21
    "language-of-the-new-testament": {"status": "names-only"},  # Greek Koine; covered under "Greek Language" in Easton
    "languages-of-the-old-testament": {"status": "names-only"},  # Hebrew/Aramaic; covered under "Hebrew Language" in Easton
    "laodiceans-epistle-to-the": {"status": "names-only"},  # apocryphal epistle attributed to Paul; extracanonical
    "lap":                    {"status": "names-only"},   # lexical; Judg 7:5-6
    "lappidoth":              {"status": "names-only"},   # Deborah's husband (Judg 4:4); minor name
    "lasciviousness":         {"status": "names-only"},   # KJV "lewdness" (Gal 5:19); covered in Easton
    "lassharon":              {"status": "names-only"},   # Canaan city (Josh 12:18); minor geographic
    "last-day":               {"status": "names-only"},   # "the last day" (John 6:39-40,44,54); covered under eschatology
    "last-days":              {"status": "names-only"},   # "in the last days" (2 Tim 3:1; Heb 1:2); covered in Easton
    "last-time-times":        {"status": "names-only"},   # "last time" (1 Pet 1:5; 1 John 2:18); eschatological; covered
    "lasthenes":              {"status": "names-only"},   # Seleucid figure (1 Macc 11:31-32); apocryphal
    "latin-version-the-old":  {"status": "names-only"},   # Old Latin Bible version; scholarly; too specialized
    "latter-days":            {"status": "names-only"},   # OT prophetic term; covered under "Day of the Lord"
    "laud":                   {"status": "names-only"},   # KJV "praise" (Rom 15:11); lexical
    "laughing-stock":         {"status": "names-only"},   # KJV "object of derision" (Job 12:4; Lam 3:14); lexical
    "laughter":               {"status": "names-only"},   # lexical
    "launch":                 {"status": "names-only"},   # lexical; Acts 27:2
    "law-in-the-new-testament": {"status": "names-only"},  # ISBE article; covered under "Law" in Easton
    "law-in-the-old-testament": {"status": "names-only"},  # ISBE article; covered under "Law" in Easton
    "law-judicial":           {"status": "names-only"},   # judicial law distinctions; covered under "Law" in Easton
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
    print(f'BPG Curation C52: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
