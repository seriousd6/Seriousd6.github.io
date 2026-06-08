"""
MKT Christ Commentary — Isaiah chapter 16
Run: python3 scripts/zc-christ-isaiah-16.py

Source data used:
- data/interlinear/isaiah.json
- data/translation/draft/mediating/isaiah.json

Key decisions in this range:
- vv. 4b-5: the messianic core — throne established in ḥesed in the tent of David
- v. 1: lamb/tribute motif — type pointing to Christ as Lamb and King
- vv. 9,11: divine mourning over Moab — theme of God's compassion on enemies
- v. 12: false worship fails — only Christ as true mediator prevails
"""
import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_comm(source, book):
    p = ROOT / 'data' / 'commentary' / source / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_comm(source, book, data):
    p = ROOT / 'data' / 'commentary' / source / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_comm(existing, new_data):
    # INTENT: Non-destructive merge — existing entries are never overwritten, safe to re-run
    for ch, verses in new_data.items():
        if ch not in existing: existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]: existing[ch][v] = html

ISAIAH = {
"16": {
"1": "<p>A type: Moab is called to send the tribute-lamb (<em>seh mōšēl 'āreṣ</em> — the lamb of the ruler of the land) to the mount of the daughter of Zion. The lamb as tribute to the Davidic king in Zion anticipates Christ, who is simultaneously the Lamb (Rev 5:6) and the Davidic King who rules from Zion. What Moab is called to send becomes the very thing YHWH provides — his own lamb (Gen 22:8; John 1:29). The nations bringing tribute to the enthroned King is a recurring eschatological theme (Ps 72:10; Isa 60:6).</p>",
"2": "<p>A revelation of God: Moab in flight like a scattered flock — the instability and vulnerability of nations that refuse to submit to Zion's ruler. The scattered-bird image is the anti-type of the gathering promised in Isaiah 11:12; those who gather to the messianic banner find security, while those who flee from it find only rootlessness. This verse establishes the necessity of the political submission that vv. 4-5 will define in messianic terms.</p>",
"3": "<p>A theme: Zion is called to give shade and shelter to the fugitive — <em>hābî'î 'ēṣāh 'ăśî mišpāṭ</em> — give counsel, grant justice, make your shade like night at noon. The shelter of Zion from the destroyer is a messianic function: Christ is the one who shelters the fugitive (Heb 6:18 — we who flee to him for refuge). The shade at midday in the burning heat is an image of divine protection (Ps 121:6; Rev 7:16: the sun will not strike them).</p>",
"4": "<p>A theme: the outcasts of Moab sheltered in Zion from the destroyer. The word <em>nādîm</em> (outcasts, the driven-away) are received, not expelled. This is the grace that runs counter to the ancient enmity between Israel and Moab — the same grace that the book of Ruth narratively demonstrates and that Paul proclaims: in Christ there is neither Jew nor Gentile, no outcast category that excludes from refuge (Rom 10:12-13). The condition given in v. 4b: this will be possible once the oppressor is removed.</p>",
"5": "<p>A direct prophecy. When the oppressor vanishes, <em>wĕhûkān bĕḥèsed kissē'</em> — <em>a throne shall be established in steadfast love</em> — and on it shall sit in faithfulness in the tent of David (<em>bĕ'ōhel dāwid</em>) one who <em>judges and seeks justice and is swift in righteousness</em>. This is the messianic core embedded in the Moab oracle: the Davidic king whose throne is constituted by <em>ḥesed</em> (covenant love) and <em>'emet</em> (faithfulness), who actively seeks justice. Luke 1:32-33 (throne of David; kingdom without end) and Revelation 4:2 (the established throne) both draw on this tradition. Christ is the king whose ḥesed-throne is the ground of all shelter for the outcast.</p>",
"6": "<p>A revelation of God: Moab's pride (<em>gē'āh... gā'ôn... gĕ'ûtô... 'ebrātô</em> — the fourfold pride) is the ground of his destruction. The anti-type of the humble messianic King of v. 5 (who sits not in pride but in ḥesed) is Moab's boastful arrogance. This contrast — between the enthroned King of ḥesed and the proud nation that refuses him — runs through the NT's theology of the cross: God chose what is foolish and weak to shame the proud (1 Cor 1:27-28).</p>",
"7": "<p>A revelation of God: Moab must wail for itself. The self-referential lament (<em>lāk̠ēn yĕyêlîl mō'āb</em>) describes a judgment that the nation brings upon itself — the internal logic of divine justice rendering to each what they have chosen. The NT framing: those who choose pride over the ḥesed-throne face the same trajectory — divine justice that confirms the choice already made.</p>",
"8": "<p>A revelation of God: the vine of Sibmah and the fields of Heshbon languish — agricultural collapse as the concrete sign of covenant judgment. This verse does not directly anticipate Christ, but establishes the creation-theology context: sin destroys the fruitfulness YHWH intended, while Christ's redemption restores it (Rom 8:19-22; the vineyard parable of John 15 frames Christ himself as the true vine that produces what Moab's vines cannot).</p>",
"9": "<p>A theme: the prophet weeps with the weeping of Jazer over Moab's destroyed vine — <em>'al-kēn 'eb̠keh bĕb̠ekî ya'zēr gèpen śib̠māh</em>. This is divine solidarity with human grief, even grief over an enemy nation's judgment. Jesus wept over Jerusalem (Luke 19:41) in precisely the same pattern: grief for those facing a judgment they have brought on themselves. The God of Israel mourns what he must judge — a tension resolved at the cross where Christ bears the judgment he mourns.</p>",
"10": "<p>A revelation of God: joy and gladness removed from the fruitful field — the vintage silenced, the treaders no longer treading with a shout. This removal of harvest joy is the covenant curse (Lev 26:20; Deut 28:30-40). Christ's work reverses this curse: he is the one who trampled the winepress alone (Isa 63:3; Rev 19:15), so that the covenant curse is absorbed and the harvest joy of the new creation can resume.</p>",
"11": "<p>A theme: the divine inward parts (<em>mê'ay</em> — entrails, the seat of deep emotion) moan like a lyre for Moab. This is the most explicit statement in the Moab oracle of YHWH's personal grief over the enemy nation he must judge. Christ embodies this grief — he looked over Jerusalem and wept (Luke 19:41), he was moved with compassion for the crowds (Matt 9:36), he prays for those who crucify him (Luke 23:34). The weeping God of Isaiah 16 is fully present in the weeping Son of God.</p>",
"12": "<p>A revelation of God: Moab wearies itself at the high place, comes to his sanctuary to pray, but does not prevail (<em>wĕlō' yûk̠āl</em>). False worship directed toward false gods — or toward YHWH through illicit means — cannot prevail. Christ as the one mediator (1 Tim 2:5) is the counterpart: through him alone do prayers prevail (John 16:23-24; Heb 4:16). Moab's futile sanctuary-approach points to the need for the true high priest who enters the true sanctuary (Heb 9:24).</p>",
"13": "<p>A revelation of God: the oracle concerning Moab was spoken in the past — YHWH's word has a track record of fulfillment, and the prophetic word spoken here now has its own trajectory of completion. The reliability of prophetic word establishes the ground for trusting the messianic prophecies: the same God who precisely announced Moab's judgment announces the Davidic throne of ḥesed (v. 5) with equal certainty.</p>",
"14": "<p>A revelation of God: in three years, like the years of a hired worker, Moab's glory will be contemptible and its remnant tiny and feeble. The divine time-constraint on judgment — three years — shows that YHWH's patience is not indefinite; judgment comes on the appointed schedule. This establishes the theological framework for Christ's <em>in the fullness of time</em> (Gal 4:4) — God operates on a precise temporal calendar, and the messianic throne of v. 5 arrives on that same schedule.</p>"
}
}

def main():
    existing = load_comm('mkt-christ', 'isaiah')
    merge_comm(existing, ISAIAH)
    save_comm('mkt-christ', 'isaiah', existing)
    v = sum(len(vs) for vs in ISAIAH.values())
    print(f'Isaiah 16 mkt-christ: {v} verses written.')

if __name__ == '__main__':
    main()
