"""
MKT Revelation chapter 15 — three-tier translation written directly to draft JSON files.
Run: python3 scripts/mkt-revelation-15-15.py

Translation decisions:
- G4592 (σημεῖον): "sign" (L/M/T) — same word used at Rev 12:1,3; consistent with those renderings
- G2298 (θαυμαστός): "marvellous" / "remarkable" (L/M) / "breathtaking" (T) — the wonders of God
- G2372 (θυμός) vs G3709 (ὀργή): only θυμός appears here (vv.1,7); rendered "wrath" (L/M),
  "righteous fury" (T) — θυμός carries the sense of a burning, active outpouring; it is God's
  enacted judgment, not mere displeasure
- G4127 (πληγή): "plagues" (L/M/T) — consistent with prior Revelation scripts; the word echoes
  the Exodus plagues (G4127 is the LXX word for Egyptian plagues); T surfaces this connection
- G5055 (τελέω / τελέω aorist passive): v.1 "is filled up" / v.8 "were fulfilled" — the same root;
  L/M: "completed" (v.1), "were fulfilled" (v.8); T: "reach their end" (v.1), "run their full course" (v.8)
- G2342 (θηρίον): "beast" (L/M/T) — v.2 reference to the Beast of ch. 13; lowercase in L/M
  consistent with mkt-revelation-7-12.py; the T tier surfaces the political-religious nature
- G5480 (χάραγμα): "mark" (L/M/T) — the mark of the Beast from 13:16–17
- G3686 (ὄνομα): "name" (L/M/T) — "the number of his name"; consistent throughout Revelation
- G1504 (εἰκών): "image" (L/M/T) — the beast's image from 13:14–15
- G5193 (ὑάλινος): "of glass" (L) / "of glass" (M) / "glassy" (T); the sea of glass recalls
  the heavenly firmament of Ezek 1:22 and the throne vision of Rev 4:6
- G4442 (πῦρ) mingled with the sea: "fire" (L/M/T) — the fire-mingled glass evokes both divine
  purity (testing by fire) and the trials the overcomers endured; T surfaces this
- G2788 (κιθάρα): "harps" (L/M) / "lyres" (T) — κιθάρα is a lyre, not the modern harp; but
  "harps of God" is the traditional rendering and M preserves it; T uses "lyres" for precision
- G5603 (ᾠδή): "song" (L/M/T) — "the song of Moses … and the song of the Lamb"; two songs or
  one? The Greek allows a single song with two names; M preserves the ambiguity; T reads as one
  combined canticle, consistent with how the passage functions liturgically
- G3475 (Μωϋσῆς): "Moses" — the servant of God; this links directly to the Exodus typology:
  Israel's song after crossing the sea (Exod 15) prefigures the overcomers' song after the sea of glass
- G721 (ἀρνίον): "Lamb" (capitalised, L/M/T) — divine title, consistent throughout Revelation
- G3841 (παντοκράτωρ): "Almighty" (L/M) / "All-Sovereign" (T) — consistent with mkt-revelation-19-22.py
- G2962 (κύριος) + G2316 (θεός): "Lord God" — the compound divine name; L/M: "Lord God Almighty"
  for the full phrase Κύριε ὁ θεὸς ὁ παντοκράτωρ
- G1342 (δίκαιος) / G228 (ἀληθινός): "just and true" (L/M) — of God's ways; T: "righteous and
  true" — δίκαιος carries both moral uprightness and covenantal faithfulness
- G3598 (ὁδός): "ways" (L/M) / "paths" (T) — God's ways in history; the plural encompasses
  both providential ordering and moral demands
- G3741 (ὅσιος): "holy" (L/M/T) — rendered "holy" here; God alone is ὅσιος, the uniquely sacred
  one; T surfaces the exclusive force
- G1484 (ἔθνος): "nations" (L/M/T) — all peoples will come to worship; eschatological universalism
  of judgment leading to recognition (cf. Ps 86:9; Isa 66:23)
- G1345 (δικαίωμα): "judgments" (L) / "righteous judgments" (M) / "acts of justice" (T) —
  in v.4 δικαιώματά σου are the acts by which God is vindicated; plural, referring to his deeds
- G3485 (ναός) / G4633 (σκηνή): "temple" (L/M/T) for ναός; "tabernacle" for σκηνή — v.5 combines
  both: "the temple of the tabernacle of testimony"; this alludes to the Mosaic Tent of Meeting
  (Exod 40:34-35) where God's glory filled the tent; T makes the Exodus typology explicit
- G3142 (μαρτύριον): "testimony" (L/M) / "the covenant witness" (T) — the ark of the covenant
  was called the "ark of the testimony"; here heaven's sanctuary contains God's covenant witness
- G3043 (λίνον): "linen" (L/M/T) — the priestly/angelic white garment material
- G2513 (καθαρός): "pure" (L/M/T) — consistently rendered throughout Revelation
- G2986 (λαμπρός): "bright/white" (L) / "bright" (M) / "gleaming" (T) — the angels' garments
  are both pure (καθαρός) and radiant (λαμπρός)
- G5552 (χρύσεος): "golden" (L/M/T) — the golden sashes and golden bowls; priestly gold imagery
- G2223 (ζώνη): "girdles" (L) / "sashes" (M/T) — belts/sashes across the chest; high priestly
  garb (cf. Dan 10:5 where a man by the Tigris wears similar attire)
- G4738 (στῆθος): "breasts" (L) / "chests" (M/T) — girded across the chest area
- G5357 (φιάλη): "vials" (L) / "bowls" (M/T) — φιάλη is a broad shallow bowl (libation bowl);
  "bowls" is more accurate than "vials" (which are narrow); L preserves the KJV tradition
- G2226 (ζῷον): "beasts" (L) / "living creatures" (M/T) — the four heavenly beings of Rev 4;
  consistently "living creatures" in M/T to distinguish from θηρίον (the Beast)
- G2198 (ζάω): "liveth" (L) / "lives" (M/T) — "the one who lives forever and ever"
- G165 (αἰών): "for ever and ever" follows the formula εἰς τοὺς αἰῶνας τῶν αἰώνων; consistent
  with mkt-revelation-7-12.py
- G2586 (καπνός): "smoke" (L/M/T) — the temple filled with smoke from God's glory; echoes
  Exod 40:34-35 (the glory filling the Mosaic tabernacle) and Isa 6:4 (the temple filled with
  smoke at Isaiah's commissioning); T surfaces both OT echoes
- G1391 (δόξα): "glory" (L/M/T) — the divine glory; consistently rendered
- G1411 (δύναμις): "power" (L/M/T) — God's power filling the temple alongside his glory
- Aspect notes:
  - v.1 ἐτελέσθη (aorist passive): the wrath of God "is completed" — punctiliar, decisive end point
  - v.2 εἶδον (aorist): "I saw" — a discrete visionary act
  - v.5 ἠνοίγη (aorist passive): "was opened" — the temple opens as a single event
  - v.8 ἐγεμίσθη (aorist passive): "was filled" — sudden, complete filling with smoke
  - v.8 ἠδύνατο (imperfect): "was able" — ongoing inability to enter during the time of plagues
- OT intertextuality:
  - vv.2-4: The sea-crossing + song directly parallels Exod 15 (Song of the Sea after crossing);
    the overcomers are the new Israel who have crossed through the fire-trial into victory
  - v.3 "Moses the servant of God": Exod 14:31; Josh 1:1; Mal 4:4 — the title marks Moses as the
    paradigmatic servant-deliverer; "servant" (δοῦλος) is used of both Moses and the Lamb's followers
  - v.3 "great and marvellous are your works": Ps 111:2; 139:14 — the psalm vocabulary of wonder
    at God's mighty acts
  - v.4 "all nations shall come and worship": Ps 86:9; Isa 66:23 — eschatological pilgrimage motif
  - v.5 "tabernacle of testimony": Exod 40:34-35; Num 17:7-8 — the Tent of Meeting, the place of
    covenant encounter; heaven's sanctuary is the archetype of which the Mosaic was a copy (Heb 8:5)
  - v.8 temple filled with smoke/glory: Exod 40:34-35 (Mosaic tabernacle); 1 Kgs 8:10-11
    (Solomonic temple); Isa 6:1-4 (Isaiah's throne vision) — the triple echo reinforces that this
    is the ultimate fulfilment of every prior theophany
"""

