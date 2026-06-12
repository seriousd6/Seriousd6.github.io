"""
Echo Commentary — Proverbs chapters 16–18
Run: python3 scripts/zc-echo-proverbs-16-18.py
Key NT echoes:
- Prov 16:9  -> Jas 4:13-15 (man plans, LORD directs steps; "if the Lord wills")
- Prov 16:18 -> 1 Cor 10:12 / Luke 14:11 (pride before a fall; Christ reverses pride/humility order)
- Prov 16:24 -> Col 4:6 (pleasant words = honey; let speech be seasoned with salt)
- Prov 16:33 -> Acts 1:26 (lot cast, LORD decides; choosing Matthias by lot)
- Prov 17:3  -> 1 Pet 1:7 (crucible/furnace tests metals; God tests hearts through trial)
- Prov 17:17 -> John 15:13 (friend loves at all times; Christ's greater love unto death)
- Prov 18:10 -> Acts 2:21 / Rom 10:13 (name of LORD strong tower; call on the name)
- Prov 18:24 -> John 15:13-15 (friend closer than a brother; Jesus calls disciples friends)
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

PROVERBS_ECHOES = {
    "16": {
        "1": [
            {"type": "allusion", "target": "Jas 4:13", "note": "To man belong the plans of the heart, but from the LORD comes the reply of the tongue — James applies this principle: 'come now, you who say, \"today or tomorrow we will go into such and such a town\"' (Jas 4:13), followed by the correction that all human plans are subject to 'if the Lord wills' (v15); the human planner who depends on divine direction finds its fullest expression in Jesus who said 'not my will, but yours' (Luke 22:42)"}
        ],
        "3": [
            {"type": "allusion", "target": "Matt 6:33", "note": "Commit to the LORD whatever you do, and he will establish your plans — Jesus teaches the same principle of whole-life entrusting: 'seek first the kingdom of God and his righteousness, and all these things will be added to you' (Matt 6:33); the one who perfectly committed all to the Father is Christ, whose plans were established through death and resurrection (Acts 2:23-24)"}
        ],
        "9": [
            {"type": "allusion", "target": "Jas 4:15", "note": "In their hearts humans plan their course, but the LORD establishes their steps — James applies this directly: 'instead you ought to say, \"if the Lord wills, we will live and do this or that\"' (Jas 4:15); Christ models the perfectly directed life: 'my food is to do the will of him who sent me' (John 4:34), and 'the Son can do nothing of his own accord, but only what he sees the Father doing' (John 5:19)"}
        ],
        "18": [
            {"type": "allusion", "target": "1 Cor 10:12", "note": "Pride goes before destruction, a haughty spirit before a fall — Paul applies this as a warning to the self-confident: 'let anyone who thinks that he stands take heed lest he fall' (1 Cor 10:12); the great reversal is Christ himself who 'humbled himself by becoming obedient to the point of death' (Phil 2:8) and was therefore exalted — the inverse of the proud who fall"},
            {"type": "allusion", "target": "Luke 14:11", "note": "Pride goes before destruction — Jesus states the gospel's inversion explicitly: 'everyone who exalts himself will be humbled, and he who humbles himself will be exalted' (Luke 14:11); this is not merely ethical advice but the pattern of the kingdom, exemplified in the incarnation and resurrection of Christ"}
        ],
        "20": [
            {"type": "allusion", "target": "John 20:29", "note": "Whoever gives heed to instruction prospers, and blessed is the one who trusts in the LORD — the macarism (beatitude) form echoes the beatitudes of Matt 5:3-11 and reaches its NT peak in Jesus's word to Thomas: 'blessed are those who have not seen and yet have believed' (John 20:29); trust in the LORD becomes trust in Christ as LORD (John 20:28)"}
        ],
        "24": [
            {"type": "allusion", "target": "Col 4:6", "note": "Gracious words are a honeycomb, sweet to the soul and healing to the bones — Paul instructs: 'let your speech always be gracious, seasoned with salt, so that you may know how you ought to answer each person' (Col 4:6); Jesus exemplified this: 'all spoke well of him and marveled at the gracious words that were coming from his mouth' (Luke 4:22)"}
        ],
        "33": [
            {"type": "allusion", "target": "Acts 1:26", "note": "The lot is cast into the lap, but its every decision is from the LORD — the early church applied this principle directly: the disciples cast lots to choose Matthias, trusting 'you, Lord, who know the hearts of all' (Acts 1:24-26); the decisive lot of redemption is the cross itself, where what appeared to be chance was the 'definite plan and foreknowledge of God' (Acts 2:23)"}
        ]
    },
    "17": {
        "3": [
            {"type": "allusion", "target": "1 Pet 1:7", "note": "The crucible for silver and the furnace for gold, but the LORD tests the heart — Peter applies the refining image to the trial of faith: 'the tested genuineness of your faith — more precious than gold that perishes though it is tested by fire' (1 Pet 1:7); Christ passed through the ultimate furnace of suffering so that those united to him might emerge as refined gold (Jas 1:3-4)"}
        ],
        "5": [
            {"type": "allusion", "target": "Matt 25:40", "note": "Whoever mocks the poor shows contempt for their Maker — Jesus identifies himself with the poor and the least: 'as you did it to one of the least of these my brothers, you did it to me' (Matt 25:40); contempt for the poor is contempt for Christ, who though rich became poor for our sakes (2 Cor 8:9)"}
        ],
        "17": [
            {"type": "allusion", "target": "John 15:13", "note": "A friend loves at all times, and a brother is born for a time of adversity — Jesus fulfills this proverb supremely: 'greater love has no one than this, that someone lay down his life for his friends' (John 15:13); the friend who loves at all times, even unto death, is Christ; and those who follow his self-giving love embody this friendship toward one another (1 John 3:16)"}
        ],
        "22": [
            {"type": "allusion", "target": "Phil 4:4", "note": "A cheerful heart is good medicine, but a crushed spirit dries up the bones — Paul grounds the call to joy in the resurrection of Christ: 'rejoice in the Lord always; again I will say, rejoice' (Phil 4:4); the peace that surpasses understanding (Phil 4:7) is the medicine Christ's victory provides for the crushed spirit"}
        ],
        "28": [
            {"type": "allusion", "target": "Jas 1:19", "note": "Even fools are thought wise if they keep silent, and discerning if they hold their tongues — James applies the same wisdom: 'let every person be quick to hear, slow to speak, slow to anger' (Jas 1:19); Jesus modeled this restraint — 'he was oppressed and afflicted, yet he did not open his mouth' (Isa 53:7) — and in the trial before Pilate, his silence confounded his accusers"}
        ]
    },
    "18": {
        "5": [
            {"type": "allusion", "target": "Acts 10:34", "note": "It is not good to be partial to the wicked and so deprive the innocent of justice — Peter declares that God himself is impartial: 'God shows no partiality, but in every nation anyone who fears him and does what is right is acceptable to him' (Acts 10:34); Christ's impartial justice is enacted in the cross where 'he condemned sin in the flesh' (Rom 8:3), not showing partiality to human pride"}
        ],
        "10": [
            {"type": "allusion", "target": "Acts 2:21", "note": "The name of the LORD is a fortified tower; the righteous run to it and are safe — Peter quotes Joel 2:32 at Pentecost: 'everyone who calls on the name of the LORD shall be saved' (Acts 2:21); Paul echoes it: 'everyone who calls on the name of the Lord will be saved' (Rom 10:13), identifying the LORD of the tower explicitly with Jesus (Rom 10:9); the name that is the strong tower is now the name of Jesus"},
            {"type": "allusion", "target": "Rom 10:13", "note": "The name of the LORD is a fortified tower — Paul quotes Joel: 'everyone who calls on the name of the Lord will be saved' (Rom 10:13), and in context identifies 'the Lord' with Jesus (Rom 10:9): 'if you confess with your mouth that Jesus is Lord and believe in your heart that God raised him from the dead, you will be saved'; the strong tower is a person, and his name saves"}
        ],
        "24": [
            {"type": "allusion", "target": "John 15:13", "note": "There is a friend who sticks closer than a brother — Jesus establishes this supreme friendship: 'no longer do I call you servants... I have called you friends' (John 15:15), and gives the ultimate proof: 'greater love has no one than this, that someone lay down his life for his friends' (John 15:13); the friend closer than a brother is Christ, who by his cross makes those far off into his own family (Eph 2:13-19)"},
            {"type": "allusion", "target": "Heb 2:11", "note": "There is a friend who sticks closer than a brother — the author of Hebrews describes Christ's solidarity in even stronger terms: 'for he who sanctifies and those who are sanctified all have one source. That is why he is not ashamed to call them brothers' (Heb 2:11); the friend closer than a brother becomes the brother who was not ashamed to share flesh and blood (Heb 2:14)"}
        ]
    }
}

existing = load_echo('proverbs')
merge_echo(existing, PROVERBS_ECHOES)
save_echo('proverbs', existing)

for ch in sorted(PROVERBS_ECHOES.keys(), key=int):
    count = sum(len(vv) for vv in PROVERBS_ECHOES[ch].values())
    print(f'  ch{ch}: {count} echo entries written')
