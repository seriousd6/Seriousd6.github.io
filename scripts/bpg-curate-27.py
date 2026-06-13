"""
BPG Curation — Batch C27: ashkelonites → awa (gaps 2599–2698)
Gaps reviewed: 100 (all score-5 isbe-scholarly entries, A range continued)

Heavy on apocryphal figure variants (1 Esd: asibias, asipha, asom, aspharasus,
assalimoth, assamias, atar, aterezaias, ateta, atharias, atipha, attus, augia,
awa → all names-only), ISBE word studies (aside, ask, asunder, attain, audience,
avail, avoid), and KJV archaisms (aul = awl, avouch, assay, austere).

Redirects: ashkelonites → ashkelon; ashtaroth;-ashteroth-karnaim;-beeshterah → ashtaroth;
asshur;-assur → asshur; assyrians → assyria; astarte;-astoreth → ashtoreth.

Script: scripts/bpg-curate-27.py
Run: python3 scripts/bpg-curate-27.py  (from project root)
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
    # ISBE demonym; Easton has ashkelon.json (Philistine city; Judg 14:19)
    "ashkelonites":                          {"status": "redirect-only", "redirect_to": "ashkelon"},
    # ISBE triple combined; Easton has ashtaroth.json (Canaanite goddess city; Deut 1:4)
    "ashtaroth;-ashteroth-karnaim;-beeshterah": {"status": "redirect-only", "redirect_to": "ashtaroth"},
    "ashteroth-karnaim":                     {"status": "names-only"},   # Gen 14:5 place; no separate Easton article
    "ashurbanipal":                          {"status": "names-only"},   # Assyrian king (Ezra 4:10); ISBE
    "asia-minor":                            {"status": "names-only"},   # ISBE place; general geographic reference
    "asia-minor-archaeology-of":             {"status": "names-only"},   # ISBE scholarly duplicate of C26 entry
    "asiarch":                               {"status": "names-only"},   # ISBE; Acts 19:31 Roman official
    "asibias":                               {"status": "names-only"},   # ISBE; 1 Esd 9:26 variant; apocryphal
    "aside":                                 {"status": "names-only"},   # ISBE word study
    "asipha":                                {"status": "names-only"},   # ISBE; 1 Esd 5:29 variant; apocryphal
    "ask":                                   {"status": "names-only"},   # ISBE word study
    "asleep":                                {"status": "names-only"},   # ISBE word study (1 Thess 4:13)
    "asmodaeus":                             {"status": "names-only"},   # ISBE; Tobit 3:8 demon; apocryphal
    "asmoneans":                             {"status": "names-only"},   # ISBE; Hasmonean dynasty; general
    "asochis-plain-of":                      {"status": "names-only"},   # ISBE; 1 Macc 12:49 region; apocryphal
    "asom":                                  {"status": "names-only"},   # ISBE; 1 Esd 9:33 variant; apocryphal
    "asphalt":                               {"status": "names-only"},   # ISBE; bitumen (Gen 11:3; 14:10)
    "asphar-the-pool":                       {"status": "names-only"},   # ISBE; 1 Macc 9:33; apocryphal place
    "aspharasus":                            {"status": "names-only"},   # ISBE; 1 Esd 5:16 variant; apocryphal
    "assalimoth":                            {"status": "names-only"},   # ISBE; 1 Esd 8:36 variant; apocryphal
    "assamias":                              {"status": "names-only"},   # ISBE; 1 Esd 9:32 variant; apocryphal
    "assaphioth":                            {"status": "names-only"},   # ISBE; 1 Esd variant; apocryphal
    "assarion":                              {"status": "names-only"},   # ISBE; Roman assarius coin (Matt 10:29)
    "assassination":                         {"status": "names-only"},   # ISBE word study; general
    "assassins":                             {"status": "names-only"},   # ISBE; Acts 21:38 Sicarii; general
    "assault":                               {"status": "names-only"},   # ISBE word study
    "assay":                                 {"status": "names-only"},   # ISBE; KJV "attempt" (Deut 4:34); word study
    "assemblies-masters-of":                 {"status": "names-only"},   # ISBE; Eccl 12:11 KJV; general
    "assembly":                              {"status": "names-only"},   # ISBE word study; general
    "assembly-solemn":                       {"status": "names-only"},   # ISBE; Lev 23:36 atzeret; general
    "assent":                                {"status": "names-only"},   # ISBE word study
    "assessor":                              {"status": "names-only"},   # ISBE; legal/judicial role
    # ISBE combined variant; Easton has asshur.json (Shem's son; Gen 10:22; Assyria)
    "asshur;-assur":                         {"status": "redirect-only", "redirect_to": "asshur"},
    "assidaeans":                            {"status": "names-only"},   # ISBE; Hasidim (1 Macc 2:42); Maccabean
    "assiduous":                             {"status": "names-only"},   # ISBE word study
    "assign":                                {"status": "names-only"},   # ISBE word study
    "associate":                             {"status": "names-only"},   # ISBE word study
    "assuage":                               {"status": "names-only"},   # ISBE word study (Gen 8:1 KJV)
    "assumption-of-moses":                   {"status": "names-only"},   # ISBE; Testament of Moses; apocryphal
    "assurbanipal":                          {"status": "names-only"},   # ISBE variant of ashurbanipal; Assyrian king
    "assyria-and-babylonia-religion-of":     {"status": "names-only"},   # ISBE scholarly; comparative religion
    "assyrian-and-babylonian-libraries":     {"status": "names-only"},   # ISBE scholarly; archaeological
    # ISBE demonym; Easton has assyria.json (2 Kgs 15:19; Isa 36)
    "assyrians":                             {"status": "redirect-only", "redirect_to": "assyria"},
    "astad":                                 {"status": "names-only"},   # ISBE; obscure variant
    # ISBE combined; Easton has ashtoreth.json (Canaanite goddess; 1 Kgs 11:5)
    "astarte;-astoreth":                     {"status": "redirect-only", "redirect_to": "ashtoreth"},
    "astath":                                {"status": "names-only"},   # ISBE; obscure; 1 Esd variant
    "astonished;-astonied":                  {"status": "names-only"},   # ISBE word study (KJV "astonied")
    "astonishment":                          {"status": "names-only"},   # ISBE word study
    "astray":                                {"status": "names-only"},   # ISBE word study
    "astrology":                             {"status": "names-only"},   # ISBE; divination; Isa 47:13; general
    "astyages":                              {"status": "names-only"},   # ISBE; Median king; apocryphal Daniel
    "asunder":                               {"status": "names-only"},   # ISBE word study
    "asuppim;-house-of-asuppim":             {"status": "names-only"},   # ISBE; 1 Chr 26:15 storehouse
    "asur":                                  {"status": "names-only"},   # ISBE; 1 Esd 5:16 variant
    "asylum":                                {"status": "names-only"},   # ISBE; cities of refuge concept; general
    "at-one":                                {"status": "names-only"},   # ISBE word study; archaic "at one = reconciled"
    "atar":                                  {"status": "names-only"},   # ISBE; 1 Esd variant; apocryphal
    "atargatis":                             {"status": "names-only"},   # ISBE; Syrian goddess (2 Macc 12:26)
    "aterezaias":                            {"status": "names-only"},   # ISBE; 1 Esd variant; apocryphal
    "atergatis":                             {"status": "names-only"},   # ISBE variant of atargatis
    "ateta":                                 {"status": "names-only"},   # ISBE; 1 Esd variant; apocryphal
    "athanasian;-creed":                     {"status": "names-only"},   # ISBE; Athanasian Creed; score-5 → names-only
    "atharias":                              {"status": "names-only"},   # ISBE; 1 Esd variant; apocryphal
    "atharim":                               {"status": "names-only"},   # ISBE; Num 21:1 "way of Atharim"
    "atheism":                               {"status": "names-only"},   # ISBE theological concept; score-5 → names-only
    "athenobius":                            {"status": "names-only"},   # ISBE; Seleucid envoy (1 Macc 15:28)
    "atipha":                                {"status": "names-only"},   # ISBE; 1 Esd 5:32 variant; apocryphal
    "atroth-beth-joab":                      {"status": "names-only"},   # ISBE place; 1 Chr 2:54; Judah genealogy
    "atroth-shophan":                        {"status": "names-only"},   # ISBE place; Num 32:35; Gadite city
    "attain":                                {"status": "names-only"},   # ISBE word study
    "attend;-attendance":                    {"status": "names-only"},   # ISBE word study
    "attent;-attentive":                     {"status": "names-only"},   # ISBE word study (KJV 2 Chr 6:40)
    "attharates":                            {"status": "names-only"},   # ISBE; 1 Esd variant of Tirshatha; apocryphal
    "attharias;-atharias":                   {"status": "names-only"},   # ISBE combined; 1 Esd variant; apocryphal
    "attire;-dyed-attire":                   {"status": "names-only"},   # ISBE; Ezek 23:15 clothing; general
    "attitudes":                             {"status": "names-only"},   # ISBE word study; prayer postures
    "attus":                                 {"status": "names-only"},   # ISBE; 1 Esd variant; apocryphal
    "audience":                              {"status": "names-only"},   # ISBE word study
    "augia":                                 {"status": "names-only"},   # ISBE; 1 Esd variant; apocryphal
    "augurs-oak":                            {"status": "names-only"},   # ISBE; Judg 9:37 "diviners' oak"
    "augury":                                {"status": "names-only"},   # ISBE; divination; general
    "augustan;-augustan-band":               {"status": "names-only"},   # ISBE; Acts 27:1 Roman cohort
    "aul":                                   {"status": "names-only"},   # KJV "awl" (Deut 15:17); word study
    "aunt":                                  {"status": "names-only"},   # ISBE word study
    "austere":                               {"status": "names-only"},   # ISBE word study (Luke 19:21-22)
    "author":                                {"status": "names-only"},   # ISBE word study
    "authority-in-religion":                 {"status": "names-only"},   # ISBE theological concept; score-5
    "authority;-authority-in-general":       {"status": "names-only"},   # ISBE combined; score-5
    "authorized-version":                    {"status": "names-only"},   # ISBE; KJV 1611; general reference
    "autranitis":                            {"status": "names-only"},   # ISBE place; Hauran/Bashan region
    "avail":                                 {"status": "names-only"},   # ISBE word study
    "avaran":                                {"status": "names-only"},   # ISBE; Eleazar Maccabee's surname (1 Macc 2:5)
    "avenge;-avenger":                       {"status": "names-only"},   # ISBE word study
    "averse":                                {"status": "names-only"},   # ISBE word study (Mic 2:8)
    "avims":                                 {"status": "names-only"},   # ISBE variant of Avvim (Deut 2:23)
    "avites":                                {"status": "names-only"},   # ISBE; people of Avva (2 Kgs 17:31)
    "avoid":                                 {"status": "names-only"},   # ISBE word study
    "avouch":                                {"status": "names-only"},   # KJV "declare" (Deut 26:17-18); word study
    "avvim;-avites":                         {"status": "names-only"},   # ISBE combined variant of avims/avites
    "awa":                                   {"status": "names-only"},   # ISBE; 1 Esd variant; apocryphal
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
    print(f'BPG Curation C27: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
