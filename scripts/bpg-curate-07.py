"""
BPG Curation — Batch C07: prudence → besor-the-brook
Gaps reviewed: 100 (gaps 601–700 by priority score)

Priority 30 range (gaps 601–609): Nave concepts with 100–169 verses.
Priority 25 range (gaps 610–700): smith-scholarly entries (often also in ISBE).

Notable decisions:
  - abomination-of-desolation: major eschatological term (Dan 9:27; Matt 24:15) → stub-needed.
  - akeldama: Field of Blood where Judas died (Acts 1:19) → stub-needed.
  - baruch-book-of: deuterocanonical book distinct from Baruch the man → stub-needed.
  - works (score-30): 127 nave verses < 150 threshold, generic noun → skip.
  - Nine redirects: Greek/variant spellings to their canonical Easton articles.

Script: scripts/bpg-curate-07.py
Run: python3 scripts/bpg-curate-07.py  (from project root)
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
    # ── Priority 30: Nave concepts (100+ verses, no dict article) ────────────
    "prudence":           {"status": "stub-needed"},   # 111 nave verses; practical wisdom theme
    "reproof":            {"status": "stub-needed"},   # 133 nave verses; biblical correction/rebuke
    "sanitation":         {"status": "stub-needed"},   # 125 nave verses; Levitical purity laws
    "seekers":            {"status": "stub-needed"},   # 116 nave verses; those who seek God
    "self-denial":        {"status": "stub-needed"},   # 102 nave verses; discipleship theme
    "speaking":           {"status": "stub-needed"},   # 169 nave verses; use of words/tongue
    "strife":             {"status": "stub-needed"},   # 105 nave verses; interpersonal conflict
    # 127 nave verses but generic English noun below 150-verse threshold
    "works":              {"status": "skip"},
    "worldliness":        {"status": "stub-needed"},   # 109 nave verses; warnings against the world

    # ── Priority 25: smith-scholarly entries (A–B names / concepts) ──────────
    "abila":              {"status": "names-only"},   # Abilene, Lysanias's tetrarchy (Luke 3:1)
    # Eschatological desecration of the temple (Dan 9:27; Matt 24:15; Mark 13:14)
    "abomination-of-desolation": {"status": "stub-needed"},
    # Variant of Ekron (Apocrypha); Easton has ekron.json
    "accaron":            {"status": "redirect-only", "redirect_to": "ekron"},
    # Variant of Achsah, Caleb's daughter (Judg 1:12); Easton has achsah.json
    "achsa":              {"status": "redirect-only", "redirect_to": "achsah"},
    "acrabbim":           {"status": "names-only"},   # "Scorpion Pass" border landmark (Num 34:4)
    "adalia":             {"status": "names-only"},   # Haman's son (Esth 9:8)
    "adasa":              {"status": "names-only"},   # village near Beth Horon (1 Macc 7:40)
    "addan":              {"status": "names-only"},   # unidentified place in Babylonia (Ezra 2:59)
    "ader":               {"status": "names-only"},   # son of Beriah (1 Chr 8:15)
    "adida":              {"status": "names-only"},   # Judah town fortified by Simon (1 Macc 12:38)
    "adoration":          {"status": "skip"},          # generic concept; Easton covers worship/prayer
    "ahasai":             {"status": "names-only"},   # post-exile priest (Neh 11:13)
    "ahban":              {"status": "names-only"},   # son of Abishur (1 Chr 2:29)
    "aher":               {"status": "names-only"},   # Benjamin descendant (1 Chr 7:12)
    "ahishahar":          {"status": "names-only"},   # Benjamin descendant (1 Chr 7:10)
    "ahuzzath":           {"status": "names-only"},   # Abimelech's friend at Gerar (Gen 26:26)
    # Variant of Ai (Neh 11:31); Easton has ai.json
    "aija":               {"status": "redirect-only", "redirect_to": "ai"},
    "akan":               {"status": "names-only"},   # Edomite chief = Jaakan (1 Chr 1:42)
    # Field of Blood where Judas died; site purchased with the 30 pieces of silver (Acts 1:18-19)
    "akeldama":           {"status": "stub-needed"},
    "alameth":            {"status": "names-only"},   # variant of Alemeth (1 Chr 7:8; 8:36)
    "alexandrians":       {"status": "names-only"},   # synagogue of the Alexandrians (Acts 6:9)
    "aliah":              {"status": "names-only"},   # Edomite chief = Alvah (1 Chr 1:51)
    "aloth":              {"status": "names-only"},   # district in northern Israel (1 Kgs 4:16)
    "alphabet":           {"status": "skip"},          # Smith scholarly note on Hebrew script; not a biblical topic
    "alvan":              {"status": "names-only"},   # Horite chief (Gen 36:23)
    "amam":               {"status": "names-only"},   # Judah town (Josh 15:26)
    "ambassage":          {"status": "skip"},          # archaic KJV word for "embassy" (Luke 14:32)
    "ammonitess":         {"status": "names-only"},   # descriptor for Ammonite women; not a standalone topic
    "ampliatus":          {"status": "names-only"},   # Roman Christian greeted by Paul (Rom 16:8)
    "amramites":          {"status": "names-only"},   # descendants of Amram (Num 3:27)
    "anaiah":             {"status": "names-only"},   # two post-exile figures (Neh 8:4; 10:22)
    "anethothite":        {"status": "names-only"},   # person from Anathoth; descriptor only
    # Anointing with oil; religious practice; Easton has anoint.json
    "anointing":          {"status": "redirect-only", "redirect_to": "anoint"},
    "aphekah":            {"status": "names-only"},   # Judah hill town (Josh 15:53)
    "aphrah":             {"status": "names-only"},   # Beth-ophrah in Micah's lament (Mic 1:10)
    "aphses":             {"status": "names-only"},   # priest division chief (1 Chr 24:15)
    "aramitess":          {"status": "names-only"},   # Aramean/Syrian woman descriptor
    "arbite":             {"status": "names-only"},   # person from Arab in Judah (2 Sam 23:35)
    "archery":            {"status": "skip"},          # military skill; no theological concept
    "architecture":       {"status": "skip"},          # Smith cultural note; no scripture narrative anchor
    "ardites":            {"status": "names-only"},   # Ard's clan in Benjamin (Num 26:40)
    "aridai":             {"status": "names-only"},   # Haman's son (Esth 9:9)
    "aridatha":           {"status": "names-only"},   # Haman's son (Esth 9:8)
    "arisai":             {"status": "names-only"},   # Haman's son (Esth 9:9)
    # The Ark of the Covenant; central OT sacred object; Easton has ark.json
    "ark-of-the-covenant": {"status": "redirect-only", "redirect_to": "ark"},
    "armlet":             {"status": "names-only"},   # arm ornament (2 Sam 1:10); single reference
    "arnan":              {"status": "names-only"},   # David's descendant (1 Chr 3:21)
    "arni":               {"status": "names-only"},   # NT genealogy = Ram (Luke 3:33)
    "arod":               {"status": "names-only"},   # son of Gad (Num 26:17)
    "arodi":              {"status": "names-only"},   # variant of Arod (Gen 46:16)
    "arodites":           {"status": "names-only"},   # Arod's descendants (Num 26:17)
    "aroerite":           {"status": "names-only"},   # person from Aroer (1 Chr 11:44)
    "arza":               {"status": "names-only"},   # steward of Elah (1 Kgs 16:9)
    "asahiah":            {"status": "names-only"},   # official sent by Josiah (2 Kgs 22:12)
    "asarelah":           {"status": "names-only"},   # Levite musician (1 Chr 25:2)
    # Greek/Apocrypha form of Ashkelon; Easton has ashkelon.json
    "ascalon":            {"status": "redirect-only", "redirect_to": "ashkelon"},
    # Greek NT form of Asher (Luke 2:36; Rev 7:6); Easton has asher.json
    "aser":               {"status": "redirect-only", "redirect_to": "asher"},
    "ashbea":             {"status": "names-only"},   # fine-linen guild at Beth Ashbea (1 Chr 4:21)
    "ashdodites":         {"status": "names-only"},   # inhabitants of Ashdod (Neh 4:7)
    "asherites":          {"status": "names-only"},   # Asher's tribal descendants
    "ashterathite":       {"status": "names-only"},   # person from Ashtaroth (1 Chr 11:44)
    "ashvath":            {"status": "names-only"},   # Asher descendant (1 Chr 7:33)
    "asnah":              {"status": "names-only"},   # post-exile temple servant (Ezra 2:50)
    "aspalathus":         {"status": "names-only"},   # fragrant plant in Sirach; apocryphal only
    "aspatha":            {"status": "names-only"},   # Haman's son (Esth 9:7)
    # Variant of Ashtaroth, Canaanite goddess; Easton has ashtaroth.json
    "astaroth":           {"status": "redirect-only", "redirect_to": "ashtaroth"},
    "athenians":          {"status": "names-only"},   # inhabitants of Athens (Acts 17:21)
    "azarael":            {"status": "names-only"},   # Levite musician (Neh 12:36)
    "azbuk":              {"status": "names-only"},   # father of Nehemiah's wall builder (Neh 3:16)
    "azem":               {"status": "names-only"},   # variant of Ezem, Simeon town (Josh 15:29)
    "aziel":              {"status": "names-only"},   # Levite musician (1 Chr 15:20)
    "aziza":              {"status": "names-only"},   # post-exile man with foreign wife (Ezra 10:27)
    # Variant spelling of Gaza; Easton has gaza.json
    "azzah":              {"status": "redirect-only", "redirect_to": "gaza"},
    "babylonians":        {"status": "names-only"},   # Chaldeans/Babylonians (Ezek 23:15)
    "bakbakkar":          {"status": "names-only"},   # Levite (1 Chr 9:15)
    "bakbuk":             {"status": "names-only"},   # post-exile temple servant (Ezra 2:51)
    "bakbukiah":          {"status": "names-only"},   # Levite gatekeeper (Neh 11:17)
    # Greek NT form of Balak (Rev 2:14); Easton has balak.json
    "balac":              {"status": "redirect-only", "redirect_to": "balak"},
    "band":               {"status": "skip"},          # generic word for military cohort; not a biblical concept
    # Deuterocanonical book associated with Baruch; distinct from Baruch the man
    "baruch-book-of":     {"status": "stub-needed"},
    "basmath":            {"status": "names-only"},   # Solomon's daughter (1 Kgs 4:15); Esau's wife (Gen 26:34)
    # Biblical bathing/purity practice; Easton has bath.json
    "bath-bathing":       {"status": "redirect-only", "redirect_to": "bath"},
    "bathshua":           {"status": "names-only"},   # wife of Judah (1 Chr 2:3); variant of Bathsheba
    "bavai":              {"status": "names-only"},   # wall builder (Neh 3:18)
    "bedeiah":            {"status": "names-only"},   # post-exile man (Ezra 10:35)
    "beerah":             {"status": "names-only"},   # Reuben leader taken captive (1 Chr 5:6)
    "beeshterah":         {"status": "names-only"},   # Levite city = Ashtaroth (Josh 21:27)
    "beninu":             {"status": "names-only"},   # covenant signer (Neh 10:13)
    # Bernice, sister of Herod Agrippa II; present at Paul's hearing (Acts 25:13,23; 26:30)
    "berenice":           {"status": "redirect-only", "redirect_to": "bernice"},
    "berothah":           {"status": "names-only"},   # northern Canaan town (Ezek 47:16)
    "besor-the-brook":    {"status": "names-only"},   # brook David crossed pursuing Amalekites (1 Sam 30:9)
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
    print(f'BPG Curation C07: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
