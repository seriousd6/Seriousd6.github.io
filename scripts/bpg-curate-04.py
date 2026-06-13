"""
BPG Curation — Batch C04: ishpan → letushim (gaps 301–400)
Gaps reviewed: 100 (all priority-35 smith-person/smith-place, I–L names)

Notable decisions:
  - joses: Barnabas's birth name (Acts 4:36) + brother of Jesus → stub-needed.
  - lahairoi (Beer-lahai-roi): site of Hagar's theophany (Gen 16) → stub-needed.
  - lasea: Crete harbor in Paul's sea voyage (Acts 27) → stub-needed.
  - jareb (Hos 5:13): disputed textual term, probably not a proper noun → skip.
  - six redirect-only: jeconiah, jehoshua, joatham, josaphat, izehar, kirjathbaal.

Script: scripts/bpg-curate-04.py
Run: python3 scripts/bpg-curate-04.py  (from project root)
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
    # ── I names (continued) ──────────────────────────────────────────────────
    "ishpan":        {"status": "names-only"},   # Benjamin's son (1 Chr 8:22)
    "ispah":         {"status": "names-only"},   # Benjamin's son (1 Chr 8:16)
    "isui":          {"status": "names-only"},   # Asher's son (Gen 46:17)
    "ithai":         {"status": "names-only"},   # one of David's warriors (1 Chr 11:31)
    "ithiel":        {"status": "names-only"},   # two OT figures (Neh 11:7; Prov 30:1 addressee)
    "ithmah":        {"status": "names-only"},   # Moabite warrior of David (1 Chr 11:46)
    "ithran":        {"status": "names-only"},   # two OT figures (Gen 36:26; 1 Chr 7:37)
    "ithream":       {"status": "names-only"},   # David's sixth son (2 Sam 3:5)
    "ittahkazin":    {"status": "names-only"},   # Zebulun border landmark (Josh 19:13)
    # Variant of Izhar the Levite (Num 3:19)
    "izehar":        {"status": "redirect-only", "redirect_to": "izhar"},
    "izrahiah":      {"status": "names-only"},   # Issachar's son (1 Chr 7:3)
    "izri":          {"status": "names-only"},   # Levite musician, variant of Zeri (1 Chr 25:11)

    # ── J names ──────────────────────────────────────────────────────────────
    "jada":          {"status": "names-only"},   # son of Onam (1 Chr 2:28)
    "jadau":         {"status": "names-only"},   # son of Nebo (Ezra 10:43)
    "jahdiel":       {"status": "names-only"},   # Manasseh leader (1 Chr 5:24)
    "jahdo":         {"status": "names-only"},   # Gad's son (1 Chr 5:14)
    "jahleel":       {"status": "names-only"},   # Zebulun's son (Gen 46:14)
    "jahmai":        {"status": "names-only"},   # Issachar's son (1 Chr 7:2)
    "jakan":         {"status": "names-only"},   # variant of Jaakan (1 Chr 1:42)
    "jamin":         {"status": "names-only"},   # three OT figures (Gen 46:10; 1 Chr 2:27; Neh 8:7)
    "jamlech":       {"status": "names-only"},   # Simeon prince (1 Chr 4:34)
    "japhlet":       {"status": "names-only"},   # Asher's son (1 Chr 7:32)
    "jarah":         {"status": "names-only"},   # Saul's descendant (1 Chr 9:42)
    # "King Jareb" in Hos 5:13 — likely epithet for Assyria, not a proper noun; textual artifact
    "jareb":         {"status": "skip"},
    "jaresiah":      {"status": "names-only"},   # Benjamin's son (1 Chr 8:27)
    "jasiel":        {"status": "names-only"},   # one of David's warriors (1 Chr 11:47)
    "jathniel":      {"status": "names-only"},   # gatekeeper (1 Chr 26:2)
    "jazer":         {"status": "names-only"},   # Gad city east of Jordan (Num 21:32; Jer 48:32)
    "jaziz":         {"status": "names-only"},   # David's flock overseer (1 Chr 27:31)
    "jeberechiah":   {"status": "names-only"},   # father of Isaiah's witness Zechariah (Isa 8:2)
    "jecamiah":      {"status": "names-only"},   # Jeconiah's son (1 Chr 3:18)
    # KJV variant of Jehoiachin the exiled king (Jer 22:24,28)
    "jeconiah":      {"status": "redirect-only", "redirect_to": "jehoiachin"},
    "jedidah":       {"status": "names-only"},   # Josiah's mother (2 Kgs 22:1)
    "jeezer":        {"status": "names-only"},   # Gilead's son, also Abiezer (Num 26:30)
    "jehiah":        {"status": "names-only"},   # ark gatekeeper (1 Chr 15:24)
    # Alternate Hebrew form of Joshua (Num 13:16 margin)
    "jehoshua":      {"status": "redirect-only", "redirect_to": "joshua"},
    "jehubbah":      {"status": "names-only"},   # Asher's son (1 Chr 7:34)
    "jehud":         {"status": "names-only"},   # Dan town (Josh 19:45)
    "jehudijah":     {"status": "names-only"},   # Judah's wife (1 Chr 4:18; meaning "Jewess")
    "jehush":        {"status": "names-only"},   # Benjamin's son (1 Chr 8:39)
    "jekamiah":      {"status": "names-only"},   # two OT figures (1 Chr 2:41; 3:18)
    "jekuthiel":     {"status": "names-only"},   # Judah descendant (1 Chr 4:18)
    "jemuel":        {"status": "names-only"},   # Simeon's son (Gen 46:10)
    "jerah":         {"status": "names-only"},   # son of Joktan (Gen 10:26)
    "jered":         {"status": "names-only"},   # two OT figures (1 Chr 1:2 = Jared; 1 Chr 4:18)
    "jeremai":       {"status": "names-only"},   # post-exile man with foreign wife (Ezra 10:33)
    "jeremoth":      {"status": "names-only"},   # several minor OT figures
    "jeriah":        {"status": "names-only"},   # Levite (1 Chr 23:19)
    "jeriel":        {"status": "names-only"},   # Issachar's son (1 Chr 7:2)
    "jerijah":       {"status": "names-only"},   # variant of Jeriah (1 Chr 26:31)
    "jerioth":       {"status": "names-only"},   # Caleb's wife (1 Chr 2:18)
    "jeshishai":     {"status": "names-only"},   # Gad descendant (1 Chr 5:14)
    "jesiah":        {"status": "names-only"},   # two OT figures (1 Chr 12:6; 23:20)
    "jesimiel":      {"status": "names-only"},   # Simeon prince (1 Chr 4:36)
    "jesui":         {"status": "names-only"},   # Asher's son, variant of Isui (Num 26:44)
    "jezaniah":      {"status": "names-only"},   # military commander (Jer 40:8)
    "jezer":         {"status": "names-only"},   # Naphtali's son (Gen 46:24)
    "jeziah":        {"status": "names-only"},   # post-exile man (Ezra 10:25)
    "jezoar":        {"status": "names-only"},   # Judah descendant (1 Chr 4:7)
    "jezrahiah":     {"status": "names-only"},   # music leader (Neh 12:42)
    "jibsam":        {"status": "names-only"},   # Issachar's son (1 Chr 7:2)
    "jidlaph":       {"status": "names-only"},   # Nahor's son (Gen 22:22)
    "jiphtah":       {"status": "names-only"},   # Judah town (Josh 15:43)
    # Greek form of Jotham used in NT genealogy (Matt 1:9)
    "joatham":       {"status": "redirect-only", "redirect_to": "jotham"},
    "joed":          {"status": "names-only"},   # Benjamin's son (Neh 11:7)
    "jogbehah":      {"status": "names-only"},   # Gad city (Num 32:35; Judg 8:11)
    "jogli":         {"status": "names-only"},   # Dan's father (Num 34:22)
    "joha":          {"status": "names-only"},   # two OT figures (1 Chr 8:16; 11:45)
    "jonan":         {"status": "names-only"},   # NT genealogy (Luke 3:30)
    "jorah":         {"status": "names-only"},   # returned-exile family (Ezra 2:18)
    "jorim":         {"status": "names-only"},   # NT genealogy (Luke 3:29)
    "josabad":       {"status": "names-only"},   # returned-exile figure (Ezra 8:33 variant)
    # Greek form of Jehoshaphat used in NT genealogy (Matt 1:8)
    "josaphat":      {"status": "redirect-only", "redirect_to": "jehoshaphat"},
    "jose":          {"status": "names-only"},   # NT genealogy (Luke 3:29)
    # NT figure: Barnabas's birth name (Acts 4:36); also a brother of Jesus (Mark 6:3)
    "joses":         {"status": "stub-needed"},
    "joshah":        {"status": "names-only"},   # Simeon prince (1 Chr 4:34)
    "joshaviah":     {"status": "names-only"},   # David's warrior (1 Chr 11:46)
    "josibiah":      {"status": "names-only"},   # Simeon's father (1 Chr 4:35)
    "josiphiah":     {"status": "names-only"},   # returned-exile leader (Ezra 8:10)
    "jucal":         {"status": "names-only"},   # court official who imprisoned Jeremiah (Jer 38:1)
    "jushabhesed":   {"status": "names-only"},   # Zerubbabel's son (1 Chr 3:20)

    # ── K names ──────────────────────────────────────────────────────────────
    "kallai":        {"status": "names-only"},   # priest in Nehemiah's day (Neh 12:20)
    "kelaiah":       {"status": "names-only"},   # Levite with foreign wife (Ezra 10:23)
    "kenan":         {"status": "names-only"},   # antediluvian patriarch (Gen 5:9-14)
    "keros":         {"status": "names-only"},   # temple servant family (Ezra 2:44)
    # Alternate name for Kirjath-jearim where the ark rested (Josh 15:60; 18:14)
    "kirjathbaal":   {"status": "redirect-only", "redirect_to": "kirjath-jearim"},
    "kishi":         {"status": "names-only"},   # Merari Levite (1 Chr 6:44)
    "kushaiah":      {"status": "names-only"},   # Levite (1 Chr 15:17)

    # ── L names ──────────────────────────────────────────────────────────────
    "laadah":        {"status": "names-only"},   # Judah descendant (1 Chr 4:21)
    "laadan":        {"status": "names-only"},   # two Levites (1 Chr 7:26; 23:7)
    "lael":          {"status": "names-only"},   # Gershon's son (Num 3:24)
    "lahad":         {"status": "names-only"},   # Judah descendant (1 Chr 4:2)
    # Beer-lahai-roi: well where Hagar received the angel's promise (Gen 16:7-14)
    "lahairoi":      {"status": "stub-needed"},
    "lahmam":        {"status": "names-only"},   # Judah town (Josh 15:40)
    "lahmi":         {"status": "names-only"},   # brother of Goliath killed by Elhanan (1 Chr 20:5)
    # Harbor on Crete near Fair Havens; Paul's ship anchored here (Acts 27:8)
    "lasea":         {"status": "stub-needed"},
    "lebaoth":       {"status": "names-only"},   # Judah/Simeon town (Josh 15:32)
    "lehabim":       {"status": "names-only"},   # son of Egypt (Gen 10:13); Libyan people
    "leshem":        {"status": "names-only"},   # original name of Laish/Dan (Josh 19:47)
    "letushim":      {"status": "names-only"},   # Dedan's son (Gen 25:3)
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
    print(f'BPG Curation C04: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
