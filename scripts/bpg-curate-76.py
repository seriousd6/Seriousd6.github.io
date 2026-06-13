"""
BPG Curation — Batch C76: betrayal → creed (gaps 7689–7793)
Gaps reviewed: 105 (score-5 isbe-scholarly B–C entries — ethics, culture, minor theology)

Score-5 B–C ISBE entries: mostly ethical abstractions, minor cultural practices, KJV lexical
terms. Notable stubs: Betrothal (Jewish binding engagement; Matt 1:18-19; Deut 22:23-27),
Burning Bush (Exod 3:1-15; theophany; divine name "I AM").
2 stub-needed; 0 redirect-only; 103 names-only.

Script: scripts/bpg-curate-76.py
Run: python3 scripts/bpg-curate-76.py  (from project root)
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
    "betrayal":              {"status": "names-only"},   # covered under Judas in Easton; lexical
    # Jewish law: betrothal was legally binding (Deut 22:23-27; "if a man finds a betrothed girl…");
    # Joseph "minded to put her away privily" (Matt 1:18-19); mohar (bride price); 12-month waiting;
    # essential context for understanding birth narrative and Jewish marriage customs
    "betrothal":             {"status": "stub-needed"},
    "betting":               {"status": "names-only"},   # gambling; names-only
    "bigamy":                {"status": "names-only"},   # polygamy context; covered under marriage
    "bill-of-divorce":       {"status": "names-only"},   # Deut 24:1-4; Matt 5:31; covered under divorce
    "blacksmith":            {"status": "names-only"},   # 1 Sam 13:19; craft; names-only
    "blain":                 {"status": "names-only"},   # KJV Exod 9:9-10 "boils and blains"; lexical
    "blasting":              {"status": "names-only"},   # Deut 28:22 crop disease; lexical
    "blushing":              {"status": "names-only"},   # Ezra 9:6; Jer 6:15; lexical
    "boar-wild":             {"status": "names-only"},   # Ps 80:13; animal; names-only
    "boiling-pot":           {"status": "names-only"},   # Ezek 24:3-14; Jer 1:13; symbolic; names-only
    "bones":                 {"status": "names-only"},   # Ezek 37 dry bones covered under that passage; lexical
    "boring-the-ear":        {"status": "names-only"},   # Exod 21:6 slave rite; covered under servants
    "botanical-gardens":     {"status": "names-only"},   # Eccl 2:5; cultural; names-only
    "box-tree":              {"status": "names-only"},   # Isa 41:19 tree variety; botanical
    "brazier":               {"status": "names-only"},   # Jer 36:22-23 fire pan; cultural
    "breath":                {"status": "names-only"},   # Gen 2:7 covered under creation/soul; lexical
    "bridegroom":            {"status": "names-only"},   # covered under marriage in Easton
    "brothel":               {"status": "names-only"},   # sexual immorality context; names-only
    "brotherly-kindness":    {"status": "names-only"},   # 2 Pet 1:7; covered under love; lexical
    "bull":                  {"status": "names-only"},   # animal sacrifice; covered under sacrifice in Easton
    "burning":               {"status": "names-only"},   # lexical; names-only
    # Exod 3:1-15: "the bush was burning but not consumed"; "I AM WHO I AM" (v.14); "holy ground";
    # Moses' call to lead Israel; first revelation of divine name YHWH; foundational OT theophany
    "burning-bush":          {"status": "stub-needed"},
    "buzzi":                 {"status": "names-only"},   # Ezekiel's father (Ezek 1:3); minor figure
    "cabinet":               {"status": "names-only"},   # political office; cultural; names-only
    "caleb-ephratah":        {"status": "names-only"},   # place (1 Chr 2:24); minor geographic
    "calkers-caulkers":      {"status": "names-only"},   # Ezek 27:9,27 ship repairers; names-only
    "candidate":             {"status": "names-only"},   # lexical; names-only
    "cannibalism":           {"status": "names-only"},   # Lev 26:29; 2 Kgs 6:28-29 siege; names-only
    "caphtorim":             {"status": "names-only"},   # Deut 2:23; covered under Philistines
    "capital-and-labor":     {"status": "names-only"},   # social concept; names-only
    "capital-punishment":    {"status": "names-only"},   # Exod 21:12; covered under law in Easton
    "carnal-mindedness":     {"status": "names-only"},   # Rom 8:6-7; covered under flesh in Easton
    "carpentry":             {"status": "names-only"},   # Joseph's trade; cultural; names-only
    "carpet":                {"status": "names-only"},   # cultural; names-only
    "casting":               {"status": "names-only"},   # lexical (lots, demons); names-only
    "caution":               {"status": "names-only"},   # Prov wisdom theme; names-only
    "cavalry":               {"status": "names-only"},   # military; names-only
    "celibacy":              {"status": "names-only"},   # Matt 19:12; 1 Cor 7:8; covered under marriage
    "censoriousness":        {"status": "names-only"},   # Matt 7:1; names-only
    "cesarea-philippi":      {"status": "names-only"},   # variant of Caesarea Philippi; covered in Easton
    "chaldeans":             {"status": "names-only"},   # covered under Chaldea in Easton
    "chalk":                 {"status": "names-only"},   # Isa 27:9; material; names-only
    "championship":          {"status": "names-only"},   # names-only
    "change-of-venue":       {"status": "names-only"},   # legal; names-only
    "charge":                {"status": "names-only"},   # lexical; names-only
    "charism":               {"status": "names-only"},   # 1 Cor 12; covered under spiritual gifts in Easton
    "charmers-and-charming": {"status": "names-only"},   # Ps 58:5; Isa 19:3; covered under magic
    "cheating":              {"status": "names-only"},   # Lev 19:35-36; names-only
    "cheerfulness":          {"status": "names-only"},   # Prov 17:22; virtue; names-only
    "chelubi":               {"status": "names-only"},   # 1 Chr 2:9 variant; names-only
    "chickens":              {"status": "names-only"},   # Matt 23:37; names-only
    "childlessness":         {"status": "names-only"},   # Sarah, Rachel, Hannah context; names-only
    "chinese":               {"status": "names-only"},   # ISBE note on Sinim/China; too speculative
    "choosing":              {"status": "names-only"},   # covered under election in Easton
    "choruses":              {"status": "names-only"},   # worship music; names-only
    "chosen-or-elected":     {"status": "names-only"},   # ISBE compound; covered under election
    "chrysolyte":            {"status": "names-only"},   # gem (Rev 21:20); names-only
    "churning":              {"status": "names-only"},   # Prov 30:33; names-only
    "civil-damages":         {"status": "names-only"},   # OT law; names-only
    "civil-engineering":     {"status": "names-only"},   # cultural; names-only
    "clairvoyance":          {"status": "names-only"},   # divination context; names-only
    "claudius-lysius":       {"status": "names-only"},   # Roman tribune (Acts 21-23); minor figure
    "clean-and-unclean-animals": {"status": "names-only"},  # Lev 11; covered under clean in Easton
    "cleanliness":           {"status": "names-only"},   # Lev 11-15; covered under purification
    "cleansing":             {"status": "names-only"},   # ritual; covered under purification
    "clergyman":             {"status": "names-only"},   # anachronistic; names-only
    "coal-oil":              {"status": "names-only"},   # names-only
    "cock-crowing":          {"status": "names-only"},   # Peter's denial; covered under Peter/cock in Easton
    "coercion":              {"status": "names-only"},   # legal/ethical; names-only
    "collusion":             {"status": "names-only"},   # legal/ethical; names-only
    "colonization":          {"status": "names-only"},   # historical; names-only
    "colosse-colossae":      {"status": "names-only"},   # ISBE compound; covered under Colossae in Easton
    "colt":                  {"status": "names-only"},   # Matt 21:5 triumphal entry; covered there
    "commissary":            {"status": "names-only"},   # supply; names-only
    "communism":             {"status": "names-only"},   # anachronistic; names-only
    "compasses":             {"status": "names-only"},   # Isa 44:13 drafting tool; names-only
    "complaint":             {"status": "names-only"},   # Ps 55:2; lexical; names-only
    "complicity":            {"status": "names-only"},   # legal/ethical; names-only
    "compromise":            {"status": "names-only"},   # ethical concept; names-only
    "conception":            {"status": "names-only"},   # Ps 51:5; Job 3:3; names-only
    "condemnation-self":     {"status": "names-only"},   # ISBE compound; names-only
    "condolence":            {"status": "names-only"},   # cultural practice; names-only
    "confectioner":          {"status": "names-only"},   # 1 Sam 8:13; names-only
    "confederacies":         {"status": "names-only"},   # political alliances; names-only
    "congestion":            {"status": "names-only"},   # names-only
    "connivance":            {"status": "names-only"},   # ethical; names-only
    "conscience-money":      {"status": "names-only"},   # Matt 27:3-10 Judas's silver; names-only
    "conscientiousness":     {"status": "names-only"},   # virtue; names-only
    "conscription":          {"status": "names-only"},   # 1 Sam 8:11-12; names-only
    "consecrated-things":    {"status": "names-only"},   # Lev 27; names-only
    "consistency":           {"status": "names-only"},   # virtue; names-only
    "constancy":             {"status": "names-only"},   # virtue; names-only
    "constitution":          {"status": "names-only"},   # political; names-only
    "contempt-of-court":     {"status": "names-only"},   # legal; names-only
    "contention":            {"status": "names-only"},   # Prov 13:10; names-only
    "continents":            {"status": "names-only"},   # geographic concept; names-only
    "contrition":            {"status": "names-only"},   # Ps 51; covered under repentance in Easton
    "convention":            {"status": "names-only"},   # names-only
    "conveyance":            {"status": "names-only"},   # names-only
    "copulation":            {"status": "names-only"},   # names-only
    "corporal-punishment":   {"status": "names-only"},   # Deut 25:3; names-only
    "corpulency":            {"status": "names-only"},   # names-only
    "cosmetics":             {"status": "names-only"},   # Ezek 23:40; 2 Kgs 9:30; names-only
    "counsel":               {"status": "names-only"},   # Prov 11:14; Isa 9:6; names-only
    "courtesy":              {"status": "names-only"},   # virtue; names-only
    "courtship":             {"status": "names-only"},   # cultural; names-only
    "craftiness":            {"status": "names-only"},   # 1 Cor 3:19; Eph 4:14; names-only
    "craftsman":             {"status": "names-only"},   # Deut 27:15; cultural; names-only
    "creed":                 {"status": "names-only"},   # covered under confessions/creeds; names-only
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
    print(f'BPG Curation C76: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
