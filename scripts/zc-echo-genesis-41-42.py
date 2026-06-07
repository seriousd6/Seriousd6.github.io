"""
Echo Layer — Genesis chapters 41–42
Run: python3 scripts/zc-echo-genesis-41-42.py

Key echo trajectories:
- Gen 41:14: Joseph drawn from prison/pit → Acts 2:24 (resurrection from death's hold)
- Gen 41:16: 'not in me; God will answer' → John 5:19, 30 (Son does nothing on his own)
- Gen 41:38: Spirit of God in Joseph → Isa 11:2; Luke 4:18 (Messiah's Spirit-anointing)
- Gen 41:40-44: full royal exaltation (signet, chariot, 'bow the knee') → Phil 2:9-11;
  Matt 28:18; Eph 1:20-22
- Gen 41:45: Gentile bride Asenath → Eph 2:11-13 (Gentiles brought near); church from nations
- Gen 41:55: 'Go to Joseph' → John 6:35 (bread of life); John 14:6
- Gen 41:57: all earth came to Joseph for grain → universal scope of Christ's provision
- Gen 42:6: brothers bow before unrecognized Joseph → Luke 24:16; John 20:14 (risen Christ
  unrecognized); Ps 22:27-29 (all nations bow)
- Gen 42:21-22: brothers acknowledge guilt → Luke 15:17-20 (prodigal's return)
- Gen 42:24: Joseph weeps → John 11:35; compassion of the exalted one for those who wronged him
- Existing echo v39 [fulfillment] Phil 2:9-11 preserved by merge_echo.
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
    """Merge echo entries; deduplicate by (type, target) within each verse."""
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

GENESIS_ECHOES = {
  "41": {
    "14": [
      {"type": "type", "target": "Acts 2:24", "note": "Joseph is brought out of the prison/dungeon (<em>bôr</em>, the pit) and brought before Pharaoh (41:14) — the movement from death-place to royal presence is the exaltation arc in miniature. Acts 2:24 names the same movement for Christ: 'God raised him up, loosing the pangs of death, because it was not possible for him to be held by it.' Joseph's emergence from the pit/prison is the type; Christ's resurrection from the tomb is the antitype — both are the vindication of the falsely condemned beloved son."}
    ],
    "16": [
      {"type": "shadow", "target": "John 5:19", "note": "'It is not in me; God will give Pharaoh a favorable answer' (41:16) — Joseph refuses to take credit for the interpretation he is about to give. This consistent self-effacement in favor of the one who sent him is the pattern Jesus articulates in John 5:19: 'the Son can do nothing of his own accord, but only what he sees the Father doing' and 5:30: 'I can do nothing on my own... I seek not my own will but the will of him who sent me.' The true representative of God claims nothing for himself."}
    ],
    "38": [
      {"type": "shadow", "target": "Isa 11:2", "note": "'Can we find a man like this, in whom is the Spirit of God?' (41:38) — Pharaoh's question marks Joseph as uniquely Spirit-endowed for a crisis-governance role. Isa 11:2 describes the Messiah: 'the Spirit of the LORD shall rest upon him, the Spirit of wisdom and understanding, the Spirit of counsel and might.' Luke 4:18 opens Jesus's ministry with the same pneumatic claim ('The Spirit of the Lord is upon me'). Joseph is the type; the Spirit-anointed servant-king is the archetype Isaiah prophesies and Jesus fulfills."}
    ],
    "40": [
      {"type": "shadow", "target": "Matt 28:18", "note": "'You shall be over my house, and all my people shall order themselves as you command' (41:40) — Pharaoh's delegation to Joseph gives him universal executive authority in Egypt. Jesus's Great Commission claim — 'all authority in heaven and on earth has been given to me' (Matt 28:18) — is the cosmic scale of the same pattern: the exalted son given all authority by the one above him. Eph 1:20-22 makes the Christological application explicit: 'seated at his right hand in the heavenly places, far above all rule and authority... he put all things under his feet.'"}
    ],
    "43": [
      {"type": "shadow", "target": "Phil 2:10", "note": "Pharaoh's herald cries 'Bow the knee!' (<em>ʾabrēk</em>) before Joseph's chariot (41:43) — a formal proclamation requiring public submission before the exalted ruler. Phil 2:10-11 quotes Isa 45:23 and applies it to the exalted Christ: 'at the name of Jesus every knee should bow, in heaven and on earth and under the earth, and every tongue confess that Jesus Christ is Lord.' Pharaoh's herald anticipates the cosmic herald who will announce the universal submission to the Lamb."}
    ],
    "45": [
      {"type": "shadow", "target": "Eph 2:13", "note": "Joseph, the Hebrew slave elevated to viceroy, is given a Gentile wife, Asenath daughter of the priest of On (41:45) — a Gentile bride for the covenant son who has become savior. Paul's description of the church in Eph 2:11-13 uses the same spatial movement: Gentiles 'once far off have been brought near by the blood of Christ.' The Gentile bride of the exalted Joseph types the church drawn from the nations as Christ's bride (Rev 5:9: 'you ransomed people for God from every tribe and language and people and nation')."}
    ],
    "55": [
      {"type": "shadow", "target": "John 6:35", "note": "When Egypt hungers, Pharaoh's answer is 'Go to Joseph; what he says to you, do' (41:55) — the universal famine-solution is a single person to whom all are directed. John 6:35 records Jesus's self-identification as the universal answer to the hunger the famine represents: 'I am the bread of life; whoever comes to me shall not hunger, and whoever believes in me shall never thirst.' Pharaoh's 'Go to Joseph' is the type of the Father's direction to the Son as the only source of life for the starving world."}
    ],
    "57": [
      {"type": "shadow", "target": "John 12:32", "note": "'All the earth came to Egypt to Joseph to buy grain, because the famine was severe over all the earth' (41:57) — universal scope: the provision is sufficient for all who come. Jesus promises the same universality: 'I, when I am lifted up from the earth, will draw all people to myself' (John 12:32). The cross-as-exaltation parallels Joseph's elevation: the one lifted up in apparent shame becomes the universal draw, the source of life for all who come."}
    ]
  },
  "42": {
    "6": [
      {"type": "shadow", "target": "Luke 24:16", "note": "Joseph's brothers 'bowed themselves before him with their faces to the ground' (42:6) — fulfilling the dream of 37:5-9 — but 'Joseph recognized his brothers, though they did not recognize him' (42:8). The risen Christ is similarly recognized and unrecognized: on the Emmaus road, 'their eyes were kept from recognizing him' (Luke 24:16); Mary mistakes him for the gardener (John 20:14-15); the disciples on the shore don't recognize him (John 21:4). The pattern: the exalted/risen one recognizes those who approach him before they recognize him."},
      {"type": "shadow", "target": "Ps 22:27", "note": "The brothers bowing with faces to the ground before the one they rejected (42:6) enacts Ps 22:27-29: 'all the ends of the earth shall remember and turn to the LORD, and all the families of the nations shall worship before you... all who go down to the dust shall bow before him.' The nations streaming to the exalted Joseph (41:57) and his own brothers prostrating themselves is the type of the universal worship of the one who was despised and rejected."}
    ],
    "7": [
      {"type": "shadow", "target": "John 1:11", "note": "Joseph spoke harshly to them and treated them as strangers (42:7) — testing the brothers who do not recognize him. The dynamic of the one who 'came to his own, and his own people did not receive him' (John 1:11) is the Joseph narrative's central tension: the rejected one returns as savior but is not recognized by the very people who rejected him. The delayed recognition is both a testing and a preparation for the tearful restoration that follows (Gen 45)."}
    ],
    "21": [
      {"type": "shadow", "target": "Luke 15:17", "note": "In their distress the brothers say to one another: 'In truth we are guilty concerning our brother... that is why this distress has come upon us' (42:21) — the moment of acknowledged guilt under pressure. Luke 15:17 describes the prodigal's analogous moment: 'when he came to himself, he said, How many of my father's hired servants have more than enough bread... I will arise and go to my father and say to him, Father, I have sinned.' In both cases, the crisis that forces the acknowledgment of guilt is the doorway to reconciliation."}
    ],
    "24": [
      {"type": "shadow", "target": "John 11:35", "note": "Joseph turned away from them and wept (42:24) — the exalted ruler weeping privately for the brothers who wronged him. This is the first of Joseph's several weeping episodes (43:30; 45:2, 14-15; 46:29; 50:1, 17). The tears of the exalted one for those who sinned against him is the Joseph type that Jesus enacts at Lazarus's tomb: 'Jesus wept' (John 11:35) — the sovereign Lord who is himself the resurrection and the life weeps with those he is about to comfort. Compassion without resentment is the character of the savior."}
    ],
    "38": [
      {"type": "shadow", "target": "John 3:16", "note": "Jacob refuses to send Benjamin: 'his brother is dead, and he is the only one left. If harm should happen to him on the journey that you are to make, you would bring down my gray hairs with sorrow to Sheol' (42:38) — the anguish of a father at the prospect of losing his only remaining beloved son. The type for John 3:16: 'For God so loved the world, that he gave his only Son' — the Father who spared not his beloved Son (Rom 8:32: 'he who did not spare his own Son') does what Jacob refuses, surrendering the beloved to secure the salvation of many."}
    ]
  }
}

def main():
    existing = load_echo('genesis')
    merge_echo(existing, GENESIS_ECHOES)
    save_echo('genesis', existing)

    result = load_echo('genesis')
    for ch in [41, 42]:
        n = len(result.get(str(ch), {}))
        print(f'  Ch {ch}: {n} verses with echoes')
    total = len(result)
    print(f'  Genesis total: {total} chapters with echo data')
    print('Genesis 41-42 echoes written.')

if __name__ == '__main__':
    main()
