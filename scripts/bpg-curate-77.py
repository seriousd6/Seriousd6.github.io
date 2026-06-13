"""
BPG Curation — Batch C77: creeping-things → exports (gaps 7784–7888)
Gaps reviewed: 105 (score-3 concept-no-article C–E entries)

Score-3 concept-no-article entries: legal concepts, abstract virtues/vices,
non-biblical academic topics, and minor persons. Conservative posture: 0 stubs.
0 stub-needed; 11 redirect-only; 94 names-only.

Redirects: curtains→curtain; cyrenius-quirinius→cyrenius;
diadem.-r.-v.-mitre→diadem; didymus-twin→didymus;
dove-turtle→turtle-turtle-dove; enon-aenon→aenon;
ephesians→ephesians-epistle-to; ephraimites→ephraim-the-tribe-of;
esar-haddon-esarhaddon→esarhaddon; eucharist-the-lords-supper→lords-supper;
exorcism→exorcist.

Script: scripts/bpg-curate-77.py
Run: python3 scripts/bpg-curate-77.py  (from project root)
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
    "creeping-things":       {"status": "names-only"},   # Gen 1:24-25; Lev 11:29-31; covered under "animals"
    "crime":                 {"status": "names-only"},   # legal concept; covered under specific crimes
    "criminals":             {"status": "names-only"},   # Luke 23:32-33; covered under specific narratives
    "crimination":           {"status": "names-only"},   # legal; accusation; lexical
    "criticism-unjust":      {"status": "names-only"},   # Matt 7:1-5; covered under "judging"
    "cross-questioning":     {"status": "names-only"},   # legal; names-only
    "cruelty":               {"status": "names-only"},   # Gen 49:5; covered under "violence"
    "cupidity":              {"status": "names-only"},   # covetousness; covered under "covetousness"
    "cures":                 {"status": "names-only"},   # covered under "miracles" and "healing"
    "cursing":               {"status": "names-only"},   # Prov 26:2; Rom 12:14; covered under "curse"
    # ISBE; Exod 26:1-14; Num 4:5; Easton has curtain.json
    "curtains":              {"status": "redirect-only", "redirect_to": "curtain"},
    # Luke 2:2 "Cyrenius/Quirinius governor of Syria"; Easton has cyrenius.json
    "cyrenius-quirinius":    {"status": "redirect-only", "redirect_to": "cyrenius"},
    "daily-offering":        {"status": "names-only"},   # Num 28:3-8 Tamid; covered under "offering"
    "damages-and-compensation": {"status": "names-only"},  # Exod 21-22; legal; covered under "law, Mosaic"
    "damned":                {"status": "names-only"},   # Mark 16:16 KJV; covered under "judgment"
    "deafness":              {"status": "names-only"},   # Lev 19:14; Mark 7:32-35; covered under "disease"
    "decrees":               {"status": "names-only"},   # political; covered under "law" and "commandments"
    "decrees-divine":        {"status": "names-only"},   # Calvinist/Arminian; covered under "election" and "predestination"
    "defense":               {"status": "names-only"},   # legal/military; lexical
    "deformity":             {"status": "names-only"},   # Lev 21:17-21; covered under "disease"
    "degrees":               {"status": "names-only"},   # Ps 120-134 "Songs of Degrees" = "Ascents"; covered under "psalms"
    "deliverance":           {"status": "names-only"},   # covered under "redemption" and "salvation"
    "deliverer":             {"status": "names-only"},   # Judg; Rom 11:26; covered under "judges" and "redemption"
    "delusion-self":         {"status": "names-only"},   # Jas 1:22; covered under "self-deception"; lexical
    "demagogism":            {"status": "names-only"},   # political; not biblical topic
    "dens":                  {"status": "names-only"},   # Dan 6:7 lion's den; brief; covered under "Daniel"
    "denying-jesus":         {"status": "names-only"},   # Matt 10:33; 2 Tim 2:12; covered under "confession"
    "design":                {"status": "names-only"},   # philosophical/theological; names-only
    "despotism":             {"status": "names-only"},   # political; covered under "government"
    "detectives":            {"status": "names-only"},   # not biblical topic; names-only
    "devotion":              {"status": "names-only"},   # covered under "prayer" and "worship"
    # Rev 6:2 KJV "diadem"; Easton has diadem.json; also covers RV/AV variant "mitre"
    "diadem.-r.-v.-mitre":  {"status": "redirect-only", "redirect_to": "diadem"},
    # John 11:16; 20:24 Thomas = Didymus (twin); Easton has didymus.json
    "didymus-twin":          {"status": "redirect-only", "redirect_to": "didymus"},
    "disbelief":             {"status": "names-only"},   # covered under "unbelief" and "faith"
    "discipleship":          {"status": "names-only"},   # covered under "disciple" in Easton; names-only
    "discontentment":        {"status": "names-only"},   # Phil 4:11; covered under "contentment"
    "discouragement":        {"status": "names-only"},   # Num 21:4; covered under "despair"
    "dispute":               {"status": "names-only"},   # Acts 15:2; lexical
    "dissembling":           {"status": "names-only"},   # Gal 2:13 KJV; covered under "hypocrisy"
    "dissension":            {"status": "names-only"},   # Acts 15:2; 23:7; lexical
    "dissipation":           {"status": "names-only"},   # Luke 15:13; covered under "prodigal son"
    "divinity-of-christ":    {"status": "names-only"},   # covered under "Jesus Christ" in Easton; score-3; names-only
    "doer":                  {"status": "names-only"},   # Jas 1:22-25 "doer of the word"; lexical
    "dogmatism":             {"status": "names-only"},   # not specifically biblical; names-only
    "domicile":              {"status": "names-only"},   # legal/social; names-only
    "donations":             {"status": "names-only"},   # covered under "alms" and "giving"
    "doorkeepers":           {"status": "names-only"},   # 2 Kgs 25:18; covered under "temple"
    # Lev 1:14; Song 2:12; Easton has turtle-turtle-dove.json
    "dove-turtle":           {"status": "redirect-only", "redirect_to": "turtle-turtle-dove"},
    "drama":                 {"status": "names-only"},   # not biblical genre; names-only
    "drawing":               {"status": "names-only"},   # art/lexical; not biblical topic
    "driving":               {"status": "names-only"},   # 2 Kgs 9:20 "driving furiously"; lexical
    "drunkard":              {"status": "names-only"},   # Prov 23:21; 1 Cor 5:11; covered under "drunkenness"
    "dumb-deafness-mute":    {"status": "names-only"},   # ISBE compound; Mark 7:32-37; covered under "disease"
    "duty-tax":              {"status": "names-only"},   # Matt 17:24-27; covered under "tribute"
    "dwarfs":                {"status": "names-only"},   # Lev 21:20 KJV; brief; covered under "deformity"
    "dyeing":                {"status": "names-only"},   # Exod 25:5; Josh 2:18; cultural; brief
    "dying":                 {"status": "names-only"},   # lexical; covered under "death"
    "dyspepsia":             {"status": "names-only"},   # 1 Tim 5:23; medical; brief
    "earnestness":           {"status": "names-only"},   # 2 Cor 8:7; covered under "zeal"
    "easter-a.v.":           {"status": "names-only"},   # Acts 12:4 KJV "Easter"; covered under "passover"
    "ecclesiasticism":       {"status": "names-only"},   # not a biblical topic; academic; names-only
    "economics":             {"status": "names-only"},   # general discipline; not biblical
    "economy":               {"status": "names-only"},   # dispensation/stewardship; covered under "dispensation"
    "egotism":               {"status": "names-only"},   # covered under "pride"
    "electioneering":        {"status": "names-only"},   # political; not biblical topic
    "elegy":                 {"status": "names-only"},   # Lamentations as elegy; covered under "lamentations"
    "elisabeth-elizabeth":   {"status": "names-only"},   # Luke 1:5-57; no elizabeth.json found; names-only
    "emancipation":          {"status": "names-only"},   # legal; covered under "slavery" and "jubilee"
    "embezzlement":          {"status": "names-only"},   # legal; not biblical topic
    "emergency":             {"status": "names-only"},   # lexical; not biblical topic
    "endurance":             {"status": "names-only"},   # Heb 12:1; Rev 3:10; covered under "patience"
    "engrafting":            {"status": "names-only"},   # Jas 1:21; Rom 11:17; covered under "adoption"
    # John 3:23; John the Baptist baptized there; Easton has aenon.json
    "enon-aenon":            {"status": "redirect-only", "redirect_to": "aenon"},
    "enquiring-of-god":      {"status": "names-only"},   # Urim/Thummim; covered under "oracle" and "urim"
    "enthusiasm":            {"status": "names-only"},   # covered under "zeal"
    "enumeration":           {"status": "names-only"},   # censuses; covered under "census"
    "epenetus-epaenetus":    {"status": "names-only"},   # Rom 16:5; no epenetus.json found; names-only
    "ephes-dammin":          {"status": "names-only"},   # 1 Sam 17:1; David and Goliath site; minor place
    # Paul's letter to Ephesus; Easton has ephesians-epistle-to.json
    "ephesians":             {"status": "redirect-only", "redirect_to": "ephesians-epistle-to"},
    # Num 26:35; Josh 16:10; Easton has ephraim-the-tribe-of.json
    "ephraimites":           {"status": "redirect-only", "redirect_to": "ephraim-the-tribe-of"},
    "ephrath":               {"status": "names-only"},   # Gen 35:19; Bethlehem-Ephrathah; covered under "bethlehem"
    "epic":                  {"status": "names-only"},   # literary genre; not biblical category
    "equality-of-men":       {"status": "names-only"},   # Gal 3:28; covered under "brotherhood" and "man"
    "equity-fairness":       {"status": "names-only"},   # Ps 98:9; covered under "justice"
    "errors":                {"status": "names-only"},   # Ps 19:12; lexical
    # 2 Kgs 19:37; Isa 37:38 Assyrian king; Easton has esarhaddon.json
    "esar-haddon-esarhaddon": {"status": "redirect-only", "redirect_to": "esarhaddon"},
    "escape":                {"status": "names-only"},   # lexical; covered under specific narratives
    "escheat":               {"status": "names-only"},   # legal; property reversion; not biblical
    "etiquette":             {"status": "names-only"},   # social manners; covered under "manners and customs"
    # Acts 2:42-47; 1 Cor 11:20-29; Easton has lords-supper.json
    "eucharist-the-lords-supper": {"status": "redirect-only", "redirect_to": "lords-supper"},
    "evangelism":            {"status": "names-only"},   # covered under "gospel" and "evangelist"
    "evaporation":           {"status": "names-only"},   # Ps 22:15; meteorological; brief
    "everlasting-fire":      {"status": "names-only"},   # Matt 18:8; 25:41; covered under "hell"
    "everlasting-life":      {"status": "names-only"},   # John 3:16; covered under "eternal life"
    "everlasting-punishment": {"status": "names-only"},  # Matt 25:46; covered under "hell" and "judgment"
    "eviction":              {"status": "names-only"},   # legal; not biblical topic
    "evidence":              {"status": "names-only"},   # legal; Deut 17:6; covered under "witness"
    "evil-for-evil":         {"status": "names-only"},   # Rom 12:17; 1 Thess 5:15; covered under "vengeance"
    "evil-speaking":         {"status": "names-only"},   # 1 Pet 2:1; covered under "slander"
    "exaltation":            {"status": "names-only"},   # Phil 2:9; covered under "ascension" and "Christ"
    "exchangers":            {"status": "names-only"},   # Matt 25:27 KJV "exchangers/money-changers"; lexical
    "excuses":               {"status": "names-only"},   # Luke 14:18-20; covered under "parable of banquet"
    # Acts 19:13-16; Easton has exorcist.json (covers both exorcism and exorcists)
    "exorcism":              {"status": "redirect-only", "redirect_to": "exorcist"},
    "expediency":            {"status": "names-only"},   # 1 Cor 6:12; covered under "liberty, Christian"
    "exports":               {"status": "names-only"},   # commercial; covered under "trade"
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
    print(f'BPG Curation C77: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
