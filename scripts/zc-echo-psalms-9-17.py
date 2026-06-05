"""
Echo layer — Psalms 9–17 (OT → NT forward direction)
Run: python3 scripts/zc-echo-psalms-9-17.py
Output: data/echoes/psalms.json (adds Ps 9-17)

For OT books, echoes trace how each psalm is taken up in the NT:
where it is quoted, alluded to, or developed theologically.

Psalms in this range with significant NT usage:
- Psalm 10: v.7 quoted in Romans 3:14 (catena on universal sinfulness)
- Psalm 14: vv.1-3 quoted in Romans 3:10-12 (no one does good)
- Psalm 16: vv.8-11 quoted in Acts 2:25-28 (Peter's resurrection proof-text);
  v.10 quoted in Acts 13:35 (Paul's sermon at Pisidian Antioch)
- Psalm 17: v.15 alluded to in 1 John 3:2 / Rev 22:4 (seeing God face to face)

Parallels file absorbed:
- 10:7: quotation-source → Romans 3:14 → quote
- 14:1: quotation-source → Romans 3:10-12 → quote; parallel → Psalm 53:1-6 → theme
- 16:10: fulfillment → Acts 2:27-28 and Acts 13:35 → fulfillment confirmed

Key classification decisions:
- Ps 16:10 classified as "fulfillment" because Peter and Paul explicitly argue
  the psalm's Holy One cannot refer to David who died and decayed; only the
  resurrection of Jesus satisfies the text
- Ps 14:1-3 classified as "fulfillment" — Paul's argument in Rom 3 is that these
  verses sum up the condition of all humanity apart from the gospel
- Ps 15:1 classified as "type" — the entrance requirements of the holy mountain
  anticipate the new covenant community's access to God through Christ
- Ps 17:15 classified as "allusion" — the seeing-God's-face hope is picked up in
  1 John 3:2 and Rev 22:4 without direct citation
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

PSALMS_ECHOES = {
  "9": {
    "8": [
      {"type": "fulfillment", "target": "Acts 17:31", "note": "The LORD will judge the world with righteousness and the peoples with equity — Paul at Athens declares that God has set a day when he will judge the world in righteousness through a man he appointed, proving it by raising him from the dead. The psalm's vision of YHWH as the universal righteous judge is fulfilled in the appointment of Christ as the eschatological judge."},
      {"type": "allusion", "target": "Rev 19:11", "note": "He who sat on the white horse is called Faithful and True; with justice he judges and wages war — John's rider on the white horse, who judges in righteousness, instantiates the Psalm 9 vision of the divine judge. The psalm's royal judge-figure reaches its culmination in the parousia of Christ."}
    ],
    "14": [
      {"type": "allusion", "target": "Heb 13:15", "note": "Through Jesus, therefore, let us continually offer to God a sacrifice of praise — the fruit of lips that openly profess his name — echoes the psalmist's declaration of praise in the gates of Daughter Zion; the NT reframes communal praise as the continual sacrifice that replaces the temple's territorial worship."}
    ]
  },
  "10": {
    "4": [
      {"type": "fulfillment", "target": "Rom 3:11", "note": "The wicked person, in his arrogance, does not seek God — Paul's catena in Romans 3 includes the paraphrase 'there is no one who seeks God'; the stance of practical atheism that Psalm 10 anatomizes in the arrogant wicked person is generalized by Paul to characterize the human condition apart from grace."}
    ],
    "7": [
      {"type": "quote", "target": "Rom 3:14", "note": "Paul quotes Psalm 10:7 verbatim in his Romans 3 catena: 'Their mouths are full of curses and bitterness.' The psalm's portrait of the wicked person whose speech is weaponized with oaths and lies becomes one of the proof-texts Paul assembles to demonstrate that the indictment 'there is no one who does good' applies universally to humanity apart from God's righteousness."}
    ],
    "16": [
      {"type": "allusion", "target": "Rev 11:15", "note": "The LORD is King for ever and ever — the seventh trumpet's proclamation that the kingdom of the world has become the kingdom of our Lord and of his Messiah echoes the Psalm's declaration of YHWH's eternal kingship. The psalm's vision of divine kingship over the nations is the OT root of the Revelation's eschatological kingdom-announcement."}
    ]
  },
  "11": {
    "4": [
      {"type": "allusion", "target": "Rev 4:2", "note": "The LORD is in his holy temple; the LORD is on his heavenly throne — John's throne-room vision in Revelation 4 opens with the same heavenly sanctuary and enthroned deity. The psalm's assertion of the divine throne as the vantage point of cosmic governance underlies the Revelation's vision of the heavenly court from which the scroll with seven seals is dispensed."},
      {"type": "allusion", "target": "Heb 4:16", "note": "Let us approach the throne of grace with confidence — the writer grounds the invitation in the heavenly sanctuary where the enthroned God reigns (cf. Ps 11:4); the psalm's vision of the divine court provides the OT backdrop for the NT's call to confident approach to the heavenly throne."}
    ]
  },
  "12": {
    "6": [
      {"type": "allusion", "target": "2 Tim 3:16-17", "note": "The words of the LORD are flawless, like silver purified in a crucible — the psalm's declaration of the purity and reliability of God's word is the OT foundation for the NT's high view of scripture. The flawless-word claim (Ps 12:6) provides the premise that Paul expands in 2 Tim 3:16 into the doctrine of scripture's profitability for correction and training."}
    ]
  },
  "13": {
    "1": [
      {"type": "allusion", "target": "Rev 6:10", "note": "How long, Sovereign Lord, holy and true, until you judge the inhabitants of the earth? — the martyrs under the altar in Revelation 6 cry out with the same 'how long' lament as Psalm 13. The psalmist's prayer from abandonment is the pattern for the eschatological community's cry for justice; the lament form persists from Psalms into the apocalyptic prayer of the vindicated community."}
    ],
    "3": [
      {"type": "allusion", "target": "Eph 5:14", "note": "Wake up, sleeper, rise from the dead, and Christ will shine on you — the psalm's petition 'give light to my eyes, lest I sleep in death' underlies the Ephesians baptismal hymn's call to awaken; the light-giving that rescues from the sleep of death is now associated with Christ's illuminating presence."}
    ]
  },
  "14": {
    "1": [
      {"type": "quote", "target": "Rom 3:10-12", "note": "Paul opens his composite OT catena in Romans 3:10-12 by quoting Psalm 14:1-3 nearly verbatim (LXX): 'There is no one righteous, not even one; there is no one who understands; there is no one who seeks God. All have turned away, they have together become worthless; there is no one who does good, not even one.' The psalm's indictment of the fool's practical atheism is expanded by Paul into a verdict on the universal human condition apart from God's righteousness in Christ."},
      {"type": "theme", "target": "Ps 53:1", "note": "Psalm 14 and Psalm 53 are nearly identical — the same psalm appears twice in the Psalter, Psalm 14 in the Elohist collection and Psalm 53 in a slightly variant form. The doubling underscores the weight of the indictment: the fool's denial of God and the consequent universal moral corruption are a central diagnosis of the human condition in the Psalter's theology."}
    ],
    "7": [
      {"type": "allusion", "target": "Rom 11:26", "note": "The deliverer will come from Zion; he will turn godlessness away from Jacob — Paul quotes Isa 59:20-21 in Romans 11:26 but the Psalm 14:7 hope is the prior grounding: 'Oh, that salvation for Israel would come out of Zion!' The Pauline mystery of Israel's restoration picks up and fulfills the psalmist's eschatological longing."}
    ]
  },
  "15": {
    "1": [
      {"type": "type", "target": "Heb 12:22-24", "note": "LORD, who may dwell in your sanctuary? Who may live on your holy mountain? — the entry requirements of Psalm 15 anticipate the Hebrews announcement that believers have come to Mount Zion, to the heavenly Jerusalem, to the general assembly of the firstborn. The psalm's question about who may ascend the holy mountain receives its NT answer: those who come through Jesus, the mediator of the new covenant."},
      {"type": "allusion", "target": "Matt 5:3-12", "note": "The beatitudes of the Sermon on the Mount describe the character of the kingdom community in terms that echo the psalm's entrance requirements: the one who 'walks blamelessly, does what is right, speaks truth' (Ps 15:2) maps onto the pure in heart and peacemakers. The psalm functions as an OT prototype for the ethical portrait of those who belong to God's holy mountain."}
    ],
    "4": [
      {"type": "allusion", "target": "Jas 5:12", "note": "Who keeps an oath even when it hurts and does not change their mind — James's instruction 'do not swear... let your yes be yes and your no be no' reflects the same ethical standard as the psalm's characterization of the one who may dwell in God's sanctuary. Oath-keeping integrity is a mark of covenant faithfulness in both texts."}
    ],
    "5": [
      {"type": "allusion", "target": "Jas 5:1-6", "note": "Who does not lend money at interest or take a bribe against the innocent — James's condemnation of the rich who have defrauded workers and corrupted justice echoes the psalm's entry requirement of honest economic conduct. The covenant ethics of the holy mountain (no usury, no bribery) become the standard against which James measures the behavior of wealthy community members."}
    ]
  },
  "16": {
    "8": [
      {"type": "fulfillment", "target": "Acts 2:25-28", "note": "I have set the LORD always before me; because he is at my right hand I shall not be shaken — Peter quotes Psalm 16:8-11 in full in his Pentecost sermon as the primary proof-text for the resurrection of Jesus. Peter's argument: David wrote this psalm but David died and his tomb is still with us; therefore the psalm cannot refer to David but to the Messiah, whose soul God would not abandon to Hades."}
    ],
    "10": [
      {"type": "fulfillment", "target": "Acts 2:27", "note": "You will not leave my soul in Hades, or let your Holy One see decay — Peter's decisive citation: the Holy One whose body would not undergo decay cannot be David, who did decay. Only the resurrection of Jesus fulfills the psalm's promise. The LXX 'Holy One' (hosion sou) is taken as a messianic title that points beyond David to the one David prefigured."},
      {"type": "fulfillment", "target": "Acts 13:35", "note": "Paul independently cites Psalm 16:10 in his sermon at Pisidian Antioch with the same argument as Peter: 'you will not let your Holy One see decay.' Both major apostolic speakers apply the text to Jesus's resurrection as its only adequate fulfillment, indicating this was a standard element of early apostolic proclamation from scripture."}
    ],
    "11": [
      {"type": "allusion", "target": "Rev 22:4", "note": "In your presence is complete joy; at your right hand are pleasures that last forever — Revelation's description of the new Jerusalem where God's servants will see his face and serve him captures the eschatological dimension of what the psalmist anticipated as 'pleasures at your right hand forevermore.' The psalm's hope for unending enjoyment of God's presence is realized in the final state."},
      {"type": "allusion", "target": "1 Cor 2:9", "note": "No eye has seen, no ear has heard, no mind has conceived what God has prepared for those who love him — Paul's citation of Isaiah 64:4 (adapted) gathers the same eschatological-pleasure expectation that the psalmist voices; the pleasures at God's right hand are precisely what no created faculty can anticipate."}
    ]
  },
  "17": {
    "8": [
      {"type": "allusion", "target": "Luke 17:21", "note": "Keep me as the apple of your eye; hide me in the shadow of your wings — the protective hiding under the divine wings is the OT image for the covenant God's sheltering of his people; Jesus's lament over Jerusalem (Luke 13:34) uses the same wing-imagery to express his desire to gather the children he would have sheltered."}
    ],
    "15": [
      {"type": "allusion", "target": "1 John 3:2", "note": "When I awake I shall be satisfied with seeing your face; I shall be satisfied with your likeness — John declares: 'we shall see him as he is'; the psalmist's eschatological hope of waking to see God's face and being satisfied with his likeness is the OT ground for the NT's beatific-vision hope. The face-of-God encounter that the psalm anticipates at the resurrection is fulfilled in the parousia-seeing of Christ."},
      {"type": "allusion", "target": "Rev 22:4", "note": "They will see his face, and his name will be on their foreheads — Revelation's closing vision of God's servants seeing his face fulfills what the psalmist longed for: 'when I awake I shall be satisfied with seeing your face.' The psalm's individual eschatological hope becomes the communal eschatological reality of the new creation."},
      {"type": "allusion", "target": "2 Cor 3:18", "note": "Being transformed into his image with ever-increasing glory — Paul's description of progressive transformation into the image (eikōn) of Christ echoes the psalm's hope of satisfaction with the divine likeness (homoia). The psalmist's 'your likeness' becomes in Paul the 'image of Christ' into which believers are transformed by the Spirit."}
    ]
  }
}

def main():
    existing = load_echo('psalms')
    merge_echo(existing, PSALMS_ECHOES)
    save_echo('psalms', existing)
    total_verses = sum(len(v) for v in existing.values())
    print(f'Psalms 9–17 echoes written. {len(existing)} psalms, {total_verses} verses with connections.')

if __name__ == '__main__':
    main()
