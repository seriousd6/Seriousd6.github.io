"""
BPG Curation — Batch C70: summer-house → terah-1 (gaps ~7049–7153)
Gaps reviewed: 105 (score-5 isbe-scholarly S–T entries)

Score-5 ISBE posture: ~92% names-only. Notable stubs: synoptic-gospels (Matthew/Mark/Luke
relationship), table-of-nations (Gen 10 ethnography), tell-el-amarna-tablets (Amarna letters),
temptation-of-christ (Matt 4 three temptations), ten-commandments-the (Decalogue).
5 stub-needed; 3 redirects; 97 names-only.

Script: scripts/bpg-curate-70.py
Run: python3 scripts/bpg-curate-70.py  (from project root)
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
    "summer-house":             {"status": "names-only"},   # Amos 3:15; Judg 3:20; cultural; brief
    "sun-1":                    {"status": "names-only"},   # ISBE disambiguation; covered under "sun"
    "sun-2":                    {"status": "names-only"},   # ISBE disambiguation; covered under "sun"
    "sun-gate":                 {"status": "names-only"},   # Jer 19:2 KJV; Jerusalem gate; place
    "sun-chariots-of-the":      {"status": "names-only"},   # 2 Kgs 23:11; covered under "sun worship"
    "sun-horses-of-the":        {"status": "names-only"},   # 2 Kgs 23:11; covered under "sun worship"
    "sun-smiting-by":           {"status": "names-only"},   # Ps 121:6; covered under "sunstroke"
    "sun-images":               {"status": "names-only"},   # 2 Chr 14:5 KJV; covered under "idol"
    "sun-worship":              {"status": "names-only"},   # covered under "sun" and "idolatry"
    "sunday":                   {"status": "names-only"},   # Lord's Day; covered under "Lord's Day"
    "sunrising":                {"status": "names-only"},   # KJV "east"; lexical
    "sunstroke":                {"status": "names-only"},   # 2 Kgs 4:18-20; brief
    "sup;-supper":              {"status": "names-only"},   # ISBE compound; covered under "Lord's Supper"
    "superfluous;-superfluity": {"status": "names-only"},   # KJV; lexical
    "superscription":           {"status": "names-only"},   # Matt 22:20 coin inscription; lexical
    "superstition;-superstitious": {"status": "names-only"},  # ISBE compound; covered under "idolatry"
    "supper-lords":             {"status": "names-only"},   # Mark 6:21; Herod's feast; brief
    "supply":                   {"status": "names-only"},   # lexical
    "sure;-surely":             {"status": "names-only"},   # KJV; lexical
    "surname":                  {"status": "names-only"},   # KJV "name given"; lexical
    "susanna-the-history-of":   {"status": "names-only"},   # apocryphal addition to Daniel
    "swaddle;-swaddling-band":  {"status": "names-only"},   # ISBE compound; Luke 2:7; cultural; brief
    "sweat":                    {"status": "names-only"},   # Gen 3:19; Luke 22:44; brief
    "sweet-cane":               {"status": "names-only"},   # Isa 43:24; calamus; botanical; brief
    "sweet-incense":            {"status": "names-only"},   # Exod 30:34; covered under "incense"
    "swell":                    {"status": "names-only"},   # lexical
    "swift":                    {"status": "names-only"},   # lexical
    "swift-beasts":             {"status": "names-only"},   # Isa 66:20 KJV; brief
    "swollen":                  {"status": "names-only"},   # KJV; lexical
    "sycomore-tree":            {"status": "names-only"},   # Luke 19:4 Zacchaeus; covered under "sycamore"
    "synagogue-of-libertines":  {"status": "names-only"},   # Acts 6:9 Freedmen's Synagogue; covered under "synagogue"
    "synagogue-of-satan":       {"status": "names-only"},   # Rev 2:9; 3:9; covered under "Revelation"
    # Matthew, Mark, Luke as "synoptic" (seen together); Synoptic Problem; source theories
    # (Q source, Markan priority, Two-Source Hypothesis, Griesbach); agreements and
    # disagreements with John; essential background for understanding the Gospels
    "synoptic;-gospels":        {"status": "stub-needed"},
    "synzygus":                 {"status": "names-only"},   # Phil 4:3 KJV "yokefellow"; brief
    # ISBE disambiguations; redirect to canonical Syria article
    "syria-1":                  {"status": "redirect-only", "redirect_to": "syria"},
    "syria-2":                  {"status": "redirect-only", "redirect_to": "syria"},
    "syria-maachah":            {"status": "names-only"},   # 2 Sam 10:6; OT kingdom; minor
    "syriac-versions":          {"status": "names-only"},   # Peshitta; too specialized at score-5
    "syrian;-language":         {"status": "names-only"},   # Aramaic (2 Kgs 18:26); covered under "aramaic"
    "syrians":                  {"status": "names-only"},   # covered under "syria" in Easton
    "syrtis":                   {"status": "names-only"},   # Acts 27:17 quicksands; geographical; brief
    "syzygus":                  {"status": "names-only"},   # variant of synzygus; Phil 4:3; brief
    "tabaoth-tabbaoth":         {"status": "names-only"},   # ISBE compound; Ezra 2:43; minor
    "tabellius":                {"status": "names-only"},   # apocryphal (1 Esd 2:16)
    "taber":                    {"status": "names-only"},   # Nah 2:7 KJV "tabering"; archaic
    "tabernacle-of-testimony-witness": {"status": "names-only"},  # ISBE compound; covered under "tabernacle"
    "table":                    {"status": "names-only"},   # lexical; covered under "table of the Lord"
    # Gen 10:1-32 listing 70 nations descending from Noah's sons Shem, Ham, Japheth;
    # foundational for understanding the spread of peoples after the flood; key text for
    # biblical ethnography; connects OT to ANE history; background for Acts 2 (Pentecost reversal)
    "table-of-nations":         {"status": "stub-needed"},
    "tabor-mount":              {"status": "names-only"},   # Judg 4:6-14; covered under "tabor"
    "tabor-oak-of":             {"status": "names-only"},   # 1 Sam 10:3; place; brief
    "tabret;-timbrel":          {"status": "names-only"},   # ISBE compound; covered under "timbrel"
    "tabrimmon":                {"status": "names-only"},   # Aram king (1 Kgs 15:18); minor
    "tahan;-tahanites":         {"status": "names-only"},   # ISBE compound; Ephraimite (Num 26:35); minor
    "tahash":                   {"status": "names-only"},   # Nahor's son (Gen 22:24); minor
    "tahath-1":                 {"status": "names-only"},   # wilderness camp (Num 33:26-27); place
    "tahath-2":                 {"status": "names-only"},   # Ephraimite ancestor (1 Chr 7:20); minor
    "tahchemonite":             {"status": "names-only"},   # David's chief warrior (2 Sam 23:8); minor
    "tahpanhes":                {"status": "names-only"},   # Egyptian city (Jer 43:7-9); covered in Easton
    "tail":                     {"status": "names-only"},   # lexical
    "take":                     {"status": "names-only"},   # lexical
    "talsas":                   {"status": "names-only"},   # apocryphal (1 Esd 5:33)
    "tamar-1":                  {"status": "names-only"},   # ISBE disambiguation; covered under "tamar"
    "tamar-2":                  {"status": "names-only"},   # ISBE disambiguation; covered under "tamar"
    "tanner":                   {"status": "names-only"},   # Acts 9:43; 10:6; cultural; brief
    "tapestry":                 {"status": "names-only"},   # Prov 7:16; 31:22 KJV; cultural; brief
    "tappuah-1":                {"status": "names-only"},   # Judah town (Josh 15:34); place
    "tappuah-2":                {"status": "names-only"},   # Ephraim town (Josh 16:8); place
    "tarshish-navy-ships-of":   {"status": "names-only"},   # covered under "tarshish" and "ships"
    "taskmaster":               {"status": "names-only"},   # Exod 1:11; covered under "Egypt"
    "tassel":                   {"status": "names-only"},   # Num 15:38-40; covered under "fringes"
    "taste":                    {"status": "names-only"},   # lexical
    "tattenai":                 {"status": "names-only"},   # Persian official (Ezra 5:3); minor
    "tattler":                  {"status": "names-only"},   # 1 Tim 5:13 KJV "gossip"; archaic
    "tav":                      {"status": "names-only"},   # Hebrew letter; covered under "Hebrew alphabet"
    "taverns-three":            {"status": "names-only"},   # Acts 28:15; Appian Way stop; place
    "taw":                      {"status": "names-only"},   # variant of tav; Hebrew letter; names-only
    "tax;-taxing":              {"status": "names-only"},   # ISBE compound; covered under "tribute"
    "teach;-teacher;-teaching": {"status": "names-only"},   # ISBE compound; covered under "teacher"
    "tear-bottle":              {"status": "names-only"},   # Ps 56:8; cultural; brief
    "tears":                    {"status": "names-only"},   # lexical; covered under "weeping"
    "teat":                     {"status": "names-only"},   # KJV "breast" (Ezek 23:3); archaic
    # ISBE variant spelling; redirect to canonical Tahpanhes article
    "tehaphnehes":              {"status": "redirect-only", "redirect_to": "tahpanhes"},
    "tel-harsha":               {"status": "names-only"},   # post-exilic area (Ezra 2:59); minor
    "telem-1":                  {"status": "names-only"},   # Judah town (Josh 15:24); place
    "telem-2":                  {"status": "names-only"},   # post-exilic gatekeeper (Ezra 10:24); minor
    "tell":                     {"status": "names-only"},   # archaeological "tell"; lexical
    # 14th century BC cuneiform tablets (1887); letters from Canaanite kings to Egyptian pharaohs;
    # mention Habiru (=Hebrew?) raids; evidence of pre-conquest Canaan political landscape;
    # confirm biblical city names (Jerusalem as "Urusalim"); key OT archaeological background
    "tell-el-amarna;-tablets":  {"status": "stub-needed"},
    "temah":                    {"status": "names-only"},   # post-exilic temple servants (Ezra 2:53); minor
    "temper":                   {"status": "names-only"},   # lexical
    "temperance;-temperate":    {"status": "names-only"},   # ISBE compound; covered under "temperance"
    "tempest":                  {"status": "names-only"},   # lexical; covered under "storm"
    "temple-keepers-servants":  {"status": "names-only"},   # netinim; covered under "nethinim"
    "temples":                  {"status": "names-only"},   # anatomical (sides of head); lexical
    "temples-robbers-of":       {"status": "names-only"},   # Acts 19:37 KJV; brief
    "tempt;-temptation":        {"status": "names-only"},   # ISBE compound; covered under "temptation"
    # Matt 4:1-11; Luke 4:1-13; three temptations: bread (stones), kingdoms (bow to Satan),
    # pinnacle test (angels catch you); each answered with Deuteronomy; recapitulates Israel's
    # forty years with forty days; Christ's sinless victory qualifies him as faithful High Priest
    # (Heb 4:15); "tempted in every way as we are, yet without sin"
    "temptation-of-christ":     {"status": "stub-needed"},
    "ten":                      {"status": "names-only"},   # lexical number
    # Exod 20:1-17; Deut 5:6-21; Ten Words (עֲשֶׂרֶת הַדְּבָרִים); division varies between
    # Catholic/Lutheran (no 2nd commandment on images; split 10th on coveting) and
    # Reformed/Orthodox traditions; moral law vs. ceremonial/civil law distinction;
    # foundational for OT ethics and natural law; essential for catechesis and Bible study
    "ten-commandments-the":     {"status": "stub-needed"},
    "ten-strings":              {"status": "names-only"},   # Ps 33:2; 92:3; musical instrument; brief
    "tender":                   {"status": "names-only"},   # lexical
    "tenon":                    {"status": "names-only"},   # Exod 26:17 KJV tabernacle joint; archaic
    "tent-maker":               {"status": "names-only"},   # Acts 18:3 Paul's trade; brief
    "tenth":                    {"status": "names-only"},   # lexical; ordinal
    "tephon":                   {"status": "names-only"},   # apocryphal (1 Macc 9:50)
    "terah-1":                  {"status": "names-only"},   # ISBE disambiguation; covered under "terah"
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
    print(f'BPG Curation C70: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
