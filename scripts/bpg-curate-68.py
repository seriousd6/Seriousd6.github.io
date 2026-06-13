"""
BPG Curation — Batch C68: sirach-the-alphabet-of → spiritual-house (gaps ~6734–6838)
Gaps reviewed: 105 (score-5 isbe-scholarly S entries)

Score-5 ISBE posture: ~93% names-only. Notable stubs: son-of-god-the and son-of-man-the
(major Christological titles), sons-of-god (Gen 6 debate), spirits-in-prison (1 Pet 3:18-20),
spiritual-gifts (cessationism/continuationism debate).
5 stub-needed; 2 redirects; 98 names-only.

Script: scripts/bpg-curate-68.py
Run: python3 scripts/bpg-curate-68.py  (from project root)
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
    "sirach-the-alphabet-of":   {"status": "names-only"},   # apocryphal acrostic; too specialized
    "sirah-well-of":            {"status": "names-only"},   # 2 Sam 3:26; place; minor
    "sisinnes":                 {"status": "names-only"},   # apocryphal (1 Esd 6:3,7)
    "sismai":                   {"status": "names-only"},   # Judahite (1 Chr 2:40); minor
    "sister":                   {"status": "names-only"},   # lexical; cultural
    "sisters-son":              {"status": "names-only"},   # KJV "nephew"; lexical
    "sith":                     {"status": "names-only"},   # KJV "since" (Ezek 35:6); archaic
    "sithri":                   {"status": "names-only"},   # Kohathite (Exod 6:22); minor
    "sixty":                    {"status": "names-only"},   # lexical number
    "skill;-skilful":           {"status": "names-only"},   # ISBE compound; lexical
    "skin":                     {"status": "names-only"},   # KJV "hide/skin"; lexical
    "skirt":                    {"status": "names-only"},   # Ruth 3:9; covered under "garment"
    "skull":                    {"status": "names-only"},   # Golgotha; covered under "Golgotha"
    "sky":                      {"status": "names-only"},   # lexical
    "slander":                  {"status": "names-only"},   # covered under "slander" in Easton
    "slaughter-of-the-innocents": {"status": "names-only"},  # Matt 2:16-18; covered under "Herod"
    "slaughter-valley-of":      {"status": "names-only"},   # Jer 7:32; covered under "tophet"
    "slave;-slavery":           {"status": "names-only"},   # ISBE compound; covered under "slave" in Easton
    "slaying":                  {"status": "names-only"},   # lexical
    "sleep":                    {"status": "names-only"},   # covered under "sleep" in Easton
    "sleep-deep":               {"status": "names-only"},   # Gen 2:21; 15:12 tardemah; covered under "sleep"
    "sleeves":                  {"status": "names-only"},   # Isa 3:22 KJV; cultural; archaic
    "sleight":                  {"status": "names-only"},   # Eph 4:14 KJV; archaic
    "slime;-slime-pits":        {"status": "names-only"},   # ISBE compound; Gen 11:3; 14:10; bitumen; brief
    "slip":                     {"status": "names-only"},   # Isa 17:10 KJV; lexical
    "slopes":                   {"status": "names-only"},   # geographic; lexical
    "slow":                     {"status": "names-only"},   # lexical
    "sluggard":                 {"status": "names-only"},   # Prov 6:6; covered under "laziness"
    "sluice":                   {"status": "names-only"},   # Isa 19:10 KJV; lexical
    "smell":                    {"status": "names-only"},   # lexical
    "smiting-by-the-sun":       {"status": "names-only"},   # sunstroke; Ps 121:6; covered under "sun"
    "smoke":                    {"status": "names-only"},   # lexical
    "sneeze":                   {"status": "names-only"},   # 2 Kgs 4:35; brief
    "snuffers;-snuffdishes":    {"status": "names-only"},   # ISBE compound; Exod 25:38; tabernacle items
    "sober;-sobriety;-soberness": {"status": "names-only"}, # ISBE compound; covered under "temperance"
    "socket":                   {"status": "names-only"},   # Exod 26:19 tabernacle; brief
    "socoh;-soco":              {"status": "names-only"},   # ISBE compound; Judah town; place
    "sod-sodden":               {"status": "names-only"},   # KJV "boiled" (Exod 12:9); archaic
    "soda":                     {"status": "names-only"},   # Jer 2:22; mineral; brief
    "sodering":                 {"status": "names-only"},   # KJV "soldering" (Isa 41:7); archaic
    "sodom-vine-of":            {"status": "names-only"},   # Deut 32:32; covered under "Sodom"
    "sodomite":                 {"status": "names-only"},   # KJV "male cult prostitute"; covered under "sodomites"
    # ISBE compound for the Dead Sea near Sodom's location; redirect to canonical article
    "sodomitish;-sea":          {"status": "redirect-only", "redirect_to": "dead-sea"},
    "sodomy":                   {"status": "names-only"},   # covered under "sodomites"
    "sojourner":                {"status": "names-only"},   # KJV "alien/stranger"; covered under "stranger"
    "soldering":                {"status": "names-only"},   # Isa 41:7; lexical
    "soldier":                  {"status": "names-only"},   # covered under "army" in Easton
    "solemn-assembly-meeting":  {"status": "names-only"},   # ISBE compound; covered under "solemn assembly"
    "solemn-solemnity":         {"status": "names-only"},   # ISBE compound; KJV; lexical
    "solomon-odes-of":          {"status": "names-only"},   # pseudepigraphical; too specialized
    "solomon-pools-of":         {"status": "names-only"},   # Eccl 2:6; Neh 2:14; covered under "Solomon"
    "solomon-psalms-psalter-of": {"status": "names-only"},  # pseudepigraphical; too specialized
    "someis":                   {"status": "names-only"},   # apocryphal (1 Esd 9:35)
    "sometime":                 {"status": "names-only"},   # KJV "formerly" (Eph 2:13); archaic
    # "You are the Son of God" (Matt 16:16); "this is my beloved Son" (Matt 3:17; 17:5);
    # divine sonship (John 5:17-18; 10:30-33) vs. Davidic/messianic sonship (Ps 2:7; Acts 13:33);
    # Nicene debate with Arians; essential Christological title defining Christ's nature
    "son-of-god-the":           {"status": "stub-needed"},
    # Dan 7:13-14 "one like a son of man" coming on clouds; Jesus's preferred self-designation
    # (70+ occurrences in Gospels); Jewish background in Ezekiel, Enoch; Mark 14:62 trial claim;
    # humanity + eschatological authority; debate: simple "human being" vs. divine figure;
    # key for understanding Jesus's self-understanding and Christology
    "son-of-man-the":           {"status": "stub-needed"},
    "son-in-law":               {"status": "names-only"},   # lexical; cultural
    "son;-sons":                {"status": "names-only"},   # ISBE compound; lexical
    "song":                     {"status": "names-only"},   # lexical
    "song-of-songs":            {"status": "names-only"},   # covered under "Solomon, Song of" in Easton
    "song-of-the-three-children": {"status": "names-only"},  # apocryphal addition to Daniel; LXX
    "songs-of-degrees":         {"status": "names-only"},   # Ps 120-134; covered under "ascent, songs of"
    "sons-of":                  {"status": "names-only"},   # lexical
    # Gen 6:1-4 "the sons of God saw the daughters of men"; Job 1:6; 2:1; 38:7;
    # three views: fallen angels (1 Enoch, Jude 6), Sethite theory, kings/nobles;
    # "nephilim" connection (Gen 6:4); significant for angelology and Genesis interpretation
    "sons-of-god":              {"status": "stub-needed"},
    "sons-of-god-new-testament": {"status": "names-only"},  # John 1:12; Rom 8:14-16; covered under "adoption"
    "soothsayers":              {"status": "names-only"},   # Isa 2:6; covered under "divination"
    "sope":                     {"status": "names-only"},   # KJV "soap" (Jer 2:22; Mal 3:2); archaic
    "sophonias":                {"status": "names-only"},   # apocryphal variant of Zephaniah
    "sorcerer;-sorcery":        {"status": "names-only"},   # ISBE compound; covered under "magic"
    "sore":                     {"status": "names-only"},   # KJV "painful/grievous"; lexical
    "sorek-valley-of":          {"status": "names-only"},   # Judg 16:4 Samson/Delilah; covered under "Delilah"
    "sorrel":                   {"status": "names-only"},   # Zech 1:8; botanical; brief
    "sorrow":                   {"status": "names-only"},   # lexical; covered under "grief"
    "sostratus":                {"status": "names-only"},   # Seleucid official (2 Macc 4:28); apocryphal
    "sottish":                  {"status": "names-only"},   # KJV "stupid/foolish" (Jer 4:22); archaic
    "soul":                     {"status": "names-only"},   # covered under "soul" in Easton
    "sound":                    {"status": "names-only"},   # lexical
    "soundings":                {"status": "names-only"},   # Acts 27:28; nautical; brief
    "sour":                     {"status": "names-only"},   # KJV "unripe" (Jer 31:29-30; Ezek 18:2); lexical
    "south-chambers-of-the":    {"status": "names-only"},   # Ezek 40:44; temple; brief
    # ISBE entry; redirect to canonical Sheba article (covers the queen's visit to Solomon)
    "south-queen-of-the":       {"status": "redirect-only", "redirect_to": "sheba"},
    "southeast":                {"status": "names-only"},   # geographic direction; lexical
    "span":                     {"status": "names-only"},   # Exod 28:16 unit of measure; covered under "weights"
    "spark":                    {"status": "names-only"},   # Isa 1:31; Job 18:5; lexical
    "sparta;-spartans":         {"status": "names-only"},   # ISBE compound; 1 Macc 12:2-23; apocryphal
    "speaking-evil":            {"status": "names-only"},   # KJV "slander/blaspheme"; covered under "slander"
    "spear;-spearmen":          {"status": "names-only"},   # ISBE compound; covered under "arms"
    "specially":                {"status": "names-only"},   # KJV; lexical
    "speckled":                 {"status": "names-only"},   # Gen 30:32-43 Jacob's flocks; brief
    "spectacle":                {"status": "names-only"},   # 1 Cor 4:9; lexical
    "speech":                   {"status": "names-only"},   # lexical
    "spelt":                    {"status": "names-only"},   # Exod 9:32; Isa 28:25; botanical; brief
    "spindle":                  {"status": "names-only"},   # Prov 31:19; cultural; brief
    "spirit-of-divination":     {"status": "names-only"},   # Acts 16:16 python spirit; covered under "divination"
    "spirit-evil":              {"status": "names-only"},   # 1 Sam 16:14-16; covered under "evil spirits"
    "spirit-familiar":          {"status": "names-only"},   # Lev 19:31; covered under "familiar spirit"
    "spirit-unclean-or-evil":   {"status": "names-only"},   # Synoptic Gospels; covered under "demon"
    # 1 Pet 3:18-20 "he went and preached to the spirits in prison"; debated passage:
    # fallen angels from Gen 6 (1 Enoch), OT saints in Hades, Noah's contemporaries;
    # Christ's descent into hell creed; 1 Pet 4:6 connection; major hermeneutical challenge
    "spirits-in-prison":        {"status": "stub-needed"},
    "spirits-discernings-of":   {"status": "names-only"},   # 1 Cor 12:10; covered under "gifts of the Spirit"
    "spiritual":                {"status": "names-only"},   # lexical; covered under "spiritual"
    "spiritual-blessing":       {"status": "names-only"},   # Eph 1:3; covered under "blessing"
    "spiritual-body":           {"status": "names-only"},   # 1 Cor 15:44; covered under "resurrection"
    "spiritual-drink":          {"status": "names-only"},   # 1 Cor 10:4; covered under "Lord's Supper"
    # 1 Cor 12-14; Romans 12:6-8; Eph 4:11; charismata; lists and purposes;
    # cessationism (gifts ceased with apostles) vs. continuationism (ongoing gifts);
    # tongues, prophecy, healing debate between Reformed and Pentecostal/charismatic traditions;
    # essential for understanding church life and the Holy Spirit's work today
    "spiritual-gifts":          {"status": "stub-needed"},
    "spiritual-house":          {"status": "names-only"},   # 1 Pet 2:5; covered under "church" and "priesthood"
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
    print(f'BPG Curation C68: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
