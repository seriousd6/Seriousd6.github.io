"""
BPG Curation — Batch C55: marsh → midianitish-woman (gaps 5599–5698)
Gaps reviewed: 100 (score-5 isbe-scholarly M entries — marsh, Matthew, meal/measure
compounds, Medes/Mediator, Megiddo/Melchizedek, Mene-Mene-Tekel, mercy compounds,
Merom, Meshech, Micah disambiguations, Midian)

Redirects: massah-and-meribah→massah; matthew-the-gospel-of→matthew-gospel-according-to;
meal-offering→meat-offering; meals-meal-time→meals; measure/measures→measure;
medaba→medeba; medes→mede; mediation/mediator→mediator; megiddo/megiddon→megiddo;
mehetabel/mehetabeel→mehetabel; melchizedek/melchisedec→melchizedek;
mene-mene-tekel-upharsin→mene; meonenim-oak-of→meonenim;
merchant/merchantman→merchant; mercury/mercurius→mercurius;
mercy-seat-the→mercy-seat; mercy/merciful→mercy;
meribath-kadesh→meribah; merom-waters-of→merom; mesech→meshech;
meshech/mesech→meshech; methushael→methusael;
micah-1/2/micha/micheas→micah; michmas→michmash; midian/midianites→midian.
0 stub-needed; 28 redirects; 72 names-only.

Script: scripts/bpg-curate-55.py
Run: python3 scripts/bpg-curate-55.py  (from project root)
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
    "marsh":                     {"status": "names-only"},   # Ezek 47:11; Job 8:11; no dedicated Easton article
    "marshal":                   {"status": "names-only"},   # Jer 51:27 KJV; military official; lexical
    "mart":                      {"status": "names-only"},   # Isa 23:3 "mart of nations"; covered under merchant; names-only
    "marvel;-marvelous":         {"status": "names-only"},   # ISBE compound; Exod 34:10; John 9:30; lexical
    "mary-the-passing-of":       {"status": "names-only"},   # apocryphal "Dormition of Mary"; extracanonical
    "masaloth":                  {"status": "names-only"},   # 1 Macc 9:2 variant place; apocryphal
    "masias":                    {"status": "names-only"},   # 1 Esd variant; apocryphal
    "masman":                    {"status": "names-only"},   # 1 Esd 9:34 variant; apocryphal
    "maspha":                    {"status": "names-only"},   # Greek apocryphal variant of Mizpah; names-only
    "massacre-of-the-innocents": {"status": "names-only"},   # Matt 2:16-18 Herod; names-only
    # ISBE compound; Exod 17:7; Num 20:13; Easton has massah.json
    "massah-and-meribah":        {"status": "redirect-only", "redirect_to": "massah"},
    "massias":                   {"status": "names-only"},   # 1 Esd 9:22 variant; apocryphal
    "mast":                      {"status": "names-only"},   # Ezek 27:5; Prov 23:34; nautical; lexical
    "master":                    {"status": "names-only"},   # Matt 23:8; John 13:13 KJV; lexical
    "mastery":                   {"status": "names-only"},   # 1 Cor 9:25 KJV; lexical
    "mastic-mastick":            {"status": "names-only"},   # resinous plant; Susanna 54 apocryphal; botanical
    "mathanias":                 {"status": "names-only"},   # 1 Esd variant; apocryphal
    "mathelas":                  {"status": "names-only"},   # 1 Esd 9:18 variant; apocryphal
    "matrites":                  {"status": "names-only"},   # 1 Sam 10:21; Benjaminite clan; minor
    "mattattah":                 {"status": "names-only"},   # Ezra 10:33; minor OT figure
    "matter":                    {"status": "names-only"},   # lexical
    # ISBE compound; Easton has matthew-gospel-according-to.json
    "matthew-the-gospel-of":     {"status": "redirect-only", "redirect_to": "matthew-gospel-according-to"},
    "maw":                       {"status": "names-only"},   # Deut 18:3 KJV "maw" = stomach; lexical
    "mazitias":                  {"status": "names-only"},   # 1 Esd 9:35 variant; apocryphal
    "mazzaloth":                 {"status": "names-only"},   # 2 Kgs 23:5 KJV "planets/constellations"; lexical
    "mazzebah":                  {"status": "names-only"},   # standing pillar/stele; Exod 23:24; no dedicated Easton slug
    "meal":                      {"status": "names-only"},   # flour meal (Num 5:15); lexical
    # KJV for grain/cereal offering; Easton has meat-offering.json
    "meal-offering":             {"status": "redirect-only", "redirect_to": "meat-offering"},
    # ISBE compound; Ruth 2:14; John 21:12; Easton has meals.json
    "meals-meal-time":           {"status": "redirect-only", "redirect_to": "meals"},
    "mean":                      {"status": "names-only"},   # lexical
    "meani":                     {"status": "names-only"},   # 1 Esd 9:34 variant; apocryphal
    # ISBE compound; various weights and measures; Easton has measure.json
    "measure;-measures":         {"status": "redirect-only", "redirect_to": "measure"},
    "measuring-line":            {"status": "names-only"},   # Jer 31:39; Zech 2:1; names-only
    "measuring-reed":            {"status": "names-only"},   # Ezek 40:3; Rev 11:1; names-only
    "mecherathite":              {"status": "names-only"},   # 1 Chr 11:36; minor warrior's epithet
    "meconah":                   {"status": "names-only"},   # Neh 11:28; Judah town; names-only
    # Num 21:30; variant of Medeba; Easton has medeba.json
    "medaba":                    {"status": "redirect-only", "redirect_to": "medeba"},
    # ISBE plural; Isa 13:17; Easton has mede.json (the Medes)
    "medes":                     {"status": "redirect-only", "redirect_to": "mede"},
    "median":                    {"status": "names-only"},   # Esth 1:19 "law of Medes and Persians"; covered under mede
    # ISBE compound; 1 Tim 2:5; Heb 9:15; Easton has mediator.json
    "mediation;-mediator":       {"status": "redirect-only", "redirect_to": "mediator"},
    "meditation":                {"status": "names-only"},   # Ps 19:14; 1 Tim 4:15; names-only
    "mediterranean-sea":         {"status": "names-only"},   # ISBE; "Great Sea"; no dedicated Easton article
    "meeda":                     {"status": "names-only"},   # 1 Esd 5:32 variant; apocryphal
    "meedda":                    {"status": "names-only"},   # 1 Esd 5:32 variant; apocryphal
    "meet":                      {"status": "names-only"},   # lexical
    # ISBE compound; Josh 12:21; Zech 12:11; Easton has megiddo.json
    "megiddo;-megiddon":         {"status": "redirect-only", "redirect_to": "megiddo"},
    # ISBE compound; Neh 6:10; Gen 36:39; Easton has mehetabel.json
    "mehetabel;-mehetabeel":     {"status": "redirect-only", "redirect_to": "mehetabel"},
    "meholathite":               {"status": "names-only"},   # 1 Sam 18:19; 2 Sam 21:8 Adriel's epithet; names-only
    "melchias":                  {"status": "names-only"},   # 1 Esd 9:26 variant; apocryphal
    "melchiel":                  {"status": "names-only"},   # Jdt 6:15 apocryphal figure; names-only
    # ISBE compound; Gen 14:18; Heb 7:1; Easton has melchizedek.json
    "melchizedek;-melchisedec":  {"status": "redirect-only", "redirect_to": "melchizedek"},
    "melody":                    {"status": "names-only"},   # Amos 5:23; Eph 5:19; lexical
    "mem":                       {"status": "names-only"},   # Hebrew letter (13th); Ps 119:97-104; lexical
    "member":                    {"status": "names-only"},   # 1 Cor 12:12-27; Rom 12:5; lexical
    "memeroth":                  {"status": "names-only"},   # Ezra 8:33 variant of Meremoth; minor figure
    "memmius-quintus":           {"status": "names-only"},   # 2 Macc 11:34 Roman envoy; apocryphal
    "memorial;-memory":          {"status": "names-only"},   # ISBE compound; Exod 3:15; Matt 26:13; lexical
    # ISBE; Dan 5:25; Easton has mene.json
    "mene-mene-tekel-upharsin":  {"status": "redirect-only", "redirect_to": "mene"},
    "menelaus":                  {"status": "names-only"},   # 2 Macc 4:23-50 Hellenistic high priest; apocryphal
    "menestheus":                {"status": "names-only"},   # 2 Macc 4:21 apocryphal figure; names-only
    "menuhah":                   {"status": "names-only"},   # Judg 20:43 KJV "rest/Menuha"; names-only
    "menuhoth":                  {"status": "names-only"},   # 1 Chr 2:52 KJV; Judah clan; names-only
    # ISBE; Judg 9:37 "diviners' oak"; Easton has meonenim.json
    "meonenim-oak-of":           {"status": "redirect-only", "redirect_to": "meonenim"},
    "meran":                     {"status": "names-only"},   # 1 Esd 5:37 variant; apocryphal
    "merchandise":               {"status": "names-only"},   # Prov 3:14; Ezek 27:16; covered under merchant
    # ISBE compound; Gen 37:28; Rev 18:11; Easton has merchant.json
    "merchant;-merchantman":     {"status": "redirect-only", "redirect_to": "merchant"},
    # ISBE compound; Acts 14:12; Easton has mercurius.json
    "mercury;-mercurius":        {"status": "redirect-only", "redirect_to": "mercurius"},
    # ISBE compound; Exod 25:17-22; Lev 16:2; Easton has mercy-seat.json
    "mercy-seat-the":            {"status": "redirect-only", "redirect_to": "mercy-seat"},
    # ISBE compound; Ps 136; Matt 5:7; Easton has mercy.json
    "mercy;-merciful":           {"status": "redirect-only", "redirect_to": "mercy"},
    # ISBE compound; Num 27:14; Deut 32:51; Easton has meribah.json
    "meribath-kadesh;-meriboth-kadesh": {"status": "redirect-only", "redirect_to": "meribah"},
    # ISBE; Josh 11:5,7; battle site; Easton has merom.json
    "merom-waters-of":           {"status": "redirect-only", "redirect_to": "merom"},
    "merran":                    {"status": "names-only"},   # 1 Esd 5:37 variant; apocryphal
    "meruth":                    {"status": "names-only"},   # 1 Esd 5:32 variant; apocryphal
    "mesaloth":                  {"status": "names-only"},   # 1 Macc 9:2 variant; apocryphal place
    # ISBE variant; Ps 120:5; Easton has meshech.json
    "mesech":                    {"status": "redirect-only", "redirect_to": "meshech"},
    # ISBE compound; Gen 10:2; Ezek 38:2; Easton has meshech.json
    "meshech;-mesech":           {"status": "redirect-only", "redirect_to": "meshech"},
    "meshezabel":                {"status": "names-only"},   # Neh 3:4; 10:21; minor figure
    "meshobab":                  {"status": "names-only"},   # 1 Chr 4:34; minor Simeonite figure
    "metal":                     {"status": "names-only"},   # ISBE scholarly; ancient metalwork; names-only
    "metal-working":             {"status": "names-only"},   # ISBE scholarly; names-only
    "metallurgy":                {"status": "names-only"},   # ISBE scholarly; names-only
    "mete":                      {"status": "names-only"},   # Matt 7:2 KJV "mete/measure"; lexical
    "meterus":                   {"status": "names-only"},   # 1 Esd 5:33 variant; apocryphal
    "meteyard":                  {"status": "names-only"},   # Lev 19:35 KJV "meteyard" = linear measure; archaic/lexical
    # ISBE; Gen 4:18; Easton has methusael.json
    "methushael":                {"status": "redirect-only", "redirect_to": "methusael"},
    "meuzal":                    {"status": "names-only"},   # Ezek 27:19 KJV variant of Uzal; names-only
    "mezarim":                   {"status": "names-only"},   # Job 37:9 KJV "scatterers" (north wind); lexical
    "mezobaite":                 {"status": "names-only"},   # 1 Chr 11:47; minor warrior's epithet
    "mica":                      {"status": "names-only"},   # 1 Chr 9:15; Neh 11:17; minor Levite; names-only
    # ISBE disambiguation; Judg 17-18; Easton has micah.json
    "micah-1":                   {"status": "redirect-only", "redirect_to": "micah"},
    # ISBE disambiguation; Micah the prophet; Easton has micah.json
    "micah-2":                   {"status": "redirect-only", "redirect_to": "micah"},
    "mice":                      {"status": "names-only"},   # 1 Sam 6:4-5 five golden mice; names-only
    # ISBE compound; 2 Sam 9:12; Neh 11:17; Easton has micah.json
    "micha;-michah":             {"status": "redirect-only", "redirect_to": "micah"},
    # ISBE compound; Greek form of Micah; Easton has micah.json
    "micheas;-michaeas":         {"status": "redirect-only", "redirect_to": "micah"},
    # variant of Michmash; Neh 11:31; Easton has michmash.json
    "michmas":                   {"status": "redirect-only", "redirect_to": "michmash"},
    "micron":                    {"status": "names-only"},   # apocryphal/minor variant; names-only
    "midday":                    {"status": "names-only"},   # Neh 8:3; Acts 26:13; lexical
    "middle-wall":               {"status": "names-only"},   # Eph 2:14 "middle wall of partition"; names-only
    # ISBE compound; Gen 25:2; Num 31; Easton has midian.json
    "midian;-midianites":        {"status": "redirect-only", "redirect_to": "midian"},
    "midianitish-woman":         {"status": "names-only"},   # Num 25:6-15 Cozbi; covered under phinehas/num 25
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
    print(f'BPG Curation C55: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
