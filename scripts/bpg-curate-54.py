"""
BPG Curation — Batch C54: maasai → marrow (gaps 5499–5598)
Gaps reviewed: 100 (score-5 isbe-scholarly M entries)

M-range names, many apocryphal figures, and compound ISBE forms. No stubs:
significant M concepts (Magi, Son of Man, manuscripts) are all covered in
Easton. Six redirects for compound/variant ISBE forms.
0 stub-needed; 6 redirects; 94 names-only.

Script: scripts/bpg-curate-54.py
Run: python3 scripts/bpg-curate-54.py  (from project root)
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
    "maasai":                 {"status": "names-only"},   # priest (Neh 11:13); minor name
    "maaseas":                {"status": "names-only"},   # apocryphal name
    "maasmas":                {"status": "names-only"},   # apocryphal name
    "mabdai":                 {"status": "names-only"},   # apocryphal name
    "mabnabedai":             {"status": "names-only"},   # apocryphal name
    "macalon":                {"status": "names-only"},   # uncertain; possibly apocryphal
    # ISBE compound; redirect to canonical Easton "Maccabees"
    "maccabaeus;-maccabees":  {"status": "redirect-only", "redirect_to": "maccabees"},
    "machbannai":             {"status": "names-only"},   # Gadite warrior (1 Chr 12:13); minor name
    "machbena":               {"status": "names-only"},   # Judah place name (1 Chr 2:49); minor
    "machir;-machirite":      {"status": "names-only"},   # Manasseh's son/clan; covered under "Machir" in Easton
    # ISBE variant spelling of Michmash; redirect to canonical Easton entry
    "machmas":                {"status": "redirect-only", "redirect_to": "michmash"},
    "maconah":                {"status": "names-only"},   # postexilic town (Neh 11:28); minor geographic
    "macron":                 {"status": "names-only"},   # Seleucid figure (2 Macc 10:12); apocryphal
    "mad;-madness":           {"status": "names-only"},   # KJV "demented" (Deut 28:28; Acts 26:24); lexical
    "madiabun":               {"status": "names-only"},   # apocryphal name
    "maelus":                 {"status": "names-only"},   # apocryphal name
    "maged":                  {"status": "names-only"},   # apocryphal place (1 Macc 5:36)
    "magi-star-of":           {"status": "names-only"},   # Star of Bethlehem (Matt 2:2); covered under "Magi" in Easton
    "magi-the":               {"status": "names-only"},   # covered under "Magi" in Easton
    "magic;-magician":        {"status": "names-only"},   # covered under "Magic" in Easton
    "magnifical":             {"status": "names-only"},   # KJV "magnificent" (1 Chr 22:5); lexical
    "magnificat":             {"status": "names-only"},   # Mary's song (Luke 1:46-55); covered under "Mary" in Easton
    "magnify":                {"status": "names-only"},   # lexical
    # ISBE compound; redirect to canonical Easton "Simon Magus"
    "magus-simon":            {"status": "redirect-only", "redirect_to": "simon-magus"},
    "mahalalel":              {"status": "names-only"},   # antediluvian patriarch (Gen 5:12-17); covered in Easton
    "mahavite":               {"status": "names-only"},   # demonym (1 Chr 11:46); minor
    "mahlites":               {"status": "names-only"},   # Merari clan (Num 3:33; 26:58); minor demonym
    "mahseiah":               {"status": "names-only"},   # Baruch's grandfather (Jer 32:12); minor name
    "maiannas":               {"status": "names-only"},   # apocryphal name
    "maid;-maiden":           {"status": "names-only"},   # lexical
    "mail":                   {"status": "names-only"},   # "coat of mail" (1 Sam 17:5); armor; cultural
    "maimed":                 {"status": "names-only"},   # Matt 18:8; Mark 9:43; lexical
    "mainsall":               {"status": "names-only"},   # Acts 27:40 KJV "mainsail"; nautical/lexical
    "make-maker":             {"status": "names-only"},   # "Maker" as divine title (Isa 17:7; Job 35:10); covered under "God"
    "makebates":              {"status": "names-only"},   # archaic "troublemaker"; lexical
    "maked":                  {"status": "names-only"},   # geographic location (1 Macc 5:26); apocryphal
    "maker":                  {"status": "names-only"},   # "Maker" title for God; covered under "God" in Easton
    "maktesh-the":            {"status": "names-only"},   # Jerusalem district (Zeph 1:11); geographic
    "malachy":                {"status": "names-only"},   # Irish form of Malachi; disambiguation
    "malchielites":           {"status": "names-only"},   # Asherite clan (Num 26:45); minor demonym
    "malchijah":              {"status": "names-only"},   # multiple OT figures (Neh 3:11; Jer 21:1); minor names
    "malchiram":              {"status": "names-only"},   # Jehoiachin's son (1 Chr 3:18); minor name
    "male":                   {"status": "names-only"},   # lexical
    "malefactor":             {"status": "names-only"},   # KJV "evildoer" (Luke 23:32-33; John 18:30); lexical
    "malice-malignity":       {"status": "names-only"},   # covered under "Malice" in Easton; lexical/moral
    "mallos":                 {"status": "names-only"},   # Cilician city (2 Macc 4:30); apocryphal
    "malluchi":               {"status": "names-only"},   # apocryphal priestly name variant
    "mallus":                 {"status": "names-only"},   # variant of Mallos; apocryphal
    "malobathron":            {"status": "names-only"},   # aromatic plant; natural history
    "maltanneus":             {"status": "names-only"},   # apocryphal name
    "mamdai":                 {"status": "names-only"},   # apocryphal name
    "mamnitanemus":           {"status": "names-only"},   # apocryphal name
    "mamuchus":               {"status": "names-only"},   # apocryphal name
    "man-of-war":             {"status": "names-only"},   # warrior; lexical
    "man-natural":            {"status": "names-only"},   # "natural man" (1 Cor 2:14); covered under "Regeneration"
    "man-old":                {"status": "names-only"},   # "old man" (Eph 4:22; Col 3:9); covered under "Regeneration"
    "man-outward":            {"status": "names-only"},   # "outward man" (2 Cor 4:16); Pauline; brief
    "man-son-of":             {"status": "names-only"},   # "Son of Man"; covered under "Son of Man" in Easton
    "man-child":              {"status": "names-only"},   # "man child" (Isa 66:7; Rev 12:5); lexical
    "man;-new":               {"status": "names-only"},   # "new man" (Eph 4:24; Col 3:10); covered under "Regeneration"
    "manahathites":           {"status": "names-only"},   # Benjaminite family (1 Chr 8:6); minor demonym
    "manasseas":              {"status": "names-only"},   # apocryphal name
    "manasseh-1":             {"status": "names-only"},   # Joseph's son/tribe; covered in Easton as "Manasseh"
    "manasseh-2":             {"status": "names-only"},   # King Manasseh; covered in Easton
    "manasseh-3":             {"status": "names-only"},   # other figures named Manasseh; disambiguation
    "manasses-the-prayer-of": {"status": "names-only"},   # apocryphal prayer; extracanonical
    "manassites":             {"status": "names-only"},   # demonym; covered under "Manasseh"
    "maneh;-mina":            {"status": "names-only"},   # unit of weight; covered under "Weights and Measures" in Easton
    "manes":                  {"status": "names-only"},   # apocryphal name
    "mani":                   {"status": "names-only"},   # apocryphal name
    "manifest;-manifestation": {"status": "names-only"},  # "manifest in the flesh" (1 Tim 3:16); lexical
    "manifestly":             {"status": "names-only"},   # lexical
    "manifold":               {"status": "names-only"},   # "manifold wisdom of God" (Eph 3:10); lexical
    "manius;-titus":          {"status": "names-only"},   # Roman figure (1 Macc 15:16); apocryphal
    "mankind":                {"status": "names-only"},   # lexical
    "manlius-titus":          {"status": "names-only"},   # variant; Roman figure in Maccabees; apocryphal
    "manner;-manners":        {"status": "names-only"},   # lexical
    "manservant":             {"status": "names-only"},   # lexical; covered under "Servant" in Easton
    "mansion":                {"status": "names-only"},   # "many mansions" (John 14:2); covered under "Heaven"
    "manstealing":            {"status": "names-only"},   # Exod 21:16; Deut 24:7; covered under "Law"
    "mantelet":               {"status": "names-only"},   # KJV "canopy/penthouse" (Nah 2:5); military/lexical
    "manuscripts":            {"status": "names-only"},   # general; covered under "Bible" in Easton
    "manuscripts-of-the-new-testament": {"status": "names-only"},  # ISBE scholarly; too specialized at score-5
    "manuscripts-of-the-old-testament": {"status": "names-only"},  # ISBE scholarly; too specialized
    "maon;-maonites":         {"status": "names-only"},   # Judah town and people (Josh 15:55; 1 Sam 23:24-25); minor
    "mar":                    {"status": "names-only"},   # lexical
    "march;-marches":         {"status": "names-only"},   # lexical
    "marcion-gospel-of":      {"status": "names-only"},   # Marcion's edited Luke; heretical; brief historical
    # Greek form of Mordecai; redirect to canonical Easton "Mordecai"
    "mardocheus":             {"status": "redirect-only", "redirect_to": "mordecai"},
    "mare":                   {"status": "names-only"},   # female horse; lexical
    "marimoth":               {"status": "names-only"},   # apocryphal name variant (= Meremoth)
    "mariner":                {"status": "names-only"},   # Jonah 1:5; Ezek 27:8-9; lexical
    "marisa":                 {"status": "names-only"},   # Hellenistic city = Mareshah; apocryphal
    "marish":                 {"status": "names-only"},   # KJV "marshland/swamp" (Ezek 47:11); lexical
    # ISBE disambiguation; John Mark; redirect to canonical Easton "Mark"
    "mark-john":              {"status": "redirect-only", "redirect_to": "mark"},
    # ISBE article on Gospel of Mark; redirect to canonical Easton "Mark"
    "mark-the-gospel-according-to": {"status": "redirect-only", "redirect_to": "mark"},
    "market-sheep":           {"status": "names-only"},   # Sheep Gate area (Neh 3:1); geographic
    "market;-marketplace;-mart": {"status": "names-only"},  # covered under "Market" in Easton
    "marmoth":                {"status": "names-only"},   # postexilic figure variant (= Meremoth); minor
    "marrow":                 {"status": "names-only"},   # Job 21:24; Heb 4:12; anatomical/lexical
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
    print(f'BPG Curation C54: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
