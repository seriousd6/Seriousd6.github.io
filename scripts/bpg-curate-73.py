"""
BPG Curation — Batch C73: uzziah;-azariah → weight (gaps 7469–7573)
Gaps reviewed: 105 (score-5 isbe-scholarly U–W entries)

Score-5 V–W ISBE entries: mostly lexical KJV terms, minor geographic variants,
Hebrew letters, and disambiguation forms. Notable stubs: virgin-birth (Matt 1/Luke 1),
weeks-seventy (Dan 9 seventy-weeks prophecy).
2 stub-needed; 11 redirects; 92 names-only.

Redirects: uzziah;-azariah→uzziah; vail/veil-1/veil-2→veil-vail;
virgin-virginity→virgin; vow→vows; wanderings-of-israel→wandering;
war;-warfare/warfare→war; wars-of-yahweh-the-lord-book-of-the→wars-of-the-lord-the-book-of-the;
wash;-washing→washing.

Script: scripts/bpg-curate-73.py
Run: python3 scripts/bpg-curate-73.py  (from project root)
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
    # ISBE compound; 2 Kgs 14:21; Easton has uzziah.json (Azariah = Uzziah king of Judah)
    "uzziah;-azariah":           {"status": "redirect-only", "redirect_to": "uzziah"},
    "vaheb":                     {"status": "names-only"},   # Num 21:14 KJV obscure place; minor
    # KJV spelling of veil; ISBE; Easton has veil-vail.json
    "vail":                      {"status": "redirect-only", "redirect_to": "veil-vail"},
    "vain":                      {"status": "names-only"},   # lexical; covered under "vanity"
    "vainglory":                 {"status": "names-only"},   # Gal 5:26; Phil 2:3; lexical
    "vaizatha;-vajezatha":       {"status": "names-only"},   # ISBE compound; Esther 9:9 Haman's son; minor
    "valiant-valiantly":         {"status": "names-only"},   # ISBE compound; lexical
    "valley-gate":               {"status": "names-only"},   # Neh 2:13; 3:13; Jerusalem gate; minor
    "valley-of-decision":        {"status": "names-only"},   # Joel 3:14; covered under "Joel"
    "valley-of-giants":          {"status": "names-only"},   # Josh 15:8 Rephaim; covered under "rephaim"
    "valley-of-keziz":           {"status": "names-only"},   # Josh 18:21 Benjamin border; minor place
    "valley-of-slaughter":       {"status": "names-only"},   # Jer 7:32; covered under "Hinnom valley"
    "valley-of-vision":          {"status": "names-only"},   # Isa 22:1; covered under "Isaiah"
    "valley-jordan":             {"status": "names-only"},   # ISBE place; covered under "Jordan"
    "vampire":                   {"status": "names-only"},   # Prov 30:15 KJV "horseleach" debate; not biblical; names-only
    "vanity-vanities":           {"status": "names-only"},   # ISBE compound; Eccl 1:2; lexical
    "vapor":                     {"status": "names-only"},   # Jas 4:14; lexical
    "vat":                       {"status": "names-only"},   # Isa 63:2; Joel 3:13; lexical
    "vault":                     {"status": "names-only"},   # Amos 9:6; architectural; lexical
    "vault-of-earth":            {"status": "names-only"},   # ISBE scholarly; cosmological; names-only
    "vav":                       {"status": "names-only"},   # Hebrew letter; covered under "Hebrew alphabet"
    "vedan":                     {"status": "names-only"},   # Ezek 27:19 obscure trading place; minor
    "vehement-vehemently":       {"status": "names-only"},   # ISBE compound; lexical
    # ISBE disambiguation; Exod 26:31-35; Easton has veil-vail.json
    "veil-1":                    {"status": "redirect-only", "redirect_to": "veil-vail"},
    # ISBE disambiguation; Matt 27:51 temple veil; Easton has veil-vail.json
    "veil-2":                    {"status": "redirect-only", "redirect_to": "veil-vail"},
    "vein":                      {"status": "names-only"},   # Job 28:1 KJV; archaic; lexical
    "vengeance":                 {"status": "names-only"},   # covered under "avenger of blood"; lexical
    "venison":                   {"status": "names-only"},   # Gen 25:28; 27:3; lexical
    "verdigris":                 {"status": "names-only"},   # rare; not a direct biblical term
    "verily-verity":             {"status": "names-only"},   # ISBE compound; "amen/truly"; lexical
    "vermilion":                 {"status": "names-only"},   # Jer 22:14; Ezek 23:14; color; brief
    "versions":                  {"status": "names-only"},   # too broad; covered under specific version articles
    "versions-georgian-gothic-slavonic": {"status": "names-only"},  # ISBE scholarly; too specialized
    "very":                      {"status": "names-only"},   # lexical
    "vessel":                    {"status": "names-only"},   # lexical; specific vessels covered separately
    "vestments":                 {"status": "names-only"},   # priestly garments; covered under "priest"
    "vestry":                    {"status": "names-only"},   # 2 Kgs 10:22 KJV; archaic; brief
    "vex-vexation":              {"status": "names-only"},   # ISBE compound; Eccl 1:14; lexical
    "vial":                      {"status": "names-only"},   # 1 Sam 10:1; Rev 15:7; lexical
    "vice-unnatural":            {"status": "names-only"},   # Rom 1:26 euphemism; names-only
    "victuals":                  {"status": "names-only"},   # KJV "food"; lexical
    "vile-villany":              {"status": "names-only"},   # ISBE compound; lexical
    "villany":                   {"status": "names-only"},   # Jer 29:23; lexical
    "vineyard":                  {"status": "names-only"},   # covered under "vine" in Easton; lexical
    "vineyards-meadow-plain-of-the": {"status": "names-only"},  # Judg 11:33 KJV; minor place
    "vintage":                   {"status": "names-only"},   # Lev 26:5; Isa 16:10; agricultural; brief
    "violence-violent":          {"status": "names-only"},   # ISBE compound; Gen 6:11; lexical
    # Matt 1:18-25; Luke 1:26-38; Isa 7:14; Holy Spirit conception; parthenogenesis;
    # Matthew's parthenos citation; Annunciation to Mary; key Christological doctrine;
    # Isa 7:14 almah vs. parthenos debate; essential background for Incarnation theology
    "virgin-birth":              {"status": "stub-needed"},
    # ISBE compound; Deut 22:15; Easton has virgin.json
    "virgin-virginity":          {"status": "redirect-only", "redirect_to": "virgin"},
    "virtue":                    {"status": "names-only"},   # Phil 4:8; 2 Pet 1:5; lexical
    "visitation":                {"status": "names-only"},   # 1 Pet 2:12; Isa 10:3; lexical
    "vocation":                  {"status": "names-only"},   # Eph 4:1 KJV "calling"; lexical
    "voice":                     {"status": "names-only"},   # lexical
    "void":                      {"status": "names-only"},   # Gen 1:2 "without form and void"; lexical
    "volume":                    {"status": "names-only"},   # Ps 40:7 KJV; Heb 10:7; lexical
    "voluntary":                 {"status": "names-only"},   # Lev 1:3 KJV; lexical
    # Num 30:2; Judg 11:30-31; Easton has vows.json
    "vow":                       {"status": "redirect-only", "redirect_to": "vows"},
    "voyage-and-shipwreck-of-paul": {"status": "names-only"},  # Acts 27–28; covered under "paul" and "acts"
    "vulgate":                   {"status": "names-only"},   # Jerome's Latin Bible; covered under "versions"
    "wafer":                     {"status": "names-only"},   # Exod 16:31; Num 6:15; lexical
    "wagon-waggon":              {"status": "names-only"},   # ISBE compound; Gen 45:19; Num 7:3; lexical
    "wail-wailing":              {"status": "names-only"},   # ISBE compound; lexical; covered under "mourning"
    "wait":                      {"status": "names-only"},   # lexical
    "walk":                      {"status": "names-only"},   # lexical; covered under "way" and "sanctification"
    "wallet":                    {"status": "names-only"},   # Matt 10:10 KJV "scrip"; lexical
    "wandering-stars":           {"status": "names-only"},   # Jude 13; covered under "stars"
    # ISBE; Num 14:33; Deut 2:7; Easton has wandering.json
    "wanderings-of-israel":      {"status": "redirect-only", "redirect_to": "wandering"},
    "war-man-of":                {"status": "names-only"},   # Exod 15:3 "LORD is a man of war"; covered under "war"
    # ISBE compound; Exod 15:3; Easton has war.json
    "war;-warfare":              {"status": "redirect-only", "redirect_to": "war"},
    "wares":                     {"status": "names-only"},   # Neh 13:16; Ezek 27:16; lexical; commercial
    # ISBE variant; Easton has war.json
    "warfare":                   {"status": "redirect-only", "redirect_to": "war"},
    "warp":                      {"status": "names-only"},   # Lev 13:48-52 KJV "warp of fabric"; archaic
    # ISBE; Num 21:14; Easton has wars-of-the-lord-the-book-of-the.json
    "wars-of-yahweh-the-lord-book-of-the": {"status": "redirect-only", "redirect_to": "wars-of-the-lord-the-book-of-the"},
    # ISBE compound; Lev 15:11; John 2:6; Easton has washing.json
    "wash;-washing":             {"status": "redirect-only", "redirect_to": "washing"},
    "washing-of-feet":           {"status": "names-only"},   # John 13:1-17; covered under "washing"
    "washpot":                   {"status": "names-only"},   # Ps 60:8; 108:9 KJV; lexical
    "wasp":                      {"status": "names-only"},   # not in canonical Bible directly; names-only
    "watch":                     {"status": "names-only"},   # Matt 24:43; 1 Pet 5:8; lexical
    "watch-tour":                {"status": "names-only"},   # ISBE scholarly; military watch; names-only
    "watcher":                   {"status": "names-only"},   # Dan 4:13,17 KJV; covered under "angel"
    "watchman":                  {"status": "names-only"},   # Isa 52:8; Ezek 33:6; covered under "prophet"
    "water":                     {"status": "names-only"},   # lexical; specific water articles covered separately
    "water-of-bitterness-or-of-jealousy": {"status": "names-only"},  # Num 5:18-27 ordeal; covered under "jealousy"
    "water-of-separation-or-of-uncleanness": {"status": "names-only"},  # Num 19:9,13; ritual; names-only
    "watercourse":               {"status": "names-only"},   # Ps 1:3; Isa 44:4; lexical
    "waterfall":                 {"status": "names-only"},   # Ps 42:7; lexical
    "waterpot":                  {"status": "names-only"},   # John 2:6-7; brief; lexical
    "waters":                    {"status": "names-only"},   # lexical; Gen 1:2; names-only
    "waters-of-merom":           {"status": "names-only"},   # Josh 11:5-7; battle site; minor place
    "waters-of-strife":          {"status": "names-only"},   # Num 20:13 Meribah; covered under "meribah"
    "waterspout":                {"status": "names-only"},   # Ps 42:7 KJV; lexical
    "waw":                       {"status": "names-only"},   # Hebrew letter variant of vav; names-only
    "way":                       {"status": "names-only"},   # lexical; John 14:6 "I am the way"; names-only
    "way-covered":               {"status": "names-only"},   # ISBE scholarly; archaic; names-only
    "way-little":                {"status": "names-only"},   # ISBE scholarly; archaic; names-only
    "wayfaring-man":             {"status": "names-only"},   # Isa 35:8 KJV; archaic
    "waymark":                   {"status": "names-only"},   # Jer 31:21 KJV; lexical
    "wealth-wealthy":            {"status": "names-only"},   # ISBE compound; lexical; covered under "riches"
    "weather":                   {"status": "names-only"},   # Matt 16:2-3; lexical; names-only
    "web":                       {"status": "names-only"},   # Isa 59:5; Job 8:14; lexical
    "wedge-of-gold":             {"status": "names-only"},   # Josh 7:21 KJV "tongue of gold"; covered under "Achan"
    "weeds":                     {"status": "names-only"},   # Jon 2:5 KJV; lexical
    # Dan 9:24-27; seventy weeks of years (490 years); 7+62+1 structure; Messianic interpretation;
    # Futurist/Historicist/Preterist readings; gap theory (church age); "desolating abomination";
    # foundational for NT eschatology and Christology; cuts off vision at Messiah
    "weeks-seventy":             {"status": "stub-needed"},
    "weeping":                   {"status": "names-only"},   # Ps 30:5; John 11:35; covered under "mourning"
    "weight":                    {"status": "names-only"},   # lexical; covered under "weights and measures"
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
    print(f'BPG Curation C73: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
