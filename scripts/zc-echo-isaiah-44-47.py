"""
echo | Isaiah | 44-47 | python3 scripts/zc-echo-isaiah-44-47.py

Key echo decisions:
- Isa 44:3 Spirit poured out -> Acts 2:17; John 7:38-39 (Pentecost)
- Isa 44:22 transgressions swept away -> Heb 9:14; Col 2:14 (debt cancelled)
- Isa 45:9 clay/potter -> Rom 9:20-21 (direct citation context)
- Isa 45:22 turn to me, all ends of earth -> Rom 10:13; Rev 22:17
- Isa 46:4 I will carry you -> John 10:28-29; Heb 13:5
- Isa 46:10 end declared from beginning -> Rev 22:13 Alpha/Omega; Acts 2:23
- Isa 46:13 righteousness/salvation near -> Rom 3:21-22; Heb 9:28
- Isa 47:7 queen forever -> Rev 18:7 DIRECT CITATION (Babylon says same words)
- Isa 47:9 loss/widowhood in one day -> Rev 18:8 (Babylon's plagues in one day)
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
    "44": {
        "3": [
            {"type": "fulfillment", "target": "Acts 2:17", "note": "I will pour out my Spirit on your offspring — this Spirit-outpouring is directly fulfilled at Pentecost; Peter cites the parallel Joel 2:28 in Acts 2:17, but Isaiah 44:3 is the same promise from a different angle: water on thirsty ground, Spirit on descendants, the new-creation refreshment of dry souls."},
            {"type": "allusion", "target": "John 7:38-39", "note": "Streams on dry ground / Spirit poured out — Jesus applies this to himself: whoever believes in me, rivers of living water will flow from within them (John 7:38-39), identifying the Spirit as the fulfillment of Isaiah's promise; the one who gives the Spirit is the one through whom the outpouring comes."}
        ],
        "22": [
            {"type": "allusion", "target": "Col 2:14", "note": "I have swept away your transgressions like a cloud, your sins like morning mist — Paul describes the same act through the cross: God cancelled the written code (the debt record) that stood against us and nailed it to the cross (Col 2:14); what Isaiah describes meteorologically, the atonement accomplishes forensically."},
            {"type": "allusion", "target": "Heb 9:14", "note": "Transgressions swept away so Israel can return — the return enabled by sin-removal points to the cleansing power of Christ's blood: how much more will the blood of Christ, who offered himself unblemished to God, cleanse our consciences from dead works to serve the living God (Heb 9:14)."}
        ],
        "24": [
            {"type": "allusion", "target": "John 1:3", "note": "The LORD your Redeemer, who formed you in the womb, who made all things — the creator-Redeemer who stretches out the heavens alone and spreads out the earth is identified by John with the eternal Word through whom all things were made (John 1:3); the one who redeems is the same one who first created."}
        ]
    },
    "45": {
        "9": [
            {"type": "allusion", "target": "Rom 9:20-21", "note": "Woe to him who quarrels with his Maker — will the clay say to the potter, What are you making? — Paul draws on this exact potter/clay language in Rom 9:20-21 (shall what is formed say to the one who formed it, Why did you make me like this?) to defend divine sovereignty in election; the Isaianic polemic against creaturely presumption becomes Paul's defense of God's freedom."}
        ],
        "14": [
            {"type": "allusion", "target": "Matt 1:23", "note": "Truly God is with you, and there is no other — the nations' confession that God is present in his people finds its fulfillment in Immanuel: God with us (Matt 1:23 citing Isa 7:14); in Christ, God's presence with his people reaches its irreversible climax."}
        ],
        "17": [
            {"type": "allusion", "target": "Heb 5:9", "note": "Israel is saved by the LORD with an everlasting salvation — the eternal, inexhaustible nature of this salvation is realized in Christ: he became the source of eternal salvation for all who obey him (Heb 5:9); what Isaiah calls everlasting salvation is what Hebrews identifies as the salvation secured by the eternal Son through his once-for-all offering."}
        ],
        "21": [
            {"type": "allusion", "target": "1 Tim 2:5", "note": "There is no God apart from me — a righteous God and a Savior — there is none besides me. The exclusive Savior claim of the one God points to Paul's declaration that there is one God and one mediator between God and humanity, Christ Jesus (1 Tim 2:5); in Christ, the one-God of Isaiah is revealed as the one Savior of all."}
        ],
        "22": [
            {"type": "allusion", "target": "Rev 22:17", "note": "Turn to me and be saved, all the ends of the earth — this universal invitation from the one God is the heartbeat of Revelation's final invitation: the Spirit and the bride say Come! Let the one who is thirsty come; let the one who wishes take the free gift of the water of life (Rev 22:17); the call to all the ends of the earth is the Great Commission in prophetic form."},
            {"type": "allusion", "target": "Rom 10:13", "note": "Turn to me and be saved, all the ends of the earth — Paul's gospel promise that everyone who calls on the name of the Lord will be saved (Rom 10:13 citing Joel 2:32) operates within the theological frame Isaiah establishes here: the exclusive-God who is alone the Savior invites the entire world to turn and be saved."}
        ]
    },
    "46": {
        "4": [
            {"type": "allusion", "target": "John 10:28-29", "note": "Even to your old age I am he, even to gray hairs I will carry you — the God who carries his people through every stage of life and never lets them fall is the Good Shepherd: no one can snatch them from my hand, and no one can snatch them from my Father's hand (John 10:28-29); the carrying God of Isaiah is the carrying Shepherd of John."},
            {"type": "allusion", "target": "Heb 13:5", "note": "I have made you, and I will carry you; I will sustain and rescue you — the divine constancy of care across the whole lifespan anticipates Heb 13:5 (Never will I leave you; never will I forsake you) and Matt 28:20 (I am with you always, to the end of the age); the one who carries from birth to old age is the one who promises perpetual presence."}
        ],
        "9": [
            {"type": "allusion", "target": "1 Cor 8:6", "note": "I am God, and there is no other; I am God, and there is none like me — the monotheistic foundation Paul builds on in 1 Cor 8:6 (for us there is but one God, the Father, from whom all things came and for whom we live; and one Lord, Jesus Christ, through whom all things came) rests on this Isaianic declaration; the one God revealed in Christ is the God Isaiah proclaims here."}
        ],
        "10": [
            {"type": "allusion", "target": "Rev 22:13", "note": "Declaring the end from the beginning, and from ancient times things not yet done, saying: my purpose will stand — the God who declares the end from the beginning is the one who calls himself the Alpha and Omega, the First and the Last, the Beginning and the End (Rev 22:13); Christ assumes this title (Rev 1:8,17; 22:13), claiming the divine prerogative of commanding all history from its source to its goal."},
            {"type": "allusion", "target": "Acts 2:23", "note": "My purpose will stand and I will accomplish all that I please — the divine purposefulness that controls history includes the cross: Jesus was handed over by God's deliberate plan and foreknowledge (Acts 2:23); what looked like the enemy's triumph was God's eternal purpose being executed precisely on schedule, the end declared from the beginning."}
        ],
        "13": [
            {"type": "allusion", "target": "Rom 3:21-22", "note": "I am bringing my righteousness near — it is not far off — and my salvation will not linger — the imminent arrival of divine righteousness and salvation is the theme of Paul's gospel: the righteousness of God has been made known, to which the Law and the Prophets testify (Rom 3:21-22); what Isaiah sees approaching in the distance, Paul announces has arrived in the death and resurrection of Christ."},
            {"type": "allusion", "target": "Heb 9:28", "note": "My salvation will not linger; I will grant salvation in Zion — the salvation that does not linger is the once-for-all offering of Christ: Christ was sacrificed once to take away the sins of many; and he will appear a second time, not to bear sin, but to bring salvation to those who are waiting for him (Heb 9:28); Isaiah's approaching salvation becomes Hebrews' two-advent framework."}
        ]
    },
    "47": {
        "8": [
            {"type": "allusion", "target": "Rev 18:7", "note": "You who say in your heart, I am, and there is no one besides me — Babylon's self-deifying I am echoes the divine name and its claim to uniqueness (Isa 45:22; 46:9); Rev 18:7 explicitly cites this verse as the boast of spiritual Babylon: She says in her heart, I sit as a queen and I am no widow, and I will never see mourning — the same pride Isaiah deconstructs here."},
            {"type": "citation", "target": "Rev 18:7", "note": "I am, and there is no one besides me... I will be a mistress forever — Rev 18:7 directly quotes the parallel verse 7 (I will be queen forever) in its portrait of Babylon/Rome: She says in her heart, I sit as queen, I am no widow, and will never see grief. John identifies spiritual Rome as the fulfillment of Babylon's boast; Isaiah's deconstruction is applied to the final empire."}
        ],
        "9": [
            {"type": "allusion", "target": "Rev 18:8", "note": "Both of these — loss of children and widowhood — shall come upon you in a moment, in a single day — the sudden collapse of Babylon in a single day is the exact language of Rev 18:8: therefore in one day her plagues will come — death, mourning, and famine — and she will be consumed by fire; John maps Isaiah's oracle against historical Babylon onto the eschatological fall of spiritual Babylon."}
        ],
        "11": [
            {"type": "allusion", "target": "Rev 18:10", "note": "Evil shall come upon you suddenly, which you will not know how to conjure away; disaster shall fall upon you which you cannot atone for — the sudden unexpected collapse recalls Rev 18:10: in one hour your judgment has come; the merchants of the earth weep over Babylon fallen in an hour, matching Isaiah's prediction of disaster that cannot be charmed away."}
        ],
        "14": [
            {"type": "allusion", "target": "Rev 20:14-15", "note": "They are like straw; the fire devours them; they cannot save themselves from the power of the flame — the fire that devours the wise men of Babylon who cannot save themselves anticipates the lake of fire in Rev 20:14-15, where no human wisdom or power provides escape; the impotence of Babylon's sorcerers before divine fire is the prototype of final judgment."}
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
