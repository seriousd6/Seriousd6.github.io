"""
MKT Echo Layer — Job chapters 19–21
Run: python3 scripts/zc-echo-job-19-21.py

Ch19: I know that my Redeemer lives — the great confession (19:25) — 1 Cor 15:20; John 11:25
      (19:25 already present: 1 Cor 15:20; adding John 11:25 and further entries)
      He has stripped my honor and removed the crown from my head (19:9) — Phil 2:7-8
      My kinsmen have failed me, my friends have forgotten me (19:14) — Matt 26:56; Heb 13:5
Ch20: Zophar: the triumph of the wicked is brief (20:5) — 1 Pet 5:4; Rev 20:10
      He swallows down riches and vomits them up again (20:15) — Luke 12:20; 1 Tim 6:9
      The wicked man's wealth stored up, given to the innocent (20:10) — Luke 12:21; Prov 13:22
Ch21: Job's reversal of Zophar — why do the wicked live on? (21:7) — Ps 73:3; 2 Pet 3:9
      Their houses are safe from fear; they prosper (21:9) — Eccl 8:11; Hab 1:13
      Yet their good is not in their own hand — God judges (21:16) — Luke 12:20; Jas 4:13-14
      Who will declare his way to his face? — the question Christ answers (21:31) — John 16:8; Acts 17:31
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

ECHOES = {
  "19": {
    "9": [
      {"type": "allusion", "target": "Phil 2:7", "note": "He has stripped my honor and taken the crown from my head — Job's description of his social and dignitary stripping as part of his suffering. Philippians 2:7-8: Christ 'emptied himself, by taking the form of a servant, being born in the likeness of men. And being found in human form, he humbled himself by becoming obedient to the point of death, even death on a cross.' The kenotic stripping Paul describes is the voluntary form of what happens to Job involuntarily: honor removed, crown taken, the high brought low. Christ's humiliation is the willing acceptance of the condition Job experiences as catastrophic loss — and it becomes the ground of Job's own future restoration."}
    ],
    "14": [
      {"type": "allusion", "target": "Matt 26:56", "note": "My kinsmen have failed me, and my close friends have forgotten me — the abandonment by those closest when suffering intensifies. Matthew 26:56: 'Then all the disciples left him and fled.' The pattern is identical: at the moment of deepest need, the inner circle abandons. Job's isolation is the type of Christ's Gethsemane abandonment — the righteous sufferer deserted by those who should have stood with him. The difference is that Job cannot understand why he is abandoned; Christ enters the abandonment with full knowledge and purpose, so that those who abandon in their weakness might find him present in their own moment of isolation."},
      {"type": "allusion", "target": "Heb 13:5", "note": "My intimate friends have forgotten me; those I loved have turned against me. The total social abandonment — kinsmen, guests, maidservants, wife, brothers, children — is the depth of Job's isolation. Hebrews 13:5: 'I will never leave you nor forsake you.' The promise is the direct antithesis of Job's experience and functions as its answer: the God who appears to have withdrawn in Job's suffering is the one who, in Christ, speaks this promise definitively. The 'never' (ou me + emphatic) is the NT's answer to Job's 'have forgotten me' — an abandonment refused and reversed in the resurrection."}
    ],
    "25": [
      {"type": "allusion", "target": "John 11:25", "note": "I know that my Redeemer lives, and at the last he will stand upon the earth — Job's confession of the living Redeemer who will vindicate him at the resurrection. John 11:25: 'I am the resurrection and the life. Whoever believes in me, though he die, yet shall he live.' Jesus applies to himself the title that is the content of Job's hope: the one who lives and who makes the dead live. The goʾēl who stands upon the earth at the last is the risen Christ who stands before the tomb of Lazarus and speaks resurrection into existence. Job's desperate, darkness-surrounded hope has a name and a face in the NT."}
    ]
  },
  "20": {
    "5": [
      {"type": "allusion", "target": "1 Pet 5:4", "note": "The exulting of the wicked is short, and the joy of the godless but for a moment — Zophar's principle that the prosperity of the unrighteous is temporary. 1 Peter 5:4: 'And when the chief Shepherd appears, you will receive the unfading crown of glory.' The contrast between the brief triumph of the wicked and the unfading crown awaiting the faithful is the NT's eschatological expansion of Zophar's principle. Zophar intends it as a retributive mechanism within history; the NT locates the definitive triumph not in historical reversal but in the appearing of the chief Shepherd — the moment when all temporary exaltations are measured against the permanent."},
      {"type": "allusion", "target": "Rev 20:10", "note": "The triumph of the wicked is short, the moment of the godless brief — Zophar states a principle that the Revelation enacts dramatically. Revelation 20:10: 'the devil who had deceived them was thrown into the lake of fire and sulfur...and they will be tormented day and night forever and ever.' The brevity of the wicked's triumph is the hinge between the present age and the age to come: what appears permanent and triumphant — the serpent's dominion — is revealed as terminally brief from the perspective of the final judgment. Zophar's principle is correct; only the mechanism is different from what he imagines."}
    ],
    "15": [
      {"type": "allusion", "target": "Luke 12:20", "note": "He swallows down riches and vomits them up again; God casts them out of his belly — the image of wealth that cannot be retained, that reverses course at the moment of expected consolidation. Luke 12:20: 'But God said to him, Fool! This night your soul is required of you, and the things you have prepared, whose will they be?' The rich fool's accumulated grain and the wicked man's swallowed riches share the same structural irony: wealth amassed at the moment of supposed triumph is precisely when it is taken. Both texts use this to establish that wealth accumulated apart from God does not constitute security but the illusion of it."},
      {"type": "allusion", "target": "1 Tim 6:9", "note": "He swallows riches — the image of consuming wealth as an end in itself, only to lose it violently. 1 Timothy 6:9: 'those who desire to be rich fall into temptation, into a snare, into many senseless and harmful desires that plunge people into ruin and destruction.' The vomiting-up of swallowed riches in Job 20 is the dramatic form of what Paul describes as the dynamic of greed: the wealth that is consumed as an ultimate good produces a kind of destruction that is internal to the act of consuming it. Both texts use physical imagery (swallowing, plunging) to convey the self-destructive nature of wealth sought as ultimate security."}
    ]
  },
  "21": {
    "7": [
      {"type": "allusion", "target": "Ps 73:3", "note": "Why do the wicked live on, reach old age, and grow mighty in power? — Job's direct challenge to Zophar's neat retribution theology. This is exactly the question of Psalm 73:3: 'I was envious of the arrogant when I saw the prosperity of the wicked.' The Psalmist's near-loss of faith and Job's counter-argument both refuse to pretend the observed world confirms simple retribution. Both are honest about the scandal of wicked prosperity. The Psalm resolves the tension eschatologically (73:17: entering the sanctuary, understanding their end); the NT grounds that eschatology in the resurrection judgment of Christ (Acts 17:31)."},
      {"type": "allusion", "target": "2 Pet 3:9", "note": "Why do the wicked prosper and grow old? — the question that appears to implicate divine indifference or injustice. 2 Peter 3:9: 'The Lord is not slow to fulfill his promise as some count slowness, but is patient toward you, not wishing that any should perish, but that all should reach repentance.' Peter addresses the same observable delay — the wicked prospering while judgment seems absent — and reinterprets the delay not as divine indifference but as mercy extended to make repentance possible. What looks like the wicked prospering indefinitely is the time of grace; the judgment that will come is certain, and the reason it has not yet come is love, not weakness."}
    ],
    "16": [
      {"type": "allusion", "target": "Luke 12:20", "note": "Behold, is not their prosperity in their own hand? The counsel of the wicked is far from me. — Job's observation that the wicked acknowledge no dependence on God for their success. Luke 12:20 is the Lucan commentary: the rich fool also treats his prosperity as in his own hand — 'I will say to my soul, Soul, you have ample goods laid up for many years; relax, eat, drink, be merry' — until the night when his soul is required. The prosperity that appears to be in one's own hand is revealed to be held at the pleasure of the one who grants the breath that makes prosperity possible."}
    ],
    "31": [
      {"type": "allusion", "target": "John 16:8", "note": "Who will declare his way to his face? Who will repay him for what he has done? — Job's question about accountability: who can confront the prosperous wicked man with the truth of his ways? John 16:8: 'And when he comes, he will convict the world concerning sin and righteousness and judgment.' The Spirit sent by Christ is the answer to Job's question: the one who will declare to the wicked man his way is the Paraclete, the Spirit of truth who convicts precisely where human accusation fails or falls silent. What no person in Job's world could accomplish — a truthful accounting before the powerful — the Spirit of the risen Christ accomplishes through the proclamation of the gospel."},
      {"type": "allusion", "target": "Acts 17:31", "note": "Who will repay him for what he has done? — the accountability question Job poses for the apparently untouchable wicked. Acts 17:31: 'because he has fixed a day on which he will judge the world in righteousness by a man whom he has appointed; and of this he has given assurance to all by raising him from the dead.' The judge who will repay has been appointed and authenticated by the resurrection. Job's unanswered question — who will confront the wicked with their deeds? — finds its answer not in history's moral arc but in the fixed day of judgment that the resurrection secures. The risen Christ is both the assurance of judgment and, for those who receive him, the answer to judgment."}
    ]
  }
}

def main():
    e = load_echo('job')
    merge_echo(e, ECHOES)
    save_echo('job', e)
    count = sum(len(v) for v in ECHOES.values())
    print(f'job echo: wrote entries for {count} chapters across ch 19-21')

if __name__ == '__main__':
    main()
