"""
BPG Curation — Batch C75: zela-zelah → beth-joab (gaps 7574–7678)
Gaps reviewed: 105 (31 score-5 isbe-scholarly Z entries + 74 score-3 concept-no-article A–B entries)

Score-3 concept-no-article entries: predominantly legal concepts, minor persons,
archaic KJV terms, and non-biblical topics. Very conservative posture — mostly names-only.
0 stub-needed; 13 redirect-only; 92 names-only.

Z redirects: zephaniah-book-of→zephaniah; zidon;-zidonians→sidon;
zimri-1/2→zimri; ziph-1/2→ziph.
Score-3 redirects: anathema-maran-atha→anathema; appii-forum→appii-forum;
aquila-and-priscilla→aquila; archelaus-archaelaus→archelaus; armor→armour;
bartimeus-bartimaeus→bartimaeus; bath-sheba-bathsheba→bath-sheba.

Script: scripts/bpg-curate-75.py
Run: python3 scripts/bpg-curate-75.py  (from project root)
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
    # --- score-5 isbe-scholarly Z entries ---
    "zela-zelah":               {"status": "names-only"},   # Josh 18:28; Benjamin border town; minor place
    "zemirah":                  {"status": "names-only"},   # 1 Chr 7:8 Benjaminite; minor
    "zend-avesta":              {"status": "names-only"},   # Zoroastrian scripture; not biblical content
    "zephaniah-apocalypse-of":  {"status": "names-only"},   # pseudepigraphical; apocryphal; too specialized
    # ISBE; Zeph 1-3; Easton has zephaniah.json (prophet and book)
    "zephaniah-book-of":        {"status": "redirect-only", "redirect_to": "zephaniah"},
    "zephathah-valley-of":      {"status": "names-only"},   # 2 Chr 14:10 Asa's battle site; minor place
    "zephi;-zepho":             {"status": "names-only"},   # ISBE compound; Gen 36:11 Edomite chief; minor
    "zephonites":               {"status": "names-only"},   # Num 26:15 Gad clan; minor
    "zerah-the-ethiopian":      {"status": "names-only"},   # 2 Chr 14:9; covered under "Asa" and "Ethiopia"
    "zerahites":                {"status": "names-only"},   # Num 26:13,20 clan; minor
    "zeredah;-zeredath;-zeredatha;-zererah;-zererath": {"status": "names-only"},  # ISBE compound; minor places
    "zereth-shahar":            {"status": "names-only"},   # Josh 13:19 Reuben border; minor place
    "zeus":                     {"status": "names-only"},   # Acts 14:12-13; Greek deity; covered under "Jupiter"
    # ISBE compound; KJV spelling of Sidon; Easton has sidon.json
    "zidon;-zidonians":         {"status": "redirect-only", "redirect_to": "sidon"},
    "zillethai":                {"status": "names-only"},   # 1 Chr 8:20; 12:20; minor persons
    # ISBE disambiguation; 1 Kgs 16:9-20; Easton has zimri.json
    "zimri-1":                  {"status": "redirect-only", "redirect_to": "zimri"},
    # ISBE disambiguation; Num 25:14; Easton has zimri.json
    "zimri-2":                  {"status": "redirect-only", "redirect_to": "zimri"},
    # ISBE disambiguation; Josh 15:55 Judah town; Easton has ziph.json
    "ziph-1":                   {"status": "redirect-only", "redirect_to": "ziph"},
    # ISBE disambiguation; Josh 15:24 Judah south; Easton has ziph.json
    "ziph-2":                   {"status": "redirect-only", "redirect_to": "ziph"},
    "ziphims":                  {"status": "names-only"},   # Ps 54 title variant of Ziphites; names-only
    "ziphites":                 {"status": "names-only"},   # 1 Sam 23:19; 26:1; covered under "Ziph"
    "ziv":                      {"status": "names-only"},   # 1 Kgs 6:1,37 Hebrew month; covered under "calendar"
    "ziz-ascent-of":            {"status": "names-only"},   # 2 Chr 20:16 pass near En-gedi; minor place
    "zoheleth-the-stone-of":    {"status": "names-only"},   # 1 Kgs 1:9 near En-rogel; minor
    "zoology":                  {"status": "names-only"},   # ISBE scholarly; too broad; not a BPG article
    "zophim-the-field-of":      {"status": "names-only"},   # Num 23:14 Balak/Balaam; minor place
    "zorathites":               {"status": "names-only"},   # 1 Chr 4:2 Judah clan; minor
    "zorites":                  {"status": "names-only"},   # 1 Chr 2:54 Judah clan; minor
    "zoroastrianism":           {"status": "names-only"},   # Persian religion; post-exilic context; not biblical
    "zorzelleus":               {"status": "names-only"},   # apocryphal (1 Esd 8:62); minor
    "zuzim":                    {"status": "names-only"},   # Gen 14:5 pre-Israelite people; brief
    # --- score-3 concept-no-article A–B entries ---
    "abetting":                 {"status": "names-only"},   # legal concept; not directly biblical
    "abortion":                 {"status": "names-only"},   # not directly addressed in canonical Bible; too specialized
    "abstemiousness":           {"status": "names-only"},   # 1 Tim 3:3; covered under "temperance"; lexical
    "accessory":                {"status": "names-only"},   # legal concept; not biblical topic
    "accomplice":               {"status": "names-only"},   # legal concept; not biblical topic
    "acrostic-poetry":          {"status": "names-only"},   # Ps 119; Lam 1-4; covered under "poetry"
    "actions-at-law":           {"status": "names-only"},   # legal concept; not biblical topic
    "adjudication-at-law":      {"status": "names-only"},   # legal concept; not biblical topic
    "admonition":               {"status": "names-only"},   # Rom 15:14; Tit 3:10; covered under "exhortation"
    "advice":                   {"status": "names-only"},   # lexical
    "afflicted":                {"status": "names-only"},   # lexical; covered under "afflictions" in Easton
    "aged":                     {"status": "names-only"},   # lexical
    "agency-free-moral":        {"status": "names-only"},   # philosophical; too academic for BPG
    "ahia":                     {"status": "names-only"},   # apocryphal variant of Ahijah; minor
    "alloy-of-metals":          {"status": "names-only"},   # metallurgy; too technical; names-only
    "alpheus-alphaeus":         {"status": "names-only"},   # ISBE compound; Mark 2:14; minor; no Easton slug found
    "amanuensis":               {"status": "names-only"},   # Rom 16:22 Tertius; too academic; names-only
    "amnesty":                  {"status": "names-only"},   # legal concept; names-only
    "anarchy":                  {"status": "names-only"},   # political; not biblical topic
    # 1 Cor 16:22; "Anathema Maranatha"; Easton has anathema.json
    "anathema-maran-atha":      {"status": "redirect-only", "redirect_to": "anathema"},
    "anatomy":                  {"status": "names-only"},   # general medicine; names-only
    "angel-of-the-churches":    {"status": "names-only"},   # Rev 2-3; covered under "angel" and "Revelation"
    "anointing-oil":            {"status": "names-only"},   # Exod 30:23-25; covered under "anointing" in Easton
    "anxiety":                  {"status": "names-only"},   # Matt 6:25-34; covered under "care" and "trust"
    "apostrophe":               {"status": "names-only"},   # rhetorical device; too literary/academic
    # Acts 28:15 "Appii Forum"; Easton has appii-forum.json
    "appii-forum":              {"status": "redirect-only", "redirect_to": "appii-forum"},
    # Acts 18:2-3; 26; Rom 16:3; Easton has aquila.json
    "aquila-and-priscilla":     {"status": "redirect-only", "redirect_to": "aquila"},
    "arbitration":              {"status": "names-only"},   # legal; 1 Cor 6:1-6; names-only
    # Matt 2:22 Herod's son; Easton has archelaus.json
    "archelaus-archaelaus":     {"status": "redirect-only", "redirect_to": "archelaus"},
    "arkites":                  {"status": "names-only"},   # Gen 10:17 Canaanite clan; minor
    # military equipment; Easton has armour.json (British spelling used)
    "armor":                    {"status": "redirect-only", "redirect_to": "armour"},
    "arms":                     {"status": "names-only"},   # weapons/military; covered under "armour" generally
    "arphad":                   {"status": "names-only"},   # 2 Kgs 18:34 Aram city; covered under "Syria"
    "arrest":                   {"status": "names-only"},   # legal; names-only
    "arrogance":                {"status": "names-only"},   # Ps 31:18; covered under "pride"
    "arson":                    {"status": "names-only"},   # legal; not biblical topic
    "arvadites":                {"status": "names-only"},   # Gen 10:18 Canaanite clan; minor
    "asceticism":               {"status": "names-only"},   # Col 2:23; covered under "fasting" and "self-denial"
    "asphaltum":                {"status": "names-only"},   # Gen 11:3 "slime/bitumen"; covered under "slime"
    "assault-and-battery":      {"status": "names-only"},   # legal; Exod 21:12-27; names-only
    "ataroth-adar":             {"status": "names-only"},   # Josh 16:5; 18:13 Ephraim border; minor place
    "atoms-of-matter":          {"status": "names-only"},   # not biblical; philosophical; names-only
    "atrophy":                  {"status": "names-only"},   # medical; not biblical topic
    "attorney":                 {"status": "names-only"},   # legal; not biblical topic
    "attributes-of-god":        {"status": "names-only"},   # covered under "god" in Easton; score-3; names-only
    "avarice":                  {"status": "names-only"},   # Luk 12:15; covered under "covetousness"
    "ax":                       {"status": "names-only"},   # Deut 19:5; Jer 46:22; tool; covered under "tools"
    "baal-gur":                 {"status": "names-only"},   # variant/minor place; names-only
    "babes":                    {"status": "names-only"},   # Matt 11:25; lexical
    "backbiting":               {"status": "names-only"},   # Ps 15:3; Rom 1:30; covered under "slander"
    "bad-company":              {"status": "names-only"},   # 1 Cor 15:33; lexical
    "bagpipe":                  {"status": "names-only"},   # Dan 3:5 KJV; covered under "music"
    "bail":                     {"status": "names-only"},   # legal; not biblical topic
    "baker":                    {"status": "names-only"},   # Gen 40:1-22; Pharaoh's baker; covered under "bread"
    "barrenness":               {"status": "names-only"},   # Gen 11:30; covered under "Sarah" and "Hannah"
    "barter":                   {"status": "names-only"},   # commercial; covered under "trade"
    # Mark 10:46 blind man healed; Easton has bartimaeus.json
    "bartimeus-bartimaeus":     {"status": "redirect-only", "redirect_to": "bartimaeus"},
    # 2 Sam 11; Uriah's wife; Easton has bath-sheba.json
    "bath-sheba-bathsheba":     {"status": "redirect-only", "redirect_to": "bath-sheba"},
    "bathing":                  {"status": "names-only"},   # Exod 2:5; Lev 15:5; covered under "washing"
    "battery":                  {"status": "names-only"},   # legal; names-only
    "battle-ax":                {"status": "names-only"},   # Jer 51:20; weapon; covered under "armour/war"
    "battlements":              {"status": "names-only"},   # Deut 22:8; architectural; brief
    "beasts":                   {"status": "names-only"},   # Rev 13; Dan 7; covered under "animals"
    "beaten-work":              {"status": "names-only"},   # Exod 25:18 KJV; archaic; brief
    "beggars":                  {"status": "names-only"},   # Ps 109:10; Luke 16:20; covered under "poor"
    "believer":                 {"status": "names-only"},   # lexical; covered under "faith"
    "believing":                {"status": "names-only"},   # lexical; covered under "faith"
    "ben-dekar-r.-v.":          {"status": "names-only"},   # 1 Kgs 4:9 RV officer of Solomon; minor
    "ben-geber-r.-v.":          {"status": "names-only"},   # 1 Kgs 4:13 RV officer; minor
    "ben-hur-r.-v.":            {"status": "names-only"},   # 1 Kgs 4:8 RV officer; minor
    "bequests":                 {"status": "names-only"},   # legal; names-only
    "beth-el-aphrah-r.-v.-aphrah-a.-v.": {"status": "names-only"},  # Mic 1:10; minor place
    "beth-hanan":               {"status": "names-only"},   # 1 Kgs 4:9 Solomon's district; minor place
    "beth-joab":                {"status": "names-only"},   # 1 Chr 2:54; minor clan/place
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
    print(f'BPG Curation C75: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
