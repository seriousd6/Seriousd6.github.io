"""
BPG Curation — Batch C03: elpalet → ishod (gaps 201–300)
Gaps reviewed: 100 (all priority-35 smith-person/smith-place, E–I names)

Notable decisions:
  - herod: Smith-only gap; Easton apparently lacks standalone article.
    Herod dynasty is major NT content → stub-needed.
  - eubulus: Minor NT companion of Paul (2 Tim 4:21) → stub-needed.
  - huzzab (Nah 2:7): textual crux — probably not a proper noun → skip.

Script: scripts/bpg-curate-03.py
Run: python3 scripts/bpg-curate-03.py  (from project root)
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
    # ── E names (continued) ──────────────────────────────────────────────────
    "elpalet":       {"status": "names-only"},   # variant of Eliphelet, David's son (1 Chr 14:5)
    "eltolad":       {"status": "names-only"},   # Simeon/Judah town (Josh 15:30)
    "eluzai":        {"status": "names-only"},   # Benjamin warrior who joined David (1 Chr 12:5)
    "elzabad":       {"status": "names-only"},   # two OT figures (1 Chr 12:12; 26:7)
    "elzaphan":      {"status": "names-only"},   # Levite who carried Nadab and Abihu (Lev 10:4)
    "enam":          {"status": "names-only"},   # Judah town (Josh 15:34)
    "enan":          {"status": "names-only"},   # father of tribal leader Ahira (Num 1:15)
    "enhaddah":      {"status": "names-only"},   # Issachar town (Josh 19:21)
    "enhazor":       {"status": "names-only"},   # Naphtali town (Josh 19:37)
    "enmishpat":     {"status": "names-only"},   # ancient name for Kadesh (Gen 14:7)
    "enrimmon":      {"status": "names-only"},   # post-exile settlement (Neh 11:29)
    "entappuah":     {"status": "names-only"},   # Manasseh border town (Josh 17:7)
    "ephlal":        {"status": "names-only"},   # Jerahmeel descendant (1 Chr 2:37)
    "er":            {"status": "names-only"},   # Judah's firstborn (Gen 38:3); narrative belongs under Judah/Onan
    "eran":          {"status": "names-only"},   # Ephraim's grandson (Num 26:36)
    "eshban":        {"status": "names-only"},   # Horite son (Gen 36:26)
    "eshek":         {"status": "names-only"},   # Saul's descendant (1 Chr 8:39)
    "esli":          {"status": "names-only"},   # NT genealogy only (Luke 3:25)
    # Greek form of Hezron used in NT genealogies (Matt 1:3; Luke 3:33)
    "esrom":         {"status": "redirect-only", "redirect_to": "hezron"},
    "ether":         {"status": "names-only"},   # Judah/Simeon town (Josh 15:42; 19:7)
    "ethnan":        {"status": "names-only"},   # Judah descendant (1 Chr 4:7)
    "ethni":         {"status": "names-only"},   # Levite (1 Chr 6:41)
    # NT figure who greets Timothy alongside Paul; named in 2 Tim 4:21
    "eubulus":       {"status": "stub-needed"},
    "evi":           {"status": "names-only"},   # Midianite king killed by Israel (Num 31:8)
    "ezbon":         {"status": "names-only"},   # two OT figures (Gen 46:16; 1 Chr 7:7)
    "ezem":          {"status": "names-only"},   # Simeon town (1 Chr 4:29)

    # ── G names ──────────────────────────────────────────────────────────────
    "gabbai":        {"status": "names-only"},   # Benjaminite settler (Neh 11:8)
    "galal":         {"status": "names-only"},   # two Levites (1 Chr 9:15,16)
    "gatam":         {"status": "names-only"},   # Edomite chief (Gen 36:11)
    # Alternate spelling of Gezer; David's battle site (2 Sam 5:25)
    "gazer":         {"status": "redirect-only", "redirect_to": "gezer"},
    "gazez":         {"status": "names-only"},   # son/grandson of Caleb (1 Chr 2:46)
    "gazzam":        {"status": "names-only"},   # temple servant family (Ezra 2:48)
    "gederothaim":   {"status": "names-only"},   # Judah town (Josh 15:36)
    "gemalli":       {"status": "names-only"},   # father of spy Ammiel (Num 13:12)
    "gergesenes":    {"status": "names-only"},   # textual variant of Gadarenes; no distinct group
    "gether":        {"status": "names-only"},   # son of Aram (Gen 10:23)
    "geuel":         {"status": "names-only"},   # Gad's spy (Num 13:15)
    "giah":          {"status": "names-only"},   # landmark near Gibeon (2 Sam 2:24)
    "gibbar":        {"status": "names-only"},   # returned-exile family (Ezra 2:20)
    "giddel":        {"status": "names-only"},   # two temple servant families (Ezra 2:47,56)
    "gideoni":       {"status": "names-only"},   # father of Abidan (Num 1:11)
    "gilalai":       {"status": "names-only"},   # Levite musician (Neh 12:36)
    "ginath":        {"status": "names-only"},   # father of rival king Tibni (1 Kgs 16:21)
    "gittites":      {"status": "names-only"},   # demonym for Gath; no distinct theological topic
    "gudgodah":      {"status": "names-only"},   # wilderness camp (Num 33:32)

    # ── H names ──────────────────────────────────────────────────────────────
    "haahashtari":   {"status": "names-only"},   # Judah descendant (1 Chr 4:6)
    "hagab":         {"status": "names-only"},   # temple servant family (Ezra 2:46)
    "haggeri":       {"status": "names-only"},   # father of warrior Mibhar (1 Chr 11:38)
    "haggiah":       {"status": "names-only"},   # Merari Levite (1 Chr 6:30)
    "hakkatan":      {"status": "names-only"},   # Johanan's father (Ezra 8:12)
    "hakupha":       {"status": "names-only"},   # temple servant family (Ezra 2:51)
    "hali":          {"status": "names-only"},   # Asher border town (Josh 19:25)
    "haniel":        {"status": "names-only"},   # two OT figures (Num 34:23; 1 Chr 7:39)
    "hannathon":     {"status": "names-only"},   # Zebulun border town (Josh 19:14)
    "hareph":        {"status": "names-only"},   # son of Hur (1 Chr 2:51)
    "harumaph":      {"status": "names-only"},   # father of wall-builder Jedaiah (Neh 3:10)
    "hashabnah":     {"status": "names-only"},   # covenant signer (Neh 10:25)
    "hashem":        {"status": "names-only"},   # Gizonite warrior of David (1 Chr 11:34)
    "hazaiah":       {"status": "names-only"},   # post-exile Judah man (Neh 11:5)
    "hazelelponi":   {"status": "names-only"},   # daughter of Etam (1 Chr 4:3)
    "heresh":        {"status": "names-only"},   # Levite (1 Chr 9:15)
    # Major NT dynasty: Herod the Great (Matt 2), Antipas (Mark 6), Agrippa (Acts 12,25-26)
    "herod":         {"status": "stub-needed"},
    "hilen":         {"status": "names-only"},   # Levitical city in Judah (1 Chr 6:58)
    "hirah":         {"status": "names-only"},   # Judah's Adullamite friend (Gen 38:1)
    "hod":           {"status": "names-only"},   # Asher son (1 Chr 7:37)
    "hodaiah":       {"status": "names-only"},   # Judah descendant (1 Chr 3:24 variant)
    "hodaviah":      {"status": "names-only"},   # three minor OT figures
    "hodesh":        {"status": "names-only"},   # wife of Shaharaim (1 Chr 8:9)
    "holon":         {"status": "names-only"},   # Judah/Moab city (Josh 15:51; Jer 48:21)
    "homam":         {"status": "names-only"},   # Edomite chief, also Heman (1 Chr 1:39)
    "horam":         {"status": "names-only"},   # Canaanite king of Gezer (Josh 10:33)
    "hori":          {"status": "names-only"},   # two OT figures (Gen 36:22; Num 13:5)
    "hoshaiah":      {"status": "names-only"},   # two OT figures (Jer 42:1; Neh 12:32)
    "hoshama":       {"status": "names-only"},   # David's grandson (1 Chr 3:18)
    "hothir":        {"status": "names-only"},   # Heman's son, musician (1 Chr 25:4)
    "hupham":        {"status": "names-only"},   # son of Benjamin (Num 26:39)
    "huppim":        {"status": "names-only"},   # son of Benjamin (Gen 46:21)
    "huram":         {"status": "names-only"},   # variant of Hiram; multiple figures (1 Chr 8:5; 2 Chr 2:13)
    "huri":          {"status": "names-only"},   # Gad's son (1 Chr 5:14)
    "hushah":        {"status": "names-only"},   # Judah descendant (1 Chr 4:4)
    "hushathite":    {"status": "names-only"},   # epithet for David's warriors from Hushah
    # Nahor's son, probably same as Uz (Gen 22:21)
    "huz":           {"status": "redirect-only", "redirect_to": "uz"},
    # Disputed term in Nah 2:7; most scholars read as verb/phrase not proper noun → data artifact
    "huzzab":        {"status": "skip"},

    # ── I names ──────────────────────────────────────────────────────────────
    "ibneiah":       {"status": "names-only"},   # Benjaminite (1 Chr 9:8)
    "ibri":          {"status": "names-only"},   # Merari Levite (1 Chr 24:27)
    "idbash":        {"status": "names-only"},   # Judah descendant (1 Chr 4:3)
    "igdaliah":      {"status": "names-only"},   # father of Hanan (Jer 35:4)
    "igeal":         {"status": "names-only"},   # son of Nathan of Zobah (2 Sam 23:36)
    "ikkesh":        {"status": "names-only"},   # father of warrior Ira (2 Sam 23:26)
    "imnah":         {"status": "names-only"},   # two OT figures (Gen 46:17; 2 Chr 31:14)
    "imrah":         {"status": "names-only"},   # Asher descendant (1 Chr 7:36)
    "ir":            {"status": "names-only"},   # Benjamin's son (1 Chr 7:12)
    "iri":           {"status": "names-only"},   # Benjamin's son (1 Chr 7:7)
    "irijah":        {"status": "names-only"},   # captain who arrested Jeremiah (Jer 37:13)
    "irpeel":        {"status": "names-only"},   # Benjamin town (Josh 18:27)
    "irshemesh":     {"status": "names-only"},   # Dan boundary town (Josh 19:41)
    "ishiah":        {"status": "names-only"},   # multiple minor OT figures
    "ishma":         {"status": "names-only"},   # Judah descendant (1 Chr 4:3)
    "ishmerai":      {"status": "names-only"},   # Benjamin's son (1 Chr 8:18)
    "ishod":         {"status": "names-only"},   # Manasseh's son (1 Chr 7:18)
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
    print(f'BPG Curation C03: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
