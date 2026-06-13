"""
BPG Curation — Batch C72: tower-of-siloam → uzzen-sheerah (gaps 7364–7468)
Gaps reviewed: 105 (score-5 isbe-scholarly T–U entries)

Score-5 T–U ISBE entries: overwhelmingly lexical KJV terms, minor geographic variants,
apocryphal figures, Hebrew letter names, and disambiguation forms.
Notable stubs: Transfiguration (Matt 17 Christological event), Trial of Jesus (Sanhedrin +
Pilate; Matt 26-27), Unpardonable Sin (blasphemy against Holy Spirit; Matt 12:31-32).
3 stub-needed; 3 redirect-only; 99 names-only.

Script: scripts/bpg-curate-72.py
Run: python3 scripts/bpg-curate-72.py  (from project root)
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
    "tower-of-siloam":      {"status": "names-only"},   # Luke 13:4 "tower in Siloam fell"; geographic; covered under Siloam
    "tower-of-syene":       {"status": "names-only"},   # Ezek 29:10 geographic reference; names-only
    "town":                 {"status": "names-only"},   # lexical
    "trade":                {"status": "names-only"},   # general; lexical
    "trades":               {"status": "names-only"},   # lexical
    "traffic-trafficker":   {"status": "names-only"},   # KJV commercial term; lexical
    "tragacanth":           {"status": "names-only"},   # gum/plant material; Gen 43:11; botanical
    "train":                {"status": "names-only"},   # lexical
    "train;-trained":       {"status": "names-only"},   # ISBE compound; lexical
    # Jesus' transfiguration (Matt 17:1-9; Mark 9:2-8; Luke 9:28-36): Moses and Elijah appear;
    # voice from cloud "this is my beloved Son"; Jesus' glory revealed; Peter's three tents;
    # key Christological event confirming divine nature and fulfillment of Law and Prophets
    "transfiguration":      {"status": "stub-needed"},
    # redirect ISBE place-form to the main event article
    "transfiguration-mount-of": {"status": "redirect-only", "redirect_to": "transfiguration"},
    "transform":            {"status": "names-only"},   # Rom 12:2 "be transformed"; lexical
    "transgression":        {"status": "names-only"},   # covered under sin/trespass in Easton; lexical
    "translation":          {"status": "names-only"},   # Bible versions / Enoch translation; too broad; lexical
    "trap":                 {"status": "names-only"},   # hunting/figurative; lexical
    "travail":              {"status": "names-only"},   # KJV "labor/birth pangs" (Isa 53:11; 1 Thess 5:3); lexical
    "traveller":            {"status": "names-only"},   # lexical
    "tread":                {"status": "names-only"},   # lexical
    "treason":              {"status": "names-only"},   # lexical; covered under political context
    "treasure;-treasurer;-treasury": {"status": "names-only"},  # covered under temple/economy in Easton
    "treasurer":            {"status": "names-only"},   # Ezra 1:8; title; names-only
    "treasury-of-temple":   {"status": "names-only"},   # covered under temple in Easton
    "treaty":               {"status": "names-only"},   # covenant/political agreement; lexical
    "tree":                 {"status": "names-only"},   # general; individual trees covered separately
    "trees-goodly":         {"status": "names-only"},   # KJV Neh 8:15; Lev 23:40; lexical
    "trees-shady":          {"status": "names-only"},   # KJV; botanical; lexical
    "trees-thick":          {"status": "names-only"},   # KJV; botanical; lexical
    "trench":               {"status": "names-only"},   # 1 Kgs 18:32 Elijah's trench; lexical
    "trespass":             {"status": "names-only"},   # covered under sin/transgression in Easton; lexical
    # Jewish trial before Sanhedrin (Matt 26:57-68; Mark 14:53-65): false witnesses, high priest's
    # challenge, Jesus' "I am" declaration; Roman trial before Pilate (Matt 27:1-26; Luke 23:1-25):
    # "I find no fault in him"; Barabbas exchange; crown of thorns; foundational to Passion narrative
    "trial-of-jesus":       {"status": "stub-needed"},
    "triclinium":           {"status": "names-only"},   # Roman three-sided dining room; cultural context
    "trim":                 {"status": "names-only"},   # lexical
    "trine-immersion;-triune-immersion": {"status": "names-only"},  # baptism practice variant; too specialized
    "tripolis":             {"status": "names-only"},   # Phoenician city; extra-biblical; apocryphal context
    "triumph":              {"status": "names-only"},   # Roman triumph; 2 Cor 2:14; lexical
    "troop":                {"status": "names-only"},   # lexical; military
    "trough":               {"status": "names-only"},   # Gen 24:20 watering trough; lexical
    "trow":                 {"status": "names-only"},   # KJV "think/believe" (Luke 17:9); lexical
    "trucebkeaker":         {"status": "names-only"},   # KJV typo for "trucebreaker" (2 Tim 3:3); lexical
    "trump;-trumpet":       {"status": "names-only"},   # covered under "trumpet" in Easton
    "trust-breach-of":      {"status": "names-only"},   # compound; names-only
    "tryphaena":            {"status": "names-only"},   # Roman woman "who work hard in the Lord" (Rom 16:12)
    "tsadhe":               {"status": "names-only"},   # Hebrew letter; names-only
    "tubias":               {"status": "names-only"},   # apocryphal figure; names-only
    "tubieni":              {"status": "names-only"},   # apocryphal people/place; names-only
    "tumor":                {"status": "names-only"},   # 1 Sam 5:6 Philistine plague; lexical
    "turban":               {"status": "names-only"},   # priestly headgear; covered under "mitre/turban" in Easton
    "turtle-dove":          {"status": "names-only"},   # sacrifice animal (Lev 1:14; Luke 2:24); names-only
    "tutor":                {"status": "names-only"},   # Gal 3:24 KJV "schoolmaster/tutor"; lexical
    "twelve":               {"status": "names-only"},   # number; names-only
    "twelve-apostles-gospels-of-the": {"status": "names-only"},  # apocryphal; extracanonical
    "twelve-patriarchs;-testaments-of-the": {"status": "names-only"},  # pseudepigraphical; too specialized
    "twelve-stars":         {"status": "names-only"},   # Rev 12:1 crown of 12 stars; symbol; brief
    "twenty":               {"status": "names-only"},   # number; names-only
    "twilight":             {"status": "names-only"},   # lexical; Prov 7:9; names-only
    "twine":                {"status": "names-only"},   # tabernacle material (Exod 26:1); lexical
    "two":                  {"status": "names-only"},   # number; names-only
    "tyre-ladder-of":       {"status": "names-only"},   # geographic; 1 Macc 11:59; apocryphal
    "tyropoeon-the":        {"status": "names-only"},   # Jerusalem valley ("Cheesemakers' Valley"); geographic
    "tzaddi":               {"status": "names-only"},   # Hebrew letter variant; names-only
    "umpire":               {"status": "names-only"},   # Job 9:33 "umpire between us"; lexical
    "unbelief":             {"status": "names-only"},   # covered under "faith" inversely in Easton; lexical
    "unbeliever":           {"status": "names-only"},   # 1 Cor 6:6; lexical
    "uncertain;-uncertainty": {"status": "names-only"},  # 1 Tim 6:17; lexical
    "unchangeable;-unchangeableness": {"status": "names-only"},  # God's immutability; covered under "God" in Easton
    "unchastity":           {"status": "names-only"},   # Matt 5:32; lexical; covered under adultery
    # ISBE compound; redirect to canonical Easton article
    "uncircumcised;-uncircumcision": {"status": "redirect-only", "redirect_to": "circumcision"},
    "uncle":                {"status": "names-only"},   # Lev 10:4; lexical; names-only
    "unclean-spirit":       {"status": "names-only"},   # covered under "demon/demoniacs" in Easton
    "unclothed":            {"status": "names-only"},   # 2 Cor 5:4; lexical
    "undefiled":            {"status": "names-only"},   # Heb 7:26; Ps 119:1; lexical
    "underneath":           {"status": "names-only"},   # Deut 33:27; lexical
    "undersetter":          {"status": "names-only"},   # KJV "support" for lavers (1 Kgs 7:30); lexical
    "undertake":            {"status": "names-only"},   # Isa 38:14; lexical
    "unequal":              {"status": "names-only"},   # Ezek 18:25; lexical
    "unfeigned":            {"status": "names-only"},   # KJV "sincere" (1 Tim 1:5; 2 Tim 1:5); lexical
    "ungodly":              {"status": "names-only"},   # Ps 1:1; lexical; covered under "wicked" generally
    "unity":                {"status": "names-only"},   # Eph 4:3 "unity of the Spirit"; lexical
    "unknown-god":          {"status": "names-only"},   # Acts 17:23 "To an Unknown God"; covered under Athens/Mars Hill
    "unlearned":            {"status": "names-only"},   # KJV Acts 4:13 "unlearned and ignorant men"; lexical
    "unleavened":           {"status": "names-only"},   # covered under "leaven" and "Passover" in Easton
    "unnatural-vice":       {"status": "names-only"},   # Rom 1:26-27 euphemism; names-only
    "unno":                 {"status": "names-only"},   # minor name (1 Esd 9:48 / Neh 8:7 Nuno); names-only
    # "blasphemy against the Holy Spirit will not be forgiven" (Matt 12:31-32; Mark 3:28-29;
    # Luke 12:10); ongoing theological debate: attributing Holy Spirit's works to Satan;
    # hardening of heart beyond repentance; Calvinist vs. Arminian readings; pastoral concern
    "unpardonable-sin":     {"status": "stub-needed"},
    "unquenchable-fire":    {"status": "names-only"},   # Matt 3:12; eschatological; covered under hell/judgment
    "untempered":           {"status": "names-only"},   # KJV "mortar without lime" (Ezek 13:10); lexical
    "untoward":             {"status": "names-only"},   # KJV "perverse" (Acts 2:40); lexical
    "unwalled":             {"status": "names-only"},   # Ezek 38:11; Deut 3:5; lexical
    "unwashen":             {"status": "names-only"},   # KJV "unwashed" (Mark 7:2); lexical
    "unworthly":            {"status": "names-only"},   # KJV typo "unworthily" (1 Cor 11:27); lexical
    "unwritten-sayings":    {"status": "names-only"},   # agrapha; extracanonical; too specialized at score-5
    "upper-chamber;-upper-room": {"status": "names-only"},  # covered under "upper room" in Easton
    # Abraham's origin city; ISBE compound; redirect to canonical Easton article
    "ur-of-the-chaldees":   {"status": "redirect-only", "redirect_to": "ur"},
    "uriah;-uruah":         {"status": "names-only"},   # ISBE compound; covered under Uriah in Easton
    "urias-1":              {"status": "names-only"},   # NT disambiguation (Matt 1:6; Ezra 8:33)
    "urias-2":              {"status": "names-only"},   # NT disambiguation (Neh 3:4,21)
    "uriel-1":              {"status": "names-only"},   # Levite (1 Chr 6:24; 15:5,11); minor figure
    "uriel-2":              {"status": "names-only"},   # Maachah's father (2 Chr 13:2); minor figure
    "uthi":                 {"status": "names-only"},   # Neh 11:22 / 1 Chr 9:4 Uthai variant; minor
    "utmost-sea;-uttermost-sea": {"status": "names-only"},  # Deut 11:24 "western/Mediterranean Sea"; lexical
    "uttermost":            {"status": "names-only"},   # lexical; Matt 5:26; Acts 1:8
    "uz-1":                 {"status": "names-only"},   # Job's homeland (Job 1:1); covered under Uz in Easton
    "uz-2":                 {"status": "names-only"},   # disambiguation; son of Nahor (Gen 22:21)
    "uzza;-uzzah":          {"status": "names-only"},   # ISBE compound; covered under Uzzah in Easton
    "uzzen-sheerah":        {"status": "names-only"},   # town built by Sheerah (1 Chr 7:24); minor place
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
    print(f'BPG Curation C72: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
