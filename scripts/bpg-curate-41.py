"""
BPG Curation — Batch C41: ephrath;-ephrathah → express (gaps 3999–4098)
Gaps reviewed: 100 (all score-5 isbe-scholarly entries, E range continued)

Word studies: ephrath/ephrathah, epilepsy, epistle, equal, equality, equity,
era, err/error, esay, espora, espousal, espy, estate, esteem, estimate,
eternal, eternity, ethics, even/evening, evenings-between, event, evidence,
evil, evil-one, evil-spirit, evil-thing, evil-doers, evil-favoredness, ewe,
exact, exaction, exactors, exalt, examine, exceed, excellency, excellent,
exchange, execute, exercise, exhortation, expect, expectation, expedient,
experience, experiment, exposure-to-wild-beasts, express.

Apocryphal: epiphanes, epiphi, epistles-spurious, esdras variants, esdris,
esebrias, eserebias, esora, esyelus, ethanus, ethma, ethnarch, eumenes-ii,
eunatan, eupator, eupolemus, eve-gospel-of.

Scholarly ISBE: eschatology (3 forms), epistles-captivity, epistles-pastoral,
eri-aku, ethiopic-language, ethiopic-versions, ethnography/ethnology,
ethics-of-jesus, eucharist, euraquilo, evolution, exegesis, exorcism,
expectation-messianic, exodus-the-book-of.

Redirects: ephron-1 → ephron; ephron-2 → ephron; esebon → heshbon;
esdraelon-plain-of → esdraelon; eshcol-1 → eshcol; eshcol-2 → eshcol;
eshkalonite → ashkelon; eshtaolites;-eshtaulites → eshtaol;
eshtemoh → eshtemoa; esther-the-rest-of → esther;
eve-in-the-new-testament → eve; eve-in-the-old-testament → eve;
exodus-the-book-of → exodus.

Script: scripts/bpg-curate-41.py
Run: python3 scripts/bpg-curate-41.py  (from project root)
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
    "ephrath;-ephrathah":                   {"status": "names-only"},   # ISBE combined; Gen 35:16-19; Mic 5:2 Bethlehem area; word study
    # ISBE disambiguation; Gen 23:8-20 Hittite (Machpelah); Easton has ephron.json
    "ephron-1":                             {"status": "redirect-only", "redirect_to": "ephron"},
    # ISBE disambiguation; boundary hill (Josh 15:9); Easton has ephron.json
    "ephron-2":                             {"status": "redirect-only", "redirect_to": "ephron"},
    "epilepsy":                             {"status": "names-only"},   # ISBE; Matt 17:15 "moonstruck"; general
    "epiphanes":                            {"status": "names-only"},   # ISBE; Antiochus IV epithet (1 Macc 1:10); apocryphal
    "epiphi":                               {"status": "names-only"},   # ISBE; 2 Macc 6:2 Egyptian month; apocryphal
    "epistle":                              {"status": "names-only"},   # ISBE word study; general
    "epistles-captivity":                   {"status": "names-only"},   # ISBE; Eph/Phil/Col/Phm (prison epistles); scholarly
    "epistles-spurious":                    {"status": "names-only"},   # ISBE; pseudepigraphal letters; scholarly
    "epistles-the-pastoral":                {"status": "names-only"},   # ISBE; 1-2 Tim, Tit; scholarly
    "equal":                                {"status": "names-only"},   # ISBE word study
    "equality":                             {"status": "names-only"},   # ISBE word study (2 Cor 8:13-14)
    "equity":                               {"status": "names-only"},   # ISBE word study (Isa 11:4; Mic 3:9)
    "era":                                  {"status": "names-only"},   # ISBE; chronological epoch; scholarly
    "eri-aku":                              {"status": "names-only"},   # ISBE; Arioch identification (Gen 14:1); scholarly
    "eri;-erites":                          {"status": "names-only"},   # ISBE combined; Gad's son + clan (Gen 46:16; Num 26:16)
    "err;-error":                           {"status": "names-only"},   # ISBE combined word study
    "esay":                                 {"status": "names-only"},   # ISBE; KJV alternate form of "Isaiah"; word study
    "eschatology":                          {"status": "names-only"},   # ISBE; study of last things; score-5 → names-only
    "eschatology-of-the-new-testament":     {"status": "names-only"},   # ISBE scholarly; NT end-times; score-5
    "eschatology-of-the-old-testament":     {"status": "names-only"},   # ISBE scholarly; OT end-times; score-5
    # ISBE; "plain of Jezreel" battle site (Judg 4-5; 1 Kgs 21); Easton has esdraelon.json
    "esdraelon-plain-of":                   {"status": "redirect-only", "redirect_to": "esdraelon"},
    "esdras-5-and-6":                       {"status": "names-only"},   # ISBE; 3-4 Ezra (variant numbering); apocryphal
    "esdras-fourth-book-of":                {"status": "names-only"},   # ISBE; 2 Esdras/4 Ezra; apocryphal
    "esdras-second-book-of":                {"status": "names-only"},   # ISBE; 2 Esdras; apocryphal
    "esdras-the-first-book-of":             {"status": "names-only"},   # ISBE; 1 Esdras (= 3 Ezra); apocryphal
    "esdras-the-second-fourth-book-of;-apocalyptic-esdras": {"status": "names-only"},  # ISBE; 4 Ezra variant; apocryphal
    "esdris":                               {"status": "names-only"},   # ISBE; 1 Esd 8:43 variant; apocryphal
    # ISBE; Esebon = Greek/Apocryphal form of Heshbon (1 Macc 5:26); Easton has heshbon.json
    "esebon":                               {"status": "redirect-only", "redirect_to": "heshbon"},
    "esebrias":                             {"status": "names-only"},   # ISBE; 1 Esd 8:54 variant; apocryphal
    "eserebias":                            {"status": "names-only"},   # ISBE; 1 Esd 8:47 variant; apocryphal
    "eshan":                                {"status": "names-only"},   # ISBE; Josh 15:52 Judah hill town; minor place
    # ISBE disambiguation; Num 13:23-24 Hebron valley; Easton has eshcol.json (Gen 14:13)
    "eshcol-1":                             {"status": "redirect-only", "redirect_to": "eshcol"},
    # ISBE disambiguation; Amorite ally of Abraham; Easton has eshcol.json
    "eshcol-2":                             {"status": "redirect-only", "redirect_to": "eshcol"},
    # ISBE; Ashkelonite variant; Judg 1:18; Easton has ashkelon.json
    "eshkalonite":                          {"status": "redirect-only", "redirect_to": "ashkelon"},
    # ISBE combined demonym; from Eshtaol (Judg 13:25); Easton has eshtaol.json
    "eshtaolites;-eshtaulites":             {"status": "redirect-only", "redirect_to": "eshtaol"},
    # ISBE; Josh 15:50; 21:14 priestly city; Easton has eshtemoa.json (1 Chr 6:57)
    "eshtemoh":                             {"status": "redirect-only", "redirect_to": "eshtemoa"},
    "esora":                                {"status": "names-only"},   # ISBE; Jdt 4:4 place; apocryphal
    "espousal;-espouse":                    {"status": "names-only"},   # ISBE combined; betrothal (Matt 1:18; Hos 2:19); word study
    "espy":                                 {"status": "names-only"},   # ISBE word study (Josh 14:7 KJV)
    "estate":                               {"status": "names-only"},   # ISBE word study
    "esteem":                               {"status": "names-only"},   # ISBE word study (Isa 53:3; Phil 2:3)
    # ISBE; apocryphal additions to Esther (Gk Esther); Easton has esther.json
    "esther-the-rest-of":                   {"status": "redirect-only", "redirect_to": "esther"},
    "estimate;-estimation":                 {"status": "names-only"},   # ISBE combined word study (Lev 27:2-8)
    "esyelus":                              {"status": "names-only"},   # ISBE; 1 Esd 9:43 variant; apocryphal
    "eternal":                              {"status": "names-only"},   # ISBE word study; general
    "eternity":                             {"status": "names-only"},   # ISBE word study; general
    "eth-kazin":                            {"status": "names-only"},   # ISBE; Josh 19:13 Zebulun boundary; minor place
    "ethanus":                              {"status": "names-only"},   # ISBE; 2 Esd 14:24 scribe; apocryphal
    "ethics":                               {"status": "names-only"},   # ISBE; biblical moral philosophy; score-5
    "ethics-of-jesus":                      {"status": "names-only"},   # ISBE scholarly; Sermon on the Mount etc.; score-5
    "ethiopic-language":                    {"status": "names-only"},   # ISBE; Ge'ez/Ethiopic language; scholarly
    "ethiopic-versions":                    {"status": "names-only"},   # ISBE; Bible translations; scholarly
    "ethma":                                {"status": "names-only"},   # ISBE; 1 Esd variant; apocryphal
    "ethnarch":                             {"status": "names-only"},   # ISBE; Seleucid/Roman title (2 Macc 14:12); word study
    "ethnography;-ethnology":               {"status": "names-only"},   # ISBE combined; biblical anthropology; scholarly
    "eucharist":                            {"status": "names-only"},   # ISBE; Lord's Supper; covered under communion in Easton
    "eumenes-ii":                           {"status": "names-only"},   # ISBE; Pergamene king (1 Macc 8:8); apocryphal
    "eunatan":                              {"status": "names-only"},   # ISBE; 1 Esd 8:44 variant; apocryphal
    "eupator":                              {"status": "names-only"},   # ISBE; 1 Macc 6:17 Antiochus V epithet; apocryphal
    "eupolemus":                            {"status": "names-only"},   # ISBE; 1 Macc 8:17 Maccabean envoy; apocryphal
    "euraquilo":                            {"status": "names-only"},   # ISBE; Acts 27:14 northeast wind; word study
    # ISBE scholarly; Luke 8:2; Gal 3:28 (Eve); Easton has eve.json (Gen 3:20)
    "eve-in-the-new-testament":             {"status": "redirect-only", "redirect_to": "eve"},
    # ISBE scholarly; Gen 2-3 Eve creation/fall narrative; Easton has eve.json
    "eve-in-the-old-testament":             {"status": "redirect-only", "redirect_to": "eve"},
    "eve-gospel-of":                        {"status": "names-only"},   # ISBE; apocryphal Gnostic gospel; extracanonical
    "even;-evening;-eventide":              {"status": "names-only"},   # ISBE combined word study
    "evenings-between-the":                 {"status": "names-only"},   # ISBE; Exod 12:6 ben ha-arbayim sacrificial time; word study
    "event":                                {"status": "names-only"},   # ISBE word study (Eccl 2:14)
    "evidence;-evident;-evidently":         {"status": "names-only"},   # ISBE combined word study (Heb 11:1)
    "evil":                                 {"status": "names-only"},   # ISBE word study; general
    "evil-one":                             {"status": "names-only"},   # ISBE; Matt 6:13 "the evil one" = Satan; word study
    "evil-spirit":                          {"status": "names-only"},   # ISBE; 1 Sam 16:14-16 Saul's evil spirit; word study
    "evil-thing":                           {"status": "names-only"},   # ISBE word study
    "evil-doers":                           {"status": "names-only"},   # ISBE word study (1 Pet 2:12-14)
    "evil-favoredness":                     {"status": "names-only"},   # ISBE; Deut 17:1 KJV "blemished animal"; word study
    "evolution":                            {"status": "names-only"},   # ISBE; creation/science; score-5 → names-only
    "ewe":                                  {"status": "names-only"},   # ISBE word study (Gen 21:28-30 female lamb)
    "exact":                                {"status": "names-only"},   # ISBE word study
    "exaction":                             {"status": "names-only"},   # ISBE word study (Neh 5:7-12; Isa 60:17)
    "exactors":                             {"status": "names-only"},   # ISBE word study (Isa 60:17 KJV)
    "exalt":                                {"status": "names-only"},   # ISBE word study; general
    "exaltation-of-christ-the":             {"status": "names-only"},   # ISBE; Phil 2:9-11; Acts 2:33; word study
    "examine;-examination":                 {"status": "names-only"},   # ISBE combined word study
    "exceed;-exceeding;-exceedingly":       {"status": "names-only"},   # ISBE combined word study
    "excellency":                           {"status": "names-only"},   # ISBE word study (Exod 15:7; 2 Cor 4:7)
    "excellent":                            {"status": "names-only"},   # ISBE word study
    "exchange;-exchanger":                  {"status": "names-only"},   # ISBE combined word study (Matt 25:27)
    "execute;-executioner":                 {"status": "names-only"},   # ISBE combined word study
    "exegesis":                             {"status": "names-only"},   # ISBE; biblical interpretation; scholarly
    "exercise":                             {"status": "names-only"},   # ISBE word study (1 Tim 4:7-8)
    "exhortation":                          {"status": "names-only"},   # ISBE word study (1 Cor 14:3; Heb 13:22)
    # ISBE; Exod 1-15 narrative; Easton has exodus.json (Exod 12:37-40)
    "exodus-the-book-of":                   {"status": "redirect-only", "redirect_to": "exodus"},
    "exorcism;-exorcist":                   {"status": "names-only"},   # ISBE combined; Acts 19:13; Mark 9:38; word study
    "expect;-expectation":                  {"status": "names-only"},   # ISBE combined word study
    "expectation-messianic":                {"status": "names-only"},   # ISBE; Jewish messianic hope; score-5 → names-only
    "expedient":                            {"status": "names-only"},   # ISBE word study (John 16:7; 1 Cor 6:12)
    "experience":                           {"status": "names-only"},   # ISBE word study (Rom 5:4)
    "experiment":                           {"status": "names-only"},   # ISBE word study (2 Cor 9:13 KJV "proof")
    "exposure-to-wild-beasts":              {"status": "names-only"},   # ISBE; 1 Cor 15:32; Roman damnatio ad bestias
    "express":                              {"status": "names-only"},   # ISBE word study (Heb 1:3 "express image")
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
    print(f'BPG Curation C41: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
