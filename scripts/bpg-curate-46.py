"""
BPG Curation — Batch C46: guile → healing-gifts-of (gaps 4599–4698)
Gaps reviewed: 100 (score-5 isbe-scholarly G–H entries)

Late-G and early-H entries. One notable stub: hammurabi (Babylonian king;
Code of Hammurabi discovered 1902, after Easton 1897; critical for Mosaic law
parallels and patriarchal period dating). hammurabi-code-of redirects to it.
Five redirects; 94 names-only.
1 stub-needed; 5 redirects; 94 names-only.

Script: scripts/bpg-curate-46.py
Run: python3 scripts/bpg-curate-46.py  (from project root)
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
    "guile":                  {"status": "names-only"},   # KJV "deceit/cunning" (Ps 32:2; 1 Pet 2:22); covered under "Deceit"
    "guilt":                  {"status": "names-only"},   # general concept; covered under "Sin" and "Atonement" in Easton
    "guilt-offering":         {"status": "names-only"},   # asham; covered under "Offerings" and "Trespass Offering" in Easton
    "guiltless":              {"status": "names-only"},   # lexical
    "guilty":                 {"status": "names-only"},   # lexical
    "gulf":                   {"status": "names-only"},   # Luke 16:26; chasm in Lazarus parable; brief/lexical
    "guni;-gunites":          {"status": "names-only"},   # Naphtali clan (Gen 46:24; Num 26:48); demonym
    "gur;-the-ascent-of":     {"status": "names-only"},   # 2 Kings 9:27; geographic
    "gymnasium":              {"status": "names-only"},   # 1 Macc 1:14; Hellenistic institution; brief historical
    "ha":                     {"status": "names-only"},   # exclamation or name prefix; minor ISBE entry
    # Variant spelling of Pi-hahiroth (Exod 14:2); redirect to canonical article
    "ha-hiroth":              {"status": "redirect-only", "redirect_to": "pi-hahiroth"},
    "ha-jehudijah":           {"status": "names-only"},   # 1 Chr 4:18; minor name
    "habaiah;-hobaiah":       {"status": "names-only"},   # returned exiles (Ezra 2:61; Neh 7:63); minor
    # Habakkuk 3 as a distinct poem; redirect to the canonical Easton Habakkuk article
    "habakkuk-the-prayer-of": {"status": "redirect-only", "redirect_to": "habakkuk"},
    "hacaliah":               {"status": "names-only"},   # Nehemiah's father (Neh 1:1; 10:1); minor name
    "hachilah-hill-of":       {"status": "names-only"},   # Judean wilderness (1 Sam 23:19; 26:1); geographic
    "hachmoni;-hachmonite":   {"status": "names-only"},   # Jashobeam's father (1 Chr 11:11; 27:32); minor
    "hagabah":                {"status": "names-only"},   # returned exile (Ezra 2:45; Neh 7:48); minor
    "hagerite":               {"status": "names-only"},   # demonym (1 Chr 27:31); minor
    "haggada":                {"status": "names-only"},   # Jewish oral tradition; Talmudic; too specialized at score-5
    "haggites":               {"status": "names-only"},   # Gad clan (Num 26:15); minor demonym
    "hagia":                  {"status": "names-only"},   # uncertain minor ISBE entry
    "hagri":                  {"status": "names-only"},   # variant of Hagrite (1 Chr 11:38); minor name
    "hagrites":               {"status": "names-only"},   # Arab people (1 Chr 5:10,19-20; Ps 83:6); covered under "Hagarenes"
    "hail-1":                 {"status": "names-only"},   # weather plague (Exod 9); covered under "Hail" in Easton
    "hail-2":                 {"status": "names-only"},   # Greek "chairein" greeting; disambiguation; lexical
    "hair-plucking-of-the":   {"status": "names-only"},   # Ezra 9:3; Neh 13:25; cultural practice
    "halak-mount":            {"status": "names-only"},   # southern boundary (Josh 11:17; 12:7); geographic
    "halakha":                {"status": "names-only"},   # Jewish oral law; Talmudic; too specialized at score-5
    "hale;-haling":           {"status": "names-only"},   # KJV "drag" (Acts 8:3; Luke 12:58); lexical
    "half":                   {"status": "names-only"},   # lexical
    "halicarnassus":          {"status": "names-only"},   # Carian city (1 Macc 15:23); minor geographic
    "hall-judgment":          {"status": "names-only"},   # praetorium; covered under "Praetorium" in Easton
    "hallow;-hallowed":       {"status": "names-only"},   # "hallowed be thy name" (Matt 6:9); covered under "Sanctification"
    "ham-1":                  {"status": "names-only"},   # Noah's son; covered in Easton as "Ham"
    "ham-2":                  {"status": "names-only"},   # ancient name for Egypt; covered under "Ham" in Easton
    "hammeah-the-tower-of":   {"status": "names-only"},   # Jerusalem tower (Neh 3:1; 12:39); geographic
    "hammiphkad-gate-of":     {"status": "names-only"},   # Jerusalem gate (Neh 3:31); geographic
    "hammolecheth":           {"status": "names-only"},   # Machir's sister (1 Chr 7:18); minor name
    "hammuel":                {"status": "names-only"},   # Simeonite (1 Chr 4:26); minor name
    # Babylonian king (c.1792–1750 BC); Code of Hammurabi (282 laws) discovered 1902 — after Easton 1897;
    # parallels to Mosaic law (lex talionis, debt slavery, false witness); cited in OT law debates;
    # important for dating the patriarchal period and understanding ancient Near Eastern legal context
    "hammurabi":              {"status": "stub-needed"},
    # ISBE sub-article on the Code; redirect to the hammurabi stub
    "hammurabi-code-of":      {"status": "redirect-only", "redirect_to": "hammurabi"},
    "hamran":                 {"status": "names-only"},   # Horite (Gen 36:26 variant of Hemdan); minor name
    "hanamel":                {"status": "names-only"},   # Jeremiah's cousin (Jer 32:7-12); covered under "Hanameel"
    "hananel-the-tower-of":   {"status": "names-only"},   # Jerusalem tower (Neh 3:1; Jer 31:38; Zech 14:10); geographic
    "hand-weapon":            {"status": "names-only"},   # cultural/military; brief
    "handful":                {"status": "names-only"},   # lexical
    "handle":                 {"status": "names-only"},   # lexical
    "hands;-hands-imposition-laying-on-of": {"status": "names-only"},  # covered under "Laying on of Hands" in Easton
    "handstaff":              {"status": "names-only"},   # KJV "shaft" (Ezek 39:9); weapon/lexical
    "hangings":               {"status": "names-only"},   # tabernacle curtains (Exod 27:9); covered under "Tabernacle"
    "hap;-haply":             {"status": "names-only"},   # KJV "chance/perhaps" (Ruth 2:3; Acts 17:27); lexical
    "happen":                 {"status": "names-only"},   # lexical
    "happiness":              {"status": "names-only"},   # general; covered under "Beatitudes" and "Joy" in Easton
    "happizzez":              {"status": "names-only"},   # priestly family (1 Chr 24:15); minor name
    # ISBE disambiguation 1; redirect to canonical Easton "Haran"
    "haran-1":                {"status": "redirect-only", "redirect_to": "haran"},
    # ISBE disambiguation 2 (Terah's son); redirect to canonical Easton "Haran"
    "haran-2":                {"status": "redirect-only", "redirect_to": "haran"},
    "harbona;-harbonah":      {"status": "names-only"},   # Persian eunuch (Esth 1:10; 7:9); minor name
    "harbour":                {"status": "names-only"},   # nautical; lexical
    "hard-sayings;-hard-sentences": {"status": "names-only"},  # "hard saying" (John 6:60); lexical
    "hard;-hardiness;-harddiness;-hardly": {"status": "names-only"},  # KJV lexical; compound form
    "harden":                 {"status": "names-only"},   # "hardened heart"; covered under "Hardening" in Easton
    "hardly;-hardness":       {"status": "names-only"},   # lexical
    "harlotry":               {"status": "names-only"},   # covered under "Adultery" and "Harlot" in Easton
    "harod-well-of":          {"status": "names-only"},   # Gideon's spring (Judg 7:1); geographic
    "harosheth-of-the-gentiles-of-the-nations": {"status": "names-only"},  # covered under "Harosheth" in Easton
    "harrows":                {"status": "names-only"},   # 2 Sam 12:31; agricultural tool; cultural
    "harsith":                {"status": "names-only"},   # possible gate name (Jer 19:2); geographic/uncertain
    "hashabneiah":            {"status": "names-only"},   # postexilic name (Neh 3:10; 9:5); minor
    "hashbadana;-hashbadnana": {"status": "names-only"},  # Ezra-Nehemiah figure (Neh 8:4); minor name
    "hasidaeans":             {"status": "names-only"},   # Hasideans (1 Macc 2:42; 7:13); covered under "Pharisees"
    "hasmoneans":             {"status": "names-only"},   # Maccabean dynasty; primarily intertestamental; names-only
    "hassenuah":              {"status": "names-only"},   # Benjaminite family (Neh 11:9); minor name
    "hassophereth":           {"status": "names-only"},   # temple servant family (Ezra 2:55); minor name
    "haste":                  {"status": "names-only"},   # lexical
    "hatchet":                {"status": "names-only"},   # 1 Macc 13:43; weapon; brief
    "hate;-hatred":           {"status": "names-only"},   # theological; "Jacob I loved, Esau I hated" (Rom 9:13); covered
    "hathach":                {"status": "names-only"},   # Persian eunuch (Esth 4:5-10); minor name
    "hatsi-hammenuchoth":     {"status": "names-only"},   # 1 Chr 4:12; minor name
    "haunt":                  {"status": "names-only"},   # KJV "frequent/dwell" (1 Sam 23:22; 30:31); lexical
    "have":                   {"status": "names-only"},   # lexical
    "havens-fair":            {"status": "names-only"},   # Acts 27:8; harbor in Crete; geographic
    "havoc":                  {"status": "names-only"},   # Acts 8:3; lexical
    "havvah":                 {"status": "names-only"},   # variant of Havvoth-jair or Eve; minor
    "havvoth-jair":           {"status": "names-only"},   # "villages of Jair" (Num 32:41; Judg 10:4); covered in Easton
    "hazar":                  {"status": "names-only"},   # prefix "enclosure/village"; lexical/geographic prefix
    "hazar-addar;-hazar-enan;-hazar-gaddah;-hazar-maveth;-hazar-shual;-hazar-susa;-hazar-susim": {"status": "names-only"},  # compound ISBE place names; minor geographic
    "hazazon-tamar":          {"status": "names-only"},   # ancient name for En-gedi (Gen 14:7; 2 Chr 20:2); covered under "En-gedi"
    "hazer-hatticon;-hazarhatticon": {"status": "names-only"},  # Ezekiel boundary (Ezek 47:16); minor geographic
    "hazzelelponi":           {"status": "names-only"},   # Judah name (1 Chr 4:3); minor figure
    "he":                     {"status": "names-only"},   # Hebrew letter or pronoun; minor entry
    "head":                   {"status": "names-only"},   # lexical
    "headband":               {"status": "names-only"},   # cultural; Isa 3:20; brief
    "headstone":              {"status": "names-only"},   # KJV "capstone/cornerstone" (Ps 118:22; Zech 4:7); lexical
    "headstrong":             {"status": "names-only"},   # lexical
    "headtire":               {"status": "names-only"},   # KJV "turban/headdress" (Ezek 24:17,23); lexical
    "heady":                  {"status": "names-only"},   # KJV "rash/impetuous" (2 Tim 3:4); lexical
    "heal":                   {"status": "names-only"},   # lexical
    "healing":                {"status": "names-only"},   # general; covered under "Disease" and "Miracles" in Easton
    "healing-gifts-of":       {"status": "names-only"},   # spiritual gift (1 Cor 12:9,28); covered under gifts in Easton
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
    print(f'BPG Curation C46: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
