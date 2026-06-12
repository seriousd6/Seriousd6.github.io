"""
Echo layer — Job chapters 36–38
Run: python3 scripts/zc-echo-job-36-38.py

Ch 36: Elihu's final address — God's pedagogy through affliction; God teaches by
       suffering (v10,15), and is the incomparable instructor (v22); the rain-and-
       cloud theophany prepares for the whirlwind speech.
Ch 37: Elihu's doxology of divine weather — thunder, lightning, frost, wind, the
       splendour of the north — all establish that no human can comprehend or advise
       God; the chapter closes as a transition into the divine speech.
Ch 38: God's first answer from the whirlwind — the great cosmological catechism:
       creation foundations, sea-boundaries, dawn, death-gates, storehouses of snow
       and hail, Pleiades and Orion, rain-sources, wisdom placed within — each
       unanswerable question exposes Job's creature-finitude against Creator-infinity.
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
  "36": {
    "10": [
      {"type": "allusion", "target": "Heb 5:8", "note": "He opens their ears to instruction and commands that they return from iniquity — Elihu's insight that God uses adversity as a disciplinary channel to open otherwise-closed ears; Hebrews makes the same claim about the Son himself: though he were a Son, yet learned he obedience by the things which he suffered (Heb 5:8); the divine pedagogy Elihu describes reaches its sharpest exemplar in Christ's own suffering-shaped obedience, where the one who needed no correction nonetheless walked the path of affliction-as-instruction on our behalf"},
      {"type": "allusion", "target": "Isa 50:4-5", "note": "He opens their ears to instruction — the same idiom governs the Servant Song: the Lord GOD has opened my ear, and I was not rebellious (Isa 50:5); the Servant whose ear God opens to receive instruction is the same figure whose mouth is given the tongue of the learned to speak a word in season to the weary; the ear-opening Elihu describes in general anthropological terms becomes in Isaiah the vocation of the Suffering Servant"}
    ],
    "15": [
      {"type": "allusion", "target": "Isa 53:4", "note": "He delivers the afflicted by their affliction and opens their ear by adversity — the paradoxical claim that God delivers by means of affliction itself, not around it; this becomes the precise logic of Isa 53:4-5: surely he has borne our griefs and carried our sorrows; he was wounded for our transgressions; deliverance comes through the Servant's affliction taken into himself; Elihu glimpsed the mechanism without knowing the Person"}
    ],
    "22": [
      {"type": "allusion", "target": "Matt 7:28-29", "note": "Behold, God is exalted in his power; who is a teacher like him? — Elihu's rhetorical claim that no teacher compares with God; the crowds echo this after the Sermon on the Mount: he taught them as one who had authority, and not as their scribes (Matt 7:28-29); the incomparability of God's teaching that Elihu argues philosophically is embodied in Jesus, who teaches with the authority of the one about whom Elihu asks — the divine Teacher made flesh"}
    ],
    "26": [
      {"type": "allusion", "target": "1 Tim 6:16", "note": "Behold, God is great, and we know him not; the number of his years is unsearchable — Elihu's acknowledgment of the epistemic boundary between creature and Creator; Paul's doxology names the same boundary: who alone has immortality, dwelling in unapproachable light, whom no one has ever seen or can see (1 Tim 6:16); this unsearchable, unapproachable God is the one who in the incarnation became searchable and approachable — crossing the boundary Elihu declares uncrossable"}
    ]
  },
  "37": {
    "5": [
      {"type": "allusion", "target": "Rev 19:6", "note": "God thunders wondrously with his voice; he does great things that we cannot comprehend — Elihu's doxology of the divine thundervoice as emblem of incomprehensible greatness; Revelation's climactic Alleluia chorus hears the same sound: as the voice of mighty thunderings, saying Alleluia: for the Lord God omnipotent reigneth (Rev 19:6); the storm-voice Elihu celebrates becomes in Revelation the anthem of final victory, the same divine power applied to eschatological sovereignty over all creation and history"}
    ],
    "14": [
      {"type": "allusion", "target": "John 5:36", "note": "Stop and consider the wondrous works of God — Elihu's call to attentive contemplation of God's deeds in nature; Jesus redirects the same charge toward his own works: the works that the Father has given me to accomplish, the very works that I am doing, bear witness about me that the Father has sent me (John 5:36); the invitation to behold God's wondrous works reaches its sharpest focus in the incarnate Son whose healings and signs are themselves the divine works Elihu commands Job to stop and behold"}
    ],
    "22": [
      {"type": "allusion", "target": "Rev 21:11", "note": "Out of the north comes golden splendour; God is clothed with awesome majesty — the theophanic glory of the approaching storm as a window on divine majesty; Revelation's vision of the new Jerusalem coming down from God out of heaven describes the city's light as like a most rare jewel, like a jasper stone, clear as crystal (Rev 21:11); the golden-splendour language Elihu reaches for to describe the divine approach finds its eschatological form in the jewelled radiance of the city whose light is the glory of God and its lamp is the Lamb (Rev 21:23)"}
    ],
    "23": [
      {"type": "allusion", "target": "Rom 11:33", "note": "The Almighty — we cannot find him out; he is great in power; justice and abundant righteousness he will not violate — Elihu's crescendo: the divine combination of incomprehensibility and unyielding justice; Paul's doxology captures the same double: O the depth of the riches both of the wisdom and knowledge of God! how unsearchable are his judgments, and his ways past finding out! (Rom 11:33); the God whom Elihu declares unfindable has not abandoned justice but exceeded it — a mystery Paul has just finished narrating in the history of Israel and the ingrafting of the Gentiles"}
    ]
  },
  "38": {
    "7": [
      {"type": "allusion", "target": "Col 1:16", "note": "When the morning stars sang together, and all the sons of God shouted for joy — the angelic assembly's worship at the laying of creation's foundation; Colossians 1:16 identifies the agent of that founding: by him were all things created, that are in heaven, and that are in earth, visible and invisible, whether they be thrones or dominions or principalities or powers; the 'sons of God' whose joy accompanies creation's birth are themselves created through and for the same preexistent Christ who is the foundation they celebrated"},
      {"type": "allusion", "target": "Rev 5:11-12", "note": "All the sons of God shouted for joy — the angelic multitude's song at creation's founding echoes the innumerable angelic host of Rev 5:11-12 who cry Worthy is the Lamb who was slain, to receive power and wealth and wisdom and might and honour and glory and blessing; the creation-shout of joy and the redemption-shout of worship are the bookend songs of the same angelic chorus, honouring the same Lord at the beginning and the consummation of all things"}
    ],
    "31": [
      {"type": "allusion", "target": "Rev 1:16", "note": "Can you bind the chains of the Pleiades or loose the belt of Orion? — God's ironic catechism on astronomical governance; in Revelation's vision of the risen Christ, he had in his right hand seven stars (Rev 1:16), and he identifies himself as he who holds the seven stars (Rev 2:1); the question God directs at Job — can you govern the star-clusters? — has its NT answer in the one who holds all stars in his right hand: the cosmic authority that silences Job is claimed by the risen Lord as his own possession"}
    ],
    "36": [
      {"type": "allusion", "target": "Jer 31:33", "note": "Who has put wisdom in the inward parts, or given understanding to the mind? — the rhetorical question assumes that only God can place wisdom within a creature; Jeremiah's new covenant promise answers how this will be done universally: I will put my law in their inward parts and write it on their hearts (Jer 31:33); the inward-placement of wisdom God claims as his prerogative becomes the new covenant's central promise, mediated by the Spirit of Christ (2 Cor 3:3)"},
      {"type": "allusion", "target": "1 Cor 2:10", "note": "Who has put wisdom in the inward parts? — the divine monopoly on inner wisdom that God asserts here is given to believers through the Spirit: for the Spirit searches everything, even the depths of God (1 Cor 2:10); what no creature can access by searching (Job 28:12-13) and no creature can self-install (Job 38:36) is granted as gift — the Spirit as the divine answer to the divine question"}
    ]
  }
}

def main():
    e = load_echo('job')
    merge_echo(e, JOB_ECHOES)
    save_echo('job', e)
    total = sum(len(vv) for vv in JOB_ECHOES.values())
    print(f'Job 36-38 echoes: '
          + ', '.join(f'ch{ch}={len(JOB_ECHOES[ch])} verses'
                      for ch in sorted(JOB_ECHOES)) +
          f' ({total} total verse-entries).')

if __name__ == '__main__':
    main()
