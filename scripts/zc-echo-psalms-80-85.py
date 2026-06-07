"""
Echo data — Psalms chapters 80–85 (gap-fill: chs 81, 83, 84, 85 missing; 80, 82 already present)
Run: python3 scripts/zc-echo-psalms-80-85.py

Key connections:
- Ps 81:10: "Open your mouth wide, and I will fill it" → John 6:35 (bread of life);
  v12 "gave them over to stubborn hearts" → Rom 1:24,26,28 (judicial hardening);
  v16 honey from the rock → 1 Cor 10:4 (Christ the Rock who satisfies).
- Ps 83:18: "Let them know that you alone are the Most High" → Phil 2:9-11 (every
  knee bows and confesses Jesus as Lord, to the glory of the Father).
- Ps 84:2: "My soul longs for the courts of the living God" → John 7:37-38 (Christ
  as the answer to the longing); Rev 21:3 (God's dwelling among people fulfilled.
- Ps 84:9: "Look on the face of your anointed" → Heb 7:25 / 2 Cor 4:6 (the face
  of Christ as the locus of divine approval and glory).
- Ps 84:11: "The LORD God is a sun and shield; he bestows favor and honor" →
  John 1:17 (grace and truth came through Christ); Rev 21:23 (Lamb as lamp).
- Ps 85:10: "Steadfast love and faithfulness meet; righteousness and peace kiss" →
  Rom 3:25-26 (the cross as the meeting point of divine justice and divine love —
  God just and the justifier of those who have faith in Jesus).
- Ps 85:13: "Righteousness will march before him and prepare a path for his steps"
  → Matt 3:3 / Luke 3:4 (John the Baptist as the way-preparer for Christ's steps).
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

# INTENT: Echo data for Psalms 81, 83, 84, 85 — the bread-of-life feeding (Ps 81:10 →
#   John 6:35), the judicial "gave them over" (Ps 81:12 → Rom 1:24), the universal-
#   name confession (Ps 83:18 → Phil 2:9-11), the longing for the living God fulfilled
#   in Christ (Ps 84:2 → John 7:37), and the cross as the meeting-point of justice and
#   love (Ps 85:10 → Rom 3:25-26).
# CHANGE? If data/echoes/psalms.json structure changes, update load_echo/save_echo
#   per Z_COMMENTARY_SCRIPT_GUIDE.md.
# VERIFY: python3 -c "import json; d=json.load(open('data/echoes/psalms.json')); print([len(d.get(str(c),{})) for c in range(80,86)])" should show non-zero for all six.

PSALMS_ECHOES = {
  "81": {
    "10": [
      {
        "type": "allusion",
        "target": "John 6:35",
        "note": "I am the LORD your God, who brought you up out of the land of Egypt. Open your mouth wide, and I will fill it — 'I am the bread of life. Whoever comes to me will never go hungry, and whoever believes in me will never be thirsty' (John 6:35). Jesus presents himself as the fulfillment of Psalm 81:10's feeding promise. The God who commanded Israel to open wide for filling is now personally present as the bread from heaven who satisfies the deepest hunger. The Exodus feeding (manna) and the Psalm's promise both find their fulfillment in Christ."
      }
    ],
    "12": [
      {
        "type": "allusion",
        "target": "Rom 1:24",
        "note": "So I gave them over to their stubborn hearts, to follow their own devices — 'Therefore God gave them over in the sinful desires of their hearts to sexual impurity' (Rom 1:24; also v.26, 28 — three-fold 'gave them over'). Paul's description of divine judicial abandonment in Romans 1 uses the same pattern as Psalm 81:12: when people persistently refuse to listen, God's judgment is to withdraw restraint and let them have what they chose. The NT's doctrine of divine hardening is rooted in this Psalmic pattern of God 'giving over' the unlistening."
      }
    ],
    "16": [
      {
        "type": "allusion",
        "target": "1 Cor 10:4",
        "note": "With honey from the rock I would have satisfied you — 'they drank from the spiritual rock that accompanied them, and that rock was Christ' (1 Cor 10:4). Paul identifies the wilderness Rock as Christ; Psalm 81:16's 'honey from the rock' thus points to the sweetness and satisfaction that come from Christ himself. The satisfaction the rebellious Israel forfeited (v.11-12 — God would have fed them, but they did not listen) is the nourishment Christ provides to those who do listen and come to him."
      }
    ]
  },
  "83": {
    "4": [
      {
        "type": "allusion",
        "target": "Rev 20:8",
        "note": "Let us wipe them out as a nation; let the name of Israel be remembered no more! — 'and will go out to deceive the nations in the four corners of the earth — Gog and Magog — and to gather them for battle. In number they are like the sand on the seashore' (Rev 20:8). The conspiracy of nations to annihilate God's people (Ps 83:4) reaches its eschatological form in the final gathering of nations against God's city in Revelation. The impulse to erase God's people that animates Psalm 83 is the same spirit that drives the final rebellion of Rev 20."
      }
    ],
    "18": [
      {
        "type": "allusion",
        "target": "Phil 2:9",
        "note": "Let them know that you alone, whose name is the LORD, are the Most High over all the earth — 'therefore God exalted him to the highest place and gave him the name that is above every name, that at the name of Jesus every knee should bow, in heaven and on earth and under the earth, and every tongue acknowledge that Jesus Christ is Lord, to the glory of God the Father' (Phil 2:9-11). The universal acknowledgment of the divine name over all the earth (Ps 83:18) is fulfilled through the exaltation of Christ — the name above every name is the name that discloses the Most High to every tongue in every nation."
      }
    ]
  },
  "84": {
    "2": [
      {
        "type": "allusion",
        "target": "John 7:37",
        "note": "My soul longs, yes, faints for the courts of the LORD; my heart and my flesh cry out for the living God — 'Let anyone who is thirsty come to me and drink. Whoever believes in me, as Scripture has said, rivers of living water will flow from within them' (John 7:37-38). The intense longing for the living God (Ps 84:2) is the longing Christ invites to himself as its answer. The courts of the living God for which the Psalmist faints are accessible in Christ — he is the presence of the living God made personally approachable, the one in whom 'all the fullness of the Deity lives in bodily form' (Col 2:9)."
      }
    ],
    "9": [
      {
        "type": "allusion",
        "target": "Heb 7:25",
        "note": "Behold our shield, O God; look on the face of your anointed! — 'therefore he is able to save completely those who come to God through him, because he always lives to intercede for them' (Heb 7:25). The prayer that God look on the face of his Anointed (meshiach) is the prayer that the NT declares permanently answered: the Father forever looks on the face of the Son who intercedes for his people. 2 Cor 4:6: 'the light of the knowledge of God's glory displayed in the face of Christ' — the face of the Anointed is the display of divine glory."
      }
    ],
    "10": [
      {
        "type": "allusion",
        "target": "John 14:2",
        "note": "A single day in your courts is better than a thousand elsewhere; I would rather stand at the threshold of the house of my God than dwell comfortably in the tents of the wicked — 'my Father's house has many rooms... I am going there to prepare a place for you' (John 14:2). The Psalmist who yearns even for a doorkeeper's position in God's house receives from Christ the promise of a prepared permanent place within it. The threshold-longing of Psalm 84:10 is answered in the room Christ prepares — access is not merely a glimpse at the door but a full dwelling with the Father."
      }
    ],
    "11": [
      {
        "type": "allusion",
        "target": "John 1:17",
        "note": "The LORD God is a sun and shield; the LORD bestows favor and honor. No good thing does he withhold from those who walk with integrity — 'for the law was given through Moses; grace and truth came through Jesus Christ' (John 1:17). The favor (grace) and honor the LORD bestows as sun-and-shield (Ps 84:11) is the grace and truth John declares came through Christ. The good things the LORD withholds from none who walk with integrity are the blessings that Christ supplies — the fullness 'from which we have all received grace upon grace' (John 1:16)."
      }
    ]
  },
  "85": {
    "10": [
      {
        "type": "fulfillment",
        "target": "Rom 3:25",
        "note": "Steadfast love and faithfulness meet; righteousness and peace kiss — 'God presented Christ as a sacrifice of atonement... he did this to demonstrate his righteousness... so as to be just and the one who justifies those who have faith in Jesus' (Rom 3:25-26). Psalm 85:10 is the OT anticipation of the cross: the meeting point where divine love (hesed) and divine justice (righteousness) embrace rather than oppose each other. The atonement is God's solution to the apparent contradiction between his love for sinners and his justice against sin — at the cross, righteousness and peace kiss."
      }
    ],
    "11": [
      {
        "type": "allusion",
        "target": "John 1:14",
        "note": "Faithfulness springs up from the earth, and righteousness looks down from heaven — 'the Word became flesh and dwelt among us, and we have seen his glory, glory as of the only Son from the Father, full of grace and truth' (John 1:14). The two movements of Psalm 85:11 — righteousness descending from heaven, faithfulness rising from earth — describe the two natures of the incarnation: the divine righteousness/glory that comes down and the human faithfulness/truth that is assumed and perfected. Christ is the meeting point of the heavenly and the earthly that the Psalm describes."
      }
    ],
    "13": [
      {
        "type": "fulfillment",
        "target": "Matt 3:3",
        "note": "Righteousness will march before him and prepare a path for his steps — 'this is he who was spoken of through the prophet Isaiah: \"A voice of one calling in the wilderness, 'Prepare the way for the Lord, make straight paths for him'\"' (Matt 3:3). The one who prepares the path for the LORD's approaching steps (Ps 85:13) is fulfilled in John the Baptist, who prepares the way for Christ. The Psalm describes righteousness marching ahead as forerunner; Matthew presents John the Baptist as that forerunner whose ministry opens the path for the Messiah's arrival."
      }
    ]
  }
}

def main():
    existing = load_echo('psalms')
    merge_echo(existing, PSALMS_ECHOES)
    save_echo('psalms', existing)
    for ch in ['80', '81', '82', '83', '84', '85']:
        entries = len(existing.get(ch, {}))
        print(f"  ch{ch}: {entries} verses with entries")
    print("Psalms 80–85 echoes complete.")

if __name__ == '__main__':
    main()
