"""
BPG Curation — Batch C81: prophetesses → state (gaps 8118–8222)
Gaps reviewed: 105 (score-3 concept-no-article P–S entries)

Score-3 concept-no-article entries. Conservative posture for generic/minor terms;
stub-needed for theologically significant concepts with ≥9 nave verses or unique
biblical significance regardless of verse count (seraphim, rebekah).

20 stub-needed; 1 redirect-only; 7 names-only; 77 skip.

Stubs: prophetesses (Miriam/Deborah/Huldah/Anna, 12v), prosperity (17v),
publicans (NT tax-collectors, 16v), quickening (spiritual life, 11v),
rebekah-rebecca (wife of Isaac), rebellion (vice, 9v), refining (spiritual
metaphor, Mal 3:3, 11v), restitution (OT legal concept, 10v), sabbatic-year
(OT institution, 15v), sacrifices (13v), security (spiritual assurance, 18v),
self-condemnation (18v), self-exaltation (19v), self-examination (spiritual
practice, 18v), seraphim-seraphs (Isaiah 6 angelic beings), shushan-susa
(Persian capital — Esther/Daniel, 12v), sobriety (spiritual virtue, 15v),
sower (major parable, 12v), sprinkling (ritual purification — Hebrews, 12v),
standard (messianic banner, Isa 11:12, 11v).

Redirects: proud→pride.

Script: scripts/bpg-curate-81.py
Run: python3 scripts/bpg-curate-81.py  (from project root)
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
    # --- stub-needed ---
    "prophetesses":             {"status": "stub-needed"},
    "prosperity":               {"status": "stub-needed"},
    "publicans":                {"status": "stub-needed"},
    "quickening":               {"status": "stub-needed"},
    "rebekah-rebecca":          {"status": "stub-needed"},
    "rebellion":                {"status": "stub-needed"},
    "refining":                 {"status": "stub-needed"},
    "restitution":              {"status": "stub-needed"},
    "sabbatic-year":            {"status": "stub-needed"},
    "sacrifices":               {"status": "stub-needed"},
    "security":                 {"status": "stub-needed"},
    "self-condemnation":        {"status": "stub-needed"},
    "self-exaltation":          {"status": "stub-needed"},
    "self-examination":         {"status": "stub-needed"},
    "seraphim-seraphs":         {"status": "stub-needed"},
    "shushan-susa":             {"status": "stub-needed"},
    "sobriety":                 {"status": "stub-needed"},
    "sower":                    {"status": "stub-needed"},
    "sprinkling":               {"status": "stub-needed"},
    "standard":                 {"status": "stub-needed"},

    # --- redirect-only ---
    "proud":                    {"status": "redirect-only", "redirect_to": "pride"},

    # --- names-only ---
    "rab-shakeh-rabshakeh":     {"status": "names-only"},
    "rabbath":                  {"status": "names-only"},
    "sabta":                    {"status": "names-only"},
    "samothracia-samothrace":   {"status": "names-only"},
    "shebna-shebnah":           {"status": "names-only"},
    "shimronites":              {"status": "names-only"},
    "siloah":                   {"status": "names-only"},

    # --- skip ---
    "protracted-meetings":          {"status": "skip"},
    "proxy":                        {"status": "skip"},
    "pruning":                      {"status": "skip"},
    "purveyor":                     {"status": "skip"},
    "quarantine":                   {"status": "skip"},
    "railing":                      {"status": "skip"},
    "raiment-clothing":             {"status": "skip"},
    "raising":                      {"status": "skip"},
    "ravishment":                   {"status": "skip"},
    "reciprocity":                  {"status": "skip"},
    "reconnoissance":               {"status": "skip"},
    "recreation-rest":              {"status": "skip"},
    "refugee-slaves":               {"status": "skip"},
    "regency":                      {"status": "skip"},
    "regicide":                     {"status": "skip"},
    "registration":                 {"status": "skip"},
    "rejection":                    {"status": "skip"},
    "renting":                      {"status": "skip"},
    "repetition":                   {"status": "skip"},
    "reports":                      {"status": "skip"},
    "reproduction":                 {"status": "skip"},
    "respect":                      {"status": "skip"},
    "responsive-religious-service": {"status": "skip"},
    "reviling":                     {"status": "skip"},
    "revolt":                       {"status": "skip"},
    "roads":                        {"status": "skip"},
    "robbers":                      {"status": "skip"},
    "rye-spelt-r.-v.":              {"status": "skip"},
    "sabbath-day-s-journey":        {"status": "skip"},
    "sailors":                      {"status": "skip"},
    "satire":                       {"status": "skip"},
    "saviour-savior":               {"status": "skip"},
    "scab":                         {"status": "skip"},
    "scapebird":                    {"status": "skip"},
    "scepter-sceptre":              {"status": "skip"},
    "scriptures":                   {"status": "skip"},
    "seamen":                       {"status": "skip"},
    "secretary-recordist":          {"status": "skip"},
    "seduction":                    {"status": "skip"},
    "seizin":                       {"status": "skip"},
    "self-confidence":              {"status": "skip"},
    "self-deception":               {"status": "skip"},
    "self-defense":                 {"status": "skip"},
    "self-incrimination":           {"status": "skip"},
    "self-indulgence":              {"status": "skip"},
    "sensuality":                   {"status": "skip"},
    "sentry":                       {"status": "skip"},
    "sergeant":                     {"status": "skip"},
    "sermon":                       {"status": "skip"},
    "shouting":                     {"status": "skip"},
    "sick-the":                     {"status": "skip"},
    "sickness":                     {"status": "skip"},
    "sieve":                        {"status": "skip"},
    "signal":                       {"status": "skip"},
    "simony":                       {"status": "skip"},
    "sinews":                       {"status": "skip"},
    "singers":                      {"status": "skip"},
    "singing":                      {"status": "skip"},
    "skepticism":                   {"status": "skip"},
    "slavery":                      {"status": "skip"},
    "smiting":                      {"status": "skip"},
    "snuffdishes":                  {"status": "skip"},
    "snuffers":                     {"status": "skip"},
    "sounding":                     {"status": "skip"},
    "spermatorrhea":                {"status": "skip"},
    "spiritual-blessings":          {"status": "skip"},
    "spiritual-blindness":          {"status": "skip"},
    "spiritual-diligence":          {"status": "skip"},
    "spiritual-peace":              {"status": "skip"},
    "spiritualism":                 {"status": "skip"},
    "spitting":                     {"status": "skip"},
    "spoils":                       {"status": "skip"},
    "spoons":                       {"status": "skip"},
    "stability":                    {"status": "skip"},
    "stairs":                       {"status": "skip"},
    "stammering":                   {"status": "skip"},
    "state":                        {"status": "skip"},
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
    print(f'BPG Curation C81: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
