"""
BPG Curation — Batch C64: rod → sanctity-legislation-of (gaps ~6419–6523)
Gaps reviewed: 105 (score-5 isbe-scholarly R–S entries)

Score-5 ISBE posture: ~95% names-only (many apocryphal/variant names in this stretch).
One notable stub: sacraments (baptism and Lord's Supper; Protestant/Catholic/Orthodox debate).
1 stub-needed; 4 redirects; 100 names-only.

Script: scripts/bpg-curate-64.py
Run: python3 scripts/bpg-curate-64.py  (from project root)
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
    "rod":                      {"status": "names-only"},   # Ps 23:4; covered under "rod" in Easton
    "rodanim":                  {"status": "names-only"},   # Gen 10:4 variant (1 Chr 1:7); minor
    "roimus":                   {"status": "names-only"},   # apocryphal (1 Esd 2:16)
    "roll-scroll":              {"status": "names-only"},   # ISBE compound; covered under "book" and "scroll"
    "roller":                   {"status": "names-only"},   # Ezek 30:24 KJV; archaic
    "rolling-thing":            {"status": "names-only"},   # Isa 17:13 KJV; archaic
    "roman-army":               {"status": "names-only"},   # NT background; covered under "rome" and "soldier"
    "roman-empire-and-christianity": {"status": "names-only"},  # broad background; covered under "rome"
    "roman-law":                {"status": "names-only"},   # NT background; covered under "rome"
    "roman-religion":           {"status": "names-only"},   # Greco-Roman religion; background; names-only
    # ISBE compound; redirect to canonical Romans/Rome article
    "roman;-romans":            {"status": "redirect-only", "redirect_to": "rome"},
    "roof-chamber":             {"status": "names-only"},   # upper room; covered under "upper room"
    "root":                     {"status": "names-only"},   # lexical; metaphorical
    "root-of-david":            {"status": "names-only"},   # Rev 5:5; 22:16; covered under "messiah"
    "root-of-jesse":            {"status": "names-only"},   # Isa 11:10; Rom 15:12; covered under "messiah"
    "rope":                     {"status": "names-only"},   # KJV "cord"; Isa 5:18; lexical
    "rosh-1":                   {"status": "names-only"},   # Benjaminite (Gen 46:21); minor
    "rosh-2":                   {"status": "names-only"},   # Ezek 38:2-3; covered under "gog"
    "rot;-rottenness":          {"status": "names-only"},   # Num 5:21-22; lexical
    "rote":                     {"status": "names-only"},   # KJV "by rote" (Isa 29:13); archaic
    "rower;-rowing":            {"status": "names-only"},   # Ezek 27:26; nautical; brief
    "royal":                    {"status": "names-only"},   # lexical
    "royal-city":               {"status": "names-only"},   # 1 Sam 27:5; covered under specific cities
    "rudder;-rudder-bands":     {"status": "names-only"},   # ISBE compound; Acts 27:40; nautical; brief
    "ruddy":                    {"status": "names-only"},   # 1 Sam 16:12 (David); lexical
    "rude":                     {"status": "names-only"},   # 2 Cor 11:6 KJV; archaic
    "rudiments":                {"status": "names-only"},   # Col 2:8 "stoicheia"; covered under "elements"
    "rug":                      {"status": "names-only"},   # Judg 4:18 KJV (Jael's mantle); archaic
    "ruin":                     {"status": "names-only"},   # lexical
    "ruler":                    {"status": "names-only"},   # lexical; general
    "ruler-of-the-feast":       {"status": "names-only"},   # John 2:8-9; covered under "Cana"
    "ruler-of-the-synagogue":   {"status": "names-only"},   # Luke 8:41 (Jairus); covered under "synagogue"
    "rulers-of-the-city":       {"status": "names-only"},   # Acts 17:6 "politarchs"; covered under "politarch"
    "rump":                     {"status": "names-only"},   # Exod 29:22 KJV "fat tail"; archaic
    "runagate":                 {"status": "names-only"},   # Ps 68:6 KJV "fugitive"; archaic
    "runner":                   {"status": "names-only"},   # 1 Kgs 14:27 royal messenger; brief
    "rust":                     {"status": "names-only"},   # Matt 6:19-20; Jas 5:3; lexical
    "sabaco;-sabakon":          {"status": "names-only"},   # Ethiopian pharaoh; mainly historical
    "sabaeans":                 {"status": "names-only"},   # Job 1:15; covered under "sheba"
    "sabanneus":                {"status": "names-only"},   # apocryphal (1 Esd 9:33)
    "sabannus":                 {"status": "names-only"},   # apocryphal
    "sabat":                    {"status": "names-only"},   # apocryphal
    "sabateus":                 {"status": "names-only"},   # apocryphal
    "sabathus":                 {"status": "names-only"},   # apocryphal
    "sabatus":                  {"status": "names-only"},   # apocryphal
    "sabban":                   {"status": "names-only"},   # apocryphal
    "sabbateus":                {"status": "names-only"},   # apocryphal
    "sabbath-court-of-the":     {"status": "names-only"},   # 2 Kgs 16:18; place reference; minor
    "sabbath-day-before-the":   {"status": "names-only"},   # liturgical calendar; brief
    "sabbath-morrow-after-the": {"status": "names-only"},   # Lev 23:11,15 firstfruits; covered under "sabbath"
    "sabbath-second-after-the-first": {"status": "names-only"},  # Luke 6:1; textual note; covered under "sabbath"
    "sabbath-breaking":         {"status": "names-only"},   # Num 15:32-36; covered under "sabbath"
    "sabbatheus":               {"status": "names-only"},   # apocryphal
    "sabbaths-of-years":        {"status": "names-only"},   # Lev 25:8 Jubilee; covered under "sabbatical year"
    "sabbeus":                  {"status": "names-only"},   # apocryphal
    "sabi":                     {"status": "names-only"},   # apocryphal
    "sabias":                   {"status": "names-only"},   # apocryphal
    "sabie":                    {"status": "names-only"},   # apocryphal
    "sabta;-sabtah":            {"status": "names-only"},   # ISBE compound; son of Cush (Gen 10:7); minor
    "sabteca":                  {"status": "names-only"},   # son of Cush (Gen 10:7); minor
    # Ordinances of the church: baptism (Matt 28:19; Rom 6:3-4) and Lord's Supper (1 Cor 11:23-26);
    # Protestant view: 2 sacraments as signs/seals of grace; Catholic: 7 sacraments as effective
    # means of grace; Orthodox: "mysteries"; Baptist: ordinances only (symbolic); key for
    # understanding ecclesiology, baptismal regeneration debate, and real presence debate
    "sacraments":               {"status": "stub-needed"},
    "sacrifice-human":          {"status": "names-only"},   # Jephthah; Molech; covered under "sacrifice"
    "sacrilege":                {"status": "names-only"},   # Rom 2:22; covered under "temple" and "idolatry"
    "sadamias":                 {"status": "names-only"},   # apocryphal (1 Esd 8:60)
    "sadas":                    {"status": "names-only"},   # apocryphal
    "saddeus":                  {"status": "names-only"},   # apocryphal
    "saddle":                   {"status": "names-only"},   # Gen 22:3; Num 22:21; brief; cultural
    "sadduk":                   {"status": "names-only"},   # apocryphal variant of Zadok
    "sail;-sailor":             {"status": "names-only"},   # ISBE compound; Acts 27; names-only
    "saints":                   {"status": "names-only"},   # covered under "saints" in Easton
    "sala-salah":               {"status": "names-only"},   # ISBE compound; Luke 3:35; minor genealogy
    "salamiel":                 {"status": "names-only"},   # apocryphal
    "salasadai":                {"status": "names-only"},   # apocryphal
    "sale":                     {"status": "names-only"},   # lexical
    "salecah;-salcah-salchah":  {"status": "names-only"},   # ISBE compound; Bashan city (Deut 3:10); place
    "salem-1":                  {"status": "names-only"},   # Jerusalem variant; covered under "salem"
    "salem-2":                  {"status": "names-only"},   # ISBE disambiguation; names-only
    "salemas":                  {"status": "names-only"},   # apocryphal
    "salimoth":                 {"status": "names-only"},   # ISBE variant; minor
    "sallumus":                 {"status": "names-only"},   # apocryphal variant of Shallum
    "salmai":                   {"status": "names-only"},   # post-exilic temple servant (Neh 7:48); minor
    # KJV variant of Shalmaneser; redirect to canonical article
    "salmanasar":               {"status": "redirect-only", "redirect_to": "shalmaneser"},
    "salmon;-salma":            {"status": "names-only"},   # ISBE compound; father of Boaz; covered under "salmon"
    "saloas":                   {"status": "names-only"},   # apocryphal
    "salom":                    {"status": "names-only"},   # apocryphal
    "salt-covenant-of":         {"status": "names-only"},   # Num 18:19; covered under "covenant" and "salt"
    "salt-pillar-of":           {"status": "names-only"},   # Gen 19:26 Lot's wife; covered under "lot"
    "salt-wort":                {"status": "names-only"},   # Job 30:4 KJV; botanical; brief
    "salum":                    {"status": "names-only"},   # apocryphal variant of Shallum
    "samael":                   {"status": "names-only"},   # apocryphal angel name; Jewish pseudepigrapha
    "samaias":                  {"status": "names-only"},   # apocryphal
    # ISBE entry on Samaria city; redirect to canonical Samaria article
    "samaria-city-of":          {"status": "redirect-only", "redirect_to": "samaria"},
    "samatus":                  {"status": "names-only"},   # apocryphal
    "samech":                   {"status": "names-only"},   # Hebrew letter; covered under "Hebrew alphabet"
    "sameius":                  {"status": "names-only"},   # apocryphal
    "samellius":                {"status": "names-only"},   # apocryphal
    "sameus":                   {"status": "names-only"},   # apocryphal
    "sami":                     {"status": "names-only"},   # apocryphal
    "samis":                    {"status": "names-only"},   # apocryphal
    "sammus":                   {"status": "names-only"},   # apocryphal
    "sampsames":                {"status": "names-only"},   # apocryphal
    "sanaas":                   {"status": "names-only"},   # apocryphal (1 Esd 5:23)
    # ISBE compound; variant spellings of Sheshbazzar; redirect to canonical article
    "sanabassar;-sanabassarus": {"status": "redirect-only", "redirect_to": "sheshbazzar"},
    "sanasib":                  {"status": "names-only"},   # apocryphal
    "sanctity-legislation-of":  {"status": "names-only"},   # ISBE "Holiness Code" (Lev 17-26); too specialized
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
    print(f'BPG Curation C64: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
