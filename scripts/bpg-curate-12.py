"""
BPG Curation — Batch C12: uta → nephish
Gaps reviewed: 100 (gaps 1101–1200 by priority score)

Score-25 range (gaps 1101–1124): final smith-scholarly entries, U–Z.
Score-20 range (gaps 1125–1200): concept-no-article (50–86 Nave verses) + smith-person/place.

Notable stub-needed decisions:
  - accusation-false: 54 nave verses; legal/ethical theme (Prov 10:18; 1 Tim 5:19) → stub-needed.
  - anthropomorphisms: theological/hermeneutical term; God described with human attributes → stub-needed.
  - apostasy: 66 nave verses; major warning (Heb 6:4-6; 1 Tim 4:1; 2 Thess 2:3) → stub-needed.
  - benedictions: 84 nave verses; biblical blessing forms (Num 6:24-26; 2 Cor 13:14) → stub-needed.
  - beneficence: 58 nave verses; generosity theme (Gal 6:10; 2 Cor 9:6-7) → stub-needed.
  - conviction: 60 nave verses; Holy Spirit conviction (John 16:8; Acts 2:37) → stub-needed.
  - cowardice: 59 nave verses; 2 Tim 1:7; Rev 21:8; biblical examples → stub-needed.
  - disobedience-to-god: 58 nave verses; root of sin (1 Sam 15:23; Rom 5:19) → stub-needed.
  - doubting: 82 nave verses; faith/doubt tension (Jas 1:6-8; John 20:27) → stub-needed.
  - friendship: 64 nave verses; David/Jonathan; John 15:13-14 → stub-needed.
  - influence: 76 nave verses; moral influence in Scripture (Prov 4:18; 1 Cor 15:33) → stub-needed.
  - ingratitude: 86 nave verses; Luke 17:17-18; Rom 1:21; 2 Tim 3:2 → stub-needed.
  - instability: 50 nave verses; Jas 1:8 double-minded; Gen 49:4 → stub-needed.
  - weights-and-measures: biblical measurement system; key cultural background → stub-needed.
  16 redirects to Easton canonical articles.

Script: scripts/bpg-curate-12.py
Run: python3 scripts/bpg-curate-12.py  (from project root)
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
    # ── U–Z score-25 smith-scholarly (final batch of that range) ─────────────
    "uta":                {"status": "names-only"},   # post-exile figure (1 Esd 5:30)
    # Variant of Uzziah; Easton has uzziah.json
    "uzzia":              {"status": "redirect-only", "redirect_to": "uzziah"},
    # Easton has valley.json
    "vale-valley":        {"status": "redirect-only", "redirect_to": "valley"},
    "village":            {"status": "names-only"},   # generic settlement type; no doctrinal anchor
    # Easton has wave-offerings.json
    "wave-offering":      {"status": "redirect-only", "redirect_to": "wave-offerings"},
    "weapons":            {"status": "names-only"},   # military hardware; Easton covers specific weapons
    # Easton has weaving-weavers.json
    "weaving":            {"status": "redirect-only", "redirect_to": "weaving-weavers"},
    # Wedding ceremony; Easton has marriage.json and marriage-feasts.json
    "wedding":            {"status": "redirect-only", "redirect_to": "marriage"},
    # Biblical measurement system (Lev 19:36; Ezek 45:10); important cultural background
    "weights-and-measures": {"status": "stub-needed"},
    # Easton has widows.json (biblical care for widows, 1 Tim 5)
    "widow":              {"status": "redirect-only", "redirect_to": "widows"},
    "willows-the-brook-of-the": {"status": "names-only"},  # Isa 15:7 geographic boundary; single reference
    # Easton has winnow.json
    "winnowing":          {"status": "redirect-only", "redirect_to": "winnow"},
    # Easton has wrestle.json (Jacob's wrestling, Gen 32)
    "wrestling":          {"status": "redirect-only", "redirect_to": "wrestle"},
    "zacchur":            {"status": "names-only"},   # multiple OT figures (Num 13:4; Neh 3:2; 10:12)
    "zamzummim":          {"status": "names-only"},   # ancient giant race (Deut 2:20); single reference
    "zaphon":             {"status": "names-only"},   # Gad town (Josh 13:27)
    # Variant of Zarethan; Easton has zarthan.json
    "zartanah":           {"status": "redirect-only", "redirect_to": "zarthan"},
    "zavan":              {"status": "names-only"},   # Edomite chief (Gen 36:27); variant of Zaavan
    "zephon":             {"status": "names-only"},   # son of Gad (Num 26:15)
    "zeri":               {"status": "names-only"},   # Levite musician (1 Chr 25:3)
    "ziphion":            {"status": "names-only"},   # son of Gad (Gen 46:16); variant of Zephon
    "zobebah":            {"status": "names-only"},   # Judah descendant (1 Chr 4:8)
    # Variant of Zuph, Samuel's ancestor (1 Chr 6:26); Easton has zuph.json
    "zophai":             {"status": "redirect-only", "redirect_to": "zuph"},
    # Variant of Zorah, Samson's hometown (Josh 15:33); Easton has zorah.json
    "zoreah":             {"status": "redirect-only", "redirect_to": "zorah"},

    # ── Score-20 concept-no-article entries (50–86 Nave verses) ──────────────
    # False accusation; Prov 10:18; Isa 54:17; Luke 23:14; 1 Tim 5:19; key legal/ethical theme
    "accusation-false":   {"status": "stub-needed"},
    # Easton has affection.json
    "affections":         {"status": "redirect-only", "redirect_to": "affection"},
    # Easton has ammonite.json
    "ammonites":          {"status": "redirect-only", "redirect_to": "ammonite"},
    # God described with human attributes (anthropopathism); Gen 6:6; Exod 15:3; Ps 44:23; key hermeneutics
    "anthropomorphisms":  {"status": "stub-needed"},
    # Falling away from faith; Heb 6:4-6; 1 Tim 4:1; 2 Thess 2:3; Luke 8:13; major biblical warning
    "apostasy":           {"status": "stub-needed"},
    "art":                {"status": "names-only"},   # generic cultural term; no distinct biblical concept
    # Priestly/apostolic benedictions; Num 6:24-26; 2 Cor 13:14; Heb 13:20-21; Acts 3:26
    "benedictions":       {"status": "stub-needed"},
    # Generosity and charity; Prov 19:17; Gal 6:10; 2 Cor 9:6-7; Heb 13:16; key NT theme
    "beneficence":        {"status": "stub-needed"},
    "bigotry":            {"status": "names-only"},   # generic human failing; not a distinct biblical concept
    # Holy Spirit convicts of sin (John 16:8); Acts 2:37; core of gospel response
    "conviction":         {"status": "stub-needed"},
    # 2 Tim 1:7 "spirit of cowardice"; Peter's denial; Saul's disobedience; Rev 21:8 "cowardly"
    "cowardice":          {"status": "stub-needed"},
    # Easton has demon.json
    "demons":             {"status": "redirect-only", "redirect_to": "demon"},
    # Sin's essence: Isa 1:19-20; 1 Sam 15:23; Rom 5:19; Eph 2:2; pervasive biblical theme
    "disobedience-to-god": {"status": "stub-needed"},
    # Thomas (John 20:27); Peter on water (Matt 14:31); Jas 1:6-8; Jude 22; faith tension
    "doubting":           {"status": "stub-needed"},
    "egyptians":          {"status": "names-only"},   # demonym; Egypt and Egyptians covered under 'egypt'
    # Easton has fast.json (fasting practices)
    "fasting":            {"status": "redirect-only", "redirect_to": "fast"},
    # David/Jonathan (1 Sam 18:1); Prov 17:17; 18:24; John 15:13-14; Jas 2:23 Abraham as God's friend
    "friendship":         {"status": "stub-needed"},
    # Easton has gate.json
    "gates":              {"status": "redirect-only", "redirect_to": "gate"},
    # Jas 1:17; Matt 7:11; Ps 84:11; every good gift from God; Easton has gift.json
    "gifts-from-god":     {"status": "redirect-only", "redirect_to": "gift"},
    # Easton has glorify.json
    "glorifying-god":     {"status": "redirect-only", "redirect_to": "glorify"},
    # Moral influence for good or evil; Prov 4:18-19; 1 Cor 15:33; Dan 12:3; light imagery
    "influence":          {"status": "stub-needed"},
    # Luke 17:17-18 (ten lepers); Rom 1:21; 2 Tim 3:2; Prov 17:13; strong Nave topic
    "ingratitude":        {"status": "stub-needed"},
    # Jas 1:8 double-minded; Gen 49:4 Reuben unstable; 2 Pet 3:16; Elijah's challenge 1 Kgs 18:21
    "instability":        {"status": "stub-needed"},
    "nation":             {"status": "names-only"},   # generic political term; Easton covers specific nations

    # ── Score-20 smith-person/place entries ───────────────────────────────────
    # Mother of Hezekiah (2 Kgs 18:2); = Abijah (2 Chr 29:1); Easton has abijah.json
    "abi":                {"status": "redirect-only", "redirect_to": "abijah"},
    "aharhel":            {"status": "names-only"},   # Judah descendant (1 Chr 4:8)
    "ahuzam":             {"status": "names-only"},   # Judah descendant (1 Chr 4:6)
    "ain":                {"status": "names-only"},   # border landmark (Num 34:11); Levite city (Josh 21:16)
    "ashbel":             {"status": "names-only"},   # Benjamin's son; Ashbelites (Gen 46:21; Num 26:38)
    # Ancient Babylon/Tower of Babel; Easton has babel-tower-of.json
    "babel":              {"status": "redirect-only", "redirect_to": "babel-tower-of"},
    "belah":              {"status": "names-only"},   # son of Benjamin (Gen 46:21); also Edomite king (Gen 36:32)
    "bethbirei":          {"status": "names-only"},   # Simeon town (1 Chr 4:31)
    "bizjothjah":         {"status": "names-only"},   # Judah town (Josh 15:28)
    "chuza":              {"status": "names-only"},   # Herod's steward, husband of Joanna (Luke 8:3); single mention
    # Greek form of Colossae; Easton has colossae.json
    "colosse":            {"status": "redirect-only", "redirect_to": "colossae"},
    "dabbasheth":         {"status": "names-only"},   # Zebulun border town (Josh 19:11)
    "dimon":              {"status": "names-only"},   # Moabite town (Isa 15:9); variant of Dibon
    "dimonah":            {"status": "names-only"},   # Judah town (Josh 15:22)
    "dishon":             {"status": "names-only"},   # Horite chiefs (Gen 36:21,26)
    "dodavah":            {"status": "names-only"},   # father of Eliezer the prophet (2 Chr 20:37)
    "elmodam":            {"status": "names-only"},   # NT genealogy (Luke 3:28)
    "elonbethhanan":      {"status": "names-only"},   # Solomon's district (1 Kgs 4:9)
    # John baptized at Aenon/Enon near Salim (John 3:23); Easton has aenon.json
    "enon":               {"status": "redirect-only", "redirect_to": "aenon"},
    "epenetus":           {"status": "names-only"},   # first convert in Asia; greeted by Paul (Rom 16:5)
    "eri":                {"status": "names-only"},   # son of Gad (Gen 46:16)
    "gispa":              {"status": "names-only"},   # overseer of temple servants (Neh 11:21)
    "guni":               {"status": "names-only"},   # son of Naphtali (Gen 46:24); also a Gad descendant (1 Chr 5:15)
    "hachaliah":          {"status": "names-only"},   # father of Nehemiah (Neh 1:1)
    "hachmoni":           {"status": "names-only"},   # father of Jashobeam (1 Chr 11:11)
    "hanoch":             {"status": "names-only"},   # son of Midian (Gen 25:4); also Reuben's son (Gen 46:9)
    "harbonah":           {"status": "names-only"},   # Persian eunuch (Esth 1:10; 7:9)
    "harosheth":          {"status": "names-only"},   # Sisera's city of chariots (Judg 4:2,13,16)
    "hashupha":           {"status": "names-only"},   # temple servant family (Ezra 2:43; Neh 7:46)
    "hezrai":             {"status": "names-only"},   # David's warrior (2 Sam 23:35); also spelled Hezro
    "horhagidgad":        {"status": "names-only"},   # wilderness camp (Num 33:32; Deut 10:7)
    "hotham":             {"status": "names-only"},   # two OT figures (1 Chr 7:32; 11:44)
    # Greek form of Edom/Idumaea; Easton has idumaea.json
    "idumea":             {"status": "redirect-only", "redirect_to": "idumaea"},
    "janna":              {"status": "names-only"},   # NT genealogy (Luke 3:24)
    "jeaterai":           {"status": "names-only"},   # Levite (1 Chr 6:21)
    # Pre-Israelite Jerusalem; Easton has jebus.json
    "jebusi":             {"status": "redirect-only", "redirect_to": "jebus"},
    "jehezekel":          {"status": "names-only"},   # priestly division head (1 Chr 24:16)
    "jehoadah":           {"status": "names-only"},   # Saul's descendant (1 Chr 8:36)
    "jekabzeel":          {"status": "names-only"},   # post-exile Judah town (Neh 11:25)
    "jesaiah":            {"status": "names-only"},   # multiple OT figures (1 Chr 3:21; 25:3; 26:25)
    "jimnah":             {"status": "names-only"},   # son of Asher (Gen 46:17); variant of Imnah
    # Moabite city (Jer 48:24,41; Amos 2:2); Easton has kerioth.json
    "kirioth":            {"status": "redirect-only", "redirect_to": "kerioth"},
    # Variant of Kiriath-jearim; Easton has kirjath-jearim.json
    "kirjatharim":        {"status": "redirect-only", "redirect_to": "kirjath-jearim"},
    # OT Lod = NT Lydda (Acts 9:32,35,38); Easton has lydda.json
    "lod":                {"status": "redirect-only", "redirect_to": "lydda"},
    "maachathi":          {"status": "names-only"},   # Maachathite descriptor; person from Maacah
    "machbenah":          {"status": "names-only"},   # Judah place/person (1 Chr 2:49)
    "meres":              {"status": "names-only"},   # Persian prince (Esth 1:14)
    # Ammonite deity (1 Kgs 11:7; 2 Kgs 23:10; Lev 18:21; Acts 7:43); Easton has moloch.json
    "molech":             {"status": "redirect-only", "redirect_to": "moloch"},
    # Variant of Nahshon; Judah's tribal leader at Exodus (Num 1:7); Easton has nahshon.json
    "naashon":            {"status": "redirect-only", "redirect_to": "nahshon"},
    # Egyptian pharaoh who killed Josiah (2 Chr 35:20-24; 2 Kgs 23:29); Easton has necho-ii.json
    "necho":              {"status": "redirect-only", "redirect_to": "necho-ii"},
    "nephish":            {"status": "names-only"},   # son of Ishmael (Gen 25:15); variant of Naphish
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
    print(f'BPG Curation C12: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
