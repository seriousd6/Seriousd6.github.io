"""
BPG Curation — Batch C62: prologue → rearward (gaps ~6214–6318)
Gaps reviewed: 105 (score-5 isbe-scholarly P–R entries)

Score-5 ISBE posture: ~90% names-only. Notable stubs: psalms-imprecatory (major
devotional/hermeneutical debate), punishment-everlasting (ECT vs annihilationism),
purpose-of-god (divine election/predestination), quotations-in-the-new-testament (NT use of OT).
4 stub-needed; 10 redirects; 91 names-only.

Script: scripts/bpg-curate-62.py
Run: python3 scripts/bpg-curate-62.py  (from project root)
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
    "prologue":                 {"status": "names-only"},   # lexical; brief
    "prolong":                  {"status": "names-only"},   # KJV "extend/lengthen"; lexical
    "promise":                  {"status": "names-only"},   # covered under "promises" in Easton
    "proper":                   {"status": "names-only"},   # lexical
    "proper-names":             {"status": "names-only"},   # covered under "names" in Easton
    "property":                 {"status": "names-only"},   # lexical; general
    "prophecy-gift-of":         {"status": "names-only"},   # covered under "prophecy" and "gifts of the Spirit"
    # ISBE compound; redirect to canonical Prophecy article
    "prophecy;-prophets":       {"status": "redirect-only", "redirect_to": "prophecy"},
    "prophesyings-false":       {"status": "names-only"},   # covered under "prophets, false"
    "prophet-the-old":          {"status": "names-only"},   # 1 Kgs 13:11-32 minor narrative figure
    "prophetess":               {"status": "names-only"},   # Miriam, Deborah, Huldah; covered under "prophecy"
    "proportion":               {"status": "names-only"},   # Rom 12:6 KJV "proportion of faith"; lexical
    "proseuche;-proseucha":     {"status": "names-only"},   # Greek "place of prayer"; covered under "synagogue"
    "prostitution":             {"status": "names-only"},   # covered under "harlot" in Easton
    "prostration":              {"status": "names-only"},   # worship posture; covered under "worship"
    "protevangelium-of-james":  {"status": "names-only"},   # apocryphal gospel; too specialized
    "prove":                    {"status": "names-only"},   # KJV "test/try"; lexical
    "provender":                {"status": "names-only"},   # KJV "fodder" for animals (Gen 24:25); archaic
    # ISBE compound; redirect to canonical Proverbs article
    "proverbs-the-book-of":     {"status": "redirect-only", "redirect_to": "proverbs"},
    "provocation;-provoke":     {"status": "names-only"},   # KJV lexical; covered under "anger"
    "prudence;-prudent":        {"status": "names-only"},   # Prov 8:12; covered under "wisdom"
    "pruning-hook":             {"status": "names-only"},   # Isa 2:4; Mic 4:3; agricultural; brief
    # Psalms calling for divine judgment on enemies (Ps 35, 55, 58, 69, 83, 109, 137);
    # "Pour out your wrath on them" (Ps 69:24); "Happy is he who dashes your infants against
    # the rocks" (Ps 137:9); theological debate: prophetic curse, Christ's voice, how Christians
    # should pray; Luther, Calvin, Bonhoeffer, Stott on using them; major pastoral/hermeneutical issue
    "psalms-imprecatory":       {"status": "stub-needed"},
    "psalter-psalms-of-solomon": {"status": "names-only"},  # pseudepigraphical; too specialized
    "psaltiel":                 {"status": "names-only"},   # apocryphal (1 Esd 5:8)
    "pseudo-matthew-gospel-of": {"status": "names-only"},   # apocryphal; not canonical
    "psychology":               {"status": "names-only"},   # general/philosophical; not a biblical article
    "ptolemy":                  {"status": "names-only"},   # general; covered under individual Ptolemies
    "puah;-puvah":              {"status": "names-only"},   # ISBE compound; covered under "pua" in Easton
    "puhites":                  {"status": "names-only"},   # Levite clan (1 Chr 2:53); minor
    # Matt 25:46 "eternal punishment"; 2 Thess 1:9 "everlasting destruction"; Rev 20:10,14-15;
    # debate: eternal conscious torment (ECT) vs annihilationism (conditional immortality) vs
    # universalism; Gehenna imagery; Augustine vs Arnobius; C.S. Lewis vs John Stott;
    # central to eschatology and theodicy
    "punishment-everlasting":   {"status": "stub-needed"},
    "purah":                    {"status": "names-only"},   # Gideon's servant (Judg 7:10-11); minor
    "purchase":                 {"status": "names-only"},   # KJV "redeem/acquire"; covered under "redemption"
    "pure;-purely;-purity":     {"status": "names-only"},   # ISBE compound; lexical; covered under "holiness"
    "purge":                    {"status": "names-only"},   # KJV "cleanse/purify"; lexical
    # ISBE compound; redirect to canonical Purim article
    "purim;-pur":               {"status": "redirect-only", "redirect_to": "purim"},
    "purity":                   {"status": "names-only"},   # covered under "holiness" in Easton
    "purloining":               {"status": "names-only"},   # Tit 2:10 KJV "stealing"; archaic
    "purple":                   {"status": "names-only"},   # Num 4:13; Rev 17:4; covered under "colors"
    # Rom 8:28-30 "called according to his purpose"; Eph 1:11 "works all things after the counsel
    # of his will"; Acts 2:23 "delivered up by the definite plan and foreknowledge of God";
    # divine decree, election, predestination; distinction from fate/determinism; essential
    # for understanding Reformed soteriology and theodicy
    "purpose-of-god":           {"status": "stub-needed"},
    "purslain;-juice":          {"status": "names-only"},   # KJV botanical; archaic
    "purtenance":               {"status": "names-only"},   # Exod 12:9 KJV "entrails"; archaic
    "puthites":                 {"status": "names-only"},   # Judahite clan (1 Chr 2:53); minor
    # ISBE variant spelling; redirect to canonical Pua article
    "puvah":                    {"status": "redirect-only", "redirect_to": "pua"},
    "pyramid":                  {"status": "names-only"},   # general; ancient Near East; not a biblical article
    "python":                   {"status": "names-only"},   # Acts 16:16 divination spirit; covered under "divination"
    # ISBE compound; redirect to canonical Kir-haraseth article
    "qir-hareseth;-kir-heres":  {"status": "redirect-only", "redirect_to": "kir-haraseth"},
    "qoph":                     {"status": "names-only"},   # Hebrew letter; covered under "Hebrew alphabet"
    "quail":                    {"status": "names-only"},   # Exod 16:13; Num 11:31; covered under "quails"
    "quarrel":                  {"status": "names-only"},   # lexical
    "quarter":                  {"status": "names-only"},   # lexical
    "queen-mother":             {"status": "names-only"},   # "gebirah"; Bathsheba, Athaliah; covered under specific queens
    # Redirect to canonical Queen of Sheba article
    "queen-of-sheba":           {"status": "redirect-only", "redirect_to": "sheba"},
    "quench":                   {"status": "names-only"},   # lexical
    "question":                 {"status": "names-only"},   # lexical
    "quick;-quicken":           {"status": "names-only"},   # KJV "alive/make alive" (Ps 71:20); archaic/lexical
    "quiet":                    {"status": "names-only"},   # lexical
    "quintus-memmius":          {"status": "names-only"},   # Roman official (2 Macc 11:34); apocryphal
    # Lk 2:2 "first registration when Quirinius was governor"; redirect to canonical Cyrenius article
    "quirinius":                {"status": "redirect-only", "redirect_to": "cyrenius"},
    "quit":                     {"status": "names-only"},   # KJV "acquit/be free" (1 Cor 16:13); archaic
    # How NT authors cite OT: formula quotations, typology, midrash, pesher;
    # "fulfillment" language (Matt 1:22-23); Paul's use of Habakkuk (Rom 1:17; Gal 3:11);
    # verbatim vs. interpretive citations; LXX vs MT; essential for understanding NT exegesis
    "quotations-in-the-new-testament": {"status": "stub-needed"},
    "raama":                    {"status": "names-only"},   # son of Cush (Gen 10:7); minor
    # ISBE compound; redirect to canonical Rameses article
    "raamses;-rameses":         {"status": "redirect-only", "redirect_to": "rameses"},
    "rabble":                   {"status": "names-only"},   # Num 11:4 "mixed multitude"; covered under "mingled-people"
    "racal":                    {"status": "names-only"},   # 1 Sam 30:29 place in Judah; place
    "races":                    {"status": "names-only"},   # 1 Cor 9:24; Heb 12:1 athletic metaphor; lexical
    "rachels-tomb":             {"status": "names-only"},   # Gen 35:19; Jer 31:15; covered under "Rachel"
    "radiant":                  {"status": "names-only"},   # lexical
    "raft":                     {"status": "names-only"},   # 1 Kgs 5:9; 2 Chr 2:16; nautical; brief
    "rafter":                   {"status": "names-only"},   # Song 1:17 KJV "beams"; architectural; brief
    "rag":                      {"status": "names-only"},   # KJV "torn cloth" (Isa 64:6); lexical
    "rages;-ragau":             {"status": "names-only"},   # apocryphal city (Tobit 1:14); apocryphal
    "raguel-1":                 {"status": "names-only"},   # Num 10:29 variant of Jethro; covered under "Jethro"
    "raguel-2":                 {"status": "names-only"},   # Tobit's father-in-law (Tobit 3:7); apocryphal
    "raid":                     {"status": "names-only"},   # lexical; brief
    "rail;-railing;-railer":    {"status": "names-only"},   # KJV "revile/mock" (2 Kgs 18:23); lexical
    "raiment":                  {"status": "names-only"},   # KJV "garment/clothing"; covered under "dress"
    "raiment-soft":             {"status": "names-only"},   # Matt 11:8 KJV; lexical
    "rainfall-in-jerusalem-in-inches": {"status": "names-only"},  # meteorological data; too specialized
    "raise":                    {"status": "names-only"},   # lexical; covered under "resurrection"
    "raisin-cakes":             {"status": "names-only"},   # 2 Sam 6:19; Hos 3:1; cultural; brief
    "ram-1":                    {"status": "names-only"},   # Judahite ancestor (Ruth 4:19); minor
    "ram-2":                    {"status": "names-only"},   # son of Jerahmeel (1 Chr 2:25); minor
    "rams-horn":                {"status": "names-only"},   # shofar (Josh 6:4); covered under "trumpet"
    "ram-battering":            {"status": "names-only"},   # siege warfare; covered under "siege" and "war"
    # ISBE compound; redirect to canonical Ramah article
    "ramathaim;-ramathem":      {"status": "redirect-only", "redirect_to": "ramah"},
    "ramoth-1":                 {"status": "names-only"},   # Ramoth-gilead; covered under "ramoth-gilead"
    "ramoth-2":                 {"status": "names-only"},   # post-exilic man (Ezra 10:29); minor
    "ramoth-3":                 {"status": "names-only"},   # Issachar town (1 Chr 6:73); place
    "rampart":                  {"status": "names-only"},   # KJV "wall/bulwark" (Lam 2:8); lexical
    "rams-skins":               {"status": "names-only"},   # Exod 25:5 tabernacle; covered under "tabernacle"
    "range":                    {"status": "names-only"},   # lexical
    "rank":                     {"status": "names-only"},   # lexical
    "ranks":                    {"status": "names-only"},   # lexical; military
    "rape":                     {"status": "names-only"},   # 2 Sam 13 Tamar; covered under specific narratives
    "rapha-raphah":             {"status": "names-only"},   # Benjaminite figures (1 Chr 8:2,37); minor
    # ISBE variant; redirect to canonical Rephaim article
    "raphaim":                  {"status": "redirect-only", "redirect_to": "rephaim"},
    "rasses":                   {"status": "names-only"},   # apocryphal place (Judith 2:23)
    "rathumus":                 {"status": "names-only"},   # apocryphal official (1 Esd 2:16)
    "raven;-ravin":             {"status": "names-only"},   # ISBE compound; 1 Kgs 17:4-6; natural history; brief
    "razis":                    {"status": "names-only"},   # 2 Macc 14:37-46; apocryphal martyrdom
    "reading":                  {"status": "names-only"},   # lexical
    "ready":                    {"status": "names-only"},   # lexical
    "reaping":                  {"status": "names-only"},   # Ruth 2; Amos 9:13; covered under "harvest"
    "rearward":                 {"status": "names-only"},   # KJV "rear guard" (Isa 52:12; 58:8); archaic
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
    print(f'BPG Curation C62: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
