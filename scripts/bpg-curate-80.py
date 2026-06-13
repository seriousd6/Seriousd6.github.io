"""
BPG Curation — Batch C80: miter → propagation (gaps 8008–8117)
Gaps reviewed: 110 (score-3 concept-no-article M–P entries)

Score-3 entries: ethical abstractions, cultural practices, NT terms, minor OT topics.
0 stubs; 12 redirects to existing dict articles; 98 names-only.

Script: scripts/bpg-curate-80.py
Run: python3 scripts/bpg-curate-80.py  (from project root)
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
    # ── M: continued ──────────────────────────────────────────────────────
    "miter":                       {"status": "names-only"},   # Exod 28:4 priestly headwear; no dict article
    "mob":                         {"status": "names-only"},   # Acts 17:5; 21:30; crowd violence; names-only
    "modesty":                     {"status": "names-only"},   # 1 Tim 2:9; covered under "meekness"/"temperance"
    "molding":                     {"status": "names-only"},   # Exod 25:25 tabernacle detail; architectural
    "monarchy":                    {"status": "names-only"},   # 1 Sam 8 request for king; covered under "kings"
    "money-changers":              {"status": "names-only"},   # Matt 21:12; covered under "temple/Jerusalem"
    "monopoly":                    {"status": "names-only"},   # economic; names-only
    "moral-agency":                {"status": "names-only"},   # philosophical; not a Nave topic with rich verses
    "moral-law":                   {"status": "redirect-only", "redirect_to": "law"},
    "mortification":               {"status": "names-only"},   # Col 3:5; covered under "self-denial"
    "mosaic-law":                  {"status": "redirect-only", "redirect_to": "law"},
    "mote-a-speck":                {"status": "names-only"},   # Matt 7:3-5 eye/speck; covered under "Sermon on the Mount"
    "motive":                      {"status": "names-only"},   # 17 verses; covered under "heart" and "purity"
    "motto":                       {"status": "names-only"},   # not a biblical topic; names-only
    "mulberry-tree":               {"status": "names-only"},   # 2 Sam 5:23; botanical; names-only
    "munitions":                   {"status": "names-only"},   # Isa 33:16; names-only
    "murrain-a-disease-of-livestock": {"status": "names-only"},  # Exod 9:3 5th plague; covered under "plagues"
    "muster":                      {"status": "names-only"},   # military assembly; names-only
    "mutiny":                      {"status": "names-only"},   # Num 16; covered under "Korah"
    # ── N ─────────────────────────────────────────────────────────────────
    "names-of-jesus":              {"status": "names-only"},   # Christological titles; covered under "Jesus Christ"
    "natural-religion":            {"status": "names-only"},   # philosophical theology; names-only
    "naturalization":              {"status": "names-only"},   # Ruth 1:16; Eph 2:19; names-only
    "navigation":                  {"status": "names-only"},   # Acts 27; covered under "ships"
    "nebuzaradan-nebuzar-adan":    {"status": "names-only"},   # 2 Kgs 25:8-20; Babylonian captain; covered in Smith
    "neophytes":                   {"status": "names-only"},   # 1 Tim 3:6; new converts; names-only
    "nepotism":                    {"status": "names-only"},   # OT court favoritism; names-only
    "new-creature":                {"status": "redirect-only", "redirect_to": "regeneration"},
    "nolle-prosequi":              {"status": "names-only"},   # Roman legal term; Luke 23; names-only
    "nonconformity":               {"status": "names-only"},   # Dan 1:8; Rom 12:2; names-only
    "nose":                        {"status": "names-only"},   # anatomical/figurative; names-only
    "nut":                         {"status": "names-only"},   # Song 6:11; Gen 43:11; botanical
    # ── O ─────────────────────────────────────────────────────────────────
    "obduracy-hardness":           {"status": "names-only"},   # 17 verses; Exod 4:21; Heb 3:8; covered under "hardness of heart"
    "object-teaching":             {"status": "names-only"},   # prophetic visual symbols; names-only
    "obligation":                  {"status": "names-only"},   # 15 verses; covenant duty; covered under "duty"
    "obliquity-deviation":         {"status": "names-only"},   # names-only
    "obsequiousness":              {"status": "names-only"},   # flattery; Prov 26:28; names-only
    "obstetrics":                  {"status": "names-only"},   # Gen 35:17; Exod 1:15-21; midwifery context
    "occult-science":              {"status": "redirect-only", "redirect_to": "witchcraft"},
    "offenses":                    {"status": "names-only"},   # Matt 18:7; covered under "stumbling block"
    "opportunity":                 {"status": "names-only"},   # 14 verses; Gal 6:10; Eph 5:16; names-only
    "ostentation":                 {"status": "names-only"},   # Matt 6:1-4; covered under "almsgiving"/"hypocrisy"
    "ostriches":                   {"status": "names-only"},   # Job 39:13-18; Lam 4:3; names-only
    "overcoming":                  {"status": "names-only"},   # Rev 2-3; covered under "victory"
    # ── P ─────────────────────────────────────────────────────────────────
    "pack-animals":                {"status": "names-only"},   # Gen 45:23; cultural; names-only
    "pale-horse":                  {"status": "names-only"},   # Rev 6:8; covered under "Revelation" commentary
    "panic":                       {"status": "names-only"},   # 12 verses; 1 Sam 14:15; covered under "fear"
    "pantomime":                   {"status": "names-only"},   # prophetic symbolic acts; names-only
    "paradox":                     {"status": "names-only"},   # 16 verses; biblical paradoxes; names-only
    "paralysis":                   {"status": "names-only"},   # 8 verses; Matt 9:2; healing miracles; names-only
    "parricide":                   {"status": "names-only"},   # killing of father; legal; names-only
    "parsimony-stinginess":        {"status": "names-only"},   # 11 verses; covered under "covetousness"
    "partiality":                  {"status": "names-only"},   # Lev 19:15; James 2:1-9; covered under "justice"
    "particeps-criminis":          {"status": "names-only"},   # Roman legal; 1 Tim 5:22; names-only
    "partnership":                 {"status": "names-only"},   # Phil 1:5; 2 Cor 6:14; names-only
    "paschal-lamb":                {"status": "redirect-only", "redirect_to": "passover"},
    "passenger":                   {"status": "names-only"},   # names-only
    "passports":                   {"status": "names-only"},   # Neh 2:7-9; letters of transit; names-only
    "patriarchal-government":      {"status": "names-only"},   # Gen 18; covered under "patriarchs"
    "patricide":                   {"status": "names-only"},   # 2 Kgs 19:37; names-only
    "pawn":                        {"status": "names-only"},   # 10 verses; Exod 22:26; pledge/collateral; names-only
    "penalty":                     {"status": "names-only"},   # covered under "punishment"
    "penitence":                   {"status": "redirect-only", "redirect_to": "repentance"},
    "penuriousness-stinginess":    {"status": "names-only"},   # names-only
    "people-common":               {"status": "names-only"},   # Lev 4:27; names-only
    "perfidy-treachery":           {"status": "names-only"},   # Ps 55:20-21; covered under "treachery"
    "perfume":                     {"status": "names-only"},   # Exod 30:23-25; covered under "anointing"/"incense"
    "personal-call":               {"status": "names-only"},   # divine vocation; covered under "call"
    "personification":             {"status": "names-only"},   # Prov 8:1-36 (Lady Wisdom); rhetorical; names-only
    "petroleum":                   {"status": "names-only"},   # Gen 11:3 asphalt; names-only
    "philanthropy":                {"status": "names-only"},   # 1 verse; covered under "benevolence"
    "phoebe-phebe":                {"status": "names-only"},   # Rom 16:1-2; minor NT deaconess; no dict article
    "physiognomy":                 {"status": "names-only"},   # 1 Sam 16:7; names-only
    "physiology":                  {"status": "names-only"},   # 5 verses; Ps 139:14; names-only
    "pinnacle-wing":               {"status": "names-only"},   # Matt 4:5; Luke 4:9; temple pinnacle; names-only
    "pispah":                      {"status": "names-only"},   # 1 Chr 7:38; minor Asherite; names-only
    "planet":                      {"status": "names-only"},   # 2 Kgs 23:5 KJV; astronomical; names-only
    "plants":                      {"status": "names-only"},   # botanical; general; names-only
    "plaster":                     {"status": "names-only"},   # Deut 27:2; Lev 14:42; architectural; names-only
    "pleading":                    {"status": "names-only"},   # 8 verses; legal/intercessory; names-only
    "plowshare":                   {"status": "names-only"},   # Isa 2:4; Joel 3:10; agricultural; names-only
    "plummet":                     {"status": "names-only"},   # 2 Kgs 21:13; Amos 7:7-8; construction; names-only
    "politics":                    {"status": "names-only"},   # 17 verses; cultural; covered under "government"
    "poll-tax":                    {"status": "names-only"},   # Exod 30:13; Matt 22:17; covered under "tribute"
    "polytheism":                  {"status": "redirect-only", "redirect_to": "idolatry"},
    "popular-sins":                {"status": "names-only"},   # 1 verse; names-only
    "popularity":                  {"status": "names-only"},   # Matt 21:9; names-only
    "porcius":                     {"status": "names-only"},   # Acts 24:27 Porcius Festus; covered under "Festus"
    "porters":                     {"status": "names-only"},   # 9 verses; Ezra 2:42; temple gatekeepers; names-only
    "prayerfulness":               {"status": "redirect-only", "redirect_to": "prayer"},
    "prayerlessness":              {"status": "redirect-only", "redirect_to": "prayer"},
    "precepts":                    {"status": "names-only"},   # Ps 119:4; covered under "commandments"
    "preparation-day":             {"status": "names-only"},   # Matt 27:62; John 19:14; Friday; names-only
    "presbyter":                   {"status": "redirect-only", "redirect_to": "elder"},
    "prescience":                  {"status": "names-only"},   # God's foreknowledge; covered under "omniscience"
    "pretorium":                   {"status": "redirect-only", "redirect_to": "praetorium"},
    "prince-of-peace":             {"status": "names-only"},   # Isa 9:6; Messianic title; covered under "Christ"
    "princesses":                  {"status": "names-only"},   # names-only
    "privilege":                   {"status": "names-only"},   # names-only
    "probation":                   {"status": "names-only"},   # 14 verses; testing/trial period; names-only
    "proclamation":                {"status": "names-only"},   # 11 verses; names-only
    "prodigal-son":                {"status": "names-only"},   # Luke 15:11-32; covered under "parables"
    "prodigality-waywardness":     {"status": "names-only"},   # names-only
    "profanation":                 {"status": "names-only"},   # covered under "temple"/"desecration"
    "profanity":                   {"status": "names-only"},   # covered under "blasphemy"
    "profession":                  {"status": "names-only"},   # Heb 3:1; 10:23; names-only
    "prognostication":             {"status": "names-only"},   # Isa 47:13; covered under "divination"
    "prohibition":                 {"status": "names-only"},   # names-only
    "promises":                    {"status": "redirect-only", "redirect_to": "covenant"},
    "promotion":                   {"status": "names-only"},   # 14 verses; names-only
    "propagation":                 {"status": "names-only"},   # Gen 9:7; cultural; names-only
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
    print(f'BPG Curation C80: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
