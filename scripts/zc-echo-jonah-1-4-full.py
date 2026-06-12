#!/usr/bin/env python3
"""
MKT Echo Layer — Jonah chapters 1–4 (chs 2 and 4 missing; 1 and 3 partial)
Run: python3 scripts/zc-echo-jonah-1-4-full.py

Echo type: OT → NT direction.
Ch 1:17 (sign of Jonah → Matt 12:40) and ch 3:5 (Nineveh repents → Matt 12:41)
already present — adding only absent chapters.

Key connections for ch 2:
- 2:2 "from the belly of Sheol I cried" → Acts 2:24 (death could not hold)
- 2:6 pit/bars closed upon me / brought up from the pit → Acts 2:27 (not left in Hades)
- 2:9 "salvation belongs to YHWH" → Rev 7:10 (salvation to God and the Lamb)

Key connections for ch 4:
- 4:2 gracious/merciful/hesed formula (Exod 34:6) → Luke 15:20-24 (prodigal father)
- 4:5-9 Jonah sulking outside city → Luke 15:25-32 (elder brother who won't rejoice)
- 4:10-11 divine pity argument → Luke 15:4-7 (shepherd leaves 99 for one lost sheep)
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

JONAH_ECHOES = {
    "2": {
        "2": [
            {
                "type": "allusion",
                "target": "Acts 2:24",
                "note": "Jonah's cry 'from the belly of Sheol I cried' (mibeten Sheol shivati) is the cry from the deepest place of death available in the OT imagination. Acts 2:24 announces its fulfillment: God raised Jesus up, 'loosing the pangs of death, because it was not possible for him to be held by it.' What was impossible for death to retain in the resurrection is what Jonah's prayer enacts as the pattern — the cry from the pit that YHWH answers by bringing up the one who went down. Jonah prefigures the pattern; Jesus is the substance."
            }
        ],
        "6": [
            {
                "type": "allusion",
                "target": "Acts 2:27",
                "note": "Jonah's description of his descent — 'I went down to the land whose bars closed upon me forever; yet you brought up my life from the pit (shahat)' — establishes the pattern of descent into death and divine rescue. Peter's Pentecost sermon applies Psalm 16:10 to Jesus: 'you will not abandon my soul to Hades, nor let your Holy One see corruption' (Acts 2:27). Both texts articulate the same theology: the one who descends to the place of the dead will be brought back up, because YHWH's faithfulness exceeds death's finality. Jonah's three days are the prototype; Jesus's three days are the fulfillment."
            }
        ],
        "9": [
            {
                "type": "allusion",
                "target": "Rev 7:10",
                "note": "Jonah's closing declaration in the psalm — 'Salvation belongs to YHWH' (la-YHWH ha-yeshuah) — is one of the OT's most compressed theological affirmations. Revelation 7:10 places this declaration on the lips of the great multitude from every nation standing before the throne: 'Salvation belongs to our God who sits on the throne, and to the Lamb.' The Hebrew yeshuah (salvation) becomes the acclamation of the eschatological assembly — what Jonah confessed in the belly of the fish from the depths of near-death, the redeemed multitude confesses in the throne room of full life. The trajectory from one prophet's crisis-confession to the universal eschatological acclamation is complete."
            }
        ]
    },
    "4": {
        "2": [
            {
                "type": "allusion",
                "target": "Luke 15:20-24",
                "note": "Jonah's complaint against divine mercy deploys the covenant name formula from Exodus 34:6-7 — 'gracious (channun), merciful (rachum), slow to anger (erekh appayim), abounding in steadfast love (rav hesed)' — but as an accusation rather than worship. He knew YHWH would relent, and this infuriates him. Jesus's parable of the prodigal son enacts this same divine character: the father runs to the returning son (Luke 15:20) and throws a feast — exactly the lavish grace Jonah resents. The father's reception of the prodigal is the embodiment of the very formula Jonah quotes. Christ incarnates what Jonah could only quote and resent."
            }
        ],
        "3": [
            {
                "type": "allusion",
                "target": "Phil 1:21-24",
                "note": "Jonah's request to die — 'It is better for me to die than to live' (tov moti me-chayyai) — arises from resentment at divine mercy extended to those he considers undeserving. Paul faces the same tension between life and death in Philippians 1:21-24 but from the opposite orientation: 'to die is gain' because of the desire to be with Christ, but 'to remain in the flesh is more necessary' for the sake of others. Jonah wants to die because he cannot bear the grace shown to Nineveh; Paul is willing to live because grace must be announced to others. The prophet and the apostle stand at opposite poles of the same life-death question."
            }
        ],
        "5": [
            {
                "type": "allusion",
                "target": "Luke 15:25-28",
                "note": "Jonah sitting east of the city, watching to see what would become of it, refusing to enter and celebrate God's mercy — is the structural parallel to the elder brother in the parable of the prodigal son (Luke 15:25-28). The elder brother refuses to enter the feast when his father receives the returning prodigal with celebration. Both Jonah and the elder brother are outside, resentful of grace extended to those they consider less deserving. The father in the parable (as YHWH in Jonah 4) comes out to the sulking figure and reasons with him. Jesus's parable is shaped by the Jonah narrative's structural logic."
            }
        ],
        "9": [
            {
                "type": "allusion",
                "target": "Matt 6:25-34",
                "note": "Jonah's disproportionate grief over the withered plant — 'I am angry enough to die' — reveals a heart that can be moved by the loss of temporary shade but not by the salvation of 120,000 people. Jesus addresses this inversion of values in the Sermon on the Mount: do not be anxious about what is temporary (food, clothing, plants); consider the lilies, how they grow and how they wither (Matt 6:25-34). Jonah's comfort rested in the qiqayon plant that perished overnight — the same disproportionate investment in the transient over the eternal that Jesus identifies as the failure mode of anxious discipleship."
            }
        ],
        "11": [
            {
                "type": "allusion",
                "target": "Luke 15:4-7",
                "note": "The book's final question — 'Should I not pity Nineveh, that great city, in which there are more than 120,000 persons who do not know their right hand from their left, and also much cattle?' — is the OT form of Jesus's argument from divine compassion in the parable of the lost sheep (Luke 15:4-7): 'What man of you, having a hundred sheep, if he has lost one of them, does not leave the ninety-nine... and seek the one that is lost?' Both arguments move from the Creator's care for his creatures to justify the rescue of those who are lost or ignorant. In both cases, the question is rhetorical — the answer is self-evident to anyone who knows the character of YHWH."
            }
        ]
    }
}

def main():
    existing = load_echo('jonah')
    merge_echo(existing, JONAH_ECHOES)
    save_echo('jonah', existing)
    print('Jonah 1-4 echoes written.')

if __name__ == '__main__':
    main()
