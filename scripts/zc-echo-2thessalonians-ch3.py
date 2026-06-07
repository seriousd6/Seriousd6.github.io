"""
echo layer — 2 Thessalonians chapter 3 (fills missing ch3)
Output: data/echoes/2thessalonians.json
Run: python3 scripts/zc-echo-2thessalonians-ch3.py
"""
import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    return json.loads(p.read_text()) if p.exists() else {}

def save_echo(book, data):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_echo(existing, new_data):
    # INTENT: Merge echo entries without overwriting existing verse keys — safe to re-run.
    # CHANGE? If echo JSON structure changes from {ch:{v:[entries]}}, update traversal.
    # VERIFY: Re-running produces identical output; existing entries preserved.
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, entries in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = entries
            else:
                seen = {(e['type'], e['target']) for e in existing[ch][v]}
                for e in entries:
                    if (e['type'], e['target']) not in seen:
                        existing[ch][v].append(e)
                        seen.add((e['type'], e['target']))

NEW_ECHOES = {
  "3": {
    "1": [
      {"type": "allusion", "target": "Ps 147:15", "note": "Pray that the word of the Lord may speed ahead (trechō — run swiftly) — Psalm 147:15 describes YHWH's word running swiftly (LXX: ho logos autou trechei tacheōs); Paul's prayer-request applies the same swift-running to the gospel's progress, casting the word's spread as YHWH's dynamic, unstoppable speech-act"},
      {"type": "allusion", "target": "Isa 55:11", "note": "That the word of the Lord may be honored (doxazō) — Isaiah 55:11 promises that YHWH's word shall not return empty but will accomplish its purpose; Paul's prayer for the word's honor and speed draws on the same prophetic confidence that God's speech achieves its goal"}
    ],
    "3": [
      {"type": "allusion", "target": "Deut 7:9", "note": "The Lord is faithful (pistos de estin ho kyrios) — Deuteronomy's foundational declaration of YHWH as the faithful God who keeps covenant (Deut 7:9: YHWH your God is God, the faithful God who keeps covenant and steadfast love) is applied to the Lord Jesus; faithfulness is a divine attribute now predicated of Christ"},
      {"type": "allusion", "target": "Ps 121:7", "note": "He will establish you and guard you against the evil one — Psalm 121:7 (the LORD will keep you from all evil; he will keep your life) provides the OT assurance of divine protection that Paul adapts for the eschatological context of the evil one (ho ponēros) identified in v.3"}
    ],
    "5": [
      {"type": "allusion", "target": "1 Chr 29:18", "note": "May the Lord direct your hearts to the love of God and to the steadfastness of Christ — David's prayer in 1 Chronicles 29:18 (O LORD God, keep forever such purposes and thoughts in the hearts of your people, and direct their hearts toward you) provides the OT template for the apostolic heart-directing prayer; Paul applies it to the new covenant community with the specifically christological targets of God's love and Christ's endurance"}
    ],
    "10": [
      {"type": "allusion", "target": "Gen 3:19", "note": "If anyone is not willing to work, let him not eat — the creation ordinance of labor (Gen 3:19: by the sweat of your face you shall eat bread) grounds the work-ethic Paul enforces; the idleness of the ataktoi (disorderly ones, possibly those so expectant of the parousia they stopped working) violates the creation order of labor before sustenance"},
      {"type": "allusion", "target": "Prov 19:15", "note": "Sloth casts into a deep sleep, and an idle person will suffer hunger (Prov 19:15); the Proverbs tradition of the sluggard (atsēl) who does not work and therefore does not eat provides the wisdom background for Paul's dominical-style maxim"}
    ],
    "14": [
      {"type": "allusion", "target": "Lev 19:17", "note": "Do not regard him as an enemy, but warn him as a brother — Leviticus 19:17 (you shall not hate your brother in your heart, but you shall reason frankly with your neighbor) provides the OT grounding for Paul's community-discipline procedure: the goal is fraternal correction, not adversarial exclusion; the limit of shunning is defined by the continuing obligation to treat the disciplined person as a brother"}
    ],
    "16": [
      {"type": "allusion", "target": "Num 6:24-26", "note": "Now may the Lord of peace himself give you peace at all times in every way — the Aaronic benediction (Num 6:24-26: the LORD bless you and keep you; the LORD make his face shine on you and be gracious to you; the LORD lift up his countenance upon you and give you peace) is the OT template for Paul's peace-benediction; the LORD of peace (kyrios tēs eirēnēs) applies the Aaronic divine-peace formula to the Lord Jesus in the letter's closing"},
      {"type": "allusion", "target": "Judg 6:24", "note": "YHWH Shalom — Gideon's altar-name (Judg 6:24: he called it The LORD is Peace) is the OT name for the peace-giving God; Paul's address of the Lord as the Lord of peace echoes this divine-peace name in the letter's benediction"}
    ],
    "17": [
      {"type": "allusion", "target": "Gal 6:11", "note": "I, Paul, write this greeting with my own hand. This is the sign of genuineness in every letter of mine — Galatians 6:11 (see with what large letters I am writing to you with my own hand) establishes Paul's autograph as his authentication signature; the explicit notice here makes this practice into a cross-letter security protocol against the forged letter mentioned in 2:2 (a letter seeming to be from us)"},
      {"type": "allusion", "target": "1 Cor 16:21", "note": "The Pauline autograph appears in 1 Cor 16:21 (I, Paul, write this greeting with my own hand), Col 4:18, and Phm 19, forming a consistent intra-Pauline corpus pattern; 2 Thess 3:17 makes the pattern explicit by calling it the sign in every letter, situating this letter within a recognized letter-series"}
    ]
  }
}

if __name__ == '__main__':
    existing = load_echo('2thessalonians')
    merge_echo(existing, NEW_ECHOES)
    save_echo('2thessalonians', existing)
    for ch in ['1', '2', '3']:
        print(f'  ch {ch}: {len(existing.get(ch, {}))} verses with echoes')
