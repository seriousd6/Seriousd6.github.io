"""
BPG Curation — Batch C66: seleucidae → shemida;-shemidah;-shemidaites (gaps ~6629–6733)
Gaps reviewed: 105 (score-5 isbe-scholarly S entries)

Score-5 ISBE posture: ~95% names-only. Notable stubs: servant-of-jehovah (Isaiah's
Servant Songs; major messianic category) and shekinah (God's manifest presence/glory).
2 stub-needed; 4 redirects; 99 names-only.

Script: scripts/bpg-curate-66.py
Run: python3 scripts/bpg-curate-66.py  (from project root)
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
    "seleucidae":               {"status": "names-only"},   # Seleucid dynasty; historical background; covered under "syria"
    "self-control":             {"status": "names-only"},   # Gal 5:23; covered under "temperance"
    "self-righteousness":       {"status": "names-only"},   # Luke 18:9-14; covered under "pharisees"
    "self-surrender":           {"status": "names-only"},   # general concept; covered under "denial, self"
    "self-will":                {"status": "names-only"},   # 2 Pet 2:10 KJV; lexical
    "sell-seller":              {"status": "names-only"},   # ISBE compound; lexical
    "selvedge":                 {"status": "names-only"},   # Exod 26:4 KJV curtain edge; archaic
    "semeias":                  {"status": "names-only"},   # apocryphal (1 Esd 8:43)
    "semeis":                   {"status": "names-only"},   # apocryphal (1 Esd 9:32)
    "semellius":                {"status": "names-only"},   # apocryphal (1 Esd 2:16)
    "semis":                    {"status": "names-only"},   # apocryphal
    "semites-semitic-religion": {"status": "names-only"},   # too broad/specialized at score-5
    "senate;-senator":          {"status": "names-only"},   # Acts 5:21 "council of elders"; covered under "sanhedrin"
    "senses":                   {"status": "names-only"},   # Heb 5:14; lexical
    "sensual":                  {"status": "names-only"},   # Jas 3:15; Jude 19 KJV; lexical
    "sent":                     {"status": "names-only"},   # lexical
    "sentence":                 {"status": "names-only"},   # lexical; covered under "judgment"
    "separate":                 {"status": "names-only"},   # lexical
    "separation":               {"status": "names-only"},   # Num 6:2-21 Nazirite; covered under "nazirite"
    "sepharvites":              {"status": "names-only"},   # 2 Kgs 17:31; Samaritan settlers; minor
    "sepphoris":                {"status": "names-only"},   # Galilean city near Nazareth; NT background; names-only
    "serar":                    {"status": "names-only"},   # apocryphal
    "serjeants":                {"status": "names-only"},   # Acts 16:35,38 KJV "lictors"; archaic
    "sermon-on-the-plain-the":  {"status": "names-only"},   # Luke 6:17-49; covered under "beatitudes"
    "seron":                    {"status": "names-only"},   # Seleucid commander (1 Macc 3:13); apocryphal
    "serpent-worship":          {"status": "names-only"},   # ancient practice; covered under "serpent"
    # Num 21:8-9 Moses' bronze serpent; destroyed by Hezekiah (2 Kgs 18:4, Nehushtan);
    # redirect to canonical Nehushtan article — John 3:14 typological connection covered there
    "serpent-brazen":           {"status": "redirect-only", "redirect_to": "nehushtan"},
    "serpent-crooked":          {"status": "names-only"},   # Isa 27:1; Job 26:13; poetic; lexical
    "serpent-charming":         {"status": "names-only"},   # Ps 58:4-5; Eccl 10:11; covered under "divination"
    # Isaiah's four Servant Songs (Isa 42:1-4; 49:1-6; 50:4-9; 52:13–53:12); identified variously
    # with Israel, Cyrus, Deutero-Isaiah, and ultimately Jesus (Acts 8:32-35; 1 Pet 2:22-25);
    # "he was wounded for our transgressions" (Isa 53:5); foundational for NT atonement theology
    # and messianic interpretation of OT; essential for any serious biblical study
    "servant-of-jehovah;-servant-of-the-lord;-servant-of-yahweh": {"status": "stub-needed"},
    "servants-solomons":        {"status": "names-only"},   # post-exilic families (Ezra 2:55-58); minor
    "service":                  {"status": "names-only"},   # lexical; covered under "ministry"
    "servitude":                {"status": "names-only"},   # lexical; covered under "slavery"
    "sesis":                    {"status": "names-only"},   # apocryphal
    "sesthel":                  {"status": "names-only"},   # apocryphal (1 Esd 9:31)
    "set":                      {"status": "names-only"},   # lexical
    # ISBE compound; redirect to canonical Seth article
    "seth;-sheth":              {"status": "redirect-only", "redirect_to": "seth"},
    "setting":                  {"status": "names-only"},   # lexical; jewelry context
    "settle-1":                 {"status": "names-only"},   # Ezek 43:14,17,20 temple ledge; architectural
    "settle-2":                 {"status": "names-only"},   # place reference; Ezek; minor
    "seven-churches":           {"status": "names-only"},   # Rev 2-3; covered under "revelation" and "churches"
    "seven-stars":              {"status": "names-only"},   # Rev 1:16,20; covered under "pleiades" and "revelation"
    # ISBE variant of Syene; redirect to canonical Syene article
    "seveneh":                  {"status": "redirect-only", "redirect_to": "syene"},
    "seventh-day":              {"status": "names-only"},   # Sabbath; covered under "sabbath"
    "seventy":                  {"status": "names-only"},   # Luke 10:1 disciples; covered under "disciples"
    "seventy-disciples":        {"status": "names-only"},   # Luke 10:1-24; covered under "disciples"
    "seventy-years":            {"status": "names-only"},   # Jer 25:11; Dan 9; covered under "captivity"
    "sever":                    {"status": "names-only"},   # lexical
    "several;-severally":       {"status": "names-only"},   # KJV "each one/separate"; archaic
    "shaalim-land-of":          {"status": "names-only"},   # 1 Sam 9:4; place; minor
    "shade;-shadow;-shadowing": {"status": "names-only"},   # ISBE compound; KJV lexical; names-only
    "shadow-of-death":          {"status": "names-only"},   # Ps 23:4; Matt 4:16; covered under "psalms"
    "shady-trees":              {"status": "names-only"},   # Job 40:21 KJV (behemoth); brief
    "shaft":                    {"status": "names-only"},   # Exod 25:31 lampstand; Isa 49:2; lexical
    "shagee":                   {"status": "names-only"},   # David's mighty men (1 Chr 11:34); minor
    "shahapaim":                {"status": "names-only"},   # Benjaminite (1 Chr 8:8); minor
    "shahazumah":               {"status": "names-only"},   # Issachar's border (Josh 19:22); place
    "shalishah-land-of":        {"status": "names-only"},   # 1 Sam 9:4; place; minor
    "shallecheth-the-gate":     {"status": "names-only"},   # 1 Chr 26:16 Jerusalem gate; place
    "shallum-1":                {"status": "names-only"},   # ISBE disambiguation; covered under "shallum"
    "shallum-2":                {"status": "names-only"},   # ISBE disambiguation; minor
    "shamai":                   {"status": "names-only"},   # Judahite (1 Chr 2:28,32); minor
    "shambles":                 {"status": "names-only"},   # 1 Cor 10:25 KJV "meat market"; archaic
    "shame":                    {"status": "names-only"},   # covered under "shame" in Easton; names-only
    "shamefacedness":           {"status": "names-only"},   # 1 Tim 2:9 KJV "modesty"; archaic
    "shamefastness":            {"status": "names-only"},   # variant of shamefacedness; archaic
    "shamir-1":                 {"status": "names-only"},   # Judah town (Josh 15:48); place
    "shamir-2":                 {"status": "names-only"},   # Ephraim town (Judg 10:1-2); place
    "shamlai":                  {"status": "names-only"},   # post-exilic temple servant (Neh 7:48); minor
    "shammua;-shammuah":        {"status": "names-only"},   # ISBE compound; minor figures; names-only
    "shape":                    {"status": "names-only"},   # lexical
    "shaphir":                  {"status": "names-only"},   # Mic 1:11 town; place
    "share":                    {"status": "names-only"},   # lexical; also agricultural implement
    "shaul;-shaulites":         {"status": "names-only"},   # ISBE compound; son of Simeon (Gen 46:10); minor
    "shaveh-vale-of":           {"status": "names-only"},   # Gen 14:17 King's Dale; place
    "shaving":                  {"status": "names-only"},   # Num 8:7; Ezek 44:20; cultural; brief
    "shawl":                    {"status": "names-only"},   # Isa 3:22; cultural; brief
    "sheaf;-sheaves":           {"status": "names-only"},   # ISBE compound; Ruth 2; covered under "harvest"
    "shear":                    {"status": "names-only"},   # lexical
    "shearing-house":           {"status": "names-only"},   # 2 Kgs 10:12,14 KJV; place
    "sheath":                   {"status": "names-only"},   # 2 Sam 20:8; John 18:11; lexical
    "sheba-1":                  {"status": "names-only"},   # ISBE disambiguation; son of Raamah (Gen 10:7); minor
    "sheba-2":                  {"status": "names-only"},   # ISBE disambiguation; son of Joktan (Gen 10:28); minor
    # ISBE entry; redirect to canonical Sheba article (which covers the queen's visit)
    "sheba-queen-of":           {"status": "redirect-only", "redirect_to": "sheba"},
    "shebat":                   {"status": "names-only"},   # Hebrew month; covered under "months"
    "shecaniah;-shechaniah":    {"status": "names-only"},   # ISBE compound; post-exilic figures; minor
    "shechemites":              {"status": "names-only"},   # Num 26:31; minor
    "shed-shedding":            {"status": "names-only"},   # KJV "pour out/spill"; lexical
    "sheep-gate":               {"status": "names-only"},   # Neh 3:1 Jerusalem gate; place; covered under "Nehemiah"
    "sheep-market":             {"status": "names-only"},   # John 5:2 KJV; covered under "Bethesda"
    "sheep-tending":            {"status": "names-only"},   # general; covered under "shepherd"
    "sheep-master":             {"status": "names-only"},   # 2 Kgs 3:4 KJV; covered under "Mesha"
    "sheep-shearing":           {"status": "names-only"},   # Gen 31:19; 38:12; cultural; brief
    "sheepcote;-sheepfold":     {"status": "names-only"},   # ISBE compound; John 10:1; covered under "shepherd"
    "sheepskin":                {"status": "names-only"},   # Heb 11:37; brief
    "sheerah":                  {"status": "names-only"},   # 1 Chr 7:24; Ephraimite woman; minor
    "sheet":                    {"status": "names-only"},   # Acts 10:11; Judg 14:12-13; lexical
    "shekel-of-the-kings-weight-royal-shekel": {"status": "names-only"},  # 2 Sam 14:26; covered under "weights"
    "shekel-of-the-sanctuary;-sacred-shekel": {"status": "names-only"},   # Exod 30:13; covered under "shekel"
    # Hebrew שְׁכִינָה; not in Scripture itself but derived from "to dwell" (shakan);
    # God's manifest presence: pillar of cloud/fire (Exod 13:21); glory filling tabernacle
    # (Exod 40:34-38) and temple (1 Kgs 8:10-11); departure (Ezek 10:18); John 1:14
    # "dwelt among us" (ἐσκήνωσεν); return in New Jerusalem (Rev 21:3); essential theological concept
    "shekinah":                 {"status": "stub-needed"},
    "shelanites":               {"status": "names-only"},   # Num 26:20; minor
    "shema-1":                  {"status": "names-only"},   # Judahite (1 Chr 2:43-44); minor
    "shema-2":                  {"status": "names-only"},   # post-exilic figure (Neh 8:4); minor
    "shemed":                   {"status": "names-only"},   # Benjaminite (1 Chr 8:12); minor
    "shemida;-shemidah;-shemidaites": {"status": "names-only"},  # ISBE compound; Manassite (Num 26:32); minor
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
    print(f'BPG Curation C66: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
