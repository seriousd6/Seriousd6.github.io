"""
Echo data — Psalms chapters 41–47 (gap-fill: chs 42, 43, 46, 47 missing; 41, 44, 45 already present)
Run: python3 scripts/zc-echo-psalms-41-47.py

Key connections:
- Ps 42:1-2: The soul's longing for the living God → John 7:37-38 / Rev 22:17
  (Christ as the living water that answers the longing).
- Ps 42:3,10: "Where is your God?" taunt → Matt 27:43 (cross mockery).
- Ps 43:3: "Send out your light and your truth" → John 1:9 / John 14:6
  (Christ as the light and truth that leads to the Father's holy mountain).
- Ps 46:4: "River whose streams bring joy to the city of God" → Rev 22:1-2
  (river of life from the throne of the Lamb).
- Ps 46:7,11: "The LORD of hosts is with us" Immanuel refrain → Matt 1:23
  (Christ as Immanuel = God with us).
- Ps 47:5: "God has ascended with shouts of joy" → Acts 1:9-11 (Ascension);
  Eph 4:8 (ascension gifts).
- Ps 47:8-9: "The nobles of the nations have gathered as the people of the God
  of Abraham" → Gal 3:8 / Rev 21:24-26 (nations streaming to the Lamb's city).
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

# INTENT: Echo data for Psalms 42, 43, 46, 47 — the deer-longing answered by
#   Christ the living water (Ps 42), light-and-truth leading to the holy mountain
#   (Ps 43), the Immanuel refrain and the eschatological river (Ps 46), and the
#   divine Ascension and universal kingship (Ps 47).
# CHANGE? If data/echoes/psalms.json structure changes, update load_echo/save_echo
#   per Z_COMMENTARY_SCRIPT_GUIDE.md.
# VERIFY: python3 -c "import json; d=json.load(open('data/echoes/psalms.json')); print([len(d.get(str(c),{})) for c in range(41,48)])" should show non-zero for all.

PSALMS_ECHOES = {
  "42": {
    "1": [
      {
        "type": "allusion",
        "target": "John 7:37",
        "note": "As a deer longs for flowing streams, so my soul longs for you, O God — Jesus' cry on the last day of the Feast: 'Let anyone who is thirsty come to me and drink. Whoever believes in me, as Scripture has said, rivers of living water will flow from within them' (John 7:37-38). The deer's longing (Ps 42:1) is the image of every soul's spiritual thirst; Christ presents himself as its answer. The longing of the Psalm becomes the invitation of the gospel."
      },
      {
        "type": "allusion",
        "target": "Rev 22:17",
        "note": "As a deer longs for flowing streams — 'the Spirit and the bride say, \"Come!\" And let the one who hears say, \"Come!\" Let the one who is thirsty come; and let the one who wishes take the free gift of the water of life' (Rev 22:17). The eschatological form of the Psalm's longing is the final invitation of Scripture — the thirsting soul welcomed to the water of life."
      }
    ],
    "2": [
      {
        "type": "fulfillment",
        "target": "John 4:14",
        "note": "My soul thirsts for God, for the living God — 'whoever drinks the water I give them will never thirst. Indeed, the water I give them will become in them a spring of water welling up to eternal life' (John 4:14). Jesus presents himself to the Samaritan woman as the answer to Psalm 42's thirst — the one who gives water that permanently quenches the longing the Psalm expresses. The 'living God' for whom the Psalmist thirsts is the God who sends the living water in his Son."
      }
    ],
    "3": [
      {
        "type": "allusion",
        "target": "Matt 27:43",
        "note": "While people keep saying to me all day long, 'Where is your God?' — 'He trusts in God. Let God rescue him now if he wants him, for he said, \"I am the Son of God\"' (Matt 27:43). The mockery at the cross takes the form of Psalm 42:3's taunt — 'where is your God?' — redirected at Jesus hanging on the cross. The one who cries 'My God, my God, why have you forsaken me?' (Ps 22:1) also bears the 'Where is your God?' mockery the Psalmist knew."
      }
    ],
    "7": [
      {
        "type": "allusion",
        "target": "Matt 26:38",
        "note": "Deep calls to deep at the roar of your waterfalls; all your waves and breakers have rolled over me — 'My soul is overwhelmed with sorrow to the point of death' (Matt 26:38, Gethsemane). The Psalmist's experience of being overwhelmed by wave after wave — the deep chaos rolling over the soul — is the language Jesus uses of his Gethsemane anguish. Christ enters the 'deep calls to deep' experience of Psalm 42:7 in its fullest form as he approaches the cross."
      }
    ],
    "5": [
      {
        "type": "allusion",
        "target": "John 20:28",
        "note": "Put your hope in God, for I will yet praise him — my Savior and my God — Thomas's post-resurrection confession: 'my Lord and my God!' (John 20:28) is the Psalm's 'my God' finally spoken in the presence of the risen Christ. The Psalm's refrain — 'I will yet praise him, my Savior and my God' — expresses the faith that persists through darkness expecting vindication; Thomas's confession is that vindication arriving."
      }
    ]
  },
  "43": {
    "1": [
      {
        "type": "allusion",
        "target": "Luke 23:14",
        "note": "Vindicate me, O God, and plead my cause against an ungodly nation; from the deceitful and unjust man deliver me — Christ stands before Pilate (Luke 23:14: 'I have examined him in your presence and have found no basis for your charges against him'), the prayer of Psalm 43:1 becoming the situation of the trial. The righteous man seeking vindication against an ungodly nation and unjust man is the type Christ embodies before Pilate; his vindication comes not through the trial but through the resurrection."
      }
    ],
    "3": [
      {
        "type": "fulfillment",
        "target": "John 1:9",
        "note": "Send out your light and your truth; let them lead me to your holy mountain — 'the true light that gives light to everyone was coming into the world' (John 1:9). The Psalmist's prayer for divine light and truth to guide him to God's mountain is answered in the incarnation of the one who is 'the way, the truth, and the life' (John 14:6). Christ is the light and truth that God sends out in response to the Psalm's prayer."
      },
      {
        "type": "allusion",
        "target": "Rev 21:23",
        "note": "Let them bring me to your holy mountain and to your dwelling place — 'the city does not need the sun or the moon to shine on it, for the glory of God gives it light, and the Lamb is its lamp' (Rev 21:23). The holy mountain and dwelling place that the Psalmist longs to reach is the eschatological city whose light is the Lamb. The prayer to be brought to God's dwelling place is fulfilled in the new Jerusalem where God dwells with his people forever (Rev 21:3)."
      }
    ],
    "4": [
      {
        "type": "allusion",
        "target": "Heb 10:19",
        "note": "Then I will approach the altar of God, to God who is my greatest joy — 'we have confidence to enter the Most Holy Place by the blood of Jesus, by a new and living way opened for us through the curtain, that is, his body' (Heb 10:19-20). The Psalmist's longing to approach the altar of God is fulfilled through Christ who opens the way into the divine presence. The approach to God that Psalm 43:4 anticipates is the access that Christ's sacrifice makes permanently available."
      }
    ]
  },
  "46": {
    "1": [
      {
        "type": "allusion",
        "target": "Matt 28:20",
        "note": "God is our refuge and strength, a help that is always present in times of trouble — 'I am with you always, to the very end of the age' (Matt 28:20). The 'always present' (Hebrew: nimtsa meod) help of Psalm 46:1 is the eternal presence that Christ promises at the Great Commission. The Immanuel God of Psalm 46 is the risen Christ who promises his permanent presence with his people through all times of trouble."
      }
    ],
    "4": [
      {
        "type": "fulfillment",
        "target": "Rev 22:1",
        "note": "There is a river whose streams bring joy to the city of God — 'then the angel showed me the river of the water of life, as clear as crystal, flowing from the throne of God and of the Lamb, down the middle of the great street of the city' (Rev 22:1-2). The river that brings joy to the city of God in Psalm 46:4 is the river of life flowing from the Lamb's throne in Revelation. The eschatological city's joy-river is the fulfillment of the Psalm's image — the living water that Christ gives (John 7:38) flowing permanently in the new Jerusalem."
      }
    ],
    "5": [
      {
        "type": "allusion",
        "target": "John 14:17",
        "note": "God is within her; she will not be shaken — 'the Spirit of truth... lives with you and will be in you' (John 14:17). The presence of God within the city (Ps 46:5) is the type of the Spirit's indwelling presence in the church. 1 Cor 3:16: 'don't you know that you yourselves are God's temple and that God's Spirit lives among you?' The city that cannot be shaken because God dwells within is the church that cannot be destroyed because the Spirit indwells it."
      }
    ],
    "7": [
      {
        "type": "fulfillment",
        "target": "Matt 1:23",
        "note": "The LORD of hosts is with us; the God of Jacob is our fortress (Selah) — 'The virgin will conceive and give birth to a son, and they will call him Immanuel (which means \"God with us\")' (Matt 1:23). The Psalm's refrain 'the LORD of hosts is with us' is the definition of Immanuel — 'God with us.' The Psalm declares what the incarnation enacts: the God who is with his people is no longer a covenantal promise alone but a personal presence in Christ."
      }
    ],
    "10": [
      {
        "type": "allusion",
        "target": "Phil 2:9",
        "note": "Be still, and know that I am God; I will be exalted among the nations, I will be exalted throughout the earth — 'therefore God exalted him to the highest place and gave him the name that is above every name, that at the name of Jesus every knee should bow, in heaven and on earth and under the earth' (Phil 2:9-10). The divine self-exaltation among the nations (Ps 46:10) is fulfilled in the exaltation of the risen Christ — the name above every name that every nation will acknowledge."
      }
    ]
  },
  "47": {
    "1": [
      {
        "type": "allusion",
        "target": "Phil 4:4",
        "note": "Clap your hands, all you peoples; shout to God with a voice of joy — 'Rejoice in the Lord always. I will say it again: Rejoice!' (Phil 4:4). The universal joyful acclaim of Psalm 47:1 is the posture Paul commands of the church and that Rev 19:1-7 depicts in the heavenly multitude: 'Hallelujah! For our Lord God Almighty reigns.' The clapping and shouting of all peoples in the Psalm anticipates the eschatological hallelujah chorus."
      }
    ],
    "2": [
      {
        "type": "allusion",
        "target": "Rev 19:16",
        "note": "The LORD Most High is to be feared; he is a great King over the whole earth — 'on his robe and on his thigh he has this name written: KING OF KINGS AND LORD OF LORDS' (Rev 19:16). The great King over the whole earth (Ps 47:2) is the risen Christ who returns as King of kings. Matt 28:18: 'all authority in heaven and on earth has been given to me' — the universal kingship of Psalm 47:2 is invested in Christ at the resurrection."
      }
    ],
    "5": [
      {
        "type": "fulfillment",
        "target": "Acts 1:9",
        "note": "God has ascended with shouts of joy, the LORD with the sound of a ram's horn — 'after he said this, he was taken up before their very eyes, and a cloud hid him from their sight' (Acts 1:9). Psalm 47:5 is the OT anticipation of the Ascension — God ascending amid acclaim and trumpet sound. Eph 4:8 (citing Ps 68:18) and Acts 1:9-11 together present the Ascension as the fulfillment of the Psalms' divine-ascent theme. The shofar-blast acclamation of the ascending God is the type of the Ascension with its angelic announcement."
      }
    ],
    "8": [
      {
        "type": "allusion",
        "target": "Rev 11:15",
        "note": "God reigns over the nations; God is seated on his holy throne — 'the kingdom of the world has become the kingdom of our Lord and of his Messiah, and he will reign for ever and ever' (Rev 11:15). The divine reign over the nations that Psalm 47:8 declares is the reign that the seventh trumpet proclaims as fully enacted in Christ. The throne of Psalm 47:8 is the throne that Rev 4-5 reveals with the Lamb sharing the divine reign."
      }
    ],
    "9": [
      {
        "type": "fulfillment",
        "target": "Gal 3:8",
        "note": "The nobles of the nations have gathered as the people of the God of Abraham — 'Scripture foresaw that God would justify the Gentiles by faith, and announced the gospel in advance to Abraham: \"All nations will be blessed through you\"' (Gal 3:8). The gathering of the Gentile nobles as the people of Abraham's God (Ps 47:9) is the fulfillment Paul identifies in Christ: the blessing of Abraham comes to the Gentiles through faith in Christ (Gal 3:14). Rev 21:24: 'the nations will walk by its light, and the kings of the earth will bring their splendor into it.'"
      }
    ]
  }
}

def main():
    existing = load_echo('psalms')
    merge_echo(existing, PSALMS_ECHOES)
    save_echo('psalms', existing)
    for ch in ['41','42','43','44','45','46','47']:
        entries = len(existing.get(ch, {}))
        print(f"  ch{ch}: {entries} verses with entries")
    print("Psalms 41–47 echoes complete.")

if __name__ == '__main__':
    main()
