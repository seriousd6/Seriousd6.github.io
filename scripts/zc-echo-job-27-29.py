"""
Echo layer — Job chapters 27–29
Run: python3 scripts/zc-echo-job-27-29.py

Ch 27: Job's third discourse — he holds fast to his righteousness while describing
       the certain doom of the wicked (the lot God assigns to the godless, vv8-23).
Ch 28: The Wisdom Hymn — surveying all human exploration, only God knows where
       Wisdom is; "the fear of the LORD is wisdom" (v28) is the chapter's verdict.
Ch 29: Job's nostalgic lament for the days of God's favour — his description of his
       former righteous ministry anticipates the messianic portrait of Isa 61 and
       Christ's own description of his works in Luke 7:22 / Matt 11:4-5.
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

JOB_ECHOES = {
  "27": {
    "5": [
      {"type": "allusion", "target": "Heb 10:23", "note": "Until I die I will not surrender my integrity — Job's refusal to release his righteousness under extreme pressure; Hebrews exhorts: hold fast the confession of our hope without wavering, for he who promised is faithful; Job's tenacious integrity under unjust suffering is the OT model for the endurance Hebrews calls the community to in the face of persecution"}
    ],
    "8": [
      {"type": "allusion", "target": "Luke 12:20", "note": "What hope does the godless man have, however much he gains, when God takes away his life? — the rhetorical question anticipates the rich fool parable: God said to him, Fool! This night your soul is required of you; both texts expose the bankruptcy of wealth accumulated without God; the stored possessions return nothing when life is demanded back"}
    ],
    "18": [
      {"type": "allusion", "target": "Matt 6:19", "note": "He builds his house as a moth builds its web — the wicked man's accumulated wealth is as fragile as a moth's web; Jesus warns against laying up treasures on earth where moth and rust destroy (Matt 6:19), using the same moth-imagery to expose the impermanence of earthly wealth vs. the permanence of heavenly treasure"}
    ]
  },
  "28": {
    "12": [
      {"type": "allusion", "target": "1 Cor 1:24", "note": "Where shall wisdom be found? And where is the place of understanding? — the great wisdom hymn's unanswerable question after cataloguing all human discovery: silver mines, gold refining, deep shafts, mountain-moving — yet wisdom remains beyond reach; the NT's answer is the one Job 28 cannot supply: Christ the power of God and the wisdom of God (1 Cor 1:24); the wisdom Job 28 declares unlocatable and unpurchasable is located in a person"},
      {"type": "allusion", "target": "Col 2:3", "note": "Where shall wisdom be found? — Job 28 establishes that wisdom is hidden from mortal searches; Paul answers that in Christ are hidden all the treasures of wisdom and knowledge (Col 2:3); the hiddenness of wisdom that Job 28 narrates is resolved only in the incarnation: the hidden God reveals himself in Christ"}
    ],
    "23": [
      {"type": "allusion", "target": "1 Cor 2:10", "note": "God understands the way to wisdom and knows its location; for he looks to the ends of the earth and sees everything — God alone possesses wisdom because he sees what human searchers cannot; the Spirit searches all things, even the depths of God (1 Cor 2:10); the divine Spirit who comprehends God's own wisdom is the NT's answer to the divine monopoly on wisdom that Job 28:23-27 establishes"}
    ],
    "28": [
      {"type": "allusion", "target": "Matt 11:25", "note": "To mankind he said: the fear of the Lord is wisdom, and to turn from evil is understanding — after the lengthy hymn establishing wisdom's inaccessibility to human searching, the chapter's final verdict is that accessible wisdom is given by God to mankind as the fear of the LORD; Jesus's prayer thanks the Father for hiding these things from the wise and understanding and revealing them to little children (Matt 11:25): the fear/humility of the child is precisely the disposition Job 28:28 calls wisdom"}
    ]
  },
  "29": {
    "3": [
      {"type": "allusion", "target": "John 8:12", "note": "When his lamp shone on my head and by his light I walked through darkness — Job's nostalgic description of God's former favour as a light that illuminated his path through darkness; Jesus's self-declaration I am the light of the world; whoever follows me will not walk in darkness but will have the light of life (John 8:12) is the eschatological fulfilment: the personal divine lamp that shone on Job by God's favour becomes the incarnate Light who permanently overcomes darkness"}
    ],
    "14": [
      {"type": "allusion", "target": "Isa 61:10", "note": "I put on righteousness and it clothed me; my justice was like a robe and a turban — Job's description of righteousness as vestment; Isaiah 61:10 uses the same metaphor: he has clothed me with the garments of salvation, he has covered me with the robe of righteousness; the NT development: put on Christ (Rom 13:14), the breastplate of righteousness (Eph 6:14), and the fine linen of righteous deeds (Rev 19:8) — the clothing of righteousness Job celebrates is ultimately Christ's imputed righteousness"}
    ],
    "15": [
      {"type": "allusion", "target": "Matt 11:5", "note": "I was eyes for the blind and feet for the lame — Job's summary of his righteous ministry as giving sight to the blind and mobility to the lame; Jesus's answer to John the Baptist's messengers (Matt 11:4-5 / Luke 7:22) lists precisely these signs: the blind receive their sight and the lame walk; Job's righteous deeds describe the pattern of justice that the Messiah fulfils in his healing ministry, and ultimately in the new creation (Isa 35:5-6: then the eyes of the blind shall be opened, and the ears of the deaf unstopped)"}
    ],
    "25": [
      {"type": "allusion", "target": "2 Cor 1:3", "note": "I chose the course for them and sat as their head; I lived as a king among his troops, as one who comforts those who mourn — Job's description of his role as leader and comforter; Paul describes the God of all comfort, who comforts us in all our tribulation (2 Cor 1:3-4), and the task of comforting others with the comfort one has received from God; the king who comforts mourners is the type of Christ who in Isa 61:2 comes to comfort all who mourn — the same text Jesus reads in Lk 4:18 as his programmatic commission"}
    ]
  }
}

def main():
    e = load_echo('job')
    merge_echo(e, JOB_ECHOES)
    save_echo('job', e)
    total = sum(len(vv) for vv in JOB_ECHOES.values())
    print(f'Job 27-29 echoes: '
          + ', '.join(f'ch{ch}={len(JOB_ECHOES[ch])} verses'
                      for ch in sorted(JOB_ECHOES)) +
          f' ({total} total verse-entries).')

if __name__ == '__main__':
    main()
