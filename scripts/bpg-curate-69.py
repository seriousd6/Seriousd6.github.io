"""
BPG Curation — Batch C69: spiritual-man → summer (gaps 7049–7153)
Gaps reviewed: 105 (score-5 isbe-scholarly S entries — star, stranger/sojourner,
straw/stubble, succoth, sulphur/brimstone)

Redirects: star;-stars→stars; stranger-and-sojourner-in-the-apocrypha→stranger;
stranger-and-sojourner-in-the-old-testament→stranger; straw;-stubble→straw;
succoth-1/2→succoth; sulphur→brimstone.
0 stub-needed; 7 redirects; 98 names-only.

Script: scripts/bpg-curate-69.py
Run: python3 scripts/bpg-curate-69.py  (from project root)
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
    "spiritual-man":            {"status": "names-only"},   # 1 Cor 2:15; covered under "spiritual gifts"
    "spiritual-meat":           {"status": "names-only"},   # 1 Cor 10:3; lexical
    "spiritual-rock":           {"status": "names-only"},   # 1 Cor 10:4; covered under "rock"
    "spiritual-sacrifice":      {"status": "names-only"},   # 1 Pet 2:5; covered under "sacrifice"
    "spiritual-songs":          {"status": "names-only"},   # Eph 5:19; Col 3:16; covered under "music"
    "spiritual-things":         {"status": "names-only"},   # 1 Cor 2:13; lexical
    "spirituality":             {"status": "names-only"},   # covered under "spiritual"
    "spiritually":              {"status": "names-only"},   # Rev 11:8 KJV; lexical
    "spit;-spittle":            {"status": "names-only"},   # ISBE compound; Mark 8:23; John 9:6; brief
    "spoil":                    {"status": "names-only"},   # lexical; covered under "war"
    "spoiler":                  {"status": "names-only"},   # Isa 16:4; Jer 48:8; lexical
    "spoke":                    {"status": "names-only"},   # 1 Kgs 7:33 chariot spoke; brief
    "spoon":                    {"status": "names-only"},   # Num 7:14 golden spoon; brief
    "sports":                   {"status": "names-only"},   # athletic games; covered under "games"
    "spot;-spotted":            {"status": "names-only"},   # ISBE compound; Gen 30:32; Jude 23; lexical
    "spread;-spreading":        {"status": "names-only"},   # ISBE compound; lexical
    "sprinkle;-sprinkling":     {"status": "names-only"},   # ISBE compound; Heb 9:13; Lev 4:6; brief
    "spurious-acts-epistles-gospels": {"status": "names-only"},  # ISBE scholarly; apocryphal; too specialized
    "spy":                      {"status": "names-only"},   # Num 13:2; Josh 2:1; lexical
    "stack":                    {"status": "names-only"},   # Exod 22:6 KJV "stack of corn"; archaic
    "staff":                    {"status": "names-only"},   # Gen 32:10; Ps 23:4; covered under "rod"
    "stair":                    {"status": "names-only"},   # Neh 9:4; 2 Kgs 9:13; architectural; brief
    "stake":                    {"status": "names-only"},   # Isa 33:20; 54:2; tent peg; brief
    "stalk":                    {"status": "names-only"},   # Gen 41:5,22; Josh 2:6; agricultural; brief
    "stall":                    {"status": "names-only"},   # 1 Kgs 4:26; 2 Chr 32:28; agricultural; brief
    "stammerer":                {"status": "names-only"},   # Isa 32:4 KJV; brief
    "standard-bearer":          {"status": "names-only"},   # Isa 10:18 KJV; military; brief
    "standing":                 {"status": "names-only"},   # lexical
    "star-in-the-east":         {"status": "names-only"},   # Matt 2:2; covered under "magi"
    "star-of-bethlehem":        {"status": "names-only"},   # Matt 2:2; astronomical/theological debate; names-only
    "star-of-the-magi":         {"status": "names-only"},   # Matt 2; same as above; names-only
    "star-of-wormwood":         {"status": "names-only"},   # Rev 8:10-11; symbolic; brief
    # ISBE compound; Job 9:9; Amos 5:8; Easton has stars.json
    "star;-stars":              {"status": "redirect-only", "redirect_to": "stars"},
    "stars-courses-of":         {"status": "names-only"},   # Judg 5:20; astronomical; brief
    "stars-falling;-morning;-wandering": {"status": "names-only"},  # ISBE compound; astronomical; brief
    "stars-seven":              {"status": "names-only"},   # Rev 1:16,20; covered under "Revelation"
    "stately":                  {"status": "names-only"},   # Ezek 23:41 KJV; archaic
    "stature":                  {"status": "names-only"},   # lexical; brief
    "staves":                   {"status": "names-only"},   # Exod 25:13-15; covered under "ark"
    "stay":                     {"status": "names-only"},   # lexical
    "stead;-steads":            {"status": "names-only"},   # ISBE compound; lexical
    "stedfastness":             {"status": "names-only"},   # KJV spelling; Col 2:5; 2 Pet 3:17; lexical
    "steward":                  {"status": "names-only"},   # Luke 16:1-8; covered under "parables"
    "stewpan":                  {"status": "names-only"},   # Lev 2:7 KJV "baking pan"; archaic; brief
    "stiff-necked":             {"status": "names-only"},   # Exod 32:9; Acts 7:51; covered under "hardness of heart"
    "still":                    {"status": "names-only"},   # lexical
    "sting":                    {"status": "names-only"},   # 1 Cor 15:55-56; Rev 9:10; brief
    "stir-stir-up":             {"status": "names-only"},   # ISBE compound; lexical
    "stock":                    {"status": "names-only"},   # Jer 2:27; Isa 44:19; lexical
    "stomach":                  {"status": "names-only"},   # 1 Tim 5:23; anatomical; brief
    "stone-stones":             {"status": "names-only"},   # ISBE compound; covered under specific stone articles
    "stone-squarers":           {"status": "names-only"},   # 1 Kgs 5:18 KJV; brief
    "stool":                    {"status": "names-only"},   # Exod 1:16 KJV "birthstool"; 2 Kgs 4:10; brief
    "storax":                   {"status": "names-only"},   # Gen 30:37 KJV "hazel" possibly storax; botanical
    "store-cities":             {"status": "names-only"},   # 1 Kgs 9:19; Exod 1:11; covered under "treasure cities"
    "storehouses":              {"status": "names-only"},   # Deut 28:8; covered under "treasury"
    "stories":                  {"status": "names-only"},   # Ezek 41:16 architectural "floors/stories"; brief
    "story":                    {"status": "names-only"},   # architectural; lexical
    "story-telling":            {"status": "names-only"},   # ISBE scholarly; brief
    "story-writer":             {"status": "names-only"},   # ISBE scholarly; brief
    "stout;-stoutness":         {"status": "names-only"},   # ISBE compound; Isa 10:12; lexical
    "straight-street":          {"status": "names-only"},   # Acts 9:11 Damascus street; minor place; brief
    "straight;-straightway":    {"status": "names-only"},   # ISBE compound; lexical
    "strain":                   {"status": "names-only"},   # Matt 23:24 KJV "strain at a gnat"; lexical
    "strait;-straiten;-straitly": {"status": "names-only"}, # ISBE compound; lexical
    "strakes":                  {"status": "names-only"},   # Gen 30:37-38 KJV "peeled white strakes"; archaic
    "strange-gods":             {"status": "names-only"},   # Gen 35:2-4; covered under "idol"
    "strange-wife":             {"status": "names-only"},   # Prov 2:16; 5:3; covered under "adultery"
    "strange-woman":            {"status": "names-only"},   # Prov 5:3-20; covered under "adultery"
    "strange-fire":             {"status": "names-only"},   # Lev 10:1; Nadab and Abihu; covered under "Nadab"
    # ISBE scholarly; Eph 2:12; Acts 17:12; Easton has stranger.json
    "stranger-and-sojourner-in-the-apocrypha-and-the-new-testament": {"status": "redirect-only", "redirect_to": "stranger"},
    # ISBE scholarly; Exod 22:21; Lev 19:34; Easton has stranger.json
    "stranger-and-sojourner-in-the-old-testament": {"status": "redirect-only", "redirect_to": "stranger"},
    "strangled":                {"status": "names-only"},   # Acts 15:20,29; covered under "law, Jewish"
    "strangling":               {"status": "names-only"},   # Job 7:15 KJV; Nah 2:12; brief
    # ISBE compound; Exod 5:12; Isa 40:24; Easton has straw.json
    "straw;-stubble":           {"status": "redirect-only", "redirect_to": "straw"},
    "strawed":                  {"status": "names-only"},   # Matt 25:24 KJV "scattered"; archaic
    "stream":                   {"status": "names-only"},   # lexical; generic
    "strength-of-israel":       {"status": "names-only"},   # 1 Sam 15:29 title for God; brief
    "strike":                   {"status": "names-only"},   # lexical
    "stringed-instruments":     {"status": "names-only"},   # Ps 4 title; covered under "music"
    "strive":                   {"status": "names-only"},   # lexical
    "stronghold":               {"status": "names-only"},   # Ps 9:9; covered under "fortress"
    "stubble":                  {"status": "names-only"},   # Exod 5:12; covered under "straw"
    "studs":                    {"status": "names-only"},   # Song 1:11 KJV "studs of silver"; brief
    "stuff":                    {"status": "names-only"},   # KJV "baggage/goods"; archaic/lexical
    "stumbling-block;-stumbling-stone": {"status": "names-only"},  # ISBE compound; 1 Cor 1:23; lexical
    "sua":                      {"status": "names-only"},   # apocryphal variant (1 Esd 5:29)
    "sub-apostolic-literature": {"status": "names-only"},   # ISBE scholarly; Apostolic Fathers; names-only
    "subai":                    {"status": "names-only"},   # apocryphal variant
    "subas":                    {"status": "names-only"},   # apocryphal variant (1 Esd 5:22)
    "suborn":                   {"status": "names-only"},   # Acts 6:11 KJV "suborned"; archaic
    "substance":                {"status": "names-only"},   # lexical
    "subtil;-subtle;-subtlety;-subtilty": {"status": "names-only"},  # ISBE compound; Gen 3:1; lexical
    "subvert":                  {"status": "names-only"},   # lexical
    "sucathites":               {"status": "names-only"},   # 1 Chr 2:55 scribal clan; minor
    "succeed;-success":         {"status": "names-only"},   # ISBE compound; lexical
    "succor;-succorer":         {"status": "names-only"},   # ISBE compound; Heb 2:18; lexical
    # ISBE disambiguation; Exod 12:37 Israelite camp; Easton has succoth.json
    "succoth-1":                {"status": "redirect-only", "redirect_to": "succoth"},
    # ISBE disambiguation; 1 Kgs 7:46 city in Jordan valley; Easton has succoth.json
    "succoth-2":                {"status": "redirect-only", "redirect_to": "succoth"},
    "sudias":                   {"status": "names-only"},   # apocryphal variant (1 Esd 5:26)
    "suffering":                {"status": "names-only"},   # 1 Pet 4:12-13; covered under "afflictions"
    "suffocation":              {"status": "names-only"},   # rare; lexical
    "suicide":                  {"status": "names-only"},   # Saul, Judas; covered under specific narratives
    # KJV "brimstone" for sulphur; Gen 19:24; Rev 19:20; Easton has brimstone.json
    "sulphur":                  {"status": "redirect-only", "redirect_to": "brimstone"},
    "summer":                   {"status": "names-only"},   # Prov 10:5; Amos 8:1-2; lexical
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
    print(f'BPG Curation C69: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
