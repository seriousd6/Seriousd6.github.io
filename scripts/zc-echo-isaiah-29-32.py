"""
echo | Isaiah | 29-32 | python3 scripts/zc-echo-isaiah-29-32.py

Key echo decisions:
- Isa 29:13 already cited (Matt 15:8-9 / Mark 7:6-7 quote); adding v16 (Rom 9:20-21 potter/clay),
  v18 (Matt 11:5 blind-see/deaf-hear messianic signs), v19 (Matt 5:5 meek)
- Isa 30:15 "repentance and rest" -> Matt 11:28-30 (my yoke is easy, rest for souls)
- Isa 30:21 "this is the way" -> John 14:6; John 10:4 (sheep know his voice)
- Isa 30:33 Topheth -> Matt 25:41 (eternal fire prepared)
- Isa 31:5 hovering-bird -> Matt 23:37 (hen gathers chicks)
- Isa 32:1 king in righteousness -> Luke 1:32-33; Rev 19:11
- Isa 32:15 Spirit poured from on high -> Acts 2:17 (Pentecost / Joel 2:28)
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

ISAIAH_ECHOES = {
    "29": {
        "16": [
            {"type": "citation", "target": "Rom 9:20-21", "note": "Should the potter be regarded like clay? — Paul develops the potter/clay analogy directly from this verse in Rom 9:20-21 to defend divine sovereignty in election; the creature challenging the Creator echoes Isaiah's rebuke of Israel's presumption."}
        ],
        "18": [
            {"type": "fulfillment", "target": "Matt 11:5", "note": "In that day the deaf will hear and the blind will see — Jesus cites this exact cluster of messianic signs when answering John the Baptist's question (Matt 11:5; Luke 7:22): the blind receive sight, the deaf hear, as proof that the kingdom has come."}
        ],
        "19": [
            {"type": "allusion", "target": "Matt 5:5", "note": "The meek will find renewed joy and the poorest will exult in the Holy One — the beatitude Blessed are the meek (Matt 5:5) and Blessed are the poor in spirit (Matt 5:3) draw on this cluster of Isaiah's reversal promises; the kingdom belongs to those whom Isaiah describes here."}
        ]
    },
    "30": {
        "8": [
            {"type": "allusion", "target": "Rev 1:11", "note": "Write it before them on a tablet, inscribe it in a book as a witness forever — the command to inscribe prophetic testimony permanently anticipates the Apocalypse's opening command (Rev 1:11: write what you see in a book); prophecy preserved in writing as enduring witness."}
        ],
        "9": [
            {"type": "allusion", "target": "Acts 7:51", "note": "A rebellious people, deceptive children who refuse to hear the instruction of the LORD — Stephen's indictment in Acts 7:51 (You stiff-necked people, you always resist the Holy Spirit) echoes this Isaianic diagnosis of Israel's chronic resistance to prophetic instruction."}
        ],
        "15": [
            {"type": "allusion", "target": "Matt 11:28-30", "note": "In repentance and rest you shall be saved; in quietness and trust is your strength — Jesus draws on this when he says Come to me all who are weary and I will give you rest (Matt 11:28-29); the Isaianic rest of repentant trust becomes the rest Christ offers to all who come to him."},
            {"type": "allusion", "target": "Heb 4:9-11", "note": "The rest promised through quietness and trust anticipates Hebrews' theological development of Sabbath-rest (Heb 4:9-11); those who believe enter that rest, the sabbath-rest that remains for the people of God."}
        ],
        "18": [
            {"type": "allusion", "target": "2 Pet 3:9", "note": "The LORD waits to be gracious to you and rises up to show mercy — the divine patience that waits for repentance is the same quality Peter cites in 2 Pet 3:9 (the Lord is not slow; he is patient, not wishing any to perish but for all to come to repentance)."}
        ],
        "19": [
            {"type": "allusion", "target": "Luke 18:7", "note": "He will surely be gracious at the sound of your cry; as soon as he hears he will answer — Jesus draws on the pattern of the God who hears and answers the cries of his people when he assures his disciples that the Father will answer those who cry to him day and night (Luke 18:7-8)."}
        ],
        "21": [
            {"type": "allusion", "target": "John 10:4", "note": "Your ears will hear a voice behind you saying, This is the way, walk in it — the guiding voice of the shepherd is the theme of John 10:4 (the sheep follow him because they know his voice); the LORD's guiding voice is fulfilled in Christ who is the way (John 14:6)."},
            {"type": "allusion", "target": "John 14:6", "note": "This is the way — the divine voice pointing to the right path is fulfilled in Christ's I am the way (John 14:6); what Isaiah describes as the word of the LORD behind you guiding your steps is incarnated in the one who is himself the way."}
        ],
        "26": [
            {"type": "allusion", "target": "Rev 21:23", "note": "The moon will be like the sun and the sun seven times brighter — the intensified light of the eschatological age anticipates Rev 21:23 where the city has no need of sun or moon for the Lamb is its light; Isaiah's hyperbole becomes the new creation's reality."}
        ],
        "27": [
            {"type": "allusion", "target": "Rev 19:15", "note": "The name of the LORD comes from afar, burning with anger, with a devouring fire — the divine warrior imagery of the coming judgment (Rev 19:11-15) draws on this Isaianic portrait of the LORD arriving in fiery wrath to execute judgment on the nations."}
        ],
        "33": [
            {"type": "allusion", "target": "Matt 25:41", "note": "Topheth has long been prepared for the king — the Valley of Hinnom/Topheth as the place of fire and judgment is the background for Jesus' warning about Gehenna (the fire prepared for the devil, Matt 25:41); Topheth becomes the prototype of the final judgment's fire."}
        ]
    },
    "31": {
        "3": [
            {"type": "allusion", "target": "John 3:6", "note": "The Egyptians are human and not God; their horses are flesh and not spirit — the flesh/spirit contrast that defines the inadequacy of human power is the same contrast Jesus uses with Nicodemus (John 3:6: what is born of flesh is flesh, born of Spirit is spirit); only divine power saves."},
            {"type": "allusion", "target": "2 Cor 10:4", "note": "Flesh-versus-spirit in military terms: relying on horses (flesh) versus the LORD (spirit) anticipates Paul's declaration that our weapons are not of the flesh but have divine power (2 Cor 10:4); the spiritual warfare Paul describes is grounded in this Isaianic contrast."}
        ],
        "5": [
            {"type": "allusion", "target": "Matt 23:37", "note": "Like birds hovering over their young, so the LORD will shield Jerusalem — Jesus applies this very imagery to himself: How often I wanted to gather your children as a hen gathers her chicks under her wings (Matt 23:37 / Luke 13:34), identifying himself as the one who longs to do what Isaiah describes the LORD doing."}
        ],
        "8": [
            {"type": "allusion", "target": "Rev 19:15", "note": "The Assyrian will fall by a sword that is not of any man — the defeat of the enemy by divine rather than human agency points forward to Rev 19:15 (from Christ's mouth comes a sharp sword with which to strike down the nations); the sword that is not human is the word of God."}
        ],
        "9": [
            {"type": "allusion", "target": "Matt 16:18", "note": "His stronghold will crumble in terror at the LORD's signal — the crumbling stronghold of the enemy anticipates Christ's declaration that the gates of Hades will not prevail against his church (Matt 16:18); the LORD's signal is the resurrection signal that defeats death's stronghold."}
        ]
    },
    "32": {
        "1": [
            {"type": "type", "target": "Luke 1:32-33", "note": "A king will reign in righteousness and rulers will govern with justice — the righteous king is the messianic promise (Jer 23:5: the righteous Branch) fulfilled in Christ; Luke 1:32-33 applies it directly: the LORD God will give him the throne of David and his kingdom will have no end."},
            {"type": "allusion", "target": "Rev 19:11", "note": "The king reigning in righteousness anticipates Rev 19:11 (the rider on the white horse, called Faithful and True, who in righteousness judges and makes war); the Isaianic vision of the righteous king finds its eschatological fulfillment here."}
        ],
        "2": [
            {"type": "allusion", "target": "John 4:14", "note": "Like streams of water in a dry land, like the shade of a great rock in a weary land — Jesus is both the rock (1 Cor 10:4) and the source of living water (John 4:14; 7:38); the shelter and refreshment Isaiah describes for the righteous king's reign is fulfilled in Christ."}
        ],
        "3": [
            {"type": "allusion", "target": "Matt 13:16", "note": "The eyes of those who see will no longer be closed, the ears of those who hear will listen — this reversal of the blindness/deafness of Isa 6:9-10 finds partial fulfillment in Jesus' words to the disciples: Blessed are your eyes because they see, your ears because they hear (Matt 13:16); full restoration comes in the kingdom."}
        ],
        "15": [
            {"type": "fulfillment", "target": "Acts 2:17", "note": "Until the Spirit is poured upon us from on high, and the wilderness becomes a fruitful orchard — the Pentecost event is the fulfillment of this outpouring; Peter cites the parallel passage (Joel 2:28-29) in Acts 2:17 (I will pour out my Spirit on all people), and Isaiah 32:15 is the same promise from a different angle."},
            {"type": "allusion", "target": "John 7:38-39", "note": "The Spirit poured out from on high transforming the wilderness anticipates Jesus' promise of rivers of living water (John 7:38-39); John explicitly identifies this with the Spirit, whom those who believed would receive after Jesus was glorified."}
        ],
        "17": [
            {"type": "allusion", "target": "Jas 3:18", "note": "The fruit of righteousness will be peace, and the result of righteousness will be quietness and confidence — James 3:18 (Peacemakers who sow in peace raise a harvest of righteousness) draws on this Isaianic connection between righteousness and peace as fruit; the Spirit-renewed community bears this fruit."},
            {"type": "allusion", "target": "Phil 4:7", "note": "The result of righteousness will be quietness and confidence forever — Paul's promise that the peace of God which transcends all understanding will guard your hearts (Phil 4:7) echoes this Isaianic vision of the settled quietness that righteousness produces in the Spirit-renewed age."}
        ],
        "18": [
            {"type": "allusion", "target": "Rev 21:3-4", "note": "My people will dwell in peaceful homes, in secure dwellings, in undisturbed resting places — the shalom dwelling of the people of God anticipates Rev 21:3-4 (God's dwelling place is now among the people; he will wipe every tear); Isaiah's promise of the secure dwelling finds its eschatological fulfillment in the new creation."}
        ],
        "20": [
            {"type": "allusion", "target": "Matt 13:23", "note": "Blessed are you who sow beside every stream — the beatitude of generous, well-watered sowing anticipates the parable of the sower (Matt 13:23: the one who hears the word and understands it produces a crop); and 2 Cor 9:6 (whoever sows generously will reap generously)."}
        ]
    }
}

def main():
    data = load_echo('isaiah')
    merge_echo(data, ISAIAH_ECHOES)
    total = sum(len(v) for ch in data.values() for v in ch.values())
    chs = sorted(data.keys(), key=int)
    print(f'Isaiah echoes: {len(chs)} chapters, {total} entries total')
    save_echo('isaiah', data)

if __name__ == '__main__':
    main()
