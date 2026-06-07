"""
MKT Echo Layer — Psalms chapters 90–95
Run: python3 scripts/zc-echo-psalms-90-95.py

Psalm 90 (Moses): v4→2 Pet 3:8 (direct quote); v10 seventy years/transience→Heb 9:27;
  v12 number-our-days wisdom→Jas 4:14; v17 establish-work-of-hands→Phil 1:6.
Psalm 91: v11-12→Matt 4:6/Luke 4:10 (Satan QUOTES THIS TO JESUS at the temptation);
  v13 tread-serpent→Luke 10:19/Rom 16:20; v14-15 deliver-and-answer→Heb 5:7.
Psalm 92 (Sabbath psalm): v1→Heb 13:15 (sacrifice of praise); v12-13 righteous-flourish→
  John 15:5.
Psalm 93 (LORD reigns): v1→Rev 19:6 (Lord God Omnipotent reigns); v4 voice-of-waters→
  Rev 1:15; v5 holiness→Rev 4:8/1 Tim 3:15.
Psalms 94 and 95 already have entries — skip.
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
  "90": {
    "4": [
      {
        "type": "quote",
        "target": "2 Pet 3:8",
        "note": "Verse 4 — 'For a thousand years in your sight are but as yesterday when it is past, or as a watch in the night' — is directly quoted in 2 Pet 3:8: 'with the Lord one day is as a thousand years, and a thousand years as one day.' Peter uses Moses' meditation on God's eternity to address the apparent delay of Christ's return: the Lord is not slow in keeping his promise; divine and human timescales are simply incommensurable."
      }
    ],
    "10": [
      {
        "type": "theme",
        "target": "Heb 9:27",
        "note": "Verse 10 — 'The years of our life are seventy, or even by reason of strength eighty; yet their span is but toil and trouble; they are soon gone, and we fly away' — establishes the frailty and brevity of human life under God's judgment. Heb 9:27 draws on the same premise: 'it is appointed for man to die once, and after that comes judgment.' The mortality Moses meditates on is the condition Christ enters and redeems through the resurrection."
      }
    ],
    "12": [
      {
        "type": "theme",
        "target": "Jas 4:14",
        "note": "Verse 12 — 'So teach us to number our days that we may get a heart of wisdom' — is the prayer that life's brevity would produce wisdom rather than vanity. Jas 4:14 picks up the same motif: 'you do not know what tomorrow will bring. What is your life? For you are a mist that appears for a little time and then vanishes.' Both passages call for the same response: living each day in light of eternity rather than presuming on its continuation."
      }
    ],
    "17": [
      {
        "type": "allusion",
        "target": "Phil 1:6",
        "note": "Verse 17 — 'Let the favor of the Lord our God be upon us, and establish the work of our hands upon us' — is Moses' prayer that God would give permanence to human effort. Phil 1:6 answers christologically: 'he who began a good work in you will bring it to completion at the day of Jesus Christ.' The establishing Moses prays for becomes the guarantee the resurrection secures — God does not abandon the work of his hands."
      }
    ]
  },
  "91": {
    "11": [
      {
        "type": "quote",
        "target": "Matt 4:6",
        "note": "Verses 11-12 — 'For he will command his angels concerning you to guard you in all your ways. On their hands they will bear you up, lest you strike your foot against a stone' — are quoted verbatim by Satan in the temptation of Jesus (Matt 4:6; Luke 4:10-11). This is a uniquely significant echo: the psalm about trust in God becomes the text Satan weaponizes to urge Christ to test God. Jesus refuses — not because the promise is false, but because presuming on it would be the opposite of the trust the psalm commends."
      }
    ],
    "13": [
      {
        "type": "fulfillment",
        "target": "Luke 10:19",
        "note": "Verse 13 — 'you will tread on the lion and the adder; the young lion and the serpent you will trample underfoot' — is fulfilled in Christ's authority over evil, which he extends to his disciples. Luke 10:19: 'I have given you authority to tread on serpents and scorpions, and over all the power of the enemy.' Rom 16:20 promises the ultimate fulfillment: 'the God of peace will soon crush Satan under your feet' — the psalm's serpent-treading applied to the eschatological defeat of the adversary."
      }
    ],
    "14": [
      {
        "type": "allusion",
        "target": "Heb 5:7",
        "note": "Verses 14-15 — 'Because he holds fast to me in love, I will deliver him... He shall call to me, and I will answer him; I will be with him in trouble; I will rescue him and honor him' — describe the pattern of divine rescue for the one who trusts God fully. Heb 5:7 applies this to Christ in Gethsemane: 'In the days of his flesh, Jesus offered up prayers and supplications, with loud cries and tears, to him who was able to save him from death, and he was heard because of his reverence.' The psalm's promise of divine response to the trusting sufferer is enacted in the Father's answer to the Son's passion-cry."
      }
    ]
  },
  "92": {
    "1": [
      {
        "type": "theme",
        "target": "Heb 13:15",
        "note": "Verse 1 — 'It is good to give thanks to the LORD, to sing praises to your name, O Most High' — is the Sabbath declaration that all existence is oriented toward God's praise. Heb 13:15 applies this to the new covenant: 'Through him let us continually offer up a sacrifice of praise to God, that is, the fruit of lips that acknowledge his name.' The Sabbath psalm's call to praise becomes, through Christ, a perpetual offering — the Sabbath rest fulfilled in the one who has entered God's rest (Heb 4:10)."
      }
    ],
    "12": [
      {
        "type": "theme",
        "target": "John 15:5",
        "note": "Verses 12-14 — 'The righteous flourish like the palm tree and grow like a cedar in Lebanon... They still bear fruit in old age; they are ever full of sap and green' — describe the flourishing of those planted in God's presence. John 15:5 (Jesus speaking) makes the condition explicit: 'I am the vine; you are the branches. Whoever abides in me and I in him, he it is that bears much fruit.' The enduring fruitfulness the psalm attributes to those in God's house is the life Christ promises to those who remain in him."
      }
    ]
  },
  "93": {
    "1": [
      {
        "type": "fulfillment",
        "target": "Rev 19:6",
        "note": "Verse 1 — 'The LORD reigns; he is robed in majesty; the LORD is robed; he has put on strength as his belt' — is the Psalter's royal declaration that launches the enthronement psalms (93, 96-99). Rev 19:6 is its eschatological answer: 'Hallelujah! For the Lord our God the Almighty reigns.' The acclamation the Psalter anticipates becomes the song of the great multitude at the final victory — Christ's resurrection and exaltation make the reign of God not a hope but a present reality."
      }
    ],
    "4": [
      {
        "type": "allusion",
        "target": "Rev 1:15",
        "note": "Verse 4 — 'Mightier than the thunders of many waters, mightier than the waves of the sea, the LORD on high is mighty' — uses the roar of the cosmic sea as a measure of divine power. Rev 1:15 applies this sonic imagery to the risen Christ: 'his voice was like the roar of many waters.' The God who is mightier than the sea's thunder speaks through the one whose voice is that thunder — the psalm's divine sovereignty is embodied in Christ's person and word."
      }
    ]
  }
}


def main():
    existing = load_echo('psalms')
    merge_echo(existing, PSALMS_ECHOES)
    save_echo('psalms', existing)
    print('Psalms 90-95 echoes written.')

if __name__ == '__main__':
    main()
