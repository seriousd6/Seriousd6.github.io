"""
Echo Layer — Genesis chapters 29–30
Run: python3 scripts/zc-echo-genesis-29-30.py

Key echo trajectories:
- The well-meeting pattern (29:1-12): recurring OT type (Gen 16, 24, Exod 2) that climaxes in
  John 4 (Jesus meeting the Samaritan woman at Jacob's well). The stone-rolling (29:10) echoes
  the resurrection (Matt 28:2; John 20:1).
- Bone of my bone (29:14): Eph 5:30-31 (union of Christ and the church)
- Seven years of labor for love (29:20): Heb 12:2 (joy set before Christ in his suffering)
- Leah unloved but chosen: the messianic line runs through Judah (Leah's son, 29:35), not
  Joseph (Rachel's son) — the election of the unlovely; 1 Cor 1:27-28
- Judah born (29:35): Rev 5:5 (Lion of the tribe of Judah); Matt 1:2-3 (genealogy)
- Barren Rachel (30:1): the barren-woman motif → Isa 54:1; Gal 4:27; Luke 1:36
- God remembered Rachel (30:22): divine-remembrance formula → Exod 2:24; Luke 1:54-55
- Joseph born (30:23-24): the Joseph type begins — beloved son, rejected, exalted to save;
  Gen 37-50 / Acts 7:9-10; John 3:16; Phil 2:6-11
- No parallels data to absorb for chs 29-30.
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

GENESIS_ECHOES = {
  "29": {
    "10": [
      {"type": "shadow", "target": "Matt 28:2", "note": "Jacob rolls the stone from the mouth of the well single-handedly when he sees Rachel (29:10) — a feat that normally required multiple shepherds (29:8). The stone-rolling at the well in a scene of covenant-meeting and life-giving water anticipates the stone-rolled-away at the tomb (Matt 28:2; Mark 16:3-4; John 20:1), where the sealed source of life is opened in a new-covenant meeting between the risen Christ and those who come seeking."},
      {"type": "shadow", "target": "John 4:6", "note": "Jacob meets Rachel at a well in a foreign land — a third 'well-meeting' alongside the servant meeting Rebekah (Gen 24) and Moses meeting Zipporah (Exod 2:16-21). All three are covenant-formation meetings at wells in foreign territory. John 4 places Jesus at 'Jacob's well' explicitly (John 4:6) and performs an ultimate well-meeting: the one who gives living water meets the Samaritan woman, fulfilling and transcending the well-meeting pattern of the patriarchal narrative."}
    ],
    "14": [
      {"type": "shadow", "target": "Eph 5:30", "note": "'You are my bone and my flesh' (29:14) — Laban's recognition of Jacob as kin uses the formula of Gen 2:23 (Adam recognizing Eve: 'bone of my bones and flesh of my flesh'). Paul quotes Gen 2:24 in Eph 5:30-31 and applies it to Christ and the church: 'we are members of his body.' The phrase 'bone and flesh' thus runs from Adam's recognition of Eve through Jacob's reception by Laban to Paul's description of the church's organic union with Christ."}
    ],
    "20": [
      {"type": "shadow", "target": "Heb 12:2", "note": "Seven years seemed to Jacob 'but a few days because of the love he had for her' (29:20) — love's capacity to make suffering light and long labor short. Heb 12:2 applies the same logic to Christ's passion: 'who for the joy set before him endured the cross, despising the shame.' The endurance that love makes possible is the same in both cases; Jacob's seven-year service typologically illuminates why Christ could endure what he did."}
    ],
    "31": [
      {"type": "shadow", "target": "1 Cor 1:27", "note": "The LORD opened Leah's womb because 'she was hated' (29:31) — divine election falls on the unbeautiful, the overlooked, the unloved. This is the pattern Paul articulates in 1 Cor 1:27-28: 'God chose what is foolish in the world to shame the wise; God chose what is weak in the world to shame the strong.' Significantly, the messianic line runs through Judah (Leah's son), not Joseph (Rachel's beloved son) — the Lion of the tribe of Judah comes from the less-loved mother."}
    ],
    "35": [
      {"type": "shadow", "target": "Rev 5:5", "note": "At Judah's birth, Leah says 'This time I will praise the LORD,' and she named him Judah (<em>yĕhûdāh</em> = praise; from the same root as <em>tôdāh</em>) (29:35). Judah is the tribe of the royal line (Gen 49:10) and ultimately of Christ (Rev 5:5: 'the Lion of the tribe of Judah, the Root of David, has conquered'). The name 'Judah' — coined in a moment of weary gratitude by an unloved woman — becomes the tribal identity from which the Savior comes."},
      {"type": "shadow", "target": "Matt 1:2", "note": "Judah's birth (29:35) opens the genealogical channel through which Christ enters history: Gen 49:10 → 1 Chr 5:2 → Matt 1:2-3 (Judah the father of Perez and Zerah by Tamar) → Luke 3:33 (Judah in Christ's genealogy). The surprising election of the unloved Leah's son as the messianic tribe foreshadows the consistent OT pattern of God choosing the unexpected bearer of the covenant."}
    ]
  },
  "30": {
    "1": [
      {"type": "shadow", "target": "Isa 54:1", "note": "'Give me children, or I shall die!' (30:1) — Rachel's cry of barren desperation joins a long OT line of barren women (Sarah, Rebekah, Manoah's wife, Hannah, Elizabeth) whose impossible conceptions mark decisive moments in redemptive history. Isa 54:1 ('Sing, O barren one, who did not bear; break forth into singing') is the prophetic crystallization of this pattern, which Paul in Gal 4:27 applies to the church as the fruit of the new covenant, born from what seemed barren."}
    ],
    "6": [
      {"type": "shadow", "target": "Luke 1:25", "note": "'God has judged me, and has also heard my voice and given me a son' (30:6) — Bilhah's son Dan named with the verbal root <em>dān</em> (judged/vindicated). The formula 'God has heard' recurs at every barren-woman conception in the OT (Gen 21:17; 1 Sam 1:19-20; Luke 1:13). Elizabeth's words after John's conception echo it directly: 'the Lord has done this for me... he has taken away my disgrace among the people' (Luke 1:25), the same pattern of divine hearing and public vindication."}
    ],
    "22": [
      {"type": "shadow", "target": "Exod 2:24", "note": "'God remembered Rachel, and God listened to her and opened her womb' (30:22) — the divine-remembrance formula that signals covenant faithfulness in action. The same formula opens the Exodus narrative: 'God heard their groaning, and God remembered his covenant with Abraham, with Isaac, and with Jacob' (Exod 2:24). In both cases, divine remembrance after long silence is the pivot point from suffering to redemption. Luke 1:54-55 ('he has helped his servant Israel, remembering to be merciful... as he spoke to our fathers') identifies the incarnation as the ultimate act of divine remembrance."}
    ],
    "23": [
      {"type": "shadow", "target": "Luke 1:25", "note": "'God has taken away my reproach' (30:23) — Rachel at Joseph's birth uses the same reproach-removal formula as Elizabeth after John's conception (Luke 1:25: 'the Lord has done this for me; in these days he has shown his favor and taken away my disgrace'). The barren woman's reproach being removed by God is a recurring type of the reversal-of-shame that the gospel enacts: 'he was despised and rejected... he has borne our griefs' (Isa 53:3-4)."}
    ],
    "24": [
      {"type": "type", "target": "Acts 7:9", "note": "Joseph's birth (30:24) begins the Joseph type — one of the most developed OT types of Christ. The key parallels: Joseph is the beloved son (Gen 37:3; Matt 3:17), rejected by his brothers (Gen 37:4, 18; John 1:11), sold for silver (Gen 37:28; Matt 26:15), falsely accused (Gen 39:14-18; Mark 14:56-57), imprisoned (Gen 39:20; Matt 27:2), exalted to the right hand of Pharaoh to save all nations from famine (Gen 41:40-41; Phil 2:9-11). Acts 7:9-10 makes the parallel explicit: 'the patriarchs were jealous of Joseph and sold him into Egypt. But God was with him.'"}
    ]
  }
}

def main():
    existing = load_echo('genesis')
    merge_echo(existing, GENESIS_ECHOES)
    save_echo('genesis', existing)

    result = load_echo('genesis')
    for ch in [29, 30]:
        n = len(result.get(str(ch), {}))
        print(f'  Ch {ch}: {n} verses with echoes')
    total = len(result)
    print(f'  Genesis total: {total} chapters with echo data')
    print('Genesis 29-30 echoes written.')

if __name__ == '__main__':
    main()
