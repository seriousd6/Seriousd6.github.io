"""
Echo Commentary — Proverbs chapters 10–12
Run: python3 scripts/zc-echo-proverbs-10-12.py
Key NT echoes:
- Prov 10:12 -> 1 Pet 4:8 / Jas 5:20 (love covers all offenses; direct NT quotation)
- Prov 10:11 -> John 4:14 / John 7:38 (mouth of righteous = fountain of life; living water)
- Prov 10:25 -> Matt 7:24-27 (righteous on everlasting foundation; wise/foolish builders)
- Prov 11:2  -> Jas 4:6 / Phil 2:3 (pride brings disgrace; humility brings wisdom)
- Prov 11:24-25 -> 2 Cor 9:6-7 (give freely and grow richer; generous sower)
- Prov 11:30 -> John 15:5 / Rev 22:2 (fruit of righteous = tree of life)
- Prov 12:17-18 -> Jas 3:5-10 (reckless words pierce; tongue of wise brings healing)
- Prov 12:28 -> John 14:6 (path of righteousness is life; no death along that road)
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
    "10": {
        "1": [
            {"type": "allusion", "target": "Matt 3:17", "note": "A wise son brings joy to his father — the paradigmatic wise son finds its fulfilment in Christ whom the Father declares 'my beloved Son, in whom I am well pleased' (Matt 3:17); Jesus is the perfect son who never brings grief to the Father"}
        ],
        "11": [
            {"type": "allusion", "target": "John 4:14", "note": "The mouth of the righteous is a fountain of life — Jesus identifies himself as the source of this living water: 'whoever drinks the water I give will never thirst; the water I give will become a spring of water welling up to eternal life' (John 4:14); the proverb's fountain-of-life image finds its personal fulfilment in Christ"},
            {"type": "allusion", "target": "John 7:38", "note": "The mouth of the righteous is a fountain of life — Jesus cries at the Feast of Tabernacles: 'whoever believes in me, as Scripture has said, rivers of living water will flow from within them' (John 7:38); the fountain-of-life that flows from the righteous one is the Spirit given through Christ"}
        ],
        "12": [
            {"type": "quotation", "target": "1 Pet 4:8", "note": "Love covers all offenses — Peter quotes this proverb directly: 'above all, keep loving one another earnestly, since love covers a multitude of sins' (1 Pet 4:8); the covering-love principle is grounded in God's love through Christ which covers the sins of those who trust him"},
            {"type": "allusion", "target": "Jas 5:20", "note": "Love covers all offenses — James echoes the same text: 'whoever brings back a sinner from his wandering will save his soul from death and will cover a multitude of sins' (Jas 5:20); the Christological ground is Christ's atoning work which covers sin permanently (Ps 32:1; Rom 4:7)"}
        ],
        "17": [
            {"type": "allusion", "target": "John 14:6", "note": "Whoever keeps instruction is on the path of life — Jesus declares himself to be that path: 'I am the way, and the truth, and the life' (John 14:6); the instruction that leads to life is ultimately the word of Christ himself (John 6:68: 'you have the words of eternal life')"}
        ],
        "19": [
            {"type": "allusion", "target": "Jas 1:19", "note": "When words are many, sin is not far off, but whoever holds back his words is prudent — James applies this principle: 'let every person be quick to hear, slow to speak, slow to anger' (Jas 1:19); Jesus modeled the same wisdom, speaking with precision and authority rather than verbosity"}
        ],
        "25": [
            {"type": "allusion", "target": "Matt 7:24", "note": "The righteous stand on an everlasting foundation — Jesus builds on this proverb's image in the parable of the wise and foolish builders: 'everyone who hears these words of mine and does them will be like a wise man who built his house on the rock' (Matt 7:24); Christ himself is the everlasting foundation (1 Cor 3:11: 'no one can lay a foundation other than that which is laid, which is Jesus Christ')"}
        ],
        "27": [
            {"type": "allusion", "target": "John 10:10", "note": "The fear of the LORD adds length to life — Jesus promises the fullest realization of this: 'I came that they may have life and have it abundantly' (John 10:10); and 'whoever believes in me, though he die, yet shall he live' (John 11:25); length of life becomes eternal life in Christ"}
        ]
    },
    "11": {
        "2": [
            {"type": "allusion", "target": "Jas 4:6", "note": "When pride arrives, disgrace follows, but with the humble comes wisdom — James quotes this principle: 'God opposes the proud but gives grace to the humble' (Jas 4:6, citing Prov 3:34); Christ embodies the humility that receives wisdom: 'he humbled himself by becoming obedient to the point of death' (Phil 2:8), and was therefore exalted"}
        ],
        "14": [
            {"type": "allusion", "target": "1 Cor 12:12", "note": "Without guidance a people falls, but in abundance of counselors comes safety — Paul's vision of the body of Christ (1 Cor 12:12-27) embodies this principle: the church is a community of mutually-dependent members where no one has all wisdom; Christ as the head provides the ultimate guidance (Col 1:18)"}
        ],
        "24": [
            {"type": "allusion", "target": "2 Cor 9:6", "note": "One gives freely and grows richer; another withholds what he should give and only comes to poverty — Paul draws directly on this paradox: 'whoever sows sparingly will also reap sparingly, and whoever sows bountifully will also reap bountifully' (2 Cor 9:6); the christological ground is Christ who gave himself freely (2 Cor 8:9: 'though he was rich, yet for your sake he became poor')"}
        ],
        "25": [
            {"type": "allusion", "target": "Luke 6:38", "note": "A generous person will be enriched, and whoever waters others will himself be watered — Jesus extends this principle: 'give, and it will be given to you. Good measure, pressed down, shaken together, running over, will be put into your lap' (Luke 6:38); the generosity of the gospel creates a community of mutual flourishing"}
        ],
        "28": [
            {"type": "allusion", "target": "Luke 12:21", "note": "Whoever trusts in his wealth will fall — Jesus warns in the parable of the rich fool: 'so is the one who lays up treasure for himself and is not rich toward God' (Luke 12:21); 1 Tim 6:17 quotes the same wisdom tradition: 'as for the rich in this present age, charge them not to be haughty, nor to set their hopes on the uncertainty of riches'"}
        ],
        "30": [
            {"type": "allusion", "target": "John 15:5", "note": "The fruit of the righteous is a tree of life — Jesus identifies himself as the source of this fruit-bearing life: 'I am the vine; you are the branches. Whoever abides in me and I in him, he it is that bears much fruit' (John 15:5); the tree of life reappears in Rev 22:2 in the new Jerusalem, its fruit for the healing of the nations"},
            {"type": "allusion", "target": "Rev 22:2", "note": "The fruit of the righteous is a tree of life — the tree of life from Gen 2-3 reappears in Rev 22:2 at the center of the new Jerusalem, its leaves for the healing of the nations; the righteous one whose fruit is a tree of life is ultimately Christ, from whose cross life flows to all who believe (John 12:32)"}
        ],
        "31": [
            {"type": "allusion", "target": "1 Pet 4:18", "note": "If the righteous receive what they deserve on earth, how much more the wicked and the sinner — Peter quotes this verse directly (LXX of Prov 11:31): 'if it is hard for the righteous to be saved, what will become of the ungodly and the sinner?' (1 Pet 4:18); the seriousness of divine judgment applies to all"}
        ]
    },
    "12": {
        "4": [
            {"type": "allusion", "target": "Eph 5:25", "note": "An excellent wife is a crown to her husband — Paul takes up the husband-wife image and elevates it to the pattern of Christ and the church: 'husbands, love your wives, as Christ loved the church and gave himself up for her' (Eph 5:25); the excellent wife who is a crown to her husband is the pattern that the church-as-bride becomes when adorned by Christ's love (Rev 21:2)"}
        ],
        "17": [
            {"type": "allusion", "target": "Acts 1:8", "note": "A truthful witness gives honest testimony — the disciples are called to be Christ's witnesses (Acts 1:8); Jesus himself is 'the faithful and true witness' (Rev 3:14; Rev 1:5), the ultimate truthful witness whose testimony is the gospel itself"}
        ],
        "18": [
            {"type": "allusion", "target": "Jas 3:5", "note": "Reckless words pierce like a sword, but the tongue of the wise brings healing — James elaborates this proverb at length (Jas 3:5-10): 'the tongue is a small member yet it boasts of great things... it sets on fire the entire course of life'; Christ's words are the healing tongue: John 6:63 'the words I have spoken to you are spirit and life'"},
            {"type": "allusion", "target": "Eph 4:29", "note": "The tongue of the wise brings healing — Paul applies this: 'let no corrupting talk come out of your mouths, but only such as is good for building up, as fits the occasion, that it may give grace to those who hear' (Eph 4:29); Christ-formed speech builds up rather than piercing"}
        ],
        "25": [
            {"type": "allusion", "target": "Matt 11:28", "note": "Anxiety in a man's heart weighs him down, but a good word makes him glad — Jesus gives the ultimate good word to the anxious: 'come to me, all who labor and are heavy laden, and I will give you rest' (Matt 11:28); his word is the relief for the weighed-down heart that Proverbs envisions"}
        ],
        "28": [
            {"type": "allusion", "target": "John 14:6", "note": "In the path of righteousness is life, and along that road there is no death — Jesus declares himself to be this path: 'I am the way, and the truth, and the life' (John 14:6); and 'whoever believes in me shall never die' (John 11:26). The path-of-righteousness that leads to life and bypasses death is Christ himself — the road is a person"}
        ]
    }
}

existing = load_echo('proverbs')
merge_echo(existing, PROVERBS_ECHOES)
save_echo('proverbs', existing)

for ch in sorted(PROVERBS_ECHOES.keys(), key=int):
    count = sum(len(vv) for vv in PROVERBS_ECHOES[ch].values())
    print(f'  ch{ch}: {count} echo entries written')
