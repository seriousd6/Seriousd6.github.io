"""
BPG Curation — Batch C10: lantern → principality (gaps 901–1000)
Gaps reviewed: 100 (all score-25 smith-scholarly entries, L–P range)

Transition from cultural/institutional smith entries to NT topics and theology.
Key stubs: Levites, Leper/Leprosy, Lion (of Judah), Maccabees (books),
Meat-offering (minchah), Moneychangers (temple cleansing), Mourning,
Nicolaitans, Mount of Olives, Old Testament, Pestilence, Phoebe, Phylactery,
Philip the Evangelist, Poetry (Hebrew), Polygamy, Principality.
Eight Greek/variant-form redirects: Libanus, Manasses, Mathusala, Nabuchodonosor,
Odollam, Michah, Moon-new → new-moon, Olivet → olives-mount-of.

Script: scripts/bpg-curate-10.py
Run: python3 scripts/bpg-curate-10.py  (from project root)
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
    # ── L entries ────────────────────────────────────────────────────────────
    "lantern":          {"status": "names-only"},   # John 18:3; general object reference
    "lead":             {"status": "names-only"},   # metal used in biblical Israel; general
    "leaf-leaves":      {"status": "names-only"},   # fig leaf (Gen 3:7); general nature reference
    "lebana":           {"status": "names-only"},   # temple servant family (Neh 7:48 variant)
    "lecah":            {"status": "names-only"},   # Judah descendant (1 Chr 4:21)
    "leeks":            {"status": "names-only"},   # food longed for in desert (Num 11:5)
    "lentils":          {"status": "names-only"},   # Esau's birthright stew (Gen 25:34); cultural
    # Mosaic purity laws, Naaman's healing (2 Kgs 5), Jesus healing ten lepers (Luke 17:11-19)
    "leper-leprosy":    {"status": "stub-needed"},
    # The tribe set apart for temple service; Levitical cities, priesthood, tithes
    "levites":          {"status": "stub-needed"},
    # Greek/Latin form of Lebanon (used in apocrypha and LXX)
    "libanus":          {"status": "redirect-only", "redirect_to": "lebanon"},
    # Synagogue of the Freedmen (Acts 6:9); freed slaves from Rome who opposed Stephen
    "libertines":       {"status": "stub-needed"},
    "likhi":            {"status": "names-only"},   # Manasseh descendant (1 Chr 7:19)
    # Lion of Judah; Daniel's den (Dan 6); "like a roaring lion" (1 Pet 5:8); Rev 5:5
    "lion":             {"status": "stub-needed"},
    "lubim":            {"status": "names-only"},   # Libyan mercenaries in Shishak's army (2 Chr 12:3)

    # ── M entries ────────────────────────────────────────────────────────────
    "maacah":           {"status": "names-only"},   # multiple figures: David's wife, small kingdom, etc.
    # 1–2 Maccabees: deuterocanonical books covering Hasmonean revolt; critical for NT context
    "maccabees-books-of": {"status": "stub-needed"},
    "magadan":          {"status": "names-only"},   # place after feeding 4000 (Matt 15:39); obscure location
    "mahli":            {"status": "names-only"},   # two Levites (Exod 6:19; 1 Chr 6:47)
    "makaz":            {"status": "names-only"},   # Solomon's administrative district (1 Kgs 4:9)
    "mamaias":          {"status": "names-only"},   # apocryphal figure; not in canonical texts
    "manahath":         {"status": "names-only"},   # Edomite chief (Gen 36:23) / Benjaminite exile site
    # Greek form of Manasseh used in NT genealogy (Matt 1:10; Rev 7:6)
    "manasses":         {"status": "redirect-only", "redirect_to": "manasseh"},
    # Greek form of Methuselah used in NT genealogy (Luke 3:37)
    "mathusala":        {"status": "redirect-only", "redirect_to": "methuselah"},
    "mattathah":        {"status": "names-only"},   # post-exile man with foreign wife (Ezra 10:33)
    "mattenai":         {"status": "names-only"},   # three post-exile figures (Neh 12:19; Ezra 10:33,37)
    "mauzzim":          {"status": "names-only"},   # Dan 11:38 "god of fortresses"; epithet, not proper noun
    "meat":             {"status": "names-only"},   # KJV generic for food; translation artifact
    # KJV for the grain/cereal offering (מִנְחָה, minchah); Lev 2; core sacrificial ritual
    "meat-offering":    {"status": "stub-needed"},
    "medicine":         {"status": "names-only"},   # healing in ancient Israel; general cultural reference
    "mehunim":          {"status": "names-only"},   # temple servant family (Ezra 2:50); Meunim people
    "melicu":           {"status": "names-only"},   # priest (Neh 12:14 variant of Malluchi)
    "menna":            {"status": "names-only"},   # NT genealogy (Luke 3:31)
    "meonothai":        {"status": "names-only"},   # Judah descendant (1 Chr 4:14)
    "meshillemith":     {"status": "names-only"},   # priest (1 Chr 9:12 variant)
    # Metals in ancient Israel: gold, silver, bronze, iron; Bezalel's craft; Dan 2 statue
    "metals":           {"status": "stub-needed"},
    # Variant of Micah; multiple prophets and persons (Judg 17; Mic 1:1; Jer 26:18)
    "michah":           {"status": "redirect-only", "redirect_to": "micah"},
    "mikneiah":         {"status": "names-only"},   # Levite musician (1 Chr 15:18,21)
    "mirror":           {"status": "names-only"},   # polished bronze mirrors (Exod 38:8; 2 Cor 3:18)
    "mispereth":        {"status": "names-only"},   # leader of returning exiles (Neh 7:7 variant of Mizpar)
    "moadiah":          {"status": "names-only"},   # priest (Neh 12:17)
    # Hometown of the Maccabees; Mattathias's revolt began here (1 Macc 2:1; 13:25)
    "modin":            {"status": "stub-needed"},
    "moli":             {"status": "names-only"},   # Merarite Levite, variant of Mahli (1 Chr 23:23)
    # Jesus drove out moneychangers (Matt 21:12; John 2:14-16); fulfilled Jer 7:11
    "moneychangers":    {"status": "stub-needed"},
    # Duplicate/variant entry; redirect to the canonical new-moon article
    "moon-new":         {"status": "redirect-only", "redirect_to": "new-moon"},
    "mother":           {"status": "names-only"},   # general reference; covered under family/household
    "mount-mountain":   {"status": "names-only"},   # general reference; individual mountains have articles
    # Mourning rites in ancient Israel: sackcloth, ashes, tearing garments, professional mourners
    "mourning":         {"status": "stub-needed"},

    # ── N entries ────────────────────────────────────────────────────────────
    # Greek/apocryphal form of Nebuchadnezzar (Judith 1:1; 1 Macc etc.)
    "nabuchodonosor":   {"status": "redirect-only", "redirect_to": "nebuchadnezzar"},
    "naggai":           {"status": "names-only"},   # NT genealogy (Luke 3:25)
    # Spikenard ointment used to anoint Jesus at Bethany (Mark 14:3; John 12:3)
    "nard":             {"status": "stub-needed"},
    "nehelamite-the":   {"status": "names-only"},   # epithet for false prophet Shemaiah (Jer 29:24)
    # Monthly new moon festival (Num 28:11-15; Isa 66:23; Col 2:16 "new moon" in Sabbath list)
    "new-moon":         {"status": "stub-needed"},
    # Feast of Trumpets / Rosh Hashanah (Lev 23:23-25; Num 29:1); beginning of civil new year
    "new-year":         {"status": "stub-needed"},
    # Heretical group condemned in Revelation (Rev 2:6,15); doctrine unknown; perhaps licentiousness
    "nicolaitans":      {"status": "stub-needed"},
    "night":            {"status": "names-only"},   # general reference; night in biblical narrative
    "nimrim":           {"status": "names-only"},   # waters of Nimrim (Isa 15:6; Jer 48:34)
    "ninevites":        {"status": "names-only"},   # demonym for Nineveh; topic covered under "nineveh"
    # No-Amon = ancient Thebes, Egypt (Nah 3:8); Nahum's comparison with Nineveh
    "no-amon":          {"status": "stub-needed"},
    "nohah":            {"status": "names-only"},   # Benjamin's son (1 Chr 8:2)
    "number":           {"status": "names-only"},   # general reference; specific numbers (7, 12, 40) have articles

    # ── O entries ────────────────────────────────────────────────────────────
    "oblation":         {"status": "names-only"},   # KJV cereal/gift offering; covered under "offerings"
    # Greek form of Adullam (1 Macc 12:38)
    "odollam":          {"status": "redirect-only", "redirect_to": "adullam"},
    "officer":          {"status": "names-only"},   # general administrative/military title
    "oil-tree":         {"status": "names-only"},   # oleaster/wild olive (Isa 41:19; 1 Kgs 6:23)
    # The Hebrew scriptures as a canonical collection; background for NT interpretation
    "old-testament":    {"status": "stub-needed"},
    # Site of Gethsemane, Olivet Discourse (Matt 24), Triumphal Entry, Ascension (Acts 1:12)
    "olives-mount-of":  {"status": "stub-needed"},
    # Variant name for Mount of Olives; redirect to canonical slug
    "olivet":           {"status": "redirect-only", "redirect_to": "olives-mount-of"},
    "onias":            {"status": "names-only"},   # high priest Onias III (2 Macc 3:1); apocryphal
    "orchard":          {"status": "names-only"},   # gardens/orchards; general reference

    # ── P entries ────────────────────────────────────────────────────────────
    # Wilderness of Paran: Israel's 38-year camp (Num 10:12; 12:16; 13:3); Ishmael settled here
    "paran-elparan":    {"status": "stub-needed"},
    "parlor":           {"status": "names-only"},   # KJV "upper room/inner chamber" (Judg 3:20); translation
    "pathrusim":        {"status": "names-only"},   # people of Upper Egypt/Pathros (Gen 10:14)
    "pelican":          {"status": "names-only"},   # bird in clean/unclean lists (Lev 11:18)
    "pen":              {"status": "names-only"},   # writing instruments; general reference
    "perezuzza":        {"status": "names-only"},   # place where Uzzah died (2 Sam 6:8); single-event site
    "persepolis":       {"status": "names-only"},   # Persian capital; apocryphal Antiochus incident (2 Macc 9:2)
    # Divine plague/pestilence (דֶּבֶר dever); judgment in Jer 14:12; Ezek 6:11; Rev 18:8
    "pestilence":       {"status": "stub-needed"},
    # Three: (1) found Moses (Exod 2:5-10), (2) Solomon's wife (1 Kgs 3:1; 9:24), (3) Mered's wife
    "pharaohs-daughter": {"status": "stub-needed"},
    "pharosh":          {"status": "names-only"},   # returned-exile family (Ezra 2:3 variant of Parosh)
    "phaselis":         {"status": "names-only"},   # Lycian city (1 Macc 15:23); apocryphal location
    # One of the seven deacons (Acts 6:5); evangelized Samaria and baptized Ethiopian eunuch (Acts 8)
    "philip-the-evangelist": {"status": "stub-needed"},
    # "Hollow and deceptive philosophy" (Col 2:8); Greek wisdom vs. cross-centered revelation
    "philosophy":       {"status": "stub-needed"},
    # Deaconess of Cenchreae (Rom 16:1-2); Paul's letter-bearer; key witness for women in NT church
    "phoebe":           {"status": "stub-needed"},
    "phuvah":           {"status": "names-only"},   # Issachar's son, variant of Puah (Gen 46:13)
    # Tefillin: leather boxes with scripture texts (Exod 13:9-16; Deut 6:8; Matt 23:5)
    "phylactery":       {"status": "stub-needed"},
    "picture":          {"status": "names-only"},   # KJV "pictures" (Num 33:52; Prov 25:11); general
    "piece-of-gold":    {"status": "names-only"},   # KJV monetary unit; translation artifact
    # 30 pieces of silver: Zechariah's prophecy (Zech 11:12-13) fulfilled in Judas (Matt 26:15; 27:3-10)
    "piece-of-silver":  {"status": "stub-needed"},
    "pildash":          {"status": "names-only"},   # Nahor's son (Gen 22:22)
    "pileha":           {"status": "names-only"},   # covenant signer (Neh 10:24)
    "pillar-plain-of-the": {"status": "names-only"}, # near Shechem (Judg 9:6 KJV); single reference
    # Hebrew poetry: parallelism, acrostic (Ps 119), lament genre, wisdom forms; essential for Psalms/Prophets
    "poetry-hebrew":    {"status": "stub-needed"},
    # Castor and Pollux (Dioscuri); figurehead of Alexandrian ship that carried Paul (Acts 28:11)
    "pollux":           {"status": "stub-needed"},
    # Biblical polygamy in patriarchs, David, Solomon; NT move to monogamy (1 Tim 3:2; Matt 19:5)
    "polygamy":         {"status": "stub-needed"},
    "pond":             {"status": "names-only"},   # pools/ponds in ancient Israel; general
    "porch":            {"status": "names-only"},   # Solomon's Porch (John 10:23); general reference
    "pot":              {"status": "names-only"},   # cooking vessels; general reference
    "president":        {"status": "names-only"},   # Persian administrative title (Dan 6:2)
    # ἀρχαί ("principalities and powers"): angelic hierarchy (Eph 1:21; 6:12; Col 1:16; 2:10,15)
    "principality":     {"status": "stub-needed"},
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
    print(f'BPG Curation C10: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
