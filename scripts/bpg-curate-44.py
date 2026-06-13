"""
BPG Curation — Batch C44: frontier → gilead-mount (gaps 4299–4398)
Gaps reviewed: 100 (score-5 isbe-scholarly F–G entries)

Late-F lexical terms and G-range names/places. No stubs: all significant
concepts are either covered in Easton/Smith or too brief at score-5.
Notable redirects: 18 compound/variant ISBE forms pointing to canonical
Easton articles (galatians-epistle-to-the, ghost-holy, genealogy-of-jesus-
christ-the, gibeath variants, gilead variants, etc.).
0 stub-needed; 18 redirects; 82 names-only.

Script: scripts/bpg-curate-44.py
Run: python3 scripts/bpg-curate-44.py  (from project root)
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
    "frontier":               {"status": "names-only"},   # lexical
    "frowardness":            {"status": "names-only"},   # KJV "perverseness" (Prov 2:14); lexical
    "frustrate":              {"status": "names-only"},   # KJV "make void" (Ezra 4:5; Gal 2:21); lexical
    "fulfil":                 {"status": "names-only"},   # lexical
    "fullers-fountain":       {"status": "names-only"},   # Jerusalem spring near Fuller's Field; geographic
    "fullness":               {"status": "names-only"},   # pleroma (Eph 1:23; 3:19); covered under "Fulness" in Easton
    "furnaces-tower-of-the":  {"status": "names-only"},   # Jerusalem tower (Neh 3:11; 12:38); geographic
    "furnish":                {"status": "names-only"},   # lexical
    "furniture":              {"status": "names-only"},   # tabernacle furniture; covered under "Tabernacle" in Easton
    "further;-furtherance":   {"status": "names-only"},   # KJV "furtherance of the gospel" (Phil 1:12); lexical
    "future":                 {"status": "names-only"},   # lexical
    "gabael":                 {"status": "names-only"},   # Tobit's friend (Tobit 1:14); apocryphal
    "gabbe":                  {"status": "names-only"},   # uncertain place; possibly apocryphal
    "gabrias":                {"status": "names-only"},   # Tobit's relative; apocryphal
    "gad-1":                  {"status": "names-only"},   # tribe/person; covered in Easton as "Gad"
    "gad-2":                  {"status": "names-only"},   # prophet Gad; covered in Easton
    "gad-3":                  {"status": "names-only"},   # pagan deity (Isa 65:11); covered under "Gad" in Easton
    "gad-4":                  {"status": "names-only"},   # ISBE disambiguation variant
    "gad-valley-of":          {"status": "names-only"},   # geographic; covered under "Gad"
    "gaddis":                 {"status": "names-only"},   # Maccabean name (1 Macc 2:2); apocryphal
    "gadites":                {"status": "names-only"},   # demonym; covered under "Gad"
    "gai":                    {"status": "names-only"},   # place name variant; minor
    "gain":                   {"status": "names-only"},   # lexical
    "gainsay":                {"status": "names-only"},   # KJV "contradict/oppose" (Luke 21:15; Tit 1:9); lexical
    "galatians":              {"status": "names-only"},   # demonym; covered under "Galatia" in Easton
    # ISBE compound article on the epistle; redirect to Easton canonical entry
    "galatians-epistle-to-the": {"status": "redirect-only", "redirect_to": "galatians"},
    # ISBE variant spelling of Gilgal; redirect to canonical Easton article
    "galgala":                {"status": "redirect-only", "redirect_to": "gilgal"},
    "galilee-mountain-in":    {"status": "names-only"},   # geographic compound; covered under "Galilee"
    "gallant":                {"status": "names-only"},   # KJV "gallant ship" (Isa 33:21); lexical
    "gamael":                 {"status": "names-only"},   # apocryphal figure (1 Esd 8:29)
    "gangrene":               {"status": "names-only"},   # KJV "canker" (2 Tim 2:17); medical/lexical
    "gar":                    {"status": "names-only"},   # unclear; minor ISBE entry
    "garden-the-kings":       {"status": "names-only"},   # Jerusalem garden area (2 Kings 25:4; Neh 3:15)
    "garden-house":           {"status": "names-only"},   # 2 Kings 9:27; geographic
    "gardener":               {"status": "names-only"},   # John 20:15; lexical
    "gareb-the-hill-of":      {"status": "names-only"},   # Jerusalem topography (Jer 31:39)
    # ISBE variant spelling; redirect to canonical Easton "Gerizim"
    "garizim":                {"status": "redirect-only", "redirect_to": "gerizim"},
    "garland":                {"status": "names-only"},   # Acts 14:13 (wreaths for sacrifice); cultural
    "garmite":                {"status": "names-only"},   # demonym (1 Chr 4:19); minor
    "gas":                    {"status": "names-only"},   # uncertain minor entry
    "gate-corner-fountain-horse-sur": {"status": "names-only"},  # Jerusalem compound gate entry; geographic
    "gate-east":              {"status": "names-only"},   # geographic; covered under city-gate articles
    "gate-the-beautiful":     {"status": "names-only"},   # Acts 3:2,10; covered under "Temple" in Easton
    "gate-valley":            {"status": "names-only"},   # Jerusalem gate (Neh 2:13); geographic
    "gather":                 {"status": "names-only"},   # lexical
    "gaulonitis":             {"status": "names-only"},   # region NE of Sea of Galilee; geographic/historical
    "gauls":                  {"status": "names-only"},   # Galatians as "Gauls"; brief historical note
    # Apocryphal name for Gezer; redirect to canonical Easton "Gezer"
    "gazara":                 {"status": "redirect-only", "redirect_to": "gezer"},
    "gazathites":             {"status": "names-only"},   # demonym; inhabitants of Gaza; covered under "Gaza"
    "gazelle":                {"status": "names-only"},   # natural history; Song of Solomon (2:9; 8:14)
    # Variant spelling; redirect to canonical Easton "Gezer"
    "gazera":                 {"status": "redirect-only", "redirect_to": "gezer"},
    "gazing-stock":           {"status": "names-only"},   # KJV "spectacle" (Nah 3:6; Heb 10:33); lexical
    "gazites":                {"status": "names-only"},   # inhabitants of Gaza; covered under "Gaza"
    "ge-harashim":            {"status": "names-only"},   # "valley of craftsmen" (1 Chr 4:14; Neh 11:35)
    "gecko":                  {"status": "names-only"},   # unclean animal (Lev 11:30 some translations); natural history
    "geddur":                 {"status": "names-only"},   # variant of Gedor; minor place
    "gederah;-gederathite":   {"status": "names-only"},   # Judah town (Josh 15:36); demonym
    "gederite":               {"status": "names-only"},   # demonym; minor
    "gem":                    {"status": "names-only"},   # covered under "Stones, Precious" in Easton
    "gemara":                 {"status": "names-only"},   # Aramaic commentary on Mishnah; Talmudic; too specialized
    "gematria":               {"status": "names-only"},   # numerological interpretation; rabbinical; too specialized
    "gender":                 {"status": "names-only"},   # KJV "beget" (Gal 4:24; Job 38:29); lexical
    # ISBE compound; redirect to Easton genealogy article (Matt 1; Luke 3)
    "genealogy-of-jesus-christ-the": {"status": "redirect-only", "redirect_to": "genealogy"},
    "general;-generally":     {"status": "names-only"},   # lexical
    "gennaeus;-genneus":      {"status": "names-only"},   # apocryphal figure (2 Macc 12:2)
    # Alternate name for Sea of Galilee (Luke 5:1); redirect to canonical article
    "gennesaret-lake-of":     {"status": "redirect-only", "redirect_to": "galilee-sea-of"},
    "gennesaret-land-of":     {"status": "names-only"},   # geographic; covered under "Galilee"
    "gentiles-court-of-the":  {"status": "names-only"},   # temple court; covered under "Temple" in Easton
    "gentiles-isles-of-the":  {"status": "names-only"},   # "coastlands" (Gen 10:5 KJV); lexical/geographic
    "gentleness":             {"status": "names-only"},   # fruit of the Spirit (Gal 5:22-23); covered in Easton
    "geography":              {"status": "names-only"},   # general term; lexical
    "geology-of-palestine":   {"status": "names-only"},   # scholarly/scientific; too specialized at score-5
    "geon":                   {"status": "names-only"},   # variant of Gihon or Kishon; unclear
    "gephyrun":               {"status": "names-only"},   # uncertain minor entry
    "gerasa;-gerasenes":      {"status": "names-only"},   # covered under "Gadara" and "Decapolis" in Easton
    # ISBE compound form; redirect to canonical Easton "Gerizim"
    "gerizim-mount":          {"status": "redirect-only", "redirect_to": "gerizim"},
    "geron":                  {"status": "names-only"},   # apocryphal figure (2 Macc 6:1)
    "gerrenians":             {"status": "names-only"},   # people of Gerra; apocryphal (2 Macc 13:24)
    # ISBE compound entry; redirect to canonical Easton "Gershon"
    "gershon;-gershonites":   {"status": "redirect-only", "redirect_to": "gershon"},
    # Variant spelling; redirect to canonical Easton "Gershon"
    "gerson":                 {"status": "redirect-only", "redirect_to": "gershon"},
    "geruth-chimham":         {"status": "names-only"},   # lodging near Bethlehem (Jer 41:17); geographic
    "geshan":                 {"status": "names-only"},   # Caleb's descendant (1 Chr 2:47); minor name
    "gesture":                {"status": "names-only"},   # cultural; brief
    "get;-getting":           {"status": "names-only"},   # lexical
    "gezrites":               {"status": "names-only"},   # variant of Girzites (1 Sam 27:8); minor group
    # KJV name for the Holy Spirit; redirect to canonical Easton "Holy Spirit"
    "ghost-holy":             {"status": "redirect-only", "redirect_to": "holy-spirit"},
    # Valley of Rephaim (2 Sam 5:18,22; 23:13); redirect to canonical Easton "Rephaim"
    "giants-valley-of-the":   {"status": "redirect-only", "redirect_to": "rephaim"},
    # Variant spelling of Gibeah; redirect to canonical Easton "Gibeah"
    "gibeath-1":              {"status": "redirect-only", "redirect_to": "gibeah"},
    # Another Gibeah variant; redirect to canonical Easton "Gibeah"
    "gibeath-2":              {"status": "redirect-only", "redirect_to": "gibeah"},
    "gibeathite":             {"status": "names-only"},   # demonym; covered under "Gibeah"
    "gibeonites":             {"status": "names-only"},   # covered under "Gibeon" in Easton
    "giblites":               {"status": "names-only"},   # people of Byblos/Gebal; covered under "Gebal"
    "gift-of-tongues":        {"status": "names-only"},   # covered under "Tongues, Gift of" in Easton
    "gifts-of-healing":       {"status": "names-only"},   # spiritual gift (1 Cor 12:9,28); covered under Easton
    "gihon-1":                {"status": "names-only"},   # Jerusalem spring; covered in Easton as "Gihon"
    "gihon-2":                {"status": "names-only"},   # Eden river (Gen 2:13); covered in Easton as "Gihon"
    # ISBE compound; redirect to canonical Easton "Gilboa"
    "gilboa-mount":           {"status": "redirect-only", "redirect_to": "gilboa"},
    # ISBE disambiguation 1; redirect to canonical Easton "Gilead"
    "gilead-1":               {"status": "redirect-only", "redirect_to": "gilead"},
    # ISBE disambiguation 2; redirect to canonical Easton "Gilead"
    "gilead-2":               {"status": "redirect-only", "redirect_to": "gilead"},
    # ISBE geographic compound; redirect to canonical Easton "Gilead"
    "gilead-mount":           {"status": "redirect-only", "redirect_to": "gilead"},
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
    print(f'BPG Curation C44: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
