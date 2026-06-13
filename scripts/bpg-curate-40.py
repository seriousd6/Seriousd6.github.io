"""
BPG Curation — Batch C40: eleven-the → ephraim-forest-of (gaps 3899–3998)
Gaps reviewed: 100 (score-5 isbe-scholarly E entries — Eli-/El- names, apocryphal, minor places)

Notable stub: Elohim — most common OT divine name (~2,570 occurrences); plural form with singular
meaning; foundational Hebrew literacy concept; not in Easton/Smith (hence a gap).
1 stub-needed; 0 redirects; 99 names-only.

Script: scripts/bpg-curate-40.py
Run: python3 scripts/bpg-curate-40.py  (from project root)
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
    "eleven-the":             {"status": "names-only"},   # "the Eleven" disciples (Mark 16:14; Luke 24:9,33)
    "eleven;-stars":          {"status": "names-only"},   # ISBE compound; Joseph's dream (Gen 37:9)
    "eliada;-eliadah":        {"status": "names-only"},   # ISBE compound; David's son (2 Sam 5:16)
    "eliadas":                {"status": "names-only"},   # apocryphal figure
    "eliadun":                {"status": "names-only"},   # apocryphal figure
    "eliali":                 {"status": "names-only"},   # apocryphal figure (1 Esd 9:27)
    "eliaonias":              {"status": "names-only"},   # apocryphal figure
    "eliasib":                {"status": "names-only"},   # variant of Eliashib; minor OT figure
    "eliasibus":              {"status": "names-only"},   # apocryphal figure
    "eliasimus":              {"status": "names-only"},   # apocryphal figure
    "eliasis":                {"status": "names-only"},   # apocryphal figure
    "eliehoenai":             {"status": "names-only"},   # various OT figures (1 Chr 3:23-24; Ezra 10:22)
    "elihaba":                {"status": "names-only"},   # David's mighty man (2 Sam 23:32)
    "elihu-1":                {"status": "names-only"},   # ISBE disambiguation; Job's friend (Job 32-37); in Easton
    "elihu-2":                {"status": "names-only"},   # ISBE disambiguation; other Elihu figures
    "elionas":                {"status": "names-only"},   # apocryphal figure (1 Esd 9:22)
    "eliphalat":              {"status": "names-only"},   # variant of Eliphelet; minor figure
    "eliphaz-1":              {"status": "names-only"},   # ISBE disambiguation; Job's friend; covered in Easton
    "eliphaz-2":              {"status": "names-only"},   # ISBE disambiguation; Esau's son (Gen 36:4-16)
    "eliphelehu":             {"status": "names-only"},   # Levite musician (1 Chr 15:18,21)
    "elisimus":               {"status": "names-only"},   # apocryphal figure
    "eliu":                   {"status": "names-only"},   # apocryphal figure
    "elkiah":                 {"status": "names-only"},   # apocryphal figure (Judith 8:1)
    "elo-beth-hanan":         {"status": "names-only"},   # 1 Kgs 4:9; minor place
    # Elohim: the most common OT name for God (~2,570 occurrences); "In the beginning God [Elohim]
    # created" (Gen 1:1); generic Semitic word for deity; plural form (‑im) with singular verbs
    # when referring to Israel's God; used by both Yahwist and Elohist sources; encompasses
    # discussions of divine plurality, unity, and early Trinitarian hints; foundational for
    # Hebrew literacy and OT theology; not in Easton or Smith (hence this gap)
    "elohim":                 {"status": "stub-needed"},
    "eloi":                   {"status": "names-only"},   # Aramaic "my God" (Mark 15:34); brief
    "eloi;-eloi;-lama;-sabachtha;-eli;-eli;-lama-sabachthani": {"status": "names-only"},  # Matt 27:46; covered under crucifixion/atonement
    "elon-1":                 {"status": "names-only"},   # ISBE disambiguation; judge (Judg 12:11-12)
    "elon-2":                 {"status": "names-only"},   # ISBE disambiguation; Zebulunite clan/town
    "elonites":               {"status": "names-only"},   # demonym for Elon; brief
    "eloquent":               {"status": "names-only"},   # Exod 4:10; Acts 18:24 Apollos; lexical
    "elpelet":                {"status": "names-only"},   # variant of Elpaal; minor figure (1 Chr 14:5)
    "elteke;-eltekeh":        {"status": "names-only"},   # ISBE compound; Josh 19:44; Levite city
    "eltekon":                {"status": "names-only"},   # Josh 15:59; minor place
    "elymaeans":              {"status": "names-only"},   # people from Elymais; apocryphal context
    "elymais":                {"status": "names-only"},   # region in Persia (1 Macc 6:1; 2 Macc 9:2); apocryphal
    "elyon":                  {"status": "names-only"},   # El Elyon "Most High" (Gen 14:18); covered under God/names
    "emadabun":               {"status": "names-only"},   # apocryphal figure (1 Esd 5:58)
    "ematheis":               {"status": "names-only"},   # apocryphal figure (1 Esd 9:27)
    "embrace":                {"status": "names-only"},   # lexical; Gen 29:13; names-only
    "embroidery":             {"status": "names-only"},   # Exod 26:36; 28:39 tabernacle; cultural
    "emek-keziz":             {"status": "names-only"},   # Josh 18:21; minor Benjaminite town
    "emim":                   {"status": "names-only"},   # Gen 14:5; Deut 2:10-11; ancient giant people in Moab
    "eminent":                {"status": "names-only"},   # KJV "elevated" (Ezek 16:24,31); lexical
    "emmer":                  {"status": "names-only"},   # apocryphal figure (1 Esd 5:24)
    "emmeruth":               {"status": "names-only"},   # apocryphal figure
    "emperor":                {"status": "names-only"},   # 1 Pet 2:13-17; Rom 13:1-7; lexical
    "empty;-emptier":         {"status": "names-only"},   # ISBE compound; KJV; lexical
    "emulation":              {"status": "names-only"},   # Rom 11:14 KJV; Gal 5:20; lexical
    "en-dor-witch-of":        {"status": "names-only"},   # 1 Sam 28:7-25; covered under Endor/divination
    "en-gaddi":               {"status": "names-only"},   # variant of Engedi; names-only
    "enable":                 {"status": "names-only"},   # lexical
    "enaim":                  {"status": "names-only"},   # Gen 38:14,21; minor place near Timnah
    "enasibus":               {"status": "names-only"},   # apocryphal figure (1 Esd 9:34)
    "encampment-by-the-red-sea": {"status": "names-only"},  # Num 33:10-11; wilderness itinerary
    "enchantment":            {"status": "names-only"},   # Num 23:23; covered under divination/magic
    "end-of-the-world":       {"status": "names-only"},   # eschatology; covered under last things in Easton
    "endamage":               {"status": "names-only"},   # KJV "damage" (Ezra 4:13); lexical
    "endeavor":               {"status": "names-only"},   # KJV "strive"; lexical
    "endirons":               {"status": "names-only"},   # andirons; cultural; brief
    "endless":                {"status": "names-only"},   # 1 Tim 1:4; Heb 7:16; lexical
    "endow;-endue":           {"status": "names-only"},   # ISBE compound; KJV; lexical
    "ends-of-the-earth":      {"status": "names-only"},   # Isa 45:22; Ps 2:8; Acts 1:8; poetic phrase
    "endure":                 {"status": "names-only"},   # Matt 10:22; Heb 12:1-2; lexical
    "enemessar":              {"status": "names-only"},   # Tobit's Assyrian king = Shalmaneser; apocryphal
    "enemy":                  {"status": "names-only"},   # Matt 5:43-44 "love your enemies"; lexical
    "eneneus":                {"status": "names-only"},   # apocryphal figure (1 Esd 8:43)
    "enflame":                {"status": "names-only"},   # Isa 57:5 KJV; lexical
    "engage":                 {"status": "names-only"},   # Jer 30:21 KJV; lexical
    "english-versions":       {"status": "names-only"},   # ISBE scholarly; too specialized at score-5
    "engraft":                {"status": "names-only"},   # Jas 1:21 KJV "engrafted word"; lexical
    "engraving":              {"status": "names-only"},   # Exod 28:11; Zech 3:9; cultural; brief
    "enigma":                 {"status": "names-only"},   # 1 Cor 13:12; Judg 14:12; lexical
    "enjoin":                 {"status": "names-only"},   # KJV "command"; lexical
    "enlarge;-enlargement":   {"status": "names-only"},   # ISBE compound; Ps 119:32; Gen 9:27; lexical
    "enlighten":              {"status": "names-only"},   # Ps 18:28; Eph 1:18; lexical
    "ennatan":                {"status": "names-only"},   # apocryphal figure (1 Esd 8:44)
    "enoch-city":             {"status": "names-only"},   # ISBE compound; Gen 4:17; names-only
    "enoch-book-of":          {"status": "names-only"},   # extracanonical; too specialized at score-5
    "enoch-ethiopic-book-of": {"status": "names-only"},   # extracanonical; too specialized
    "enoch-slavonic-book-of": {"status": "names-only"},   # extracanonical; too specialized
    "enoch;-the-book-of-the-secrets-of": {"status": "names-only"},  # extracanonical; too specialized
    "enormity":               {"status": "names-only"},   # lexical
    "enos;-enosh":            {"status": "names-only"},   # ISBE compound; Gen 4:26; 5:6-11; covered in Easton
    "enquire":                {"status": "names-only"},   # lexical
    "enrolment":              {"status": "names-only"},   # Luke 2:1-5 census; covered under census
    "ensample":               {"status": "names-only"},   # KJV archaic "example" (1 Cor 10:11); lexical
    "ensue":                  {"status": "names-only"},   # KJV "pursue" (1 Pet 3:11); lexical
    "entangle":               {"status": "names-only"},   # Matt 22:15; Gal 5:1; lexical
    "entreat":                {"status": "names-only"},   # KJV "treat/beg"; lexical
    "envy":                   {"status": "names-only"},   # Gal 5:21; Prov 14:30; covered under envy in Easton
    "ephah-1":                {"status": "names-only"},   # ISBE disambiguation; unit of dry measure; in Easton
    "ephah-2":                {"status": "names-only"},   # ISBE disambiguation; Midianite clan (Gen 25:4)
    "ephesian;-ephesians":    {"status": "names-only"},   # ISBE compound; residents of Ephesus
    "ephesians-epistle-to-the": {"status": "names-only"}, # ISBE compound; Ephesians as book; covered in Easton
    "ephod-1":                {"status": "names-only"},   # ISBE disambiguation; priestly vestment; covered in Easton
    "ephod-2":                {"status": "names-only"},   # ISBE disambiguation; Manassite father (Num 34:23)
    "ephraim-1":              {"status": "names-only"},   # ISBE disambiguation; Joseph's son; covered in Easton
    "ephraim-2":              {"status": "names-only"},   # ISBE disambiguation; place near Baal-hazor
    "ephraim-forest-of":      {"status": "names-only"},   # 2 Sam 18:6-17 where Absalom died; minor place
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
    print(f'BPG Curation C40: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
