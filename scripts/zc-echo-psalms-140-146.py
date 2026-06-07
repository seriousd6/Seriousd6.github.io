"""
Echo data — Psalms chapters 140–146 (gap-fill: chs 141–146 missing; 140 already present)
Run: python3 scripts/zc-echo-psalms-140-146.py

Key connections across the late Davidic lament-to-praise sequence:
- Ps 141:2: "May my prayer be set before you like incense; may the lifting up of my
  hands be like the evening sacrifice" → Rev 5:8 / 8:3-4 (golden bowls of incense
  = prayers of the saints; the heavenly liturgy fulfills the evening offering).
- Ps 141:3: "Set a guard over my mouth, O LORD" → Jas 3:6-10 (the tongue is a fire;
  the NT's sustained treatment of speech-ethics).
- Ps 142:4: "No one is concerned for me; I have no refuge; no one cares for my life"
  → Heb 4:15 (Christ not unable to sympathize with our weakness; he entered every
  desolation Psalm 142 describes).
- Ps 143:2: "Do not bring your servant into judgment, for no one living is righteous
  before you" → Rom 3:20 (no one will be declared righteous in God's sight by the
  works of the law) — Paul quotes this verse in Romans.
- Ps 143:10: "Teach me to do your will, for you are my God; may your good Spirit lead
  me on level ground" → Rom 8:14 (those who are led by the Spirit of God are children
  of God) / Gal 5:18.
- Ps 144:3: "What are human beings that you care for them?" → Heb 2:6-8 (Ps 8 applied
  to Christ; the one who is truly human fulfills this lowly dignity).
- Ps 145:13: "Your kingdom is an everlasting kingdom; your dominion endures through
  all generations" → Rev 11:15 (the kingdom of the world has become the kingdom of
  our Lord and of his Messiah).
- Ps 146:6-7: "The Maker of heaven and earth... upholds the cause of the oppressed,
  gives food to the hungry" → Luke 4:18 (the Nazareth manifesto: good news to the
  poor, release to captives — Jesus enacts the program Ps 146 attributes to God).
- Ps 146:9: "The LORD watches over the foreigner and sustains the fatherless" →
  Jas 1:27 (pure religion: caring for orphans and widows in their distress).
"""

import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def load_echo(book):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save_echo(book, data):
    p = ROOT / 'data' / 'echoes' / f'{book}.json'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_echo(existing, new_data):
    """Merge echo entries; deduplicate by (type, target) within each verse."""
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

# INTENT: Echo data for Psalms 141–146 — late lament-to-praise sequence ending in
#   the Hallelujah psalms; key connections: prayer-as-incense fulfilled in heavenly
#   liturgy (Ps 141:2 → Rev 8:3), Paul's direct citation of Ps 143:2 in Rom 3:20
#   (no one righteous before God), Christ entering the desolation of Ps 142 (Heb 4:15),
#   and the program of Ps 146 (care for oppressed/hungry/foreigner) enacted in Jesus'
#   Nazareth manifesto (Luke 4:18).
# CHANGE? If data/echoes/psalms.json structure changes, update load_echo/save_echo
#   per Z_COMMENTARY_SCRIPT_GUIDE.md.
# VERIFY: python3 -c "import json; d=json.load(open('data/echoes/psalms.json')); print([len(d.get(str(c),{})) for c in range(141,147)])" should show non-zero for all six.

