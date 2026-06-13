"""
BPG Curation — Batch C13: ar → shaalbonite (gaps 1200–1299)
Gaps reviewed: 100 (score-20 concepts/persons + score-15 isbe-only entries)

Batch includes important score-20 concepts (Pilate, Types, Vanity, Sorcery,
Preaching, Watchfulness) alongside the first wave of isbe-only entries (score-15)
which are almost all minor variants and demonyms.
Key stubs: Pilate, Preaching, Prisoners, Types, Sorcery, Thaddeus, Vanity,
Waiting, Watchfulness, Tryphena, Theft-and-thieves, Reprobacy.
11 redirects: Prisca→Priscilla, Achaz→Ahaz, Aminadab→Amminadab,
Askelon→Ashkelon, Joakim→Jehoiakim, Judaea→Judah, Kadesh-barnea→Kadesh,
Maleleel→Mahalalel, Noe→Noah, Palestina→Philistia, Pontius→Pilate.
1 skip: Readings-select (Nave organizational category).

Script: scripts/bpg-curate-13.py
Run: python3 scripts/bpg-curate-13.py  (from project root)
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
    # ── Score-20 entries (ar–zophim) ─────────────────────────────────────────
    "ar":               {"status": "names-only"},   # capital city of Moab (Num 21:28; Isa 15:1)
    "nephishesim":      {"status": "names-only"},   # temple servant family (Neh 7:52 variant)
    "nephusim":         {"status": "names-only"},   # temple servant family (Ezra 2:50 variant)
    # Repentant sinners: Prodigal son, tax collector (Luke 18:13), thief on cross (Luke 23:40-42)
    "penitent":         {"status": "stub-needed"},
    "perazim":          {"status": "names-only"},   # Baal-perazim: David's victory site (2 Sam 5:20)
    "phichol":          {"status": "names-only"},   # Abimelech's army commander (Gen 21:22; 26:26)
    # Roman prefect who condemned Jesus; Gospels (all four), Acts 3:13; 1 Tim 6:13; key Passion figure
    "pilate":           {"status": "stub-needed"},
    "pochereth":        {"status": "names-only"},   # temple servant family (Ezra 2:57)
    # NT preaching: kerygma; "foolishness of preaching" (1 Cor 1:21); Paul's homilies in Acts
    "preaching":        {"status": "stub-needed"},
    # Priscilla's name in Paul's letters (Rom 16:3; 1 Cor 16:19; 2 Tim 4:19)
    "prisca":           {"status": "redirect-only", "redirect_to": "priscilla"},
    # "Remember those in prison as if you were their fellow prisoner" (Heb 13:3); Joseph, Paul, Silas
    "prisoners":        {"status": "stub-needed"},
    # Nave organizational category for passages; not a theological concept
    "readings-select":  {"status": "skip"},
    # "Reprobate mind" (Rom 1:28); 2 Tim 3:8; God giving up the ungodly; Reformed doctrine of reprobation
    "reprobacy":        {"status": "stub-needed"},
    # Christian resignation: submission to God's will in suffering (Job; Eli 1 Sam 3:18; Gethsemane)
    "resignation":      {"status": "stub-needed"},
    # "Scoffers will come in the last days" (2 Pet 3:3-4); Prov 21:24; Isaiah's mockers
    "scoffing":         {"status": "stub-needed"},
    "shage":            {"status": "names-only"},   # father of David's warrior Jonathan (1 Chr 11:34)
    "shammuah":         {"status": "names-only"},   # David's son by Bathsheba (2 Sam 5:14 variant)
    "shaul":            {"status": "names-only"},   # Edomite king (Gen 36:37) and Simeon's son (Gen 46:10)
    "shaveh":           {"status": "names-only"},   # Valley of Shaveh; Abram met Melchizedek there (Gen 14:17)
    "shemida":          {"status": "names-only"},   # Manasseh's son (Num 26:32; Josh 17:2)
    "shephi":           {"status": "names-only"},   # Edomite chief (1 Chr 1:40)
    "shepho":           {"status": "names-only"},   # Edomite chief (Gen 36:23 variant of Shephi)
    "shephuphan":       {"status": "names-only"},   # Benjamin's son (1 Chr 8:5 variant of Shupham)
    "shillem":          {"status": "names-only"},   # Naphtali's son (Gen 46:24 variant of Shallum)
    "shuni":            {"status": "names-only"},   # Gad's son (Gen 46:16; Num 26:15)
    "shuthelah":        {"status": "names-only"},   # Ephraim's son (Num 26:35; 1 Chr 7:20)
    "sia":              {"status": "names-only"},   # temple servant family (Neh 7:47 variant of Siaha)
    "sibbechai":        {"status": "names-only"},   # David's warrior who killed giant (2 Sam 21:18)
    "siddim":           {"status": "names-only"},   # Valley of Siddim = Dead Sea area (Gen 14:3)
    "sinim":            {"status": "names-only"},   # Isa 49:12 distant land; probably Syene (Aswan)
    "socoh":            {"status": "names-only"},   # two Judah towns (Josh 15:35,48)
    # Divination, witchcraft; condemned (Lev 19:31; Deut 18:10-12; Gal 5:20; Rev 21:8; Acts 8:9-24)
    "sorcery":          {"status": "stub-needed"},
    "tahan":            {"status": "names-only"},   # Ephraim's son (Num 26:35; 1 Chr 7:25)
    "tahath":           {"status": "names-only"},   # three OT figures: Levite, Ephraim descendants
    # Apostle also called Lebbaeus (Matt 10:3; Mark 3:18); probably = Judas son of James (Luke 6:16)
    "thaddeus":         {"status": "stub-needed"},
    # 8th Commandment (Exod 20:15); Zacchaeus (Luke 19:8); good thief (Luke 23:40); restitution laws
    "theft-and-thieves": {"status": "stub-needed"},
    "tikvah":           {"status": "names-only"},   # two OT figures (2 Kgs 22:14; Ezra 10:15)
    "tob":              {"status": "names-only"},   # region where Jephthah fled (Judg 11:3,5)
    # NT woman who "works hard in the Lord" (Rom 16:12); listed alongside Tryphena; likely deaconess
    "tryphena":         {"status": "stub-needed"},
    # Biblical typology: Adam/Christ (Rom 5:14), Passover/Crucifixion, Tabernacle/Heaven; hermeneutical method
    "types":            {"status": "stub-needed"},
    # "Do nothing out of selfish ambition" (Phil 2:3-4); model of Christ (Phil 2:5-8); core NT virtue
    "unselfishness":    {"status": "stub-needed"},
    # הֶבֶל (hebel) = breath/vapor; "vanity of vanities" (Eccl 1:2); futility of life without God
    "vanity":           {"status": "stub-needed"},
    # "Wait for the LORD" (Ps 27:14); "those who wait on the LORD shall renew their strength" (Isa 40:31)
    "waiting":          {"status": "stub-needed"},
    # "Watch and pray" (Matt 26:41); "be sober and watchful" (1 Pet 5:8); Rev 3:2-3; eschatological theme
    "watchfulness":     {"status": "stub-needed"},
    "zepho":            {"status": "names-only"},   # Edomite chief (Gen 36:11; 1 Chr 1:36 variant Zephi)
    "zophim":           {"status": "names-only"},   # field of Zophim on Pisgah (Num 23:14)

    # ── Score-15 isbe-only entries (almost all names-only or redirects) ───────
    "abidah":           {"status": "names-only"},   # Midian's son (Gen 25:4 variant of Abida)
    # Greek form of Ahaz used in NT genealogy (Matt 1:9)
    "achaz":            {"status": "redirect-only", "redirect_to": "ahaz"},
    "adlai":            {"status": "names-only"},   # father of David's herds overseer (1 Chr 27:29)
    "ahiah":            {"status": "names-only"},   # two OT figures: Saul's priest (1 Sam 14:3); Solomon's secretary
    "ahlai":            {"status": "names-only"},   # two OT figures (1 Chr 2:31; 11:41)
    # Greek form of Amminadab used in NT genealogy (Matt 1:4; Luke 3:33)
    "aminadab":         {"status": "redirect-only", "redirect_to": "amminadab"},
    "apollonius":       {"status": "names-only"},   # Maccabean-era governor (1 Macc 1:29; 3:10); apocryphal
    # Variant spelling of Ashkelon (Judg 1:18; 14:19; Zeph 2:4)
    "askelon":          {"status": "redirect-only", "redirect_to": "ashkelon"},
    "asshurim":         {"status": "names-only"},   # son of Dedan (Gen 25:3); Arabian tribe
    "ataroth-addar":    {"status": "names-only"},   # Benjamin border town (Josh 16:5; 18:13)
    "attalus":          {"status": "names-only"},   # Attalus III of Pergamum (1 Macc 15:22); apocryphal
    "azareel":          {"status": "names-only"},   # multiple minor OT figures (1 Chr 25:18, etc.)
    "baaseiah":         {"status": "names-only"},   # Levite ancestor (1 Chr 6:40)
    "beon":             {"status": "names-only"},   # Reubenite town (Num 32:3 variant of Baal-meon)
    "beth-azmaveth":    {"status": "names-only"},   # post-exile town (Neh 7:28 variant of Azmaveth)
    "bishlam":          {"status": "names-only"},   # Persian official opposing rebuilding (Ezra 4:7)
    "bozez":            {"status": "names-only"},   # rocky cliff near Michmash (1 Sam 14:4)
    "chenani":          {"status": "names-only"},   # Levite who led public confession (Neh 9:4)
    "deuel":            {"status": "names-only"},   # father of Eliasaph (Num 1:14 variant of Reuel)
    "eladah":           {"status": "names-only"},   # Ephraim descendant (1 Chr 7:20)
    "elkoshite":        {"status": "names-only"},   # epithet for Nahum (Nah 1:1); demonym from Elkosh
    "hapharaim":        {"status": "names-only"},   # Issachar town (Josh 19:19)
    "harhas":           {"status": "names-only"},   # grandfather of Shallum (2 Kgs 22:14)
    "hattil":           {"status": "names-only"},   # temple servant family (Ezra 2:57)
    "imri":             {"status": "names-only"},   # two OT figures (1 Chr 9:4; Neh 3:2)
    "jahaziah":         {"status": "names-only"},   # post-exile figure (Ezra 10:15)
    # Greek form of Jehoiakim used in apocryphal texts
    "joakim":           {"status": "redirect-only", "redirect_to": "jehoiakim"},
    # Greek/Latin form of the Roman province Judaea
    "judaea":           {"status": "redirect-only", "redirect_to": "judah"},
    # ISBE entry for the major wilderness camp; Easton covers it under "Kadesh"
    "kadesh-barnea":    {"status": "redirect-only", "redirect_to": "kadesh"},
    "labana":           {"status": "names-only"},   # temple servant family (1 Esd 5:29 variant)
    "maadai":           {"status": "names-only"},   # post-exile man with foreign wife (Ezra 10:34)
    "maaz":             {"status": "names-only"},   # Judah descendant (1 Chr 2:27)
    "malchiel":         {"status": "names-only"},   # Asher's son (Gen 46:17; Num 26:45)
    # Greek form of Mahalalel used in NT genealogy (Luke 3:37)
    "maleleel":         {"status": "redirect-only", "redirect_to": "mahalalel"},
    "manahethites":     {"status": "names-only"},   # Judah clan (1 Chr 2:54)
    "mattatha":         {"status": "names-only"},   # NT genealogy (Luke 3:31)
    "matthanias":       {"status": "names-only"},   # Greek variant of Mattaniah; various minor figures
    "mesobaite":        {"status": "names-only"},   # epithet for Jasiel (1 Chr 11:47)
    "mishraites":       {"status": "names-only"},   # Kenite clan (1 Chr 2:53)
    "mispar":           {"status": "names-only"},   # leader of returning exiles (Ezra 2:2 variant)
    "mithnite":         {"status": "names-only"},   # epithet for Joshaphat (1 Chr 11:43)
    # Greek form of Noah used in NT (Luke 17:26; Matt 24:37; Heb 11:7)
    "noe":              {"status": "redirect-only", "redirect_to": "noah"},
    "palal":            {"status": "names-only"},   # wall-builder (Neh 3:25)
    # KJV/Hebrew form of Philistia (Exod 15:14; Isa 14:29,31)
    "palestina":        {"status": "redirect-only", "redirect_to": "philistia"},
    "parnach":          {"status": "names-only"},   # father of Elizaphan (Num 34:25)
    "parosh":           {"status": "names-only"},   # returned-exile family (Ezra 2:3)
    "pelonite":         {"status": "names-only"},   # epithet for David's warriors (1 Chr 11:27,36)
    # Name element referring to Pontius Pilate; the ISBE standalone entry for the name
    "pontius":          {"status": "redirect-only", "redirect_to": "pilate"},
    "punites":          {"status": "names-only"},   # clan of Puah/Puvah (Num 26:23)
    "pur":              {"status": "names-only"},   # "lot" used to set Purim date (Esth 3:7); covered under "purim"
    "ribai":            {"status": "names-only"},   # father of David's warrior Ittai (2 Sam 23:29)
    "salma":            {"status": "names-only"},   # Judah descendant related to David's line (1 Chr 2:11,51)
    "shaalbim":         {"status": "names-only"},   # Dan town (Josh 19:42; 1 Kgs 4:9)
    "shaalbonite":      {"status": "names-only"},   # epithet for David's warrior Eliahba (2 Sam 23:32)
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
    print(f'BPG Curation C13: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
