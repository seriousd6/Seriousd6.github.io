"""
Echo Layer — Exodus chapters 36–38
Run: python3 scripts/zc-echo-exodus-36-38-fill.py

Key decisions:
- Ch 36 v.35: the inner veil (parokhet) torn at Christ's death is the chapter's
  primary echo; its construction here is the type, Matt 27:51 / Heb 10:19-20 the fulfillment.
- Ch 37 v.6-9: the kapporeth (mercy seat) = hilasterion (Rom 3:25); Jesus is the mercy
  seat, the place of atoning blood. Two cherubim facing each other → John 20:12 angels
  at the tomb echoes this type.
- Ch 37 v.17: the menorah = Christ as light of the world (John 8:12); Rev 1 lampstands.
- Ch 38 v.1: the bronze altar = the cross — the first object encountered, place of
  blood sacrifice through which alone one approaches God.
- Ch 38 v.8: bronze basin from mirrors → washing/cleansing in Christ (Eph 5:26; Titus 3:5).
- Ch 38 v.21: Heb 8:5 citation — the tabernacle as shadow/copy of the heavenly.
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

EXODUS_ECHOES = {
  "36": {
    "5": [
      {"type": "theme", "target": "2 Cor 9:7", "note": "The Israelites' giving for the tabernacle overflows to the point where Moses must restrain them — 'more than enough' (Exod 36:5-7) — anticipating the NT theology of hilarious generosity: 'God loves a cheerful giver' (2 Cor 9:7). The construction of God's dwelling-place is funded by free, Spirit-prompted overflow, not taxation or compulsion."}
    ],
    "35": [
      {"type": "type", "target": "Matt 27:51", "note": "The inner curtain (parokhet) made here — blue, purple, scarlet, with cherubim woven in — divided the Holy Place from the Most Holy Place, barring ordinary access to the divine presence. At Jesus's death, 'the curtain of the temple was torn in two from top to bottom' (Matt 27:51), the tearing being from above, not below — God's own act removing the barrier. The physical veil constructed in Exodus 36:35 is the type; Christ's torn body is the fulfillment."},
      {"type": "fulfillment", "target": "Heb 10:19-20", "note": "The author of Hebrews explicitly identifies Christ's body with the inner curtain: 'we have confidence to enter the Most Holy Place by the blood of Jesus, by a new and living way opened for us through the curtain, that is, his body' (Heb 10:19-20). The curtain constructed in Exodus 36:35 is not merely analogous to Christ's flesh — the author says it is his flesh; the tabernacle's architecture was always a description of the incarnation."}
    ]
  },
  "37": {
    "6": [
      {"type": "type", "target": "Rom 3:25", "note": "The mercy seat (kapporeth, from kipper = to atone/cover) is the lid of the ark, the specific point where the high priest sprinkled blood on the Day of Atonement (Lev 16:14-15). Paul in Romans 3:25 calls Christ a 'propitiation' (hilastērion) — the Greek word used in the LXX for kapporeth. Jesus is the mercy seat: the place where the atoning blood is applied, where the divine wrath and divine mercy meet, where the ark of the covenant (YHWH's throne) is made accessible through blood."},
      {"type": "allusion", "target": "Heb 9:5", "note": "Hebrews describes the tabernacle's Most Holy Place and names 'the cherubim of glory overshadowing the atonement cover' (Heb 9:5) — deliberately evoking the mercy seat as the center of the whole atonement system, now superseded by Christ who entered the true holy place with his own blood (Heb 9:12)."}
    ],
    "7": [
      {"type": "allusion", "target": "John 20:12", "note": "The two golden cherubim facing each other, looking down at the mercy seat (Exod 37:7-9), are echoed in the two angels at the empty tomb: 'She saw two angels in white, seated where Jesus' body had been, one at the head and the other at the foot' (John 20:12). John's placement of two angels at the head and feet mirrors the two cherubim at the head and feet of the ark; the resurrection is the moment the true mercy seat has received its atoning blood and the cherubim-guardians stand witness."}
    ],
    "17": [
      {"type": "type", "target": "John 8:12", "note": "The golden lampstand (menorah) made as one hammered piece — its light the only illumination in the Holy Place — is the type of Christ as 'the light of the world' (John 8:12). The menorah was never to go out (Lev 24:2 — the 'eternal flame'); Christ is the inextinguishable light who shines in the darkness and the darkness cannot overcome it (John 1:5)."},
      {"type": "allusion", "target": "Rev 1:12-13", "note": "John sees the risen Christ standing among seven golden lampstands (Rev 1:12-13), the image deliberately multiplying the single Mosaic menorah — the Son of Man in the midst of the lampstands is both the source and the guardian of the church's light, as the menorah was the sole light source of the Mosaic sanctuary."}
    ],
    "25": [
      {"type": "shadow", "target": "Heb 7:25", "note": "The incense altar — placed directly before the inner veil, closest to the divine presence — was the altar of perpetual intercession; sweet incense burned morning and evening as the priests went about their service. Heb 7:25 says Christ 'always lives to make intercession' for those who come to God through him, his continuous high-priestly ministry corresponding to the incense that never ceased on the altar before the veil."},
      {"type": "allusion", "target": "Rev 8:3-4", "note": "In Revelation, an angel offers incense with the prayers of all God's people on the golden altar before the throne, and the smoke ascends before God (Rev 8:3-4) — the incense altar of Exodus 37:25 now placed before the heavenly throne, with Christ as the one whose intercession makes all prayer fragrant."}
    ]
  },
  "38": {
    "1": [
      {"type": "type", "target": "Eph 5:2", "note": "The bronze altar of burnt offering — the first object encountered upon entering the tabernacle court, the unavoidable threshold of sacrifice — is the type of the cross. Before anyone could proceed toward the holy place, they passed through the altar of blood. Christ 'gave himself up for us, a fragrant offering and sacrifice to God' (Eph 5:2); access to God still begins at the altar, now the cross. Heb 13:10 makes this explicit: 'we have an altar from which those who minister at the tabernacle have no right to eat.'"},
      {"type": "allusion", "target": "1 Pet 1:19", "note": "The unblemished animals sacrificed on the bronze altar anticipate the 'precious blood of Christ, like that of a lamb without blemish or spot' (1 Pet 1:19). The altar constructed in Exodus 38:1-7 is the structural model for understanding what the cross is: the place where the unblemished offering bears the judgment that should fall on the worshipper."}
    ],
    "8": [
      {"type": "allusion", "target": "Eph 5:26", "note": "The bronze basin made from the mirrors of the serving women — used for the ritual washing of the priests before they approached the altar and entered the tent (Exod 30:20-21) — is a type of the cleansing that precedes access to God. Eph 5:25-26: Christ loved the church and gave himself up for her 'to make her holy, cleansing her by the washing with water through the word.' The priests' washing at the basin is the shadow; the church's washing in Christ is the reality."},
      {"type": "allusion", "target": "Titus 3:5", "note": "The laver at the entrance to the tabernacle, between the altar and the tent, required priestly washing — none could serve in holiness without it. Titus 3:5 describes salvation as 'the washing of regeneration and renewing of the Holy Spirit,' employing the ritual washing imagery of the tabernacle service to describe what Christ has done for those who come to God through him."}
    ],
    "21": [
      {"type": "allusion", "target": "Heb 8:5", "note": "The summary inventory of the tabernacle's materials — 'this is the record of the materials for the tabernacle, the tabernacle of the testimony' — confirms the completion of the earthly copy. Heb 8:5 cites the divine instruction to Moses directly: 'they serve as a shadow and copy of what is in heaven... See to it that you make everything according to the pattern shown you on the mountain.' The detailed construction account of Exodus 36-38 is the documentation of that shadow; Christ is the substance of which it casts the shadow (Col 2:17)."}
    ]
  }
}

def main():
    existing = load_echo('exodus')
    merge_echo(existing, EXODUS_ECHOES)
    save_echo('exodus', existing)
    print('Exodus 36-38 echoes written.')

if __name__ == '__main__':
    main()
