"""
BPG Curation — Batch C79: ingrafting → mite-a-lepta (gaps 8104–8208)
Gaps reviewed: 105 (score-3 concept-no-article I–M entries)

Score-3 concept-no-article entries: legal concepts, cultural practices, minor
biblical persons/places, ethical abstractions. Conservative posture: 0 stubs.
0 stub-needed; 11 redirect-only; 94 names-only.

Redirects: jailer-jailor→jailer; judgment-hall→judgment-hall;
judgment-seat→judgment-seat; lamentations→lamentations-book-of;
lign-aloe→lign-aloes; magician→magicians; mandrake→mandrakes;
melchesedec→melchizedek; melita-malta→melita; midianites→midianite;
mite-a-lepta→mite.

Script: scripts/bpg-curate-79.py
Run: python3 scripts/bpg-curate-79.py  (from project root)
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
    "ingrafting":               {"status": "names-only"},   # Jas 1:21 "engrafted word"; covered under "word"
    "inhospitableness":         {"status": "names-only"},   # 3 John 9-10; covered under "hospitality"
    "innocency":                {"status": "names-only"},   # Ps 26:6; Dan 6:22; lexical
    "innuendo":                 {"status": "names-only"},   # not a biblical concept; names-only
    "inquest":                  {"status": "names-only"},   # legal; names-only
    "insanity":                 {"status": "names-only"},   # 1 Sam 21:13-15 David feigns madness; covered under "disease"
    "inscriptions":             {"status": "names-only"},   # John 19:19 titulus; archaeological; names-only
    "insincerity":              {"status": "names-only"},   # covered under "hypocrisy"; names-only
    "insinuation":              {"status": "names-only"},   # rhetorical/legal; names-only
    "insomnia":                 {"status": "names-only"},   # Esth 6:1; Dan 6:18; medical; names-only
    "instinct":                 {"status": "names-only"},   # Prov 30; covered under "animals"; names-only
    "instrumentality":          {"status": "names-only"},   # philosophy of means; names-only
    "insurgents":               {"status": "names-only"},   # Judg rebellion context; names-only
    "intemperance":             {"status": "names-only"},   # covered under "drunkenness" and "temperance"
    "interpreter":              {"status": "names-only"},   # Gen 42:23; 1 Cor 14:28; names-only
    "intoxicants":              {"status": "names-only"},   # covered under "wine" and "drunkenness"
    "intoxication":             {"status": "names-only"},   # covered under "drunkenness"
    "intrigue":                 {"status": "names-only"},   # political/court; names-only
    "invective":                {"status": "names-only"},   # rhetorical curse/denunciation; names-only
    "invention":                {"status": "names-only"},   # Eccl 7:29 KJV; names-only
    "investigation":            {"status": "names-only"},   # legal; names-only
    "israelites":               {"status": "names-only"},   # covered under "israel" in Easton; names-only
    "ithrites":                 {"status": "names-only"},   # 2 Sam 23:38; 1 Chr 2:53; minor clan; names-only
    "itinerary":                {"status": "names-only"},   # Num 33; covered under "wanderings"
    # Acts 16:27-34; Philippian jailer; Easton has jailer.json
    "jailer-jailor":            {"status": "redirect-only", "redirect_to": "jailer"},
    "jewels":                   {"status": "names-only"},   # covered under "jewel" in Easton; names-only
    "josedech":                 {"status": "names-only"},   # Ezra 3:2; Hag 1:1 high priest's father; minor
    "judging":                  {"status": "names-only"},   # Matt 7:1-5; covered under "judge" in Easton
    # Acts 25:10; Pilate's judgment hall; Easton has judgment-hall.json
    "judgment-hall":            {"status": "redirect-only", "redirect_to": "judgment-hall"},
    # Rom 14:10; 2 Cor 5:10; Easton has judgment-seat.json
    "judgment-seat":            {"status": "redirect-only", "redirect_to": "judgment-seat"},
    "jury":                     {"status": "names-only"},   # legal; not a biblical institution; names-only
    "kidnapping":               {"status": "names-only"},   # Exod 21:16; Deut 24:7; covered under "law, Mosaic"
    "kidney":                   {"status": "names-only"},   # Lev 3:4; anatomical/sacrificial; names-only
    "killing":                  {"status": "names-only"},   # covered under "murder" in Easton; names-only
    "kine-bovine":              {"status": "names-only"},   # ISBE compound; Gen 41:2-4; covered under "cattle"
    "lachrymatory-tear-bottle": {"status": "names-only"},   # Ps 56:8; archaeological artifact; names-only
    "lama-sabachthani":         {"status": "names-only"},   # Matt 27:46 "My God, my God, why…"; Ps 22:1; names-only
    "lameness":                 {"status": "names-only"},   # Acts 3:2; 14:8; covered under "disease"
    # OT poetry of grief over Jerusalem's fall (587 BC); Easton has lamentations-book-of.json
    "lamentations":             {"status": "redirect-only", "redirect_to": "lamentations-book-of"},
    "lance":                    {"status": "names-only"},   # 1 Kgs 18:28; John 19:34; weapon; names-only
    "landmarks":                {"status": "names-only"},   # Deut 19:14; Prov 22:28; covered under "land"
    "lapidary":                 {"status": "names-only"},   # gem-cutting; cultural; names-only
    "larceny":                  {"status": "names-only"},   # theft; covered under "theft" in Easton; names-only
    "lawsuits":                 {"status": "names-only"},   # 1 Cor 6:1-8; covered under "law" and "courts"
    "laziness":                 {"status": "names-only"},   # Prov 6:6-11; covered under "sloth"
    "leadership":               {"status": "names-only"},   # covered under "rulers" and "government"
    "learning":                 {"status": "names-only"},   # Acts 26:24; covered under "wisdom" and "education"
    "lease":                    {"status": "names-only"},   # legal; OT land tenure; names-only
    "legends-inscriptions":     {"status": "names-only"},   # archaeological context; names-only
    "legislation":              {"status": "names-only"},   # covered under "law" in Easton; names-only
    "legs":                     {"status": "names-only"},   # John 19:31-33; anatomical; names-only
    "lex-talionis":             {"status": "names-only"},   # covered under "eye-for-eye" (stub-needed) and "law, Mosaic"
    "liars":                    {"status": "names-only"},   # Ps 116:11; Rev 21:8; covered under "lying"
    "libyans":                  {"status": "names-only"},   # 2 Chr 12:3; Jer 46:9; covered under "Libya"
    "licentiousness":           {"status": "names-only"},   # Gal 5:19; covered under "fornication"
    # Num 24:6 KJV "lign aloes"; Ps 45:8; Prov 7:17; Easton has lign-aloes.json
    "lign-aloe":                {"status": "redirect-only", "redirect_to": "lign-aloes"},
    "litigation":               {"status": "names-only"},   # legal; 1 Cor 6:1-8; covered under "lawsuits"
    "livery":                   {"status": "names-only"},   # 2 Kgs 25:30; ration/portion; lexical
    "lobbying":                 {"status": "names-only"},   # political; not biblical; names-only
    "lost-sheep":               {"status": "names-only"},   # Matt 18:12-14; Luke 15:4-7; covered under parables
    "lost-the":                 {"status": "names-only"},   # Luke 15; covered under parables
    "lovefeasts":               {"status": "names-only"},   # Jude 12; 2 Pet 2:13; covered under "agape" feast
    "lovers":                   {"status": "names-only"},   # Lam 1:2; Hos 2:7; lexical
    "lunacy":                   {"status": "names-only"},   # Matt 4:24; 17:15 KJV "lunatic"; names-only
    # Dan 1:20; Acts 13:6-8; Easton has magicians.json
    "magician":                 {"status": "redirect-only", "redirect_to": "magicians"},
    "magna-charta":             {"status": "names-only"},   # historical; not biblical; names-only
    "magnanimity":              {"status": "names-only"},   # Phil 4:5; covered under "gentleness"
    "maiden":                   {"status": "names-only"},   # Gen 24:16; lexical; covered under "virgin"
    "majesty":                  {"status": "names-only"},   # Heb 1:3; Ps 104:1; names-only
    "majority-and-minority-reports": {"status": "names-only"},  # Num 13 spies report; names-only
    "malefactors-criminals":    {"status": "names-only"},   # Luke 23:32-33; covered under "thief/criminals"
    "malfeasance-in-office":    {"status": "names-only"},   # legal; names-only
    "malingering":              {"status": "names-only"},   # not biblical; names-only
    # Gen 30:14-16; mandrake as fertility plant; Easton has mandrakes.json
    "mandrake":                 {"status": "redirect-only", "redirect_to": "mandrakes"},
    "manners":                  {"status": "names-only"},   # cultural; covered under "manners and customs"
    "manslaughter":             {"status": "names-only"},   # Num 35:11-28; covered under "cities of refuge"
    "manure":                   {"status": "names-only"},   # Isa 25:10 KJV; Luk 13:8; agricultural; names-only
    "mariners-sailors":         {"status": "names-only"},   # Jon 1:5; Acts 27:27; covered under "ships"
    "market":                   {"status": "names-only"},   # Mark 12:38; Acts 16:19; covered under "trade"
    "masking":                  {"status": "names-only"},   # cultural disguise; names-only
    "massacre":                 {"status": "names-only"},   # specific massacres covered under narratives; names-only
    "master-workman":           {"status": "names-only"},   # Exod 31:1-6; 1 Kgs 7:14; covered under "arts"
    "materialism":              {"status": "names-only"},   # philosophical; not biblical topic; names-only
    "mechanic":                 {"status": "names-only"},   # cultural; names-only
    "meddling":                 {"status": "names-only"},   # Prov 26:17; 1 Pet 4:15; names-only
    "mediation":                {"status": "names-only"},   # 1 Tim 2:5; covered under "mediator" in Easton
    # Gen 14:18-20; Ps 110:4; Heb 5-7 high priest; variant spelling of Melchizedek
    "melchesedec":              {"status": "redirect-only", "redirect_to": "melchizedek"},
    # Acts 28:1-10; Paul's shipwreck island; Easton has melita.json
    "melita-malta":             {"status": "redirect-only", "redirect_to": "melita"},
    "melon":                    {"status": "names-only"},   # Num 11:5; botanical; names-only
    "memorial":                 {"status": "names-only"},   # Josh 4:7; Exod 12:14; covered under "feasts"
    "menses":                   {"status": "names-only"},   # Lev 15:19-24; covered under "unclean"
    "menstruation":             {"status": "names-only"},   # Lev 15:19-24; covered under "unclean"
    "mercenaries":              {"status": "names-only"},   # 2 Sam 10:6; 2 Chr 25:6; names-only
    "merit":                    {"status": "names-only"},   # Phil 3:9; covered under "works" and "grace"
    "metaphor":                 {"status": "names-only"},   # rhetorical; not a biblical topic per se
    # Num 25; Judg 6-8; Easton has midianite.json
    "midianites":               {"status": "redirect-only", "redirect_to": "midianite"},
    "midwifery":                {"status": "names-only"},   # Gen 35:17; Exod 1:15-21; names-only
    "military-instruction":     {"status": "names-only"},   # cultural; names-only
    "minister-civil":           {"status": "names-only"},   # Rom 13:1-7; covered under "government"
    "minority-report":          {"status": "names-only"},   # Num 13; names-only
    "minors":                   {"status": "names-only"},   # legal; names-only
    "miscegenation":            {"status": "names-only"},   # Ezra 9-10; Deut 7:3; covered under "marriage"
    "miser":                    {"status": "names-only"},   # Prov 11:24; 28:22; covered under "covetousness"
    "misjudgment":              {"status": "names-only"},   # names-only
    # Mark 12:42 "two mites" (lepta); Easton has mite.json
    "mite-a-lepta":             {"status": "redirect-only", "redirect_to": "mite"},
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
    print(f'BPG Curation C79: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
