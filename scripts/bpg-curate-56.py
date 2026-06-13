"""
BPG Curation — Batch C56: midnight → nabataeans (gaps 5599–5698)
Gaps reviewed: 100 (score-5 isbe-scholarly M–N entries)

Score-5 ISBE posture: ~90% names-only. Stubs for concepts absent from Easton/Smith.
Notable stubs: midrash (Jewish interpretive method), mishna (oral law collection),
molech/moloch (Canaanite child-sacrifice deity critical for OT study), moriah (Gen 22
binding of Isaac / temple mount), millennium views (postmil/premil eschatology).
6 stub-needed; 8 redirects; 86 names-only.

Script: scripts/bpg-curate-56.py
Run: python3 scripts/bpg-curate-56.py  (from project root)
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
    "midnight":                     {"status": "names-only"},   # KJV time reference; lexical
    # Jewish biblical commentary method: midrash halakha (legal), midrash aggadah (narrative);
    # "midrash of the book of the kings" (2 Chr 24:27); essential for NT Jewish background;
    # understanding how rabbis read Scripture illuminates NT interpretation methods
    "midrash":                      {"status": "stub-needed"},
    "migdal-eder":                  {"status": "names-only"},   # tower of the flock (Gen 35:21; Mic 4:8); place
    "mill;-millstone":              {"status": "names-only"},   # ISBE compound; grinding grain; general
    # Eschatological position: Christ returns after the church-age millennium; Augustine's
    # framework; Puritan optimism; "binding of Satan" (Rev 20:2) now fulfilled; kingdom grows;
    # requires its own article as a distinct view alongside premillennial/amillennial
    "millennium-postmillennial-view": {"status": "stub-needed"},
    # Eschatological position: Christ returns before 1,000-year literal reign on earth (Rev 20);
    # dispensational vs. historic variants; key texts: Dan 2:44; Zech 14:4-9; Rev 20:1-6;
    # dominant evangelical view in 20th c.; requires its own article for the debate
    "millennium-premillennial-view":  {"status": "stub-needed"},
    "millstone":                    {"status": "names-only"},   # Deut 24:6; Matt 18:6; grinding implement
    "mina":                         {"status": "names-only"},   # unit of weight/money (Luke 19:13-25); covered under weights
    "mind":                         {"status": "names-only"},   # lexical; general
    "mine;-mining":                 {"status": "names-only"},   # Job 28:1-11; general
    "minerals":                     {"status": "names-only"},   # general category; natural history
    "mingled-people;-mixed-multitude": {"status": "names-only"},  # Exod 12:38; "erev rav"; brief
    "minish":                       {"status": "names-only"},   # KJV "diminish" (Exod 5:19); archaic
    "ministry":                     {"status": "names-only"},   # covered under "minister" in Easton/Smith
    "miphkad;-gate-of":             {"status": "names-only"},   # Neh 3:31 gate of Jerusalem; place
    "miracles-gift-of":             {"status": "names-only"},   # spiritual gift; covered under "miracles"
    "mirage":                       {"status": "names-only"},   # Isa 35:7 KJV "parched ground"; natural
    "mire":                         {"status": "names-only"},   # Ps 69:2; lexical
    "mirmah":                       {"status": "names-only"},   # Benjaminite (1 Chr 8:10); minor
    "misael":                       {"status": "names-only"},   # variant of Mishael; apocryphal
    "misaias":                      {"status": "names-only"},   # apocryphal variant of Isaiah
    "mischief":                     {"status": "names-only"},   # KJV "harm/evil"; lexical
    # Oral Torah compiled by Judah HaNasi (~200 AD); 6 orders (Seder), 63 tractates;
    # codifies Pharisaic halakha; essential for understanding Judaism Jesus addressed;
    # Mishnah + Gemara = Talmud; foundational for NT background study
    "mishna":                       {"status": "stub-needed"},
    "mishneh":                      {"status": "names-only"},   # "second quarter" of Jerusalem (2 Kgs 22:14); place
    "mishor":                       {"status": "names-only"},   # Hebrew "plateau/plain" (Deut 3:10); geographic term
    "mist":                         {"status": "names-only"},   # Gen 2:6; Acts 13:11; lexical
    "mistress":                     {"status": "names-only"},   # KJV "lady/owner" (Isa 24:2; Nah 3:4); lexical
    "mithkah":                      {"status": "names-only"},   # wilderness camp (Num 33:28-29); place
    "mithradates":                  {"status": "names-only"},   # Persian/Seleucid official (Ezra 4:7); minor
    "mizar-the-hill":               {"status": "names-only"},   # Ps 42:6; geographic; uncertain
    # ISBE compound; multiple sites named Mizpah; redirect to canonical Mizpeh article
    "mizpah;-mizpeh":               {"status": "redirect-only", "redirect_to": "mizpeh"},
    # ISBE compound; redirect to canonical article on Moab
    "moab;-moabites":               {"status": "redirect-only", "redirect_to": "moab"},
    "moabitess":                    {"status": "redirect-only", "redirect_to": "moab"},  # Ruth 1:22; demonym
    "mochmur-the-brook":            {"status": "names-only"},   # Judith 7:18; apocryphal
    "mock;-mocker;-mocking":        {"status": "names-only"},   # Prov 17:5; KJV; lexical
    "modad-book-of-eldad-and":      {"status": "names-only"},   # pseudepigraphical; not canonical
    "moderately":                   {"status": "names-only"},   # KJV Joel 2:23 "former rain moderately"; lexical
    "moderation":                   {"status": "names-only"},   # Phil 4:5 "let your moderation be known"; lexical
    "moeth":                        {"status": "names-only"},   # apocryphal figure (1 Esd 5:24)
    # Canaanite deity worshipped by child sacrifice (Lev 18:21; 20:2-5; 2 Kgs 23:10);
    # Tophet in Valley of Hinnom; Ahaz and Manasseh burned sons to Molech (2 Chr 28:3);
    # connected to "passing through fire"; NT "Gehenna" derived from Hinnom valley
    "molech;-moloch":               {"status": "stub-needed"},
    "mollify":                      {"status": "names-only"},   # KJV "soften" (Isa 1:6); lexical
    "molten-sea":                   {"status": "names-only"},   # bronze basin in temple (1 Kgs 7:23-26); covered under "sea"
    "molten-image":                 {"status": "names-only"},   # idol; covered under "idolatry"
    "momdis":                       {"status": "names-only"},   # apocryphal figure (1 Esd 5:25)
    "moment":                       {"status": "names-only"},   # KJV "instant"; lexical
    "money-current":                {"status": "names-only"},   # Gen 23:16 KJV "current money"; lexical
    # ISBE entry; redirect to covetousness (1 Tim 6:10)
    "money-love-of":                {"status": "redirect-only", "redirect_to": "covetousness"},
    "money-sin":                    {"status": "names-only"},   # ISBE entry on usury/interest laws; general
    "monster":                      {"status": "names-only"},   # Lam 4:3 KJV; lexical/natural
    "monthly;-prognosticators":     {"status": "names-only"},   # Isa 47:13 astrologers; lexical
    "monument":                     {"status": "names-only"},   # Isa 65:4 KJV; lexical
    "mooli":                        {"status": "names-only"},   # apocryphal (1 Esd 8:46,47)
    "moossias":                     {"status": "names-only"},   # apocryphal (1 Esd 9:31)
    # Egyptian city; ISBE variant form; redirect to Memphis
    "moph":                         {"status": "redirect-only", "redirect_to": "memphis"},
    "morality":                     {"status": "names-only"},   # general ethical concept; not a biblical article
    "morashtite":                   {"status": "names-only"},   # Micah's demonym (Mic 1:1; Jer 26:18); covered under Micah
    "moreh-hill-of":                {"status": "names-only"},   # Judg 7:1; geographic reference
    "moreh-oak-of":                 {"status": "names-only"},   # Gen 12:6; Abram's first stop in Canaan; minor
    # Gen 22:2 "land of Moriah" where Abraham bound Isaac; identified with Jerusalem (2 Chr 3:1);
    # temple mount connection; "the LORD will provide" (Jehovah-jireh); critical for typology
    # of Isaac as type of Christ; links patriarchal narrative to temple theology
    "moriah-land-of":               {"status": "stub-needed"},
    "morning":                      {"status": "names-only"},   # lexical; time reference
    "morning-watch":                {"status": "names-only"},   # Exod 14:24; night watch division; lexical
    "morning-wings-of":             {"status": "names-only"},   # Ps 139:9; poetic; lexical
    "morrow-after-the-sabbath":     {"status": "names-only"},   # Lev 23:11 firstfruits timing; lexical
    "morrow-tomorrow":              {"status": "names-only"},   # KJV lexical
    "morsel":                       {"status": "names-only"},   # Prov 17:1; lexical
    "mortal;-mortality":            {"status": "names-only"},   # 1 Cor 15:53-54; covered under resurrection
    "mortgage":                     {"status": "names-only"},   # Neh 5:3; economic/historical; minor
    "mortify":                      {"status": "names-only"},   # Rom 8:13; Col 3:5 KJV "put to death"; lexical
    "moses-assumption-of":          {"status": "names-only"},   # pseudepigraphical; Jude 9 background; too specialized
    "moses-song-of":                {"status": "names-only"},   # Deut 32; covered under Moses/Deuteronomy
    "mosollamon":                   {"status": "names-only"},   # apocryphal (1 Esd 8:44)
    "mosollamus":                   {"status": "names-only"},   # apocryphal (1 Esd 1:9)
    "most-high-most-holy":          {"status": "names-only"},   # divine titles; covered under "God, names of"
    "mother-in-law":                {"status": "names-only"},   # Naomi/Ruth; Lev 18:17; lexical
    "motion":                       {"status": "names-only"},   # KJV "impulse" (Rom 7:5); lexical
    "mound":                        {"status": "names-only"},   # Josh 11:13 KJV; archaeological term; general
    "mount-ephraim":                {"status": "names-only"},   # geographic area; covered under Ephraim
    "mount-of-congregation-the":    {"status": "names-only"},   # Isa 14:13; cosmic mountain; poetic/lexical
    # ISBE entry; redirect to canonical article
    "mount-of-olives":              {"status": "redirect-only", "redirect_to": "olives"},
    "mouse;-mice":                  {"status": "names-only"},   # Lev 11:29; 1 Sam 6:4-5; natural history
    "mouth":                        {"status": "names-only"},   # lexical; anatomical
    "mowing;-mown-grass":           {"status": "names-only"},   # Ps 72:6; Amos 7:1; agricultural; brief
    "muffler":                      {"status": "names-only"},   # Isa 3:19 KJV veil; lexical
    "mulberry;-trees":              {"status": "names-only"},   # 2 Sam 5:23-24; natural history; brief
    "mulcted":                      {"status": "names-only"},   # KJV "fined" (Amos 2:8); archaic
    "multitude;-mixed":             {"status": "names-only"},   # ISBE variant; see mingled-people
    "munition":                     {"status": "names-only"},   # KJV "fortress/stronghold" (Isa 29:7); lexical
    "murderers":                    {"status": "names-only"},   # Rev 21:8; lexical; covered under "murder"
    "murmur;-murmurings":           {"status": "names-only"},   # Exod 16:7-8; Israel's wilderness complaint; lexical
    "muse;-musing":                 {"status": "names-only"},   # Ps 39:3 KJV; lexical
    # ISBE compound; redirect to canonical music article
    "musical-instruments":          {"status": "redirect-only", "redirect_to": "music"},
    "mutilation":                   {"status": "names-only"},   # Gal 5:12; Phil 3:2 KJV; lexical
    "mutter":                       {"status": "names-only"},   # Isa 8:19 KJV spiritists; lexical
    "myndus":                       {"status": "names-only"},   # Lycian city (1 Macc 15:23); apocryphal
    "mythology":                    {"status": "names-only"},   # 1 Tim 1:4 KJV "myths"; general; lexical
    "naamah-1":                     {"status": "names-only"},   # Lamech's daughter (Gen 4:22); minor
    "naamah-2":                     {"status": "names-only"},   # Solomon's Ammonite wife (1 Kgs 14:21,31); minor
    "naamite":                      {"status": "names-only"},   # demonym for Naamah; epithet (Job 2:11)
    "naarah-1":                     {"status": "names-only"},   # Asher's border town (Josh 16:7); place
    "naarah-2":                     {"status": "names-only"},   # Ashur's wife (1 Chr 4:5,6); minor
    "naaran;-narath":               {"status": "names-only"},   # variant of Naarah-1; ISBE alternate spelling
    # ISBE compound; variant spellings of Nahshon; redirect to canonical article
    "naashon;-naason;-naasson":     {"status": "redirect-only", "redirect_to": "nahshon"},
    "naathus":                      {"status": "names-only"},   # apocryphal figure (1 Esd 9:31)
    "nabarias":                     {"status": "names-only"},   # apocryphal figure (1 Esd 8:44)
    "nabataeans;-nabathaeans":      {"status": "names-only"},   # Arab trading kingdom; 2 Cor 11:32; historical
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
    print(f'BPG Curation C56: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
