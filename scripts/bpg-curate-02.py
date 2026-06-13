"""
BPG Curation — Batch C02: azor → elpaal (gaps 101–200)
Gaps reviewed: 100 (all priority-35 smith-person/smith-place, A–E names)

All entries have 0 Nave verses. Decisions based on whether the figure/place
has a notable biblical narrative (stub-needed), is an alternate spelling of
a covered term (redirect-only), or is a minor genealogy/list entry (names-only).

Script: scripts/bpg-curate-02.py
Run: python3 scripts/bpg-curate-02.py  (from project root)
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
    # ── A names (continued from C01) ────────────────────────────────────────
    "azor":          {"status": "names-only"},   # NT genealogy only (Matt 1:13-14)
    "azriel":        {"status": "names-only"},   # three minor OT figures
    "azrikam":       {"status": "names-only"},   # four minor OT figures
    "azur":          {"status": "names-only"},   # two minor OT figures (Jer 28:1; Ezek 11:1)
    "azzan":         {"status": "names-only"},   # father of tribal prince Paltiel (Num 34:26)
    "azzur":         {"status": "names-only"},   # covenant signer (Neh 10:17)

    # ── B names ──────────────────────────────────────────────────────────────
    "baara":         {"status": "names-only"},   # wife of Shaharaim (1 Chr 8:8)
    # Pilgrim valley of Psalm 84:6 ("valley of weeping/balsam"); significant poetic image
    "baca":          {"status": "stub-needed"},
    "barachias":     {"status": "names-only"},   # father of Zechariah (Matt 23:35), no narrative of his own
    "bebai":         {"status": "names-only"},   # returned-exile family (Ezra 2:11)
    "bechorath":     {"status": "names-only"},   # Saul's ancestor, genealogy only (1 Sam 9:1)
    "bedad":         {"status": "names-only"},   # father of Edomite king Hadad (Gen 36:35)
    # David's son also called Eliada; variant name only
    "beeliada":      {"status": "redirect-only", "redirect_to": "eliada"},
    "beera":         {"status": "names-only"},   # two minor OT figures (1 Chr 5:6; 7:37)
    "ben":           {"status": "names-only"},   # Levite gatekeeper, list (1 Chr 15:18)
    "beneberak":     {"status": "names-only"},   # Dan border town (Josh 19:45)
    "benhail":       {"status": "names-only"},   # official sent to teach (2 Chr 17:7)
    "benhanan":      {"status": "names-only"},   # son of Shimon (1 Chr 4:20)
    "beno":          {"status": "names-only"},   # Merari Levite (1 Chr 24:26-27)
    # Rachel's dying name for Benjamin; the article lives under "Benjamin"
    "benoni":        {"status": "redirect-only", "redirect_to": "benjamin"},
    "benzoheth":     {"status": "names-only"},   # son of Ishi (1 Chr 4:20)
    "berachiah":     {"status": "names-only"},   # father of Asaph the musician (1 Chr 6:39)
    "beraiah":       {"status": "names-only"},   # son of Shimei (1 Chr 8:21)
    "beri":          {"status": "names-only"},   # Asher descendant (1 Chr 7:36)
    # Canaanite god Baal-Berith worshipped at Shechem; key to Abimelech narrative (Judg 9:4,46)
    "berith":        {"status": "stub-needed"},
    "besai":         {"status": "names-only"},   # temple servant family (Ezra 2:49)
    "besodeiah":     {"status": "names-only"},   # father of wall-builder Meshullam (Neh 3:6)
    "beten":         {"status": "names-only"},   # Asher border town (Josh 19:25)
    "bethbaalmeon":  {"status": "names-only"},   # alternate name for Baal Meon; no distinct article
    "bethemek":      {"status": "names-only"},   # Asher border town (Josh 19:27)
    "bethgader":     {"status": "names-only"},   # Judah locality (1 Chr 2:51)
    "bethharan":     {"status": "names-only"},   # Gad city (Num 32:36)
    "bethlebaoth":   {"status": "names-only"},   # Simeon town (Josh 19:6)
    "bethmarcaboth": {"status": "names-only"},   # Simeon town (Josh 19:5)
    "bethmeon":      {"status": "names-only"},   # short form of Beth Baal Meon (Jer 48:23)
    "bethnimrah":    {"status": "names-only"},   # Gad city (Num 32:36)
    "bethpalet":     {"status": "names-only"},   # Judah town (Josh 15:27)
    "bethpazzez":    {"status": "names-only"},   # Issachar town (Josh 19:21)
    "bethphelet":    {"status": "names-only"},   # Judah town (Neh 11:26)
    "bethrapha":     {"status": "names-only"},   # son of Eshton (1 Chr 4:12)
    "betonim":       {"status": "names-only"},   # Gad town (Josh 13:26)
    "bezai":         {"status": "names-only"},   # returned-exile family (Ezra 2:17)
    "bichri":        {"status": "names-only"},   # father of rebel Sheba (2 Sam 20:1)
    "bidkar":        {"status": "names-only"},   # Jehu's officer (2 Kgs 9:25)
    "bigvai":        {"status": "names-only"},   # returned-exile leader (Ezra 2:2)
    "bileam":        {"status": "names-only"},   # Manasseh Levite town (1 Chr 6:70)
    "binea":         {"status": "names-only"},   # Saul's descendant (1 Chr 8:37)
    "binnui":        {"status": "names-only"},   # several post-exile figures
    "bithiah":       {"status": "names-only"},   # daughter of Pharaoh, wife of Mered (1 Chr 4:18)
    "bocheru":       {"status": "names-only"},   # Saul's descendant (1 Chr 8:38)
    "bohan":         {"status": "names-only"},   # stone marker on tribal border (Josh 15:6)
    "bukki":         {"status": "names-only"},   # two OT figures (Levite Num 3:4; Dan prince Num 34:22)
    "bukkiah":       {"status": "names-only"},   # Levite musician (1 Chr 25:4)
    "bunah":         {"status": "names-only"},   # son of Jerahmeel (1 Chr 2:25)
    "bunni":         {"status": "names-only"},   # two Levite figures (Neh 9:4; 11:15)

    # ── C names ──────────────────────────────────────────────────────────────
    "cabbon":        {"status": "names-only"},   # Judah town (Josh 15:40)
    "carcas":        {"status": "names-only"},   # Persian eunuch (Esth 1:10)
    "careah":        {"status": "names-only"},   # father of Johanan (2 Kgs 25:23)
    # NT figure; kept Paul's cloak and scrolls at Troas (2 Tim 4:13)
    "carpus":        {"status": "stub-needed"},
    "carshena":      {"status": "names-only"},   # Persian noble (Esth 1:14)
    "chalcol":       {"status": "names-only"},   # wise man surpassed by Solomon (1 Kgs 4:31)
    # Major battle site (605 BC) where Nebuchadnezzar defeated Egypt; appears in Jer 46:2
    "charchemish":   {"status": "stub-needed"},
    "chelal":        {"status": "names-only"},   # post-exile man (Ezra 10:30)
    "chelluh":       {"status": "names-only"},   # post-exile man (Ezra 10:35)
    "chelub":        {"status": "names-only"},   # two OT figures (1 Chr 4:11; 27:26)
    # Alternate name for Caleb son of Hezron (1 Chr 2:9)
    "chelubai":      {"status": "redirect-only", "redirect_to": "caleb"},
    "chenaniah":     {"status": "names-only"},   # Levite music leader (1 Chr 15:22)
    "cheran":        {"status": "names-only"},   # Horite son (Gen 36:26)
    "chislon":       {"status": "names-only"},   # father of prince Elidad (Num 34:21)
    "chislothtabor": {"status": "names-only"},   # Zebulun border town (Josh 19:12)
    # Greek form of Kish, father of Saul (Acts 13:21)
    "cis":           {"status": "redirect-only", "redirect_to": "kish"},
    "colhozeh":      {"status": "names-only"},   # post-exile figure (Neh 3:15)
    # KJV form of Jeconiah/Jehoiachin (Jer 22:24,28)
    "coniah":        {"status": "redirect-only", "redirect_to": "jehoiachin"},
    "cosam":         {"status": "names-only"},   # NT genealogy (Luke 3:28)
    "coz":           {"status": "names-only"},   # Judah descendant (1 Chr 4:8)
    # Midianite woman killed by Phinehas during Baal-Peor plague (Num 25:15-18)
    "cozbi":         {"status": "stub-needed"},

    # ── D names ──────────────────────────────────────────────────────────────
    "dabareh":       {"status": "names-only"},   # Issachar town (Josh 19:12)
    "dalaiah":       {"status": "names-only"},   # son of Elioenai (1 Chr 3:24)
    "dalphon":       {"status": "names-only"},   # Haman's son (Esth 9:7)
    "darkon":        {"status": "names-only"},   # servant of Solomon (Ezra 2:56)
    "dekar":         {"status": "names-only"},   # father of one of Solomon's officers (1 Kgs 4:9)
    "diblath":       {"status": "names-only"},   # place in Ezek 6:14 (likely Riblah)
    "dibri":         {"status": "names-only"},   # father of the blasphemer (Lev 24:11)
    "diklah":        {"status": "names-only"},   # son of Joktan (Gen 10:27)
    "dilean":        {"status": "names-only"},   # Judah town (Josh 15:38)

    # ── E names ──────────────────────────────────────────────────────────────
    "ebiasaph":      {"status": "names-only"},   # Levite (1 Chr 6:23; also Abiasaph variant)
    "eker":          {"status": "names-only"},   # son of Ram (1 Chr 2:27)
    "eldaah":        {"status": "names-only"},   # son of Midian (Gen 25:4)
    "elead":         {"status": "names-only"},   # Ephraim descendant killed in raid (1 Chr 7:21)
    "eleph":         {"status": "names-only"},   # Benjamin town (Josh 18:28)
    "eliah":         {"status": "names-only"},   # David's brother and a Reubenite (1 Chr 27:18)
    "eliahba":       {"status": "names-only"},   # one of David's thirty warriors (2 Sam 23:32)
    "eliasaph":      {"status": "names-only"},   # two OT tribal leaders (Num 1:14; 3:24)
    "elienai":       {"status": "names-only"},   # son of Shimei (1 Chr 8:20)
    "elihoreph":     {"status": "names-only"},   # Solomon's secretary (1 Kgs 4:3)
    "eliphal":       {"status": "names-only"},   # one of David's warriors (1 Chr 11:35)
    "eliud":         {"status": "names-only"},   # NT genealogy (Matt 1:14-15)
    "elizur":        {"status": "names-only"},   # leader of Reuben (Num 1:5)
    "elnaam":        {"status": "names-only"},   # father of two of David's warriors (1 Chr 11:46)
    "elpaal":        {"status": "names-only"},   # Benjamin descendant (1 Chr 8:11)
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
    print(f'BPG Curation C02: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
