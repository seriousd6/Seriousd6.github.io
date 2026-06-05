"""
MKT Christ Commentary — Hebrews chapters 10–11
Run: python3 scripts/zc-christ-hebrews-10-11.py

Key decisions:
- 10:5-7 Ps 40 body-offering: "A fulfillment:" — the Son's words at incarnation fulfilling Ps 40
- 10:10 once for all sanctification: "A direct revelation:" — the completed sanctification
- 10:19-22 access to holiest: "A direct revelation:" — the opened way as present reality
- 10:37-38 Hab 2 + faith: "A fulfillment:" — the coming-one of Habakkuk = Christ
- 11:10 city with foundations: "A shadow:" — Abraham's faith as a type of the community's faith
- 11:17-19 Aqedah: "A type:" — Abraham offering Isaac as type of the Father offering the Son
- 11:26 Moses' reproach of Christ: "A shadow:" — Moses participating in the messianic reproach
- 11:39-40 not perfected without us: "A direct revelation:" — the communal eschatology
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
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, html in verses.items():
            if v not in existing[ch]:
                existing[ch][v] = html

HEBREWS = {
  "10": {
    "5": '<p>A fulfillment: "Sacrifices and offerings you have not desired, but a body you have prepared for me... I have come to do your will, O God." The Son speaks these words at his entry into the world (incarnation), applying Psalm 40:6-8 to himself. The body prepared for the Son is the instrument of the will-doing that replaces and fulfills what the animal sacrifices only anticipated. The incarnation is the fulfillment of the Psalm\'s declaration: the one who comes to do God\'s will is the Son, the will he does is his obedient self-offering, and the body he does it in is the one God prepared for him at Bethlehem.</p>',
    "10": '<p>A direct revelation: we have been sanctified through the offering of the body of Jesus Christ once for all. The sanctification accomplished by Christ\'s body-offering is a completed act (aorist-perfect: we have been sanctified) with permanent effect. The "once for all" (<em>ephapax</em>) is the theological key: it cannot be supplemented, repeated, or improved. Those who are in Christ are fully and permanently holy before God because of what Christ did — not partially holy pending further sacrifice or repeated ritual.</p>',
    "12": '<p>A direct revelation: Christ, after offering one sacrifice for sins forever, sat down at the right hand of God. The sitting down is the posture of completed work — no Levitical priest ever sat in the sanctuary (the work was never done). The right-hand session is the evidence of divine acceptance. The single sacrifice for sins forever — not "for now" or "for past sins" but for sins as a category, permanently and completely — is what the session declares complete. The community draws near on the basis of this completed sacrifice.</p>',
    "19": '<p>A direct revelation: we have confidence to enter the holy places by the blood of Jesus, by the new and living way that he opened for us through the curtain, that is, through his flesh. The opened way is the Incarnation-death-resurrection-ascension sequence understood as Christ\'s path through the curtain into the Father\'s presence, and simultaneously as the path he has opened for all who follow him through his death and resurrection into the same divine presence. The "new and living way" contrasts with the Levitical way: new (in the new covenant sense — qualitatively different), living (because Christ is alive and the way is sustained by his living intercession).</p>',
    "25": '<p>A direct revelation: not neglecting to meet together, and all the more as you see the Day drawing near. The Day of the Lord — Christ\'s return — is the eschatological horizon that orients the community\'s present assembly. The assembly anticipates the great heavenly assembly (12:22-24) that the return will complete. The mutual encouragement of the assembly is the community\'s participation in what the Spirit and the Son are already doing from the right hand of God — drawing the community together in love toward the Day.',
    "37": '<p>A fulfillment: "He who is coming will come and will not delay; but my righteous one shall live by faith." The "coming one" of Habakkuk 2:3 — the vision awaiting its appointed time — is fulfilled in the coming of Christ at his first advent and anticipated in his second. Hebrews applies the text to encourage a community waiting for the parousia: the same Habakkuk-logic applies — the vision (now: Christ\'s return) awaits its time, will certainly come, and the righteous are those who live by faith through the waiting rather than shrinking back.'
  },
  "11": {
    "1": '<p>A direct revelation: faith is the substance of things hoped for, the evidence of things not seen. The definition locates faith in the economy of revelation: what faith grasps is not imagination but disclosed reality — the things hoped for are real because God has revealed them; the things not seen are the eschatological realities that the Spirit has given knowledge of. The definition situates the community in the same position as the OT cloud of witnesses: seeing the promised-but-not-yet-received, and holding firm to it as the most real thing in their world.</p>',
    "4": '<p>A shadow: Abel\'s faith-offering that was acceptable to God is the first shadow of the one true acceptable offering. Abel brought the firstborn of his flock — the best, the costly — in faith that God would receive it. Christ is the firstborn of all creation (Col 1:15) who offers himself to God as the definitively acceptable sacrifice. Abel\'s blood cried for justice; Christ\'s blood speaks the better word of forgiveness (12:24). The shadow-structure: the acceptable-in-faith offering points to the once-for-all offering that is accepted not merely for the offerer but for all who share his faith.</p>',
    "7": '<p>A shadow: Noah, warned by God about things not yet seen, built the ark in reverent faith and thereby condemned the world and became heir of righteousness that comes by faith. The pattern: divine warning about judgment not yet visible, faith-obedience that prepares a means of salvation, and the salvation of those who enter. The antitype: Christ warned by the Spirit of the coming judgment (and knowing it himself as the Son), provided by his death the salvation-vessel into which faith enters. Those who believe and are baptized are in the ark; those who do not are condemned by the flood of divine judgment.</p>',
    "17": '<p>A type: by faith Abraham, when he was tested, offered up Isaac, and he who had received the promises was in the act of offering up his only son. He considered that God was able even to raise him from the dead, from which, figuratively speaking, he did receive him back. The Aqedah is the supremely explicit OT type of the Father\'s offering of the Son: Abraham\'s willingness to give the beloved only son, the divine provision of a substitute (the ram in the thicket), and the receiving-back in a figure all correspond to the Father giving the Son, the Son\'s substitutionary death, and his resurrection. The type preserves the structure of the atoning act at the deepest level.</p>',
    "26": '<p>A shadow: Moses considered the reproach of Christ greater wealth than the treasures of Egypt, for he was looking to the reward. Moses participates in the messianic reproach across the centuries — not because he knew Christ as the community does, but because the reproach of God\'s people (which Moses took on by identifying with them) is structurally the same as the reproach of the Messiah. The community that bears the reproach of Christ (13:13) enters the same pattern: what Moses began in shadow, the community enacts in the light of the disclosed Messiah.</p>',
    "39": '<p>A direct revelation: all these, though commended through their faith, did not receive what was promised, since God had provided something better for us, that apart from us they should not be made perfect. The eschatological communality of salvation: the OT faith-heroes cannot receive the completion of their faith apart from the new covenant community. This is the revelation of the economy of grace: salvation is not individualistic-chronological (each person receives at death) but communal-eschatological (the whole people of God, across all ages, is perfected together at the parousia). The OT witnesses are waiting for the community of Christ to be complete before the common perfection is achieved.</p>'
  }
}

def main():
    existing = load_comm('mkt-christ', 'hebrews')
    merge_comm(existing, HEBREWS)
    save_comm('mkt-christ', 'hebrews', existing)
    total = sum(len(v) for v in existing.values())
    print(f'Hebrews mkt-christ: {len(existing)} chapters, {total} verses written.')

if __name__ == '__main__':
    main()
