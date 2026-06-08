"""
MKT Christ Commentary — Isaiah chapter 9
Run: python3 scripts/zc-christ-isaiah-9.py

Source data used:
- data/interlinear/isaiah.json
- data/translation/draft/mediating/isaiah.json

Key decisions in this range:
- vv. 1-2: direct fulfillment — Matt 4:15-16 cites these verses of Jesus' Galilean ministry
- vv. 6-7: direct — four throne-names; 'el gibbor = Mighty God, same as 10:21 (for YHWH)
- vv. 8-21: wrath/judgment cycle — classified revelation of God / theme; each refrain noted
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
"9": {
"1": "<p>A direct prophecy fulfilled in Christ. The opening promise — darkness reversed for Zebulun and Naphtali, the road by the sea — is cited by Matthew 4:15-16 as fulfilled in Jesus' move from Nazareth to Capernaum and the beginning of his Galilean ministry. The geography is precise: Galilee of the nations, the northern territory most exposed to foreign domination, is the first region to receive the Light. Matthew reads the verse as the programmatic announcement of where the messianic light begins to dawn.</p>",
"2": "<p>A direct prophecy. <em>The people who walked in darkness have seen a great light</em> — Matthew 4:16 quotes this of Jesus' proclamation of the kingdom in Galilee. The contrast (darkness → light) runs throughout John's Gospel (John 1:4-5; 8:12: <em>I am the light of the world</em>) and is applied to the Incarnation itself: the Light entered the darkness and the darkness could not overcome it.</p>",
"3": "<p>A shadow: the joy of harvest and the dividing of spoils describes the effect of the messianic deliverance — the abundance that follows when the oppressor is overcome. The NT applies harvest and joy imagery to the gathering of people into the kingdom (Matt 13:30; John 4:35). The multiplication of the nation points forward to the spiritual multiplication of Abraham's family through Christ (Gal 3:29).</p>",
"4": "<p>A shadow: the breaking of the oppressor's yoke <em>as on the day of Midian</em> — Gideon's unexpected victory with weak instruments (Judg 7) is the pattern. Christ breaks the ultimate oppression — sin, death, and the devil — through the cross, the most unexpected of instruments. The Gideon parallel is significant: God chooses weakness to shame strength (1 Cor 1:27-28), a pattern fulfilled completely in the crucifixion.</p>",
"5": "<p>A shadow: the burning of all war implements signals the end of the warfare age. The NT frames Christ's work as inaugurating the messianic peace — he is <em>our peace</em> who broke down the dividing wall (Eph 2:14). The full burning of boots and garments of war awaits the consummation (Rev 19:11-21), when Christ returns as the conquering King and warfare ends permanently.</p>",
"6": "<p>A direct prophecy. The child born and son given receives four throne-names that define his divine identity: <strong>pele'-yo'ets</strong> (<em>Wonderful Counselor</em> — one whose counsel is beyond ordinary, lit. wonder-of-counsel); <strong>'el gibbor</strong> (<em>Mighty God</em> — the identical phrase used in 10:21 for YHWH himself, establishing the Messiah's divine identity); <strong>'abi-'ad</strong> (<em>Everlasting Father</em> — Father of eternity, the one who rules the age that has no end); <strong>sar-shalom</strong> (<em>Prince of Peace</em> — the sovereign whose rule produces cosmic shalom). Luke 1:32-35 echoes this verse when Gabriel announces to Mary that the child will be great and called Son of the Most High, with the throne of David forever.</p>",
"7": "<p>A direct prophecy. The eternal increase of government and the endless peace on the throne of David — <em>to uphold it with justice and righteousness from now on and forevermore</em> — is fulfilled in Christ's resurrection and session at the Father's right hand. Luke 1:32-33 (the throne of David, the kingdom without end) is Gabriel's interpretation of this verse as applying to Jesus. Hebrews 1:8 applies <em>Your throne, O God, is forever and ever</em> to the Son, echoing this passage's royal-divine register.</p>",
"8": "<p>A revelation of God: YHWH's word is sent against Jacob and falls on Israel — the divine word is effective and directional, accomplishing what it announces (cf. Isa 55:11). This establishes the principle that the NT applies to the gospel: the word of the cross is the power of God (1 Cor 1:18). The same effective word that announced judgment now announces salvation in Christ — with the same certainty of fulfillment.</p>",
"9": "<p>A theme: the pride and arrogance of Ephraim — <em>in pride and arrogance of heart</em> — represents the human posture that Christ confronts and reverses. He who is meek and lowly of heart (Matt 11:29) comes against the pride that says <em>we will rebuild better</em>. The arrogance of self-sufficiency is the root of Israel's sin here; it is the same root the gospel addresses by announcing that human schemes cannot reconstruct what only God can restore.</p>",
"10": "<p>A theme: <em>the bricks have fallen, but we will build with dressed stones</em> — the human response to divine discipline is defiant self-improvement rather than repentance. This verse portrays the anti-gospel instinct: when things collapse, reinforce and upgrade by human effort. Christ's call is the inverse — not <em>we will build back better</em> but <em>repent and believe</em>. The contrast with the stone that the builders rejected (Ps 118:22; Matt 21:42) is sharp: Israel builds with fine stones while rejecting the cornerstone.</p>",
"11": "<p>A revelation of God: YHWH raises up adversaries against Israel — the Syrians before and the Philistines behind. Divine sovereignty over the nations for disciplinary purposes is a consistent theme that the NT frames in Christ: all things work together for the good of those who love God (Rom 8:28), but the same sovereignty brings judgment on those who harden their hearts. The refrain <em>his anger has not turned away</em> will be resolved only when it turns away fully at the cross (Rom 5:9).</p>",
"12": "<p>A revelation of God: Israel devoured from east and west, and still the divine hand stretched out. The recurring refrain — <em>for all this his anger has not turned away, and his hand is stretched out still</em> — is the heartbeat of this judgment cycle. The outstretched hand of judgment in Isa 9 becomes the outstretched hand of invitation in Isa 65:2 (quoted in Rom 10:21). Christ is the point where the outstretched hand of judgment and the outstretched hand of grace converge — in the cross.</p>",
"13": "<p>A theme: <em>the people did not turn to him who struck them, and they did not seek the LORD of hosts</em>. The failure of repentance under discipline is the persistent human condition. The NT frames Christ as the one who does what Israel failed to do: he seeks and saves the lost (Luke 19:10) where Israel would not seek YHWH. His vicarious penitence and obedience accomplish what Israel's stubbornness refused.</p>",
"14": "<p>A theme: YHWH removes head and tail, palm branch and reed in a single day — false leadership is stripped away by divine judgment. Christ is the true head (Eph 1:22), the true shepherd (John 10:11), who replaces the lying prophets and failed elders. The removal of corrupt leadership creates the vacancy that the messianic King fills.</p>",
"15": "<p>A theme: the elder who is honored is the head, and the prophet who teaches lies is the tail — the leadership structure of Israel is inverted by wickedness. Christ is the prophet greater than Moses (Deut 18:15; Acts 3:22), the teacher who speaks truth with authority rather than teaching lies. His teaching astonishes precisely because he does not teach as the scribes (Matt 7:29).</p>",
"16": "<p>A theme: those who guide this people lead them astray — a direct indictment of Israel's shepherds. Ezekiel 34 develops the same charge and announces YHWH himself as the true shepherd. Jesus applies this to himself (John 10:11; cf. Matt 9:36: the crowds were like sheep without a shepherd). The failure of human shepherds makes the incarnate shepherd necessary.</p>",
"17": "<p>A revelation of God: divine mercy is withheld from those who persist in wickedness — YHWH does not rejoice over their young men. This is the severe side of divine justice that the NT does not suppress: those who <em>suppress the truth in unrighteousness</em> (Rom 1:18) face the wrath revealed from heaven. The refrain continues: the outstretched hand of judgment still hangs over the unrepentant.</p>",
"18": "<p>A revelation of God: <em>wickedness burns like a fire; it consumes briers and thorns</em>. The self-consuming nature of sin — it destroys its host — is a theme that runs from the curse of Genesis 3 through to Revelation 18's self-destruction of Babylon. Christ absorbs this burning judgment at the cross, becoming a curse for us (Gal 3:13) so that the fire of divine wrath is exhausted in him.</p>",
"19": "<p>A revelation of God: through the wrath of YHWH of hosts the land is scorched and the people are fuel for the fire. The divine wrath as fire against covenant violation is real and operative — the same wrath that Isaiah's commission (ch. 6) warned would harden Israel. This is the wrath that Christ propitiates (1 John 2:2; Rom 3:25), bearing it in his person so that those who are in him receive it no more.</p>",
"20": "<p>A revelation of God: the wicked devour on the right and left and are still unsatisfied — the insatiability of sin as it turns inward. The self-destructive dynamic of unchecked wickedness is the dark mirror of Christ's provision: he is the bread of life who satisfies completely (John 6:35), while sin is the food that always leaves one emptier than before.</p>",
"21": "<p>A revelation of God: Manasseh devours Ephraim and Ephraim devours Manasseh — the fratricidal collapse of the northern kingdom, united only in opposition to Judah. The self-destruction of those who reject YHWH's order is the final note of this judgment cycle. The refrain closes: <em>for all this his anger has not turned away, and his hand is stretched out still</em>. The extended hand awaits the one who will finally satisfy divine justice — establishing the need for the atoning work that chapters 52-53 will announce.</p>"
}
}

def main():
    existing = load_comm('mkt-christ', 'isaiah')
    merge_comm(existing, ISAIAH)
    save_comm('mkt-christ', 'isaiah', existing)
    v = sum(len(vs) for vs in ISAIAH.values())
    print(f'Isaiah 9 mkt-christ: {v} verses written.')

if __name__ == '__main__':
    main()
