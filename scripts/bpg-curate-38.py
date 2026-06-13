"""
BPG Curation — Batch C38: demand → door (gaps 3699–3798)
Gaps reviewed: 100 (score-5 isbe-scholarly D entries — lexical, apocryphal, minor compound forms)

Entirely names-only batch. Demon/demonology covered under devil/Satan in Easton.
Diaspora/dispersion covered under dispersion article. Divorce compounds covered under divorce.
0 stub-needed; 0 redirects; 100 names-only.

Script: scripts/bpg-curate-38.py
Run: python3 scripts/bpg-curate-38.py  (from project root)
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
    "demand":                 {"status": "names-only"},   # lexical
    "demetrius-1":            {"status": "names-only"},   # ISBE disambiguation; Acts 19:24-41 silversmith
    "demetrius-2":            {"status": "names-only"},   # ISBE disambiguation; 3 John 12; commended
    "demon;-demoniac;-demonology": {"status": "names-only"},  # covered under devil/Satan in Easton/Smith
    "demophon":               {"status": "names-only"},   # apocryphal figure (2 Macc 12:2)
    "denounce":               {"status": "names-only"},   # KJV "declare/warn" (Deut 30:18); lexical
    "deny":                   {"status": "names-only"},   # Matt 16:24; Peter's denial; lexical
    "deposit":                {"status": "names-only"},   # lexical
    "depth":                  {"status": "names-only"},   # Ps 130:1; lexical/poetic
    "derision":               {"status": "names-only"},   # Ps 2:4; lexical/poetic
    "descend;-descent":       {"status": "names-only"},   # ISBE compound; lexical
    "descent-of-jesus":       {"status": "names-only"},   # 1 Pet 3:19; Eph 4:9; covered under resurrection/Hades
    "describe":               {"status": "names-only"},   # lexical
    "descry":                 {"status": "names-only"},   # KJV "spy out" (Josh 18:8); lexical
    "desire":                 {"status": "names-only"},   # lexical
    "desolate":               {"status": "names-only"},   # lexical; desolating abomination covered elsewhere
    "despair":                {"status": "names-only"},   # 2 Cor 4:8; lexical
    "despite;-despiteful":    {"status": "names-only"},   # ISBE compound; KJV; lexical
    "dessau":                 {"status": "names-only"},   # apocryphal place (2 Macc 14:16)
    "destiny-meni":           {"status": "names-only"},   # Isa 65:11 KJV "Meni" destiny goddess; brief
    "destruction-city-of-heliopolis-or-city-of-the-sun": {"status": "names-only"},  # Isa 19:18; geographic
    "determinate":            {"status": "names-only"},   # Acts 2:23 KJV "determinate counsel"; lexical
    "determine":              {"status": "names-only"},   # lexical
    "detestable-things":      {"status": "names-only"},   # ISBE compound; Ezekiel's idols; covered elsewhere
    "deutero-canonical-books": {"status": "names-only"},  # Apocrypha; too specialized at score-5
    "device":                 {"status": "names-only"},   # lexical
    "devoted-things":         {"status": "names-only"},   # herem (Josh 6:17-18); covered under cherem
    "devotion;-devotions":    {"status": "names-only"},   # ISBE compound; Acts 17:23; lexical
    "devout":                 {"status": "names-only"},   # Acts 2:5; 10:2; lexical
    "dial-of-ahaz":           {"status": "names-only"},   # 2 Kgs 20:11; Isa 38:8; covered under Hezekiah
    "diana;-artemis":         {"status": "names-only"},   # ISBE compound; Acts 19:28-41; contextual; names-only
    "diaspora":               {"status": "names-only"},   # Jewish Diaspora; covered under dispersion in Easton
    "diblah":                 {"status": "names-only"},   # Ezek 6:14 variant of Riblah; minor place
    "dibon;-dibon-gad":       {"status": "names-only"},   # ISBE compound; Moabite town (Num 21:30); names-only
    "dice-playing":           {"status": "names-only"},   # cultural practice; brief
    "dictionaries":           {"status": "names-only"},   # ISBE scholarly; too specialized
    "didache":                {"status": "names-only"},   # early Christian document; extracanonical; too specialized
    "didrachma":              {"status": "names-only"},   # Matt 17:24 half-shekel; covered under money
    "die":                    {"status": "names-only"},   # lexical
    "diet":                   {"status": "names-only"},   # lexical
    "dig":                    {"status": "names-only"},   # lexical
    "dignities;-dignity":     {"status": "names-only"},   # ISBE compound; 2 Pet 2:10; Jude 8; lexical
    "dike":                   {"status": "names-only"},   # lexical; not a significant biblical term
    "diligence;-diligent;-diligently": {"status": "names-only"},  # ISBE compound; Prov 4:23; 2 Pet 1:5; lexical
    "dill":                   {"status": "names-only"},   # Matt 23:23; botanical; covered under anise/dill
    "diminish":               {"status": "names-only"},   # lexical
    "dimon;-dimonah":         {"status": "names-only"},   # ISBE compound; Isa 15:9; Moabite place
    "dinner":                 {"status": "names-only"},   # Matt 22:4 parable; lexical
    "dionysia":               {"status": "names-only"},   # Greek festival; extrabiblical
    "dionysus-bacchus":       {"status": "names-only"},   # ISBE compound; Greek god; extrabiblical
    "dioscorinthius":         {"status": "names-only"},   # 2 Macc 11:21 calendar ref; apocryphal
    "dioscuri":               {"status": "names-only"},   # Acts 28:11 "Twin Brothers" ship sign; brief
    "dip":                    {"status": "names-only"},   # lexical
    "diphath":                {"status": "names-only"},   # 1 Chr 1:6 variant of Riphath; minor variant
    "disallow":               {"status": "names-only"},   # KJV "reject" (1 Pet 2:4); lexical
    "disannul":               {"status": "names-only"},   # KJV "make void" (Isa 14:27; Gal 3:17); lexical
    "disappoint":             {"status": "names-only"},   # KJV "frustrate" (Job 5:12); lexical
    "discern":                {"status": "names-only"},   # 1 Kgs 3:9; lexical; covered under wisdom
    "discernings-of-spirits": {"status": "names-only"},   # 1 Cor 12:10 spiritual gift; covered under that topic
    "discipline":             {"status": "names-only"},   # Heb 12:5-11; covered under chastening in Easton
    "discomfit;-discomfiture": {"status": "names-only"},  # ISBE compound; KJV military "rout"; lexical
    "discourse":              {"status": "names-only"},   # lexical
    "discover":               {"status": "names-only"},   # KJV "uncover/expose"; lexical
    "discrepancies-biblical": {"status": "names-only"},   # ISBE scholarly; apologetics; too specialized
    "discus":                 {"status": "names-only"},   # 2 Macc 4:14; Greek games; apocryphal
    "disease;-diseases":      {"status": "names-only"},   # ISBE compound; covered under healing/medicine in Easton
    "diseases-of-the-eye":    {"status": "names-only"},   # ISBE compound; blindness miracles; brief
    "dishan;-dishon":         {"status": "names-only"},   # ISBE compound; Horite clan (Gen 36:21-30)
    "dishonesty":             {"status": "names-only"},   # 2 Cor 4:2; lexical
    "disobedience;-disobedient": {"status": "names-only"},  # ISBE compound; Rom 5:19; Eph 2:2; lexical
    "disorderly":             {"status": "names-only"},   # 2 Thess 3:6-11; lexical
    "dispatch":               {"status": "names-only"},   # Ezek 23:47 KJV; lexical
    "dispersion-of-nations":  {"status": "names-only"},   # ISBE compound; Gen 11; covered under Babel
    "dispersion-the":         {"status": "names-only"},   # ISBE compound; 1 Pet 1:1; Jas 1:1; covered elsewhere
    "disposition":            {"status": "names-only"},   # Acts 7:53; lexical
    "disputation":            {"status": "names-only"},   # Acts 15:2; Jude 9; lexical
    "distil":                 {"status": "names-only"},   # KJV "drip/drop" (Deut 32:2; Job 36:28); lexical
    "distinctly":             {"status": "names-only"},   # Neh 8:8; lexical
    "ditch":                  {"status": "names-only"},   # Matt 15:14; Ps 7:15; lexical
    "divers;-diverse;-diversities": {"status": "names-only"},  # ISBE compound; KJV "various"; lexical
    "dives":                  {"status": "names-only"},   # Latin name; Luke 16:19-31; covered under Lazarus
    "divide":                 {"status": "names-only"},   # lexical
    "divine-names":           {"status": "names-only"},   # divine titles; covered under individual name articles
    "divine-visitation":      {"status": "names-only"},   # ISBE compound; lexical/theological; brief
    "divine;-diviner":        {"status": "names-only"},   # ISBE compound; covered under divination in Easton
    "division":               {"status": "names-only"},   # lexical
    "divorce-in-the-new-testament": {"status": "names-only"},  # Matt 5:31-32; 19:3-12; covered under divorce
    "divorce-in-the-old-testament": {"status": "names-only"},  # Deut 24:1-4; Mal 2:16; covered under divorce
    "doctrine":               {"status": "names-only"},   # 2 Tim 3:16; Titus 1:9; lexical
    "docus":                  {"status": "names-only"},   # apocryphal place (1 Macc 16:15)
    "dodavahu":               {"status": "names-only"},   # 2 Chr 20:37; minor OT figure
    "dodo;-dodai":            {"status": "names-only"},   # ISBE compound; 2 Sam 23:9; minor figures
    "doe":                    {"status": "names-only"},   # Song 2:9; Prov 5:19; animal reference; brief
    "dogma":                  {"status": "names-only"},   # scholarly term; lexical
    "dok":                    {"status": "names-only"},   # apocryphal place (1 Macc 16:15)
    "doleful":                {"status": "names-only"},   # Isa 13:21; Mic 2:4 KJV; lexical
    "dolphin":                {"status": "names-only"},   # Num 4:6 ISBE interpretation; brief
    "dominion":               {"status": "names-only"},   # Col 1:16; Dan 7:14; lexical; covered under creation/angels
    "doom":                   {"status": "names-only"},   # lexical
    "door":                   {"status": "names-only"},   # John 10:7,9 "I am the door"; lexical; covered elsewhere
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
    print(f'BPG Curation C38: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
