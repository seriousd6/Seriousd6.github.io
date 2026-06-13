"""
BPG Curation — Batch C48: holyday → infanticide (gaps 4899–4998)
Gaps reviewed: 100 (score-5 isbe-scholarly H–I entries)

Late-H and early-I entries. One stub: image-of-god (imago Dei, Gen 1:26-27;
foundational for theological anthropology and human dignity; not in Easton as
its own article). Four redirects for compound/variant ISBE forms.
1 stub-needed; 4 redirects; 95 names-only.

Script: scripts/bpg-curate-48.py
Run: python3 scripts/bpg-curate-48.py  (from project root)
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
    "holyday":                {"status": "names-only"},   # KJV "holy day" (Col 2:16; Esth 8:17); lexical
    "home":                   {"status": "names-only"},   # lexical
    "home-born":              {"status": "names-only"},   # KJV "homeborn slave" (Jer 2:14); lexical
    "homicide":               {"status": "names-only"},   # covered under "Murder" and "Manslayer" in Easton
    "honest;-honesty":        {"status": "names-only"},   # KJV "honorable/decent" (Rom 13:13; Phil 4:8); lexical
    "honorable":              {"status": "names-only"},   # lexical
    "hoopoe":                 {"status": "names-only"},   # bird (Lev 11:19; Deut 14:18 some translations); natural history
    # ISBE compound; redirect to canonical Easton "Hophni" (Hophni and Phinehas, Eli's sons)
    "hophni-and-phinehas":    {"status": "redirect-only", "redirect_to": "hophni"},
    "hor-mount":              {"status": "names-only"},   # where Aaron died (Num 20:22-29); covered under "Hor, Mount" in Easton
    "hor-haggidgad":          {"status": "names-only"},   # wilderness camp (Num 33:32-33); minor geographic
    "horesh":                 {"status": "names-only"},   # Judean wilderness (1 Sam 23:15-19); geographic
    # ISBE compound; redirect to canonical Easton "Horites"
    "horite;-horim":          {"status": "redirect-only", "redirect_to": "horites"},
    "horns-of-the-altar":     {"status": "names-only"},   # Exod 27:2; 1 Kings 1:50; covered under "Altar" in Easton
    "horns-rams":             {"status": "names-only"},   # military signal (Josh 6:4); natural history/cultural
    "horrible":               {"status": "names-only"},   # lexical; "horrible thing" (Jer 5:30)
    "horror":                 {"status": "names-only"},   # lexical
    "horse-gate":             {"status": "names-only"},   # Jerusalem gate (Neh 3:28; Jer 31:40); geographic
    "horse-black":            {"status": "names-only"},   # Rev 6:5; covered under "Seals, Seven" in Easton
    "horse-red":              {"status": "names-only"},   # Rev 6:4; covered under "Seals, Seven"
    "horse-white":            {"status": "names-only"},   # Rev 6:2; 19:11; covered under "Seals, Seven"
    "horseleach":             {"status": "names-only"},   # KJV "leech" (Prov 30:15); natural history
    "horses-of-the-sun":      {"status": "names-only"},   # 2 Kings 23:11; pagan solar worship; brief
    "hosen":                  {"status": "names-only"},   # KJV "trousers" (Dan 3:21); lexical
    "hospitality;-host":      {"status": "names-only"},   # covered under "Hospitality" in Easton
    "hosts-lord-of":          {"status": "names-only"},   # "LORD of hosts" (Sabaoth); covered under "God" and "Jehovah" in Easton
    "hotham;-hothan":         {"status": "names-only"},   # Asherite (1 Chr 7:32); minor name
    "hours-of-prayer":        {"status": "names-only"},   # Jewish prayer times (Acts 3:1; Dan 6:10); covered under "Prayer"
    "house-of-god":           {"status": "names-only"},   # general term; covered under "Temple" and "Tabernacle" in Easton
    "house-fathers":          {"status": "names-only"},   # "heads of fathers' houses" (Num 1:44); lexical
    "house-garden":           {"status": "names-only"},   # palace garden; brief geographic
    "household":              {"status": "names-only"},   # lexical
    "household-caesars":      {"status": "names-only"},   # Phil 4:22 "Caesar's household"; brief historical
    "householder":            {"status": "names-only"},   # Matt 13:52; 21:33; lexical
    "housetop":               {"status": "names-only"},   # cultural; Matt 10:27; brief
    "how":                    {"status": "names-only"},   # lexical
    "hozai":                  {"status": "names-only"},   # 2 Chr 33:19 "seers"; minor/uncertain
    "huckster":               {"status": "names-only"},   # KJV "peddle" (2 Cor 2:17); lexical
    "human-sacrifice":        {"status": "names-only"},   # covered under "Molech" and "Idolatry" in Easton
    "humps":                  {"status": "names-only"},   # KJV "hump" (Isa 30:6); lexical/natural history
    "hundred":                {"status": "names-only"},   # lexical
    "hunger":                 {"status": "names-only"},   # lexical
    "hurt":                   {"status": "names-only"},   # lexical
    "husbands-brother":       {"status": "names-only"},   # levirate law kinship term; covered under "Levirate Marriage"
    "husbandman;-husbandry":  {"status": "names-only"},   # KJV "farmer/farming"; covered under "Agriculture" in Easton
    "husham":                 {"status": "names-only"},   # Edomite king (Gen 36:34-35; 1 Chr 1:45-46); minor name
    "hushshathite":           {"status": "names-only"},   # demonym (2 Sam 21:18; 23:27); minor
    "hyades":                 {"status": "names-only"},   # star cluster (Job 9:9 some translations); astronomical
    "hydaspes":               {"status": "names-only"},   # Indian river in apocrypha (Jdt 1:6); minor geographic
    "hyena":                  {"status": "names-only"},   # unclean animal; natural history
    "hypocrisy;-hyprocrite":  {"status": "names-only"},   # covered under "Hypocrisy" in Easton
    "hyrcanus":               {"status": "names-only"},   # Hasmonean figure; intertestamental; covered under "Maccabees"
    # ISBE entry for Hebrew divine name Ehyeh (Exod 3:14); redirect to canonical Easton "Jehovah"
    "i-will-be":              {"status": "redirect-only", "redirect_to": "jehovah"},
    # "I AM THAT I AM" (Exod 3:14); ISBE disambiguation; redirect to canonical Easton "Jehovah"
    "i-i-am-i-am-that-i-am":  {"status": "redirect-only", "redirect_to": "jehovah"},
    "iacimus":                {"status": "names-only"},   # variant of Alcimus; Maccabean high priest; apocryphal
    "iacubus":                {"status": "names-only"},   # variant of Jacob; apocryphal
    "iadinus":                {"status": "names-only"},   # apocryphal name
    "ibis":                   {"status": "names-only"},   # unclean bird (Lev 11:17 some translations); natural history
    "ibsam":                  {"status": "names-only"},   # Issachar clan (1 Chr 7:2); minor name
    "idle;-idleness":         {"status": "names-only"},   # covered under "Sloth" in Easton
    "iduel":                  {"status": "names-only"},   # apocryphal figure (1 Esd 8:43)
    "idumaea;-idumaeans":     {"status": "names-only"},   # Edomites in NT period; covered under "Edom" and "Idumaea" in Easton
    "ieddias":                {"status": "names-only"},   # apocryphal name (1 Esd 9:26)
    "iezer;-iezerites":       {"status": "names-only"},   # Manasseh clan (Num 26:30); minor
    "ignorance":              {"status": "names-only"},   # "sins of ignorance" (Lev 4; Heb 9:7); covered in Easton
    "iliadun":                {"status": "names-only"},   # apocryphal name
    "ill;-ill-favored":       {"status": "names-only"},   # KJV "ugly/bad" (Gen 41:3; Jas 2:2); lexical
    "illumination":           {"status": "names-only"},   # spiritual enlightenment (Heb 6:4); covered under "Enlightenment"
    "illustrious-the":        {"status": "names-only"},   # ISBE title/epithet variant; unclear
    # "Image of God" / imago Dei (Gen 1:26-27; Col 3:10; 2 Cor 3:18); humans created in God's image;
    # basis for human dignity, moral capacity, and the possibility of salvation; dominion mandate;
    # distorted by sin (Gen 5:3), renewed in Christ (Rom 8:29); not covered as standalone article in Easton
    "image-of-god":           {"status": "stub-needed"},
    "images":                 {"status": "names-only"},   # "no graven images" (Exod 20:4); covered under "Idolatry" in Easton
    "imagination":            {"status": "names-only"},   # KJV "evil imagination" (Gen 6:5); lexical
    "imagine":                {"status": "names-only"},   # lexical
    "imalcue":                {"status": "names-only"},   # Maccabean/Arabian figure (1 Macc 11:39); apocryphal
    "imla;-imlah":            {"status": "names-only"},   # Micaiah's father (1 Kings 22:8-9); minor name
    "immaculate-conception-the": {"status": "names-only"},  # Catholic doctrine; not a biblical concept per se
    "immortal;-immortality":  {"status": "names-only"},   # covered under "Immortality" in Easton
    "immutability;-immutable": {"status": "names-only"},  # God's unchangeableness; covered under "God" in Easton
    "imnites":                {"status": "names-only"},   # Asherite clan (Num 26:44); minor demonym
    "impart":                 {"status": "names-only"},   # lexical
    "impediment":             {"status": "names-only"},   # Mark 7:32 (speech impediment); lexical
    "implead":                {"status": "names-only"},   # KJV "sue/accuse" (Acts 19:38); lexical
    "importable":             {"status": "names-only"},   # KJV "unbearable" (Acts 15:10); lexical
    "importunity":            {"status": "names-only"},   # Luke 11:8 (persistence in prayer); covered under "Prayer"
    "imposition-of-hands":    {"status": "names-only"},   # covered under "Laying on of Hands" in Easton
    "impossible":             {"status": "names-only"},   # lexical
    "impotent":               {"status": "names-only"},   # KJV "unable/powerless" (John 5:3,7; Acts 4:9); lexical
    "imprisonment":           {"status": "names-only"},   # legal/historical; covered briefly in Easton
    "impurity":               {"status": "names-only"},   # covered under "Clean and Unclean" in Easton
    "in":                     {"status": "names-only"},   # lexical preposition; minor ISBE entry
    "in-the-lord":            {"status": "names-only"},   # Pauline phrase (Rom 16:2; Eph 4:1); brief
    "incantation":            {"status": "names-only"},   # covered under "Magic" and "Divination" in Easton
    "incest":                 {"status": "names-only"},   # Lev 18; 1 Cor 5:1; covered under "Incest" in Easton
    "incontinency":           {"status": "names-only"},   # KJV "lack of self-control" (1 Cor 7:5; 2 Tim 3:3); lexical
    "incorruption":           {"status": "names-only"},   # KJV "immortality" (1 Cor 15:42-54); covered under "Immortality"
    "increase":               {"status": "names-only"},   # lexical
    "indignities":            {"status": "names-only"},   # lexical
    "indite":                 {"status": "names-only"},   # KJV "compose/dictate" (Ps 45:1); lexical
    "infancy-gospel-of-the":  {"status": "names-only"},   # extracanonical apocryphal gospel; too specialized
    "infant-baptism":         {"status": "names-only"},   # paedobaptism debate; covered under "Baptism" in Easton
    "infanticide":            {"status": "names-only"},   # child sacrifice/killing; covered under "Murder" and "Molech"
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
    print(f'BPG Curation C48: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
