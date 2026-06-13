"""
BPG Curation — Batch C05: linus → sharon
Gaps reviewed: 100 (gaps 401–500 by priority score)

Priority 35 range: smith-person/smith-place entries, L–S names.
All have 0 Nave verse count.

Notable decisions:
  - linus: bishop of Rome named in 2 Tim 4:21; early church tradition → stub-needed.
  - milcom: Ammonite deity Solomon worshipped (1 Kgs 11:5,33) → stub-needed.
  - prochorus: one of the seven deacons (Acts 6:5) → stub-needed.
  - ramah: prophetic city; Rachel weeping (Jer 31:15 / Matt 2:18) → stub-needed.
  - sanhedrin: Jewish ruling council; tried Jesus and Paul → stub-needed.
  - shalmaneser: Assyrian king who deported northern Israel (2 Kgs 17) → stub-needed.
  - Eleven redirects: Greek/variant spellings to their canonical Easton articles.

Script: scripts/bpg-curate-05.py
Run: python3 scripts/bpg-curate-05.py  (from project root)
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
    # ── L names ──────────────────────────────────────────────────────────────
    # Bishop of Rome; named alongside Paul in 2 Tim 4:21; earliest post-apostolic tradition
    "linus":         {"status": "stub-needed"},
    # Claudius Lysias, the tribune who rescued Paul (Acts 21:31–23:30); Easton has lysias-claudius
    "lysias":        {"status": "redirect-only", "redirect_to": "lysias-claudius"},
    "lysimachus":    {"status": "names-only"},   # translator of LXX Esther (Esth 11:1 LXX)

    # ── M names ──────────────────────────────────────────────────────────────
    "maadiah":       {"status": "names-only"},   # priest (Neh 12:5)
    "maai":          {"status": "names-only"},   # Levite musician (Neh 12:36)
    "machi":         {"status": "names-only"},   # father of spy Geuel (Num 13:15)
    "machnadebai":   {"status": "names-only"},   # post-exile man (Ezra 10:40)
    # Greek/Latin form of Midian; Easton has midian.json
    "madian":        {"status": "redirect-only", "redirect_to": "midian"},
    "magbish":       {"status": "names-only"},   # returned-exile family (Ezra 2:30)
    "magdiel":       {"status": "names-only"},   # Edomite chief (Gen 36:43)
    "magpiash":      {"status": "names-only"},   # covenant signer (Neh 10:20)
    "mahalah":       {"status": "names-only"},   # daughter of Hammoleketh (1 Chr 7:18)
    "mahali":        {"status": "names-only"},   # son of Merari (Exod 6:19); variant of Mahli
    "maharai":       {"status": "names-only"},   # one of David's thirty warriors (2 Sam 23:28)
    "marsena":       {"status": "names-only"},   # Persian noble (Esth 1:14)
    "matred":        {"status": "names-only"},   # mother of Mehetabel (Gen 36:39)
    "matri":         {"status": "names-only"},   # Benjaminite clan of Saul (1 Sam 10:21)
    "mehida":        {"status": "names-only"},   # post-exile temple servant family (Ezra 2:52)
    "mehir":         {"status": "names-only"},   # Judah descendant (1 Chr 4:11)
    "melatiah":      {"status": "names-only"},   # wall builder (Neh 3:7)
    "melchiah":      {"status": "names-only"},   # several minor OT figures
    "melchishua":    {"status": "names-only"},   # son of Saul (1 Sam 14:49); died at Gilboa
    "menan":         {"status": "names-only"},   # NT genealogy (Luke 3:31)
    "meunim":        {"status": "names-only"},   # post-exile temple servant family (Ezra 2:50)
    "mijamin":       {"status": "names-only"},   # several minor OT figures (Neh 10:7; Ezra 10:25)
    "milalai":       {"status": "names-only"},   # Levite musician (Neh 12:36)
    "milcah":        {"status": "names-only"},   # daughter of Zelophehad (Num 26:33); wife of Nahor (Gen 11:29)
    # Ammonite deity that Solomon built a high place for (1 Kgs 11:5,33; 2 Kgs 23:13)
    "milcom":        {"status": "stub-needed"},
    "miniamin":      {"status": "names-only"},   # several OT figures (2 Chr 31:15; Neh 12:17)
    "molid":         {"status": "names-only"},   # Jerahmeel's son (1 Chr 2:29)
    "moserah":       {"status": "names-only"},   # wilderness camp (Num 33:30; Deut 10:6)
    "muppim":        {"status": "names-only"},   # son of Benjamin (Gen 46:21)

    # ── N names ──────────────────────────────────────────────────────────────
    # Greek form of Nahor used in NT genealogy (Luke 3:34); Easton has nahor.json
    "nachor":        {"status": "redirect-only", "redirect_to": "nahor"},
    "naham":         {"status": "names-only"},   # brother of Hodiah (1 Chr 4:19)
    "nathanmelech":  {"status": "names-only"},   # official in Josiah's reform (2 Kgs 23:11)
    "naum":          {"status": "names-only"},   # NT genealogy (Luke 3:25)
    "neariah":       {"status": "names-only"},   # two OT figures (1 Chr 3:22; 4:42)
    "nebai":         {"status": "names-only"},   # covenant signer (Neh 10:19)
    "nehum":         {"status": "names-only"},   # post-exile leader (Neh 7:7)
    "nekoda":        {"status": "names-only"},   # post-exile families (Ezra 2:48,60)
    "nepheg":        {"status": "names-only"},   # two OT figures (Exod 6:21; 2 Sam 5:15)
    # Greek NT form of Naphtali (Matt 4:13,15; Rev 7:6); Easton has naphtali.json
    "nephthalim":    {"status": "redirect-only", "redirect_to": "naphtali"},
    "neri":          {"status": "names-only"},   # NT genealogy (Luke 3:27); grandfather of Zerubbabel
    "neriah":        {"status": "names-only"},   # father of Baruch and Seraiah (Jer 32:12)
    # Variant of Nun (Joshua's father); Easton has nun.json
    "non":           {"status": "redirect-only", "redirect_to": "nun"},

    # ── O names ──────────────────────────────────────────────────────────────
    "ocran":         {"status": "names-only"},   # father of Asher's tribal leader (Num 1:13)
    "onam":          {"status": "names-only"},   # two OT figures (Gen 36:23; 1 Chr 2:26)
    # Original name of Joshua before Moses renamed him (Num 13:8,16); Easton has joshua.json
    "oshea":         {"status": "redirect-only", "redirect_to": "joshua"},

    # ── P names ──────────────────────────────────────────────────────────────
    "padon":         {"status": "names-only"},   # post-exile temple servant (Ezra 2:44)
    "pai":           {"status": "names-only"},   # capital of Edomite king Hadar (1 Chr 1:50)
    "paseah":        {"status": "names-only"},   # three OT figures (1 Chr 4:12; Ezra 2:49; Neh 3:6)
    "pelaliah":      {"status": "names-only"},   # Levite helper of Ezra (Neh 8:7)
    # Place where Jacob wrestled with God and received the name Israel (Gen 32:30); Easton has penuel.json
    "peniel":        {"status": "redirect-only", "redirect_to": "penuel"},
    "peninnah":      {"status": "names-only"},   # Hannah's rival wife (1 Sam 1:2); narrative centres on Hannah
    "peresh":        {"status": "names-only"},   # son of Machir (1 Chr 7:16)
    "philologus":    {"status": "names-only"},   # Roman Christian greeted by Paul (Rom 16:15)
    "phurah":        {"status": "names-only"},   # Gideon's servant who accompanied him to Midianite camp (Judg 7:10)
    "pinon":         {"status": "names-only"},   # Edomite chief (Gen 36:41)
    "pithon":        {"status": "names-only"},   # Saul's descendant (1 Chr 8:35)
    "poratha":       {"status": "names-only"},   # Haman's son (Esth 9:8)
    # One of the seven original deacons chosen in Acts 6:5; a founding figure of the diaconate
    "prochorus":     {"status": "stub-needed"},
    "punon":         {"status": "names-only"},   # wilderness camp (Num 33:42)
    "putiel":        {"status": "names-only"},   # father-in-law of Eleazar (Exod 6:25)

    # ── R names ──────────────────────────────────────────────────────────────
    "raddai":        {"status": "names-only"},   # David's brother (1 Chr 2:14)
    # NT form of Reu (Luke 3:35); Easton has serug.json but not ragau; treat as genealogy
    "ragau":         {"status": "names-only"},
    # City of Benjamin/Ephraim; Rachel weeping here (Jer 31:15 / Matt 2:18); Samuel's hometown
    "ramah":         {"status": "stub-needed"},
    "ramiah":        {"status": "names-only"},   # post-exile man (Ezra 10:25)
    "reaiah":        {"status": "names-only"},   # three OT figures (1 Chr 4:2; 5:5; Ezra 2:47)
    "reelaiah":      {"status": "names-only"},   # post-exile leader (Ezra 2:2)
    "regem":         {"status": "names-only"},   # Judah descendant (1 Chr 2:47)
    "remmon":        {"status": "names-only"},   # variant of Rimmon; single border mention (Josh 19:7)
    "rephaiah":      {"status": "names-only"},   # five minor OT figures
    "reu":           {"status": "names-only"},   # son of Peleg; ancestor of Abraham (Gen 11:18)
    "reumah":        {"status": "names-only"},   # Nahor's concubine (Gen 22:24)
    "rinnah":        {"status": "names-only"},   # Judah descendant (1 Chr 4:20)
    "rohgah":        {"status": "names-only"},   # Asher descendant (1 Chr 7:34)

    # ── S names ──────────────────────────────────────────────────────────────
    "sacar":         {"status": "names-only"},   # two OT figures (1 Chr 11:35; 26:4)
    "samlah":        {"status": "names-only"},   # Edomite king (Gen 36:36)
    # Jewish supreme council (71 members) that tried Jesus (Matt 26:59) and Paul (Acts 23)
    "sanhedrin":     {"status": "stub-needed"},
    "sarid":         {"status": "names-only"},   # Zebulun border town (Josh 19:10)
    # Greek form of Sharon; Easton has sharon-saron.json
    "saron":         {"status": "redirect-only", "redirect_to": "sharon-saron"},
    "sarsechim":     {"status": "names-only"},   # Babylonian official at Jerusalem's fall (Jer 39:3)
    # Greek form of Serug (Luke 3:35); Easton has serug.json
    "saruch":        {"status": "redirect-only", "redirect_to": "serug"},
    "seled":         {"status": "names-only"},   # Jerahmeel's son (1 Chr 2:30)
    # Greek/NT form of Shem (Luke 3:36); Easton has shem.json
    "sem":           {"status": "redirect-only", "redirect_to": "shem"},
    "semachiah":     {"status": "names-only"},   # Obed-edom's son, gatekeeper (1 Chr 26:7)
    "shachia":       {"status": "names-only"},   # Benjamin descendant (1 Chr 8:10)
    "shalmai":       {"status": "names-only"},   # post-exile temple servant (Neh 7:48)
    # Assyrian king Shalmaneser V who besieged Samaria 725–722 BC (2 Kgs 17:3; 18:9)
    "shalmaneser":   {"status": "stub-needed"},
    "shamariah":     {"status": "names-only"},   # son of Rehoboam (2 Chr 11:19)
    "shamed":        {"status": "names-only"},   # Zebulun descendant (1 Chr 8:12)
    "shamer":        {"status": "names-only"},   # two OT figures (1 Chr 6:46; 7:34)
    "shamhuth":      {"status": "names-only"},   # one of David's monthly commanders (1 Chr 27:8)
    "shammai":       {"status": "names-only"},   # three OT figures in Judah genealogy
    "shammoth":      {"status": "names-only"},   # one of David's mighty men (1 Chr 11:27)
    "shamsherai":    {"status": "names-only"},   # Benjamin descendant (1 Chr 8:26)
    "shapham":       {"status": "names-only"},   # Gad leader (1 Chr 5:12)
    "sharai":        {"status": "names-only"},   # post-exile man (Ezra 10:40)
    "sharar":        {"status": "names-only"},   # father of David's warrior Ahiam (2 Sam 23:33)
    # Plain of Sharon; Easton has sharon-saron.json
    "sharon":        {"status": "redirect-only", "redirect_to": "sharon-saron"},
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
    print(f'BPG Curation C05: updated {updated} / {len(DECISIONS)} gaps.')
    counts = {}
    for d in DECISIONS.values():
        counts[d['status']] = counts.get(d['status'], 0) + 1
    for status, n in sorted(counts.items()):
        print(f'  {status}: {n}')


if __name__ == '__main__':
    main()
