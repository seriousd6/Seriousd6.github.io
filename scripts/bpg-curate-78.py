"""
BPG Curation — Batch C78: midianites → proclamation (gaps 7999–8108)
Gaps reviewed: 110 (score-3 concept-no-article M–P entries)

Stub-needed criteria applied:
  - Core Christological titles regardless of verse count (names-of-jesus, new-creature, prince-of-peace)
  - Nave verse count >= 11 AND theologically/historically significant (midianites, miscegenation,
    motive, obduracy-hardness, panic, paradox, parsimony-stinginess, politics, polytheism,
    prayerfulness, prayerlessness, probation)
  - Important figures with narrative significance (nebuzaradan: 7v, destroyed Jerusalem)
  - Significant NT events despite low verse count (money-changers: 3v, all 4 Gospels)
  - Liturgical concepts critical to biblical chronology (preparation-day: 6v, crucifixion)
  - Historically significant locations (pretorium: 7v, site of Jesus' trial)
  - Key spiritual practices (prayerfulness: 18v, prayerlessness: 15v, porters: 9v)

20 stub-needed; 3 redirect-only; 87 skip.

Script: scripts/bpg-curate-78.py
Run: python3 scripts/bpg-curate-78.py (from repo root)
"""

import json
import os

GAPS_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'biblepedia', 'gaps.json')


def load_gaps():
    with open(GAPS_FILE, encoding='utf-8') as f:
        return json.load(f)


def save_gaps(gaps):
    with open(GAPS_FILE, 'w', encoding='utf-8') as f:
        json.dump(gaps, f, ensure_ascii=False, indent=2)


