"""
Echo data — Psalms chapters 22–27 (gap-fill: only Psalm 26 missing)
Run: python3 scripts/zc-echo-psalms-22-27.py

Psalm 26 is a psalm of integrity and vindication by David — the righteous man
who invites divine examination (v2), washes his hands in innocence (v6), loves
God's dwelling place (v8), and stands in the great congregation (v12).

Key connections:
- v6: David's hand-washing in innocence is the anti-type of Pilate's hand-washing
  (Matt 27:24) — the one who truly could wash his hands in innocence (Christ,
  fully innocent) is condemned by the one who washed his hands in guilt pretending
  innocence. Also connects to Heb 9:14 (Christ's blood that actually cleanses).
- v8: "I love the dwelling place of your house" — parallel to John 2:17 (Jesus'
  zeal for the Father's house consuming him, citing Ps 69:9 but the sentiment
  is precisely this verse).
- v1: "Vindicate me, O LORD" — the vindication prayer answered in the resurrection:
  1 Tim 3:16 ("vindicated by the Spirit"); Acts 2:24 (God vindicating Christ by
  raising him from the dead).
- v2: "Test me, O LORD, and try me" — Heb 4:15 (Christ tested in all things yet
  without sin; the ultimate divine examination passed perfectly).
- v12: "in the great congregation I will praise the LORD" — Heb 12:22-23 (the
  eschatological assembly of the church triumphant).
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

# INTENT: Echo data for Psalm 26 — the integrity psalm whose hand-washing (v6)
#   becomes the anti-type of Pilate's hand-washing (Matt 27:24), whose love of
#   the Temple (v8) is echoed in Jesus' zeal for the Father's house, and whose
#   vindication prayer (v1) is answered in the resurrection (1 Tim 3:16).
# CHANGE? If data/echoes/psalms.json structure changes, update load_echo/save_echo
#   per Z_COMMENTARY_SCRIPT_GUIDE.md.
# VERIFY: python3 -c "import json; d=json.load(open('data/echoes/psalms.json')); print(len(d.get('26',{})), 'verses in ch26')" should print "6 verses in ch26".

PSALMS_ECHOES = {
  "26": {
    "1": [
      {
        "type": "fulfillment",
        "target": "1 Tim 3:16",
        "note": "Vindicate me, O LORD, for I have walked in integrity — the vindication prayer of Psalm 26 is answered in the vindication of Christ. 1 Tim 3:16's confessional fragment includes 'vindicated by the Spirit' (δικαιωθη εν πνευματι) — the resurrection as the Spirit's verdict that Jesus is exactly who he claimed to be. The righteous man's prayer for vindication (Ps 26:1) is the prayer that the cross seems to have denied and the resurrection answers decisively."
      },
      {
        "type": "allusion",
        "target": "Acts 2:24",
        "note": "God raised him from the dead, freeing him from the agony of death, because it was impossible for death to keep its hold on him — Peter's Pentecost sermon presents the resurrection as God's vindication of Jesus against the unjust verdict of the crucifixion. The one who walked in integrity (Ps 26:1) was condemned by human courts; the divine vindication reverses the human verdict."
      }
    ],
    "2": [
      {
        "type": "allusion",
        "target": "Heb 4:15",
        "note": "Test me, O LORD, and try me; examine my heart and my inmost self — David invites the divine examination he knows will vindicate him. Christ undergoes the ultimate divine examination in his earthly life and is found without sin: 'we have one who has been tempted in every way, just as we are — yet he did not sin' (Heb 4:15). The prayer 'test me' is the prayer of the one with nothing to hide, answered in Christ who passes every test the Father allows."
      }
    ],
    "3": [
      {
        "type": "allusion",
        "target": "John 1:14",
        "note": "For your steadfast love (hesed) is before my eyes, and I have conducted myself in your faithfulness — the paired covenant terms hesed and emet (steadfast love and faithfulness/truth) are precisely the pair that John 1:14 applies to the incarnate Word: 'full of grace and truth' (pleres charitos kai aletheias). The LXX rendered hesed as eleos and emet as aletheia; John's 'grace and truth' maps onto David's 'steadfast love and faithfulness.' The one in whom David's hope is grounded arrives as the embodiment of the very character he trusts."
      }
    ],
    "6": [
      {
        "type": "allusion",
        "target": "Matt 27:24",
        "note": "I wash my hands in innocence and take my place at your altar, O LORD — Pilate's hand-washing (Matt 27:24: 'I am innocent of this man's blood') is the ironic anti-type of Psalm 26:6. David washes his hands before the altar as a genuine expression of covenant integrity; Pilate performs the same gesture to declare himself innocent of condemning the genuinely innocent one. The one who truly could make David's declaration (Jesus, the truly innocent man) is condemned by the one who makes it performatively. The psalm's hand-washing exposes the hollow hand-washing of Pilate."
      },
      {
        "type": "allusion",
        "target": "Heb 9:14",
        "note": "I wash my hands in innocence — the hand-washing of innocence David describes is a ritual enacted through external washing. Heb 9:14 announces what actually accomplishes the cleansing David's gesture points to: 'how much more will the blood of Christ, who through the eternal Spirit offered himself unblemished to God, cleanse our consciences from acts that lead to death.' The blood of Christ is the substance of which David's water is the shadow; the cleansed conscience is the reality of which the washed hands are the type."
      }
    ],
    "7": [
      {
        "type": "allusion",
        "target": "Luke 19:37",
        "note": "Lifting my voice in thanksgiving and recounting all your wonderful works — the whole crowd of disciples began joyfully to praise God in loud voices for all the miracles they had seen (Luke 19:37), as Jesus entered Jerusalem. The Palm Sunday acclamation is the great congregation's recounting of the wonderful works, enacting the pattern of Psalm 26:7. The thanksgiving proclamation of the Psalm finds its fullest expression in the community that has witnessed the wonders of the Messiah's ministry."
      }
    ],
    "8": [
      {
        "type": "allusion",
        "target": "John 2:17",
        "note": "LORD, I love the dwelling place of your house and the place where your glory lives — when Jesus clears the Temple, his disciples remember Psalm 69:9 ('zeal for your house will consume me'), but the sentiment of Psalm 26:8 is equally present. Jesus' love for the Father's house that drives him to cleanse it of corruption is the embodied form of the Psalm's confession. John 2:17 presents Jesus' Temple action as the expression of his love for God's dwelling place — the same love the Psalmist confesses."
      },
      {
        "type": "allusion",
        "target": "John 14:2",
        "note": "The place where your glory lives — 'my Father's house has many rooms; if that were not so, would I have told you that I am going there to prepare a place for you?' (John 14:2). Jesus' promise of the Father's house picks up the Psalm's language of the divine dwelling place — the place where God's glory lives. The Psalmist loves the earthly Temple as the place of divine presence; Jesus promises the eschatological dwelling in the Father's house as the permanent fulfilment of what the Temple pointed to."
      }
    ],
    "11": [
      {
        "type": "allusion",
        "target": "Eph 1:7",
        "note": "Redeem me and show me your grace — the double petition at the psalm's close (redemption + grace) is the double gift of the gospel. Eph 1:7: 'in him we have redemption through his blood, the forgiveness of sins, in accordance with the riches of God's grace.' The prayer 'redeem me and show me grace' is the prayer that Christ's atonement answers: the redemption and the grace come through the same act, purchased by the same blood."
      }
    ],
    "12": [
      {
        "type": "allusion",
        "target": "Heb 12:22",
        "note": "My foot stands on level ground; in the great congregation I will praise the LORD — the 'great congregation' (qahal rab) where the vindicated righteous man praises God is the eschatological assembly. Heb 12:22-23: 'you have come to Mount Zion, to the city of the living God, the heavenly Jerusalem... to the general assembly and church of the firstborn, whose names are written in heaven.' The great congregation of Psalm 26 is the earthly shadow of the heavenly assembly that the redeemed enter through Christ."
      }
    ]
  }
}

def main():
    existing = load_echo('psalms')
    merge_echo(existing, PSALMS_ECHOES)
    save_echo('psalms', existing)
    print(f"  ch26 echo entries: {len(existing.get('26', {}))}")
    print("Psalms 22–27 echoes complete.")

if __name__ == '__main__':
    main()
