"""
BPG Curation — Batch C60: pence;-penny → plagues-of-egypt (gaps ~6009–6113)
Gaps reviewed: 105 (score-5 isbe-scholarly P entries)

Score-5 ISBE posture: ~90% names-only. Notable stubs: perseverance (perseverance of saints),
person-of-christ (hypostatic union/Chalcedonian definition), philo-judaeus (Logos concept,
NT background), pentateuch-the-samaritan (OT textual criticism), plagues-of-egypt (Exodus).
5 stub-needed; 7 redirects; 93 names-only.

Script: scripts/bpg-curate-60.py
Run: python3 scripts/bpg-curate-60.py  (from project root)
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
    "pence;-penny":             {"status": "names-only"},   # KJV currency; covered under "money" and "denarius"
    "pencil":                   {"status": "names-only"},   # Isa 44:13 KJV writing implement; lexical
    "pendant":                  {"status": "names-only"},   # jewelry (Isa 3:19); cultural; brief
    "penknife":                 {"status": "names-only"},   # Jer 36:23 KJV scribe's knife; lexical
    "pension":                  {"status": "names-only"},   # lexical; not a significant biblical concept
    # Pentateuch text preserved by Samaritans; diverges from MT at ~6,000 points;
    # closer to LXX in places; valuable for OT textual criticism; Gerizim vs Jerusalem as
    # worship site; important for understanding Samaritan woman dialogue (John 4:20)
    "pentateuch-the-samaritan": {"status": "stub-needed"},
    "penury":                   {"status": "names-only"},   # KJV "poverty" (Prov 14:23; Luke 21:4); archaic
    "people":                   {"status": "names-only"},   # lexical; general
    "peraea":                   {"status": "names-only"},   # region east of Jordan; covered under "perea"
    "perdition":                {"status": "names-only"},   # John 17:12; Phil 1:28; covered under "hell"
    # ISBE compound; redirect to canonical Pharez/Perez article
    "perez;-pharez":            {"status": "redirect-only", "redirect_to": "pharez"},
    "perfect;-perfection":      {"status": "names-only"},   # Matt 5:48; covered under "perfection" in Easton
    "perform":                  {"status": "names-only"},   # lexical
    "perfume-making":           {"status": "names-only"},   # cultural; covered under "perfume" and "ointment"
    "perfume;-perfumer":        {"status": "names-only"},   # ISBE compound; cultural; covered under "perfume"
    # ISBE compound; redirect to canonical Pergamos article (Rev 2 church)
    "pergamos;-pergamum":       {"status": "redirect-only", "redirect_to": "pergamos"},
    "perizzite":                {"status": "names-only"},   # pre-Israelite people; covered under "perizzites"
    "perjury":                  {"status": "names-only"},   # false swearing; covered under "oath" and "swearing"
    "perpetual;-perpetually;-perpetuity": {"status": "names-only"},  # KJV "eternal/forever"; lexical
    "perseus":                  {"status": "names-only"},   # Macedonian king (1 Macc 8:5); apocryphal
    # "The one who endures to the end will be saved" (Matt 24:13); "He who began a good work…
    # will complete it" (Phil 1:6); Calvinist doctrine of perseverance of the saints (TULIP);
    # Arminian view: genuine believers can fall away (Heb 6:4-6); contested but central
    "perseverance":             {"status": "stub-needed"},
    "persian-language-and-literature-ancient": {"status": "names-only"},  # too specialized for biblepedia
    "persian-religion-ancient": {"status": "names-only"},   # Zoroastrianism; too specialized
    "persians":                 {"status": "names-only"},   # covered under "persia" in Easton
    # Hypostatic union: Christ as fully God and fully man in one person; Council of Chalcedon (451 AD)
    # "two natures, without confusion, without change, without division, without separation";
    # refutes Docetism (only God), Ebionism (only man), Nestorianism (two persons), Eutychianism
    # (mixed nature); essential for understanding incarnation, atonement, and mediation
    "person-of-christ":         {"status": "stub-needed"},
    "person-personality":       {"status": "names-only"},   # philosophical concept; lexical
    "personality":              {"status": "names-only"},   # lexical; general
    "persuade;-persuasion":     {"status": "names-only"},   # lexical
    "perverse":                 {"status": "names-only"},   # lexical; covered under "sin"
    "pestle":                   {"status": "names-only"},   # Prov 27:22; grinding implement; cultural
    "peter-apocalypse-of":      {"status": "names-only"},   # pseudepigraphical; not canonical
    "peter-epistles-of":        {"status": "names-only"},   # ISBE entry; covered under individual epistles
    "peter-gospel-according-to": {"status": "names-only"},  # gnostic gospel; apocryphal
    "peter-simon":              {"status": "names-only"},   # ISBE disambiguation; covered under "peter" in Easton
    "peter-the-first-epistle-of": {"status": "names-only"},  # covered under "peter" in Easton
    "peter-the-second-epistle-of": {"status": "names-only"}, # covered under "peter" in Easton
    "petition":                 {"status": "names-only"},   # lexical; covered under "prayer"
    "peulthai;-peullethai":     {"status": "names-only"},   # Levite (1 Chr 26:5); minor
    "phaath-moab":              {"status": "names-only"},   # post-exilic family (Ezra 2:6); minor
    "phacareth":                {"status": "names-only"},   # apocryphal
    "phaisur":                  {"status": "names-only"},   # apocryphal variant of Pashhur
    "phaldeus":                 {"status": "names-only"},   # apocryphal (1 Esd 9:22)
    "phaleas":                  {"status": "names-only"},   # apocryphal (1 Esd 5:22)
    "phalias":                  {"status": "names-only"},   # apocryphal (1 Esd 9:22)
    "pharakim":                 {"status": "names-only"},   # apocryphal (1 Esd 5:31)
    "pharaoh-hophra":           {"status": "names-only"},   # Egyptian pharaoh (Jer 44:30); covered under "hophra"
    "pharaoh-necoh":            {"status": "names-only"},   # Egyptian pharaoh (2 Kgs 23:29); covered under "pharaoh"
    "pharathon":                {"status": "names-only"},   # apocryphal (1 Macc 9:50)
    # ISBE variant; redirect to canonical Pharez article
    "phares":                   {"status": "redirect-only", "redirect_to": "pharez"},
    "pharida":                  {"status": "names-only"},   # apocryphal (1 Esd 5:31)
    "pharira":                  {"status": "names-only"},   # apocryphal
    "pharzites":                {"status": "names-only"},   # Num 26:20 descendants of Perez; minor
    "phaseah-paseah":           {"status": "names-only"},   # post-exilic family (Ezra 2:49); minor
    "phasiron":                 {"status": "names-only"},   # apocryphal
    "phassaron":                {"status": "names-only"},   # apocryphal (1 Esd 5:25)
    "phassurus":                {"status": "names-only"},   # apocryphal variant of Pashhur
    "pheresites":               {"status": "redirect-only", "redirect_to": "perizzites"},  # variant spelling
    "pherezite":                {"status": "redirect-only", "redirect_to": "perizzites"},  # variant spelling
    "phi-beseth":               {"status": "names-only"},   # Egyptian city Bubastis (Ezek 30:17); place
    "philarches":               {"status": "names-only"},   # Greek administrative title; apocryphal
    "philip-1":                 {"status": "names-only"},   # ISBE disambiguation; covered under "philip" in Easton
    "philip-2":                 {"status": "names-only"},   # ISBE disambiguation; covered under "philip" in Easton
    "philip-3":                 {"status": "names-only"},   # ISBE disambiguation; covered under "philip" in Easton
    "philip-the-gospel-of":     {"status": "names-only"},   # gnostic gospel; apocryphal
    # ISBE compound; redirect to canonical Philippians article
    "philippians-the-epistle-to-the": {"status": "redirect-only", "redirect_to": "philippians"},
    # ISBE variant; redirect to canonical Philistines article
    "philistim":                {"status": "redirect-only", "redirect_to": "philistines"},
    "philistines-lords-of-the": {"status": "names-only"},   # five lords (Josh 13:3); covered under "philistines"
    "philistines-sea-of-the":   {"status": "names-only"},   # Exod 23:31 Mediterranean; geographic; brief
    # Jewish philosopher (c.20 BC – 50 AD); Logos as intermediary between God and creation
    # (anticipated John 1:1); allegorical interpretation of Scripture; bridge between Greek
    # philosophy and Jewish faith; influential on early church Fathers; NT background for
    # understanding Hebrews and Johannine literature
    "philo-judaeus":            {"status": "stub-needed"},
    "philometor":               {"status": "names-only"},   # Ptolemy VI; apocryphal context
    "phinees":                  {"status": "names-only"},   # apocryphal variant of Phinehas
    "phinoe":                   {"status": "names-only"},   # apocryphal
    "phoenice":                 {"status": "names-only"},   # Acts 27:12 harbor; covered under "phoenix"
    # ISBE compound; redirect to canonical Phenicia/Phoenicia article
    "phoenicia;-phoenicians":   {"status": "redirect-only", "redirect_to": "phenicia"},
    "phoenix":                  {"status": "names-only"},   # Crete harbor (Acts 27:12); geographic; brief
    "phoros":                   {"status": "names-only"},   # apocryphal (1 Esd 5:9)
    "phrurai":                  {"status": "names-only"},   # apocryphal
    "phygelus;-phygellus":      {"status": "names-only"},   # 2 Tim 1:15; minor NT figure
    "phylarch":                 {"status": "names-only"},   # Greek tribal leader title; apocryphal
    "phylarches":               {"status": "names-only"},   # Greek title variant; apocryphal
    "piece":                    {"status": "names-only"},   # lexical
    "piece-of-money":           {"status": "names-only"},   # shekel/coin; covered under "money"
    "pilate-acts-of":           {"status": "names-only"},   # pseudepigraphical; apocryphal
    "pile":                     {"status": "names-only"},   # lexical; brief
    "pilgrim;-pilgrimage":      {"status": "names-only"},   # 1 Pet 2:11; Heb 11:13; covered under "pilgrim"
    "pilha":                    {"status": "names-only"},   # post-exilic signatory (Neh 10:24); minor
    "pill":                     {"status": "names-only"},   # Gen 30:37-38 KJV Jacob's rods; archaic
    "pillar-of-salt":           {"status": "names-only"},   # Gen 19:26 Lot's wife; covered under "Lot"
    "pillars-of-the-earth":     {"status": "names-only"},   # 1 Sam 2:8; Job 9:6; poetic; lexical
    "pillow":                   {"status": "names-only"},   # Gen 28:11; 1 Sam 19:13; cultural; brief
    "pilot":                    {"status": "names-only"},   # Ezek 27:8; nautical; brief
    "piltai":                   {"status": "names-only"},   # post-exilic priest (Neh 12:17); minor
    "pin":                      {"status": "names-only"},   # Judg 16:13-14 Delilah; brief
    "pine":                     {"status": "names-only"},   # Isa 41:19; Neh 8:15; botanical; brief
    "pining-sickness":          {"status": "names-only"},   # Isa 10:18 KJV; archaic
    "pinion":                   {"status": "names-only"},   # Isa 40:31 KJV "wing"; archaic
    "pira":                     {"status": "names-only"},   # apocryphal
    "pirathon;-pirathonite":    {"status": "names-only"},   # ISBE compound; Ephraim town (Judg 12:13-15); place
    # ISBE compound; redirect to canonical Pison article (Eden river, Gen 2:11)
    "pishon;-pison":            {"status": "redirect-only", "redirect_to": "pison"},
    "pispa":                    {"status": "names-only"},   # Asherite (1 Chr 7:38); minor
    "pitiful":                  {"status": "names-only"},   # KJV "compassionate" (Lam 4:10; Jas 5:11); archaic
    "pity":                     {"status": "names-only"},   # lexical; covered under "compassion"
    "place":                    {"status": "names-only"},   # lexical
    "place-broad;-high":        {"status": "names-only"},   # KJV topographical terms; lexical
    # The ten plagues: Nile to blood (Exod 7:20), frogs (8:6), gnats (8:17), flies (8:24),
    # livestock disease (9:6), boils (9:10), hail (9:22), locusts (10:13), darkness (10:22),
    # death of firstborn (12:29); each plague confronts an Egyptian deity; theological theme:
    # "that you may know that I am the LORD" (Exod 10:2); foundational for Exodus narrative
    "plagues-of-egypt":         {"status": "stub-needed"},
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
    print(f'BPG Curation C60: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
