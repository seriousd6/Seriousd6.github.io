"""
MKT Echo Layer — Job chapters 33–35 (Elihu's first three speeches)
Run: python3 scripts/zc-echo-job-33-35.py

Ch33: The Spirit made me; breath of the Almighty gives me life (33:4) — Gen 2:7; John 20:22
      God speaks once, twice — through dreams, through suffering (33:14-15) — Heb 1:1-2
      The mediator-messenger who says 'Deliver him from the pit' (33:23-24) — 1 Tim 2:5; Heb 7:25
      He redeems the soul from going down into the pit (33:28) — 1 Pet 1:18; Ps 49:15
Ch34: If God gathered his spirit and breath to himself, all flesh would perish (34:14-15) — Acts 17:25; 28
      Shall one who hates justice govern? — Elihu's defense of divine justice (34:17) — Rom 3:26
      His eyes are on the ways of a man; no darkness where evildoers can hide (34:21-22) — Heb 4:13
Ch35: Where is God my Maker who gives songs in the night? (35:10) — Ps 42:8; Acts 16:25
      Faith and sight — you do not see him, yet he is there (35:14) — Heb 11:1; 2 Cor 5:7
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
  "33": {
    "4": [
      {"type": "allusion", "target": "Gen 2:7", "note": "The Spirit of God has made me; the breath of the Almighty gives me life — Elihu grounds his authority to speak in the same divine creative act that constituted Adam. Genesis 2:7: 'then the Lord God formed the man of dust from the ground and breathed into his nostrils the breath of life, and the man became a living creature.' The breath (nišmat šadday) Elihu claims as the source of his life is the same nišmāh that God breathed into Adam. This grounding of human speech and wisdom in divine breath anticipates the NT pattern: John 20:22, where the risen Christ breathes on the disciples and says 'receive the Holy Spirit' — the new creation's counterpart to Genesis 2:7's first creation breath."},
      {"type": "allusion", "target": "John 20:22", "note": "The breath of the Almighty gives me life — Elihu's appeal to the animating breath as the source of wisdom and speech. John 20:22: 'And when he had said this, he breathed on them and said to them, Receive the Holy Spirit.' The risen Christ's breath-giving act is the new creation's counterpart to Elihu's appeal: just as God breathed life into Adam and just as Elihu claims that same breath as the source of his capacity for speech, so Christ breathes the Spirit into his disciples as the source of their capacity to speak and witness. The divine breath that creates also inspires — and the NT grounds both in the life of the risen Son."}
    ],
    "14": [
      {"type": "allusion", "target": "Heb 1:1", "note": "God speaks in one way, and in two, though man does not perceive it — through dreams, through visions of the night (33:15), through pain on the bed (33:19), through the mediating messenger (33:23). Elihu's taxonomy of divine communication is the OT background for the Hebrews prologue: 'Long ago, at many times and in many ways, God spoke to our fathers by the prophets, but in these last days he has spoken to us by his Son.' The many-ways/many-times structure Elihu describes — dreams, suffering, messenger — is exactly what Hebrews 1:1 acknowledges as real before declaring its surpassment by the definitive speech in the Son."}
    ],
    "23": [
      {"type": "allusion", "target": "1 Tim 2:5", "note": "If there be for him a messenger, a mediator, one of the thousand, to declare to man what is right for him — and he is gracious to him, and says, Deliver him from going down into the pit. Elihu's vision of the mediating messenger who intercedes for the sufferer and effects his deliverance from death is the most developed anticipation of the mediatorial office in the poetic books. 1 Timothy 2:5: 'For there is one God, and there is one mediator between God and men, the man Christ Jesus.' Elihu describes the role; Paul names the person. The messenger from the thousand (miʾalep) who declares what is right and procures deliverance from the pit is the figure Christ fulfills as the one mediator whose death achieves the ransom (2:6)."},
      {"type": "allusion", "target": "Heb 7:25", "note": "The mediator-messenger says to God: Deliver him from going down into the pit; I have found a ransom. The ransoming declaration — the mediator speaking the price of deliverance into existence — is the functional form of Christ's priestly intercession. Hebrews 7:25: 'he is able to save to the uttermost those who draw near to God through him, since he always lives to make intercession for them.' Elihu's mediator makes a single declaration that effects deliverance; the Hebrews Christ makes perpetual intercession that effects perpetual salvation. The permanent nature of Christ's intercession surpasses and fulfills the momentary grace of Elihu's envisioned messenger."}
    ],
    "28": [
      {"type": "allusion", "target": "1 Pet 1:18", "note": "He has redeemed my soul from going down into the pit, and my life shall look upon the light — the song of the restored person who has been ransomed from the descent into Sheol. 1 Peter 1:18-19: 'you were ransomed from the futile ways inherited from your forefathers, not with perishable things such as silver or gold, but with the precious blood of Christ, like that of a lamb without blemish or spot.' Elihu's ransom-word (kōper, 33:24) and the ransom-song of the delivered person (33:28) describe the experience of redemption whose price the NT names: not a ransom of silver or gold but the blood of the one whose intervention Elihu could only sketch as a merciful messenger from the thousand."}
    ]
  },
  "34": {
    "14": [
      {"type": "allusion", "target": "Acts 17:25", "note": "If he should set his heart to it and gather to himself his spirit and his breath, all flesh would perish together, and man would return to dust. Elihu's point is that the creature's existence is entirely contingent on the Creator's active sustaining will — a withdrawal of breath means immediate death. Acts 17:25: 'nor is he served by human hands, as though he needed anything, since he himself gives to all mankind life and breath and everything.' Paul and Elihu agree on the foundational contingency: the creature breathes only because the Creator actively gives breath. Elihu uses this to defend divine prerogative; Paul uses it to establish that the Creator cannot be in our debt — we owe him everything, including the breath with which we argue about him."},
      {"type": "allusion", "target": "Acts 17:28", "note": "All flesh would perish if God gathered his spirit and breath to himself — the creature is radically dependent on the Creator's moment-by-moment sustaining. Acts 17:28: 'In him we live and move and have our being.' The 'in him' of Acts 17:28 is the NT's positive expression of what Elihu states negatively: remove the divine sustaining and all perishes; maintain it and we live. Elihu's argument is about divine sovereignty over life; Paul's quotation of a Greek poet is about the intimacy of creaturely existence within the divine sustaining — and becomes the platform for the proclamation of the resurrection."}
    ],
    "17": [
      {"type": "allusion", "target": "Rom 3:26", "note": "Shall one who hates justice govern? Will you condemn him who is righteous and mighty? — Elihu's assertion that the God who rules must be the God who is just. Romans 3:26: 'It was to show his righteousness at the present time, so that he might be just and the justifier of the one who has faith in Jesus.' Paul's resolution of the justice-problem is the cross: God is simultaneously just (the sin is punished) and the justifier (the sinner is acquitted). Elihu insists on God's justice as a logical necessity of governance; the NT demonstrates how that justice is maintained and extended in the gospel without compromising either attribute."}
    ],
    "21": [
      {"type": "allusion", "target": "Heb 4:13", "note": "His eyes are on the ways of a man, and he sees all his steps. There is no gloom or deep darkness where evildoers may hide themselves — the radical divine omniscience that makes concealment impossible. Hebrews 4:13: 'And no creature is hidden from his sight, but all are naked and exposed to the eyes of him to whom we must give account.' Elihu's statement and Hebrews 4:13 make the same claim: divine sight penetrates every darkness; nothing is hidden. Hebrews places this divine omniscience in the context of the living and active word of God that discerns all (4:12) — the word that is ultimately the incarnate Son who, as the one to whom we give account, is the same one who intercedes for us (4:14-16)."}
    ]
  },
  "35": {
    "10": [
      {"type": "allusion", "target": "Ps 42:8", "note": "But none says, Where is God my Maker, who gives songs in the night — Elihu's observation that those who cry out in suffering do not seek God himself but only relief from suffering. The phrase 'songs in the night' is the rare NT-facing element here: Psalm 42:8: 'at night his song is with me, a prayer to the God of my life.' Both the Psalm and Job 35 acknowledge that the night of suffering is precisely where divine song can be heard — but only by those who seek the Maker himself rather than merely deliverance from darkness. Paul and Silas singing in the Philippian prison at midnight (Acts 16:25) is the NT enactment of what Elihu describes: the song that comes from the God who gives songs in the night."},
      {"type": "allusion", "target": "Acts 16:25", "note": "God my Maker gives songs in the night — the paradox of praise in darkness, which Elihu names as the mark of those who genuinely seek God. Acts 16:25: 'About midnight Paul and Silas were praying and singing hymns to God, and the prisoners were listening to them.' The Philippian prison scene is the literal enactment of Job 35:10: songs in the night, addressed to God who gives them. Where the suffering masses in Elihu's speech cry out without seeking the Maker who gives songs, Paul and Silas demonstrate what that seeking looks like in practice — and the result (the earthquake, the jailer's conversion) is the NT's demonstration of what God who gives songs in the night can accomplish."}
    ],
    "14": [
      {"type": "allusion", "target": "Heb 11:1", "note": "How much less when you say that you do not see him — Elihu's point that the case is even more urgent when Job claims that God is hidden and inaccessible. The invisibility of God is the condition in which faith operates. Hebrews 11:1: 'Now faith is the assurance of things hoped for, the conviction of things not seen.' Elihu's observation that not-seeing is the normal condition of the creature in relation to the Creator is the anthropological premise on which Hebrews 11's entire gallery of faith operates. The heroes of faith all acted without seeing — and their acting is what makes their trust intelligible as faith rather than sight."},
      {"type": "allusion", "target": "2 Cor 5:7", "note": "You do not see him — the condition Job is in and the condition Elihu references as the normal circumstance of the creature before God. 2 Corinthians 5:7: 'for we walk by faith, not by sight.' Paul's compressed axiom is the NT articulation of the condition Elihu addresses: the creature relates to God without the kind of vision that would make trust unnecessary. The incarnation does not abolish this structure — even those who saw Jesus in the flesh required faith; the resurrection appearances happened to those already disciples. The NT does not resolve the hiddenness Elihu names but transforms it: the one not seen is now the risen Lord whose unseen presence is the church's constant companion."}
    ]
  }
}

def main():
    e = load_echo('job')
    merge_echo(e, ECHOES)
    save_echo('job', e)
    count = sum(len(v) for v in ECHOES.values())
    print(f'job echo: wrote entries for {count} chapters across ch 33-35')

if __name__ == '__main__':
    main()
