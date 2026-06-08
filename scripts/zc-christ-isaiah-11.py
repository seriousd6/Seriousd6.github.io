"""
MKT Christ Commentary — Isaiah chapter 11
Run: python3 scripts/zc-christ-isaiah-11.py

Source data used:
- data/interlinear/isaiah.json
- data/translation/draft/mediating/isaiah.json

Key decisions in this range:
- v. 1: direct — nēṣer (branch) / Matt 2:23 Nazareth connection; Jesse not David = humility
- v. 2: direct — sixfold Spirit; fulfilled at baptism (Matt 3:16; John 1:32-34)
- v. 4: direct — rod of his mouth; Rev 19:15 cites this of Christ's return
- v. 8: type — serpent reversal of Gen 3:15 enmity
- v. 10: direct — Rom 15:12 cites root of Jesse as fulfilled in Christ for Gentiles
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
"11": {
"1": "<p>A direct prophecy. The <em>ḥōṭer</em> (shoot, twig) from the stump of Jesse and <em>nēṣer</em> (branch) from his roots — Jesse is David's father, one generation further back, emphasizing the unexpected and humble origin of the Messiah after the Davidic dynasty has been cut down like a felled tree. The term <em>nēṣer</em> likely underlies Matthew 2:23's citation that Jesus would be called a Nazarene (<em>Nazoraios</em>), Matthew reading the branch-prophecy in the place-name Nazareth. The shoot from a stump is the image of life from apparent death — the post-exilic Davidic house restored through one who emerges when all looks finished.</p>",
"2": "<p>A direct prophecy. The Spirit of YHWH rests upon the shoot — six descriptions in three pairs: Spirit of YHWH; wisdom (<em>ḥok̠māh</em>) and understanding (<em>bînāh</em>); counsel (<em>'ēṣāh</em>) and might (<em>gĕb̠ûrāh</em>); knowledge (<em>da'at</em>) and fear of YHWH (<em>yir'at YHWH</em>). The Spirit descending on Jesus at his baptism (Matt 3:16; John 1:32-34) is the fulfillment of this anointing — the Messianic Spirit-reception that marks the beginning of his public ministry. The Lukan genealogy traces Jesus back to Jesse and then to Adam, placing this Davidic-messianic anointing in its full human context.</p>",
"3": "<p>A type: the Messiah does not judge by outward appearance or hearsay but by inner righteousness. Jesus demonstrates this throughout the Gospels — he knows what is in human hearts (John 2:25), judges not by appearances but with right judgment (John 7:24), and sees the faith of the paralytic before pronouncing forgiveness (Mark 2:5). This verse establishes that messianic justice is penetrating and uncorrupted by the social pressures that distort human judgment.</p>",
"4": "<p>A direct prophecy. The rod of his mouth (<em>šēb̠eṭ pîw</em>) and the breath of his lips that kills the wicked — Revelation 19:15 applies this directly to Christ at his return: <em>from his mouth comes a sharp sword with which to strike down the nations</em>. Paul echoes v. 4 in 2 Thessalonians 2:8 (the lawless one destroyed by the breath of Christ's mouth). The messianic King does not merely pronounce justice — his word is the weapon of execution, establishing his sovereignty as absolute.</p>",
"5": "<p>A type: righteousness (<em>ṣedeq</em>) as the belt around the Messiah's waist and faithfulness (<em>'emûnāh</em>) as the belt around his loins — the Messiah's personal character is his armor. Ephesians 6:14 includes the belt of truth and breastplate of righteousness in the Christian's spiritual armor — armor that derives from and mirrors the Messiah's own character. Christ's righteousness becomes the believer's covering (2 Cor 5:21).</p>",
"6": "<p>A shadow: the peaceable kingdom where wolf and lamb dwell together, leopard and young goat lie down, calf and lion graze side by side. The cosmic restoration of creation-order — predator and prey at peace — is the eschatological reversal of the enmity introduced by the Fall. Romans 8:19-22 frames creation itself as groaning toward this liberation. Revelation 21-22 presents the new creation as its fulfillment. The peaceable kingdom is not allegory but eschatological reality: Christ's reign will restore what sin fractured.</p>",
"7": "<p>A shadow: cow and bear graze together, lion eats straw like the ox. The carnivore transformed — the dietary order of predation that followed the Fall reversed. This is not merely environmental metaphor but creation theology: what death corrupted, the Messiah restores. The theme of cosmic reconciliation points to Christ as the one through whom all things are reconciled (Col 1:20 — all things, whether on earth or in heaven).</p>",
"8": "<p>A type: the nursing child plays over the cobra's hole, the weaned child puts its hand on the adder's den — and is unharmed. This is the explicit reversal of the serpent-curse of Genesis 3:15 (enmity between the seed of the woman and the serpent, the serpent striking the heel). The child of v. 8 is safe precisely because the seed of the woman has crushed the serpent's head (Gen 3:15; Rom 16:20). Christ's victory over the devil (Heb 2:14) makes the serpent's den safe for his people to approach.</p>",
"9": "<p>A shadow: no hurting or destroying on YHWH's holy mountain; the earth full of the knowledge of YHWH as the waters cover the sea. Habakkuk 2:14 uses nearly identical language. The universal knowledge of YHWH that fills the earth is what Christ brings: John 17:3 defines eternal life as knowing the Father and the Son he sent; 2 Corinthians 4:6 frames the gospel as the light of the knowledge of God's glory in the face of Christ. The filled-earth imagery points to the universal scope of Christ's mission.</p>",
"10": "<p>A direct prophecy. The <em>šōreš yišay</em> — root of Jesse — standing as a signal (<em>nēs</em>) to the peoples, with the nations seeking him and his resting place being glorious. Paul quotes this verse in Romans 15:12 as fulfilled in Christ: <em>the root of Jesse will come, the one who rises to rule the Gentiles; in him will the Gentiles hope</em>. This is Paul's explicit scriptural warrant for his Gentile mission — the shoot of Jesse was always intended to draw in all nations, not only Israel.</p>",
"11": "<p>A shadow: the second exodus — YHWH extends his hand a second time to recover the remnant from all nations (Egypt, Assyria, Pathros, Cush, Elam, Shinar, Hamath, the coastlands). The first exodus was from Egypt; the eschatological exodus is from the entire diaspora. The NT frames Christ's cross as the definitive second-exodus event (Luke 9:31: the exodus Jesus was to accomplish in Jerusalem), and the church's mission as the gathering of the dispersed children of God from all nations (John 11:52).</p>",
"12": "<p>A shadow: the banner (<em>nēs</em>) lifted to the nations to assemble the dispersed of Israel from the four corners of the earth. The banner/signal motif runs through Isaiah (11:10, 49:22, 62:10) — it is the messianic standard around which the nations gather. Christ lifted up on the cross becomes this gathering signal: John 12:32 (<em>when I am lifted up from the earth, I will draw all people to myself</em>) applies this logic explicitly.</p>",
"13": "<p>A shadow: the jealousy of Ephraim and the hostility of Judah healed — the old north-south division overcome. In Christ, the dividing wall is broken down — not only between Jew and Gentile (Eph 2:14) but also within Israel between the alienated northern and southern kingdoms. The new humanity in Christ is the eschatological Israel that Ezekiel's two-sticks vision (Ezek 37:16-28) anticipated and Paul describes in Ephesians 2-3.</p>",
"14": "<p>A shadow: the reunited Israel's victories over surrounding enemies — Philistines, Edomites, Moabites, Ammonites. The military conquest imagery depicts the Messiah's dominion extending outward through his people. The NT spiritualizes this as the advance of the gospel through the preaching of the crucified King, with Christ's victory on the cross the ground of all subsequent victories.</p>",
"15": "<p>A shadow: the second-exodus geography — YHWH destroys the tongue of the Egyptian Sea and strikes the Euphrates into seven channels. The original exodus reversed (sea split, desert crossed) becomes the pattern for the eschatological restoration. The Revelation's vision of a new exodus (Rev 15:3 — the song of Moses and the Lamb) appropriates this imagery for the final deliverance of God's people from the ultimate oppressor.</p>",
"16": "<p>A shadow: the highway from Assyria for the remnant — as there was a highway for Israel from Egypt. The exodus-highway motif (cf. Isa 40:3; 57:14) is explicitly the model: the second exodus requires a second highway. Matthew 3:3 applies Isaiah 40:3 (prepare the way of YHWH) to John the Baptist, framing Jesus' advent as the second-exodus event. The highway of return is the highway of the gospel — the path along which the scattered people of God are brought home to the Father through the Son.</p>"
}
}

def main():
    existing = load_comm('mkt-christ', 'isaiah')
    merge_comm(existing, ISAIAH)
    save_comm('mkt-christ', 'isaiah', existing)
    v = sum(len(vs) for vs in ISAIAH.values())
    print(f'Isaiah 11 mkt-christ: {v} verses written.')

if __name__ == '__main__':
    main()