PSALMS_ECHOES = {
  "141": {
    "2": [
      {
        "type": "fulfillment",
        "target": "Rev 8:3",
        "note": "May my prayer be set before you like incense; may the lifting up of my hands be like the evening sacrifice — 'another angel, who had a golden censer, came and stood at the altar. He was given much incense to offer, with the prayers of all God's people, on the golden altar in front of the throne' (Rev 8:3-4). Psalm 141:2's prayer-as-incense is not just a metaphor — it is the image Revelation uses for the heavenly liturgy. The prayers of the saints ascend before God as incense; the Psalm's aspiration is realized in the throne-room reality where Christ intercedes and the incense of prayer rises continuously."
      }
    ],
    "3": [
      {
        "type": "allusion",
        "target": "Jas 3:6",
        "note": "Set a guard over my mouth, O LORD; keep watch over the door of my lips — 'the tongue also is a fire, a world of evil among the parts of the body. It corrupts the whole body, sets the whole course of one's life on fire, and is itself set on fire by hell' (Jas 3:6). The prayer for divine guardianship over the mouth (Ps 141:3) is answered by James's NT theology of speech: the tongue cannot be tamed by human effort alone (Jas 3:8) — only the Spirit can set a guard over the mouth. The Psalm's petition acknowledges what James's analysis confirms: speech is a spiritual problem requiring divine intervention."
      }
    ]
  },
  "142": {
    "4": [
      {
        "type": "allusion",
        "target": "Heb 4:15",
        "note": "Look and see, there is no one at my right hand; no one is concerned for me. I have no refuge; no one cares for my life — 'for we do not have a high priest who is unable to empathize with our weaknesses, but we have one who has been tempted in every way, just as we are — yet he did not sin' (Heb 4:15). The cave-psalm desolation of Psalm 142:4 — total abandonment, no helper, no refuge — is a condition Christ entered fully: Gethsemane, the arrest when everyone fled (Mark 14:50), and the cross cry of dereliction (Matt 27:46). The high priest of Hebrews can sympathize because he passed through the very abandonment Psalm 142 describes."
      }
    ]
  },
  "143": {
    "2": [
      {
        "type": "quote",
        "target": "Rom 3:20",
        "note": "Do not bring your servant into judgment, for no one living is righteous before you — 'therefore no one will be declared righteous in God's sight by the works of the law; rather, through the law we become conscious of our sin' (Rom 3:20). Paul cites Psalm 143:2 directly as scriptural proof that universal human unrighteousness before God is not Paul's invention but the teaching of Israel's own Scriptures. The Psalm's prayer is the OT admission of what Romans 3 expounds: no one living is righteous before God by their own standing. The need for imputed righteousness (Rom 3:22) is the answer to what Psalm 143:2 acknowledges."
      }
    ],
    "10": [
      {
        "type": "allusion",
        "target": "Rom 8:14",
        "note": "Teach me to do your will, for you are my God; may your good Spirit lead me on level ground — 'for those who are led by the Spirit of God are the children of God' (Rom 8:14). The prayer for the Spirit's leading on level ground (Ps 143:10) is the daily reality Paul describes as the mark of God's children. The Psalmist asks for what the NT declares is given in Christ: the Spirit who teaches us God's will and leads us through the terrain of the life of faith. Gal 5:18: 'if you are led by the Spirit, you are not under the law.'"
      }
    ]
  },
  "144": {
    "3": [
      {
        "type": "allusion",
        "target": "Heb 2:6",
        "note": "LORD, what are human beings that you care for them, mere mortals that you think of them? — 'but there is a place where someone has testified: \"What is mankind that you are mindful of them, a son of man that you care for him?\"' (Heb 2:6, citing Ps 8:4). Psalm 144:3 echoes Psalm 8:4's question of human insignificance; Hebrews applies Psalm 8's answer to Christ — the one who is truly the Son of Man, who entered human lowliness and was then crowned with glory and honor. The question of why God cares for mere mortals finds its deepest answer in the incarnation: God cared so much that he became one of them."
      }
    ]
  },
  "145": {
    "13": [
      {
        "type": "allusion",
        "target": "Rev 11:15",
        "note": "Your kingdom is an everlasting kingdom, and your dominion endures through all generations — 'the kingdom of the world has become the kingdom of our Lord and of his Messiah, and he will reign for ever and ever' (Rev 11:15). The everlasting kingdom of Psalm 145:13 is the kingdom that Revelation's seventh trumpet declares arrived: through Christ, the LORD's eternal dominion has broken into history and will be consummated at his return. The Psalm's declaration of permanence is the eschatological promise that Rev 11:15 announces as actualized in Christ's resurrection and coming reign."
      }
    ],
    "18": [
      {
        "type": "allusion",
        "target": "John 4:24",
        "note": "The LORD is near to all who call on him, to all who call on him in truth — 'God is spirit, and his worshipers must worship in the Spirit and in truth' (John 4:24). The nearness of the LORD to those who call in truth (Ps 145:18) is the presence that Jesus reveals is now accessible in Spirit and truth — no longer tied to a geographic location (John 4:21). The Samaritan woman's question about where to worship is answered by the one who is himself the presence of the LORD, near to all who call on him through the Spirit."
      }
    ]
  },
  "146": {
    "7": [
      {
        "type": "fulfillment",
        "target": "Luke 4:18",
        "note": "He upholds the cause of the oppressed and gives food to the hungry. The LORD sets prisoners free — 'The Spirit of the Lord is on me, because he has anointed me to proclaim good news to the poor. He has sent me to proclaim freedom for the prisoners and recovery of sight for the blind, to set the oppressed free' (Luke 4:18). The Nazareth manifesto is Jesus' self-presentation as the personal enactor of the divine program that Psalm 146:7-8 attributes to the LORD. He does not merely announce that God does these things — he is the one through whom God now does them. The Psalm's list of divine deeds (food to hungry, freedom to prisoners, sight to the blind) becomes the list of Christ's miracles."
      }
    ],
    "9": [
      {
        "type": "allusion",
        "target": "Jas 1:27",
        "note": "The LORD watches over the foreigner and sustains the fatherless and the widow, but he frustrates the ways of the wicked — 'religion that God our Father accepts as pure and faultless is this: to look after orphans and widows in their distress and to keep oneself from being polluted by the world' (Jas 1:27). The divine character declared in Psalm 146:9 — watchfulness over foreigner, fatherless, and widow — is the character James identifies as the content of true religion. Those who reflect the LORD's concern for the vulnerable embody the religion that God accepts; Psalm 146:9 is the OT ground of James's definition of practical holiness."
      }
    ]
  }
}

def main():
    existing = load_echo('psalms')
    merge_echo(existing, PSALMS_ECHOES)
    save_echo('psalms', existing)
    for ch in range(140, 147):
        entries = len(existing.get(str(ch), {}))
        print(f"  ch{ch}: {entries} verses with entries")
    print("Psalms 140-146 echoes complete.")

if __name__ == '__main__':
    main()
