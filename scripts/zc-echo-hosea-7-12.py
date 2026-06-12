"""
MKT Echo Layer — Hosea chapters 7-12
Run: python3 scripts/zc-echo-hosea-7-12.py

Key NT connections:
- 8:7 sow wind/reap whirlwind: Gal 6:7-8 (sow to flesh/Spirit)
- 8:12 law written but treated as foreign: Jer 31:33/Heb 8:10 (new covenant, law on heart)
- 10:8 call to mountains cover us: Luke 23:30 / Rev 6:16
- 10:12 break up unplowed ground: parable of the sower (Mark 4)
- 11:1 already present (Matt 2:15)
- 11:8 how can I give you up: divine paternal love (Luke 15:20)
- 12:3-4 Jacob wrestling the angel: pre-incarnate Christ (Heb 13:8 / Gen 32)
- 12:10 spoke through prophets: Heb 1:1-2 (God now speaking through his Son)
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

HOSEA_ECHOES = {
  "7": {
    "14": [
      {"type": "allusion", "target": "Matt 6:5-6", "note": "They do not cry to me from their hearts; they merely howl on their beds — Hosea indicts Israel's outward, performative prayer that lacks genuine heart-engagement; Jesus's teaching on prayer (go into your room and pray in secret) addresses the same pathology: prayer that is display rather than genuine communication with the Father"},
    ]
  },
  "8": {
    "7": [
      {"type": "allusion", "target": "Gal 6:7-8", "note": "They have sown the wind and shall reap the whirlwind — Hosea's agricultural sowing-reaping principle applied to covenant violation; Paul applies the same principle in Galatians: the one who sows to his own flesh will from the flesh reap corruption, but the one who sows to the Spirit will reap eternal life. The law is inviolable: the harvest corresponds to the seed"}
    ],
    "12": [
      {"type": "allusion", "target": "Heb 8:10", "note": "Though I wrote for him the great things of my law, they were treated as something foreign — Israel's failure to internalize the written law is the problem the new covenant addresses: I will put my laws into their minds and write them on their hearts (Heb 8:10, citing Jer 31:33). The externally written law that Israel treated as foreign becomes internally inscribed by the Spirit (2 Cor 3:3: written on tablets of human hearts)"}
    ]
  },
  "9": {
    "10": [
      {"type": "allusion", "target": "Mark 11:13", "note": "I found Israel like grapes in the wilderness; your ancestors as the first ripe fruit on a fig tree — YHWH's delight in finding first-fruit Israel; Jesus's cursing of the fig tree with no fruit (Mark 11:13-14) applies the same fruitfulness-expectation: the fig tree should bear fruit; when it does not, it is cursed. The vineyard/fig tree imagery of Hosea 9:10 lies behind Jesus's use of the fig tree as a symbol of Israel's failure to bear the fruit of repentance"}
    ]
  },
  "10": {
    "8": [
      {"type": "fulfillment", "target": "Luke 23:30", "note": "They will say to the mountains, Cover us, and to the hills, Fall on us — Hosea predicts that in the day of judgment, those who made false altars at the high places will cry for the mountains to cover them; Jesus quotes this directly on the way to the cross (Luke 23:30) as a prophecy about Jerusalem's coming destruction in 70 CE, and Revelation 6:16 applies the same cry to the final judgment"},
      {"type": "allusion", "target": "Rev 6:16", "note": "They will say to the mountains, Cover us — the cry of those fleeing divine judgment; Revelation 6:16 (they called to the mountains and rocks: fall on us and hide us from the face of him who sits on the throne) applies Hosea's language of the final judgment: the same cry of those unwilling to face God that Hosea predicts for Israel becomes the universal human response at the end of the age"}
    ],
    "12": [
      {"type": "allusion", "target": "Mark 4:20", "note": "Break up your unplowed ground; for it is time to seek the LORD — the agricultural imagery of prepared versus hardened soil; Hosea calls Israel to till the untilled ground of the heart. The parable of the sower (Mark 4) develops the same diagnostic: different soils produce different results; the good soil (v. 20: those who hear the word and accept it and bear fruit, thirty-, sixty-, and a hundredfold) corresponds to the 'broken-up unplowed ground' Hosea envisions"}
    ]
  },
  "11": {
    "3": [
      {"type": "allusion", "target": "John 1:14", "note": "I taught Ephraim to walk, taking him by the arms; but they did not know that I healed them — the tender image of YHWH as the parent who teaches the child to walk, the one who heals without being recognized; the incarnation makes this care visible and personal: the Word became flesh and dwelt among us (John 1:14), and Jesus heals those who often do not recognize their healer (Luke 17:17-18: the nine lepers who do not return to give thanks)"}
    ],
    "8": [
      {"type": "allusion", "target": "Luke 15:20", "note": "How can I give you up, Ephraim? How can I hand you over, Israel? My heart recoils within me; my compassion grows warm and tender — YHWH's reluctance to judge, the internal divine anguish over the faithless nation; the parable of the prodigal son (Luke 15:20) expresses the same divine paternal anguish and compassion: while he was still a long way off, his father saw him and felt compassion, and ran and embraced him. The father who cannot give up his wayward child is the NT's portrait of the God whom Hosea voices"}
    ],
    "9": [
      {"type": "allusion", "target": "Matt 5:48", "note": "I am God and not a human being — the holy One in your midst; YHWH declares that his restraint from consuming anger is rooted in his divine nature, not human emotion. The NT develops this: God's holiness expressed through Christ is perfect love rather than burning wrath for those in Christ (1 John 4:8); be perfect as your heavenly Father is perfect (Matt 5:48) is the NT's invitation to participate in the divine nature through Christ"}
    ]
  },
  "12": {
    "3": [
      {"type": "allusion", "target": "Gen 32:24", "note": "In the womb he grasped his brother's heel, and in his strength he contended with God — Hosea recalls Jacob's entire life in compressed summary: the heel-grasping birth (Gen 25:26) and the wrestling with God at Peniel (Gen 32:24-30); the wrestler Jacob contended with is identified as the Angel of the LORD/God (Hos 12:4-5), which the NT's angel-Christology (as in Rev 1:14-16; 10:1) identifies with the pre-incarnate Son of God"}
    ],
    "10": [
      {"type": "fulfillment", "target": "Heb 1:1-2", "note": "I spoke through the prophets; I multiplied visions and gave parables through the prophets — YHWH's declaration that he communicated to Israel through multiple prophetic voices and modes; Hebrews 1:1-2 opens by citing this pattern explicitly: long ago, at many times and in many ways, God spoke to our fathers by the prophets, but in these last days he has spoken to us by his Son. Hosea 12:10 identifies the pattern; Hebrews 1:1-2 identifies its culmination and replacement"}
    ]
  }
}

def main():
    existing = load_echo('hosea')
    merge_echo(existing, HOSEA_ECHOES)
    save_echo('hosea', existing)

    print('=== echo Hosea ch7-12 coverage ===')
    for ch in range(7, 13):
        ck = str(ch)
        entries = existing.get(ck, {})
        status = f'done ({len(entries)} verses with entries)' if entries else 'missing'
        print(f'  ch{ch}: {status}')

if __name__ == '__main__':
    main()