# Curation decisions: { id: { status, redirect_to? } }
DECISIONS = {
    # --- stub-needed: theologically/historically significant ---
    "midianites":               {"status": "stub-needed"},   # 16v; key OT people group (Exodus, Gideon, Balaam)
    "miscegenation":            {"status": "stub-needed"},   # 16v; intermarriage prohibition is a recurring OT theme (Ezra, Nehemiah)
    "money-changers":           {"status": "stub-needed"},   # 3v but all 4 Gospels; Temple cleansing is a landmark event
    "motive":                   {"status": "stub-needed"},   # 17v; heart-motive (Matt 6, Jas 4) is central NT ethics
    "names-of-jesus":           {"status": "stub-needed"},   # 0v but major Christological topic; titles/names of Jesus
    "nebuzaradan-nebuzar-adan": {"status": "stub-needed"},   # 7v; Babylonian commander who destroyed Jerusalem (2 Ki 25; Jer 39-41)
    "new-creature":             {"status": "stub-needed"},   # 0v but core Pauline doctrine (2 Cor 5:17; Gal 6:15)
    "obduracy-hardness":        {"status": "stub-needed"},   # 17v; hardness of heart is a major biblical motif (Pharaoh, Israel)
    "panic":                    {"status": "stub-needed"},   # 12v; divine panic sent on enemies is a distinct OT holy-war motif
    "paradox":                  {"status": "stub-needed"},   # 16v; biblical paradoxes (dying to live, last-first) are a rich topic
    "parsimony-stinginess":     {"status": "stub-needed"},   # 11v; biblical vice opposite generosity; substantial NT teaching
    "politics":                 {"status": "stub-needed"},   # 17v; church-state relations and political themes throughout Scripture
    "polytheism":               {"status": "stub-needed"},   # 13v; biblical critique of idolatry/polytheism; core OT conflict
    "porters":                  {"status": "stub-needed"},   # 9v; Temple gatekeepers as a Levitical order (1 Chr 9; Ezra 2)
    "prayerfulness":            {"status": "stub-needed"},   # 18v; prayer as a virtue; highest verse count in batch
    "prayerlessness":           {"status": "stub-needed"},   # 15v; failure of prayer as a spiritual problem (1 Sam 12:23)
    "preparation-day":          {"status": "stub-needed"},   # 6v; day before Passover/Sabbath; critical to crucifixion chronology
    "pretorium":                {"status": "stub-needed"},   # 7v; Pilate's praetorium where Jesus was tried; historically significant
    "prince-of-peace":          {"status": "stub-needed"},   # 0v but one of the four Messianic titles in Isa 9:6
    "probation":                {"status": "stub-needed"},   # 14v; spiritual testing/trial period is a genuine biblical concept

    # --- redirect-only: variant names or thin aliases ---
    "paschal-lamb":             {"status": "redirect-only", "redirect_to": "passover"},              # "Paschal Lamb" = Passover lamb; redirect to Passover article
    "penitence":                {"status": "redirect-only", "redirect_to": "repentance"},            # Synonym for repentance; Repentance is a full dict article
    "penuriousness-stinginess": {"status": "redirect-only", "redirect_to": "parsimony-stinginess"}, # Duplicate concept (stinginess); redirect to stub

    # --- skip: too low verse count, generic, or data artifact ---
    "midwifery":                {"status": "skip"},   # nave=3; narrow topic; incidental references
    "military-instruction":     {"status": "skip"},   # nave=1; single verse; too narrow
    "minister-civil":           {"status": "skip"},   # nave=10; government officials; covered under broader governance topics
    "minority-report":          {"status": "skip"},   # nave=0; data artifact
    "minors":                   {"status": "skip"},   # nave=2; generic; too few verses
    "miser":                    {"status": "skip"},   # nave=2; covered under covetousness
    "misjudgment":              {"status": "skip"},   # nave=3; generic; insufficient for article
    "mite-a-lepta":             {"status": "skip"},   # nave=2; widow's mite covered under broader Gospel/Giving topics
    "miter":                    {"status": "skip"},   # nave=4; priestly headgear; covered under priestly vestments
    "mob":                      {"status": "skip"},   # nave=4; incidental references
    "modesty":                  {"status": "skip"},   # nave=5; covered under humility
    "molding":                  {"status": "skip"},   # nave=12; Temple architectural detail; too technical
    "monarchy":                 {"status": "skip"},   # nave=1; single verse; covered under Kingship
    "monopoly":                 {"status": "skip"},   # nave=4; economic concept; marginal biblical content
    "moral-agency":             {"status": "skip"},   # nave=0; philosophical term; no dedicated biblical verse content
    "moral-law":                {"status": "skip"},   # nave=0; covered under Law of Moses articles
    "mortification":            {"status": "skip"},   # nave=2; too few verses
    "mosaic-law":               {"status": "skip"},   # nave=0; covered under Law/Torah articles
    "mote-a-speck":             {"status": "skip"},   # nave=3; single-episode reference (Matt 7:3)
    "motto":                    {"status": "skip"},   # nave=0; data artifact
    "mulberry-tree":            {"status": "skip"},   # nave=3; incidental natural history
    "munitions":                {"status": "skip"},   # nave=1; single verse
    "murrain-a-disease-of-livestock": {"status": "skip"}, # nave=3; specific plague; covered under Plagues of Egypt
    "muster":                   {"status": "skip"},   # nave=5; military census; too narrow
    "mutiny":                   {"status": "skip"},   # nave=1; single verse
    "natural-religion":         {"status": "skip"},   # nave=0; theological philosophy; not a biblical category
    "naturalization":           {"status": "skip"},   # nave=3; legal/social; incidental
    "navigation":               {"status": "skip"},   # nave=1; single verse
    "neophytes":                {"status": "skip"},   # nave=6; new converts; covered under discipleship/conversion
    "nepotism":                 {"status": "skip"},   # nave=6; social concept; incidental references
    "nolle-prosequi":           {"status": "skip"},   # nave=1; Latin legal term; data artifact
    "nonconformity":            {"status": "skip"},   # nave=0; no biblical verse category
    "nose":                     {"status": "skip"},   # nave=4; body part; incidental
    "nut":                      {"status": "skip"},   # nave=2; natural history; too few verses
    "object-teaching":          {"status": "skip"},   # nave=0; pedagogical term; no biblical verse content
    "obligation":               {"status": "skip"},   # nave=15; broad concept; subsumed under Law/Covenant
    "obliquity-deviation":      {"status": "skip"},   # nave=0; data artifact
    "obsequiousness":           {"status": "skip"},   # nave=4; too narrow; incidental
    "obstetrics":               {"status": "skip"},   # nave=1; single verse
    "occult-science":           {"status": "skip"},   # nave=0; covered under Divination/Sorcery
    "offenses":                 {"status": "skip"},   # nave=0; covered under Sin/Transgression
    "opportunity":              {"status": "skip"},   # nave=14; generic concept; not a distinct biblical topic
    "ostentation":              {"status": "skip"},   # nave=3; covered under Pride/Hypocrisy
    "ostriches":                {"status": "skip"},   # nave=10; natural history; incidental (Job, Lamentations)
    "overcoming":               {"status": "skip"},   # nave=0; no dedicated verse content
    "pack-animals":             {"status": "skip"},   # nave=1; single verse
    "pale-horse":               {"status": "skip"},   # nave=1; single verse; covered under Revelation/Horsemen topics
    "pantomime":                {"status": "skip"},   # nave=5; prophetic sign acts; covered under Prophecy articles
    "paralysis":                {"status": "skip"},   # nave=8; healing narratives; covered under Miracles/Healing
    "parricide":                {"status": "skip"},   # nave=3; too narrow; incidental
    "partiality":               {"status": "skip"},   # nave=2; too few verses
    "particeps-criminis":       {"status": "skip"},   # nave=1; Latin legal term; data artifact
    "partnership":              {"status": "skip"},   # nave=4; too narrow
    "passenger":                {"status": "skip"},   # nave=0; data artifact
    "passports":                {"status": "skip"},   # nave=1; single verse; anachronistic concept
    "patriarchal-government":   {"status": "skip"},   # nave=0; covered under Patriarchs/Governance
    "patricide":                {"status": "skip"},   # nave=2; too few verses
    "pawn":                     {"status": "skip"},   # nave=10; pledge/collateral; covered under Law/Property
    "penalty":                  {"status": "skip"},   # nave=0; covered under Punishment/Law
    "people-common":            {"status": "skip"},   # nave=5; social category; too narrow
    "perfidy-treachery":        {"status": "skip"},   # nave=0; covered under Betrayal/Deceit
    "perfume":                  {"status": "skip"},   # nave=7; covered under Anointing/Ointment
    "personal-call":            {"status": "skip"},   # nave=0; data artifact
    "personification":          {"status": "skip"},   # nave=4; literary device; not a biblical content topic
    "petroleum":                {"status": "skip"},   # nave=1; single verse
    "philanthropy":             {"status": "skip"},   # nave=1; single verse; covered under Charity/Giving
    "phoebe-phebe":             {"status": "skip"},   # nave=1; minor NT figure (Rom 16:1); single verse
    "physiognomy":              {"status": "skip"},   # nave=1; single verse
    "physiology":               {"status": "skip"},   # nave=5; general science term; not a biblical category
    "pinnacle-wing":            {"status": "skip"},   # nave=1; single verse (Temple pinnacle in temptation)
    "pispah":                   {"status": "skip"},   # nave=1; minor name; single reference
    "planet":                   {"status": "skip"},   # nave=0; data artifact
    "plants":                   {"status": "skip"},   # nave=0; covered under Flora/Botany
    "plaster":                  {"status": "skip"},   # nave=5; construction detail; incidental
    "pleading":                 {"status": "skip"},   # nave=8; legal/prayer pleading; covered under Prayer/Justice
    "plowshare":                {"status": "skip"},   # nave=3; agricultural tool; incidental
    "plummet":                  {"status": "skip"},   # nave=4; measuring tool; covered under Plumb Line/Judgment
    "poll-tax":                 {"status": "skip"},   # nave=0; covered under Tribute/Tax
    "popular-sins":             {"status": "skip"},   # nave=1; single verse; covered under Sin topics
    "popularity":               {"status": "skip"},   # nave=4; too narrow; incidental
    "porcius":                  {"status": "skip"},   # nave=0; minor Roman official; no verse content
    "precepts":                 {"status": "skip"},   # nave=0; covered under Commandments/Law
    "presbyter":                {"status": "skip"},   # nave=0; covered under Elder/Church Office
    "prescience":               {"status": "skip"},   # nave=0; covered under Foreknowledge/Omniscience
    "princesses":               {"status": "skip"},   # nave=2; too few verses; covered under Royalty
    "privilege":                {"status": "skip"},   # nave=0; covered under Election/Grace
    "proclamation":             {"status": "skip"},   # nave=11; generic; covered under Preaching/Prophecy
}


def main():
    gaps = load_gaps()
    idx = {g['id']: g for g in gaps}
    updated = 0
    for gid, decision in DECISIONS.items():
        if gid in idx:
            idx[gid].update(decision)
            updated += 1
        else:
            print(f'WARNING: gap id {gid!r} not found in gaps.json')
    save_gaps(list(idx.values()))
    stubs = sum(1 for d in DECISIONS.values() if d['status'] == 'stub-needed')
    redirects = sum(1 for d in DECISIONS.values() if d['status'] == 'redirect-only')
    skips = sum(1 for d in DECISIONS.values() if d['status'] == 'skip')
    print(f'BPG Curation C78: updated {updated} gaps.')
    print(f'  stub-needed={stubs}  redirect-only={redirects}  skip={skips}')


if __name__ == '__main__':
    main()
