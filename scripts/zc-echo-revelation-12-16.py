"""
MKT Echo Layer — Revelation ch12-16
Fills ch15 and ch16 (ch12-14 already had partial entries from prior run)
Run: python3 scripts/zc-echo-revelation-12-16.py

Echo strategy (per guide: selective — 2-3 best echoes per verse, not every parallel):
- Ch15: Song of Moses (Exod 15; Deut 32), tabernacle of testimony (Exod 38),
        Sinai glory-cloud filling sanctuary (Exod 40; 1 Kgs 8)
- Ch16: Seven bowls echo seven Egyptian plagues structurally;
        key: boils (Exod 9), water-to-blood (Exod 7), darkness (Exod 10),
        Euphrates drying (Isa 11; Jer 51), frogs (Exod 8),
        cup of wrath (Jer 25; Isa 51), hail (Exod 9), Armageddon (Zech 12; Judg 5)
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

REVELATION_ECHOES = {
  "15": {
    "3": [
      {"type": "allusion", "target": "Exod 15:1-18", "note": "The Song of Moses after the Exodus sea-crossing — 'Great and marvelous are your works' matches the victory-doxology register of Exod 15, where YHWH's rescue of Israel from Egypt is celebrated in song. John combines 'song of Moses' and 'song of the Lamb' to signal that the final Exodus (the Lamb's redemption) fulfills and surpasses the first."},
      {"type": "allusion", "target": "Deut 32:3-4", "note": "Moses's final Song (Deut 32): 'I will proclaim the name of the LORD... his works are perfect and all his ways are just' — the Deuteronomic Song of Moses identifies divine justice in judgment as the content of true worship; Revelation's martyrs sing the same acknowledgment of God's righteous ways in the face of the bowls."},
      {"type": "allusion", "target": "Ps 145:17", "note": "'The LORD is righteous in all his ways and faithful in all he does' — the Psalmic acclamation of divine righteousness provides the liturgical vocabulary for the saints' doxology; 'just and true are your ways' (Rev 15:3) draws from this tradition of worship-as-theodicy."}
    ],
    "4": [
      {"type": "allusion", "target": "Ps 86:9", "note": "'All the nations you have made will come and worship before you, Lord' — the Davidic psalm anticipates the eschatological worship of all nations; Rev 15:4 ('all nations will come and worship before you') cites this as the goal that the bowl judgments ultimately serve: universal worship through universal justice."},
      {"type": "allusion", "target": "Jer 10:7", "note": "'Who should not fear you, King of the nations? This is your due' — Jeremiah's polemic against idols grounds the fear-of-God in the uniqueness of YHWH as King of the nations; Rev 15:4 ('Who will not fear you, O Lord, and glorify your name?') transplants this motif to the final vindication of YHWH's sovereignty over every imperial power."}
    ],
    "5": [
      {"type": "allusion", "target": "Exod 38:21", "note": "The 'tabernacle of the covenant law' (lit. tabernacle of testimony — <em>mishkan ha-eduth</em>) — the wilderness Tabernacle was called the tabernacle of testimony because it housed the ark containing the tablets of the covenant. Rev 15:5 opens the heavenly counterpart of that earthly sanctuary, signaling that the bowl judgments proceed from the very source of the covenant law that has been violated."},
      {"type": "allusion", "target": "Num 1:50", "note": "The Levites were appointed over 'the tabernacle of the testimony' (<em>mishkan ha-eduth</em>) — the identical phrase used in Rev 15:5 for the heavenly temple. The careful alignment of heavenly sanctuary with the Mosaic tabernacle-of-testimony establishes the bowls as covenant-faithfulness in action: what the earthly tabernacle foreshadowed, the heavenly temple now executes."}
    ],
    "8": [
      {"type": "allusion", "target": "Exod 40:34-35", "note": "The glory-cloud filled the tabernacle so that Moses could not enter — the completion of the tabernacle inaugurated by the divine Presence filling it and temporarily excluding the mediator. Rev 15:8 mirrors this: the heavenly temple fills with smoke from God's glory, and no one can enter until the seven plagues are fulfilled. The pattern: the completion of judgment (like the completion of the sanctuary) is marked by the overwhelming divine Presence."},
      {"type": "allusion", "target": "1 Kgs 8:10-11", "note": "When Solomon's temple was dedicated, the glory-cloud filled it so that the priests could not enter — the Solomonic dedication theophany repeats the Exodus tabernacle pattern. Revelation deploys both precedents: the heavenly temple's inaccessibility during the bowl sequence maps the same divine-glory-filling that marked the great dedications of Israel's worship history."}
    ]
  },
  "16": {
    "2": [
      {"type": "allusion", "target": "Exod 9:8-12", "note": "The sixth Egyptian plague: Moses threw soot into the air and festering boils broke out on the Egyptians. The first bowl (ugly, festering sores on those with the mark of the beast) directly reprises this plague — the beast's worshipers receive the judgment the Pharaoh's subjects received. The bowls are the new-Exodus plagues poured on the new Egypt (Rome/Babylon)."}
    ],
    "3": [
      {"type": "allusion", "target": "Exod 7:17-21", "note": "The first Egyptian plague: the Nile turned to blood and every fish died — Pharaoh's water-system becomes a death-system. The second bowl (sea turns to blood like a dead man, every living creature dies) escalates the Exodus plague from the Nile to the entire sea, signaling that the new-Exodus judgment is total, not partial."}
    ],
    "4": [
      {"type": "allusion", "target": "Ps 78:44", "note": "'He turned their rivers to blood; they could not drink from their streams' — the psalmist's recitation of the Exodus plagues frames them as covenant-history events to be retold in worship. Rev 16:4 (rivers and springs become blood) draws on this psalmic tradition of plague-as-covenant-enforcement, applicable now to Babylon's empire."},
      {"type": "allusion", "target": "Exod 7:19", "note": "Moses stretched out his staff over all the waters of Egypt — streams, canals, ponds, all reservoirs — and they turned to blood. The third bowl extends the water-to-blood judgment from sea (v3) to inland fresh waters, completing the saturation of the water system that the Exodus plague began."}
    ],
    "5": [
      {"type": "allusion", "target": "Deut 32:4", "note": "'He is the Rock, his works are perfect, and all his ways are just' — the Song of Moses' declaration of divine righteousness in judgment underlies the angel of the waters' doxology ('you are just in these judgments'). Rev 16:5-7 pauses the bowl sequence for two theodicy-doxologies, grounding the violence of the judgments in the character of the God who poured them."}
    ],
    "10": [
      {"type": "allusion", "target": "Exod 10:21-23", "note": "The ninth Egyptian plague: thick darkness covered Egypt for three days so that no one could see or move, while Israel had light. The fifth bowl (beast's kingdom plunged into darkness) reprises this plague against the Pharaonic empire's successor — the beast's kingdom loses the light as Pharaoh's land did."},
      {"type": "allusion", "target": "Isa 8:22", "note": "'They will look toward the earth and see only distress and darkness' — Isaiah's judgment-darkness against those who reject YHWH's word. The gnawing of tongues in agony (Rev 16:10) parallels the Isaianic imagery of judgment-torment that results from rejecting the divine light."}
    ],
    "12": [
      {"type": "allusion", "target": "Isa 11:15-16", "note": "'The LORD will dry up the gulf of the Egyptian sea... he will make people cross over dry-shod... as there was for Israel when they came up from Egypt' — Isaiah's new-Exodus vision includes drying up the Euphrates for the return of the remnant. Rev 16:12 inverts the direction: the Euphrates is dried to prepare the way for eastern kings, but the echo activates both the Exodus-crossing pattern and the judgment-against-Babylon theme."},
      {"type": "allusion", "target": "Jer 51:36", "note": "'I will dry up her sea and make her springs run dry' — YHWH's judgment against Babylon includes drying up her waters. Revelation's bowl against the Euphrates (Babylon's river) implements Jeremiah's Babylon-oracle: the great river that sustained and protected Babylon is removed to prepare the final assault."}
    ],
    "13": [
      {"type": "allusion", "target": "Exod 8:1-15", "note": "The second Egyptian plague: frogs swarmed from the Nile over all Egypt. Rev 16:13 (three frog-like impure spirits emerging from the dragon, beast, and false prophet) transforms the Exodus plague into a demonic triad — the unholy trinity disgorges frogs as Pharaoh's Egypt was afflicted by them, linking the two great empires of opposition to God's purposes."}
    ],
    "15": [
      {"type": "allusion", "target": "Matt 24:43", "note": "'If the owner of the house had known at what time of night the thief was coming, he would have kept watch' — Jesus's own parable of the unexpected thief interrupts the bowl sequence as a direct-speech beatitude from the risen Christ. The thief-warning was spoken in the Olivet Discourse context; its insertion here confirms that the bowl-judgments are the backdrop against which the church's watchfulness becomes urgent."},
      {"type": "allusion", "target": "1 Thess 5:2", "note": "'You know very well that the day of the Lord will come like a thief in the night' — Paul's eschatological warning uses the same thief-imagery as the dominical saying, indicating it was already a fixed early Christian phrase for the unexpected Parousia. Rev 16:15 embeds it within the bowl sequence as a pastoral aside to the letter's recipients."}
    ],
    "16": [
      {"type": "allusion", "target": "Zech 12:11", "note": "'On that day the weeping in Jerusalem will be great, like the weeping of Hadad Rimmon in the plain of Megiddo' — Zechariah's eschatological mourning oracle (for the one who was pierced, v10) is located at Megiddo. Rev 16:16 names the gathering point as Har-Megiddo (Armageddon), the place Zechariah associates with the final mourning and repentance before YHWH."},
      {"type": "allusion", "target": "Judg 5:19", "note": "'Kings came, they fought; at Taanach, by the waters of Megiddo, they took no plunder' — Deborah's song commemorates the proto-Armageddon battle where the kings of Canaan assembled at Megiddo and were destroyed. The naming of Har-Megiddo as the gathering place of the kings of the whole world activates the ancient memory of decisive cosmic battle at this specific geographic locus."}
    ],
    "19": [
      {"type": "allusion", "target": "Jer 25:15-16", "note": "'Take from my hand this cup filled with the wine of my wrath and make all the nations to whom I send you drink it' — YHWH gave Jeremiah a cup of wrath to pass to all nations beginning with Jerusalem; Rev 16:19 (Babylon given the cup of the wine of the fury of his wrath) completes this Jeremian program: Babylon, last in the sequence of nations Jeremiah addressed (Jer 25:26: 'the king of Babylon'), finally receives the cup she was spared for last."},
      {"type": "allusion", "target": "Isa 51:17", "note": "'Awake, awake! Rise up, Jerusalem, you who have drunk from the hand of the LORD the cup of his wrath, you who have drained to its dregs the goblet that makes people stagger' — Israel drank the cup before Babylon did; now Babylon receives what Israel endured. The echo reframes the bowl judgment: Babylon's cup is the mirror of the cup YHWH's own people drank."}
    ],
    "21": [
      {"type": "allusion", "target": "Exod 9:22-26", "note": "The seventh Egyptian plague: Moses stretched out his staff and YHWH sent hail throughout Egypt — the worst hailstorm Egypt had ever seen. Rev 16:21 (hundred-pound hailstones) reprises and exceeds the Exodus hail as the seventh bowl exceeds the seventh plague, and men curse God as Pharaoh's heart was hardened rather than softened by the same judgment."},
      {"type": "allusion", "target": "Josh 10:11", "note": "'The LORD hurled large hailstones down on them... and more of them died from the hail than were killed by the Israelites' — the hail at Beth Horon, where YHWH fought for Israel against the Amorite kings, becomes the precedent for divine hail-warfare. The kings gathered at Armageddon (v16) face the same divine-warrior hail that destroyed the kings who opposed Joshua."}
    ]
  }
}

def main():
    existing = load_echo('revelation')
    merge_echo(existing, REVELATION_ECHOES)
    save_echo('revelation', existing)

    # Verify ch15 and ch16 now have entries
    for ch in ['12', '13', '14', '15', '16']:
        count = len(existing.get(ch, {}))
        status = 'done' if count > 0 else 'MISSING'
        print(f'  ch{ch}: {count} verses with echoes — {status}')

if __name__ == '__main__':
    main()
