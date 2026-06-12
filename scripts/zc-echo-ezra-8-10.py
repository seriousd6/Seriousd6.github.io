"""
MKT Echo Layer — Ezra chapters 8–10
Run: python3 scripts/zc-echo-ezra-8-10.py

Ch8: Ashamed to ask for military escort — trusting YHWH rather than worldly power (8:22) — 2 Cor 1:9; Matt 6:25-33
     Sacred vessels carried by consecrated bearers (8:28-29) — 2 Cor 4:7; 1 Pet 2:9
Ch9: Ezra's penitential confession — the grammar of communal repentance before God (9:6-9) — Rom 3:10-12; 1 John 1:9
     A little reviving in the midst of bondage (9:8) — 2 Cor 4:8; Rom 5:20
     God's punishment less than iniquities deserved (9:13) — Rom 3:24-26
Ch10: Weeping assembly before God's house — mass repentance as covenant renewal (10:1) — Luke 15:7; Acts 2:37
      Separate yourselves from the peoples (10:11) — 2 Cor 6:17 (citing Isa 52:11)
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

ECHOES = {
  "8": {
    "22": [
      {"type": "allusion", "target": "2 Cor 1:9", "note": "Ezra was ashamed to ask the king for soldiers and horsemen to protect the caravan, because he had declared to the king: 'The hand of our God is favorable to all who seek him, but his power and his wrath are against all who forsake him.' The prior public testimony precluded requesting armed guards — doing so would have contradicted the claim Ezra had already made. 2 Corinthians 1:9: 'we had the sentence of death within ourselves so that we would not trust in ourselves but in God who raises the dead.' Paul and Ezra share the same posture: the acknowledged impossibility of self-protection becomes the condition for the revelation of divine protection. The hand-of-God formula appears nine times in Ezra-Nehemiah as the phrase for divine providential care."},
      {"type": "allusion", "target": "Matt 6:25", "note": "Ezra's refusal to seek military escort is a practical enactment of 'seek first the kingdom of God and his righteousness, and all these things will be added to you' — trusting YHWH's protective hand rather than adding human security measures to divine promise. Ezra verbally committed to divine protection before the king, then acted consistently with that testimony by fasting and seeking YHWH for the journey. Jesus's teaching on non-anxiety (Matt 6:25-33) rests on the same covenant premise: the Father who provides for birds and flowers provides for those who seek his kingdom."}
    ],
    "28": [
      {"type": "allusion", "target": "2 Cor 4:7", "note": "Ezra declared the vessels holy to YHWH and the priests set apart to carry them: 'Watch and keep them until you weigh them before the chief priests.' The consecrated people carrying consecrated vessels — the vessel-bearer principle. 2 Corinthians 4:7: 'we have this treasure in jars of clay, to show that the surpassing power belongs to God and not to us.' The NT extends the principle: the apostles are the new Levitical carriers of divine glory, vulnerable human containers of indestructible heavenly content."},
      {"type": "allusion", "target": "1 Pet 2:9", "note": "The priests set apart as holy carriers of YHWH's consecrated silver and gold — their own consecrated status qualifying them for the holy transport. Peter's application of the priestly vocabulary to the whole church (1 Pet 2:9: 'a royal priesthood, a holy nation, a people for his own possession') draws on this tradition: all believers are consecrated bearers of divine treasure, set apart to declare the excellencies of him who called them."}
    ]
  },
  "9": {
    "6": [
      {"type": "allusion", "target": "Rom 3:10", "note": "Ezra's great confession: 'O my God, I am ashamed and blush to lift my face to you, my God, for our iniquities have risen higher than our heads, and our guilt has mounted up to the heavens.' The image of iniquity towering over the one who should be its judge is the personal-representative form of the comprehensive indictment Paul draws from the Psalms in Rom 3:10-18: 'None is righteous, no, not one.' Ezra identifies with the corporate guilt of the community though not personally guilty of the intermarriage — the representative-confession structure that Christ fulfills by bearing the guilt he did not incur."},
      {"type": "allusion", "target": "1 John 1:9", "note": "Ezra's confession is the OT paradigm of the covenant structure of confession and forgiveness: he speaks the iniquity openly and fully before God without minimizing it. 1 John 1:9: 'If we confess our sins, he is faithful and just to forgive us our sins and to cleanse us from all unrighteousness.' Ezra's prayer — total transparency, naming the sin, acknowledging the justice of the punishment, asking nothing but the continuance of grace — is the OT form of the confessional pattern the NT makes the basis of ongoing fellowship with God."}
    ],
    "8": [
      {"type": "allusion", "target": "2 Cor 4:8", "note": "'But now for a brief moment favor has been shown by the LORD our God, to leave us a remnant and to give us a secure hold within his holy place' — partial preservation in the midst of deserved judgment. The regaʿ qāṭān (brief moment) of divine grace producing a remnant is the OT form of what Paul describes in 2 Cor 4:8-9: 'afflicted in every way, but not crushed; perplexed, but not driven to despair; persecuted, but not forsaken; struck down, but not destroyed.' The not-yet-destroyed remnant in Ezra is the OT's own 'not crushed' — the thread of grace that runs through judgment."},
      {"type": "allusion", "target": "Rom 5:20", "note": "'Grace has been shown us by the LORD our God' in the context of a community whose sin of intermarriage echoes the very sin that brought the exile — grace appearing exactly where another judgment would be most expected. Romans 5:20: 'where sin increased, grace abounded all the more.' The pattern in Ezra is the OT instantiation: the post-exilic community is already on borrowed covenant time, yet YHWH's grace continues to appear at the junctions of greatest guilt."}
    ],
    "13": [
      {"type": "allusion", "target": "Rom 3:24", "note": "'After all that has come upon us for our evil deeds and for our great guilt, seeing that you, our God, have punished us less than our iniquities deserved...' — the explicit statement that YHWH's actual judgment was mitigated relative to the deserved sentence. This mitigation is the OT's own recognition of divine forbearance, which Paul addresses in Rom 3:24-26: God 'passed over former sins in his divine forbearance' — a forbearance that looked forward to the cross where what was left unpunished in the OT would be paid in full through Christ's sacrifice. Ezra's gratitude for under-punishment is gratitude for what the cross will eventually justify."}
    ]
  },
  "10": {
    "1": [
      {"type": "allusion", "target": "Luke 15:7", "note": "As Ezra prayed and confessed, weeping and casting himself down before the house of God, a very great assembly of men, women, and children gathered from Israel and the people wept bitterly. The mass weeping before God's house in response to one man's prostrate confession is the OT form of communal repentance. Luke 15:7: 'there will be more joy in heaven over one sinner who repents than over ninety-nine righteous persons who need no repentance.' The assembly's collective repentance — gathered by Ezra's personal confession — anticipates the Pentecost scene: Acts 2:37 'they were cut to the heart and said... Brothers, what shall we do?'"},
      {"type": "allusion", "target": "Acts 2:37", "note": "The great weeping assembly before the house of God — gathered by Ezra's public confession — echoes forward to Acts 2:37: 'When they heard this, they were cut to the heart and said to Peter and the rest of the apostles, Brothers, what shall we do?' Both scenes feature a community whose sin has been declared publicly, who weep collectively, and who ask what must be done. The structure of corporate conviction leading to the question of covenant obligation is the same — though the answer differs: in Ezra, dissolution of foreign marriages; at Pentecost, baptism into Christ."}
    ],
    "11": [
      {"type": "allusion", "target": "2 Cor 6:17", "note": "'Make confession to the LORD, the God of your fathers, and do his will. Separate yourselves from the peoples of the land and from the foreign wives.' The separation-call that concludes Ezra's covenant-renewal assembly. 2 Corinthians 6:17 cites Isaiah 52:11 — 'go out from their midst, and be separate from them, says the Lord' — in the context of warning against unequal yokes with unbelievers. The Ezra context is the OT instantiation of the same principle: covenant identity requires distinguishing boundaries. The NT form is not ethnic but relational-to-idolatry — separation from the values and allegiances of the surrounding culture, not from the people themselves (cf. 1 Cor 5:10)."}
    ]
  }
}

def main():
    e = load_echo('ezra')
    merge_echo(e, ECHOES)
    save_echo('ezra', e)
    count = sum(len(v) for v in ECHOES.values())
    print(f'ezra echo: wrote entries for {count} verses across ch 8-10')

if __name__ == '__main__':
    main()
