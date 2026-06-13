"""
BPG Curation — Batch C19: mahavite-the → phares-pharez-or-perez (gaps 1799–1898)
Gaps reviewed: 100 (score-10 entries, M–P range)

Dense cluster of Gospel/book article variants (mark-gospel-of, matthew-gospel-of,
micah-the-book-of, nehemiah-the-book-of) and four Mary entries — all redirect to Easton
canonical slugs. Also: Babylonian/Assyrian Smith combined forms (medes-media,
nebuchadnezzar-or-nebuchadrezzar), triple nahshon variants, and four mary entries.

Key stubs: Miracles (Smith article; core NT concept), Parables (Jesus's teaching method).
Redirect cluster: Gospel/book variants, four Mary entries, demonyms, Smith combined forms.

Script: scripts/bpg-curate-19.py
Run: python3 scripts/bpg-curate-19.py  (from project root)
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
    # ── M entries ─────────────────────────────────────────────────────────────
    "mahavite-the":        {"status": "names-only"},   # 1 Chr 11:46 epithet; obscure
    # Smith combined variant; Easton has mahalaleel.json (Enoch's grandfather, Gen 5:12)
    "maleleel-or-mahalaleel": {"status": "redirect-only", "redirect_to": "mahalaleel"},
    "manahetbites":        {"status": "names-only"},   # Manahathites; Caleb descendants (1 Chr 2:54)
    # Manasseh's descendants; Easton has manasseh.json
    "manassites-the":      {"status": "redirect-only", "redirect_to": "manasseh"},
    "maonites-the":        {"status": "names-only"},   # Judg 10:12 obscure people; minor
    # Smith combined variant; Easton has mareshah.json (Judah city; 2 Chr 11:8; Micah's birthplace)
    "mareshah-or-mareshah": {"status": "redirect-only", "redirect_to": "mareshah"},
    # Smith gospel variant; Easton has mark.json
    "mark-gospel-of":      {"status": "redirect-only", "redirect_to": "mark"},
    "market-of-appius":    {"status": "names-only"},   # Acts 28:15 Appii Forum; single reference
    "marketplaces":        {"status": "names-only"},   # general reference
    "martyrdom":           {"status": "names-only"},   # 32 Nave verses; general concept
    # Mary Magdalene (Luke 8:2; John 20:11-18); Easton has mary.json
    "mary-magdalene":      {"status": "redirect-only", "redirect_to": "mary"},
    # Virgin Mary; Easton has mary.json
    "mary-the-virgin":     {"status": "redirect-only", "redirect_to": "mary"},
    # Mary mother of John Mark (Acts 12:12); Easton has mary.json
    "mary-mother-of-mark": {"status": "redirect-only", "redirect_to": "mary"},
    # Mary of Bethany (Luke 10:39; John 11:2); Easton has mary.json
    "mary-sister-of-lazarus": {"status": "redirect-only", "redirect_to": "mary"},
    "massrekah":           {"status": "names-only"},   # Edomite royal city (Gen 36:36)
    "matithiah":           {"status": "names-only"},   # multiple minor figures (1 Chr 15:18; Neh 8:4)
    # Smith gospel variant; Easton has matthew.json
    "matthew-gospel-of":   {"status": "redirect-only", "redirect_to": "matthew"},
    "measures":            {"status": "names-only"},   # biblical weights/measures; no distinct Easton article
    "mecherathite-the":    {"status": "names-only"},   # 1 Chr 11:36 epithet; obscure
    # Smith combined; Easton has media.json (Medo-Persian empire; Dan 5:28)
    "medes-media":         {"status": "redirect-only", "redirect_to": "media"},
    # "The Median" demonym; Easton has media.json
    "median-the":          {"status": "redirect-only", "redirect_to": "media"},
    "mehetableel":         {"status": "names-only"},   # Neh 6:10; minor figure
    "meholathite-the":     {"status": "names-only"},   # Adriel's epithet (1 Sam 18:19)
    "mehunims-the":        {"status": "names-only"},   # Meunim people (2 Chr 26:7)
    # Smith variant of Melchizedek; Easton has melchizedek.json (Gen 14:18; Heb 7)
    "melchisedec":         {"status": "redirect-only", "redirect_to": "melchizedek"},
    "merarath":            {"status": "names-only"},   # Smith place entry; minor
    # Smith combined; Easton has merari.json (Levi's third son; temple servants)
    "merari-merarites":    {"status": "redirect-only", "redirect_to": "merari"},
    "mercury":             {"status": "names-only"},   # Acts 14:12 (called Hermes/Mercury); pagan god
    "meribbaa":            {"status": "names-only"},   # Mephibosheth's son (1 Chr 8:34 variant)
    "meronothithe-the":    {"status": "names-only"},   # Neh 3:7; 1 Chr 27:30 epithet
    "mesech-meshech":      {"status": "names-only"},   # Japheth's son (Gen 10:2); Ps 120:5 variant
    "meshezabeel":         {"status": "names-only"},   # Neh 3:4; 10:21; minor figures
    "mesobaite-the":       {"status": "names-only"},   # 1 Chr 11:47 epithet; obscure
    # Greek form of Messiah (John 1:41; 4:25); Easton has messiah.json
    "messias":             {"status": "redirect-only", "redirect_to": "messiah"},
    "meuzai":              {"status": "names-only"},   # Smith place; unclear entry
    # Smith "book of" variant; Easton has micah.json
    "micah-the-book-of":   {"status": "redirect-only", "redirect_to": "micah"},
    # Smith combined variant; Easton has michmash.json (Saul's battle; 1 Sam 13-14)
    "michmas-or-michmash": {"status": "redirect-only", "redirect_to": "michmash"},
    "millo-the-house-of":  {"status": "names-only"},   # fortification (Judg 9:6; 2 Sam 5:9)
    "mines-mining":        {"status": "names-only"},   # Job 28 passage; general reference
    "miphkad":             {"status": "names-only"},   # Jerusalem gate (Neh 3:31); single reference
    # Signs and wonders throughout Scripture; core NT concept; no Easton miracles.json
    "miracles":            {"status": "stub-needed"},
    "mirma":               {"status": "names-only"},   # Benjamin descendant (1 Chr 8:10)
    "mishal-or-misheal":   {"status": "names-only"},   # Asher town (Josh 19:26 variant)
    "mishraites-the":      {"status": "names-only"},   # Caleb descendants (1 Chr 2:53)
    "missions":            {"status": "names-only"},   # 25 Nave verses; general concept
    "mithnite-the":        {"status": "names-only"},   # 1 Chr 11:43 epithet; obscure
    # Smith variant; Easton has mizpah.json (important meeting place; Gen 31:49; Judg 11:11)
    "mizpeh":              {"status": "redirect-only", "redirect_to": "mizpah"},
    # Smith combined variant; Easton has mizraim.json (Hebrew name for Egypt)
    "mizraim-or-mizraim":  {"status": "redirect-only", "redirect_to": "mizraim"},
    "moabite-stone-the":   {"status": "names-only"},   # Mesha stele; archaeological inscription
    # Moabites demonym; Easton has moab.json
    "moabites":            {"status": "redirect-only", "redirect_to": "moab"},
    "mocking":             {"status": "names-only"},   # 25 Nave verses; general
    "morasthite-the":      {"status": "names-only"},   # Micah's epithet (Jer 26:18)
    "mountain":            {"status": "names-only"},   # 31 Nave verses; general geographic
    "mountain-of-the-amorites": {"status": "names-only"},  # Deut 1:7; single reference
    "muaz":                {"status": "names-only"},   # Smith entry; unclear figure
    "mulbury-trees":       {"status": "names-only"},   # 2 Sam 5:23-24 baca trees; general
    "musical-instruments-of-the-hebrews": {"status": "names-only"},  # Smith article; general
    # Nave concept (32 verses); Easton has mystery.json (Rom 16:25; Eph 3:3-6)
    "mysteries":           {"status": "redirect-only", "redirect_to": "mystery"},

    # ── N entries ─────────────────────────────────────────────────────────────
    # Naamites = Naaman's clan (Num 26:40); Easton has naaman.json
    "naamites-the":        {"status": "redirect-only", "redirect_to": "naaman"},
    # Greek form of Nahshon (Matt 1:4; Luke 3:32); Easton has nahshon.json
    "naasson":             {"status": "redirect-only", "redirect_to": "nahshon"},
    "nachons":             {"status": "names-only"},   # Nacon/Nachon (2 Sam 6:6); single reference
    "nahalal-or-nahalal":  {"status": "names-only"},   # Zebulun town (Josh 19:15); Smith combined
    "nahalol":             {"status": "names-only"},   # variant of Nahalal (Josh 21:35)
    "nahamaai":            {"status": "names-only"},   # returned exile (Neh 7:7 variant)
    "nahari":              {"status": "names-only"},   # Joab's armor-bearer (2 Sam 23:37 variant)
    # Smith combined variant; Easton has nahshon.json (Aaron's brother-in-law; Num 1:7)
    "nahshon-or-naashon":  {"status": "redirect-only", "redirect_to": "nahshon"},
    "names":               {"status": "names-only"},   # Smith article on biblical names; general
    "nave":                {"status": "names-only"},   # architectural term (1 Kgs 6:17); general
    # Smith combined variant; Easton has nebaioth.json (Ishmael's firstborn; Gen 25:13)
    "nebaioth-nebajoth":   {"status": "redirect-only", "redirect_to": "nebaioth"},
    # Smith combined variant; Easton has nebuchadnezzar.json (Babylonian king)
    "nebuchadnezzar-or-nebuchadrezzar": {"status": "redirect-only", "redirect_to": "nebuchadnezzar"},
    # Smith "book of" variant; Easton has nehemiah.json
    "nehemiah-the-book-of": {"status": "redirect-only", "redirect_to": "nehemiah"},
    "nephtoah-or-nephtoah": {"status": "names-only"},  # border spring (Josh 15:9); Smith combined
    "netophathite":        {"status": "names-only"},   # person from Netophah; minor epithet
    "nopha":               {"status": "names-only"},   # Moabite city (Num 21:30); minor
    "nose-jewel":          {"status": "names-only"},   # Isa 3:21; general jewelry reference
    "numbers":             {"status": "names-only"},   # book of Numbers; no Easton numbers.json
    "nurse":               {"status": "names-only"},   # Deborah, Naomi; general reference
    "nym-phas":            {"status": "names-only"},   # Col 4:15 Nympha; minor figure

    # ── O entries ─────────────────────────────────────────────────────────────
    "offerings":           {"status": "names-only"},   # Smith article; general; individual offerings covered
    "old-age":             {"status": "names-only"},   # 25 Nave verses; general concept
    # Smith combined; Easton has omega.json (Alpha and Omega; Rev 1:8)
    "omega-or-omega":      {"status": "redirect-only", "redirect_to": "omega"},
    "opinion-public":      {"status": "names-only"},   # 29 Nave verses; general
    "orator":              {"status": "names-only"},   # Acts 24:1 Tertullus; general
    # Smith "rock of" variant; Easton has oreb.json (Midianite prince; Judg 7:25)
    "oreb-the-rock":       {"status": "redirect-only", "redirect_to": "oreb"},
    "ornaments-personal":  {"status": "names-only"},   # Isa 3:18-23 jewelry list; general

    # ── P entries ─────────────────────────────────────────────────────────────
    "paial":               {"status": "names-only"},   # Neh 11:12 variant; minor figure
    # Smith combined; Easton has palestine.json
    "palestina-and-palestine": {"status": "redirect-only", "redirect_to": "palestine"},
    "palluites":           {"status": "names-only"},   # Pallu's family (Num 26:5)
    # Jesus's teaching method (Matt 13; Luke 15); 30 Nave verses; significant NT concept
    "parables":            {"status": "stub-needed"},
    "parnaeh":             {"status": "names-only"},   # Zebulun leader (Num 34:25)
    "patriotism":          {"status": "names-only"},   # 34 Nave verses; general
    "peacocks":            {"status": "names-only"},   # 1 Kgs 10:22; general animal reference
    "pedarhzur":           {"status": "names-only"},   # Manasseh tribal leader (Num 1:10 variant)
    "pelonite-the":        {"status": "names-only"},   # 1 Chr 11:36 epithet; obscure
    "penny-pennyworth":    {"status": "names-only"},   # KJV denarius (Matt 20:2); translation artifact
    # Smith article; Easton has pentateuch.json (Torah; Gen–Deut)
    "pentateuch-the":      {"status": "redirect-only", "redirect_to": "pentateuch"},
    # Pergamum church (Rev 2:12-17); Easton has pergamos.json
    "pergamum":            {"status": "redirect-only", "redirect_to": "pergamos"},
    # Smith "the" variant; Easton has perizzites.json (pre-Canaanite people)
    "perizzite-the":       {"status": "redirect-only", "redirect_to": "perizzites"},
    "pharaoh-the-wife-of": {"status": "names-only"},   # Solomon's wife (1 Kgs 3:1); general
    # Smith combined; Easton has perez.json (Judah's son; Ruth 4:18; Matt 1:3)
    "phares-pharez-or-perez": {"status": "redirect-only", "redirect_to": "perez"},
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
    print(f'BPG Curation C19: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
