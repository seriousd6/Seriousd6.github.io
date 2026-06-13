"""
BPG Curation — Batch C45: gileadites → guide (gaps 4399–4498)
Gaps reviewed: 100 (score-5 isbe-scholarly G entries — Gilead demonyms, glass/glow,
god-compound articles, goshen variants, gospels, greece variants, grave/gravel,
grecians, greek-language/versions, grief range)

Heavy redirect batch: many ISBE disambiguation pairs (gomer-1/2, goshen-1/2,
grave-1/2), compound articles (greece;-graecia, grecians;-greeks), and
lexical-to-canonical redirects (grapes→grape, grate;-grating→grate,
glad-tidings→gospel, godliness;-godly→godliness, goyim→gentiles).
God-compound articles (god-image-of, god-the-father, etc.) are names-only at
score-5 — covered in canonical god.json and godhead.json.
0 stub-needed; 29 redirects; 71 names-only.

Script: scripts/bpg-curate-45.py
Run: python3 scripts/bpg-curate-45.py  (from project root)
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
    # Num 26:29; Judg 5:17; demonym from Gilead; Easton has gilead.json
    "gileadites":                  {"status": "redirect-only", "redirect_to": "gilead"},
    # Ahithophel the Gilonite (2 Sam 15:12); demonym from Giloh; Easton has giloh.json
    "gilonite":                    {"status": "redirect-only", "redirect_to": "giloh"},
    "gimel":                       {"status": "names-only"},   # Hebrew letter (3rd); Ps 119:17-24; lexical
    "ginnethoi;-ginnethon":        {"status": "names-only"},   # ISBE combined; Neh 10:6; 12:4,16; minor Levite names
    "girl":                        {"status": "names-only"},   # lexical; Joel 3:3; Zech 8:5
    "girzites":                    {"status": "names-only"},   # 1 Sam 27:8 semi-nomadic group; minor tribal reference
    "gishpa":                      {"status": "names-only"},   # Neh 11:21; temple servant; minor OT figure
    "give":                        {"status": "names-only"},   # lexical; "God so loved he gave" (John 3:16)
    "gizrites":                    {"status": "names-only"},   # variant of Girzites (1 Sam 27:8); names-only
    # Luke 1:19; 2:10; Acts 13:32; KJV "glad tidings" = euangelion; Easton has gospel.json
    "glad-tidings":                {"status": "redirect-only", "redirect_to": "gospel"},
    "glass-sea-of":                {"status": "names-only"},   # Rev 4:6; 15:2; eschatological vision element; brief
    "glistering":                  {"status": "names-only"},   # 1 Chr 29:2; Luke 9:29 KJV; lexical
    "glitter;-glittering":         {"status": "names-only"},   # ISBE compound; Deut 32:41 "glittering sword"; KJV/lexical
    "glorious":                    {"status": "names-only"},   # lexical; covered under glory.json
    "glowing-sand":                {"status": "names-only"},   # ISBE; Isa 35:7 "parched ground/mirage" (sharab); brief
    # Deut 21:20; Prov 23:21; Matt 11:19; Easton has glutton.json
    "glutton;-gluttonous":         {"status": "redirect-only", "redirect_to": "glutton"},
    "gnosticism":                  {"status": "names-only"},   # ISBE; early heresy; score-5 → names-only
    "go":                          {"status": "names-only"},   # lexical
    # Jer 31:39; Jerusalem boundary point; Easton has goath.json
    "goah;-goath":                 {"status": "redirect-only", "redirect_to": "goath"},
    # Exod 26:7; tabernacle curtain material; Easton has goat.json (covers goat's hair)
    "goats-hair":                  {"status": "redirect-only", "redirect_to": "goat"},
    "goatskins":                   {"status": "names-only"},   # Heb 11:37; wandering in goatskins; cultural
    "god-children-of":             {"status": "names-only"},   # John 1:12; 1 John 3:1-2; covered under adoption/salvation
    "god-image-of":                {"status": "names-only"},   # Gen 1:26-27; Col 1:15; covered under god.json/godhead.json
    "god-names-of":                {"status": "names-only"},   # divine titles; covered under god.json and individual name articles
    "god-son-sons-of":             {"status": "names-only"},   # ISBE compound; covered under god.json
    "god-strange":                 {"status": "names-only"},   # "strange gods" (Deut 32:16); covered under idolatry
    "god-the-father":              {"status": "names-only"},   # ISBE compound; covered under god.json and godhead.json
    "god-the-unknown":             {"status": "names-only"},   # Acts 17:23 Areopagus speech; brief; contextual
    "goddess":                     {"status": "names-only"},   # covered under individual deities (Asherah, Ashtoreth) in Easton
    "godless":                     {"status": "names-only"},   # lexical; Job 8:13; 2 Pet 2:5 KJV "ungodly"
    # 1 Tim 3:16; 4:7-8; 6:6; Tit 1:1; Easton has godliness.json
    "godliness;-godly":            {"status": "redirect-only", "redirect_to": "godliness"},
    "gods":                        {"status": "names-only"},   # lexical/plural; covered under god.json and idolatry
    "godspeed":                    {"status": "names-only"},   # 2 John 10-11 KJV; greeting formula; lexical
    "goiim":                       {"status": "names-only"},   # variant of goyim; Gen 14:1 king Tidal; names-only
    "going;-goings":               {"status": "names-only"},   # ISBE compound; lexical
    # Deut 4:43; Josh 20:8; Golan city of refuge; Easton has golan.json
    "golan;-gaulonitis":           {"status": "redirect-only", "redirect_to": "golan"},
    "golden-city":                 {"status": "names-only"},   # Isa 14:4 KJV "oppressor" (NRSV; LXX); Babylon ref; lexical
    "golden-number":               {"status": "names-only"},   # ISBE; Metonic cycle calendar term; technical; names-only
    # ISBE disambiguation; Gen 10:2-3 son of Japheth; Easton has gomer.json
    "gomer-1":                     {"status": "redirect-only", "redirect_to": "gomer"},
    # ISBE disambiguation; Hos 1:3 Hosea's wife; Easton has gomer.json
    "gomer-2":                     {"status": "redirect-only", "redirect_to": "gomer"},
    "good":                        {"status": "names-only"},   # lexical; "God saw that it was good" (Gen 1)
    "good-chief":                  {"status": "names-only"},   # ISBE; "the chief good" / summum bonum; philosophical; names-only
    "goodliness":                  {"status": "names-only"},   # Isa 40:6; 1 Pet 1:24; lexical
    "goodly":                      {"status": "names-only"},   # KJV "beautiful/fine"; lexical
    "goodman":                     {"status": "names-only"},   # KJV "householder/master" (Matt 20:11; 24:43); lexical
    "goods":                       {"status": "names-only"},   # lexical; possessions
    # Gen 6:14 ark wood; Easton has gopher.json
    "gopher-wood":                 {"status": "redirect-only", "redirect_to": "gopher"},
    "gore":                        {"status": "names-only"},   # Exod 21:28-36 goring ox law; legal/cultural; brief
    "gorgeous;-gorgeously":        {"status": "names-only"},   # ISBE compound; Luke 7:25; 23:11 KJV; lexical
    "gorget":                      {"status": "names-only"},   # KJV archaic neck armor; lexical
    "gorgias":                     {"status": "names-only"},   # 1 Macc 3:38; Seleucid general; apocryphal
    "gortyna":                     {"status": "names-only"},   # 1 Macc 15:23; Cretan city; apocryphal
    # ISBE disambiguation; Exod 8:22; region of Egypt; Easton has goshen.json
    "goshen-1":                    {"status": "redirect-only", "redirect_to": "goshen"},
    # ISBE disambiguation; Josh 10:41 Judah region; Easton has goshen.json
    "goshen-2":                    {"status": "redirect-only", "redirect_to": "goshen"},
    "gospel-according-to-the-hebrews": {"status": "names-only"},  # apocryphal/Jewish-Christian gospel; extracanonical
    "gospels-of-the-childhood":    {"status": "names-only"},   # Infancy Gospel of Thomas etc.; apocryphal
    "gospels-spurious":            {"status": "names-only"},   # ISBE; apocryphal gospels collection; extracanonical
    # ISBE scholarly; Matt/Mark/Luke synoptic problem; Easton has gospels.json
    "gospels-the-synoptic":        {"status": "redirect-only", "redirect_to": "gospels"},
    "gothic-version":              {"status": "names-only"},   # ISBE; Wulfila's 4th-c. Gothic Bible; scholarly
    "gotholias":                   {"status": "names-only"},   # 1 Esd 8:33 variant; apocryphal
    "gothoniel":                   {"status": "names-only"},   # Jdt 6:15; apocryphal figure
    # 2 Kgs 4:39 wild gourds (colocynth); Easton has gourd.json (Jonah 4:6-10)
    "gourd-wild":                  {"status": "redirect-only", "redirect_to": "gourd"},
    "government":                  {"status": "names-only"},   # ISBE; Isa 9:6; general; covered under government-of-god.json
    # Hebrew "goyim" = nations/Gentiles (Gen 14:1; Isa 9:1); Easton has gentiles.json
    "goyim":                       {"status": "redirect-only", "redirect_to": "gentiles"},
    "graba":                       {"status": "names-only"},   # 1 Esd variant place; apocryphal
    "gracious":                    {"status": "names-only"},   # lexical; Exod 22:27; "gracious and merciful" (Neh 9:17)
    # ISBE variant name for Greece; Easton has greece.json
    "graecia":                     {"status": "redirect-only", "redirect_to": "greece"},
    # Jer 50:26; storage pit; Easton has garner.json (Matt 3:12; Luke 3:17)
    "granary":                     {"status": "redirect-only", "redirect_to": "garner"},
    # Num 13:23; Song 1:14; Easton has grape.json
    "grapes":                      {"status": "redirect-only", "redirect_to": "grape"},
    # Isa 5:2-4; Jer 2:21; degenerate vines; Easton has grape.json
    "grapes-wild":                 {"status": "redirect-only", "redirect_to": "grape"},
    "grasp":                       {"status": "names-only"},   # lexical
    # Exod 27:4-5; 38:4-5; bronze altar grating; Easton has grate.json
    "grate;-grating":              {"status": "redirect-only", "redirect_to": "grate"},
    # ISBE disambiguation; burial/tomb; Easton has grave.json
    "grave-1":                     {"status": "redirect-only", "redirect_to": "grave"},
    # ISBE disambiguation; engraving/carving (Exod 28:9); Easton has grave.json
    "grave-2":                     {"status": "redirect-only", "redirect_to": "grave"},
    # ISBE compound; Easton has grave.json
    "grave;-graving":              {"status": "redirect-only", "redirect_to": "grave"},
    "gravel":                      {"status": "names-only"},   # Prov 20:17; Lam 3:16; natural material; lexical
    "gravity":                     {"status": "names-only"},   # 1 Tim 3:4; Tit 2:7 KJV "seriousness"; lexical
    "gray":                        {"status": "names-only"},   # Prov 20:29; lexical
    "grease":                      {"status": "names-only"},   # Ps 119:70 KJV "fat as grease"; lexical
    "great;-greatness":            {"status": "names-only"},   # ISBE compound; lexical
    # ISBE compound; Acts 6:1; John 7:35; Easton has grecians.json
    "grecians;-greeks":            {"status": "redirect-only", "redirect_to": "grecians"},
    "greece-religion-in-ancient":  {"status": "names-only"},   # ISBE scholarly; too specialized at score-5
    # Dan 8:21; Zech 9:13 "sons of Greece"; Easton has greece.json
    "greece-sons-of":              {"status": "redirect-only", "redirect_to": "greece"},
    # ISBE compound variant; Easton has greece.json
    "greece;-graecia":             {"status": "redirect-only", "redirect_to": "greece"},
    "greek-language":              {"status": "names-only"},   # ISBE scholarly; Koine Greek; names-only
    "greek-versions":              {"status": "names-only"},   # ISBE; Septuagint, Aquila, Theodotion etc.; scholarly
    # ISBE; Acts 16:3; 18:4; Easton has grecians.json (same people group)
    "greeks":                      {"status": "redirect-only", "redirect_to": "grecians"},
    "green;-greenish":             {"status": "names-only"},   # ISBE compound; Lev 13:49; lexical
    "greeting":                    {"status": "names-only"},   # lexical; epistolary formula
    "grief;-grieve":               {"status": "names-only"},   # ISBE compound; Isa 53:3; lexical
    "grievance":                   {"status": "names-only"},   # Hab 1:3 KJV; lexical
    "grievous;-grievously;-greievousness": {"status": "names-only"},  # ISBE compound; KJV; lexical
    "grinder":                     {"status": "names-only"},   # Eccl 12:3 "grinders cease" (teeth); cultural/lexical
    # Gen 31:10,12; Zech 6:3,6; Easton has grizzled.json
    "grisled;-grizzled":           {"status": "redirect-only", "redirect_to": "grizzled"},
    "groan":                       {"status": "names-only"},   # Rom 8:22-23; 2 Cor 5:2-4; lexical
    "gross":                       {"status": "names-only"},   # Matt 13:15; Acts 28:27 KJV "dull/fat"; lexical
    "ground;-grounded":            {"status": "names-only"},   # ISBE compound; lexical; "grounded in love" (Eph 3:17)
    "grudge":                      {"status": "names-only"},   # Lev 19:18 KJV; Jas 5:9; lexical
    "guardian":                    {"status": "names-only"},   # Gal 4:2 "guardian/tutor" (epitropos); lexical
    "guide":                       {"status": "names-only"},   # lexical; "God will be our guide" (Ps 48:14)
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
    print(f'BPG Curation C45: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