import json, pathlib

ROOT  = pathlib.Path(__file__).parent.parent
DRAFT = ROOT / 'data' / 'translation' / 'draft'

def load(tier, book):
    p = DRAFT / tier / f'{book}.json'
    if p.exists():
        return json.loads(p.read_text())
    return {}

def save(tier, book, data):
    p = DRAFT / tier / f'{book}.json'
    p.write_text(json.dumps(data, ensure_ascii=False, indent=None))
    print(f'  wrote {p.relative_to(ROOT)}')

def merge_tier(existing, new_data, tier_key):
    for ch, verses in new_data.items():
        if ch not in existing:
            existing[ch] = {}
        for v, tiers in verses.items():
            existing[ch][v] = tiers[tier_key]


REVELATION = {
  "15": {
    "1": {
      "L": "And I saw another sign in heaven, great and marvellous: seven angels having the seven last plagues, for in them is filled up the wrath of God.",
      "M": "Then I saw another remarkable sign in heaven: seven angels with the seven last plagues, for with them the wrath of God is completed.",
      "T": "Then I saw another breathtaking sign in heaven: seven angels carrying the seven final plagues — for with these, God's wrath reaches its end."
    },
    "2": {
      "L": "And I saw as it were a sea of glass mingled with fire, and them that had gotten the victory over the beast, and over his image, and over his mark, and over the number of his name, standing on the sea of glass, having the harps of God.",
      "M": "And I saw what appeared to be a sea of glass mixed with fire, and those who had conquered the beast and its image and the number of its name, standing on the glassy sea and holding the harps of God.",
      "T": "I saw what looked like a sea of glass shot through with fire, and standing on it were those who had won the victory over the beast — over its image, its mark, and the number of its name. They stood there holding the lyres of God."
    },
    "3": {
      "L": "And they sing the song of Moses the servant of God, and the song of the Lamb, saying, 'Great and marvellous are thy works, Lord God Almighty; just and true are thy ways, thou King of saints.",
      "M": "They were singing the song of Moses the servant of God and the song of the Lamb: 'Great and marvellous are your works, O Lord God Almighty! Just and true are your ways, O King of the nations.",
      "T": "They sang the song of Moses, God's servant, and the song of the Lamb — one great canticle of the redeemed: 'Magnificent and astonishing are all your works, Lord God All-Sovereign! Your paths through history are righteous and true, O King of every nation."
    },
    "4": {
      "L": "Who shall not fear thee, O Lord, and glorify thy name? for thou only art holy: for all nations shall come and worship before thee; for thy judgments are made manifest.'",
      "M": "Who will not fear you, O Lord, and glorify your name? For you alone are holy, and all nations will come and worship before you, for your righteous judgments have been revealed.'",
      "T": "Who could ever fail to fear you, O Lord, and not give glory to your name? For you alone are truly holy — and all the nations will come and bow before you, because your acts of justice have been laid bare for all to see.'"
    },
    "5": {
      "L": "And after that I looked, and behold, the temple of the tabernacle of the testimony in heaven was opened:",
      "M": "After this I looked, and the temple of the tabernacle of testimony in heaven was opened,",
      "T": "After this vision I looked, and there it was — the inner sanctuary of the heavenly Tabernacle of the Covenant thrown wide open:"
    },
    "6": {
      "L": "And the seven angels came out of the temple, having the seven plagues, clothed in pure and white linen, and having their breasts girded with golden girdles.",
      "M": "and the seven angels with the seven plagues came out of the temple, clothed in pure, bright linen, with golden sashes across their chests.",
      "T": "the seven angels bearing the seven plagues came out of the sanctuary, robed in pure gleaming linen and belted with golden sashes across their chests."
    },
    "7": {
      "L": "And one of the four beasts gave unto the seven angels seven golden vials full of the wrath of God, who liveth for ever and ever.",
      "M": "Then one of the four living creatures gave to the seven angels seven golden bowls filled with the wrath of God, who lives forever and ever.",
      "T": "One of the four living creatures handed to the seven angels seven golden bowls brimming with the wrath of God, who lives throughout all the ages of ages."
    },
    "8": {
      "L": "And the temple was filled with smoke from the glory of God, and from his power; and no man was able to enter into the temple, till the seven plagues of the seven angels were fulfilled.",
      "M": "The temple was filled with smoke from the glory of God and from his power, and no one was able to enter the temple until the seven plagues of the seven angels were fulfilled.",
      "T": "Then the sanctuary was engulfed in smoke rising from the glory and the power of God — the same smoke that had filled Moses' tabernacle, Solomon's temple, and Isaiah's vision of the throne. No one could enter the sanctuary until the seven angels had run the full course of their seven plagues."
    }
  }
}


def main():
    for tier_key, tier_dir in [('L', 'literal'), ('M', 'mediating'), ('T', 'thought')]:
        existing = load(tier_dir, 'revelation')
        merge_tier(existing, REVELATION, tier_key)
        save(tier_dir, 'revelation', existing)
    print('Revelation 15 written.')

if __name__ == '__main__':
    main()
