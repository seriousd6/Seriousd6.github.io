"""
BPG Curation — Batch C06: shashai → presumption (gaps 501–600)
Gaps reviewed: 100 (smith-person S–Z names, then doctrine/concept gaps)

Transition batch: gaps 501–581 are final smith-person/place minor entries;
gaps 582–600 are doctrine-no-article / concept-no-article with Nave verse counts.
All doctrine/concept entries (582–600) get stub-needed except one Nave
organizational category (meteorology-and-celestial-phenomena).

Notable smith stubs: Shinar (Babel plain), Shishak (Pharaoh invader),
Silvanus (= Silas, Paul's companion), Tiberius (emperor of Luke 3:1),
Tiglath-pileser (Assyrian king), Tirzah (N. Israel capital), Tryphosa (NT).

Script: scripts/bpg-curate-06.py
Run: python3 scripts/bpg-curate-06.py  (from project root)
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
    # ── S names (smith-person/place, continued) ──────────────────────────────
    "shashai":       {"status": "names-only"},   # post-exile man with foreign wife (Ezra 10:40)
    "shashak":       {"status": "names-only"},   # Benjamin's son (1 Chr 8:14)
    "sheariah":      {"status": "names-only"},   # Saul's descendant (1 Chr 8:38)
    "shebam":        {"status": "names-only"},   # Reuben city, alternate for Sibmah (Num 32:3)
    "sheber":        {"status": "names-only"},   # Caleb's son by Maacah (1 Chr 2:48)
    "shedeur":       {"status": "names-only"},   # leader of Reuben (Num 1:5)
    "shehariah":     {"status": "names-only"},   # Benjamin's son (1 Chr 8:26)
    "sheleph":       {"status": "names-only"},   # son of Joktan (Gen 10:26)
    "shelesh":       {"status": "names-only"},   # Asher's son (1 Chr 7:35)
    "shelomi":       {"status": "names-only"},   # Asher's leader (Num 34:27)
    "shelumiel":     {"status": "names-only"},   # leader of Simeon (Num 1:6)
    "shemer":        {"status": "names-only"},   # owner of Samaria hill sold to Omri (1 Kgs 16:24)
    "shenazar":      {"status": "names-only"},   # Jehoiachin's son (1 Chr 3:18)
    "sherah":        {"status": "names-only"},   # Ephraim's daughter who built towns (1 Chr 7:24)
    "sheshan":       {"status": "names-only"},   # Judah descendant (1 Chr 2:31)
    "shicron":       {"status": "names-only"},   # Judah border landmark (Josh 15:11)
    "shilhi":        {"status": "names-only"},   # Jehoshaphat's maternal grandfather (1 Kgs 22:42)
    "shilshah":      {"status": "names-only"},   # Asher's son (1 Chr 7:37)
    "shimon":        {"status": "names-only"},   # Judah descendant (1 Chr 4:20)
    "shimrith":      {"status": "names-only"},   # Moabite mother of Jehoash's assassin (2 Chr 24:26)
    # Babylonian plain where Tower of Babel stood; temple plunder taken here (Dan 1:2; Isa 11:11)
    "shinar":        {"status": "stub-needed"},
    "shiphi":        {"status": "names-only"},   # Simeon's prince (1 Chr 4:37)
    "shisha":        {"status": "names-only"},   # father of Solomon's secretaries (1 Kgs 4:3)
    # Pharaoh who invaded Judah under Rehoboam, looted temple (1 Kgs 14:25-26; 2 Chr 12)
    "shishak":       {"status": "stub-needed"},
    "shiza":         {"status": "names-only"},   # Reubenite, father of David's warrior (1 Chr 11:42)
    "shobek":        {"status": "names-only"},   # covenant signer (Neh 10:24)
    "shochoh":       {"status": "names-only"},   # Judah town near Goliath battle (1 Sam 17:1)
    "shoham":        {"status": "names-only"},   # Merari Levite (1 Chr 24:27)
    "shophach":      {"status": "names-only"},   # Syrian army commander (1 Chr 19:16,18)
    "shual":         {"status": "names-only"},   # Asher's son / land of Shual (1 Chr 7:36; 1 Sam 13:17)
    "shubael":       {"status": "names-only"},   # two Levites (1 Chr 24:20; 25:20)
    "shuham":        {"status": "names-only"},   # Dan's son (Num 26:42)
    # NT missionary: Paul's companion on second journey; secretary of 1 Peter (Acts 15:40; 1 Pet 5:12)
    "silvanus":      {"status": "stub-needed"},
    "sippai":        {"status": "names-only"},   # Philistine giant (1 Chr 20:4)
    "sisamai":       {"status": "names-only"},   # Sheshan's son (1 Chr 2:40)
    "sodi":          {"status": "names-only"},   # Zebulun's spy (Num 13:10)
    "sophereth":     {"status": "names-only"},   # temple servant family (Ezra 2:55)
    "sotai":         {"status": "names-only"},   # temple servant family (Ezra 2:55)
    "suah":          {"status": "names-only"},   # Asher's son (1 Chr 7:36)

    # ── T names ──────────────────────────────────────────────────────────────
    "tahrea":        {"status": "names-only"},   # Saul's descendant (1 Chr 9:41)
    "tamah":         {"status": "names-only"},   # temple servant family (Ezra 2:53)
    "tanach":        {"status": "names-only"},   # variant of Taanach (Josh 17:11)
    "taphath":       {"status": "names-only"},   # Solomon's daughter (1 Kgs 4:11)
    "taralah":       {"status": "names-only"},   # Benjamin town (Josh 18:27)
    "tarea":         {"status": "names-only"},   # Saul's descendant (1 Chr 8:35)
    "tebah":         {"status": "names-only"},   # Nahor's son (Gen 22:24)
    "tebaliah":      {"status": "names-only"},   # Levite gatekeeper (1 Chr 26:11)
    "tehinnah":      {"status": "names-only"},   # Judah descendant (1 Chr 4:12)
    "telah":         {"status": "names-only"},   # Ephraim's ancestor (1 Chr 7:25)
    "thamah":        {"status": "names-only"},   # temple servant family, variant of Tamah (Ezra 2:53)
    "thelasar":      {"status": "names-only"},   # Assyrian-held territory (2 Kgs 19:12; Isa 37:12)
    # Roman emperor (14–37 AD); Luke 3:1 dates John the Baptist's ministry to his reign
    "tiberius":      {"status": "stub-needed"},
    # Assyrian king who deported northern Israel; key figure in 2 Kgs 15-16 (2 Kgs 15:29; 16:7-10)
    "tiglathpileser":{"status": "stub-needed"},
    "tilon":         {"status": "names-only"},   # Judah descendant (1 Chr 4:20)
    "tiria":         {"status": "names-only"},   # Judah descendant (1 Chr 4:16)
    # City of northern Israel: first capital after Jeroboam; Zelophehad's daughter's inheritance (1 Kgs 14:17)
    "tirzah":        {"status": "stub-needed"},
    "toah":          {"status": "names-only"},   # Levite (1 Chr 6:34)
    "tryphon":       {"status": "names-only"},   # Maccabean-era figure; not in canonical OT/NT
    # NT woman greeted by Paul alongside Tryphena (Rom 16:12); likely deaconess at Rome
    "tryphosa":      {"status": "stub-needed"},

    # ── U–Z names ────────────────────────────────────────────────────────────
    "uel":           {"status": "names-only"},   # post-exile man with foreign wife (Ezra 10:34)
    "ulam":          {"status": "names-only"},   # two OT figures (1 Chr 7:16; 8:39)
    "ulla":          {"status": "names-only"},   # Asher's son (1 Chr 7:39)
    "uri":           {"status": "names-only"},   # three OT figures (father of Bezalel; Solomon's officer; Ezra)
    "uthai":         {"status": "names-only"},   # two OT figures (1 Chr 9:4; Ezra 8:14)
    "uzai":          {"status": "names-only"},   # father of wall-builder Palal (Neh 3:25)
    "vaniah":        {"status": "names-only"},   # post-exile man with foreign wife (Ezra 10:36)
    "vashni":        {"status": "names-only"},   # Samuel's firstborn (1 Chr 6:28 KJV)
    "vophsi":        {"status": "names-only"},   # Naphtali's spy (Num 13:14)
    "zaham":         {"status": "names-only"},   # Rehoboam's son (2 Chr 11:19)
    "zalaph":        {"status": "names-only"},   # father of wall-builder Hanun (Neh 3:30)
    "zareah":        {"status": "names-only"},   # alternate form of Zorah (Neh 11:29)
    "zebina":        {"status": "names-only"},   # post-exile man with foreign wife (Ezra 10:43)
    "zelzah":        {"status": "names-only"},   # landmark near Rachel's tomb (1 Sam 10:2)
    "zenan":         {"status": "names-only"},   # Judah town (Josh 15:37)
    "zer":           {"status": "names-only"},   # Naphtali fortified city (Josh 19:35)
    "zerahiah":      {"status": "names-only"},   # three OT figures (1 Chr 6:6; Ezra 7:4; 8:4)
    "zereth":        {"status": "names-only"},   # Judah descendant (1 Chr 4:7)
    "zeror":         {"status": "names-only"},   # Benjamin's ancestor, Saul's forefather (1 Sam 9:1)
    "zethar":        {"status": "names-only"},   # Persian eunuch (Esth 1:10)
    # Greek/NT form of Zerubbabel (Matt 1:12; Luke 3:27)
    "zorobabel":     {"status": "redirect-only", "redirect_to": "zerubbabel"},
    "zuar":          {"status": "names-only"},   # father of Nethaneel (Num 1:8)

    # ── Doctrine / concept gaps (gaps 582–600) ───────────────────────────────
    # All have no or few Nave verses but are significant theological topics
    "eternal-punishment":              {"status": "stub-needed"},
    "fight-of-faith":                  {"status": "stub-needed"},
    "kingdom-of-satan":                {"status": "stub-needed"},
    "plan-of-salvation":               {"status": "stub-needed"},
    "reconciliation":                  {"status": "stub-needed"},
    "wrath":                           {"status": "stub-needed"},
    "animals":                         {"status": "stub-needed"},  # 163 Nave verses
    "apostles":                        {"status": "stub-needed"},  # 108 Nave verses
    "character":                       {"status": "stub-needed"},  # 196 Nave verses (>150 threshold)
    "citizens":                        {"status": "stub-needed"},  # 103 Nave verses; heavenly citizenship theme
    "depravity-of-man":                {"status": "stub-needed"},  # 120 Nave verses; core doctrine
    "impenitence":                     {"status": "stub-needed"},  # 163 Nave verses; biblical warning
    "infidelity":                      {"status": "stub-needed"},  # 143 Nave verses; unfaithfulness to God
    "judgments":                       {"status": "stub-needed"},  # 110 Nave verses; God's acts of judgment
    "liberality":                      {"status": "stub-needed"},  # 178 Nave verses; generosity virtue
    "malice":                          {"status": "stub-needed"},  # 182 Nave verses; significant vice
    # Nave organizational category for weather/stars, not a theological concept
    "meteorology-and-celestial-phenomena": {"status": "skip"},
    "parents":                         {"status": "stub-needed"},  # 125 Nave verses; pastoral/ethical
    "presumption":                     {"status": "stub-needed"},  # 104 Nave verses; sin of presumption
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
    print(f'BPG Curation C06: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
