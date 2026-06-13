"""
BPG Curation — Batch C53: law-roman → maareh-geba (gaps 5299–5398)
Gaps reviewed: 100 (score-5 isbe-scholarly L–M entries — law/levi/lords compounds,
lot disambiguation, lot/lots/lots-feast, lucius/lud/luke/lydia disambiguation pairs,
lying→lie, maachah compound)

Heavy redirect batch: ISBE compound and disambiguation articles cover major topics
with existing Easton canonical articles. 36 redirects include: law-roman→law;
levi-1/2→levi; levitical-cities/levis→levite; lord-of-hosts/lord;-the-lord→lord;
lords-prayer-the→lords-prayer; lords-supper;-eucharist→lords-supper;
lot-1/2/lots/lots-feast-of→lot; luke disambiguation→luke/luke-gospel-according-to;
lydia-1/2/lydian→lydia; maacah;-maachah/maacathites→maachah.
0 stub-needed; 36 redirects; 64 names-only.

Script: scripts/bpg-curate-53.py
Run: python3 scripts/bpg-curate-53.py  (from project root)
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
    # ISBE scholarly; Roman law in NT; Easton has law.json
    "law-roman":                 {"status": "redirect-only", "redirect_to": "law"},
    "lawful":                    {"status": "names-only"},   # Matt 12:10; 1 Cor 6:12; lexical
    "lawgiver":                  {"status": "names-only"},   # Isa 33:22; Jas 4:12; covered under law.json
    "lawless":                   {"status": "names-only"},   # 1 Tim 1:9; 2 Thess 2:8 KJV; lexical
    "lay;-laying":               {"status": "names-only"},   # ISBE compound; lexical
    # Prov 30:15 KJV; Easton has horse-leech.json
    "leach":                     {"status": "redirect-only", "redirect_to": "horse-leech"},
    "leaping":                   {"status": "names-only"},   # 2 Sam 6:16; Song 2:8; lexical
    "ledge":                     {"status": "names-only"},   # 1 Kgs 7:28-29 KJV; architectural; names-only
    "left":                      {"status": "names-only"},   # lexical
    "leg":                       {"status": "names-only"},   # Ps 147:10; Prov 26:7; lexical
    "legislation-of-sanctity":   {"status": "names-only"},   # ISBE; Lev 17-26 "Holiness Code"; scholarly
    # Exod 22:25; Luke 6:35; Easton has loan.json
    "lend-loan":                 {"status": "redirect-only", "redirect_to": "loan"},
    "lessau":                    {"status": "names-only"},   # 1 Esd 5:29 variant; apocryphal
    "let":                       {"status": "names-only"},   # lexical
    "lethech":                   {"status": "names-only"},   # Hos 3:2 KJV "half homer"; dry measure; lexical
    # ISBE; written correspondence; Easton has letter.json
    "letters":                   {"status": "redirect-only", "redirect_to": "letter"},
    # ISBE disambiguation; Gen 29:34; Leah's son/tribe; Easton has levi.json
    "levi-1":                    {"status": "redirect-only", "redirect_to": "levi"},
    # ISBE disambiguation; Luke 3:24,29; Jesus' ancestors; Easton has levi.json
    "levi-2":                    {"status": "redirect-only", "redirect_to": "levi"},
    # ISBE; variant of Levites; Easton has levite.json
    "levis":                     {"status": "redirect-only", "redirect_to": "levite"},
    # ISBE; Josh 21; cities assigned to Levites; Easton has levite.json
    "levitical-cities":          {"status": "redirect-only", "redirect_to": "levite"},
    # ISBE compound; Easton has lewdness.json
    "lewd;-lewdness":            {"status": "redirect-only", "redirect_to": "lewdness"},
    "libation":                  {"status": "names-only"},   # drink offering; no dedicated Easton slug; covered under offerings
    "liberal;-liberality;-liberally": {"status": "names-only"},  # ISBE compound; 2 Cor 9:11-13; lexical
    "liberty":                   {"status": "names-only"},   # Gal 5:1,13; 2 Cor 3:17; no dedicated Easton article
    # ISBE; Num 3:21; 26:58; Gershonite clan; Easton has libni.json
    "libnites":                  {"status": "redirect-only", "redirect_to": "libni"},
    "libraries":                 {"status": "names-only"},   # ISBE scholarly; ancient Near East libraries; names-only
    "library-of-nineveh":        {"status": "names-only"},   # ISBE; Ashurbanipal's cuneiform library; scholarly
    # ISBE compound; Jer 46:9; Nah 3:9; Easton has libya.json
    "libya;-libyans":            {"status": "redirect-only", "redirect_to": "libya"},
    "licence":                   {"status": "names-only"},   # Acts 21:40; 25:16 KJV; lexical
    # ISBE; Josh 13:26 KJV "Lo-debar"; Easton has lo-debar.json
    "lidebir":                   {"status": "redirect-only", "redirect_to": "lo-debar"},
    # ISBE compound; Easton has lie.json
    "lie;-lying":                {"status": "redirect-only", "redirect_to": "lie"},
    "liers-in-wait":             {"status": "names-only"},   # Josh 8:4-7; Judg 9:25; military ambush; lexical
    # ISBE compound; Gen 2:9; Rev 22:2; Easton has life.json
    "life-tree-of":              {"status": "redirect-only", "redirect_to": "life"},
    "lift":                      {"status": "names-only"},   # lexical
    # ISBE compound; Easton has light.json
    "light;-lightness":          {"status": "redirect-only", "redirect_to": "light"},
    "like;-liken;-likeness;-liking": {"status": "names-only"},  # ISBE compound; lexical
    "lilith":                    {"status": "names-only"},   # Isa 34:14 KJV "screech owl"; uncertain; names-only
    "lily-work":                 {"status": "names-only"},   # 1 Kgs 7:19,22,26; temple architectural detail
    "limit":                     {"status": "names-only"},   # lexical
    "line":                      {"status": "names-only"},   # measuring line (Jer 31:39); lexical
    "lineage":                   {"status": "names-only"},   # lexical
    "liquor":                    {"status": "names-only"},   # Num 6:3 KJV; Exod 22:29; lexical
    "list":                      {"status": "names-only"},   # lexical
    "literature-sub-apostolic":  {"status": "names-only"},   # ISBE scholarly; Apostolic Fathers; names-only
    "little-genesis":            {"status": "names-only"},   # alternate name for Book of Jubilees; apocryphal
    "lively;-living":            {"status": "names-only"},   # ISBE compound; 1 Pet 2:4-5 "lively stones"; lexical
    # ISBE; Rev 4:6-8; Ezek 1:5-14; Easton has living-creatures.json
    "living-creature":           {"status": "redirect-only", "redirect_to": "living-creatures"},
    "loaf":                      {"status": "names-only"},   # lexical
    "locks":                     {"status": "names-only"},   # Song 5:11; Num 6:5; hair/locks; lexical
    # ISBE compound; Acts 9:32-35; Easton has lydda.json (= Lod)
    "lod;-lydda":                {"status": "redirect-only", "redirect_to": "lydda"},
    "loddeus":                   {"status": "names-only"},   # 1 Esd 5:30 variant; apocryphal
    "loft":                      {"status": "names-only"},   # 1 Kgs 17:19; Acts 20:9 KJV; upper room; lexical
    "loftily;-loftiness;-lofty": {"status": "names-only"},   # ISBE compound; Isa 2:11-17; lexical
    "logia-the":                 {"status": "names-only"},   # ISBE scholarly; sayings of Jesus (Q); names-only
    "logos":                     {"status": "names-only"},   # ISBE; John 1:1 "Word"; Christological; scholarly; score-5
    "loins":                     {"status": "names-only"},   # Gen 35:11; Eph 6:14 "gird your loins"; lexical
    "longevity":                 {"status": "names-only"},   # ISBE; Gen 5 antediluvian ages; names-only
    "longsuffering":             {"status": "names-only"},   # Gal 5:22; 2 Pet 3:15; covered under patience
    "look":                      {"status": "names-only"},   # lexical
    "looking-glass":             {"status": "names-only"},   # Exod 38:8 KJV "mirror"; lexical
    "loom":                      {"status": "names-only"},   # weaving device; cultural; names-only
    # ISBE; "LORD of hosts" = Yahweh Sabaoth; Easton has lord.json
    "lord-of-hosts":             {"status": "redirect-only", "redirect_to": "lord"},
    # ISBE compound; Matt 6:9-13; Easton has lords-prayer.json
    "lords-prayer-the":          {"status": "redirect-only", "redirect_to": "lords-prayer"},
    # ISBE compound; 1 Cor 11:20-34; Easton has lords-supper.json
    "lords-supper;-eucharist":   {"status": "redirect-only", "redirect_to": "lords-supper"},
    # ISBE compound; Easton has lord.json
    "lord;-the-lord":            {"status": "redirect-only", "redirect_to": "lord"},
    "lords-of-the-philistines":  {"status": "names-only"},   # Judg 3:3; 16:5; Philistine rulers; covered under Philistines
    "loss":                      {"status": "names-only"},   # Phil 3:7-8; lexical
    # ISBE disambiguation; Gen 11:27; Abraham's nephew; Easton has lot.json
    "lot-1":                     {"status": "redirect-only", "redirect_to": "lot"},
    # ISBE disambiguation; casting lots (Prov 16:33; Acts 1:26); Easton has lot.json
    "lot-2":                     {"status": "redirect-only", "redirect_to": "lot"},
    "lothasubus":                {"status": "names-only"},   # 1 Esd 9:44 variant; apocryphal
    # ISBE; Prov 16:33; Acts 1:26; Easton has lot.json
    "lots":                      {"status": "redirect-only", "redirect_to": "lot"},
    # ISBE; Purim = feast of lots (Esth 9:26-28); Easton has lot.json
    "lots-feast-of":             {"status": "redirect-only", "redirect_to": "lot"},
    "lotus-trees":               {"status": "names-only"},   # Job 40:21-22 KJV; botanical; names-only
    "love-brotherly":            {"status": "names-only"},   # Rom 12:10; Heb 13:1; covered under love.json
    "love-feast":                {"status": "names-only"},   # Jude 12; 2 Pet 2:13; agape meal; names-only
    "lovely":                    {"status": "names-only"},   # Phil 4:8; lexical
    "lover":                     {"status": "names-only"},   # lexical
    "loves":                     {"status": "names-only"},   # lexical
    "lovingkindness":            {"status": "names-only"},   # Hebrew hesed; Ps 36:7; names-only (distinct from general love)
    "low-country":               {"status": "names-only"},   # Josh 9:1; Judah "Shephelah"; names-only
    "lowland":                   {"status": "names-only"},   # same as low-country; Shephelah; names-only
    "lozon":                     {"status": "names-only"},   # 1 Esd 5:33 variant; apocryphal
    # ISBE disambiguation; Acts 13:1 prophet/teacher at Antioch; Easton has lucius.json
    "lucius-1":                  {"status": "redirect-only", "redirect_to": "lucius"},
    # ISBE disambiguation; Rom 16:21 kinsman of Paul; Easton has lucius.json
    "lucius-2":                  {"status": "redirect-only", "redirect_to": "lucius"},
    # ISBE compound; Gen 10:13; Isa 66:19; Easton has lud.json
    "lud;-ludim":                {"status": "redirect-only", "redirect_to": "lud"},
    "luhith-ascent-of":          {"status": "names-only"},   # Isa 15:5; Jer 48:5; Moabite route; minor place
    # ISBE compound; Col 4:14; 2 Tim 4:11; Easton has luke.json
    "luke-the-evangelist":       {"status": "redirect-only", "redirect_to": "luke"},
    # ISBE compound; Easton has luke-gospel-according-to.json
    "luke-the-gospel-of":        {"status": "redirect-only", "redirect_to": "luke-gospel-according-to"},
    "lunatick":                  {"status": "names-only"},   # Matt 4:24 KJV; epilepsy/demon; lexical
    "lurk;-lurking-place":       {"status": "names-only"},   # ISBE compound; Ps 10:8-9; lexical
    "lute":                      {"status": "names-only"},   # uncertain instrument (Ps 150:4); musical; names-only
    # ISBE disambiguation; Acts 16:14-15 purple cloth seller; Easton has lydia.json
    "lydia-1":                   {"status": "redirect-only", "redirect_to": "lydia"},
    # ISBE disambiguation; Lydia region (Asia Minor); Easton has lydia.json
    "lydia-2":                   {"status": "redirect-only", "redirect_to": "lydia"},
    # ISBE; Jer 46:9 KJV; people of Lydia; Easton has lydia.json
    "lydian":                    {"status": "redirect-only", "redirect_to": "lydia"},
    "lye":                       {"status": "names-only"},   # Jer 2:22; Mal 3:2 KJV "soap/lye"; lexical
    # ISBE; Prov 12:19; Easton has lie.json
    "lying":                     {"status": "redirect-only", "redirect_to": "lie"},
    # ISBE compound; Gen 3:16; 27:43; Easton has maachah.json
    "maacah;-maachah":           {"status": "redirect-only", "redirect_to": "maachah"},
    # ISBE; Josh 12:5; 13:13; demonym from Maacah; Easton has maachah.json
    "maacathites":               {"status": "redirect-only", "redirect_to": "maachah"},
    "maani":                     {"status": "names-only"},   # 1 Esd 9:34 variant; apocryphal
    "maareh-geba":               {"status": "names-only"},   # Judg 20:33 KJV "meadow of Gibeah"; minor place
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
    print(f'BPG Curation C53: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
