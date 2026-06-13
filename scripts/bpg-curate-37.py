"""
BPG Curation — Batch C37: daily → delusion (gaps 3599–3698)
Gaps reviewed: 100 (all score-5 isbe-scholarly entries, D range)

Word studies: daily, dainties, dally, dam, damage, damn/damnation, damsel,
dancing, dandle, danger, dare, dark/darkness, darkly, dart-snake, dash, daub,
daughter-in-law, dawn, day-*, dead, deadly, deaf, deal, dear, debt, decay,
deceit, deceive, decently, decision, decline, dedicate, deed, deep-sleep,
defame, defect, defence, defenced, defer, defile, defy, degenerate, degree,
dehort, delay, delectable, delicacy, delicate, deliciously, delight, deliver.

Apocryphal: daisan, dakubi, dalan, dammesek-eliezer, dathema, dehaites,
delos.

Theological: day-of-christ, day-of-judgment, day-of-the-lord-yahweh,
day-of-yahweh, day-last, days-last, dead-baptism-for-the, dead-state-of-the,
death-second, debate, decease-in-new-testament/old-testament → names-only.

Redirects: damascenes → damascus; dan-1;-dan-tribe-of → dan; dan-2 → dan;
dan-3 → dan; danites → dan; day-of-atonement → atonement;
david-root-of → david; david-tower-of → david; dead-sea-the → dead-sea;
deacon;-deaconess → deacon; debir-1 → debir; debir-2 → debir;
dedan;-dedanites → dedan; deluge-of-noah → deluge.

Script: scripts/bpg-curate-37.py
Run: python3 scripts/bpg-curate-37.py  (from project root)
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
    "daily":                                {"status": "names-only"},   # ISBE word study; general
    "daily-offering;-daily-sacrifice":      {"status": "names-only"},   # ISBE combined; Num 28:3-8 tamid; general
    "dainties;-dainty-meats":               {"status": "names-only"},   # ISBE combined; Gen 49:20; Prov 23:3; word study
    "daisan":                               {"status": "names-only"},   # ISBE; 1 Esd 5:31 variant; apocryphal
    "dakubi":                               {"status": "names-only"},   # ISBE; 1 Esd variant; apocryphal
    "dalan":                                {"status": "names-only"},   # ISBE; 1 Esd variant; apocryphal
    "dale-kings":                           {"status": "names-only"},   # ISBE; Gen 14:17 "King's Dale" near Jerusalem
    "daleth":                               {"status": "names-only"},   # ISBE; Hebrew letter ד; Ps 119:25-32 section
    "dally":                                {"status": "names-only"},   # ISBE word study (Judg 16:15)
    "dam":                                  {"status": "names-only"},   # ISBE; Deut 22:6-7 mother bird; word study
    "damage":                               {"status": "names-only"},   # ISBE word study (Ezra 4:22)
    # ISBE demonym; Easton has damascus.json (Aram capital; Gen 14:15; Acts 9)
    "damascenes":                           {"status": "redirect-only", "redirect_to": "damascus"},
    "dammesek-eliezer":                     {"status": "names-only"},   # ISBE; Gen 15:2 "Eliezer of Damascus"; minor figure
    "damn;-damnation;-damnable":            {"status": "names-only"},   # ISBE combined word study; general
    "damsel":                               {"status": "names-only"},   # ISBE word study; general
    # ISBE disambiguation; son of Jacob + tribe; Easton has dan.json (Gen 30:6)
    "dan-1;-dan-tribe-of":                  {"status": "redirect-only", "redirect_to": "dan"},
    # ISBE disambiguation; northern sanctuary city (1 Kgs 12:29); Easton has dan.json
    "dan-2":                                {"status": "redirect-only", "redirect_to": "dan"},
    # ISBE disambiguation; additional Dan entry; Easton has dan.json
    "dan-3":                                {"status": "redirect-only", "redirect_to": "dan"},
    "dancing":                              {"status": "names-only"},   # ISBE; 2 Sam 6:14; Exod 15:20; Ps 149:3; general
    "dandle":                               {"status": "names-only"},   # ISBE word study (Isa 66:12)
    "danger":                               {"status": "names-only"},   # ISBE word study
    # ISBE demonym; from Dan (Judg 18:1); Easton has dan.json
    "danites":                              {"status": "redirect-only", "redirect_to": "dan"},
    "daphne":                               {"status": "names-only"},   # ISBE; 2 Macc 4:33 Seleucid sanctuary; apocryphal
    "dare":                                 {"status": "names-only"},   # ISBE word study (Job 41:10; Rom 5:7)
    "dark-sayings":                         {"status": "names-only"},   # ISBE; Ps 49:4; 78:2 riddles/parables; word study
    "dark;-darkness":                       {"status": "names-only"},   # ISBE combined word study; general
    "darkly":                               {"status": "names-only"},   # ISBE; 1 Cor 13:12 "through a glass darkly"; word study
    "dart-snake":                           {"status": "names-only"},   # ISBE; Isa 34:15 "arrow snake"; word study
    "dash":                                 {"status": "names-only"},   # ISBE word study (Ps 2:9; 91:12)
    "dathema":                              {"status": "names-only"},   # ISBE; 1 Macc 5:9 Maccabean stronghold; apocryphal
    "daub":                                 {"status": "names-only"},   # ISBE word study (Ezek 13:10-15)
    "daughter-in-law":                      {"status": "names-only"},   # ISBE; Ruth 1:22; Mic 7:6; word study
    # ISBE messianic title; Rev 22:16; Isa 11:10; Easton has david.json
    "david-root-of":                        {"status": "redirect-only", "redirect_to": "david"},
    # ISBE; Neh 3:25-26; Song 4:4; Easton has david.json (Jerusalem citadel)
    "david-tower-of":                       {"status": "redirect-only", "redirect_to": "david"},
    "dawn;-dawning":                        {"status": "names-only"},   # ISBE combined word study
    "day-and-night":                        {"status": "names-only"},   # ISBE word study; general
    "day-before-the-sabbath":               {"status": "names-only"},   # ISBE; Mark 15:42 "preparation day"; word study
    # ISBE; Lev 16:29-34 Yom Kippur; Easton has atonement.json (covers Yom Kippur)
    "day-of-atonement":                     {"status": "redirect-only", "redirect_to": "atonement"},
    "day-of-christ":                        {"status": "names-only"},   # ISBE; Phil 1:6,10; 2:16 parousia term; word study
    "day-of-judgment":                      {"status": "names-only"},   # ISBE; Matt 10:15; 12:36; eschatological; word study
    "day-of-the-lord-yahweh":               {"status": "names-only"},   # ISBE; Amos 5:18-20; Joel 1:15; Zeph 1:14-18; word study
    "day-of-yahweh":                        {"status": "names-only"},   # ISBE variant; same as day-of-the-lord; word study
    "day-break-of":                         {"status": "names-only"},   # ISBE; Acts 20:11; Gen 32:24; word study
    "day-joshuas-long":                     {"status": "names-only"},   # ISBE; Josh 10:12-14 sun standing still; general
    "day-last":                             {"status": "names-only"},   # ISBE; John 6:39-40; 11:24 resurrection day; word study
    "day-lords":                            {"status": "names-only"},   # ISBE; Rev 1:10 "Lord's day"; word study
    "day-that-the":                         {"status": "names-only"},   # ISBE word study
    "days-last":                            {"status": "names-only"},   # ISBE; 2 Tim 3:1; Heb 1:2 eschatological; word study
    "deacon;-deaconess":                    {"status": "redirect-only", "redirect_to": "deacon"},   # ISBE combined; Easton has deacon.json (Phil 1:1; 1 Tim 3:8-13)
    "dead":                                 {"status": "names-only"},   # ISBE word study; general
    "dead-body":                            {"status": "names-only"},   # ISBE word study (Num 19:11-19)
    # ISBE; salt lake SE of Jerusalem; Easton has dead-sea.json (Gen 14:3)
    "dead-sea-the":                         {"status": "redirect-only", "redirect_to": "dead-sea"},
    "dead-baptism-for-the":                 {"status": "names-only"},   # ISBE; 1 Cor 15:29 disputed practice; word study
    "dead-state-of-the":                    {"status": "names-only"},   # ISBE; intermediate state; Sheol/Hades; general
    "deadly":                               {"status": "names-only"},   # ISBE word study
    "deaf":                                 {"status": "names-only"},   # ISBE word study (Mark 7:37; Exod 4:11)
    "deal":                                 {"status": "names-only"},   # ISBE word study
    "dear;-dearly":                         {"status": "names-only"},   # ISBE combined word study
    "death-body-of":                        {"status": "names-only"},   # ISBE; Rom 7:24 "body of this death"; word study
    "death-second":                         {"status": "names-only"},   # ISBE; Rev 2:11; 20:6,14; lake of fire; word study
    "debate":                               {"status": "names-only"},   # ISBE word study (Isa 27:8; Rom 1:29)
    # ISBE disambiguation; Othniel's city (Josh 15:15); Easton has debir.json
    "debir-1":                              {"status": "redirect-only", "redirect_to": "debir"},
    # ISBE disambiguation; southern king/town (Josh 10:3); Easton has debir.json
    "debir-2":                              {"status": "redirect-only", "redirect_to": "debir"},
    "debt;-debtor":                         {"status": "names-only"},   # ISBE combined word study; Matt 6:12; 18:23-35
    "decay":                                {"status": "names-only"},   # ISBE word study
    "decease-in-new-testament":             {"status": "names-only"},   # ISBE; Luke 9:31 "decease"/exodus; word study
    "decease-in-the-old-testament-and-apocyphra": {"status": "names-only"},  # ISBE; death terminology; word study
    "deceit":                               {"status": "names-only"},   # ISBE word study; general
    "deceivableness;-deceive":              {"status": "names-only"},   # ISBE combined word study
    "decently":                             {"status": "names-only"},   # ISBE word study (1 Cor 14:40)
    "decision":                             {"status": "names-only"},   # ISBE word study
    "declaration;-declare":                 {"status": "names-only"},   # ISBE combined word study
    "decline":                              {"status": "names-only"},   # ISBE word study (Exod 23:2; Ps 119:157)
    # ISBE combined; Arabia/NW Arabia peoples; Easton has dedan.json (Gen 10:7; Ezek 27:15)
    "dedan;-dedanites":                     {"status": "redirect-only", "redirect_to": "dedan"},
    "dedicate;-dedication":                 {"status": "names-only"},   # ISBE combined word study; general
    "dedication-feast-of":                  {"status": "names-only"},   # ISBE; John 10:22 Hanukkah; covered under festivals
    "deed":                                 {"status": "names-only"},   # ISBE word study
    "deep-sleep":                           {"status": "names-only"},   # ISBE; Gen 2:21; 15:12 tardemah; word study
    "defame;-defaming":                     {"status": "names-only"},   # ISBE combined word study (1 Cor 4:13)
    "defect;-defective":                    {"status": "names-only"},   # ISBE combined word study
    "defence":                              {"status": "names-only"},   # ISBE word study
    "defenced":                             {"status": "names-only"},   # ISBE; KJV "fortified" (Isa 25:2); word study
    "defer":                                {"status": "names-only"},   # ISBE word study (Prov 13:12; Eccl 5:4)
    "defile;-defilement":                   {"status": "names-only"},   # ISBE combined word study; general
    "defy":                                 {"status": "names-only"},   # ISBE word study (1 Sam 17:10)
    "degenerate":                           {"status": "names-only"},   # ISBE word study (Jer 2:21)
    "degree":                               {"status": "names-only"},   # ISBE word study (Ps 120-134 Songs of Degrees)
    "dehaites":                             {"status": "names-only"},   # ISBE; Ezra 4:9 Samaritan people; minor
    "dehort":                               {"status": "names-only"},   # ISBE; KJV "dissuade"; word study
    "delay":                                {"status": "names-only"},   # ISBE word study
    "delectable":                           {"status": "names-only"},   # ISBE word study (Isa 44:9)
    "delicacy":                             {"status": "names-only"},   # ISBE word study (Rev 18:3)
    "delicate;-delicately":                 {"status": "names-only"},   # ISBE combined word study
    "deliciously":                          {"status": "names-only"},   # ISBE word study (Rev 18:7,9)
    "delight":                              {"status": "names-only"},   # ISBE word study; general
    "delightsome":                          {"status": "names-only"},   # ISBE word study (Mal 3:12)
    "deliver":                              {"status": "names-only"},   # ISBE word study; general
    "delos":                                {"status": "names-only"},   # ISBE; 1 Macc 15:23 Aegean island; apocryphal
    # ISBE; Gen 6-9 worldwide flood; Easton has deluge.json
    "deluge-of-noah":                       {"status": "redirect-only", "redirect_to": "deluge"},
    "delusion":                             {"status": "names-only"},   # ISBE word study (2 Thess 2:11)
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
    print(f'BPG Curation C37: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
