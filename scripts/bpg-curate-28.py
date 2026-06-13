"""
BPG Curation — Batch C28: await → barnabas-gospel-of (gaps 2699–2798)
Gaps reviewed: 100 (score-5 isbe-scholarly A-B entries — lexical, apocryphal, Babylon compounds)

Score-5 ISBE continues near-total names-only. Notable stub:
Babylonian Captivity (586 BC exile; Ps 137; Daniel; Ezra-Nehemiah typology).
Notable redirects: babel-babylon-1/2, babylon-in-the-old/new-testament, babylonia → babylon.
1 stub-needed; 5 redirects; 94 names-only.

Script: scripts/bpg-curate-28.py
Run: python3 scripts/bpg-curate-28.py  (from project root)
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
    "await":                  {"status": "names-only"},   # lexical
    "awake":                  {"status": "names-only"},   # lexical; "Awake, O sword" (Zech 13:7); covered elsewhere
    "away-with":              {"status": "names-only"},   # KJV "take away/remove"; lexical
    "awe":                    {"status": "names-only"},   # lexical; "stand in awe of God" (Ps 4:4; 33:8)
    "ax-axe;-ax-head":        {"status": "names-only"},   # ISBE compound; iron axe-head miracle (2 Kgs 6:5); brief
    "axle-tree":              {"status": "names-only"},   # KJV "axle" (1 Kgs 7:32-33); architectural; lexical
    "ayin":                   {"status": "names-only"},   # Hebrew letter (16th); lexical
    "azael":                  {"status": "names-only"},   # apocryphal figure
    "azaelus":                {"status": "names-only"},   # apocryphal figure
    "azaphion":               {"status": "names-only"},   # apocryphal figure
    "azara":                  {"status": "names-only"},   # apocryphal figure
    "azaraias":               {"status": "names-only"},   # apocryphal figure (1 Esd 9:21)
    "azarel":                 {"status": "names-only"},   # ISBE disambiguation; minor OT figures
    "azarias":                {"status": "names-only"},   # apocryphal variant (1 Esd; Tobit); names-only
    "azaru":                  {"status": "names-only"},   # apocryphal figure
    "azbasareth":             {"status": "names-only"},   # apocryphal figure
    "azephurith":             {"status": "names-only"},   # apocryphal figure
    "azetas":                 {"status": "names-only"},   # apocryphal figure
    "aziei":                  {"status": "names-only"},   # apocryphal figure
    "azmaveth-1":             {"status": "names-only"},   # one of David's mighty men (2 Sam 23:31); disambiguation
    "azmaveth-2":             {"status": "names-only"},   # place in Benjamin (Neh 12:29); disambiguation
    "azuran":                 {"status": "names-only"},   # apocryphal figure
    "baal-1":                 {"status": "names-only"},   # ISBE disambiguation; Baal the deity covered in Easton/Smith
    "baal-2":                 {"status": "names-only"},   # son of Jehiel (1 Chr 8:30); disambiguation
    "baal-3":                 {"status": "names-only"},   # place in Simeon (1 Chr 4:33); disambiguation
    "baal-shalishah":         {"status": "names-only"},   # 2 Kgs 4:42 (Elisha's bread miracle); minor place
    "baalbek":                {"status": "names-only"},   # ancient Heliopolis in Lebanon; extrabiblical
    "baale-judah":            {"status": "names-only"},   # another name for Kiriath-jearim (2 Sam 6:2)
    "baalsamus":              {"status": "names-only"},   # apocryphal figure (1 Esd 9:43)
    "baani":                  {"status": "names-only"},   # apocryphal figure (1 Esd 9:34)
    "baanias":                {"status": "names-only"},   # apocryphal figure (1 Esd 9:26)
    "babbler":                {"status": "names-only"},   # Acts 17:18; Athenians mocking Paul; lexical
    "babbling":               {"status": "names-only"},   # 1 Tim 6:20 "empty chatter"; lexical
    # ISBE Babel/Babylon disambiguation; redirect to canonical article
    "babel-babylon-1":        {"status": "redirect-only", "redirect_to": "babylon"},
    "babel-babylon-2":        {"status": "redirect-only", "redirect_to": "babylon"},
    "babi":                   {"status": "names-only"},   # apocryphal figure
    # ISBE compound; Babylon's symbolic use in NT (Rev 14:8; 17-18; 1 Pet 5:13); redirect to Babylon
    "babylon-in-the-new-testament": {"status": "redirect-only", "redirect_to": "babylon"},
    # ISBE compound; redirect to canonical Babylon article covering OT usage
    "babylon-in-the-old-testament": {"status": "redirect-only", "redirect_to": "babylon"},
    # ISBE compound for the Babylonian region; redirect to main Babylon article
    "babylonia":              {"status": "redirect-only", "redirect_to": "babylon"},
    "babylonia-and-assyria-religion-of": {"status": "names-only"},  # ISBE scholarly; too specialized at score-5
    # The Babylonian Captivity (605–536 BC): deportations under Nebuchadnezzar (2 Kgs 24-25);
    # "By the rivers of Babylon we sat and wept" (Ps 137:1); prophetic context of Jeremiah, Ezekiel,
    # Daniel; Cyrus decree (Ezra 1:1-4); return under Zerubbabel/Ezra/Nehemiah; typological of
    # spiritual exile and restoration; pivot point in biblical history
    "babylonian-captivity":   {"status": "stub-needed"},
    "babylonish-mantle":      {"status": "names-only"},   # Achan's sin (Josh 7:21); brief item
    "bacchides":              {"status": "names-only"},   # Seleucid general (1 Macc 7:8); apocryphal
    "bacchurus":              {"status": "names-only"},   # apocryphal figure
    "bacchus":                {"status": "names-only"},   # Dionysus; Greek god; extrabiblical
    "bacenor":                {"status": "names-only"},   # apocryphal figure (2 Macc 12:35)
    "bachrite":               {"status": "names-only"},   # demonym for Becher; Numbers genealogy
    "back-back-parts":        {"status": "names-only"},   # KJV compound; lexical
    "backside":               {"status": "names-only"},   # KJV "far side/back of" (Exod 3:1); lexical
    "baean":                  {"status": "names-only"},   # place (1 Macc 5:4); apocryphal
    "baggage":                {"status": "names-only"},   # 1 Sam 17:22 (David at battle); lexical
    "bago":                   {"status": "names-only"},   # apocryphal figure
    "bagoas":                 {"status": "names-only"},   # Holofernes' servant (Judith 12:11); apocryphal
    "bagoi":                  {"status": "names-only"},   # apocryphal figure (1 Esd 5:14)
    "baharumite;-barhumite":  {"status": "names-only"},   # ISBE compound; variant demonym
    "baiterus":               {"status": "names-only"},   # apocryphal figure (1 Esd 5:17)
    "baking":                 {"status": "names-only"},   # cultural practice; general
    "baking-pan":             {"status": "names-only"},   # Lev 2:5 grain offering utensil; brief
    "balamon":                {"status": "names-only"},   # place (Judith 8:3); apocryphal
    "balancings":             {"status": "names-only"},   # Job 37:16 KJV "balancings of clouds"; lexical
    "balasamus":              {"status": "names-only"},   # apocryphal figure (1 Esd 9:43)
    "bald-locust":            {"status": "names-only"},   # Lev 11:22 clean insect; covered under locusts
    "ball":                   {"status": "names-only"},   # Isa 22:18; lexical
    "balm-of-gilead":         {"status": "names-only"},   # Jer 8:22; Gen 37:25; covered under Balm in Easton
    "balnuus":                {"status": "names-only"},   # apocryphal figure
    "balsam":                 {"status": "names-only"},   # aromatic resin; botanical; general
    "baltasar":               {"status": "names-only"},   # Greek form of Belshazzar; covered under Belshazzar
    "bamoth;-bamoth-baal":    {"status": "names-only"},   # ISBE compound; Moabite high places (Num 21:19; 22:41)
    "ban":                    {"status": "names-only"},   # herem/devoted thing (Josh 6:17-18); covered under Cherem
    "banaias":                {"status": "names-only"},   # apocryphal figure (1 Esd 9:35)
    "bands-of-rudder":        {"status": "names-only"},   # Acts 27:40 nautical term; lexical
    "bands-beauty-and":       {"status": "names-only"},   # Zech 11:7 Zechariah's symbolic staffs; lexical
    "banias-1":               {"status": "names-only"},   # Caesarea Philippi (ancient Paneas); geographic
    "banias-2":               {"status": "names-only"},   # another location variant; geographic
    "banid":                  {"status": "names-only"},   # apocryphal figure
    "banishment":             {"status": "names-only"},   # general concept; covered under exile/cities of refuge
    "bank":                   {"status": "names-only"},   # lexical; Prov 26:17 KJV; riverbank
    "bank;-banking":          {"status": "names-only"},   # ISBE compound; too specialized at score-5
    "bannaia":                {"status": "names-only"},   # apocryphal figure
    "bannas":                 {"status": "names-only"},   # apocryphal figure (1 Esd 9:26)
    "banneas":                {"status": "names-only"},   # apocryphal figure
    "bannus":                 {"status": "names-only"},   # Josephus' teacher; extrabiblical
    "banuas":                 {"status": "names-only"},   # apocryphal figure (1 Esd 9:26)
    "baptism-lutheran-doctrine": {"status": "names-only"},  # ISBE denominational article; too specialized
    "baptism-non-immersionist-view": {"status": "names-only"},  # ISBE denominational; too specialized
    "baptism-the-baptist-interpretation": {"status": "names-only"},  # ISBE denominational; too specialized
    "baptism-of-fire":        {"status": "names-only"},   # Matt 3:11; Luke 3:16; covered under baptism/Holy Spirit
    "baptism-of-the-holy-spirit": {"status": "names-only"},  # Acts 1:5; 2:4; covered under Holy Spirit/baptism
    "baptism-infant":         {"status": "names-only"},   # ISBE denominational; too specialized at score-5
    "baptismal-regeneration": {"status": "names-only"},   # ISBE denominational; covered under baptism
    "baptist":                {"status": "names-only"},   # John the Baptist's title; covered under John the Baptist
    "bar-1":                  {"status": "names-only"},   # ISBE disambiguation; Aramaic prefix "son of"; lexical
    "bar-2":                  {"status": "names-only"},   # ISBE disambiguation; metal/wooden bar; lexical
    "bar-jonah":              {"status": "names-only"},   # Peter's surname (Matt 16:17); covered under Simon Peter
    "barachiah":              {"status": "names-only"},   # variant of Berechiah (Zech 1:1); names-only
    "barbarian;-barbarous":   {"status": "names-only"},   # Col 3:11; Rom 1:14; "neither Greek nor barbarian"; lexical
    "barchus":                {"status": "names-only"},   # apocryphal figure
    "barhumite":              {"status": "names-only"},   # variant of Baharumite; demonym
    "barnabas-epistle-of":    {"status": "names-only"},   # extracanonical; too specialized at score-5
    "barnabas-gospel-of":     {"status": "names-only"},   # extracanonical; too specialized at score-5
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
    print(f'BPG Curation C28: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
