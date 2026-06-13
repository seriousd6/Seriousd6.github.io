"""
BPG Curation — Batch C58: noah-book-apocalypse-of → oreb;-zeeb (gaps 5804–5908)
Gaps reviewed: 105 (score-5 isbe-scholarly N–O entries)

Score-5 ISBE posture: ~90% names-only. Notable stubs: offices-of-christ (munus triplex),
obedience-of-christ (active/passive obedience), omnipotence/omnipresence/omniscience
(divine attributes), old-testament-canon, old-testament-languages, only-begotten (monogenes).
8 stub-needed; 4 redirects; 93 names-only.

Script: scripts/bpg-curate-58.py
Run: python3 scripts/bpg-curate-58.py  (from project root)
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
    "noah-book-apocalypse-of":  {"status": "names-only"},   # pseudepigraphical; not canonical
    "nobai":                    {"status": "names-only"},   # post-exilic signatory (Neh 10:19); minor
    "noble;-nobles;-nobleman":  {"status": "names-only"},   # KJV lexical; covered under "princes"
    "noeba":                    {"status": "names-only"},   # apocryphal (1 Esd 5:31)
    "noise":                    {"status": "names-only"},   # lexical
    "noisome":                  {"status": "names-only"},   # KJV "harmful/noxious" (Ps 91:3; Rev 16:2); archaic
    "nooma":                    {"status": "names-only"},   # apocryphal
    "noon;-noonday":            {"status": "names-only"},   # KJV time reference; lexical
    "north;-north-country":     {"status": "names-only"},   # geographic direction; covered under geography articles
    "northeast-southeast":      {"status": "names-only"},   # KJV nautical direction (Acts 27:12,14); lexical
    "nose;-nostrils":           {"status": "names-only"},   # anatomical; lexical
    "notable":                  {"status": "names-only"},   # KJV "famous" (Dan 8:5; Acts 2:20); lexical
    "note":                     {"status": "names-only"},   # lexical
    "nothing":                  {"status": "names-only"},   # lexical
    "nought":                   {"status": "names-only"},   # KJV "nothing"; archaic
    "nourish":                  {"status": "names-only"},   # lexical
    "novice":                   {"status": "names-only"},   # 1 Tim 3:6 KJV "not a novice"; lexical
    "number-golden":            {"status": "names-only"},   # ecclesiastical calendar; too specialized
    "numbering":                {"status": "names-only"},   # census; covered under "census"
    "numenius":                 {"status": "names-only"},   # Maccabean envoy (1 Macc 12:16); apocryphal
    "nun-1":                    {"status": "names-only"},   # Joshua's father; covered under "Joshua"
    "nun-2":                    {"status": "names-only"},   # Hebrew letter; covered under "Hebrew alphabet"
    "nurse;-nursing":           {"status": "names-only"},   # 2 Sam 4:4; Ruth 4:16; cultural; brief
    "nurture":                  {"status": "names-only"},   # Eph 6:4 KJV "nurture and admonition"; lexical
    "oabdius":                  {"status": "names-only"},   # apocryphal (1 Esd 8:32)
    "oak-of-tabor":             {"status": "names-only"},   # 1 Sam 10:3; place reference; brief
    "oar":                      {"status": "names-only"},   # Ezek 27:6; nautical; brief
    "obdia":                    {"status": "names-only"},   # apocryphal variant of Obadiah
    # Christ's active obedience (law-keeping, Rom 5:19) and passive obedience (suffering, Phil 2:8);
    # imputed righteousness of Christ; distinct from general "obedience" concept;
    # core to Reformed soteriology: Christ obeyed in our place so we are counted righteous
    "obedience-of-christ":      {"status": "stub-needed"},
    # ISBE compound form; redirect to canonical Easton article
    "obedience;-obey":          {"status": "redirect-only", "redirect_to": "obedience"},
    "obelisk":                  {"status": "names-only"},   # Jer 43:13 KJV "images"; archaeological
    "obeth":                    {"status": "names-only"},   # apocryphal (1 Esd 8:32)
    "object":                   {"status": "names-only"},   # lexical
    "obscurity":                {"status": "names-only"},   # lexical
    "observe":                  {"status": "names-only"},   # lexical
    "observer-of-times":        {"status": "names-only"},   # Deut 18:10; divination; covered under "divination"
    "obstinacy":                {"status": "names-only"},   # lexical; covered under "hardness of heart"
    "occasion":                 {"status": "names-only"},   # lexical
    "occupy":                   {"status": "names-only"},   # KJV "trade/use" (Luke 19:13); archaic
    "occurrent":                {"status": "names-only"},   # KJV "occurrence" (1 Kgs 5:4); archaic
    "ochielus":                 {"status": "names-only"},   # apocryphal (1 Esd 8:32)
    "ochran":                   {"status": "names-only"},   # Num 1:13 father of Pagiel; minor
    "ochre-red":                {"status": "names-only"},   # pigment; general
    "ocidelus":                 {"status": "names-only"},   # apocryphal
    "ocina":                    {"status": "names-only"},   # coastal city; apocryphal
    "odes-of-solomon":          {"status": "names-only"},   # pseudepigraphical; too specialized
    "odomera":                  {"status": "names-only"},   # apocryphal commander (1 Macc 9:66)
    "odor":                     {"status": "names-only"},   # incense/fragrance; covered under "incense"
    "of":                       {"status": "names-only"},   # lexical preposition; no article needed
    "offence;-offend":          {"status": "names-only"},   # ISBE compound; covered under "offence"
    # ISBE compound; redirect to canonical offerings article
    "offer;-offering":          {"status": "redirect-only", "redirect_to": "offerings"},
    "office":                   {"status": "names-only"},   # lexical; covered under specific church offices
    # Christ's threefold office (munus triplex): Prophet (Deut 18:15; Acts 3:22), Priest (Heb 7:17),
    # King (Ps 2:6; Luke 1:33); Westminster Shorter Catechism Q.23; Calvin's Institutes;
    # essential framework for understanding all of Christ's saving work
    "offices-of-christ":        {"status": "stub-needed"},
    "offscouring":              {"status": "names-only"},   # KJV "refuse" (1 Cor 4:13; Lam 3:45); lexical
    "offspring":                {"status": "names-only"},   # lexical; genealogical reference
    "often":                    {"status": "names-only"},   # lexical
    "oholah":                   {"status": "names-only"},   # Ezek 23; symbolic name for Samaria; covered under Ezekiel
    "oholiab":                  {"status": "names-only"},   # tabernacle craftsman (Exod 31:6); minor
    "oholibah":                 {"status": "names-only"},   # Ezek 23; symbolic for Jerusalem; covered under Ezekiel
    "oholibamah":               {"status": "names-only"},   # Esau's wife (Gen 36:2,5); minor
    "oil-press":                {"status": "names-only"},   # Gethsemane etymology; covered under "Gethsemane"
    "oil-anointing":            {"status": "names-only"},   # covered under "anointing" and "anointing oil"
    "oil-beaten":               {"status": "names-only"},   # Exod 27:20 KJV; type of olive oil; brief
    "oil-holy":                 {"status": "names-only"},   # covered under "anointing oil"
    "oil-olive":                {"status": "names-only"},   # general; covered under "olive" and "oil"
    "oil-making":               {"status": "names-only"},   # covered under "olive"
    "olamus":                   {"status": "names-only"},   # apocryphal (1 Esd 9:30)
    "old":                      {"status": "names-only"},   # lexical
    "old-man":                  {"status": "names-only"},   # Rom 6:6; Eph 4:22 KJV; covered under "sanctification"
    "old-prophet-the":          {"status": "names-only"},   # 1 Kgs 13:11-32; minor narrative figure
    # Formation of the OT canon: Torah recognized first, Prophets (~400 BC), Writings debated
    # to Council of Jamnia (90 AD); 39 books in Protestant canon; 46 in Catholic (+ Apocrypha);
    # Septuagint's wider canon; Dead Sea Scrolls evidence; essential for understanding Scripture's authority
    "old-testament-canon":      {"status": "stub-needed"},
    # Biblical Hebrew (prose and poetry), Biblical Aramaic (Dan 2:4b–7:28; Ezra 4:8–6:18; Jer 10:11);
    # Semitic language family; Masoretic pointing; key for understanding OT word studies;
    # critical background for any serious Bible student
    "old-testament-languages":  {"status": "stub-needed"},
    "oleaster":                 {"status": "names-only"},   # Isa 41:19 KJV "oil tree"; botanical
    "olive-berries":            {"status": "names-only"},   # Jas 3:12; covered under "olive"
    "olive-tree":               {"status": "names-only"},   # ISBE entry; covered under "olive"
    "olive-yard":               {"status": "names-only"},   # Neh 5:11; covered under "olive"
    "olive-grafted":            {"status": "names-only"},   # Rom 11:17-24; covered under "olive"
    "olive-wild":               {"status": "names-only"},   # Rom 11:17; covered under "olive"
    "olympius":                 {"status": "names-only"},   # Zeus Olympios (2 Macc 6:2); apocryphal
    "omaerus":                  {"status": "names-only"},   # apocryphal
    "omens":                    {"status": "names-only"},   # covered under "divination" and "superstition"
    # God's all-powerfulness: "Is anything too hard for the LORD?" (Gen 18:14); "I am God Almighty"
    # (Gen 17:1); Rev 19:6 "the Lord God omnipotent reigneth"; limited by his own nature (cannot lie);
    # essential divine attribute for understanding prayer and miracles
    "omnipotence":              {"status": "stub-needed"},
    # God's universal presence: "Where can I go from your Spirit?" (Ps 139:7-10); "Do I not fill
    # heaven and earth?" (Jer 23:24); distinguished from pantheism; Spirit's indwelling (1 Cor 3:16);
    # distinct from omnipotence (power) and omniscience (knowledge)
    "omnipresence":             {"status": "stub-needed"},
    # God's all-knowingness: "he knows the secrets of the heart" (Ps 44:21); "known to God from
    # eternity" (Acts 15:18); foreknowledge and predestination (Rom 8:29); Arminian/Calvinist
    # debate on foreknowledge; essential divine attribute for theodicy and assurance
    "omniscience":              {"status": "stub-needed"},
    "on-1":                     {"status": "names-only"},   # Egyptian city Heliopolis (Gen 41:45); place
    "on-2":                     {"status": "names-only"},   # Reubenite (Num 16:1); minor
    "one":                      {"status": "names-only"},   # lexical
    "oniares":                  {"status": "names-only"},   # apocryphal
    "onions":                   {"status": "names-only"},   # Num 11:5; Egyptian food; covered under "food"
    # Greek monogenes (μονογενής): "one of a kind/unique" (John 1:14,18; 3:16,18; 1 John 4:9);
    # Nicene debate: "begotten, not made" vs. Arian "first-created"; Heb 11:17 applied to Isaac;
    # critical Christological term for Trinity doctrine
    "only-begotten":            {"status": "stub-needed"},
    "onus":                     {"status": "names-only"},   # KJV archaic; lexical
    "open":                     {"status": "names-only"},   # lexical
    "operation":                {"status": "names-only"},   # lexical
    "opinion":                  {"status": "names-only"},   # lexical
    "opobalsamum":              {"status": "names-only"},   # balm of Gilead; covered under "balm"
    "oppression":               {"status": "names-only"},   # OT prophetic theme; covered under "justice" and "poor"
    "or":                       {"status": "names-only"},   # lexical conjunction; no article
    "oracles-sibylline":        {"status": "names-only"},   # pseudepigraphical; too specialized
    "orator;-ortion":           {"status": "names-only"},   # Acts 24:1 Tertullus; lexical
    # ISBE compound; redirect to canonical ordination article
    "ordain;-ordination":       {"status": "redirect-only", "redirect_to": "ordination"},
    "order":                    {"status": "names-only"},   # lexical
    "ordinance":                {"status": "names-only"},   # KJV "statute/decree"; covered under "law"
    "ordinances-of-heaven":     {"status": "names-only"},   # Jer 33:25; astronomical laws; poetic/lexical
    "ordination":               {"status": "names-only"},   # covered in Easton/Smith
    # ISBE compound; Midianite princes (Judg 7:25; Ps 83:11); redirect to canonical Oreb article
    "oreb;-zeeb":               {"status": "redirect-only", "redirect_to": "oreb"},
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
    print(f'BPG Curation C58: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
