"""
BPG Curation — Batch C67: shemites → sirach-book-of (gaps 6839–6943)
Gaps reviewed: 105 (score-5 isbe-scholarly S entries — shewbread, shiloh, shoe, silk,
sidon, siloam, simeon, simon, ships, sin-against-holy-spirit)

Redirects: shewbread-the/showbread→shewbread; shewbread-table-of/showbread-table-of→shewbread;
shiloh-1/2→shiloh; shittah;-tree;-shittim-wood→shittah-tree; shoe;-shoe-latchet→shoe;
sidon-1/2→sidon; siloam;-siloah;-shelah;-shiloah→siloam-pool-of;
siloam-towerin→siloam-tower-of; silk;-silkworm→silk;
ships-and-boats→ships; simeon-1/2→simeon; simeonites→simeon-the-tribe-of;
simon-peter→peter; simon-the-canaanite;-simon-the-cananaean;-simon-the-zealot→simon.
1 stub-needed; 19 redirects; 85 names-only.

Script: scripts/bpg-curate-67.py
Run: python3 scripts/bpg-curate-67.py  (from project root)
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
    "shemites":                 {"status": "names-only"},   # Gen 10:21 Semites; covered under "shem"
    "shenazzar":                {"status": "names-only"},   # 1 Chr 3:18 son of Jehoiachin; minor
    "shephelah":                {"status": "names-only"},   # ISBE; lowland of Judah; covered under "lowland"
    "shepher":                  {"status": "names-only"},   # ISBE place; Num 33:23-24 campsite; minor
    "shephi-shepho":            {"status": "names-only"},   # ISBE compound; Gen 36:23; 1 Chr 1:40; minor
    "shephupham-shephuphan":    {"status": "names-only"},   # ISBE compound; Num 26:39; 1 Chr 8:5; minor
    "sherd":                    {"status": "names-only"},   # pottery shard; Isa 30:14; archaeological; brief
    "sherghat-asshur-assur":    {"status": "names-only"},   # ISBE place; ancient Assur; archaeological
    "sheriff":                  {"status": "names-only"},   # Dan 3:2-3 KJV Persian official; archaic
    "shethar-bozenai-shethar-boznai": {"status": "names-only"},  # Ezra 5:3-6 Persian official; minor
    "shew-show":                {"status": "names-only"},   # ISBE compound; KJV spelling variant; lexical
    # ISBE; Exod 25:30; 1 Sam 21:6; Easton has shewbread.json
    "shewbread-table-of":       {"status": "redirect-only", "redirect_to": "shewbread"},
    # ISBE; Exod 25:30; Heb 9:2; Easton has shewbread.json
    "shewbread-the":            {"status": "redirect-only", "redirect_to": "shewbread"},
    "shibah":                   {"status": "names-only"},   # Gen 26:33 well name; minor
    "shikkeron":                {"status": "names-only"},   # Josh 15:11 Judah border; minor place
    "shillem-shillemites":      {"status": "names-only"},   # ISBE compound; Gen 46:24; minor
    # ISBE disambiguation; city in Ephraim (Josh 18:1); Easton has shiloh.json
    "shiloh-1":                 {"status": "redirect-only", "redirect_to": "shiloh"},
    # ISBE disambiguation; Gen 49:10 messianic reading; Easton has shiloh.json
    "shiloh-2":                 {"status": "redirect-only", "redirect_to": "shiloh"},
    "shimeathites":             {"status": "names-only"},   # 1 Chr 2:55 scribal clan; minor
    "shimi-shimites":           {"status": "names-only"},   # ISBE compound; Num 3:21; minor clan
    "shimron-1":                {"status": "names-only"},   # Gen 46:13 son of Issachar; minor
    "shimron-2":                {"status": "names-only"},   # Josh 11:1 Canaanite city; minor place
    "shin-sin":                 {"status": "names-only"},   # Hebrew letter; covered under "Hebrew alphabet"
    "shine":                    {"status": "names-only"},   # lexical
    "shion":                    {"status": "names-only"},   # Josh 19:19 Issachar town; minor place
    "shipmaster":               {"status": "names-only"},   # Jon 1:6; Rev 18:17 KJV; lexical
    "shipmen":                  {"status": "names-only"},   # 1 Kgs 9:27 KJV "sailors"; archaic
    # ISBE compound; Acts 27; Ezek 27; Easton has ships.json
    "ships-and-boats":          {"status": "redirect-only", "redirect_to": "ships"},
    # ISBE compound; Exod 25:5; Easton has shittah-tree.json
    "shittah;-tree;-shittim-wood": {"status": "redirect-only", "redirect_to": "shittah-tree"},
    # ISBE compound; Amos 2:15; John 1:27; Easton has shoe.json
    "shoe;-shoe-latchet":       {"status": "redirect-only", "redirect_to": "shoe"},
    "shore":                    {"status": "names-only"},   # lexical
    "shorten":                  {"status": "names-only"},   # Matt 24:22 KJV; lexical
    "shoshannim-eduth":         {"status": "names-only"},   # Ps 80 title; musical/liturgical; names-only
    "shoulder":                 {"status": "names-only"},   # lexical; anatomical
    "shoulder-blade":           {"status": "names-only"},   # Job 31:22; anatomical; brief
    "shoulder-piece":           {"status": "names-only"},   # Exod 28:7 ephod shoulder-piece; brief
    "shovel":                   {"status": "names-only"},   # Isa 30:24; Exod 27:3; agricultural; brief
    "show":                     {"status": "names-only"},   # lexical
    # ISBE variant spelling; Exod 25:30; Easton has shewbread.json
    "showbread":                {"status": "redirect-only", "redirect_to": "shewbread"},
    # ISBE variant; Exod 25:23-30; Easton has shewbread.json
    "showbread-table-of":       {"status": "redirect-only", "redirect_to": "shewbread"},
    "shower":                   {"status": "names-only"},   # Ps 65:10; Ezek 34:26; lexical
    "shrine":                   {"status": "names-only"},   # Acts 19:24; idolatry; covered under "idol"
    "shroud":                   {"status": "names-only"},   # Ezek 31:3 KJV "bough/shade"; lexical
    "shrub":                    {"status": "names-only"},   # Gen 2:5; Job 30:4; botanical; lexical
    "shua;-shuah":              {"status": "names-only"},   # ISBE compound; Gen 38:2; 1 Chr 4:11; minor
    "shual-land-of":            {"status": "names-only"},   # 1 Sam 13:17 region; minor
    "shuhah":                   {"status": "names-only"},   # 1 Chr 4:11; Judahite; minor
    "shulammite":               {"status": "names-only"},   # Song 6:13; covered under "Solomon's Song"
    "shumathites":              {"status": "names-only"},   # 1 Chr 2:53 Judahite clan; minor
    "shuni;-shunites":          {"status": "names-only"},   # ISBE compound; Gen 46:16 Gad's son; minor
    "shupham;-shuphamites":     {"status": "names-only"},   # ISBE compound; Num 26:39 Benjaminite clan; minor
    "shushan-eduth":            {"status": "names-only"},   # Ps 60 title; musical; brief
    "shushanchites":            {"status": "names-only"},   # Ezra 4:9 deportees from Susa; minor
    "shuthalhites":             {"status": "names-only"},   # Num 26:35 Ephraim clan; minor
    "shuthelah;-shuthelahites": {"status": "names-only"},   # ISBE compound; Num 26:35; minor clan
    "shuttle":                  {"status": "names-only"},   # Job 7:6 KJV "weaver's shuttle"; lexical
    "sia;-siaha":               {"status": "names-only"},   # ISBE compound; Neh 7:47; Ezra 2:44; minor
    "sibbecai-sibbechai":       {"status": "names-only"},   # ISBE compound; 2 Sam 21:18; David's warrior; minor
    "sibylline-oracles":        {"status": "names-only"},   # pseudepigraphical; too specialized
    "sicarii":                  {"status": "names-only"},   # Acts 21:38 KJV "assassins"; 1st-century Jewish sect; names-only
    "sick;-sickness":           {"status": "names-only"},   # ISBE compound; covered under "disease"
    "sides":                    {"status": "names-only"},   # lexical
    # ISBE disambiguation; Phoenician city; Easton has sidon.json
    "sidon-1":                  {"status": "redirect-only", "redirect_to": "sidon"},
    # ISBE disambiguation; Easton has sidon.json
    "sidon-2":                  {"status": "redirect-only", "redirect_to": "sidon"},
    "siege":                    {"status": "names-only"},   # military; covered under "war"
    "sieve;-sift":              {"status": "names-only"},   # ISBE compound; Amos 9:9; Luke 22:31; brief
    "siglos":                   {"status": "names-only"},   # Persian weight/coin; covered under "weights and measures"
    "sign":                     {"status": "names-only"},   # lexical; covered under "miracles"
    "signs-of-the-heavens":     {"status": "names-only"},   # Jer 10:2; Matt 16:3; brief
    "signs-numerical":          {"status": "names-only"},   # ISBE scholarly; numbers symbolism; names-only
    "sihor-libnath":            {"status": "names-only"},   # Josh 19:26 Asher boundary; minor place
    "silence":                  {"status": "names-only"},   # lexical; covered under "worship"
    # ISBE compound; Rev 18:12; Prov 31:22; Easton has silk.json
    "silk;-silkworm":           {"status": "redirect-only", "redirect_to": "silk"},
    # ISBE; Luke 13:4; Easton has siloam-tower-of.json
    "siloam-towerin":           {"status": "redirect-only", "redirect_to": "siloam-tower-of"},
    # ISBE compound; Neh 3:15; John 9:7-11; Easton has siloam-pool-of.json
    "siloam;-siloah;-shelah;-shiloah": {"status": "redirect-only", "redirect_to": "siloam-pool-of"},
    "silversmith":              {"status": "names-only"},   # Acts 19:24 Demetrius; covered under "Demetrius"
    "simalcue":                 {"status": "names-only"},   # 1 Macc 11:39; apocryphal
    # ISBE disambiguation; Gen 29:33; Easton has simeon.json
    "simeon-1":                 {"status": "redirect-only", "redirect_to": "simeon"},
    # ISBE disambiguation; Luke 2:25-35; Easton has simeon.json
    "simeon-2":                 {"status": "redirect-only", "redirect_to": "simeon"},
    # ISBE; Num 26:14; Easton has simeon-the-tribe-of.json
    "simeonites":               {"status": "redirect-only", "redirect_to": "simeon-the-tribe-of"},
    "similitude":               {"status": "names-only"},   # KJV "likeness/image"; lexical
    # ISBE disambiguation; Acts 18:2 Simon Niger etc; Easton has simon.json
    "simon-1":                  {"status": "names-only"},   # ISBE disambiguation; various; covered under simon.json
    "simon-2":                  {"status": "names-only"},   # ISBE disambiguation; various; names-only
    "simon-magus":              {"status": "names-only"},   # Acts 8:9-24; covered under specific Acts narratives
    # ISBE; Matt 10:4; Acts 1:13; Easton has peter.json
    "simon-peter":              {"status": "redirect-only", "redirect_to": "peter"},
    # ISBE compound; Matt 10:4; Easton has simon.json
    "simon-the-canaanite;-simon-the-cananaean;-simon-the-zealot": {"status": "redirect-only", "redirect_to": "simon"},
    "simple":                   {"status": "names-only"},   # Ps 19:7; Prov 1:4; lexical
    "simplicity":               {"status": "names-only"},   # 2 Cor 11:3; lexical
    "sin-1":                    {"status": "names-only"},   # ISBE disambiguation; Num 33:11 wilderness; minor
    "sin-2":                    {"status": "names-only"},   # ISBE disambiguation; Ezek 30:15-16 Egyptian city; minor
    # Matt 12:31-32; Mark 3:28-29; Luke 12:10; the "unpardonable sin";
    # theological debate: permanent apostasy, final rejection of Holy Spirit, blasphemy in context;
    # major pastoral question with significant anxiety in Christian life; Augustine, Calvin, Luther
    "sin-against-the-holy-ghost-spirit": {"status": "stub-needed"},
    "sin-money":                {"status": "names-only"},   # 2 Kgs 12:16 KJV "trespass money"; lexical
    "sin-man-of":               {"status": "names-only"},   # 2 Thess 2:3 "man of sin"; covered under eschatology
    "sina":                     {"status": "names-only"},   # Greek form of Sinai; covered under "Sinai"
    "sincere;-sincerity":       {"status": "names-only"},   # ISBE compound; 1 Cor 5:8; Eph 6:24; lexical
    "sinew":                    {"status": "names-only"},   # Gen 32:32; Isa 48:4; anatomical; brief
    "singers;-singing":         {"status": "names-only"},   # ISBE compound; covered under "music"
    "single-eye":               {"status": "names-only"},   # Matt 6:22 KJV "single eye"; lexical
    "singular":                 {"status": "names-only"},   # Lev 27:2 KJV; archaic
    "sinim-land-of":            {"status": "names-only"},   # Isa 49:12; debated = China or Aswan; brief
    "sinites":                  {"status": "names-only"},   # Gen 10:17 Canaanite clan; minor
    "sinlessness":              {"status": "names-only"},   # covered under "sanctification" and "Christ's sinlessness"
    "sinner":                   {"status": "names-only"},   # lexical
    "sir":                      {"status": "names-only"},   # lexical title; archaic
    "sirach-book-of":           {"status": "names-only"},   # deuterocanonical/apocryphal "Ecclesiasticus"; not Protestant canon
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
    print(f'BPG Curation C67: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
