"""
BPG Curation — Batch C01: angel-a-spirit → aznothtabor
Gaps reviewed: 100 (gaps 1–100 by priority score)

Priority 40–70 range (gaps 1–24): all major doctrine/concept/virtue gaps.
Priority 35 range (gaps 25–100): smith-person/smith-place entries, A-names.

Decisions documented below. Status values:
  stub-needed   — add to BP Phase 2 queue
  redirect-only — alias; redirect_to field set
  names-only    — minor name, low priority
  skip          — too obscure or data artifact
  already-covered — article exists

Script: scripts/bpg-curate-01.py
Run: python3 scripts/bpg-curate-01.py  (from project root)
"""

import json

GAPS_FILE = 'data/biblepedia/gaps.json'


def load_gaps():
    with open(GAPS_FILE, encoding='utf-8') as f:
        return json.load(f)


def save_gaps(gaps):
    with open(GAPS_FILE, 'w', encoding='utf-8') as f:
        json.dump(gaps, f, ensure_ascii=False, indent=2)


# Curation decisions: { id: { status, redirect_to? } }
# ─────────────────────────────────────────────────────
# Priority 70–40 (gaps 1–24): high-value doctrine/concept/virtue topics
# ─────────────────────────────────────────────────────
DECISIONS = {
    # ── Priority 70 ──────────────────────────────────────────────────────────
    "angel-a-spirit":              {"status": "stub-needed"},
    "obedience":                   {"status": "stub-needed"},

    # ── Priority 60 ──────────────────────────────────────────────────────────
    "judgment":                    {"status": "stub-needed"},

    # ── Priority 50 ──────────────────────────────────────────────────────────
    "afflictions-and-adversities": {"status": "stub-needed"},
    "grace-of-god":                {"status": "stub-needed"},
    "jesus-the-christ":            {"status": "stub-needed"},
    "minister-christian":          {"status": "stub-needed"},
    # Nave organizational cross-reference category, not a stand-alone topic
    "quotations-and-allusions":    {"status": "skip"},
    "righteous":                   {"status": "stub-needed"},
    "wicked-people":               {"status": "stub-needed"},

    # ── Priority 40 ──────────────────────────────────────────────────────────
    "angel-holy-trinity":          {"status": "stub-needed"},
    # Generic military term; no theological concept to anchor an article
    "armies":                      {"status": "skip"},
    "backsliders":                 {"status": "stub-needed"},
    "church-and-state":            {"status": "stub-needed"},
    "commandments":                {"status": "stub-needed"},
    "hypocrisy":                   {"status": "stub-needed"},
    "israel-prophecies-concerning":{"status": "stub-needed"},
    "kingdom-of-heaven":           {"status": "stub-needed"},
    "pride":                       {"status": "stub-needed"},
    "prophets":                    {"status": "stub-needed"},
    "rulers":                      {"status": "stub-needed"},
    # Nave meta-category for figurative speech; not a theological topic
    "symbols-and-similitudes":     {"status": "skip"},
    "thankfulness":                {"status": "stub-needed"},
    "zeal-religious":              {"status": "stub-needed"},

    # ─────────────────────────────────────────────────────────────────────────
    # Priority 35 smith-person/smith-place entries (gaps 25–100)
    # Rule: stub-needed if figure has clear biblical narrative (>1 scene) or
    #       is a significant NT figure / named place with battle/journey context.
    #       redirect-only if it is an alternate spelling of another article.
    #       names-only otherwise (genealogy / list mention only).
    # ─────────────────────────────────────────────────────────────────────────
    "abelmaim":       {"status": "names-only"},   # alternate name for Abel-beth-maacah (2 Chr 16:4)
    "abiezer":        {"status": "stub-needed"},  # judge/mighty-man; two distinct biblical figures
    "abishalom":      {"status": "redirect-only", "redirect_to": "absalom"},  # variant spelling (1 Kgs 15:2)
    "abiud":          {"status": "names-only"},   # genealogy only (Matt 1:13)
    "achaicus":       {"status": "stub-needed"},  # Corinthian Christian who visited Paul (1 Cor 16:17)
    "achim":          {"status": "names-only"},   # genealogy only (Matt 1:14)
    "adadah":         {"status": "names-only"},   # border town of Judah (Josh 15:22)
    "adaiah":         {"status": "names-only"},   # multiple minor figures, no single clear narrative
    "adami":          {"status": "names-only"},   # border landmark (Josh 19:33)
    "adithaim":       {"status": "names-only"},   # Judah town, single mention (Josh 15:36)
    "admatha":        {"status": "names-only"},   # Persian noble, list only (Esth 1:14)
    "adna":           {"status": "names-only"},   # two minor post-exile figures
    "adonizedek":     {"status": "stub-needed"},  # Canaanite king; led coalition vs. Joshua (Josh 10)
    "adoraim":        {"status": "names-only"},   # fortified by Rehoboam (2 Chr 11:9)
    "aeneas":         {"status": "stub-needed"},  # paralytic healed by Peter at Lydda (Acts 9:32-35)
    "agar":           {"status": "redirect-only", "redirect_to": "hagar"},  # KJV spelling (Gal 4:24)
    "agrippa":        {"status": "stub-needed"},  # Herod Agrippa II; Paul's defense (Acts 25–26)
    "aharah":         {"status": "names-only"},   # son of Benjamin, genealogy (1 Chr 8:1)
    "ahasbai":        {"status": "names-only"},   # father of one of David's warriors (2 Sam 23:34)
    "ahi":            {"status": "names-only"},   # two minor Gad/Asher figures
    "ahian":          {"status": "names-only"},   # son of Shemida (1 Chr 7:19)
    "ahilud":         {"status": "names-only"},   # father of the recorder, list context
    "ahimoth":        {"status": "names-only"},   # Levite musician, list (1 Chr 6:25)
    "ahiram":         {"status": "names-only"},   # son of Benjamin, clan head (Num 26:38)
    "ahisamach":      {"status": "names-only"},   # father of craftsman Oholiab (Exod 31:6)
    "ahumai":         {"status": "names-only"},   # son of Jahath (1 Chr 4:2)
    "aiah":           {"status": "names-only"},   # two minor OT figures (Rizpah's father)
    "aiath":          {"status": "names-only"},   # place in Isaiah's Assyrian march poem (Isa 10:28)
    "alammelech":     {"status": "names-only"},   # Asher border town (Josh 19:26)
    "alian":          {"status": "names-only"},   # Edomite chief (1 Chr 1:40)
    "almondiblathaim":{"status": "names-only"},   # wilderness camp (Num 33:46-47)
    "alvah":          {"status": "names-only"},   # Edomite chief (Gen 36:40)
    "amad":           {"status": "names-only"},   # Asher town, single mention (Josh 19:26)
    "amal":           {"status": "names-only"},   # Asher descendant (1 Chr 7:35)
    "aman":           {"status": "names-only"},   # place in Judah (Josh 15:26)
    "ami":            {"status": "names-only"},   # servant of Solomon (Ezra 2:57)
    "amok":           {"status": "names-only"},   # priestly family head (Neh 12:7)
    "amzi":           {"status": "names-only"},   # two minor Levite figures
    "anaharath":      {"status": "names-only"},   # Issachar border town (Josh 19:19)
    "anani":          {"status": "names-only"},   # son of Elioenai (1 Chr 3:24)
    "aniam":          {"status": "names-only"},   # Manasseh descendant (1 Chr 7:19)
    "antothijah":     {"status": "names-only"},   # son of Shashak (1 Chr 8:24)
    "anub":           {"status": "names-only"},   # Judah descendant (1 Chr 4:8)
    "aphek":          {"status": "stub-needed"},  # multiple significant battle sites (1 Sam 4; 1 Kgs 20)
    "aphiah":         {"status": "names-only"},   # Saul's ancestor, genealogy (1 Sam 9:1)
    "appaim":         {"status": "names-only"},   # Jerahmeel's son (1 Chr 2:30-31)
    "ara":            {"status": "names-only"},   # Asher descendant (1 Chr 7:38)
    "arah":           {"status": "names-only"},   # multiple minor figures / returned-exile family
    "areli":          {"status": "names-only"},   # son of Gad (Gen 46:16)
    "artemas":        {"status": "stub-needed"},  # Paul's companion sent to Titus (Titus 3:12)
    "arumah":         {"status": "names-only"},   # Abimelech's residence (Judg 9:41)
    "asaiah":         {"status": "names-only"},   # multiple minor Levite/Simeon figures
    "asareel":        {"status": "names-only"},   # Judah descendant (1 Chr 4:16)
    "ashan":          {"status": "names-only"},   # Simeon city in Judah (Josh 15:42)
    "ashima":         {"status": "stub-needed"},  # deity of Hamath worshipped in Samaria (2 Kgs 17:30)
    "ashnah":         {"status": "names-only"},   # two Judah towns (Josh 15:33, 43)
    "ashriel":        {"status": "names-only"},   # Manasseh descendant (1 Chr 7:14)
    "ashur":          {"status": "stub-needed"},  # son of Shem; eponym of Assyria (Gen 10:22)
    "asiel":          {"status": "names-only"},   # Simeon ancestor (1 Chr 4:35)
    "asriel":         {"status": "names-only"},   # Manasseh clan head (Num 26:31)
    "assir":          {"status": "names-only"},   # three minor Levite figures
    "assur":          {"status": "redirect-only", "redirect_to": "ashur"},  # alternate spelling
    "asyncritus":     {"status": "stub-needed"},  # Roman Christian greeted by Paul (Rom 16:14)
    "atarah":         {"status": "names-only"},   # wife of Jerahmeel (1 Chr 2:26)
    "athach":         {"status": "names-only"},   # city in Judah (1 Sam 30:30)
    "athaiah":        {"status": "names-only"},   # post-exile settler (Neh 11:4)
    "athlai":         {"status": "names-only"},   # post-exile man with foreign wife (Ezra 10:28)
    "attai":          {"status": "names-only"},   # three minor OT figures
    "attalia":        {"status": "stub-needed"},  # seaport in Pamphylia; Paul's return (Acts 14:25)
    "avith":          {"status": "names-only"},   # Edom capital under Hadad (Gen 36:35)
    "azaliah":        {"status": "names-only"},   # Shaphan's father (2 Kgs 22:3)
    "azaniah":        {"status": "names-only"},   # Levite who sealed covenant (Neh 10:9)
    "azaz":           {"status": "names-only"},   # Reuben descendant (1 Chr 5:8)
    "azgad":          {"status": "names-only"},   # returned-exile family (Ezra 2:12)
    "azmon":          {"status": "names-only"},   # southern border of Canaan (Num 34:4)
    "aznothtabor":    {"status": "names-only"},   # Naphtali border mark (Josh 19:34)
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
    print(f'BPG Curation C01: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
