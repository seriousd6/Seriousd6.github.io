"""
BPG Curation — Batch C31: bloodguiltiness → broken (gaps 2999–3098)
Gaps reviewed: 100 (all score-5 isbe-scholarly entries, B range continued)

Very dense word-study cluster: bloodguiltiness, bloodshedding, boldness, bound,
bountifulness, brag, brawler, breadth, break, brightness, bring, broken — all
ISBE lexical entries → names-only. Apocryphal texts: book-of-enoch, book-of-jubilees,
book-of-noah, books-of-adam → names-only. KJV archaisms: broidered, brasen,
bowman, bowshot, borderer, bore, boot, bolt.

Redirects: bow-in-the-cloud → rainbow; breastplate-of-the-high-priest → breastplate.

Script: scripts/bpg-curate-31.py
Run: python3 scripts/bpg-curate-31.py  (from project root)
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
    "bloodguiltiness":                        {"status": "names-only"},   # ISBE; Ps 51:14 KJV; word study
    "bloodshedding":                          {"status": "names-only"},   # ISBE word study (Heb 9:22)
    "bloodthirsty":                           {"status": "names-only"},   # ISBE word study
    "bloody":                                 {"status": "names-only"},   # ISBE word study
    "bloody-flux":                            {"status": "names-only"},   # KJV "dysentery" (Acts 28:8); word study
    "bloom;-blossom":                         {"status": "names-only"},   # ISBE word study
    "blow":                                   {"status": "names-only"},   # ISBE word study
    "board":                                  {"status": "names-only"},   # ISBE word study
    "boast":                                  {"status": "names-only"},   # ISBE word study
    "boat":                                   {"status": "names-only"},   # ISBE word study; general
    "boccas":                                 {"status": "names-only"},   # ISBE; 1 Esd 8:2 variant; apocryphal
    "body":                                   {"status": "names-only"},   # ISBE word study; general
    "body-of-death":                          {"status": "names-only"},   # ISBE; Rom 7:24 "body of death"; general
    "body-of-heaven":                         {"status": "names-only"},   # ISBE; Exod 24:10 KJV; word study
    "body-spiritual":                         {"status": "names-only"},   # ISBE; 1 Cor 15:44; general
    "body-guard":                             {"status": "names-only"},   # ISBE; royal bodyguard; general
    "boil-1":                                 {"status": "names-only"},   # ISBE numbered; Exod 9:9-11 plague
    "boil-2":                                 {"status": "names-only"},   # ISBE numbered; skin condition
    "boldness":                               {"status": "names-only"},   # ISBE word study
    "bolt":                                   {"status": "names-only"},   # ISBE place; general
    "bondmaid":                               {"status": "names-only"},   # ISBE; KJV female slave; word study
    "bondman":                                {"status": "names-only"},   # ISBE; KJV male slave; word study
    "bondservant":                            {"status": "names-only"},   # ISBE word study; general
    "bone;-bones":                            {"status": "names-only"},   # ISBE word study; general
    "book-of-abraham":                        {"status": "names-only"},   # ISBE; apocryphal/pseudepigrapha
    "book-of-enoch":                          {"status": "names-only"},   # ISBE; 1 Enoch; apocryphal
    "book-of-jubilees":                       {"status": "names-only"},   # ISBE; apocryphal pseudepigrapha
    "book-of-life":                           {"status": "names-only"},   # ISBE; Rev 3:5; 20:12-15; score-5 → names-only
    "book-of-noah":                           {"status": "names-only"},   # ISBE; apocryphal/pseudepigrapha
    "book-of-remembrance":                    {"status": "names-only"},   # ISBE; Mal 3:16; general
    "books-of-adam":                          {"status": "names-only"},   # ISBE; apocryphal pseudepigrapha
    "boot":                                   {"status": "names-only"},   # ISBE; Isa 9:5 KJV footwear; word study
    "booths-feast-of":                        {"status": "names-only"},   # ISBE variant; covered under tabernacles stub
    "bor-ashan":                              {"status": "names-only"},   # ISBE; 1 Sam 30:30; minor Judah place
    "border;-borders":                        {"status": "names-only"},   # ISBE word study
    "borderer":                               {"status": "names-only"},   # ISBE word study
    "bore":                                   {"status": "names-only"},   # ISBE; Exod 21:6 ear-piercing; word study
    "borith":                                 {"status": "names-only"},   # ISBE; 1 Esd variant; apocryphal
    "born":                                   {"status": "names-only"},   # ISBE word study
    "born-again":                             {"status": "names-only"},   # ISBE; John 3:3; covered under regeneration
    "borne":                                  {"status": "names-only"},   # ISBE word study
    "borrowing":                              {"status": "names-only"},   # ISBE word study; Exod 22:25; Matt 5:42
    "bosom-abrahams":                         {"status": "names-only"},   # ISBE; Luke 16:22; afterlife parable
    "bosora":                                 {"status": "names-only"},   # ISBE place; 1 Macc 5:26; apocryphal
    "boss":                                   {"status": "names-only"},   # ISBE; Job 15:26 "boss of a shield"; word study
    "botany":                                 {"status": "names-only"},   # ISBE scholarly; plants of the Bible
    "botrys":                                 {"status": "names-only"},   # ISBE place; Josh 19:25 Asher town variant
    "bottom":                                 {"status": "names-only"},   # ISBE word study
    "bottomless-pit":                         {"status": "names-only"},   # ISBE; Rev 9:1; covered under abyss
    "bough":                                  {"status": "names-only"},   # ISBE word study
    "bought-1":                               {"status": "names-only"},   # ISBE numbered; "bought/purchased"; word study
    "bought-2":                               {"status": "names-only"},   # ISBE numbered; same
    "bound":                                  {"status": "names-only"},   # ISBE word study
    "bounds":                                 {"status": "names-only"},   # ISBE word study
    "bountifulness;-bounty":                  {"status": "names-only"},   # ISBE word study (2 Cor 9:5)
    # ISBE; Gen 9:13-16 rainbow covenant sign; Easton has rainbow.json
    "bow-in-the-cloud":                       {"status": "redirect-only", "redirect_to": "rainbow"},
    "bow;-bowing":                            {"status": "names-only"},   # ISBE word study
    "bowman":                                 {"status": "names-only"},   # ISBE; archer; general
    "bowshot":                                {"status": "names-only"},   # ISBE; Gen 21:16 distance; word study
    "boxing":                                 {"status": "names-only"},   # ISBE; 1 Cor 9:26; general
    "boy":                                    {"status": "names-only"},   # ISBE word study
    "bozcath":                                {"status": "names-only"},   # ISBE; 2 Kgs 22:1 Josiah's mother's city
    "brag":                                   {"status": "names-only"},   # ISBE word study
    "braided;-braiding":                      {"status": "names-only"},   # ISBE; 1 Tim 2:9 hairstyle; word study
    "bran":                                   {"status": "names-only"},   # ISBE; grain processing; general
    "branch-;bough":                          {"status": "names-only"},   # ISBE combined; general
    "brand":                                  {"status": "names-only"},   # ISBE word study (Zech 3:2)
    "branding":                               {"status": "names-only"},   # ISBE; 1 Tim 4:2 "seared conscience"
    "brasen":                                 {"status": "names-only"},   # KJV for "bronze"; ISBE word study
    "brass;-brazen":                          {"status": "names-only"},   # ISBE combined; copper/bronze; general
    "brawler":                                {"status": "names-only"},   # ISBE word study (1 Tim 3:3)
    "bray":                                   {"status": "names-only"},   # ISBE word study (Job 6:5; Prov 27:22)
    "brazen":                                 {"status": "names-only"},   # ISBE; variant of brass/bronze; general
    "brazen-sea":                             {"status": "names-only"},   # ISBE; Solomon's molten sea (1 Kgs 7:23)
    "breach-of-covenant":                     {"status": "names-only"},   # ISBE; general concept
    "breach-of-ritual":                       {"status": "names-only"},   # ISBE; general concept
    "breach-of-trust":                        {"status": "names-only"},   # ISBE word study; general
    "breadth":                                {"status": "names-only"},   # ISBE word study
    "break":                                  {"status": "names-only"},   # ISBE word study
    "break-of-day":                           {"status": "names-only"},   # ISBE; Acts 20:11 KJV; word study
    "breast":                                 {"status": "names-only"},   # ISBE word study
    # ISBE; Exod 28:15-30; twelve tribal stones; Easton has breastplate.json
    "breastplate-of-the-high-priest":         {"status": "redirect-only", "redirect_to": "breastplate"},
    "breath;-breathe;-breathing":             {"status": "names-only"},   # ISBE combined word study
    "breed":                                  {"status": "names-only"},   # ISBE word study
    "brethren":                               {"status": "names-only"},   # ISBE word study; general
    "brethren-of-the-lord":                   {"status": "names-only"},   # ISBE; Matt 12:46-50; general
    "bribery":                                {"status": "names-only"},   # ISBE word study
    "brick-kiln":                             {"status": "names-only"},   # ISBE; 2 Sam 12:31; Nah 3:14; general
    "bride-chamber":                          {"status": "names-only"},   # ISBE; Matt 9:15 KJV wedding room
    "bride-chamber-sons-children-of-the":     {"status": "names-only"},   # ISBE; KJV "bridegroom's friends"
    "bridegroom;-bridegroom-friend-of":       {"status": "names-only"},   # ISBE combined; John 3:29; general
    "bridge":                                 {"status": "names-only"},   # ISBE word study
    "brightness":                             {"status": "names-only"},   # ISBE word study
    "brim":                                   {"status": "names-only"},   # ISBE word study
    "bring":                                  {"status": "names-only"},   # ISBE word study
    "brink":                                  {"status": "names-only"},   # ISBE word study
    "broad":                                  {"status": "names-only"},   # ISBE word study
    "broad-place":                            {"status": "names-only"},   # ISBE place; general
    "broidered":                              {"status": "names-only"},   # KJV "embroidered" (Exod 28:4); word study
    "broken":                                 {"status": "names-only"},   # ISBE word study
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
    print(f'BPG Curation C31: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
