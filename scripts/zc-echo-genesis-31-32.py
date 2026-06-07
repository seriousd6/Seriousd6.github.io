"""
Echo Layer — Genesis chapters 31–32
Run: python3 scripts/zc-echo-genesis-31-32.py

Key echo trajectories:
- Gen 31:3: divine commission with presence-promise → Matt 28:20; Exod 3:12
- Gen 32:9-12: Jacob's prayer as covenant-prayer model → Luke 18:1-8; Matt 7:7-8
- Gen 32:10: 'not worthy of the least...' → Luke 15:21 (prodigal); Eph 3:8 (Paul)
- Gen 32:22-32: Wrestling at Peniel — the primary OT christophany debate; the man who
  blesses Jacob but refuses to reveal his name (→ Exod 3:14; Judg 13:18);
  Jacob survives seeing God face-to-face → anticipates the incarnation (John 1:14, 18)
- Gen 32:26: 'I will not let you go unless you bless me' → persistent/importunate
  prayer (Luke 11:5-8; 18:1-8); Heb 7:25 (Christ intercedes for us)
- Gen 32:28: New name (Israel) → Rev 2:17 (new name given to the overcomer); John 1:42
- Gen 32:31: Sun rises on limping Jacob → wounded-and-blessed pattern → John 20:27;
  Rev 5:6 (Lamb standing as though slain)
- No parallels data to absorb for chs 31-32.
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
  "31": {
    "3": [
      {"type": "shadow", "target": "Matt 28:20", "note": "'Return to the land of your fathers and to your kindred, and I will be with you' (31:3) — the divine commission paired with the promise of presence is a recurring structure throughout the OT (Exod 3:12: 'I will be with you'; Josh 1:5; Judg 6:16; Jer 1:8) that reaches its definitive expression in the Great Commission: 'I am with you always, to the end of the age' (Matt 28:20). The sent-one is never sent alone; the Sender accompanies the mission."}
    ],
    "11": [
      {"type": "shadow", "target": "Heb 1:14", "note": "The angel of God speaks to Jacob in a dream (31:11-13), functioning as God's personal messenger to guide the covenant-bearer through a crisis. The pattern of angelic divine guidance in the patriarchal narratives (Gen 16:7; 21:17; 22:11; 28:12; 31:11; 32:1) is the background for Hebrews 1:14's description of angels as 'ministering spirits sent out to serve for the sake of those who are to inherit salvation.' The patriarchs were heirs of the promise; the angels served them."}
    ],
    "13": [
      {"type": "shadow", "target": "Exod 3:6", "note": "'I am the God of Bethel' (31:13) — God identifies himself to Jacob by reference to the place where he previously appeared and made covenant promises (Gen 28:10-22). This identification-by-promise-history is the structural pattern of the divine self-disclosure to Moses: 'I am the God of your father, the God of Abraham, the God of Isaac, and the God of Jacob' (Exod 3:6). God's name is inseparable from his covenant history — a pattern Christ assumes when he says 'Before Abraham was, I am' (John 8:58)."}
    ],
    "42": [
      {"type": "shadow", "target": "Acts 9:31", "note": "'The God of Abraham and the Fear of Isaac had been with me' (31:42) — 'the Fear of Isaac' (<em>paḥad yiṣḥāq</em>) is a divine title unique to this passage, probably meaning 'the one Isaac fears/reverences.' The godly fear that marked Isaac's devotion becomes a name for the God he worshiped. The NT describes the early church as 'walking in the fear of the Lord and in the comfort of the Holy Spirit' (Acts 9:31) — the same combination of reverence and intimate presence that characterized the patriarchal covenant relationship."}
    ],
    "49": [
      {"type": "shadow", "target": "1 Tim 2:5", "note": "'The LORD watch between you and me when we are out of each other's sight' (31:49, the Mizpah benediction) — a covenant witness invoked when the two parties must separate. The covenant that requires a watching third party anticipates the role of the mediator: 'there is one God, and there is one mediator between God and men, the man Christ Jesus' (1 Tim 2:5). Where human covenants require a witness, the new covenant is secured by the mediator himself who stands between God and humanity permanently."}
    ]
  },
  "32": {
    "9": [
      {"type": "shadow", "target": "Luke 18:1", "note": "Jacob's prayer in 32:9-12 is the most developed patriarchal prayer in Genesis: it invokes God by covenant name and title, recalls the specific divine command being obeyed, confesses unworthiness, appeals to past covenant faithfulness, and states the specific need. Jesus's parable of the persistent widow (Luke 18:1-8) teaches that 'they ought always to pray and not lose heart' — Jacob's prayer at Peniel (32:9-12, 24-26) is the OT embodiment of that persistence: covenant-grounded, honest, and unrelenting."}
    ],
    "10": [
      {"type": "shadow", "target": "Luke 15:21", "note": "'I am not worthy of the least of all the deeds of steadfast love and all the faithfulness that you have shown to your servant' (32:10) — the covenant prayer begins with confession of unworthiness. The prodigal son's return speech uses the same structure: 'I am no longer worthy to be called your son' (Luke 15:21). Both Jacob and the prodigal approach with empty hands and appeal entirely to the other's character; both receive blessing beyond what they asked for."},
      {"type": "shadow", "target": "Eph 3:8", "note": "Jacob's self-description as unworthy of 'the least' of God's mercies (32:10) recurs in Paul: 'I am the least of all the saints, yet this grace was given to me' (Eph 3:8). The pattern of covenant unworthiness paired with covenant overflow is the grammar of grace throughout Scripture: the recipient recognizes the disproportion between who they are and what God gives, and this recognition becomes the occasion for greater praise, not paralysis."}
    ],
    "24": [
      {"type": "shadow", "target": "Hos 12:4", "note": "A man wrestles with Jacob until the breaking of the day (32:24) — the unnamed opponent who later reveals power to harm but also to bless. Hosea 12:3-4 interprets this as wrestling with the Angel and weeping/seeking his favor. Christian tradition consistently reads the man as a christophany — the pre-incarnate Word (cf. 32:29-30: Jacob survives seeing God face to face). The night-long wrestling as prevailing prayer is the type Jesus enacts in Gethsemane (Luke 22:44: 'being in agony he prayed more earnestly'), though with opposite tears — Jacob weeps for blessing; Jesus weeps over the cup."},
      {"type": "shadow", "target": "Luke 22:44", "note": "Jacob wrestles through the night until dawn (32:24) — the agonizing, extended, solitary encounter with God that is both combat and prayer. Luke 22:44 describes Jesus in Gethsemane: 'being in agony he prayed more earnestly; and his sweat became like great drops of blood.' Both are night-long, solitary, agonizing encounters with God at the hinge of a decisive mission — Jacob before meeting Esau, Jesus before the cross. Both emerge transformed (new name; resurrection) but marked by the struggle."}
    ],
    "26": [
      {"type": "shadow", "target": "Matt 7:7", "note": "'I will not let you go unless you bless me' (32:26) — the persistence in prayer that prevails against all apparent resistance. Jesus teaches exactly this posture: 'Ask, and it will be given to you; seek, and you will find; knock, and it will be opened to you' (Matt 7:7) and embodies the theology in the importunate-friend parable (Luke 11:5-8): the one who keeps knocking receives. Jacob's tenacious grip is the praxis of which Jesus's teaching is the principle."},
      {"type": "shadow", "target": "Heb 7:25", "note": "Jacob will not release the divine stranger until he receives blessing (32:26) — covenant boldness that clings to God's promises despite apparent rejection. Heb 7:25 describes Christ's permanent intercessory work: 'he always lives to make intercession for them.' Where Jacob's one-night wrestling secures a blessing for himself, Christ's eternal intercession secures the blessing for all those the Father has given him (John 17:9, 24)."}
    ],
    "28": [
      {"type": "shadow", "target": "Rev 2:17", "note": "'Your name shall no longer be called Jacob, but Israel, for you have striven with God and with men, and have prevailed' (32:28) — the new name given at the moment of covenant transformation. The pattern of divine name-giving at covenant transformation runs through Abram → Abraham (Gen 17:5), Sarai → Sarah (Gen 17:15), Jacob → Israel (Gen 32:28), Simon → Peter (John 1:42), and culminates in Rev 2:17: 'I will give him a white stone, with a new name written on the stone that no one knows except the one who receives it.' The overcomer receives a new identity from God."},
      {"type": "shadow", "target": "John 1:42", "note": "Jacob receives a new name from the divine wrestler (32:28) — the new name signifies the new identity and new chapter in covenant history. Jesus gives Simon a new name: 'You are Simon the son of John. You shall be called Cephas (which means Peter/Rock)' (John 1:42). The pattern: encounter with Christ → new name → new identity for the covenant mission. Israel becomes the name of the covenant people; Cephas becomes the rock on which the church is built."}
    ],
    "29": [
      {"type": "shadow", "target": "Exod 3:14", "note": "'Why is it that you ask my name?' (32:29) — the wrestler refuses to disclose his name. The same refusal appears at Judges 13:18 (the angel to Manoah: 'Why do you ask my name? It is wonderful/<em>pelî</em>') and contrasts with the divine name-disclosure of Exod 3:14 ('I AM WHO I AM'). The hidden name is the hidden identity of the pre-incarnate Christ, disclosed fully only in the incarnation: 'his name shall be called Wonderful Counselor, Mighty God' (Isa 9:6) and 'he has a name written that no one knows but himself' (Rev 19:12)."}
    ],
    "30": [
      {"type": "shadow", "target": "John 1:18", "note": "Jacob named the place Peniel, saying 'I have seen God face to face, and yet my life has been delivered' (32:30) — survival of the face-to-face divine encounter is presented as exceptional and surprising. Exod 33:20 explains why: 'man shall not see me and live.' Yet Jacob lives. The NT resolution: the incarnation makes God visible without consuming the viewer. John 1:18 ('no one has ever seen God; the only God, who is at the Father's side, he has made him known') and 1 John 1:1-2 (we have seen, heard, and touched him) fulfill what Peniel anticipates — God truly seen, in human form, and life preserved."}
    ],
    "31": [
      {"type": "shadow", "target": "Rev 5:6", "note": "The sun rose on Jacob as he passed Penuel, limping (32:31) — the wound that remains after the blessing-encounter. Jacob's permanent limp is the mark of the night when he wrestled with God and prevailed; it is wound and trophy simultaneously. Rev 5:6 describes the Lamb in the throne room: 'standing as though slain' — the marks of the crucifixion remain on the risen Christ, simultaneously wounds and victory-signs. John 20:27 (Jesus shows Thomas his hands and side) is the same pattern: the resurrection body carries and displays the wounds of its costly victory."}
    ]
  }
}

def main():
    existing = load_echo('genesis')
    merge_echo(existing, GENESIS_ECHOES)
    save_echo('genesis', existing)

    result = load_echo('genesis')
    for ch in [31, 32]:
        n = len(result.get(str(ch), {}))
        print(f'  Ch {ch}: {n} verses with echoes')
    total = len(result)
    print(f'  Genesis total: {total} chapters with echo data')
    print('Genesis 31-32 echoes written.')

if __name__ == '__main__':
    main()
