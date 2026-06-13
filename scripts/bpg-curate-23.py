"""
BPG Curation — Batch C23: abisei → aelia (gaps 2199–2298)
Gaps reviewed: 100 (all score-5 isbe-scholarly entries, A range)

Pure ISBE-scholarly batch. Entries are: variant spellings of canonical figures,
ISBE word studies (able, abolish, abound, abode, etc.), numbered ISBE sub-articles
(absalom-1/2, adar-1/2, acre-1/2), apocryphal figures (abubus, achior, achiacharus),
and minor place names. No theological concepts warrant stubs at score-5.

Strategy: names-only for all word studies, variants, apocryphal, and minor places.
Redirect ISBE numbered/variant articles to Easton where the canonical article exists
(absalom-1/2 → absalom, adam-* → adam, adrammelech-and-anammelech → adrammelech).

Script: scripts/bpg-curate-23.py
Run: python3 scripts/bpg-curate-23.py  (from project root)
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
    # ISBE variants of Abishai
    "abisei":              {"status": "names-only"},
    "abissei":             {"status": "names-only"},
    "abisue":              {"status": "names-only"},
    "abisum":              {"status": "names-only"},
    # ISBE word studies
    "abject":              {"status": "names-only"},
    "able":                {"status": "names-only"},
    "abode":               {"status": "names-only"},
    "abolish":             {"status": "names-only"},
    "abomination-birds-of": {"status": "names-only"},   # Lev 11 unclean birds
    "abound;-abundance;-abundant;-abundantly": {"status": "names-only"},
    "about":               {"status": "names-only"},
    "abraham-book-of":     {"status": "names-only"},   # Testament of Abraham; apocryphal
    "abrech":              {"status": "names-only"},   # Gen 41:43 "bow the knee"; KJV Egyptian term
    "abroad":              {"status": "names-only"},
    "abroad-scattered":    {"status": "names-only"},
    # ISBE numbered articles for Absalom; Easton has absalom.json
    "absalom-1":           {"status": "redirect-only", "redirect_to": "absalom"},
    "absalom-2":           {"status": "redirect-only", "redirect_to": "absalom"},
    # Latin variant of Absalom; Easton has absalom.json
    "absalon":             {"status": "redirect-only", "redirect_to": "absalom"},
    "absolution":          {"status": "names-only"},   # ISBE theological term
    "abstinence":          {"status": "names-only"},   # ISBE word study
    "abubus":              {"status": "names-only"},   # 1 Macc 16:11; apocryphal
    "abundance;-abundant": {"status": "names-only"},   # ISBE word study (variant entry)
    "abuse":               {"status": "names-only"},
    "abyss":               {"status": "names-only"},   # Luke 8:31; Rev 9:1; score-5 → names-only
    "abyssinia":           {"status": "names-only"},   # Ethiopia/Cush; general geographic
    "acatan":              {"status": "names-only"},
    "accaba":              {"status": "names-only"},
    "accad;-accadians":    {"status": "names-only"},   # Gen 10:10; Akkad; ancient city
    "accept;-acceptable;-acceptation": {"status": "names-only"},
    "acceptance":          {"status": "names-only"},
    "access":              {"status": "names-only"},
    "acco":                {"status": "names-only"},   # Judg 1:31; Ptolemais/Akko; no Easton article
    "accommodation":       {"status": "names-only"},
    "accomplish":          {"status": "names-only"},
    "accord;-according;-accordingly": {"status": "names-only"},
    "accos":               {"status": "names-only"},
    "account":             {"status": "names-only"},
    "accountability":      {"status": "names-only"},
    "accoz":               {"status": "names-only"},
    "accursed":            {"status": "names-only"},   # ISBE; anathema/cherem
    "achar":               {"status": "names-only"},   # ISBE variant of Achan
    "achiacharus":         {"status": "names-only"},   # Tobit; apocryphal
    "achias":              {"status": "names-only"},
    "achior":              {"status": "names-only"},   # Judith 5:5; apocryphal
    "achipha":             {"status": "names-only"},
    "achitob":             {"status": "names-only"},   # ISBE variant of Ahitub
    "acho":                {"status": "names-only"},   # ISBE variant of Acco
    "acipha":              {"status": "names-only"},
    "acitho;-acithoh":     {"status": "names-only"},
    "acknowledge":         {"status": "names-only"},
    "acquaint;-acquaintance": {"status": "names-only"},
    "acra":                {"status": "names-only"},   # Jerusalem Seleucid fortress; 1 Macc
    "acrabattene":         {"status": "names-only"},   # 1 Macc 5:3; region
    "acre-1":              {"status": "names-only"},   # ISBE numbered; land measure
    "acre-2":              {"status": "names-only"},   # ISBE numbered
    "acrostic":            {"status": "names-only"},   # ISBE literary term; Ps 119 etc.
    "acts-of-pilate":      {"status": "names-only"},   # apocryphal text
    "acts-of-solomon":     {"status": "names-only"},   # 1 Kgs 11:41; lost source
    "acts-apocryphal":     {"status": "names-only"},   # apocryphal Acts (Thomas, Peter, etc.)
    "acua":                {"status": "names-only"},
    "acub":                {"status": "names-only"},
    "acud":                {"status": "names-only"},
    "adadrimmon":          {"status": "names-only"},   # Zech 12:11; Megiddo plain mourning
    # ISBE numbered articles for Adam; Easton has adam.json
    "adam-in-the-new-testament": {"status": "redirect-only", "redirect_to": "adam"},
    "adam-in-the-old-testament": {"status": "redirect-only", "redirect_to": "adam"},
    "adam-in-the-old-testament-and-the-apocrypha": {"status": "redirect-only", "redirect_to": "adam"},
    "adam-books-of":       {"status": "names-only"},   # apocryphal pseudepigrapha
    "adam-city-of":        {"status": "names-only"},   # Josh 3:16; Jordan place
    "adami-nekeb":         {"status": "names-only"},   # Naphtali town (Josh 19:33)
    "adan":                {"status": "names-only"},   # ISBE variant of Addon/Addan (Ezra 2:59)
    "adar-1":              {"status": "names-only"},   # ISBE numbered; Hebrew month
    "adar-2":              {"status": "names-only"},   # ISBE numbered
    "adarsa":              {"status": "names-only"},   # 1 Macc 7:40; battle site
    "add":                 {"status": "names-only"},
    "addict":              {"status": "names-only"},   # KJV 1 Cor 16:15 "addicted"
    "addo":                {"status": "names-only"},   # ISBE variant of Iddo
    "addus":               {"status": "names-only"},
    "adiabene":            {"status": "names-only"},   # Mesopotamian region; Josephus
    "adinu;-adin":         {"status": "names-only"},   # ISBE variant; returned exile
    "adinus":              {"status": "names-only"},
    "admin":               {"status": "names-only"},   # ISBE variant of Amminadab (Luke 3:33)
    "administer;-administration": {"status": "names-only"},
    "admiration":          {"status": "names-only"},   # KJV Rev 17:6; word study
    "ado":                 {"status": "names-only"},
    "adonai":              {"status": "names-only"},   # divine name; score-5 → names-only; covered under god/lord
    "adonis":              {"status": "names-only"},   # pagan god; Tammuz (Ezek 8:14); general
    "ador;-adora":         {"status": "names-only"},   # ISBE place; Adoraim
    "adorn":               {"status": "names-only"},
    "adra":                {"status": "names-only"},   # ISBE place variant
    # Smith combined; Easton has adrammelech.json (Sepharvite god; 2 Kgs 17:31)
    "adrammelech-and-anammelech": {"status": "redirect-only", "redirect_to": "adrammelech"},
    "aduel":               {"status": "names-only"},   # Tobit; apocryphal
    "advantage":           {"status": "names-only"},
    "advent":              {"status": "names-only"},   # ISBE theological term; score-5 → names-only
    "adventure":           {"status": "names-only"},
    "adversity":           {"status": "names-only"},
    "advertise":           {"status": "names-only"},   # KJV Num 24:14; word study
    "advice;-advise;-advisement": {"status": "names-only"},
    "adytum":              {"status": "names-only"},   # ISBE; Holy of Holies technical term
    "aedias":              {"status": "names-only"},   # ISBE variant; Ezra 10:26
    "aelia":               {"status": "names-only"},   # Aelia Capitolina = Jerusalem under Hadrian
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
    print(f'BPG Curation C23: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
