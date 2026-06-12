"""
MKT Echo Layer — Job chapters 8–11
Run: python3 scripts/zc-echo-job-8-11.py

Ch8:  Bildad's appeal to tradition — the ancestral wisdom test (8:8-10) — 1 Cor 10:11; Heb 1:1-2
      Does God pervert justice? — the rhetorical foundation of retribution theology (8:3) — Rom 3:5-6
      The hope of the godless perishes — the papyrus-without-water figure (8:13-14) — 1 Tim 6:17
Ch9:  How can a mortal be righteous before God? — the question that drives the entire book (9:2) — Rom 3:20
      Job cries out for a mediator who can lay his hand on both (9:33) — 1 Tim 2:5; Heb 9:15
      He stretches out the heavens alone — theophanic creation claim (9:8) — Col 1:16; Isa 40:22
Ch10: You fashioned me like clay — the creature questioning the potter (10:9) — Rom 9:20; Isa 45:9
      You gave me life and steadfast love (10:12) — Acts 17:28; Jas 1:17
      Land of darkness and deep shadow (10:21-22) — John 8:12; 1 Pet 2:9
Ch11: Can you find out the deep things of God? — Zophar's challenge (11:7) — Rom 11:33; 1 Cor 2:10
      Life brighter than noonday, darkness like morning (11:17) — John 8:12; 2 Pet 1:19
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
  "8": {
    "3": [
      {"type": "allusion", "target": "Rom 3:5", "note": "Bildad's foundational premise: Does God pervert justice? Or does the Almighty pervert the right? — the rhetorical question that anchors all three friends' argument. Their logic runs: God is just; Job suffers; therefore Job sinned. Romans 3:5-6 employs the same rhetorical form against a different purpose: 'Is God unjust to inflict wrath? By no means! For then how could God judge the world?' Paul uses the question to establish divine justice as the basis for the gospel's condemnation of sin — including Paul's own. The friends use it to condemn Job. The identical premise yields opposite pastoral conclusions: the friends use divine justice to accuse, Paul uses it to establish mercy for all."}
    ],
    "8": [
      {"type": "allusion", "target": "Heb 1:1", "note": "Bildad's appeal to the ancients: inquire of the former age; consider what the fathers found out. The argument from tradition — the accumulated wisdom of past generations as authoritative — is the wisdom tradition's normal epistemology. Hebrews 1:1-2 invokes precisely this structure before reversing it: 'Long ago, at many times and in many ways, God spoke to our fathers by the prophets, but in these last days he has spoken to us by his Son.' The fathers and their tradition are real and authoritative — but surpassed by the definitive word in the Son. Job's predicament shows the limit of ancestral wisdom: the tradition-consensus says Job sinned; God's verdict says the friends were wrong."},
      {"type": "allusion", "target": "1 Cor 10:11", "note": "The ancestors investigated and passed down their findings — Bildad assumes their cumulative experience is reliable. 1 Corinthians 10:11 uses ancestral experience in the same way but with a different hermeneutical key: 'these things happened to them as an example, but they were written down for our instruction, on whom the end of the ages has come.' The OT's recorded experiences are typologically significant for NT readers, not simply tradition-proofs. Both uses of ancestral experience acknowledge its theological weight; the NT presses beyond transmission to typological fulfillment."}
    ],
    "13": [
      {"type": "allusion", "target": "1 Tim 6:17", "note": "The hope of the godless will perish — Bildad's contrast between the one who forgets God (whose hope is cut off, whose trust is a spider's web) and the righteous (who will flourish). 1 Timothy 6:17 identifies the precise error Bildad warns against: 'as for the rich in this present age, charge them not to be haughty, nor to set their hopes on the uncertainty of riches, but on God, who richly provides us with everything to enjoy.' The hope grounded in created wealth and status is spider-web hope: intricate, visible, and ultimately incapable of bearing weight. God alone as the ground of hope is both texts' shared affirmation — though Bildad misapplies it by assuming Job's suffering proves he placed his hope wrongly."}
    ],
    "20": [
      {"type": "allusion", "target": "Phil 3:9", "note": "Bildad's assurance: God will not reject a blameless man — he will yet fill your mouth with laughter. The promise that the blameless man will not be rejected touches the question of the ground on which one stands before God. Philippians 3:9 is Paul's radical restatement of this ground: he does not wish to be found with 'a righteousness of my own that comes from the law, but that which comes through faith in Christ, the righteousness from God that depends on faith.' The blamelessness Bildad promises to the morally upright person is replaced in Christ with the alien righteousness that no suffering can remove, because it rests not on moral achievement but on the completed work of Another."}
    ]
  },
  "9": {
    "2": [
      {"type": "allusion", "target": "Rom 3:20", "note": "Job's central anguished question: how can a mortal be in the right before God? — the problem that drives the entire book. This is not rhetorical flourish; Job is asking what ground of righteousness could possibly sustain him in a legal contest with the Almighty. Romans 3:20 answers the question with equal directness: 'by works of the law no human being will be justified in his sight, since through the law comes knowledge of sin.' Job's intuition — that no creature can establish righteousness before God by its own resources — is Paul's foundational anthropological premise. Both Job and Paul arrive at the same cliff's edge; only the gospel provides the bridge Job anticipates in verse 33."}
    ],
    "8": [
      {"type": "allusion", "target": "Col 1:16", "note": "He alone stretched out the heavens and treads on the waves of the sea — Job's doxological confession of divine power even in the midst of his protest. The one who stretched out the heavens is identified in Colossians 1:16 as the Son: 'all things were created through him and for him.' Job's solitary Creator (he alone) is the undivided divine act that the NT distributes through the trinitarian lens: the Father creates, but the eternal Son is the agent through whom all things — including the stretched-out heavens — were made."},
      {"type": "allusion", "target": "Isa 40:22", "note": "He stretches out the heavens like a curtain — Job 9:8 and Isaiah 40:22 share identical language for the creative act. Isaiah deploys it as comfort for the exiled: the God who stretches out the heavens like a curtain reduces princes to nothing. Job deploys it as awe-filled terror: this is the God with whom he must contend. The same divine majesty that is comfort in Isaiah becomes the problem in Job — which is itself instructive about how the same attribute of God can be experienced differently depending on one's sense of standing before him. The gospel resolves this asymmetry: in Christ the God who stretches out the heavens is Immanuel, God with us."}
    ],
    "33": [
      {"type": "allusion", "target": "Heb 9:15", "note": "Job's explicit longing for a mediator: there is no arbiter between us who might lay his hand on both. He needs someone who can represent him to God and God to him — one who shares both natures and stands in both relationships. Hebrews 9:15: 'Therefore he is the mediator of a new covenant, so that those who are called may receive the promised eternal inheritance, since a death has occurred that redeems them from the transgressions committed under the first covenant.' Christ is the arbiter Job could not find: the one who lays his hand on both — fully God and fully human — and whose death satisfies the covenant's justice while securing the creature's inheritance. Job's longing is among the most explicit anticipations of the incarnation in the OT."}
    ],
    "34": [
      {"type": "allusion", "target": "Heb 4:16", "note": "If only the mediator would take his rod away, so that his dread would not terrify me — then I could speak without fear. Job's desire is to approach God without the terror that divine holiness produces in fallen creatures. Hebrews 4:16: 'Let us then with confidence draw near to the throne of grace, that we may receive mercy and find grace to help in time of need.' The confidence that Hebrews describes is exactly what Job craves and cannot find: an approach to the divine presence without terror. The Epistle grounds this confidence in the high priest who was tested in every way as we are — the one who himself, in Gethsemane, faced what Job faced and passed through it on behalf of those who could not."}
    ]
  },
  "10": {
    "8": [
      {"type": "allusion", "target": "Ps 139:14", "note": "Your hands fashioned and made me — and now you turn around and destroy me. Job's protest over the contradiction between God's careful craftsmanship and present apparent abandonment. Psalm 139:14: 'I praise you, for I am fearfully and wonderfully made. Wonderful are your works; my soul knows it very well.' The Psalm turns the same premise — the Creator's intimate involvement in making — toward doxology; Job turns it toward lament. Both are theological responses to the same reality; the difference is not the doctrine but the existential situation. The incarnation takes both responses seriously: Christ himself on the cross cries the abandonment lament while being the one through whom all things were made."}
    ],
    "9": [
      {"type": "allusion", "target": "Rom 9:20", "note": "Remember that you have made me like clay; and will you return me to dust? — Job addressing God as the Potter who now seems to be crushing his own workmanship. Romans 9:20: 'But who are you, O man, to answer back to God? Will what is molded say to its molder, Why have you made me like this?' Paul quotes Isaiah and uses the clay-potter figure to establish divine sovereignty. Job actually speaks the lament that Paul forbids — and God does not rebuke Job for it; the friends who rebuke him are the ones whose speech God judges as wrong (42:7). This distinguishes protest-lament addressed to God (which God hears) from accusation against God's character (which the friends commit by defending God against Job)."}
    ],
    "12": [
      {"type": "allusion", "target": "Acts 17:28", "note": "You granted me life and steadfast love, and your care has preserved my spirit — Job's acknowledgment that even his current life is sustained by the God against whom he protests. Acts 17:28: 'In him we live and move and have our being.' Paul quotes a Greek poet to articulate what Job intuits: the creature's very existence is held in the divine sustaining care, not merely at creation but at every moment. Job's protest does not deny this — the preservation of his spirit is what makes his lament possible. The incarnation takes Acts 17:28 to its furthest point: the Son who sustains all things by his word (Heb 1:3) himself entered the created order he sustains."}
    ],
    "21": [
      {"type": "allusion", "target": "John 8:12", "note": "Before I go to the place of no return, to the land of darkness and deep shadow — Job's anticipation of Sheol as the horizon of his hopeless condition. John 8:12: 'I am the light of the world. Whoever follows me will not walk in darkness, but will have the light of life.' The land of darkness and deep shadow is transformed in the NT not by denying Sheol's reality but by the light of resurrection entering it: Christ went into the realm of death (1 Pet 3:19) and came out the other side, abolishing death's finality and bringing life and immortality to light (2 Tim 1:10). Job's hopeless horizon becomes the very place Christ enters and transforms."}
    ]
  },
  "11": {
    "7": [
      {"type": "allusion", "target": "Rom 11:33", "note": "Can you find out the deep things of God? Can you find out the limit of the Almighty? — Zophar's challenge to Job, intended to humble him but pointing to a genuine truth about divine incomprehensibility. Romans 11:33: 'Oh, the depth of the riches and wisdom and knowledge of God! How unsearchable are his judgments and how inscrutable his ways!' Zophar's rhetorical challenge and Paul's doxological exclamation both point to the same divine hiddenness. The difference: Zophar uses divine incomprehensibility to end Job's protest; Paul arrives at it as the summit of his exposition of the gospel — the mystery of election and mercy that surpasses human accounting. The hiddenness of God is not a conversation-stopper but the mystery into which the gospel reaches."},
      {"type": "allusion", "target": "1 Cor 2:10", "note": "Zophar asks: can you find out the deep things of God? — the answer assumed to be no, meant to silence Job's questioning. 1 Corinthians 2:10: 'these things God has revealed to us through the Spirit. For the Spirit searches everything, even the depths of God.' Paul's answer to Zophar's question is unexpected: yes — not by human investigation but by divine revelation through the Spirit. The deep things (bathē) of God have been disclosed in Christ and applied by the Spirit. What Zophar meant as a silencing question becomes in the NT the announcement of what has actually been revealed."}
    ],
    "17": [
      {"type": "allusion", "target": "2 Pet 1:19", "note": "Your life will be brighter than the noonday; its darkness will be like the morning — Zophar's promise of restoration if Job repents. The language of progressive light-increase — darkness becoming morning, morning ascending to noonday — is the idiom of eschatological hope. 2 Peter 1:19: 'We have the prophetic word more fully confirmed...as a lamp shining in a dark place, until the day dawns and the morning star rises in your hearts.' The light-to-noonday arc that Zophar promises conditionally is given unconditionally in Christ: the morning star of his resurrection breaks in the believer's heart and will be consummated in the noonday of the new creation when there is no more night."}
    ]
  }
}

def main():
    e = load_echo('job')
    merge_echo(e, ECHOES)
    save_echo('job', e)
    count = sum(len(v) for v in ECHOES.values())
    print(f'job echo: wrote entries for {count} chapters across ch 8-11')

if __name__ == '__main__':
    main()
