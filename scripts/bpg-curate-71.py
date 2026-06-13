"""
BPG Curation — Batch C71: terah-2 → tower-of-shechem (gaps 7259–7363)
Gaps reviewed: 105 (score-5 isbe-scholarly T entries — thessalonians, threshing,
timothy, titus, tongues, torch, tower-of-babel, tower-of-hananeel)

Redirects: testimony-ark-of-the→testimony;
thessalonians-the-first/second→thessalonians-epistles-to-the; thistles→thistle;
thorns-thistles-etc.→thorn; threshing-floor→threshing; timothy-epistles-to→timothy;
titus;-titius-justus→titus; tongues-interpretation-of→tongues-gift-of;
torch→torches; tower-of-babel→babel-tower-of; tower-of-hananeel→hananeel.
0 stub-needed; 12 redirects; 93 names-only.

Script: scripts/bpg-curate-71.py
Run: python3 scripts/bpg-curate-71.py  (from project root)
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
    "terah-2":                  {"status": "names-only"},   # ISBE disambiguation; Num 33:27 campsite; minor
    "terrace":                  {"status": "names-only"},   # 2 Chr 9:11 KJV "terraces/stairs"; brief
    "terrible-terror":          {"status": "names-only"},   # ISBE compound; lexical
    "testament-of-isaac":       {"status": "names-only"},   # pseudepigraphical; apocryphal; too specialized
    "testament-new-canon-of-the": {"status": "names-only"}, # ISBE scholarly; covered under "canon"
    "testament-new-text-and-manuscripts-of-the": {"status": "names-only"},  # ISBE scholarly; names-only
    "testament-old-canon-of-the": {"status": "names-only"}, # ISBE scholarly; covered under "canon"
    "testament-old-text-of-the": {"status": "names-only"},  # ISBE scholarly; names-only
    "testaments-of-the-twelve-patriarchs": {"status": "names-only"},  # pseudepigraphical; too specialized
    "testaments-between-the":   {"status": "names-only"},   # ISBE intertestamental period; covered under "apocrypha"
    # ISBE; Exod 25:16,21 "ark of the testimony"; Easton has testimony.json
    "testimony-ark-of-the":     {"status": "redirect-only", "redirect_to": "testimony"},
    "teta":                     {"status": "names-only"},   # apocryphal variant (1 Esd 5:32)
    "teth":                     {"status": "names-only"},   # Hebrew letter; covered under "Hebrew alphabet"
    "tetter":                   {"status": "names-only"},   # Lev 21:20 KJV skin disease; archaic
    "text-and-manuscripts-of-the-new-testament": {"status": "names-only"},  # ISBE scholarly; duplicate entry
    "text-of-the-old-testament": {"status": "names-only"},  # ISBE scholarly; names-only
    "thammuz":                  {"status": "names-only"},   # Ezek 8:14 pagan deity; covered under "Tammuz"
    "thamnatha":                {"status": "names-only"},   # 1 Macc 9:50 variant of Timnah; apocryphal
    "thank-offering":           {"status": "names-only"},   # Lev 7:12-15; covered under "peace offerings"
    "thank;-thanks;-thanksgiving": {"status": "names-only"}, # ISBE compound; Ps 100; lexical
    "thassi":                   {"status": "names-only"},   # 1 Macc 2:3 Simon Maccabee's surname; apocryphal
    "that-day":                 {"status": "names-only"},   # OT prophetic formula; covered under "day of the Lord"
    "thecoe":                   {"status": "names-only"},   # 1 Macc 9:33 variant of Tekoa; apocryphal
    "thee-ward":                {"status": "names-only"},   # KJV archaic "toward thee"; lexical
    "thelersas":                {"status": "names-only"},   # Ezra 2:59 Babylonian place; minor
    "theocanus":                {"status": "names-only"},   # apocryphal variant (1 Esd 9:25)
    "theodotion":               {"status": "names-only"},   # ISBE scholarly; 2nd-c. Greek OT translator; names-only
    "theodotus":                {"status": "names-only"},   # 2 Macc 14:19; apocryphal
    "theology":                 {"status": "names-only"},   # general academic discipline; too broad for an article
    "theras":                   {"status": "names-only"},   # ISBE place; Ezra 2:59 variant; names-only
    "thermeleth":               {"status": "names-only"},   # Ezra 2:59 Babylonian place; minor
    # ISBE compound; Easton has thessalonians-epistles-to-the.json
    "thessalonians-the-first-epistle-of-paul-to-the": {"status": "redirect-only", "redirect_to": "thessalonians-epistles-to-the"},
    # ISBE compound; Easton has thessalonians-epistles-to-the.json
    "thessalonians-the-second-epistle-of-paul-to-the": {"status": "redirect-only", "redirect_to": "thessalonians-epistles-to-the"},
    "thick-trees":              {"status": "names-only"},   # Lev 23:40; Neh 8:15 "leafy branches"; botanical; brief
    "thicket":                  {"status": "names-only"},   # Gen 22:13 "thicket"; Jer 4:7; brief
    "thief":                    {"status": "names-only"},   # Exod 22:2; Matt 6:19; lexical
    "thigh":                    {"status": "names-only"},   # Gen 24:2,9; Gen 32:25; anatomical; cultural
    "think":                    {"status": "names-only"},   # lexical
    "third":                    {"status": "names-only"},   # lexical
    "third-day":                {"status": "names-only"},   # 1 Cor 15:4; resurrection; covered under "resurrection"
    "thirst":                   {"status": "names-only"},   # John 4:13-14; 19:28; lexical
    "thirteen;-thirty":         {"status": "names-only"},   # ISBE compound; numerical; names-only
    "thisbe":                   {"status": "names-only"},   # 1 Kgs 17:1 KJV Elijah's hometown (Tishbe); minor
    # ISBE; Gen 3:18; 2 Kgs 14:9; Easton has thistle.json
    "thistles":                 {"status": "redirect-only", "redirect_to": "thistle"},
    "thocanus":                 {"status": "names-only"},   # apocryphal variant (1 Esd 9:25)
    "thomas-gospel-of":         {"status": "names-only"},   # Gnostic gospel; apocryphal; too specialized
    "thomei":                   {"status": "names-only"},   # apocryphal variant (1 Esd 9:27)
    # ISBE compound; Gen 3:18; Heb 6:8; Easton has thorn.json
    "thorns-thistles-etc.":     {"status": "redirect-only", "redirect_to": "thorn"},
    "thought":                  {"status": "names-only"},   # lexical
    "thousand":                 {"status": "names-only"},   # lexical; numerical
    "thracia;-thracian":        {"status": "names-only"},   # ISBE place; Acts 16:11 area; names-only
    "thrasaeus":                {"status": "names-only"},   # 2 Macc 3:5 father of Apollonius; apocryphal
    "three":                    {"status": "names-only"},   # lexical
    "three-children-song-of-the": {"status": "names-only"}, # deuterocanonical; apocryphal; names-only
    "threescore":               {"status": "names-only"},   # KJV "sixty"; archaic/lexical
    # ISBE; Ruth 3:2; Amos 1:3; Easton has threshing.json
    "threshing-floor":          {"status": "redirect-only", "redirect_to": "threshing"},
    "thrum":                    {"status": "names-only"},   # Isa 38:12 KJV "loom end thread"; archaic
    "tidings-glad":             {"status": "names-only"},   # covered under "gospel" (euangelion)
    "tikvah;-tikvath":          {"status": "names-only"},   # ISBE compound; 2 Kgs 22:14; minor persons
    "tile;-tiling":             {"status": "names-only"},   # ISBE compound; Luke 5:19; Ezek 4:1; architectural
    "tillage":                  {"status": "names-only"},   # Prov 13:23; 1 Chr 27:26; agricultural; lexical
    "time":                     {"status": "names-only"},   # lexical
    "time-last":                {"status": "names-only"},   # covered under "eschatology" and "last days"
    "time-times-and-a-half":    {"status": "names-only"},   # Dan 7:25; 12:7; Rev 12:14; covered under "Daniel"
    "times-observer-of":        {"status": "names-only"},   # Deut 18:10 divination; covered under "divination"
    "timna":                    {"status": "names-only"},   # Gen 36:12,22; Edomite; minor
    # ISBE compound; 1 Tim 1:2; Easton has timothy.json (covers both epistles)
    "timothy-epistles-to":      {"status": "redirect-only", "redirect_to": "timothy"},
    "tirathites":               {"status": "names-only"},   # 1 Chr 2:55 scribal clan; minor
    "tire-headtire":            {"status": "names-only"},   # Isa 3:18 KJV "ornament/headband"; archaic
    "tires-round":              {"status": "names-only"},   # Judg 8:21,26 KJV "ornaments"; archaic
    "tirhana":                  {"status": "names-only"},   # 1 Chr 2:48 Caleb's son; minor
    "tishri;-tisri":            {"status": "names-only"},   # ISBE compound; Hebrew calendar month; covered under "calendar"
    "titans":                   {"status": "names-only"},   # general mythology; not biblical
    "title":                    {"status": "names-only"},   # John 19:19 "title" on cross; lexical
    "titus-manius":             {"status": "names-only"},   # 2 Macc 11:34 Roman envoy; apocryphal
    # ISBE compound; Acts 18:7 Titius Justus; Easton has titus.json (Paul's companion)
    "titus;-titius-justus":     {"status": "redirect-only", "redirect_to": "titus"},
    "tizite":                   {"status": "names-only"},   # 1 Chr 11:45 epithet of Joha; minor
    "tobias":                   {"status": "names-only"},   # deuterocanonical/apocryphal Tobit character; names-only
    "tobie":                    {"status": "names-only"},   # apocryphal variant of Tobias; names-only
    "tobiel":                   {"status": "names-only"},   # Tobit 1:1 Tobit's father; apocryphal; minor
    "token":                    {"status": "names-only"},   # KJV "sign/pledge"; lexical
    "tokhath":                  {"status": "names-only"},   # 2 Chr 34:22 variant of Tikvah; minor
    "tolbanes":                 {"status": "names-only"},   # apocryphal variant (1 Esd 9:25)
    "tomorrow":                 {"status": "names-only"},   # lexical
    "tongs":                    {"status": "names-only"},   # Isa 6:6; 1 Kgs 7:49; temple utensil; brief
    "tongue":                   {"status": "names-only"},   # lexical; covered under "tongues, gift of"
    "tongues-of-fire":          {"status": "names-only"},   # Acts 2:3; covered under "pentecost"
    # ISBE; 1 Cor 12:10,30; 14:28; Easton has tongues-gift-of.json
    "tongues-interpretation-of": {"status": "redirect-only", "redirect_to": "tongues-gift-of"},
    "tools":                    {"status": "names-only"},   # general; covered under specific tool articles
    "toparchy":                 {"status": "names-only"},   # Roman administrative division; 1 Macc 11:28; names-only
    "torah":                    {"status": "names-only"},   # Hebrew "law/teaching"; covered under "law"
    # ISBE; Judg 15:4-5; Nah 2:4; Easton has torches.json
    "torch":                    {"status": "redirect-only", "redirect_to": "torches"},
    "torment-place-of":         {"status": "names-only"},   # Luke 16:28; covered under "Hades" and "Gehenna"
    "tormentor":                {"status": "names-only"},   # Matt 18:34 KJV; lexical
    "totemism":                 {"status": "names-only"},   # anthropological concept; not specifically biblical
    "tou":                      {"status": "names-only"},   # 2 Sam 8:9 variant of Toi king of Hamath; minor
    # ISBE; Gen 11:1-9; Easton has babel-tower-of.json
    "tower-of-babel":           {"status": "redirect-only", "redirect_to": "babel-tower-of"},
    "tower-of-david":           {"status": "names-only"},   # Song 4:4; Jerusalem; covered under "Jerusalem"
    "tower-of-edar-the-flock":  {"status": "names-only"},   # Gen 35:21; Mic 4:8; brief
    # ISBE; Neh 3:1; 12:39; Easton has hananeel.json
    "tower-of-hananeel":        {"status": "redirect-only", "redirect_to": "hananeel"},
    "tower-of-ivory":           {"status": "names-only"},   # Song 7:4; brief
    "tower-of-lebanon":         {"status": "names-only"},   # Song 7:4; brief
    "tower-of-meah":            {"status": "names-only"},   # Neh 3:1; Jerusalem tower; brief
    "tower-of-penuel":          {"status": "names-only"},   # Judg 8:17; minor
    "tower-of-shechem":         {"status": "names-only"},   # Judg 9:46-49; minor
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
    print(f'BPG Curation C71: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
