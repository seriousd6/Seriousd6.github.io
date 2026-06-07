"""
Echo Layer — Genesis chapters 7–9
Run: python3 scripts/zc-echo-genesis-7-9.py

The Flood narrative and Noahic Covenant. Key echo trajectories:
- The ark as type of salvation: 1 Pet 3:20-21 absorbs the "eight souls through water" typology
- The dove as type of the Holy Spirit: Matt 3:16 / Luke 3:22
- 40 days of rain: the 40-day pattern saturates OT and NT (Elijah, Moses, Jesus)
- The Noahic Covenant: rainbow → Rev 4:3, 10:1; "everlasting covenant" → Heb 13:20
- "Days of Noah" as eschatological cipher: Matt 24:37-39; Luke 17:26-27; 2 Pet 3:3-7
- New creation mandate in ch 9: echoes Great Commission (Matt 28:19) and food law suspension
  (Acts 10:13-15; Mark 7:19)
- No parallels data for chapters 7-9 to absorb.
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
  "7": {
    "1": [
      {"type": "type", "target": "Heb 11:7", "note": "Noah entering the ark 'by faith' to save his household structurally anticipates the pattern of the righteous remnant preserved through judgment — a type Hebrews explicitly applies: 'By faith Noah, being warned of God of things not seen as yet, moved with fear, prepared an ark to the saving of his house.'"},
      {"type": "theme", "target": "1 Pet 3:20", "note": "The call to enter the ark before judgment falls is the narrative frame that 1 Peter 3:20-21 absorbs into its baptism typology — the invitation to safety precedes and enables survival through the waters of judgment."}
    ],
    "7": [
      {"type": "type", "target": "1 Pet 3:20", "note": "Eight souls (<em>oktō psychai</em>) saved through water is the precise echo-point in 1 Pet 3:20-21: 'eight persons were brought safely through water. Baptism, which corresponds to this, now saves you.' The small number of the saved through water becomes the type for Christian baptism as passage through death into new life."}
    ],
    "12": [
      {"type": "shadow", "target": "Matt 4:2", "note": "Forty days and forty nights of rain echo the recurring 40-day wilderness period: Moses on Sinai (Exod 24:18; 34:28), Elijah's flight to Horeb (1 Kgs 19:8), and Jesus's temptation (Matt 4:2; Luke 4:2). The flood's 40 days launches the OT pattern of 40 as a period of trial, testing, or divine provision that culminates in Jesus's messianic temptation."},
      {"type": "theme", "target": "2 Pet 3:6", "note": "The rain that 'came upon the earth forty days and forty nights' (7:12) and ultimately destroyed all life is the specific judgment event 2 Peter 3:6 cites as precedent for the final judgment by fire: 'the world that then existed was deluged with water and perished.'"}
    ],
    "11": [
      {"type": "shadow", "target": "2 Pet 3:5", "note": "The cosmological rupture — all the springs of the great deep bursting forth, floodgates of heaven opening — is the foundational judgment event that 2 Peter 3:5-7 invokes as the pattern for eschatological judgment: 'the world that then existed was deluged with water and perished... the heavens and earth that now exist are stored up for fire.'"}
    ],
    "21": [
      {"type": "shadow", "target": "Matt 24:38", "note": "The total perishing of all flesh outside the ark — 'all flesh died that moved on the earth' (7:21) — is the annihilating scope that Jesus's eschatological discourse invokes: 'they were eating and drinking... until the day when Noah entered the ark, and the flood came and swept them all away. So will be the coming of the Son of Man' (Matt 24:38-39; Luke 17:27)."}
    ],
    "23": [
      {"type": "type", "target": "Luke 17:27", "note": "Only Noah and those with him in the ark survived the destruction of 'every living thing on the face of the ground' (7:23). Jesus uses this total destruction as the paradigm of sudden eschatological judgment that overtakes the unprepared, contrasting those inside (with the Son of Man) and those outside, swept away."}
    ]
  },
  "8": {
    "1": [
      {"type": "theme", "target": "Luke 23:42", "note": "'God remembered Noah' (<em>wayyizkōr</em>) — divine remembrance as the turning point from death to life. The vocabulary of God 'remembering' a person initiates restoration: cf. God remembering Rachel (Gen 30:22), Hannah (1 Sam 1:19), and Israel in slavery (Exod 2:24). The thief's 'remember me when you come into your kingdom' (Luke 23:42) reaches for this same salvific remembrance."},
      {"type": "shadow", "target": "Isa 54:9", "note": "The divine remembrance that ends the flood becomes the explicit type for God's covenant faithfulness in Isa 54:9: 'This is like the days of Noah to me: as I swore that the waters of Noah should no more go over the earth, so I have sworn that I will not be angry with you.'"}
    ],
    "8": [
      {"type": "type", "target": "Matt 3:16", "note": "The dove (<em>yônāh</em>) sent out over the waters of judgment as a scout for habitable land becomes the foundational type for the Holy Spirit descending as a dove at Jesus's baptism (Matt 3:16; Mark 1:10; Luke 3:22; John 1:32). Both dove-events occur immediately after a passage through waters of judgment and mark the beginning of a new creation era."}
    ],
    "11": [
      {"type": "type", "target": "Rom 5:1", "note": "The fresh olive leaf (<em>ʿalêh-zayit</em>) carried back by the dove signals that the judgment is past and peace with the ground is restored. Olive branches are the emblem of peace throughout Scripture; the dove's return with the olive leaf becomes a type of the 'peace with God' (Rom 5:1) that the Spirit announces and produces in those who have passed through baptismal death into resurrection life (cf. 1 Pet 3:20-21)."}
    ],
    "20": [
      {"type": "shadow", "target": "Heb 13:15", "note": "Noah's first act on dry ground is to build an altar and offer burnt offerings of every clean animal and bird (8:20). The sacrifice that arises as a 'pleasing aroma' to the LORD foreshadows the sacrificial system that culminates in Christ's offering of himself (Eph 5:2: 'a fragrant offering and sacrifice to God'). The pattern — deliverance followed immediately by sacrifice and worship — recurs at the Passover, Sinai, and the cross."}
    ],
    "21": [
      {"type": "shadow", "target": "2 Pet 3:9", "note": "'I will never again curse the ground because of man' (8:21) opens the Noahic covenant of common grace — the restraint of universal judgment that persists until the final reckoning. 2 Peter 3:9 interprets this patience: 'The Lord is not slow to fulfill his promise as some count slowness, but is patient toward you, not wishing that any should perish.'"},
      {"type": "shadow", "target": "Jer 33:20", "note": "The fixed order of 'seedtime and harvest, cold and heat, summer and winter, day and night' (8:22) as God's covenant guarantee becomes the basis for Jeremiah's 'fixed order' argument for the certainty of God's covenant promises (Jer 33:20-21, 25-26) — as surely as day follows night, so God's covenant with David will stand."}
    ]
  },
  "9": {
    "1": [
      {"type": "shadow", "target": "Matt 28:19", "note": "'Be fruitful and multiply and fill the earth' (9:1) re-issues the original creation mandate (Gen 1:28) to the post-flood humanity, marking Noah as a new-Adam figure beginning creation afresh. The Great Commission (Matt 28:19-20) echoes this post-resurrection new-creation mandate: Christ, the last Adam (1 Cor 15:45), sends his people to 'fill the earth' with disciples in the power of the Spirit."}
    ],
    "3": [
      {"type": "shadow", "target": "Acts 10:13", "note": "'Every moving thing that lives shall be food for you' (9:3) grants Noah's post-flood humanity a broader food permission than Eden's (Gen 1:29-30). Jesus's declaration that all foods are clean (Mark 7:19) and Peter's vision ('Rise, kill and eat' — Acts 10:13-15) fulfill this trajectory, removing the Levitical distinctions that had qualified the Noahic permission for Israel."},
      {"type": "fulfillment", "target": "Mark 7:19", "note": "Mark glosses Jesus's teaching on defilement with the editorial note 'thus he declared all foods clean' (Mark 7:19), presenting this as a fulfillment and clarification of the principle established in 9:3 — the post-flood permission for all flesh — against which Levitical distinctions were a temporary, pedagogical narrowing."}
    ],
    "6": [
      {"type": "shadow", "target": "Acts 17:26", "note": "'For God made man in his own image' (9:6) grounds the prohibition of murder in the <em>imago Dei</em> — human dignity is not self-generated but derived from divine imaging. Paul's Areopagus speech echoes this (Acts 17:26-28): all humanity from one man, bearing the divine image, is accountable to the one who made them. Christ as the 'image of the invisible God' (Col 1:15) restores and fulfills the image."},
      {"type": "shadow", "target": "John 19:11", "note": "The lex talionis of 9:6 ('by man shall his blood be shed') establishes that the authority over life and death belongs to God, delegated to human courts. Jesus acknowledges this in John 19:11 ('you would have no authority over me at all unless it had been given you from above') — the judicial killing at the cross operates within the same divinely delegated framework that 9:6 establishes."}
    ],
    "9": [
      {"type": "shadow", "target": "Heb 6:13", "note": "God's covenant with Noah (9:9-11) is one of several foundational divine covenants (Abrahamic, Mosaic, Davidic, New) that form the backbone of redemptive history. Hebrews 6:13-20 connects God's covenant oath-making to Christ as 'a sure and steadfast anchor of the soul, a hope that enters into the inner place behind the curtain' — every divine covenant oath reaches its 'Yes' in Christ (2 Cor 1:20)."}
    ],
    "11": [
      {"type": "shadow", "target": "2 Cor 1:20", "note": "'Never again shall all flesh be cut off by the waters of a flood' (9:11) — the covenant promise that common grace will persist until the appointed end. Paul's claim that 'all the promises of God find their Yes in him [Christ]' (2 Cor 1:20) includes this foundational promise: the patience of God in sustaining creation despite human sin is itself a covenant mercy, sustained by Christ, who was appointed heir of all things (Heb 1:2)."}
    ],
    "12": [
      {"type": "shadow", "target": "Rev 4:3", "note": "The rainbow (<em>qešet</em>, 9:12-13) set in the cloud as the sign of the Noahic covenant reappears around the throne of God in John's vision (Rev 4:3: 'a rainbow that had the appearance of an emerald encircled the throne') and on the angel with a little scroll (Rev 10:1). The rainbow migrates from sign of past judgment's end to emblem of the sovereign mercy that governs all things from the divine throne."}
    ],
    "13": [
      {"type": "shadow", "target": "Rev 10:1", "note": "The rainbow in the cloud (9:13) is the covenant sign that God will not again destroy all life — God's restraint of judgment upon a sinful world. Rev 10:1 shows a mighty angel 'wrapped in a cloud, with a rainbow over his head' — the covenant mercy of 9:13 is carried into the eschatological judgment scene as the assurance that God's judgments remain bounded by covenant faithfulness."}
    ],
    "16": [
      {"type": "shadow", "target": "Heb 13:20", "note": "'The everlasting covenant between God and every living creature' (9:16) uses the phrase <em>bĕrît ʿôlām</em> (everlasting/eternal covenant) — the same formula applied to the Abrahamic (Gen 17:7), Mosaic (Lev 24:8), Davidic (2 Sam 23:5), and New Covenant (Jer 32:40; Ezek 37:26) commitments. Heb 13:20 identifies Christ's resurrection as the ratification of 'the eternal covenant' by 'the blood of the eternal covenant,' drawing this entire covenant chain into Christ."}
    ],
    "26": [
      {"type": "shadow", "target": "Luke 3:36", "note": "'Blessed be the LORD, the God of Shem' (9:26) — the blessing on Shem initiates the redemptive genealogical trajectory that runs through Shem → Eber → Terah → Abraham → Isaac → Jacob → Judah → David → Christ. Luke 3:36 includes Shem explicitly in Christ's genealogy, anchoring the messianic line in the post-flood table of nations precisely at the point where Noah's blessing narrowed the promise."}
    ]
  }
}

def main():
    existing = load_echo('genesis')
    merge_echo(existing, GENESIS_ECHOES)
    save_echo('genesis', existing)

    # Verify
    result = load_echo('genesis')
    for ch in [7, 8, 9]:
        n = len(result.get(str(ch), {}))
        print(f'  Ch {ch}: {n} verses with echoes')
    print('Genesis 7–9 echoes written.')

if __name__ == '__main__':
    main()
